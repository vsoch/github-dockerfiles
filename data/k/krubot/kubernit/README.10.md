# cert-manager

cert-manager is a Kubernetes addon to automate the management and issuance of
TLS certificates from various issuing sources.

It will ensure certificates are valid and up to date periodically, and attempt
to renew certificates at an appropriate time before expiry.

## Prerequisites

- Kubernetes 1.7+

## Installing the Chart

Full installation instructions, including details on how to configure extra
functionality in cert-manager can be found in the [getting started docs](https://cert-manager.readthedocs.io/en/latest/getting-started/).

To install the chart with the release name `my-release`:

```console
$ helm install --name my-release stable/cert-manager
```

In order to begin issuing certificates, you will need to set up a ClusterIssuer
or Issuer resource (for example, by creating a 'letsencrypt-staging' issuer).

More information on the different types of issuers and how to configure them
can be found in our documentation:

https://cert-manager.readthedocs.io/en/latest/reference/issuers.html

For information on how to configure cert-manager to automatically provision
Certificates for Ingress resources, take a look at the `ingress-shim`
documentation:

https://cert-manager.readthedocs.io/en/latest/reference/ingress-shim.html

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following table lists the configurable parameters of the cert-manager chart and their default values.

| Parameter | Description | Default |
| --------- | ----------- | ------- |
| `image.repository` | Image repository | `quay.io/jetstack/cert-manager-controller` |
| `image.tag` | Image tag | `v0.4.0` |
| `image.pullPolicy` | Image pull policy | `IfNotPresent` |
| `replicaCount`  | Number of cert-manager replicas  | `1` |
| `createCustomResource` | Create CRD/TPR with this release | `true` |
| `clusterResourceNamespace` | Override the namespace used to store DNS provider credentials etc. for ClusterIssuer resources | Same namespace as cert-manager pod
| `leaderElection.Namespace` | Override the namespace used to store the ConfigMap for leader election | Same namespace as cert-manager pod
| `certificateResourceShortNames` | Custom aliases for Certificate CRD | `["cert", "certs"]` |
| `extraArgs` | Optional flags for cert-manager | `[]` |
| `extraEnv` | Optional environment variables for cert-manager | `[]` |
| `rbac.create` | If `true`, create and use RBAC resources | `true` |
| `serviceAccount.create` | If `true`, create a new service account | `true` |
| `serviceAccount.name` | Service account to be used. If not set and `serviceAccount.create` is `true`, a name is generated using the fullname template |  |
| `resources` | CPU/memory resource requests/limits | `requests: {cpu: 10m, memory: 32Mi}` |
| `nodeSelector` | Node labels for pod assignment | `{}` |
| `affinity` | Node affinity for pod assignment | `{}` |
| `tolerations` | Node tolerations for pod assignment | `[]` |
| `ingressShim.defaultIssuerName` | Optional default issuer to use for ingress resources |  |
| `ingressShim.defaultIssuerKind` | Optional default issuer kind to use for ingress resources |  |
| `ingressShim.defaultACMEChallengeType` | Optional default challenge type to use for ingresses using ACME issuers |  |
| `ingressShim.defaultACMEDNS01ChallengeProvider` | Optional default DNS01 challenge provider to use for ingresses using ACME issuers with DNS01 |  |
| `podAnnotations` | Annotations to add to the cert-manager pod | `{}` |
| `podDnsPolicy` | Optional cert-manager pod [DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pods-dns-policy) |  |
| `podDnsConfig` | Optional cert-manager pod [DNS configurations](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pods-dns-config) |  |
| `podLabels` | Labels to add to the cert-manager pod | `{}` |
| `http_proxy` | Value of the `HTTP_PROXY` environment variable in the cert-manager pod | |
| `https_proxy` | Value of the `HTTPS_PROXY` environment variable in the cert-manager pod | |
| `no_proxy` | Value of the `NO_PROXY` environment variable in the cert-manager pod | |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install --name my-release -f values.yaml .
```
> **Tip**: You can use the default [values.yaml](values.yaml)

## Contributing

This chart is maintained at [github.com/jetstack/cert-manager](https://github.com/jetstack/cert-manager/tree/master/contrib/charts/cert-manager).
# prometheus-operator

Installs [prometheus-operator](https://github.com/coreos/prometheus-operator) to create/configure/manage Prometheus clusters atop Kubernetes.

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/prometheus-operator
```

## Introduction

This chart bootstraps a [prometheus-operator](https://github.com/coreos/prometheus-operator) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.8+ with Beta APIs

### RBAC
If role-based access control (RBAC) is enabled in your cluster, you may need to give Tiller (the server-side component of Helm) additional permissions. **If RBAC is not enabled, be sure to set `rbacEnable` to `false` when installing the chart.**

1. Create a ServiceAccount for Tiller in the `kube-system` namespace
```console
$ kubectl -n kube-system create sa tiller
```

2. Create a ClusterRoleBinding for Tiller
```console
$ kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```

3. Install Tiller, specifying the new ServiceAccount
```console
$ helm init --service-account tiller
```

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install --name my-release coreos/prometheus-operator
```

The command deploys prometheus-operator on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the prometheus-operator chart and their default values.

Parameter | Description | Default
--- | --- | ---
`configmapReload.repository` | configmap-reload image | `quay.io/coreos/configmap-reload`
`configmapReload.tag` | configmap-reload tag | `v0.0.1`
`global.hyperkube.repository` | Hyperkube image | `quay.io/coreos/hyperkube`
`global.hyperkube.tag` | Hyperkube image tag | `v1.7.6_coreos.0`
`global.hyperkube.pullPolicy` | Hyperkube image pull policy | `IfNotPresent`
`image.repository` | Image | `quay.io/coreos/prometheus-operator`
`image.tag` | Image tag | `v0.19.0`
`image.pullPolicy` | Image pull policy | `IfNotPresent`
`kubeletService.enable` | If true, the operator will create a service for scraping kubelets | `true`
`kubeletService.namespace` | The namespace in which the kubelet service should be created | `kube-system`
`kubeletService.name` | The name of the kubelet service to be created | `kubelet`
`nodeSelector` | Node labels for pod assignment | `{}`
`prometheusConfigReloader.repository` | prometheus-config-reloader image | `quay.io/coreos/prometheus-config-reloader`
`prometheusConfigReloader.tag` | prometheus-config-reloader tag | `v0.0.4`
`rbacEnable` | If true, create & use RBAC resources | `true`
`resources` | Pod resource requests & limits | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```console
$ helm install --name my-release coreos/prometheus-operator --set sendAnalytics=true
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install --name my-release coreos/prometheus-operator -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)
# Grafana Helm Chart

* Installs the web dashboarding system [Grafana](http://grafana.org/)

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/grafana
```
## Introduction

This chart bootstraps an [Grafana](http://grafana.org) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager, and preinstalled some defaut dashboard for dashboarding Kubernetes metrics.

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install --name my-release coreos/grafana
```

## Uninstalling the Chart

To uninstall/delete the my-release deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.


## Configuration

Parameter | Description | Default
--- | --- | ---
`routePrefix` | Prefix used to register routes | `"/"`
`auth.anonymous.enabled` | If true, enable anonymous authentication | `true`
`adminUser` | Grafana admin user name | `admin`
`adminPassword` | Grafana admin user password | `admin`
`image.repository` | Image | `grafana/grafana`
`image.tag` | Image tag | `4.4.1`
`extraVars` | Pass extra environment variables to the Grafana container. | `{}`
`grafanaWatcher.repository` | Image | `quay.io/coreos/grafana-watcher`
`grafanaWatcher.tag` | Image tag | `v0.0.8`
`ingress.enabled` | If true, Grafana Ingress will be created | `false`
`ingress.annotations` | Annotations for Grafana Ingress | `{}`
`ingress.labels` | Labels for Grafana Ingress | `{}`
`ingress.hosts` | Grafana Ingress fully-qualified domain names | `[]`
`ingress.tls` | TLS configuration for Grafana Ingress | `[]`
`nodeSelector` | Node labels for pod assignment | `{}`
`resources` | Pod resource requests & limits | `{}`
`service.annotations` | Annotations to be added to the Grafana Service | `{}`
`service.clusterIP` | Cluster-internal IP address for Grafana Service | `""`
`service.externalIPs` | List of external IP addresses at which the Grafana Service will be available | `[]`
`service.labels` | Labels for Grafana Service | `{}`
`service.loadBalancerIP` | External IP address to assign to Grafana Service | `""`
`service.loadBalancerSourceRanges` | List of client IPs allowed to access Grafana Service | `[]`
`service.nodePort` | Port to expose Grafana Service on each node | `30902`
`service.type` | Grafana Service type | `ClusterIP`
`storageSpec` | Grafana StorageSpec for persistent data | `{}`
`resources` | Pod resource requests & limits | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,
$ helm install coreos/grafana --name my-release --set adminUser=bob
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install coreos/grafana --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

> **Tip**: On GCE If you want to  use  `Ingress.enabled=true`, you must put `service.type=NodePort`

## Adding Grafana Dashboards

You can either add new dashboards via `serverDashboardConfigmaps` in `values.yaml`. These can then be
picked up by Grafana Watcher.

```yaml
serverDashboardConfigmaps:
  - example-dashboards
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-dashboards
data:
{{ (.Files.Glob "custom-dashboards/*.json").AsConfig | indent 2 }}

# Or
#
# data:
#   custom-dashboard.json: |-
# {{ (.Files.Get "custom.json") | indent 4 }}
#
# The filename (and consequently the key under data) must be in the format `xxx-dashboard.json` or `xxx-datasource.json`
# for them to be picked up.
```

Another way is to add them through `serverDashboardFiles` directly in `values.yaml`. These are then combined
into the same ConfigMap for the rest of the default dashboards.

```yaml
serverDashboardFiles:
  example-dashboard.json: |-
    {
      "dashboard": {
        "annotations:[]
        ...
      }
    }
```

In both cases, if you're exporting the jsons directly from Grafana, you'll want to wrap it in `{"dashboard": {}}`
as stated in [Grafana Watcher's README](https://github.com/coreos/prometheus-operator/tree/master/contrib/grafana-watcher).
# kube-prometheus

This is the helm chart equivalent of `contrib/kube-prometheus`.

# Prerequisites

Requires helm >= 2.5.0
# alertmanager

Installs a [Prometheus](https://prometheus.io) Alertmanager instance using the CoreOS [prometheus-operator](https://github.com/coreos/prometheus-operator).

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/alertmanager
```

## Introduction

This chart bootstraps an [Alertmanager](https://github.com/prometheus/alertmanager) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.4+ with Beta APIs & ThirdPartyResources enabled
  - [prometheus-operator](https://github.com/coreos/prometheus-operator/blob/master/helm/prometheus-operator/README.md).

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install coreos/alertmanager --name my-release
```

The command deploys Alertmanager  on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the alertmanager chart and their default values.

Parameter | Description | Default
--- | --- | ---
`config` | Alertmanager configuration directives | `{}`
`externalUrl` | External URL at which Alertmanager will be reachable | `""`
`routePrefix` | Prefix used to register routes | `"/"`
`image.repository` | Image | `quay.io/prometheus/alertmanager`
`image.tag` | Image tag | `v0.12.0`
`ingress.enabled` | If true, Alertmanager Ingress will be created | `false`
`ingress.annotations` | Annotations for Alertmanager Ingress` | `{}`
`ingress.labels` | Labels for Alertmanager Ingress` | `{}`
`ingress.hosts` | Alertmanager Ingress hosts | `[]`
`ingress.tls` | TLS configuration for Alertmanager Ingress | `[]`
`nodeSelector` | Node labels for pod assignment | `{}`
`paused` | If true, the Operator won't process any Alertmanager configuration changes | `false`
`podAntiAffinity` | If "soft", the scheduler attempts to place Alertmanager replicas on different nodes. If "hard" the scheduler is required to place them on different nodes. If "" (empty) then no anti-affinity rules will be configured. | `soft`
`prometheusRules` | Prometheus rules | `[templates/alertmanager.rules.yaml](templates/alertmanager.rules.yaml)`
`replicaCount` | Number of Alertmanager replicas desired | `1`
`resources` | Pod resource requests & limits | `{}`
`service.annotations` | Annotations to be added to the Alertmanager Service | `{}`
`service.clusterIP` | Cluster-internal IP address for Alertmanager Service | `""`
`service.externalIPs` | List of external IP addresses at which the Alertmanager Service will be available | `[]`
`service.loadBalancerIP` | External IP address to assign to Alertmanager Service | `""`
`service.loadBalancerSourceRanges` | List of client IPs allowed to access Alertmanager Service | `[]`
`service.nodePort` | Port to expose Alertmanager Service on each node | `39093`
`service.type` | Alertmanager Service type | `ClusterIP`
`storageSpec` | Alertmanager StorageSpec for persistent data | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,
$ helm install coreos/alertmanager --name my-release --set externalUrl=http://alertmanager.example.com
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install coreos/alertmanager --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

### CRD Resource Documentation
- [Alertmanager](/Documentation/design.md#alertmanager)
- [Prometheus](/Documentation/design.md#prometheus)
- [ServiceMonitor](/Documentation/design.md#servicemonitor)
# prometheus

Installs a [Prometheus](https://prometheus.io) instance using the CoreOS [prometheus-operator](https://github.com/coreos/prometheus-operator).

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/prometheus
```

## Introduction

This chart bootstraps a [Prometheus](https://github.com/prometheus/prometheus) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.4+ with Beta APIs & ThirdPartyResources enabled
  - [prometheus-operator](https://github.com/coreos/prometheus-operator/blob/master/helm/prometheus-operator/README.md).

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install coreos/prometheus --name my-release
```

The command deploys Prometheus on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the prometheus chart and their default values.

Parameter | Description | Default
--- | --- | ---
`alertingEndpoints` | Alertmanagers to which alerts will be sent | `[]`
`config` | Prometheus configuration directives | `{}`
`externalLabels` | The labels to add to any time series or alerts when communicating with external systems  | `{}`
`externalUrl` | External URL at which Prometheus will be reachable | `""`
`routePrefix` | Prefix used to register routes | `"/"`
`image.repository` | Image | `quay.io/prometheus/prometheus`
`image.tag` | Image tag | `v2.2.1`
`ingress.enabled` | If true, Prometheus Ingress will be created | `false`
`ingress.annotations` | Annotations for Prometheus Ingress` | `{}`
`ingress.labels` | Labels for Prometheus Ingress | `{}`
`ingress.hosts` | Prometheus Ingress fully-qualified domain names | `[]`
`ingress.tls` | TLS configuration for Prometheus Ingress | `[]`
`nodeSelector` | Node labels for pod assignment | `{}`
`paused` | If true, the Operator won't process any Prometheus configuration changes | `false`
`podAntiAffinity` | If "soft", the scheduler attempts to place Prometheus replicas on different nodes. If "hard" the scheduler is required to place them on different nodes. If "" (empty) then no anti-affinity rules will be configured. | `soft`
`prometheusRules` | Prometheus rules | `[templates/prometheus.rules.yaml](templates/prometheus.rules.yaml)`
`replicaCount` | Number of Prometheus replicas desired | `1`
`remoteRead` | The remote_read spec configuration for Prometheus | `{}`
`remoteWrite` | The remote_read spec configuration for Prometheus | `{}`
`resources` | Pod resource requests & limits | `{}`
`retention` | How long to retain metrics | `24h`
`routePrefix` | Prefix used to register routes, overriding externalUrl route | `/`
`rules` | Prometheus alerting & recording rules | `{}`
`ruleNamespaceSelector` | Namespaces to be selected for PrometheusRules discovery | `{}`
`rulesSelector` | Rules CRD selector | `{}`
`secrets` | List of Secrets in the same namespace as the Prometheus object, which shall be mounted into the Prometheus Pods. | `{}`
`service.annotations` | Annotations to be added to the Prometheus Service | `{}`
`service.clusterIP` | Cluster-internal IP address for Prometheus Service | `""`
`service.externalIPs` | List of external IP addresses at which the Prometheus Service will be available | `[]`
`service.loadBalancerIP` | External IP address to assign to Prometheus Service | `""`
`service.loadBalancerSourceRanges` | List of client IPs allowed to access Prometheus Service | `[]`
`service.nodePort` | Port to expose Prometheus Service on each node | `39090`
`service.type` | Prometheus Service type | `ClusterIP`
`serviceMonitors` | ServiceMonitor crd resources to create & be scraped by this Prometheus instance | `[]`
`serviceMonitorsSelector` | ServiceMonitor ConfigMap selector | `{}`
`storageSpec` | Prometheus StorageSpec for persistent data | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,
$ helm install coreos/prometheus --name my-release --set externalUrl=http://prometheus.example.com


Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example:

```console
$ helm install coreos/prometheus --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)


### Service Monitors

Custom service monitors can be added in values.yaml in the `serviceMonitors` section. Please refere to `values.yaml` for all available parameters.


#### Example service monitor


This example Service Monitor will monitor applications matching `app: nginx-ingress`. The port `metrics` will be scraped with the path `/merics`. The endpoint will be scraped every 30 seconds.

```
serviceMonitors:
  - name: kube-prometheus-nginx-ingress
    labels:
      prometheus: kube-prometheus
    selector:
      matchLabels:
        app: nginx-ingress
    endpoints:
      - port: metrics
        interval: 30s
        path: /metrics
    namespaceSelector:
      any: true
```

### CRD Resource Documentation
- [Alertmanager](/Documentation/design.md#alertmanager)
- [Prometheus](/Documentation/design.md#prometheus)
- [ServiceMonitor](/Documentation/design.md#servicemonitor)
# Flux

Flux is a tool that automatically ensures that the state of a cluster matches the config in git.
It uses an operator in the cluster to trigger deployments inside Kubernetes, which means you don't need a separate CD tool.
It monitors all relevant image repositories, detects new images, triggers deployments and updates the desired running
configuration based on that (and a configurable policy).

## Introduction

This chart bootstraps a [Flux](https://github.com/weaveworks/flux) deployment on
a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites

- Kubernetes 1.9+

## Installation

We put together a simple [Get Started
guide](../../site/helm/get-started.md) which takes about 5-10 minutes to follow.
You will have a fully working Flux installation deploying workloads to your
cluster.

## Installing Flux using Helm

### Installing the Chart

Add the weaveworks repo:

```sh
helm repo add weaveworks https://weaveworks.github.io/flux
```

#### To install the chart with the release name `flux`:

```console
$ helm install --name flux \
--set git.url=ssh://git@github.com/weaveworks/flux-example \
--namespace flux \
weaveworks/flux
```

#### To connect Flux to a Weave Cloud instance:

```console
helm install --name flux \
--set token=YOUR_WEAVE_CLOUD_SERVICE_TOKEN \
--namespace flux \
weaveworks/flux
```

#### To install Flux with the Helm operator (alpha version):

```console
$ helm install --name flux \
--set git.url=ssh://git@github.com/weaveworks/flux-helm-test \
--set helmOperator.create=true \
--namespace flux \
weaveworks/flux
```

#### To install Flux with a private git host:

When using a private git host, setting the `ssh.known_hosts` variable 
is required for enabling successful key matches because `StrictHostKeyChecking` 
is enabled during flux git daemon operations.

By setting the `ssh.known_hosts` variable, a configmap will be created
called `flux-ssh-config` which in turn will be mounted into a volume named
`sshdir` at `/root/.ssh/known_hosts`.

* Get the `ssh.known_hosts` keys by running the following command:

```bash
ssh-keyscan <your_git_host_domain>
```

To prevent a potential man-in-the-middle attack, one should
verify the ssh keys acquired through the `ssh-keyscan` match expectations
using an alternate mechanism.

* Start flux and flux helm operator:

  - Using a string for setting `known_hosts`
  
    ```sh
    YOUR_GIT_HOST=your_git_host.example.com
    KNOWN_HOSTS='domain ssh-rsa line1
    domain ecdsa-sha2-line2
    domain ssh-ed25519 line3'
    
    helm install \
    --name flux \
    --set helmOperator.create=true \
    --set git.url="ssh://git@${YOUR_GIT_HOST}:weaveworks/flux-helm-test.git" \
    --set-string ssh.known_hosts="${KNOWN_HOSTS}" \
    --namespace flux \
    chart/flux 
    ```
    
  - Using a file for setting `known_hosts`
  
    Copy known_hosts keys into a temporary file `/tmp/flux_known_hosts`
    
    ```sh
    YOUR_GIT_HOST=your_git_host.example.com
    
    helm install \
    --name flux \
    --set helmOperator.create=true \
    --set git.url="ssh://git@${YOUR_GIT_HOST}:weaveworks/flux-helm-test.git" \
    --set-file ssh.known_hosts=/tmp/flux_known_hosts \
    --namespace flux \
    chart/flux 
    ```

The [configuration](#configuration) section lists all the parameters that can be configured during installation.

#### Setup Git deploy

At startup Flux generates a SSH key and logs the public key.
Find the SSH public key with:

```bash
kubectl -n flux logs deployment/flux | grep identity.pub | cut -d '"' -f2
```

In order to sync your cluster state with GitHub you need to copy the public key and
create a deploy key with write access on your GitHub repository.
Go to _Settings > Deploy keys_ click on _Add deploy key_, check
_Allow write access_, paste the Flux public key and click _Add key_.

### Uninstalling the Chart

To uninstall/delete the `flux` deployment:

```console
helm delete --purge flux
```

The command removes all the Kubernetes components associated with the chart and deletes the release.
You should also remove the deploy key from your GitHub repository.

### Configuration

The following tables lists the configurable parameters of the Weave Flux chart and their default values.

| Parameter                       | Description                                | Default                                                    |
| ------------------------------- | ------------------------------------------ | ---------------------------------------------------------- |
| `image.repository` | Image repository | `quay.io/weaveworks/flux`
| `image.tag` | Image tag | `1.3.1`
| `image.pullPolicy` | Image pull policy | `IfNotPresent`
| `resources` | CPU/memory resource requests/limits | None
| `rbac.create` | If `true`, create and use RBAC resources | `true`
| `serviceAccount.create` | If `true`, create a new service account | `true`
| `serviceAccount.name` | Service account to be used | `flux`
| `service.type` | Service type to be used (exposing the Flux API outside of the cluster is not advised) | `ClusterIP`
| `service.port` | Service port to be used | `3030`
| `git.url` | URL of git repo with Kubernetes manifests | None
| `git.branch` | Branch of git repo to use for Kubernetes manifests | `master`
| `git.path` | Path within git repo to locate Kubernetes manifests (relative path) | None
| `git.user` | Username to use as git committer | `Weave Flux`
| `git.email` | Email to use as git committer | `support@weave.works`
| `git.chartsPath` | Path within git repo to locate Helm charts (relative path) | `charts`
| `git.pollInterval` | Period at which to poll git repo for new commits | `30s`
| `ssh.known_hosts`  | The contents of an SSH `known_hosts` file, if you need to supply host key(s) |
| `helmOperator.create` | If `true`, install the Helm operator | `false`
| `helmOperator.repository` | Helm operator image repository | `quay.io/weaveworks/helm-operator`
| `helmOperator.tag` | Helm operator image tag | `0.1.0-alpha`
| `helmOperator.pullPolicy` | Helm operator image pull policy | `IfNotPresent`
| `helmOperator.logReleaseDiffs` | Helm operator should log the diff when a chart release diverges (possibly insecure) | `false`
| `helmOperator.tillerNamespace` | Namespace in which the Tiller server can be found | `kube-system`
| `helmOperator.tls.enable` | Enable TLS for communicating with Tiller | `false`
| `helmOperator.tls.verify` | Verify the Tiller certificate, also enables TLS when set to true | `false`
| `helmOperator.tls.secretName` | Name of the secret containing the TLS client certificates for communicating with Tiller | `helm-client-certs`
| `helmOperator.tls.keyFile` | Name of the key file within the k8s secret | `tls.key`
| `helmOperator.tls.certFile` | Name of the certificate file within the k8s secret | `tls.crt`
| `helmOperator.tls.caContent` | Certificate Authority content used to validate the Tiller server certificate | None
| `token` | Weave Cloud service token | None

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example:

```console
$ helm upgrade --install --wait flux \
--set git.url=ssh://git@github.com/stefanprodan/podinfo \
--set git.path=deploy/auto-scaling \
--namespace flux \
weaveworks/flux
```

### Upgrade

Update Weave Flux version with:

```console
helm upgrade --reuse-values flux \
--set image.tag=1.3.2 \
weaveworks/flux
```

### Installing Weave Flux helm-operator and Helm with TLS enabled

#### Installing Helm / Tiller

Generate certificates for Tiller and Flux. This will provide a CA, server certs for tiller and client certs for helm / weave flux.

The following script can be used for that (requires [cfssl](https://github.com/cloudflare/cfssl)):

```bash
export TILLER_HOSTNAME=tiller-server
export TILLER_SERVER=server
export USER_NAME=flux-helm-operator

mkdir tls
cd ./tls

# Prep the configuration
echo '{"CN":"CA","key":{"algo":"rsa","size":4096}}' | cfssl gencert -initca - | cfssljson -bare ca -
echo '{"signing":{"default":{"expiry":"43800h","usages":["signing","key encipherment","server auth","client auth"]}}}' > ca-config.json

# Create the tiller certificate
echo '{"CN":"'$TILLER_SERVER'","hosts":[""],"key":{"algo":"rsa","size":4096}}' | cfssl gencert \
  -config=ca-config.json -ca=ca.pem \
  -ca-key=ca-key.pem \
  -hostname="$TILLER_HOSTNAME" - | cfssljson -bare $TILLER_SERVER

# Create a client certificate
echo '{"CN":"'$USER_NAME'","hosts":[""],"key":{"algo":"rsa","size":4096}}' | cfssl gencert \
  -config=ca-config.json -ca=ca.pem -ca-key=ca-key.pem \
  -hostname="$TILLER_HOSTNAME" - | cfssljson -bare $USER_NAME
```

Alternatively, you can follow the [Helm documentation for configuring TLS](https://docs.helm.sh/using_helm/#using-ssl-between-helm-and-tiller).

Next deploy Helm with TLS and RBAC enabled;

Create a file called `helm-rbac.yaml`. This contains all the RBAC configuration for Tiller:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system

---
# Helm client serviceaccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: Role
metadata:
  name: tiller-user
  namespace: kube-system
rules:
- apiGroups:
  - ""
  resources:
  - pods/portforward
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - list
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: RoleBinding
metadata:
  name: tiller-user-binding
  namespace: kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: tiller-user
subjects:
- kind: ServiceAccount
  name: helm
  namespace: kube-system
```

Deploy Tiller:

```bash
kubectl apply -f helm-rbac.yaml

# Deploy helm with mutual TLS enabled
helm init --upgrade --service-account tiller \
    --override 'spec.template.spec.containers[0].command'='{/tiller,--storage=secret}' \
    --tiller-tls \
    --tiller-tls-cert ./tls/server.pem \
    --tiller-tls-key ./tls/server-key.pem \
    --tiller-tls-verify \
    --tls-ca-cert ./tls/ca.pem
```

To check if Tiller installed succesfully with TLS enabled, try `helm ls`. This should give an error:

```bash
# Should give an error
$ helm ls
Error: transport is closing
```

When providing the certificates, it should work correctly:

```bash
helm --tls \
  --tls-ca-cert ./tls/ca.pem \
  --tls-cert ./tls/flux-helm-operator.pem \
  --tls-key ././tls/flux-helm-operator-key.pem \
  ls
```

### deploy weave flux helm-operator

First create a new Kubernetes TLS secret for the client certs;

```bash
kubectl create secret tls helm-client --cert=tls/flux-helm-operator.pem --key=./tls/flux-helm-operator-key.pem
```

> note; this has to be in the same namespace as the helm-operator is deployed in.

Deploy flux with Helm;

```bash
helm repo add weaveworks https://weaveworks.github.io/flux

helm upgrade --install \
    --set helmOperator.create=true \
    --set git.url=$YOUR_GIT_REPO \
    --set helmOperator.tls.enable=true \
    --set helmOperator.tls.verify=true \
    --set helmOperator.tls.secretName=helm-client \
    --set helmOperator.tls.caContent="$(cat ./tls/ca.pem)" \
    flux \
    weaveworks/flux
```

#### Check if it worked

Use `kubectl logs` on the helm-operator and observe the helm client being created.

#### Debugging

##### Error creating helm client: failed to append certificates from file: /etc/fluxd/helm-ca/ca.crt

Your CA certificate content is not set correctly, check if your configMap contains the correct values. Example:

```bash
$ kubectl get configmaps flux-helm-tls-ca-config -o yaml
apiVersion: v1
data:
  ca.crt: |
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
kind: ConfigMap
metadata:
  creationTimestamp: 2018-07-04T15:27:25Z
  name: flux-helm-tls-ca-config
  namespace: helm-system
  resourceVersion: "1267257"
  selfLink: /api/v1/namespaces/helm-system/configmaps/flux-helm-tls-ca-config
  uid: c106f866-7f9e-11e8-904a-025000000001
```
