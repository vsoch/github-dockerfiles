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

# Pure Go UUID implementation

This package provides immutable UUID structs and the functions
NewV3, NewV4, NewV5 and Parse() for generating versions 3, 4
and 5 UUIDs as specified in [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt).

## Installation

Use the `go` tool:

	$ go get github.com/nu7hatch/gouuid

## Usage

See [documentation and examples](http://godoc.org/github.com/nu7hatch/gouuid)
for more information.

## Copyright

Copyright (C) 2011 by Krzysztof Kowalik <chris@nu7hat.ch>. See [COPYING](https://github.com/nu7hatch/gouuid/tree/master/COPYING)
file for details.
# go-cmd/Cmd

[![Go Report Card](https://goreportcard.com/badge/github.com/go-cmd/cmd)](https://goreportcard.com/report/github.com/go-cmd/cmd) [![Build Status](https://travis-ci.org/go-cmd/cmd.svg?branch=master)](https://travis-ci.org/go-cmd/cmd) [![Coverage Status](https://coveralls.io/repos/github/go-cmd/cmd/badge.svg?branch=master)](https://coveralls.io/github/go-cmd/cmd?branch=master) [![GoDoc](https://godoc.org/github.com/go-cmd/cmd?status.svg)](https://godoc.org/github.com/go-cmd/cmd)

This package is a small but very useful wrapper around [os/exec.Cmd](https://golang.org/pkg/os/exec/#Cmd) for Linux and macOS that makes it safe and simple to run external commands in highly concurrent, asynchronous, real-time applications. Here's the look and feel:

```go
import "github.com/go-cmd/cmd"

// Start a long-running process, capture stdout and stderr
findCmd := cmd.NewCmd("find", "/", "--name" "needle")
statusChan := findCmd.Start() // non-blocking

ticker := time.NewTicker(2 * time.Second)

// Print last line of stdout every 2s
go func() {
  for range ticker.C {
    status := c.Status()
    n := len(status.Stdout)
    fmt.Println(status.Stdout[n - 1])
  }
}()

// Stop command after 1 hour
go func() {
  <-time.After(1 * time.Hour)
  findCmd.Stop()
}()

// Check if command is done
select {
case finalStatus := <-statusChan:
  // done
default:
  // no, still running
}

// Block waiting for command to exit, be stopped, or be killed
finalStatus := <-statusChan
```

That's it, only three methods: `Start`, `Stop`, and `Status`. When possible, it's better to use `go-cmd/Cmd` than `os/exec.Cmd` because `go-cmd/Cmd` provides:

1. Channel-based fire and forget
1. Real-time stdout and stderr
1. Real-time status
1. Complete and consolidated return
1. Proper process termination
1. _100%_ test coverage, no race conditions

### Channel-based fire and forget

As the example above shows, starting a command immediately returns a channel to which the final status is sent when the command exits for any reason. So by default commands run asynchronously, but running synchronously is possible and easy, too:

```go
// Run foo and block waiting for it to exit
c := cmd.NewCmd("foo")
s := <-c.Start()
```
To achieve similar with `os/exec.Cmd` requires everything this package already does.

### Real-time stdout and stderr

It's common to want to read stdout or stderr _while_ the command is running. The common approach is to call [StdoutPipe](https://golang.org/pkg/os/exec/#Cmd.StdoutPipe) and read from the provided `io.ReadCloser`. This works but it's wrong because it causes a race condition (that `go test -race` detects) and the docs say it's wrong: "it is incorrect to call Wait before all reads from the pipe have completed. [...] it is incorrect to call Run when using StdoutPipe".

The proper solution is to set the `io.Writer` of `Stdout`. To be thread-safe and non-racey, this requires further work to write while possibly N-many goroutines read. `go-cmd/Cmd` has done this work.

### Real-time status

Similar to real-time stdout and stderr, it's nice to see, for example, elapsed runtime. This package allows that: `Status` can be called any time by any goroutine, and it returns this struct:
```go
type Status struct {
    Cmd      string
    PID      int
    Complete bool
    Exit     int
    Error    error
    Runtime  float64 // seconds
    Stdout   []string
    Stderr   []string
}
```

### Complete and consolidated return

Speaking of that struct above, Go built-in `Cmd` does not put all the return information in one place, which is fine because Go is awesome! But to save some time, `go-cmd/Cmd` uses the `Status` struct above to convey all information about the command. Even when the command finishes, calling `Status` returns the final status, the same final status sent to the status channel returned by the call to `Start`.

### Proper process termination

[os/exec/Cmd.Wait](https://golang.org/pkg/os/exec/#Cmd.Wait) can block even after the command is killed. That can be surprising and cause problems. But `go-cmd/Cmd.Stop` reliably terminates the command, no surprises. The issue has to do with process group IDs. It's common to kill the command PID, but usually one needs to kill its process group ID instead. `go-cmd/Cmd.Stop` implements the necessary low-level magic to make this happen.

### 100% test coverage, no race conditions

In addition to 100% test coverage and no race conditions, this package is actively used in production environments.

---

## Acknowledgements

[Brian Ip](https://github.com/BrianIp) wrote the original code to get the exit status. Strangely, Go doesn't just provide this, it requires magic like `exiterr.Sys().(syscall.WaitStatus)` and more.
# Deep Variable Equality for Humans

[![Go Report Card](https://goreportcard.com/badge/github.com/go-test/deep)](https://goreportcard.com/report/github.com/go-test/deep) [![Build Status](https://travis-ci.org/go-test/deep.svg?branch=master)](https://travis-ci.org/go-test/deep) [![Coverage Status](https://coveralls.io/repos/github/go-test/deep/badge.svg?branch=master)](https://coveralls.io/github/go-test/deep?branch=master) [![GoDoc](https://godoc.org/github.com/go-test/deep?status.svg)](https://godoc.org/github.com/go-test/deep)

This package provides a single function: `deep.Equal`. It's like [reflect.DeepEqual](http://golang.org/pkg/reflect/#DeepEqual) but much friendlier to humans (or any sentient being) for two reason:

* `deep.Equal` returns a list of differences
* `deep.Equal` does not compare unexported fields (by default)

`reflect.DeepEqual` is good (like all things Golang!), but it's a game of [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus). For large maps, slices, and structs, finding the difference is difficult.

`deep.Equal` doesn't play games with you, it lists the differences:

```go
package main_test

import (
	"testing"
	"github.com/go-test/deep"
)

type T struct {
	Name    string
	Numbers []float64
}

func TestDeepEqual(t *testing.T) {
	// Can you spot the difference?
	t1 := T{
		Name:    "Isabella",
		Numbers: []float64{1.13459, 2.29343, 3.010100010},
	}
	t2 := T{
		Name:    "Isabella",
		Numbers: []float64{1.13459, 2.29843, 3.010100010},
	}

	if diff := deep.Equal(t1, t2); diff != nil {
		t.Error(diff)
	}
}
```


```
$ go test
--- FAIL: TestDeepEqual (0.00s)
        main_test.go:25: [Numbers.slice[1]: 2.29343 != 2.29843]
```

The difference is in `Numbers.slice[1]`: the two values aren't equal using Go `==`.
# gRPC-Go

[![Build Status](https://travis-ci.org/grpc/grpc-go.svg)](https://travis-ci.org/grpc/grpc-go) [![GoDoc](https://godoc.org/google.golang.org/grpc?status.svg)](https://godoc.org/google.golang.org/grpc) [![GoReportCard](https://goreportcard.com/badge/grpc/grpc-go)](https://goreportcard.com/report/github.com/grpc/grpc-go)

The Go implementation of [gRPC](https://grpc.io/): A high performance, open source, general RPC framework that puts mobile and HTTP/2 first. For more information see the [gRPC Quick Start: Go](https://grpc.io/docs/quickstart/go.html) guide.

Installation
------------

To install this package, you need to install Go and setup your Go workspace on your computer. The simplest way to install the library is to run:

```
$ go get -u google.golang.org/grpc
```

Prerequisites
-------------

This requires Go 1.6 or later. Go 1.7 will be required soon.

Constraints
-----------
The grpc package should only depend on standard Go packages and a small number of exceptions. If your contribution introduces new dependencies which are NOT in the [list](http://godoc.org/google.golang.org/grpc?imports), you need a discussion with gRPC-Go authors and consultants.

Documentation
-------------
See [API documentation](https://godoc.org/google.golang.org/grpc) for package and API descriptions and find examples in the [examples directory](examples/).

Performance
-----------
See the current benchmarks for some of the languages supported in [this dashboard](https://performance-dot-grpc-testing.appspot.com/explore?dashboard=5652536396611584&widget=490377658&container=1286539696).

Status
------
General Availability [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages).

FAQ
---

#### Compiling error, undefined: grpc.SupportPackageIsVersion

Please update proto package, gRPC package and rebuild the proto files:
 - `go get -u github.com/golang/protobuf/{proto,protoc-gen-go}`
 - `go get -u google.golang.org/grpc`
 - `protoc --go_out=plugins=grpc:. *.proto`

#### How to turn on logging

The default logger is controlled by the environment variables. Turn everything
on by setting:

```
GRPC_GO_LOG_VERBOSITY_LEVEL=99 GRPC_GO_LOG_SEVERITY_LEVEL=info
```

#### The RPC failed with error `"code = Unavailable desc = transport is closing"`

This error means the connection the RPC is using was closed, and there are many
possible reasons, including:
 1. mis-configured transport credentials, connection failed on handshaking
 1. bytes disrupted, possibly by a proxy in between
 1. server shutdown

It can be tricky to debug this because the error happens on the client side but
the root cause of the connection being closed is on the server side. Turn on
logging on __both client and server__, and see if there are any transport
errors.
