## Introduction

docker-credential-helpers is a suite of programs to use native stores to keep Docker credentials safe.

## Installation

Go to the [Releases](https://github.com/docker/docker-credential-helpers/releases) page and download the binary that works better for you. Put that binary in your `$PATH`, so Docker can find it.

### Building from scratch

The programs in this repository are written with the Go programming language. These instructions assume that you have previous knowledge about the language and you have it installed in your machine.

1 - Download the source and put it in your `$GOPATH` with `go get`.

```
$ go get github.com/docker/docker-credential-helpers
```

2 - Use `make` to build the program you want. That will leave any executable in the `bin` directory inside the repository.

```
$ cd $GOPATH/docker/docker-credentials-helpers
$ make osxkeychain
```

3 - Put that binary in your `$PATH`, so Docker can find it.

## Usage

### With the Docker Engine

Set the `credsStore` option in your `.docker/config.json` file with the suffix of the program you want to use. For instance, set it to `osxkeychain` if you want to use `docker-credential-osxkeychain`.

```json
{
  "credsStore": "osxkeychain"
}
```

### With other command line applications

The sub-package [client](https://godoc.org/github.com/docker/docker-credential-helpers/client) includes
functions to call external programs from your own command line applications.

There are three things you need to know if you need to interact with a helper:

1. The name of the program to execute, for instance `docker-credential-osxkeychain`.
2. The server address to identify the credentials, for instance `https://example.com`.
3. The username and secret to store, when you want to store credentials.

You can see examples of each function in the [client](https://godoc.org/github.com/docker/docker-credential-helpers/client) documentation.

### Available programs

1. osxkeychain: Provides a helper to use the OS X keychain as credentials store.
2. secretservice: Provides a helper to use the D-Bus secret service as credentials store.
3. wincred: Provides a helper to use Windows credentials manager as store.
4. pass: Provides a helper to use `pass` as credentials store.

#### Note

`pass` needs to be configured for `docker-credential-pass` to work properly.
It must be initialized with a `gpg2` key ID. Make sure your GPG key exists is in `gpg2` keyring as `pass` uses `gpg2` instead of the regular `gpg`.

## Development

A credential helper can be any program that can read values from the standard input. We use the first argument in the command line to differentiate the kind of command to execute. There are four valid values:

- `store`: Adds credentials to the keychain. The payload in the standard input is a JSON document with `ServerURL`, `Username` and `Secret`.
- `get`: Retrieves credentials from the keychain. The payload in the standard input is the raw value for the `ServerURL`.
- `erase`: Removes credentials from the keychain. The payload in the standard input is the raw value for the `ServerURL`.
- `list`: Lists stored credentials. There is no standard input payload.

This repository also includes libraries to implement new credentials programs in Go. Adding a new helper program is pretty easy. You can see how the OS X keychain helper works in the [osxkeychain](osxkeychain) directory.

1. Implement the interface `credentials.Helper` in `YOUR_PACKAGE/YOUR_PACKAGE_$GOOS.go`
2. Create a main program in `YOUR_PACKAGE/cmd/main_$GOOS.go`.
3. Add make tasks to build your program and run tests.

## License

MIT. See [LICENSE](LICENSE) for more information.
The Moby Project
================

![Moby Project logo](docs/static_files/moby-project-logo.png "The Moby Project")

Moby is an open-source project created by Docker to enable and accelerate software containerization.

It provides a "Lego set" of toolkit components, the framework for assembling them into custom container-based systems, and a place for all container enthusiasts and professionals to experiment and exchange ideas.
Components include container build tools, a container registry, orchestration tools, a runtime and more, and these can be used as building blocks in conjunction with other tools and projects.

## Principles

Moby is an open project guided by strong principles, aiming to be modular, flexible and without too strong an opinion on user experience.
It is open to the community to help set its direction.

- Modular: the project includes lots of components that have well-defined functions and APIs that work together.
- Batteries included but swappable: Moby includes enough components to build fully featured container system, but its modular architecture ensures that most of the components can be swapped by different implementations.
- Usable security: Moby provides secure defaults without compromising usability.
- Developer focused: The APIs are intended to be functional and useful to build powerful tools.
They are not necessarily intended as end user tools but as components aimed at developers.
Documentation and UX is aimed at developers not end users.

## Audience

The Moby Project is intended for engineers, integrators and enthusiasts looking to modify, hack, fix, experiment, invent and build systems based on containers.
It is not for people looking for a commercially supported system, but for people who want to work and learn with open source code.

## Relationship with Docker

The components and tools in the Moby Project are initially the open source components that Docker and the community have built for the Docker Project.
New projects can be added if they fit with the community goals. Docker is committed to using Moby as the upstream for the Docker Product.
However, other projects are also encouraged to use Moby as an upstream, and to reuse the components in diverse ways, and all these uses will be treated in the same way. External maintainers and contributors are welcomed.

The Moby project is not intended as a location for support or feature requests for Docker products, but as a place for contributors to work on open source code, fix bugs, and make the code more useful.
The releases are supported by the maintainers, community and users, on a best efforts basis only, and are not intended for customers who want enterprise or commercial support; Docker EE is the appropriate product for these use cases.

-----

Legal
=====

*Brought to you courtesy of our legal counsel. For more context,
please see the [NOTICE](https://github.com/moby/moby/blob/master/NOTICE) document in this repo.*

Use and transfer of Moby may be subject to certain restrictions by the
United States and other governments.

It is your responsibility to ensure that your use and/or transfer does not
violate applicable laws.

For more information, please see https://www.bis.doc.gov

Licensing
=========
Moby is licensed under the Apache License, Version 2.0. See
[LICENSE](https://github.com/moby/moby/blob/master/LICENSE) for the full
license text.
# Working on the Engine API

The Engine API is an HTTP API used by the command-line client to communicate with the daemon. It can also be used by third-party software to control the daemon.

It consists of various components in this repository:

- `api/swagger.yaml` A Swagger definition of the API.
- `api/types/` Types shared by both the client and server, representing various objects, options, responses, etc. Most are written manually, but some are automatically generated from the Swagger definition. See [#27919](https://github.com/docker/docker/issues/27919) for progress on this.
- `cli/` The command-line client.
- `client/` The Go client used by the command-line client. It can also be used by third-party Go programs.
- `daemon/` The daemon, which serves the API.

## Swagger definition

The API is defined by the [Swagger](http://swagger.io/specification/) definition in `api/swagger.yaml`. This definition can be used to:

1. Automatically generate documentation.
2. Automatically generate the Go server and client. (A work-in-progress.)
3. Provide a machine readable version of the API for introspecting what it can do, automatically generating clients for other languages, etc.

## Updating the API documentation

The API documentation is generated entirely from `api/swagger.yaml`. If you make updates to the API, edit this file to represent the change in the documentation.

The file is split into two main sections:

- `definitions`, which defines re-usable objects used in requests and responses
- `paths`, which defines the API endpoints (and some inline objects which don't need to be reusable)

To make an edit, first look for the endpoint you want to edit under `paths`, then make the required edits. Endpoints may reference reusable objects with `$ref`, which can be found in the `definitions` section.

There is hopefully enough example material in the file for you to copy a similar pattern from elsewhere in the file (e.g. adding new fields or endpoints), but for the full reference, see the [Swagger specification](https://github.com/docker/docker/issues/27919).

`swagger.yaml` is validated by `hack/validate/swagger` to ensure it is a valid Swagger definition. This is useful when making edits to ensure you are doing the right thing.

## Viewing the API documentation

When you make edits to `swagger.yaml`, you may want to check the generated API documentation to ensure it renders correctly.

Run `make swagger-docs` and a preview will be running at `http://localhost`. Some of the styling may be incorrect, but you'll be able to ensure that it is generating the correct documentation.

The production documentation is generated by vendoring `swagger.yaml` into [docker/docker.github.io](https://github.com/docker/docker.github.io).
# Legacy API type versions

This package includes types for legacy API versions. The stable version of the API types live in `api/types/*.go`.

Consider moving a type here when you need to keep backwards compatibility in the API. This legacy types are organized by the latest API version they appear in. For instance, types in the `v1p19` package are valid for API versions below or equal `1.19`. Types in the `v1p20` package are valid for the API version `1.20`, since the versions below that will use the legacy types in `v1p19`.

## Package name conventions

The package name convention is to use `v` as a prefix for the version number and `p`(patch) as a separator. We use this nomenclature due to a few restrictions in the Go package name convention:

1. We cannot use `.` because it's interpreted by the language, think of `v1.20.CallFunction`.
2. We cannot use `_` because golint complains about it. The code is actually valid, but it looks probably more weird: `v1_20.CallFunction`.

For instance, if you want to modify a type that was available in the version `1.21` of the API but it will have different fields in the version `1.22`, you want to create a new package under `api/types/versions/v1p21`.
pkg/ is a collection of utility packages used by the Moby project without being specific to its internals.

Utility packages are kept separate from the moby core codebase to keep it as small and concise as possible.
If some utilities grow larger and their APIs stabilize, they may be moved to their own repository under the
Moby organization, to facilitate re-use by other projects. However that is not the priority.

The directory `pkg` is named after the same directory in the camlistore project. Since Brad is a core
Go maintainer, we thought it made sense to copy his methods for organizing Go code :) Thanks Brad!

Because utility packages are small and neatly separated from the rest of the codebase, they are a good
place to start for aspiring maintainers and contributors. Get in touch if you want to help maintain them!
Locker
=====

locker provides a mechanism for creating finer-grained locking to help
free up more global locks to handle other tasks.

The implementation looks close to a sync.Mutex, however, the user must provide a
reference to use to refer to the underlying lock when locking and unlocking,
and unlock may generate an error.

If a lock with a given name does not exist when `Lock` is called, one is
created.
Lock references are automatically cleaned up on `Unlock` if nothing else is
waiting for the lock.


## Usage

```go
package important

import (
	"sync"
	"time"

	"github.com/docker/docker/pkg/locker"
)

type important struct {
	locks *locker.Locker
	data  map[string]interface{}
	mu    sync.Mutex
}

func (i *important) Get(name string) interface{} {
	i.locks.Lock(name)
	defer i.locks.Unlock(name)
	return i.data[name]
}

func (i *important) Create(name string, data interface{}) {
	i.locks.Lock(name)
	defer i.locks.Unlock(name)

	i.createImportant(data)

	i.mu.Lock()
	i.data[name] = data
	i.mu.Unlock()
}

func (i *important) createImportant(data interface{}) {
	time.Sleep(10 * time.Second)
}
```

For functions dealing with a given name, always lock at the beginning of the
function (or before doing anything with the underlying state), this ensures any
other function that is dealing with the same name will block.

When needing to modify the underlying data, use the global lock to ensure nothing
else is modifying it at the same time.
Since name lock is already in place, no reads will occur while the modification
is being performed.

SysInfo stores information about which features a kernel supports.
This code provides helper functions for dealing with archive files.
Plugin RPC Generator
====================

Generates go code from a Go interface definition for proxying between the plugin
API and the subsystem being extended.

## Usage

Given an interface definition:

```go
type volumeDriver interface {
	Create(name string, opts opts) (err error)
	Remove(name string) (err error)
	Path(name string) (mountpoint string, err error)
	Mount(name string) (mountpoint string, err error)
	Unmount(name string) (err error)
}
```

**Note**: All function options and return values must be named in the definition.

Run the generator:

```bash
$ pluginrpc-gen --type volumeDriver --name VolumeDriver -i volumes/drivers/extpoint.go -o volumes/drivers/proxy.go
```

Where:
- `--type` is the name of the interface to use
- `--name` is the subsystem that the plugin "Implements"
- `-i` is the input file containing the interface definition
- `-o` is the output file where the generated code should go

**Note**: The generated code will use the same package name as the one defined in the input file

Optionally, you can skip functions on the interface that should not be
implemented in the generated proxy code by passing in the function name to `--skip`.
This flag can be specified multiple times.

You can also add build tags that should be prepended to the generated code by
supplying `--tag`. This flag can be specified multiple times.

## Known issues

## go-generate

You can also use this with go-generate, which is pretty awesome.  
To do so, place the code at the top of the file which contains the interface
definition (i.e., the input file):

```go
//go:generate pluginrpc-gen -i $GOFILE -o proxy.go -type volumeDriver -name VolumeDriver
```

Then cd to the package dir and run `go generate`

**Note**: the `pluginrpc-gen` binary must be within your `$PATH`
---
page_title: Docker discovery
page_description: discovery
page_keywords: docker, clustering, discovery
---

# Discovery

Docker comes with multiple Discovery backends.

## Backends

### Using etcd

Point your Docker Engine instances to a common etcd instance. You can specify
the address Docker uses to advertise the node using the `--cluster-advertise`
flag.

```bash
$ dockerd -H=<node_ip:2376> --cluster-advertise=<node_ip:2376> --cluster-store etcd://<etcd_ip1>,<etcd_ip2>/<path>
```

### Using consul

Point your Docker Engine instances to a common Consul instance. You can specify
the address Docker uses to advertise the node using the `--cluster-advertise`
flag.

```bash
$ dockerd -H=<node_ip:2376> --cluster-advertise=<node_ip:2376> --cluster-store consul://<consul_ip>/<path>
```

### Using zookeeper

Point your Docker Engine instances to a common Zookeeper instance. You can specify
the address Docker uses to advertise the node using the `--cluster-advertise`
flag.

```bash
$ dockerd -H=<node_ip:2376> --cluster-advertise=<node_ip:2376> --cluster-store zk://<zk_addr1>,<zk_addr2>/<path>
```
This package provides helper functions to pack version information into a single User-Agent header.
This package provides helper functions for dealing with signals across various operating systemsThis package provides helper functions for dealing with string identifiers
# reexec

The `reexec` package facilitates the busybox style reexec of the docker binary that we require because 
of the forking limitations of using Go.  Handlers can be registered with a name and the argv 0 of 
the exec of the binary will be used to find and execute custom init paths.
Package symlink implements EvalSymlinksInScope which is an extension of filepath.EvalSymlinks,
as well as a Windows long-path aware version of filepath.EvalSymlinks
from the [Go standard library](https://golang.org/pkg/path/filepath).

The code from filepath.EvalSymlinks has been adapted in fs.go.
Please read the LICENSE.BSD file that governs fs.go and LICENSE.APACHE for fs_test.go.
The `contrib` directory contains scripts, images, and other helpful things
which are not part of the core docker distribution. Please note that they
could be out of date, since they do not receive the same attention as the
rest of the repository.
Docker device tool for devicemapper storage driver backend
===================

The ./contrib/docker-device-tool contains a tool to manipulate devicemapper thin-pool.

Compile
========

    $ make shell
    ## inside build container
    $ go build contrib/docker-device-tool/device_tool.go

    # if devicemapper version is old and compilation fails, compile with `libdm_no_deferred_remove` tag
    $ go build -tags libdm_no_deferred_remove contrib/docker-device-tool/device_tool.go
# Vagrant integration

Currently there are at least 4 different projects that we are aware of that deals
with integration with [Vagrant](http://vagrantup.com/) at different levels. One
approach is to use Docker as a [provisioner](http://docs.vagrantup.com/v2/provisioning/index.html)
which means you can create containers and pull base images on VMs using Docker's
CLI and the other is to use Docker as a [provider](http://docs.vagrantup.com/v2/providers/index.html),
meaning you can use Vagrant to control Docker containers.


### Provisioners

* [Vocker](https://github.com/fgrehm/vocker)
* [Ventriloquist](https://github.com/fgrehm/ventriloquist)

### Providers

* [docker-provider](https://github.com/fgrehm/docker-provider)
* [vagrant-shell](https://github.com/destructuring/vagrant-shell)

## Setting up Vagrant-docker with the Engine API

The initial Docker upstart script will not work because it runs on `127.0.0.1`, which is not accessible to the host machine. Instead, we need to change the script to connect to `0.0.0.0`. To do this, modify `/etc/init/docker.conf` to look like this:

```
description     "Docker daemon"

start on filesystem
stop on runlevel [!2345]

respawn

script
    /usr/bin/dockerd -H=tcp://0.0.0.0:2375
end script
```

Once that's done, you need to set up an SSH tunnel between your host machine and the vagrant machine that's running Docker. This can be done by running the following command in a host terminal:

```
ssh -L 2375:localhost:2375 -p 2222 vagrant@localhost
```

(The first 2375 is what your host can connect to, the second 2375 is what port Docker is running on in the vagrant machine, and the 2222 is the port Vagrant is providing for SSH. If VirtualBox is the VM you're using, you can see what value "2222" should be by going to: Network > Adapter 1 > Advanced > Port Forwarding in the VirtualBox GUI.)

Note that because the port has been changed, to run docker commands from within the command line you must run them like this:

```
sudo docker -H 0.0.0.0:2375 < commands for docker >
```
SELinux policy for docker
# `dockercore/builder-rpm`

This image's tags contain the dependencies for building Docker `.rpm`s for each of the RPM-based platforms Docker targets.

To add new tags, see [`contrib/builder/rpm/amd64` in https://github.com/docker/docker](https://github.com/docker/docker/tree/master/contrib/builder/rpm/amd64), specifically the `generate.sh` script, whose usage is described in a comment at the top of the file.
# `dockercore/builder-deb`

This image's tags contain the dependencies for building Docker `.deb`s for each of the Debian-based platforms Docker targets.

To add new tags, see [`contrib/builder/deb/amd64` in https://github.com/docker/docker](https://github.com/docker/docker/tree/master/contrib/builder/deb/amd64), specifically the `generate.sh` script, whose usage is described in a comment at the top of the file.
SELinux policy for docker
Desktop Integration
===================

The ./contrib/desktop-integration contains examples of typical dockerized
desktop applications.

Examples
========

* Chromium: ./chromium/Dockerfile shows a way to dockerize a common application
* Gparted: ./gparted/Dockerfile shows a way to dockerize a common application w devices
# Docker.tmbundle

Dockerfile syntax highlighting for TextMate and Sublime Text.

## Install

### Sublime Text

Available for Sublime Text under [package control](https://sublime.wbond.net/packages/Dockerfile%20Syntax%20Highlighting).
Search for *Dockerfile Syntax Highlighting*

### TextMate 2

You can install this bundle in TextMate by opening the preferences and going to the bundles tab. After installation it will be automatically updated for you.

enjoy.

dockerfile.vim
==============

Syntax highlighting for Dockerfiles

Installation
------------
With [pathogen](https://github.com/tpope/vim-pathogen), the usual way...

With [Vundle](https://github.com/gmarik/Vundle.vim)
  
    Plugin 'docker/docker' , {'rtp': '/contrib/syntax/vim/'}

Features
--------

The syntax highlighting includes:

* The directives (e.g. `FROM`)
* Strings
* Comments

License
-------

BSD, short and sweet
Dockerfile.nanorc
=================

Dockerfile syntax highlighting for nano

Single User Installation
------------------------
1. Create a nano syntax directory in your home directory:
 * `mkdir -p ~/.nano/syntax`

2. Copy `Dockerfile.nanorc` to` ~/.nano/syntax/`
 * `cp Dockerfile.nanorc ~/.nano/syntax/`

3. Add the following to your `~/.nanorc` to tell nano where to find the `Dockerfile.nanorc` file
  ```
## Dockerfile files
include "~/.nano/syntax/Dockerfile.nanorc"
  ```

System Wide Installation
------------------------
1. Create a nano syntax directory: 
  * `mkdir /usr/local/share/nano`

2. Copy `Dockerfile.nanorc` to `/usr/local/share/nano`
  * `cp Dockerfile.nanorc /usr/local/share/nano/`

3. Add the following to your `/etc/nanorc`:
  ```
## Dockerfile files
include "/usr/local/share/nano/Dockerfile.nanorc"
  ```
# Hacking on Docker

The `project/` directory holds information and tools for everyone involved in the process of creating and
distributing Docker, specifically:

## Guides

If you're a *contributor* or aspiring contributor, you should read [CONTRIBUTING.md](../CONTRIBUTING.md).

If you're a *maintainer* or aspiring maintainer, you should read [MAINTAINERS](../MAINTAINERS).

If you're a *packager* or aspiring packager, you should read [PACKAGERS.md](./PACKAGERS.md).

If you're a maintainer in charge of a *release*, you should read [RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md).

## Roadmap

A high-level roadmap is available at [ROADMAP.md](../ROADMAP.md).


## Build tools

[hack/make.sh](../hack/make.sh) is the primary build tool for docker. It is used for compiling the official binary,
running the test suite, and pushing releases.
# devicemapper - a storage backend based on Device Mapper

## Theory of operation

The device mapper graphdriver uses the device mapper thin provisioning
module (dm-thinp) to implement CoW snapshots. The preferred model is
to have a thin pool reserved outside of Docker and passed to the
daemon via the `--storage-opt dm.thinpooldev` option. Alternatively,
the device mapper graphdriver can setup a block device to handle this
for you via the `--storage-opt dm.directlvm_device` option.

As a fallback if no thin pool is provided, loopback files will be
created.  Loopback is very slow, but can be used without any
pre-configuration of storage.  It is strongly recommended that you do
not use loopback in production.  Ensure your Docker daemon has a
`--storage-opt dm.thinpooldev` argument provided.

In loopback, a thin pool is created at `/var/lib/docker/devicemapper`
(devicemapper graph location) based on two block devices, one for
data and one for metadata. By default these block devices are created
automatically by using loopback mounts of automatically created sparse
files.

The default loopback files used are
`/var/lib/docker/devicemapper/devicemapper/data` and
`/var/lib/docker/devicemapper/devicemapper/metadata`. Additional metadata
required to map from docker entities to the corresponding devicemapper
volumes is stored in the `/var/lib/docker/devicemapper/devicemapper/json`
file (encoded as Json).

In order to support multiple devicemapper graphs on a system, the thin
pool will be named something like: `docker-0:33-19478248-pool`, where
the `0:33` part is the minor/major device nr and `19478248` is the
inode number of the `/var/lib/docker/devicemapper` directory.

On the thin pool, docker automatically creates a base thin device,
called something like `docker-0:33-19478248-base` of a fixed
size. This is automatically formatted with an empty filesystem on
creation. This device is the base of all docker images and
containers. All base images are snapshots of this device and those
images are then in turn used as snapshots for other images and
eventually containers.

## Information on `docker info`

As of docker-1.4.1, `docker info` when using the `devicemapper` storage driver
will display something like:

	$ sudo docker info
	[...]
	Storage Driver: devicemapper
	 Pool Name: docker-253:1-17538953-pool
	 Pool Blocksize: 65.54 kB
	 Base Device Size: 107.4 GB
	 Data file: /dev/loop4
	 Metadata file: /dev/loop4
	 Data Space Used: 2.536 GB
	 Data Space Total: 107.4 GB
	 Data Space Available: 104.8 GB
	 Metadata Space Used: 7.93 MB
	 Metadata Space Total: 2.147 GB
	 Metadata Space Available: 2.14 GB
	 Udev Sync Supported: true
	 Data loop file: /home/docker/devicemapper/devicemapper/data
	 Metadata loop file: /home/docker/devicemapper/devicemapper/metadata
	 Library Version: 1.02.82-git (2013-10-04)
	[...]

### status items

Each item in the indented section under `Storage Driver: devicemapper` are
status information about the driver.
 *  `Pool Name` name of the devicemapper pool for this driver.
 *  `Pool Blocksize` tells the blocksize the thin pool was initialized with. This only changes on creation.
 *  `Base Device Size` tells the maximum size of a container and image
 *  `Data file` blockdevice file used for the devicemapper data
 *  `Metadata file` blockdevice file used for the devicemapper metadata
 *  `Data Space Used` tells how much of `Data file` is currently used
 *  `Data Space Total` tells max size the `Data file`
 *  `Data Space Available` tells how much free space there is in the `Data file`. If you are using a loop device this will report the actual space available to the loop device on the underlying filesystem.
 *  `Metadata Space Used` tells how much of `Metadata file` is currently used
 *  `Metadata Space Total` tells max size the `Metadata file`
 *  `Metadata Space Available` tells how much free space there is in the `Metadata file`. If you are using a loop device this will report the actual space available to the loop device on the underlying filesystem.
 *  `Udev Sync Supported` tells whether devicemapper is able to sync with Udev. Should be `true`.
 *  `Data loop file` file attached to `Data file`, if loopback device is used
 *  `Metadata loop file` file attached to `Metadata file`, if loopback device is used
 *  `Library Version` from the libdevmapper used

## About the devicemapper options

The devicemapper backend supports some options that you can specify
when starting the docker daemon using the `--storage-opt` flags.
This uses the `dm` prefix and would be used something like `dockerd --storage-opt dm.foo=bar`.

These options are currently documented both in [the man
page](../../../man/docker.1.md) and in [the online
documentation](https://docs.docker.com/engine/reference/commandline/dockerd/#/storage-driver-options).
If you add an options, update both the `man` page and the documentation.
### Get set up for Moby development

 * [README first](who-written-for.md)
 * [Get the required software](software-required.md)
 * [Set up for development on Windows](software-req-win.md)
 * [Configure Git for contributing](set-up-git.md)
 * [Work with a development container](set-up-dev-env.md)
 * [Run tests and test documentation](test.md)
docker.go contains Docker daemon's main function.

This file provides first line CLI argument parsing and environment variable setting.
## About

This directory contains a collection of scripts used to build and manage this
repository. If there are any issues regarding the intention of a particular
script (or even part of a certain script), please reach out to us.
It may help us either refine our current scripts, or add on new ones
that are appropriate for a given use case.

## DinD (dind.sh)

DinD is a wrapper script which allows Docker to be run inside a Docker
container. DinD requires the container to
be run with privileged mode enabled.

## Generate Authors (generate-authors.sh)

Generates AUTHORS; a file with all the names and corresponding emails of
individual contributors. AUTHORS can be found in the home directory of
this repository.

## Make

There are two make files, each with different extensions. Neither are supposed
to be called directly; only invoke `make`. Both scripts run inside a Docker
container.

### make.ps1

- The Windows native build script that uses PowerShell semantics; it is limited
unlike `hack\make.sh` since it does not provide support for the full set of
operations provided by the Linux counterpart, `make.sh`. However, `make.ps1`
does provide support for local Windows development and Windows to Windows CI.
More information is found within `make.ps1` by the author, @jhowardmsft

### make.sh

- Referenced via `make test` when running tests on a local machine,
or directly referenced when running tests inside a Docker development container.  
- When running on a local machine, `make test` to run all tests found in
`test`, `test-unit`, `test-integration`, and `test-docker-py` on
your local machine. The default timeout is set in `make.sh` to 60 minutes
(`${TIMEOUT:=60m}`), since it currently takes up to an hour to run
all of the tests.
- When running inside a Docker development container, `hack/make.sh` does
not have a single target that runs all the tests. You need to provide a
single command line with multiple targets that performs the same thing.
An example referenced from [Run targets inside a development container](https://docs.docker.com/opensource/project/test-and-docs/#run-targets-inside-a-development-container): `root@5f8630b873fe:/go/src/github.com/moby/moby# hack/make.sh dynbinary binary cross test-unit test-integration test-docker-py`
- For more information related to testing outside the scope of this README,
refer to
[Run tests and test documentation](https://docs.docker.com/opensource/project/test-and-docs/)

## Release (release.sh)

Releases any bundles built by `make` on a public AWS S3 bucket.
For information regarding configuration, please view `release.sh`.

## Vendor (vendor.sh)

A shell script that is a wrapper around Vndr. For information on how to use
this, please refer to [vndr's README](https://github.com/LK4D4/vndr/blob/master/README.md)
This directory holds scripts called by `make.sh` in the parent directory.

Each script is named after the bundle it creates.
They should not be called directly - instead, pass it as argument to make.sh, for example:

```
./hack/make.sh binary ubuntu

# Or to run all default bundles:
./hack/make.sh
```

To add a bundle:

* Create a shell-compatible file here
* Add it to $DEFAULT_BUNDLES in make.sh
# Integration Testing on Swarm

IT on Swarm allows you to execute integration test in parallel across a Docker Swarm cluster

## Architecture

### Master service

  - Works as a funker caller
  - Calls a worker funker (`-worker-service`) with a chunk of `-check.f` filter strings (passed as a file via `-input` flag, typically `/mnt/input`)

### Worker service

  - Works as a funker callee
  - Executes an equivalent of `TESTFLAGS=-check.f TestFoo|TestBar|TestBaz ... make test-integration` using the bind-mounted API socket (`docker.sock`)

### Client

  - Controls master and workers via `docker stack`
  - No need to have a local daemon

Typically, the master and workers are supposed to be running on a cloud environment,
while the client is supposed to be running on a laptop, e.g. Docker for Mac/Windows.

## Requirement

  - Docker daemon 1.13 or later
  - Private registry for distributed execution with multiple nodes

## Usage

### Step 1: Prepare images

    $ make build-integration-cli-on-swarm

Following environment variables are known to work in this step:

 - `BUILDFLAGS`
 - `DOCKER_INCREMENTAL_BINARY`

Note: during the transition into Moby Project, you might need to create a symbolic link `$GOPATH/src/github.com/docker/docker` to `$GOPATH/src/github.com/moby/moby`. 

### Step 2: Execute tests

    $ ./hack/integration-cli-on-swarm/integration-cli-on-swarm -replicas 40 -push-worker-image YOUR_REGISTRY.EXAMPLE.COM/integration-cli-worker:latest 

Following environment variables are known to work in this step:

 - `DOCKER_GRAPHDRIVER`
 - `DOCKER_EXPERIMENTAL`

#### Flags

Basic flags:

 - `-replicas N`: the number of worker service replicas. i.e. degree of parallelism.
 - `-chunks N`: the number of chunks. By default, `chunks` == `replicas`.
 - `-push-worker-image REGISTRY/IMAGE:TAG`: push the worker image to the registry. Note that if you have only single node and hence you do not need a private registry, you do not need to specify `-push-worker-image`.

Experimental flags for mitigating makespan nonuniformity:

 - `-shuffle`: Shuffle the test filter strings

Flags for debugging IT on Swarm itself:

 - `-rand-seed N`: the random seed. This flag is useful for deterministic replaying. By default(0), the timestamp is used.
 - `-filters-file FILE`: the file contains `-check.f` strings. By default, the file is automatically generated.
 - `-dry-run`: skip the actual workload
 - `keep-executor`: do not auto-remove executor containers, which is used for running privileged programs on Swarm
# Go client for the Docker Engine API

The `docker` command uses this package to communicate with the daemon. It can also be used by your own Go applications to do anything the command-line interface does – running containers, pulling images, managing swarms, etc.

For example, to list running containers (the equivalent of `docker ps`):

```go
package main

import (
	"context"
	"fmt"

	"github.com/docker/docker/api/types"
	"github.com/docker/docker/client"
)

func main() {
	cli, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

	containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{})
	if err != nil {
		panic(err)
	}

	for _, container := range containers {
		fmt.Printf("%s %s\n", container.ID[:10], container.Image)
	}
}
```

[Full documentation is available on GoDoc.](https://godoc.org/github.com/docker/docker/client)
