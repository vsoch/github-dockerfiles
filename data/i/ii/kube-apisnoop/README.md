Kube-apisnoop is a prototype for an MITM based approach that generates k8s API usage allowing us to test addon conformance and prioritize the order that tests should be written.

-  We'd like to map the k8s addons/e2e API requests against the OpenAPI/Swagger definition, including recording invalid/alpha/beta calls.
-  We are transparently proxying k8s API traffic though mitmproxy using an Initializer that modifies iptables and obtains a valid API server cert via k8s CSRs.
-  It's a short step from here to begin writing the inline api coverage tool
-  [High Level Spec for API Coverage Proxy](https://docs.google.com/document/d/1pJAneNJvivUP-J0HL5mLFRjpler-vQSrz1iGRvh_xVg/edit)
-  We should be able to group API calls by pod/container
-  Generating addon API usage logs will allow us to prioritize the order that tests are written. 

# kube-apisnoop

Transparent proxy that observes the Kubernetes API server requests of pods and addons.

Based on kubernetes-tproxy - https://github.com/danisla/kubernetes-tproxy

**N.B. This is currently in its very early stages and is subject to change **

<img src="./docs/images/mitmweb-entries.png" width="800px"></img>

## Requirements

- **Kubernetes** 
    - with **Initializers enabled (alpha feature)** (Tested on GKE v1.9.3-gke.0) 
        - Self-hosted - https://kubernetes.io/docs/admin/extensible-admission-controllers/#enable-initializers-alpha-feature
        - On GKE - https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters
    - with **RBAC disabled (currently)** 
        - On GKE - enable legacy authorization
    - For example, on GKE:

```bash
gcloud container clusters create tproxy-example \
  --zone us-central1-f \
  --machine-type n1-standard-1 \
  --num-nodes 3 \
  --enable-kubernetes-alpha \
  --enable-legacy-authorization \
  --cluster-version 1.9.3
```

- **Helm**

```bash
curl -L https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
helm init
```

- **Kubectl**

```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.9.6/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv ./kubectl /usr/local/bin/
```

- **Docker** - see https://docs.docker.com/install/
- **OpenSSL**

```bash
sudo apt-get update && sudo apt-get install openssl
```


## Setup proxy pods and initializer

### TLDR

Run the following code:

```bash
# Prerequisites:                                                                                                                                
# - An active kubernetes cluster with alpha features and legacy authentication enabled   
# Get the code                                                                                                                                  
git clone https://github.com/ii/kube-apisnoop.git kube-apisnoop
cd kube-apisnoop/
# Make sure Helm is installed                                                                                                                   
helm init --wait
# Create a cert sign request with apiserver DNS and IPs, send to Kubernetes CA to sign                                                          
./create-kubeapi-crt.sh
# Setup a mitmproxy-based pod per node to intercept traffic                                                                                     
./setup-mitm-proxy.sh
# Next deploy an example app that makes apiserver requests using kubectl                                                                        
kubectl apply -f examples/kubectl-app.yaml
# Figure out which node's mitmproxy pod needs to be port forwarded so that intercepted requests can be seen.                                    
./list-pod-nodes.sh
export APP_NODE=$(./list-pod-nodes.sh | grep "^kubectl-app" | awk '{print $2}')
export APP_POD=$(./list-pod-nodes.sh | grep "^kubectl-app" | awk '{print $1}')
export TPROXY_POD=$(./list-pod-nodes.sh | grep "^tproxy-.\+$APP_NODE" | awk '{print $1}')
# Port forward the tproxy pod so we can access it locally                                                                                       
kubectl port-forward $TPROXY_POD 9000:8081 | grep -v "^Handling" &
sleep 3
# Open the web interface to mitmproxy in the default browser                                                                                    
[[ $OSTYPE == linux* ]] && xdg-open http://127.0.0.1:9000
[[ $OSTYPE == darwin* ]] && open http://127.0.0.1:9000
# Apply the annotation to the example pod so that the traffic is intercepted                                                                    
sleep 1
kubectl annotate pod $APP_POD  initializer.kubernetes.io/tproxy=true
kubectl logs $APP_POD  -f --tail=4
```

## Step by step with output

### 1. Clone repo and checkout branch

```bash
git clone https://github.com/ii/kube-apisnoop.git
cd kube-apisnoop
```

### 2. Create a certificate request for mitmproxy and send it to Kubernetes to be signed

```bash
./create-kubeapi-crt.sh
```

**Output:**

```
Generating key
Generating RSA private key, 2048 bit long modulus
[...]
Generating k8s-ca.pem
Generating csr request
Adding CSR to Kubernetes
certificatesigningrequest "k8s-mitm-20180323.222453.ii" created
Approving CSR
certificatesigningrequest "k8s-mitm-20180323.222453.ii" approved
Getting result cert
Done. Heres the result
[...]
```

### 3. Install the proxy pods and initializer using helm
```
./setup-mitm-proxy.sh
```

**Output:**

```
Installing tproxy using helm....
NAME:   tproxy
LAST DEPLOYED: [...]
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/ConfigMap
NAME                       DATA  AGE
tproxy-tproxy              2     4s
tproxy-tproxy-initializer  1     4s
tproxy-tproxy-root-certs   1     4s
[...]
```

## Example deployment

Deploy examples/kubectl-app.yaml to test things out. This deployment repeatedly calls `kubectl get pods` every 5 seconds.

```bash
kubectl apply -f examples/kubectl-app.yaml
```

Find out which node the deployed pod is running on:

```bash
./list-pod-nodes.sh
```

**Example output:**

```
POD                          NODE
kubectl-app-c7556b7f4-lj8px  gke-loomio-ii-nz-default-pool-b70b968b-xj55
tproxy-tproxy-cbgsb          gke-loomio-ii-nz-default-pool-b70b968b-xj55
tproxy-tproxy-scmxq          gke-loomio-ii-nz-default-pool-b70b968b-q5t7
```

Work out which tproxy pod is on the same node as the pod you just deployed. 
In this case, the pod **kubectl-app-c7556b7f4-lj8px** is on the same node as the tproxy pod **tproxy-tproxy-cbgsb**. Your pod names will be different.

Port forward the web interface on the chosen tproxy pod - (in this case it is **tproxy-tproxy-cbgsb**)

```bash
kubectl port-forward tproxy-tproxy-cbgsb 9000:8081
```

Go to the website http://127.0.0.1:9000 for the mitmproxy web interface.

<img src="./docs/images/mitmweb-empty.png" width="800px"></img>

Notice how there are no logging events showing in mitmweb. You can get the logs of the example pod by:

```
kubectl logs kubectl-app-c7556b7f4-lj8px --tail=20
```

Now activate logging by annotating the pod:

```
kubectl annotate pod kubectl-app-c7556b7f4-lj8px  initializer.kubernetes.io/tproxy=true --overwrite
```

You will now see the kubectl api requests logged in mitmweb.

<img src="./docs/images/mitmweb-entries.png" width="800px"></img>

## Tag your own deployments

To observe the API server traffic for a pod, add the following to its spec:

```yaml
metadata:
  annotations:
    "initializer.kubernetes.io/tproxy": "true"
```

Or alternatively, use the following command to annotate an already deployed pod:

```bash
kubectl annotate pod your-pod initializer.kubernetes.io/tproxy=true
```

## Technical architecture

### From https://github.com/danisla/kubernetes-tproxy

<img src="./tproxy_initializers_diagram.png" width="800px"></img>