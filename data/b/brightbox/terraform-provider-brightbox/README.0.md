# complete

A tool for bash writing bash completion in go, and bash completion for the go command line.

[![Build Status](https://travis-ci.org/posener/complete.svg?branch=master)](https://travis-ci.org/posener/complete)
[![codecov](https://codecov.io/gh/posener/complete/branch/master/graph/badge.svg)](https://codecov.io/gh/posener/complete)
[![GoDoc](https://godoc.org/github.com/posener/complete?status.svg)](http://godoc.org/github.com/posener/complete)
[![Go Report Card](https://goreportcard.com/badge/github.com/posener/complete)](https://goreportcard.com/report/github.com/posener/complete)

Writing bash completion scripts is a hard work. This package provides an easy way
to create bash completion scripts for any command, and also an easy way to install/uninstall
the completion of the command.

## go command bash completion

In [gocomplete](./gocomplete) there is an example for bash completion for the `go` command line.

This is an example that uses the `complete` package on the `go` command - the `complete` package
can also be used to implement any completions, see [Usage](#usage).

### Install

1. Type in your shell:
```
go get -u github.com/posener/complete/gocomplete
gocomplete -install
```

2. Restart your shell

Uninstall by `gocomplete -uninstall`

### Features

- Complete `go` command, including sub commands and all flags.
- Complete packages names or `.go` files when necessary.
- Complete test names after `-run` flag.

## complete package

Supported shells:

- [x] bash
- [x] zsh
- [x] fish

### Usage

Assuming you have program called `run` and you want to have bash completion
for it, meaning, if you type `run` then space, then press the `Tab` key,
the shell will suggest relevant complete options.

In that case, we will create a program called `runcomplete`, a go program,
with a `func main()` and so, that will make the completion of the `run`
program. Once the `runcomplete` will be in a binary form, we could 
`runcomplete -install` and that will add to our shell all the bash completion
options for `run`.

So here it is:

```go
import "github.com/posener/complete"

func main() {

	// create a Command object, that represents the command we want
	// to complete.
	run := complete.Command{

		// Sub defines a list of sub commands of the program,
		// this is recursive, since every command is of type command also.
		Sub: complete.Commands{

			// add a build sub command
			"build": complete.Command {

				// define flags of the build sub command
				Flags: complete.Flags{
					// build sub command has a flag '-cpus', which
					// expects number of cpus after it. in that case
					// anything could complete this flag.
					"-cpus": complete.PredictAnything,
				},
			},
		},

		// define flags of the 'run' main command
		Flags: complete.Flags{
			// a flag -o, which expects a file ending with .out after
			// it, the tab completion will auto complete for files matching
			// the given pattern.
			"-o": complete.PredictFiles("*.out"),
		},

		// define global flags of the 'run' main command
		// those will show up also when a sub command was entered in the
		// command line
		GlobalFlags: complete.Flags{

			// a flag '-h' which does not expects anything after it
			"-h": complete.PredictNothing,
		},
	}

	// run the command completion, as part of the main() function.
	// this triggers the autocompletion when needed.
	// name must be exactly as the binary that we want to complete.
	complete.New("run", run).Run()
}
```

### Self completing program

In case that the program that we want to complete is written in go we
can make it self completing.

Here is an [example](./example/self/main.go)
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
# OAuth2 for Go

[![Build Status](https://travis-ci.org/golang/oauth2.svg?branch=master)](https://travis-ci.org/golang/oauth2)
[![GoDoc](https://godoc.org/golang.org/x/oauth2?status.svg)](https://godoc.org/golang.org/x/oauth2)

oauth2 package contains a client implementation for OAuth 2.0 spec.

## Installation

~~~~
go get golang.org/x/oauth2
~~~~

Or you can manually git clone the repository to
`$(go env GOPATH)/src/golang.org/x/oauth2`.

See godoc for further documentation and examples.

* [godoc.org/golang.org/x/oauth2](http://godoc.org/golang.org/x/oauth2)
* [godoc.org/golang.org/x/oauth2/google](http://godoc.org/golang.org/x/oauth2/google)


## App Engine

In change 96e89be (March 2015), we removed the `oauth2.Context2` type in favor
of the [`context.Context`](https://golang.org/x/net/context#Context) type from
the `golang.org/x/net/context` package

This means it's no longer possible to use the "Classic App Engine"
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

```go
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
```

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the oauth2 repository is located at
https://github.com/golang/oauth2/issues.
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
# Brightbox Golang Client

`gobrightbox` is a [Brightbox Cloud](https://www.brightbox.com) [API](https://api.gb1.brightbox.com/1.0/)
client implementation written in [Go](http://golang.org/).

Documentation is available at [godoc.org](http://godoc.org/github.com/brightbox/gobrightbox).

## Authentication

This client does not itself handle authentication. Instead, use the standard
[OAuth2](https://godoc.org/golang.org/x/oauth2) golang library to
[authenticate](https://api.gb1.brightbox.com/1.0/#authentication) and create
tokens.

## Currently implemented

* Full [Server](https://api.gb1.brightbox.com/1.0/#server) support
* Full [Server Group](https://api.gb1.brightbox.com/1.0/#server_group) support
* Full [CloudIP](https://api.gb1.brightbox.com/1.0/#cloud_ip) support
* Full [Firewall Policy](https://api.gb1.brightbox.com/1.0/#firewall_policy) support
* Full [Load Balancer](https://api.gb1.brightbox.com/1.0/#load_balancer) support
* Full [Cloud SQL](https://api.gb1.brightbox.com/1.0/#database_server) support
* Full [Api Client](https://api.gb1.brightbox.com/1.0/#api_client) support
* Basic [Image](https://api.gb1.brightbox.com/1.0/#image) support
* Basic event stream support

## TODO

* Orbit storage support
* Collaboration support
* User support
* Account support
* Cloud SQL Snapshot support
* Cloud SQL Type support

## Help

If you need help using this library, drop an email to support at brightbox dot com.

## License

This code is released under an MIT License.

Copyright (c) 2015-2016 Brightbox Systems Ltd.
semver for golang [![Build Status](https://travis-ci.org/blang/semver.svg?branch=master)](https://travis-ci.org/blang/semver) [![GoDoc](https://godoc.org/github.com/blang/semver?status.png)](https://godoc.org/github.com/blang/semver) [![Coverage Status](https://img.shields.io/coveralls/blang/semver.svg)](https://coveralls.io/r/blang/semver?branch=master)
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
- Wildcards `>=1.x`, `<=2.5.x`
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

Note that spaces between the operator and the version will be gracefully tolerated.

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
# Golang Link Header Parser

Library for parsing HTTP Link headers. Requires Go 1.2 or higher.

Docs can be found on [the GoDoc page](https://godoc.org/github.com/tomnomnom/linkheader).

[![Build Status](https://travis-ci.org/tomnomnom/linkheader.svg)](https://travis-ci.org/tomnomnom/linkheader)

## Basic Example

```go
package main

import (
	"fmt"

	"github.com/tomnomnom/linkheader"
)

func main() {
	header := "<https://api.github.com/user/58276/repos?page=2>; rel=\"next\"," +
		"<https://api.github.com/user/58276/repos?page=2>; rel=\"last\""
	links := linkheader.Parse(header)

	for _, link := range links {
		fmt.Printf("URL: %s; Rel: %s\n", link.URL, link.Rel)
	}
}

// Output:
// URL: https://api.github.com/user/58276/repos?page=2; Rel: next
// URL: https://api.github.com/user/58276/repos?page=2; Rel: last
```


# Package xz

This Go language package supports the reading and writing of xz
compressed streams. It includes also a gxz command for compressing and
decompressing data. The package is completely written in Go and doesn't
have any dependency on any C code.

The package is currently under development. There might be bugs and APIs
are not considered stable. At this time the package cannot compete with
the xz tool regarding compression speed and size. The algorithms there
have been developed over a long time and are highly optimized. However
there are a number of improvements planned and I'm very optimistic about
parallel compression and decompression. Stay tuned!

# Using the API

The following example program shows how to use the API.

    package main

    import (
        "bytes"
        "io"
        "log"
        "os"

        "github.com/ulikunitz/xz"
    )

    func main() {
        const text = "The quick brown fox jumps over the lazy dog.\n"
        var buf bytes.Buffer
        // compress text
        w, err := xz.NewWriter(&buf)
        if err != nil {
            log.Fatalf("xz.NewWriter error %s", err)
        }
        if _, err := io.WriteString(w, text); err != nil {
            log.Fatalf("WriteString error %s", err)
        }
        if err := w.Close(); err != nil {
            log.Fatalf("w.Close error %s", err)
        }
        // decompress buffer and write output to stdout
        r, err := xz.NewReader(&buf)
        if err != nil {
            log.Fatalf("NewReader error %s", err)
        }
        if _, err = io.Copy(os.Stdout, r); err != nil {
            log.Fatalf("io.Copy error %s", err)
        }
    }

# Using the gxz compression tool

The package includes a gxz command line utility for compression and
decompression.

Use following command for installation:

    $ go get github.com/ulikunitz/xz/cmd/gxz

To test it call the following command.

    $ gxz bigfile

After some time a much smaller file bigfile.xz will replace bigfile.
To decompress it use the following command.

    $ gxz -d bigfile.xz

# A Go package for calculating the Levenshtein distance between two strings

[![Release](https://img.shields.io/github/release/agext/levenshtein.svg?style=flat)](https://github.com/agext/levenshtein/releases/latest)
[![GoDoc](https://img.shields.io/badge/godoc-reference-blue.svg?style=flat)](https://godoc.org/github.com/agext/levenshtein) 
[![Build Status](https://travis-ci.org/agext/levenshtein.svg?branch=master&style=flat)](https://travis-ci.org/agext/levenshtein)
[![Coverage Status](https://coveralls.io/repos/github/agext/levenshtein/badge.svg?style=flat)](https://coveralls.io/github/agext/levenshtein)
[![Go Report Card](https://goreportcard.com/badge/github.com/agext/levenshtein?style=flat)](https://goreportcard.com/report/github.com/agext/levenshtein)


This package implements distance and similarity metrics for strings, based on the Levenshtein measure, in [Go](http://golang.org).

## Project Status

v1.2.1 Stable: Guaranteed no breaking changes to the API in future v1.x releases. Probably safe to use in production, though provided on "AS IS" basis.

This package is being actively maintained. If you encounter any problems or have any suggestions for improvement, please [open an issue](https://github.com/agext/levenshtein/issues). Pull requests are welcome.

## Overview

The Levenshtein `Distance` between two strings is the minimum total cost of edits that would convert the first string into the second. The allowed edit operations are insertions, deletions, and substitutions, all at character (one UTF-8 code point) level. Each operation has a default cost of 1, but each can be assigned its own cost equal to or greater than 0.

A `Distance` of 0 means the two strings are identical, and the higher the value the more different the strings. Since in practice we are interested in finding if the two strings are "close enough", it often does not make sense to continue the calculation once the result is mathematically guaranteed to exceed a desired threshold. Providing this value to the `Distance` function allows it to take a shortcut and return a lower bound instead of an exact cost when the threshold is exceeded.

The `Similarity` function calculates the distance, then converts it into a normalized metric within the range 0..1, with 1 meaning the strings are identical, and 0 that they have nothing in common. A minimum similarity threshold can be provided to speed up the calculation of the metric for strings that are far too dissimilar for the purpose at hand. All values under this threshold are rounded down to 0.

The `Match` function provides a similarity metric, with the same range and meaning as `Similarity`, but with a bonus for string pairs that share a common prefix and have a similarity above a "bonus threshold". It uses the same method as proposed by Winkler for the Jaro distance, and the reasoning behind it is that these string pairs are very likely spelling variations or errors, and they are more closely linked than the edit distance alone would suggest.

The underlying `Calculate` function is also exported, to allow the building of other derivative metrics, if needed.

## Installation

```
go get github.com/agext/levenshtein
```

## License

Package levenshtein is released under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.
go-radix [![Build Status](https://travis-ci.org/armon/go-radix.png)](https://travis-ci.org/armon/go-radix)
=========

Provides the `radix` package that implements a [radix tree](http://en.wikipedia.org/wiki/Radix_tree).
The package only provides a single `Tree` implementation, optimized for sparse nodes.

As a radix tree, it provides the following:
 * O(k) operations. In many cases, this can be faster than a hash table since
   the hash function is an O(k) operation, and hash tables have very poor cache locality.
 * Minimum / Maximum value lookups
 * Ordered iteration

For an immutable variant, see [go-immutable-radix](https://github.com/hashicorp/go-immutable-radix).

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/armon/go-radix).

Example
=======

Below is a simple example of usage

```go
// Create a tree
r := radix.New()
r.Insert("foo", 1)
r.Insert("bar", 2)
r.Insert("foobar", 2)

// Find the longest prefix match
m, _, _ := r.LongestPrefix("foozip")
if m != "foo" {
    panic("should be foo")
}
```

# go-testing-interface

go-testing-interface is a Go library that exports an interface that
`*testing.T` implements as well as a runtime version you can use in its
place.

The purpose of this library is so that you can export test helpers as a
public API without depending on the "testing" package, since you can't
create a `*testing.T` struct manually. This lets you, for example, use the
public testing APIs to generate mock data at runtime, rather than just at
test time.

## Usage & Example

For usage and examples see the [Godoc](http://godoc.org/github.com/mitchellh/go-testing-interface).

Given a test helper written using `go-testing-interface` like this:

    import "github.com/mitchellh/go-testing-interface"

    func TestHelper(t testing.T) {
        t.Fatal("I failed")
    }

You can call the test helper in a real test easily:

    import "testing"

    func TestThing(t *testing.T) {
        TestHelper(t)
    }

You can also call the test helper at runtime if needed:

    import "github.com/mitchellh/go-testing-interface"

    func main() {
        TestHelper(&testing.RuntimeT{})
    }

## Why?!

**Why would I call a test helper that takes a *testing.T at runtime?**

You probably shouldn't. The only use case I've seen (and I've had) for this
is to implement a "dev mode" for a service where the test helpers are used
to populate mock data, create a mock DB, perhaps run service dependencies
in-memory, etc.

Outside of a "dev mode", I've never seen a use case for this and I think
there shouldn't be one since the point of the `testing.T` interface is that
you can fail immediately.
# hashstructure [![GoDoc](https://godoc.org/github.com/mitchellh/hashstructure?status.svg)](https://godoc.org/github.com/mitchellh/hashstructure)

hashstructure is a Go library for creating a unique hash value
for arbitrary values in Go.

This can be used to key values in a hash (for use in a map, set, etc.)
that are complex. The most common use case is comparing two values without
sending data across the network, caching values locally (de-dup), and so on.

## Features

  * Hash any arbitrary Go value, including complex types.

  * Tag a struct field to ignore it and not affect the hash value.

  * Tag a slice type struct field to treat it as a set where ordering
    doesn't affect the hash code but the field itself is still taken into
    account to create the hash value.

  * Optionally specify a custom hash function to optimize for speed, collision
    avoidance for your data set, etc.
  
  * Optionally hash the output of `.String()` on structs that implement fmt.Stringer,
    allowing effective hashing of time.Time

## Installation

Standard `go get`:

```
$ go get github.com/mitchellh/hashstructure
```

## Usage & Example

For usage and examples see the [Godoc](http://godoc.org/github.com/mitchellh/hashstructure).

A quick code example is shown below:

```go
type ComplexStruct struct {
    Name     string
    Age      uint
    Metadata map[string]interface{}
}

v := ComplexStruct{
    Name: "mitchellh",
    Age:  64,
    Metadata: map[string]interface{}{
        "car":      true,
        "location": "California",
        "siblings": []string{"Bob", "John"},
    },
}

hash, err := hashstructure.Hash(v, nil)
if err != nil {
    panic(err)
}

fmt.Printf("%d", hash)
// Output:
// 2307517237273902113
```
# copystructure

copystructure is a Go library for deep copying values in Go.

This allows you to copy Go values that may contain reference values
such as maps, slices, or pointers, and copy their data as well instead
of just their references.

## Installation

Standard `go get`:

```
$ go get github.com/mitchellh/copystructure
```

## Usage & Example

For usage and examples see the [Godoc](http://godoc.org/github.com/mitchellh/copystructure).

The `Copy` function has examples associated with it there.
# Go CLI Library [![GoDoc](https://godoc.org/github.com/mitchellh/cli?status.png)](https://godoc.org/github.com/mitchellh/cli)

cli is a library for implementing powerful command-line interfaces in Go.
cli is the library that powers the CLI for
[Packer](https://github.com/mitchellh/packer),
[Serf](https://github.com/hashicorp/serf),
[Consul](https://github.com/hashicorp/consul),
[Vault](https://github.com/hashicorp/vault),
[Terraform](https://github.com/hashicorp/terraform), and
[Nomad](https://github.com/hashicorp/nomad).

## Features

* Easy sub-command based CLIs: `cli foo`, `cli bar`, etc.

* Support for nested subcommands such as `cli foo bar`.

* Optional support for default subcommands so `cli` does something
  other than error.

* Support for shell autocompletion of subcommands, flags, and arguments
  with callbacks in Go. You don't need to write any shell code.

* Automatic help generation for listing subcommands

* Automatic help flag recognition of `-h`, `--help`, etc.

* Automatic version flag recognition of `-v`, `--version`.

* Helpers for interacting with the terminal, such as outputting information,
  asking for input, etc. These are optional, you can always interact with the
  terminal however you choose.

* Use of Go interfaces/types makes augmenting various parts of the library a
  piece of cake.

## Example

Below is a simple example of creating and running a CLI

```go
package main

import (
	"log"
	"os"

	"github.com/mitchellh/cli"
)

func main() {
	c := cli.NewCLI("app", "1.0.0")
	c.Args = os.Args[1:]
	c.Commands = map[string]cli.CommandFactory{
		"foo": fooCommandFactory,
		"bar": barCommandFactory,
	}

	exitStatus, err := c.Run()
	if err != nil {
		log.Println(err)
	}

	os.Exit(exitStatus)
}
```

# go-wordwrap

`go-wordwrap` (Golang package: `wordwrap`) is a package for Go that
automatically wraps words into multiple lines. The primary use case for this
is in formatting CLI output, but of course word wrapping is a generally useful
thing to do.

## Installation and Usage

Install using `go get github.com/mitchellh/go-wordwrap`.

Full documentation is available at
http://godoc.org/github.com/mitchellh/go-wordwrap

Below is an example of its usage ignoring errors:

```go
wrapped := wordwrap.WrapString("foo bar baz", 3)
fmt.Println(wrapped)
```

Would output:

```
foo
bar
baz
```

## Word Wrap Algorithm

This library doesn't use any clever algorithm for word wrapping. The wrapping
is actually very naive: whenever there is whitespace or an explicit linebreak.
The goal of this library is for word wrapping CLI output, so the input is
typically pretty well controlled human language. Because of this, the naive
approach typically works just fine.

In the future, we'd like to make the algorithm more advanced. We would do
so without breaking the API.
# go-homedir

This is a Go library for detecting the user's home directory without
the use of cgo, so the library can be used in cross-compilation environments.

Usage is incredibly simple, just call `homedir.Dir()` to get the home directory
for a user, and `homedir.Expand()` to expand the `~` in a path to the home
directory.

**Why not just use `os/user`?** The built-in `os/user` package requires
cgo on Darwin systems. This means that any Go code that uses that package
cannot cross compile. But 99% of the time the use for `os/user` is just to
retrieve the home directory, which we can do for the current user without
cgo. This library does that, enabling cross-compilation.
# reflectwalk

reflectwalk is a Go library for "walking" a value in Go using reflection,
in the same way a directory tree can be "walked" on the filesystem. Walking
a complex structure can allow you to do manipulations on unknown structures
such as those decoded from JSON.
# mapstructure [![Godoc](https://godoc.org/github.com/mitchellh/mapstructure?status.svg)](https://godoc.org/github.com/mitchellh/mapstructure)

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
# go-jmespath - A JMESPath implementation in Go

[![Build Status](https://img.shields.io/travis/jmespath/go-jmespath.svg)](https://travis-ci.org/jmespath/go-jmespath)



See http://jmespath.org for more info.
INI [![Build Status](https://travis-ci.org/go-ini/ini.svg?branch=master)](https://travis-ci.org/go-ini/ini) [![Sourcegraph](https://img.shields.io/badge/view%20on-Sourcegraph-brightgreen.svg)](https://sourcegraph.com/github.com/go-ini/ini)
===

![](https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

## Features

- Load from multiple data sources(`[]byte`, file and `io.ReadCloser`) with overwrites.
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

```sh
$ go get gopkg.in/ini.v1
```

To use with latest changes:

```sh
$ go get github.com/go-ini/ini
```

Please add `-u` flag to update in the future.

## Getting Help

- [Getting Started](https://ini.unknwon.io/docs/intro/getting_started)
- [API Documentation](https://gowalker.org/gopkg.in/ini.v1)

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.
# run

[![GoDoc](https://godoc.org/github.com/oklog/run?status.svg)](https://godoc.org/github.com/oklog/run) 
[![Build Status](https://travis-ci.org/oklog/run.svg?branch=master)](https://travis-ci.org/oklog/run) 
[![Go Report Card](https://goreportcard.com/badge/github.com/oklog/run)](https://goreportcard.com/report/github.com/oklog/run)
[![Apache 2 licensed](https://img.shields.io/badge/license-Apache2-blue.svg)](https://raw.githubusercontent.com/oklog/run/master/LICENSE)

run.Group is a universal mechanism to manage goroutine lifecycles.

Create a zero-value run.Group, and then add actors to it. Actors are defined as
a pair of functions: an **execute** function, which should run synchronously;
and an **interrupt** function, which, when invoked, should cause the execute
function to return. Finally, invoke Run, which blocks until the first actor
returns. This general-purpose API allows callers to model pretty much any
runnable task, and achieve well-defined lifecycle semantics for the group.

run.Group was written to manage component lifecycles in func main for 
[OK Log](https://github.com/oklog/oklog). 
But it's useful in any circumstance where you need to orchestrate multiple
goroutines as a unit whole.
[Click here](https://www.youtube.com/watch?v=LHe1Cb_Ud_M&t=15m45s) to see a
video of a talk where run.Group is described.

## Examples

### context.Context

```go
ctx, cancel := context.WithCancel(context.Background())
g.Add(func() error {
	return myProcess(ctx, ...)
}, func(error) {
	cancel()
})
```

### net.Listener

```go
ln, _ := net.Listen("tcp", ":8080")
g.Add(func() error {
	return http.Serve(ln, nil)
}, func(error) {
	ln.Close()
})
```

### io.ReadCloser

```go
var conn io.ReadCloser = ...
g.Add(func() error {
	s := bufio.NewScanner(conn)
	for s.Scan() {
		println(s.Text())
	}
	return s.Err()
}, func(error) {
	conn.Close()
})
```

## Comparisons

Package run is somewhat similar to package 
[errgroup](https://godoc.org/golang.org/x/sync/errgroup), 
except it doesn't require actor goroutines to understand context semantics.

It's somewhat similar to package
[tomb.v1](https://godoc.org/gopkg.in/tomb.v1) or 
[tomb.v2](https://godoc.org/gopkg.in/tomb.v2),
except it has a much smaller API surface, delegating e.g. staged shutdown of 
goroutines to the caller.
# cleanhttp

Functions for accessing "clean" Go http.Client values

-------------

The Go standard library contains a default `http.Client` called
`http.DefaultClient`. It is a common idiom in Go code to start with
`http.DefaultClient` and tweak it as necessary, and in fact, this is
encouraged; from the `http` package documentation:

> The Client's Transport typically has internal state (cached TCP connections),
so Clients should be reused instead of created as needed. Clients are safe for
concurrent use by multiple goroutines.

Unfortunately, this is a shared value, and it is not uncommon for libraries to
assume that they are free to modify it at will. With enough dependencies, it
can be very easy to encounter strange problems and race conditions due to
manipulation of this shared value across libraries and goroutines (clients are
safe for concurrent use, but writing values to the client struct itself is not
protected).

Making things worse is the fact that a bare `http.Client` will use a default
`http.Transport` called `http.DefaultTransport`, which is another global value
that behaves the same way. So it is not simply enough to replace
`http.DefaultClient` with `&http.Client{}`.

This repository provides some simple functions to get a "clean" `http.Client`
-- one that uses the same default values as the Go standard library, but
returns a client that does not share any state with other clients.
# go-hclog

[![Go Documentation](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)][godocs]

[godocs]: https://godoc.org/github.com/hashicorp/go-hclog

`go-hclog` is a package for Go that provides a simple key/value logging
interface for use in development and production environments.

It provides logging levels that provide decreased output based upon the
desired amount of output, unlike the standard library `log` package.

It provides `Printf` style logging of values via `hclog.Fmt()`.

It provides a human readable output mode for use in development as well as
JSON output mode for production.

## Stability Note

While this library is fully open source and HashiCorp will be maintaining it
(since we are and will be making extensive use of it), the API and output
format is subject to minor changes as we fully bake and vet it in our projects.
This notice will be removed once it's fully integrated into our major projects
and no further changes are anticipated.

## Installation and Docs

Install using `go get github.com/hashicorp/go-hclog`.

Full documentation is available at
http://godoc.org/github.com/hashicorp/go-hclog

## Usage

### Use the global logger

```go
hclog.Default().Info("hello world")
```

```text
2017-07-05T16:15:55.167-0700 [INFO ] hello world
```

(Note timestamps are removed in future examples for brevity.)

### Create a new logger

```go
appLogger := hclog.New(&hclog.LoggerOptions{
	Name:  "my-app",
	Level: hclog.LevelFromString("DEBUG"),
})
```

### Emit an Info level message with 2 key/value pairs

```go
input := "5.5"
_, err := strconv.ParseInt(input, 10, 32)
if err != nil {
	appLogger.Info("Invalid input for ParseInt", "input", input, "error", err)
}
```

```text
... [INFO ] my-app: Invalid input for ParseInt: input=5.5 error="strconv.ParseInt: parsing "5.5": invalid syntax"
```

### Create a new Logger for a major subsystem

```go
subsystemLogger := appLogger.Named("transport")
subsystemLogger.Info("we are transporting something")
```

```text
... [INFO ] my-app.transport: we are transporting something
```

Notice that logs emitted by `subsystemLogger` contain `my-app.transport`,
reflecting both the application and subsystem names.

### Create a new Logger with fixed key/value pairs

Using `With()` will include a specific key-value pair in all messages emitted
by that logger.

```go
requestID := "5fb446b6-6eba-821d-df1b-cd7501b6a363"
requestLogger := subsystemLogger.With("request", requestID)
requestLogger.Info("we are transporting a request")
```

```text
... [INFO ] my-app.transport: we are transporting a request: request=5fb446b6-6eba-821d-df1b-cd7501b6a363
```

This allows sub Loggers to be context specific without having to thread that
into all the callers.

### Using `hclog.Fmt()`

```go
var int totalBandwidth = 200
appLogger.Info("total bandwidth exceeded", "bandwidth", hclog.Fmt("%d GB/s", totalBandwidth))
```

```text
... [INFO ] my-app: total bandwidth exceeded: bandwidth="200 GB/s"
```

### Use this with code that uses the standard library logger

If you want to use the standard library's `log.Logger` interface you can wrap
`hclog.Logger` by calling the `StandardLogger()` method. This allows you to use
it with the familiar `Println()`, `Printf()`, etc. For example:

```go
stdLogger := appLogger.StandardLogger(&hclog.StandardLoggerOptions{
	InferLevels: true,
})
// Printf() is provided by stdlib log.Logger interface, not hclog.Logger
stdLogger.Printf("[DEBUG] %+v", stdLogger)
```

```text
... [DEBUG] my-app: &{mu:{state:0 sema:0} prefix: flag:0 out:0xc42000a0a0 buf:[]}
```

Notice that if `appLogger` is initialized with the `INFO` log level _and_ you
specify `InferLevels: true`, you will not see any output here. You must change
`appLogger` to `DEBUG` to see output. See the docs for more information.
# Go Plugin System over RPC

`go-plugin` is a Go (golang) plugin system over RPC. It is the plugin system
that has been in use by HashiCorp tooling for over 4 years. While initially
created for [Packer](https://www.packer.io), it is additionally in use by
[Terraform](https://www.terraform.io), [Nomad](https://www.nomadproject.io), and
[Vault](https://www.vaultproject.io).

While the plugin system is over RPC, it is currently only designed to work
over a local [reliable] network. Plugins over a real network are not supported
and will lead to unexpected behavior.

This plugin system has been used on millions of machines across many different
projects and has proven to be battle hardened and ready for production use.

## Features

The HashiCorp plugin system supports a number of features:

**Plugins are Go interface implementations.** This makes writing and consuming
plugins feel very natural. To a plugin author: you just implement an
interface as if it were going to run in the same process. For a plugin user:
you just use and call functions on an interface as if it were in the same
process. This plugin system handles the communication in between.

**Cross-language support.** Plugins can be written (and consumed) by
almost every major language. This library supports serving plugins via
[gRPC](http://www.grpc.io). gRPC-based plugins enable plugins to be written
in any language.

**Complex arguments and return values are supported.** This library
provides APIs for handling complex arguments and return values such
as interfaces, `io.Reader/Writer`, etc. We do this by giving you a library
(`MuxBroker`) for creating new connections between the client/server to
serve additional interfaces or transfer raw data.

**Bidirectional communication.** Because the plugin system supports
complex arguments, the host process can send it interface implementations
and the plugin can call back into the host process.

**Built-in Logging.** Any plugins that use the `log` standard library
will have log data automatically sent to the host process. The host
process will mirror this output prefixed with the path to the plugin
binary. This makes debugging with plugins simple. If the host system
uses [hclog](https://github.com/hashicorp/go-hclog) then the log data
will be structured. If the plugin also uses hclog, logs from the plugin
will be sent to the host hclog and be structured.

**Protocol Versioning.** A very basic "protocol version" is supported that
can be incremented to invalidate any previous plugins. This is useful when
interface signatures are changing, protocol level changes are necessary,
etc. When a protocol version is incompatible, a human friendly error
message is shown to the end user.

**Stdout/Stderr Syncing.** While plugins are subprocesses, they can continue
to use stdout/stderr as usual and the output will get mirrored back to
the host process. The host process can control what `io.Writer` these
streams go to to prevent this from happening.

**TTY Preservation.** Plugin subprocesses are connected to the identical
stdin file descriptor as the host process, allowing software that requires
a TTY to work. For example, a plugin can execute `ssh` and even though there
are multiple subprocesses and RPC happening, it will look and act perfectly
to the end user.

**Host upgrade while a plugin is running.** Plugins can be "reattached"
so that the host process can be upgraded while the plugin is still running.
This requires the host/plugin to know this is possible and daemonize
properly. `NewClient` takes a `ReattachConfig` to determine if and how to
reattach.

**Cryptographically Secure Plugins.** Plugins can be verified with an expected
checksum and RPC communications can be configured to use TLS. The host process
must be properly secured to protect this configuration.

## Architecture

The HashiCorp plugin system works by launching subprocesses and communicating
over RPC (using standard `net/rpc` or [gRPC](http://www.grpc.io)). A single
connection is made between any plugin and the host process. For net/rpc-based
plugins, we use a [connection multiplexing](https://github.com/hashicorp/yamux)
library to multiplex any other connections on top. For gRPC-based plugins,
the HTTP2 protocol handles multiplexing.

This architecture has a number of benefits:

  * Plugins can't crash your host process: A panic in a plugin doesn't
    panic the plugin user.

  * Plugins are very easy to write: just write a Go application and `go build`.
    Or use any other language to write a gRPC server with a tiny amount of
    boilerplate to support go-plugin.

  * Plugins are very easy to install: just put the binary in a location where
    the host will find it (depends on the host but this library also provides
    helpers), and the plugin host handles the rest.

  * Plugins can be relatively secure: The plugin only has access to the
    interfaces and args given to it, not to the entire memory space of the
    process. Additionally, go-plugin can communicate with the plugin over
    TLS.

## Usage

To use the plugin system, you must take the following steps. These are
high-level steps that must be done. Examples are available in the
`examples/` directory.

  1. Choose the interface(s) you want to expose for plugins.

  2. For each interface, implement an implementation of that interface
     that communicates over a `net/rpc` connection or other a
     [gRPC](http://www.grpc.io) connection or both. You'll have to implement
     both a client and server implementation.

  3. Create a `Plugin` implementation that knows how to create the RPC
     client/server for a given plugin type.

  4. Plugin authors call `plugin.Serve` to serve a plugin from the
     `main` function.

  5. Plugin users use `plugin.Client` to launch a subprocess and request
     an interface implementation over RPC.

That's it! In practice, step 2 is the most tedious and time consuming step.
Even so, it isn't very difficult and you can see examples in the `examples/`
directory as well as throughout our various open source projects.

For complete API documentation, see [GoDoc](https://godoc.org/github.com/hashicorp/go-plugin).

## Roadmap

Our plugin system is constantly evolving. As we use the plugin system for
new projects or for new features in existing projects, we constantly find
improvements we can make.

At this point in time, the roadmap for the plugin system is:

**Semantic Versioning.** Plugins will be able to implement a semantic version.
This plugin system will give host processes a system for constraining
versions. This is in addition to the protocol versioning already present
which is more for larger underlying changes.

**Plugin fetching.** We will integrate with [go-getter](https://github.com/hashicorp/go-getter)
to support automatic download + install of plugins. Paired with cryptographically
secure plugins (above), we can make this a safe operation for an amazing
user experience.

## What About Shared Libraries?

When we started using plugins (late 2012, early 2013), plugins over RPC
were the only option since Go didn't support dynamic library loading. Today,
Go still doesn't support dynamic library loading, but they do intend to.
Since 2012, our plugin system has stabilized from millions of users using it,
and has many benefits we've come to value greatly.

For example, we intend to use this plugin system in
[Vault](https://www.vaultproject.io), and dynamic library loading will
simply never be acceptable in Vault for security reasons. That is an extreme
example, but we believe our library system has more upsides than downsides
over dynamic library loading and since we've had it built and tested for years,
we'll likely continue to use it.

Shared libraries have one major advantage over our system which is much
higher performance. In real world scenarios across our various tools,
we've never required any more performance out of our plugin system and it
has seen very high throughput, so this isn't a concern for us at the moment.

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
# go-safetemp
[![Godoc](https://godoc.org/github.com/hashcorp/go-safetemp?status.svg)](https://godoc.org/github.com/hashicorp/go-safetemp)

Functions for safely working with temporary directories and files.

## Why?

The Go standard library provides the excellent `ioutil` package for
working with temporary directories and files. This library builds on top
of that to provide safe abstractions above that.
# Terraform Helper Lib: schema

The `schema` package provides a high-level interface for writing resource
providers for Terraform.

If you're writing a resource provider, we recommend you use this package.

The interface exposed by this package is much friendlier than trying to
write to the Terraform API directly. The core Terraform API is low-level
and built for maximum flexibility and control, whereas this library is built
as a framework around that to more easily write common providers.
# uuid [![Build Status](https://travis-ci.org/hashicorp/go-uuid.svg?branch=master)](https://travis-ci.org/hashicorp/go-uuid)

Generates UUID-format strings using high quality, _purely random_ bytes. It is **not** intended to be RFC compliant, merely to use a well-understood string representation of a 128-bit value. It can also parse UUID-format strings into their component bytes.

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/hashicorp/go-uuid).
# HIL

[![GoDoc](https://godoc.org/github.com/hashicorp/hil?status.png)](https://godoc.org/github.com/hashicorp/hil) [![Build Status](https://travis-ci.org/hashicorp/hil.svg?branch=master)](https://travis-ci.org/hashicorp/hil)

HIL (HashiCorp Interpolation Language) is a lightweight embedded language used
primarily for configuration interpolation. The goal of HIL is to make a simple
language for interpolations in the various configurations of HashiCorp tools.

HIL is built to interpolate any string, but is in use by HashiCorp primarily
with [HCL](https://github.com/hashicorp/hcl). HCL is _not required_ in any
way for use with HIL.

HIL isn't meant to be a general purpose language. It was built for basic
configuration interpolations. Therefore, you can't currently write functions,
have conditionals, set intermediary variables, etc. within HIL itself. It is
possible some of these may be added later but the right use case must exist.

## Why?

Many of our tools have support for something similar to templates, but
within the configuration itself. The most prominent requirement was in
[Terraform](https://github.com/hashicorp/terraform) where we wanted the
configuration to be able to reference values from elsewhere in the
configuration. Example:

    foo = "hi ${var.world}"

We originally used a full templating language for this, but found it
was too heavy weight. Additionally, many full languages required bindings
to C (and thus the usage of cgo) which we try to avoid to make cross-compilation
easier. We then moved to very basic regular expression based
string replacement, but found the need for basic arithmetic and function
calls resulting in overly complex regular expressions.

Ultimately, we wrote our own mini-language within Terraform itself. As
we built other projects such as [Nomad](https://nomadproject.io) and
[Otto](https://ottoproject.io), the need for basic interpolations arose
again.

Thus HIL was born. It is extracted from Terraform, cleaned up, and
better tested for general purpose use.

## Syntax

For a complete grammar, please see the parser itself. A high-level overview
of the syntax and grammer is listed here.

Code begins within `${` and `}`. Outside of this, text is treated
literally. For example, `foo` is a valid HIL program that is just the
string "foo", but `foo ${bar}` is an HIL program that is the string "foo "
concatened with the value of `bar`. For the remainder of the syntax
docs, we'll assume you're within `${}`.

  * Identifiers are any text in the format of `[a-zA-Z0-9-.]`. Example
    identifiers: `foo`, `var.foo`, `foo-bar`.

  * Strings are double quoted and can contain any UTF-8 characters.
    Example: `"Hello, World"`

  * Numbers are assumed to be base 10. If you prefix a number with 0x,
    it is treated as a hexadecimal. If it is prefixed with 0, it is
    treated as an octal. Numbers can be in scientific notation: "1e10".

  * Unary `-` can be used for negative numbers. Example: `-10` or `-0.2`

  * Boolean values: `true`, `false`
  
  * The following arithmetic operations are allowed: +, -, *, /, %. 

  * Function calls are in the form of `name(arg1, arg2, ...)`. Example:
    `add(1, 5)`. Arguments can be any valid HIL expression, example:
    `add(1, var.foo)` or even nested function calls:
    `add(1, get("some value"))`. 

  * Within strings, further interpolations can be opened with `${}`.
    Example: `"Hello ${nested}"`. A full example including the 
    original `${}` (remember this list assumes were inside of one
    already) could be: `foo ${func("hello ${var.foo}")}`. 

## Language Changes

We've used this mini-language in Terraform for years. For backwards compatibility
reasons, we're unlikely to make an incompatible change to the language but
we're not currently making that promise, either.

The internal API of this project may very well change as we evolve it
to work with more of our projects. We recommend using some sort of dependency
management solution with this package.

## Future Changes

The following changes are already planned to be made at some point:

  * Richer types: lists, maps, etc.

  * Convert to a more standard Go parser structure similar to HCL. This
    will improve our error messaging as well as allow us to have automatic
    formatting.

  * Allow interpolations to result in more types than just a string. While
    within the interpolation basic types are honored, the result is always
    a string.
# errwrap

`errwrap` is a package for Go that formalizes the pattern of wrapping errors
and checking if an error contains another error.

There is a common pattern in Go of taking a returned `error` value and
then wrapping it (such as with `fmt.Errorf`) before returning it. The problem
with this pattern is that you completely lose the original `error` structure.

Arguably the _correct_ approach is that you should make a custom structure
implementing the `error` interface, and have the original error as a field
on that structure, such [as this example](http://golang.org/pkg/os/#PathError).
This is a good approach, but you have to know the entire chain of possible
rewrapping that happens, when you might just care about one.

`errwrap` formalizes this pattern (it doesn't matter what approach you use
above) by giving a single interface for wrapping errors, checking if a specific
error is wrapped, and extracting that error.

## Installation and Docs

Install using `go get github.com/hashicorp/errwrap`.

Full documentation is available at
http://godoc.org/github.com/hashicorp/errwrap

## Usage

#### Basic Usage

Below is a very basic example of its usage:

```go
// A function that always returns an error, but wraps it, like a real
// function might.
func tryOpen() error {
	_, err := os.Open("/i/dont/exist")
	if err != nil {
		return errwrap.Wrapf("Doesn't exist: {{err}}", err)
	}

	return nil
}

func main() {
	err := tryOpen()

	// We can use the Contains helpers to check if an error contains
	// another error. It is safe to do this with a nil error, or with
	// an error that doesn't even use the errwrap package.
	if errwrap.Contains(err, "does not exist") {
		// Do something
	}
	if errwrap.ContainsType(err, new(os.PathError)) {
		// Do something
	}

	// Or we can use the associated `Get` functions to just extract
	// a specific error. This would return nil if that specific error doesn't
	// exist.
	perr := errwrap.GetType(err, new(os.PathError))
}
```

#### Custom Types

If you're already making custom types that properly wrap errors, then
you can get all the functionality of `errwraps.Contains` and such by
implementing the `Wrapper` interface with just one function. Example:

```go
type AppError {
  Code ErrorCode
  Err  error
}

func (e *AppError) WrappedErrors() []error {
  return []error{e.Err}
}
```

Now this works:

```go
err := &AppError{Err: fmt.Errorf("an error")}
if errwrap.ContainsType(err, fmt.Errorf("")) {
	// This will work!
}
```
# Yamux

Yamux (Yet another Multiplexer) is a multiplexing library for Golang.
It relies on an underlying connection to provide reliability
and ordering, such as TCP or Unix domain sockets, and provides
stream-oriented multiplexing. It is inspired by SPDY but is not
interoperable with it.

Yamux features include:

* Bi-directional streams
  * Streams can be opened by either client or server
  * Useful for NAT traversal
  * Server-side push support
* Flow control
  * Avoid starvation
  * Back-pressure to prevent overwhelming a receiver
* Keep Alives
  * Enables persistent connections over a load balancer
* Efficient
  * Enables thousands of logical streams with low overhead

## Documentation

For complete documentation, see the associated [Godoc](http://godoc.org/github.com/hashicorp/yamux).

## Specification

The full specification for Yamux is provided in the `spec.md` file.
It can be used as a guide to implementors of interoperable libraries.

## Usage

Using Yamux is remarkably simple:

```go

func client() {
    // Get a TCP connection
    conn, err := net.Dial(...)
    if err != nil {
        panic(err)
    }

    // Setup client side of yamux
    session, err := yamux.Client(conn, nil)
    if err != nil {
        panic(err)
    }

    // Open a new stream
    stream, err := session.Open()
    if err != nil {
        panic(err)
    }

    // Stream implements net.Conn
    stream.Write([]byte("ping"))
}

func server() {
    // Accept a TCP connection
    conn, err := listener.Accept()
    if err != nil {
        panic(err)
    }

    // Setup server side of yamux
    session, err := yamux.Server(conn, nil)
    if err != nil {
        panic(err)
    }

    // Accept a stream
    stream, err := session.Accept()
    if err != nil {
        panic(err)
    }

    // Listen for a message
    buf := make([]byte, 4)
    stream.Read(buf)
}

```

# logutils

logutils is a Go package that augments the standard library "log" package
to make logging a bit more modern, without fragmenting the Go ecosystem
with new logging packages.

## The simplest thing that could possibly work

Presumably your application already uses the default `log` package. To switch, you'll want your code to look like the following:

```go
package main

import (
	"log"
	"os"

	"github.com/hashicorp/logutils"
)

func main() {
	filter := &logutils.LevelFilter{
		Levels: []logutils.LogLevel{"DEBUG", "WARN", "ERROR"},
		MinLevel: logutils.LogLevel("WARN"),
		Writer: os.Stderr,
	}
	log.SetOutput(filter)

	log.Print("[DEBUG] Debugging") // this will not print
	log.Print("[WARN] Warning") // this will
	log.Print("[ERROR] Erring") // and so will this
	log.Print("Message I haven't updated") // and so will this
}
```

This logs to standard error exactly like go's standard logger. Any log messages you haven't converted to have a level will continue to print as before.
# go-getter

[![Build Status](http://img.shields.io/travis/hashicorp/go-getter.svg?style=flat-square)][travis]
[![Build status](https://ci.appveyor.com/api/projects/status/ulq3qr43n62croyq/branch/master?svg=true)][appveyor]
[![Go Documentation](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)][godocs]

[travis]: http://travis-ci.org/hashicorp/go-getter
[godocs]: http://godoc.org/github.com/hashicorp/go-getter
[appveyor]: https://ci.appveyor.com/project/hashicorp/go-getter/branch/master

go-getter is a library for Go (golang) for downloading files or directories
from various sources using a URL as the primary form of input.

The power of this library is being flexible in being able to download
from a number of different sources (file paths, Git, HTTP, Mercurial, etc.)
using a single string as input. This removes the burden of knowing how to
download from a variety of sources from the implementer.

The concept of a _detector_ automatically turns invalid URLs into proper
URLs. For example: "github.com/hashicorp/go-getter" would turn into a
Git URL. Or "./foo" would turn into a file URL. These are extensible.

This library is used by [Terraform](https://terraform.io) for
downloading modules and [Nomad](https://nomadproject.io) for downloading
binaries.

## Installation and Usage

Package documentation can be found on
[GoDoc](http://godoc.org/github.com/hashicorp/go-getter).

Installation can be done with a normal `go get`:

```
$ go get github.com/hashicorp/go-getter
```

go-getter also has a command you can use to test URL strings:

```
$ go install github.com/hashicorp/go-getter/cmd/go-getter
...

$ go-getter github.com/foo/bar ./foo
...
```

The command is useful for verifying URL structures.

## URL Format

go-getter uses a single string URL as input to download from a variety of
protocols. go-getter has various "tricks" with this URL to do certain things.
This section documents the URL format.

### Supported Protocols and Detectors

**Protocols** are used to download files/directories using a specific
mechanism. Example protocols are Git and HTTP.

**Detectors** are used to transform a valid or invalid URL into another
URL if it matches a certain pattern. Example: "github.com/user/repo" is
automatically transformed into a fully valid Git URL. This allows go-getter
to be very user friendly.

go-getter out of the box supports the following protocols. Additional protocols
can be augmented at runtime by implementing the `Getter` interface.

  * Local files
  * Git
  * Mercurial
  * HTTP
  * Amazon S3

In addition to the above protocols, go-getter has what are called "detectors."
These take a URL and attempt to automatically choose the best protocol for
it, which might involve even changing the protocol. The following detection
is built-in by default:

  * File paths such as "./foo" are automatically changed to absolute
    file URLs.
  * GitHub URLs, such as "github.com/mitchellh/vagrant" are automatically
    changed to Git protocol over HTTP.
  * BitBucket URLs, such as "bitbucket.org/mitchellh/vagrant" are automatically
    changed to a Git or mercurial protocol using the BitBucket API.

### Forced Protocol

In some cases, the protocol to use is ambiguous depending on the source
URL. For example, "http://github.com/mitchellh/vagrant.git" could reference
an HTTP URL or a Git URL. Forced protocol syntax is used to disambiguate this
URL.

Forced protocol can be done by prefixing the URL with the protocol followed
by double colons. For example: `git::http://github.com/mitchellh/vagrant.git`
would download the given HTTP URL using the Git protocol.

Forced protocols will also override any detectors.

In the absense of a forced protocol, detectors may be run on the URL, transforming
the protocol anyways. The above example would've used the Git protocol either
way since the Git detector would've detected it was a GitHub URL.

### Protocol-Specific Options

Each protocol can support protocol-specific options to configure that
protocol. For example, the `git` protocol supports specifying a `ref`
query parameter that tells it what ref to checkout for that Git
repository.

The options are specified as query parameters on the URL (or URL-like string)
given to go-getter. Using the Git example above, the URL below is a valid
input to go-getter:

    github.com/hashicorp/go-getter?ref=abcd1234

The protocol-specific options are documented below the URL format
section. But because they are part of the URL, we point it out here so
you know they exist.

### Subdirectories

If you want to download only a specific subdirectory from a downloaded
directory, you can specify a subdirectory after a double-slash `//`.
go-getter will first download the URL specified _before_ the double-slash
(as if you didn't specify a double-slash), but will then copy the
path after the double slash into the target directory.

For example, if you're downloading this GitHub repository, but you only
want to download the `test-fixtures` directory, you can do the following:

```
https://github.com/hashicorp/go-getter.git//test-fixtures
```

If you downloaded this to the `/tmp` directory, then the file
`/tmp/archive.gz` would exist. Notice that this file is in the `test-fixtures`
directory in this repository, but because we specified a subdirectory,
go-getter automatically copied only that directory contents.

Subdirectory paths may contain may also use filesystem glob patterns.
The path must match _exactly one_ entry or go-getter will return an error.
This is useful if you're not sure the exact directory name but it follows
a predictable naming structure.

For example, the following URL would also work:

```
https://github.com/hashicorp/go-getter.git//test-*
```

### Checksumming

For file downloads of any protocol, go-getter can automatically verify
a checksum for you. Note that checksumming only works for downloading files,
not directories, but checksumming will work for any protocol.

To checksum a file, append a `checksum` query parameter to the URL.
The paramter value should be in the format of `type:value`, where
type is "md5", "sha1", "sha256", or "sha512". The "value" should be
the actual checksum value. go-getter will parse out this query parameter
automatically and use it to verify the checksum. An example URL
is shown below:

```
./foo.txt?checksum=md5:b7d96c89d09d9e204f5fedc4d5d55b21
```

The checksum query parameter is never sent to the backend protocol
implementation. It is used at a higher level by go-getter itself.

### Unarchiving

go-getter will automatically unarchive files into a file or directory
based on the extension of the file being requested (over any protocol).
This works for both file and directory downloads.

go-getter looks for an `archive` query parameter to specify the format of
the archive. If this isn't specified, go-getter will use the extension of
the path to see if it appears archived. Unarchiving can be explicitly
disabled by setting the `archive` query parameter to `false`.

The following archive formats are supported:

  * `tar.gz` and `tgz`
  * `tar.bz2` and `tbz2`
  * `tar.xz` and `txz`
  * `zip`
  * `gz`
  * `bz2`
  * `xz`

For example, an example URL is shown below:

```
./foo.zip
```

This will automatically be inferred to be a ZIP file and will be extracted.
You can also be explicit about the archive type:

```
./some/other/path?archive=zip
```

And finally, you can disable archiving completely:

```
./some/path?archive=false
```

You can combine unarchiving with the other features of go-getter such
as checksumming. The special `archive` query parameter will be removed
from the URL before going to the final protocol downloader.

## Protocol-Specific Options

This section documents the protocol-specific options that can be specified
for go-getter. These options should be appended to the input as normal query
parameters. Depending on the usage of go-getter, applications may provide
alternate ways of inputting options. For example, [Nomad](https://www.nomadproject.io)
provides a nice options block for specifying options rather than in the URL.

## General (All Protocols)

The options below are available to all protocols:

  * `archive` - The archive format to use to unarchive this file, or "" (empty
    string) to disable unarchiving. For more details, see the complete section
    on archive support above.

  * `checksum` - Checksum to verify the downloaded file or archive. See
    the entire section on checksumming above for format and more details.

  * `filename` - When in file download mode, allows specifying the name of the
    downloaded file on disk. Has no effect in directory mode.

### Local Files (`file`)

None

### Git (`git`)

  * `ref` - The Git ref to checkout. This is a ref, so it can point to
    a commit SHA, a branch name, etc. If it is a named ref such as a branch
    name, go-getter will update it to the latest on each get.

  * `sshkey` - An SSH private key to use during clones. The provided key must
    be a base64-encoded string. For example, to generate a suitable `sshkey`
    from a private key file on disk, you would run `base64 -w0 <file>`.

    **Note**: Git 2.3+ is required to use this feature.

### Mercurial (`hg`)

  * `rev` - The Mercurial revision to checkout.

### HTTP (`http`)

#### Basic Authentication

To use HTTP basic authentication with go-getter, simply prepend `username:password@` to the
hostname in the URL such as `https://Aladdin:OpenSesame@www.example.com/index.html`. All special
characters, including the username and password, must be URL encoded.

### S3 (`s3`)

S3 takes various access configurations in the URL. Note that it will also
read these from standard AWS environment variables if they're set. S3 compliant servers like Minio
are also supported. If the query parameters are present, these take priority.

  * `aws_access_key_id` - AWS access key.
  * `aws_access_key_secret` - AWS access key secret.
  * `aws_access_token` - AWS access token if this is being used.

#### Using IAM Instance Profiles with S3

If you use go-getter and want to use an EC2 IAM Instance Profile to avoid
using credentials, then just omit these and the profile, if available will
be used automatically.

### Using S3 with Minio
 If you use go-gitter for Minio support, you must consider the following:

  * `aws_access_key_id` (required) - Minio access key.
  * `aws_access_key_secret` (required) - Minio access key secret.
  * `region` (optional - defaults to us-east-1) - Region identifier to use.
  * `version` (optional - defaults to Minio default) - Configuration file format.

#### S3 Bucket Examples

S3 has several addressing schemes used to reference your bucket. These are
listed here: http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro

Some examples for these addressing schemes:
- s3::https://s3.amazonaws.com/bucket/foo
- s3::https://s3-eu-west-1.amazonaws.com/bucket/foo
- bucket.s3.amazonaws.com/foo
- bucket.s3-eu-west-1.amazonaws.com/foo/bar
- "s3::http://127.0.0.1:9000/test-bucket/hello.txt?aws_access_key_id=KEYID&aws_access_key_secret=SECRETKEY&region=us-east-2"

# Versioning Library for Go
[![Build Status](https://travis-ci.org/hashicorp/go-version.svg?branch=master)](https://travis-ci.org/hashicorp/go-version)

go-version is a library for parsing versions and version constraints,
and verifying versions against a set of constraints. go-version
can sort a collection of versions properly, handles prerelease/beta
versions, can increment versions, etc.

Versions used with go-version must follow [SemVer](http://semver.org/).

## Installation and Usage

Package documentation can be found on
[GoDoc](http://godoc.org/github.com/hashicorp/go-version).

Installation can be done with a normal `go get`:

```
$ go get github.com/hashicorp/go-version
```

#### Version Parsing and Comparison

```go
v1, err := version.NewVersion("1.2")
v2, err := version.NewVersion("1.5+metadata")

// Comparison example. There is also GreaterThan, Equal, and just
// a simple Compare that returns an int allowing easy >=, <=, etc.
if v1.LessThan(v2) {
    fmt.Printf("%s is less than %s", v1, v2)
}
```

#### Version Constraints

```go
v1, err := version.NewVersion("1.2")

// Constraints example.
constraints, err := version.NewConstraint(">= 1.0, < 1.4")
if constraints.Check(v1) {
	fmt.Printf("%s satisfies constraints %s", v1, constraints)
}
```

#### Version Sorting

```go
versionsRaw := []string{"1.1", "0.7.1", "1.4-beta", "1.4", "2"}
versions := make([]*version.Version, len(versionsRaw))
for i, raw := range versionsRaw {
    v, _ := version.NewVersion(raw)
    versions[i] = v
}

// After this, the versions are properly sorted
sort.Sort(version.Collection(versions))
```

## Issues and Contributing

If you find an issue with this library, please report an issue. If you'd
like, we welcome any contributions. Fork this library and submit a pull
request.
# go-multierror

[![Build Status](http://img.shields.io/travis/hashicorp/go-multierror.svg?style=flat-square)][travis]
[![Go Documentation](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)][godocs]

[travis]: https://travis-ci.org/hashicorp/go-multierror
[godocs]: https://godoc.org/github.com/hashicorp/go-multierror

`go-multierror` is a package for Go that provides a mechanism for
representing a list of `error` values as a single `error`.

This allows a function in Go to return an `error` that might actually
be a list of errors. If the caller knows this, they can unwrap the
list and access the errors. If the caller doesn't know, the error
formats to a nice human-readable format.

`go-multierror` implements the
[errwrap](https://github.com/hashicorp/errwrap) interface so that it can
be used with that library, as well.

## Installation and Docs

Install using `go get github.com/hashicorp/go-multierror`.

Full documentation is available at
http://godoc.org/github.com/hashicorp/go-multierror

## Usage

go-multierror is easy to use and purposely built to be unobtrusive in
existing Go applications/libraries that may not be aware of it.

**Building a list of errors**

The `Append` function is used to create a list of errors. This function
behaves a lot like the Go built-in `append` function: it doesn't matter
if the first argument is nil, a `multierror.Error`, or any other `error`,
the function behaves as you would expect.

```go
var result error

if err := step1(); err != nil {
	result = multierror.Append(result, err)
}
if err := step2(); err != nil {
	result = multierror.Append(result, err)
}

return result
```

**Customizing the formatting of the errors**

By specifying a custom `ErrorFormat`, you can customize the format
of the `Error() string` function:

```go
var result *multierror.Error

// ... accumulate errors here, maybe using Append

if result != nil {
	result.ErrorFormat = func([]error) string {
		return "errors!"
	}
}
```

**Accessing the list of errors**

`multierror.Error` implements `error` so if the caller doesn't know about
multierror, it will work just fine. But if you're aware a multierror might
be returned, you can use type switches to access the list of errors:

```go
if err := something(); err != nil {
	if merr, ok := err.(*multierror.Error); ok {
		// Use merr.Errors
	}
}
```

**Returning a multierror only if there are errors**

If you build a `multierror.Error`, you can use the `ErrorOrNil` function
to return an `error` implementation only if there are errors to return:

```go
var result *multierror.Error

// ... accumulate errors here

// Return the `error` only if errors were added to the multierror, otherwise
// return nil since there are no errors.
return result.ErrorOrNil()
```
# Color [![GoDoc](https://godoc.org/github.com/fatih/color?status.svg)](https://godoc.org/github.com/fatih/color) [![Build Status](https://img.shields.io/travis/fatih/color.svg?style=flat-square)](https://travis-ci.org/fatih/color)



Color lets you use colorized outputs in terms of [ANSI Escape
Codes](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors) in Go (Golang). It
has support for Windows too! The API can be used in several ways, pick one that
suits you.


![Color](https://i.imgur.com/c1JI0lA.png)


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

### Disable/Enable color
 
There might be a case where you want to explicitly disable/enable color output. the 
`go-isatty` package will automatically disable color output for non-tty output streams 
(for example if the output were piped directly to `less`)

`Color` has support to disable/enable colors both globally and for single color 
definitions. For example suppose you have a CLI app and a `--no-color` bool flag. You 
can easily disable the color output with:

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
# Cloud IP Example

This Cloud IP example launches a web server, installs nginx. It also creates security group 

## Running the example

run `terraform apply` 

Give couple of mins for userdata to install nginx, and then type the DNS name from outputs in your browser and see the nginx welcome page
#  Web layer Example

Full web layer example including load balancer and cloud sql server

## Running the example

run `terraform apply` 

