# CockroachDB Helm Chart

## Prerequisites Details
* Kubernetes 1.8
* PV support on the underlying infrastructure
* If you want to secure your cluster to use TLS certificates for all network
  communication, [Helm must be installed with RBAC
  privileges](https://github.com/kubernetes/helm/blob/master/docs/rbac.md)
  or else you will get an "attempt to grant extra privileges" error.

## StatefulSet Details
* http://kubernetes.io/docs/concepts/abstractions/controllers/statefulsets/

## StatefulSet Caveats
* http://kubernetes.io/docs/concepts/abstractions/controllers/statefulsets/#limitations

## Chart Details

This chart will do the following:

* Set up a dynamically scalable CockroachDB cluster using a Kubernetes StatefulSet

## Installing the Chart

To install the chart with the release name `my-release`:

```shell
helm install --name my-release stable/cockroachdb
```

Note that for a production cluster, you are very likely to want to modify the
`Storage` and `StorageClass` parameters. This chart defaults to just 1 GiB of
disk space per pod in order for it to work in small environments like Minikube,
and the default persistent volume `StorageClass` in your environment may not be
what you want for a database (e.g. on GCE the default is not SSD).

If you are running in secure mode (with configuration parameter `Secure.Enabled`
set to `true`), then you will have to manually approve the cluster's security
certificates as the pods are created. You can see the pending
certificate-signing requests by running `kubectl get csr`, and approve them by
running `kubectl certificate approve <csr-name>`. You'll have to approve one
certificate for each node (e.g.  `default.node.eerie-horse-cockroachdb-0` and
one client certificate for the job that initializes the cluster (e.g.
`default.node.root`).

## Upgrading
### To 2.0.0
Due to having no explicit selector set for the StatefulSet before version 2.0.0 of
this chart, upgrading from any version that uses a version of kubernetes that locks
the selector labels to any other version is impossible without deleting the StatefulSet.
Luckily there is a way to do it without actually deleting all the resources managed
by the StatefulSet. Use the workaround below to upgrade from versions previous to 2.0.0.
The following example assumes that the release name is crdb:

```console
$ kubectl delete statefulset crdb-cockroachdb --cascade=false
```

Verify that no pod is deleted and then upgrade as normal. A new StatefulSet will
be created taking over the management of the existing pods upgrading them if needed.

For more information about the upgrading bug see https://github.com/helm/charts/issues/7680.

## Configuration

The following table lists the configurable parameters of the CockroachDB chart and their default values.

| Parameter                      | Description                                      | Default                                   |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- |
| `Name`                         | Chart name                                       | `cockroachdb`                             |
| `Image`                        | Container image name                             | `cockroachdb/cockroach`                   |
| `ImageTag`                     | Container image tag                              | `v2.0.6`                                  |
| `ImagePullPolicy`              | Container pull policy                            | `Always`                                  |
| `Replicas`                     | k8s statefulset replicas                         | `3`                                       |
| `MaxUnavailable`               | k8s PodDisruptionBudget parameter                | `1`                                       |
| `Component`                    | k8s selector key                                 | `cockroachdb`                             |
| `ExternalGrpcPort`             | CockroachDB primary serving port                 | `26257`                                   |
| `ExternalGrpcName`             | CockroachDB primary serving port name            | `grpc`                                    |
| `InternalGrpcPort`             | CockroachDB inter-cockroachdb port               | `26257`                                   |
| `InternalGrpcName`             | CockroachDB inter-cockroachdb port name          | `grpc`                                    |
| `InternalHttpPort`             | CockroachDB HTTP port                            | `8080`                                    |
| `ExternalHttpPort`             | CockroachDB HTTP port on service                 | `8080`                                    |
| `HttpName`                     | Name given to the http service port              | `http`                                    |
| `Resources`                    | Resource requests and limits                     | `{}`                                      |
| `Storage`                      | Persistent volume size                           | `1Gi`                                     |
| `StorageClass`                 | Persistent volume class                          | `null`                                    |
| `CacheSize`                    | Size of CockroachDB's in-memory cache            | `25%`                                     |
| `MaxSQLMemory`                 | Max memory to use processing SQL queries         | `25%`                                     |
| `ClusterDomain`                | Cluster's default DNS domain                     | `cluster.local`                           |
| `NetworkPolicy.Enabled`        | Enable NetworkPolicy                             | `false`                                   |
| `NetworkPolicy.AllowExternal`  | Don't require client label for connections       | `true`                                    |
| `Service.Type`                 | Public service type                              | `ClusterIP`                               |
| `Service.Annotations`          | Annotations to apply to the service              | `{}`                                      |
| `PodManagementPolicy`          | `OrderedReady` or `Parallel` pod creation/deletion order | `Parallel`                        |
| `UpdateStrategy.type`          | allows setting of RollingUpdate strategy         | `RollingUpdate`                           |
| `NodeSelector`                 | Node labels for pod assignment                   | `{}`                                      |
| `Tolerations`                  | List of node taints to tolerate                  | `{}`                                      |
| `Secure.Enabled`               | Whether to run securely using TLS certificates   | `false`                                   |
| `Secure.RequestCertsImage`     | Image to use for requesting TLS certificates     | `cockroachdb/cockroach-k8s-request-cert`  |
| `Secure.RequestCertsImageTag`  | Image tag to use for requesting TLS certificates | `0.3`                                     |
| `Secure.ServiceAccount.Create` | Whether to create a new RBAC service account     | `true`                                    |
| `Secure.ServiceAccount.Name`   | Name of RBAC service account to use              | `""`                                      |
| `JoinExisting`                 | List of already-existing cockroach instances     | `[]`                                      |
| `Locality`                     | Locality attribute for this deployment           | `""`                                      |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

Alternatively, a YAML file that specifies the values for the parameters can be provided while installing the chart. For example,

```shell
helm install --name my-release -f values.yaml stable/cockroachdb
```

> **Tip**: You can use the default [values.yaml](values.yaml)

# Deep dive

## Connecting to the CockroachDB cluster

Once you've created the cluster, you can start talking to it by connecting
to its "public" service. CockroachDB is PostgreSQL wire protocol compatible so
there's a [wide variety of supported
clients](https://www.cockroachlabs.com/docs/install-client-drivers.html). For
the sake of example, we'll open up a SQL shell using CockroachDB's built-in
shell and play around with it a bit, like this (likely needing to replace
"my-release-cockroachdb-public" with the name of the "-public" service that
was created with your installed chart):

```console
$ kubectl run -it --rm cockroach-client \
    --image=cockroachdb/cockroach \
    --restart=Never \
    --command -- ./cockroach sql --insecure --host my-release-cockroachdb-public
Waiting for pod default/cockroach-client to be running, status is Pending,
pod ready: false
If you don't see a command prompt, try pressing enter.
root@my-release-cockroachdb-public:26257> SHOW DATABASES;
+--------------------+
|      Database      |
+--------------------+
| information_schema |
| pg_catalog         |
| system             |
+--------------------+
(3 rows)
root@my-release-cockroachdb-public:26257> CREATE DATABASE bank;
CREATE DATABASE
root@my-release-cockroachdb-public:26257> CREATE TABLE bank.accounts (id INT
PRIMARY KEY, balance DECIMAL);
CREATE TABLE
root@my-release-cockroachdb-public:26257> INSERT INTO bank.accounts VALUES
(1234, 10000.50);
INSERT 1
root@my-release-cockroachdb-public:26257> SELECT * FROM bank.accounts;
+------+---------+
|  id  | balance |
+------+---------+
| 1234 | 10000.5 |
+------+---------+
(1 row)
root@my-release-cockroachdb-public:26257> \q
Waiting for pod default/cockroach-client to terminate, status is Running
pod "cockroach-client" deleted
```

If you are running in secure mode, you will have to provide a client certificate
to the cluster in order to authenticate, so the above command will not work. See
[here](https://github.com/cockroachdb/cockroach/blob/master/cloud/kubernetes/client-secure.yaml)
for an example of how to set up an interactive SQL shell against a secure
cluster or
[here](https://github.com/cockroachdb/cockroach/blob/master/cloud/kubernetes/example-app-secure.yaml)
for an example application connecting to a secure cluster.

## Cluster health

Because our pod spec includes regular health checks of the CockroachDB processes,
simply running `kubectl get pods` and looking at the `STATUS` column is sufficient
to determine the health of each instance in the cluster.

If you want more detailed information about the cluster, the best place to look
is the admin UI.

## Accessing the admin UI

If you want to see information about how the cluster is doing, you can try
pulling up the CockroachDB admin UI by port-forwarding from your local machine
to one of the pods (replacing "my-release-cockroachdb-0" with one of your pods'
names):

```shell
kubectl port-forward my-release-cockroachdb-0 8080
```

Once you’ve done that, you should be able to access the admin UI by visiting
http://localhost:8080/ in your web browser.

## Failover

If any CockroachDB member fails it gets restarted or recreated automatically by
the Kubernetes infrastructure, and will rejoin the cluster automatically when
it comes back up. You can test this scenario by killing any of the pods:

```shell
kubectl delete pod my-release-cockroachdb-1
```

```shell
$ kubectl get pods -l "component=my-release-cockroachdb"
NAME                      READY     STATUS        RESTARTS   AGE
my-release-cockroachdb-0  1/1       Running       0          5m
my-release-cockroachdb-2  1/1       Running       0          5m
```

After a while:

```console
$ kubectl get pods -l "component=my-release-cockroachdb"
NAME                      READY     STATUS        RESTARTS   AGE
my-release-cockroachdb-0  1/1       Running       0          5m
my-release-cockroachdb-1  1/1       Running       0          20s
my-release-cockroachdb-2  1/1       Running       0          5m
```

You can check state of re-joining from the new pod's logs:

```console
$ kubectl logs my-release-cockroachdb-1
[...]
I161028 19:32:09.754026 1 server/node.go:586  [n1] node connected via gossip and
verified as part of cluster {"35ecbc27-3f67-4e7d-9b8f-27c31aae17d6"}
[...]
cockroachdb-0.my-release-cockroachdb.default.svc.cluster.local:26257
build:      beta-20161027-55-gd2d3c7f @ 2016/10/28 19:27:25 (go1.7.3)
admin:      http://0.0.0.0:8080
sql:
postgresql://root@my-release-cockroachdb-1.my-release-cockroachdb.default.svc.cluster.local:26257?sslmode=disable
logs:       cockroach-data/logs
store[0]:   path=cockroach-data
status:     restarted pre-existing node
clusterID:  {35ecbc27-3f67-4e7d-9b8f-27c31aae17d6}
nodeID:     2
[...]
```

## NetworkPolicy

To enable network policy for CockroachDB,
install [a networking plugin that implements the Kubernetes
NetworkPolicy spec](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy#before-you-begin),
and set `NetworkPolicy.Enabled` to `true`.

For Kubernetes v1.5 & v1.6, you must also turn on NetworkPolicy by setting
the DefaultDeny namespace annotation. Note: this will enforce policy for _all_ pods in the namespace:

    kubectl annotate namespace default "net.beta.kubernetes.io/network-policy={\"ingress\":{\"isolation\":\"DefaultDeny\"}}"

For more precise policy, set `networkPolicy.allowExternal=false`. This will
only allow pods with the generated client label to connect to CockroachDB.
This label will be displayed in the output of a successful install.

## Scaling

Scaling should typically be managed via the `helm upgrade` command, but StatefulSets
don't yet work with `helm upgrade`. In the meantime until `helm upgrade` works,
if you want to change the number of replicas, you can use the `kubectl scale`
as shown below:

```shell
kubectl scale statefulset my-release-cockroachdb --replicas=4
```

Note that if you are running in secure mode and increase the size of your
cluster, you will also have to approve the certificate-signing request of each
new node (using `kubectl get csr` and `kubectl certificate approve`).
# CockroachDB on Kubernetes as a StatefulSet

This example deploys CockroachDB on [Kubernetes](https://kubernetes.io) as a
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).
Kubernetes is an open source system for managing containerized applications
across multiple hosts, providing basic mechanisms for deployment, maintenance,
and scaling of applications.

This is a copy of the [similar example stored in the Kubernetes
repository](https://github.com/kubernetes/kubernetes/tree/master/examples/cockroachdb).
We keep a copy here as well for faster iteration, since merging things into
Kubernetes can be quite slow, particularly during the code freeze before
releases. The copy here will typically be more up-to-date.

Note that if all you want to do is run a single cockroachdb instance for
testing and don't care about data persistence, you can do so with just a single
command instead of following this guide (which sets up a more reliable cluster):

```shell
kubectl run cockroachdb --image=cockroachdb/cockroach --restart=Never -- start --insecure
```

## Limitations

### Kubernetes version

The minimum Kubernetes version to successfully run the examples in this
directory without modification is `1.8`. If you want to run them on an older
version of Kubernetes, use the files from the appropriate subdirectory (e.g. the
`v1.7` directory for Kubernetes 1.7 or the `v1.6` directory for Kubernetes 1.6).
Older Kubernetes versions that don't have their own directory are no longer
supported.

For secure mode, the controller must enable `certificatesigningrequests`.
You can check if this is enabled by looking at the controller logs:
```
# On cloud platform:
# Find the controller:
$ kubectl get pods --all-namespaces | grep controller
kube-system   po/kube-controller-manager-k8s-master-5ef244d4-0   1/1       Running   0          7m

# Check the logs:
$ kubectl logs kube-controller-manager-k8s-master-5ef244d4-0 -n kube-system | grep certificate
I0628 12:38:23.471365       1 controllermanager.go:427] Starting "certificatesigningrequests"
E0628 12:38:23.473076       1 certificates.go:38] Failed to start certificate controller: open /etc/kubernetes/ca/ca.pem: no such file or directory
W0628 12:38:23.473106       1 controllermanager.go:434] Skipping "certificatesigningrequests"
# This shows that the certificate controller is not running, approved CSRs will not trigger a certificate.

# On minikube:
$ minikube logs | grep certificate
Jun 28 12:49:00 minikube localkube[3440]: I0628 12:49:00.224903    3440 controllermanager.go:437] Started "certificatesigningrequests"
Jun 28 12:49:00 minikube localkube[3440]: I0628 12:49:00.231134    3440 certificate_controller.go:120] Starting certificate controller manager
# This shows that the certificate controller is running, approved CSRs will get a certificate.

```

### StatefulSet limitations

Node-local storage for StatefulSets was only recently promoted to beta as a
Kubernetes feature (known as [local persistent
volumes](https://kubernetes.io/docs/concepts/storage/volumes/#local)), so we
don't yet recommend running that way in production. Instead, these examples use
dynamically provisioned remote persistent volumes. Note that CockroachDB already
replicates its data and thus, for the best performance, should not be deployed
on a persistent volume which already replicates internally. High-performance use
cases that need the very best performance may want to consider a
[DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
deployment until node-local storage has been more rigorously hardened.

### Secure mode

Secure mode currently works by requesting node/client certificates from the kubernetes controller at pod initialization time.

### Geographically distributed clusters

The configuration files and instructions in this directory are limited to
deployments that exist entirely within a single Kubernetes cluster. If you'd
like to deploy CockroachDB across multiple geographically distributed Kubernetes
clusters, see the [multiregion subdirectory](multiregion).

## Creating your kubernetes cluster

### Locally on minikube

Set up your minikube cluster following the
[instructions provided in the Kubernetes docs](https://kubernetes.io/docs/getting-started-guides/minikube/).

### On AWS

Set up your cluster following the
[instructions provided in the Kubernetes docs](https://kubernetes.io/docs/getting-started-guides/aws/).

### On GCE

You can either set up your cluster following the
[instructions provided in the Kubernetes docs](https://kubernetes.io/docs/getting-started-guides/gce/)
or by using the hosted
[Google Kubernetes Engine (GKE)](https://cloud.google.com/container-engine/docs) service:

```shell
gcloud container clusters create NAME
```

If you're using GKE and want to run a secure cluster, one extra step is
required. A limitation in GKE's Role-Based Access Control (RBAC) integration
necessitates running a special command in order to let you create the RBAC
roles that CockroachDB needs to manage certificates.

1. Get the email address associated with your Google Cloud account by running:
   ```shell
   `gcloud info | grep Account`
   ```
2. Run [the following command from the GKE
   documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#prerequisites_for_using_role-based_access_control)
   with that email address:
   ```shell
   kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=<your.google.cloud.email@example.org>
   ```

### On Azure

Set up your cluster following the
[instructions provided in the Kubernetes docs](https://kubernetes.io/docs/getting-started-guides/azure/).


## Creating the cockroach cluster

Once your kubernetes cluster is up and running, you can launch your cockroach cluster.

### Insecure mode

To create the cluster, run:
```shell
kubectl create -f cockroachdb-statefulset.yaml
```

Then, to initialize the cluster, run:
```shell
kubectl create -f cluster-init.yaml
```

### Secure mode

#### Prerequisites

**REQUIRED**: the kubernetes cluster must run with the certificate controller enabled.
This is done by passing the `--cluster-signing-cert-file` and `--cluster-signing-key-file` flags.
If you are using minikube v0.23.0 or newer (run `minikube version` if you aren't sure), you can
tell it to use the minikube-generated CA by specifying:
```shell
minikube start --extra-config=controller-manager.ClusterSigningCertFile="/var/lib/localkube/certs/ca.crt" --extra-config=controller-manager.ClusterSigningKeyFile="/var/lib/localkube/certs/ca.key"
```

If you're running on an older version of minikube, you can similarly run:
```shell
minikube start --extra-config=controller-manager.ClusterSigningCertFile="/var/lib/localkube/ca.crt" --extra-config=controller-manager.ClusterSigningKeyFile="/var/lib/localkube/ca.key"
```

#### Creating the cluster

Run: `kubectl create -f cockroachdb-statefulset-secure.yaml`

If you get an error saying "attempt to grant extra privileges", you don't have
sufficient permissions in the cluster to manage certificates. If this happens
and you're running on Google Kubernetes Engine, see [the note above](#on-gce).
If not, talk to your cluster administrator.

Each new node will request a certificate from the kubernetes CA during its initialization phase.
We have configured the StatefulSet to bring up all its pods at once, so you can approve all of
the pods' certificates in quick succession.

If a pod is rescheduled, it will reuse the previously-generated certificate.

You can view pending certificates and approve them using:
```
# List CSRs:
$ kubectl get csr
NAME                         AGE       REQUESTOR                               CONDITION
default.node.cockroachdb-0   4s        system:serviceaccount:default:default   Pending
default.node.cockroachdb-1   4s        system:serviceaccount:default:default   Pending
default.node.cockroachdb-2   4s        system:serviceaccount:default:default   Pending

# Examine the CSR:
$ kubectl describe csr default.node.cockroachdb-0
Name:                   default.node.cockroachdb-0
Labels:                 <none>
Annotations:            <none>
CreationTimestamp:      Thu, 22 Jun 2017 09:56:49 -0400
Requesting User:        system:serviceaccount:default:default
Status:                 Pending
Subject:
        Common Name:    node
        Serial Number:
        Organization:   Cockroach
Subject Alternative Names:
        DNS Names:      localhost
                        cockroachdb-0.cockroachdb.default.svc.cluster.local
                        cockroachdb-public
        IP Addresses:   127.0.0.1
                        172.17.0.5
Events: <none>

# If everything checks out, approve the CSR:
$ kubectl certificate approve default.node.cockroachdb-0
certificatesigningrequest "default.node.cockroachdb-0" approved

# Otherwise, deny the CSR:
$ kubectl certificate deny default.node.cockroachdb-0
certificatesigningrequest "default.node.cockroachdb-0" denied
```

Once all the pods have started, to initialize the cluster run:
```shell
kubectl create -f cluster-init-secure.yaml
```

This will create a CSR called "default.client.root", which you can approve by
running:
```shell
kubectl certificate approve default.client.root
```

To confirm that it's done, run:
```shell
kubectl get job cluster-init-secure
```

The output should look like:
```
NAME                  DESIRED   SUCCESSFUL   AGE
cluster-init-secure   1         1            5m
```

## Accessing the database

Along with our StatefulSet configuration, we expose a standard Kubernetes service
that offers a load-balanced virtual IP for clients to access the database
with. In our example, we've called this service `cockroachdb-public`.

In insecure mode, start up a client pod and open up an interactive, (mostly) Postgres-flavor
SQL shell:

```shell
kubectl run cockroachdb -it --image=cockroachdb/cockroach --rm --restart=Never \
    -- sql --insecure --host=cockroachdb-public
```

In secure mode, use our `client-secure.yaml` config to launch a pod that runs indefinitely with the `cockroach` binary inside it:

```shell
kubectl create -f client-secure.yaml
```

Check and approve the CSR for the pod as described above, and then get a shell to the pod and run:

```shell
kubectl exec -it cockroachdb-client-secure -- ./cockroach sql --certs-dir=/cockroach-certs --host=cockroachdb-public
```

You can see example SQL statements for inserting and querying data in the
included [demo script](demo.sh), but can use almost any Postgres-style SQL
commands. Some more basic examples can be found within
[CockroachDB's documentation](https://www.cockroachlabs.com/docs/stable/learn-cockroachdb-sql.html).

## Accessing the admin UI

If you want to see information about how the cluster is doing, you can try
pulling up the CockroachDB admin UI by port-forwarding from your local machine
to one of the pods:

```shell
kubectl port-forward cockroachdb-0 8080
```

Once you’ve done that, you should be able to access the admin UI by visiting
http://localhost:8080/ in your web browser.

## Running the example app

This directory contains the configuration to launch a simple load generator with one pod.

If you created an insecure cockroach cluster, run:
```shell
kubectl create -f example-app.yaml
```

If you created a secure cockroach cluster, run:
```shell
kubectl create -f example-app-secure.yaml
```

When the first pod is being initialized, you will need to approve its client certificate request:
```shell
kubectl certificate approve default.client.root
```

If more pods are then added through `kubectl scale deployment example-secure --replicas=X`, the generated
certificate will be reused.
**WARNING**: the example app in secure mode should be started with only one replica, or concurrent and
conflicting certificate requests will be sent, causing issues.


## Secure client apps with other users

Applications should be run with a user other than `root`. This can be done using the following:

#### Create the desired user and database

Connect to the `cockroachdb-client-secure` pod (created in the "Accessing the database" section):
```shell
kubectl exec -it cockroachdb-client-secure -- ./cockroach sql --certs-dir=/cockroach-certs --host=cockroachdb-public
```

Create the the app user, its database, and grant it privileges:
```shell
root@:26257/defaultdb> CREATE USER myapp;
CREATE USER 1

Time: 164.811054ms

root@:26257/defaultdb> CREATE DATABASE myappdb;
CREATE DATABASE

Time: 153.44247ms

root@:26257/defaultdb> GRANT ALL ON DATABASE myappdb TO myapp;
GRANT

Time: 90.488168ms
```

#### Create the client pod

Modify [example-app-secure.yaml](example-app-secure.yaml) to match your user and app:

The init container `init-certs` needs to request a certificate and key for your new user:
```shell
"/request-cert -namespace=${POD_NAMESPACE} -certs-dir=/cockroach-certs -type=client -user=myapp -symlink-ca-from=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
```

The `loadgen` container should be modified for your client app docker image and command, and the connection url modified to match the user and database:
```shell
"postgres://myapp@cockroachdb-public:26257/myappdb?sslmode=verify-full&sslcert=/cockroach-certs/client.myapp.crt&sslkey=/cockroach-certs/client.myapp.key&sslrootcert=/cockroach-certs/ca.crt"
```

You can now create the client pod:
```shell
kubectl create -f example-app-secure.yaml
```

#### Approve the client CSR

The init container sends a CSR and waits for approval. You can approve it using:
```shell
kubectl certificate approve default.client.myapp
```

Once approved, the init container copies the certificate and key to `/cockroach-certs` and terminates. The app container now starts, using the mounted certificate directory.


## Simulating failures

When all (or enough) nodes are up, simulate a failure like this:

```shell
kubectl exec cockroachdb-0 -- /bin/bash -c "while true; do kill 1; done"
```

You can then reconnect to the database as demonstrated above and verify
that no data was lost. The example runs with three-fold replication, so
it can tolerate one failure of any given node at a time. Note also that
there is a brief period of time immediately after the creation of the
cluster during which the three-fold replication is established, and during
which killing a node may lead to unavailability.

The [demo script](demo.sh) gives an example of killing one instance of the
database and ensuring the other replicas have all data that was written.

## Scaling up or down

Scale the StatefulSet by running

```shell
kubectl scale statefulset cockroachdb --replicas=4
```

You should never scale the StatefulSet down by more than one replica at a time.
Doing so could lead to data unavailability. For best practices on safely
removing nodes from a safely, see our docs on [node
decommissioning](https://www.cockroachlabs.com/docs/stable/remove-nodes.html).

## Doing a rolling upgrade to a different CockroachDB version

Open up the StatefulSet's current configuration in your default text editor
using the command below, find the line specifying the `cockroachdb/cockroach`
image being used, change the version tag to the new one, save the file, and
quit.

```shell
kubectl edit statefulset cockroachdb
```

Kubernetes will then automatically replace the pods in your StatefulSet one by
one to run on the newly specified image. For more details on upgrading
CockroachDB, see [our
docs](https://www.cockroachlabs.com/docs/stable/upgrade-cockroach-version.html).
For how to use alternative rolling update commands such as `kubectl patch` and
`kubectl replace`, see the [Kubernetes
docs](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#rolling-update).

## Cleaning up when you're done

Because all of the resources in this example have been tagged with the label `app=cockroachdb`,
we can clean up everything that we created in one quick command using a selector on that label:

```shell
kubectl delete statefulsets,pods,persistentvolumes,persistentvolumeclaims,services,poddisruptionbudget,jobs,rolebinding,clusterrolebinding,role,clusterrole,serviceaccount -l app=cockroachdb
```

If running in secure mode, you'll want to cleanup old certificate requests:
```shell
kubectl delete csr --all
```
# Running CockroachDB across multiple Kubernetes clusters

The script and configuration files in this directory enable deploying
CockroachDB across multiple Kubernetes clusters that are spread across different
geographic regions. It deploys a CockroachDB
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
into each separate cluster, and links them together using DNS.

To use the configuration provided here, check out this repository (or otherwise
download a copy of this directory), fill in the constants at the top of
[setup.py](setup.py) with the relevant information about your Kubernetes
clusters, optionally make any desired modifications to
[cockroachdb-statefulset-secure.yaml](cockroachdb-statefulset-secure.yaml) as
explained in [our Kubernetes performance tuning
guide](https://www.cockroachlabs.com/docs/stable/kubernetes-performance.html),
then finally run [setup.py](setup.py).

You should see a lot of output as it does its thing, hopefully ending after
printing out `job "cluster-init-secure" created`. This implies that everything
was created successfully, and you should soon see the CockroachDB cluster
initialized with 3 pods in the "READY" state in each Kubernetes cluster. At this
point you can manage the StatefulSet in each cluster independently if you so
desire, scaling up the number of replicas, changing their resource requests, or
making other modifications as you please.

If anything goes wrong along the way, please let us know via any of the [normal
troubleshooting
channels](https://www.cockroachlabs.com/docs/stable/support-resources.html).
While we believe this creates a highly available, maintainable multi-region
deployment, it is still pushing the boundaries of how Kubernetes is typically
used, so feedback and issue reports are very appreciated.

## Limitations

### Pod-to-pod connectivity

The deployment outlined in this directory relies on pod IP addresses being
routable even across Kubernetes clusters and regions. This achieves optimal
performance, particularly when compared to alternative solutions that route all packets between clusters through load balancers, but means that it won't work in certain environments.

This requirement is satisfied by clusters deployed in cloud environments such as Google Kubernetes Engine, and
can also be satisfied by on-prem environments depending on the [Kubernetes networking setup](https://kubernetes.io/docs/concepts/cluster-administration/networking/) used. If you want to test whether your cluster will work, you can run this basic network test:

```shell
$ kubectl run network-test --image=alpine --restart=Never -- sleep 999999
pod "network-test" created
$ kubectl describe pod network-test | grep IP
IP:           THAT-PODS-IP-ADDRESS
$ kubectl config use-context YOUR-OTHER-CLUSTERS-CONTEXT-HERE
$ kubectl run -it network-test --image=alpine --restart=Never -- ping THAT-PODS-IP-ADDRESS
If you don't see a command prompt, try pressing enter.
64 bytes from 10.12.14.10: seq=1 ttl=62 time=0.570 ms
64 bytes from 10.12.14.10: seq=2 ttl=62 time=0.449 ms
64 bytes from 10.12.14.10: seq=3 ttl=62 time=0.635 ms
64 bytes from 10.12.14.10: seq=4 ttl=62 time=0.722 ms
64 bytes from 10.12.14.10: seq=5 ttl=62 time=0.504 ms
...
```

If the pods can directly connect, you should see successful ping output like the
above. If they can't, you won't see any successful ping responses. Make sure to
delete the `network-test` pod in each cluster when you're done!

### Exposing DNS servers to the Internet

As currently configured, the way that the DNS servers from each Kubernetes
cluster are hooked together is by exposing them via a load balanced IP address
that's visible to the public Internet. This is because [Google Cloud Platform's Internal Load Balancers do not currently support clients in one region using a load balancer in another region](https://cloud.google.com/compute/docs/load-balancing/internal/#deploying_internal_load_balancing_with_clients_across_vpn_or_interconnect). 

None of the services in your Kubernetes cluster will be made accessible, but
their names could leak out to a motivated attacker. If this is unacceptable,
please let us know and we can demonstrate other options. [Your voice could also
help convince Google to allow clients from one region to use an Internal Load
Balancer in another](https://issuetracker.google.com/issues/111021512),
eliminating the problem.

## Cleaning up

To remove all the resources created in your clusters by [setup.py](setup.py),
copy the parameters you provided at the top of [setup.py](setup.py) to the top
of [teardown.py](teardown.py) and run [teardown.py](teardown.py).

## More information

For more information on running CockroachDB in Kubernetes, please see the [README
in the parent directory](../README.md).
This guide is based on using CoreOS's Prometheus Operator, which allows
a Prometheus instance to be managed using native Kubernetes concepts.


References used:
* https://github.com/coreos/prometheus-operator/blob/master/Documentation/user-guides/getting-started.md
* https://github.com/coreos/prometheus-operator/blob/master/Documentation/user-guides/alerting.md

# Preflight

Create and initialize a Cockroach cluster, if you haven't already done
so:
* `kubectl apply -f
https://raw.githubusercontent.com/cockroachdb/cockroach/master/cloud/kubernetes/cockroachdb-statefulset.yaml`
* `kubectl apply -f
https://raw.githubusercontent.com/cockroachdb/cockroach/master/cloud/kubernetes/cluster-init.yaml`


If you're running on Google Kubernetes Engine, it's necessary to ensure
that your Kubernetes user is part of the cluster-admin groups.  Edit the
following command before running it; the email address should be
whatever account you use to access GKE.  This is required, regardless
of whether or not you are using a secure CockroachDB cluster.
* `kubectl create clusterrolebinding $USER-cluster-admin-binding
--clusterrole=cluster-admin --user=YOU@YOURDOMAIN.COM`

# Monitoring

Edit the cockroachdb service to add the label `prometheus: cockroachdb`.
We use this because we don't want to duplicate the monitoring data
between the two services that we create.  If we don't have a way to
distinguish the `cockroachdb` and `cockroachdb-public` services from
one another, we'd have two different prometheus jobs that had duplicated
backends.
* `kubectl label svc cockroachdb prometheus=cockroachdb`


Install Prometheus Operator:
* `kubectl apply -f
https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.20/bundle.yaml`

Ensure that the instance of prometheus-operator has started before
continuing.  The `kubectl get` command and its desired output is below:
```
$ kubectl get deploy prometheus-operator
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
prometheus-operator   1         1         1            1           23h
```

Create the various objects necessary to run a prometheus instance:
* `kubectl apply -f prometheus.yaml`

To view the Prometheus UI locally:
* `kubectl port-forward
prometheus-cockroachdb-0 9090`
* Open http://localhost:9090 in your browser.
* Select the `Status -> Targets` menu entry to verify that the
  CockroachDB instances have been located.
  ![Targets screenshot](img/targets.png)
* Graphing the `sys_uptime` variable will verify that data is being
  collected. ![Uptime graph screenshot](img/graph.png)


# Alerting

Edit the template `alertmanager.yaml` with your relevant configuration.
What's in the file has a dummy web hook, per the prometheus-operator
alerting guide linked from the top of the document.

Upload `alertmanager-config.yaml`, renaming it to `alertmanager.yaml`
in the process, and labelling it to make it easier to find.
* `kubectl create secret generic
alertmanager-cockroachdb --from-file=alertmanager.yaml=alertmanager-config.yaml`
* `kubectl label secret  alertmanager-cockroachdb app=cockroachdb`

It's critical that the name of the secret and the `alertmanager.yaml`
are given exactly as shown.

Create an AlertManager object to run a replicated AlertManager instance
and create a ClusterIP service so that Prometheus can forward alerts:
* `kubectl apply -f alertmanager.yaml`


Verify that AlertManager is running:
* `kubectl port-forward alertmanager-cockroachdb-0  9093`
* Open http://localhost:9093 in your browser.  You should see something
  similar to the following:
  ![AlertManager screenshot](img/alertmanager.png)
* Ensure that the AlertManagers are visible to Prometheus by checking
  http://localhost:9090/status.  It may take a minute for the configuration
  changes to propagate.  If this is successful, you should see something
  similar to the following:
  ![AlertManager screenshot](img/status-alertmanagers.png)


Upload alert rules:
*  These are copied from https://github.com/cockroachdb/cockroach/blob/master/monitoring/rules/alerts.rules.yml:
* `kubectl apply -f alert-rules.yaml`
* Check that the rules are visible to Prometheus by opening
  http://localhost:9090/rules.  It may take a minute for the configuration
  changes to propagate. ![Rule screenshot](img/rules.png)
* Verify that the example alert is firing by opening
  http://localhost:9090/rules ![Alerts screenshot](img/alerts.png)
* Remove the example alert by running
  `kubectl edit prometheusrules prometheus-cockroachdb-rules` and
  deleting the `dummy.rules` block.

# Cleaning Up

You can remove the monitoring configurations using the following command:

`kubectl delete Alertmanager,Prometheus,PrometheusRule,ServiceMonitor -l app=cockroachdb`

# Maintenance

The contents of `alert-rules.yaml` are generated from our reference
prometheus configs, located in the top-level `cockroach/monitoring`
directory.  A `wraprules` tool exists to make maintaining this easier.

```
go get github.com/cockroachdb/cockroach/pkg/cmd/wraprules
wraprules -o path/to/alert-rules.yaml path/to/cockroach/monitoring/rules/*.rules.yml
```
