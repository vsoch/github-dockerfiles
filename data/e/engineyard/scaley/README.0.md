# Go Text

This repository holds supplementary Go libraries for text processing, many involving Unicode.

## Semantic Versioning
This repo uses Semantic versioning (http://semver.org/), so
1. MAJOR version when you make incompatible API changes,
1. MINOR version when you add functionality in a backwards-compatible manner,
   and
1. PATCH version when you make backwards-compatible bug fixes.

Until version 1.0.0 of x/text is reached, the minor version is considered a
major version. So going from 0.1.0 to 0.2.0 is considered to be a major version
bump.

A major new CLDR version is mapped to a minor version increase in x/text.
Any other new CLDR version is mapped to a patch version increase in x/text.

It is important that the Unicode version used in `x/text` matches the one used
by your Go compiler. The `x/text` repository supports multiple versions of
Unicode and will match the version of Unicode to that of the Go compiler. At the
moment this is supported for Go compilers from version 1.7.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/text`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/text`.

## Contribute
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

TODO:
- updating unversioned source files.

## Generating Tables

To generate the tables in this repository (except for the encoding
tables), run `go generate` from this directory. By default tables are
generated for the Unicode version in core and the CLDR version defined in
golang.org/x/text/unicode/cldr.

Running go generate will as a side effect create a DATA subdirectory in this
directory which holds all files that are used as a source for generating the
tables. This directory will also serve as a cache.

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

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the image repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/image:" in the
subject line, so it is easy to find.
The export directory contains packages that are generated using the x/text
infrastructure, but live elsewhere.
At some point we can expose some of the infrastructure, but for now this
is not done.
# sys

This repository holds supplemental Go packages for low-level interactions with
the operating system.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/sys`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/sys`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the sys repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/sys:" in the
subject line, so it is easy to find.
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

// Note: struct fields must be public in order for unmarshal to
// correctly populate the data.
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

The jamaica pacakge provides some handy step definitions and functions for in-process testing of CLI applications via the [godog](https://github.com/DATA-DOG/godog) Cucumber port.

In short, this is an attempt to implement a very minimal [aruba](https://github.com/cucumber/aruba) for Go.

## Installation ##

It would be best to use [dep](https://github.com/golang/dep) to include jamaica in your dependency tree, but there is absolutely no reason that you shouldn't be
able to simply do the standard `go get`:

```
go get github.com/ess/jamaica
```

## Configuration ##

The same steps are necessary regardless of the way that your `godog` suite is set up:

1. Use `jamaica.SetRootCmd()` to declare the command that you want to test. The object passed must adhere to the [`jamaica.Command`]() interface.
2. Use `jamaica.StepUp()` to inject the jamaica step definitions into your `godog` suite.

### Basic Godog Configuration ###

If you're not using `TestMain` to execute your `godog` suite, you would set up jamaica within the `FeatureContext` in one of your test files:

```go
package something

import (
  "github.com/DATA-DOG/godog"
  "github.com/ess/jamaica"
)

func FeatureContext(s *godog.Suite) {
  jamaica.SetRootCmd(myCommand)
  jamaica.StepUp(s)
  
  // Register the rest of your steps
}
```

### TestMain Configuration ###

If you're using `TestMain` to execute your `godog` suite, you would set up jamaica like so:

```go
package main

import (
  "os"
  "testing"

  "github.com/DATA-DOG/godog"
  "github.com/ess/jamaica"
)

func TestMain(m *testing.M) {
  jamaica.SetRootCmd(cmd.RootCmd)

  status := godog.RunWithOptions(
    "godog",

    func(s *godog.Suite) {
      jamaica.StepUp(s)
      
      // Register the rest of your steps
    },

    godog.Options{
      Format: "pretty",
      Paths: []string{"features"},
    },
  )

  if st := m.Run(); st > status {
    status = st
  }

  os.Exit(status)
}
```

## Provided Steps ##

A fairly minimal set of steps are provided by jamaica, because it's not exactly aruba.

### Running the Command ###

After you've set up all of your givens and such, you can use the following
step to run the command under test in-process:

```gherkin
When I run `mycommand and its arguments`
```

### Checking the Output ###

To assert that the command output contains a given string, use the following step:

```gherkin
Then stdout contains "a given string"
```

To assert that the command output exactly matches a given string, use the following step:

```gherkin
Then stdout is "a given string"
```

If these steps don't suit your needs (or if you'd prefer to use your own terminology), you can access the command's stdout via `jamaica.LastCommandStdout()` for your comparisons.

### Checking the Exit Status ###

To assert the expectation that the application ran successfully (without error), use the following step:

```gherkin
Then it exits successfully
```

On the other hand, to assert that you expect for the command to have failed, use this:

```gherkin
Then it exits with an error
```

## Usage ##

Simply run your test suite via either `godog` or by using godog with the "test main" pattern.

## History ##

* v1.0.2 - Added missing steps
* v1.0.1 - Fixing some typos
* v1.0.0 - First stable release
* v0.0.8 - No hard deps
* v0.0.7 - Minor tweaks
* v0.0.6 - And now you can get the command output
* v0.0.5 - Now maybe even working
* v0.0.4 - Root the command
* v0.0.3 - Always be returning
* v0.0.2 - Or maybe I can cargo cult my own code properly
* v0.0.1 - Initial attempt
## History ##

* v0.0.3 - Quick correction
* v0.0.2 - No hard deps
* v0.0.1 - Initial attempt
Mockable is a quick and dirty package that lets you know if your user wants
you to use mocked interfaces and such.

## WHY?!?!?!?! ##

Well, because I write a lot of API clients and such, and then I end up using
them in my apps. When I run tests against those apps, I find it easiest if
the library itself provides a transparent mocked interface.

I prefer to decide if mocking is desired by checking an environment variable,
because I write a lot of my app-level tests in languages other than Go. As
I do this sort of thing quite a lot, occasionallly needing to enable mocking
for several clients at once, it finally made sense to just go ahead and
formalize the process and use a uniform environment variable, MOCKABLE,
for everything.

## Installation ##

I suggest the use of [glide](https://glide.sh/) for managing your Go deps, but
you should be able to install it directly without much issue:

```
go get github.com/ess/mockable
```

As mentioned, though, a better idea is to use glide (or another package manager
that supports SemVer).

## Usage ##

Here's a quasi-real-world example. Let's say your library generates widgets.
Now, in production, you really want to make good, real, quality widgets. Under
test, though, the app that uses your widget generator may just need to ensure
that a widget gets generated. Here's how I like to handle that:

```go
package widget

import "github.com/ess/mockable"

type Widget struct {
  Name string
}

type Generator interface {
  Generate(name string) *Widget
}

type realGenerator struct {}

func (generator *realGenerator) Generate(name string) *Widget {
  // do a bunch of stuff that hits the real widget service out there in space
  // ...
  return generatedWidget
}

type fakeGenerator struct {}

func (generator *fakeGenerator) Generate(name string) *Widget {
  return &Widget{Name: name}
}

func NewGenerator() Generator {
  if mockable.Mocked() {
    return &fakeGenerator{}
  }

  return &realGenerator{}
}
```

Now, when the above is used and `widget.NewGenerator()` is called, a fake
generator is returned if mocking is enabled (by setting the `MOCKABLE`
environment variable to pretty much anything), but a real generator otherwise.

## Test Helpers ##

In addition to the main functionality, there are a few helpers available for
writing your unit tests.

In the main `mockable` package, there is `Enable()` and `Disable()`, which are
used to explicitly set the mocking state.

Additionally, in `mockable/mocking`,we have `EnabledDo` and `DisabledDo`. Both
of these functions take a `*testing.T` and a `func(*testing.T)` and are used 
like so:

```go
package main

import (
  "testing"

  "github.com/ess/mockable/mocking"
)

func TestExpecationsMet(t *testing.T) {
  mocking.EnabledDo(t, func(t *testing.T) {
    if !ExpectationsMet() {
      t.Error("Expectations not met when mocking is enabled!!!")
    }
  })
}
```
## History ##

* v0.2.0 - Now with test helpers
* v0.1.3 - I like y'all, so I've removed the vendor from this repo
* v0.1.2 - Added Enable()/Disable() for use in consumer unit tests
* v0.1.1 - Documentation added
* v0.1.0 - Initial release
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
[![](https://img.shields.io/github/tag/magiconair/properties.svg?style=flat-square&label=release)](https://github.com/magiconair/properties/releases)
[![Build Status](https://img.shields.io/travis/magiconair/properties.svg?branch=master&style=flat-square)](https://travis-ci.org/magiconair/properties)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg?style=flat-square)](https://raw.githubusercontent.com/magiconair/properties/master/LICENSE)
[![GoDoc](http://img.shields.io/badge/godoc-reference-5272B4.svg?style=flat-square)](http://godoc.org/github.com/magiconair/properties)

# Overview

#### Please run `git pull --tags` to update the tags. See [below](#updated-git-tags) why.

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

Read the full documentation on [GoDoc](https://godoc.org/github.com/magiconair/properties)   [![GoDoc](https://godoc.org/github.com/magiconair/properties?status.png)](https://godoc.org/github.com/magiconair/properties)

## Getting Started

```go
import (
	"flag"
	"github.com/magiconair/properties"
)

func main() {
	// init from a file
	p := properties.MustLoadFile("${HOME}/config.properties", properties.UTF8)

	// or multiple files
	p = properties.MustLoadFiles([]string{
			"${HOME}/config.properties",
			"${HOME}/config-${USER}.properties",
		}, properties.UTF8, true)

	// or from a map
	p = properties.LoadMap(map[string]string{"key": "value", "abc": "def"})

	// or from a string
	p = properties.MustLoadString("key=value\nabc=def")

	// or from a URL
	p = properties.MustLoadURL("http://host/path")

	// or from multiple URLs
	p = properties.MustLoadURL([]string{
			"http://host/config",
			"http://host/config-${USER}",
		}, true)

	// or from flags
	p.MustFlag(flag.CommandLine)

	// get values through getters
	host := p.MustGetString("host")
	port := p.GetInt("port", 8080)

	// or through Decode
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
}

```

## Installation and Upgrade

```
$ go get -u github.com/magiconair/properties
```

## License

2 clause BSD license. See [LICENSE](https://github.com/magiconair/properties/blob/master/LICENSE) file for details.

## ToDo

* Dump contents with passwords and secrets obscured

## Updated Git tags

#### 13 Feb 2018

I realized that all of the git tags I had pushed before v1.7.5 were lightweight tags
and I've only recently learned that this doesn't play well with `git describe` 😞

I have replaced all lightweight tags with signed tags using this script which should
retain the commit date, name and email address. Please run `git pull --tags` to update them.

Worst case you have to reclone the repo.

```shell
#!/bin/bash
tag=$1
echo "Updating $tag"
date=$(git show ${tag}^0 --format=%aD | head -1)
email=$(git show ${tag}^0 --format=%aE | head -1)
name=$(git show ${tag}^0 --format=%aN | head -1)
GIT_COMMITTER_DATE="$date" GIT_COMMITTER_NAME="$name" GIT_COMMITTER_EMAIL="$email" git tag -s -f ${tag} ${tag}^0 -m ${tag}
```

I apologize for the inconvenience.

Frank

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
# File system notifications for Go

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

Please see [the documentation](https://godoc.org/github.com/fsnotify/fsnotify) and consult the [FAQ](#faq) for usage information.

## API stability

fsnotify is a fork of [howeyc/fsnotify](https://godoc.org/github.com/howeyc/fsnotify) with a new API as of v1.0. The API is based on [this design document](http://goo.gl/MrYxyA). 

All [releases](https://github.com/fsnotify/fsnotify/releases) are tagged based on [Semantic Versioning](http://semver.org/). Further API changes are [planned](https://github.com/fsnotify/fsnotify/milestones), and will be tagged with a new major revision number.

Go 1.6 supports dependencies located in the `vendor/` folder. Unless you are creating a library, it is recommended that you copy fsnotify into `vendor/github.com/fsnotify/fsnotify` within your project, and likewise for `golang.org/x/sys`.

## Contributing

Please refer to [CONTRIBUTING][] before opening an issue or pull request.

## Example

See [example_test.go](https://github.com/fsnotify/fsnotify/blob/master/example_test.go).

## FAQ

**When a file is moved to another directory is it still being watched?**

No (it shouldn't be, unless you are watching where it was moved to).

**When I watch a directory, are all subdirectories watched as well?**

No, you must add watches for any directory you want to watch (a recursive watcher is on the roadmap [#18][]).

**Do I have to watch the Error and Event channels in a separate goroutine?**

As of now, yes. Looking into making this single-thread friendly (see [howeyc #7][#7])

**Why am I receiving multiple events for the same file on OS X?**

Spotlight indexing on OS X can result in multiple events (see [howeyc #62][#62]). A temporary workaround is to add your folder(s) to the *Spotlight Privacy settings* until we have a native FSEvents implementation (see [#11][]).

**How many files can be watched at once?**

There are OS-specific limits as to how many watches can be created:
* Linux: /proc/sys/fs/inotify/max_user_watches contains the limit, reaching this limit results in a "no space left on device" error.
* BSD / OSX: sysctl variables "kern.maxfiles" and "kern.maxfilesperproc", reaching these limits results in a "too many open files" error.

[#62]: https://github.com/howeyc/fsnotify/issues/62
[#18]: https://github.com/fsnotify/fsnotify/issues/18
[#11]: https://github.com/fsnotify/fsnotify/issues/11
[#7]: https://github.com/howeyc/fsnotify/issues/7

[contributing]: https://github.com/fsnotify/fsnotify/blob/master/CONTRIBUTING.md

## Related Projects

* [notify](https://github.com/rjeczalik/notify)
* [fsevents](https://github.com/fsnotify/fsevents)

[![Build Status](https://travis-ci.org/DATA-DOG/godog.svg?branch=master)](https://travis-ci.org/DATA-DOG/godog)
[![GoDoc](https://godoc.org/github.com/DATA-DOG/godog?status.svg)](https://godoc.org/github.com/DATA-DOG/godog)
[![codecov.io](https://codecov.io/github/DATA-DOG/godog/branch/master/graph/badge.svg)](https://codecov.io/github/DATA-DOG/godog)

# Godog

<p align="center"><img src="/logo.png" alt="Godog logo" style="width:250px;" /></p>

**The API is likely to change a few times before we reach 1.0.0**

Please read all the README, you may find it very useful. And do not forget
to peek into the
[CHANGELOG](https://github.com/DATA-DOG/godog/blob/master/CHANGELOG.md)
from time to time.

Package godog is the official Cucumber BDD framework for Golang, it merges
specification and test documentation into one cohesive whole. The author
is a core member of [cucumber team](https://github.com/cucumber).

The project is inspired by [behat][behat] and [cucumber][cucumber] and is
based on cucumber [gherkin3 parser][gherkin].

**Godog** does not intervene with the standard **go test** command
behavior. You can leverage both frameworks to functionally test your
application while maintaining all test related source code in **_test.go**
files.

**Godog** acts similar compared to **go test** command, by using go
compiler and linker tool in order to produce test executable. Godog
contexts need to be exported the same way as **Test** functions for go
tests. Note, that if you use **godog** command tool, it will use `go`
executable to determine compiler and linker.

**Godog** ships gherkin parser dependency as a subpackage. This will
ensure that it is always compatible with the installed version of godog.
So in general there are no vendor dependencies needed for installation.

The following about section was taken from
[cucumber](https://cucumber.io/) homepage.

## About

#### A single source of truth

Cucumber merges specification and test documentation into one cohesive whole.

#### Living documentation

Because they're automatically tested by Cucumber, your specifications are
always bang up-to-date.

#### Focus on the customer

Business and IT don't always understand each other. Cucumber's executable
specifications encourage closer collaboration, helping teams keep the
business goal in mind at all times.

#### Less rework

When automated testing is this much fun, teams can easily protect
themselves from costly regressions.

## Install

    go get github.com/DATA-DOG/godog/cmd/godog

## Example

The following example can be [found
here](/examples/godogs).

### Step 1

Given we create a new go package **$GOPATH/src/godogs**. From now on, this
is our work directory `cd $GOPATH/src/godogs`.

Imagine we have a **godog cart** to serve godogs for lunch. First of all,
we describe our feature in plain text - `vim
$GOPATH/src/godogs/features/godogs.feature`:

``` gherkin
# file: $GOPATH/src/godogs/features/godogs.feature
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining
```

**NOTE:** same as **go test** godog respects package level isolation. All
your step definitions should be in your tested package root directory. In
this case - `$GOPATH/src/godogs`

### Step 2

If godog is installed in your GOPATH. We can run `godog` inside the
**$GOPATH/src/godogs** directory. You should see that the steps are
undefined:

![Undefined step snippets](/screenshots/undefined.png?raw=true)

If we wish to vendor godog dependency, we can do it as usual, using tools
you prefer:

    git clone https://github.com/DATA-DOG/godog.git $GOPATH/src/godogs/vendor/github.com/DATA-DOG/godog

It gives you undefined step snippets to implement in your test context.
You may copy these snippets into your `godogs_test.go` file.

Our directory structure should now look like:

![Directory layout](/screenshots/dir-tree.png?raw=true)

If you copy the snippets into our test file and run godog again. We should
see the step definition is now pending:

![Pending step definition](/screenshots/pending.png?raw=true)

You may change **ErrPending** to **nil** and the scenario will
pass successfully.

Since we need a working implementation, we may start by implementing only what is necessary.

### Step 3

We only need a number of **godogs** for now. Lets keep it simple.

``` go
/* file: $GOPATH/src/godogs/godogs.go */
package main

// Godogs available to eat
var Godogs int

func main() { /* usual main func */ }
```

### Step 4

Now lets implement our step definitions, which we can copy from generated
console output snippets in order to test our feature requirements:

``` go
/* file: $GOPATH/src/godogs/godogs_test.go */
package main

import (
	"fmt"

	"github.com/DATA-DOG/godog"
)

func thereAreGodogs(available int) error {
	Godogs = available
	return nil
}

func iEat(num int) error {
	if Godogs < num {
		return fmt.Errorf("you cannot eat %d godogs, there are %d available", num, Godogs)
	}
	Godogs -= num
	return nil
}

func thereShouldBeRemaining(remaining int) error {
	if Godogs != remaining {
		return fmt.Errorf("expected %d godogs to be remaining, but there is %d", remaining, Godogs)
	}
	return nil
}

func FeatureContext(s *godog.Suite) {
	s.Step(`^there are (\d+) godogs$`, thereAreGodogs)
	s.Step(`^I eat (\d+)$`, iEat)
	s.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)

	s.BeforeScenario(func(interface{}) {
		Godogs = 0 // clean the state before every scenario
	})
}
```

Now when you run the `godog` again, you should see:

![Passed suite](/screenshots/passed.png?raw=true)

We have hooked to **BeforeScenario** event in order to reset application
state before each scenario. You may hook into more events, like
**AfterStep** to print all state in case of an error. Or
**BeforeSuite** to prepare a database.

By now, you should have figured out, how to use **godog**. Another advice
is to make steps orthogonal, small and simple to read for an user. Whether
the user is a dumb website user or an API developer, who may understand
a little more technical context - it should target that user.

When steps are orthogonal and small, you can combine them just like you do
with Unix tools. Look how to simplify or remove ones, which can be
composed.

### References and Tutorials

- [cucumber-html-reporter](https://github.com/gkushang/cucumber-html-reporter)
  may be used in order to generate **html** reports together with
  **cucumber** output formatter. See the [following docker
  image](https://github.com/myie/cucumber-html-reporter) for usage
  details.
- [how to use godog by semaphoreci](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go)
- see [examples](https://github.com/DATA-DOG/godog/tree/master/examples)
- see extension [AssistDog](https://github.com/hellomd/assistdog), which
  may have useful **gherkin.DataTable** transformations or comparison
  methods for assertions.

### Documentation

See [godoc][godoc] for general API details.
See **.travis.yml** for supported **go** versions.
See `godog -h` for general command options.

See implementation examples:

- [rest API server](/examples/api)
- [rest API with Database](/examples/db)
- [godogs](/examples/godogs)

## FAQ

### Running Godog with go test

You may integrate running **godog** in your **go test** command. You can
run it using go [TestMain](https://golang.org/pkg/testing/#hdr-Main) func
available since **go 1.4**. In this case it is not necessary to have
**godog** command installed. See the following example:

``` go
func TestMain(m *testing.M) {
	status := godog.RunWithOptions("godog", func(s *godog.Suite) {
		FeatureContext(s)
	}, godog.Options{
		Format:    "progress",
		Paths:     []string{"features"},
		Randomize: time.Now().UTC().UnixNano(), // randomize scenario execution order
	})

	if st := m.Run(); st > status {
		status = st
	}
	os.Exit(status)
}
```

You can even go one step further and reuse **go test** flags, like
**verbose** mode in order to switch godog **format**. See the following
example:

``` go
func TestMain(m *testing.M) {
	format := "progress"
	for _, arg := range os.Args[1:] {
		if arg == "-test.v=true" { // go test transforms -v option
			format = "pretty"
			break
		}
	}
	status := godog.RunWithOptions("godog", func(s *godog.Suite) {
		godog.SuiteContext(s)
	}, godog.Options{
		Format: format,
		Paths:     []string{"features"},
	})

	if st := m.Run(); st > status {
		status = st
	}
	os.Exit(status)
}
```

Now when running `go test -v` it will use **pretty** format.

### Configure common options for godog CLI

There are no global options or configuration files. Alias your common or
project based commands: `alias godog-wip="godog --format=progress
--tags=@wip"`

### Testing browser interactions

**godog** does not come with builtin packages to connect to the browser.
You may want to look at [selenium](http://www.seleniumhq.org/) and
probably [phantomjs](http://phantomjs.org/). See also the following
components:

1. [browsersteps](https://github.com/llonchj/browsersteps) - provides
   basic context steps to start selenium and navigate browser content.
2. You may wish to have [goquery](https://github.com/PuerkitoBio/goquery)
   in order to work with HTML responses like with JQuery.

### Concurrency

In order to support concurrency well, you should reset the state and
isolate each scenario. They should not share any state. It is suggested to
run the suite concurrently in order to make sure there is no state
corruption or race conditions in the application.

It is also useful to randomize the order of scenario execution, which you
can now do with **--random** command option.

**NOTE:** if suite runs with concurrency option, it concurrently runs
every feature, not scenario per different features. This gives
a flexibility to isolate state per feature. For example using
**BeforeFeature** hook, it is possible to spin up costly service and shut
it down only in **AfterFeature** hook and share the service between all
scenarios in that feature. It is not advisable though, because you are
risking having a state dependency.

## Contributions

Feel free to open a pull request. Note, if you wish to contribute an extension to public (exported methods or types) -
please open an issue before to discuss whether these changes can be accepted. All backward incompatible changes are
and will be treated cautiously.

## License

**Godog** is licensed under the [three clause BSD license][license]

**Gherkin** is licensed under the [MIT][gherkin-license] and developed as
a part of the [cucumber project][cucumber]

[godoc]: http://godoc.org/github.com/DATA-DOG/godog "Documentation on godoc"
[golang]: https://golang.org/  "GO programming language"
[behat]: http://docs.behat.org/ "Behavior driven development framework for PHP"
[cucumber]: https://cucumber.io/ "Behavior driven development framework"
[gherkin]: https://github.com/cucumber/gherkin-go "Gherkin3 parser for GO"
[gherkin-license]: https://en.wikipedia.org/wiki/MIT_License "The MIT license"
[license]: http://en.wikipedia.org/wiki/BSD_licenses "The three clause BSD license"
# An example of API feature

The following example demonstrates steps how we describe and test our API using **godog**.

### Step 1

Describe our feature. Imagine we need a REST API with **json** format. Lets from the point, that
we need to have a **/version** endpoint, which responds with a version number. We also need to manage
error responses.

``` gherkin
# file: version.feature
Feature: get version
  In order to know godog version
  As an API user
  I need to be able to request version

  Scenario: does not allow POST method
    When I send "POST" request to "/version"
    Then the response code should be 405
    And the response should match json:
      """
      {
        "error": "Method not allowed"
      }
      """

  Scenario: should get version number
    When I send "GET" request to "/version"
    Then the response code should be 200
    And the response should match json:
      """
      {
        "version": "v0.5.3"
      }
      """
```

Save it as **version.feature**.
Now we have described a success case and an error when the request method is not allowed.

### Step 2

Run **godog version.feature**. You should see the following result, which says that all of our
steps are yet undefined and provide us with the snippets to implement them.

![Screenshot](https://raw.github.com/DATA-DOG/godog/master/examples/api/screenshots/undefined.png)

### Step 3

Lets copy the snippets to **api_test.go** and modify it for our use case. Since we know that we will
need to store state within steps (a response), we should introduce a structure with some variables.

``` go
// file: api_test.go
package main

import (
	"github.com/DATA-DOG/godog"
	"github.com/DATA-DOG/godog/gherkin"
)

type apiFeature struct {
}

func (a *apiFeature) iSendrequestTo(method, endpoint string) error {
	return godog.ErrPending
}

func (a *apiFeature) theResponseCodeShouldBe(code int) error {
	return godog.ErrPending
}

func (a *apiFeature) theResponseShouldMatchJSON(body *gherkin.DocString) error {
	return godog.ErrPending
}

func FeatureContext(s *godog.Suite) {
	api := &apiFeature{}
	s.Step(`^I send "([^"]*)" request to "([^"]*)"$`, api.iSendrequestTo)
	s.Step(`^the response code should be (\d+)$`, api.theResponseCodeShouldBe)
	s.Step(`^the response should match json:$`, api.theResponseShouldMatchJSON)
}
```

### Step 4

Now we can implemented steps, since we know what behavior we expect:

``` go
// file: api_test.go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"

	"github.com/DATA-DOG/godog"
	"github.com/DATA-DOG/godog/gherkin"
)

type apiFeature struct {
	resp *httptest.ResponseRecorder
}

func (a *apiFeature) resetResponse(interface{}) {
	a.resp = httptest.NewRecorder()
}

func (a *apiFeature) iSendrequestTo(method, endpoint string) (err error) {
	req, err := http.NewRequest(method, endpoint, nil)
	if err != nil {
		return
	}

	// handle panic
	defer func() {
		switch t := recover().(type) {
		case string:
			err = fmt.Errorf(t)
		case error:
			err = t
		}
	}()

	switch endpoint {
	case "/version":
		getVersion(a.resp, req)
	default:
		err = fmt.Errorf("unknown endpoint: %s", endpoint)
	}
	return
}

func (a *apiFeature) theResponseCodeShouldBe(code int) error {
	if code != a.resp.Code {
		return fmt.Errorf("expected response code to be: %d, but actual is: %d", code, a.resp.Code)
	}
	return nil
}

func (a *apiFeature) theResponseShouldMatchJSON(body *gherkin.DocString) (err error) {
	var expected, actual []byte
	var data interface{}
	if err = json.Unmarshal([]byte(body.Content), &data); err != nil {
		return
	}
	if expected, err = json.Marshal(data); err != nil {
		return
	}
	actual = a.resp.Body.Bytes()
	if !bytes.Equal(actual, expected) {
		err = fmt.Errorf("expected json, does not match actual: %s", string(actual))
	}
	return
}

func FeatureContext(s *godog.Suite) {
	api := &apiFeature{}

	s.BeforeScenario(api.resetResponse)

	s.Step(`^I send "(GET|POST|PUT|DELETE)" request to "([^"]*)"$`, api.iSendrequestTo)
	s.Step(`^the response code should be (\d+)$`, api.theResponseCodeShouldBe)
	s.Step(`^the response should match json:$`, api.theResponseShouldMatchJSON)
}
```

**NOTE:** the `getVersion` handler call on **/version** endpoint. We actually need to implement it now.
If we made some mistakes in step implementations, we will know about it when we run the tests.

Though, we could also improve our **JSON** comparison function to range through the interfaces and
match their types and values.

In case if some router is used, you may search the handler based on the endpoint. Current example
uses a standard http package.

### Step 5

Finally, lets implement the **api** server:

``` go
// file: api.go
// Example - demonstrates REST API server implementation tests.
package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/DATA-DOG/godog"
)

func getVersion(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		fail(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	data := struct {
		Version string `json:"version"`
	}{Version: godog.Version}

	ok(w, data)
}

func main() {
	http.HandleFunc("/version", getVersion)
	http.ListenAndServe(":8080", nil)
}

// fail writes a json response with error msg and status header
func fail(w http.ResponseWriter, msg string, status int) {
	w.Header().Set("Content-Type", "application/json")

	data := struct {
		Error string `json:"error"`
	}{Error: msg}

	resp, _ := json.Marshal(data)
	w.WriteHeader(status)

	fmt.Fprintf(w, string(resp))
}

// ok writes data to response with 200 status
func ok(w http.ResponseWriter, data interface{}) {
	w.Header().Set("Content-Type", "application/json")

	if s, ok := data.(string); ok {
		fmt.Fprintf(w, s)
		return
	}

	resp, err := json.Marshal(data)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		fail(w, "oops something evil has happened", 500)
		return
	}

	fmt.Fprintf(w, string(resp))
}
```

The implementation details are clearly production ready and the imported **godog** package is only
used to respond with the correct constant version number.

### Step 6

Run our tests to see whether everything is happening as we have expected: `godog version.feature`

![Screenshot](https://raw.github.com/DATA-DOG/godog/master/examples/api/screenshots/passed.png)

### Conclusions

Hope you have enjoyed it like I did.

Any developer (who is the target of our application) can read and remind himself about how API behaves.
# An example of API with DB

The following example demonstrates steps how we describe and test our API with DB using **godog**.
To start with, see [API example](https://github.com/DATA-DOG/godog/tree/master/examples/api) before.
We have extended it to be used with database.

The interesting point is, that we have [go-txdb](https://github.com/DATA-DOG/go-txdb) library,
which has an implementation of custom sql.driver to allow execute every and each scenario
within a **transaction**. After it completes, transaction is rolled back so the state could
be clean for the next scenario.

To run **users.feature** you need MySQL installed on your system with an anonymous root password.
Then run:

    make test

The json comparisom function should be improved and we should also have placeholders for primary
keys when comparing a json result.
[![Build Status](https://secure.travis-ci.org/cucumber/gherkin-go.svg)](http://travis-ci.org/cucumber/gherkin-go)

Gherkin parser/compiler for Go. Please see [Gherkin](https://github.com/cucumber/gherkin) for details.
# go-toml

Go library for the [TOML](https://github.com/mojombo/toml) format.

This library supports TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

[![GoDoc](https://godoc.org/github.com/pelletier/go-toml?status.svg)](http://godoc.org/github.com/pelletier/go-toml)
[![license](https://img.shields.io/github/license/pelletier/go-toml.svg)](https://github.com/pelletier/go-toml/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/pelletier/go-toml.svg?branch=master)](https://travis-ci.org/pelletier/go-toml)
[![Coverage Status](https://coveralls.io/repos/github/pelletier/go-toml/badge.svg?branch=master)](https://coveralls.io/github/pelletier/go-toml?branch=master)
[![Go Report Card](https://goreportcard.com/badge/github.com/pelletier/go-toml)](https://goreportcard.com/report/github.com/pelletier/go-toml)

## Features

Go-toml provides the following features for using data parsed from TOML documents:

* Load TOML documents from files and string data
* Easily navigate TOML structure using Tree
* Mashaling and unmarshaling to and from data structures
* Line & column position data for all parsed elements
* [Query support similar to JSON-Path](query/)
* Syntax errors contain line and column numbers

## Import

```go
import "github.com/pelletier/go-toml"
```

## Usage example

Read a TOML document:

```go
config, _ := toml.Load(`
[postgres]
user = "pelletier"
password = "mypassword"`)
// retrieve data directly
user := config.Get("postgres.user").(string)

// or using an intermediate object
postgresConfig := config.Get("postgres").(*toml.Tree)
password := postgresConfig.Get("password").(string)
```

Or use Unmarshal:

```go
type Postgres struct {
    User     string
    Password string
}
type Config struct {
    Postgres Postgres
}

doc := []byte(`
[Postgres]
User = "pelletier"
Password = "mypassword"`)

config := Config{}
toml.Unmarshal(doc, &config)
fmt.Println("user=", config.Postgres.User)
```

Or use a query:

```go
// use a query to gather elements without walking the tree
q, _ := query.Compile("$..[user,password]")
results := q.Execute(config)
for ii, item := range results.Values() {
    fmt.Println("Query result %d: %v", ii, item)
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
    go install github.com/pelletier/go-toml/cmd/tomljson
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

### Fuzzing

The script `./fuzz.sh` is available to
run [go-fuzz](https://github.com/dvyukov/go-fuzz) on go-toml.

## Versioning

Go-toml follows [Semantic Versioning](http://semver.org/). The supported version
of [TOML](https://github.com/toml-lang/toml) is indicated at the beginning of
this document. The last two major versions of Go are supported
(see [Go Release Policy](https://golang.org/doc/devel/release.html#policy)).

## License

The MIT License (MIT). Read [LICENSE](LICENSE).
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
## eycore ##

Engine Yard Core API Golang client Edit Edit

### History ###

* v0.3.4 - Added Feature implementation
* v0.3.3 - Added Provider credentials
* v0.3.2 - Now modeling Applications
* v0.3.1 - Added servers.All
* v0.3.0 - Redesign!
* v0.2.12 - Params are now URL escaped for every request
* v0.2.11 - Catching low-level HTTP errors in CoreAPI
* v0.2.10 - Mocking /environments/:id/requests
* v0.2.9 - Removed attributes that kubey don't do
* v0.2.8 - Providers, Locations, Flavors
* v0.2.7 - Detroit the environment
* v0.2.6 - Support ApplyEnvironment, code around API inconsistency
* v0.2.5 - Account.BillingSignupURL is string, not bool
* v0.2.4 - Stupid debug messages
* v0.2.3 - MockAPI supports posting to /tokens
* v0.2.2 - Quick fix to add ip specification to environment boot params
* v0.2.1 - Added basic Address support
* v0.2.0 - Added POST operations
* v0.1.2 - Added basic MockAPI implementation
* v0.1.1 - First viable release
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
var AppFs = afero.NewMemMapFs()

or

var AppFs = afero.NewOsFs()
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
We would replace it with:
```go
AppFs.Open('/tmp/foo')
```

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
fs := afero.NewMemMapFs()
afs := &afero.Afero{Fs: fs}
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
	appFS := afero.NewMemMapFs()
	// create test files and directories
	appFS.MkdirAll("src/a", 0755)
	afero.WriteFile(appFS, "src/a/b", []byte("file b"), 0644)
	afero.WriteFile(appFS, "src/c", []byte("file c"), 0644)
	name := "src/c"
	_, err := appFS.Stat(name)
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
* [Imgur’s Incus](https://github.com/Imgur/incus)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)
* [Docker Notary](https://github.com/docker/Notary)
* [BloomApi](https://www.bloomapi.com/)
* [doctl](https://github.com/digitalocean/doctl)
* [Clairctl](https://github.com/jgsqware/clairctl)

[![Build Status](https://travis-ci.org/spf13/viper.svg)](https://travis-ci.org/spf13/viper) [![Join the chat at https://gitter.im/spf13/viper](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spf13/viper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![GoDoc](https://godoc.org/github.com/spf13/viper?status.svg)](https://godoc.org/github.com/spf13/viper)


## What is Viper?

Viper is a complete configuration solution for Go applications including 12-Factor apps. It is designed
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
required for a key, but it’s useful in the event that a key hasn’t been set via
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

For individual flags, the `BindPFlag()` method provides this functionality.

Example:

```go
serverCmd.Flags().Int("port", 1138, "Port to run Application server on")
viper.BindPFlag("port", serverCmd.Flags().Lookup("port"))
```

You can also bind an existing set of pflags (pflag.FlagSet):

Example:

```go
pflag.Int("flagname", 1234, "help message for flagname")

pflag.Parse()
viper.BindPFlags(pflag.CommandLine)

i := viper.GetInt("flagname") // retrieve values from viper instead of pflag
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

	// using standard library "flag" package
	flag.Int("flagname", 1234, "help message for flagname")

	pflag.CommandLine.AddGoFlagSet(flag.CommandLine)
	pflag.Parse()
	viper.BindPFlags(pflag.CommandLine)

	i := viper.GetInt("flagname") // retrieve value from viper

	...
}
```

#### Flag interfaces

Viper provides two Go interfaces to bind other flag systems if you don’t use `Pflags`.

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

In Viper, there are a few ways to get a value depending on the value’s type.
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
Now it’s easy to create these 2 caches separately as:

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

In all of the examples above, they demonstrate using viper in its singleton
style approach.

### Working with multiple vipers

You can also create many different vipers for use in your application. Each will
have its own unique set of configurations and values. Each can read from a
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
cast
====
[![GoDoc](https://godoc.org/github.com/spf13/cast?status.svg)](https://godoc.org/github.com/spf13/cast)
[![Build Status](https://api.travis-ci.org/spf13/cast.svg?branch=master)](https://travis-ci.org/spf13/cast)
[![Go Report Card](https://goreportcard.com/badge/github.com/spf13/cast)](https://goreportcard.com/report/github.com/spf13/cast)

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
* [nehm](https://github.com/bogem/nehm)

[![Build Status](https://travis-ci.org/spf13/cobra.svg "Travis CI status")](https://travis-ci.org/spf13/cobra)
[![CircleCI status](https://circleci.com/gh/spf13/cobra.png?circle-token=:circle-token "CircleCI status")](https://circleci.com/gh/spf13/cobra)
[![GoDoc](https://godoc.org/github.com/spf13/cobra?status.svg)](https://godoc.org/github.com/spf13/cobra)

# Table of Contents

- [Overview](#overview)
- [Concepts](#concepts)
  * [Commands](#commands)
  * [Flags](#flags)
- [Installing](#installing)
- [Getting Started](#getting-started)
  * [Using the Cobra Generator](#using-the-cobra-generator)
  * [Using the Cobra Library](#using-the-cobra-library)
  * [Working with Flags](#working-with-flags)
  * [Positional and Custom Arguments](#positional-and-custom-arguments)
  * [Example](#example)
  * [Help Command](#help-command)
  * [Usage Message](#usage-message)
  * [PreRun and PostRun Hooks](#prerun-and-postrun-hooks)
  * [Suggestions when "unknown command" happens](#suggestions-when-unknown-command-happens)
  * [Generating documentation for your command](#generating-documentation-for-your-command)
  * [Generating bash completions](#generating-bash-completions)
- [Contributing](#contributing)
- [License](#license)

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
* Automatic help flag recognition of `-h`, `--help`, etc.
* Automatically generated bash autocomplete for your application
* Automatically generated man pages for your application
* Command aliases so you can change things without breaking them
* The flexibility to define your own help, usage, etc.
* Optional tight integration with [viper](http://github.com/spf13/viper) for 12-factor apps

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

[More about cobra.Command](https://godoc.org/github.com/spf13/cobra#Command)

## Flags

A flag is a way to modify the behavior of a command. Cobra supports
fully POSIX-compliant flags as well as the Go [flag package](https://golang.org/pkg/flag/).
A Cobra command can define flags that persist through to children commands
and flags that are only available to that command.

In the example above, 'port' is the flag.

Flag functionality is provided by the [pflag
library](https://github.com/spf13/pflag), a fork of the flag standard library
which maintains the same interface while adding POSIX compliance.

# Installing
Using Cobra is easy. First, use `go get` to install the latest version
of the library. This command will install the `cobra` generator executable
along with the library and its dependencies:

    go get -u github.com/spf13/cobra/cobra

Next, include Cobra in your application:

```go
import "github.com/spf13/cobra"
```

# Getting Started

While you are welcome to provide your own organization, typically a Cobra-based
application will follow the following organizational structure:

```
  ▾ appName/
    ▾ cmd/
        add.go
        your.go
        commands.go
        here.go
      main.go
```

In a Cobra app, typically the main.go file is very bare. It serves one purpose: initializing Cobra.

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

[Here](https://github.com/spf13/cobra/blob/master/cobra/README.md) you can find more information about it.

## Using the Cobra Library

To manually implement Cobra you need to create a bare main.go file and a RootCmd file.
You will optionally provide additional commands as you see fit.

### Create rootCmd

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

func Execute() {
  RootCmd.Execute()
}

func initConfig() {
  // Don't forget to read config either from cfgFile or from home directory!
  if cfgFile != "" {
    // Use config file from the flag.
    viper.SetConfigFile(cfgFile)
  } else {
    // Find home directory.
    home, err := homedir.Dir()
    if err != nil {
      fmt.Println(err)
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

### Local Flag on Parent Commands

By default Cobra only parses local flags on the target command, any local flags on 
parent commands are ignored. By enabling `Command.TraverseChildren` Cobra will 
parse local flags on each command before executing the target command.

```go
command := cobra.Command{
  Use: "print [OPTIONS] [COMMANDS]",
  TraverseChildren: true,
}
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

## Positional and Custom Arguments

Validation of positional arguments can be specified using the `Args` field
of `Command`.

The following validators are built in:

- `NoArgs` - the command will report an error if there are any positional args.
- `ArbitraryArgs` - the command will accept any args.
- `OnlyValidArgs` - the command will report an error if there are any positional args that are not in the `ValidArgs` field of `Command`.
- `MinimumNArgs(int)` - the command will report an error if there are not at least N positional args.
- `MaximumNArgs(int)` - the command will report an error if there are more than N positional args.
- `ExactArgs(int)` - the command will report an error if there are not exactly N positional args.
- `RangeArgs(min, max)` - the command will report an error if the number of args is not between the minimum and maximum number of expected args.

An example of setting the custom validator:

```go
var cmd = &cobra.Command{
  Short: "hello",
  Args: func(cmd *cobra.Command, args []string) error {
    if len(args) < 1 {
      return errors.New("requires at least one arg")
    }
    if myapp.IsValidColor(args[0]) {
      return nil
    }
    return fmt.Errorf("invalid color specified: %s", args[0])
  },
  Run: func(cmd *cobra.Command, args []string) {
    fmt.Println("Hello, World!")
  },
}
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
For many years people have printed back to the screen.`,
    Args: cobra.MinimumNArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
      fmt.Println("Print: " + strings.Join(args, " "))
    },
  }

  var cmdEcho = &cobra.Command{
    Use:   "echo [string to echo]",
    Short: "Echo anything to the screen",
    Long: `echo is for echoing anything back.
Echo works a lot like print, except it has a child command.`,
    Args: cobra.MinimumNArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
      fmt.Println("Print: " + strings.Join(args, " "))
    },
  }

  var cmdTimes = &cobra.Command{
    Use:   "times [# times] [string to echo]",
    Short: "Echo anything to the screen more times",
    Long: `echo things multiple times back to the user by providing
a count and a string.`,
    Args: cobra.MinimumNArgs(1),
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

## Help Command

Cobra automatically adds a help command to your application when you have subcommands.
This will be called when a user runs 'app help'. Additionally, help will also
support all other commands as input. Say, for instance, you have a command called
'create' without any additional configuration; Cobra will work when 'app help
create' is called.  Every command will automatically have the '--help' flag added.

### Example

The following output is automatically generated by Cobra. Nothing beyond the
command and flag definitions are needed.

    $ cobra help

    Cobra is a CLI library for Go that empowers applications.
    This application is a tool to generate the needed files
    to quickly create a Cobra application.

    Usage:
      cobra [command]

    Available Commands:
      add         Add a command to a Cobra Application
      help        Help about any command
      init        Initialize a Cobra Application

    Flags:
      -a, --author string    author name for copyright attribution (default "YOUR NAME")
          --config string    config file (default is $HOME/.cobra.yaml)
      -h, --help             help for cobra
      -l, --license string   name of license for the project
          --viper            use Viper for configuration (default true)

    Use "cobra [command] --help" for more information about a command.


Help is just a command like any other. There is no special logic or behavior
around it. In fact, you can provide your own if you want.

### Defining your own help

You can provide your own Help command or your own template for the default command to use
with followind functions:

```go
cmd.SetHelpCommand(cmd *Command)
cmd.SetHelpFunc(f func(*Command, []string))
cmd.SetHelpTemplate(s string)
```

The latter two will also apply to any children commands.

## Usage Message

When the user provides an invalid flag or invalid command, Cobra responds by
showing the user the 'usage'.

### Example
You may recognize this from the help above. That's because the default help
embeds the usage as part of its output.

    $ cobra --invalid
    Error: unknown flag: --invalid
    Usage:
      cobra [command]

    Available Commands:
      add         Add a command to a Cobra Application
      help        Help about any command
      init        Initialize a Cobra Application

    Flags:
      -a, --author string    author name for copyright attribution (default "YOUR NAME")
          --config string    config file (default is $HOME/.cobra.yaml)
      -h, --help             help for cobra
      -l, --license string   name of license for the project
          --viper            use Viper for configuration (default true)

    Use "cobra [command] --help" for more information about a command.

### Defining your own usage
You can provide your own usage function or template for Cobra to use.
Like help, the function and template are overridable through public methods:

```go
cmd.SetUsageFunc(f func(*Command) error)
cmd.SetUsageTemplate(s string)
```

## PreRun and PostRun Hooks

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
  rootCmd.Execute()
  fmt.Println()
  rootCmd.SetArgs([]string{"sub", "arg1", "arg2"})
  rootCmd.Execute()
}
```

Output:
```
Inside rootCmd PersistentPreRun with args: []
Inside rootCmd PreRun with args: []
Inside rootCmd Run with args: []
Inside rootCmd PostRun with args: []
Inside rootCmd PersistentPostRun with args: []

Inside rootCmd PersistentPreRun with args: [arg1 arg2]
Inside subCmd PreRun with args: [arg1 arg2]
Inside subCmd Run with args: [arg1 arg2]
Inside subCmd PostRun with args: [arg1 arg2]
Inside subCmd PersistentPostRun with args: [arg1 arg2]
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

## Generating documentation for your command

Cobra can generate documentation based on subcommands, flags, etc. in the following formats:

- [Markdown](doc/md_docs.md)
- [ReStructured Text](doc/rest_docs.md)
- [Man Page](doc/man_docs.md)

## Generating bash completions

Cobra can generate a bash-completion file. If you add more information to your command, these completions can be amazingly powerful and flexible.  Read more about it in [Bash Completions](bash_completions.md).

# Contributing

1. Fork it
2. Download your fork to your PC (`git clone https://github.com/your_username/cobra && cd cobra`)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Make changes and add them (`git add .`)
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin my-new-feature`)
7. Create new pull request

# License

Cobra is released under the Apache 2.0 license. See [LICENSE.txt](https://github.com/spf13/cobra/blob/master/LICENSE.txt)
# Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

In order to use the cobra command, compile it using the following command:

    go get github.com/spf13/cobra/cobra

This will create the cobra executable under your `$GOPATH/bin` directory.

### cobra init

The `cobra init [app]` command will create your initial application code
for you. It is a very powerful application that will populate your program with
the right structure so you can immediately enjoy all the benefits of Cobra. It
will also automatically apply the license you specify to your application.

Cobra init is pretty smart. You can provide it a full path, or simply a path
similar to what is expected in the import.

```
cobra init github.com/spf13/newApp
```

### cobra add

Once an application is initialized, Cobra can create additional commands for you.
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
Otherwise, you will encounter errors.
For example, `cobra add add-user` is incorrect, but `cobra add addUser` is valid.*

Once you have run these three commands you would have an app structure similar to
the following:

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
with `go run main.go help serve`, etc. would all work.

Obviously you haven't added your own code to these yet. The commands are ready
for you to give them their tasks. Have fun!

### Configuring the cobra generator

The Cobra generator will be easier to use if you provide a simple configuration
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
standard usage. Eg.

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

NOTE: You can also use the library in a non-global setting by creating an instance of a Notebook:

```go
notepad = jww.NewNotepad(jww.LevelInfo, jww.LevelTrace, os.Stdout, ioutil.Discard, "", log.Ldate|log.Ltime)
notepad.WARN.Println("Some warning"")
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


### Setting a log file

JWW can log to any `io.Writer`:


```go

    jww.SetLogOutput(customWriter) 

```


# More information

This is an early release. I’ve been using it for a while and this is the
third interface I’ve tried. I like this one pretty well, but no guarantees
that it won’t change a bit.

I wrote this for use in [hugo](https://gohugo.io). If you are looking
for a static website engine that’s super fast please checkout Hugo.
