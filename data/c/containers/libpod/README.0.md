This repo is still in the experimental stage. Shortly it will contain the schema of the API that are served by the Kubernetes apiserver.
# apimachinery

Scheme, typing, encoding, decoding, and conversion packages for Kubernetes and Kubernetes-like API objects.


## Purpose

This library is a shared dependency for servers and clients to work with Kubernetes API infrastructure without direct 
type dependencies.  Its first consumers are `k8s.io/kubernetes`, `k8s.io/client-go`, and `k8s.io/apiserver`.


## Compatibility

There are *NO compatibility guarantees* for this repository.  It is in direct support of Kubernetes, so branches
will track Kubernetes and be compatible with that repo.  As we more cleanly separate the layers, we will review the
compatibility guarantee.


## Where does it come from?

`apimachinery` is synced from https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery.
Code changes are made in that location, merged into `k8s.io/kubernetes` and later synced here.


## Things you should *NOT* do

 1. Add API types to this repo.  This is for the machinery, not for the types.
 2. Directly modify any files under `pkg` in this repo.  Those are driven from `k8s.io/kubernetes/staging/src/k8s.io/apimachinery`.
 3. Expect compatibility.  This repo is direct support of Kubernetes and the API isn't yet stable enough for API guarantees.
# client-go

Go clients for talking to a [kubernetes](http://kubernetes.io/) cluster.

We currently recommend using the v6.0.0 tag. See [INSTALL.md](/INSTALL.md) for
detailed installation instructions. `go get k8s.io/client-go/...` works, but
will give you head and doesn't handle the dependencies well.

[![BuildStatus Widget]][BuildStatus Result]
[![GoReport Widget]][GoReport Status]
[![GoDocWidget]][GoDocReference]

[BuildStatus Result]: https://travis-ci.org/kubernetes/client-go
[BuildStatus Widget]: https://travis-ci.org/kubernetes/client-go.svg?branch=master

[GoReport Status]: https://goreportcard.com/report/github.com/kubernetes/client-go
[GoReport Widget]: https://goreportcard.com/badge/github.com/kubernetes/client-go

[GoDocWidget]: https://godoc.org/k8s.io/client-go?status.svg
[GoDocReference]:https://godoc.org/k8s.io/client-go 

## Table of Contents

- [What's included](#whats-included)
- [Versioning](#versioning)
  - [Compatibility: your code <-> client-go](#compatibility-your-code---client-go)
  - [Compatibility: client-go <-> Kubernetes clusters](#compatibility-client-go---kubernetes-clusters)
  - [Compatibility matrix](#compatibility-matrix)
  - [Why do the 1.4 and 1.5 branch contain top-level folder named after the version?](#why-do-the-14-and-15-branch-contain-top-level-folder-named-after-the-version)
- [Kubernetes tags](#kubernetes-tags)
- [How to get it](#how-to-get-it)
- [How to use it](#how-to-use-it)
- [Dependency management](#dependency-management)
- [Contributing code](#contributing-code)

### What's included

* The `kubernetes` package contains the clientset to access Kubernetes API.
* The `discovery` package is used to discover APIs supported by a Kubernetes API server.
* The `dynamic` package contains a dynamic client that can perform generic operations on arbitrary Kubernetes API objects.
* The `transport` package is used to set up auth and start a connection.
* The `tools/cache` package is useful for writing controllers.

### Versioning

`client-go` follows [semver](http://semver.org/). We will not make
backwards-incompatible changes without incrementing the major version number. A
change is backwards-incompatible either if it *i)* changes the public interfaces
of `client-go`, or *ii)* makes `client-go` incompatible with otherwise supported
versions of Kubernetes clusters.

Changes that add features in a backwards-compatible way will result in bumping
the minor version (second digit) number.

Bugfixes will result in the patch version (third digit) changing. PRs that are
cherry-picked into an older Kubernetes release branch will result in an update
to the corresponding branch in `client-go`, with a corresponding new tag
changing the patch version.

A consequence of this is that `client-go` version numbers will be unrelated to
Kubernetes version numbers.

#### Branches and tags.

We will create a new branch and tag for each increment in the major version number or
minor version number. We will create only a new tag for each increment in the patch
version number. See [semver](http://semver.org/) for definitions of major,
minor, and patch.

The master branch will track HEAD in the main Kubernetes repo and
accumulate changes. Consider HEAD to have the version `x.(y+1).0-alpha` or
`(x+1).0.0-alpha` (depending on whether it has accumulated a breaking change or
not), where `x` and `y` are the current major and minor versions.

#### Compatibility: your code <-> client-go

`client-go` follows [semver](http://semver.org/), so until the major version of
client-go gets increased, your code will compile and will continue to work with
explicitly supported versions of Kubernetes clusters. You must use a dependency
management system and pin a specific major version of `client-go` to get this
benefit, as HEAD follows the upstream Kubernetes repo.

#### Compatibility: client-go <-> Kubernetes clusters

Since Kubernetes is backwards compatible with clients, older `client-go`
versions will work with many different Kubernetes cluster versions.

We will backport bugfixes--but not new features--into older versions of
`client-go`.


#### Compatibility matrix

|                     | Kubernetes 1.4 | Kubernetes 1.5 | Kubernetes 1.6 | Kubernetes 1.7 | Kubernetes 1.8 | Kubernetes 1.9 |
|---------------------|----------------|----------------|----------------|----------------|----------------|----------------|
| client-go 1.4       | ✓              | -              | -              | -              | -              | -              |
| client-go 1.5       | +              | -              | -              | -              | -              | -              |
| client-go 2.0       | +-             | ✓              | +-             | +-             | +-             | +-             |
| client-go 3.0       | +-             | +-             | ✓              | -              | +-             | +-             |
| client-go 4.0       | +-             | +-             | +-             | ✓              | +-             | +-             |
| client-go 5.0       | +-             | +-             | +-             | +-             | ✓              | +-             |
| client-go 6.0       | +-             | +-             | +-             | +-             | +-             | ✓              |
| client-go HEAD      | +-             | +-             | +-             | +-             | +-             | +              |

Key:

* `✓` Exactly the same features / API objects in both client-go and the Kubernetes
  version.
* `+` client-go has features or API objects that may not be present in the
  Kubernetes cluster, either due to that client-go has additional new API, or
  that the server has removed old API. However, everything they have in
  common (i.e., most APIs) will work. Please note that alpha APIs may vanish or
  change significantly in a single release.
* `-` The Kubernetes cluster has features the client-go library can't use,
  either due to the server has additional new API, or that client-go has
  removed old API. However, everything they share in common (i.e., most APIs)
  will work.

See the [CHANGELOG](./CHANGELOG.md) for a detailed description of changes
between client-go versions.

| Branch         | Canonical source code location       | Maintenance status            |
|----------------|--------------------------------------|-------------------------------|
| client-go 1.4  | Kubernetes main repo, 1.4 branch     | = -                           |
| client-go 1.5  | Kubernetes main repo, 1.5 branch     | = -                           |
| client-go 2.0  | Kubernetes main repo, 1.5 branch     | = -                           |
| client-go 3.0  | Kubernetes main repo, 1.6 branch     | = -                           |
| client-go 4.0  | Kubernetes main repo, 1.7 branch     | ✓                             |
| client-go 5.0  | Kubernetes main repo, 1.8 branch     | ✓                             |
| client-go 6.0  | Kubernetes main repo, 1.9 branch     | ✓                             |
| client-go HEAD | Kubernetes main repo, master branch  | ✓                             |

Key:

* `✓` Changes in main Kubernetes repo are actively published to client-go by a bot
* `=` Maintenance is manual, only severe security bugs will be patched.
* `-` Deprecated; please upgrade.

#### Deprecation policy

We will maintain branches for at least six months after their first stable tag
is cut. (E.g., the clock for the release-2.0 branch started ticking when we
tagged v2.0.0, not when we made the first alpha.) This policy applies to
every version greater than or equal to 2.0.

#### Why do the 1.4 and 1.5 branch contain top-level folder named after the version?

For the initial release of client-go, we thought it would be easiest to keep
separate directories for each minor version. That soon proved to be a mistake.
We are keeping the top-level folders in the 1.4 and 1.5 branches so that
existing users won't be broken.

### Kubernetes tags

As of October 2017, client-go is still a mirror of
[k8s.io/kubernetes/staging/src/client-go](https://github.com/kubernetes/kubernetes/tree/master/staging/src/k8s.io/client-go),
the code development is still done in the staging area. Since Kubernetes 1.8
release, when syncing the code from the staging area, we also sync the Kubernetes
version tags to client-go, prefixed with "kubernetes-". For example, if you check
out the `kubernetes-v1.8.0` tag in client-go, the code you get is exactly the
same as if you check out the `v1.8.0` tag in kubernetes, and change directory to
`staging/src/k8s.io/client-go`. The purpose is to let users quickly find matching
commits among published repos, like
[sample-apiserver](https://github.com/kubernetes/sample-apiserver),
[apiextension-apiserver](https://github.com/kubernetes/apiextensions-apiserver),
etc. The Kubernetes version tag does NOT claim any backwards compatibility
guarantees for client-go. Please check the [semantic versions](#versioning) if
you care about backwards compatibility.

### How to get it

You can use `go get k8s.io/client-go/...` to get client-go, but **you will get
the unstable master branch** and `client-go`'s vendored dependencies will not be
added to your `$GOPATH`. So we think most users will want to use a dependency
management system. See [INSTALL.md](/INSTALL.md) for detailed instructions.

### How to use it

If your application runs in a Pod in the cluster, please refer to the
in-cluster [example](examples/in-cluster-client-configuration), otherwise please
refer to the out-of-cluster [example](examples/out-of-cluster-client-configuration).

### Dependency management

If your application depends on a package that client-go depends on, and you let the Go compiler find the dependency in `GOPATH`, you will end up with duplicated dependencies: one copy from the `GOPATH`, and one from the vendor folder of client-go. This will cause unexpected runtime error like flag redefinition, since the go compiler ends up importing both packages separately, even if they are exactly the same thing. If this happens, you can either
* run `godep restore` ([godep](https://github.com/tools/godep)) in the client-go/ folder, then remove the vendor folder of client-go. Then the packages in your GOPATH will be the only copy
* or run `godep save` in your application folder to flatten all dependencies.

### Contributing code
Please send pull requests against the client packages in the Kubernetes main [repository](https://github.com/kubernetes/kubernetes). Changes in the staging area will be published to this repository every day.
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

where `x.x.x` must correspond to a directory in https://www.unicode.org/Public/.
If this version is newer than the version in core it will also update the
relevant packages there. The idna package in x/net will always be updated.

To update a CLDR version run

    CLDR_VERSION=version go generate

where `version` must correspond to a directory in
https://www.unicode.org/Public/cldr/.

Note that the code gets adapted over time to changes in the data and that
backwards compatibility is not maintained.
So updating to a different version may not work.

The files in DATA/{iana|icu|w3|whatwg} are currently not versioned.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the image repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/text:" in the
subject line, so it is easy to find.
# Go Sync

This repository provides Go concurrency primitives in addition to the
ones provided by the language and "sync" and "sync/atomic" packages.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/sync`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/sync`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the sync repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/sync:" in the
subject line, so it is easy to find.
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

### Old Build System (currently for `GOOS != "linux"`)

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

### New Build System (currently for `GOOS == "linux"`)

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
# Go Cryptography

This repository holds supplementary Go cryptography libraries.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/crypto/...`. You
can also manually git clone the repository to `$GOPATH/src/golang.org/x/crypto`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the crypto repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/crypto:" in the
subject line, so it is easy to find.

Note that contributions to the cryptography package receive additional scrutiny
due to their sensitive nature. Patches may take longer than normal to receive
feedback.
# Go Networking

This repository holds supplementary Go networking libraries.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/net`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/net`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit
changes to this repository, see https://golang.org/doc/contribute.html.
The main issue tracker for the net repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/net:" in the
subject line, so it is easy to find.
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
# Go Time

This repository provides supplementary Go time packages.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/time`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/time`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the time repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/time:" in the
subject line, so it is easy to find.
The MongoDB driver for Go
-------------------------

Please go to [http://labix.org/mgo](http://labix.org/mgo) for all project details.
# Terminal progress bar for Go  

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
First  34 / 200 [=========>---------------------------------------------]  17.00% 00m08s
Second  42 / 200 [===========>------------------------------------------]  21.00% 00m06s
Third  36 / 200 [=========>---------------------------------------------]  18.00% 00m08s
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
Gotty is a library written in Go that determines and reads termcap database
files to produce an interface for interacting with the capabilities of a
terminal.
See the godoc documentation or the source code for more information about
function usage.
# go-patricia #

**Documentation**: [GoDoc](http://godoc.org/github.com/tchap/go-patricia/patricia)<br />
**Build Status**: [![Build
Status](https://drone.io/github.com/tchap/go-patricia/status.png)](https://drone.io/github.com/tchap/go-patricia/latest)<br />
**Test Coverage**: [![Coverage
Status](https://coveralls.io/repos/tchap/go-patricia/badge.png)](https://coveralls.io/r/tchap/go-patricia)

## About ##

A generic patricia trie (also called radix tree) implemented in Go (Golang).

The patricia trie as implemented in this library enables fast visiting of items
in some particular ways:

1. visit all items saved in the tree,
2. visit all items matching particular prefix (visit subtree), or
3. given a string, visit all items matching some prefix of that string.

`[]byte` type is used for keys, `interface{}` for values.

`Trie` is not thread safe. Synchronize the access yourself.

### State of the Project ###

Apparently some people are using this, so the API should not change often.
Any ideas on how to make the library better are still welcome.

More (unit) testing would be cool as well...

## Usage ##

Import the package from GitHub first.

```go
import "github.com/tchap/go-patricia/patricia"
```

You can as well use gopkg.in thingie:

```go
import "gopkg.in/tchap/go-patricia.v2/patricia"
```

Then you can start having fun.

```go
printItem := func(prefix patricia.Prefix, item patricia.Item) error {
	fmt.Printf("%q: %v\n", prefix, item)
	return nil
}

// Create a new default trie (using the default parameter values).
trie := NewTrie()

// Create a new custom trie.
trie := NewTrie(MaxPrefixPerNode(16), MaxChildrenPerSparseNode(10))

// Insert some items.
trie.Insert(Prefix("Pepa Novak"), 1)
trie.Insert(Prefix("Pepa Sindelar"), 2)
trie.Insert(Prefix("Karel Macha"), 3)
trie.Insert(Prefix("Karel Hynek Macha"), 4)

// Just check if some things are present in the tree.
key := Prefix("Pepa Novak")
fmt.Printf("%q present? %v\n", key, trie.Match(key))
// "Pepa Novak" present? true
key = Prefix("Karel")
fmt.Printf("Anybody called %q here? %v\n", key, trie.MatchSubtree(key))
// Anybody called "Karel" here? true

// Walk the tree in alphabetical order.
trie.Visit(printItem)
// "Karel Hynek Macha": 4
// "Karel Macha": 3
// "Pepa Novak": 1
// "Pepa Sindelar": 2

// Walk a subtree.
trie.VisitSubtree(Prefix("Pepa"), printItem)
// "Pepa Novak": 1
// "Pepa Sindelar": 2

// Modify an item, then fetch it from the tree.
trie.Set(Prefix("Karel Hynek Macha"), 10)
key = Prefix("Karel Hynek Macha")
fmt.Printf("%q: %v\n", key, trie.Get(key))
// "Karel Hynek Macha": 10

// Walk prefixes.
prefix := Prefix("Karel Hynek Macha je kouzelnik")
trie.VisitPrefixes(prefix, printItem)
// "Karel Hynek Macha": 10

// Delete some items.
trie.Delete(Prefix("Pepa Novak"))
trie.Delete(Prefix("Karel Macha"))

// Walk again.
trie.Visit(printItem)
// "Karel Hynek Macha": 10
// "Pepa Sindelar": 2

// Delete a subtree.
trie.DeleteSubtree(Prefix("Pepa"))

// Print what is left.
trie.Visit(printItem)
// "Karel Hynek Macha": 10
```

## License ##

MIT, check the `LICENSE` file.

[![Gittip
Badge](http://img.shields.io/gittip/alanhamlett.png)](https://www.gittip.com/tchap/
"Gittip Badge")

[![Bitdeli
Badge](https://d2weczhvl823v0.cloudfront.net/tchap/go-patricia/trend.png)](https://bitdeli.com/free
"Bitdeli Badge")
## `filepath-securejoin` ##

[![Build Status](https://travis-ci.org/cyphar/filepath-securejoin.svg?branch=master)](https://travis-ci.org/cyphar/filepath-securejoin)

An implementation of `SecureJoin`, a [candidate for inclusion in the Go
standard library][go#20126]. The purpose of this function is to be a "secure"
alternative to `filepath.Join`, and in particular it provides certain
guarantees that are not provided by `filepath.Join`.

This is the function prototype:

```go
func SecureJoin(root, unsafePath string) (string, error)
```

This library **guarantees** the following:

* If no error is set, the resulting string **must** be a child path of
  `SecureJoin` and will not contain any symlink path components (they will all
  be expanded).

* When expanding symlinks, all symlink path components **must** be resolved
  relative to the provided root. In particular, this can be considered a
  userspace implementation of how `chroot(2)` operates on file paths. Note that
  these symlinks will **not** be expanded lexically (`filepath.Clean` is not
  called on the input before processing).

* Non-existant path components are unaffected by `SecureJoin` (similar to
  `filepath.EvalSymlinks`'s semantics).

* The returned path will always be `filepath.Clean`ed and thus not contain any
  `..` components.

A (trivial) implementation of this function on GNU/Linux systems could be done
with the following (note that this requires root privileges and is far more
opaque than the implementation in this library, and also requires that
`readlink` is inside the `root` path):

```go
package securejoin

import (
	"os/exec"
	"path/filepath"
)

func SecureJoin(root, unsafePath string) (string, error) {
	unsafePath = string(filepath.Separator) + unsafePath
	cmd := exec.Command("chroot", root,
		"readlink", "--canonicalize-missing", "--no-newline", unsafePath)
	output, err := cmd.CombinedOutput()
	if err != nil {
		return "", err
	}
	expanded := string(output)
	return filepath.Join(root, expanded), nil
}
```

[go#20126]: https://github.com/golang/go/issues/20126

### License ###

The license of this project is the same as Go, which is a BSD 3-clause license
available in the `LICENSE` file.
# Mergo

A helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.

Also a lovely [comune](http://en.wikipedia.org/wiki/Mergo) (municipality) in the Province of Ancona in the Italian region of Marche.

## Status

It is ready for production use. [It is used in several projects by Docker, Google, The Linux Foundation, VMWare, Shopify, etc](https://github.com/imdario/mergo#mergo-in-the-wild).

[![GoDoc][3]][4]
[![GoCard][5]][6]
[![Build Status][1]][2]
[![Coverage Status][7]][8]
[![Sourcegraph][9]][10]

[1]: https://travis-ci.org/imdario/mergo.png
[2]: https://travis-ci.org/imdario/mergo
[3]: https://godoc.org/github.com/imdario/mergo?status.svg
[4]: https://godoc.org/github.com/imdario/mergo
[5]: https://goreportcard.com/badge/imdario/mergo
[6]: https://goreportcard.com/report/github.com/imdario/mergo
[7]: https://coveralls.io/repos/github/imdario/mergo/badge.svg?branch=master
[8]: https://coveralls.io/github/imdario/mergo?branch=master
[9]: https://sourcegraph.com/github.com/imdario/mergo/-/badge.svg
[10]: https://sourcegraph.com/github.com/imdario/mergo?badge

### Latest release

[Release v0.3.6](https://github.com/imdario/mergo/releases/tag/v0.3.6).

### Important note

Please keep in mind that in [0.3.2](//github.com/imdario/mergo/releases/tag/0.3.2) Mergo changed `Merge()`and `Map()` signatures to support [transformers](#transformers). An optional/variadic argument has been added, so it won't break existing code.

If you were using Mergo **before** April 6th 2015, please check your project works as intended after updating your local copy with ```go get -u github.com/imdario/mergo```. I apologize for any issue caused by its previous behavior and any future bug that Mergo could cause (I hope it won't!) in existing projects after the change (release 0.2.0).

### Donations

If Mergo is useful to you, consider buying me a coffee, a beer or making a monthly donation so I can keep building great free software. :heart_eyes:

<a href='https://ko-fi.com/B0B58839' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi1.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
[![Beerpay](https://beerpay.io/imdario/mergo/badge.svg)](https://beerpay.io/imdario/mergo)
[![Beerpay](https://beerpay.io/imdario/mergo/make-wish.svg)](https://beerpay.io/imdario/mergo)
<a href="https://liberapay.com/dario/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>

### Mergo in the wild

- [moby/moby](https://github.com/moby/moby)
- [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
- [vmware/dispatch](https://github.com/vmware/dispatch)
- [Shopify/themekit](https://github.com/Shopify/themekit)
- [imdario/zas](https://github.com/imdario/zas)
- [matcornic/hermes](https://github.com/matcornic/hermes)
- [OpenBazaar/openbazaar-go](https://github.com/OpenBazaar/openbazaar-go)
- [kataras/iris](https://github.com/kataras/iris)
- [michaelsauter/crane](https://github.com/michaelsauter/crane)
- [go-task/task](https://github.com/go-task/task)
- [sensu/uchiwa](https://github.com/sensu/uchiwa)
- [ory/hydra](https://github.com/ory/hydra)
- [sisatech/vcli](https://github.com/sisatech/vcli)
- [dairycart/dairycart](https://github.com/dairycart/dairycart)
- [projectcalico/felix](https://github.com/projectcalico/felix)
- [resin-os/balena](https://github.com/resin-os/balena)
- [go-kivik/kivik](https://github.com/go-kivik/kivik)
- [Telefonica/govice](https://github.com/Telefonica/govice)
- [supergiant/supergiant](supergiant/supergiant)
- [SergeyTsalkov/brooce](https://github.com/SergeyTsalkov/brooce)
- [soniah/dnsmadeeasy](https://github.com/soniah/dnsmadeeasy)
- [ohsu-comp-bio/funnel](https://github.com/ohsu-comp-bio/funnel)
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
- [bukalapak/snowboard](https://github.com/bukalapak/snowboard)

## Installation

    go get github.com/imdario/mergo

    // use in your .go code
    import (
        "github.com/imdario/mergo"
    )

## Usage

You can only merge same-type structs with exported fields initialized as zero value of their type and same-types maps. Mergo won't merge unexported (private) fields but will do recursively any exported one. It won't merge empty structs value as [they are not considered zero values](https://golang.org/ref/spec#The_zero_value) either. Also maps will be merged recursively except for structs inside maps (because they are not addressable using Go reflection).

```go
if err := mergo.Merge(&dst, src); err != nil {
    // ...
}
```

Also, you can merge overwriting values using the transformer `WithOverride`.

```go
if err := mergo.Merge(&dst, src, mergo.WithOverride); err != nil {
    // ...
}
```

Additionally, you can map a `map[string]interface{}` to a struct (and otherwise, from struct to map), following the same restrictions as in `Merge()`. Keys are capitalized to find each corresponding exported field.

```go
if err := mergo.Map(&dst, srcMap); err != nil {
    // ...
}
```

Warning: if you map a struct to map, it won't do it recursively. Don't expect Mergo to map struct members of your struct as `map[string]interface{}`. They will be just assigned as values.

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
		B: 2,
	}
	dest := Foo{
		A: "two",
	}
	mergo.Merge(&dest, src)
	fmt.Println(dest)
	// Will print
	// {two 2}
}
```

Note: if test are failing due missing package, please execute:

    go get gopkg.in/yaml.v2

### Transformers

Transformers allow to merge specific types differently than in the default behavior. In other words, now you can customize how some types are merged. For example, `time.Time` is a struct; it doesn't have zero value but IsZero can return true because it has fields with zero value. How can we merge a non-zero `time.Time`?

```go
package main

import (
	"fmt"
	"github.com/imdario/mergo"
        "reflect"
        "time"
)

type timeTransfomer struct {
}

func (t timeTransfomer) Transformer(typ reflect.Type) func(dst, src reflect.Value) error {
	if typ == reflect.TypeOf(time.Time{}) {
		return func(dst, src reflect.Value) error {
			if dst.CanSet() {
				isZero := dst.MethodByName("IsZero")
				result := isZero.Call([]reflect.Value{})
				if result[0].Bool() {
					dst.Set(src)
				}
			}
			return nil
		}
	}
	return nil
}

type Snapshot struct {
	Time time.Time
	// ...
}

func main() {
	src := Snapshot{time.Now()}
	dest := Snapshot{}
	mergo.Merge(&dest, src, mergo.WithTransformers(timeTransfomer{}))
	fmt.Println(dest)
	// Will print
	// { 2018-01-12 01:15:00 +0000 UTC m=+0.000000001 }
}
```


## Contact me

If I can help you, you have an idea or you are using Mergo in your projects, don't hesitate to drop me a line (or a pull request): [@im_dario](https://twitter.com/im_dario)

## About

Written by [Dario Castañé](http://dario.im).

## License

[BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) license, as [Go language](http://golang.org/LICENSE).
[![Linux Build Status](https://travis-ci.org/containernetworking/plugins.svg?branch=master)](https://travis-ci.org/containernetworking/plugins)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/kcuubx0chr76ev86/branch/master?svg=true)](https://ci.appveyor.com/project/cni-bot/plugins/branch/master)

# plugins
Some CNI network plugins, maintained by the containernetworking team. For more information, see the individual READMEs.

## Plugins supplied:
### Main: interface-creating
* `bridge`: Creates a bridge, adds the host and the container to it.
* `ipvlan`: Adds an [ipvlan](https://www.kernel.org/doc/Documentation/networking/ipvlan.txt) interface in the container
* `loopback`: Creates a loopback interface
* `macvlan`: Creates a new MAC address, forwards all traffic to that to the container
* `ptp`: Creates a veth pair.
* `vlan`: Allocates a vlan device.

### IPAM: IP address allocation
* `dhcp`: Runs a daemon on the host to make DHCP requests on behalf of the container
* `host-local`: maintains a local database of allocated IPs

### Meta: other plugins
* `flannel`: generates an interface corresponding to a flannel config file
* `tuning`: Tweaks sysctl parameters of an existing interface
* `portmap`: An iptables-based portmapping plugin. Maps ports from the host's address space to the container.

### Sample
The sample plugin provides an example for building your own plugin.
### Namespaces, Threads, and Go
On Linux each OS thread can have a different network namespace.  Go's thread scheduling model switches goroutines between OS threads based on OS thread load and whether the goroutine would block other goroutines.  This can result in a goroutine switching network namespaces without notice and lead to errors in your code.

### Namespace Switching
Switching namespaces with the `ns.Set()` method is not recommended without additional strategies to prevent unexpected namespace changes when your goroutines switch OS threads.

Go provides the `runtime.LockOSThread()` function to ensure a specific goroutine executes on its current OS thread and prevents any other goroutine from running in that thread until the locked one exits.  Careful usage of `LockOSThread()` and goroutines can provide good control over which network namespace a given goroutine executes in.

For example, you cannot rely on the `ns.Set()` namespace being the current namespace after the `Set()` call unless you do two things.  First, the goroutine calling `Set()` must have previously called `LockOSThread()`.  Second, you must ensure `runtime.UnlockOSThread()` is not called somewhere in-between.  You also cannot rely on the initial network namespace remaining the current network namespace if any other code in your program switches namespaces, unless you have already called `LockOSThread()` in that goroutine.  Note that `LockOSThread()` prevents the Go scheduler from optimally scheduling goroutines for best performance, so `LockOSThread()` should only be used in small, isolated goroutines that release the lock quickly.

### Do() The Recommended Thing
The `ns.Do()` method provides **partial** control over network namespaces for you by implementing these strategies. All code dependent on a particular network namespace (including the root namespace) should be wrapped in the `ns.Do()` method to ensure the correct namespace is selected for the duration of your code.  For example:

```go
targetNs, err := ns.NewNS()
if err != nil {
    return err
}
err = targetNs.Do(func(hostNs ns.NetNS) error {
	dummy := &netlink.Dummy{
		LinkAttrs: netlink.LinkAttrs{
			Name: "dummy0",
		},
	}
	return netlink.LinkAdd(dummy)
})
```

Note this requirement to wrap every network call is very onerous - any libraries you call might call out to network services such as DNS, and all such calls need to be protected after you call `ns.Do()`. The CNI plugins all exit very soon after calling `ns.Do()` which helps to minimize the problem.

Also:  If the runtime spawns a new OS thread, it will inherit the network namespace of the parent thread, which may have been temporarily switched, and thus the new OS thread will be permanently "stuck in the wrong namespace".

In short, **there is no safe way to change network namespaces from within a long-lived, multithreaded Go process**.  If your daemon process needs to be namespace aware, consider spawning a separate process (like a CNI plugin) for each namespace.

### Further Reading
 - https://github.com/golang/go/wiki/LockOSThread
 - http://morsmachine.dk/go-scheduler
 - https://github.com/containernetworking/cni/issues/262
 - https://golang.org/pkg/runtime/
 - https://www.weave.works/blog/linux-namespaces-and-go-don-t-mix
[![Linux Build Status](https://travis-ci.org/containernetworking/cni.svg?branch=master)](https://travis-ci.org/containernetworking/cni)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/wtrkou8oow7x533e/branch/master?svg=true)](https://ci.appveyor.com/project/cni-bot/cni/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/containernetworking/cni/badge.svg?branch=master)](https://coveralls.io/github/containernetworking/cni?branch=master)
[![Slack Status](https://cryptic-tundra-43194.herokuapp.com/badge.svg)](https://cryptic-tundra-43194.herokuapp.com/)

![CNI Logo](logo.png)

---

# Community Sync Meeting

There is a community sync meeting for users and developers every 1-2 months. The next meeting will help on a Google Hangout and the link is in the [agenda](https://docs.google.com/document/d/10ECyT2mBGewsJUcmYmS8QNo1AcNgy2ZIe2xS7lShYhE/edit?usp=sharing) (Notes from previous meeting are also in this doc). 

The next meeting will be held on *Wednesday, October 4th* at *3:00pm UTC / 11:00am EDT / 8:00am PDT* [Add to Calendar](https://www.worldtimebuddy.com/?qm=1&lid=100,5,2643743,5391959&h=100&date=2017-10-04&sln=15-16).

---

# CNI - the Container Network Interface

## What is CNI?

CNI (_Container Network Interface_), a [Cloud Native Computing Foundation](https://cncf.io) project, consists of a specification and libraries for writing plugins to configure network interfaces in Linux containers, along with a number of supported plugins.
CNI concerns itself only with network connectivity of containers and removing allocated resources when the container is deleted.
Because of this focus, CNI has a wide range of support and the specification is simple to implement.

As well as the [specification](SPEC.md), this repository contains the Go source code of a [library for integrating CNI into applications](libcni) and an [example command-line tool](cnitool) for executing CNI plugins.  A [separate repository contains reference plugins](https://github.com/containernetworking/plugins) and a template for making new plugins.

The template code makes it straight-forward to create a CNI plugin for an existing container networking project.
CNI also makes a good framework for creating a new container networking project from scratch.

## Why develop CNI?

Application containers on Linux are a rapidly evolving area, and within this area networking is not well addressed as it is highly environment-specific.
We believe that many container runtimes and orchestrators will seek to solve the same problem of making the network layer pluggable.

To avoid duplication, we think it is prudent to define a common interface between the network plugins and container execution: hence we put forward this specification, along with libraries for Go and a set of plugins.

## Who is using CNI?
### Container runtimes
- [rkt - container engine](https://coreos.com/blog/rkt-cni-networking.html)
- [Kubernetes - a system to simplify container operations](http://kubernetes.io/docs/admin/network-plugins/)
- [OpenShift - Kubernetes with additional enterprise features](https://github.com/openshift/origin/blob/master/docs/openshift_networking_requirements.md)
- [Cloud Foundry - a platform for cloud applications](https://github.com/cloudfoundry-incubator/cf-networking-release)
- [Apache Mesos - a distributed systems kernel](https://github.com/apache/mesos/blob/master/docs/cni.md)
- [Amazon ECS - a highly scalable, high performance container management service](https://aws.amazon.com/ecs/)

### 3rd party plugins
- [Project Calico - a layer 3 virtual network](https://github.com/projectcalico/calico-cni)
- [Weave - a multi-host Docker network](https://github.com/weaveworks/weave)
- [Contiv Networking - policy networking for various use cases](https://github.com/contiv/netplugin)
- [SR-IOV](https://github.com/hustcat/sriov-cni)
- [Cilium - BPF & XDP for containers](https://github.com/cilium/cilium)
- [Infoblox - enterprise IP address management for containers](https://github.com/infobloxopen/cni-infoblox)
- [Multus - a Multi plugin](https://github.com/Intel-Corp/multus-cni)
- [Romana - Layer 3 CNI plugin supporting network policy for Kubernetes](https://github.com/romana/kube)
- [CNI-Genie - generic CNI network plugin](https://github.com/Huawei-PaaS/CNI-Genie)
- [Nuage CNI - Nuage Networks SDN plugin for network policy kubernetes support ](https://github.com/nuagenetworks/nuage-cni)
- [Silk - a CNI plugin designed for Cloud Foundry](https://github.com/cloudfoundry-incubator/silk)
- [Linen - a CNI plugin designed for overlay networks with Open vSwitch and fit in SDN/OpenFlow network environment](https://github.com/John-Lin/linen-cni)
- [Vhostuser - a Dataplane network plugin - Supports OVS-DPDK & VPP](https://github.com/intel/vhost-user-net-plugin)
- [Amazon ECS CNI Plugins - a collection of CNI Plugins to configure containers with Amazon EC2 elastic network interfaces (ENIs)](https://github.com/aws/amazon-ecs-cni-plugins)
- [Bonding CNI - a Link aggregating plugin to address failover and high availability network](https://github.com/Intel-Corp/bond-cni)
- [ovn-kubernetes - an container network plugin built on Open vSwitch (OVS) and Open Virtual Networking (OVN) with support for both Linux and Windows](https://github.com/openvswitch/ovn-kubernetes)

The CNI team also maintains some [core plugins in a separate repository](https://github.com/containernetworking/plugins).


## Contributing to CNI

We welcome contributions, including [bug reports](https://github.com/containernetworking/cni/issues), and code and documentation improvements.
If you intend to contribute to code or documentation, please read [CONTRIBUTING.md](CONTRIBUTING.md). Also see the [contact section](#contact) in this README.

## How do I use CNI?

### Requirements

The CNI spec is language agnostic.  To use the Go language libraries in this repository, you'll need a recent version of Go.  Our [automated tests](https://travis-ci.org/containernetworking/cni/builds) cover Go versions 1.7 and 1.8.

### Reference Plugins

The CNI project maintains a set of [reference plugins](https://github.com/containernetworking/plugins) that implement the CNI specification.
NOTE: the reference plugins used to live in this repository but have been split out into a [separate repository](https://github.com/containernetworking/plugins) as of May 2017.

### Running the plugins

After building and installing the [reference plugins](https://github.com/containernetworking/plugins), you can use the `priv-net-run.sh` and `docker-run.sh` scripts in the `scripts/` directory to exercise the plugins.

**note - priv-net-run.sh depends on `jq`**

Start out by creating a netconf file to describe a network:

```bash
$ mkdir -p /etc/cni/net.d
$ cat >/etc/cni/net.d/10-mynet.conf <<EOF
{
	"cniVersion": "0.2.0",
	"name": "mynet",
	"type": "bridge",
	"bridge": "cni0",
	"isGateway": true,
	"ipMasq": true,
	"ipam": {
		"type": "host-local",
		"subnet": "10.22.0.0/16",
		"routes": [
			{ "dst": "0.0.0.0/0" }
		]
	}
}
EOF
$ cat >/etc/cni/net.d/99-loopback.conf <<EOF
{
	"cniVersion": "0.2.0",
	"type": "loopback"
}
EOF
```

The directory `/etc/cni/net.d` is the default location in which the scripts will look for net configurations.

Next, build the plugins:

```bash
$ cd $GOPATH/src/github.com/containernetworking/plugins
$ ./build.sh
```

Finally, execute a command (`ifconfig` in this example) in a private network namespace that has joined the `mynet` network:

```bash
$ CNI_PATH=$GOPATH/src/github.com/containernetworking/plugins/bin
$ cd $GOPATH/src/github.com/containernetworking/cni/scripts
$ sudo CNI_PATH=$CNI_PATH ./priv-net-run.sh ifconfig
eth0      Link encap:Ethernet  HWaddr f2:c2:6f:54:b8:2b  
          inet addr:10.22.0.2  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::f0c2:6fff:fe54:b82b/64 Scope:Link
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:1 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:1 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:90 (90.0 B)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

The environment variable `CNI_PATH` tells the scripts and library where to look for plugin executables.

## Running a Docker container with network namespace set up by CNI plugins

Use the instructions in the previous section to define a netconf and build the plugins.
Next, docker-run.sh script wraps `docker run`, to execute the plugins prior to entering the container:

```bash
$ CNI_PATH=$GOPATH/src/github.com/containernetworking/plugins/bin
$ cd $GOPATH/src/github.com/containernetworking/cni/scripts
$ sudo CNI_PATH=$CNI_PATH ./docker-run.sh --rm busybox:latest ifconfig
eth0      Link encap:Ethernet  HWaddr fa:60:70:aa:07:d1  
          inet addr:10.22.0.2  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::f860:70ff:feaa:7d1/64 Scope:Link
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:1 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:1 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:90 (90.0 B)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

## What might CNI do in the future?

CNI currently covers a wide range of needs for network configuration due to it simple model and API.
However, in the future CNI might want to branch out into other directions:

- Dynamic updates to existing network configuration
- Dynamic policies for network bandwidth and firewall rules

If these topics of are interest, please contact the team via the mailing list or IRC and find some like-minded people in the community to put a proposal together.

## Contact

For any questions about CNI, please reach out on the mailing list:
- Email: [cni-dev](https://groups.google.com/forum/#!forum/cni-dev)
- IRC: #[containernetworking](irc://irc.freenode.org:6667/#containernetworking) channel on freenode.org
- Slack: [containernetworking.slack.com](https://cryptic-tundra-43194.herokuapp.com)
# reflect2

[![Sourcegraph](https://sourcegraph.com/github.com/modern-go/reflect2/-/badge.svg)](https://sourcegraph.com/github.com/modern-go/reflect2?badge)
[![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/modern-go/reflect2)
[![Build Status](https://travis-ci.org/modern-go/reflect2.svg?branch=master)](https://travis-ci.org/modern-go/reflect2)
[![codecov](https://codecov.io/gh/modern-go/reflect2/branch/master/graph/badge.svg)](https://codecov.io/gh/modern-go/reflect2)
[![rcard](https://goreportcard.com/badge/github.com/modern-go/reflect2)](https://goreportcard.com/report/github.com/modern-go/reflect2)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://raw.githubusercontent.com/modern-go/reflect2/master/LICENSE)

reflect api that avoids runtime reflect.Value cost

* reflect get/set interface{}, with type checking
* reflect get/set unsafe.Pointer, without type checking
* `reflect2.TypeByName` works like `Class.forName` found in java

[json-iterator](https://github.com/json-iterator/go) use this package to save runtime dispatching cost.
This package is designed for low level libraries to optimize reflection performance.
General application should still use reflect standard library.

# reflect2.TypeByName

```go
// given package is github.com/your/awesome-package
type MyStruct struct {
	// ...
}

// will return the type
reflect2.TypeByName("awesome-package.MyStruct")
// however, if the type has not been used
// it will be eliminated by compiler, so we can not get it in runtime
```

# reflect2 get/set interface{}

```go
valType := reflect2.TypeOf(1)
i := 1
j := 10
valType.Set(&i, &j)
// i will be 10
```

to get set `type`, always use its pointer `*type`

# reflect2 get/set unsafe.Pointer

```go
valType := reflect2.TypeOf(1)
i := 1
j := 10
valType.UnsafeSet(unsafe.Pointer(&i), unsafe.Pointer(&j))
// i will be 10
```

to get set `type`, always use its pointer `*type`

# benchmark

Benchmark is not necessary for this package. It does nothing actually.
As it is just a thin wrapper to make go runtime public. 
Both `reflect2` and `reflect` call same function 
provided by `runtime` package exposed by go language.

# unsafe safety

Instead of casting `[]byte` to `sliceHeader` in your application using unsafe.
We can use reflect2 instead. This way, if `sliceHeader` changes in the future,
only reflect2 need to be upgraded.

reflect2 tries its best to keep the implementation same as reflect (by testing).# concurrent

[![Sourcegraph](https://sourcegraph.com/github.com/modern-go/concurrent/-/badge.svg)](https://sourcegraph.com/github.com/modern-go/concurrent?badge)
[![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/modern-go/concurrent)
[![Build Status](https://travis-ci.org/modern-go/concurrent.svg?branch=master)](https://travis-ci.org/modern-go/concurrent)
[![codecov](https://codecov.io/gh/modern-go/concurrent/branch/master/graph/badge.svg)](https://codecov.io/gh/modern-go/concurrent)
[![rcard](https://goreportcard.com/badge/github.com/modern-go/concurrent)](https://goreportcard.com/report/github.com/modern-go/concurrent)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://raw.githubusercontent.com/modern-go/concurrent/master/LICENSE)

* concurrent.Map: backport sync.Map for go below 1.9
* concurrent.Executor: goroutine with explicit ownership and cancellable

# concurrent.Map

because sync.Map is only available in go 1.9, we can use concurrent.Map to make code portable

```go
m := concurrent.NewMap()
m.Store("hello", "world")
elem, found := m.Load("hello")
// elem will be "world"
// found will be true
```

# concurrent.Executor

```go
executor := concurrent.NewUnboundedExecutor()
executor.Go(func(ctx context.Context) {
    everyMillisecond := time.NewTicker(time.Millisecond)
    for {
        select {
        case <-ctx.Done():
            fmt.Println("goroutine exited")
            return
        case <-everyMillisecond.C:
            // do something
        }
    }
})
time.Sleep(time.Second)
executor.StopAndWaitForever()
fmt.Println("executor stopped")
```

attach goroutine to executor instance, so that we can

* cancel it by stop the executor with Stop/StopAndWait/StopAndWaitForever
* handle panic by callback: the default behavior will no longer crash your application# go-systemd

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
# go-iptables

[![GoDoc](https://godoc.org/github.com/coreos/go-iptables/iptables?status.svg)](https://godoc.org/github.com/coreos/go-iptables/iptables)
[![Build Status](https://travis-ci.org/coreos/go-iptables.png?branch=master)](https://travis-ci.org/coreos/go-iptables)

Go bindings for iptables utility.

In-kernel netfilter does not have a good userspace API. The tables are manipulated via setsockopt that sets/replaces the entire table. Changes to existing table need to be resolved by userspace code which is difficult and error-prone. Netfilter developers heavily advocate using iptables utlity for programmatic manipulation.

go-iptables wraps invocation of iptables utility with functions to append and delete rules; create, clear and delete chains.
# go-ansiterm

This is a cross platform Ansi Terminal Emulation library.  It reads a stream of Ansi characters and produces the appropriate function calls.  The results of the function calls are platform dependent.

For example the parser might receive "ESC, [, A" as a stream of three characters.  This is the code for Cursor Up (http://www.vt100.net/docs/vt510-rm/CUU).  The parser then calls the cursor up function (CUU()) on an event handler.  The event handler determines what platform specific work must be done to cause the cursor to move up one position.

The parser (parser.go) is a partial implementation of this state machine (http://vt100.net/emu/vt500_parser.png).  There are also two event handler implementations, one for tests (test_event_handler.go) to validate that the expected events are being produced and called, the other is a Windows implementation (winterm/win_event_handler.go).

See parser_test.go for examples exercising the state machine and generating appropriate function calls.

-----
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
# errors [![Travis-CI](https://travis-ci.org/pkg/errors.svg)](https://travis-ci.org/pkg/errors) [![AppVeyor](https://ci.appveyor.com/api/projects/status/b98mptawhudj53ep/branch/master?svg=true)](https://ci.appveyor.com/project/davecheney/errors/branch/master) [![GoDoc](https://godoc.org/github.com/pkg/errors?status.svg)](http://godoc.org/github.com/pkg/errors) [![Report card](https://goreportcard.com/badge/github.com/pkg/errors)](https://goreportcard.com/report/github.com/pkg/errors) [![Sourcegraph](https://sourcegraph.com/github.com/pkg/errors/-/badge.svg)](https://sourcegraph.com/github.com/pkg/errors?badge)

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

## License

BSD-2-Clause
profile
=======

Simple profiling support package for Go

[![Build Status](https://travis-ci.org/pkg/profile.svg?branch=master)](https://travis-ci.org/pkg/profile) [![GoDoc](http://godoc.org/github.com/pkg/profile?status.svg)](http://godoc.org/github.com/pkg/profile)


installation
------------

    go get github.com/pkg/profile

usage
-----

Enabling profiling in your application is as simple as one line at the top of your main function

```go
import "github.com/pkg/profile"

func main() {
    defer profile.Start().Stop()
    ...
}
```

options
-------

What to profile is controlled by config value passed to profile.Start. 
By default CPU profiling is enabled.

```go
import "github.com/pkg/profile"

func main() {
    // p.Stop() must be called before the program exits to
    // ensure profiling information is written to disk.
    p := profile.Start(profile.MemProfile, profile.ProfilePath("."), profile.NoShutdownHook)
    ...
}
```

Several convenience package level values are provided for cpu, memory, and block (contention) profiling.

For more complex options, consult the [documentation](http://godoc.org/github.com/pkg/profile).

contributing
------------

We welcome pull requests, bug fixes and issue reports.

Before proposing a change, please discuss it first by raising an issue.
[![master](https://travis-ci.org/checkpoint-restore/go-criu.svg?branch=master)](https://travis-ci.org/checkpoint-restore/go-criu)

## go-criu -- Go bindings for [CRIU](https://criu.org/)

This repository provides Go bindings for CRIU. The code is based on the Go based PHaul
implementation from the CRIU repository. For easier inclusion into other Go projects the
CRIU Go bindings have been moved to this repository.

The Go bindings provide an easy way to use the CRIU RPC calls from Go without the need
to set up all the infrastructure to make the actual RPC connection to CRIU.

The following example would print the version of CRIU:
```
	c := criu.MakeCriu()
	version, err := c.GetCriuVersion()
	fmt.Println(version)
```
or to just check if at least a certain CRIU version is installed:
```
	c := criu.MakeCriu()
	result, err := c.IsCriuAtLeast(31100)
```

## How to contribute

While bug fixes can first be identified via an "issue", that is not required.
It's ok to just open up a PR with the fix, but make sure you include the same
information you would have included in an issue - like how to reproduce it.

PRs for new features should include some background on what use cases the
new code is trying to address. When possible and when it makes sense, try to
break-up larger PRs into smaller ones - it's easier to review smaller
code changes. But only if those smaller ones make sense as stand-alone PRs.

Regardless of the type of PR, all PRs should include:
* well documented code changes
* additional testcases. Ideally, they should fail w/o your code change applied
* documentation changes

Squash your commits into logical pieces of work that might want to be reviewed
separate from the rest of the PRs. Ideally, each commit should implement a
single idea, and the PR branch should pass the tests at every commit. GitHub
makes it easy to review the cumulative effect of many commits; so, when in
doubt, use smaller commits.

PRs that fix issues should include a reference like `Closes #XXXX` in the
commit message so that github will automatically close the referenced issue
when the PR is merged.

Contributors must assert that they are in compliance with the [Developer
Certificate of Origin 1.1](http://developercertificate.org/). This is achieved
by adding a "Signed-off-by" line containing the contributor's name and e-mail
to every commit message. Your signature certifies that you wrote the patch or
otherwise have the right to pass it on as an open-source patch.

### License

The license of go-criu is the Apache 2.0 license.
# ffjson: faster JSON for Go

[![Build Status](https://travis-ci.org/pquerna/ffjson.svg?branch=master)](https://travis-ci.org/pquerna/ffjson)

`ffjson` generates static `MarshalJSON` and `UnmarshalJSON` functions for structures in Go. The generated functions reduce the reliance upon runtime reflection to do serialization and are generally 2 to 3 times faster.  In cases where `ffjson` doesn't understand a Type involved, it falls back to `encoding/json`, meaning it is a safe drop in replacement.  By using `ffjson` your JSON serialization just gets faster with no additional code changes.

When you change your `struct`, you will need to run `ffjson` again (or make it part of your build tools).

## Blog Posts

* 2014-03-31: [First Release and Background](https://journal.paul.querna.org/articles/2014/03/31/ffjson-faster-json-in-go/)

## Getting Started

If `myfile.go` contains the `struct` types you would like to be faster, and assuming `GOPATH` is set to a reasonable value for an existing project (meaning that in this particular example if `myfile.go` is in the `myproject` directory, the project should be under `$GOPATH/src/myproject`), you can just run:

    go get -u github.com/pquerna/ffjson
    ffjson myfile.go
    git add myfile_ffjson.go


## Performance Status:

* `MarshalJSON` is **2x to 3x** faster than `encoding/json`.
* `UnmarshalJSON` is **2x to 3x** faster than `encoding/json`.

## Features

* **Unmarshal Support:** Since v0.9, `ffjson` supports Unmarshaling of structures.
* **Drop in Replacement:** Because `ffjson` implements the interfaces already defined by `encoding/json` the performance enhancements are transparent to users of your structures.
* **Supports all types:** `ffjson` has native support for most of Go's types -- for any type it doesn't support with fast paths, it falls back to using `encoding/json`.  This means all structures should work out of the box. If they don't, [open a issue!](https://github.com/pquerna/ffjson/issues)
* **ffjson: skip**: If you have a structure you want `ffjson` to ignore, add `ffjson: skip` to the doc string for this structure.
* **Extensive Tests:** `ffjson` contains an extensive test suite including fuzz'ing against the JSON parser.


# Using ffjson

`ffjson` generates code based upon existing `struct` types.  For example, `ffjson foo.go` will by default create a new file `foo_ffjson.go` that contains serialization functions for all structs found in `foo.go`.

```
Usage of ffjson:

        ffjson [options] [input_file]

ffjson generates Go code for optimized JSON serialization.

  -go-cmd="": Path to go command; Useful for `goapp` support.
  -import-name="": Override import name in case it cannot be detected.
  -nodecoder: Do not generate decoder functions
  -noencoder: Do not generate encoder functions
  -w="": Write generate code to this path instead of ${input}_ffjson.go.
```

Your code must be in a compilable state for `ffjson` to work. If you code doesn't compile ffjson will most likely exit with an error.

## Disabling code generation for structs

You might not want all your structs to have JSON code generated. To completely disable generation for a struct, add `ffjson: skip` to the struct comment. For example:

```Go
// ffjson: skip
type Foo struct {
   Bar string
}
```

You can also choose not to have either the decoder or encoder generated by including `ffjson: nodecoder` or `ffjson: noencoder` in your comment. For instance, this will only generate the encoder (marshal) part for this struct:

```Go
// ffjson: nodecoder
type Foo struct {
   Bar string
}
```

You can also disable encoders/decoders entirely for a file by using the `-noencoder`/`-nodecoder` commandline flags.

## Using ffjson with `go generate`

`ffjson` is a great fit with `go generate`. It allows you to specify the ffjson command inside your individual go files and run them all at once. This way you don't have to maintain a separate build file with the files you need to generate.

Add this comment anywhere inside your go files:

```Go
//go:generate ffjson $GOFILE
```

To re-generate ffjson for all files with the tag in a folder, simply execute:

```sh
go generate
```

To generate for the current package and all sub-packages, use:

```sh
go generate ./...
```
This is most of what you need to know about go generate, but you can sese more about [go generate on the golang blog](http://blog.golang.org/generate).

## Should I include ffjson files in VCS?

That question is really up to you. If you don't, you will have a more complex build process. If you do, you have to keep the generated files updated if you change the content of your structs.

That said, ffjson operates deterministically, so it will generate the same code every time it run, so unless your code changes, the generated content should not change. Note however that this is only true if you are using the same ffjson version, so if you have several people working on a project, you might need to synchronize your ffjson version.

## Performance pitfalls

`ffjson` has a few cases where it will fall back to using the runtime encoder/decoder. Notable cases are:

* Interface struct members. Since it isn't possible to know the type of these types before runtime, ffjson has to use the reflect based coder.
* Structs with custom marshal/unmarshal.
* Map with a complex value. Simple types like `map[string]int` is fine though.
* Inline struct definitions `type A struct{B struct{ X int} }` are handled by the encoder, but currently has fallback in the decoder.
* Slices of slices / slices of maps are currently falling back when generating the decoder.

## Reducing Garbage Collection

`ffjson` already does a lot to help garbage generation. However whenever you go through the json.Marshal you get a new byte slice back. On very high throughput servers this can lead to increased GC pressure. 

### Tip 1: Use ffjson.Marshal() / ffjson.Unmarshal()

This is probably the easiest optimization for you. Instead of going through encoding/json, you can call ffjson. This will disable the checks that encoding/json does to the json when it receives it from struct functions.

```Go
	import "github.com/pquerna/ffjson/ffjson"

	// BEFORE:
	buf, err := json.Marshal(&item)

	// AFTER:
	buf, err := ffjson.Marshal(&item)
```
This simple change is likely to double the speed of your encoding/decoding.


[![GoDoc][1]][2]
[1]: https://godoc.org/github.com/pquerna/ffjson/ffjson?status.svg
[2]: https://godoc.org/github.com/pquerna/ffjson/ffjson#Marshal

### Tip 2: Pooling the buffer

On servers where you have a lot of concurrent encoding going on, you can hand back the byte buffer you get from json.Marshal once you are done using it. An example could look like this:
```Go
import "github.com/pquerna/ffjson/ffjson"

func Encode(item interface{}, out io.Writer) {
	// Encode
	buf, err := ffjson.Marshal(&item)
	
	// Write the buffer
	_,_ = out.Write(buf)
	
	// We are now no longer need the buffer so we pool it. 
	ffjson.Pool(buf)
}
```
Note that the buffers you put back in the pool can still be reclaimed by the garbage collector, so you wont risk your program building up a big memory use by pooling the buffers.

[![GoDoc][1]][2]
[1]: https://godoc.org/github.com/pquerna/ffjson/ffjson?status.svg
[2]: https://godoc.org/github.com/pquerna/ffjson/ffjson#Pool

### Tip 3: Creating an Encoder

There might be cases where you need to encode many objects at once. This could be a server backing up, writing a lot of entries to files, etc.

To do this, there is an interface similar to `encoding/json`, that allow you to create a re-usable encoder. Here is an example where we want to encode an array of the `Item` type, with a comma between entries:
```Go
import "github.com/pquerna/ffjson/ffjson"

func EncodeItems(items []Item, out io.Writer) {
        // We create an encoder.
	enc := ffjson.NewEncoder(out)
	
	for i, item := range items {
		// Encode into the buffer
		err := enc.Encode(&item)
		
		// If err is nil, the content is written to out, so we can write to it as well.
		if i != len(items) -1 {
			_,_ = out.Write([]byte{','})
		}
	}
}
```


Documentation: [![GoDoc][1]][2]
[1]: https://godoc.org/github.com/pquerna/ffjson/ffjson?status.svg
[2]: https://godoc.org/github.com/pquerna/ffjson/ffjson#Encoder

## Tip 4: Avoid interfaces

We don't want to dictate how you structure your data, but having interfaces in your code will make ffjson use the golang encoder for these. When ffjson has to do this, it may even become slower than using `json.Marshal` directly. 

To see where that happens, search the generated `_ffjson.go` file for the text `Falling back`, which will indicate where ffjson is unable to generate code for your data structure.

## Tip 5: `ffjson` all the things!

You should not only create ffjson code for your main struct, but also any structs that is included/used in your json code.

So if your struct looks like this:
```Go
type Foo struct {
  V Bar
}
```
You should also make sure that code is generated for `Bar` if it is placed in another file. Also note that currently it requires you to do this in order, since generating code for `Foo` will check if code for `Bar` exists. This is only an issue if `Foo` and `Bar` are placed in different files. We are currently working on allowing simultaneous generation of an entire package.


## Improvements, bugs, adding features, and taking ffjson new directions!

Please [open issues in Github](https://github.com/pquerna/ffjson/issues) for ideas, bugs, and general thoughts.  Pull requests are of course preferred :)

## Similar projects

* [go-codec](https://github.com/ugorji/go/tree/master/codec#readme). Very good project, that also allows streaming en/decoding, but requires you to call the library to use.
* [megajson](https://github.com/benbjohnson/megajson). This has limited support, and development seems to have almost stopped at the time of writing.

# Credits

`ffjson` has recieved significant contributions from:

* [Klaus Post](https://github.com/klauspost)
* [Paul Querna](https://github.com/pquerna) 
* [Erik Dubbelboer](https://github.com/erikdubbelboer)

## License

`ffjson` is licensed under the [Apache License, Version 2.0](./LICENSE)

[![Build Status](https://travis-ci.org/varlink/go.svg?branch=master)](https://travis-ci.org/varlink/go)
[![Go Report Card](https://goreportcard.com/badge/github.com/varlink/go)](https://goreportcard.com/report/github.com/varlink/go)
[![Go Doc](https://img.shields.io/badge/godoc-reference-blue.svg?style=flat-square)](http://godoc.org/github.com/varlink/go/varlink)
[![Coverage Status](https://coveralls.io/repos/github/varlink/go/badge.svg?branch=master)](https://coveralls.io/github/varlink/go?branch=master)
[![Release](https://img.shields.io/github/release/golang-standards/project-layout.svg?style=flat-square)](https://github.com/varlink/go/varlink/releases/latest)

# go/varlink
OSTree-Go
=========

Go bindings for OSTree. Find out more about OSTree [here](https://github.com/ostreedev/ostree)
# Go support for Protocol Buffers - Google's data interchange format

[![Build Status](https://travis-ci.org/golang/protobuf.svg?branch=master)](https://travis-ci.org/golang/protobuf)
[![GoDoc](https://godoc.org/github.com/golang/protobuf?status.svg)](https://godoc.org/github.com/golang/protobuf)

Google's data interchange format.
Copyright 2010 The Go Authors.
https://github.com/golang/protobuf

This package and the code it generates requires at least Go 1.6.

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

## Packages and input paths ##

The protocol buffer language has a concept of "packages" which does not
correspond well to the Go notion of packages. In generated Go code,
each source `.proto` file is associated with a single Go package. The
name and import path for this package is specified with the `go_package`
proto option:

	option go_package = "github.com/golang/protobuf/ptypes/any";

The protocol buffer compiler will attempt to derive a package name and
import path if a `go_package` option is not present, but it is
best to always specify one explicitly.

There is a one-to-one relationship between source `.proto` files and
generated `.pb.go` files, but any number of `.pb.go` files may be
contained in the same Go package.

The output name of a generated file is produced by replacing the
`.proto` suffix with `.pb.go` (e.g., `foo.proto` produces `foo.pb.go`).
However, the output directory is selected in one of two ways.  Let
us say we have `inputs/x.proto` with a `go_package` option of
`github.com/golang/protobuf/p`. The corresponding output file may
be:

- Relative to the import path:

```shell
  protoc --go_out=. inputs/x.proto
  # writes ./github.com/golang/protobuf/p/x.pb.go
```

  (This can work well with `--go_out=$GOPATH`.)

- Relative to the input file:

```shell
protoc --go_out=paths=source_relative:. inputs/x.proto
# generate ./inputs/x.pb.go
```

## Generated code ##

The package comment for the proto library contains text describing
the interface provided in Go for protocol buffers. Here is an edited
version.

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
	syntax = "proto2";
	package example;

	enum FOO { X = 17; };

	message Test {
	  required string label = 1;
	  optional int32 type = 2 [default=77];
	  repeated int64 reps = 3;
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
		test := &example.Test{
			Label: proto.String("hello"),
			Type:  proto.Int32(17),
			Reps:  []int64{1, 2, 3},
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

- `paths=(import | source_relative)` - specifies how the paths of
  generated files are structured. See the "Packages and imports paths"
  section above. The default is `import`.
- `plugins=plugin1+plugin2` - specifies the list of sub-plugins to
  load. The only plugin in this repo is `grpc`.
- `Mfoo/bar.proto=quux/shme` - declares that foo/bar.proto is
  associated with Go package quux/shme.  This is subject to the
  import_prefix parameter.

The following parameters are deprecated and should not be used:

- `import_prefix=xxx` - a prefix that is added onto the beginning of
  all imports.
- `import_path=foo/bar` - used as the package if no input files
  declare `go_package`. If it contains slashes, everything up to the
  rightmost slash is ignored.

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
go-shlex is a simple lexer for go that supports shell-style quoting,
commenting, and escaping.
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
[![Sourcegraph](https://sourcegraph.com/github.com/json-iterator/go/-/badge.svg)](https://sourcegraph.com/github.com/json-iterator/go?badge)
[![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/json-iterator/go)
[![Build Status](https://travis-ci.org/json-iterator/go.svg?branch=master)](https://travis-ci.org/json-iterator/go)
[![codecov](https://codecov.io/gh/json-iterator/go/branch/master/graph/badge.svg)](https://codecov.io/gh/json-iterator/go)
[![rcard](https://goreportcard.com/badge/github.com/json-iterator/go)](https://goreportcard.com/report/github.com/json-iterator/go)
[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](https://raw.githubusercontent.com/json-iterator/go/master/LICENSE)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/json-iterator/Lobby)

A high-performance 100% compatible drop-in replacement of "encoding/json"

You can also use thrift like JSON using [thrift-iterator](https://github.com/thrift-iterator/go)

```
Go开发者们请加入我们，滴滴出行平台技术部 taowen@didichuxing.com
```

# Benchmark

![benchmark](http://jsoniter.com/benchmarks/go-benchmark.png)

Source code: https://github.com/json-iterator/go-benchmark/blob/master/src/github.com/json-iterator/go-benchmark/benchmark_medium_payload_test.go

Raw Result (easyjson requires static code generation)

| | ns/op | allocation bytes | allocation times |
| --- | --- | --- | --- |
| std decode | 35510 ns/op | 1960 B/op | 99 allocs/op |
| easyjson decode | 8499 ns/op | 160 B/op | 4 allocs/op |
| jsoniter decode | 5623 ns/op | 160 B/op | 3 allocs/op |
| std encode | 2213 ns/op | 712 B/op | 5 allocs/op |
| easyjson encode | 883 ns/op | 576 B/op | 3 allocs/op |
| jsoniter encode | 837 ns/op | 384 B/op | 4 allocs/op |

Always benchmark with your own workload. 
The result depends heavily on the data input.

# Usage

100% compatibility with standard lib

Replace

```go
import "encoding/json"
json.Marshal(&data)
```

with 

```go
import "github.com/json-iterator/go"

var json = jsoniter.ConfigCompatibleWithStandardLibrary
json.Marshal(&data)
```

Replace

```go
import "encoding/json"
json.Unmarshal(input, &data)
```

with

```go
import "github.com/json-iterator/go"

var json = jsoniter.ConfigCompatibleWithStandardLibrary
json.Unmarshal(input, &data)
```

[More documentation](http://jsoniter.com/migrate-from-go-std.html)

# How to get

```
go get github.com/json-iterator/go
```

# Contribution Welcomed !

Contributors

* [thockin](https://github.com/thockin) 
* [mattn](https://github.com/mattn)
* [cch123](https://github.com/cch123)
* [Oleg Shaldybin](https://github.com/olegshaldybin)
* [Jason Toffaletti](https://github.com/toffaletti)

Report issue or pull request, or email taowen@gmail.com, or [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/json-iterator/Lobby)
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

## Using the API

The following example program shows how to use the API.

```go
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
```

## Using the gxz compression tool

The package includes a gxz command line utility for compression and
decompression.

Use following command for installation:

    $ go get github.com/ulikunitz/xz/cmd/gxz

To test it call the following command.

    $ gxz bigfile

After some time a much smaller file bigfile.xz will replace bigfile.
To decompress it use the following command.

    $ gxz -d bigfile.xz

# hcsshim

[![Build status](https://ci.appveyor.com/api/projects/status/nbcw28mnkqml0loa/branch/master?svg=true)](https://ci.appveyor.com/project/WindowsVirtualization/hcsshim/branch/master)

This package contains the Golang interface for using the Windows [Host Compute Service](https://blogs.technet.microsoft.com/virtualization/2017/01/27/introducing-the-host-compute-service-hcs/) (HCS) to launch and manage [Windows Containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/about/). It also contains other helpers and functions for managing Windows Containers such as the Golang interface for the Host Network Service (HNS).

It is primarily used in the [Moby Project](https://github.com/moby/moby), but it can be freely used by other projects as well.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Dependencies

This project requires Golang 1.9 or newer to build.

For system requirements to run this project, see the Microsoft docs on [Windows Container requirements](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/system-requirements).

## Reporting Security Issues

Security issues and bugs should be reported privately, via email, to the Microsoft Security
Response Center (MSRC) at [secure@microsoft.com](mailto:secure@microsoft.com). You should
receive a response within 24 hours. If for some reason you do not, please follow up via
email to ensure we received your original message. Further information, including the
[MSRC PGP](https://technet.microsoft.com/en-us/security/dn606155) key, can be found in
the [Security TechCenter](https://technet.microsoft.com/en-us/security/default).

For additional details, see [Report a Computer Security Vulnerability](https://technet.microsoft.com/en-us/security/ff852094.aspx) on Technet

---------------
Copyright (c) 2018 Microsoft Corp.  All rights reserved.
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
`storage` is a Go library which aims to provide methods for storing filesystem
layers, container images, and containers.  A `containers-storage` CLI wrapper
is also included for manual and scripting use.

To build the CLI wrapper, use 'make binary'.

Operations which use VMs expect to launch them using 'vagrant', defaulting to
using its 'libvirt' provider.  The boxes used are also available for the
'virtualbox' provider, and can be selected by setting $VAGRANT_PROVIDER to
'virtualbox' before kicking off the build.

The library manages three types of items: layers, images, and containers.

A *layer* is a copy-on-write filesystem which is notionally stored as a set of
changes relative to its *parent* layer, if it has one.  A given layer can only
have one parent, but any layer can be the parent of multiple layers.  Layers
which are parents of other layers should be treated as read-only.

An *image* is a reference to a particular layer (its _top_ layer), along with
other information which the library can manage for the convenience of its
caller.  This information typically includes configuration templates for
running a binary contained within the image's layers, and may include
cryptographic signatures.  Multiple images can reference the same layer, as the
differences between two images may not be in their layer contents.

A *container* is a read-write layer which is a child of an image's top layer,
along with information which the library can manage for the convenience of its
caller.  This information typically includes configuration information for
running the specific container.  Multiple containers can be derived from a
single image.

Layers, images, and containers are represented primarily by 32 character
hexadecimal IDs, but items of each kind can also have one or more arbitrary
names attached to them, which the library will automatically resolve to IDs
when they are passed in to API calls which expect IDs.

The library can store what it calls *metadata* for each of these types of
items.  This is expected to be a small piece of data, since it is cached in
memory and stored along with the library's own bookkeeping information.

Additionally, the library can store one or more of what it calls *big data* for
images and containers.  This is a named chunk of larger data, which is only in
memory when it is being read from or being written to its own disk file.

**[Contributing](CONTRIBUTING.md)**
Information about contributing to this project.
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

	"github.com/containers/storage/pkg/locker"
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

This code provides helper functions for dealing with archive files.
This package provides helper functions for dealing with strings
This package provides helper functions for dealing with string identifiers
# reexec

The `reexec` package facilitates the busybox style reexec of the docker binary that we require because 
of the forking limitations of using Go.  Handlers can be registered with a name and the argv 0 of 
the exec of the binary will be used to find and execute custom init paths.
[![GoDoc](https://godoc.org/github.com/containers/image?status.svg)](https://godoc.org/github.com/containers/image) [![Build Status](https://travis-ci.org/containers/image.svg?branch=master)](https://travis-ci.org/containers/image)
=

`image` is a set of Go libraries aimed at working in various way with
containers' images and container image registries.

The containers/image library allows application to pull and push images from
container image registries, like the upstream docker registry. It also
implements "simple image signing".

The containers/image library also allows you to inspect a repository on a
container registry without pulling down the image. This means it fetches the
repository's manifest and it is able to show you a `docker inspect`-like json
output about a whole repository or a tag. This library, in contrast to `docker
inspect`, helps you gather useful information about a repository or a tag
without requiring you to run `docker pull`.

The containers/image library also allows you to translate from one image format
to another, for example docker container images to OCI images. It also allows
you to copy container images between various registries, possibly converting
them as necessary, and to sign and verify images.

## Command-line usage

The containers/image project is only a library with no user interface;
you can either incorporate it into your Go programs, or use the `skopeo` tool:

The [skopeo](https://github.com/containers/skopeo) tool uses the
containers/image library and takes advantage of many of its features,
e.g. `skopeo copy` exposes the `containers/image/copy.Image` functionality.

## Dependencies

This library does not ship a committed version of its dependencies in a `vendor`
subdirectory.  This is so you can make well-informed decisions about which
libraries you should use with this package in your own projects, and because
types defined in the `vendor` directory would be impossible to use from your projects.

What this project tests against dependencies-wise is located
[in vendor.conf](https://github.com/containers/image/blob/master/vendor.conf).

## Building

If you want to see what the library can do, or an example of how it is called,
consider starting with the [skopeo](https://github.com/containers/skopeo) tool
instead.

To integrate this library into your project, put it into `$GOPATH` or use
your preferred vendoring tool to include a copy in your project.
Ensure that the dependencies documented [in vendor.conf](https://github.com/containers/image/blob/master/vendor.conf)
are also available
(using those exact versions or different versions of your choosing).

This library, by default, also depends on the GpgME and libostree C libraries. Either install them:
```sh
Fedora$ dnf install gpgme-devel libassuan-devel ostree-devel
macOS$ brew install gpgme
```
or use the build tags described below to avoid the dependencies (e.g. using `go build -tags …`)

### Supported build tags

- `containers_image_openpgp`: Use a Golang-only OpenPGP implementation for signature verification instead of the default cgo/gpgme-based implementation;
the primary downside is that creating new signatures with the Golang-only implementation is not supported.
- `containers_image_ostree_stub`: Instead of importing `ostree:` transport in `github.com/containers/image/transports/alltransports`, use a stub which reports that the transport is not supported. This allows building the library without requiring the `libostree` development libraries. The `github.com/containers/image/ostree` package is completely disabled
and impossible to import when this build tag is in use.

## [Contributing](CONTRIBUTING.md)**

Information about contributing to this project.

When developing this library, please use `make` (or `make … BUILDTAGS=…`) to take advantage of the tests and validation.

## License

Apache License 2.0

SPDX-License-Identifier: Apache-2.0

## Contact

- Mailing list: [containers-dev](https://groups.google.com/forum/?hl=en#!forum/containers-dev)
- IRC: #[container-projects](irc://irc.freenode.net:6667/#container-projects) on freenode.net
This package was replicated from [github.com/docker/docker v17.04.0-ce](https://github.com/docker/docker/tree/v17.04.0-ce/api/types/strslice).
This is a copy of github.com/docker/distribution/reference as of commit fb0bebc4b64e3881cc52a2478d749845ed76d2a8,
except that ParseAnyReferenceWithSet has been removed to drop the dependency on github.com/docker/distribution/digestset.![buildah logo](https://cdn.rawgit.com/containers/buildah/master/logos/buildah-logo_large.png)

# [Buildah](https://www.youtube.com/embed/YVk5NgSiUw8) - a tool that facilitates building [Open Container Initiative (OCI)](https://www.opencontainers.org/) container images

[![Go Report Card](https://goreportcard.com/badge/github.com/containers/buildah)](https://goreportcard.com/report/github.com/containers/buildah)
[![Travis](https://travis-ci.org/containers/buildah.svg?branch=master)](https://travis-ci.org/containers/buildah)

The Buildah package provides a command line tool that can be used to
* create a working container, either from scratch or using an image as a starting point
* create an image, either from a working container or via the instructions in a Dockerfile
* images can be built in either the OCI image format or the traditional upstream docker image format
* mount a working container's root filesystem for manipulation
* unmount a working container's root filesystem
* use the updated contents of a container's root filesystem as a filesystem layer to create a new image
* delete a working container or an image
* rename a local container

## Buildah Information for Developers

For blogs, release announcements and more, please checkout the [buildah.io](https://buildah.io) website!

**[Buildah Demos](demos)**

**[Changelog](CHANGELOG.md)**

**[Contributing](CONTRIBUTING.md)**

**[Development Plan](developmentplan.md)**

**[Installation notes](install.md)**

**[Troubleshooting Guide](troubleshooting.md)**

**[Tutorials](docs/tutorials)**

## Buildah and Podman relationship

Buildah and Podman are two complementary Open-source projects that are available on
most Linux platforms and both projects reside at [GitHub.com](https://github.com)
with Buildah [here](https://github.com/containers/buildah) and
Podman [here](https://github.com/containers/libpod).  Both Buildah and Podman are
command line tools that work on OCI images and containers.  The two projects
differentiate in their specialization.

Buildah specializes in building OCI images.  Buildah's commands replicate all
of the commands that are found in a Dockerfile. Buildah’s goal is also to
provide a lower level coreutils interface to build images, allowing people to build
containers without requiring a Dockerfile.  The intent with Buildah is to allow other
scripting languages to build container images, without requiring a daemon.

Podman specializes in all of the commands and functions that help you to maintain and modify
OCI images, such as pulling and tagging.  It also allows you to create, run, and maintain those containers
created from those images.

A major difference between Podman and Buildah is their concept of a container.  Podman
allows users to create "traditional containers" where the intent of these containers is
to be long lived.  While Buildah containers are really just created to allow content
to be added back to the container image.   An easy way to think of it is the
`buildah run` command emulates the RUN command in a Dockerfile while the `podman run`
command emulates the `docker run` command in functionality.  Because of this and their underlying
storage differences, you can not see Podman containers from within Buildah or vice versa.

In short Buildah is an efficient way to create OCI images  while Podman allows
you to manage and maintain those images and containers in a production environment using
familiar container cli commands.  For more details, see the
[Container Tools Guide](https://github.com/containers/buildah/tree/master/docs/containertools).

## Example

From [`./examples/lighttpd.sh`](examples/lighttpd.sh):

```bash
$ cat > lighttpd.sh <<"EOF"
#!/bin/bash -x

ctr1=`buildah from ${1:-fedora}`

## Get all updates and install our minimal httpd server
buildah run $ctr1 -- dnf update -y
buildah run $ctr1 -- dnf install -y lighttpd

## Include some buildtime annotations
buildah config --annotation "com.example.build.host=$(uname -n)" $ctr1

## Run our server and expose the port
buildah config --cmd "/usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf" $ctr1
buildah config --port 80 $ctr1

## Commit this container to an image name
buildah commit $ctr1 ${2:-$USER/lighttpd}
EOF

$ chmod +x lighttpd.sh
$ sudo ./lighttpd.sh
```

## Commands
| Command                                              | Description                                                                                          |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [buildah-add(1)](/docs/buildah-add.md)               | Add the contents of a file, URL, or a directory to the container.                                    |
| [buildah-bud(1)](/docs/buildah-bud.md)               | Build an image using instructions from Dockerfiles.                                                  |
| [buildah-commit(1)](/docs/buildah-commit.md)         | Create an image from a working container.                                                            |
| [buildah-config(1)](/docs/buildah-config.md)         | Update image configuration settings.                                                                 |
| [buildah-containers(1)](/docs/buildah-containers.md) | List the working containers and their base images.                                                   |
| [buildah-copy(1)](/docs/buildah-copy.md)             | Copies the contents of a file, URL, or directory into a container's working directory.               |
| [buildah-from(1)](/docs/buildah-from.md)             | Creates a new working container, either from scratch or using a specified image as a starting point. |
| [buildah-images(1)](/docs/buildah-images.md)         | List images in local storage.                                                                        |
| [buildah-info(1)](/docs/buildah-info.md)             | Display Buildah system information.                                                                  |
| [buildah-inspect(1)](/docs/buildah-inspect.md)       | Inspects the configuration of a container or image.                                                  |
| [buildah-mount(1)](/docs/buildah-mount.md)           | Mount the working container's root filesystem.                                                       |
| [buildah-pull(1)](/docs/buildah-pull.md)             | Pull an image from the specified location.                                                           |
| [buildah-push(1)](/docs/buildah-push.md)             | Push an image from local storage to elsewhere.                                                       |
| [buildah-rename(1)](/docs/buildah-rename.md)         | Rename a local container.                                                                            |
| [buildah-rm(1)](/docs/buildah-rm.md)                 | Removes one or more working containers.                                                              |
| [buildah-rmi(1)](/docs/buildah-rmi.md)               | Removes one or more images.                                                                          |
| [buildah-run(1)](/docs/buildah-run.md)               | Run a command inside of the container.                                                               |
| [buildah-tag(1)](/docs/buildah-tag.md)               | Add an additional name to a local image.                                                             |
| [buildah-umount(1)](/docs/buildah-umount.md)         | Unmount a working container's root file system.                                                      |
| [buildah-unshare(1)](/docs/buildah-unshare.md)       | Launch a command in a user namespace with modified ID mappings.                                      |
| [buildah-version(1)](/docs/buildah-version.md)       | Display the Buildah Version Information                                                              |

**Future goals include:**
* more CI tests
* additional CLI commands (?)
[![GoDoc](https://godoc.org/github.com/containers/psgo?status.svg)](https://godoc.org/github.com/containers/psgo) [![Build Status](https://travis-ci.org/containers/psgo.svg?branch=master)](https://travis-ci.org/containers/psgo)

# psgo
A ps(1) AIX-format compatible golang library extended with various descriptors useful for displaying container-related data.

The idea behind the library is to provide an easy to use way of extracting process-related data, just as ps(1) does. The problem when using ps(1) is that the ps format strings split columns with whitespaces, making the output nearly impossible to parse. It also adds some jitter as we have to fork and execute ps either in the container or filter the output afterwards, further limiting applicability.

This library aims to make things a bit more comfortable, especially for container runtimes, as the API allows to join the mount namespace of a given process and will parse `/proc` and `/dev/` from there. The API consists of the following functions:

 - `psgo.ProcessInfo(descriptors []string) ([][]string, error)`
   - ProcessInfo returns the process information of all processes in the current mount namespace. The input descriptors must be a slice of supported AIX format descriptors in the normal form or in the code form, if supported.  If the input descriptor slice is empty, the `psgo.DefaultDescriptors` are used. The return value contains the string slice of process data, one per process.

 - `psgo.ProcessInfoByPids(pids []string, descriptors []string) ([][]string, error)`
   - ProcessInfoByPids is similar to `psgo.ProcessInfo`, but limits the return value to a list of specified pids. The pids input must be a slice of PIDs for which process information should be returned. If the input descriptor slice is empty, only the format descriptor headers are returned.

 - `psgo.JoinNamespaceAndProcessInfo(pid string, descriptors []string) ([][]string, error)`
   - JoinNamespaceAndProcessInfo has the same semantics as ProcessInfo but joins the mount namespace of the specified pid before extracting data from /proc.  This way, we can extract the `/proc` data from a container without executing any command inside the container.

 - `psgo.JoinNamespaceAndProcessInfoByPids(pids []string, descriptors []string) ([][]string, error)`
   - JoinNamespaceAndProcessInfoByPids is similar to `psgo.JoinNamespaceAndProcessInfo` but takes a slice of pids as an argument.  To avoid duplicate entries (e.g., when two or more containers share the same PID namespace), a given PID namespace will be joined only once.

 - `psgo.ListDescriptors() []string`
   - ListDescriptors returns a sorted string slice of all supported AIX format descriptors in the normal form (e.g., "args,comm,user").  It can be useful in the context of bash-completion, help messages, etc.

### Listing processes
We can use the [psgo](https://github.com/containers/psgo/blob/master/sample/sample.go) sample tool from this project to test the core components of this library. First, let's build `psgo` via `make build`.  The binary is now located under `./bin/psgo`.  By default `psgo` displays data about all running processes in the current mount namespace, similar to the output of `ps -ef`.

```
$ ./bin/psgo | head -n5
USER         PID     PPID    %CPU     ELAPSED              TTY      TIME        COMMAND
root         1       0       0.064    6h3m27.677997443s    ?        13.98s      systemd
root         2       0       0.000    6h3m27.678380128s    ?        20ms        [kthreadd]
root         4       2       0.000    6h3m27.678701852s    ?        0s          [kworker/0:0H]
root         6       2       0.000    6h3m27.678999508s    ?        0s          [mm_percpu_wq]
```

### Listing processes
You can use the `--pids` flag to restrict `psgo` output to a subset of processes. This option accepts a list of comma separate process IDs and will return exactly the same kind of information per process as the default output.

```
$ ./bin/psgo --pids 1,$(pgrep bash | tr "\n" ",")
USER   PID     PPID    %CPU    ELAPSED                TTY     TIME   COMMAND
root   1       0       0.009   128h52m44.193475932s   ?       40s    systemd
root   20830   20827   0.000   105h2m44.19579679s     pts/5   0s     bash
root   25843   25840   0.000   102h56m4.196072027s    pts/6   0s     bash
```

### Listing processes within a container
Let's have a look at how we can use this library in the context of containers.  As a simple show case, we'll start a Docker container, extract the process ID via `docker-inspect` and run the `psgo` binary to extract the data of running processes within that container.

```shell
$ docker run -d alpine sleep 100
473c9a05d4223b88ef7f5a9ac11e3d21e9914e012338425cc1cef853fc6c32a2

$ docker inspect --format '{{.State.Pid}}' 473c9
5572

$ sudo ./bin/psgo -pids 5572 -join
USER   PID   PPID   %CPU    ELAPSED         TTY   TIME   COMMAND
root   1     0      0.000   17.249905587s   ?     0s     sleep
```

### Format descriptors
The ps library is compatible with all AIX format descriptors of the ps command-line utility (see `man 1 ps` for details) but it also supports some additional descriptors that can be useful when seeking specific process-related information.

- **capamb**
  - Set of ambient capabilities. See capabilities(7) for more information.
- **capbnd**
  - Set of bounding capabilities. See capabilities(7) for more information.
- **capeff**
  - Set of effective capabilities. See capabilities(7) for more information.
- **capinh**
  - Set of inheritable capabilities. See capabilities(7) for more information.
- **capprm**
  - Set of permitted capabilities. See capabilities(7) for more information.
- **hgroup**
  - The corresponding effective group of a container process on the host.
- **hpid**
  - The corresponding host PID of a container process.
- **huser**
  - The corresponding effective user of a container process on the host.
- **label**
  - Current security attributes of the process.
- **seccomp**
  - Seccomp mode of the process (i.e., disabled, strict or filter). See seccomp(2) for more information.
- **state**
  - Process state codes (e.g, **R** for *running*, **S** for *sleeping*). See proc(5) for more information.

We can try out different format descriptors with the psgo binary:

```shell
$ ./bin/psgo -format "pid, user, group, seccomp" | head -n5
PID     USER         GROUP        SECCOMP
1       root         root         disabled
2       root         root         disabled
4       root         root         disabled
6       root         root         disabled
```
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

# Deepcopier

[![Build Status](https://secure.travis-ci.org/ulule/deepcopier.png?branch=master)](http://travis-ci.org/ulule/deepcopier)

This package is meant to make copying of structs to/from others structs a bit easier.

## Installation

```bash
go get -u github.com/ulule/deepcopier
```

## Usage

```golang
// Deep copy instance1 into instance2
Copy(instance1).To(instance2)

// Deep copy instance1 into instance2 and passes the following context (which
// is basically a map[string]interface{}) as first argument
// to methods of instance2 that defined the struct tag "context".
Copy(instance1).WithContext(map[string]interface{}{"foo": "bar"}).To(instance2)

// Deep copy instance2 into instance1
Copy(instance1).From(instance2)

// Deep copy instance2 into instance1 and passes the following context (which
// is basically a map[string]interface{}) as first argument
// to methods of instance1 that defined the struct tag "context".
Copy(instance1).WithContext(map[string]interface{}{"foo": "bar"}).From(instance2)
```

Available options for `deepcopier` struct tag:

| Option    | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| `field`   | Field or method name in source instance                              |
| `skip`    | Ignores the field                                                    |
| `context` | Takes a `map[string]interface{}` as first argument (for methods)     |
| `force`   | Set the value of a `sql.Null*` field (instead of copying the struct) |

**Options example:**

```golang
type Source struct {
    Name                         string
    SkipMe                       string
    SQLNullStringToSQLNullString sql.NullString
    SQLNullStringToString        sql.NullString

}

func (Source) MethodThatTakesContext(c map[string]interface{}) string {
    return "whatever"
}

type Destination struct {
    FieldWithAnotherNameInSource      string         `deepcopier:"field:Name"`
    SkipMe                            string         `deepcopier:"skip"`
    MethodThatTakesContext            string         `deepcopier:"context"`
    SQLNullStringToSQLNullString      sql.NullString 
    SQLNullStringToString             string         `deepcopier:"force"`
}

```

Example:

```golang
package main

import (
    "fmt"
 
    "github.com/ulule/deepcopier"
)

// Model
type User struct {
    // Basic string field
    Name  string
    // Deepcopier supports https://golang.org/pkg/database/sql/driver/#Valuer
    Email sql.NullString
}

func (u *User) MethodThatTakesContext(ctx map[string]interface{}) string {
    // do whatever you want
    return "hello from this method"
}

// Resource
type UserResource struct {
    DisplayName            string `deepcopier:"field:Name"`
    SkipMe                 string `deepcopier:"skip"`
    MethodThatTakesContext string `deepcopier:"context"`
    Email                  string `deepcopier:"force"`

}

func main() {
    user := &User{
        Name: "gilles",
        Email: sql.NullString{
            Valid: true,
            String: "gilles@example.com",
        },
    }

    resource := &UserResource{}

    deepcopier.Copy(user).To(resource)

    fmt.Println(resource.DisplayName)
    fmt.Println(resource.Email)
}
```

Looking for more information about the usage?

We wrote [an introduction article](https://github.com/ulule/deepcopier/blob/master/examples/rest-usage/README.rst).
Have a look and feel free to give us your feedback.

## Contributing

* Ping us on twitter [@oibafsellig](https://twitter.com/oibafsellig), [@thoas](https://twitter.com/thoas)
* Fork the [project](https://github.com/ulule/deepcopier)
* Help us improving and fixing [issues](https://github.com/ulule/deepcopier/issues)

Don't hesitate ;)
Protocol Buffers for Go with Gadgets

GoGoProtobuf http://github.com/gogo/protobuf extends
GoProtobuf http://github.com/golang/protobuf

Copyright (c) 2013, The GoGo Authors. All rights reserved.


# Go support for Protocol Buffers

Google's data interchange format.
Copyright 2010 The Go Authors.
https://github.com/golang/protobuf

This package and the code it generates requires at least Go 1.6.

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

## Packages and input paths ##

The protocol buffer language has a concept of "packages" which does not
correspond well to the Go notion of packages. In generated Go code,
each source `.proto` file is associated with a single Go package. The
name and import path for this package is specified with the `go_package`
proto option:

	option go_package = "github.com/gogo/protobuf/types";

The protocol buffer compiler will attempt to derive a package name and
import path if a `go_package` option is not present, but it is
best to always specify one explicitly.

There is a one-to-one relationship between source `.proto` files and
generated `.pb.go` files, but any number of `.pb.go` files may be
contained in the same Go package.

The output name of a generated file is produced by replacing the
`.proto` suffix with `.pb.go` (e.g., `foo.proto` produces `foo.pb.go`).
However, the output directory is selected in one of two ways.  Let
us say we have `inputs/x.proto` with a `go_package` option of
`github.com/golang/protobuf/p`. The corresponding output file may
be:

- Relative to the import path:

	protoc --gogo_out=. inputs/x.proto
	# writes ./github.com/gogo/protobuf/p/x.pb.go

  (This can work well with `--gogo_out=$GOPATH`.)

- Relative to the input file:

	protoc --gogo_out=paths=source_relative:. inputs/x.proto
	# generate ./inputs/x.pb.go

## Generated code ##

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
  - Enum types do not get an Enum method.

Consider file test.proto, containing

```proto
	syntax = "proto2";
	package example;

	enum FOO { X = 17; };

	message Test {
	  required string label = 1;
	  optional int32 type = 2 [default=77];
	  repeated int64 reps = 3;
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
		test := &example.Test{
			Label: proto.String("hello"),
			Type:  proto.Int32(17),
			Reps:  []int64{1, 2, 3},
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

- `paths=(import | source_relative)` - specifies how the paths of
  generated files are structured. See the "Packages and imports paths"
  section above. The default is `import`.
- `plugins=plugin1+plugin2` - specifies the list of sub-plugins to
  load. The only plugin in this repo is `grpc`.
- `Mfoo/bar.proto=quux/shme` - declares that foo/bar.proto is
  associated with Go package quux/shme.  This is subject to the
  import_prefix parameter.

The following parameters are deprecated and should not be used:

- `import_prefix=xxx` - a prefix that is added onto the beginning of
  all imports.
- `import_path=foo/bar` - used as the package if no input files
  declare `go_package`. If it contains slashes, everything up to the
  rightmost slash is ignored.

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

The `protoc-gen-go/generator` package exposes a plugin interface,
which is used by the gRPC code generation. This interface is not
supported and is subject to incompatible changes without notice.
# go-dockerclient

[![Travis Build Status](https://travis-ci.org/fsouza/go-dockerclient.svg?branch=master)](https://travis-ci.org/fsouza/go-dockerclient)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/4m374pti06ubg2l7?svg=true)](https://ci.appveyor.com/project/fsouza/go-dockerclient)
[![GoDoc](https://img.shields.io/badge/api-Godoc-blue.svg?style=flat-square)](https://godoc.org/github.com/fsouza/go-dockerclient)

This package presents a client for the Docker remote API. It also provides
support for the extensions in the [Swarm API](https://docs.docker.com/swarm/swarm-api/).

This package also provides support for docker's network API, which is a simple
passthrough to the libnetwork remote API.  Note that docker's network API is
only available in docker 1.8 and above, and only enabled in docker if
DOCKER_EXPERIMENTAL is defined during the docker build process.

For more details, check the [remote API
documentation](http://docs.docker.com/engine/reference/api/docker_remote_api/).

## Example

```go
package main

import (
	"fmt"

	"github.com/fsouza/go-dockerclient"
)

func main() {
	endpoint := "unix:///var/run/docker.sock"
	client, err := docker.NewClient(endpoint)
	if err != nil {
		panic(err)
	}
	imgs, err := client.ListImages(docker.ListImagesOptions{All: false})
	if err != nil {
		panic(err)
	}
	for _, img := range imgs {
		fmt.Println("ID: ", img.ID)
		fmt.Println("RepoTags: ", img.RepoTags)
		fmt.Println("Created: ", img.Created)
		fmt.Println("Size: ", img.Size)
		fmt.Println("VirtualSize: ", img.VirtualSize)
		fmt.Println("ParentId: ", img.ParentID)
	}
}
```

## Using with TLS

In order to instantiate the client for a TLS-enabled daemon, you should use
NewTLSClient, passing the endpoint and path for key and certificates as
parameters.

```go
package main

import (
	"fmt"

	"github.com/fsouza/go-dockerclient"
)

func main() {
	endpoint := "tcp://[ip]:[port]"
	path := os.Getenv("DOCKER_CERT_PATH")
	ca := fmt.Sprintf("%s/ca.pem", path)
	cert := fmt.Sprintf("%s/cert.pem", path)
	key := fmt.Sprintf("%s/key.pem", path)
	client, _ := docker.NewTLSClient(endpoint, cert, key, ca)
	// use client
}
```

If using [docker-machine](https://docs.docker.com/machine/), or another
application that exports environment variables `DOCKER_HOST`,
`DOCKER_TLS_VERIFY`, `DOCKER_CERT_PATH`, you can use NewClientFromEnv.


```go
package main

import (
	"fmt"

	"github.com/fsouza/go-dockerclient"
)

func main() {
	client, _ := docker.NewClientFromEnv()
	// use client
}
```

See the documentation for more details.

## Developing

All development commands can be seen in the [Makefile](Makefile).

Commited code must pass:

* [golint](https://github.com/golang/lint) (with some exceptions, see the Makefile).
* [go vet](https://golang.org/cmd/vet/)
* [gofmt](https://golang.org/cmd/gofmt)
* [go test](https://golang.org/cmd/go/#hdr-Test_packages)

Running `make test` will check all of these. If your editor does not
automatically call ``gofmt -s``, `make fmt` will format all go files in this
repository.

## Vendoring

go-dockerclient uses [dep](https://github.com/golang/dep/) for vendoring. If
you're using dep, you should be able to pick go-dockerclient releases and get
the proper dependencies.

With other vendoring tools, users might need to specify go-dockerclient's
dependencies manually.

## Using with Docker 1.9 and Go 1.4

There's a tag for using go-dockerclient with Docker 1.9 (which requires
compiling go-dockerclient with Go 1.4), the tag name is ``docker-1.9/go-1.4``.

The instructions below can be used to get a version of go-dockerclient that compiles with Go 1.4:

```
% git clone -b docker-1.9/go-1.4 https://github.com/fsouza/go-dockerclient.git $GOPATH/src/github.com/fsouza/go-dockerclient
% git clone -b v1.9.1 https://github.com/docker/docker.git $GOPATH/src/github.com/docker/docker
% go get github.com/fsouza/go-dockerclient
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

// TestSomethingElse is a second example of how to use our test object to
// make assertions about some target code we are testing.
// This time using a placeholder. Placeholders might be used when the
// data being passed in is normally dynamically generated and cannot be
// predicted beforehand (eg. containing hashes that are time sensitive)
func TestSomethingElse(t *testing.T) {

  // create an instance of our test object
  testObj := new(MyMockedObject)

  // setup expectations with a placeholder in the argument list
  testObj.On("DoSomething", mock.Anything).Return(true, nil)

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
    github.com/stretchr/testify/require
    github.com/stretchr/testify/mock
    github.com/stretchr/testify/suite
    github.com/stretchr/testify/http (deprecated)

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

Supported go versions
==================

We support the three major Go versions, which are 1.9, 1.10, and 1.11 at the moment.

------

Contributing
============

Please feel free to submit issues, fork the repository and send pull requests!

When submitting an issue, we ask that you please include a complete test function that demonstrates the issue.  Extra credit for those using Testify to write the test code that demonstrates it.

------

License
=======

This project is licensed under the terms of the MIT license.
# tar-split

[![Build Status](https://travis-ci.org/vbatts/tar-split.svg?branch=master)](https://travis-ci.org/vbatts/tar-split)
[![Go Report Card](https://goreportcard.com/badge/github.com/vbatts/tar-split)](https://goreportcard.com/report/github.com/vbatts/tar-split)

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
is not something I seek to fix immediately, but would rather have an alert that
precise reassembly is not possible.
(see more http://www.gnu.org/software/tar/manual/html_node/Sparse-Formats.html)


Other caveat, while tar archives support having multiple file entries for the
same path, we will not support this feature. If there are more than one entries
with the same path, expect an err (like `ErrDuplicatePath`) or a resulting tar
stream that does not validate your original checksum/signature.

## Contract

Do not break the API of stdlib `archive/tar` in our fork (ideally find an upstream mergeable solution).

## Std Version

The version of golang stdlib `archive/tar` is from go1.11
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

# Go Wrapper for ZFS #

Simple wrappers for ZFS command line tools.

[![GoDoc](https://godoc.org/github.com/mistifyio/go-zfs?status.svg)](https://godoc.org/github.com/mistifyio/go-zfs)

## Requirements ##

You need a working ZFS setup.  To use on Ubuntu 14.04, setup ZFS:

    sudo apt-get install python-software-properties
    sudo apt-add-repository ppa:zfs-native/stable
    sudo apt-get update
    sudo apt-get install ubuntu-zfs libzfs-dev

Developed using Go 1.3, but currently there isn't anything 1.3 specific. Don't use Ubuntu packages for Go, use http://golang.org/doc/install

Generally you need root privileges to use anything zfs related.

## Status ##

This has been only been tested on Ubuntu 14.04

In the future, we hope to work directly with libzfs.

# Hacking #

The tests have decent examples for most functions.

```go
//assuming a zpool named test
//error handling ommitted


f, err := zfs.CreateFilesystem("test/snapshot-test", nil)
ok(t, err)

s, err := f.Snapshot("test", nil)
ok(t, err)

// snapshot is named "test/snapshot-test@test"

c, err := s.Clone("test/clone-test", nil)

err := c.Destroy()
err := s.Destroy()
err := f.Destroy()

```

# Contributing #

See the [contributing guidelines](./CONTRIBUTING.md)

# GPGME (golang)

Go wrapper for the GPGME library.

This library is intended for use with desktop applications. If you are looking to add OpenPGP support to a server application I suggest you first look at [golang.org/x/crypto/openpgp](https://godoc.org/golang.org/x/crypto/openpgp).

## Installation

    go get -u github.com/proglottis/gpgme

## Documentation

* [godoc](https://godoc.org/github.com/proglottis/gpgme)
# Open Container Initiative Runtime Specification

The [Open Container Initiative][oci] develops specifications for standards on Operating System process and application containers.

The specification can be found [here](spec.md).

## Table of Contents

Additional documentation about how this group operates:

- [Code of Conduct][code-of-conduct]
- [Style and Conventions](style.md)
- [Implementations](implementations.md)
- [Releases](RELEASES.md)
- [project](project.md)
- [charter][charter]

## Use Cases

To provide context for users the following section gives example use cases for each part of the spec.

### Application Bundle Builders

Application bundle builders can create a [bundle](bundle.md) directory that includes all of the files required for launching an application as a container.
The bundle contains an OCI [configuration file](config.md) where the builder can specify host-independent details such as [which executable to launch](config.md#process) and host-specific settings such as [mount](config.md#mounts) locations, [hook](config.md#posix-platform-hooks) paths, Linux [namespaces](config-linux.md#namespaces) and [cgroups](config-linux.md#control-groups).
Because the configuration includes host-specific settings, application bundle directories copied between two hosts may require configuration adjustments.

### Hook Developers

[Hook](config.md#posix-platform-hooks) developers can extend the functionality of an OCI-compliant runtime by hooking into a container's lifecycle with an external application.
Example use cases include sophisticated network configuration, volume garbage collection, etc.

### Runtime Developers

Runtime developers can build runtime implementations that run OCI-compliant bundles and container configuration, containing low-level OS and host-specific details, on a particular platform.

## Contributing

Development happens on GitHub for the spec.
Issues are used for bugs and actionable items and longer discussions can happen on the [mailing list](#mailing-list).

The specification and code is licensed under the Apache 2.0 license found in the [LICENSE](./LICENSE) file.

### Discuss your design

The project welcomes submissions, but please let everyone know what you are working on.

Before undertaking a nontrivial change to this specification, send mail to the [mailing list](#mailing-list) to discuss what you plan to do.
This gives everyone a chance to validate the design, helps prevent duplication of effort, and ensures that the idea fits.
It also guarantees that the design is sound before code is written; a GitHub pull-request is not the place for high-level discussions.

Typos and grammatical errors can go straight to a pull-request.
When in doubt, start on the [mailing-list](#mailing-list).

### Meetings

The contributors and maintainers of all OCI projects have monthly meetings, which are usually at 2:00 PM (USA Pacific) on the first Wednesday of every month.
There is an [iCalendar][rfc5545] format for the meetings [here](meeting.ics).
Everyone is welcome to participate via [UberConference web][uberconference] or audio-only: +1 415 968 0849 (no PIN needed).
An initial agenda will be posted to the [mailing list](#mailing-list) in the week before each meeting, and everyone is welcome to propose additional topics or suggest other agenda alterations there.
Minutes are posted to the [mailing list](#mailing-list) and minutes from past calls are archived [here][minutes], with minutes from especially old meetings (September 2015 and earlier) archived [here][runtime-wiki].

### Mailing List

You can subscribe and join the mailing list on [Google Groups][dev-list].

### IRC

OCI discussion happens on #opencontainers on Freenode ([logs][irc-logs]).

### Git commit

#### Sign your work

The sign-off is a simple line at the end of the explanation for the patch, which certifies that you wrote it or otherwise have the right to pass it on as an open-source patch.
The rules are pretty simple: if you can certify the below (from http://developercertificate.org):

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

#### Commit Style

Simple house-keeping for clean git history.
Read more on [How to Write a Git Commit Message][how-to-git-commit] or the Discussion section of [git-commit(1)][git-commit.1].

1. Separate the subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how
    * If there was important/useful/essential conversation or information, copy or include a reference
8. When possible, one keyword to scope the change in the subject (i.e. "README: ...", "runtime: ...")


[charter]: https://www.opencontainers.org/about/governance
[code-of-conduct]: https://github.com/opencontainers/tob/blob/master/code-of-conduct.md
[dev-list]: https://groups.google.com/a/opencontainers.org/forum/#!forum/dev
[how-to-git-commit]: http://chris.beams.io/posts/git-commit
[irc-logs]: http://ircbot.wl.linuxfoundation.org/eavesdrop/%23opencontainers/
[iso-week]: https://en.wikipedia.org/wiki/ISO_week_date#Calculating_the_week_number_of_a_given_date
[minutes]: http://ircbot.wl.linuxfoundation.org/meetings/opencontainers/
[oci]: https://www.opencontainers.org
[rfc5545]: https://tools.ietf.org/html/rfc5545
[runtime-wiki]: https://github.com/opencontainers/runtime-spec/wiki
[uberconference]: https://www.uberconference.com/opencontainers

[git-commit.1]: http://git-scm.com/docs/git-commit
# runc

[![Build Status](https://travis-ci.org/opencontainers/runc.svg?branch=master)](https://travis-ci.org/opencontainers/runc)
[![Go Report Card](https://goreportcard.com/badge/github.com/opencontainers/runc)](https://goreportcard.com/report/github.com/opencontainers/runc)
[![GoDoc](https://godoc.org/github.com/opencontainers/runc?status.svg)](https://godoc.org/github.com/opencontainers/runc)

## Introduction

`runc` is a CLI tool for spawning and running containers according to the OCI specification.

## Releases

`runc` depends on and tracks the [runtime-spec](https://github.com/opencontainers/runtime-spec) repository.
We will try to make sure that `runc` and the OCI specification major versions stay in lockstep.
This means that `runc` 1.0.0 should implement the 1.0 version of the specification.

You can find official releases of `runc` on the [release](https://github.com/opencontainers/runc/releases) page.

### Security

If you wish to report a security issue, please disclose the issue responsibly
to security@opencontainers.org.

## Building

`runc` currently supports the Linux platform with various architecture support.
It must be built with Go version 1.6 or higher in order for some features to function properly.

In order to enable seccomp support you will need to install `libseccomp` on your platform.
> e.g. `libseccomp-devel` for CentOS, or `libseccomp-dev` for Ubuntu

Otherwise, if you do not want to build `runc` with seccomp support you can add `BUILDTAGS=""` when running make.

```bash
# create a 'github.com/opencontainers' in your GOPATH/src
cd github.com/opencontainers
git clone https://github.com/opencontainers/runc
cd runc

make
sudo make install
```

You can also use `go get` to install to your `GOPATH`, assuming that you have a `github.com` parent folder already created under `src`:

```bash
go get github.com/opencontainers/runc
cd $GOPATH/src/github.com/opencontainers/runc
make
sudo make install
```

`runc` will be installed to `/usr/local/sbin/runc` on your system.


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
| apparmor  | apparmor profile support           | <none>      |
| ambient   | ambient capability support         | kernel 4.3  |
| nokmem    | disable kernel memory account      | <none>      |


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

You can run a specific integration test by setting the `TESTPATH` variable.

```bash
# make test TESTPATH="/checkpoint.bats"
```

You can run a test in your proxy environment by setting `DOCKER_BUILD_PROXY` and `DOCKER_RUN_PROXY` variables.

```bash
# make test DOCKER_BUILD_PROXY="--build-arg HTTP_PROXY=http://yourproxy/" DOCKER_RUN_PROXY="-e HTTP_PROXY=http://yourproxy/"
```

### Dependencies Management

`runc` uses [vndr](https://github.com/LK4D4/vndr) for dependencies management.
Please refer to [vndr](https://github.com/LK4D4/vndr) for how to add or update
new dependencies.

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
# run as root
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
                "capabilities": {
                        "bounding": [
                                "CAP_AUDIT_WRITE",
                                "CAP_KILL",
                                "CAP_NET_BIND_SERVICE"
                        ],
                        "effective": [
                                "CAP_AUDIT_WRITE",
                                "CAP_KILL",
                                "CAP_NET_BIND_SERVICE"
                        ],
                        "inheritable": [
                                "CAP_AUDIT_WRITE",
                                "CAP_KILL",
                                "CAP_NET_BIND_SERVICE"
                        ],
                        "permitted": [
                                "CAP_AUDIT_WRITE",
                                "CAP_KILL",
                                "CAP_NET_BIND_SERVICE"
                        ],
                        "ambient": [
                                "CAP_AUDIT_WRITE",
                                "CAP_KILL",
                                "CAP_NET_BIND_SERVICE"
                        ]
                },
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

Now we can go through the lifecycle operations in your shell.


```bash
# run as root
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

This allows higher level systems to augment the containers creation logic with setup of various settings after the container is created and/or before it is deleted. For example, the container's network stack is commonly set up after `create` but before `start`.

#### Rootless containers
`runc` has the ability to run containers without root privileges. This is called `rootless`. You need to pass some parameters to `runc` in order to run rootless containers. See below and compare with the previous version. Run the following commands as an ordinary user:
```bash
# Same as the first example
mkdir ~/mycontainer
cd ~/mycontainer
mkdir rootfs
docker export $(docker create busybox) | tar -C rootfs -xvf -

# The --rootless parameter instructs runc spec to generate a configuration for a rootless container, which will allow you to run the container as a non-root user.
runc spec --rootless

# The --root parameter tells runc where to store the container state. It must be writable by the user.
runc --root /tmp/runc run mycontainerid
```

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

## License

The code and docs are released under the [Apache 2.0 license](LICENSE).
# libcontainer

[![GoDoc](https://godoc.org/github.com/opencontainers/runc/libcontainer?status.svg)](https://godoc.org/github.com/opencontainers/runc/libcontainer)

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

In addition to the go init function the early stage bootstrap is handled by importing
[nsenter](https://github.com/opencontainers/runc/blob/master/libcontainer/nsenter/README.md).

```go
import (
	_ "github.com/opencontainers/runc/libcontainer/nsenter"
)

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
defaultMountFlags := unix.MS_NOEXEC | unix.MS_NOSUID | unix.MS_NODEV
config := &configs.Config{
	Rootfs: "/your/path/to/rootfs",
	Capabilities: &configs.Capabilities{
                Bounding: []string{
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
                Effective: []string{
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
                Inheritable: []string{
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
                Permitted: []string{
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
                Ambient: []string{
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
        },
	Namespaces: configs.Namespaces([]configs.Namespace{
		{Type: configs.NEWNS},
		{Type: configs.NEWUTS},
		{Type: configs.NEWIPC},
		{Type: configs.NEWPID},
		{Type: configs.NEWUSER},
		{Type: configs.NEWNET},
		{Type: configs.NEWCGROUP},
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
			Flags:       unix.MS_NOSUID | unix.MS_STRICTATIME,
			Data:        "mode=755",
		},
		{
			Source:      "devpts",
			Destination: "/dev/pts",
			Device:      "devpts",
			Flags:       unix.MS_NOSUID | unix.MS_NOEXEC,
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
			Flags:       defaultMountFlags | unix.MS_RDONLY,
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
			Type: unix.RLIMIT_NOFILE,
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

// get current status of the container.
status, err := container.Status()

// get current container's state information.
state, err := container.State()
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

Code and documentation copyright 2014 Docker, inc.
The code and documentation are released under the [Apache 2.0 license](../LICENSE).
The documentation is also released under Creative Commons Attribution 4.0 International License.
You may obtain a copy of the license, titled CC-BY-4.0, at http://creativecommons.org/licenses/by/4.0/.
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
called. And package `nsenter` is only imported in `init.go`, so every time the runc
`init` command is invoked, that C code is run.

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
`CLONE_NEW*` clone flags because we must fork a new process in order to
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

Please DO NOT file a public issue, instead send your report privately to
security@opencontainers.org.

The maintainers take security seriously. If you discover a security issue,
please bring it to their attention right away!

If you are reporting a security issue, do not create an issue or file a pull
request on GitHub. Instead, disclose the issue responsibly by sending an email
to security@opencontainers.org (which is inhabited only by the maintainers of
the various OCI projects).

# Copyright and license

Copyright © 2016 Docker, Inc. All rights reserved, except as follows. Code is released under the [Apache 2.0 license](LICENSE). This `README.md` file and the [`CONTRIBUTING.md`](CONTRIBUTING.md) file are licensed under the Creative Commons Attribution 4.0 International License under the terms and conditions set forth in the file [`LICENSE.docs`](LICENSE.docs). You may obtain a duplicate copy of the same license, titled CC BY-SA 4.0, at http://creativecommons.org/licenses/by-sa/4.0/.
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
# oci-runtime-tool [![Build Status](https://travis-ci.org/opencontainers/runtime-tools.svg?branch=master)](https://travis-ci.org/opencontainers/runtime-tools) [![Go Report Card](https://goreportcard.com/badge/github.com/opencontainers/runtime-tools)](https://goreportcard.com/report/github.com/opencontainers/runtime-tools)

oci-runtime-tool is a collection of tools for working with the [OCI runtime specification][runtime-spec].
To build from source code, runtime-tools requires Go 1.7.x or above.

## Generating an OCI runtime spec configuration files

[`oci-runtime-tool generate`][generate.1] generates [configuration JSON][config.json] for an [OCI bundle][bundle].
[OCI-compatible runtimes][runtime-spec] like [runC][] expect to read the configuration from `config.json`.

```console
$ oci-runtime-tool generate --output config.json
$ cat config.json
{
        "ociVersion": "0.5.0",
        …
}
```

## Validating an OCI bundle

[`oci-runtime-tool validate`][validate.1] validates an OCI bundle.
The error message will be printed if the OCI bundle failed the validation procedure.

```console
$ oci-runtime-tool generate
$ oci-runtime-tool validate
INFO[0000] Bundle validation succeeded.
```

## Testing OCI runtimes

The runtime validation suite uses [node-tap][], which is packaged for some distributions (for example, it is in [Debian's `node-tap` package][debian-node-tap]).
If your distribution does not package node-tap, you can install [npm][] (for example, from [Gentoo's `nodejs` package][gentoo-nodejs]) and use it:

```console
$ npm install tap
```

Build the validation executables:

```console
$ make runtimetest validation-executables
```

Runtime validation currently [only supports](docs/runtime-compliance-testing.md) the [OCI Runtime Command Line Interface](docs/command-line-interface.md).
If we add support for alternative APIs in the future, runtime validation will gain an option to select the desired runtime API.
For the command line interface, the `RUNTIME` option selects the runtime command (`funC` in the [OCI Runtime Command Line Interface](docs/command-line-interface.md)).

```
$ sudo make RUNTIME=runc localvalidation
RUNTIME=runc tap validation/pidfile.t validation/linux_cgroups_hugetlb.t validation/linux_cgroups_memory.t validation/linux_rootfs_propagation_shared.t validation/kill.t validation/create.t validation/poststart.t validation/linux_cgroups_network.t validation/poststop_fail.t validation/linux_readonly_paths.t validation/prestart_fail.t validation/hooks_stdin.t validation/default.t validation/linux_masked_paths.t validation/poststop.t validation/misc_props.t validation/prestart.t validation/poststart_fail.t validation/mounts.t validation/linux_cgroups_relative_pids.t validation/process_user.t validation/process.t validation/hooks.t validation/process_capabilities_fail.t validation/process_rlimits_fail.t validation/linux_cgroups_relative_cpus.t validation/process_rlimits.t validation/linux_cgroups_relative_blkio.t validation/linux_sysctl.t validation/linux_seccomp.t validation/linux_devices.t validation/start.t validation/linux_cgroups_pids.t validation/process_capabilities.t validation/process_oom_score_adj.t validation/linux_cgroups_relative_hugetlb.t validation/linux_cgroups_cpus.t validation/linux_cgroups_relative_memory.t validation/state.t validation/root_readonly_true.t validation/linux_cgroups_blkio.t validation/linux_rootfs_propagation_unbindable.t validation/delete.t validation/linux_cgroups_relative_network.t validation/hostname.t validation/killsig.t validation/linux_uid_mappings.t
validation/pidfile.t .failed to create the container
container_linux.go:348: starting container process caused "process_linux.go:402: container init caused \"process_linux.go:367: setting cgroup config for procHooks process caused \\\"failed to write 56892210544640 to hugetlb.1GB.limit_in_bytes: open /sys/fs/cgroup/hugetlb/cgrouptest/hugetlb.1GB.limit_in_bytes: permission denied\\\"\""
exit status 1
validation/pidfile.t .................................. 1/1 315ms
validation/linux_cgroups_hugetlb.t .................... 0/1
  not ok validation/linux_cgroups_hugetlb.t
    timeout: 30000
    file: validation/linux_cgroups_hugetlb.t
    command: validation/linux_cgroups_hugetlb.t
    args: []
    stdio:
      - 0
      - pipe
      - 2
    cwd: /…/go/src/github.com/opencontainers/runtime-tools
    exitCode: 1

validation/linux_cgroups_memory.t ..................... 9/9
validation/linux_rootfs_propagation_shared.t ...... 252/282
  not ok shared root propagation exposes "/target348456609/mount892511628/example376408222"

  Skipped: 29
     /dev/null (default device) has unconfigured permissions
…
total ........................................... 4381/4962


  4381 passing (1m)
  567 pending
  14 failing

make: *** [Makefile:44: localvalidation] Error 1
```

You can also run an individual test executable directly:

```console
$ sudo RUNTIME=runc validation/default/default.t
TAP version 13
ok 1 - has expected hostname
  ---
  {
    "actual": "mrsdalloway",
    "expected": "mrsdalloway"
  }
  ...
…
ok 287 # SKIP linux.gidMappings not set
1..287
```

If you cannot install node-tap, you can probably run the test suite with another [TAP consumer][tap-consumers].
For example, with [`prove`][prove]:

```console
$ sudo make TAP='prove -Q -j9' RUNTIME=runc VALIDATION_TESTS=validation/pidfile/pidfile.t localvalidation
RUNTIME=runc prove -Q -j9 validation/pidfile.t
All tests successful.
Files=1, Tests=1,  0 wallclock secs ( 0.01 usr  0.01 sys +  0.03 cusr  0.03 csys =  0.08 CPU)
Result: PASS
```

[bundle]: https://github.com/opencontainers/runtime-spec/blob/master/bundle.md
[config.json]: https://github.com/opencontainers/runtime-spec/blob/master/config.md
[debian-node-tap]: https://packages.debian.org/stretch/node-tap
[debian-nodejs]: https://packages.debian.org/stretch/nodejs
[gentoo-nodejs]: https://packages.gentoo.org/packages/net-libs/nodejs
[node-tap]: http://www.node-tap.org/
[npm]: https://www.npmjs.com/
[prove]: http://search.cpan.org/~leont/Test-Harness-3.39/bin/prove
[runC]: https://github.com/opencontainers/runc
[runtime-spec]: https://github.com/opencontainers/runtime-spec
[tap-consumers]: https://testanything.org/consumers.html

[generate.1]: man/oci-runtime-tool-generate.1.md
[validate.1]: man/oci-runtime-tool-validate.1.md
# selinux

[![GoDoc](https://godoc.org/github.com/opencontainers/selinux?status.svg)](https://godoc.org/github.com/opencontainers/selinux) [![Go Report Card](https://goreportcard.com/badge/github.com/opencontainers/selinux)](https://goreportcard.com/report/github.com/opencontainers/selinux) [![Build Status](https://travis-ci.org/opencontainers/selinux.svg?branch=master)](https://travis-ci.org/opencontainers/selinux)

Common SELinux package used across the container ecosystem.

Please see the [godoc](https://godoc.org/github.com/opencontainers/selinux) for more information.
# fileutils

Collection of utilities for file manipulation in golang

The library is based on docker pkg/archive pkg/idtools but does copies instead of handling archive formats.
cli
===

[![Build Status](https://travis-ci.org/urfave/cli.svg?branch=master)](https://travis-ci.org/urfave/cli)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/rtgk5xufi932pb2v?svg=true)](https://ci.appveyor.com/project/urfave/cli)
[![GoDoc](https://godoc.org/github.com/urfave/cli?status.svg)](https://godoc.org/github.com/urfave/cli)
[![codebeat](https://codebeat.co/badges/0a8f30aa-f975-404b-b878-5fab3ae1cc5f)](https://codebeat.co/projects/github-com-urfave-cli)
[![Go Report Card](https://goreportcard.com/badge/urfave/cli)](https://goreportcard.com/report/urfave/cli)
[![top level coverage](https://gocover.io/_badge/github.com/urfave/cli?0 "top level coverage")](http://gocover.io/github.com/urfave/cli) /
[![altsrc coverage](https://gocover.io/_badge/github.com/urfave/cli/altsrc?0 "altsrc coverage")](http://gocover.io/github.com/urfave/cli/altsrc)

This is the library formerly known as `github.com/codegangsta/cli` -- Github
will automatically redirect requests to this repository, but we recommend
updating your references for clarity.

cli is a simple, fast, and fun package for building command line apps in Go. The
goal is to enable developers to write fast and distributable command line
applications in an expressive way.

<!-- toc -->

- [Overview](#overview)
- [Installation](#installation)
  * [Supported platforms](#supported-platforms)
  * [Using the `v2` branch](#using-the-v2-branch)
  * [Pinning to the `v1` releases](#pinning-to-the-v1-releases)
- [Getting Started](#getting-started)
- [Examples](#examples)
  * [Arguments](#arguments)
  * [Flags](#flags)
    + [Placeholder Values](#placeholder-values)
    + [Alternate Names](#alternate-names)
    + [Ordering](#ordering)
    + [Values from the Environment](#values-from-the-environment)
    + [Values from files](#values-from-files)
    + [Values from alternate input sources (YAML, TOML, and others)](#values-from-alternate-input-sources-yaml-toml-and-others)
    + [Precedence](#precedence)
  * [Subcommands](#subcommands)
  * [Subcommands categories](#subcommands-categories)
  * [Exit code](#exit-code)
  * [Bash Completion](#bash-completion)
    + [Enabling](#enabling)
    + [Distribution](#distribution)
    + [Customization](#customization)
  * [Generated Help Text](#generated-help-text)
    + [Customization](#customization-1)
  * [Version Flag](#version-flag)
    + [Customization](#customization-2)
    + [Full API Example](#full-api-example)
  * [Combining short Bool options](#combining-short-bool-options)
- [Contribution Guidelines](#contribution-guidelines)

<!-- tocstop -->

## Overview

Command line apps are usually so tiny that there is absolutely no reason why
your code should *not* be self-documenting. Things like generating help text and
parsing command flags/options should not hinder productivity when writing a
command line app.

**This is where cli comes into play.** cli makes command line programming fun,
organized, and expressive!

## Installation

Make sure you have a working Go environment.  Go version 1.2+ is supported.  [See
the install instructions for Go](http://golang.org/doc/install.html).

To install cli, simply run:
```
$ go get github.com/urfave/cli
```

Make sure your `PATH` includes the `$GOPATH/bin` directory so your commands can
be easily used:
```
export PATH=$PATH:$GOPATH/bin
```

### Supported platforms

cli is tested against multiple versions of Go on Linux, and against the latest
released version of Go on OS X and Windows.  For full details, see
[`./.travis.yml`](./.travis.yml) and [`./appveyor.yml`](./appveyor.yml).

### Using the `v2` branch

**Warning**: The `v2` branch is currently unreleased and considered unstable.

There is currently a long-lived branch named `v2` that is intended to land as
the new `master` branch once development there has settled down.  The current
`master` branch (mirrored as `v1`) is being manually merged into `v2` on
an irregular human-based schedule, but generally if one wants to "upgrade" to
`v2` *now* and accept the volatility (read: "awesomeness") that comes along with
that, please use whatever version pinning of your preference, such as via
`gopkg.in`:

```
$ go get gopkg.in/urfave/cli.v2
```

``` go
...
import (
  "gopkg.in/urfave/cli.v2" // imports as package "cli"
)
...
```

### Pinning to the `v1` releases

Similarly to the section above describing use of the `v2` branch, if one wants
to avoid any unexpected compatibility pains once `v2` becomes `master`, then
pinning to `v1` is an acceptable option, e.g.:

```
$ go get gopkg.in/urfave/cli.v1
```

``` go
...
import (
  "gopkg.in/urfave/cli.v1" // imports as package "cli"
)
...
```

This will pull the latest tagged `v1` release (e.g. `v1.18.1` at the time of writing).

## Getting Started

One of the philosophies behind cli is that an API should be playful and full of
discovery. So a cli app can be as little as one line of code in `main()`.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "A new cli application"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  err := cli.NewApp().Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

This app will run and show help text, but is not very useful. Let's give an
action to execute and some help documentation:

<!-- {
  "output": "boom! I say!"
} -->
``` go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()
  app.Name = "boom"
  app.Usage = "make an explosive entrance"
  app.Action = func(c *cli.Context) error {
    fmt.Println("boom! I say!")
    return nil
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Running this already gives you a ton of functionality, plus support for things
like subcommands and flags, which are covered below.

## Examples

Being a programmer can be a lonely job. Thankfully by the power of automation
that is not the case! Let's create a greeter app to fend off our demons of
loneliness!

Start by creating a directory named `greet`, and within it, add a file,
`greet.go` with the following code in it:

<!-- {
  "output": "Hello friend!"
} -->
``` go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()
  app.Name = "greet"
  app.Usage = "fight the loneliness!"
  app.Action = func(c *cli.Context) error {
    fmt.Println("Hello friend!")
    return nil
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Install our command to the `$GOPATH/bin` directory:

```
$ go install
```

Finally run our new command:

```
$ greet
Hello friend!
```

cli also generates neat help text:

```
$ greet help
NAME:
    greet - fight the loneliness!

USAGE:
    greet [global options] command [command options] [arguments...]

VERSION:
    0.0.0

COMMANDS:
    help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS
    --version Shows version information
```

### Arguments

You can lookup arguments by calling the `Args` function on `cli.Context`, e.g.:

<!-- {
  "output": "Hello \""
} -->
``` go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Action = func(c *cli.Context) error {
    fmt.Printf("Hello %q", c.Args().Get(0))
    return nil
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

### Flags

Setting and querying flags is simple.

<!-- {
  "output": "Hello Nefertiti"
} -->
``` go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang",
      Value: "english",
      Usage: "language for the greeting",
    },
  }

  app.Action = func(c *cli.Context) error {
    name := "Nefertiti"
    if c.NArg() > 0 {
      name = c.Args().Get(0)
    }
    if c.String("lang") == "spanish" {
      fmt.Println("Hola", name)
    } else {
      fmt.Println("Hello", name)
    }
    return nil
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

You can also set a destination variable for a flag, to which the content will be
scanned.

<!-- {
  "output": "Hello someone"
} -->
``` go
package main

import (
  "log"
  "os"
  "fmt"

  "github.com/urfave/cli"
)

func main() {
  var language string

  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name:        "lang",
      Value:       "english",
      Usage:       "language for the greeting",
      Destination: &language,
    },
  }

  app.Action = func(c *cli.Context) error {
    name := "someone"
    if c.NArg() > 0 {
      name = c.Args()[0]
    }
    if language == "spanish" {
      fmt.Println("Hola", name)
    } else {
      fmt.Println("Hello", name)
    }
    return nil
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

See full list of flags at http://godoc.org/github.com/urfave/cli

#### Placeholder Values

Sometimes it's useful to specify a flag's value within the usage string itself.
Such placeholders are indicated with back quotes.

For example this:

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "&#45;&#45;config FILE, &#45;c FILE"
} -->
```go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag{
    cli.StringFlag{
      Name:  "config, c",
      Usage: "Load configuration from `FILE`",
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Will result in help output like:

```
--config FILE, -c FILE   Load configuration from FILE
```

Note that only the first placeholder is used. Subsequent back-quoted words will
be left as-is.

#### Alternate Names

You can set alternate (or short) names for flags by providing a comma-delimited
list for the `Name`. e.g.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "&#45;&#45;lang value, &#45;l value.*language for the greeting.*default: \"english\""
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "language for the greeting",
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

That flag can then be set with `--lang spanish` or `-l spanish`. Note that
giving two different forms of the same flag in the same command invocation is an
error.

#### Ordering

Flags for the application and commands are shown in the order they are defined.
However, it's possible to sort them from outside this library by using `FlagsByName`
or `CommandsByName` with `sort`.

For example this:

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "add a task to the list\n.*complete a task on the list\n.*\n\n.*\n.*Load configuration from FILE\n.*Language for the greeting.*"
} -->
``` go
package main

import (
  "log"
  "os"
  "sort"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "Language for the greeting",
    },
    cli.StringFlag{
      Name: "config, c",
      Usage: "Load configuration from `FILE`",
    },
  }

  app.Commands = []cli.Command{
    {
      Name:    "complete",
      Aliases: []string{"c"},
      Usage:   "complete a task on the list",
      Action:  func(c *cli.Context) error {
        return nil
      },
    },
    {
      Name:    "add",
      Aliases: []string{"a"},
      Usage:   "add a task to the list",
      Action:  func(c *cli.Context) error {
        return nil
      },
    },
  }

  sort.Sort(cli.FlagsByName(app.Flags))
  sort.Sort(cli.CommandsByName(app.Commands))

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Will result in help output like:

```
--config FILE, -c FILE  Load configuration from FILE
--lang value, -l value  Language for the greeting (default: "english")
```

#### Values from the Environment

You can also have the default value set from the environment via `EnvVar`.  e.g.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "language for the greeting.*APP_LANG"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "language for the greeting",
      EnvVar: "APP_LANG",
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

The `EnvVar` may also be given as a comma-delimited "cascade", where the first
environment variable that resolves is used as the default.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "language for the greeting.*LEGACY_COMPAT_LANG.*APP_LANG.*LANG"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "language for the greeting",
      EnvVar: "LEGACY_COMPAT_LANG,APP_LANG,LANG",
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

#### Values from files

You can also have the default value set from file via `FilePath`.  e.g.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "password for the mysql database"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "password, p",
      Usage: "password for the mysql database",
      FilePath: "/etc/mysql/password",
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Note that default values set from file (e.g. `FilePath`) take precedence over
default values set from the enviornment (e.g. `EnvVar`).

#### Values from alternate input sources (YAML, TOML, and others)

There is a separate package altsrc that adds support for getting flag values
from other file input sources.

Currently supported input source formats:
* YAML
* TOML

In order to get values for a flag from an alternate input source the following
code would be added to wrap an existing cli.Flag like below:

``` go
  altsrc.NewIntFlag(cli.IntFlag{Name: "test"})
```

Initialization must also occur for these flags. Below is an example initializing
getting data from a yaml file below.

``` go
  command.Before = altsrc.InitInputSourceWithContext(command.Flags, NewYamlSourceFromFlagFunc("load"))
```

The code above will use the "load" string as a flag name to get the file name of
a yaml file from the cli.Context.  It will then use that file name to initialize
the yaml input source for any flags that are defined on that command.  As a note
the "load" flag used would also have to be defined on the command flags in order
for this code snipped to work.

Currently only YAML and JSON files are supported but developers can add support
for other input sources by implementing the altsrc.InputSourceContext for their
given sources.

Here is a more complete sample of a command using YAML support:

<!-- {
  "args": ["test-cmd", "&#45;&#45;help"],
  "output": "&#45&#45;test value.*default: 0"
} -->
``` go
package notmain

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
  "github.com/urfave/cli/altsrc"
)

func main() {
  app := cli.NewApp()

  flags := []cli.Flag{
    altsrc.NewIntFlag(cli.IntFlag{Name: "test"}),
    cli.StringFlag{Name: "load"},
  }

  app.Action = func(c *cli.Context) error {
    fmt.Println("yaml ist rad")
    return nil
  }

  app.Before = altsrc.InitInputSourceWithContext(flags, altsrc.NewYamlSourceFromFlagFunc("load"))
  app.Flags = flags

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

#### Precedence

The precedence for flag value sources is as follows (highest to lowest):

0. Command line flag value from user
0. Environment variable (if specified)
0. Configuration file (if specified)
0. Default defined on the flag

### Subcommands

Subcommands can be defined for a more git-like command line app.

<!-- {
  "args": ["template", "add"],
  "output": "new task template: .+"
} -->
```go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Commands = []cli.Command{
    {
      Name:    "add",
      Aliases: []string{"a"},
      Usage:   "add a task to the list",
      Action:  func(c *cli.Context) error {
        fmt.Println("added task: ", c.Args().First())
        return nil
      },
    },
    {
      Name:    "complete",
      Aliases: []string{"c"},
      Usage:   "complete a task on the list",
      Action:  func(c *cli.Context) error {
        fmt.Println("completed task: ", c.Args().First())
        return nil
      },
    },
    {
      Name:        "template",
      Aliases:     []string{"t"},
      Usage:       "options for task templates",
      Subcommands: []cli.Command{
        {
          Name:  "add",
          Usage: "add a new template",
          Action: func(c *cli.Context) error {
            fmt.Println("new task template: ", c.Args().First())
            return nil
          },
        },
        {
          Name:  "remove",
          Usage: "remove an existing template",
          Action: func(c *cli.Context) error {
            fmt.Println("removed task template: ", c.Args().First())
            return nil
          },
        },
      },
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

### Subcommands categories

For additional organization in apps that have many subcommands, you can
associate a category for each command to group them together in the help
output.

E.g.

```go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Commands = []cli.Command{
    {
      Name: "noop",
    },
    {
      Name:     "add",
      Category: "Template actions",
    },
    {
      Name:     "remove",
      Category: "Template actions",
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Will include:

```
COMMANDS:
    noop

  Template actions:
    add
    remove
```

### Exit code

Calling `App.Run` will not automatically call `os.Exit`, which means that by
default the exit code will "fall through" to being `0`.  An explicit exit code
may be set by returning a non-nil error that fulfills `cli.ExitCoder`, *or* a
`cli.MultiError` that includes an error that fulfills `cli.ExitCoder`, e.g.:

``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()
  app.Flags = []cli.Flag{
    cli.BoolTFlag{
      Name:  "ginger-crouton",
      Usage: "is it in the soup?",
    },
  }
  app.Action = func(ctx *cli.Context) error {
    if !ctx.Bool("ginger-crouton") {
      return cli.NewExitError("it is not in the soup", 86)
    }
    return nil
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

### Bash Completion

You can enable completion commands by setting the `EnableBashCompletion`
flag on the `App` object.  By default, this setting will only auto-complete to
show an app's subcommands, but you can write your own completion methods for
the App or its subcommands.

<!-- {
  "args": ["complete", "&#45;&#45;generate&#45;bash&#45;completion"],
  "output": "laundry"
} -->
``` go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  tasks := []string{"cook", "clean", "laundry", "eat", "sleep", "code"}

  app := cli.NewApp()
  app.EnableBashCompletion = true
  app.Commands = []cli.Command{
    {
      Name:  "complete",
      Aliases: []string{"c"},
      Usage: "complete a task on the list",
      Action: func(c *cli.Context) error {
         fmt.Println("completed task: ", c.Args().First())
         return nil
      },
      BashComplete: func(c *cli.Context) {
        // This will complete if no args are passed
        if c.NArg() > 0 {
          return
        }
        for _, t := range tasks {
          fmt.Println(t)
        }
      },
    },
  }

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

#### Enabling

Source the `autocomplete/bash_autocomplete` file in your `.bashrc` file while
setting the `PROG` variable to the name of your program:

`PROG=myprogram source /.../cli/autocomplete/bash_autocomplete`

#### Distribution

Copy `autocomplete/bash_autocomplete` into `/etc/bash_completion.d/` and rename
it to the name of the program you wish to add autocomplete support for (or
automatically install it there if you are distributing a package). Don't forget
to source the file to make it active in the current shell.

```
sudo cp src/bash_autocomplete /etc/bash_completion.d/<myprogram>
source /etc/bash_completion.d/<myprogram>
```

Alternatively, you can just document that users should source the generic
`autocomplete/bash_autocomplete` in their bash configuration with `$PROG` set
to the name of their program (as above).

#### Customization

The default bash completion flag (`--generate-bash-completion`) is defined as
`cli.BashCompletionFlag`, and may be redefined if desired, e.g.:

<!-- {
  "args": ["&#45;&#45;compgen"],
  "output": "wat\nhelp\nh"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.BashCompletionFlag = cli.BoolFlag{
    Name:   "compgen",
    Hidden: true,
  }

  app := cli.NewApp()
  app.EnableBashCompletion = true
  app.Commands = []cli.Command{
    {
      Name: "wat",
    },
  }
  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

### Generated Help Text

The default help flag (`-h/--help`) is defined as `cli.HelpFlag` and is checked
by the cli internals in order to print generated help text for the app, command,
or subcommand, and break execution.

#### Customization

All of the help text generation may be customized, and at multiple levels.  The
templates are exposed as variables `AppHelpTemplate`, `CommandHelpTemplate`, and
`SubcommandHelpTemplate` which may be reassigned or augmented, and full override
is possible by assigning a compatible func to the `cli.HelpPrinter` variable,
e.g.:

<!-- {
  "output": "Ha HA.  I pwnd the help!!1"
} -->
``` go
package main

import (
  "fmt"
  "log"
  "io"
  "os"

  "github.com/urfave/cli"
)

func main() {
  // EXAMPLE: Append to an existing template
  cli.AppHelpTemplate = fmt.Sprintf(`%s

WEBSITE: http://awesometown.example.com

SUPPORT: support@awesometown.example.com

`, cli.AppHelpTemplate)

  // EXAMPLE: Override a template
  cli.AppHelpTemplate = `NAME:
   {{.Name}} - {{.Usage}}
USAGE:
   {{.HelpName}} {{if .VisibleFlags}}[global options]{{end}}{{if .Commands}} command [command options]{{end}} {{if .ArgsUsage}}{{.ArgsUsage}}{{else}}[arguments...]{{end}}
   {{if len .Authors}}
AUTHOR:
   {{range .Authors}}{{ . }}{{end}}
   {{end}}{{if .Commands}}
COMMANDS:
{{range .Commands}}{{if not .HideHelp}}   {{join .Names ", "}}{{ "\t"}}{{.Usage}}{{ "\n" }}{{end}}{{end}}{{end}}{{if .VisibleFlags}}
GLOBAL OPTIONS:
   {{range .VisibleFlags}}{{.}}
   {{end}}{{end}}{{if .Copyright }}
COPYRIGHT:
   {{.Copyright}}
   {{end}}{{if .Version}}
VERSION:
   {{.Version}}
   {{end}}
`

  // EXAMPLE: Replace the `HelpPrinter` func
  cli.HelpPrinter = func(w io.Writer, templ string, data interface{}) {
    fmt.Println("Ha HA.  I pwnd the help!!1")
  }

  err := cli.NewApp().Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

The default flag may be customized to something other than `-h/--help` by
setting `cli.HelpFlag`, e.g.:

<!-- {
  "args": ["&#45;&#45halp"],
  "output": "haaaaalp.*HALP"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.HelpFlag = cli.BoolFlag{
    Name: "halp, haaaaalp",
    Usage: "HALP",
    EnvVar: "SHOW_HALP,HALPPLZ",
  }

  err := cli.NewApp().Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

### Version Flag

The default version flag (`-v/--version`) is defined as `cli.VersionFlag`, which
is checked by the cli internals in order to print the `App.Version` via
`cli.VersionPrinter` and break execution.

#### Customization

The default flag may be customized to something other than `-v/--version` by
setting `cli.VersionFlag`, e.g.:

<!-- {
  "args": ["&#45;&#45print-version"],
  "output": "partay version 19\\.99\\.0"
} -->
``` go
package main

import (
  "log"
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.VersionFlag = cli.BoolFlag{
    Name: "print-version, V",
    Usage: "print only the version",
  }

  app := cli.NewApp()
  app.Name = "partay"
  app.Version = "19.99.0"
  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

Alternatively, the version printer at `cli.VersionPrinter` may be overridden, e.g.:

<!-- {
  "args": ["&#45;&#45version"],
  "output": "version=19\\.99\\.0 revision=fafafaf"
} -->
``` go
package main

import (
  "fmt"
  "log"
  "os"

  "github.com/urfave/cli"
)

var (
  Revision = "fafafaf"
)

func main() {
  cli.VersionPrinter = func(c *cli.Context) {
    fmt.Printf("version=%s revision=%s\n", c.App.Version, Revision)
  }

  app := cli.NewApp()
  app.Name = "partay"
  app.Version = "19.99.0"
  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}
```

#### Full API Example

**Notice**: This is a contrived (functioning) example meant strictly for API
demonstration purposes.  Use of one's imagination is encouraged.

<!-- {
  "output": "made it!\nPhew!"
} -->
``` go
package main

import (
  "errors"
  "flag"
  "fmt"
  "io"
  "io/ioutil"
  "os"
  "time"

  "github.com/urfave/cli"
)

func init() {
  cli.AppHelpTemplate += "\nCUSTOMIZED: you bet ur muffins\n"
  cli.CommandHelpTemplate += "\nYMMV\n"
  cli.SubcommandHelpTemplate += "\nor something\n"

  cli.HelpFlag = cli.BoolFlag{Name: "halp"}
  cli.BashCompletionFlag = cli.BoolFlag{Name: "compgen", Hidden: true}
  cli.VersionFlag = cli.BoolFlag{Name: "print-version, V"}

  cli.HelpPrinter = func(w io.Writer, templ string, data interface{}) {
    fmt.Fprintf(w, "best of luck to you\n")
  }
  cli.VersionPrinter = func(c *cli.Context) {
    fmt.Fprintf(c.App.Writer, "version=%s\n", c.App.Version)
  }
  cli.OsExiter = func(c int) {
    fmt.Fprintf(cli.ErrWriter, "refusing to exit %d\n", c)
  }
  cli.ErrWriter = ioutil.Discard
  cli.FlagStringer = func(fl cli.Flag) string {
    return fmt.Sprintf("\t\t%s", fl.GetName())
  }
}

type hexWriter struct{}

func (w *hexWriter) Write(p []byte) (int, error) {
  for _, b := range p {
    fmt.Printf("%x", b)
  }
  fmt.Printf("\n")

  return len(p), nil
}

type genericType struct{
  s string
}

func (g *genericType) Set(value string) error {
  g.s = value
  return nil
}

func (g *genericType) String() string {
  return g.s
}

func main() {
  app := cli.NewApp()
  app.Name = "kənˈtrīv"
  app.Version = "19.99.0"
  app.Compiled = time.Now()
  app.Authors = []cli.Author{
    cli.Author{
      Name:  "Example Human",
      Email: "human@example.com",
    },
  }
  app.Copyright = "(c) 1999 Serious Enterprise"
  app.HelpName = "contrive"
  app.Usage = "demonstrate available API"
  app.UsageText = "contrive - demonstrating the available API"
  app.ArgsUsage = "[args and such]"
  app.Commands = []cli.Command{
    cli.Command{
      Name:        "doo",
      Aliases:     []string{"do"},
      Category:    "motion",
      Usage:       "do the doo",
      UsageText:   "doo - does the dooing",
      Description: "no really, there is a lot of dooing to be done",
      ArgsUsage:   "[arrgh]",
      Flags: []cli.Flag{
        cli.BoolFlag{Name: "forever, forevvarr"},
      },
      Subcommands: cli.Commands{
        cli.Command{
          Name:   "wop",
          Action: wopAction,
        },
      },
      SkipFlagParsing: false,
      HideHelp:        false,
      Hidden:          false,
      HelpName:        "doo!",
      BashComplete: func(c *cli.Context) {
        fmt.Fprintf(c.App.Writer, "--better\n")
      },
      Before: func(c *cli.Context) error {
        fmt.Fprintf(c.App.Writer, "brace for impact\n")
        return nil
      },
      After: func(c *cli.Context) error {
        fmt.Fprintf(c.App.Writer, "did we lose anyone?\n")
        return nil
      },
      Action: func(c *cli.Context) error {
        c.Command.FullName()
        c.Command.HasName("wop")
        c.Command.Names()
        c.Command.VisibleFlags()
        fmt.Fprintf(c.App.Writer, "dodododododoodododddooooododododooo\n")
        if c.Bool("forever") {
          c.Command.Run(c)
        }
        return nil
      },
      OnUsageError: func(c *cli.Context, err error, isSubcommand bool) error {
        fmt.Fprintf(c.App.Writer, "for shame\n")
        return err
      },
    },
  }
  app.Flags = []cli.Flag{
    cli.BoolFlag{Name: "fancy"},
    cli.BoolTFlag{Name: "fancier"},
    cli.DurationFlag{Name: "howlong, H", Value: time.Second * 3},
    cli.Float64Flag{Name: "howmuch"},
    cli.GenericFlag{Name: "wat", Value: &genericType{}},
    cli.Int64Flag{Name: "longdistance"},
    cli.Int64SliceFlag{Name: "intervals"},
    cli.IntFlag{Name: "distance"},
    cli.IntSliceFlag{Name: "times"},
    cli.StringFlag{Name: "dance-move, d"},
    cli.StringSliceFlag{Name: "names, N"},
    cli.UintFlag{Name: "age"},
    cli.Uint64Flag{Name: "bigage"},
  }
  app.EnableBashCompletion = true
  app.HideHelp = false
  app.HideVersion = false
  app.BashComplete = func(c *cli.Context) {
    fmt.Fprintf(c.App.Writer, "lipstick\nkiss\nme\nlipstick\nringo\n")
  }
  app.Before = func(c *cli.Context) error {
    fmt.Fprintf(c.App.Writer, "HEEEERE GOES\n")
    return nil
  }
  app.After = func(c *cli.Context) error {
    fmt.Fprintf(c.App.Writer, "Phew!\n")
    return nil
  }
  app.CommandNotFound = func(c *cli.Context, command string) {
    fmt.Fprintf(c.App.Writer, "Thar be no %q here.\n", command)
  }
  app.OnUsageError = func(c *cli.Context, err error, isSubcommand bool) error {
    if isSubcommand {
      return err
    }

    fmt.Fprintf(c.App.Writer, "WRONG: %#v\n", err)
    return nil
  }
  app.Action = func(c *cli.Context) error {
    cli.DefaultAppComplete(c)
    cli.HandleExitCoder(errors.New("not an exit coder, though"))
    cli.ShowAppHelp(c)
    cli.ShowCommandCompletions(c, "nope")
    cli.ShowCommandHelp(c, "also-nope")
    cli.ShowCompletions(c)
    cli.ShowSubcommandHelp(c)
    cli.ShowVersion(c)

    categories := c.App.Categories()
    categories.AddCommand("sounds", cli.Command{
      Name: "bloop",
    })

    for _, category := range c.App.Categories() {
      fmt.Fprintf(c.App.Writer, "%s\n", category.Name)
      fmt.Fprintf(c.App.Writer, "%#v\n", category.Commands)
      fmt.Fprintf(c.App.Writer, "%#v\n", category.VisibleCommands())
    }

    fmt.Printf("%#v\n", c.App.Command("doo"))
    if c.Bool("infinite") {
      c.App.Run([]string{"app", "doo", "wop"})
    }

    if c.Bool("forevar") {
      c.App.RunAsSubcommand(c)
    }
    c.App.Setup()
    fmt.Printf("%#v\n", c.App.VisibleCategories())
    fmt.Printf("%#v\n", c.App.VisibleCommands())
    fmt.Printf("%#v\n", c.App.VisibleFlags())

    fmt.Printf("%#v\n", c.Args().First())
    if len(c.Args()) > 0 {
      fmt.Printf("%#v\n", c.Args()[1])
    }
    fmt.Printf("%#v\n", c.Args().Present())
    fmt.Printf("%#v\n", c.Args().Tail())

    set := flag.NewFlagSet("contrive", 0)
    nc := cli.NewContext(c.App, set, c)

    fmt.Printf("%#v\n", nc.Args())
    fmt.Printf("%#v\n", nc.Bool("nope"))
    fmt.Printf("%#v\n", nc.BoolT("nerp"))
    fmt.Printf("%#v\n", nc.Duration("howlong"))
    fmt.Printf("%#v\n", nc.Float64("hay"))
    fmt.Printf("%#v\n", nc.Generic("bloop"))
    fmt.Printf("%#v\n", nc.Int64("bonk"))
    fmt.Printf("%#v\n", nc.Int64Slice("burnks"))
    fmt.Printf("%#v\n", nc.Int("bips"))
    fmt.Printf("%#v\n", nc.IntSlice("blups"))
    fmt.Printf("%#v\n", nc.String("snurt"))
    fmt.Printf("%#v\n", nc.StringSlice("snurkles"))
    fmt.Printf("%#v\n", nc.Uint("flub"))
    fmt.Printf("%#v\n", nc.Uint64("florb"))
    fmt.Printf("%#v\n", nc.GlobalBool("global-nope"))
    fmt.Printf("%#v\n", nc.GlobalBoolT("global-nerp"))
    fmt.Printf("%#v\n", nc.GlobalDuration("global-howlong"))
    fmt.Printf("%#v\n", nc.GlobalFloat64("global-hay"))
    fmt.Printf("%#v\n", nc.GlobalGeneric("global-bloop"))
    fmt.Printf("%#v\n", nc.GlobalInt("global-bips"))
    fmt.Printf("%#v\n", nc.GlobalIntSlice("global-blups"))
    fmt.Printf("%#v\n", nc.GlobalString("global-snurt"))
    fmt.Printf("%#v\n", nc.GlobalStringSlice("global-snurkles"))

    fmt.Printf("%#v\n", nc.FlagNames())
    fmt.Printf("%#v\n", nc.GlobalFlagNames())
    fmt.Printf("%#v\n", nc.GlobalIsSet("wat"))
    fmt.Printf("%#v\n", nc.GlobalSet("wat", "nope"))
    fmt.Printf("%#v\n", nc.NArg())
    fmt.Printf("%#v\n", nc.NumFlags())
    fmt.Printf("%#v\n", nc.Parent())

    nc.Set("wat", "also-nope")

    ec := cli.NewExitError("ohwell", 86)
    fmt.Fprintf(c.App.Writer, "%d", ec.ExitCode())
    fmt.Printf("made it!\n")
    return nil
  }

  if os.Getenv("HEXY") != "" {
    app.Writer = &hexWriter{}
    app.ErrWriter = &hexWriter{}
  }

  app.Metadata = map[string]interface{}{
    "layers":     "many",
    "explicable": false,
    "whatever-values": 19.99,
  }


  // ignore error so we don't exit non-zero and break gfmrun README example tests
  _ = app.Run(os.Args)
}

func wopAction(c *cli.Context) error {
  fmt.Fprintf(c.App.Writer, ":wave: over here, eh\n")
  return nil
}
```

### Combining short Bool options

Traditional use of boolean options using their shortnames look like this:
```
# cmd foobar -s -o
```

Suppose you want users to be able to combine your bool options with their shortname.  This
can be done using the **UseShortOptionHandling** bool in your commands.  Suppose your program
has a two bool flags such as *serve* and *option* with the short options of *-o* and
*-s* respectively. With **UseShortOptionHandling** set to *true*, a user can use a syntax
like:
```
# cmd foobar -so
```

If you enable the **UseShortOptionHandling*, then you must not use any flags that have a single
leading *-* or this will result in failures.  For example, **-option** can no longer be used.  Flags
with two leading dashes (such as **--options**) are still valid.

## Contribution Guidelines

See [./CONTRIBUTING.md](./CONTRIBUTING.md)
# gorilla/mux

[![GoDoc](https://godoc.org/github.com/gorilla/mux?status.svg)](https://godoc.org/github.com/gorilla/mux)
[![Build Status](https://travis-ci.org/gorilla/mux.svg?branch=master)](https://travis-ci.org/gorilla/mux)
[![Sourcegraph](https://sourcegraph.com/github.com/gorilla/mux/-/badge.svg)](https://sourcegraph.com/github.com/gorilla/mux?badge)

![Gorilla Logo](http://www.gorillatoolkit.org/static/images/gorilla-icon-64.png)

http://www.gorillatoolkit.org/pkg/mux

Package `gorilla/mux` implements a request router and dispatcher for matching incoming requests to
their respective handler.

The name mux stands for "HTTP request multiplexer". Like the standard `http.ServeMux`, `mux.Router` matches incoming requests against a list of registered routes and calls a handler for the route that matches the URL or other conditions. The main features are:

* It implements the `http.Handler` interface so it is compatible with the standard `http.ServeMux`.
* Requests can be matched based on URL host, path, path prefix, schemes, header and query values, HTTP methods or using custom matchers.
* URL hosts, paths and query values can have variables with an optional regular expression.
* Registered URLs can be built, or "reversed", which helps maintaining references to resources.
* Routes can be used as subrouters: nested routes are only tested if the parent route matches. This is useful to define groups of routes that share common conditions like a host, a path prefix or other repeated attributes. As a bonus, this optimizes request matching.

---

* [Install](#install)
* [Examples](#examples)
* [Matching Routes](#matching-routes)
* [Static Files](#static-files)
* [Registered URLs](#registered-urls)
* [Walking Routes](#walking-routes)
* [Graceful Shutdown](#graceful-shutdown)
* [Middleware](#middleware)
* [Testing Handlers](#testing-handlers)
* [Full Example](#full-example)

---

## Install

With a [correctly configured](https://golang.org/doc/install#testing) Go toolchain:

```sh
go get -u github.com/gorilla/mux
```

## Examples

Let's start registering a couple of URL paths and handlers:

```go
func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", HomeHandler)
    r.HandleFunc("/products", ProductsHandler)
    r.HandleFunc("/articles", ArticlesHandler)
    http.Handle("/", r)
}
```

Here we register three routes mapping URL paths to handlers. This is equivalent to how `http.HandleFunc()` works: if an incoming request URL matches one of the paths, the corresponding handler is called passing (`http.ResponseWriter`, `*http.Request`) as parameters.

Paths can have variables. They are defined using the format `{name}` or `{name:pattern}`. If a regular expression pattern is not defined, the matched variable will be anything until the next slash. For example:

```go
r := mux.NewRouter()
r.HandleFunc("/products/{key}", ProductHandler)
r.HandleFunc("/articles/{category}/", ArticlesCategoryHandler)
r.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler)
```

The names are used to create a map of route variables which can be retrieved calling `mux.Vars()`:

```go
func ArticlesCategoryHandler(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    w.WriteHeader(http.StatusOK)
    fmt.Fprintf(w, "Category: %v\n", vars["category"])
}
```

And this is all you need to know about the basic usage. More advanced options are explained below.

### Matching Routes

Routes can also be restricted to a domain or subdomain. Just define a host pattern to be matched. They can also have variables:

```go
r := mux.NewRouter()
// Only matches if domain is "www.example.com".
r.Host("www.example.com")
// Matches a dynamic subdomain.
r.Host("{subdomain:[a-z]+}.domain.com")
```

There are several other matchers that can be added. To match path prefixes:

```go
r.PathPrefix("/products/")
```

...or HTTP methods:

```go
r.Methods("GET", "POST")
```

...or URL schemes:

```go
r.Schemes("https")
```

...or header values:

```go
r.Headers("X-Requested-With", "XMLHttpRequest")
```

...or query values:

```go
r.Queries("key", "value")
```

...or to use a custom matcher function:

```go
r.MatcherFunc(func(r *http.Request, rm *RouteMatch) bool {
    return r.ProtoMajor == 0
})
```

...and finally, it is possible to combine several matchers in a single route:

```go
r.HandleFunc("/products", ProductsHandler).
  Host("www.example.com").
  Methods("GET").
  Schemes("http")
```

Routes are tested in the order they were added to the router. If two routes match, the first one wins:

```go
r := mux.NewRouter()
r.HandleFunc("/specific", specificHandler)
r.PathPrefix("/").Handler(catchAllHandler)
```

Setting the same matching conditions again and again can be boring, so we have a way to group several routes that share the same requirements. We call it "subrouting".

For example, let's say we have several URLs that should only match when the host is `www.example.com`. Create a route for that host and get a "subrouter" from it:

```go
r := mux.NewRouter()
s := r.Host("www.example.com").Subrouter()
```

Then register routes in the subrouter:

```go
s.HandleFunc("/products/", ProductsHandler)
s.HandleFunc("/products/{key}", ProductHandler)
s.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler)
```

The three URL paths we registered above will only be tested if the domain is `www.example.com`, because the subrouter is tested first. This is not only convenient, but also optimizes request matching. You can create subrouters combining any attribute matchers accepted by a route.

Subrouters can be used to create domain or path "namespaces": you define subrouters in a central place and then parts of the app can register its paths relatively to a given subrouter.

There's one more thing about subroutes. When a subrouter has a path prefix, the inner routes use it as base for their paths:

```go
r := mux.NewRouter()
s := r.PathPrefix("/products").Subrouter()
// "/products/"
s.HandleFunc("/", ProductsHandler)
// "/products/{key}/"
s.HandleFunc("/{key}/", ProductHandler)
// "/products/{key}/details"
s.HandleFunc("/{key}/details", ProductDetailsHandler)
```


### Static Files

Note that the path provided to `PathPrefix()` represents a "wildcard": calling
`PathPrefix("/static/").Handler(...)` means that the handler will be passed any
request that matches "/static/\*". This makes it easy to serve static files with mux:

```go
func main() {
    var dir string

    flag.StringVar(&dir, "dir", ".", "the directory to serve files from. Defaults to the current dir")
    flag.Parse()
    r := mux.NewRouter()

    // This will serve files under http://localhost:8000/static/<filename>
    r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir(dir))))

    srv := &http.Server{
        Handler:      r,
        Addr:         "127.0.0.1:8000",
        // Good practice: enforce timeouts for servers you create!
        WriteTimeout: 15 * time.Second,
        ReadTimeout:  15 * time.Second,
    }

    log.Fatal(srv.ListenAndServe())
}
```

### Registered URLs

Now let's see how to build registered URLs.

Routes can be named. All routes that define a name can have their URLs built, or "reversed". We define a name calling `Name()` on a route. For example:

```go
r := mux.NewRouter()
r.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler).
  Name("article")
```

To build a URL, get the route and call the `URL()` method, passing a sequence of key/value pairs for the route variables. For the previous route, we would do:

```go
url, err := r.Get("article").URL("category", "technology", "id", "42")
```

...and the result will be a `url.URL` with the following path:

```
"/articles/technology/42"
```

This also works for host and query value variables:

```go
r := mux.NewRouter()
r.Host("{subdomain}.domain.com").
  Path("/articles/{category}/{id:[0-9]+}").
  Queries("filter", "{filter}").
  HandlerFunc(ArticleHandler).
  Name("article")

// url.String() will be "http://news.domain.com/articles/technology/42?filter=gorilla"
url, err := r.Get("article").URL("subdomain", "news",
                                 "category", "technology",
                                 "id", "42",
                                 "filter", "gorilla")
```

All variables defined in the route are required, and their values must conform to the corresponding patterns. These requirements guarantee that a generated URL will always match a registered route -- the only exception is for explicitly defined "build-only" routes which never match.

Regex support also exists for matching Headers within a route. For example, we could do:

```go
r.HeadersRegexp("Content-Type", "application/(text|json)")
```

...and the route will match both requests with a Content-Type of `application/json` as well as `application/text`

There's also a way to build only the URL host or path for a route: use the methods `URLHost()` or `URLPath()` instead. For the previous route, we would do:

```go
// "http://news.domain.com/"
host, err := r.Get("article").URLHost("subdomain", "news")

// "/articles/technology/42"
path, err := r.Get("article").URLPath("category", "technology", "id", "42")
```

And if you use subrouters, host and path defined separately can be built as well:

```go
r := mux.NewRouter()
s := r.Host("{subdomain}.domain.com").Subrouter()
s.Path("/articles/{category}/{id:[0-9]+}").
  HandlerFunc(ArticleHandler).
  Name("article")

// "http://news.domain.com/articles/technology/42"
url, err := r.Get("article").URL("subdomain", "news",
                                 "category", "technology",
                                 "id", "42")
```

### Walking Routes

The `Walk` function on `mux.Router` can be used to visit all of the routes that are registered on a router. For example,
the following prints all of the registered routes:

```go
package main

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gorilla/mux"
)

func handler(w http.ResponseWriter, r *http.Request) {
	return
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/", handler)
	r.HandleFunc("/products", handler).Methods("POST")
	r.HandleFunc("/articles", handler).Methods("GET")
	r.HandleFunc("/articles/{id}", handler).Methods("GET", "PUT")
	r.HandleFunc("/authors", handler).Queries("surname", "{surname}")
	err := r.Walk(func(route *mux.Route, router *mux.Router, ancestors []*mux.Route) error {
		pathTemplate, err := route.GetPathTemplate()
		if err == nil {
			fmt.Println("ROUTE:", pathTemplate)
		}
		pathRegexp, err := route.GetPathRegexp()
		if err == nil {
			fmt.Println("Path regexp:", pathRegexp)
		}
		queriesTemplates, err := route.GetQueriesTemplates()
		if err == nil {
			fmt.Println("Queries templates:", strings.Join(queriesTemplates, ","))
		}
		queriesRegexps, err := route.GetQueriesRegexp()
		if err == nil {
			fmt.Println("Queries regexps:", strings.Join(queriesRegexps, ","))
		}
		methods, err := route.GetMethods()
		if err == nil {
			fmt.Println("Methods:", strings.Join(methods, ","))
		}
		fmt.Println()
		return nil
	})

	if err != nil {
		fmt.Println(err)
	}

	http.Handle("/", r)
}
```

### Graceful Shutdown

Go 1.8 introduced the ability to [gracefully shutdown](https://golang.org/doc/go1.8#http_shutdown) a `*http.Server`. Here's how to do that alongside `mux`:

```go
package main

import (
    "context"
    "flag"
    "log"
    "net/http"
    "os"
    "os/signal"
    "time"

    "github.com/gorilla/mux"
)

func main() {
    var wait time.Duration
    flag.DurationVar(&wait, "graceful-timeout", time.Second * 15, "the duration for which the server gracefully wait for existing connections to finish - e.g. 15s or 1m")
    flag.Parse()

    r := mux.NewRouter()
    // Add your routes as needed

    srv := &http.Server{
        Addr:         "0.0.0.0:8080",
        // Good practice to set timeouts to avoid Slowloris attacks.
        WriteTimeout: time.Second * 15,
        ReadTimeout:  time.Second * 15,
        IdleTimeout:  time.Second * 60,
        Handler: r, // Pass our instance of gorilla/mux in.
    }

    // Run our server in a goroutine so that it doesn't block.
    go func() {
        if err := srv.ListenAndServe(); err != nil {
            log.Println(err)
        }
    }()

    c := make(chan os.Signal, 1)
    // We'll accept graceful shutdowns when quit via SIGINT (Ctrl+C)
    // SIGKILL, SIGQUIT or SIGTERM (Ctrl+/) will not be caught.
    signal.Notify(c, os.Interrupt)

    // Block until we receive our signal.
    <-c

    // Create a deadline to wait for.
    ctx, cancel := context.WithTimeout(context.Background(), wait)
    defer cancel()
    // Doesn't block if no connections, but will otherwise wait
    // until the timeout deadline.
    srv.Shutdown(ctx)
    // Optionally, you could run srv.Shutdown in a goroutine and block on
    // <-ctx.Done() if your application should wait for other services
    // to finalize based on context cancellation.
    log.Println("shutting down")
    os.Exit(0)
}
```

### Middleware

Mux supports the addition of middlewares to a [Router](https://godoc.org/github.com/gorilla/mux#Router), which are executed in the order they are added if a match is found, including its subrouters.
Middlewares are (typically) small pieces of code which take one request, do something with it, and pass it down to another middleware or the final handler. Some common use cases for middleware are request logging, header manipulation, or `ResponseWriter` hijacking.

Mux middlewares are defined using the de facto standard type:

```go
type MiddlewareFunc func(http.Handler) http.Handler
```

Typically, the returned handler is a closure which does something with the http.ResponseWriter and http.Request passed to it, and then calls the handler passed as parameter to the MiddlewareFunc. This takes advantage of closures being able access variables from the context where they are created, while retaining the signature enforced by the receivers.

A very basic middleware which logs the URI of the request being handled could be written as:

```go
func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        // Do stuff here
        log.Println(r.RequestURI)
        // Call the next handler, which can be another middleware in the chain, or the final handler.
        next.ServeHTTP(w, r)
    })
}
```

Middlewares can be added to a router using `Router.Use()`:

```go
r := mux.NewRouter()
r.HandleFunc("/", handler)
r.Use(loggingMiddleware)
```

A more complex authentication middleware, which maps session token to users, could be written as:

```go
// Define our struct
type authenticationMiddleware struct {
	tokenUsers map[string]string
}

// Initialize it somewhere
func (amw *authenticationMiddleware) Populate() {
	amw.tokenUsers["00000000"] = "user0"
	amw.tokenUsers["aaaaaaaa"] = "userA"
	amw.tokenUsers["05f717e5"] = "randomUser"
	amw.tokenUsers["deadbeef"] = "user0"
}

// Middleware function, which will be called for each request
func (amw *authenticationMiddleware) Middleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("X-Session-Token")

        if user, found := amw.tokenUsers[token]; found {
        	// We found the token in our map
        	log.Printf("Authenticated user %s\n", user)
        	// Pass down the request to the next middleware (or final handler)
        	next.ServeHTTP(w, r)
        } else {
        	// Write an error and stop the handler chain
        	http.Error(w, "Forbidden", http.StatusForbidden)
        }
    })
}
```

```go
r := mux.NewRouter()
r.HandleFunc("/", handler)

amw := authenticationMiddleware{}
amw.Populate()

r.Use(amw.Middleware)
```

Note: The handler chain will be stopped if your middleware doesn't call `next.ServeHTTP()` with the corresponding parameters. This can be used to abort a request if the middleware writer wants to. Middlewares _should_ write to `ResponseWriter` if they _are_ going to terminate the request, and they _should not_ write to `ResponseWriter` if they _are not_ going to terminate it.

### Testing Handlers

Testing handlers in a Go web application is straightforward, and _mux_ doesn't complicate this any further. Given two files: `endpoints.go` and `endpoints_test.go`, here's how we'd test an application using _mux_.

First, our simple HTTP handler:

```go
// endpoints.go
package main

func HealthCheckHandler(w http.ResponseWriter, r *http.Request) {
    // A very simple health check.
    w.WriteHeader(http.StatusOK)
    w.Header().Set("Content-Type", "application/json")

    // In the future we could report back on the status of our DB, or our cache
    // (e.g. Redis) by performing a simple PING, and include them in the response.
    io.WriteString(w, `{"alive": true}`)
}

func main() {
    r := mux.NewRouter()
    r.HandleFunc("/health", HealthCheckHandler)

    log.Fatal(http.ListenAndServe("localhost:8080", r))
}
```

Our test code:

```go
// endpoints_test.go
package main

import (
    "net/http"
    "net/http/httptest"
    "testing"
)

func TestHealthCheckHandler(t *testing.T) {
    // Create a request to pass to our handler. We don't have any query parameters for now, so we'll
    // pass 'nil' as the third parameter.
    req, err := http.NewRequest("GET", "/health", nil)
    if err != nil {
        t.Fatal(err)
    }

    // We create a ResponseRecorder (which satisfies http.ResponseWriter) to record the response.
    rr := httptest.NewRecorder()
    handler := http.HandlerFunc(HealthCheckHandler)

    // Our handlers satisfy http.Handler, so we can call their ServeHTTP method
    // directly and pass in our Request and ResponseRecorder.
    handler.ServeHTTP(rr, req)

    // Check the status code is what we expect.
    if status := rr.Code; status != http.StatusOK {
        t.Errorf("handler returned wrong status code: got %v want %v",
            status, http.StatusOK)
    }

    // Check the response body is what we expect.
    expected := `{"alive": true}`
    if rr.Body.String() != expected {
        t.Errorf("handler returned unexpected body: got %v want %v",
            rr.Body.String(), expected)
    }
}
```

In the case that our routes have [variables](#examples), we can pass those in the request. We could write
[table-driven tests](https://dave.cheney.net/2013/06/09/writing-table-driven-tests-in-go) to test multiple
possible route variables as needed.

```go
// endpoints.go
func main() {
    r := mux.NewRouter()
    // A route with a route variable:
    r.HandleFunc("/metrics/{type}", MetricsHandler)

    log.Fatal(http.ListenAndServe("localhost:8080", r))
}
```

Our test file, with a table-driven test of `routeVariables`:

```go
// endpoints_test.go
func TestMetricsHandler(t *testing.T) {
    tt := []struct{
        routeVariable string
        shouldPass bool
    }{
        {"goroutines", true},
        {"heap", true},
        {"counters", true},
        {"queries", true},
        {"adhadaeqm3k", false},
    }

    for _, tc := range tt {
        path := fmt.Sprintf("/metrics/%s", tc.routeVariable)
        req, err := http.NewRequest("GET", path, nil)
        if err != nil {
            t.Fatal(err)
        }

        rr := httptest.NewRecorder()
	
	// Need to create a router that we can pass the request through so that the vars will be added to the context
	router := mux.NewRouter()
        router.HandleFunc("/metrics/{type}", MetricsHandler)
        router.ServeHTTP(rr, req)

        // In this case, our MetricsHandler returns a non-200 response
        // for a route variable it doesn't know about.
        if rr.Code == http.StatusOK && !tc.shouldPass {
            t.Errorf("handler should have failed on routeVariable %s: got %v want %v",
                tc.routeVariable, rr.Code, http.StatusOK)
        }
    }
}
```

## Full Example

Here's a complete, runnable example of a small `mux` based server:

```go
package main

import (
    "net/http"
    "log"
    "github.com/gorilla/mux"
)

func YourHandler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Gorilla!\n"))
}

func main() {
    r := mux.NewRouter()
    // Routes consist of a path and a handler function.
    r.HandleFunc("/", YourHandler)

    // Bind to a port and pass our router in
    log.Fatal(http.ListenAndServe(":8000", r))
}
```

## License

BSD licensed. See the LICENSE file for details.
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

gorilla/context is a general purpose registry for global request variables.

> Note: gorilla/context, having been born well before `context.Context` existed, does not play well
> with the shallow copying of the request that [`http.Request.WithContext`](https://golang.org/pkg/net/http/#Request.WithContext) (added to net/http Go 1.7 onwards) performs. You should either use *just* gorilla/context, or moving forward, the new `http.Request.Context()`.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
# ocicni

API layer to call the CNI plugins from an OCI lifecycle daemon
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
# Syslog Hooks for Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>

## Usage

```go
import (
  "log/syslog"
  "github.com/sirupsen/logrus"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
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
  "github.com/sirupsen/logrus"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("", "", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```
## TOML parser and encoder for Go with reflection

TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library `json` and `xml` 
packages. This package also supports the `encoding.TextUnmarshaler` and
`encoding.TextMarshaler` interfaces so that you can define custom data 
representations. (There is an example of this below.)

Spec: https://github.com/mojombo/toml

Compatible with TOML version
[v0.2.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.2.0.md)

Documentation: http://godoc.org/github.com/BurntSushi/toml

Installation:

```bash
go get github.com/BurntSushi/toml
```

Try the toml validator:

```bash
go get github.com/BurntSushi/toml/cmd/tomlv
tomlv some-toml-file.toml
```

[![Build status](https://api.travis-ci.org/BurntSushi/toml.png)](https://travis-ci.org/BurntSushi/toml)


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

## Description

This library provides basic building blocks for building advanced console UIs.

Initially created for [Gor](http://github.com/buger/gor).

Full API documentation: http://godoc.org/github.com/buger/goterm

## Basic usage

Full screen console app, printing current time:

```go
import (
    tm "github.com/buger/goterm"
    "time"
)

func main() {
    tm.Clear() // Clear current screen

    for {
        // By moving cursor to top-left position we ensure that console output
        // will be overwritten each time, instead of adding new.
        tm.MoveCursor(1,1)

        tm.Println("Current Time:", time.Now().Format(time.RFC1123))

        tm.Flush() // Call it every time at the end of rendering

        time.Sleep(time.Second)
    }
}
```

This can be seen in [examples/time_example.go](examples/time_example.go).  To
run it yourself, go into your `$GOPATH/src/github.com/buger/goterm` directory
and run `go run ./examples/time_example.go`


Print red bold message on white background:

```go    
tm.Println(tm.Background(tm.Color(tm.Bold("Important header"), tm.RED), tm.WHITE))
```


Create box and move it to center of the screen:

```go
tm.Clear()

// Create Box with 30% width of current screen, and height of 20 lines
box := tm.NewBox(30|tm.PCT, 20, 0)

// Add some content to the box
// Note that you can add ANY content, even tables
fmt.Fprint(box, "Some box content")

// Move Box to approx center of the screen
tm.Print(tm.MoveTo(box.String(), 40|tm.PCT, 40|tm.PCT))

tm.Flush()
```

This can be found in [examples/box_example.go](examples/box_example.go).

Draw table:

```go
// Based on http://golang.org/pkg/text/tabwriter
totals := tm.NewTable(0, 10, 5, ' ', 0)
fmt.Fprintf(totals, "Time\tStarted\tActive\tFinished\n")
fmt.Fprintf(totals, "%s\t%d\t%d\t%d\n", "All", started, started-finished, finished)
tm.Println(totals)
tm.Flush()
```

This can be found in [examples/table_example.go](examples/table_example.go).

## Line charts

Chart example:

![screen shot 2013-07-09 at 5 05 37 pm](https://f.cloud.github.com/assets/14009/767676/e3dd35aa-e887-11e2-9cd2-f6451eb26adc.png)


```go
    import (
        tm "github.com/buger/goterm"
    )

    chart := tm.NewLineChart(100, 20)
    
    data := new(tm.DataTable)
    data.AddColumn("Time")
    data.AddColumn("Sin(x)")
    data.AddColumn("Cos(x+1)")

    for i := 0.1; i < 10; i += 0.1 {
	data.AddRow(i, math.Sin(i), math.Cos(i+1))
    }
    
    tm.Println(chart.Draw(data))
```

This can be found in [examples/chart_example.go](examples/chart_example.go).

Drawing 2 separate graphs in different scales. Each graph have its own Y axe.

```go
chart.Flags = tm.DRAW_INDEPENDENT
```

Drawing graph with relative scale (Grapwh draw starting from min value instead of zero)

```go
chart.Flags = tm.DRAW_RELATIVE
```
[![Build Status](https://travis-ci.org/godbus/dbus.svg?branch=master)](https://travis-ci.org/godbus/dbus)

dbus
----

dbus is a simple library that implements native Go client bindings for the
D-Bus message bus system.

### Features

* Complete native implementation of the D-Bus message protocol
* Go-like API (channels for signals / asynchronous method calls, Goroutine-safe connections)
* Subpackages that help with the introspection / property interfaces

### Installation

This packages requires Go 1.1. If you installed it and set up your GOPATH, just run:

```
go get github.com/godbus/dbus
```

If you want to use the subpackages, you can install them the same way.

### Usage

The complete package documentation and some simple examples are available at
[godoc.org](http://godoc.org/github.com/godbus/dbus). Also, the
[_examples](https://github.com/godbus/dbus/tree/master/_examples) directory
gives a short overview over the basic usage. 

#### Projects using godbus
- [notify](https://github.com/esiqveland/notify) provides desktop notifications over dbus into a library.
- [go-bluetooth](https://github.com/muka/go-bluetooth) provides a bluetooth client over bluez dbus API.

Please note that the API is considered unstable for now and may change without
further notice.

### License

go.dbus is available under the Simplified BSD License; see LICENSE for the full
text.

Nearly all of the credit for this library goes to github.com/guelfey/go.dbus.
# cgroups

[![Build Status](https://travis-ci.org/containerd/cgroups.svg?branch=master)](https://travis-ci.org/containerd/cgroups)
[![codecov](https://codecov.io/gh/containerd/cgroups/branch/master/graph/badge.svg)](https://codecov.io/gh/containerd/cgroups)
[![GoDoc](https://godoc.org/github.com/containerd/cgroups?status.svg)](https://godoc.org/github.com/containerd/cgroups)
[![Go Report Card](https://goreportcard.com/badge/github.com/containerd/cgroups)](https://goreportcard.com/report/github.com/containerd/cgroups)

Go package for creating, managing, inspecting, and destroying cgroups.
The resources format for settings on the cgroup uses the OCI runtime-spec found
[here](https://github.com/opencontainers/runtime-spec).

## Examples

### Create a new cgroup

This creates a new cgroup using a static path for all subsystems under `/test`.

* /sys/fs/cgroup/cpu/test
* /sys/fs/cgroup/memory/test
* etc....

It uses a single hierarchy and specifies cpu shares as a resource constraint and
uses the v1 implementation of cgroups.


```go
shares := uint64(100)
control, err := cgroups.New(cgroups.V1, cgroups.StaticPath("/test"), &specs.LinuxResources{
    CPU: &specs.CPU{
        Shares: &shares,
    },
})
defer control.Delete()
```

### Create with systemd slice support


```go
control, err := cgroups.New(cgroups.Systemd, cgroups.Slice("system.slice", "runc-test"), &specs.LinuxResources{
    CPU: &specs.CPU{
        Shares: &shares,
    },
})

```

### Load an existing cgroup

```go
control, err = cgroups.Load(cgroups.V1, cgroups.StaticPath("/test"))
```

### Add a process to the cgroup

```go
if err := control.Add(cgroups.Process{Pid:1234}); err != nil {
}
```

###  Update the cgroup 

To update the resources applied in the cgroup

```go
shares = uint64(200)
if err := control.Update(&specs.LinuxResources{
    CPU: &specs.CPU{
        Shares: &shares,
    },
}); err != nil {
}
```

### Freeze and Thaw the cgroup

```go
if err := control.Freeze(); err != nil {
}
if err := control.Thaw(); err != nil {
}
```

### List all processes in the cgroup or recursively

```go
processes, err := control.Processes(cgroups.Devices, recursive)
```

### Get Stats on the cgroup

```go
stats, err := control.Stat()
```

By adding `cgroups.IgnoreNotExist` all non-existent files will be ignored, e.g. swap memory stats without swap enabled
```go
stats, err := control.Stat(cgroups.IgnoreNotExist)
```

### Move process across cgroups

This allows you to take processes from one cgroup and move them to another.

```go
err := control.MoveTo(destination)
```

### Create subcgroup

```go
subCgroup, err := control.New("child", resources)
```

## Project details

Cgroups is a containerd sub-project, licensed under the [Apache 2.0 license](./LICENSE).
As a containerd sub-project, you will find the:

 * [Project governance](https://github.com/containerd/project/blob/master/GOVERNANCE.md),
 * [Maintainers](https://github.com/containerd/project/blob/master/MAINTAINERS),
 * and [Contributing guidelines](https://github.com/containerd/project/blob/master/CONTRIBUTING.md)

information in our [`containerd/project`](https://github.com/containerd/project) repository.
# continuity

[![GoDoc](https://godoc.org/github.com/containerd/continuity?status.svg)](https://godoc.org/github.com/containerd/continuity)
[![Build Status](https://travis-ci.org/containerd/continuity.svg?branch=master)](https://travis-ci.org/containerd/continuity)

A transport-agnostic, filesystem metadata manifest system

This project is a staging area for experiments in providing transport agnostic
metadata storage.

Please see https://github.com/opencontainers/specs/issues/11 for more details.

## Manifest Format

A continuity manifest encodes filesystem metadata in Protocol Buffers.
Please refer to [proto/manifest.proto](proto/manifest.proto).

## Usage

Build:

```console
$ make
```

Create a manifest (of this repo itself):

```console
$ ./bin/continuity build . > /tmp/a.pb
```

Dump a manifest:

```console
$ ./bin/continuity ls /tmp/a.pb
...
-rw-rw-r--      270 B   /.gitignore
-rw-rw-r--      88 B    /.mailmap
-rw-rw-r--      187 B   /.travis.yml
-rw-rw-r--      359 B   /AUTHORS
-rw-rw-r--      11 kB   /LICENSE
-rw-rw-r--      1.5 kB  /Makefile
...
-rw-rw-r--      986 B   /testutil_test.go
drwxrwxr-x      0 B     /version
-rw-rw-r--      478 B   /version/version.go
```

Verify a manifest:

```console
$ ./bin/continuity verify . /tmp/a.pb
```

Break the directory and restore using the manifest:
```console
$ chmod 777 Makefile
$ ./bin/continuity verify . /tmp/a.pb
2017/06/23 08:00:34 error verifying manifest: resource "/Makefile" has incorrect mode: -rwxrwxrwx != -rw-rw-r--
$ ./bin/continuity apply . /tmp/a.pb
$ stat -c %a Makefile
664
$ ./bin/continuity verify . /tmp/a.pb
```


## Contribution Guide
### Building Proto Package

If you change the proto file you will need to rebuild the generated Go with `go generate`.

```console
$ go generate ./proto
```

## Project details

continuity is a containerd sub-project, licensed under the [Apache 2.0 license](./LICENSE).
As a containerd sub-project, you will find the:
 * [Project governance](https://github.com/containerd/project/blob/master/GOVERNANCE.md),
 * [Maintainers](https://github.com/containerd/project/blob/master/MAINTAINERS),
 * and [Contributing guidelines](https://github.com/containerd/project/blob/master/CONTRIBUTING.md)

information in our [`containerd/project`](https://github.com/containerd/project) repository.
Docker / OCI Image Builder
==========================

[![Go Report Card](https://goreportcard.com/badge/github.com/openshift/imagebuilder)](https://goreportcard.com/report/github.com/openshift/imagebuilder)
[![GoDoc](https://godoc.org/github.com/openshift/imagebuilder?status.png)](https://godoc.org/github.com/openshift/imagebuilder)
[![Travis](https://travis-ci.org/openshift/imagebuilder.svg?branch=master)](https://travis-ci.org/openshift/imagebuilder)
[![Join the chat at freenode:openshift-dev](https://img.shields.io/badge/irc-freenode%3A%20%23openshift--dev-blue.svg)](http://webchat.freenode.net/?channels=%23openshift-dev)

Note: this library is beta and may contain bugs that prevent images from being identical to Docker build.  Test your images (and add to our conformance suite)!

This library supports using the Dockerfile syntax to build Docker
compatible images, without invoking Docker build. It is intended to give
clients more control over how a Docker build is run, including:

* Instead of building one layer per line, run all instructions in the
  same container
* Set Docker HostConfig settings like network and memory controls that
  are not available when running Docker builds
* Mount external files into the build that are not persisted as part of
  the final image (i.e. "secrets")
* If there are no RUN commands in the Dockerfile, the container is created
  and committed, but never started.

The final image should be 99.9% compatible with regular docker builds,
but bugs are always possible.

Future goals include:

* Output OCI compatible images
* Support other container execution engines, like runc or rkt
* Better conformance testing
* Windows support

## Install and Run

To download and install the library and the binary, set up a Golang build environment and with `GOPATH` set run:

```
$ go get -u github.com/openshift/imagebuilder/cmd/imagebuilder
```

The included command line takes one argument, a path to a directory containing a Dockerfile. The `-t` option
can be used to specify an image to tag as:

```
$ imagebuilder [-t TAG] DIRECTORY
```

To mount a file into the image for build that will not be present in the final output image, run:

```
$ imagebuilder --mount ~/secrets/private.key:/etc/keys/private.key path/to/my/code testimage
```

Any processes in the Dockerfile will have access to `/etc/keys/private.key`, but that file will not be part of the committed image.

Running `--mount` requires Docker 1.10 or newer, as it uses a Docker volume to hold the mounted files and the volume API was not
available in earlier versions.

You can also customize which Dockerfile is run, or run multiple Dockerfiles in sequence (the FROM is ignored on
later files):

```
$ imagebuilder -f Dockerfile:Dockerfile.extra .
```

will build the current directory and combine the first Dockerfile with the second. The FROM in the second image
is ignored.


## Code Example

```
f, err := os.Open("path/to/Dockerfile")
if err != nil {
	return err
}
defer f.Close()

e := builder.NewClientExecutor(o.Client)
e.Out, e.ErrOut = os.Stdout, os.Stderr
e.AllowPull = true
e.Directory = "context/directory"
e.Tag = "name/of-image:and-tag"
e.AuthFn = nil // ... pass a function to retrieve authorization info
e.LogFn = func(format string, args ...interface{}) {
	fmt.Fprintf(e.ErrOut, "--> %s\n", fmt.Sprintf(format, args...))
}

buildErr := e.Build(f, map[string]string{"arg1":"value1"})
if err := e.Cleanup(); err != nil {
	fmt.Fprintf(e.ErrOut, "error: Unable to clean up build: %v\n", err)
}

return buildErr
```

Example of usage from OpenShift's experimental `dockerbuild` [command with mount secrets](https://github.com/openshift/origin/blob/26c9e032ff42f613fe10649cd7c5fa1b4c33501b/pkg/cmd/cli/cmd/dockerbuild/dockerbuild.go)

## Run conformance tests (very slow):

```
go test ./dockerclient/conformance_test.go -tags conformance
```
This package provides helper functions for dealing with signals across various operating systemsgo-spew
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
# compress

This package is based on an optimized Deflate function, which is used by gzip/zip/zlib packages.

It offers slightly better compression at lower compression settings, and up to 3x faster encoding at highest compression level.

* [High Throughput Benchmark](http://blog.klauspost.com/go-gzipdeflate-benchmarks/).
* [Small Payload/Webserver Benchmarks](http://blog.klauspost.com/gzip-performance-for-go-webservers/).
* [Linear Time Compression](http://blog.klauspost.com/constant-time-gzipzip-compression/).
* [Re-balancing Deflate Compression Levels](https://blog.klauspost.com/rebalancing-deflate-compression-levels/)

[![Build Status](https://travis-ci.org/klauspost/compress.svg?branch=master)](https://travis-ci.org/klauspost/compress)
[![Sourcegraph Badge](https://sourcegraph.com/github.com/klauspost/compress/-/badge.svg)](https://sourcegraph.com/github.com/klauspost/compress?badge)

# changelog

* Aug 1, 2018: Added [huff0 README](https://github.com/klauspost/compress/tree/master/huff0#huff0-entropy-compression).
* Jul 8, 2018: Added [Performance Update 2018](#performance-update-2018) below.
* Jun 23, 2018: Merged [Go 1.11 inflate optimizations](https://go-review.googlesource.com/c/go/+/102235). Go 1.9 is now required. Backwards compatible version tagged with [v1.3.0](https://github.com/klauspost/compress/releases/tag/v1.3.0).
* Apr 2, 2018: Added [huff0](https://godoc.org/github.com/klauspost/compress/huff0) en/decoder. Experimental for now, API may change.
* Mar 4, 2018: Added [FSE Entropy](https://godoc.org/github.com/klauspost/compress/fse) en/decoder. Experimental for now, API may change.
* Nov 3, 2017: Add compression [Estimate](https://godoc.org/github.com/klauspost/compress#Estimate) function.
* May 28, 2017: Reduce allocations when resetting decoder.
* Apr 02, 2017: Change back to official crc32, since changes were merged in Go 1.7.
* Jan 14, 2017: Reduce stack pressure due to array copies. See [Issue #18625](https://github.com/golang/go/issues/18625).
* Oct 25, 2016: Level 2-4 have been rewritten and now offers significantly better performance than before.
* Oct 20, 2016: Port zlib changes from Go 1.7 to fix zlib writer issue. Please update.
* Oct 16, 2016: Go 1.7 changes merged. Apples to apples this package is a few percent faster, but has a significantly better balance between speed and compression per level. 
* Mar 24, 2016: Always attempt Huffman encoding on level 4-7. This improves base 64 encoded data compression.
* Mar 24, 2016: Small speedup for level 1-3.
* Feb 19, 2016: Faster bit writer, level -2 is 15% faster, level 1 is 4% faster.
* Feb 19, 2016: Handle small payloads faster in level 1-3.
* Feb 19, 2016: Added faster level 2 + 3 compression modes.
* Feb 19, 2016: [Rebalanced compression levels](https://blog.klauspost.com/rebalancing-deflate-compression-levels/), so there is a more even progresssion in terms of compression. New default level is 5.
* Feb 14, 2016: Snappy: Merge upstream changes. 
* Feb 14, 2016: Snappy: Fix aggressive skipping.
* Feb 14, 2016: Snappy: Update benchmark.
* Feb 13, 2016: Deflate: Fixed assembler problem that could lead to sub-optimal compression.
* Feb 12, 2016: Snappy: Added AMD64 SSE 4.2 optimizations to matching, which makes easy to compress material run faster. Typical speedup is around 25%.
* Feb 9, 2016: Added Snappy package fork. This version is 5-7% faster, much more on hard to compress content.
* Jan 30, 2016: Optimize level 1 to 3 by not considering static dictionary or storing uncompressed. ~4-5% speedup.
* Jan 16, 2016: Optimization on deflate level 1,2,3 compression.
* Jan 8 2016: Merge [CL 18317](https://go-review.googlesource.com/#/c/18317): fix reading, writing of zip64 archives.
* Dec 8 2015: Make level 1 and -2 deterministic even if write size differs.
* Dec 8 2015: Split encoding functions, so hashing and matching can potentially be inlined. 1-3% faster on AMD64. 5% faster on other platforms.
* Dec 8 2015: Fixed rare [one byte out-of bounds read](https://github.com/klauspost/compress/issues/20). Please update!
* Nov 23 2015: Optimization on token writer. ~2-4% faster. Contributed by [@dsnet](https://github.com/dsnet).
* Nov 20 2015: Small optimization to bit writer on 64 bit systems.
* Nov 17 2015: Fixed out-of-bound errors if the underlying Writer returned an error. See [#15](https://github.com/klauspost/compress/issues/15).
* Nov 12 2015: Added [io.WriterTo](https://golang.org/pkg/io/#WriterTo) support to gzip/inflate.
* Nov 11 2015: Merged [CL 16669](https://go-review.googlesource.com/#/c/16669/4): archive/zip: enable overriding (de)compressors per file
* Oct 15 2015: Added skipping on uncompressible data. Random data speed up >5x.

# usage

The packages are drop-in replacements for standard libraries. Simply replace the import path to use them:

| old import         | new import                              |
|--------------------|-----------------------------------------|
| `compress/gzip`    | `github.com/klauspost/compress/gzip`    |
| `compress/zlib`    | `github.com/klauspost/compress/zlib`    |
| `archive/zip`      | `github.com/klauspost/compress/zip`     |
| `compress/flate`   | `github.com/klauspost/compress/flate`   |

You may also be interested in [pgzip](https://github.com/klauspost/pgzip), which is a drop in replacement for gzip, which support multithreaded compression on big files and the optimized [crc32](https://github.com/klauspost/crc32) package used by these packages.

The packages contains the same as the standard library, so you can use the godoc for that: [gzip](http://golang.org/pkg/compress/gzip/), [zip](http://golang.org/pkg/archive/zip/),  [zlib](http://golang.org/pkg/compress/zlib/), [flate](http://golang.org/pkg/compress/flate/).

Currently there is only minor speedup on decompression (mostly CRC32 calculation).

# Performance Update 2018

It has been a while since we have been looking at the speed of this package compared to the standard library, so I thought I would re-do my tests and give some overall recommendations based on the current state. All benchmarks have been performed with Go 1.10 on my Desktop Intel(R) Core(TM) i7-2600 CPU @3.40GHz. Since I last ran the tests, I have gotten more RAM, which means tests with big files are no longer limited by my SSD.

The raw results are in my [updated spreadsheet](https://docs.google.com/spreadsheets/d/1nuNE2nPfuINCZJRMt6wFWhKpToF95I47XjSsc-1rbPQ/edit?usp=sharing). Due to cgo changes and upstream updates i could not get the cgo version of gzip to compile. Instead I included the [zstd](https://github.com/datadog/zstd) cgo implementation. If I get cgo gzip to work again, I might replace the results in the sheet.

The columns to take note of are: *MB/s* - the throughput. *Reduction* - the data size reduction in percent of the original. *Rel Speed* relative speed compared to the standard libary at the same level. *Smaller* - how many percent smaller is the compressed output compared to stdlib. Negative means the output was bigger. *Loss* means the loss (or gain) in compression as a percentage difference of the input.

The `gzstd` (standard library gzip) and `gzkp` (this package gzip) only uses one CPU core. [`pgzip`](https://github.com/klauspost/pgzip), [`bgzf`](https://github.com/biogo/hts/bgzf) uses all 4 cores. [`zstd`](https://github.com/DataDog/zstd) uses one core, and is a beast (but not Go, yet).


## Overall differences.

There appears to be a roughly 5-10% speed advantage over the standard library when comparing at similar compression levels.

The biggest difference you will see is the result of [re-balancing](https://blog.klauspost.com/rebalancing-deflate-compression-levels/) the compression levels. I wanted by library to give a smoother transition between the compression levels than the standard library.

This package attempts to provide a more smooth transition, where "1" is taking a lot of shortcuts, "5" is the reasonable trade-off and "9" is the "give me the best compression", and the values in between gives something reasonable in between. The standard library has big differences in levels 1-4, but levels 5-9 having no significant gains - often spending a lot more time than can be justified by the achieved compression.

There are links to all the test data in the [spreadsheet](https://docs.google.com/spreadsheets/d/1nuNE2nPfuINCZJRMt6wFWhKpToF95I47XjSsc-1rbPQ/edit?usp=sharing) in the top left field on each tab.

## Web Content

This test set aims to emulate typical use in a web server. The test-set is 4GB data in 53k files, and is a mixture of (mostly) HTML, JS, CSS.

Since level 1 and 9 are close to being the same code, they are quite close. But looking at the levels in-between the differences are quite big.

Looking at level 6, this package is 88% faster, but will output about 6% more data. For a web server, this means you can serve 88% more data, but have to pay for 6% more bandwidth. You can draw your own conclusions on what would be the most expensive for your case.

## Object files

This test is for typical data files stored on a server. In this case it is a collection of Go precompiled objects. They are very compressible.

The picture is similar to the web content, but with small differences since this is very compressible. Levels 2-3 offer good speed, but is sacrificing quite a bit of compression. 

The standard library seems suboptimal on level 3 and 4 - offering both worse compression and speed than level 6 & 7 of this package respectively.

## Highly Compressible File

This is a JSON file with very high redundancy. The reduction starts at 95% on level 1, so in real life terms we are dealing with something like a highly redundant stream of data, etc.

It is definitely visible that we are dealing with specialized content here, so the results are very scattered. This package does not do very well at levels 1-4, but picks up significantly at level 5 and levels 7 and 8 offering great speed for the achieved compression.

So if you know you content is extremely compressible you might want to go slightly higher than the defaults. The standard library has a huge gap between levels 3 and 4 in terms of speed (2.75x slowdown), so it offers little "middle ground".

## Medium-High Compressible

This is a pretty common test corpus: [enwik9](http://mattmahoney.net/dc/textdata.html). It contains the first 10^9 bytes of the English Wikipedia dump on Mar. 3, 2006. This is a very good test of typical text based compression and more data heavy streams.

We see a similar picture here as in "Web Content". On equal levels some compression is sacrificed for more speed. Level 5 seems to be the best trade-off between speed and size, beating stdlib level 3 in both.

## Medium Compressible

I will combine two test sets, one [10GB file set](http://mattmahoney.net/dc/10gb.html) and a VM disk image (~8GB). Both contain different data types and represent a typical backup scenario.

The most notable thing is how quickly the standard libary drops to very low compression speeds around level 5-6 without any big gains in compression. Since this type of data is fairly common, this does not seem like good behavior.


## Un-compressible Content

This is mainly a test of how good the algorithms are at detecting un-compressible input. The standard library only offers this feature with very conservative settings at level 1. Obviously there is no reason for the algorithms to try to compress input that cannot be compressed.  The only downside is that it might skip some compressible data on false detections.


# linear time compression (huffman only)

This compression library adds a special compression level, named `HuffmanOnly`, which allows near linear time compression. This is done by completely disabling matching of previous data, and only reduce the number of bits to represent each character. 

This means that often used characters, like 'e' and ' ' (space) in text use the fewest bits to represent, and rare characters like '¤' takes more bits to represent. For more information see [wikipedia](https://en.wikipedia.org/wiki/Huffman_coding) or this nice [video](https://youtu.be/ZdooBTdW5bM).

Since this type of compression has much less variance, the compression speed is mostly unaffected by the input data, and is usually more than *180MB/s* for a single core.

The downside is that the compression ratio is usually considerably worse than even the fastest conventional compression. The compression raio can never be better than 8:1 (12.5%). 

The linear time compression can be used as a "better than nothing" mode, where you cannot risk the encoder to slow down on some content. For comparison, the size of the "Twain" text is *233460 bytes* (+29% vs. level 1) and encode speed is 144MB/s (4.5x level 1). So in this case you trade a 30% size increase for a 4 times speedup.

For more information see my blog post on [Fast Linear Time Compression](http://blog.klauspost.com/constant-time-gzipzip-compression/).

This is implemented on Go 1.7 as "Huffman Only" mode, though not exposed for gzip.


# snappy package

The standard snappy package has now been improved. This repo contains a copy of the snappy repo.

I would advise to use the standard package: https://github.com/golang/snappy


# license

This code is licensed under the same conditions as the original Go code. See LICENSE file.
pgzip
=====

Go parallel gzip compression/decompression. This is a fully gzip compatible drop in replacement for "compress/gzip".

This will split compression into blocks that are compressed in parallel. 
This can be useful for compressing big amounts of data. The output is a standard gzip file.

The gzip decompression is modified so it decompresses ahead of the current reader. 
This means that reads will be non-blocking if the decompressor can keep ahead of your code reading from it. 
CRC calculation also takes place in a separate goroutine.

You should only use this if you are (de)compressing big amounts of data, 
say **more than 1MB** at the time, otherwise you will not see any benefit, 
and it will likely be faster to use the internal gzip library 
or [this package](https://github.com/klauspost/compress).

It is important to note that this library creates and reads *standard gzip files*. 
You do not have to match the compressor/decompressor to get the described speedups, 
and the gzip files are fully compatible with other gzip readers/writers.

A golang variant of this is [bgzf](https://godoc.org/github.com/biogo/hts/bgzf), 
which has the same feature, as well as seeking in the resulting file. 
The only drawback is a slightly bigger overhead compared to this and pure gzip. 
See a comparison below.

[![GoDoc][1]][2] [![Build Status][3]][4]

[1]: https://godoc.org/github.com/klauspost/pgzip?status.svg
[2]: https://godoc.org/github.com/klauspost/pgzip
[3]: https://travis-ci.org/klauspost/pgzip.svg
[4]: https://travis-ci.org/klauspost/pgzip

Installation
====
```go get github.com/klauspost/pgzip/...```

You might need to get/update the dependencies:

```
go get -u github.com/klauspost/compress
go get -u github.com/klauspost/crc32
```

Usage
====
[Godoc Doumentation](https://godoc.org/github.com/klauspost/pgzip)

To use as a replacement for gzip, exchange 

```import "compress/gzip"``` 
with 
```import gzip "github.com/klauspost/pgzip"```.

# Changes

* Oct 6, 2016: Fixed an issue if the destination writer returned an error.
* Oct 6, 2016: Better buffer reuse, should now generate less garbage.
* Oct 6, 2016: Output does not change based on write sizes.
* Dec 8, 2015: Decoder now supports the io.WriterTo interface, giving a speedup and less GC pressure.
* Oct 9, 2015: Reduced allocations by ~35 by using sync.Pool. ~15% overall speedup.

Changes in [github.com/klauspost/compress](https://github.com/klauspost/compress#changelog) are also carried over, so see that for more changes.

## Compression
The simplest way to use this is to simply do the same as you would when using [compress/gzip](http://golang.org/pkg/compress/gzip). 

To change the block size, use the added (*pgzip.Writer).SetConcurrency(blockSize, blocks int) function. With this you can control the approximate size of your blocks, as well as how many you want to be processing in parallel. Default values for this is SetConcurrency(250000, 16), meaning blocks are split at 250000 bytes and up to 16 blocks can be processing at once before the writer blocks.


Example:
```
var b bytes.Buffer
w := gzip.NewWriter(&b)
w.SetConcurrency(100000, 10)
w.Write([]byte("hello, world\n"))
w.Close()
```

To get any performance gains, you should at least be compressing more than 1 megabyte of data at the time.

You should at least have a block size of 100k and at least a number of blocks that match the number of cores your would like to utilize, but about twice the number of blocks would be the best.

Another side effect of this is, that it is likely to speed up your other code, since writes to the compressor only blocks if the compressor is already compressing the number of blocks you have specified. This also means you don't have worry about buffering input to the compressor.

## Decompression

Decompression works similar to compression. That means that you simply call pgzip the same way as you would call [compress/gzip](http://golang.org/pkg/compress/gzip). 

The only difference is that if you want to specify your own readahead, you have to use `pgzip.NewReaderN(r io.Reader, blockSize, blocks int)` to get a reader with your custom blocksizes. The `blockSize` is the size of each block decoded, and `blocks` is the maximum number of blocks that is decoded ahead.

See [Example on playground](http://play.golang.org/p/uHv1B5NbDh)

Performance
====
## Compression

See my blog post in [Benchmarks of Golang Gzip](https://blog.klauspost.com/go-gzipdeflate-benchmarks/).

Compression cost is usually about 0.2% with default settings with a block size of 250k.

Example with GOMAXPROC set to 8 (quad core with 8 hyperthreads)

Content is [Matt Mahoneys 10GB corpus](http://mattmahoney.net/dc/10gb.html). Compression level 6.

Compressor  | MB/sec   | speedup | size | size overhead (lower=better)
------------|----------|---------|------|---------
[gzip](http://golang.org/pkg/compress/gzip) (golang) | 7.21MB/s | 1.0x | 4786608902 | 0%
[gzip](http://github.com/klauspost/compress/gzip) (klauspost) | 10.98MB/s | 1.52x | 4781331645 | -0.11%
[pgzip](https://github.com/klauspost/pgzip) (klauspost) | 50.76MB/s|7.04x | 4784121440 | -0.052%
[bgzf](https://godoc.org/github.com/biogo/hts/bgzf) (biogo) | 38.65MB/s | 5.36x | 4924899484 | 2.889%
[pargzip](https://godoc.org/github.com/golang/build/pargzip) (builder) | 32.00MB/s | 4.44x | 4791226567 | 0.096%

pgzip also contains a [linear time compression](https://github.com/klauspost/compress#linear-time-compression) mode, that will allow compression at ~150MB per core per second, independent of the content.

See the [complete sheet](https://docs.google.com/spreadsheets/d/1nuNE2nPfuINCZJRMt6wFWhKpToF95I47XjSsc-1rbPQ/edit?usp=sharing) for different content types and compression settings.

## Decompression

The decompression speedup is there because it allows you to do other work while the decompression is taking place.

In the example above, the numbers are as follows on a 4 CPU machine:

Decompressor | Time | Speedup
-------------|------|--------
[gzip](http://golang.org/pkg/compress/gzip) (golang) | 1m28.85s | 0%
[pgzip](https://github.com/klauspost/pgzip) (golang) | 43.48s | 104%

But wait, since gzip decompression is inherently singlethreaded (aside from CRC calculation) how can it be more than 100% faster?  Because pgzip due to its design also acts as a buffer. When using unbuffered gzip, you are also waiting for io when you are decompressing. If the gzip decoder can keep up, it will always have data ready for your reader, and you will not be waiting for input to the gzip decompressor to complete.

This is pretty much an optimal situation for pgzip, but it reflects most common usecases for CPU intensive gzip usage.

I haven't included [bgzf](https://godoc.org/github.com/biogo/hts/bgzf) in this comparison, since it only can decompress files created by a compatible encoder, and therefore cannot be considered a generic gzip decompressor. But if you are able to compress your files with a bgzf compatible program, you can expect it to scale beyond 100%.

# License
This contains large portions of code from the go repository - see GO_LICENSE for more information. The changes are released under MIT License. See LICENSE for more information.
# cpuid
Package cpuid provides information about the CPU running the current program.

CPU features are detected on startup, and kept for fast access through the life of the application.
Currently x86 / x64 (AMD64) is supported, and no external C (cgo) code is used, which should make the library very easy to use.

You can access the CPU information by accessing the shared CPU variable of the cpuid library.

Package home: https://github.com/klauspost/cpuid

[![GoDoc][1]][2] [![Build Status][3]][4]

[1]: https://godoc.org/github.com/klauspost/cpuid?status.svg
[2]: https://godoc.org/github.com/klauspost/cpuid
[3]: https://travis-ci.org/klauspost/cpuid.svg
[4]: https://travis-ci.org/klauspost/cpuid

# features
## CPU Instructions
*  **CMOV** (i686 CMOV)
*  **NX** (NX (No-Execute) bit)
*  **AMD3DNOW** (AMD 3DNOW)
*  **AMD3DNOWEXT** (AMD 3DNowExt)
*  **MMX** (standard MMX)
*  **MMXEXT** (SSE integer functions or AMD MMX ext)
*  **SSE** (SSE functions)
*  **SSE2** (P4 SSE functions)
*  **SSE3** (Prescott SSE3 functions)
*  **SSSE3** (Conroe SSSE3 functions)
*  **SSE4** (Penryn SSE4.1 functions)
*  **SSE4A** (AMD Barcelona microarchitecture SSE4a instructions)
*  **SSE42** (Nehalem SSE4.2 functions)
*  **AVX** (AVX functions)
*  **AVX2** (AVX2 functions)
*  **FMA3** (Intel FMA 3)
*  **FMA4** (Bulldozer FMA4 functions)
*  **XOP** (Bulldozer XOP functions)
*  **F16C** (Half-precision floating-point conversion)
*  **BMI1** (Bit Manipulation Instruction Set 1)
*  **BMI2** (Bit Manipulation Instruction Set 2)
*  **TBM** (AMD Trailing Bit Manipulation)
*  **LZCNT** (LZCNT instruction)
*  **POPCNT** (POPCNT instruction)
*  **AESNI** (Advanced Encryption Standard New Instructions)
*  **CLMUL** (Carry-less Multiplication)
*  **HTT** (Hyperthreading (enabled))
*  **HLE** (Hardware Lock Elision)
*  **RTM** (Restricted Transactional Memory)
*  **RDRAND** (RDRAND instruction is available)
*  **RDSEED** (RDSEED instruction is available)
*  **ADX** (Intel ADX (Multi-Precision Add-Carry Instruction Extensions))
*  **SHA** (Intel SHA Extensions)
*  **AVX512F** (AVX-512 Foundation)
*  **AVX512DQ** (AVX-512 Doubleword and Quadword Instructions)
*  **AVX512IFMA** (AVX-512 Integer Fused Multiply-Add Instructions)
*  **AVX512PF** (AVX-512 Prefetch Instructions)
*  **AVX512ER** (AVX-512 Exponential and Reciprocal Instructions)
*  **AVX512CD** (AVX-512 Conflict Detection Instructions)
*  **AVX512BW** (AVX-512 Byte and Word Instructions)
*  **AVX512VL** (AVX-512 Vector Length Extensions)
*  **AVX512VBMI** (AVX-512 Vector Bit Manipulation Instructions)
*  **MPX** (Intel MPX (Memory Protection Extensions))
*  **ERMS** (Enhanced REP MOVSB/STOSB)
*  **RDTSCP** (RDTSCP Instruction)
*  **CX16** (CMPXCHG16B Instruction)
*  **SGX** (Software Guard Extensions, with activation details)

## Performance
*  **RDTSCP()** Returns current cycle count. Can be used for benchmarking.
*  **SSE2SLOW** (SSE2 is supported, but usually not faster)
*  **SSE3SLOW** (SSE3 is supported, but usually not faster)
*  **ATOM** (Atom processor, some SSSE3 instructions are slower)
*  **Cache line** (Probable size of a cache line).
*  **L1, L2, L3 Cache size** on newer Intel/AMD CPUs.

## Cpu Vendor/VM
* **Intel**
* **AMD**
* **VIA**
* **Transmeta**
* **NSC**
* **KVM**  (Kernel-based Virtual Machine)
* **MSVM** (Microsoft Hyper-V or Windows Virtual PC)
* **VMware**
* **XenHVM**

# installing

```go get github.com/klauspost/cpuid```

# example

```Go
package main

import (
	"fmt"
	"github.com/klauspost/cpuid"
)

func main() {
	// Print basic CPU information:
	fmt.Println("Name:", cpuid.CPU.BrandName)
	fmt.Println("PhysicalCores:", cpuid.CPU.PhysicalCores)
	fmt.Println("ThreadsPerCore:", cpuid.CPU.ThreadsPerCore)
	fmt.Println("LogicalCores:", cpuid.CPU.LogicalCores)
	fmt.Println("Family", cpuid.CPU.Family, "Model:", cpuid.CPU.Model)
	fmt.Println("Features:", cpuid.CPU.Features)
	fmt.Println("Cacheline bytes:", cpuid.CPU.CacheLine)
	fmt.Println("L1 Data Cache:", cpuid.CPU.Cache.L1D, "bytes")
	fmt.Println("L1 Instruction Cache:", cpuid.CPU.Cache.L1D, "bytes")
	fmt.Println("L2 Cache:", cpuid.CPU.Cache.L2, "bytes")
	fmt.Println("L3 Cache:", cpuid.CPU.Cache.L3, "bytes")

	// Test if we have a specific feature:
	if cpuid.CPU.SSE() {
		fmt.Println("We have Streaming SIMD Extensions")
	}
}
```

Sample output:
```
>go run main.go
Name: Intel(R) Core(TM) i5-2540M CPU @ 2.60GHz
PhysicalCores: 2
ThreadsPerCore: 2
LogicalCores: 4
Family 6 Model: 42
Features: CMOV,MMX,MMXEXT,SSE,SSE2,SSE3,SSSE3,SSE4.1,SSE4.2,AVX,AESNI,CLMUL
Cacheline bytes: 64
We have Streaming SIMD Extensions
```

# private package

In the "private" folder you can find an autogenerated version of the library you can include in your own packages.

For this purpose all exports are removed, and functions and constants are lowercased.

This is not a recommended way of using the library, but provided for convenience, if it is difficult for you to use external packages.

# license

This code is published under an MIT license. See LICENSE file for more information.
# CamelCase [![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/fatih/camelcase) [![Build Status](http://img.shields.io/travis/fatih/camelcase.svg?style=flat-square)](https://travis-ci.org/fatih/camelcase)

CamelCase is a Golang (Go) package to split the words of a camelcase type
string into a slice of words. It can be used to convert a camelcase word (lower
or upper case) into any type of word.

## Splitting rules:

1. If string is not valid UTF-8, return it without splitting as
   single item array.
2. Assign all unicode characters into one of 4 sets: lower case
   letters, upper case letters, numbers, and all other characters.
3. Iterate through characters of string, introducing splits
   between adjacent characters that belong to different sets.
4. Iterate through array of split strings, and if a given string
   is upper case:
   * if subsequent string is lower case:
     * move last character of upper case string to beginning of
       lower case string

## Install

```bash
go get github.com/fatih/camelcase
```

## Usage and examples

```go
splitted := camelcase.Split("GolangPackage")

fmt.Println(splitted[0], splitted[1]) // prints: "Golang", "Package"
```

Both lower camel case and upper camel case are supported. For more info please
check: [http://en.wikipedia.org/wiki/CamelCase](http://en.wikipedia.org/wiki/CamelCase)

Below are some example cases:

```
"" =>                     []
"lowercase" =>            ["lowercase"]
"Class" =>                ["Class"]
"MyClass" =>              ["My", "Class"]
"MyC" =>                  ["My", "C"]
"HTML" =>                 ["HTML"]
"PDFLoader" =>            ["PDF", "Loader"]
"AString" =>              ["A", "String"]
"SimpleXMLParser" =>      ["Simple", "XML", "Parser"]
"vimRPCPlugin" =>         ["vim", "RPC", "Plugin"]
"GL11Version" =>          ["GL", "11", "Version"]
"99Bottles" =>            ["99", "Bottles"]
"May5" =>                 ["May", "5"]
"BFG9000" =>              ["BFG", "9000"]
"BöseÜberraschung" =>     ["Böse", "Überraschung"]
"Two  spaces" =>          ["Two", "  ", "spaces"]
"BadUTF8\xe2\xe2\xa1" =>  ["BadUTF8\xe2\xe2\xa1"]
```
libseccomp-golang: Go Language Bindings for the libseccomp Project
===============================================================================
https://github.com/seccomp/libseccomp-golang
https://github.com/seccomp/libseccomp

The libseccomp library provides an easy to use, platform independent, interface
to the Linux Kernel's syscall filtering mechanism.  The libseccomp API is
designed to abstract away the underlying BPF based syscall filter language and
present a more conventional function-call based filtering interface that should
be familiar to, and easily adopted by, application developers.

The libseccomp-golang library provides a Go based interface to the libseccomp
library.

* Online Resources

The library source repository currently lives on GitHub at the following URLs:

	-> https://github.com/seccomp/libseccomp-golang
	-> https://github.com/seccomp/libseccomp

The project mailing list is currently hosted on Google Groups at the URL below,
please note that a Google account is not required to subscribe to the mailing
list.

	-> https://groups.google.com/d/forum/libseccomp

Documentation is also available at:

	-> https://godoc.org/github.com/seccomp/libseccomp-golang

* Installing the package

The libseccomp-golang bindings require at least Go v1.2.1 and GCC v4.8.4;
earlier versions may yield unpredictable results.  If you meet these
requirements you can install this package using the command below:

	$ go get github.com/seccomp/libseccomp-golang

* Testing the Library

A number of tests and lint related recipes are provided in the Makefile, if
you want to run the standard regression tests, you can excute the following:

	$ make check

In order to execute the 'make lint' recipe the 'golint' tool is needed, it
can be found at:

	-> https://github.com/golang/lint

`containers-golang` is a set of Go libraries used by container runtimes to generate and load seccomp mappings into the kernel.

seccomp (short for secure computing mode) is a BPF based syscall filter language and present a more conventional function-call based filtering interface that should be familiar to, and easily adopted by, application developers.

## Building
   make - Generates default.json file, which containes the whitelisted syscalls that can be used by container runtime engines like [CRI-O][cri-o], [Buildah][buildah], [Podman][podman] and [Docker][docker], and container runtimes like OCI [Runc][runc] to controll the syscalls available to containers.

### Supported build tags

   `seccomp`
   
## Contributing

When developing this library, please use `make` (or `make … BUILDTAGS=…`) to take advantage of the tests and validation.

## License

ASL 2.0

## Contact

- IRC: #[CRI-O](irc://irc.freenode.net:6667/#cri-o) on freenode.net

[cri-o]:   https://github.com/kubernetes-incubator/cri-o/pulls
[buildah]: https://github.com/projectatomic/buildah
[podman]:  https://github.com/projectatomic/podman
[docker]:  https://github.com/docker/docker
[runc]:    https://github.com/opencontainers/runc

[![GoDoc](https://godoc.org/github.com/xeipuuv/gojsonschema?status.svg)](https://godoc.org/github.com/xeipuuv/gojsonschema)
[![Build Status](https://travis-ci.org/xeipuuv/gojsonschema.svg)](https://travis-ci.org/xeipuuv/gojsonschema)

# gojsonschema

## Description

An implementation of JSON Schema for the Go  programming language. Supports draft-04, draft-06 and draft-07.

References :

* http://json-schema.org
* http://json-schema.org/latest/json-schema-core.html
* http://json-schema.org/latest/json-schema-validation.html

## Installation

```
go get github.com/xeipuuv/gojsonschema
```

Dependencies :
* [github.com/xeipuuv/gojsonpointer](https://github.com/xeipuuv/gojsonpointer)
* [github.com/xeipuuv/gojsonreference](https://github.com/xeipuuv/gojsonreference)
* [github.com/stretchr/testify/assert](https://github.com/stretchr/testify#assert-package)

## Usage

### Example

```go

package main

import (
    "fmt"
    "github.com/xeipuuv/gojsonschema"
)

func main() {

    schemaLoader := gojsonschema.NewReferenceLoader("file:///home/me/schema.json")
    documentLoader := gojsonschema.NewReferenceLoader("file:///home/me/document.json")

    result, err := gojsonschema.Validate(schemaLoader, documentLoader)
    if err != nil {
        panic(err.Error())
    }

    if result.Valid() {
        fmt.Printf("The document is valid\n")
    } else {
        fmt.Printf("The document is not valid. see errors :\n")
        for _, desc := range result.Errors() {
            fmt.Printf("- %s\n", desc)
        }
    }
}


```

#### Loaders

There are various ways to load your JSON data.
In order to load your schemas and documents,
first declare an appropriate loader :

* Web / HTTP, using a reference :

```go
loader := gojsonschema.NewReferenceLoader("http://www.some_host.com/schema.json")
```

* Local file, using a reference :

```go
loader := gojsonschema.NewReferenceLoader("file:///home/me/schema.json")
```

References use the URI scheme, the prefix (file://) and a full path to the file are required.

* JSON strings :

```go
loader := gojsonschema.NewStringLoader(`{"type": "string"}`)
```

* Custom Go types :

```go
m := map[string]interface{}{"type": "string"}
loader := gojsonschema.NewGoLoader(m)
```

And

```go
type Root struct {
	Users []User `json:"users"`
}

type User struct {
	Name string `json:"name"`
}

...

data := Root{}
data.Users = append(data.Users, User{"John"})
data.Users = append(data.Users, User{"Sophia"})
data.Users = append(data.Users, User{"Bill"})

loader := gojsonschema.NewGoLoader(data)
```

#### Validation

Once the loaders are set, validation is easy :

```go
result, err := gojsonschema.Validate(schemaLoader, documentLoader)
```

Alternatively, you might want to load a schema only once and process to multiple validations :

```go
schema, err := gojsonschema.NewSchema(schemaLoader)
...
result1, err := schema.Validate(documentLoader1)
...
result2, err := schema.Validate(documentLoader2)
...
// etc ...
```

To check the result :

```go
    if result.Valid() {
    	fmt.Printf("The document is valid\n")
    } else {
        fmt.Printf("The document is not valid. see errors :\n")
        for _, err := range result.Errors() {
        	// Err implements the ResultError interface
            fmt.Printf("- %s\n", err)
        }
    }
```


## Loading local schemas

By default `file` and `http(s)` references to external schemas are loaded automatically via the file system or via http(s). An external schema can also be loaded using a `SchemaLoader`.

```go
	sl := gojsonschema.NewSchemaLoader()
	loader1 := gojsonschema.NewStringLoader(`{ "type" : "string" }`)
	err := sl.AddSchema("http://some_host.com/string.json", loader1)
```

Alternatively if your schema already has an `$id` you can use the `AddSchemas` function
```go
	loader2 := gojsonschema.NewStringLoader(`{
			"$id" : "http://some_host.com/maxlength.json",
			"maxLength" : 5
		}`)
	err = sl.AddSchemas(loader2)
```

The main schema should be passed to the `Compile` function. This main schema can then directly reference the added schemas without needing to download them.
```go
	loader3 := gojsonschema.NewStringLoader(`{
		"$id" : "http://some_host.com/main.json",
		"allOf" : [
			{ "$ref" : "http://some_host.com/string.json" },
			{ "$ref" : "http://some_host.com/maxlength.json" }
		]
	}`)

	schema, err := sl.Compile(loader3)

	documentLoader := gojsonschema.NewStringLoader(`"hello world"`)

	result, err := schema.Validate(documentLoader)
```

It's also possible to pass a `ReferenceLoader` to the `Compile` function that references a loaded schema.

```go
err = sl.AddSchemas(loader3)
schema, err := sl.Compile(gojsonschema.NewReferenceLoader("http://some_host.com/main.json"))
``` 

Schemas added by `AddSchema` and `AddSchemas` are only validated when the entire schema is compiled, unless meta-schema validation is used.

## Using a specific draft
By default `gojsonschema` will try to detect the draft of a schema by using the `$schema` keyword and parse it in a strict draft-04, draft-06 or draft-07 mode. If `$schema` is missing, or the draft version is not explicitely set, a hybrid mode is used which merges together functionality of all drafts into one mode.

Autodectection can be turned off with the `AutoDetect` property. Specific draft versions can be specified with the `Draft` property.

```go
sl := gojsonschema.NewSchemaLoader()
sl.Draft = gojsonschema.Draft7
sl.AutoDetect = false
```

If autodetection is on (default), a draft-07 schema can savely reference draft-04 schemas and vice-versa, as long as `$schema` is specified in all schemas.

## Meta-schema validation
Schemas that are added using the `AddSchema`, `AddSchemas` and `Compile` can be validated against their meta-schema by setting the `Validate` property.

The following example will produce an error as `multipleOf` must be a number. If `Validate` is off (default), this error is only returned at the `Compile` step. 

```go
sl := gojsonschema.NewSchemaLoader()
sl.Validate = true
err := sl.AddSchemas(gojsonschema.NewStringLoader(`{
     $id" : "http://some_host.com/invalid.json",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "multipleOf" : true
}`))
 ```
``` 
 ```

Errors returned by meta-schema validation are more readable and contain more information, which helps significantly if you are developing a schema.

Meta-schema validation also works with a custom `$schema`. In case `$schema` is missing, or `AutoDetect` is set to `false`, the meta-schema of the used draft is used.


## Working with Errors

The library handles string error codes which you can customize by creating your own gojsonschema.locale and setting it
```go
gojsonschema.Locale = YourCustomLocale{}
```

However, each error contains additional contextual information. 

Newer versions of `gojsonschema` may have new additional errors, so code that uses a custom locale will need to be updated when this happens.

**err.Type()**: *string* Returns the "type" of error that occurred. Note you can also type check. See below

Note: An error of RequiredType has an err.Type() return value of "required"

    "required": RequiredError
    "invalid_type": InvalidTypeError
    "number_any_of": NumberAnyOfError
    "number_one_of": NumberOneOfError
    "number_all_of": NumberAllOfError
    "number_not": NumberNotError
    "missing_dependency": MissingDependencyError
    "internal": InternalError
    "const": ConstEror
    "enum": EnumError
    "array_no_additional_items": ArrayNoAdditionalItemsError
    "array_min_items": ArrayMinItemsError
    "array_max_items": ArrayMaxItemsError
    "unique": ItemsMustBeUniqueError
    "contains" : ArrayContainsError
    "array_min_properties": ArrayMinPropertiesError
    "array_max_properties": ArrayMaxPropertiesError
    "additional_property_not_allowed": AdditionalPropertyNotAllowedError
    "invalid_property_pattern": InvalidPropertyPatternError
    "invalid_property_name":  InvalidPropertyNameError
    "string_gte": StringLengthGTEError
    "string_lte": StringLengthLTEError
    "pattern": DoesNotMatchPatternError
    "multiple_of": MultipleOfError
    "number_gte": NumberGTEError
    "number_gt": NumberGTError
    "number_lte": NumberLTEError
    "number_lt": NumberLTError
    "condition_then" : ConditionThenError
    "condition_else" : ConditionElseError

**err.Value()**: *interface{}* Returns the value given

**err.Context()**: *gojsonschema.JsonContext* Returns the context. This has a String() method that will print something like this: (root).firstName

**err.Field()**: *string* Returns the fieldname in the format firstName, or for embedded properties, person.firstName. This returns the same as the String() method on *err.Context()* but removes the (root). prefix.

**err.Description()**: *string* The error description. This is based on the locale you are using. See the beginning of this section for overwriting the locale with a custom implementation.

**err.DescriptionFormat()**: *string* The error description format. This is relevant if you are adding custom validation errors afterwards to the result.

**err.Details()**: *gojsonschema.ErrorDetails* Returns a map[string]interface{} of additional error details specific to the error. For example, GTE errors will have a "min" value, LTE will have a "max" value. See errors.go for a full description of all the error details. Every error always contains a "field" key that holds the value of *err.Field()*

Note in most cases, the err.Details() will be used to generate replacement strings in your locales, and not used directly. These strings follow the text/template format i.e.
```
{{.field}} must be greater than or equal to {{.min}}
```

The library allows you to specify custom template functions, should you require more complex error message handling.
```go
gojsonschema.ErrorTemplateFuncs = map[string]interface{}{
	"allcaps": func(s string) string {
		return strings.ToUpper(s)
	},
}
```

Given the above definition, you can use the custom function `"allcaps"` in your localization templates:
```
{{allcaps .field}} must be greater than or equal to {{.min}}
```

The above error message would then be rendered with the `field` value in capital letters. For example:
```
"PASSWORD must be greater than or equal to 8"
```

Learn more about what types of template functions you can use in `ErrorTemplateFuncs` by referring to Go's [text/template FuncMap](https://golang.org/pkg/text/template/#FuncMap) type.

## Formats
JSON Schema allows for optional "format" property to validate instances against well-known formats. gojsonschema ships with all of the formats defined in the spec that you can use like this:

````json
{"type": "string", "format": "email"}
````

Not all formats defined in draft-07 are available. Implemented formats are:

* `date`
* `time`
* `date-time`
* `hostname`. Subdomains that start with a number are also supported, but this means that it doesn't strictly follow [RFC1034](http://tools.ietf.org/html/rfc1034#section-3.5) and has the implication that ipv4 addresses are also recognized as valid hostnames.
* `email`. Go's email parser deviates slightly from [RFC5322](https://tools.ietf.org/html/rfc5322). Includes unicode support.
* `idn-email`. Same caveat as `email`.
* `ipv4`
* `ipv6`
* `uri`. Includes unicode support.
* `uri-reference`. Includes unicode support.
* `iri`
* `iri-reference`
* `uri-template`
* `uuid`
* `regex`. Go uses the [RE2](https://github.com/google/re2/wiki/Syntax) engine and is not [ECMA262](http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf) compatible.
* `json-pointer`
* `relative-json-pointer`

`email`, `uri` and `uri-reference` use the same validation code as their unicode counterparts `idn-email`, `iri` and `iri-reference`. If you rely on unicode support you should use the specific 
unicode enabled formats for the sake of interoperability as other implementations might not support unicode in the regular formats.

The validation code for `uri`, `idn-email` and their relatives use mostly standard library code. Go 1.5 and 1.6 contain some minor bugs with handling URIs and unicode. You are encouraged to use Go 1.7+ if you rely on these formats.

For repetitive or more complex formats, you can create custom format checkers and add them to gojsonschema like this:

```go
// Define the format checker
type RoleFormatChecker struct {}

// Ensure it meets the gojsonschema.FormatChecker interface
func (f RoleFormatChecker) IsFormat(input interface{}) bool {

    asString, ok := input.(string)
    if ok == false {
        return false
    }

    return strings.HasPrefix("ROLE_", asString)
}

// Add it to the library
gojsonschema.FormatCheckers.Add("role", RoleFormatChecker{})
````

Now to use in your json schema:
````json
{"type": "string", "format": "role"}
````

Another example would be to check if the provided integer matches an id on database:

JSON schema:
```json
{"type": "integer", "format": "ValidUserId"}
```

```go
// Define the format checker
type ValidUserIdFormatChecker struct {}

// Ensure it meets the gojsonschema.FormatChecker interface
func (f ValidUserIdFormatChecker) IsFormat(input interface{}) bool {

    asFloat64, ok := input.(float64) // Numbers are always float64 here
    if ok == false {
        return false
    }

    // XXX
    // do the magic on the database looking for the int(asFloat64)

    return true
}

// Add it to the library
gojsonschema.FormatCheckers.Add("ValidUserId", ValidUserIdFormatChecker{})
````

Formats can also be removed, for example if you want to override one of the formats that is defined by default.

```go
gojsonschema.FormatCheckers.Remove("hostname")
```


## Additional custom validation
After the validation has run and you have the results, you may add additional
errors using `Result.AddError`. This is useful to maintain the same format within the resultset instead
of having to add special exceptions for your own errors. Below is an example.

```go
type AnswerInvalidError struct {
    gojsonschema.ResultErrorFields
}

func newAnswerInvalidError(context *gojsonschema.JsonContext, value interface{}, details gojsonschema.ErrorDetails) *AnswerInvalidError {
    err := AnswerInvalidError{}
    err.SetContext(context)
    err.SetType("custom_invalid_error")
    // it is important to use SetDescriptionFormat() as this is used to call SetDescription() after it has been parsed
    // using the description of err will be overridden by this.
    err.SetDescriptionFormat("Answer to the Ultimate Question of Life, the Universe, and Everything is {{.answer}}")
    err.SetValue(value)
    err.SetDetails(details)

    return &err
}

func main() {
    // ...
    schema, err := gojsonschema.NewSchema(schemaLoader)
    result, err := gojsonschema.Validate(schemaLoader, documentLoader)

    if true { // some validation
        jsonContext := gojsonschema.NewJsonContext("question", nil)
        errDetail := gojsonschema.ErrorDetails{
            "answer": 42,
        }
        result.AddError(
            newAnswerInvalidError(
                gojsonschema.NewJsonContext("answer", jsonContext),
                52,
                errDetail,
            ),
            errDetail,
        )
    }

    return result, err

}
```

This is especially useful if you want to add validation beyond what the
json schema drafts can provide such business specific logic.

## Uses

gojsonschema uses the following test suite :

https://github.com/json-schema/JSON-Schema-Test-Suite
# gojsonreference
An implementation of JSON Reference - Go language

## Dependencies
https://github.com/xeipuuv/gojsonpointer

## References
http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-07

http://tools.ietf.org/html/draft-pbryan-zyp-json-ref-03
# gojsonpointer
An implementation of JSON Pointer - Go language

## Usage
	jsonText := `{
		"name": "Bobby B",
		"occupation": {
			"title" : "King",
			"years" : 15,
			"heir" : "Joffrey B"			
		}
	}`
	
    var jsonDocument map[string]interface{}
    json.Unmarshal([]byte(jsonText), &jsonDocument)
    
    //create a JSON pointer
    pointerString := "/occupation/title"
    pointer, _ := NewJsonPointer(pointerString)
    
    //SET a new value for the "title" in the document     
    pointer.Set(jsonDocument, "Supreme Leader of Westeros")
    
    //GET the new "title" from the document
    title, _, _ := pointer.Get(jsonDocument)
    fmt.Println(title) //outputs "Supreme Leader of Westeros"
    
    //DELETE the "heir" from the document
    deletePointer := NewJsonPointer("/occupation/heir")
    deletePointer.Delete(jsonDocument)
    
    b, _ := json.Marshal(jsonDocument)
    fmt.Println(string(b))
    //outputs `{"name":"Bobby B","occupation":{"title":"Supreme Leader of Westeros","years":15}}`


## References
http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-07

### Note
The 4.Evaluation part of the previous reference, starting with 'If the currently referenced value is a JSON array, the reference token MUST contain either...' is not implemented.
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
# netns - network namespaces in go #

The netns package provides an ultra-simple interface for handling
network namespaces in go. Changing namespaces requires elevated
privileges, so in most cases this code needs to be run as root.

## Local Build and Test ##

You can use go get command:

    go get github.com/vishvananda/netns

Testing (requires root):

    sudo -E go test github.com/vishvananda/netns

## Example ##

```go
package main

import (
    "fmt"
    "net"
    "runtime"
    "github.com/vishvananda/netns"
)

func main() {
    // Lock the OS Thread so we don't accidentally switch namespaces
    runtime.LockOSThread()
    defer runtime.UnlockOSThread()

    // Save the current network namespace
    origns, _ := netns.Get()
    defer origns.Close()

    // Create a new network namespace
    newns, _ := netns.New()
    netns.Set(newns)
    defer newns.Close()

    // Do something with the network namespace
    ifaces, _ := net.Interfaces()
    fmt.Printf("Interfaces: %v\n", ifaces)

    // Switch back to the original namespace
    netns.Set(origns)
}

```
# netlink - netlink library for go #

[![Build Status](https://travis-ci.org/vishvananda/netlink.png?branch=master)](https://travis-ci.org/vishvananda/netlink) [![GoDoc](https://godoc.org/github.com/vishvananda/netlink?status.svg)](https://godoc.org/github.com/vishvananda/netlink)

The netlink package provides a simple netlink library for go. Netlink
is the interface a user-space program in linux uses to communicate with
the kernel. It can be used to add and remove interfaces, set ip addresses
and routes, and configure ipsec. Netlink communication requires elevated
privileges, so in most cases this code needs to be run as root. Since
low-level netlink messages are inscrutable at best, the library attempts
to provide an api that is loosely modeled on the CLI provided by iproute2.
Actions like `ip link add` will be accomplished via a similarly named
function like AddLink(). This library began its life as a fork of the
netlink functionality in
[docker/libcontainer](https://github.com/docker/libcontainer) but was
heavily rewritten to improve testability, performance, and to add new
functionality like ipsec xfrm handling.

## Local Build and Test ##

You can use go get command:

    go get github.com/vishvananda/netlink

Testing dependencies:

    go get github.com/vishvananda/netns

Testing (requires root):

    sudo -E go test github.com/vishvananda/netlink

## Examples ##

Add a new bridge and add eth1 into it:

```go
package main

import (
    "fmt"
    "github.com/vishvananda/netlink"
)

func main() {
    la := netlink.NewLinkAttrs()
    la.Name = "foo"
    mybridge := &netlink.Bridge{LinkAttrs: la}
    err := netlink.LinkAdd(mybridge)
    if err != nil  {
        fmt.Printf("could not add %s: %v\n", la.Name, err)
    }
    eth1, _ := netlink.LinkByName("eth1")
    netlink.LinkSetMaster(eth1, mybridge)
}

```
Note `NewLinkAttrs` constructor, it sets default values in structure. For now
it sets only `TxQLen` to `-1`, so kernel will set default by itself. If you're
using simple initialization(`LinkAttrs{Name: "foo"}`) `TxQLen` will be set to
`0` unless you specify it like `LinkAttrs{Name: "foo", TxQLen: 1000}`.

Add a new ip address to loopback:

```go
package main

import (
    "github.com/vishvananda/netlink"
)

func main() {
    lo, _ := netlink.LinkByName("lo")
    addr, _ := netlink.ParseAddr("169.254.169.254/32")
    netlink.AddrAdd(lo, addr)
}

```

## Future Work ##

Many pieces of netlink are not yet fully supported in the high-level
interface. Aspects of virtually all of the high-level objects don't exist.
Many of the underlying primitives are there, so its a matter of putting
the right fields into the high-level objects and making sure that they
are serialized and deserialized correctly in the Add and List methods.

There are also a few pieces of low level netlink functionality that still
need to be implemented. Routing rules are not in place and some of the
more advanced link types. Hopefully there is decent structure and testing
in place to make these fairly straightforward to add.

## Introduction

docker-credential-helpers is a suite of programs to use native stores to keep Docker credentials safe.

## Installation

Go to the [Releases](https://github.com/docker/docker-credential-helpers/releases) page and download the binary that works better for you. Put that binary in your `$PATH`, so Docker can find it.

### Building from scratch

The programs in this repository are written with the Go programming language. These instructions assume that you have previous knowledge about the language and you have it installed in your machine.

1 - Download the source and put it in your `$GOPATH` with `go get`.

```
$ go get github.com/docker/docker-credential-helpers
```

2 - Use `make` to build the program you want. That will leave any executable in the `bin` directory inside the repository.

```
$ cd $GOPATH/docker/docker-credentials-helpers
$ make osxkeychain
```

3 - Put that binary in your `$PATH`, so Docker can find it.

## Usage

### With the Docker Engine

Set the `credsStore` option in your `.docker/config.json` file with the suffix of the program you want to use. For instance, set it to `osxkeychain` if you want to use `docker-credential-osxkeychain`.

```json
{
  "credsStore": "osxkeychain"
}
```

### With other command line applications

The sub-package [client](https://godoc.org/github.com/docker/docker-credential-helpers/client) includes
functions to call external programs from your own command line applications.

There are three things you need to know if you need to interact with a helper:

1. The name of the program to execute, for instance `docker-credential-osxkeychain`.
2. The server address to identify the credentials, for instance `https://example.com`.
3. The username and secret to store, when you want to store credentials.

You can see examples of each function in the [client](https://godoc.org/github.com/docker/docker-credential-helpers/client) documentation.

### Available programs

1. osxkeychain: Provides a helper to use the OS X keychain as credentials store.
2. secretservice: Provides a helper to use the D-Bus secret service as credentials store.
3. wincred: Provides a helper to use Windows credentials manager as store.
4. pass: Provides a helper to use `pass` as credentials store.

#### Note

`pass` needs to be configured for `docker-credential-pass` to work properly.
It must be initialized with a `gpg2` key ID. Make sure your GPG key exists is in `gpg2` keyring as `pass` uses `gpg2` instead of the regular `gpg`.

## Development

A credential helper can be any program that can read values from the standard input. We use the first argument in the command line to differentiate the kind of command to execute. There are four valid values:

- `store`: Adds credentials to the keychain. The payload in the standard input is a JSON document with `ServerURL`, `Username` and `Secret`.
- `get`: Retrieves credentials from the keychain. The payload in the standard input is the raw value for the `ServerURL`.
- `erase`: Removes credentials from the keychain. The payload in the standard input is the raw value for the `ServerURL`.
- `list`: Lists stored credentials. There is no standard input payload.

This repository also includes libraries to implement new credentials programs in Go. Adding a new helper program is pretty easy. You can see how the OS X keychain helper works in the [osxkeychain](osxkeychain) directory.

1. Implement the interface `credentials.Helper` in `YOUR_PACKAGE/YOUR_PACKAGE_$GOOS.go`
2. Create a main program in `YOUR_PACKAGE/cmd/main_$GOOS.go`.
3. Add make tasks to build your program and run tests.

## License

MIT. See [LICENSE](LICENSE) for more information.
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

> **WARNING** this library is no longer actively developed, and will be integrated
> in the [docker/distribution][https://www.github.com/docker/distribution]
> repository in future.

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

# SpdyStream

A multiplexed stream library using spdy

## Usage

Client example (connecting to mirroring server without auth)

```go
package main

import (
	"fmt"
	"github.com/docker/spdystream"
	"net"
	"net/http"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		panic(err)
	}
	spdyConn, err := spdystream.NewConnection(conn, false)
	if err != nil {
		panic(err)
	}
	go spdyConn.Serve(spdystream.NoOpStreamHandler)
	stream, err := spdyConn.CreateStream(http.Header{}, nil, false)
	if err != nil {
		panic(err)
	}

	stream.Wait()

	fmt.Fprint(stream, "Writing to stream")

	buf := make([]byte, 25)
	stream.Read(buf)
	fmt.Println(string(buf))

	stream.Close()
}
```

Server example (mirroring server without auth)

```go
package main

import (
	"github.com/docker/spdystream"
	"net"
)

func main() {
	listener, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		panic(err)
	}
	for {
		conn, err := listener.Accept()
		if err != nil {
			panic(err)
		}
		spdyConn, err := spdystream.NewConnection(conn, true)
		if err != nil {
			panic(err)
		}
		go spdyConn.Serve(spdystream.MirrorStreamHandler)
	}
}
```

## Copyright and license

Copyright © 2014-2015 Docker, Inc. All rights reserved, except as follows. Code is released under the Apache 2.0 license. The README.md file, and files in the "docs" folder are licensed under the Creative Commons Attribution 4.0 International License under the terms and conditions set forth in the file "LICENSE.docs". You may obtain a duplicate copy of the same license, titled CC-BY-SA-4.0, at http://creativecommons.org/licenses/by/4.0/.
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
The Moby Project
================

![Moby Project logo](docs/static_files/moby-project-logo.png "The Moby Project")

Moby is an open-source project created by Docker to enable and accelerate software containerization.

It provides a "Lego set" of toolkit components, the framework for assembling them into custom container-based systems, and a place for all container enthusiasts and professionals to experiment and exchange ideas.
Components include container build tools, a container registry, orchestration tools, a runtime and more, and these can be used as building blocks in conjunction with other tools and projects.

## Principles

Moby is an open project guided by strong principles, aiming to be modular, flexible and without too strong an opinion on user experience.
It is open to the community to help set its direction.

- Modular: the project includes lots of components that have well-defined functions and APIs that work together.
- Batteries included but swappable: Moby includes enough components to build fully featured container system, but its modular architecture ensures that most of the components can be swapped by different implementations.
- Usable security: Moby provides secure defaults without compromising usability.
- Developer focused: The APIs are intended to be functional and useful to build powerful tools.
They are not necessarily intended as end user tools but as components aimed at developers.
Documentation and UX is aimed at developers not end users.

## Audience

The Moby Project is intended for engineers, integrators and enthusiasts looking to modify, hack, fix, experiment, invent and build systems based on containers.
It is not for people looking for a commercially supported system, but for people who want to work and learn with open source code.

## Relationship with Docker

The components and tools in the Moby Project are initially the open source components that Docker and the community have built for the Docker Project.
New projects can be added if they fit with the community goals. Docker is committed to using Moby as the upstream for the Docker Product.
However, other projects are also encouraged to use Moby as an upstream, and to reuse the components in diverse ways, and all these uses will be treated in the same way. External maintainers and contributors are welcomed.

The Moby project is not intended as a location for support or feature requests for Docker products, but as a place for contributors to work on open source code, fix bugs, and make the code more useful.
The releases are supported by the maintainers, community and users, on a best efforts basis only, and are not intended for customers who want enterprise or commercial support; Docker EE is the appropriate product for these use cases.

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

## Swagger definition

The API is defined by the [Swagger](http://swagger.io/specification/) definition in `api/swagger.yaml`. This definition can be used to:

1. Automatically generate documentation.
2. Automatically generate the Go server and client. (A work-in-progress.)
3. Provide a machine readable version of the API for introspecting what it can do, automatically generating clients for other languages, etc.

## Updating the API documentation

The API documentation is generated entirely from `api/swagger.yaml`. If you make updates to the API, edit this file to represent the change in the documentation.

The file is split into two main sections:

- `definitions`, which defines re-usable objects used in requests and responses
- `paths`, which defines the API endpoints (and some inline objects which don't need to be reusable)

To make an edit, first look for the endpoint you want to edit under `paths`, then make the required edits. Endpoints may reference reusable objects with `$ref`, which can be found in the `definitions` section.

There is hopefully enough example material in the file for you to copy a similar pattern from elsewhere in the file (e.g. adding new fields or endpoints), but for the full reference, see the [Swagger specification](https://github.com/docker/docker/issues/27919).

`swagger.yaml` is validated by `hack/validate/swagger` to ensure it is a valid Swagger definition. This is useful when making edits to ensure you are doing the right thing.

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
This package provides helper functions for dealing with strings
This package provides helper functions for dealing with signals across various operating systemsThe `contrib` directory contains scripts, images, and other helpful things
which are not part of the core docker distribution. Please note that they
could be out of date, since they do not receive the same attention as the
rest of the repository.
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
[![GoDoc](https://godoc.org/github.com/docker/go-connections?status.svg)](https://godoc.org/github.com/docker/go-connections)

# Introduction

go-connections provides common package to work with network connections.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-connections) for examples and documentation.

## License

go-connections is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
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
* [Ponzu CMS](https://ponzu-cms.org) - Headless CMS + automatic JSON API with auto-HTTPS, HTTP/2 Server Push, and flexible server framework.

If you are using Bolt in a project please send a pull request to add it to the list.
![PODMAN logo](../logo/podman-logo-source.svg)
# Test utils
Test utils provide common functions and structs for testing. It includes two structs:
* `PodmanTest`: Handle the *podman* command and other global resources like temporary
directory. It provides basic methods, like checking podman image and pod status. Test
suites should create their owner test *struct* as a composite of `PodmanTest`, and their
owner PodmanMakeOptions().

* `PodmanSession`: Store execution session data and related *methods*. Such like get command
output and so on. It can be used directly in the test suite, only embed it to your owner
session struct if you need expend it.

## Unittest for test/utils
To ensure neither *tests* nor *utils* break, There are unit-tests for each *functions* and
*structs* in `test/utils`. When you adding functions or structs to this *package*, please
update both unit-tests for it and this documentation.

### Run unit test for test/utils
Run unit test for test/utils.

```
make localunit
```

## Structure of the test utils and test suites
The test *utils* package is at the same level of test suites. Each test suites also have their
owner common functions and structs stored in `libpod_suite_test.go`.

# Ginkgo test framework
[Ginkgo](https://github.com/onsi/ginkgo) is a BDD testing framework. This allows
us to use native Golang to perform our tests and there is a strong affiliation
between Ginkgo and the Go test framework.

## Installing dependencies
The dependencies for integration really consists of three things:
* ginkgo binary
* ginkgo sources
* gomega sources

The following instructions assume your GOPATH is ~/go. Adjust as needed for your
environment.

### Installing ginkgo
Fetch and build ginkgo with the following command:
```
GOPATH=~/go go get -u github.com/onsi/ginkgo/ginkgo
```
Now install the ginkgo binary into your path:
```
install -D -m 755 "$GOPATH"/bin/ginkgo /usr/bin/
```
You now have a ginkgo binary and its sources in your GOPATH.

### Install gomega sources
The gomega sources can be simply installed with the command:
```
GOPATH=~/go go get github.com/onsi/gomega/...
```

# Integration Tests
Test suite for integration test for podman command line. It has its own structs:
* `PodmanTestIntegration`: Integration test *struct* as a composite of `PodmanTest`. It
set up the global options for *podman* command to ignore the environment influence from
different test system.

* `PodmanSessionIntegration`: This *struct* has it own *methods* for checking command
output with given format JSON by using *structs* defined in inspect package.

## Running the integration tests
You can run the entire suite of integration tests with the following command:

```
GOPATH=~/go ginkgo -v test/e2e/.
```

Note the trailing period on the command above. Also, **-v** invokes verbose mode.  That
switch is optional.

You can run a single file of integration tests using the go test command:

```
GOPATH=~/go go test -v test/e2e/libpod_suite_test.go test/e2e/config.go test/e2e/config_amd64.go test/e2e/your_test.go
```

#### Run all tests like PAPR
You can closely emulate the PAPR run for Fedora with the following command:

```
make integration.fedora
```

This will run lint, git-validation, and gofmt tests and then execute unit and integration
tests as well.

### Run tests in a container
In case you have issue running the tests locally on your machine, you can run
them in a container:
```
make shell
```

This will run a container and give you a shell and you can follow the instructions above.

# System test
System tests are used for testing the *podman* CLI in the context of a complete system. It
requires that *podman*, all dependencies, and configurations are in place.  The intention of
system testing is to match as closely as possible with real-world user/developer use-cases
and environments. The orchestration of the environments and tests is left to external
tooling.

* `PodmanTestSystem`: System test *struct* as a composite of `PodmanTest`. It will not add any
options to the command by default. When you run system test, you can set GLOBALOPTIONS,
PODMAN_SUBCMD_OPTIONS or PODMAN_BINARY in ENV to run the test suite for different test matrices.

## Run system test
You can run the test with following command:

```
make localsystem
```
# Installation Tests

The Dockerfiles in this directory attempt to install the RPMs built from this
repo into the target OS. Make the RPMs first with:

```
make -f .copr/Makefile srpm outdir=test/install/rpms
make -f .copr/Makefile build_binary outdir=test/install/rpms
```

Then, run a container image build using the Dockerfiles in this directory.SysInfo stores information about which features a kernel supports.
# OCI Hooks Configuration

For POSIX platforms, the [OCI runtime configuration][runtime-spec] supports [hooks][spec-hooks] for configuring custom actions related to the life cycle of the container.
The way you enable the hooks above is by editing the OCI runtime configuration before running the OCI runtime (e.g. [`runc`][runc]).
CRI-O and `podman create` create the OCI configuration for you, and this documentation allows developers to configure them to set their intended hooks.

One problem with hooks is that the runtime actually stalls execution of the container before running the hooks and stalls completion of the container, until all hooks complete.
This can cause some performance issues.
Also a lot of hooks just check if certain configuration is set and then exit early, without doing anything.
For example the [oci-systemd-hook][] only executes if the command is `init` or `systemd`, otherwise it just exits.
This means if we automatically enabled all hooks, every container would have to execute `oci-systemd-hook`, even if they don't run systemd inside of the container.
Performance would also suffer if we exectuted each hook at each stage ([pre-start][], [post-start][], and [post-stop][]).

The hooks configuration is documented in [`oci-hooks.5`](docs/oci-hooks.5.md).

[oci-systemd-hook]: https://github.com/projectatomic/oci-systemd-hook
[post-start]: https://github.com/opencontainers/runtime-spec/blob/v1.0.1/config.md#poststart
[post-stop]: https://github.com/opencontainers/runtime-spec/blob/v1.0.1/config.md#poststop
[pre-start]: https://github.com/opencontainers/runtime-spec/blob/v1.0.1/config.md#prestart
[runc]: https://github.com/opencontainers/runc
[runtime-spec]: https://github.com/opencontainers/runtime-spec/blob/v1.0.1/spec.md
[spec-hooks]: https://github.com/opencontainers/runtime-spec/blob/v1.0.1/config.md#posix-platform-hooks
## perftest : tool for benchmarking and profiling libpod library
perftest uses libpod as golang library and perform stress test and profile for CPU usage.

Build:

```
# cd $GOPATH/src/github.com/containers/libpod/contrib/perftest
# go build
# go install
```

Usage:

```
# perftest -h
Usage of perftest:

-count int
        count of loop counter for test (default 50)
-image string
        image-name to be used for test (default "docker.io/library/alpine:latest")

```

e.g.

```
# perftest
runc version spec: 1.0.1-dev
conmon version 1.12.0-dev, commit: b6c5cafeffa9b3cde89812207b29ccedd3102712

preparing test environment...
2018/11/05 16:52:14 profile: cpu profiling enabled, /tmp/profile626959338/cpu.pprof
Test Round: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
Profile data

        Create  Start   Stop    Delete
Min     0.23s   0.34s   2.12s   0.51s
Avg     0.25s   0.38s   2.13s   0.54s
Max     0.27s   0.48s   2.13s   0.70s
Total   12.33s  18.82s  106.47s 26.91s
2018/11/05 16:54:59 profile: cpu profiling disabled, /tmp/profile626959338/cpu.pprof

```

Analyse CPU profile.

```
# go tool pprof -http=":8081" $GOPATH/src/github.com/containers/libpod/contrib/perftest/perftest /tmp/profile626959338/cpu.pprof
```
- Open http://localhost:8081 in webbrowser![PODMAN logo](../../logo/podman-logo-source.svg)

A standard container image for `gofmt` and lint-checking the libpod
repository.  The [contributors guide contains the documentation for usage.](https://github.com/containers/libpod/blob/master/CONTRIBUTING.md#go-format-and-lint)
![PODMAN logo](../../logo/podman-logo-source.svg)

# Cirrus-CI

Similar to other integrated github CI/CD services, Cirrus utilizes a simple
YAML-based configuration/description file: ``.cirrus.yml``.  Ref: https://cirrus-ci.org/


## Workflow

All tasks execute in parallel, unless there are conditions or dependencies
which alter this behavior.  Within each task, each script executes in sequence,
so long as any previous script exited successfully.  The overall state of each
task (pass or fail) is set based on the exit status of the last script to execute.


### ``gating`` Task

***N/B: Steps below are performed by automation***

1. Launch a purpose-built container in Cirrus's community cluster.
   For container image details, please see
   [the contributors guide](https://github.com/containers/libpod/blob/master/CONTRIBUTING.md#go-format-and-lint).

3. ``validate``: Perform standard `make validate` source verification,
   Should run for less than a minute or two.

4. ``lint``: Execute regular `make lint` to check for any code cruft.
   Should also run for less than a few minutes.


### ``testing`` Task

***N/B: Steps below are performed by automation***

1. After `gating` passes, spin up one VM per
   `matrix: image_name` item. Once accessible, ``ssh``
   into each VM as the `root` user.

2. ``setup_environment.sh``: Configure root's `.bash_profile`
    for all subsequent scripts (each run in a new shell).  Any
    distribution-specific environment variables are also defined
    here.  For example, setting tags/flags to use compiling.

5. ``integration_test.sh``: Execute integration-testing.  This is
   much more involved, and relies on access to external
   resources like container images and code from other repositories.
   Total execution time is capped at 2-hours (includes all the above)
   but this script normally completes in less than an hour.


### ``optional_testing`` Task

***N/B: Steps below are performed by automation***

1. Optionally executes in parallel with ``testing``.  Requires
    **prior** to job-start, the magic string ``***CIRRUS: SYSTEM TEST***``
   is found in the pull-request *description*.  The *description* is the first
   text-box under the main *summary* line in the github WebUI.

2. ``setup_environment.sh``: Same as for other tasks.

3. ``system_test.sh``: Build both dependencies and libpod, install them,
   then execute `make localsystem` from the repository root.


### ``cache_images`` Task

Modifying the contents of cache-images is done by making changes to
one or more of the ``./contrib/cirrus/packer/*_setup.sh`` files.  Testing
those changes currently requires adding a temporary commit to a PR that
updates ``.cirrus.yml``:

* Remove all task sections except ``cache_images_task``.
* Remove the ``only_if`` condition and ``depends_on`` dependencies

The new image names will be displayed at the end of output, assuming the build
is successful, at that point the temporary commit may be removed.  Finally,
the new names may be used as ``image_name`` values in ``.cirrus.yml``.

***N/B: Steps below are performed by automation***

1. When a PR is merged (``$CIRRUS_BRANCH`` == ``master``), run another
   round of the ``gating`` and ``testing`` tasks (above).

2. Assuming tests pass, if the commit message contains the magic string
   ``***CIRRUS: REBUILD IMAGES***``, then this task continues.  Otherwise
   simply mark the master branch as 'passed'.

3. ``setup_environment.sh``: Same as for other tasks.

4. ``build_vm_images.sh``: Utilize [the packer tool](http://packer.io/docs/)
   to produce new VM images.  Create a new VM from each base-image, connect
   to them with ``ssh``, and perform the steps as defined by the
   ``$PACKER_BASE/libpod_images.json`` file:

    1. On a base-image VM, as root, copy the current state of the repository
       into ``/tmp/libpod``.
    2. Execute distribution-specific scripts to prepare the image for
       use by the ``integration_testing`` task (above).  For example,
       ``fedora_setup.sh``.
    3. If successful, shut down each VM and create a new GCE Image
       named with the base image, and the commit sha of the merge.

### Base-images

Base-images are VM disk-images specially prepared for executing as GCE VMs.
In particular, they run services on startup similar in purpose/function
as the standard 'cloud-init' services.

*  The google services are required for full support of ssh-key management
   and GCE OAuth capabilities.  Google provides native images in GCE
   with services pre-installed, for many platforms. For example,
   RHEL, CentOS, and Ubuntu.

*  Google does ***not*** provide any images for Fedora or Fedora Atomic
   Host (as of 11/2018), nor do they provide a base-image prepared to
   run packer for creating other images in the ``build_vm_images`` Task
   (above).

*  Base images do not need to be produced often, but doing so completely
   manually would be time-consuming and error-prone.  Therefor a special
   semi-automatic *Makefile* target is provided to assist with producing
   all the base-images: ``libpod_base_images``

To produce new base-images, including an `image-builder-image` (used by
the ``cache_images`` Task) some input parameters are required:

* ``GCP_PROJECT_ID``: The complete GCP project ID string e.g. foobar-12345
  identifying where the images will be stored.

* ``GOOGLE_APPLICATION_CREDENTIALS``: A *JSON* file containing
  credentials for a GCE service account.  This can be [a service
  account](https://cloud.google.com/docs/authentication/production#obtaining_and_providing_service_account_credentials_manually)
  or [end-user
  credentials](https://cloud.google.com/docs/authentication/end-user#creating_your_client_credentials)

* ``RHEL_IMAGE_FILE`` and ``RHEL_CSUM_FILE`` complete paths
  to a `rhel-server-ec2-*.raw.xz` and it's cooresponding
  checksum file.  These must be supplied manually because
  they're not available directly via URL like other images.

* ``RHSM_COMMAND`` contains the complete string needed to register
  the VM for installing package dependencies.  The VM will be de-registered
  upon completion.

*  Optionally, CSV's may be specified to ``PACKER_BUILDS``
   to limit the base-images produced.  For example,
   ``PACKER_BUILDS=fedora,image-builder-image``.

If there is an existing 'image-builder-image' within GCE, it may be utilized
to produce base-images (in addition to cache-images).  However it must be
created with support for nested-virtualization, and with elevated cloud
privileges (to access GCE, from within the GCE VM).  For example:

```
$ alias pgcloud='sudo podman run -it --rm -e AS_ID=$UID
    -e AS_USER=$USER -v $HOME:$HOME:z quay.io/cevich/gcloud_centos:latest'

$ URL=https://www.googleapis.com/auth
$ SCOPES=$URL/userinfo.email,$URL/compute,$URL/devstorage.full_control

# The --min-cpu-platform is critical for nested-virt.
$ pgcloud compute instances create $USER-making-images \
    --image-family image-builder-image \
    --boot-disk-size "200GB" \
    --min-cpu-platform "Intel Haswell" \
    --machine-type n1-standard-2 \
    --scopes $SCOPES
```

Alternatively, if there is no image-builder-image available yet, a bare-metal
CentOS 7 machine with network access to GCE is required.  Software dependencies
can be obtained from the ``packer/image-builder-image_base_setup.sh`` script.

In both cases, the following can be used to setup and build base-images.

```
$ IP_ADDRESS=1.2.3.4  # EXTERNAL_IP from command output above
$ rsync -av $PWD centos@$IP_ADDRESS:.
$ scp $GOOGLE_APPLICATION_CREDENTIALS centos@$IP_ADDRESS:.
$ ssh centos@$IP_ADDRESS
...
```

When ready, change to the ``packer`` sub-directory, and build the images:

```
$ cd libpod/contrib/cirrus/packer
$ make libpod_base_images GCP_PROJECT_ID=<VALUE> \
    GOOGLE_APPLICATION_CREDENTIALS=<VALUE> \
    RHEL_IMAGE_FILE=<VALUE> \
    RHEL_CSUM_FILE=<VALUE> \
    RHSM_COMMAND=<VALUE> \
    PACKER_BUILDS=<OPTIONAL>
```

Assuming this is successful (hence the semi-automatic part), packer will
produce a ``packer-manifest.json`` output file.  This contains the base-image
names suitable for updating in ``.cirrus.yml``, `env` keys ``*_BASE_IMAGE``.

On failure, it should be possible to determine the problem from the packer
output.  Sometimes that means setting `PACKER_LOG=1` and troubleshooting
the nested virt calls.  It's also possible to observe the (nested) qemu-kvm
console output.  Simply set the ``TTYDEV`` parameter, for example:

```
$ make libpod_base_images ... TTYDEV=$(tty)
  ...
```
These are definitions and scripts consumed by packer to produce the
various distribution images used for CI testing.  For more details
see the [Cirrus CI documentation](../README.md)
## `cni` ##

There are a wide variety of different [CNI][cni] network configurations. This
directory just contains an example configuration that can be used as the
basis for your own configuration.

To use this configuration, place it in `/etc/cni/net.d` (or the directory
specified by `cni_config_dir` in your `libpod.conf`).

In addition, you need to install the [CNI plugins][cni] necessary into
`/opt/cni/bin` (or the directory specified by `cni_plugin_dir`). The
two plugins necessary for the example CNI configurations are `portmap` and
`bridge`.

[cni]: https://github.com/containernetworking/plugins
![PODMAN logo](../../logo/podman-logo-source.svg)

# Podman Tutorials

## Links to a number of useful tutorials for the Podman utility.

**[Introduction Tutorial](https://github.com/containers/libpod/tree/master/docs/tutorials/podman_tutorial.md)**

Learn how to setup Podman and perform some basic commands with the utility.
# podman - Simple debugging tool for pods and images
podman is a daemonless container runtime for managing containers, pods, and container images.
It is intended as a counterpart to CRI-O, to provide low-level debugging not available through the CRI interface used by Kubernetes.
It can also act as a container runtime independent of CRI-O, creating and managing its own set of containers.

## Use cases
1. Create containers
2. Start, stop, signal, attach to, and inspect existing containers
3. Run new commands in existing containers
4. Push and pull images
5. List and inspect existing images
6. Create new images by committing changes within a container
7. Create pods
8. Start, stop, signal, and inspect existing pods
9. Populate pods with containers
