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

murmur3
=======

[![Build Status](https://travis-ci.org/spaolacci/murmur3.svg?branch=master)](https://travis-ci.org/spaolacci/murmur3)

Native Go implementation of Austin Appleby's third MurmurHash revision (aka
MurmurHash3).

Reference algorithm has been slightly hacked as to support the streaming mode
required by Go's standard [Hash interface](http://golang.org/pkg/hash/#Hash).


Benchmarks
----------

Go tip as of 2014-06-12 (i.e almost go1.3), core i7 @ 3.4 Ghz. All runs
include hasher instantiation and sequence finalization.

<pre>

Benchmark32_1        500000000     7.69 ns/op      130.00 MB/s
Benchmark32_2        200000000     8.83 ns/op      226.42 MB/s
Benchmark32_4        500000000     7.99 ns/op      500.39 MB/s
Benchmark32_8        200000000     9.47 ns/op      844.69 MB/s
Benchmark32_16       100000000     12.1 ns/op     1321.61 MB/s
Benchmark32_32       100000000     18.3 ns/op     1743.93 MB/s
Benchmark32_64        50000000     30.9 ns/op     2071.64 MB/s
Benchmark32_128       50000000     57.6 ns/op     2222.96 MB/s
Benchmark32_256       20000000      116 ns/op     2188.60 MB/s
Benchmark32_512       10000000      226 ns/op     2260.59 MB/s
Benchmark32_1024       5000000      452 ns/op     2263.73 MB/s
Benchmark32_2048       2000000      891 ns/op     2296.02 MB/s
Benchmark32_4096       1000000     1787 ns/op     2290.92 MB/s
Benchmark32_8192        500000     3593 ns/op     2279.68 MB/s
Benchmark128_1       100000000     26.1 ns/op       38.33 MB/s
Benchmark128_2       100000000     29.0 ns/op       69.07 MB/s
Benchmark128_4        50000000     29.8 ns/op      134.17 MB/s
Benchmark128_8        50000000     31.6 ns/op      252.86 MB/s
Benchmark128_16      100000000     26.5 ns/op      603.42 MB/s
Benchmark128_32      100000000     28.6 ns/op     1117.15 MB/s
Benchmark128_64       50000000     35.5 ns/op     1800.97 MB/s
Benchmark128_128      50000000     50.9 ns/op     2515.50 MB/s
Benchmark128_256      20000000     76.9 ns/op     3330.11 MB/s
Benchmark128_512      20000000      135 ns/op     3769.09 MB/s
Benchmark128_1024     10000000      250 ns/op     4094.38 MB/s
Benchmark128_2048      5000000      477 ns/op     4290.75 MB/s
Benchmark128_4096      2000000      940 ns/op     4353.29 MB/s
Benchmark128_8192      1000000     1838 ns/op     4455.47 MB/s

</pre>


<pre>

benchmark              Go1.0 MB/s    Go1.1 MB/s  speedup    Go1.2 MB/s  speedup    Go1.3 MB/s  speedup
Benchmark32_1               98.90        118.59    1.20x        114.79    0.97x        130.00    1.13x
Benchmark32_2              168.04        213.31    1.27x        210.65    0.99x        226.42    1.07x
Benchmark32_4              414.01        494.19    1.19x        490.29    0.99x        500.39    1.02x
Benchmark32_8              662.19        836.09    1.26x        836.46    1.00x        844.69    1.01x
Benchmark32_16             917.46       1304.62    1.42x       1297.63    0.99x       1321.61    1.02x
Benchmark32_32            1141.93       1737.54    1.52x       1728.24    0.99x       1743.93    1.01x
Benchmark32_64            1289.47       2039.51    1.58x       2038.20    1.00x       2071.64    1.02x
Benchmark32_128           1299.23       2097.63    1.61x       2177.13    1.04x       2222.96    1.02x
Benchmark32_256           1369.90       2202.34    1.61x       2213.15    1.00x       2188.60    0.99x
Benchmark32_512           1399.56       2255.72    1.61x       2264.49    1.00x       2260.59    1.00x
Benchmark32_1024          1410.90       2285.82    1.62x       2270.99    0.99x       2263.73    1.00x
Benchmark32_2048          1422.14       2297.62    1.62x       2269.59    0.99x       2296.02    1.01x
Benchmark32_4096          1420.53       2307.81    1.62x       2273.43    0.99x       2290.92    1.01x
Benchmark32_8192          1424.79       2312.87    1.62x       2286.07    0.99x       2279.68    1.00x
Benchmark128_1               8.32         30.15    3.62x         30.84    1.02x         38.33    1.24x
Benchmark128_2              16.38         59.72    3.65x         59.37    0.99x         69.07    1.16x
Benchmark128_4              32.26        112.96    3.50x        114.24    1.01x        134.17    1.17x
Benchmark128_8              62.68        217.88    3.48x        218.18    1.00x        252.86    1.16x
Benchmark128_16            128.47        451.57    3.51x        474.65    1.05x        603.42    1.27x
Benchmark128_32            246.18        910.42    3.70x        871.06    0.96x       1117.15    1.28x
Benchmark128_64            449.05       1477.64    3.29x       1449.24    0.98x       1800.97    1.24x
Benchmark128_128           762.61       2222.42    2.91x       2217.30    1.00x       2515.50    1.13x
Benchmark128_256          1179.92       3005.46    2.55x       2931.55    0.98x       3330.11    1.14x
Benchmark128_512          1616.51       3590.75    2.22x       3592.08    1.00x       3769.09    1.05x
Benchmark128_1024         1964.36       3979.67    2.03x       4034.01    1.01x       4094.38    1.01x
Benchmark128_2048         2225.07       4156.93    1.87x       4244.17    1.02x       4290.75    1.01x
Benchmark128_4096         2360.15       4299.09    1.82x       4392.35    1.02x       4353.29    0.99x
Benchmark128_8192         2411.50       4356.84    1.81x       4480.68    1.03x       4455.47    0.99x

</pre>

![Gomega: Ginkgo's Preferred Matcher Library](http://onsi.github.io/gomega/images/gomega.png)

[![Build Status](https://travis-ci.org/onsi/gomega.svg)](https://travis-ci.org/onsi/gomega)

Jump straight to the [docs](http://onsi.github.io/gomega/) to learn about Gomega, including a list of [all available matchers](http://onsi.github.io/gomega/#provided-matchers).

If you have a question, comment, bug report, feature request, etc. please open a GitHub issue.

## [Ginkgo](http://github.com/onsi/ginkgo): a BDD Testing Framework for Golang

Learn more about Ginkgo [here](http://onsi.github.io/ginkgo/)

## Community Matchers

A collection of community matchers is available on the [wiki](https://github.com/onsi/gomega/wiki).

## License

Gomega is MIT-Licensed

The `ConsistOf` matcher uses [goraph](https://github.com/amitkgupta/goraph) which is embedded in the source to simplify distribution.  goraph has an MIT license.
![Ginkgo: A Go BDD Testing Framework](http://onsi.github.io/ginkgo/images/ginkgo.png)

[![Build Status](https://travis-ci.org/onsi/ginkgo.svg)](https://travis-ci.org/onsi/ginkgo)

Jump to the [docs](http://onsi.github.io/ginkgo/) to learn more.  To start rolling your Ginkgo tests *now* [keep reading](#set-me-up)!

If you have a question, comment, bug report, feature request, etc. please open a GitHub issue.

## Feature List

- Ginkgo uses Go's `testing` package and can live alongside your existing `testing` tests.  It's easy to [bootstrap](http://onsi.github.io/ginkgo/#bootstrapping-a-suite) and start writing your [first tests](http://onsi.github.io/ginkgo/#adding-specs-to-a-suite)

- Structure your BDD-style tests expressively:
    - Nestable [`Describe`, `Context` and `When` container blocks](http://onsi.github.io/ginkgo/#organizing-specs-with-containers-describe-and-context)
    - [`BeforeEach` and `AfterEach` blocks](http://onsi.github.io/ginkgo/#extracting-common-setup-beforeeach) for setup and teardown
    - [`It` and `Specify` blocks](http://onsi.github.io/ginkgo/#individual-specs-) that hold your assertions
    - [`JustBeforeEach` blocks](http://onsi.github.io/ginkgo/#separating-creation-and-configuration-justbeforeeach) that separate creation from configuration (also known as the subject action pattern).
    - [`BeforeSuite` and `AfterSuite` blocks](http://onsi.github.io/ginkgo/#global-setup-and-teardown-beforesuite-and-aftersuite) to prep for and cleanup after a suite.

- A comprehensive test runner that lets you:
    - Mark specs as [pending](http://onsi.github.io/ginkgo/#pending-specs)
    - [Focus](http://onsi.github.io/ginkgo/#focused-specs) individual specs, and groups of specs, either programmatically or on the command line
    - Run your tests in [random order](http://onsi.github.io/ginkgo/#spec-permutation), and then reuse random seeds to replicate the same order.
    - Break up your test suite into parallel processes for straightforward [test parallelization](http://onsi.github.io/ginkgo/#parallel-specs)

- `ginkgo`: a command line interface with plenty of handy command line arguments for [running your tests](http://onsi.github.io/ginkgo/#running-tests) and [generating](http://onsi.github.io/ginkgo/#generators) test files.  Here are a few choice examples:
    - `ginkgo -nodes=N` runs your tests in `N` parallel processes and print out coherent output in realtime
    - `ginkgo -cover` runs your tests using Go's code coverage tool
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

- [Completions for VSCode](https://github.com/onsi/vscode-ginkgo): just use VSCode's extension installer to install `vscode-ginkgo`.

- Straightforward support for third-party testing libraries such as [Gomock](https://code.google.com/p/gomock/) and [Testify](https://github.com/stretchr/testify).  Check out the [docs](http://onsi.github.io/ginkgo/#third-party-integrations) for details.

- A modular architecture that lets you easily:
    - Write [custom reporters](http://onsi.github.io/ginkgo/#writing-custom-reporters) (for example, Ginkgo comes with a [JUnit XML reporter](http://onsi.github.io/ginkgo/#generating-junit-xml-output) and a TeamCity reporter).
    - [Adapt an existing matcher library (or write your own!)](http://onsi.github.io/ginkgo/#using-other-matcher-libraries) to work with Ginkgo

## [Gomega](http://github.com/onsi/gomega): Ginkgo's Preferred Matcher Library

Ginkgo is best paired with Gomega.  Learn more about Gomega [here](http://onsi.github.io/gomega/)

## [Agouti](http://github.com/sclevine/agouti): A Go Acceptance Testing Framework

Agouti allows you run WebDriver integration tests.  Learn more about Agouti [here](http://agouti.org)

## Set Me Up!

You'll need the Go command-line tools. Ginkgo is tested with Go 1.6+, but preferably you should get the latest. Follow the [installation instructions](https://golang.org/doc/install) if you don't have it installed.

```bash

go get -u github.com/onsi/ginkgo/ginkgo  # installs the ginkgo CLI
go get -u github.com/onsi/gomega/...     # fetches the matcher library

cd path/to/package/you/want/to/test

ginkgo bootstrap # set up a new ginkgo suite
ginkgo generate  # will create a sample test file.  edit this file and add your tests then...

go test # to run your tests

ginkgo  # also runs your tests

```

## I'm new to Go: What are my testing options?

Of course, I heartily recommend [Ginkgo](https://github.com/onsi/ginkgo) and [Gomega](https://github.com/onsi/gomega).  Both packages are seeing heavy, daily, production use on a number of projects and boast a mature and comprehensive feature-set.

With that said, it's great to know what your options are :)

### What Go gives you out of the box

Testing is a first class citizen in Go, however Go's built-in testing primitives are somewhat limited: The [testing](http://golang.org/pkg/testing) package provides basic XUnit style tests and no assertion library.

### Matcher libraries for Go's XUnit style tests

A number of matcher libraries have been written to augment Go's built-in XUnit style tests.  Here are two that have gained traction:

- [testify](https://github.com/stretchr/testify)
- [gocheck](http://labix.org/gocheck)

You can also use Ginkgo's matcher library [Gomega](https://github.com/onsi/gomega) in [XUnit style tests](http://onsi.github.io/gomega/#using-gomega-with-golangs-xunitstyle-tests)

### BDD style testing frameworks

There are a handful of BDD-style testing frameworks written for Go.  Here are a few:

- [Ginkgo](https://github.com/onsi/ginkgo) ;)
- [GoConvey](https://github.com/smartystreets/goconvey) 
- [Goblin](https://github.com/franela/goblin)
- [Mao](https://github.com/azer/mao)
- [Zen](https://github.com/pranavraja/zen)

Finally, @shageman has [put together](https://github.com/shageman/gotestit) a comprehensive comparison of Go testing libraries.

Go explore!

## License

Ginkgo is MIT-Licensed

## Contributing

Since Ginkgo tests also internal packages, when you fork, you'll have to replace imports with your repository.<br />
Use `before_pr.sh` for that<br />
After you finished your changes and before you push your pull request, use `after_pr.sh` to revert those changes
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
