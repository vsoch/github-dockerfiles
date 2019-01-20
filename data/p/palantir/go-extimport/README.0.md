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
# Terminal progress bar for Go  

[![Join the chat at https://gitter.im/cheggaaa/pb](https://badges.gitter.im/cheggaaa/pb.svg)](https://gitter.im/cheggaaa/pb?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Simple progress bar for console programs.    
   
Please check the new version https://github.com/cheggaaa/pb/tree/v2 (currently, it's beta)

## Installation

```
go get gopkg.in/cheggaaa/pb.v1
```   

## Usage   

```Go
package main

import (
	"gopkg.in/cheggaaa/pb.v1"
	"time"
)

func main() {
	count := 100000
	bar := pb.StartNew(count)
	for i := 0; i < count; i++ {
		bar.Increment()
		time.Sleep(time.Millisecond)
	}
	bar.FinishPrint("The End!")
}

```

Result will be like this:

```
> go run test.go
37158 / 100000 [================>_______________________________] 37.16% 1m11s
```

## Customization

```Go  
// create bar
bar := pb.New(count)

// refresh info every second (default 200ms)
bar.SetRefreshRate(time.Second)

// show percents (by default already true)
bar.ShowPercent = true

// show bar (by default already true)
bar.ShowBar = true

// no counters
bar.ShowCounters = false

// show "time left"
bar.ShowTimeLeft = true

// show average speed
bar.ShowSpeed = true

// sets the width of the progress bar
bar.SetWidth(80)

// sets the width of the progress bar, but if terminal size smaller will be ignored
bar.SetMaxWidth(80)

// convert output to readable format (like KB, MB)
bar.SetUnits(pb.U_BYTES)

// and start
bar.Start()
``` 

## Progress bar for IO Operations

```go
// create and start bar
bar := pb.New(myDataLen).SetUnits(pb.U_BYTES)
bar.Start()

// my io.Reader
r := myReader

// my io.Writer
w := myWriter

// create proxy reader
reader := bar.NewProxyReader(r)

// and copy from pb reader
io.Copy(w, reader)

```

```go
// create and start bar
bar := pb.New(myDataLen).SetUnits(pb.U_BYTES)
bar.Start()

// my io.Reader
r := myReader

// my io.Writer
w := myWriter

// create multi writer
writer := io.MultiWriter(w, bar)

// and copy
io.Copy(writer, r)

bar.Finish()
```

## Custom Progress Bar Look-and-feel

```go
bar.Format("<.- >")
```

## Multiple Progress Bars (experimental and unstable)

Do not print to terminal while pool is active.

```go
package main

import (
    "math/rand"
    "sync"
    "time"

    "gopkg.in/cheggaaa/pb.v1"
)

func main() {
    // create bars
    first := pb.New(200).Prefix("First ")
    second := pb.New(200).Prefix("Second ")
    third := pb.New(200).Prefix("Third ")
    // start pool
    pool, err := pb.StartPool(first, second, third)
    if err != nil {
        panic(err)
    }
    // update bars
    wg := new(sync.WaitGroup)
    for _, bar := range []*pb.ProgressBar{first, second, third} {
        wg.Add(1)
        go func(cb *pb.ProgressBar) {
            for n := 0; n < 200; n++ {
                cb.Increment()
                time.Sleep(time.Millisecond * time.Duration(rand.Intn(100)))
            }
            cb.Finish()
            wg.Done()
        }(bar)
    }
    wg.Wait()
    // close pool
    pool.Stop()
}
```

The result will be as follows:

```
$ go run example/multiple.go 
First 141 / 1000 [===============>---------------------------------------] 14.10 % 44s
Second 139 / 1000 [==============>---------------------------------------] 13.90 % 44s
Third 152 / 1000 [================>--------------------------------------] 15.20 % 40s
```
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

go-runewidth
============

[![Build Status](https://travis-ci.org/mattn/go-runewidth.png?branch=master)](https://travis-ci.org/mattn/go-runewidth)
[![Coverage Status](https://coveralls.io/repos/mattn/go-runewidth/badge.png?branch=HEAD)](https://coveralls.io/r/mattn/go-runewidth?branch=HEAD)
[![GoDoc](https://godoc.org/github.com/mattn/go-runewidth?status.svg)](http://godoc.org/github.com/mattn/go-runewidth)
[![Go Report Card](https://goreportcard.com/badge/github.com/mattn/go-runewidth)](https://goreportcard.com/report/github.com/mattn/go-runewidth)

Provides functions to get fixed width of the character or string.

Usage
-----

```go
runewidth.StringWidth("つのだ☆HIRO") == 12
```


Author
------

Yasuhiro Matsumoto

License
-------

under the MIT License: http://mattn.mit-license.org/2013
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
go-difflib
==========

[![Build Status](https://travis-ci.org/pmezard/go-difflib.png?branch=master)](https://travis-ci.org/pmezard/go-difflib)
[![GoDoc](https://godoc.org/github.com/pmezard/go-difflib/difflib?status.svg)](https://godoc.org/github.com/pmezard/go-difflib/difflib)

Go-difflib is a partial port of python 3 difflib package. Its main goal
was to make unified and context diff available in pure Go, mostly for
testing purposes.

The following class and functions (and related tests) have be ported:

* `SequenceMatcher`
* `unified_diff()`
* `context_diff()`

## Installation

```bash
$ go get github.com/pmezard/go-difflib/difflib
```

### Quick Start

Diffs are configured with Unified (or ContextDiff) structures, and can
be output to an io.Writer or returned as a string.

```Go
diff := UnifiedDiff{
    A:        difflib.SplitLines("foo\nbar\n"),
    B:        difflib.SplitLines("foo\nbaz\n"),
    FromFile: "Original",
    ToFile:   "Current",
    Context:  3,
}
text, _ := GetUnifiedDiffString(diff)
fmt.Printf(text)
```

would output:

```
--- Original
+++ Current
@@ -1,3 +1,3 @@
 foo
-bar
+baz
```

Testify - Thou Shalt Write Tests
================================

[![Build Status](https://travis-ci.org/stretchr/testify.svg)](https://travis-ci.org/stretchr/testify) [![Go Report Card](https://goreportcard.com/badge/github.com/stretchr/testify)](https://goreportcard.com/report/github.com/stretchr/testify) [![GoDoc](https://godoc.org/github.com/stretchr/testify?status.svg)](https://godoc.org/github.com/stretchr/testify)

Go code (golang) set of packages that provide many tools for testifying that your code will behave as you intend.

Features include:

  * [Easy assertions](#assert-package)
  * [Mocking](#mock-package)
  * [Testing suite interfaces and functions](#suite-package)

Get started:

  * Install testify with [one line of code](#installation), or [update it with another](#staying-up-to-date)
  * For an introduction to writing test code in Go, see http://golang.org/doc/code.html#Testing
  * Check out the API Documentation http://godoc.org/github.com/stretchr/testify
  * To make your testing life easier, check out our other project, [gorc](http://github.com/stretchr/gorc)
  * A little about [Test-Driven Development (TDD)](http://en.wikipedia.org/wiki/Test-driven_development)



[`assert`](http://godoc.org/github.com/stretchr/testify/assert "API documentation") package
-------------------------------------------------------------------------------------------

The `assert` package provides some helpful methods that allow you to write better test code in Go.

  * Prints friendly, easy to read failure descriptions
  * Allows for very readable code
  * Optionally annotate each assertion with a message

See it in action:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {

  // assert equality
  assert.Equal(t, 123, 123, "they should be equal")

  // assert inequality
  assert.NotEqual(t, 123, 456, "they should not be equal")

  // assert for nil (good for errors)
  assert.Nil(t, object)

  // assert for not nil (good when you expect something)
  if assert.NotNil(t, object) {

    // now we know that object isn't nil, we are safe to make
    // further assertions without causing any errors
    assert.Equal(t, "Something", object.Value)

  }

}
```

  * Every assert func takes the `testing.T` object as the first argument.  This is how it writes the errors out through the normal `go test` capabilities.
  * Every assert func returns a bool indicating whether the assertion was successful or not, this is useful for if you want to go on making further assertions under certain conditions.

if you assert many times, use the below:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
  assert := assert.New(t)

  // assert equality
  assert.Equal(123, 123, "they should be equal")

  // assert inequality
  assert.NotEqual(123, 456, "they should not be equal")

  // assert for nil (good for errors)
  assert.Nil(object)

  // assert for not nil (good when you expect something)
  if assert.NotNil(object) {

    // now we know that object isn't nil, we are safe to make
    // further assertions without causing any errors
    assert.Equal("Something", object.Value)
  }
}
```

[`require`](http://godoc.org/github.com/stretchr/testify/require "API documentation") package
---------------------------------------------------------------------------------------------

The `require` package provides same global functions as the `assert` package, but instead of returning a boolean result they terminate current test.

See [t.FailNow](http://golang.org/pkg/testing/#T.FailNow) for details.

[`mock`](http://godoc.org/github.com/stretchr/testify/mock "API documentation") package
----------------------------------------------------------------------------------------

The `mock` package provides a mechanism for easily writing mock objects that can be used in place of real objects when writing test code.

An example test function that tests a piece of code that relies on an external object `testObj`, can setup expectations (testify) and assert that they indeed happened:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/mock"
)

/*
  Test objects
*/

// MyMockedObject is a mocked object that implements an interface
// that describes an object that the code I am testing relies on.
type MyMockedObject struct{
  mock.Mock
}

// DoSomething is a method on MyMockedObject that implements some interface
// and just records the activity, and returns what the Mock object tells it to.
//
// In the real object, this method would do something useful, but since this
// is a mocked object - we're just going to stub it out.
//
// NOTE: This method is not being tested here, code that uses this object is.
func (m *MyMockedObject) DoSomething(number int) (bool, error) {

  args := m.Called(number)
  return args.Bool(0), args.Error(1)

}

/*
  Actual test functions
*/

// TestSomething is an example of how to use our test object to
// make assertions about some target code we are testing.
func TestSomething(t *testing.T) {

  // create an instance of our test object
  testObj := new(MyMockedObject)

  // setup expectations
  testObj.On("DoSomething", 123).Return(true, nil)

  // call the code we are testing
  targetFuncThatDoesSomethingWithObj(testObj)

  // assert that the expectations were met
  testObj.AssertExpectations(t)

}
```

For more information on how to write mock code, check out the [API documentation for the `mock` package](http://godoc.org/github.com/stretchr/testify/mock).

You can use the [mockery tool](http://github.com/vektra/mockery) to autogenerate the mock code against an interface as well, making using mocks much quicker.

[`suite`](http://godoc.org/github.com/stretchr/testify/suite "API documentation") package
-----------------------------------------------------------------------------------------

The `suite` package provides functionality that you might be used to from more common object oriented languages.  With it, you can build a testing suite as a struct, build setup/teardown methods and testing methods on your struct, and run them with 'go test' as per normal.

An example suite is shown below:

```go
// Basic imports
import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/suite"
)

// Define the suite, and absorb the built-in basic suite
// functionality from testify - including a T() method which
// returns the current testing context
type ExampleTestSuite struct {
    suite.Suite
    VariableThatShouldStartAtFive int
}

// Make sure that VariableThatShouldStartAtFive is set to five
// before each test
func (suite *ExampleTestSuite) SetupTest() {
    suite.VariableThatShouldStartAtFive = 5
}

// All methods that begin with "Test" are run as tests within a
// suite.
func (suite *ExampleTestSuite) TestExample() {
    assert.Equal(suite.T(), 5, suite.VariableThatShouldStartAtFive)
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestExampleTestSuite(t *testing.T) {
    suite.Run(t, new(ExampleTestSuite))
}
```

For a more complete example, using all of the functionality provided by the suite package, look at our [example testing suite](https://github.com/stretchr/testify/blob/master/suite/suite_test.go)

For more information on writing suites, check out the [API documentation for the `suite` package](http://godoc.org/github.com/stretchr/testify/suite).

`Suite` object has assertion methods:

```go
// Basic imports
import (
    "testing"
    "github.com/stretchr/testify/suite"
)

// Define the suite, and absorb the built-in basic suite
// functionality from testify - including assertion methods.
type ExampleTestSuite struct {
    suite.Suite
    VariableThatShouldStartAtFive int
}

// Make sure that VariableThatShouldStartAtFive is set to five
// before each test
func (suite *ExampleTestSuite) SetupTest() {
    suite.VariableThatShouldStartAtFive = 5
}

// All methods that begin with "Test" are run as tests within a
// suite.
func (suite *ExampleTestSuite) TestExample() {
    suite.Equal(suite.VariableThatShouldStartAtFive, 5)
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestExampleTestSuite(t *testing.T) {
    suite.Run(t, new(ExampleTestSuite))
}
```

------

Installation
============

To install Testify, use `go get`:

    go get github.com/stretchr/testify

This will then make the following packages available to you:

    github.com/stretchr/testify/assert
    github.com/stretchr/testify/mock
    github.com/stretchr/testify/http

Import the `testify/assert` package into your code using this template:

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {

  assert.True(t, true, "True is true!")

}
```

------

Staying up to date
==================

To update Testify to the latest version, use `go get -u github.com/stretchr/testify`.

------

Contributing
============

Please feel free to submit issues, fork the repository and send pull requests!

When submitting an issue, we ask that you please include a complete test function that demonstrates the issue.  Extra credit for those using Testify to write the test code that demonstrates it.
pkg
===

`pkg` is a collection of Go packages that provide various different functionality. The packages in this project are
generally independent and strive to depend on as few external packages as possible. Many of the packages in the project
are also independent from each other.

An overview of some of the packages is included below. Refer to the package comments for individual packages for more
information.

cli
---
`cli` provides a framework for creating CLI applications. It provides support for commands, subcommands, flags, before
and after hooks, documentation, deprecation, command-line completion and other functionality.

matcher
-------
`matcher` allows files to be matched based on their name or path. Supports composing and combining matchers and provides
data structures that can be used as configuration to specify include and exclude rules.

objmatcher
----------
`objmatcher` provides the ability to match objects based on criteria and returns a descriptive error when an object does
not match its expectation. When used in combination with maps, makes it easy to perform complex matching on maps in a
declarative manner (for example, requiring that some map entries match an expectation exactly while others should match
a particular regular expression).

pkgpath
-------
`pkgpath` provides functions for getting Go package paths. Provides functions for getting the paths to all of the
packages rooted in a directory and for converting between different representations of package paths including relative,
`GOPATH`-relative and absolute. Depends on `matcher`.

specdir
-------
`specdir` provides the ability to define specifications for directory layouts, verify that existing directories match
the specification and create new directory structures based on a specification.

License
-------
This project is made available under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).
gödel
=====

[![Bintray](https://img.shields.io/bintray/v/palantir/releases/godel.svg)](https://bintray.com/palantir/releases/godel/_latestVersion)
[![CircleCI](https://circleci.com/gh/palantir/godel.svg?style=shield)](https://circleci.com/gh/palantir/godel)

gödel is a Go build tool that provides tasks for configuring, formatting, checking, testing, building and publishing Go
projects in a declarative, consistent and reproducible manner across different platforms and environments. gödel can be
used in both local development environments and for verifying the correctness of project in CI environments. gödel uses
declarative configuration to define the parameters for a project and provides an executable that orchestrates build
tasks using standard Go commands. It centralizes project configuration and eliminates the need for custom build scripts
that conflate configuration with logic. gödel is designed to be portable, fast and lightweight -- adding it to a project
consists of copying a single file and directory into the project and adds less than 50kb of version-controlled material.

Features
--------
* Add to a project by copying the `godelw` script and the `godel` configuration directory into a project
* `./godelw git-hooks` installs Git commit hook that formats files on commit
* `./godelw idea` creates and configures an IntelliJ IDEA project for the project
* Supports configuring directories and files that should be excluded by the tool (vendor directory is excluded by default)
* `./godelw format` formats all code in a project
* `./godelw check` runs a variety of code linting checks on all the code in a project
* `./godelw license` applies a specified license header to all Go files in a project
  * Supports configuring custom license headers for specific directories or files
* `./godelw generate` runs `go generate` tasks for a project
* `./godelw test` runs the tests in the project
  * Configuration can be used to define test sets (such as integration tests) and run specific test sets
  * Supports outputting the test results in a JUnit XML format
* `./godelw build` builds executables for `main` packages in the project
  * Supports cross-platform compilation
  * Supports configuration of `ldflag` for version and other variables
  * Installs packages by default to speed up repeated builds
* `./godelw dist` creates distribution files for products
  * Supports creating `tgz` and `rpm` distributions
  * Supports customizing creation of distribution using scripts
* `./godelw publish` publishes artifacts to Bintray or Artifactory
* `palantir/godel/pkg/products` package provides a mechanism to easily write integration tests for gödel projects
  * Provides a function that builds the product executable or distribution and provides a path to invoke it
* `./godelw update` updates gödel to the version specified in `godel/config/godel.properties`
* `./godelw github-wiki` mirrors a documents directory to a GitHub Wiki repository
* `./godelw verify` runs the `format`, `import`, `license`, `check` and `test` tasks
  * Can be used locally as a single command to apply changes and run checks
  * Can be used in CI to verify that a project is in the proper state without applying changes

This list is not exhaustive -- run `./godelw --help` for a list of all of the available commands.

Documentation
-------------
Documentation for this project is in the `docs` directory and the [GitHub Wiki](https://github.com/palantir/godel/wiki)
(the GitHub Wiki mirrors the contents of the `docs` directory).

Development
-----------
The code for the tasks provided by gödel is in the `cmd` directory. gödel tasks fall into 2 categories: those whose
functionality are implemented directly in gödel packages and those whose functionality is implemented by a sub-program
that exposes its tasks as library functions that are directly callable.

The `app.go` file in the top-level `godel` package registers the top-level tasks available in the CLI. It registers the
tasks whose functionality is implemented directly in gödel directly. The tasks provided by sub-programs are defined in
`cmd/clicmds/cfgcli.go`.

After making changes to the code, run `./godelw verify` to format the code, apply the proper license headers, update
dependency information, run code linting checks and all unit tests.

gödel also defines integration tests in the `test/integration` directory. The tests in this file create a distribution
of gödel and run tests against it. Run `./godelw test --tags=integration` to run the integration tests (the integration
tests are not run by `./godelw verify` or `./godelw test` by default).

### Sub-applications in the apps directory
The functionality for some gödel tasks are provided by sub-applications. `distgo`, `gonform`, `gunit` and `okgo` are
such sub-applications and are located in the `apps` directory. These sub-applications can be compiled and run as self-
contained CLI applications, but also expose functionality as libraries.

Changes that are made in these sub-applications directly impact gödel, and many of the gödel integration tests test the
functionality provided by these sub-applications. The sub-applications also have their own set of tests. Each of the
sub-applications in the `apps` directory have their own test suite that is the name of the sub-application and can be
invoked using its tag -- for example, to run the tests for `distgo`, run `./godelw test --tags=distgo`.

Refer to the README files in the sub-applications for more information on application-specific development.

### Sub-applications outside of the repository
Some tasks such as `imports` and `license` use sub-applications that are defined outside of the repository (in this
case, `gocd` and `golicense`, respectively) and vendor the sub-applications to use their functionality. Changing these
tasks is akin to changing a vendored library -- locate the original repository for the library, make changes there and
then update the vendored library in gödel.

License
-------
This project is made available under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).
godelinit
=========
`godelinit` is a CLI that can be used to add gödel to any project. Once it is installed, invoking `godelinit` will add
the latest version of gödel to the working directory.

Installation
------------
`go install github.com/palantir/godel/godelinit`

Usage
-----
Run `godelinit` in the root directory of a Go project to add the `godelw` script and `godel` configuration directory
from the latest gödel release (as listed on https://github.com/palantir/godel/releases) to the project.

Running `godelinit` in the root directory of a project that already uses gödel will update that project to use the
latest version (if it is already on the latest version, it will be a no-op).

The `--version` flag can be used to specify the version of gödel that should be installed. This flag should be used if
the latest released version is not the desired one.

If a version is not specified using the `--version` flag, `godelinit` determines the latest release by querying the
GitHub API of the palantir/godel GitHub project. The version of the latest release is stored in a cache directory in the
gödel home directory. If the latest version was determined within the last hour, the cached version will be used (and
thus an API call will not be made). The `--ignore-cache` flag can be used to ignore the cached version and force it to
be retrieved using the GitHub API even if a valid cache entry exists.
gonform
=======
gonform is a library and CLI for running formatting operations on Go files. It uses
[gofmt](https://golang.org/cmd/gofmt/) and [ptimports](https://github.com/palantir/checks/tree/develop/ptimports) as the
libraries that perform the formatting operations.

Documentation
-------------
Documentation for gonform is provided in the Go code and as part of the application itself.

* Run `gonform --help` to get an overview of the commands and flags
* gonform is configured using a YML or JSON configuration file. Refer to the documentation in
  `apps/gonform/config/config.go` for information on the configuration parameters that are available.
* Refer to `apps/gonform/config/example_test.go` for sample configuration files

Development
-----------
Use the following commands for development. All paths in the example commands assume that they are run from the root
project directory of godel -- if the current working directory is `apps/gonform`, use `../../godelw` instead.

* Run `./godelw verify` to apply formatting, perform linting checks and run the gödel tests
* Run `./godelw test --tags=gonform` to run the gonform-specific tests (not included by default in the tests run by `./godlew verify`)
* Run `./godelw build` to build the gonform binary in `apps/gonform/build`

### Add a new formatter
* In order for a formatter to be added, it must be a Go program that has a main package
* The formatters are managed and packaged by [amalgomate](https://github.com/palantir/amalgomate)
* Add the code required for the new check (the main package and any supporting code) to the vendor directory
* Edit `apps/gonform/formatters.yml` and add an entry for the new formatter
  * Add an entry to `packages` where the key is the name of the formatter (no whitespace) and the value has a key
    named `main` and the value is the import path to the main package for the formatter. For more details on the
    config file format, refer to the documentation for amalgomate.
* Run `go generate` in the root directory of the project to re-generate the files in `generated_src`

### Generate
Run `go generate` in the `apps/gonform` directory to create or update the `generated_src` directory and the source files
within it. The `go generate` task for this project requires the amalgomate command to run. The version of amalgomate
used to build the distribution is included as a vendored dependency.
gunit
=====
gunit is a library and CLI for running Go tests, generating coverage reports and generating JUnit-style XML output. It
uses [go-junit-report](https://github.com/jstemmer/go-junit-report) as the library for formatting test reports and
[gt](https://godoc.org/rsc.io/gt) for running cached tests.

Documentation
-------------
Documentation for `gunit` is provided in the Go code and as part of the application itself.

* Run `gunit --help` to get an overview of the commands and flags
* gunit is configured using a YML or JSON configuration file. Refer to the documentation in
  `apps/gunit/config/config.go` for information on the configuration parameters that are available.
* Refer to `apps/gunit/config/example_test.go` for sample configuration files

Development
-----------
Use the following commands for development. All paths in the example commands assume that they are run from the root
project directory of godel -- if the current working directory is `apps/gunit`, use `../../godelw` instead.

* Run `./godelw verify` to apply formatting, perform linting checks and run the gödel tests
* Run `./godelw test --tags=gunit` to run the gunit-specific tests (not included by default in the tests run by `./godlew verify`)
* Run `./godelw build` to build the gunit binary in `apps/gunit/build`

### Add a new test utility
* In order for a test utility to be added, it must be a Go program that has a main package
* The test utilities are managed and packaged by [amalgomate](https://github.com/palantir/amalgomate)
* Add the code required for the new test utility (the main package and any supporting code) to the vendor directory
* Edit `apps/gunit/testers.yml` and add an entry for the new test utility
  * Add an entry to `packages` where the key is the name of the test utility (no whitespace) and the value has a key
    named `main` and the value is the import path to the `main` package for the test utility. For more details on the
    config file format, refer to the documentation for amalgomate.
* Run `go generate` in the root directory of the project to re-generate the files in `generated_src`

### Generate
Run `go generate` in the `apps/gonform` directory to create or update the `generated_src` directory and the source files
within it. The `go generate` task for this project requires the amalgomate command to run. The version of amalgomate
used to build the distribution is included as a vendored dependency.
distgo
======
distgo is a library and CLI for running, building, distributing and publishing products in a Go project.

Documentation
-------------
Documentation for distgo is provided in the Go code and as part of the application itself.

* Run `distgo --help` to get an overview of the commands and flags
* distgo is configured using a YML or JSON configuration file. Refer to the documentation in
  `apps/distgo/config/config.go` for information on the configuration parameters that are available.
* Refer to `apps/distgo/config/example_test.go` for sample configuration files

Development
-----------
Use the following commands for development. All paths in the example commands assume that they are run from the root
project directory of godel -- if the current working directory is `apps/distgo`, use `../../godelw` instead.

* Run `./godelw verify` to apply formatting, perform linting checks and run the gödel tests
* Run `./godelw test --tags=distgo` to run the distgo-specific tests (not included by default in the tests run by `./godlew verify`)
* Run `./godelw build` to build the `distgo` binary in `apps/distgo/build`
okgo
====
okgo is a library and CLI for running static linting checks on Go code. okgo performs the following checks:

* [deadcode](https://github.com/tsenart/deadcode)
* [errcheck](https://github.com/kisielk/errcheck)
* [extimport](https://github.com/palantir/checks/tree/develop/extimport)
* [go vet](https://golang.org/cmd/vet/)
* [golint](https://github.com/golang/lint/tree/master/golint)
* [ineffassign](https://github.com/gordonklaus/ineffassign)
* [outparamcheck](https://github.com/palantir/checks/tree/develop/outparamcheck)
* [unconvert](https://github.com/mdempsky/unconvert)
* [varcheck](https://github.com/opennota/check/tree/master/cmd/varcheck)

Documentation
-------------
Documentation for okgo is provided in the Go code and as part of the application itself.

* Run `okgo --help` to get an overview of the commands and flags
* okgo is configured using a YML or JSON configuration file. Refer to the documentation in
  `apps/okgo/config/config.go` for information on the configuration parameters that are available.
* Refer to `apps/okgo/config/example_test.go` for sample configuration files

Development
-----------
Use the following commands for development. All paths in the example commands assume that they are run from the root
project directory of godel -- if the current working directory is `apps/okgo`, use `../../godelw` instead.

* Run `./godelw verify` to apply formatting, perform linting checks and run the gödel tests
* Run `./godelw test --tags=okgo` to run the okgo-specific tests (not included by default in the tests run by `./godlew verify`)
* Run `./godelw build` to build the okgo binary in `apps/okgo/build`

### Add a new check
* In order for a check to be added, it must be a Go program that has a main package
* The checks are managed and packaged by [amalgomate](https://github.com/palantir/amalgomate)
* Add the code required for the new check (the main package and any supporting code) to the vendor directory
* Edit `apps/okgo/checks.yml` and add an entry for the new check
  * Add an entry to `packages` where the key is the name of the check (no whitespace) and the value has a key named
    `main` and the value is the import path to the main package for the formatter. For more details on the config file
    format, refer to the documentation for amalgomate.
* Run `go generate` in the root directory of the project to re-generate the files in `generated_src`
* Add a definition for the check in `ckecks/definition.go`

### Generate
Run `go generate` in the `apps/gonform` directory to create or update the `generated_src` directory and the source files
within it. The `go generate` task for this project requires the amalgomate command to run. The version of amalgomate
used to build the distribution is included as a vendored dependency.
compiles
========

`compiles` verifies that all of the go packages that are part of a project compile properly. This is similar to the
check done by `go build ./...`, but goes further by also verifying that test files (both those that are part of a
package and those that are part of a `_test` package) also compile and build without errors.

Usage
=====
`compiles` uses its current working directory as the project root. If no arguments are provided, it is invoked on all
of the go packages it can find in the current working directory and its subdirectories. If arguments are provided, they
are interpreted as packages relative to the working directory, and only the specified packages will be checked.
outparamcheck
=============

`outparamcheck` is a static code checker for Go based on [errcheck](https://github.com/kisielk/errcheck). It verifies
that functions that take output parameters defined as `interface{}` types are passed pointers to an object rather than
a concrete object.

A canonical example of this is the `json.Unmarshal` function, which has the following definition:

```go
func Unmarshal(data []byte, v interface{}) error
```

As noted in the godoc ("Unmarshal parses the JSON-encoded data and stores the result in the value pointed to by v"), the
`v` must be a pointer so that the results of the operation are available to the caller. However, because `v` is declared
as an `interface{}`, the compiler allows non-pointer values to be passed to the function and the failure is not detected
until runtime.

`outparamcheck` allows these classes of checks to be performed using static analysis. By default, this tool checks the
calls to `encoding/json.Unmarshal`, `encoding/safejson.Unmarshal` and `gopkg.in/yaml.v2.Unmarshal`. It is possible to
use a configuration file to add to the set of functions that are checked.

Install
=======

```
go get -u github.com/palantir/checks/outparamcheck
```

Usage
=====

Run `outparamcheck` with the default checks on all packages within the current directory:

```
./outparamcheck ./...
```

Configuration
=============

Additional checks can be configured using JSON. The JSON can be provided to the check directly as a parameter or by
specifying the path to a file that contains the configuration. The tool accepts a single JSON map where the keys are the
name of the function to be checked and the values are an array that specifies the parameter indices of the "out"
parameter (the parameter that must be a pointer). For example, in order to check that the first (index 0) parameter of
the `github.com/palantir/example/config.Load` function is an output parameter, the JSON would be the following:

```json
{
    "github.com/palantir/example/config.Load": [0]
}
```

The configuration is provided to the tool using the `-config` flag. The value for the flag is treated as a literal JSON
string unless it starts with the `@` character, in which case it is interpreted as the path to a JSON file. The checks
that are specified in the configuration are run in addition to the built-in checks. It is not possible to override or
ignore the built-in checks.

Example invocation configured using JSON directly:

```
./outparamcheck -config '{"github.com/palantir/example/config.Load":[0]}' ./...
```

Example invocation using JSON specified in the file `config.json`:

```
./outparamcheck -config @config.json ./...
```
importalias
===========
`importalias` is a check that verifies that import aliases in a project are used consistently. It verifies that, if a
given package is imported using an alias, then all aliases for that import are consistent across the project.

Usage
-----
`importalias` uses its current working directory as the project root. If no arguments are provided, it is invoked on all
of the go packages it can find in the current working directory and its subdirectories. If arguments are provided, they
are interpreted as packages relative to the working directory, and only the specified packages will be checked.

By default, the output of the check is standard Go check output format. The program operates as follows:

* Finds all imports and all aliases that are used for imports.
* If a package is imported using multiple different aliases, the alias that is most commonly used to import the package
  is considered the "correct" import.
  * If there is a tie for the most commonly used alias, it is assumed that there is no consensus for the alias.
* Any line that imports a package using an alias that is not the most common one (or an alias for which there is no
  consensus) is treated as an error. The file and line number is printed, along with a suggestion for how the alias
  should be renamed.

The `-v` or `--verbose` flag can be used to print an overview of all of the imports in the project that are imported
using multiple aliases. The output is organized by import and lists all of the aliases used for the import (in order of
most commonly used) and the files and locations in the files in which the imports occur.
extimport
=========

`extimport` is a program that verifies that there are no imports that reference external packages in a go project. If
external package imports are found, the program prints them and exits with an exit code of 1. An exit code of 0
indicates that there are no external package imports in the project, which means that it should be possible to build the
project in a default `$GOPATH`.

A package is considered external if it is not in the standard Go library and not resolvable within the project
directory itself (the package is not in the project or vendored in the project). An import is considered to be directly
external if it imports an external package. An import is considered transitively external if the imported package itself
is not external, but one of its dependent packages is external.

Given a package, `extimports` checks the imports of all of the go files and go test files in that package. However, when
checking transitive external package dependencies, only non-test go files are considered (that is, the check will not
fail if a test file of an imported package has an external dependency).

Usage
=====
`extimport` uses its current working directory as the project root. If no arguments are provided, it is invoked on all
of the go packages it can find in the current working directory and its subdirectories. If arguments are provided, they
are interpreted as packages relative to the working directory, and only the specified packages will be checked.
novendor
========

`novendor` is a program that verifies that there are no unused vendored imports in a Go project. If unused vendored
packages are found, the program prints them and exits with a non-0 exit code. An exit code of 0 indicates that there are
no unused vendored packages in the project given the parameters that were provided to the program.

A vendored package is considered unused if the package is not imported by any of the non-vendored code in the project
(including test code) either directly or transitively. It should be possible to remove any package that is reported by
this tool from vendoring and still have the project build correctly. Standard Go build rules are used to determine if a
package is vendored (basically, any package that is within a "vendor" directory is vendored).

Project Packages
================
`novendor` has a notion of "project packages". A "project package" is considered to be a top-level package for a single
project that may contain many subpackages. Although this is not an official Go concept, it captures much of how code is
organized in practice. A "project package" is considered to be the 3rd level of a package import (if the import path has
fewer than 3 parts, then all of it is considered). For example, the "project package" of
`github.com/palantir/stacktrace/cleanpath` is `github.palantir.com/palantir/stacktrace`, while the "project package" of
`gopkg.in/yaml.v2` is `gopkg.in/yaml.v2`. This scheme is not perfect -- for example, if a package named
`gopkg.in/yaml.v2/subpackage` exists, its "project package" would be `gopkg.in/yaml.v2/subpackage`, even though
conceptually `gopkg.in/yaml.v2` would probably be more appropriate. However, in practice the 3-level heuristic works for
most packages

This concept is used because in many cases projects want to vendor "project packages" as a unit. For example, consider
the packages `github.com/org/project`, `github.com/org/project/api` and `github.com/org/project/impl`. If the primary
project code only imports `github.com/org/project/api`, then technically the other 2 packages are "unused". However, a
project may still want to vendor `github.com/org/project` and all of its subdirectories because they may want to make
use of the other code later or ensure that different subdirectories of a single project are not inadvertently vendored
at different versions.

The default behavior of `novendor` works at the "project package" granularity. So, if `github.com/org/project/api` and
`github.com/org/project/impl` are both vendored but only `github.com/org/project/api` is used, `github.com/org/project`
is considered as "used" and is not reported as an unused project package. If both are unused, the default behavior will
report that `github.com/org/project` is unused.

Use the `--project-package=false` flag to turn off the "project package" behavior (this will cause all used/unused
determination and output to be done purely at the Go package level).

Usage
=====
`novendor` takes the path to the packages that are part of the project for which vendoring status should be determined.
For example, if a project consists of a top-level package and a `cmd` package, `novendor` would be run at the project
root as:

```bash
novendor . ./cmd
```

Note that, as shown above, all packages that are part of a project should be provided as arguments (if no arguments are
provided, all non-vendored packages that are found in the working directory are used).

Usage of `novendor`:

```
  -f    Include full path of unused packages (default omits path to vendor directory)
  --project-package
        Use the 'project' paradigm to interpret packages and only output projects that are unused (default true)
```

Examples
========

```bash
> novendor .
github.com/docker/go-connections
gopkg.in/mcuadros/go-syslog.v2
```

```bash
> novendor -f .
github.palantir.build/deployability/novendor/vendor/github.com/docker/go-connections
github.palantir.build/deployability/novendor/vendor/gopkg.in/mcuadros/go-syslog.v2
```

```bash
> novendor --project-package=false .
github.com/docker/docker/pkg/longpath
github.com/docker/go-connections/nat
github.com/docker/go-connections/sockets
github.com/docker/go-connections/tlsconfig
gopkg.in/mcuadros/go-syslog.v2
gopkg.in/mcuadros/go-syslog.v2/example
gopkg.in/mcuadros/go-syslog.v2/format
```

```bash
> novendor -f --project-package=false .
github.palantir.build/deployability/novendor/vendor/github.com/docker/docker/pkg/longpath
github.palantir.build/deployability/novendor/vendor/github.com/docker/go-connections/nat
github.palantir.build/deployability/novendor/vendor/github.com/docker/go-connections/sockets
github.palantir.build/deployability/novendor/vendor/github.com/docker/go-connections/tlsconfig
github.palantir.build/deployability/novendor/vendor/gopkg.in/mcuadros/go-syslog.v2
github.palantir.build/deployability/novendor/vendor/gopkg.in/mcuadros/go-syslog.v2/example
github.palantir.build/deployability/novendor/vendor/gopkg.in/mcuadros/go-syslog.v2/format
```
nobadfuncs
==========
`nobadfuncs` verifies that a set of specified functions are not referenced in the packages being checked. It can be used
to blacklist specific functions that should not typically be referenced or called. It is possible to explicitly allow
uses of black-listed functions by adding a comment to the line before the calling line.

Usage
-----
`nobadfuncs` takes the path to the packages that should be checked for function calls. It also takes configuration (as
JSON) that specifies the blacklisted functions.

The function signatures that are blacklisted are full function signatures consisting of the fully qualified package name
or receiver, name, parameter types and return types. Examples:

```
func (*net/http.Client).Do(*net/http.Request) (*net/http.Response, error)
func fmt.Println(...interface{}) (int, error)
```

`nobadfuncs` can be run with the `--all` flag to print all of the function references in the provided packages. The output
can be used as the basis for determining the signatures for blacklist functions.

Examples
========

```bash
> nobadfuncs --all .
/Volumes/.../src/github.com/palantir/checks/nobadfuncs/nobadfuncs.go:54:13: func github.com/palantir/pkg/cli.NewApp(...github.com/palantir/pkg/cli.Option) *github.com/palantir/pkg/cli.App
/Volumes/.../src/github.com/palantir/checks/nobadfuncs/nobadfuncs.go:54:24: func github.com/palantir/pkg/cli.DebugHandler(github.com/palantir/pkg/cli.ErrorStringer) github.com/palantir/pkg/cli.Option
```

```bash
> nobadfuncs --config '{"func os.Exit(int)": "do not call os.Exit directly"}' .
/Volumes/.../src/github.com/palantir/checks/nobadfuncs/nobadfuncs.go:85:5: do not call os.Exit directly
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
pkg
===
A collection of Go packages. Refer to the Go documentation of the individual packages for details.
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
* [nehm](https://github.com/bogem/nehm)
* [Pouch](https://github.com/alibaba/pouch)

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
  cmd.Execute()
}
```

## Using the Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

[Here](https://github.com/spf13/cobra/blob/master/cobra/README.md) you can find more information about it.

## Using the Cobra Library

To manually implement Cobra you need to create a bare main.go file and a rootCmd file.
You will optionally provide additional commands as you see fit.

### Create rootCmd

Cobra doesn't require any special constructors. Simply create your commands.

Ideally you place this in app/cmd/root.go:

```go
var rootCmd = &cobra.Command{
  Use:   "hugo",
  Short: "Hugo is a very fast static site generator",
  Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
  Run: func(cmd *cobra.Command, args []string) {
    // Do Stuff Here
  },
}

func Execute() {
  if err := rootCmd.Execute(); err != nil {
    fmt.Println(err)
    os.Exit(1)
  }
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
  rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.cobra.yaml)")
  rootCmd.PersistentFlags().StringVarP(&projectBase, "projectbase", "b", "", "base project directory eg. github.com/spf13/")
  rootCmd.PersistentFlags().StringP("author", "a", "YOUR NAME", "Author name for copyright attribution")
  rootCmd.PersistentFlags().StringVarP(&userLicense, "license", "l", "", "Name of license for the project (can provide `licensetext` in config)")
  rootCmd.PersistentFlags().Bool("viper", true, "Use Viper for configuration")
  viper.BindPFlag("author", rootCmd.PersistentFlags().Lookup("author"))
  viper.BindPFlag("projectbase", rootCmd.PersistentFlags().Lookup("projectbase"))
  viper.BindPFlag("useViper", rootCmd.PersistentFlags().Lookup("viper"))
  viper.SetDefault("author", "NAME HERE <EMAIL ADDRESS>")
  viper.SetDefault("license", "apache")
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
  cmd.Execute()
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
  "fmt"

  "github.com/spf13/cobra"
)

func init() {
  rootCmd.AddCommand(versionCmd)
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
rootCmd.PersistentFlags().BoolVarP(&Verbose, "verbose", "v", false, "verbose output")
```

### Local Flags

A flag can also be assigned locally which will only apply to that specific command.

```go
rootCmd.Flags().StringVarP(&Source, "source", "s", "", "Source directory to read from")
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
  rootCmd.PersistentFlags().StringVar(&author, "author", "YOUR NAME", "Author name for copyright attribution")
  viper.BindPFlag("author", rootCmd.PersistentFlags().Lookup("author"))
}
```

In this example the persistent flag `author` is bound with `viper`.
**Note**, that the variable `author` will not be set to the value from config,
when the `--author` flag is not provided by user.

More in [viper documentation](https://github.com/spf13/viper#working-with-flags).

### Required flags

Flags are optional by default. If instead you wish your command to report an error
when a flag has not been set, mark it as required:
```go
rootCmd.Flags().StringVarP(&Region, "region", "r", "", "AWS region (required)")
rootCmd.MarkFlagRequired("region")
```

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
with following functions:

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

## Version Flag

Cobra adds a top-level '--version' flag if the Version field is set on the root command.
Running an application with the '--version' flag will print the version to stdout using
the version template. The template can be customized using the
`cmd.SetVersionTemplate(s string)` function.

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
