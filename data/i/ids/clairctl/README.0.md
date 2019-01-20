See https://github.com/samneirinck/posh-dockerThese files under this directory are for reference only. 

They are used by Jenkins for CI runs.# client-go

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
This repository holds supplemental Go packages for low-level interactions with the operating system.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
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
This repository provides supplementary Go time packages.
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

# go-colorable

[![Godoc Reference](https://godoc.org/github.com/mattn/go-colorable?status.svg)](http://godoc.org/github.com/mattn/go-colorable)
[![Build Status](https://travis-ci.org/mattn/go-colorable.svg?branch=master)](https://travis-ci.org/mattn/go-colorable)
[![Coverage Status](https://coveralls.io/repos/github/mattn/go-colorable/badge.svg?branch=master)](https://coveralls.io/github/mattn/go-colorable?branch=master)
[![Go Report Card](https://goreportcard.com/badge/mattn/go-colorable)](https://goreportcard.com/report/mattn/go-colorable)

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
# go-shellwords

[![Coverage Status](https://coveralls.io/repos/mattn/go-shellwords/badge.png?branch=master)](https://coveralls.io/r/mattn/go-shellwords?branch=master)
[![Build Status](https://travis-ci.org/mattn/go-shellwords.svg?branch=master)](https://travis-ci.org/mattn/go-shellwords)

Parse line as shell words.

## Usage

```go
args, err := shellwords.Parse("./foo --bar=baz")
// args should be ["./foo", "--bar=baz"]
```

```go
os.Setenv("FOO", "bar")
p := shellwords.NewParser()
p.ParseEnv = true
args, err := p.Parse("./foo $FOO")
// args should be ["./foo", "bar"]
```

```go
p := shellwords.NewParser()
p.ParseBacktick = true
args, err := p.Parse("./foo `echo $SHELL`")
// args should be ["./foo", "/bin/bash"]
```

```go
shellwords.ParseBacktick = true
p := shellwords.NewParser()
args, err := p.Parse("./foo `echo $SHELL`")
// args should be ["./foo", "/bin/bash"]
```

# Thanks

This is based on cpan module [Parse::CommandLine](https://metacpan.org/pod/Parse::CommandLine).

# License

under the MIT License: http://mattn.mit-license.org/2014

# Author

Yasuhiro Matsumoto (a.k.a mattn)
# go-isatty

[![Godoc Reference](https://godoc.org/github.com/mattn/go-isatty?status.svg)](http://godoc.org/github.com/mattn/go-isatty)
[![Build Status](https://travis-ci.org/mattn/go-isatty.svg?branch=master)](https://travis-ci.org/mattn/go-isatty)
[![Coverage Status](https://coveralls.io/repos/github/mattn/go-isatty/badge.svg?branch=master)](https://coveralls.io/github/mattn/go-isatty?branch=master)
[![Go Report Card](https://goreportcard.com/badge/mattn/go-isatty)](https://goreportcard.com/report/mattn/go-isatty)

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
	} else if isatty.IsCygwinTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Cygwin/MSYS2 Terminal")
	} else {
		fmt.Println("Is Not Terminal")
	}
}
```

## Installation

```
$ go get github.com/mattn/go-isatty
```

## License

MIT

## Author

Yasuhiro Matsumoto (a.k.a mattn)

## Thanks

* k-takata: base idea for IsCygwinTerminal

    https://github.com/k-takata/go-iscygpty
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
Gotty is a library written in Go that determines and reads termcap database
files to produce an interface for interacting with the capabilities of a
terminal.
See the godoc documentation or the source code for more information about
function usage.
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
  - Handle unique idiosynchracies of codecs e.g. 
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
  -rt="": tags for go run
  -t="": build tag to put in file
  -u=false: Use unsafe, e.g. to avoid unnecessary allocation on []byte->string
  -x=false: keep temp file

% codecgen -o values_codecgen.go values.go values2.go moretypedefs.go
```

Please see the [blog article](http://ugorji.net/blog/go-codecgen)
for more information on how to use the tool.

# go-oidc

[![GoDoc](https://godoc.org/github.com/coreos/go-oidc?status.svg)](https://godoc.org/github.com/coreos/go-oidc)
[![Build Status](https://travis-ci.org/coreos/go-oidc.png?branch=master)](https://travis-ci.org/coreos/go-oidc)

go-oidc provides a comprehensive collection of golang libraries for other projects to implement [OpenID Connect (OIDC)][oidc] server and client components.

[oidc]: http://openid.net/connect

## package documentation

- [github.com/coreos/go-oidc/oidc](http://godoc.org/github.com/coreos/go-oidc/oidc) - OIDC client- and server-related components
- [github.com/coreos/go-oidc/oauth2](http://godoc.org/github.com/coreos/go-oidc/oauth2) - OAuth2-specific code needed by the OIDC components
- [github.com/coreos/go-oidc/jose](http://godoc.org/github.com/coreos/go-oidc/jose) - Javascript Object Signing and Encryption (JOSE) object ([JWS](https://tools.ietf.org/html/draft-ietf-jose-json-web-signature-41), [JWK](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41)) generation, validation and serialization
- [github.com/coreos/go-oidc/key](http://godoc.org/github.com/coreos/go-oidc/key) - RSA key management for OIDC components
a collection of go utility packages

[![Build Status](https://semaphoreci.com/api/v1/projects/14b3f261-22c2-4f56-b1ff-f23f4aa03f5c/411991/badge.svg)](https://semaphoreci.com/coreos/pkg) [![Godoc](http://img.shields.io/badge/godoc-reference-blue.svg?style=flat)](https://godoc.org/github.com/coreos/pkg)
# capnslog, the CoreOS logging package

There are far too many logging packages out there, with varying degrees of licenses, far too many features (colorization, all sorts of log frameworks) or are just a pain to use (lack of `Fatalln()`?).
capnslog provides a simple but consistent logging interface suitable for all kinds of projects.

### Design Principles

##### `package main` is the place where logging gets turned on and routed

A library should not touch log options, only generate log entries. Libraries are silent until main lets them speak.

##### All log options are runtime-configurable. 

Still the job of `main` to expose these configurations. `main` may delegate this to, say, a configuration webhook, but does so explicitly. 

##### There is one log object per package. It is registered under its repository and package name.

`main` activates logging for its repository and any dependency repositories it would also like to have output in its logstream. `main` also dictates at which level each subpackage logs.

##### There is *one* output stream, and it is an `io.Writer` composed with a formatter.

Splitting streams is probably not the job of your program, but rather, your log aggregation framework. If you must split output streams, again, `main` configures this and you can write a very simple two-output struct that satisfies io.Writer.

Fancy colorful formatting and JSON output are beyond the scope of a basic logging framework -- they're application/log-collector dependant. These are, at best, provided as options, but more likely, provided by your application.

##### Log objects are an interface

An object knows best how to print itself. Log objects can collect more interesting metadata if they wish, however, because text isn't going away anytime soon, they must all be marshalable to text. The simplest log object is a string, which returns itself. If you wish to do more fancy tricks for printing your log objects, see also JSON output -- introspect and write a formatter which can handle your advanced log interface. Making strings is the only thing guaranteed.

##### Log levels have specific meanings:

  * Critical: Unrecoverable. Must fail.
  * Error: Data has been lost, a request has failed for a bad reason, or a required resource has been lost
  * Warning: (Hopefully) Temporary conditions that may cause errors, but may work fine. A replica disappearing (that may reconnect) is a warning.
  * Notice: Normal, but important (uncommon) log information.
  * Info: Normal, working log information, everything is fine, but helpful notices for auditing or common operations.
  * Debug: Everything is still fine, but even common operations may be logged, and less helpful but more quantity of notices.
  * Trace: Anything goes, from logging every function call as part of a common operation, to tracing execution of a query.

httputil
====

Common code for dealing with HTTP.

Includes:

* Code for returning JSON responses.

### Documentation

Visit the docs on [gopkgdoc](http://godoc.org/github.com/coreos/pkg/httputil)

health
====

A simple framework for implementing an HTTP health check endpoint on servers.

Users implement their `health.Checkable` types, and create a `health.Checker`, from which they can get an `http.HandlerFunc` using `health.Checker.MakeHealthHandlerFunc`.

### Documentation

For more details, visit the docs on [gopkgdoc](http://godoc.org/github.com/coreos/pkg/health)

# Clair

[![Build Status](https://api.travis-ci.org/coreos/clair.svg?branch=master "Build Status")](https://travis-ci.org/coreos/clair)
[![Docker Repository on Quay](https://quay.io/repository/coreos/clair/status "Docker Repository on Quay")](https://quay.io/repository/coreos/clair)
[![Go Report Card](https://goreportcard.com/badge/coreos/clair "Go Report Card")](https://goreportcard.com/report/coreos/clair)
[![GoDoc](https://godoc.org/github.com/coreos/clair?status.svg "GoDoc")](https://godoc.org/github.com/coreos/clair)
[![IRC Channel](https://img.shields.io/badge/freenode-%23clair-blue.svg "IRC Channel")](http://webchat.freenode.net/?channels=clair)

**Note**: The `master` branch may be in an *unstable or even broken state* during development.
Please use [releases] instead of the `master` branch in order to get stable binaries.

![Clair Logo](img/Clair_horizontal_color.png)

Clair is an open source project for the static analysis of vulnerabilities in [appc] and [docker] containers.

Vulnerability data is continuously imported from a known set of sources and correlated with the indexed contents of container images in order to produce lists of vulnerabilities that threaten a container.
When vulnerability data changes upstream, the previous state and new state of the vulnerability along with the images they affect can be sent via webhook to a configured endpoint.
All major components can be [customized programmatically] at compile-time without forking the project.

Our goal is to enable a more transparent view of the security of container-based infrastructure.
Thus, the project was named `Clair` after the French term which translates to *clear*, *bright*, *transparent*.

[appc]: https://github.com/appc/spec
[docker]: https://github.com/docker/docker/blob/master/image/spec/v1.md
[customized programmatically]: #customization
[releases]: https://github.com/coreos/clair/releases

## Common Use Cases

### Manual Auditing

You're building an application and want to depend on a third-party container image that you found by searching the internet.
To make sure that you do not knowingly introduce a new vulnerability into your production service, you decide to scan the container for vulnerabilities.
You `docker pull` the container to your development machine and start an instance of Clair.
Once it finishes updating, you use the [local image analysis tool] to analyze the container.
You realize this container is vulnerable to many critical CVEs, so you decide to use another one.

[local image analysis tool]: https://github.com/coreos/clair/tree/master/contrib/analyze-local-images

### Container Registry Integration

Your company has a continuous-integration pipeline and you want to stop deployments if they introduce a dangerous vulnerability.
A developer merges some code into the master branch of your codebase.
The first step of your continuous-integration pipeline automates the testing and building of your container and pushes a new container to your container registry.
Your container registry notifies Clair which causes the download and indexing of the images for the new container.
Clair detects some vulnerabilities and sends a webhook to your continuous deployment tool to prevent this vulnerable build from seeing the light of day.

## Hello Heartbleed

During the first run, Clair will bootstrap its database with vulnerability data from its data sources.
It can take several minutes before the database has been fully populated.

**NOTE:** These setups are not meant for production workloads, but as a quick way to get started.

### Kubernetes

An easy way to run Clair is with Kubernetes 1.2+.
If you are using the [CoreOS Kubernetes single-node instructions][single-node] for Vagrant you will be able to access the Clair's API at http://172.17.4.99:30060/ after following these instructions.

```
git clone https://github.com/coreos/clair
cd clair/contrib/k8s
kubectl create secret generic clairsecret --from-file=./config.yaml
kubectl create -f clair-kubernetes.yaml
```

[single-node]: https://coreos.com/kubernetes/docs/latest/kubernetes-on-vagrant-single.html

### Docker Compose

Another easy way to get an instance of Clair running is to use Docker Compose to run everything locally.
This runs a PostgreSQL database insecurely and locally in a container.
This method should only be used for testing.

```sh
$ curl -L https://raw.githubusercontent.com/coreos/clair/v1.2.5/docker-compose.yml -o $HOME/docker-compose.yml
$ mkdir $HOME/clair_config
$ curl -L https://raw.githubusercontent.com/coreos/clair/v1.2.5/config.example.yaml -o $HOME/clair_config/config.yaml
$ $EDITOR $HOME/clair_config/config.yaml # Edit database source to be postgresql://postgres:password@postgres:5432?sslmode=disable
$ docker-compose -f $HOME/docker-compose.yml up -d
```

Docker Compose may start Clair before Postgres which will raise an error.
If this error is raised, manually execute `docker start clair_clair`.


### Docker

This method assumes you already have a [PostgreSQL 9.4+] database running.
This is the recommended method for production deployments.

[PostgreSQL 9.4+]: http://postgresql.org

```sh
$ mkdir $HOME/clair_config
$ curl -L https://raw.githubusercontent.com/coreos/clair/v1.2.5/config.example.yaml -o $HOME/clair_config/config.yaml
$ $EDITOR $HOME/clair_config/config.yaml # Add the URI for your postgres database
$ docker run -d -p 6060-6061:6060-6061 -v $HOME/clair_config:/config quay.io/coreos/clair:v1.2.5 -config=/config/config.yaml
```

### Source

To build Clair, you need to latest stable version of [Go] and a working [Go environment].
In addition, Clair requires that [bzr], [rpm], and [xz] be available on the system [$PATH].

[Go]: https://github.com/golang/go/releases
[Go environment]: https://golang.org/doc/code.html
[bzr]: http://bazaar.canonical.com/en
[rpm]: http://www.rpm.org
[xz]: http://tukaani.org/xz
[$PATH]: https://en.wikipedia.org/wiki/PATH_(variable)

```sh
$ go get github.com/coreos/clair
$ go install github.com/coreos/clair/cmd/clair
$ $EDITOR config.yaml # Add the URI for your postgres database
$ ./$GOBIN/clair -config=config.yaml
```

## Documentation

The latest stable documentation can be found [on the CoreOS website]. Documentation for the current branch can be found [inside the Documentation directory][docs-dir] at the root of the project's source code.

[on the CoreOS website]: https://coreos.com/clair/docs/latest/
[docs-dir]: /Documentation

### Architecture at a Glance

![Simple Clair Diagram](img/simple_diagram.png)

### Terminology

- *Image* - a tarball of the contents of a container
- *Layer* - an *appc* or *Docker* image that may or maybe not be dependent on another image
- *Detector* - a Go package that identifies the content, *namespaces* and *features* from a *layer*
- *Namespace* - a context around *features* and *vulnerabilities* (e.g. an operating system)
- *Feature* - anything that when present could be an indication of a *vulnerability* (e.g. the presence of a file or an installed software package)
- *Fetcher* - a Go package that tracks an upstream vulnerability database and imports them into Clair

### Vulnerability Analysis

There are two major ways to perform analysis of programs: [Static Analysis] and [Dynamic Analysis].
Clair has been designed to perform *static analysis*; containers never need to be executed.
Rather, the filesystem of the container image is inspected and *features* are indexed into a database.
By indexing the features of an image into the database, images only need to be rescanned when new *detectors* are added.

[Static Analysis]: https://en.wikipedia.org/wiki/Static_program_analysis
[Dynamic Analysis]: https://en.wikipedia.org/wiki/Dynamic_program_analysis

### Default Data Sources

| Data Source                   | Versions                                               | Format |
|-------------------------------|--------------------------------------------------------|--------|
| [Debian Security Bug Tracker] | 6, 7, 8, unstable                                      | [dpkg] |
| [Ubuntu CVE Tracker]          | 12.04, 12.10, 13.04, 14.04, 14.10, 15.04, 15.10, 16.04 | [dpkg] |
| [Red Hat Security Data]       | 5, 6, 7                                                | [rpm]  |

[Debian Security Bug Tracker]: https://security-tracker.debian.org/tracker
[Ubuntu CVE Tracker]: https://launchpad.net/ubuntu-cve-tracker
[Red Hat Security Data]: https://www.redhat.com/security/data/metrics
[dpkg]: https://en.wikipedia.org/wiki/dpkg
[rpm]: http://www.rpm.org


### Customization

The major components of Clair are all programmatically extensible in the same way Go's standard [database/sql] package is extensible.

Custom behavior can be accomplished by creating a package that contains a type that implements an interface declared in Clair and registering that interface in [init()]. To expose the new behavior, unqualified imports to the package must be added in your [main.go], which should then start Clair using `Boot(*config.Config)`.

The following interfaces can have custom implementations registered via [init()] at compile time:

- `Datastore` - the backing storage
- `Notifier` - the means by which endpoints are notified of vulnerability changes
- `Fetcher` - the sources of vulnerability data that is automatically imported
- `MetadataFetcher` - the sources of vulnerability metadata that is automatically added to known vulnerabilities
- `DataDetector` - the means by which contents of an image are detected
- `FeatureDetector` - the means by which features are identified from a layer
- `NamespaceDetector` - the means by which a namespace is identified from a layer

[init()]: https://golang.org/doc/effective_go.html#init
[database/sql]: https://godoc.org/database/sql
[main.go]: https://github.com/coreos/clair/blob/master/cmd/clair/main.go

## Related Links

- [Talk](https://www.youtube.com/watch?v=PA3oBAgjnkU) and [Slides](https://docs.google.com/presentation/d/1toUKgqLyy1b-pZlDgxONLduiLmt2yaLR0GliBB7b3L0/pub?start=false&loop=false&slide=id.p) @ ContainerDays NYC 2015
- [Quay](https://quay.io): the first container registry to integrate with Clair
- [Dockyard](https://github.com/containerops/dockyard): an open source container registry with Clair integration
check_openvz_mirror_with_clair
==============================

**check_openvz_mirror_with_clair** - little tool for add templates from OpenVZ 6 mirror to [clair](https://github.com/coreos/clair) for vulnerability analysis it.

Install
-------

You must have already install and worked [clair](https://github.com/coreos/clair)

```
export GOPATH=$(pwd)
go get github.com/coreos/clair/contrib/check-openvz-mirror-with-clair
go build github.com/coreos/clair/contrib/check-openvz-mirror-with-clair
```

Usage
-----

```
check_openvz_mirror_with_clair -m MIRROR [ -i ADRESS -p PORT -P PRIORITY --help ]
```

- -m  - link for openvz mirror like https://download.openvz.org/template/precreated/ or path to local mirror with listing file like /home/user/openvzmirror
- -a  - adress to clair API
- -p  - port to clair API
- -P  - the minimum priority of the returned vulnerabilities (default "High")
- -cert  - a PEM encoded certificate file for connect to clair
- -key - a PEM encoded private key file for connect to clair
- -CA - a PEM eoncoded CA's certificate file for connet to clair

Example
--------
```
# Local mirror and clair with  client certificate auth
./check_openvz_mirror_with_clair -m /home/user/Downloads/mirror --cert /home/user/clair/cert/client1.crt --key /home/user/clair/cert/client1.key.insecure --CA /home/user/clair/cert/ca.crt -P LOW
We use:
Clair -  127.0.0.1:6060
We have clair with APIVersion: 1 and EngineVersion: 1
OpenVZ mirror -  /home/user/Downloads/mirror
We have 2 templates on mirror

Try to add  debian-6.0-x86_64-someimage
debian-6.0-x86_64-someimage added success
You can check it via:
curl -s https://127.0.0.1:6060/v1/layers/debian-6.0-x86_64-someimage/vulnerabilities?minimumPriority=Low --cert /home/user/clair/cert/client1.crt --key /home/user/clair/cert/client1.key.insecure --cacert /home/user/clair/cert/ca.crt | python -m json.tool
Detect 169 vulnerabilities for this template

Try to add  debian-7.0-x86_64-someimage
debian-7.0-x86_64-someimage added success
You can check it via:
curl -s https://127.0.0.1:6060/v1/layers/debian-7.0-x86_64-someimage/vulnerabilities?minimumPriority=Low --cert /home/user/clair/cert/client1.crt --key /home/user/clair/cert/client1.key.insecure --cacert /home/user/clair/cert/ca.crt | python -m json.tool
Detect 146 vulnerabilities for this template


# Remote mirror 
./check_openvz_mirror_with_clair -m http://mirror.yandex.ru/mirrors/download.openvz.org/template/precreated/ -a 127.0.0.1 -p 6060 -P Low
We use:
Clair -  127.0.0.1:6060
OpenVZ mirror -  http://mirror.yandex.ru/mirrors/download.openvz.org/template/precreated/
We have 45 templates on mirror

Try to add  centos-5-x86_64-devel
centos-5-x86_64-devel added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-5-x86_64-devel/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 0 vulnerabilities for this template

Try to add  centos-5-x86_64
centos-5-x86_64 added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-5-x86_64/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 0 vulnerabilities for this template

Try to add  centos-5-x86-devel
centos-5-x86-devel added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-5-x86-devel/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 0 vulnerabilities for this template

Try to add  centos-5-x86
centos-5-x86 added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-5-x86/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 0 vulnerabilities for this template

Try to add  centos-6-x86_64-devel
centos-6-x86_64-devel added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-6-x86_64-devel/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 3 vulnerabilities for this template

Try to add  centos-6-x86_64-minimal
centos-6-x86_64-minimal added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-6-x86_64-minimal/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 1 vulnerabilities for this template

Try to add  centos-6-x86_64
centos-6-x86_64 added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-6-x86_64/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 2 vulnerabilities for this template

Try to add  centos-6-x86-devel
centos-6-x86-devel added success
You can check it via:
curl -s http://127.0.0.1:6060/v1/layers/centos-6-x86-devel/vulnerabilities?minimumPriority=Low | python -m json.tool
Detect 3 vulnerabilities for this template
...

```

# Analyze local images

This is a basic tool that allow you to analyze your local Docker images with Clair.
It is intended to let everyone discover Clair and offer awareness around containers' security.
There are absolutely no guarantees and it only uses a minimal subset of Clair's features.

## Install

To install the tool, simply run the following command, with a proper Go environment:

    go get -u github.com/coreos/clair/contrib/analyze-local-images

You also need a working Clair instance. To learn how to run Clair, take a look at the [README](https://github.com/coreos/clair/blob/master/README.md). You then should wait for its initial vulnerability update to complete, which may take some time.

# Usage

If you are running Clair locally (ie. compiled or local Docker),

```
analyze-local-images <Docker Image ID>
```

Or, If you run Clair remotely (ie. boot2docker),

```
analyze-local-images -endpoint "http://<CLAIR-IP-ADDRESS>:6060" -my-address "<MY-IP-ADDRESS>" <Docker Image ID>
```

Clair needs access to the image files. If you run Clair locally, this tool will store the files in the system's temporary folder and Clair will find them there. It means if Clair is running in Docker, the host's temporary folder must be mounted in the Clair's container. If you run Clair remotely, this tool will run a small HTTP server to let Clair downloading them. It listens on the port 9279 and allows a single host: Clair's IP address, extracted from the `-endpoint` parameter. The `my-address` parameters defines the IP address of the HTTP server that Clair will use to download the images. With boot2docker, these parameters would be `-endpoint "http://192.168.99.100:6060" -my-address "192.168.99.1"`.

As it runs an HTTP server and not an HTTP**S** one, be sure to **not** expose sensitive data and container images.
# go-systemd

[![Build Status](https://travis-ci.org/coreos/go-systemd.png?branch=master)](https://travis-ci.org/coreos/go-systemd)
[![godoc](https://godoc.org/github.com/coreos/go-systemd?status.svg)](http://godoc.org/github.com/coreos/go-systemd)

Go bindings to systemd. The project has several packages:

- `activation` - for writing and using socket activation from Go
- `dbus` - for starting/stopping/inspecting running services and units
- `journal` - for writing to systemd's logging service, journald
- `sdjournal` - for reading from journald by wrapping its C API
- `machine1` - for registering machines/containers with systemd
- `unit` - for (de)serialization and comparison of unit files

## Socket Activation

An example HTTP server using socket activation can be quickly set up by following this README on a Linux machine running systemd:

https://github.com/coreos/go-systemd/tree/master/examples/activation/httpserver

## Journal

Using the pure-Go `journal` package you can submit journal entries directly to systemd's journal, taking advantage of features like indexed key/value pairs for each log entry.
The `sdjournal` package provides read access to the journal by wrapping around journald's native C API; consequently it requires cgo and the journal headers to be available.

## D-Bus

The `dbus` package connects to the [systemd D-Bus API](http://www.freedesktop.org/wiki/Software/systemd/dbus/) and lets you start, stop and introspect systemd units. The API docs are here:

http://godoc.org/github.com/coreos/go-systemd/dbus

### Debugging

Create `/etc/dbus-1/system-local.conf` that looks like this:

```
<!DOCTYPE busconfig PUBLIC
"-//freedesktop//DTD D-Bus Bus Configuration 1.0//EN"
"http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>
    <policy user="root">
        <allow eavesdrop="true"/>
        <allow eavesdrop="true" send_destination="*"/>
    </policy>
</busconfig>
```

## machined

The `machine1` package allows interaction with the [systemd machined D-Bus API](http://www.freedesktop.org/wiki/Software/systemd/machined/).

## Units

The `unit` package provides various functions for working with [systemd unit files](http://www.freedesktop.org/software/systemd/man/systemd.unit.html).
## socket activated http server

This is a simple example of using socket activation with systemd to serve a
simple HTTP server on http://127.0.0.1:8076

To try it out `go get` the httpserver and run it under the systemd-activate helper

```
export GOPATH=`pwd`
go get github.com/coreos/go-systemd/examples/activation/httpserver
sudo /usr/lib/systemd/systemd-activate -l 127.0.0.1:8076 ./bin/httpserver
```

Then curl the URL and you will notice that it starts up:

```
curl 127.0.0.1:8076
hello socket activated world!
```
# go-ansiterm

This is a cross platform Ansi Terminal Emulation library.  It reads a stream of Ansi characters and produces the appropriate function calls.  The results of the function calls are platform dependent.

For example the parser might receive "ESC, [, A" as a stream of three characters.  This is the code for Cursor Up (http://www.vt100.net/docs/vt510-rm/CUU).  The parser then calls the cursor up function (CUU()) on an event handler.  The event handler determines what platform specific work must be done to cause the cursor to move up one position.

The parser (parser.go) is a partial implementation of this state machine (http://vt100.net/emu/vt500_parser.png).  There are also two event handler implementations, one for tests (test_event_handler.go) to validate that the expected events are being produced and called, the other is a Windows implementation (winterm/win_event_handler.go).

See parser_test.go for examples exercising the state machine and generating appropriate function calls.

-----
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
clockwork
=========

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

Inspired by @wickman's [threaded fake clock](https://gist.github.com/wickman/3840816), and the [Golang playground](http://blog.golang.org/playground#Faking time)
sftp
----

The `sftp` package provides support for file system operations on remote ssh servers using the SFTP subsystem.

[![UNIX Build Status](https://travis-ci.org/pkg/sftp.svg?branch=master)](https://travis-ci.org/pkg/sftp) [![GoDoc](http://godoc.org/github.com/pkg/sftp?status.svg)](http://godoc.org/github.com/pkg/sftp)

usage and examples
------------------

See [godoc.org/github.com/pkg/sftp](http://godoc.org/github.com/pkg/sftp) for examples and usage.

The basic operation of the package mirrors the facilities of the [os](http://golang.org/pkg/os) package.

The Walker interface for directory traversal is heavily inspired by Keith Rarick's [fs](http://godoc.org/github.com/kr/fs) package.

roadmap
-------

 * There is way too much duplication in the Client methods. If there was an unmarshal(interface{}) method this would reduce a heap of the duplication.

contributing
------------

We welcome pull requests, bug fixes and issue reports.

Before proposing a large change, first please discuss your change by raising an issue.
Example SFTP server implementation
===

In order to use this example you will need an RSA key.

On linux-like systems with openssh installed, you can use the command:

```
ssh-keygen -t rsa -f id_rsa
```

Then you will be able to run the sftp-server command in the current directory.
# errors [![Travis-CI](https://travis-ci.org/pkg/errors.svg)](https://travis-ci.org/pkg/errors) [![AppVeyor](https://ci.appveyor.com/api/projects/status/b98mptawhudj53ep/branch/master?svg=true)](https://ci.appveyor.com/project/davecheney/errors/branch/master) [![GoDoc](https://godoc.org/github.com/pkg/errors?status.svg)](http://godoc.org/github.com/pkg/errors) [![Report card](https://goreportcard.com/badge/github.com/pkg/errors)](https://goreportcard.com/report/github.com/pkg/errors)

Package errors provides simple error handling primitives.

`go get github.com/pkg/errors`

The traditional error handling idiom in Go is roughly akin to
```go
if err != nil {
        return err
}
```
which applied recursively up the call stack results in error reports without context or debugging information. The errors package allows programmers to add context to the failure path in their code in a way that does not destroy the original value of the error.

## Adding context to an error

The errors.Wrap function returns a new error that adds context to the original error. For example
```go
_, err := ioutil.ReadAll(r)
if err != nil {
        return errors.Wrap(err, "read failed")
}
```
## Retrieving the cause of an error

Using `errors.Wrap` constructs a stack of errors, adding context to the preceding error. Depending on the nature of the error it may be necessary to reverse the operation of errors.Wrap to retrieve the original error for inspection. Any error value which implements this interface can be inspected by `errors.Cause`.
```go
type causer interface {
        Cause() error
}
```
`errors.Cause` will recursively retrieve the topmost error which does not implement `causer`, which is assumed to be the original cause. For example:
```go
switch err := errors.Cause(err).(type) {
case *MyError:
        // handle specifically
default:
        // unknown error
}
```

[Read the package documentation for more information](https://godoc.org/github.com/pkg/errors).

## Contributing

We welcome pull requests, bug fixes and issue reports. With that said, the bar for adding new symbols to this package is intentionally set high.

Before proposing a change, please discuss your change by raising an issue.

## Licence

BSD-2-Clause
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
# mousetrap

mousetrap is a tiny library that answers a single question.

On a Windows machine, was the process invoked by someone double clicking on
the executable file while browsing in explorer?

### Motivation

Windows developers unfamiliar with command line tools will often "double-click"
the executable for a tool. Because most CLI tools print the help and then exit
when invoked without arguments, this is often very frustrating for those users.

mousetrap provides a way to detect these invocations so that you can provide
more helpful behavior and instructions on how to run the CLI tool. To see what
this looks like, both from an organizational and a technical perspective, see
https://inconshreveable.com/09-09-2014/sweat-the-small-stuff/

### The interface

The library exposes a single interface:

    func StartedByExplorer() (bool)
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
```
f := fuzz.New()
var myInt int
f.Fuzz(&myInt) // myInt gets a random value.
```

You can use it on maps:
```
f := fuzz.New().NilChance(0).NumElements(1, 1)
var myMap map[ComplexKeyType]string
f.Fuzz(&myMap) // myMap will have exactly one element.
```

Customize the chance of getting a nil pointer:
```
f := fuzz.New().NilChance(.5)
var fancyStruct struct {
  A, B, C, D *string
}
f.Fuzz(&fancyStruct) // About half the pointers should be set.
```

You can even customize the randomization completely if needed:
```
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
	- Routing algorithm after [JSR311](http://jsr311.java.net/nonav/releases/1.1/spec/spec.html) that is implemented using (but does **not** accept) regular expressions (See RouterJSR311 which is used by default)
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
- [Example posted on blog](http://ernestmicklei.com/2012/11/go-restful-first-working-example/)
- [Design explained on blog](http://ernestmicklei.com/2012/11/go-restful-api-design/)
- [sourcegraph](https://sourcegraph.com/github.com/emicklei/go-restful)
- [gopkg.in](https://gopkg.in/emicklei/go-restful.v1)
- [showcase: Mora - MongoDB REST Api server](https://github.com/emicklei/mora)

[![Build Status](https://drone.io/github.com/emicklei/go-restful/status.png)](https://drone.io/github.com/emicklei/go-restful/latest)

(c) 2012 - 2015, http://ernestmicklei.com. MIT License

Type ```git shortlog -s``` for a full list of contributors.
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
- Sortable (implements sort.Interface)
- database/sql compatible (sql.Scanner/Valuer)
- encoding/json compatible (json.Marshaler/Unmarshaler)


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

    BenchmarkParseSimple         5000000      328    ns/op    49 B/op   1 allocs/op
    BenchmarkParseComplex        1000000     2105    ns/op   263 B/op   7 allocs/op
    BenchmarkParseAverage        1000000     1301    ns/op   168 B/op   4 allocs/op
    BenchmarkStringSimple       10000000      130    ns/op     5 B/op   1 allocs/op
    BenchmarkStringLarger        5000000      280    ns/op    32 B/op   2 allocs/op
    BenchmarkStringComplex       3000000      512    ns/op    80 B/op   3 allocs/op
    BenchmarkStringAverage       5000000      387    ns/op    47 B/op   2 allocs/op
    BenchmarkValidateSimple    500000000        7.92 ns/op     0 B/op   0 allocs/op
    BenchmarkValidateComplex     2000000      923    ns/op     0 B/op   0 allocs/op
    BenchmarkValidateAverage     5000000      452    ns/op     0 B/op   0 allocs/op
    BenchmarkCompareSimple     100000000       11.2  ns/op     0 B/op   0 allocs/op
    BenchmarkCompareComplex     50000000       40.9  ns/op     0 B/op   0 allocs/op
    BenchmarkCompareAverage     50000000       43.8  ns/op     0 B/op   0 allocs/op
    BenchmarkSort                5000000      436    ns/op   259 B/op   2 allocs/op

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
# go-winio

This repository contains utilities for efficiently performing Win32 IO operations in
Go. Currently, this is focused on accessing named pipes and other file handles, and
for using named pipes as a net transport.

This code relies on IO completion ports to avoid blocking IO on system threads, allowing Go
to reuse the thread to schedule another goroutine. This limits support to Windows Vista and
newer operating systems. This is similar to the implementation of network sockets in Go's net
package.

Please see the LICENSE file for licensing information.

This project has adopted the [Microsoft Open Source Code of
Conduct](https://opensource.microsoft.com/codeofconduct/). For more information
see the [Code of Conduct
FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact
[opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional
questions or comments.

Thanks to natefinch for the inspiration for this library. See https://github.com/natefinch/npipe
for another named pipe implementation.
Overview [![Build Status](https://travis-ci.org/magiconair/properties.svg?branch=master)](https://travis-ci.org/magiconair/properties)
========

#### Current version: 1.7.0

properties is a Go library for reading and writing properties files.

It supports reading from multiple files or URLs and Spring style recursive
property expansion of expressions like `${key}` to their corresponding value.
Value expressions can refer to other keys like in `${key}` or to environment
variables like in `${USER}`.  Filenames can also contain environment variables
like in `/home/${USER}/myapp.properties`.

Properties can be decoded into structs, maps, arrays and values through
struct tags.

Comments and the order of keys are preserved. Comments can be modified
and can be written to the output.

The properties library supports both ISO-8859-1 and UTF-8 encoded data.

Starting from version 1.3.0 the behavior of the MustXXX() functions is
configurable by providing a custom `ErrorHandler` function. The default has
changed from `panic` to `log.Fatal` but this is configurable and custom
error handling functions can be provided. See the package documentation for
details.

Getting Started
---------------

```go
import (
	"flag"
	"github.com/magiconair/properties"
)

func main() {
	p := properties.MustLoadFile("${HOME}/config.properties", properties.UTF8)

	// via getters
	host := p.MustGetString("host")
	port := p.GetInt("port", 8080)

	// or via decode
	type Config struct {
		Host    string        `properties:"host"`
		Port    int           `properties:"port,default=9000"`
		Accept  []string      `properties:"accept,default=image/png;image;gif"`
		Timeout time.Duration `properties:"timeout,default=5s"`
	}
	var cfg Config
	if err := p.Decode(&cfg); err != nil {
		log.Fatal(err)
	}

	// or via flags
	p.MustFlag(flag.CommandLine)

	// or via url
	p = properties.MustLoadURL("http://host/path")
}

```

Read the full documentation on [GoDoc](https://godoc.org/github.com/magiconair/properties)   [![GoDoc](https://godoc.org/github.com/magiconair/properties?status.png)](https://godoc.org/github.com/magiconair/properties)

Installation and Upgrade
------------------------

```
$ go get -u github.com/magiconair/properties
```

License
-------

2 clause BSD license. See [LICENSE](https://github.com/magiconair/properties/blob/master/LICENSE) file for details.

ToDo
----
* Dump contents with passwords and secrets obscured
Instructions
============

Install the package with:

    go get gopkg.in/check.v1
    
Import it with:

    import "gopkg.in/check.v1"

and use _check_ as the package name inside the code.

For more details, visit the project page:

* http://labix.org/gocheck

and the API documentation:

* https://gopkg.in/check.v1
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

## Plugins ##

The `protoc-gen-go/generator` package exposes a plugin interface,
which is used by the gRPC code generation. This interface is not
supported and is subject to incompatible changes without notice.
# Background
Under most circumstances, manually downloading this repository should never
be required.

# Prerequisites
# Base
* [Google Protocol Buffers](https://developers.google.com/protocol-buffers)

## Java
* [Apache Maven](http://maven.apache.org)
* [Prometheus Maven Repository](https://github.com/prometheus/io.prometheus-maven-repository) checked out into ../io.prometheus-maven-repository

## Go
*  [Go](http://golang.org)
*  [goprotobuf](https://code.google.com/p/goprotobuf)

## Ruby
*  [Ruby](https://www.ruby-lang.org)
*  [bundler](https://rubygems.org/gems/bundler)

# Building
    $ make

# Getting Started
  * The Go source code is periodically indexed: [Go Protocol Buffer Model](http://godoc.org/github.com/prometheus/client_model/go).
  * All of the core developers are accessible via the [Prometheus Developers Mailinglist](https://groups.google.com/forum/?fromgroups#!forum/prometheus-developers).
# Prometheus Ruby client model

Data model artifacts for the [Prometheus Ruby client][1].

## Installation

    gem install prometheus-client-model

## Usage

Build the artifacts from the protobuf specification:

    make build

While this Gem's main purpose is to define the Prometheus data types for the
[client][1], it's possible to use it without the client to decode a stream of
delimited protobuf messages:

```ruby
require 'open-uri'
require 'prometheus/client/model'

CONTENT_TYPE = 'application/vnd.google.protobuf; proto=io.prometheus.client.MetricFamily; encoding=delimited'

stream = open('http://localhost:9090/metrics', 'Accept' => CONTENT_TYPE).read
while family = Prometheus::Client::MetricFamily.read_delimited(stream)
  puts family
end
```

[1]: https://github.com/prometheus/client_ruby
# procfs

This procfs package provides functions to retrieve system, kernel and process
metrics from the pseudo-filesystem proc.

*WARNING*: This package is a work in progress. Its API may still break in
backwards-incompatible ways without warnings. Use it at your own risk.

[![GoDoc](https://godoc.org/github.com/prometheus/procfs?status.png)](https://godoc.org/github.com/prometheus/procfs)
[![Build Status](https://travis-ci.org/prometheus/procfs.svg?branch=master)](https://travis-ci.org/prometheus/procfs)
This directory contains some empty files that are the symlinks the files in the "fd" directory point to.
They are otherwise ignored by the tests
# Prometheus Go client library

[![Build Status](https://travis-ci.org/prometheus/client_golang.svg?branch=master)](https://travis-ci.org/prometheus/client_golang)

This is the [Go](http://golang.org) client library for
[Prometheus](http://prometheus.io). It has two separate parts, one for
instrumenting application code, and one for creating clients that talk to the
Prometheus HTTP API.

## Instrumenting applications

[![code-coverage](http://gocover.io/_badge/github.com/prometheus/client_golang/prometheus)](http://gocover.io/github.com/prometheus/client_golang/prometheus) [![go-doc](https://godoc.org/github.com/prometheus/client_golang/prometheus?status.svg)](https://godoc.org/github.com/prometheus/client_golang/prometheus)

The
[`prometheus` directory](https://github.com/prometheus/client_golang/tree/master/prometheus)
contains the instrumentation library. See the
[best practices section](http://prometheus.io/docs/practices/naming/) of the
Prometheus documentation to learn more about instrumenting applications.

The
[`examples` directory](https://github.com/prometheus/client_golang/tree/master/examples)
contains simple examples of instrumented code.

## Client for the Prometheus HTTP API

[![code-coverage](http://gocover.io/_badge/github.com/prometheus/client_golang/api/prometheus)](http://gocover.io/github.com/prometheus/client_golang/api/prometheus) [![go-doc](https://godoc.org/github.com/prometheus/client_golang/api/prometheus?status.svg)](https://godoc.org/github.com/prometheus/client_golang/api/prometheus)

The
[`api/prometheus` directory](https://github.com/prometheus/client_golang/tree/master/api/prometheus)
contains the client for the
[Prometheus HTTP API](http://prometheus.io/docs/querying/api/). It allows you
to write Go applications that query time series data from a Prometheus server.

## Where is `model`, `extraction`, and `text`?

The `model` packages has been moved to
[`prometheus/common/model`](https://github.com/prometheus/common/tree/master/model).

The `extraction` and `text` packages are now contained in
[`prometheus/common/expfmt`](https://github.com/prometheus/common/tree/master/expfmt).

## Contributing and community

See the [contributing guidelines](CONTRIBUTING.md) and the
[Community section](http://prometheus.io/community/) of the homepage.
# Overview
This is the [Prometheus](http://www.prometheus.io) telemetric
instrumentation client [Go](http://golang.org) client library.  It
enable authors to define process-space metrics for their servers and
expose them through a web service interface for extraction,
aggregation, and a whole slew of other post processing techniques.

# Installing
    $ go get github.com/prometheus/client_golang/prometheus

# Example
```go
package main

import (
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
)

var (
	indexed = prometheus.NewCounter(prometheus.CounterOpts{
		Namespace: "my_company",
		Subsystem: "indexer",
		Name:      "documents_indexed",
		Help:      "The number of documents indexed.",
	})
	size = prometheus.NewGauge(prometheus.GaugeOpts{
		Namespace: "my_company",
		Subsystem: "storage",
		Name:      "documents_total_size_bytes",
		Help:      "The total size of all documents in the storage.",
	})
)

func main() {
	http.Handle("/metrics", prometheus.Handler())

	indexed.Inc()
	size.Set(5)

	http.ListenAndServe(":8080", nil)
}

func init() {
	prometheus.MustRegister(indexed)
	prometheus.MustRegister(size)
}
```

# Documentation

[![GoDoc](https://godoc.org/github.com/prometheus/client_golang?status.png)](https://godoc.org/github.com/prometheus/client_golang)
# Common
[![Build Status](https://travis-ci.org/prometheus/common.svg)](https://travis-ci.org/prometheus/common)

This repository contains Go libraries that are shared across Prometheus
components and libraries.

* **model**: Shared data structures
* **expfmt**: Decoding and encoding for the exposition format
* **route**: A routing wrapper around [httprouter](https://github.com/julienschmidt/httprouter) using `context.Context`
* **log**: A logging wrapper around [logrus](https://github.com/Sirupsen/logrus)
PACKAGE

package goautoneg
import "bitbucket.org/ww/goautoneg"

HTTP Content-Type Autonegotiation.

The functions in this package implement the behaviour specified in
http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html

Copyright (c) 2011, Open Knowledge Foundation Ltd.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.

    Neither the name of the Open Knowledge Foundation Ltd. nor the
    names of its contributors may be used to endorse or promote
    products derived from this software without specific prior written
    permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


FUNCTIONS

func Negotiate(header string, alternatives []string) (content_type string)
Negotiate the most appropriate content_type given the accept header
and a list of alternatives.

func ParseAccept(header string) (accept []Accept)
Parse an Accept Header string returning a sorted list
of clauses


TYPES

type Accept struct {
    Type, SubType string
    Q             float32
    Params        map[string]string
}
Structure to represent a clause in an HTTP Accept Header


SUBDIRECTORIES

	.hg
# HttpRouter [![Build Status](https://travis-ci.org/julienschmidt/httprouter.svg?branch=master)](https://travis-ci.org/julienschmidt/httprouter) [![Coverage](http://gocover.io/_badge/github.com/julienschmidt/httprouter?0)](http://gocover.io/github.com/julienschmidt/httprouter) [![GoDoc](http://godoc.org/github.com/julienschmidt/httprouter?status.svg)](http://godoc.org/github.com/julienschmidt/httprouter)

HttpRouter is a lightweight high performance HTTP request router (also called *multiplexer* or just *mux* for short) for [Go](http://golang.org/).

In contrast to the [default mux][http.ServeMux] of Go's `net/http` package, this router supports variables in the routing pattern and matches against the request method. It also scales better.

The router is optimized for high performance and a small memory footprint. It scales well even with very long paths and a large number of routes. A compressing dynamic trie (radix tree) structure is used for efficient matching.

## Features

**Only explicit matches:** With other routers, like [`http.ServeMux`][http.ServeMux], a requested URL path could match multiple patterns. Therefore they have some awkward pattern priority rules, like *longest match* or *first registered, first matched*. By design of this router, a request can only match exactly one or no route. As a result, there are also no unintended matches, which makes it great for SEO and improves the user experience.

**Stop caring about trailing slashes:** Choose the URL style you like, the router automatically redirects the client if a trailing slash is missing or if there is one extra. Of course it only does so, if the new path has a handler. If you don't like it, you can [turn off this behavior](http://godoc.org/github.com/julienschmidt/httprouter#Router.RedirectTrailingSlash).

**Path auto-correction:** Besides detecting the missing or additional trailing slash at no extra cost, the router can also fix wrong cases and remove superfluous path elements (like `../` or `//`). Is [CAPTAIN CAPS LOCK](http://www.urbandictionary.com/define.php?term=Captain+Caps+Lock) one of your users? HttpRouter can help him by making a case-insensitive look-up and redirecting him to the correct URL.

**Parameters in your routing pattern:** Stop parsing the requested URL path, just give the path segment a name and the router delivers the dynamic value to you. Because of the design of the router, path parameters are very cheap.

**Zero Garbage:** The matching and dispatching process generates zero bytes of garbage. In fact, the only heap allocations that are made, is by building the slice of the key-value pairs for path parameters. If the request path contains no parameters, not a single heap allocation is necessary.

**Best Performance:** [Benchmarks speak for themselves][benchmark]. See below for technical details of the implementation.

**No more server crashes:** You can set a [Panic handler][Router.PanicHandler] to deal with panics occurring during handling a HTTP request. The router then recovers and lets the `PanicHandler` log what happened and deliver a nice error page.

Of course you can also set **custom [`NotFound`][Router.NotFound] and  [`MethodNotAllowed`](http://godoc.org/github.com/julienschmidt/httprouter#Router.MethodNotAllowed) handlers** and [**serve static files**][Router.ServeFiles].

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

As you can see, `:name` is a *named parameter*. The values are accessible via `httprouter.Params`, which is just a slice of `httprouter.Param`s. You can get the value of a parameter either by its index in the slice, or by using the `ByName(name)` method: `:name` can be retrived by `ByName("name")`.

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

The second type are *catch-all* parameters and have the form `*name`. Like the name suggests, they match everything. Therefore they must always be at the **end** of the pattern:

```
Pattern: /src/*filepath

 /src/                     match
 /src/somefile.go          match
 /src/subdir/somefile.go   match
```

## How does it work?

The router relies on a tree structure which makes heavy use of *common prefixes*, it is basically a *compact* [*prefix tree*](http://en.wikipedia.org/wiki/Trie) (or just [*Radix tree*](http://en.wikipedia.org/wiki/Radix_tree)). Nodes with a common prefix also share a common parent. Here is a short example what the routing tree for the `GET` request method could look like:

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

Every `*<num>` represents the memory address of a handler function (a pointer). If you follow a path trough the tree from the root to the leaf, you get the complete route path, e.g `\blog\:post\`, where `:post` is just a placeholder ([*parameter*](#named-parameters)) for an actual post name. Unlike hash-maps, a tree structure also allows us to use dynamic parts like the `:post` parameter, since we actually match against the routing patterns instead of just comparing hashes. [As benchmarks show][benchmark], this works very well and efficient.

Since URL paths have a hierarchical structure and make use only of a limited set of characters (byte values), it is very likely that there are a lot of common prefixes. This allows us to easily reduce the routing into ever smaller problems. Moreover the router manages a separate tree for every request method. For one thing it is more space efficient than holding a method->handle map in every single node, for another thing is also allows us to greatly reduce the routing problem before even starting the look-up in the prefix-tree.

For even better scalability, the child nodes on each tree level are ordered by priority, where the priority is just the number of handles registered in sub nodes (children, grandchildren, and so on..). This helps in two ways:

1. Nodes which are part of the most routing paths are evaluated first. This helps to make as much routes as possible to be reachable as fast as possible.
2. It is some sort of cost compensation. The longest reachable path (highest cost) can always be evaluated first. The following scheme visualizes the tree structure. Nodes are evaluated from top to bottom and from left to right.

```
├------------
├---------
├-----
├----
├--
├--
└-
```

## Why doesn't this work with `http.Handler`?

**It does!** The router itself implements the `http.Handler` interface. Moreover the router provides convenient [adapters for `http.Handler`][Router.Handler]s and [`http.HandlerFunc`][Router.HandlerFunc]s which allows them to be used as a [`httprouter.Handle`][Router.Handle] when registering a route. The only disadvantage is, that no parameter values can be retrieved when a `http.Handler` or `http.HandlerFunc` is used, since there is no efficient way to pass the values with the existing function parameters. Therefore [`httprouter.Handle`][Router.Handle] has a third function parameter.

Just try it out for yourself, the usage of HttpRouter is very straightforward. The package is compact and minimalistic, but also probably one of the easiest routers to set up.

## Where can I find Middleware *X*?

This package just provides a very efficient request router with a few extra features. The router is just a [`http.Handler`][http.Handler], you can chain any http.Handler compatible middleware before the router, for example the [Gorilla handlers](http://www.gorillatoolkit.org/pkg/handlers). Or you could [just write your own](http://justinas.org/writing-http-middleware-in-go/), it's very easy!

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

Another quick example: Basic Authentication (RFC 2617) for handles:

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

**NOTE: It might be required to set [`Router.HandleMethodNotAllowed`][Router.HandleMethodNotAllowed] to `false` to avoid problems.**

You can use another [`http.Handler`][http.Handler], for example another router, to handle requests which could not be matched by this router by using the [`Router.NotFound`][Router.NotFound] handler. This allows chaining.

### Static files

The `NotFound` handler can for example be used to serve static files from the root path `/` (like an `index.html` file along with other assets):

```go
// Serve static files from the ./public directory
router.NotFound = http.FileServer(http.Dir("public"))
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
* [httpway](http://github.com/corneldamian/httpway): Simple middleware extension with context for httprouter and a server with gracefully shutdown support
* [kami](https://github.com/guregu/kami): A tiny web framework using x/net/context
* [Medeina](https://github.com/imdario/medeina): Inspired by Ruby's Roda and Cuba
* [Neko](https://github.com/rocwong/neko): A lightweight web application framework for Golang
* [Roxanna](https://github.com/iamthemuffinman/Roxanna): An amalgamation of httprouter, better logging, and hot reload
* [siesta](https://github.com/VividCortex/siesta): Composable HTTP handlers with contexts

[benchmark]: <https://github.com/julienschmidt/go-http-routing-benchmark>
[http.Handler]: <http://golang.org/pkg/net/http/#Handler
[http.ServeMux]: <http://golang.org/pkg/net/http/#ServeMux>
[Router.Handle]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.Handle>
[Router.HandleMethodNotAllowed]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.HandleMethodNotAllowed>
[Router.Handler]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.Handler>
[Router.HandlerFunc]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.HandlerFunc>
[Router.NotFound]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.NotFound>
[Router.PanicHandler]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.PanicHandler>
[Router.ServeFiles]: <http://godoc.org/github.com/julienschmidt/httprouter#Router.ServeFiles>
# mapstructure

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
# tar-split

[![Build Status](https://travis-ci.org/vbatts/tar-split.svg?branch=master)](https://travis-ci.org/vbatts/tar-split)

Pristinely disassembling a tar archive, and stashing needed raw bytes and offsets to reassemble a validating original archive.

## Docs

Code API for libraries provided by `tar-split`:

* https://godoc.org/github.com/vbatts/tar-split/tar/asm
* https://godoc.org/github.com/vbatts/tar-split/tar/storage
* https://godoc.org/github.com/vbatts/tar-split/archive/tar

## Install

The command line utilitiy is installable via:

```bash
go get github.com/vbatts/tar-split/cmd/tar-split
```

## Usage

For cli usage, see its [README.md](cmd/tar-split/README.md).
For the library see the [docs](#docs)

## Demo

### Basic disassembly and assembly

This demonstrates the `tar-split` command and how to assemble a tar archive from the `tar-data.json.gz`


![basic cmd demo thumbnail](https://i.ytimg.com/vi/vh5wyjIOBtc/2.jpg?time=1445027151805)
[youtube video of basic command demo](https://youtu.be/vh5wyjIOBtc)

### Docker layer preservation

This demonstrates the tar-split integration for docker-1.8. Providing consistent tar archives for the image layer content.

![docker tar-split demo](https://i.ytimg.com/vi_webp/vh5wyjIOBtc/default.webp)
[youtube vide of docker layer checksums](https://youtu.be/tV_Dia8E8xw)

## Caveat

Eventually this should detect TARs that this is not possible with.

For example stored sparse files that have "holes" in them, will be read as a
contiguous file, though the archive contents may be recorded in sparse format.
Therefore when adding the file payload to a reassembled tar, to achieve
identical output, the file payload would need be precisely re-sparsified. This
is not something I seek to fix imediately, but would rather have an alert that
precise reassembly is not possible.
(see more http://www.gnu.org/software/tar/manual/html_node/Sparse-Formats.html)


Other caveat, while tar archives support having multiple file entries for the
same path, we will not support this feature. If there are more than one entries
with the same path, expect an err (like `ErrDuplicatePath`) or a resulting tar
stream that does not validate your original checksum/signature.

## Contract

Do not break the API of stdlib `archive/tar` in our fork (ideally find an upstream mergeable solution).

## Std Version

The version of golang stdlib `archive/tar` is from go1.6
It is minimally extended to expose the raw bytes of the TAR, rather than just the marshalled headers and file stream.


## Design

See the [design](concept/DESIGN.md).

## Stored Metadata

Since the raw bytes of the headers and padding are stored, you may be wondering
what the size implications are. The headers are at least 512 bytes per
file (sometimes more), at least 1024 null bytes on the end, and then various
padding. This makes for a constant linear growth in the stored metadata, with a
naive storage implementation.

First we'll get an archive to work with. For repeatability, we'll make an
archive from what you've just cloned:

```bash
git archive --format=tar -o tar-split.tar HEAD .
```

```bash
$ go get github.com/vbatts/tar-split/cmd/tar-split
$ tar-split checksize ./tar-split.tar
inspecting "tar-split.tar" (size 210k)
 -- number of files: 50
 -- size of metadata uncompressed: 53k
 -- size of gzip compressed metadata: 3k
```

So assuming you've managed the extraction of the archive yourself, for reuse of
the file payloads from a relative path, then the only additional storage
implications are as little as 3kb.

But let's look at a larger archive, with many files.

```bash
$ ls -sh ./d.tar
1.4G ./d.tar
$ tar-split checksize ~/d.tar 
inspecting "/home/vbatts/d.tar" (size 1420749k)
 -- number of files: 38718
 -- size of metadata uncompressed: 43261k
 -- size of gzip compressed metadata: 2251k
```

Here, an archive with 38,718 files has a compressed footprint of about 2mb.

Rolling the null bytes on the end of the archive, we will assume a
bytes-per-file rate for the storage implications.

| uncompressed | compressed |
| :----------: | :--------: |
| ~ 1kb per/file | 0.06kb per/file |


## What's Next?

* More implementations of storage Packer and Unpacker
* More implementations of FileGetter and FilePutter
* would be interesting to have an assembler stream that implements `io.Seeker`


## License

See [LICENSE](LICENSE)

asm
===

This library for assembly and disassembly of tar archives, facilitated by
`github.com/vbatts/tar-split/tar/storage`.


Concerns
--------

For completely safe assembly/disassembly, there will need to be a Content
Addressable Storage (CAS) directory, that maps to a checksum in the
`storage.Entity` of `storage.FileType`.

This is due to the fact that tar archives _can_ allow multiple records for the
same path, but the last one effectively wins. Even if the prior records had a
different payload. 

In this way, when assembling an archive from relative paths, if the archive has
multiple entries for the same path, then all payloads read in from a relative
path would be identical.


Thoughts
--------

Have a look-aside directory or storage. This way when a clobbering record is
encountered from the tar stream, then the payload of the prior/existing file is
stored to the CAS. This way the clobbering record's file payload can be
extracted, but we'll have preserved the payload needed to reassemble a precise
tar archive.

clobbered/path/to/file.[0-N]

*alternatively*

We could just _not_ support tar streams that have clobbering file paths.
Appending records to the archive is not incredibly common, and doesn't happen
by default for most implementations.  Not supporting them wouldn't be a
security concern either, as if it did occur, we would reassemble an archive
that doesn't validate signature/checksum, so it shouldn't be trusted anyway.

Otherwise, this will allow us to defer support for appended files as a FUTURE FEATURE.

# tar-split utility

## Installation

	go get -u github.com/vbatts/tar-split/cmd/tar-split

## Usage

### Disassembly

```bash
$ sha256sum archive.tar 
d734a748db93ec873392470510b8a1c88929abd8fae2540dc43d5b26f7537868  archive.tar
$ mkdir ./x
$ tar-split disasm --output tar-data.json.gz ./archive.tar | tar -C ./x -x
time="2015-07-20T15:45:04-04:00" level=info msg="created tar-data.json.gz from ./archive.tar (read 204800 bytes)"
```

### Assembly

```bash
$ tar-split asm --output new.tar --input ./tar-data.json.gz  --path ./x/
INFO[0000] created new.tar from ./x/ and ./tar-data.json.gz (wrote 204800 bytes)
$ sha256sum new.tar 
d734a748db93ec873392470510b8a1c88929abd8fae2540dc43d5b26f7537868  new.tar
```

### Estimating metadata size

```bash
$ tar-split checksize ./archive.tar
inspecting "./archive.tar" (size 200k)
 -- number of files: 28
 -- size of metadata uncompressed: 28k
 -- size of gzip compressed metadata: 1k
```



# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/Sirupsen/logrus.svg?branch=master)](https://travis-ci.org/Sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/Sirupsen/logrus?status.svg)](https://godoc.org/github.com/Sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc]. **Please note the Logrus API is not
yet stable (pre 1.0). Logrus itself is completely stable and has been used in
many large deployments. The core API is unlikely to change much but please
version control your Logrus to make sure you aren't fetching latest `master` on
every build.**

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

#### Example

The simplest way to use Logrus is simply the package-level exported logger:

```go
package main

import (
  log "github.com/Sirupsen/logrus"
)

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
  }).Info("A walrus appears")
}
```

Note that it's completely api-compatible with the stdlib logger, so you can
replace your `log` imports everywhere with `log "github.com/Sirupsen/logrus"`
and you'll now have the flexibility of Logrus. You can customize it all you
want:

```go
package main

import (
  "os"
  log "github.com/Sirupsen/logrus"
)

func init() {
  // Log as JSON instead of the default ASCII formatter.
  log.SetFormatter(&log.JSONFormatter{})

  // Output to stderr instead of stdout, could also be a file.
  log.SetOutput(os.Stderr)

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
  "github.com/Sirupsen/logrus"
)

// Create a new instance of the logger. You can have any number of instances.
var log = logrus.New()

func main() {
  // The API for setting attributes is a little different than the package level
  // exported logger. See Godoc.
  log.Out = os.Stderr

  log.WithFields(logrus.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")
}
```

#### Fields

Logrus encourages careful, structured logging though logging fields instead of
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

#### Hooks

You can add hooks for logging levels. For example to send errors to an exception
tracking service on `Error`, `Fatal` and `Panic`, info to StatsD or log to
multiple places simultaneously, e.g. syslog.

Logrus comes with [built-in hooks](hooks/). Add those, or your custom hook, in
`init`:

```go
import (
  log "github.com/Sirupsen/logrus"
  "gopkg.in/gemnasium/logrus-airbrake-hook.v2" // the package is named "aibrake"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
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
| [Airbrake](https://github.com/gemnasium/logrus-airbrake-hook) | Send errors to the Airbrake API V3. Uses the official [`gobrake`](https://github.com/airbrake/gobrake) behind the scenes. |
| [Airbrake "legacy"](https://github.com/gemnasium/logrus-airbrake-legacy-hook) | Send errors to an exception tracking service compatible with the Airbrake API V2. Uses [`airbrake-go`](https://github.com/tobi/airbrake-go) behind the scenes. |
| [Papertrail](https://github.com/polds/logrus-papertrail-hook) | Send errors to the [Papertrail](https://papertrailapp.com) hosted logging service via UDP. |
| [Syslog](https://github.com/Sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [Bugsnag](https://github.com/Shopify/logrus-bugsnag/blob/master/bugsnag.go) | Send errors to the Bugsnag exception tracking service. |
| [Sentry](https://github.com/evalphobia/logrus_sentry) | Send errors to the Sentry error logging and aggregation service. |
| [Hiprus](https://github.com/nubo/hiprus) | Send errors to a channel in hipchat. |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Journalhook](https://github.com/wercker/journalhook) | Hook for logging to `systemd-journald` |
| [Graylog](https://github.com/gemnasium/logrus-graylog-hook) | Hook for logging to [Graylog](http://graylog2.org/) |
| [Raygun](https://github.com/squirkle/logrus-raygun-hook) | Hook for logging to [Raygun.io](http://raygun.io/) |
| [LFShook](https://github.com/rifflock/lfshook) | Hook for logging to the local filesystem |
| [Honeybadger](https://github.com/agonzalezro/logrus_honeybadger) | Hook for sending exceptions to Honeybadger |
| [Mail](https://github.com/zbindenren/logrus_mail) | Hook for sending exceptions via mail |
| [Rollrus](https://github.com/heroku/rollrus) | Hook for sending errors to rollbar |
| [Fluentd](https://github.com/evalphobia/logrus_fluent) | Hook for logging to fluentd |
| [Mongodb](https://github.com/weekface/mgorus) | Hook for logging to mongodb |
| [Influxus] (http://github.com/vlad-doru/influxus) | Hook for concurrently logging to [InfluxDB] (http://influxdata.com/) |
| [InfluxDB](https://github.com/Abramovic/logrus_influxdb) | Hook for logging to influxdb |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [DeferPanic](https://github.com/deferpanic/dp-logrus) | Hook for logging to DeferPanic |
| [Redis-Hook](https://github.com/rogierlommers/logrus-redis-hook) | Hook for logging to a ELK stack (through Redis) |
| [Amqp-Hook](https://github.com/vladoatanasov/logrus_amqp) | Hook for logging to Amqp broker (Like RabbitMQ) |
| [KafkaLogrus](https://github.com/goibibo/KafkaLogrus) | Hook for logging to kafka |
| [Typetalk](https://github.com/dragon3/logrus-typetalk-hook) | Hook for logging to [Typetalk](https://www.typetalk.in/) |
| [ElasticSearch](https://github.com/sohlich/elogrus) | Hook for logging to ElasticSearch|
| [Sumorus](https://github.com/doublefree/sumorus) | Hook for logging to [SumoLogic](https://www.sumologic.com/)|
| [Scribe](https://github.com/sagar8192/logrus-scribe-hook) | Hook for logging to [Scribe](https://github.com/facebookarchive/scribe)|
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [logz.io](https://github.com/ripcurld00d/logrus-logzio-hook) | Hook for logging to [logz.io](https://logz.io), a Log as a Service using Logstash |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |
| [Pushover](https://github.com/toorop/logrus_pushover) | Send error via [Pushover](https://pushover.net) |


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
  log "github.com/Sirupsen/logrus"
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
    `DisableColors` field to `true`
* `logrus.JSONFormatter`. Logs fields as JSON.

Third party logging formatters:

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

#### Rotation

Log rotation is not provided with Logrus. Log rotation should be done by an
external program (like `logrotate(8)`) that can compress and delete old log
entries. It should not be a feature of the application-level logger.

#### Tools

| Tool | Description |
| ---- | ----------- |
|[Logrus Mate](https://github.com/gogap/logrus_mate)|Logrus mate is a tool for Logrus to manage loggers, you can initial logger's level, hook and formatter by config file, the logger will generated with different config at different environment.|
|[Logrus Viper Helper](https://github.com/heirko/go-contrib/tree/master/logrusHelper)|An Helper arround Logrus to wrap with spf13/Viper to load configuration with fangs! And to simplify Logrus configuration use some behavior of [Logrus Mate](https://github.com/gogap/logrus_mate). [sample](https://github.com/heirko/iris-contrib/blob/master/middleware/logrus-logger/example) |

#### Testing

Logrus has a built in facility for asserting the presence of log messages. This is implemented through the `test` hook and provides:

* decorators for existing logger (`test.NewLocal` and `test.NewGlobal`) which basically just add the `test` hook
* a test logger (`test.NewNullLogger`) that just records log messages (and does not output any):

```go
logger, hook := NewNullLogger()
logger.Error("Hello error")

assert.Equal(1, len(hook.Entries))
assert.Equal(logrus.ErrorLevel, hook.LastEntry().Level)
assert.Equal("Hello error", hook.LastEntry().Message)

hook.Reset()
assert.Nil(hook.LastEntry())
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

#### Thread safty

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
  "github.com/Sirupsen/logrus"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```

If you want to connect to local syslog (Ex. "/dev/log" or "/var/run/syslog" or "/var/run/log"). Just assign empty string to the first two parameters of `NewSyslogHook`. It should look like the following.

```go
import (
  "log/syslog"
  "github.com/Sirupsen/logrus"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("", "", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```# File system notifications for Go

[![GoDoc](https://godoc.org/github.com/fsnotify/fsnotify?status.svg)](https://godoc.org/github.com/fsnotify/fsnotify) [![Go Report Card](https://goreportcard.com/badge/github.com/fsnotify/fsnotify)](https://goreportcard.com/report/github.com/fsnotify/fsnotify)

fsnotify utilizes [golang.org/x/sys](https://godoc.org/golang.org/x/sys) rather than `syscall` from the standard library. Ensure you have the latest version installed by running:

```console
go get -u golang.org/x/sys/...
```

Cross platform: Windows, Linux, BSD and macOS.

|Adapter   |OS        |Status    |
|----------|----------|----------|
|inotify   |Linux 2.6.27 or later, Android\*|Supported [![Build Status](https://travis-ci.org/fsnotify/fsnotify.svg?branch=master)](https://travis-ci.org/fsnotify/fsnotify)|
|kqueue    |BSD, macOS, iOS\*|Supported [![Build Status](https://travis-ci.org/fsnotify/fsnotify.svg?branch=master)](https://travis-ci.org/fsnotify/fsnotify)|
|ReadDirectoryChangesW|Windows|Supported [![Build status](https://ci.appveyor.com/api/projects/status/ivwjubaih4r0udeh/branch/master?svg=true)](https://ci.appveyor.com/project/NathanYoungman/fsnotify/branch/master)|
|FSEvents  |macOS         |[Planned](https://github.com/fsnotify/fsnotify/issues/11)|
|FEN       |Solaris 11    |[In Progress](https://github.com/fsnotify/fsnotify/issues/12)|
|fanotify  |Linux 2.6.37+ | |
|USN Journals |Windows    |[Maybe](https://github.com/fsnotify/fsnotify/issues/53)|
|Polling   |*All*         |[Maybe](https://github.com/fsnotify/fsnotify/issues/9)|

\* Android and iOS are untested.

Please see [the documentation](https://godoc.org/github.com/fsnotify/fsnotify) for usage. Consult the [Wiki](https://github.com/fsnotify/fsnotify/wiki) for the FAQ and further information.

## API stability

fsnotify is a fork of [howeyc/fsnotify](https://godoc.org/github.com/howeyc/fsnotify) with a new API as of v1.0. The API is based on [this design document](http://goo.gl/MrYxyA). 

All [releases](https://github.com/fsnotify/fsnotify/releases) are tagged based on [Semantic Versioning](http://semver.org/). Further API changes are [planned](https://github.com/fsnotify/fsnotify/milestones), and will be tagged with a new major revision number.

Go 1.6 supports dependencies located in the `vendor/` folder. Unless you are creating a library, it is recommended that you copy fsnotify into `vendor/github.com/fsnotify/fsnotify` within your project, and likewise for `golang.org/x/sys`.

## Contributing

Please refer to [CONTRIBUTING][] before opening an issue or pull request.

## Example

See [example_test.go](https://github.com/fsnotify/fsnotify/blob/master/example_test.go).

[contributing]: https://github.com/fsnotify/fsnotify/blob/master/CONTRIBUTING.md

## Related Projects

* [notify](https://github.com/rjeczalik/notify)
* [fsevents](https://github.com/fsnotify/fsevents)

# Perks for Go (golang.org)

Perks contains the Go package quantile that computes approximate quantiles over
an unbounded data stream within low memory and CPU bounds.

For more information and examples, see:
http://godoc.org/github.com/bmizerany/perks

A very special thank you and shout out to Graham Cormode (Rutgers University),
Flip Korn (AT&T Labs–Research), S. Muthukrishnan (Rutgers University), and
Divesh Srivastava (AT&T Labs–Research) for their research and publication of
[Effective Computation of Biased Quantiles over Data Streams](http://www.cs.rutgers.edu/~muthu/bquant.pdf)

Thank you, also:
* Armon Dadgar (@armon)
* Andrew Gerrand (@nf)
* Brad Fitzpatrick (@bradfitz)
* Keith Rarick (@kr)

FAQ:

Q: Why not move the quantile package into the project root?
A: I want to add more packages to perks later.

Copyright (C) 2013 Blake Mizerany

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Open Container Initiative Runtime Specification

The [Open Container Initiative](http://www.opencontainers.org/) develops specifications for standards on Operating System process and application containers.


Table of Contents

- [Introduction](README.md)
  - [Code of Conduct](#code-of-conduct)
  - [Container Principles](principles.md)
  - [Style and Conventions](style.md)
  - [Roadmap](ROADMAP.md)
  - [Implementations](implementations.md)
  - [project](project.md)
- [Filesystem Bundle](bundle.md)
- Runtime and Lifecycle
  - [General Runtime and Lifecycle](runtime.md)
  - [Linux-specific Runtime and Lifecycle](runtime-linux.md)
- Configuration
  - [General Configuration](config.md)
  - [Linux-specific Configuration](config-linux.md)
  - [Solaris-specific Configuration](config-solaris.md)
  - [Windows-specific Configuration](config-windows.md)
- [Glossary](glossary.md)

In the specifications in the above table of contents, the keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119) (Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997).

The keywords "unspecified", "undefined", and "implementation-defined" are to be interpreted as described in the [rationale for the C99 standard][c99-unspecified].

An implementation is not compliant for a given CPU architecture if it fails to satisfy one or more of the MUST, REQUIRED, or SHALL requirements for the protocols it implements.
An implementation is compliant for a given CPU architecture if it satisfies all the MUST, REQUIRED, and SHALL requirements for the protocols it implements.

Protocols defined by this specification are:
* Linux containers: [runtime.md](runtime.md), [config.md](config.md), [config-linux.md](config-linux.md), and [runtime-linux.md](runtime-linux.md).
* Solaris containers: [runtime.md](runtime.md), [config.md](config.md), and [config-solaris.md](config-solaris.md).
* Windows containers: [runtime.md](runtime.md), [config.md](config.md), and [config-windows.md](config-windows.md).

# Use Cases

To provide context for users the following section gives example use cases for each part of the spec.

#### Application Bundle Builders

Application bundle builders can create a [bundle](bundle.md) directory that includes all of the files required for launching an application as a container.
The bundle contains an OCI [configuration file](config.md) where the builder can specify host-independent details such as [which executable to launch](config.md#process-configuration) and host-specific settings such as [mount](config.md#mounts) locations, [hook](config.md#hooks) paths, Linux [namespaces](config-linux.md#namespaces) and [cgroups](config-linux.md#control-groups).
Because the configuration includes host-specific settings, application bundle directories copied between two hosts may require configuration adjustments.

#### Hook Developers

[Hook](config.md#hooks) developers can extend the functionality of an OCI-compliant runtime by hooking into a container's lifecycle with an external application.
Example use cases include sophisticated network configuration, volume garbage collection, etc.

#### Runtime Developers

Runtime developers can build runtime implementations that run OCI-compliant bundles and container configuration, containing low-level OS and host specific details, on a particular platform.

# Releases

There is a loose [Road Map](./ROADMAP.md).
During the `0.x` series of OCI releases we make no backwards compatibility guarantees and intend to break the schema during this series.

# Contributing

Development happens on GitHub for the spec.
Issues are used for bugs and actionable items and longer discussions can happen on the [mailing list](#mailing-list).

The specification and code is licensed under the Apache 2.0 license found in the [LICENSE](./LICENSE) file.

## Code of Conduct

Participation in the OpenContainers community is governed by [OpenContainer's Code of Conduct](https://github.com/opencontainers/tob/blob/d2f9d68c1332870e40693fe077d311e0742bc73d/code-of-conduct.md).

## Discuss your design

The project welcomes submissions, but please let everyone know what you are working on.

Before undertaking a nontrivial change to this specification, send mail to the [mailing list](#mailing-list) to discuss what you plan to do.
This gives everyone a chance to validate the design, helps prevent duplication of effort, and ensures that the idea fits.
It also guarantees that the design is sound before code is written; a GitHub pull-request is not the place for high-level discussions.

Typos and grammatical errors can go straight to a pull-request.
When in doubt, start on the [mailing-list](#mailing-list).

## Weekly Call

The contributors and maintainers of all OCI projects have a weekly meeting Wednesdays at 2:00 PM (USA Pacific).
Everyone is welcome to participate via [UberConference web][UberConference] or audio-only: 415-968-0849 (no PIN needed.)
An initial agenda will be posted to the [mailing list](#mailing-list) earlier in the week, and everyone is welcome to propose additional topics or suggest other agenda alterations there.
Minutes are posted to the [mailing list](#mailing-list) and minutes from past calls are archived to the [wiki](https://github.com/opencontainers/runtime-spec/wiki) for those who are unable to join the call.

## Mailing List

You can subscribe and join the mailing list on [Google Groups](https://groups.google.com/a/opencontainers.org/forum/#!forum/dev).

## IRC

OCI discussion happens on #opencontainers on Freenode ([logs][irc-logs]).

## Git commit

### Sign your work

The sign-off is a simple line at the end of the explanation for the patch, which certifies that you wrote it or otherwise have the right to pass it on as an open-source patch.
The rules are pretty simple: if you can certify the below (from [developercertificate.org](http://developercertificate.org/)):

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
660 York Street, Suite 102,
San Francisco, CA 94110 USA

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

then you just add a line to every git commit message:

    Signed-off-by: Joe Smith <joe@gmail.com>

using your real name (sorry, no pseudonyms or anonymous contributions.)

You can add the sign off when creating the git commit via `git commit -s`.

### Commit Style

Simple house-keeping for clean git history.
Read more on [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/) or the Discussion section of [`git-commit(1)`](http://git-scm.com/docs/git-commit).

1. Separate the subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how
  * If there was important/useful/essential conversation or information, copy or include a reference
8. When possible, one keyword to scope the change in the subject (i.e. "README: ...", "runtime: ...")

[c99-unspecified]: http://www.open-std.org/jtc1/sc22/wg14/www/C99RationaleV5.10.pdf#page=18
[UberConference]: https://www.uberconference.com/opencontainers
[irc-logs]: http://ircbot.wl.linuxfoundation.org/eavesdrop/%23opencontainers/
# JSON schema

## Overview

This directory contains the [JSON Schema](http://json-schema.org/) for validating JSON covered by this specification.

The layout of the files is as follows:

* [config-schema.json](config-schema.json) - the primary entrypoint for the [configuration](../config.md) schema
* [config-linux.json](config-linux.json) - the [Linux-specific configuration sub-structure](../config-linux.md)
* [config-solaris.json](config-solaris.json) - the [Solaris-specific configuration sub-structure](../config-solaris.md)
* [config-windows.json](config-windows.json) - the [Windows-specific configuration sub-structure](../config-windows.md)
* [state-schema.json](state-schema.json) - the primary entrypoint for the [state JSON](../runtime.md#state) schema
* [defs.json](defs.json) - definitions for general types
* [defs-linux.json](defs-linux.json) - definitions for Linux-specific types
* [validate.go](validate.go) - validation utility source code


## Utility

There is also included a simple utility for facilitating validation.
To build it:

```bash
export GOPATH=`mktemp -d`
go get -d ./...
go build ./validate.go
rm -rf $GOPATH
```

Or you can just use make command to create the utility:

```bash
make validate
```

Then use it like:

```bash
./validate config-schema.json <yourpath>/config.json
```
[![Build Status](https://jenkins.dockerproject.org/buildStatus/icon?job=runc Master)](https://jenkins.dockerproject.org/job/runc Master)

## runc

`runc` is a CLI tool for spawning and running containers according to the OCI specification.

## Releases

`runc` depends on and tracks the [runtime-spec](https://github.com/opencontainers/runtime-spec) repository.
We will try to make sure that `runc` and the OCI specification major versions stay in lockstep.
This means that `runc` 1.0.0 should implement the 1.0 version of the specification.

You can find official releases of `runc` on the [release](https://github.com/opencontainers/runc/releases) page.

## Building

`runc` currently supports the Linux platform with various architecture support. 
It must be built with Go version 1.6 or higher in order for some features to function properly.

```bash
# create a 'github.com/opencontainers' in your GOPATH/src
cd github.com/opencontainers
git clone https://github.com/opencontainers/runc
cd runc

make
sudo make install
```

`runc` will be installed to `/usr/local/sbin/runc` on your system.

In order to enable seccomp support you will need to install libseccomp on your platform.
If you do not want to build `runc` with seccomp support you can add `BUILDTAGS=""` when running make.

#### Build Tags

`runc` supports optional build tags for compiling support of various features.
To add build tags to the make option the `BUILDTAGS` variable must be set.

```bash
make BUILDTAGS='seccomp apparmor'
```

| Build Tag | Feature                            | Dependency  |
|-----------|------------------------------------|-------------|
| seccomp   | Syscall filtering                  | libseccomp  |
| selinux   | selinux process and mount labeling | <none>      |
| apparmor  | apparmor profile support           | libapparmor |


### Running the test suite

`runc` currently supports running its test suite via Docker.
To run the suite just type `make test`.

```bash
make test
```

There are additional make targets for running the tests outside of a container but this is not recommended as the tests are written with the expectation that they can write and remove anywhere.

You can run a specific test case by setting the `TESTFLAGS` variable.

```bash
# make test TESTFLAGS="-run=SomeTestFunction"
```

## Using runc

### Creating an OCI Bundle

In order to use runc you must have your container in the format of an OCI bundle.
If you have Docker installed you can use its `export` method to acquire a root filesystem from an existing Docker container.

```bash
# create the top most bundle directory
mkdir /mycontainer
cd /mycontainer

# create the rootfs directory
mkdir rootfs

# export busybox via Docker into the rootfs directory
docker export $(docker create busybox) | tar -C rootfs -xvf -
```

After a root filesystem is populated you just generate a spec in the format of a `config.json` file inside your bundle.
`runc` provides a `spec` command to generate a base template spec that you are then able to edit.
To find features and documentation for fields in the spec please refer to the [specs](https://github.com/opencontainers/runtime-spec) repository.

```bash
runc spec
```

### Running Containers

Assuming you have an OCI bundle from the previous step you can execute the container in two different ways.

The first way is to use the convenience command `run` that will handle creating, starting, and deleting the container after it exits.

```bash
cd /mycontainer

runc run mycontainerid
```

If you used the unmodified `runc spec` template this should give you a `sh` session inside the container.

The second way to start a container is using the specs lifecycle operations.
This gives you more power over how the container is created and managed while it is running.
This will also launch the container in the background so you will have to edit the `config.json` to remove the `terminal` setting for the simple examples here.
Your process field in the `config.json` should look like this below with `"terminal": false` and `"args": ["sleep", "5"]`.


```json
        "process": {
                "terminal": false,
                "user": {
                        "uid": 0,
                        "gid": 0
                },
                "args": [
                        "sleep", "5"
                ],
                "env": [
                        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                        "TERM=xterm"
                ],
                "cwd": "/",
                "capabilities": [
                        "CAP_AUDIT_WRITE",
                        "CAP_KILL",
                        "CAP_NET_BIND_SERVICE"
                ],
                "rlimits": [
                        {
                                "type": "RLIMIT_NOFILE",
                                "hard": 1024,
                                "soft": 1024
                        }
                ],
                "noNewPrivileges": true
        },
```

Now we can go though the lifecycle operations in your shell.


```bash
cd /mycontainer

runc create mycontainerid

# view the container is created and in the "created" state
runc list

# start the process inside the container
runc start mycontainerid

# after 5 seconds view that the container has exited and is now in the stopped state
runc list

# now delete the container
runc delete mycontainerid
```

This adds more complexity but allows higher level systems to manage runc and provides points in the containers creation to setup various settings after the container has created and/or before it is deleted.
This is commonly used to setup the container's network stack after `create` but before `start` where the user's defined process will be running.

#### Supervisors

`runc` can be used with process supervisors and init systems to ensure that containers are restarted when they exit.
An example systemd unit file looks something like this.

```systemd
[Unit]
Description=Start My Container

[Service]
Type=forking
ExecStart=/usr/local/sbin/runc run -d --pid-file /run/mycontainerid.pid mycontainerid
ExecStopPost=/usr/local/sbin/runc delete mycontainerid
WorkingDirectory=/mycontainer
PIDFile=/run/mycontainerid.pid

[Install]
WantedBy=multi-user.target
```
# runc Integration Tests

Integration tests provide end-to-end testing of runc.

Note that integration tests do **not** replace unit tests.

As a rule of thumb, code should be tested thoroughly with unit tests.
Integration tests on the other hand are meant to test a specific feature end
to end.

Integration tests are written in *bash* using the
[bats](https://github.com/sstephenson/bats) framework.

## Running integration tests

The easiest way to run integration tests is with Docker:
```
$ make integration
```
Alternatively, you can run integration tests directly on your host through make:
```
$ sudo make localintegration
```
Or you can just run them directly using bats
```
$ sudo bats tests/integration
```
To run a single test bucket:
```
$ make integration TESTFLAGS="/checkpoint.bats"
```


To run them on your host, you will need to setup a development environment plus
[bats](https://github.com/sstephenson/bats#installing-bats-from-source)
For example:
```
$ cd ~/go/src/github.com
$ git clone https://github.com/sstephenson/bats.git
$ cd bats
$ ./install.sh /usr/local
```

> **Note**: There are known issues running the integration tests using
> **devicemapper** as a storage driver, make sure that your docker daemon
> is using **aufs** if you want to successfully run the integration tests.

## Writing integration tests

[helper functions]
(https://github.com/opencontainers/runc/blob/master/test/integration/helpers.bash)
are provided in order to facilitate writing tests.

```sh
#!/usr/bin/env bats

# This will load the helpers.
load helpers

# setup is called at the beginning of every test.
function setup() {
  # see functions teardown_hello and setup_hello in helpers.bash, used to
  # create a pristine environment for running your tests
  teardown_hello
  setup_hello
}

# teardown is called at the end of every test.
function teardown() {
  teardown_hello
}

@test "this is a simple test" {
  runc run containerid
  # "The runc macro" automatically populates $status, $output and $lines.
  # Please refer to bats documentation to find out more.
  [ "$status" -eq 0 ]

  # check expected output
  [[ "${output}" == *"Hello"* ]]
}

```
runc man pages
====================

This directory contains man pages for runc in markdown format.

To generate man pages from it, use this command

    ./md2man-all.sh

You will see man pages generated under the man8 directory.

Libcontainer provides a native Go implementation for creating containers
with namespaces, cgroups, capabilities, and filesystem access controls.
It allows you to manage the lifecycle of the container performing additional operations
after the container is created.


#### Container
A container is a self contained execution environment that shares the kernel of the
host system and which is (optionally) isolated from other containers in the system.

#### Using libcontainer

Because containers are spawned in a two step process you will need a binary that
will be executed as the init process for the container. In libcontainer, we use
the current binary (/proc/self/exe) to be executed as the init process, and use
arg "init", we call the first step process "bootstrap", so you always need a "init"
function as the entry of "bootstrap".

```go
func init() {
	if len(os.Args) > 1 && os.Args[1] == "init" {
		runtime.GOMAXPROCS(1)
		runtime.LockOSThread()
		factory, _ := libcontainer.New("")
		if err := factory.StartInitialization(); err != nil {
			logrus.Fatal(err)
		}
		panic("--this line should have never been executed, congratulations--")
	}
}
```

Then to create a container you first have to initialize an instance of a factory
that will handle the creation and initialization for a container.

```go
factory, err := libcontainer.New("/var/lib/container", libcontainer.Cgroupfs, libcontainer.InitArgs(os.Args[0], "init"))
if err != nil {
	logrus.Fatal(err)
	return
}
```

Once you have an instance of the factory created we can create a configuration
struct describing how the container is to be created. A sample would look similar to this:

```go
defaultMountFlags := syscall.MS_NOEXEC | syscall.MS_NOSUID | syscall.MS_NODEV
config := &configs.Config{
	Rootfs: "/your/path/to/rootfs",
	Capabilities: []string{
		"CAP_CHOWN",
		"CAP_DAC_OVERRIDE",
		"CAP_FSETID",
		"CAP_FOWNER",
		"CAP_MKNOD",
		"CAP_NET_RAW",
		"CAP_SETGID",
		"CAP_SETUID",
		"CAP_SETFCAP",
		"CAP_SETPCAP",
		"CAP_NET_BIND_SERVICE",
		"CAP_SYS_CHROOT",
		"CAP_KILL",
		"CAP_AUDIT_WRITE",
	},
	Namespaces: configs.Namespaces([]configs.Namespace{
		{Type: configs.NEWNS},
		{Type: configs.NEWUTS},
		{Type: configs.NEWIPC},
		{Type: configs.NEWPID},
		{Type: configs.NEWUSER},
		{Type: configs.NEWNET},
	}),
	Cgroups: &configs.Cgroup{
		Name:   "test-container",
		Parent: "system",
		Resources: &configs.Resources{
			MemorySwappiness: nil,
			AllowAllDevices:  nil,
			AllowedDevices:   configs.DefaultAllowedDevices,
		},
	},
	MaskPaths: []string{
		"/proc/kcore",
		"/sys/firmware",
	},
	ReadonlyPaths: []string{
		"/proc/sys", "/proc/sysrq-trigger", "/proc/irq", "/proc/bus",
	},
	Devices:  configs.DefaultAutoCreatedDevices,
	Hostname: "testing",
	Mounts: []*configs.Mount{
		{
			Source:      "proc",
			Destination: "/proc",
			Device:      "proc",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "tmpfs",
			Destination: "/dev",
			Device:      "tmpfs",
			Flags:       syscall.MS_NOSUID | syscall.MS_STRICTATIME,
			Data:        "mode=755",
		},
		{
			Source:      "devpts",
			Destination: "/dev/pts",
			Device:      "devpts",
			Flags:       syscall.MS_NOSUID | syscall.MS_NOEXEC,
			Data:        "newinstance,ptmxmode=0666,mode=0620,gid=5",
		},
		{
			Device:      "tmpfs",
			Source:      "shm",
			Destination: "/dev/shm",
			Data:        "mode=1777,size=65536k",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "mqueue",
			Destination: "/dev/mqueue",
			Device:      "mqueue",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "sysfs",
			Destination: "/sys",
			Device:      "sysfs",
			Flags:       defaultMountFlags | syscall.MS_RDONLY,
		},
	},
	UidMappings: []configs.IDMap{
		{
			ContainerID: 0,
			HostID: 1000,
			Size: 65536,
		},
	},
	GidMappings: []configs.IDMap{
		{
			ContainerID: 0,
			HostID: 1000,
			Size: 65536,
		},
	},
	Networks: []*configs.Network{
		{
			Type:    "loopback",
			Address: "127.0.0.1/0",
			Gateway: "localhost",
		},
	},
	Rlimits: []configs.Rlimit{
		{
			Type: syscall.RLIMIT_NOFILE,
			Hard: uint64(1025),
			Soft: uint64(1025),
		},
	},
}
```

Once you have the configuration populated you can create a container:

```go
container, err := factory.Create("container-id", config)
if err != nil {
	logrus.Fatal(err)
	return
}
```

To spawn bash as the initial process inside the container and have the
processes pid returned in order to wait, signal, or kill the process:

```go
process := &libcontainer.Process{
	Args:   []string{"/bin/bash"},
	Env:    []string{"PATH=/bin"},
	User:   "daemon",
	Stdin:  os.Stdin,
	Stdout: os.Stdout,
	Stderr: os.Stderr,
}

err := container.Run(process)
if err != nil {
	container.Destroy()
	logrus.Fatal(err)
	return
}

// wait for the process to finish.
_, err := process.Wait()
if err != nil {
	logrus.Fatal(err)
}

// destroy the container.
container.Destroy()
```

Additional ways to interact with a running container are:

```go
// return all the pids for all processes running inside the container.
processes, err := container.Processes()

// get detailed cpu, memory, io, and network statistics for the container and
// it's processes.
stats, err := container.Stats()

// pause all processes inside the container.
container.Pause()

// resume all paused processes.
container.Resume()

// send signal to container's init process.
container.Signal(signal)

// update container resource constraints.
container.Set(config)
```


#### Checkpoint & Restore

libcontainer now integrates [CRIU](http://criu.org/) for checkpointing and restoring containers.
This let's you save the state of a process running inside a container to disk, and then restore
that state into a new process, on the same machine or on another machine.

`criu` version 1.5.2 or higher is required to use checkpoint and restore.
If you don't already  have `criu` installed, you can build it from source, following the
[online instructions](http://criu.org/Installation). `criu` is also installed in the docker image
generated when building libcontainer with docker.


## Copyright and license

Code and documentation copyright 2014 Docker, inc. Code released under the Apache 2.0 license.
Docs released under Creative commons.

## nsenter

The `nsenter` package registers a special init constructor that is called before 
the Go runtime has a chance to boot.  This provides us the ability to `setns` on 
existing namespaces and avoid the issues that the Go runtime has with multiple 
threads.  This constructor will be called if this package is registered, 
imported, in your go application.

The `nsenter` package will `import "C"` and it uses [cgo](https://golang.org/cmd/cgo/)
package. In cgo, if the import of "C" is immediately preceded by a comment, that comment, 
called the preamble, is used as a header when compiling the C parts of the package.
So every time we  import package `nsenter`, the C code function `nsexec()` would be 
called. And package `nsenter` is now only imported in `main_unix.go`, so every time
before we call `cmd.Start` on linux, that C code would run.

Because `nsexec()` must be run before the Go runtime in order to use the
Linux kernel namespace, you must `import` this library into a package if
you plan to use `libcontainer` directly. Otherwise Go will not execute
the `nsexec()` constructor, which means that the re-exec will not cause
the namespaces to be joined. You can import it like this:

```go
import _ "github.com/opencontainers/runc/libcontainer/nsenter"
```

`nsexec()` will first get the file descriptor number for the init pipe
from the environment variable `_LIBCONTAINER_INITPIPE` (which was opened
by the parent and kept open across the fork-exec of the `nsexec()` init
process). The init pipe is used to read bootstrap data (namespace paths,
clone flags, uid and gid mappings, and the console path) from the parent
process. `nsexec()` will then call `setns(2)` to join the namespaces
provided in the bootstrap data (if available), `clone(2)` a child process
with the provided clone flags, update the user and group ID mappings, do
some further miscellaneous setup steps, and then send the PID of the
child process to the parent of the `nsexec()` "caller". Finally,
the parent `nsexec()` will exit and the child `nsexec()` process will
return to allow the Go runtime take over.

NOTE: We do both `setns(2)` and `clone(2)` even if we don't have any
CLONE_NEW* clone flags because we must fork a new process in order to
enter the PID namespace.



# go-digest

[![GoDoc](https://godoc.org/github.com/opencontainers/go-digest?status.svg)](https://godoc.org/github.com/opencontainers/go-digest) [![Go Report Card](https://goreportcard.com/badge/github.com/opencontainers/go-digest)](https://goreportcard.com/report/github.com/opencontainers/go-digest) [![Build Status](https://travis-ci.org/opencontainers/go-digest.svg?branch=master)](https://travis-ci.org/opencontainers/go-digest)

Common digest package used across the container ecosystem.

Please see the [godoc](https://godoc.org/github.com/opencontainers/go-digest) for more information.

# What is a digest?

A digest is just a hash.

The most common use case for a digest is to create a content
identifier for use in [Content Addressable Storage](https://en.wikipedia.org/wiki/Content-addressable_storage)
systems:

```go
id := digest.FromBytes([]byte("my content"))
```

In the example above, the id can be used to uniquely identify 
the byte slice "my content". This allows two disparate applications
to agree on a verifiable identifier without having to trust one
another.

An identifying digest can be verified, as follows:

```go
if id != digest.FromBytes([]byte("my content")) {
  return errors.New("the content has changed!")
}
```

A `Verifier` type can be used to handle cases where an `io.Reader`
makes more sense:

```go
rd := getContent()
verifier := id.Verifier()
io.Copy(verifier, rd)

if !verifier.Verified() {
  return errors.New("the content has changed!")
}
```

Using [Merkle DAGs](https://en.wikipedia.org/wiki/Merkle_tree), this
can power a rich, safe, content distribution system.

# Usage

While the [godoc](https://godoc.org/github.com/opencontainers/go-digest) is
considered the best resource, a few important items need to be called 
out when using this package.

1. Make sure to import the hash implementations into your application
    or the package will panic. You should have something like the 
    following in the main (or other entrypoint) of your application:
   
    ```go
    import (
        _ "crypto/sha256"
   	    _ "crypto/sha512"
    )
    ```
    This may seem inconvenient but it allows you replace the hash 
    implementations with others, such as https://github.com/stevvooe/resumable.
 
2. Even though `digest.Digest` may be assemable as a string, _always_ 
    verify your input with `digest.Parse` or use `Digest.Validate`
    when accepting untrusted input. While there are measures to 
    avoid common problems, this will ensure you have valid digests
    in the rest of your application.

# Stability

The Go API, at this stage, is considered stable, unless otherwise noted.

As always, before using a package export, read the [godoc](https://godoc.org/github.com/opencontainers/go-digest).

# Contributing

This package is considered fairly complete. It has been in production
in thousands (millions?) of deployments and is fairly battle-hardened.
New additions will be met with skepticism. If you think there is a 
missing feature, please file a bug clearly describing the problem and 
the alternatives you tried before submitting a PR.

# Reporting security issues

The maintainers take security seriously. If you discover a security 
issue, please bring it to their attention right away!

Please DO NOT file a public issue, instead send your report privately
to security@docker.com.

Security reports are greatly appreciated and we will publicly thank you 
for it. We also like to send gifts—if you're into Docker schwag, make 
sure to let us know. We currently do not offer a paid security bounty 
program, but are not ruling it out in the future.

# Copyright and license

Copyright © 2016 Docker, Inc. All rights reserved, except as follows. Code is released under the [Apache 2.0 license](LICENSE.code). This `README.md` file and the [`CONTRIBUTING.md`](CONTRIBUTING.md) file are licensed under the Creative Commons Attribution 4.0 International License under the terms and conditions set forth in the file [`LICENSE.docs`](LICENSE.docs). You may obtain a duplicate copy of the same license, titled CC BY-SA 4.0, at http://creativecommons.org/licenses/by-sa/4.0/.
mux
===
[![Build Status](https://travis-ci.org/gorilla/mux.png?branch=master)](https://travis-ci.org/gorilla/mux)

gorilla/mux is a powerful URL router and dispatcher.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/mux
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

gorilla/context is a general purpose registry for global request variables.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
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
Package untar provides helper function to easily extract contents of a tar
stream to a file system directory. Useful for cases where you'd want a call to
`tar x`.

See [documentation](https://godoc.org/github.com/artyom/untar) for usage and
example command in `cmd/untar` subdirectory.

LICENSE: MIT.
# Overview
This repository provides various Protocol Buffer extensions for the Go
language (golang), namely support for record length-delimited message
streaming.

| Java                           | Go                    |
| ------------------------------ | --------------------- |
| MessageLite#parseDelimitedFrom | pbutil.ReadDelimited  |
| MessageLite#writeDelimitedTo   | pbutil.WriteDelimited |

Because [Code Review 9102043](https://codereview.appspot.com/9102043/) is
destined to never be merged into mainline (i.e., never be promoted to formal
[goprotobuf features](https://github.com/golang/protobuf)), this repository
will live here in the wild.

# Documentation
We have [generated Go Doc documentation](http://godoc.org/github.com/matttproud/golang_protobuf_extensions/pbutil) here.

# Testing
[![Build Status](https://travis-ci.org/matttproud/golang_protobuf_extensions.png?branch=master)](https://travis-ci.org/matttproud/golang_protobuf_extensions)
# buffruneio

[![Tests Status](https://travis-ci.org/pelletier/go-buffruneio.svg?branch=master)](https://travis-ci.org/pelletier/go-buffruneio)
[![GoDoc](https://godoc.org/github.com/pelletier/go-buffruneio?status.svg)](https://godoc.org/github.com/pelletier/go-buffruneio)

Buffruneio is a wrapper around bufio to provide buffered runes access with
unlimited unreads.

```go
import "github.com/pelletier/go-buffruneio"
```

## Examples

```go
import (
    "fmt"
    "github.com/pelletier/go-buffruneio"
    "strings"
)

reader := buffruneio.NewReader(strings.NewReader("abcd"))
fmt.Println(reader.ReadRune()) // 'a'
fmt.Println(reader.ReadRune()) // 'b'
fmt.Println(reader.ReadRune()) // 'c'
reader.UnreadRune()
reader.UnreadRune()
fmt.Println(reader.ReadRune()) // 'b'
fmt.Println(reader.ReadRune()) // 'c'
```

## Documentation

The documentation and additional examples are available at
[godoc.org](http://godoc.org/github.com/pelletier/go-buffruneio).

## Contribute

Feel free to report bugs and patches using GitHub's pull requests system on
[pelletier/go-toml](https://github.com/pelletier/go-buffruneio). Any feedback is
much appreciated!

## LICENSE

Copyright (c) 2016 Thomas Pelletier

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# go-toml

Go library for the [TOML](https://github.com/mojombo/toml) format.

This library supports TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

[![GoDoc](https://godoc.org/github.com/pelletier/go-toml?status.svg)](http://godoc.org/github.com/pelletier/go-toml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/goadesign/goa/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/pelletier/go-toml.svg?branch=master)](https://travis-ci.org/pelletier/go-toml)
[![Coverage Status](https://coveralls.io/repos/github/pelletier/go-toml/badge.svg?branch=master)](https://coveralls.io/github/pelletier/go-toml?branch=master)
[![Go Report Card](https://goreportcard.com/badge/github.com/pelletier/go-toml)](https://goreportcard.com/report/github.com/pelletier/go-toml)

## Features

Go-toml provides the following features for using data parsed from TOML documents:

* Load TOML documents from files and string data
* Easily navigate TOML structure using TomlTree
* Line & column position data for all parsed elements
* Query support similar to JSON-Path
* Syntax errors contain line and column numbers

Go-toml is designed to help cover use-cases not covered by reflection-based TOML parsing:

* Semantic evaluation of parsed TOML
* Informing a user of mistakes in the source document, after it has been parsed
* Programatic handling of default values on a case-by-case basis
* Using a TOML document as a flexible data-store

## Import

    import "github.com/pelletier/go-toml"

## Usage

### Example

Say you have a TOML file that looks like this:

```toml
[postgres]
user = "pelletier"
password = "mypassword"
```

Read the username and password like this:

```go
import (
    "fmt"
    "github.com/pelletier/go-toml"
)

config, err := toml.LoadFile("config.toml")
if err != nil {
    fmt.Println("Error ", err.Error())
} else {
    // retrieve data directly
    user := config.Get("postgres.user").(string)
    password := config.Get("postgres.password").(string)

    // or using an intermediate object
    configTree := config.Get("postgres").(*toml.TomlTree)
    user = configTree.Get("user").(string)
    password = configTree.Get("password").(string)
    fmt.Println("User is ", user, ". Password is ", password)

    // show where elements are in the file
    fmt.Println("User position: %v", configTree.GetPosition("user"))
    fmt.Println("Password position: %v", configTree.GetPosition("password"))

    // use a query to gather elements without walking the tree
    results, _ := config.Query("$..[user,password]")
    for ii, item := range results.Values() {
      fmt.Println("Query result %d: %v", ii, item)
    }
}
```

## Documentation

The documentation and additional examples are available at
[godoc.org](http://godoc.org/github.com/pelletier/go-toml).

## Tools

Go-toml provides two handy command line tools:

* `tomll`: Reads TOML files and lint them.

    ```
    go install github.com/pelletier/go-toml/cmd/tomll
    tomll --help
    ```
* `tomljson`: Reads a TOML file and outputs its JSON representation.

    ```
    go install github.com/pelletier/go-toml/cmd/tomjson
    tomljson --help
    ```

## Contribute

Feel free to report bugs and patches using GitHub's pull requests system on
[pelletier/go-toml](https://github.com/pelletier/go-toml). Any feedback would be
much appreciated!

### Run tests

You have to make sure two kind of tests run:

1. The Go unit tests
2. The TOML examples base

You can run both of them using `./test.sh`.

## License

The MIT License (MIT). Read [LICENSE](LICENSE).
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
# HCL

[![GoDoc](https://godoc.org/github.com/hashicorp/hcl?status.png)](https://godoc.org/github.com/hashicorp/hcl) [![Build Status](https://travis-ci.org/hashicorp/hcl.svg?branch=master)](https://travis-ci.org/hashicorp/hcl)

HCL (HashiCorp Configuration Language) is a configuration language built
by HashiCorp. The goal of HCL is to build a structured configuration language
that is both human and machine friendly for use with command-line tools, but
specifically targeted towards DevOps tools, servers, etc.

HCL is also fully JSON compatible. That is, JSON can be used as completely
valid input to a system expecting HCL. This helps makes systems
interoperable with other systems.

HCL is heavily inspired by
[libucl](https://github.com/vstakhov/libucl),
nginx configuration, and others similar.

## Why?

A common question when viewing HCL is to ask the question: why not
JSON, YAML, etc.?

Prior to HCL, the tools we built at [HashiCorp](http://www.hashicorp.com)
used a variety of configuration languages from full programming languages
such as Ruby to complete data structure languages such as JSON. What we
learned is that some people wanted human-friendly configuration languages
and some people wanted machine-friendly languages.

JSON fits a nice balance in this, but is fairly verbose and most
importantly doesn't support comments. With YAML, we found that beginners
had a really hard time determining what the actual structure was, and
ended up guessing more often than not whether to use a hyphen, colon, etc.
in order to represent some configuration key.

Full programming languages such as Ruby enable complex behavior
a configuration language shouldn't usually allow, and also forces
people to learn some set of Ruby.

Because of this, we decided to create our own configuration language
that is JSON-compatible. Our configuration language (HCL) is designed
to be written and modified by humans. The API for HCL allows JSON
as an input so that it is also machine-friendly (machines can generate
JSON instead of trying to generate HCL).

Our goal with HCL is not to alienate other configuration languages.
It is instead to provide HCL as a specialized language for our tools,
and JSON as the interoperability layer.

## Syntax

For a complete grammar, please see the parser itself. A high-level overview
of the syntax and grammar is listed here.

  * Single line comments start with `#` or `//`

  * Multi-line comments are wrapped in `/*` and `*/`. Nested block comments
    are not allowed. A multi-line comment (also known as a block comment)
    terminates at the first `*/` found.

  * Values are assigned with the syntax `key = value` (whitespace doesn't
    matter). The value can be any primitive: a string, number, boolean,
    object, or list.

  * Strings are double-quoted and can contain any UTF-8 characters.
    Example: `"Hello, World"`

  * Multi-line strings start with `<<EOF` at the end of a line, and end
    with `EOF` on its own line ([here documents](https://en.wikipedia.org/wiki/Here_document)).
    Any text may be used in place of `EOF`. Example:
```
<<FOO
hello
world
FOO
```

  * Numbers are assumed to be base 10. If you prefix a number with 0x,
    it is treated as a hexadecimal. If it is prefixed with 0, it is
    treated as an octal. Numbers can be in scientific notation: "1e10".

  * Boolean values: `true`, `false`

  * Arrays can be made by wrapping it in `[]`. Example:
    `["foo", "bar", 42]`. Arrays can contain primitives,
    other arrays, and objects. As an alternative, lists
    of objects can be created with repeated blocks, using
    this structure:

    ```hcl
    service {
        key = "value"
    }

    service {
        key = "value"
    }
    ```

Objects and nested objects are created using the structure shown below:

```
variable "ami" {
    description = "the AMI to use"
}
```
This would be equivalent to the following json:
``` json
{
  "variable": {
      "ami": {
          "description": "the AMI to use"
        }
    }
}
```

## Thanks

Thanks to:

  * [@vstakhov](https://github.com/vstakhov) - The original libucl parser
    and syntax that HCL was based off of.

  * [@fatih](https://github.com/fatih) - The rewritten HCL parser
    in pure Go (no goyacc) and support for a printer.
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
# Color [![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/fatih/color) [![Build Status](http://img.shields.io/travis/fatih/color.svg?style=flat-square)](https://travis-ci.org/fatih/color)



Color lets you use colorized outputs in terms of [ANSI Escape
Codes](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors) in Go (Golang). It
has support for Windows too! The API can be used in several ways, pick one that
suits you.


![Color](http://i.imgur.com/c1JI0lA.png)


## Install

```bash
go get github.com/fatih/color
```

Note that the `vendor` folder is here for stability. Remove the folder if you
already have the dependencies in your GOPATH.

## Examples

### Standard colors

```go
// Print with default helper functions
color.Cyan("Prints text in cyan.")

// A newline will be appended automatically
color.Blue("Prints %s in blue.", "text")

// These are using the default foreground colors
color.Red("We have red")
color.Magenta("And many others ..")

```

### Mix and reuse colors

```go
// Create a new color object
c := color.New(color.FgCyan).Add(color.Underline)
c.Println("Prints cyan text with an underline.")

// Or just add them to New()
d := color.New(color.FgCyan, color.Bold)
d.Printf("This prints bold cyan %s\n", "too!.")

// Mix up foreground and background colors, create new mixes!
red := color.New(color.FgRed)

boldRed := red.Add(color.Bold)
boldRed.Println("This will print text in bold red.")

whiteBackground := red.Add(color.BgWhite)
whiteBackground.Println("Red text with white background.")
```

### Use your own output (io.Writer)

```go
// Use your own io.Writer output
color.New(color.FgBlue).Fprintln(myWriter, "blue color!")

blue := color.New(color.FgBlue)
blue.Fprint(writer, "This will print text in blue.")
```

### Custom print functions (PrintFunc)

```go
// Create a custom print function for convenience
red := color.New(color.FgRed).PrintfFunc()
red("Warning")
red("Error: %s", err)

// Mix up multiple attributes
notice := color.New(color.Bold, color.FgGreen).PrintlnFunc()
notice("Don't forget this...")
```

### Custom fprint functions (FprintFunc)

```go
blue := color.New(FgBlue).FprintfFunc()
blue(myWriter, "important notice: %s", stars)

// Mix up with multiple attributes
success := color.New(color.Bold, color.FgGreen).FprintlnFunc()
success(myWriter, "Don't forget this...")
```

### Insert into noncolor strings (SprintFunc)

```go
// Create SprintXxx functions to mix strings with other non-colorized strings:
yellow := color.New(color.FgYellow).SprintFunc()
red := color.New(color.FgRed).SprintFunc()
fmt.Printf("This is a %s and this is %s.\n", yellow("warning"), red("error"))

info := color.New(color.FgWhite, color.BgGreen).SprintFunc()
fmt.Printf("This %s rocks!\n", info("package"))

// Use helper functions
fmt.Println("This", color.RedString("warning"), "should be not neglected.")
fmt.Printf("%v %v\n", color.GreenString("Info:"), "an important message.")

// Windows supported too! Just don't forget to change the output to color.Output
fmt.Fprintf(color.Output, "Windows support: %s", color.GreenString("PASS"))
```

### Plug into existing code

```go
// Use handy standard colors
color.Set(color.FgYellow)

fmt.Println("Existing text will now be in yellow")
fmt.Printf("This one %s\n", "too")

color.Unset() // Don't forget to unset

// You can mix up parameters
color.Set(color.FgMagenta, color.Bold)
defer color.Unset() // Use it in your function

fmt.Println("All text will now be bold magenta.")
```

### Disable color

There might be a case where you want to disable color output (for example to
pipe the standard output of your app to somewhere else). `Color` has support to
disable colors both globally and for single color definition. For example
suppose you have a CLI app and a `--no-color` bool flag. You can easily disable
the color output with:

```go

var flagNoColor = flag.Bool("no-color", false, "Disable color output")

if *flagNoColor {
	color.NoColor = true // disables colorized output
}
```

It also has support for single color definitions (local). You can
disable/enable color output on the fly:

```go
c := color.New(color.FgCyan)
c.Println("Prints cyan text")

c.DisableColor()
c.Println("This is printed without any color")

c.EnableColor()
c.Println("This prints again cyan...")
```

## Todo

* Save/Return previous values
* Evaluate fmt.Formatter interface


## Credits

 * [Fatih Arslan](https://github.com/fatih)
 * Windows support via @mattn: [colorable](https://github.com/mattn/go-colorable)

## License

The MIT License (MIT) - see [`LICENSE.md`](https://github.com/fatih/color/blob/master/LICENSE.md) for more details

# OAI object model [![Build Status](https://ci.vmware.run/api/badges/go-openapi/spec/status.svg)](https://ci.vmware.run/go-openapi/spec) [![Coverage](https://coverage.vmware.run/badges/go-openapi/spec/coverage.svg)](https://coverage.vmware.run/go-openapi/spec) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

[![license](http://img.shields.io/badge/license-Apache%20v2-orange.svg)](https://raw.githubusercontent.com/go-openapi/spec/master/LICENSE) [![GoDoc](https://godoc.org/github.com/go-openapi/spec?status.svg)](http://godoc.org/github.com/go-openapi/spec)

The object model for OpenAPI specification documents# Swagger 2.0 specification schema

This folder contains the Swagger 2.0 specification schema files maintained here:

https://github.com/reverb/swagger-spec/blob/master/schemas/v2.0# Swag [![Build Status](https://ci.vmware.run/api/badges/go-openapi/swag/status.svg)](https://ci.vmware.run/go-openapi/swag) [![Coverage](https://coverage.vmware.run/badges/go-openapi/swag/coverage.svg)](https://coverage.vmware.run/go-openapi/swag) [![Slack Status](https://slackin.goswagger.io/badge.svg)](https://slackin.goswagger.io)

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
![afero logo-sm](https://cloud.githubusercontent.com/assets/173412/11490338/d50e16dc-97a5-11e5-8b12-019a300d0fcb.png)

A FileSystem Abstraction System for Go

[![Build Status](https://travis-ci.org/spf13/afero.svg)](https://travis-ci.org/spf13/afero) [![Build status](https://ci.appveyor.com/api/projects/status/github/spf13/afero?branch=master&svg=true)](https://ci.appveyor.com/project/spf13/afero) [![GoDoc](https://godoc.org/github.com/spf13/afero?status.svg)](https://godoc.org/github.com/spf13/afero) [![Join the chat at https://gitter.im/spf13/afero](https://badges.gitter.im/Dev%20Chat.svg)](https://gitter.im/spf13/afero?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Overview

Afero is an filesystem framework providing a simple, uniform and universal API
interacting with any filesystem, as an abstraction layer providing interfaces,
types and methods. Afero has an exceptionally clean interface and simple design
without needless constructors or initialization methods.

Afero is also a library providing a base set of interoperable backend
filesystems that make it easy to work with afero while retaining all the power
and benefit of the os and ioutil packages.

Afero provides significant improvements over using the os package alone, most
notably the ability to create mock and testing filesystems without relying on the disk.

It is suitable for use in a any situation where you would consider using the OS
package as it provides an additional abstraction that makes it easy to use a
memory backed file system during testing. It also adds support for the http
filesystem for full interoperability.


## Afero Features

* A single consistent API for accessing a variety of filesystems
* Interoperation between a variety of file system types
* A set of interfaces to encourage and enforce interoperability between backends
* An atomic cross platform memory backed file system
* Support for compositional (union) file systems by combining multiple file systems acting as one
* Specialized backends which modify existing filesystems (Read Only, Regexp filtered)
* A set of utility functions ported from io, ioutil & hugo to be afero aware


# Using Afero

Afero is easy to use and easier to adopt.

A few different ways you could use Afero:

* Use the interfaces alone to define you own file system.
* Wrap for the OS packages.
* Define different filesystems for different parts of your application.
* Use Afero for mock filesystems while testing

## Step 1: Install Afero

First use go get to install the latest version of the library.

    $ go get github.com/spf13/afero

Next include Afero in your application.
```go
import "github.com/spf13/afero"
```

## Step 2: Declare a backend

First define a package variable and set it to a pointer to a filesystem.
```go
var AppFs afero.Fs = afero.NewMemMapFs()

or

var AppFs afero.Fs = afero.NewOsFs()
```
It is important to note that if you repeat the composite literal you
will be using a completely new and isolated filesystem. In the case of
OsFs it will still use the same underlying filesystem but will reduce
the ability to drop in other filesystems as desired.

## Step 3: Use it like you would the OS package

Throughout your application use any function and method like you normally
would.

So if my application before had:
```go
os.Open('/tmp/foo')
```
We would replace it with a call to `AppFs.Open('/tmp/foo')`.

`AppFs` being the variable we defined above.


## List of all available functions

File System Methods Available:
```go
Chmod(name string, mode os.FileMode) : error
Chtimes(name string, atime time.Time, mtime time.Time) : error
Create(name string) : File, error
Mkdir(name string, perm os.FileMode) : error
MkdirAll(path string, perm os.FileMode) : error
Name() : string
Open(name string) : File, error
OpenFile(name string, flag int, perm os.FileMode) : File, error
Remove(name string) : error
RemoveAll(path string) : error
Rename(oldname, newname string) : error
Stat(name string) : os.FileInfo, error
```
File Interfaces and Methods Available:
```go
io.Closer
io.Reader
io.ReaderAt
io.Seeker
io.Writer
io.WriterAt

Name() : string
Readdir(count int) : []os.FileInfo, error
Readdirnames(n int) : []string, error
Stat() : os.FileInfo, error
Sync() : error
Truncate(size int64) : error
WriteString(s string) : ret int, err error
```
In some applications it may make sense to define a new package that
simply exports the file system variable for easy access from anywhere.

## Using Afero's utility functions

Afero provides a set of functions to make it easier to use the underlying file systems.
These functions have been primarily ported from io & ioutil with some developed for Hugo.

The afero utilities support all afero compatible backends.

The list of utilities includes:

```go
DirExists(path string) (bool, error)
Exists(path string) (bool, error)
FileContainsBytes(filename string, subslice []byte) (bool, error)
GetTempDir(subPath string) string
IsDir(path string) (bool, error)
IsEmpty(path string) (bool, error)
ReadDir(dirname string) ([]os.FileInfo, error)
ReadFile(filename string) ([]byte, error)
SafeWriteReader(path string, r io.Reader) (err error)
TempDir(dir, prefix string) (name string, err error)
TempFile(dir, prefix string) (f File, err error)
Walk(root string, walkFn filepath.WalkFunc) error
WriteFile(filename string, data []byte, perm os.FileMode) error
WriteReader(path string, r io.Reader) (err error)
```
For a complete list see [Afero's GoDoc](https://godoc.org/github.com/spf13/afero)

They are available under two different approaches to use. You can either call
them directly where the first parameter of each function will be the file
system, or you can declare a new `Afero`, a custom type used to bind these
functions as methods to a given filesystem.

### Calling utilities directly

```go
fs := new(afero.MemMapFs)
f, err := afero.TempFile(fs,"", "ioutil-test")

```

### Calling via Afero

```go
fs := afero.NewMemMapFs
afs := &Afero{Fs: fs}
f, err := afs.TempFile("", "ioutil-test")
```

## Using Afero for Testing

There is a large benefit to using a mock filesystem for testing. It has a
completely blank state every time it is initialized and can be easily
reproducible regardless of OS. You could create files to your heart’s content
and the file access would be fast while also saving you from all the annoying
issues with deleting temporary files, Windows file locking, etc. The MemMapFs
backend is perfect for testing.

* Much faster than performing I/O operations on disk
* Avoid security issues and permissions
* Far more control. 'rm -rf /' with confidence
* Test setup is far more easier to do
* No test cleanup needed

One way to accomplish this is to define a variable as mentioned above.
In your application this will be set to afero.NewOsFs() during testing you
can set it to afero.NewMemMapFs().

It wouldn't be uncommon to have each test initialize a blank slate memory
backend. To do this I would define my `appFS = afero.NewOsFs()` somewhere
appropriate in my application code. This approach ensures that Tests are order
independent, with no test relying on the state left by an earlier test.

Then in my tests I would initialize a new MemMapFs for each test:
```go
func TestExist(t *testing.T) {
	appFS = afero.NewMemMapFs()
	// create test files and directories
	appFS.MkdirAll("src/a", 0755))
	afero.WriteFile(appFS, "src/a/b", []byte("file b"), 0644)
	afero.WriteFile(appFS, "src/c", []byte("file c"), 0644)
	_, err := appFS.Stat("src/c")
	if os.IsNotExist(err) {
        t.Errorf("file \"%s\" does not exist.\n", name)
	}
}

```

# Available Backends

## Operating System Native

### OsFs

The first is simply a wrapper around the native OS calls. This makes it
very easy to use as all of the calls are the same as the existing OS
calls. It also makes it trivial to have your code use the OS during
operation and a mock filesystem during testing or as needed.

```go
appfs := afero.NewOsFs()
appfs.MkdirAll("src/a", 0755))
```

## Memory Backed Storage

### MemMapFs

Afero also provides a fully atomic memory backed filesystem perfect for use in
mocking and to speed up unnecessary disk io when persistence isn’t
necessary. It is fully concurrent and will work within go routines
safely.

```go
mm := afero.NewMemMapFs()
mm.MkdirAll("src/a", 0755))
```

#### InMemoryFile

As part of MemMapFs, Afero also provides an atomic, fully concurrent memory
backed file implementation. This can be used in other memory backed file
systems with ease. Plans are to add a radix tree memory stored file
system using InMemoryFile.

## Network Interfaces

### SftpFs

Afero has experimental support for secure file transfer protocol (sftp). Which can
be used to perform file operations over a encrypted channel.

## Filtering Backends

### BasePathFs

The BasePathFs restricts all operations to a given path within an Fs.
The given file name to the operations on this Fs will be prepended with
the base path before calling the source Fs.

```go
bp := afero.NewBasePathFs(afero.NewOsFs(), "/base/path")
```

### ReadOnlyFs

A thin wrapper around the source Fs providing a read only view.

```go
fs := afero.NewReadOnlyFs(afero.NewOsFs())
_, err := fs.Create("/file.txt")
// err = syscall.EPERM
```

# RegexpFs

A filtered view on file names, any file NOT matching
the passed regexp will be treated as non-existing.
Files not matching the regexp provided will not be created.
Directories are not filtered.

```go
fs := afero.NewRegexpFs(afero.NewMemMapFs(), regexp.MustCompile(`\.txt$`))
_, err := fs.Create("/file.html")
// err = syscall.ENOENT
```

### HttpFs

Afero provides an http compatible backend which can wrap any of the existing
backends.

The Http package requires a slightly specific version of Open which
returns an http.File type.

Afero provides an httpFs file system which satisfies this requirement.
Any Afero FileSystem can be used as an httpFs.

```go
httpFs := afero.NewHttpFs(<ExistingFS>)
fileserver := http.FileServer(httpFs.Dir(<PATH>)))
http.Handle("/", fileserver)
```

## Composite Backends

Afero provides the ability have two filesystems (or more) act as a single
file system.

### CacheOnReadFs

The CacheOnReadFs will lazily make copies of any accessed files from the base
layer into the overlay. Subsequent reads will be pulled from the overlay
directly permitting the request is within the cache duration of when it was
created in the overlay.

If the base filesystem is writeable, any changes to files will be
done first to the base, then to the overlay layer. Write calls to open file
handles like `Write()` or `Truncate()` to the overlay first.

To writing files to the overlay only, you can use the overlay Fs directly (not
via the union Fs).

Cache files in the layer for the given time.Duration, a cache duration of 0
means "forever" meaning the file will not be re-requested from the base ever.

A read-only base will make the overlay also read-only but still copy files
from the base to the overlay when they're not present (or outdated) in the
caching layer.

```go
base := afero.NewOsFs()
layer := afero.NewMemMapFs()
ufs := afero.NewCacheOnReadFs(base, layer, 100 * time.Second)
```

### CopyOnWriteFs()

The CopyOnWriteFs is a read only base file system with a potentially
writeable layer on top.

Read operations will first look in the overlay and if not found there, will
serve the file from the base.

Changes to the file system will only be made in the overlay.

Any attempt to modify a file found only in the base will copy the file to the
overlay layer before modification (including opening a file with a writable
handle).

Removing and Renaming files present only in the base layer is not currently
permitted. If a file is present in the base layer and the overlay, only the
overlay will be removed/renamed.

```go
	base := afero.NewOsFs()
	roBase := afero.NewReadOnlyFs(base)
	ufs := afero.NewCopyOnWriteFs(roBase, afero.NewMemMapFs())

	fh, _ = ufs.Create("/home/test/file2.txt")
	fh.WriteString("This is a test")
	fh.Close()
```

In this example all write operations will only occur in memory (MemMapFs)
leaving the base filesystem (OsFs) untouched.


## Desired/possible backends

The following is a short list of possible backends we hope someone will
implement:

* SSH
* ZIP
* TAR
* S3

# About the project

## What's in the name

Afero comes from the latin roots Ad-Facere.

**"Ad"** is a prefix meaning "to".

**"Facere"** is a form of the root "faciō" making "make or do".

The literal meaning of afero is "to make" or "to do" which seems very fitting
for a library that allows one to make files and directories and do things with them.

The English word that shares the same roots as Afero is "affair". Affair shares
the same concept but as a noun it means "something that is made or done" or "an
object of a particular type".

It's also nice that unlike some of my other libraries (hugo, cobra, viper) it
Googles very well.

## Release Notes

* **0.10.0** 2015.12.10
  * Full compatibility with Windows
  * Introduction of afero utilities
  * Test suite rewritten to work cross platform
  * Normalize paths for MemMapFs
  * Adding Sync to the file interface
  * **Breaking Change** Walk and ReadDir have changed parameter order
  * Moving types used by MemMapFs to a subpackage
  * General bugfixes and improvements
* **0.9.0** 2015.11.05
  * New Walk function similar to filepath.Walk
  * MemMapFs.OpenFile handles O_CREATE, O_APPEND, O_TRUNC
  * MemMapFs.Remove now really deletes the file
  * InMemoryFile.Readdir and Readdirnames work correctly
  * InMemoryFile functions lock it for concurrent access
  * Test suite improvements
* **0.8.0** 2014.10.28
  * First public version
  * Interfaces feel ready for people to build using
  * Interfaces satisfy all known uses
  * MemMapFs passes the majority of the OS test suite
  * OsFs passes the majority of the OS test suite

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors

Names in no particular order:

* [spf13](https://github.com/spf13)
* [jaqx0r](https://github.com/jaqx0r)
* [mbertschler](https://github.com/mbertschler)
* [xor-gate](https://github.com/xor-gate)

## License

Afero is released under the Apache 2.0 license. See
[LICENSE.txt](https://github.com/spf13/afero/blob/master/LICENSE.txt)
![viper logo](https://cloud.githubusercontent.com/assets/173412/10886745/998df88a-8151-11e5-9448-4736db51020d.png)

Go configuration with fangs!

Many Go projects are built using Viper including:

* [Hugo](http://gohugo.io)
* [EMC RexRay](http://rexray.readthedocs.org/en/stable/)
* [Imgur's Incus](https://github.com/Imgur/incus)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)
* [Docker Notary](https://github.com/docker/Notary)
* [BloomApi](https://www.bloomapi.com/)
* [doctl](https://github.com/digitalocean/doctl)

[![Build Status](https://travis-ci.org/spf13/viper.svg)](https://travis-ci.org/spf13/viper) [![Join the chat at https://gitter.im/spf13/viper](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spf13/viper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![GoDoc](https://godoc.org/github.com/spf13/viper?status.svg)](https://godoc.org/github.com/spf13/viper)


## What is Viper?

Viper is a complete configuration solution for go applications including 12 factor apps. It is designed
to work within an application, and can handle all types of configuration needs
and formats. It supports:

* setting defaults
* reading from JSON, TOML, YAML, HCL, and Java properties config files
* live watching and re-reading of config files (optional)
* reading from environment variables
* reading from remote config systems (etcd or Consul), and watching changes
* reading from command line flags
* reading from buffer
* setting explicit values

Viper can be thought of as a registry for all of your applications
configuration needs.

## Why Viper?

When building a modern application, you don’t want to worry about
configuration file formats; you want to focus on building awesome software.
Viper is here to help with that.

Viper does the following for you:

1. Find, load, and unmarshal a configuration file in JSON, TOML, YAML, HCL, or Java properties formats.
2. Provide a mechanism to set default values for your different
   configuration options.
3. Provide a mechanism to set override values for options specified through
   command line flags.
4. Provide an alias system to easily rename parameters without breaking existing
   code.
5. Make it easy to tell the difference between when a user has provided a
   command line or config file which is the same as the default.

Viper uses the following precedence order. Each item takes precedence over the
item below it:

 * explicit call to Set
 * flag
 * env
 * config
 * key/value store
 * default

Viper configuration keys are case insensitive.

## Putting Values into Viper

### Establishing Defaults

A good configuration system will support default values. A default value is not
required for a key, but it's useful in the event that a key hasn’t been set via
config file, environment variable, remote configuration or flag.

Examples:

```go
viper.SetDefault("ContentDir", "content")
viper.SetDefault("LayoutDir", "layouts")
viper.SetDefault("Taxonomies", map[string]string{"tag": "tags", "category": "categories"})
```

### Reading Config Files

Viper requires minimal configuration so it knows where to look for config files.
Viper supports JSON, TOML, YAML, HCL, and Java Properties files. Viper can search multiple paths, but
currently a single Viper instance only supports a single configuration file.
Viper does not default to any configuration search paths leaving defaults decision
to an application.

Here is an example of how to use Viper to search for and read a configuration file.
None of the specific paths are required, but at least one path should be provided
where a configuration file is expected.

```go
viper.SetConfigName("config") // name of config file (without extension)
viper.AddConfigPath("/etc/appname/")   // path to look for the config file in
viper.AddConfigPath("$HOME/.appname")  // call multiple times to add many search paths
viper.AddConfigPath(".")               // optionally look for config in the working directory
err := viper.ReadInConfig() // Find and read the config file
if err != nil { // Handle errors reading the config file
	panic(fmt.Errorf("Fatal error config file: %s \n", err))
}
```

### Watching and re-reading config files

Viper supports the ability to have your application live read a config file while running.

Gone are the days of needing to restart a server to have a config take effect,
viper powered applications can read an update to a config file while running and
not miss a beat.

Simply tell the viper instance to watchConfig.
Optionally you can provide a function for Viper to run each time a change occurs.

**Make sure you add all of the configPaths prior to calling `WatchConfig()`**

```go
		viper.WatchConfig()
		viper.OnConfigChange(func(e fsnotify.Event) {
			fmt.Println("Config file changed:", e.Name)
		})
```

### Reading Config from io.Reader

Viper predefines many configuration sources such as files, environment
variables, flags, and remote K/V store, but you are not bound to them. You can
also implement your own required configuration source and feed it to viper.

```go
viper.SetConfigType("yaml") // or viper.SetConfigType("YAML")

// any approach to require this configuration into your program.
var yamlExample = []byte(`
Hacker: true
name: steve
hobbies:
- skateboarding
- snowboarding
- go
clothing:
  jacket: leather
  trousers: denim
age: 35
eyes : brown
beard: true
`)

viper.ReadConfig(bytes.NewBuffer(yamlExample))

viper.Get("name") // this would be "steve"
```

### Setting Overrides

These could be from a command line flag, or from your own application logic.

```go
viper.Set("Verbose", true)
viper.Set("LogFile", LogFile)
```

### Registering and Using Aliases

Aliases permit a single value to be referenced by multiple keys

```go
viper.RegisterAlias("loud", "Verbose")

viper.Set("verbose", true) // same result as next line
viper.Set("loud", true)   // same result as prior line

viper.GetBool("loud") // true
viper.GetBool("verbose") // true
```

### Working with Environment Variables

Viper has full support for environment variables. This enables 12 factor
applications out of the box. There are four methods that exist to aid working
with ENV:

 * `AutomaticEnv()`
 * `BindEnv(string...) : error`
 * `SetEnvPrefix(string)`
 * `SetEnvReplacer(string...) *strings.Replacer`

_When working with ENV variables, it’s important to recognize that Viper
treats ENV variables as case sensitive._

Viper provides a mechanism to try to ensure that ENV variables are unique. By
using `SetEnvPrefix`, you can tell Viper to use add a prefix while reading from
the environment variables. Both `BindEnv` and `AutomaticEnv` will use this
prefix.

`BindEnv` takes one or two parameters. The first parameter is the key name, the
second is the name of the environment variable. The name of the environment
variable is case sensitive. If the ENV variable name is not provided, then
Viper will automatically assume that the key name matches the ENV variable name,
but the ENV variable is IN ALL CAPS. When you explicitly provide the ENV
variable name, it **does not** automatically add the prefix.

One important thing to recognize when working with ENV variables is that the
value will be read each time it is accessed. Viper does not fix the value when
the `BindEnv` is called.

`AutomaticEnv` is a powerful helper especially when combined with
`SetEnvPrefix`. When called, Viper will check for an environment variable any
time a `viper.Get` request is made. It will apply the following rules. It will
check for a environment variable with a name matching the key uppercased and
prefixed with the `EnvPrefix` if set.

`SetEnvReplacer` allows you to use a `strings.Replacer` object to rewrite Env
keys to an extent. This is useful if you want to use `-` or something in your
`Get()` calls, but want your environmental variables to use `_` delimiters. An
example of using it can be found in `viper_test.go`.

#### Env example

```go
SetEnvPrefix("spf") // will be uppercased automatically
BindEnv("id")

os.Setenv("SPF_ID", "13") // typically done outside of the app

id := Get("id") // 13
```

### Working with Flags

Viper has the ability to bind to flags. Specifically, Viper supports `Pflags`
as used in the [Cobra](https://github.com/spf13/cobra) library.

Like `BindEnv`, the value is not set when the binding method is called, but when
it is accessed. This means you can bind as early as you want, even in an
`init()` function.

The `BindPFlag()` method provides this functionality.

Example:

```go
serverCmd.Flags().Int("port", 1138, "Port to run Application server on")
viper.BindPFlag("port", serverCmd.Flags().Lookup("port"))
```

The use of [pflag](https://github.com/spf13/pflag/) in Viper does not preclude
the use of other packages that use the [flag](https://golang.org/pkg/flag/)
package from the standard library. The pflag package can handle the flags
defined for the flag package by importing these flags. This is accomplished
by a calling a convenience function provided by the pflag package called
AddGoFlagSet().

Example:

```go
package main

import (
	"flag"
	"github.com/spf13/pflag"
)

func main() {
	pflag.CommandLine.AddGoFlagSet(flag.CommandLine)
	pflag.Parse()
    ...
}
```

#### Flag interfaces

Viper provides two Go interfaces to bind other flag systems if you don't use `Pflags`.

`FlagValue` represents a single flag. This is a very simple example on how to implement this interface:

```go
type myFlag struct {}
func (f myFlag) HasChanged() bool { return false }
func (f myFlag) Name() string { return "my-flag-name" }
func (f myFlag) ValueString() string { return "my-flag-value" }
func (f myFlag) ValueType() string { return "string" }
```

Once your flag implements this interface, you can simply tell Viper to bind it:

```go
viper.BindFlagValue("my-flag-name", myFlag{})
```

`FlagValueSet` represents a group of flags. This is a very simple example on how to implement this interface:

```go
type myFlagSet struct {
	flags []myFlag
}

func (f myFlagSet) VisitAll(fn func(FlagValue)) {
	for _, flag := range flags {
		fn(flag)
	}
}
```

Once your flag set implements this interface, you can simply tell Viper to bind it:

```go
fSet := myFlagSet{
	flags: []myFlag{myFlag{}, myFlag{}},
}
viper.BindFlagValues("my-flags", fSet)
```

### Remote Key/Value Store Support

To enable remote support in Viper, do a blank import of the `viper/remote`
package:

`import _ "github.com/spf13/viper/remote"`

Viper will read a config string (as JSON, TOML, YAML or HCL) retrieved from a path
in a Key/Value store such as etcd or Consul.  These values take precedence over
default values, but are overridden by configuration values retrieved from disk,
flags, or environment variables.

Viper uses [crypt](https://github.com/xordataexchange/crypt) to retrieve
configuration from the K/V store, which means that you can store your
configuration values encrypted and have them automatically decrypted if you have
the correct gpg keyring.  Encryption is optional.

You can use remote configuration in conjunction with local configuration, or
independently of it.

`crypt` has a command-line helper that you can use to put configurations in your
K/V store. `crypt` defaults to etcd on http://127.0.0.1:4001.

```bash
$ go get github.com/xordataexchange/crypt/bin/crypt
$ crypt set -plaintext /config/hugo.json /Users/hugo/settings/config.json
```

Confirm that your value was set:

```bash
$ crypt get -plaintext /config/hugo.json
```

See the `crypt` documentation for examples of how to set encrypted values, or
how to use Consul.

### Remote Key/Value Store Example - Unencrypted

```go
viper.AddRemoteProvider("etcd", "http://127.0.0.1:4001","/config/hugo.json")
viper.SetConfigType("json") // because there is no file extension in a stream of bytes, supported extensions are "json", "toml", "yaml", "yml", "properties", "props", "prop"
err := viper.ReadRemoteConfig()
```

### Remote Key/Value Store Example - Encrypted

```go
viper.AddSecureRemoteProvider("etcd","http://127.0.0.1:4001","/config/hugo.json","/etc/secrets/mykeyring.gpg")
viper.SetConfigType("json") // because there is no file extension in a stream of bytes,  supported extensions are "json", "toml", "yaml", "yml", "properties", "props", "prop"
err := viper.ReadRemoteConfig()
```

### Watching Changes in etcd - Unencrypted

```go
// alternatively, you can create a new viper instance.
var runtime_viper = viper.New()

runtime_viper.AddRemoteProvider("etcd", "http://127.0.0.1:4001", "/config/hugo.yml")
runtime_viper.SetConfigType("yaml") // because there is no file extension in a stream of bytes, supported extensions are "json", "toml", "yaml", "yml", "properties", "props", "prop"

// read from remote config the first time.
err := runtime_viper.ReadRemoteConfig()

// unmarshal config
runtime_viper.Unmarshal(&runtime_conf)

// open a goroutine to watch remote changes forever
go func(){
	for {
	    time.Sleep(time.Second * 5) // delay after each request

	    // currently, only tested with etcd support
	    err := runtime_viper.WatchRemoteConfig()
	    if err != nil {
	        log.Errorf("unable to read remote config: %v", err)
	        continue
	    }

	    // unmarshal new config into our runtime config struct. you can also use channel
	    // to implement a signal to notify the system of the changes
	    runtime_viper.Unmarshal(&runtime_conf)
	}
}()
```

## Getting Values From Viper

In Viper, there are a few ways to get a value depending on the value's type.
The following functions and methods exist:

 * `Get(key string) : interface{}`
 * `GetBool(key string) : bool`
 * `GetFloat64(key string) : float64`
 * `GetInt(key string) : int`
 * `GetString(key string) : string`
 * `GetStringMap(key string) : map[string]interface{}`
 * `GetStringMapString(key string) : map[string]string`
 * `GetStringSlice(key string) : []string`
 * `GetTime(key string) : time.Time`
 * `GetDuration(key string) : time.Duration`
 * `IsSet(key string) : bool`

One important thing to recognize is that each Get function will return a zero
value if it’s not found. To check if a given key exists, the `IsSet()` method
has been provided.

Example:
```go
viper.GetString("logfile") // case-insensitive Setting & Getting
if viper.GetBool("verbose") {
    fmt.Println("verbose enabled")
}
```
### Accessing nested keys

The accessor methods also accept formatted paths to deeply nested keys. For
example, if the following JSON file is loaded:

```json
{
    "host": {
        "address": "localhost",
        "port": 5799
    },
    "datastore": {
        "metric": {
            "host": "127.0.0.1",
            "port": 3099
        },
        "warehouse": {
            "host": "198.0.0.1",
            "port": 2112
        }
    }
}

```

Viper can access a nested field by passing a `.` delimited path of keys:

```go
GetString("datastore.metric.host") // (returns "127.0.0.1")
```

This obeys the precedence rules established above; the search for the path
will cascade through the remaining configuration registries until found.

For example, given this configuration file, both `datastore.metric.host` and
`datastore.metric.port` are already defined (and may be overridden). If in addition
`datastore.metric.protocol` was defined in the defaults, Viper would also find it.

However, if `datastore.metric` was overridden (by a flag, an environment variable,
the `Set()` method, …) with an immediate value, then all sub-keys of
`datastore.metric` become undefined, they are “shadowed” by the higher-priority
configuration level.

Lastly, if there exists a key that matches the delimited key path, its value
will be returned instead. E.g.

```json
{
    "datastore.metric.host": "0.0.0.0",
    "host": {
        "address": "localhost",
        "port": 5799
    },
    "datastore": {
        "metric": {
            "host": "127.0.0.1",
            "port": 3099
        },
        "warehouse": {
            "host": "198.0.0.1",
            "port": 2112
        }
    }
}

GetString("datastore.metric.host") // returns "0.0.0.0"
```

### Extract sub-tree

Extract sub-tree from Viper.

For example, `viper` represents:

```json
app:
  cache1:
    max-items: 100
    item-size: 64
  cache2:
    max-items: 200
    item-size: 80
```

After executing:

```go
subv := viper.Sub("app.cache1")
```

`subv` represents:

```json
max-items: 100
item-size: 64
```

Suppose we have:

```go
func NewCache(cfg *Viper) *Cache {...}
```

which creates a cache based on config information formatted as `subv`.
Now it's easy to create these 2 caches separately as:

```go
cfg1 := viper.Sub("app.cache1")
cache1 := NewCache(cfg1)

cfg2 := viper.Sub("app.cache2")
cache2 := NewCache(cfg2)
```

### Unmarshaling

You also have the option of Unmarshaling all or a specific value to a struct, map,
etc.

There are two methods to do this:

 * `Unmarshal(rawVal interface{}) : error`
 * `UnmarshalKey(key string, rawVal interface{}) : error`

Example:

```go
type config struct {
	Port int
	Name string
	PathMap string `mapstructure:"path_map"`
}

var C config

err := Unmarshal(&C)
if err != nil {
	t.Fatalf("unable to decode into struct, %v", err)
}
```

## Viper or Vipers?

Viper comes ready to use out of the box. There is no configuration or
initialization needed to begin using Viper. Since most applications will want
to use a single central repository for their configuration, the viper package
provides this. It is similar to a singleton.

In all of the examples above, they demonstrate using viper in it's singleton
style approach.

### Working with multiple vipers

You can also create many different vipers for use in your application. Each will
have it’s own unique set of configurations and values. Each can read from a
different config file, key value store, etc. All of the functions that viper
package supports are mirrored as methods on a viper.

Example:

```go
x := viper.New()
y := viper.New()

x.SetDefault("ContentDir", "content")
y.SetDefault("ContentDir", "foobar")

//...
```

When working with multiple vipers, it is up to the user to keep track of the
different vipers.

## Q & A

Q: Why not INI files?

A: Ini files are pretty awful. There’s no standard format, and they are hard to
validate. Viper is designed to work with JSON, TOML or YAML files. If someone
really wants to add this feature, I’d be happy to merge it. It’s easy to specify
which formats your application will permit.

Q: Why is it called “Viper”?

A: Viper is designed to be a [companion](http://en.wikipedia.org/wiki/Viper_(G.I._Joe))
to [Cobra](https://github.com/spf13/cobra). While both can operate completely
independently, together they make a powerful pair to handle much of your
application foundation needs.

Q: Why is it called “Cobra”?

A: Is there a better name for a [commander](http://en.wikipedia.org/wiki/Cobra_Commander)?
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
cast
====

Easy and safe casting from one type to another in Go

Don’t Panic! ... Cast

## What is Cast?

Cast is a library to convert between different go types in a consistent and easy way.

Cast provides simple functions to easily convert a number to a string, an
interface into a bool, etc. Cast does this intelligently when an obvious
conversion is possible. It doesn’t make any attempts to guess what you meant,
for example you can only convert a string to an int when it is a string
representation of an int such as “8”. Cast was developed for use in
[Hugo](http://hugo.spf13.com), a website engine which uses YAML, TOML or JSON
for meta data.

## Why use Cast?

When working with dynamic data in Go you often need to cast or convert the data
from one type into another. Cast goes beyond just using type assertion (though
it uses that when possible) to provide a very straightforward and convenient
library.

If you are working with interfaces to handle things like dynamic content
you’ll need an easy way to convert an interface into a given type. This
is the library for you.

If you are taking in data from YAML, TOML or JSON or other formats which lack
full types, then Cast is the library for you.

## Usage

Cast provides a handful of To_____ methods. These methods will always return
the desired type. **If input is provided that will not convert to that type, the
0 or nil value for that type will be returned**.

Cast also provides identical methods To_____E. These return the same result as
the To_____ methods, plus an additional error which tells you if it successfully
converted. Using these methods you can tell the difference between when the
input matched the zero value or when the conversion failed and the zero value
was returned.

The following examples are merely a sample of what is available. Please review
the code for a complete set.

### Example ‘ToString’:

    cast.ToString("mayonegg")         // "mayonegg"
    cast.ToString(8)                  // "8"
    cast.ToString(8.31)               // "8.31"
    cast.ToString([]byte("one time")) // "one time"
    cast.ToString(nil)                // ""

	var foo interface{} = "one more time"
    cast.ToString(foo)                // "one more time"


### Example ‘ToInt’:

    cast.ToInt(8)                  // 8
    cast.ToInt(8.31)               // 8
    cast.ToInt("8")                // 8
    cast.ToInt(true)               // 1
    cast.ToInt(false)              // 0

	var eight interface{} = 8
    cast.ToInt(eight)              // 8
    cast.ToInt(nil)                // 0

![cobra logo](https://cloud.githubusercontent.com/assets/173412/10886352/ad566232-814f-11e5-9cd0-aa101788c117.png)

Cobra is both a library for creating powerful modern CLI applications as well as a program to generate applications and command files.

Many of the most widely used Go projects are built using Cobra including:

* [Kubernetes](http://kubernetes.io/)
* [Hugo](http://gohugo.io)
* [rkt](https://github.com/coreos/rkt)
* [etcd](https://github.com/coreos/etcd)
* [Docker (distribution)](https://github.com/docker/distribution)
* [OpenShift](https://www.openshift.com/)
* [Delve](https://github.com/derekparker/delve)
* [GopherJS](http://www.gopherjs.org/)
* [CockroachDB](http://www.cockroachlabs.com/)
* [Bleve](http://www.blevesearch.com/)
* [ProjectAtomic (enterprise)](http://www.projectatomic.io/)
* [Parse (CLI)](https://parse.com/)
* [GiantSwarm's swarm](https://github.com/giantswarm/cli)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)


[![Build Status](https://travis-ci.org/spf13/cobra.svg "Travis CI status")](https://travis-ci.org/spf13/cobra)
[![CircleCI status](https://circleci.com/gh/spf13/cobra.png?circle-token=:circle-token "CircleCI status")](https://circleci.com/gh/spf13/cobra)
[![GoDoc](https://godoc.org/github.com/spf13/cobra?status.svg)](https://godoc.org/github.com/spf13/cobra) 

![cobra](https://cloud.githubusercontent.com/assets/173412/10911369/84832a8e-8212-11e5-9f82-cc96660a4794.gif)

# Overview

Cobra is a library providing a simple interface to create powerful modern CLI
interfaces similar to git & go tools.

Cobra is also an application that will generate your application scaffolding to rapidly
develop a Cobra-based application.

Cobra provides:
* Easy subcommand-based CLIs: `app server`, `app fetch`, etc.
* Fully POSIX-compliant flags (including short & long versions)
* Nested subcommands
* Global, local and cascading flags
* Easy generation of applications & commands with `cobra create appname` & `cobra add cmdname`
* Intelligent suggestions (`app srver`... did you mean `app server`?)
* Automatic help generation for commands and flags
* Automatic detailed help for `app help [command]`
* Automatic help flag recognition of `-h`, `--help`, etc.
* Automatically generated bash autocomplete for your application
* Automatically generated man pages for your application
* Command aliases so you can change things without breaking them
* The flexibilty to define your own help, usage, etc.
* Optional tight integration with [viper](http://github.com/spf13/viper) for 12-factor apps

Cobra has an exceptionally clean interface and simple design without needless
constructors or initialization methods.

Applications built with Cobra commands are designed to be as user-friendly as
possible. Flags can be placed before or after the command (as long as a
confusing space isn’t provided). Both short and long flags can be used. A
command need not even be fully typed.  Help is automatically generated and
available for the application or for a specific command using either the help
command or the `--help` flag.

# Concepts

Cobra is built on a structure of commands, arguments & flags.

**Commands** represent actions, **Args** are things and **Flags** are modifiers for those actions.

The best applications will read like sentences when used. Users will know how
to use the application because they will natively understand how to use it.

The pattern to follow is
`APPNAME VERB NOUN --ADJECTIVE.`
    or
`APPNAME COMMAND ARG --FLAG`

A few good real world examples may better illustrate this point.

In the following example, 'server' is a command, and 'port' is a flag:

    > hugo server --port=1313

In this command we are telling Git to clone the url bare.

    > git clone URL --bare

## Commands

Command is the central point of the application. Each interaction that
the application supports will be contained in a Command. A command can
have children commands and optionally run an action.

In the example above, 'server' is the command.

A Command has the following structure:

```go
type Command struct {
    Use string // The one-line usage message.
    Short string // The short description shown in the 'help' output.
    Long string // The long message shown in the 'help <this-command>' output.
    Run func(cmd *Command, args []string) // Run runs the command.
}
```

## Flags

A Flag is a way to modify the behavior of a command. Cobra supports
fully POSIX-compliant flags as well as the Go [flag package](https://golang.org/pkg/flag/).
A Cobra command can define flags that persist through to children commands
and flags that are only available to that command.

In the example above, 'port' is the flag.

Flag functionality is provided by the [pflag
library](https://github.com/ogier/pflag), a fork of the flag standard library
which maintains the same interface while adding POSIX compliance.

## Usage

Cobra works by creating a set of commands and then organizing them into a tree.
The tree defines the structure of the application.

Once each command is defined with its corresponding flags, then the
tree is assigned to the commander which is finally executed.

# Installing
Using Cobra is easy. First, use `go get` to install the latest version
of the library. This command will install the `cobra` generator executible
along with the library:

    > go get -v github.com/spf13/cobra/cobra

Next, include Cobra in your application:

```go
import "github.com/spf13/cobra"
```

# Getting Started

While you are welcome to provide your own organization, typically a Cobra based
application will follow the following organizational structure.

```
  ▾ appName/
    ▾ cmd/
        add.go
        your.go
        commands.go
        here.go
      main.go
```

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import "{pathToYourApp}/cmd"

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}
```

## Using the Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

In order to use the cobra command, compile it using the following command:

    > go install github.com/spf13/cobra/cobra

This will create the cobra executable under your go path bin directory!

### cobra init

The `cobra init [yourApp]` command will create your initial application code
for you. It is a very powerful application that will populate your program with
the right structure so you can immediately enjoy all the benefits of Cobra. It
will also automatically apply the license you specify to your application.

Cobra init is pretty smart. You can provide it a full path, or simply a path
similar to what is expected in the import.

```
cobra init github.com/spf13/newAppName
```

### cobra add

Once an application is initialized Cobra can create additional commands for you.
Let's say you created an app and you wanted the following commands for it:

* app serve
* app config
* app config create

In your project directory (where your main.go file is) you would run the following:

```
cobra add serve
cobra add config
cobra add create -p 'configCmd'
```

Once you have run these three commands you would have an app structure that would look like:

```
  ▾ app/
    ▾ cmd/
        serve.go
        config.go
        create.go
      main.go
```

at this point you can run `go run main.go` and it would run your app. `go run
main.go serve`, `go run main.go config`, `go run main.go config create` along
with `go run main.go help serve`, etc would all work.

Obviously you haven't added your own code to these yet, the commands are ready
for you to give them their tasks. Have fun.

### Configuring the cobra generator

The cobra generator will be easier to use if you provide a simple configuration
file which will help you eliminate providing a bunch of repeated information in
flags over and over.

An example ~/.cobra.yaml file:

```yaml
author: Steve Francia <spf@spf13.com>
license: MIT
```

You can specify no license by setting `license` to `none` or you can specify
a custom license:

```yaml
license:
  header: This file is part of {{ .appName }}.
  text: |
    {{ .copyright }}

    This is my license. There are many like it, but this one is mine.
    My license is my best friend. It is my life. I must master it as I must
    master my life.  
```

## Manually implementing Cobra

To manually implement cobra you need to create a bare main.go file and a RootCmd file.
You will optionally provide additional commands as you see fit.

### Create the root command

The root command represents your binary itself.


#### Manually create rootCmd

Cobra doesn't require any special constructors. Simply create your commands.

Ideally you place this in app/cmd/root.go:

```go
var RootCmd = &cobra.Command{
	Use:   "hugo",
	Short: "Hugo is a very fast static site generator",
	Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
	Run: func(cmd *cobra.Command, args []string) {
		// Do Stuff Here
	},
}
```

You will additionally define flags and handle configuration in your init() function.

for example cmd/root.go:

```go
func init() {
	cobra.OnInitialize(initConfig)
	RootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.cobra.yaml)")
	RootCmd.PersistentFlags().StringVarP(&projectBase, "projectbase", "b", "", "base project directory eg. github.com/spf13/")
	RootCmd.PersistentFlags().StringP("author", "a", "YOUR NAME", "Author name for copyright attribution")
	RootCmd.PersistentFlags().StringVarP(&userLicense, "license", "l", "", "Name of license for the project (can provide `licensetext` in config)")
	RootCmd.PersistentFlags().Bool("viper", true, "Use Viper for configuration")
	viper.BindPFlag("author", RootCmd.PersistentFlags().Lookup("author"))
	viper.BindPFlag("projectbase", RootCmd.PersistentFlags().Lookup("projectbase"))
	viper.BindPFlag("useViper", RootCmd.PersistentFlags().Lookup("viper"))
	viper.SetDefault("author", "NAME HERE <EMAIL ADDRESS>")
	viper.SetDefault("license", "apache")
}
```

### Create your main.go

With the root command you need to have your main function execute it.
Execute should be run on the root for clarity, though it can be called on any command.

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import "{pathToYourApp}/cmd"

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}
```


### Create additional commands

Additional commands can be defined and typically are each given their own file
inside of the cmd/ directory.

If you wanted to create a version command you would create cmd/version.go and
populate it with the following:

```go
package cmd

import (
	"github.com/spf13/cobra"
)

func init() {
	RootCmd.AddCommand(versionCmd)
}

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "Print the version number of Hugo",
	Long:  `All software has versions. This is Hugo's`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Hugo Static Site Generator v0.9 -- HEAD")
	},
}
```

### Attach command to its parent


If you notice in the above example we attach the command to its parent. In
this case the parent is the rootCmd. In this example we are attaching it to the
root, but commands can be attached at any level.

```go
RootCmd.AddCommand(versionCmd)
```

### Remove a command from its parent

Removing a command is not a common action in simple programs, but it allows 3rd
parties to customize an existing command tree.

In this example, we remove the existing `VersionCmd` command of an existing
root command, and we replace it with our own version:

```go
mainlib.RootCmd.RemoveCommand(mainlib.VersionCmd)
mainlib.RootCmd.AddCommand(versionCmd)
```

## Working with Flags

Flags provide modifiers to control how the action command operates.

### Assign flags to a command

Since the flags are defined and used in different locations, we need to
define a variable outside with the correct scope to assign the flag to
work with.

```go
var Verbose bool
var Source string
```

There are two different approaches to assign a flag.

### Persistent Flags

A flag can be 'persistent' meaning that this flag will be available to the
command it's assigned to as well as every command under that command. For
global flags, assign a flag as a persistent flag on the root.

```go
RootCmd.PersistentFlags().BoolVarP(&Verbose, "verbose", "v", false, "verbose output")
```

### Local Flags

A flag can also be assigned locally which will only apply to that specific command.

```go
RootCmd.Flags().StringVarP(&Source, "source", "s", "", "Source directory to read from")
```


## Example

In the example below, we have defined three commands. Two are at the top level
and one (cmdTimes) is a child of one of the top commands. In this case the root
is not executable meaning that a subcommand is required. This is accomplished
by not providing a 'Run' for the 'rootCmd'.

We have only defined one flag for a single command.

More documentation about flags is available at https://github.com/spf13/pflag

```go
package main

import (
	"fmt"
	"strings"

	"github.com/spf13/cobra"
)

func main() {

	var echoTimes int

	var cmdPrint = &cobra.Command{
		Use:   "print [string to print]",
		Short: "Print anything to the screen",
		Long: `print is for printing anything back to the screen.
            For many years people have printed back to the screen.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdEcho = &cobra.Command{
		Use:   "echo [string to echo]",
		Short: "Echo anything to the screen",
		Long: `echo is for echoing anything back.
            Echo works a lot like print, except it has a child command.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdTimes = &cobra.Command{
		Use:   "times [# times] [string to echo]",
		Short: "Echo anything to the screen more times",
		Long: `echo things multiple times back to the user by providing
            a count and a string.`,
		Run: func(cmd *cobra.Command, args []string) {
			for i := 0; i < echoTimes; i++ {
				fmt.Println("Echo: " + strings.Join(args, " "))
			}
		},
	}

	cmdTimes.Flags().IntVarP(&echoTimes, "times", "t", 1, "times to echo the input")

	var rootCmd = &cobra.Command{Use: "app"}
	rootCmd.AddCommand(cmdPrint, cmdEcho)
	cmdEcho.AddCommand(cmdTimes)
	rootCmd.Execute()
}
```

For a more complete example of a larger application, please checkout [Hugo](http://gohugo.io/).

## The Help Command

Cobra automatically adds a help command to your application when you have subcommands.
This will be called when a user runs 'app help'. Additionally, help will also
support all other commands as input. Say, for instance, you have a command called
'create' without any additional configuration; Cobra will work when 'app help
create' is called.  Every command will automatically have the '--help' flag added.

### Example

The following output is automatically generated by Cobra. Nothing beyond the
command and flag definitions are needed.

    > hugo help

    hugo is the main command, used to build your Hugo site.

    Hugo is a Fast and Flexible Static Site Generator
    built with love by spf13 and friends in Go.

    Complete documentation is available at http://gohugo.io/.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

    Use "hugo [command] --help" for more information about a command.


Help is just a command like any other. There is no special logic or behavior
around it. In fact, you can provide your own if you want.

### Defining your own help

You can provide your own Help command or your own template for the default command to use.

The default help command is

```go
func (c *Command) initHelp() {
	if c.helpCommand == nil {
		c.helpCommand = &Command{
			Use:   "help [command]",
			Short: "Help about any command",
			Long: `Help provides help for any command in the application.
        Simply type ` + c.Name() + ` help [path to command] for full details.`,
			Run: c.HelpFunc(),
		}
	}
	c.AddCommand(c.helpCommand)
}
```

You can provide your own command, function or template through the following methods:

```go
command.SetHelpCommand(cmd *Command)

command.SetHelpFunc(f func(*Command, []string))

command.SetHelpTemplate(s string)
```

The latter two will also apply to any children commands.

## Usage

When the user provides an invalid flag or invalid command, Cobra responds by
showing the user the 'usage'.

### Example
You may recognize this from the help above. That's because the default help
embeds the usage as part of its output.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

### Defining your own usage
You can provide your own usage function or template for Cobra to use.

The default usage function is:

```go
return func(c *Command) error {
	err := tmpl(c.Out(), c.UsageTemplate(), c)
	return err
}
```

Like help, the function and template are overridable through public methods:

```go
command.SetUsageFunc(f func(*Command) error)

command.SetUsageTemplate(s string)
```

## PreRun or PostRun Hooks

It is possible to run functions before or after the main `Run` function of your command. The `PersistentPreRun` and `PreRun` functions will be executed before `Run`. `PersistentPostRun` and `PostRun` will be executed after `Run`.  The `Persistent*Run` functions will be inherited by children if they do not declare their own.  These functions are run in the following order:

- `PersistentPreRun`
- `PreRun`
- `Run`
- `PostRun`
- `PersistentPostRun`

An example of two commands which use all of these features is below.  When the subcommand is executed, it will run the root command's `PersistentPreRun` but not the root command's `PersistentPostRun`:

```go
package main

import (
	"fmt"

	"github.com/spf13/cobra"
)

func main() {

	var rootCmd = &cobra.Command{
		Use:   "root [sub]",
		Short: "My root command",
		PersistentPreRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PersistentPreRun with args: %v\n", args)
		},
		PreRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PreRun with args: %v\n", args)
		},
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd Run with args: %v\n", args)
		},
		PostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PostRun with args: %v\n", args)
		},
		PersistentPostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PersistentPostRun with args: %v\n", args)
		},
	}

	var subCmd = &cobra.Command{
		Use:   "sub [no options!]",
		Short: "My subcommand",
		PreRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd PreRun with args: %v\n", args)
		},
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd Run with args: %v\n", args)
		},
		PostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd PostRun with args: %v\n", args)
		},
		PersistentPostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd PersistentPostRun with args: %v\n", args)
		},
	}

	rootCmd.AddCommand(subCmd)

	rootCmd.SetArgs([]string{""})
	_ = rootCmd.Execute()
	fmt.Print("\n")
	rootCmd.SetArgs([]string{"sub", "arg1", "arg2"})
	_ = rootCmd.Execute()
}
```


## Alternative Error Handling

Cobra also has functions where the return signature is an error. This allows for errors to bubble up to the top,
providing a way to handle the errors in one location. The current list of functions that return an error is:

* PersistentPreRunE
* PreRunE
* RunE
* PostRunE
* PersistentPostRunE

If you would like to silence the default `error` and `usage` output in favor of your own, you can set `SilenceUsage`
and `SilenceErrors` to `false` on the command. A child command respects these flags if they are set on the parent
command.

**Example Usage using RunE:**

```go
package main

import (
	"errors"
	"log"

	"github.com/spf13/cobra"
)

func main() {
	var rootCmd = &cobra.Command{
		Use:   "hugo",
		Short: "Hugo is a very fast static site generator",
		Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
		RunE: func(cmd *cobra.Command, args []string) error {
			// Do Stuff Here
			return errors.New("some random error")
		},
	}

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}
```

## Suggestions when "unknown command" happens

Cobra will print automatic suggestions when "unknown command" errors happen. This allows Cobra to behave similarly to the `git` command when a typo happens. For example:

```
$ hugo srever
Error: unknown command "srever" for "hugo"

Did you mean this?
        server

Run 'hugo --help' for usage.
```

Suggestions are automatic based on every subcommand registered and use an implementation of [Levenshtein distance](http://en.wikipedia.org/wiki/Levenshtein_distance). Every registered command that matches a minimum distance of 2 (ignoring case) will be displayed as a suggestion.

If you need to disable suggestions or tweak the string distance in your command, use:

```go
command.DisableSuggestions = true
```

or

```go
command.SuggestionsMinimumDistance = 1
```

You can also explicitly set names for which a given command will be suggested using the `SuggestFor` attribute. This allows suggestions for strings that are not close in terms of string distance, but makes sense in your set of commands and for some which you don't want aliases. Example:

```
$ kubectl remove
Error: unknown command "remove" for "kubectl"

Did you mean this?
        delete

Run 'kubectl help' for usage.
```

## Generating Markdown-formatted documentation for your command

Cobra can generate a Markdown-formatted document based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Markdown Docs](doc/md_docs.md).

## Generating man pages for your command

Cobra can generate a man page based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Man Docs](doc/man_docs.md).

## Generating bash completions for your command

Cobra can generate a bash-completion file. If you add more information to your command, these completions can be amazingly powerful and flexible.  Read more about it in [Bash Completions](bash_completions.md).

## Debugging

Cobra provides a ‘DebugFlags’ method on a command which, when called, will print
out everything Cobra knows about the flags for each command.

### Example

```go
command.DebugFlags()
```

## Release Notes
* **0.9.0** June 17, 2014
  * flags can appears anywhere in the args (provided they are unambiguous)
  * --help prints usage screen for app or command
  * Prefix matching for commands
  * Cleaner looking help and usage output
  * Extensive test suite
* **0.8.0** Nov 5, 2013
  * Reworked interface to remove commander completely
  * Command now primary structure
  * No initialization needed
  * Usage & Help templates & functions definable at any level
  * Updated Readme
* **0.7.0** Sept 24, 2013
  * Needs more eyes
  * Test suite
  * Support for automatic error messages
  * Support for help command
  * Support for printing to any io.Writer instead of os.Stderr
  * Support for persistent flags which cascade down tree
  * Ready for integration into Hugo
* **0.1.0** Sept 3, 2013
  * Implement first draft

## Extensions

Libraries for extending Cobra:

* [cmdns](https://github.com/gosuri/cmdns): Enables name spacing a command's immediate children. It provides an alternative way to structure subcommands, similar to `heroku apps:create` and `ovrclk clusters:launch`.

## ToDo
* Launch proper documentation site

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors

Names in no particular order:

* [spf13](https://github.com/spf13),
[eparis](https://github.com/eparis),
[bep](https://github.com/bep), and many more!

## License

Cobra is released under the Apache 2.0 license. See [LICENSE.txt](https://github.com/spf13/cobra/blob/master/LICENSE.txt)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/spf13/cobra/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
jWalterWeatherman
=================

Seamless printing to the terminal (stdout) and logging to a io.Writer
(file) that’s as easy to use as fmt.Println.

![and_that__s_why_you_always_leave_a_note_by_jonnyetc-d57q7um](https://cloud.githubusercontent.com/assets/173412/11002937/ccd01654-847d-11e5-828e-12ebaf582eaf.jpg)
Graphic by [JonnyEtc](http://jonnyetc.deviantart.com/art/And-That-s-Why-You-Always-Leave-a-Note-315311422)

JWW is primarily a wrapper around the excellent standard log library. It
provides a few advantages over using the standard log library alone.

1. Ready to go out of the box. 
2. One library for both printing to the terminal and logging (to files).
3. Really easy to log to either a temp file or a file you specify.


I really wanted a very straightforward library that could seamlessly do
the following things.

1. Replace all the println, printf, etc statements thought my code with
   something more useful
2. Allow the user to easily control what levels are printed to stdout
3. Allow the user to easily control what levels are logged
4. Provide an easy mechanism (like fmt.Println) to print info to the user
   which can be easily logged as well 
5. Due to 2 & 3 provide easy verbose mode for output and logs
6. Not have any unnecessary initialization cruft. Just use it.

# Usage

## Step 1. Use it
Put calls throughout your source based on type of feedback.
No initialization or setup needs to happen. Just start calling things.

Available Loggers are:

 * TRACE
 * DEBUG
 * INFO
 * WARN
 * ERROR
 * CRITICAL
 * FATAL

These each are loggers based on the log standard library and follow the
standard usage. Eg..

```go
    import (
        jww "github.com/spf13/jwalterweatherman"
    )

    ...

    if err != nil {

        // This is a pretty serious error and the user should know about
        // it. It will be printed to the terminal as well as logged under the
        // default thresholds.

        jww.ERROR.Println(err)
    }

    if err2 != nil {
        // This error isn’t going to materially change the behavior of the
        // application, but it’s something that may not be what the user
        // expects. Under the default thresholds, Warn will be logged, but
        // not printed to the terminal. 

        jww.WARN.Println(err2)
    }

    // Information that’s relevant to what’s happening, but not very
    // important for the user. Under the default thresholds this will be
    // discarded.

    jww.INFO.Printf("information %q", response)

```

_Why 7 levels?_

Maybe you think that 7 levels are too much for any application... and you
are probably correct. Just because there are seven levels doesn’t mean
that you should be using all 7 levels. Pick the right set for your needs.
Remember they only have to mean something to your project.

## Step 2. Optionally configure JWW

Under the default thresholds :

 * Debug, Trace & Info goto /dev/null
 * Warn and above is logged (when a log file/io.Writer is provided)
 * Error and above is printed to the terminal (stdout)

### Changing the thresholds

The threshold can be changed at any time, but will only affect calls that
execute after the change was made.

This is very useful if your application has a verbose mode. Of course you
can decide what verbose means to you or even have multiple levels of
verbosity.


```go
    import (
        jww "github.com/spf13/jwalterweatherman"
    )

    if Verbose {
        jww.SetLogThreshold(jww.LevelTrace)
        jww.SetStdoutThreshold(jww.LevelInfo)
    }
```

Note that JWW's own internal output uses log levels as well, so set the log
level before making any other calls if you want to see what it's up to.

### Using a temp log file

JWW conveniently creates a temporary file and sets the log Handle to
a io.Writer created for it. You should call this early in your application
initialization routine as it will only log calls made after it is executed. 
When this option is used, the library will fmt.Println where to find the
log file.

```go
    import (
        jww "github.com/spf13/jwalterweatherman"
    )

    jww.UseTempLogFile("YourAppName") 

```

### Setting a log file

JWW can log to any file you provide a path to (provided it’s writable).
Will only append to this file.


```go
    import (
        jww "github.com/spf13/jwalterweatherman"
    )

    jww.SetLogFile("/path/to/logfile") 

```


# More information

This is an early release. I’ve been using it for a while and this is the
third interface I’ve tried. I like this one pretty well, but no guarantees
that it won’t change a bit.

I wrote this for use in [hugo](http://hugo.spf13.com). If you are looking
for a static website engine that’s super fast please checkout Hugo.
[![GoDoc](https://godoc.org/github.com/docker/go-units?status.svg)](https://godoc.org/github.com/docker/go-units)

# Introduction

go-units is a library to transform human friendly measurements into machine friendly values.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-units) for examples and documentation.

## Copyright and license

Copyright © 2015 Docker, Inc.

go-units is licensed under the Apache License, Version 2.0.
See [LICENSE](LICENSE) for the full text of the license.
# libtrust

Libtrust is library for managing authentication and authorization using public key cryptography.

Authentication is handled using the identity attached to the public key.
Libtrust provides multiple methods to prove possession of the private key associated with an identity.
 - TLS x509 certificates
 - Signature verification
 - Key Challenge

Authorization and access control is managed through a distributed trust graph.
Trust servers are used as the authorities of the trust graph and allow caching portions of the graph for faster access.

## Copyright and license

Code and documentation copyright 2014 Docker, inc. Code released under the Apache 2.0 license.
Docs released under Creative commons.

## Libtrust TLS Config Demo

This program generates key pairs and trust files for a TLS client and server.

To generate the keys, run:

```
$ go run genkeys.go
```

The generated files are:

```
$ ls -l client_data/ server_data/
client_data/:
total 24
-rw-------  1 jlhawn  staff  281 Aug  8 16:21 private_key.json
-rw-r--r--  1 jlhawn  staff  225 Aug  8 16:21 public_key.json
-rw-r--r--  1 jlhawn  staff  275 Aug  8 16:21 trusted_hosts.json

server_data/:
total 24
-rw-r--r--  1 jlhawn  staff  348 Aug  8 16:21 trusted_clients.json
-rw-------  1 jlhawn  staff  281 Aug  8 16:21 private_key.json
-rw-r--r--  1 jlhawn  staff  225 Aug  8 16:21 public_key.json
```

The private key and public key for the client and server are stored in `private_key.json` and `public_key.json`, respectively, and in their respective directories. They are represented as JSON Web Keys: JSON objects which represent either an ECDSA or RSA private key. The host keys trusted by the client are stored in `trusted_hosts.json` and contain a mapping of an internet address, `<HOSTNAME_OR_IP>:<PORT>`, to a JSON Web Key which is a JSON object representing either an ECDSA or RSA public key of the trusted server. The client keys trusted by the server are stored in `trusted_clients.json` and contain an array of JSON objects which contain a comment field which can be used describe the key and a JSON Web Key which is a JSON object representing either an ECDSA or RSA public key of the trusted client.

To start the server, run:

```
$ go run server.go
```

This starts an HTTPS server which listens on `localhost:8888`. The server configures itself with a certificate which is valid for both `localhost` and `127.0.0.1` and uses the key from `server_data/private_key.json`. It accepts connections from clients which present a certificate for a key that it is configured to trust from the `trusted_clients.json` file and returns a simple 'hello' message.

To make a request using the client, run:

```
$ go run client.go
```

This command creates an HTTPS client which makes a GET request to `https://localhost:8888`. The client configures itself with a certificate using the key from `client_data/private_key.json`. It only connects to a server which presents a certificate signed by the key specified for the `localhost:8888` address from `client_data/trusted_hosts.json` and made to be used for the `localhost` hostname. If the connection succeeds, it prints the response from the server.

The file `gencert.go` can be used to generate PEM encoded version of the client key and certificate. If you save them to `key.pem` and `cert.pem` respectively, you can use them with `curl` to test out the server (if it is still running).

```
curl --cert cert.pem --key key.pem -k https://localhost:8888
``` 
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
Docker: the container engine [![Release](https://img.shields.io/github/release/docker/docker.svg)](https://github.com/docker/docker/releases/latest)
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
This package provides helper functions for dealing with strings
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

If you're a *contributor* or aspiring contributor, you should read [CONTRIBUTORS.md](../CONTRIBUTING.md).

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
For enabling experimental features, you need to start the Docker daemon with
`--experimental` flag.
You can also enable the daemon flag via `/etc/docker/daemon.json`. e.g.

```json
{
    "experimental": true
}
```

Then make sure the experimental flag is enabled:

```bash
$ docker version -f '{{.Server.Experimental}}'
true
```

## Current experimental features

 * [External graphdriver plugins](../docs/extend/plugins_graphdriver.md)
 * [Ipvlan Network Drivers](vlan-networks.md)
 * [Docker Stacks and Distributed Application Bundles](docker-stacks-and-bundles.md)
 * [Checkpoint & Restore](checkpoint-restore.md)

## How to comment on an experimental feature

Each feature's documentation includes a list of proposal pull requests or PRs associated with the feature. If you want to comment on or suggest a change to a feature, please add it to the existing feature PR.

Issues or problems with a feature? Inquire for help on the `#docker` IRC channel or on the [Docker Google group](https://groups.google.com/forum/#!forum/docker-user).
[![GoDoc](https://godoc.org/github.com/docker/go-connections?status.svg)](https://godoc.org/github.com/docker/go-connections)

# Introduction

go-connections provides common package to work with network connections.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-connections) for examples and documentation.

## License

go-connections is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
# Google Cloud for Go

[![Build Status](https://travis-ci.org/GoogleCloudPlatform/google-cloud-go.svg?branch=master)](https://travis-ci.org/GoogleCloudPlatform/google-cloud-go)
[![GoDoc](https://godoc.org/cloud.google.com/go?status.svg)](https://godoc.org/cloud.google.com/go)

``` go
import "cloud.google.com/go"
```

Go packages for Google Cloud Platform services.

**NOTE:** These packages are under development, and may occasionally make
backwards-incompatible changes.

**NOTE:** Github repo is a mirror of [https://code.googlesource.com/gocloud](https://code.googlesource.com/gocloud).

## News

_September 8, 2016_

* New clients for some of Google's Machine Learning APIs: Vision, Speech, and
Natural Language.

* Preview version of a new [Stackdriver Logging][cloud-logging] client in
[`cloud.google.com/go/preview/logging`](https://godoc.org/cloud.google.com/go/preview/logging).
This client uses gRPC as its transport layer, and supports log reading, sinks
and metrics. It will replace the current client at `cloud.google.com/go/logging` shortly.

## Supported APIs

Google API                     | Status       | Package
-------------------------------|--------------|-----------------------------------------------------------
[Datastore][cloud-datastore]   | beta         | [`cloud.google.com/go/datastore`][cloud-datastore-ref]
[Storage][cloud-storage]       | beta         | [`cloud.google.com/go/storage`][cloud-storage-ref]
[Pub/Sub][cloud-pubsub]        | experimental | [`cloud.google.com/go/pubsub`][cloud-pubsub-ref]
[Bigtable][cloud-bigtable]     | beta         | [`cloud.google.com/go/bigtable`][cloud-bigtable-ref]
[BigQuery][cloud-bigquery]     | experimental | [`cloud.google.com/go/bigquery`][cloud-bigquery-ref]
[Logging][cloud-logging]       | experimental | [`cloud.google.com/go/logging`][cloud-logging-ref]
[Vision][cloud-vision]         | experimental | [`cloud.google.com/go/vision`][cloud-vision-ref]
[Language][cloud-language]     | experimental | [`cloud.google.com/go/language/apiv1beta1`][cloud-language-ref]
[Speech][cloud-speech]         | experimental | [`cloud.google.com/go/speech/apiv1beta`][cloud-speech-ref]


> **Experimental status**: the API is still being actively developed. As a
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

Manually-configured authorization can be achieved using the
[`golang.org/x/oauth2`](https://godoc.org/golang.org/x/oauth2) package to
create an `oauth2.TokenSource`. This token source can be passed to the `NewClient`
function for the relevant API using a
[`option.WithTokenSource`](https://godoc.org/google.golang.org/api/option#WithTokenSource)
option.

## Google Cloud Datastore [![GoDoc](https://godoc.org/cloud.google.com/go/datastore?status.svg)](https://godoc.org/cloud.google.com/go/datastore)

[Google Cloud Datastore][cloud-datastore] ([docs][cloud-datastore-docs]) is a fully-
managed, schemaless database for storing non-relational data. Cloud Datastore
automatically scales with your users and supports ACID transactions, high availability
of reads and writes, strong consistency for reads and ancestor queries, and eventual
consistency for all other queries.

Follow the [activation instructions][cloud-datastore-activation] to use the Google
Cloud Datastore API with your project.

First create a `datastore.Client` to use throughout your application:

```go
client, err := datastore.NewClient(ctx, "my-project-id")
if err != nil {
	log.Fatalln(err)
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

## Google Cloud Storage [![GoDoc](https://godoc.org/cloud.google.com/go/storage?status.svg)](https://godoc.org/cloud.google.com/go/storage)

[Google Cloud Storage][cloud-storage] ([docs][cloud-storage-docs]) allows you to store
data on Google infrastructure with very high reliability, performance and availability,
and can be used to distribute large data objects to users via direct download.

https://godoc.org/cloud.google.com/go/storage

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

## Google Cloud Pub/Sub [![GoDoc](https://godoc.org/cloud.google.com/go/pubsub?status.svg)](https://godoc.org/cloud.google.com/go/pubsub)

[Google Cloud Pub/Sub][cloud-pubsub] ([docs][cloud-pubsub-docs]) allows you to connect
your services with reliable, many-to-many, asynchronous messaging hosted on Google's
infrastructure. Cloud Pub/Sub automatically scales as you need it and provides a foundation
for building your own robust, global services.

First create a `pubsub.Client` to use throughout your application:

```go
client, err := pubsub.NewClient(ctx, "project-id")
if err != nil {
	log.Fatal(err)
}
```

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
	if err == pubsub.Done {
		break
	}
	if err != nil {
		log.Fatalf("Failed to retrieve message: %v", err)
	}

	fmt.Printf("Message %d: %s\n", i, msg.Data)
	msg.Done(true) // Acknowledge that we've consumed the message.
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
[cloud-storage-docs]: https://cloud.google.com/storage/docs/overview
[cloud-storage-create-bucket]: https://cloud.google.com/storage/docs/cloud-console#_creatingbuckets

[cloud-bigtable]: https://cloud.google.com/bigtable/
[cloud-bigtable-ref]: https://godoc.org/cloud.google.com/go/bigtable

[cloud-bigquery]: https://cloud.google.com/bigquery/
[cloud-bigquery-ref]: https://godoc.org/cloud.google.com/go/bigquery

[cloud-logging]: https://cloud.google.com/logging/
[cloud-logging-ref]: https://godoc.org/cloud.google.com/go/logging

[cloud-vision]: https://cloud.google.com/vision/
[cloud-vision-ref]: https://godoc.org/cloud.google.com/go/vision

[cloud-language]: https://cloud.google.com/natural-language
[cloud-language-ref]: https://godoc.org/cloud.google.com/go/language/apiv1beta1

[cloud-speech]: https://cloud.google.com/speech
[cloud-speech-ref]: https://godoc.org/cloud.google.com/go/speech/apiv1beta1

[default-creds]: https://developers.google.com/identity/protocols/application-default-credentials
Auto-generated pubsub v1 clients
=================================

This package includes auto-generated clients for the pubsub v1 API.

Use the handwritten logging client (in the parent directory,
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
  Use [Google Cloud Storage](https://godoc.org/google.golang.org/cloud/storage) instead.
* `appengine/socket` is not required on App Engine flexible environment / Managed VMs.
  Use the standard `net` package instead.
> temp stuffCONTRIBUTION
-----------------

# Running a development environnement

```bash
# Running Authentication server, Registry, Clair
docker-compose up -d

# Run Any command ex:
go run main.go help
# Or
go run main.go pull registry:5000/wemanity-belgium/ubuntu-git
```
