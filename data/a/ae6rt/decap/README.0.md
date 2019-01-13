## Decap Web Service

This project's dependencies are managed by the
[dep](https://github.com/golang/dep) tool, which is emerging as the
official Go dependency management tool.

This is the core web service for Decap.  It exposes REST API endoints
for a web UI frontend, and receives post commit hooks from Github
(and eventually other repository managers, including Stash and
Bitbucket), and parses those events and launches a new build in the
build container accordingly.

A given branch on a project is locked in etcd to ensure that only
one container is building this project branch at any one time.  This
may be more important for some projects types than others.

### Post commit hook endpoints

HTTP endpoints for various source code management systems

<table>
    <tr>
        <th>Repository Manager Name</th>
        <th>URL</th>
    </tr>
    <tr>
        <td>Github</td>
        <td>/hooks/github</td>
    </tr>
    <tr>
        <td>Build scripts repository reload</td>
        <td>/hooks/buildscripts</td>
    </tr>
</table>

Github post-commit hooks should be pointed at _/hooks/github_.
Decap will parse the payload and launch a build accordingly.

The _/hooks/buildscripts_ endpoint is a special endpoint that
post-commit hooks on the build-scripts repository should hit.  It
forces a reload of the managed Projects.

### REST API

Read more about the Decap [REST API](https://github.com/ae6rt/decap/wiki/API).

### More information

See the [Developer Getting Started Guide for more information](https://github.com/ae6rt/decap/wiki/Developing)
# client-go

Go clients for talking to a [kubernetes](http://kubernetes.io/) cluster.

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
- [Reporting bugs](#reporting-bugs)
- [Contributing code](#contributing-code)

### What's included

* The `kubernetes` package contains the clientset to access Kubernetes API.
* The `discovery` package is used to discover APIs supported by a Kubernetes API server.
* The `dynamic` package contains a dynamic client that can perform generic operations on arbitrary Kubernetes API objects.
* The `transport` package is used to set up auth and start a connection.
* The `tools/cache` package is useful for writing controllers.

### Versioning

`client-go` version numbers are unrelated to Kubernetes version numbers. Please see the [compatibility matrix](#compatibility-matrix) for the compatible Kubernetes clusters.

`client-go` follows [semver](http://semver.org/). We will not make backwards-incompatible changes without incrementing the major version number. A change is backwards-incompatible either if it *i)* changes the public interfaces of `client-go`, or *ii)* makes `client-go` incompatible with otherwise supported versions of Kubernetes clusters.

We will create a new branch for each increment in the major version number or minor version number. We will create a new tag for each increment in the patch version number. See [semver](http://semver.org/) for definitions of major, minor, and patch.

The master branch will track the head in the main Kubernetes repo and accumulating changes. We will make a new client-go major/minor/patch version when:
* A new major (very rare) or a new minor version is released in the Kubernetes main repository.
* A feature or a bug fix in the master branch is popular and users want it in a stable branch or with a stable tag. 

#### Compatibility: your code <-> client-go

`client-go` follows [semver](http://semver.org/), so until the major version of client-go gets increased, your code will compile and will continue to work with explicitly supported versions of Kubernetes clusters.

#### Compatibility: client-go <-> Kubernetes clusters

`client-go` versions will be backwards compatible with many Kubernetes clusters. As we increment `client-go` versions, we will note which Kubernetes versions we expect them to work with. 

We do not back-port new Kubernetes features into older clients. If you need a new feature, you are expected to upgrade to the new client. You can check out the [CHANGELOG](./CHANGELOG.md) for notable changes.

#### Compatibility matrix

* **client-go/1.4** is compatible with Kubernetes 1.3 through 1.5; it includes all features provided by Kubernetes 1.4.
* **client-go/1.5** is compatible with Kubernetes 1.3 through 1.5; it includes all features provided by Kubernetes 1.4.

#### Why do the 1.4 and 1.5 branch contain top-level folder named after the version?

1.4 and 1.5 branch keep the top-level folders so they do not break the import lines of existing users. These top-level folders are deprecated and are removed from the master branch and future branches.

### How to get it

If you use `go get` to get client-go, **you will get the unstable master branch!** You can `git checkout` a stable branch.

We recommend using a vendor tool, like [godep](https://github.com/tools/godep), [glide](https://github.com/Masterminds/glide), or [govendor](https://github.com/kardianos/govendor) to track a stable version of `client-go`.

### How to use it

If your application runs in a Pod in the cluster, please refer to the in-cluster [example](examples/in-cluster/main.go), otherwise please refer to the out-of-cluster [example](examples/out-of-cluster/main.go).

### Dependency management

If your application depends on a package that client-go depends on, and you let the Go compiler find the dependency in `GOPATH`, you will end up with duplicated dependencies: one copy from the `GOPATH`, and one from the vendor folder of client-go. This will cause unexpected runtime error like flag redefinition, since the go compiler ends up importing both packages separately, even if they are exactly the same thing. If this happens, you can either
* run `godep restore` ([godep](https://github.com/tools/godep)) in the client-go/ folder, then remove the vendor folder of client-go. Then the packages in your GOPATH will be the only copy
* or run `godep save` in your application folder to flatten all dependencies.

### Reporting bugs

Please report bugs to the main Kubernetes [repository](https://github.com/kubernetes/kubernetes/issues/new).

### Contributing code
Please send pull requests against the client packages in the Kubernetes main [repository](https://github.com/kubernetes/kubernetes), and run the `/staging/copy.sh` script to update the staging area in the main repository. Changes in the staging area will be published to this repository every day.
# Third Party Resources Example

This particular example demonstrates how to perform basic operations such as:

* How to register a new ThirdPartyResource (custom Resource type)
* How to create/get/list instances of your new Resource type (update/delete/etc work as well but are not demonstrated) 

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
```This repository holds supplementary Go libraries for text processing, many involving Unicode.

To submit changes to this repository, see http://golang.org/doc/contribute.html.

To generate the tables in this repository (except for the encoding tables),
run go generate from this directory. By default tables are generated for the
Unicode version in core and the CLDR version defined in
golang.org/x/text/unicode/cldr.

Running go generate will as a side effect create a DATA subdirectory in this
directory which holds all files that are used as a source for generating the
tables. This directory will also serve as a cache.

Run

	go test ./...

from this directory to run all tests. Add the "-tags icu" flag to also run
ICU conformance tests (if available). This requires that you have the correct
ICU version installed on your system.

TODO:
- updating unversioned source files.The export directory contains packages that are generated using the x/text
infrastructure, but live elsewhere.
At some point we can expose some of the infrastructure, but for now this
is not done.
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
This repository holds supplementary Go cryptography libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
# OAuth2 for Go

[![Build Status](https://travis-ci.org/golang/oauth2.svg?branch=master)](https://travis-ci.org/golang/oauth2)
[![GoDoc](https://godoc.org/golang.org/x/oauth2?status.svg)](https://godoc.org/golang.org/x/oauth2)

oauth2 package contains a client implementation for OAuth 2.0 spec.

## Installation

~~~~
go get golang.org/x/oauth2
~~~~

See godoc for further documentation and examples.

* [godoc.org/golang.org/x/oauth2](http://godoc.org/golang.org/x/oauth2)
* [godoc.org/golang.org/x/oauth2/google](http://godoc.org/golang.org/x/oauth2/google)


## App Engine

In change 96e89be (March 2015) we removed the `oauth2.Context2` type in favor
of the [`context.Context`](https://golang.org/x/net/context#Context) type from
the `golang.org/x/net/context` package

This means its no longer possible to use the "Classic App Engine"
`appengine.Context` type with the `oauth2` package. (You're using
Classic App Engine if you import the package `"appengine"`.)

To work around this, you may use the new `"google.golang.org/appengine"`
package. This package has almost the same API as the `"appengine"` package,
but it can be fetched with `go get` and used on "Managed VMs" and well as
Classic App Engine.

See the [new `appengine` package's readme](https://github.com/golang/appengine#updating-a-go-app-engine-app)
for information on updating your app.

If you don't want to update your entire app to use the new App Engine packages,
you may use both sets of packages in parallel, using only the new packages
with the `oauth2` package.

	import (
		"golang.org/x/net/context"
		"golang.org/x/oauth2"
		"golang.org/x/oauth2/google"
		newappengine "google.golang.org/appengine"
		newurlfetch "google.golang.org/appengine/urlfetch"

		"appengine"
	)

	func handler(w http.ResponseWriter, r *http.Request) {
		var c appengine.Context = appengine.NewContext(r)
		c.Infof("Logging a message with the old package")

		var ctx context.Context = newappengine.NewContext(r)
		client := &http.Client{
			Transport: &oauth2.Transport{
				Source: google.AppEngineTokenSource(ctx, "scope"),
				Base:   &newurlfetch.Transport{Context: ctx},
			},
		}
		client.Get("...")
	}

## Contributing

We appreciate your help!

To contribute, please read the contribution guidelines:
	https://golang.org/doc/contribute.html

Note that the Go project does not use GitHub pull requests but
uses Gerrit for code reviews. See the contribution guide for details.
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

The yaml package is licensed under the Apache License 2.0. Please see the LICENSE file for details.


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
  -stubs
    	only generate stubs for marshaler/unmarshaler funcs
```

Using `-all` will generate marshalers/unmarshalers for all Go structs in the
file. If `-all` is not provided, then only those structs whose preceeding
comment starts with `easyjson:json` will have marshalers/unmarshalers
generated. For example:

```go
//easyjson:json
struct A{}
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

[go/codec](https://github.com/ugorji/go/codec) provides
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
- [GoogleCloudPlatform/kubernetes](https://github.com/GoogleCloudPlatform/kubernetes)
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
	}

	dest := Foo{
		A: "two",
		B: 2,
	}

	mergo.Merge(&dest, src)

	fmt.Println(dest)
	// Will print
	// {two 2}
}
```

Note: if test are failing due missing package, please execute:

    go get gopkg.in/yaml.v1

## Contact me

If I can help you, you have an idea or you are using Mergo in your projects, don't hesitate to drop me a line (or a pull request): [@im_dario](https://twitter.com/im_dario)

## About

Written by [Dario Castañé](http://dario.im).

## License

[BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) license, as [Go language](http://golang.org/LICENSE).
# go-oidc

[![GoDoc](https://godoc.org/github.com/coreos/go-oidc?status.svg)](https://godoc.org/github.com/coreos/go-oidc)
[![Build Status](https://travis-ci.org/coreos/go-oidc.png?branch=master)](https://travis-ci.org/coreos/go-oidc)

## OpenID Connect support for Go

This package enables OpenID Connect support for the [golang.org/x/oauth2](https://godoc.org/golang.org/x/oauth2) package.

```go
provider, err := oidc.NewProvider(ctx, "https://accounts.google.com")
if err != nil {
    // handle error
}

// Configure an OpenID Connect aware OAuth2 client.
oauth2Config := oauth2.Config{
    ClientID:     clientID,
    ClientSecret: clientSecret,
    RedirectURL:  redirectURL,

    // Discovery returns the OAuth2 endpoints.
    Endpoint: provider.Endpoint(),

    // "openid" is a required scope for OpenID Connect flows.
    Scopes: []string{oidc.ScopeOpenID, "profile", "email"},
}
```

OAuth2 redirects are unchanged.

```go
func handleRedirect(w http.ResponseWriter, r *http.Request) {
    http.Redirect(w, r, oauth2Config.AuthCodeURL(state), http.StatusFound)
}
```

The on responses, the provider can be used to verify ID Tokens.

```go
var verifier = provider.Verifier()

func handleOAuth2Callback(w http.ResponseWriter, r *http.Request) {
    // Verify state and errors.

    oauth2Token, err := oauth2Config.Exchange(ctx, r.URL.Query().Get("code"))
    if err != nil {
        // handle error
    }

    // Extract the ID Token from OAuth2 token.
    rawIDToken, ok := oauth2Token.Extra("id_token").(string)
    if !ok {
        // handle missing token
    }

    // Parse and verify ID Token payload.
    idToken, err := verifier.Verify(ctx, rawIDToken)
    if err != nil {
        // handle error
    }

    // Extract custom claims
    var claims struct {
        Email    string `json:"email"`
        Verified bool   `json:"email_verified"`
    }
    if err := idToken.Claims(&claims); err != nil {
        // handle error
    }
}
```
# Examples

These are example uses of the oidc package. Each requires a Google account and the client ID and secret of a registered OAuth2 application. To create one:

1. Visit your [Google Developer Console][google-developer-console].
2. Click "Credentials" on the left column.
3. Click the "Create credentials" button followed by "OAuth client ID".
4. Select "Web application" and add "http://127.0.0.1:5556/auth/google/callback" as an authorized redirect URI.
5. Click create and add the printed client ID and secret to your environment using the following variables:

```
GOOGLE_OAUTH2_CLIENT_ID
GOOGLE_OAUTH2_CLIENT_SECRET
```

Finally run the examples using the Go tool and navigate to http://127.0.0.1:5556.

```
go run ./example/idtoken/app.go
```
[google-developer-console]: https://console.developers.google.com/apis/dashboard
clockwork
=========

[![Build Status](https://travis-ci.org/jonboulle/clockwork.png?branch=master)](https://travis-ci.org/jonboulle/clockwork)
[![godoc](https://godoc.org/github.com/jonboulle/clockwork?status.svg)](http://godoc.org/github.com/jonboulle/clockwork) 

a simple fake clock for golang

# Usage

Replace uses of the `time` package with the `clockwork.Clock` interface instead.

For example, instead of using `time.Sleep` directly:

```
func my_func() {
	time.Sleep(3 * time.Second)
	do_something()
}
```

inject a clock and use its `Sleep` method instead:

```
func my_func(clock clockwork.Clock) {
	clock.Sleep(3 * time.Second)
	do_something()
}
```

Now you can easily test `my_func` with a `FakeClock`:

```
func TestMyFunc(t *testing.T) {
	c := clockwork.NewFakeClock()

	// Start our sleepy function
	my_func(c)

	// Ensure we wait until my_func is sleeping
	c.BlockUntil(1)

	assert_state()

	// Advance the FakeClock forward in time
	c.Advance(3)

	assert_state()
}
```

and in production builds, simply inject the real clock instead:
```
my_func(clockwork.NewRealClock())
```

See [example_test.go](example_test.go) for a full example.

# Credits

clockwork is inspired by @wickman's [threaded fake clock](https://gist.github.com/wickman/3840816), and the [Golang playground](http://blog.golang.org/playground#Faking time)
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
Google API Extensions for Go
============================

[![Build Status](https://travis-ci.org/googleapis/gax-go.svg?branch=master)](https://travis-ci.org/googleapis/gax-go)
[![Code Coverage](https://img.shields.io/codecov/c/github/googleapis/gax-go.svg)](https://codecov.io/github/googleapis/gax-go)

Google API Extensions for Go (gax-go) is a set of modules which aids the
development of APIs for clients and servers based on `gRPC` and Google API
conventions.

Application code will rarely need to use this library directly,
but the code generated automatically from API definition files can use it
to simplify code generation and to provide more convenient and idiomatic API surface.

**This project is currently experimental and not supported.**

Go Versions
===========
This library requires Go 1.6 or above.

License
=======
BSD - please see [LICENSE](https://github.com/googleapis/gax-go/blob/master/LICENSE)
for more information.
go-restful
==========

package for building REST-style Web Services using Google Go

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
	- Routing algorithm after [JSR311](http://jsr311.java.net/nonav/releases/1.1/spec/spec.html) that is implemented using (but doest **not** accept) regular expressions (See RouterJSR311 which is used by default)
	- Fast routing algorithm that allows static elements, regular expressions and dynamic parameters in the URL path (e.g. /meetings/{id} or /static/{subpath:*}, See CurlyRouter)
- Request API for reading structs from JSON/XML and accesing parameters (path,query,header)
- Response API for writing structs to JSON/XML and setting headers
- Filters for intercepting the request &#8594; response flow on Service or Route level
- Request-scoped variables using attributes
- Containers for WebServices on different HTTP endpoints
- Content encoding (gzip,deflate) of request and response payloads
- Automatic responses on OPTIONS (using a filter)
- Automatic CORS request handling (using a filter)
- API declaration for Swagger UI (see swagger package)
- Panic recovery to produce HTTP 500, customizable using RecoverHandler(...)
- Route errors produce HTTP 404/405/406/415 errors, customizable using ServiceErrorHandler(...)
- Configurable (trace) logging
- Customizable encoding using EntityReaderWriter registration
- Customizable gzip/deflate readers and writers using CompressorProvider registration
	
### Resources

- [Documentation on godoc.org](http://godoc.org/github.com/emicklei/go-restful)
- [Code examples](https://github.com/emicklei/go-restful/tree/master/examples)
- [Example posted on blog](http://ernestmicklei.com/2012/11/24/go-restful-first-working-example/)
- [Design explained on blog](http://ernestmicklei.com/2012/11/11/go-restful-api-design/)
- [sourcegraph](https://sourcegraph.com/github.com/emicklei/go-restful)
- [gopkg.in](https://gopkg.in/emicklei/go-restful.v1)
- [showcase: Mora - MongoDB REST Api server](https://github.com/emicklei/mora)

[![Build Status](https://drone.io/github.com/emicklei/go-restful/status.png)](https://drone.io/github.com/emicklei/go-restful/latest)

(c) 2012 - 2015, http://ernestmicklei.com. MIT License

Type ```git shortlog -s``` for a full list of contributors.How to use Swagger UI with go-restful
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
semver for golang [![Build Status](https://drone.io/github.com/blang/semver/status.png)](https://drone.io/github.com/blang/semver/latest) [![GoDoc](https://godoc.org/github.com/blang/semver?status.png)](https://godoc.org/github.com/blang/semver) [![Coverage Status](https://img.shields.io/coveralls/blang/semver.svg)](https://coveralls.io/r/blang/semver?branch=master)
======

semver is a [Semantic Versioning](http://semver.org/) library written in golang. It fully covers spec version `2.0.0`.

Usage
-----
```bash
$ go get github.com/blang/semver
```
Note: Always vendor your dependencies or fix on a specific version tag.

```go
import github.com/blang/semver
v1, err := semver.Make("1.0.0-beta")
v2, err := semver.Make("2.0.0-beta")
v1.Compare(v2)
```

Also check the [GoDocs](http://godoc.org/github.com/blang/semver).

Why should I use this lib?
-----

- Fully spec compatible
- No reflection
- No regex
- Fully tested (Coverage >99%)
- Readable parsing/validation errors
- Fast (See [Benchmarks](#benchmarks))
- Only Stdlib
- Uses values instead of pointers
- Many features, see below


Features
-----

- Parsing and validation at all levels
- Comparator-like comparisons
- Compare Helper Methods
- InPlace manipulation
- Ranges `>=1.0.0 <2.0.0 || >=3.0.0 !3.0.1-beta.1`
- Sortable (implements sort.Interface)
- database/sql compatible (sql.Scanner/Valuer)
- encoding/json compatible (json.Marshaler/Unmarshaler)

Ranges
------

A `Range` is a set of conditions which specify which versions satisfy the range.

A condition is composed of an operator and a version. The supported operators are:

- `<1.0.0` Less than `1.0.0`
- `<=1.0.0` Less than or equal to `1.0.0`
- `>1.0.0` Greater than `1.0.0`
- `>=1.0.0` Greater than or equal to `1.0.0`
- `1.0.0`, `=1.0.0`, `==1.0.0` Equal to `1.0.0`
- `!1.0.0`, `!=1.0.0` Not equal to `1.0.0`. Excludes version `1.0.0`.

A `Range` can link multiple `Ranges` separated by space:

Ranges can be linked by logical AND:

  - `>1.0.0 <2.0.0` would match between both ranges, so `1.1.1` and `1.8.7` but not `1.0.0` or `2.0.0`
  - `>1.0.0 <3.0.0 !2.0.3-beta.2` would match every version between `1.0.0` and `3.0.0` except `2.0.3-beta.2`

Ranges can also be linked by logical OR:

  - `<2.0.0 || >=3.0.0` would match `1.x.x` and `3.x.x` but not `2.x.x`

AND has a higher precedence than OR. It's not possible to use brackets.

Ranges can be combined by both AND and OR

  - `>1.0.0 <2.0.0 || >3.0.0 !4.2.1` would match `1.2.3`, `1.9.9`, `3.1.1`, but not `4.2.1`, `2.1.1`

Range usage:

```
v, err := semver.Parse("1.2.3")
range, err := semver.ParseRange(">1.0.0 <2.0.0 || >=3.0.0")
if range(v) {
    //valid
}

```

Example
-----

Have a look at full examples in [examples/main.go](examples/main.go)

```go
import github.com/blang/semver

v, err := semver.Make("0.0.1-alpha.preview+123.github")
fmt.Printf("Major: %d\n", v.Major)
fmt.Printf("Minor: %d\n", v.Minor)
fmt.Printf("Patch: %d\n", v.Patch)
fmt.Printf("Pre: %s\n", v.Pre)
fmt.Printf("Build: %s\n", v.Build)

// Prerelease versions array
if len(v.Pre) > 0 {
    fmt.Println("Prerelease versions:")
    for i, pre := range v.Pre {
        fmt.Printf("%d: %q\n", i, pre)
    }
}

// Build meta data array
if len(v.Build) > 0 {
    fmt.Println("Build meta data:")
    for i, build := range v.Build {
        fmt.Printf("%d: %q\n", i, build)
    }
}

v001, err := semver.Make("0.0.1")
// Compare using helpers: v.GT(v2), v.LT, v.GTE, v.LTE
v001.GT(v) == true
v.LT(v001) == true
v.GTE(v) == true
v.LTE(v) == true

// Or use v.Compare(v2) for comparisons (-1, 0, 1):
v001.Compare(v) == 1
v.Compare(v001) == -1
v.Compare(v) == 0

// Manipulate Version in place:
v.Pre[0], err = semver.NewPRVersion("beta")
if err != nil {
    fmt.Printf("Error parsing pre release version: %q", err)
}

fmt.Println("\nValidate versions:")
v.Build[0] = "?"

err = v.Validate()
if err != nil {
    fmt.Printf("Validation failed: %s\n", err)
}
```


Benchmarks
-----

    BenchmarkParseSimple-4           5000000    390    ns/op    48 B/op   1 allocs/op
    BenchmarkParseComplex-4          1000000   1813    ns/op   256 B/op   7 allocs/op
    BenchmarkParseAverage-4          1000000   1171    ns/op   163 B/op   4 allocs/op
    BenchmarkStringSimple-4         20000000    119    ns/op    16 B/op   1 allocs/op
    BenchmarkStringLarger-4         10000000    206    ns/op    32 B/op   2 allocs/op
    BenchmarkStringComplex-4         5000000    324    ns/op    80 B/op   3 allocs/op
    BenchmarkStringAverage-4         5000000    273    ns/op    53 B/op   2 allocs/op
    BenchmarkValidateSimple-4      200000000      9.33 ns/op     0 B/op   0 allocs/op
    BenchmarkValidateComplex-4       3000000    469    ns/op     0 B/op   0 allocs/op
    BenchmarkValidateAverage-4       5000000    256    ns/op     0 B/op   0 allocs/op
    BenchmarkCompareSimple-4       100000000     11.8  ns/op     0 B/op   0 allocs/op
    BenchmarkCompareComplex-4       50000000     30.8  ns/op     0 B/op   0 allocs/op
    BenchmarkCompareAverage-4       30000000     41.5  ns/op     0 B/op   0 allocs/op
    BenchmarkSort-4                  3000000    419    ns/op   256 B/op   2 allocs/op
    BenchmarkRangeParseSimple-4      2000000    850    ns/op   192 B/op   5 allocs/op
    BenchmarkRangeParseAverage-4     1000000   1677    ns/op   400 B/op  10 allocs/op
    BenchmarkRangeParseComplex-4      300000   5214    ns/op  1440 B/op  30 allocs/op
    BenchmarkRangeMatchSimple-4     50000000     25.6  ns/op     0 B/op   0 allocs/op
    BenchmarkRangeMatchAverage-4    30000000     56.4  ns/op     0 B/op   0 allocs/op
    BenchmarkRangeMatchComplex-4    10000000    153    ns/op     0 B/op   0 allocs/op

See benchmark cases at [semver_test.go](semver_test.go)


Motivation
-----

I simply couldn't find any lib supporting the full spec. Others were just wrong or used reflection and regex which i don't like.


Contribution
-----

Feel free to make a pull request. For bigger changes create a issue first to discuss about it.


License
-----

See [LICENSE](LICENSE) file.
# getpasswd in Go [![GoDoc](https://godoc.org/github.com/howeyc/gopass?status.svg)](https://godoc.org/github.com/howeyc/gopass) [![Build Status](https://secure.travis-ci.org/howeyc/gopass.png?branch=master)](http://travis-ci.org/howeyc/gopass)

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
# HttpRouter [![Build Status](https://travis-ci.org/julienschmidt/httprouter.png?branch=master)](https://travis-ci.org/julienschmidt/httprouter) [![Coverage](http://gocover.io/_badge/github.com/julienschmidt/httprouter?0)](http://gocover.io/github.com/julienschmidt/httprouter) [![GoDoc](http://godoc.org/github.com/julienschmidt/httprouter?status.png)](http://godoc.org/github.com/julienschmidt/httprouter)

HttpRouter is a lightweight high performance HTTP request router
(also called *multiplexer* or just *mux* for short) for [Go](http://golang.org/).

In contrast to the [default mux](http://golang.org/pkg/net/http/#ServeMux) of Go's net/http package, this router supports
variables in the routing pattern and matches against the request method.
It also scales better.

The router is optimized for high performance and a small memory footprint.
It scales well even with very long paths and a large number of routes.
A compressing dynamic trie (radix tree) structure is used for efficient matching.

## Features
**Only explicit matches:** With other routers, like [http.ServeMux](http://golang.org/pkg/net/http/#ServeMux),
a requested URL path could match multiple patterns. Therefore they have some
awkward pattern priority rules, like *longest match* or *first registered,
first matched*. By design of this router, a request can only match exactly one
or no route. As a result, there are also no unintended matches, which makes it
great for SEO and improves the user experience.

**Stop caring about trailing slashes:** Choose the URL style you like, the
router automatically redirects the client if a trailing slash is missing or if
there is one extra. Of course it only does so, if the new path has a handler.
If you don't like it, you can [turn off this behavior](http://godoc.org/github.com/julienschmidt/httprouter#Router.RedirectTrailingSlash).

**Path auto-correction:** Besides detecting the missing or additional trailing
slash at no extra cost, the router can also fix wrong cases and remove
superfluous path elements (like `../` or `//`).
Is [CAPTAIN CAPS LOCK](http://www.urbandictionary.com/define.php?term=Captain+Caps+Lock) one of your users?
HttpRouter can help him by making a case-insensitive look-up and redirecting him
to the correct URL.

**Parameters in your routing pattern:** Stop parsing the requested URL path,
just give the path segment a name and the router delivers the dynamic value to
you. Because of the design of the router, path parameters are very cheap.

**Zero Garbage:** The matching and dispatching process generates zero bytes of
garbage. In fact, the only heap allocations that are made, is by building the
slice of the key-value pairs for path parameters. If the request path contains
no parameters, not a single heap allocation is necessary.

**Best Performance:** [Benchmarks speak for themselves](https://github.com/julienschmidt/go-http-routing-benchmark).
See below for technical details of the implementation.

**No more server crashes:** You can set a [Panic handler](http://godoc.org/github.com/julienschmidt/httprouter#Router.PanicHandler) to deal with panics
occurring during handling a HTTP request. The router then recovers and lets the
PanicHandler log what happened and deliver a nice error page.

Of course you can also set **custom [NotFound](http://godoc.org/github.com/julienschmidt/httprouter#Router.NotFound) and  [MethodNotAllowed](http://godoc.org/github.com/julienschmidt/httprouter#Router.MethodNotAllowed) handlers** and [**serve static files**](http://godoc.org/github.com/julienschmidt/httprouter#Router.ServeFiles).

## Usage
This is just a quick introduction, view the [GoDoc](http://godoc.org/github.com/julienschmidt/httprouter) for details.

Let's start with a trivial example:
```go
package main

import (
    "fmt"
    "github.com/julienschmidt/httprouter"
    "net/http"
    "log"
)

func Index(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Welcome!\n")
}

func Hello(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
    fmt.Fprintf(w, "hello, %s!\n", ps.ByName("name"))
}

func main() {
    router := httprouter.New()
    router.GET("/", Index)
    router.GET("/hello/:name", Hello)

    log.Fatal(http.ListenAndServe(":8080", router))
}
```

### Named parameters
As you can see, `:name` is a *named parameter*.
The values are accessible via `httprouter.Params`, which is just a slice of `httprouter.Param`s.
You can get the value of a parameter either by its index in the slice, or by using the `ByName(name)` method:
`:name` can be retrived by `ByName("name")`.

Named parameters only match a single path segment:
```
Pattern: /user/:user

 /user/gordon              match
 /user/you                 match
 /user/gordon/profile      no match
 /user/                    no match
```

**Note:** Since this router has only explicit matches, you can not register static routes and parameters for the same path segment. For example you can not register the patterns `/user/new` and `/user/:user` for the same request method at the same time. The routing of different request methods is independent from each other.

### Catch-All parameters
The second type are *catch-all* parameters and have the form `*name`.
Like the name suggests, they match everything.
Therefore they must always be at the **end** of the pattern:
```
Pattern: /src/*filepath

 /src/                     match
 /src/somefile.go          match
 /src/subdir/somefile.go   match
```

## How does it work?
The router relies on a tree structure which makes heavy use of *common prefixes*,
it is basically a *compact* [*prefix tree*](http://en.wikipedia.org/wiki/Trie)
(or just [*Radix tree*](http://en.wikipedia.org/wiki/Radix_tree)).
Nodes with a common prefix also share a common parent. Here is a short example
what the routing tree for the `GET` request method could look like:

```
Priority   Path             Handle
9          \                *<1>
3          ├s               nil
2          |├earch\         *<2>
1          |└upport\        *<3>
2          ├blog\           *<4>
1          |    └:post      nil
1          |         └\     *<5>
2          ├about-us\       *<6>
1          |        └team\  *<7>
1          └contact\        *<8>
```
Every `*<num>` represents the memory address of a handler function (a pointer).
If you follow a path trough the tree from the root to the leaf, you get the
complete route path, e.g `\blog\:post\`, where `:post` is just a placeholder
([*parameter*](#named-parameters)) for an actual post name. Unlike hash-maps, a
tree structure also allows us to use dynamic parts like the `:post` parameter,
since we actually match against the routing patterns instead of just comparing
hashes. [As benchmarks show](https://github.com/julienschmidt/go-http-routing-benchmark),
this works very well and efficient.

Since URL paths have a hierarchical structure and make use only of a limited set
of characters (byte values), it is very likely that there are a lot of common
prefixes. This allows us to easily reduce the routing into ever smaller problems.
Moreover the router manages a separate tree for every request method.
For one thing it is more space efficient than holding a method->handle map in
every single node, for another thing is also allows us to greatly reduce the
routing problem before even starting the look-up in the prefix-tree.

For even better scalability, the child nodes on each tree level are ordered by
priority, where the priority is just the number of handles registered in sub
nodes (children, grandchildren, and so on..).
This helps in two ways:

1. Nodes which are part of the most routing paths are evaluated first. This
helps to make as much routes as possible to be reachable as fast as possible.
2. It is some sort of cost compensation. The longest reachable path (highest
cost) can always be evaluated first. The following scheme visualizes the tree
structure. Nodes are evaluated from top to bottom and from left to right.

```
├------------
├---------
├-----
├----
├--
├--
└-
```


## Why doesn't this work with http.Handler?
**It does!** The router itself implements the http.Handler interface.
Moreover the router provides convenient [adapters for http.Handler](http://godoc.org/github.com/julienschmidt/httprouter#Router.Handler)s and [http.HandlerFunc](http://godoc.org/github.com/julienschmidt/httprouter#Router.HandlerFunc)s
which allows them to be used as a [httprouter.Handle](http://godoc.org/github.com/julienschmidt/httprouter#Router.Handle) when registering a route.
The only disadvantage is, that no parameter values can be retrieved when a
http.Handler or http.HandlerFunc is used, since there is no efficient way to
pass the values with the existing function parameters.
Therefore [httprouter.Handle](http://godoc.org/github.com/julienschmidt/httprouter#Router.Handle) has a third function parameter.

Just try it out for yourself, the usage of HttpRouter is very straightforward. The package is compact and minimalistic, but also probably one of the easiest routers to set up.


## Where can I find Middleware *X*?
This package just provides a very efficient request router with a few extra
features. The router is just a [http.Handler](http://golang.org/pkg/net/http/#Handler),
you can chain any http.Handler compatible middleware before the router,
for example the [Gorilla handlers](http://www.gorillatoolkit.org/pkg/handlers).
Or you could [just write your own](http://justinas.org/writing-http-middleware-in-go/),
it's very easy!

Alternatively, you could try [a web framework based on HttpRouter](#web-frameworks-based-on-httprouter).

### Multi-domain / Sub-domains
Here is a quick example: Does your server serve multiple domains / hosts?
You want to use sub-domains?
Define a router per host!
```go
// We need an object that implements the http.Handler interface.
// Therefore we need a type for which we implement the ServeHTTP method.
// We just use a map here, in which we map host names (with port) to http.Handlers
type HostSwitch map[string]http.Handler

// Implement the ServerHTTP method on our new type
func (hs HostSwitch) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// Check if a http.Handler is registered for the given host.
	// If yes, use it to handle the request.
	if handler := hs[r.Host]; handler != nil {
		handler.ServeHTTP(w, r)
	} else {
		// Handle host names for wich no handler is registered
		http.Error(w, "Forbidden", 403) // Or Redirect?
	}
}

func main() {
	// Initialize a router as usual
	router := httprouter.New()
	router.GET("/", Index)
	router.GET("/hello/:name", Hello)

	// Make a new HostSwitch and insert the router (our http handler)
	// for example.com and port 12345
	hs := make(HostSwitch)
	hs["example.com:12345"] = router

	// Use the HostSwitch to listen and serve on port 12345
	log.Fatal(http.ListenAndServe(":12345", hs))
}
```

### Basic Authentication
Another quick example: Basic Authentification (RFC 2617) for handles:

```go
package main

import (
    "bytes"
    "encoding/base64"
    "fmt"
    "github.com/julienschmidt/httprouter"
    "net/http"
    "log"
    "strings"
)

func BasicAuth(h httprouter.Handle, user, pass []byte) httprouter.Handle {
	return func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
		const basicAuthPrefix string = "Basic "

		// Get the Basic Authentication credentials
		auth := r.Header.Get("Authorization")
		if strings.HasPrefix(auth, basicAuthPrefix) {
			// Check credentials
			payload, err := base64.StdEncoding.DecodeString(auth[len(basicAuthPrefix):])
			if err == nil {
				pair := bytes.SplitN(payload, []byte(":"), 2)
				if len(pair) == 2 &&
					bytes.Equal(pair[0], user) &&
					bytes.Equal(pair[1], pass) {

					// Delegate request to the given handle
					h(w, r, ps)
					return
				}
			}
		}

		// Request Basic Authentication otherwise
		w.Header().Set("WWW-Authenticate", "Basic realm=Restricted")
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
	}
}

func Index(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Not protected!\n")
}

func Protected(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Protected!\n")
}

func main() {
    user := []byte("gordon")
    pass := []byte("secret!")
    
    router := httprouter.New()
    router.GET("/", Index)
    router.GET("/protected/", BasicAuth(Protected, user, pass))

    log.Fatal(http.ListenAndServe(":8080", router))
}
```

## Chaining with the NotFound handler

**NOTE: It might be required to set [Router.HandleMethodNotAllowed](http://godoc.org/github.com/julienschmidt/httprouter#Router.HandleMethodNotAllowed) to `false` to avoid problems.**

You can use another [http.HandlerFunc](http://golang.org/pkg/net/http/#HandlerFunc), for example another router, to handle requests which could not be matched by this router by using the [Router.NotFound](http://godoc.org/github.com/julienschmidt/httprouter#Router.NotFound) handler. This allows chaining.

### Static files
The `NotFound` handler can for example be used to serve static files from the root path `/` (like an index.html file along with other assets):
```go
// Serve static files from the ./public directory
router.NotFound = http.FileServer(http.Dir("public")).ServeHTTP
```

But this approach sidesteps the strict core rules of this router to avoid routing problems. A cleaner approach is to use a distinct sub-path for serving files, like `/static/*filepath` or `/files/*filepath`.

## Web Frameworks based on HttpRouter
If the HttpRouter is a bit too minimalistic for you, you might try one of the following more high-level 3rd-party web frameworks building upon the HttpRouter package:
* [Ace](https://github.com/plimble/ace): Blazing fast Go Web Framework
* [api2go](https://github.com/univedo/api2go): A JSON API Implementation for Go
* [Gin](https://github.com/gin-gonic/gin): Features a martini-like API with much better performance
* [Goat](https://github.com/bahlo/goat): A minimalistic REST API server in Go
* [Hikaru](https://github.com/najeira/hikaru): Supports standalone and Google AppEngine
* [Hitch](https://github.com/nbio/hitch): Hitch ties httprouter, [httpcontext](https://github.com/nbio/httpcontext), and middleware up in a bow
* [kami](https://github.com/guregu/kami): A tiny web framework using x/net/context
* [Medeina](https://github.com/imdario/medeina): Inspired by Ruby's Roda and Cuba
* [Neko](https://github.com/rocwong/neko): A lightweight web application framework for Golang
* [Roxanna](https://github.com/iamthemuffinman/Roxanna): An amalgamation of httprouter, better logging, and hot reload
* [siesta](https://github.com/VividCortex/siesta): Composable HTTP handlers with contexts
# go-jmespath - A JMESPath implementation in Go

[![Build Status](https://img.shields.io/travis/jmespath/go-jmespath.svg)](https://travis-ci.org/jmespath/go-jmespath)



See http://jmespath.org for more info.
# AWS SDK for Go

[![API Reference](http://img.shields.io/badge/api-reference-blue.svg)](http://docs.aws.amazon.com/sdk-for-go/api)
[![Join the chat at https://gitter.im/aws/aws-sdk-go](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aws/aws-sdk-go?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://img.shields.io/travis/aws/aws-sdk-go.svg)](https://travis-ci.org/aws/aws-sdk-go)
[![Apache V2 License](http://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/aws/aws-sdk-go/blob/master/LICENSE.txt)

aws-sdk-go is the official AWS SDK for the Go programming language.

Checkout our [release notes](https://github.com/aws/aws-sdk-go/releases) for information about the latest bug fixes, updates, and features added to the SDK.

## Installing

If you are using Go 1.5 with the `GO15VENDOREXPERIMENT=1` vendoring flag, or 1.6 and higher you can use the following command to retrieve the SDK. The SDK's non-testing dependencies will be included and are vendored in the `vendor` folder.

    go get -u github.com/aws/aws-sdk-go

Otherwise if your Go environment does not have vendoring support enabled, or you do not want to include the vendored SDK's dependencies you can use the following command to retrieve the SDK and its non-testing dependencies using `go get`.

    go get -u github.com/aws/aws-sdk-go/aws/...
    go get -u github.com/aws/aws-sdk-go/service/...

If you're looking to retrieve just the SDK without any dependencies use the following command.

    go get -d github.com/aws/aws-sdk-go/

These two processes will still include the `vendor` folder and it should be deleted if its not going to be used by your environment.

    rm -rf $GOPATH/src/github.com/aws/aws-sdk-go/vendor

## Getting Help

Please use these community resources for getting help. We use the GitHub issues for tracking bugs and feature requests.
* Ask a question on [StackOverflow](http://stackoverflow.com/) and tag it with the [`aws-sdk-go`](http://stackoverflow.com/questions/tagged/aws-sdk-go) tag.
* Come join the AWS SDK for Go community chat on [gitter](https://gitter.im/aws/aws-sdk-go).
* Open a support ticket with [AWS Support](http://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
* If you think you may of found a bug, please open an [issue](https://github.com/aws/aws-sdk-go/issues/new).

## Opening Issues

If you encounter a bug with the AWS SDK for Go we would like to hear about it. Search the [existing issues]( https://github.com/aws/aws-sdk-go/issues) and see if others are also experiencing the issue before opening a new issue. Please include the version of AWS SDK for Go, Go language, and OS you’re using. Please also include repro case when appropriate.

The GitHub issues are intended for bug reports and feature requests. For help and questions with using AWS SDK for GO please make use of the resources listed in the [Getting Help]( https://github.com/aws/aws-sdk-go#getting-help) section. Keeping the list of open issues lean will help us respond in a timely manner.

## Reference Documentation

[`Getting Started Guide`](https://aws.amazon.com/sdk-for-go/) - This document is a general introduction how to configure and make requests with the SDK. If this is your first time using the SDK, this documentation and the API documentation will help you get started. This document focuses on the syntax and behavior of the SDK. The [Service Developer Guide](https://aws.amazon.com/documentation/) will help you get started using specific AWS services.

[`SDK API Reference Documentation`](https://docs.aws.amazon.com/sdk-for-go/api/) - Use this document to look up all API operation input and output parameters for AWS services supported by the SDK. The API reference also includes documentation of the SDK, and examples how to using the SDK, service client API operations, and API operation require parameters.

[`Service Developer Guide`](https://aws.amazon.com/documentation/) - Use this documentation to learn how to interface with an AWS service. These are great guides both, if you're getting started with a service, or looking for more information on a service. You should not need this document for coding, though in some cases, services may supply helpful samples that you might want to look out for.

[`SDK Examples`](https://github.com/aws/aws-sdk-go/tree/master/example) - Included in the SDK's repo are a several hand crafted examples using the SDK features and AWS services.

## Configuring Credentials

Before using the SDK, ensure that you've configured credentials. The best
way to configure credentials on a development machine is to use the
`~/.aws/credentials` file, which might look like:

```
[default]
aws_access_key_id = AKID1234567890
aws_secret_access_key = MY-SECRET-KEY
```

You can learn more about the credentials file from this
[blog post](http://blogs.aws.amazon.com/security/post/Tx3D6U6WSFGOK2H/A-New-and-Standardized-Way-to-Manage-Credentials-in-the-AWS-SDKs).

Alternatively, you can set the following environment variables:

```
AWS_ACCESS_KEY_ID=AKID1234567890
AWS_SECRET_ACCESS_KEY=MY-SECRET-KEY
```

### AWS shared config file (`~/.aws/config`)
The AWS SDK for Go added support the shared config file in release [v1.3.0](https://github.com/aws/aws-sdk-go/releases/tag/v1.3.0). You can opt into enabling support for the shared config by setting the environment variable `AWS_SDK_LOAD_CONFIG` to a truthy value. See the [Session](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sessions.html) docs for more information about this feature.

## Using the Go SDK

To use a service in the SDK, create a service variable by calling the `New()`
function. Once you have a service client, you can call API operations which each
return response data and a possible error.

To list a set of instance IDs from EC2, you could run:

```go
package main

import (
	"fmt"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/ec2"
)

func main() {
	sess, err := session.NewSession()
	if err != nil {
		panic(err)
	}

	// Create an EC2 service object in the "us-west-2" region
	// Note that you can also configure your region globally by
	// exporting the AWS_REGION environment variable
	svc := ec2.New(sess, &aws.Config{Region: aws.String("us-west-2")})

	// Call the DescribeInstances Operation
	resp, err := svc.DescribeInstances(nil)
	if err != nil {
		panic(err)
	}

	// resp has all of the response data, pull out instance IDs:
	fmt.Println("> Number of reservation sets: ", len(resp.Reservations))
	for idx, res := range resp.Reservations {
		fmt.Println("  > Number of instances: ", len(res.Instances))
		for _, inst := range resp.Reservations[idx].Instances {
			fmt.Println("    - Instance ID: ", *inst.InstanceId)
		}
	}
}
```

You can find more information and operations in our
[API documentation](http://docs.aws.amazon.com/sdk-for-go/api/).

## License

This SDK is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0),
see LICENSE.txt and NOTICE.txt for more information.
# Example

This example shows how the CloudFront CookieSigner can be used to generate signed cookies to provided short term access to restricted resourced fronted by CloudFront.

# Usage
Makes a request for object using CloudFront cookie signing, and outputs the contents of the object to stdout.

```sh
go run -tags example signCookies.go -file <privkey file>  -id <keyId> -r <resource pattern> -g <object to get>
```


# Example

`scanItems` is an example how to use Amazon DynamoDB's Scan API operation with the SDK's `dynamodbattributes.UnmarshalListOfMaps` to unmarshal the Scan response's `Items` `[]map[string]*dynamodb.AttributeValue` field. This unmarshaler can be used with all `[]map[string]*dynamodb.AttributeValue` type fields.

## Go Type

The `Item` time will be used by the example to unmarshal the DynamoDB table's items to.

```go
type Item struct {
	Key  int
	Desc string
	Data map[string]interface{}
}
```

In DynamoDB the structure of the item to be returned will be:
```json
{
  "Data": {
    "Value 1": "abc",
    "Value 2": 1234567890
  },
  "Desc": "First ddb item",
  "Key": 1
}
```

## Usage

`scanItems.go -table "<table_name>" -region "<optional_region>"`

## Output

```
0: Key: 123, Desc: An item in the DynamoDB table 
	Num Data Values: 0
1: Key: 2, Desc: Second ddb item
	Num Data Values: 2
	- "A Field": 123
	- "Another Field": abc
2: Key: 1, Desc: First ddb item
	Num Data Values: 2
	- "Value 1": abc
	- "Value 2": 1234567890
```
# Example
You can instantiate `*dynamodb.DynamoDB` and pass that as a parameter to all
methods connecting to DynamoDB, or as `unitTest` demonstrates, create your own
`type` and pass it along as a field.

## Test-compatible DynamoDB field
If you use `*dynamodb.DynamoDB` as a field, you will be unable to unit test it,
as documented in #88. Cast it instead as `dynamodbiface.DynamoDBAPI`:
```go
type ItemGetter struct {
		DynamoDB dynamodbiface.DynamoDBAPI
}
```

## Querying actual DynamoDB
You'll need an `*aws.Config` and `*session.Session` for these to work correctly:
```go
// Setup
var getter = new(ItemGetter)
var config *aws.Config = &aws.Config{Region: aws.String("us-west-2"),}
var sess *session.Session = session.NewSession(config)
var svc *dynamodb.DynamoDB = dynamodb.New()
getter.DynamoDB = dynamodbiface.DynamoDBAPI(svc)
// Finally
getter.DynamoDB.GetItem(/* ... */)
```

## Querying in tests
Construct a `fakeDynamoDB` and add the necessary methods for each of those
structs (custom ones for `ItemGetter` and [whatever methods you're using for
DynamoDB](https://github.com/aws/aws-sdk-go/blob/master/service/dynamodb/dynamodbiface/interface.go)),
and you're good to go!
```go
type fakeDynamoDB struct {
		dynamodbiface.DynamoDBAPI
}
var getter = new(ItemGetter)
getter.DynamoDB = &fakeDynamoDB{}
// And to run it (assuming you've mocked fakeDynamoDB.GetItem)
getter.DynamoDB.GetItem(/* ... */)
```

## Output
```
$ go test -cover
PASS
coverage: 100.0% of statements
ok		_/Users/shatil/workspace/aws-sdk-go/example/service/dynamodb/unitTest	0.008s
```
# Example

filter_ec2_by_tag is an example using the AWS SDK for Go to list ec2 instaces that match provided tag name filter.


# Usage

The example uses the the bucket name provided, and lists all object keys in a bucket.

```sh
go run -tags example filter_ec2_by_tag.go <name_filter>
```

Output:
```
listing instances with tag vpn in: us-east-1
[{
  Instances: [{
      AmiLaunchIndex: 0,
      Architecture: "x86_64",
      BlockDeviceMappings: [{
          DeviceName: "/dev/xvda",
          Ebs: {
            AttachTime: 2016-07-06 18:04:53 +0000 UTC,
            DeleteOnTermination: true,
            Status: "attached",
            VolumeId: "vol-xxxx"
          }
        }],
      ...
```
# Example

listObjects is an example using the AWS SDK for Go to list objects' key in a S3 bucket.


# Usage

The example uses the the bucket name provided, and lists all object keys in a bucket.

```sh
go run -tags example listObjects.go <bucket>
```

Output:
```
Page, 0
Object: myKey
Object: mykey.txt
Object: resources/0001/item-01
Object: resources/0001/item-02
Object: resources/0001/item-03
Object: resources/0002/item-01
Object: resources/0002/item-02
Object: resources/0002/item-03
Object: resources/0002/item-04
Object: resources/0002/item-05
```
# Example

concatObjects is an example using the AWS SDK for Go to concatenate two objects together.
We use `UploadPartCopy` which uses an object for a part. Here in this example we have two parts, or in other words
two objects that we want to concatenate together.


# Usage

The example uses the the bucket name provided, two keys for each object, and lastly the output key.

```sh
AWS_REGION=<region> go run -tags example concatenateObjects.go <bucket> <key for object 1> <key for object 2> <key for output>
```
## Example

listObjectsConcurrentlv is an example using the AWS SDK for Go concurrently to list the encrypted objects in the S3 buckets owned by an account.

## Usage

The example's `accounts` string slice contains a list of the SharedCredentials profiles which will be used to look up the buckets owned by each profile. Each bucket's objects will be queried.

```
AWS_REGION=us-east-1 go run -tags example listObjectsConcurrentlv.go
```


# Example

putObjectAcl is an example using the AWS SDK for Go to put an ACL on an S3 object.

# Usage

```sh
putBucketAcl <params>
	-region <region> // required
	-bucket <bucket> // required
	-key <key> // required
	-owner-name <owner-name>
	-owner-id <owner-id>
	-grantee-type <some type> // required
	-uri <uri to group>
	-email <email address>
	-user-id <user-id>
	-display-name <display name>
```

```sh
go run -tags example putObjectAcl.go 
	-bucket <bucket> 
	-key <key> 
	-owner-name <name> 
	-owner-id <id>
	-grantee-type <some type>
	-user-id <user-id>
```

Depending on the type is used depends on which of the three, `uri`, `email`, or `user-id`, needs to be used.
* `s3.TypeCanonicalUser`: `user-id` or `display-name` must be used
* `s3.TypeAmazonCustomerByEmail`: `email` must be used
* `s3.TypeGroup`: `uri` must be used

Output:
```
success {
} nil
```
# Example

This example shows how the SDK's API interfaces can be used by your code intead of the concrete service client type directly. Using this pattern allows you to mock out your code's usage of the SDK's service client for testing.

# Usage

Use the `go test` tool to verify the `Queue` type's `GetMessages` function correctly unmarshals the SQS message responses.

`go test ./`
# Example

Uploads a file to S3 given a bucket and object key. Also takes a duration
value to terminate the update if it doesn't complete within that time.

The AWS Region needs to be provided in the AWS shared config or on the
environment variable as `AWS_REGION`. Credentials also must be provided
Will default to shared config file, but can load from environment if provided.

## Usage:

    # Upload myfile.txt to myBucket/myKey. Must complete within 10 minutes or will fail
    go run withContext.go -b mybucket -k myKey -d 10m < myfile.txt
# Handling Specific Service Error Codes

This examples highlights how you can use the `awserr.Error` type to perform logic based on specific error codes returned by service API operations.

In this example the `S3` `GetObject` API operation is used to request the contents of a object in S3. The example handles the `NoSuchBucket` and `NoSuchKey` error codes printing custom messages to stderr. If Any other error is received a generic message is printed.

## Usage

Will make a request to S3 for the contents of an object. If the request was successful, and the object was found the object's path and size will be printed to stdout.

If the object's bucket or key does not exist a specific error message will be printed to stderr for the error.

Any other error will be printed as an unknown error.

```sh
go run -tags example handleServiceErrorCodes.go mybucket mykey
```
Enumerate Regions and Endpoints Example
===

Demostrates how the SDK's endpoints can be enumerated over to discover regions, services, and endpoints defined by the SDK's Regions and Endpoints metadata.

Usage
---

The following parameters can be used to enumerate the SDK's partition metadata.

Example:

    go run enumEndpoints.go -p aws -services -r us-west-2

Output:

    Services with endpoint us-west-2 in aws:
	ec2
	dynamodb
	s3
    ...

CLI parameters
---

```
    -p=id partition id, e.g: aws
    -r=id region id, e.g: us-west-2
    -s=id service id, e.g: s3
    
    -partitions Lists all partitions.
    -regions Lists all regions in a partition. Requires partition ID.
             If service ID is also provided will show endpoints for a service.
    -services Lists all services in a partition. Requires partition ID.
              If region ID is also provided, will show services available in that region.
```

Custom Endpoint Example
===

This example provides examples on how you can provide custom endpoints, and logic to how endpoints are resolved by the SDK.

The example creates multiple clients with different endpoint configuraiton. From a custom endpoint resolver that wraps the defeault resolver so that any S3 service client created uses the custom endpoint, to how you can provide your own logic to a single service's endpoint resolving.
## AWS SDK for Go Private packages ##
`private` is a collection of packages used internally by the SDK, and is subject to have breaking changes. This package is not `internal` so that if you really need to use its functionality, and understand breaking changes will be made, you are able to.

These packages will be refactored in the future so that the API generator and model parsers are exposed cleanly on their own. Making it easier for you to generate your own code based on the API models.
INI [![Build Status](https://travis-ci.org/go-ini/ini.svg?branch=master)](https://travis-ci.org/go-ini/ini) [![Sourcegraph](https://sourcegraph.com/github.com/go-ini/ini/-/badge.svg)](https://sourcegraph.com/github.com/go-ini/ini?badge)
===

![](https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

[简体中文](README_ZH.md)

## Feature

- Load multiple data sources(`[]byte`, file and `io.ReadCloser`) with overwrites.
- Read with recursion values.
- Read with parent-child sections.
- Read with auto-increment key names.
- Read with multiple-line values.
- Read with tons of helper methods.
- Read and convert values to Go types.
- Read and **WRITE** comments of sections and keys.
- Manipulate sections, keys and comments with ease.
- Keep sections and keys in order as you parse and save.

## Installation

To use a tagged revision:

	go get gopkg.in/ini.v1

To use with latest changes:

	go get github.com/go-ini/ini

Please add `-u` flag to update in the future.

### Testing

If you want to test on your machine, please apply `-t` flag:

	go get -t gopkg.in/ini.v1

Please add `-u` flag to update in the future.

## Getting Started

### Loading from data sources

A **Data Source** is either raw data in type `[]byte`, a file name with type `string` or `io.ReadCloser`. You can load **as many data sources as you want**. Passing other types will simply return an error.

```go
cfg, err := ini.Load([]byte("raw data"), "filename", ioutil.NopCloser(bytes.NewReader([]byte("some other data"))))
```

Or start with an empty object:

```go
cfg := ini.Empty()
```

When you cannot decide how many data sources to load at the beginning, you will still be able to **Append()** them later.

```go
err := cfg.Append("other file", []byte("other raw data"))
```

If you have a list of files with possibilities that some of them may not available at the time, and you don't know exactly which ones, you can use `LooseLoad` to ignore nonexistent files without returning error.

```go
cfg, err := ini.LooseLoad("filename", "filename_404")
```

The cool thing is, whenever the file is available to load while you're calling `Reload` method, it will be counted as usual.

#### Ignore cases of key name

When you do not care about cases of section and key names, you can use `InsensitiveLoad` to force all names to be lowercased while parsing.

```go
cfg, err := ini.InsensitiveLoad("filename")
//...

// sec1 and sec2 are the exactly same section object
sec1, err := cfg.GetSection("Section")
sec2, err := cfg.GetSection("SecTIOn")

// key1 and key2 are the exactly same key object
key1, err := cfg.GetKey("Key")
key2, err := cfg.GetKey("KeY")
```

#### MySQL-like boolean key 

MySQL's configuration allows a key without value as follows:

```ini
[mysqld]
...
skip-host-cache
skip-name-resolve
```

By default, this is considered as missing value. But if you know you're going to deal with those cases, you can assign advanced load options:

```go
cfg, err := LoadSources(LoadOptions{AllowBooleanKeys: true}, "my.cnf"))
```

The value of those keys are always `true`, and when you save to a file, it will keep in the same foramt as you read.

To generate such keys in your program, you could use `NewBooleanKey`:

```go
key, err := sec.NewBooleanKey("skip-host-cache")
```

#### Comment

Take care that following format will be treated as comment:

1. Line begins with `#` or `;`
2. Words after `#` or `;`
3. Words after section name (i.e words after `[some section name]`)

If you want to save a value with `#` or `;`, please quote them with ``` ` ``` or ``` """ ```.

### Working with sections

To get a section, you would need to:

```go
section, err := cfg.GetSection("section name")
```

For a shortcut for default section, just give an empty string as name:

```go
section, err := cfg.GetSection("")
```

When you're pretty sure the section exists, following code could make your life easier:

```go
section := cfg.Section("section name")
```

What happens when the section somehow does not exist? Don't panic, it automatically creates and returns a new section to you.

To create a new section:

```go
err := cfg.NewSection("new section")
```

To get a list of sections or section names:

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### Working with keys

To get a key under a section:

```go
key, err := cfg.Section("").GetKey("key name")
```

Same rule applies to key operations:

```go
key := cfg.Section("").Key("key name")
```

To check if a key exists:

```go
yes := cfg.Section("").HasKey("key name")
```

To create a new key:

```go
err := cfg.Section("").NewKey("name", "value")
```

To get a list of keys or key names:

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

To get a clone hash of keys and corresponding values:

```go
hash := cfg.Section("").KeysHash()
```

### Working with values

To get a string value:

```go
val := cfg.Section("").Key("key name").String()
```

To validate key value on the fly:

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

If you do not want any auto-transformation (such as recursive read) for the values, you can get raw value directly (this way you get much better performance):

```go
val := cfg.Section("").Key("key name").Value()
```

To check if raw value exists:

```go
yes := cfg.Section("").HasValue("test value")
```

To get value with types:

```go
// For boolean values:
// true when value is: 1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false when value is: 0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// Methods start with Must also accept one argument for default value
// when key not found or fail to parse value to given type.
// Except method MustString, which you have to pass a default value.

v = cfg.Section("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

What if my value is three-line long?

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

Not a problem!

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

That's cool, how about continuation lines?

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

Piece of cake!

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

Well, I hate continuation lines, how do I disable that?

```go
cfg, err := ini.LoadSources(ini.LoadOptions{
	IgnoreContinuation: true,
}, "filename")
```

Holy crap! 

Note that single quotes around values will be stripped:

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

That's all? Hmm, no.

#### Helper methods of working with values

To get value with given candidates:

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

Default value will be presented if value of key is not in candidates you given, and default value does not need be one of candidates.

To validate value in a given range:

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

##### Auto-split values into a slice

To use zero value of type for invalid inputs:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [0.0 2.2 0.0 0.0]
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

To exclude invalid values out of result slice:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [2.2]
vals = cfg.Section("").Key("FLOAT64S").ValidFloat64s(",")
vals = cfg.Section("").Key("INTS").ValidInts(",")
vals = cfg.Section("").Key("INT64S").ValidInt64s(",")
vals = cfg.Section("").Key("UINTS").ValidUints(",")
vals = cfg.Section("").Key("UINT64S").ValidUint64s(",")
vals = cfg.Section("").Key("TIMES").ValidTimes(",")
```

Or to return nothing but error when have invalid inputs:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> error
vals = cfg.Section("").Key("FLOAT64S").StrictFloat64s(",")
vals = cfg.Section("").Key("INTS").StrictInts(",")
vals = cfg.Section("").Key("INT64S").StrictInt64s(",")
vals = cfg.Section("").Key("UINTS").StrictUints(",")
vals = cfg.Section("").Key("UINT64S").StrictUint64s(",")
vals = cfg.Section("").Key("TIMES").StrictTimes(",")
```

### Save your configuration

Finally, it's time to save your configuration to somewhere.

A typical way to save configuration is writing it to a file:

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

Another way to save is writing to a `io.Writer` interface:

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

By default, spaces are used to align "=" sign between key and values, to disable that:

```go
ini.PrettyFormat = false
``` 

## Advanced Usage

### Recursive Values

For all value of keys, there is a special syntax `%(<name>)s`, where `<name>` is the key name in same section or default section, and `%(<name>)s` will be replaced by corresponding value(empty string if key not found). You can use this syntax at most 99 level of recursions.

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### Parent-child Sections

You can use `.` in section name to indicate parent-child relationship between two or more sections. If the key not found in the child section, library will try again on its parent section until there is no parent section.

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### Retrieve parent keys available to a child section

```go
cfg.Section("package.sub").ParentKeys() // ["CLONE_URL"]
```

### Unparseable Sections

Sometimes, you have sections that do not contain key-value pairs but raw content, to handle such case, you can use `LoadOptions.UnparsableSections`:

```go
cfg, err := LoadSources(LoadOptions{UnparseableSections: []string{"COMMENTS"}}, `[COMMENTS]
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>`))

body := cfg.Section("COMMENTS").Body()

/* --- start ---
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>
------  end  --- */
```

### Auto-increment Key Names

If key name is `-` in data source, then it would be seen as special syntax for auto-increment key name start from 1, and every section is independent on counter.

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### Map To Struct

Want more objective way to play with INI? Cool.

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// Things can be simpler.
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// Just map a section? Fine.
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

Can I have default value for field? Absolutely.

Assign it before you map to struct. It will keep the value as it is if the key is not presented or got wrong type.

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

It's really cool, but what's the point if you can't give me my file back from struct?

### Reflect From Struct

Why not?

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string    `ini:"places,omitempty"`
	None   []int       `ini:",omitempty"`
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

So, what do I get?

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
places = HangZhou,Boston
```

#### Name Mapper

To save your time and make your code cleaner, this library supports [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) between struct field and actual section and key name.

There are 2 built-in name mappers:

- `AllCapsUnderscore`: it converts to format `ALL_CAPS_UNDERSCORE` then match section or key.
- `TitleUnderscore`: it converts to format `title_underscore` then match section or key.

To use them:

```go
type Info struct {
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

Same rules of name mapper apply to `ini.ReflectFromWithMapper` function.

#### Value Mapper

To expand values (e.g. from environment variables), you can use the `ValueMapper` to transform values:

```go
type Env struct {
	Foo string `ini:"foo"`
}

func main() {
	cfg, err := ini.Load([]byte("[env]\nfoo = ${MY_VAR}\n")
	cfg.ValueMapper = os.ExpandEnv
	// ...
	env := &Env{}
	err = cfg.Section("env").MapTo(env)
}
```

This would set the value of `env.Foo` to the value of the environment variable `MY_VAR`.

#### Other Notes On Map/Reflect

Any embedded struct is treated as a section by default, and there is no automatic parent-child relations in map/reflect feature:

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

What if, yes, I'm paranoid, I want embedded struct to be in the same section. Well, all roads lead to Rome.

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## Getting Help

- [API Documentation](https://gowalker.org/gopkg.in/ini.v1)
- [File An Issue](https://github.com/go-ini/ini/issues/new)

## FAQs

### What does `BlockMode` field do?

By default, library lets you read and write values so we need a locker to make sure your data is safe. But in cases that you are very sure about only reading data through the library, you can set `cfg.BlockMode = false` to speed up read operations about **50-70%** faster.

### Why another INI library?

Many people are using my another INI library [goconfig](https://github.com/Unknwon/goconfig), so the reason for this one is I would like to make more Go style code. Also when you set `cfg.BlockMode = false`, this one is about **10-30%** faster.

To make those changes I have to confirm API broken, so it's safer to keep it in another place and start using `gopkg.in` to version my package at this time.(PS: shorter import path)

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.
本包提供了 Go 语言中读写 INI 文件的功能。

## 功能特性

- 支持覆盖加载多个数据源（`[]byte`、文件和 `io.ReadCloser`）
- 支持递归读取键值
- 支持读取父子分区
- 支持读取自增键名
- 支持读取多行的键值
- 支持大量辅助方法
- 支持在读取时直接转换为 Go 语言类型
- 支持读取和 **写入** 分区和键的注释
- 轻松操作分区、键值和注释
- 在保存文件时分区和键值会保持原有的顺序

## 下载安装

使用一个特定版本：

    go get gopkg.in/ini.v1

使用最新版：

	go get github.com/go-ini/ini

如需更新请添加 `-u` 选项。

### 测试安装

如果您想要在自己的机器上运行测试，请使用 `-t` 标记：

	go get -t gopkg.in/ini.v1

如需更新请添加 `-u` 选项。

## 开始使用

### 从数据源加载

一个 **数据源** 可以是 `[]byte` 类型的原始数据，`string` 类型的文件路径或 `io.ReadCloser`。您可以加载 **任意多个** 数据源。如果您传递其它类型的数据源，则会直接返回错误。

```go
cfg, err := ini.Load([]byte("raw data"), "filename", ioutil.NopCloser(bytes.NewReader([]byte("some other data"))))
```

或者从一个空白的文件开始：

```go
cfg := ini.Empty()
```

当您在一开始无法决定需要加载哪些数据源时，仍可以使用 **Append()** 在需要的时候加载它们。

```go
err := cfg.Append("other file", []byte("other raw data"))
```

当您想要加载一系列文件，但是不能够确定其中哪些文件是不存在的，可以通过调用函数 `LooseLoad` 来忽略它们（`Load` 会因为文件不存在而返回错误）：

```go
cfg, err := ini.LooseLoad("filename", "filename_404")
```

更牛逼的是，当那些之前不存在的文件在重新调用 `Reload` 方法的时候突然出现了，那么它们会被正常加载。

#### 忽略键名的大小写

有时候分区和键的名称大小写混合非常烦人，这个时候就可以通过 `InsensitiveLoad` 将所有分区和键名在读取里强制转换为小写：

```go
cfg, err := ini.InsensitiveLoad("filename")
//...

// sec1 和 sec2 指向同一个分区对象
sec1, err := cfg.GetSection("Section")
sec2, err := cfg.GetSection("SecTIOn")

// key1 和 key2 指向同一个键对象
key1, err := cfg.GetKey("Key")
key2, err := cfg.GetKey("KeY")
```

#### 类似 MySQL 配置中的布尔值键

MySQL 的配置文件中会出现没有具体值的布尔类型的键：

```ini
[mysqld]
...
skip-host-cache
skip-name-resolve
```

默认情况下这被认为是缺失值而无法完成解析，但可以通过高级的加载选项对它们进行处理：

```go
cfg, err := LoadSources(LoadOptions{AllowBooleanKeys: true}, "my.cnf"))
```

这些键的值永远为 `true`，且在保存到文件时也只会输出键名。

如果您想要通过程序来生成此类键，则可以使用 `NewBooleanKey`：

```go
key, err := sec.NewBooleanKey("skip-host-cache")
```

#### 关于注释

下述几种情况的内容将被视为注释：

1. 所有以 `#` 或 `;` 开头的行
2. 所有在 `#` 或 `;` 之后的内容
3. 分区标签后的文字 (即 `[分区名]` 之后的内容)

如果你希望使用包含 `#` 或 `;` 的值，请使用 ``` ` ``` 或 ``` """ ``` 进行包覆。

### 操作分区（Section）

获取指定分区：

```go
section, err := cfg.GetSection("section name")
```

如果您想要获取默认分区，则可以用空字符串代替分区名：

```go
section, err := cfg.GetSection("")
```

当您非常确定某个分区是存在的，可以使用以下简便方法：

```go
section := cfg.Section("section name")
```

如果不小心判断错了，要获取的分区其实是不存在的，那会发生什么呢？没事的，它会自动创建并返回一个对应的分区对象给您。

创建一个分区：

```go
err := cfg.NewSection("new section")
```

获取所有分区对象或名称：

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### 操作键（Key）

获取某个分区下的键：

```go
key, err := cfg.Section("").GetKey("key name")
```

和分区一样，您也可以直接获取键而忽略错误处理：

```go
key := cfg.Section("").Key("key name")
```

判断某个键是否存在：

```go
yes := cfg.Section("").HasKey("key name")
```

创建一个新的键：

```go
err := cfg.Section("").NewKey("name", "value")
```

获取分区下的所有键或键名：

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

获取分区下的所有键值对的克隆：

```go
hash := cfg.Section("").KeysHash()
```

### 操作键值（Value）

获取一个类型为字符串（string）的值：

```go
val := cfg.Section("").Key("key name").String()
```

获取值的同时通过自定义函数进行处理验证：

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

如果您不需要任何对值的自动转变功能（例如递归读取），可以直接获取原值（这种方式性能最佳）：

```go
val := cfg.Section("").Key("key name").Value()
```

判断某个原值是否存在：

```go
yes := cfg.Section("").HasValue("test value")
```

获取其它类型的值：

```go
// 布尔值的规则：
// true 当值为：1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false 当值为：0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// 由 Must 开头的方法名允许接收一个相同类型的参数来作为默认值，
// 当键不存在或者转换失败时，则会直接返回该默认值。
// 但是，MustString 方法必须传递一个默认值。

v = cfg.Seciont("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

如果我的值有好多行怎么办？

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

嗯哼？小 case！

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

赞爆了！那要是我属于一行的内容写不下想要写到第二行怎么办？

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

简直是小菜一碟！

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

可是我有时候觉得两行连在一起特别没劲，怎么才能不自动连接两行呢？

```go
cfg, err := ini.LoadSources(ini.LoadOptions{
	IgnoreContinuation: true,
}, "filename")
```

哇靠给力啊！

需要注意的是，值两侧的单引号会被自动剔除：

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

这就是全部了？哈哈，当然不是。

#### 操作键值的辅助方法

获取键值时设定候选值：

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

如果获取到的值不是候选值的任意一个，则会返回默认值，而默认值不需要是候选值中的一员。

验证获取的值是否在指定范围内：

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

##### 自动分割键值到切片（slice）

当存在无效输入时，使用零值代替：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [0.0 2.2 0.0 0.0]
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

从结果切片中剔除无效输入：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [2.2]
vals = cfg.Section("").Key("FLOAT64S").ValidFloat64s(",")
vals = cfg.Section("").Key("INTS").ValidInts(",")
vals = cfg.Section("").Key("INT64S").ValidInt64s(",")
vals = cfg.Section("").Key("UINTS").ValidUints(",")
vals = cfg.Section("").Key("UINT64S").ValidUint64s(",")
vals = cfg.Section("").Key("TIMES").ValidTimes(",")
```

当存在无效输入时，直接返回错误：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> error
vals = cfg.Section("").Key("FLOAT64S").StrictFloat64s(",")
vals = cfg.Section("").Key("INTS").StrictInts(",")
vals = cfg.Section("").Key("INT64S").StrictInt64s(",")
vals = cfg.Section("").Key("UINTS").StrictUints(",")
vals = cfg.Section("").Key("UINT64S").StrictUint64s(",")
vals = cfg.Section("").Key("TIMES").StrictTimes(",")
```

### 保存配置

终于到了这个时刻，是时候保存一下配置了。

比较原始的做法是输出配置到某个文件：

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

另一个比较高级的做法是写入到任何实现 `io.Writer` 接口的对象中：

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

默认情况下，空格将被用于对齐键值之间的等号以美化输出结果，以下代码可以禁用该功能：

```go
ini.PrettyFormat = false
``` 

## 高级用法

### 递归读取键值

在获取所有键值的过程中，特殊语法 `%(<name>)s` 会被应用，其中 `<name>` 可以是相同分区或者默认分区下的键名。字符串 `%(<name>)s` 会被相应的键值所替代，如果指定的键不存在，则会用空字符串替代。您可以最多使用 99 层的递归嵌套。

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### 读取父子分区

您可以在分区名称中使用 `.` 来表示两个或多个分区之间的父子关系。如果某个键在子分区中不存在，则会去它的父分区中再次寻找，直到没有父分区为止。

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### 获取上级父分区下的所有键名

```go
cfg.Section("package.sub").ParentKeys() // ["CLONE_URL"]
```

### 无法解析的分区

如果遇到一些比较特殊的分区，它们不包含常见的键值对，而是没有固定格式的纯文本，则可以使用 `LoadOptions.UnparsableSections` 进行处理：

```go
cfg, err := LoadSources(LoadOptions{UnparseableSections: []string{"COMMENTS"}}, `[COMMENTS]
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>`))

body := cfg.Section("COMMENTS").Body()

/* --- start ---
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>
------  end  --- */
```

### 读取自增键名

如果数据源中的键名为 `-`，则认为该键使用了自增键名的特殊语法。计数器从 1 开始，并且分区之间是相互独立的。

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### 映射到结构

想要使用更加面向对象的方式玩转 INI 吗？好主意。

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// 一切竟可以如此的简单。
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// 嗯哼？只需要映射一个分区吗？
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

结构的字段怎么设置默认值呢？很简单，只要在映射之前对指定字段进行赋值就可以了。如果键未找到或者类型错误，该值不会发生改变。

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

这样玩 INI 真的好酷啊！然而，如果不能还给我原来的配置文件，有什么卵用？

### 从结构反射

可是，我有说不能吗？

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string    `ini:"places,omitempty"`
	None   []int       `ini:",omitempty"`
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

瞧瞧，奇迹发生了。

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
places = HangZhou,Boston
```

#### 名称映射器（Name Mapper）

为了节省您的时间并简化代码，本库支持类型为 [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) 的名称映射器，该映射器负责结构字段名与分区名和键名之间的映射。

目前有 2 款内置的映射器：

- `AllCapsUnderscore`：该映射器将字段名转换至格式 `ALL_CAPS_UNDERSCORE` 后再去匹配分区名和键名。
- `TitleUnderscore`：该映射器将字段名转换至格式 `title_underscore` 后再去匹配分区名和键名。

使用方法：

```go
type Info struct{
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

使用函数 `ini.ReflectFromWithMapper` 时也可应用相同的规则。

#### 值映射器（Value Mapper）

值映射器允许使用一个自定义函数自动展开值的具体内容，例如：运行时获取环境变量：

```go
type Env struct {
	Foo string `ini:"foo"`
}

func main() {
	cfg, err := ini.Load([]byte("[env]\nfoo = ${MY_VAR}\n")
	cfg.ValueMapper = os.ExpandEnv
	// ...
	env := &Env{}
	err = cfg.Section("env").MapTo(env)
}
```

本例中，`env.Foo` 将会是运行时所获取到环境变量 `MY_VAR` 的值。

#### 映射/反射的其它说明

任何嵌入的结构都会被默认认作一个不同的分区，并且不会自动产生所谓的父子分区关联：

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

很好，但是，我就是要嵌入结构也在同一个分区。好吧，你爹是李刚！

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## 获取帮助

- [API 文档](https://gowalker.org/gopkg.in/ini.v1)
- [创建工单](https://github.com/go-ini/ini/issues/new)

## 常见问题

### 字段 `BlockMode` 是什么？

默认情况下，本库会在您进行读写操作时采用锁机制来确保数据时间。但在某些情况下，您非常确定只进行读操作。此时，您可以通过设置 `cfg.BlockMode = false` 来将读操作提升大约 **50-70%** 的性能。

### 为什么要写另一个 INI 解析库？

许多人都在使用我的 [goconfig](https://github.com/Unknwon/goconfig) 来完成对 INI 文件的操作，但我希望使用更加 Go 风格的代码。并且当您设置 `cfg.BlockMode = false` 时，会有大约 **10-30%** 的性能提升。

为了做出这些改变，我必须对 API 进行破坏，所以新开一个仓库是最安全的做法。除此之外，本库直接使用 `gopkg.in` 来进行版本化发布。（其实真相是导入路径更短了）
Go UUID implementation
========================

[![Build Status](https://travis-ci.org/twinj/uuid.png?branch=master)](https://travis-ci.org/twinj/uuid)
[![GoDoc](http://godoc.org/github.com/twinj/uuid?status.png)](http://godoc.org/github.com/twinj/uuid)

This package provides RFC 4122 compliant UUIDs.
It will generate the following:

* Version 1: based on timestamp and MAC address
* Version 3: based on MD5 hash
* Version 4: based on cryptographically secure random numbers
* Version 5: based on SHA-1 hash

Functions NewV1, NewV3, NewV4, NewV5, New, NewHex and Parse() for generating versions 3, 4
and 5 UUIDs are as specified in [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt).

# Requirements

Go 1.4, 1.3, 1.2 and tip supported.

# Recent Changes

* Removed use of OS Thread locking and runtime package requirement
* Changed String() output to CleanHyphen to match the canonical standard
* Plenty of minor change and housekeeping
* Removed default saver and replaced with interface
* API changes to simplify use.
* Added formatting support for user defined formats
* Added support for Google App Engine
* Variant type bits are now set correctly
* Variant type can now be retrieved more efficiently
* New tests for variant setting to confirm correctness
* New tests added to confirm proper version setting
* Type UUID change to UUIDArray for V3-5 UUIDs and UUIDStruct added for V1 UUIDs
** These implement the BinaryMarshaller and BinaryUnmarshaller interfaces
* New was added to create a base UUID from a []byte slice - this uses UUIDArray
* ParseHex was renamed to ParseUUID
* NewHex now performs unsafe creation of UUID from a hex string
* NewV3 and NewV5 now take anything that implements the Stringer interface
* V1 UUIDs can now be created
* The printing format can be changed

## Installation

Use the `go` tool:

	$ go get github.com/twinj/uuid

## Usage

See [documentation and examples](http://godoc.org/github.com/twinj/uuid)
for more information.

	var config = uuid.StateSaverConfig{SaveReport: true, SaveSchedule: 30 * time.Minute}
	uuid.SetupFileSystemStateSaver(config)

	u1 := uuid.NewV1()
	uP, _ := uuid.Parse("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
	u3 := uuid.NewV3(uP, uuid.Name("test"))
	u4 := uuid.NewV4()
	fmt.Printf(print, u4.Version(), u4.Variant(), u4)

	u5 := uuid.NewV5(uuid.NamespaceURL, uuid.Name("test"))

	if uuid.Equal(u1, u3) {
		fmt.Printf("Will never happen")
	}
	fmt.Printf(uuid.Formatter(u5, uuid.CurlyHyphen))

	uuid.SwitchFormat(uuid.BracketHyphen)

## Copyright

This is a derivative work

Orginal version from
Copyright (C) 2011 by Krzysztof Kowalik <chris@nu7hat.ch>.
See [COPYING](https://github.com/nu7hatch/gouuid/tree/master/COPYING)
file for details.

Also see: Algorithm details in [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt).

Copyright (C) 2014 twinj@github.com
See [LICENSE](https://github.com/twinj/uuid/tree/master/LICENSE)
file for details.
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

https://github.com/reverb/swagger-spec/blob/master/schemas/v2.0# Swag [![Build Status](https://travis-ci.org/go-openapi/swag.svg?branch=master)](https://travis-ci.org/go-openapi/swag) [![codecov](https://codecov.io/gh/go-openapi/swag/branch/master/graph/badge.svg)](https://codecov.io/gh/go-openapi/swag) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

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
This project was automatically exported from code.google.com/p/go-uuid

# uuid ![build status](https://travis-ci.org/pborman/uuid.svg?branch=master)
The uuid package generates and inspects UUIDs based on [RFC 412](http://tools.ietf.org/html/rfc4122) and DCE 1.1: Authentication and Security Services. 

###### Install
`go get github.com/pborman/uuid`

###### Documentation 
[![GoDoc](https://godoc.org/github.com/pborman/uuid?status.svg)](http://godoc.org/github.com/pborman/uuid)

Full `go doc` style documentation for the package can be viewed online without installing this package by using the GoDoc site here: 
http://godoc.org/github.com/pborman/uuid
# Google Cloud for Go

[![Build Status](https://travis-ci.org/GoogleCloudPlatform/google-cloud-go.svg?branch=master)](https://travis-ci.org/GoogleCloudPlatform/google-cloud-go)
[![GoDoc](https://godoc.org/cloud.google.com/go?status.svg)](https://godoc.org/cloud.google.com/go)

``` go
import "cloud.google.com/go"
```

Go packages for Google Cloud Platform services.

To install the packages on your system,

```
$ go get -u cloud.google.com/go/...
```

**NOTE:** These packages are under development, and may occasionally make
backwards-incompatible changes.

**NOTE:** Github repo is a mirror of [https://code.googlesource.com/gocloud](https://code.googlesource.com/gocloud).

  * [News](#news)
  * [Supported APIs](#supported-apis)
  * [Go Versions Supported](#go-versions-supported)
  * [Authorization](#authorization)
  * [Cloud Datastore](#cloud-datastore-)
  * [Cloud Storage](#cloud-storage-)
  * [Cloud Pub/Sub](#cloud-pub-sub-)
  * [Cloud BigQuery](#cloud-bigquery-)
  * [Stackdriver Logging](#stackdriver-logging-)
  * [Cloud Spanner](#cloud-spanner-)


## News

_February 14, 2017_

Release of a client library for Spanner. See
the
[blog post](https://cloudplatform.googleblog.com/2017/02/introducing-Cloud-Spanner-a-global-database-service-for-mission-critical-applications.html). 

Note that although the Spanner service is beta, the Go client library is alpha.

_December 12, 2016_

Beta release of BigQuery, DataStore, Logging and Storage. See the
[blog post](https://cloudplatform.googleblog.com/2016/12/announcing-new-google-cloud-client.html).

Also, BigQuery now supports structs. Read a row directly into a struct with
`RowIterator.Next`, and upload a row directly from a struct with `Uploader.Put`.
You can also use field tags. See the [package documentation][cloud-bigquery-ref]
for details.

_December 5, 2016_

More changes to BigQuery:

* The `ValueList` type was removed. It is no longer necessary. Instead of
   ```go
   var v ValueList
   ... it.Next(&v) ..
   ```
   use

   ```go
   var v []Value
   ... it.Next(&v) ...
   ```

* Previously, repeatedly calling `RowIterator.Next` on the same `[]Value` or
  `ValueList` would append to the slice. Now each call resets the size to zero first.

* Schema inference will infer the SQL type BYTES for a struct field of
  type []byte. Previously it inferred STRING.

* The types `uint`, `uint64` and `uintptr` are no longer supported in schema
  inference. BigQuery's integer type is INT64, and those types may hold values
  that are not correctly represented in a 64-bit signed integer.

* The SQL types DATE, TIME and DATETIME are now supported. They correspond to
  the `Date`, `Time` and `DateTime` types in the new `cloud.google.com/go/civil`
  package.

_November 17, 2016_

Change to BigQuery: values from INTEGER columns will now be returned as int64,
not int. This will avoid errors arising from large values on 32-bit systems.

_November 8, 2016_

New datastore feature: datastore now encodes your nested Go structs as Entity values,
instead of a flattened list of the embedded struct's fields.
This means that you may now have twice-nested slices, eg.
```go
type State struct {
  Cities  []struct{
    Populations []int
  }
}
```

See [the announcement](https://groups.google.com/forum/#!topic/google-api-go-announce/79jtrdeuJAg) for
more details.

_November 8, 2016_

Breaking changes to datastore: contexts no longer hold namespaces; instead you
must set a key's namespace explicitly. Also, key functions have been changed
and renamed.

* The WithNamespace function has been removed. To specify a namespace in a Query, use the Query.Namespace method:
  ```go
  q := datastore.NewQuery("Kind").Namespace("ns")
  ```

* All the fields of Key are exported. That means you can construct any Key with a struct literal:
  ```go
  k := &Key{Kind: "Kind",  ID: 37, Namespace: "ns"}
  ```

* As a result of the above, the Key methods Kind, ID, d.Name, Parent, SetParent and Namespace have been removed.

* `NewIncompleteKey` has been removed, replaced by `IncompleteKey`. Replace
  ```go
  NewIncompleteKey(ctx, kind, parent)
  ```
  with
  ```go
  IncompleteKey(kind, parent)
  ```
  and if you do use namespaces, make sure you set the namespace on the returned key.

* `NewKey` has been removed, replaced by `NameKey` and `IDKey`. Replace
  ```go
  NewKey(ctx, kind, name, 0, parent)
  NewKey(ctx, kind, "", id, parent)
  ```
  with
  ```go
  NameKey(kind, name, parent)
  IDKey(kind, id, parent)
  ```
  and if you do use namespaces, make sure you set the namespace on the returned key.

* The `Done` variable has been removed. Replace `datastore.Done` with `iterator.Done`, from the package `google.golang.org/api/iterator`.

* The `Client.Close` method will have a return type of error. It will return the result of closing the underlying gRPC connection.

See [the announcement](https://groups.google.com/forum/#!topic/google-api-go-announce/hqXtM_4Ix-0) for
more details.

_October 27, 2016_

Breaking change to bigquery: `NewGCSReference` is now a function,
not a method on `Client`.

New bigquery feature: `Table.LoaderFrom` now accepts a `ReaderSource`, enabling
loading data into a table from a file or any `io.Reader`.

_October 21, 2016_

Breaking change to pubsub: removed `pubsub.Done`.

Use `iterator.Done` instead, where `iterator` is the package
`google.golang.org/api/iterator`.


[Older news](https://github.com/GoogleCloudPlatform/google-cloud-go/blob/master/old-news.md)

## Supported APIs

Google API                     | Status       | Package
-------------------------------|--------------|-----------------------------------------------------------
[Datastore][cloud-datastore]   | beta         | [`cloud.google.com/go/datastore`][cloud-datastore-ref]
[Storage][cloud-storage]       | beta         | [`cloud.google.com/go/storage`][cloud-storage-ref]
[Bigtable][cloud-bigtable]     | beta         | [`cloud.google.com/go/bigtable`][cloud-bigtable-ref]
[BigQuery][cloud-bigquery]     | beta         | [`cloud.google.com/go/bigquery`][cloud-bigquery-ref]
[Logging][cloud-logging]       | beta         | [`cloud.google.com/go/logging`][cloud-logging-ref]
[Pub/Sub][cloud-pubsub]        | alpha | [`cloud.google.com/go/pubsub`][cloud-pubsub-ref]
[Vision][cloud-vision]         | beta | [`cloud.google.com/go/vision`][cloud-vision-ref]
[Language][cloud-language]     | alpha | [`cloud.google.com/go/language/apiv1`][cloud-language-ref]
[Speech][cloud-speech]         | alpha | [`cloud.google.com/go/speech/apiv1beta`][cloud-speech-ref]
[Spanner][cloud-spanner]       | alpha | [`cloud.google.com/go/spanner`][cloud-spanner-ref]


> **Alpha status**: the API is still being actively developed. As a
> result, it might change in backward-incompatible ways and is not recommended
> for production use.
>
> **Beta status**: the API is largely complete, but still has outstanding
> features and bugs to be addressed. There may be minor backwards-incompatible
> changes where necessary.
>
> **Stable status**: the API is mature and ready for production use. We will
> continue addressing bugs and feature requests.

Documentation and examples are available at
https://godoc.org/cloud.google.com/go

Visit or join the
[google-api-go-announce group](https://groups.google.com/forum/#!forum/google-api-go-announce)
for updates on these packages.

## Go Versions Supported

We support the two most recent major versions of Go. If Google App Engine uses
an older version, we support that as well. You can see which versions are
currently supported by looking at the lines following `go:` in
[`.travis.yml`](.travis.yml).

## Authorization

By default, each API will use [Google Application Default Credentials][default-creds]
for authorization credentials used in calling the API endpoints. This will allow your
application to run in many environments without requiring explicit configuration.

```go
client, err := storage.NewClient(ctx)
```

To authorize using a
[JSON key file](https://cloud.google.com/iam/docs/managing-service-account-keys),
pass
[`option.WithServiceAccountFile`](https://godoc.org/google.golang.org/api/option#WithServiceAccountFile)
to the `NewClient` function of the desired package. For example:

```go
client, err := storage.NewClient(ctx, option.WithServiceAccountFile("path/to/keyfile.json"))
```

You can exert more control over authorization by using the
[`golang.org/x/oauth2`](https://godoc.org/golang.org/x/oauth2) package to
create an `oauth2.TokenSource`. Then pass
[`option.WithTokenSource`](https://godoc.org/google.golang.org/api/option#WithTokenSource)
to the `NewClient` function:
```go
tokenSource := ...
client, err := storage.NewClient(ctx, option.WithTokenSource(tokenSource))
```

## Cloud Datastore [![GoDoc](https://godoc.org/cloud.google.com/go/datastore?status.svg)](https://godoc.org/cloud.google.com/go/datastore)

- [About Cloud Datastore][cloud-datastore]
- [Activating the API for your project][cloud-datastore-activation]
- [API documentation][cloud-datastore-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/datastore)
- [Complete sample program](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/datastore/tasks)

### Example Usage

First create a `datastore.Client` to use throughout your application:

```go
client, err := datastore.NewClient(ctx, "my-project-id")
if err != nil {
	log.Fatal(err)
}
```

Then use that client to interact with the API:

```go
type Post struct {
	Title       string
	Body        string `datastore:",noindex"`
	PublishedAt time.Time
}
keys := []*datastore.Key{
	datastore.NewKey(ctx, "Post", "post1", 0, nil),
	datastore.NewKey(ctx, "Post", "post2", 0, nil),
}
posts := []*Post{
	{Title: "Post 1", Body: "...", PublishedAt: time.Now()},
	{Title: "Post 2", Body: "...", PublishedAt: time.Now()},
}
if _, err := client.PutMulti(ctx, keys, posts); err != nil {
	log.Fatal(err)
}
```

## Cloud Storage [![GoDoc](https://godoc.org/cloud.google.com/go/storage?status.svg)](https://godoc.org/cloud.google.com/go/storage)

- [About Cloud Storage][cloud-storage]
- [API documentation][cloud-storage-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/storage)
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/storage)

### Example Usage

First create a `storage.Client` to use throughout your application:

```go
client, err := storage.NewClient(ctx)
if err != nil {
	log.Fatal(err)
}
```

```go
// Read the object1 from bucket.
rc, err := client.Bucket("bucket").Object("object1").NewReader(ctx)
if err != nil {
	log.Fatal(err)
}
defer rc.Close()
body, err := ioutil.ReadAll(rc)
if err != nil {
	log.Fatal(err)
}
```

## Cloud Pub/Sub [![GoDoc](https://godoc.org/cloud.google.com/go/pubsub?status.svg)](https://godoc.org/cloud.google.com/go/pubsub)

- [About Cloud Pubsub][cloud-pubsub]
- [API documentation][cloud-pubsub-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/pubsub)
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/pubsub)

### Example Usage

First create a `pubsub.Client` to use throughout your application:

```go
client, err := pubsub.NewClient(ctx, "project-id")
if err != nil {
	log.Fatal(err)
}
```

Then use the client to publish and subscribe:

```go
// Publish "hello world" on topic1.
topic := client.Topic("topic1")
msgIDs, err := topic.Publish(ctx, &pubsub.Message{
	Data: []byte("hello world"),
})
if err != nil {
	log.Fatal(err)
}

// Create an iterator to pull messages via subscription1.
it, err := client.Subscription("subscription1").Pull(ctx)
if err != nil {
	log.Println(err)
}
defer it.Stop()

// Consume N messages from the iterator.
for i := 0; i < N; i++ {
	msg, err := it.Next()
	if err == iterator.Done {
		break
	}
	if err != nil {
		log.Fatalf("Failed to retrieve message: %v", err)
	}

	fmt.Printf("Message %d: %s\n", i, msg.Data)
	msg.Done(true) // Acknowledge that we've consumed the message.
}
```

## Cloud BigQuery [![GoDoc](https://godoc.org/cloud.google.com/go/bigquery?status.svg)](https://godoc.org/cloud.google.com/go/bigquery)

- [About Cloud BigQuery][cloud-bigquery]
- [API documentation][cloud-bigquery-docs]
- [Go client documentation][cloud-bigquery-ref]
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/bigquery)

### Example Usage

First create a `bigquery.Client` to use throughout your application:
```go
c, err := bigquery.NewClient(ctx, "my-project-ID")
if err != nil {
    // TODO: Handle error.
}
```
Then use that client to interact with the API:
```go
// Construct a query.
q := c.Query(`
    SELECT year, SUM(number)
    FROM [bigquery-public-data:usa_names.usa_1910_2013]
    WHERE name = "William"
    GROUP BY year
    ORDER BY year
`)
// Execute the query.
it, err := q.Read(ctx)
if err != nil {
    // TODO: Handle error.
}
// Iterate through the results.
for {
    var values []bigquery.Value
    err := it.Next(&values)
    if err == iterator.Done {
        break
    }
    if err != nil {
        // TODO: Handle error.
    }
    fmt.Println(values)
}
```


## Stackdriver Logging [![GoDoc](https://godoc.org/cloud.google.com/go/logging?status.svg)](https://godoc.org/cloud.google.com/go/logging)

- [About Stackdriver Logging][cloud-logging]
- [API documentation][cloud-logging-docs]
- [Go client documentation][cloud-logging-ref]
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/logging)

### Example Usage

First create a `logging.Client` to use throughout your application:

```go
ctx := context.Background()
client, err := logging.NewClient(ctx, "my-project")
if err != nil {
    // TODO: Handle error.
}
```
Usually, you'll want to add log entries to a buffer to be periodically flushed
(automatically and asynchronously) to the Stackdriver Logging service.
```go
logger := client.Logger("my-log")
logger.Log(logging.Entry{Payload: "something happened!"})
```
Close your client before your program exits, to flush any buffered log entries.
```go
err = client.Close()
if err != nil {
    // TODO: Handle error.
}
```


## Cloud Spanner [![GoDoc](https://godoc.org/cloud.google.com/go/spanner?status.svg)](https://godoc.org/cloud.google.com/go/spanner)

- [About Cloud Spanner][cloud-spanner]
- [API documentation][cloud-spanner-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/spanner)

### Example Usage

First create a `spanner.Client` to use throughout your application:

```go
client, err := spanner.NewClient(ctx, "projects/P/instances/I/databases/D")
if err != nil {
    log.Fatal(err)
}
```

```go
// Simple Reads And Writes
_, err := client.Apply(ctx, []*spanner.Mutation{
    spanner.Insert("Users",
        []string{"name", "email"},
        []interface{}{"alice", "a@example.com"})})
if err != nil {
    log.Fatal(err)
}
row, err := client.Single().ReadRow(ctx, "Users",
    spanner.Key{"alice"}, []string{"email"})
if err != nil {
   log.Fatal(err)
}
```


## Contributing

Contributions are welcome. Please, see the
[CONTRIBUTING](https://github.com/GoogleCloudPlatform/google-cloud-go/blob/master/CONTRIBUTING.md)
document for details. We're using Gerrit for our code reviews. Please don't open pull
requests against this repo, new pull requests will be automatically closed.

Please note that this project is released with a Contributor Code of Conduct.
By participating in this project you agree to abide by its terms.
See [Contributor Code of Conduct](https://github.com/GoogleCloudPlatform/google-cloud-go/blob/master/CONTRIBUTING.md#contributor-code-of-conduct)
for more information.

[cloud-datastore]: https://cloud.google.com/datastore/
[cloud-datastore-ref]: https://godoc.org/cloud.google.com/go/datastore
[cloud-datastore-docs]: https://cloud.google.com/datastore/docs
[cloud-datastore-activation]: https://cloud.google.com/datastore/docs/activate

[cloud-pubsub]: https://cloud.google.com/pubsub/
[cloud-pubsub-ref]: https://godoc.org/cloud.google.com/go/pubsub
[cloud-pubsub-docs]: https://cloud.google.com/pubsub/docs

[cloud-storage]: https://cloud.google.com/storage/
[cloud-storage-ref]: https://godoc.org/cloud.google.com/go/storage
[cloud-storage-docs]: https://cloud.google.com/storage/docs
[cloud-storage-create-bucket]: https://cloud.google.com/storage/docs/cloud-console#_creatingbuckets

[cloud-bigtable]: https://cloud.google.com/bigtable/
[cloud-bigtable-ref]: https://godoc.org/cloud.google.com/go/bigtable

[cloud-bigquery]: https://cloud.google.com/bigquery/
[cloud-bigquery-docs]: https://cloud.google.com/bigquery/docs
[cloud-bigquery-ref]: https://godoc.org/cloud.google.com/go/bigquery

[cloud-logging]: https://cloud.google.com/logging/
[cloud-logging-docs]: https://cloud.google.com/logging/docs
[cloud-logging-ref]: https://godoc.org/cloud.google.com/go/logging

[cloud-vision]: https://cloud.google.com/vision/
[cloud-vision-ref]: https://godoc.org/cloud.google.com/go/vision

[cloud-language]: https://cloud.google.com/natural-language
[cloud-language-ref]: https://godoc.org/cloud.google.com/go/language/apiv1

[cloud-speech]: https://cloud.google.com/speech
[cloud-speech-ref]: https://godoc.org/cloud.google.com/go/speech/apiv1beta1

[cloud-spanner]: https://cloud.google.com/spanner/
[cloud-spanner-ref]: https://godoc.org/cloud.google.com/go/spanner
[cloud-spanner-docs]: https://cloud.google.com/spanner/docs

[default-creds]: https://developers.google.com/identity/protocols/application-default-credentials
Auto-generated pubsub v1 clients
=================================

This package includes auto-generated clients for the pubsub v1 API.

Use the handwritten client (in the parent directory,
cloud.google.com/go/pubsub) in preference to this.

This code is EXPERIMENTAL and subject to CHANGE AT ANY TIME.
# User Counter
# (Cloud Bigtable on Managed VMs using Go)

This app counts how often each user visits. The app uses Cloud Bigtable to store the visit counts for each user.

## Prerequisites

1. Set up Cloud Console.
  1. Go to the [Cloud Console](https://cloud.google.com/console) and create or select your project.
     You will need the project ID later.
  1. Go to **Settings > Project Billing Settings** and enable billing.
  1. Select **APIs & Auth > APIs**.
  1. Enable the **Cloud Bigtable API** and the **Cloud Bigtable Admin API**.
  (You may need to search for the API).
1. Set up gcloud.
  1. `gcloud components update`
  1. `gcloud auth login`
  1. `gcloud config set project PROJECT_ID`
1. Download App Engine SDK for Go.
  1. `go get -u google.golang.org/appengine/...`
1. In main.go, change the `project` and `instance` constants.

## Running locally

1. From the sample project folder, `dev_appserver.py app.yaml`.

## Deploying on Google App Engine flexible environment

Follow the [deployment instructions](https://cloud.google.com/appengine/docs/flexible/go/testing-and-deploying-your-app).
# Cloud Bigtable Hello World in Go

This is a simple application that demonstrates using the [Google Cloud APIs Go
Client Library](https://github.com/GoogleCloudPlatform/google-cloud-go) to connect
to and interact with Cloud Bigtable.

## Prerequisites

1. Set up Cloud Console.
  1. Go to the [Cloud Console](https://cloud.google.com/console) and create or select your project.
     You will need the project ID later.
  1. Go to **Settings > Project Billing Settings** and enable billing.
  1. Select **APIs & Auth > APIs**.
  1. Enable the **Cloud Bigtable API** and the **Cloud Bigtable Admin API**.
  (You may need to search for the API).
1. Set up gcloud.
  1. `gcloud components update`
  1. `gcloud auth login`
  1. `gcloud config set project PROJECT_ID`
1. Provision a Cloud Bigtable instance
  1. Follow the instructions in the [user
documentation](https://cloud.google.com/bigtable/docs/creating-instance) to
create a Google Cloud Platform project and Cloud Bigtable instance if necessary.
  1. You'll need to reference your project id and instance id to run the application.

## Running

1. From the hello_world example folder, `go run main.go -project PROJECT_ID -instance INSTANCE_ID`, substituting your project id and instance id.

## Cleaning up

To avoid incurring extra charges to your Google Cloud Platform account, remove
the resources created for this sample.

1.  Go to the Clusters page in the [Cloud
    Console](https://console.cloud.google.com).

    [Go to the Clusters page](https://console.cloud.google.com/project/_/bigtable/clusters)

1.  Click the cluster name.

1.  Click **Delete**.

    ![Delete](https://cloud.google.com/bigtable/img/delete-quickstart-cluster.png)

1. Type the cluster ID, then click **Delete** to delete the cluster.
translate-nov2016-api.json is a hand-modified version of translate-api.json.
It correctly reflects the API as of 2016-11-15.

Differences:

- Change to base URL
- Addition of OAuth scopes

To generate:



Auto-generated vision v1 clients
=================================

This package includes auto-generated clients for the vision v1 API.

Use the handwritten client (in the parent directory,
cloud.google.com/go/vision) in preference to this.

This code is EXPERIMENTAL and subject to CHANGE AT ANY TIME.
The following files were copied from https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/data:
cat.jpg
face.jpg
faulkner.jpg
mountain.jpg
no-text.jpg

eiffel-tower.jpg is from
https://commons.wikimedia.org/wiki/File:Tour_Eiffel_Wikimedia_Commons_(cropped).jpg.

google.png is from the Google home page:
https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png.




Auto-generated logging v2 clients
=================================

This package includes auto-generated clients for the logging v2 API.

Use the handwritten logging client (in the parent directory,
cloud.google.com/go/logging) in preference to this.

This code is EXPERIMENTAL and subject to CHANGE AT ANY TIME.


#gRPC-Go

[![Build Status](https://travis-ci.org/grpc/grpc-go.svg)](https://travis-ci.org/grpc/grpc-go) [![GoDoc](https://godoc.org/google.golang.org/grpc?status.svg)](https://godoc.org/google.golang.org/grpc)

The Go implementation of [gRPC](http://www.grpc.io/): A high performance, open source, general RPC framework that puts mobile and HTTP/2 first. For more information see the [gRPC Quick Start](http://www.grpc.io/docs/) guide.

Installation
------------

To install this package, you need to install Go and setup your Go workspace on your computer. The simplest way to install the library is to run:

```
$ go get google.golang.org/grpc
```

Prerequisites
-------------

This requires Go 1.5 or later.

A note on the version used: significant performance improvements in benchmarks
of grpc-go have been seen by upgrading the go version from 1.5 to the latest
1.7.1.

From https://golang.org/doc/install, one way to install the latest version of go is:
```
$ GO_VERSION=1.7.1
$ OS=linux
$ ARCH=amd64
$ curl -O https://storage.googleapis.com/golang/go${GO_VERSION}.${OS}-${ARCH}.tar.gz
$ sudo tar -C /usr/local -xzf go$GO_VERSION.$OS-$ARCH.tar.gz
$ # Put go on the PATH, keep the usual installation dir
$ sudo ln -s /usr/local/go/bin/go /usr/bin/go
$ rm go$GO_VERSION.$OS-$ARCH.tar.gz
```

Constraints
-----------
The grpc package should only depend on standard Go packages and a small number of exceptions. If your contribution introduces new dependencies which are NOT in the [list](http://godoc.org/google.golang.org/grpc?imports), you need a discussion with gRPC-Go authors and consultants.

Documentation
-------------
See [API documentation](https://godoc.org/google.golang.org/grpc) for package and API descriptions and find examples in the [examples directory](examples/).

Status
------
GA

FAQ
---

#### Compiling error, undefined: grpc.SupportPackageIsVersion

Please update proto package, gRPC package and rebuild the proto files:
 - `go get -u github.com/golang/protobuf/{proto,protoc-gen-go}`
 - `go get -u google.golang.org/grpc`
 - `protoc --go_out=plugins=grpc:. *.proto`
gRPC in 3 minutes (Go)
======================

BACKGROUND
-------------
For this sample, we've already generated the server and client stubs from [helloworld.proto](helloworld/helloworld/helloworld.proto).

PREREQUISITES
-------------

- This requires Go 1.5 or later
- Requires that [GOPATH is set](https://golang.org/doc/code.html#GOPATH)

```
$ go help gopath
$ # ensure the PATH contains $GOPATH/bin
$ export PATH=$PATH:$GOPATH/bin
```

INSTALL
-------

```
$ go get -u google.golang.org/grpc/examples/helloworld/greeter_client
$ go get -u google.golang.org/grpc/examples/helloworld/greeter_server
```

TRY IT!
-------

- Run the server

```
$ greeter_server &
```

- Run the client

```
$ greeter_client
```

OPTIONAL - Rebuilding the generated code
----------------------------------------

1 First [install protoc](https://github.com/google/protobuf/blob/master/README.md)
  - For now, this needs to be installed from source
  - This is will change once proto3 is officially released

2 Install the protoc Go plugin.

```
$ go get -a github.com/golang/protobuf/protoc-gen-go
$
$ # from this dir; invoke protoc
$  protoc -I ./helloworld/helloworld/ ./helloworld/helloworld/helloworld.proto --go_out=plugins=grpc:helloworld
```
# Description
The route guide server and client demonstrate how to use grpc go libraries to
perform unary, client streaming, server streaming and full duplex RPCs.

Please refer to [gRPC Basics: Go] (http://www.grpc.io/docs/tutorials/basic/go.html) for more information.

See the definition of the route guide service in proto/route_guide.proto.

# Run the sample code
To compile and run the server, assuming you are in the root of the route_guide
folder, i.e., .../examples/route_guide/, simply:

```sh
$ go run server/server.go
```

Likewise, to run the client:

```sh
$ go run client/client.go
```

# Optional command line flags
The server and client both take optional command line flags. For example, the
client and server run without TLS by default. To enable TLS:

```sh
$ go run server/server.go -tls=true
```

and

```sh
$ go run client/client.go -tls=true
```
# Reflection

Package reflection implements server reflection service.

The service implemented is defined in: https://github.com/grpc/grpc/blob/master/src/proto/grpc/reflection/v1alpha/reflection.proto.

To register server reflection on a gRPC server:
```go
import "google.golang.org/grpc/reflection"

s := grpc.NewServer()
pb.RegisterYourOwnServer(s, &server{})

// Register reflection service on gRPC server.
reflection.Register(s)

s.Serve(lis)
```
# Go App Engine packages

[![Build Status](https://travis-ci.org/golang/appengine.svg)](https://travis-ci.org/golang/appengine)

This repository supports the Go runtime on App Engine,
including both the standard App Engine and the
"App Engine flexible environment" (formerly known as "Managed VMs").
It provides APIs for interacting with App Engine services.
Its canonical import path is `google.golang.org/appengine`.

See https://cloud.google.com/appengine/docs/go/
for more information.

File issue reports and feature requests on the [Google App Engine issue
tracker](https://code.google.com/p/googleappengine/issues/entry?template=Go%20defect).

## Directory structure
The top level directory of this repository is the `appengine` package. It
contains the
basic APIs (e.g. `appengine.NewContext`) that apply across APIs. Specific API
packages are in subdirectories (e.g. `datastore`).

There is an `internal` subdirectory that contains service protocol buffers,
plus packages required for connectivity to make API calls. App Engine apps
should not directly import any package under `internal`.

## Updating a Go App Engine app

This section describes how to update an older Go App Engine app to use
these packages. A provided tool, `aefix`, can help automate steps 2 and 3
(run `go get google.golang.org/appengine/cmd/aefix` to install it), but
read the details below since `aefix` can't perform all the changes.

### 1. Update YAML files (App Engine flexible environment / Managed VMs only)

The `app.yaml` file (and YAML files for modules) should have these new lines added:
```
vm: true
```
See https://cloud.google.com/appengine/docs/go/modules/#Go_Instance_scaling_and_class for details.

### 2. Update import paths

The import paths for App Engine packages are now fully qualified, based at `google.golang.org/appengine`.
You will need to update your code to use import paths starting with that; for instance,
code importing `appengine/datastore` will now need to import `google.golang.org/appengine/datastore`.

### 3. Update code using deprecated, removed or modified APIs

Most App Engine services are available with exactly the same API.
A few APIs were cleaned up, and some are not available yet.
This list summarises the differences:

* `appengine.Context` has been replaced with the `Context` type from `golang.org/x/net/context`.
* Logging methods that were on `appengine.Context` are now functions in `google.golang.org/appengine/log`.
* `appengine.Timeout` has been removed. Use `context.WithTimeout` instead.
* `appengine.Datacenter` now takes a `context.Context` argument.
* `datastore.PropertyLoadSaver` has been simplified to use slices in place of channels.
* `delay.Call` now returns an error.
* `search.FieldLoadSaver` now handles document metadata.
* `urlfetch.Transport` no longer has a Deadline field; set a deadline on the
  `context.Context` instead.
* `aetest` no longer declares its own Context type, and uses the standard one instead.
* `taskqueue.QueueStats` no longer takes a maxTasks argument. That argument has been
  deprecated and unused for a long time.
* `appengine.BackendHostname` and `appengine.BackendInstance` were for the deprecated backends feature.
  Use `appengine.ModuleHostname`and `appengine.ModuleName` instead.
* Most of `appengine/file` and parts of `appengine/blobstore` are deprecated.
  Use [Google Cloud Storage](https://godoc.org/cloud.google.com/go/storage) if the
  feature you require is not present in the new
  [blobstore package](https://google.golang.org/appengine/blobstore).
* `appengine/socket` is not required on App Engine flexible environment / Managed VMs.
  Use the standard `net` package instead.
angular-loading-bar
===================

The idea is simple: Add a loading bar / progress bar whenever an XHR request goes out in angular.  Multiple requests within the same time period get bundled together such that each response increments the progress bar by the appropriate amount.

This is mostly cool because you simply include it in your app, and it works.  There's no complicated setup, and no need to maintain the state of the loading bar; it's all handled automatically by the interceptor.

**Requirements:** AngularJS 1.2+

**File Size:** 2.4Kb minified, 0.5Kb gzipped


## Usage:

1. include the loading bar as a dependency for your app.  If you want animations, include `ngAnimate` as well. *note: ngAnimate is optional*

    ```js
    angular.module('myApp', ['angular-loading-bar', 'ngAnimate'])
    ```
    
2. include the supplied CSS file (or create your own).
3. That's it -- you're done!

#### via bower:
```
$ bower install angular-loading-bar
```
#### via npm:
```
$ npm install angular-loading-bar
```


## Why I created this
There are a couple projects similar to this out there, but none were ideal for me.  All implementations I've seen require that you maintain state on behalf of the loading bar.  In other words, you're setting the value of the loading/progress bar manually from potentially many different locations.  This becomes complicated when you have a very large application with several services all making independant XHR requests. It becomes even more complicated if you want these services to be loosly coupled.

Additionally, Angular was created as a highly testable framework, so it pains me to see Angular modules without tests.  That is not the case here as this loading bar ships with 100% code coverage.


**Goals for this project:**

1. Make it automatic
2. Unit tests, 100% coverage
3. Must work well with ngAnimate
4. Must be styled via external CSS (not inline)
5. No jQuery dependencies


## Configuration

#### Turn the spinner on or off:
The insertion of the spinner can be controlled through configuration.  It's on by default, but if you'd like to turn it off, simply configure the service:

```js
angular.module('myApp', ['angular-loading-bar'])
  .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.includeSpinner = false;
  }])
```

#### Turn the loading bar on or off:
Like the spinner configuration above, the loading bar can also be turned off for cases where you only want the spinner:

```js
angular.module('myApp', ['angular-loading-bar'])
  .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.includeBar = false;
  }])
```

#### Latency Threshold
By default, the loading bar will only display after it has been waiting for a response for over 100ms.  This helps keep things feeling snappy, and avoids the annoyingness of showing a loading bar every few seconds on really chatty applications.  This threshold is totally configurable:

```js
angular.module('myApp', ['angular-loading-bar'])
  .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.latencyThreshold = 500;
  }])
```

#### Ignoring particular XHR requests:
The loading bar can also be forced to ignore certain requests, for example, when long-polling or periodically sending debugging information back to the server.

```js
// ignore particular $http requests:
$http.get('/status', {
  ignoreLoadingBar: true
});

```


```js
// ignore particular $resource requests:
.factory('Restaurant', function($resource) {
  return $resource('/api/restaurant/:id', {id: '@id'}, {
    query: {
      method: 'GET',
      isArray: true,
      ignoreLoadingBar: true
    }
  });
});

```




## How it works:
This library is split into two modules, an $http `interceptor`, and a `service`:

**Interceptor**  
The interceptor simply listens for all outgoing XHR requests, and then instructs the loadingBar service to start, stop, and increment accordingly.  There is no public API for the interceptor.  It can be used stand-alone by including `cfp.loadingBarInterceptor` as a dependency for your module.

**Service**  
The service is responsible for the presentation of the loading bar.  It injects the loading bar into the DOM, adjusts the width whenever `set()` is called, and `complete()`s the whole show by removing the loading bar from the DOM.

## Service API (advanced usage)
Under normal circumstances you won't need to use this.  However, if you wish to use the loading bar without the interceptor, you can do that as well.  Simply include the loading bar service as a dependency instead of the main `angular-loading-bar` module:

```js
angular.module('myApp', ['cfp.loadingBar'])
```


```js

cfpLoadingBar.start();
// will insert the loading bar into the DOM, and display its progress at 1%.
// It will automatically call `inc()` repeatedly to give the illusion that the page load is progressing.

cfpLoadingBar.inc();
// increments the loading bar by a random amount.
// It is important to note that the auto incrementing will begin to slow down as
// the progress increases.  This is to prevent the loading bar from appearing
// completed (or almost complete) before the XHR request has responded. 

cfpLoadingBar.set(0.3) // Set the loading bar to 30%
cfpLoadingBar.status() // Returns the loading bar's progress.
// -> 0.3

cfpLoadingBar.complete()
// Set the loading bar's progress to 100%, and then remove it from the DOM.

```

## Events
The loading bar broadcasts the following events over $rootScope allowing further customization:

**`cfpLoadingBar:loading`** triggered upon each XHR request that is not already cached

**`cfpLoadingBar:loaded`** triggered each time an XHR request recieves a response (either successful or error)

**`cfpLoadingBar:started`** triggered once upon the first XHR request.  Will trigger again if another request goes out after `cfpLoadingBar:completed` has triggered.

**`cfpLoadingBar:completed`** triggered once when the all XHR requests have returned (either successfully or not)

## Credits: 
Credit goes to [rstacruz](https://github.com/rstacruz) for his excellent [nProgress](https://github.com/rstacruz/nprogress).

## License:
Licensed under the MIT license
angular-ui-notification
=======================

[![Dependency Status](https://david-dm.org/alexcrack/angular-ui-notification.png)](https://david-dm.org/alexcrack/angular-ui-notification)
[![devDependency Status](https://david-dm.org/alexcrack/angular-ui-notification/dev-status.png)](https://david-dm.org/alexcrack/angular-ui-notification#info=devDependencies)
[![Build Status](https://travis-ci.org/alexcrack/angular-ui-notification.svg?branch=master)](https://travis-ci.org/alexcrack/angular-ui-notification)
[![Dependency Status](https://www.versioneye.com/user/projects/54f96af44f3108e7800000e4/badge.svg?style=flat)](https://www.versioneye.com/user/projects/54f96af44f3108e7800000e4)
[![Code Climate](https://codeclimate.com/github/alexcrack/angular-ui-notification/badges/gpa.svg)](https://codeclimate.com/github/alexcrack/angular-ui-notification)

Angular.js service providing simple notifications using Bootstrap 3 styles with css transitions for animations

## Features
* No dependencies except of angular.js.
* CSS3 Animations.
* Small size.
* 5 message types.
* Use HTML in your messages.
* Configure options globally py the provider
* Use custom options by the message
* Use custom template

## Install

To install the package using bower and save as a dependency use...
```bash
bower install angular-ui-notification --save
```  

## Usage
 [Heres a plunker demo](http://plnkr.co/edit/5Gk8UVvzUsjyof7Gxsua?p=preview)

  
In your html/template add 
```html
...
  <link rel="stylesheet" href="angular-ui-notification.min.css">
...
  <script src="angular-ui-notification.min.js"></script>
...

```

In your application, declare dependency injection like so..

```javascript
  angular.module('notificationTest', ['ui-notification']);
...
```

You can configure module by the provider
```javascript
angular.module('notificationTest', ['ui-notification'])
    .config(function(NotificationProvider) {
        NotificationProvider.setOptions({
            delay: 10000,
            startTop: 20,
            startRight: 10,
            verticalSpacing: 20,
            horizontalSpacing: 20,
            positionX: 'left',
            positionY: 'bottom'
        });
    });
...
```


And when you need to show notifications, inject service and call it!

```javascript
angular.module('notificationTest').controller('notificationController', function($scope, Notification) {
 
  Notification.primary('Primary notification');
  // or simply..
  Notification('Primary notification');
  
  // Other Options
  // Success
  Notification.success('Success notification');
  
  // With Title
  Notification({message: 'Primary notification', title: 'Primary notification'});
  
  // Message with custom delay
  Notification.error({message: 'Error notification 1s', delay: 1000});
  
  // Embed HTML within your message.....
  Notification.success({message: 'Success notification<br>Some other <b>content</b><br><a href="https://github.com/alexcrack/angular-ui-notification">This is a link</a><br><img src="https://angularjs.org/img/AngularJS-small.png">', title: 'Html content'});

  // Change position notification
  Notification.error({message: 'Error Bottom Right', positionY: 'bottom', positionX: 'right'});
  
  // Replace message
  Notification.error({message: 'Error notification 1s', replaceMessage: true});
}
```

## Service

Module name: "ui-notification"

Service: "Notification"

Configuration provider: "NotificationProvider"


## Options

Options can be passed to configuration provider globally or used in the current message.

The options list:

|       Option      |      Possible values      |         Default value          |                               Description                                |
| ----------------- | ------------------------- | ------------------------------ | ------------------------------------------------------------------------ |
| delay             | Any integer value         | 5000                           | The time in ms the message is showing before start fading out            |
| startTop          | Any integer value         | 10                             | Vertical padding between messages and vertical border of the browser     |
| startRight        | Any integer value         | 10                             | Horizontal padding between messages and horizontal border of the browser |
| verticalSpacing   | Any integer value         | 10                             | Vertical spacing between messages                                        |
| horizontalSpacing | Any integer value         | 10                             | Horizontal spacing between messages                                      |
| positionX         | "right", "left", "center" | "right"                        | Horizontal position of the message                                       |
| positionY         | "top", "bottom"           | "top"                          | Vertical position of the message                                         |
| replaceMessage    | true, false               | false                          | If true every next appearing message replace old messages                |
| templateUrl       | Any string                | "angular-ui-notification.html" | Custom template filename (URL)                                           |

Also you can pass the "scope" option. This is an angular scope option Notification scope will be inherited from. This option can be passed only in the methods. The default value is $rootScope

## Methods

#### Notification service methods

|              Method name               |                   Description                   |
|----------------------------------------|-------------------------------------------------|
| Notification(), Notification.primary() | Show the message with bootstrap's primary class |
| Notification.info()                    | Show the message with bootstrap's info class    |
| Notification.success()                 | Show the message with bootstrap's success class |
| Notification.warning()                 | Show the message with bootstrap's warn class    |
| Notification.error()                   | Show the message with bootstrap's danger class  |
| Notification.clearAll()                | Remove all shown messages                       |

#### Notification service options

|     Option     |                 Possible values                  |           Default value           |                                              Description                                               |
| -------------- | ------------------------------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| title          | *String*                                         | `""`                              | Title to appear at the top of the notification                                                         |
| message        | *String*                                         | `""`                              | Message to appear in the notification                                                                  |
| templateUrl    | *String*                                         | `"angular-ui-notification.html"`  | URL of template to be used for notification                                                            |
| delay          | *Int* (?)                                        | `5000` or configured global delay | Number of ms before notification fades out. If not an integer, notification will persist until killed. |
| type           | "primary", "info", "success", "warning", "error" | `"primary"`                       | Bootstrap flavoring                                                                                    |
| positionY      | "top", "bottom"                                  | `"top"`                           |                                                                                                        |
| positionX      | "right", "left", "center"                        | `"right"                          |                                                                                                        |
| replaceMessage | *Boolean*                                        | `false`                           | If true this message will replace old(er) message(s)                                                   |

#### Returning value

Every "show" method returns a promise resolves a notification scope with methods:

|          Method name           |                                                   Description                                                    |
|--------------------------------|------------------------------------------------------------------------------------------------------------------|
| notificationScope.kill(isHard) | Remove the specific message<br>isHard - if false or omitted kill message with fadeout effect (default). If true - immediately remove the message|



## Custom Templates

Custom template can be provided.

```html
<div class="ui-notification">
    <h3 ng-show="title" ng-bind-html="title"></h3>
    <div class="message" ng-bind-html="message"></div>
</div>
```
Default existing scope values is "title" - the title of the message and "message".
Also any custom scope's properties can be used.
# Chart.js 

[![Build Status](https://travis-ci.org/nnnick/Chart.js.svg?branch=master)](https://travis-ci.org/nnnick/Chart.js) [![Code Climate](https://codeclimate.com/github/nnnick/Chart.js/badges/gpa.svg)](https://codeclimate.com/github/nnnick/Chart.js)


*Simple HTML5 Charts using the canvas element* [chartjs.org](http://www.chartjs.org)

## Documentation

You can find documentation at [chartjs.org/docs](http://www.chartjs.org/docs/). The markdown files that build the site are available under `/docs`. Please note - in some of the json examples of configuration you might notice some liquid tags - this is just for the generating the site html, please disregard.

## Bugs, issues and contributing

Before submitting an issue or a pull request to the project, please take a moment to look over the [contributing guidelines](https://github.com/nnnick/Chart.js/blob/master/CONTRIBUTING.md) first.

For support using Chart.js, please post questions with the [`chartjs` tag on Stack Overflow](http://stackoverflow.com/questions/tagged/chartjs).

## License

Chart.js is available under the [MIT license](http://opensource.org/licenses/MIT).
# bower-angular-sanitize

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngSanitize).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-sanitize
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-sanitize/angular-sanitize.js"></script>
```

And add `ngSanitize` as a dependency for your app:

```javascript
angular.module('myApp', ['ngSanitize']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngSanitize).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# bower-angular-animate

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngAnimate).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-animate
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-animate/angular-animate.js"></script>
```

And add `ngAnimate` as a dependency for your app:

```javascript
angular.module('myApp', ['ngAnimate']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngAnimate).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# bower-angular-mocks

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngMock).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-mocks
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/guide/dev_guide.unit-testing).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# metisMenu [![Build Status](https://secure.travis-ci.org/onokumus/metisMenu.png?branch=master)](https://travis-ci.org/onokumus/metisMenu)

> Easy menu jQuery plugin for Twitter Bootstrap 3

> Now support cdnjs & jsdelivr


## Installation

* [npm](http://npmjs.org/)

```bash
npm install metismenu
```

* [Bower](http://bower.io)

```bash
bower install metisMenu
```

* [Download](https://github.com/onokumus/metisMenu/archive/master.zip)

## Usage

1. Include Twitter Bootstrap StyleSheet

    ```html
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.0/css/bootstrap.min.css">
    ```

2. Include metisMenu StyleSheet

    ```html
    <link rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap.metismenu/1.1.2/css/metismenu.min.css">
    ```

3. Include jQuery

    ```html
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    ```

4. Include Twitter Bootstrap Script

    ```html
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.0/js/bootstrap.min.js"></script>
    ```

5. Include metisMenu plugin's code

    ```html
    <script src="//cdn.jsdelivr.net/bootstrap.metismenu/1.1.2/js/metismenu.min.js"></script>
    ```

6. Call the plugin:

    ```javascript
    $("#menu").metisMenu();
    ```

### Options

#### toggle
Type: `Boolean`
Default: `true`

For auto collapse support.

```javascript
  $("#menu").metisMenu({
    toggle: false
  });
```

#### doubleTapToGo
Type: `Boolean`
Default: `false`

For double tap support.

```javascript
  $("#menu").metisMenu({
    doubleTapToGo: true
  });
```


### [DEMO](http://demo.onokumus.com/metisMenu/)

Contains a simple HTML file to demonstrate metisMenu plugin.

### Release History
**DATE**       **VERSION**   **CHANGES**
* 2014-11-01   v1.1.3        Bootstrap 3.3.0
* 2014-07-07   v1.1.0	       Add double tap functionality
* 2014-06-24   v1.0.3	       cdnjs support & rename plugin
* 2014-06-18   v1.0.3        Create grunt task
* 2014-06-10   v1.0.2        Fixed for IE8 & IE9


## Author

metisMenu was made with love by these guys and a bunch of awesome [contributors](https://github.com/onokumus/metisMenu/graphs/contributors).

[![Osman Nuri Okumuş](https://0.gravatar.com/avatar/4fa374411129d6f574c33e4753ec402e?s=70)](http://onokumus.com) |
--- | --- | --- | --- | --- | --- | ---
[Osman Nuri Okumuş](http://onokumus.com) |


## License

[MIT License](https://github.com/onokumus/metisMenu/blob/master/LICENSE)
# angular-chart.js

[![Bower version](https://badge.fury.io/bo/angular-chart.js.svg)](http://badge.fury.io/bo/angular-chart.js)
[![npm version](https://badge.fury.io/js/angular-chart.js.svg)](http://badge.fury.io/js/angular-chart.js)
[![Build Status](https://travis-ci.org/jtblin/angular-chart.js.png)](https://travis-ci.org/jtblin/angular-chart.js)
[![Code Climate](https://codeclimate.com/github/jtblin/angular-chart.js/badges/gpa.svg)](https://codeclimate.com/github/jtblin/angular-chart.js)

Beautiful, reactive, responsive charts for Angular.JS using [Chart.js](http://www.chartjs.org/). 

[Demo](http://jtblin.github.io/angular-chart.js/)

# Installation

    bower install angular-chart.js --save
    
or copy the files from `dist/`. Then add the sources to your code (adjust paths as needed) after 
adding the dependencies for Angular and Chart.js first:

```html
<script src="../bower_components/angular/angular.min.js"></script>
<script src="/bower_components/Chart.js/Chart.min.js"></script>
<script src="/bower_components/angular-chart.js/dist/angular-chart.js"></script>
```

# Utilisation

There are 6 types of charts so 6 directives: `chart-line`, `chart-bar`, `chart-radar`, `chart-pie`, 
`chart-polar-area`, `chart-doughnut`.

They all use mostly the same API:

- `data`: series data
- `labels`: x axis labels (line, bar, radar) or series labels (pie, doughnut, polar area)
- `options`: chart options (as from [Chart.js documentation](http://www.chartjs.org/docs/))
- `series`: (default: `[]`): series labels (line, bar, radar)
- `colours`: data colours (will use default colours if not specified)
- `getColour`: function that returns a colour in case there are not enough (will use random colours if not specified)
- `click`: onclick event handler
- `legend`: (default: `false`): show legend below the chart

There is another directive `chart-base` that takes an extra attribute `chart-type` to define the type
dynamically, see [stacked bar example](http://jtblin.github.io/angular-chart.js/examples/stacked-bars.html).

## Browser compatibility

For IE8 and older browsers, you will need 
to include [excanvas](https://code.google.com/p/explorercanvas/wiki/Instructions). 
You will also need [shims](https://github.com/es-shims/es5-shim) for ES5 functions.

```html
<head>
<!--[if lt IE 9]><script src="excanvas.js"></script><![endif]-->
<!--[if lt IE 9]><script src="es5-shim.js"></script><![endif]-->
</head>
```

# Example

## Markup

```html
<canvas id="line" class="chart chart-line" data="data" labels="labels" 
	legend="true" series="series" click="onClick"></canvas> 
```

## Javascript

```javascript
angular.module("app", ["chart.js"]).controller("LineCtrl", ['$scope', '$timeout', function ($scope, $timeout) {

  $scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
  $scope.series = ['Series A', 'Series B'];
  $scope.data = [
    [65, 59, 80, 81, 56, 55, 40],
    [28, 48, 40, 19, 86, 27, 90]
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  
  // Simulate async data update
  $timeout(function () {
    $scope.data = [
      [28, 48, 40, 19, 86, 27, 90],
      [65, 59, 80, 81, 56, 55, 40]
    ];
  }, 3000);
}]);
```

## Reactive

angular-chart.js watch updates on data, series, labels, colours and options and will update, or destroy and recreate, 
the chart on changes.

## Events

angular-chart.js emits the following events on the `scope` and pass the chart as argument:

* `create`: when chart is created
* `update`: when chart is updated

```
$scope.$on('create', function (event, chart) {
  console.log(chart);
});
```

**Note**: the event can be emitted multiple times for each chart as the chart can be destroyed and
created multiple times during angular `watch` lifecycle.

angular-chart.js listen to the scope `destroy` event and destroy the chart when it happens.

## Colours

There are a set of 7 default colours. Colours can be replaced using the `colours` attribute.
If there is more data than colours, colours are generated randomly or can be provided 
via a function through the `getColour` attribute.

Hex colours are converted to Chart.js colours automatically, 
including different shades for highlight, fill, stroke, etc.

# Issues

**Issues or feature requests for Chart.js (e.g. new chart type, new axis, etc.) need to be opened on 
[Chart.js issues tracker](https://github.com/nnnick/Chart.js/issues)**
 
Please check if issue exists and otherwise open issue in [github](https://github.com/jtblin/angular-chart.js/issues). 
**Please add a link to a plunker, jsbin, or equivalent.** 
Here is a [jsbin template](http://jsbin.com/dufibi/3/edit?html,js,output) for convenience.

# Contributing
 
Pull requests welcome!

1. Fork the repo
1. Make your changes
1. Run tests: `npm test`
1. Submit pull request

## Contributors

Thank you!

* @ManuelRauber
* @vad710
* @JAAulde
* @offsky
* @jonathansampson

# Author

Jerome Touffe-Blin, [@jtblin](https://twitter.com/jtblin), [About me](http://about.me/jtblin)

# License

angular-chart.js is copyright 2014 Jerome Touffe-Blin and contributors. 
It is licensed under the BSD license. See the include LICENSE file for details.
# JSON 3 #

![JSON 3 Logo](http://bestiejs.github.io/json3/page/logo.png)

[![Build Status](https://secure.travis-ci.org/bestiejs/json3.png?branch=gh-pages)](http://travis-ci.org/bestiejs/json3)

**JSON 3** is a modern JSON implementation compatible with a variety of JavaScript platforms, including Internet Explorer 6, Opera 7, Safari 2, and Netscape 6. The current version is **3.3.2**.

- [Development Version](http://cdnjs.cloudflare.com/ajax/libs/json3/3.3.2/json3.js) *(43 KB; uncompressed with comments)*
- [Production Version](http://cdnjs.cloudflare.com/ajax/libs/json3/3.3.2/json3.min.js) *(3.5 KB; compressed and `gzip`-ped)*

Special thanks to [cdnjs](http://cdnjs.com/libraries/json3/) and [jsDelivr](http://www.jsdelivr.com/#!json3) for hosting CDN copies of JSON 3.

[JSON](http://json.org/) is a language-independent data interchange format based on a loose subset of the JavaScript grammar. Originally popularized by [Douglas Crockford](http://www.crockford.com/), the format was standardized in the [fifth edition](http://es5.github.com/) of the ECMAScript specification. The 5.1 edition, ratified in June 2011, incorporates several modifications to the grammar pertaining to the serialization of dates.

JSON 3 exposes two functions: `stringify()` for [serializing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/stringify) a JavaScript value to JSON, and `parse()` for [producing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/parse) a JavaScript value from a JSON source string. It is a **drop-in replacement** for [JSON 2](http://json.org/js). The functions behave exactly as described in the ECMAScript spec, **except** for the date serialization discrepancy noted below.

The JSON 3 parser does **not** use `eval` or regular expressions. This provides security and performance benefits in obsolete and mobile environments, where the margin is particularly significant. The complete [benchmark suite](http://jsperf.com/json3) is available on [jsPerf](http://jsperf.com/).

The project is [hosted on GitHub](http://git.io/json3), along with the [unit tests](http://bestiejs.github.io/json3/test/test_browser.html). It is part of the [BestieJS](https://github.com/bestiejs) family, a collection of best-in-class JavaScript libraries that promote cross-platform support, specification precedents, unit testing, and plenty of documentation.

# Changes from JSON 2 #

JSON 3...

* Correctly serializes primitive wrapper objects.
* Throws a `TypeError` when serializing cyclic structures (JSON 2 recurses until the call stack overflows).
* Utilizes **feature tests** to detect broken or incomplete *native* JSON implementations (JSON 2 only checks for the presence of the native functions). The tests are only executed once at runtime, so there is no additional performance cost when parsing or serializing values.

**As of v3.2.3**, JSON 3 is compatible with [Prototype](http://prototypejs.org) 1.6.1 and older.

In contrast to JSON 2, JSON 3 **does not**...

* Add `toJSON()` methods to the `Boolean`, `Number`, and `String` prototypes. These are not part of any standard, and are made redundant by the design of the `stringify()` implementation.
* Add `toJSON()` or `toISOString()` methods to `Date.prototype`. See the note about date serialization below.

## Date Serialization

**JSON 3 deviates from the specification in one important way**: it does not define `Date#toISOString()` or `Date#toJSON()`. This preserves CommonJS compatibility and avoids polluting native prototypes. Instead, date serialization is performed internally by the `stringify()` implementation: if a date object does not define a custom `toJSON()` method, it is serialized as a [simplified ISO 8601 date-time string](http://es5.github.com/#x15.9.1.15).

**Several native `Date#toJSON()` implementations produce date time strings that do *not* conform to the grammar outlined in the spec**. For instance, all versions of Safari 4, as well as JSON 2, fail to serialize extended years correctly. Furthermore, JSON 2 and older implementations omit the milliseconds from the date-time string (optional in ES 5, but required in 5.1). Finally, in all versions of Safari 4 and 5, serializing an invalid date will produce the string `"Invalid Date"`, rather than `null`. Because these environments exhibit other serialization bugs, however, JSON 3 will override the native `stringify()` implementation.

Portions of the date serialization code are adapted from the [`date-shim`](https://github.com/Yaffle/date-shim) project.

# Usage #

## Web Browsers

    <script src="//cdnjs.cloudflare.com/ajax/libs/json3/3.3.2/json3.min.js"></script>
    <script>
      JSON.stringify({"Hello": 123});
      // => '{"Hello":123}'
      JSON.parse("[[1, 2, 3], 1, 2, 3, 4]", function (key, value) {
        if (typeof value == "number") {
          value = value % 2 ? "Odd" : "Even";
        }
        return value;
      });
      // => [["Odd", "Even", "Odd"], "Odd", "Even", "Odd", "Even"]
    </script>

**When used in a web browser**, JSON 3 exposes an additional `JSON3` object containing the `noConflict()` and `runInContext()` functions, as well as aliases to the `stringify()` and `parse()` functions.

### `noConflict` and `runInContext`

* `JSON3.noConflict()` restores the original value of the global `JSON` object and returns a reference to the `JSON3` object.
* `JSON3.runInContext([context, exports])` initializes JSON 3 using the given `context` object (e.g., `window`, `global`, etc.), or the global object if omitted. If an `exports` object is specified, the `stringify()`, `parse()`, and `runInContext()` functions will be attached to it instead of a new object.

### Asynchronous Module Loaders

JSON 3 is defined as an [anonymous module](https://github.com/amdjs/amdjs-api/wiki/AMD#define-function-) for compatibility with [RequireJS](http://requirejs.org/), [`curl.js`](https://github.com/cujojs/curl), and other asynchronous module loaders.

    <script src="//cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.js"></script>
    <script>
      require({
        "paths": {
          "json3": "./path/to/json3"
        }
      }, ["json3"], function (JSON) {
        JSON.parse("[1, 2, 3]");
        // => [1, 2, 3]
      });
    </script>

To avoid issues with third-party scripts, **JSON 3 is exported to the global scope even when used with a module loader**. If this behavior is undesired, `JSON3.noConflict()` can be used to restore the global `JSON` object to its original value.

## CommonJS Environments

    var JSON3 = require("./path/to/json3");
    JSON3.parse("[1, 2, 3]");
    // => [1, 2, 3]

## JavaScript Engines

    load("path/to/json3.js");
    JSON.stringify({"Hello": 123, "Good-bye": 456}, ["Hello"], "\t");
    // => '{\n\t"Hello": 123\n}'

# Compatibility #

JSON 3 has been **tested** with the following web browsers, CommonJS environments, and JavaScript engines.

## Web Browsers

- Windows [Internet Explorer](http://www.microsoft.com/windows/internet-explorer), version 6.0 and higher
- Mozilla [Firefox](http://www.mozilla.com/firefox), version 1.0 and higher
- Apple [Safari](http://www.apple.com/safari), version 2.0 and higher
- [Opera](http://www.opera.com) 7.02 and higher
- [Mozilla](http://sillydog.org/narchive/gecko.php) 1.0, [Netscape](http://sillydog.org/narchive/) 6.2.3, and [SeaMonkey](http://www.seamonkey-project.org/) 1.0 and higher

## CommonJS Environments

- [Node](http://nodejs.org/) 0.2.6 and higher
- [RingoJS](http://ringojs.org/) 0.4 and higher
- [Narwhal](http://narwhaljs.org/) 0.3.2 and higher

## JavaScript Engines

- Mozilla [Rhino](http://www.mozilla.org/rhino) 1.5R5 and higher
- WebKit [JSC](https://trac.webkit.org/wiki/JSC)
- Google [V8](http://code.google.com/p/v8)

## Known Incompatibilities

* Attempting to serialize the `arguments` object may produce inconsistent results across environments due to specification version differences. As a workaround, please convert the `arguments` object to an array first: `JSON.stringify([].slice.call(arguments, 0))`.

## Required Native Methods

JSON 3 assumes that the following methods exist and function as described in the ECMAScript specification:

- The `Number`, `String`, `Array`, `Object`, `Date`, `SyntaxError`, and `TypeError` constructors.
- `String.fromCharCode`
- `Object#toString`
- `Function#call`
- `Math.floor`
- `Number#toString`
- `Date#valueOf`
- `String.prototype`: `indexOf`, `charCodeAt`, `charAt`, `slice`.
- `Array.prototype`: `push`, `pop`, `join`.

# Contribute #

Check out a working copy of the JSON 3 source code with [Git](http://git-scm.com/):

    $ git clone git://github.com/bestiejs/json3.git
    $ cd json3

If you'd like to contribute a feature or bug fix, you can [fork](http://help.github.com/fork-a-repo/) JSON 3, commit your changes, and [send a pull request](http://help.github.com/send-pull-requests/). Please make sure to update the unit tests in the `test` directory as well.

Alternatively, you can use the [GitHub issue tracker](https://github.com/bestiejs/json3/issues) to submit bug reports, feature requests, and questions, or send tweets to [@kitcambridge](http://twitter.com/kitcambridge).

JSON 3 is released under the [MIT License](http://kit.mit-license.org/).
# bower-angular-resource

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngResource).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-resource
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-resource/angular-resource.js"></script>
```

And add `ngResource` as a dependency for your app:

```javascript
angular.module('myApp', ['ngResource']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngResource).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# bower-angular-scenario

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngScenario).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-scenario
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# [Bootstrap](http://getbootstrap.com)
[![Slack](https://bootstrap-slack.herokuapp.com/badge.svg)](https://bootstrap-slack.herokuapp.com)
![Bower version](https://img.shields.io/bower/v/bootstrap.svg)
[![npm version](https://img.shields.io/npm/v/bootstrap.svg)](https://www.npmjs.com/package/bootstrap)
[![Build Status](https://img.shields.io/travis/twbs/bootstrap/master.svg)](https://travis-ci.org/twbs/bootstrap)
[![devDependency Status](https://img.shields.io/david/dev/twbs/bootstrap.svg)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat), and maintained by the [core team](https://github.com/orgs/twbs/people) with the massive support and involvement of the community.

To get started, check out <http://getbootstrap.com>!

## Table of contents

- [Quick start](#quick-start)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Quick start

Several quick start options are available:

- [Download the latest release](https://github.com/twbs/bootstrap/archive/v3.3.5.zip).
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
- Install with [Bower](http://bower.io): `bower install bootstrap`.
- Install with [npm](https://www.npmjs.com): `npm install bootstrap`.
- Install with [Meteor](https://www.meteor.com): `meteor add twbs:bootstrap`.
- Install with [Composer](https://getcomposer.org): `composer require twbs/bootstrap`.

Read the [Getting started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   └── bootstrap-theme.min.css
├── js/
│   ├── bootstrap.js
│   └── bootstrap.min.js
└── fonts/
    ├── glyphicons-halflings-regular.eot
    ├── glyphicons-halflings-regular.svg
    ├── glyphicons-halflings-regular.ttf
    ├── glyphicons-halflings-regular.woff
    └── glyphicons-halflings-regular.woff2
```

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). CSS [source maps](https://developer.chrome.com/devtools/docs/css-preprocessors) (`bootstrap.*.map`) are available for use with certain browsers' developer tools. Fonts from Glyphicons are included, as is the optional Bootstrap theme.



## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](http://jekyllrb.com) and publicly hosted on GitHub Pages at <http://getbootstrap.com>. The docs may also be run locally.

### Running documentation locally

1. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) (requires v2.5.x).
  - **Windows users:** Read [this unofficial guide](http://jekyll-windows.juthilo.com/) to get Jekyll up and running without problems.
2. Install the Ruby-based syntax highlighter, [Rouge](https://github.com/jneen/rouge), with `gem install rouge`.
3. From the root `/bootstrap` directory, run `jekyll serve` in the command line.
4. Open <http://localhost:9001> in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.



## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include [relevant unit tests](https://github.com/twbs/bootstrap/tree/master/js/tests). All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.



## Community

Get updates on Bootstrap's development and chat with the project maintainers and community members.

- Follow [@getbootstrap on Twitter](https://twitter.com/getbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
- Join [the official Slack room](https://bootstrap-slack.herokuapp.com).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`twitter-bootstrap-3`](https://stackoverflow.com/questions/tagged/twitter-bootstrap-3)).
- Developers should use the keyword `bootstrap` on packages which modify or add to the functionality of Bootstrap when distributing through [npm](https://www.npmjs.com/browse/keyword/bootstrap) or similar delivery mechanisms for maximum discoverability.



## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.



## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>



## Copyright and license

Code and documentation copyright 2011-2015 Twitter, Inc. Code released under [the MIT license](https://github.com/twbs/bootstrap/blob/master/LICENSE). Docs released under [Creative Commons](https://github.com/twbs/bootstrap/blob/master/docs/LICENSE).
# packaged angular

This repo is for distribution on `npm` and `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js).
Please file issues and pull requests against that repo.

## Install

You can install this package either with `npm` or with `bower`.

### npm

```shell
npm install angular
```

Then add a `<script>` to your `index.html`:

```html
<script src="/node_modules/angular/angular.js"></script>
```

Or `require('angular')` from your code.

### bower

```shell
bower install angular
```

Then add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular/angular.js"></script>
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/).

## License

The MIT License

Copyright (c) 2010-2015 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
#es5-shim <sup>[![Version Badge][2]][1]</sup>

[![npm badge][9]][1]

[![Build Status][3]][4] [![dependency status][5]][6]  [![dev dependency status][7]][8]

`es5-shim.js` and `es5-shim.min.js` monkey-patch a JavaScript context to
contain all EcmaScript 5 methods that can be faithfully emulated with a
legacy JavaScript engine.

`es5-sham.js` and `es5-sham.min.js` monkey-patch other ES5 methods as
closely as possible.  For these methods, as closely as possible to ES5
is not very close.  Many of these shams are intended only to allow code
to be written to ES5 without causing run-time errors in older engines.
In many cases, this means that these shams cause many ES5 methods to
silently fail.  Decide carefully whether this is what you want.


## Tests

The tests are written with the Jasmine BDD test framework.
To run the tests, navigate to <root-folder>/tests/. 

## Shims

### Complete tests ###

* Array.prototype.every
* Array.prototype.filter
* Array.prototype.forEach
* Array.prototype.indexOf
* Array.prototype.lastIndexOf
* Array.prototype.map
* Array.prototype.some
* Array.prototype.reduce
* Array.prototype.reduceRight
* Array.isArray
* Date.now
* Date.prototype.toJSON
* Function.prototype.bind
    * :warning: Caveat: the bound function has a prototype property.
    * :warning: Caveat: bound functions do not try too hard to keep you
      from manipulating their ``arguments`` and ``caller`` properties.
    * :warning: Caveat: bound functions don't have checks in ``call`` and
      ``apply`` to avoid executing as a constructor.
* Number.prototype.toFixed
* Object.keys
* String.prototype.split
* String.prototype.trim
* String.prototype.replace
    * Firefox (through v29) natively handles capturing groups incorrectly.
* Date.parse (for ISO parsing)
* Date.prototype.toISOString
* parseInt

## Shams

* :warning: Object.create

    For the case of simply "begetting" an object that inherits
    prototypically from another, this should work fine across legacy
    engines.

    :warning: Object.create(null) will work only in browsers that
    support prototype assignment.  This creates an object that does not
    have any properties inherited from Object.prototype.  It will
    silently fail otherwise.

    :warning: The second argument is passed to Object.defineProperties
    which will probably fail either silently or with extreme predudice.

* :warning: Object.getPrototypeOf

    This will return "undefined" in some cases.  It uses `__proto__` if
    it's available.  Failing that, it uses constructor.prototype, which
    depends on the constructor property of the object's prototype having
    not been replaced.  If your object was created like this, it won't
    work:

        function Foo() {
        }
        Foo.prototype = {};

    Because the prototype reassignment destroys the constructor
    property.

    This will work for all objects that were created using
    `Object.create` implemented with this library.

* :warning: Object.getOwnPropertyNames

    This method uses Object.keys, so it will not be accurate on legacy
    engines.

* Object.isSealed

    Returns "false" in all legacy engines for all objects, which is
    conveniently guaranteed to be accurate.

* Object.isFrozen

    Returns "false" in all legacy engines for all objects, which is
    conveniently guaranteed to be accurate.

* Object.isExtensible

    Works like a charm, by trying very hard to extend the object then
    redacting the extension.

### May fail

* :warning: Object.getOwnPropertyDescriptor

    The behavior of this shim does not conform to ES5.  It should
    probably not be used at this time, until its behavior has been
    reviewed and been confirmed to be useful in legacy engines.

* :warning: Object.defineProperty

    In the worst of circumstances, IE 8 provides a version of this
    method that only works on DOM objects.  This sham will not be
    installed.  The given version of `defineProperty` will throw an
    exception if used on non-DOM objects.

    In slightly better circumstances, this method will silently fail to
    set "writable", "enumerable", and "configurable" properties.

    Providing a getter or setter with "get" or "set" on a descriptor
    will silently fail on engines that lack "__defineGetter__" and
    "__defineSetter__", which include all versions of IE.

    https://github.com/es-shims/es5-shim/issues#issue/5

* :warning: Object.defineProperties

    This uses the Object.defineProperty shim

* Object.seal

    Silently fails on all legacy engines.  This should be
    fine unless you are depending on the safety and security
    provisions of this method, which you cannot possibly
    obtain in legacy engines.

* Object.freeze

    Silently fails on all legacy engines.  This should be
    fine unless you are depending on the safety and security
    provisions of this method, which you cannot possibly
    obtain in legacy engines.

* Object.preventExtensions

    Silently fails on all legacy engines.  This should be
    fine unless you are depending on the safety and security
    provisions of this method, which you cannot possibly
    obtain in legacy engines.

[1]: https://npmjs.org/package/es5-shim
[2]: http://vb.teelaun.ch/es-shims/es5-shim.svg
[3]: https://travis-ci.org/es-shims/es5-shim.png
[4]: https://travis-ci.org/es-shims/es5-shim
[5]: https://david-dm.org/es-shims/es5-shim.png
[6]: https://david-dm.org/es-shims/es5-shim
[7]: https://david-dm.org/es-shims/es5-shim/dev-status.png
[8]: https://david-dm.org/es-shims/es5-shim#info=devDependencies
[9]: https://nodei.co/npm/es5-shim.png?downloads=true&stars=true

# AngularUI Router &nbsp;[![Build Status](https://travis-ci.org/angular-ui/ui-router.svg?branch=master)](https://travis-ci.org/angular-ui/ui-router)

#### The de-facto solution to flexible routing with nested views
---
**[Download 0.2.15](http://angular-ui.github.io/ui-router/release/angular-ui-router.js)** (or **[Minified](http://angular-ui.github.io/ui-router/release/angular-ui-router.min.js)**) **|**
**[Guide](https://github.com/angular-ui/ui-router/wiki) |**
**[API](http://angular-ui.github.io/ui-router/site) |**
**[Sample](http://angular-ui.github.com/ui-router/sample/) ([Src](https://github.com/angular-ui/ui-router/tree/gh-pages/sample)) |**
**[FAQ](https://github.com/angular-ui/ui-router/wiki/Frequently-Asked-Questions) |**
**[Resources](#resources) |**
**[Report an Issue](https://github.com/angular-ui/ui-router/blob/master/CONTRIBUTING.md#report-an-issue) |**
**[Contribute](https://github.com/angular-ui/ui-router/blob/master/CONTRIBUTING.md#contribute) |**
**[Help!](http://stackoverflow.com/questions/ask?tags=angularjs,angular-ui-router) |**
**[Discuss](https://groups.google.com/forum/#!categories/angular-ui/router)**

---

AngularUI Router is a routing framework for [AngularJS](http://angularjs.org), which allows you to organize the
parts of your interface into a [*state machine*](https://en.wikipedia.org/wiki/Finite-state_machine). Unlike the
[`$route` service](http://docs.angularjs.org/api/ngRoute.$route) in the Angular ngRoute module, which is organized around URL
routes, UI-Router is organized around [*states*](https://github.com/angular-ui/ui-router/wiki),
which may optionally have routes, as well as other behavior, attached.

States are bound to *named*, *nested* and *parallel views*, allowing you to powerfully manage your application's interface.

Check out the sample app: http://angular-ui.github.io/ui-router/sample/

-
**Note:** *UI-Router is under active development. As such, while this library is well-tested, the API may change. Consider using it in production applications only if you're comfortable following a changelog and updating your usage accordingly.*


## Get Started

**(1)** Get UI-Router in one of the following ways:
 - clone & [build](CONTRIBUTING.md#developing) this repository
 - [download the release](http://angular-ui.github.io/ui-router/release/angular-ui-router.js) (or [minified](http://angular-ui.github.io/ui-router/release/angular-ui-router.min.js))
 - [link to cdn](http://cdnjs.com/libraries/angular-ui-router)
 - via **[jspm](http://jspm.io/)**: by running `$ jspm install angular-ui-router` from your console
 - or via **[npm](https://www.npmjs.org/)**: by running `$ npm install angular-ui-router` from your console
 - or via **[Bower](http://bower.io/)**: by running `$ bower install angular-ui-router` from your console
 - or via **[Component](https://github.com/component/component)**: by running `$ component install angular-ui/ui-router` from your console

**(2)** Include `angular-ui-router.js` (or `angular-ui-router.min.js`) in your `index.html`, after including Angular itself (For Component users: ignore this step)

**(3)** Add `'ui.router'` to your main module's list of dependencies (For Component users: replace `'ui.router'` with `require('angular-ui-router')`)

When you're done, your setup should look similar to the following:

>
```html
<!doctype html>
<html ng-app="myApp">
<head>
    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.1.5/angular.min.js"></script>
    <script src="js/angular-ui-router.min.js"></script>
    <script>
        var myApp = angular.module('myApp', ['ui.router']);
        // For Component users, it should look like this:
        // var myApp = angular.module('myApp', [require('angular-ui-router')]);
    </script>
    ...
</head>
<body>
    ...
</body>
</html>
```

### [Nested States & Views](http://plnkr.co/edit/u18KQc?p=preview)

The majority of UI-Router's power is in its ability to nest states & views.

**(1)** First, follow the [setup](#get-started) instructions detailed above.

**(2)** Then, add a [`ui-view` directive](https://github.com/angular-ui/ui-router/wiki/Quick-Reference#ui-view) to the `<body />` of your app.

>
```html
<!-- index.html -->
<body>
    <div ui-view></div>
    <!-- We'll also add some navigation: -->
    <a ui-sref="state1">State 1</a>
    <a ui-sref="state2">State 2</a>
</body>
```

**(3)** You'll notice we also added some links with [`ui-sref` directives](https://github.com/angular-ui/ui-router/wiki/Quick-Reference#ui-sref). In addition to managing state transitions, this directive auto-generates the `href` attribute of the `<a />` element it's attached to, if the corresponding state has a URL. Next we'll add some templates. These will plug into the `ui-view` within `index.html`. Notice that they have their own `ui-view` as well! That is the key to nesting states and views.

>
```html
<!-- partials/state1.html -->
<h1>State 1</h1>
<hr/>
<a ui-sref="state1.list">Show List</a>
<div ui-view></div>
```
```html
<!-- partials/state2.html -->
<h1>State 2</h1>
<hr/>
<a ui-sref="state2.list">Show List</a>
<div ui-view></div>
```

**(4)** Next, we'll add some child templates. *These* will get plugged into the `ui-view` of their parent state templates.

>
```html
<!-- partials/state1.list.html -->
<h3>List of State 1 Items</h3>
<ul>
  <li ng-repeat="item in items">{{ item }}</li>
</ul>
```

>
```html
<!-- partials/state2.list.html -->
<h3>List of State 2 Things</h3>
<ul>
  <li ng-repeat="thing in things">{{ thing }}</li>
</ul>
```

**(5)** Finally, we'll wire it all up with `$stateProvider`. Set up your states in the module config, as in the following:


>
```javascript
myApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/state1");
  //
  // Now set up the states
  $stateProvider
    .state('state1', {
      url: "/state1",
      templateUrl: "partials/state1.html"
    })
    .state('state1.list', {
      url: "/list",
      templateUrl: "partials/state1.list.html",
      controller: function($scope) {
        $scope.items = ["A", "List", "Of", "Items"];
      }
    })
    .state('state2', {
      url: "/state2",
      templateUrl: "partials/state2.html"
    })
    .state('state2.list', {
      url: "/list",
      templateUrl: "partials/state2.list.html",
      controller: function($scope) {
        $scope.things = ["A", "Set", "Of", "Things"];
      }
    });
});
```

**(6)** See this quick start example in action.
>**[Go to Quick Start Plunker for Nested States & Views](http://plnkr.co/edit/u18KQc?p=preview)**

**(7)** This only scratches the surface
>**[Dive Deeper!](https://github.com/angular-ui/ui-router/wiki)**


### [Multiple & Named Views](http://plnkr.co/edit/SDOcGS?p=preview)

Another great feature is the ability to have multiple `ui-view`s view per template.

**Pro Tip:** *While multiple parallel views are a powerful feature, you'll often be able to manage your
interfaces more effectively by nesting your views, and pairing those views with nested states.*

**(1)** Follow the [setup](#get-started) instructions detailed above.

**(2)** Add one or more `ui-view` to your app, give them names.
>
```html
<!-- index.html -->
<body>
    <div ui-view="viewA"></div>
    <div ui-view="viewB"></div>
    <!-- Also a way to navigate -->
    <a ui-sref="route1">Route 1</a>
    <a ui-sref="route2">Route 2</a>
</body>
```

**(3)** Set up your states in the module config:
>
```javascript
myApp.config(function($stateProvider) {
  $stateProvider
    .state('index', {
      url: "",
      views: {
        "viewA": { template: "index.viewA" },
        "viewB": { template: "index.viewB" }
      }
    })
    .state('route1', {
      url: "/route1",
      views: {
        "viewA": { template: "route1.viewA" },
        "viewB": { template: "route1.viewB" }
      }
    })
    .state('route2', {
      url: "/route2",
      views: {
        "viewA": { template: "route2.viewA" },
        "viewB": { template: "route2.viewB" }
      }
    })
});
```

**(4)** See this quick start example in action.
>**[Go to Quick Start Plunker for Multiple & Named Views](http://plnkr.co/edit/SDOcGS?p=preview)**


## Resources

* [In-Depth Guide](https://github.com/angular-ui/ui-router/wiki)
* [API Reference](http://angular-ui.github.io/ui-router/site)
* [Sample App](http://angular-ui.github.com/ui-router/sample/) ([Source](https://github.com/angular-ui/ui-router/tree/gh-pages/sample))
* [FAQ](https://github.com/angular-ui/ui-router/wiki/Frequently-Asked-Questions)
* [Slides comparing ngRoute to ui-router](http://slid.es/timkindberg/ui-router#/)
* [UI-Router Extras / Addons](http://christopherthielen.github.io/ui-router-extras/#/home) (@christopherthielen)
 
### Videos

* [Introduction Video](https://egghead.io/lessons/angularjs-introduction-ui-router) (egghead.io)
* [Tim Kindberg on Angular UI-Router](https://www.youtube.com/watch?v=lBqiZSemrqg)
* [Activating States](https://egghead.io/lessons/angularjs-ui-router-activating-states) (egghead.io)
* [Learn Angular.js using UI-Router](http://youtu.be/QETUuZ27N0w) (LearnCode.academy)



## Reporting issues and Contributing

Please read our [Contributor guidelines](CONTRIBUTING.md) before reporting an issue or creating a pull request.
### UI Bootstrap - [AngularJS](http://angularjs.org/) directives specific to [Bootstrap](http://getbootstrap.com)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/angular-ui/bootstrap?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://secure.travis-ci.org/angular-ui/bootstrap.svg)](http://travis-ci.org/angular-ui/bootstrap)
[![devDependency Status](https://david-dm.org/angular-ui/bootstrap/dev-status.svg?branch=master)](https://david-dm.org/angular-ui/bootstrap#info=devDependencies)

### Quick links
- [Demo](#demo)
- [Installation](#installation)
    - [NPM](#install-with-npm)
    - [Bower](#install-with-bower)
    - [NuGet](#install-with-nuget)
    - [Custom](#custom-build)
    - [Manual](#manual-download)
- [Support](#support)
    - [FAQ](#faq)
    - [Supported browsers](#supported-browsers)
    - [Need help?](#need-help)
    - [Found a bug?](#found-a-bug)
- [Contributing to the project](#contributing-to-the-project)
- [Development, meeting minutes, roadmap and more.](#development-meeting-minutes-roadmap-and-more)


# Demo

Do you want to see directives in action? Visit http://angular-ui.github.io/bootstrap/!

# Installation

Installation is easy as UI Bootstrap has minimal dependencies - only the AngularJS and Twitter Bootstrap's CSS are required.
Note: Since version 0.13.0, UI Bootstrap depends on [ngAnimate](https://docs.angularjs.org/api/ngAnimate) for transitions and animations, such as the accordion, carousel, etc. Include `ngAnimate` in the module dependencies for your app in order to enable animation.

#### Install with NPM

```sh
$ npm install angular-ui-bootstrap
```

This will install AngularJS and Bootstrap NPM packages.

#### Install with Bower
```sh
$ bower install angular-bootstrap
```

Note: do not install 'angular-ui-bootstrap'.  A separate repository - [bootstrap-bower](https://github.com/angular-ui/bootstrap-bower) - hosts the compiled javascript file and bower.json.

#### Install with NuGet
To install AngularJS UI Bootstrap, run the following command in the Package Manager Console

```sh
PM> Install-Package Angular.UI.Bootstrap
```

#### Custom build

Head over to http://angular-ui.github.io/bootstrap/ and hit the *Custom build* button to create your own custom UI Bootstrap build, just the way you like it.

#### Manual download

After downloading dependencies (or better yet, referencing them from your favorite CDN) you need to download build version of this project. All the files and their purposes are described here:
https://github.com/angular-ui/bootstrap/tree/gh-pages#build-files
Don't worry, if you are not sure which file to take, opt for `ui-bootstrap-tpls-[version].min.js`.

### Adding dependency to your project

When you are done downloading all the dependencies and project files the only remaining part is to add dependencies on the `ui.bootstrap` AngularJS module:

```js
angular.module('myModule', ['ui.bootstrap']);
```

If you're a Browserify or Webpack user, you can do:

```js
var uibs = require('angular-ui-bootstrap');

angular.module('myModule', [uibs]);
```

# Support

## FAQ

https://github.com/angular-ui/bootstrap/wiki/FAQ

## Supported browsers

Directives from this repository are automatically tested with the following browsers:
* Chrome (stable and canary channel)
* Firefox
* IE 9 and 10
* Opera
* Safari

Modern mobile browsers should work without problems.


## Need help?
Need help using UI Bootstrap?

* Live help in the IRC (`#angularjs` channel at the `freenode` network). Use this [webchat](https://webchat.freenode.net/) or your own IRC client.
* Ask a question in [StackOverflow](http://stackoverflow.com/) under the [angular-ui-bootstrap](http://stackoverflow.com/questions/tagged/angular-ui-bootstrap) tag.

**Please do not create new issues in this repository to ask questions about using UI Bootstrap**

## Found a bug?
Please take a look at [CONTRIBUTING.md](CONTRIBUTING.md#you-think-youve-found-a-bug) and submit your issue [here](https://github.com/angular-ui/bootstrap/issues/new).


----


# Contributing to the project

We are always looking for the quality contributions! Please check the [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution guidelines.

# Development, meeting minutes, roadmap and more.

Head over to the [Wiki](https://github.com/angular-ui/bootstrap/wiki) for notes on development for UI Bootstrap, meeting minutes from the UI Bootstrap team, roadmap plans, project philosophy and more.
ocLazyLoad [![Build Status](https://travis-ci.org/ocombe/ocLazyLoad.svg)](https://travis-ci.org/ocombe/ocLazyLoad)
==========

Load modules on demand (lazy load) in AngularJS

## Key features
- Dependencies are automatically loaded
- Debugger friendly (no eval code)
- The ability to mix normal boot and load on demand
- Load via the service or the directive
- Use the embedded async loader or use your own (requireJS, ...)
- Load js (angular or not) / css / templates files
- Compatible with AngularJS 1.2.x and 1.3.x

## Usage
- Put ocLazyLoad.js into you project

- Add the module ```oc.lazyLoad``` to your application (you can install it with `bower install oclazyload` or `npm install oclazyload`)

- Load on demand:
With $ocLazyLoad you can load angular modules, but if you want to load controllers / services / filters / ... without defining a new module it's entirely possible, just use the name an existing module (your app name for example).
There are multiple ways to use `$ocLazyLoad` to load your files, just choose the one that fits you the best.

###### More examples / tutorials / articles
You can find three basic examples in the example folder. If you need more, check out these links:
- Lazy loading with requirejs, ocLazyLoad and ui-router: [using the templateProvider](http://plnkr.co/edit/OGvi01?p=preview) / [using the uiRouterDecorator](http://plnkr.co/edit/6CLDsz?p=preview) - by @gilbox
- Lazy Loading ui-router states with requirejs, ocLazyLoad and ui-router-extras futureStates, [part 1](http://bardo.io/posts/oclazyload-future-states/) / [part 2](http://bardo.io/posts/ng-deferred-bootstrap-like-with-oclazyload/) - by @kbdaitch
- Lazy loading Angular modules with ocLazyLoad, [part 1](https://egghead.io/lessons/angularjs-lazy-loading-angular-modules-with-oclazyload) / [part 2](https://egghead.io/lessons/angularjs-lazy-loading-modules-with-ui-router-and-oclazyload) / [part 3](https://egghead.io/lessons/angularjs-simple-lazy-loaded-angular-module-syntax-with-oclazyload) / [part 4](https://egghead.io/lessons/angularjs-lazy-loading-non-angular-libraries-with-oclazyload) - An AngularJS lesson by [@johnlindquist](https://twitter.com/johnlindquist) on [egghead.io](https://egghead.io/)

### Service
You can include `$ocLazyLoad` and use the function `load` which returns a promise. It supports a single dependency (object) or multiple dependencies (array of objects).

Load a single module with one file:
```js
$ocLazyLoad.load({
	name: 'TestModule',
	files: ['testModule.js']
});
```

Load a single module with multiple files:
```js
$ocLazyLoad.load({
	name: 'TestModule',
	files: ['testModule.js', 'testModuleCtrl.js', 'testModuleService.js']
});
```

Load multiple modules with one or more files:
```js
$ocLazyLoad.load([{
	name: 'TestModule',
	files: ['testModule.js', 'testModuleCtrl.js', 'testModuleService.js']
},{
    name: 'AnotherModule',
    files: ['anotherModule.js']
}]);
```

You can also load external libs (not angular):
```js
$ocLazyLoad.load([{
	name: 'TestModule',
	files: ['testModule.js', 'bower_components/bootstrap/dist/js/bootstrap.js']
},{
    name: 'AnotherModule',
    files: ['anotherModule.js']
}]);
```

If you don't load angular files at all, you don't need to define the module name:
```js
$ocLazyLoad.load([{
	files: ['bower_components/bootstrap/dist/js/bootstrap.js']
}]);
```

In fact, if you don't load an angular module, why bother with an object having a single `files` property? You can just pass the urls.
Single file:
```js
$ocLazyLoad.load('bower_components/bootstrap/dist/js/bootstrap.js');
```

You can also load css and template files:
```js
$ocLazyLoad.load([
	'bower_components/bootstrap/dist/js/bootstrap.js',
	'bower_components/bootstrap/dist/css/bootstrap.css',
	'partials/template1.html'
]);
```

If you want to load templates, the template file should be an html (or htm) file with regular [script templates](https://docs.angularjs.org/api/ng/directive/script). It looks like this:
```html
<script type="text/ng-template" id="/tpl.html">
  Content of the template.
</script>
```

You can put more than one template script in your template file, just make sure to use different ids:
```html
<script type="text/ng-template" id="/tpl1.html">
  Content of the first template.
</script>

<script type="text/ng-template" id="/tpl2.html">
  Content of the second template.
</script>
```

There are two ways to define config options for the load function. You can use a second optional parameter that will define configs for all the modules that you will load, or you can define optional parameters to each module.
For example, these are equivalent:
```js
$ocLazyLoad.load([{
	name: 'TestModule',
	files: ['testModule.js', 'bower_components/bootstrap/dist/js/bootstrap.js'],
	cache: false
},{
    name: 'AnotherModule',
    files: ['anotherModule.js'],
    cache: false
}]);
```
And
```js
$ocLazyLoad.load([{
	name: 'TestModule',
	files: ['testModule.js', 'bower_components/bootstrap/dist/js/bootstrap.js']
},{
    name: 'AnotherModule',
    files: ['anotherModule.js']
}],
{cache: false});
```

If you load a template with the native template loader, you can use any parameter from the $http service (check: https://docs.angularjs.org/api/ng/service/$http#usage).
```js
$ocLazyLoad.load(
	['partials/template1.html', 'partials/template2.html'],
	{cache: false, timeout: 5000}
);
```

The existing parameters that you can use are `cache`, `reconfig`, `rerun`, `serie` and `insertBefore`.
The parameter `cache: false` works for all native loaders (**all requests are cached by default**):

```js
$ocLazyLoad.load({
	name: 'TestModule',
	cache: false,
	files: ['testModule.js', 'bower_components/bootstrap/dist/js/bootstrap.js']
});
```

By default, if you reload a module, the config block won't be invoked again (because often it will lead to unexpected results). But if you really need to execute the config function again, use the parameter `reconfig: true`:
```js
$ocLazyLoad.load({
	name: 'TestModule',
	reconfig: true,
	files: ['testModule.js', 'bower_components/bootstrap/dist/js/bootstrap.js']
});
```

The same problem might happen with run blocks, use `rerun: true` to rerun the run blocks:
```js
$ocLazyLoad.load({
	name: 'TestModule',
	rerun: true,
	files: ['testModule.js', 'bower_components/bootstrap/dist/js/bootstrap.js']
});
```

By default the native loaders will load your files in parallel. If you need to load your files in serie, you can use `serie: true`:
```js
$ocLazyLoad.load({
	name: 'mgcrea.ngStrap',
	serie: true,
	files: [
		'bower_components/angular-strap/dist/angular-strap.js',
		'bower_components/angular-strap/dist/angular-strap.tpl.js'
	]
});
```

The files, by default, will be inserted before the last child of the `head` element. You can override this by using `insertBefore: 'cssSelector'`:
```js
$ocLazyLoad.load({
	name: 'TestModule',
	insertBefore: '#load_css_before',
	files: ['bower_components/bootstrap/dist/css/bootstrap.css']
});
```

### Directive
The directive usage is very similar to the service. The main interest here is that the content will be included and compiled once your modules have been loaded.
This means that you can use directives that will be lazy loaded inside the oc-lazy-load directive.

Use the same parameters as a service:
```html
<div oc-lazy-load="{name: 'TestModule', files: ['js/testModule.js', 'partials/lazyLoadTemplate.html']}">
	// Use a directive from TestModule
	<test-directive></test-directive>
</div>
```

You can use variables to store parameters:
```js
$scope.lazyLoadParams = {
	name: 'TestModule',
	files: [
		'js/testModule.js',
		'partials/lazyLoadTemplate.html'
	]
};
```
```html
<div oc-lazy-load="lazyLoadParams"></div>
```

### Bonus: Use dependency injection
As a convenience you can also load dependencies by placing a module definition in the dependency injection block of your module. This will only work for lazy loaded modules:
```js
angular.module('MyModule', ['pascalprecht.translate', {
		name: 'TestModule',
		files: ['/components/TestModule/TestModule.js']
	}, {
		files: [
			'/components/bootstrap/css/bootstrap.css',
			'/components/bootstrap/js/bootstrap.js'
		]
	}]
);
```


## Configuration
You can configure the service provider ```$ocLazyLoadProvider``` in the config function of your application:

```js
angular.module('app').config(['$ocLazyLoadProvider', function($ocLazyLoadProvider) {
	$ocLazyLoadProvider.config({
		...
	});
}]);
```

The options are:
- `jsLoader`: You can use your own async loader. The one provided with $ocLazyLoad is based on $script.js, but you can use requireJS or any other async loader that works with the following syntax:
	```js
	$ocLazyLoadProvider.config({
		jsLoader: function([Array of files], callback, params);
	});
	```

- `cssLoader`: You can also define your own css async loader. The rules and syntax are the same as jsLoader.
	```js
	$ocLazyLoadProvider.config({
		cssLoader: function([Array of files], callback, params);
	});
	```

- `templatesLoader`: You can use your template loader. It's similar to the `jsLoader` but it uses an optional config parameter
	```js
	$ocLazyLoadProvider.config({
		templatesLoader: function([Array of files], callback, params);
	});
	```

- `debug`: $ocLazyLoad returns a promise that can be rejected if there is an error. If you set debug to true, $ocLazyLoad will also log all errors to the console.
	```js
	$ocLazyLoadProvider.config({
		debug: true
	});
	```

- `events`: $ocLazyLoad can broadcast an event when you load a module, a component and a file (js/css/template). It is disabled by default, set events to true to activate it. The events are `ocLazyLoad.moduleLoaded`, `ocLazyLoad.moduleReloaded`, `ocLazyLoad.componentLoaded`, `ocLazyLoad.fileLoaded`.
	```js
	$ocLazyLoadProvider.config({
		events: true
	});
	```
	```js
	$scope.$on('ocLazyLoad.moduleLoaded', function(e, module) {
		console.log('module loaded', module);
	});
	```

- `modules`: predefine the configuration of your modules for a later use
	```js
	$ocLazyLoadProvider.config({
	    modules: [{
	        name: 'TestModule',
	        files: ['js/TestModule.js']
	    }]
	});
	```
	```js
	$ocLazyLoad.load('TestModule');
	```


## Works well with your router
`$ocLazyLoad` works well with routers and especially [ui-router](https://github.com/angular-ui/ui-router). Since it returns a promise, use the [resolve property](https://github.com/angular-ui/ui-router/wiki#resolve) to make sure that your components are loaded before the view is resolved:
```js
$stateProvider.state('index', {
	url: "/", // root route
	views: {
		"lazyLoadView": {
			controller: 'AppCtrl', // This view will use AppCtrl loaded below in the resolve
			templateUrl: 'partials/main.html'
		}
	},
	resolve: { // Any property in resolve should return a promise and is executed before the view is loaded
		loadMyCtrl: ['$ocLazyLoad', function($ocLazyLoad) {
			// you can lazy load files for an existing module
             return $ocLazyLoad.load({
                name: 'app',
                files: ['js/AppCtrl.js']
             });
		}]
	}
});
```

If you have nested views, make sure to include the resolve from the parent to load your components in the right order:
```js
$stateProvider.state('parent', {
	url: "/",
	resolve: {
		loadMyService: ['$ocLazyLoad', function($ocLazyLoad) {
             return $ocLazyLoad.load({
                name: 'app',
                files: ['js/ServiceTest.js']
             });
		}]
	}
})
.state('parent.child', {
    resolve: {
        test: ['loadMyService', '$ServiceTest', function(loadMyService, $ServiceTest) {
            // you can use your service
            $ServiceTest.doSomething();
        }]
    }
});
```

It also works for sibling resolves:
```js
$stateProvider.state('index', {
	url: "/",
	resolve: {
		loadMyService: ['$ocLazyLoad', function($ocLazyLoad) {
             return $ocLazyLoad.load({
                name: 'app',
                files: ['js/ServiceTest.js']
             });
		}],
        test: ['loadMyService', '$serviceTest', function(loadMyService, $serviceTest) {
            // you can use your service
            $serviceTest.doSomething();
        }]
    }
});
```

Of course, if you want to use the loaded files immediately, you don't need to define two resolves, you can also use the injector (it works anywhere, not just in the router):
```js
$stateProvider.state('index', {
	url: "/",
	resolve: {
		loadMyService: ['$ocLazyLoad', '$injector', function($ocLazyLoad, $injector) {
             return $ocLazyLoad.load({
                name: 'app',
                files: ['js/ServiceTest.js']
             }).then(function() {
                var $serviceTest = $injector.get("$serviceTest");
                $serviceTest.doSomething();
             });
		}]
    }
});
```


##Other functions
`$ocLazyLoad` provides a few other functions that might help you in a few specific cases:

- `setModuleConfig(moduleConfig)`: Lets you define a module config object

- `getModuleConfig(moduleName)`: Lets you get a module config object

- `getModules()`: Returns the list of loaded modules

- `isLoaded(modulesNames)`: Lets you check if a module (or a list of modules) has been loaded into Angular or not


##Contribute
If you want to get started and the docs are not enough, see the examples in the 'examples' folder!

If you want to contribute, it would be really awesome to add some tests, or more examples :)
Use `bower install` to download the libraries used in this example.# angular-toggle-switch [![Build Status](https://travis-ci.org/cgarvis/angular-toggle-switch.png?branch=master)](https://travis-ci.org/cgarvis/angular-toggle-switch)

Toggle Switches for AngularJS.  Based off [Bootstrap switch](http://www.larentis.eu/switch/) by Matt Lartentis.

## Demo
[cgarvis.github.io/angular-toggle-switch](http://cgarvis.github.io/angular-toggle-switch)

## Installation

Download [angular-toggle-switch.min.js](https://raw.github.com/cgarvis/angular-toggle-switch/master/angular-toggle-switch.min.js) or install with bower.

```bash
$ bower install angular-toggle-switch --save
```

Load `angular-toggle-switch.min.js` then add the `toggle-switch` module to your Angular App.

```javascript
angular.module('app', ['toggle-switch']);
```

See [demo](http://cgarvis.github.io/angular-toggle-switch) for usage.

## Development

Testing is done using Karma Test Runner.

```bash
$ grunt test
```

## Release

```bash
$ grunt release
```
# bower-angular-touch

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngTouch).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-touch
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-touch/angular-touch.js"></script>
```

And add `ngTouch` as a dependency for your app:

```javascript
angular.module('myApp', ['ngTouch']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngTouch).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# bower-angular-route

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngRoute).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-route
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-route/angular-route.js"></script>
```

And add `ngRoute` as a dependency for your app:

```javascript
angular.module('myApp', ['ngRoute']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngRoute).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# bower-angular-cookies

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngCookies).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-cookies
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-cookies/angular-cookies.js"></script>
```

And add `ngCookies` as a dependency for your app:

```javascript
angular.module('myApp', ['ngCookies']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngCookies).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
