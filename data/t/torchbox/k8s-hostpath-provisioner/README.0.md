This repo is still in the experimental stage. Shortly it will contain the schema of the API that are served by the Kubernetes apiserver.
# apimachinery

Scheme, typing, encoding, decoding, and conversion packages for Kubernetes and Kubernetes-like API objects.


## Purpose

This library is a shared dependency for servers and clients to work with Kubernetes API infrastructure without direct 
type dependencies.  It's first comsumers are `k8s.io/kubernetes`, `k8s.io/client-go`, and `k8s.io/apiserver`.


## Compatibility

There are *NO compatibility guarantees* for this repository.  It is in direct support of Kubernetes, so branches
will track Kubernetes and be compatible with that repo.  As we more cleanly separate the layers, we will review the
compatibility guarantee.


## Where does it come from?

`apimachinery` is synced from https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery.
Code changes are made in that location, merged into `k8s.io/kubernetes` and later synced here.


## Things you should *NOT* do

 1. Add API types to this repo.  This is for the machinery, not for the types.
 2. Directly modify any files under `pkg` in this repo.  Those are driven from `k8s.io/kuberenetes/staging/src/k8s.io/apimachinery`.
 3. Expect compatibility.  This repo is direct support of Kubernetes and the API isn't yet stable enough for API guarantees.# client-go

Go clients for talking to a [kubernetes](http://kubernetes.io/) cluster.

We currently recommend using the v2.0.0 tag. See [INSTALL.md](/INSTALL.md) for
detailed installation instructions. `go get k8s.io/client-go/...` works, but
will give you head and doesn't handle the dependencies well.

[![Build Status](https://travis-ci.org/kubernetes/client-go.svg?branch=master)](https://travis-ci.org/kubernetes/client-go)
[![GoDoc](https://godoc.org/k8s.io/client-go?status.svg)](https://godoc.org/k8s.io/client-go)

## Table of Contents
 
- [What's included](#whats-included)
- [Versioning](#versioning)
  - [Compatibility: your code <-> client-go](#compatibility-your-code---client-go)
  - [Compatibility: client-go <-> Kubernetes clusters](#compatibility-client-go---kubernetes-clusters)
  - [Compatibility matrix](#compatibility-matrix)
  - [Why do the 1.4 and 1.5 branch contain top-level folder named after the version?](#why-do-the-14-and-15-branch-contain-top-level-folder-named-after-the-version)
- [How to get it](#how-to-get-it)
- [How to use it](#how-to-use-it)
- [Dependency management](#dependency-management)
- [Contributing code](#contributing-code)

### What's included

* The `kubernetes` package contains the clientset to access Kubernetes API.
* The `discovery` package is used to discover APIs supported by a Kubernetes API server.
* The `dynamic` package contains a dynamic client that can perform generic operations on arbitrary Kubernetes API objects.
* The `transport` package is used to set up auth and start a connection.
* The `tools/cache` package is useful for writing controllers.

### Versioning

`client-go` follows [semver](http://semver.org/). We will not make
backwards-incompatible changes without incrementing the major version number. A
change is backwards-incompatible either if it *i)* changes the public interfaces
of `client-go`, or *ii)* makes `client-go` incompatible with otherwise supported
versions of Kubernetes clusters.

Changes that add features in a backwards-compatible way will result in bumping
the minor version (second digit) number.

Bugfixes will result in the patch version (third digit) changing. PRs that are
cherry-picked into an older Kubernetes release branch will result in an update
to the corresponding branch in `client-go`, with a corresponding new tag
changing the patch version.

A consequence of this is that `client-go` version numbers will be unrelated to
Kubernetes version numbers.

#### Branches and tags.

We will create a new branch and tag for each increment in the major version number or
minor version number. We will create only a new tag for each increment in the patch
version number. See [semver](http://semver.org/) for definitions of major,
minor, and patch.

The master branch will track HEAD in the main Kubernetes repo and
accumulate changes. Consider HEAD to have the version `x.(y+1).0-alpha` or
`(x+1).0.0-alpha` (depending on whether it has accumulated a breaking change or
not), where `x` and `y` are the current major and minor versions.

#### Compatibility: your code <-> client-go

`client-go` follows [semver](http://semver.org/), so until the major version of
client-go gets increased, your code will compile and will continue to work with
explicitly supported versions of Kubernetes clusters. You must use a dependency
management system and pin a specific major version of `client-go` to get this
benefit, as HEAD follows the upstream Kubernetes repo.

#### Compatibility: client-go <-> Kubernetes clusters

Since Kubernetes is backwards compatible with clients, older `client-go`
versions will work with many different Kubernetes cluster versions.

We will backport bugfixes--but not new features--into older versions of
`client-go`.


#### Compatibility matrix

|                     | Kubernetes 1.3 | Kubernetes 1.4 | Kubernetes 1.5 | Kubernetes 1.6 |
|---------------------|----------------|----------------|----------------|----------------|
| client-go 1.4       | +              | ✓              | -              | -              |
| client-go 1.5       | +              | +              | -              | -              |
| client-go 2.0       | +              | +              | ✓              | -              |
| client-go 3.0 beta  | +              | +              | +              | ✓              |
| client-go HEAD      | +              | +              | +              | +              |

Key:

* `✓` Exactly the same features / API objects in both client-go and the Kubernetes
  version.
* `+` client-go has features or api objects that may not be present in the
  Kubernetes cluster, but everything they have in common will work.
* `-` The Kubernetes cluster has features the client-go library can't use
  (additional API objects, etc).

See the [CHANGELOG](./CHANGELOG.md) for a detailed description of changes
between client-go versions.

| Branch         | Canonical source code location       | Maintenance status            |
|----------------|--------------------------------------|-------------------------------|
| client-go 1.4  | Kubernetes main repo, 1.4 branch     | = -                           |
| client-go 1.5  | Kubernetes main repo, 1.5 branch     | = -                           |
| client-go 2.0  | Kubernetes main repo, 1.5 branch     | ✓                             |
| client-go 3.0  | Kubernetes main repo, 1.6 branch     | ✓                             |
| client-go HEAD | Kubernetes main repo, master branch  | ✓                             |

Key:

* `✓` Changes in main Kubernetes repo are actively published to client-go by a bot
* `=` Maintenance is manual, only severe security bugs will be patched.
* `-` Deprecated; please upgrade.

#### Deprecation policy

We will maintain branches for at least six months after their first stable tag
is cut. (E.g., the clock for the release-2.0 branch started ticking when we
tagged v2.0.0, not when we made the first alpha.) This policy applies to
every version greater than or equal to 2.0.

#### Why do the 1.4 and 1.5 branch contain top-level folder named after the version?

For the initial release of client-go, we thought it would be easiest to keep
separate directories for each minor version. That soon proved to be a mistake.
We are keeping the top-level folders in the 1.4 and 1.5 branches so that
existing users won't be broken.

### How to get it

You can use `go get k8s.io/client-go/...` to get client-go, but **you will get
the unstable master branch** and `client-go`'s vendored dependencies will not be
added to your `$GOPATH`. So we think most users will want to use a dependency
management system. See [INSTALL.md](/INSTALL.md) for detailed instructions.

### How to use it

If your application runs in a Pod in the cluster, please refer to the in-cluster [example](examples/in-cluster/main.go), otherwise please refer to the out-of-cluster [example](examples/out-of-cluster/main.go).

### Dependency management

If your application depends on a package that client-go depends on, and you let the Go compiler find the dependency in `GOPATH`, you will end up with duplicated dependencies: one copy from the `GOPATH`, and one from the vendor folder of client-go. This will cause unexpected runtime error like flag redefinition, since the go compiler ends up importing both packages separately, even if they are exactly the same thing. If this happens, you can either
* run `godep restore` ([godep](https://github.com/tools/godep)) in the client-go/ folder, then remove the vendor folder of client-go. Then the packages in your GOPATH will be the only copy
* or run `godep save` in your application folder to flatten all dependencies.

### Contributing code
Please send pull requests against the client packages in the Kubernetes main [repository](https://github.com/kubernetes/kubernetes), and run the `/staging/copy.sh` script to update the staging area in the main repository. Changes in the staging area will be published to this repository every day.
# client-go Examples

This directory contains examples that cover various use cases and functionality
for client-go.

### Configuration

- [**Authenticate in cluster**](./in-cluster-client-configuration): Configure a
  client while running inside the Kubernetes cluster.
- [**Authenticate out of cluster**](./out-of-cluster-client-configuration):
  Configure a client to access a Kubernetes cluster from outside.

### Basics

- [**Managing resources with API**](./create-update-delete-deployment): Create,
  get, update, delete a Deployment resource.

### Advanced Concepts

- [**Work queues**](./workqueue): Create a hotloop-free controller with the
  rate-limited workqueue and the [informer framework][informer].
- [**Third-party resources (deprecated)**](./third-party-resources-deprecated):
  Register a third-party resource type with the API, create/update/query this third-party
  type, and write a controller that drives the cluster state based on the changes to
  the third-party resources.
- [**Custom Resource Definition (successor of TPR)**](https://git.k8s.io/apiextensions-apiserver/examples/client-go):
  Register a custom resource type with the API, create/update/query this custom
  type, and write a controller that drives the cluster state based on the changes to
  the custom resources.

[informer]: https://godoc.org/k8s.io/client-go/tools/cache#NewInformer
# Third Party Resources Example – Deprecated

**Note:** ThirdPartyResources are deprecated since 1.7. The successor is CustomResourceDefinition in the apiextensions.k8s.io API group.

This particular example demonstrates how to perform basic operations such as:

* How to register a new ThirdPartyResource (custom Resource type)
* How to create/get/list instances of your new Resource type (update/delete/etc work as well but are not demonstrated) 
* How to setup a controller on Resource handling create/update/delete events

## Running

```
# assumes you have a working kubeconfig, not required if operating in-cluster
go run *.go -kubeconfig=$HOME/.kube/config
```

## Use Cases

ThirdPartyResources can be used to implement custom Resource types for your Kubernetes cluster.
These act like most other Resources in Kubernetes, and may be `kubectl apply`'d, etc.

Some example use cases:

* Provisioning/Management of external datastores/databases (eg. CloudSQL/RDS instances)
* Higher level abstractions around Kubernetes primitives (eg. a single Resource to define an etcd cluster, backed by a Service and a ReplicationController) 

## Defining types

Each instance of your ThirdPartyResource has an attached Spec, which should be defined via a `struct{}` to provide data format validation.
In practice, this Spec is arbitrary key-value data that specifies the configuration/behavior of your Resource.

For example, if you were implementing a ThirdPartyResource for a Database, you might provide a DatabaseSpec like the following:

``` go
type DatabaseSpec struct {
	Databases []string `json:"databases"`
	Users     []User   `json:"users"`
	Version   string   `json:"version"`
}

type User struct {
	Name     string `json:"name"`
	Password string `json:"password"`
}
```# Workqueue Example

This example demonstrates how to write a controller which follows the states
of watched resources.

It demonstrates how to:
 * combine the workqueue with a cache to a full controller
 * synchronize the controller on startup

The example is based on https://git.k8s.io/community/contributors/devel/controllers.md.

## Running

```
# if outside of the cluster
go run *.go -kubeconfig=/my/config -logtostderr=true
```
# Create, Update & Delete Deployment

This example program demonstrates the fundamental operations for managing on
[Deployment][1] resources, such as `Create`, `List`, `Update` and `Delete`.

You can adopt the source code from this example to write programs that manage
other types of resources through the Kubernetes API.

## Running this example

Make sure you have a Kubernetes cluster and `kubectl` is configured:

    kubectl get nodes

Compile this example on your workstation:

```
cd create-update-delete-deployment
go build -o ./app
```

Now, run this application on your workstation with your local kubeconfig file:

```
./app -kubeconfig=$HOME/.kube/config
```

Running this command will execute the following operations on your cluster:

1. **Create Deployment:** This will create a 2 replica Deployment. Verify with
   `kubectl get pods`.
2. **Update Deployment:** This will update the Deployment resource created in
   previous step to set the replica count to 1 and add annotations. You are
   encouraged to inspect the retry loop that handles conflicts. Verify the new
   replica count and `foo=bar` annotation with `kubectl describe deployment
   demo`.
3. **List Deployments:** This will retrieve Deployments in the `default`
   namespace and print their names and replica counts.
4. **Delete Deployment:** This will delete the Deployment object and its
   dependent ReplicaSet resource. Verify with `kubectl get deployments`.

Each step is separated by an interactive prompt. You must hit the
<kbd>Return</kbd> key to proceeed to the next step. You can use these prompts as
a break to take time to  run `kubectl` and inspect the result of the operations
executed.

You should see an output like the following:

```
Creating deployment...
Created deployment "demo-deployment".
-> Press Return key to continue.

Updating deployment...
Updated deployment...
-> Press Return key to continue.

Listing deployments in namespace "default":
 * demo-deployment (1 replicas)
-> Press Return key to continue.

Deleting deployment...
Deleted deployment.
```

## Cleanup

Successfully running this program will clean the created artifacts. If you
terminate the program without completing, you can clean up the created
deployment with:

    kubectl delete deploy demo-deployment

## Troubleshooting

If you are getting the following error, make sure Kubernetes version of your
cluster is v1.6 or above in `kubectl version`:

    panic: the server could not find the requested resource

[1]: https://kubernetes.io/docs/user-guide/deployments/
# Authenticating outside the cluster

This example shows you how to configure a client with client-go to authenticate
to the Kubernetes API from an application running outside the Kubernetes
cluster.

You can use your kubeconfig file that contains the context information
of your cluster to initialize a client. The kubeconfig file is also used
by the `kubectl` command to authenticate to the clusters.

## Running this example

Make sure your `kubectl` is configured and pointed to a cluster. Run
`kubectl get nodes` to confirm.

Run this application with:

    cd out-of-cluster-client-configuration
    go build -o app .
    ./app

Running this application will use the kubeconfig file and then authenticate to the
cluster, and print the number of nodes in the cluster every 10 seconds:

    $ ./app
    There are 3 pods in the cluster
    There are 3 pods in the cluster
    There are 3 pods in the cluster
    ...

Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to quit this application.

> **Note:** You can use the `-kubeconfig` option to use a different config file. By default
this program picks up the default file used by kubectl (when `KUBECONFIG`
environment variable is not set).
# Authenticating inside the cluster

This example shows you how to configure a client with client-go to authenticate
to the Kubernetes API from an application running inside the Kubernetes cluster.

client-go uses the [Service Account token][sa] mounted inside the Pod at the
`/var/run/secrets/kubernetes.io/serviceaccount` path when the
`rest.InClusterConfig()` is used.

## Running this example

First compile the application for Linux:

    cd in-cluster-client-configuration
    GOOS=linux go build -o ./app .

Then package it to a docker image using the provided Dockerfile to run it on
Kubernetes.

If you are running a [Minikube][mk] cluster, you can build this image directly
on the Docker engine of the Minikube node without pushing it to a registry. To
build the image on Minikube:

    eval $(minikube docker-env)
    docker build -t in-cluster .

If you are not using Minikube, you should build this image and push it to a registry
that your Kubernetes cluster can pull from.

Then, run the image in a Pod with a single instance Deployment:

    $ kubectl run --rm -i demo --image=in-cluster --image-pull-policy=Never

    There are 4 pods in the cluster
    There are 4 pods in the cluster
    There are 4 pods in the cluster
    ...

The example now runs on Kubernetes API and successfully queries the number of
pods in the cluster every 10 seconds.

### Clean up

To stop this example and clean up the pod, press <kbd>Ctrl</kbd>+<kbd>C</kbd> on
the `kubectl run` command and then run:

    kubectl delete deployment demo

[sa]: https://kubernetes.io/docs/admin/authentication/#service-account-tokens
[mk]: https://kubernetes.io/docs/getting-started-guides/minikube/
# Azure Active Directory plugin for client authentication

This plugin provides an integration with Azure Active Directory device flow. If no tokens are present in the kubectl configuration, it will prompt a device code which can be used to login in a browser. After login it will automatically fetch the tokens and stored them in the kubectl configuration. In addition it will refresh and update the tokens in configuration when expired.


## Usage

1. Create an Azure Active Directory *Web App / API* application for `apiserver` following these [instructions](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-app-registration)

2. Create a second Azure Active Directory native application for `kubectl` 

3. On `kubectl` application's configuration page in Azure portal grant permissions to `apiserver` application by clicking on *Required Permissions*, click the *Add* button and search for the apiserver application created in step 1. Select "Access apiserver" under the *DELEGATED PERMISSIONS*. Once added click the *Grant Permissions* button to apply the changes

4. Configure the `apiserver` to use the Azure Active Directory as an OIDC provider with following options

   ```
   --oidc-client-id="spn:APISERVER_APPLICATION_ID" \
   --oidc-issuer-url="https://sts.windows.net/TENANT_ID/"
   --oidc-username-claim="sub"
   ```

   * Replace the `APISERVER_APPLICATION_ID` with the application ID of `apiserver` application
   * Replace `TENANT_ID` with your tenant ID.

5. Configure the `kubectl` to use the `azure` authentication provider 

   ```
   kubectl config set-credentials "USER_NAME" --auth-provider=azure \
     --auth-provider-arg=environment=AzurePublicCloud \
     --auth-provider-arg=client-id=APPLICATION_ID \
     --auth-provider-arg=tenant-id=TENANT_ID \
     --auth-provider-arg=apiserver-id=APISERVER_APPLICATION_ID
   ```

   * Supported environments: `AzurePublicCloud`, `AzureUSGovernmentCloud`, `AzureChinaCloud`, `AzureGermanCloud`
   * Replace `USER_NAME` and `TENANT_ID` with your user name and tenant ID
   * Replace `APPLICATION_ID` with the application ID of your`kubectl` application ID
   * Replace `APISERVER_APPLICATION_ID` with the application ID of your `apiserver` application ID 

 6. The access token is acquired when first `kubectl` command is executed

   ```
   kubectl get pods

   To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code DEC7D48GA to authenticate.
   ```

   * After signing in a web browser, the token is stored in the configuration, and it will be reused when executing next commands.
# Kubernetes

[![Submit Queue Widget]][Submit Queue] [![GoDoc Widget]][GoDoc]

<img src="https://github.com/kubernetes/kubernetes/raw/master/logo/logo.png" width="100">

----

Kubernetes is an open source system for managing [containerized applications]
across multiple hosts, providing basic mechanisms for deployment, maintenance,
and scaling of applications.

Kubernetes builds upon a decade and a half of experience at Google running
production workloads at scale using a system called [Borg],
combined with best-of-breed ideas and practices from the community.

Kubernetes is hosted by the Cloud Native Computing Foundation ([CNCF]).
If you are a company that wants to help shape the evolution of
technologies that are container-packaged, dynamically-scheduled
and microservices-oriented, consider joining the CNCF.
For details about who's involved and how Kubernetes plays a role,
read the CNCF [announcement].

----

## To start using Kubernetes

See our documentation on [kubernetes.io].

Try our [interactive tutorial].

Take a free course on [Scalable Microservices with Kubernetes].

## To start developing Kubernetes

The [community repository] hosts all information about
building Kubernetes from source, how to contribute code
and documentation, who to contact about what, etc.

If you want to build Kubernetes right away there are two options:

##### You have a working [Go environment].

```
$ go get -d k8s.io/kubernetes
$ cd $GOPATH/src/k8s.io/kubernetes
$ make
```

##### You have a working [Docker environment].

```
$ git clone https://github.com/kubernetes/kubernetes
$ cd kubernetes
$ make quick-release
```

If you are less impatient, head over to the [developer's documentation].

## Support

If you need support, start with the [troubleshooting guide]
and work your way through the process that we've outlined.

That said, if you have questions, reach out to us
[one way or another][communication].

[announcement]: https://cncf.io/news/announcement/2015/07/new-cloud-native-computing-foundation-drive-alignment-among-container
[Borg]: https://research.google.com/pubs/pub43438.html
[CNCF]: https://www.cncf.io/about
[communication]: https://github.com/kubernetes/community/blob/master/communication.md
[community repository]: https://github.com/kubernetes/community
[containerized applications]: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/
[developer's documentation]: https://github.com/kubernetes/community/tree/master/contributors/devel
[Docker environment]: https://docs.docker.com/engine
[Go environment]: https://golang.org/doc/install
[GoDoc]: https://godoc.org/k8s.io/kubernetes
[GoDoc Widget]: https://godoc.org/k8s.io/kubernetes?status.svg
[interactive tutorial]: http://kubernetes.io/docs/tutorials/kubernetes-basics
[kubernetes.io]: http://kubernetes.io
[Scalable Microservices with Kubernetes]: https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615
[Submit Queue]: http://submit-queue.k8s.io/#/e2e
[Submit Queue Widget]: http://submit-queue.k8s.io/health.svg?v=1
[troubleshooting guide]: https://kubernetes.io/docs/tasks/debug-application-cluster/troubleshooting/ 

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/README.md?pixel)]()
# Readme

URL: https://github.com/swagger-api/swagger-ui/tree/master/dist
License: Apache License, Version 2.0
License File: LICENSE

## Description
Files from dist folder of https://github.com/swagger-api/swagger-ui.
These are dependency-free collection of HTML, Javascript, and CSS assets that
dynamically generate beautiful documentation and sandbox from a
Swagger-compliant API.
Instructions on how to use these:
https://github.com/swagger-api/swagger-ui#how-to-use-it

## Local Modifications
- Updated the url in index.html to "../../swaggerapi" as per instructions at:
https://github.com/swagger-api/swagger-ui#how-to-use-it
- Modified swagger-ui.js to list resources and operations in sorted order: https://github.com/kubernetes/kubernetes/pull/3421
- Set supportedSubmitMethods: [] in index.html to remove "Try it out" buttons.
- Remove the url query param to fix XSS issue:
  https://github.com/kubernetes/kubernetes/pull/23234

LICENSE file has been created for compliance purposes.
Not included in original distribution.
Forked from gonum/graph@50b27dea7ebbfb052dfaf91681afc6fde28d8796 to support memory-use improvements to the simple graph
Forked from etcd 2.3 release branch to support migration from 3.0 WAL to 2.3 WAL format
Forked from etcd 2.2 release branch to support migration from 3.0 WAL to 2.2 WAL format
# intemp

A bash script to execute a command within a temporary work directory.


## Dependencies

Requires: mktemp


## Install

```
git clone https://github.com/karlkfi/intemp
cd intemp
make install
```

or

```
curl -o- https://raw.githubusercontent.com/karlkfi/intemp/master/install.sh | bash
```

## Usage

```
intemp.sh [-t prefix] "<command>"
```

Example (install intemp using intemp):

```
intemp.sh -t intemp "git clone https://github.com/karlkfi/intemp . && make install"
```


## License

Copyright 2015 Karl Isenberg

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.# Kubernetes Examples: releases.k8s.io/HEAD

This directory contains a number of examples of how to run
real applications with Kubernetes.

Demonstrations of how to use specific Kubernetes features can be found in our [documents](https://kubernetes.io/docs/).


### Maintained Examples

Maintained Examples are expected to be updated with every Kubernetes
release, to use the latest and greatest features, current guidelines
and best practices, and to refresh command syntax, output, changed
prerequisites, as needed.

|Name | Description | Notable Features Used | Complexity Level|
------------- | ------------- | ------------ | ------------ | 
|[Guestbook](guestbook/) | PHP app with Redis | Replication Controller, Service | Beginner |
|[WordPress](mysql-wordpress-pd/) | WordPress with MySQL | Deployment, Persistent Volume with Claim | Beginner|
|[Cassandra](storage/cassandra/) | Cloud Native Cassandra | Daemon Set | Intermediate 

* Note: Please add examples to the list above that are maintained.

See [Example Guidelines](guidelines.md) for a description of what goes
in this directory, and what examples should contain.

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Runtime Constraints example

This example demonstrates how Kubernetes enforces runtime constraints for compute resources.

### Prerequisites

For the purpose of this example, we will spin up a 1 node cluster using the Vagrant provider that
is not running with any additional add-ons that consume node resources.  This keeps our demonstration
of compute resources easier to follow by starting with an empty cluster.

```
$ export KUBERNETES_PROVIDER=vagrant
$ export NUM_NODES=1
$ export KUBE_ENABLE_CLUSTER_MONITORING=none
$ export KUBE_ENABLE_CLUSTER_DNS=false
$ export KUBE_ENABLE_CLUSTER_UI=false
$ cluster/kube-up.sh
```

We should now have a single node cluster running 0 pods.

```
$ cluster/kubectl.sh get nodes
NAME         LABELS                              STATUS    AGE
10.245.1.3   kubernetes.io/hostname=10.245.1.3   Ready     17m
$ cluster/kubectl.sh get pods --all-namespaces
```

When demonstrating runtime constraints, it's useful to show what happens when a node is under heavy load.  For
this scenario, we have a single node with 2 cpus and 1GB of memory to demonstrate behavior under load, but the
results extend to multi-node scenarios.

### CPU requests

Each container in a pod may specify the amount of CPU it requests on a node.  CPU requests are used at schedule time, and represent a minimum amount of CPU that should be reserved for your container to run.

When executing your container, the Kubelet maps your containers CPU requests to CFS shares in the Linux kernel.  CFS CPU shares do not impose a ceiling on the actual amount of CPU the container can use.  Instead, it defines a relative weight across all containers on the system for how much CPU time the container should get if there is CPU contention.

Let's demonstrate this concept using a simple container that will consume as much CPU as possible.

```
$ cluster/kubectl.sh run cpuhog \
    --image=busybox \
    --requests=cpu=100m \
    -- md5sum /dev/urandom
```

This will create a single pod on your node that requests 1/10 of a CPU, but it has no limit on how much CPU it may actually consume
on the node.

To demonstrate this, if you SSH into your machine, you will see it is consuming as much CPU as possible on the node.

```
$ vagrant ssh node-1
$ sudo docker stats $(sudo docker ps -q)
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
6b593b1a9658        0.00%               1.425 MB/1.042 GB   0.14%               1.038 kB/738 B
ae8ae4ffcfe4        150.06%             831.5 kB/1.042 GB   0.08%               0 B/0 B
```

As you can see, its consuming 150% of the total CPU.

If we scale our replication controller to 20 pods, we should see that each container is given an equal proportion of CPU time.

```
$ cluster/kubectl.sh scale rc/cpuhog --replicas=20
```

Once all the pods are running, you will see on your node that each container is getting approximately an equal proportion of CPU time.

```
$ sudo docker stats $(sudo docker ps -q)
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
089e2d061dee        9.24%               786.4 kB/1.042 GB   0.08%               0 B/0 B
0be33d6e8ddb        10.48%              823.3 kB/1.042 GB   0.08%               0 B/0 B
0f4e3c4a93e0        10.43%              786.4 kB/1.042 GB   0.08%               0 B/0 B
```

Each container is getting 10% of the CPU time per their scheduling request, and we are unable to schedule more.

As you can see CPU requests are used to schedule pods to the node in a manner that provides weighted distribution of CPU time
when under contention.  If the node is not being actively consumed by other containers, a container is able to burst up to as much
available CPU time as possible.  If there is contention for CPU, CPU time is shared based on the requested value.

Let's delete all existing resources in preparation for the next scenario.  Verify all the pods are deleted and terminated.

```
$ cluster/kubectl.sh delete rc --all
$ cluster/kubectl.sh get pods
NAME      READY     STATUS    RESTARTS   AGE
```

### CPU limits

So what do you do if you want to control the maximum amount of CPU that your container can burst to use in order provide a consistent
level of service independent of CPU contention on the node?  You can specify an upper limit on the total amount of CPU that a pod's
container may consume.

To enforce this feature, your node must run a docker version >= 1.7, and your operating system kernel must
have support for CFS quota enabled.  Finally, your the Kubelet must be started with the following flag:

```
kubelet --cpu-cfs-quota=true
```

To demonstrate, let's create the same pod again, but this time set an upper limit to use 50% of a single CPU.

```
$ cluster/kubectl.sh run cpuhog \
    --image=busybox \
    --requests=cpu=100m \
    --limits=cpu=500m \
    -- md5sum /dev/urandom
```

Let's SSH into the node, and look at usage stats.

```
$ vagrant ssh node-1
$ sudo su
$ docker stats $(docker ps -q)
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
2a196edf7de2        47.38%              835.6 kB/1.042 GB   0.08%               0 B/0 B
...
```

As you can see, the container is no longer allowed to consume all available CPU on the node.  Instead, it is being limited to use
50% of a CPU over every 100ms period.  As a result, the reported value will be in the range of 50% but may oscillate above and below.

Let's delete all existing resources in preparation for the next scenario.  Verify all the pods are deleted and terminated.

```
$ cluster/kubectl.sh delete rc --all
$ cluster/kubectl.sh get pods
NAME      READY     STATUS    RESTARTS   AGE
```

### Memory requests

By default, a container is able to consume as much memory on the node as possible.  In order to improve placement of your
pods in the cluster, it is recommended to specify the amount of memory your container will require to run.  The scheduler
will then take available node memory capacity into account prior to binding your pod to a node.

Let's demonstrate this by creating a pod that runs a single container which requests 100Mi of memory.  The container will
allocate and write to 200MB of memory every 2 seconds.

```
$ cluster/kubectl.sh run memhog \
   --image=derekwaynecarr/memhog \
   --requests=memory=100Mi \
   --command \
   -- /bin/sh -c "while true; do memhog -r100 200m; sleep 1; done"
```

If you look at output of docker stats on the node:

```
$ docker stats $(docker ps -q)
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
2badf74ae782        0.00%               1.425 MB/1.042 GB   0.14%               816 B/348 B
a320182967fa        105.81%             214.2 MB/1.042 GB   20.56%              0 B/0 B

```

As you can see, the container is using approximately 200MB of memory, and is only limited to the 1GB of memory on the node.

We scheduled against 100Mi, but have burst our memory usage to a greater value.

We refer to this as memory having __Burstable__ quality of service for this container.

Let's delete all existing resources in preparation for the next scenario.  Verify all the pods are deleted and terminated.

```
$ cluster/kubectl.sh delete rc --all
$ cluster/kubectl.sh get pods
NAME      READY     STATUS    RESTARTS   AGE
```

### Memory limits

If you specify a memory limit, you can constrain the amount of memory your container can use.

For example, let's limit our container to 200Mi of memory, and just consume 100MB.

```
$ cluster/kubectl.sh run memhog \
   --image=derekwaynecarr/memhog \
   --limits=memory=200Mi \
   --command -- /bin/sh -c "while true; do memhog -r100 100m; sleep 1; done"
```

If you look at output of docker stats on the node:

```
$ docker stats $(docker ps -q)
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
5a7c22ae1837        125.23%             109.4 MB/209.7 MB   52.14%              0 B/0 B
c1d7579c9291        0.00%               1.421 MB/1.042 GB   0.14%               1.038 kB/816 B
```

As you can see, we are limited to 200Mi memory, and are only consuming 109.4MB on the node.

Let's demonstrate what happens if you exceed your allowed memory usage by creating a replication controller
whose pod will keep being OOM killed because it attempts to allocate 300MB of memory, but is limited to 200Mi.

```
$ cluster/kubectl.sh run memhog-oom    --image=derekwaynecarr/memhog    --limits=memory=200Mi    --command -- memhog -r100 300m
```

If we describe the created pod, you will see that it keeps restarting until it ultimately goes into a CrashLoopBackOff.

The reason it is killed and restarts is because it is OOMKilled as it attempts to exceed its memory limit.

```
$ cluster/kubectl.sh get pods
NAME               READY     STATUS             RESTARTS   AGE
memhog-oom-gj9hw   0/1       CrashLoopBackOff   2          26s
$ cluster/kubectl.sh describe pods/memhog-oom-gj9hw | grep -C 3 "Terminated"
      memory:           200Mi
    State:          Waiting
      Reason:           CrashLoopBackOff
    Last Termination State: Terminated
      Reason:           OOMKilled
      Exit Code:        137
      Started:          Wed, 23 Sep 2015 15:23:58 -0400
```

Let's clean-up before proceeding further.

```
$ cluster/kubectl.sh delete rc --all
```

### What if my node runs out of memory?

If you only schedule __Guaranteed__ memory containers, where the request is equal to the limit, then you are not in major danger of
causing an OOM event on your node.  If any individual container consumes more than their specified limit, it will be killed.

If you schedule __BestEffort__ memory containers, where the request and limit is not specified, or __Burstable__ memory containers, where
the request is less than any specified limit, then it is possible that a container will request more memory than what is actually available on the node.

If this occurs, the system will attempt to prioritize the containers that are killed based on their quality of service.  This is done
by using the OOMScoreAdjust feature in the Linux kernel which provides a heuristic to rank a process between -1000 and 1000.  Processes
with lower values are preserved in favor of processes with higher values.  The system daemons (kubelet, kube-proxy, docker) all run with
low OOMScoreAdjust values.

In simplest terms, containers with __Guaranteed__ memory containers are given a lower value than __Burstable__ containers which has
a lower value than __BestEffort__ containers.  As a consequence, containers with __BestEffort__ should be killed before the other tiers.

To demonstrate this, let's spin up a set of different replication controllers that will over commit the node.

```
$ cluster/kubectl.sh run mem-guaranteed --image=derekwaynecarr/memhog --replicas=2 --requests=cpu=10m --limits=memory=600Mi --command -- memhog -r100000 500m
$ cluster/kubectl.sh run mem-burstable --image=derekwaynecarr/memhog --replicas=2 --requests=cpu=10m,memory=600Mi --command -- memhog -r100000 100m
$ cluster/kubectl.sh run mem-besteffort --replicas=10 --image=derekwaynecarr/memhog --requests=cpu=10m --command -- memhog -r10000 500m
```

This will induce a SystemOOM

```
$ cluster/kubectl.sh get events | grep OOM
43m       8m        178       10.245.1.3             Node                                                        SystemOOM          {kubelet 10.245.1.3}        System OOM encountered
```

If you look at the pods:

```
$ cluster/kubectl.sh get pods
NAME                   READY     STATUS             RESTARTS   AGE
...
mem-besteffort-zpnpm   0/1       CrashLoopBackOff   4          3m
mem-burstable-n0yz1    1/1       Running            0          4m
mem-burstable-q3dts    1/1       Running            0          4m
mem-guaranteed-fqsw8   1/1       Running            0          4m
mem-guaranteed-rkqso   1/1       Running            0          4m
```

You see that our BestEffort pod goes in a restart cycle, but the pods with greater levels of quality of service continue to function.

As you can see, we rely on the Kernel to react to system OOM events.  Depending on how your host operating
system was configured, and which process the Kernel ultimately decides to kill on your Node, you may experience unstable results.  In addition, during an OOM event, while the kernel is cleaning up processes, the system may experience significant periods of slow down or appear unresponsive.  As a result, while the system allows you to overcommit on memory, we recommend to not induce a Kernel sys OOM.

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/runtime-constraints/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
### explorer

Explorer is a little container for examining the runtime environment Kubernetes produces for your pods.

The intended use is to substitute gcr.io/google_containers/explorer for your intended container, and then visit it via the proxy.

Currently, you can look at:
 * The environment variables to make sure Kubernetes is doing what you expect.
 * The filesystem to make sure the mounted volumes and files are also what you expect.
 * Perform DNS lookups, to see how DNS works.

`pod.yaml` is supplied as an example. You can control the port it serves on with the -port flag.

Example from command line (the DNS lookup looks better from a web browser):

```console
$ kubectl create -f examples/explorer/pod.yaml
$ kubectl proxy &
Starting to serve on localhost:8001

$ curl localhost:8001/api/v1/proxy/namespaces/default/pods/explorer:8080/vars/
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=explorer
KIBANA_LOGGING_PORT_5601_TCP_PORT=5601
KUBERNETES_SERVICE_HOST=10.0.0.2
MONITORING_GRAFANA_PORT_80_TCP_PROTO=tcp
MONITORING_INFLUXDB_UI_PORT_80_TCP_PROTO=tcp
KIBANA_LOGGING_SERVICE_PORT=5601
MONITORING_HEAPSTER_PORT_80_TCP_PORT=80
MONITORING_INFLUXDB_UI_PORT_80_TCP_PORT=80
KIBANA_LOGGING_SERVICE_HOST=10.0.204.206
KIBANA_LOGGING_PORT_5601_TCP=tcp://10.0.204.206:5601
KUBERNETES_PORT=tcp://10.0.0.2:443
MONITORING_INFLUXDB_PORT=tcp://10.0.2.30:80
MONITORING_INFLUXDB_PORT_80_TCP_PROTO=tcp
MONITORING_INFLUXDB_UI_PORT=tcp://10.0.36.78:80
KUBE_DNS_PORT_53_UDP=udp://10.0.0.10:53
MONITORING_INFLUXDB_SERVICE_HOST=10.0.2.30
ELASTICSEARCH_LOGGING_PORT=tcp://10.0.48.200:9200
ELASTICSEARCH_LOGGING_PORT_9200_TCP_PORT=9200
KUBERNETES_PORT_443_TCP=tcp://10.0.0.2:443
ELASTICSEARCH_LOGGING_PORT_9200_TCP_PROTO=tcp
KIBANA_LOGGING_PORT_5601_TCP_ADDR=10.0.204.206
KUBE_DNS_PORT_53_UDP_ADDR=10.0.0.10
MONITORING_HEAPSTER_PORT_80_TCP_PROTO=tcp
MONITORING_INFLUXDB_PORT_80_TCP_ADDR=10.0.2.30
KIBANA_LOGGING_PORT=tcp://10.0.204.206:5601
MONITORING_GRAFANA_SERVICE_PORT=80
MONITORING_HEAPSTER_SERVICE_PORT=80
MONITORING_HEAPSTER_PORT_80_TCP=tcp://10.0.150.238:80
ELASTICSEARCH_LOGGING_PORT_9200_TCP=tcp://10.0.48.200:9200
ELASTICSEARCH_LOGGING_PORT_9200_TCP_ADDR=10.0.48.200
MONITORING_GRAFANA_PORT_80_TCP_PORT=80
MONITORING_HEAPSTER_PORT=tcp://10.0.150.238:80
MONITORING_INFLUXDB_PORT_80_TCP=tcp://10.0.2.30:80
KUBE_DNS_SERVICE_PORT=53
KUBE_DNS_PORT_53_UDP_PORT=53
MONITORING_GRAFANA_PORT_80_TCP_ADDR=10.0.100.174
MONITORING_INFLUXDB_UI_SERVICE_HOST=10.0.36.78
KIBANA_LOGGING_PORT_5601_TCP_PROTO=tcp
MONITORING_GRAFANA_PORT=tcp://10.0.100.174:80
MONITORING_INFLUXDB_UI_PORT_80_TCP_ADDR=10.0.36.78
KUBE_DNS_SERVICE_HOST=10.0.0.10
KUBERNETES_PORT_443_TCP_PORT=443
MONITORING_HEAPSTER_PORT_80_TCP_ADDR=10.0.150.238
MONITORING_INFLUXDB_UI_SERVICE_PORT=80
KUBE_DNS_PORT=udp://10.0.0.10:53
ELASTICSEARCH_LOGGING_SERVICE_HOST=10.0.48.200
KUBERNETES_SERVICE_PORT=443
MONITORING_HEAPSTER_SERVICE_HOST=10.0.150.238
MONITORING_INFLUXDB_SERVICE_PORT=80
MONITORING_INFLUXDB_PORT_80_TCP_PORT=80
KUBE_DNS_PORT_53_UDP_PROTO=udp
MONITORING_GRAFANA_PORT_80_TCP=tcp://10.0.100.174:80
ELASTICSEARCH_LOGGING_SERVICE_PORT=9200
MONITORING_GRAFANA_SERVICE_HOST=10.0.100.174
MONITORING_INFLUXDB_UI_PORT_80_TCP=tcp://10.0.36.78:80
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.0.0.2
HOME=/

$ curl localhost:8001/api/v1/proxy/namespaces/default/pods/explorer:8080/fs/
mount/
var/
.dockerenv
etc/
dev/
proc/
.dockerinit
sys/
README.md
explorer

$ curl localhost:8001/api/v1/proxy/namespaces/default/pods/explorer:8080/dns?q=elasticsearch-logging
<html><head></head><body>
<form action="/api/v1/proxy/namespaces/default/pods/explorer:8080/dns">
<input name="q" type="text" value="elasticsearch-logging"/>
<button type="submit">Lookup</button>
</form>
<br/><br/><pre>LookupNS(elasticsearch-logging):
Result: ([]*net.NS)<nil>
Error: &lt;*&gt;lookup elasticsearch-logging: no such host

LookupTXT(elasticsearch-logging):
Result: ([]string)<nil>
Error: &lt;*&gt;lookup elasticsearch-logging: no such host

LookupSRV(&#34;&#34;, &#34;&#34;, elasticsearch-logging):
cname: elasticsearch-logging.default.svc.cluster.local.
Result: ([]*net.SRV)[&lt;*&gt;{Target:(string)elasticsearch-logging.default.svc.cluster.local. Port:(uint16)9200 Priority:(uint16)10 Weight:(uint16)100}]
Error: <nil>

LookupHost(elasticsearch-logging):
Result: ([]string)[10.0.60.245]
Error: <nil>

LookupIP(elasticsearch-logging):
Result: ([]net.IP)[10.0.60.245]
Error: <nil>

LookupMX(elasticsearch-logging):
Result: ([]*net.MX)<nil>
Error: &lt;*&gt;lookup elasticsearch-logging: no such host

</nil></nil></nil></nil></nil></nil></pre>

</body></html>
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/explorer/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->

This file has moved to: http://kubernetes.io/docs/user-guide/jobs/


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/job/expansions/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->

This file has moved to: http://kubernetes.io/docs/user-guide/jobs/


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/job/work-queue-1/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->

This file has moved to: http://kubernetes.io/docs/user-guide/jobs/


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/job/work-queue-2/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Persistent Volume Provisioning

This example shows how to use dynamic persistent volume provisioning.

### Prerequisites

This example assumes that you have an understanding of Kubernetes administration and can modify the
scripts that launch kube-controller-manager.

### Admin Configuration

The admin must define `StorageClass` objects that describe named "classes" of storage offered in a cluster. Different classes might map to arbitrary levels or policies determined by the admin. When configuring a `StorageClass` object for persistent volume provisioning, the admin will need to describe the type of provisioner to use and the parameters that will be used by the provisioner when it provisions a `PersistentVolume` belonging to the class.

The name of a StorageClass object is significant, and is how users can request a particular class, by specifying the name in their `PersistentVolumeClaim`. The `provisioner` field must be specified as it determines what volume plugin is used for provisioning PVs. The `parameters` field contains the parameters that describe volumes belonging to the storage class. Different parameters may be accepted depending on the `provisioner`. For example, the value `io1`, for the parameter `type`, and the parameter `iopsPerGB` are specific to EBS . When a parameter is omitted, some default is used.

See [Kubernetes StorageClass documentation](https://kubernetes.io/docs/user-guide/persistent-volumes/#storageclasses) for complete reference of all supported parameters.

#### AWS

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: slow
provisioner: kubernetes.io/aws-ebs
parameters:
  type: io1
  zones: us-east-1d, us-east-1c
  iopsPerGB: "10"
```

* `type`: `io1`, `gp2`, `sc1`, `st1`. See AWS docs for details. Default: `gp2`.
* `zone`: AWS zone. If neither zone nor zones is specified, volumes are generally round-robin-ed across all active zones where Kubernetes cluster has a node. Note: zone and zones parameters must not be used at the same time.
* `zones`: a comma separated list of AWS zone(s). If neither zone nor zones is specified, volumes are generally round-robin-ed across all active zones where Kubernetes cluster has a node. Note: zone and zones parameters must not be used at the same time.
* `iopsPerGB`: only for `io1` volumes. I/O operations per second per GiB. AWS volume plugin multiplies this with size of requested volume to compute IOPS of the volume and caps it at 20 000 IOPS (maximum supported by AWS, see AWS docs).
* `encrypted`: denotes whether the EBS volume should be encrypted or not. Valid values are `true` or `false`.
* `kmsKeyId`: optional. The full Amazon Resource Name of the key to use when encrypting the volume. If none is supplied but `encrypted` is true, a key is generated by AWS. See AWS docs for valid ARN value.

#### GCE

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: slow
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard
  zones: us-central1-a, us-central1-b
```

* `type`: `pd-standard` or `pd-ssd`. Default: `pd-ssd`
* `zone`: GCE zone. If neither zone nor zones is specified, volumes are generally round-robin-ed across all active zones where Kubernetes cluster has a node. Note: zone and zones parameters must not be used at the same time.
* `zones`: a comma separated list of GCE zone(s). If neither zone nor zones is specified, volumes are generally round-robin-ed across all active zones where Kubernetes cluster has a node. Note: zone and zones parameters must not be used at the same time.

#### vSphere

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: slow
provisioner: kubernetes.io/vsphere-volume
parameters:
  diskformat: eagerzeroedthick
  fstype:     ext3
```

* `diskformat`: `thin`, `zeroedthick` and `eagerzeroedthick`. See vSphere docs for details. Default: `"thin"`.
* `fstype`: fstype that are supported by kubernetes. Default: `"ext4"`.

#### Portworx Volume

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: portworx-io-priority-high
provisioner: kubernetes.io/portworx-volume
parameters:
  repl: "1"
  snap_interval:   "70"
  io_priority:  "high"

```

*  `fs`: filesystem to be laid out: [none/xfs/ext4] (default: `ext4`)
*  `block_size`: block size in Kbytes (default: `32`)
*  `repl`: replication factor [1..3] (default: `1`)
*  `io_priority`: IO Priority: [high/medium/low] (default: `low`)
*  `snap_interval`: snapshot interval in minutes, 0 disables snaps (default: `0`)
*  `aggregation_level`: specifies the number of chunks the volume would be distributed into, 0 indicates a non-aggregated volume (default: `0`)
*  `ephemeral`: ephemeral storage [true/false] (default `false`)

For a complete example refer ([Portworx Volume docs](../volumes/portworx/README.md))

#### StorageOS

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: sc-fast
provisioner: kubernetes.io/storageos
parameters:
  pool: default
  description: Kubernetes volume
  fsType: ext4
  adminSecretNamespace: default
  adminSecretName: storageos-secret
```

*  `pool`: The name of the StorageOS distributed capacity pool to provision the volume from.  Uses the `default` pool which is normally present if not specified.
*  `description`: The description to assign to volumes that were created dynamically.  All volume descriptions will be the same for the storage class, but different storage classes can be used to allow descriptions for different use cases.  Defaults to `Kubernetes volume`.
*  `fsType`: The default filesystem type to request.  Note that user-defined rules within StorageOS may override this value.  Defaults to `ext4`.
*  `adminSecretNamespace`: The namespace where the API configuration secret is located. Required if adminSecretName set.
*  `adminSecretName`: The name of the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.

For a complete example refer to the ([StorageOS example](../../volumes/storageos/README.md))

#### GLUSTERFS

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: slow
provisioner: kubernetes.io/glusterfs
parameters:
  resturl: "http://127.0.0.1:8081"
  clusterid: "630372ccdc720a92c681fb928f27b53f"
  restuser: "admin"
  secretNamespace: "default"
  secretName: "heketi-secret"
  gidMin: "40000"
  gidMax: "50000"
  volumetype: "replicate:3"
```

Example storageclass can be found in [glusterfs-storageclass.yaml](glusterfs/glusterfs-storageclass.yaml).

* `resturl` : Gluster REST service/Heketi service url which provision gluster volumes on demand. The general format should be `IPaddress:Port` and this is a mandatory parameter for GlusterFS dynamic provisioner. If Heketi service is exposed as a routable service in openshift/kubernetes setup, this can have a format similar to
`http://heketi-storage-project.cloudapps.mystorage.com` where the fqdn is a resolvable heketi service url.

* `restauthenabled` : Gluster REST service authentication boolean that enables authentication to the REST server. If this value is 'true', `restuser` and `restuserkey` or `secretNamespace` + `secretName` have to be filled. This option is deprecated, authentication is enabled when any of `restuser`, `restuserkey`, `secretName` or `secretNamespace` is specified.

* `restuser` : Gluster REST service/Heketi user who has access to create volumes in the Gluster Trusted Pool.

* `restuserkey` : Gluster REST service/Heketi user's password which will be used for authentication to the REST server. This parameter is deprecated in favor of `secretNamespace` + `secretName`.

* `secretNamespace` + `secretName` : Identification of Secret instance that contains user password to use when talking to Gluster REST service. These parameters are optional, empty password will be used when both `secretNamespace` and `secretName` are omitted. The provided secret must have type "kubernetes.io/glusterfs".
When both `restuserkey` and `secretNamespace` + `secretName` is specified, the secret will be used.

* `clusterid`: `630372ccdc720a92c681fb928f27b53f` is the ID of the cluster which will be used by Heketi when provisioning the volume. It can also be a list of clusterids, for ex:
"8452344e2becec931ece4e33c4674e4e,42982310de6c63381718ccfa6d8cf397". This is an optional parameter.

Example of a secret can be found in [glusterfs-secret.yaml](glusterfs/glusterfs-secret.yaml).

* `gidMin` + `gidMax` : The minimum and maximum value of GID range for the storage class. A unique value (GID) in this range ( gidMin-gidMax ) will be used for dynamically provisioned volumes. These are optional values. If not specified, the volume will be provisioned with a value between 2000-2147483647 which are defaults for gidMin and gidMax respectively.

* `volumetype` : The volume type and its parameters can be configured with this optional value. If the volume type is not mentioned, it's up to the provisioner to decide the volume type.
For example:

  'Replica volume':
    `volumetype: replicate:3` where '3' is replica count.
  'Disperse/EC volume':
    `volumetype: disperse:4:2` where '4' is data and '2' is the redundancy count.
  'Distribute volume':
    `volumetype: none`

For available volume types and its administration options refer: ([Administration Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Storage/3.1/html/Administration_Guide/part-Overview.html))

Reference : ([How to configure Gluster on Kubernetes](https://github.com/gluster/gluster-kubernetes/blob/master/docs/setup-guide.md))

Reference : ([How to configure Heketi](https://github.com/heketi/heketi/wiki/Setting-up-the-topology))

When the persistent volumes are dynamically provisioned, the Gluster plugin automatically create an endpoint and a headless service in the name `gluster-dynamic-<claimname>`. This dynamic endpoint and service will be deleted automatically when the persistent volume claim is deleted.


#### OpenStack Cinder

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: gold
provisioner: kubernetes.io/cinder
parameters:
  type: fast
  availability: nova
```

* `type`: [VolumeType](http://docs.openstack.org/admin-guide/dashboard-manage-volumes.html) created in Cinder. Default is empty.
* `availability`: Availability Zone. Default is empty.

#### Ceph RBD

```yaml
  apiVersion: storage.k8s.io/v1
  kind: StorageClass
  metadata:
    name: fast
  provisioner: kubernetes.io/rbd
  parameters:
    monitors: 10.16.153.105:6789
    adminId: kube
    adminSecretName: ceph-secret
    adminSecretNamespace: kube-system
    pool: kube
    userId: kube
    userSecretName: ceph-secret-user
    imageFormat: "1"
```

* `monitors`: Ceph monitors, comma delimited. It is required.
* `adminId`: Ceph client ID that is capable of creating images in the pool. Default is "admin".
* `adminSecret`: Secret Name for `adminId`. It is required. The provided secret must have type "kubernetes.io/rbd".
* `adminSecretNamespace`: The namespace for `adminSecret`. Default is "default".
* `pool`: Ceph RBD pool. Default is "rbd".
* `userId`: Ceph client ID that is used to map the RBD image. Default is the same as `adminId`.
* `userSecretName`: The name of Ceph Secret for `userId` to map RBD image. It must exist in the same namespace as PVCs. It is required.
* `imageFormat`: Ceph RBD image format, "1" or "2". Default is "1".
* `imageFeatures`: Ceph RBD image format 2 features, comma delimited. This is optional, and only be used if you set `imageFormat` to "2". Currently supported features are `layering` only. Default is "", no features is turned on.

NOTE: We cannot turn on `exclusive-lock` feature for now (and `object-map`, `fast-diff`, `journaling` which require `exclusive-lock`), because exclusive lock and advisory lock cannot work together. (See [#45805](https://issue.k8s.io/45805))

#### Quobyte

<!-- BEGIN MUNGE: EXAMPLE quobyte/quobyte-storage-class.yaml -->

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
   name: slow
provisioner: kubernetes.io/quobyte
parameters:
    quobyteAPIServer: "http://138.68.74.142:7860"
    registry: "138.68.74.142:7861"
    adminSecretName: "quobyte-admin-secret"
    adminSecretNamespace: "kube-system"
    user: "root"
    group: "root"
    quobyteConfig: "BASE"
    quobyteTenant: "DEFAULT"
```

[Download example](quobyte/quobyte-storage-class.yaml?raw=true)
<!-- END MUNGE: EXAMPLE quobyte/quobyte-storage-class.yaml -->

* **quobyteAPIServer** API Server of Quobyte in the format http(s)://api-server:7860
* **registry** Quobyte registry to use to mount the volume. You can specify the registry as <host>:<port> pair or if you want to specify multiple registries you just have to put a comma between them e.q. <host1>:<port>,<host2>:<port>,<host3>:<port>. The host can be an IP address or if you have a working DNS you can also provide the DNS names.
* **adminSecretName** secret that holds information about the Quobyte user and the password to authenticate against the API server. The provided secret must have type "kubernetes.io/quobyte".
* **adminSecretNamespace** The namespace for **adminSecretName**. Default is `default`.
* **user** maps all access to this user. Default is `root`.
* **group** maps all access to this group. Default is `nfsnobody`.
* **quobyteConfig** use the specified configuration to create the volume. You can create a new configuration or modify an existing one with the Web console or the quobyte CLI. Default is `BASE`
* **quobyteTenant** use the specified tenant ID to create/delete the volume. This Quobyte tenant has to be already present in Quobyte. For Quobyte < 1.4 use an empty string `""` as `DEFAULT` tenant. Default is `DEFAULT`

First create Quobyte admin's Secret in the system namespace. Here the Secret is created in `kube-system`:

```
$ kubectl create -f examples/persistent-volume-provisioning/quobyte/quobyte-admin-secret.yaml --namespace=kube-system
```

Then create the Quobyte storage class:

```
$ kubectl create -f examples/persistent-volume-provisioning/quobyte/quobyte-storage-class.yaml
```

Now create a PVC

```
$ kubectl create -f examples/persistent-volume-provisioning/claim1.json
```

Check the created PVC:

```
$ kubectl describe pvc
Name:       claim1
Namespace:      default
Status:     Bound
Volume:     pvc-bdb82652-694a-11e6-b811-080027242396
Labels:     <none>
Capacity:       3Gi
Access Modes:   RWO
No events.

$ kubectl describe pv
Name:  		pvc-bdb82652-694a-11e6-b811-080027242396
Labels:		<none>
Status:		Bound
Claim: 		default/claim1
Reclaim Policy:	Delete
Access Modes:  	RWO
Capacity:      	3Gi
Message:
Source:
    Type:      	Quobyte (a Quobyte mount on the host that shares a pod's lifetime)
    Registry:  	138.68.79.14:7861
    Volume:    	kubernetes-dynamic-pvc-bdb97c58-694a-11e6-91b6-080027242396
    ReadOnly:  	false
No events.
```

Create a Pod to use the PVC:

```
$ kubectl create -f examples/persistent-volume-provisioning/quobyte/example-pod.yaml
```

#### <a name="azure-disk">Azure Disk</a>

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: slow
provisioner: kubernetes.io/azure-disk
parameters:
  skuName: Standard_LRS
  location: eastus
  storageAccount: azure_storage_account_name
```

* `skuName`: Azure storage account Sku tier. Default is empty.
* `location`: Azure storage account location. Default is empty.
* `storageAccount`: Azure storage account name. If storage account is not provided, all storage accounts associated with the resource group are searched to find one that matches `skuName` and `location`. If storage account is provided, it must reside in the same resource group as the cluster, and `skuName` and `location` are ignored.

#### Azure File

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1beta1
metadata:
  name: slow
provisioner: kubernetes.io/azure-file
parameters:
  skuName: Standard_LRS
  location: eastus
  storageAccount: azure_storage_account_name
```

The parameters are the same as those used by [Azure Disk](#azure-disk)

### User provisioning requests

Users request dynamically provisioned storage by including a storage class in their `PersistentVolumeClaim` using `spec.storageClassName` attribute.
It is required that this value matches the name of a `StorageClass` configured by the administrator.

```
{
  "kind": "PersistentVolumeClaim",
  "apiVersion": "v1",
  "metadata": {
    "name": "claim1"
  },
  "spec": {
    "accessModes": [
      "ReadWriteOnce"
    ],
    "resources": {
      "requests": {
        "storage": "3Gi"
      }
    },
    "storageClassName": "slow"
  }
}
```

### Sample output

#### GCE

This example uses GCE but any provisioner would follow the same flow.

First we note there are no Persistent Volumes in the cluster.  After creating a storage class and a claim including that storage class, we see a new PV is created
and automatically bound to the claim requesting storage.


```
$ kubectl get pv

$ kubectl create -f examples/persistent-volume-provisioning/gce-pd.yaml
storageclass "slow" created

$ kubectl create -f examples/persistent-volume-provisioning/claim1.json
persistentvolumeclaim "claim1" created

$ kubectl get pv
NAME                                       CAPACITY   ACCESSMODES   STATUS    CLAIM                        REASON    AGE
pvc-bb6d2f0c-534c-11e6-9348-42010af00002   3Gi        RWO           Bound     default/claim1                         4s

$ kubectl get pvc
NAME      LABELS    STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
claim1    <none>    Bound     pvc-bb6d2f0c-534c-11e6-9348-42010af00002   3Gi        RWO           7s

# delete the claim to release the volume
$ kubectl delete pvc claim1
persistentvolumeclaim "claim1" deleted

# the volume is deleted in response to being release of its claim
$ kubectl get pv

```


#### Ceph RBD

This section will guide you on how to configure and use the Ceph RBD provisioner.

##### Pre-requisites

For this to work you must have a functional Ceph cluster, and the `rbd` command line utility must be installed on any host/container that `kube-controller-manager` or `kubelet` is running on.

##### Configuration

First we must identify the Ceph client admin key. This is usually found in `/etc/ceph/ceph.client.admin.keyring` on your Ceph cluster nodes. The file will look something like this:

```
[client.admin]
  key = AQBfxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==
  auid = 0
  caps mds = "allow"
  caps mon = "allow *"
  caps osd = "allow *"
```

From the key value, we will create a secret. We must create the Ceph admin Secret in the namespace defined in our `StorageClass`. In this example we've set the namespace to `kube-system`.

```
$ kubectl create secret generic ceph-secret-admin --from-literal=key='AQBfxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==' --namespace=kube-system --type=kubernetes.io/rbd
```

Now modify `examples/persistent-volume-provisioning/rbd/rbd-storage-class.yaml` to reflect your environment, particularly the `monitors` field.  We are now ready to create our RBD Storage Class:

```
$ kubectl create -f examples/persistent-volume-provisioning/rbd/rbd-storage-class.yaml
```

The kube-controller-manager is now able to provision storage, however we still need to be able to map the RBD volume to a node. Mapping should be done with a non-privileged key, if you have existing users you can get all keys by running `ceph auth list` on your Ceph cluster with the admin key. For this example we will create a new user and pool.

```
$ ceph osd pool create kube 512
$ ceph auth get-or-create client.kube mon 'allow r' osd 'allow rwx pool=kube'
[client.kube]
	key = AQBQyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy==
```

This key will be made into a secret, just like the admin secret. However this user secret will need to be created in every namespace where you intend to consume RBD volumes provisioned in our example storage class. Let's create a namespace called `myns`, and create the user secret in that namespace.

```
kubectl create namespace myns
kubectl create secret generic ceph-secret-user --from-literal=key='AQBQyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy==' --namespace=myns --type=kubernetes.io/rbd
```

You are now ready to provision and use RBD storage.

##### Usage

With the storageclass configured, let's create a PVC in our example namespace, `myns`:

```
$ kubectl create -f examples/persistent-volume-provisioning/claim1.json --namespace=myns
```

Eventually the PVC creation will result in a PV and RBD volume to match:

```
$ kubectl describe pvc --namespace=myns
Name:		claim1
Namespace:	myns
Status:		Bound
Volume:		pvc-1cfa23b3-664b-11e6-9eb9-90b11c09520d
Labels:		<none>
Capacity:	3Gi
Access Modes:	RWO
No events.

$ kubectl describe pv
Name:		pvc-1cfa23b3-664b-11e6-9eb9-90b11c09520d
Labels:		<none>
Status:		Bound
Claim:		myns/claim1
Reclaim Policy:	Delete
Access Modes:	RWO
Capacity:	3Gi
Message:
Source:
    Type:		RBD (a Rados Block Device mount on the host that shares a pod's lifetime)
    CephMonitors:	[127.0.0.1:6789]
    RBDImage:		kubernetes-dynamic-pvc-1cfb1862-664b-11e6-9a5d-90b11c09520d
    FSType:		
    RBDPool:		kube
    RadosUser:		kube
    Keyring:		/etc/ceph/keyring
    SecretRef:		&{ceph-secret-user}
    ReadOnly:		false
No events.
```

With our storage provisioned, we can now create a Pod to use the PVC:

```
$ kubectl create -f examples/persistent-volume-provisioning/rbd/pod.yaml --namespace=myns
```

Now our pod has an RBD mount!

```
$ export PODNAME=`kubectl get pod --selector='role=server' --namespace=myns --output=template --template="{{with index .items 0}}{{.metadata.name}}{{end}}"`
$ kubectl exec -it $PODNAME --namespace=myns -- df -h | grep rbd
/dev/rbd1       2.9G  4.5M  2.8G   1% /var/lib/www/html
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/persistent-volume-provisioning/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Microsoft Operations Management Suite (OMS) Container Monitoring Example

The [Microsoft Operations Management Suite (OMS)](https://www.microsoft.com/en-us/cloud-platform/operations-management-suite) is a software-as-a-service offering from Microsoft that allows Enterprise IT to manage any hybrid cloud.

This example will create a DaemonSet to deploy the OMS Linux agents running as containers to every node in the Kubernetes cluster.

### Supported Linux Operating Systems & Docker
- Docker 1.10 thru 1.12.1

- An x64 version of the following:
	- Ubuntu 14.04 LTS, 16.04 LTS
	- CoreOS (stable)
	- Amazon Linux 2016.09.0
	- openSUSE 13.2
	- CentOS 7
	- SLES 12
	- RHEL 7.2

## Step 1

If you already have a Microsoft Azure account, you can quickly create a free OMS account by following the steps [here](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-get-started#sign-up-quickly-using-microsoft-azure).

If you don't have a Microsoft Azure account, you can create a free OMS account by following the guide [here](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-get-started#sign-up-in-3-steps-using-oms).

## Step 2

You will need to edit the [omsagent-daemonset.yaml](./omsagent-daemonset.yaml) file to add your Workspace ID and Primary Key of your OMS account.

```
- env:
        - name: WSID
          value: <your workspace ID>
        - name: KEY
          value: <your key>
```

The Workspace ID and Primary Key can be found inside the OMS Portal under Settings in the connected sources tab (see below screenshot).
![connected-resources](./images/connected-resources.png)

## Step 3

Run the following command to deploy the OMS agent to your Kubernetes nodes:

```
kubectl -f omsagent-daemonset.yaml 
```

## Step 4

Add the Container solution to your OMS workspace:

1. Log in to the OMS portal.
2. Click the Solutions Gallery tile.
3. On the OMS Solutions Gallery page, click on Containers.
4. On the page for the Containers solution, detailed information about the solution is displayed. Click Add.

A new tile for the Container solution that you added appears on the Overview page in OMS. It would take 5 minutes for your data to appear in OMS.

![oms-portal](./images/oms-portal.png)

![coms-container-solution](./images/oms-container-solution.png)## Galera Replication for MySQL on Kubernetes

This document explains a simple demonstration example of running MySQL synchronous replication using Galera, specifically, Percona XtraDB cluster. The example is simplistic and used a fixed number (3) of nodes but the idea can be built upon and made more dynamic as Kubernetes matures.

### Prerequisites

This example assumes that you have a Kubernetes cluster installed and running, and that you have installed the ```kubectl``` command line tool somewhere in your path.  Please see the [getting started](https://kubernetes.io/docs/getting-started-guides/) for installation instructions for your platform.

Also, this example requires the image found in the ```image``` directory. For your convenience, it is built and available on Docker's public image repository as ```capttofu/percona_xtradb_cluster_5_6```. It can also be built which would merely require that the image in the pod or replication controller files is updated.

This example was tested on OS X with a Galera cluster running on VMWare using the fine repo developed by Paulo Pires [https://github.com/pires/kubernetes-vagrant-coreos-cluster] and client programs built for OS X.

### Basic concept

The basic idea is this: three replication controllers with a single pod, corresponding services, and a single overall service to connect to all three nodes. One of the important design goals of MySQL replication and/or clustering is that you don't want a single-point-of-failure, hence the need to distribute each node or slave across hosts or even geographical locations. Kubernetes is well-suited for facilitating this design pattern using the service and replication controller configuration files in this example.

By defaults, there are only three pods (hence replication controllers) for this cluster. This number can be increased using the variable NUM_NODES, specified in the replication controller configuration file. It's important to know the number of nodes must always be odd.

When the replication controller is created, it results in the corresponding container to start, run an entrypoint script that installs the MySQL system tables, set up users, and build up a list of servers that is used with the galera parameter ```wsrep_cluster_address```.  This is a list of running nodes that galera uses for election of a node to obtain SST (Single State Transfer) from.

Note: Kubernetes best-practices is to pre-create the services for each controller, and the configuration files which contain the service and replication controller for each node, when created, will result in both a service and replication contrller running for the given node. An important thing to know is that it's important that initially pxc-node1.yaml be processed first and no other pxc-nodeN services that don't have corresponding replication controllers should exist. The reason for this is that if there is a node in ```wsrep_clsuter_address``` without a backing galera node there will be nothing to obtain SST from which will cause the node to shut itself down and the container in question to exit (and another soon relaunched, repeatedly).

First, create the overall cluster service that will be used to connect to the cluster:

```kubectl create -f examples/storage/mysql-galera/pxc-cluster-service.yaml```

Create the service and replication controller for the first node:

```kubectl create -f examples/storage/mysql-galera/pxc-node1.yaml```

### Create services and controllers for the remaining nodes

Repeat the same previous steps for ```pxc-node2``` and ```pxc-node3```

When complete, you should be able connect with a MySQL client to the IP address
 service ```pxc-cluster``` to find a working cluster

### An example of creating a cluster

Shown below are examples of Using ```kubectl``` from within the ```./examples/storage/mysql-galera``` directory, the status of the lauched replication controllers and services can be confirmed

```
$ kubectl create -f examples/storage/mysql-galera/pxc-cluster-service.yaml 
services/pxc-cluster

$ kubectl create -f examples/storage/mysql-galera/pxc-node1.yaml 
services/pxc-node1
replicationcontrollers/pxc-node1

$ kubectl create -f examples/storage/mysql-galera/pxc-node2.yaml 
services/pxc-node2
replicationcontrollers/pxc-node2

$ kubectl create -f examples/storage/mysql-galera/pxc-node3.yaml 
services/pxc-node3
replicationcontrollers/pxc-node3

```

### Confirm a running cluster

Verify everything is running:

```
$ kubectl get rc,pods,services
CONTROLLER   CONTAINER(S)   IMAGE(S)                                    SELECTOR           REPLICAS
pxc-node1    pxc-node1      capttofu/percona_xtradb_cluster_5_6:beta    name=pxc-node1     1
pxc-node2    pxc-node2      capttofu/percona_xtradb_cluster_5_6:beta    name=pxc-node2     1
pxc-node3    pxc-node3      capttofu/percona_xtradb_cluster_5_6:beta    name=pxc-node3     1
NAME              READY     STATUS    RESTARTS   AGE
pxc-node1-h6fqr   1/1       Running   0          41m
pxc-node2-sfqm6   1/1       Running   0          41m
pxc-node3-017b3   1/1       Running   0          40m
NAME          LABELS    SELECTOR           IP(S)            PORT(S)
pxc-cluster   <none>    unit=pxc-cluster   10.100.179.58    3306/TCP
pxc-node1     <none>    name=pxc-node1     10.100.217.202   3306/TCP
                                                            4444/TCP
                                                            4567/TCP
                                                            4568/TCP
pxc-node2     <none>    name=pxc-node2     10.100.47.212    3306/TCP
                                                            4444/TCP
                                                            4567/TCP
                                                            4568/TCP
pxc-node3     <none>    name=pxc-node3     10.100.200.14    3306/TCP
                                                            4444/TCP
                                                            4567/TCP
                                                            4568/TCP

```

The cluster should be ready for use!

### Connecting to the cluster

Using the name of ```pxc-cluster``` service running interactively using ```kubernetes exec```, it is possible to connect to any of the pods using the mysql client on the pod's container to verify the cluster size, which should be ```3```. In this example below, pxc-node3 replication controller is chosen, and to find out the pod name, ```kubectl get pods``` and ```awk``` are employed:

```
$ kubectl get pods|grep pxc-node3|awk '{ print $1 }'
pxc-node3-0b5mc

$ kubectl exec pxc-node3-0b5mc -i -t -- mysql -u root -p -h pxc-cluster

Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.6.24-72.2-56-log Percona XtraDB Cluster (GPL), Release rel72.2, Revision 43abf03, WSREP version 25.11, wsrep_25.11

Copyright (c) 2009-2015 Percona LLC and/or its affiliates
Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
1 row in set (0.06 sec)

```

At this point, there is a working cluster that can begin being used via the pxc-cluster service IP address!

### TODO

This setup certainly can become more fluid and dynamic. One idea is to perhaps use an etcd container to store information about node state. Originally, there was a read-only kubernetes API available to each container but that has since been removed. Also, Kelsey Hightower is working on moving the functionality of confd to Kubernetes. This could replace the shell duct tape that builds the cluster configuration file for the image.



<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/mysql-galera/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Vitess Example

This example shows how to run a [Vitess](http://vitess.io) cluster in Kubernetes.
Vitess is a MySQL clustering system developed at YouTube that makes sharding
transparent to the application layer. It also makes scaling MySQL within
Kubernetes as simple as launching more pods.

The example brings up a database with 2 shards, and then runs a pool of
[sharded guestbook](https://github.com/youtube/vitess/tree/master/examples/kubernetes/guestbook)
pods. The guestbook app was ported from the original
[guestbook](../../../examples/guestbook-go/)
example found elsewhere in this tree, modified to use Vitess as the backend.

For a more detailed, step-by-step explanation of this example setup, see the
[Vitess on Kubernetes](http://vitess.io/getting-started/) guide.

### Prerequisites

You'll need to install [Go 1.4+](https://golang.org/doc/install) to build
`vtctlclient`, the command-line admin tool for Vitess.

We also assume you have a running Kubernetes cluster with `kubectl` pointing to
it by default. See the [Getting Started guides](https://kubernetes.io/docs/getting-started-guides/)
for how to get to that point. Note that your Kubernetes cluster needs to have
enough resources (CPU+RAM) to schedule all the pods. By default, this example
requires a cluster-wide total of at least 6 virtual CPUs and 10GiB RAM. You can
tune these requirements in the
[resource limits](https://kubernetes.io/docs/user-guide/compute-resources.md)
section of each YAML file.

Lastly, you need to open ports 30000-30001 (for the Vitess admin daemon) and 80 (for
the guestbook app) in your firewall. See the
[Services and Firewalls](https://kubernetes.io/docs/user-guide/services-firewalls.md)
guide for examples of how to do that.

### Configure site-local settings

Run the `configure.sh` script to generate a `config.sh` file, which will be used
to customize your cluster settings.

``` console
./configure.sh
```

Currently, we have out-of-the-box support for storing
[backups](http://vitess.io/user-guide/backup-and-restore.html) in
[Google Cloud Storage](https://cloud.google.com/storage/).
If you're using GCS, fill in the fields requested by the configure script.
Note that your Kubernetes cluster must be running on instances with the
`storage-rw` scope for this to work. With Container Engine, you can do this by
passing `--scopes storage-rw` to the `glcoud container clusters create` command.

For other platforms, you'll need to choose the `file` backup storage plugin,
and mount a read-write network volume into the `vttablet` and `vtctld` pods.
For example, you can mount any storage service accessible through NFS into a
Kubernetes volume. Then provide the mount path to the configure script here.

If you prefer to skip setting up a backup volume for the purpose of this example,
you can choose `file` mode and set the path to `/tmp`.

### Start Vitess

``` console
./vitess-up.sh
```

This will run through the steps to bring up Vitess. At the end, you should see
something like this:

``` console
****************************
* Complete!
* Use the following line to make an alias to kvtctl:
* alias kvtctl='$GOPATH/bin/vtctlclient -server 104.197.47.173:30001'
* See the vtctld UI at: http://104.197.47.173:30000
****************************
```

### Start the Guestbook app

``` console
./guestbook-up.sh
```

The guestbook service is configured with `type: LoadBalancer` to tell Kubernetes
to expose it on an external IP. It may take a minute to set up, but you should
soon see the external IP show up under the internal one like this:

``` console
$ kubectl get service guestbook
NAME        LABELS    SELECTOR         IP(S)             PORT(S)
guestbook   <none>    name=guestbook   10.67.253.173     80/TCP
                                       104.197.151.132
```

Visit the external IP in your browser to view the guestbook. Note that in this
modified guestbook, there are multiple pages to demonstrate range-based sharding
in Vitess. Each page number is assigned to one of the shards using a
[consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing) scheme.

### Tear down

``` console
./guestbook-down.sh
./vitess-down.sh
```

You may also want to remove any firewall rules you created.


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/vitess/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Cloud Native Deployment of Minio using Kubernetes

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Minio Standalone Server Deployment](#minio-standalone-server-deployment)
  - [Standalone Quickstart](#standalone-quickstart)
  - [Step 1: Create Persistent Volume Claim](#step-1-create-persistent-volume-claim)
  - [Step 2: Create Deployment](#step-2-create-minio-deployment)
  - [Step 3: Create LoadBalancer Service](#step-3-create-minio-service)
  - [Step 4: Resource cleanup](#step-4-resource-cleanup)
- [Minio Distributed Server Deployment](#minio-distributed-server-deployment)
  - [Distributed Quickstart](#distributed-quickstart)
  - [Step 1: Create Minio Headless Service](#step-1-create-minio-headless-service)
  - [Step 2: Create Minio Statefulset](#step-2-create-minio-statefulset)
  - [Step 3: Create LoadBalancer Service](#step-3-create-minio-service)
  - [Step 4: Resource cleanup](#step-4-resource-cleanup)

## Introduction
Minio is an AWS S3 compatible, object storage server built for cloud applications and devops. Minio is _cloud native_, meaning Minio understands that it is running within a cluster manager, and uses the cluster management infrastructure for allocation of compute and storage resources.

## Prerequisites

This example assumes that you have a Kubernetes version >=1.4 cluster installed and running, and that you have installed the [`kubectl`](https://kubernetes.io/docs/tasks/kubectl/install/) command line tool in your path. Please see the
[getting started guides](https://kubernetes.io/docs/getting-started-guides/) for installation instructions for your platform.

## Minio Standalone Server Deployment

The following section describes the process to deploy standalone [Minio](https://minio.io/) server on Kubernetes. The deployment uses the [official Minio Docker image](https://hub.docker.com/r/minio/minio/~/dockerfile/) from Docker Hub.

This section uses following core components of Kubernetes:

- [_Pods_](https://kubernetes.io/docs/user-guide/pods/)
- [_Services_](https://kubernetes.io/docs/user-guide/services/)
- [_Deployments_](https://kubernetes.io/docs/user-guide/deployments/)
- [_Persistent Volume Claims_](https://kubernetes.io/docs/user-guide/persistent-volumes/#persistentvolumeclaims)

### Standalone Quickstart

Run the below commands to get started quickly

```sh
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-standalone-pvc.yaml?raw=true
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-standalone-deployment.yaml?raw=true
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-standalone-service.yaml?raw=true
```

### Step 1: Create Persistent Volume Claim

Minio needs persistent storage to store objects. If there is no
persistent storage, the data stored in Minio instance will be stored in the container file system and will be wiped off as soon as the container restarts.

Create a persistent volume claim (PVC) to request storage for the Minio instance. Kubernetes looks out for PVs matching the PVC request in the cluster and binds it to the PVC automatically.

This is the PVC description.

```sh
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  # This name uniquely identifies the PVC. Will be used in deployment below.
  name: minio-pv-claim
  annotations:
    volume.alpha.kubernetes.io/storage-class: anything
  labels:
    app: minio-storage-claim
spec:
  # Read more about access modes here: http://kubernetes.io/docs/user-guide/persistent-volumes/#access-modes
  accessModes:
    - ReadWriteOnce
  resources:
    # This is the request for storage. Should be available in the cluster.
    requests:
      storage: 10Gi
```

Create the PersistentVolumeClaim

```sh
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-standalone-pvc.yaml?raw=true
persistentvolumeclaim "minio-pv-claim" created
```

### Step 2: Create Minio Deployment

A deployment encapsulates replica sets and pods — so, if a pod goes down, replication controller makes sure another pod comes up automatically. This way you won’t need to bother about pod failures and will have a stable Minio service available.

This is the deployment description.

```sh
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  # This name uniquely identifies the Deployment
  name: minio-deployment
spec:
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        # Label is used as selector in the service.
        app: minio
    spec:
      # Refer to the PVC created earlier
      volumes:
      - name: storage
        persistentVolumeClaim:
          # Name of the PVC created earlier
          claimName: minio-pv-claim
      containers:
      - name: minio
        # Pulls the default Minio image from Docker Hub
        image: minio/minio:latest
        args:
        - server
        - /storage
        env:
        # Minio access key and secret key
        - name: MINIO_ACCESS_KEY
          value: "minio"
        - name: MINIO_SECRET_KEY
          value: "minio123"
        ports:
        - containerPort: 9000
          hostPort: 9000
        # Mount the volume into the pod
        volumeMounts:
        - name: storage # must match the volume name, above
          mountPath: "/storage"
```

Create the Deployment

```sh
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-standalone-deployment.yaml?raw=true
deployment "minio-deployment" created
```

### Step 3: Create Minio Service

Now that you have a Minio deployment running, you may either want to access it internally (within the cluster) or expose it as a Service onto an external (outside of your cluster, maybe public internet) IP address, depending on your use case. You can achieve this using Services. There are 3 major service types — default type is ClusterIP, which exposes a service to connection from inside the cluster. NodePort and LoadBalancer are two types that expose services to external traffic.

In this example, we expose the Minio Deployment by creating a LoadBalancer service. This is the service description.

```sh
apiVersion: v1
kind: Service
metadata:
  name: minio-service
spec:
  type: LoadBalancer
  ports:
    - port: 9000
      targetPort: 9000
      protocol: TCP
  selector:
    app: minio
```
Create the Minio service

```sh
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-standalone-service.yaml?raw=true
service "minio-service" created
```

The `LoadBalancer` service takes couple of minutes to launch. To check if the service was created successfully, run the command

```sh
kubectl get svc minio-service
NAME            CLUSTER-IP     EXTERNAL-IP       PORT(S)          AGE
minio-service   10.55.248.23   104.199.249.165   9000:31852/TCP   1m
```

### Step 4: Resource cleanup

Once you are done, cleanup the cluster using
```sh
kubectl delete deployment minio-deployment \
&&  kubectl delete pvc minio-pv-claim \
&& kubectl delete svc minio-service
```

## Minio Distributed Server Deployment

The following document describes the process to deploy [distributed Minio](https://docs.minio.io/docs/distributed-minio-quickstart-guide) server on Kubernetes. This example uses the [official Minio Docker image](https://hub.docker.com/r/minio/minio/~/dockerfile/) from Docker Hub.

This example uses following core components of Kubernetes:

- [_Pods_](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
- [_Services_](https://kubernetes.io/docs/concepts/services-networking/service/)
- [_Statefulsets_](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)

### Distributed Quickstart

Run the below commands to get started quickly

```sh
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-distributed-headless-service.yaml?raw=true
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-distributed-statefulset.yaml?raw=true
kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-distributed-service.yaml?raw=true
```

### Step 1: Create Minio Headless Service

Headless Service controls the domain within which StatefulSets are created. The domain managed by this Service takes the form: `$(service name).$(namespace).svc.cluster.local` (where “cluster.local” is the cluster domain), and the pods in this domain take the form: `$(pod-name-{i}).$(service name).$(namespace).svc.cluster.local`. This is required to get a DNS resolvable URL for each of the pods created within the Statefulset.

This is the Headless service description.

```sh
apiVersion: v1
kind: Service
metadata:
  name: minio
  labels:
    app: minio
spec:
  clusterIP: None
  ports:
    - port: 9000
      name: minio
  selector:
    app: minio
```

Create the Headless Service

```sh
$ kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-distributed-headless-service.yaml?raw=true
service "minio" created
```

### Step 2: Create Minio Statefulset

A StatefulSet provides a deterministic name and a unique identity to each pod, making it easy to deploy stateful distributed applications. To launch distributed Minio you need to pass drive locations as parameters to the minio server command. Then, you’ll need to run the same command on all the participating pods. StatefulSets offer a perfect way to handle this requirement.

This is the Statefulset description.

```sh
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: minio
spec:
  serviceName: minio
  replicas: 4
  template:
    metadata:
      annotations:
        pod.alpha.kubernetes.io/initialized: "true"
      labels:
        app: minio
    spec:
      containers:
      - name: minio
        env:
        - name: MINIO_ACCESS_KEY
          value: "minio"
        - name: MINIO_SECRET_KEY
          value: "minio123"
        image: minio/minio:latest
        args:
        - server
        - http://minio-0.minio.default.svc.cluster.local/data
        - http://minio-1.minio.default.svc.cluster.local/data
        - http://minio-2.minio.default.svc.cluster.local/data
        - http://minio-3.minio.default.svc.cluster.local/data
        ports:
        - containerPort: 9000
          hostPort: 9000
        # These volume mounts are persistent. Each pod in the Statefulset
        # gets a volume mounted based on this field.
        volumeMounts:
        - name: data
          mountPath: /data
  # These are converted to volume claims by the controller
  # and mounted at the paths mentioned above.
  volumeClaimTemplates:
  - metadata:
      name: data
      annotations:
        volume.alpha.kubernetes.io/storage-class: anything
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
```

Create the Statefulset

```sh
$ kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-distributed-statefulset.yaml?raw=true
statefulset "minio" created
```

### Step 3: Create Minio Service

Now that you have a Minio statefulset running, you may either want to access it internally (within the cluster) or expose it as a Service onto an external (outside of your cluster, maybe public internet) IP address, depending on your use case. You can achieve this using Services. There are 3 major service types — default type is ClusterIP, which exposes a service to connection from inside the cluster. NodePort and LoadBalancer are two types that expose services to external traffic.

In this example, we expose the Minio Deployment by creating a LoadBalancer service. This is the service description.

```sh
apiVersion: v1
kind: Service
metadata:
  name: minio-service
spec:
  type: LoadBalancer
  ports:
    - port: 9000
      targetPort: 9000
      protocol: TCP
  selector:
    app: minio
```
Create the Minio service

```sh
$ kubectl create -f https://github.com/kubernetes/kubernetes/blob/master/examples/storage/minio/minio-distributed-service.yaml?raw=true
service "minio-service" created
```

The `LoadBalancer` service takes couple of minutes to launch. To check if the service was created successfully, run the command

```sh
$ kubectl get svc minio-service
NAME            CLUSTER-IP     EXTERNAL-IP       PORT(S)          AGE
minio-service   10.55.248.23   104.199.249.165   9000:31852/TCP   1m
```

### Step 4: Resource cleanup

You can cleanup the cluster using
```sh
kubectl delete statefulset minio \
&&  kubectl delete svc minio \
&& kubectl delete svc minio-service
```
## Reliable, Scalable Redis on Kubernetes

The following document describes the deployment of a reliable, multi-node Redis on Kubernetes.  It deploys a master with replicated slaves, as well as replicated redis sentinels which are use for health checking and failover.

### Prerequisites

This example assumes that you have a Kubernetes cluster installed and running, and that you have installed the ```kubectl``` command line tool somewhere in your path.  Please see the [getting started](https://kubernetes.io/docs/getting-started-guides/) for installation instructions for your platform.

### A note for the impatient

This is a somewhat long tutorial.  If you want to jump straight to the "do it now" commands, please see the [tl; dr](#tl-dr) at the end.

### Turning up an initial master/sentinel pod.

A [_Pod_](https://kubernetes.io/docs/user-guide/pods.md) is one or more containers that _must_ be scheduled onto the same host.  All containers in a pod share a network namespace, and may optionally share mounted volumes.

We will use the shared network namespace to bootstrap our Redis cluster.  In particular, the very first sentinel needs to know how to find the master (subsequent sentinels just ask the first sentinel).  Because all containers in a Pod share a network namespace, the sentinel can simply look at ```$(hostname -i):6379```.

Here is the config for the initial master and sentinel pod: [redis-master.yaml](redis-master.yaml)


Create this master as follows:

```sh
kubectl create -f examples/storage/redis/redis-master.yaml
```

### Turning up a sentinel service

In Kubernetes a [_Service_](https://kubernetes.io/docs/user-guide/services.md) describes a set of Pods that perform the same task.  For example, the set of nodes in a Cassandra cluster, or even the single node we created above.  An important use for a Service is to create a load balancer which distributes traffic across members of the set.  But a _Service_ can also be used as a standing query which makes a dynamically changing set of Pods (or the single Pod we've already created) available via the Kubernetes API.

In Redis, we will use a Kubernetes Service to provide a discoverable endpoints for the Redis sentinels in the cluster.  From the sentinels Redis clients can find the master, and then the slaves and other relevant info for the cluster.  This enables new members to join the cluster when failures occur.

Here is the definition of the sentinel service: [redis-sentinel-service.yaml](redis-sentinel-service.yaml)

Create this service:

```sh
kubectl create -f examples/storage/redis/redis-sentinel-service.yaml
```

### Turning up replicated redis servers

So far, what we have done is pretty manual, and not very fault-tolerant.  If the ```redis-master``` pod that we previously created is destroyed for some reason (e.g. a machine dying) our Redis service goes away with it.

In Kubernetes a [_Replication Controller_](https://kubernetes.io/docs/user-guide/replication-controller.md) is responsible for replicating sets of identical pods.  Like a _Service_ it has a selector query which identifies the members of it's set.  Unlike a _Service_ it also has a desired number of replicas, and it will create or delete _Pods_ to ensure that the number of _Pods_ matches up with it's desired state.

Replication Controllers will "adopt" existing pods that match their selector query, so let's create a Replication Controller with a single replica to adopt our existing Redis server. Here is the replication controller config: [redis-controller.yaml](redis-controller.yaml)

The bulk of this controller config is actually identical to the redis-master pod definition above.  It forms the template or "cookie cutter" that defines what it means to be a member of this set.

Create this controller:

```sh
kubectl create -f examples/storage/redis/redis-controller.yaml
```

We'll do the same thing for the sentinel.  Here is the controller config: [redis-sentinel-controller.yaml](redis-sentinel-controller.yaml)

We create it as follows:

```sh
kubectl create -f examples/storage/redis/redis-sentinel-controller.yaml
```

### Scale our replicated pods

Initially creating those pods didn't actually do anything, since we only asked for one sentinel and one redis server, and they already existed, nothing changed.  Now we will add more replicas:

```sh
kubectl scale rc redis --replicas=3
```

```sh
kubectl scale rc redis-sentinel --replicas=3
```

This will create two additional replicas of the redis server and two additional replicas of the redis sentinel.

Unlike our original redis-master pod, these pods exist independently, and they use the ```redis-sentinel-service``` that we defined above to discover and join the cluster.

### Delete our manual pod

The final step in the cluster turn up is to delete the original redis-master pod that we created manually.  While it was useful for bootstrapping discovery in the cluster, we really don't want the lifespan of our sentinel to be tied to the lifespan of one of our redis servers, and now that we have a successful, replicated redis sentinel service up and running, the binding is unnecessary.

Delete the master as follows:

```sh
kubectl delete pods redis-master
```

Now let's take a close look at what happens after this pod is deleted.  There are three things that happen:

  1. The redis replication controller notices that its desired state is 3 replicas, but there are currently only 2 replicas, and so it creates a new redis server to bring the replica count back up to 3
  2. The redis-sentinel replication controller likewise notices the missing sentinel, and also creates a new sentinel.
  3. The redis sentinels themselves, realize that the master has disappeared from the cluster, and begin the election procedure for selecting a new master.  They perform this election and selection, and chose one of the existing redis server replicas to be the new master.

### Conclusion

At this point we now have a reliable, scalable Redis installation.  By scaling the replication controller for redis servers, we can increase or decrease the number of read-slaves in our cluster.  Likewise, if failures occur, the redis-sentinels will perform master election and select a new master.

**NOTE:** since redis 3.2 some security measures (bind to 127.0.0.1 and `--protected-mode`) are enabled by default. Please read about this in http://antirez.com/news/96


### tl; dr

For those of you who are impatient, here is the summary of commands we ran in this tutorial:

```
# Create a bootstrap master
kubectl create -f examples/storage/redis/redis-master.yaml

# Create a service to track the sentinels
kubectl create -f examples/storage/redis/redis-sentinel-service.yaml

# Create a replication controller for redis servers
kubectl create -f examples/storage/redis/redis-controller.yaml

# Create a replication controller for redis sentinels
kubectl create -f examples/storage/redis/redis-sentinel-controller.yaml

# Scale both replication controllers
kubectl scale rc redis --replicas=3
kubectl scale rc redis-sentinel --replicas=3

# Delete the original master pod
kubectl delete pods redis-master
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/redis/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
RethinkDB Cluster on Kubernetes
==============================

Setting up a [rethinkdb](http://rethinkdb.com/) cluster on [kubernetes](http://kubernetes.io)

**Features**

 * Auto configuration cluster by querying info from k8s
 * Simple

Quick start
-----------

**Step 1**

Rethinkdb will discover its peer using endpoints provided by kubernetes service,
so first create a service so the following pod can query its endpoint

```sh
$kubectl create -f examples/storage/rethinkdb/driver-service.yaml
```

check out:

```sh
$kubectl get services
NAME              CLUSTER_IP       EXTERNAL_IP       PORT(S)       SELECTOR               AGE
rethinkdb-driver  10.0.27.114      <none>            28015/TCP     db=rethinkdb           10m
[...]
```

**Step 2**

start the first server in the cluster

```sh
$kubectl create -f examples/storage/rethinkdb/rc.yaml
```

Actually, you can start servers as many as you want at one time, just modify the `replicas` in `rc.ymal`

check out again:

```sh
$kubectl get pods
NAME                                                  READY     REASON    RESTARTS   AGE
[...]
rethinkdb-rc-r4tb0                                    1/1       Running   0          1m
```

**Done!**


---

Scale
-----

You can scale up your cluster using `kubectl scale`. The new pod will join to the existing cluster automatically, for example


```sh
$kubectl scale rc rethinkdb-rc --replicas=3
scaled

$kubectl get pods
NAME                                                  READY     REASON    RESTARTS   AGE
[...]
rethinkdb-rc-f32c5                                    1/1       Running   0          1m
rethinkdb-rc-m4d50                                    1/1       Running   0          1m
rethinkdb-rc-r4tb0                                    1/1       Running   0          3m
```

Admin
-----

You need a separate pod (labeled as role:admin) to access Web Admin UI

```sh
kubectl create -f examples/storage/rethinkdb/admin-pod.yaml
kubectl create -f examples/storage/rethinkdb/admin-service.yaml
```

find the service

```console
$kubectl get services
NAME              CLUSTER_IP       EXTERNAL_IP       PORT(S)       SELECTOR                  AGE
[...]
rethinkdb-admin   10.0.131.19      104.197.19.120    8080/TCP      db=rethinkdb,role=admin   10m
rethinkdb-driver  10.0.27.114      <none>            28015/TCP     db=rethinkdb              20m
```

We request an external load balancer in the [admin-service.yaml](admin-service.yaml) file:

```
type: LoadBalancer
```

The external load balancer allows us to access the service from outside the firewall via an external IP, 104.197.19.120 in this case.

Note that you may need to create a firewall rule to allow the traffic, assuming you are using Google Compute Engine:

```console
$ gcloud compute firewall-rules create rethinkdb --allow=tcp:8080
```

Now you can open a web browser and access to *http://104.197.19.120:8080* to manage your cluster.



**Why not just using pods in replicas?**

This is because kube-proxy will act as a load balancer and send your traffic to different server,
since the ui is not stateless when playing with Web Admin UI will cause `Connection not open on server` error.


- - -

**BTW**

  * `gen_pod.sh` is using to generate pod templates for my local cluster,
the generated pods which is using `nodeSelector` to force k8s to schedule containers to my designate nodes, for I need to access persistent data on my host dirs. Note that one needs to label the node before 'nodeSelector' can work, see this [tutorial](https://kubernetes.io/docs/user-guide/node-selection/)

  * see [antmanler/rethinkdb-k8s](https://github.com/antmanler/rethinkdb-k8s) for detail


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/rethinkdb/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Cloud Native Deployments of Hazelcast using Kubernetes

The following document describes the development of a _cloud native_ [Hazelcast](http://hazelcast.org/) deployment on Kubernetes.  When we say _cloud native_ we mean an application which understands that it is running within a cluster manager, and uses this cluster management infrastructure to help implement the application. In particular, in this instance, a custom Hazelcast ```bootstrapper``` is used to enable Hazelcast to dynamically discover Hazelcast nodes that have already joined the cluster.

Any topology changes are communicated and handled by Hazelcast nodes themselves.

This document also attempts to describe the core components of Kubernetes: _Pods_, _Services_, and _Deployments_.

### Prerequisites

This example assumes that you have a Kubernetes cluster installed and running, and that you have installed the `kubectl` command line tool somewhere in your path.  Please see the [getting started](https://kubernetes.io/docs/getting-started-guides/) for installation instructions for your platform.

### A note for the impatient

This is a somewhat long tutorial.  If you want to jump straight to the "do it now" commands, please see the [tl; dr](#tl-dr) at the end.

### Sources

Source is freely available at:
* Hazelcast Discovery - https://github.com/pires/hazelcast-kubernetes-bootstrapper
* Dockerfile - https://github.com/pires/hazelcast-kubernetes
* Docker Trusted Build - https://quay.io/repository/pires/hazelcast-kubernetes

### Simple Single Pod Hazelcast Node

In Kubernetes, the atomic unit of an application is a [_Pod_](https://kubernetes.io/docs/user-guide/pods.md).  A Pod is one or more containers that _must_ be scheduled onto the same host.  All containers in a pod share a network namespace, and may optionally share mounted volumes.

In this case, we shall not run a single Hazelcast pod, because the discovery mechanism now relies on a service definition.


### Adding a Hazelcast Service

In Kubernetes a _[Service](https://kubernetes.io/docs/user-guide/services.md)_ describes a set of Pods that perform the same task. For example, the set of nodes in a Hazelcast cluster. An important use for a Service is to create a load balancer which distributes traffic across members of the set.  But a _Service_ can also be used as a standing query which makes a dynamically changing set of Pods available via the Kubernetes API. This is actually how our discovery mechanism works, by relying on the service to discover other Hazelcast pods.

Here is the service description:

<!-- BEGIN MUNGE: EXAMPLE hazelcast-service.yaml -->

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    name: hazelcast
  name: hazelcast
spec: 
  ports:
    - port: 5701
  selector:
    name: hazelcast
```

[Download example](hazelcast-service.yaml?raw=true)
<!-- END MUNGE: EXAMPLE hazelcast-service.yaml -->

The important thing to note here is the `selector`. It is a query over labels, that identifies the set of _Pods_ contained by the _Service_.  In this case the selector is `name: hazelcast`.  If you look at the Replication Controller specification below, you'll see that the pod has the corresponding label, so it will be selected for membership in this Service.

Create this service as follows:

```sh
$ kubectl create -f examples/storage/hazelcast/hazelcast-service.yaml
```

### Adding replicated nodes

The real power of Kubernetes and Hazelcast lies in easily building a replicated, resizable Hazelcast cluster.

In Kubernetes a _[_Deployment_](https://kubernetes.io/docs/user-guide/deployments.md)_ is responsible for replicating sets of identical pods. Like a _Service_ it has a selector query which identifies the members of its set.  Unlike a _Service_ it also has a desired number of replicas, and it will create or delete _Pods_ to ensure that the number of _Pods_ matches up with its desired state.

Deployments will "adopt" existing pods that match their selector query, so let's create a Deployment with a single replica to adopt our existing Hazelcast Pod.

<!-- BEGIN MUNGE: EXAMPLE hazelcast-controller.yaml -->

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata: 
  name: hazelcast
  labels: 
    name: hazelcast
spec: 
  template: 
    metadata: 
      labels: 
        name: hazelcast
    spec: 
      containers: 
      - name: hazelcast
        image: quay.io/pires/hazelcast-kubernetes:0.8.0
        imagePullPolicy: Always
        env:
        - name: "DNS_DOMAIN"
          value: "cluster.local"
        ports: 
        - name: hazelcast
          containerPort: 5701
```

[Download example](hazelcast-deployment.yaml?raw=true)
<!-- END MUNGE: EXAMPLE hazelcast-controller.yaml -->

You may note that we tell Kubernetes that the container exposes the `hazelcast` port.

The bulk of the replication controller config is actually identical to the Hazelcast pod declaration above, it simply gives the controller a recipe to use when creating new pods.  The other parts are the `selector` which contains the controller's selector query, and the `replicas` parameter which specifies the desired number of replicas, in this case 1.

Last but not least, we set `DNS_DOMAIN` environment variable according to your Kubernetes clusters DNS configuration.

Create this controller:

```sh
$ kubectl create -f examples/storage/hazelcast/hazelcast-deployment.yaml
```

After the controller provisions successfully the pod, you can query the service endpoints:
```sh
$ kubectl get endpoints hazelcast -o yaml
apiVersion: v1
kind: Endpoints
metadata:
  creationTimestamp: 2017-03-15T09:40:11Z
  labels:
    name: hazelcast
  name: hazelcast
  namespace: default
  resourceVersion: "65060"
  selfLink: /api/v1/namespaces/default/endpoints/hazelcast
  uid: 62645b71-0963-11e7-b39c-080027985ce6
subsets:
- addresses:
  - ip: 172.17.0.2
    nodeName: minikube
    targetRef:
      kind: Pod
      name: hazelcast-4195412960-mgqtk
      namespace: default
      resourceVersion: "65058"
      uid: 7043708f-0963-11e7-b39c-080027985ce6
  ports:
  - port: 5701
    protocol: TCP

```

You can see that the _Service_ has found the pod created by the replication controller.

Now it gets even more interesting. Let's scale our cluster to 2 pods:
```sh
$ kubectl scale deployment hazelcast --replicas 2
```

Now if you list the pods in your cluster, you should see two hazelcast pods:

```sh
$ kubectl get deployment,pods
NAME               DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/hazelcast   2         2         2            2           2m

NAME                                           READY     STATUS    RESTARTS   AGE
po/hazelcast-4195412960-0tl3w                  1/1       Running   0          7s
po/hazelcast-4195412960-mgqtk                  1/1       Running   0          2m
```

To prove that this all works, you can use the `log` command to examine the logs of one pod, for example:

```sh
kubectl logs -f hazelcast-4195412960-0tl3w
2017-03-15 09:42:45.046  INFO 7 --- [           main] com.github.pires.hazelcast.Application   : Starting Application on hazelcast-4195412960-0tl3w with PID 7 (/bootstrapper.jar started by root in /)
2017-03-15 09:42:45.060  INFO 7 --- [           main] com.github.pires.hazelcast.Application   : No active profile set, falling back to default profiles: default
2017-03-15 09:42:45.128  INFO 7 --- [           main] s.c.a.AnnotationConfigApplicationContext : Refreshing org.springframework.context.annotation.AnnotationConfigApplicationContext@14514713: startup date [Wed Mar 15 09:42:45 GMT 2017]; root of context hierarchy
2017-03-15 09:42:45.989  INFO 7 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2017-03-15 09:42:46.001  INFO 7 --- [           main] c.g.p.h.HazelcastDiscoveryController     : Asking k8s registry at https://kubernetes.default.svc.cluster.local..
2017-03-15 09:42:46.376  INFO 7 --- [           main] c.g.p.h.HazelcastDiscoveryController     : Found 2 pods running Hazelcast.
2017-03-15 09:42:46.458  INFO 7 --- [           main] c.h.instance.DefaultAddressPicker        : [LOCAL] [someGroup] [3.8] Interfaces is disabled, trying to pick one address from TCP-IP config addresses: [172.17.0.6, 172.17.0.2]
2017-03-15 09:42:46.458  INFO 7 --- [           main] c.h.instance.DefaultAddressPicker        : [LOCAL] [someGroup] [3.8] Prefer IPv4 stack is true.
2017-03-15 09:42:46.464  INFO 7 --- [           main] c.h.instance.DefaultAddressPicker        : [LOCAL] [someGroup] [3.8] Picked [172.17.0.6]:5701, using socket ServerSocket[addr=/0:0:0:0:0:0:0:0,localport=5701], bind any local is true
2017-03-15 09:42:46.484  INFO 7 --- [           main] com.hazelcast.system                     : [172.17.0.6]:5701 [someGroup] [3.8] Hazelcast 3.8 (20170217 - d7998b4) starting at [172.17.0.6]:5701
2017-03-15 09:42:46.484  INFO 7 --- [           main] com.hazelcast.system                     : [172.17.0.6]:5701 [someGroup] [3.8] Copyright (c) 2008-2017, Hazelcast, Inc. All Rights Reserved.
2017-03-15 09:42:46.485  INFO 7 --- [           main] com.hazelcast.system                     : [172.17.0.6]:5701 [someGroup] [3.8] Configured Hazelcast Serialization version : 1
2017-03-15 09:42:46.679  INFO 7 --- [           main] c.h.s.i.o.impl.BackpressureRegulator     : [172.17.0.6]:5701 [someGroup] [3.8] Backpressure is disabled
2017-03-15 09:42:47.069  INFO 7 --- [           main] com.hazelcast.instance.Node              : [172.17.0.6]:5701 [someGroup] [3.8] Creating TcpIpJoiner
2017-03-15 09:42:47.182  INFO 7 --- [           main] c.h.s.i.o.impl.OperationExecutorImpl     : [172.17.0.6]:5701 [someGroup] [3.8] Starting 2 partition threads
2017-03-15 09:42:47.189  INFO 7 --- [           main] c.h.s.i.o.impl.OperationExecutorImpl     : [172.17.0.6]:5701 [someGroup] [3.8] Starting 3 generic threads (1 dedicated for priority tasks)
2017-03-15 09:42:47.197  INFO 7 --- [           main] com.hazelcast.core.LifecycleService      : [172.17.0.6]:5701 [someGroup] [3.8] [172.17.0.6]:5701 is STARTING
2017-03-15 09:42:47.253  INFO 7 --- [cached.thread-3] c.hazelcast.nio.tcp.InitConnectionTask   : [172.17.0.6]:5701 [someGroup] [3.8] Connecting to /172.17.0.2:5701, timeout: 0, bind-any: true
2017-03-15 09:42:47.262  INFO 7 --- [cached.thread-3] c.h.nio.tcp.TcpIpConnectionManager       : [172.17.0.6]:5701 [someGroup] [3.8] Established socket connection between /172.17.0.6:58073 and /172.17.0.2:5701
2017-03-15 09:42:54.260  INFO 7 --- [ration.thread-0] com.hazelcast.system                     : [172.17.0.6]:5701 [someGroup] [3.8] Cluster version set to 3.8
2017-03-15 09:42:54.262  INFO 7 --- [ration.thread-0] c.h.internal.cluster.ClusterService      : [172.17.0.6]:5701 [someGroup] [3.8] 

Members [2] {
	Member [172.17.0.2]:5701 - 170f6924-7888-442a-9875-ad4d25659a8a
	Member [172.17.0.6]:5701 - b1b82bfa-86c2-4931-af57-325c10c03b3b this
}

2017-03-15 09:42:56.285  INFO 7 --- [           main] com.hazelcast.core.LifecycleService      : [172.17.0.6]:5701 [someGroup] [3.8] [172.17.0.6]:5701 is STARTED
2017-03-15 09:42:56.287  INFO 7 --- [           main] com.github.pires.hazelcast.Application   : Started Application in 11.831 seconds (JVM running for 12.219)
```

Now let's scale our cluster to 4 nodes:
```sh
$ kubectl scale deployment hazelcast --replicas 4
```

Examine the status again by checking a node's logs and you should see the 4 members connected. Something like:
```
(...)

Members [4] {
	Member [172.17.0.2]:5701 - 170f6924-7888-442a-9875-ad4d25659a8a
	Member [172.17.0.6]:5701 - b1b82bfa-86c2-4931-af57-325c10c03b3b this
	Member [172.17.0.9]:5701 - 0c7530d3-1b5a-4f40-bd59-7187e43c1110
	Member [172.17.0.10]:5701 - ad5c3000-7fd0-4ce7-8194-e9b1c2ed6dda
}
```

### tl; dr;

For those of you who are impatient, here is the summary of the commands we ran in this tutorial.

```sh
kubectl create -f service.yaml
kubectl create -f deployment.yaml
kubectl scale deployment hazelcast --replicas 2
kubectl scale deployment hazelcast --replicas 4
```

### Hazelcast Discovery Source

See [here](https://github.com/pires/hazelcast-kubernetes-bootstrapper/blob/master/src/main/java/com/github/pires/hazelcast/HazelcastDiscoveryController.java)


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/hazelcast/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->

# Cloud Native Deployments of Cassandra using Kubernetes

## Table of Contents

  - [Prerequisites](#prerequisites)
  - [Cassandra Docker](#cassandra-docker)
  - [Quickstart](#quickstart)
  - [Step 1: Create a Cassandra Headless Service](#step-1-create-a-cassandra-headless-service)
  - [Step 2: Use a StatefulSet to create Cassandra Ring](#step-2-use-a-statefulset-to-create-cassandra-ring)
  - [Step 3: Validate and Modify The Cassandra StatefulSet](#step-3-validate-and-modify-the-cassandra-statefulset)
  - [Step 4: Delete Cassandra StatefulSet](#step-4-delete-cassandra-statefulset)
  - [Step 5: Use a Replication Controller to create Cassandra node pods](#step-5-use-a-replication-controller-to-create-cassandra-node-pods)
  - [Step 6: Scale up the Cassandra cluster](#step-6-scale-up-the-cassandra-cluster)
  - [Step 7: Delete the Replication Controller](#step-7-delete-the-replication-controller)
  - [Step 8: Use a DaemonSet instead of a Replication Controller](#step-8-use-a-daemonset-instead-of-a-replication-controller)
  - [Step 9: Resource Cleanup](#step-9-resource-cleanup)
  - [Seed Provider Source](#seed-provider-source)

The following document describes the development of a _cloud native_
[Cassandra](http://cassandra.apache.org/) deployment on Kubernetes.  When we say
_cloud native_, we mean an application which understands that it is running
within a cluster manager, and uses this cluster management infrastructure to
help implement the application.  In particular, in this instance, a custom
Cassandra `SeedProvider` is used to enable Cassandra to dynamically discover
new Cassandra nodes as they join the cluster.

This example also uses some of the core components of Kubernetes:

- [_Pods_](https://kubernetes.io/docs/user-guide/pods.md)
- [ _Services_](https://kubernetes.io/docs/user-guide/services.md)
- [_Replication Controllers_](https://kubernetes.io/docs/user-guide/replication-controller.md)
- [_Stateful Sets_](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [_Daemon Sets_](https://kubernetes.io/docs/admin/daemons.md)

## Prerequisites

This example assumes that you have a Kubernetes version >=1.2 cluster installed and running,
and that you have installed the [`kubectl`](https://kubernetes.io/docs/user-guide/kubectl/kubectl.md)
command line tool somewhere in your path.  Please see the
[getting started guides](https://kubernetes.io/docs/getting-started-guides/)
for installation instructions for your platform.

This example also has a few code and configuration files needed.  To avoid
typing these out, you can `git clone` the Kubernetes repository to your local
computer.

## Cassandra Docker

The pods use the [```gcr.io/google-samples/cassandra:v12```](image/Dockerfile)
image from Google's [container registry](https://cloud.google.com/container-registry/docs/).
The docker is based on `debian:jessie` and includes OpenJDK 8. This image
includes a standard Cassandra installation from the Apache Debian repo.  Through the use of environment variables you are able to change values that are inserted into the `cassandra.yaml`.

| ENV VAR       | DEFAULT VALUE  |
| ------------- |:-------------: |
| CASSANDRA_CLUSTER_NAME | 'Test Cluster'  |
| CASSANDRA_NUM_TOKENS  | 32               |
| CASSANDRA_RPC_ADDRESS | 0.0.0.0          |

## Quickstart

If you want to jump straight to the commands we will run,
here are the steps:

```sh
#
# StatefulSet
#

# create a service to track all cassandra statefulset nodes
kubectl create -f examples/storage/cassandra/cassandra-service.yaml

# create a statefulset
kubectl create -f examples/storage/cassandra/cassandra-statefulset.yaml

# validate the Cassandra cluster. Substitute the name of one of your pods.
kubectl exec -ti cassandra-0 -- nodetool status

# cleanup
grace=$(kubectl get po cassandra-0 --template '{{.spec.terminationGracePeriodSeconds}}') \
  && kubectl delete statefulset,po -l app=cassandra \
  && echo "Sleeping $grace" \
  && sleep $grace \
  && kubectl delete pvc -l app=cassandra

#
# Resource Controller Example
#

# create a replication controller to replicate cassandra nodes
kubectl create -f examples/storage/cassandra/cassandra-controller.yaml

# validate the Cassandra cluster. Substitute the name of one of your pods.
kubectl exec -ti cassandra-xxxxx -- nodetool status

# scale up the Cassandra cluster
kubectl scale rc cassandra --replicas=4

# delete the replication controller
kubectl delete rc cassandra

#
# Create a DaemonSet to place a cassandra node on each kubernetes node
#

kubectl create -f examples/storage/cassandra/cassandra-daemonset.yaml --validate=false

# resource cleanup
kubectl delete service -l app=cassandra
kubectl delete daemonset cassandra
```

## Step 1: Create a Cassandra Headless Service

A Kubernetes _[Service](https://kubernetes.io/docs/user-guide/services.md)_ describes a set of
[_Pods_](https://kubernetes.io/docs/user-guide/pods.md) that perform the same task. In
Kubernetes, the atomic unit of an application is a Pod: one or more containers
that _must_ be scheduled onto the same host.

The Service is used for DNS lookups between Cassandra Pods, and Cassandra clients
within the Kubernetes Cluster.

Here is the service description:

<!-- BEGIN MUNGE: EXAMPLE cassandra-service.yaml -->

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: cassandra
  name: cassandra
spec:
  clusterIP: None
  ports:
    - port: 9042
  selector:
    app: cassandra
```

[Download example](cassandra-service.yaml?raw=true)
<!-- END MUNGE: EXAMPLE cassandra-service.yaml -->

Create the service for the StatefulSet:


```console
$ kubectl create -f examples/storage/cassandra/cassandra-service.yaml
```

The following command shows if the service has been created.

```console
$ kubectl get svc cassandra
```

The response should be like:

```console
NAME        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
cassandra   None         <none>        9042/TCP   45s
```

If an error is returned the service create failed.

## Step 2: Use a StatefulSet to create Cassandra Ring

StatefulSets (previously PetSets) are a feature that was upgraded to a <i>Beta</i> component in
Kubernetes 1.5.  Deploying stateful distributed applications, like Cassandra, within a clustered
environment can be challenging.  We implemented StatefulSet to greatly simplify this
process.  Multiple StatefulSet features are used within this example, but is out of
scope of this documentation.  [Please refer to the Stateful Set documentation.](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

The StatefulSet manifest that is included below, creates a Cassandra ring that consists
of three pods.

This example includes using a GCE Storage Class, please update appropriately depending
on the cloud you are working with. 

<!-- BEGIN MUNGE: EXAMPLE cassandra-statefulset.yaml -->

```yaml
apiVersion: "apps/v1beta1"
kind: StatefulSet
metadata:
  name: cassandra
spec:
  serviceName: cassandra
  replicas: 3
  template:
    metadata:
      labels:
        app: cassandra
    spec:
      containers:
      - name: cassandra
        image: gcr.io/google-samples/cassandra:v12
        imagePullPolicy: Always
        ports:
        - containerPort: 7000
          name: intra-node
        - containerPort: 7001
          name: tls-intra-node
        - containerPort: 7199
          name: jmx
        - containerPort: 9042
          name: cql
        resources:
          limits:
            cpu: "500m"
            memory: 1Gi
          requests:
           cpu: "500m"
           memory: 1Gi
        securityContext:
          capabilities:
            add:
              - IPC_LOCK
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sh", "-c", "PID=$(pidof java) && kill $PID && while ps -p $PID > /dev/null; do sleep 1; done"]
        env:
          - name: MAX_HEAP_SIZE
            value: 512M
          - name: HEAP_NEWSIZE
            value: 100M
          - name: CASSANDRA_SEEDS
            value: "cassandra-0.cassandra.default.svc.cluster.local"
          - name: CASSANDRA_CLUSTER_NAME
            value: "K8Demo"
          - name: CASSANDRA_DC
            value: "DC1-K8Demo"
          - name: CASSANDRA_RACK
            value: "Rack1-K8Demo"
          - name: CASSANDRA_AUTO_BOOTSTRAP
            value: "false"
          - name: POD_IP
            valueFrom:
              fieldRef:
                fieldPath: status.podIP
        readinessProbe:
          exec:
            command:
            - /bin/bash
            - -c
            - /ready-probe.sh
          initialDelaySeconds: 15
          timeoutSeconds: 5
        # These volume mounts are persistent. They are like inline claims,
        # but not exactly because the names need to match exactly one of
        # the stateful pod volumes.
        volumeMounts:
        - name: cassandra-data
          mountPath: /cassandra_data
  # These are converted to volume claims by the controller
  # and mounted at the paths mentioned above.
  # do not use these in production until ssd GCEPersistentDisk or other ssd pd
  volumeClaimTemplates:
  - metadata:
      name: cassandra-data
      annotations:
        volume.beta.kubernetes.io/storage-class: fast
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
---
kind: StorageClass
apiVersion: storage.k8s.io/v1beta1
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
```

[Download example](cassandra-statefulset.yaml?raw=true)
<!-- END MUNGE: EXAMPLE cassandra-statefulset.yaml -->

Create the Cassandra StatefulSet as follows:

```console
$ kubectl create -f examples/storage/cassandra/cassandra-statefulset.yaml
```

## Step 3: Validate and Modify The Cassandra StatefulSet

Deploying this StatefulSet shows off two of the new features that StatefulSets provides.

1. The pod names are known
2. The pods deploy in incremental order

First validate that the StatefulSet has deployed, by running `kubectl` command below.

```console
$ kubectl get statefulset cassandra
```

The command should respond like:

```console
NAME        DESIRED   CURRENT   AGE
cassandra   3         3         13s
```

Next watch the Cassandra pods deploy, one after another.  The StatefulSet resource
deploys pods in a number fashion: 1, 2, 3, etc.  If you execute the following
command before the pods deploy you are able to see the ordered creation.

```console
$ kubectl get pods -l="app=cassandra"
NAME          READY     STATUS              RESTARTS   AGE
cassandra-0   1/1       Running             0          1m
cassandra-1   0/1       ContainerCreating   0          8s
```

The above example shows two of the three pods in the Cassandra StatefulSet deployed.
Once all of the pods are deployed the same command will respond with the full
StatefulSet.

```console
$ kubectl get pods -l="app=cassandra"
NAME          READY     STATUS    RESTARTS   AGE
cassandra-0   1/1       Running   0          10m
cassandra-1   1/1       Running   0          9m
cassandra-2   1/1       Running   0          8m
```

Running the Cassandra utility `nodetool` will display the status of the ring.

```console
$ kubectl exec cassandra-0 -- nodetool status
Datacenter: DC1-K8Demo
======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address   Load       Tokens       Owns (effective)  Host ID                               Rack
UN  10.4.2.4  65.26 KiB  32           63.7%             a9d27f81-6783-461d-8583-87de2589133e  Rack1-K8Demo
UN  10.4.0.4  102.04 KiB  32           66.7%             5559a58c-8b03-47ad-bc32-c621708dc2e4  Rack1-K8Demo
UN  10.4.1.4  83.06 KiB  32           69.6%             9dce943c-581d-4c0e-9543-f519969cc805  Rack1-K8Demo
```

You can also run `cqlsh` to describe the keyspaces in the cluster.

```console
$ kubectl exec cassandra-0 -- cqlsh -e 'desc keyspaces'

system_traces  system_schema  system_auth  system  system_distributed
```

In order to increase or decrease the size of the Cassandra StatefulSet, you must use
`kubectl edit`.  You can find more information about the edit command in the [documentation](https://kubernetes.io/docs/user-guide/kubectl/kubectl_edit.md).

Use the following command to edit the StatefulSet.

```console
$ kubectl edit statefulset cassandra
```

This will create an editor in your terminal.  The line you are looking to change is
`replicas`. The example does on contain the entire contents of the terminal window, and
the last line of the example below is the replicas line that you want to change.

```console
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  creationTimestamp: 2016-08-13T18:40:58Z
  generation: 1
  labels:
    app: cassandra
  name: cassandra
  namespace: default
  resourceVersion: "323"
  selfLink: /apis/apps/v1beta1/namespaces/default/statefulsets/cassandra
  uid: 7a219483-6185-11e6-a910-42010a8a0fc0
spec:
  replicas: 3
```

Modify the manifest to the following, and save the manifest.

```console
spec:
  replicas: 4
```

The StatefulSet will now contain four pods.

```console
$ kubectl get statefulset cassandra
```

The command should respond like:

```console
NAME        DESIRED   CURRENT   AGE
cassandra   4         4         36m
```

For the Kubernetes 1.5 release, the beta StatefulSet resource does not have `kubectl scale`
functionality, like a Deployment, ReplicaSet, Replication Controller, or Job.

## Step 4: Delete Cassandra StatefulSet

Deleting and/or scaling a StatefulSet down will not delete the volumes associated with the StatefulSet. This is done to ensure safety first, your data is more valuable than an auto purge of all related StatefulSet resources. Deleting the Persistent Volume Claims may result in a deletion of the associated volumes, depending on the storage class and reclaim policy. You should never assume ability to access a volume after claim deletion.

Use the following commands to delete the StatefulSet.

```console
$ grace=$(kubectl get po cassandra-0 --template '{{.spec.terminationGracePeriodSeconds}}') \
  && kubectl delete statefulset -l app=cassandra \
  && echo "Sleeping $grace" \
  && sleep $grace \
  && kubectl delete pvc -l app=cassandra
```

## Step 5: Use a Replication Controller to create Cassandra node pods

A Kubernetes
_[Replication Controller](https://kubernetes.io/docs/user-guide/replication-controller.md)_
is responsible for replicating sets of identical pods.  Like a
Service, it has a selector query which identifies the members of its set.
Unlike a Service, it also has a desired number of replicas, and it will create
or delete Pods to ensure that the number of Pods matches up with its
desired state.

The Replication Controller, in conjunction with the Service we just defined,
will let us easily build a replicated, scalable Cassandra cluster.

Let's create a replication controller with two initial replicas.

<!-- BEGIN MUNGE: EXAMPLE cassandra-controller.yaml -->

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: cassandra
  # The labels will be applied automatically
  # from the labels in the pod template, if not set
  # labels:
    # app: cassandra
spec:
  replicas: 2
  # The selector will be applied automatically
  # from the labels in the pod template, if not set.
  # selector:
      # app: cassandra
  template:
    metadata:
      labels:
        app: cassandra
    spec:
      containers:
        - command:
            - /run.sh
          resources:
            limits:
              cpu: 0.5
          env:
            - name: MAX_HEAP_SIZE
              value: 512M
            - name: HEAP_NEWSIZE
              value: 100M
            - name: CASSANDRA_SEED_PROVIDER
              value: "io.k8s.cassandra.KubernetesSeedProvider"
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
          image: gcr.io/google-samples/cassandra:v12
          name: cassandra
          ports:
            - containerPort: 7000
              name: intra-node
            - containerPort: 7001
              name: tls-intra-node
            - containerPort: 7199
              name: jmx
            - containerPort: 9042
              name: cql
          volumeMounts:
            - mountPath: /cassandra_data
              name: data
      volumes:
        - name: data
          emptyDir: {}
```

[Download example](cassandra-controller.yaml?raw=true)
<!-- END MUNGE: EXAMPLE cassandra-controller.yaml -->

There are a few things to note in this description.

The `selector` attribute contains the controller's selector query. It can be
explicitly specified, or applied automatically from the labels in the pod
template if not set, as is done here.

The pod template's label, `app:cassandra`, matches the Service selector
from Step 1. This is how pods created by this replication controller are picked up
by the Service."

The `replicas` attribute specifies the desired number of replicas, in this
case 2 initially.  We'll scale up to more shortly.

Create the Replication Controller:

```console

$ kubectl create -f examples/storage/cassandra/cassandra-controller.yaml

```

You can list the new controller:

```console

$ kubectl get rc -o wide
NAME        DESIRED   CURRENT   AGE       CONTAINER(S)   IMAGE(S)                             SELECTOR
cassandra   2         2         11s       cassandra      gcr.io/google-samples/cassandra:v12   app=cassandra

```

Now if you list the pods in your cluster, and filter to the label
`app=cassandra`, you should see two Cassandra pods. (The `wide` argument lets
you see which Kubernetes nodes the pods were scheduled onto.)

```console

$ kubectl get pods -l="app=cassandra" -o wide
NAME              READY     STATUS    RESTARTS   AGE       NODE
cassandra-21qyy   1/1       Running   0          1m        kubernetes-minion-b286
cassandra-q6sz7   1/1       Running   0          1m        kubernetes-minion-9ye5

```

Because these pods have the label `app=cassandra`, they map to the service we
defined in Step 1.

You can check that the Pods are visible to the Service using the following service endpoints query:

```console

$ kubectl get endpoints cassandra -o yaml
apiVersion: v1
kind: Endpoints
metadata:
  creationTimestamp: 2015-06-21T22:34:12Z
  labels:
    app: cassandra
  name: cassandra
  namespace: default
  resourceVersion: "944373"
  selfLink: /api/v1/namespaces/default/endpoints/cassandra
  uid: a3d6c25f-1865-11e5-a34e-42010af01bcc
subsets:
- addresses:
  - ip: 10.244.3.15
    targetRef:
      kind: Pod
      name: cassandra
      namespace: default
      resourceVersion: "944372"
      uid: 9ef9895d-1865-11e5-a34e-42010af01bcc
  ports:
  - port: 9042
    protocol: TCP

```

To show that the `SeedProvider` logic is working as intended, you can use the
`nodetool` command to examine the status of the Cassandra cluster.  To do this,
use the `kubectl exec` command, which lets you run `nodetool` in one of your
Cassandra pods.  Again, substitute `cassandra-xxxxx` with the actual name of one
of your pods.

```console

$ kubectl exec -ti cassandra-xxxxx -- nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load       Tokens  Owns (effective)  Host ID                               Rack
UN  10.244.0.5  74.09 KB   256     100.0%            86feda0f-f070-4a5b-bda1-2eeb0ad08b77  rack1
UN  10.244.3.3  51.28 KB   256     100.0%            dafe3154-1d67-42e1-ac1d-78e7e80dce2b  rack1

```

## Step 6: Scale up the Cassandra cluster

Now let's scale our Cassandra cluster to 4 pods.  We do this by telling the
Replication Controller that we now want 4 replicas.

```sh

$ kubectl scale rc cassandra --replicas=4

```

You can see the new pods listed:

```console

$ kubectl get pods -l="app=cassandra" -o wide
NAME              READY     STATUS    RESTARTS   AGE       NODE
cassandra-21qyy   1/1       Running   0          6m        kubernetes-minion-b286
cassandra-81m2l   1/1       Running   0          47s       kubernetes-minion-b286
cassandra-8qoyp   1/1       Running   0          47s       kubernetes-minion-9ye5
cassandra-q6sz7   1/1       Running   0          6m        kubernetes-minion-9ye5

```

In a few moments, you can examine the Cassandra cluster status again, and see
that the new pods have been detected by the custom `SeedProvider`:

```console

$ kubectl exec -ti cassandra-xxxxx -- nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load       Tokens  Owns (effective)  Host ID                               Rack
UN  10.244.0.6  51.67 KB   256     48.9%             d07b23a5-56a1-4b0b-952d-68ab95869163  rack1
UN  10.244.1.5  84.71 KB   256     50.7%             e060df1f-faa2-470c-923d-ca049b0f3f38  rack1
UN  10.244.1.6  84.71 KB   256     47.0%             83ca1580-4f3c-4ec5-9b38-75036b7a297f  rack1
UN  10.244.0.5  68.2 KB    256     53.4%             72ca27e2-c72c-402a-9313-1e4b61c2f839  rack1

```

## Step 7: Delete the Replication Controller

Before you start Step 5, __delete the replication controller__ you created above:

```sh

$ kubectl delete rc cassandra

```

## Step 8: Use a DaemonSet instead of a Replication Controller

In Kubernetes, a [_Daemon Set_](https://kubernetes.io/docs/admin/daemons.md) can distribute pods
onto Kubernetes nodes, one-to-one.  Like a _ReplicationController_, it has a
selector query which identifies the members of its set.  Unlike a
_ReplicationController_, it has a node selector to limit which nodes are
scheduled with the templated pods, and replicates not based on a set target
number of pods, but rather assigns a single pod to each targeted node.

An example use case: when deploying to the cloud, the expectation is that
instances are ephemeral and might die at any time. Cassandra is built to
replicate data across the cluster to facilitate data redundancy, so that in the
case that an instance dies, the data stored on the instance does not, and the
cluster can react by re-replicating the data to other running nodes.

`DaemonSet` is designed to place a single pod on each node in the Kubernetes
cluster.  That will give us data redundancy. Let's create a
DaemonSet to start our storage cluster:

<!-- BEGIN MUNGE: EXAMPLE cassandra-daemonset.yaml -->

```yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  labels:
    name: cassandra
  name: cassandra
spec:
  template:
    metadata:
      labels:
        app: cassandra
    spec:
      # Filter to specific nodes:
      # nodeSelector:
      #  app: cassandra
      containers:
        - command:
            - /run.sh
          env:
            - name: MAX_HEAP_SIZE
              value: 512M
            - name: HEAP_NEWSIZE
              value: 100M
            - name: CASSANDRA_SEED_PROVIDER
              value: "io.k8s.cassandra.KubernetesSeedProvider"
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
          image: gcr.io/google-samples/cassandra:v12
          name: cassandra
          ports:
            - containerPort: 7000
              name: intra-node
            - containerPort: 7001
              name: tls-intra-node
            - containerPort: 7199
              name: jmx
            - containerPort: 9042
              name: cql
              # If you need it it is going away in C* 4.0
              #- containerPort: 9160
              #  name: thrift
          resources:
            requests:
              cpu: 0.5
          volumeMounts:
            - mountPath: /cassandra_data
              name: data
      volumes:
        - name: data
          emptyDir: {}
```

[Download example](cassandra-daemonset.yaml?raw=true)
<!-- END MUNGE: EXAMPLE cassandra-daemonset.yaml -->

Most of this DaemonSet definition is identical to the ReplicationController
definition above; it simply gives the daemon set a recipe to use when it creates
new Cassandra pods, and targets all Cassandra nodes in the cluster.

Differentiating aspects are the `nodeSelector` attribute, which allows the
DaemonSet to target a specific subset of nodes (you can label nodes just like
other resources), and the lack of a `replicas` attribute due to the 1-to-1 node-
pod relationship.

Create this DaemonSet:

```console

$ kubectl create -f examples/storage/cassandra/cassandra-daemonset.yaml

```

You may need to disable config file validation, like so:

```console

$ kubectl create -f examples/storage/cassandra/cassandra-daemonset.yaml --validate=false

```

You can see the DaemonSet running:

```console

$ kubectl get daemonset
NAME        DESIRED   CURRENT   NODE-SELECTOR
cassandra   3         3         <none>

```

Now, if you list the pods in your cluster, and filter to the label
`app=cassandra`, you should see one (and only one) new cassandra pod for each
node in your network.

```console

$ kubectl get pods -l="app=cassandra" -o wide
NAME              READY     STATUS    RESTARTS   AGE       NODE
cassandra-ico4r   1/1       Running   0          4s        kubernetes-minion-rpo1
cassandra-kitfh   1/1       Running   0          1s        kubernetes-minion-9ye5
cassandra-tzw89   1/1       Running   0          2s        kubernetes-minion-b286

```

To prove that this all worked as intended, you can again use the `nodetool`
command to examine the status of the cluster.  To do this, use the `kubectl
exec` command to run `nodetool` in one of your newly-launched cassandra pods.

```console

$ kubectl exec -ti cassandra-xxxxx -- nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load       Tokens  Owns (effective)  Host ID                               Rack
UN  10.244.0.5  74.09 KB   256     100.0%            86feda0f-f070-4a5b-bda1-2eeb0ad08b77  rack1
UN  10.244.4.2  32.45 KB   256     100.0%            0b1be71a-6ffb-4895-ac3e-b9791299c141  rack1
UN  10.244.3.3  51.28 KB   256     100.0%            dafe3154-1d67-42e1-ac1d-78e7e80dce2b  rack1

```

**Note**: This example had you delete the cassandra Replication Controller before
you created the DaemonSet.  This is because – to keep this example simple – the
RC and the DaemonSet are using the same `app=cassandra` label (so that their pods map to the
service we created, and so that the SeedProvider can identify them).

If we didn't delete the RC first, the two resources would conflict with
respect to how many pods they wanted to have running. If we wanted, we could support running
both together by using additional labels and selectors.

## Step 9: Resource Cleanup

When you are ready to take down your resources, do the following:

```console

$ kubectl delete service -l app=cassandra
$ kubectl delete daemonset cassandra

```

### Custom Seed Provider

A custom [`SeedProvider`](https://svn.apache.org/repos/asf/cassandra/trunk/src/java/org/apache/cassandra/locator/SeedProvider.java)
is included for running Cassandra on top of Kubernetes.  Only when you deploy Cassandra
via a replication control or a daemonset, you will need to use the custom seed provider.
In Cassandra, a `SeedProvider` bootstraps the gossip protocol that Cassandra uses to find other
Cassandra nodes. Seed addresses are hosts deemed as contact points. Cassandra
instances use the seed list to find each other and learn the topology of the
ring. The [`KubernetesSeedProvider`](java/src/main/java/io/k8s/cassandra/KubernetesSeedProvider.java)
discovers Cassandra seeds IP addresses via the Kubernetes API, those Cassandra
instances are defined within the Cassandra Service.

Refer to the custom seed provider [README](java/README.md) for further
`KubernetesSeedProvider` configurations. For this example you should not need
to customize the Seed Provider configurations.

See the [image](image/) directory of this example for specifics on
how the container docker image was built and what it contains.

You may also note that we are setting some Cassandra parameters (`MAX_HEAP_SIZE`
and `HEAP_NEWSIZE`), and adding information about the
[namespace](https://kubernetes.io/docs/user-guide/namespaces.md).
We also tell Kubernetes that the container exposes
both the `CQL` and `Thrift` API ports.  Finally, we tell the cluster
manager that we need 0.1 cpu (0.1 core).


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/cassandra/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Cassandra on Kubernetes Custom Seed Provider: releases.k8s.io/HEAD

Within any deployment of Cassandra a Seed Provider is used to for node discovery and communication.  When a Cassandra node first starts it must discover which nodes, or seeds, for the information about the Cassandra nodes in the ring / rack / datacenter.

This Java project provides a custom Seed Provider which communicates with the Kubernetes API to discover the required information.  This provider is bundled with the Docker provided in this example.

# Configuring the Seed Provider

The following environment variables may be used to override the default configurations:

| ENV VAR       | DEFAULT VALUE  | NOTES |
| ------------- |:-------------: |:-------------:|
| KUBERNETES_PORT_443_TCP_ADDR   | kubernetes.default.svc.cluster.local  | The hostname of the API server   |
| KUBERNETES_PORT_443_TCP_PORT   | 443                                   | API port number                  |
| CASSANDRA_SERVICE              | cassandra                             | Default service name for lookup  |
| POD_NAMESPACE                  | default                               | Default pod service namespace    |
| K8S_ACCOUNT_TOKEN 		 | /var/run/secrets/kubernetes.io/serviceaccount/token | Default path to service token |

# Using


If no endpoints are discovered from the API the seeds configured in the cassandra.yaml file are used.

# Provider limitations

This Cassandra Provider implements `SeedProvider`. and utilizes `SimpleSnitch`.  This limits a Cassandra Ring to a single Cassandra Datacenter and ignores Rack setup.  Datastax provides more documentation on the use of [_SNITCHES_](https://docs.datastax.com/en/cassandra/3.x/cassandra/architecture/archSnitchesAbout.html).  Further development is planned to
expand this capability.

This in affect makes every node a seed provider, which is not a recommended best practice.  This increases maintenance and reduces gossip performance.


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storage/cassandra/java/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Kubernetes DNS example

This is a toy example demonstrating how to use kubernetes DNS.

### Step Zero: Prerequisites

This example assumes that you have forked the repository and [turned up a Kubernetes cluster](https://kubernetes.io/docs/getting-started-guides/). Make sure DNS is enabled in your setup, see [DNS doc](https://github.com/kubernetes/dns).

```sh
$ cd kubernetes
$ hack/dev-build-and-up.sh
```

### Step One: Create two namespaces

We'll see how cluster DNS works across multiple [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), first we need to create two namespaces:

```sh
$ kubectl create -f examples/cluster-dns/namespace-dev.yaml
$ kubectl create -f examples/cluster-dns/namespace-prod.yaml
```

Now list all namespaces:

```sh
$ kubectl get namespaces
NAME          LABELS             STATUS
default       <none>             Active
development   name=development   Active
production    name=production    Active
```

For kubectl client to work with each namespace, we define two contexts:

```sh
$ kubectl config set-context dev --namespace=development --cluster=${CLUSTER_NAME} --user=${USER_NAME}
$ kubectl config set-context prod --namespace=production --cluster=${CLUSTER_NAME} --user=${USER_NAME}
```

You can view your cluster name and user name in kubernetes config at ~/.kube/config.

### Step Two: Create backend replication controller in each namespace

Use the file [`examples/cluster-dns/dns-backend-rc.yaml`](dns-backend-rc.yaml) to create a backend server [replication controller](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/) in each namespace.

```sh
$ kubectl config use-context dev
$ kubectl create -f examples/cluster-dns/dns-backend-rc.yaml
```

Once that's up you can list the pod in the cluster:

```sh
$ kubectl get rc
CONTROLLER    CONTAINER(S)   IMAGE(S)              SELECTOR           REPLICAS
dns-backend   dns-backend    ddysher/dns-backend   name=dns-backend   1
```

Now repeat the above commands to create a replication controller in prod namespace:

```sh
$ kubectl config use-context prod
$ kubectl create -f examples/cluster-dns/dns-backend-rc.yaml
$ kubectl get rc
CONTROLLER    CONTAINER(S)   IMAGE(S)              SELECTOR           REPLICAS
dns-backend   dns-backend    ddysher/dns-backend   name=dns-backend   1
```

### Step Three: Create backend service

Use the file [`examples/cluster-dns/dns-backend-service.yaml`](dns-backend-service.yaml) to create
a [service](https://kubernetes.io/docs/concepts/services-networking/service/) for the backend server.

```sh
$ kubectl config use-context dev
$ kubectl create -f examples/cluster-dns/dns-backend-service.yaml
```

Once that's up you can list the service in the cluster:

```sh
$ kubectl get service dns-backend
NAME         CLUSTER_IP       EXTERNAL_IP       PORT(S)                SELECTOR          AGE
dns-backend  10.0.2.3         <none>            8000/TCP               name=dns-backend  1d
```

Again, repeat the same process for prod namespace:

```sh
$ kubectl config use-context prod
$ kubectl create -f examples/cluster-dns/dns-backend-service.yaml
$ kubectl get service dns-backend
NAME         CLUSTER_IP       EXTERNAL_IP       PORT(S)                SELECTOR          AGE
dns-backend  10.0.2.4         <none>            8000/TCP               name=dns-backend  1d
```

### Step Four: Create client pod in one namespace

Use the file [`examples/cluster-dns/dns-frontend-pod.yaml`](dns-frontend-pod.yaml) to create a client [pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) in dev namespace. The client pod will make a connection to backend and exit. Specifically, it tries to connect to address `http://dns-backend.development.cluster.local:8000`.

```sh
$ kubectl config use-context dev
$ kubectl create -f examples/cluster-dns/dns-frontend-pod.yaml
```

Once that's up you can list the pod in the cluster:

```sh
$ kubectl get pods dns-frontend
NAME           READY     STATUS       RESTARTS   AGE
dns-frontend   0/1       ExitCode:0   0          1m
```

Wait until the pod succeeds, then we can see the output from the client pod:

```sh
$ kubectl logs dns-frontend
2015-05-07T20:13:54.147664936Z 10.0.236.129
2015-05-07T20:13:54.147721290Z Send request to: http://dns-backend.development.cluster.local:8000
2015-05-07T20:13:54.147733438Z <Response [200]>
2015-05-07T20:13:54.147738295Z Hello World!
```

Please refer to the [source code](images/frontend/client.py) about the log. First line prints out the ip address associated with the service in dev namespace; remaining lines print out our request and server response.

If we switch to prod namespace with the same pod config, we'll see the same result, i.e. dns will resolve across namespace.

```sh
$ kubectl config use-context prod
$ kubectl create -f examples/cluster-dns/dns-frontend-pod.yaml
$ kubectl logs dns-frontend
2015-05-07T20:13:54.147664936Z 10.0.236.129
2015-05-07T20:13:54.147721290Z Send request to: http://dns-backend.development.cluster.local:8000
2015-05-07T20:13:54.147733438Z <Response [200]>
2015-05-07T20:13:54.147738295Z Hello World!
```


#### Note about default namespace

If you prefer not using namespace, then all your services can be addressed using `default` namespace, e.g. `http://dns-backend.default.svc.cluster.local:8000`, or shorthand version `http://dns-backend:8000`


### tl; dr;

For those of you who are impatient, here is the summary of the commands we ran in this tutorial. Remember to set first `$CLUSTER_NAME` and `$USER_NAME` to the values found in `~/.kube/config`.

```sh
# create dev and prod namespaces
kubectl create -f examples/cluster-dns/namespace-dev.yaml
kubectl create -f examples/cluster-dns/namespace-prod.yaml

# create two contexts
kubectl config set-context dev --namespace=development --cluster=${CLUSTER_NAME} --user=${USER_NAME}
kubectl config set-context prod --namespace=production --cluster=${CLUSTER_NAME} --user=${USER_NAME}

# create two backend replication controllers
kubectl config use-context dev
kubectl create -f examples/cluster-dns/dns-backend-rc.yaml
kubectl config use-context prod
kubectl create -f examples/cluster-dns/dns-backend-rc.yaml

# create backend services
kubectl config use-context dev
kubectl create -f examples/cluster-dns/dns-backend-service.yaml
kubectl config use-context prod
kubectl create -f examples/cluster-dns/dns-backend-service.yaml

# create a pod in each namespace and get its output
kubectl config use-context dev
kubectl create -f examples/cluster-dns/dns-frontend-pod.yaml
kubectl logs dns-frontend

kubectl config use-context prod
kubectl create -f examples/cluster-dns/dns-frontend-pod.yaml
kubectl logs dns-frontend
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/cluster-dns/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Node.js and MongoDB on Kubernetes

The following document describes the deployment of a basic Node.js and MongoDB web stack on Kubernetes.  Currently this example does not use replica sets for MongoDB.

For more a in-depth explanation of this example, please [read this post.](https://medium.com/google-cloud-platform-developer-advocates/running-a-mean-stack-on-google-cloud-platform-with-kubernetes-149ca81c2b5d)

### Prerequisites

This example assumes that you have a basic understanding of Kubernetes conecepts (Pods, Services, Replication Controllers), a Kubernetes cluster up and running, and that you have installed the ```kubectl``` command line tool somewhere in your path.  Please see the [getting started](https://kubernetes.io/docs/getting-started-guides/) for installation instructions for your platform.

Note: This example was tested on [Google Container Engine](https://cloud.google.com/container-engine/docs/). Some optional commands require the [Google Cloud SDK](https://cloud.google.com/sdk/).

### Creating the MongoDB Service

The first thing to do is create the MongoDB Service.  This service is used by the other Pods in the cluster to find and connect to the MongoDB instance.

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    name: mongo
  name: mongo
spec:
  ports:
    - port: 27017
      targetPort: 27017
  selector:
    name: mongo
```

[Download file](mongo-service.yaml)

This service looks for all pods with the "mongo" tag, and creates a Service on port 27017 that targets port 27017 on the MongoDB pods. Port 27017 is the standard MongoDB port.

To start the service, run:

```sh
kubectl create -f examples/nodesjs-mongodb/mongo-service.yaml
```

### Creating the MongoDB Controller

Next, create the MongoDB instance that runs the Database.  Databases also need persistent storage, which will be different for each platform.

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  labels:
    name: mongo
  name: mongo-controller
spec:
  replicas: 1
  template:
    metadata:
      labels:
        name: mongo
    spec:
      containers:
      - image: mongo
        name: mongo
        ports:
        - name: mongo
          containerPort: 27017
          hostPort: 27017
        volumeMounts:
            - name: mongo-persistent-storage
              mountPath: /data/db
      volumes:
        - name: mongo-persistent-storage
          gcePersistentDisk:
            pdName: mongo-disk
            fsType: ext4
```

[Download file](mongo-controller.yaml)

Looking at this file from the bottom up:

First, it creates a volume called "mongo-persistent-storage."

In the above example, it is using a "gcePersistentDisk" to back the storage. This is only applicable if you are running your Kubernetes cluster in Google Cloud Platform.

If you don't already have a [Google Persistent Disk](https://cloud.google.com/compute/docs/disks) created in the same zone as your cluster, create a new disk in the same Google Compute Engine / Container Engine zone as your cluster with this command:

```sh
gcloud compute disks create --size=200GB --zone=$ZONE mongo-disk
```

If you are using AWS, replace the "volumes" section with this (untested):

```yaml
      volumes:
        - name: mongo-persistent-storage
          awsElasticBlockStore:
            volumeID: aws://{region}/{volume ID}
            fsType: ext4
```

If you don't have a EBS volume in the same region as your cluster, create a new EBS volume in the same region with this command (untested):

```sh
ec2-create-volume --size 200 --region $REGION --availability-zone $ZONE
```

This command will return a volume ID to use.

For other storage options (iSCSI, NFS, OpenStack), please follow the documentation.

Now that the volume is created and usable by Kubernetes, the next step is to create the Pod.

Looking at the container section: It uses the official MongoDB container, names itself "mongo", opens up port 27017, and mounts the disk to "/data/db" (where the mongo container expects the data to be).

Now looking at the rest of the file, it is creating a Replication Controller with one replica, called mongo-controller. It is important to use a Replication Controller and not just a Pod, as a Replication Controller will restart the instance in case it crashes.

Create this controller with this command:

```sh
kubectl create -f examples/nodesjs-mongodb/mongo-controller.yaml
```

At this point, MongoDB is up and running.

Note: There is no password protection or auth running on the database by default. Please keep this in mind!

### Creating the Node.js Service

The next step is to create the Node.js service. This service is what will be the endpoint for the web site, and will load balance requests to the Node.js instances.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
  labels:
    name: web
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 3000
      protocol: TCP
  selector:
    name: web
```

[Download file](web-service.yaml)

This service is called "web," and it uses a [LoadBalancer](https://kubernetes.io/docs/user-guide/services.md#type-loadbalancer) to distribute traffic on port 80 to port 3000 running on Pods with the "web" tag. Port 80 is the standard HTTP port, and port 3000 is the standard Node.js port.

On Google Container Engine, a [network load balancer](https://cloud.google.com/compute/docs/load-balancing/network/) and [firewall rule](https://cloud.google.com/compute/docs/networking#addingafirewall) to allow traffic are automatically created.

To start the service, run:

```sh
kubectl create -f examples/nodesjs-mongodb/web-service.yaml
```

If you are running on a platform that does not support LoadBalancer (i.e Bare Metal), you need to use a [NodePort](https://kubernetes.io/docs/user-guide/services.md#type-nodeport) with your own load balancer.

You may also need to open appropriate Firewall ports to allow traffic.

### Creating the Node.js Controller

The final step is deploying the Node.js container that will run the application code. This container can easily by replaced by any other web serving frontend, such as Rails, LAMP, Java, Go, etc.

The most important thing to keep in mind is how to access the MongoDB service.

If you were running MongoDB and Node.js on the same server, you would access MongoDB like so:

```javascript
MongoClient.connect('mongodb://localhost:27017/database-name', function(err, db) { console.log(db); });
```

With this Kubernetes setup, that line of code would become:

```javascript
MongoClient.connect('mongodb://mongo:27017/database-name', function(err, db) { console.log(db); });
```

The MongoDB Service previously created tells Kubernetes to configure the cluster so 'mongo' points to the MongoDB instance created earlier.

#### Custom Container

You should have your own container that runs your Node.js code hosted in a container registry.

See [this example](https://medium.com/google-cloud-platform-developer-advocates/running-a-mean-stack-on-google-cloud-platform-with-kubernetes-149ca81c2b5d#8edc) to see how to make your own Node.js container.

Once you have created your container, create the web controller.

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  labels:
    name: web
  name: web-controller
spec:
  replicas: 2
  selector:
    name: web
  template:
    metadata:
      labels:
        name: web
    spec:
      containers:
      - image: <YOUR-CONTAINER>
        name: web
        ports:
        - containerPort: 3000
          name: http-server
```

[Download file](web-controller.yaml)

Replace <YOUR-CONTAINER> with the url of your container.

This Controller will create two replicas of the Node.js container, and each Node.js container will have the tag "web" and expose port 3000. The Service LoadBalancer will forward port 80 traffic to port 3000 automatically, along with load balancing traffic between the two instances.

To start the Controller, run:

```sh
kubectl create -f examples/nodesjs-mongodb/web-controller.yaml
```

#### Demo Container

If you DON'T want to create a custom container, you can use the following YAML file:

Note: You cannot run both Controllers at the same time, as they both try to control the same Pods.

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  labels:
    name: web
  name: web-controller
spec:
  replicas: 2
  selector:
    name: web
  template:
    metadata:
      labels:
        name: web
    spec:
      containers:
      - image: node:0.10.40
        command: ['/bin/sh', '-c']
        args: ['cd /home && git clone https://github.com/ijason/NodeJS-Sample-App.git demo && cd demo/EmployeeDB/ && npm install && sed -i -- ''s/localhost/mongo/g'' app.js && node app.js']
        name: web
        ports:
        - containerPort: 3000
          name: http-server
```

[Download file](web-controller-demo.yaml)

This will use the default Node.js container, and will pull and execute code at run time. This is not recommended; typically, your code should be part of the container.

To start the Controller, run:

```sh
kubectl create -f examples/nodesjs-mongodb/web-controller-demo.yaml
```

### Testing it out

Now that all the components are running, visit the IP address of the load balancer to access the website.

With Google Cloud Platform, get the IP address of all load balancers with the following command:

```sh
gcloud compute forwarding-rules list
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/nodesjs-mongodb/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Using Flocker volumes

[Flocker](https://clusterhq.com/flocker) is an open-source clustered container data volume manager. It provides management
and orchestration of data volumes backed by a variety of storage backends.

This example provides information about how to set-up a Flocker installation and configure it in Kubernetes, as well as how to use the plugin to use Flocker datasets as volumes in Kubernetes.

### Prerequisites

A Flocker cluster is required to use Flocker with Kubernetes. A Flocker cluster comprises:

- *Flocker Control Service*: provides a REST over HTTP API to modify the desired configuration of the cluster;
- *Flocker Dataset Agent(s)*: a convergence agent that modifies the cluster state to match the desired configuration;
- *Flocker Container Agent(s)*: a convergence agent that modifies the cluster state to match the desired configuration (unused in this configuration but still required in the cluster).

The Flocker cluster can be installed on the same nodes you are using for Kubernetes. For instance, you can install the Flocker Control Service on the same node as Kubernetes Master and Flocker Dataset/Container Agents on every Kubernetes Slave node.

It is recommended to follow [Installing Flocker](https://docs.clusterhq.com/en/latest/install/index.html) and the instructions below to set-up the Flocker cluster to be used with Kubernetes.

#### Flocker Control Service

The Flocker Control Service should be installed manually on a host. In the future, this may be deployed in pod(s) and exposed as a Kubernetes service.

#### Flocker Agent(s)

The Flocker Agents should be manually installed on *all* Kubernetes nodes. These agents are responsible for (de)attachment and (un)mounting and are therefore services that should be run with appropriate privileges on these hosts.

In order for the plugin to connect to Flocker (via REST API), several environment variables must be specified on *all* Kubernetes nodes. This may be specified in an init script for the node's Kubelet service, for example, you could store the below environment variables in a file called `/etc/flocker/env` and place `EnvironmentFile=/etc/flocker/env` into `/etc/systemd/system/kubelet.service` or wherever the `kubelet.service` file lives.

The environment variables that need to be set are:

- `FLOCKER_CONTROL_SERVICE_HOST` should refer to the hostname of the Control Service
- `FLOCKER_CONTROL_SERVICE_PORT` should refer to the port of the Control Service (the API service defaults to 4523 but this must still be specified)

The following environment variables should refer to keys and certificates on the host that are specific to that host.

- `FLOCKER_CONTROL_SERVICE_CA_FILE` should refer to the full path to the cluster certificate file
- `FLOCKER_CONTROL_SERVICE_CLIENT_KEY_FILE` should refer to the full path to the [api key](https://docs.clusterhq.com/en/latest/config/generate-api-plugin.html) file for the API user
- `FLOCKER_CONTROL_SERVICE_CLIENT_CERT_FILE` should refer to the full path to the [api certificate](https://docs.clusterhq.com/en/latest/config/generate-api-plugin.html) file for the API user

More details regarding cluster authentication can be found at the documentation: [Flocker Cluster Security & Authentication](https://docs.clusterhq.com/en/latest/concepts/security.html) and [Configuring Cluster Authentication](https://docs.clusterhq.com/en/latest/config/configuring-authentication.html).

### Create a pod with a Flocker volume

**Note**: A new dataset must first be provisioned using the Flocker tools or Docker CLI *(To use the Docker CLI, you need the [Flocker plugin for Docker](https://clusterhq.com/docker-plugin/) installed along with Docker 1.9+)*. For example, using the [Volumes CLI](https://docs.clusterhq.com/en/latest/labs/volumes-cli.html), create a new dataset called 'my-flocker-vol' of size 10GB:

```sh
flocker-volumes create -m name=my-flocker-vol -s 10G -n <node-uuid>

# -n or --node= Is the initial primary node for dataset (any unique 
# prefix of node uuid, see flocker-volumes list-nodes)
```

The following *volume* spec from the [example pod](flocker-pod.yml) illustrates how to use this Flocker dataset as a volume.

> Note, the [example pod](flocker-pod.yml) used here does not include a replication controller, therefore the POD will not be rescheduled upon failure. If your looking for an example that does include a replication controller and service spec you can use [this example pod including a replication controller](flocker-pod-with-rc.yml)

```yaml
  volumes:
    - name: www-root
      flocker:
        datasetName: my-flocker-vol
```

- **datasetName** is the unique name for the Flocker dataset and should match the *name* in the metadata.

Use `kubetctl` to create the pod.

```sh
$ kubectl create -f examples/volumes/flocker/flocker-pod.yml
```

You should now verify that the pod is running and determine it's IP address:

```sh
$ kubectl get pods
NAME             READY     STATUS    RESTARTS   AGE
flocker          1/1       Running   0          3m
$ kubectl get pods flocker -t '{{.status.hostIP}}{{"\n"}}'
172.31.25.62
```

An `ls` of the `/flocker` directory on the host (identified by the IP as above) will show the mount point for the volume.

```sh
$ ls /flocker
0cf8789f-00da-4da0-976a-b6b1dc831159
```

You can also see the mountpoint by inspecting the docker container on that host.

```sh
$ docker inspect -f "{{.Mounts}}" <container-id> | grep flocker
...{ /flocker/0cf8789f-00da-4da0-976a-b6b1dc831159 /usr/share/nginx/html true}
```

Add an index.html inside this directory and use `curl` to see this HTML file served up by nginx.

```sh
$ echo "<h1>Hello, World</h1>" | tee /flocker/0cf8789f-00da-4da0-976a-b6b1dc831159/index.html
$ curl ip

```

### More Info

Read more about the [Flocker Cluster Architecture](https://docs.clusterhq.com/en/latest/concepts/architecture.html) and learn more about Flocker by visiting the [Flocker Documentation](https://docs.clusterhq.com/).

#### Video Demo

To see a demo example of using Kubernetes and Flocker, visit [Flocker's blog post on High Availability with Kubernetes and Flocker](https://clusterhq.com/2015/12/22/ha-demo-kubernetes-flocker/)

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/flocker/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Portworx Volume

  - [Portworx](#portworx)
  - [Prerequisites](#prerequisites)
  - [Examples](#examples)
    - [Using Pre-provisioned Portworx Volumes](#pre-provisioned)
      - [Running Pod](#running-pod)
      - [Persistent Volumes](#persistent-volumes)
    - [Using Dynamic Provisioning](#dynamic-provisioning)
      - [Storage Class](#storage-class)

## Portworx

[Portworx](http://www.portworx.com) can be used as a storage provider for your Kubernetes cluster. Portworx pools your servers capacity and turns your servers
or cloud instances into converged, highly available compute and storage nodes

## Prerequisites

- A Portworx instance running on all of your Kubernetes nodes. For
  more information on how you can install Portworx can be found [here](http://docs.portworx.com)

## Examples

The following examples assumes that you already have a running Kubernetes cluster with Portworx installed on all nodes.

### Using Pre-provisioned Portworx Volumes

  Create a Volume using Portworx CLI.
  On one of the Kubernetes nodes with Portworx installed run the following command

  ```shell
  /opt/pwx/bin/pxctl volume create <vol-id> --size <size> --fs <fs-type>
  ```

#### Running Pods

   Create Pod which uses Portworx Volumes

   Example spec:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
    name: test-portworx-volume-pod
   spec:
     containers:
     - image: gcr.io/google_containers/test-webserver
       name: test-container
       volumeMounts:
       - mountPath: /test-portworx-volume
         name: test-volume
     volumes:
     - name: test-volume
       # This Portworx volume must already exist.
       portworxVolume:
         volumeID: "<vol-id>"
         fsType: "<fs-type>"
   ```

   [Download example](portworx-volume-pod.yaml?raw=true)

   Make sure to replace <vol-id> and <fs-type> in the above spec with
   the ones that you used while creating the volume.

   Create the Pod.

   ``` bash
   $ kubectl create -f examples/volumes/portworx/portworx-volume-pod.yaml
   ```

   Verify that pod is running:

   ```bash
   $ kubectl.sh get pods
     NAME                       READY     STATUS    RESTARTS   AGE
     test-portworx-volume-pod   1/1       Running   0          16s
   ```

#### Persistent Volumes

  1. Create Persistent Volume.

      Example spec:

      ```yaml
      apiVersion: v1
      kind: PersistentVolume
      metadata:
        name: <vol-id>
      spec:
        capacity:
          storage: <size>Gi
        accessModes:
          - ReadWriteOnce
        persistentVolumeReclaimPolicy: Retain
        portworxVolume:
          volumeID: "<vol-id>"
          fsType:   "<fs-type>"
      ```

      Make sure to replace <vol-id>, <size> and <fs-type> in the above spec with
      the ones that you used while creating the volume.

      [Download example](portworx-volume-pv.yaml?raw=true)

      Creating the persistent volume:

      ``` bash
      $ kubectl create -f examples/volumes/portworx/portworx-volume-pv.yaml
      ```

      Verifying persistent volume is created:

      ``` bash
      $ kubectl describe pv pv0001
      Name: 	        pv0001
      Labels:		<none>
      StorageClass:
      Status:		Available
      Claim:
      Reclaim Policy:	Retain
      Access Modes:	RWO
      Capacity:	2Gi
      Message:
      Source:
      Type:	        PortworxVolume (a Portworx Persistent Volume resource)
      VolumeID:	        pv0001
      FSType:           ext4
      No events.
      ```

  2. Create Persistent Volume Claim.

      Example spec:

      ```yaml
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: pvc0001
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: <size>Gi
      ```

      [Download example](portworx-volume-pvc.yaml?raw=true)

      Creating the persistent volume claim:

      ``` bash
      $ kubectl create -f examples/volumes/portworx/portworx-volume-pvc.yaml
      ```

      Verifying persistent volume claim is created:

      ``` bash
      $ kubectl describe pvc pvc0001
      Name:		pvc0001
      Namespace:	default
      Status:		Bound
      Volume:		pv0001
      Labels:		<none>
      Capacity:	2Gi
      Access Modes:	RWO
      No events.
      ```

  3. Create Pod which uses Persistent Volume Claim.

      See example:

      ```yaml
      apiVersion: v1
      kind: Pod
      metadata:
        name: pvpod
      spec:
        containers:
        - name: test-container
          image: gcr.io/google_containers/test-webserver
          volumeMounts:
          - name: test-volume
            mountPath: /test-portworx-volume
        volumes:
        - name: test-volume
          persistentVolumeClaim:
            claimName: pvc0001
      ```

      [Download example](portworx-volume-pvcpod.yaml?raw=true)

      Creating the pod:

      ``` bash
      $ kubectl create -f examples/volumes/portworx/portworx-volume-pvcpod.yaml
      ```

      Verifying pod is created:

      ``` bash
      $ kubectl get pod pvpod
      NAME      READY     STATUS    RESTARTS   AGE
      pvpod       1/1     Running   0          48m        
      ```

### Using Dynamic Provisioning

Using Dynamic Provisioning and Storage Classes you don't need to
create Portworx volumes out of band and they will be created automatically.

#### Storage Class

  Using Storage Classes objects an admin can define the different classes of Portworx Volumes
  that are offered in a cluster. Following are the different parameters that can be used to define a Portworx
  Storage Class

  * `fs`: filesystem to be laid out: none|xfs|ext4 (default: `ext4`)
  * `block_size`: block size in Kbytes (default: `32`)
  * `repl`: replication factor [1..3] (default: `1`)
  * `io_priority`: IO Priority: [high|medium|low] (default: `low`)
  * `snap_interval`: snapshot interval in minutes, 0 disables snaps (default: `0`)
  * `aggregation_level`: specifies the number of replication sets the volume can be aggregated from (default: `1`)
  * `ephemeral`: ephemeral storage [true|false] (default `false`)


  1. Create Storage Class.

     See example:

     ```yaml
     kind: StorageClass
     apiVersion: storage.k8s.io/v1beta1
     metadata:
       name: portworx-io-priority-high
     provisioner: kubernetes.io/portworx-volume
     parameters:
       repl: "1"
       snap_interval:   "70"
       io_priority:  "high"
     ```

     [Download example](portworx-volume-sc-high.yaml?raw=true)

     Creating the storageclass:

     ``` bash
     $ kubectl create -f examples/volumes/portworx/portworx-volume-sc-high.yaml
     ```

     Verifying storage class is created:

     ``` bash
     $ kubectl describe storageclass portworx-io-priority-high
       Name: 	        portworx-io-priority-high
       IsDefaultClass:	No
       Annotations:	<none>
       Provisioner:	kubernetes.io/portworx-volume
       Parameters:	io_priority=high,repl=1,snapshot_interval=70
       No events.
     ```

  2. Create Persistent Volume Claim.

     See example:

     ```yaml
     kind: PersistentVolumeClaim
     apiVersion: v1
     metadata:
       name: pvcsc001
       annotations:
         volume.beta.kubernetes.io/storage-class: portworx-io-priority-high
     spec:
       accessModes:
         - ReadWriteOnce
       resources:
         requests:
           storage: 2Gi
     ```

     [Download example](portworx-volume-pvcsc.yaml?raw=true)

     Creating the persistent volume claim:

     ``` bash
     $ kubectl create -f examples/volumes/portworx/portworx-volume-pvcsc.yaml
     ```

     Verifying persistent volume claim is created:

     ``` bash
     $ kubectl describe pvc pvcsc001
     Name:	      pvcsc001
     Namespace:      default
     StorageClass:   portworx-io-priority-high
     Status:	      Bound
     Volume:         pvc-e5578707-c626-11e6-baf6-08002729a32b
     Labels:	      <none>
     Capacity:	      2Gi
     Access Modes:   RWO
     No Events
     ```

     Persistent Volume is automatically created and is bounded to this pvc.

     Verifying persistent volume claim is created:

     ``` bash
     $ kubectl describe pv pvc-e5578707-c626-11e6-baf6-08002729a32b
     Name: 	      pvc-e5578707-c626-11e6-baf6-08002729a32b
     Labels:         <none>
     StorageClass:   portworx-io-priority-high
     Status:	      Bound
     Claim:	      default/pvcsc001
     Reclaim Policy: Delete
     Access Modes:   RWO
     Capacity:	      2Gi
     Message:
     Source:
         Type:	      PortworxVolume (a Portworx Persistent Volume resource)
	 VolumeID:   374093969022973811
     No events.
     ```

  3. Create Pod which uses Persistent Volume Claim with storage class.

     See example:

     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: pvpod
     spec:
       containers:
       - name: test-container
         image: gcr.io/google_containers/test-webserver
         volumeMounts:
         - name: test-volume
           mountPath: /test-portworx-volume
     volumes:
     - name: test-volume
       persistentVolumeClaim:
         claimName: pvcsc001
     ```

     [Download example](portworx-volume-pvcscpod.yaml?raw=true)

     Creating the pod:

     ``` bash
     $ kubectl create -f examples/volumes/portworx/portworx-volume-pvcscpod.yaml
     ```

     Verifying pod is created:

     ``` bash
     $ kubectl get pod pvpod
     NAME      READY     STATUS    RESTARTS   AGE
     pvpod       1/1     Running   0          48m        
     ```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/portworx/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# How to Use it?

Install Ceph on the Kubernetes host. For example, on Fedora 21

    # yum -y install ceph-common

If you don't have a Ceph cluster, you can set up a [containerized Ceph cluster](https://github.com/ceph/ceph-docker)

Then get the keyring from the Ceph cluster and copy it to */etc/ceph/keyring*.

Once you have installed Ceph and new Kubernetes, you can create a pod based on my examples [rbd.json](rbd.json)  [rbd-with-secret.json](rbd-with-secret.json). In the pod JSON, you need to provide the following information.

- *monitors*:  Ceph monitors.
- *pool*: The name of the RADOS pool, if not provided, default *rbd* pool is used.
- *image*: The image name that rbd has created.
- *user*: The RADOS user name. If not provided, default *admin* is used.
- *keyring*: The path to the keyring file. If not provided, default */etc/ceph/keyring* is used.
- *secretName*: The name of the authentication secrets. If provided, *secretName* overrides *keyring*. Note, see below about how to create a secret.
- *fsType*: The filesystem type (ext4, xfs, etc) that formatted on the device.
- *readOnly*: Whether the filesystem is used as readOnly.

# Use Ceph Authentication Secret

If Ceph authentication secret is provided, the secret should be first be *base64 encoded*, then encoded string is placed in a secret yaml. For example, getting Ceph user `kube`'s base64 encoded secret can use the following command:

```console
  # grep key /etc/ceph/ceph.client.kube.keyring |awk '{printf "%s", $NF}'|base64
QVFBTWdYaFZ3QkNlRGhBQTlubFBhRnlmVVNhdEdENGRyRldEdlE9PQ==
```

An example yaml is provided [here](secret/ceph-secret.yaml). Then post the secret through ```kubectl``` in the following command.

```console
    # kubectl create -f examples/volumes/rbd/secret/ceph-secret.yaml
```

# Get started

Here are my commands:

```console
    # kubectl create -f examples/volumes/rbd/rbd.json
    # kubectl get pods
```

On the Kubernetes host, I got these in mount output

```console
    #mount |grep kub
	/dev/rbd0 on /var/lib/kubelet/plugins/kubernetes.io/rbd/rbd/kube-image-foo type ext4 (ro,relatime,stripe=4096,data=ordered)
	/dev/rbd0 on /var/lib/kubelet/pods/ec2166b4-de07-11e4-aaf5-d4bed9b39058/volumes/kubernetes.io~rbd/rbdpd type ext4 (ro,relatime,stripe=4096,data=ordered)
```

 If you ssh to that machine, you can run `docker ps` to see the actual pod and `docker inspect` to see the volumes used by the container.


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/rbd/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# How to Use it?

Install *cifs-utils* on the Kubernetes host. For example, on Fedora based Linux

    # yum -y install cifs-utils

Note, as explained in [Azure File Storage for Linux](https://azure.microsoft.com/en-us/documentation/articles/storage-how-to-use-files-linux/), the Linux hosts and the file share must be in the same Azure region.

Obtain an Microsoft Azure storage account and create a [secret](secret/azure-secret.yaml) that contains the base64 encoded Azure Storage account name and key. In the secret file, base64-encode Azure Storage account name and pair it with name *azurestorageaccountname*, and base64-encode Azure Storage access key and pair it with name *azurestorageaccountkey*.

Then create a Pod using the volume spec based on [azure](azure.yaml).

In the pod, you need to provide the following information:

- *secretName*:  the name of the secret that contains both Azure storage account name and key.
- *shareName*: The share name to be used.
- *readOnly*: Whether the filesystem is used as readOnly.

Create the secret:

```console
    # kubectl create -f examples/volumes/azure_file/secret/azure-secret.yaml
```

You should see the account name and key from `kubectl get secret`

Then create the Pod:

```console
    # kubectl create -f examples/volumes/azure_file/azure.yaml
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/azure_file/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Outline

This example describes how to create Web frontend server, an auto-provisioned persistent volume on GCE, and an NFS-backed persistent claim.

Demonstrated Kubernetes Concepts:

* [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to
  define persistent disks (disk lifecycle not tied to the Pods).
* [Services](https://kubernetes.io/docs/concepts/services-networking/service/) to enable Pods to
  locate one another.

![alt text][nfs pv example]

As illustrated above, two persistent volumes are used in this example:

- Web frontend Pod uses a persistent volume based on NFS server, and
- NFS server uses an auto provisioned [persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) from GCE PD or AWS EBS.

Note, this example uses an NFS container that doesn't support NFSv4.

[nfs pv example]: nfs-pv.png


## Quickstart

```console
$ kubectl create -f examples/volumes/nfs/provisioner/nfs-server-gce-pv.yaml
$ kubectl create -f examples/volumes/nfs/nfs-server-rc.yaml
$ kubectl create -f examples/volumes/nfs/nfs-server-service.yaml
# get the cluster IP of the server using the following command
$ kubectl describe services nfs-server
# use the NFS server IP to update nfs-pv.yaml and execute the following
$ kubectl create -f examples/volumes/nfs/nfs-pv.yaml
$ kubectl create -f examples/volumes/nfs/nfs-pvc.yaml
# run a fake backend
$ kubectl create -f examples/volumes/nfs/nfs-busybox-rc.yaml
# get pod name from this command
$ kubectl get pod -l name=nfs-busybox
# use the pod name to check the test file
$ kubectl exec nfs-busybox-jdhf3 -- cat /mnt/index.html
```

## Example of NFS based persistent volume

See [NFS Service and Replication Controller](nfs-web-rc.yaml) for a quick example of how to use an NFS
volume claim in a replication controller. It relies on the
[NFS persistent volume](nfs-pv.yaml) and
[NFS persistent volume claim](nfs-pvc.yaml) in this example as well.

## Complete setup

The example below shows how to export a NFS share from a single pod replication
controller and import it into two replication controllers.

### NFS server part

Define [the NFS Service and Replication Controller](nfs-server-rc.yaml) and
[NFS service](nfs-server-service.yaml):

The NFS server exports an an auto-provisioned persistent volume backed by GCE PD:

```console
$ kubectl create -f examples/volumes/nfs/provisioner/nfs-server-gce-pv.yaml
```

```console
$ kubectl create -f examples/volumes/nfs/nfs-server-rc.yaml
$ kubectl create -f examples/volumes/nfs/nfs-server-service.yaml
```

The directory contains dummy `index.html`. Wait until the pod is running
by checking `kubectl get pods -l role=nfs-server`.

### Create the NFS based persistent volume claim

The [NFS busybox controller](nfs-busybox-rc.yaml) uses a simple script to
generate data written to the NFS server we just started. First, you'll need to
find the cluster IP of the server:

```console
$ kubectl describe services nfs-server
```

Replace the invalid IP in the [nfs PV](nfs-pv.yaml). (In the future,
we'll be able to tie these together using the service names, but for
now, you have to hardcode the IP.)

Create the the [persistent volume](https://kubernetes.io/docs/user-guide/persistent-volumes.md)
and the persistent volume claim for your NFS server. The persistent volume and
claim gives us an indirection that allow multiple pods to refer to the NFS
server using a symbolic name rather than the hardcoded server address.

```console
$ kubectl create -f examples/volumes/nfs/nfs-pv.yaml
$ kubectl create -f examples/volumes/nfs/nfs-pvc.yaml
```

## Setup the fake backend

The [NFS busybox controller](nfs-busybox-rc.yaml) updates `index.html` on the
NFS server every 10 seconds. Let's start that now:

```console
$ kubectl create -f examples/volumes/nfs/nfs-busybox-rc.yaml
```

Conveniently, it's also a `busybox` pod, so we can get an early check
that our mounts are working now. Find a busybox pod and exec:

```console
$ kubectl get pod -l name=nfs-busybox
NAME                READY     STATUS    RESTARTS   AGE
nfs-busybox-jdhf3   1/1       Running   0          25m
nfs-busybox-w3s4t   1/1       Running   0          25m
$ kubectl exec nfs-busybox-jdhf3 -- cat /mnt/index.html
Thu Oct 22 19:20:18 UTC 2015
nfs-busybox-w3s4t
```

You should see output similar to the above if everything is working well. If
it's not, make sure you changed the invalid IP in the [NFS PV](nfs-pv.yaml) file
and make sure the `describe services` command above had endpoints listed
(indicating the service was associated with a running pod).

### Setup the web server

The [web server controller](nfs-web-rc.yaml) is an another simple replication
controller demonstrates reading from the NFS share exported above as a NFS
volume and runs a simple web server on it.

Define the pod:

```console
$ kubectl create -f examples/volumes/nfs/nfs-web-rc.yaml
```

This creates two pods, each of which serve the `index.html` from above. We can
then use a simple service to front it:

```console
kubectl create -f examples/volumes/nfs/nfs-web-service.yaml
```

We can then use the busybox container we launched before to check that `nginx`
is serving the data appropriately:

```console
$ kubectl get pod -l name=nfs-busybox
NAME                READY     STATUS    RESTARTS   AGE
nfs-busybox-jdhf3   1/1       Running   0          1h
nfs-busybox-w3s4t   1/1       Running   0          1h
$ kubectl get services nfs-web
NAME      LABELS    SELECTOR            IP(S)        PORT(S)
nfs-web   <none>    role=web-frontend   10.0.68.37   80/TCP
$ kubectl exec nfs-busybox-jdhf3 -- wget -qO- http://10.0.68.37
Thu Oct 22 19:28:55 UTC 2015
nfs-busybox-w3s4t
```




<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/nfs/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# NFS-exporter container with a file

This container exports /exports with index.html in it via NFS. Based on
../exports. Since some Linux kernels have issues running NFSv4 daemons in containers,
only NFSv3 is opened in this container.

Available as `gcr.io/google-samples/nfs-server`



<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/nfs/nfs-data/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
<!-- BEGIN MUNGE: UNVERSIONED_WARNING -->

<!-- BEGIN STRIP_FOR_RELEASE -->

<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING"
     width="25" height="25">
<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING"
     width="25" height="25">
<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING"
     width="25" height="25">
<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING"
     width="25" height="25">
<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING"
     width="25" height="25">

<h2>PLEASE NOTE: This document applies to the HEAD of the source tree</h2>

If you are using a released version of Kubernetes, you should
refer to the docs that go with that version.

Documentation for other releases can be found at
[releases.k8s.io](http://releases.k8s.io).
</strong>
--

<!-- END STRIP_FOR_RELEASE -->

<!-- END MUNGE: UNVERSIONED_WARNING -->

# Dell EMC ScaleIO Volume Plugin for Kubernetes

This document shows how to configure Kubernetes resources to consume storage from volumes hosted on ScaleIO cluster.

## Pre-Requisites

* Kubernetes ver 1.6 or later
* ScaleIO ver 2.0 or later
* A ScaleIO cluster with an API gateway
* ScaleIO SDC binary installed/configured on each Kubernetes node that will consume storage

## ScaleIO Setup

This document assumes you are familiar with ScaleIO and have a cluster ready to go.  If you are *not familiar* with ScaleIO, please review *Learn how to setup a 3-node* [ScaleIO cluster on Vagrant](https://github.com/codedellemc/labs/tree/master/setup-scaleio-vagrant) and see *General instructions on* [setting up ScaleIO](https://www.emc.com/products-solutions/trial-software-download/scaleio.htm)

For this demonstration, ensure the following: 

 - The ScaleIO `SDC` component is installed and properly configured on all Kubernetes nodes where deployed pods will consume ScaleIO-backed volumes.
 - You have a configured ScaleIO gateway that is accessible from the Kubernetes nodes. 

## Deploy Kubernetes Secret for ScaleIO

The ScaleIO plugin uses a Kubernetes Secret object to store the `username` and `password` credentials.  
Kuberenetes requires the secret values to be base64-encoded to simply obfuscate (not encrypt) the clear text as shown below.

```
$> echo -n "siouser" | base64
c2lvdXNlcg==
$> echo -n "sc@l3I0" | base64
c2NAbDNJMA==
```
The previous will generate `base64-encoded` values for the username and password.  
Remember to generate the credentials for your own environment and copy them in a secret file similar to the following.  

File: [secret.yaml](secret.yaml)

```
apiVersion: v1
kind: Secret
metadata:
  name: sio-secret
type: kubernetes.io/scaleio
data:
  username: c2lvdXNlcg==
  password: c2NAbDNJMA==
```

Notice the name of the secret specified above as `sio-secret`.  It will be referred in other YAML files.  Next, deploy the secret.

```
$ kubectl create -f ./examples/volumes/scaleio/secret.yaml
```

## Deploying Pods with Persistent Volumes

The example presented in this section shows how the ScaleIO volume plugin can automatically attach, format, and mount an existing ScaleIO volume for pod. 
The Kubernetes ScaleIO volume spec supports the following attributes:

| Attribute | Description |
|-----------|-------------|
| gateway | address to a ScaleIO API gateway (required)|
| system  | the name of the ScaleIO system (required)|
| protectionDomain| the name of the ScaleIO protection domain (default `default`)|
| storagePool| the name of the volume storage pool (default `default`)|
| storageMode| the storage provision mode: `ThinProvisionned` (default) or `ThickProvisionned`|
| volumeName| the name of an existing volume in ScaleIO (required)|
| secretRef:name| reference to a configured Secret object (required, see Secret earlier)|
| readOnly| specifies the access mode to the mounted volume (default `false`)|
| fsType| the file system to use for the volume (default `ext4`)|

### Create Volume

Static persistent volumes require that the volume, to be consumed by the pod, be already created in ScaleIO.  You can use your ScaleIO tooling to create a new volume or use the name of a volume that already exists in ScaleIO.  For this demo, we assume there's a volume named `vol-0`.  If you want to use an existing volume, ensure its name is reflected properly in the `volumeName` attribute below.

### Deploy Pod YAML

Create a pod YAML file that declares the volume (above) to be used.

File: [pod.yaml](pod.yaml)

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-0
spec:
  containers:
  - image: gcr.io/google_containers/test-webserver
    name: pod-0
    volumeMounts:
    - mountPath: /test-pd
      name: vol-0
  volumes:
  - name: vol-0
    scaleIO:
      gateway: https://localhost:443/api
      system: scaleio
      volumeName: vol-0
      secretRef:
        name: sio-secret
      fsType: xfs
```
Notice the followings in the previous YAML:

- Update the `gatewway` to point to your ScaleIO gateway endpoint.
- The `volumeName` attribute refers to the name of an existing volume in ScaleIO.
- The `secretRef:name` attribute references the name of the secret object deployed earlier.

Next, deploy the pod.

```
$> kubectl create -f examples/volumes/scaleio/pod.yaml
```
You can verify the pod:
```
$> kubectl get pod
NAME      READY     STATUS    RESTARTS   AGE
pod-0     1/1       Running   0          33s
```
Or for more detail, use 
```
kubectl describe pod pod-0
```
You can see the attached/mapped volume on the node:
```
$> lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
...
scinia      252:0    0    8G  0 disk /var/lib/kubelet/pods/135986c7-dcb7-11e6-9fbf-080027c990a7/volumes/kubernetes.io~scaleio/vol-0
```

## StorageClass and Dynamic Provisioning

In the example in this section, we will see how the ScaleIO volume plugin can automatically provision described in a `StorageClass`.
The ScaleIO volume plugin is a dynamic provisioner identified as `kubernetes.io/scaleio` and supports the following parameters:

| Parameter | Description |
|-----------|-------------|
| gateway | address to a ScaleIO API gateway (required)|
| system  | the name of the ScaleIO system (required)|
| protectionDomain| the name of the ScaleIO protection domain (default `default`)|
| storagePool| the name of the volume storage pool (default `default`)|
| storageMode| the storage provision mode: `ThinProvisionned` (default) or `ThickProvisionned`|
| secretRef| reference to the name of a configured Secret object (required)|
| readOnly| specifies the access mode to the mounted volume (default `false`)|
| fsType| the file system to use for the volume (default `ext4`)|


### ScaleIO StorageClass

Define a new `StorageClass` as shown in the following YAML.

File [sc.yaml](sc.yaml)

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: sio-small
provisioner: kubernetes.io/scaleio
parameters:
  gateway: https://localhost:443/api
  system: scaleio
  protectionDomain: default
  secretRef: sio-secret
  fsType: xfs
```
Note the followings:

- The `name` attribute is set to sio-small . It will be referenced later.
- The `secretRef` attribute matches the name of the Secret object created earlier.

Next, deploy the storage class file.

```
$> kubectl create -f examples/volumes/scaleio/sc.yaml

$> kubectl get sc
NAME        TYPE
sio-small   kubernetes.io/scaleio
```

### PVC for the StorageClass

The next step is to define/deploy a `PersistentVolumeClaim` that will use the StorageClass.

File [sc-pvc.yaml](sc-pvc.yaml)

```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvc-sio-small
  annotations:
      volume.beta.kubernetes.io/storage-class: sio-small
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

Note the `annotations:` entry which specifies annotation `volume.beta.kubernetes.io/storage-class: sio-small` which references the name of the storage class defined earlier.

Next, we deploy PVC file for the storage class.  This step will cause the Kubernetes ScaleIO plugin to create the volume in the storage system.  
```
$> kubectl create -f examples/volumes/scaleio/sc-pvc.yaml
```
You verify that a new volume created in the ScaleIO dashboard.  You can also verify the newly created volume as follows.
```
 kubectl get pvc
NAME            STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
pvc-sio-small   Bound     pvc-5fc78518-dcae-11e6-a263-080027c990a7   10Gi       RWO           1h
```

###Pod for PVC and SC
At this point, the volume is created (by the claim) in the storage system.  To use it, we must define a pod that references the volume as done in this YAML.

File [pod-sc-pvc.yaml](pod-sc-pvc.yaml)

```
kind: Pod
apiVersion: v1
metadata:
  name: pod-sio-small
spec:
  containers:
    - name: pod-sio-small-container
      image: gcr.io/google_containers/test-webserver
      volumeMounts:
      - mountPath: /test
        name: test-data
  volumes:
    - name: test-data
      persistentVolumeClaim:
        claimName: pvc-sio-small
```

Notice that the `claimName:` attribute refers to the name of the PVC defined and deployed earlier.  Next, let us deploy the file.

```
$> kubectl create -f examples/volumes/scaleio/pod-sc-pvc.yaml
```
We can now verify that the new pod is deployed OK.
```
kubectl get pod
NAME            READY     STATUS    RESTARTS   AGE
pod-0           1/1       Running   0          23m
pod-sio-small   1/1       Running   0          5s
```
You can use the ScaleIO dashboard to verify that the new volume has one attachment.  You can verify the volume information for the pod:
```
$> kubectl describe pod pod-sio-small
...
Volumes:
  test-data:
    Type:	PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:	pvc-sio-small
    ReadOnly:	false
...
```
Lastly, you can see the volume's attachment on the Kubernetes node:
```
$> lsblk
...
scinia      252:0    0    8G  0 disk /var/lib/kubelet/pods/135986c7-dcb7-11e6-9fbf-080027c990a7/volumes/kubernetes.io~scaleio/vol-0
scinib      252:16   0   16G  0 disk /var/lib/kubelet/pods/62db442e-dcba-11e6-9fbf-080027c990a7/volumes/kubernetes.io~scaleio/sio-5fc9154ddcae11e68db708002

```
<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/scaleio/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
This is a simple web server pod which serves HTML from an AWS EBS
volume.

If you did not use kube-up script, make sure that your minions have the following IAM permissions ([Amazon IAM Roles](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#create-iam-role-console)):

```shell
  ec2:AttachVolume
  ec2:DetachVolume
  ec2:DescribeInstances
  ec2:DescribeVolumes
```

Create a volume in the same region as your node.

Add your volume information in the pod description file aws-ebs-web.yaml then create the pod:

```shell
  $ kubectl create -f examples/volumes/aws_ebs/aws-ebs-web.yaml
```

Add some data to the volume if is empty:

```sh
  $ echo  "Hello World" >& /var/lib/kubelet/plugins/kubernetes.io/aws-ebs/mounts/aws/{Region}/{Volume ID}/index.html
```

You should now be able to query your web server:

```sh
  $ curl <Pod IP address>
  $ Hello World
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/aws_ebs/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Introduction

The Kubernetes iSCSI implementation can connect to iSCSI devices via open-iscsi and multipathd on Linux.
Currently supported features are
  * Connecting to one portal
  * Mounting a device directly or via multipathd
  * Formatting and partitioning any new device connected
  * CHAP authentication

## Prerequisites

This example expects there to be a working iSCSI target to connect to.
If there isn't one in place then it is possible to setup a software version on Linux by following these guides

  * [Setup a iSCSI target on Fedora](http://www.server-world.info/en/note?os=Fedora_21&p=iscsi)
  * [Install the iSCSI initiator on Fedora](http://www.server-world.info/en/note?os=Fedora_21&p=iscsi&f=2)
  * [Install multipathd for mpio support if required](http://www.linuxstories.eu/2014/07/how-to-setup-dm-multipath-on-rhel.html)


## Creating the pod with iSCSI persistent storage

Once you have configured the iSCSI initiator, you can create a pod based on the example *iscsi.yaml*. In the pod YAML, you need to provide *targetPortal* (the iSCSI target's **IP** address and *port* if not the default port 3260), target's *iqn*, *lun*, and the type of the filesystem that has been created on the lun, and *readOnly* boolean. No initiator information is required. If you have more than one target portals for a single IQN, you can mention other portal IPs in *portals* field.

If you want to use an iSCSI offload card or other open-iscsi transports besides tcp, setup an iSCSI interface and provide *iscsiInterface* in the pod YAML. The default name for an iscsi iface (open-iscsi parameter iface.iscsi\_ifacename) is in the format transport\_name.hwaddress when generated by iscsiadm. See [open-iscsi](http://www.open-iscsi.org/docs/README) or [openstack](http://docs.openstack.org/kilo/config-reference/content/iscsi-iface-config.html) for detailed configuration information.

**Note:** If you have followed the instructions in the links above you
may have partitioned the device, the iSCSI volume plugin does not
currently support partitions so format the device as one partition or leave the device raw and Kubernetes will partition and format it one first mount.

### CHAP Authentication

To enable one-way or two-way CHAP authentication for discovery or session, following these steps.

 * Set `chapAuthDiscovery` to `true` for discovery authentication.
 * Set `chapAuthSession` to `true` for session authentication.
 * Create a CHAP secret and set `secretRef` to reference the CHAP secret.


Example can be found at [iscsi-chap.yaml](iscsi-chap.yaml)

### CHAP Secret

As illustrated in [chap-secret.yaml](chap-secret.yaml), the secret must have type `kubernetes.io/iscsi-chap` and consists of the following keys:

```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: chap-secret
type: "kubernetes.io/iscsi-chap"  
data:
  discovery.sendtargets.auth.username: 
  discovery.sendtargets.auth.password: 
  discovery.sendtargets.auth.username_in: 
  discovery.sendtargets.auth.password_in: 
  node.session.auth.username: 
  node.session.auth.password: 
  node.session.auth.username_in: 
  node.session.auth.password_in: 
```

These keys map to those used by Open-iSCSI initiator. Detailed documents on these keys can be found at [Open-iSCSI](https://github.com/open-iscsi/open-iscsi/blob/master/etc/iscsid.conf)

#### Create CHAP secret before creating iSCSI volumes and Pods

```console
# kubectl create -f examples/volumes/iscsi/chap-iscsi.yaml
```



Once the pod config is created, run it on the Kubernetes master:

```console
kubectl create -f ./your_new_pod.yaml
```

Here is the example pod created and expected output:

```console
# kubectl create -f examples/volumes/iscsi/iscsi.yaml
# kubectl get pods
NAME      READY     STATUS    RESTARTS   AGE
iscsipd   2/2       RUNNING   0           2m
```

On the Kubernetes node, verify the mount output

For a non mpio device the output should look like the following

```console
# mount |grep kub
/dev/sdb on /var/lib/kubelet/plugins/kubernetes.io/iscsi/10.0.2.15:3260-iqn.2001-04.com.example:storage.kube.sys1.xyz-lun-0 type ext4 (rw,relatime,data=ordered)
/dev/sdb on /var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-rw type ext4 (ro,relatime,data=ordered)
/dev/sdc on /var/lib/kubelet/plugins/kubernetes.io/iscsi/10.0.2.16:3260-iqn.2001-04.com.example:storage.kube.sys1.xyz-lun-0 type ext4 (rw,relatime,data=ordered)
/dev/sdc on /var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-rw type ext4 (rw,relatime,data=ordered)
/dev/sdd on /var/lib/kubelet/plugins/kubernetes.io/iscsi/10.0.2.17:3260-iqn.2001-04.com.example:storage.kube.sys1.xyz-lun-0 type ext4 (rw,relatime,data=ordered)
/dev/sdd on /var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-rw type ext4 (rw,relatime,data=ordered)
```

And for a node with mpio enabled the expected output would be similar to the following

```console
# mount |grep kub
/dev/mapper/mpatha on /var/lib/kubelet/plugins/kubernetes.io/iscsi/10.0.2.15:3260-iqn.2001-04.com.example:storage.kube.sys1.xyz-lun-0 type ext4 (rw,relatime,data=ordered)
/dev/mapper/mpatha on /var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-ro type ext4 (ro,relatime,data=ordered)
/dev/mapper/mpathb on /var/lib/kubelet/plugins/kubernetes.io/iscsi/10.0.2.16:3260-iqn.2001-04.com.example:storage.kube.sys1.xyz-lun-0 type ext4 (rw,relatime,data=ordered)
/dev/mapper/mpathb on /var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-rw type ext4 (rw,relatime,data=ordered)
/dev/mapper/mpathc on /var/lib/kubelet/plugins/kubernetes.io/iscsi/10.0.2.17:3260-iqn.2001-04.com.example:storage.kube.sys1.xyz-lun-0 type ext4 (rw,relatime,data=ordered)
/dev/mapper/mpathb on /var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-rw type ext4 (rw,relatime,data=ordered)
```


If you ssh to that machine, you can run `docker ps` to see the actual pod.

```console
# docker ps
CONTAINER ID        IMAGE                                  COMMAND             CREATED             STATUS              PORTS               NAMES
3b8a772515d2        kubernetes/pause                       "/pause"            6 minutes ago       Up 6 minutes                            k8s_iscsipd-rw.ed58ec4e_iscsipd_default_f527ca5b-6d87-11e5-aa7e-080027ff6387_d25592c5
```

Run *docker inspect* and verify the container mounted the host directory into the their */mnt/iscsipd* directory.

```console
# docker inspect --format '{{ range .Mounts }}{{ if eq .Destination "/mnt/iscsipd" }}{{ .Source }}{{ end }}{{ end }}' f855336407f4
/var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-ro

# docker inspect --format '{{ range .Mounts }}{{ if eq .Destination "/mnt/iscsipd" }}{{ .Source }}{{ end }}{{ end }}' 3b8a772515d2
/var/lib/kubelet/pods/f527ca5b-6d87-11e5-aa7e-080027ff6387/volumes/kubernetes.io~iscsi/iscsipd-rw
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/iscsi/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# vSphere Volume

  - [Prerequisites](#prerequisites)
  - [Examples](#examples)
    - [Volumes](#volumes)
    - [Persistent Volumes](#persistent-volumes)
    - [Storage Class](#storage-class)
    - [Storage Policy Management inside kubernetes] (#storage-policy-management-inside-kubernetes)
      - [Using existing vCenter SPBM policy] (#using-existing-vcenter-spbm-policy)
      - [Virtual SAN policy support](#virtual-san-policy-support)
    - [Stateful Set](#stateful-set)

## Prerequisites

- Kubernetes with vSphere Cloud Provider configured.
  For cloudprovider configuration please refer [vSphere getting started guide](http://kubernetes.io/docs/getting-started-guides/vsphere/).

## Examples

### Volumes

  1. Create VMDK.

      First ssh into ESX and then use following command to create vmdk,

      ```shell
      vmkfstools -c 2G /vmfs/volumes/datastore1/volumes/myDisk.vmdk
      ```

  2. Create Pod which uses 'myDisk.vmdk'.

     See example

     ```yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: test-vmdk
        spec:
          containers:
          - image: gcr.io/google_containers/test-webserver
            name: test-container
            volumeMounts:
            - mountPath: /test-vmdk
              name: test-volume
          volumes:
          - name: test-volume
            # This VMDK volume must already exist.
            vsphereVolume:
              volumePath: "[datastore1] volumes/myDisk"
              fsType: ext4
     ```

     [Download example](vsphere-volume-pod.yaml?raw=true)

     Creating the pod:

     ``` bash
     $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pod.yaml
     ```

     Verify that pod is running:

     ```bash
     $ kubectl get pods test-vmdk
     NAME      READY     STATUS    RESTARTS   AGE
     test-vmdk   1/1     Running   0          48m
     ```

### Persistent Volumes

  1. Create VMDK.

      First ssh into ESX and then use following command to create vmdk,

      ```shell
      vmkfstools -c 2G /vmfs/volumes/datastore1/volumes/myDisk.vmdk
      ```

  2. Create Persistent Volume.

      See example:

      ```yaml
      apiVersion: v1
      kind: PersistentVolume
      metadata:
        name: pv0001
      spec:
        capacity:
          storage: 2Gi
        accessModes:
          - ReadWriteOnce
        persistentVolumeReclaimPolicy: Retain
        vsphereVolume:
          volumePath: "[datastore1] volumes/myDisk"
          fsType: ext4
      ```
      In the above example datastore1 is located in the root folder. If datastore is member of Datastore Cluster or located in sub folder, the folder path needs to be provided in the VolumePath as below. 
      ```yaml
      vsphereVolume:
          VolumePath:	"[DatastoreCluster/datastore1] volumes/myDisk" 
      ```

      [Download example](vsphere-volume-pv.yaml?raw=true)

      Creating the persistent volume:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pv.yaml
      ```

      Verifying persistent volume is created:

      ``` bash
      $ kubectl describe pv pv0001
      Name:		pv0001
      Labels:		<none>
      Status:		Available
      Claim:
      Reclaim Policy:	Retain
      Access Modes:	RWO
      Capacity:	2Gi
      Message:
      Source:
          Type:	vSphereVolume (a Persistent Disk resource in vSphere)
          VolumePath:	[datastore1] volumes/myDisk
          FSType:	ext4
      No events.
      ```

  3. Create Persistent Volume Claim.

      See example:

      ```yaml
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: pvc0001
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 2Gi
      ```

      [Download example](vsphere-volume-pvc.yaml?raw=true)

      Creating the persistent volume claim:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pvc.yaml
      ```

      Verifying persistent volume claim is created:

      ``` bash
      $ kubectl describe pvc pvc0001
      Name:		pvc0001
      Namespace:	default
      Status:		Bound
      Volume:		pv0001
      Labels:		<none>
      Capacity:	2Gi
      Access Modes:	RWO
      No events.
      ```

  3. Create Pod which uses Persistent Volume Claim.

      See example:

      ```yaml
      apiVersion: v1
      kind: Pod
      metadata:
        name: pvpod
      spec:
        containers:
        - name: test-container
          image: gcr.io/google_containers/test-webserver
          volumeMounts:
          - name: test-volume
            mountPath: /test-vmdk
        volumes:
        - name: test-volume
          persistentVolumeClaim:
            claimName: pvc0001
      ```

      [Download example](vsphere-volume-pvcpod.yaml?raw=true)

      Creating the pod:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pvcpod.yaml
      ```

      Verifying pod is created:

      ``` bash
      $ kubectl get pod pvpod
      NAME      READY     STATUS    RESTARTS   AGE
      pvpod       1/1     Running   0          48m
      ```

### Storage Class

  __Note: Here you don't need to create vmdk it is created for you.__
  1. Create Storage Class.

      Example 1:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1beta1
      metadata:
        name: fast
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: zeroedthick
          fstype:     ext3
      ```

      [Download example](vsphere-volume-sc-fast.yaml?raw=true)

      You can also specify the datastore in the Storageclass as shown in example 2. The volume will be created on the datastore specified in the storage class.
      This field is optional. If not specified as shown in example 1, the volume will be created on the datastore specified in the vsphere config file used to initialize the vSphere Cloud Provider.

      Example 2:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1beta1
      metadata:
        name: fast
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: zeroedthick
          datastore: VSANDatastore
      ```     
      If datastore is member of DataStore Cluster or within some sub folder, the datastore folder path needs to be provided in the datastore parameter as below.

       ```yaml
       parameters:
          datastore:	DatastoreCluster/VSANDatastore
       ```

      [Download example](vsphere-volume-sc-with-datastore.yaml?raw=true)
      Creating the storageclass:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-sc-fast.yaml
      ```

      Verifying storage class is created:

      ``` bash
      $ kubectl describe storageclass fast 
      Name:           fast
      IsDefaultClass: No
      Annotations:    <none>
      Provisioner:    kubernetes.io/vsphere-volume
      Parameters:     diskformat=zeroedthick,fstype=ext3
      No events.
      ```

  2. Create Persistent Volume Claim.

      See example:

      ```yaml
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: pvcsc001
        annotations:
          volume.beta.kubernetes.io/storage-class: fast
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 2Gi
      ```

      [Download example](vsphere-volume-pvcsc.yaml?raw=true)

      Creating the persistent volume claim:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pvcsc.yaml
      ```

      Verifying persistent volume claim is created:

      ``` bash
      $ kubectl describe pvc pvcsc001
      Name:           pvcsc001
      Namespace:      default
      StorageClass:   fast
      Status:         Bound
      Volume:         pvc-83295256-f8e0-11e6-8263-005056b2349c
      Labels:         <none>
      Capacity:       2Gi
      Access Modes:   RWO
      Events:
        FirstSeen     LastSeen        Count   From                            SubObjectPath   Type            Reason                  Message
        ---------     --------        -----   ----                            -------------   --------        ------                  -------
        1m            1m              1       persistentvolume-controller                     Normal          ProvisioningSucceeded   Successfully provisioned volume pvc-83295256-f8e0-11e6-8263-005056b2349c using kubernetes.io/vsphere-volume

      ```

      Persistent Volume is automatically created and is bounded to this pvc.

      Verifying persistent volume claim is created:

      ``` bash
      $ kubectl describe pv pvc-83295256-f8e0-11e6-8263-005056b2349c
      Name:           pvc-83295256-f8e0-11e6-8263-005056b2349c
      Labels:         <none>
      StorageClass:   fast
      Status:         Bound
      Claim:          default/pvcsc001
      Reclaim Policy: Delete
      Access Modes:   RWO
      Capacity:       2Gi
      Message:
      Source:
          Type:       vSphereVolume (a Persistent Disk resource in vSphere)
          VolumePath: [datastore1] kubevols/kubernetes-dynamic-pvc-83295256-f8e0-11e6-8263-005056b2349c.vmdk
          FSType:     ext3
      No events.
      ```

      __Note: VMDK is created inside ```kubevols``` folder in datastore which is mentioned in 'vsphere' cloudprovider configuration.
      The cloudprovider config is created during setup of Kubernetes cluster on vSphere.__

  3. Create Pod which uses Persistent Volume Claim with storage class.

      See example:

      ```yaml
      apiVersion: v1
      kind: Pod
      metadata:
        name: pvpod
      spec:
        containers:
        - name: test-container
          image: gcr.io/google_containers/test-webserver
          volumeMounts:
          - name: test-volume
            mountPath: /test-vmdk
        volumes:
        - name: test-volume
          persistentVolumeClaim:
            claimName: pvcsc001
      ```

      [Download example](vsphere-volume-pvcscpod.yaml?raw=true)

      Creating the pod:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pvcscpod.yaml
      ```

      Verifying pod is created:

      ``` bash
      $ kubectl get pod pvpod
      NAME      READY     STATUS    RESTARTS   AGE
      pvpod       1/1     Running   0          48m
      ```

### Storage Policy Management inside kubernetes
#### Using existing vCenter SPBM policy
  Admins can use the existing vCenter Storage Policy Based Management (SPBM) policy to configure a persistent volume with the SPBM policy.

  __Note: Here you don't need to create persistent volume it is created for you.__
   1. Create Storage Class.

      Example 1:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1
      metadata:
        name: fast
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: zeroedthick
          storagePolicyName: gold
      ```
      [Download example](vsphere-volume-spbm-policy.yaml?raw=true)

      The admin specifies the SPBM policy - "gold" as part of storage class definition for dynamic volume provisioning. When a PVC is created, the persistent volume will be provisioned on a compatible datastore with maximum free space that satisfies the "gold" storage policy requirements.

      Example 2:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1
      metadata:
        name: fast
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: zeroedthick
          storagePolicyName: gold
          datastore: VSANDatastore
      ```
      [Download example](vsphere-volume-spbm-policy-with-datastore.yaml?raw=true)

      The admin can also specify a custom datastore where he wants the volume to be provisioned along with the SPBM policy name. When a PVC is created, the vSphere Cloud Provider checks if the user specified datastore satisfies the "gold" storage policy requirements. If yes, it will provision the persistent volume on user specified datastore. If not, it will error out to the user that the user specified datastore is not compatible with "gold" storage policy requirements.

#### Virtual SAN policy support

  Vsphere Infrastructure(VI) Admins will have the ability to specify custom Virtual SAN Storage Capabilities during dynamic volume provisioning. You can now define storage requirements, such as performance and availability, in the form of storage capabilities during dynamic volume provisioning. The storage capability requirements are converted into a Virtual SAN policy which are then pushed down to the Virtual SAN layer when a persistent volume (virtual disk) is being created. The virtual disk is distributed across the Virtual SAN datastore to meet the requirements.

  The official [VSAN policy documentation](https://pubs.vmware.com/vsphere-65/index.jsp?topic=%2Fcom.vmware.vsphere.virtualsan.doc%2FGUID-08911FD3-2462-4C1C-AE81-0D4DBC8F7990.html) describes in detail about each of the individual storage capabilities that are supported by VSAN. The user can specify these storage capabilities as part of storage class defintion based on his application needs.

  The policy settings can be one or more of the following:

  * *hostFailuresToTolerate*: represents NumberOfFailuresToTolerate
  * *diskStripes*: represents NumberofDiskStripesPerObject
  * *objectSpaceReservation*: represents ObjectSpaceReservation
  * *cacheReservation*: represents FlashReadCacheReservation
  * *iopsLimit*: represents IOPSLimitForObject
  * *forceProvisioning*: represents if volume must be Force Provisioned

  __Note: Here you don't need to create persistent volume it is created for you.__
  1. Create Storage Class.

      Example 1:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1beta1
      metadata:
        name: fast
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: zeroedthick
          hostFailuresToTolerate: "2"
          cachereservation: "20"
      ```
      [Download example](vsphere-volume-sc-vsancapabilities.yaml?raw=true)

      Here a persistent volume will be created with the Virtual SAN capabilities - hostFailuresToTolerate to 2 and cachereservation is 20% read cache reserved for storage object. Also the persistent volume will be *zeroedthick* disk.
      The official [VSAN policy documentation](https://pubs.vmware.com/vsphere-65/index.jsp?topic=%2Fcom.vmware.vsphere.virtualsan.doc%2FGUID-08911FD3-2462-4C1C-AE81-0D4DBC8F7990.html) describes in detail about each of the individual storage capabilities that are supported by VSAN and can be configured on the virtual disk.

      You can also specify the datastore in the Storageclass as shown in example 2. The volume will be created on the datastore specified in the storage class.
      This field is optional. If not specified as shown in example 1, the volume will be created on the datastore specified in the vsphere config file used to initialize the vSphere Cloud Provider.

      Example 2:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1beta1
      metadata:
        name: fast
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: zeroedthick
          datastore: VSANDatastore
          hostFailuresToTolerate: "2"
          cachereservation: "20"
      ```

      [Download example](vsphere-volume-sc-vsancapabilities-with-datastore.yaml?raw=true)

      __Note: If you do not apply a storage policy during dynamic provisioning on a VSAN datastore, it will use a default Virtual SAN policy.__

      Creating the storageclass:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-sc-vsancapabilities.yaml
      ```

      Verifying storage class is created:

      ``` bash
      $ kubectl describe storageclass fast
      Name:		fast
      Annotations:	<none>
      Provisioner:	kubernetes.io/vsphere-volume
      Parameters:	diskformat=zeroedthick, hostFailuresToTolerate="2", cachereservation="20"
      No events.
      ```

  2. Create Persistent Volume Claim.

      See example:

      ```yaml
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: pvcsc-vsan
        annotations:
          volume.beta.kubernetes.io/storage-class: fast
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 2Gi
      ```

      [Download example](vsphere-volume-pvcsc.yaml?raw=true)

      Creating the persistent volume claim:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pvcsc.yaml
      ```

      Verifying persistent volume claim is created:

      ``` bash
      $ kubectl describe pvc pvcsc-vsan
      Name:		pvcsc-vsan
      Namespace:	default
      Status:		Bound
      Volume:		pvc-80f7b5c1-94b6-11e6-a24f-005056a79d2d
      Labels:		<none>
      Capacity:	2Gi
      Access Modes:	RWO
      No events.
      ```

      Persistent Volume is automatically created and is bounded to this pvc.

      Verifying persistent volume claim is created:

      ``` bash
      $ kubectl describe pv pvc-80f7b5c1-94b6-11e6-a24f-005056a79d2d
      Name:		pvc-80f7b5c1-94b6-11e6-a24f-005056a79d2d
      Labels:		<none>
      Status:		Bound
      Claim:		default/pvcsc-vsan
      Reclaim Policy:	Delete
      Access Modes:	RWO
      Capacity:	2Gi
      Message:
      Source:
          Type:	vSphereVolume (a Persistent Disk resource in vSphere)
          VolumePath:	[VSANDatastore] kubevols/kubernetes-dynamic-pvc-80f7b5c1-94b6-11e6-a24f-005056a79d2d.vmdk
          FSType:	ext4
      No events.
      ```

      __Note: VMDK is created inside ```kubevols``` folder in datastore which is mentioned in 'vsphere' cloudprovider configuration.
      The cloudprovider config is created during setup of Kubernetes cluster on vSphere.__

  3. Create Pod which uses Persistent Volume Claim with storage class.

      See example:

      ```yaml
      apiVersion: v1
      kind: Pod
      metadata:
        name: pvpod
      spec:
        containers:
        - name: test-container
          image: gcr.io/google_containers/test-webserver
          volumeMounts:
          - name: test-volume
            mountPath: /test
        volumes:
        - name: test-volume
          persistentVolumeClaim:
            claimName: pvcsc-vsan
      ```

      [Download example](vsphere-volume-pvcscpod.yaml?raw=true)

      Creating the pod:

      ``` bash
      $ kubectl create -f examples/volumes/vsphere/vsphere-volume-pvcscpod.yaml
      ```

      Verifying pod is created:

      ``` bash
      $ kubectl get pod pvpod
      NAME      READY     STATUS    RESTARTS   AGE
      pvpod       1/1     Running   0          48m
      ```

###  Stateful Set

vSphere volumes can be consumed by Stateful Sets.

  1. Create a storage class that will be used by the ```volumeClaimTemplates``` of a Stateful Set.

      See example:

      ```yaml
      kind: StorageClass
      apiVersion: storage.k8s.io/v1beta1
      metadata:
        name: thin-disk
      provisioner: kubernetes.io/vsphere-volume
      parameters:
          diskformat: thin
      ```

      [Download example](simple-storageclass.yaml)

  2. Create a Stateful set that consumes storage from the Storage Class created.

     See example:
     ```yaml
     ---
     apiVersion: v1
     kind: Service
     metadata:
       name: nginx
       labels:
         app: nginx
     spec:
       ports:
       - port: 80
         name: web
       clusterIP: None
       selector:
         app: nginx
     ---
     apiVersion: apps/v1beta1
     kind: StatefulSet
     metadata:
       name: web
     spec:
       serviceName: "nginx"
       replicas: 14
       template:
         metadata:
           labels:
             app: nginx
         spec:
           containers:
           - name: nginx
             image: gcr.io/google_containers/nginx-slim:0.8
             ports:
             - containerPort: 80
               name: web
             volumeMounts:
             - name: www
               mountPath: /usr/share/nginx/html
       volumeClaimTemplates:
       - metadata:
           name: www
           annotations:
             volume.beta.kubernetes.io/storage-class: thin-disk
         spec:
           accessModes: [ "ReadWriteOnce" ]
           resources:
             requests:
               storage: 1Gi
     ```
     This will create Persistent Volume Claims for each replica and provision a volume for each claim if an existing volume could be bound to the claim.

     [Download example](simple-statefulset.yaml)

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/vsphere/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# How to Use it?

On Azure VM, create a Pod using the volume spec based on [azure](azure.yaml).

In the pod, you need to provide the following information:

- *diskName*:  (required) the name of the VHD blob object.
- *diskURI*: (required) the URI of the vhd blob object.
- *cachingMode*: (optional) disk caching mode. Must be one of None, ReadOnly, or ReadWrite. Default is None.
- *fsType*:  (optional) the filesytem type to mount. Default is ext4.
- *readOnly*: (optional) whether the filesystem is used as readOnly. Default is false.


Launch the Pod:

```console
    # kubectl create -f examples/volumes/azure_disk/azure.yaml
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/azure_disk/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## GlusterFS

[GlusterFS](http://www.gluster.org) is an open source scale-out filesystem. These examples provide information about how to allow containers use GlusterFS volumes.

There are couple of ways to use GlusterFS as a persistent data store in application pods.

*) Static Provisioning of GlusterFS Volumes.
*) Dynamic Provisioning of GlusterFS Volumes.

### Static Provisioning

Static Provisioning of GlusterFS Volumes is analogues to creation of a PV ( Persistent Volume) resource by specifying the parameters in it. This
also need a working GlusterFS cluster/trusted pool available to carve out GlusterFS volumes.

The example assumes that you have already set up a GlusterFS server cluster and have a working GlusterFS volume ready to use in the containers.

#### Prerequisites

* Set up a GlusterFS server cluster
* Create a GlusterFS volume
* If you are not using hyperkube, you may need to install the GlusterFS client package on the Kubernetes nodes ([Guide](http://gluster.readthedocs.io/en/latest/Administrator%20Guide/))

#### Create endpoints

The first step is to create the GlusterFS endpoints definition in Kubernetes. Here is a snippet of [glusterfs-endpoints.json](glusterfs-endpoints.json):

```
  "subsets": [
    {
      "addresses": [{ "ip": "10.240.106.152" }],
      "ports": [{ "port": 1 }]
    },
    {
      "addresses": [{ "ip": "10.240.79.157" }],
      "ports": [{ "port": 1 }]
    }
  ]
```

The `subsets` field should be populated with the addresses of the nodes in the GlusterFS cluster. It is fine to provide any valid value (from 1 to 65535) in the `port` field.

Create the endpoints:

```sh
$ kubectl create -f examples/volumes/glusterfs/glusterfs-endpoints.json
```

You can verify that the endpoints are successfully created by running

```sh
$ kubectl get endpoints
NAME                ENDPOINTS
glusterfs-cluster   10.240.106.152:1,10.240.79.157:1
```

We also need to create a service for these endpoints, so that they will persist. We will add this service without a selector to tell Kubernetes we want to add its endpoints manually. You can see [glusterfs-service.json](glusterfs-service.json) for details.

Use this command to create the service:

```sh
$ kubectl create -f examples/volumes/glusterfs/glusterfs-service.json
```


#### Create a Pod

The following *volume* spec in [glusterfs-pod.json](glusterfs-pod.json) illustrates a sample configuration:

```json
"volumes": [
  {
    "name": "glusterfsvol",
    "glusterfs": {
      "endpoints": "glusterfs-cluster",
      "path": "kube_vol",
      "readOnly": true
    }
  }
]
```

The parameters are explained as the followings.

- **endpoints** is the name of the Endpoints object that represents a Gluster cluster configuration. *kubelet* is optimized to avoid mount storm, it will randomly pick one from the endpoints to mount. If this host is unresponsive, the next Gluster host in the endpoints is automatically selected.
- **path** is the Glusterfs volume name.
- **readOnly** is the boolean that sets the mountpoint readOnly or readWrite.

Create a pod that has a container using Glusterfs volume,

```sh
$ kubectl create -f examples/volumes/glusterfs/glusterfs-pod.json
```

You can verify that the pod is running:

```sh
$ kubectl get pods
NAME             READY     STATUS    RESTARTS   AGE
glusterfs        1/1       Running   0          3m
```

You may execute the command `mount` inside the container to see if the GlusterFS volume is mounted correctly:

```sh
$ kubectl exec glusterfs -- mount | grep gluster
10.240.106.152:kube_vol on /mnt/glusterfs type fuse.glusterfs (rw,relatime,user_id=0,group_id=0,default_permissions,allow_other,max_read=131072)
```

You may also run `docker ps` on the host to see the actual container.

### Dynamic Provisioning of GlusterFS Volumes:

Dynamic Provisioning means provisioning of GlusterFS volumes based on a Storage class. Please refer [this guide](./../../persistent-volume-provisioning/README.md)
.
<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/glusterfs/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
This is a simple web server pod which serves HTML from an Cinder volume.

Create a volume in the same tenant and zone as your node.

Add your volume information in the pod description file cinder-web.yaml then create the pod:

```shell
  $ kubectl create -f examples/volumes/cinder/cinder-web.yaml
```

Add some data to the volume if is empty:

```sh
  $ echo  "Hello World" >& /var/lib/kubelet/plugins/kubernetes.io/cinder/mounts/{Volume ID}/index.html
```

You should now be able to query your web server:

```sh
  $ curl <Pod IP address>
  $ Hello World
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/cinder/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# StorageOS Volume

  - [StorageOS](#storageos)
  - [Prerequisites](#prerequisites)
  - [Examples](#examples)
    - [Pre-provisioned Volumes](#pre-provisioned)
      - [Pod](#pod)
      - [Persistent Volumes](#persistent-volumes)
    - [Dynamic Provisioning](#dynamic-provisioning)
      - [Storage Class](#storage-class)
  - [API Configuration](#api-configuration)

## StorageOS

[StorageOS](https://www.storageos.com) can be used as a storage provider for your Kubernetes cluster.  StorageOS runs as a container within your Kubernetes environment, making local storage accessible from any node within the Kubernetes cluster.  Data can be replicated to protect against node failure.

At its core, StorageOS provides block storage.  You may choose the filesystem type to install to make devices usable from within containers.

## Prerequisites

The StorageOS container must be running on each Kubernetes node that wants to contribute storage or that wants to consume storage.  For more information on how you can run StorageOS, consult the [StorageOS  documentation](https://docs.storageos.com).

## API Configuration

The StorageOS provider has been pre-configured to use the StorageOS API defaults, and no additional configuration is required for testing.  If you have changed the API port, or have removed the default account or changed its password (recommended), you must specify the new settings.  This is done using Kubernetes [Secrets](../../../docs/user-guide/secrets/).

API configuration is set by using Kubernetes secrets.  The configuration secret supports the following parameters:

*  `apiAddress`: The address of the StorageOS API.  This is optional and defaults to `tcp://localhost:5705`, which should be correct if the StorageOS container is running using the default settings. 
*  `apiUsername`: The username to authenticate to the StorageOS API with.
*  `apiPassword`: The password to authenticate to the StorageOS API with.
*  `apiVersion`: Optional, string value defaulting to `1`.  Only set this if requested in StorageOS documentation.

Mutiple credentials can be used by creating different secrets.  

For Persistent Volumes, secrets must be created in the Pod namespace.  Specify the secret name using the `secretName` parameter when attaching existing volumes in Pods or creating new persistent volumes. 

For dynamically provisioned volumes using storage classes, the secret can be created in any namespace.  Note that you would want this to be an admin-controlled namespace with restricted access to users. Specify the secret namespace as parameter `adminSecretNamespace` and name as parameter `adminSecretName` in storage classes.

Example spec:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: storageos-secret
type: "kubernetes.io/storageos"
data:
  apiAddress: dGNwOi8vMTI3LjAuMC4xOjU3MDU=
  apiUsername: c3RvcmFnZW9z
  apiPassword: c3RvcmFnZW9z
```

Values for `apiAddress`, `apiUsername` and `apiPassword` can be generated with:

```bash
$ echo -n "tcp://127.0.0.1:5705" | base64
dGNwOi8vMTI3LjAuMC4xOjU3MDU=
```

Create the secret:

```bash
$ kubectl create -f storageos-secret.yaml
secret "storageos-secret" created
```

Verify the secret:

```bash
$ kubectl describe secret storageos-secret
Name:		storageos-secret
Namespace:	default
Labels:		<none>
Annotations:	<none>

Type:	kubernetes.io/storageos

Data
====
apiAddress:	20 bytes
apiPassword:	8 bytes
apiUsername:	8 bytes

```
## Examples

These examples assume you have a running Kubernetes cluster with the StorageOS container running on each node, and that an API configuration secret called `storageos-secret` has been created in the `default` namespace.

### Pre-provisioned Volumes

#### Pod

Pods can be created that access volumes directly.

1. Create a volume using the StorageOS UI, CLI or API.  Consult the [StorageOS documentation](https://docs.storageos.com) for details.
1. Create a pod that refers to the new volume.  In this case the volume is named `redis-vol01`.

   Example spec:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     labels:
       name: redis
       role: master
     name: test-storageos-redis
   spec:
     containers:
       - name: master
         image: kubernetes/redis:v1
         env:
           - name: MASTER
             value: "true"
         ports:
           - containerPort: 6379
         resources:
           limits:
             cpu: "0.1"
         volumeMounts:
           - mountPath: /redis-master-data
             name: redis-data
     volumes:
       - name: redis-data
         storageos:
           # This volume must already exist within StorageOS
           volumeName: redis-vol01
           # volumeNamespace is optional, and specifies the volume scope within
           # StorageOS.  If no namespace is provided, it will use the namespace
           # of the pod.  Set to `default` or leave blank if you are not using
           # namespaces.
           #volumeNamespace: test-storageos
           # The filesystem type to format the volume with, if required.
           fsType: ext4
           # The secret name for API credentials
           secretName: storageos-secret
   ```

   [Download example](storageos-pod.yaml?raw=true)

   Create the pod:

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-pod.yaml
   ```

   Verify that the pod is running:

   ```bash
   $ kubectl get pods test-storageos-redis
   NAME                   READY     STATUS    RESTARTS   AGE
   test-storageos-redis   1/1       Running   0          30m
   ```

### Persistent Volumes

1. Create a volume using the StorageOS UI, CLI or API.  Consult the [StorageOS documentation](https://docs.storageos.com) for details.
1. Create the persistent volume `redis-vol01`.

   Example spec:

   ```yaml
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: pv0001
   spec:
     capacity:
       storage: 5Gi
     accessModes:
       - ReadWriteOnce
     persistentVolumeReclaimPolicy: Delete
     storageos:
       # This volume must already exist within StorageOS
       volumeName: pv0001
       # volumeNamespace is optional, and specifies the volume scope within
       # StorageOS.  Set to `default` or leave blank if you are not using
       # namespaces.
       #volumeNamespace: default
       # The filesystem type to create on the volume, if required.
       fsType: ext4
       # The secret name for API credentials
       secretName: storageos-secret
   ```

   [Download example](storageos-pv.yaml?raw=true)

   Create the persistent volume:

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-pv.yaml
   ```

   Verify that the pv has been created:

   ```bash
   $ kubectl describe pv pv0001
   Name:           pv0001
   Labels:         <none>
   Annotations:    <none>
   StorageClass:   fast
   Status:         Available
   Claim:
   Reclaim Policy: Delete
   Access Modes:   RWO
   Capacity:       5Gi
   Message:
   Source:
       Type:             StorageOS (a StorageOS Persistent Disk resource)
       VolumeName:       pv0001
       VolumeNamespace:
       FSType:           ext4
       ReadOnly:         false
   Events:               <none>
   ```

1. Create persistent volume claim

   Example spec:

   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: pvc0001
   spec:
     accessModes:
       - ReadWriteOnce
     resources:
       requests:
         storage: 5Gi
     storageClassName: fast
   ```

   [Download example](storageos-pvc.yaml?raw=true)

   Create the persistent volume claim:

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-pvc.yaml
   ```

   Verify that the pvc has been created:

   ```bash
   $ kubectl describe pvc pvc0001
   Name:          pvc0001
   Namespace:     default
   StorageClass:  fast
   Status:        Bound
   Volume:        pv0001
   Labels:        <none>
   Capacity:      5Gi
   Access Modes:  RWO
   No events.
   ```

1. Create pod which uses the persistent volume claim

   Example spec:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     labels:
       name: redis
       role: master
     name: test-storageos-redis-pvc
   spec:
     containers:
       - name: master
         image: kubernetes/redis:v1
         env:
           - name: MASTER
             value: "true"
         ports:
           - containerPort: 6379
         resources:
           limits:
             cpu: "0.1"
         volumeMounts:
           - mountPath: /redis-master-data
             name: redis-data
     volumes:
       - name: redis-data
         persistentVolumeClaim:
           claimName: pvc0001
   ```

   [Download example](storageos-pvcpod.yaml?raw=true)

   Create the pod:

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-pvcpod.yaml
   ```

   Verify that the pod has been created:

   ```bash
   $ kubectl get pods
   NAME                       READY     STATUS    RESTARTS   AGE
   test-storageos-redis-pvc   1/1       Running   0          40s
   ```

### Dynamic Provisioning

Dynamic provisioning can be used to auto-create volumes when needed.  They require a Storage Class, a Persistent Volume Claim, and a Pod.

#### Storage Class

Kubernetes administrators can use storage classes to define different types of storage made available within the cluster.  Each storage class definition specifies a provisioner type and any parameters needed to access it, as well as any other configuration.

StorageOS supports the following storage class parameters:

*  `pool`: The name of the StorageOS distributed capacity pool to provision the volume from.  Uses the `default` pool which is normally present if not specified.
*  `description`: The description to assign to volumes that were created dynamically.  All volume descriptions will be the same for the storage class, but different storage classes can be used to allow descriptions for different use cases.  Defaults to `Kubernetes volume`.
*  `fsType`: The default filesystem type to request.  Note that user-defined rules within StorageOS may override this value.  Defaults to `ext4`.
*  `adminSecretNamespace`: The namespace where the API configuration secret is located. Required if adminSecretName set.
*  `adminSecretName`: The name of the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.

1. Create storage class

   Example spec:

   ```yaml
   kind: StorageClass
   apiVersion: storage.k8s.io/v1
   metadata:
     name: sc-fast
   provisioner: kubernetes.io/storageos
   parameters:
     pool: default
     description: Kubernetes volume
     fsType: ext4
     adminSecretNamespace: default
     adminSecretName: storageos-secret
   ```

   [Download example](storageos-sc.yaml?raw=true)

   Create the storage class:

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-sc.yaml
   ```

   Verify the storage class has been created:

   ```bash
   $ kubectl describe storageclass fast
   Name:           fast
   IsDefaultClass: No
   Annotations:    <none>
   Provisioner:    kubernetes.io/storageos
   Parameters:     description=Kubernetes volume,fsType=ext4,pool=default,secretName=storageos-secret
   No events.
   ```

1. Create persistent volume claim

   Example spec:

   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: fast0001
   spec:
     storageClassName: fast
     accessModes:
       - ReadWriteOnce
     resources:
       requests:
         storage: 5Gi
   ```

   Create the persistent volume claim (pvc):

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-sc-pvc.yaml
   ```

   Verify the pvc has been created:

   ```bash
   $ kubectl describe pvc fast0001
   Name:         fast0001
   Namespace:    default
   StorageClass: fast
   Status:       Bound
   Volume:       pvc-480952e7-f8e0-11e6-af8c-08002736b526
   Labels:       <none>
   Capacity:     5Gi
   Access Modes: RWO
   Events:
     <snip>
   ```

   A new persistent volume will also be created and bound to the pvc:

   ```bash
   $ kubectl describe pv pvc-480952e7-f8e0-11e6-af8c-08002736b526
   Name:            pvc-480952e7-f8e0-11e6-af8c-08002736b526
   Labels:          storageos.driver=filesystem
   StorageClass:    fast
   Status:          Bound
   Claim:           default/fast0001
   Reclaim Policy:  Delete
   Access Modes:    RWO
   Capacity:        5Gi
   Message:
   Source:
       Type:        StorageOS (a StorageOS Persistent Disk resource)
       VolumeName:  pvc-480952e7-f8e0-11e6-af8c-08002736b526
       Namespace:   default
       FSType:      ext4
       ReadOnly:    false
   No events.
   ```

1. Create pod which uses the persistent volume claim

   Example spec:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     labels:
       name: redis
       role: master
     name: test-storageos-redis-sc-pvc
   spec:
     containers:
       - name: master
         image: kubernetes/redis:v1
         env:
           - name: MASTER
             value: "true"
         ports:
           - containerPort: 6379
         resources:
           limits:
             cpu: "0.1"
         volumeMounts:
           - mountPath: /redis-master-data
             name: redis-data
     volumes:
       - name: redis-data
         persistentVolumeClaim:
           claimName: fast0001
   ```

   [Download example](storageos-sc-pvcpod.yaml?raw=true)

   Create the pod:

   ```bash
   $ kubectl create -f examples/volumes/storageos/storageos-sc-pvcpod.yaml
   ```

   Verify that the pod has been created:

   ```bash
   $ kubectl get pods
   NAME                          READY     STATUS    RESTARTS   AGE
   test-storageos-redis-sc-pvc   1/1       Running   0          44s
   ```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/storageos/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# How to Use it?

Install Ceph on the Kubernetes host. For example, on Fedora 21

    # yum -y install ceph

If you don't have a Ceph cluster, you can set up a [containerized Ceph cluster](https://github.com/ceph/ceph-docker/tree/master/examples/kubernetes)

Then get the keyring from the Ceph cluster and copy it to */etc/ceph/keyring*.

Once you have installed Ceph and a Kubernetes cluster, you can create a pod based on my examples [cephfs.yaml](cephfs.yaml)  and [cephfs-with-secret.yaml](cephfs-with-secret.yaml). In the pod yaml, you need to provide the following information.

- *monitors*:  Array of Ceph monitors.
- *path*: Used as the mounted root, rather than the full Ceph tree. If not provided, default */* is used.
- *user*: The RADOS user name. If not provided, default *admin* is used.
- *secretFile*: The path to the keyring file. If not provided, default */etc/ceph/user.secret* is used.
- *secretRef*: Reference to Ceph authentication secrets. If provided, *secret* overrides *secretFile*.
- *readOnly*: Whether the filesystem is used as readOnly.


Here are the commands:

```console
    # kubectl create -f examples/volumes/cephfs/cephfs.yaml

    # create a secret if you want to use Ceph secret instead of secret file
    # kubectl create -f examples/volumes/cephfs/secret/ceph-secret.yaml
	
    # kubectl create -f examples/volumes/cephfs/cephfs-with-secret.yaml
    # kubectl get pods
```

 If you ssh to that machine, you can run `docker ps` to see the actual pod and `docker inspect` to see the volumes used by the container.


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/cephfs/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Step 1. Setting up Fibre Channel Target

On your FC SAN Zone manager, allocate and mask LUNs so Kubernetes hosts can access them.

## Step 2. Creating the Pod with Fibre Channel persistent storage

Once you have installed Fibre Channel initiator and new Kubernetes, you can create a pod based on my example [fc.yaml](fc.yaml). In the pod JSON, you need to provide *targetWWNs* (array of Fibre Channel target's World Wide Names), *lun*, and the type of the filesystem that has been created on the lun, and *readOnly* boolean.

Once your pod is created, run it on the Kubernetes master:

```console
kubectl create -f ./your_new_pod.json
```

Here is my command and output:

```console
# kubectl create -f examples/volumes/fibre_channel/fc.yaml
# kubectl get pods
NAME      READY     STATUS    RESTARTS   AGE
fcpd      2/2       Running   0          10m
```

On the Kubernetes host, I got these in mount output

```console
#mount |grep /var/lib/kubelet/plugins/kubernetes.io
/dev/mapper/360a98000324669436c2b45666c567946 on /var/lib/kubelet/plugins/kubernetes.io/fc/500a0982991b8dc5-lun-2 type ext4 (ro,relatime,seclabel,stripe=16,data=ordered)
/dev/mapper/360a98000324669436c2b45666c567944 on /var/lib/kubelet/plugins/kubernetes.io/fc/500a0982991b8dc5-lun-1 type ext4 (rw,relatime,seclabel,stripe=16,data=ordered)
```

If you ssh to that machine, you can run `docker ps` to see the actual pod.

```console
# docker ps
CONTAINER ID        IMAGE                                  COMMAND             CREATED             STATUS              PORTS               NAMES
090ac457ddc2        kubernetes/pause                       "/pause"            12 minutes ago      Up 12 minutes                           k8s_fcpd-rw.aae720ec_fcpd_default_4024318f-4121-11e5-a294-e839352ddd54_99eb5415   
5e2629cf3e7b        kubernetes/pause                       "/pause"            12 minutes ago      Up 12 minutes                           k8s_fcpd-ro.857720dc_fcpd_default_4024318f-4121-11e5-a294-e839352ddd54_c0175742   
2948683253f7        gcr.io/google_containers/pause:0.8.0   "/pause"            12 minutes ago      Up 12 minutes                           k8s_POD.7be6d81d_fcpd_default_4024318f-4121-11e5-a294-e839352ddd54_8d9dd7bf       
```

## Multipath

To leverage multiple paths for block storage, it is important to perform the
multipath configuration on the host.
If your distribution does not provide `/etc/multipath.conf`, then you can
either use the following minimalistic one:

    defaults {
        find_multipaths yes
        user_friendly_names yes
    }

or create a new one by running:

    $ mpathconf --enable

Finally you'll need to ensure to start or reload and enable multipath:

    $ systemctl enable multipathd.service
    $ systemctl restart multipathd.service

**Note:** Any change to `multipath.conf` or enabling multipath can lead to
inaccessible block devices, because they'll be claimed by multipath and
exposed as a device in /dev/mapper/*.

Some additional informations about multipath can be found in the
[iSCSI documentation](../iscsi/README.md)


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/volumes/fibre_channel/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
Please refer to https://github.com/kubernetes/community/tree/master/contributors/devel/flexvolume.md for documentation.# Sharing Clusters

This example demonstrates how to access one kubernetes cluster from another. It only works if both clusters are running on the same network, on a cloud provider that provides a private ip range per network (eg: GCE, GKE, AWS).

## Setup

Create a cluster in US (you don't need to do this if you already have a running kubernetes cluster)

```shell
$ cluster/kube-up.sh
```

Before creating our second cluster, lets have a look at the kubectl config:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: REDACTED
    server: https://104.197.84.16
  name: <clustername_us>
...
current-context: <clustername_us>
...
```

Now spin up the second cluster in Europe

```shell
$ ./cluster/kube-up.sh
$ KUBE_GCE_ZONE=europe-west1-b KUBE_GCE_INSTANCE_PREFIX=eu ./cluster/kube-up.sh
```

Your kubectl config should contain both clusters:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: REDACTED
    server: https://146.148.25.221
  name: <clustername_eu>
- cluster:
    certificate-authority-data: REDACTED
    server: https://104.197.84.16
  name: <clustername_us>
...
current-context: kubernetesdev_eu
...
```

And kubectl get nodes should agree:

```
$ kubectl get nodes
NAME             LABELS                                  STATUS
eu-node-0n61     kubernetes.io/hostname=eu-node-0n61     Ready
eu-node-79ua     kubernetes.io/hostname=eu-node-79ua     Ready
eu-node-7wz7     kubernetes.io/hostname=eu-node-7wz7     Ready
eu-node-loh2     kubernetes.io/hostname=eu-node-loh2     Ready

$ kubectl config use-context <clustername_us>
$ kubectl get nodes
NAME                     LABELS                                                            STATUS
kubernetes-node-5jtd     kubernetes.io/hostname=kubernetes-node-5jtd                       Ready
kubernetes-node-lqfc     kubernetes.io/hostname=kubernetes-node-lqfc                       Ready
kubernetes-node-sjra     kubernetes.io/hostname=kubernetes-node-sjra                       Ready
kubernetes-node-wul8     kubernetes.io/hostname=kubernetes-node-wul8                       Ready
```

## Testing reachability

For this test to work we'll need to create a service in europe:

```
$ kubectl config use-context <clustername_eu>
$ kubectl create -f /tmp/secret.json
$ kubectl create -f examples/https-nginx/nginx-app.yaml
$ kubectl exec -it my-nginx-luiln -- echo "Europe nginx" >> /usr/share/nginx/html/index.html
$ kubectl get ep
NAME         ENDPOINTS
kubernetes   10.240.249.92:443
nginxsvc     10.244.0.4:80,10.244.0.4:443
```

Just to test reachability, we'll try hitting the Europe nginx from our initial US central cluster. Create a basic curl pod in the US cluster:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: curlpod
spec:
  containers:
  - image: radial/busyboxplus:curl
    command:
      - sleep
      - "360000000"
    imagePullPolicy: IfNotPresent
    name: curlcontainer
  restartPolicy: Always
```

And test that you can actually reach the test nginx service across continents

```
$ kubectl config use-context <clustername_us>
$ kubectl -it exec curlpod -- /bin/sh
[ root@curlpod:/ ]$ curl http://10.244.0.4:80
Europe nginx
```

## Granting access to the remote cluster

We will grant the US cluster access to the Europe cluster. Basically we're going to setup a secret that allows kubectl to function in a pod running in the US cluster, just like it did on our local machine in the previous step. First create a secret with the contents of the current .kube/config:

```shell
$ kubectl config use-context <clustername_eu>
$ go run ./make_secret.go --kubeconfig=$HOME/.kube/config > /tmp/secret.json
$ kubectl config use-context <clustername_us>
$ kubectl create -f /tmp/secret.json
```

Create a kubectl pod that uses the secret, in the US cluster.

```json
{
  "kind": "Pod",
  "apiVersion": "v1",
  "metadata": {
    "name": "kubectl-tester"
  },
  "spec": {
    "volumes": [
       {
            "name": "secret-volume",
            "secret": {
                "secretName": "kubeconfig"
            }
        }
    ],
    "containers": [
      {
        "name": "kubectl",
        "image": "bprashanth/kubectl:0.0",
        "imagePullPolicy": "Always",
        "env": [
            {
                "name": "KUBECONFIG",
                "value": "/.kube/config"
            }
        ],
        "args": [
          "proxy", "-p", "8001"
        ],
        "volumeMounts": [
          {
              "name": "secret-volume",
               "mountPath": "/.kube"
          }
        ]
      }
    ]
  }
}
```

And check that you can access the remote cluster

```shell
$ kubectl config use-context <clustername_us>
$ kubectl exec -it kubectl-tester bash

kubectl-tester $ kubectl get nodes
NAME             LABELS                                  STATUS
eu-node-0n61     kubernetes.io/hostname=eu-node-0n61     Ready
eu-node-79ua     kubernetes.io/hostname=eu-node-79ua     Ready
eu-node-7wz7     kubernetes.io/hostname=eu-node-7wz7     Ready
eu-node-loh2     kubernetes.io/hostname=eu-node-loh2     Ready
```

For a more advanced example of sharing clusters, see the [service-loadbalancer](https://github.com/kubernetes/contrib/tree/master/service-loadbalancer/README.md)


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/sharing-clusters/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## New Relic Server Monitoring Agent Example

This example shows how to run a New Relic server monitoring agent as a pod in a DaemonSet on an existing Kubernetes cluster.

This example will create a DaemonSet which places the New Relic monitoring agent on every node in the cluster. It's also fairly trivial to exclude specific Kubernetes nodes from the DaemonSet to just monitor specific servers.

### Step 0: Prerequisites

This process will create privileged containers which have full access to the host system for logging. Beware of the security implications of this.

If you are using a Salt based KUBERNETES\_PROVIDER (**gce**, **vagrant**, **aws**), you should make sure the creation of privileged containers via the API is enabled. Check `cluster/saltbase/pillar/privilege.sls`.

DaemonSets must be enabled on your cluster. Instructions for enabling DaemonSet can be found [here](https://kubernetes.io/docs/api.md#enabling-the-extensions-group).

### Step 1: Configure New Relic Agent

The New Relic agent is configured via environment variables. We will configure these environment variables in a sourced bash script, encode the environment file data, and store it in a secret which will be loaded at container runtime.

The [New Relic Linux Server configuration page]
(https://docs.newrelic.com/docs/servers/new-relic-servers-linux/installation-configuration/configuring-servers-linux) lists all the other settings for nrsysmond.

To create an environment variable for a setting, prepend NRSYSMOND_ to its name. For example,

```console
loglevel=debug
```

translates to

```console
NRSYSMOND_loglevel=debug
```

Edit examples/newrelic/nrconfig.env and set up the environment variables for your NewRelic agent. Be sure to edit the license key field and fill in your own New Relic license key.

Now, let's vendor the config into a secret.

```console
$ cd examples/newrelic/
$ ./config-to-secret.sh
```

<!-- BEGIN MUNGE: EXAMPLE newrelic-config-template.yaml -->

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: newrelic-config
type: Opaque
data:
  config: {{config_data}}
```

[Download example](newrelic-config-template.yaml?raw=true)
<!-- END MUNGE: EXAMPLE newrelic-config-template.yaml -->

The script will encode the config file and write it to `newrelic-config.yaml`.

Finally, submit the config to the cluster:

```console
$ kubectl create -f examples/newrelic/newrelic-config.yaml
```

### Step 2: Create the DaemonSet definition.

The DaemonSet definition instructs Kubernetes to place a newrelic sysmond agent on each Kubernetes node.

<!-- BEGIN MUNGE: EXAMPLE newrelic-daemonset.yaml -->

```yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: newrelic-agent
  labels:
    tier: monitoring
    app: newrelic-agent
    version: v1
spec:
  template:
    metadata:
      labels:
        name: newrelic
    spec:
      # Filter to specific nodes:
      # nodeSelector:
      #  app: newrelic
      hostPID: true
      hostIPC: true
      hostNetwork: true
      containers:
        - resources:
            requests:
              cpu: 0.15
          securityContext:
            privileged: true
          env:
            - name: NRSYSMOND_logfile
              value: "/var/log/nrsysmond.log"
          image: newrelic/nrsysmond
          name: newrelic
          command: [ "bash", "-c", "source /etc/kube-newrelic/config && /usr/sbin/nrsysmond -E -F" ]
          volumeMounts:
            - name: newrelic-config
              mountPath: /etc/kube-newrelic
              readOnly: true
            - name: dev
              mountPath: /dev
            - name: run
              mountPath: /var/run/docker.sock
            - name: sys
              mountPath: /sys
            - name: log
              mountPath: /var/log
      volumes:
        - name: newrelic-config
          secret:
            secretName: newrelic-config
        - name: dev
          hostPath:
              path: /dev
        - name: run
          hostPath:
              path: /var/run/docker.sock
        - name: sys
          hostPath:
              path: /sys
        - name: log
          hostPath:
              path: /var/log
```

[Download example](newrelic-daemonset.yaml?raw=true)
<!-- END MUNGE: EXAMPLE newrelic-daemonset.yaml -->

The daemonset instructs Kubernetes to spawn pods on each node, mapping /dev/, /run/, /sys/, and /var/log to the container. It also maps the secrets we set up earlier to /etc/kube-newrelic/config, and sources them in the startup script, configuring the agent properly.

#### DaemonSet customization

- To include a custom hostname prefix (or other per-container environment variables that can be generated at run-time), you can modify the DaemonSet `command` value:

```
command: [ "bash", "-c", "source /etc/kube-newrelic/config && export NRSYSMOND_hostname=mycluster-$(hostname) && /usr/sbin/nrsysmond -E -F" ]
```

When the New Relic agent starts, `NRSYSMOND_hostname` is set using the output of `hostname` with `mycluster` prepended.


### Known issues

It's a bit cludgy to define the environment variables like we do here in these config files. There is [another issue](https://github.com/kubernetes/kubernetes/issues/4710) to discuss adding mapping secrets to environment variables in Kubernetes.

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/newrelic/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## PSP RBAC Example

This example demonstrates the usage of *PodSecurityPolicy* to control access to privileged containers
based on role and groups.

### Prerequisites

The server must be started to enable the appropriate APIs and flags

1.  allow privileged containers
1.  allow security contexts
1.  enable RBAC and accept any token
1.  enable PodSecurityPolicies
1.  use the PodSecurityPolicy admission controller

If you are using the `local-up-cluster.sh` script you may enable these settings with the following syntax

```
PSP_ADMISSION=true ALLOW_PRIVILEGED=true ALLOW_SECURITY_CONTEXT=true ALLOW_ANY_TOKEN=true ENABLE_RBAC=true RUNTIME_CONFIG="extensions/v1beta1=true,extensions/v1beta1/podsecuritypolicy=true" hack/local-up-cluster.sh
```

### Using the protected port

It is important to note that this example uses the following syntax to test with RBAC

1.  `--server=https://127.0.0.1:6443`: when performing requests this ensures that the protected port is used so
that RBAC will be enforced
1.  `--token={user}/{group(s)}`: this syntax allows a request to specify the username and groups to use for
testing.  It relies on the `ALLOW_ANY_TOKEN` setting.

## Creating the policies, roles, and bindings

### Policies

The first step to enforcing cluster constraints via PSP is to create your policies.  In this
example we will use two policies, `restricted` and `privileged`.  For simplicity, the only difference
between these policies is the ability to run a privileged container.

```yaml
apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
  name: privileged
spec:
  fsGroup:
    rule: RunAsAny
  privileged: true
  runAsUser:
    rule: RunAsAny
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  volumes:
  - '*'
---
apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  fsGroup:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  volumes:
  - '*'

```

To create these policies run

```
$ kubectl --server=https://127.0.0.1:6443 --token=foo/system:masters create -f examples/podsecuritypolicy/rbac/policies.yaml 
podsecuritypolicy "privileged" created
podsecuritypolicy "restricted" created
```

### Roles and bindings

In order to create a pod, either the creating user or the service account
specified by the pod must be authorized to use a `PodSecurityPolicy` object
that allows the pod. That authorization is determined by the ability to perform
the `use` verb on a particular `podsecuritypolicies` resource. The `use` verb
is a special verb that grants access to use a policy while not permitting any
other access. For this example, we'll first create RBAC `ClusterRoles` that
enable access to `use` specific policies.

1. `restricted-psp-user`: this role allows the `use` verb on the `restricted` policy only
2. `privileged-psp-user`: this role allows the `use` verb on the `privileged` policy only


We can then create `ClusterRoleBindings` to grant groups of users the
"restricted" and/or "privileged" `ClusterRoles`.  In this example, the bindings
grant the following roles to groups.

1. `privileged`: this group is bound to the `privilegedPSP` role and `restrictedPSP` role which gives users
in this group access to both policies.
1. `restricted`: this group is bound to the `restrictedPSP` role.
1. `system:authenticated`: this is a system group for any authenticated user.  It is bound to the `edit`
role which is already provided by the cluster.

To create these roles and bindings run

```
$ kubectl --server=https://127.0.0.1:6443 --token=foo/system:masters create -f examples/podsecuritypolicy/rbac/roles.yaml 
clusterrole "restricted-psp-user" created
clusterrole "privileged-psp-user" created

$ kubectl --server=https://127.0.0.1:6443 --token=foo/system:masters create -f examples/podsecuritypolicy/rbac/bindings.yaml 
clusterrolebinding "privileged-psp-users" created
clusterrolebinding "restricted-psp-users" created
clusterrolebinding "edit" created
```

## Testing access

### Restricted user can create non-privileged pods

Create the pod

```
$ kubectl --server=https://127.0.0.1:6443 --token=foo/restricted-psp-users create -f examples/podsecuritypolicy/rbac/pod.yaml 
pod "nginx" created
```

Check the PSP that allowed the pod

```
$ kubectl get pod nginx -o yaml | grep psp
    kubernetes.io/psp: restricted
```

### Restricted user cannot create privileged pods

Delete the existing pod

```
$ kubectl delete pod nginx
pod "nginx" deleted
```

Create the privileged pod

```
$ kubectl --server=https://127.0.0.1:6443 --token=foo/restricted-psp-users create -f examples/podsecuritypolicy/rbac/pod_priv.yaml 
Error from server (Forbidden): error when creating "examples/podsecuritypolicy/rbac/pod_priv.yaml": pods "nginx" is forbidden: unable to validate against any pod security policy: [spec.containers[0].securityContext.privileged: Invalid value: true: Privileged containers are not allowed]
```

### Privileged user can create non-privileged pods

```
$ kubectl --server=https://127.0.0.1:6443 --token=foo/privileged-psp-users create -f examples/podsecuritypolicy/rbac/pod.yaml 
pod "nginx" created
```

Check the PSP that allowed the pod.  Note, this could be the `restricted` or `privileged` PSP since both allow
for the creation of non-privileged pods.

```
$ kubectl get pod nginx -o yaml | egrep "psp|privileged"
    kubernetes.io/psp: privileged
      privileged: false
```

### Privileged user can create privileged pods

Delete the existing pod

```
$ kubectl delete pod nginx
pod "nginx" deleted
```

Create the privileged pod

```
$ kubectl --server=https://127.0.0.1:6443 --token=foo/privileged-psp-users create -f examples/podsecuritypolicy/rbac/pod_priv.yaml 
pod "nginx" created
```

Check the PSP that allowed the pod.

```
$ kubectl get pod nginx -o yaml | egrep "psp|privileged"
    kubernetes.io/psp: privileged
      privileged: true
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/podsecuritypolicy/rbac/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## OpenShift Origin example

This example shows how to run OpenShift Origin as a pod on an existing Kubernetes cluster.

OpenShift Origin runs with a rich set of role based policy rules out of the box that requires authentication from users via certificates.  When run as a pod on an existing Kubernetes cluster, it proxies access to the underlying Kubernetes services to provide security.

As a result, this example is a complex end-to-end configuration that shows how to configure certificates for a service that runs on Kubernetes, and requires a number of configuration files to be injected dynamically via a secret volume to the pod.

This example will create a pod running the OpenShift Origin master. In addition, it will run a three-pod etcd setup to hold OpenShift content. OpenShift embeds Kubernetes in the stand-alone setup, so the configuration for OpenShift when it is running against an external Kubernetes cluster is different: content specific to Kubernetes will be stored in the Kubernetes etcd repository (i.e. pods, services, replication controllers, etc.), but OpenShift specific content (builds, images, users, policies, etc.) are stored in its etcd setup.

### Step 0: Prerequisites

This example assumes that you have an understanding of Kubernetes and that you have forked the repository.

OpenShift Origin creates privileged containers when running Docker builds during the source-to-image process.

If you are using a Salt based KUBERNETES_PROVIDER (**gce**, **vagrant**, **aws**), you should enable the
ability to create privileged containers via the API.

```sh
$ cd kubernetes
$ vi cluster/saltbase/pillar/privilege.sls

# If true, allow privileged containers to be created by API
allow_privileged: true
```

Now spin up a cluster using your preferred KUBERNETES_PROVIDER. Remember that `kube-up.sh` may start other pods on your nodes, so ensure that you have enough resources to run the five pods for this example.


```sh
$ export KUBERNETES_PROVIDER=${YOUR_PROVIDER}
$ cluster/kube-up.sh
```

Next, let's setup some variables, and create a local folder that will hold generated configuration files.

```sh
$ export OPENSHIFT_EXAMPLE=$(pwd)/examples/openshift-origin
$ export OPENSHIFT_CONFIG=${OPENSHIFT_EXAMPLE}/config
$ mkdir ${OPENSHIFT_CONFIG}

$ export ETCD_INITIAL_CLUSTER_TOKEN=$(python -c "import string; import random; print(''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(40)))")
$ export ETCD_DISCOVERY_TOKEN=$(python -c "import string; import random; print(\"etcd-cluster-\" + ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(5)))")
$ sed -i.bak -e "s/INSERT_ETCD_INITIAL_CLUSTER_TOKEN/\"${ETCD_INITIAL_CLUSTER_TOKEN}\"/g" -e "s/INSERT_ETCD_DISCOVERY_TOKEN/\"${ETCD_DISCOVERY_TOKEN}\"/g" ${OPENSHIFT_EXAMPLE}/etcd-controller.yaml
```

This will have created a `etcd-controller.yaml.bak` file in your directory, which you should remember to restore when doing cleanup (or use the given `cleanup.sh`). Finally, let's start up the external etcd pods and the discovery service necessary for their initialization:

```sh
$ kubectl create -f examples/openshift-origin/openshift-origin-namespace.yaml
$ kubectl create -f examples/openshift-origin/etcd-discovery-controller.yaml --namespace="openshift-origin"
$ kubectl create -f examples/openshift-origin/etcd-discovery-service.yaml --namespace="openshift-origin"
$ kubectl create -f examples/openshift-origin/etcd-controller.yaml --namespace="openshift-origin"
$ kubectl create -f examples/openshift-origin/etcd-service.yaml --namespace="openshift-origin"
```

### Step 1: Export your Kubernetes configuration file for use by OpenShift pod

OpenShift Origin uses a configuration file to know how to access your Kubernetes cluster with administrative authority.

```
$ cluster/kubectl.sh config view --output=yaml --flatten=true --minify=true > ${OPENSHIFT_CONFIG}/kubeconfig
```

The output from this command will contain a single file that has all the required information needed to connect to your Kubernetes cluster that you previously provisioned. This file should be considered sensitive, so do not share this file with untrusted parties.

We will later use this file to tell OpenShift how to bootstrap its own configuration.

### Step 2: Create an External Load Balancer to Route Traffic to OpenShift

An external load balancer is needed to route traffic to our OpenShift master service that will run as a pod on your Kubernetes cluster.


```sh
$ cluster/kubectl.sh create -f $OPENSHIFT_EXAMPLE/openshift-service.yaml --namespace="openshift-origin"
```

### Step 3: Generate configuration file for your OpenShift master pod

The OpenShift master requires a configuration file as input to know how to bootstrap the system.

In order to build this configuration file, we need to know the public IP address of our external load balancer in order to build default certificates.

Grab the public IP address of the service we previously created: the two-line script below will attempt to do so, but make sure to check that the IP was set as a result - if it was not, try again after a couple seconds.


```sh
$  export PUBLIC_OPENSHIFT_IP=$(kubectl get services openshift  --namespace="openshift-origin" --template="{{ index .status.loadBalancer.ingress 0 \"ip\" }}")
$  echo ${PUBLIC_OPENSHIFT_IP}
```

You can automate the process with the following script, as it might take more than a minute for the IP to be set and discoverable.

```shell
$ while [ ${#PUBLIC_OPENSHIFT_IP} -lt 1 ]; do
  	echo -n .
  	sleep 1
  	{
	  	export PUBLIC_OPENSHIFT_IP=$(kubectl get services openshift  --namespace="openshift-origin" --template="{{ index .status.loadBalancer.ingress 0 \"ip\" }}")
	  } 2> ${OPENSHIFT_EXAMPLE}/openshift-startup.log
	  if [[ ! ${PUBLIC_OPENSHIFT_IP} =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
		  export PUBLIC_OPENSHIFT_IP=""
  	fi
  done
$ echo
$ echo "Public OpenShift IP set to: ${PUBLIC_OPENSHIFT_IP}"
```

Ensure you have a valid PUBLIC_IP address before continuing in the example.

We now need to run a command on your host to generate a proper OpenShift configuration.  To do this, we will volume mount the configuration directory that holds your Kubernetes kubeconfig file from the prior step.


```sh
$ docker run --privileged -v ${OPENSHIFT_CONFIG}:/config openshift/origin start master --write-config=/config --kubeconfig=/config/kubeconfig --master=https://localhost:8443 --public-master=https://${PUBLIC_OPENSHIFT_IP}:8443 --etcd=http://etcd:2379
```

You should now see a number of certificates minted in your configuration directory, as well as a master-config.yaml file that tells the OpenShift master how to execute.  We need to make some adjustments to this configuration directory in order to allow the OpenShift cluster to use Kubernetes serviceaccounts. First, write the Kubernetes service account key to the `${OPENSHIFT_CONFIG}` directory. The following script assumes you are using GCE. If you are not, use `scp` or `ssh` to get the key from the master node running Kubernetes. It is usually located at `/srv/kubernetes/server.key`.

```shell
$ export ZONE=$(gcloud compute instances list | grep "${KUBE_GCE_INSTANCE_PREFIX}\-master" | awk '{print $2}' | head -1)
$ echo "sudo cat /srv/kubernetes/server.key; exit;" | gcloud compute ssh ${KUBE_GCE_INSTANCE_PREFIX}-master --zone ${ZONE} | grep -Ex "(^\-.*\-$|^\S+$)" > ${OPENSHIFT_CONFIG}/serviceaccounts.private.key

```

Although we are retrieving the private key from the Kubernetes master, OpenShift will take care of the conversion for us so that serviceaccounts are created with the public key. Edit your `master-config.yaml` file in the `${OPENSHIFT_CONFIG}` directory to add `serviceaccounts.private.key` to the list of `publicKeyFiles`:

```shell
$ sed -i -e 's/publicKeyFiles:.*$/publicKeyFiles:/g' -e '/publicKeyFiles:/a \ \ - serviceaccounts.private.key' ${OPENSHIFT_CONFIG}/master-config.yaml
```

Now, the configuration files are complete. In the next step, we will bundle the resulting configuration into a Kubernetes Secret that our OpenShift master pod will consume.

### Step 4: Bundle the configuration into a Secret

We now need to bundle the contents of our configuration into a secret for use by our OpenShift master pod.

OpenShift includes an experimental command to make this easier.

First, update the ownership for the files previously generated:

```
$ sudo -E chown -R ${USER} ${OPENSHIFT_CONFIG}
```

Then run the following command to collapse them into a Kubernetes secret.

```sh
$ docker run -it --privileged -e="KUBECONFIG=/config/admin.kubeconfig" -v ${OPENSHIFT_CONFIG}:/config openshift/origin cli secrets new openshift-config /config -o json &> examples/openshift-origin/secret.json
```

Now, lets create the secret in your Kubernetes cluster.

```sh
$ cluster/kubectl.sh create -f examples/openshift-origin/secret.json --namespace="openshift-origin"
```

**NOTE: This secret is secret and should not be shared with untrusted parties.**

### Step 5: Deploy OpenShift Master

We are now ready to deploy OpenShift.

We will deploy a pod that runs the OpenShift master.  The OpenShift master will delegate to the underlying Kubernetes
system to manage Kubernetes specific resources.  For the sake of simplicity, the OpenShift master will run with an embedded etcd to hold OpenShift specific content.  This demonstration will evolve in the future to show how to run etcd in a pod so that content is not destroyed if the OpenShift master fails.

```sh
$  cluster/kubectl.sh create -f ${OPENSHIFT_EXAMPLE}/openshift-controller.yaml --namespace="openshift-origin"
```

You should now get a pod provisioned whose name begins with openshift.

```sh
$ cluster/kubectl.sh get pods | grep openshift
$ cluster/kubectl.sh log openshift-t7147 origin
Running: cluster/../cluster/gce/../../cluster/../_output/dockerized/bin/linux/amd64/kubectl logs openshift-t7t47 origin
2015-04-30T15:26:00.454146869Z I0430 15:26:00.454005       1 start_master.go:296] Starting an OpenShift master, reachable at 0.0.0.0:8443 (etcd: [https://10.0.27.2:4001])
2015-04-30T15:26:00.454231211Z I0430 15:26:00.454223       1 start_master.go:297] OpenShift master public address is https://104.197.73.241:8443
```

Depending upon your cloud provider, you may need to open up an external firewall rule for tcp:8443.  For GCE, you can run the following:

```sh
$ gcloud compute --project "your-project" firewall-rules create "origin" --allow tcp:8443 --network "your-network" --source-ranges "0.0.0.0/0"
```

Consult your cloud provider's documentation for more information.

Open a browser and visit the OpenShift master public address reported in your log.

You can use the CLI commands by running the following:

```sh
$ docker run --privileged --entrypoint="/usr/bin/bash" -it -e="OPENSHIFTCONFIG=/config/admin.kubeconfig" -v ${OPENSHIFT_CONFIG}:/config openshift/origin
$ osc config use-context public-default
$ osc --help
```

## Cleanup

Clean up your cluster from resources created with this example:

```sh
$ ${OPENSHIFT_EXAMPLE}/cleanup.sh
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/openshift-origin/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# MySQL installation with cinder volume plugin

Cinder is a Block Storage service for OpenStack. This example shows how it can be used as an attachment mounted to a pod in Kubernets.

### Prerequisites

Start kubelet with cloud provider as openstack with a valid cloud config
Sample cloud_config:

```
[Global]
auth-url=https://os-identity.vip.foo.bar.com:5443/v2.0
username=user
password=pass
region=region1
tenant-id=0c331a1df18571594d49fe68asa4e
```

Currently the cinder volume plugin is designed to work only on linux hosts and offers ext4 and ext3 as supported fs types
Make sure that kubelet host machine has the following executables

```
/bin/lsblk -- To Find out the fstype of the volume
/sbin/mkfs.ext3 and /sbin/mkfs.ext4 -- To format the volume if required
/usr/bin/udevadm -- To probe the volume attached so that a symlink is created under /dev/disk/by-id/ with a virtio- prefix
```

Ensure cinder is installed and configured properly in the region in which kubelet is spun up

### Example

Create a cinder volume Ex:

`cinder create --display-name=test-repo 2`

Use the id of the cinder volume created to create a pod [definition](mysql.yaml)
Create a new pod with the definition

`cluster/kubectl.sh create -f examples/mysql-cinder-pd/mysql.yaml`

This should now

1. Attach the specified volume to the kubelet's host machine
2. Format the volume if required (only if the volume specified is not already formatted to the fstype specified)
3. Mount it on the kubelet's host machine
4. Spin up a container with this volume mounted to the path specified in the pod definition


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/mysql-cinder-pd/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Java Web Application with Tomcat and Sidecar Container

The following document describes the deployment of a Java Web application using Tomcat. Instead of packaging `war` file inside the Tomcat image or mount the `war` as a volume, we use a sidecar container as `war` file provider.

### Prerequisites

https://github.com/kubernetes/kubernetes/blob/master/docs/user-guide/prereqs.md

### Overview

This sidecar mode brings a new workflow for Java users:

![](workflow.png?raw=true "Workflow")

As you can see, user can create a `sample:v2` container as sidecar to "provide" war file to Tomcat by copying it to the shared `emptyDir` volume. And Pod will make sure the two containers compose an "atomic" scheduling unit, which is perfect for this case. Thus, your application version management will be totally separated from web server management.

For example, if you are going to change the configurations of your Tomcat:

```console
$ docker exec -it <tomcat_container_id> /bin/bash
# make some change, and then commit it to a new image
$ docker commit <tomcat_container_id> mytomcat:7.0-dev
```

Done! The new Tomcat image **will not** mess up with your `sample.war` file. You can re-use your tomcat image with lots of different war container images for lots of different apps without having to build lots of different images.

Also this means that rolling out a new Tomcat to patch security or whatever else, doesn't require rebuilding N different images.

**Why not put my `sample.war` in a host dir and mount it to tomcat container?**

You have to **manage the volumes** in this case, for example, when you restart or scale the pod on another node, your contents is not ready on that host.

Generally, we have to set up a distributed file system (NFS at least) volume to solve this (if we do not have GCE PD volume). But this is generally unnecessary.

### How To Set this Up

In Kubernetes a [_Pod_](https://kubernetes.io/docs/user-guide/pods.md) is the smallest deployable unit that can be created, scheduled, and managed. It's a collocated group of containers that share an IP and storage volume.

Here is the config [javaweb.yaml](javaweb.yaml) for Java Web pod:

NOTE: you should define `war` container **first** as it is the "provider".

<!-- BEGIN MUNGE: javaweb.yaml -->

```
apiVersion: v1
kind: Pod
metadata:
  name: javaweb
spec:
  containers:
  - image: resouer/sample:v1
    name: war
    volumeMounts:
    - mountPath: /app
      name: app-volume
  - image: resouer/mytomcat:7.0
    name: tomcat
    command: ["sh","-c","/root/apache-tomcat-7.0.42-v2/bin/start.sh"]
    volumeMounts:
    - mountPath: /root/apache-tomcat-7.0.42-v2/webapps
      name: app-volume
    ports:
    - containerPort: 8080
      hostPort: 8001
  volumes:
  - name: app-volume
    emptyDir: {}
```

<!-- END MUNGE: EXAMPLE -->

The only magic here is the `resouer/sample:v1` image:

```
FROM busybox:latest
ADD sample.war sample.war
CMD "sh" "mv.sh"
```

And the contents of `mv.sh` is:

```sh
cp /sample.war /app
tail -f /dev/null
```

#### Explanation

1. 'war' container only contains the `war` file of your app
2. 'war' container's CMD tries to copy `sample.war` to the `emptyDir` volume path
3. The last line of `tail -f` is just used to hold the container, as Replication Controller does not support one-off task
4. 'tomcat' container will load the `sample.war` from volume path

What's more, if you don't want to enclose a build-in `mv.sh` script in the `war` container, you can use Pod lifecycle handler to do the copy work, here's a example [javaweb-2.yaml](javaweb-2.yaml):


<!-- BEGIN MUNGE: javaweb-2.yaml -->

```
apiVersion: v1
kind: Pod
metadata:
  name: javaweb-2
spec:
  containers:
  - image: resouer/sample:v2
    name: war
    lifecycle:
      postStart:
        exec:
          command:
            - "cp"
            - "/sample.war"
            - "/app"
    volumeMounts:
    - mountPath: /app
      name: app-volume
  - image: resouer/mytomcat:7.0
    name: tomcat
    command: ["sh","-c","/root/apache-tomcat-7.0.42-v2/bin/start.sh"]
    volumeMounts:
    - mountPath: /root/apache-tomcat-7.0.42-v2/webapps
      name: app-volume
    ports:
    - containerPort: 8080
      hostPort: 8001 
  volumes:
  - name: app-volume
    emptyDir: {}
```

<!-- END MUNGE: EXAMPLE -->

And the `resouer/sample:v2` Dockerfile is quite simple:

```
FROM busybox:latest
ADD sample.war sample.war
CMD "tail" "-f" "/dev/null"
```

#### Explanation

1. 'war' container only contains the `war` file of your app
2. 'war' container's CMD uses `tail -f` to hold the container, nothing more
3. The `postStart` lifecycle handler will do `cp` after the `war` container is started
4. Again 'tomcat' container will load the `sample.war` from volume path

Done! Now your `war` container contains nothing except `sample.war`, clean enough.

### Test It Out

Create the Java web pod:

```console
$ kubectl create -f examples/javaweb-tomcat-sidecar/javaweb-2.yaml
```

Check status of the pod:

```console
$ kubectl get -w po
NAME        READY     STATUS    RESTARTS   AGE
javaweb-2   2/2       Running   0         7s
```

Wait for the status to `2/2` and `Running`. Then you can visit "Hello, World" page on `http://localhost:8001/sample/index.html`

You can also test `javaweb.yaml` in the same way.

### Delete Resources

All resources created in this application can be deleted:

```console
$ kubectl delete -f examples/javaweb-tomcat-sidecar/javaweb-2.yaml
```




<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/javaweb-tomcat-sidecar/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
[Sysdig Cloud](http://www.sysdig.com/) is a monitoring, alerting, and troubleshooting platform designed to natively support containerized and service-oriented applications.

Sysdig Cloud comes with built-in, first class support for Kubernetes. In order to instrument your Kubernetes environment with Sysdig Cloud, you simply need to install the Sysdig Cloud agent container on each underlying host in your Kubernetes cluster. Sysdig Cloud will automatically begin monitoring all of your hosts, apps, pods, and services, and will also automatically connect to the Kubernetes API to pull relevant metadata about your environment.

# Example Installation Files

Provided here are two example sysdig.yaml files that can be used to automatically deploy the Sysdig Cloud agent container across a Kubernetes cluster.

The recommended method is using daemon sets - minimum kubernetes version 1.1.1.

If daemon sets are not available, then the replication controller method can be used (based on [this hack](https://stackoverflow.com/questions/33377054/how-to-require-one-pod-per-minion-kublet-when-configuring-a-replication-controll/33381862#33381862 )).

# Latest Files

See here for the latest maintained and updated versions of these example files:
https://github.com/draios/sysdig-cloud-scripts/tree/master/agent_deploy/kubernetes

# Install instructions

Please see the Sysdig Cloud support site for the latest documentation:
http://support.sysdigcloud.com/hc/en-us/sections/200959909



<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/sysdig-cloud/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->

## Guestbook Example

This example shows how to build a simple, multi-tier web application using Kubernetes and [Docker](https://www.docker.com/).

**Table of Contents**
<!-- BEGIN MUNGE: GENERATED_TOC -->

  - [Guestbook Example](#guestbook-example)
    - [Prerequisites](#prerequisites)
    - [Quick Start](#quick-start)
    - [Step One: Start up the redis master](#step-one-start-up-the-redis-master)
      - [Define a Deployment](#define-a-deployment)
      - [Define a Service](#define-a-service)
      - [Create a Service](#create-a-service)
      - [Finding a Service](#finding-a-service)
        - [Environment variables](#environment-variables)
        - [DNS service](#dns-service)
      - [Create a Deployment](#create-a-deployment)
      - [Optional Interlude](#optional-interlude)
    - [Step Two: Start up the redis slave](#step-two-start-up-the-redis-slave)
    - [Step Three: Start up the guestbook frontend](#step-three-start-up-the-guestbook-frontend)
      - [Using 'type: LoadBalancer' for the frontend service (cloud-provider-specific)](#using-type-loadbalancer-for-the-frontend-service-cloud-provider-specific)
    - [Step Four: Cleanup](#step-four-cleanup)
    - [Troubleshooting](#troubleshooting)
    - [Appendix: Accessing the guestbook site externally](#appendix-accessing-the-guestbook-site-externally)
      - [Google Compute Engine External Load Balancer Specifics](#google-compute-engine-external-load-balancer-specifics)

<!-- END MUNGE: GENERATED_TOC -->

The example consists of:

- A web frontend
- A [redis](http://redis.io/) master (for storage), and a replicated set of redis 'slaves'.

The web frontend interacts with the redis master via javascript redis API calls.

**Note**:  If you are running this example on a [Google Container Engine](https://cloud.google.com/container-engine/) installation, see [this Google Container Engine guestbook walkthrough](https://cloud.google.com/container-engine/docs/tutorials/guestbook) instead. The basic concepts are the same, but the walkthrough is tailored to a Container Engine setup.

### Prerequisites

This example requires a running Kubernetes cluster. First, check that kubectl is properly configured by getting the cluster state:

```console
$ kubectl cluster-info
```

If you see a url response, you are ready to go. If not, read the [Getting Started guides](http://kubernetes.io/docs/getting-started-guides/) for how to get started, and follow the [prerequisites](http://kubernetes.io/docs/user-guide/prereqs/) to install and configure `kubectl`. As noted above, if you have a Google Container Engine cluster set up, read [this example](https://cloud.google.com/container-engine/docs/tutorials/guestbook) instead.

All the files referenced in this example can be downloaded in [current folder](./).

### Quick Start

This section shows the simplest way to get the example work. If you want to know the details, you should skip this and read [the rest of the example](#step-one-start-up-the-redis-master).

Start the guestbook with one command:

```console
$ kubectl create -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml
service "redis-master" created
deployment "redis-master" created
service "redis-slave" created
deployment "redis-slave" created
service "frontend" created
deployment "frontend" created
```

Alternatively, you can start the guestbook by running:

```console
$ kubectl create -f examples/guestbook/
```

Then, list all your Services:

```console
$ kubectl get services
NAME           CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
frontend       10.0.0.117   <none>        80/TCP     20s
redis-master   10.0.0.170   <none>        6379/TCP   20s
redis-slave    10.0.0.201   <none>        6379/TCP   20s
```

Now you can access the guestbook on each node with frontend Service's `<Cluster-IP>:<PORT>`, e.g. `10.0.0.117:80` in this guide. `<Cluster-IP>` is a cluster-internal IP. If you want to access the guestbook from outside of the cluster, add `type: NodePort` to the frontend Service `spec` field. Then you can access the guestbook with `<NodeIP>:NodePort` from outside of the cluster. On cloud providers which support external load balancers, adding `type: LoadBalancer` to the frontend Service `spec` field will provision a load balancer for your Service. There are several ways for you to access the guestbook. You may learn from [Accessing services running on the cluster](https://kubernetes.io/docs/concepts/cluster-administration/access-cluster/#accessing-services-running-on-the-cluster).

Clean up the guestbook:

```console
$ kubectl delete -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml
```

or

```console
$ kubectl delete -f examples/guestbook/
```


### Step One: Start up the redis master

Before continuing to the gory details, we also recommend you to read Kubernetes [concepts and user guide](http://kubernetes.io/docs/user-guide/).
**Note**: The redis master in this example is *not* highly available.  Making it highly available would be an interesting, but intricate exercise — redis doesn't actually support multi-master Deployments at this point in time, so high availability would be a somewhat tricky thing to implement, and might involve periodic serialization to disk, and so on.

#### Define a Deployment

To start the redis master, use the file [redis-master-deployment.yaml](redis-master-deployment.yaml), which describes a single [pod](http://kubernetes.io/docs/user-guide/pods/) running a redis key-value server in a container.

Although we have a single instance of our redis master, we are using a [Deployment](http://kubernetes.io/docs/user-guide/deployments/) to enforce that exactly one pod keeps running. E.g., if the node were to go down, the Deployment will ensure that the redis master gets restarted on a healthy node. (In our simplified example, this could result in data loss.)

The file [redis-master-deployment.yaml](redis-master-deployment.yaml) defines the redis master Deployment:

<!-- BEGIN MUNGE: EXAMPLE redis-master-deployment.yaml -->

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: redis-master
  # these labels can be applied automatically 
  # from the labels in the pod template if not set
  # labels:
  #   app: redis
  #   role: master
  #   tier: backend
spec:
  # this replicas value is default
  # modify it according to your case
  replicas: 1
  # selector can be applied automatically 
  # from the labels in the pod template if not set
  # selector:
  #   matchLabels:
  #     app: guestbook
  #     role: master
  #     tier: backend
  template:
    metadata:
      labels:
        app: redis
        role: master
        tier: backend
    spec:
      containers:
      - name: master
        image: gcr.io/google_containers/redis:e2e
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 6379
```

[Download example](redis-master-deployment.yaml?raw=true)
<!-- END MUNGE: EXAMPLE redis-master-deployment.yaml -->

#### Define a Service

A Kubernetes [Service](http://kubernetes.io/docs/user-guide/services/) is a named load balancer that proxies traffic to one or more containers. This is done using the [labels](http://kubernetes.io/docs/user-guide/labels/) metadata that we defined in the `redis-master` pod above.  As mentioned, we have only one redis master, but we nevertheless want to create a Service for it. Why? Because it gives us a deterministic way to route to the single master using an elastic IP.

Services find the pods to load balance based on the pods' labels.
The selector field of the Service description determines which pods will receive the traffic sent to the Service, and the `port` and `targetPort` information defines what port the Service proxy will run at.

The file [redis-master-service.yaml](redis-master-deployment.yaml) defines the redis master Service:

<!-- BEGIN MUNGE: EXAMPLE redis-master-service.yaml -->

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-master
  labels:
    app: redis
    role: master
    tier: backend
spec:
  ports:
    # the port that this service should serve on
  - port: 6379
    targetPort: 6379
  selector:
    app: redis
    role: master
    tier: backend
```

[Download example](redis-master-service.yaml?raw=true)
<!-- END MUNGE: EXAMPLE redis-master-service.yaml -->

#### Create a Service

According to the [config best practices](http://kubernetes.io/docs/user-guide/config-best-practices/), create a Service before corresponding Deployments so that the scheduler can spread the pods comprising the Service. So we first create the Service by running:

```console
$ kubectl create -f examples/guestbook/redis-master-service.yaml
service "redis-master" created
```

Then check the list of services, which should include the redis-master:

```console
$ kubectl get services
NAME              CLUSTER-IP       EXTERNAL-IP       PORT(S)       AGE
redis-master      10.0.76.248      <none>            6379/TCP      1s
```

This will cause all pods to see the redis master apparently running on `<CLUSTER-IP>:<PORT>`.  A Service can map an incoming port to any `targetPort` in the backend pod.  Once created, the Service proxy on each node is configured to set up a proxy on the specified port (in this case port `6379`).

`targetPort` will default to `port` if it is omitted in the configuration. `targetPort` is the port the container accepts traffic on, and `port` is the abstracted Service port, which can be any port other pods use to access the Service. For simplicity's sake, we omit it in the following configurations.

The traffic flow from slaves to masters can be described in two steps:

  - A *redis slave* will connect to `port` on the *redis master Service*
  - Traffic will be forwarded from the Service `port` (on the Service node) to the `targetPort` on the pod that the Service listens to.

For more details, please see [Connecting applications](http://kubernetes.io/docs/user-guide/connecting-applications/).

#### Finding a Service

Kubernetes supports two primary modes of finding a Service — environment variables and DNS.


##### Environment variables

The services in a Kubernetes cluster are discoverable inside other containers via [environment variables](https://kubernetes.io/docs/concepts/services-networking/service/#environment-variables).

##### DNS service

An alternative is to use the [cluster's DNS service](https://kubernetes.io/docs/concepts/services-networking/service/#dns), if it has been enabled for the cluster.  This lets all pods do name resolution of services automatically, based on the Service name.

This example has been configured to use the DNS service by default.

If your cluster does not have the DNS service enabled, then you can use environment variables by setting the
`GET_HOSTS_FROM` env value in both
[redis-slave-deployment.yaml](redis-slave-deployment.yaml) and [frontend-deployment.yaml](frontend-deployment.yaml)
from `dns` to `env` before you start up the app.
(However, this is unlikely to be necessary. You can check for the DNS service in the list of the cluster's services by
running `kubectl --namespace=kube-system get rc -l k8s-app=kube-dns`.)
Note that switching to env causes creation-order dependencies, since Services need to be created before their clients that require env vars.

#### Create a Deployment

Second, create the redis master pod in your Kubernetes cluster by running:

```console
$ kubectl create -f examples/guestbook/redis-master-deployment.yaml
deployment "redis-master" created
```

You can see the Deployment for your cluster by running:

```console
$ kubectl get deployments
NAME           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
redis-master   1         1         1            1           27s
```

Then, you can list the pods in the cluster, to verify that the master is running:

```console
$ kubectl get pods
```

You'll see all pods in the cluster, including the redis master pod, and the status of each pod.
The name of the redis master will look similar to that in the following list:

```console
NAME                            READY     STATUS    RESTARTS   AGE
redis-master-2353460263-1ecey   1/1       Running   0          1m
...
```

(Note that an initial `docker pull` to grab a container image may take a few minutes, depending on network conditions. A pod will be reported as `Pending` while its image is being downloaded.)

`kubectl get pods` will show only the pods in the default [namespace](http://kubernetes.io/docs/user-guide/namespaces/).  To see pods in all namespaces, run:

```
kubectl get pods --all-namespaces
```

For more details, please see [Configuring containers](http://kubernetes.io/docs/user-guide/configuring-containers/) and [Deploying applications](http://kubernetes.io/docs/user-guide/deploying-applications/).

#### Optional Interlude

You can get information about a pod, including the machine that it is running on, via `kubectl describe pods/<POD-NAME>`.  E.g., for the redis master, you should see something like the following (your pod name will be different):

```console
$ kubectl describe pods redis-master-2353460263-1ecey
Name:		redis-master-2353460263-1ecey
Node:		kubernetes-node-m0k7/10.240.0.5
...
Labels:		app=redis,pod-template-hash=2353460263,role=master,tier=backend
Status:		Running
IP:		10.244.2.3
Controllers:	ReplicaSet/redis-master-2353460263
Containers:
  master:
    Container ID:	docker://76cf8115485966131587958ea3cbe363e2e1dcce129e2e624883f393ce256f6c
    Image:		gcr.io/google_containers/redis:e2e
    Image ID:		docker://e5f6c5a2b5646828f51e8e0d30a2987df7e8183ab2c3ed0ca19eaa03cc5db08c
    Port:		6379/TCP
...
```

The `Node` is the name and IP of the machine, e.g. `kubernetes-node-m0k7` in the example above. You can find more details about this node with `kubectl describe nodes kubernetes-node-m0k7`.

If you want to view the container logs for a given pod, you can run:

```console
$ kubectl logs <POD-NAME>
```

These logs will usually give you enough information to troubleshoot.

However, if you should want to SSH to the listed host machine, you can inspect various logs there directly as well.  For example, with Google Compute Engine, using `gcloud`, you can SSH like this:

```console
me@workstation$ gcloud compute ssh <NODE-NAME>
```

Then, you can look at the Docker containers on the remote machine.  You should see something like this (the specifics of the IDs will be different):

```console
me@kubernetes-node-krxw:~$ sudo docker ps
CONTAINER ID        IMAGE                                 COMMAND                 CREATED              STATUS              PORTS                   NAMES
...
0ffef9649265        redis:latest                          "/entrypoint.sh redi"   About a minute ago   Up About a minute                           k8s_master.869d22f3_redis-master-dz33o_default_1449a58a-5ead-11e5-a104-688f84ef8ef6_d74cb2b5
```

If you want to see the logs for a given container, you can run:

```console
$ docker logs <container_id>
```

### Step Two: Start up the redis slave

Now that the redis master is running, we can start up its 'read slaves'.

We'll define these as replicated pods as well, though this time — unlike for the redis master — we'll define the number of replicas to be 2.
In Kubernetes, a Deployment is responsible for managing multiple instances of a replicated pod. The Deployment will automatically launch new pods if the number of replicas falls below the specified number.
(This particular replicated pod is a great one to test this with -- you can try killing the Docker processes for your pods directly, then watch them come back online on a new node shortly thereafter.)

Just like the master, we want to have a Service to proxy connections to the redis slaves. In this case, in addition to discovery, the slave Service will provide transparent load balancing to web app clients.

This time we put the Service and Deployment into one [file](http://kubernetes.io/docs/user-guide/managing-deployments/#organizing-resource-configurations). Grouping related objects together in a single file is often better than having separate files.
The specification for the slaves is in [all-in-one/redis-slave.yaml](all-in-one/redis-slave.yaml):

<!-- BEGIN MUNGE: EXAMPLE all-in-one/redis-slave.yaml -->

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-slave
  labels:
    app: redis
    role: slave
    tier: backend
spec:
  ports:
    # the port that this service should serve on
  - port: 6379
  selector:
    app: redis
    role: slave
    tier: backend
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: redis-slave
  # these labels can be applied automatically
  # from the labels in the pod template if not set
  # labels:
  #   app: redis
  #   role: slave
  #   tier: backend
spec:
  # this replicas value is default
  # modify it according to your case
  replicas: 2
  # selector can be applied automatically
  # from the labels in the pod template if not set
  # selector:
  #   matchLabels:
  #     app: guestbook
  #     role: slave
  #     tier: backend
  template:
    metadata:
      labels:
        app: redis
        role: slave
        tier: backend
    spec:
      containers:
      - name: slave
        image: gcr.io/google_samples/gb-redisslave:v1
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        env:
        - name: GET_HOSTS_FROM
          value: dns
          # If your cluster config does not include a dns service, then to
          # instead access an environment variable to find the master
          # service's host, comment out the 'value: dns' line above, and
          # uncomment the line below.
          # value: env
        ports:
        - containerPort: 6379
```

[Download example](all-in-one/redis-slave.yaml?raw=true)
<!-- END MUNGE: EXAMPLE all-in-one/redis-slave.yaml -->

This time the selector for the Service is `app=redis,role=slave,tier=backend`, because that identifies the pods running redis slaves. It is generally helpful to set labels on your Service itself as we've done here to make it easy to locate them with the `kubectl get services -l "app=redis,role=slave,tier=backend"` command. For more information on the usage of labels, see [using-labels-effectively](http://kubernetes.io/docs/user-guide/managing-deployments/#using-labels-effectively).

Now that you have created the specification, create the Service in your cluster by running:

```console
$ kubectl create -f examples/guestbook/all-in-one/redis-slave.yaml
service "redis-slave" created
deployment "redis-slave" created

$ kubectl get services
NAME           CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
redis-master   10.0.76.248    <none>        6379/TCP   20m
redis-slave    10.0.112.188   <none>        6379/TCP   16s

$ kubectl get deployments
NAME           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
redis-master   1         1         1            1           22m
redis-slave    2         2         2            2           2m
```

Once the Deployment is up, you can list the pods in the cluster, to verify that the master and slaves are running.  You should see a list that includes something like the following:

```console
$ kubectl get pods
NAME                            READY     STATUS    RESTARTS   AGE
redis-master-2353460263-1ecey   1/1       Running   0          35m
redis-slave-1691881626-dlf5f    1/1       Running   0          15m
redis-slave-1691881626-sfn8t    1/1       Running   0          15m
```

You should see a single redis master pod and two redis slave pods.  As mentioned above, you can get more information about any pod with: `kubectl describe pods/<POD_NAME>`. And also can view the resources on [kube-ui](http://kubernetes.io/docs/user-guide/ui/).

### Step Three: Start up the guestbook frontend

A frontend pod is a simple PHP server that is configured to talk to either the slave or master services, depending on whether the client request is a read or a write. It exposes a simple AJAX interface, and serves an Angular-based UX.
Again we'll create a set of replicated frontend pods instantiated by a Deployment — this time, with three replicas.

As with the other pods, we now want to create a Service to group the frontend pods.
The Deployment and Service are described in the file [all-in-one/frontend.yaml](all-in-one/frontend.yaml):

<!-- BEGIN MUNGE: EXAMPLE all-in-one/frontend.yaml -->

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend
  labels:
    app: guestbook
    tier: frontend
spec:
  # if your cluster supports it, uncomment the following to automatically create
  # an external load-balanced IP for the frontend service.
  # type: LoadBalancer
  ports:
    # the port that this service should serve on
  - port: 80
  selector:
    app: guestbook
    tier: frontend
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: frontend
  # these labels can be applied automatically
  # from the labels in the pod template if not set
  # labels:
  #   app: guestbook
  #   tier: frontend
spec:
  # this replicas value is default
  # modify it according to your case
  replicas: 3
  # selector can be applied automatically
  # from the labels in the pod template if not set
  # selector:
  #   matchLabels:
  #     app: guestbook
  #     tier: frontend
  template:
    metadata:
      labels:
        app: guestbook
        tier: frontend
    spec:
      containers:
      - name: php-redis
        image: gcr.io/google-samples/gb-frontend:v4
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        env:
        - name: GET_HOSTS_FROM
          value: dns
          # If your cluster config does not include a dns service, then to
          # instead access environment variables to find service host
          # info, comment out the 'value: dns' line above, and uncomment the
          # line below.
          # value: env
        ports:
        - containerPort: 80
```

[Download example](all-in-one/frontend.yaml?raw=true)
<!-- END MUNGE: EXAMPLE all-in-one/frontend.yaml -->

#### Using 'type: LoadBalancer' for the frontend service (cloud-provider-specific)

For supported cloud providers, such as Google Compute Engine or Google Container Engine, you can specify to use an external load balancer
in the service `spec`, to expose the service onto an external load balancer IP.
To do this, uncomment the `type: LoadBalancer` line in the [all-in-one/frontend.yaml](all-in-one/frontend.yaml) file before you start the service.

[See the appendix below](#appendix-accessing-the-guestbook-site-externally) on accessing the guestbook site externally for more details.

Create the service and Deployment like this:

```console
$ kubectl create -f examples/guestbook/all-in-one/frontend.yaml
service "frontend" created
deployment "frontend" created
```

Then, list all your services again:

```console
$ kubectl get services
NAME           CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
frontend       10.0.63.63     <none>        80/TCP     1m
redis-master   10.0.76.248    <none>        6379/TCP   39m
redis-slave    10.0.112.188   <none>        6379/TCP   19m
```

Also list all your Deployments:

```console
$ kubectl get deployments 
NAME           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
frontend       3         3         3            3           2m
redis-master   1         1         1            1           39m
redis-slave    2         2         2            2           20m
```

Once it's up, i.e. when desired replicas match current replicas (again, it may take up to thirty seconds to create the pods), you can list the pods with specified labels in the cluster, to verify that the master, slaves and frontends are all running. You should see a list containing pods with label 'tier' like the following:

```console
$ kubectl get pods -L tier
NAME                            READY     STATUS    RESTARTS   AGE       TIER
frontend-1211764471-4e1j2       1/1       Running   0          4m        frontend
frontend-1211764471-gkbkv       1/1       Running   0          4m        frontend
frontend-1211764471-rk1cf       1/1       Running   0          4m        frontend
redis-master-2353460263-1ecey   1/1       Running   0          42m       backend
redis-slave-1691881626-dlf5f    1/1       Running   0          22m       backend
redis-slave-1691881626-sfn8t    1/1       Running   0          22m       backend
```

You should see a single redis master pod, two redis slaves, and three frontend pods.

The code for the PHP server that the frontends are running is in `examples/guestbook/php-redis/guestbook.php`.  It looks like this:

```php
<?

set_include_path('.:/usr/local/lib/php');

error_reporting(E_ALL);
ini_set('display_errors', 1);

require 'Predis/Autoloader.php';

Predis\Autoloader::register();

if (isset($_GET['cmd']) === true) {
  $host = 'redis-master';
  if (getenv('GET_HOSTS_FROM') == 'env') {
    $host = getenv('REDIS_MASTER_SERVICE_HOST');
  }
  header('Content-Type: application/json');
  if ($_GET['cmd'] == 'set') {
    $client = new Predis\Client([
      'scheme' => 'tcp',
      'host'   => $host,
      'port'   => 6379,
    ]);

    $client->set($_GET['key'], $_GET['value']);
    print('{"message": "Updated"}');
  } else {
    $host = 'redis-slave';
    if (getenv('GET_HOSTS_FROM') == 'env') {
      $host = getenv('REDIS_SLAVE_SERVICE_HOST');
    }
    $client = new Predis\Client([
      'scheme' => 'tcp',
      'host'   => $host,
      'port'   => 6379,
    ]);

    $value = $client->get($_GET['key']);
    print('{"data": "' . $value . '"}');
  }
} else {
  phpinfo();
} ?>
```

Note the use of the `redis-master` and `redis-slave` host names -- we're finding those Services via the Kubernetes cluster's DNS service, as discussed above.  All the frontend replicas will write to the load-balancing redis-slaves service, which can be highly replicated as well.

### Step Four: Cleanup

If you are in a live Kubernetes cluster, you can just kill the pods by deleting the Deployments and Services. Using labels to select the resources to delete is an easy way to do this in one command.

```console
$ kubectl delete deployments,services -l "app in (redis, guestbook)"
```

To completely tear down a Kubernetes cluster, if you ran this from source, you can use:

```console
$ <kubernetes>/cluster/kube-down.sh
```

### Troubleshooting

If you are having trouble bringing up your guestbook app, double check that your external IP is properly defined for your frontend Service, and that the firewall for your cluster nodes is open to port 80.

Then, see the [troubleshooting documentation](http://kubernetes.io/docs/troubleshooting/) for a further list of common issues and how you can diagnose them.



### Appendix: Accessing the guestbook site externally

You'll want to set up your guestbook Service so that it can be accessed from outside of the internal Kubernetes network. Above, we introduced one way to do that, by setting `type: LoadBalancer` to Service `spec`.

More generally, Kubernetes supports two ways of exposing a Service onto an external IP address: `NodePort`s and `LoadBalancer`s , as described [here](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services---service-types).

If the `LoadBalancer` specification is used, it can take a short period for an external IP to show up in `kubectl get services` output, but you should then see it listed as well, e.g. like this:

```console
$ kubectl get services
NAME           CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
frontend       10.0.63.63     23.236.59.54  80/TCP     1m
redis-master   10.0.76.248    <none>        6379/TCP   39m
redis-slave    10.0.112.188   <none>        6379/TCP   19m
```

Once you've exposed the service to an external IP, visit the IP to see your guestbook in action, i.e. `http://<EXTERNAL-IP>:<PORT>`.

You should see a web page that looks something like this (without the messages).  Try adding some entries to it!

<img width="50%" src="http://amy-jo.storage.googleapis.com/images/gb_k8s_ex1.png">

If you are more advanced in the ops arena, you can also manually get the service IP from looking at the output of `kubectl get pods,services`, and modify your firewall using standard tools and services (firewalld, iptables, selinux) which you are already familiar with.

#### Google Compute Engine External Load Balancer Specifics

In Google Compute Engine, Kubernetes automatically creates forwarding rules for services with `LoadBalancer`.

You can list the forwarding rules like this (the forwarding rule also indicates the external IP):

```console
$ gcloud compute forwarding-rules list
NAME                  REGION      IP_ADDRESS     IP_PROTOCOL TARGET
frontend              us-central1 130.211.188.51 TCP         us-central1/targetPools/frontend
```

In Google Compute Engine, you also may need to open the firewall for port 80 using the [console][cloud-console] or the `gcloud` tool. The following command will allow traffic from any source to instances tagged `kubernetes-node` (replace with your tags as appropriate):

```console
$ gcloud compute firewall-rules create --allow=tcp:80 --target-tags=kubernetes-node kubernetes-node-80
```

For GCE Kubernetes startup details, see the [Getting started on Google Compute Engine](http://kubernetes.io/docs/getting-started-guides/gce/)

For Google Compute Engine details about limiting traffic to specific sources, see the [Google Compute Engine firewall documentation][gce-firewall-docs].

[cloud-console]: https://console.developer.google.com
[gce-firewall-docs]: https://cloud.google.com/compute/docs/networking#firewalls

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/guestbook/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Storm example

Following this example, you will create a functional [Apache
Storm](http://storm.apache.org/) cluster using Kubernetes and
[Docker](http://docker.io).

You will setup an [Apache ZooKeeper](http://zookeeper.apache.org/)
service, a Storm master service (a.k.a. Nimbus server), and a set of
Storm workers (a.k.a. supervisors).

For the impatient expert, jump straight to the [tl;dr](#tldr)
section.

### Sources

Source is freely available at:
* Docker image - https://github.com/mattf/docker-storm
* Docker Trusted Build - https://registry.hub.docker.com/search?q=mattf/storm

## Step Zero: Prerequisites

This example assumes you have a Kubernetes cluster installed and
running, and that you have installed the ```kubectl``` command line
tool somewhere in your path. Please see the [getting
started](https://kubernetes.io/docs/getting-started-guides/) for installation
instructions for your platform.

## Step One: Start your ZooKeeper service

ZooKeeper is a distributed coordination [service](https://kubernetes.io/docs/user-guide/services.md) that Storm uses as a
bootstrap and for state storage.

Use the [`examples/storm/zookeeper.json`](zookeeper.json) file to create a [pod](https://kubernetes.io/docs/user-guide/pods.md) running
the ZooKeeper service.

```sh
$ kubectl create -f examples/storm/zookeeper.json
```

Then, use the [`examples/storm/zookeeper-service.json`](zookeeper-service.json) file to create a
logical service endpoint that Storm can use to access the ZooKeeper
pod.

```sh
$ kubectl create -f examples/storm/zookeeper-service.json
```

You should make sure the ZooKeeper pod is Running and accessible
before proceeding.

### Check to see if ZooKeeper is running

```sh
$ kubectl get pods
NAME        READY     STATUS    RESTARTS   AGE
zookeeper   1/1       Running   0          43s
```

### Check to see if ZooKeeper is accessible

```console
$ kubectl get services
NAME              CLUSTER_IP       EXTERNAL_IP       PORT(S)       SELECTOR               AGE
zookeeper         10.254.139.141   <none>            2181/TCP      name=zookeeper         10m
kubernetes        10.0.0.2         <none>            443/TCP       <none>                 1d

$ echo ruok | nc 10.254.139.141 2181; echo
imok
```

## Step Two: Start your Nimbus service

The Nimbus service is the master (or head) service for a Storm
cluster. It depends on a functional ZooKeeper service.

Use the [`examples/storm/storm-nimbus.json`](storm-nimbus.json) file to create a pod running
the Nimbus service.

```sh
$ kubectl create -f examples/storm/storm-nimbus.json
```

Then, use the [`examples/storm/storm-nimbus-service.json`](storm-nimbus-service.json) file to
create a logical service endpoint that Storm workers can use to access
the Nimbus pod.

```sh
$ kubectl create -f examples/storm/storm-nimbus-service.json
```

Ensure that the Nimbus service is running and functional.

### Check to see if Nimbus is running and accessible

```sh
$ kubectl get services
NAME                LABELS                                    SELECTOR            IP(S)               PORT(S)
kubernetes          component=apiserver,provider=kubernetes   <none>              10.254.0.2          443
zookeeper           name=zookeeper                            name=zookeeper      10.254.139.141      2181
nimbus              name=nimbus                               name=nimbus         10.254.115.208      6627

$ sudo docker run -it -w /opt/apache-storm mattf/storm-base sh -c '/configure.sh 10.254.139.141 10.254.115.208; ./bin/storm list'
...
No topologies running.
```

## Step Three: Start your Storm workers

The Storm workers (or supervisors) do the heavy lifting in a Storm
cluster. They run your stream processing topologies and are managed by
the Nimbus service.

The Storm workers need both the ZooKeeper and Nimbus services to be
running.

Use the [`examples/storm/storm-worker-controller.json`](storm-worker-controller.json) file to create a
[replication controller](https://kubernetes.io/docs/user-guide/replication-controller.md) that manages the worker pods.

```sh
$ kubectl create -f examples/storm/storm-worker-controller.json
```

### Check to see if the workers are running

One way to check on the workers is to get information from the
ZooKeeper service about how many clients it has.

```sh
$  echo stat | nc 10.254.139.141 2181; echo
Zookeeper version: 3.4.6--1, built on 10/23/2014 14:18 GMT
Clients:
 /192.168.48.0:44187[0](queued=0,recved=1,sent=0)
 /192.168.45.0:39568[1](queued=0,recved=14072,sent=14072)
 /192.168.86.1:57591[1](queued=0,recved=34,sent=34)
 /192.168.8.0:50375[1](queued=0,recved=34,sent=34)

Latency min/avg/max: 0/2/2570
Received: 23199
Sent: 23198
Connections: 4
Outstanding: 0
Zxid: 0xa39
Mode: standalone
Node count: 13
```

There should be one client from the Nimbus service and one per
worker. Ideally, you should get ```stat``` output from ZooKeeper
before and after creating the replication controller.

(Pull requests welcome for alternative ways to validate the workers)

## tl;dr

```kubectl create -f zookeeper.json```

```kubectl create -f zookeeper-service.json```

Make sure the ZooKeeper Pod is running (use: ```kubectl get pods```).

```kubectl create -f storm-nimbus.json```

```kubectl create -f storm-nimbus-service.json```

Make sure the Nimbus Pod is running.

```kubectl create -f storm-worker-controller.json```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/storm/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Selenium on Kubernetes

Selenium is a browser automation tool used primarily for testing web applications. However when Selenium is used in a CI pipeline to test applications, there is often contention around the use of Selenium resources. This example shows you how to deploy Selenium to Kubernetes in a scalable fashion.

### Prerequisites

This example assumes you have a working Kubernetes cluster and a properly configured kubectl client. See the [Getting Started Guides](https://kubernetes.io/docs/getting-started-guides/) for details.

Google Container Engine is also a quick way to get Kubernetes up and running: https://cloud.google.com/container-engine/

Your cluster must have 4 CPU and 6 GB of RAM to complete the example up to the scaling portion.

### Deploy Selenium Grid Hub:

We will be using Selenium Grid Hub to make our Selenium install scalable via a master/worker model. The Selenium Hub is the master, and the Selenium Nodes are the workers(not to be confused with Kubernetes nodes). We only need one hub, but we're using a replication controller to ensure that the hub is always running:

```console
kubectl create --filename=examples/selenium/selenium-hub-rc.yaml
```

The Selenium Nodes will need to know how to get to the Hub, let's create a service for the nodes to connect to.

```console
kubectl create --filename=examples/selenium/selenium-hub-svc.yaml
```

### Verify Selenium Hub Deployment

Let's verify our deployment of Selenium hub by connecting to the web console.

#### Kubernetes Nodes Reachable

If your Kubernetes nodes are reachable from your network, you can verify the hub by hitting it on the nodeport. You can retrieve the nodeport by typing `kubectl describe svc selenium-hub`, however the snippet below automates that by using kubectl's template functionality:

```console
export NODEPORT=`kubectl get svc --selector='app=selenium-hub' --output=template --template="{{ with index .items 0}}{{with index .spec.ports 0 }}{{.nodePort}}{{end}}{{end}}"`
export NODE=`kubectl get nodes --output=template --template="{{with index .items 0 }}{{.metadata.name}}{{end}}"`

curl http://$NODE:$NODEPORT
```

#### Kubernetes Nodes Unreachable

If you cannot reach your Kubernetes nodes from your network, you can proxy via kubectl.

```console
export PODNAME=`kubectl get pods --selector="app=selenium-hub" --output=template --template="{{with index .items 0}}{{.metadata.name}}{{end}}"`
kubectl port-forward $PODNAME 4444:4444
```

In a separate terminal, you can now check the status.

```console
curl http://localhost:4444
```

#### Using Google Container Engine

If you are using Google Container Engine, you can expose your hub via the internet. This is a bad idea for many reasons, but you can do it as follows:

```console
kubectl expose rc selenium-hub --name=selenium-hub-external --labels="app=selenium-hub,external=true" --type=LoadBalancer
```

Then wait a few minutes, eventually your new `selenium-hub-external` service will be assigned a load balanced IP from gcloud. Once `kubectl get svc selenium-hub-external` shows two IPs, run this snippet.

```console
export INTERNET_IP=`kubectl get svc --selector="app=selenium-hub,external=true" --output=template --template="{{with index .items 0}}{{with index .status.loadBalancer.ingress 0}}{{.ip}}{{end}}{{end}}"`

curl http://$INTERNET_IP:4444/
```

You should now be able to hit `$INTERNET_IP` via your web browser, and so can everyone else on the Internet!

### Deploy Firefox and Chrome Nodes:

Now that the Hub is up, we can deploy workers.

This will deploy 2 Chrome nodes.

```console
kubectl create --filename=examples/selenium/selenium-node-chrome-rc.yaml
```

And 2 Firefox nodes to match.

```console
kubectl create --filename=examples/selenium/selenium-node-firefox-rc.yaml
```

Once the pods start, you will see them show up in the Selenium Hub interface.

### Run a Selenium Job

Let's run a quick Selenium job to validate our setup.

#### Setup Python Environment

First, we need to start a python container that we can attach to.

```console
kubectl run selenium-python --image=google/python-hello
```

Next, we need to get inside this container.

```console
export PODNAME=`kubectl get pods --selector="run=selenium-python" --output=template --template="{{with index .items 0}}{{.metadata.name}}{{end}}"`
kubectl exec --stdin=true --tty=true $PODNAME bash
```

Once inside, we need to install the Selenium library

```console
pip install selenium
```

#### Run Selenium Job with Python

We're all set up, start the python interpreter.

```console
python
```

And paste in the contents of selenium-test.py.

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def check_browser(browser):
  driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=getattr(DesiredCapabilities, browser)
  )
  driver.get("http://google.com")
  assert "google" in driver.page_source
  driver.close()
  print("Browser %s checks out!" % browser)


check_browser("FIREFOX")
check_browser("CHROME")
```

You should get

```
>>> check_browser("FIREFOX")
Browser FIREFOX checks out!
>>> check_browser("CHROME")
Browser CHROME checks out!
```

Congratulations, your Selenium Hub is up, with Firefox and Chrome nodes!

### Scale your Firefox and Chrome nodes.

If you need more Firefox or Chrome nodes, your hardware is the limit:

```console
kubectl scale rc selenium-node-firefox --replicas=10
kubectl scale rc selenium-node-chrome --replicas=10
```

You now have 10 Firefox and 10 Chrome nodes, happy Seleniuming!

### Debugging

Sometimes it is necessary to check on a hung test. Each pod is running VNC. To check on one of the browser nodes via VNC, it's recommended that you proxy, since we don't want to expose a service for every pod, and the containers have a weak VNC password. Replace POD_NAME with the name of the pod you want to connect to.

```console
kubectl port-forward $POD_NAME 5900:5900
```

Then connect to localhost:5900 with your VNC client using the password "secret"

Enjoy your scalable Selenium Grid!

Adapted from: https://github.com/SeleniumHQ/docker-selenium

### Teardown

To remove all created resources, run the following:

```console
kubectl delete rc selenium-hub
kubectl delete rc selenium-node-chrome
kubectl delete rc selenium-node-firefox
kubectl delete deployment selenium-python
kubectl delete svc selenium-hub
kubectl delete svc selenium-hub-external
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/selenium/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Phabricator example

This example shows how to build a simple multi-tier web application using Kubernetes and Docker.

The example combines a web frontend and an external service that provides MySQL database. We use CloudSQL on Google Cloud Platform in this example, but in principle any approach to running MySQL should work.

### Step Zero: Prerequisites

This example assumes that you have a basic understanding of kubernetes [services](https://kubernetes.io/docs/user-guide/services.md) and that you have forked the repository and [turned up a Kubernetes cluster](https://kubernetes.io/docs/getting-started-guides/):

```sh
$ cd kubernetes
$ cluster/kube-up.sh
```

### Step One: Set up Cloud SQL instance

Follow the [official instructions](https://cloud.google.com/sql/docs/getting-started) to set up Cloud SQL instance.

In the remaining part of this example we will assume that your instance is named "phabricator-db", has IP 1.2.3.4, is listening on port 3306 and the password is "1234".

### Step Two: Authenticate phabricator in Cloud SQL

In order to allow phabricator to connect to your Cloud SQL instance you need to run the following command to authorize all your nodes within a cluster:

```bash
NODE_NAMES=`kubectl get nodes | cut -d" " -f1 | tail -n+2`
NODE_IPS=`gcloud compute instances list $NODE_NAMES | tr -s " " | cut -d" " -f 5 | tail -n+2`
gcloud sql instances patch phabricator-db --authorized-networks $NODE_IPS
```

Otherwise you will see the following logs:

```bash
$ kubectl logs phabricator-controller-02qp4
[...]
Raw MySQL Error: Attempt to connect to root@1.2.3.4 failed with error
#2013: Lost connection to MySQL server at 'reading initial communication packet', system error: 0.

```

### Step Three: Turn up the phabricator

To start Phabricator server use the file [`examples/phabricator/phabricator-controller.json`](phabricator-controller.json) which describes a [replication controller](https://kubernetes.io/docs/user-guide/replication-controller.md) with a single [pod](https://kubernetes.io/docs/user-guide/pods.md) running an Apache server with Phabricator PHP source:

<!-- BEGIN MUNGE: EXAMPLE phabricator-controller.json -->

```json
{
  "kind": "ReplicationController",
  "apiVersion": "v1",
  "metadata": {
    "name": "phabricator-controller",
    "labels": {
      "name": "phabricator"
    }
  },
  "spec": {
    "replicas": 1,
    "selector": {
      "name": "phabricator"
    },
    "template": {
      "metadata": {
        "labels": {
          "name": "phabricator"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "phabricator",
            "image": "fgrzadkowski/example-php-phabricator",
            "ports": [
              {
                "name": "http-server",
                "containerPort": 80
              }
            ],
            "env": [
              {
                "name": "MYSQL_SERVICE_IP",
                "value": "1.2.3.4"
              },
              {
                "name": "MYSQL_SERVICE_PORT",
                "value": "3306"
              },
              {
                "name": "MYSQL_PASSWORD",
                "value": "1234"
              }
            ]
          }
        ]
      }
    }
  }
}
```

[Download example](phabricator-controller.json?raw=true)
<!-- END MUNGE: EXAMPLE phabricator-controller.json -->

Create the phabricator pod in your Kubernetes cluster by running:

```sh
$ kubectl create -f examples/phabricator/phabricator-controller.json
```

**Note:** Remember to substitute environment variable values in json file before create replication controller.

Once that's up you can list the pods in the cluster, to verify that it is running:

```sh
kubectl get pods
```

You'll see a single phabricator pod. It will also display the machine that the pod is running on once it gets placed (may take up to thirty seconds):

```
NAME                           READY     STATUS    RESTARTS   AGE
phabricator-controller-9vy68   1/1       Running   0          1m
```

If you ssh to that machine, you can run `docker ps` to see the actual pod:

```sh
me@workstation$ gcloud compute ssh --zone us-central1-b kubernetes-node-2

$ sudo docker ps
CONTAINER ID        IMAGE                             COMMAND     CREATED       STATUS      PORTS   NAMES
54983bc33494        fgrzadkowski/phabricator:latest   "/run.sh"   2 hours ago   Up 2 hours          k8s_phabricator.d6b45054_phabricator-controller-02qp4.default.api_eafb1e53-b6a9-11e4-b1ae-42010af05ea6_01c2c4ca
```

(Note that initial `docker pull` may take a few minutes, depending on network conditions.  During this time, the `get pods` command will return `Pending` because the container has not yet started )

### Step Four: Turn up the phabricator service

A Kubernetes 'service' is a named load balancer that proxies traffic to one or more containers. The services in a Kubernetes cluster are discoverable inside other containers via *environment variables*. Services find the containers to load balance based on pod labels.  These environment variables are typically referenced in application code, shell scripts, or other places where one node needs to talk to another in a distributed system.  You should catch up on [kubernetes services](https://kubernetes.io/docs/user-guide/services.md) before proceeding.

The pod that you created in Step Three has the label `name=phabricator`. The selector field of the service determines which pods will receive the traffic sent to the service.

Use the file [`examples/phabricator/phabricator-service.json`](phabricator-service.json):

<!-- BEGIN MUNGE: EXAMPLE phabricator-service.json -->

```json
{
  "kind": "Service",
  "apiVersion": "v1",
  "metadata": {
    "name": "phabricator"
  },
  "spec": {
    "ports": [
      {
        "port": 80,
        "targetPort": "http-server"
      }
    ],
    "selector": {
      "name": "phabricator"
    },
    "type": "LoadBalancer"
  }
}
```

[Download example](phabricator-service.json?raw=true)
<!-- END MUNGE: EXAMPLE phabricator-service.json -->

To create the service run:

```sh
$ kubectl create -f examples/phabricator/phabricator-service.json
phabricator
```

To play with the service itself, find the external IP of the load balancer:

```console
$ kubectl get services
NAME          LABELS                                    SELECTOR           IP(S)         PORT(S)
kubernetes    component=apiserver,provider=kubernetes   <none>             10.0.0.1      443/TCP
phabricator   <none>                                    name=phabricator   10.0.31.173   80/TCP
$ kubectl get services phabricator -o json | grep ingress -A 4
            "ingress": [
                {
                    "ip": "104.197.13.125"
                }
            ]
```

and then visit port 80 of that IP address.

**Note**: Provisioning of the external IP address may take few minutes.

**Note**: You may need to open the firewall for port 80 using the [console][cloud-console] or the `gcloud` tool. The following command will allow traffic from any source to instances tagged `kubernetes-node`:

```sh
$ gcloud compute firewall-rules create phabricator-node-80 --allow=tcp:80 --target-tags kubernetes-node
```

### Step Six: Cleanup

To turn down a Kubernetes cluster:

```sh
$ cluster/kube-down.sh
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/phabricator/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Guestbook Example

This example shows how to build a simple multi-tier web application using Kubernetes and Docker. The application consists of a web front-end, Redis master for storage, and replicated set of Redis slaves, all for which we will create Kubernetes replication controllers, pods, and services.

If you are running a cluster in Google Container Engine (GKE), instead see the [Guestbook Example for Google Container Engine](https://cloud.google.com/container-engine/docs/tutorials/guestbook).

##### Table of Contents

 * [Step Zero: Prerequisites](#step-zero)
 * [Step One: Create the Redis master pod](#step-one)
 * [Step Two: Create the Redis master service](#step-two)
 * [Step Three: Create the Redis slave pods](#step-three)
 * [Step Four: Create the Redis slave service](#step-four)
 * [Step Five: Create the guestbook pods](#step-five)
 * [Step Six: Create the guestbook service](#step-six)
 * [Step Seven: View the guestbook](#step-seven)
 * [Step Eight: Cleanup](#step-eight)

### Step Zero: Prerequisites <a id="step-zero"></a>

This example assumes that you have a working cluster. See the [Getting Started Guides](https://kubernetes.io/docs/getting-started-guides/) for details about creating a cluster.

**Tip:** View all the `kubectl` commands, including their options and descriptions in the [kubectl CLI reference](https://kubernetes.io/docs/user-guide/kubectl/kubectl.md).

### Step One: Create the Redis master pod<a id="step-one"></a>

Use the `examples/guestbook-go/redis-master-controller.json` file to create a [replication controller](https://kubernetes.io/docs/user-guide/replication-controller.md) and Redis master [pod](https://kubernetes.io/docs/user-guide/pods.md). The pod runs a Redis key-value server in a container. Using a replication controller is the preferred way to launch long-running pods, even for 1 replica, so that the pod benefits from the self-healing mechanism in Kubernetes (keeps the pods alive).

1. Use the [redis-master-controller.json](redis-master-controller.json) file to create the Redis master replication controller in your Kubernetes cluster by running the `kubectl create -f` *`filename`* command:

    ```console
    $ kubectl create -f examples/guestbook-go/redis-master-controller.json
    replicationcontrollers/redis-master
    ```

2. To verify that the redis-master controller is up, list the replication controllers you created in the cluster with the `kubectl get rc` command(if you don't specify a `--namespace`, the `default` namespace will be used. The same below):

    ```console
    $ kubectl get rc
    CONTROLLER             CONTAINER(S)            IMAGE(S)                    SELECTOR                         REPLICAS
    redis-master           redis-master            gurpartap/redis             app=redis,role=master            1
    ...
    ```

    Result: The replication controller then creates the single Redis master pod.

3. To verify that the redis-master pod is running, list the pods you created in cluster with the `kubectl get pods` command:

    ```console
    $ kubectl get pods
    NAME                        READY     STATUS    RESTARTS   AGE
    redis-master-xx4uv          1/1       Running   0          1m
    ...
    ```

    Result: You'll see a single Redis master pod and the machine where the pod is running after the pod gets placed (may take up to thirty seconds).

4. To verify what containers are running in the redis-master pod, you can SSH to that machine with `gcloud compute ssh --zone` *`zone_name`* *`host_name`* and then run `docker ps`:

    ```console
    me@workstation$ gcloud compute ssh --zone us-central1-b kubernetes-node-bz1p
    
    me@kubernetes-node-3:~$ sudo docker ps
    CONTAINER ID        IMAGE     COMMAND                  CREATED             STATUS
    d5c458dabe50        redis     "/entrypoint.sh redis"   5 minutes ago       Up 5 minutes
    ```

    Note: The initial `docker pull` can take a few minutes, depending on network conditions.

### Step Two: Create the Redis master service <a id="step-two"></a>

A Kubernetes [service](https://kubernetes.io/docs/user-guide/services.md) is a named load balancer that proxies traffic to one or more pods. The services in a Kubernetes cluster are discoverable inside other pods via environment variables or DNS.

Services find the pods to load balance based on pod labels. The pod that you created in Step One has the label `app=redis` and `role=master`. The selector field of the service determines which pods will receive the traffic sent to the service.

1. Use the [redis-master-service.json](redis-master-service.json) file to create the service in your Kubernetes cluster by running the `kubectl create -f` *`filename`* command:

    ```console
    $ kubectl create -f examples/guestbook-go/redis-master-service.json
    services/redis-master
    ```

2. To verify that the redis-master service is up, list the services you created in the cluster with the `kubectl get services` command:

    ```console
    $ kubectl get services
    NAME              CLUSTER_IP       EXTERNAL_IP       PORT(S)       SELECTOR               AGE
    redis-master      10.0.136.3       <none>            6379/TCP      app=redis,role=master  1h
    ...
    ```

    Result: All new pods will see the `redis-master` service running on the host (`$REDIS_MASTER_SERVICE_HOST` environment variable) at port 6379, or running on `redis-master:6379`. After the service is created, the service proxy on each node is configured to set up a proxy on the specified port (in our example, that's port 6379).


### Step Three: Create the Redis slave pods <a id="step-three"></a>

The Redis master we created earlier is a single pod (REPLICAS = 1), while the Redis read slaves we are creating here are 'replicated' pods. In Kubernetes, a replication controller is responsible for managing the multiple instances of a replicated pod.

1. Use the file [redis-slave-controller.json](redis-slave-controller.json) to create the replication controller by running the `kubectl create -f` *`filename`* command:

    ```console
    $ kubectl create -f examples/guestbook-go/redis-slave-controller.json
    replicationcontrollers/redis-slave
    ```

2. To verify that the redis-slave controller is running, run the `kubectl get rc` command:

    ```console
    $ kubectl get rc
    CONTROLLER              CONTAINER(S)            IMAGE(S)                         SELECTOR                    REPLICAS
    redis-master            redis-master            redis                            app=redis,role=master       1
    redis-slave             redis-slave             kubernetes/redis-slave:v2        app=redis,role=slave        2
    ...
    ```

    Result: The replication controller creates and configures the Redis slave pods through the redis-master service (name:port pair, in our example that's `redis-master:6379`).

    Example:
    The Redis slaves get started by the replication controller with the following command:

    ```console
    redis-server --slaveof redis-master 6379
    ```

3. To verify that the Redis master and slaves pods are running, run the `kubectl get pods` command:

    ```console
    $ kubectl get pods
    NAME                          READY     STATUS    RESTARTS   AGE
    redis-master-xx4uv            1/1       Running   0          18m
    redis-slave-b6wj4             1/1       Running   0          1m
    redis-slave-iai40             1/1       Running   0          1m
    ...
    ```

    Result: You see the single Redis master and two Redis slave pods.

### Step Four: Create the Redis slave service <a id="step-four"></a>

Just like the master, we want to have a service to proxy connections to the read slaves. In this case, in addition to discovery, the Redis slave service provides transparent load balancing to clients.

1. Use the [redis-slave-service.json](redis-slave-service.json) file to create the Redis slave service by running the `kubectl create -f` *`filename`* command:

    ```console
    $ kubectl create -f examples/guestbook-go/redis-slave-service.json
    services/redis-slave
    ```

2. To verify that the redis-slave service is up, list the services you created in the cluster with the `kubectl get services` command:

    ```console
    $ kubectl get services
    NAME              CLUSTER_IP       EXTERNAL_IP       PORT(S)       SELECTOR               AGE
    redis-master      10.0.136.3       <none>            6379/TCP      app=redis,role=master  1h
    redis-slave       10.0.21.92       <none>            6379/TCP      app-redis,role=slave   1h
    ...
    ```

    Result: The service is created with labels `app=redis` and `role=slave` to identify that the pods are running the Redis slaves.

Tip: It is helpful to set labels on your services themselves--as we've done here--to make it easy to locate them later.

### Step Five: Create the guestbook pods <a id="step-five"></a>

This is a simple Go `net/http` ([negroni](https://github.com/codegangsta/negroni) based) server that is configured to talk to either the slave or master services depending on whether the request is a read or a write. The pods we are creating expose a simple JSON interface and serves a jQuery-Ajax based UI. Like the Redis read slaves, these pods are also managed by a replication controller.

1. Use the [guestbook-controller.json](guestbook-controller.json) file to create the guestbook replication controller by running the `kubectl create -f` *`filename`* command:

    ```console
    $ kubectl create -f examples/guestbook-go/guestbook-controller.json
    replicationcontrollers/guestbook
    ```

 Tip: If you want to modify the guestbook code open the `_src` of this example and read the README.md and the Makefile. If you have pushed your custom image be sure to update the `image` accordingly in the guestbook-controller.json.

2. To verify that the guestbook replication controller is running, run the `kubectl get rc` command:

    ```console
    $ kubectl get rc
    CONTROLLER            CONTAINER(S)         IMAGE(S)                               SELECTOR                  REPLICAS
    guestbook             guestbook            gcr.io/google_containers/guestbook:v3  app=guestbook             3
    redis-master          redis-master         redis                                  app=redis,role=master     1
    redis-slave           redis-slave          kubernetes/redis-slave:v2              app=redis,role=slave      2
    ...
    ```

3. To verify that the guestbook pods are running (it might take up to thirty seconds to create the pods), list the pods you created in cluster with the `kubectl get pods` command:

    ```console
    $ kubectl get pods
    NAME                           READY     STATUS    RESTARTS   AGE
    guestbook-3crgn                1/1       Running   0          2m
    guestbook-gv7i6                1/1       Running   0          2m
    guestbook-x405a                1/1       Running   0          2m
    redis-master-xx4uv             1/1       Running   0          23m
    redis-slave-b6wj4              1/1       Running   0          6m
    redis-slave-iai40              1/1       Running   0          6m
    ... 
    ```

    Result: You see a single Redis master, two Redis slaves, and three guestbook pods.

### Step Six: Create the guestbook service <a id="step-six"></a>

Just like the others, we create a service to group the guestbook pods but this time, to make the guestbook front-end externally visible, we specify `"type": "LoadBalancer"`.

1. Use the [guestbook-service.json](guestbook-service.json) file to create the guestbook service by running the `kubectl create -f` *`filename`* command:

    ```console
    $ kubectl create -f examples/guestbook-go/guestbook-service.json
    ```


2. To verify that the guestbook service is up, list the services you created in the cluster with the `kubectl get services` command:

    ```console
    $ kubectl get services
    NAME              CLUSTER_IP       EXTERNAL_IP       PORT(S)       SELECTOR               AGE
    guestbook         10.0.217.218     146.148.81.8      3000/TCP      app=guestbook          1h
    redis-master      10.0.136.3       <none>            6379/TCP      app=redis,role=master  1h
    redis-slave       10.0.21.92       <none>            6379/TCP      app-redis,role=slave   1h
    ...
    ```

    Result: The service is created with label `app=guestbook`.

### Step Seven: View the guestbook <a id="step-seven"></a>

You can now play with the guestbook that you just created by opening it in a browser (it might take a few moments for the guestbook to come up).

 * **Local Host:**
    If you are running Kubernetes locally, to view the guestbook, navigate to `http://localhost:3000` in your browser.

 * **Remote Host:**
    1. To view the guestbook on a remote host, locate the external IP of the load balancer in the **IP** column of the `kubectl get services` output. In our example, the internal IP address is `10.0.217.218` and the external IP address is `146.148.81.8` (*Note: you might need to scroll to see the IP column*).

    2. Append port `3000` to the IP address (for example `http://146.148.81.8:3000`), and then navigate to that address in your browser.

    Result: The guestbook displays in your browser:

    ![Guestbook](guestbook-page.png)

    **Further Reading:**
    If you're using Google Compute Engine, see the details about limiting traffic to specific sources at [Google Compute Engine firewall documentation][gce-firewall-docs].

[cloud-console]: https://console.developer.google.com
[gce-firewall-docs]: https://cloud.google.com/compute/docs/networking#firewalls

### Step Eight: Cleanup <a id="step-eight"></a>

After you're done playing with the guestbook, you can cleanup by deleting the guestbook service and removing the associated resources that were created, including load balancers, forwarding rules, target pools, and Kubernetes replication controllers and services.

Delete all the resources by running the following `kubectl delete -f` *`filename`* command:

```console
$ kubectl delete -f examples/guestbook-go
guestbook-controller
guestbook
redid-master-controller
redis-master
redis-slave-controller
redis-slave
```

Tip: To turn down your Kubernetes cluster, follow the corresponding instructions in the version of the
[Getting Started Guides](https://kubernetes.io/docs/getting-started-guides/) that you previously used to create your cluster.


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/guestbook-go/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
## Java EE Application using WildFly and MySQL

The following document describes the deployment of a Java EE application using [WildFly](http://wildfly.org) application server and MySQL database server on Kubernetes. The sample application source code is at: https://github.com/javaee-samples/javaee7-simple-sample.

### Prerequisites

https://github.com/kubernetes/kubernetes/blob/master/docs/user-guide/prereqs.md

### Start MySQL Pod

In Kubernetes a [_Pod_](https://kubernetes.io/docs/user-guide/pods.md) is the smallest deployable unit that can be created, scheduled, and managed. It's a collocated group of containers that share an IP and storage volume.

Here is the config for MySQL pod: [mysql-pod.yaml](mysql-pod.yaml)

<!-- BEGIN MUNGE: mysql-pod.yaml -->
<!-- END MUNGE: EXAMPLE -->

Create the MySQL pod:

```sh
kubectl create -f examples/javaee/mysql-pod.yaml
```

Check status of the pod:

```sh
kubectl get -w po
NAME        READY     STATUS    RESTARTS   AGE
mysql-pod   0/1       Pending   0          4s
NAME        READY     STATUS    RESTARTS   AGE
mysql-pod   0/1       Running   0          44s
mysql-pod   1/1       Running   0         44s
```

Wait for the status to `1/1` and `Running`.

### Start MySQL Service

We are creating a [_Service_](https://kubernetes.io/docs/user-guide/services.md) to expose the TCP port of the MySQL server. A Service distributes traffic across a set of Pods. The order of Service and the targeted Pods does not matter. However Service needs to be started before any other Pods consuming the Service are started.

In this application, we will use a Kubernetes Service to provide a discoverable endpoints for the MySQL endpoint in the cluster.  MySQL service target pods with the labels `name: mysql-pod` and `context: docker-k8s-lab`.

Here is definition of the MySQL service: [mysql-service.yaml](mysql-service.yaml)

<!-- BEGIN MUNGE: mysql-service.yaml -->
<!-- END MUNGE: EXAMPLE -->

Create this service:

```sh
kubectl create -f examples/javaee/mysql-service.yaml
```

Get status of the service:

```sh
kubectl get -w svc
NAME            LABELS                                    SELECTOR                                IP(S)          PORT(S)
kubernetes      component=apiserver,provider=kubernetes   <none>                                  10.247.0.1     443/TCP
mysql-service   context=docker-k8s-lab,name=mysql-pod     context=docker-k8s-lab,name=mysql-pod   10.247.63.43   3306/TCP
```

If multiple services are running, then it can be narrowed by specifying labels:

```sh
kubectl get -w po -l context=docker-k8s-lab,name=mysql-pod
NAME        READY     STATUS    RESTARTS   AGE
mysql-pod   1/1       Running   0          4m
```

This is also the selector label used by service to target pods.

When a Service is run on a node, the kubelet adds a set of environment variables for each active Service. It supports both Docker links compatible variables and simpler `{SVCNAME}_SERVICE_HOST` and `{SVCNAME}_SERVICE_PORT` variables, where the Service name is upper-cased and dashes are converted to underscores.

Our service name is ``mysql-service'' and so ``MYSQL_SERVICE_SERVICE_HOST'' and ``MYSQL_SERVICE_SERVICE_PORT'' variables are available to other pods. This host and port variables are then used to create the JDBC resource in WildFly.

### Start WildFly Replication Controller

WildFly is a lightweight Java EE 7 compliant application server. It is wrapped in a Replication Controller and used as the Java EE runtime.

In Kubernetes a [_Replication Controller_](https://kubernetes.io/docs/user-guide/replication-controller.md) is responsible for replicating sets of identical pods. Like a _Service_ it has a selector query which identifies the members of it's set.  Unlike a service it also has a desired number of replicas, and it will create or delete pods to ensure that the number of pods matches up with it's desired state.

Here is definition of the MySQL service: [wildfly-rc.yaml](wildfly-rc.yaml).

<!-- BEGIN MUNGE: wildfly-rc.yaml -->
<!-- END MUNGE: EXAMPLE -->

Create this controller:

```sh
kubectl create -f examples/javaee/wildfly-rc.yaml
```

Check status of the pod inside replication controller:

```sh
kubectl get po
NAME               READY     STATUS    RESTARTS   AGE
mysql-pod          1/1       Running   0          1h
wildfly-rc-w2kk5   1/1       Running   0          6m
```

### Access the application

Get IP address of the pod:

```sh
kubectl get -o template po wildfly-rc-w2kk5 --template={{.status.podIP}}
10.246.1.23
```

Log in to node and access the application:

```sh
vagrant ssh node-1
Last login: Thu Jul 16 00:24:36 2015 from 10.0.2.2
[vagrant@kubernetes-node-1 ~]$ curl http://10.246.1.23:8080/employees/resources/employees/
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><collection><employee><id>1</id><name>Penny</name></employee><employee><id>2</id><name>Sheldon</name></employee><employee><id>3</id><name>Amy</name></employee><employee><id>4</id><name>Leonard</name></employee><employee><id>5</id><name>Bernadette</name></employee><employee><id>6</id><name>Raj</name></employee><employee><id>7</id><name>Howard</name></employee><employee><id>8</id><name>Priya</name></employee></collection>
```

### Delete resources

All resources created in this application can be deleted:

```sh
kubectl delete -f examples/javaee/mysql-pod.yaml
kubectl delete -f examples/javaee/mysql-service.yaml
kubectl delete -f examples/javaee/wildfly-rc.yaml
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/javaee/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Elasticsearch for Kubernetes

Kubernetes makes it trivial for anyone to easily build and scale [Elasticsearch](http://www.elasticsearch.org/) clusters. Here, you'll find how to do so.
Current Elasticsearch version is `1.7.1`.

[A more robust example that follows Elasticsearch best-practices of separating nodes concern is also available](production_cluster/README.md).

<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING" width="25" height="25"> Current pod descriptors use an `emptyDir` for storing data in each data node container. This is meant to be for the sake of simplicity and [should be adapted according to your storage needs](https://kubernetes.io/docs/design/persistent-storage.md).

## Docker image

The [pre-built image](https://github.com/pires/docker-elasticsearch-kubernetes) used in this example will not be supported. Feel free to fork to fit your own needs, but keep in mind that you will need to change Kubernetes descriptors accordingly.

## Deploy

Let's kickstart our cluster with 1 instance of Elasticsearch.

```
kubectl create -f examples/elasticsearch/service-account.yaml
kubectl create -f examples/elasticsearch/es-svc.yaml
kubectl create -f examples/elasticsearch/es-rc.yaml
```

Let's see if it worked:

```
$ kubectl get pods
NAME             READY     STATUS    RESTARTS   AGE
es-kfymw         1/1       Running   0          7m
kube-dns-p3v1u   3/3       Running   0          19m
```

```
$ kubectl logs es-kfymw
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
[2015-08-30 10:01:31,946][INFO ][node                     ] [Hammerhead] version[1.7.1], pid[7], build[b88f43f/2015-07-29T09:54:16Z]
[2015-08-30 10:01:31,946][INFO ][node                     ] [Hammerhead] initializing ...
[2015-08-30 10:01:32,110][INFO ][plugins                  ] [Hammerhead] loaded [cloud-kubernetes], sites []
[2015-08-30 10:01:32,153][INFO ][env                      ] [Hammerhead] using [1] data paths, mounts [[/data (/dev/sda9)]], net usable_space [14.4gb], net total_space [15.5gb], types [ext4]
[2015-08-30 10:01:37,188][INFO ][node                     ] [Hammerhead] initialized
[2015-08-30 10:01:37,189][INFO ][node                     ] [Hammerhead] starting ...
[2015-08-30 10:01:37,499][INFO ][transport                ] [Hammerhead] bound_address {inet[/0:0:0:0:0:0:0:0:9300]}, publish_address {inet[/10.244.48.2:9300]}
[2015-08-30 10:01:37,550][INFO ][discovery                ] [Hammerhead] myesdb/n2-6uu_UT3W5XNrjyqBPiA
[2015-08-30 10:01:43,966][INFO ][cluster.service          ] [Hammerhead] new_master [Hammerhead][n2-6uu_UT3W5XNrjyqBPiA][es-kfymw][inet[/10.244.48.2:9300]]{master=true}, reason: zen-disco-join (elected_as_master)
[2015-08-30 10:01:44,010][INFO ][http                     ] [Hammerhead] bound_address {inet[/0:0:0:0:0:0:0:0:9200]}, publish_address {inet[/10.244.48.2:9200]}
[2015-08-30 10:01:44,011][INFO ][node                     ] [Hammerhead] started
[2015-08-30 10:01:44,042][INFO ][gateway                  ] [Hammerhead] recovered [0] indices into cluster_state
```

So we have a 1-node Elasticsearch cluster ready to handle some work.

## Scale

Scaling is as easy as:

```
kubectl scale --replicas=3 rc es
```

Did it work?

```
$ kubectl get pods
NAME             READY     STATUS    RESTARTS   AGE
es-78e0s         1/1       Running   0          8m
es-kfymw         1/1       Running   0          17m
es-rjmer         1/1       Running   0          8m
kube-dns-p3v1u   3/3       Running   0          30m
```

Let's take a look at logs:

```
$ kubectl logs es-kfymw
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
[2015-08-30 10:01:31,946][INFO ][node                     ] [Hammerhead] version[1.7.1], pid[7], build[b88f43f/2015-07-29T09:54:16Z]
[2015-08-30 10:01:31,946][INFO ][node                     ] [Hammerhead] initializing ...
[2015-08-30 10:01:32,110][INFO ][plugins                  ] [Hammerhead] loaded [cloud-kubernetes], sites []
[2015-08-30 10:01:32,153][INFO ][env                      ] [Hammerhead] using [1] data paths, mounts [[/data (/dev/sda9)]], net usable_space [14.4gb], net total_space [15.5gb], types [ext4]
[2015-08-30 10:01:37,188][INFO ][node                     ] [Hammerhead] initialized
[2015-08-30 10:01:37,189][INFO ][node                     ] [Hammerhead] starting ...
[2015-08-30 10:01:37,499][INFO ][transport                ] [Hammerhead] bound_address {inet[/0:0:0:0:0:0:0:0:9300]}, publish_address {inet[/10.244.48.2:9300]}
[2015-08-30 10:01:37,550][INFO ][discovery                ] [Hammerhead] myesdb/n2-6uu_UT3W5XNrjyqBPiA
[2015-08-30 10:01:43,966][INFO ][cluster.service          ] [Hammerhead] new_master [Hammerhead][n2-6uu_UT3W5XNrjyqBPiA][es-kfymw][inet[/10.244.48.2:9300]]{master=true}, reason: zen-disco-join (elected_as_master)
[2015-08-30 10:01:44,010][INFO ][http                     ] [Hammerhead] bound_address {inet[/0:0:0:0:0:0:0:0:9200]}, publish_address {inet[/10.244.48.2:9200]}
[2015-08-30 10:01:44,011][INFO ][node                     ] [Hammerhead] started
[2015-08-30 10:01:44,042][INFO ][gateway                  ] [Hammerhead] recovered [0] indices into cluster_state
[2015-08-30 10:08:02,517][INFO ][cluster.service          ] [Hammerhead] added {[Tenpin][2gv5MiwhRiOSsrTOF3DhuA][es-78e0s][inet[/10.244.54.4:9300]]{master=true},}, reason: zen-disco-receive(join from node[[Tenpin][2gv5MiwhRiOSsrTOF3DhuA][es-78e0s][inet[/10.244.54.4:9300]]{master=true}])
[2015-08-30 10:10:10,645][INFO ][cluster.service          ] [Hammerhead] added {[Evilhawk][ziTq2PzYRJys43rNL2tbyg][es-rjmer][inet[/10.244.33.3:9300]]{master=true},}, reason: zen-disco-receive(join from node[[Evilhawk][ziTq2PzYRJys43rNL2tbyg][es-rjmer][inet[/10.244.33.3:9300]]{master=true}])
```

So we have a 3-node Elasticsearch cluster ready to handle more work.

## Access the service

*Don't forget* that services in Kubernetes are only accessible from containers in the cluster. For different behavior you should [configure the creation of an external load-balancer](http://kubernetes.io/v1.0/docs/user-guide/services.html#type-loadbalancer). While it's supported within this example service descriptor, its usage is out of scope of this document, for now.

```
$ kubectl get service elasticsearch
NAME            LABELS                    SELECTOR                  IP(S)           PORT(S)
elasticsearch   component=elasticsearch   component=elasticsearch   10.100.108.94   9200/TCP
                                                                                    9300/TCP
```

From any host on your cluster (that's running `kube-proxy`), run:

```
$ curl 10.100.108.94:9200
```

You should see something similar to the following:


```json
{
  "status" : 200,
  "name" : "Hammerhead",
  "cluster_name" : "myesdb",
  "version" : {
    "number" : "1.7.1",
    "build_hash" : "b88f43fc40b0bcd7f173a1f9ee2e97816de80b19",
    "build_timestamp" : "2015-07-29T09:54:16Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.4"
  },
  "tagline" : "You Know, for Search"
}
```

Or if you want to check cluster information:


```
curl 10.100.108.94:9200/_cluster/health?pretty
```

You should see something similar to the following:

```json
{
  "cluster_name" : "myesdb",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 3,
  "active_primary_shards" : 0,
  "active_shards" : 0,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0
}
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/elasticsearch/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Elasticsearch for Kubernetes

Kubernetes makes it trivial for anyone to easily build and scale [Elasticsearch](http://www.elasticsearch.org/) clusters. Here, you'll find how to do so.
Current Elasticsearch version is `1.7.1`.

Before we start, one needs to know that Elasticsearch best-practices recommend to separate nodes in three roles:
* `Master` nodes - intended for clustering management only, no data, no HTTP API
* `Client` nodes - intended for client usage, no data, with HTTP API
* `Data` nodes - intended for storing and indexing your data, no HTTP API

This is enforced throughout this document.

<img src="http://kubernetes.io/kubernetes/img/warning.png" alt="WARNING" width="25" height="25"> Current pod descriptors use an `emptyDir` for storing data in each data node container. This is meant to be for the sake of simplicity and [should be adapted according to your storage needs](https://kubernetes.io/docs/design/persistent-storage.md).

## Docker image

This example uses [this pre-built image](https://github.com/pires/docker-elasticsearch-kubernetes). Feel free to fork and update it to fit your own needs, but keep in mind that you will need to change Kubernetes descriptors accordingly.

## Deploy

```
kubectl create -f examples/elasticsearch/production_cluster/service-account.yaml
kubectl create -f examples/elasticsearch/production_cluster/es-discovery-svc.yaml
kubectl create -f examples/elasticsearch/production_cluster/es-svc.yaml
kubectl create -f examples/elasticsearch/production_cluster/es-master-rc.yaml
```

Wait until `es-master` is provisioned, and

```
kubectl create -f examples/elasticsearch/production_cluster/es-client-rc.yaml
```

Wait until `es-client` is provisioned, and

```
kubectl create -f examples/elasticsearch/production_cluster/es-data-rc.yaml
```

Wait until `es-data` is provisioned.

Now, I leave up to you how to validate the cluster, but a first step is to wait for containers to be in ```RUNNING``` state and check the Elasticsearch master logs:

```
$ kubectl get pods
NAME              READY     STATUS    RESTARTS   AGE
es-client-2ep9o   1/1       Running   0          2m
es-data-r9tgv     1/1       Running   0          1m
es-master-vxl6c   1/1       Running   0          6m
```

```
$ kubectl logs es-master-vxl6c
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
[2015-08-21 10:58:51,324][INFO ][node                     ] [Arc] version[1.7.1], pid[8], build[b88f43f/2015-07-29T09:54:16Z]
[2015-08-21 10:58:51,328][INFO ][node                     ] [Arc] initializing ...
[2015-08-21 10:58:51,542][INFO ][plugins                  ] [Arc] loaded [cloud-kubernetes], sites []
[2015-08-21 10:58:51,624][INFO ][env                      ] [Arc] using [1] data paths, mounts [[/data (/dev/sda9)]], net usable_space [14.4gb], net total_space [15.5gb], types [ext4]
[2015-08-21 10:58:57,439][INFO ][node                     ] [Arc] initialized
[2015-08-21 10:58:57,439][INFO ][node                     ] [Arc] starting ...
[2015-08-21 10:58:57,782][INFO ][transport                ] [Arc] bound_address {inet[/0:0:0:0:0:0:0:0:9300]}, publish_address {inet[/10.244.15.2:9300]}
[2015-08-21 10:58:57,847][INFO ][discovery                ] [Arc] myesdb/-x16XFUzTCC8xYqWoeEOYQ
[2015-08-21 10:59:05,167][INFO ][cluster.service          ] [Arc] new_master [Arc][-x16XFUzTCC8xYqWoeEOYQ][es-master-vxl6c][inet[/10.244.15.2:9300]]{data=false, master=true}, reason: zen-disco-join (elected_as_master)
[2015-08-21 10:59:05,202][INFO ][node                     ] [Arc] started
[2015-08-21 10:59:05,238][INFO ][gateway                  ] [Arc] recovered [0] indices into cluster_state
[2015-08-21 11:02:28,797][INFO ][cluster.service          ] [Arc] added {[Gideon][4EfhWSqaTqikbK4tI7bODA][es-data-r9tgv][inet[/10.244.59.4:9300]]{master=false},}, reason: zen-disco-receive(join from node[[Gideon][4EfhWSqaTqikbK4tI7bODA][es-data-r9tgv][inet[/10.244.59.4:9300]]{master=false}])
[2015-08-21 11:03:16,822][INFO ][cluster.service          ] [Arc] added {[Venomm][tFYxwgqGSpOejHLG4umRqg][es-client-2ep9o][inet[/10.244.53.2:9300]]{data=false, master=false},}, reason: zen-disco-receive(join from node[[Venomm][tFYxwgqGSpOejHLG4umRqg][es-client-2ep9o][inet[/10.244.53.2:9300]]{data=false, master=false}])
```

As you can assert, the cluster is up and running. Easy, wasn't it?

## Scale

Scaling each type of node to handle your cluster is as easy as:

```
kubectl scale --replicas=3 rc es-master
kubectl scale --replicas=2 rc es-client
kubectl scale --replicas=2 rc es-data
```

Did it work?

```
$ kubectl get pods
NAME              READY     STATUS    RESTARTS   AGE
es-client-2ep9o   1/1       Running   0          4m
es-client-ye5s1   1/1       Running   0          50s
es-data-8az22     1/1       Running   0          47s
es-data-r9tgv     1/1       Running   0          3m
es-master-57h7k   1/1       Running   0          52s
es-master-kuwse   1/1       Running   0          52s
es-master-vxl6c   1/1       Running   0          8m
```

Let's take another look of the Elasticsearch master logs:

```
$ kubectl logs es-master-vxl6c
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
log4j:WARN No such property [maxBackupIndex] in org.apache.log4j.DailyRollingFileAppender.
[2015-08-21 10:58:51,324][INFO ][node                     ] [Arc] version[1.7.1], pid[8], build[b88f43f/2015-07-29T09:54:16Z]
[2015-08-21 10:58:51,328][INFO ][node                     ] [Arc] initializing ...
[2015-08-21 10:58:51,542][INFO ][plugins                  ] [Arc] loaded [cloud-kubernetes], sites []
[2015-08-21 10:58:51,624][INFO ][env                      ] [Arc] using [1] data paths, mounts [[/data (/dev/sda9)]], net usable_space [14.4gb], net total_space [15.5gb], types [ext4]
[2015-08-21 10:58:57,439][INFO ][node                     ] [Arc] initialized
[2015-08-21 10:58:57,439][INFO ][node                     ] [Arc] starting ...
[2015-08-21 10:58:57,782][INFO ][transport                ] [Arc] bound_address {inet[/0:0:0:0:0:0:0:0:9300]}, publish_address {inet[/10.244.15.2:9300]}
[2015-08-21 10:58:57,847][INFO ][discovery                ] [Arc] myesdb/-x16XFUzTCC8xYqWoeEOYQ
[2015-08-21 10:59:05,167][INFO ][cluster.service          ] [Arc] new_master [Arc][-x16XFUzTCC8xYqWoeEOYQ][es-master-vxl6c][inet[/10.244.15.2:9300]]{data=false, master=true}, reason: zen-disco-join (elected_as_master)
[2015-08-21 10:59:05,202][INFO ][node                     ] [Arc] started
[2015-08-21 10:59:05,238][INFO ][gateway                  ] [Arc] recovered [0] indices into cluster_state
[2015-08-21 11:02:28,797][INFO ][cluster.service          ] [Arc] added {[Gideon][4EfhWSqaTqikbK4tI7bODA][es-data-r9tgv][inet[/10.244.59.4:9300]]{master=false},}, reason: zen-disco-receive(join from node[[Gideon][4EfhWSqaTqikbK4tI7bODA][es-data-r9tgv][inet[/10.244.59.4:9300]]{master=false}])
[2015-08-21 11:03:16,822][INFO ][cluster.service          ] [Arc] added {[Venomm][tFYxwgqGSpOejHLG4umRqg][es-client-2ep9o][inet[/10.244.53.2:9300]]{data=false, master=false},}, reason: zen-disco-receive(join from node[[Venomm][tFYxwgqGSpOejHLG4umRqg][es-client-2ep9o][inet[/10.244.53.2:9300]]{data=false, master=false}])
[2015-08-21 11:04:40,781][INFO ][cluster.service          ] [Arc] added {[Erik Josten][QUJlahfLTi-MsxzM6_Da0g][es-master-kuwse][inet[/10.244.59.5:9300]]{data=false, master=true},}, reason: zen-disco-receive(join from node[[Erik Josten][QUJlahfLTi-MsxzM6_Da0g][es-master-kuwse][inet[/10.244.59.5:9300]]{data=false, master=true}])
[2015-08-21 11:04:41,076][INFO ][cluster.service          ] [Arc] added {[Power Princess][V4qnR-6jQOS5ovXQsPgo7g][es-master-57h7k][inet[/10.244.53.3:9300]]{data=false, master=true},}, reason: zen-disco-receive(join from node[[Power Princess][V4qnR-6jQOS5ovXQsPgo7g][es-master-57h7k][inet[/10.244.53.3:9300]]{data=false, master=true}])
[2015-08-21 11:04:53,966][INFO ][cluster.service          ] [Arc] added {[Cagliostro][Wpfx5fkBRiG2qCEWd8laaQ][es-client-ye5s1][inet[/10.244.15.3:9300]]{data=false, master=false},}, reason: zen-disco-receive(join from node[[Cagliostro][Wpfx5fkBRiG2qCEWd8laaQ][es-client-ye5s1][inet[/10.244.15.3:9300]]{data=false, master=false}])
[2015-08-21 11:04:56,803][INFO ][cluster.service          ] [Arc] added {[Thog][vkdEtX3ESfWmhXXf-Wi0_Q][es-data-8az22][inet[/10.244.15.4:9300]]{master=false},}, reason: zen-disco-receive(join from node[[Thog][vkdEtX3ESfWmhXXf-Wi0_Q][es-data-8az22][inet[/10.244.15.4:9300]]{master=false}])
```

## Access the service

*Don't forget* that services in Kubernetes are only accessible from containers in the cluster. For different behavior you should [configure the creation of an external load-balancer](http://kubernetes.io/v1.0/docs/user-guide/services.html#type-loadbalancer). While it's supported within this example service descriptor, its usage is out of scope of this document, for now.

```
$ kubectl get service elasticsearch
NAME            LABELS                                SELECTOR                              IP(S)          PORT(S)
elasticsearch   component=elasticsearch,role=client   component=elasticsearch,role=client   10.100.134.2   9200/TCP
```

From any host on your cluster (that's running `kube-proxy`), run:

```
curl http://10.100.134.2:9200
```

You should see something similar to the following:


```json
{
  "status" : 200,
  "name" : "Cagliostro",
  "cluster_name" : "myesdb",
  "version" : {
    "number" : "1.7.1",
    "build_hash" : "b88f43fc40b0bcd7f173a1f9ee2e97816de80b19",
    "build_timestamp" : "2015-07-29T09:54:16Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.4"
  },
  "tagline" : "You Know, for Search"
}
```

Or if you want to check cluster information:


```
curl http://10.100.134.2:9200/_cluster/health?pretty
```

You should see something similar to the following:

```json
{
  "cluster_name" : "myesdb",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 7,
  "number_of_data_nodes" : 2,
  "active_primary_shards" : 0,
  "active_shards" : 0,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0
}
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/elasticsearch/production_cluster/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
Meteor on Kubernetes
====================

This example shows you how to package and run a
[Meteor](https://www.meteor.com/) app on Kubernetes.

Get started on Google Compute Engine
------------------------------------

Meteor uses MongoDB, and we will use the `GCEPersistentDisk` type of
volume for persistent storage. Therefore, this example is only
applicable to [Google Compute
Engine](https://cloud.google.com/compute/). Take a look at the
[volumes documentation](https://kubernetes.io/docs/user-guide/volumes.md) for other options.

First, if you have not already done so:

1. [Create](https://cloud.google.com/compute/docs/quickstart) a
[Google Cloud Platform](https://cloud.google.com/) project.
2. [Enable
billing](https://developers.google.com/console/help/new/#billing).
3. Install the [gcloud SDK](https://cloud.google.com/sdk/).

Authenticate with gcloud and set the gcloud default project name to
point to the project you want to use for your Kubernetes cluster:

```sh
gcloud auth login
gcloud config set project <project-name>
```

Next, start up a Kubernetes cluster:

```sh
wget -q -O - https://get.k8s.io | bash
```

Please see the [Google Compute Engine getting started
guide](https://kubernetes.io/docs/getting-started-guides/gce.md) for full
details and other options for starting a cluster.

Build a container for your Meteor app
-------------------------------------

To be able to run your Meteor app on Kubernetes you need to build a
Docker container for it first. To do that you need to install
[Docker](https://www.docker.com) Once you have that you need to add 2
files to your existing Meteor project `Dockerfile` and
`.dockerignore`.

`Dockerfile` should contain the below lines. You should replace the
`ROOT_URL` with the actual hostname of your app.

```
FROM chees/meteor-kubernetes
ENV ROOT_URL http://myawesomeapp.com
```

The `.dockerignore` file should contain the below lines. This tells
Docker to ignore the files on those directories when it's building
your container.

```
.meteor/local
packages/*/.build*
```

You can see an example meteor project already set up at:
[meteor-gke-example](https://github.com/Q42/meteor-gke-example). Feel
free to use this app for this example.

> Note: The next step will not work if you have added mobile platforms
> to your meteor project. Check with `meteor list-platforms`

Now you can build your container by running this in
your Meteor project directory:

```
docker build -t my-meteor .
```

Pushing to a registry
---------------------

For the [Docker Hub](https://hub.docker.com/), tag your app image with
your username and push to the Hub with the below commands. Replace
`<username>` with your Hub username.

```
docker tag my-meteor <username>/my-meteor
docker push <username>/my-meteor
```

For [Google Container
Registry](https://cloud.google.com/tools/container-registry/), tag
your app image with your project ID, and push to GCR. Replace
`<project>` with your project ID.

```
docker tag my-meteor gcr.io/<project>/my-meteor
gcloud docker -- push gcr.io/<project>/my-meteor
```

Running
-------

Now that you have containerized your Meteor app it's time to set up
your cluster. Edit [`meteor-controller.json`](meteor-controller.json)
and make sure the `image:` points to the container you just pushed to
the Docker Hub or GCR.

We will need to provide MongoDB a persistent Kubernetes volume to
store its data. See the [volumes documentation](https://kubernetes.io/docs/user-guide/volumes.md) for
options. We're going to use Google Compute Engine persistent
disks. Create the MongoDB disk by running:

```
gcloud compute disks create --size=200GB mongo-disk
```

Now you can start Mongo using that disk:

```
kubectl create -f examples/meteor/mongo-pod.json
kubectl create -f examples/meteor/mongo-service.json
```

Wait until Mongo is started completely and then start up your Meteor app:

```
kubectl create -f examples/meteor/meteor-service.json
kubectl create -f examples/meteor/meteor-controller.json
```

Note that [`meteor-service.json`](meteor-service.json) creates a load balancer, so
your app should be available through the IP of that load balancer once
the Meteor pods are started. We also created the service before creating the rc to
aid the scheduler in placing pods, as the scheduler ranks pod placement according to
service anti-affinity (among other things). You can find the IP of your load balancer
by running:

```
kubectl get service meteor --template="{{range .status.loadBalancer.ingress}} {{.ip}} {{end}}"
```

You will have to open up port 80 if it's not open yet in your
environment. On Google Compute Engine, you may run the below command.

```
gcloud compute firewall-rules create meteor-80 --allow=tcp:80 --target-tags kubernetes-node
```

What is going on?
-----------------

Firstly, the `FROM chees/meteor-kubernetes` line in your `Dockerfile`
specifies the base image for your Meteor app. The code for that image
is located in the `dockerbase/` subdirectory. Open up the `Dockerfile`
to get an insight of what happens during the `docker build` step. The
image is based on the Node.js official image. It then installs Meteor
and copies in your apps' code. The last line specifies what happens
when your app container is run.

```sh
ENTRYPOINT MONGO_URL=mongodb://$MONGO_SERVICE_HOST:$MONGO_SERVICE_PORT /usr/local/bin/node main.js
```

Here we can see the MongoDB host and port information being passed
into the Meteor app. The `MONGO_SERVICE...` environment variables are
set by Kubernetes, and point to the service named `mongo` specified in
[`mongo-service.json`](mongo-service.json). See the [environment
documentation](https://kubernetes.io/docs/user-guide/container-environment.md) for more details.

As you may know, Meteor uses long lasting connections, and requires
_sticky sessions_. With Kubernetes you can scale out your app easily
with session affinity. The
[`meteor-service.json`](meteor-service.json) file contains
`"sessionAffinity": "ClientIP"`, which provides this for us. See the
[service
documentation](https://kubernetes.io/docs/user-guide/services.md#virtual-ips-and-service-proxies) for
more information.

As mentioned above, the mongo container uses a volume which is mapped
to a persistent disk by Kubernetes. In [`mongo-pod.json`](mongo-pod.json) the container
section specifies the volume:

```json
{
        "volumeMounts": [
          {
            "name": "mongo-disk",
            "mountPath": "/data/db"
          }
```

The name `mongo-disk` refers to the volume specified outside the
container section:

```json
{
    "volumes": [
      {
        "name": "mongo-disk",
        "gcePersistentDisk": {
          "pdName": "mongo-disk",
          "fsType": "ext4"
        }
      }
    ],
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/meteor/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
Building the meteor-kubernetes base image
-----------------------------------------

As a normal user you don't need to do this since the image is already built and pushed to Docker Hub. You can just use it as a base image. See [this example](https://github.com/Q42/meteor-gke-example/blob/master/Dockerfile).

To build and push the base meteor-kubernetes image:

    docker build -t chees/meteor-kubernetes .
    docker push chees/meteor-kubernetes


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/meteor/dockerbase/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# CockroachDB on Kubernetes as a StatefulSet

This example deploys [CockroachDB](https://cockroachlabs.com) on Kubernetes as
a StatefulSet. CockroachDB is a distributed, scalable NewSQL database. Please see
[the homepage](https://cockroachlabs.com) and the
[documentation](https://www.cockroachlabs.com/docs/) for details.

## Limitations

### StatefulSet limitations

Standard StatefulSet limitations apply: There is currently no possibility to use
node-local storage (outside of single-node tests), and so there is likely
a performance hit associated with running CockroachDB on some external storage.
Note that CockroachDB already does replication and thus it is unnecessary to
deploy it onto persistent volumes which already replicate internally.
For this reason, high-performance use cases on a private Kubernetes cluster
may want to consider a DaemonSet deployment until Stateful Sets support node-local
storage (see #7562).

### Recovery after persistent storage failure

A persistent storage failure (e.g. losing the hard drive) is gracefully handled
by CockroachDB as long as enough replicas survive (two out of three by
default). Due to the bootstrapping in this deployment, a storage failure of the
first node is special in that the administrator must manually prepopulate the
"new" storage medium by running an instance of CockroachDB with the `--join`
parameter. If this is not done, the first node will bootstrap a new cluster,
which will lead to a lot of trouble.

### Dynamic volume provisioning

The deployment is written for a use case in which dynamic volume provisioning is
available. When that is not the case, the persistent volume claims need
to be created manually. See [minikube.sh](minikube.sh) for the necessary
steps. If you're on GCE or AWS, where dynamic provisioning is supported, no
manual work is needed to create the persistent volumes.

## Testing locally on minikube

Follow the steps in [minikube.sh](minikube.sh) (or simply run that file).

## Testing in the cloud on GCE or AWS

Once you have a Kubernetes cluster running, just run
`kubectl create -f cockroachdb-statefulset.yaml` to create your cockroachdb cluster.
This works because GCE and AWS support dynamic volume provisioning by default,
so persistent volumes will be created for the CockroachDB pods as needed.

## Accessing the database

Along with our StatefulSet configuration, we expose a standard Kubernetes service
that offers a load-balanced virtual IP for clients to access the database
with. In our example, we've called this service `cockroachdb-public`.

Start up a client pod and open up an interactive, (mostly) Postgres-flavor
SQL shell using:

```console
$ kubectl run -it --rm cockroach-client --image=cockroachdb/cockroach --restart=Never --command -- ./cockroach sql --host cockroachdb-public --insecure
```

You can see example SQL statements for inserting and querying data in the
included [demo script](demo.sh), but can use almost any Postgres-style SQL
commands. Some more basic examples can be found within
[CockroachDB's documentation](https://www.cockroachlabs.com/docs/learn-cockroachdb-sql.html).

## Accessing the admin UI

If you want to see information about how the cluster is doing, you can try
pulling up the CockroachDB admin UI by port-forwarding from your local machine
to one of the pods:

```shell
kubectl port-forward cockroachdb-0 8080
```

Once you’ve done that, you should be able to access the admin UI by visiting
http://localhost:8080/ in your web browser.

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

Scale the Stateful Set by running

```shell
kubectl scale statefulset cockroachdb --replicas=4
```

Note that you may need to create a new persistent volume claim first. If you
ran `minikube.sh`, there's a spare volume so you can immediately scale up by
one. If you're running on GCE or AWS, you can scale up by as many as you want
because new volumes will automatically be created for you. Convince yourself
that the new node immediately serves reads and writes.

## Cleaning up when you're done

Because all of the resources in this example have been tagged with the label `app=cockroachdb`,
we can clean up everything that we created in one quick command using a selector on that label:

```shell
kubectl delete statefulsets,persistentvolumes,persistentvolumeclaims,services,poddisruptionbudget -l app=cockroachdb
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/cockroachdb/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
To access the Kubernetes API [from a Pod](https://kubernetes.io/docs/user-guide/accessing-the-cluster.md#accessing-the-api-from-a-pod) one of the solution is to run `kubectl proxy` in a so-called sidecar container within the Pod. To do this, you need to package `kubectl` in a container. It is useful when service accounts are being used for accessing the API and the old no-auth KUBERNETES_RO service is not available. Since all containers in a Pod share the same network namespace, containers will be able to reach the API on localhost.

This example contains a [Dockerfile](Dockerfile) and [Makefile](Makefile) for packaging up `kubectl` into
a container and pushing the resulting container image on the Google Container Registry. You can modify the Makefile to push to a different registry if needed.

Assuming that you have checked out the Kubernetes source code and setup your environment to be able to build it. The typical build step of this kubectl container will be:

    $ cd examples/kubectl-container
    $ make kubectl
    $ make tag
    $ make container
    $ make push

It is not currently automated as part of a release process, so for the moment
this is an example of what to do if you want to package `kubectl` into a
container and use it within a pod.

In the future, we may release consistently versioned groups of containers when
we cut a release, in which case the source of gcr.io/google_containers/kubectl
would become that automated process.

[```pod.json```](pod.json) is provided as an example of running `kubectl` as a sidecar
container in a Pod, and to help you verify that `kubectl` works correctly in
this configuration. To launch this Pod, you will need a configured Kubernetes endpoint and `kubectl` installed locally, then simply create the Pod:

    $ kubectl create -f pod.json


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/kubectl-container/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->

# Nginx https service

This example creates a basic nginx https service useful in verifying proof of concept, keys, secrets, configmap, and end-to-end https service creation in kubernetes.
It uses an [nginx server block](http://wiki.nginx.org/ServerBlockExample) to serve the index page over both http and https. It will detect changes to nginx's configuration file, default.conf, mounted as a configmap volume and reload nginx automatically.

### Generate certificates

First generate a self signed rsa key and certificate that the server can use for TLS. This step invokes the make_secret.go script in the same directory, which uses the kubernetes api to generate a secret json config in /tmp/secret.json.

```sh
$ make keys secret KEY=/tmp/nginx.key CERT=/tmp/nginx.crt SECRET=/tmp/secret.json
```

### Create a https nginx application running in a kubernetes cluster

You need a [running kubernetes cluster](https://kubernetes.io/docs/setup/pick-right-solution/) for this to work.

Create a secret and a configmap.

```sh
$ kubectl create -f /tmp/secret.json
secret "nginxsecret" created

$ kubectl create configmap nginxconfigmap --from-file=examples/https-nginx/default.conf
configmap "nginxconfigmap" created
```

Create a service and a replication controller using the configuration in nginx-app.yaml.

```sh
$ kubectl create -f examples/https-nginx/nginx-app.yaml
You have exposed your service on an external port on all nodes in your
cluster.  If you want to expose this service to the external internet, you may
need to set up firewall rules for the service port(s) (tcp:32211,tcp:30028) to serve traffic.
...
service "nginxsvc" created
replicationcontroller "my-nginx" created
```

Then, find the node port that Kubernetes is using for http and https traffic.

```sh
$ kubectl get service nginxsvc -o json
...
                    {
                        "name": "http",
                        "protocol": "TCP",
                        "port": 80,
                        "targetPort": 80,
                        "nodePort": 32211
                    },
                    {
                        "name": "https",
                        "protocol": "TCP",
                        "port": 443,
                        "targetPort": 443,
                        "nodePort": 30028
                    }
...
```

If you are using Kubernetes on a cloud provider, you may need to create cloud firewall rules to serve traffic.
If you are using GCE or GKE, you can use the following commands to add firewall rules.

```sh
$ gcloud compute firewall-rules create allow-nginx-http --allow tcp:32211 --description "Incoming http allowed."
Created [https://www.googleapis.com/compute/v1/projects/hello-world-job/global/firewalls/allow-nginx-http].
NAME              NETWORK  SRC_RANGES  RULES      SRC_TAGS  TARGET_TAGS
allow-nginx-http  default  0.0.0.0/0   tcp:32211

$ gcloud compute firewall-rules create allow-nginx-https --allow tcp:30028 --description "Incoming https allowed."
Created [https://www.googleapis.com/compute/v1/projects/hello-world-job/global/firewalls/allow-nginx-https].
NAME               NETWORK  SRC_RANGES  RULES      SRC_TAGS  TARGET_TAGS
allow-nginx-https  default  0.0.0.0/0   tcp:30028
```

Find your nodes' IPs.

```sh
$ kubectl get nodes -o json | grep ExternalIP -A 2
                        "type": "ExternalIP",
                        "address": "104.198.1.26"
                    }
--
                        "type": "ExternalIP",
                        "address": "104.198.12.158"
                    }
--
                        "type": "ExternalIP",
                        "address": "104.198.11.137"
                    }
```

Now your service is up. You can either use your browser or type the following commands.

```sh
$ curl https://<your-node-ip>:<your-port> -k

$ curl https://104.198.1.26:30028 -k
...
<title>Welcome to nginx!</title>
...
```

Then we will update the configmap by changing `index.html` to `index2.html`.

```sh
kubectl create configmap nginxconfigmap --from-file=examples/https-nginx/default.conf -o yaml --dry-run\
| sed 's/index.html/index2.html/g' | kubectl apply -f -
configmap "nginxconfigmap" configured
```

Wait a few seconds to let the change propagate. Now you should be able to either use your browser or type the following commands to verify Nginx has been reloaded with new configuration.

```sh
$ curl https://<your-node-ip>:<your-port> -k

$ curl https://104.198.1.26:30028 -k
...
<title>Nginx reloaded!</title>
...
```

For more information on how to run this in a kubernetes cluster, please see the [user-guide](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/).

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/https-nginx/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Spark example

Following this example, you will create a functional [Apache
Spark](http://spark.apache.org/) cluster using Kubernetes and
[Docker](http://docker.io).

You will setup a Spark master service and a set of Spark workers using Spark's [standalone mode](http://spark.apache.org/docs/latest/spark-standalone.html).

For the impatient expert, jump straight to the [tl;dr](#tldr)
section.

### Sources

The Docker images are heavily based on https://github.com/mattf/docker-spark.
And are curated in https://github.com/kubernetes/application-images/tree/master/spark

The Spark UI Proxy is taken from https://github.com/aseigneurin/spark-ui-proxy.

The PySpark examples are taken from http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python/27946768#27946768

## Step Zero: Prerequisites

This example assumes

- You have a Kubernetes cluster installed and running.
- That you have installed the ```kubectl``` command line tool installed in your path and configured to talk to your Kubernetes cluster
- That your Kubernetes cluster is running [kube-dns](https://github.com/kubernetes/dns) or an equivalent integration.

Optionally, your Kubernetes cluster should be configured with a Loadbalancer integration (automatically configured via kube-up or GKE)

## Step One: Create namespace

```sh
$ kubectl create -f examples/spark/namespace-spark-cluster.yaml
```

Now list all namespaces:

```sh
$ kubectl get namespaces
NAME          LABELS             STATUS
default       <none>             Active
spark-cluster name=spark-cluster Active
```

To configure kubectl to work with our namespace, we will create a new context using our current context as a base:

```sh
$ CURRENT_CONTEXT=$(kubectl config view -o jsonpath='{.current-context}')
$ USER_NAME=$(kubectl config view -o jsonpath='{.contexts[?(@.name == "'"${CURRENT_CONTEXT}"'")].context.user}')
$ CLUSTER_NAME=$(kubectl config view -o jsonpath='{.contexts[?(@.name == "'"${CURRENT_CONTEXT}"'")].context.cluster}')
$ kubectl config set-context spark --namespace=spark-cluster --cluster=${CLUSTER_NAME} --user=${USER_NAME}
$ kubectl config use-context spark
```

## Step Two: Start your Master service

The Master [service](https://kubernetes.io/docs/user-guide/services.md) is the master service
for a Spark cluster.

Use the
[`examples/spark/spark-master-controller.yaml`](spark-master-controller.yaml)
file to create a
[replication controller](https://kubernetes.io/docs/user-guide/replication-controller.md)
running the Spark Master service.

```console
$ kubectl create -f examples/spark/spark-master-controller.yaml
replicationcontroller "spark-master-controller" created
```

Then, use the
[`examples/spark/spark-master-service.yaml`](spark-master-service.yaml) file to
create a logical service endpoint that Spark workers can use to access the
Master pod:

```console
$ kubectl create -f examples/spark/spark-master-service.yaml
service "spark-master" created
```

### Check to see if Master is running and accessible

```console
$ kubectl get pods
NAME                            READY     STATUS    RESTARTS   AGE
spark-master-controller-5u0q5   1/1       Running   0          8m
```

Check logs to see the status of the master. (Use the pod retrieved from the previous output.)

```sh
$ kubectl logs spark-master-controller-5u0q5
starting org.apache.spark.deploy.master.Master, logging to /opt/spark-1.5.1-bin-hadoop2.6/sbin/../logs/spark--org.apache.spark.deploy.master.Master-1-spark-master-controller-g0oao.out
Spark Command: /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -cp /opt/spark-1.5.1-bin-hadoop2.6/sbin/../conf/:/opt/spark-1.5.1-bin-hadoop2.6/lib/spark-assembly-1.5.1-hadoop2.6.0.jar:/opt/spark-1.5.1-bin-hadoop2.6/lib/datanucleus-rdbms-3.2.9.jar:/opt/spark-1.5.1-bin-hadoop2.6/lib/datanucleus-core-3.2.10.jar:/opt/spark-1.5.1-bin-hadoop2.6/lib/datanucleus-api-jdo-3.2.6.jar -Xms1g -Xmx1g org.apache.spark.deploy.master.Master --ip spark-master --port 7077 --webui-port 8080
========================================
15/10/27 21:25:05 INFO Master: Registered signal handlers for [TERM, HUP, INT]
15/10/27 21:25:05 INFO SecurityManager: Changing view acls to: root
15/10/27 21:25:05 INFO SecurityManager: Changing modify acls to: root
15/10/27 21:25:05 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(root); users with modify permissions: Set(root)
15/10/27 21:25:06 INFO Slf4jLogger: Slf4jLogger started
15/10/27 21:25:06 INFO Remoting: Starting remoting
15/10/27 21:25:06 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkMaster@spark-master:7077]
15/10/27 21:25:06 INFO Utils: Successfully started service 'sparkMaster' on port 7077.
15/10/27 21:25:07 INFO Master: Starting Spark master at spark://spark-master:7077
15/10/27 21:25:07 INFO Master: Running Spark version 1.5.1
15/10/27 21:25:07 INFO Utils: Successfully started service 'MasterUI' on port 8080.
15/10/27 21:25:07 INFO MasterWebUI: Started MasterWebUI at http://spark-master:8080
15/10/27 21:25:07 INFO Utils: Successfully started service on port 6066.
15/10/27 21:25:07 INFO StandaloneRestServer: Started REST server for submitting applications on port 6066
15/10/27 21:25:07 INFO Master: I have been elected leader! New state: ALIVE
```

Once the master is started, we'll want to check the Spark WebUI. In order to access the Spark WebUI, we will deploy a [specialized proxy](https://github.com/aseigneurin/spark-ui-proxy). This proxy is neccessary to access worker logs from the Spark UI.

Deploy the proxy controller with [`examples/spark/spark-ui-proxy-controller.yaml`](spark-ui-proxy-controller.yaml):

```console
$ kubectl create -f examples/spark/spark-ui-proxy-controller.yaml
replicationcontroller "spark-ui-proxy-controller" created
```

We'll also need a corresponding Loadbalanced service for our Spark Proxy [`examples/spark/spark-ui-proxy-service.yaml`](spark-ui-proxy-service.yaml):

```console
$ kubectl create -f examples/spark/spark-ui-proxy-service.yaml
service "spark-ui-proxy" created
```

After creating the service, you should eventually get a loadbalanced endpoint:

```console
$ kubectl get svc spark-ui-proxy -o wide
 NAME             CLUSTER-IP    EXTERNAL-IP                                                              PORT(S)   AGE       SELECTOR
spark-ui-proxy   10.0.51.107   aad59283284d611e6839606c214502b5-833417581.us-east-1.elb.amazonaws.com   80/TCP    9m        component=spark-ui-proxy
```

The Spark UI in the above example output will be available at http://aad59283284d611e6839606c214502b5-833417581.us-east-1.elb.amazonaws.com

If your Kubernetes cluster is not equipped with a Loadbalancer integration, you will need to use the [kubectl proxy](https://kubernetes.io/docs/user-guide/accessing-the-cluster.md#using-kubectl-proxy) to
connect to the Spark WebUI:

```console
kubectl proxy --port=8001
```

At which point the UI will be available at
[http://localhost:8001/api/v1/proxy/namespaces/spark-cluster/services/spark-master:8080/](http://localhost:8001/api/v1/proxy/namespaces/spark-cluster/services/spark-master:8080/).

## Step Three: Start your Spark workers

The Spark workers do the heavy lifting in a Spark cluster. They
provide execution resources and data cache capabilities for your
program.

The Spark workers need the Master service to be running.

Use the [`examples/spark/spark-worker-controller.yaml`](spark-worker-controller.yaml) file to create a
[replication controller](https://kubernetes.io/docs/user-guide/replication-controller.md) that manages the worker pods.

```console
$ kubectl create -f examples/spark/spark-worker-controller.yaml
replicationcontroller "spark-worker-controller" created
```

### Check to see if the workers are running

If you launched the Spark WebUI, your workers should just appear in the UI when
they're ready. (It may take a little bit to pull the images and launch the
pods.) You can also interrogate the status in the following way:

```console
$ kubectl get pods
NAME                            READY     STATUS    RESTARTS   AGE
spark-master-controller-5u0q5   1/1       Running   0          25m
spark-worker-controller-e8otp   1/1       Running   0          6m
spark-worker-controller-fiivl   1/1       Running   0          6m
spark-worker-controller-ytc7o   1/1       Running   0          6m

$ kubectl logs spark-master-controller-5u0q5
[...]
15/10/26 18:20:14 INFO Master: Registering worker 10.244.1.13:53567 with 2 cores, 6.3 GB RAM
15/10/26 18:20:14 INFO Master: Registering worker 10.244.2.7:46195 with 2 cores, 6.3 GB RAM
15/10/26 18:20:14 INFO Master: Registering worker 10.244.3.8:39926 with 2 cores, 6.3 GB RAM
```

## Step Four: Start the Zeppelin UI to launch jobs on your Spark cluster

The Zeppelin UI pod can be used to launch jobs into the Spark cluster either via
a web notebook frontend or the traditional Spark command line. See
[Zeppelin](https://zeppelin.incubator.apache.org/) and
[Spark architecture](https://spark.apache.org/docs/latest/cluster-overview.html)
for more details.

Deploy Zeppelin:

```console
$ kubectl create -f examples/spark/zeppelin-controller.yaml
replicationcontroller "zeppelin-controller" created
```

And the corresponding service:

```console
$ kubectl create -f examples/spark/zeppelin-service.yaml
service "zeppelin" created
```

Zeppelin needs the spark-master service to be running.

### Check to see if Zeppelin is running

```console
$ kubectl get pods -l component=zeppelin
NAME                        READY     STATUS    RESTARTS   AGE
zeppelin-controller-ja09s   1/1       Running   0          53s
```

## Step Five: Do something with the cluster

Now you have two choices, depending on your predilections. You can do something
graphical with the Spark cluster, or you can stay in the CLI.

For both choices, we will be working with this Python snippet:

```python
from math import sqrt; from itertools import count, islice

def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

nums = sc.parallelize(xrange(10000000))
print nums.filter(isprime).count()
```

### Do something fast with pyspark!

Simply copy and paste the python snippet into pyspark from within the zeppelin pod:

```console
$ kubectl exec zeppelin-controller-ja09s -it pyspark
Python 2.7.9 (default, Mar  1 2015, 12:57:24)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.5.1
      /_/

Using Python version 2.7.9 (default, Mar  1 2015 12:57:24)
SparkContext available as sc, HiveContext available as sqlContext.
>>> from math import sqrt; from itertools import count, islice
>>>
>>> def isprime(n):
...     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
...
>>> nums = sc.parallelize(xrange(10000000))

>>> print nums.filter(isprime).count()
664579
```

Congratulations, you now know how many prime numbers there are within the first 10 million numbers!

### Do something graphical and shiny!

Creating the Zeppelin service should have yielded you a Loadbalancer endpoint:

```console
$ kubectl get svc zeppelin -o wide
 NAME       CLUSTER-IP   EXTERNAL-IP                                                              PORT(S)   AGE       SELECTOR
zeppelin   10.0.154.1   a596f143884da11e6839506c114532b5-121893930.us-east-1.elb.amazonaws.com   80/TCP    3m        component=zeppelin
```

If your Kubernetes cluster does not have a Loadbalancer integration, then we will have to use port forwarding.

Take the Zeppelin pod from before and port-forward the WebUI port:

```console
$ kubectl port-forward zeppelin-controller-ja09s 8080:8080
```

This forwards `localhost` 8080 to container port 8080. You can then find
Zeppelin at [http://localhost:8080/](http://localhost:8080/).

Once you've loaded up the Zeppelin UI, create a "New Notebook". In there we will paste our python snippet, but we need to add a `%pyspark` hint for Zeppelin to understand it:

```
%pyspark
from math import sqrt; from itertools import count, islice

def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

nums = sc.parallelize(xrange(10000000))
print nums.filter(isprime).count()
```

After pasting in our code, press shift+enter or click the play icon to the right of our snippet. The Spark job will run and once again we'll have our result!

## Result

You now have services and replication controllers for the Spark master, Spark
workers and Spark driver.  You can take this example to the next step and start
using the Apache Spark cluster you just created, see
[Spark documentation](https://spark.apache.org/documentation.html) for more
information.

## tl;dr

```console
kubectl create -f examples/spark
```

After it's setup:

```console
kubectl get pods # Make sure everything is running
kubectl get svc -o wide # Get the Loadbalancer endpoints for spark-ui-proxy and zeppelin
```

At which point the Master UI and Zeppelin will be available at the URLs under the `EXTERNAL-IP` field.

You can also interact with the Spark cluster using the traditional `spark-shell` /
`spark-subsubmit` / `pyspark` commands by using `kubectl exec` against the
`zeppelin-controller` pod.

If your Kubernetes cluster does not have a Loadbalancer integration, use `kubectl proxy` and `kubectl port-forward` to access the Spark UI and Zeppelin.

For Spark UI:

```console
kubectl proxy --port=8001
```

Then visit [http://localhost:8001/api/v1/proxy/namespaces/spark-cluster/services/spark-ui-proxy/](http://localhost:8001/api/v1/proxy/namespaces/spark-cluster/services/spark-ui-proxy/).

For Zeppelin:

```console
kubectl port-forward zeppelin-controller-abc123 8080:8080 &
```

Then visit [http://localhost:8080/](http://localhost:8080/).

## Known Issues With Spark

* This provides a Spark configuration that is restricted to the cluster network,
  meaning the Spark master is only available as a cluster service. If you need
  to submit jobs using external client other than Zeppelin or `spark-submit` on
  the `zeppelin` pod, you will need to provide a way for your clients to get to
  the
  [`examples/spark/spark-master-service.yaml`](spark-master-service.yaml). See
  [Services](https://kubernetes.io/docs/user-guide/services.md) for more information.

## Known Issues With Zeppelin

* The Zeppelin pod is large, so it may take a while to pull depending on your
  network. The size of the Zeppelin pod is something we're working on, see issue #17231.

* Zeppelin may take some time (about a minute) on this pipeline the first time
  you run it. It seems to take considerable time to load.

* On GKE, `kubectl port-forward` may not be stable over long periods of time. If
  you see Zeppelin go into `Disconnected` state (there will be a red dot on the
  top right as well), the `port-forward` probably failed and needs to be
  restarted. See #12179.

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/spark/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Spark on GlusterFS example

This guide is an extension of the standard [Spark on Kubernetes Guide](../../../examples/spark/) and describes how to run Spark on GlusterFS using the [Kubernetes Volume Plugin for GlusterFS](../../../examples/volumes/glusterfs/)

The setup is the same in that you will setup a Spark Master Service in the same way you do with the standard Spark guide but you will deploy a modified Spark Master and a Modified Spark Worker ReplicationController, as they will be modified to use the GlusterFS volume plugin to mount a GlusterFS volume into the Spark Master and Spark Workers containers. Note that this example can be used as a guide for implementing any of the Kubernetes Volume Plugins with the Spark Example.

[There is also a video available that provides a walkthrough for how to set this solution up](https://youtu.be/xyIaoM0-gM0)

## Step Zero: Prerequisites

This example assumes that you have been able to successfully get the standard Spark Example working in Kubernetes and that you have a GlusterFS cluster that is accessible from your Kubernetes cluster. It is also recommended that you are familiar with the GlusterFS Volume Plugin and how to configure it.

## Step One: Define the endpoints for your GlusterFS Cluster

Modify the `examples/spark/spark-gluster/glusterfs-endpoints.yaml` file to list the IP addresses of some of the servers in your GlusterFS cluster. The GlusterFS Volume Plugin uses these IP addresses to perform a Fuse Mount of the GlusterFS Volume into the Spark Worker Containers that are launched by the ReplicationController in the next section.

Register your endpoints by running the following command:

```console
$ kubectl create -f examples/spark/spark-gluster/glusterfs-endpoints.yaml
```

## Step Two: Modify and Submit your Spark Master ReplicationController

Modify the `examples/spark/spark-gluster/spark-master-controller.yaml` file to reflect the GlusterFS Volume that you wish to use in the PATH parameter of the volumes subsection.

Submit the Spark Master Pod

```console
$ kubectl create -f examples/spark/spark-gluster/spark-master-controller.yaml
```

Verify that the Spark Master Pod deployed successfully.

```console
$ kubectl get pods
```

Submit the Spark Master Service

```console
$ kubectl create -f examples/spark/spark-gluster/spark-master-service.yaml
```

Verify that the Spark Master Service deployed successfully.

```console
$ kubectl get services
```

## Step Three: Start your Spark workers

Modify the `examples/spark/spark-gluster/spark-worker-controller.yaml` file to reflect the GlusterFS Volume that you wish to use in the PATH parameter of the Volumes subsection.

Make sure that the replication factor for the pods is not greater than the amount of Kubernetes nodes available in your Kubernetes cluster.

Submit your Spark Worker ReplicationController by running the following command:

```console
$ kubectl create -f examples/spark/spark-gluster/spark-worker-controller.yaml
```

Verify that the Spark Worker ReplicationController deployed its pods successfully.

```console
$ kubectl get pods
```

Follow the steps from the standard example to verify the Spark Worker pods have registered successfully with the Spark Master.

## Step Four: Submit a Spark Job

All the Spark Workers and the Spark Master in your cluster have a mount to GlusterFS. This means that any of them can be used as the Spark Client to submit a job. For simplicity, lets use the Spark Master as an example.


The Spark Worker and Spark Master containers include a setup_client utility script that takes two parameters, the Service IP of the Spark Master and the port that it is running on. This must be to setup the container as a Spark client prior to submitting any Spark Jobs.

Obtain the Service IP (listed as IP:) and Full Pod Name by running

```console
$ kubectl describe pod spark-master-controller
```

Now we will shell into the Spark Master Container and run a Spark Job. In the example below, we are running the Spark Wordcount example and specifying the input and output directory at the location where GlusterFS is mounted in the Spark Master Container. This will submit the job to the Spark Master who will distribute the work to all the Spark Worker Containers.

All the Spark Worker containers  will be able to access the data as they all have the same GlusterFS volume mounted at /mnt/glusterfs. The reason we are submitting the job from a Spark Worker and not an additional Spark Base container (as in the standard Spark Example) is due to the fact that the Spark instance submitting the job must be able to access the data. Only the Spark Master and Spark Worker containers have GlusterFS mounted.

The Spark Worker and Spark Master containers include a setup_client utility script that takes two parameters, the Service IP of the Spark Master and the port that it is running on. This must be done to setup the container as a Spark client prior to submitting any Spark Jobs.

Shell into the Master Spark Node (spark-master-controller) by running

```console
kubectl exec spark-master-controller-<ID> -i -t -- bash -i

root@spark-master-controller-c1sqd:/# . /setup_client.sh <Service IP> 7077
root@spark-master-controller-c1sqd:/# pyspark

Python 2.7.9 (default, Mar  1 2015, 12:57:24)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
15/06/26 14:25:28 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.4.0
      /_/
Using Python version 2.7.9 (default, Mar  1 2015 12:57:24)
SparkContext available as sc, HiveContext available as sqlContext.
>>> file = sc.textFile("/mnt/glusterfs/somefile.txt")
>>> counts = file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
>>> counts.saveAsTextFile("/mnt/glusterfs/output")
```

While still in the container, you can see the output of your Spark Job in the Distributed File System by running the following:

```console
root@spark-master-controller-c1sqd:/# ls -l /mnt/glusterfs/output
```

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/spark/spark-gluster/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
# Persistent Installation of MySQL and WordPress on Kubernetes

This example describes how to run a persistent installation of
[WordPress](https://wordpress.org/) and
[MySQL](https://www.mysql.com/) on Kubernetes. We'll use the
[mysql](https://registry.hub.docker.com/_/mysql/) and
[wordpress](https://registry.hub.docker.com/_/wordpress/) official
[Docker](https://www.docker.com/) images for this installation. (The
WordPress image includes an Apache server).

Demonstrated Kubernetes Concepts:

* [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to
  define persistent disks (disk lifecycle not tied to the Pods).
* [Services](https://kubernetes.io/docs/concepts/services-networking/service/) to enable Pods to
  locate one another.
* [External Load Balancers](https://kubernetes.io/docs/concepts/services-networking/service/#type-loadbalancer)
  to expose Services externally.
* [Deployments](http://kubernetes.io/docs/user-guide/deployments/) to ensure Pods
  stay up and running.
* [Secrets](http://kubernetes.io/docs/user-guide/secrets/) to store sensitive
  passwords.

## Quickstart

Put your desired MySQL password in a file called `password.txt` with
no trailing newline. The first `tr` command will remove the newline if
your editor added one.

**Note:** if your cluster enforces **_selinux_** and you will be using [Host Path](#host-path) for storage, then please follow this [extra step](#selinux).

```shell
tr --delete '\n' <password.txt >.strippedpassword.txt && mv .strippedpassword.txt password.txt
kubectl create -f https://raw.githubusercontent.com/kubernetes/kubernetes/master/examples/mysql-wordpress-pd/local-volumes.yaml
kubectl create secret generic mysql-pass --from-file=password.txt
kubectl create -f https://raw.githubusercontent.com/kubernetes/kubernetes/master/examples/mysql-wordpress-pd/mysql-deployment.yaml
kubectl create -f https://raw.githubusercontent.com/kubernetes/kubernetes/master/examples/mysql-wordpress-pd/wordpress-deployment.yaml
```

## Table of Contents

<!-- BEGIN MUNGE: GENERATED_TOC -->

- [Persistent Installation of MySQL and WordPress on Kubernetes](#persistent-installation-of-mysql-and-wordpress-on-kubernetes)
  - [Quickstart](#quickstart)
  - [Table of Contents](#table-of-contents)
  - [Cluster Requirements](#cluster-requirements)
  - [Decide where you will store your data](#decide-where-you-will-store-your-data)
    - [Host Path](#host-path)
        - [SELinux](#selinux)
    - [GCE Persistent Disk](#gce-persistent-disk)
  - [Create the MySQL Password Secret](#create-the-mysql-password-secret)
  - [Deploy MySQL](#deploy-mysql)
  - [Deploy WordPress](#deploy-wordpress)
  - [Visit your new WordPress blog](#visit-your-new-wordpress-blog)
  - [Take down and restart your blog](#take-down-and-restart-your-blog)
  - [Next Steps](#next-steps)

<!-- END MUNGE: GENERATED_TOC -->

## Cluster Requirements

Kubernetes runs in a variety of environments and is inherently
modular. Not all clusters are the same. These are the requirements for
this example.

* Kubernetes version 1.2 is required due to using newer features, such
  at PV Claims and Deployments. Run `kubectl version` to see your
  cluster version.
* [Cluster DNS](https://github.com/kubernetes/dns) will be used for service discovery.
* An [external load balancer](https://kubernetes.io/docs/concepts/services-networking/service/#type-loadbalancer)
  will be used to access WordPress.
* [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
  are used. You must create Persistent Volumes in your cluster to be
  claimed. This example demonstrates how to create two types of
  volumes, but any volume is sufficient.

Consult a
[Getting Started Guide](http://kubernetes.io/docs/getting-started-guides/)
to set up a cluster and the
[kubectl](http://kubernetes.io/docs/user-guide/prereqs/) command-line client.

## Decide where you will store your data

MySQL and WordPress will each use a
[Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
to store their data. We will use a Persistent Volume Claim to claim an
available persistent volume. This example covers HostPath and
GCEPersistentDisk volumes. Choose one of the two, or see
[Types of Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes)
for more options.

### Host Path

Host paths are volumes mapped to directories on the host. **These
should be used for testing or single-node clusters only**. The data
will not be moved between nodes if the pod is recreated on a new
node. If the pod is deleted and recreated on a new node, data will be
lost.

##### SELinux

On systems supporting selinux it is preferred to leave it enabled/enforcing.
However, docker containers mount the host path with the "_svirt_sandbox_file_t_"
label type, which is incompatible with the default label type for /tmp ("_tmp_t_"),
resulting in a permissions error when the mysql container attempts to `chown`
_/var/lib/mysql_.
Therefore, on selinx systems using host path, you should pre-create the host path
directory (/tmp/data/) and change it's selinux label type to "_svirt_sandbox_file_t_",
as follows:

```shell
## on every node:
mkdir -p /tmp/data
chmod a+rwt /tmp/data  # match /tmp permissions
chcon -Rt svirt_sandbox_file_t /tmp/data
```

Continuing with host path, create the persistent volume objects in Kubernetes using
[local-volumes.yaml](local-volumes.yaml):

```shell
export KUBE_REPO=https://raw.githubusercontent.com/kubernetes/kubernetes/master
kubectl create -f $KUBE_REPO/examples/mysql-wordpress-pd/local-volumes.yaml
```


### GCE Persistent Disk

This storage option is applicable if you are running on
[Google Compute Engine](http://kubernetes.io/docs/getting-started-guides/gce/).

Create two persistent disks. You will need to create the disks in the
same [GCE zone](https://cloud.google.com/compute/docs/zones) as the
Kubernetes cluster. The default setup script will create the cluster
in the `us-central1-b` zone, as seen in the
[config-default.sh](../../cluster/gce/config-default.sh) file. Replace
`<zone>` below with the appropriate zone. The names `wordpress-1` and
`wordpress-2` must match the `pdName` fields we have specified in
[gce-volumes.yaml](gce-volumes.yaml).

```shell
gcloud compute disks create --size=20GB --zone=<zone> wordpress-1
gcloud compute disks create --size=20GB --zone=<zone> wordpress-2
```

Create the persistent volume objects in Kubernetes for those disks:

```shell
export KUBE_REPO=https://raw.githubusercontent.com/kubernetes/kubernetes/master
kubectl create -f $KUBE_REPO/examples/mysql-wordpress-pd/gce-volumes.yaml
```

## Create the MySQL Password Secret

Use a [Secret](http://kubernetes.io/docs/user-guide/secrets/) object
to store the MySQL password. First create a file (in the same directory
as the wordpress sample files) called
`password.txt` and save your password in it. Make sure to not have a
trailing newline at the end of the password. The first `tr` command
will remove the newline if your editor added one. Then, create the
Secret object.

```shell
tr --delete '\n' <password.txt >.strippedpassword.txt && mv .strippedpassword.txt password.txt
kubectl create secret generic mysql-pass --from-file=password.txt
```

This secret is referenced by the MySQL and WordPress pod configuration
so that those pods will have access to it. The MySQL pod will set the
database password, and the WordPress pod will use the password to
access the database.

## Deploy MySQL

Now that the persistent disks and secrets are defined, the Kubernetes
pods can be launched. Start MySQL using
[mysql-deployment.yaml](mysql-deployment.yaml).

```shell
kubectl create -f $KUBE_REPO/examples/mysql-wordpress-pd/mysql-deployment.yaml
```

Take a look at [mysql-deployment.yaml](mysql-deployment.yaml), and
note that we've defined a volume mount for `/var/lib/mysql`, and then
created a Persistent Volume Claim that looks for a 20G volume. This
claim is satisfied by any volume that meets the requirements, in our
case one of the volumes we created above.

Also look at the `env` section and see that we specified the password
by referencing the secret `mysql-pass` that we created above. Secrets
can have multiple key:value pairs. Ours has only one key
`password.txt` which was the name of the file we used to create the
secret. The [MySQL image](https://hub.docker.com/_/mysql/) sets the
database password using the `MYSQL_ROOT_PASSWORD` environment
variable.

It may take a short period before the new pod reaches the `Running`
state.  List all pods to see the status of this new pod.

```shell
kubectl get pods
```

```
NAME                          READY     STATUS    RESTARTS   AGE
wordpress-mysql-cqcf4-9q8lo   1/1       Running   0          1m
```

Kubernetes logs the stderr and stdout for each pod. Take a look at the
logs for a pod by using `kubectl log`. Copy the pod name from the
`get pods` command, and then:

```shell
kubectl logs <pod-name>
```

```
...
2016-02-19 16:58:05 1 [Note] InnoDB: 128 rollback segment(s) are active.
2016-02-19 16:58:05 1 [Note] InnoDB: Waiting for purge to start
2016-02-19 16:58:05 1 [Note] InnoDB: 5.6.29 started; log sequence number 1626007
2016-02-19 16:58:05 1 [Note] Server hostname (bind-address): '*'; port: 3306
2016-02-19 16:58:05 1 [Note] IPv6 is available.
2016-02-19 16:58:05 1 [Note]   - '::' resolves to '::';
2016-02-19 16:58:05 1 [Note] Server socket created on IP: '::'.
2016-02-19 16:58:05 1 [Warning] 'proxies_priv' entry '@ root@wordpress-mysql-cqcf4-9q8lo' ignored in --skip-name-resolve mode.
2016-02-19 16:58:05 1 [Note] Event Scheduler: Loaded 0 events
2016-02-19 16:58:05 1 [Note] mysqld: ready for connections.
Version: '5.6.29'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
```

Also in [mysql-deployment.yaml](mysql-deployment.yaml) we created a
service to allow other pods to reach this mysql instance. The name is
`wordpress-mysql` which resolves to the pod IP.

Up to this point one Deployment, one Pod, one PVC, one Service, one Endpoint,
two PVs, and one Secret have been created, shown below:

```shell
kubectl get deployment,pod,svc,endpoints,pvc -l app=wordpress -o wide && \
  kubectl get secret mysql-pass && \
  kubectl get pv
```

```shell
NAME                     DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/wordpress-mysql   1         1         1            1           3m
NAME                                  READY     STATUS    RESTARTS   AGE       IP           NODE
po/wordpress-mysql-3040864217-40soc   1/1       Running   0          3m        172.17.0.2   127.0.0.1
NAME                  CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE       SELECTOR
svc/wordpress-mysql   None         <none>        3306/TCP   3m        app=wordpress,tier=mysql
NAME                 ENDPOINTS         AGE
ep/wordpress-mysql   172.17.0.2:3306   3m
NAME                 STATUS    VOLUME       CAPACITY   ACCESSMODES   AGE
pvc/mysql-pv-claim   Bound     local-pv-2   20Gi       RWO           3m
NAME         TYPE      DATA      AGE
mysql-pass   Opaque    1         3m
NAME         CAPACITY   ACCESSMODES   STATUS      CLAIM                    REASON    AGE
local-pv-1   20Gi       RWO           Available                                      3m
local-pv-2   20Gi       RWO           Bound       default/mysql-pv-claim             3m
```

## Deploy WordPress

Next deploy WordPress using
[wordpress-deployment.yaml](wordpress-deployment.yaml):

```shell
kubectl create -f $KUBE_REPO/examples/mysql-wordpress-pd/wordpress-deployment.yaml
```

Here we are using many of the same features, such as a volume claim
for persistent storage and a secret for the password.

The [WordPress image](https://hub.docker.com/_/wordpress/) accepts the
database hostname through the environment variable
`WORDPRESS_DB_HOST`. We set the env value to the name of the MySQL
service we created: `wordpress-mysql`.

The WordPress service has the setting `type: LoadBalancer`.  This will
set up the wordpress service behind an external IP.

Find the external IP for your WordPress service. **It may take a minute
to have an external IP assigned to the service, depending on your
cluster environment.**

```shell
kubectl get services wordpress
```

```
NAME        CLUSTER-IP     EXTERNAL-IP     PORT(S)   AGE
wordpress   10.0.0.5       1.2.3.4         80/TCP    19h
```

## Visit your new WordPress blog

Now, we can visit the running WordPress app. Use the external IP of
the service that you obtained above.

```
http://<external-ip>
```

You should see the familiar WordPress init page.

![WordPress init page](WordPress.png "WordPress init page")

> Warning: Do not leave your WordPress installation on this page. If
> it is found by another user, they can set up a website on your
> instance and use it to serve potentially malicious content. You
> should either continue with the installation past the point at which
> you create your username and password, delete your instance, or set
> up a firewall to restrict access.

## Take down and restart your blog

Set up your WordPress blog and play around with it a bit. Then, take
down its pods and bring them back up again. Because you used
persistent disks, your blog state will be preserved.

All of the resources are labeled with `app=wordpress`, so you can
easily bring them down using a label selector:

```shell
kubectl delete deployment,service -l app=wordpress
kubectl delete secret mysql-pass
```

Later, re-creating the resources with the original commands will pick
up the original disks with all your data intact. Because we did not
delete the PV Claims, no other pods in the cluster could claim them
after we deleted our pods. Keeping the PV Claims also ensured
recreating the Pods did not cause the PD to switch Pods.

If you are ready to release your persistent volumes and the data on them, run:

```shell
kubectl delete pvc -l app=wordpress
```

And then delete the volume objects themselves:

```shell
kubectl delete pv local-pv-1 local-pv-2
```

or

```shell
kubectl delete pv wordpress-pv-1 wordpress-pv-2
```

## Next Steps

* [Introspection and Debugging](http://kubernetes.io/docs/user-guide/introspection-and-debugging/)
* [Jobs](http://kubernetes.io/docs/user-guide/jobs/) may be useful to run SQL queries.
* [Exec](http://kubernetes.io/docs/user-guide/getting-into-containers/)
* [Port Forwarding](http://kubernetes.io/docs/user-guide/connecting-to-applications-port-forward/)

<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/examples/mysql-wordpress-pd/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
See [e2e-node-tests](https://git.k8s.io/community/contributors/devel/e2e-node-tests.md)

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/e2e_node/README.md?pixel)]()
## Obsolete Config Files From Docs

These config files were originally from docs, but have been separated
and put here to be used by various tests.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/fixtures/doc-yaml/README.md?pixel)]()
# Zookeeper statefulset e2e tester

The image in this directory is the init container for contrib/pets/zookeeper but for one difference, it bakes a specific version of zookeeper into the base image so we get deterministic test results without having to depend on a zookeeper download server. Discussing the tradeoffs to either approach (download the version at runtime, or maintain an image per version) are outside the scope of this document.

You can execute the image locally via:
```
$ docker run -it gcr.io/google_containers/zookeeper-install-3.5.0-alpha:e2e --cmd --install-into=/opt --work-dir=/work-dir
```
To share the installation with other containers mount the appropriate volumes as `--install-into` and `--work-dir`, where `install-into` is the directory to install zookeeper into, and `work-dir` is the directory to install the user/admin supplied on-{start,change} hook scripts.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/pets/zookeeper/README.md?pixel)]()
# Redis statefulset e2e tester

The image in this directory is the init container for contrib/pets/redis but for one difference, it bakes a specific version of redis into the base image so we get deterministic test results without having to depend on a redis download server. Discussing the tradeoffs to either approach (download the version at runtime, or maintain an image per version) are outside the scope of this document.

You can execute the image locally via:
```
$ docker run -it gcr.io/google_containers/redis-install-3.2.0:e2e --cmd --install-into=/opt --work-dir=/work-dir
```
To share the installation with other containers mount the appropriate volumes as `--install-into` and `--work-dir`, where `install-into` is the directory to install redis into, and `work-dir` is the directory to install the user/admin supplied on-{start,change} hook scripts.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/pets/redis/README.md?pixel)]()
## cuda_vector_add

This is a small CUDA application that performs a simple vector addition. Useful for testing CUDA support in Kubernetes.

## How to release:

```
# Build
$ make

# Push
$ make push
```
# Logs Generator

## Overview

Logs generator is a tool to create predictable load on the logs delivery system.
Is generates random lines with predictable format and predictable average length.
Each line can be later uniquely identified to ensure logs delivery.

## Usage

Tool is parametrized with the total number of number that should be generated and the duration of
the generation process. For example, if you want to create a throughput of 100 lines per second
for a minute, you set total number of lines to 6000 and duration to 1 minute.

Parameters are passed through environment variables. There are no defaults, you should always 
set up container parameters. Total number of line is parametrized through env variable
`LOGS_GENERATOR_LINES_TOTAL` and duration in go format is parametrized through env variable
`LOGS_GENERATOR_DURATION`.

Inside the container all log lines are written to the stdout.

Each line is on average 100 bytes long and follows this pattern:

```
2000-12-31T12:59:59Z <id> <method> /api/v1/namespaces/<namespace>/endpoints/<random_string> <random_number>
```

Where `<id>` refers to the number from 0 to `total_lines - 1`, which is unique for each
line in a given run of the container.

## Image

Image is located in the public repository of Google Container Registry under the name

```
gcr.io/google_containers/logs-generator:v0.1.1
```

## Examples

```
docker run -i \
  -e "LOGS_GENERATOR_LINES_TOTAL=10" \
  -e "LOGS_GENERATOR_DURATION=1s" \
  gcr.io/google_containers/logs-generator:v0.1.1
```

```
kubectl run logs-generator \
  --generator=run-pod/v1 \
  --image=gcr.io/google_containers/logs-generator:v0.1.1 \
  --restart=Never \
  --env "LOGS_GENERATOR_LINES_TOTAL=1000" \
  --env "LOGS_GENERATOR_DURATION=1m"
```

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/logs-generator/README.md?pixel)]()
This directory contains go source, Dockerfile and Makefile for making a test
container which serves requested data on ports specified in ENV variables.

The included localhost.crt is a PEM-encoded TLS cert with SAN IPs
"127.0.0.1" and "[::1]", expiring in January 2084, generated from
src/crypto/tls:
go run generate_cert.go  --rsa-bits 2048 --host 127.0.0.1,::1,example.com --ca --start-date "Jan 1 00:00:00 1970" --duration=1000000h

To use a different cert/key, mount them into the pod and set the 
CERT_FILE and KEY_FILE environment variables to the desired paths.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/porter/README.md?pixel)]()
This is a dockerfile which we curate inside of kubernetes for running iperf as a service.

Eventually we would like to update it to iperf3.

Possibly we might even start using a pure go based iperf and maintain the same cmd line abstraction.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/iperf/README.md?pixel)]()
# NFS server container for testing

This container exports '/' directory with an index.html inside. NFSv4 only.

Accepts a -G option for specifying a group id to give exported directories.
Clients in the specified group will have full rwx permissions, others none.

Inspired by https://github.com/cpuguy83/docker-nfs-server.

Used by test/e2e/* to test NFSVolumeSource. Not for production use!


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/volumes-tester/nfs/README.md?pixel)]()
# iSCSI target container for testing.

Inspired by https://github.com/rvykydal/dockerfile-iscsid

* The container needs /lib/modules from the host to insert appropriate
  kernel modules for iscsi. This assumes that these modules are installed
  on the host!

* The container needs to run with docker --privileged

block.tar.gz is a small ext2 filesystem created by `make block` (run as root!)


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/volumes-tester/iscsi/README.md?pixel)]()
# Gluster server container for testing

This container exports test_vol volume with an index.html inside.

Used by test/e2e/* to test GlusterfsVolumeSource. Not for production use!


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/volumes-tester/gluster/README.md?pixel)]()
# Ceph server container for testing

This container exports ceph fs with an index.html inside.

Used by test/e2e/* to test CephFSVolumeSource. Not for production use!


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/volumes-tester/ceph/README.md?pixel)]()
# Resource Consumer

## Overview
Resource Consumer is a tool which allows to generate cpu/memory utilization in a container.
The reason why it was created is testing kubernetes autoscaling.
Resource Consumer can help with autoscaling tests for:
- cluster size autoscaling,
- horizontal autoscaling of pod - changing the size of replication controller,
- vertical autoscaling of pod - changing its resource limits.

## Usage
Resource Consumer starts an HTTP server and handle sent requests.
It listens on port given as a flag (default 8080).
Action of consuming resources is send to the container by a POST http request.
Each http request creates new process.
Http request handler is in file resource_consumer_handler.go 

The container consumes specified amount of resources:

- CPU in millicores,
- Memory in megabytes,
- Fake custom metrics.

###Consume CPU http request
- suffix "ConsumeCPU",
- parameters "millicores" and "durationSec".

Consumes specified amount of millicores for durationSec seconds.
Consume CPU uses "./consume-cpu/consume-cpu" binary (file consume-cpu/consume_cpu.go).
When CPU consumption is too low this binary uses cpu by calculating math.sqrt(0) 10^7 times
and if consumption is too high binary sleeps for 10 millisecond.
One replica of Resource Consumer cannot consume more that 1 cpu.

###Consume Memory http request
- suffix "ConsumeMem",
- parameters "megabytes" and "durationSec".

Consumes specified amount of megabytes for durationSec seconds.
Consume Memory uses stress tool (stress -m 1 --vm-bytes megabytes --vm-hang 0 -t durationSec).
Request leading to consuming more memory then container limit will be ignored.

###Bump value of a fake custom metric
- suffix "BumpMetric",
- parameters "metric", "delta" and "durationSec".

Bumps metric with given name by delta for durationSec seconds.
Custom metrics in Prometheus format are exposed on "/metrics" endpoint.

###CURL example
```console
$ kubectl run resource-consumer --image=gcr.io/google_containers/resource_consumer:beta --expose --service-overrides='{ "spec": { "type": "LoadBalancer" } }' --port 8080
$ kubectl get services resource-consumer
```

There are two IPs.  The first one is internal, while the second one is the external load-balanced IP.  Both serve port 8080. (Use second one)

```console
$ curl --data "millicores=300&durationSec=600" http://<EXTERNAL-IP>:8080/ConsumeCPU
```

300 millicores will be consumed for 600 seconds.

## Image

Docker image of Resource Consumer can be found in Google Container Registry as gcr.io/google_containers/resource_consumer:beta

## Use cases

###Cluster size autoscaling
1. Consume more resources on each node that is specified for autoscaler
2. Observe that cluster size increased

###Horizontal autoscaling of pod
1. Create consuming RC and start consuming appropriate amount of resources
2. Observe that RC has been resized
3. Observe that usage on each replica decreased

###Vertical autoscaling of pod
1. Create consuming pod and start consuming appropriate amount of resources
2. Observed that limits has been increased




[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/resource-consumer/README.md?pixel)]()
## serve_hostname

This is a small util app to serve your hostname on TCP and/or UDP.  Useful for testing.

The `serve_hostname` Makefile supports multiple architectures, which means it may cross-compile and build an docker image easily.
Arch-specific busybox images serve as base images.

If you are releasing a new version, please bump the `TAG` value in the `Makefile` before building the images.

## How to release:

```
# Build cross-platform binaries
$ make all-push

# Build for linux/amd64 (default)
$ make push ARCH=amd64
# ---> gcr.io/google_containers/serve_hostname-amd64:TAG

$ make push ARCH=arm
# ---> gcr.io/google_containers/serve_hostname-arm:TAG

$ make push ARCH=arm64
# ---> gcr.io/google_containers/serve_hostname-arm64:TAG

$ make push ARCH=ppc64le
# ---> gcr.io/google_containers/serve_hostname-ppc64le:TAG

$ make push ARCH=s390x
# ---> gcr.io/google_containers/serve_hostname-s390x:TAG
```

Of course, if you don't want to push the images, run `make all-container` or `make container ARCH={target_arch}` instead.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/contrib/for-demos/serve_hostname/README.md?pixel)]()


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/serve_hostname/README.md?pixel)]()
# Overview

The goal of this Go project is to consolidate all low-level
network testing "daemons" into one place. In network testing we
frequently have need of simple daemons (common/Runner) that perform
some "trivial" set of actions on a socket.

# Usage

* A package for each general area that is being tested, for example
  `nat/` will contain Runners that test various NAT features.
* Every runner should be registered via `main.go:makeRunnerMap()`.
* Runners receive a JSON options structure as to their configuration. `Run()`
  should return the disposition of the test.

Runners can be executed into two different ways, either through the
the command-line or via an HTTP request:

## Command-line

````
$ ./net -runner <runner> -options <json>
./net \
  -runner nat-closewait-client \
  -options '{"RemoteAddr":"127.0.0.1:9999"}'
````

## HTTP server
````
$ ./net --serve :8889
$ curl -v -X POST localhost:8889/run/nat-closewait-server \
  -d '{"LocalAddr":"127.0.0.1:9999"}'
````


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/images/net/README.md?pixel)]()
These resources are used to add extra (non-default) bindings to kubemark to match users and groups that are particular to the kubemark environment. These are not standard bootstrap bindings and not standard users they are bound to, and have been adapted from cluster/addons/e2e-rbac-bindings. Tighten/loosen these access rights as required in future.
See [e2e-tests](https://git.k8s.io/community/contributors/devel/e2e-tests.md#federation-e2e-tests)

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/e2e_federation//README.md?pixel)]()
Scheduler Performance Test
======

Motivation
------
We already have a performance testing system -- Kubemark. However, Kubemark requires setting up and bootstrapping a whole cluster, which takes a lot of time.

We want to have a standard way to reproduce scheduling latency metrics result and benchmark scheduler as simple and fast as possible. We have the following goals:

- Save time on testing
  - The test and benchmark can be run in a single box.
    We only set up components necessary to scheduling without booting up a cluster.
- Profiling runtime metrics to find out bottleneck
  - Write scheduler integration test but focus on performance measurement.
    Take advantage of go profiling tools and collect fine-grained metrics,
    like cpu-profiling, memory-profiling and block-profiling.
- Reproduce test result easily
  - We want to have a known place to do the performance related test for scheduler.
    Developers should just run one script to collect all the information they need.

Currently the test suite has the following:

- density test (by adding a new Go test)
  - schedule 30k pods on 1000 (fake) nodes and 3k pods on 100 (fake) nodes
  - print out scheduling rate every second
  - let you learn the rate changes vs number of scheduled pods
- benchmark
  - make use of `go test -bench` and report nanosecond/op.
  - schedule b.N pods when the cluster has N nodes and P scheduled pods. Since it takes relatively long time to finish one round, b.N is small: 10 - 100.


How To Run
------
```
cd kubernetes/test/integration/scheduler_perf
./test-performance.sh
```


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/component/scheduler/perf/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/integration/scheduler_perf/README.md?pixel)]()
# Soak Test serve_hostnames
This directory contains the source for a soak test `serve_hostnames` which performs the following actions when used with the GCE provider:

* A connection is established to the master of the cluster identified from the current context set in `$HOME/.kube/.kubeconfig`.
* The nodes available on the cluster are enumerated (say *N* nodes).
* On each node, *M* pods are created (by default 1). The pod encapsulates the `serve_hostnames` image which simply returns the name of the pod in response to a `GET` request.
The pods are created individually (i.e. not with a replication controller).
* A service is created which maps to these pods.
* The program makes *I* iterations (default 1) where it issues *QxNxM* queries (*Q* default is 10) via the service proxy interface at the master.
* The program verifies that every pod (and thus every node) responded to at least one query (the average should be about *Q*). 
* The time taken to perform various operations is reported and some operations are re-tried if they failed.

Here is some representative output.
```
$ ./serve_hostnames 
I0326 14:21:04.179893   11434 serve_hostnames.go:60] Starting serve_hostnames soak test with queries=10 and podsPerNode=1 upTo=1
I0326 14:21:04.507252   11434 serve_hostnames.go:85] Nodes found on this cluster:
I0326 14:21:04.507282   11434 serve_hostnames.go:87] 0: kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:21:04.507297   11434 serve_hostnames.go:87] 1: kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:21:04.507309   11434 serve_hostnames.go:87] 2: kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:21:04.507320   11434 serve_hostnames.go:87] 3: kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:21:04.507347   11434 serve_hostnames.go:95] Using namespace serve-hostnames-8145 for this test.
I0326 14:21:04.507363   11434 serve_hostnames.go:98] Creating service serve-hostnames-8145/serve-hostnames
I0326 14:21:04.559849   11434 serve_hostnames.go:148] Creating pod serve-hostnames-8145/serve-hostname-0-0 on node kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:21:04.605603   11434 serve_hostnames.go:148] Creating pod serve-hostnames-8145/serve-hostname-1-0 on node kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:21:04.662099   11434 serve_hostnames.go:148] Creating pod serve-hostnames-8145/serve-hostname-2-0 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:21:04.707179   11434 serve_hostnames.go:148] Creating pod serve-hostnames-8145/serve-hostname-3-0 on node kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:21:04.757646   11434 serve_hostnames.go:194] Waiting for the serve-hostname pods to be ready
I0326 14:23:31.125188   11434 serve_hostnames.go:211] serve-hostnames-8145/serve-hostname-0-0 is running
I0326 14:23:31.165984   11434 serve_hostnames.go:211] serve-hostnames-8145/serve-hostname-1-0 is running
I0326 14:25:22.213751   11434 serve_hostnames.go:211] serve-hostnames-8145/serve-hostname-2-0 is running
I0326 14:25:37.387257   11434 serve_hostnames.go:211] serve-hostnames-8145/serve-hostname-3-0 is running
W0326 14:25:39.243813   11434 serve_hostnames.go:265] No response from pod serve-hostname-3-0 on node kubernetes-node-jay1.c.kubernetes-satnam.internal at iteration 0
I0326 14:25:39.243844   11434 serve_hostnames.go:269] Iteration 0 took 1.814483599s for 40 queries (22.04 QPS)
I0326 14:25:39.243871   11434 serve_hostnames.go:182] Cleaning up pods
I0326 14:25:39.434619   11434 serve_hostnames.go:130] Cleaning up service serve-hostnames-8145/server-hostnames
```

The pods are named with -*N*-*M* suffixes which identify the number of the node *N* and the number of the pod *M* on that node.
Notice that in this run the pod (number 0) running on node 3 did not respond to any queries.

The number of iterations to perform for issuing queries can be changed from the default of 1 to some higher value e.g. `--up_to=3` and the number of pods per node can also be changed e.g. `--pods_per_node=2`:

```
$ ./serve_hostnames --up_to=3 --pods_per_node=2
I0326 14:27:27.584378   11808 serve_hostnames.go:60] Starting serve_hostnames soak test with queries=10 and podsPerNode=2 upTo=3
I0326 14:27:27.913713   11808 serve_hostnames.go:85] Nodes found on this cluster:
I0326 14:27:27.913774   11808 serve_hostnames.go:87] 0: kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:27:27.913800   11808 serve_hostnames.go:87] 1: kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:27:27.913825   11808 serve_hostnames.go:87] 2: kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:27:27.913846   11808 serve_hostnames.go:87] 3: kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:27:27.913904   11808 serve_hostnames.go:95] Using namespace serve-hostnames-4997 for this test.
I0326 14:27:27.913931   11808 serve_hostnames.go:98] Creating service serve-hostnames-4997/serve-hostnames
I0326 14:27:27.969083   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-0-0 on node kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:27:28.020133   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-0-1 on node kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:27:28.070054   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-1-0 on node kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:27:28.118641   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-1-1 on node kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:27:28.168786   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-2-0 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:27:28.214730   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-2-1 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:27:28.261685   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-3-0 on node kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:27:28.320224   11808 serve_hostnames.go:148] Creating pod serve-hostnames-4997/serve-hostname-3-1 on node kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:27:28.387007   11808 serve_hostnames.go:194] Waiting for the serve-hostname pods to be ready
I0326 14:28:28.969149   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-0-0 is running
I0326 14:28:29.010376   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-0-1 is running
I0326 14:28:29.050463   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-1-0 is running
I0326 14:28:29.091164   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-1-1 is running
I0326 14:30:00.850461   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-2-0 is running
I0326 14:30:00.891559   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-2-1 is running
I0326 14:30:00.932829   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-3-0 is running
I0326 14:30:00.973941   11808 serve_hostnames.go:211] serve-hostnames-4997/serve-hostname-3-1 is running
W0326 14:30:04.726582   11808 serve_hostnames.go:265] No response from pod serve-hostname-2-0 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal at iteration 0
W0326 14:30:04.726658   11808 serve_hostnames.go:265] No response from pod serve-hostname-2-1 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal at iteration 0
I0326 14:30:04.726696   11808 serve_hostnames.go:269] Iteration 0 took 3.711080213s for 80 queries (21.56 QPS)
W0326 14:30:08.267297   11808 serve_hostnames.go:265] No response from pod serve-hostname-2-0 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal at iteration 1
W0326 14:30:08.267365   11808 serve_hostnames.go:265] No response from pod serve-hostname-2-1 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal at iteration 1
I0326 14:30:08.267404   11808 serve_hostnames.go:269] Iteration 1 took 3.540635303s for 80 queries (22.59 QPS)
I0326 14:30:11.971349   11808 serve_hostnames.go:269] Iteration 2 took 3.703884372s for 80 queries (21.60 QPS)
I0326 14:30:11.971425   11808 serve_hostnames.go:182] Cleaning up pods
I0326 14:30:12.382932   11808 serve_hostnames.go:130] Cleaning up service serve-hostnames-4997/server-hostnames
```

Notice here that for the first two iterations neither of the pods on node 2 responded but by the third iteration responses
were received from all nodes.

For a soak test use `--up_to=-1` which will loop indefinitely.


Note that this is not designed to be a performance test. The goal for this program is to provide an easy way to have a soak test
that can run indefinitely an exercise enough of Kubernetes' functionality to be confident that the cluster is still up and healthy.
The reported QPS mainly indicates latency to the master since the proxy requests are issued (deliberately) in a serial manner.


A more detailed report can be produced with `--v=4` which measures the time taken to perform various operations
and it also reports the distribution of responses received from the pods. In the example below
we see that the pod on node 0 returned 18 responses, the pod on node 1 returned 10 responses and the
pod on node 3 returned 12 responses and the pod on node 2 did not respond at all.
```
$ ./serve_hostnames --v=4
I0326 14:33:26.020917   12099 serve_hostnames.go:60] Starting serve_hostnames soak test with queries=10 and podsPerNode=1 upTo=1
I0326 14:33:26.365201   12099 serve_hostnames.go:85] Nodes found on this cluster:
I0326 14:33:26.365260   12099 serve_hostnames.go:87] 0: kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:33:26.365288   12099 serve_hostnames.go:87] 1: kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:33:26.365313   12099 serve_hostnames.go:87] 2: kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:33:26.365334   12099 serve_hostnames.go:87] 3: kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:33:26.365392   12099 serve_hostnames.go:95] Using namespace serve-hostnames-1631 for this test.
I0326 14:33:26.365419   12099 serve_hostnames.go:98] Creating service serve-hostnames-1631/serve-hostnames
I0326 14:33:26.423927   12099 serve_hostnames.go:118] Service create serve-hostnames-1631/server-hostnames took 58.473361ms
I0326 14:33:26.423981   12099 serve_hostnames.go:148] Creating pod serve-hostnames-1631/serve-hostname-0-0 on node kubernetes-node-5h4m.c.kubernetes-satnam.internal
I0326 14:33:26.480185   12099 serve_hostnames.go:168] Pod create serve-hostnames-1631/serve-hostname-0-0 request took 56.178906ms
I0326 14:33:26.480271   12099 serve_hostnames.go:148] Creating pod serve-hostnames-1631/serve-hostname-1-0 on node kubernetes-node-9i4n.c.kubernetes-satnam.internal
I0326 14:33:26.534300   12099 serve_hostnames.go:168] Pod create serve-hostnames-1631/serve-hostname-1-0 request took 53.981761ms
I0326 14:33:26.534396   12099 serve_hostnames.go:148] Creating pod serve-hostnames-1631/serve-hostname-2-0 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal
I0326 14:33:26.590188   12099 serve_hostnames.go:168] Pod create serve-hostnames-1631/serve-hostname-2-0 request took 55.752115ms
I0326 14:33:26.590222   12099 serve_hostnames.go:148] Creating pod serve-hostnames-1631/serve-hostname-3-0 on node kubernetes-node-jay1.c.kubernetes-satnam.internal
I0326 14:33:26.650024   12099 serve_hostnames.go:168] Pod create serve-hostnames-1631/serve-hostname-3-0 request took 59.781614ms
I0326 14:33:26.650083   12099 serve_hostnames.go:194] Waiting for the serve-hostname pods to be ready
I0326 14:33:32.776651   12099 serve_hostnames.go:211] serve-hostnames-1631/serve-hostname-0-0 is running
I0326 14:33:32.822324   12099 serve_hostnames.go:211] serve-hostnames-1631/serve-hostname-1-0 is running
I0326 14:35:03.741235   12099 serve_hostnames.go:211] serve-hostnames-1631/serve-hostname-2-0 is running
I0326 14:35:03.786411   12099 serve_hostnames.go:211] serve-hostnames-1631/serve-hostname-3-0 is running
I0326 14:35:03.878030   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 45.656425ms
I0326 14:35:03.923999   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 45.887564ms
I0326 14:35:03.967731   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.7004ms
I0326 14:35:04.011077   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.318018ms
I0326 14:35:04.054958   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.843043ms
I0326 14:35:04.099051   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.030505ms
I0326 14:35:04.143197   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.069434ms
I0326 14:35:04.186800   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.530301ms
I0326 14:35:04.230492   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.658239ms
I0326 14:35:04.274337   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.800072ms
I0326 14:35:04.317801   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.379729ms
I0326 14:35:04.362778   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.897882ms
I0326 14:35:04.406845   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.976645ms
I0326 14:35:04.450513   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.613496ms
I0326 14:35:04.494369   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.777934ms
I0326 14:35:04.538399   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.945502ms
I0326 14:35:04.583760   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 45.285171ms
I0326 14:35:04.637430   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 53.629532ms
I0326 14:35:04.681389   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.918124ms
I0326 14:35:04.725401   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.964965ms
I0326 14:35:04.769218   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.734827ms
I0326 14:35:04.812660   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.376494ms
I0326 14:35:04.857974   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 45.246004ms
I0326 14:35:04.901706   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.668478ms
I0326 14:35:04.945372   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.642202ms
I0326 14:35:04.989023   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.619706ms
I0326 14:35:05.033153   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.087168ms
I0326 14:35:05.077038   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.791991ms
I0326 14:35:05.124299   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 47.214038ms
I0326 14:35:05.168162   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.795225ms
I0326 14:35:05.211687   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.48304ms
I0326 14:35:05.255553   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.799647ms
I0326 14:35:05.299352   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.72493ms
I0326 14:35:05.342916   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.509589ms
I0326 14:35:05.386952   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.947881ms
I0326 14:35:05.431467   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.442041ms
I0326 14:35:05.475834   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.304759ms
I0326 14:35:05.519373   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.501574ms
I0326 14:35:05.563584   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 44.162687ms
I0326 14:35:05.607126   12099 serve_hostnames.go:249] Proxy call in namespace serve-hostnames-1631 took 43.478674ms
I0326 14:35:05.607164   12099 serve_hostnames.go:258] serve-hostname-3-0: 12  
I0326 14:35:05.607176   12099 serve_hostnames.go:258] serve-hostname-1-0: 10  
I0326 14:35:05.607186   12099 serve_hostnames.go:258] serve-hostname-0-0: 18  
W0326 14:35:05.607199   12099 serve_hostnames.go:265] No response from pod serve-hostname-2-0 on node kubernetes-node-d0yo.c.kubernetes-satnam.internal at iteration 0
I0326 14:35:05.607211   12099 serve_hostnames.go:269] Iteration 0 took 1.774856469s for 40 queries (22.54 QPS)
I0326 14:35:05.607236   12099 serve_hostnames.go:182] Cleaning up pods
I0326 14:35:05.797893   12099 serve_hostnames.go:130] Cleaning up service serve-hostnames-1631/server-hostnames
```


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/soak/serve_hostnames/README.md?pixel)]()
See [e2e-tests](https://git.k8s.io/community/contributors/devel/e2e-tests.md)

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/test/e2e/README.md?pixel)]()
# Translations README

This is a basic sketch of the workflow needed to add translations:

# Adding/Updating Translations

## New languages
Create `translations/kubectl/<language>/LC_MESSAGES/k8s.po`. There's
no need to update `translations/test/...` which is only used for unit tests.

There is an example [PR here](https://github.com/kubernetes/kubernetes/pull/40645) which adds support for French.

Once you've added a new language, you'll need to register it in
`pkg/util/i18n/i18n.go` by adding it to the `knownTranslations` map.

## Wrapping strings
There is a simple script in `translations/extract.py` that performs
simple regular expression based wrapping of strings. It can always
use improvements to understand additional strings.

## Extracting strings
Once the strings are wrapped, you can extract strings from go files using
the `go-xgettext` command which can be installed with:

```console
go get github.com/gosexy/gettext/go-xgettext
```

Once that's installed you can run `./hack/update-translations.sh`, which
will extract and sort any new strings.

## Adding new translations
Edit the appropriate `k8s.po` file, `poedit` is a popular open source tool
for translations. You can load the `translations/kubectl/template.pot` file
to find messages that might be missing.

Once you are done with your `k8s.po` file, generate the corresponding `k8s.mo`
file. `poedit` does this automatically on save, but you can also run
`./hack/update-translations.sh` to perform the `po` to `mo` translation.

We use the English translation as the `msgid`.

## Regenerating the bindata file
Run `./hack/generate-bindata.sh`, this will turn the translation files
into generated code which will in turn be packaged into the Kubernetes
binaries.

## Extracting strings

There is a script in `translations/extract.py` that knows how to do some
simple extraction. It needs a lot of work.

# Using translations

To use translations, you simply need to add:
```go
import pkg/i18n
...
// Get a translated string
translated := i18n.T("Your message in english here")

// Get a translated plural string
translated := i18n.T("You had % items", items)

// Translated error
return i18n.Error("Something bad happened")

// Translated plural error
return i18n.Error("%d bad things happened")
```


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/translations/README.md?pixel)]()
##### Deprecation Notice: This directory has entered maintenance mode and will not be accepting new providers. Cloud Providers in this directory will continue to be actively developed or maintained and supported at their current level of support as a longer-term solution evolves. 
 
## Overview: 
The mechanism for supporting cloud providers is currently in transition:  the original method of implementing cloud provider-specific functionality within the main kubernetes tree (here) is no longer advised; however, the proposed solution is still in development.
 
#### Guidance for potential cloud providers: 
* Support for cloud providers is currently in a state of flux. Background information on motivation and the proposal for improving is in the github [proposal](https://git.k8s.io/community/contributors/design-proposals/cloud-provider-refactoring.md). 
* In support of this plan, a new cloud-controller-manager binary was added in 1.6. This was the first of several steps (see the proposal for more information). 
* Attempts to contribute new cloud providers or (to a lesser extent) persistent volumes to the core repo will likely meet with some pushback from reviewers/approvers. 
* It is understood that this is an unfortunate situation in which 'the old way is no longer supported but the new way is not ready yet', but the initial path is unsustainable, and contributors are encouraged to participate in the implementation of the proposed long-term solution, as there is risk that PRs for new cloud providers here will not be approved. 
* Though the fully productized support envisioned in the proposal is still 2 - 3 releases out, the foundational work is underway, and a motivated cloud provider could accomplish the work in a forward-looking way. Contributors are encouraged to assist with the implementation of the design outlined in the proposal. 
 
#### Some additional context on status / direction: 
* 1.6 added a new cloud-controller-manager binary that may be used for testing the new out-of-core cloudprovider flow.
* Setting cloud-provider=external allows for creation of a separate controller-manager binary
* 1.7 adds [extensible admission control](https://git.k8s.io/community/contributors/design-proposals/admission_control_extension.md), further enabling topology customization. 
This folder contains test cases for interactive edit, and helpers for recording new test cases

To record a new test:

1. Start a local cluster running unsecured on http://localhost:8080 (e.g. hack/local-up-cluster.sh)
2. Set up any pre-existing resources you want to be available on that server (namespaces, resources to edit, etc)
3. Run ./pkg/kubectl/cmd/testdata/edit/record_testcase.sh my-testcase
4. Run the desired `kubectl edit ...` command, and interact with the editor as desired until it completes.
  * You can do things that cause errors to appear in the editor (change immutable fields, fail validation, etc)
  * You can perform edit flows that invoke the editor multiple times
  * You can make out-of-band changes to the server resources that cause conflict errors to be returned
  * The API requests/responses and editor inputs/outputs are captured in your testcase folder
5. Type exit.
6. Inspect the captured requests/responses and inputs/outputs for sanity
7. Modify the generated test.yaml file:
  * Set a description of what the test is doing
  * Enter the args (if any) you invoked edit with
  * Enter the filename (if any) you invoked edit with
  * Enter the output format (if any) you invoked edit with
  * Optionally specify substrings to look for in the stdout or stderr of the edit command
8. Add your new testcase name to the list of testcases in edit_test.go
9. Run `go test ./pkg/kubectl/cmd -run TestEdit -v` to run edit tests
# Cluster Federation

Kubernetes Cluster Federation enables users to federate multiple
Kubernetes clusters. Please see the [user guide](https://kubernetes.io/docs/concepts/cluster-administration/federation-service-discovery/)
and the [admin guide](https://kubernetes.io/docs/tutorials/federation/set-up-cluster-federation-kubefed/)
for more details about setting up and using the Cluster Federation.

# Building Kubernetes Cluster Federation

Please see the [Kubernetes Development Guide](https://github.com/kubernetes/kubernetes/blob/master/docs/devel/development.md)
for initial setup. Once you have the development environment setup
as explained in that guide, you also need to install [`jq`](https://stedolan.github.io/jq/download/)
<!-- TODO(madhusudancs): Re-evaluate using jq even in the development
     environment. There is a concern that adding more tools as dependencies
     might lead to proliferation of tools one need to install to develop
     Kubernetes. jq is already a dependency for kubernetes-anywhere on
     which this workflow depends, so we are giving an exception to jq
     for now. -->

Building cluster federation artifacts should be as simple as running:

```shell
make build
```

You can specify the docker registry to tag the image using the
KUBE_REGISTRY environment variable. Please make sure that you use
the same value in all the subsequent commands.

To push the built docker images to the registry, run:

```shell
make push
```

To initialize the deployment run:

(This pulls the installer images)

```shell
make init
```

To deploy the clusters and install the federation components, edit the
`${KUBE_ROOT}/_output/federation/config.json` file to describe your
clusters and run:

```shell
make deploy
```

To turn down the federation components and tear down the clusters run:

```shell
make destroy
```

# Ideas for improvement

1. Continue with `destroy` phase even in the face of errors.

   The bash script sets `set -e errexit` which causes the script to exit
   at the very first error. This should be the default mode for deploying
   components but not for destroying/cleanup.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/federation/README.md?pixel)]()
# API Reference

Federation API server supports the following group versions:

* federation/v1beta1: [operations](https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/federation/docs/api-reference/federation/v1beta1/operations.html), [model definitions](https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/federation/docs/api-reference/federation/v1beta1/definitions.html)
* v1: [operations](https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/federation/docs/api-reference/v1/operations.html), [model definitions](https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/federation/docs/api-reference/v1/definitions.html)
* extensions/v1beta1: [operations](https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/federation/docs/api-reference/extensions/v1beta1/operations.html), [model definitions](https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/federation/docs/api-reference/extensions/v1beta1/definitions.html)


<!-- BEGIN MUNGE: GENERATED_ANALYTICS -->
[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/federation/docs/api-reference/README.md?pixel)]()
<!-- END MUNGE: GENERATED_ANALYTICS -->
This directory is the staging area for packages that have been split to their
own repository. The content here will be periodically published to respective
top-level k8s.io repositories.

Most code in the `staging/` directory is authoritative, i.e. the only copy of
the code. You can directly modify such code. However the packages in
`staging/src/k8s.io/client-go/pkg` are copied from `pkg/`. If you modify the
original code in `pkg/`, you need to run `hack/godep-restore.sh` from the k8s
root directory, followed by `hack/update-staging-client-go.sh`. We are working
towards making all code in `staging/` authoritative.

The `vendor/k8s.io` directory contains symlinks pointing to this staging area,
so to use a package in the staging area, you can import it as
`k8s.io/<package-name>`, as if the package were vendored. Packages will be
vendored from `k8s.io/<package-name>` for real after the test matrix is
converted to vendor k8s components.
# client-go Examples

This directory contains examples that cover various use cases and functionality
for client-go.

### Configuration

- [**Authenticate in cluster**](./in-cluster-client-configuration): Configure a
  client while running inside the Kubernetes cluster.
- [**Authenticate out of cluster**](./out-of-cluster-client-configuration):
  Configure a client to access a Kubernetes cluster from outside.

### Basics

- [**Managing resources with API**](./create-update-delete-deployment): Create,
  get, update, delete a Deployment resource.

### Advanced Concepts

- [**Work queues**](./workqueue): Create a hotloop-free controller with the
  rate-limited workqueue and the [informer framework][informer].
- [**Third-party resources (deprecated)**](./third-party-resources-deprecated):
  Register a custom resource type with the API, create/update/query this custom
  type, and write a controller drives the cluster state based on the changes to
  the custom resources.

[informer]: https://godoc.org/k8s.io/client-go/tools/cache#NewInformer

# Third Party Resources Example – Deprecated

**Note:** ThirdPartyResources are deprecated since 1.7. The successor is CustomResourceDefinition in the apiextensions.k8s.io API group.

This particular example demonstrates how to perform basic operations such as:

* How to register a new ThirdPartyResource (custom Resource type)
* How to create/get/list instances of your new Resource type (update/delete/etc work as well but are not demonstrated) 
* How to setup a controller on Resource handling create/update/delete events

## Running

```
# assumes you have a working kubeconfig, not required if operating in-cluster
go run *.go -kubeconfig=$HOME/.kube/config
```

## Use Cases

ThirdPartyResources can be used to implement custom Resource types for your Kubernetes cluster.
These act like most other Resources in Kubernetes, and may be `kubectl apply`'d, etc.

Some example use cases:

* Provisioning/Management of external datastores/databases (eg. CloudSQL/RDS instances)
* Higher level abstractions around Kubernetes primitives (eg. a single Resource to define an etcd cluster, backed by a Service and a ReplicationController) 

## Defining types

Each instance of your ThirdPartyResource has an attached Spec, which should be defined via a `struct{}` to provide data format validation.
In practice, this Spec is arbitrary key-value data that specifies the configuration/behavior of your Resource.

For example, if you were implementing a ThirdPartyResource for a Database, you might provide a DatabaseSpec like the following:

``` go
type DatabaseSpec struct {
	Databases []string `json:"databases"`
	Users     []User   `json:"users"`
	Version   string   `json:"version"`
}

type User struct {
	Name     string `json:"name"`
	Password string `json:"password"`
}
```# Workqueue Example

This example demonstrates how to write a controller which follows the states
of watched resources.

It demonstrates how to:
 * combine the workqueue with a cache to a full controller
 * synchronize the controller on startup

The example is based on https://git.k8s.io/community/contributors/devel/controllers.md.

## Running

```
# if outside of the cluster
go run *.go -kubeconfig=/my/config -logtostderr=true
```
# Create, Update & Delete Deployment

This example program demonstrates the fundamental operations for managing on
[Deployment][1] resources, such as `Create`, `List`, `Update` and `Delete`.

You can adopt the source code from this example to write programs that manage
other types of resources through the Kubernetes API.

## Running this example

Make sure you have a Kubernetes cluster and `kubectl` is configured:

    kubectl get nodes

Compile this example on your workstation:

```
cd create-update-delete-deployment
go build -o ./app
```

Now, run this application on your workstation with your local kubeconfig file:

```
./app -kubeconfig=$HOME/.kube/config
```

Running this command will execute the following operations on your cluster:

1. **Create Deployment:** This will create a 2 replica Deployment. Verify with
   `kubectl get pods`.
2. **Update Deployment:** This will update the Deployment resource created in
   previous step to set the replica count to 1 and add annotations. You are
   encouraged to inspect the retry loop that handles conflicts. Verify the new
   replica count and `foo=bar` annotation with `kubectl describe deployment
   demo`.
3. **List Deployments:** This will retrieve Deployments in the `default`
   namespace and print their names and replica counts.
4. **Delete Deployment:** This will delete the Deployment object and its
   dependent ReplicaSet resource. Verify with `kubectl get deployments`.

Each step is separated by an interactive prompt. You must hit the
<kbd>Return</kbd> key to proceeed to the next step. You can use these prompts as
a break to take time to  run `kubectl` and inspect the result of the operations
executed.

You should see an output like the following:

```
Creating deployment...
Created deployment "demo-deployment".
-> Press Return key to continue.

Updating deployment...
Updated deployment...
-> Press Return key to continue.

Listing deployments in namespace "default":
 * demo-deployment (1 replicas)
-> Press Return key to continue.

Deleting deployment...
Deleted deployment.
```

## Cleanup

Successfully running this program will clean the created artifacts. If you
terminate the program without completing, you can clean up the created
deployment with:

    kubectl delete deploy demo-deployment

## Troubleshooting

If you are getting the following error, make sure Kubernetes version of your
cluster is v1.6 or above in `kubectl version`:

    panic: the server could not find the requested resource

[1]: https://kubernetes.io/docs/user-guide/deployments/
# Authenticating outside the cluster

This example shows you how to configure a client with client-go to authenticate
to the Kubernetes API from an application running outside the Kubernetes
cluster.

You can use your kubeconfig file that contains the context information
of your cluster to initialize a client. The kubeconfig file is also used
by the `kubectl` command to authenticate to the clusters.

## Running this example

Make sure your `kubectl` is configured and pointed to a cluster. Run
`kubectl get nodes` to confirm.

Run this application with:

    cd out-of-cluster-client-configuration
    go build -o app .
    ./app

Running this application will use the kubeconfig file and then authenticate to the
cluster, and print the number of nodes in the cluster every 10 seconds:

    $ ./app
    There are 3 pods in the cluster
    There are 3 pods in the cluster
    There are 3 pods in the cluster
    ...

Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to quit this application.

> **Note:** You can use the `-kubeconfig` option to use a different config file. By default
this program picks up the default file used by kubectl (when `KUBECONFIG`
environment variable is not set).
# Authenticating inside the cluster

This example shows you how to configure a client with client-go to authenticate
to the Kubernetes API from an application running inside the Kubernetes cluster.

client-go uses the [Service Account token][sa] mounted inside the Pod at the
`/var/run/secrets/kubernetes.io/serviceaccount` path when the
`rest.InClusterConfig()` is used.

## Running this example

First compile the application for Linux:

    cd in-cluster-client-configuration
    GOOS=linux go build -o ./app .

Then package it to a docker image using the provided Dockerfile to run it on
Kubernetes.

If you are running a [Minikube][mk] cluster, you can build this image directly
on the Docker engine of the Minikube node without pushing it to a registry. To
build the image on Minikube:

    eval $(minikube docker-env)
    docker build -t in-cluster .

If you are not using Minikube, you should build this image and push it to a registry
that your Kubernetes cluster can pull from.

Then, run the image in a Pod with a single instance Deployment:

    $ kubectl run --rm -i demo --image=in-cluster --image-pull-policy=Never

    There are 4 pods in the cluster
    There are 4 pods in the cluster
    There are 4 pods in the cluster
    ...

The example now runs on Kubernetes API and successfully queries the number of
pods in the cluster every 10 seconds.

### Clean up

To stop this example and clean up the pod, press <kbd>Ctrl</kbd>+<kbd>C</kbd> on
the `kubectl run` command and then run:

    kubectl delete deployment demo

[sa]: https://kubernetes.io/docs/admin/authentication/#service-account-tokens
[mk]: https://kubernetes.io/docs/getting-started-guides/minikube/
# Custom Resource Example

**Note:** CustomResourceDefinition is the successor of the deprecated ThirdPartyResource.

For a client-go example using CustomResourceDefinitions, go to

  [k8s.io/apiextensions-apiserver/examples/client-go](https://git.k8s.io/apiextensions-apiserver/examples/client-go).
# Azure Active Directory plugin for client authentication

This plugin provides an integration with Azure Active Directory device flow. If no tokens are present in the kubectl configuration, it will prompt a device code which can be used to login in a browser. After login it will automatically fetch the tokens and stored them in the kubectl configuration. In addition it will refresh and update the tokens in configuration when expired.


## Usage

1. Create an Azure Active Directory *Web App / API* application for `apiserver` following these [instructions](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-app-registration)

2. Create a second Azure Active Directory native application for `kubectl` 

3. On `kubectl` application's configuration page in Azure portal grant permissions to `apiserver` application by clicking on *Required Permissions*, click the *Add* button and search for the apiserver application created in step 1. Select "Access apiserver" under the *DELEGATED PERMISSIONS*. Once added click the *Grant Permissions* button to apply the changes

4. Configure the `apiserver` to use the Azure Active Directory as an OIDC provider with following options

   ```
   --oidc-client-id="spn:APISERVER_APPLICATION_ID" \
   --oidc-issuer-url="https://sts.windows.net/TENANT_ID/"
   --oidc-username-claim="sub"
   ```

   * Replace the `APISERVER_APPLICATION_ID` with the application ID of `apiserver` application
   * Replace `TENANT_ID` with your tenant ID.

5. Configure the `kubectl` to use the `azure` authentication provider 

   ```
   kubectl config set-credentials "USER_NAME" --auth-provider=azure \
     --auth-provider-arg=environment=AzurePublicCloud \
     --auth-provider-arg=client-id=APPLICATION_ID \
     --auth-provider-arg=tenant-id=TENANT_ID \
     --auth-provider-arg=apiserver-id=APISERVER_APPLICATION_ID
   ```

   * Supported environments: `AzurePublicCloud`, `AzureUSGovernmentCloud`, `AzureChinaCloud`, `AzureGermanCloud`
   * Replace `USER_NAME` and `TENANT_ID` with your user name and tenant ID
   * Replace `APPLICATION_ID` with the application ID of your`kubectl` application ID
   * Replace `APISERVER_APPLICATION_ID` with the application ID of your `apiserver` application ID 

 6. The access token is acquired when first `kubectl` command is executed

   ```
   kubectl get pods

   To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code DEC7D48GA to authenticate.
   ```

   * After signing in a web browser, the token is stored in the configuration, and it will be reused when executing next commands.
# Custom Resource Example

**Note:** CustomResourceDefinition is the successor of the deprecated ThirdPartyResource.

This particular example demonstrates how to perform basic operations such as:

* How to register a new custom resource (custom resource type) using a CustomResourceDefinition
* How to create/get/list instances of your new resource type (update/delete/etc work as well but are not demonstrated)
* How to setup a controller on resource handling create/update/delete events

## Running

```
# assumes you have a working kubeconfig, not required if operating in-cluster
go run *.go -kubeconfig=$HOME/.kube/config
```

## Use Cases

CustomResourceDefinitions can be used to implement custom resource types for your Kubernetes cluster.
These act like most other Resources in Kubernetes, and may be `kubectl apply`'d, etc.

Some example use cases:

* Provisioning/Management of external datastores/databases (eg. CloudSQL/RDS instances)
* Higher level abstractions around Kubernetes primitives (eg. a single Resource to define an etcd cluster, backed by a Service and a ReplicationController) 

## Defining types

Each instance of your custom resource has an attached Spec, which should be defined via a `struct{}` to provide data format validation.
In practice, this Spec is arbitrary key-value data that specifies the configuration/behavior of your Resource.

For example, if you were implementing a custom resource for a Database, you might provide a DatabaseSpec like the following:

``` go
type DatabaseSpec struct {
	Databases []string `json:"databases"`
	Users     []User   `json:"users"`
	Version   string   `json:"version"`
}

type User struct {
	Name     string `json:"name"`
	Password string `json:"password"`
}
```The datafiles contained in these directories were generated by the script
```sh
hack/build-ui.sh
```

Do not edit by hand.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/pkg/genericapiserver/addons/data/README.md?pixel)]()


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/pkg/genericapiserver/server/routes/data/README.md?pixel)]()
This file has moved to [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/README.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/README.md)
This file has moved to [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/clustering/README.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/clustering/README.md)
This file has moved to [https://github.com/kubernetes/community/blob/master/contributors/devel/README.md](https://github.com/kubernetes/community/blob/master/contributors/devel/README.md)
See [generating-clientset.md](https://kubernetes.io/docs/devel/generating-clientset.md)


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cmd/libs/go2idl/client-gen/README.md?pixel)]()
This dir can not be named "testdata" because of the way ugorji gnerates code.
Specifically, it emits a .go file and then calls `go run` on it.  Because
"testdata" is a special name to Go, it decides NOT to find the vendor dir, and
therefore fails to compile.  Just name it something else.
# Generate OpenAPI definitions

- To generate definition for a specific type or package add "+k8s:openapi-gen=true" tag to the type/package comment lines.
- To exclude a type or a member from a tagged package/type, add "+k8s:openapi-gen=false" tag to the comment lines.

# OpenAPI Extensions
OpenAPI spec can have extensions on types. To define one or more extensions on a type or its member
add "+k8s:openapi-gen=x-kubernetes-$NAME:$VALUE" to the comment lines before type/member. A type/member can
have multiple extensions. The rest of the line in the comment will be used as $VALUE so there is no need to
escape or quote the value string. Extensions can be use to pass more information to client generators or
documentation generators. For example a type my have a friendly name to be displayed in documentation or
being used in a client's fluent interface.

# Documentation Mungers

Basically this is like lint/gofmt for md docs.

It basically does the following:
- iterate over all files in the given doc root.
- for each file split it into a slice (mungeLines) of lines (mungeLine)
- a mungeline has metadata about each line typically determined by a 'fast' regex.
  - metadata contains things like 'is inside a preformatted block'
  - contains a markdown header
  - has a link to another file
  - etc..
  - if you have a really slow regex with a lot of backtracking you might want to write a fast one to limit how often you run the slow one.
- each munger is then called in turn
  - they are given the mungeLines
  - they create an entirely new set of mungeLines with their modifications
  - the new set is returned
- the new set is then fed into the next munger.
- in the end we might commit the end mungeLines to the file or not (--verify)


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cmd/mungedocs/README.md?pixel)]()
some text
# Cluster Configuration

##### Deprecation Notice: This directory has entered maintenance mode and will not be accepting new providers. Please submit new automation deployments to [kube-deploy](https://github.com/kubernetes/kube-deploy). Deployments in this directory will continue to be maintained and supported at their current level of support.

The scripts and data in this directory automate creation and configuration of a Kubernetes cluster, including networking, DNS, nodes, and master components.

See the [getting-started guides](https://kubernetes.io/docs/getting-started-guides) for examples of how to use the scripts.

*cloudprovider*/`config-default.sh` contains a set of tweakable definitions/parameters for the cluster.

The heavy lifting of configuring the VMs is done by [SaltStack](http://www.saltstack.com/).


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/README.md?pixel)]()
### hyperkube

`hyperkube` is an all-in-one binary for the Kubernetes server components
`hyperkube` is built for multiple architectures and _the image is pushed automatically on every release._

#### How to release by hand

```console
# First, build the binaries
$ build/run.sh make cross

# Build for linux/amd64 (default)
# export REGISTRY=$HOST/$ORG to switch from gcr.io/google_containers

$ make push VERSION={target_version} ARCH=amd64
# ---> gcr.io/google_containers/hyperkube-amd64:VERSION
# ---> gcr.io/google_containers/hyperkube:VERSION (image with backwards-compatible naming)

$ make push VERSION={target_version} ARCH=arm
# ---> gcr.io/google_containers/hyperkube-arm:VERSION

$ make push VERSION={target_version} ARCH=arm64
# ---> gcr.io/google_containers/hyperkube-arm64:VERSION

$ make push VERSION={target_version} ARCH=ppc64le
# ---> gcr.io/google_containers/hyperkube-ppc64le:VERSION

$ make push VERSION={target_version} ARCH=s390x
# ---> gcr.io/google_containers/hyperkube-s390x:VERSION
```

If you don't want to push the images, run `make` or `make build` instead


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/images/hyperkube/README.md?pixel)]()
# etcd-version-monitor

This is a tool for exporting metrics related to etcd version, like etcd
server's binary version, cluster version, and counts of different kinds of
gRPC calls (which is a characteristic of v3), etc. These metrics are in
prometheus format and can be scraped by a prometheus server.
The metrics are exposed at the http://localhost:9101/metrics endpoint.

**RUNNING THE TOOL**

To run this tool as a docker container:
- make build
- docker run --net=host -i -t gcr.io/google_containers/etcd-version-monitor:test /etcd-version-monitor --logtostderr

To run this as a pod on the kubernetes cluster:
- Place the 'etcd-version-monitor.yaml' in the manifests directory of
  kubelet on the master machine.

*Note*: This tool has to run on the same machine as etcd, as communication
with etcd is over localhost.

**VERIFYING THE TOOL**

- Goto [http://localhost:9101/metrics](http://localhost:9101/metrics) in order to view the exported metrics.
- The metrics prefixed with "etcd_" are the ones of interest to us.
### etcd

This is a small etcd image used in Kubernetes setups where `etcd` is deployed as a docker image.

For `amd64`, official `etcd` and `etcdctl` binaries are downloaded from Github to maintain official support.
For other architectures, `etcd` is cross-compiled from source. Arch-specific `busybox` images serve as base images.

#### How to release

```console
# Build for linux/amd64 (default)
$ make push ARCH=amd64
# ---> gcr.io/google_containers/etcd-amd64:TAG
# ---> gcr.io/google_containers/etcd:TAG

$ make push ARCH=arm
# ---> gcr.io/google_containers/etcd-arm:TAG

$ make push ARCH=arm64
# ---> gcr.io/google_containers/etcd-arm64:TAG

$ make push ARCH=ppc64le
# ---> gcr.io/google_containers/etcd-ppc64le:TAG

$ make push ARCH=s390x
# ---> gcr.io/google_containers/etcd-s390x:TAG
```

If you don't want to push the images, run `make` or `make build` instead


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/images/etcd/README.md?pixel)]()
# Rollback workflow

Build it in this directory.
Make sure you have etcd dependency ready. Last time we use etcd v3.0.7.
```
$ go build .
```


Run it:
```
$ ./rollback2 --data-dir $ETCD_DATA_DIR --ttl 1h
```

This will rollback KV pairs from v3 into v2.
If a key was attached to a lease before, it will be created with given TTL (default to 1h).

On success, it will print at the end:
```
Finished successfully
```

Repeat this on all etcd members.

You can do simple check on keys (if any exists):
```
etcdctl ls /
```

Important Note
------

This tool isn't recommended to use if any problem comes up in etcd3 backend.
Please report bugs and we will fix it soon.

If it's still preferred to run this tool, please backup all your data beforehand.
This tool will also back up datadir to same path with ".rollback.backup" suffix.

Caveats:
- The tool doesn't preserve versions of keys.
- If any v2 data exists before rollback, they will be wiped out.
- v3 data only exists in the backup after successful rollback.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/images/etcd/rollback/README.md?pixel)]()# Cluster add-ons

## Overview

Cluster add-ons are resources like Services and Deployments (with pods) that are
shipped with the Kubernetes binaries and are considered an inherent part of the
Kubernetes clusters.

There are currently two classes of add-ons:
- Add-ons that will be reconciled.
- Add-ons that will be created if they don't exist.

More details could be found in [addon-manager/README.md](addon-manager/README.md).

## Cooperating Horizontal / Vertical Auto-Scaling with "reconcile class addons"

"Reconcile" class addons will be periodically reconciled to the original state given
by the initial config. In order to make Horizontal / Vertical Auto-scaling functional,
the related fields in config should be left unset. More specifically, leave `replicas`
in `ReplicationController` / `Deployment` / `ReplicaSet` unset for Horizontal Scaling,
leave `resources` for container unset for Vertical Scaling. The periodic reconcile
won't clobbered these fields, hence they could be managed by Horizontal / Vertical
Auto-scaler.

## Add-on naming

The suggested naming for most of the resources is `<basename>` (with no version number).
Though resources like `Pod`, `ReplicationController` and `DaemonSet` are exceptional.
It would be hard to update `Pod` because many fields in `Pod` are immutable. For
`ReplicationController` and `DaemonSet`, in-place update may not trigger the underlying
pods to be re-created. You probably need to change their names during update to trigger
a complete deletion and creation.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/README.md?pixel)]()
### Addon-manager

addon-manager manages two classes of addons with given template files.
- Addons with label `addonmanager.kubernetes.io/mode=Reconcile` will be periodically
reconciled. Direct manipulation to these addons through apiserver is discouraged because
addon-manager will bring them back to the original state. In particular:
	- Addon will be re-created if it is deleted.
	- Addon will be reconfigured to the state given by the supplied fields in the template
	file periodically.
	- Addon will be deleted when its manifest file is deleted.
- Addons with label `addonmanager.kubernetes.io/mode=EnsureExists` will be checked for
existence only. Users can edit these addons as they want. In particular:
	- Addon will only be created/re-created with the given template file when there is no
	instance of the resource with that name.
	- Addon will not be deleted when the manifest file is deleted.

Notes:
- Label `kubernetes.io/cluster-service=true` is deprecated (only for Addon Manager).
In future release (after one year), Addon Manager may not respect it anymore. Addons
have this label but without `addonmanager.kubernetes.io/mode=EnsureExists` will be
treated as "reconcile class addons" for now.
- Resources under $ADDON_PATH (default `/etc/kubernetes/addons/`) needs to have either one
of these two labels. Meanwhile namespaced resources need to be in `kube-system` namespace.
Otherwise it will be omitted.
- The above label and namespace rule does not stand for `/opt/namespace.yaml` and
resources under `/etc/kubernetes/admission-controls/`. addon-manager will attempt to
create them regardless during startup.

#### How to release

The `addon-manager` is built for multiple architectures.

1. Change something in the source
2. Bump `VERSION` in the `Makefile`
3. Bump `KUBECTL_VERSION` in the `Makefile` if required
4. Build the `amd64` image and test it on a cluster
5. Push all images

```console
# Build for linux/amd64 (default)
$ make push ARCH=amd64
# ---> gcr.io/google-containers/kube-addon-manager-amd64:VERSION
# ---> gcr.io/google-containers/kube-addon-manager:VERSION (image with backwards-compatible naming)

$ make push ARCH=arm
# ---> gcr.io/google-containers/kube-addon-manager-arm:VERSION

$ make push ARCH=arm64
# ---> gcr.io/google-containers/kube-addon-manager-arm64:VERSION

$ make push ARCH=ppc64le
# ---> gcr.io/google-containers/kube-addon-manager-ppc64le:VERSION

$ make push ARCH=s390x
# ---> gcr.io/google-containers/kube-addon-manager-s390x:VERSION
```

If you don't want to push the images, run `make` or `make build` instead


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/addon-manager/README.md?pixel)]()
# Python image

The python image here is used by OS distros that don't have python installed to
run python scripts to parse the yaml files in the addon updater script.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/python-image/README.md?pixel)]()
# Calico Policy Controller
==============

Calico is an implementation of the Kubernetes network policy API.  The provided manifests install:

- A DaemonSet which runs Calico on each node in the cluster.
- A Deployment which installs the Calico Typha agent.
- A Service for the Calico Typha agent.

### Learn More

Learn more about Calico at http://docs.projectcalico.org

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/calico-policy-controller/README.md?pixel)]()
# Stackdriver Logging Agent
==============

Stackdriver Logging Agent is a DaemonSet which spawns a pod on each node
that reads logs, generated by kubelet, container runtime and containers
and sends them to the Stackdriver. When logs are exported to the Stackdriver,
they can be searched, viewed, and analyzed.

Learn more at: https://kubernetes.io/docs/tasks/debug-application-cluster/logging-stackdriver

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/fluentd-gcp/README.md?pixel)]()
# Collecting Docker Log Files with Fluentd and sending to GCP.

The image was moved to the the
[new location](https://github.com/kubernetes/contrib/tree/master/fluentd/fluentd-gcp-image).

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/fluentd-gcp/fluentd-gcp-image/README.md?pixel)]()
# Node Problem Detector
==============

Node Problem Detector is a DaemonSet running on each node, detecting node
problems.

Learn more at: https://github.com/kubernetes/node-problem-detector


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/node-problem-detector/README.md?pixel)]()
# Kubernetes Dashboard
==============

Kubernetes Dashboard is a general purpose, web-based UI for Kubernetes clusters.
It allows users to manage applications running in the cluster, troubleshoot them,
as well as manage the cluster itself.

Learn more at: https://github.com/kubernetes/dashboard


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/dashboard/README.md?pixel)]()
# Logging Agent For Elasticsearch
==============

Logging Agent For Elasticsearch is a DaemonSet which spawns a pod on each node
that reads logs, generated by kubelet, container runtime and containers
and sends them to Elasticsearch, deployed in the cluster. Later logs can be
accessed either by querying Elasticsearch directly or by using Kibana.

Learn more at: https://kubernetes.io/docs/tasks/debug-application-cluster/logging-elasticsearch-kibana

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/fluentd-elasticsearch/README.md?pixel)]()
# Collecting Docker Log Files with Fluentd and Elasticsearch
This directory contains the source files needed to make a Docker image
that collects Docker container log files using [Fluentd](http://www.fluentd.org/)
and sends them to an instance of [Elasticsearch](http://www.elasticsearch.org/).
This image is designed to be used as part of the [Kubernetes](https://github.com/kubernetes/kubernetes)
cluster bring up process. The image resides at DockerHub under the name
[kubernetes/fluentd-elasticsearch](https://registry.hub.docker.com/u/kubernetes/fluentd-elasticsearch/).


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/fluentd-elasticsearch/fluentd-es-image/README.md?pixel)]()
# kube-dns

`kube-dns` schedules DNS Pods and Service on the cluster, other pods in cluster
can use the DNS Service’s IP to resolve DNS names.

* [Administrators guide](http://kubernetes.io/docs/admin/dns/)
* [Code repository](http://www.github.com/kubernetes/dns)

## Manually scale kube-dns Deployment

kube-dns creates only one DNS Pod by default. If
[dns-horizontal-autoscaler](../dns-horizontal-autoscaler/)
is not enabled, you may need to manually scale kube-dns Deployment.

Please use below `kubectl scale` command to scale:
```
kubectl --namespace=kube-system scale deployment kube-dns --replicas=<NUM_YOU_WANT>
```

Do not use `kubectl edit` to modify kube-dns Deployment object if it is
controlled by [Addon Manager](../addon-manager/). Otherwise the modifications
will be clobbered, in addition the replicas count for kube-dns Deployment will
be reset to 1. See [Cluster add-ons README](../README.md) and
[#36411](https://github.com/kubernetes/kubernetes/issues/36411) for reference.

## kube-dns Deployment and Service templates

This directory contains the base UNDERSCORE templates that can be used to
generate the kubedns-controller.yaml.in and kubedns.controller.yaml.in needed in
Salt format.

Due to a varied preference in templating language choices, the transform
Makefile in this directory should be enhanced to generate all required formats
from the base underscore templates.

**N.B.**: When you add a parameter you should also update the various scripts
that supply values for your new parameter.  Here is one way you might find those
scripts:

```
cd kubernetes && git grep 'kubedns-controller.yaml'
```

### Base Template files

These are the authoritative base templates.
Run 'make' to generate the Salt and Sed yaml templates from these.

```
kubedns-controller.yaml.base
kubedns-svc.yaml.base
```

### Generated Salt files

```
kubedns-controller.yaml.in
kubedns-svc.yaml.in
```

### Generated Sed files

```
kubedns-controller.yaml.sed
kubedns-svc.yaml.sed
```

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/dns/README.md?pixel)]()
# GCE Load-Balancer Controller (GLBC) Cluster Addon

This cluster addon is composed of:
* A [Google L7 LoadBalancer Controller](https://github.com/kubernetes/contrib/tree/master/ingress/controllers/gce)
* A [404 default backend](https://github.com/kubernetes/contrib/tree/master/404-server) Service + RC

It relies on the [Ingress resource](https://kubernetes.io/docs/user-guide/ingress.md) only available in Kubernetes version 1.1 and beyond.

## Prerequisites

Before you can receive traffic through the GCE L7 Loadbalancer Controller you need:
* A Working Kubernetes 1.1 cluster
* At least 1 Kubernetes [NodePort Service](https://kubernetes.io/docs/user-guide/services.md#type-nodeport) (this is the endpoint for your Ingress)
* Firewall-rules that allow traffic to the NodePort service, as indicated by `kubectl` at Service creation time
* Adequate quota, as mentioned in the next section
* A single instance of the L7 Loadbalancer Controller pod (if you're using the default GCE setup, this should already be running in the `kube-system` namespace)

## Quota

GLBC is not aware of your GCE quota. As of this writing users get 3 [GCE Backend Services](https://cloud.google.com/compute/docs/load-balancing/http/backend-service) by default. If you plan on creating Ingresses for multiple Kubernetes Services, remember that each one requires a backend service, and request quota. Should you fail to do so the controller will poll periodically and grab the first free backend service slot it finds. You can view your quota:

```console
$ gcloud compute project-info describe --project myproject
```
See [GCE documentation](https://cloud.google.com/compute/docs/resource-quotas#checking_your_quota) for how to request more.

## Latency

It takes ~1m to spin up a loadbalancer (this includes acquiring the public ip), and ~5-6m before the GCE api starts healthchecking backends. So as far as latency goes, here's what to expect:

Assume one creates the following simple Ingress:
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: test-ingress
spec:
  backend:
    # This will just loopback to the default backend of GLBC
    serviceName: default-http-backend
    servicePort: 80
```

* time, t=0
```console
$ kubectl get ing
NAME           RULE      BACKEND                   ADDRESS
test-ingress   -         default-http-backend:80
$ kubectl describe ing
No events.
```

* time, t=1m
```console
$ kubectl get ing
NAME           RULE      BACKEND                   ADDRESS
test-ingress   -         default-http-backend:80   130.211.5.27

$ kubectl describe ing
target-proxy:		k8s-tp-default-test-ingress
url-map:		    k8s-um-default-test-ingress
backends:		    {"k8s-be-32342":"UNKNOWN"}
forwarding-rule:	k8s-fw-default-test-ingress
Events:
  FirstSeen	LastSeen	Count	From				SubobjectPath	Reason	Message
  ─────────	────────	─────	────				─────────────	──────	───────
  46s		46s		1	{loadbalancer-controller }	Success	Created loadbalancer 130.211.5.27
```

* time, t=5m
```console
$ kubectl describe ing
target-proxy:		k8s-tp-default-test-ingress
url-map:		    k8s-um-default-test-ingress
backends:		    {"k8s-be-32342":"HEALTHY"}
forwarding-rule:	k8s-fw-default-test-ingress
Events:
  FirstSeen	LastSeen	Count	From				SubobjectPath	Reason	Message
  ─────────	────────	─────	────				─────────────	──────	───────
  46s		46s		1	{loadbalancer-controller }	Success	Created loadbalancer 130.211.5.27

```

## Disabling GLBC

Since GLBC runs as a cluster addon, you cannot simply delete the RC. The easiest way to disable it is to do as follows:

* IFF you want to tear down existing L7 loadbalancers, hit the /delete-all-and-quit endpoint on the pod:

```console
$ kubectl get pods --namespace=kube-system
NAME                                               READY     STATUS    RESTARTS   AGE
l7-lb-controller-7bb21                             1/1       Running   0          1h
$ kubectl exec l7-lb-controller-7bb21 -c l7-lb-controller curl http://localhost:8081/delete-all-and-quit --namespace=kube-system
$ kubectl logs l7-lb-controller-7b221 -c l7-lb-controller --follow
...
I1007 00:30:00.322528       1 main.go:160] Handled quit, awaiting pod deletion.
```

* Nullify the RC (but don't delete it or the addon controller will "fix" it for you)
```console
$ kubectl scale rc l7-lb-controller --replicas=0 --namespace=kube-system
```

## Limitations

* This cluster addon is still in the Beta phase. It behooves you to read through the GLBC documentation mentioned above and make sure there are no surprises.
* The recommended way to tear down a cluster with active Ingresses is to either delete each Ingress, or hit the /delete-all-and-quit endpoint on GLBC as described below, before invoking a cluster teardown script (eg: kube-down.sh). You will have to manually cleanup GCE resources through the [cloud console](https://cloud.google.com/compute/docs/console#access) or [gcloud CLI](https://cloud.google.com/compute/docs/gcloud-compute/) if you simply tear down the cluster with active Ingresses.
* All L7 Loadbalancers created by GLBC have a default backend. If you don't specify one in your Ingress, GLBC will assign the 404 default backend mentioned above.
* All Kubernetes services must serve a 200 page on '/', or whatever custom value you've specified through GLBC's `--health-check-path argument`.
* GLBC is not built for performance. Creating many Ingresses at a time can overwhelm it. It won't fall over, but will take its own time to churn through the Ingress queue. It doesn't understand concepts like fairness or backoff just yet.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/cluster-loadbalancing/glbc/README.md?pixel)]()
# DNS Horizontal Autoscaler

DNS Horizontal Autoscaler enables horizontal autoscaling feature for DNS service
in Kubernetes clusters. This autoscaler runs as a Deployment. It collects cluster
status from the APIServer, horizontally scales the number of DNS backends based
on demand. Autoscaling parameters could be tuned by modifying the `kube-dns-autoscaler`
ConfigMap in `kube-system` namespace.

Learn more about:
- Usage: http://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
- Implementation: https://github.com/kubernetes-incubator/cluster-proportional-autoscaler/


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/dns-horizontal-autoscaler/README.md?pixel)]()
# Kubernetes Monitoring

[Heapster](https://github.com/kubernetes/heapster) enables monitoring and performance analysis in Kubernetes Clusters.
Heapster collects signals from kubelets and the api server, processes them, and exports them via REST APIs or to a configurable timeseries storage backend.

More details can be found in [Monitoring user guide](http://kubernetes.io/docs/user-guide/monitoring/).

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/cluster-monitoring/README.md?pixel)]()
# Metadata proxy
==============

This metadata proxy returns a 403 for kubelet's kube-env data, but otherwise allows
pods access to the metadata server.
# Private Docker Registry in Kubernetes

Kubernetes offers an optional private Docker registry addon, which you can turn
on when you bring up a cluster or install later.  This gives you a place to
store truly private Docker images for your cluster.

## How it works

The private registry runs as a `Pod` in your cluster.  It does not currently
support SSL or authentication, which triggers Docker's "insecure registry"
logic.  To work around this, we run a proxy on each node in the cluster,
exposing a port onto the node (via a hostPort), which Docker accepts as
"secure", since it is accessed by `localhost`.

## Turning it on

Some cluster installs (e.g. GCE) support this as a cluster-birth flag.  The
`ENABLE_CLUSTER_REGISTRY` variable in `cluster/gce/config-default.sh` governs
whether the registry is run or not.  To set this flag, you can specify
`KUBE_ENABLE_CLUSTER_REGISTRY=true` when running `kube-up.sh`.  If your cluster
does not include this flag, the following steps should work.  Note that some of
this is cloud-provider specific, so you may have to customize it a bit.

### Make some storage

The primary job of the registry is to store data.  To do that we have to decide
where to store it.  For cloud environments that have networked storage, we can
use Kubernetes's `PersistentVolume` abstraction.  The following template is
expanded by `salt` in the GCE cluster turnup, but can easily be adapted to
other situations:

<!-- BEGIN MUNGE: EXAMPLE registry-pv.yaml.in -->
```yaml
kind: PersistentVolume
apiVersion: v1
metadata:
  name: kube-system-kube-registry-pv
  labels:
    kubernetes.io/cluster-service: "true"
spec:
{% if pillar.get('cluster_registry_disk_type', '') == 'gce' %}
  capacity:
    storage: {{ pillar['cluster_registry_disk_size'] }}
  accessModes:
    - ReadWriteOnce
  gcePersistentDisk:
    pdName: "{{ pillar['cluster_registry_disk_name'] }}"
    fsType: "ext4"
{% endif %}
```
<!-- END MUNGE: EXAMPLE registry-pv.yaml.in -->

If, for example, you wanted to use NFS you would just need to change the
`gcePersistentDisk` block to `nfs`. See
[here](https://kubernetes.io/docs/user-guide/volumes.md) for more details on volumes.

Note that in any case, the storage (in the case the GCE PersistentDisk) must be
created independently - this is not something Kubernetes manages for you (yet).

### I don't want or don't have persistent storage

If you are running in a place that doesn't have networked storage, or if you
just want to kick the tires on this without committing to it, you can easily
adapt the `ReplicationController` specification below to use a simple
`emptyDir` volume instead of a `persistentVolumeClaim`.

## Claim the storage

Now that the Kubernetes cluster knows that some storage exists, you can put a
claim on that storage.  As with the `PersistentVolume` above, you can start
with the `salt` template:

<!-- BEGIN MUNGE: EXAMPLE registry-pvc.yaml.in -->
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: kube-registry-pvc
  namespace: kube-system
  labels:
    kubernetes.io/cluster-service: "true"
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: {{ pillar['cluster_registry_disk_size'] }}
```
<!-- END MUNGE: EXAMPLE registry-pvc.yaml.in -->

This tells Kubernetes that you want to use storage, and the `PersistentVolume`
you created before will be bound to this claim (unless you have other
`PersistentVolumes` in which case those might get bound instead).  This claim
gives you the right to use this storage until you release the claim.

## Run the registry

Now we can run a Docker registry:

<!-- BEGIN MUNGE: EXAMPLE registry-rc.yaml -->
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: kube-registry-v0
  namespace: kube-system
  labels:
    k8s-app: kube-registry-upstream
    version: v0
    kubernetes.io/cluster-service: "true"
spec:
  replicas: 1
  selector:
    k8s-app: kube-registry-upstream
    version: v0
  template:
    metadata:
      labels:
        k8s-app: kube-registry-upstream
        version: v0
        kubernetes.io/cluster-service: "true"
    spec:
      containers:
      - name: registry
        image: registry:2
        resources:
          limits:
            cpu: 100m
            memory: 100Mi
        env:
        - name: REGISTRY_HTTP_ADDR
          value: :5000
        - name: REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY
          value: /var/lib/registry
        volumeMounts:
        - name: image-store
          mountPath: /var/lib/registry
        ports:
        - containerPort: 5000
          name: registry
          protocol: TCP
      volumes:
      - name: image-store
        persistentVolumeClaim:
          claimName: kube-registry-pvc
```
<!-- END MUNGE: EXAMPLE registry-rc.yaml -->

## Expose the registry in the cluster

Now that we have a registry `Pod` running, we can expose it as a Service:

<!-- BEGIN MUNGE: EXAMPLE registry-svc.yaml -->
```yaml
apiVersion: v1
kind: Service
metadata:
  name: kube-registry
  namespace: kube-system
  labels:
    k8s-app: kube-registry-upstream
    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: "KubeRegistry"
spec:
  selector:
    k8s-app: kube-registry-upstream
  ports:
  - name: registry
    port: 5000
    protocol: TCP
```
<!-- END MUNGE: EXAMPLE registry-svc.yaml -->

## Expose the registry on each node

Now that we have a running `Service`, we need to expose it onto each Kubernetes
`Node` so that Docker will see it as `localhost`.  We can load a `Pod` on every
node by creating following daemonset.

<!-- BEGIN MUNGE: EXAMPLE ../../saltbase/salt/kube-registry-proxy/kube-registry-proxy.yaml -->
```yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: kube-registry-proxy
  namespace: kube-system
  labels:
    k8s-app: kube-registry-proxy
    kubernetes.io/cluster-service: "true"
    version: v0.4
spec:
  template:
    metadata:
      labels:
        k8s-app: kube-registry-proxy
        kubernetes.io/name: "kube-registry-proxy"
        kubernetes.io/cluster-service: "true"
        version: v0.4
    spec:
      containers:
      - name: kube-registry-proxy
        image: gcr.io/google_containers/kube-registry-proxy:0.4
        resources:
          limits:
            cpu: 100m
            memory: 50Mi
        env:
        - name: REGISTRY_HOST
          value: kube-registry.kube-system.svc.cluster.local
        - name: REGISTRY_PORT
          value: "5000"
        ports:
        - name: registry
          containerPort: 80
          hostPort: 5000
```
<!-- END MUNGE: EXAMPLE ../../saltbase/salt/kube-registry-proxy/kube-registry-proxy.yaml -->

When modifying replication-controller, service and daemon-set defintions, take
care to ensure _unique_ identifiers for the rc-svc couple and the daemon-set.
Failing to do so will have register the localhost proxy daemon-sets to the
upstream service. As a result they will then try to proxy themselves, which
will, for obvious reasons, not work.

This ensures that port 5000 on each node is directed to the registry `Service`.
You should be able to verify that it is running by hitting port 5000 with a web
browser and getting a 404 error:

```console
$ curl localhost:5000
404 page not found
```

## Using the registry

To use an image hosted by this registry, simply say this in your `Pod`'s
`spec.containers[].image` field:

```yaml
    image: localhost:5000/user/container
```

Before you can use the registry, you have to be able to get images into it,
though.  If you are building an image on your Kubernetes `Node`, you can spell
out `localhost:5000` when you build and push.  More likely, though, you are
building locally and want to push to your cluster.

You can use `kubectl` to set up a port-forward from your local node to a
running Pod:

```console
$ POD=$(kubectl get pods --namespace kube-system -l k8s-app=kube-registry-upstream \
            -o template --template '{{range .items}}{{.metadata.name}} {{.status.phase}}{{"\n"}}{{end}}' \
            | grep Running | head -1 | cut -f1 -d' ')

$ kubectl port-forward --namespace kube-system $POD 5000:5000 &
```

Now you can build and push images on your local computer as
`localhost:5000/yourname/container` and those images will be available inside
your kubernetes cluster with the same name.

# More Extensions

- [Use GCS as storage backend](gcs/README.md)
- [Enable TLS/SSL](tls/README.md)
- [Enable Authentication](auth/README.md)

## Future improvements

* Allow port-forwarding to a Service rather than a pod (#15180)


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/registry/README.md?pixel)]()
# Enable Authentication with Htpasswd for Kube-Registry 

Docker registry support a few authentication providers. Full list of supported provider can be found [here](https://docs.docker.com/registry/configuration/#auth). This document describes how to enable authentication with htpasswd for kube-registry. 

### Prepare Htpasswd Secret

Please generate your own htpasswd file. Assuming the file you generated is `htpasswd`. 
Creating secret to hold htpasswd...
```console
$ kubectl --namespace=kube-system create secret generic registry-auth-secret --from-file=htpasswd=htpasswd
```

### Run Registry

Please be noted that this sample rc is using emptyDir as storage backend for simplicity. 

<!-- BEGIN MUNGE: EXAMPLE registry-auth-rc.yaml -->
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: kube-registry-v0
  namespace: kube-system
  labels:
    k8s-app: kube-registry
    version: v0
#    kubernetes.io/cluster-service: "true"
spec:
  replicas: 1
  selector:
    k8s-app: kube-registry
    version: v0
  template:
    metadata:
      labels:
        k8s-app: kube-registry
        version: v0
#        kubernetes.io/cluster-service: "true"
    spec:
      containers:
      - name: registry
        image: registry:2
        resources:
          # keep request = limit to keep this container in guaranteed class
          limits:
            cpu: 100m
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
        env:
        - name: REGISTRY_HTTP_ADDR
          value: :5000
        - name: REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY
          value: /var/lib/registry
        - name: REGISTRY_AUTH_HTPASSWD_REALM
          value: basic_realm
        - name: REGISTRY_AUTH_HTPASSWD_PATH
          value: /auth/htpasswd
        volumeMounts:
        - name: image-store
          mountPath: /var/lib/registry
        - name: auth-dir
          mountPath: /auth
        ports:
        - containerPort: 5000
          name: registry
          protocol: TCP
      volumes:
      - name: image-store
        emptyDir: {}
      - name: auth-dir
        secret:
          secretName: registry-auth-secret
```
<!-- END MUNGE: EXAMPLE registry-auth-rc.yaml -->

No changes are needed for other components (kube-registry service and proxy). 

### To Verify

Setup proxy or port-forwarding to the kube-registry. Image push/pull should fail without authentication. Then use `docker login` to authenticate with kube-registry and see if it works.

### Configure Nodes to Authenticate with Kube-Registry

By default, nodes assume no authentication is required by kube-registry. Without authentication, nodes cannot pull images from kube-registry. To solve this, more documentation can be found [Here](https://github.com/kubernetes/kubernetes/blob/master/docs/user-guide/images.md#configuring-nodes-to-authenticate-to-a-private-repository)





[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/registry/auth/README.md?pixel)]()
# Enable TLS for Kube-Registry 

This document describes how to enable TLS for kube-registry. Before you start, please check if you have all the prerequisite:

- A domain for kube-registry. Assuming it is ` myregistrydomain.com`.
- Domain certificate and key. Assuming they are `domain.crt` and `domain.key`

### Pack domain.crt and domain.key into a Secret 

```console
$ kubectl --namespace=kube-system create secret generic registry-tls-secret --from-file=domain.crt=domain.crt --from-file=domain.key=domain.key
```

### Run Registry

Please be noted that this sample rc is using emptyDir as storage backend for simplicity. 

<!-- BEGIN MUNGE: EXAMPLE registry-tls-rc.yaml -->
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: kube-registry-v0
  namespace: kube-system
  labels:
    k8s-app: kube-registry
    version: v0
#    kubernetes.io/cluster-service: "true"
spec:
  replicas: 1
  selector:
    k8s-app: kube-registry
    version: v0
  template:
    metadata:
      labels:
        k8s-app: kube-registry
        version: v0
#        kubernetes.io/cluster-service: "true"
    spec:
      containers:
      - name: registry
        image: registry:2
        resources:
          # keep request = limit to keep this container in guaranteed class
          limits:
            cpu: 100m
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
        env:
        - name: REGISTRY_HTTP_ADDR
          value: :5000
        - name: REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY
          value: /var/lib/registry
        - name: REGISTRY_HTTP_TLS_CERTIFICATE
          value: /certs/domain.crt
        - name: REGISTRY_HTTP_TLS_KEY
          value: /certs/domain.key
        volumeMounts:
        - name: image-store
          mountPath: /var/lib/registry
        - name: cert-dir
          mountPath: /certs
        ports:
        - containerPort: 5000
          name: registry
          protocol: TCP
      volumes:
      - name: image-store
        emptyDir: {}
      - name: cert-dir
        secret:
          secretName: registry-tls-secret
```
<!-- END MUNGE: EXAMPLE registry-tls-rc.yaml -->

### Expose External IP for Kube-Registry

Modify the default kube-registry service to `LoadBalancer` type and point the DNS record of `myregistrydomain.com` to the service external ip. 

<!-- BEGIN MUNGE: EXAMPLE registry-tls-svc.yaml -->
```yaml
apiVersion: v1
kind: Service
metadata:
  name: kube-registry
  namespace: kube-system
  labels:
    k8s-app: kube-registry
#    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: "KubeRegistry"
spec:
  selector:
    k8s-app: kube-registry
  type: LoadBalancer
  ports:
  - name: registry
    port: 5000
    protocol: TCP
```
<!-- END MUNGE: EXAMPLE registry-tls-svc.yaml -->

### To Verify 

Now you should be able to access your kube-registry from another docker host. 
```console
docker pull busybox
docker tag busybox myregistrydomain.com:5000/busybox
docker push myregistrydomain.com:5000/busybox
docker pull myregistrydomain.com:5000/busybox
```


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/registry/tls/README.md?pixel)]()
# Kube-Registry with GCS storage backend

Besides local file system, docker registry also supports a number of cloud storage backends. Full list of supported backend can be found [here](https://docs.docker.com/registry/configuration/#storage). This document describes how to enable GCS for kube-registry as storage backend. 

A few preparation steps are needed. 
 1. Create a bucket named kube-registry in GCS.
 1. Create a service account for GCS access and create key file in json format. Detail instruction can be found [here](https://cloud.google.com/storage/docs/authentication#service_accounts).


### Pack Keyfile into a Secret

Assuming you have downloaded the keyfile as `keyfile.json`. Create secret with the `keyfile.json`...
```console
$ kubectl --namespace=kube-system create secret generic gcs-key-secret --from-file=keyfile=keyfile.json
```


### Run Registry

<!-- BEGIN MUNGE: EXAMPLE registry-gcs-rc.yaml -->
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: kube-registry-v0
  namespace: kube-system
  labels:
    k8s-app: kube-registry
    version: v0
#    kubernetes.io/cluster-service: "true"
spec:
  replicas: 1
  selector:
    k8s-app: kube-registry
    version: v0
  template:
    metadata:
      labels:
        k8s-app: kube-registry
        version: v0
#        kubernetes.io/cluster-service: "true"
    spec:
      containers:
      - name: registry
        image: registry:2
        resources:
          # keep request = limit to keep this container in guaranteed class
          limits:
            cpu: 100m
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
        env:
        - name: REGISTRY_HTTP_ADDR
          value: :5000
        - name: REGISTRY_STORAGE
          value: gcs
        - name: REGISTRY_STORAGE_GCS_BUCKET
          value: kube-registry
        - name: REGISTRY_STORAGE_GCS_KEYFILE
          value: /gcs/keyfile
        ports:
        - containerPort: 5000
          name: registry
          protocol: TCP
        volumeMounts:
        - name: gcs-key
          mountPath: /gcs
      volumes:
      - name: gcs-key
        secret:
          secretName: gcs-key-secret
```
<!-- END MUNGE: EXAMPLE registry-gcs-rc.yaml -->


No changes are needed for other components (kube-registry service and proxy). 


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/addons/registry/gcs/README.md?pixel)]()
# Kubernetes CoreOS cluster

With this tutorial one creates a Kubernetes CoreOS cluster containing of one
master and three minions (workers) running on `192.168.10.1`-`192.168.10.4`.

For working correctly you need to create the directory addressed as `POOL_PATH` in
`util.sh`:
```
$ sudo mkdir /var/lib/libvirt/images/kubernetes
$ sudo chown -R $USER:$USER /var/lib/libvirt/images/kubernetes/
```

Then we follow the instructions in the main `kubernetes` directory.

For debugging set `export UTIL_SH_DEBUG=1`.
```
$ export KUBERNETES_PROVIDER=libvirt-coreos
$ make release-skip-tests
$ ./cluster/kube-up.sh
```

To bring the cluster down again, execute:
```
$ ./cluster/kube-down.sh
```

Have fun!



[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/libvirt-coreos/README.md?pixel)]()
Please use [Kubernetes-anywhere](https://github.com/kubernetes/kubernetes-anywhere) to get started on vSphere.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/vsphere/README.md?pixel)]()
The scripts in this directory are not meant to be invoked
directly. Instead they are partial scripts that are combined into full
scripts by util.sh and are run on the Kubernetes nodes are part of the
setup. 
# SaltStack configuration

This is the root of the SaltStack configuration for Kubernetes. A high
level overview for the Kubernetes SaltStack configuration can be found [in the docs tree.](https://kubernetes.io/docs/admin/salt.md)

This SaltStack configuration currently applies to default
configurations for Debian-on-GCE, Fedora-on-Vagrant, Ubuntu-on-AWS and
Ubuntu-on-Azure. (That doesn't mean it can't be made to apply to an
arbitrary configuration, but those are only the in-tree OS/IaaS
combinations supported today.) As you peruse the configuration, these
are shorthanded as `gce`, `vagrant`, `aws`, `azure-legacy` in `grains.cloud`;
the documentation in this tree uses this same shorthand for convenience.

See more:
* [pillar](pillar/)
* [reactor](reactor/)
* [salt](salt/)


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/saltbase/README.md?pixel)]()
[SaltStack reactor](http://docs.saltstack.com/en/latest/topics/reactor/) files, largely defining reactions to new nodes.

**Ignored for GCE, which runs standalone on each machine**


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/saltbase/reactor/README.md?pixel)]()
The
[SaltStack pillar](http://docs.saltstack.com/en/latest/topics/pillar/)
data is partially statically derived from the contents of this
directory. The bulk of the pillars are hard to perceive from browsing
this directory, though, because they are written into
[cluster-params.sls](cluster-params.sls) at cluster inception.

* [cluster-params.sls](cluster-params.sls) is generated entirely at cluster inception. See e.g. [configure-vm.sh](../../gce/configure-vm.sh#L262)
* [docker-images.sls](docker-images.sls) stores the Docker tags of the current Docker-wrapped server binaries, twiddling by the Salt install script
* [logging.sls](logging.sls) defines the cluster log level
* [mine.sls](mine.sls): defines the variables shared across machines in the Salt
  mine. It is starting to be largely deprecated in use, and is totally
  unavailable on GCE, which runs standalone.
* [privilege.sls](privilege.sls) defines whether privileged containers are allowed.
* [top.sls](top.sls) defines which pillars are active across the cluster.

## Future work

Document the current pillars across providers


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/saltbase/pillar/README.md?pixel)]()
This directory forms the base of the main SaltStack configuration. The
place to start with any SaltStack configuration is
[top.sls](top.sls). However, unless you are particularly keen on
reading Jinja templates, the following tables break down what
configurations run on what providers. (NB: The [_states](_states/)
directory is a special directory included by Salt for `ensure` blocks,
and is only used for the [docker](docker/) config.)

Key: M = Config applies to master, n = config applies to nodes

Config                                              | GCE   | Vagrant | AWS | Azure
----------------------------------------------------|-------|---------|-----|------
[debian-auto-upgrades](debian-auto-upgrades/)       | M n   | M n     | M n | M n
[docker](docker/)                                   | M n   | M n     | M n | M n
[etcd](etcd/)                                       | M     | M       | M   | M
[generate-cert](generate-cert/)                     | M     | M       | M   | M
[kube-addons](kube-addons/)                         | M     | M       | M   | M
[kube-apiserver](kube-apiserver/)                   | M     | M       | M   | M
[kube-controller-manager](kube-controller-manager/) | M     | M       | M   | M
[kube-proxy](kube-proxy/)                           |   n   |   n     |   n |   n
[kube-scheduler](kube-scheduler/)                   | M     | M       | M   | M
[kubelet](kubelet/)                                 | M n   | M n     | M n | M n
[logrotate](logrotate/)                             | M n   |   n     | M n | M n
[supervisord](supervisor/)                          | M n   | M n     | M n | M n
[base](base.sls)                                    | M n   | M n     | M n | M n
[kube-client-tools](kube-client-tools.sls)          | M     | M       | M   | M


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/saltbase/salt/README.md?pixel)]()
# kubeapi-load-balancer

Simple NGINX reverse proxy to lend a hand in HA kubernetes-master deployments.


# Kubernetes end to end

End-to-end (e2e) tests for Kubernetes provide a mechanism to test end-to-end
behavior of the system, and is the last signal to ensure end user operations
match developer specifications. Although unit and integration tests provide a
good signal, in a distributed system like Kubernetes it is not uncommon that a
minor change may pass all unit and integration tests, but cause unforeseen
changes at the system level.

The primary objectives of the e2e tests are to ensure a consistent and reliable
behavior of the kubernetes code base, and to catch hard-to-test bugs before
users do, when unit and integration tests are insufficient.


## Usage

To deploy the end-to-end test suite, it is best to deploy the
[kubernetes-core bundle](https://github.com/juju-solutions/bundle-kubernetes-core)
and then relate the `kubernetes-e2e` charm.

```shell
juju deploy kubernetes-core
juju deploy cs:~containers/kubernetes-e2e
juju add-relation kubernetes-e2e kubernetes-master
juju add-relation kubernetes-e2e easyrsa
```


Once the relations have settled, and the `kubernetes-e2e` charm reports
 `Ready to test.` - you may kick off an end to end validation test.

### Running the e2e test

The e2e test is encapsulated as an action to ensure consistent runs of the
end to end test. The defaults are sensible for most deployments.

```shell
juju run-action kubernetes-e2e/0 test
```

### Tuning the e2e test

The e2e test is configurable. By default it will focus on or skip the declared
conformance tests in a cloud agnostic way. Default behaviors are configurable.
This allows the operator to test only a subset of the conformance tests, or to
test more behaviors not enabled by default. You can see all tunable options on
the charm by inspecting the schema output of the actions:

```shell
$ juju actions kubernetes-e2e --format=yaml --schema
test:
  description: Run end-to-end validation test suite
  properties:
    focus:
      default: \[Conformance\]
      description: Regex focus for executing the test
      type: string
    skip:
      default: \[Flaky\]
      description: Regex of tests to skip
      type: string
    timeout:
      default: 30000
      description: Timeout in nanoseconds
      type: integer
  title: test
  type: object
```


As an example, you can run a more limited set of tests for rapid validation of
a deployed cluster. The following example will skip the `Flaky`, `Slow`, and
`Feature` labeled tests:

```shell
juju run-action kubernetes-e2e/0 test skip='\[(Flaky|Slow|Feature:.*)\]'
```

> Note: the escaping of the regex due to how bash handles brackets.

To see the different types of tests the Kubernetes end-to-end charm has access
to, we encourage you to see the upstream documentation on the different types
of tests, and to strongly understand what subsets of the tests you are running.

[Kinds of tests](https://github.com/kubernetes/kubernetes/blob/master/docs/devel/e2e-tests.md#kinds-of-tests)

### More information on end-to-end testing

Along with the above descriptions, end-to-end testing is a much larger subject
than this readme can encapsulate. There is far more information in the
[end-to-end testing guide](https://github.com/kubernetes/kubernetes/blob/master/docs/devel/e2e-tests.md).

### Evaluating end-to-end results

It is not enough to just simply run the test. Result output is stored in two
places. The raw output of the e2e run is available in the `juju show-action-output`
command, as well as a flat file on disk on the `kubernetes-e2e` unit that
executed the test.

> Note: The results will only be available once the action has
completed the test run. End-to-end testing can be quite time intensive. Often
times taking **greater than 1 hour**, depending on configuration.

##### Flat file

```shell
$ juju run-action kubernetes-e2e/0 test
Action queued with id: 4ceed33a-d96d-465a-8f31-20d63442e51b

$ juju scp kubernetes-e2e/0:4ceed33a-d96d-465a-8f31-20d63442e51b.log .
```

##### Action result output

```shell
$ juju run-action kubernetes-e2e/0 test
Action queued with id: 4ceed33a-d96d-465a-8f31-20d63442e51b

$ juju show-action-output 4ceed33a-d96d-465a-8f31-20d63442e51b
```

## Known issues

The e2e test suite assumes egress network access. It will pull container
images from `gcr.io`. You will need to have this registry unblocked in your
firewall to successfully run e2e test results. Or you may use the exposed
proxy settings [properly configured](https://github.com/juju-solutions/bundle-canonical-kubernetes#proxy-configuration)
on the kubernetes-worker units.

## Contact information

Primary Authors: The ~containers team at Canonical

- [Matt Bruzek &lt;matthew.bruzek@canonical.com&gt;](mailto:matthew.bruzek@canonical.com)
- [Charles Butler &lt;charles.butler@canonical.com&gt;](mailto:charles.butler@canonical.com)

More resources for help:

- [Bug Tracker](https://github.com/juju-solutions/bundle-canonical-kubernetes/issues)
- [Github Repository](https://github.com/kubernetes/kubernetes/)
- [Mailing List](mailto:juju@lists.ubuntu.com)
# Kubernetes Worker

## Usage

This charm deploys a container runtime, and additionally stands up the Kubernetes
worker applications: kubelet, and kube-proxy.

In order for this charm to be useful, it should be deployed with its companion
charm [kubernetes-master](https://jujucharms.com/u/containers/kubernetes-master)
and linked with an SDN-Plugin.

This charm has also been bundled up for your convenience so you can skip the
above steps, and deploy it with a single command:

```shell
juju deploy canonical-kubernetes
```

For more information about [Canonical Kubernetes](https://jujucharms.com/canonical-kubernetes)
consult the bundle `README.md` file.


## Scale out

To add additional compute capacity to your Kubernetes workers, you may
`juju add-unit` scale the cluster of applications. They will automatically
join any related kubernetes-master, and enlist themselves as ready once the
deployment is complete.

## Operational actions

The kubernetes-worker charm supports the following Operational Actions:

#### Pause

Pausing the workload enables administrators to both [drain](http://kubernetes.io/docs/user-guide/kubectl/kubectl_drain/) and [cordon](http://kubernetes.io/docs/user-guide/kubectl/kubectl_cordon/)
a unit for maintenance.


#### Resume

Resuming the workload will [uncordon](http://kubernetes.io/docs/user-guide/kubectl/kubectl_uncordon/) a paused unit. Workloads will automatically migrate unless otherwise directed via their application declaration.

## Private registry

With the "registry" action that is part for the kubernetes-worker charm, you can very easily create a private docker registry, with authentication, and available over TLS. Please note that the registry deployed with the action is not HA, and uses storage tied to the kubernetes node where the pod is running. So if the registry pod changes is migrated from one node to another for whatever reason, you will need to re-publish the images.

### Example usage

Create the relevant authentication files. Let's say you want user `userA` to authenticate with the password `passwordA`. Then you'll do :

    echo "userA:passwordA" > htpasswd-plain
    htpasswd -c -b -B htpasswd userA passwordA

(the `htpasswd` program comes with the `apache2-utils` package)

Supposing your registry will be reachable at `myregistry.company.com`, and that you already have your TLS key in the `registry.key` file, and your TLS certificate (with `myregistry.company.com` as Common Name) in the `registry.crt` file, you would then run :

    juju run-action kubernetes-worker/0 registry domain=myregistry.company.com htpasswd="$(base64 -w0 htpasswd)" htpasswd-plain="$(base64 -w0 htpasswd-plain)" tlscert="$(base64 -w0 registry.crt)" tlskey="$(base64 -w0 registry.key)" ingress=true

If you then decide that you want do delete the registry, just run :

    juju run-action kubernetes-worker/0 registry delete=true ingress=true

## Known Limitations

Kubernetes workers currently only support 'phaux' HA scenarios. Even when configured with an HA cluster string, they will only ever contact the first unit in the cluster map. To enable a proper HA story, kubernetes-worker units are encouraged to proxy through a [kubeapi-load-balancer](https://jujucharms.com/kubeapi-load-balancer)
application. This enables a HA deployment without the need to
re-render configuration and disrupt the worker services.

External access to pods must be performed through a [Kubernetes
Ingress Resource](http://kubernetes.io/docs/user-guide/ingress/).

When using NodePort type networking, there is no automation in exposing the
ports selected by kubernetes or chosen by the user. They will need to be
opened manually and can be performed across an entire worker pool.

If your NodePort service port selected is `30510` you can open this across all
members of a worker pool named `kubernetes-worker` like so:

```
juju run --application kubernetes-worker open-port 30510/tcp
```

Don't forget to expose the kubernetes-worker application if its not already
exposed, as this can cause confusion once the port has been opened and the
service is not reachable.

Note: When debugging connection issues with NodePort services, its important
to first check the kube-proxy service on the worker units. If kube-proxy is not
running, the associated port-mapping will not be configured in the iptables
rulechains. 

If you need to close the NodePort once a workload has been terminated, you can
follow the same steps inversely.

```
juju run --application kubernetes-worker close-port 30510
```

# Kubernetes-master

[Kubernetes](http://kubernetes.io/) is an open source system for managing 
application containers across a cluster of hosts. The Kubernetes project was
started by Google in 2014, combining the experience of running production 
workloads combined with best practices from the community.

The Kubernetes project defines some new terms that may be unfamiliar to users
or operators. For more information please refer to the concept guide in the 
[getting started guide](https://kubernetes.io/docs/home/).

This charm is an encapsulation of the Kubernetes master processes and the 
operations to run on any cloud for the entire lifecycle of the cluster.

This charm is built from other charm layers using the Juju reactive framework.
The other layers focus on specific subset of operations making this layer 
specific to operations of Kubernetes master processes.

# Deployment

This charm is not fully functional when deployed by itself. It requires other
charms to model a complete Kubernetes cluster. A Kubernetes cluster needs a
distributed key value store such as [Etcd](https://coreos.com/etcd/) and the
kubernetes-worker charm which delivers the Kubernetes node services. A cluster
requires a Software Defined Network (SDN) and Transport Layer Security (TLS) so
the components in a cluster communicate securely. 

Please take a look at the [Canonical Distribution of Kubernetes](https://jujucharms.com/canonical-kubernetes/) 
or the [Kubernetes core](https://jujucharms.com/kubernetes-core/) bundles for 
examples of complete models of Kubernetes clusters.

# Resources

The kubernetes-master charm takes advantage of the [Juju Resources](https://jujucharms.com/docs/2.0/developer-resources) 
feature to deliver the Kubernetes software.

In deployments on public clouds the Charm Store provides the resource to the
charm automatically with no user intervention. Some environments with strict
firewall rules may not be able to contact the Charm Store. In these network
restricted  environments the resource can be uploaded to the model by the Juju
operator.

# Configuration

This charm supports some configuration options to set up a Kubernetes cluster 
that works in your environment:

#### dns_domain

The domain name to use for the Kubernetes cluster for DNS.

#### enable-dashboard-addons

Enables the installation of Kubernetes dashboard, Heapster, Grafana, and
InfluxDB.

# DNS for the cluster

The DNS add-on allows the pods to have a DNS names in addition to IP addresses.
The Kubernetes cluster DNS server (based off the SkyDNS library) supports 
forward lookups (A records), service lookups (SRV records) and reverse IP 
address lookups (PTR records). More information about the DNS can be obtained
from the [Kubernetes DNS admin guide](http://kubernetes.io/docs/admin/dns/).

# Actions

The kubernetes-master charm models a few one time operations called 
[Juju actions](https://jujucharms.com/docs/stable/actions) that can be run by
Juju users.

#### create-rbd-pv

This action creates RADOS Block Device (RBD) in Ceph and defines a Persistent
Volume in Kubernetes so the containers can use durable storage. This action
requires a relation to the ceph-mon charm before it can create the volume.

#### restart

This action restarts the master processes `kube-apiserver`, 
`kube-controller-manager`, and `kube-scheduler` when the user needs a restart.

# More information

 - [Kubernetes github project](https://github.com/kubernetes/kubernetes)
 - [Kubernetes issue tracker](https://github.com/kubernetes/kubernetes/issues)
 - [Kubernetes documentation](http://kubernetes.io/docs/)
 - [Kubernetes releases](https://github.com/kubernetes/kubernetes/releases)

# Contact

The kubernetes-master charm is free and open source operations created
by the containers team at Canonical. 

Canonical also offers enterprise support and customization services. Please
refer to the [Kubernetes product page](https://www.ubuntu.com/cloud/kubernetes)
for more details.
# kubernetes-bundle

The kubernetes-bundle allows you to deploy the many services of
Kubernetes to a cloud environment and get started using the Kubernetes
technology quickly.

## Kubernetes

Kubernetes is an open source system for managing containerized
applications.  Kubernetes uses [Docker](http://docker.com) to run
containerized applications.

## Juju TL;DR

The [Juju](https://jujucharms.com) system provides provisioning and
orchestration across a variety of clouds and bare metal. A juju bundle
describes collection of services and how they interrelate. `juju
quickstart` allows you to bootstrap a deployment environment and
deploy a bundle.

## Dive in!

#### Install Juju Quickstart

You will need to
[install the Juju client](https://jujucharms.com/get-started) and
`juju-quickstart` as prerequisites.  To deploy the bundle use
`juju-quickstart` which runs on Mac OS (`brew install
juju-quickstart`) or Ubuntu (`apt-get install juju-quickstart`).

### Deploy a Kubernetes Bundle

Use the 'juju quickstart' command to deploy a Kubernetes cluster to any cloud
supported by Juju.  

The charm store version of the Kubernetes bundle can be deployed as follows:

    juju quickstart u/kubernetes/kubernetes-cluster

> Note: The charm store bundle may be locked to a specific Kubernetes release.

Alternately you could deploy a Kubernetes bundle straight from github or a file:

    juju quickstart -i https://raw.githubusercontent.com/whitmo/bundle-kubernetes/master/bundles.yaml

The command above does few things for you:

- Starts a curses based gui for managing your cloud or MAAS credentials
- Looks for a bootstrapped deployment environment, and bootstraps if
  required. This will launch a bootstrap node in your chosen
  deployment environment (machine 0).
- Deploys the Juju GUI to your environment onto the bootstrap node.
- Provisions 4 machines, and deploys the Kubernetes services on top of
  them (Kubernetes-master, two Kubernetes minions using flannel, and etcd).
- Orchestrates the relations among the services, and exits.

Now you should have a running Kubernetes. Run `juju status
--format=oneline` to see the address of your kubernetes-master unit.

For further reading on [Juju Quickstart](https://pypi.python.org/pypi/juju-quickstart)

Go to the [Getting started with Juju guide](https://github.com/kubernetes/kubernetes/blob/master/docs/getting-started-guides/juju.md)
for more information about deploying a development Kubernetes cluster.

### Using the Kubernetes Client

You'll need the Kubernetes command line client,
[kubectl](https://github.com/kubernetes/kubernetes/blob/master/docs/user-guide/kubectl/kubectl.md)
to interact with the created cluster.  The kubectl command is
installed on the kubernetes-master charm. If you want to work with
the cluster from your computer you will need to install the binary
locally.

You can access kubectl by a number ways using juju.

via juju run:

    juju run --service kubernetes-master/0 "sudo kubectl get nodes"

via juju ssh:

    juju ssh kubernetes-master/0 -t "sudo kubectl get nodes"

You may also SSH to the kubernetes-master unit (`juju ssh kubernetes-master/0`)
and call kubectl from the command prompt.

See the
[kubectl documentation](https://github.com/kubernetes/kubernetes/blob/master/docs/user-guide/kubectl/kubectl.md)
for more details of what can be done with the command line tool.

### Scaling up the cluster

You can add capacity by adding more Docker units:

     juju add-unit docker

### Known Limitations

Kubernetes currently has several platform specific functionality. For
example load balancers and persistence volumes only work with the
Google Compute provider at this time.

The Juju integration uses the Kubernetes null provider. This means
external load balancers and storage can't be directly driven through
Kubernetes config files at this time. We look forward to adding these
capabilities to the charms.


## More about the components the bundle deploys

### Kubernetes master

The master controls the Kubernetes cluster.  It manages for the worker
nodes and provides the primary interface for control by the user.

### Kubernetes minion

The minions are the servers that perform the work.  Minions must
communicate with the master and run the workloads that are assigned to
them.

### Flannel-docker

Flannel provides individual subnets for each machine in the cluster by
creating a
[software defined networking](http://en.wikipedia.org/wiki/Software-defined_networking).

### Docker

An open platform for distributed applications for developers and sysadmins.

### Etcd

Etcd persists state for Flannel and Kubernetes. It is a distributed
key-value store with an http interface.


## For further information on getting started with Juju

Juju has complete documentation with regard to setup, and cloud
configuration on it's own
[documentation site](https://jujucharms.com/docs/).

- [Getting Started](https://jujucharms.com/docs/stable/getting-started)
- [Using Juju](https://jujucharms.com/docs/stable/charms)


## Installing the kubectl outside of kubernetes-master unit

Download the Kubernetes release from:
https://github.com/kubernetes/kubernetes/releases and extract
the release, you can then just directly use the cli binary at
./kubernetes/platforms/linux/amd64/kubectl

You'll need the address of the kubernetes-master as environment variable :

    juju status kubernetes-master/0

Grab the public-address there and export it as KUBERNETES_MASTER
environment variable :

    export KUBERNETES_MASTER=$(juju status --format=oneline kubernetes-master | grep kubernetes-master | cut -d' ' -f3):8080

And now you can run kubectl on the command line :

    kubectl get no

See the
[kubectl documentation](https://github.com/kubernetes/kubernetes/blob/master/docs/user-guide/kubectl/kubectl.md)
for more details of what can be done with the command line tool.


## Hacking on the kubernetes-bundle and associated charms

The kubernetes-bundle is open source and available on github.com.  If
you want to get started developing on the bundle you can clone it from
github.  

    git clone https://github.com/kubernetes/kubernetes.git

Go to the [Getting started with Juju guide](https://github.com/kubernetes/kubernetes/blob/master/docs/getting-started-guides/juju.md)
for more information about the bundle or charms.

## How to contribute

Send us pull requests!  We'll send you a cookie if they include tests and docs.


## Current and Most Complete Information

The charms and bundles are in the [kubernetes](https://github.com/kubernetes/kubernetes)
repository in github.

 - [kubernetes-master charm on GitHub](https://github.com/kubernetes/kubernetes/tree/master/cluster/juju/charms/trusty/kubernetes-master)
 - [kubernetes charm on GitHub](https://github.com/kubernetes/kubernetes/tree/master/cluster/juju/charms/trusty/kubernetes)


More information about the
[Kubernetes project](https://github.com/kubernetes/kubernetes)
or check out the
[Kubernetes Documentation](https://github.com/kubernetes/kubernetes/tree/master/docs)
for more details about the Kubernetes concepts and terminology.

Having a problem? Check the [Kubernetes issues database](https://github.com/kubernetes/kubernetes/issues)
for related issues.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/juju/bundles/README.md?pixel)]()
# Container Linux image

The [Container Linux Operating System](https://coreos.com/why/) is a Linux distribution optimized for running containers securely at scale.
CoreOS provides [a Container Linux image](https://coreos.com/os/docs/latest/booting-on-google-compute-engine.html) for Google Cloud Platform (GCP).

This folder contains configuration and tooling to allow kube-up to create a Kubernetes cluster on Google Cloud Platform running on the official Container Linux image.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/gce/container-linux/README.md?pixel)]()
# Container-VM Image

[Container-VM Image](https://cloud.google.com/compute/docs/containers/vm-image/)
is a container-optimized OS image for the Google Cloud Platform (GCP). It is
primarily for running Google services on GCP. Unlike the open preview version
of container-vm, the new Container-VM Image is based on the open source
ChromiumOS project, allowing us greater control over the build management,
security compliance, and customizations for GCP.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/gce/gci/README.md?pixel)]()
# Jenkins

[Jenkins](http://jenkins-ci.org/) is a pluggable continuous
integration system. The Google team is running two Jenkins servers in GCE for
the Kubernetes project. The post-commit instance runs continuous builds, unit
tests, integration tests, code verification tests, and end-to-end tests on
multiple providers using the latest commits to the Kubernetes repo from the
master and release branches. The PR Jenkins instance runs these tests on each
PR by a trusted contributor, it but only runs a subset of the end-to-end tests
and only on GCE.

## General flow
The flow of the post-commit Jenkins instance:
* Under the `kubernetes-build` job: Every 2 minutes, Jenkins polls for a batch
  of new commits, after which it runs the `build.sh` script (in this directory)
  on the latest tip. This results in build assets getting pushed to GCS and the
  `latest.txt` file in the `ci` bucket being updated.
* On trigger, and every half hour (which effectively means all the time, unless
  we're failing cluster creation), e2e variants run, on the latest build assets
  in GCS:
  * `kubernetes-e2e-gce`: Standard GCE e2e.
  * `kubernetes-e2e-gke`: GKE provider e2e, with head k8s client and GKE
    creating clusters at its default version.
  * `kubernetes-e2e-aws`: AWS provider e2e. This only runs once a day.
* Each job will not run concurrently with itself, so, for instance,
  Jenkins executor will only ever run one `kubernetes-build`
  job. However, it may run the jobs in parallel,
  i.e. `kubernetes-build` may be run at the same time as
  `kubernetes-e2e-gce`. For this reason, you may see your changes
  pushed to our GCS bucket rapidly, but they may take some time to
  fully work through Jenkins. Or you may get lucky and catch the
  train in 5 minutes.
* There are many jobs not listed here, including upgrade tests, soak tests, and
  tests for previous releases.

## Scripts

The scripts in this directory are directly used by Jenkins, either by
curl from githubusercontent (if we don't have a git checkout handy) or
by executing it from the git checkout. Since Jenkins is an entity
outside this repository, it's tricky to keep documentation for it up
to date quickly. However, the scripts themselves attempt to provide
color for the configuration(s) that each script runs in.

## GCS Log Format

Our `upload-to-gcs.sh` script runs at the start and end of every job. Logs on
post-commit Jenkins go under `gs://kubernetes-jenkins/logs/`. Logs on PR
Jenkins go under `gs://kubernetes-jenkins-pull/pr-logs/pull/PULL_NUMBER/`.
Individual run logs go into the `JOB_NAME/BUILD_NUMBER` folder.

At the start of the job, it uploads `started.json` containing the version of
Kubernetes under test and the timestamp.

At the end, it uploads `finished.json` containing the result and timestamp, as
well as the build log into `build-log.txt`. Under `artifacts/` we put our
test results in `junit_XY.xml`, along with gcp resource lists and cluster logs.

It also updates `latest-build.txt` at the end to point to this build number.
In the end, the directory structure looks like this:

```
gs://kubernetes-jenkins/logs/kubernetes-e2e-gce/
  latest-build.txt
  12345/
    build-log.txt
    started.json
    finished.json
    artifacts/
      gcp-resources-{before, after}.txt
      junit_{00, 01, ...}.xml
      jenkins-e2e-master/{kube-apiserver.log, ...}
      jenkins-e2e-node-abcd/{kubelet.log, ...}
  12344/
    ...
```

The munger uses `latest-build.txt` and the JUnit reports to figure out whether
or not the job is healthy.

## Job Builder

New jobs should be specified as YAML files to be processed by [Jenkins Job
Builder](http://docs.openstack.org/infra/jenkins-job-builder/). The YAML files
live in `jenkins/job-configs` and its subfolders **in the 
[kubernetes/test-infra repository](https://github.com/kubernetes/test-infra)**.
Jenkins runs Jenkins Job Builder in a Docker container defined in
`job-builder-image`, and triggers it using `update-jobs.sh`. Jenkins Job Builder
uses a config file called
[jenkins_jobs.ini](http://docs.openstack.org/infra/jenkins-job-builder/execution.html)
which contains the location and credentials of the Jenkins server.

E2E Job definitions are templated to avoid code duplication. To add a new job,
add a new entry to the appropriate `project`.
[This](https://github.com/kubernetes/kubernetes/commit/eb273e5a4bdd3905f881563ada4e6543c7eb96b5)
is an example of a commit which does this. If necessary, create a new project, as in
[this](https://github.com/kubernetes/kubernetes/commit/09c27cdabc300e0420a2914100bedb565c23ed73)
commit.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/hack/jenkins/README.md?pixel)]()
This folder contains the sources needed to build the gen-swagger-doc container.

To build the container image, 

```
$ sudo docker build -t gcr.io/google_containers/gen-swagger-docs:v1 .
```

To generate the html docs,

```
$ ./gen-swagger-docs.sh <API version> <absolute output path, default to PWD>
```

The generated definitions.html and operations.html will be stored in output paths.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/hack/gen-swagger-doc/README.md?pixel)]()
# Building Kubernetes

Building Kubernetes is easy if you take advantage of the containerized build environment. This document will help guide you through understanding this build process.

## Requirements

1. Docker, using one of the following configurations:
  1. **Mac OS X** You can either use Docker for Mac or docker-machine. See installation instructions [here](https://docs.docker.com/docker-for-mac/).
     **Note**: You will want to set the Docker VM to have at least 3GB of initial memory or building will likely fail. (See: [#11852]( http://issue.k8s.io/11852)).
  2. **Linux with local Docker**  Install Docker according to the [instructions](https://docs.docker.com/installation/#installation) for your OS.
  3. **Remote Docker engine** Use a big machine in the cloud to build faster. This is a little trickier so look at the section later on.
2. **Optional** [Google Cloud SDK](https://developers.google.com/cloud/sdk/)

You must install and configure Google Cloud SDK if you want to upload your release to Google Cloud Storage and may safely omit this otherwise.

## Overview

While it is possible to build Kubernetes using a local golang installation, we have a build process that runs in a Docker container.  This simplifies initial set up and provides for a very consistent build and test environment.

## Key scripts

The following scripts are found in the `build/` directory. Note that all scripts must be run from the Kubernetes root directory.

* `build/run.sh`: Run a command in a build docker container.  Common invocations:
  *  `build/run.sh make`: Build just linux binaries in the container.  Pass options and packages as necessary.
  *  `build/run.sh make cross`: Build all binaries for all platforms
  *  `build/run.sh make test`: Run all unit tests
  *  `build/run.sh make test-integration`: Run integration test
  *  `build/run.sh make test-cmd`: Run CLI tests
* `build/copy-output.sh`: This will copy the contents of `_output/dockerized/bin` from the Docker container to the local `_output/dockerized/bin`. It will also copy out specific file patterns that are generated as part of the build process. This is run automatically as part of `build/run.sh`.
* `build/make-clean.sh`: Clean out the contents of `_output`, remove any locally built container images and remove the data container.
* `/build/shell.sh`: Drop into a `bash` shell in a build container with a snapshot of the current repo code.

## Basic Flow

The scripts directly under `build/` are used to build and test.  They will ensure that the `kube-build` Docker image is built (based on `build/build-image/Dockerfile`) and then execute the appropriate command in that container.  These scripts will both ensure that the right data is cached from run to run for incremental builds and will copy the results back out of the container.

The `kube-build` container image is built by first creating a "context" directory in `_output/images/build-image`.  It is done there instead of at the root of the Kubernetes repo to minimize the amount of data we need to package up when building the image.

There are 3 different containers instances that are run from this image.  The first is a "data" container to store all data that needs to persist across to support incremental builds. Next there is an "rsync" container that is used to transfer data in and out to the data container.  Lastly there is a "build" container that is used for actually doing build actions.  The data container persists across runs while the rsync and build containers are deleted after each use.

`rsync` is used transparently behind the scenes to efficiently move data in and out of the container.  This will use an ephemeral port picked by Docker.  You can modify this by setting the `KUBE_RSYNC_PORT` env variable.

All Docker names are suffixed with a hash derived from the file path (to allow concurrent usage on things like CI machines) and a version number.  When the version number changes all state is cleared and clean build is started.  This allows the build infrastructure to be changed and signal to CI systems that old artifacts need to be deleted.

## Proxy Settings

If you are behind a proxy and you are letting these scripts use `docker-machine` to set up your local VM for you on macOS, you need to export proxy settings for Kubernetes build, the following environment variables should be defined.

```
export KUBERNETES_HTTP_PROXY=http://username:password@proxyaddr:proxyport
export KUBERNETES_HTTPS_PROXY=https://username:password@proxyaddr:proxyport
```

Optionally, you can specify addresses of no proxy for Kubernetes build, for example

```
export KUBERNETES_NO_PROXY=127.0.0.1
```

If you are using sudo to make Kubernetes build for example make quick-release, you need run `sudo -E make quick-release` to pass the environment variables.

## Really Remote Docker Engine

It is possible to use a Docker Engine that is running remotely (under your desk or in the cloud).  Docker must be configured to connect to that machine and the local rsync port must be forwarded (via SSH or nc) from localhost to the remote machine.

To do this easily with GCE and `docker-machine`, do something like this:
```
# Create the remote docker machine on GCE.  This is a pretty beefy machine with SSD disk.
KUBE_BUILD_VM=k8s-build
KUBE_BUILD_GCE_PROJECT=<project>
docker-machine create \
  --driver=google \
  --google-project=${KUBE_BUILD_GCE_PROJECT} \
  --google-zone=us-west1-a \
  --google-machine-type=n1-standard-8 \
  --google-disk-size=50 \
  --google-disk-type=pd-ssd \
  ${KUBE_BUILD_VM}

# Set up local docker to talk to that machine
eval $(docker-machine env ${KUBE_BUILD_VM})

# Pin down the port that rsync will be exposed on on the remote machine
export KUBE_RSYNC_PORT=8730

# forward local 8730 to that machine so that rsync works
docker-machine ssh ${KUBE_BUILD_VM} -L ${KUBE_RSYNC_PORT}:localhost:${KUBE_RSYNC_PORT} -N &
```

Look at `docker-machine stop`, `docker-machine start` and `docker-machine rm` to manage this VM.

## Releasing

The `build/release.sh` script will build a release.  It will build binaries, run tests, (optionally) build runtime Docker images.

The main output is a tar file: `kubernetes.tar.gz`.  This includes:
* Cross compiled client utilities.
* Script (`kubectl`) for picking and running the right client binary based on platform.
* Examples
* Cluster deployment scripts for various clouds
* Tar file containing all server binaries
* Tar file containing salt deployment tree shared across multiple cloud deployments.

In addition, there are some other tar files that are created:
* `kubernetes-client-*.tar.gz` Client binaries for a specific platform.
* `kubernetes-server-*.tar.gz` Server binaries for a specific platform.
* `kubernetes-salt.tar.gz` The salt script/tree shared across multiple deployment scripts.

When building final release tars, they are first staged into `_output/release-stage` before being tar'd up and put into `_output/release-tars`.

[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/build/README.md?pixel)]()
# Kubernetes Debian Base

The Kubernetes debian-base image provides a common base for Kubernetes system images that require
external dependencies (such as `iptables`, `sh`, or anything that is more than a static go-binary).

This image differs from the standard debian image by removing a lot of packages and files that are
generally not necessary in containers. The end result is an image that is just over 40 MB, down from
123 MB.

The image also provides a convenience script `/usr/local/bin/clean-install` that encapsulates the
process of updating apt repositories, installing the packages, and then cleaning up unnecessary
caches & logs.
### debian-iptables

Serves as the base image for `gcr.io/google_containers/kube-proxy-${ARCH}` and multiarch (not `amd64`) `gcr.io/google_containers/flannel-${ARCH}` images.

This image is compiled for multiple architectures.

#### How to release

If you're editing the Dockerfile or some other thing, please bump the `TAG` in the Makefile.

```console
# Build for linux/amd64 (default)
$ make push ARCH=amd64
# ---> gcr.io/google_containers/debian-iptables-amd64:TAG

$ make push ARCH=arm
# ---> gcr.io/google_containers/debian-iptables-arm:TAG

$ make push ARCH=arm64
# ---> gcr.io/google_containers/debian-iptables-arm64:TAG

$ make push ARCH=ppc64le
# ---> gcr.io/google_containers/debian-iptables-ppc64le:TAG

$ make push ARCH=s390x
# ---> gcr.io/google_containers/debian-iptables-s390x:TAG
```

If you don't want to push the images, run `make` or `make build` instead


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/build/debian-iptables/README.md?pixel)]()
# Package Groups Used in Kubernetes Visibility Rules

## Background

`BUILD` rules define dependencies, answering the question:
on what packages does _foo_ depend?

The `BUILD` file in this package allows one to define
_allowed_ reverse dependencies, answering the question:
given a package _foo_, what other specific packages are
allowed to depend on it?

This is done via visibility rules.

Visibility rules discourage unintended, spurious
dependencies that blur code boundaries, slow CICD queues and
generally inhibit progress.

#### Facts

* A package is any directory that contains a `BUILD` file.

* A `package_group` is a `BUILD` file rule that defines a named
  set of packages for use in other rules, e.g., given
  ```
  package_group(
    name = "database_CONSUMERS",
    packages = [
        "//foo/dbinitializer",
        "//foo/backend/...",  # `backend` and everything below it
    ],
  )
  ```
  one can specify the following visibility rule in any `BUILD` rule:
  ```
  visibility = [ "//build/visible_to:database_CONSUMERS" ],
  ``` 

* A visibility rule takes a list of package groups as its
  argument - or one of the pre-defined groups
  `//visibility:private` or `//visibility:public`.

* If no visibility is explicitly defined, a package is
  _private_ by default.

* Violations in visibility cause `make bazel-build` to fail,
  which in turn causes the submit queue to fail - that's the
  enforcement.

#### Why define all package groups meant for visibility here (in one file)?

 * Ease discovery of appropriate groups for use in a rule.
 * Ease reuse (inclusions) of commonly used groups.
 * Consistent style:
    * easy to read `//build/visible_to:math_library_CONSUMERS` rules,
    * call out bad dependencies for eventual removal.
 * Make it more obvious in code reviews when visibility is being
   modified.
 * One set of `OWNERS` to manage visibility.

The alternative is to use special [package literals] directly
in visibility rules, e.g. 

```
  visibility = [
        "//foo/dbinitializer:__pkg__",
        "//foo/backend:__subpackages__",
  ],
```

The difference in style is similar to the difference between
using a named static constant like `MAX_NODES` rather than a
literal like `12`.  Names are preferable to literals for intent
documentation, search, changing one place rather than _n_,
associating usage in distant code blocks, etc.


## Rule Examples

#### Nobody outside this package can depend on me.

```
visibility = ["//visibility:private"],
```

Since this is the default, there's no reason to use this
rule except as a means to override, for some specific
target, some broader, whole-package visibility rule.

#### Anyone can depend on me (eschew this).

```
visibility = ["//visibility:public"],
```

#### Only some servers can depend on me.

Appropriate for, say, backend storage utilities.

```
visibility = ["//visible_to:server_foo","//visible_to:server_bar"].
```

#### Both some client and some server can see me.

Appropriate for shared API definition files and generated code:

```
visibility = ["//visible_to:client_foo,//visible_to:server_foo"],
```

## Handy commands

#### Quickly check for visibility violations
```
bazel build --check_visibility --nobuild \
    //cmd/... //pkg/... //federation/... //plugin/... \
    //third_party/... //examples/... //test/... //vendor/k8s.io/...
```

#### Who depends on target _q_?

To create a seed set for a visibility group, one can ask what
packages currently depend on (must currently be able to see) a
given Go library target?  It's a time consuming query.

```
q=//pkg/kubectl/cmd:go_default_library
bazel query "rdeps(...,${q})" | \
    grep go_default_library | \
    sed 's/\(.*\):go_default_library/ "\1",/'
```

#### What targets below _p_ are visible to anyone?

A means to look for things one missed when locking down _p_.

```
p=//pkg/kubectl/cmd
bazel query "visible(...,${p}/...)"
```

#### What packages below _p_ may target _q_ depend on without violating visibility rules?

A means to pinpoint unexpected visibility.

```
p=//pkg/kubectl
q=//cmd/kubelet:kubelet
bazel query "visible(${q},${p}/...)" | more
```

#### What packages does target _q_ need?

```
q=//cmd/kubectl:kubectl
bazel query "buildfiles(deps($q))" | \
    grep -v @bazel_tools | \
    grep -v @io_bazel_rules | \
    grep -v @io_kubernetes_build | \
    grep -v @local_config | \
    grep -v @local_jdk | \
    grep -v //visible_to: | \
    sed 's/:BUILD//' | \
    sort | uniq > ~/KUBECTL_BUILD.txt
```

or try

```
bazel query --nohost_deps --noimplicit_deps \
    "kind('source file', deps($q))" | wc -
```


#### How does kubectl depend on pkg/util/parsers?

```
bazel query "somepath(cmd/kubectl:kubectl, pkg/util/parsers:go_default_library)"
```

 

[package literals]: https://bazel.build/versions/master/docs/be/common-definitions.html#common.visibility
This repository holds supplementary Go libraries for text processing, many involving Unicode.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
This repository holds supplemental Go packages for low-level interactions with the operating system.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
This repository holds supplementary Go cryptography libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
This repository holds supplementary Go networking libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
The *.dat files in this directory are copied from The WebKit Open Source
Project, specifically $WEBKITROOT/LayoutTests/html5lib/resources.
WebKit is licensed under a BSD style license.
http://webkit.org/coding/bsd-license.html says:

Copyright (C) 2009 Apple Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY APPLE INC. AND ITS CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL APPLE INC. OR ITS CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

These test cases come from
http://www.w3.org/International/tests/repository/html5/the-input-byte-stream/results-basics

Distributed under both the W3C Test Suite License
(http://www.w3.org/Consortium/Legal/2008/04-testsuite-license)
and the W3C 3-clause BSD License
(http://www.w3.org/Consortium/Legal/2008/03-bsd-license).
To contribute to a W3C Test Suite, see the policies and contribution
forms (http://www.w3.org/2004/10/27-testcases).
This is a work-in-progress HTTP/2 implementation for Go.

It will eventually live in the Go standard library and won't require
any changes to your code to use.  It will just be automatic.

Status:

* The server support is pretty good. A few things are missing
  but are being worked on.
* The client work has just started but shares a lot of code
  is coming along much quicker.

Docs are at https://godoc.org/golang.org/x/net/http2

Demo test server at https://http2.golang.org/

Help & bug reports welcome!

Contributing: https://golang.org/doc/contribute.html
Bugs:         https://golang.org/issue/new?title=x/net/http2:+
# h2i

**h2i** is an interactive HTTP/2 ("h2") console debugger. Miss the good ol'
days of telnetting to your HTTP/1.n servers? We're bringing you
back.

Features:
- send raw HTTP/2 frames
 - PING
 - SETTINGS
 - HEADERS
 - etc
- type in HTTP/1.n and have it auto-HPACK/frame-ify it for HTTP/2
- pretty print all received HTTP/2 frames from the peer (including HPACK decoding)
- tab completion of commands, options

Not yet features, but soon:
- unnecessary CONTINUATION frames on short boundaries, to test peer implementations 
- request bodies (DATA frames)
- send invalid frames for testing server implementations (supported by underlying Framer)

Later:
- act like a server

## Installation

```
$ go get golang.org/x/net/http2/h2i
$ h2i <host>
```

## Demo

```
$ h2i
Usage: h2i <hostname>
  
  -insecure
        Whether to skip TLS cert validation
  -nextproto string
        Comma-separated list of NPN/ALPN protocol names to negotiate. (default "h2,h2-14")

$ h2i google.com
Connecting to google.com:443 ...
Connected to 74.125.224.41:443
Negotiated protocol "h2-14"
[FrameHeader SETTINGS len=18]
  [MAX_CONCURRENT_STREAMS = 100]
  [INITIAL_WINDOW_SIZE = 1048576]
  [MAX_FRAME_SIZE = 16384]
[FrameHeader WINDOW_UPDATE len=4]
  Window-Increment = 983041
  
h2i> PING h2iSayHI
[FrameHeader PING flags=ACK len=8]
  Data = "h2iSayHI"
h2i> headers
(as HTTP/1.1)> GET / HTTP/1.1
(as HTTP/1.1)> Host: ip.appspot.com
(as HTTP/1.1)> User-Agent: h2i/brad-n-blake
(as HTTP/1.1)>  
Opening Stream-ID 1:
 :authority = ip.appspot.com
 :method = GET
 :path = /
 :scheme = https
 user-agent = h2i/brad-n-blake
[FrameHeader HEADERS flags=END_HEADERS stream=1 len=77]
  :status = "200"
  alternate-protocol = "443:quic,p=1"
  content-length = "15"
  content-type = "text/html"
  date = "Fri, 01 May 2015 23:06:56 GMT"
  server = "Google Frontend"
[FrameHeader DATA flags=END_STREAM stream=1 len=15]
  "173.164.155.78\n"
[FrameHeader PING len=8]
  Data = "\x00\x00\x00\x00\x00\x00\x00\x00"
h2i> ping  
[FrameHeader PING flags=ACK len=8]  
  Data = "h2i_ping"  
h2i> ping  
[FrameHeader PING flags=ACK len=8]
  Data = "h2i_ping"
h2i> ping
[FrameHeader GOAWAY len=22]
  Last-Stream-ID = 1; Error-Code = PROTOCOL_ERROR (1)

ReadFrame: EOF
```

## Status

Quick few hour hack. So much yet to do. Feel free to file issues for
bugs or wishlist items, but [@bmizerany](https://github.com/bmizerany/)
and I aren't yet accepting pull requests until things settle down.


Client:
 -- Firefox nightly with about:config network.http.spdy.enabled.http2draft set true
 -- Chrome: go to chrome://flags/#enable-spdy4, save and restart (button at bottom)

Make CA:
$ openssl genrsa -out rootCA.key 2048
$ openssl req -x509 -new -nodes -key rootCA.key -days 1024 -out rootCA.pem
... install that to Firefox

Make cert:
$ openssl genrsa -out server.key 2048
$ openssl req -new -key server.key -out server.csr
$ openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.crt -days 500


This is a fork of the encoding/xml package at ca1d6c4, the last commit before
https://go.googlesource.com/go/+/c0d6d33 "encoding/xml: restore Go 1.4 name
space behavior" made late in the lead-up to the Go 1.5 release.

The list of encoding/xml changes is at
https://go.googlesource.com/go/+log/master/src/encoding/xml

This fork is temporary, and I (nigeltao) expect to revert it after Go 1.6 is
released.

See http://golang.org/issue/11841
# YAML support for the Go language

Introduction
------------

The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within [Canonical](https://www.canonical.com) as
part of the [juju](https://juju.ubuntu.com) project, and is based on a
pure Go port of the well-known [libyaml](http://pyyaml.org/wiki/LibYAML)
C library to parse and generate YAML data quickly and reliably.

Compatibility
-------------

The yaml package supports most of YAML 1.1 and 1.2, including support for
anchors, tags, map merging, etc. Multi-document unmarshalling is not yet
implemented, and base-60 floats from YAML 1.1 are purposefully not
supported since they're a poor design and are gone in YAML 1.2.

Installation and usage
----------------------

The import path for the package is *gopkg.in/yaml.v2*.

To install it, run:

    go get gopkg.in/yaml.v2

API documentation
-----------------

If opened in a browser, the import path itself leads to the API documentation:

  * [https://gopkg.in/yaml.v2](https://gopkg.in/yaml.v2)

API stability
-------------

The package API for yaml v2 will remain stable as described in [gopkg.in](https://gopkg.in).


License
-------

The yaml package is licensed under the LGPL with an exception that allows it to be linked statically. Please see the LICENSE file for details.


Example
-------

```Go
package main

import (
        "fmt"
        "log"

        "gopkg.in/yaml.v2"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

type T struct {
        A string
        B struct {
                RenamedC int   `yaml:"c"`
                D        []int `yaml:",flow"`
        }
}

func main() {
        t := T{}
    
        err := yaml.Unmarshal([]byte(data), &t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t:\n%v\n\n", t)
    
        d, err := yaml.Marshal(&t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t dump:\n%s\n\n", string(d))
    
        m := make(map[interface{}]interface{})
    
        err = yaml.Unmarshal([]byte(data), &m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)
    
        d, err = yaml.Marshal(&m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m dump:\n%s\n\n", string(d))
}
```

This example will generate the following output:

```
--- t:
{Easy! {2 [3 4]}}

--- t dump:
a: Easy!
b:
  c: 2
  d: [3, 4]


--- m:
map[a:Easy! b:map[c:2 d:[3 4]]]

--- m dump:
a: Easy!
b:
  c: 2
  d:
  - 3
  - 4
```

# External Storage
[![Build Status](https://travis-ci.org/kubernetes-incubator/external-storage.svg?branch=master)](https://travis-ci.org/kubernetes-incubator/external-storage)
[![GoDoc](https://godoc.org/github.com/kubernetes-incubator/external-storage?status.svg)](https://godoc.org/github.com/kubernetes-incubator/external-storage)
[![Go Report Card](https://goreportcard.com/badge/github.com/kubernetes-incubator/external-storage)](https://goreportcard.com/report/github.com/kubernetes-incubator/external-storage)

## External Provisioners
This repository houses community-maintained external provisioners plus a helper library for building them. Each provisioner is contained in its own directory so for information on how to use one, enter its directory and read its documentation. The library is contained in the `lib` directory.

### What is an 'external provisioner'?
An external provisioner is a dynamic PV provisioner whose code lives out-of-tree/external to Kubernetes. Unlike [in-tree dynamic provisioners](https://kubernetes.io/docs/user-guide/persistent-volumes/#aws) that run as part of the Kubernetes controller manager, external ones can be deployed & updated independently.

External provisioners work just like in-tree dynamic PV provisioners. A `StorageClass` object can specify an external provisioner instance to be its `provisioner` like it can in-tree provisioners. The instance will then watch for `PersistentVolumeClaims` that ask for the `StorageClass` and automatically create `PersistentVolumes` for them. For more information on how dynamic provisioning works, see [the docs](http://kubernetes.io/docs/user-guide/persistent-volumes/) or [this blog post](http://blog.kubernetes.io/2016/10/dynamic-provisioning-and-storage-in-kubernetes.html).

### How to use the library
```go
import (
  "github.com/kubernetes-incubator/external-storage/lib/controller"
)
```
You need to implement the `Provisioner` interface then pass your implementation to a `ProvisionController` and run the controller. The controller takes care of deciding when to call your implementation's `Provision` or `Delete`. The interface and controller are defined in the above package.

You will want to import a specific version of the library to ensure compatibility with certain versions of Kubernetes and to avoid breaking changes. This repo will be tagged according to the library's version (individual provisioners will need to version themselves independently, e.g. by in their documentation pointing to Docker Hub and using Docker tags), so to keep track of releases, go to this repo's [releases page](https://github.com/kubernetes-incubator/external-storage/releases).

Note that because your provisioner needs to depend also on [client-go](https://github.com/kubernetes/client-go) and the library itself depends on a specific version of client-go, to avoid a dependency conflict you must ensure you use the exact same version of client-go as the library. You can check what version of client-go the library depends on by looking at its [glide.yaml](lib/glide.yaml).

[For all documentation, including a full guide on how to write an external provisioner using the library that demonstrates the above, see here](./docs).

### `client-go` integration strategy
This library is integrated with `client-go` `master` branch. As soon as the `client-go` `master` branch contains a new version of `client-go` vendor dependencies, dependencies of this library shall be updated to the tip of the `client-go` `master` branch.

## Roadmap

February
* Finalize repo structure, release process, etc.

## Community, discussion, contribution, and support

Learn how to engage with the Kubernetes community on the [community page](http://kubernetes.io/community/).

You can reach the maintainers of this project at:

- Slack: #sig-storage

## Kubernetes Incubator

This is a [Kubernetes Incubator project](https://github.com/kubernetes/community/blob/master/incubator.md). The project was established 2016-11-15 (as nfs-provisioner). The incubator team for the project is:

- Sponsor: Clayton (@smarterclayton)
- Champion: Jan (@jsafrane) & Brad (@childsb)
- SIG: sig-storage

### Code of conduct

Participation in the Kubernetes community is governed by the [Kubernetes Code of Conduct](code-of-conduct.md).
# Kubernetes repository infrastructure

This repository contains repository infrastructure tools for use in
`kubernetes` and `kubernetes-incubator` repositories.  Examples:

- Boilerplate verification
- Go source code quality verification
- Golang build infrastructure

---

## Using this repository

This repository can be used via some golang "vendoring" mechanism 
(such as glide), or it can be used via
[git subtree](http://git.kernel.org/cgit/git/git.git/plain/contrib/subtree/git-subtree.txt).

### Using "vendoring"

The exact mechanism to pull in this repository will vary depending on
the tool you use. However, unless you end up having this repository
at the root of your project's repository you wll probably need to 
make sure you use the `--rootdir` command line parameter to let the
`verify-boilerplate.sh` know its location, eg:

    verify-boilerplate.sh --rootdir=/home/myrepo

### Using `git subtree`

When using the git subtree mechanism, this repository should be placed in the 
top level of your project.

To add `repo-infra` to your repository, use the following commands from the 
root directory of **your** repository.

First, add a git remote for the `repo-infra` repository:

```
$ git remote add repo-infra git://github.com/kubernetes/repo-infra
```

This is not strictly necessary, but reduces the typing required for subsequent
commands.

Next, use `git subtree add` to create a new subtree in the `repo-infra`
directory within your project:

```
$ git subtree add -P repo-infra repo-infra master --squash
```

After this command, you will have:

1.  A `repo-infra` directory in your project containing the content of **this**
    project
2.  2 new commits in the active branch:
  1.  A commit that squashes the git history of the `repo-infra` project
  2.  A merge commit whose ancestors are:
    1.  The `HEAD` of the branch prior to when you ran `git subtree add`
    2.  The commit containing the squashed `repo-infra` commits

kazel - a BUILD file generator for go and bazel
===============================================

Requirements:
#############

* Your project must be somewhat compatible with go tool because
  kazel uses go tool to parse your import tree.
* You must have a **GOPATH** and **GOROOT** setup and your project must
  be in the correct location in your **GOPATH**.
* Your ``./vendor`` directory may not contain ``BUILD`` files.

Usage:
######

1. Get kazel by running ``go get k8s.io/repo-infra/kazel``.

2. Create a ``.kazelcfg.json`` in the root of the repository. For the
   kazel repository, the ``.kazelcfg.json`` would look like:

  .. code-block:: json

   {
     "GoPrefix": "k8s.io/repo-infra",
     "SrcDirs": [
       "./kazel"
     ],
     "SkippedPaths": [
       ".*foobar(baz)?.*$"
     ]
   }

3. Run kazel:

  .. code-block:: bash

    $ kazel -root=$GOPATH/src/k8s.io/repo-infra

Defaults:
#########

* **SrcDirs** in ``.kazelcfg.json`` defaults to ``["./"]``
* ``-root`` option defaults to the current working directory

Automanagement:
###############

kazel reconciles rules that have the "**automanaged**" tag. If
you no longer want kazel to manage a rule, you can remove the
**automanaged** tag and kazel will no longer manage that rule.

kazel only manages srcs, deps, and library attributes of a
rule after initial creation so you can add and managed other
attributes like data and copts and kazel will respect your
changes.

kazel automatically formats all ``BUILD`` files in your repository
except for those matching **SkippedPaths**.

Adding "sources" rules:
#######################

If you set "**AddSourcesRules**": ``true`` in your ``.kazelcfg.json``,
kazel will create "**package-srcs**" and "**all-srcs**" rules in every
package.

The "**package-srcs**" rule is a glob matching all files in the
package recursively, but not any files owned by packages in
subdirectories.

The "**all-srcs**" rule includes both the "**package-srcs**" rule and
the "**all-srcs**" rules of all subpackages; i.e. **//:all-srcs** will
include all files in your repository.

The "**package-srcs**" rule defaults to private visibility,
since it is safer to depend on the "**all-srcs**" rule: if a
subpackage is added, the "**package-srcs**" rule will no longer
include those files.

You can remove the "**automanaged**" tag from the "**package-srcs**"
rule if you need to modify the glob (such as adding excludes).
It's recommended that you leave the "**all-srcs**" rule
automanaged.

Validating BUILD files in CI:
#############################

If you run kazel with ``--validate``, it will not update any ``BUILD`` files, but it
will exit nonzero if any ``BUILD`` files are out-of-date. You can add ``--print-diff``
to print out the changes needed.
# Verification scripts

Collection of scripts that verifies that a project meets requirements set for kubernetes related projects. The scripts are to be invoked depending on the needs via CI tooling, such as Travis CI. See main Readme file on how to integrate the repo-infra in your project. 

The scripts are currently being migrated from the main kubernetes repository. If your project requires additional set of verifications, consider creating an issue/PR on repo-infra to avoid code duplication across multiple projects. 

If repo-infra is integrated at the root of your project as git submodule at path: `/repo-infra`,
then scripts can be invoked as `repo-infra/verify/verify-*.sh`

travis.yaml example: 

```
dist: trusty

os:
- linux

language: go

go:
- 1.8

before_install:
- go get -u github.com/alecthomas/gometalinter

install:
- gometalinter --install

script:
- repo-infra/verify/verify-go-src.sh -v
- repo-infra/verify/verify-boilerplate.sh
# OR with vendoring 
# - vendor/github.com/kubernetes/repo-infra/verify-go-src.sh --rootdir=$(pwd) -v
```

## Verify boilerplate

Verifies that the boilerplate for various formats (go files, Makefile, etc.) is included in each file: `verify-boilerplate.sh`. 

## Verify go source code 

Runs a set of scripts on the go source code excluding vendored files: `verify-go-src.sh`. Expects `gometalinter` tooling installed (see travis file above)

With git submodule from your repo root: `repo-infra/verify/verify-go-src.sh -v`

With vendoring: `vendor/repo-infra/verify/verify-go-src.sh -v --rootdir $(pwd)`

Checks include:

1. gofmt
2. gometalinter
3. govet
# Local Persistent Storage User Guide

## Overview

Local persistent volumes allows users to access local storage through the
standard PVC interface in a simple and portable way.  The PV contains node
affinity information that the system uses to schedule pods to the correct
nodes.

An external static provisioner and a related bootstrapper are available to help
simplify local storage management once the local volumes are configured.

## Feature Status

Current status: 1.7 - Alpha

What works:
* Create a PV specifying a directory with node affinity.
* Pod using the PVC that is bound to this PV will always get scheduled to that node.
* External static provisioner daemonset that discovers local directories,
  creates, cleans up and deletes PVs.

What doesn't work and workarounds:
* Multiple local PVCs in a single pod.
    * Goal for 1.8.
    * No known workarounds.
* PVC binding does not consider pod scheduling requirements and may make
  suboptimal or incorrect decisions.
    * Goal for 1.8.
    * Workarounds:
        * Run your pods that require local storage first.
        * Give your pods high priority.
        * Run a workaround controller that unbinds PVCs for pods that are
          stuck pending. TODO: add link
* External provisioner cannot correctly detect capacity of mounts added after it
  has been started.
    * This requires mount propagation to work, which is targeted for 1.8.
    * Workaround: Before adding any new mount points, stop the daemonset, add
      the new mount points, start the daemonset.
* Fsgroup conflict if multiple pods using the same PVC specify different fsgroup
    * Workaround: Don't do this!

Future features:
* Local block devices as a volume source, with partitioning and fs formatting
* Pod accessing local raw block device
* Local PV health monitoring, taints and tolerations
* Inline PV (use dedicated local disk as ephemeral storage)
* Dynamic provisioning for shared local persistent storage

## User Guide

### Step 1: Bringing up a cluster with local disks

#### Option 1: GCE

``` console
KUBE_FEATURE_GATES="PersistentLocalVolumes=true" NODE_LOCAL_SSDS=<n> cluster/kube-up.sh
```

#### Option 2: GKE

``` console
gcloud container cluster create ... --local-ssd-count=<n> --enable-kubernetes-alpha --cluster-version=1.7.1
gcloud container node-pools create ... --local-ssd-count=<n>
```

#### Option 3: Baremetal environments

1. Partition and format the disks on each node according to your application's
   requirements.
2. Mount all the filesystems under one directory per StorageClass. The directories
   are specified in a configmap, see below. By default, the discovery directory is
   `/mnt/disks` and storage class is `local-storage`.
3. Configure the Kubernetes API Server, controller-manager, scheduler, and all kubelets with the `PersistentLocalVolumes` feature gate.

#### Option 4: Local test cluster

1. Create `/mnt/disks` directory and mount several volumes into its subdirectories.
   The example below uses three ram disks to simulate real local volumes:
```console
$ mkdir /mnt/disks
$ for vol in vol1 vol2 vol3; do
    mkdir /mnt/disks/$vol
    mount -t tmpfs $vol /mnt/disks/$vol
done
```

2. Run the local cluster.
```console
$ ALLOW_PRIVILEGED=true LOG_LEVEL=5 FEATURE_GATES=PersistentLocalVolumes=true hack/local-up-cluster.sh
```

3. Continue with [Creating local persistent volumes](#creating-local-persistent-volumes)
   below.

### Step 2: Creating local persistent volumes

#### Option 1: Bootstrapping the external static provisioner

This is optional, only for automated creation and cleanup of local volumes. See
[bootstrapper/](./bootstrapper) and [provisioner/](./provisioner) for details and
sample configuration files.

1. Create an admin account with cluster admin priviledge:
``` console
$ kubectl create -f bootstrapper/deployment/kubernetes/admin-account.yaml
```

2. Create a ConfigMap with your local storage configuration details:
```console
$ kubectl create -f bootstrapper/deployment/kubernetes/example-config.yaml
```

3. Launch the bootstrapper, which in turn creates static provisioner daemonset:
``` console
$ kubectl create -f bootstrapper/deployment/kubernetes/bootstrapper.yaml
```

#### Option 2: Manually create local persistent volume

If you don't use the external provisioner, then you have to create the local PVs
manually. Note that with manual PV creation, the volume has to be manually
reclaimed when deleted. Example PV:

``` yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: example-local-pv
  annotations:
    "volume.alpha.kubernetes.io/node-affinity": '{
      "requiredDuringSchedulingIgnoredDuringExecution": {
        "nodeSelectorTerms": [
          { "matchExpressions": [
            { "key": "kubernetes.io/hostname",
              "operator": "In",
              "values": ["my-node"]
            }
          ]}
         ]}
        }'
spec:
  capacity:
    storage: 5Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  local:
    path: /mnt/disks/ssd1
```
Please replace the following elements to reflect your configuration:
  * "my-node" with the name of kubernetes node which is hosting this
    local storage disk
  * "5Gi" with the required size of storage volume, same as specified in PVC
  * "local-storage" with the name of storage class which should be used
     for local volumes
  * "/mnt/disks/ssd1" with the path to the mount point of local volumes
 
### Step 3: Create local persistent volume claim

``` yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: example-local-claim
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: local-storage
```
Please replace the following elements to reflect your configuration:
  * "5Gi" with required size of storage volume
  * "local-storage" with the name of storage class which should be used
     for local PVs

## E2E Tests

### Running
``` console
go run hack/e2e.go -- -v --test --test_args="--ginkgo.focus=\[Feature:LocalPersistentVolumes\]"
```

### View CI Results
[GCE Alpha](https://k8s-testgrid.appspot.com/sig-storage#gce-alpha)
[GCE GCI Alpha](https://k8s-testgrid.appspot.com/sig-storage#gci-gce-alpha)

## Best Practices

* For IO isolation, a whole disk per volume is recommended
* For capacity isolation, separate partitions per volume is recommended
* Avoid recreating nodes with the same node name while there are still old PVs
  with that node's affinity specified. Otherwise, the system could think that
  the new node contains the old PVs.

### Deleting/removing the underlying volume

When you want to decommission the local volume, here is a possible workflow.
1. Stop the pods that are using the volume
2. Remove the local volume from the node (ie unmounting, pulling out the disk, etc)
3. Delete the PVC
4. The provisioner will try to cleanup the volume, but will fail since the volume no longer exists
5. Manually delete the PV object
# local-volume-provisioner

`quay.io/external-storage/local-volume-provisioner:1.0.0`

local-volume-provisioner is an out-of-tree static provisioner for the local volume
plugin, which is a 1.7 alpha feature.

It runs on each node in the cluster and monitors specified directories to look for
new local file-based volumes.  The volumes can be a mount point or a directory in
a shared filesystem.  It then statically creates a Local PersistentVolume for each
local volume.  It also monitors when the PersistentVolumes have been released, and
will clean up the volume, and recreate the PV.

## [Changelog](CHANGELOG.md)

## Development

Compile the provisioner
``` console
make
```

Make the container image and push to the registry
``` console
make push
```

## Design

There is one provisioner instance on each node in the cluster.  Each instance is
reponsible for monitoring and managing the local volumes on its node.

The basic components of the provisioner are as follows:

- Discovery: The discovery routine periodically reads the configured discovery
  directories and looks for new mount points that don't have a PV, and creates
  a PV for it.

- Deleter: The deleter routine is invoked by the Informer when a PV phase changes.
  If the phase is Released, then it cleans up the volume and deletes the PV API
  object.

- Cache: A central cache stores all the Local PersistentVolumes that the provisioner
  has created.  It is populated by a PV informer that filters out the PVs that
  belong to this node and have been created by this provisioner.  It is used by
  the Discovery and Deleter routines to get the existing PVs.

- Controller: The controller runs a sync loop that coordinates the other components.
  The discovery and deleter run serially to simplify synchronization with the cache
  and create/delete operations.
# local-volume-provisioner-bootstrap

local-volume-provisioner-bootstrap is used to bootstrap provisioner. The main use
case of bootstrapper is to make provisioner configurable. Below is a detailed flow
of how the bootstrap process works:

- looks for a configmap passed in via flag `-volume-config`; otherwise, a default
  configmap named `local-volume-default-config` will be created
- reads and validates the configmap, then auto-generates missing configurations,
  see below
- looks for a service account passed in via flag `-serviceaccount`; otherwise, a
  default service account named `local-storage-admin` will be created
- creates two cluster role bindings for the service account, i.e. `system:persistent-volume-provisioner`
  and `system:node`. The role bindings are named `local-storage:provisioner-node-binding` and
  `local-storage:provisioner-pv-binding` respectively.
- creates provisioner daemonset based on the service account, volume configmap,
  `-image` option, etc
- exit

## Configuration

### Volume config

Volume config is a map from storage class to volume configuration, i.e. `map[string]MountConfig`,
where `MountConfig` is the configuration for a single volume, see below.

```go
type MountConfig struct {
	// The hostpath directory
	HostDir string `json:"hostDir"`
	// The mount point of the hostpath volume
	MountDir string `json:"mountDir"`
}
```

- `HostDir` is required; it points to the directory where provisioner looks for
  local volumes.
- `MountDir` is optional, it is the path inside container where `hostDir` is mounted
  to. If omitted, `MountDir` will be auto-generated by bootstrapper. The generation
  rule is to trim '/' prefix and change "/" to "~" (based on kubernetes convention),
  then concatenate with root path. For example, suppose `-mountRoot` flag equals to
  "/mnt/local-storage" and `hostDir` equals to "/mnt/others", then generated `MountDir`
  will be "/mnt/local-storage/mnt~others".

Below is an example configmap:

```yaml
kind: ConfigMap
metadata:
  name: local-volume-config
  namespace: kube-system
data:
  "local-fast": |
    {
      "hostDir": "/mnt/ssds",
      "mountDir": "/local-ssds"
    }
  "local-slow": |
    {
      "hostDir": "/mnt/hdds",
      "mountDir": "/local-hdds"
    }
  "local-storage": |
    {
      "hostDir": "/mnt/disks"
    }
```

### Command line options

To see all options, compile bootstrapper and use `-h` option, below is a curated
list of important options:

- `-image`: Name of local volume provisioner image (default "quay.io/external_storage/local-volume-provisioner")
- `-volume-config`: Name of the local volume configuration configmap. The configmap
  must reside in the same namespace with bootstrapper. (default "local-volume-default-config")
- `-serviceaccount`: Name of the service accout for local volume provisioner
  (default "local-storage-admin")

## Development

Compile the bootstrapper:

```console
make
```

Make the container image and push to the registry
``` console
make push
```

Deploy to existing cluster:

```console
kubectl create -f deployment/kubernetes/example-config.yaml
kubectl create -f deployment/kubernetes/admin-account.yaml
kubectl create -f deployment/kubernetes/bootstrapper.yaml
```

## Future improvements

- Right now, bootstrapper is bound to cluster-admin role and provisioner is bound
  to system:node, system:persistent-volume-provisioner, these roles have more
  more privileges than we need. As a future enhancemnet, we can look into using
  different roles with fewer permissions.
- Bootstrapper will update user-created configmap if `MountDir` is omitted from
  user. We choose to update the confimap instead of auto-generating a new one
  because 1. the config will be shared between bootstrapper and provisioner; 2.
  the config only has settings for volumes so it won't mis-configure any other
  settings. We can revisit this when we have more settings in this configmap.
- Auto-generated `MountDir` doesn't take path length into consideration. If user
  provides a very long `HostPath`, bootstrapper will fail to create `MountDir`.
# Kubernetes external FLEX provisioner

This is an example external provisioner for kubernetes meant for use with FLEX based volume plugins.  The provisioner runs in a pod, so the shell script which provisions/deletes the volumes must also be included in the POD's container (and not on the host).

**First Steps**

Before building and packaging this, you need to include the shell script which flex will use for provisioning.  The shell script path must match what's in the provisioning container.

The current example is in flex/deploy/docker and is specified in examples/pod-provisioner.yaml here:
*- "-execCommand=/opt/storage/flex-provision.sh"*
If you copy in a new file or change the path, update the flag in the pod yaml.

**To Build**

```bash
make
```

**To Deploy**

You can use the example provisioner pod to deploy ```kubectl create -f examples/pod-provisioner.yaml```

# nfs-provisioner

[![Docker Repository on Quay](https://quay.io/repository/kubernetes_incubator/nfs-provisioner/status "Docker Repository on Quay")](https://quay.io/repository/kubernetes_incubator/nfs-provisioner)
```
quay.io/kubernetes_incubator/nfs-provisioner:v1.0.8
```

nfs-provisioner is an out-of-tree dynamic provisioner for Kubernetes 1.4. You can use it to quickly & easily deploy shared storage that works almost anywhere. Or it can help you write your own out-of-tree dynamic provisioner by serving as an example implementation of the requirements detailed in [the proposal](https://github.com/kubernetes/kubernetes/pull/30285). Go [here](./docs/demo) for a demo of how to use it and [here](../docs/demo/hostpath-provisioner) for an example of how to write your own.

It works just like in-tree dynamic provisioners: a `StorageClass` object can specify an instance of nfs-provisioner to be its `provisioner` like it specifies in-tree provisioners such as GCE or AWS. Then, the instance of nfs-provisioner will watch for `PersistentVolumeClaims` that ask for the `StorageClass` and automatically create NFS-backed `PersistentVolumes` for them. For more information on how dynamic provisioning works, see [the docs](http://kubernetes.io/docs/user-guide/persistent-volumes/) or [this blog post](http://blog.kubernetes.io/2016/10/dynamic-provisioning-and-storage-in-kubernetes.html).

## Quickstart
Choose some volume for your nfs-provisioner instance to store its state & data in and mount the volume at `/export` in `deploy/kubernetes/deployment.yaml`. It doesn't have to be a `hostPath` volume, it can e.g. be a PVC. Note that the volume must have a [supported file system](https://github.com/nfs-ganesha/nfs-ganesha/wiki/Fsalsupport#vfs) on it: any local filesystem on Linux is supported & NFS is not supported.
```yaml
...
  volumeMounts:
    - name: export-volume
      mountPath: /export
volumes:
  - name: export-volume
    hostPath:
      path: /tmp/nfs-provisioner
...
```

Choose a `provisioner` name for a `StorageClass` to specify and set it in `deploy/kubernetes/deployment.yaml`
```yaml
...
args:
  - "-provisioner=example.com/nfs"
...
```

Create the deployment.
```console
$ kubectl create -f deploy/kubernetes/deployment.yaml
service "nfs-provisioner" created
deployment "nfs-provisioner" created
```

Create a `StorageClass` named "example-nfs" with `provisioner: example.com/nfs`.
```console
$ kubectl create -f deploy/kubernetes/class.yaml
storageclass "example-nfs" created
```

Create a `PersistentVolumeClaim` with annotation `volume.beta.kubernetes.io/storage-class: "example-nfs"`
```console
$ kubectl create -f deploy/kubernetes/claim.yaml
persistentvolumeclaim "nfs" created
```

A `PersistentVolume` is provisioned for the `PersistentVolumeClaim`. Now the claim can be consumed by some pod(s) and the backing NFS storage read from or written to.
```console
$ kubectl get pv
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS      CLAIM         REASON    AGE
pvc-dce84888-7a9d-11e6-b1ee-5254001e0c1b   1Mi        RWX           Delete          Bound       default/nfs             23s
```

Deleting the `PersistentVolumeClaim` will cause the provisioner to delete the `PersistentVolume` and its data.

Deleting the provisioner deployment will cause any outstanding `PersistentVolumes` to become unusable for as long as the provisioner is gone.

## Running
Go [here](./docs/demo) for a demo of how to run nfs-provisioner. You may also/instead want to read the (dryer but more detailed) following docs.

To authorize nfs-provisioner on a Kubernetes cluster (only if you have RBAC and/or PSP enabled or are running OpenShift) see [Authorization](docs/authorization.md).

To deploy nfs-provisioner on a Kubernetes cluster see [Deployment](docs/deployment.md).

To use nfs-provisioner once it is deployed see [Usage](docs/usage.md).

For information on running multiple instances of nfs-provisioner see [Running Multiple Provisioners](docs/multiple.md).

## [Changelog](CHANGELOG.md)
Releases done here in external-storage will not have corresponding git tags (external-storage's git tags are reserved for versioning the library), so to keep track of releases check this README, the [changelog](CHANGELOG.md), or [Quay](https://quay.io/repository/kubernetes_incubator/nfs-provisioner)

## Writing your own
Go [here](../docs/demo/hostpath-provisioner) for an example of how to write your own out-of-tree dynamic provisioner.

## Roadmap
This is still alpha/experimental and will change to reflect the [out-of-tree dynamic provisioner proposal](https://github.com/kubernetes/kubernetes/pull/30285)

## Community, discussion, contribution, and support

Learn how to engage with the Kubernetes community on the [community page](http://kubernetes.io/community/).

You can reach the maintainers of this project at:

- Slack: #sig-storage

## Kubernetes Incubator

This is a [Kubernetes Incubator project](https://github.com/kubernetes/community/blob/master/incubator.md). The project was established 2016-11-15. The incubator team for the project is:

- Sponsor: Clayton (@smarterclayton)
- Champion: Brad (@childsb)
- SIG: sig-storage

### Code of conduct

Participation in the Kubernetes community is governed by the [Kubernetes Code of Conduct](code-of-conduct.md).
Please see [Deployment](../docs/deployment.md) for how to deploy nfs-provisioner on a Kubernetes cluster using these files.
#Demo

The [beta dynamic provisioning feature](http://blog.kubernetes.io/2016/10/dynamic-provisioning-and-storage-in-kubernetes.html) allows administrators to define `StorageClasses` to enable Kubernetes to create `PersistentVolumes` on-demand. Kubernetes includes many [provisioners](http://kubernetes.io/docs/user-guide/persistent-volumes/#provisioner) to specify in `StorageClasses` definitions and now, with Kubernetes 1.5, also includes support for [external or out-of-tree provisioners](https://github.com/kubernetes/kubernetes/pull/30285) like [nfs-provisioner](https://github.com/kubernetes-incubator/external-storage/nfs).

nfs-provisioner creates NFS-backed PV's, leveraging the NFS volume plugin of Kubernetes, so given the ubiquity of NFS it will work almost anywhere. It's ideal for local clusters and dev work, any place a PV is wanted but not the manual work of creating one. We'll demonstrate how to get it quickly up and running, following a variation of the Kubernetes repo's [NFS example](https://github.com/kubernetes/kubernetes/tree/release-1.5/examples/volumes/nfs).

If the cluster you intend to follow this demo with has RBAC and/or PSP enabled or it's an OpenShift cluster, you must first complete the [authorization guide](../authorization.md).

The recommended way to run nfs-provisioner, which we'll demonstrate here, is as a [single-instance stateful app](http://kubernetes.io/docs/tutorials/stateful-application/run-stateful-application/), where we create a `Deployment` and back it with some persistent storage like a `hostPath` volume. We always create it in tandem with a matching service that has the necessary ports exposed. We'll see that when it's setup like so, the NFS server it runs to serve its PV's can maintain state and so survive pod restarts. The other ways to run are as a `DaemonSet`, standalone Docker container, or standalone binary, all documented [here](../deployment.md)

There are two main things one can customize here before creating the deployment: the provisioner name and the backing volume.

The provisioner name must follow the naming scheme `<vendor name>/<provisioner name>`, like for example `kubernetes.io/gce-pd`. It's specified here in the `args` field. This is the `provisioner` a `StorageClass` will specify later. We'll use the name `example.com/nfs-tmp`.

```yaml
...
args:
  - "-provisioner=example.com/nfs"
...
```

The backing volume is the place mounted at `/export` where the nfs-provisioner instance stores its state and the data of every PV it provisions. So we can mount any volume there to specify that volume as the backing storage for provisioned PV's. We'll use a [`hostPath`](http://kubernetes.io/docs/user-guide/volumes/#hostpath) volume at `/tmp/nfs-provisioner`, so we need to make sure that the directory exists on the nodes our deployment's pod could be scheduled to and, if selinux is enforcing, that it is labelled appropriately.

```yaml
...
  volumeMounts:
    - name: export-volume
      mountPath: /export
volumes:
  - name: export-volume
    hostPath:
      path: /tmp/nfs-provisioner
...
```

```console
$ mkdir -p /tmp/nfs-provisioner
$ sudo chcon -Rt svirt_sandbox_file_t /tmp/nfs-provisioner
```

If you completed the [authorization guide](../authorization.md) (because your cluster has RBAC and/or PSP enabled or it's an OpenShift cluster) and it told you to remember to ensure the pod template of the deployment specifies the service account you created, do that now as well by adding a `serviceAccount` line.
```yaml
...
    spec:
      serviceAccount: nfs-provisioner
      containers:
...
```

We create the deployment and its service.

```console
$ kubectl create -f deployment.yaml
service "nfs-provisioner" created
deployment "nfs-provisioner" created
```

Now, our instance of nfs-provisioner can be treated like any other provisioner: we specify its name in a `StorageClass` object and the provisioner will automatically create `PersistentVolumes` for `PersistentVolumeClaims` that ask for the `StorageClass`. We'll show all that.

We create a `StorageClass` that specifies our provisioner.

```console
$ kubectl create -f class.yaml
storageclass "example-nfs" created
```

We create a `PersistentVolumeClaim` asking for our `StorageClass`.

```console
$ kubectl create -f claim.yaml
persistentvolumeclaim "nfs" created
```

And a `PersistentVolume` is provisioned automatically and already bound to our claim. We didn't have to manually figure out the NFS server's IP, put that IP into a PV yaml, then create the yaml. We just had to deploy our nfs-provisioner and create a `StorageClass` for it, which are one-time steps.

```console
$ kubectl get pv
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS      CLAIM         REASON    AGE
pvc-dce84888-7a9d-11e6-b1ee-5254001e0c1b   1Mi        RWX           Delete          Bound       default/nfs        
```

If you don't see a PV bound to your PVC, check the deployment's provisioner pod's logs using `kubectl logs` and look for events in the PVC using `kubectl describe`.

Now we have an NFS-backed PVC & PV pair that is exactly like what is expected by the official Kubernetes NFS example, so we'll finish the [example](https://github.com/kubernetes/kubernetes/tree/release-1.5/examples/volumes/nfs#setup-the-fake-backend) to show our storage works, can be shared, and persists. If you don't need that proof, you can skip ahead to the part where we discuss deleting and cleaning up the provisioner and its storage.

We setup the fake backend that updates `index.html` on the NFS server every 10 seconds. And check that our mounts are working.

```console
$ kubectl create -f nfs-busybox-rc.yaml
$ kubectl get pod -l name=nfs-busybox
NAME                READY     STATUS    RESTARTS   AGE
nfs-busybox-h782l   1/1       Running   0          13m
nfs-busybox-nul47   1/1       Running   0          13m
$ kubectl exec nfs-busybox-h782l -- cat /mnt/index.html
Mon Dec 19 18:10:09 UTC 2016
nfs-busybox-h782l
```

We setup the web server that reads from the NFS share and runs a simple web server on it. And check that `nginx` is serving the data, the `index.html` from above, appropriately.

```console
$ kubectl create -f nfs-web-rc.yaml
$ kubectl create -f nfs-web-service.yaml
$ kubectl get pod -l name=nfs-busybox
NAME                READY     STATUS    RESTARTS   AGE
nfs-busybox-h782l   1/1       Running   0          13m
nfs-busybox-nul47   1/1       Running   0          13m
$ kubectl get services nfs-web
NAME      CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
nfs-web   10.0.0.187   <none>        80/TCP    7s
$ kubectl exec nfs-busybox-h782l -- wget -qO- http://10.0.0.187
Mon Dec 19 18:11:51 UTC 2016
nfs-busybox-nul47
```

We see that the PV created by our nfs-provisioner works, let's now show that it will continue to work even after our nfs-provisioner pod restarts. Because of how NFS works, anything that has shares mounted will hang as it tries to access or unmount them while the NFS server is down. Recall that all our nfs-provisioner instance's state and data persists in the volume we mounted at `/export`, so it should recover and its shares become accessible again when it, and the NFS server it runs, restarts. We'll simulate this situation.

We scale the deployment down to 0 replicas.

```console
$ kubectl scale --replicas=0 deployment/nfs-provisioner
deployment "nfs-provisioner" scaled
```

We try the same check from before that `nginx` is serving the data, and we see it hangs indefinitely as it tries to read the share.

```console
$ kubectl exec nfs-busybox-h782l -- wget -qO- http://10.0.0.187
...
^C
```

We scale the deployment back up to 1 replica.

```console
$ kubectl scale --replicas=1 deployment/nfs-provisioner
deployment "nfs-provisioner" scaled
```

And after a brief delay all should be working again.

```console
$ kubectl exec nfs-busybox-h782l -- wget -qO- http://10.0.0.187
Mon Dec 19 18:21:49 UTC 2016
nfs-busybox-nul47
```

Now we'll show how to delete the storage provisioned by our nfs-provisioner once we're done with it. Let's first delete the fake backend and web server that are  using the PVC.

```console
$ kubectl delete rc nfs-busybox nfs-web
replicationcontroller "nfs-busybox" deleted
replicationcontroller "nfs-web" deleted
$ kubectl delete service nfs-web
service "nfs-web" deleted
```

Once all those pods have disappeared and so we are confident they have unmounted the NFS share, we can safely delete the PVC. The provisioned PV the PVC is bound to has the `ReclaimPolicy` `Delete`, so when we delete the PVC, the PV and its data will be automatically deleted by our nfs-provisioner.

```console
$ kubectl delete pvc nfs
persistentvolumeclaim "nfs" deleted
$ kubectl get pv
```

Note that deleting an nfs-provisioner instance won't delete the PV's it created, so before we do so we need to make sure none still exist as they would be useless for as long as the provisioner is gone.

```console
$ kubectl delete deployment nfs-provisioner
deployment "nfs-provisioner" deleted
$ kubectl delete service nfs-provisioner
service "nfs-provisioner" deleted
```

Thanks for following along. If at any point things didn't work correctly, check the provisioner pod's logs using `kubectl logs` and look for events in the PV's and PVC's using `kubectl describe`. If you are interested in Kubernetes storage-related things like this, head to the [Storage SIG](http://blog.kubernetes.io/2016/10/dynamic-provisioning-and-storage-in-kubernetes.html). If you are interested in writing your own external provisioner, all the code is available for you to read or fork, and better documentation on how to do it is in the works.

# efs-provisioner

[![Docker Repository on Quay](https://quay.io/repository/external_storage/efs-provisioner/status "Docker Repository on Quay")](https://quay.io/repository/external_storage/efs-provisioner)

The efs-provisioner allows you to mount EFS storage as PersistentVolumes in kubernetes. It consists of a container that has access to an AWS [EFS](https://aws.amazon.com/efs/) resource. The container reads a configmap which contains the EFS filesystem ID, the AWS region and the name you want to use for your efs-provisioner. This name will be used later when you create a storage class.

## Prerequisites
* An EFS file system in your cluster's region
* [Mount targets](http://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html) and [security groups](http://docs.aws.amazon.com/efs/latest/ug/accessing-fs-create-security-groups.html) such that any node (in any zone in the cluster's region) can mount the EFS file system by its [File system DNS name](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html)

## Getting Started

If you are new to Kubernetes or to PersistentVolumes this quick start will get you up and running with simple defaults.

- Download the manifest file [manifest.yaml](deploy/manifest.yaml).
  ```
  wget https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/aws/efs/deploy/manifest.yaml
  ```

- In the configmap section change the `file.system.id:` and `aws.region:` to match the details of the EFS you created.

- In the deployment section change the `server:` to the DNS endpoint of the EFS you created.

- `kubectl apply -f manifest.yaml` 

- Now you can use your PersistentVolume in your pod or deployment by referencing your claim name when it's created.

```
kind: Pod
apiVersion: v1
metadata:
  name: test-pod
spec:
  containers:
  - name: test-pod
    image: gcr.io/google_containers/busybox:1.24
    command:
      - "/bin/sh"
    args:
      - "-c"
      - "touch /mnt/SUCCESS && exit 0 || exit 1"
    volumeMounts:
      - name: efs-pvc
        mountPath: "/mnt"
  restartPolicy: "Never"
  volumes:
    - name: efs-pvc
      persistentVolumeClaim:
        claimName: efs
```

If you scale this pod each aditional pod will also be able to read and write the same files. You may also reference the same claimName in another type of pod so your 2 applications can read and write the same files. If you wish to have a second application that uses EFS storage but don't want other pods to access the files, create a new claim using a new name but the same storage class.

Some times you want the replica pods to be on EFS but you do not wish them to share the same files. In those situations it's best to use a [StatefulSet](./https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). When a StatefulSet scales up it will dynamically create new claims for your pods.

```
apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
---
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: gcr.io/google_containers/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: efs
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: efs
      annotations:
        volume.beta.kubernetes.io/storage-class: aws-efs
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Mi
```
Note: We do not reference a claim name, instead we give the new claim the name efs and we list the StorageClass we wish to use when creating the claim. I like to use the type of storage, because the name of the pod will be be added to it. This example when ran will create the claim `efs-web-0` and scaling the pod up to 3 will create `efs-web-1` and `efs-web-2`.

If you wish to learn more about efs-provisioner and how to change additional settings, you can continue on in the deployment section. You might also want to check the FAQ at the bottom.

## Deployment

Create a configmap containing the [**File system ID**](http://docs.aws.amazon.com/efs/latest/ug/gs-step-two-create-efs-resources.html) and Amazon EC2 region of the EFS file system you wish to provision NFS PVs from, plus the name of the provisioner, which administrators will specify in the `provisioner` field of their `StorageClass(es)`, e.g. `provisioner: example.com/aws-efs`.

```console
$ kubectl create configmap efs-provisioner \
--from-literal=file.system.id=fs-47a2c22e \
--from-literal=aws.region=us-west-2 \
--from-literal=provisioner.name=example.com/aws-efs
```

> See [Optional: AWS credentials secret](#optional-aws-credentials-secret) if you want the provisioner to only once at startup check that the EFS file system you specified in the configmap actually exists.

Decide on & set aside a directory within the EFS file system for the provisioner to use. The provisioner will create child directories to back each PV it provisions. Then edit the `volumes` section at the bottom of "deploy/deployment.yaml" so that the `path` refers to the directory you set aside and the `server` is the same EFS file system you specified.

```yaml
      volumes:
        - name: pv-volume
          nfs:
            server: fs-47a2c22e.efs.us-west-2.amazonaws.com
            path: /persistentvolumes
```
You will need to create the directory you use for `path:` on your EFS file system first or the efs-provisioner pod will fail to start.

```console
$ kubectl create -f deploy/deployment.yaml
deployment "efs-provisioner" created
```
If you are not using RBAC or OpenShift you can continue to the usage section.

### Authorization

If your cluster has RBAC enabled or you are running OpenShift you must authorize the provisioner. If you are in a namespace/project other than "default" either edit `deploy/auth/clusterrolebinding.yaml` or edit the `oadm policy` command accordingly.

#### RBAC
```console
$ kubectl create -f deploy/auth/serviceaccount.yaml
serviceaccount "efs-provisioner" created
$ kubectl create -f deploy/auth/clusterrole.yaml
clusterrole "efs-provisioner-runner" created
$ kubectl create -f deploy/auth/clusterrolebinding.yaml
clusterrolebinding "run-efs-provisioner" created
$ kubectl patch deployment efs-provisioner -p '{"spec":{"template":{"spec":{"serviceAccount":"efs-provisioner"}}}}'
```

#### OpenShift
```console
$ oc create -f deploy/auth/serviceaccount.yaml
serviceaccount "efs-provisioner" created
$ oc create -f deploy/auth/openshift-clusterrole.yaml
clusterrole "efs-provisioner-runner" created
$ oadm policy add-scc-to-user hostmount-anyuid system:serviceaccount:default:efs-provisioner
$ oadm policy add-cluster-role-to-user efs-provisioner-runner system:serviceaccount:default:efs-provisioner
$ oc patch deployment efs-provisioner -p '{"spec":{"template":{"spec":{"serviceAccount":"efs-provisioner"}}}}'
```
### SELinux
If SELinux is enforcing on the node where the provisioner runs, you must enable writing from a pod to a remote NFS server (EFS in this case) on the node by running:
```console
$ setsebool -P virt_use_nfs 1
$ setsebool -P virt_sandbox_use_nfs 1
```
https://docs.openshift.org/latest/install_config/persistent_storage/persistent_storage_nfs.html#nfs-selinux

## Usage

First a [`StorageClass`](https://kubernetes.io/docs/user-guide/persistent-volumes/#storageclasses) for claims to ask for needs to be created.

```yaml
apiVersion: storage.k8s.io/v1beta1
kind: StorageClass
metadata:
  name: slow
provisioner: example.com/aws-efs
parameters:
  gidMin: "40000"
  gidMax: "50000"
```

### Parameters

* `gidMin` + `gidMax` : The minimum and maximum value of GID range for the storage class. A unique value (GID) in this range ( gidMin-gidMax ) will be used for dynamically provisioned volumes. These are optional values. If not specified, the volume will be provisioned with a value between 2000-2147483647 which are defaults for gidMin and gidMax respectively.

Once you have finished configuring the class to have the name you chose when deploying the provisioner and the parameters you want, create it.

```console
$ kubectl create -f deploy/class.yaml 
storageclass "aws-efs" created
```

When you create a claim that asks for the class, a volume will be automatically created.

```console
$ kubectl create -f deploy/claim.yaml 
persistentvolumeclaim "efs" created
$ kubectl get pv
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM         REASON    AGE
pvc-557b4436-ed73-11e6-84b3-06a700dda5f5   1Mi        RWX           Delete          Bound     default/efs             2s
```
Note: any pod that consumes the claim will be able to read/write to the volume. This is because the volumes are provisioned with a GID (from the default range or according to `gidMin` + `gidMax`) and any pod that mounts the volume via the claim automatically gets the GID as a supplemental group.

---
##### Optional: AWS credentials secret

Create a secret containing the AWS credentials of a user assigned the AmazonElasticFileSystemReadOnlyAccess policy. The credentials will be used by the provisioner only once at startup to check that the EFS file system you specified in the configmap actually exists.

```console
$ kubectl create secret generic aws-credentials \
--from-literal=aws-access-key-id=AKIAIOSFODNN7EXAMPLE \
--from-literal=aws-secret-access-key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

Add a reference to the secret in the deployment yaml.
```yaml
...
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: aws-credentials
              key: aws-access-key-id
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: aws-credentials
              key: aws-secret-access-key
...
```

## FAQ

- Do I have to use a configmap?

Nope, the configmap values are just fed to the container as an environment variables. It is handy though when you create your EFS with Terraform and use Terraform to create the configmap dynamically.

- I noticed the EFS gets mounted directly to the efs-provisioner container, can I do that for my apps? 

Yes you can but it's not recommended. You lose the reusability of the StorageClass to be able to dynamically provision new PersistentVolumes for new containers and pods. 

- But what if the efs-provisoner pod goes down?

Your containers will continue to have EFS storage as they are mapped directly to EFS but behind the scenes they were mounted to a folder created by the EFS provisioner. New claims will not be provisioned nor deleted while the efs-provisioner pod is not running. When it comes backup it will catchup on any work it has missed.

- Can I scale the efs-provisioner accross my nodes? 

You can but it's not needed. You won't see a performance increase and you wont have a storage outage if the underlying node dies.

- Can I have multiple efs-provisioners pointed at multiple EFS mounts?

Yes you can, but would you really need to? EFS is designed to scale across many nodes and the efs-provisioner already has the ability to divide EFS into seperate chunks for your applications.

- I don't like the manual step of mounting and creating the /persistentvolumes directory. 

It's not needed but it is helpful if you are going to use your EFS for other things than Kubernetes. In your efs-provisioner deployment set your mounts like this...

```
          volumeMounts:
            - name: pv-volume
              mountPath: /persistentvolumes
      volumes:
        - name: pv-volume
          nfs:
            server: {{ efs_file_system_id }}.efs.{{ aws_region }}.amazonaws.com
            path: /
```

- I noticed when creating the claim it has request for a really small amount of storage?

The storage section size is a requirment because most other PersistentVolumes need it. Every pod accessing EFS will have unlimited storage. I use 1Mi to remind my self it's unlimited.

- Can I omit that part of the claim?

No, you must list a size even though it's not used with EFS.
# kubernetes nfs-client-provisioner

[![Docker Repository on Quay](https://quay.io/repository/external_storage/nfs-client-provisioner/status "Docker Repository on Quay")](https://quay.io/repository/external_storage/nfs-client-provisioner)

- pv provisioned as ${namespace}-${pvcName}-${pvName}
- pv recycled as archieved-${namespace}-${pvcName}-${pvName}

# deploy
- modify and deploy `deploy/deployment.yaml`
- modify and deploy `deploy/class.yaml`

## ARM based
To deploy on ARM based (Raspberry PI) use `deploy/deployment-arm.yaml` instead of `deploy/deployment.yaml`

# authorization

If your cluster has RBAC enabled or you are running OpenShift you must
authorize the provisioner. If you are in a namespace/project other than
"default" either edit `deploy/auth/clusterrolebinding.yaml` or edit the `oadm
policy` command accordingly.

## RBAC
```console
$ kubectl create -f deploy/auth/serviceaccount.yaml
serviceaccount "nfs-client-provisioner" created
$ kubectl create -f deploy/auth/clusterrole.yaml
clusterrole "nfs-client-provisioner-runner" created
$ kubectl create -f deploy/auth/clusterrolebinding.yaml
clusterrolebinding "run-nfs-client-provisioner" created
$ kubectl patch deployment nfs-client-provisioner -p '{"spec":{"template":{"spec":{"serviceAccount":"nfs-client-provisioner"}}}}'
```

## OpenShift
```console
$ oc create -f deploy/auth/serviceaccount.yaml
serviceaccount "nfs-client-provisioner" created
$ oc create -f deploy/auth/openshift-clusterrole.yaml
clusterrole "nfs-client-provisioner-runner" created
$ oadm policy add-scc-to-user hostmount-anyuid system:serviceaccount:default:nfs-client-provisioner
$ oadm policy add-cluster-role-to-user nfs-client-provisioner-runner system:serviceaccount:default:nfs-client-provisioner
$ oc patch deployment nfs-client-provisioner -p '{"spec":{"template":{"spec":{"serviceAccount":"nfs-client-provisioner"}}}}'
```

# test
- `kubectl create -f deploy/test-claim.yaml`
- `kubectl create -f deploy/test-pod.yaml`
- check the folder and file "SUCCESS" created
- `kubectl delete -f deploy/test-pod.yaml`
- `kubectl delete -f deploy/test-claim.yaml`
- check the folder renamed to `archived-???`
# Docs
* External provisioner library
	* [`hostPath` demo](demo/hostpath-provisioner/README.md) - a comprehensive walkthrough of how to use the library to write and build then run a `hostPath` provisioner (on a local one-node cluster)
	* More in-depth looks at particular topics:
		* [Building provisioner programs and managing dependencies](#building-provisioner-programs-and-managing-dependencies)
		* [Authorizing provisioners for RBAC or OpenShift](#authorizing-provisioners-for-rbac-or-openshift)
		* [Running multiple provisioners and giving provisioners identities](#running-multiple-provisioners-and-giving-provisioners-identities)
	* [The code](../lib/controller) - being a library, the code is *supposed* to be well-documented -- if you find it insufficient, open an issue
* [Contributing](#contributing)

## Building provisioner programs and managing dependencies

The library depends on [client-go](https://github.com/kubernetes/client-go) and your provisioner probably will too. This situation pretty much necessitates that you manage your dependencies with [vendoring](https://github.com/golang/go/wiki/PackageManagementTools) using a tool like [glide](https://github.com/Masterminds/glide).

Please see [client-go's installation doc](https://github.com/kubernetes/client-go/blob/master/INSTALL.md#installing-client-go) for a good explanation on how to depend on client-go and dependency management in general.

Let's say you've just finished writing your prototype provisioner. Now you want to vendor its dependencies using glide so that you can compile your program using the dependencies.

Your program's imports will probably include packages like these:

```go
import (
...
	"github.com/golang/glog"
	"github.com/kubernetes-incubator/external-storage/lib/controller"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/util/wait"
	"k8s.io/client-go/kubernetes"
	"k8s.io/api/core/v1"
	"k8s.io/client-go/rest"
)
```

Obviously the external provisioner library is there. So too are client-go and apimachinery, because they provide packages essential to applications made for Kubernetes.

Run `glide init` to populate a glide.yaml. When asked about using a release of external-storage answer Yes! But when asked about client-go or apimachinery, answer **No**! The reason you say No here is because external-storage depends on specific versions of these repos, and glide is not smart enough to always make the correct recommendation here.

```
[INFO]	The package github.com/kubernetes-incubator/external-storage appears to have Semantic Version releases (http://semver.org).
[INFO]	The latest release is v2.0.0. You are currently not using a release. Would you like
[INFO]	to use this release? Yes (Y) or No (N)
```

(If you ignore glide's prompts, you can always add `version` fields to your glide.yaml yourself later.)

Your glide.yaml will now look like this:

```yaml
package: github.com/kubernetes-incubator/external-storage/docs/demo/hostpath-provisioner
import:
- package: github.com/golang/glog
- package: github.com/kubernetes-incubator/external-storage
  version: v2.0.0
  subpackages:
  - lib/controller
- package: k8s.io/apimachinery
  subpackages:
  - pkg/apis/meta/v1
  - pkg/util/wait
- package: k8s.io/client-go
  subpackages:
  - kubernetes
  - pkg/api/v1
  - rest
```

At this point, if you run `glide install -v` glide *should* be smart enough to determine the correct versions of client-go/apimachinery to fetch, i.e. the versions that can satisfy both your and your other dependencies' (external-storage) requirements. But this is not a guarantee, so for your convenience, external-storage will always specify exactly what version of client-go/apimachinery to use on the [releases page](https://github.com/kubernetes-incubator/external-storage/releases). So add `version` fields to both client-go and apimachinery accordingly.

After you have edited your glide.yaml to your satisfaction, run `glide install -v` to get a vendor directory full of your dependencies which you can build your provisioner with.

Finally you'll want to build your program. You can write some sort of containerized build or stick to a `go build` invocation. In order for a `go build .` or variation thereof to work, you must
* be working in your `GOPATH`, your code has to be somewhere under "$GOPATH/src". This is a requirement (even) when using vendored dependencies
* have go version 1.8 or greater installed
The binary produced can then be e.g. used to make a Docker image.

## Authorizing provisioners for RBAC or OpenShift

The controller requires authorization to perform the following API calls:
* `get`, `list`, `watch`, `create`, `delete` "persistentvolumes"
* `get`, `list`, `watch`, `update` "persistentvolumeclaims"
* `get`, `list`, `watch` "storageclasses"
* `list`, `watch`, `create`, `update`, `patch` "events"

As of Kubernetes 1.6 these needed permissions are enumerated in an RBAC bootstrap `ClusterRole` named ["system:persistent-volume-provisioner"](https://github.com/kubernetes/kubernetes/blob/4e01d1d1412950250148d25ca607fb9585f4c86b/plugin/pkg/auth/authorizer/rbac/bootstrappolicy/testdata/cluster-roles.yaml#L693). In OpenShift this bootstrap `ClusterRole` doesn't yet exist but it would look exactly the same except for the `apiVersion` field.

As the author of your external provisioner you will need to instruct users on how to authorize the provisioner. Assuming you intend for the provisioner to be deployed as an application on top of Kubernetes/OpenShift, authorization means creating a service account for the provisioner to run as and granting the service account the needed permissions.

In Kubernetes you grant the needed permissions by creating a `ClusterRoleBinding` that refers to "system:persistent-volume-provisioner".
In OpenShift you do so by running something like: `oadm policy add-cluster-role-to-user system:persistent-volume-provisioner system:serviceaccount:default:my-provisioner`

For an example of what all this looks like, see the [EFS provisioner documentation](https://github.com/kubernetes-incubator/external-storage/tree/master/aws/efs#authorization) and its associated [yamls](https://github.com/kubernetes-incubator/external-storage/tree/master/aws/efs/deploy/auth).

## Running multiple provisioners and giving provisioners identities

You must determine whether you want to support the use-case of running multiple provisioner-controller instances in a cluster. Further, you must determine whether you want to implement this identity idea to address that use-case.

The library supports running multiple instances out of the box via its basic leader election implementation wherein multiple controllers trying to provision for the same class of claims race to lock/lead claims in order to be the one to provision for them. This prevents multiple provisioners from needlessly calling `Provision`, which is undesirable because only one will succeed in creating a PV and the rest will have wasted API calls and/or resources creating useless storage assets. Configuration of all this is done via controller parameters.

There is no such race to lock implementation for deleting PVs: all provisioners will call `Delete`, repeatedly until the storage asset backing the PV and the PV are deleted. This is why it's desirable to implement the identity idea, so that only the provisioner who is *responsible* for deleting a PV actually attempts to delete the PV's backing storage asset. The rest should return the special `IgnoredError` which indicates to the controller that they ignored the PV, as opposed to trying and failing (which would result in a misleading error message) or succeeding (obviously a bad idea to lie about that).

In some cases, the provisioner who is *responsible* for deleting a PV is also the only one *capable* of deleting a PV, in which case it's not only desirable to implement the identity idea, but necessary. This is the case with the `hostPath` provisioner example: obviously only the provisioner running on a certain host can delete the backing storage asset because the backing storage asset is local to the host.

Now, actually giving provisioners identities and effectively making them pets may be the hard part. In the `hostPath` example, the sensible thing to do was tie a provisioner's identity to the node/host it runs on. In your case, maybe it makes sense to tie each provisioner to e.g. a certain member in a storage pool. And should a certain provisioner die, when it comes back it should retain its identity lest the cluster be left with dangling volumes that no running provisioner can delete.

## Contributing

This repository is structured such that each external provisioner gets its own directory for its code, docs, examples, yamls, etc. What they don't get is individual "vendor" directories for their respective dependencies, they must depend on the shared top-level vendor and lib directories. This helps reduce the size of the repo and forces all parts of it to stay updated, but introduces some complications for contributors.

### Conventions
[Kubernetes project](https://github.com/kubernetes/kubernetes/) conventions are followed if not otherwise stated.

### Adding a provisioner

Basically you create a directory to house everything you want to check in, add build and/or test invocations to [travis](../.travis.yml), and add dependencies to the top-level vendor directory.

### Adding a vendor dependency

This repository uses [glide](https://github.com/Masterminds/glide) for package management. Add the packages to [glide.yaml](../glide.yaml), run "glide up -v", then run "glide-vc --use-lock-file".

### Updating a vendor dependency and/or contributing to the library

Any breaking update to a vendor dependency requires an update to every external provisioner that depends on it. It follows that any breaking update to the library requires an update to every external provisioner. If the provisioners that need to be updated are not updated, they simply won't build.

Generally, breaking vendor dependency updates won't happen often (at least every time kubernetes/client-go updates, maybe) and all the provisioners can be updated with ease, without requiring explicit approval from their respective OWNERS, unless the change is big enough or they've asked that it be required.

As the contributor of a dependency/library update, you're usually responsible for updating the dependents so travis CI passes, as it shouldn't be harder than a find/replace. Otherwise, if it's decided that you don't need to be responsible, some other solution will be worked out to make sure everything stays in a buildable state.

### Using Persistent Volume annotations
External provisioners may need to store custom data in Persistent Volume annotations. An annotation should have the below format:
```
annotations:
  <provisioner-type>.external-storage.incubator.kubernetes.io/<variable> : <value>
```
A usage example:
```
annotations:
  "manila.external-storage.incubator.kubernetes.io/ID": "de64eb77-05cb-4502-a6e5-7e8552c352f3"
```
# Writing an Out-of-tree Dynamic Provisioner

In this guide we'll demonstrate how to write an out-of-tree dynamic provisioner using [the helper library](https://github.com/kubernetes-incubator/external-storage/tree/master/lib)

## The Provisioner Interface

Ideally, all you should need to do to write your own provisioner is implement the `Provisioner` interface which has two methods: `Provision` and `Delete`. Then you can just pass it to the `ProvisionController`, which handles all the logic of calling the two methods. The signatures should be self-explanatory but we'll explain the methods in more detail anyhow. For this explanation we'll refer to the `ProvisionController` as the controller and the implementer of the `Provisioner` interface as the provisioner. The code can be found in the [`controller` directory](https://github.com/kubernetes-incubator/external-storage/tree/master/lib/controller)

```go
Provision(VolumeOptions) (*v1.PersistentVolume, error)
```

`Provision` creates a storage asset and returns a `PersistentVolume` object representing that storage asset. The given `VolumeOptions` object includes information needed to create the PV: the PV's reclaim policy, PV's name, the PVC object for which the PV is being provisioned (which has in its spec capacity & access modes), & parameters from the PVC's storage class.

You should store any information that will be later needed to delete the storage asset here in the PV using annotations. It's also recommended that you give every instance of your provisioner a unique identity and store it on the PV using an annotation here, for reasons we will see soon.

`Provision` is not responsible for actually creating the PV, i.e. submitting it to the Kubernetes API, it just returns it and the controller handles creating the API object.

```go
Delete(*v1.PersistentVolume) error
```

`Delete` removes the storage asset that was created by `Provision` to back the given PV. The given PV will still have any useful annotations that were set earlier in `Provision`.

Special consideration must be given to the case where multiple controllers that serve the same storage class (that have the same `provisioner` name) are running: how do you know that *this* provisioner was the one to provision the given PV? This is why it's recommended to store a provisioner's identity on its PVs in `Provision`, so that each can remember if it was the one to provision a PV when it comes time to delete it, and if not, ignore it by returning `IgnoredError`. If you are confused by any of this, please continue through the `hostPath` example to see a practical implementation and if that isn't enough, please read [this doc](../../README.md#running-multiple-provisioners-and-giving-provisioners-identities) after the example.

`Delete` is not responsible for actually deleting the PV, i.e. removing it from the Kubernetes API, it just deletes the storage asset backing the PV and the controller handles deleting the API object.

## Writing a `hostPath` Dynamic Provisioner

Now that we understand the interface expected by the controller, let's implement it and create our own out-of-tree `hostPath` dynamic provisioner. This is for single node testing and demonstration purposes only - local storage is not supported in any way and will not work on multi-node clusters. This simple program has the power to delete and create local data on your node, so if you intend to actually follow along and run it, be careful!

We define a `hostPathProvisioner` struct. It will back every `hostPath` PV it provisions with a new child directory in `pvDir`, hard-coded here to `/tmp/hostpath-provisioner`. It will also give itself a unique `identity`, set to the name of the node/host it runs on, which is passed in via an env variable.

```go
type hostPathProvisioner struct {
	// The directory to create PV-backing directories in
	pvDir string

	// Identity of this hostPathProvisioner, set to node's name. Used to identify
	// "this" provisioner's PVs.
	identity string
}

func NewHostPathProvisioner() controller.Provisioner {
	nodeName := os.Getenv("NODE_NAME")
	if nodeName == "" {
		glog.Fatal("env variable NODE_NAME must be set so that this provisioner can identify itself")
	}
	return &hostPathProvisioner{
		pvDir:    "/tmp/hostpath-provisioner",
		identity: nodeName,
	}
}
```

We implement `Provision`. It creates a directory with the name `options.PVName`, which is always unique to the PVC being provisioned for, in `pvDir`. It sets a custom `identity` annotation on the PV and fills in the other fields of the PV according to the `VolumeOptions` to satisfy the PVC's requirements. And the PV's `PersistentVolumeSource` is of course set to a `hostPath` volume representing the directory just created.

```go
// Provision creates a storage asset and returns a PV object representing it.
func (p *hostPathProvisioner) Provision(options controller.VolumeOptions) (*v1.PersistentVolume, error) {
	path := path.Join(p.pvDir, options.PVName)

	if err := os.MkdirAll(path, 0777); err != nil {
		return nil, err
	}

	pv := &v1.PersistentVolume{
		ObjectMeta: metav1.ObjectMeta{
			Name: options.PVName,
			Annotations: map[string]string{
				"hostPathProvisionerIdentity": p.identity,
			},
		},
		Spec: v1.PersistentVolumeSpec{
			PersistentVolumeReclaimPolicy: options.PersistentVolumeReclaimPolicy,
			AccessModes:                   options.PVC.Spec.AccessModes,
			Capacity: v1.ResourceList{
				v1.ResourceName(v1.ResourceStorage): options.PVC.Spec.Resources.Requests[v1.ResourceName(v1.ResourceStorage)],
			},
			PersistentVolumeSource: v1.PersistentVolumeSource{
				HostPath: &v1.HostPathVolumeSource{
					Path: path,
				},
			},
		},
	}

	return pv, nil
}
```

We implement `Delete`. First it checks if this provisioner was the one that created the directory backing the given PV by looking at the identity annotation. If not, it returns an `IgnoredError`: the safest assumption is that some other `hostPath` provisioner that is/was running on a different node was the one that created the directory on that different node, so it would be a dangerous idea for *this* provisioner to attempt to delete the directory here on *this* node! Otherwise, if the identity annotation matches this provisioner's, it can safely delete the directory.

```go
// Delete removes the storage asset that was created by Provision represented
// by the given PV.
func (p *hostPathProvisioner) Delete(volume *v1.PersistentVolume) error {
	ann, ok := volume.Annotations["hostPathProvisionerIdentity"]
	if !ok {
		return errors.New("identity annotation not found on PV")
	}
	if ann != p.identity {
		return &controller.IgnoredError{"identity annotation on PV does not match ours"}
	}

	path := path.Join(p.pvDir, volume.Name)
	if err := os.RemoveAll(path); err != nil {
		return err
	}

	return nil
}
```

Now all that's left is to connect our `Provisioner` with a `ProvisionController` and run the controller, all in `main`. This part will look largely the same regardless of how the provisioner interface is implemented. We'll write it such that it expects to be run as a pod in Kubernetes.

We need to create a couple of things the controller expects as arguments, including our `hostPathProvisioner`, before we create and run it. First we create a client for communicating with Kubernetes from within a pod. We use it to determine the server version of Kubernetes. Then we create our `hostPathProvisioner`. We pass all of these things into `NewProvisionController`, plus some other arguments we'll explain now. 

* `resyncPeriod` determines how often the controller relists PVCs and PVs to check if they should be provisioned for or deleted.
* `provisionerName` is the `provisioner` that storage classes will specify, "example.com/hostpath" here.  It must follow the `<vendor name>/<provisioner name>` naming scheme and `<vendor name>` cannot be "kubernetes.io"
* `exponentialBackOffOnError` determines whether it should exponentially back off from calls to `Provision` or `Delete`, useful if either of those involves some API call.
* `failedRetryThreshold` is the threshold for failed `Provision` attempts before giving up trying to provision for a claim.
* The last four arguments configure leader election wherein mutliple controllers trying to provision for the same class of claims race to lock/lead claims in order to be the one to provision for them. The meaning of these parameters is documented in the [leaderelection package](https://github.com/kubernetes-incubator/external-storage/tree/master/lib/leaderelection). If you don't intend for users to run more than one instance of your provisioner for the same class of claims, you may ignore these and simply use the default as we do here. See [this doc](../../README.md#running-multiple-provisioners-and-giving-provisioners-identities) for more info on running multiple provisioners.

(There are many other possible parameters of the controller that could be exposed, please create an issue if you would like one to be.)

Finally, we create and `Run` the controller.

```go
const (
	resyncPeriod              = 15 * time.Second
	provisionerName           = "example.com/hostpath"
	exponentialBackOffOnError = false
	failedRetryThreshold      = 5
	leasePeriod               = leaderelection.DefaultLeaseDuration
	retryPeriod               = leaderelection.DefaultRetryPeriod
	renewDeadline             = leaderelection.DefaultRenewDeadline
	termLimit                 = leaderelection.DefaultTermLimit
)
```
```go
func main() {
	flag.Parse()
	// Create an InClusterConfig and use it to create a client for the controller
	// to use to communicate with Kubernetes
	config, err := rest.InClusterConfig()
	if err != nil {
		glog.Fatalf("Failed to create config: %v", err)
	}
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		glog.Fatalf("Failed to create client: %v", err)
	}

	// The controller needs to know what the server version is because out-of-tree
	// provisioners aren't officially supported until 1.5
	serverVersion, err := clientset.Discovery().ServerVersion()
	if err != nil {
		glog.Fatalf("Error getting server version: %v", err)
	}

	// Create the provisioner: it implements the Provisioner interface expected by
	// the controller
	hostPathProvisioner := NewHostPathProvisioner()

	// Start the provision controller which will dynamically provision hostPath
	// PVs
	pc := controller.NewProvisionController(clientset, resyncPeriod, "example.com/hostpath", hostPathProvisioner, serverVersion.GitVersion, exponentialBackOffOnError, failedRetryThreshold, leasePeriod, renewDeadline, retryPeriod, termLimit)
	pc.Run(wait.NeverStop)
}
```

We're now done writing code. The code we wrote can be found [here](./hostpath-provisioner.go). The other files we'll use in the remainder of the walkthrough can be found in the same directory.

Notice we just import "github.com/kubernetes-incubator/external-storage/lib/controller" to get access to the required interface and function.

## Building and Running our `hostPath` Dynamic Provisioner

Before we can run our provisioner in a pod we need to build a Docker image for the pod to specify. Our hostpath-provisioner Go package has many dependencies so it's a good idea to use a tool to manage them. It's especially important to do so when depending on a package like [client-go](https://github.com/kubernetes/client-go#how-to-get-it) that has an unstable master branch. We'll use [glide](https://github.com/Masterminds/glide).

In order for the build method described below to work, you must
* be working in your `GOPATH`, your code has to be somewhere under "$GOPATH/src". This is a requirement (even) when using vendored dependencies
* have go version 1.7 or greater installed
* have Docker installed

Our [glide.yaml](./glide.yaml) was created by manually setting the latest version of external-storage/lib & setting the version of client-go to the same one that external-storage/lib uses. We use it to populate a vendor directory containing dependencies. For more information on how to get this build working, see [this doc](../../README.md#building-provisioner-programs-and-managing-dependencies).

Now we can use build & run our hostpath-provisioner using a simple Makefile where we first we run `glide install -v` to get the dependencies listed in our glide.yaml, then do a static go build of our program that can run in our "FROM scratch" Dockerfile.

```make
...
image: hostpath-provisioner
	docker build -t $(IMAGE) -f Dockerfile.scratch .

hostpath-provisioner: $(shell find . -name "*.go")
	glide install -v --strip-vcs
	CGO_ENABLED=0 go build -a -ldflags '-extldflags "-static"' -o hostpath-provisioner .
...
```
```Dockerfile
FROM scratch
COPY hostpath-provisioner /
CMD ["/hostpath-provisioner"]
```

We run make. Note that the Docker image needs to be on the node we'll run the pod on. So you may need to tag your image and push it to Docker Hub so that it can be pulled later by the node, or just work on the node and build the image there.

```console
$ make
...
Successfully built c3cd467b5fbe
```

Now we can specify our image in a pod. Recall that we set `pvDir` to `/tmp/hostpath-provisioner`. Since we are running our provisioner in a container as a pod, we should mount a corresponding `hostPath` volume there to serve as the parent of all provisioned PVs' `hostPath` volumes.

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: hostpath-provisioner
spec:
  containers:
    - name: hostpath-provisioner
      image: hostpath-provisioner:latest
      imagePullPolicy: "IfNotPresent"
      volumeMounts:
        - name: pv-volume
          mountPath: /tmp/hostpath-provisioner
  volumes:
    - name: pv-volume
      hostPath:
        path: /tmp/hostpath-provisioner
```

If SELinux is enforcing, we need to label `/tmp/hostpath-provisioner` so that it can be accessed by pods. We do this on the single node those pods will be scheduled to.

```console
$ mkdir -p /tmp/hostpath-provisioner
$ sudo chcon -Rt svirt_sandbox_file_t /tmp/hostpath-provisioner
```

## Using our `hostPath` Dynamic Provisioner

As said before, this dynamic provisioner is for single node testing purposes only. It has been tested to work with [hack/local-up-cluster.sh](https://github.com/kubernetes/kubernetes/blob/release-1.5/hack/local-up-cluster.sh) started like so. If you want to run your provisioner on a cluster with RBAC enabled or an OpenShift cluster, please see [this doc](../../README.md#authorizing-provisioners-for-rbac-or-openshift).

```console
$ API_HOST_IP=0.0.0.0 $GOPATH/src/k8s.io/kubernetes/hack/local-up-cluster.sh
```

Once our cluster is running, we create the hostpath-provisioner pod. Note how we populate the "NODE_NAME" variable.

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: hostpath-provisioner
spec:
  containers:
    - name: hostpath-provisioner
      image: hostpath-provisioner:latest
      imagePullPolicy: "IfNotPresent"
      env:
        - name: NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
      volumeMounts:
        - name: pv-volume
          mountPath: /tmp/hostpath-provisioner
  volumes:
    - name: pv-volume
      hostPath:
        path: /tmp/hostpath-provisioner
```
```console
$ kubectl create -f pod.yaml
pod "hostpath-provisioner" created
```

Before proceeding, we check that it doesn't immediately crash due to one of the fatal conditions we wrote.

```console
$ kubectl get pod
NAME                   READY     STATUS    RESTARTS   AGE
hostpath-provisioner   1/1       Running   0          5s
```

Now we create a `StorageClass` & `PersistentVolumeClaim` and see that a `PersistentVolume` is automatically created.

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1beta1
metadata:
  name: example-hostpath
provisioner: example.com/hostpath
```

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: hostpath
  annotations:
    volume.beta.kubernetes.io/storage-class: "example-hostpath"
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Mi
```

```console
$ kubectl create -f class.yaml
storageclass "example-hostpath" created
$ kubectl create -f claim.yaml
persistentvolumeclaim "hostpath" created
$ kubectl get pv
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM              REASON    AGE
pvc-f41f0dfc-c7bf-11e6-8c5d-c81f66424618   1Mi        RWX           Delete          Bound     default/hostpath             8s
```

If we check the contents of `/tmp/hostpath-provisioner` on the node we should see the PV's backing directory.

```console
$ ls /tmp/hostpath-provisioner/
pvc-f41f0dfc-c7bf-11e6-8c5d-c81f66424618
```

Now let's do a simple test: have a pod use the claim and write to it. We create such a pod and see that it succeeds.

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: test-pod
spec:
  containers:
  - name: test-pod
    image: gcr.io/google_containers/busybox:1.24
    command:
      - "/bin/sh"
    args:
      - "-c"
      - "touch /mnt/SUCCESS && exit 0 || exit 1"
    volumeMounts:
      - name: hostpath-pvc
        mountPath: "/mnt"
  restartPolicy: "Never"
  volumes:
    - name: hostpath-pvc
      persistentVolumeClaim:
        claimName: hostpath
```
```console
$ kubectl create -f test-pod.yaml
pod "test-pod" created
$ kubectl get pod --show-all
NAME                   READY     STATUS      RESTARTS   AGE
hostpath-provisioner   1/1       Running     0          2m
test-pod               0/1       Completed   0          8s
```

If we check the contents of the PV's backing directory we should see the data it wrote.

```console
$ ls /tmp/hostpath-provisioner/pvc-f41f0dfc-c7bf-11e6-8c5d-c81f66424618
SUCCESS
```

When we delete the PVC, the PV it was bound to and the data will be deleted also.

```console
$ kubectl delete pvc --all
persistentvolumeclaim "hostpath" deleted
$ kubectl get pv
No resources found.
$ ls /tmp/hostpath-provisioner
```

Finally, we delete the provisioner pod when it has deleted all its PVs and it's no longer wanted.

```console
$ kubectl delete pod hostpath-provisioner
pod "hostpath-provisioner" deleted
```


## Extras
So as we can see, it can be easy to write a simple but useful dynamic provisioner. For something more complicated here are some various other things to consider...

We did not show how to parse `StorageClass` parameters. They are passed from the storage class as a `map[string]string` to `Provision`, so you can define and parse any arbitrary set of parameters you want. You must reject parameters that you don't recognize.

We made it so our hostpath-provisioner binary must run from within a Kubernetes cluster. But it's also possible to have it communicate with Kubernetes from [outside](https://github.com/kubernetes/client-go/blob/release-2.0/examples/out-of-cluster/main.go). nfs-provisioner can do this and defines this (and other) behaviour using flags/arguments.

Note that the errors returned by Provision/Delete are sent as events on the PVC/PV and this is the primary way of communicating with the user, so they should be understandable.

If there is some behaviour of the controller you would like to change, feel free to open an issue. There are many parameters that could easily be made configurable but aren't because it would be too messy. The controller is written to follow the [proposal](https://github.com/kubernetes/kubernetes/pull/30285) and be like the upstream PV controller as much as possible, but there is always room for improvement.

It's possible (but not pretty) to write e2e tests for your provisioner that look similar to kubernetes e2e tests by copying files from the e2e framework and fixing import statements. Like [here](https://github.com/kubernetes-incubator/external-storage/tree/master/nfs/test/e2e). Keep in mind the license, etc. In your case, unit & integration tests may be sufficient. 
# iSCSI-targetd provisioner 

iSCSI-targetd provisioner is an out of tree provisioner for iSCSI storage for
Kubernetes and OpenShift.  The provisioniner uses the API provided by
[targetd](https://github.com/open-iscsi/targetd) to create and export
iSCSI storage on a remote server.

## Prerequisites

iSCSI-targetd provisioner has the following prerequisistes:

1. an iSCSI server managed by `targetd`
2. all the openshift nodes correclty configured to communicate with the iSCSI server
3. sufficient disk space available as LVM2 volume group (thinly provisioned volumes are also supported and can be used to alleviate this requirement)

## How it works

When a pvc request is issued for an iscsi provisioner controlled
storage class the following happens:

1. a new volume in the configured volume group is created, the size of
the volume corresponds to the size requested in the pvc
2. the volume is exported to the first available lun and made
accessible to all the configured initiators.
3. the corresponding pv is created and bound to the pvc.


Each storage class is tied to an iSCSI target and a volume
group. Because a target can manage a maximum of 255 LUNs, each
storage class manages at most 255 pvs. iSCSI-targetd provisioner can manage
multiple storage classes.

## Installing the prerequisites

These instructions should work for RHEL/CentOS 7+ and Fedora 24+.

On Fedora 24, current updates to the SELinux policy do not work with
targetd.  There is a bug filed:
https://bugzilla.redhat.com/show_bug.cgi?id=1451139 Until this bug is
resolve, SELinux must be set to permissive mode on Fedora 25+.

For RHEL and Centos make sure you install targetd >= 0.8.6-1 as in 
previous versions there a bug that prevented exposing a volume to more 
than one initiator 

### A note about names

In various places, iSCSI Qualified Names (IQNs) need to be created.
These need to be unique.  So every target must have it's own unique
IQN, and every client (initiator) must have its own IQN.

IF NON-UNIQUE IQNs ARE USED, THEN THERE IS A POTENTIAL FOR DATA LOSS
AND BAD PERFORMANCE!

IQNs have a specific format:

iqn.YEAR-MM.com.example.blah:tag

See the [wikipedia
article](https://en.wikipedia.org/wiki/ISCSI#Addressing) for more
information.

### Configure Storage

Before configuring the iSCSI server, it needs to have storage
configured.  `targetd` uses LVM to provision storage.

If possible, it's best to have a dedicated disk or partition that can
be configured as a volume group.  However, if this is not possible, a
loopback device can be used to simulate a dedicated block device.

#### Create a Volume Group with a dedicated disk or partition

This requires an additional dedicated disk or partition to use for the
volume group.  If that's not possible, see the section on using a
loopback device.

Assuming that the dedicated block device is `/dev/vdb` and that
`targetd` is configured to use `vg-targetd`:

```
pvcreate /dev/vdb
vgcreate vg-targetd /dev/vdb
```

#### Create a Volume Group on a Loopback Device
the volume group should be called `vg-target`, this way you don' have to change any default

here is how you would do it in minishift
```
cd /var/lib/minishift
sudo dd if=/dev/zero of=disk.img bs=1G count=2
export LOOP=`sudo losetup -f`
sudo losetup $LOOP disk.img
sudo vgcreate vg-targetd $LOOP
```

#### Optional:  Enable Thin Provisioning

Logical Volumes created in a volume group are thick provisioned by
default, i.e. space is reserved at time of creation.  Optionally, a
LVM can use a thin provisioning pool to create thin provisioned volumes.  

To create a thin provisioning pool, called `pool` this example,
execute the following commands:

```
# This will create a 15GB thin pool in the vg-targetd volume group
lvcreate -L 15G --thinpool pool vg-targetd
```

When configuring `targetd`, the pool_name setting in targetd.yaml will
need to be set to <volume group name>/<thin pool name>.  In this
example, it would be `vg-targetd/pool`.

### Configure the iSCSI server

#### Install targetd and targetcli

Only `targetd` needs to be installed.  However, it's highly recommended
to also install `targetcli` as it provides a simple user interface for
looking at the state of the iSCSI system.

```
sudo yum install -y targetcli targetd

```

#### Configure target

Enable and start `target.service`.  This will ensure that iSCSI
configuration persists through reboot.

```
sudo systemctl enable target
sudo systemctl start target
```

#### Configure targetd

First, edit `/etc/target/targetd.yaml`.  A working sample
configuration is provided below:

```
password: ciao

# defaults below; uncomment and edit
# if using a thin pool, use <volume group name>/<thin pool name>
# e.g vg-targetd/pool
pool_name: vg-targetd
user: admin
ssl: false
target_name: iqn.2003-01.org.linux-iscsi.minishift:targetd
```

Next, enable and start `targetd.service`.

```
sudo systemctl enable targetd
sudo systemctl start targetd
```

#### Configure the Firewall

The default configuration requires that port 3260/tcp, 3260/udp and
18700/tcp be open on the iSCSI server.

If using `firewalld`, 

```
firewall-cmd --add-service=iscsi-target --permanent
firewall-cmd --add-port=18700/tcp --permanent 
firewall-cmd --reload
```

Otherwise, add the following iptables rules to `/etc/sysconfig/iptables`

```
TODO
```

### Configure the nodes (iscsi clients)

#### Install the iscsi-initiator-utils package

The `iscsiadm` command is required for all clients.  This is provided
by the `iscsi-initiator-utils` package and should be part of the
standard RHEL, CentOS or Fedora installation.

```
sudo yum install -y iscsi-initiator-utils
```

#### Configure the Initiator Name

Each node requires a unique initiator name.  USE OF DUPLICATE NAMES
MAY CAUSE PERFORMANCE ISSUES AND DATA LOSS.

By default, a random initiator name is generated when the
`iscsi-initiator-utils` package is installed.  This usually unique
enough, but is not guaranteed.  It's also not very descriptive.

To set a custom initiator name, edit the file `/etc/iscsi/initiatorname.iscsi`:

```
InitiatorName=iqn.2017-04.com.example:node1
```

In the above example, the initiator name is set to
`iqn.2017-04.com.example:node1`.

After changing the initiator name, restart `iscsid.service`.

```
sudo systemctl restart iscsid

```
### Install the iscsi provisioner pod in Kubernetes
Run the following commands. The secret correspond to username and password you have chosen for targetd (admin is the default for the username).
This set of command will install iSCSI-targetd provisioner in the `default` namespace.
```
export NS=default 
kubectl create secret generic targetd-account --from-literal=username=admin --from-literal=password=ciao -n $NS
kubectl apply -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/kubernetes/iscsi-provisioner-d.yaml -n $NS
kubectl apply -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/kubernetes/iscsi-provisioner-pvc.yaml -n $NS
```

### Install the iscsi provisioner pod in Openshift

Run the following commands. The secret correspond to username and password you have chosen for targetd (admin is the default for the username)
```
oc new-project iscsi-provisioner
oc create sa iscsi-provisioner
oc adm policy add-cluster-role-to-user cluster-reader system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc adm policy add-cluster-role-to-user system:pv-provisioner-controller system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc adm policy add-cluster-role-to-user system:pv-binder-controller system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc adm policy add-cluster-role-to-user system:pv-recycler-controller system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc secret new-basicauth targetd-account --username=admin --password=ciao
oc create -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/openshift/iscsi-provisioner-dc.yaml
```
### Create a storage class
storage classes should look like the following
```
kind: StorageClass
apiVersion: storage.k8s.io/v1beta1
metadata:
  name: iscsi
provisioner: iscsi
parameters:
# this id where the iscsi server is running
  targetPortal: 192.168.99.100:3260
  
# this is the iscsi server iqn  
  iqn: iqn.2003-01.org.linux-iscsi.minishift:targetd
  
# this is the iscsi interface to be used, the default is default
# iscsiInterface: default

# this must be on eof the volume groups condifgured in targed.yaml, the default is vg-targetd
# volumeGroup: vg-targetd

# this is a comma separated list of initiators that will be give access to the created volumes, they must correspond to what you have configured in your nodes.
  initiators: iqn.2017-04.com.example:node1 
```
you can create one with the following command in kubernetes

```
oc create -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/kubernetes/iscsi-provisioner-class.yaml
```
or this command in openshift
```
oc create -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/openshift/iscsi-provisioner-class.yaml
```
### Test iscsi provisioner
Create a pvc
```
oc create -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/openshift/iscsi-provisioner-pvc.yaml
```
verify that the pv has been created
```
oc get pv
```
you may also want to verify that the volume has been created in you volume group
```
targetcli ls
```
deploy a pod that uses the pvc
```
oc create -f https://raw.githubusercontent.com/kubernetes-incubator/external-storage/master/iscsi/targetd/openshift/iscsi-test-pod.yaml
```
## Installing iSCSI provisioner using ansible

If you have installed OpenShift using the ansible installer you can use a set of playbook to automate the above instructions.
You can find more documentation on these playbooks [here](./ansible/README.md)
before running the playbooks you need to annotate the inventory file with some additional variables and the nodes with the iscsi inititator name that you want to be created. Here is a summary of the variables:

| Variable Name  | Description  |
|---|---|
| targetd_lvm_volume_group |  the volume group to be created |
| targetd_lvm_physical_volume| comma separated list of devices to add to the volume group  |
| targetd_password  | the password used to authenticate the connection to targetd, you may want to not store this on your inventory file, you can pass this as `{{ lookup('env','TARGETD_PASSWORD') }}`  |
|  targetd_user |  the username used to authenticate the connection to targetd, you may want to not store this on your inventory file, you can pass this as `{{ lookup('env','TARGETD_USERNAME') }}` |
| targetd_iscsi_target | the name of the target to be created in the target server  |
| iscsi_provisioner_pullspec |  the location of the iSCSI-targetd provisioner image |
| iscsi_provisioner_default_storage_class | whether the created storage class should be the default class  |

All the nodes should have a label with their defining the initiator name for that node, here is an example:

```
ose-node1.cscc openshift_node_labels="{'region': 'primary', 'zone': 'default'}" iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-node1
ose-node2.cscc openshift_node_labels="{'region': 'primary', 'zone': 'default'}" iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-node2
```


To install iSCSI provisioner using ansible, run the following
```
ansible-playbook -i <your inventory file> ansible/targetd-playbook.yaml
ansible-playbook -i <your inventory file> ansible/initiator-playbook.yaml
ansible-playbook -i <your inventory file> ansible/provisioner-playbook.yaml
```# Ansible Playbooks for iSCSI provisioner

This folder contains simple ansible playbooks to help
configure targetd and the iSCSI provisioner.

They are intended to be used with an inventory file belonging 
to OpenShift Container Platform 3.4+ or OpenShift Origin 1.4+

## Playbooks:

* targetd-playbook.yaml - Configures the targetd server, including LVM
* initiator-playbook.yaml - Configures the initiators
* provisioner-playbook.yaml - Configures OpenShift project and provisioner

These should be run in order above.

## Bugs

Currently, it appears that the targetd server needs to be rebooted if 
firewalld is not currently installed.

## Example Host File

```
[OSEv3:children]
masters
nodes
etcd
targetd

[OSEv3:vars]
targetd_lvm_volume_group=vg-targetd
targetd_lvm_physical_volume=/dev/vdb
targetd_password=ciao
targetd_user=admin
targetd_iscsi_target=iqn.2003-01.org.example.mach1:1234
iscsi_provisioner_pullspec=raffaelespazzoli/iscsi-controller:0.0.1
iscsi_provisioner_default_storage_class=true

[targetd]
targetd.cscc

[nodes]
ose-master1.cscc openshift_node_labels="{'region': 'infra', 'zone': 'default'}" openshift_schedulable=true iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-master1
ose-master2.cscc openshift_node_labels="{'region': 'infra', 'zone': 'default'}" openshift_schedulable=true iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-master2
ose-master3.cscc openshift_node_labels="{'region': 'infra', 'zone': 'default'}" openshift_schedulable=true iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-master3
ose-node1.cscc openshift_node_labels="{'region': 'primary', 'zone': 'default'}" iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-node1
ose-node2.cscc openshift_node_labels="{'region': 'primary', 'zone': 'default'}" iscsi_initiator_name=iqn.2003-03.net.deadvax:ose-node2
```
# install iscsi controller

```
oc new-project iscsi-provisioner
oc create sa iscsi-provisioner
oc adm policy add-cluster-role-to-user cluster-reader system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc adm policy add-cluster-role-to-user system:pv-provisioner-controller system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc adm policy add-cluster-role-to-user system:pv-binder-controller system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc adm policy add-cluster-role-to-user system:pv-recycler-controller system:serviceaccount:iscsi-provisioner:iscsi-provisioner
oc create -f iscsi-provisioner-class.yaml 
oc secret new-basicauth targetd-account --username=admin --password=ciao
oc create -f iscsi-provisioner-dc.yaml
oc create -f iscsi-provisioner-pvc.yaml
``` # install iscsi controller

```
export NS=default
kubectl apply -f iscsi-provisioner-class.yaml 
kubectl create secret generic targetd-account --from-literal=username=admin --from-literal=password=ciao -n $NS
kubectl apply -f iscsi-provisioner-d.yaml -n $NS
kubectl apply -f iscsi-provisioner-pvc.yaml -n $NS
``` # Glusterblock Volume Provisioner for Kubernetes 1.5+


[![Docker Repository on Quay](https://quay.io/repository/external_storage/glusterblock-provisioner/status "Docker Repository on Quay")](https://quay.io/repository/external_storage/glusterblock-provisioner)
```
quay.io/external_storage/glusterblock-provisioner:latest
```

[TOC]

## What is Gluster Block Provisioner ?

Gluster Block Provisioner is an external provisioner which dynamically provision gluster block volumes ( ISCSI volumes ) on demand. The persistent Volume Claim which has been requested with this external provisioner's identity ( for eg# `gluster.org/glusterblock`)  will be served by this provisioner. This provisioner is capable of operating on couple of modes ( `gluster-block` and `heketi`).

`gluster-block` mode :  This is an experimental or test mode on which the provisioner will directly talk to `gluster-block` utility or command line interface of gluster-block. 

`heketi` mode : This is the recommended/supported mode on which the provisioner will talk to `heketi's` Block API to provision gluster block volumes.  

Additional Reference:
[gluster-block](https://github.com/gluster/gluster-block)
[heketi](https://github.com/heketi/heketi)
[gluster-kubernetes](https://github.com/gluster/gluster-kubernetes)


## Build Gluster Block Provisioner and container image

If you want to build the container from source instead of pulling the docker image, please follow below steps:

 Step 1: Build the provisioner binary
```
[root@localhost]# go build glusterblock-provisioner.go
```

Step 2:  Build docker container image
```
[root@localhost]# docker build -t glusterblock-provisioner .
```

## Start Kubernetes Cluster

## Start glusterblock provisioner

The following example uses `gluster.org/glusterblock` as the identity for the instance and assumes kubeconfig is at `/root/.kube`. The identity should remain the same if the provisioner restarts. If there are multiple provisioners, each should have a different identity.

```
[root@localhost] docker run -ti -v /root/.kube:/kube -v /var/run/kubernetes:/var/run/kubernetes --privileged --net=host  glusterblock-provisioner  -master=http://127.0.0.1:8080 -kubeconfig=/kube/config -id=gluster.org/glusterblock
```


## Create a glusterblock Storage Class

```
[root@localhost] kubectl create -f glusterblock-class.yaml
```

The available storage class parameter are listed below:

```yaml

parameters:
    resturl: "http://127.0.0.1:8081"
    restuser: "admin"
    restsecretnamespace: "default"
    restsecretname: "heketi-secret"
    hacount: "3"
    chapauthenabled: "true"
    opmode: "gluster-block"
    blockmodeargs: "glustervol=blockmaster1,hosts=10.67.116.108"

```


### Global parameters applicable for both modes:

* `opmode`: This value decide in which mode gluster block provisioner has to work.

* `chapauthenabled`: This value has to be set to `true` if we want to provision block volume with CHAP authentication enabled. This is an optional parameter.

* `hacount`: This is the count of number of paths to the block target server. This provide high availability via multipathing capability of iscsi. If there is a path failure, the I/Os will not be disturbed and will be served via another available paths.


### Heketi Mode Parameters:

If provisioner want to operate on `heketi` mode, below args can be  filled in storageclass accordingly.

* `resturl` : Gluster REST service/Heketi service url which provision gluster block volumes on demand. The general format should be `IPaddress:Port` and this is a mandatory parameter for GlusterFS dynamic provisioner. If Heketi service is exposed as a routable service in openshift/kubernetes setup, this can have a format similar to
`http://heketi-storage-project.cloudapps.mystorage.com` where the fqdn is a resolvable heketi service url.

* `restuser` : Gluster REST service/Heketi user who has access to create volumes in the Gluster Trusted Pool.

* `restsecretnamespace` + `restsecretname` : Identification of Secret instance that contains user password to use when talking to Gluster REST service. These parameters are optional, empty password will be used when both `restsecretnamespace` and `restsecretname` are omitted. The provided secret must have type "gluster.org/glusterblock".


### Gluster-Block Mode parameters:

If provisioner want to operate on `gluster-block`, below args are required to be filled in storageclass.

* `blockmodeargs`:

This mode requires `glustervol` name and `hosts` to be mentioned in `,` seperated values as shown below. This is a mandatory parameter to be filled
in storage class parameter.

```
"glustervol=blockmaster1,hosts=10.67.116.108"
```

## How to test:

### Create a claim

```
[root@localhost]# kubectl create -f glusterblock-claim1.yaml
persistentvolumeclaim "claim1" created

[root@localhost]# kubectl get pvc
NAME      STATUS    VOLUME                                     CAPACITY   ACCESSMODES   STORAGECLASS   AGE
claim1    Bound     pvc-b7045edf-3a26-11e7-af53-c85b7636c232   1Gi        RWX           glusterblock   56s
[root@localhost]# kubectl get pv
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM            STORAGECLASS   REASON    AGE
pvc-b7045edf-3a26-11e7-af53-c85b7636c232   1Gi        RWX           Delete          Bound     default/claim1   glusterblock             46s

[root@localhost]# kubectl get pvc,pv
NAME         STATUS    VOLUME                                     CAPACITY   ACCESSMODES   STORAGECLASS   AGE
pvc/claim1   Bound     pvc-b7045edf-3a26-11e7-af53-c85b7636c232   1Gi        RWX           glusterblock   1m

NAME                                          CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM            STORAGECLASS   REASON    AGE
pv/pvc-b7045edf-3a26-11e7-af53-c85b7636c232   1Gi        RWX           Delete          Bound     default/claim1   glusterblock             1m
```

# GlusterFS Simple Provisioner for Kubernetes 1.5+

GlusterFS simple provisioner is an external provisioner which
dynamically provision glusterfs volumes on demand.

Unlike [Heketi][1], this provisioner will not manage GlusterFS cluster.
So that you must manage GlusterFS cluster by yourself. This will simply
create Gluster volume in the specified GlusterFS cluster like nfs-client
provisioner.

It means, for example, if you want to add brick to your Gluster volume,
you can use familiar `gluster vol add-brick` command.

[1]: https://github.com/heketi/heketi

## Build GlusterFS Simple Provisioner and container image

```bash
[root@localhost]# make container
```

## Start Kubernetes local cluster

## Start GlusterFS cluster on Kubernetes

GlusterFS Simple Provisioner requires Gluster cluster which is running on the top of Kubernetes cluster.

```bash
[root@localhost]# kubectl create -f deploy/glusterfs-daemonset.yaml
[root@localhost]# kubectl label node <...node...> storagenode=glusterfs
```
### Configure the GlusterFS trusted pool

GlusterFS Simple Provisioner will not manage GlusterFS cluster at all, so it is needed to manage GlusterFS cluster by yourself.

Check GlusterFS node's `podIP`s.

```bash
[root@localhost]# kubectl get pods -o wide --selector=glusterfs-node=pod
NAME              READY     STATUS    RESTARTS   AGE       IP             NODE
glusterfs-grck0   1/1       Running   0          11m       172.16.2.132   worker02
glusterfs-mgmnd   1/1       Running   0          11m       172.16.2.131   worker01
```

And add nodes to trusted pool

```bash
[root@localhost]# kubectl exec -ti glusterfs-grck0 gluster peer probe 172.16.2.131
[root@localhost]# kubectl exec -ti glusterfs-mgmnd gluster peer probe 172.16.2.132
```

## Start glusterfs simple provisioner

The following example assumes kubeconfig is at `/root/.kube`.

```bash
docker run -ti \
           -v /root/.kube:/kube \
           -v /var/run/kubernetes:/var/run/kubernetes \
           external_storage/glusterfs-simple-provisioner \
              -kubeconfig=/kube/config
```

## Create a glusterfs-simple Storage Class

```bash
echo 'kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: glusterfs-simple
provisioner: gluster.org/glusterfs-simple
parameters:
  forceCreate: "true"
  brickrootPaths: "172.16.2.131:/tmp/,172.16.2.132:/tmp"' | kubectl create -f -
```

The available storage class parameter are listed below:

```yaml

parameters:
    brickRootPaths: "172.16.2.131:/tmp/,172.16.2.132:/tmp"
    volumeType: "replica 2"
    namespace: "default"
    selector: "glusterfs-node==pod"
    forceCreate: "true"
```

* `brickRootPaths`: Bricks will be created under this directories.
* `volumeType`: Storage class will create this type of volume.
* `namespace`: Namespace which GlusterFS pods are consisted.
* `selector`: Label selector which will specify GlusterFS pods.
* `forceCreate`: If true, glusterd create volume forcefully.

# RBD Volume Provisioner for Kubernetes 1.5+

`rbd-provisioner` is an out-of-tree dynamic provisioner for Kubernetes 1.5+.
You can use it quickly & easily deploy ceph RBD storage that works almost
anywhere. 

It works just like in-tree dynamic provisioner. For more information on how
dynamic provisioning works, see [the docs](http://kubernetes.io/docs/user-guide/persistent-volumes/)
or [this blog post](http://blog.kubernetes.io/2016/10/dynamic-provisioning-and-storage-in-kubernetes.html).

## Test instruction

Compile the provisioner
``` console
make
```

Make the container image and push to the registry
``` console
make push
```

* Start Kubernetes local cluster

* Create a Ceph admin secret

```bash
ceph auth get client.admin 2>&1 |grep "key = " |awk '{print  $3'} |xargs echo -n > /tmp/secret
kubectl create secret generic ceph-admin-secret --from-file=/tmp/secret --namespace=kube-system
```

* Create a Ceph pool and a user secret

```bash
ceph osd pool create kube 8 8
ceph auth add client.kube mon 'allow r' osd 'allow rwx pool=kube'
ceph auth get client.kube 2>&1 |grep "key = " |awk '{print  $3'} |xargs echo -n > /tmp/secret
kubectl create secret generic ceph-secret --from-file=/tmp/secret --namespace=default
```

* Start RBD provisioner

The following example uses `rbd-provisioner-1` as the identity for the instance and assumes kubeconfig is at `/root/.kube`. The identity should remain the same if the provisioner restarts. If there are multiple provisioners, each should have a different identity.

```bash
docker run -ti -v /root/.kube:/kube -v /var/run/kubernetes:/var/run/kubernetes --privileged --net=host rbd-provisioner /usr/local/bin/rbd-provisioner -master=http://127.0.0.1:8080 -kubeconfig=/kube/config -id=rbd-provisioner-1
```

Alternatively, start a deployment:

```bash
kubectl create -f deployment.yaml
```

* Create a RBD Storage Class

Replace Ceph monitor's IP in [class.yaml](class.yaml) with your own and create storage class:

```bash
kubectl create -f class.yaml
```

* Create a claim

```bash
kubectl create -f claim.yaml
```

* Create a Pod using the claim

```bash
kubectl create -f test-pod.yaml
```

# Acknowledgements

- This provisioner is extracted from [Kubernetes core](https://github.com/kubernetes/kubernetes) with some modifications for this project.
# CephFS Volume Provisioner for Kubernetes 1.5+

[![Docker Repository on Quay](https://quay.io/repository/external_storage/cephfs-provisioner/status "Docker Repository on Quay")](https://quay.io/repository/external_storage/cephfs-provisioner)

Using Ceph volume client

# Test instruction

Compile the provisioner
``` console
make
```

Make the container image and push to the registry
``` console
make push
```

* Start Kubernetes local cluster

* Create a Ceph admin secret

```bash
ceph auth get client.admin 2>&1 |grep "key = " |awk '{print  $3'} |xargs echo -n > /tmp/secret
kubectl create secret generic ceph-secret-admin --from-file=/tmp/secret --namespace=kube-system
```

* Start CephFS provisioner

The following example uses `cephfs-provisioner-1` as the identity for the instance and assumes kubeconfig is at `/root/.kube`. The identity should remain the same if the provisioner restarts. If there are multiple provisioners, each should have a different identity.

```bash
docker run -ti -v /root/.kube:/kube -v /var/run/kubernetes:/var/run/kubernetes --privileged --net=host  cephfs-provisioner /usr/local/bin/cephfs-provisioner -master=http://127.0.0.1:8080 -kubeconfig=/kube/config -id=cephfs-provisioner-1
```
Alternatively, start a deployment:

```bash
kubectl create -f deployment.yaml
```

* Create a CephFS Storage Class

Replace Ceph monitor's IP in [class.yaml](class.yaml) with your own and create storage class:

```bash
kubectl create -f class.yaml
```

* Create a claim

```bash
kubectl create -f claim.yaml
```

* Create a Pod using the claim

```bash
kubectl create -f test-pod.yaml
```


# Known limitations

* Kernel CephFS doesn't work with SELinux, setting SELinux label in Pod's securityContext will not work.
* Kernel CephFS doesn't support quota or capacity, capacity requested by PVC is not enforced or validated.
* Currently each Ceph user created by the provisioner has `allow r` MDS cap to permit CephFS mount.

# Acknowledgement
Inspired by CephFS Manila provisioner and conversation with John Spray
urlesc [![Build Status](https://travis-ci.org/PuerkitoBio/urlesc.png?branch=master)](https://travis-ci.org/PuerkitoBio/urlesc) [![GoDoc](http://godoc.org/github.com/PuerkitoBio/urlesc?status.svg)](http://godoc.org/github.com/PuerkitoBio/urlesc)
======

Package urlesc implements query escaping as per RFC 3986.

It contains some parts of the net/url package, modified so as to allow
some reserved characters incorrectly escaped by net/url (see [issue 5684](https://github.com/golang/go/issues/5684)).

## Install

    go get github.com/PuerkitoBio/urlesc

## License

Go license (BSD-3-Clause)

# Purell

Purell is a tiny Go library to normalize URLs. It returns a pure URL. Pure-ell. Sanitizer and all. Yeah, I know...

Based on the [wikipedia paper][wiki] and the [RFC 3986 document][rfc].

[![build status](https://secure.travis-ci.org/PuerkitoBio/purell.png)](http://travis-ci.org/PuerkitoBio/purell)

## Install

`go get github.com/PuerkitoBio/purell`

## Changelog

*    **2016-07-27 (v1.0.0)** : Normalize IDN to ASCII (thanks to @zenovich).
*    **2015-02-08** : Add fix for relative paths issue ([PR #5][pr5]) and add fix for unnecessary encoding of reserved characters ([see issue #7][iss7]).
*    **v0.2.0** : Add benchmarks, Attempt IDN support.
*    **v0.1.0** : Initial release.

## Examples

From `example_test.go` (note that in your code, you would import "github.com/PuerkitoBio/purell", and would prefix references to its methods and constants with "purell."):

```go
package purell

import (
  "fmt"
  "net/url"
)

func ExampleNormalizeURLString() {
  if normalized, err := NormalizeURLString("hTTp://someWEBsite.com:80/Amazing%3f/url/",
    FlagLowercaseScheme|FlagLowercaseHost|FlagUppercaseEscapes); err != nil {
    panic(err)
  } else {
    fmt.Print(normalized)
  }
  // Output: http://somewebsite.com:80/Amazing%3F/url/
}

func ExampleMustNormalizeURLString() {
  normalized := MustNormalizeURLString("hTTpS://someWEBsite.com:443/Amazing%fa/url/",
    FlagsUnsafeGreedy)
  fmt.Print(normalized)

  // Output: http://somewebsite.com/Amazing%FA/url
}

func ExampleNormalizeURL() {
  if u, err := url.Parse("Http://SomeUrl.com:8080/a/b/.././c///g?c=3&a=1&b=9&c=0#target"); err != nil {
    panic(err)
  } else {
    normalized := NormalizeURL(u, FlagsUsuallySafeGreedy|FlagRemoveDuplicateSlashes|FlagRemoveFragment)
    fmt.Print(normalized)
  }

  // Output: http://someurl.com:8080/a/c/g?c=3&a=1&b=9&c=0
}
```

## API

As seen in the examples above, purell offers three methods, `NormalizeURLString(string, NormalizationFlags) (string, error)`, `MustNormalizeURLString(string, NormalizationFlags) (string)` and `NormalizeURL(*url.URL, NormalizationFlags) (string)`. They all normalize the provided URL based on the specified flags. Here are the available flags:

```go
const (
	// Safe normalizations
	FlagLowercaseScheme           NormalizationFlags = 1 << iota // HTTP://host -> http://host, applied by default in Go1.1
	FlagLowercaseHost                                            // http://HOST -> http://host
	FlagUppercaseEscapes                                         // http://host/t%ef -> http://host/t%EF
	FlagDecodeUnnecessaryEscapes                                 // http://host/t%41 -> http://host/tA
	FlagEncodeNecessaryEscapes                                   // http://host/!"#$ -> http://host/%21%22#$
	FlagRemoveDefaultPort                                        // http://host:80 -> http://host
	FlagRemoveEmptyQuerySeparator                                // http://host/path? -> http://host/path

	// Usually safe normalizations
	FlagRemoveTrailingSlash // http://host/path/ -> http://host/path
	FlagAddTrailingSlash    // http://host/path -> http://host/path/ (should choose only one of these add/remove trailing slash flags)
	FlagRemoveDotSegments   // http://host/path/./a/b/../c -> http://host/path/a/c

	// Unsafe normalizations
	FlagRemoveDirectoryIndex   // http://host/path/index.html -> http://host/path/
	FlagRemoveFragment         // http://host/path#fragment -> http://host/path
	FlagForceHTTP              // https://host -> http://host
	FlagRemoveDuplicateSlashes // http://host/path//a///b -> http://host/path/a/b
	FlagRemoveWWW              // http://www.host/ -> http://host/
	FlagAddWWW                 // http://host/ -> http://www.host/ (should choose only one of these add/remove WWW flags)
	FlagSortQuery              // http://host/path?c=3&b=2&a=1&b=1 -> http://host/path?a=1&b=1&b=2&c=3

	// Normalizations not in the wikipedia article, required to cover tests cases
	// submitted by jehiah
	FlagDecodeDWORDHost           // http://1113982867 -> http://66.102.7.147
	FlagDecodeOctalHost           // http://0102.0146.07.0223 -> http://66.102.7.147
	FlagDecodeHexHost             // http://0x42660793 -> http://66.102.7.147
	FlagRemoveUnnecessaryHostDots // http://.host../path -> http://host/path
	FlagRemoveEmptyPortSeparator  // http://host:/path -> http://host/path

	// Convenience set of safe normalizations
	FlagsSafe NormalizationFlags = FlagLowercaseHost | FlagLowercaseScheme | FlagUppercaseEscapes | FlagDecodeUnnecessaryEscapes | FlagEncodeNecessaryEscapes | FlagRemoveDefaultPort | FlagRemoveEmptyQuerySeparator

	// For convenience sets, "greedy" uses the "remove trailing slash" and "remove www. prefix" flags,
	// while "non-greedy" uses the "add (or keep) the trailing slash" and "add www. prefix".

	// Convenience set of usually safe normalizations (includes FlagsSafe)
	FlagsUsuallySafeGreedy    NormalizationFlags = FlagsSafe | FlagRemoveTrailingSlash | FlagRemoveDotSegments
	FlagsUsuallySafeNonGreedy NormalizationFlags = FlagsSafe | FlagAddTrailingSlash | FlagRemoveDotSegments

	// Convenience set of unsafe normalizations (includes FlagsUsuallySafe)
	FlagsUnsafeGreedy    NormalizationFlags = FlagsUsuallySafeGreedy | FlagRemoveDirectoryIndex | FlagRemoveFragment | FlagForceHTTP | FlagRemoveDuplicateSlashes | FlagRemoveWWW | FlagSortQuery
	FlagsUnsafeNonGreedy NormalizationFlags = FlagsUsuallySafeNonGreedy | FlagRemoveDirectoryIndex | FlagRemoveFragment | FlagForceHTTP | FlagRemoveDuplicateSlashes | FlagAddWWW | FlagSortQuery

	// Convenience set of all available flags
	FlagsAllGreedy    = FlagsUnsafeGreedy | FlagDecodeDWORDHost | FlagDecodeOctalHost | FlagDecodeHexHost | FlagRemoveUnnecessaryHostDots | FlagRemoveEmptyPortSeparator
	FlagsAllNonGreedy = FlagsUnsafeNonGreedy | FlagDecodeDWORDHost | FlagDecodeOctalHost | FlagDecodeHexHost | FlagRemoveUnnecessaryHostDots | FlagRemoveEmptyPortSeparator
)
```

For convenience, the set of flags `FlagsSafe`, `FlagsUsuallySafe[Greedy|NonGreedy]`, `FlagsUnsafe[Greedy|NonGreedy]` and `FlagsAll[Greedy|NonGreedy]` are provided for the similarly grouped normalizations on [wikipedia's URL normalization page][wiki]. You can add (using the bitwise OR `|` operator) or remove (using the bitwise AND NOT `&^` operator) individual flags from the sets if required, to build your own custom set.

The [full godoc reference is available on gopkgdoc][godoc].

Some things to note:

*    `FlagDecodeUnnecessaryEscapes`, `FlagEncodeNecessaryEscapes`, `FlagUppercaseEscapes` and `FlagRemoveEmptyQuerySeparator` are always implicitly set, because internally, the URL string is parsed as an URL object, which automatically decodes unnecessary escapes, uppercases and encodes necessary ones, and removes empty query separators (an unnecessary `?` at the end of the url). So this operation cannot **not** be done. For this reason, `FlagRemoveEmptyQuerySeparator` (as well as the other three) has been included in the `FlagsSafe` convenience set, instead of `FlagsUnsafe`, where Wikipedia puts it.

*    The `FlagDecodeUnnecessaryEscapes` decodes the following escapes (*from -> to*):
    -    %24 -> $
    -    %26 -> &
    -    %2B-%3B -> +,-./0123456789:;
    -    %3D -> =
    -    %40-%5A -> @ABCDEFGHIJKLMNOPQRSTUVWXYZ
    -    %5F -> _
    -    %61-%7A -> abcdefghijklmnopqrstuvwxyz
    -    %7E -> ~


*    When the `NormalizeURL` function is used (passing an URL object), this source URL object is modified (that is, after the call, the URL object will be modified to reflect the normalization).

*    The *replace IP with domain name* normalization (`http://208.77.188.166/ → http://www.example.com/`) is obviously not possible for a library without making some network requests. This is not implemented in purell.

*    The *remove unused query string parameters* and *remove default query parameters* are also not implemented, since this is a very case-specific normalization, and it is quite trivial to do with an URL object.

### Safe vs Usually Safe vs Unsafe

Purell allows you to control the level of risk you take while normalizing an URL. You can aggressively normalize, play it totally safe, or anything in between.

Consider the following URL:

`HTTPS://www.RooT.com/toto/t%45%1f///a/./b/../c/?z=3&w=2&a=4&w=1#invalid`

Normalizing with the `FlagsSafe` gives:

`https://www.root.com/toto/tE%1F///a/./b/../c/?z=3&w=2&a=4&w=1#invalid`

With the `FlagsUsuallySafeGreedy`:

`https://www.root.com/toto/tE%1F///a/c?z=3&w=2&a=4&w=1#invalid`

And with `FlagsUnsafeGreedy`:

`http://root.com/toto/tE%1F/a/c?a=4&w=1&w=2&z=3`

## TODOs

*    Add a class/default instance to allow specifying custom directory index names? At the moment, removing directory index removes `(^|/)((?:default|index)\.\w{1,4})$`.

## Thanks / Contributions

@rogpeppe
@jehiah
@opennota
@pchristopher1275
@zenovich

## License

The [BSD 3-Clause license][bsd].

[bsd]: http://opensource.org/licenses/BSD-3-Clause
[wiki]: http://en.wikipedia.org/wiki/URL_normalization
[rfc]: http://tools.ietf.org/html/rfc3986#section-6
[godoc]: http://go.pkgdoc.org/github.com/PuerkitoBio/purell
[pr5]: https://github.com/PuerkitoBio/purell/pull/5
[iss7]: https://github.com/PuerkitoBio/purell/issues/7
# easyjson [![Build Status](https://travis-ci.org/mailru/easyjson.svg?branch=master)](https://travis-ci.org/mailru/easyjson)

easyjson allows to (un-)marshal JSON golang structs without the use of reflection by generating marshaller code.  

One of the aims of the library is to keep generated code simple enough so that it can be easily optimized or fixed. Another goal is to provide users with ability to customize the generated code not available in 'encoding/json', such as generating snake_case names or enabling 'omitempty' behavior by default.

## usage
```
go get github.com/mailru/easyjson/...
easyjson -all <file>.go
```

This will generate `<file>_easyjson.go` with marshaller/unmarshaller methods for structs. `GOPATH` variable needs to be set up correctly, since the generation invokes a `go run` on a temporary file (this is a really convenient approach to code generation borrowed from https://github.com/pquerna/ffjson).

## options
```
Usage of .root/bin/easyjson:
  -all
        generate un-/marshallers for all structs in a file
  -build_tags string
        build tags to add to generated file
  -leave_temps
        do not delete temporary files
  -no_std_marshalers
        don't generate MarshalJSON/UnmarshalJSON methods
  -noformat
        do not run 'gofmt -w' on output file
  -omit_empty
        omit empty fields by default
  -snake_case
        use snake_case names instead of CamelCase by default
  -stubs
        only generate stubs for marshallers/unmarshallers methods
```

Using `-all` will generate (un-)marshallers for all structs in the file. By default, structs need to have a line beginning with `easyjson:json` in their docstring, e.g.:
```
//easyjson:json
struct A{}
```

`-snake_case` tells easyjson to generate snake\_case field names by default (unless explicitly overriden by a field tag). The CamelCase to snake\_case conversion algorithm should work in most cases (e.g. HTTPVersion will be converted to http_version). There can be names like JSONHTTPRPC where the conversion will return an unexpected result (jsonhttprpc without underscores),  but such names require a dictionary to do the conversion and may be ambiguous.

`-build_tags` will add corresponding build tag line for the generated file.
## marshaller/unmarshaller interfaces

easyjson generates MarshalJSON/UnmarshalJSON methods that are compatible with interfaces from 'encoding/json'. They are usable with 'json.Marshal' and 'json.Unmarshal' functions, however actually using those will result in significantly worse performance compared to custom interfaces.

`MarshalEasyJSON` / `UnmarshalEasyJSON` methods are generated for faster parsing using custom Lexer/Writer structs (`jlexer.Lexer`  and  `jwriter.Writer`). The method signature is defined in `easyjson.Marshaler` / `easyjson.Unmarshaler` interfaces. These interfaces allow to avoid using any unnecessary reflection or type assertions during parsing. Functions can be used manually or with `easyjson.Marshal<...>` and `easyjson.Unmarshal<...>` helper methods. 

`jwriter.Writer` struct in addition to function for returning the data as a single slice also has methods to return the size and to send the data to an `io.Writer`. This is aimed at a typical HTTP use-case, when you want to know the `Content-Length` before actually starting to send the data.

There are helpers in the top-level package for marhsaling/unmarshaling the data using custom interfaces to and from writers, including a helper for `http.ResponseWriter`.

## custom types
If `easyjson.Marshaler` / `easyjson.Unmarshaler` interfaces are implemented by a type involved in JSON parsing, the type will be marshaled/unmarshaled using these methods.  `easyjson.Optional` interface allows for a custom type to integrate with 'omitempty' logic. 

As an example, easyjson includes an `easyjson.RawMessage` analogous to `json.RawMessage`.

Also, there are 'optional' wrappers for primitive types in `easyjson/opt` package. These are useful in the case when it is necessary to distinguish between missing and default value for the type. Wrappers allow to avoid pointers and extra heap allocations in such cases.
 
## memory pooling

The library uses a custom buffer which allocates data in increasing chunks (128-32768 bytes). Chunks of 512 bytes and larger are reused with the help of `sync.Pool`. The maximum size of a chunk is bounded to reduce redundancy in memory allocation and to make the chunks more reusable in the case of large buffer sizes.

The buffer code is in `easyjson/buffer` package the exact values can be tweaked by a `buffer.Init()` call before the first serialization.

## limitations
* The library is at an early stage, there are likely to be some bugs and some features of 'encoding/json' may not be supported. Please report such cases, so that they may be fixed sooner.
* Object keys are case-sensitive (unlike encodin/json). Case-insentive behavior will be implemented as an option (case-insensitive matching is slower).
* Unsafe package is used by the code. While a non-unsafe version of easyjson can be made in the future, using unsafe package simplifies a lot of code by allowing no-copy []byte to string conversion within the library. This is used only during parsing and all the returned values are allocated properly.
* Floats are currently formatted with default precision for 'strconv' package. It is obvious that it is not always the correct way to handle it, but there aren't enough use-cases for floats at hand to do anything better.
* During parsing, parts of JSON that are skipped over are not syntactically validated more than required to skip matching parentheses.
* No true streaming support for encoding/decoding. For many use-cases and protocols, data length is typically known on input and needs to be known before sending the data.

## benchmarks
Most benchmarks were done using a sample 13kB JSON (9k if serialized back trimming the whitespace) from https://dev.twitter.com/rest/reference/get/search/tweets. The sample is very close to real-world data, quite structured and contains a variety of different types.

For small request benchmarks, an 80-byte portion of the regular sample was used.

For large request marshalling benchmarks, a struct containing 50 regular samples was used, making a ~500kB output JSON.

Benchmarks are available in the repository and are run on 'make'.

### easyjson vs. encoding/json

easyjson seems to be 5-6 times faster than the default json serialization for unmarshalling, 3-4 times faster for non-concurrent marshalling. Concurrent marshalling is 6-7x faster if marshalling to a writer.

### easyjson vs. ffjson

easyjson uses the same approach for code generation as ffjson, but a significantly different approach to lexing and generated code. This allows easyjson to be 2-3x faster for unmarshalling and 1.5-2x faster for non-concurrent unmarshalling. 

ffjson seems to behave weird if used concurrently: for large request pooling hurts performance instead of boosting it, it also does not quite scale well. These issues are likely to be fixable and until that comparisons might vary from version to version a lot.

easyjson is similar in performance for small requests and 2-5x times faster for large ones if used with a writer.

### easyjson vs. go/codec

github.com/ugorji/go/codec library provides compile-time helpers for JSON generation. In this case, helpers are not exactly marshallers as they are encoding-independent.

easyjson is generally ~2x faster for non-concurrent benchmarks and about 3x faster for concurrent encoding (without marshalling to a writer). Unsafe option for generated helpers was used.

As an attempt to measure marshalling performance of 'go/codec' (as opposed to allocations/memcpy/writer interface invocations), a benchmark was done with resetting lenght of a byte slice rather than resetting the whole slice to nil. However, the optimization in this exact form may not be applicable in practice, since the memory is not freed between marshalling operations.

### easyjson vs 'ujson' python module
ujson is using C code for parsing, so it is interesting to see how plain golang compares to that. It is imporant to note that the resulting object for python is slower to access, since the library parses JSON object into dictionaries.

easyjson seems to be slightly faster for unmarshalling (finally!) and 2-3x faster for marshalling.

### benchmark figures
The data was measured on 4 February, 2016 using current ffjson and golang 1.6. Data for go/codec was added on 4 March 2016, benchmarked on the same machine.

#### Unmarshalling
| lib    | json size | MB/s | allocs/op | B/op
|--------|-----------|------|-----------|-------
|standard| regular   | 22   | 218       | 10229
|standard| small     | 9.7  | 14        | 720
|--------|-----------|------|-----------|-------
|easyjson| regular   | 125  | 128       | 9794
|easyjson| small     | 67   | 3         | 128
|--------|-----------|------|-----------|-------
|ffjson  | regular   | 66   | 141       | 9985
|ffjson  | small     | 17.6 | 10        | 488
|--------|-----------|------|-----------|-------
|codec   | regular   | 55   | 434       | 19299
|codec   | small     | 29   | 7         | 336
|--------|-----------|------|-----------|-------
|ujson   | regular   | 103  | N/A       | N/A

#### Marshalling, one goroutine.
| lib      | json size | MB/s | allocs/op | B/op
|----------|-----------|------|-----------|-------
|standard  | regular   | 75   | 9         | 23256
|standard  | small     | 32   | 3         | 328
|standard  | large     | 80   | 17        | 1.2M
|----------|-----------|------|-----------|-------
|easyjson  | regular   | 213  | 9         | 10260
|easyjson* | regular   | 263  | 8         | 742
|easyjson  | small     | 125  | 1         | 128
|easyjson  | large     | 212  | 33        | 490k
|easyjson* | large     | 262  | 25        | 2879
|----------|-----------|------|-----------|-------
|ffjson    | regular   | 122  | 153       | 21340
|ffjson**  | regular   | 146  | 152       | 4897
|ffjson    | small     | 36   | 5         | 384
|ffjson**  | small     | 64   | 4         | 128
|ffjson    | large     | 134  | 7317      | 818k
|ffjson**  | large     | 125  | 7320      | 827k
|----------|-----------|------|-----------|-------
|codec     | regular   | 80   | 17        | 33601
|codec***  | regular   | 108  | 9         | 1153
|codec     | small     | 42   | 3         | 304
|codec***  | small     | 56   | 1         | 48
|codec     | large     | 73   | 483       | 2.5M
|codec***  | large     | 103  | 451       | 66007
|----------|-----------|------|-----------|-------
|ujson     | regular   | 92   | N/A       | N/A
\* marshalling to a writer,
\*\* using `ffjson.Pool()`,
\*\*\* reusing output slice instead of resetting it to nil

#### Marshalling, concurrent.
| lib      | json size | MB/s  | allocs/op | B/op
|----------|-----------|-------|-----------|-------
|standard  | regular   | 252   | 9         | 23257
|standard  | small     | 124   | 3         | 328
|standard  | large     | 289   | 17        | 1.2M
|----------|-----------|-------|-----------|-------
|easyjson  | regular   | 792   | 9         | 10597
|easyjson* | regular   | 1748  | 8         | 779
|easyjson  | small     | 333   | 1         | 128
|easyjson  | large     | 718   | 36        | 548k
|easyjson* | large     | 2134  | 25        | 4957
|----------|-----------|------|-----------|-------
|ffjson    | regular   | 301  | 153       | 21629
|ffjson**  | regular   | 707  | 152       | 5148
|ffjson    | small     | 62   | 5         | 384
|ffjson**  | small     | 282  | 4         | 128
|ffjson    | large     | 438  | 7330      | 1.0M
|ffjson**  | large     | 131  | 7319      | 820k
|----------|-----------|------|-----------|-------
|codec     | regular   | 183  | 17        | 33603
|codec***  | regular   | 671  | 9         | 1157
|codec     | small     | 147  | 3         | 304
|codec***  | small     | 299  | 1         | 48
|codec     | large     | 190  | 483       | 2.5M
|codec***  | large     | 752  | 451       | 77574
\* marshalling to a writer,
\*\* using `ffjson.Pool()`,
\*\*\* reusing output slice instead of resetting it to nil



# go/codec

This repository contains the `go-codec` library,
a High Performance and Feature-Rich Idiomatic encode/decode and rpc library for

  - msgpack: https://github.com/msgpack/msgpack
  - binc:    http://github.com/ugorji/binc
  - cbor:    http://cbor.io http://tools.ietf.org/html/rfc7049
  - json:    http://json.org http://tools.ietf.org/html/rfc7159 

For more information:

  - [see the codec/Readme for quick usage information](https://github.com/ugorji/go/tree/master/codec#readme)
  - [view the API on godoc](http://godoc.org/github.com/ugorji/go/codec)
  - [read the detailed usage/how-to primer](http://ugorji.net/blog/go-codec-primer)

Install using:

    go get github.com/ugorji/go/codec

# Codec

High Performance, Feature-Rich Idiomatic Go codec/encoding library for
binc, msgpack, cbor, json.

Supported Serialization formats are:

  - msgpack: https://github.com/msgpack/msgpack
  - binc:    http://github.com/ugorji/binc
  - cbor:    http://cbor.io http://tools.ietf.org/html/rfc7049
  - json:    http://json.org http://tools.ietf.org/html/rfc7159
  - simple: 

To install:

    go get github.com/ugorji/go/codec

This package understands the `unsafe` tag, to allow using unsafe semantics:

  - When decoding into a struct, you need to read the field name as a string 
    so you can find the struct field it is mapped to.
    Using `unsafe` will bypass the allocation and copying overhead of `[]byte->string` conversion.

To use it, you must pass the `unsafe` tag during install:

```
go install -tags=unsafe github.com/ugorji/go/codec 
```

Online documentation: http://godoc.org/github.com/ugorji/go/codec  
Detailed Usage/How-to Primer: http://ugorji.net/blog/go-codec-primer

The idiomatic Go support is as seen in other encoding packages in
the standard library (ie json, xml, gob, etc).

Rich Feature Set includes:

  - Simple but extremely powerful and feature-rich API
  - Very High Performance.
    Our extensive benchmarks show us outperforming Gob, Json, Bson, etc by 2-4X.
  - Multiple conversions:
    Package coerces types where appropriate 
    e.g. decode an int in the stream into a float, etc.
  - Corner Cases: 
    Overflows, nil maps/slices, nil values in streams are handled correctly
  - Standard field renaming via tags
  - Support for omitting empty fields during an encoding
  - Encoding from any value and decoding into pointer to any value
    (struct, slice, map, primitives, pointers, interface{}, etc)
  - Extensions to support efficient encoding/decoding of any named types
  - Support encoding.(Binary|Text)(M|Unm)arshaler interfaces
  - Decoding without a schema (into a interface{}).
    Includes Options to configure what specific map or slice type to use
    when decoding an encoded list or map into a nil interface{}
  - Encode a struct as an array, and decode struct from an array in the data stream
  - Comprehensive support for anonymous fields
  - Fast (no-reflection) encoding/decoding of common maps and slices
  - Code-generation for faster performance.
  - Support binary (e.g. messagepack, cbor) and text (e.g. json) formats
  - Support indefinite-length formats to enable true streaming 
    (for formats which support it e.g. json, cbor)
  - Support canonical encoding, where a value is ALWAYS encoded as same sequence of bytes.
    This mostly applies to maps, where iteration order is non-deterministic.
  - NIL in data stream decoded as zero value
  - Never silently skip data when decoding.
    User decides whether to return an error or silently skip data when keys or indexes
    in the data stream do not map to fields in the struct.
  - Encode/Decode from/to chan types (for iterative streaming support)
  - Drop-in replacement for encoding/json. `json:` key in struct tag supported.
  - Provides a RPC Server and Client Codec for net/rpc communication protocol.
  - Handle unique idiosyncrasies of codecs e.g. 
    - For messagepack, configure how ambiguities in handling raw bytes are resolved 
    - For messagepack, provide rpc server/client codec to support
      msgpack-rpc protocol defined at:
      https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md

## Extension Support

Users can register a function to handle the encoding or decoding of
their custom types.

There are no restrictions on what the custom type can be. Some examples:

    type BisSet   []int
    type BitSet64 uint64
    type UUID     string
    type MyStructWithUnexportedFields struct { a int; b bool; c []int; }
    type GifImage struct { ... }

As an illustration, MyStructWithUnexportedFields would normally be
encoded as an empty map because it has no exported fields, while UUID
would be encoded as a string. However, with extension support, you can
encode any of these however you like.

## RPC

RPC Client and Server Codecs are implemented, so the codecs can be used
with the standard net/rpc package.

## Usage

Typical usage model:

    // create and configure Handle
    var (
      bh codec.BincHandle
      mh codec.MsgpackHandle
      ch codec.CborHandle
    )

    mh.MapType = reflect.TypeOf(map[string]interface{}(nil))

    // configure extensions
    // e.g. for msgpack, define functions and enable Time support for tag 1
    // mh.SetExt(reflect.TypeOf(time.Time{}), 1, myExt)

    // create and use decoder/encoder
    var (
      r io.Reader
      w io.Writer
      b []byte
      h = &bh // or mh to use msgpack
    )

    dec = codec.NewDecoder(r, h)
    dec = codec.NewDecoderBytes(b, h)
    err = dec.Decode(&v)

    enc = codec.NewEncoder(w, h)
    enc = codec.NewEncoderBytes(&b, h)
    err = enc.Encode(v)

    //RPC Server
    go func() {
        for {
            conn, err := listener.Accept()
            rpcCodec := codec.GoRpc.ServerCodec(conn, h)
            //OR rpcCodec := codec.MsgpackSpecRpc.ServerCodec(conn, h)
            rpc.ServeCodec(rpcCodec)
        }
    }()

    //RPC Communication (client side)
    conn, err = net.Dial("tcp", "localhost:5555")
    rpcCodec := codec.GoRpc.ClientCodec(conn, h)
    //OR rpcCodec := codec.MsgpackSpecRpc.ClientCodec(conn, h)
    client := rpc.NewClientWithCodec(rpcCodec)

# codecgen tool

Generate is given a list of *.go files to parse, and an output file (fout),
codecgen will create an output file __file.go__ which
contains `codec.Selfer` implementations for the named types found
in the files parsed.

Using codecgen is very straightforward.

**Download and install the tool**

`go get -u github.com/ugorji/go/codec/codecgen`

**Run the tool on your files**

The command line format is:

`codecgen [options] (-o outfile) (infile ...)`

```sh
% codecgen -?
Usage of codecgen:
  -c="github.com/ugorji/go/codec": codec path
  -o="": out file
  -r=".*": regex for type name to match
  -nr="": regex for type name to exclude
  -rt="": tags for go run
  -t="": build tag to put in file
  -u=false: Use unsafe, e.g. to avoid unnecessary allocation on []byte->string
  -x=false: keep temp file

% codecgen -o values_codecgen.go values.go values2.go moretypedefs.go
```

Please see the [blog article](http://ugorji.net/blog/go-codecgen)
for more information on how to use the tool.

# Mergo

A helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.

Also a lovely [comune](http://en.wikipedia.org/wiki/Mergo) (municipality) in the Province of Ancona in the Italian region Marche.

![Mergo dall'alto](http://www.comune.mergo.an.it/Siti/Mergo/Immagini/Foto/mergo_dall_alto.jpg)

## Status

It is ready for production use. It works fine although it may use more of testing. Here some projects in the wild using Mergo:

- [EagerIO/Stout](https://github.com/EagerIO/Stout)
- [lynndylanhurley/defsynth-api](https://github.com/lynndylanhurley/defsynth-api)
- [russross/canvasassignments](https://github.com/russross/canvasassignments)
- [rdegges/cryptly-api](https://github.com/rdegges/cryptly-api)
- [casualjim/exeggutor](https://github.com/casualjim/exeggutor)
- [divshot/gitling](https://github.com/divshot/gitling)
- [RWJMurphy/gorl](https://github.com/RWJMurphy/gorl)

[![Build Status][1]][2]
[![GoDoc](https://godoc.org/github.com/imdario/mergo?status.svg)](https://godoc.org/github.com/imdario/mergo)

[1]: https://travis-ci.org/imdario/mergo.png
[2]: https://travis-ci.org/imdario/mergo

## Installation

    go get github.com/imdario/mergo

    // use in your .go code
    import (
        "github.com/imdario/mergo"
    )

## Usage

You can only merge same-type structs with exported fields initialized as zero value of their type and same-types maps. Mergo won't merge unexported (private) fields but will do recursively any exported one. Also maps will be merged recursively except for structs inside maps (because they are not addressable using Go reflection).

    if err := mergo.Merge(&dst, src); err != nil {
        // ...
    }

Additionally, you can map a map[string]interface{} to a struct (and otherwise, from struct to map), following the same restrictions as in Merge(). Keys are capitalized to find each corresponding exported field.

    if err := mergo.Map(&dst, srcMap); err != nil {
        // ...
    }

Warning: if you map a struct to map, it won't do it recursively. Don't expect Mergo to map struct members of your struct as map[string]interface{}. They will be just assigned as values.

More information and examples in [godoc documentation](http://godoc.org/github.com/imdario/mergo).

Note: if test are failing due missing package, please execute:

    go get gopkg.in/yaml.v1

## Contact me

If I can help you, you have an idea or you are using Mergo in your projects, don't hesitate to drop me a line (or a pull request): [@im_dario](https://twitter.com/im_dario)

## About

Written by [Dario Castañé](http://dario.im).

## License

[BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) license, as [Go language](http://golang.org/LICENSE).
[![GoDoc](https://godoc.org/github.com/pkg/xattr?status.svg)](http://godoc.org/github.com/pkg/xattr)
[![Go Report Card](https://goreportcard.com/badge/github.com/pkg/xattr)](https://goreportcard.com/report/github.com/pkg/xattr)
[![Build Status](https://travis-ci.org/pkg/xattr.svg?branch=master)](https://travis-ci.org/pkg/xattr)

xattr
=====
Extended attribute support for Go (linux + darwin + freebsd).

"Extended attributes are name:value pairs associated permanently with files and directories, similar to the environment strings associated with a process. An attribute may be defined or undefined. If it is defined, its value may be empty or non-empty." [See more...](https://en.wikipedia.org/wiki/Extended_file_attributes)


### Example
```
  const path = "/tmp/myfile"
  const prefix = "user."

  if err := xattr.Set(path, prefix+"test", []byte("test-attr-value")); err != nil {
  	log.Fatal(err)
  }
 
  var list []string
  if list, err = xattr.List(path); err != nil {
  	log.Fatal(err)
  }
  
  var data []byte
  if data, err = xattr.Get(path, prefix+"test"); err != nil {
  	log.Fatal(err)
  }

  if err = xattr.Remove(path, prefix+"test"); err != nil {
  	log.Fatal(err)
  }
```
# groupcache

## Summary

groupcache is a caching and cache-filling library, intended as a
replacement for memcached in many cases.

For API docs and examples, see http://godoc.org/github.com/golang/groupcache

## Comparison to memcached

### **Like memcached**, groupcache:

 * shards by key to select which peer is responsible for that key

### **Unlike memcached**, groupcache:

 * does not require running a separate set of servers, thus massively
   reducing deployment/configuration pain.  groupcache is a client
   library as well as a server.  It connects to its own peers.

 * comes with a cache filling mechanism.  Whereas memcached just says
   "Sorry, cache miss", often resulting in a thundering herd of
   database (or whatever) loads from an unbounded number of clients
   (which has resulted in several fun outages), groupcache coordinates
   cache fills such that only one load in one process of an entire
   replicated set of processes populates the cache, then multiplexes
   the loaded value to all callers.

 * does not support versioned values.  If key "foo" is value "bar",
   key "foo" must always be "bar".  There are neither cache expiration
   times, nor explicit cache evictions.  Thus there is also no CAS,
   nor Increment/Decrement.  This also means that groupcache....

 * ... supports automatic mirroring of super-hot items to multiple
   processes.  This prevents memcached hot spotting where a machine's
   CPU and/or NIC are overloaded by very popular keys/values.

 * is currently only available for Go.  It's very unlikely that I
   (bradfitz@) will port the code to any other language.

## Loading process

In a nutshell, a groupcache lookup of **Get("foo")** looks like:

(On machine #5 of a set of N machines running the same code)

 1. Is the value of "foo" in local memory because it's super hot?  If so, use it.

 2. Is the value of "foo" in local memory because peer #5 (the current
    peer) is the owner of it?  If so, use it.

 3. Amongst all the peers in my set of N, am I the owner of the key
    "foo"?  (e.g. does it consistent hash to 5?)  If so, load it.  If
    other callers come in, via the same process or via RPC requests
    from peers, they block waiting for the load to finish and get the
    same answer.  If not, RPC to the peer that's the owner and get
    the answer.  If the RPC fails, just load it locally (still with
    local dup suppression).

## Users

groupcache is in production use by dl.google.com (its original user),
parts of Blogger, parts of Google Code, parts of Google Fiber, parts
of Google production monitoring systems, etc.

## Presentations

See http://talks.golang.org/2013/oscon-dl.slide

## Help

Use the golang-nuts mailing list for any discussion or questions.
glog
====

Leveled execution logs for Go.

This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package
	http://code.google.com/p/google-glog

By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control over logging at the file level.

The comment from glog.go introduces the ideas:

	Package glog implements logging analogous to the Google-internal
	C++ INFO/ERROR/V setup.  It provides functions Info, Warning,
	Error, Fatal, plus formatting variants such as Infof. It
	also provides V-style logging controlled by the -v and
	-vmodule=file=2 flags.
	
	Basic examples:
	
		glog.Info("Prepare to repel boarders")
	
		glog.Fatalf("Initialization failed: %s", err)
	
	See the documentation for the V function for an explanation
	of these examples:
	
		if glog.V(2) {
			glog.Info("Starting transaction...")
		}
	
		glog.V(2).Infoln("Processed", nItems, "elements")


The repository contains an open source version of the log package
used inside Google. The master copy of the source lives inside
Google, not here. The code in this repo is for export only and is not itself
under development. Feature requests will be ignored.

Send bug reports to golang-nuts@googlegroups.com.
gofuzz
======

gofuzz is a library for populating go objects with random values.

[![GoDoc](https://godoc.org/github.com/google/gofuzz?status.png)](https://godoc.org/github.com/google/gofuzz)
[![Travis](https://travis-ci.org/google/gofuzz.svg?branch=master)](https://travis-ci.org/google/gofuzz)

This is useful for testing:

* Do your project's objects really serialize/unserialize correctly in all cases?
* Is there an incorrectly formatted object that will cause your project to panic?

Import with ```import "github.com/google/gofuzz"```

You can use it on single variables:
```go
f := fuzz.New()
var myInt int
f.Fuzz(&myInt) // myInt gets a random value.
```

You can use it on maps:
```go
f := fuzz.New().NilChance(0).NumElements(1, 1)
var myMap map[ComplexKeyType]string
f.Fuzz(&myMap) // myMap will have exactly one element.
```

Customize the chance of getting a nil pointer:
```go
f := fuzz.New().NilChance(.5)
var fancyStruct struct {
  A, B, C, D *string
}
f.Fuzz(&fancyStruct) // About half the pointers should be set.
```

You can even customize the randomization completely if needed:
```go
type MyEnum string
const (
        A MyEnum = "A"
        B MyEnum = "B"
)
type MyInfo struct {
        Type MyEnum
        AInfo *string
        BInfo *string
}

f := fuzz.New().NilChance(0).Funcs(
        func(e *MyInfo, c fuzz.Continue) {
                switch c.Intn(2) {
                case 0:
                        e.Type = A
                        c.Fuzz(&e.AInfo)
                case 1:
                        e.Type = B
                        c.Fuzz(&e.BInfo)
                }
        },
)

var myObject MyInfo
f.Fuzz(&myObject) // Type will correspond to whether A or B info is set.
```

See more examples in ```example_test.go```.

Happy testing!
go-restful
==========
package for building REST-style Web Services using Google Go

[![Build Status](https://travis-ci.org/emicklei/go-restful.png)](https://travis-ci.org/emicklei/go-restful)
[![Go Report Card](https://goreportcard.com/badge/github.com/emicklei/go-restful)](https://goreportcard.com/report/github.com/emicklei/go-restful)
[![GoDoc](https://godoc.org/github.com/emicklei/go-restful?status.svg)](https://godoc.org/github.com/emicklei/go-restful)

- [Code examples](https://github.com/emicklei/go-restful/tree/master/examples)

REST asks developers to use HTTP methods explicitly and in a way that's consistent with the protocol definition. This basic REST design principle establishes a one-to-one mapping between create, read, update, and delete (CRUD) operations and HTTP methods. According to this mapping:

- GET = Retrieve a representation of a resource
- POST = Create if you are sending content to the server to create a subordinate of the specified resource collection, using some server-side algorithm.
- PUT = Create if you are sending the full content of the specified resource (URI).
- PUT = Update if you are updating the full content of the specified resource.
- DELETE = Delete if you are requesting the server to delete the resource
- PATCH = Update partial content of a resource
- OPTIONS = Get information about the communication options for the request URI
    
### Example

```Go
ws := new(restful.WebService)
ws.
	Path("/users").
	Consumes(restful.MIME_XML, restful.MIME_JSON).
	Produces(restful.MIME_JSON, restful.MIME_XML)

ws.Route(ws.GET("/{user-id}").To(u.findUser).
	Doc("get a user").
	Param(ws.PathParameter("user-id", "identifier of the user").DataType("string")).
	Writes(User{}))		
...
	
func (u UserResource) findUser(request *restful.Request, response *restful.Response) {
	id := request.PathParameter("user-id")
	...
}
```
	
[Full API of a UserResource](https://github.com/emicklei/go-restful/tree/master/examples/restful-user-resource.go) 
		
### Features

- Routes for request &#8594; function mapping with path parameter (e.g. {id}) support
- Configurable router:
	- (default) Fast routing algorithm that allows static elements, regular expressions and dynamic parameters in the URL path (e.g. /meetings/{id} or /static/{subpath:*}
	- Routing algorithm after [JSR311](http://jsr311.java.net/nonav/releases/1.1/spec/spec.html) that is implemented using (but does **not** accept) regular expressions
- Request API for reading structs from JSON/XML and accesing parameters (path,query,header)
- Response API for writing structs to JSON/XML and setting headers
- Customizable encoding using EntityReaderWriter registration
- Filters for intercepting the request &#8594; response flow on Service or Route level
- Request-scoped variables using attributes
- Containers for WebServices on different HTTP endpoints
- Content encoding (gzip,deflate) of request and response payloads
- Automatic responses on OPTIONS (using a filter)
- Automatic CORS request handling (using a filter)
- API declaration for Swagger UI (see [go-restful-swagger12](https://github.com/emicklei/go-restful-swagger12),[go-restful-openapi](https://github.com/emicklei/go-restful-openapi))
- Panic recovery to produce HTTP 500, customizable using RecoverHandler(...)
- Route errors produce HTTP 404/405/406/415 errors, customizable using ServiceErrorHandler(...)
- Configurable (trace) logging
- Customizable gzip/deflate readers and writers using CompressorProvider registration
	
### Resources

- [Example posted on blog](http://ernestmicklei.com/2012/11/go-restful-first-working-example/)
- [Design explained on blog](http://ernestmicklei.com/2012/11/go-restful-api-design/)
- [sourcegraph](https://sourcegraph.com/github.com/emicklei/go-restful)
- [showcase: Mora - MongoDB REST Api server](https://github.com/emicklei/mora)

Type ```git shortlog -s``` for a full list of contributors.

© 2012 - 2017, http://ernestmicklei.com. MIT License. Contributions are welcome.# go-restful-swagger12

[![Build Status](https://travis-ci.org/emicklei/go-restful-swagger12.png)](https://travis-ci.org/emicklei/go-restful-swagger12)
[![GoDoc](https://godoc.org/github.com/emicklei/go-restful-swagger12?status.svg)](https://godoc.org/github.com/emicklei/go-restful-swagger12)

How to use Swagger UI with go-restful
=

Get the Swagger UI sources (version 1.2 only)

	git clone https://github.com/wordnik/swagger-ui.git
	
The project contains a "dist" folder.
Its contents has all the Swagger UI files you need.

The `index.html` has an `url` set to `http://petstore.swagger.wordnik.com/api/api-docs`.
You need to change that to match your WebService JSON endpoint  e.g. `http://localhost:8080/apidocs.json`

Now, you can install the Swagger WebService for serving the Swagger specification in JSON.

	config := swagger.Config{
		WebServices:    restful.RegisteredWebServices(),
		ApiPath:        "/apidocs.json",
		SwaggerPath:     "/apidocs/",
		SwaggerFilePath: "/Users/emicklei/Projects/swagger-ui/dist"}
	swagger.InstallSwaggerService(config)		
	
	
Documenting Structs
--

Currently there are 2 ways to document your structs in the go-restful Swagger.

###### By using struct tags
- Use tag "description" to annotate a struct field with a description to show in the UI
- Use tag "modelDescription" to annotate the struct itself with a description to show in the UI. The tag can be added in an field of the struct and in case that there are multiple definition, they will be appended with an empty line.

###### By using the SwaggerDoc method
Here is an example with an `Address` struct and the documentation for each of the fields. The `""` is a special entry for **documenting the struct itself**.

	type Address struct {
		Country  string `json:"country,omitempty"`
		PostCode int    `json:"postcode,omitempty"`
	}

	func (Address) SwaggerDoc() map[string]string {
		return map[string]string{
			"":         "Address doc",
			"country":  "Country doc",
			"postcode": "PostCode doc",
		}
	}

This example will generate a JSON like this

	{
		"Address": {
			"id": "Address",
			"description": "Address doc",
			"properties": {
				"country": {
				"type": "string",
				"description": "Country doc"
				},
				"postcode": {
				"type": "integer",
				"format": "int32",
				"description": "PostCode doc"
				}
			}
		}
	}

**Very Important Notes:**
- `SwaggerDoc()` is using a **NON-Pointer** receiver (e.g. func (Address) and not func (*Address))
- The returned map should use as key the name of the field as defined in the JSON parameter (e.g. `"postcode"` and not `"PostCode"`)

Notes
--
- The Nickname of an Operation is automatically set by finding the name of the function. You can override it using RouteBuilder.Operation(..) 
- The WebServices field of swagger.Config can be used to control which service you want to expose and document ; you can have multiple configs and therefore multiple endpoints.

© 2017, ernestmicklei.com.  MIT License. Contributions welcome.# getpasswd in Go [![GoDoc](https://godoc.org/github.com/howeyc/gopass?status.svg)](https://godoc.org/github.com/howeyc/gopass) [![Build Status](https://secure.travis-ci.org/howeyc/gopass.png?branch=master)](http://travis-ci.org/howeyc/gopass)

Retrieve password from user terminal or piped input without echo.

Verified on BSD, Linux, and Windows.

Example:
```go
package main

import "fmt"
import "github.com/howeyc/gopass"

func main() {
	fmt.Printf("Password: ")

	// Silent. For printing *'s use gopass.GetPasswdMasked()
	pass, err := gopass.GetPasswd()
	if err != nil {
		// Handle gopass.ErrInterrupted or getch() read error
	}

	// Do something with pass
}
```

Caution: Multi-byte characters not supported!
GoGoProtobuf http://github.com/gogo/protobuf extends 
GoProtobuf http://github.com/golang/protobuf

# Go support for Protocol Buffers

Google's data interchange format.
Copyright 2010 The Go Authors.
https://github.com/golang/protobuf

This package and the code it generates requires at least Go 1.4.

This software implements Go bindings for protocol buffers.  For
information about protocol buffers themselves, see
	https://developers.google.com/protocol-buffers/

## Installation ##

To use this software, you must:
- Install the standard C++ implementation of protocol buffers from
	https://developers.google.com/protocol-buffers/
- Of course, install the Go compiler and tools from
	https://golang.org/
  See
	https://golang.org/doc/install
  for details or, if you are using gccgo, follow the instructions at
	https://golang.org/doc/install/gccgo
- Grab the code from the repository and install the proto package.
  The simplest way is to run `go get -u github.com/golang/protobuf/{proto,protoc-gen-go}`.
  The compiler plugin, protoc-gen-go, will be installed in $GOBIN,
  defaulting to $GOPATH/bin.  It must be in your $PATH for the protocol
  compiler, protoc, to find it.

This software has two parts: a 'protocol compiler plugin' that
generates Go source files that, once compiled, can access and manage
protocol buffers; and a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers.

There is support for gRPC in Go using protocol buffers.
See the note at the bottom of this file for details.

There are no insertion points in the plugin.

GoGoProtobuf provides extensions for protocol buffers and GoProtobuf
see http://github.com/gogo/protobuf/gogoproto/doc.go

## Using protocol buffers with Go ##

Once the software is installed, there are two steps to using it.
First you must compile the protocol buffer definitions and then import
them, with the support library, into your program.

To compile the protocol buffer definition, run protoc with the --gogo_out
parameter set to the directory you want to output the Go code to.

	protoc --gogo_out=. *.proto

The generated files will be suffixed .pb.go.  See the Test code below
for an example using such a file.

The package comment for the proto library contains text describing
the interface provided in Go for protocol buffers. Here is an edited
version.

If you are using any gogo.proto extensions you will need to specify the
proto_path to include the descriptor.proto and gogo.proto.
gogo.proto is located in github.com/gogo/protobuf/gogoproto
This should be fine, since your import is the same.
descriptor.proto is located in either github.com/gogo/protobuf/protobuf
or code.google.com/p/protobuf/trunk/src/
Its import is google/protobuf/descriptor.proto so it might need some help.

	protoc --gogo_out=. -I=.:github.com/gogo/protobuf/protobuf *.proto

==========

The proto package converts data structures to and from the
wire format of protocol buffers.  It works in concert with the
Go source code generated for .proto files by the protocol compiler.

A summary of the properties of the protocol buffer interface
for a protocol buffer variable v:

  - Names are turned from camel_case to CamelCase for export.
  - There are no methods on v to set fields; just treat
  	them as structure fields.
  - There are getters that return a field's value if set,
	and return the field's default value if unset.
	The getters work even if the receiver is a nil message.
  - The zero value for a struct is its correct initialization state.
	All desired fields must be set before marshaling.
  - A Reset() method will restore a protobuf struct to its zero state.
  - Non-repeated fields are pointers to the values; nil means unset.
	That is, optional or required field int32 f becomes F *int32.
  - Repeated fields are slices.
  - Helper functions are available to aid the setting of fields.
	Helpers for getting values are superseded by the
	GetFoo methods and their use is deprecated.
		msg.Foo = proto.String("hello") // set field
  - Constants are defined to hold the default values of all fields that
	have them.  They have the form Default_StructName_FieldName.
	Because the getter methods handle defaulted values,
	direct use of these constants should be rare.
  - Enums are given type names and maps from names to values.
	Enum values are prefixed with the enum's type name. Enum types have
	a String method, and a Enum method to assist in message construction.
  - Nested groups and enums have type names prefixed with the name of
  	the surrounding message type.
  - Extensions are given descriptor names that start with E_,
	followed by an underscore-delimited list of the nested messages
	that contain it (if any) followed by the CamelCased name of the
	extension field itself.  HasExtension, ClearExtension, GetExtension
	and SetExtension are functions for manipulating extensions.
  - Oneof field sets are given a single field in their message,
	with distinguished wrapper types for each possible field value.
  - Marshal and Unmarshal are functions to encode and decode the wire format.

When the .proto file specifies `syntax="proto3"`, there are some differences:

  - Non-repeated fields of non-message type are values instead of pointers.
  - Getters are only generated for message and oneof fields.
  - Enum types do not get an Enum method.

Consider file test.proto, containing

```proto
	package example;
	
	enum FOO { X = 17; };
	
	message Test {
	  required string label = 1;
	  optional int32 type = 2 [default=77];
	  repeated int64 reps = 3;
	  optional group OptionalGroup = 4 {
	    required string RequiredField = 5;
	  }
	}
```

To create and play with a Test object from the example package,

```go
	package main

	import (
		"log"

		"github.com/gogo/protobuf/proto"
		"path/to/example"
	)

	func main() {
		test := &example.Test {
			Label: proto.String("hello"),
			Type:  proto.Int32(17),
			Reps:  []int64{1, 2, 3},
			Optionalgroup: &example.Test_OptionalGroup {
				RequiredField: proto.String("good bye"),
			},
		}
		data, err := proto.Marshal(test)
		if err != nil {
			log.Fatal("marshaling error: ", err)
		}
		newTest := &example.Test{}
		err = proto.Unmarshal(data, newTest)
		if err != nil {
			log.Fatal("unmarshaling error: ", err)
		}
		// Now test and newTest contain the same data.
		if test.GetLabel() != newTest.GetLabel() {
			log.Fatalf("data mismatch %q != %q", test.GetLabel(), newTest.GetLabel())
		}
		// etc.
	}
```


## Parameters ##

To pass extra parameters to the plugin, use a comma-separated
parameter list separated from the output directory by a colon:


	protoc --gogo_out=plugins=grpc,import_path=mypackage:. *.proto


- `import_prefix=xxx` - a prefix that is added onto the beginning of
  all imports. Useful for things like generating protos in a
  subdirectory, or regenerating vendored protobufs in-place.
- `import_path=foo/bar` - used as the package if no input files
  declare `go_package`. If it contains slashes, everything up to the
  rightmost slash is ignored.
- `plugins=plugin1+plugin2` - specifies the list of sub-plugins to
  load. The only plugin in this repo is `grpc`.
- `Mfoo/bar.proto=quux/shme` - declares that foo/bar.proto is
  associated with Go package quux/shme.  This is subject to the
  import_prefix parameter.

## gRPC Support ##

If a proto file specifies RPC services, protoc-gen-go can be instructed to
generate code compatible with gRPC (http://www.grpc.io/). To do this, pass
the `plugins` parameter to protoc-gen-go; the usual way is to insert it into
the --go_out argument to protoc:

	protoc --gogo_out=plugins=grpc:. *.proto

## Compatibility ##

The library and the generated code are expected to be stable over time.
However, we reserve the right to make breaking changes without notice for the
following reasons:

- Security. A security issue in the specification or implementation may come to
  light whose resolution requires breaking compatibility. We reserve the right
  to address such security issues.
- Unspecified behavior.  There are some aspects of the Protocol Buffers
  specification that are undefined.  Programs that depend on such unspecified
  behavior may break in future releases.
- Specification errors or changes. If it becomes necessary to address an
  inconsistency, incompleteness, or change in the Protocol Buffers
  specification, resolving the issue could affect the meaning or legality of
  existing programs.  We reserve the right to address such issues, including
  updating the implementations.
- Bugs.  If the library has a bug that violates the specification, a program
  that depends on the buggy behavior may break if the bug is fixed.  We reserve
  the right to fix such bugs.
- Adding methods or fields to generated structs.  These may conflict with field
  names that already exist in a schema, causing applications to break.  When the
  code generator encounters a field in the schema that would collide with a
  generated field or method name, the code generator will append an underscore
  to the generated field or method name.
- Adding, removing, or changing methods or fields in generated structs that
  start with `XXX`.  These parts of the generated code are exported out of
  necessity, but should not be considered part of the public API.
- Adding, removing, or changing unexported symbols in generated code.

Any breaking changes outside of these will be announced 6 months in advance to
protobuf@googlegroups.com.

You should, whenever possible, use generated code created by the `protoc-gen-go`
tool built at the same commit as the `proto` package.  The `proto` package
declares package-level constants in the form `ProtoPackageIsVersionX`.
Application code and generated code may depend on one of these constants to
ensure that compilation will fail if the available version of the proto library
is too old.  Whenever we make a change to the generated code that requires newer
library support, in the same commit we will increment the version number of the
generated code and declare a new package-level constant whose name incorporates
the latest version number.  Removing a compatibility constant is considered a
breaking change and would be subject to the announcement policy stated above.

## Plugins ##

The `protoc-gen-go/generator` package exposes a plugin interface,
which is used by the gRPC code generation. This interface is not
supported and is subject to incompatible changes without notice.
# The Bug

If in a message the following options are set:

* `typedecl` `false`
* `go_getters` `false`
* `marshaller` `true`

And one of the fields is using the `stdtime` and `nullable` `false` extension (to
use `time.Time` instead of the protobuf type), then an import to the _time_ package
is added even if it is not needed.
# YAML marshaling and unmarshaling support for Go

[![Build Status](https://travis-ci.org/ghodss/yaml.svg)](https://travis-ci.org/ghodss/yaml)

## Introduction

A wrapper around [go-yaml](https://github.com/go-yaml/yaml) designed to enable a better way of handling YAML when marshaling to and from structs. 

In short, this library first converts YAML to JSON using go-yaml and then uses `json.Marshal` and `json.Unmarshal` to convert to or from the struct. This means that it effectively reuses the JSON struct tags as well as the custom JSON methods `MarshalJSON` and `UnmarshalJSON` unlike go-yaml. For a detailed overview of the rationale behind this method, [see this blog post](http://ghodss.com/2014/the-right-way-to-handle-yaml-in-golang/).

## Compatibility

This package uses [go-yaml v2](https://github.com/go-yaml/yaml) and therefore supports [everything go-yaml supports](https://github.com/go-yaml/yaml#compatibility).

## Caveats

**Caveat #1:** When using `yaml.Marshal` and `yaml.Unmarshal`, binary data should NOT be preceded with the `!!binary` YAML tag. If you do, go-yaml will convert the binary data from base64 to native binary data, which is not compatible with JSON. You can still use binary in your YAML files though - just store them without the `!!binary` tag and decode the base64 in your code (e.g. in the custom JSON methods `MarshalJSON` and `UnmarshalJSON`). This also has the benefit that your YAML and your JSON binary data will be decoded exactly the same way. As an example:

```
BAD:
	exampleKey: !!binary gIGC

GOOD:
	exampleKey: gIGC
... and decode the base64 data in your code.
```

**Caveat #2:** When using `YAMLToJSON` directly, maps with keys that are maps will result in an error since this is not supported by JSON. This error will occur in `Unmarshal` as well since you can't unmarshal map keys anyways since struct fields can't be keys.

## Installation and usage

To install, run:

```
$ go get github.com/ghodss/yaml
```

And import using:

```
import "github.com/ghodss/yaml"
```

Usage is very similar to the JSON library:

```go
import (
	"fmt"

	"github.com/ghodss/yaml"
)

type Person struct {
	Name string `json:"name"`  // Affects YAML field names too.
	Age int `json:"name"`
}

func main() {
	// Marshal a Person struct to YAML.
	p := Person{"John", 30}
	y, err := yaml.Marshal(p)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(y))
	/* Output:
	name: John
	age: 30
	*/

	// Unmarshal the YAML back into a Person struct.
	var p2 Person
	err := yaml.Unmarshal(y, &p2)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(p2)
	/* Output:
	{John 30}
	*/
}
```

`yaml.YAMLToJSON` and `yaml.JSONToYAML` methods are also available:

```go
import (
	"fmt"

	"github.com/ghodss/yaml"
)
func main() {
	j := []byte(`{"name": "John", "age": 30}`)
	y, err := yaml.JSONToYAML(j)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(y))
	/* Output:
	name: John
	age: 30
	*/
	j2, err := yaml.YAMLToJSON(y)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(j2))
	/* Output:
	{"age":30,"name":"John"}
	*/
}
```
go-spew
=======

[![Build Status](https://travis-ci.org/davecgh/go-spew.png?branch=master)]
(https://travis-ci.org/davecgh/go-spew) [![Coverage Status]
(https://coveralls.io/repos/davecgh/go-spew/badge.png?branch=master)]
(https://coveralls.io/r/davecgh/go-spew?branch=master)

Go-spew implements a deep pretty printer for Go data structures to aid in
debugging.  A comprehensive suite of tests with 100% test coverage is provided
to ensure proper functionality.  See `test_coverage.txt` for the gocov coverage
report.  Go-spew is licensed under the liberal ISC license, so it may be used in
open source or commercial projects.

If you're interested in reading about how this package came to life and some
of the challenges involved in providing a deep pretty printer, there is a blog
post about it
[here](https://blog.cyphertite.com/go-spew-a-journey-into-dumping-go-data-structures/).

## Documentation

[![GoDoc](https://godoc.org/github.com/davecgh/go-spew/spew?status.png)]
(http://godoc.org/github.com/davecgh/go-spew/spew)

Full `go doc` style documentation for the project can be viewed online without
installing this package by using the excellent GoDoc site here:
http://godoc.org/github.com/davecgh/go-spew/spew

You can also view the documentation locally once the package is installed with
the `godoc` tool by running `godoc -http=":6060"` and pointing your browser to
http://localhost:6060/pkg/github.com/davecgh/go-spew/spew

## Installation

```bash
$ go get -u github.com/davecgh/go-spew/spew
```

## Quick Start

Add this import line to the file you're working in:

```Go
import "github.com/davecgh/go-spew/spew"
```

To dump a variable with full newlines, indentation, type, and pointer
information use Dump, Fdump, or Sdump:

```Go
spew.Dump(myVar1, myVar2, ...)
spew.Fdump(someWriter, myVar1, myVar2, ...)
str := spew.Sdump(myVar1, myVar2, ...)
```

Alternatively, if you would prefer to use format strings with a compacted inline
printing style, use the convenience wrappers Printf, Fprintf, etc with %v (most
compact), %+v (adds pointer addresses), %#v (adds types), or %#+v (adds types
and pointer addresses): 

```Go
spew.Printf("myVar1: %v -- myVar2: %+v", myVar1, myVar2)
spew.Printf("myVar3: %#v -- myVar4: %#+v", myVar3, myVar4)
spew.Fprintf(someWriter, "myVar1: %v -- myVar2: %+v", myVar1, myVar2)
spew.Fprintf(someWriter, "myVar3: %#v -- myVar4: %#+v", myVar3, myVar4)
```

## Debugging a Web Application Example

Here is an example of how you can use `spew.Sdump()` to help debug a web application. Please be sure to wrap your output using the `html.EscapeString()` function for safety reasons. You should also only use this debugging technique in a development environment, never in production.

```Go
package main

import (
    "fmt"
    "html"
    "net/http"

    "github.com/davecgh/go-spew/spew"
)

func handler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "text/html")
    fmt.Fprintf(w, "Hi there, %s!", r.URL.Path[1:])
    fmt.Fprintf(w, "<!--\n" + html.EscapeString(spew.Sdump(w)) + "\n-->")
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
```

## Sample Dump Output

```
(main.Foo) {
 unexportedField: (*main.Bar)(0xf84002e210)({
  flag: (main.Flag) flagTwo,
  data: (uintptr) <nil>
 }),
 ExportedField: (map[interface {}]interface {}) {
  (string) "one": (bool) true
 }
}
([]uint8) {
 00000000  11 12 13 14 15 16 17 18  19 1a 1b 1c 1d 1e 1f 20  |............... |
 00000010  21 22 23 24 25 26 27 28  29 2a 2b 2c 2d 2e 2f 30  |!"#$%&'()*+,-./0|
 00000020  31 32                                             |12|
}
```

## Sample Formatter Output

Double pointer to a uint8:
```
	  %v: <**>5
	 %+v: <**>(0xf8400420d0->0xf8400420c8)5
	 %#v: (**uint8)5
	%#+v: (**uint8)(0xf8400420d0->0xf8400420c8)5
```

Pointer to circular struct with a uint8 field and a pointer to itself:
```
	  %v: <*>{1 <*><shown>}
	 %+v: <*>(0xf84003e260){ui8:1 c:<*>(0xf84003e260)<shown>}
	 %#v: (*main.circular){ui8:(uint8)1 c:(*main.circular)<shown>}
	%#+v: (*main.circular)(0xf84003e260){ui8:(uint8)1 c:(*main.circular)(0xf84003e260)<shown>}
```

## Configuration Options

Configuration of spew is handled by fields in the ConfigState type. For
convenience, all of the top-level functions use a global state available via the
spew.Config global.

It is also possible to create a ConfigState instance that provides methods
equivalent to the top-level functions. This allows concurrent configuration
options. See the ConfigState documentation for more details.

```
* Indent
	String to use for each indentation level for Dump functions.
	It is a single space by default.  A popular alternative is "\t".

* MaxDepth
	Maximum number of levels to descend into nested data structures.
	There is no limit by default.

* DisableMethods
	Disables invocation of error and Stringer interface methods.
	Method invocation is enabled by default.

* DisablePointerMethods
	Disables invocation of error and Stringer interface methods on types
	which only accept pointer receivers from non-pointer variables.  This option
	relies on access to the unsafe package, so it will not have any effect when
	running in environments without access to the unsafe package such as Google
	App Engine or with the "disableunsafe" build tag specified.
	Pointer method invocation is enabled by default.

* ContinueOnMethod
	Enables recursion into types after invoking error and Stringer interface
	methods. Recursion after method invocation is disabled by default.

* SortKeys
	Specifies map keys should be sorted before being printed. Use
	this to have a more deterministic, diffable output.  Note that
	only native types (bool, int, uint, floats, uintptr and string)
	and types which implement error or Stringer interfaces are supported,
	with other types sorted according to the reflect.Value.String() output
	which guarantees display stability.  Natural map order is used by
	default.

* SpewKeys
	SpewKeys specifies that, as a last resort attempt, map keys should be
	spewed to strings and sorted by those strings.  This is only considered
	if SortKeys is true.

```

## Unsafe Package Dependency

This package relies on the unsafe package to perform some of the more advanced
features, however it also supports a "limited" mode which allows it to work in
environments where the unsafe package is not available.  By default, it will
operate in this mode on Google App Engine.  The "disableunsafe" build tag may
also be specified to force the package to build without using the unsafe
package.

## License

Go-spew is licensed under the liberal ISC License.
golang-lru
==========

This provides the `lru` package which implements a fixed-size
thread safe LRU cache. It is based on the cache in Groupcache.

Documentation
=============

Full docs are available on [Godoc](http://godoc.org/github.com/hashicorp/golang-lru)

Example
=======

Using the LRU is very simple:

```go
l, _ := New(128)
for i := 0; i < 256; i++ {
    l.Add(i, nil)
}
if l.Len() != 128 {
    panic(fmt.Sprintf("bad len: %v", l.Len()))
}
```
# ratelimit
--
    import "github.com/juju/ratelimit"

The ratelimit package provides an efficient token bucket implementation. See
http://en.wikipedia.org/wiki/Token_bucket.

## Usage

#### func  Reader

```go
func Reader(r io.Reader, bucket *Bucket) io.Reader
```
Reader returns a reader that is rate limited by the given token bucket. Each
token in the bucket represents one byte.

#### func  Writer

```go
func Writer(w io.Writer, bucket *Bucket) io.Writer
```
Writer returns a writer that is rate limited by the given token bucket. Each
token in the bucket represents one byte.

#### type Bucket

```go
type Bucket struct {
}
```

Bucket represents a token bucket that fills at a predetermined rate. Methods on
Bucket may be called concurrently.

#### func  NewBucket

```go
func NewBucket(fillInterval time.Duration, capacity int64) *Bucket
```
NewBucket returns a new token bucket that fills at the rate of one token every
fillInterval, up to the given maximum capacity. Both arguments must be positive.
The bucket is initially full.

#### func  NewBucketWithQuantum

```go
func NewBucketWithQuantum(fillInterval time.Duration, capacity, quantum int64) *Bucket
```
NewBucketWithQuantum is similar to NewBucket, but allows the specification of
the quantum size - quantum tokens are added every fillInterval.

#### func  NewBucketWithRate

```go
func NewBucketWithRate(rate float64, capacity int64) *Bucket
```
NewBucketWithRate returns a token bucket that fills the bucket at the rate of
rate tokens per second up to the given maximum capacity. Because of limited
clock resolution, at high rates, the actual rate may be up to 1% different from
the specified rate.

#### func (*Bucket) Rate

```go
func (tb *Bucket) Rate() float64
```
Rate returns the fill rate of the bucket, in tokens per second.

#### func (*Bucket) Take

```go
func (tb *Bucket) Take(count int64) time.Duration
```
Take takes count tokens from the bucket without blocking. It returns the time
that the caller should wait until the tokens are actually available.

Note that if the request is irrevocable - there is no way to return tokens to
the bucket once this method commits us to taking them.

#### func (*Bucket) TakeAvailable

```go
func (tb *Bucket) TakeAvailable(count int64) int64
```
TakeAvailable takes up to count immediately available tokens from the bucket. It
returns the number of tokens removed, or zero if there are no available tokens.
It does not block.

#### func (*Bucket) TakeMaxDuration

```go
func (tb *Bucket) TakeMaxDuration(count int64, maxWait time.Duration) (time.Duration, bool)
```
TakeMaxDuration is like Take, except that it will only take tokens from the
bucket if the wait time for the tokens is no greater than maxWait.

If it would take longer than maxWait for the tokens to become available, it does
nothing and reports false, otherwise it returns the time that the caller should
wait until the tokens are actually available, and reports true.

#### func (*Bucket) Wait

```go
func (tb *Bucket) Wait(count int64)
```
Wait takes count tokens from the bucket, waiting until they are available.

#### func (*Bucket) WaitMaxDuration

```go
func (tb *Bucket) WaitMaxDuration(count int64, maxWait time.Duration) bool
```
WaitMaxDuration is like Wait except that it will only take tokens from the
bucket if it needs to wait for no greater than maxWait. It reports whether any
tokens have been removed from the bucket If no tokens have been removed, it
returns immediately.
# OAI object model [![Build Status](https://ci.vmware.run/api/badges/go-openapi/spec/status.svg)](https://ci.vmware.run/go-openapi/spec) [![Coverage](https://coverage.vmware.run/badges/go-openapi/spec/coverage.svg)](https://coverage.vmware.run/go-openapi/spec) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/spec/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/spec?status.svg)](http://godoc.org/github.com/go-openapi/spec)

The object model for OpenAPI specification documents# Swagger 2.0 specification schema

This folder contains the Swagger 2.0 specification schema files maintained here:

https://github.com/reverb/swagger-spec/blob/master/schemas/v2.0# Loads OAI specs  [![Build Status](https://ci.vmware.run/api/badges/go-openapi/loads/status.svg)](https://ci.vmware.run/go-openapi/loads) [![Coverage](https://coverage.vmware.run/badges/go-openapi/loads/coverage.svg)](https://coverage.vmware.run/go-openapi/loads) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/loads/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/loads?status.svg)](http://godoc.org/github.com/go-openapi/loads)

Loading of OAI specification documents from local or remote locations.
# OpenAPI initiative analysis [![Build Status](https://ci.vmware.run/api/badges/go-openapi/analysis/status.svg)](https://ci.vmware.run/go-openapi/analysis) [![Coverage](https://coverage.vmware.run/badges/go-openapi/analysis/coverage.svg)](https://coverage.vmware.run/go-openapi/analysis) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/analysis/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/analysis?status.svg)](http://godoc.org/github.com/go-openapi/analysis) 


A foundational library to analyze an OAI specification document for easier reasoning about the content.# Swag [![Build Status](https://ci.vmware.run/api/badges/go-openapi/swag/status.svg)](https://ci.vmware.run/go-openapi/swag) [![Coverage](https://coverage.vmware.run/badges/go-openapi/swag/coverage.svg)](https://coverage.vmware.run/go-openapi/swag) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/swag/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/swag?status.svg)](http://godoc.org/github.com/go-openapi/swag)

Contains a bunch of helper functions:

* convert between value and pointers for builtins
* convert from string to builtin
* fast json concatenation
* search in path
* load from file or http
* name manglin# gojsonpointer [![Build Status](https://ci.vmware.run/api/badges/go-openapi/jsonpointer/status.svg)](https://ci.vmware.run/go-openapi/jsonpointer) [![Coverage](https://coverage.vmware.run/badges/go-openapi/jsonpointer/coverage.svg)](https://coverage.vmware.run/go-openapi/jsonpointer) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/jsonpointer/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/jsonpointer?status.svg)](http://godoc.org/github.com/go-openapi/jsonpointer)
An implementation of JSON Pointer - Go language

## Status
Completed YES

Tested YES

## References
http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-07

### Note
The 4.Evaluation part of the previous reference, starting with 'If the currently referenced value is a JSON array, the reference token MUST contain either...' is not implemented.
# gojsonreference [![Build Status](https://ci.vmware.run/api/badges/go-openapi/jsonreference/status.svg)](https://ci.vmware.run/go-openapi/jsonreference) [![Coverage](https://coverage.vmware.run/badges/go-openapi/jsonreference/coverage.svg)](https://coverage.vmware.run/go-openapi/jsonreference) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/jsonreference/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/jsonreference?status.svg)](http://godoc.org/github.com/go-openapi/jsonreference)
An implementation of JSON Reference - Go language

## Status
Work in progress ( 90% done )

## Dependencies
https://github.com/xeipuuv/gojsonpointer

## References
http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-07

http://tools.ietf.org/html/draft-pbryan-zyp-json-ref-03
[![Build Status](https://travis-ci.org/spf13/pflag.svg?branch=master)](https://travis-ci.org/spf13/pflag)

## Description

pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

pflag is compatible with the [GNU extensions to the POSIX recommendations
for command-line options][1]. For a more precise description, see the
"Command-line flag syntax" section below.

[1]: http://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html

pflag is available under the same style of BSD license as the Go language,
which can be found in the LICENSE file.

## Installation

pflag is available using the standard `go get` command.

Install by running:

    go get github.com/spf13/pflag

Run tests by running:

    go test github.com/spf13/pflag

## Usage

pflag is a drop-in replacement of Go's native flag package. If you import
pflag under the name "flag" then all code should continue to function
with no changes.

``` go
import flag "github.com/spf13/pflag"
```

There is one exception to this: if you directly instantiate the Flag struct
there is one more field "Shorthand" that you will need to set.
Most code never instantiates this struct directly, and instead uses
functions such as String(), BoolVar(), and Var(), and is therefore
unaffected.

Define flags using flag.String(), Bool(), Int(), etc.

This declares an integer flag, -flagname, stored in the pointer ip, with type *int.

``` go
var ip *int = flag.Int("flagname", 1234, "help message for flagname")
```

If you like, you can bind the flag to a variable using the Var() functions.

``` go
var flagvar int
func init() {
    flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")
}
```

Or you can create custom flags that satisfy the Value interface (with
pointer receivers) and couple them to flag parsing by

``` go
flag.Var(&flagVal, "name", "help message for flagname")
```

For such flags, the default value is just the initial value of the variable.

After all flags are defined, call

``` go
flag.Parse()
```

to parse the command line into the defined flags.

Flags may then be used directly. If you're using the flags themselves,
they are all pointers; if you bind to variables, they're values.

``` go
fmt.Println("ip has value ", *ip)
fmt.Println("flagvar has value ", flagvar)
```

There are helpers function to get values later if you have the FlagSet but
it was difficult to keep up with all of the flag pointers in your code.
If you have a pflag.FlagSet with a flag called 'flagname' of type int you
can use GetInt() to get the int value. But notice that 'flagname' must exist
and it must be an int. GetString("flagname") will fail.

``` go
i, err := flagset.GetInt("flagname")
```

After parsing, the arguments after the flag are available as the
slice flag.Args() or individually as flag.Arg(i).
The arguments are indexed from 0 through flag.NArg()-1.

The pflag package also defines some new functions that are not in flag,
that give one-letter shorthands for flags. You can use these by appending
'P' to the name of any function that defines a flag.

``` go
var ip = flag.IntP("flagname", "f", 1234, "help message")
var flagvar bool
func init() {
    flag.BoolVarP("boolname", "b", true, "help message")
}
flag.VarP(&flagVar, "varname", "v", 1234, "help message")
```

Shorthand letters can be used with single dashes on the command line.
Boolean shorthand flags can be combined with other shorthand flags.

The default set of command-line flags is controlled by
top-level functions.  The FlagSet type allows one to define
independent sets of flags, such as to implement subcommands
in a command-line interface. The methods of FlagSet are
analogous to the top-level functions for the command-line
flag set.

## Setting no option default values for flags

After you create a flag it is possible to set the pflag.NoOptDefVal for
the given flag. Doing this changes the meaning of the flag slightly. If
a flag has a NoOptDefVal and the flag is set on the command line without
an option the flag will be set to the NoOptDefVal. For example given:

``` go
var ip = flag.IntP("flagname", "f", 1234, "help message")
flag.Lookup("flagname").NoOptDefVal = "4321"
```

Would result in something like

| Parsed Arguments | Resulting Value |
| -------------    | -------------   |
| --flagname=1357  | ip=1357         |
| --flagname       | ip=4321         |
| [nothing]        | ip=1234         |

## Command line flag syntax

```
--flag    // boolean flags, or flags with no option default values
--flag x  // only on flags without a default value
--flag=x
```

Unlike the flag package, a single dash before an option means something
different than a double dash. Single dashes signify a series of shorthand
letters for flags. All but the last shorthand letter must be boolean flags
or a flag with a default value

```
// boolean or flags where the 'no option default value' is set
-f
-f=true
-abc
but
-b true is INVALID

// non-boolean and flags without a 'no option default value'
-n 1234
-n=1234
-n1234

// mixed
-abcs "hello"
-absd="hello"
-abcs1234
```

Flag parsing stops after the terminator "--". Unlike the flag package,
flags can be interspersed with arguments anywhere on the command line
before this terminator.

Integer flags accept 1234, 0664, 0x1234 and may be negative.
Boolean flags (in their long form) accept 1, 0, t, f, true, false,
TRUE, FALSE, True, False.
Duration flags accept any input valid for time.ParseDuration.

## Mutating or "Normalizing" Flag names

It is possible to set a custom flag name 'normalization function.' It allows flag names to be mutated both when created in the code and when used on the command line to some 'normalized' form. The 'normalized' form is used for comparison. Two examples of using the custom normalization func follow.

**Example #1**: You want -, _, and . in flags to compare the same. aka --my-flag == --my_flag == --my.flag

``` go
func wordSepNormalizeFunc(f *pflag.FlagSet, name string) pflag.NormalizedName {
	from := []string{"-", "_"}
	to := "."
	for _, sep := range from {
		name = strings.Replace(name, sep, to, -1)
	}
	return pflag.NormalizedName(name)
}

myFlagSet.SetNormalizeFunc(wordSepNormalizeFunc)
```

**Example #2**: You want to alias two flags. aka --old-flag-name == --new-flag-name

``` go
func aliasNormalizeFunc(f *pflag.FlagSet, name string) pflag.NormalizedName {
	switch name {
	case "old-flag-name":
		name = "new-flag-name"
		break
	}
	return pflag.NormalizedName(name)
}

myFlagSet.SetNormalizeFunc(aliasNormalizeFunc)
```

## Deprecating a flag or its shorthand
It is possible to deprecate a flag, or just its shorthand. Deprecating a flag/shorthand hides it from help text and prints a usage message when the deprecated flag/shorthand is used.

**Example #1**: You want to deprecate a flag named "badflag" as well as inform the users what flag they should use instead.
```go
// deprecate a flag by specifying its name and a usage message
flags.MarkDeprecated("badflag", "please use --good-flag instead")
```
This hides "badflag" from help text, and prints `Flag --badflag has been deprecated, please use --good-flag instead` when "badflag" is used.

**Example #2**: You want to keep a flag name "noshorthandflag" but deprecate its shortname "n".
```go
// deprecate a flag shorthand by specifying its flag name and a usage message
flags.MarkShorthandDeprecated("noshorthandflag", "please use --noshorthandflag only")
```
This hides the shortname "n" from help text, and prints `Flag shorthand -n has been deprecated, please use --noshorthandflag only` when the shorthand "n" is used.

Note that usage message is essential here, and it should not be empty.

## Hidden flags
It is possible to mark a flag as hidden, meaning it will still function as normal, however will not show up in usage/help text.

**Example**: You have a flag named "secretFlag" that you need for internal use only and don't want it showing up in help text, or for its usage text to be available.
```go
// hide a flag by specifying its name
flags.MarkHidden("secretFlag")
```

## Supporting Go flags when using pflag
In order to support flags defined using Go's `flag` package, they must be added to the `pflag` flagset. This is usually necessary
to support flags defined by third-party dependencies (e.g. `golang/glog`).

**Example**: You want to add the Go flags to the `CommandLine` flagset
```go
import (
	goflag "flag"
	flag "github.com/spf13/pflag"
)

var ip *int = flag.Int("flagname", 1234, "help message for flagname")

func main() {
	flag.CommandLine.AddGoFlagSet(goflag.CommandLine)
	flag.Parse()
}
```

## More info

You can see the full reference documentation of the pflag package
[at godoc.org][3], or through go's standard documentation system by
running `godoc -http=:6060` and browsing to
[http://localhost:6060/pkg/github.com/ogier/pflag][2] after
installation.

[2]: http://localhost:6060/pkg/github.com/ogier/pflag
[3]: http://godoc.org/github.com/ogier/pflag
