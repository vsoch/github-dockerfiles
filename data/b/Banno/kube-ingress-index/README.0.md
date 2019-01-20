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
# Go Text

This repository holds supplementary Go libraries for text processing, many involving Unicode.

## Semantic Versioning
This repo uses Semantic versioning (http://semver.org/), so
1. MAJOR version when you make incompatible API changes,
1. MINOR version when you add functionality in a backwards-compatible manner,
   and
1. PATCH version when you make backwards-compatible bug fixes.

Until version 1.0.0 of x/text is reached, the minor version is considered a
major version. So going from 0.1.0 to 0.2.0 is considered to be a major version
bump.

A major new CLDR version is mapped to a minor version increase in x/text.
Any other new CLDR version is mapped to a patch version increase in x/text.

It is important that the Unicode version used in `x/text` matches the one used
by your Go compiler. The `x/text` repository supports multiple versions of
Unicode and will match the version of Unicode to that of the Go compiler. At the
moment this is supported for Go compilers from version 1.7.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/text`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/text`.

## Contribute
To submit changes to this repository, see http://golang.org/doc/contribute.html.

To generate the tables in this repository (except for the encoding tables),
run go generate from this directory. By default tables are generated for the
Unicode version in core and the CLDR version defined in
golang.org/x/text/unicode/cldr.

Running go generate will as a side effect create a DATA subdirectory in this
directory, which holds all files that are used as a source for generating the
tables. This directory will also serve as a cache.

## Testing
Run

    go test ./...

from this directory to run all tests. Add the "-tags icu" flag to also run
ICU conformance tests (if available). This requires that you have the correct
ICU version installed on your system.

TODO:
- updating unversioned source files.

## Generating Tables

To generate the tables in this repository (except for the encoding
tables), run `go generate` from this directory. By default tables are
generated for the Unicode version in core and the CLDR version defined in
golang.org/x/text/unicode/cldr.

Running go generate will as a side effect create a DATA subdirectory in this
directory which holds all files that are used as a source for generating the
tables. This directory will also serve as a cache.

## Versions
To update a Unicode version run

    UNICODE_VERSION=x.x.x go generate

where `x.x.x` must correspond to a directory in http://www.unicode.org/Public/.
If this version is newer than the version in core it will also update the
relevant packages there. The idna package in x/net will always be updated.

To update a CLDR version run

    CLDR_VERSION=version go generate

where `version` must correspond to a directory in
http://www.unicode.org/Public/cldr/.

Note that the code gets adapted over time to changes in the data and that
backwards compatibility is not maintained.
So updating to a different version may not work.

The files in DATA/{iana|icu|w3|whatwg} are currently not versioned.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the image repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/image:" in the
subject line, so it is easy to find.
The export directory contains packages that are generated using the x/text
infrastructure, but live elsewhere.
At some point we can expose some of the infrastructure, but for now this
is not done.
# sys

This repository holds supplemental Go packages for low-level interactions with
the operating system.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/sys`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/sys`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the sys repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/sys:" in the
subject line, so it is easy to find.
# Building `sys/unix`

The sys/unix package provides access to the raw system call interface of the
underlying operating system. See: https://godoc.org/golang.org/x/sys/unix

Porting Go to a new architecture/OS combination or adding syscalls, types, or
constants to an existing architecture/OS pair requires some manual effort;
however, there are tools that automate much of the process.

## Build Systems

There are currently two ways we generate the necessary files. We are currently
migrating the build system to use containers so the builds are reproducible.
This is being done on an OS-by-OS basis. Please update this documentation as
components of the build system change.

### Old Build System (currently for `GOOS != "Linux" || GOARCH == "sparc64"`)

The old build system generates the Go files based on the C header files
present on your system. This means that files
for a given GOOS/GOARCH pair must be generated on a system with that OS and
architecture. This also means that the generated code can differ from system
to system, based on differences in the header files.

To avoid this, if you are using the old build system, only generate the Go
files on an installation with unmodified header files. It is also important to
keep track of which version of the OS the files were generated from (ex.
Darwin 14 vs Darwin 15). This makes it easier to track the progress of changes
and have each OS upgrade correspond to a single change.

To build the files for your current OS and architecture, make sure GOOS and
GOARCH are set correctly and run `mkall.sh`. This will generate the files for
your specific system. Running `mkall.sh -n` shows the commands that will be run.

Requirements: bash, perl, go

### New Build System (currently for `GOOS == "Linux" && GOARCH != "sparc64"`)

The new build system uses a Docker container to generate the go files directly
from source checkouts of the kernel and various system libraries. This means
that on any platform that supports Docker, all the files using the new build
system can be generated at once, and generated files will not change based on
what the person running the scripts has installed on their computer.

The OS specific files for the new build system are located in the `${GOOS}`
directory, and the build is coordinated by the `${GOOS}/mkall.go` program. When
the kernel or system library updates, modify the Dockerfile at
`${GOOS}/Dockerfile` to checkout the new release of the source.

To build all the files under the new build system, you must be on an amd64/Linux
system and have your GOOS and GOARCH set accordingly. Running `mkall.sh` will
then generate all of the files for all of the GOOS/GOARCH pairs in the new build
system. Running `mkall.sh -n` shows the commands that will be run.

Requirements: bash, perl, go, docker

## Component files

This section describes the various files used in the code generation process.
It also contains instructions on how to modify these files to add a new
architecture/OS or to add additional syscalls, types, or constants. Note that
if you are using the new build system, the scripts cannot be called normally.
They must be called from within the docker container.

### asm files

The hand-written assembly file at `asm_${GOOS}_${GOARCH}.s` implements system
call dispatch. There are three entry points:
```
  func Syscall(trap, a1, a2, a3 uintptr) (r1, r2, err uintptr)
  func Syscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2, err uintptr)
  func RawSyscall(trap, a1, a2, a3 uintptr) (r1, r2, err uintptr)
```
The first and second are the standard ones; they differ only in how many
arguments can be passed to the kernel. The third is for low-level use by the
ForkExec wrapper. Unlike the first two, it does not call into the scheduler to
let it know that a system call is running.

When porting Go to an new architecture/OS, this file must be implemented for
each GOOS/GOARCH pair.

### mksysnum

Mksysnum is a script located at `${GOOS}/mksysnum.pl` (or `mksysnum_${GOOS}.pl`
for the old system). This script takes in a list of header files containing the
syscall number declarations and parses them to produce the corresponding list of
Go numeric constants. See `zsysnum_${GOOS}_${GOARCH}.go` for the generated
constants.

Adding new syscall numbers is mostly done by running the build on a sufficiently
new installation of the target OS (or updating the source checkouts for the
new build system). However, depending on the OS, you make need to update the
parsing in mksysnum.

### mksyscall.pl

The `syscall.go`, `syscall_${GOOS}.go`, `syscall_${GOOS}_${GOARCH}.go` are
hand-written Go files which implement system calls (for unix, the specific OS,
or the specific OS/Architecture pair respectively) that need special handling
and list `//sys` comments giving prototypes for ones that can be generated.

The mksyscall.pl script takes the `//sys` and `//sysnb` comments and converts
them into syscalls. This requires the name of the prototype in the comment to
match a syscall number in the `zsysnum_${GOOS}_${GOARCH}.go` file. The function
prototype can be exported (capitalized) or not.

Adding a new syscall often just requires adding a new `//sys` function prototype
with the desired arguments and a capitalized name so it is exported. However, if
you want the interface to the syscall to be different, often one will make an
unexported `//sys` prototype, an then write a custom wrapper in
`syscall_${GOOS}.go`.

### types files

For each OS, there is a hand-written Go file at `${GOOS}/types.go` (or
`types_${GOOS}.go` on the old system). This file includes standard C headers and
creates Go type aliases to the corresponding C types. The file is then fed
through godef to get the Go compatible definitions. Finally, the generated code
is fed though mkpost.go to format the code correctly and remove any hidden or
private identifiers. This cleaned-up code is written to
`ztypes_${GOOS}_${GOARCH}.go`.

The hardest part about preparing this file is figuring out which headers to
include and which symbols need to be `#define`d to get the actual data
structures that pass through to the kernel system calls. Some C libraries
preset alternate versions for binary compatibility and translate them on the
way in and out of system calls, but there is almost always a `#define` that can
get the real ones.
See `types_darwin.go` and `linux/types.go` for examples.

To add a new type, add in the necessary include statement at the top of the
file (if it is not already there) and add in a type alias line. Note that if
your type is significantly different on different architectures, you may need
some `#if/#elif` macros in your include statements.

### mkerrors.sh

This script is used to generate the system's various constants. This doesn't
just include the error numbers and error strings, but also the signal numbers
an a wide variety of miscellaneous constants. The constants come from the list
of include files in the `includes_${uname}` variable. A regex then picks out
the desired `#define` statements, and generates the corresponding Go constants.
The error numbers and strings are generated from `#include <errno.h>`, and the
signal numbers and strings are generated from `#include <signal.h>`. All of
these constants are written to `zerrors_${GOOS}_${GOARCH}.go` via a C program,
`_errors.c`, which prints out all the constants.

To add a constant, add the header that includes it to the appropriate variable.
Then, edit the regex (if necessary) to match the desired constant. Avoid making
the regex too broad to avoid matching unintended constants.


## Generated files

### `zerror_${GOOS}_${GOARCH}.go`

A file containing all of the system's generated error numbers, error strings,
signal numbers, and constants. Generated by `mkerrors.sh` (see above).

### `zsyscall_${GOOS}_${GOARCH}.go`

A file containing all the generated syscalls for a specific GOOS and GOARCH.
Generated by `mksyscall.pl` (see above).

### `zsysnum_${GOOS}_${GOARCH}.go`

A list of numeric constants for all the syscall number of the specific GOOS
and GOARCH. Generated by mksysnum (see above).

### `ztypes_${GOOS}_${GOARCH}.go`

A file containing Go types for passing into (or returning from) syscalls.
Generated by godefs and the types file (see above).
# Go Cryptography

This repository holds supplementary Go cryptography libraries.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/crypto/...`. You
can also manually git clone the repository to `$GOPATH/src/golang.org/x/crypto`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the crypto repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/crypto:" in the
subject line, so it is easy to find.

Note that contributions to the cryptography package receive additional scrutiny
due to their sensitive nature. Patches may take longer than normal to receive
feedback.
# Go Networking

This repository holds supplementary Go networking libraries.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/net`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/net`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit
changes to this repository, see https://golang.org/doc/contribute.html.
The main issue tracker for the net repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/net:" in the
subject line, so it is easy to find.
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
The MongoDB driver for Go
-------------------------

Please go to [http://labix.org/mgo](http://labix.org/mgo) for all project details.
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

The yaml package is licensed under the Apache License 2.0. Please see the LICENSE file for details.


Example
-------

Some more examples can be found in the "examples" folder.

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

// Note: struct fields must be public in order for unmarshal to
// correctly populate the data.
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

urlesc [![Build Status](https://travis-ci.org/PuerkitoBio/urlesc.svg?branch=master)](https://travis-ci.org/PuerkitoBio/urlesc) [![GoDoc](http://godoc.org/github.com/PuerkitoBio/urlesc?status.svg)](http://godoc.org/github.com/PuerkitoBio/urlesc)
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

*    **2016-11-14 (v1.1.0)** : IDN: Conform to RFC 5895: Fold character width (thanks to @beeker1121).
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
@beeker1121

## License

The [BSD 3-Clause license][bsd].

[bsd]: http://opensource.org/licenses/BSD-3-Clause
[wiki]: http://en.wikipedia.org/wiki/URL_normalization
[rfc]: http://tools.ietf.org/html/rfc3986#section-6
[godoc]: http://go.pkgdoc.org/github.com/PuerkitoBio/purell
[pr5]: https://github.com/PuerkitoBio/purell/pull/5
[iss7]: https://github.com/PuerkitoBio/purell/issues/7
# easyjson [![Build Status](https://travis-ci.org/mailru/easyjson.svg?branch=master)](https://travis-ci.org/mailru/easyjson) [![Go Report Card](https://goreportcard.com/badge/github.com/mailru/easyjson)](https://goreportcard.com/report/github.com/mailru/easyjson)

Package easyjson provides a fast and easy way to marshal/unmarshal Go structs
to/from JSON without the use of reflection. In performance tests, easyjson
outperforms the standard `encoding/json` package by a factor of 4-5x, and other
JSON encoding packages by a factor of 2-3x.

easyjson aims to keep generated Go code simple enough so that it can be easily
optimized or fixed. Another goal is to provide users with the ability to
customize the generated code by providing options not available with the
standard `encoding/json` package, such as generating "snake_case" names or
enabling `omitempty` behavior by default.

## Usage
```sh
# install
go get -u github.com/mailru/easyjson/...

# run
easyjson -all <file>.go
```

The above will generate `<file>_easyjson.go` containing the appropriate marshaler and
unmarshaler funcs for all structs contained in `<file>.go`.

Please note that easyjson requires a full Go build environment and the `GOPATH`
environment variable to be set. This is because easyjson code generation
invokes `go run` on a temporary file (an approach to code generation borrowed
from [ffjson](https://github.com/pquerna/ffjson)).

## Options
```txt
Usage of easyjson:
  -all
    	generate marshaler/unmarshalers for all structs in a file
  -build_tags string
    	build tags to add to generated file
  -leave_temps
    	do not delete temporary files
  -no_std_marshalers
    	don't generate MarshalJSON/UnmarshalJSON funcs
  -noformat
    	do not run 'gofmt -w' on output file
  -omit_empty
    	omit empty fields by default
  -output_filename string
    	specify the filename of the output
  -pkg
    	process the whole package instead of just the given file
  -snake_case
    	use snake_case names instead of CamelCase by default
  -lower_camel_case
        use lowerCamelCase instead of CamelCase by default
  -stubs
    	only generate stubs for marshaler/unmarshaler funcs
```

Using `-all` will generate marshalers/unmarshalers for all Go structs in the
file. If `-all` is not provided, then only those structs whose preceding
comment starts with `easyjson:json` will have marshalers/unmarshalers
generated. For example:

```go
//easyjson:json
type A struct {}
```

Additional option notes:

* `-snake_case` tells easyjson to generate snake\_case field names by default
  (unless overridden by a field tag). The CamelCase to snake\_case conversion
  algorithm should work in most cases (ie, HTTPVersion will be converted to
  "http_version").

* `-build_tags` will add the specified build tags to generated Go sources.

## Generated Marshaler/Unmarshaler Funcs

For Go struct types, easyjson generates the funcs `MarshalEasyJSON` /
`UnmarshalEasyJSON` for marshaling/unmarshaling JSON. In turn, these satisify
the `easyjson.Marshaler` and `easyjson.Unmarshaler` interfaces and when used in
conjunction with `easyjson.Marshal` / `easyjson.Unmarshal` avoid unnecessary
reflection / type assertions during marshaling/unmarshaling to/from JSON for Go
structs.

easyjson also generates `MarshalJSON` and `UnmarshalJSON` funcs for Go struct
types compatible with the standard `json.Marshaler` and `json.Unmarshaler`
interfaces. Please be aware that using the standard `json.Marshal` /
`json.Unmarshal` for marshaling/unmarshaling will incur a significant
performance penalty when compared to using `easyjson.Marshal` /
`easyjson.Unmarshal`.

Additionally, easyjson exposes utility funcs that use the `MarshalEasyJSON` and
`UnmarshalEasyJSON` for marshaling/unmarshaling to and from standard readers
and writers. For example, easyjson provides `easyjson.MarshalToHTTPResponseWriter`
which marshals to the standard `http.ResponseWriter`. Please see the [GoDoc
listing](https://godoc.org/github.com/mailru/easyjson) for the full listing of
utility funcs that are available.

## Controlling easyjson Marshaling and Unmarshaling Behavior

Go types can provide their own `MarshalEasyJSON` and `UnmarshalEasyJSON` funcs
that satisify the `easyjson.Marshaler` / `easyjson.Unmarshaler` interfaces.
These will be used by `easyjson.Marshal` and `easyjson.Unmarshal` when defined
for a Go type.

Go types can also satisify the `easyjson.Optional` interface, which allows the
type to define its own `omitempty` logic.

## Type Wrappers

easyjson provides additional type wrappers defined in the `easyjson/opt`
package. These wrap the standard Go primitives and in turn satisify the
easyjson interfaces.

The `easyjson/opt` type wrappers are useful when needing to distinguish between
a missing value and/or when needing to specifying a default value. Type
wrappers allow easyjson to avoid additional pointers and heap allocations and
can significantly increase performance when used properly.

## Memory Pooling

easyjson uses a buffer pool that allocates data in increasing chunks from 128
to 32768 bytes. Chunks of 512 bytes and larger will be reused with the help of
`sync.Pool`. The maximum size of a chunk is bounded to reduce redundant memory
allocation and to allow larger reusable buffers.

easyjson's custom allocation buffer pool is defined in the `easyjson/buffer`
package, and the default behavior pool behavior can be modified (if necessary)
through a call to `buffer.Init()` prior to any marshaling or unmarshaling.
Please see the [GoDoc listing](https://godoc.org/github.com/mailru/easyjson/buffer)
for more information.

## Issues, Notes, and Limitations

* easyjson is still early in its development. As such, there are likely to be
  bugs and missing features when compared to `encoding/json`. In the case of a
  missing feature or bug, please create a GitHub issue. Pull requests are
  welcome!

* Unlike `encoding/json`, object keys are case-sensitive. Case-insensitive
  matching is not currently provided due to the significant performance hit
  when doing case-insensitive key matching. In the future, case-insensitive
  object key matching may be provided via an option to the generator.

* easyjson makes use of `unsafe`, which simplifies the code and
  provides significant performance benefits by allowing no-copy
  conversion from `[]byte` to `string`. That said, `unsafe` is used
  only when unmarshaling and parsing JSON, and any `unsafe` operations
  / memory allocations done will be safely deallocated by
  easyjson. Set the build tag `easyjson_nounsafe` to compile it
  without `unsafe`.

* easyjson is compatible with Google App Engine. The `appengine` build
  tag (set by App Engine's environment) will automatically disable the
  use of `unsafe`, which is not allowed in App Engine's Standard
  Environment. Note that the use with App Engine is still experimental.

* Floats are formatted using the default precision from Go's `strconv` package.
  As such, easyjson will not correctly handle high precision floats when
  marshaling/unmarshaling JSON. Note, however, that there are very few/limited
  uses where this behavior is not sufficient for general use. That said, a
  different package may be needed if precise marshaling/unmarshaling of high
  precision floats to/from JSON is required.

* While unmarshaling, the JSON parser does the minimal amount of work needed to
  skip over unmatching parens, and as such full validation is not done for the
  entire JSON value being unmarshaled/parsed.

* Currently there is no true streaming support for encoding/decoding as
  typically for many uses/protocols the final, marshaled length of the JSON
  needs to be known prior to sending the data. Currently this is not possible
  with easyjson's architecture.

## Benchmarks

Most benchmarks were done using the example
[13kB example JSON](https://dev.twitter.com/rest/reference/get/search/tweets)
(9k after eliminating whitespace). This example is similar to real-world data,
is well-structured, and contains a healthy variety of different types, making
it ideal for JSON serialization benchmarks.

Note:

* For small request benchmarks, an 80 byte portion of the above example was
  used.

* For large request marshaling benchmarks, a struct containing 50 regular
  samples was used, making a ~500kB output JSON.

* Benchmarks are showing the results of easyjson's default behaviour,
  which makes use of `unsafe`.

Benchmarks are available in the repository and can be run by invoking `make`.

### easyjson vs. encoding/json

easyjson is roughly 5-6 times faster than the standard `encoding/json` for
unmarshaling, and 3-4 times faster for non-concurrent marshaling. Concurrent
marshaling is 6-7x faster if marshaling to a writer.

### easyjson vs. ffjson

easyjson uses the same approach for JSON marshaling as
[ffjson](https://github.com/pquerna/ffjson), but takes a significantly
different approach to lexing and parsing JSON during unmarshaling. This means
easyjson is roughly 2-3x faster for unmarshaling and 1.5-2x faster for
non-concurrent unmarshaling.

As of this writing, `ffjson` seems to have issues when used concurrently:
specifically, large request pooling hurts `ffjson`'s performance and causes
scalability issues. These issues with `ffjson` can likely be fixed, but as of
writing remain outstanding/known issues with `ffjson`.

easyjson and `ffjson` have similar performance for small requests, however
easyjson outperforms `ffjson` by roughly 2-5x times for large requests when
used with a writer.

### easyjson vs. go/codec

[go/codec](https://github.com/ugorji/go) provides
compile-time helpers for JSON generation. In this case, helpers do not work
like marshalers as they are encoding-independent.

easyjson is generally 2x faster than `go/codec` for non-concurrent benchmarks
and about 3x faster for concurrent encoding (without marshaling to a writer).

In an attempt to measure marshaling performance of `go/codec` (as opposed to
allocations/memcpy/writer interface invocations), a benchmark was done with
resetting length of a byte slice rather than resetting the whole slice to nil.
However, the optimization in this exact form may not be applicable in practice,
since the memory is not freed between marshaling operations.

### easyjson vs 'ujson' python module

[ujson](https://github.com/esnme/ultrajson) is using C code for parsing, so it
is interesting to see how plain golang compares to that. It is imporant to note
that the resulting object for python is slower to access, since the library
parses JSON object into dictionaries.

easyjson is slightly faster for unmarshaling and 2-3x faster than `ujson` for
marshaling.

### Benchmark Results

`ffjson` results are from February 4th, 2016, using the latest `ffjson` and go1.6.
`go/codec` results are from March 4th, 2016, using the latest `go/codec` and go1.6.

#### Unmarshaling

| lib      | json size | MB/s | allocs/op | B/op  |
|:---------|:----------|-----:|----------:|------:|
| standard | regular   | 22   | 218       | 10229 |
| standard | small     | 9.7  | 14        | 720   |
|          |           |      |           |       |
| easyjson | regular   | 125  | 128       | 9794  |
| easyjson | small     | 67   | 3         | 128   |
|          |           |      |           |       |
| ffjson   | regular   | 66   | 141       | 9985  |
| ffjson   | small     | 17.6 | 10        | 488   |
|          |           |      |           |       |
| codec    | regular   | 55   | 434       | 19299 |
| codec    | small     | 29   | 7         | 336   |
|          |           |      |           |       |
| ujson    | regular   | 103  | N/A       | N/A   |

#### Marshaling, one goroutine.

| lib       | json size | MB/s | allocs/op | B/op  |
|:----------|:----------|-----:|----------:|------:|
| standard  | regular   | 75   | 9         | 23256 |
| standard  | small     | 32   | 3         | 328   |
| standard  | large     | 80   | 17        | 1.2M  |
|           |           |      |           |       |
| easyjson  | regular   | 213  | 9         | 10260 |
| easyjson* | regular   | 263  | 8         | 742   |
| easyjson  | small     | 125  | 1         | 128   |
| easyjson  | large     | 212  | 33        | 490k  |
| easyjson* | large     | 262  | 25        | 2879  |
|           |           |      |           |       |
| ffjson    | regular   | 122  | 153       | 21340 |
| ffjson**  | regular   | 146  | 152       | 4897  |
| ffjson    | small     | 36   | 5         | 384   |
| ffjson**  | small     | 64   | 4         | 128   |
| ffjson    | large     | 134  | 7317      | 818k  |
| ffjson**  | large     | 125  | 7320      | 827k  |
|           |           |      |           |       |
| codec     | regular   | 80   | 17        | 33601 |
| codec***  | regular   | 108  | 9         | 1153  |
| codec     | small     | 42   | 3         | 304   |
| codec***  | small     | 56   | 1         | 48    |
| codec     | large     | 73   | 483       | 2.5M  |
| codec***  | large     | 103  | 451       | 66007 |
|           |           |      |           |       |
| ujson     | regular   | 92   | N/A       | N/A   |

\* marshaling to a writer,
\*\* using `ffjson.Pool()`,
\*\*\* reusing output slice instead of resetting it to nil

#### Marshaling, concurrent.

| lib       | json size | MB/s | allocs/op | B/op  |
|:----------|:----------|-----:|----------:|------:|
| standard  | regular   | 252  | 9         | 23257 |
| standard  | small     | 124  | 3         | 328   |
| standard  | large     | 289  | 17        | 1.2M  |
|           |           |      |           |       |
| easyjson  | regular   | 792  | 9         | 10597 |
| easyjson* | regular   | 1748 | 8         | 779   |
| easyjson  | small     | 333  | 1         | 128   |
| easyjson  | large     | 718  | 36        | 548k  |
| easyjson* | large     | 2134 | 25        | 4957  |
|           |           |      |           |       |
| ffjson    | regular   | 301  | 153       | 21629 |
| ffjson**  | regular   | 707  | 152       | 5148  |
| ffjson    | small     | 62   | 5         | 384   |
| ffjson**  | small     | 282  | 4         | 128   |
| ffjson    | large     | 438  | 7330      | 1.0M  |
| ffjson**  | large     | 131  | 7319      | 820k  |
|           |           |      |           |       |
| codec     | regular   | 183  | 17        | 33603 |
| codec***  | regular   | 671  | 9         | 1157  |
| codec     | small     | 147  | 3         | 304   |
| codec***  | small     | 299  | 1         | 48    |
| codec     | large     | 190  | 483       | 2.5M  |
| codec***  | large     | 752  | 451       | 77574 |

\* marshaling to a writer,
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

It is ready for production use. It works fine after extensive use in the wild.

[![Build Status][1]][2]
[![GoDoc][3]][4]
[![GoCard][5]][6]

[1]: https://travis-ci.org/imdario/mergo.png
[2]: https://travis-ci.org/imdario/mergo
[3]: https://godoc.org/github.com/imdario/mergo?status.svg
[4]: https://godoc.org/github.com/imdario/mergo
[5]: https://goreportcard.com/badge/imdario/mergo
[6]: https://goreportcard.com/report/github.com/imdario/mergo

### Important note

Mergo is intended to assign **only** zero value fields on destination with source value. Since April 6th it works like this. Before it didn't work properly, causing some random overwrites. After some issues and PRs I found it didn't merge as I designed it. Thanks to [imdario/mergo#8](https://github.com/imdario/mergo/pull/8) overwriting functions were added and the wrong behavior was clearly detected.

If you were using Mergo **before** April 6th 2015, please check your project works as intended after updating your local copy with ```go get -u github.com/imdario/mergo```. I apologize for any issue caused by its previous behavior and any future bug that Mergo could cause (I hope it won't!) in existing projects after the change (release 0.2.0).

### Mergo in the wild

- [docker/docker](https://github.com/docker/docker/)
- [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
- [imdario/zas](https://github.com/imdario/zas)
- [soniah/dnsmadeeasy](https://github.com/soniah/dnsmadeeasy)
- [EagerIO/Stout](https://github.com/EagerIO/Stout)
- [lynndylanhurley/defsynth-api](https://github.com/lynndylanhurley/defsynth-api)
- [russross/canvasassignments](https://github.com/russross/canvasassignments)
- [rdegges/cryptly-api](https://github.com/rdegges/cryptly-api)
- [casualjim/exeggutor](https://github.com/casualjim/exeggutor)
- [divshot/gitling](https://github.com/divshot/gitling)
- [RWJMurphy/gorl](https://github.com/RWJMurphy/gorl)
- [andrerocker/deploy42](https://github.com/andrerocker/deploy42)
- [elwinar/rambler](https://github.com/elwinar/rambler)
- [tmaiaroto/gopartman](https://github.com/tmaiaroto/gopartman)
- [jfbus/impressionist](https://github.com/jfbus/impressionist)
- [Jmeyering/zealot](https://github.com/Jmeyering/zealot)
- [godep-migrator/rigger-host](https://github.com/godep-migrator/rigger-host)
- [Dronevery/MultiwaySwitch-Go](https://github.com/Dronevery/MultiwaySwitch-Go)
- [thoas/picfit](https://github.com/thoas/picfit)
- [mantasmatelis/whooplist-server](https://github.com/mantasmatelis/whooplist-server)
- [jnuthong/item_search](https://github.com/jnuthong/item_search)
- [Iris Web Framework](https://github.com/kataras/iris)

## Installation

    go get github.com/imdario/mergo

    // use in your .go code
    import (
        "github.com/imdario/mergo"
    )

## Usage

You can only merge same-type structs with exported fields initialized as zero value of their type and same-types maps. Mergo won't merge unexported (private) fields but will do recursively any exported one. Also maps will be merged recursively except for structs inside maps (because they are not addressable using Go reflection).

```go
if err := mergo.Merge(&dst, src); err != nil {
    // ...
}
```

Also, you can merge overwriting values using the transformer WithOverride.

```go
if err := mergo.Merge(&dst, src, WithOverride); err != nil {
    // ...
}
```

Additionally, you can map a map[string]interface{} to a struct (and otherwise, from struct to map), following the same restrictions as in Merge(). Keys are capitalized to find each corresponding exported field.

```go
if err := mergo.Map(&dst, srcMap); err != nil {
    // ...
}
```

Warning: if you map a struct to map, it won't do it recursively. Don't expect Mergo to map struct members of your struct as `map[string]interface{}`. They will be just assigned as values.

More information and examples in [godoc documentation](http://godoc.org/github.com/imdario/mergo).

### Nice example

```go
package main

import (
	"fmt"
	"github.com/imdario/mergo"
)

type Foo struct {
	A string
	B int64
}

func main() {
	src := Foo{
		A: "one",
		B: 2,
	}
	dest := Foo{
		A: "two",
	}
	mergo.Merge(&dest, src)
	fmt.Println(dest)
	// Will print
	// {two 2}
}
```

Note: if test are failing due missing package, please execute:

    go get gopkg.in/yaml.v2

### Transformers

Transformers allow to merge specific types differently than in the default behavior. In other words, now you can customize how some types are merged. For example, `time.Time` is a struct; it doesn't have zero value but IsZero can return true because it has fields with zero value. How can we merge a non-zero `time.Time`?

```go
package main

import (
	"fmt"
        "reflect"
        "time"
)

type timeTransfomer struct {
}

func (t timeTransfomer) Transformer(typ reflect.Type) func(dst, src reflect.Value) error {
	if typ == reflect.TypeOf(time.Time{}) {
		return func(dst, src reflect.Value) error {
			if dst.CanSet() {
				isZero := dst.MethodByName("IsZero")
				result := isZero.Call([]reflect.Value{})
				if result[0].Bool() {
					dst.Set(src)
				}
			}
		}
	}
	return nil
}

type Snapshot struct {
	Time time.Time
	// ...
}

func main() {
	src := Snapshot{time.Now()}
	dest := Snapshot{}
	mergo.Merge(&dest, src, WithTransformers(timeTransfomer{}))
	fmt.Println(dest)
	// Will print
	// { 2018-01-12 01:15:00 +0000 UTC m=+0.000000001 }
}
```


## Contact me

If I can help you, you have an idea or you are using Mergo in your projects, don't hesitate to drop me a line (or a pull request): [@im_dario](https://twitter.com/im_dario)

## About

Written by [Dario Castañé](http://dario.im).

## License

[BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) license, as [Go language](http://golang.org/LICENSE).
gomock [![Build Status](https://travis-ci.org/golang/mock.svg?branch=master)](https://travis-ci.org/golang/mock)
======

GoMock is a mocking framework for the [Go programming language][golang]. It
integrates well with Go's built-in `testing` package, but can be used in other
contexts too.


Installation
------------

Once you have [installed Go][golang-install], run these commands
to install the `gomock` package and the `mockgen` tool:

    go get github.com/golang/mock/gomock
    go get github.com/golang/mock/mockgen


Documentation
-------------

After installing, you can use `go doc` to get documentation:

    go doc github.com/golang/mock/gomock

Alternatively, there is an online reference for the package hosted on GoPkgDoc
[here][gomock-ref].


Running mockgen
---------------

`mockgen` has two modes of operation: source and reflect.
Source mode generates mock interfaces from a source file.
It is enabled by using the -source flag. Other flags that
may be useful in this mode are -imports and -aux_files.

Example:

	mockgen -source=foo.go [other options]

Reflect mode generates mock interfaces by building a program
that uses reflection to understand interfaces. It is enabled
by passing two non-flag arguments: an import path, and a
comma-separated list of symbols.

Example:

	mockgen database/sql/driver Conn,Driver

The `mockgen` command is used to generate source code for a mock
class given a Go source file containing interfaces to be mocked.
It supports the following flags:

 *  `-source`: A file containing interfaces to be mocked.

 *  `-destination`: A file to which to write the resulting source code. If you
    don't set this, the code is printed to standard output.

 *  `-package`: The package to use for the resulting mock class
    source code. If you don't set this, the package name is `mock_` concatenated
    with the package of the input file.

 *  `-imports`: A list of explicit imports that should be used in the resulting
    source code, specified as a comma-separated list of elements of the form
    `foo=bar/baz`, where `bar/baz` is the package being imported and `foo` is
    the identifier to use for the package in the generated source code.

 *  `-aux_files`: A list of additional files that should be consulted to
    resolve e.g. embedded interfaces defined in a different file. This is
    specified as a comma-separated list of elements of the form
    `foo=bar/baz.go`, where `bar/baz.go` is the source file and `foo` is the
    package name of that file used by the -source file.

*  `-build_flags`: (reflect mode only) Flags passed verbatim to `go build`.

For an example of the use of `mockgen`, see the `sample/` directory. In simple
cases, you will need only the `-source` flag.


TODO: Brief overview of how to create mock objects and set up expectations, and
an example.

[golang]: http://golang.org/
[golang-install]: http://golang.org/doc/install.html#releases
[gomock-ref]: http://godoc.org/github.com/golang/mock/gomock
From #52, this tests an unexported method in the mocked interface.
This directory contains an example of a package containing a non-trivial
interface that can be mocked with GoMock. The interesting files are:

 *  `user.go`: Source code for the sample package, containing interfaces to be
    mocked. This file depends on the packages named imp[1-4] for various things.

 *  `user_test.go`: A test for the sample package, in which mocks of the
    interfaces from `user.go` are used. This demonstrates how to create mock
    objects, set up expectations, and so on.

 *  `mock_user/mock_user.go`: The generated mock code. See ../update_mocks.sh
    for the command used to generate it.

To run the test,

    go test github.com/golang/mock/sample
glog
====

Leveled execution logs for Go.

This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package
	https://github.com/google/glog

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
- API declaration for Swagger UI ([go-restful-openapi](https://github.com/emicklei/go-restful-openapi), see [go-restful-swagger12](https://github.com/emicklei/go-restful-swagger12))
- Panic recovery to produce HTTP 500, customizable using RecoverHandler(...)
- Route errors produce HTTP 404/405/406/415 errors, customizable using ServiceErrorHandler(...)
- Configurable (trace) logging
- Customizable gzip/deflate readers and writers using CompressorProvider registration
	
### Resources

- [Example posted on blog](http://ernestmicklei.com/2012/11/go-restful-first-working-example/)
- [Design explained on blog](http://ernestmicklei.com/2012/11/go-restful-api-design/)
- [sourcegraph](https://sourcegraph.com/github.com/emicklei/go-restful)
- [showcase: Zazkia - tcp proxy for testing resiliency](https://github.com/emicklei/zazkia)
- [showcase: Mora - MongoDB REST Api server](https://github.com/emicklei/mora)

Type ```git shortlog -s``` for a full list of contributors.

© 2012 - 2017, http://ernestmicklei.com. MIT License. Contributions are welcome.
# go-restful-swagger12

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
go-difflib
==========

[![Build Status](https://travis-ci.org/pmezard/go-difflib.png?branch=master)](https://travis-ci.org/pmezard/go-difflib)
[![GoDoc](https://godoc.org/github.com/pmezard/go-difflib/difflib?status.svg)](https://godoc.org/github.com/pmezard/go-difflib/difflib)

Go-difflib is a partial port of python 3 difflib package. Its main goal
was to make unified and context diff available in pure Go, mostly for
testing purposes.

The following class and functions (and related tests) have be ported:

* `SequenceMatcher`
* `unified_diff()`
* `context_diff()`

## Installation

```bash
$ go get github.com/pmezard/go-difflib/difflib
```

### Quick Start

Diffs are configured with Unified (or ContextDiff) structures, and can
be output to an io.Writer or returned as a string.

```Go
diff := UnifiedDiff{
    A:        difflib.SplitLines("foo\nbar\n"),
    B:        difflib.SplitLines("foo\nbaz\n"),
    FromFile: "Original",
    ToFile:   "Current",
    Context:  3,
}
text, _ := GetUnifiedDiffString(diff)
fmt.Printf(text)
```

would output:

```
--- Original
+++ Current
@@ -1,3 +1,3 @@
 foo
-bar
+baz
```

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
  The simplest way is to run `go get -u github.com/golang/protobuf/protoc-gen-go`.
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
![Gomega: Ginkgo's Preferred Matcher Library](http://onsi.github.io/gomega/images/gomega.png)

[![Build Status](https://travis-ci.org/onsi/gomega.svg)](https://travis-ci.org/onsi/gomega)

Jump straight to the [docs](http://onsi.github.io/gomega/) to learn about Gomega, including a list of [all available matchers](http://onsi.github.io/gomega/#provided-matchers).

If you have a question, comment, bug report, feature request, etc. please open a GitHub issue.

## [Ginkgo](http://github.com/onsi/ginkgo): a BDD Testing Framework for Golang

Learn more about Ginkgo [here](http://onsi.github.io/ginkgo/)

## Community Matchers

A collection of community matchers is available on the [wiki](https://github.com/onsi/gomega/wiki).

## License

Gomega is MIT-Licensed

The `ConsistOf` matcher uses [goraph](https://github.com/amitkgupta/goraph) which is embedded in the source to simplify distribution.  goraph has an MIT license.
![Ginkgo: A Golang BDD Testing Framework](http://onsi.github.io/ginkgo/images/ginkgo.png)

[![Build Status](https://travis-ci.org/onsi/ginkgo.svg)](https://travis-ci.org/onsi/ginkgo)

Jump to the [docs](http://onsi.github.io/ginkgo/) to learn more.  To start rolling your Ginkgo tests *now* [keep reading](#set-me-up)!

If you have a question, comment, bug report, feature request, etc. please open a GitHub issue.

## Feature List

- Ginkgo uses Go's `testing` package and can live alongside your existing `testing` tests.  It's easy to [bootstrap](http://onsi.github.io/ginkgo/#bootstrapping-a-suite) and start writing your [first tests](http://onsi.github.io/ginkgo/#adding-specs-to-a-suite)

- Structure your BDD-style tests expressively:
    - Nestable [`Describe` and `Context` container blocks](http://onsi.github.io/ginkgo/#organizing-specs-with-containers-describe-and-context)
    - [`BeforeEach` and `AfterEach` blocks](http://onsi.github.io/ginkgo/#extracting-common-setup-beforeeach) for setup and teardown
    - [`It` blocks](http://onsi.github.io/ginkgo/#individual-specs-) that hold your assertions
    - [`JustBeforeEach` blocks](http://onsi.github.io/ginkgo/#separating-creation-and-configuration-justbeforeeach) that separate creation from configuration (also known as the subject action pattern).
    - [`BeforeSuite` and `AfterSuite` blocks](http://onsi.github.io/ginkgo/#global-setup-and-teardown-beforesuite-and-aftersuite) to prep for and cleanup after a suite.

- A comprehensive test runner that lets you:
    - Mark specs as [pending](http://onsi.github.io/ginkgo/#pending-specs)
    - [Focus](http://onsi.github.io/ginkgo/#focused-specs) individual specs, and groups of specs, either programmatically or on the command line
    - Run your tests in [random order](http://onsi.github.io/ginkgo/#spec-permutation), and then reuse random seeds to replicate the same order.
    - Break up your test suite into parallel processes for straightforward [test parallelization](http://onsi.github.io/ginkgo/#parallel-specs)

- `ginkgo`: a command line interface with plenty of handy command line arguments for [running your tests](http://onsi.github.io/ginkgo/#running-tests) and [generating](http://onsi.github.io/ginkgo/#generators) test files.  Here are a few choice examples:
    - `ginkgo -nodes=N` runs your tests in `N` parallel processes and print out coherent output in realtime
    - `ginkgo -cover` runs your tests using Golang's code coverage tool
    - `ginkgo convert` converts an XUnit-style `testing` package to a Ginkgo-style package
    - `ginkgo -focus="REGEXP"` and `ginkgo -skip="REGEXP"` allow you to specify a subset of tests to run via regular expression
    - `ginkgo -r` runs all tests suites under the current directory
    - `ginkgo -v` prints out identifying information for each tests just before it runs

    And much more: run `ginkgo help` for details!

    The `ginkgo` CLI is convenient, but purely optional -- Ginkgo works just fine with `go test`

- `ginkgo watch` [watches](https://onsi.github.io/ginkgo/#watching-for-changes) packages *and their dependencies* for changes, then reruns tests.  Run tests immediately as you develop!

- Built-in support for testing [asynchronicity](http://onsi.github.io/ginkgo/#asynchronous-tests)

- Built-in support for [benchmarking](http://onsi.github.io/ginkgo/#benchmark-tests) your code.  Control the number of benchmark samples as you gather runtimes and other, arbitrary, bits of numerical information about your code. 

- [Completions for Sublime Text](https://github.com/onsi/ginkgo-sublime-completions): just use [Package Control](https://sublime.wbond.net/) to install `Ginkgo Completions`.

- [Completions for VSCode](https://github.com/onsi/vscode-ginkgo): just use VSCode's extension installer to install `vscode-ginkgo`.

- Straightforward support for third-party testing libraries such as [Gomock](https://code.google.com/p/gomock/) and [Testify](https://github.com/stretchr/testify).  Check out the [docs](http://onsi.github.io/ginkgo/#third-party-integrations) for details.

- A modular architecture that lets you easily:
    - Write [custom reporters](http://onsi.github.io/ginkgo/#writing-custom-reporters) (for example, Ginkgo comes with a [JUnit XML reporter](http://onsi.github.io/ginkgo/#generating-junit-xml-output) and a TeamCity reporter).
    - [Adapt an existing matcher library (or write your own!)](http://onsi.github.io/ginkgo/#using-other-matcher-libraries) to work with Ginkgo

## [Gomega](http://github.com/onsi/gomega): Ginkgo's Preferred Matcher Library

Ginkgo is best paired with Gomega.  Learn more about Gomega [here](http://onsi.github.io/gomega/)

## [Agouti](http://github.com/sclevine/agouti): A Golang Acceptance Testing Framework

Agouti allows you run WebDriver integration tests.  Learn more about Agouti [here](http://agouti.org)

## Set Me Up!

You'll need Golang v1.3+ (Ubuntu users: you probably have Golang v1.0 -- you'll need to upgrade!)

```bash

go get github.com/onsi/ginkgo/ginkgo  # installs the ginkgo CLI
go get github.com/onsi/gomega         # fetches the matcher library

cd path/to/package/you/want/to/test

ginkgo bootstrap # set up a new ginkgo suite
ginkgo generate  # will create a sample test file.  edit this file and add your tests then...

go test # to run your tests

ginkgo  # also runs your tests

```

## I'm new to Go: What are my testing options?

Of course, I heartily recommend [Ginkgo](https://github.com/onsi/ginkgo) and [Gomega](https://github.com/onsi/gomega).  Both packages are seeing heavy, daily, production use on a number of projects and boast a mature and comprehensive feature-set.

With that said, it's great to know what your options are :)

### What Golang gives you out of the box

Testing is a first class citizen in Golang, however Go's built-in testing primitives are somewhat limited: The [testing](http://golang.org/pkg/testing) package provides basic XUnit style tests and no assertion library.

### Matcher libraries for Golang's XUnit style tests

A number of matcher libraries have been written to augment Go's built-in XUnit style tests.  Here are two that have gained traction:

- [testify](https://github.com/stretchr/testify)
- [gocheck](http://labix.org/gocheck)

You can also use Ginkgo's matcher library [Gomega](https://github.com/onsi/gomega) in [XUnit style tests](http://onsi.github.io/gomega/#using-gomega-with-golangs-xunitstyle-tests)

### BDD style testing frameworks

There are a handful of BDD-style testing frameworks written for Golang.  Here are a few:

- [Ginkgo](https://github.com/onsi/ginkgo) ;)
- [GoConvey](https://github.com/smartystreets/goconvey) 
- [Goblin](https://github.com/franela/goblin)
- [Mao](https://github.com/azer/mao)
- [Zen](https://github.com/pranavraja/zen)

Finally, @shageman has [put together](https://github.com/shageman/gotestit) a comprehensive comparison of golang testing libraries.

Go explore!

## License

Ginkgo is MIT-Licensed
## Colorize Windows

These packages are used for colorize on Windows and contributed by mattn.jp@gmail.com

  * go-colorable: <https://github.com/mattn/go-colorable>
  * go-isatty: <https://github.com/mattn/go-isatty>
# go-colorable

Colorable writer for windows.

For example, most of logger packages doesn't show colors on windows. (I know we can do it with ansicon. But I don't want.)
This package is possible to handle escape sequence for ansi color on windows.

## Too Bad!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/bad.png)


## So Good!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/good.png)

## Usage

```go
logrus.SetFormatter(&logrus.TextFormatter{ForceColors: true})
logrus.SetOutput(colorable.NewColorableStdout())

logrus.Info("succeeded")
logrus.Warn("not correct")
logrus.Error("something error")
logrus.Fatal("panic")
```

You can compile above code on non-windows OSs.

## Installation

```
$ go get github.com/mattn/go-colorable
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)
# go-isatty

isatty for golang

## Usage

```go
package main

import (
	"fmt"
	"github.com/mattn/go-isatty"
	"os"
)

func main() {
	if isatty.IsTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Terminal")
	} else {
		fmt.Println("Is Not Terminal")
	}
}
```

## Installation

```
$ go get github.com/mattn/go-isatty
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)
# mapstructure [![Godoc](https://godoc.org/github.com/mitchell/mapstructure?status.svg)](https://godoc.org/github.com/mitchell/mapstructure)

mapstructure is a Go library for decoding generic map values to structures
and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't _quite_ know the structure of the underlying data
until you read a part of it. You can therefore read a `map[string]interface{}`
and use this library to decode it into the proper underlying native Go
structure.

## Installation

Standard `go get`:

```
$ go get github.com/mitchellh/mapstructure
```

## Usage & Example

For usage and examples see the [Godoc](http://godoc.org/github.com/mitchellh/mapstructure).

The `Decode` function has examples associated with it there.

## But Why?!

Go offers fantastic standard libraries for decoding formats such as JSON.
The standard method is to have a struct pre-created, and populate that struct
from the bytes of the encoded format. This is great, but the problem is if
you have configuration or an encoding that changes slightly depending on
specific fields. For example, consider this JSON:

```json
{
  "type": "person",
  "name": "Mitchell"
}
```

Perhaps we can't populate a specific structure without first reading
the "type" field from the JSON. We could always do two passes over the
decoding of the JSON (reading the "type" first, and the rest later).
However, it is much simpler to just decode this into a `map[string]interface{}`
structure, read the "type" key, then use something like this library
to decode it into the proper structure.
Testify - Thou Shalt Write Tests
================================

[![Build Status](https://travis-ci.org/stretchr/testify.svg)](https://travis-ci.org/stretchr/testify) [![Go Report Card](https://goreportcard.com/badge/github.com/stretchr/testify)](https://goreportcard.com/report/github.com/stretchr/testify) [![GoDoc](https://godoc.org/github.com/stretchr/testify?status.svg)](https://godoc.org/github.com/stretchr/testify)

Go code (golang) set of packages that provide many tools for testifying that your code will behave as you intend.

Features include:

  * [Easy assertions](#assert-package)
  * [Mocking](#mock-package)
  * [HTTP response trapping](#http-package)
  * [Testing suite interfaces and functions](#suite-package)

Get started:

  * Install testify with [one line of code](#installation), or [update it with another](#staying-up-to-date)
  * For an introduction to writing test code in Go, see http://golang.org/doc/code.html#Testing
  * Check out the API Documentation http://godoc.org/github.com/stretchr/testify
  * To make your testing life easier, check out our other project, [gorc](http://github.com/stretchr/gorc)
  * A little about [Test-Driven Development (TDD)](http://en.wikipedia.org/wiki/Test-driven_development)



[`assert`](http://godoc.org/github.com/stretchr/testify/assert "API documentation") package
-------------------------------------------------------------------------------------------

The `assert` package provides some helpful methods that allow you to write better test code in Go.

  * Prints friendly, easy to read failure descriptions
  * Allows for very readable code
  * Optionally annotate each assertion with a message

See it in action:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {

  // assert equality
  assert.Equal(t, 123, 123, "they should be equal")

  // assert inequality
  assert.NotEqual(t, 123, 456, "they should not be equal")

  // assert for nil (good for errors)
  assert.Nil(t, object)

  // assert for not nil (good when you expect something)
  if assert.NotNil(t, object) {

    // now we know that object isn't nil, we are safe to make
    // further assertions without causing any errors
    assert.Equal(t, "Something", object.Value)

  }

}
```

  * Every assert func takes the `testing.T` object as the first argument.  This is how it writes the errors out through the normal `go test` capabilities.
  * Every assert func returns a bool indicating whether the assertion was successful or not, this is useful for if you want to go on making further assertions under certain conditions.

if you assert many times, use the below:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
  assert := assert.New(t)

  // assert equality
  assert.Equal(123, 123, "they should be equal")

  // assert inequality
  assert.NotEqual(123, 456, "they should not be equal")

  // assert for nil (good for errors)
  assert.Nil(object)

  // assert for not nil (good when you expect something)
  if assert.NotNil(object) {

    // now we know that object isn't nil, we are safe to make
    // further assertions without causing any errors
    assert.Equal("Something", object.Value)
  }
}
```

[`require`](http://godoc.org/github.com/stretchr/testify/require "API documentation") package
---------------------------------------------------------------------------------------------

The `require` package provides same global functions as the `assert` package, but instead of returning a boolean result they terminate current test.

See [t.FailNow](http://golang.org/pkg/testing/#T.FailNow) for details.


[`http`](http://godoc.org/github.com/stretchr/testify/http "API documentation") package
---------------------------------------------------------------------------------------

The `http` package contains test objects useful for testing code that relies on the `net/http` package.  Check out the [(deprecated) API documentation for the `http` package](http://godoc.org/github.com/stretchr/testify/http).

We recommend you use [httptest](http://golang.org/pkg/net/http/httptest) instead.

[`mock`](http://godoc.org/github.com/stretchr/testify/mock "API documentation") package
----------------------------------------------------------------------------------------

The `mock` package provides a mechanism for easily writing mock objects that can be used in place of real objects when writing test code.

An example test function that tests a piece of code that relies on an external object `testObj`, can setup expectations (testify) and assert that they indeed happened:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/mock"
)

/*
  Test objects
*/

// MyMockedObject is a mocked object that implements an interface
// that describes an object that the code I am testing relies on.
type MyMockedObject struct{
  mock.Mock
}

// DoSomething is a method on MyMockedObject that implements some interface
// and just records the activity, and returns what the Mock object tells it to.
//
// In the real object, this method would do something useful, but since this
// is a mocked object - we're just going to stub it out.
//
// NOTE: This method is not being tested here, code that uses this object is.
func (m *MyMockedObject) DoSomething(number int) (bool, error) {

  args := m.Called(number)
  return args.Bool(0), args.Error(1)

}

/*
  Actual test functions
*/

// TestSomething is an example of how to use our test object to
// make assertions about some target code we are testing.
func TestSomething(t *testing.T) {

  // create an instance of our test object
  testObj := new(MyMockedObject)

  // setup expectations
  testObj.On("DoSomething", 123).Return(true, nil)

  // call the code we are testing
  targetFuncThatDoesSomethingWithObj(testObj)

  // assert that the expectations were met
  testObj.AssertExpectations(t)

}
```

For more information on how to write mock code, check out the [API documentation for the `mock` package](http://godoc.org/github.com/stretchr/testify/mock).

You can use the [mockery tool](http://github.com/vektra/mockery) to autogenerate the mock code against an interface as well, making using mocks much quicker.

[`suite`](http://godoc.org/github.com/stretchr/testify/suite "API documentation") package
-----------------------------------------------------------------------------------------

The `suite` package provides functionality that you might be used to from more common object oriented languages.  With it, you can build a testing suite as a struct, build setup/teardown methods and testing methods on your struct, and run them with 'go test' as per normal.

An example suite is shown below:

```go
// Basic imports
import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/suite"
)

// Define the suite, and absorb the built-in basic suite
// functionality from testify - including a T() method which
// returns the current testing context
type ExampleTestSuite struct {
    suite.Suite
    VariableThatShouldStartAtFive int
}

// Make sure that VariableThatShouldStartAtFive is set to five
// before each test
func (suite *ExampleTestSuite) SetupTest() {
    suite.VariableThatShouldStartAtFive = 5
}

// All methods that begin with "Test" are run as tests within a
// suite.
func (suite *ExampleTestSuite) TestExample() {
    assert.Equal(suite.T(), 5, suite.VariableThatShouldStartAtFive)
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestExampleTestSuite(t *testing.T) {
    suite.Run(t, new(ExampleTestSuite))
}
```

For a more complete example, using all of the functionality provided by the suite package, look at our [example testing suite](https://github.com/stretchr/testify/blob/master/suite/suite_test.go)

For more information on writing suites, check out the [API documentation for the `suite` package](http://godoc.org/github.com/stretchr/testify/suite).

`Suite` object has assertion methods:

```go
// Basic imports
import (
    "testing"
    "github.com/stretchr/testify/suite"
)

// Define the suite, and absorb the built-in basic suite
// functionality from testify - including assertion methods.
type ExampleTestSuite struct {
    suite.Suite
    VariableThatShouldStartAtFive int
}

// Make sure that VariableThatShouldStartAtFive is set to five
// before each test
func (suite *ExampleTestSuite) SetupTest() {
    suite.VariableThatShouldStartAtFive = 5
}

// All methods that begin with "Test" are run as tests within a
// suite.
func (suite *ExampleTestSuite) TestExample() {
    suite.Equal(suite.VariableThatShouldStartAtFive, 5)
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestExampleTestSuite(t *testing.T) {
    suite.Run(t, new(ExampleTestSuite))
}
```

------

Installation
============

To install Testify, use `go get`:

    * Latest version: go get github.com/stretchr/testify
    * Specific version: go get gopkg.in/stretchr/testify.v1

This will then make the following packages available to you:

    github.com/stretchr/testify/assert
    github.com/stretchr/testify/mock
    github.com/stretchr/testify/http

Import the `testify/assert` package into your code using this template:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {

  assert.True(t, true, "True is true!")

}
```

------

Staying up to date
==================

To update Testify to the latest version, use `go get -u github.com/stretchr/testify`.

------

Version History
===============

   * 1.0 - New package versioning strategy adopted.

------

Contributing
============

Please feel free to submit issues, fork the repository and send pull requests!

When submitting an issue, we ask that you please include a complete test function that demonstrates the issue.  Extra credit for those using Testify to write the test code that demonstrates it.

------

Licence
=======
Copyright (c) 2012 - 2013 Mat Ryer and Tyler Bunnell

Please consider promoting this project if you find it useful.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/sirupsen/logrus.svg?branch=master)](https://travis-ci.org/sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/sirupsen/logrus?status.svg)](https://godoc.org/github.com/sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger.

**Seeing weird case-sensitive problems?** It's in the past been possible to
import Logrus as both upper- and lower-case. Due to the Go package environment,
this caused issues in the community and we needed a standard. Some environments
experienced problems with the upper-case variant, so the lower-case was decided.
Everything using `logrus` will need to use the lower-case:
`github.com/sirupsen/logrus`. Any package that isn't, should be changed.

To fix Glide, see [these
comments](https://github.com/sirupsen/logrus/issues/553#issuecomment-306591437).
For an in-depth explanation of the casing issue, see [this
comment](https://github.com/sirupsen/logrus/issues/570#issuecomment-313933276).

**Are you interested in assisting in maintaining Logrus?** Currently I have a
lot of obligations, and I am unable to provide Logrus with the maintainership it
needs. If you'd like to help, please reach out to me at `simon at author's
username dot com`.

Nicely color-coded in development (when a TTY is attached, otherwise just
plain text):

![Colored](http://i.imgur.com/PY7qMwd.png)

With `log.SetFormatter(&log.JSONFormatter{})`, for easy parsing by logstash
or Splunk:

```json
{"animal":"walrus","level":"info","msg":"A group of walrus emerges from the
ocean","size":10,"time":"2014-03-10 19:57:38.562264131 -0400 EDT"}

{"level":"warning","msg":"The group's number increased tremendously!",
"number":122,"omg":true,"time":"2014-03-10 19:57:38.562471297 -0400 EDT"}

{"animal":"walrus","level":"info","msg":"A giant walrus appears!",
"size":10,"time":"2014-03-10 19:57:38.562500591 -0400 EDT"}

{"animal":"walrus","level":"info","msg":"Tremendously sized cow enters the ocean.",
"size":9,"time":"2014-03-10 19:57:38.562527896 -0400 EDT"}

{"level":"fatal","msg":"The ice breaks!","number":100,"omg":true,
"time":"2014-03-10 19:57:38.562543128 -0400 EDT"}
```

With the default `log.SetFormatter(&log.TextFormatter{})` when a TTY is not
attached, the output is compatible with the
[logfmt](http://godoc.org/github.com/kr/logfmt) format:

```text
time="2015-03-26T01:27:38-04:00" level=debug msg="Started observing beach" animal=walrus number=8
time="2015-03-26T01:27:38-04:00" level=info msg="A group of walrus emerges from the ocean" animal=walrus size=10
time="2015-03-26T01:27:38-04:00" level=warning msg="The group's number increased tremendously!" number=122 omg=true
time="2015-03-26T01:27:38-04:00" level=debug msg="Temperature changes" temperature=-4
time="2015-03-26T01:27:38-04:00" level=panic msg="It's over 9000!" animal=orca size=9009
time="2015-03-26T01:27:38-04:00" level=fatal msg="The ice breaks!" err=&{0x2082280c0 map[animal:orca size:9009] 2015-03-26 01:27:38.441574009 -0400 EDT panic It's over 9000!} number=100 omg=true
exit status 1
```

#### Case-sensitivity

The organization's name was changed to lower-case--and this will not be changed
back. If you are getting import conflicts due to case sensitivity, please use
the lower-case import: `github.com/sirupsen/logrus`.

#### Example

The simplest way to use Logrus is simply the package-level exported logger:

```go
package main

import (
  log "github.com/sirupsen/logrus"
)

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
  }).Info("A walrus appears")
}
```

Note that it's completely api-compatible with the stdlib logger, so you can
replace your `log` imports everywhere with `log "github.com/sirupsen/logrus"`
and you'll now have the flexibility of Logrus. You can customize it all you
want:

```go
package main

import (
  "os"
  log "github.com/sirupsen/logrus"
)

func init() {
  // Log as JSON instead of the default ASCII formatter.
  log.SetFormatter(&log.JSONFormatter{})

  // Output to stdout instead of the default stderr
  // Can be any io.Writer, see below for File example
  log.SetOutput(os.Stdout)

  // Only log the warning severity or above.
  log.SetLevel(log.WarnLevel)
}

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")

  log.WithFields(log.Fields{
    "omg":    true,
    "number": 122,
  }).Warn("The group's number increased tremendously!")

  log.WithFields(log.Fields{
    "omg":    true,
    "number": 100,
  }).Fatal("The ice breaks!")

  // A common pattern is to re-use fields between logging statements by re-using
  // the logrus.Entry returned from WithFields()
  contextLogger := log.WithFields(log.Fields{
    "common": "this is a common field",
    "other": "I also should be logged always",
  })

  contextLogger.Info("I'll be logged with common and other field")
  contextLogger.Info("Me too")
}
```

For more advanced usage such as logging to multiple locations from the same
application, you can also create an instance of the `logrus` Logger:

```go
package main

import (
  "os"
  "github.com/sirupsen/logrus"
)

// Create a new instance of the logger. You can have any number of instances.
var log = logrus.New()

func main() {
  // The API for setting attributes is a little different than the package level
  // exported logger. See Godoc.
  log.Out = os.Stdout

  // You could set this to any `io.Writer` such as a file
  // file, err := os.OpenFile("logrus.log", os.O_CREATE|os.O_WRONLY, 0666)
  // if err == nil {
  //  log.Out = file
  // } else {
  //  log.Info("Failed to log to file, using default stderr")
  // }

  log.WithFields(logrus.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")
}
```

#### Fields

Logrus encourages careful, structured logging through logging fields instead of
long, unparseable error messages. For example, instead of: `log.Fatalf("Failed
to send event %s to topic %s with key %d")`, you should log the much more
discoverable:

```go
log.WithFields(log.Fields{
  "event": event,
  "topic": topic,
  "key": key,
}).Fatal("Failed to send event")
```

We've found this API forces you to think about logging in a way that produces
much more useful logging messages. We've been in countless situations where just
a single added field to a log statement that was already there would've saved us
hours. The `WithFields` call is optional.

In general, with Logrus using any of the `printf`-family functions should be
seen as a hint you should add a field, however, you can still use the
`printf`-family functions with Logrus.

#### Default Fields

Often it's helpful to have fields _always_ attached to log statements in an
application or parts of one. For example, you may want to always log the
`request_id` and `user_ip` in the context of a request. Instead of writing
`log.WithFields(log.Fields{"request_id": request_id, "user_ip": user_ip})` on
every line, you can create a `logrus.Entry` to pass around instead:

```go
requestLogger := log.WithFields(log.Fields{"request_id": request_id, "user_ip": user_ip})
requestLogger.Info("something happened on that request") # will log request_id and user_ip
requestLogger.Warn("something not great happened")
```

#### Hooks

You can add hooks for logging levels. For example to send errors to an exception
tracking service on `Error`, `Fatal` and `Panic`, info to StatsD or log to
multiple places simultaneously, e.g. syslog.

Logrus comes with [built-in hooks](hooks/). Add those, or your custom hook, in
`init`:

```go
import (
  log "github.com/sirupsen/logrus"
  "gopkg.in/gemnasium/logrus-airbrake-hook.v2" // the package is named "aibrake"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
  "log/syslog"
)

func init() {

  // Use the Airbrake hook to report errors that have Error severity or above to
  // an exception tracker. You can create custom hooks, see the Hooks section.
  log.AddHook(airbrake.NewHook(123, "xyz", "production"))

  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")
  if err != nil {
    log.Error("Unable to connect to local syslog daemon")
  } else {
    log.AddHook(hook)
  }
}
```
Note: Syslog hook also support connecting to local syslog (Ex. "/dev/log" or "/var/run/syslog" or "/var/run/log"). For the detail, please check the [syslog hook README](hooks/syslog/README.md).

| Hook  | Description |
| ----- | ----------- |
| [Airbrake "legacy"](https://github.com/gemnasium/logrus-airbrake-legacy-hook) | Send errors to an exception tracking service compatible with the Airbrake API V2. Uses [`airbrake-go`](https://github.com/tobi/airbrake-go) behind the scenes. |
| [Airbrake](https://github.com/gemnasium/logrus-airbrake-hook) | Send errors to the Airbrake API V3. Uses the official [`gobrake`](https://github.com/airbrake/gobrake) behind the scenes. |
| [Amazon Kinesis](https://github.com/evalphobia/logrus_kinesis) | Hook for logging to [Amazon Kinesis](https://aws.amazon.com/kinesis/) |
| [Amqp-Hook](https://github.com/vladoatanasov/logrus_amqp) | Hook for logging to Amqp broker (Like RabbitMQ) |
| [AzureTableHook](https://github.com/kpfaulkner/azuretablehook/) | Hook for logging to Azure Table Storage|
| [Bugsnag](https://github.com/Shopify/logrus-bugsnag/blob/master/bugsnag.go) | Send errors to the Bugsnag exception tracking service. |
| [DeferPanic](https://github.com/deferpanic/dp-logrus) | Hook for logging to DeferPanic |
| [Discordrus](https://github.com/kz/discordrus) | Hook for logging to [Discord](https://discordapp.com/) |
| [ElasticSearch](https://github.com/sohlich/elogrus) | Hook for logging to ElasticSearch|
| [Firehose](https://github.com/beaubrewer/logrus_firehose) | Hook for logging to [Amazon Firehose](https://aws.amazon.com/kinesis/firehose/)
| [Fluentd](https://github.com/evalphobia/logrus_fluent) | Hook for logging to fluentd |
| [Go-Slack](https://github.com/multiplay/go-slack) | Hook for logging to [Slack](https://slack.com) |
| [Graylog](https://github.com/gemnasium/logrus-graylog-hook) | Hook for logging to [Graylog](http://graylog2.org/) |
| [Hiprus](https://github.com/nubo/hiprus) | Send errors to a channel in hipchat. |
| [Honeybadger](https://github.com/agonzalezro/logrus_honeybadger) | Hook for sending exceptions to Honeybadger |
| [InfluxDB](https://github.com/Abramovic/logrus_influxdb) | Hook for logging to influxdb |
| [Influxus](http://github.com/vlad-doru/influxus) | Hook for concurrently logging to [InfluxDB](http://influxdata.com/) |
| [Journalhook](https://github.com/wercker/journalhook) | Hook for logging to `systemd-journald` |
| [KafkaLogrus](https://github.com/tracer0tong/kafkalogrus) | Hook for logging to Kafka |
| [LFShook](https://github.com/rifflock/lfshook) | Hook for logging to the local filesystem |
| [Logbeat](https://github.com/macandmia/logbeat) | Hook for logging to [Opbeat](https://opbeat.com/) |
| [Logentries](https://github.com/jcftang/logentriesrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logentrus](https://github.com/puddingfactory/logentrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [Mail](https://github.com/zbindenren/logrus_mail) | Hook for sending exceptions via mail |
| [Mattermost](https://github.com/shuLhan/mattermost-integration/tree/master/hooks/logrus) | Hook for logging to [Mattermost](https://mattermost.com/) |
| [Mongodb](https://github.com/weekface/mgorus) | Hook for logging to mongodb |
| [NATS-Hook](https://github.com/rybit/nats_logrus_hook) | Hook for logging to [NATS](https://nats.io) |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [Papertrail](https://github.com/polds/logrus-papertrail-hook) | Send errors to the [Papertrail](https://papertrailapp.com) hosted logging service via UDP. |
| [PostgreSQL](https://github.com/gemnasium/logrus-postgresql-hook) | Send logs to [PostgreSQL](http://postgresql.org) |
| [Promrus](https://github.com/weaveworks/promrus) | Expose number of log messages as [Prometheus](https://prometheus.io/) metrics |
| [Pushover](https://github.com/toorop/logrus_pushover) | Send error via [Pushover](https://pushover.net) |
| [Raygun](https://github.com/squirkle/logrus-raygun-hook) | Hook for logging to [Raygun.io](http://raygun.io/) |
| [Redis-Hook](https://github.com/rogierlommers/logrus-redis-hook) | Hook for logging to a ELK stack (through Redis) |
| [Rollrus](https://github.com/heroku/rollrus) | Hook for sending errors to rollbar |
| [Scribe](https://github.com/sagar8192/logrus-scribe-hook) | Hook for logging to [Scribe](https://github.com/facebookarchive/scribe)|
| [Sentry](https://github.com/evalphobia/logrus_sentry) | Send errors to the Sentry error logging and aggregation service. |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Stackdriver](https://github.com/knq/sdhook) | Hook for logging to [Google Stackdriver](https://cloud.google.com/logging/) |
| [Sumorus](https://github.com/doublefree/sumorus) | Hook for logging to [SumoLogic](https://www.sumologic.com/)|
| [Syslog](https://github.com/sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [Syslog TLS](https://github.com/shinji62/logrus-syslog-ng) | Send errors to remote syslog server with TLS support. |
| [Telegram](https://github.com/rossmcdonald/telegram_hook) | Hook for logging errors to [Telegram](https://telegram.org/) |
| [TraceView](https://github.com/evalphobia/logrus_appneta) | Hook for logging to [AppNeta TraceView](https://www.appneta.com/products/traceview/) |
| [Typetalk](https://github.com/dragon3/logrus-typetalk-hook) | Hook for logging to [Typetalk](https://www.typetalk.in/) |
| [logz.io](https://github.com/ripcurld00d/logrus-logzio-hook) | Hook for logging to [logz.io](https://logz.io), a Log as a Service using Logstash |
| [SQS-Hook](https://github.com/tsarpaul/logrus_sqs) | Hook for logging to [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) |

#### Level logging

Logrus has six logging levels: Debug, Info, Warning, Error, Fatal and Panic.

```go
log.Debug("Useful debugging information.")
log.Info("Something noteworthy happened!")
log.Warn("You should probably take a look at this.")
log.Error("Something failed but I'm not quitting.")
// Calls os.Exit(1) after logging
log.Fatal("Bye.")
// Calls panic() after logging
log.Panic("I'm bailing.")
```

You can set the logging level on a `Logger`, then it will only log entries with
that severity or anything above it:

```go
// Will log anything that is info or above (warn, error, fatal, panic). Default.
log.SetLevel(log.InfoLevel)
```

It may be useful to set `log.Level = logrus.DebugLevel` in a debug or verbose
environment if your application has that.

#### Entries

Besides the fields added with `WithField` or `WithFields` some fields are
automatically added to all logging events:

1. `time`. The timestamp when the entry was created.
2. `msg`. The logging message passed to `{Info,Warn,Error,Fatal,Panic}` after
   the `AddFields` call. E.g. `Failed to send event.`
3. `level`. The logging level. E.g. `info`.

#### Environments

Logrus has no notion of environment.

If you wish for hooks and formatters to only be used in specific environments,
you should handle that yourself. For example, if your application has a global
variable `Environment`, which is a string representation of the environment you
could do:

```go
import (
  log "github.com/sirupsen/logrus"
)

init() {
  // do something here to set environment depending on an environment variable
  // or command-line flag
  if Environment == "production" {
    log.SetFormatter(&log.JSONFormatter{})
  } else {
    // The TextFormatter is default, you don't actually have to do this.
    log.SetFormatter(&log.TextFormatter{})
  }
}
```

This configuration is how `logrus` was intended to be used, but JSON in
production is mostly only useful if you do log aggregation with tools like
Splunk or Logstash.

#### Formatters

The built-in logging formatters are:

* `logrus.TextFormatter`. Logs the event in colors if stdout is a tty, otherwise
  without colors.
  * *Note:* to force colored output when there is no TTY, set the `ForceColors`
    field to `true`.  To force no colored output even if there is a TTY  set the
    `DisableColors` field to `true`. For Windows, see
    [github.com/mattn/go-colorable](https://github.com/mattn/go-colorable).
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#TextFormatter).
* `logrus.JSONFormatter`. Logs fields as JSON.
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#JSONFormatter).

Third party logging formatters:

* [`FluentdFormatter`](https://github.com/joonix/log). Formats entries that can be parsed by Kubernetes and Google Container Engine.
* [`logstash`](https://github.com/bshuster-repo/logrus-logstash-hook). Logs fields as [Logstash](http://logstash.net) Events.
* [`prefixed`](https://github.com/x-cray/logrus-prefixed-formatter). Displays log entry source along with alternative layout.
* [`zalgo`](https://github.com/aybabtme/logzalgo). Invoking the P͉̫o̳̼̊w̖͈̰͎e̬͔̭͂r͚̼̹̲ ̫͓͉̳͈ō̠͕͖̚f̝͍̠ ͕̲̞͖͑Z̖̫̤̫ͪa͉̬͈̗l͖͎g̳̥o̰̥̅!̣͔̲̻͊̄ ̙̘̦̹̦.

You can define your formatter by implementing the `Formatter` interface,
requiring a `Format` method. `Format` takes an `*Entry`. `entry.Data` is a
`Fields` type (`map[string]interface{}`) with all your fields as well as the
default ones (see Entries section above):

```go
type MyJSONFormatter struct {
}

log.SetFormatter(new(MyJSONFormatter))

func (f *MyJSONFormatter) Format(entry *Entry) ([]byte, error) {
  // Note this doesn't include Time, Level and Message which are available on
  // the Entry. Consult `godoc` on information about those fields or read the
  // source of the official loggers.
  serialized, err := json.Marshal(entry.Data)
    if err != nil {
      return nil, fmt.Errorf("Failed to marshal fields to JSON, %v", err)
    }
  return append(serialized, '\n'), nil
}
```

#### Logger as an `io.Writer`

Logrus can be transformed into an `io.Writer`. That writer is the end of an `io.Pipe` and it is your responsibility to close it.

```go
w := logger.Writer()
defer w.Close()

srv := http.Server{
    // create a stdlib log.Logger that writes to
    // logrus.Logger.
    ErrorLog: log.New(w, "", 0),
}
```

Each line written to that writer will be printed the usual way, using formatters
and hooks. The level for those entries is `info`.

This means that we can override the standard library logger easily:

```go
logger := logrus.New()
logger.Formatter = &logrus.JSONFormatter{}

// Use logrus for standard log output
// Note that `log` here references stdlib's log
// Not logrus imported under the name `log`.
log.SetOutput(logger.Writer())
```

#### Rotation

Log rotation is not provided with Logrus. Log rotation should be done by an
external program (like `logrotate(8)`) that can compress and delete old log
entries. It should not be a feature of the application-level logger.

#### Tools

| Tool | Description |
| ---- | ----------- |
|[Logrus Mate](https://github.com/gogap/logrus_mate)|Logrus mate is a tool for Logrus to manage loggers, you can initial logger's level, hook and formatter by config file, the logger will generated with different config at different environment.|
|[Logrus Viper Helper](https://github.com/heirko/go-contrib/tree/master/logrusHelper)|An Helper around Logrus to wrap with spf13/Viper to load configuration with fangs! And to simplify Logrus configuration use some behavior of [Logrus Mate](https://github.com/gogap/logrus_mate). [sample](https://github.com/heirko/iris-contrib/blob/master/middleware/logrus-logger/example) |

#### Testing

Logrus has a built in facility for asserting the presence of log messages. This is implemented through the `test` hook and provides:

* decorators for existing logger (`test.NewLocal` and `test.NewGlobal`) which basically just add the `test` hook
* a test logger (`test.NewNullLogger`) that just records log messages (and does not output any):

```go
import(
  "github.com/sirupsen/logrus"
  "github.com/sirupsen/logrus/hooks/test"
  "github.com/stretchr/testify/assert"
  "testing"
)

func TestSomething(t*testing.T){
  logger, hook := test.NewNullLogger()
  logger.Error("Helloerror")

  assert.Equal(t, 1, len(hook.Entries))
  assert.Equal(t, logrus.ErrorLevel, hook.LastEntry().Level)
  assert.Equal(t, "Helloerror", hook.LastEntry().Message)

  hook.Reset()
  assert.Nil(t, hook.LastEntry())
}
```

#### Fatal handlers

Logrus can register one or more functions that will be called when any `fatal`
level message is logged. The registered handlers will be executed before
logrus performs a `os.Exit(1)`. This behavior may be helpful if callers need
to gracefully shutdown. Unlike a `panic("Something went wrong...")` call which can be intercepted with a deferred `recover` a call to `os.Exit(1)` can not be intercepted.

```
...
handler := func() {
  // gracefully shutdown something...
}
logrus.RegisterExitHandler(handler)
...
```

#### Thread safety

By default Logger is protected by mutex for concurrent writes, this mutex is invoked when calling hooks and writing logs.
If you are sure such locking is not needed, you can call logger.SetNoLock() to disable the locking.

Situation when locking is not needed includes:

* You have no hooks registered, or hooks calling is already thread-safe.

* Writing to logger.Out is already thread-safe, for example:

  1) logger.Out is protected by locks.

  2) logger.Out is a os.File handler opened with `O_APPEND` flag, and every write is smaller than 4k. (This allow multi-thread/multi-process writing)

     (Refer to http://www.notthewizard.com/2014/06/17/are-files-appends-really-atomic/)
# Syslog Hooks for Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>

## Usage

```go
import (
  "log/syslog"
  "github.com/sirupsen/logrus"
  lSyslog "github.com/sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := lSyslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```

If you want to connect to local syslog (Ex. "/dev/log" or "/var/run/syslog" or "/var/run/log"). Just assign empty string to the first two parameters of `NewSyslogHook`. It should look like the following.

```go
import (
  "log/syslog"
  "github.com/sirupsen/logrus"
  lSyslog "github.com/sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := lSyslog.NewSyslogHook("", "", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```
# YAML marshaling and unmarshaling support for Go

[![Build Status](https://travis-ci.org/ghodss/yaml.svg)](https://travis-ci.org/ghodss/yaml)

## Introduction

A wrapper around [go-yaml](https://github.com/go-yaml/yaml) designed to enable a better way of handling YAML when marshaling to and from structs.

In short, this library first converts YAML to JSON using go-yaml and then uses `json.Marshal` and `json.Unmarshal` to convert to or from the struct. This means that it effectively reuses the JSON struct tags as well as the custom JSON methods `MarshalJSON` and `UnmarshalJSON` unlike go-yaml. For a detailed overview of the rationale behind this method, [see this blog post](http://ghodss.com/2014/the-right-way-to-handle-yaml-in-golang/).

## Compatibility

This package uses [go-yaml](https://github.com/go-yaml/yaml) and therefore supports [everything go-yaml supports](https://github.com/go-yaml/yaml#compatibility).

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
package main

import (
	"fmt"

	"github.com/ghodss/yaml"
)

type Person struct {
	Name string `json:"name"` // Affects YAML field names too.
	Age  int    `json:"age"`
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
	age: 30
	name: John
	*/

	// Unmarshal the YAML back into a Person struct.
	var p2 Person
	err = yaml.Unmarshal(y, &p2)
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
package main

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
govalidator
===========
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/asaskevich/govalidator?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![GoDoc](https://godoc.org/github.com/asaskevich/govalidator?status.png)](https://godoc.org/github.com/asaskevich/govalidator) [![Coverage Status](https://img.shields.io/coveralls/asaskevich/govalidator.svg)](https://coveralls.io/r/asaskevich/govalidator?branch=master) [![wercker status](https://app.wercker.com/status/1ec990b09ea86c910d5f08b0e02c6043/s "wercker status")](https://app.wercker.com/project/bykey/1ec990b09ea86c910d5f08b0e02c6043)
[![Build Status](https://travis-ci.org/asaskevich/govalidator.svg?branch=master)](https://travis-ci.org/asaskevich/govalidator) [![Go Report Card](https://goreportcard.com/badge/github.com/asaskevich/govalidator)](https://goreportcard.com/report/github.com/asaskevich/govalidator) [![GoSearch](http://go-search.org/badge?id=github.com%2Fasaskevich%2Fgovalidator)](http://go-search.org/view?id=github.com%2Fasaskevich%2Fgovalidator)

A package of validators and sanitizers for strings, structs and collections. Based on [validator.js](https://github.com/chriso/validator.js).

#### Installation
Make sure that Go is installed on your computer.
Type the following command in your terminal:

	go get github.com/asaskevich/govalidator

or you can get specified release of the package with `gopkg.in`:

	go get gopkg.in/asaskevich/govalidator.v4

After it the package is ready to use.


#### Import package in your project
Add following line in your `*.go` file:
```go
import "github.com/asaskevich/govalidator"
```
If you are unhappy to use long `govalidator`, you can do something like this:
```go
import (
  valid "github.com/asaskevich/govalidator"
)
```

#### Activate behavior to require all fields have a validation tag by default
`SetFieldsRequiredByDefault` causes validation to fail when struct fields do not include validations or are not explicitly marked as exempt (using `valid:"-"` or `valid:"email,optional"`). A good place to activate this is a package init function or the main() function.

```go
import "github.com/asaskevich/govalidator"

func init() {
  govalidator.SetFieldsRequiredByDefault(true)
}
```

Here's some code to explain it:
```go
// this struct definition will fail govalidator.ValidateStruct() (and the field values do not matter):
type exampleStruct struct {
  Name  string ``
  Email string `valid:"email"`
}

// this, however, will only fail when Email is empty or an invalid email address:
type exampleStruct2 struct {
  Name  string `valid:"-"`
  Email string `valid:"email"`
}

// lastly, this will only fail when Email is an invalid email address but not when it's empty:
type exampleStruct2 struct {
  Name  string `valid:"-"`
  Email string `valid:"email,optional"`
}
```

#### Recent breaking changes (see [#123](https://github.com/asaskevich/govalidator/pull/123))
##### Custom validator function signature
A context was added as the second parameter, for structs this is the object being validated – this makes dependent validation possible.
```go
import "github.com/asaskevich/govalidator"

// old signature
func(i interface{}) bool

// new signature
func(i interface{}, o interface{}) bool
```

##### Adding a custom validator
This was changed to prevent data races when accessing custom validators.
```go
import "github.com/asaskevich/govalidator"

// before
govalidator.CustomTypeTagMap["customByteArrayValidator"] = CustomTypeValidator(func(i interface{}, o interface{}) bool {
  // ...
})

// after
govalidator.CustomTypeTagMap.Set("customByteArrayValidator", CustomTypeValidator(func(i interface{}, o interface{}) bool {
  // ...
}))
```

#### List of functions:
```go
func Abs(value float64) float64
func BlackList(str, chars string) string
func ByteLength(str string, params ...string) bool
func CamelCaseToUnderscore(str string) string
func Contains(str, substring string) bool
func Count(array []interface{}, iterator ConditionIterator) int
func Each(array []interface{}, iterator Iterator)
func ErrorByField(e error, field string) string
func ErrorsByField(e error) map[string]string
func Filter(array []interface{}, iterator ConditionIterator) []interface{}
func Find(array []interface{}, iterator ConditionIterator) interface{}
func GetLine(s string, index int) (string, error)
func GetLines(s string) []string
func InRange(value, left, right float64) bool
func IsASCII(str string) bool
func IsAlpha(str string) bool
func IsAlphanumeric(str string) bool
func IsBase64(str string) bool
func IsByteLength(str string, min, max int) bool
func IsCIDR(str string) bool
func IsCreditCard(str string) bool
func IsDNSName(str string) bool
func IsDataURI(str string) bool
func IsDialString(str string) bool
func IsDivisibleBy(str, num string) bool
func IsEmail(str string) bool
func IsFilePath(str string) (bool, int)
func IsFloat(str string) bool
func IsFullWidth(str string) bool
func IsHalfWidth(str string) bool
func IsHexadecimal(str string) bool
func IsHexcolor(str string) bool
func IsHost(str string) bool
func IsIP(str string) bool
func IsIPv4(str string) bool
func IsIPv6(str string) bool
func IsISBN(str string, version int) bool
func IsISBN10(str string) bool
func IsISBN13(str string) bool
func IsISO3166Alpha2(str string) bool
func IsISO3166Alpha3(str string) bool
func IsISO693Alpha2(str string) bool
func IsISO693Alpha3b(str string) bool
func IsISO4217(str string) bool
func IsIn(str string, params ...string) bool
func IsInt(str string) bool
func IsJSON(str string) bool
func IsLatitude(str string) bool
func IsLongitude(str string) bool
func IsLowerCase(str string) bool
func IsMAC(str string) bool
func IsMongoID(str string) bool
func IsMultibyte(str string) bool
func IsNatural(value float64) bool
func IsNegative(value float64) bool
func IsNonNegative(value float64) bool
func IsNonPositive(value float64) bool
func IsNull(str string) bool
func IsNumeric(str string) bool
func IsPort(str string) bool
func IsPositive(value float64) bool
func IsPrintableASCII(str string) bool
func IsRFC3339(str string) bool
func IsRFC3339WithoutZone(str string) bool
func IsRGBcolor(str string) bool
func IsRequestURI(rawurl string) bool
func IsRequestURL(rawurl string) bool
func IsSSN(str string) bool
func IsSemver(str string) bool
func IsTime(str string, format string) bool
func IsURL(str string) bool
func IsUTFDigit(str string) bool
func IsUTFLetter(str string) bool
func IsUTFLetterNumeric(str string) bool
func IsUTFNumeric(str string) bool
func IsUUID(str string) bool
func IsUUIDv3(str string) bool
func IsUUIDv4(str string) bool
func IsUUIDv5(str string) bool
func IsUpperCase(str string) bool
func IsVariableWidth(str string) bool
func IsWhole(value float64) bool
func LeftTrim(str, chars string) string
func Map(array []interface{}, iterator ResultIterator) []interface{}
func Matches(str, pattern string) bool
func NormalizeEmail(str string) (string, error)
func PadBoth(str string, padStr string, padLen int) string
func PadLeft(str string, padStr string, padLen int) string
func PadRight(str string, padStr string, padLen int) string
func Range(str string, params ...string) bool
func RemoveTags(s string) string
func ReplacePattern(str, pattern, replace string) string
func Reverse(s string) string
func RightTrim(str, chars string) string
func RuneLength(str string, params ...string) bool
func SafeFileName(str string) string
func SetFieldsRequiredByDefault(value bool)
func Sign(value float64) float64
func StringLength(str string, params ...string) bool
func StringMatches(s string, params ...string) bool
func StripLow(str string, keepNewLines bool) string
func ToBoolean(str string) (bool, error)
func ToFloat(str string) (float64, error)
func ToInt(str string) (int64, error)
func ToJSON(obj interface{}) (string, error)
func ToString(obj interface{}) string
func Trim(str, chars string) string
func Truncate(str string, length int, ending string) string
func UnderscoreToCamelCase(s string) string
func ValidateStruct(s interface{}) (bool, error)
func WhiteList(str, chars string) string
type ConditionIterator
type CustomTypeValidator
type Error
func (e Error) Error() string
type Errors
func (es Errors) Error() string
func (es Errors) Errors() []error
type ISO3166Entry
type Iterator
type ParamValidator
type ResultIterator
type UnsupportedTypeError
func (e *UnsupportedTypeError) Error() string
type Validator
```

#### Examples
###### IsURL
```go
println(govalidator.IsURL(`http://user@pass:domain.com/path/page`))
```
###### ToString
```go
type User struct {
	FirstName string
	LastName string
}

str := govalidator.ToString(&User{"John", "Juan"})
println(str)
```
###### Each, Map, Filter, Count for slices
Each iterates over the slice/array and calls Iterator for every item
```go
data := []interface{}{1, 2, 3, 4, 5}
var fn govalidator.Iterator = func(value interface{}, index int) {
	println(value.(int))
}
govalidator.Each(data, fn)
```
```go
data := []interface{}{1, 2, 3, 4, 5}
var fn govalidator.ResultIterator = func(value interface{}, index int) interface{} {
	return value.(int) * 3
}
_ = govalidator.Map(data, fn) // result = []interface{}{1, 6, 9, 12, 15}
```
```go
data := []interface{}{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
var fn govalidator.ConditionIterator = func(value interface{}, index int) bool {
	return value.(int)%2 == 0
}
_ = govalidator.Filter(data, fn) // result = []interface{}{2, 4, 6, 8, 10}
_ = govalidator.Count(data, fn) // result = 5
```
###### ValidateStruct [#2](https://github.com/asaskevich/govalidator/pull/2)
If you want to validate structs, you can use tag `valid` for any field in your structure. All validators used with this field in one tag are separated by comma. If you want to skip validation, place `-` in your tag. If you need a validator that is not on the list below, you can add it like this:
```go
govalidator.TagMap["duck"] = govalidator.Validator(func(str string) bool {
	return str == "duck"
})
```
For completely custom validators (interface-based), see below.

Here is a list of available validators for struct fields (validator - used function):
```go
"email":              IsEmail,
"url":                IsURL,
"dialstring":         IsDialString,
"requrl":             IsRequestURL,
"requri":             IsRequestURI,
"alpha":              IsAlpha,
"utfletter":          IsUTFLetter,
"alphanum":           IsAlphanumeric,
"utfletternum":       IsUTFLetterNumeric,
"numeric":            IsNumeric,
"utfnumeric":         IsUTFNumeric,
"utfdigit":           IsUTFDigit,
"hexadecimal":        IsHexadecimal,
"hexcolor":           IsHexcolor,
"rgbcolor":           IsRGBcolor,
"lowercase":          IsLowerCase,
"uppercase":          IsUpperCase,
"int":                IsInt,
"float":              IsFloat,
"null":               IsNull,
"uuid":               IsUUID,
"uuidv3":             IsUUIDv3,
"uuidv4":             IsUUIDv4,
"uuidv5":             IsUUIDv5,
"creditcard":         IsCreditCard,
"isbn10":             IsISBN10,
"isbn13":             IsISBN13,
"json":               IsJSON,
"multibyte":          IsMultibyte,
"ascii":              IsASCII,
"printableascii":     IsPrintableASCII,
"fullwidth":          IsFullWidth,
"halfwidth":          IsHalfWidth,
"variablewidth":      IsVariableWidth,
"base64":             IsBase64,
"datauri":            IsDataURI,
"ip":                 IsIP,
"port":               IsPort,
"ipv4":               IsIPv4,
"ipv6":               IsIPv6,
"dns":                IsDNSName,
"host":               IsHost,
"mac":                IsMAC,
"latitude":           IsLatitude,
"longitude":          IsLongitude,
"ssn":                IsSSN,
"semver":             IsSemver,
"rfc3339":            IsRFC3339,
"rfc3339WithoutZone": IsRFC3339WithoutZone,
"ISO3166Alpha2":      IsISO3166Alpha2,
"ISO3166Alpha3":      IsISO3166Alpha3,
```
Validators with parameters

```go
"range(min|max)": Range,
"length(min|max)": ByteLength,
"runelength(min|max)": RuneLength,
"matches(pattern)": StringMatches,
"in(string1|string2|...|stringN)": IsIn,
```

And here is small example of usage:
```go
type Post struct {
	Title    string `valid:"alphanum,required"`
	Message  string `valid:"duck,ascii"`
	AuthorIP string `valid:"ipv4"`
	Date     string `valid:"-"`
}
post := &Post{
	Title:   "My Example Post",
	Message: "duck",
	AuthorIP: "123.234.54.3",
}

// Add your own struct validation tags
govalidator.TagMap["duck"] = govalidator.Validator(func(str string) bool {
	return str == "duck"
})

result, err := govalidator.ValidateStruct(post)
if err != nil {
	println("error: " + err.Error())
}
println(result)
```
###### WhiteList
```go
// Remove all characters from string ignoring characters between "a" and "z"
println(govalidator.WhiteList("a3a43a5a4a3a2a23a4a5a4a3a4", "a-z") == "aaaaaaaaaaaa")
```

###### Custom validation functions
Custom validation using your own domain specific validators is also available - here's an example of how to use it:
```go
import "github.com/asaskevich/govalidator"

type CustomByteArray [6]byte // custom types are supported and can be validated

type StructWithCustomByteArray struct {
  ID              CustomByteArray `valid:"customByteArrayValidator,customMinLengthValidator"` // multiple custom validators are possible as well and will be evaluated in sequence
  Email           string          `valid:"email"`
  CustomMinLength int             `valid:"-"`
}

govalidator.CustomTypeTagMap.Set("customByteArrayValidator", CustomTypeValidator(func(i interface{}, context interface{}) bool {
  switch v := context.(type) { // you can type switch on the context interface being validated
  case StructWithCustomByteArray:
    // you can check and validate against some other field in the context,
    // return early or not validate against the context at all – your choice
  case SomeOtherType:
    // ...
  default:
    // expecting some other type? Throw/panic here or continue
  }

  switch v := i.(type) { // type switch on the struct field being validated
  case CustomByteArray:
    for _, e := range v { // this validator checks that the byte array is not empty, i.e. not all zeroes
      if e != 0 {
        return true
      }
    }
  }
  return false
}))
govalidator.CustomTypeTagMap.Set("customMinLengthValidator", CustomTypeValidator(func(i interface{}, context interface{}) bool {
  switch v := context.(type) { // this validates a field against the value in another field, i.e. dependent validation
  case StructWithCustomByteArray:
    return len(v.ID) >= v.CustomMinLength
  }
  return false
}))
```

#### Notes
Documentation is available here: [godoc.org](https://godoc.org/github.com/asaskevich/govalidator).
Full information about code coverage is also available here: [govalidator on gocover.io](http://gocover.io/github.com/asaskevich/govalidator).

#### Support
If you do have a contribution to the package, feel free to create a Pull Request or an Issue.

#### What to contribute
If you don't know what to do, there are some features and functions that need to be done

- [ ] Refactor code
- [ ] Edit docs and [README](https://github.com/asaskevich/govalidator/README.md): spellcheck, grammar and typo check
- [ ] Create actual list of contributors and projects that currently using this package
- [ ] Resolve [issues and bugs](https://github.com/asaskevich/govalidator/issues)
- [ ] Update actual [list of functions](https://github.com/asaskevich/govalidator#list-of-functions)
- [ ] Update [list of validators](https://github.com/asaskevich/govalidator#validatestruct-2) that available for `ValidateStruct` and add new
- [ ] Implement new validators: `IsFQDN`, `IsIMEI`, `IsPostalCode`, `IsISIN`, `IsISRC` etc
- [ ] Implement [validation by maps](https://github.com/asaskevich/govalidator/issues/224)
- [ ] Implement fuzzing testing
- [ ] Implement some struct/map/array utilities
- [ ] Implement map/array validation
- [ ] Implement benchmarking
- [ ] Implement batch of examples
- [ ] Look at forks for new features and fixes

#### Advice
Feel free to create what you want, but keep in mind when you implement new features:
- Code must be clear and readable, names of variables/constants clearly describes what they are doing
- Public functions must be documented and described in source file and added to README.md to the list of available functions
- There are must be unit-tests for any new functions and improvements

#### Special thanks to [contributors](https://github.com/asaskevich/govalidator/graphs/contributors)
* [Daniel Lohse](https://github.com/annismckenzie)
* [Attila Oláh](https://github.com/attilaolah)
* [Daniel Korner](https://github.com/Dadie)
* [Steven Wilkin](https://github.com/stevenwilkin)
* [Deiwin Sarjas](https://github.com/deiwin)
* [Noah Shibley](https://github.com/slugmobile)
* [Nathan Davies](https://github.com/nathj07)
* [Matt Sanford](https://github.com/mzsanford)
* [Simon ccl1115](https://github.com/ccl1115)
# Exponential Backoff [![GoDoc][godoc image]][godoc] [![Build Status][travis image]][travis] [![Coverage Status][coveralls image]][coveralls]

This is a Go port of the exponential backoff algorithm from [Google's HTTP Client Library for Java][google-http-java-client].

[Exponential backoff][exponential backoff wiki]
is an algorithm that uses feedback to multiplicatively decrease the rate of some process,
in order to gradually find an acceptable rate.
The retries exponentially increase and stop increasing when a certain threshold is met.

## Usage

See https://godoc.org/github.com/cenkalti/backoff#pkg-examples

## Contributing

* I would like to keep this library as small as possible.
* Please don't send a PR without opening an issue and discussing it first.
* If proposed change is not a common use case, I will probably not accept it.

[godoc]: https://godoc.org/github.com/cenkalti/backoff
[godoc image]: https://godoc.org/github.com/cenkalti/backoff?status.png
[travis]: https://travis-ci.org/cenkalti/backoff
[travis image]: https://travis-ci.org/cenkalti/backoff.png?branch=master
[coveralls]: https://coveralls.io/github/cenkalti/backoff?branch=master
[coveralls image]: https://coveralls.io/repos/github/cenkalti/backoff/badge.svg?branch=master

[google-http-java-client]: https://github.com/google/google-http-java-client
[exponential backoff wiki]: http://en.wikipedia.org/wiki/Exponential_backoff

[advanced example]: https://godoc.org/github.com/cenkalti/backoff#example_
go-spew
=======

[![Build Status](https://img.shields.io/travis/davecgh/go-spew.svg)]
(https://travis-ci.org/davecgh/go-spew) [![ISC License]
(http://img.shields.io/badge/license-ISC-blue.svg)](http://copyfree.org) [![Coverage Status]
(https://img.shields.io/coveralls/davecgh/go-spew.svg)]
(https://coveralls.io/r/davecgh/go-spew?branch=master)


Go-spew implements a deep pretty printer for Go data structures to aid in
debugging.  A comprehensive suite of tests with 100% test coverage is provided
to ensure proper functionality.  See `test_coverage.txt` for the gocov coverage
report.  Go-spew is licensed under the liberal ISC license, so it may be used in
open source or commercial projects.

If you're interested in reading about how this package came to life and some
of the challenges involved in providing a deep pretty printer, there is a blog
post about it
[here](https://web.archive.org/web/20160304013555/https://blog.cyphertite.com/go-spew-a-journey-into-dumping-go-data-structures/).

## Documentation

[![GoDoc](https://img.shields.io/badge/godoc-reference-blue.svg)]
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
	App Engine or with the "safe" build tag specified.
	Pointer method invocation is enabled by default.

* DisablePointerAddresses
	DisablePointerAddresses specifies whether to disable the printing of
	pointer addresses. This is useful when diffing data structures in tests.

* DisableCapacities
	DisableCapacities specifies whether to disable the printing of capacities
	for arrays, slices, maps and channels. This is useful when diffing data
	structures in tests.

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
operate in this mode on Google App Engine and when compiled with GopherJS.  The
"safe" build tag may also be specified to force the package to build without
using the unsafe package.

## License

Go-spew is licensed under the [copyfree](http://copyfree.org) ISC License.
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
# OAI object model [![Build Status](https://travis-ci.org/go-openapi/spec.svg?branch=master)](https://travis-ci.org/go-openapi/spec) [![codecov](https://codecov.io/gh/go-openapi/spec/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/spec) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/spec/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/spec?status.svg)](http://godoc.org/github.com/go-openapi/spec)

The object model for OpenAPI specification documents
# Swagger 2.0 specification schema

This folder contains the Swagger 2.0 specification schema files maintained here:

https://github.com/reverb/swagger-spec/blob/master/schemas/v2.0# Loads OAI specs  [![Build Status](https://travis-ci.org/go-openapi/loads.svg?branch=master)](https://travis-ci.org/go-openapi/loads) [![codecov](https://codecov.io/gh/go-openapi/loads/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/loads) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/loads/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/loads?status.svg)](http://godoc.org/github.com/go-openapi/loads)

Loading of OAI specification documents from local or remote locations.
# OpenAPI errors [![Build Status](https://travis-ci.org/go-openapi/errors.svg?branch=master)](https://travis-ci.org/go-openapi/errors) [![codecov](https://codecov.io/gh/go-openapi/errors/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/errors) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/errors/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/errors?status.svg)](http://godoc.org/github.com/go-openapi/errors) 

Shared errors used throughout the various libraries for the go-openapi toolkit # Strfmt [![Build Status](https://travis-ci.org/go-openapi/strfmt.svg?branch=master)](https://travis-ci.org/go-openapi/strfmt) [![codecov](https://codecov.io/gh/go-openapi/strfmt/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/strfmt) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/strfmt/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/strfmt?status.svg)](http://godoc.org/github.com/go-openapi/strfmt)

strfmt represents a well known string format such as credit card or email. The go toolkit for open api specifications knows how to deal with those.
# OpenAPI initiative analysis [![Build Status](https://travis-ci.org/go-openapi/analysis.svg?branch=master)](https://travis-ci.org/go-openapi/analysis) [![codecov](https://codecov.io/gh/go-openapi/analysis/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/analysis) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/analysis/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/analysis?status.svg)](http://godoc.org/github.com/go-openapi/analysis) 


A foundational library to analyze an OAI specification document for easier reasoning about the content.# Swag [![Build Status](https://travis-ci.org/go-openapi/swag.svg?branch=master)](https://travis-ci.org/go-openapi/swag) [![codecov](https://codecov.io/gh/go-openapi/swag/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/swag) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/swag/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/swag?status.svg)](http://godoc.org/github.com/go-openapi/swag)

Contains a bunch of helper functions:

* convert between value and pointers for builtins
* convert from string to builtin
* fast json concatenation
* search in path
* load from file or http
* name manglin# gojsonpointer [![Build Status](https://travis-ci.org/go-openapi/jsonpointer.svg?branch=master)](https://travis-ci.org/go-openapi/jsonpointer) [![codecov](https://codecov.io/gh/go-openapi/jsonpointer/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/jsonpointer) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/jsonpointer/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/jsonpointer?status.svg)](http://godoc.org/github.com/go-openapi/jsonpointer)
An implementation of JSON Pointer - Go language

## Status
Completed YES

Tested YES

## References
http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-07

### Note
The 4.Evaluation part of the previous reference, starting with 'If the currently referenced value is a JSON array, the reference token MUST contain either...' is not implemented.
# gojsonreference [![Build Status](https://travis-ci.org/go-openapi/jsonreference.svg?branch=master)](https://travis-ci.org/go-openapi/jsonreference) [![codecov](https://codecov.io/gh/go-openapi/jsonreference/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/jsonreference) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/jsonreference/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/jsonreference?status.svg)](http://godoc.org/github.com/go-openapi/jsonreference)
An implementation of JSON Reference - Go language

## Status
Work in progress ( 90% done )

## Dependencies
https://github.com/go-openapi/jsonpointer

## References
http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-07

http://tools.ietf.org/html/draft-pbryan-zyp-json-ref-03
[![Build Status](https://travis-ci.org/spf13/pflag.svg?branch=master)](https://travis-ci.org/spf13/pflag)
[![Go Report Card](https://goreportcard.com/badge/github.com/spf13/pflag)](https://goreportcard.com/report/github.com/spf13/pflag)
[![GoDoc](https://godoc.org/github.com/spf13/pflag?status.svg)](https://godoc.org/github.com/spf13/pflag)

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
	flag.BoolVarP(&flagvar, "boolname", "b", true, "help message")
}
flag.VarP(&flagVal, "varname", "v", "help message")
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

## Disable sorting of flags
`pflag` allows you to disable sorting of flags for help and usage message.

**Example**:
```go
flags.BoolP("verbose", "v", false, "verbose output")
flags.String("coolflag", "yeaah", "it's really cool flag")
flags.Int("usefulflag", 777, "sometimes it's very useful")
flags.SortFlags = false
flags.PrintDefaults()
```
**Output**:
```
  -v, --verbose           verbose output
      --coolflag string   it's really cool flag (default "yeaah")
      --usefulflag int    sometimes it's very useful (default 777)
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
[http://localhost:6060/pkg/github.com/spf13/pflag][2] after
installation.

[2]: http://localhost:6060/pkg/github.com/spf13/pflag
[3]: http://godoc.org/github.com/spf13/pflag
# Distribution

The Docker toolset to pack, ship, store, and deliver content.

This repository's main product is the Docker Registry 2.0 implementation
for storing and distributing Docker images. It supersedes the
[docker/docker-registry](https://github.com/docker/docker-registry)
project with a new API design, focused around security and performance.

<img src="https://www.docker.com/sites/default/files/oyster-registry-3.png" width=200px/>

[![Circle CI](https://circleci.com/gh/docker/distribution/tree/master.svg?style=svg)](https://circleci.com/gh/docker/distribution/tree/master)
[![GoDoc](https://godoc.org/github.com/docker/distribution?status.svg)](https://godoc.org/github.com/docker/distribution)

This repository contains the following components:

|**Component**       |Description                                                                                                                                                                                         |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **registry**       | An implementation of the [Docker Registry HTTP API V2](docs/spec/api.md) for use with docker 1.6+.                                                                                                  |
| **libraries**      | A rich set of libraries for interacting with distribution components. Please see [godoc](https://godoc.org/github.com/docker/distribution) for details. **Note**: These libraries are **unstable**. |
| **specifications** | _Distribution_ related specifications are available in [docs/spec](docs/spec)                                                                                                                        |
| **documentation**  | Docker's full documentation set is available at [docs.docker.com](https://docs.docker.com). This repository [contains the subset](docs/) related just to the registry.                                                                                                                                          |

### How does this integrate with Docker engine?

This project should provide an implementation to a V2 API for use in the [Docker
core project](https://github.com/docker/docker). The API should be embeddable
and simplify the process of securely pulling and pushing content from `docker`
daemons.

### What are the long term goals of the Distribution project?

The _Distribution_ project has the further long term goal of providing a
secure tool chain for distributing content. The specifications, APIs and tools
should be as useful with Docker as they are without.

Our goal is to design a professional grade and extensible content distribution
system that allow users to:

* Enjoy an efficient, secured and reliable way to store, manage, package and
  exchange content
* Hack/roll their own on top of healthy open-source components
* Implement their own home made solution through good specs, and solid
  extensions mechanism.

## More about Registry 2.0

The new registry implementation provides the following benefits:

- faster push and pull
- new, more efficient implementation
- simplified deployment
- pluggable storage backend
- webhook notifications

For information on upcoming functionality, please see [ROADMAP.md](ROADMAP.md).

### Who needs to deploy a registry?

By default, Docker users pull images from Docker's public registry instance.
[Installing Docker](https://docs.docker.com/engine/installation/) gives users this
ability. Users can also push images to a repository on Docker's public registry,
if they have a [Docker Hub](https://hub.docker.com/) account.

For some users and even companies, this default behavior is sufficient. For
others, it is not.

For example, users with their own software products may want to maintain a
registry for private, company images. Also, you may wish to deploy your own
image repository for images used to test or in continuous integration. For these
use cases and others, [deploying your own registry instance](https://github.com/docker/docker.github.io/blob/master/registry/deploying.md)
may be the better choice.

### Migration to Registry 2.0

For those who have previously deployed their own registry based on the Registry
1.0 implementation and wish to deploy a Registry 2.0 while retaining images,
data migration is required. A tool to assist with migration efforts has been
created. For more information see [docker/migrator]
(https://github.com/docker/migrator).

## Contribute

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute
issues, fixes, and patches to this project. If you are contributing code, see
the instructions for [building a development environment](BUILDING.md).

## Support

If any issues are encountered while using the _Distribution_ project, several
avenues are available for support:

<table>
<tr>
	<th align="left">
	IRC
	</th>
	<td>
	#docker-distribution on FreeNode
	</td>
</tr>
<tr>
	<th align="left">
	Issue Tracker
	</th>
	<td>
	github.com/docker/distribution/issues
	</td>
</tr>
<tr>
	<th align="left">
	Google Groups
	</th>
	<td>
	https://groups.google.com/a/dockerproject.org/forum/#!forum/distribution
	</td>
</tr>
<tr>
	<th align="left">
	Mailing List
	</th>
	<td>
	docker@dockerproject.org
	</td>
</tr>
</table>


## License

This project is distributed under [Apache License, Version 2.0](LICENSE).
# Docker Registry Integration Testing

These integration tests cover interactions between registry clients such as
the docker daemon and the registry server. All tests can be run using the
[golem integration test runner](https://github.com/docker/golem)

The integration tests configure components using docker compose
(see docker-compose.yaml) and the runner can be using the golem
configuration file (see golem.conf).

## Running integration tests

### Run using multiversion script

The integration tests in the `contrib/docker-integration` directory can be simply
run by executing the run script `./run_multiversion.sh`. If there is no running
daemon to connect to, run as `./run_multiversion.sh -d`.

This command will build the distribution image from the locally checked out
version and run against multiple versions of docker defined in the script. To
run a specific version of the registry or docker, Golem will need to be
executed manually.

### Run manually using Golem

Using the golem tool directly allows running against multiple versions of
the registry and docker. Running against multiple versions of the registry
can be useful for testing changes in the docker daemon which are not
covered by the default run script.

#### Installing Golem

Golem is distributed as an executable binary which can be installed from
the [release page](https://github.com/docker/golem/releases/tag/v0.1).

#### Running golem with docker

Additionally golem can be run as a docker image requiring no additonal
installation.

`docker run --privileged -v "$GOPATH/src/github.com/docker/distribution/contrib/docker-integration:/test" -w /test distribution/golem golem -rundaemon .`

#### Golem custom images

Golem tests version of software by defining the docker image to test.

Run with registry 2.2.1 and docker 1.10.3

`golem -i golem-dind:latest,docker:1.10.3-dind,1.10.3 -i golem-distribution:latest,registry:2.2.1 .`


#### Use golem caching for developing tests

Golem allows caching image configuration to reduce test start up time.
Using this cache will allow tests with the same set of images to start
up quickly. This can be useful when developing tests and needing the
test to run quickly. If there are changes which effect the image (such as
building a new registry image), then startup time will be slower.

Run this command multiple times and after the first time test runs
should start much quicker.
`golem -cache ~/.cache/docker/golem -i golem-dind:latest,docker:1.10.3-dind,1.10.3 -i golem-distribution:latest,registry:2.2.1 .`

# Docker Compose V1 + V2 registry

This compose configuration configures a `v1` and `v2` registry behind an `nginx`
proxy. By default, you can access the combined registry at `localhost:5000`.

The configuration does not support pushing images to `v2` and pulling from `v1`.
If a `docker` client has a version less than 1.6, Nginx will route its requests
to the 1.0 registry. Requests from newer clients will route to the 2.0 registry.

### Install Docker Compose

1. Open a new terminal on the host with your `distribution` source.

2. Get the `docker-compose` binary.

		$ sudo wget https://github.com/docker/compose/releases/download/1.1.0/docker-compose-`uname  -s`-`uname -m` -O /usr/local/bin/docker-compose

	This command installs the binary in the `/usr/local/bin` directory. 
	
3. Add executable permissions to the binary.

		$  sudo chmod +x /usr/local/bin/docker-compose
		
## Build and run with Compose
	
1. In your terminal, navigate to the `distribution/contrib/compose` directory

	This directory includes a single `docker-compose.yml` configuration.
	
		nginx:
			build: "nginx"
			ports:
				- "5000:5000"
			links:
				- registryv1:registryv1
				- registryv2:registryv2
		registryv1:
			image: registry
			ports:
				- "5000"
		registryv2:
			build: "../../"
			ports:
				- "5000"

	This configuration builds a new `nginx` image as specified by the
	`nginx/Dockerfile` file. The 1.0 registry comes from Docker's official
	public image. Finally, the registry 2.0 image is built from the
	`distribution/Dockerfile` you've used previously.
 		
2. Get a registry 1.0 image.

		$ docker pull registry:0.9.1 

	The Compose configuration looks for this image locally. If you don't do this
	step, later steps can fail.
	
3. Build `nginx`, the registry 2.0 image, and 

		$ docker-compose build
		registryv1 uses an image, skipping
		Building registryv2...
		Step 0 : FROM golang:1.4
		
		...
		
		Removing intermediate container 9f5f5068c3f3
		Step 4 : COPY docker-registry-v2.conf /etc/nginx/docker-registry-v2.conf
		 ---> 74acc70fa106
		Removing intermediate container edb84c2b40cb
		Successfully built 74acc70fa106
		
	The commmand outputs its progress until it completes.

4. Start your configuration with compose.

		$ docker-compose up
		Recreating compose_registryv1_1...
		Recreating compose_registryv2_1...
		Recreating compose_nginx_1...
		Attaching to compose_registryv1_1, compose_registryv2_1, compose_nginx_1
		...
	

5. In another terminal, display the running configuration.

		$ docker ps
		CONTAINER ID        IMAGE                       COMMAND                CREATED             STATUS              PORTS                                     NAMES
		a81ad2557702        compose_nginx:latest        "nginx -g 'daemon of   8 minutes ago       Up 8 minutes        80/tcp, 443/tcp, 0.0.0.0:5000->5000/tcp   compose_nginx_1        
		0618437450dd        compose_registryv2:latest   "registry cmd/regist   8 minutes ago       Up 8 minutes        0.0.0.0:32777->5000/tcp                   compose_registryv2_1   
		aa82b1ed8e61        registry:latest             "docker-registry"      8 minutes ago       Up 8 minutes        0.0.0.0:32776->5000/tcp                   compose_registryv1_1   
	
### Explore a bit

1. Check for TLS on your `nginx` server.

		$ curl -v https://localhost:5000
		* Rebuilt URL to: https://localhost:5000/
		* Hostname was NOT found in DNS cache
		*   Trying 127.0.0.1...
		* Connected to localhost (127.0.0.1) port 5000 (#0)
		* successfully set certificate verify locations:
		*   CAfile: none
			CApath: /etc/ssl/certs
		* SSLv3, TLS handshake, Client hello (1):
		* SSLv3, TLS handshake, Server hello (2):
		* SSLv3, TLS handshake, CERT (11):
		* SSLv3, TLS alert, Server hello (2):
		* SSL certificate problem: self signed certificate
		* Closing connection 0
		curl: (60) SSL certificate problem: self signed certificate
		More details here: http://curl.haxx.se/docs/sslcerts.html
		
2. Tag the `v1` registry image.

		 $ docker tag registry:latest localhost:5000/registry_one:latest

2. Push it to the localhost.

		 $ docker push localhost:5000/registry_one:latest
		
	If you are using the 1.6 Docker client, this pushes the image the `v2 `registry.

4. Use `curl` to list the image in the registry.

			$ curl -v -X GET http://localhost:32777/v2/registry1/tags/list
			* Hostname was NOT found in DNS cache
			*   Trying 127.0.0.1...
			* Connected to localhost (127.0.0.1) port 32777 (#0)
			> GET /v2/registry1/tags/list HTTP/1.1
			> User-Agent: curl/7.36.0
			> Host: localhost:32777
			> Accept: */*
			> 
			< HTTP/1.1 200 OK
			< Content-Type: application/json; charset=utf-8
			< Docker-Distribution-Api-Version: registry/2.0
			< Date: Tue, 14 Apr 2015 22:34:13 GMT
			< Content-Length: 39
			< 
			{"name":"registry1","tags":["latest"]}
			* Connection #0 to host localhost left intact
		
	This example refers to the specific port assigned to the 2.0 registry. You saw
	this port earlier, when you used `docker ps` to show your running containers.


# Apache HTTPd sample for Registry v1, v2 and mirror

3 containers involved 

* Docker Registry v1 (registry 0.9.1)
* Docker Registry v2 (registry 2.0.0)
* Docker Registry v1 in mirror mode

HTTP for mirror and HTTPS for v1 & v2

* http://registry.example.com proxify Docker Registry 1.0 in Mirror mode
* https://registry.example.com proxify Docker Registry 1.0 or 2.0 in Hosting mode

## 3 Docker containers should be started 

* Docker Registry 1.0 in Mirror mode : port 5001
* Docker Registry 1.0 in Hosting mode : port 5000
* Docker Registry 2.0 in Hosting mode : port 5002

### Registry v1

    docker run -d -e SETTINGS_FLAVOR=dev -v /var/lib/docker-registry/storage/hosting-v1:/tmp -p 5000:5000 registry:0.9.1"

### Mirror

    docker run -d -e SETTINGS_FLAVOR=dev -e STANDALONE=false -e MIRROR_SOURCE=https://registry-1.docker.io -e MIRROR_SOURCE_INDEX=https://index.docker.io \
                  -e MIRROR_TAGS_CACHE_TTL=172800 -v /var/lib/docker-registry/storage/mirror:/tmp -p 5001:5000 registry:0.9.1"

### Registry v2

    docker run -d -e SETTINGS_FLAVOR=dev -v /var/lib/axway/docker-registry/storage/hosting2-v2:/tmp -p 5002:5000 registry:2"

# For Hosting mode access

* users should have account (valid-user) to be able to fetch images
* only users using account docker-deployer will be allowed to push images
Git Hooks
=========

To enforce valid and properly-formatted code, there is CI in place which runs `gofmt`, `golint`, and `go vet` against code in the repository.

As an aid to prevent committing invalid code in the first place, a git pre-commit hook has been added to the repository, found in [pre-commit](./pre-commit). As it is impossible to automatically add linked hooks to a git repository, this hook should be linked into your `.git/hooks/pre-commit`, which can be done by running the `configure-hooks.sh` script in this directory. This script is the preferred method of configuring hooks, as it will be updated as more are added.# The docs have been moved!

The documentation for Registry has been merged into
[the general documentation repo](https://github.com/docker/docker.github.io).
Commit history has been preserved.

The docs for Registry are now here:
https://github.com/docker/docker.github.io/tree/master/registry

> Note: The definitive [./spec directory](spec/) directory and
[configuration.md](configuration.md) file will be maintained in this repository
and be refreshed periodically in
[the general documentation repo](https://github.com/docker/docker.github.io).

As always, the docs in the general repo remain open-source and we appreciate
your feedback and pull requests!
