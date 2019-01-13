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
- updating unversioned source files.This repository provides Go concurrency primitives in addition to the
ones provided by the language and "sync" and "sync/atomic" packages.
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
go-shlex is a simple lexer for go that supports shell-style quoting,
commenting, and escaping.
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
# OCI Image Format Specification
<div>
<a href="https://travis-ci.org/opencontainers/image-spec">
<img src="https://travis-ci.org/opencontainers/image-spec.svg?branch=master"></img>
</a>
</div>

The OCI Image Format project creates and maintains the software shipping container image format spec (OCI Image Format).

**[The specification can be found here](spec.md).**

This repository also provides [Go types](specs-go), [intra-blob validation tooling, and JSON Schema](schema).
The Go types and validation should be compatible with the current Go release; earlier Go releases are not supported.

Additional documentation about how this group operates:

- [Code of Conduct](https://github.com/opencontainers/tob/blob/d2f9d68c1332870e40693fe077d311e0742bc73d/code-of-conduct.md)
- [Roadmap](#roadmap)
- [Releases](RELEASES.md)
- [Project Documentation](project.md)

The _optional_ and _base_ layers of all OCI projects are tracked in the [OCI Scope Table](https://www.opencontainers.org/about/oci-scope-table).

## Running an OCI Image

The OCI Image Format partner project is the [OCI Runtime Spec project](https://github.com/opencontainers/runtime-spec).
The Runtime Specification outlines how to run a "[filesystem bundle](https://github.com/opencontainers/runtime-spec/blob/master/bundle.md)" that is unpacked on disk.
At a high-level an OCI implementation would download an OCI Image then unpack that image into an OCI Runtime filesystem bundle.
At this point the OCI Runtime Bundle would be run by an OCI Runtime.

This entire workflow supports the UX that users have come to expect from container engines like Docker and rkt: primarily, the ability to run an image with no additional arguments:

* docker run example.com/org/app:v1.0.0
* rkt run example.com/org/app,version=v1.0.0

To support this UX the OCI Image Format contains sufficient information to launch the application on the target platform (e.g. command, arguments, environment variables, etc).

## FAQ

**Q: Why doesn't this project mention distribution?**

A: Distribution, for example using HTTP as both Docker v2.2 and AppC do today, is currently out of scope on the [OCI Scope Table](https://www.opencontainers.org/about/oci-scope-table).
There has been [some discussion on the TOB mailing list](https://groups.google.com/a/opencontainers.org/d/msg/tob/A3JnmI-D-6Y/tLuptPDHAgAJ) to make distribution an optional layer, but this topic is a work in progress.

**Q: What happens to AppC or Docker Image Formats?**

A: Existing formats can continue to be a proving ground for technologies, as needed.
The OCI Image Format project strives to provide a dependable open specification that can be shared between different tools and be evolved for years or decades of compatibility; as the deb and rpm format have.

Find more [FAQ on the OCI site](https://www.opencontainers.org/faq).

## Roadmap

The [GitHub milestones](https://github.com/opencontainers/image-spec/milestones) lay out the path to the OCI v1.0.0 release in late 2016.

# Contributing

Development happens on GitHub for the spec.
Issues are used for bugs and actionable items and longer discussions can happen on the [mailing list](#mailing-list).

The specification and code is licensed under the Apache 2.0 license found in the `LICENSE` file of this repository.

## Discuss your design

The project welcomes submissions, but please let everyone know what you are working on.

Before undertaking a nontrivial change to this specification, send mail to the [mailing list](#mailing-list) to discuss what you plan to do.
This gives everyone a chance to validate the design, helps prevent duplication of effort, and ensures that the idea fits.
It also guarantees that the design is sound before code is written; a GitHub pull-request is not the place for high-level discussions.

Typos and grammatical errors can go straight to a pull-request.
When in doubt, start on the [mailing-list](#mailing-list).

## Weekly Call

The contributors and maintainers of all OCI projects have a weekly meeting Wednesdays at 2:00 PM (USA Pacific).
Everyone is welcome to participate via [UberConference web][UberConference] or audio-only: +1-415-968-0849 (no PIN needed).
An initial agenda will be posted to the [mailing list](#mailing-list) earlier in the week, and everyone is welcome to propose additional topics or suggest other agenda alterations there.
Minutes are posted to the [mailing list](#mailing-list) and minutes from past calls are archived [here][minutes].

## Mailing List

You can subscribe and join the mailing list on [Google Groups](https://groups.google.com/a/opencontainers.org/forum/#!forum/dev).

## IRC

OCI discussion happens on #opencontainers on Freenode ([logs][irc-logs]).

## Markdown style

To keep consistency throughout the Markdown files in the Open Container spec all files should be formatted one sentence per line.
This fixes two things: it makes diffing easier with git and it resolves fights about line wrapping length.
For example, this paragraph will span three lines in the Markdown source.

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


[UberConference]: https://www.uberconference.com/opencontainers
[irc-logs]: http://ircbot.wl.linuxfoundation.org/eavesdrop/%23opencontainers/
[minutes]: http://ircbot.wl.linuxfoundation.org/meetings/opencontainers/
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/sirupsen/logrus.svg?branch=master)](https://travis-ci.org/sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/sirupsen/logrus?status.svg)](https://godoc.org/github.com/sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc]. **Please note the Logrus API is not
yet stable (pre 1.0). Logrus itself is completely stable and has been used in
many large deployments. The core API is unlikely to change much but please
version control your Logrus to make sure you aren't fetching latest `master` on
every build.**

**Seeing weird case-sensitive problems?** Unfortunately, the author failed to
realize the consequences of renaming to lower-case. Due to the Go package
environment, this caused issues. Regretfully, there's no turning back now.
Everything using `logrus` will need to use the lower-case:
`github.com/sirupsen/logrus`. Any package that isn't, should be changed.

I am terribly sorry for this inconvenience. Logrus strives hard for backwards
compatibility, and the author failed to realize the cascading consequences of
such a name-change. To fix Glide, see [these
comments](https://github.com/sirupsen/logrus/issues/553#issuecomment-306591437).

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
| [KafkaLogrus](https://github.com/goibibo/KafkaLogrus) | Hook for logging to kafka |
| [LFShook](https://github.com/rifflock/lfshook) | Hook for logging to the local filesystem |
| [Logentries](https://github.com/jcftang/logentriesrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logentrus](https://github.com/puddingfactory/logentrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [Mail](https://github.com/zbindenren/logrus_mail) | Hook for sending exceptions via mail |
| [Mongodb](https://github.com/weekface/mgorus) | Hook for logging to mongodb |
| [NATS-Hook](https://github.com/rybit/nats_logrus_hook) | Hook for logging to [NATS](https://nats.io) |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [Papertrail](https://github.com/polds/logrus-papertrail-hook) | Send errors to the [Papertrail](https://papertrailapp.com) hosted logging service via UDP. |
| [PostgreSQL](https://github.com/gemnasium/logrus-postgresql-hook) | Send logs to [PostgreSQL](http://postgresql.org) |
| [Pushover](https://github.com/toorop/logrus_pushover) | Send error via [Pushover](https://pushover.net) |
| [Raygun](https://github.com/squirkle/logrus-raygun-hook) | Hook for logging to [Raygun.io](http://raygun.io/) |
| [Redis-Hook](https://github.com/rogierlommers/logrus-redis-hook) | Hook for logging to a ELK stack (through Redis) |
| [Rollrus](https://github.com/heroku/rollrus) | Hook for sending errors to rollbar |
| [Scribe](https://github.com/sagar8192/logrus-scribe-hook) | Hook for logging to [Scribe](https://github.com/facebookarchive/scribe)|
| [Sentry](https://github.com/evalphobia/logrus_sentry) | Send errors to the Sentry error logging and aggregation service. |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Stackdriver](https://github.com/knq/sdhook) | Hook for logging to [Google Stackdriver](https://cloud.google.com/logging/) |
| [Sumorus](https://github.com/doublefree/sumorus) | Hook for logging to [SumoLogic](https://www.sumologic.com/)|
| [Syslog](https://github.com/Sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [Syslog TLS](https://github.com/shinji62/logrus-syslog-ng) | Send errors to remote syslog server with TLS support. |
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
  "github.com/sirupsen/logrus/hooks/null"
  "github.com/stretchr/testify/assert"
  "testing"
)

func TestSomething(t*testing.T){
  logger, hook := null.NewNullLogger()
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
Package locker is a simple package to manage named ReadWrite mutexes. These
appear to be especially useful for synchronizing access to session based
information in web applications.

The common use case is to use the package level functions, which use a package
level set of locks (safe to use from multiple goroutines simultaneously).
However, you may also create a new separate set of locks.

All locks are implemented with read-write mutexes. To use them like a regular
mutex, simply ignore the RLock/RUnlock functions.


### Installation

    go get github.com/BurntSushi/locker


### Documentation

http://godoc.org/github.com/BurntSushi/locker

![banner](/docs/images/containerd-dark.png?raw=true)

[![GoDoc](https://godoc.org/github.com/containerd/containerd?status.svg)](https://godoc.org/github.com/containerd/containerd)
[![Build Status](https://travis-ci.org/containerd/containerd.svg?branch=master)](https://travis-ci.org/containerd/containerd)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fcontainerd%2Fcontainerd.svg?type=shield)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fcontainerd%2Fcontainerd?ref=badge_shield)
[![Go Report Card](https://goreportcard.com/badge/github.com/containerd/containerd)](https://goreportcard.com/report/github.com/containerd/containerd)

containerd is an industry-standard container runtime with an emphasis on simplicity, robustness and portability. It is available as a daemon for Linux and Windows, which can manage the complete container lifecycle of its host system: image transfer and storage, container execution and supervision, low-level storage and network attachments, etc.

containerd is designed to be embedded into a larger system, rather than being used directly by developers or end-users.

## Getting Started

If you are interested in trying out containerd please see our [Getting Started Guide](docs/getting-started.md).

## Features

### Client

containerd offers a full client package to help you integrate containerd into your platform.

```go

import "github.com/containerd/containerd"

func main() {
	client, err := containerd.New("/run/containerd/containerd.sock")
	defer client.Close()
}

```

### Namespaces

Namespaces allow multiple consumers to use the same containerd without conflicting with each other.  It has the benefit of sharing content but still having separation with containers and images.

To set a namespace for requests to the API:

```go
context    = context.Background()
// create a context for docker
docker = namespaces.WithNamespace(context, "docker")

containerd, err := client.NewContainer(docker, "id")
```

To set a default namespace on the client:

```go
client, err := containerd.New(address, containerd.WithDefaultNamespace("docker"))
```

### Distribution

```go
// pull an image
image, err := client.Pull(context, "docker.io/library/redis:latest")

// push an image
err := client.Push(context, "docker.io/library/redis:latest", image.Target())
```

### Containers

In containerd, a container is a metadata object.  Resources such as an OCI runtime specification, image, root filesystem, and other metadata can be attached to a container.

```go
redis, err := client.NewContainer(context, "redis-master")
defer redis.Delete(context)
```

### OCI Runtime Specification

containerd fully supports the OCI runtime specification for running containers.  We have built in functions to help you generate runtime specifications based on images as well as custom parameters.

You can specify options when creating a container about how to modify the specification.

```go
redis, err := client.NewContainer(context, "redis-master", containerd.WithNewSpec(containerd.WithImageConfig(image)))
```

## Root Filesystems

containerd allows you to use overlay or snapshot filesystems with your containers.  It comes with builtin support for overlayfs and btrfs.

```go
// pull an image and unpack it into the configured snapshotter
image, err := client.Pull(context, "docker.io/library/redis:latest", containerd.WithPullUnpack)

// allocate a new RW root filesystem for a container based on the image
redis, err := client.NewContainer(context, "redis-master",
	containerd.WithNewSnapshot("redis-rootfs", image),
	containerd.WithNewSpec(containerd.WithImageConfig(image)),

)

// use a readonly filesystem with multiple containers
for i := 0; i < 10; i++ {
	id := fmt.Sprintf("id-%s", i)
	container, err := client.NewContainer(ctx, id,
		containerd.WithNewSnapshotView(id, image),
		containerd.WithNewSpec(containerd.WithImageConfig(image)),
	)
}
```

### Tasks

Taking a container object and turning it into a runnable process on a system is done by creating a new `Task` from the container.  A task represents the runnable object within containerd.

```go
// create a new task
task, err := redis.NewTask(context, containerd.Stdio)
defer task.Delete(context)

// the task is now running and has a pid that can be use to setup networking
// or other runtime settings outside of containerd
pid := task.Pid()

// start the redis-server process inside the container
err := task.Start(context)

// wait for the task to exit and get the exit status
status, err := task.Wait(context)
```

### Checkpoint and Restore

If you have [criu](https://criu.org/Main_Page) installed on your machine you can checkpoint and restore containers and their tasks.  This allow you to clone and/or live migrate containers to other machines.

```go
// checkpoint the task then push it to a registry
checkpoint, err := task.Checkpoint(context, containerd.WithExit)

err := client.Push(context, "myregistry/checkpoints/redis:master", checkpoint)

// on a new machine pull the checkpoint and restore the redis container
image, err := client.Pull(context, "myregistry/checkpoints/redis:master")

checkpoint := image.Target()

redis, err = client.NewContainer(context, "redis-master", containerd.WithCheckpoint(checkpoint, "redis-rootfs"))
defer container.Delete(context)

task, err = redis.NewTask(context, containerd.Stdio, containerd.WithTaskCheckpoint(checkpoint))
defer task.Delete(context)

err := task.Start(context)
```

### Developer Quick-Start

To build the daemon and `ctr` simple test client, the following build system dependencies are required:

* Go 1.8.x or above (requires 1.8 due to use of golang plugin(s))
* Protoc 3.x compiler and headers (download at the [Google protobuf releases page](https://github.com/google/protobuf/releases))
* Btrfs headers and libraries for your distribution. Note that building the btrfs driver can be disabled via build tag removing this dependency.

For proper results, install the `protoc` release into `/usr/local` on your build system. For example, the following commands will download and install the 3.1.0 release for a 64-bit Linux host:

```
$ wget -c https://github.com/google/protobuf/releases/download/v3.1.0/protoc-3.1.0-linux-x86_64.zip
$ sudo unzip protoc-3.1.0-linux-x86_64.zip -d /usr/local
```

With the required dependencies installed, the `Makefile` target named **binaries** will compile the `ctr` and `containerd` binaries and place them in the `bin/` directory. Using `sudo make install` will place the binaries in `/usr/local/bin`. When making any changes to the gRPC API, `make generate` will use the installed `protoc` compiler to regenerate the API generated code packages.

> *Note*: A build tag is currently available to disable building the btrfs snapshot driver.
> Adding `BUILDTAGS=no_btrfs` to your environment before calling the **binaries**
> Makefile target will disable the btrfs driver within the containerd Go build.

Vendoring of external imports uses the [`vndr` tool](https://github.com/LK4D4/vndr) which uses a simple config file, `vendor.conf`, to provide the URL and version or hash details for each vendored import. After modifying `vendor.conf` run the `vndr` tool to update the `vendor/` directory contents. Combining the `vendor.conf` update with the changeset in `vendor/` after running `vndr` should become a single commit for a PR which relies on vendored updates.

Please refer to [RUNC.md](/RUNC.md) for the currently supported version of `runc` that is used by containerd.

### Releases and API Stability

Please see [RELEASES.md](RELEASES.md) for details on versioning and stability
of containerd components.

### Development reports.

Weekly summary on the progress and what is being worked on.
https://github.com/containerd/containerd/tree/master/reports

### Communication

For async communication and long running discussions please use issues and pull requests on the github repo.
This will be the best place to discuss design and implementation.

For sync communication we have a community slack with a #containerd channel that everyone is welcome to join and chat about development.

**Slack:** https://dockr.ly/community

### Reporting security issues

__If you are reporting a security issue, please follow the responsible
disclosure guidelines and reach out discreetly at containerd-security@googlegroups.com__.

## Copyright and license

Copyright ©2016-2017 Docker, Inc. All rights reserved, except as follows. Code
is released under the Apache 2.0 license. The README.md file, and files in the
"docs" folder are licensed under the Creative Commons Attribution 4.0
International License under the terms and conditions set forth in the file
"LICENSE.docs". You may obtain a duplicate copy of the same license, titled
CC-BY-SA-4.0, at http://creativecommons.org/licenses/by/4.0/.
[![GoDoc](https://godoc.org/github.com/docker/go-units?status.svg)](https://godoc.org/github.com/docker/go-units)

# Introduction

go-units is a library to transform human friendly measurements into machine friendly values.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-units) for examples and documentation.

## Copyright and license

Copyright © 2015 Docker, Inc.

go-units is licensed under the Apache License, Version 2.0.
See [LICENSE](LICENSE) for the full text of the license.
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
created. For more information see [docker/migrator](https://github.com/docker/migrator).

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
### Docker users, see [Moby and Docker](https://mobyproject.org/#moby-and-docker) to clarify the relationship between the projects

### Docker maintainers and contributors, see [Transitioning to Moby](#transitioning-to-moby) for more details

The Moby Project
================

![Moby Project logo](docs/static_files/moby-project-logo.png "The Moby Project")

Moby is an open-source project created by Docker to advance the software containerization movement.
It provides a “Lego set” of dozens of components, the framework for assembling them into custom container-based systems, and a place for all container enthusiasts to experiment and exchange ideas.

# Moby

## Overview

At the core of Moby is a framework to assemble specialized container systems.
It provides:

- A library of containerized components for all vital aspects of a container system: OS, container runtime, orchestration, infrastructure management, networking, storage, security, build, image distribution, etc.
- Tools to assemble the components into runnable artifacts for a variety of platforms and architectures: bare metal (both x86 and Arm); executables for Linux, Mac and Windows; VM images for popular cloud and virtualization providers.
- A set of reference assemblies which can be used as-is, modified, or used as inspiration to create your own.

All Moby components are containers, so creating new components is as easy as building a new OCI-compatible container.

## Principles

Moby is an open project guided by strong principles, but modular, flexible and without too strong an opinion on user experience, so it is open to the community to help set its direction.
The guiding principles are:

- Batteries included but swappable: Moby includes enough components to build fully featured container system, but its modular architecture ensures that most of the components can be swapped by different implementations.
- Usable security: Moby will provide secure defaults without compromising usability.
- Container centric: Moby is built with containers, for running containers.

With Moby, you should be able to describe all the components of your distributed application, from the high-level configuration files down to the kernel you would like to use and build and deploy it easily.

Moby uses [containerd](https://github.com/containerd/containerd) as the default container runtime.

## Audience

Moby is recommended for anyone who wants to assemble a container-based system. This includes:

- Hackers who want to customize or patch their Docker build
- System engineers or integrators building a container system
- Infrastructure providers looking to adapt existing container systems to their environment
- Container enthusiasts who want to experiment with the latest container tech
- Open-source developers looking to test their project in a variety of different systems
- Anyone curious about Docker internals and how it’s built

Moby is NOT recommended for:

- Application developers looking for an easy way to run their applications in containers. We recommend Docker CE instead.
- Enterprise IT and development teams looking for a ready-to-use, commercially supported container platform. We recommend Docker EE instead.
- Anyone curious about containers and looking for an easy way to learn. We recommend the [docker.com](https://www.docker.com/) website instead.

# Transitioning to Moby

Docker is transitioning all of its open source collaborations to the Moby project going forward.
During the transition, all open source activity should continue as usual.

We are proposing the following list of changes:

- splitting up the engine into more open components
- removing the docker UI, SDK etc to keep them in the Docker org
- clarifying that the project is not limited to the engine, but to the assembly of all the individual components of the Docker platform
- open-source new tools & components which we currently use to assemble the Docker product, but could benefit the community
- defining an open, community-centric governance inspired by the Fedora project (a very successful example of balancing the needs of the community with the constraints of the primary corporate sponsor)

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

## Swagger definition

The API is defined by the [Swagger](http://swagger.io/specification/) definition in `api/swagger.yaml`. This definition can be used to:

1. Automatically generate documentation.
2. Automatically generate the Go server and client. (A work-in-progress.)
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
pkg/ is a collection of utility packages used by the Docker project without being specific to its internals.

Utility packages are kept separate from the docker core codebase to keep it as small and concise as possible.
If some utilities grow larger and their APIs stabilize, they may be moved to their own repository under the
Docker organization, to facilitate re-use by other projects. However that is not the priority.

The directory `pkg` is named after the same directory in the camlistore project. Since Brad is a core
Go maintainer, we thought it made sense to copy his methods for organizing Go code :) Thanks Brad!

Because utility packages are small and neatly separated from the rest of the codebase, they are a good
place to start for aspiring maintainers and contributors. Get in touch if you want to help maintain them!
This package provides helper functions for dealing with signals across various operating systems## About

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
# Integration Testing on Swarm

IT on Swarm allows you to execute integration test in parallel across a Docker Swarm cluster

## Architecture

### Master service

  - Works as a funker caller
  - Calls a worker funker (`-worker-service`) with a chunk of `-check.f` filter strings (passed as a file via `-input` flag, typically `/mnt/input`)

### Worker service

  - Works as a funker callee
  - Executes an equivalent of `TESTFLAGS=-check.f TestFoo|TestBar|TestBaz ... make test-integration-cli` using the bind-mounted API socket (`docker.sock`)

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
[![GoDoc](https://godoc.org/github.com/docker/go-connections?status.svg)](https://godoc.org/github.com/docker/go-connections)

# Introduction

go-connections provides common package to work with network connections.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-connections) for examples and documentation.

## License

go-connections is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
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
