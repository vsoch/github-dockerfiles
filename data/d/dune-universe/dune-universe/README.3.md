VPN-friendly networking devices for [HyperKit](https://github.com/moby/hyperkit)
===============================

[![Build Status (OSX)](https://circleci.com/gh/moby/vpnkit.png)](https://circleci.com/gh/moby/vpnkit)

Binary artefacts are built by CI:

- [MacOS](https://circleci.com/gh/moby/vpnkit)
- [Windows](https://ci.appveyor.com/project/moby/vpnkit/history)

![VPNKit diagram](http://moby.github.io/vpnkit/vpnkit.png)

VPNKit is a set of tools and services for helping [HyperKit](https://github.com/moby/hyperkit)
VMs interoperate with host VPN configurations.


Building on Unix
----------------

First install `wget`, `opam` using your package manager of choice.

Build all the dependencies and the program itself with:

```
cd [path to vpnkit source]
opam remote add vpnkit ./repo/darwin
opam install --deps-only vpnkit
make
```

When the build succeeds the `vpnkit` binary should be available in the current path.

Running with hyperkit
---------------------

First ask `vpnkit` to listen for ethernet connections on a local Unix domain socket:
```
vpnkit --ethernet /tmp/ethernet --debug
```
Next ask [com.docker.hyperkit](https://github.com/moby/hyperkit) to connect a NIC to this
socket by adding a command-line option like `-s 2:0,virtio-vpnkit,path=/tmp/ethernet`. Note:
you may need to change the slot `2:0` to a free slot in your VM configuration.

Why is this needed?
-------------------

Running a VM usually involves modifying the network configuration on the host, for example
by activating Ethernet bridges, new routing table entries, DNS and firewall/NAT configurations.
Activating a VPN involves modifying the same routing tables, DNS and firewall/NAT configurations
and therefore there can be a clash -- this often results in the network connection to the VM
being disconnected.

VPNKit, part of [HyperKit](https://github.com/moby/hyperkit)
attempts to work nicely with VPN software by intercepting the VM traffic at the Ethernet level,
parsing and understanding protocols like NTP, DNS, UDP, TCP and doing the "right thing" with
respect to the host's VPN configuration.

VPNKit operates by reconstructing Ethernet traffic from the VM and translating it into the
relevant socket API calls on OSX or Windows. This allows the host application to generate
traffic without requiring low-level Ethernet bridging support.

Design
------

- [Using vpnkit as a default gateway](docs/ethernet.md): describes the flow of ethernet traffic to/from the VM
- [Port forwarding](docs/ports.md): describes how ports are forwarded from the host into the VM
- [Experimental transparent HTTP proxy](docs/transparent-http-proxy.md): describes the
  experimental support for transparent HTTP(S) proxying

Licensing
---------

VPNKit is licensed under the Apache License, Version 2.0. See
[LICENSE](https://github.com/moby/vpnkit/blob/master/LICENSE.md) for the full
license text.

Contributions are welcome under the terms of this license. You may wish to browse
the [weekly reports](reports) to read about overall activity in the repository.
This repository holds supplemental Go packages for low-level interactions with the operating system.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
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
## DataKit -- Orchestrate applications using a Git-like dataflow

*DataKit* is a tool to orchestrate applications using a Git-like dataflow. It
revisits the UNIX pipeline concept, with a modern twist: streams of
tree-structured data instead of raw text. DataKit allows you to define
complex build pipelines over version-controlled data.

DataKit is currently used as the coordination
layer for [HyperKit](http://github.com/docker/hyperkit), the
hypervisor component of
[Docker for Mac and Windows](https://blog.docker.com/2016/03/docker-for-mac-windows-beta/), and
for the [DataKitCI][] continuous integration system.

---

[![Build Status (OSX, Linux)](https://travis-ci.org/moby/datakit.svg)](https://travis-ci.org/moby/datakit)
[![Build status (Windows)](https://ci.appveyor.com/api/projects/status/6qrdgiqbhi4sehmy/branch/master?svg=true)](https://ci.appveyor.com/project/moby/datakit/branch/master)
[![docs](https://img.shields.io/badge/doc-online-blue.svg)](https://docker.github.io/datakit/)

There are several components in this repository:

- `src` contains the main DataKit service. This is a Git-like database to which other services can connect.
- `ci` contains [DataKitCI][], a continuous integration system that uses DataKit to monitor repositories and store build results.
- `ci/self-ci` is the CI configuration for DataKitCI that tests DataKit itself.
- `bridge/github` is a service that monitors repositories on GitHub and syncs their metadata with a DataKit database.
  e.g. when a pull request is opened or updated, it will commit that information to DataKit. If you commit a status message to DataKit, the bridge will push it to GitHub.
- `bridge/local` is a drop-in replacement for `bridge/github` that just monitors a local Git repository. This is useful for local testing.

### Quick Start

The easiest way to use DataKit is to start both the server and the client in containers.

To expose a Git repository as a 9p endpoint on port 5640 on a private network, run:

```shell
$ docker network create datakit-net # create a private network
$ docker run -it --net datakit-net --name datakit -v <path/to/git/repo>:/data datakit/db
```

*Note*: The `--name datakit` option is mandatory.  It will allow the client
to connect to a known name on the private network.

You can then start a DataKit client, which will mount the 9p endpoint and
expose the database as a filesystem API:

```shell
# In an other terminal
$ docker run -it --privileged --net datakit-net datakit/client
$ ls /db
branch     remotes    snapshots  trees
```

*Note*: the `--privileged` option is needed because the container will have
to mount the 9p endpoint into its local filesystem.

Now you can explore, edit and script `/db`. See the
[Filesystem API][]
for more details.

### Building

The easiest way to build the DataKit project is to use [docker](https://docker.com),
(which is what the
[start-datakit.sh](https://github.com/moby/datakit/blob/master/scripts/start-datakit.sh) script
does under the hood):

```shell
docker build -t datakit/db -f Dockerfile .
docker run -p 5640:5640 -it --rm datakit/db --listen-9p=tcp://0.0.0.0:5640
```
These commands will expose the database's 9p endpoint on port 5640.

If you want to build the project from source without Docker, you will need to install
[ocaml](http://ocaml.org/) and [opam](http://opam.ocaml.org/). Then write:

```shell
$ make depends
$ make && make test
```

For information about command-line options:

```shell
$ datakit --help
```

## Prometheus metric reporting

Run with `--listen-prometheus 9090` to expose metrics at `http://*:9090/metrics`.

Note: there is no encryption and no access control. You are expected to run the
database in a container and to not export this port to the outside world. You
can either collect the metrics by running a Prometheus service in a container
on the same Docker network, or front the service with nginx or similar if you
want to collect metrics remotely.

## Language bindings

* **Go** bindings are in the `api/go` directory.
* **OCaml** bindings are in the `api/ocaml` directory. See `examples/ocaml-client` for an example.

## Licensing

DataKit is licensed under the Apache License, Version 2.0. See
[LICENSE](https://github.com/moby/datakit/blob/master/LICENSE.md) for the full
license text.

Contributions are welcome under the terms of this license. You may wish to browse
the [weekly reports](reports) to read about overall activity in the repository.

[DataKitCI]: https://github.com/moby/datakit/tree/master/ci
[Filesystem API]: https://github.com/moby/datakit/tree/master/9p.md
To run test on windows, launch the a datakit server with --url \\.\pipe\datakit-test
This repository contains Go bindings and sample code for [Hyper-V sockets](https://msdn.microsoft.com/en-us/virtualization/hyperv_on_windows/develop/make_mgmt_service) and [virtio sockets](http://stefanha.github.io/virtio/)(VSOCK).

## Organisation

- `pkg/hvsock`: Go binding for Hyper-V sockets
- `pkg/vsock`: Go binding for virtio VSOCK
- `examples`: Sample Go code and stress test
- `scripts`: Miscellaneous scripts
- `c`: Sample C code (including benchmarks and stress tests)
- `data`: Data from benchmarks


## Building

By default the Go sample code is build in a container. Simply type `make`.

If you want to build binaries on a local system use `make build-binaries`.

## Testing

There are several examples and tests written both in [Go](./examples) and in [C](./c). The C code is Hyper-V sockets only while the Go code also works with virtio sockets and [HyperKit](https://github.com/moby/hyperkit). The respective READMEs contain instructions on how to run the tests, but the simplest way is to use [LinuxKit](https://github.com/linuxkit/linuxkit).

Assuming you have LinuxKit installed, the make target `make linuxkit`
will build a custom Linux image which can be booted on HyperKit or on
Windows. The custom Linux image contains the test binaries.

### macOS

Boot the Linux VM:
```
linuxkit run hvtest
```
This should create a directory called `./hvtest-state`.

Run the server in the VM and client on the host:
```
linux$ virtsock_stress -s -v 1
macos$ ./build/virtsock_stress.darwin -c 3 -m hyperkit:./hvtest-state -v 1
```

Run the server on the host and the client inside the VM:
```
macos$ ./build/virtsock_stress.darwin -s -m hyperkit:./hvtest-state -v 1
linux$ virtsock_stress -c 2 -v 1
```

### Windows

TBD

## Known limitations

- `hvsock`: The Windows side does not implement `accept()` due to
  limitations on some Windows builds where a VM can not connect to the
  host via Hyper-V sockets.

- `vsock`: There is general host side implementation as the interface
  is hypervisor specific. The `vsock` package includes some support
  for connecting with the VSOCK implementation in
  [Hyperkit](https://github.com/moby/hyperkit), but there is no
  implementation for, e.g. `qemu`.

# Hyper-V sockets sample applications

## Building

Building is driven by `make` (or `mingw32-make.exe`). By default both
Linux and Windows binaries are build.

Linux builds are done via Dockerfiles and create static binaries.

Windows builds require MSBuild, Visual Studio and Windows SDK
installed with a minimum version of 14290. The project/solutions
assumes 14291, so you may have to adjust the
`WindowsTargetPlatformVersion` in the project files.


## Running

All sample application assume a service ID of `3049197C-FACB-11E6-BD58-64006A7986D3` which needs to be registered *once* using:
```
$service = New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\GuestCommunicationServices" -Name 3049197C-FACB-11E6-BD58-64006A7986D3

$service.SetValue("ElementName", "Hyper-V Socket Echo Service")
```

### Echo applications 

The echo server is started with:
```
hvecho -s
```

The client supports a number of modes. By default, with no arguments supplied it will connected using loopback mode, i.e. it tries to connect to the server on the same partition:
```
hvecho -c
```

The client can be run in a VM and started with:
```
hvecho -c parent
```
which attempts to connect to the server in the parent partition.


Finally, if the server is run in a VM, the client can be invoked in the parent partition with:
```
client -c <vmid>
```
where `<vmid>` is the GUID of the VM the server is running in. The GUID can be retrieved with: `(get-vm <VM Name>).id`.
# p9p [![GoDoc](https://godoc.org/github.com/docker/go-p9p?status.svg)](https://godoc.org/github.com/docker/go-p9p) [![Apache licensed](https://img.shields.io/badge/license-Apache-blue.svg)](https://raw.githubusercontent.com/docker/go-p9p/master/LICENSE) [![CircleCI](https://circleci.com/gh/docker/go-p9p.svg?style=shield)](https://circleci.com/gh/docker/go-p9p) [![TravisCI](https://travis-ci.org/docker/go-p9p.svg?branch=master)](https://travis-ci.org/docker/go-p9p) [![Go Report Card](https://goreportcard.com/badge/github.com/docker/go-p9p)](https://goreportcard.com/report/github.com/docker/go-p9p) [![Badge Badge](http://doyouevenbadge.com/github.com/docker/go-p9p)](http://doyouevenbadge.com/report/github.com/docker/go-p9p)


A modern, performant 9P library for Go.

For information on usage, please see the [GoDoc](https://godoc.org/github.com/docker/go-p9p).

## Copyright and license

Copyright © 2015 Docker, Inc. go-p9p is licensed under the Apache License,
Version 2.0. See [LICENSE](LICENSE) for the full license text.
This repo is still in the experimental stage. Shortly it will contain the schema of the API that are served by the Kubernetes apiserver.
# Kube OpenAPI

This repo is the home for Kubernetes OpenAPI discovery spec generation. The goal 
is to support a subset of OpenAPI features to satisfy kubernetes use-cases but 
implement that subset with little to no assumption about the structure of the 
code or routes. Thus, there should be no kubernetes specific code in this repo. 


There are two main parts: 
 - A model generator that goes through .go files, find and generate model 
definitions. 
 - The spec generator that is responsible for dynamically generate 
the final OpenAPI spec using web service routes or combining other 
OpenAPI/Json specs.
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

We currently recommend using the v4.0.0 tag. See [INSTALL.md](/INSTALL.md) for
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

|                     | Kubernetes 1.3 | Kubernetes 1.4 | Kubernetes 1.5 | Kubernetes 1.6 | Kubernetes 1.7 |
|---------------------|----------------|----------------|----------------|----------------|----------------|
| client-go 1.4       | +              | ✓              | -              | -              | -              |
| client-go 1.5       | +              | +              | -              | -              | -              |
| client-go 2.0       | +              | +              | ✓              | -              | -              |
| client-go 3.0       | †              | †              | †              | ✓              | -              |
| client-go 4.0       | †              | †              | †              | +              | ✓              |
| client-go HEAD      | †              | †              | †              | +              | +              |

Key:

* `✓` Exactly the same features / API objects in both client-go and the Kubernetes
  version.
* `+` client-go has features or api objects that may not be present in the
  Kubernetes cluster, but everything they have in common will work. Please
  note that alpha APIs may vanish or change significantly in a single release.
* `†` client-go has new features or api objects, and some APIs running in the
  cluster may have been deprecated and removed from client-go. But everything
  they share in common (i.e., most APIs) will work.
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
| client-go 4.0  | Kubernetes main repo, 1.7 branch     | ✓                             |
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

If your application runs in a Pod in the cluster, please refer to the
in-cluster [example](examples/in-cluster-client-configuration), otherwise please
refer to the out-of-cluster [example](examples/out-of-cluster-client-configuration).

### Dependency management

If your application depends on a package that client-go depends on, and you let the Go compiler find the dependency in `GOPATH`, you will end up with duplicated dependencies: one copy from the `GOPATH`, and one from the vendor folder of client-go. This will cause unexpected runtime error like flag redefinition, since the go compiler ends up importing both packages separately, even if they are exactly the same thing. If this happens, you can either
* run `godep restore` ([godep](https://github.com/tools/godep)) in the client-go/ folder, then remove the vendor folder of client-go. Then the packages in your GOPATH will be the only copy
* or run `godep save` in your application folder to flatten all dependencies.

### Contributing code
Please send pull requests against the client packages in the Kubernetes main [repository](https://github.com/kubernetes/kubernetes). Changes in the staging area will be published to this repository every day.
This repository holds supplementary Go libraries for text processing, many involving Unicode.


# Semantic Versioning
This repo uses Semantic versioning (http://semver.org/), so
1. MAJOR version when you make incompatible API changes,
1. MINOR version when you add functionality in a backwards-compatible manner,
   and
1. PATCH version when you make backwards-compatible bug fixes.

A Unicode major and minor version bump is mapped to a major version bump in
x/text.
A path version bump in Unicode is mapped to a minor version bump in x/text.
Note that, consistent with the definitions in semver, until version 1.0.0 of
x/text is reached, the minor version is considered a major version.
So going from 0.1.0 to 0.2.0 is considered to be a major version bump.

A major new CLDR version is mapped to a minor version increase in x/text.
Any other new CLDR version is mapped to a patch version increase in x/text.


# Contribute
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
This repository holds supplementary Go networking libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
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
# What is diskv?

Diskv (disk-vee) is a simple, persistent key-value store written in the Go
language. It starts with an incredibly simple API for storing arbitrary data on
a filesystem by key, and builds several layers of performance-enhancing
abstraction on top.  The end result is a conceptually simple, but highly
performant, disk-backed storage system.

[![Build Status][1]][2]

[1]: https://drone.io/github.com/peterbourgon/diskv/status.png
[2]: https://drone.io/github.com/peterbourgon/diskv/latest


# Installing

Install [Go 1][3], either [from source][4] or [with a prepackaged binary][5].
Then,

```bash
$ go get github.com/peterbourgon/diskv
```

[3]: http://golang.org
[4]: http://golang.org/doc/install/source
[5]: http://golang.org/doc/install


# Usage

```go
package main

import (
	"fmt"
	"github.com/peterbourgon/diskv"
)

func main() {
	// Simplest transform function: put all the data files into the base dir.
	flatTransform := func(s string) []string { return []string{} }

	// Initialize a new diskv store, rooted at "my-data-dir", with a 1MB cache.
	d := diskv.New(diskv.Options{
		BasePath:     "my-data-dir",
		Transform:    flatTransform,
		CacheSizeMax: 1024 * 1024,
	})

	// Write three bytes to the key "alpha".
	key := "alpha"
	d.Write(key, []byte{'1', '2', '3'})

	// Read the value back out of the store.
	value, _ := d.Read(key)
	fmt.Printf("%v\n", value)

	// Erase the key+value from the store (and the disk).
	d.Erase(key)
}
```

More complex examples can be found in the "examples" subdirectory.


# Theory

## Basic idea

At its core, diskv is a map of a key (`string`) to arbitrary data (`[]byte`).
The data is written to a single file on disk, with the same name as the key.
The key determines where that file will be stored, via a user-provided
`TransformFunc`, which takes a key and returns a slice (`[]string`)
corresponding to a path list where the key file will be stored. The simplest
TransformFunc,

```go
func SimpleTransform (key string) []string {
    return []string{}
}
```

will place all keys in the same, base directory. The design is inspired by
[Redis diskstore][6]; a TransformFunc which emulates the default diskstore
behavior is available in the content-addressable-storage example.

[6]: http://groups.google.com/group/redis-db/browse_thread/thread/d444bc786689bde9?pli=1

**Note** that your TransformFunc should ensure that one valid key doesn't
transform to a subset of another valid key. That is, it shouldn't be possible
to construct valid keys that resolve to directory names. As a concrete example,
if your TransformFunc splits on every 3 characters, then

```go
d.Write("abcabc", val) // OK: written to <base>/abc/abc/abcabc
d.Write("abc", val)    // Error: attempted write to <base>/abc/abc, but it's a directory
```

This will be addressed in an upcoming version of diskv.

Probably the most important design principle behind diskv is that your data is
always flatly available on the disk. diskv will never do anything that would
prevent you from accessing, copying, backing up, or otherwise interacting with
your data via common UNIX commandline tools.

## Adding a cache

An in-memory caching layer is provided by combining the BasicStore
functionality with a simple map structure, and keeping it up-to-date as
appropriate. Since the map structure in Go is not threadsafe, it's combined
with a RWMutex to provide safe concurrent access.

## Adding order

diskv is a key-value store and therefore inherently unordered. An ordering
system can be injected into the store by passing something which satisfies the
diskv.Index interface. (A default implementation, using Google's
[btree][7] package, is provided.) Basically, diskv keeps an ordered (by a
user-provided Less function) index of the keys, which can be queried.

[7]: https://github.com/google/btree

## Adding compression

Something which implements the diskv.Compression interface may be passed
during store creation, so that all Writes and Reads are filtered through
a compression/decompression pipeline. Several default implementations,
using stdlib compression algorithms, are provided. Note that data is cached
compressed; the cost of decompression is borne with each Read.

## Streaming

diskv also now provides ReadStream and WriteStream methods, to allow very large
data to be handled efficiently.


# Future plans

 * Needs plenty of robust testing: huge datasets, etc...
 * More thorough benchmarking
 * Your suggestions for use-cases I haven't thought of
httpcache
=========

[![Build Status](https://travis-ci.org/gregjones/httpcache.svg?branch=master)](https://travis-ci.org/gregjones/httpcache) [![GoDoc](https://godoc.org/github.com/gregjones/httpcache?status.svg)](https://godoc.org/github.com/gregjones/httpcache)

Package httpcache provides a http.RoundTripper implementation that works as a mostly RFC-compliant cache for http responses.

It is only suitable for use as a 'private' cache (i.e. for a web-browser or an API-client and not for a shared proxy).

Cache Backends
--------------

- The built-in 'memory' cache stores responses in an in-memory map.
- [`github.com/gregjones/httpcache/diskcache`](https://github.com/gregjones/httpcache/tree/master/diskcache) provides a filesystem-backed cache using the [diskv](https://github.com/peterbourgon/diskv) library.
- [`github.com/gregjones/httpcache/memcache`](https://github.com/gregjones/httpcache/tree/master/memcache) provides memcache implementations, for both App Engine and 'normal' memcache servers.
- [`sourcegraph.com/sourcegraph/s3cache`](https://sourcegraph.com/github.com/sourcegraph/s3cache) uses Amazon S3 for storage.
- [`github.com/gregjones/httpcache/leveldbcache`](https://github.com/gregjones/httpcache/tree/master/leveldbcache) provides a filesystem-backed cache using [leveldb](https://github.com/syndtr/goleveldb/leveldb).
- [`github.com/die-net/lrucache`](https://github.com/die-net/lrucache) provides an in-memory cache that will evict least-recently used entries.
- [`github.com/die-net/lrucache/twotier`](https://github.com/die-net/lrucache/tree/master/twotier) allows caches to be combined, for example to use lrucache above with a persistent disk-cache.

License
-------

-	[MIT License](LICENSE.txt)
# Go support for Protocol Buffers

[![Build Status](https://travis-ci.org/golang/protobuf.svg?branch=master)](https://travis-ci.org/golang/protobuf)

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


## Using protocol buffers with Go ##

Once the software is installed, there are two steps to using it.
First you must compile the protocol buffer definitions and then import
them, with the support library, into your program.

To compile the protocol buffer definition, run protoc with the --go_out
parameter set to the directory you want to output the Go code to.

	protoc --go_out=. *.proto

The generated files will be suffixed .pb.go.  See the Test code below
for an example using such a file.


The package comment for the proto library contains text describing
the interface provided in Go for protocol buffers. Here is an edited
version.

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
	syntax = "proto2";
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

		"github.com/golang/protobuf/proto"
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


	protoc --go_out=plugins=grpc,import_path=mypackage:. *.proto


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

	protoc --go_out=plugins=grpc:. *.proto

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

The `protoc-gen-go/generator` package exposes a plugin interface,
which is used by the gRPC code generation. This interface is not
supported and is subject to incompatible changes without notice.
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
# BTree implementation for Go

![Travis CI Build Status](https://api.travis-ci.org/google/btree.svg?branch=master)

This package provides an in-memory B-Tree implementation for Go, useful as
an ordered, mutable data structure.

The API is based off of the wonderful
http://godoc.org/github.com/petar/GoLLRB/llrb, and is meant to allow btree to
act as a drop-in replacement for gollrb trees.

See http://godoc.org/github.com/google/btree for documentation.
[![Build Status](https://travis-ci.org/googleapis/gnostic.svg?branch=master)](https://travis-ci.org/googleapis/gnostic)

# ⨁ gnostic

This repository contains a Go command line tool which converts
JSON and YAML [OpenAPI](https://github.com/OAI/OpenAPI-Specification)
descriptions to and from equivalent Protocol Buffer representations.

[Protocol Buffers](https://developers.google.com/protocol-buffers/)
provide a language-neutral, platform-neutral, extensible mechanism
for serializing structured data.
**gnostic**'s Protocol Buffer models for the OpenAPI Specification
can be used to generate code that includes data structures with 
explicit fields for the elements of an OpenAPI description.
This makes it possible for developers to work with OpenAPI
descriptions in type-safe ways, which is particularly useful
in strongly-typed languages like Go and Swift.

**gnostic** reads OpenAPI descriptions into
these generated data structures, reports errors,
resolves internal dependencies, and writes the results
in a binary form that can be used in any language that is
supported by the Protocol Buffer tools.
A plugin interface simplifies integration with API
tools written in a variety of different languages,
and when necessary, Protocol Buffer OpenAPI descriptions
can be reexported as JSON or YAML.

**gnostic** compilation code and OpenAPI Protocol Buffer
models are automatically generated from an
[OpenAPI JSON Schema](https://github.com/OAI/OpenAPI-Specification/blob/master/schemas/v2.0/schema.json).
Source code for the generator is in the [generate-gnostic](generate-gnostic) directory.

## Disclaimer

This is prerelease software and work in progress. Feedback and
contributions are welcome, but we currently make no guarantees of
function or stability.

## Requirements

**gnostic** can be run in any environment that supports [Go](http://golang.org)
and the [Google Protocol Buffer Compiler](https://github.com/google/protobuf).

## Installation

1. Get this package by downloading it with `go get`.

        go get github.com/googleapis/gnostic
  
2. [Optional] Build and run the compiler generator. 
This uses the OpenAPI JSON schema to generate a Protocol Buffer language file 
that describes the OpenAPI specification and a Go-language file of code that 
will read a JSON or YAML OpenAPI representation into the generated protocol 
buffers. Pre-generated versions of these files are in the OpenAPIv2 directory.

        cd $GOPATH/src/github.com/googleapis/gnostic/generate-gnostic
        go install
        cd ..
        generate-gnostic --v2

3. [Optional] Generate Protocol Buffer support code. 
A pre-generated version of this file is checked into the OpenAPIv2 directory.
This step requires a local installation of protoc, the Protocol Buffer Compiler.
You can get protoc [here](https://github.com/google/protobuf).

        ./COMPILE-PROTOS.sh

4. [Optional] Rebuild **gnostic**. This is only necessary if you've performed steps
2 or 3 above.

        go install github.com/googleapis/gnostic

5. Run **gnostic**. This will create a file in the current directory named "petstore.pb" that contains a binary
Protocol Buffer description of a sample API.

        gnostic --pb-out=. examples/petstore.json

6. You can also compile files that you specify with a URL. Here's another way to compile the previous 
example. This time we're creating "petstore.text", which contains a textual representation of the
Protocol Buffer description. This is mainly for use in testing and debugging.

        gnostic --text-out=petstore.text https://raw.githubusercontent.com/googleapis/gnostic/master/examples/petstore.json

7. For a sample application, see apps/report.

        go install github.com/googleapis/gnostic/apps/report
        report petstore.pb

8. **gnostic** supports plugins. This builds and runs a sample plugin
that reports some basic information about an API. The "-" causes the plugin to 
write its output to stdout.

        go install github.com/googleapis/gnostic/plugins/gnostic-go-sample
        gnostic examples/petstore.json --go-sample-out=-

## Copyright

Copyright 2017, Google Inc.

## License

Released under the Apache 2.0 license.
# Extensions

This directory contains support code for building Gnostic extensions and associated examples.

Extensions are used to compile vendor or specification extensions into protocol buffer structures.
# OpenAPI v2 Protocol Buffer Models

This directory contains a Protocol Buffer-language model
and related code for supporting OpenAPI v2.

Gnostic applications and plugins can use OpenAPIv2.proto
to generate Protocol Buffer support code for their preferred languages.

OpenAPIv2.go is used by Gnostic to read JSON and YAML OpenAPI 
descriptions into the Protocol Buffer-based datastructures 
generated from OpenAPIv2.proto.

OpenAPIv2.proto and OpenAPIv2.go are generated by the Gnostic 
compiler generator, and OpenAPIv2.pb.go is generated by 
protoc, the Protocol Buffer compiler, and protoc-gen-go, the
Protocol Buffer Go code generation plugin.
# Compiler support code

This directory contains compiler support code used by Gnostic and Gnostic extensions.[![Sourcegraph](https://sourcegraph.com/github.com/json-iterator/go/-/badge.svg)](https://sourcegraph.com/github.com/json-iterator/go?badge)
[![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/json-iterator/go)
[![Build Status](https://travis-ci.org/json-iterator/go.svg?branch=master)](https://travis-ci.org/json-iterator/go)
[![codecov](https://codecov.io/gh/json-iterator/go/branch/master/graph/badge.svg)](https://codecov.io/gh/json-iterator/go)
[![rcard](https://goreportcard.com/badge/github.com/json-iterator/go)](https://goreportcard.com/report/github.com/json-iterator/go)
[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](https://raw.githubusercontent.com/json-iterator/go/master/LICENSE)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/json-iterator/Lobby)

A high-performance 100% compatible drop-in replacement of "encoding/json"

```
Go开发者们请加入我们，滴滴出行平台技术部 taowen@didichuxing.com
```

# Benchmark

![benchmark](http://jsoniter.com/benchmarks/go-benchmark.png)

Source code: https://github.com/json-iterator/go-benchmark/blob/master/src/github.com/json-iterator/go-benchmark/benchmark_medium_payload_test.go

Raw Result (easyjson requires static code generation)

| | ns/op | allocation bytes | allocation times |
| --- | --- | --- | --- |
| std decode | 35510 ns/op | 1960 B/op | 99 allocs/op |
| easyjson decode | 8499 ns/op | 160 B/op | 4 allocs/op |
| jsoniter decode | 5623 ns/op | 160 B/op | 3 allocs/op |
| std encode | 2213 ns/op | 712 B/op | 5 allocs/op |
| easyjson encode | 883 ns/op | 576 B/op | 3 allocs/op |
| jsoniter encode | 837 ns/op | 384 B/op | 4 allocs/op |

# Usage

100% compatibility with standard lib

Replace

```go
import "encoding/json"
json.Marshal(&data)
```

with 

```go
import "github.com/json-iterator/go"
jsoniter.Marshal(&data)
```

Replace

```go
import "encoding/json"
json.Unmarshal(input, &data)
```

with

```go
import "github.com/json-iterator/go"
jsoniter.Unmarshal(input, &data)
```

[More documentation](http://jsoniter.com/migrate-from-go-std.html)

# How to get

```
go get github.com/json-iterator/go
```

# Contribution Welcomed !

Contributors

* [thockin](https://github.com/thockin) 
* [mattn](https://github.com/mattn)
* [cch123](https://github.com/cch123)
* [Oleg Shaldybin](https://github.com/olegshaldybin)
* [Jason Toffaletti](https://github.com/toffaletti)

Report issue or pull request, or email taowen@gmail.com, or [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/json-iterator/Lobby)
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

© 2017, ernestmicklei.com.  MIT License. Contributions welcome.GoGoProtobuf http://github.com/gogo/protobuf extends 
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
# GoLLRB

GoLLRB is a Left-Leaning Red-Black (LLRB) implementation of 2-3 balanced binary
search trees in Go Language.

## Overview

As of this writing and to the best of the author's knowledge, 
Go still does not have a balanced binary search tree (BBST) data structure.
These data structures are quite useful in a variety of cases. A BBST maintains
elements in sorted order under dynamic updates (inserts and deletes) and can
support various order-specific queries. Furthermore, in practice one often
implements other common data structures like Priority Queues, using BBST's.

2-3 trees (a type of BBST's), as well as the runtime-similar 2-3-4 trees, are
the de facto standard BBST algoritms found in implementations of Python, Java,
and other libraries. The LLRB method of implementing 2-3 trees is a recent
improvement over the traditional implementation. The LLRB approach was
discovered relatively recently (in 2008) by Robert Sedgewick of Princeton
University.

GoLLRB is a Go implementation of LLRB 2-3 trees.

## Maturity

GoLLRB has been used in some pretty heavy-weight machine learning tasks over many gigabytes of data.
I consider it to be in stable, perhaps even production, shape. There are no known bugs.

## Installation

With a healthy Go Language installed, simply run `go get github.com/petar/GoLLRB/llrb`

## Example
    
	package main

	import (
		"fmt"
		"github.com/petar/GoLLRB/llrb"
	)

	func lessInt(a, b interface{}) bool { return a.(int) < b.(int) }

	func main() {
		tree := llrb.New(lessInt)
		tree.ReplaceOrInsert(1)
		tree.ReplaceOrInsert(2)
		tree.ReplaceOrInsert(3)
		tree.ReplaceOrInsert(4)
		tree.DeleteMin()
		tree.Delete(4)
		c := tree.IterAscend()
		for {
			u := <-c
			if u == nil {
				break
			}
			fmt.Printf("%d\n", int(u.(int)))
		}
	}

## About

GoLLRB was written by [Petar Maymounkov](http://pdos.csail.mit.edu/~petar/). 

Follow me on [Twitter @maymounkov](http://www.twitter.com/maymounkov)!
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
# Swag [![Build Status](https://travis-ci.org/go-openapi/swag.svg?branch=master)](https://travis-ci.org/go-openapi/swag) [![codecov](https://codecov.io/gh/go-openapi/swag/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/swag) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

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
#### VPNKit iptables wrapper for dockerd

This is an iptables wrapper that will call `vpnkit-expose-port` when a swarm port is published by `dockerd` inside the guest VM. The wrapper has to be installed as `iptables` in $PATH in a location that comes before the regular iptables. It expects regular iptables to exist in `/sbin/iptables`.

If the file `/var/config/vpnkit/native-port-forwarding` exists and contains a `0` all requests will be passed directly to `/sbin/iptables`, disabling the wrapper.

# vpnkit-register-uuid

`vpnkit` associates ethernet clients with UUIDs. When a client reconnects, it provides
the same UUID as it used in the past and then it will be allocated the same MAC
and DHCP IP address.

`vpnkit-register-uuid` calls vpnkit to register a given UUID and returns the IP address.
This allows the following sequence:

1. read a UUID from a config file (or generate a fresh one)
2. use `vpnkit-register-uuid` to register the UUID and discover the IP
3. start a VM with [hyperkit](https://github.com/moby/hyperkit) with a VIF using this UUID
4. connect to a service running in the VM using the IP
