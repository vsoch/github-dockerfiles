# brightbox-cloud-controller-manager
Kubernetes Cloud Controller Manager implementation for Brightbox Cloud

## Intro
This implementation uses the cloud-controller framework from Kubernetes described in the following documents

- https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/
- https://kubernetes.io/docs/concepts/architecture/cloud-controller/
- https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/

## Running the Cloud controller on a cluster

Is [described here](config/README.md)

## main package
`main.go` is a copy of the [controller manager](https://github.com/kubernetes/kubernetes/blob/master/cmd/cloud-controller-manager/controller-manager.go)
with alterations made to accommodate this implementation.

You can regenerate `main.go` from the latest version of the upstream
controller by removing the file and running `make main.go`. This will
apply the Brightbox Cloud patch to the upstream controller file.

## versioning
The controller uses the Kubernetes versioning system with magic strings
injected into the binary via Loader flags given to the Go compiler.

The script `hack/version.sh` generates the required loader flags from
the commits and tags in the git repository.

## Dependencies
Vendored dependencies are managed with `dep` with the restrictions
described in `Gopkg.toml`. Run `dep ensure` to check vendor is up to date.

## Design approach
The implementation in the brightbox package satisifes the
`cloudprovider.Interface` pluggable interface.

The provider implements:

- the node controller - annotating nodes with zone, region and image
type information allowing the k8s scheduler to better place containers
in a resilient manner

- the service controller - building Brightbox Cloud load balancers on demand.

It treats the cloud-controller framework and the wider Kubernetes system
as a supervisor system - along the lines of Erlang. The approach taken
in each implemented function is to be completely idempotent and to
crash out as soon as any problem is detected - returning a meaningful
error. Kubernetes will then log the error message in the event list for
the resource and schedule a retry.

The main advantage is that you don't need to wait for anything in
the code. Just stop and let the retry process handle it. Avoid making
unnecessary API calls to reduce the load on Brightbox Cloud API servers.

Currently each load balancer created generates a server group and
firewall policy specifically for that load balancer with a single firewall
rule pointing at the exposed node port. This avoids any race conditions
within the cloud-controller trying to insert and update rules in a single
firewall policy and group.

The Controller avoids any additional Goroutines. The Interfaces
implemented are described in `brightbox/cloud-controller-interface.go`,
with a separate file in the package for each of the interfaces
implemented.

## Examples

The load balancer supports annotations that allow you to use the range of
facilities available on Brightbox Cloud Load Balancers. See the [manifest
examples](https://github.com/brightbox/kubernetes-cluster/blob/master/README.md)
for details.

## Developing

We're very happy to receive PR requests on this controller. If you can
improve things or make suggestions then please do so.

`make test` runs the Go test files against the implementation. The
Brightbox Cloud API is mocked out so you can run it without credentials.

`make compile` creates the stripped binary cloud controller (including
magic version information) that can be copied to a cluster.

`make build` creates a docker image of the cloud controller.

To test on a cluster shutdown any running cloud controller containers
using `kubectl`, copy the binary to the cluster and then run in
a shell. (This assumes the cluster was built with `kubeadm` and the
`admin.conf` kubeconfig is available).

Obtain an [api client from the Brightbox Manager](https://www.brightbox.com/docs/guides/manager/api-clients/) and run the controller using the following command

```
sudo BRIGHTBOX_CLIENT=cli-xxxxx \
     BRIGHTBOX_CLIENT_SECRET=my_secret \
     BRIGHTBOX_API_URL=https://api.gb1.brightbox.com \
     ./brightbox-cloud-controller-manager \
        --cloud-provider=brightbox \
        --bind-address=::1 \
        --port=0 \
        --secure-port=10253 \
        --configure-cloud-routes=false \
        --kubeconfig=/etc/kubernetes/admin.conf \
        --cluster-name=My_Cluster_Name \
        --leader-elect=false \
	-v=4 \
        --use-service-account-credentials=false 
```

The logs from the cloud controller will come out on the terminal.

Exercise the controller by using `kubectl` in a separate terminal by
creating, updating and deleting nodes and loadbalancers.
