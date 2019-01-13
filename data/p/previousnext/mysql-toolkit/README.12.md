See https://github.com/samneirinck/posh-dockerThese files under this directory are for reference only. 

They are used by Jenkins for CI runs.Docker: the container engine [![Release](https://img.shields.io/github/release/docker/docker.svg)](https://github.com/docker/docker/releases/latest)
============================

Docker is an open source project to pack, ship and run any application
as a lightweight container.

Docker containers are both *hardware-agnostic* and *platform-agnostic*.
This means they can run anywhere, from your laptop to the largest
cloud compute instance and everything in between - and they don't require
you to use a particular language, framework or packaging system. That
makes them great building blocks for deploying and scaling web apps,
databases, and backend services without depending on a particular stack
or provider.

Docker began as an open-source implementation of the deployment engine which
powered [dotCloud](http://web.archive.org/web/20130530031104/https://www.dotcloud.com/),
a popular Platform-as-a-Service. It benefits directly from the experience
accumulated over several years of large-scale operation and support of hundreds
of thousands of applications and databases.

![Docker logo](docs/static_files/docker-logo-compressed.png "Docker")

## Security Disclosure

Security is very important to us. If you have any issue regarding security,
please disclose the information responsibly by sending an email to
security@docker.com and not by creating a GitHub issue.

## Better than VMs

A common method for distributing applications and sandboxing their
execution is to use virtual machines, or VMs. Typical VM formats are
VMware's vmdk, Oracle VirtualBox's vdi, and Amazon EC2's ami. In theory
these formats should allow every developer to automatically package
their application into a "machine" for easy distribution and deployment.
In practice, that almost never happens, for a few reasons:

  * *Size*: VMs are very large which makes them impractical to store
     and transfer.
  * *Performance*: running VMs consumes significant CPU and memory,
    which makes them impractical in many scenarios, for example local
    development of multi-tier applications, and large-scale deployment
    of cpu and memory-intensive applications on large numbers of
    machines.
  * *Portability*: competing VM environments don't play well with each
     other. Although conversion tools do exist, they are limited and
     add even more overhead.
  * *Hardware-centric*: VMs were designed with machine operators in
    mind, not software developers. As a result, they offer very
    limited tooling for what developers need most: building, testing
    and running their software. For example, VMs offer no facilities
    for application versioning, monitoring, configuration, logging or
    service discovery.

By contrast, Docker relies on a different sandboxing method known as
*containerization*. Unlike traditional virtualization, containerization
takes place at the kernel level. Most modern operating system kernels
now support the primitives necessary for containerization, including
Linux with [openvz](https://openvz.org),
[vserver](http://linux-vserver.org) and more recently
[lxc](https://linuxcontainers.org/), Solaris with
[zones](https://docs.oracle.com/cd/E26502_01/html/E29024/preface-1.html#scrolltoc),
and FreeBSD with
[Jails](https://www.freebsd.org/doc/handbook/jails.html).

Docker builds on top of these low-level primitives to offer developers a
portable format and runtime environment that solves all four problems.
Docker containers are small (and their transfer can be optimized with
layers), they have basically zero memory and cpu overhead, they are
completely portable, and are designed from the ground up with an
application-centric design.

Perhaps best of all, because Docker operates at the OS level, it can still be
run inside a VM!

## Plays well with others

Docker does not require you to buy into a particular programming
language, framework, packaging system, or configuration language.

Is your application a Unix process? Does it use files, tcp connections,
environment variables, standard Unix streams and command-line arguments
as inputs and outputs? Then Docker can run it.

Can your application's build be expressed as a sequence of such
commands? Then Docker can build it.

## Escape dependency hell

A common problem for developers is the difficulty of managing all
their application's dependencies in a simple and automated way.

This is usually difficult for several reasons:

  * *Cross-platform dependencies*. Modern applications often depend on
    a combination of system libraries and binaries, language-specific
    packages, framework-specific modules, internal components
    developed for another project, etc. These dependencies live in
    different "worlds" and require different tools - these tools
    typically don't work well with each other, requiring awkward
    custom integrations.

  * *Conflicting dependencies*. Different applications may depend on
    different versions of the same dependency. Packaging tools handle
    these situations with various degrees of ease - but they all
    handle them in different and incompatible ways, which again forces
    the developer to do extra work.

  * *Custom dependencies*. A developer may need to prepare a custom
    version of their application's dependency. Some packaging systems
    can handle custom versions of a dependency, others can't - and all
    of them handle it differently.


Docker solves the problem of dependency hell by giving the developer a simple
way to express *all* their application's dependencies in one place, while
streamlining the process of assembling them. If this makes you think of
[XKCD 927](https://xkcd.com/927/), don't worry. Docker doesn't
*replace* your favorite packaging systems. It simply orchestrates
their use in a simple and repeatable way. How does it do that? With
layers.

Docker defines a build as running a sequence of Unix commands, one
after the other, in the same container. Build commands modify the
contents of the container (usually by installing new files on the
filesystem), the next command modifies it some more, etc. Since each
build command inherits the result of the previous commands, the
*order* in which the commands are executed expresses *dependencies*.

Here's a typical Docker build process:

```bash
FROM ubuntu:12.04
RUN apt-get update && apt-get install -y python python-pip curl
RUN curl -sSL https://github.com/shykes/helloflask/archive/master.tar.gz | tar -xzv
RUN cd helloflask-master && pip install -r requirements.txt
```

Note that Docker doesn't care *how* dependencies are built - as long
as they can be built by running a Unix command in a container.


Getting started
===============

Docker can be installed either on your computer for building applications or
on servers for running them. To get started, [check out the installation
instructions in the
documentation](https://docs.docker.com/engine/installation/).

Usage examples
==============

Docker can be used to run short-lived commands, long-running daemons
(app servers, databases, etc.), interactive shell sessions, etc.

You can find a [list of real-world
examples](https://docs.docker.com/engine/examples/) in the
documentation.

Under the hood
--------------

Under the hood, Docker is built on the following components:

* The
  [cgroups](https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt)
  and
  [namespaces](http://man7.org/linux/man-pages/man7/namespaces.7.html)
  capabilities of the Linux kernel
* The [Go](https://golang.org) programming language
* The [Docker Image Specification](https://github.com/docker/docker/blob/master/image/spec/v1.md)
* The [Libcontainer Specification](https://github.com/opencontainers/runc/blob/master/libcontainer/SPEC.md)

Contributing to Docker [![GoDoc](https://godoc.org/github.com/docker/docker?status.svg)](https://godoc.org/github.com/docker/docker)
======================

| **Master** (Linux) | **Experimental** (Linux) | **Windows** | **FreeBSD** |
|------------------|----------------------|---------|---------|
| [![Jenkins Build Status](https://jenkins.dockerproject.org/view/Docker/job/Docker%20Master/badge/icon)](https://jenkins.dockerproject.org/view/Docker/job/Docker%20Master/) | [![Jenkins Build Status](https://jenkins.dockerproject.org/view/Docker/job/Docker%20Master%20%28experimental%29/badge/icon)](https://jenkins.dockerproject.org/view/Docker/job/Docker%20Master%20%28experimental%29/) | [![Build Status](http://jenkins.dockerproject.org/job/Docker%20Master%20(windows)/badge/icon)](http://jenkins.dockerproject.org/job/Docker%20Master%20(windows)/) | [![Build Status](http://jenkins.dockerproject.org/job/Docker%20Master%20(freebsd)/badge/icon)](http://jenkins.dockerproject.org/job/Docker%20Master%20(freebsd)/) |

Want to hack on Docker? Awesome! We have [instructions to help you get
started contributing code or documentation](https://docs.docker.com/opensource/project/who-written-for/).

These instructions are probably not perfect, please let us know if anything
feels wrong or incomplete. Better yet, submit a PR and improve them yourself.

Getting the development builds
==============================

Want to run Docker from a master build? You can download
master builds at [master.dockerproject.org](https://master.dockerproject.org).
They are updated with each commit merged into the master branch.

Don't know how to use that super cool new feature in the master build? Check
out the master docs at
[docs.master.dockerproject.org](http://docs.master.dockerproject.org).

How the project is run
======================

Docker is a very, very active project. If you want to learn more about how it is run,
or want to get more involved, the best place to start is [the project directory](https://github.com/docker/docker/tree/master/project).

We are always open to suggestions on process improvements, and are always looking for more maintainers.

### Talking to other Docker users and contributors

<table class="tg">
  <col width="45%">
  <col width="65%">
  <tr>
    <td>Internet&nbsp;Relay&nbsp;Chat&nbsp;(IRC)</td>
    <td>
      <p>
        IRC is a direct line to our most knowledgeable Docker users; we have
        both the  <code>#docker</code> and <code>#docker-dev</code> group on
        <strong>irc.freenode.net</strong>.
        IRC is a rich chat protocol but it can overwhelm new users. You can search
        <a href="https://botbot.me/freenode/docker/#" target="_blank">our chat archives</a>.
      </p>
      Read our <a href="https://docs.docker.com/opensource/get-help/#/irc-quickstart" target="_blank">IRC quickstart guide</a> for an easy way to get started.
    </td>
  </tr>
  <tr>
    <td>Docker Community Forums</td>
    <td>
      The <a href="https://forums.docker.com/c/open-source-projects/de" target="_blank">Docker Engine</a>
      group is for users of the Docker Engine project.
    </td>
  </tr>
  <tr>
    <td>Google Groups</td>
    <td>
      The <a href="https://groups.google.com/forum/#!forum/docker-dev"
      target="_blank">docker-dev</a> group is for contributors and other people
      contributing to the Docker project.  You can join this group without a
      Google account by sending an email to <a
      href="mailto:docker-dev+subscribe@googlegroups.com">docker-dev+subscribe@googlegroups.com</a>.
      You'll receive a join-request message; simply reply to the message to
      confirm your subscription.
    </td>
  </tr>
  <tr>
    <td>Twitter</td>
    <td>
      You can follow <a href="https://twitter.com/docker/" target="_blank">Docker's Twitter feed</a>
      to get updates on our products. You can also tweet us questions or just
      share blogs or stories.
    </td>
  </tr>
  <tr>
    <td>Stack Overflow</td>
    <td>
      Stack Overflow has over 7000 Docker questions listed. We regularly
      monitor <a href="https://stackoverflow.com/search?tab=newest&q=docker" target="_blank">Docker questions</a>
      and so do many other knowledgeable Docker users.
    </td>
  </tr>
</table>

### Legal

*Brought to you courtesy of our legal counsel. For more context,
please see the [NOTICE](https://github.com/docker/docker/blob/master/NOTICE) document in this repo.*

Use and transfer of Docker may be subject to certain restrictions by the
United States and other governments.

It is your responsibility to ensure that your use and/or transfer does not
violate applicable laws.

For more information, please see https://www.bis.doc.gov


Licensing
=========
Docker is licensed under the Apache License, Version 2.0. See
[LICENSE](https://github.com/docker/docker/blob/master/LICENSE) for the full
license text.

Other Docker Related Projects
=============================
There are a number of projects under development that are based on Docker's
core technology. These projects expand the tooling built around the
Docker platform to broaden its application and utility.

* [Docker Registry](https://github.com/docker/distribution): Registry
server for Docker (hosting/delivery of repositories and images)
* [Docker Machine](https://github.com/docker/machine): Machine management
for a container-centric world
* [Docker Swarm](https://github.com/docker/swarm): A Docker-native clustering
system
* [Docker Compose](https://github.com/docker/compose) (formerly Fig):
Define and run multi-container apps
* [Kitematic](https://github.com/docker/kitematic): The easiest way to use
Docker on Mac and Windows

If you know of another project underway that should be listed here, please help
us keep this list up-to-date by submitting a PR.

Awesome-Docker
==============
You can find more projects, tools and articles related to Docker on the [awesome-docker list](https://github.com/veggiemonk/awesome-docker). Add your project there.
# Working on the Engine API

The Engine API is an HTTP API used by the command-line client to communicate with the daemon. It can also be used by third-party software to control the daemon.

It consists of various components in this repository:

- `api/swagger.yaml` A Swagger definition of the API.
- `api/types/` Types shared by both the client and server, representing various objects, options, responses, etc. Most are written manually, but some are automatically generated from the Swagger definition. See [#27919](https://github.com/docker/docker/issues/27919) for progress on this.
- `cli/` The command-line client.
- `client/` The Go client used by the command-line client. It can also be used by third-party Go programs.
- `daemon/` The daemon, which serves the API.

## Swagger definition

The API is defined by the [Swagger](http://swagger.io/specification/) definition in `api/swagger.yaml`. This definition can be used to:

1. To automatically generate documentation.
2. To automatically generate the Go server and client. (A work-in-progress.)
3. Provide a machine readable version of the API for introspecting what it can do, automatically generating clients for other languages, etc.

## Updating the API documentation

The API documentation is generated entirely from `api/swagger.yaml`. If you make updates to the API, you'll need to edit this file to represent the change in the documentation.

The file is split into two main sections:

- `definitions`, which defines re-usable objects used in requests and responses
- `paths`, which defines the API endpoints (and some inline objects which don't need to be reusable)

To make an edit, first look for the endpoint you want to edit under `paths`, then make the required edits. Endpoints may reference reusable objects with `$ref`, which can be found in the `definitions` section.

There is hopefully enough example material in the file for you to copy a similar pattern from elsewhere in the file (e.g. adding new fields or endpoints), but for the full reference, see the [Swagger specification](https://github.com/docker/docker/issues/27919)

`swagger.yaml` is validated by `hack/validate/swagger` to ensure it is a valid Swagger definition. This is useful for when you are making edits to ensure you are doing the right thing.

## Viewing the API documentation

When you make edits to `swagger.yaml`, you may want to check the generated API documentation to ensure it renders correctly.

All the documentation generation is done in the documentation repository, [docker/docker.github.io](https://github.com/docker/docker.github.io). The Swagger definition is vendored periodically into this repository, but you can manually copy over the Swagger definition to test changes.

Copy `api/swagger.yaml` in this repository to `engine/api/[VERSION_NUMBER]/swagger.yaml` in the documentation repository, overwriting what is already there. Then, run `docker-compose up` in the documentation repository and browse to [http://localhost:4000/engine/api/](http://localhost:4000/engine/api/) when it finishes rendering.
## Legacy API type versions

This package includes types for legacy API versions. The stable version of the API types live in `api/types/*.go`.

Consider moving a type here when you need to keep backwards compatibility in the API. This legacy types are organized by the latest API version they appear in. For instance, types in the `v1p19` package are valid for API versions below or equal `1.19`. Types in the `v1p20` package are valid for the API version `1.20`, since the versions below that will use the legacy types in `v1p19`.

### Package name conventions

The package name convention is to use `v` as a prefix for the version number and `p`(patch) as a separator. We use this nomenclature due to a few restrictions in the Go package name convention:

1. We cannot use `.` because it's interpreted by the language, think of `v1.20.CallFunction`.
2. We cannot use `_` because golint complains about it. The code is actually valid, but it looks probably more weird: `v1_20.CallFunction`.

For instance, if you want to modify a type that was available in the version `1.21` of the API but it will have different fields in the version `1.22`, you want to create a new package under `api/types/versions/v1p21`.
pkg/ is a collection of utility packages used by the Docker project without being specific to its internals.

Utility packages are kept separate from the docker core codebase to keep it as small and concise as possible.
If some utilities grow larger and their APIs stabilize, they may be moved to their own repository under the
Docker organization, to facilitate re-use by other projects. However that is not the priority.

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
	return data[name]
}

func (i *important) Create(name string, data interface{}) {
	i.locks.Lock(name)
	defer i.locks.Unlock(name)

	i.createImportant(data)

	s.mu.Lock()
	i.data[name] = data
	s.mu.Unlock()
}

func (i *important) createImportant(data interface{}) {
	time.Sleep(10 * time.Second)
}
```

For functions dealing with a given name, always lock at the beginning of the
function (or before doing anything with the underlying state), this ensures any
other function that is dealing with the same name will block.

When needing to modify the underlying data, use the global lock to ensure nothing
else is modfying it at the same time.
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
- `-o` is the output file where the the generated code should go

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
$ docker daemon -H=<node_ip:2376> --cluster-advertise=<node_ip:2376> --cluster-store etcd://<etcd_ip1>,<etcd_ip2>/<path>
```

### Using consul

Point your Docker Engine instances to a common Consul instance. You can specify
the address Docker uses to advertise the node using the `--cluster-advertise`
flag.

```bash
$ docker daemon -H=<node_ip:2376> --cluster-advertise=<node_ip:2376> --cluster-store consul://<consul_ip>/<path>
```

### Using zookeeper

Point your Docker Engine instances to a common Zookeeper instance. You can specify
the address Docker uses to advertise the node using the `--cluster-advertise`
flag.

```bash
$ docker daemon -H=<node_ip:2376> --cluster-advertise=<node_ip:2376> --cluster-store zk://<zk_addr1>,<zk_addr2>/<path>
```
This package provides helper functions for dealing with strings
This package provides helper functions to pack version information into a single User-Agent header.
This package provides helper functions for dealing with signals across various operating systemsThis package provides helper functions for dealing with string identifiers
## reexec

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
    /usr/bin/docker daemon -H=tcp://0.0.0.0:2375
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

If you're a *contributor* or aspiring contributor, you should read [CONTRIBUTORS.md](../CONTRIBUTING.md).

If you're a *maintainer* or aspiring maintainer, you should read [MAINTAINERS](../MAINTAINERS).

If you're a *packager* or aspiring packager, you should read [PACKAGERS.md](./PACKAGERS.md).

If you're a maintainer in charge of a *release*, you should read [RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md).

## Roadmap

A high-level roadmap is available at [ROADMAP.md](../ROADMAP.md).


## Build tools

[hack/make.sh](../hack/make.sh) is the primary build tool for docker. It is used for compiling the official binary,
running the test suite, and pushing releases.
## devicemapper - a storage backend based on Device Mapper

### Theory of operation

The device mapper graphdriver uses the device mapper thin provisioning
module (dm-thinp) to implement CoW snapshots. The preferred model is
to have a thin pool reserved outside of Docker and passed to the
daemon via the `--storage-opt dm.thinpooldev` option.

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

### Information on `docker info`

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

#### status items

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

### About the devicemapper options

The devicemapper backend supports some options that you can specify
when starting the docker daemon using the `--storage-opt` flags.
This uses the `dm` prefix and would be used something like `docker daemon --storage-opt dm.foo=bar`.

These options are currently documented both in [the man
page](../../../man/docker.1.md) and in [the online
documentation](https://docs.docker.com/engine/reference/commandline/dockerd/#/storage-driver-options).
If you add an options, update both the `man` page and the documentation.
# The non-reference docs have been moved!

<!-- This file is maintained within the docker/docker Github
     repository at https://github.com/docker/docker/. Make all
     pull requests against that repo. If you see this file in
     another repository, consider it read-only there, as it will
     periodically be overwritten by the definitive file. Pull
     requests which include edits to this file in other repositories
     will be rejected.
-->

The documentation for Docker Engine has been merged into
[the general documentation repo](https://github.com/docker/docker.github.io).

See the [README](https://github.com/docker/docker.github.io/blob/master/README.md)
for instructions on contributing to and building the documentation.

If you'd like to edit the current published version of the Engine docs,
do it in the master branch here:
https://github.com/docker/docker.github.io/tree/master/engine

If you need to document the functionality of an upcoming Engine release,
use the `vnext-engine` branch:
https://github.com/docker/docker.github.io/tree/vnext-engine/engine

The reference docs have been left in docker/docker (this repo), which remains
the place to edit them.

The docs in the general repo are open-source and we appreciate
your feedback and pull requests!
docker.go contains Docker daemon's main function.

This file provides first line CLI argument parsing and environment variable setting.
Docker Documentation
====================

This directory contains scripts for generating the man pages. Many of the man
pages are generated directly from the `spf13/cobra` `Command` definition. Some
legacy pages are still generated from the markdown files in this directory.
Do *not* edit the man pages in the man1 directory. Instead, update the
Cobra command or amend the Markdown files for legacy pages.


## Generate the man pages

From within the project root directory run:

    make manpages
This directory holds scripts called by `make.sh` in the parent directory.

Each script is named after the bundle it creates.
They should not be called directly - instead, pass it as argument to make.sh, for example:

```
./hack/make.sh test
./hack/make.sh binary ubuntu

# Or to run all bundles:
./hack/make.sh
```

To add a bundle:

* Create a shell-compatible file here
* Add it to $DEFAULT_BUNDLES in make.sh
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
# Docker Experimental Features

This page contains a list of features in the Docker engine which are
experimental. Experimental features are **not** ready for production. They are
provided for test and evaluation in your sandbox environments.

The information below describes each feature and the GitHub pull requests and
issues associated with it. If necessary, links are provided to additional
documentation on an issue.  As an active Docker user and community member,
please feel free to provide any feedback on these features you wish.

## Use Docker experimental

Experimental features are now included in the standard Docker binaries as of
version 1.13.0.
To enable experimental features, start the Docker daemon with the
`--experimental` flag or enable the daemon flag in the
`/etc/docker/daemon.json` configuration file:

```json
{
    "experimental": true
}
```

You can check to see if experimental features are enabled on a running daemon
using the following command:

```bash
$ docker version -f '{{.Server.Experimental}}'
true
```

## Current experimental features

Docker service logs command to view logs for a Docker service. This is needed in Swarm mode.
Option to squash image layers to the base image after successful builds.
Checkpoint and restore support for Containers.
Metrics (Prometheus) output for basic container, image, and daemon operations.

 * The top-level [docker deploy](../../docs/reference/deploy.md) command. The
   `docker stack deploy` command is **not** experimental.
 * [`docker service logs` command](../docs/reference/commandline/service_logs.md)
 * [`--squash` option to `docker build` command](../docs/reference/commandline/build.md##squash-an-images-layers---squash-experimental-only)
 * [External graphdriver plugins](../docs/extend/plugins_graphdriver.md)
 * [Ipvlan Network Drivers](vlan-networks.md)
 * [Distributed Application Bundles](docker-stacks-and-bundles.md)
 * [Checkpoint & Restore](checkpoint-restore.md)

## How to comment on an experimental feature

Each feature's documentation includes a list of proposal pull requests or PRs associated with the feature. If you want to comment on or suggest a change to a feature, please add it to the existing feature PR.

Issues or problems with a feature? Inquire for help on the `#docker` IRC channel or on the [Docker Google group](https://groups.google.com/forum/#!forum/docker-user).
