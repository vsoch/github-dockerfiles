some_key_NAME = "wat"
Age = 25
Cats = [ "Cauchy", "Plato" ]
Pi = 3.14
Perfection = [ 6, 28, 496, 8128 ]
DOB = 1987-07-05T05:45:00Z
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
# Storm

[![Join the chat at https://gitter.im/asdine/storm](https://badges.gitter.im/asdine/storm.svg)](https://gitter.im/asdine/storm?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/asdine/storm.svg)](https://travis-ci.org/asdine/storm)
[![GoDoc](https://godoc.org/github.com/asdine/storm?status.svg)](https://godoc.org/github.com/asdine/storm)
[![Go Report Card](https://goreportcard.com/badge/github.com/asdine/storm)](https://goreportcard.com/report/github.com/asdine/storm)

Storm is a simple and powerful toolkit for [BoltDB](https://github.com/boltdb/bolt). Basically, Storm provides indexes, a wide range of methods to store and fetch data, an advanced query system, and much more.

In addition to the examples below, see also the [examples in the GoDoc](https://godoc.org/github.com/asdine/storm#pkg-examples).

## Table of Contents

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:0 orderedList:0 -->

- [Getting Started](#getting-started)
- [Import Storm](#import-storm)
- [Open a database](#open-a-database)
- [Simple CRUD system](#simple-crud-system)
	- [Declare your structures](#declare-your-structures)
	- [Save your object](#save-your-object)
		- [Auto Increment](#auto-increment)
	- [Simple queries](#simple-queries)
		- [Fetch one object](#fetch-one-object)
		- [Fetch multiple objects](#fetch-multiple-objects)
		- [Fetch all objects](#fetch-all-objects)
		- [Fetch all objects sorted by index](#fetch-all-objects-sorted-by-index)
		- [Fetch a range of objects](#fetch-a-range-of-objects)
		- [Skip, Limit and Reverse](#skip-limit-and-reverse)
		- [Delete an object](#delete-an-object)
		- [Update an object](#update-an-object)
		- [Initialize buckets and indexes before saving an object](#initialize-buckets-and-indexes-before-saving-an-object)
		- [Drop a bucket](#drop-a-bucket)
		- [Re-index a bucket](#re-index-a-bucket)
	- [Advanced queries](#advanced-queries)
	- [Transactions](#transactions)
	- [Options](#options)
		- [BoltOptions](#boltoptions)
		- [MarshalUnmarshaler](#marshalunmarshaler)
			- [Provided Codecs](#provided-codecs)
		- [Use existing Bolt connection](#use-existing-bolt-connection)
		- [Batch mode](#batch-mode)
- [Nodes and nested buckets](#nodes-and-nested-buckets)
	- [Node options](#node-options)
- [Simple Key/Value store](#simple-keyvalue-store)
- [BoltDB](#boltdb)
- [Migrations](#migrations)
- [License](#license)
- [Credits](#credits)

<!-- /TOC -->

## Getting Started

```bash
go get -u github.com/asdine/storm
```

## Import Storm

```go
import "github.com/asdine/storm"
```

## Open a database

Quick way of opening a database
```go
db, err := storm.Open("my.db")

defer db.Close()
```

`Open` can receive multiple options to customize the way it behaves. See [Options](#options) below

## Simple CRUD system

### Declare your structures

```go
type User struct {
  ID int // primary key
  Group string `storm:"index"` // this field will be indexed
  Email string `storm:"unique"` // this field will be indexed with a unique constraint
  Name string // this field will not be indexed
  Age int `storm:"index"`
}
```

The primary key can be of any type as long as it is not a zero value. Storm will search for the tag `id`, if not present Storm will search for a field named `ID`.

```go
type User struct {
  ThePrimaryKey string `storm:"id"`// primary key
  Group string `storm:"index"` // this field will be indexed
  Email string `storm:"unique"` // this field will be indexed with a unique constraint
  Name string // this field will not be indexed
}
```

Storm handles tags in nested structures with the `inline` tag

```go
type Base struct {
  Ident bson.ObjectId `storm:"id"`
}

type User struct {
	Base      `storm:"inline"`
	Group     string `storm:"index"`
	Email     string `storm:"unique"`
	Name      string
	CreatedAt time.Time `storm:"index"`
}
```

### Save your object

```go
user := User{
  ID: 10,
  Group: "staff",
  Email: "john@provider.com",
  Name: "John",
  Age: 21,
  CreatedAt: time.Now(),
}

err := db.Save(&user)
// err == nil

user.ID++
err = db.Save(&user)
// err == storm.ErrAlreadyExists
```

That's it.

`Save` creates or updates all the required indexes and buckets, checks the unique constraints and saves the object to the store.

#### Auto Increment

Storm can auto increment integer values so you don't have to worry about that when saving your objects. Also, the new value is automatically inserted in your field.

```go

type Product struct {
	Pk                  int `storm:"id,increment"` // primary key with auto increment
	Name                string
	IntegerField        uint64 `storm:"increment"`
	IndexedIntegerField uint32 `storm:"index,increment"`
	UniqueIntegerField  int16  `storm:"unique,increment=100"` // the starting value can be set
}

p := Product{Name: "Vaccum Cleaner"}

fmt.Println(p.Pk)
fmt.Println(p.IntegerField)
fmt.Println(p.IndexedIntegerField)
fmt.Println(p.UniqueIntegerField)
// 0
// 0
// 0
// 0

_ = db.Save(&p)

fmt.Println(p.Pk)
fmt.Println(p.IntegerField)
fmt.Println(p.IndexedIntegerField)
fmt.Println(p.UniqueIntegerField)
// 1
// 1
// 1
// 100

```

### Simple queries

Any object can be fetched, indexed or not. Storm uses indexes when available, otherwhise it uses the [query system](#advanced-queries).

#### Fetch one object

```go
var user User
err := db.One("Email", "john@provider.com", &user)
// err == nil

err = db.One("Name", "John", &user)
// err == nil

err = db.One("Name", "Jack", &user)
// err == storm.ErrNotFound
```

#### Fetch multiple objects

```go
var users []User
err := db.Find("Group", "staff", &users)
```

#### Fetch all objects

```go
var users []User
err := db.All(&users)
```

#### Fetch all objects sorted by index

```go
var users []User
err := db.AllByIndex("CreatedAt", &users)
```

#### Fetch a range of objects

```go
var users []User
err := db.Range("Age", 10, 21, &users)
```

#### Skip, Limit and Reverse

```go
var users []User
err := db.Find("Group", "staff", &users, storm.Skip(10))
err = db.Find("Group", "staff", &users, storm.Limit(10))
err = db.Find("Group", "staff", &users, storm.Reverse())
err = db.Find("Group", "staff", &users, storm.Limit(10), storm.Skip(10), storm.Reverse())

err = db.All(&users, storm.Limit(10), storm.Skip(10), storm.Reverse())
err = db.AllByIndex("CreatedAt", &users, storm.Limit(10), storm.Skip(10), storm.Reverse())
err = db.Range("Age", 10, 21, &users, storm.Limit(10), storm.Skip(10), storm.Reverse())
```

#### Delete an object

```go
err := db.DeleteStruct(&user)
```

#### Update an object

```go
// Update multiple fields
err := db.Update(&User{ID: 10, Name: "Jack", Age: 45})

// Update a single field
err := db.UpdateField(&User{ID: 10}, "Age", 0)
```

#### Initialize buckets and indexes before saving an object

```go
err := db.Init(&User{})
```

Useful when starting your application

#### Drop a bucket

Using the struct

```go
err := db.Drop(&User)
```

Using the bucket name

```go
err := db.Drop("User")
```

#### Re-index a bucket

```go
err := db.ReIndex(&User{})
```

Useful when the structure has changed

### Advanced queries

For more complex queries, you can use the `Select` method.
`Select` takes any number of [`Matcher`](https://godoc.org/github.com/asdine/storm/q#Matcher) from the [`q`](https://godoc.org/github.com/asdine/storm/q) package.

Here are some common Matchers:

```go
// Equality
q.Eq("Name", John)

// Strictly greater than
q.Gt("Age", 7)

// Lesser than or equal to
q.Lte("Age", 77)

// Regex with name that starts with the letter D
q.Re("Name", "^D")

// In the given slice of values
q.In("Group", []string{"Staff", "Admin"})
```

Matchers can also be combined with `And`, `Or` and `Not`:

```go

// Match if all match
q.And(
  q.Gt("Age", 7),
  q.Re("Name", "^D")
)

// Match if one matches
q.Or(
  q.Re("Name", "^A"),
  q.Not(
    q.Re("Name", "^B")
  ),
  q.Re("Name", "^C"),
  q.In("Group", []string{"Staff", "Admin"}),
  q.And(
    q.StrictEq("Password", []byte(password)),
    q.Eq("Registered", true)
  )
)
```

You can find the complete list in the [documentation](https://godoc.org/github.com/asdine/storm/q#Matcher).

`Select` takes any number of matchers and wraps them into a `q.And()` so it's not necessary to specify it. It returns a [`Query`](https://godoc.org/github.com/asdine/storm#Query) type.

```go
query := db.Select(q.Gte("Age", 7), q.Lte("Age", 77))
```

The `Query` type contains methods to filter and order the records.

```go
// Limit
query = query.Limit(10)

// Skip
query = query.Skip(20)

// Calls can also be chained
query = query.Limit(10).Skip(20).OrderBy("Age").Reverse()
```

But also to specify how to fetch them.

```go
var users []User
err = query.Find(&users)

var user User
err = query.First(&user)
```

Examples with `Select`:

```go
// Find all users with an ID between 10 and 100
err = db.Select(q.Gte("ID", 10), q.Lte("ID", 100)).Find(&users)

// Nested matchers
err = db.Select(q.Or(
  q.Gt("ID", 50),
  q.Lt("Age", 21),
  q.And(
    q.Eq("Group", "admin"),
    q.Gte("Age", 21),
  ),
)).Find(&users)

query := db.Select(q.Gte("ID", 10), q.Lte("ID", 100)).Limit(10).Skip(5).Reverse().OrderBy("Age")

// Find multiple records
err = query.Find(&users)
// or
err = db.Select(q.Gte("ID", 10), q.Lte("ID", 100)).Limit(10).Skip(5).Reverse().OrderBy("Age").Find(&users)

// Find first record
err = query.First(&user)
// or
err = db.Select(q.Gte("ID", 10), q.Lte("ID", 100)).Limit(10).Skip(5).Reverse().OrderBy("Age").First(&user)

// Delete all matching records
err = query.Delete(new(User))

// Fetching records one by one (useful when the bucket contains a lot of records)
query = db.Select(q.Gte("ID", 10),q.Lte("ID", 100)).OrderBy("Age")

err = query.Each(new(User), func(record interface{}) error) {
  u := record.(*User)
  ...
  return nil
}
```

See the [documentation](https://godoc.org/github.com/asdine/storm#Query) for a complete list of methods.

### Transactions

```go
tx, err := db.Begin(true)
if err != nil {
  return err
}
defer tx.Rollback()

accountA.Amount -= 100
accountB.Amount += 100

err = tx.Save(accountA)
if err != nil {
  return err
}

err = tx.Save(accountB)
if err != nil {
  return err
}

return tx.Commit()
```
### Options

Storm options are functions that can be passed when constructing you Storm instance. You can pass it any number of options.

#### BoltOptions

By default, Storm opens a database with the mode `0600` and a timeout of one second.
You can change this behavior by using `BoltOptions`

```go
db, err := storm.Open("my.db", storm.BoltOptions(0600, &bolt.Options{Timeout: 1 * time.Second}))
```

#### MarshalUnmarshaler

To store the data in BoltDB, Storm marshals it in JSON by default. If you wish to change this behavior you can pass a codec that implements [`codec.MarshalUnmarshaler`](https://godoc.org/github.com/asdine/storm/codec#MarshalUnmarshaler) via the [`storm.Codec`](https://godoc.org/github.com/asdine/storm#Codec) option:

```go
db := storm.Open("my.db", storm.Codec(myCodec))
```

##### Provided Codecs

You can easily implement your own `MarshalUnmarshaler`, but Storm comes with built-in support for [JSON](https://godoc.org/github.com/asdine/storm/codec/json) (default), [GOB](https://godoc.org/github.com/asdine/storm/codec/gob),  [Sereal](https://godoc.org/github.com/asdine/storm/codec/sereal) and [Protocol Buffers](https://godoc.org/github.com/asdine/storm/codec/protobuf)

These can be used by importing the relevant package and use that codec to configure Storm. The example below shows all variants (without proper error handling):

```go
import (
	"github.com/asdine/storm"
	"github.com/asdine/storm/codec/gob"
	"github.com/asdine/storm/codec/json"
	"github.com/asdine/storm/codec/sereal"
	"github.com/asdine/storm/codec/protobuf"
)

var gobDb, _ = storm.Open("gob.db", storm.Codec(gob.Codec))
var jsonDb, _ = storm.Open("json.db", storm.Codec(json.Codec))
var serealDb, _ = storm.Open("sereal.db", storm.Codec(sereal.Codec))
var protobufDb, _ = storm.Open("protobuf.db", storm.Codec(protobuf.Codec))
```

**Tip**: Adding Storm tags to generated Protobuf files can be tricky. A good solution is to use [this tool](https://github.com/favadi/protoc-go-inject-tag) to inject the tags during the compilation.

#### Use existing Bolt connection

You can use an existing connection and pass it to Storm

```go
bDB, _ := bolt.Open(filepath.Join(dir, "bolt.db"), 0600, &bolt.Options{Timeout: 10 * time.Second})
db := storm.Open("my.db", storm.UseDB(bDB))
```

#### Batch mode

Batch mode can be enabled to speed up concurrent writes (see [Batch read-write transactions](https://github.com/boltdb/bolt#batch-read-write-transactions))

```go
db := storm.Open("my.db", storm.Batch())
```

## Nodes and nested buckets

Storm takes advantage of BoltDB nested buckets feature by using `storm.Node`.
A `storm.Node` is the underlying object used by `storm.DB` to manipulate a bucket.
To create a nested bucket and use the same API as `storm.DB`, you can use the `DB.From` method.

```go
repo := db.From("repo")

err := repo.Save(&Issue{
  Title: "I want more features",
  Author: user.ID,
})

err = repo.Save(newRelease("0.10"))

var issues []Issue
err = repo.Find("Author", user.ID, &issues)

var release Release
err = repo.One("Tag", "0.10", &release)
```

You can also chain the nodes to create a hierarchy

```go
chars := db.From("characters")
heroes := chars.From("heroes")
enemies := chars.From("enemies")

items := db.From("items")
potions := items.From("consumables").From("medicine").From("potions")
```

You can even pass the entire hierarchy as arguments to `From`:

```go
privateNotes := db.From("notes", "private")
workNotes :=  db.From("notes", "work")
```

### Node options

A Node can also be configured. Activating an option on a Node creates a copy, so a Node is always thread-safe.

```go
n := db.From("my-node")
```

Give a bolt.Tx transaction to the Node
```go
n = n.WithTransaction(tx)
```

Enable batch mode
```go
n = n.WithBatch(true)
```

Use a Codec
```go
n = n.WithCodec(gob.Codec)
```

## Simple Key/Value store

Storm can be used as a simple, robust, key/value store that can store anything.
The key and the value can be of any type as long as the key is not a zero value.

Saving data :
```go
db.Set("logs", time.Now(), "I'm eating my breakfast man")
db.Set("sessions", bson.NewObjectId(), &someUser)
db.Set("weird storage", "754-3010", map[string]interface{}{
  "hair": "blonde",
  "likes": []string{"cheese", "star wars"},
})
```

Fetching data :
```go
user := User{}
db.Get("sessions", someObjectId, &user)

var details map[string]interface{}
db.Get("weird storage", "754-3010", &details)

db.Get("sessions", someObjectId, &details)
```

Deleting data :
```go
db.Delete("sessions", someObjectId)
db.Delete("weird storage", "754-3010")
```

## BoltDB

BoltDB is still easily accessible and can be used as usual

```go
db.Bolt.View(func(tx *bolt.Tx) error {
  bucket := tx.Bucket([]byte("my bucket"))
  val := bucket.Get([]byte("any id"))
  fmt.Println(string(val))
  return nil
})
```

A transaction can be also be passed to Storm

```go
db.Bolt.Update(func(tx *bolt.Tx) error {
  ...
  dbx := db.WithTransaction(tx)
  err = dbx.Save(&user)
  ...
  return nil
})
```

## Migrations

You can use the migration tool to migrate databases that use older version of Storm.
See this [README](https://github.com/asdine/storm-migrator) for more informations.

## License

MIT

## Credits

- [Asdine El Hrychy](https://github.com/asdine)
- [Bjørn Erik Pedersen](https://github.com/bep)
[![GoDoc](https://godoc.org/github.com/emirpasic/gods?status.svg)](https://godoc.org/github.com/emirpasic/gods) [![Build Status](https://travis-ci.org/emirpasic/gods.svg)](https://travis-ci.org/emirpasic/gods) [![Go Report Card](https://goreportcard.com/badge/github.com/emirpasic/gods)](https://goreportcard.com/report/github.com/emirpasic/gods) [![PyPI](https://img.shields.io/pypi/l/Django.svg?maxAge=2592000)](https://github.com/emirpasic/gods/blob/master/LICENSE)

# GoDS (Go Data Structures)

Implementation of various data structures and algorithms in Go.

## Data Structures

- [Containers](#containers)
  - [Lists](#lists)
    - [ArrayList](#arraylist)
    - [SinglyLinkedList](#singlylinkedlist)
    - [DoublyLinkedList](#doublylinkedlist)
  - [Sets](#sets)
    - [HashSet](#hashset)
    - [TreeSet](#treeset)
  - [Stacks](#stacks)
    - [LinkedListStack](#linkedliststack)
    - [ArrayStack](#arraystack)
  - [Maps](#maps)
    - [HashMap](#hashmap)
    - [TreeMap](#treemap)
    - [HashBidiMap](#hashbidimap)
    - [TreeBidiMap](#treebidimap)
  - [Trees](#trees)
    - [RedBlackTree](#redblacktree)
    - [AVLTree](#avltree)
    - [BTree](#btree)
    - [BinaryHeap](#binaryheap)
- [Functions](#functions)
    - [Comparator](#comparator)
    - [Iterator](#iterator)
      - [IteratorWithIndex](#iteratorwithindex)
      - [IteratorWithKey](#iteratorwithkey)
      - [ReverseIteratorWithIndex](#reverseiteratorwithindex)
      - [ReverseIteratorWithKey](#reverseiteratorwithkey)
    - [Enumerable](#enumerable)
      - [EnumerableWithIndex](#enumerablewithindex)
      - [EnumerableWithKey](#enumerablewithkey)
    - [Serialization](#serialization)
      - [JSONSerializer](#jsonserializer)
      - [JSONDeserializer](#jsondeserializer)
    - [Sort](#sort)
    - [Container](#container)
- [Appendix](#appendix)


## Containers

All data structures implement the container interface with the following methods:

```go
type Container interface {
	Empty() bool
	Size() int
	Clear()
	Values() []interface{}
}
```

Containers are either ordered or unordered. All ordered containers provide [stateful iterators](#iterator) and some of them allow [enumerable functions](#enumerable).

| Container | Ordered | [Iterator](#iterator) | [Enumerable](#enumerable) | Referenced by |
| :--- | :---: | :---: | :---: | :---: |
| [ArrayList](#arraylist) | yes | yes* | yes | index |
| [SinglyLinkedList](#singlylinkedlist) | yes | yes | yes | index |
| [DoublyLinkedList](#doublylinkedlist) | yes | yes* | yes | index |
| [HashSet](#hashset) | no | no | no | index |
| [TreeSet](#treeset) | yes | yes* | yes | index |
| [LinkedListStack](#linkedliststack) | yes | yes | no | index |
| [ArrayStack](#arraystack) | yes | yes* | no | index |
| [HashMap](#hashmap) | no | no | no | key |
| [TreeMap](#treemap) | yes | yes* | yes | key |
| [HashBidiMap](#hashbidimap) | no | no | no | key* |
| [TreeBidiMap](#treebidimap) | yes | yes* | yes | key* |
| [RedBlackTree](#redblacktree) | yes | yes* | no | key |
| [AVLTree](#avltree) | yes | yes* | no | key |
| [BTree](#btree) | yes | yes* | no | key |
| [BinaryHeap](#binaryheap) | yes | yes* | no | index |
|  |  | <sub><sup>*reversible</sup></sub> |  | <sub><sup>*bidirectional</sup></sub> |

### Lists

A list is a data structure that stores values and may have repeated values.

Implements [Container](#containers) interface.

```go
type List interface {
    Get(index int) (interface{}, bool)
	Remove(index int)
	Add(values ...interface{})
	Contains(values ...interface{}) bool
	Sort(comparator utils.Comparator)
    Swap(index1, index2 int)
   	Insert(index int, values ...interface{})

	containers.Container
	// Empty() bool
	// Size() int
	// Clear()
	// Values() []interface{}
}
```

#### ArrayList

A [list](#lists) backed by a dynamic array that grows and shrinks implicitly.

Implements [List](#lists), [IteratorWithIndex](#iteratorwithindex), [EnumerableWithIndex](#enumerablewithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import (
	"github.com/emirpasic/gods/lists/arraylist"
    "github.com/emirpasic/gods/utils"
)

func main() {
	list := arraylist.New()
	list.Add("a")                         // ["a"]
	list.Add("c", "b")                    // ["a","c","b"]
	list.Sort(utils.StringComparator)     // ["a","b","c"]
	_, _ = list.Get(0)                    // "a",true
	_, _ = list.Get(100)                  // nil,false
	_ = list.Contains("a", "b", "c")      // true
	_ = list.Contains("a", "b", "c", "d") // false
	list.Swap(0, 1)                       // ["b","a",c"]
	list.Remove(2)                        // ["b","a"]
	list.Remove(1)                        // ["b"]
	list.Remove(0)                        // []
	list.Remove(0)                        // [] (ignored)
	_ = list.Empty()                      // true
	_ = list.Size()                       // 0
	list.Add("a")                         // ["a"]
	list.Clear()                          // []
    list.Insert(0, "b")                   // ["b"]
    list.Insert(0, "a")                   // ["a","b"]
}
```

#### SinglyLinkedList

A [list](#lists) where each element points to the next element in the list.

Implements [List](#lists), [IteratorWithIndex](#iteratorwithindex), [EnumerableWithIndex](#enumerablewithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import (
	sll "github.com/emirpasic/gods/lists/singlylinkedlist"
	"github.com/emirpasic/gods/utils"
)

func main() {
	list := sll.New()
	list.Add("a")                         // ["a"]
	list.Add("c", "b")                    // ["a","c","b"]
	list.Sort(utils.StringComparator)     // ["a","b","c"]
	_, _ = list.Get(0)                    // "a",true
	_, _ = list.Get(100)                  // nil,false
	_ = list.Contains("a", "b", "c")      // true
	_ = list.Contains("a", "b", "c", "d") // false
	list.Swap(0, 1)                       // ["b","a",c"]
	list.Remove(2)                        // ["b","a"]
	list.Remove(1)                        // ["b"]
	list.Remove(0)                        // []
	list.Remove(0)                        // [] (ignored)
	_ = list.Empty()                      // true
	_ = list.Size()                       // 0
	list.Add("a")                         // ["a"]
	list.Clear()                          // []
    list.Insert(0, "b")                   // ["b"]
    list.Insert(0, "a")                   // ["a","b"]
}
```

#### DoublyLinkedList

A [list](#lists) where each element points to the next and previous elements in the list.

Implements [List](#lists), [IteratorWithIndex](#iteratorwithindex), [EnumerableWithIndex](#enumerablewithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import (
	dll "github.com/emirpasic/gods/lists/doublylinkedlist"
	"github.com/emirpasic/gods/utils"
)

func main() {
	list := dll.New()
	list.Add("a")                         // ["a"]
	list.Add("c", "b")                    // ["a","c","b"]
	list.Sort(utils.StringComparator)     // ["a","b","c"]
	_, _ = list.Get(0)                    // "a",true
	_, _ = list.Get(100)                  // nil,false
	_ = list.Contains("a", "b", "c")      // true
	_ = list.Contains("a", "b", "c", "d") // false
	list.Swap(0, 1)                       // ["b","a",c"]
	list.Remove(2)                        // ["b","a"]
	list.Remove(1)                        // ["b"]
	list.Remove(0)                        // []
	list.Remove(0)                        // [] (ignored)
	_ = list.Empty()                      // true
	_ = list.Size()                       // 0
	list.Add("a")                         // ["a"]
	list.Clear()                          // []
    list.Insert(0, "b")                   // ["b"]
    list.Insert(0, "a")                   // ["a","b"]
}
```

### Sets

A set is a data structure that can store elements and has no repeated values. It is a computer implementation of the mathematical concept of a finite set. Unlike most other collection types, rather than retrieving a specific element from a set, one typically tests an element for membership in a set. This structure is often used to ensure that no duplicates are present in a container.

Implements [Container](#containers) interface.

```go
type Set interface {
    Add(elements ...interface{})
	Remove(elements ...interface{})
	Contains(elements ...interface{}) bool

	containers.Container
	// Empty() bool
	// Size() int
	// Clear()
	// Values() []interface{}
}
```

#### HashSet

A [set](#sets) backed by a hash table (actually a Go's map). It makes no guarantees as to the iteration order of the set.

Implements [Set](#sets), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import "github.com/emirpasic/gods/sets/hashset"

func main() {
	set := hashset.New()   // empty
	set.Add(1)             // 1
	set.Add(2, 2, 3, 4, 5) // 3, 1, 2, 4, 5 (random order, duplicates ignored)
	set.Remove(4)          // 5, 3, 2, 1 (random order)
	set.Remove(2, 3)       // 1, 5 (random order)
	set.Contains(1)        // true
	set.Contains(1, 5)     // true
	set.Contains(1, 6)     // false
	_ = set.Values()       // []int{5,1} (random order)
	set.Clear()            // empty
	set.Empty()            // true
	set.Size()             // 0
}
```

#### TreeSet

A [set](#sets) backed by a [red-black tree](#redblacktree) to keep the elements ordered with respect to the [comparator](#comparator).

Implements [Set](#sets), [IteratorWithIndex](#iteratorwithindex), [EnumerableWithIndex](#enumerablewithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import "github.com/emirpasic/gods/sets/treeset"

func main() {
	set := treeset.NewWithIntComparator() // empty (keys are of type int)
	set.Add(1)                            // 1
	set.Add(2, 2, 3, 4, 5)                // 1, 2, 3, 4, 5 (in order, duplicates ignored)
	set.Remove(4)                         // 1, 2, 3, 5 (in order)
	set.Remove(2, 3)                      // 1, 5 (in order)
	set.Contains(1)                       // true
	set.Contains(1, 5)                    // true
	set.Contains(1, 6)                    // false
	_ = set.Values()                      // []int{1,5} (in order)
	set.Clear()                           // empty
	set.Empty()                           // true
	set.Size()                            // 0
}
```

### Stacks

A stack that represents a last-in-first-out (LIFO) data structure. The usual push and pop operations are provided, as well as a method to peek at the top item on the stack.

Implements [Container](#containers) interface.

```go
type Stack interface {
	Push(value interface{})
	Pop() (value interface{}, ok bool)
	Peek() (value interface{}, ok bool)

	containers.Container
	// Empty() bool
	// Size() int
	// Clear()
	// Values() []interface{}
}
```

#### LinkedListStack

A [stack](#stacks) based on a [linked list](#singlylinkedlist).

Implements [Stack](#stacks), [IteratorWithIndex](#iteratorwithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import lls "github.com/emirpasic/gods/stacks/linkedliststack"

func main() {
	stack := lls.New()  // empty
	stack.Push(1)       // 1
	stack.Push(2)       // 1, 2
	stack.Values()      // 2, 1 (LIFO order)
	_, _ = stack.Peek() // 2,true
	_, _ = stack.Pop()  // 2, true
	_, _ = stack.Pop()  // 1, true
	_, _ = stack.Pop()  // nil, false (nothing to pop)
	stack.Push(1)       // 1
	stack.Clear()       // empty
	stack.Empty()       // true
	stack.Size()        // 0
}
```

#### ArrayStack

A [stack](#stacks) based on a [array list](#arraylist).

Implements [Stack](#stacks), [IteratorWithIndex](#iteratorwithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import "github.com/emirpasic/gods/stacks/arraystack"

func main() {
	stack := arraystack.New() // empty
	stack.Push(1)             // 1
	stack.Push(2)             // 1, 2
	stack.Values()            // 2, 1 (LIFO order)
	_, _ = stack.Peek()       // 2,true
	_, _ = stack.Pop()        // 2, true
	_, _ = stack.Pop()        // 1, true
	_, _ = stack.Pop()        // nil, false (nothing to pop)
	stack.Push(1)             // 1
	stack.Clear()             // empty
	stack.Empty()             // true
	stack.Size()              // 0
}
```

### Maps

A Map is a data structure that maps keys to values. A map cannot contain duplicate keys and each key can map to at most one value.

Implements [Container](#containers) interface.

```go
type Map interface {
    Put(key interface{}, value interface{})
	Get(key interface{}) (value interface{}, found bool)
	Remove(key interface{})
	Keys() []interface{}

	containers.Container
	// Empty() bool
	// Size() int
	// Clear()
	// Values() []interface{}
}
```

A BidiMap is an extension to the Map. A bidirectional map (BidiMap), also called a hash bag, is an associative data structure in which the key-value pairs form a one-to-one relation. This relation works in both directions by allow the value to also act as a key to key, e.g. a pair (a,b) thus provides a coupling between 'a' and 'b' so that 'b' can be found when 'a' is used as a key and 'a' can be found when 'b' is used as a key.

```go
type BidiMap interface {
	GetKey(value interface{}) (key interface{}, found bool)

	Map
}
```

#### HashMap

A [map](#maps) based on hash tables. Keys are unordered.

Implements [Map](#maps), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import "github.com/emirpasic/gods/maps/hashmap"

func main() {
	m := hashmap.New() // empty
	m.Put(1, "x")      // 1->x
	m.Put(2, "b")      // 2->b, 1->x (random order)
	m.Put(1, "a")      // 2->b, 1->a (random order)
	_, _ = m.Get(2)    // b, true
	_, _ = m.Get(3)    // nil, false
	_ = m.Values()     // []interface {}{"b", "a"} (random order)
	_ = m.Keys()       // []interface {}{1, 2} (random order)
	m.Remove(1)        // 2->b
	m.Clear()          // empty
	m.Empty()          // true
	m.Size()           // 0
}
```

#### TreeMap

A [map](#maps) based on [red-black tree](#redblacktree). Keys are ordered  ordered with respect to the [comparator](#comparator).

Implements [Map](#maps), [IteratorWithKey](#iteratorwithkey), [EnumerableWithKey](#enumerablewithkey), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import "github.com/emirpasic/gods/maps/treemap"

func main() {
	m := treemap.NewWithIntComparator() // empty (keys are of type int)
	m.Put(1, "x")                       // 1->x
	m.Put(2, "b")                       // 1->x, 2->b (in order)
	m.Put(1, "a")                       // 1->a, 2->b (in order)
	_, _ = m.Get(2)                     // b, true
	_, _ = m.Get(3)                     // nil, false
	_ = m.Values()                      // []interface {}{"a", "b"} (in order)
	_ = m.Keys()                        // []interface {}{1, 2} (in order)
	m.Remove(1)                         // 2->b
	m.Clear()                           // empty
	m.Empty()                           // true
	m.Size()                            // 0

    // Other:
    m.Min() // Returns the minimum key and its value from map.
    m.Max() // Returns the maximum key and its value from map.
}
```

#### HashBidiMap

A [map](#maps) based on two hashmaps. Keys are unordered.

Implements [BidiMap](#maps), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import "github.com/emirpasic/gods/maps/hashbidimap"

func main() {
	m := hashbidimap.New() // empty
	m.Put(1, "x")          // 1->x
	m.Put(3, "b")          // 1->x, 3->b (random order)
	m.Put(1, "a")          // 1->a, 3->b (random order)
	m.Put(2, "b")          // 1->a, 2->b (random order)
	_, _ = m.GetKey("a")   // 1, true
	_, _ = m.Get(2)        // b, true
	_, _ = m.Get(3)        // nil, false
	_ = m.Values()         // []interface {}{"a", "b"} (random order)
	_ = m.Keys()           // []interface {}{1, 2} (random order)
	m.Remove(1)            // 2->b
	m.Clear()              // empty
	m.Empty()              // true
	m.Size()               // 0
}
```

#### TreeBidiMap

A [map](#maps) based on red-black tree. This map guarantees that the map will be in both ascending key and value order.  Other than key and value ordering, the goal with this structure is to avoid duplication of elements (unlike in [HashBidiMap](#hashbidimap)), which can be significant if contained elements are large.

Implements [BidiMap](#maps), [IteratorWithKey](#iteratorwithkey), [EnumerableWithKey](#enumerablewithkey), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

```go
package main

import (
	"github.com/emirpasic/gods/maps/treebidimap"
	"github.com/emirpasic/gods/utils"
)

func main() {
	m := treebidimap.NewWith(utils.IntComparator, utils.StringComparator)
	m.Put(1, "x")        // 1->x
	m.Put(3, "b")        // 1->x, 3->b (ordered)
	m.Put(1, "a")        // 1->a, 3->b (ordered)
	m.Put(2, "b")        // 1->a, 2->b (ordered)
	_, _ = m.GetKey("a") // 1, true
	_, _ = m.Get(2)      // b, true
	_, _ = m.Get(3)      // nil, false
	_ = m.Values()       // []interface {}{"a", "b"} (ordered)
	_ = m.Keys()         // []interface {}{1, 2} (ordered)
	m.Remove(1)          // 2->b
	m.Clear()            // empty
	m.Empty()            // true
	m.Size()             // 0
}
```

### Trees

A tree is a widely used data data structure that simulates a hierarchical tree structure, with a root value and subtrees of children, represented as a set of linked nodes; thus no cyclic links.

Implements [Container](#containers) interface.

```go
type Tree interface {
	containers.Container
	// Empty() bool
	// Size() int
	// Clear()
	// Values() []interface{}
}
```

#### RedBlackTree

A red–black [tree](#trees) is a binary search tree with an extra bit of data per node, its color, which can be either red or black. The extra bit of storage ensures an approximately balanced tree by constraining how nodes are colored from any path from the root to the leaf. Thus, it is a data structure which is a type of self-balancing binary search tree.

The balancing of the tree is not perfect but it is good enough to allow it to guarantee searching in O(log n) time, where n is the total number of elements in the tree. The insertion and deletion operations, along with the tree rearrangement and recoloring, are also performed in O(log n) time. <sub><sup>[Wikipedia](http://en.wikipedia.org/wiki/Red%E2%80%93black_tree)</sup></sub>

Implements [Tree](#trees), [ReverseIteratorWithKey](#reverseiteratorwithkey), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

<p align="center"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Red-black_tree_example.svg/500px-Red-black_tree_example.svg.png" width="400px" height="200px" /></p>

```go
package main

import (
	"fmt"
	rbt "github.com/emirpasic/gods/trees/redblacktree"
)

func main() {
	tree := rbt.NewWithIntComparator() // empty (keys are of type int)

	tree.Put(1, "x") // 1->x
	tree.Put(2, "b") // 1->x, 2->b (in order)
	tree.Put(1, "a") // 1->a, 2->b (in order, replacement)
	tree.Put(3, "c") // 1->a, 2->b, 3->c (in order)
	tree.Put(4, "d") // 1->a, 2->b, 3->c, 4->d (in order)
	tree.Put(5, "e") // 1->a, 2->b, 3->c, 4->d, 5->e (in order)
	tree.Put(6, "f") // 1->a, 2->b, 3->c, 4->d, 5->e, 6->f (in order)

	fmt.Println(tree)
	//
	//  RedBlackTree
	//  │           ┌── 6
	//	│       ┌── 5
	//	│   ┌── 4
	//	│   │   └── 3
	//	└── 2
	//		└── 1

	_ = tree.Values() // []interface {}{"a", "b", "c", "d", "e", "f"} (in order)
	_ = tree.Keys()   // []interface {}{1, 2, 3, 4, 5, 6} (in order)

	tree.Remove(2) // 1->a, 3->c, 4->d, 5->e, 6->f (in order)
	fmt.Println(tree)
	//
	//  RedBlackTree
	//  │       ┌── 6
	//  │   ┌── 5
	//  └── 4
	//      │   ┌── 3
	//      └── 1

	tree.Clear() // empty
	tree.Empty() // true
	tree.Size()  // 0

    // Other:
    tree.Left() // gets the left-most (min) node
    tree.Right() // get the right-most (max) node
    tree.Floor(1) // get the floor node
    tree.Ceiling(1) // get the ceiling node
}
```

Extending the red-black tree's functionality  has been demonstrated in the following [example](https://github.com/emirpasic/gods/blob/master/examples/redblacktreeextended.go).

#### AVLTree

AVL [tree](#trees) is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where n is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.

AVL trees are often compared with red–black trees because both support the same set of operations and take O(log n) time for the basic operations. For lookup-intensive applications, AVL trees are faster than red–black trees because they are more strictly balanced. <sub><sup>[Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)</sup></sub>

Implements [Tree](#trees), [ReverseIteratorWithKey](#reverseiteratorwithkey), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/AVL-tree-wBalance_K.svg/262px-AVL-tree-wBalance_K.svg.png" width="300px" height="180px" /><br/><sub>AVL tree with balance factors (green)</sub></p>

```go
package main

import (
	"fmt"
	avl "github.com/emirpasic/gods/trees/avltree"
)

func main() {
	tree := avl.NewWithIntComparator() // empty(keys are of type int)

	tree.Put(1, "x") // 1->x
	tree.Put(2, "b") // 1->x, 2->b (in order)
	tree.Put(1, "a") // 1->a, 2->b (in order, replacement)
	tree.Put(3, "c") // 1->a, 2->b, 3->c (in order)
	tree.Put(4, "d") // 1->a, 2->b, 3->c, 4->d (in order)
	tree.Put(5, "e") // 1->a, 2->b, 3->c, 4->d, 5->e (in order)
	tree.Put(6, "f") // 1->a, 2->b, 3->c, 4->d, 5->e, 6->f (in order)

	fmt.Println(tree)
	//
	//  AVLTree
	//  │       ┌── 6
	//  │   ┌── 5
	//  └── 4
	//      │   ┌── 3
	//      └── 2
	//          └── 1


	_ = tree.Values() // []interface {}{"a", "b", "c", "d", "e", "f"} (in order)
	_ = tree.Keys()   // []interface {}{1, 2, 3, 4, 5, 6} (in order)

	tree.Remove(2) // 1->a, 3->c, 4->d, 5->e, 6->f (in order)
	fmt.Println(tree)
	//
	//  AVLTree
	//  │       ┌── 6
	//  │   ┌── 5
	//  └── 4
	//      └── 3
	//          └── 1

	tree.Clear() // empty
	tree.Empty() // true
	tree.Size()  // 0
}
```

#### BTree

B-tree is a self-balancing tree data structure that keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time. The B-tree is a generalization of a binary search tree in that a node can have more than two children.

According to Knuth's definition, a B-tree of order m is a tree which satisfies the following properties:

- Every node has at most m children.
- Every non-leaf node (except root) has at least ⌈m/2⌉ children.
- The root has at least two children if it is not a leaf node.
- A non-leaf node with k children contains k−1 keys.
- All leaves appear in the same level

Each internal node’s keys act as separation values which divide its subtrees. For example, if an internal node has 3 child nodes (or subtrees) then it must have 2 keys: a1 and a2. All values in the leftmost subtree will be less than a1, all values in the middle subtree will be between a1 and a2, and all values in the rightmost subtree will be greater than a2.<sub><sup>[Wikipedia](http://en.wikipedia.org/wiki/Red%E2%80%93black_tree)</sub></sup>

Implements [Tree](#trees), [ReverseIteratorWithKey](#reverseiteratorwithkey), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/B-tree.svg/831px-B-tree.svg.png" width="400px" height="111px" /></p>

```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/trees/btree"
)

func main() {
	tree := btree.NewWithIntComparator(3) // empty (keys are of type int)

	tree.Put(1, "x") // 1->x
	tree.Put(2, "b") // 1->x, 2->b (in order)
	tree.Put(1, "a") // 1->a, 2->b (in order, replacement)
	tree.Put(3, "c") // 1->a, 2->b, 3->c (in order)
	tree.Put(4, "d") // 1->a, 2->b, 3->c, 4->d (in order)
	tree.Put(5, "e") // 1->a, 2->b, 3->c, 4->d, 5->e (in order)
	tree.Put(6, "f") // 1->a, 2->b, 3->c, 4->d, 5->e, 6->f (in order)
	tree.Put(7, "g") // 1->a, 2->b, 3->c, 4->d, 5->e, 6->f, 7->g (in order)

	fmt.Println(tree)
	// BTree
	//         1
	//     2
	//         3
	// 4
	//         5
	//     6
	//         7

	_ = tree.Values() // []interface {}{"a", "b", "c", "d", "e", "f", "g"} (in order)
	_ = tree.Keys()   // []interface {}{1, 2, 3, 4, 5, 6, 7} (in order)

	tree.Remove(2) // 1->a, 3->c, 4->d, 5->e, 6->f (in order)
	fmt.Println(tree)
	// BTree
	//     1
	//     3
	// 4
	//     5
	//     6

	tree.Clear() // empty
	tree.Empty() // true
	tree.Size()  // 0

	// Other:
	tree.Height() // gets the height of the tree
	tree.Left() // gets the left-most (min) node
	tree.LeftKey() // get the left-most (min) node's key
	tree.LeftValue() // get the left-most (min) node's value
	tree.Right() // get the right-most (max) node
	tree.RightKey() // get the right-most (max) node's key
	tree.RightValue() // get the right-most (max) node's value
}
```

#### BinaryHeap

A binary heap is a [tree](#trees) created using a binary tree. It can be seen as a binary tree with two additional constraints:

- Shape property:

  A binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
- Heap property:

  All nodes are either greater than or equal to or less than or equal to each of its children, according to a comparison predicate defined for the heap. <sub><sup>[Wikipedia](http://en.wikipedia.org/wiki/Binary_heap)</sub></sup>

Implements [Tree](#trees), [ReverseIteratorWithIndex](#reverseiteratorwithindex), [JSONSerializer](#jsonserializer) and [JSONDeserializer](#jsondeserializer) interfaces.

<p align="center"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/501px-Max-Heap.svg.png" width="300px" height="200px" /></p>

```go
package main

import (
	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/emirpasic/gods/utils"
)

func main() {

	// Min-heap
	heap := binaryheap.NewWithIntComparator() // empty (min-heap)
	heap.Push(2)                              // 2
	heap.Push(3)                              // 2, 3
	heap.Push(1)                              // 1, 3, 2
	heap.Values()                             // 1, 3, 2
	_, _ = heap.Peek()                        // 1,true
	_, _ = heap.Pop()                         // 1, true
	_, _ = heap.Pop()                         // 2, true
	_, _ = heap.Pop()                         // 3, true
	_, _ = heap.Pop()                         // nil, false (nothing to pop)
	heap.Push(1)                              // 1
	heap.Clear()                              // empty
	heap.Empty()                              // true
	heap.Size()                               // 0

	// Max-heap
	inverseIntComparator := func(a, b interface{}) int {
		return -utils.IntComparator(a, b)
	}
	heap = binaryheap.NewWith(inverseIntComparator) // empty (min-heap)
	heap.Push(2, 3, 1)                              // 3, 2, 1 (bulk optimized)
	heap.Values()                                   // 3, 2, 1
}
```

## Functions

Various helper functions used throughout the library.

### Comparator

Some data structures (e.g. TreeMap, TreeSet) require a comparator function to automatically keep their elements sorted upon insertion. This comparator is necessary during the initalization.

Comparator is defined as:

Return values (int):

```go
negative , if a < b
zero     , if a == b
positive , if a > b
```

Comparator signature:

```go
type Comparator func(a, b interface{}) int
```

All common comparators for builtin types are included in the library:

```go
func StringComparator(a, b interface{}) int

func IntComparator(a, b interface{}) int

func Int8Comparator(a, b interface{}) int

func Int16Comparator(a, b interface{}) int

func Int32Comparator(a, b interface{}) int

func Int64Comparator(a, b interface{}) int

func UIntComparator(a, b interface{}) int

func UInt8Comparator(a, b interface{}) int

func UInt16Comparator(a, b interface{}) int

func UInt32Comparator(a, b interface{}) int

func UInt64Comparator(a, b interface{}) int

func Float32Comparator(a, b interface{}) int

func Float64Comparator(a, b interface{}) int

func ByteComparator(a, b interface{}) int

func RuneComparator(a, b interface{}) int

func TimeComparator(a, b interface{}) int
```

Writing custom comparators is easy:

```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/sets/treeset"
)

type User struct {
	id   int
	name string
}

// Custom comparator (sort by IDs)
func byID(a, b interface{}) int {

	// Type assertion, program will panic if this is not respected
	c1 := a.(User)
	c2 := b.(User)

	switch {
	case c1.id > c2.id:
		return 1
	case c1.id < c2.id:
		return -1
	default:
		return 0
	}
}

func main() {
	set := treeset.NewWith(byID)

	set.Add(User{2, "Second"})
	set.Add(User{3, "Third"})
	set.Add(User{1, "First"})
	set.Add(User{4, "Fourth"})

	fmt.Println(set) // {1 First}, {2 Second}, {3 Third}, {4 Fourth}
}
```

### Iterator

All ordered containers have stateful iterators. Typically an iterator is obtained by _Iterator()_ function of an ordered container. Once obtained, iterator's _Next()_ function moves the iterator to the next element and returns true if there was a next element. If there was an element, then element's can be obtained by iterator's _Value()_ function. Depending on the ordering type, it's position can be obtained by iterator's _Index()_ or _Key()_ functions. Some containers even provide reversible iterators, essentially the same, but provide another extra _Prev()_ function that moves the iterator to the previous element and returns true if there was a previous element.

Note: it is unsafe to remove elements from container while iterating.

#### IteratorWithIndex

An [iterator](#iterator) whose elements are referenced by an index.

Typical usage:
```go
it := list.Iterator()
for it.Next() {
	index, value := it.Index(), it.Value()
    ...
}
```

Other usages:
```go
if it.First() {
	firstIndex, firstValue := it.Index(), it.Value()
	...
}
```

```go
for it.Begin(); it.Next(); {
	...
}
```

#### IteratorWithKey

An [iterator](#iterator) whose elements are referenced by a key.

Typical usage:
```go
it := tree.Iterator()
for it.Next() {
	key, value := it.Key(), it.Value()
    ...
}
```

Other usages:
```go
if it.First() {
	firstKey, firstValue := it.Key(), it.Value()
	...
}
```

```go
for it.Begin(); it.Next(); {
	...
}
```

#### ReverseIteratorWithIndex

An [iterator](#iterator) whose elements are referenced by an index. Provides all functions as [IteratorWithIndex](#iteratorwithindex), but can also be used for reverse iteration.

Typical usage of iteration in reverse:
```go
it := list.Iterator()
for it.End(); it.Prev(); {
	index, value := it.Index(), it.Value()
    ...
}
```

Other usages:
```go
if it.Last() {
	lastIndex, lastValue := it.Index(), it.Value()
	...
}
```

#### ReverseIteratorWithKey

An [iterator](#iterator) whose elements are referenced by a key. Provides all functions as [IteratorWithKey](#iteratorwithkey), but can also be used for reverse iteration.

Typical usage of iteration in reverse:
```go
it := tree.Iterator()
for it.End(); it.Prev(); {
	key, value := it.Key(), it.Value()
    ...
}
```

Other usages:
```go
if it.Last() {
	lastKey, lastValue := it.Key(), it.Value()
	...
}
```

### Enumerable

Enumerable functions for ordered containers that implement [EnumerableWithIndex](#enumerablewithindex) or [EnumerableWithKey](#enumerablewithkey) interfaces.

#### EnumerableWithIndex

[Enumerable](#enumerable) functions for ordered containers whose values can be fetched by an index.

**Each**

Calls the given function once for each element, passing that element's index and value.

```go
Each(func(index int, value interface{}))
```

**Map**

Invokes the given function once for each element and returns a container containing the values returned by the given function.

```go
Map(func(index int, value interface{}) interface{}) Container
```

**Select**

Returns a new container containing all elements for which the given function returns a true value.

```go
Select(func(index int, value interface{}) bool) Container
```

**Any**

Passes each element of the container to the given function and returns true if the function ever returns true for any element.

```go
Any(func(index int, value interface{}) bool) bool
```

**All**

Passes each element of the container to the given function and returns true if the function returns true for all elements.

```go
All(func(index int, value interface{}) bool) bool
```

**Find**

Passes each element of the container to the given function and returns the first (index,value) for which the function is true or -1,nil otherwise if no element matches the criteria.

```go
Find(func(index int, value interface{}) bool) (int, interface{})}
```

**Example:**

```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/sets/treeset"
)

func printSet(txt string, set *treeset.Set) {
	fmt.Print(txt, "[ ")
	set.Each(func(index int, value interface{}) {
		fmt.Print(value, " ")
	})
	fmt.Println("]")
}

func main() {
	set := treeset.NewWithIntComparator()
	set.Add(2, 3, 4, 2, 5, 6, 7, 8)
	printSet("Initial", set) // [ 2 3 4 5 6 7 8 ]

	even := set.Select(func(index int, value interface{}) bool {
		return value.(int)%2 == 0
	})
	printSet("Even numbers", even) // [ 2 4 6 8 ]

	foundIndex, foundValue := set.Find(func(index int, value interface{}) bool {
		return value.(int)%2 == 0 && value.(int)%3 == 0
	})
	if foundIndex != -1 {
		fmt.Println("Number divisible by 2 and 3 found is", foundValue, "at index", foundIndex) // value: 6, index: 4
	}

	square := set.Map(func(index int, value interface{}) interface{} {
		return value.(int) * value.(int)
	})
	printSet("Numbers squared", square) // [ 4 9 16 25 36 49 64 ]

	bigger := set.Any(func(index int, value interface{}) bool {
		return value.(int) > 5
	})
	fmt.Println("Set contains a number bigger than 5 is ", bigger) // true

	positive := set.All(func(index int, value interface{}) bool {
		return value.(int) > 0
	})
	fmt.Println("All numbers are positive is", positive) // true

	evenNumbersSquared := set.Select(func(index int, value interface{}) bool {
		return value.(int)%2 == 0
	}).Map(func(index int, value interface{}) interface{} {
		return value.(int) * value.(int)
	})
	printSet("Chaining", evenNumbersSquared) // [ 4 16 36 64 ]
}
```

#### EnumerableWithKey

Enumerable functions for ordered containers whose values whose elements are key/value pairs.

**Each**

Calls the given function once for each element, passing that element's key and value.

```go
Each(func(key interface{}, value interface{}))
```

**Map**

Invokes the given function once for each element and returns a container containing the values returned by the given function as key/value pairs.

```go
Map(func(key interface{}, value interface{}) (interface{}, interface{})) Container
```

**Select**

Returns a new container containing all elements for which the given function returns a true value.

```go
Select(func(key interface{}, value interface{}) bool) Container
```

**Any**

Passes each element of the container to the given function and returns true if the function ever returns true for any element.

```go
Any(func(key interface{}, value interface{}) bool) bool
```

**All**

Passes each element of the container to the given function and returns true if the function returns true for all elements.

```go
All(func(key interface{}, value interface{}) bool) bool
```

**Find**

Passes each element of the container to the given function and returns the first (key,value) for which the function is true or nil,nil otherwise if no element matches the criteria.

```go
Find(func(key interface{}, value interface{}) bool) (interface{}, interface{})
```

**Example:**

```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/maps/treemap"
)

func printMap(txt string, m *treemap.Map) {
	fmt.Print(txt, " { ")
	m.Each(func(key interface{}, value interface{}) {
		fmt.Print(key, ":", value, " ")
	})
	fmt.Println("}")
}

func main() {
	m := treemap.NewWithStringComparator()
	m.Put("g", 7)
	m.Put("f", 6)
	m.Put("e", 5)
	m.Put("d", 4)
	m.Put("c", 3)
	m.Put("b", 2)
	m.Put("a", 1)
	printMap("Initial", m) // { a:1 b:2 c:3 d:4 e:5 f:6 g:7 }

	even := m.Select(func(key interface{}, value interface{}) bool {
		return value.(int) % 2 == 0
	})
	printMap("Elements with even values", even) // { b:2 d:4 f:6 }

	foundKey, foundValue := m.Find(func(key interface{}, value interface{}) bool {
		return value.(int) % 2 == 0 && value.(int) % 3 == 0
	})
	if foundKey != nil {
		fmt.Println("Element with value divisible by 2 and 3 found is", foundValue, "with key", foundKey) // value: 6, index: 4
	}

	square := m.Map(func(key interface{}, value interface{}) (interface{}, interface{}) {
		return key.(string) + key.(string), value.(int) * value.(int)
	})
	printMap("Elements' values squared and letters duplicated", square) // { aa:1 bb:4 cc:9 dd:16 ee:25 ff:36 gg:49 }

	bigger := m.Any(func(key interface{}, value interface{}) bool {
		return value.(int) > 5
	})
	fmt.Println("Map contains element whose value is bigger than 5 is", bigger) // true

	positive := m.All(func(key interface{}, value interface{}) bool {
		return value.(int) > 0
	})
	fmt.Println("All map's elements have positive values is", positive) // true

	evenNumbersSquared := m.Select(func(key interface{}, value interface{}) bool {
		return value.(int) % 2 == 0
	}).Map(func(key interface{}, value interface{}) (interface{}, interface{}) {
		return key, value.(int) * value.(int)
	})
	printMap("Chaining", evenNumbersSquared) // { b:4 d:16 f:36 }
}
```

### Serialization

All data structures can be serialized (marshalled) and deserialized (unmarshalled). Currently only JSON support is available.

#### JSONSerializer

Outputs the container into its JSON representation.

Typical usage for key-value structures:
```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/maps/hashmap"
)

func main() {
	m := hashmap.New()
	m.Put("a", "1")
	m.Put("b", "2")
	m.Put("c", "3")

	json, err := m.ToJSON()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(json)) // {"a":"1","b":"2","c":"3"}
```

Typical usage for value-only structures:
```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/lists/arraylist"
)

func main() {
	list := arraylist.New()
	list.Add("a", "b", "c")

	json, err := list.ToJSON()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(json)) // ["a","b","c"]
}
```

#### JSONDeserializer

Populates the container with elements from the input JSON representation.

Typical usage for key-value structures:
```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/lists/arraylist"
)

func main() {
	list := arraylist.New()

	json := []byte(`["a","b"]`)
	err := list.FromJSON(json)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(list) // ArrayList ["a","b"]
}
```

Typical usage for value-only structures:
```go
package main

import (
	"fmt"
	"github.com/emirpasic/gods/lists/arraylist"
)

func main() {
	list := arraylist.New()

	json := []byte(`["a","b"]`)
	err := list.FromJSON(json)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(list) // ArrayList ["a","b"]
}
```

### Sort

Sort is a general purpose sort function.

Lists have an in-place _Sort()_ function and all containers can return their sorted elements via _containers.GetSortedValues()_ function.

Internally these all use the _utils.Sort()_ method:

```go
package main

import "github.com/emirpasic/gods/utils"

func main() {
	strings := []interface{}{}                  // []
	strings = append(strings, "d")              // ["d"]
	strings = append(strings, "a")              // ["d","a"]
	strings = append(strings, "b")              // ["d","a",b"
	strings = append(strings, "c")              // ["d","a",b","c"]
	utils.Sort(strings, utils.StringComparator) // ["a","b","c","d"]
}
```

### Container

Container specific operations:

```go
// Returns sorted container''s elements with respect to the passed comparator.
// Does not effect the ordering of elements within the container.
func GetSortedValues(container Container, comparator utils.Comparator) []interface{}
```

Usage:

```go
package main

import (
	"github.com/emirpasic/gods/lists/arraylist"
    "github.com/emirpasic/gods/utils"
)

func main() {
	list := arraylist.New()
    list.Add(2, 1, 3)
    values := GetSortedValues(container, utils.StringComparator) // [1, 2, 3]
}
```

## Appendix

### Motivation

Collections and data structures found in other languages: Java Collections, C++ Standard Template Library (STL) containers, Qt Containers, Ruby Enumerable etc.

### Goals

**Fast algorithms**:

  - Based on decades of knowledge and experiences of other libraries mentioned above.

**Memory efficient algorithms**:

  - Avoiding to consume memory by using optimal algorithms and data structures for the given set of problems, e.g. red-black tree in case of TreeMap to avoid keeping redundant sorted array of keys in memory.

**Easy to use library**:

  - Well-structured library with minimalistic set of atomic operations from which more complex operations can be crafted.

**Stable library**:

  - Only additions are permitted keeping the library backward compatible.

**Solid documentation and examples**:

  - Learning by example.

**Production ready**:

  - Used in production.

**No dependencies**:

  - No external imports.

There is often a tug of war between speed and memory when crafting algorithms. We choose to optimize for speed in most cases within reasonable limits on memory consumption.

Thread safety is not a concern of this project, this should be handled at a higher level.

### Testing and Benchmarking

This takes a while, so test within sub-packages:

`go test -run=NO_TEST -bench . -benchmem  -benchtime 1s ./...`

<p align="center"><img src="https://cloud.githubusercontent.com/assets/3115942/16892979/5e698d46-4b27-11e6-864b-cb2b865327b6.png" /></p>

### Contributing

Biggest contribution towards this library is to use it and give us feedback for further improvements and additions.

For direct contributions, _pull request_ into master branch or ask to become a contributor.

Coding style:

```shell
# Install tooling and set path:
go get github.com/golang/lint/golint
go get github.com/fzipp/gocyclo
go get github.com/kisielk/errcheck
export PATH=$PATH:$GOPATH/bin

# Fix errors and warnings:
go fmt ./... && gofmt -s -w . && go vet ./... && go get ./... && go test ./... && golint ./... && gocyclo -avg -over 15 . && errcheck ./...
```

### License

This library is distributed under the BSD-style license found in the [LICENSE](https://github.com/emirpasic/gods/blob/master/LICENSE) file.
## TOML parser and encoder for Go with reflection

TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library `json` and `xml`
packages. This package also supports the `encoding.TextUnmarshaler` and
`encoding.TextMarshaler` interfaces so that you can define custom data
representations. (There is an example of this below.)

Spec: https://github.com/toml-lang/toml

Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

Documentation: https://godoc.org/github.com/BurntSushi/toml

Installation:

```bash
go get github.com/BurntSushi/toml
```

Try the toml validator:

```bash
go get github.com/BurntSushi/toml/cmd/tomlv
tomlv some-toml-file.toml
```

[![Build Status](https://travis-ci.org/BurntSushi/toml.svg?branch=master)](https://travis-ci.org/BurntSushi/toml) [![GoDoc](https://godoc.org/github.com/BurntSushi/toml?status.svg)](https://godoc.org/github.com/BurntSushi/toml)

### Testing

This package passes all tests in
[toml-test](https://github.com/BurntSushi/toml-test) for both the decoder
and the encoder.

### Examples

This package works similarly to how the Go standard library handles `XML`
and `JSON`. Namely, data is loaded into Go values via reflection.

For the simplest example, consider some TOML file as just a list of keys
and values:

```toml
Age = 25
Cats = [ "Cauchy", "Plato" ]
Pi = 3.14
Perfection = [ 6, 28, 496, 8128 ]
DOB = 1987-07-05T05:45:00Z
```

Which could be defined in Go as:

```go
type Config struct {
  Age int
  Cats []string
  Pi float64
  Perfection []int
  DOB time.Time // requires `import time`
}
```

And then decoded with:

```go
var conf Config
if _, err := toml.Decode(tomlData, &conf); err != nil {
  // handle error
}
```

You can also use struct tags if your struct field name doesn't map to a TOML
key value directly:

```toml
some_key_NAME = "wat"
```

```go
type TOML struct {
  ObscureKey string `toml:"some_key_NAME"`
}
```

### Using the `encoding.TextUnmarshaler` interface

Here's an example that automatically parses duration strings into
`time.Duration` values:

```toml
[[song]]
name = "Thunder Road"
duration = "4m49s"

[[song]]
name = "Stairway to Heaven"
duration = "8m03s"
```

Which can be decoded with:

```go
type song struct {
  Name     string
  Duration duration
}
type songs struct {
  Song []song
}
var favorites songs
if _, err := toml.Decode(blob, &favorites); err != nil {
  log.Fatal(err)
}

for _, s := range favorites.Song {
  fmt.Printf("%s (%s)\n", s.Name, s.Duration)
}
```

And you'll also need a `duration` type that satisfies the
`encoding.TextUnmarshaler` interface:

```go
type duration struct {
	time.Duration
}

func (d *duration) UnmarshalText(text []byte) error {
	var err error
	d.Duration, err = time.ParseDuration(string(text))
	return err
}
```

### More complex usage

Here's an example of how to load the example from the official spec page:

```toml
# This is a TOML document. Boom.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
organization = "GitHub"
bio = "GitHub Cofounder & CEO\nLikes tater tots and beer."
dob = 1979-05-27T07:32:00Z # First class dates? Why not?

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]

  # You can indent as you please. Tabs or spaces. TOML don't care.
  [servers.alpha]
  ip = "10.0.0.1"
  dc = "eqdc10"

  [servers.beta]
  ip = "10.0.0.2"
  dc = "eqdc10"

[clients]
data = [ ["gamma", "delta"], [1, 2] ] # just an update to make sure parsers support it

# Line breaks are OK when inside arrays
hosts = [
  "alpha",
  "omega"
]
```

And the corresponding Go types are:

```go
type tomlConfig struct {
	Title string
	Owner ownerInfo
	DB database `toml:"database"`
	Servers map[string]server
	Clients clients
}

type ownerInfo struct {
	Name string
	Org string `toml:"organization"`
	Bio string
	DOB time.Time
}

type database struct {
	Server string
	Ports []int
	ConnMax int `toml:"connection_max"`
	Enabled bool
}

type server struct {
	IP string
	DC string
}

type clients struct {
	Data [][]interface{}
	Hosts []string
}
```

Note that a case insensitive match will be tried if an exact match can't be
found.

A working example of the above can be found in `_examples/example.{go,toml}`.
# TOML Validator

If Go is installed, it's simple to try it out:

```bash
go get github.com/BurntSushi/toml/cmd/tomlv
tomlv some-toml-file.toml
```

You can see the types of every key in a TOML file with:

```bash
tomlv -types some-toml-file.toml
```

At the moment, only one error message is reported at a time. Error messages
include line numbers. No output means that the files given are valid TOML, or
there is a bug in `tomlv`.

Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)
# Implements the TOML test suite interface for TOML encoders

This is an implementation of the interface expected by
[toml-test](https://github.com/BurntSushi/toml-test) for the
[TOML encoder](https://github.com/BurntSushi/toml).
In particular, it maps JSON data on `stdin` to a TOML format on `stdout`.


Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

Compatible with `toml-test` version
[v0.2.0](https://github.com/BurntSushi/toml-test/tree/v0.2.0)
# Implements the TOML test suite interface

This is an implementation of the interface expected by
[toml-test](https://github.com/BurntSushi/toml-test) for my
[toml parser written in Go](https://github.com/BurntSushi/toml).
In particular, it maps TOML data on `stdin` to a JSON format on `stdout`.


Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

Compatible with `toml-test` version
[v0.2.0](https://github.com/BurntSushi/toml-test/tree/v0.2.0)
# UUID package for Go language

[![Build Status](https://travis-ci.org/satori/go.uuid.png?branch=master)](https://travis-ci.org/satori/go.uuid)
[![Coverage Status](https://coveralls.io/repos/github/satori/go.uuid/badge.svg?branch=master)](https://coveralls.io/github/satori/go.uuid)
[![GoDoc](http://godoc.org/github.com/satori/go.uuid?status.png)](http://godoc.org/github.com/satori/go.uuid)

This package provides pure Go implementation of Universally Unique Identifier (UUID). Supported both creation and parsing of UUIDs.

With 100% test coverage and benchmarks out of box.

Supported versions:
* Version 1, based on timestamp and MAC address (RFC 4122)
* Version 2, based on timestamp, MAC address and POSIX UID/GID (DCE 1.1)
* Version 3, based on MD5 hashing (RFC 4122)
* Version 4, based on random numbers (RFC 4122)
* Version 5, based on SHA-1 hashing (RFC 4122)

## Installation

Use the `go` command:

	$ go get github.com/satori/go.uuid

## Requirements

UUID package requires Go >= 1.2.

## Example

```go
package main

import (
	"fmt"
	"github.com/satori/go.uuid"
)

func main() {
	// Creating UUID Version 4
	u1 := uuid.NewV4()
	fmt.Printf("UUIDv4: %s\n", u1)

	// Parsing UUID from string input
	u2, err := uuid.FromString("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
	if err != nil {
		fmt.Printf("Something gone wrong: %s", err)
	}
	fmt.Printf("Successfully parsed: %s", u2)
}
```

## Documentation

[Documentation](http://godoc.org/github.com/satori/go.uuid) is hosted at GoDoc project.

## Links
* [RFC 4122](http://tools.ietf.org/html/rfc4122)
* [DCE 1.1: Authentication and Security Services](http://pubs.opengroup.org/onlinepubs/9696989899/chap5.htm#tagcjh_08_02_01_01)

## Copyright

Copyright (C) 2013-2016 by Maxim Bublis <b@codemonkey.ru>.

UUID package released under MIT License.
See [LICENSE](https://github.com/satori/go.uuid/blob/master/LICENSE) for details.
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
![cobra logo](https://cloud.githubusercontent.com/assets/173412/10886352/ad566232-814f-11e5-9cd0-aa101788c117.png)

Cobra is both a library for creating powerful modern CLI applications as well as a program to generate applications and command files.

Many of the most widely used Go projects are built using Cobra including:

* [Kubernetes](http://kubernetes.io/)
* [Hugo](http://gohugo.io)
* [rkt](https://github.com/coreos/rkt)
* [etcd](https://github.com/coreos/etcd)
* [Moby (former Docker)](https://github.com/moby/moby)
* [Docker (distribution)](https://github.com/docker/distribution)
* [OpenShift](https://www.openshift.com/)
* [Delve](https://github.com/derekparker/delve)
* [GopherJS](http://www.gopherjs.org/)
* [CockroachDB](http://www.cockroachlabs.com/)
* [Bleve](http://www.blevesearch.com/)
* [ProjectAtomic (enterprise)](http://www.projectatomic.io/)
* [GiantSwarm's swarm](https://github.com/giantswarm/cli)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)
* [rclone](http://rclone.org/)


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
* Easy generation of applications & commands with `cobra init appname` & `cobra add cmdname`
* Intelligent suggestions (`app srver`... did you mean `app server`?)
* Automatic help generation for commands and flags
* Automatic detailed help for `app help [command]`
* Automatic help flag recognition of `-h`, `--help`, etc.
* Automatically generated bash autocomplete for your application
* Automatically generated man pages for your application
* Command aliases so you can change things without breaking them
* The flexibility to define your own help, usage, etc.
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

    hugo server --port=1313

In this command we are telling Git to clone the url bare.

    git clone URL --bare

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
library](https://github.com/spf13/pflag), a fork of the flag standard library
which maintains the same interface while adding POSIX compliance.

## Usage

Cobra works by creating a set of commands and then organizing them into a tree.
The tree defines the structure of the application.

Once each command is defined with its corresponding flags, then the
tree is assigned to the commander which is finally executed.

# Installing
Using Cobra is easy. First, use `go get` to install the latest version
of the library. This command will install the `cobra` generator executable
along with the library and its dependencies:

    go get -u github.com/spf13/cobra

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

import (
	"fmt"
	"os"

	"{pathToYourApp}/cmd"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
```

## Using the Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

In order to use the cobra command, compile it using the following command:

    go get github.com/spf13/cobra/cobra

This will create the cobra executable under your `$GOPATH/bin` directory.

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

*Note: Use camelCase (not snake_case/snake-case) for command names.
Otherwise, you will become unexpected errors.
For example, `cobra add add-user` is incorrect, but `cobra add addUser` is valid.*

Once you have run these three commands you would have an app structure that would look like:

```
  ▾ app/
    ▾ cmd/
        serve.go
        config.go
        create.go
      main.go
```

At this point you can run `go run main.go` and it would run your app. `go run
main.go serve`, `go run main.go config`, `go run main.go config create` along
with `go run main.go help serve`, etc would all work.

Obviously you haven't added your own code to these yet, the commands are ready
for you to give them their tasks. Have fun!

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

You can also use built-in licenses. For example, **GPLv2**, **GPLv3**, **LGPL**,
**AGPL**, **MIT**, **2-Clause BSD** or **3-Clause BSD**.

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

For example cmd/root.go:

```go
import (
	"fmt"
	"os"

	homedir "github.com/mitchellh/go-homedir"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

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

func main() {
  // Don't forget to read config either from cfgFile or from home directory!
	if cfgFile != "" {
		// Use config file from the flag.
		viper.SetConfigFile(cfgFile)
	} else {
		// Find home directory.
		home, err := homedir.Dir()
		if err != nil {
			fmt.Println(home)
			os.Exit(1)
		}

		// Search config in home directory with name ".cobra" (without extension).
		viper.AddConfigPath(home)
		viper.SetConfigName(".cobra")
	}

	if err := viper.ReadInConfig(); err != nil {
		fmt.Println("Can't read config:", err)
    os.Exit(1)
	}
}
```

### Create your main.go

With the root command you need to have your main function execute it.
Execute should be run on the root for clarity, though it can be called on any command.

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import (
	"fmt"
	"os"

	"{pathToYourApp}/cmd"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
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
	"fmt"
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

### Bind Flags with Config

You can also bind your flags with [viper](https://github.com/spf13/viper):
```go
var author string

func init() {
	RootCmd.PersistentFlags().StringVar(&author, "author", "YOUR NAME", "Author name for copyright attribution")
	viper.BindPFlag("author", RootCmd.PersistentFlags().Lookup("author"))
}
```

In this example the persistent flag `author` is bound with `viper`.
**Note**, that the variable `author` will not be set to the value from config,
when the `--author` flag is not provided by user.

More in [viper documentation](https://github.com/spf13/viper#working-with-flags).

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
and `SilenceErrors` to `true` on the command. A child command respects these flags if they are set on the parent
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

## Extensions

Libraries for extending Cobra:

* [cmdns](https://github.com/gosuri/cmdns): Enables name spacing a command's immediate children. It provides an alternative way to structure subcommands, similar to `heroku apps:create` and `ovrclk clusters:launch`.

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
Bolt [![Coverage Status](https://coveralls.io/repos/boltdb/bolt/badge.svg?branch=master)](https://coveralls.io/r/boltdb/bolt?branch=master) [![GoDoc](https://godoc.org/github.com/boltdb/bolt?status.svg)](https://godoc.org/github.com/boltdb/bolt) ![Version](https://img.shields.io/badge/version-1.2.1-green.svg)
====

Bolt is a pure Go key/value store inspired by [Howard Chu's][hyc_symas]
[LMDB project][lmdb]. The goal of the project is to provide a simple,
fast, and reliable database for projects that don't require a full database
server such as Postgres or MySQL.

Since Bolt is meant to be used as such a low-level piece of functionality,
simplicity is key. The API will be small and only focus on getting values
and setting values. That's it.

[hyc_symas]: https://twitter.com/hyc_symas
[lmdb]: http://symas.com/mdb/

## Project Status

Bolt is stable, the API is fixed, and the file format is fixed. Full unit
test coverage and randomized black box testing are used to ensure database
consistency and thread safety. Bolt is currently used in high-load production
environments serving databases as large as 1TB. Many companies such as
Shopify and Heroku use Bolt-backed services every day.

## Table of Contents

- [Getting Started](#getting-started)
  - [Installing](#installing)
  - [Opening a database](#opening-a-database)
  - [Transactions](#transactions)
    - [Read-write transactions](#read-write-transactions)
    - [Read-only transactions](#read-only-transactions)
    - [Batch read-write transactions](#batch-read-write-transactions)
    - [Managing transactions manually](#managing-transactions-manually)
  - [Using buckets](#using-buckets)
  - [Using key/value pairs](#using-keyvalue-pairs)
  - [Autoincrementing integer for the bucket](#autoincrementing-integer-for-the-bucket)
  - [Iterating over keys](#iterating-over-keys)
    - [Prefix scans](#prefix-scans)
    - [Range scans](#range-scans)
    - [ForEach()](#foreach)
  - [Nested buckets](#nested-buckets)
  - [Database backups](#database-backups)
  - [Statistics](#statistics)
  - [Read-Only Mode](#read-only-mode)
  - [Mobile Use (iOS/Android)](#mobile-use-iosandroid)
- [Resources](#resources)
- [Comparison with other databases](#comparison-with-other-databases)
  - [Postgres, MySQL, & other relational databases](#postgres-mysql--other-relational-databases)
  - [LevelDB, RocksDB](#leveldb-rocksdb)
  - [LMDB](#lmdb)
- [Caveats & Limitations](#caveats--limitations)
- [Reading the Source](#reading-the-source)
- [Other Projects Using Bolt](#other-projects-using-bolt)

## Getting Started

### Installing

To start using Bolt, install Go and run `go get`:

```sh
$ go get github.com/boltdb/bolt/...
```

This will retrieve the library and install the `bolt` command line utility into
your `$GOBIN` path.


### Opening a database

The top-level object in Bolt is a `DB`. It is represented as a single file on
your disk and represents a consistent snapshot of your data.

To open your database, simply use the `bolt.Open()` function:

```go
package main

import (
	"log"

	"github.com/boltdb/bolt"
)

func main() {
	// Open the my.db data file in your current directory.
	// It will be created if it doesn't exist.
	db, err := bolt.Open("my.db", 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	...
}
```

Please note that Bolt obtains a file lock on the data file so multiple processes
cannot open the same database at the same time. Opening an already open Bolt
database will cause it to hang until the other process closes it. To prevent
an indefinite wait you can pass a timeout option to the `Open()` function:

```go
db, err := bolt.Open("my.db", 0600, &bolt.Options{Timeout: 1 * time.Second})
```


### Transactions

Bolt allows only one read-write transaction at a time but allows as many
read-only transactions as you want at a time. Each transaction has a consistent
view of the data as it existed when the transaction started.

Individual transactions and all objects created from them (e.g. buckets, keys)
are not thread safe. To work with data in multiple goroutines you must start
a transaction for each one or use locking to ensure only one goroutine accesses
a transaction at a time. Creating transaction from the `DB` is thread safe.

Read-only transactions and read-write transactions should not depend on one
another and generally shouldn't be opened simultaneously in the same goroutine.
This can cause a deadlock as the read-write transaction needs to periodically
re-map the data file but it cannot do so while a read-only transaction is open.


#### Read-write transactions

To start a read-write transaction, you can use the `DB.Update()` function:

```go
err := db.Update(func(tx *bolt.Tx) error {
	...
	return nil
})
```

Inside the closure, you have a consistent view of the database. You commit the
transaction by returning `nil` at the end. You can also rollback the transaction
at any point by returning an error. All database operations are allowed inside
a read-write transaction.

Always check the return error as it will report any disk failures that can cause
your transaction to not complete. If you return an error within your closure
it will be passed through.


#### Read-only transactions

To start a read-only transaction, you can use the `DB.View()` function:

```go
err := db.View(func(tx *bolt.Tx) error {
	...
	return nil
})
```

You also get a consistent view of the database within this closure, however,
no mutating operations are allowed within a read-only transaction. You can only
retrieve buckets, retrieve values, and copy the database within a read-only
transaction.


#### Batch read-write transactions

Each `DB.Update()` waits for disk to commit the writes. This overhead
can be minimized by combining multiple updates with the `DB.Batch()`
function:

```go
err := db.Batch(func(tx *bolt.Tx) error {
	...
	return nil
})
```

Concurrent Batch calls are opportunistically combined into larger
transactions. Batch is only useful when there are multiple goroutines
calling it.

The trade-off is that `Batch` can call the given
function multiple times, if parts of the transaction fail. The
function must be idempotent and side effects must take effect only
after a successful return from `DB.Batch()`.

For example: don't display messages from inside the function, instead
set variables in the enclosing scope:

```go
var id uint64
err := db.Batch(func(tx *bolt.Tx) error {
	// Find last key in bucket, decode as bigendian uint64, increment
	// by one, encode back to []byte, and add new key.
	...
	id = newValue
	return nil
})
if err != nil {
	return ...
}
fmt.Println("Allocated ID %d", id)
```


#### Managing transactions manually

The `DB.View()` and `DB.Update()` functions are wrappers around the `DB.Begin()`
function. These helper functions will start the transaction, execute a function,
and then safely close your transaction if an error is returned. This is the
recommended way to use Bolt transactions.

However, sometimes you may want to manually start and end your transactions.
You can use the `DB.Begin()` function directly but **please** be sure to close
the transaction.

```go
// Start a writable transaction.
tx, err := db.Begin(true)
if err != nil {
    return err
}
defer tx.Rollback()

// Use the transaction...
_, err := tx.CreateBucket([]byte("MyBucket"))
if err != nil {
    return err
}

// Commit the transaction and check for error.
if err := tx.Commit(); err != nil {
    return err
}
```

The first argument to `DB.Begin()` is a boolean stating if the transaction
should be writable.


### Using buckets

Buckets are collections of key/value pairs within the database. All keys in a
bucket must be unique. You can create a bucket using the `DB.CreateBucket()`
function:

```go
db.Update(func(tx *bolt.Tx) error {
	b, err := tx.CreateBucket([]byte("MyBucket"))
	if err != nil {
		return fmt.Errorf("create bucket: %s", err)
	}
	return nil
})
```

You can also create a bucket only if it doesn't exist by using the
`Tx.CreateBucketIfNotExists()` function. It's a common pattern to call this
function for all your top-level buckets after you open your database so you can
guarantee that they exist for future transactions.

To delete a bucket, simply call the `Tx.DeleteBucket()` function.


### Using key/value pairs

To save a key/value pair to a bucket, use the `Bucket.Put()` function:

```go
db.Update(func(tx *bolt.Tx) error {
	b := tx.Bucket([]byte("MyBucket"))
	err := b.Put([]byte("answer"), []byte("42"))
	return err
})
```

This will set the value of the `"answer"` key to `"42"` in the `MyBucket`
bucket. To retrieve this value, we can use the `Bucket.Get()` function:

```go
db.View(func(tx *bolt.Tx) error {
	b := tx.Bucket([]byte("MyBucket"))
	v := b.Get([]byte("answer"))
	fmt.Printf("The answer is: %s\n", v)
	return nil
})
```

The `Get()` function does not return an error because its operation is
guaranteed to work (unless there is some kind of system failure). If the key
exists then it will return its byte slice value. If it doesn't exist then it
will return `nil`. It's important to note that you can have a zero-length value
set to a key which is different than the key not existing.

Use the `Bucket.Delete()` function to delete a key from the bucket.

Please note that values returned from `Get()` are only valid while the
transaction is open. If you need to use a value outside of the transaction
then you must use `copy()` to copy it to another byte slice.


### Autoincrementing integer for the bucket
By using the `NextSequence()` function, you can let Bolt determine a sequence
which can be used as the unique identifier for your key/value pairs. See the
example below.

```go
// CreateUser saves u to the store. The new user ID is set on u once the data is persisted.
func (s *Store) CreateUser(u *User) error {
    return s.db.Update(func(tx *bolt.Tx) error {
        // Retrieve the users bucket.
        // This should be created when the DB is first opened.
        b := tx.Bucket([]byte("users"))

        // Generate ID for the user.
        // This returns an error only if the Tx is closed or not writeable.
        // That can't happen in an Update() call so I ignore the error check.
        id, _ := b.NextSequence()
        u.ID = int(id)

        // Marshal user data into bytes.
        buf, err := json.Marshal(u)
        if err != nil {
            return err
        }

        // Persist bytes to users bucket.
        return b.Put(itob(u.ID), buf)
    })
}

// itob returns an 8-byte big endian representation of v.
func itob(v int) []byte {
    b := make([]byte, 8)
    binary.BigEndian.PutUint64(b, uint64(v))
    return b
}

type User struct {
    ID int
    ...
}
```

### Iterating over keys

Bolt stores its keys in byte-sorted order within a bucket. This makes sequential
iteration over these keys extremely fast. To iterate over keys we'll use a
`Cursor`:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume bucket exists and has keys
	b := tx.Bucket([]byte("MyBucket"))

	c := b.Cursor()

	for k, v := c.First(); k != nil; k, v = c.Next() {
		fmt.Printf("key=%s, value=%s\n", k, v)
	}

	return nil
})
```

The cursor allows you to move to a specific point in the list of keys and move
forward or backward through the keys one at a time.

The following functions are available on the cursor:

```
First()  Move to the first key.
Last()   Move to the last key.
Seek()   Move to a specific key.
Next()   Move to the next key.
Prev()   Move to the previous key.
```

Each of those functions has a return signature of `(key []byte, value []byte)`.
When you have iterated to the end of the cursor then `Next()` will return a
`nil` key.  You must seek to a position using `First()`, `Last()`, or `Seek()`
before calling `Next()` or `Prev()`. If you do not seek to a position then
these functions will return a `nil` key.

During iteration, if the key is non-`nil` but the value is `nil`, that means
the key refers to a bucket rather than a value.  Use `Bucket.Bucket()` to
access the sub-bucket.


#### Prefix scans

To iterate over a key prefix, you can combine `Seek()` and `bytes.HasPrefix()`:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume bucket exists and has keys
	c := tx.Bucket([]byte("MyBucket")).Cursor()

	prefix := []byte("1234")
	for k, v := c.Seek(prefix); k != nil && bytes.HasPrefix(k, prefix); k, v = c.Next() {
		fmt.Printf("key=%s, value=%s\n", k, v)
	}

	return nil
})
```

#### Range scans

Another common use case is scanning over a range such as a time range. If you
use a sortable time encoding such as RFC3339 then you can query a specific
date range like this:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume our events bucket exists and has RFC3339 encoded time keys.
	c := tx.Bucket([]byte("Events")).Cursor()

	// Our time range spans the 90's decade.
	min := []byte("1990-01-01T00:00:00Z")
	max := []byte("2000-01-01T00:00:00Z")

	// Iterate over the 90's.
	for k, v := c.Seek(min); k != nil && bytes.Compare(k, max) <= 0; k, v = c.Next() {
		fmt.Printf("%s: %s\n", k, v)
	}

	return nil
})
```

Note that, while RFC3339 is sortable, the Golang implementation of RFC3339Nano does not use a fixed number of digits after the decimal point and is therefore not sortable.


#### ForEach()

You can also use the function `ForEach()` if you know you'll be iterating over
all the keys in a bucket:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume bucket exists and has keys
	b := tx.Bucket([]byte("MyBucket"))

	b.ForEach(func(k, v []byte) error {
		fmt.Printf("key=%s, value=%s\n", k, v)
		return nil
	})
	return nil
})
```

Please note that keys and values in `ForEach()` are only valid while
the transaction is open. If you need to use a key or value outside of
the transaction, you must use `copy()` to copy it to another byte
slice.

### Nested buckets

You can also store a bucket in a key to create nested buckets. The API is the
same as the bucket management API on the `DB` object:

```go
func (*Bucket) CreateBucket(key []byte) (*Bucket, error)
func (*Bucket) CreateBucketIfNotExists(key []byte) (*Bucket, error)
func (*Bucket) DeleteBucket(key []byte) error
```

Say you had a multi-tenant application where the root level bucket was the account bucket. Inside of this bucket was a sequence of accounts which themselves are buckets. And inside the sequence bucket you could have many buckets pertaining to the Account itself (Users, Notes, etc) isolating the information into logical groupings.

```go

// createUser creates a new user in the given account.
func createUser(accountID int, u *User) error {
    // Start the transaction.
    tx, err := db.Begin(true)
    if err != nil {
        return err
    }
    defer tx.Rollback()

    // Retrieve the root bucket for the account.
    // Assume this has already been created when the account was set up.
    root := tx.Bucket([]byte(strconv.FormatUint(accountID, 10)))

    // Setup the users bucket.
    bkt, err := root.CreateBucketIfNotExists([]byte("USERS"))
    if err != nil {
        return err
    }

    // Generate an ID for the new user.
    userID, err := bkt.NextSequence()
    if err != nil {
        return err
    }
    u.ID = userID

    // Marshal and save the encoded user.
    if buf, err := json.Marshal(u); err != nil {
        return err
    } else if err := bkt.Put([]byte(strconv.FormatUint(u.ID, 10)), buf); err != nil {
        return err
    }

    // Commit the transaction.
    if err := tx.Commit(); err != nil {
        return err
    }

    return nil
}

```




### Database backups

Bolt is a single file so it's easy to backup. You can use the `Tx.WriteTo()`
function to write a consistent view of the database to a writer. If you call
this from a read-only transaction, it will perform a hot backup and not block
your other database reads and writes.

By default, it will use a regular file handle which will utilize the operating
system's page cache. See the [`Tx`](https://godoc.org/github.com/boltdb/bolt#Tx)
documentation for information about optimizing for larger-than-RAM datasets.

One common use case is to backup over HTTP so you can use tools like `cURL` to
do database backups:

```go
func BackupHandleFunc(w http.ResponseWriter, req *http.Request) {
	err := db.View(func(tx *bolt.Tx) error {
		w.Header().Set("Content-Type", "application/octet-stream")
		w.Header().Set("Content-Disposition", `attachment; filename="my.db"`)
		w.Header().Set("Content-Length", strconv.Itoa(int(tx.Size())))
		_, err := tx.WriteTo(w)
		return err
	})
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}
```

Then you can backup using this command:

```sh
$ curl http://localhost/backup > my.db
```

Or you can open your browser to `http://localhost/backup` and it will download
automatically.

If you want to backup to another file you can use the `Tx.CopyFile()` helper
function.


### Statistics

The database keeps a running count of many of the internal operations it
performs so you can better understand what's going on. By grabbing a snapshot
of these stats at two points in time we can see what operations were performed
in that time range.

For example, we could start a goroutine to log stats every 10 seconds:

```go
go func() {
	// Grab the initial stats.
	prev := db.Stats()

	for {
		// Wait for 10s.
		time.Sleep(10 * time.Second)

		// Grab the current stats and diff them.
		stats := db.Stats()
		diff := stats.Sub(&prev)

		// Encode stats to JSON and print to STDERR.
		json.NewEncoder(os.Stderr).Encode(diff)

		// Save stats for the next loop.
		prev = stats
	}
}()
```

It's also useful to pipe these stats to a service such as statsd for monitoring
or to provide an HTTP endpoint that will perform a fixed-length sample.


### Read-Only Mode

Sometimes it is useful to create a shared, read-only Bolt database. To this,
set the `Options.ReadOnly` flag when opening your database. Read-only mode
uses a shared lock to allow multiple processes to read from the database but
it will block any processes from opening the database in read-write mode.

```go
db, err := bolt.Open("my.db", 0666, &bolt.Options{ReadOnly: true})
if err != nil {
	log.Fatal(err)
}
```

### Mobile Use (iOS/Android)

Bolt is able to run on mobile devices by leveraging the binding feature of the
[gomobile](https://github.com/golang/mobile) tool. Create a struct that will
contain your database logic and a reference to a `*bolt.DB` with a initializing
constructor that takes in a filepath where the database file will be stored.
Neither Android nor iOS require extra permissions or cleanup from using this method.

```go
func NewBoltDB(filepath string) *BoltDB {
	db, err := bolt.Open(filepath+"/demo.db", 0600, nil)
	if err != nil {
		log.Fatal(err)
	}

	return &BoltDB{db}
}

type BoltDB struct {
	db *bolt.DB
	...
}

func (b *BoltDB) Path() string {
	return b.db.Path()
}

func (b *BoltDB) Close() {
	b.db.Close()
}
```

Database logic should be defined as methods on this wrapper struct.

To initialize this struct from the native language (both platforms now sync
their local storage to the cloud. These snippets disable that functionality for the
database file):

#### Android

```java
String path;
if (android.os.Build.VERSION.SDK_INT >=android.os.Build.VERSION_CODES.LOLLIPOP){
    path = getNoBackupFilesDir().getAbsolutePath();
} else{
    path = getFilesDir().getAbsolutePath();
}
Boltmobiledemo.BoltDB boltDB = Boltmobiledemo.NewBoltDB(path)
```

#### iOS

```objc
- (void)demo {
    NSString* path = [NSSearchPathForDirectoriesInDomains(NSLibraryDirectory,
                                                          NSUserDomainMask,
                                                          YES) objectAtIndex:0];
	GoBoltmobiledemoBoltDB * demo = GoBoltmobiledemoNewBoltDB(path);
	[self addSkipBackupAttributeToItemAtPath:demo.path];
	//Some DB Logic would go here
	[demo close];
}

- (BOOL)addSkipBackupAttributeToItemAtPath:(NSString *) filePathString
{
    NSURL* URL= [NSURL fileURLWithPath: filePathString];
    assert([[NSFileManager defaultManager] fileExistsAtPath: [URL path]]);

    NSError *error = nil;
    BOOL success = [URL setResourceValue: [NSNumber numberWithBool: YES]
                                  forKey: NSURLIsExcludedFromBackupKey error: &error];
    if(!success){
        NSLog(@"Error excluding %@ from backup %@", [URL lastPathComponent], error);
    }
    return success;
}

```

## Resources

For more information on getting started with Bolt, check out the following articles:

* [Intro to BoltDB: Painless Performant Persistence](http://npf.io/2014/07/intro-to-boltdb-painless-performant-persistence/) by [Nate Finch](https://github.com/natefinch).
* [Bolt -- an embedded key/value database for Go](https://www.progville.com/go/bolt-embedded-db-golang/) by Progville


## Comparison with other databases

### Postgres, MySQL, & other relational databases

Relational databases structure data into rows and are only accessible through
the use of SQL. This approach provides flexibility in how you store and query
your data but also incurs overhead in parsing and planning SQL statements. Bolt
accesses all data by a byte slice key. This makes Bolt fast to read and write
data by key but provides no built-in support for joining values together.

Most relational databases (with the exception of SQLite) are standalone servers
that run separately from your application. This gives your systems
flexibility to connect multiple application servers to a single database
server but also adds overhead in serializing and transporting data over the
network. Bolt runs as a library included in your application so all data access
has to go through your application's process. This brings data closer to your
application but limits multi-process access to the data.


### LevelDB, RocksDB

LevelDB and its derivatives (RocksDB, HyperLevelDB) are similar to Bolt in that
they are libraries bundled into the application, however, their underlying
structure is a log-structured merge-tree (LSM tree). An LSM tree optimizes
random writes by using a write ahead log and multi-tiered, sorted files called
SSTables. Bolt uses a B+tree internally and only a single file. Both approaches
have trade-offs.

If you require a high random write throughput (>10,000 w/sec) or you need to use
spinning disks then LevelDB could be a good choice. If your application is
read-heavy or does a lot of range scans then Bolt could be a good choice.

One other important consideration is that LevelDB does not have transactions.
It supports batch writing of key/values pairs and it supports read snapshots
but it will not give you the ability to do a compare-and-swap operation safely.
Bolt supports fully serializable ACID transactions.


### LMDB

Bolt was originally a port of LMDB so it is architecturally similar. Both use
a B+tree, have ACID semantics with fully serializable transactions, and support
lock-free MVCC using a single writer and multiple readers.

The two projects have somewhat diverged. LMDB heavily focuses on raw performance
while Bolt has focused on simplicity and ease of use. For example, LMDB allows
several unsafe actions such as direct writes for the sake of performance. Bolt
opts to disallow actions which can leave the database in a corrupted state. The
only exception to this in Bolt is `DB.NoSync`.

There are also a few differences in API. LMDB requires a maximum mmap size when
opening an `mdb_env` whereas Bolt will handle incremental mmap resizing
automatically. LMDB overloads the getter and setter functions with multiple
flags whereas Bolt splits these specialized cases into their own functions.


## Caveats & Limitations

It's important to pick the right tool for the job and Bolt is no exception.
Here are a few things to note when evaluating and using Bolt:

* Bolt is good for read intensive workloads. Sequential write performance is
  also fast but random writes can be slow. You can use `DB.Batch()` or add a
  write-ahead log to help mitigate this issue.

* Bolt uses a B+tree internally so there can be a lot of random page access.
  SSDs provide a significant performance boost over spinning disks.

* Try to avoid long running read transactions. Bolt uses copy-on-write so
  old pages cannot be reclaimed while an old transaction is using them.

* Byte slices returned from Bolt are only valid during a transaction. Once the
  transaction has been committed or rolled back then the memory they point to
  can be reused by a new page or can be unmapped from virtual memory and you'll
  see an `unexpected fault address` panic when accessing it.

* Bolt uses an exclusive write lock on the database file so it cannot be
  shared by multiple processes.

* Be careful when using `Bucket.FillPercent`. Setting a high fill percent for
  buckets that have random inserts will cause your database to have very poor
  page utilization.

* Use larger buckets in general. Smaller buckets causes poor page utilization
  once they become larger than the page size (typically 4KB).

* Bulk loading a lot of random writes into a new bucket can be slow as the
  page will not split until the transaction is committed. Randomly inserting
  more than 100,000 key/value pairs into a single new bucket in a single
  transaction is not advised.

* Bolt uses a memory-mapped file so the underlying operating system handles the
  caching of the data. Typically, the OS will cache as much of the file as it
  can in memory and will release memory as needed to other processes. This means
  that Bolt can show very high memory usage when working with large databases.
  However, this is expected and the OS will release memory as needed. Bolt can
  handle databases much larger than the available physical RAM, provided its
  memory-map fits in the process virtual address space. It may be problematic
  on 32-bits systems.

* The data structures in the Bolt database are memory mapped so the data file
  will be endian specific. This means that you cannot copy a Bolt file from a
  little endian machine to a big endian machine and have it work. For most
  users this is not a concern since most modern CPUs are little endian.

* Because of the way pages are laid out on disk, Bolt cannot truncate data files
  and return free pages back to the disk. Instead, Bolt maintains a free list
  of unused pages within its data file. These free pages can be reused by later
  transactions. This works well for many use cases as databases generally tend
  to grow. However, it's important to note that deleting large chunks of data
  will not allow you to reclaim that space on disk.

  For more information on page allocation, [see this comment][page-allocation].

[page-allocation]: https://github.com/boltdb/bolt/issues/308#issuecomment-74811638


## Reading the Source

Bolt is a relatively small code base (<3KLOC) for an embedded, serializable,
transactional key/value database so it can be a good starting point for people
interested in how databases work.

The best places to start are the main entry points into Bolt:

- `Open()` - Initializes the reference to the database. It's responsible for
  creating the database if it doesn't exist, obtaining an exclusive lock on the
  file, reading the meta pages, & memory-mapping the file.

- `DB.Begin()` - Starts a read-only or read-write transaction depending on the
  value of the `writable` argument. This requires briefly obtaining the "meta"
  lock to keep track of open transactions. Only one read-write transaction can
  exist at a time so the "rwlock" is acquired during the life of a read-write
  transaction.

- `Bucket.Put()` - Writes a key/value pair into a bucket. After validating the
  arguments, a cursor is used to traverse the B+tree to the page and position
  where they key & value will be written. Once the position is found, the bucket
  materializes the underlying page and the page's parent pages into memory as
  "nodes". These nodes are where mutations occur during read-write transactions.
  These changes get flushed to disk during commit.

- `Bucket.Get()` - Retrieves a key/value pair from a bucket. This uses a cursor
  to move to the page & position of a key/value pair. During a read-only
  transaction, the key and value data is returned as a direct reference to the
  underlying mmap file so there's no allocation overhead. For read-write
  transactions, this data may reference the mmap file or one of the in-memory
  node values.

- `Cursor` - This object is simply for traversing the B+tree of on-disk pages
  or in-memory nodes. It can seek to a specific key, move to the first or last
  value, or it can move forward or backward. The cursor handles the movement up
  and down the B+tree transparently to the end user.

- `Tx.Commit()` - Converts the in-memory dirty nodes and the list of free pages
  into pages to be written to disk. Writing to disk then occurs in two phases.
  First, the dirty pages are written to disk and an `fsync()` occurs. Second, a
  new meta page with an incremented transaction ID is written and another
  `fsync()` occurs. This two phase write ensures that partially written data
  pages are ignored in the event of a crash since the meta page pointing to them
  is never written. Partially written meta pages are invalidated because they
  are written with a checksum.

If you have additional notes that could be helpful for others, please submit
them via pull request.


## Other Projects Using Bolt

Below is a list of public, open source projects that use Bolt:

* [BoltDbWeb](https://github.com/evnix/boltdbweb) - A web based GUI for BoltDB files.
* [Operation Go: A Routine Mission](http://gocode.io) - An online programming game for Golang using Bolt for user accounts and a leaderboard.
* [Bazil](https://bazil.org/) - A file system that lets your data reside where it is most convenient for it to reside.
* [DVID](https://github.com/janelia-flyem/dvid) - Added Bolt as optional storage engine and testing it against Basho-tuned leveldb.
* [Skybox Analytics](https://github.com/skybox/skybox) - A standalone funnel analysis tool for web analytics.
* [Scuttlebutt](https://github.com/benbjohnson/scuttlebutt) - Uses Bolt to store and process all Twitter mentions of GitHub projects.
* [Wiki](https://github.com/peterhellberg/wiki) - A tiny wiki using Goji, BoltDB and Blackfriday.
* [ChainStore](https://github.com/pressly/chainstore) - Simple key-value interface to a variety of storage engines organized as a chain of operations.
* [MetricBase](https://github.com/msiebuhr/MetricBase) - Single-binary version of Graphite.
* [Gitchain](https://github.com/gitchain/gitchain) - Decentralized, peer-to-peer Git repositories aka "Git meets Bitcoin".
* [event-shuttle](https://github.com/sclasen/event-shuttle) - A Unix system service to collect and reliably deliver messages to Kafka.
* [ipxed](https://github.com/kelseyhightower/ipxed) - Web interface and api for ipxed.
* [BoltStore](https://github.com/yosssi/boltstore) - Session store using Bolt.
* [photosite/session](https://godoc.org/bitbucket.org/kardianos/photosite/session) - Sessions for a photo viewing site.
* [LedisDB](https://github.com/siddontang/ledisdb) - A high performance NoSQL, using Bolt as optional storage.
* [ipLocator](https://github.com/AndreasBriese/ipLocator) - A fast ip-geo-location-server using bolt with bloom filters.
* [cayley](https://github.com/google/cayley) - Cayley is an open-source graph database using Bolt as optional backend.
* [bleve](http://www.blevesearch.com/) - A pure Go search engine similar to ElasticSearch that uses Bolt as the default storage backend.
* [tentacool](https://github.com/optiflows/tentacool) - REST api server to manage system stuff (IP, DNS, Gateway...) on a linux server.
* [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Highly scalable distributed key~file system with O(1) disk read.
* [InfluxDB](https://influxdata.com) - Scalable datastore for metrics, events, and real-time analytics.
* [Freehold](http://tshannon.bitbucket.org/freehold/) - An open, secure, and lightweight platform for your files and data.
* [Prometheus Annotation Server](https://github.com/oliver006/prom_annotation_server) - Annotation server for PromDash & Prometheus service monitoring system.
* [Consul](https://github.com/hashicorp/consul) - Consul is service discovery and configuration made easy. Distributed, highly available, and datacenter-aware.
* [Kala](https://github.com/ajvb/kala) - Kala is a modern job scheduler optimized to run on a single node. It is persistent, JSON over HTTP API, ISO 8601 duration notation, and dependent jobs.
* [drive](https://github.com/odeke-em/drive) - drive is an unofficial Google Drive command line client for \*NIX operating systems.
* [stow](https://github.com/djherbis/stow) -  a persistence manager for objects
  backed by boltdb.
* [buckets](https://github.com/joyrexus/buckets) - a bolt wrapper streamlining
  simple tx and key scans.
* [mbuckets](https://github.com/abhigupta912/mbuckets) - A Bolt wrapper that allows easy operations on multi level (nested) buckets.
* [Request Baskets](https://github.com/darklynx/request-baskets) - A web service to collect arbitrary HTTP requests and inspect them via REST API or simple web UI, similar to [RequestBin](http://requestb.in/) service
* [Go Report Card](https://goreportcard.com/) - Go code quality report cards as a (free and open source) service.
* [Boltdb Boilerplate](https://github.com/bobintornado/boltdb-boilerplate) - Boilerplate wrapper around bolt aiming to make simple calls one-liners.
* [lru](https://github.com/crowdriff/lru) - Easy to use Bolt-backed Least-Recently-Used (LRU) read-through cache with chainable remote stores.
* [Storm](https://github.com/asdine/storm) - Simple and powerful ORM for BoltDB.
* [GoWebApp](https://github.com/josephspurrier/gowebapp) - A basic MVC web application in Go using BoltDB.
* [SimpleBolt](https://github.com/xyproto/simplebolt) - A simple way to use BoltDB. Deals mainly with strings.
* [Algernon](https://github.com/xyproto/algernon) - A HTTP/2 web server with built-in support for Lua. Uses BoltDB as the default database backend.
* [MuLiFS](https://github.com/dankomiocevic/mulifs) - Music Library Filesystem creates a filesystem to organise your music files.
* [GoShort](https://github.com/pankajkhairnar/goShort) - GoShort is a URL shortener written in Golang and BoltDB for persistent key/value storage and for routing it's using high performent HTTPRouter.
* [torrent](https://github.com/anacrolix/torrent) - Full-featured BitTorrent client package and utilities in Go. BoltDB is a storage backend in development.
* [gopherpit](https://github.com/gopherpit/gopherpit) - A web service to manage Go remote import paths with custom domains
* [bolter](https://github.com/hasit/bolter) - Command-line app for viewing BoltDB file in your terminal.
* [btcwallet](https://github.com/btcsuite/btcwallet) - A bitcoin wallet.
* [dcrwallet](https://github.com/decred/dcrwallet) - A wallet for the Decred cryptocurrency.
* [Ironsmith](https://github.com/timshannon/ironsmith) - A simple, script-driven continuous integration (build - > test -> release) tool, with no external dependencies
* [BoltHold](https://github.com/timshannon/bolthold) - An embeddable NoSQL store for Go types built on BoltDB

If you are using Bolt in a project please send a pull request to add it to the list.
# gRPC-Go

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

This requires Go 1.6 or later.

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
Go generated proto packages
===========================

[![Build Status](https://travis-ci.org/google/go-genproto.svg?branch=master)](https://travis-ci.org/google/go-genproto)
[![GoDoc](https://godoc.org/google.golang.org/genproto?status.svg)](https://godoc.org/google.golang.org/genproto)

> **IMPORTANT** This repository is currently experimental. The structure
> of the contained packages is subject to change. Please see the original
> source repositories (listed below) to find out the status of the each
> protocol buffer's associated service.

This repository contains the generated Go packages for common protocol buffer
types, and the generated [gRPC][1] code necessary for interacting with Google's gRPC
APIs.

There are two sources for the proto files used in this repository:

1. [google/protobuf][2]: the code in the `protobuf` and `ptypes` subdirectories
   is derived from this repo. The messages in `protobuf` are used to describe
   protocol buffer messages themselves. The messages under `ptypes` define the
   common well-known types.
2. [googleapis/googleapis][3]: the code in the `googleapis` is derived from this
   repo. The packages here contain types specifically for interacting with Google
   APIs.

[1]: http://grpc.io
[2]: https://github.com/google/protobuf/
[3]: https://github.com/googleapis/googleapis/
# React-Native-Warpdrive
