This repository holds supplementary Go libraries for text processing, many involving Unicode.

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

![Gomega: Ginkgo's Preferred Matcher Library](http://onsi.github.io/gomega/images/gomega.png)

[![Build Status](https://travis-ci.org/onsi/gomega.svg)](https://travis-ci.org/onsi/gomega)

Jump straight to the [docs](http://onsi.github.io/gomega/) to learn about Gomega, including a list of [all available matchers](http://onsi.github.io/gomega/#provided-matchers).

To discuss Gomega and get updates, join the [google group](https://groups.google.com/d/forum/ginkgo-and-gomega).

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

To discuss Ginkgo and get updates, join the [google group](https://groups.google.com/d/forum/ginkgo-and-gomega).

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
Slack API in Go [![GoDoc](https://godoc.org/github.com/nlopes/slack?status.svg)](https://godoc.org/github.com/nlopes/slack) [![Build Status](https://travis-ci.org/nlopes/slack.svg)](https://travis-ci.org/nlopes/slack)
===============

This library supports most if not all of the `api.slack.com` REST
calls, as well as the Real-Time Messaging protocol over websocket, in
a fully managed way.

## Change log

### v0.1.0 - May 28, 2017

This is released before adding context support.
As the used context package is the one from Go 1.7 this will be the last
compatible with Go < 1.7.

Please check [0.1.0](https://github.com/nlopes/slack/releases/tag/v0.1.0)

### CHANGELOG.md

As of this version a [CHANGELOG.md](https://github.com/nlopes/slack/blob/master/README.md) is available. Please visit it for updates. 

## Installing

### *go get*

    $ go get -u github.com/nlopes/slack

## Example

### Getting all groups

```golang
import (
	"fmt"

	"github.com/nlopes/slack"
)

func main() {
	api := slack.New("YOUR_TOKEN_HERE")
	// If you set debugging, it will log all requests to the console
	// Useful when encountering issues
	// api.SetDebug(true)
	groups, err := api.GetGroups(false)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	for _, group := range groups {
		fmt.Printf("ID: %s, Name: %s\n", group.ID, group.Name)
	}
}
```

### Getting User Information

```golang
import (
    "fmt"

    "github.com/nlopes/slack"
)

func main() {
    api := slack.New("YOUR_TOKEN_HERE")
    user, err := api.GetUserInfo("U023BECGF")
    if err != nil {
	    fmt.Printf("%s\n", err)
	    return
    }
    fmt.Printf("ID: %s, Fullname: %s, Email: %s\n", user.ID, user.Profile.RealName, user.Profile.Email)
}
```

## Minimal RTM usage:

See https://github.com/nlopes/slack/blob/master/examples/websocket/websocket.go


## Contributing

You are more than welcome to contribute to this project.  Fork and
make a Pull Request, or create an Issue if you see any problem.

## License

BSD 2 Clause license
