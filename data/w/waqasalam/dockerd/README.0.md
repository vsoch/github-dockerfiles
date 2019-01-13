Incremental file directory sync tools in golang.

```
BENCH_FILE_SIZE=10000 ./bench.test --test.bench .
BenchmarkCopyWithTar10-4                	    2000	    995242 ns/op
BenchmarkCopyWithTar50-4                	     300	   4710021 ns/op
BenchmarkCopyWithTar200-4               	     100	  16627260 ns/op
BenchmarkCopyWithTar1000-4              	      20	  60031459 ns/op
BenchmarkCPA10-4                        	    1000	   1678367 ns/op
BenchmarkCPA50-4                        	     500	   3690306 ns/op
BenchmarkCPA200-4                       	     200	   9495066 ns/op
BenchmarkCPA1000-4                      	      50	  29769289 ns/op
BenchmarkDiffCopy10-4                   	    2000	    943889 ns/op
BenchmarkDiffCopy50-4                   	     500	   3285950 ns/op
BenchmarkDiffCopy200-4                  	     200	   8563792 ns/op
BenchmarkDiffCopy1000-4                 	      50	  29511340 ns/op
BenchmarkDiffCopyProto10-4              	    2000	    944615 ns/op
BenchmarkDiffCopyProto50-4              	     500	   3334940 ns/op
BenchmarkDiffCopyProto200-4             	     200	   9420038 ns/op
BenchmarkDiffCopyProto1000-4            	      50	  30632429 ns/op
BenchmarkIncrementalDiffCopy10-4        	    2000	    691993 ns/op
BenchmarkIncrementalDiffCopy50-4        	    1000	   1304253 ns/op
BenchmarkIncrementalDiffCopy200-4       	     500	   3306519 ns/op
BenchmarkIncrementalDiffCopy1000-4      	     200	  10211343 ns/op
BenchmarkIncrementalDiffCopy5000-4      	      20	  55194427 ns/op
BenchmarkIncrementalDiffCopy10000-4     	      20	  91759289 ns/op
BenchmarkIncrementalCopyWithTar10-4     	    2000	   1020258 ns/op
BenchmarkIncrementalCopyWithTar50-4     	     300	   5348786 ns/op
BenchmarkIncrementalCopyWithTar200-4    	     100	  19495000 ns/op
BenchmarkIncrementalCopyWithTar1000-4   	      20	  70338507 ns/op
BenchmarkIncrementalRsync10-4           	      30	  45215754 ns/op
BenchmarkIncrementalRsync50-4           	      30	  45837260 ns/op
BenchmarkIncrementalRsync200-4          	      30	  48780614 ns/op
BenchmarkIncrementalRsync1000-4         	      20	  54801892 ns/op
BenchmarkIncrementalRsync5000-4         	      20	  84782542 ns/op
BenchmarkIncrementalRsync10000-4        	      10	 103355108 ns/op
BenchmarkRsync10-4                      	      30	  46776470 ns/op
BenchmarkRsync50-4                      	      30	  48601555 ns/op
BenchmarkRsync200-4                     	      20	  59642691 ns/op
BenchmarkRsync1000-4                    	      20	 101343010 ns/op
BenchmarkGnuTar10-4                     	     500	   3171448 ns/op
BenchmarkGnuTar50-4                     	     300	   5030296 ns/op
BenchmarkGnuTar200-4                    	     100	  10464313 ns/op
BenchmarkGnuTar1000-4                   	      50	  30375257 ns/op
```### fifo

[![Build Status](https://travis-ci.org/containerd/fifo.svg?branch=master)](https://travis-ci.org/containerd/fifo)

Go package for handling fifos in a sane way.

```
// OpenFifo opens a fifo. Returns io.ReadWriteCloser.
// Context can be used to cancel this function until open(2) has not returned.
// Accepted flags:
// - syscall.O_CREAT - create new fifo if one doesn't exist
// - syscall.O_RDONLY - open fifo only from reader side
// - syscall.O_WRONLY - open fifo only from writer side
// - syscall.O_RDWR - open fifo from both sides, never block on syscall level
// - syscall.O_NONBLOCK - return io.ReadWriteCloser even if other side of the
//     fifo isn't open. read/write will be connected after the actual fifo is
//     open or after fifo is closed.
func OpenFifo(ctx context.Context, fn string, flag int, perm os.FileMode) (io.ReadWriteCloser, error)


// Read from a fifo to a byte array.
func (f *fifo) Read(b []byte) (int, error)


// Write from byte array to a fifo.
func (f *fifo) Write(b []byte) (int, error)


// Close the fifo. Next reads/writes will error. This method can also be used
// before open(2) has returned and fifo was never opened.
func (f *fifo) Close() error 
```
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
bbolt
=====

[![Go Report Card](https://goreportcard.com/badge/github.com/etcd-io/bbolt?style=flat-square)](https://goreportcard.com/report/github.com/etcd-io/bbolt)
[![Coverage](https://codecov.io/gh/etcd-io/bbolt/branch/master/graph/badge.svg)](https://codecov.io/gh/etcd-io/bbolt)
[![Build Status Travis](https://img.shields.io/travis/etcd-io/bboltlabs.svg?style=flat-square&&branch=master)](https://travis-ci.com/etcd-io/bbolt)
[![Godoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](https://godoc.org/github.com/etcd-io/bbolt)
[![Releases](https://img.shields.io/github/release/etcd-io/bbolt/all.svg?style=flat-square)](https://github.com/etcd-io/bbolt/releases)
[![LICENSE](https://img.shields.io/github/license/etcd-io/bbolt.svg?style=flat-square)](https://github.com/etcd-io/bbolt/blob/master/LICENSE)

bbolt is a fork of [Ben Johnson's][gh_ben] [Bolt][bolt] key/value
store. The purpose of this fork is to provide the Go community with an active
maintenance and development target for Bolt; the goal is improved reliability
and stability. bbolt includes bug fixes, performance enhancements, and features
not found in Bolt while preserving backwards compatibility with the Bolt API.

Bolt is a pure Go key/value store inspired by [Howard Chu's][hyc_symas]
[LMDB project][lmdb]. The goal of the project is to provide a simple,
fast, and reliable database for projects that don't require a full database
server such as Postgres or MySQL.

Since Bolt is meant to be used as such a low-level piece of functionality,
simplicity is key. The API will be small and only focus on getting values
and setting values. That's it.

[gh_ben]: https://github.com/benbjohnson
[bolt]: https://github.com/boltdb/bolt
[hyc_symas]: https://twitter.com/hyc_symas
[lmdb]: http://symas.com/mdb/

## Project Status

Bolt is stable, the API is fixed, and the file format is fixed. Full unit
test coverage and randomized black box testing are used to ensure database
consistency and thread safety. Bolt is currently used in high-load production
environments serving databases as large as 1TB. Many companies such as
Shopify and Heroku use Bolt-backed services every day.

## Project versioning

bbolt uses [semantic versioning](http://semver.org).
API should not change between patch and minor releases.
New minor versions may add additional features to the API.

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
$ go get go.etcd.io/bbolt/...
```

This will retrieve the library and install the `bolt` command line utility into
your `$GOBIN` path.


### Importing bbolt

To use bbolt as an embedded key-value store, import as:

```go
import bolt "go.etcd.io/bbolt"

db, err := bolt.Open(path, 0666, nil)
if err != nil {
  return err
}
defer db.Close()
```


### Opening a database

The top-level object in Bolt is a `DB`. It is represented as a single file on
your disk and represents a consistent snapshot of your data.

To open your database, simply use the `bolt.Open()` function:

```go
package main

import (
	"log"

	bolt "go.etcd.io/bbolt"
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
system's page cache. See the [`Tx`](https://godoc.org/go.etcd.io/bbolt#Tx)
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

Bolt is a relatively small code base (<5KLOC) for an embedded, serializable,
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

* [Algernon](https://github.com/xyproto/algernon) - A HTTP/2 web server with built-in support for Lua. Uses BoltDB as the default database backend.
* [Bazil](https://bazil.org/) - A file system that lets your data reside where it is most convenient for it to reside.
* [bolter](https://github.com/hasit/bolter) - Command-line app for viewing BoltDB file in your terminal.
* [boltcli](https://github.com/spacewander/boltcli) - the redis-cli for boltdb with Lua script support.
* [BoltHold](https://github.com/timshannon/bolthold) - An embeddable NoSQL store for Go types built on BoltDB
* [BoltStore](https://github.com/yosssi/boltstore) - Session store using Bolt.
* [Boltdb Boilerplate](https://github.com/bobintornado/boltdb-boilerplate) - Boilerplate wrapper around bolt aiming to make simple calls one-liners.
* [BoltDbWeb](https://github.com/evnix/boltdbweb) - A web based GUI for BoltDB files.
* [bleve](http://www.blevesearch.com/) - A pure Go search engine similar to ElasticSearch that uses Bolt as the default storage backend.
* [btcwallet](https://github.com/btcsuite/btcwallet) - A bitcoin wallet.
* [buckets](https://github.com/joyrexus/buckets) - a bolt wrapper streamlining
  simple tx and key scans.
* [cayley](https://github.com/google/cayley) - Cayley is an open-source graph database using Bolt as optional backend.
* [ChainStore](https://github.com/pressly/chainstore) - Simple key-value interface to a variety of storage engines organized as a chain of operations.
* [Consul](https://github.com/hashicorp/consul) - Consul is service discovery and configuration made easy. Distributed, highly available, and datacenter-aware.
* [DVID](https://github.com/janelia-flyem/dvid) - Added Bolt as optional storage engine and testing it against Basho-tuned leveldb.
* [dcrwallet](https://github.com/decred/dcrwallet) - A wallet for the Decred cryptocurrency.
* [drive](https://github.com/odeke-em/drive) - drive is an unofficial Google Drive command line client for \*NIX operating systems.
* [event-shuttle](https://github.com/sclasen/event-shuttle) - A Unix system service to collect and reliably deliver messages to Kafka.
* [Freehold](http://tshannon.bitbucket.org/freehold/) - An open, secure, and lightweight platform for your files and data.
* [Go Report Card](https://goreportcard.com/) - Go code quality report cards as a (free and open source) service.
* [GoWebApp](https://github.com/josephspurrier/gowebapp) - A basic MVC web application in Go using BoltDB.
* [GoShort](https://github.com/pankajkhairnar/goShort) - GoShort is a URL shortener written in Golang and BoltDB for persistent key/value storage and for routing it's using high performent HTTPRouter.
* [gopherpit](https://github.com/gopherpit/gopherpit) - A web service to manage Go remote import paths with custom domains
* [Gitchain](https://github.com/gitchain/gitchain) - Decentralized, peer-to-peer Git repositories aka "Git meets Bitcoin".
* [InfluxDB](https://influxdata.com) - Scalable datastore for metrics, events, and real-time analytics.
* [ipLocator](https://github.com/AndreasBriese/ipLocator) - A fast ip-geo-location-server using bolt with bloom filters.
* [ipxed](https://github.com/kelseyhightower/ipxed) - Web interface and api for ipxed.
* [Ironsmith](https://github.com/timshannon/ironsmith) - A simple, script-driven continuous integration (build - > test -> release) tool, with no external dependencies
* [Kala](https://github.com/ajvb/kala) - Kala is a modern job scheduler optimized to run on a single node. It is persistent, JSON over HTTP API, ISO 8601 duration notation, and dependent jobs.
* [LedisDB](https://github.com/siddontang/ledisdb) - A high performance NoSQL, using Bolt as optional storage.
* [lru](https://github.com/crowdriff/lru) - Easy to use Bolt-backed Least-Recently-Used (LRU) read-through cache with chainable remote stores.
* [mbuckets](https://github.com/abhigupta912/mbuckets) - A Bolt wrapper that allows easy operations on multi level (nested) buckets.
* [MetricBase](https://github.com/msiebuhr/MetricBase) - Single-binary version of Graphite.
* [MuLiFS](https://github.com/dankomiocevic/mulifs) - Music Library Filesystem creates a filesystem to organise your music files.
* [Operation Go: A Routine Mission](http://gocode.io) - An online programming game for Golang using Bolt for user accounts and a leaderboard.
* [photosite/session](https://godoc.org/bitbucket.org/kardianos/photosite/session) - Sessions for a photo viewing site.
* [Prometheus Annotation Server](https://github.com/oliver006/prom_annotation_server) - Annotation server for PromDash & Prometheus service monitoring system.
* [reef-pi](https://github.com/reef-pi/reef-pi) - reef-pi is an award winning, modular, DIY reef tank controller using easy to learn electronics based on a Raspberry Pi.
* [Request Baskets](https://github.com/darklynx/request-baskets) - A web service to collect arbitrary HTTP requests and inspect them via REST API or simple web UI, similar to [RequestBin](http://requestb.in/) service
* [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Highly scalable distributed key~file system with O(1) disk read.
* [stow](https://github.com/djherbis/stow) -  a persistence manager for objects
  backed by boltdb.
* [Storm](https://github.com/asdine/storm) - Simple and powerful ORM for BoltDB.
* [SimpleBolt](https://github.com/xyproto/simplebolt) - A simple way to use BoltDB. Deals mainly with strings.
* [Skybox Analytics](https://github.com/skybox/skybox) - A standalone funnel analysis tool for web analytics.
* [Scuttlebutt](https://github.com/benbjohnson/scuttlebutt) - Uses Bolt to store and process all Twitter mentions of GitHub projects.
* [tentacool](https://github.com/optiflows/tentacool) - REST api server to manage system stuff (IP, DNS, Gateway...) on a linux server.
* [torrent](https://github.com/anacrolix/torrent) - Full-featured BitTorrent client package and utilities in Go. BoltDB is a storage backend in development.
* [Wiki](https://github.com/peterhellberg/wiki) - A tiny wiki using Goji, BoltDB and Blackfriday.

If you are using Bolt in a project please send a pull request to add it to the list.
# gotest.tools

A collection of packages to augment `testing` and support common patterns.

[![GoDoc](https://godoc.org/gotest.tools?status.svg)](https://godoc.org/gotest.tools)
[![CircleCI](https://circleci.com/gh/gotestyourself/gotestyourself/tree/master.svg?style=shield)](https://circleci.com/gh/gotestyourself/gotestyourself/tree/master)
[![Go Reportcard](https://goreportcard.com/badge/gotest.tools)](https://goreportcard.com/report/gotest.tools)


## Packages

* [assert](http://godoc.org/gotest.tools/assert) -
  compare values and fail the test when a comparison fails
* [env](http://godoc.org/gotest.tools/env) -
  test code which uses environment variables
* [fs](http://godoc.org/gotest.tools/fs) -
  create temporary files and compare a filesystem tree to an expected value
* [golden](http://godoc.org/gotest.tools/golden) -
  compare large multi-line strings against values frozen in golden files
* [icmd](http://godoc.org/gotest.tools/icmd) -
  execute binaries and test the output
* [poll](http://godoc.org/gotest.tools/poll) -
  test asynchronous code by polling until a desired state is reached
* [skip](http://godoc.org/gotest.tools/skip) -
  skip a test and print the source code of the condition used to skip the test

## Related

* [gotest.tools/gotestsum](https://github.com/gotestyourself/gotestsum) - go test runner with custom output
* [maxbrunsfeld/counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) - generate fakes for interfaces
* [jonboulle/clockwork](https://github.com/jonboulle/clockwork) - a fake clock for testing code that uses `time`
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

under the MIT License: http://mattn.mit-license.org/2017

# Author

Yasuhiro Matsumoto (a.k.a mattn)
le_go
=====

Golang client library for logentries.com

It is compatible with http://golang.org/pkg/log/#Logger
and also implements http://golang.org/pkg/io/#Writer

[![GoDoc](https://godoc.org/github.com/bsphere/le_go?status.png)](https://godoc.org/github.com/bsphere/le_go)

[![Build Status](https://travis-ci.org/bsphere/le_go.svg)](https://travis-ci.org/bsphere/le_go)

Usage
-----
Add a new manual TCP token log at [logentries.com](https://logentries.com/quick-start/) and copy the [token](https://logentries.com/doc/input-token/).

Installation: `go get github.com/bsphere/le_go`

**Note:** The Logger is blocking, it can be easily run in a goroutine by calling `go le.Println(...)`

```go
package main

import "github.com/bsphere/le_go"

func main() {
	le, err := le_go.Connect("XXXX-XXXX-XXXX-XXXX") // replace with token
	if err != nil {
		panic(err)
	}

	defer le.Close()

	le.Println("another test message")
}
```

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
MessagePack Code Generator [![Build Status](https://travis-ci.org/tinylib/msgp.svg?branch=master)](https://travis-ci.org/tinylib/msgp)
=======

This is a code generation tool and serialization library for [MessagePack](http://msgpack.org). You can read more about MessagePack [in the wiki](http://github.com/tinylib/msgp/wiki), or at [msgpack.org](http://msgpack.org).

### Why?

- Use Go as your schema language
- Performance
- [JSON interop](http://godoc.org/github.com/tinylib/msgp/msgp#CopyToJSON)
- [User-defined extensions](http://github.com/tinylib/msgp/wiki/Using-Extensions)
- Type safety
- Encoding flexibility

### Quickstart

In a source file, include the following directive:

```go
//go:generate msgp
```

The `msgp` command will generate serialization methods for all exported type declarations in the file.

You can [read more about the code generation options here](http://github.com/tinylib/msgp/wiki/Using-the-Code-Generator).

### Use

Field names can be set in much the same way as the `encoding/json` package. For example:

```go
type Person struct {
	Name       string `msg:"name"`
	Address    string `msg:"address"`
	Age        int    `msg:"age"`
	Hidden     string `msg:"-"` // this field is ignored
	unexported bool             // this field is also ignored
}
```

By default, the code generator will satisfy `msgp.Sizer`, `msgp.Encodable`, `msgp.Decodable`, 
`msgp.Marshaler`, and `msgp.Unmarshaler`. Carefully-designed applications can use these methods to do
marshalling/unmarshalling with zero heap allocations.

While `msgp.Marshaler` and `msgp.Unmarshaler` are quite similar to the standard library's
`json.Marshaler` and `json.Unmarshaler`, `msgp.Encodable` and `msgp.Decodable` are useful for 
stream serialization. (`*msgp.Writer` and `*msgp.Reader` are essentially protocol-aware versions
of `*bufio.Writer` and `*bufio.Reader`, respectively.)

### Features

 - Extremely fast generated code
 - Test and benchmark generation
 - JSON interoperability (see `msgp.CopyToJSON() and msgp.UnmarshalAsJSON()`)
 - Support for complex type declarations
 - Native support for Go's `time.Time`, `complex64`, and `complex128` types 
 - Generation of both `[]byte`-oriented and `io.Reader/io.Writer`-oriented methods
 - Support for arbitrary type system extensions
 - [Preprocessor directives](http://github.com/tinylib/msgp/wiki/Preprocessor-Directives)
 - File-based dependency model means fast codegen regardless of source tree size.

Consider the following:
```go
const Eight = 8
type MyInt int
type Data []byte

type Struct struct {
	Which  map[string]*MyInt `msg:"which"`
	Other  Data              `msg:"other"`
	Nums   [Eight]float64    `msg:"nums"`
}
```
As long as the declarations of `MyInt` and `Data` are in the same file as `Struct`, the parser will determine that the type information for `MyInt` and `Data` can be passed into the definition of `Struct` before its methods are generated.

#### Extensions

MessagePack supports defining your own types through "extensions," which are just a tuple of
the data "type" (`int8`) and the raw binary. You [can see a worked example in the wiki.](http://github.com/tinylib/msgp/wiki/Using-Extensions)

### Status

Mostly stable, in that no breaking changes have been made to the `/msgp` library in more than a year. Newer versions
of the code may generate different code than older versions for performance reasons. I (@philhofer) am aware of a
number of stability-critical commercial applications that use this code with good results. But, caveat emptor.

You can read more about how `msgp` maps MessagePack types onto Go types [in the wiki](http://github.com/tinylib/msgp/wiki).

Here some of the known limitations/restrictions:

- Identifiers from outside the processed source file are assumed (optimistically) to satisfy the generator's interfaces. If this isn't the case, your code will fail to compile.
- Like most serializers, `chan` and `func` fields are ignored, as well as non-exported fields.
- Encoding of `interface{}` is limited to built-ins or types that have explicit encoding methods.
- _Maps must have `string` keys._ This is intentional (as it preserves JSON interop.) Although non-string map keys are not forbidden by the MessagePack standard, many serializers impose this restriction. (It also means *any* well-formed `struct` can be de-serialized into a `map[string]interface{}`.) The only exception to this rule is that the deserializers will allow you to read map keys encoded as `bin` types, due to the fact that some legacy encodings permitted this. (However, those values will still be cast to Go `string`s, and they will be converted to `str` types when re-encoded. It is the responsibility of the user to ensure that map keys are UTF-8 safe in this case.) The same rules hold true for JSON translation.

If the output compiles, then there's a pretty good chance things are fine. (Plus, we generate tests for you.) *Please, please, please* file an issue if you think the generator is writing broken code.

### Performance

If you like benchmarks, see [here](http://bravenewgeek.com/so-you-wanna-go-fast/) and [here](https://github.com/alecthomas/go_serialization_benchmarks).

As one might expect, the generated methods that deal with `[]byte` are faster for small objects, but the `io.Reader/Writer` methods are generally more memory-efficient (and, at some point, faster) for large (> 2KB) objects.
[![Build Status](https://travis-ci.org/miekg/dns.svg?branch=master)](https://travis-ci.org/miekg/dns)
[![Code Coverage](https://img.shields.io/codecov/c/github/miekg/dns/master.svg)](https://codecov.io/github/miekg/dns?branch=master)
[![Go Report Card](https://goreportcard.com/badge/github.com/miekg/dns)](https://goreportcard.com/report/miekg/dns)
[![](https://godoc.org/github.com/miekg/dns?status.svg)](https://godoc.org/github.com/miekg/dns)

# Alternative (more granular) approach to a DNS library

> Less is more.

Complete and usable DNS library. All widely used Resource Records are supported, including the
DNSSEC types. It follows a lean and mean philosophy. If there is stuff you should know as a DNS
programmer there isn't a convenience function for it. Server side and client side programming is
supported, i.e. you can build servers and resolvers with it.

We try to keep the "master" branch as sane as possible and at the bleeding edge of standards,
avoiding breaking changes wherever reasonable. We support the last two versions of Go.

# Goals

* KISS;
* Fast;
* Small API. If it's easy to code in Go, don't make a function for it.

# Users

A not-so-up-to-date-list-that-may-be-actually-current:

* https://github.com/coredns/coredns
* https://cloudflare.com
* https://github.com/abh/geodns
* http://www.statdns.com/
* http://www.dnsinspect.com/
* https://github.com/chuangbo/jianbing-dictionary-dns
* http://www.dns-lg.com/
* https://github.com/fcambus/rrda
* https://github.com/kenshinx/godns
* https://github.com/skynetservices/skydns
* https://github.com/hashicorp/consul
* https://github.com/DevelopersPL/godnsagent
* https://github.com/duedil-ltd/discodns
* https://github.com/StalkR/dns-reverse-proxy
* https://github.com/tianon/rawdns
* https://mesosphere.github.io/mesos-dns/
* https://pulse.turbobytes.com/
* https://play.google.com/store/apps/details?id=com.turbobytes.dig
* https://github.com/fcambus/statzone
* https://github.com/benschw/dns-clb-go
* https://github.com/corny/dnscheck for http://public-dns.info/
* https://namesmith.io
* https://github.com/miekg/unbound
* https://github.com/miekg/exdns
* https://dnslookup.org
* https://github.com/looterz/grimd
* https://github.com/phamhongviet/serf-dns
* https://github.com/mehrdadrad/mylg
* https://github.com/bamarni/dockness
* https://github.com/fffaraz/microdns
* http://kelda.io
* https://github.com/ipdcode/hades (JD.COM)
* https://github.com/StackExchange/dnscontrol/
* https://www.dnsperf.com/
* https://dnssectest.net/
* https://dns.apebits.com
* https://github.com/oif/apex
* https://github.com/jedisct1/dnscrypt-proxy
* https://github.com/jedisct1/rpdns

Send pull request if you want to be listed here.

# Features

* UDP/TCP queries, IPv4 and IPv6;
* RFC 1035 zone file parsing ($INCLUDE, $ORIGIN, $TTL and $GENERATE (for all record types) are supported;
* Fast:
    * Reply speed around ~ 80K qps (faster hardware results in more qps);
    * Parsing RRs ~ 100K RR/s, that's 5M records in about 50 seconds;
* Server side programming (mimicking the net/http package);
* Client side programming;
* DNSSEC: signing, validating and key generation for DSA, RSA, ECDSA and Ed25519;
* EDNS0, NSID, Cookies;
* AXFR/IXFR;
* TSIG, SIG(0);
* DNS over TLS: optional encrypted connection between client and server;
* DNS name compression;
* Depends only on the standard library.

Have fun!

Miek Gieben  -  2010-2012  -  <miek@miek.nl>

# Building

Building is done with the `go` tool. If you have setup your GOPATH correctly, the following should
work:

    go get github.com/miekg/dns
    go build github.com/miekg/dns

## Examples

A short "how to use the API" is at the beginning of doc.go (this also will show
when you call `godoc github.com/miekg/dns`).

Example programs can be found in the `github.com/miekg/exdns` repository.

## Supported RFCs

*all of them*

* 103{4,5} - DNS standard
* 1348 - NSAP record (removed the record)
* 1982 - Serial Arithmetic
* 1876 - LOC record
* 1995 - IXFR
* 1996 - DNS notify
* 2136 - DNS Update (dynamic updates)
* 2181 - RRset definition - there is no RRset type though, just []RR
* 2537 - RSAMD5 DNS keys
* 2065 - DNSSEC (updated in later RFCs)
* 2671 - EDNS record
* 2782 - SRV record
* 2845 - TSIG record
* 2915 - NAPTR record
* 2929 - DNS IANA Considerations
* 3110 - RSASHA1 DNS keys
* 3225 - DO bit (DNSSEC OK)
* 340{1,2,3} - NAPTR record
* 3445 - Limiting the scope of (DNS)KEY
* 3597 - Unknown RRs
* 403{3,4,5} - DNSSEC + validation functions
* 4255 - SSHFP record
* 4343 - Case insensitivity
* 4408 - SPF record
* 4509 - SHA256 Hash in DS
* 4592 - Wildcards in the DNS
* 4635 - HMAC SHA TSIG
* 4701 - DHCID
* 4892 - id.server
* 5001 - NSID
* 5155 - NSEC3 record
* 5205 - HIP record
* 5702 - SHA2 in the DNS
* 5936 - AXFR
* 5966 - TCP implementation recommendations
* 6605 - ECDSA
* 6725 - IANA Registry Update
* 6742 - ILNP DNS
* 6840 - Clarifications and Implementation Notes for DNS Security
* 6844 - CAA record
* 6891 - EDNS0 update
* 6895 - DNS IANA considerations
* 6975 - Algorithm Understanding in DNSSEC
* 7043 - EUI48/EUI64 records
* 7314 - DNS (EDNS) EXPIRE Option
* 7477 - CSYNC RR
* 7828 - edns-tcp-keepalive EDNS0 Option
* 7553 - URI record
* 7858 - DNS over TLS: Initiation and Performance Considerations
* 7871 - EDNS0 Client Subnet
* 7873 - Domain Name System (DNS) Cookies (draft-ietf-dnsop-cookies)
* 8080 - EdDSA for DNSSEC

## Loosely based upon

* `ldns`
* `NSD`
* `Net::DNS`
* `GRONG`
[![Sourcegraph](https://sourcegraph.com/github.com/ugorji/go/-/badge.svg?v=2)](https://sourcegraph.com/github.com/ugorji/go/-/tree/codec)
[![Build Status](https://travis-ci.org/ugorji/go.svg?branch=master)](https://travis-ci.org/ugorji/go)
[![codecov](https://codecov.io/gh/ugorji/go/branch/master/graph/badge.svg?v=2)](https://codecov.io/gh/ugorji/go)
[![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/ugorji/go/codec)
[![rcard](https://goreportcard.com/badge/github.com/ugorji/go/codec?v=2)](https://goreportcard.com/report/github.com/ugorji/go/codec)
[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](https://raw.githubusercontent.com/ugorji/go/master/LICENSE)

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

TODO:

  - [ ] 2018-03-12 - Release v1.1.1 containing 32-bit fixes

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

This package will carefully use 'unsafe' for performance reasons in specific places.
You can build without unsafe use by passing the safe or appengine tag
i.e. 'go install -tags=safe ...'. Note that unsafe is only supported for the last 3
go sdk versions e.g. current go release is go 1.9, so we support unsafe use only from
go 1.7+ . This is because supporting unsafe requires knowledge of implementation details.

Online documentation: http://godoc.org/github.com/ugorji/go/codec  
Detailed Usage/How-to Primer: http://ugorji.net/blog/go-codec-primer

The idiomatic Go support is as seen in other encoding packages in
the standard library (ie json, xml, gob, etc).

Rich Feature Set includes:

  - Simple but extremely powerful and feature-rich API
  - Support for go1.4 and above, while selectively using newer APIs for later releases
  - Excellent code coverage ( > 90% )
  - Very High Performance.
    Our extensive benchmarks show us outperforming Gob, Json, Bson, etc by 2-4X.
  - Careful selected use of 'unsafe' for targeted performance gains.
    100% mode exists where 'unsafe' is not used at all.
  - Lock-free (sans mutex) concurrency for scaling to 100's of cores
  - Coerce types where appropriate
    e.g. decode an int in the stream into a float, decode numbers from formatted strings, etc
  - Corner Cases: 
    Overflows, nil maps/slices, nil values in streams are handled correctly
  - Standard field renaming via tags
  - Support for omitting empty fields during an encoding
  - Encoding from any value and decoding into pointer to any value
    (struct, slice, map, primitives, pointers, interface{}, etc)
  - Extensions to support efficient encoding/decoding of any named types
  - Support encoding.(Binary|Text)(M|Unm)arshaler interfaces
  - Support IsZero() bool to determine if a value is a zero value.
    Analogous to time.Time.IsZero() bool.
  - Decoding without a schema (into a interface{}).
    Includes Options to configure what specific map or slice type to use
    when decoding an encoded list or map into a nil interface{}
  - Mapping a non-interface type to an interface, so we can decode appropriately
    into any interface type with a correctly configured non-interface value.
  - Encode a struct as an array, and decode struct from an array in the data stream
  - Option to encode struct keys as numbers (instead of strings)
    (to support structured streams with fields encoded as numeric codes)
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
  - Handle unique idiosyncrasies of codecs e.g. 
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

## Custom Encoding and Decoding

This package maintains symmetry in the encoding and decoding halfs.
We determine how to encode or decode by walking this decision tree

  - is type a codec.Selfer?
  - is there an extension registered for the type?
  - is format binary, and is type a encoding.BinaryMarshaler and BinaryUnmarshaler?
  - is format specifically json, and is type a encoding/json.Marshaler and Unmarshaler?
  - is format text-based, and type an encoding.TextMarshaler?
  - else we use a pair of functions based on the "kind" of the type e.g. map, slice, int64, etc

This symmetry is important to reduce chances of issues happening because the
encoding and decoding sides are out of sync e.g. decoded via very specific
encoding.TextUnmarshaler but encoded via kind-specific generalized mode.

Consequently, if a type only defines one-half of the symmetry
(e.g. it implements UnmarshalJSON() but not MarshalJSON() ),
then that type doesn't satisfy the check and we will continue walking down the
decision tree.

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

## Running Tests

To run tests, use the following:

    go test

To run the full suite of tests, use the following:

    go test -tags alltests -run Suite

You can run the tag 'safe' to run tests or build in safe mode. e.g.

    go test -tags safe -run Json
    go test -tags "alltests safe" -run Suite

## Running Benchmarks

Please see http://github.com/ugorji/go-codec-bench .

## Caveats

Struct fields matching the following are ignored during encoding and decoding

  - struct tag value set to -
  - func, complex numbers, unsafe pointers
  - unexported and not embedded
  - unexported and embedded and not struct kind
  - unexported and embedded pointers (from go1.10)

Every other field in a struct will be encoded/decoded.

Embedded fields are encoded as if they exist in the top-level struct,
with some caveats. See Encode documentation.
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

# fwd
    import "github.com/philhofer/fwd"

The `fwd` package provides a buffered reader
and writer. Each has methods that help improve
the encoding/decoding performance of some binary
protocols.

The `fwd.Writer` and `fwd.Reader` type provide similar
functionality to their counterparts in `bufio`, plus
a few extra utility methods that simplify read-ahead
and write-ahead. I wrote this package to improve serialization
performance for <a href="http://github.com/tinylib/msgp">http://github.com/tinylib/msgp</a>,
where it provided about a 2x speedup over `bufio` for certain
workloads. However, care must be taken to understand the semantics of the
extra methods provided by this package, as they allow
the user to access and manipulate the buffer memory
directly.

The extra methods for `fwd.Reader` are `Peek`, `Skip`
and `Next`. `(*fwd.Reader).Peek`, unlike `(*bufio.Reader).Peek`,
will re-allocate the read buffer in order to accommodate arbitrarily
large read-ahead. `(*fwd.Reader).Skip` skips the next `n` bytes
in the stream, and uses the `io.Seeker` interface if the underlying
stream implements it. `(*fwd.Reader).Next` returns a slice pointing
to the next `n` bytes in the read buffer (like `Peek`), but also
increments the read position. This allows users to process streams
in arbitrary block sizes without having to manage appropriately-sized
slices. Additionally, obviating the need to copy the data from the
buffer to another location in memory can improve performance dramatically
in CPU-bound applications.

`fwd.Writer` only has one extra method, which is `(*fwd.Writer).Next`, which
returns a slice pointing to the next `n` bytes of the writer, and increments
the write position by the length of the returned slice. This allows users
to write directly to the end of the buffer.




## Constants
``` go
const (
    // DefaultReaderSize is the default size of the read buffer
    DefaultReaderSize = 2048
)
```
``` go
const (
    // DefaultWriterSize is the
    // default write buffer size.
    DefaultWriterSize = 2048
)
```



## type Reader
``` go
type Reader struct {
    // contains filtered or unexported fields
}
```
Reader is a buffered look-ahead reader









### func NewReader
``` go
func NewReader(r io.Reader) *Reader
```
NewReader returns a new *Reader that reads from 'r'


### func NewReaderSize
``` go
func NewReaderSize(r io.Reader, n int) *Reader
```
NewReaderSize returns a new *Reader that
reads from 'r' and has a buffer size 'n'




### func (\*Reader) BufferSize
``` go
func (r *Reader) BufferSize() int
```
BufferSize returns the total size of the buffer



### func (\*Reader) Buffered
``` go
func (r *Reader) Buffered() int
```
Buffered returns the number of bytes currently in the buffer



### func (\*Reader) Next
``` go
func (r *Reader) Next(n int) ([]byte, error)
```
Next returns the next 'n' bytes in the stream.
Unlike Peek, Next advances the reader position.
The returned bytes point to the same
data as the buffer, so the slice is
only valid until the next reader method call.
An EOF is considered an unexpected error.
If an the returned slice is less than the
length asked for, an error will be returned,
and the reader position will not be incremented.



### func (\*Reader) Peek
``` go
func (r *Reader) Peek(n int) ([]byte, error)
```
Peek returns the next 'n' buffered bytes,
reading from the underlying reader if necessary.
It will only return a slice shorter than 'n' bytes
if it also returns an error. Peek does not advance
the reader. EOF errors are *not* returned as
io.ErrUnexpectedEOF.



### func (\*Reader) Read
``` go
func (r *Reader) Read(b []byte) (int, error)
```
Read implements `io.Reader`



### func (\*Reader) ReadByte
``` go
func (r *Reader) ReadByte() (byte, error)
```
ReadByte implements `io.ByteReader`



### func (\*Reader) ReadFull
``` go
func (r *Reader) ReadFull(b []byte) (int, error)
```
ReadFull attempts to read len(b) bytes into
'b'. It returns the number of bytes read into
'b', and an error if it does not return len(b).
EOF is considered an unexpected error.



### func (\*Reader) Reset
``` go
func (r *Reader) Reset(rd io.Reader)
```
Reset resets the underlying reader
and the read buffer.



### func (\*Reader) Skip
``` go
func (r *Reader) Skip(n int) (int, error)
```
Skip moves the reader forward 'n' bytes.
Returns the number of bytes skipped and any
errors encountered. It is analogous to Seek(n, 1).
If the underlying reader implements io.Seeker, then
that method will be used to skip forward.

If the reader encounters
an EOF before skipping 'n' bytes, it
returns io.ErrUnexpectedEOF. If the
underlying reader implements io.Seeker, then
those rules apply instead. (Many implementations
will not return `io.EOF` until the next call
to Read.)



### func (\*Reader) WriteTo
``` go
func (r *Reader) WriteTo(w io.Writer) (int64, error)
```
WriteTo implements `io.WriterTo`



## type Writer
``` go
type Writer struct {
    // contains filtered or unexported fields
}
```
Writer is a buffered writer









### func NewWriter
``` go
func NewWriter(w io.Writer) *Writer
```
NewWriter returns a new writer
that writes to 'w' and has a buffer
that is `DefaultWriterSize` bytes.


### func NewWriterSize
``` go
func NewWriterSize(w io.Writer, size int) *Writer
```
NewWriterSize returns a new writer
that writes to 'w' and has a buffer
that is 'size' bytes.




### func (\*Writer) BufferSize
``` go
func (w *Writer) BufferSize() int
```
BufferSize returns the maximum size of the buffer.



### func (\*Writer) Buffered
``` go
func (w *Writer) Buffered() int
```
Buffered returns the number of buffered bytes
in the reader.



### func (\*Writer) Flush
``` go
func (w *Writer) Flush() error
```
Flush flushes any buffered bytes
to the underlying writer.



### func (\*Writer) Next
``` go
func (w *Writer) Next(n int) ([]byte, error)
```
Next returns the next 'n' free bytes
in the write buffer, flushing the writer
as necessary. Next will return `io.ErrShortBuffer`
if 'n' is greater than the size of the write buffer.
Calls to 'next' increment the write position by
the size of the returned buffer.



### func (\*Writer) ReadFrom
``` go
func (w *Writer) ReadFrom(r io.Reader) (int64, error)
```
ReadFrom implements `io.ReaderFrom`



### func (\*Writer) Write
``` go
func (w *Writer) Write(p []byte) (int, error)
```
Write implements `io.Writer`



### func (\*Writer) WriteByte
``` go
func (w *Writer) WriteByte(b byte) error
```
WriteByte implements `io.ByteWriter`



### func (\*Writer) WriteString
``` go
func (w *Writer) WriteString(s string) (int, error)
```
WriteString is analogous to Write, but it takes a string.









- - -
Generated by [godoc2md](http://godoc.org/github.com/davecheney/godoc2md)a collection of go utility packages

[![Build Status](https://travis-ci.org/coreos/pkg.png?branch=master)](https://travis-ci.org/coreos/pkg)
[![Godoc](http://img.shields.io/badge/godoc-reference-blue.svg?style=flat)](https://godoc.org/github.com/coreos/pkg)
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

# go-systemd

[![Build Status](https://travis-ci.org/coreos/go-systemd.png?branch=master)](https://travis-ci.org/coreos/go-systemd)
[![godoc](https://godoc.org/github.com/coreos/go-systemd?status.svg)](http://godoc.org/github.com/coreos/go-systemd)

Go bindings to systemd. The project has several packages:

- `activation` - for writing and using socket activation from Go
- `daemon` - for notifying systemd of service status changes
- `dbus` - for starting/stopping/inspecting running services and units
- `journal` - for writing to systemd's logging service, journald
- `sdjournal` - for reading from journald by wrapping its C API
- `login1` - for integration with the systemd logind API
- `machine1` - for registering machines/containers with systemd
- `unit` - for (de)serialization and comparison of unit files

## Socket Activation

An example HTTP server using socket activation can be quickly set up by following this README on a Linux machine running systemd:

https://github.com/coreos/go-systemd/tree/master/examples/activation/httpserver

## systemd Service Notification

The `daemon` package is an implementation of the [sd_notify protocol](https://www.freedesktop.org/software/systemd/man/sd_notify.html#Description). It can be used to inform systemd of service start-up completion, watchdog events, and other status changes.

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

## Journal

### Writing to the Journal

Using the pure-Go `journal` package you can submit journal entries directly to systemd's journal, taking advantage of features like indexed key/value pairs for each log entry.

### Reading from the Journal

The `sdjournal` package provides read access to the journal by wrapping around journald's native C API; consequently it requires cgo and the journal headers to be available.

## logind

The `login1` package provides functions to integrate with the [systemd logind API](http://www.freedesktop.org/wiki/Software/systemd/logind/).

## machined

The `machine1` package allows interaction with the [systemd machined D-Bus API](http://www.freedesktop.org/wiki/Software/systemd/machined/).

## Units

The `unit` package provides various functions for working with [systemd unit files](http://www.freedesktop.org/software/systemd/man/systemd.unit.html).
# go-semver - Semantic Versioning Library

[![Build Status](https://travis-ci.org/coreos/go-semver.svg?branch=master)](https://travis-ci.org/coreos/go-semver)
[![GoDoc](https://godoc.org/github.com/coreos/go-semver/semver?status.svg)](https://godoc.org/github.com/coreos/go-semver/semver)

go-semver is a [semantic versioning][semver] library for Go. It lets you parse
and compare two semantic version strings.

[semver]: http://semver.org/

## Usage

```go
vA := semver.New("1.2.3")
vB := semver.New("3.2.1")

fmt.Printf("%s < %s == %t\n", vA, vB, vA.LessThan(*vB))
```

## Example Application

```
$ go run example.go 1.2.3 3.2.1
1.2.3 < 3.2.1 == true

$ go run example.go 5.2.3 3.2.1
5.2.3 < 3.2.1 == false
```
# etcd

[![Go Report Card](https://goreportcard.com/badge/github.com/coreos/etcd?style=flat-square)](https://goreportcard.com/report/github.com/coreos/etcd)
[![Coverage](https://codecov.io/gh/coreos/etcd/branch/master/graph/badge.svg)](https://codecov.io/gh/coreos/etcd)
[![Build Status Travis](https://img.shields.io/travis/coreos/etcdlabs.svg?style=flat-square&&branch=master)](https://travis-ci.org/coreos/etcd)
[![Build Status Semaphore](https://semaphoreci.com/api/v1/coreos/etcd/branches/master/shields_badge.svg)](https://semaphoreci.com/coreos/etcd)
[![Godoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](https://godoc.org/github.com/coreos/etcd)
[![Releases](https://img.shields.io/github/release/coreos/etcd/all.svg?style=flat-square)](https://github.com/coreos/etcd/releases)
[![LICENSE](https://img.shields.io/github/license/coreos/etcd.svg?style=flat-square)](https://github.com/coreos/etcd/blob/master/LICENSE)

**Note**: The `master` branch may be in an *unstable or even broken state* during development. Please use [releases][github-release] instead of the `master` branch in order to get stable binaries.

*the etcd v2 [documentation](Documentation/v2/README.md) has moved*

![etcd Logo](logos/etcd-horizontal-color.png)

etcd is a distributed reliable key-value store for the most critical data of a distributed system, with a focus on being:

* *Simple*: well-defined, user-facing API (gRPC)
* *Secure*: automatic TLS with optional client cert authentication
* *Fast*: benchmarked 10,000 writes/sec
* *Reliable*: properly distributed using Raft

etcd is written in Go and uses the [Raft][raft] consensus algorithm to manage a highly-available replicated log.

etcd is used [in production by many companies](./Documentation/production-users.md), and the development team stands behind it in critical deployment scenarios, where etcd is frequently teamed with applications such as [Kubernetes][k8s], [fleet][fleet], [locksmith][locksmith], [vulcand][vulcand], [Doorman][doorman], and many others. Reliability is further ensured by rigorous [testing][etcd-tests].

See [etcdctl][etcdctl] for a simple command line client.

[raft]: https://raft.github.io/
[k8s]: http://kubernetes.io/
[doorman]: https://github.com/youtube/doorman
[fleet]: https://github.com/coreos/fleet
[locksmith]: https://github.com/coreos/locksmith
[vulcand]: https://github.com/vulcand/vulcand
[etcdctl]: https://github.com/coreos/etcd/tree/master/etcdctl
[etcd-tests]: http://dash.etcd.io

## Community meetings

etcd contributors and maintainers have bi-weekly meetings at 11:00 AM (USA Pacific) on Tuesdays. There is an [iCalendar][rfc5545] format for the meetings [here](meeting.ics). Anyone is welcome to join via [Zoom][zoom] or audio-only: +1 669 900 6833. An initial agenda will be posted to the [shared Google docs][shared-meeting-notes] a day before each meeting, and everyone is welcome to suggest additional topics or other agendas.

[rfc5545]: https://tools.ietf.org/html/rfc5545
[zoom]: https://coreos.zoom.us/j/854793406
[shared-meeting-notes]: https://docs.google.com/document/d/1DbVXOHvd9scFsSmL2oNg4YGOHJdXqtx583DmeVWrB_M/edit#

## Getting started

### Getting etcd

The easiest way to get etcd is to use one of the pre-built release binaries which are available for OSX, Linux, Windows, [rkt][rkt], and Docker. Instructions for using these binaries are on the [GitHub releases page][github-release].

For those wanting to try the very latest version, [build the latest version of etcd][dl-build] from the `master` branch. This first needs [*Go*](https://golang.org/) installed (version 1.9+ is required). All development occurs on `master`, including new features and bug fixes. Bug fixes are first targeted at `master` and subsequently ported to release branches, as described in the [branch management][branch-management] guide.

[rkt]: https://github.com/rkt/rkt/releases/
[github-release]: https://github.com/coreos/etcd/releases/
[branch-management]: ./Documentation/branch_management.md
[dl-build]: ./Documentation/dl_build.md#build-the-latest-version

### Running etcd

First start a single-member cluster of etcd.

If etcd is installed using the [pre-built release binaries][github-release], run it from the installation location as below:

```sh
/tmp/etcd-download-test/etcd
```
The etcd command can be simply run as such if it is moved to the system path as below:

```sh
mv /tmp/etcd-download-test/etcd /usr/locale/bin/

etcd
```

If etcd is [build from the master branch][dl-build], run it as below:

```sh
./bin/etcd
```

This will bring up etcd listening on port 2379 for client communication and on port 2380 for server-to-server communication.

Next, let's set a single key, and then retrieve it:

```
ETCDCTL_API=3 etcdctl put mykey "this is awesome"
ETCDCTL_API=3 etcdctl get mykey
```

That's it! etcd is now running and serving client requests. For more

- [Animated quick demo][demo-gif]
- [Interactive etcd playground][etcd-play]

[demo-gif]: ./Documentation/demo.md
[etcd-play]: http://play.etcd.io/

### etcd TCP ports

The [official etcd ports][iana-ports] are 2379 for client requests, and 2380 for peer communication.

[iana-ports]: http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt

### Running a local etcd cluster

First install [goreman](https://github.com/mattn/goreman), which manages Procfile-based applications.

Our [Procfile script](./Procfile) will set up a local example cluster. Start it with:

```sh
goreman start
```

This will bring up 3 etcd members `infra1`, `infra2` and `infra3` and etcd `grpc-proxy`, which runs locally and composes a cluster.

Every cluster member and proxy accepts key value reads and key value writes.

### Running etcd on Kubernetes

To run an etcd cluster on Kubernetes, try [etcd operator](https://github.com/coreos/etcd-operator).

### Next steps

Now it's time to dig into the full etcd API and other guides.

- Read the full [documentation][fulldoc].
- Explore the full gRPC [API][api].
- Set up a [multi-machine cluster][clustering].
- Learn the [config format, env variables and flags][configuration].
- Find [language bindings and tools][integrations].
- Use TLS to [secure an etcd cluster][security].
- [Tune etcd][tuning].

[fulldoc]: ./Documentation/docs.md
[api]: ./Documentation/dev-guide/api_reference_v3.md
[clustering]: ./Documentation/op-guide/clustering.md
[configuration]: ./Documentation/op-guide/configuration.md
[integrations]: ./Documentation/integrations.md
[security]: ./Documentation/op-guide/security.md
[tuning]: ./Documentation/tuning.md

## Contact

- Mailing list: [etcd-dev](https://groups.google.com/forum/?hl=en#!forum/etcd-dev)
- IRC: #[etcd](irc://irc.freenode.org:6667/#etcd) on freenode.org
- Planning/Roadmap: [milestones](https://github.com/coreos/etcd/milestones), [roadmap](./ROADMAP.md)
- Bugs: [issues](https://github.com/coreos/etcd/issues)

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for details on submitting patches and the contribution workflow.

## Reporting bugs

See [reporting bugs](Documentation/reporting_bugs.md) for details about reporting any issues.

### License

etcd is under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.
pkg/ is a collection of utility packages used by etcd without being specific to etcd itself. A package belongs here
only if it could possibly be moved out into its own repository in the future.
# Raft library

Raft is a protocol with which a cluster of nodes can maintain a replicated state machine.
The state machine is kept in sync through the use of a replicated log.
For more details on Raft, see "In Search of an Understandable Consensus Algorithm"
(https://ramcloud.stanford.edu/raft.pdf) by Diego Ongaro and John Ousterhout.

This Raft library is stable and feature complete. As of 2016, it is **the most widely used** Raft library in production, serving tens of thousands clusters each day. It powers distributed systems such as etcd, Kubernetes, Docker Swarm, Cloud Foundry Diego, CockroachDB, TiDB, Project Calico, Flannel, and more.

Most Raft implementations have a monolithic design, including storage handling, messaging serialization, and network transport. This library instead follows a minimalistic design philosophy by only implementing the core raft algorithm. This minimalism buys flexibility, determinism, and performance.

To keep the codebase small as well as provide flexibility, the library only implements the Raft algorithm; both network and disk IO are left to the user. Library users must implement their own transportation layer for message passing between Raft peers over the wire. Similarly, users must implement their own storage layer to persist the Raft log and state.

In order to easily test the Raft library, its behavior should be deterministic. To achieve this determinism, the library models Raft as a state machine.  The state machine takes a `Message` as input. A message can either be a local timer update or a network message sent from a remote peer. The state machine's output is a 3-tuple `{[]Messages, []LogEntries, NextState}` consisting of an array of `Messages`, `log entries`, and `Raft state changes`. For state machines with the same state, the same state machine input should always generate the same state machine output.

A simple example application, _raftexample_, is also available to help illustrate how to use this package in practice: https://github.com/coreos/etcd/tree/master/contrib/raftexample

# Features

This raft implementation is a full feature implementation of Raft protocol. Features includes:

- Leader election
- Log replication
- Log compaction 
- Membership changes
- Leadership transfer extension
- Efficient linearizable read-only queries served by both the leader and followers
  - leader checks with quorum and bypasses Raft log before processing read-only queries
  - followers asks leader to get a safe read index before processing read-only queries
- More efficient lease-based linearizable read-only queries served by both the leader and followers
  - leader bypasses Raft log and processing read-only queries locally
  - followers asks leader to get a safe read index before processing read-only queries
  - this approach relies on the clock of the all the machines in raft group

This raft implementation also includes a few optional enhancements:

- Optimistic pipelining to reduce log replication latency
- Flow control for log replication
- Batching Raft messages to reduce synchronized network I/O calls
- Batching log entries to reduce disk synchronized I/O
- Writing to leader's disk in parallel
- Internal proposal redirection from followers to leader
- Automatic stepping down when the leader loses quorum 

## Notable Users

- [cockroachdb](https://github.com/cockroachdb/cockroach) A Scalable, Survivable, Strongly-Consistent SQL Database
- [dgraph](https://github.com/dgraph-io/dgraph) A Scalable, Distributed, Low Latency, High Throughput Graph Database
- [etcd](https://github.com/coreos/etcd) A distributed reliable key-value store
- [tikv](https://github.com/pingcap/tikv) A Distributed transactional key value database powered by Rust and Raft
- [swarmkit](https://github.com/docker/swarmkit) A toolkit for orchestrating distributed systems at any scale.
- [chain core](https://github.com/chain/chain) Software for operating permissioned, multi-asset blockchain networks

## Usage

The primary object in raft is a Node. Either start a Node from scratch using raft.StartNode or start a Node from some initial state using raft.RestartNode.

To start a three-node cluster
```go
  storage := raft.NewMemoryStorage()
  c := &Config{
    ID:              0x01,
    ElectionTick:    10,
    HeartbeatTick:   1,
    Storage:         storage,
    MaxSizePerMsg:   4096,
    MaxInflightMsgs: 256,
  }
  // Set peer list to the other nodes in the cluster.
  // Note that they need to be started separately as well.
  n := raft.StartNode(c, []raft.Peer{{ID: 0x02}, {ID: 0x03}})
```

Start a single node cluster, like so:
```go
  // Create storage and config as shown above.
  // Set peer list to itself, so this node can become the leader of this single-node cluster.
  peers := []raft.Peer{{ID: 0x01}}
  n := raft.StartNode(c, peers)
```

To allow a new node to join this cluster, do not pass in any peers. First, add the node to the existing cluster by calling `ProposeConfChange` on any existing node inside the cluster. Then, start the node with an empty peer list, like so:
```go
  // Create storage and config as shown above.
  n := raft.StartNode(c, nil)
```

To restart a node from previous state:
```go
  storage := raft.NewMemoryStorage()

  // Recover the in-memory storage from persistent snapshot, state and entries.
  storage.ApplySnapshot(snapshot)
  storage.SetHardState(state)
  storage.Append(entries)

  c := &Config{
    ID:              0x01,
    ElectionTick:    10,
    HeartbeatTick:   1,
    Storage:         storage,
    MaxSizePerMsg:   4096,
    MaxInflightMsgs: 256,
  }

  // Restart raft without peer information.
  // Peer information is already included in the storage.
  n := raft.RestartNode(c)
```

After creating a Node, the user has a few responsibilities:

First, read from the Node.Ready() channel and process the updates it contains. These steps may be performed in parallel, except as noted in step 2.

1. Write Entries, HardState and Snapshot to persistent storage in order, i.e. Entries first, then HardState and Snapshot if they are not empty. If persistent storage supports atomic writes then all of them can be written together. Note that when writing an Entry with Index i, any previously-persisted entries with Index >= i must be discarded.

2. Send all Messages to the nodes named in the To field. It is important that no messages be sent until the latest HardState has been persisted to disk, and all Entries written by any previous Ready batch (Messages may be sent while entries from the same batch are being persisted). To reduce the I/O latency, an optimization can be applied to make leader write to disk in parallel with its followers (as explained at section 10.2.1 in Raft thesis). If any Message has type MsgSnap, call Node.ReportSnapshot() after it has been sent (these messages may be large). Note: Marshalling messages is not thread-safe; it is important to make sure that no new entries are persisted while marshalling. The easiest way to achieve this is to serialise the messages directly inside the main raft loop.

3. Apply Snapshot (if any) and CommittedEntries to the state machine. If any committed Entry has Type EntryConfChange, call Node.ApplyConfChange() to apply it to the node. The configuration change may be cancelled at this point by setting the NodeID field to zero before calling ApplyConfChange (but ApplyConfChange must be called one way or the other, and the decision to cancel must be based solely on the state machine and not external information such as the observed health of the node).

4. Call Node.Advance() to signal readiness for the next batch of updates. This may be done at any time after step 1, although all updates must be processed in the order they were returned by Ready.

Second, all persisted log entries must be made available via an implementation of the Storage interface. The provided MemoryStorage type can be used for this (if repopulating its state upon a restart), or a custom disk-backed implementation can be supplied.

Third, after receiving a message from another node, pass it to Node.Step:

```go
	func recvRaftRPC(ctx context.Context, m raftpb.Message) {
		n.Step(ctx, m)
	}
```

Finally, call `Node.Tick()` at regular intervals (probably via a `time.Ticker`). Raft has two important timeouts: heartbeat and the election timeout. However, internally to the raft package time is represented by an abstract "tick".

The total state machine handling loop will look something like this:

```go
  for {
    select {
    case <-s.Ticker:
      n.Tick()
    case rd := <-s.Node.Ready():
      saveToStorage(rd.State, rd.Entries, rd.Snapshot)
      send(rd.Messages)
      if !raft.IsEmptySnap(rd.Snapshot) {
        processSnapshot(rd.Snapshot)
      }
      for _, entry := range rd.CommittedEntries {
        process(entry)
        if entry.Type == raftpb.EntryConfChange {
          var cc raftpb.ConfChange
          cc.Unmarshal(entry.Data)
          s.Node.ApplyConfChange(cc)
        }
      }
      s.Node.Advance()
    case <-s.done:
      return
    }
  }
```

To propose changes to the state machine from the node to take application data, serialize it into a byte slice and call:

```go
	n.Propose(ctx, data)
```

If the proposal is committed, data will appear in committed entries with type raftpb.EntryNormal. There is no guarantee that a proposed command will be committed; the command may have to be reproposed after a timeout. 

To add or remove node in a cluster, build ConfChange struct 'cc' and call:

```go
	n.ProposeConfChange(ctx, cc)
```

After config change is committed, some committed entry with type raftpb.EntryConfChange will be returned. This must be applied to node through:

```go
	var cc raftpb.ConfChange
	cc.Unmarshal(data)
	n.ApplyConfChange(cc)
```

Note: An ID represents a unique node in a cluster for all time. A
given ID MUST be used only once even if the old node has been removed.
This means that for example IP addresses make poor node IDs since they
may be reused. Node IDs must be non-zero.

## Implementation notes

This implementation is up to date with the final Raft thesis (https://ramcloud.stanford.edu/~ongaro/thesis.pdf), although this implementation of the membership change protocol differs somewhat from that described in chapter 4. The key invariant that membership changes happen one node at a time is preserved, but in our implementation the membership change takes effect when its entry is applied, not when it is added to the log (so the entry is committed under the old membership instead of the new). This is equivalent in terms of safety, since the old and new configurations are guaranteed to overlap.

To ensure there is no attempt to commit two membership changes at once by matching log positions (which would be unsafe since they should have different quorum requirements), any proposed membership change is simply disallowed while any uncommitted change appears in the leader's log.

This approach introduces a problem when removing a member from a two-member cluster: If one of the members dies before the other one receives the commit of the confchange entry, then the member cannot be removed any more since the cluster cannot make progress. For this reason it is highly recommended to use three or more nodes in every cluster.
# etcd/client

etcd/client is the Go client library for etcd.

[![GoDoc](https://godoc.org/github.com/coreos/etcd/client?status.png)](https://godoc.org/github.com/coreos/etcd/client)

etcd uses `cmd/vendor` directory to store external dependencies, which are
to be compiled into etcd release binaries. `client` can be imported without
vendoring. For full compatibility, it is recommended to vendor builds using
etcd's vendored packages, using tools like godep, as in
[vendor directories](https://golang.org/cmd/go/#hdr-Vendor_Directories).
For more detail, please read [Go vendor design](https://golang.org/s/go15vendor).

## Install

```bash
go get github.com/coreos/etcd/client
```

## Usage

```go
package main

import (
	"log"
	"time"
	"context"

	"github.com/coreos/etcd/client"
)

func main() {
	cfg := client.Config{
		Endpoints:               []string{"http://127.0.0.1:2379"},
		Transport:               client.DefaultTransport,
		// set timeout per request to fail fast when the target endpoint is unavailable
		HeaderTimeoutPerRequest: time.Second,
	}
	c, err := client.New(cfg)
	if err != nil {
		log.Fatal(err)
	}
	kapi := client.NewKeysAPI(c)
	// set "/foo" key with "bar" value
	log.Print("Setting '/foo' key with 'bar' value")
	resp, err := kapi.Set(context.Background(), "/foo", "bar", nil)
	if err != nil {
		log.Fatal(err)
	} else {
		// print common key info
		log.Printf("Set is done. Metadata is %q\n", resp)
	}
	// get "/foo" key's value
	log.Print("Getting '/foo' key value")
	resp, err = kapi.Get(context.Background(), "/foo", nil)
	if err != nil {
		log.Fatal(err)
	} else {
		// print common key info
		log.Printf("Get is done. Metadata is %q\n", resp)
		// print value
		log.Printf("%q key has %q value\n", resp.Node.Key, resp.Node.Value)
	}
}
```

## Error Handling

etcd client might return three types of errors.

- context error

Each API call has its first parameter as `context`. A context can be canceled or have an attached deadline. If the context is canceled or reaches its deadline, the responding context error will be returned no matter what internal errors the API call has already encountered.

- cluster error

Each API call tries to send request to the cluster endpoints one by one until it successfully gets a response. If a requests to an endpoint fails, due to exceeding per request timeout or connection issues, the error will be added into a list of errors. If all possible endpoints fail, a cluster error that includes all encountered errors will be returned.

- response error

If the response gets from the cluster is invalid, a plain string error will be returned. For example, it might be a invalid JSON error.

Here is the example code to handle client errors:

```go
cfg := client.Config{Endpoints: []string{"http://etcd1:2379","http://etcd2:2379","http://etcd3:2379"}}
c, err := client.New(cfg)
if err != nil {
	log.Fatal(err)
}

kapi := client.NewKeysAPI(c)
resp, err := kapi.Set(ctx, "test", "bar", nil)
if err != nil {
	if err == context.Canceled {
		// ctx is canceled by another routine
	} else if err == context.DeadlineExceeded {
		// ctx is attached with a deadline and it exceeded
	} else if cerr, ok := err.(*client.ClusterError); ok {
		// process (cerr.Errors)
	} else {
		// bad cluster endpoints, which are not etcd servers
	}
}
```


## Caveat

1. etcd/client prefers to use the same endpoint as long as the endpoint continues to work well. This saves socket resources, and improves efficiency for both client and server side. This preference doesn't remove consistency from the data consumed by the client because data replicated to each etcd member has already passed through the consensus process.

2. etcd/client does round-robin rotation on other available endpoints if the preferred endpoint isn't functioning properly. For example, if the member that etcd/client connects to is hard killed, etcd/client will fail on the first attempt with the killed member, and succeed on the second attempt with another member. If it fails to talk to all available endpoints, it will return all errors happened.

3. Default etcd/client cannot handle the case that the remote server is SIGSTOPed now. TCP keepalive mechanism doesn't help in this scenario because operating system may still send TCP keep-alive packets. Over time we'd like to improve this functionality, but solving this issue isn't high priority because a real-life case in which a server is stopped, but the connection is kept alive, hasn't been brought to our attention.

4. etcd/client cannot detect whether a member is healthy with watches and non-quorum read requests. If the member is isolated from the cluster, etcd/client may retrieve outdated data. Instead, users can either issue quorum read requests or monitor the /health endpoint for member health information.
# go-ansiterm

This is a cross platform Ansi Terminal Emulation library.  It reads a stream of Ansi characters and produces the appropriate function calls.  The results of the function calls are platform dependent.

For example the parser might receive "ESC, [, A" as a stream of three characters.  This is the code for Cursor Up (http://www.vt100.net/docs/vt510-rm/CUU).  The parser then calls the cursor up function (CUU()) on an event handler.  The event handler determines what platform specific work must be done to cause the cursor to move up one position.

The parser (parser.go) is a partial implementation of this state machine (http://vt100.net/emu/vt500_parser.png).  There are also two event handler implementations, one for tests (test_event_handler.go) to validate that the expected events are being produced and called, the other is a Windows implementation (winterm/win_event_handler.go).

See parser_test.go for examples exercising the state machine and generating appropriate function calls.

-----
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
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
This project is the source for http://godoc.org/

[![GoDoc](https://godoc.org/github.com/golang/gddo?status.svg)](http://godoc.org/github.com/golang/gddo)
[![Build
Status](https://travis-ci.org/golang/gddo.svg?branch=master)](https://travis-ci.org/golang/gddo)

The code in this project is designed to be used by godoc.org. Send mail to
golang-dev@googlegroups.com if you want to discuss other uses of the code.

## Feedback

Send ideas and questions to golang-dev@googlegroups.com. Request features and
report bugs using the [GitHub Issue
Tracker](https://github.com/golang/gddo/issues/new).

## Contributions

Contributions to this project are welcome, though please [file an
issue](https://github.com/golang/gddo/issues/new). before starting work on
anything major.

**We do not accept GitHub pull requests**

Please refer to the [Contribution
Guidelines](https://golang.org/doc/contribute.html) on how to submit changes.

We use https://go-review.googlesource.com to review change submissions.

## Getting the Source

To get started contributing to this project, clone the repository from its
canonical location

```
git clone https://go.googlesource.com/gddo $GOPATH/src/github.com/golang/gddo
```

Information on how to set up a local environment is available at
https://github.com/golang/gddo/wiki/Development-Environment-Setup.

## More Documentation

More documentation about this project is available on the
[wiki](https://github.com/golang/gddo/wiki).
# Go support for Protocol Buffers

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

	protoc --go_out=. inputs/x.proto
	# writes ./github.com/golang/protobuf/p/x.pb.go

  (This can work well with `--go_out=$GOPATH`.)

- Relative to the input file:

	protoc --go_out=paths=source_relative:. inputs/x.proto
	# generate ./inputs/x.pb.go

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
# Certificate Transparency: Go Code

[![Build Status](https://travis-ci.org/google/certificate-transparency-go.svg?branch=master)](https://travis-ci.org/google/certificate-transparency-go)
[![Go Report Card](https://goreportcard.com/badge/github.com/google/certificate-transparency-go)](https://goreportcard.com/report/github.com/google/certificate-transparency-go)
[![GoDoc](https://godoc.org/github.com/google/certificate-transparency-go?status.svg)](https://godoc.org/github.com/google/certificate-transparency-go)

This repository holds Go code related to
[Certificate Transparency](https://www.certificate-transparency.org/) (CT).  The
repository requires Go version 1.9.

 - [Repository Structure](#repository-structure)
 - [Trillian CT Personality](#trillian-ct-personality)
 - [Working on the Code](#working-on-the-code)
     - [Rebuilding Generated Code](#rebuilding-generated-code)
     - [Updating Vendor Code](#updating-vendor-code)
     - [Running Codebase Checks](#running-codebase-checks)

## Repository Structure

The main parts of the repository are:

 - Encoding libraries:
   - `asn1/` and `x509/` are forks of the upstream Go `encoding/asn1` and
     `crypto/x509` libraries.  We maintain separate forks of these packages
     because CT is intended to act as an observatory of certificates across the
     ecosystem; as such, we need to be able to process somewhat-malformed
     certificates that the stricter upstream code would (correctly) reject.
     Our `x509` fork also includes code for working with the
     [pre-certificates defined in RFC 6962](https://tools.ietf.org/html/rfc6962#section-3.1).
   - `tls` holds a library for processing TLS-encoded data as described in
     [RFC 5246](https://tools.ietf.org/html/rfc5246).
   - `x509util` provides additional utilities for dealing with
     `x509.Certificate`s.
 - CT client libraries:
   - The top-level `ct` package (in `.`) holds types and utilities for working
     with CT data structures defined in
     [RFC 6962](https://tools.ietf.org/html/rfc6962).
   - `client/` and `jsonclient/` hold libraries that allow access to CT Logs
     via entrypoints described in
     [section 4 of RFC 6962](https://tools.ietf.org/html/rfc6962#section-4).
   - `scanner/` holds a library for scanning the entire contents of an existing
     CT Log.
 - Command line tools:
   - `./client/ctclient` allows interaction with a CT Log
   - `./scanner/scanlog` allows an existing CT Log to be scanned for certificates
      of interest; please be polite when running this tool against a Log.
   - `./x509util/certcheck` allows display and verification of certificates
   - `./x509util/crlcheck` allows display and verification of certificate
     revocation lists (CRLs).
 - CT Personality for [Trillian](https://github.com/google/trillian):
    - `trillian/` holds code that allows a Certificate Transparency Log to be
      run using a Trillian Log as its back-end -- see
      [below](#trillian-ct-personality).


## Trillian CT Personality

The `trillian/` subdirectory holds code and scripts for running a CT Log based
on the [Trillian](https://github.com/google/trillian) general transparency Log.

The main code for the CT personality is held in `trillian/ctfe`; this code
responds to HTTP requests on the
[CT API paths](https://tools.ietf.org/html/rfc6962#section-4) and translates
them to the equivalent gRPC API requests to the Trillian Log.

This obviously relies on the gRPC API definitions at
`github.com/google/trillian`; the code also uses common libraries from the
Trillian project for:
 - exposing monitoring and statistics via an `interface` and corresponding
   Prometheus implementation (`github.com/google/trillian/monitoring/...`)
 - dealing with cryptographic keys (`github.com/google/trillian/crypto/...`).

The `trillian/integration/` directory holds scripts and tests for running the whole
system locally.  In particular:
 - `trillian/integration/ct_integration_test.sh` brings up local processes
   running a Trillian Log server, signer and a CT personality, and exercises the
   complete set of RFC 6962 API entrypoints.
 - `trillian/integration/ct_hammer_test.sh` brings up a complete system and runs
   a continuous randomized test of the CT entrypoints.

These scripts require a local database instance to be configured as described
in the [Trillian instructions](https://github.com/google/trillian#mysql-setup).


## Working on the Code

Developers who want to make changes to the codebase need some additional
dependencies and tools, described in the following sections.  The
[Travis configuration](.travis.yml) for the codebase is also useful reference
for the required tools and scripts, as it may be more up-to-date than this
document.

### Rebuilding Generated Code

Some of the CT Go code is autogenerated from other files:

 - [Protocol buffer](https://developers.google.com/protocol-buffers/) message
   definitions are converted to `.pb.go` implementations.
 - A mock implementation of the Trillian gRPC API (in `trillian/mockclient`) is
   created with [GoMock](https://github.com/golang/mock).

Re-generating mock or protobuffer files is only needed if you're changing
the original files; if you do, you'll need to install the prerequisites:

  - `mockgen` tool from https://github.com/golang/mock
  - `protoc`, [Go support for protoc](https://github.com/golang/protobuf) (see
     documentation linked from the
     [protobuf site](https://github.com/google/protobuf))

and run the following:

```bash
go generate -x ./...  # hunts for //go:generate comments and runs them
```

### Updating Vendor Code

The codebase includes a couple of external projects under the `vendor/`
subdirectory, to ensure that builds use a fixed version (typically because the
upstream repository does not guarantee back-compatibility between the tip
`master` branch and the current stable release).  See
[instructions in the Trillian repo](https://github.com/google/trillian#updating-vendor-code)
for how to update vendored subtrees.


### Running Codebase Checks

The [`scripts/presubmit.sh`](scripts/presubmit.sh) script runs various tools
and tests over the codebase.

```bash
# Install gometalinter and all linters
go get -u github.com/alecthomas/gometalinter
gometalinter --install

# Run code generation, build, test and linters
./scripts/presubmit.sh

# Run build, test and linters but skip code generation
./scripts/presubmit.sh  --no-generate

# Or just run the linters alone:
gometalinter --config=gometalinter.json ./...
```
go-shlex is a simple lexer for go that supports shell-style quoting,
commenting, and escaping.
# Package for equality of Go values

[![GoDoc](https://godoc.org/github.com/google/go-cmp/cmp?status.svg)][godoc]
[![Build Status](https://travis-ci.org/google/go-cmp.svg?branch=master)][travis]

This package is intended to be a more powerful and safer alternative to
`reflect.DeepEqual` for comparing whether two values are semantically equal.

The primary features of `cmp` are:

* When the default behavior of equality does not suit the needs of the test,
  custom equality functions can override the equality operation.
  For example, an equality function may report floats as equal so long as they
  are within some tolerance of each other.

* Types that have an `Equal` method may use that method to determine equality.
  This allows package authors to determine the equality operation for the types
  that they define.

* If no custom equality functions are used and no `Equal` method is defined,
  equality is determined by recursively comparing the primitive kinds on both
  values, much like `reflect.DeepEqual`. Unlike `reflect.DeepEqual`, unexported
  fields are not compared by default; they result in panics unless suppressed
  by using an `Ignore` option (see `cmpopts.IgnoreUnexported`) or explicitly
  compared using the `AllowUnexported` option.

See the [GoDoc documentation][godoc] for more information.

This is not an official Google product.

[godoc]: https://godoc.org/github.com/google/go-cmp/cmp
[travis]: https://travis-ci.org/google/go-cmp

## Install

```
go get -u github.com/google/go-cmp/cmp
```

## License

BSD - See [LICENSE][license] file

[license]: https://github.com/google/go-cmp/blob/master/LICENSE
# Shakers
🐹 + 🐙 = 😽 [![Circle CI](https://circleci.com/gh/vdemeester/shakers.svg?style=svg)](https://circleci.com/gh/vdemeester/shakers)

A collection of `go-check` Checkers to ease the use of it.

## Building and testing it

You need either [docker](https://github.com/docker/docker), or `go`
and `glide` in order to build and test shakers.

### Using Docker and Makefile

You need to run the ``test-unit`` target. 
```bash
$ make test-unit
docker build -t "shakers-dev:master" .
# […]
docker run --rm -it   "shakers-dev:master" ./script/make.sh test-unit
---> Making bundle: test-unit (in .)
+ go test -cover -coverprofile=cover.out .
ok      github.com/vdemeester/shakers   0.015s  coverage: 96.0% of statements

Test success
```

### Using glide and `GO15VENDOREXPERIMENT`

- Get the dependencies with `glide up` (or use `go get` but you have no garantuees over the version of the dependencies)
- If you're using glide (and not standard `go get`) export `GO15VENDOREXPERIMENT` with `export GO15VENDOREXPERIMENT=1`
- Run tests with `go test .`
Google API Extensions for Go
============================

[![Build Status](https://travis-ci.org/googleapis/gax-go.svg?branch=master)](https://travis-ci.org/googleapis/gax-go)
[![Code Coverage](https://img.shields.io/codecov/c/github/googleapis/gax-go.svg)](https://codecov.io/github/googleapis/gax-go)

Google API Extensions for Go (gax-go) is a set of modules which aids the
development of APIs for clients and servers based on `gRPC` and Google API
conventions.

Application code will rarely need to use this library directly,
but the code generated automatically from API definition files can use it
to simplify code generation and to provide more convenient and idiomatic API surface.

**This project is currently experimental and not supported.**

Go Versions
===========
This library requires Go 1.6 or above.

License
=======
BSD - please see [LICENSE](https://github.com/googleapis/gax-go/blob/master/LICENSE)
for more information.
Stream Control Transmission Protocol (SCTP)
----

[![Build Status](https://travis-ci.org/ishidawataru/sctp.svg?branch=master)](https://travis-ci.org/ishidawataru/sctp/builds)

Examples
----

See `example/sctp.go`

```go
$ cd example
$ go build
$ # run example SCTP server
$ ./example -server -port 1000 -ip 10.10.0.1,10.20.0.1
$ # run example SCTP client
$ ./example -port 1000 -ip 10.10.0.1,10.20.0.1
```
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

# Open Guest Compute Service (opengcs) [![Build Status](https://travis-ci.org/Microsoft/opengcs.svg?branch=master)](https://travis-ci.org/Microsoft/opengcs)

Open Guest Compute Service is a Linux open source project to further the development of a production quality implementation of Linux Hyper-V container on Windows (LCOW).  It's designed to run inside a custom Linux OS for supporting Linux container payload.

# Getting Started

  [How to build GCS binaries](./docs/gcsbuildinstructions.md/)

  [How to build custom Linux OS images](./docs/customosbuildinstructions.md/)

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
1. This program only runs in Linux. So you just first copy the files over to a Linux machine. 
2. Get Go and and then run make get-deps && make. This is set the $GOPATH for you and build the binaries.
3. vhd_to_tar and tar_to_vhd are the standalone executables that read/write to stdin/out and do the tar <-> vhd conversion.
   tar2vhd_server is the service VM server that takes client requests over hvsock.
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
go-radix [![Build Status](https://travis-ci.org/armon/go-radix.png)](https://travis-ci.org/armon/go-radix)
=========

Provides the `radix` package that implements a [radix tree](http://en.wikipedia.org/wiki/Radix_tree).
The package only provides a single `Tree` implementation, optimized for sparse nodes.

As a radix tree, it provides the following:
 * O(k) operations. In many cases, this can be faster than a hash table since
   the hash function is an O(k) operation, and hash tables have very poor cache locality.
 * Minimum / Maximum value lookups
 * Ordered iteration

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

go-metrics
==========

This library provides a `metrics` package which can be used to instrument code,
expose application metrics, and profile runtime performance in a flexible manner.

Sinks
=====

The `metrics` package makes use of a `MetricSink` interface to support delivery
to any type of backend. Currently the following sinks are provided:

* StatsiteSink : Sinks to a statsite instance (TCP)
* StatsdSink: Sinks to a statsd / statsite instance (UDP)
* InmemSink : Provides in-memory aggregation, can be used to export stats
* FanoutSink : Sinks to multiple sinks. Enables writing to multiple statsite instances for example.
* BlackholeSink : Sinks to nowhere

In addition to the sinks, the `InmemSignal` can be used to catch a signal,
and dump a formatted output of recent metrics. For example, when a process gets
a SIGUSR1, it can dump to stderr recent performance metrics for debugging.

Examples
========

Here is an example of using the package:

    func SlowMethod() {
        // Profiling the runtime of a method
        defer metrics.MeasureSince([]string{"SlowMethod"}, time.Now())
    }

    // Configure a statsite sink as the global metrics sink
    sink, _ := metrics.NewStatsiteSink("statsite:8125")
    metrics.NewGlobal(metrics.DefaultConfig("service-name"), sink)

    // Emit a Key/Value pair
    metrics.EmitKey([]string{"questions", "meaning of life"}, 42)


Here is an example of setting up an signal handler:

    // Setup the inmem sink and signal handler
    inm := NewInmemSink(10*time.Second, time.Minute)
    sig := DefaultInmemSignal(inm)
    metrics.NewGlobal(metrics.DefaultConfig("service-name"), inm)

    // Run some code
    inm.SetGauge([]string{"foo"}, 42)
	inm.EmitKey([]string{"bar"}, 30)

	inm.IncrCounter([]string{"baz"}, 42)
	inm.IncrCounter([]string{"baz"}, 1)
	inm.IncrCounter([]string{"baz"}, 80)

	inm.AddSample([]string{"method", "wow"}, 42)
	inm.AddSample([]string{"method", "wow"}, 100)
	inm.AddSample([]string{"method", "wow"}, 22)

    ....

When a signal comes in, output like the following will be dumped to stderr:

    [2014-01-28 14:57:33.04 -0800 PST][G] 'foo': 42.000
    [2014-01-28 14:57:33.04 -0800 PST][P] 'bar': 30.000
	[2014-01-28 14:57:33.04 -0800 PST][C] 'baz': Count: 3 Min: 1.000 Mean: 41.000 Max: 80.000 Stddev: 39.509
    [2014-01-28 14:57:33.04 -0800 PST][S] 'method.wow': Count: 3 Min: 22.000 Mean: 54.667 Max: 100.000 Stddev: 40.513

# go-stdlib

This repository contains OpenTracing instrumentation for packages in
the Go standard library.

For documentation on the packages,
[check godoc](https://godoc.org/github.com/opentracing-contrib/go-stdlib/).

**The APIs in the various packages are experimental and may change in
the future. You should vendor them to avoid spurious breakage.**

## Packages

Instrumentation is provided for the following packages, with the
following caveats:

- **net/http**: Client and server instrumentation. *Only supported
  with Go 1.7 and later.*
# CFSSL

[![Build Status](https://travis-ci.org/cloudflare/cfssl.svg?branch=master)](https://travis-ci.org/cloudflare/cfssl)
[![Coverage Status](http://codecov.io/github/cloudflare/cfssl/coverage.svg?branch=master)](http://codecov.io/github/cloudflare/cfssl?branch=master)
[![GoDoc](https://godoc.org/github.com/cloudflare/cfssl?status.svg)](https://godoc.org/github.com/cloudflare/cfssl)

## CloudFlare's PKI/TLS toolkit

CFSSL is CloudFlare's PKI/TLS swiss army knife. It is both a command line
tool and an HTTP API server for signing, verifying, and bundling TLS
certificates. It requires Go 1.8+ to build.

Note that certain linux distributions have certain algorithms removed
(RHEL-based distributions in particular), so the golang from the
official repositories will not work. Users of these distributions should
[install go manually](//golang.org/dl) to install CFSSL.

CFSSL consists of:

* a set of packages useful for building custom TLS PKI tools
* the `cfssl` program, which is the canonical command line utility
  using the CFSSL packages.
* the `multirootca` program, which is a certificate authority server
  that can use multiple signing keys.
* the `mkbundle` program is used to build certificate pool bundles.
* the `cfssljson` program, which takes the JSON output from the
  `cfssl` and `multirootca` programs and writes certificates, keys,
  CSRs, and bundles to disk.

### Building

See [BUILDING](BUILDING.md)

### Installation

Installation requires a
[working Go 1.8+ installation](http://golang.org/doc/install) and a
properly set `GOPATH`.

```
$ go get -u github.com/cloudflare/cfssl/cmd/cfssl
```

will download and build the CFSSL tool, installing it in
`$GOPATH/bin/cfssl`.

To install any of the other utility programs that are
in this repo (for instance `cffsljson` in this case):

```
$ go get -u github.com/cloudflare/cfssl/cmd/cfssljson
```

This will download and build the CFSSLJSON tool, installing it in
`$GOPATH/bin/`.

And to simply install __all__ of the programs in this repo:

```
$ go get -u github.com/cloudflare/cfssl/cmd/...
```

This will download, build, and install all of the utility programs
(including `cfssl`, `cfssljson`, and `mkbundle` among others) into the
`$GOPATH/bin/` directory.

### Using the Command Line Tool

The `cfssl` command line tool takes a command to specify what
operation it should carry out:

       sign             signs a certificate
       bundle           build a certificate bundle
       genkey           generate a private key and a certificate request
       gencert          generate a private key and a certificate
       serve            start the API server
       version          prints out the current version
       selfsign         generates a self-signed certificate
       print-defaults   print default configurations

Use `cfssl [command] -help` to find out more about a command.
The `version` command takes no arguments.

#### Signing

```
cfssl sign [-ca cert] [-ca-key key] [-hostname comma,separated,hostnames] csr [subject]
```

The `csr` is the client's certificate request. The `-ca` and `-ca-key`
flags are the CA's certificate and private key, respectively. By
default, they are `ca.pem` and `ca_key.pem`. The `-hostname` is
a comma separated hostname list that overrides the DNS names and
IP address in the certificate SAN extension.
For example, assuming the CA's private key is in
`/etc/ssl/private/cfssl_key.pem` and the CA's certificate is in
`/etc/ssl/certs/cfssl.pem`, to sign the `cloudflare.pem` certificate
for cloudflare.com:

```
cfssl sign -ca     /etc/ssl/certs/cfssl.pem       \
           -ca-key /etc/ssl/private/cfssl_key.pem \
           -hostname cloudflare.com               \
           ./cloudflare.pem
```

It is also possible to specify CSR with the `-csr` flag. By doing so,
flag values take precedence and will overwrite the argument.

The subject is an optional file that contains subject information that
should be used in place of the information from the CSR. It should be
a JSON file as follows:

```json
{
    "CN": "example.com",
    "names": [
        {
            "C":  "US",
            "L":  "San Francisco",
            "O":  "Internet Widgets, Inc.",
            "OU": "WWW",
            "ST": "California"
        }
    ]
}
```

**N.B.** As of Go 1.7, self-signed certificates will not include
[the AKI](https://go.googlesource.com/go/+/b623b71509b2d24df915d5bc68602e1c6edf38ca).

#### Bundling

```
cfssl bundle [-ca-bundle bundle] [-int-bundle bundle] \
             [-metadata metadata_file] [-flavor bundle_flavor] \
             -cert certificate_file [-key key_file]
```

The bundles are used for the root and intermediate certificate
pools. In addition, platform metadata is specified through `-metadata`.
The bundle files, metadata file (and auxiliary files) can be
found at:

        https://github.com/cloudflare/cfssl_trust

Specify PEM-encoded client certificate and key through `-cert` and
`-key` respectively. If key is specified, the bundle will be built
and verified with the key. Otherwise the bundle will be built
without a private key. Instead of file path, use `-` for reading
certificate PEM from stdin. It is also acceptable that the certificate
file should contain a (partial) certificate bundle.

Specify bundling flavor through `-flavor`. There are three flavors:
`optimal` to generate a bundle of shortest chain and most advanced
cryptographic algorithms, `ubiquitous` to generate a bundle of most
widely acceptance across different browsers and OS platforms, and
`force` to find an acceptable bundle which is identical to the
content of the input certificate file.

Alternatively, the client certificate can be pulled directly from
a domain. It is also possible to connect to the remote address
through `-ip`.

```
cfssl bundle [-ca-bundle bundle] [-int-bundle bundle] \
             [-metadata metadata_file] [-flavor bundle_flavor] \
             -domain domain_name [-ip ip_address]
```

The bundle output form should follow the example:

```json
{
    "bundle": "CERT_BUNDLE_IN_PEM",
    "crt": "LEAF_CERT_IN_PEM",
    "crl_support": true,
    "expires": "2015-12-31T23:59:59Z",
    "hostnames": ["example.com"],
    "issuer": "ISSUER CERT SUBJECT",
    "key": "KEY_IN_PEM",
    "key_size": 2048,
    "key_type": "2048-bit RSA",
    "ocsp": ["http://ocsp.example-ca.com"],
    "ocsp_support": true,
    "root": "ROOT_CA_CERT_IN_PEM",
    "signature": "SHA1WithRSA",
    "subject": "LEAF CERT SUBJECT",
    "status": {
        "rebundled": false,
        "expiring_SKIs": [],
        "untrusted_root_stores": [],
        "messages": [],
        "code": 0
    }
}
```


#### Generating certificate signing request and private key

```
cfssl genkey csr.json
```

To generate a private key and corresponding certificate request, specify
the key request as a JSON file. This file should follow the form:

```json
{
    "hosts": [
        "example.com",
        "www.example.com"
    ],
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C":  "US",
            "L":  "San Francisco",
            "O":  "Internet Widgets, Inc.",
            "OU": "WWW",
            "ST": "California"
        }
    ]
}
```

#### Generating self-signed root CA certificate and private key

```
cfssl genkey -initca csr.json | cfssljson -bare ca
```

To generate a self-signed root CA certificate, specify the key request as
a JSON file in the same format as in 'genkey'. Three PEM-encoded entities
will appear in the output: the private key, the csr, and the self-signed
certificate.

#### Generating a remote-issued certificate and private key.

```
cfssl gencert -remote=remote_server [-hostname=comma,separated,hostnames] csr.json
```

This calls `genkey` but has a remote CFSSL server sign and issue
the certificate. You may use `-hostname` to override certificate SANs.

#### Generating a local-issued certificate and private key.

```
cfssl gencert -ca cert -ca-key key [-hostname=comma,separated,hostnames] csr.json
```

This generates and issues a certificate and private key from a local CA
via a JSON request. You may use `-hostname` to override certificate SANs.


#### Updating an OCSP responses file with a newly issued certificate

```
cfssl ocspsign -ca cert -responder key -responder-key key -cert cert \
 | cfssljson -bare -stdout >> responses
```

This will generate an OCSP response for the `cert` and add it to the
`responses` file. You can then pass `responses` to `ocspserve` to start an
OCSP server.

### Starting the API Server

CFSSL comes with an HTTP-based API server; the endpoints are
documented in `doc/api/intro.txt`. The server is started with the `serve`
command:

```
cfssl serve [-address address] [-ca cert] [-ca-bundle bundle] \
            [-ca-key key] [-int-bundle bundle] [-int-dir dir] [-port port] \
            [-metadata file] [-remote remote_host] [-config config] \
            [-responder cert] [-responder-key key] [-db-config db-config]
```

Address and port default to "127.0.0.1:8888". The `-ca` and `-ca-key`
arguments should be the PEM-encoded certificate and private key to use
for signing; by default, they are `ca.pem` and `ca_key.pem`. The
`-ca-bundle` and `-int-bundle` should be the certificate bundles used
for the root and intermediate certificate pools, respectively. These
default to `ca-bundle.crt` and `int-bundle.crt` respectively. If the
`-remote` option is specified, all signature operations will be forwarded
to the remote CFSSL.

`-int-dir` specifies an intermediates directory. `-metadata` is a file for
root certificate presence. The content of the file is a json dictionary 
(k,v) such that each key k is an SHA-1 digest of a root certificate while value v 
is a list of key store filenames. `-config` specifies a path to a configuration
file. `-responder` and  `-responder-key` are the certificate and the
private key for the OCSP responder, respectively.

The amount of logging can be controlled with the `-loglevel` option. This
comes *after* the serve command:

```
cfssl serve -loglevel 2
```

The levels are:

* 0 - DEBUG
* 1 - INFO (this is the default level)
* 2 - WARNING
* 3 - ERROR
* 4 - CRITICAL

### The multirootca

The `cfssl` program can act as an online certificate authority, but it
only uses a single key. If multiple signing keys are needed, the
`multirootca` program can be used. It only provides the `sign`,
`authsign` and `info` endpoints. The documentation contains instructions
for configuring and running the CA.

### The mkbundle Utility

`mkbundle` is used to build the root and intermediate bundles used in
verifying certificates. It can be installed with

```
go get -u github.com/cloudflare/cfssl/cmd/mkbundle
```

It takes a collection of certificates, checks for CRL revocation (OCSP
support is planned for the next release) and expired certificates, and
bundles them into one file. It takes directories of certificates and
certificate files (which may contain multiple certificates). For example,
if the directory `intermediates` contains a number of intermediate
certificates:

```
mkbundle -f int-bundle.crt intermediates
```

will check those certificates and combine valid certificates into a single
`int-bundle.crt` file.

The `-f` flag specifies an output name; `-loglevel` specifies the verbosity
of the logging (using the same loglevels as above), and `-nw` controls the
number of revocation-checking workers.

### The cfssljson Utility

Most of the output from `cfssl` is in JSON. The `cfssljson` utility can take
this output and split it out into separate `key`, `certificate`, `CSR`, and
`bundle` files as appropriate. The tool takes a single flag, `-f`, that
specifies the input file, and an argument that specifies the base name for
the files produced. If the input filename is `-` (which is the default),
cfssljson reads from standard input. It maps keys in the JSON file to
filenames in the following way:

* if __cert__ or __certificate__ is specified,         __basename.pem__          will be produced.
* if __key__  or __private_key__ is specified,         __basename-key.pem__      will be produced.
* if __csr__  or __certificate_request__ is specified, __basename.csr__          will be produced.
* if __bundle__       is specified,                    __basename-bundle.pem__   will be produced.
* if __ocspResponse__ is specified,                    __basename-response.der__ will be produced.

Instead of saving to a file, you can pass `-stdout` to output the encoded
contents to standard output.

### Static Builds

By default, the web assets are accessed from disk, based on their
relative locations. If you wish to distribute a single,
statically-linked, `cfssl` binary, you’ll want to embed these resources
before building. This can by done with the
[go.rice](https://github.com/GeertJohan/go.rice) tool.

```
pushd cli/serve && rice embed-go && popd
```

Then building with `go build` will use the embedded resources.

### Using a PKCS#11 hardware token / HSM

For better security, you may wish to store your private key in an HSM or
smartcard. The interface to both of these categories of device is described by
the PKCS#11 spec. If you need to do approximately one signing operation per
second or fewer, the Yubikey NEO and NEO-n are inexpensive smartcard options:

        https://www.yubico.com/products/yubikey-hardware/yubikey-neo/

In general you should look for a product that supports PIV (personal identity verification). If
your signing needs are in the hundreds of signatures per second, you will need
to purchase an expensive HSM (in the thousands to many thousands of USD).

If you wish to try out the PKCS#11 signing modes without a hardware token, you
can use the [SoftHSM](https://github.com/opendnssec/SoftHSMv1#softhsm)
implementation. Please note that using SoftHSM simply stores your private key in
a file on disk and does not increase security.

To get started with your PKCS#11 token you will need to initialize it with a
private key, PIN, and token label. The instructions to do this will be specific
to each hardware device, and you should follow the instructions provided by your
vendor. You will also need to find the path to your `module`, a shared object
file (.so). Having initialized your device, you can query it to check your token
label with:

    pkcs11-tool --module <module path> --list-token-slots

You'll also want to check the label of the private key you imported (or
generated). Run the following command and look for a `Private Key Object`:

    pkcs11-tool --module <module path> --pin <pin> \
      --list-token-slots --login --list-objects

You now have all the information you need to use your PKCS#11 token with CFSSL.
CFSSL supports PKCS#11 for certificate signing and OCSP signing. To create a
Signer (for certificate signing), import `signer/universal` and call NewSigner
with a Root object containing the module, pin, token label and private label
from above, plus a path to your certificate. The structure of the Root object is
documented in `universal.go`.

Alternately, you can construct a pkcs11key.Key or pkcs11key.Pool yourself, and
pass it to ocsp.NewSigner (for OCSP) or local.NewSigner (for certificate
signing). This will be necessary, for example, if you are using a single-session
token like the Yubikey and need both OCSP signing and certificate signing at the
same time.

### Additional Documentation

Additional documentation can be found in the "doc" directory:

* `api/intro.txt`: documents the API endpoints
* `bootstrap.txt`: a walkthrough from building the package to getting
  up and running
# certdb usage

Using a database enables additional functionality for existing commands when a
db config is provided:

 - `sign` and `gencert` add a certificate to the certdb after signing it
 - `serve` enables database functionality for the sign and revoke endpoints

A database is required for the following:

 - `revoke` marks certificates revoked in the database with an optional reason
 - `ocsprefresh` refreshes the table of cached OCSP responses
 - `ocspdump` outputs cached OCSP responses in a concatenated base64-encoded format

## Setup/Migration

This directory stores [goose](https://bitbucket.org/liamstask/goose/) db migration scripts for various DB backends.
Currently supported:
 - MySQL in mysql
 - PostgreSQL in pg
 - SQLite in sqlite

### Get goose

    go get bitbucket.org/liamstask/goose/cmd/goose

### Use goose to start and terminate a MySQL DB
To start a MySQL using goose:

    goose -path $GOPATH/src/github.com/cloudflare/cfssl/certdb/mysql up

To tear down a MySQL DB using goose

    goose -path $GOPATH/src/github.com/cloudflare/cfssl/certdb/mysql down

Note: the administration of MySQL DB is not included. We assume
the databases being connected to are already created and access control
is properly handled.

### Use goose to start and terminate a PostgreSQL DB
To start a PostgreSQL using goose:

    goose -path $GOPATH/src/github.com/cloudflare/cfssl/certdb/pg up

To tear down a PostgreSQL DB using goose

    goose -path $GOPATH/src/github.com/cloudflare/cfssl/certdb/pg down

Note: the administration of PostgreSQL DB is not included. We assume
the databases being connected to are already created and access control
is properly handled.

### Use goose to start and terminate a SQLite DB
To start a SQLite DB using goose:

    goose -path $GOPATH/src/github.com/cloudflare/cfssl/certdb/sqlite up

To tear down a SQLite DB using goose

    goose -path $GOPATH/src/github.com/cloudflare/cfssl/certdb/sqlite down

## CFSSL Configuration

Several cfssl commands take a -db-config flag. Create a file with a
JSON dictionary:

    {"driver":"sqlite3","data_source":"certs.db"}

or

    {"driver":"postgres","data_source":"postgres://user:password@host/db"}
 
or

    {"driver":"mysql","data_source":"user:password@tcp(hostname:3306)/db?parseTime=true"}
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
# procfs

This procfs package provides functions to retrieve system, kernel and process
metrics from the pseudo-filesystem proc.

*WARNING*: This package is a work in progress. Its API may still break in
backwards-incompatible ways without warnings. Use it at your own risk.

[![GoDoc](https://godoc.org/github.com/prometheus/procfs?status.png)](https://godoc.org/github.com/prometheus/procfs)
[![Build Status](https://travis-ci.org/prometheus/procfs.svg?branch=master)](https://travis-ci.org/prometheus/procfs)
[![Go Report Card](https://goreportcard.com/badge/github.com/prometheus/procfs)](https://goreportcard.com/report/github.com/prometheus/procfs)
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
See [![go-doc](https://godoc.org/github.com/prometheus/client_golang/prometheus?status.svg)](https://godoc.org/github.com/prometheus/client_golang/prometheus).
# Common
[![Build Status](https://travis-ci.org/prometheus/common.svg)](https://travis-ci.org/prometheus/common)

This repository contains Go libraries that are shared across Prometheus
components and libraries.

* **config**: Common configuration structures
* **expfmt**: Decoding and encoding for the exposition format
* **log**: A logging wrapper around [logrus](https://github.com/sirupsen/logrus)
* **model**: Shared data structures
* **route**: A routing wrapper around [httprouter](https://github.com/julienschmidt/httprouter) using `context.Context`
* **version**: Version information and metrics
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
# go-jmespath - A JMESPath implementation in Go

[![Build Status](https://img.shields.io/travis/jmespath/go-jmespath.svg)](https://travis-ci.org/jmespath/go-jmespath)



See http://jmespath.org for more info.
################
GRPC-OpenTracing
################

This package enables distributed tracing in GRPC clients and servers via `The OpenTracing Project`_: a set of consistent, expressive, vendor-neutral APIs for distributed tracing and context propagation.

Once a production system contends with real concurrency or splits into many services, crucial (and formerly easy) tasks become difficult: user-facing latency optimization, root-cause analysis of backend errors, communication about distinct pieces of a now-distributed system, etc. Distributed tracing follows a request on its journey from inception to completion from mobile/browser all the way to the microservices. 

As core services and libraries adopt OpenTracing, the application builder is no longer burdened with the task of adding basic tracing instrumentation to their own code. In this way, developers can build their applications with the tools they prefer and benefit from built-in tracing instrumentation. OpenTracing implementations exist for major distributed tracing systems and can be bound or swapped with a one-line configuration change.

*******************
Further Information
*******************

If you’re interested in learning more about the OpenTracing standard, join the conversation on our `mailing list`_ or `Gitter`_.

If you want to learn more about the underlying API for your platform, visit the `source code`_. 

If you would like to implement OpenTracing in your project and need help, feel free to send us a note at `community@opentracing.io`_.

.. _The OpenTracing Project: http://opentracing.io/
.. _source code: https://github.com/opentracing/
.. _mailing list: http://opentracing.us13.list-manage.com/subscribe?u=180afe03860541dae59e84153&id=19117aa6cd
.. _Gitter: https://gitter.im/opentracing/public
.. _community@opentracing.io: community@opentracing.io
# OpenTracing support for gRPC in Go

The `otgrpc` package makes it easy to add OpenTracing support to gRPC-based
systems in Go.

## Installation

```
go get github.com/grpc-ecosystem/grpc-opentracing/go/otgrpc
```

## Documentation

See the basic usage examples below and the [package documentation on
godoc.org](https://godoc.org/github.com/grpc-ecosystem/grpc-opentracing/go/otgrpc).

## Client-side usage example

Wherever you call `grpc.Dial`:

```go
// You must have some sort of OpenTracing Tracer instance on hand.
var tracer opentracing.Tracer = ...
...

// Set up a connection to the server peer.
conn, err := grpc.Dial(
    address,
    ... // other options
    grpc.WithUnaryInterceptor(
        otgrpc.OpenTracingClientInterceptor(tracer)),
    grpc.WithStreamInterceptor(
        otgrpc.OpenTracingStreamClientInterceptor(tracer)))

// All future RPC activity involving `conn` will be automatically traced.
```

## Server-side usage example

Wherever you call `grpc.NewServer`:

```go
// You must have some sort of OpenTracing Tracer instance on hand.
var tracer opentracing.Tracer = ...
...

// Initialize the gRPC server.
s := grpc.NewServer(
    ... // other options
    grpc.UnaryInterceptor(
        otgrpc.OpenTracingServerInterceptor(tracer)),
    grpc.StreamInterceptor(
        otgrpc.OpenTracingStreamServerInterceptor(tracer)))

// All future RPC activity involving `s` will be automatically traced.
```

The repo has moved.
-------------------

https://github.com/opentracing-contrib/python-grpc
# Go gRPC Interceptors for Prometheus monitoring 

[![Travis Build](https://travis-ci.org/grpc-ecosystem/go-grpc-prometheus.svg)](https://travis-ci.org/grpc-ecosystem/go-grpc-prometheus)
[![Go Report Card](https://goreportcard.com/badge/github.com/grpc-ecosystem/go-grpc-prometheus)](http://goreportcard.com/report/grpc-ecosystem/go-grpc-prometheus)
[![GoDoc](http://img.shields.io/badge/GoDoc-Reference-blue.svg)](https://godoc.org/github.com/grpc-ecosystem/go-grpc-prometheus)
[![SourceGraph](https://sourcegraph.com/github.com/grpc-ecosystem/go-grpc-prometheus/-/badge.svg)](https://sourcegraph.com/github.com/grpc-ecosystem/go-grpc-prometheus/?badge)
[![codecov](https://codecov.io/gh/grpc-ecosystem/go-grpc-prometheus/branch/master/graph/badge.svg)](https://codecov.io/gh/grpc-ecosystem/go-grpc-prometheus)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[Prometheus](https://prometheus.io/) monitoring for your [gRPC Go](https://github.com/grpc/grpc-go) servers and clients.

A sister implementation for [gRPC Java](https://github.com/grpc/grpc-java) (same metrics, same semantics) is in [grpc-ecosystem/java-grpc-prometheus](https://github.com/grpc-ecosystem/java-grpc-prometheus).

## Interceptors

[gRPC Go](https://github.com/grpc/grpc-go) recently acquired support for Interceptors, i.e. middleware that is executed
by a gRPC Server before the request is passed onto the user's application logic. It is a perfect way to implement
common patterns: auth, logging and... monitoring.

To use Interceptors in chains, please see [`go-grpc-middleware`](https://github.com/mwitkow/go-grpc-middleware).

## Usage

There are two types of interceptors: client-side and server-side. This package provides monitoring Interceptors for both.

### Server-side

```go
import "github.com/grpc-ecosystem/go-grpc-prometheus"
...
    // Initialize your gRPC server's interceptor.
    myServer := grpc.NewServer(
        grpc.StreamInterceptor(grpc_prometheus.StreamServerInterceptor),
        grpc.UnaryInterceptor(grpc_prometheus.UnaryServerInterceptor),
    )
    // Register your gRPC service implementations.
    myservice.RegisterMyServiceServer(s.server, &myServiceImpl{})
    // After all your registrations, make sure all of the Prometheus metrics are initialized.
    grpc_prometheus.Register(myServer)
    // Register Prometheus metrics handler.    
    http.Handle("/metrics", promhttp.Handler())
...
```

### Client-side

```go
import "github.com/grpc-ecosystem/go-grpc-prometheus"
...
   clientConn, err = grpc.Dial(
       address,
		   grpc.WithUnaryInterceptor(grpc_prometheus.UnaryClientInterceptor),
		   grpc.WithStreamInterceptor(grpc_prometheus.StreamClientInterceptor)
   )
   client = pb_testproto.NewTestServiceClient(clientConn)
   resp, err := client.PingEmpty(s.ctx, &myservice.Request{Msg: "hello"})
...
```

# Metrics

## Labels

All server-side metrics start with `grpc_server` as Prometheus subsystem name. All client-side metrics start with `grpc_client`. Both of them have mirror-concepts. Similarly all methods
contain the same rich labels:
  
  * `grpc_service` - the [gRPC service](http://www.grpc.io/docs/#defining-a-service) name, which is the combination of protobuf `package` and
    the `grpc_service` section name. E.g. for `package = mwitkow.testproto` and 
     `service TestService` the label will be `grpc_service="mwitkow.testproto.TestService"`
  * `grpc_method` - the name of the method called on the gRPC service. E.g.  
    `grpc_method="Ping"`
  * `grpc_type` - the gRPC [type of request](http://www.grpc.io/docs/guides/concepts.html#rpc-life-cycle). 
    Differentiating between the two is important especially for latency measurements.

     - `unary` is single request, single response RPC
     - `client_stream` is a multi-request, single response RPC
     - `server_stream` is a single request, multi-response RPC
     - `bidi_stream` is a multi-request, multi-response RPC
    

Additionally for completed RPCs, the following labels are used:

  * `grpc_code` - the human-readable [gRPC status code](https://github.com/grpc/grpc-go/blob/master/codes/codes.go).
    The list of all statuses is to long, but here are some common ones:
      
      - `OK` - means the RPC was successful
      - `IllegalArgument` - RPC contained bad values
      - `Internal` - server-side error not disclosed to the clients
      
## Counters

The counters and their up to date documentation is in [server_reporter.go](server_reporter.go) and [client_reporter.go](client_reporter.go) 
the respective Prometheus handler (usually `/metrics`). 

For the purpose of this documentation we will only discuss `grpc_server` metrics. The `grpc_client` ones contain mirror concepts.

For simplicity, let's assume we're tracking a single server-side RPC call of [`mwitkow.testproto.TestService`](examples/testproto/test.proto),
calling the method `PingList`. The call succeeds and returns 20 messages in the stream.

First, immediately after the server receives the call it will increment the
`grpc_server_started_total` and start the handling time clock (if histograms are enabled). 

```jsoniq
grpc_server_started_total{grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream"} 1
```

Then the user logic gets invoked. It receives one message from the client containing the request 
(it's a `server_stream`):

```jsoniq
grpc_server_msg_received_total{grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream"} 1
```

The user logic may return an error, or send multiple messages back to the client. In this case, on 
each of the 20 messages sent back, a counter will be incremented:

```jsoniq
grpc_server_msg_sent_total{grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream"} 20
```

After the call completes, its status (`OK` or other [gRPC status code](https://github.com/grpc/grpc-go/blob/master/codes/codes.go)) 
and the relevant call labels increment the `grpc_server_handled_total` counter.

```jsoniq
grpc_server_handled_total{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream"} 1
```

## Histograms

[Prometheus histograms](https://prometheus.io/docs/concepts/metric_types/#histogram) are a great way
to measure latency distributions of your RPCs. However, since it is bad practice to have metrics
of [high cardinality](https://prometheus.io/docs/practices/instrumentation/#do-not-overuse-labels)
the latency monitoring metrics are disabled by default. To enable them please call the following
in your server initialization code:

```jsoniq
grpc_prometheus.EnableHandlingTimeHistogram()
```

After the call completes, its handling time will be recorded in a [Prometheus histogram](https://prometheus.io/docs/concepts/metric_types/#histogram)
variable `grpc_server_handling_seconds`. The histogram variable contains three sub-metrics:

 * `grpc_server_handling_seconds_count` - the count of all completed RPCs by status and method 
 * `grpc_server_handling_seconds_sum` - cumulative time of RPCs by status and method, useful for 
   calculating average handling times
 * `grpc_server_handling_seconds_bucket` - contains the counts of RPCs by status and method in respective
   handling-time buckets. These buckets can be used by Prometheus to estimate SLAs (see [here](https://prometheus.io/docs/practices/histograms/))

The counter values will look as follows:

```jsoniq
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.005"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.01"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.025"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.05"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.1"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.25"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="0.5"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="1"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="2.5"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="5"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="10"} 1
grpc_server_handling_seconds_bucket{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream",le="+Inf"} 1
grpc_server_handling_seconds_sum{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream"} 0.0003866430000000001
grpc_server_handling_seconds_count{grpc_code="OK",grpc_method="PingList",grpc_service="mwitkow.testproto.TestService",grpc_type="server_stream"} 1
```


## Useful query examples

Prometheus philosophy is to provide raw metrics to the monitoring system, and
let the aggregations be handled there. The verbosity of above metrics make it possible to have that
flexibility. Here's a couple of useful monitoring queries:


### request inbound rate
```jsoniq
sum(rate(grpc_server_started_total{job="foo"}[1m])) by (grpc_service)
```
For `job="foo"` (common label to differentiate between Prometheus monitoring targets), calculate the
rate of requests per second (1 minute window) for each gRPC `grpc_service` that the job has. Please note
how the `grpc_method` is being omitted here: all methods of a given gRPC service will be summed together.

### unary request error rate
```jsoniq
sum(rate(grpc_server_handled_total{job="foo",grpc_type="unary",grpc_code!="OK"}[1m])) by (grpc_service)
```
For `job="foo"`, calculate the per-`grpc_service` rate of `unary` (1:1) RPCs that failed, i.e. the 
ones that didn't finish with `OK` code.

### unary request error percentage
```jsoniq
sum(rate(grpc_server_handled_total{job="foo",grpc_type="unary",grpc_code!="OK"}[1m])) by (grpc_service)
 / 
sum(rate(grpc_server_started_total{job="foo",grpc_type="unary"}[1m])) by (grpc_service)
 * 100.0
```
For `job="foo"`, calculate the percentage of failed requests by service. It's easy to notice that
this is a combination of the two above examples. This is an example of a query you would like to
[alert on](https://prometheus.io/docs/alerting/rules/) in your system for SLA violations, e.g.
"no more than 1% requests should fail".

### average response stream size
```jsoniq
sum(rate(grpc_server_msg_sent_total{job="foo",grpc_type="server_stream"}[10m])) by (grpc_service)
 /
sum(rate(grpc_server_started_total{job="foo",grpc_type="server_stream"}[10m])) by (grpc_service)
```
For `job="foo"` what is the `grpc_service`-wide `10m` average of messages returned for all `
server_stream` RPCs. This allows you to track the stream sizes returned by your system, e.g. allows 
you to track when clients started to send "wide" queries that ret
Note the divisor is the number of started RPCs, in order to account for in-flight requests.

### 99%-tile latency of unary requests
```jsoniq
histogram_quantile(0.99, 
  sum(rate(grpc_server_handling_seconds_bucket{job="foo",grpc_type="unary"}[5m])) by (grpc_service,le)
)
```
For `job="foo"`, returns an 99%-tile [quantile estimation](https://prometheus.io/docs/practices/histograms/#quantiles)
of the handling time of RPCs per service. Please note the `5m` rate, this means that the quantile
estimation will take samples in a rolling `5m` window. When combined with other quantiles
(e.g. 50%, 90%), this query gives you tremendous insight into the responsiveness of your system 
(e.g. impact of caching).

### percentage of slow unary queries (>250ms)
```jsoniq
100.0 - (
sum(rate(grpc_server_handling_seconds_bucket{job="foo",grpc_type="unary",le="0.25"}[5m])) by (grpc_service)
 / 
sum(rate(grpc_server_handling_seconds_count{job="foo",grpc_type="unary"}[5m])) by (grpc_service)
) * 100.0
```
For `job="foo"` calculate the by-`grpc_service` fraction of slow requests that took longer than `0.25` 
seconds. This query is relatively complex, since the Prometheus aggregations use `le` (less or equal)
buckets, meaning that counting "fast" requests fractions is easier. However, simple maths helps.
This is an example of a query you would like to alert on in your system for SLA violations, 
e.g. "less than 1% of requests are slower than 250ms".


## Status

This code has been used since August 2015 as the basis for monitoring of *production* gRPC micro services  at [Improbable](https://improbable.io).

## License

`go-grpc-prometheus` is released under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.
[![Build Status](https://travis-ci.org/deckarep/golang-set.png?branch=master)](https://travis-ci.org/deckarep/golang-set)
[![GoDoc](https://godoc.org/github.com/deckarep/golang-set?status.png)](http://godoc.org/github.com/deckarep/golang-set)

## golang-set


The missing set collection for the Go language.  Until Go has sets built-in...use this.

Coming from Python one of the things I miss is the superbly wonderful set collection.  This is my attempt to mimic the primary features of the set from Python.
You can of course argue that there is no need for a set in Go, otherwise the creators would have added one to the standard library.  To those I say simply ignore this repository
and carry-on and to the rest that find this useful please contribute in helping me make it better by:

* Helping to make more idiomatic improvements to the code.
* Helping to increase the performance of it. ~~(So far, no attempt has been made, but since it uses a map internally, I expect it to be mostly performant.)~~
* Helping to make the unit-tests more robust and kick-ass.
* Helping to fill in the [documentation.](http://godoc.org/github.com/deckarep/golang-set)
* Simply offering feedback and suggestions.  (Positive, constructive feedback is appreciated.)

I have to give some credit for helping seed the idea with this post on [stackoverflow.](http://programmers.stackexchange.com/questions/177428/sets-data-structure-in-golang)

*Update* - as of 3/9/2014, you can use a compile-time generic version of this package in the [gen](http://clipperhouse.github.io/gen/) framework.  This framework allows you to use the golang-set in a completely generic and type-safe way by allowing you to generate a supporting .go file based on your custom types.

## Features (as of 9/22/2014)

* a CartesionProduct() method has been added with unit-tests: [Read more about the cartesion product](http://en.wikipedia.org/wiki/Cartesian_product)

## Features (as of 9/15/2014)

* a PowerSet() method has been added with unit-tests: [Read more about the Power set](http://en.wikipedia.org/wiki/Power_set)

## Features (as of 4/22/2014)

* One common interface to both implementations
* Two set implementations to choose from
  * a thread-safe implementation designed for concurrent use
  * a non-thread-safe implementation designed for performance
* 75 benchmarks for both implementations
* 35 unit tests for both implementations
* 14 concurrent tests for the thread-safe implementation



Please see the unit test file for additional usage examples.  The Python set documentation will also do a better job than I can of explaining how a set typically [works.](http://docs.python.org/2/library/sets.html)    Please keep in mind
however that the Python set is a built-in type and supports additional features and syntax that make it awesome.

## Examples but not exhaustive:

```go
requiredClasses := mapset.NewSet()
requiredClasses.Add("Cooking")
requiredClasses.Add("English")
requiredClasses.Add("Math")
requiredClasses.Add("Biology")

scienceSlice := []interface{}{"Biology", "Chemistry"}
scienceClasses := mapset.NewSetFromSlice(scienceSlice)

electiveClasses := mapset.NewSet()
electiveClasses.Add("Welding")
electiveClasses.Add("Music")
electiveClasses.Add("Automotive")

bonusClasses := mapset.NewSet()
bonusClasses.Add("Go Programming")
bonusClasses.Add("Python Programming")

//Show me all the available classes I can take
allClasses := requiredClasses.Union(scienceClasses).Union(electiveClasses).Union(bonusClasses)
fmt.Println(allClasses) //Set{Cooking, English, Math, Chemistry, Welding, Biology, Music, Automotive, Go Programming, Python Programming}


//Is cooking considered a science class?
fmt.Println(scienceClasses.Contains("Cooking")) //false

//Show me all classes that are not science classes, since I hate science.
fmt.Println(allClasses.Difference(scienceClasses)) //Set{Music, Automotive, Go Programming, Python Programming, Cooking, English, Math, Welding}

//Which science classes are also required classes?
fmt.Println(scienceClasses.Intersect(requiredClasses)) //Set{Biology}

//How many bonus classes do you offer?
fmt.Println(bonusClasses.Cardinality()) //2

//Do you have the following classes? Welding, Automotive and English?
fmt.Println(allClasses.IsSuperset(mapset.NewSetFromSlice([]interface{}{"Welding", "Automotive", "English"}))) //true
```

Thanks!

-Ralph

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/deckarep/golang-set/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

[![Analytics](https://ga-beacon.appspot.com/UA-42584447-2/deckarep/golang-set)](https://github.com/igrigorik/ga-beacon)
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

[![API Reference](http://img.shields.io/badge/api-reference-blue.svg)](http://docs.aws.amazon.com/sdk-for-go/api) [![Join the chat at https://gitter.im/aws/aws-sdk-go](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aws/aws-sdk-go?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Build Status](https://img.shields.io/travis/aws/aws-sdk-go.svg)](https://travis-ci.org/aws/aws-sdk-go) [![Apache V2 License](http://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/aws/aws-sdk-go/blob/master/LICENSE.txt)

# AWS SDK for Go

aws-sdk-go is the official AWS SDK for the Go programming language.

Checkout our [release notes](https://github.com/aws/aws-sdk-go/releases) for information about the latest bug fixes, updates, and features added to the SDK.

We [announced](https://aws.amazon.com/blogs/developer/aws-sdk-for-go-2-0-developer-preview/) the Developer Preview for the [v2 AWS SDK for Go](). The v2 SDK is available at https://github.com/aws/aws-sdk-go-v2, and `go get github.com/aws/aws-sdk-go-v2` via `go get`. Check out the v2 SDK's [changes and updates](https://github.com/aws/aws-sdk-go-v2/blob/master/CHANGELOG.md), and let us know what you think. We want your feedback. 

## Installing

If you are using Go 1.5 with the `GO15VENDOREXPERIMENT=1` vendoring flag, or 1.6 and higher you can use the following command to retrieve the SDK. The SDK's non-testing dependencies will be included and are vendored in the `vendor` folder.

    go get -u github.com/aws/aws-sdk-go

Otherwise if your Go environment does not have vendoring support enabled, or you do not want to include the vendored SDK's dependencies you can use the following command to retrieve the SDK and its non-testing dependencies using `go get`.

    go get -u github.com/aws/aws-sdk-go/aws/...
    go get -u github.com/aws/aws-sdk-go/service/...

If you're looking to retrieve just the SDK without any dependencies use the following command.

    go get -d github.com/aws/aws-sdk-go/

These two processes will still include the `vendor` folder and it should be deleted if its not going to be used by your environment.

    rm -rf $GOPATH/src/github.com/aws/aws-sdk-go/vendor

## Getting Help

Please use these community resources for getting help. We use the GitHub issues for tracking bugs and feature requests.

* Ask a question on [StackOverflow](http://stackoverflow.com/) and tag it with the [`aws-sdk-go`](http://stackoverflow.com/questions/tagged/aws-sdk-go) tag.
* Come join the AWS SDK for Go community chat on [gitter](https://gitter.im/aws/aws-sdk-go).
* Open a support ticket with [AWS Support](http://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
* If you think you may have found a bug, please open an [issue](https://github.com/aws/aws-sdk-go/issues/new).

## Opening Issues

If you encounter a bug with the AWS SDK for Go we would like to hear about it. Search the [existing issues](https://github.com/aws/aws-sdk-go/issues) and see if others are also experiencing the issue before opening a new issue. Please include the version of AWS SDK for Go, Go language, and OS you’re using. Please also include repro case when appropriate.

The GitHub issues are intended for bug reports and feature requests. For help and questions with using AWS SDK for GO please make use of the resources listed in the [Getting Help](https://github.com/aws/aws-sdk-go#getting-help) section. Keeping the list of open issues lean will help us respond in a timely manner.

## Reference Documentation

[`Getting Started Guide`](https://aws.amazon.com/sdk-for-go/) - This document is a general introduction how to configure and make requests with the SDK. If this is your first time using the SDK, this documentation and the API documentation will help you get started. This document focuses on the syntax and behavior of the SDK. The [Service Developer Guide](https://aws.amazon.com/documentation/) will help you get started using specific AWS services.

[`SDK API Reference Documentation`](https://docs.aws.amazon.com/sdk-for-go/api/) - Use this document to look up all API operation input and output parameters for AWS services supported by the SDK. The API reference also includes documentation of the SDK, and examples how to using the SDK, service client API operations, and API operation require parameters.

[`Service Developer Guide`](https://aws.amazon.com/documentation/) - Use this documentation to learn how to interface with an AWS service. These are great guides both, if you're getting started with a service, or looking for more information on a service. You should not need this document for coding, though in some cases, services may supply helpful samples that you might want to look out for.

[`SDK Examples`](https://github.com/aws/aws-sdk-go/tree/master/example) - Included in the SDK's repo are a several hand crafted examples using the SDK features and AWS services.

## Overview of SDK's Packages

The SDK is composed of two main components, SDK core, and service clients.
The SDK core packages are all available under the aws package at the root of
the SDK. Each client for a supported AWS service is available within its own
package under the service folder at the root of the SDK.

  * aws - SDK core, provides common shared types such as Config, Logger,
    and utilities to make working with API parameters easier.

      * awserr - Provides the error interface that the SDK will use for all
        errors that occur in the SDK's processing. This includes service API
        response errors as well. The Error type is made up of a code and message.
        Cast the SDK's returned error type to awserr.Error and call the Code
        method to compare returned error to specific error codes. See the package's
        documentation for additional values that can be extracted such as RequestID.

      * credentials - Provides the types and built in credentials providers
        the SDK will use to retrieve AWS credentials to make API requests with.
        Nested under this folder are also additional credentials providers such as
        stscreds for assuming IAM roles, and ec2rolecreds for EC2 Instance roles.

      * endpoints - Provides the AWS Regions and Endpoints metadata for the SDK.
        Use this to lookup AWS service endpoint information such as which services
        are in a region, and what regions a service is in. Constants are also provided
        for all region identifiers, e.g UsWest2RegionID for "us-west-2".

      * session - Provides initial default configuration, and load
        configuration from external sources such as environment and shared
        credentials file.

      * request - Provides the API request sending, and retry logic for the SDK.
        This package also includes utilities for defining your own request
        retryer, and configuring how the SDK processes the request.

  * service - Clients for AWS services. All services supported by the SDK are
    available under this folder.

## How to Use the SDK's AWS Service Clients

The SDK includes the Go types and utilities you can use to make requests to
AWS service APIs. Within the service folder at the root of the SDK you'll find
a package for each AWS service the SDK supports. All service clients follows
a common pattern of creation and usage.

When creating a client for an AWS service you'll first need to have a Session
value constructed. The Session provides shared configuration that can be shared
between your service clients. When service clients are created you can pass
in additional configuration via the aws.Config type to override configuration
provided by in the Session to create service client instances with custom
configuration.

Once the service's client is created you can use it to make API requests the
AWS service. These clients are safe to use concurrently.

## Configuring the SDK

In the AWS SDK for Go, you can configure settings for service clients, such
as the log level and maximum number of retries. Most settings are optional;
however, for each service client, you must specify a region and your credentials.
The SDK uses these values to send requests to the correct AWS region and sign
requests with the correct credentials. You can specify these values as part
of a session or as environment variables.

See the SDK's [configuration guide][config_guide] for more information.

See the [session][session_pkg] package documentation for more information on how to use Session
with the SDK.

See the [Config][config_typ] type in the [aws][aws_pkg] package for more information on configuration
options.

[config_guide]: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html
[session_pkg]: https://docs.aws.amazon.com/sdk-for-go/api/aws/session/
[config_typ]: https://docs.aws.amazon.com/sdk-for-go/api/aws/#Config
[aws_pkg]: https://docs.aws.amazon.com/sdk-for-go/api/aws/

### Configuring Credentials

When using the SDK you'll generally need your AWS credentials to authenticate
with AWS services. The SDK supports multiple methods of supporting these
credentials. By default the SDK will source credentials automatically from
its default credential chain. See the session package for more information
on this chain, and how to configure it. The common items in the credential
chain are the following:

  * Environment Credentials - Set of environment variables that are useful
    when sub processes are created for specific roles.

  * Shared Credentials file (~/.aws/credentials) - This file stores your
    credentials based on a profile name and is useful for local development.

  * EC2 Instance Role Credentials - Use EC2 Instance Role to assign credentials
    to application running on an EC2 instance. This removes the need to manage
    credential files in production.

Credentials can be configured in code as well by setting the Config's Credentials
value to a custom provider or using one of the providers included with the
SDK to bypass the default credential chain and use a custom one. This is
helpful when you want to instruct the SDK to only use a specific set of
credentials or providers.

This example creates a credential provider for assuming an IAM role, "myRoleARN"
and configures the S3 service client to use that role for API requests.

```go
  // Initial credentials loaded from SDK's default credential chain. Such as
  // the environment, shared credentials (~/.aws/credentials), or EC2 Instance
  // Role. These credentials will be used to to make the STS Assume Role API.
  sess := session.Must(session.NewSession())

  // Create the credentials from AssumeRoleProvider to assume the role
  // referenced by the "myRoleARN" ARN.
  creds := stscreds.NewCredentials(sess, "myRoleArn")

  // Create service client value configured for credentials
  // from assumed role.
  svc := s3.New(sess, &aws.Config{Credentials: creds})
```

See the [credentials][credentials_pkg] package documentation for more information on credential
providers included with the SDK, and how to customize the SDK's usage of
credentials.

The SDK has support for the shared configuration file (~/.aws/config). This
support can be enabled by setting the environment variable, "AWS_SDK_LOAD_CONFIG=1",
or enabling the feature in code when creating a Session via the
Option's SharedConfigState parameter.

```go
  sess := session.Must(session.NewSessionWithOptions(session.Options{
      SharedConfigState: session.SharedConfigEnable,
  }))
```

[credentials_pkg]: https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials

### Configuring AWS Region

In addition to the credentials you'll need to specify the region the SDK
will use to make AWS API requests to. In the SDK you can specify the region
either with an environment variable, or directly in code when a Session or
service client is created. The last value specified in code wins if the region
is specified multiple ways.

To set the region via the environment variable set the "AWS_REGION" to the
region you want to the SDK to use. Using this method to set the region will
allow you to run your application in multiple regions without needing additional
code in the application to select the region.

    AWS_REGION=us-west-2

The endpoints package includes constants for all regions the SDK knows. The
values are all suffixed with RegionID. These values are helpful, because they
reduce the need to type the region string manually.

To set the region on a Session use the aws package's Config struct parameter
Region to the AWS region you want the service clients created from the session to
use. This is helpful when you want to create multiple service clients, and
all of the clients make API requests to the same region.

```go
  sess := session.Must(session.NewSession(&aws.Config{
      Region: aws.String(endpoints.UsWest2RegionID),
  }))
```

See the [endpoints][endpoints_pkg] package for the AWS Regions and Endpoints metadata.

In addition to setting the region when creating a Session you can also set
the region on a per service client bases. This overrides the region of a
Session. This is helpful when you want to create service clients in specific
regions different from the Session's region.

```go
  svc := s3.New(sess, &aws.Config{
      Region: aws.String(endpoints.UsWest2RegionID),
  })
```

See the [Config][config_typ] type in the [aws][aws_pkg] package for more information and additional
options such as setting the Endpoint, and other service client configuration options.

[endpoints_pkg]: https://docs.aws.amazon.com/sdk-for-go/api/aws/endpoints/

## Making API Requests

Once the client is created you can make an API request to the service.
Each API method takes a input parameter, and returns the service response
and an error. The SDK provides methods for making the API call in multiple ways.

In this list we'll use the S3 ListObjects API as an example for the different
ways of making API requests.

  * ListObjects - Base API operation that will make the API request to the service.

  * ListObjectsRequest - API methods suffixed with Request will construct the
    API request, but not send it. This is also helpful when you want to get a
    presigned URL for a request, and share the presigned URL instead of your
    application making the request directly.

  * ListObjectsPages - Same as the base API operation, but uses a callback to
    automatically handle pagination of the API's response.

  * ListObjectsWithContext - Same as base API operation, but adds support for
    the Context pattern. This is helpful for controlling the canceling of in
    flight requests. See the Go standard library context package for more
    information. This method also takes request package's Option functional
    options as the variadic argument for modifying how the request will be
    made, or extracting information from the raw HTTP response.

  * ListObjectsPagesWithContext - same as ListObjectsPages, but adds support for
    the Context pattern. Similar to ListObjectsWithContext this method also
    takes the request package's Option function option types as the variadic
    argument.

In addition to the API operations the SDK also includes several higher level
methods that abstract checking for and waiting for an AWS resource to be in
a desired state. In this list we'll use WaitUntilBucketExists to demonstrate
the different forms of waiters.

  * WaitUntilBucketExists. - Method to make API request to query an AWS service for
    a resource's state. Will return successfully when that state is accomplished.

  * WaitUntilBucketExistsWithContext - Same as WaitUntilBucketExists, but adds
    support for the Context pattern. In addition these methods take request
    package's WaiterOptions to configure the waiter, and how underlying request
    will be made by the SDK.

The API method will document which error codes the service might return for
the operation. These errors will also be available as const strings prefixed
with "ErrCode" in the service client's package. If there are no errors listed
in the API's SDK documentation you'll need to consult the AWS service's API
documentation for the errors that could be returned.

```go
  ctx := context.Background()

  result, err := svc.GetObjectWithContext(ctx, &s3.GetObjectInput{
      Bucket: aws.String("my-bucket"),
      Key: aws.String("my-key"),
  })
  if err != nil {
      // Cast err to awserr.Error to handle specific error codes.
      aerr, ok := err.(awserr.Error)
      if ok && aerr.Code() == s3.ErrCodeNoSuchKey {
          // Specific error code handling
      }
      return err
  }

  // Make sure to close the body when done with it for S3 GetObject APIs or
  // will leak connections.
  defer result.Body.Close()

  fmt.Println("Object Size:", aws.Int64Value(result.ContentLength))
```

### API Request Pagination and Resource Waiters

Pagination helper methods are suffixed with "Pages", and provide the
functionality needed to round trip API page requests. Pagination methods
take a callback function that will be called for each page of the API's response.

```go
   objects := []string{}
   err := svc.ListObjectsPagesWithContext(ctx, &s3.ListObjectsInput{
       Bucket: aws.String(myBucket),
   }, func(p *s3.ListObjectsOutput, lastPage bool) bool {
       for _, o := range p.Contents {
           objects = append(objects, aws.StringValue(o.Key))
       }
       return true // continue paging
   })
   if err != nil {
       panic(fmt.Sprintf("failed to list objects for bucket, %s, %v", myBucket, err))
   }

   fmt.Println("Objects in bucket:", objects)
```

Waiter helper methods provide the functionality to wait for an AWS resource
state. These methods abstract the logic needed to to check the state of an
AWS resource, and wait until that resource is in a desired state. The waiter
will block until the resource is in the state that is desired, an error occurs,
or the waiter times out. If a resource times out the error code returned will
be request.WaiterResourceNotReadyErrorCode.

```go
  err := svc.WaitUntilBucketExistsWithContext(ctx, &s3.HeadBucketInput{
      Bucket: aws.String(myBucket),
  })
  if err != nil {
      aerr, ok := err.(awserr.Error)
      if ok && aerr.Code() == request.WaiterResourceNotReadyErrorCode {
          fmt.Fprintf(os.Stderr, "timed out while waiting for bucket to exist")
      }
      panic(fmt.Errorf("failed to wait for bucket to exist, %v", err))
  }
  fmt.Println("Bucket", myBucket, "exists")
```

## Complete SDK Example

This example shows a complete working Go file which will upload a file to S3
and use the Context pattern to implement timeout logic that will cancel the
request if it takes too long. This example highlights how to use sessions,
create a service client, make a request, handle the error, and process the
response.

```go
  package main

  import (
  	"context"
  	"flag"
  	"fmt"
  	"os"
  	"time"

  	"github.com/aws/aws-sdk-go/aws"
  	"github.com/aws/aws-sdk-go/aws/awserr"
  	"github.com/aws/aws-sdk-go/aws/request"
  	"github.com/aws/aws-sdk-go/aws/session"
  	"github.com/aws/aws-sdk-go/service/s3"
  )

  // Uploads a file to S3 given a bucket and object key. Also takes a duration
  // value to terminate the update if it doesn't complete within that time.
  //
  // The AWS Region needs to be provided in the AWS shared config or on the
  // environment variable as `AWS_REGION`. Credentials also must be provided
  // Will default to shared config file, but can load from environment if provided.
  //
  // Usage:
  //   # Upload myfile.txt to myBucket/myKey. Must complete within 10 minutes or will fail
  //   go run withContext.go -b mybucket -k myKey -d 10m < myfile.txt
  func main() {
  	var bucket, key string
  	var timeout time.Duration

  	flag.StringVar(&bucket, "b", "", "Bucket name.")
  	flag.StringVar(&key, "k", "", "Object key name.")
  	flag.DurationVar(&timeout, "d", 0, "Upload timeout.")
  	flag.Parse()

  	// All clients require a Session. The Session provides the client with
 	// shared configuration such as region, endpoint, and credentials. A
 	// Session should be shared where possible to take advantage of
 	// configuration and credential caching. See the session package for
 	// more information.
  	sess := session.Must(session.NewSession())

 	// Create a new instance of the service's client with a Session.
 	// Optional aws.Config values can also be provided as variadic arguments
 	// to the New function. This option allows you to provide service
 	// specific configuration.
  	svc := s3.New(sess)

  	// Create a context with a timeout that will abort the upload if it takes
  	// more than the passed in timeout.
  	ctx := context.Background()
  	var cancelFn func()
  	if timeout > 0 {
  		ctx, cancelFn = context.WithTimeout(ctx, timeout)
  	}
  	// Ensure the context is canceled to prevent leaking.
  	// See context package for more information, https://golang.org/pkg/context/
  	defer cancelFn()

  	// Uploads the object to S3. The Context will interrupt the request if the
  	// timeout expires.
  	_, err := svc.PutObjectWithContext(ctx, &s3.PutObjectInput{
  		Bucket: aws.String(bucket),
  		Key:    aws.String(key),
  		Body:   os.Stdin,
  	})
  	if err != nil {
  		if aerr, ok := err.(awserr.Error); ok && aerr.Code() == request.CanceledErrorCode {
  			// If the SDK can determine the request or retry delay was canceled
  			// by a context the CanceledErrorCode error code will be returned.
  			fmt.Fprintf(os.Stderr, "upload canceled due to timeout, %v\n", err)
  		} else {
  			fmt.Fprintf(os.Stderr, "failed to upload object, %v\n", err)
  		}
  		os.Exit(1)
  	}

  	fmt.Printf("successfully uploaded file to %s/%s\n", bucket, key)
  }
```

## License

This SDK is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0),
see LICENSE.txt and NOTICE.txt for more information.
## AWS SDK for Go Private packages ##
`private` is a collection of packages used internally by the SDK, and is subject to have breaking changes. This package is not `internal` so that if you really need to use its functionality, and understand breaking changes will be made, you are able to.

These packages will be refactored in the future so that the API generator and model parsers are exposed cleanly on their own. Making it easier for you to generate your own code based on the API models.
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

[![asciicinema example](https://asciinema.org/a/gPEIEo1NzmDTUu2bEPsUboqmU.png)](https://asciinema.org/a/gPEIEo1NzmDTUu2bEPsUboqmU)


## BuildKit

[![GoDoc](https://godoc.org/github.com/moby/buildkit?status.svg)](https://godoc.org/github.com/moby/buildkit/client/llb)
[![Build Status](https://travis-ci.org/moby/buildkit.svg?branch=master)](https://travis-ci.org/moby/buildkit)
[![Go Report Card](https://goreportcard.com/badge/github.com/moby/buildkit)](https://goreportcard.com/report/github.com/moby/buildkit)


BuildKit is a toolkit for converting source code to build artifacts in an efficient, expressive and repeatable manner.

Key features:
- Automatic garbage collection
- Extendable frontend formats
- Concurrent dependency resolution
- Efficient instruction caching
- Build cache import/export
- Nested build job invocations
- Distributable workers
- Multiple output formats
- Pluggable architecture
- Execution without root privileges


Read the proposal from https://github.com/moby/moby/issues/32925

Introductory blog post https://blog.mobyproject.org/introducing-buildkit-17e056cc5317

### Used by

[Moby](https://github.com/moby/moby/pull/37151)

[img](https://github.com/genuinetools/img)

[OpenFaaS Cloud](https://github.com/openfaas/openfaas-cloud)

[container build interface](https://github.com/containerbuilding/cbi)

### Quick start

Dependencies:
- [runc](https://github.com/opencontainers/runc)
- [containerd](https://github.com/containerd/containerd) (if you want to use containerd worker)


The following command installs `buildkitd` and `buildctl` to `/usr/local/bin`:

```bash
$ make && sudo make install
```

You can also use `make binaries-all` to prepare `buildkitd.containerd_only` and `buildkitd.oci_only`.

#### Starting the buildkitd daemon:

```
buildkitd --debug --root /var/lib/buildkit
```

The buildkitd daemon supports two worker backends: OCI (runc) and containerd.

By default, the OCI (runc) worker is used.
You can set `--oci-worker=false --containerd-worker=true` to use the containerd worker.

We are open to adding more backends.

#### Exploring LLB

BuildKit builds are based on a binary intermediate format called LLB that is used for defining the dependency graph for processes running part of your build. tl;dr: LLB is to Dockerfile what LLVM IR is to C.

- Marshaled as Protobuf messages
- Concurrently executable
- Efficiently cacheable
- Vendor-neutral (i.e. non-Dockerfile languages can be easily implemented)

See [`solver/pb/ops.proto`](./solver/pb/ops.proto) for the format definition.

Currently, following high-level languages has been implemented for LLB:

- Dockerfile (See [Exploring Dockerfiles](#exploring-dockerfiles))
- (open a PR to add your own language)

For understanding the basics of LLB, `examples/buildkit*` directory contains scripts that define how to build different configurations of BuildKit itself and its dependencies using the `client` package. Running one of these scripts generates a protobuf definition of a build graph. Note that the script itself does not execute any steps of the build.

You can use `buildctl debug dump-llb` to see what data is in this definition. Add `--dot` to generate dot layout.

```bash
go run examples/buildkit0/buildkit.go | buildctl debug dump-llb | jq .
```

To start building use `buildctl build` command. The example script accepts `--with-containerd` flag to choose if containerd binaries and support should be included in the end result as well. 

```bash
go run examples/buildkit0/buildkit.go | buildctl build
```

`buildctl build` will show interactive progress bar by default while the build job is running. It will also show you the path to the trace file that contains all information about the timing of the individual steps and logs.

Different versions of the example scripts show different ways of describing the build definition for this project to show the capabilities of the library. New versions have been added when new features have become available.

- `./examples/buildkit0` - uses only exec operations, defines a full stage per component.
- `./examples/buildkit1` - cloning git repositories has been separated for extra concurrency.
- `./examples/buildkit2` - uses git sources directly instead of running `git clone`, allowing better performance and much safer caching.
- `./examples/buildkit3` - allows using local source files for separate components eg. `./buildkit3 --runc=local | buildctl build --local runc-src=some/local/path`  
- `./examples/dockerfile2llb` - can be used to convert a Dockerfile to LLB for debugging purposes
- `./examples/gobuild` - shows how to use nested invocation to generate LLB for Go package internal dependencies


#### Exploring Dockerfiles

Frontends are components that run inside BuildKit and convert any build definition to LLB. There is a special frontend called gateway (gateway.v0) that allows using any image as a frontend.

During development, Dockerfile frontend (dockerfile.v0) is also part of the BuildKit repo. In the future, this will be moved out, and Dockerfiles can be built using an external image.

##### Building a Dockerfile with `buildctl`

```
buildctl build --frontend=dockerfile.v0 --local context=. --local dockerfile=.
buildctl build --frontend=dockerfile.v0 --local context=. --local dockerfile=. --frontend-opt target=foo --frontend-opt build-arg:foo=bar
```

`--local` exposes local source files from client to the builder. `context` and `dockerfile` are the names Dockerfile frontend looks for build context and Dockerfile location.

##### build-using-dockerfile utility

For people familiar with `docker build` command, there is an example wrapper utility in `./examples/build-using-dockerfile` that allows building Dockerfiles with BuildKit using a syntax similar to `docker build`.

```
go build ./examples/build-using-dockerfile && sudo install build-using-dockerfile /usr/local/bin

build-using-dockerfile -t myimage .
build-using-dockerfile -t mybuildkit -f ./hack/dockerfiles/test.Dockerfile .

# build-using-dockerfile will automatically load the resulting image to Docker
docker inspect myimage
```

##### Building a Dockerfile using [external frontend](https://hub.docker.com/r/tonistiigi/dockerfile/tags/):

During development, an external version of the Dockerfile frontend is pushed to https://hub.docker.com/r/tonistiigi/dockerfile that can be used with the gateway frontend. The source for the external frontend is currently located in `./frontend/dockerfile/cmd/dockerfile-frontend` but will move out of this repository in the future ([#163](https://github.com/moby/buildkit/issues/163)). For automatic build from master branch of this repository `tonistiigi/dockerfile:master` image can be used.

```
buildctl build --frontend=gateway.v0 --frontend-opt=source=tonistiigi/dockerfile --local context=. --local dockerfile=.
buildctl build --frontend gateway.v0 --frontend-opt=source=tonistiigi/dockerfile --frontend-opt=context=git://github.com/moby/moby --frontend-opt build-arg:APT_MIRROR=cdn-fastly.deb.debian.org
````

### Exporters

By default, the build result and intermediate cache will only remain internally in BuildKit. Exporter needs to be specified to retrieve the result.

##### Exporting resulting image to containerd

The containerd worker needs to be used

```
buildctl build ... --exporter=image --exporter-opt name=docker.io/username/image
ctr --namespace=buildkit images ls
```

##### Push resulting image to registry

```
buildctl build ... --exporter=image --exporter-opt name=docker.io/username/image --exporter-opt push=true
```

If credentials are required, `buildctl` will attempt to read Docker configuration file.


##### Exporting build result back to client

The local client will copy the files directly to the client. This is useful if BuildKit is being used for building something else than container images.

```
buildctl build ... --exporter=local --exporter-opt output=path/to/output-dir
```

##### Exporting built image to Docker

```
# exported tarball is also compatible with OCI spec
buildctl build ... --exporter=docker --exporter-opt name=myimage | docker load
```

##### Exporting [OCI Image Format](https://github.com/opencontainers/image-spec) tarball to client

```
buildctl build ... --exporter=oci --exporter-opt output=path/to/output.tar
buildctl build ... --exporter=oci > output.tar
```

### Other

#### View build cache

```
buildctl du -v
```

#### Show enabled workers

```
buildctl debug workers -v
```

### Running containerized buildkit

BuildKit can also be used by running the `buildkitd` daemon inside a Docker container and accessing it remotely. The client tool `buildctl` is also available for Mac and Windows.

To run daemon in a container:

```
docker run -d --privileged -p 1234:1234 tonistiigi/buildkit --addr tcp://0.0.0.0:1234
export BUILDKIT_HOST=tcp://0.0.0.0:1234
buildctl build --help
```

The `tonistiigi/buildkit` image can be built locally using the Dockerfile in `./hack/dockerfiles/test.Dockerfile`.

### Opentracing support

BuildKit supports opentracing for buildkitd gRPC API and buildctl commands. To capture the trace to [Jaeger](https://github.com/jaegertracing/jaeger), set `JAEGER_TRACE` environment variable to the collection address.


```
docker run -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:latest
export JAEGER_TRACE=0.0.0.0:6831
# restart buildkitd and buildctl so they know JAEGER_TRACE
# any buildctl command should be traced to http://127.0.0.1:16686/
```


### Supported runc version

During development, BuildKit is tested with the version of runc that is being used by the containerd repository. Please refer to [runc.md](https://github.com/containerd/containerd/blob/v1.1.3/RUNC.md) for more information.

### Running BuildKit without root privileges

Please refer to [`docs/rootless.md`](docs/rootless.md).

### Contributing

Running tests:

```bash
make test
```

This runs all unit and integration tests in a containerized environment. Locally, every package can be tested separately with standard Go tools, but integration tests are skipped if local user doesn't have enough permissions or worker binaries are not installed.

```
# test a specific package only
make test TESTPKGS=./client

# run a specific test with all worker combinations
make test TESTPKGS=./client TESTFLAGS="--run /TestCallDiskUsage -v" 

# run all integration tests with a specific worker
# supported workers: oci, oci-rootless, containerd, containerd-1.0
make test TESTPKGS=./client TESTFLAGS="--run //worker=containerd -v" 
```

Updating vendored dependencies:

```bash
# update vendor.conf
make vendor
```

Validating your updates before submission:

```bash
make validate-all
```
INI [![Build Status](https://travis-ci.org/go-ini/ini.svg?branch=master)](https://travis-ci.org/go-ini/ini) [![Sourcegraph](https://sourcegraph.com/github.com/go-ini/ini/-/badge.svg)](https://sourcegraph.com/github.com/go-ini/ini?badge)
===

![](https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

[简体中文](README_ZH.md)

## Feature

- Load multiple data sources(`[]byte`, file and `io.ReadCloser`) with overwrites.
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

	go get gopkg.in/ini.v1

To use with latest changes:

	go get github.com/go-ini/ini

Please add `-u` flag to update in the future.

### Testing

If you want to test on your machine, please apply `-t` flag:

	go get -t gopkg.in/ini.v1

Please add `-u` flag to update in the future.

## Getting Started

### Loading from data sources

A **Data Source** is either raw data in type `[]byte`, a file name with type `string` or `io.ReadCloser`. You can load **as many data sources as you want**. Passing other types will simply return an error.

```go
cfg, err := ini.Load([]byte("raw data"), "filename", ioutil.NopCloser(bytes.NewReader([]byte("some other data"))))
```

Or start with an empty object:

```go
cfg := ini.Empty()
```

When you cannot decide how many data sources to load at the beginning, you will still be able to **Append()** them later.

```go
err := cfg.Append("other file", []byte("other raw data"))
```

If you have a list of files with possibilities that some of them may not available at the time, and you don't know exactly which ones, you can use `LooseLoad` to ignore nonexistent files without returning error.

```go
cfg, err := ini.LooseLoad("filename", "filename_404")
```

The cool thing is, whenever the file is available to load while you're calling `Reload` method, it will be counted as usual.

#### Ignore cases of key name

When you do not care about cases of section and key names, you can use `InsensitiveLoad` to force all names to be lowercased while parsing.

```go
cfg, err := ini.InsensitiveLoad("filename")
//...

// sec1 and sec2 are the exactly same section object
sec1, err := cfg.GetSection("Section")
sec2, err := cfg.GetSection("SecTIOn")

// key1 and key2 are the exactly same key object
key1, err := cfg.GetKey("Key")
key2, err := cfg.GetKey("KeY")
```

#### MySQL-like boolean key 

MySQL's configuration allows a key without value as follows:

```ini
[mysqld]
...
skip-host-cache
skip-name-resolve
```

By default, this is considered as missing value. But if you know you're going to deal with those cases, you can assign advanced load options:

```go
cfg, err := LoadSources(LoadOptions{AllowBooleanKeys: true}, "my.cnf"))
```

The value of those keys are always `true`, and when you save to a file, it will keep in the same foramt as you read.

To generate such keys in your program, you could use `NewBooleanKey`:

```go
key, err := sec.NewBooleanKey("skip-host-cache")
```

#### Comment

Take care that following format will be treated as comment:

1. Line begins with `#` or `;`
2. Words after `#` or `;`
3. Words after section name (i.e words after `[some section name]`)

If you want to save a value with `#` or `;`, please quote them with ``` ` ``` or ``` """ ```.

### Working with sections

To get a section, you would need to:

```go
section, err := cfg.GetSection("section name")
```

For a shortcut for default section, just give an empty string as name:

```go
section, err := cfg.GetSection("")
```

When you're pretty sure the section exists, following code could make your life easier:

```go
section := cfg.Section("section name")
```

What happens when the section somehow does not exist? Don't panic, it automatically creates and returns a new section to you.

To create a new section:

```go
err := cfg.NewSection("new section")
```

To get a list of sections or section names:

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### Working with keys

To get a key under a section:

```go
key, err := cfg.Section("").GetKey("key name")
```

Same rule applies to key operations:

```go
key := cfg.Section("").Key("key name")
```

To check if a key exists:

```go
yes := cfg.Section("").HasKey("key name")
```

To create a new key:

```go
err := cfg.Section("").NewKey("name", "value")
```

To get a list of keys or key names:

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

To get a clone hash of keys and corresponding values:

```go
hash := cfg.Section("").KeysHash()
```

### Working with values

To get a string value:

```go
val := cfg.Section("").Key("key name").String()
```

To validate key value on the fly:

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

If you do not want any auto-transformation (such as recursive read) for the values, you can get raw value directly (this way you get much better performance):

```go
val := cfg.Section("").Key("key name").Value()
```

To check if raw value exists:

```go
yes := cfg.Section("").HasValue("test value")
```

To get value with types:

```go
// For boolean values:
// true when value is: 1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false when value is: 0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// Methods start with Must also accept one argument for default value
// when key not found or fail to parse value to given type.
// Except method MustString, which you have to pass a default value.

v = cfg.Section("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

What if my value is three-line long?

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

Not a problem!

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

That's cool, how about continuation lines?

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

Piece of cake!

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

Well, I hate continuation lines, how do I disable that?

```go
cfg, err := ini.LoadSources(ini.LoadOptions{
	IgnoreContinuation: true,
}, "filename")
```

Holy crap! 

Note that single quotes around values will be stripped:

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

That's all? Hmm, no.

#### Helper methods of working with values

To get value with given candidates:

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

Default value will be presented if value of key is not in candidates you given, and default value does not need be one of candidates.

To validate value in a given range:

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

##### Auto-split values into a slice

To use zero value of type for invalid inputs:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [0.0 2.2 0.0 0.0]
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

To exclude invalid values out of result slice:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [2.2]
vals = cfg.Section("").Key("FLOAT64S").ValidFloat64s(",")
vals = cfg.Section("").Key("INTS").ValidInts(",")
vals = cfg.Section("").Key("INT64S").ValidInt64s(",")
vals = cfg.Section("").Key("UINTS").ValidUints(",")
vals = cfg.Section("").Key("UINT64S").ValidUint64s(",")
vals = cfg.Section("").Key("TIMES").ValidTimes(",")
```

Or to return nothing but error when have invalid inputs:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> error
vals = cfg.Section("").Key("FLOAT64S").StrictFloat64s(",")
vals = cfg.Section("").Key("INTS").StrictInts(",")
vals = cfg.Section("").Key("INT64S").StrictInt64s(",")
vals = cfg.Section("").Key("UINTS").StrictUints(",")
vals = cfg.Section("").Key("UINT64S").StrictUint64s(",")
vals = cfg.Section("").Key("TIMES").StrictTimes(",")
```

### Save your configuration

Finally, it's time to save your configuration to somewhere.

A typical way to save configuration is writing it to a file:

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

Another way to save is writing to a `io.Writer` interface:

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

By default, spaces are used to align "=" sign between key and values, to disable that:

```go
ini.PrettyFormat = false
``` 

## Advanced Usage

### Recursive Values

For all value of keys, there is a special syntax `%(<name>)s`, where `<name>` is the key name in same section or default section, and `%(<name>)s` will be replaced by corresponding value(empty string if key not found). You can use this syntax at most 99 level of recursions.

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### Parent-child Sections

You can use `.` in section name to indicate parent-child relationship between two or more sections. If the key not found in the child section, library will try again on its parent section until there is no parent section.

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### Retrieve parent keys available to a child section

```go
cfg.Section("package.sub").ParentKeys() // ["CLONE_URL"]
```

### Unparseable Sections

Sometimes, you have sections that do not contain key-value pairs but raw content, to handle such case, you can use `LoadOptions.UnparsableSections`:

```go
cfg, err := LoadSources(LoadOptions{UnparseableSections: []string{"COMMENTS"}}, `[COMMENTS]
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>`))

body := cfg.Section("COMMENTS").Body()

/* --- start ---
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>
------  end  --- */
```

### Auto-increment Key Names

If key name is `-` in data source, then it would be seen as special syntax for auto-increment key name start from 1, and every section is independent on counter.

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### Map To Struct

Want more objective way to play with INI? Cool.

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// Things can be simpler.
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// Just map a section? Fine.
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

Can I have default value for field? Absolutely.

Assign it before you map to struct. It will keep the value as it is if the key is not presented or got wrong type.

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

It's really cool, but what's the point if you can't give me my file back from struct?

### Reflect From Struct

Why not?

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string    `ini:"places,omitempty"`
	None   []int       `ini:",omitempty"`
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

So, what do I get?

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
places = HangZhou,Boston
```

#### Name Mapper

To save your time and make your code cleaner, this library supports [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) between struct field and actual section and key name.

There are 2 built-in name mappers:

- `AllCapsUnderscore`: it converts to format `ALL_CAPS_UNDERSCORE` then match section or key.
- `TitleUnderscore`: it converts to format `title_underscore` then match section or key.

To use them:

```go
type Info struct {
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

Same rules of name mapper apply to `ini.ReflectFromWithMapper` function.

#### Value Mapper

To expand values (e.g. from environment variables), you can use the `ValueMapper` to transform values:

```go
type Env struct {
	Foo string `ini:"foo"`
}

func main() {
	cfg, err := ini.Load([]byte("[env]\nfoo = ${MY_VAR}\n")
	cfg.ValueMapper = os.ExpandEnv
	// ...
	env := &Env{}
	err = cfg.Section("env").MapTo(env)
}
```

This would set the value of `env.Foo` to the value of the environment variable `MY_VAR`.

#### Other Notes On Map/Reflect

Any embedded struct is treated as a section by default, and there is no automatic parent-child relations in map/reflect feature:

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

What if, yes, I'm paranoid, I want embedded struct to be in the same section. Well, all roads lead to Rome.

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## Getting Help

- [API Documentation](https://gowalker.org/gopkg.in/ini.v1)
- [File An Issue](https://github.com/go-ini/ini/issues/new)

## FAQs

### What does `BlockMode` field do?

By default, library lets you read and write values so we need a locker to make sure your data is safe. But in cases that you are very sure about only reading data through the library, you can set `cfg.BlockMode = false` to speed up read operations about **50-70%** faster.

### Why another INI library?

Many people are using my another INI library [goconfig](https://github.com/Unknwon/goconfig), so the reason for this one is I would like to make more Go style code. Also when you set `cfg.BlockMode = false`, this one is about **10-30%** faster.

To make those changes I have to confirm API broken, so it's safer to keep it in another place and start using `gopkg.in` to version my package at this time.(PS: shorter import path)

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.
本包提供了 Go 语言中读写 INI 文件的功能。

## 功能特性

- 支持覆盖加载多个数据源（`[]byte`、文件和 `io.ReadCloser`）
- 支持递归读取键值
- 支持读取父子分区
- 支持读取自增键名
- 支持读取多行的键值
- 支持大量辅助方法
- 支持在读取时直接转换为 Go 语言类型
- 支持读取和 **写入** 分区和键的注释
- 轻松操作分区、键值和注释
- 在保存文件时分区和键值会保持原有的顺序

## 下载安装

使用一个特定版本：

    go get gopkg.in/ini.v1

使用最新版：

	go get github.com/go-ini/ini

如需更新请添加 `-u` 选项。

### 测试安装

如果您想要在自己的机器上运行测试，请使用 `-t` 标记：

	go get -t gopkg.in/ini.v1

如需更新请添加 `-u` 选项。

## 开始使用

### 从数据源加载

一个 **数据源** 可以是 `[]byte` 类型的原始数据，`string` 类型的文件路径或 `io.ReadCloser`。您可以加载 **任意多个** 数据源。如果您传递其它类型的数据源，则会直接返回错误。

```go
cfg, err := ini.Load([]byte("raw data"), "filename", ioutil.NopCloser(bytes.NewReader([]byte("some other data"))))
```

或者从一个空白的文件开始：

```go
cfg := ini.Empty()
```

当您在一开始无法决定需要加载哪些数据源时，仍可以使用 **Append()** 在需要的时候加载它们。

```go
err := cfg.Append("other file", []byte("other raw data"))
```

当您想要加载一系列文件，但是不能够确定其中哪些文件是不存在的，可以通过调用函数 `LooseLoad` 来忽略它们（`Load` 会因为文件不存在而返回错误）：

```go
cfg, err := ini.LooseLoad("filename", "filename_404")
```

更牛逼的是，当那些之前不存在的文件在重新调用 `Reload` 方法的时候突然出现了，那么它们会被正常加载。

#### 忽略键名的大小写

有时候分区和键的名称大小写混合非常烦人，这个时候就可以通过 `InsensitiveLoad` 将所有分区和键名在读取里强制转换为小写：

```go
cfg, err := ini.InsensitiveLoad("filename")
//...

// sec1 和 sec2 指向同一个分区对象
sec1, err := cfg.GetSection("Section")
sec2, err := cfg.GetSection("SecTIOn")

// key1 和 key2 指向同一个键对象
key1, err := cfg.GetKey("Key")
key2, err := cfg.GetKey("KeY")
```

#### 类似 MySQL 配置中的布尔值键

MySQL 的配置文件中会出现没有具体值的布尔类型的键：

```ini
[mysqld]
...
skip-host-cache
skip-name-resolve
```

默认情况下这被认为是缺失值而无法完成解析，但可以通过高级的加载选项对它们进行处理：

```go
cfg, err := LoadSources(LoadOptions{AllowBooleanKeys: true}, "my.cnf"))
```

这些键的值永远为 `true`，且在保存到文件时也只会输出键名。

如果您想要通过程序来生成此类键，则可以使用 `NewBooleanKey`：

```go
key, err := sec.NewBooleanKey("skip-host-cache")
```

#### 关于注释

下述几种情况的内容将被视为注释：

1. 所有以 `#` 或 `;` 开头的行
2. 所有在 `#` 或 `;` 之后的内容
3. 分区标签后的文字 (即 `[分区名]` 之后的内容)

如果你希望使用包含 `#` 或 `;` 的值，请使用 ``` ` ``` 或 ``` """ ``` 进行包覆。

### 操作分区（Section）

获取指定分区：

```go
section, err := cfg.GetSection("section name")
```

如果您想要获取默认分区，则可以用空字符串代替分区名：

```go
section, err := cfg.GetSection("")
```

当您非常确定某个分区是存在的，可以使用以下简便方法：

```go
section := cfg.Section("section name")
```

如果不小心判断错了，要获取的分区其实是不存在的，那会发生什么呢？没事的，它会自动创建并返回一个对应的分区对象给您。

创建一个分区：

```go
err := cfg.NewSection("new section")
```

获取所有分区对象或名称：

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### 操作键（Key）

获取某个分区下的键：

```go
key, err := cfg.Section("").GetKey("key name")
```

和分区一样，您也可以直接获取键而忽略错误处理：

```go
key := cfg.Section("").Key("key name")
```

判断某个键是否存在：

```go
yes := cfg.Section("").HasKey("key name")
```

创建一个新的键：

```go
err := cfg.Section("").NewKey("name", "value")
```

获取分区下的所有键或键名：

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

获取分区下的所有键值对的克隆：

```go
hash := cfg.Section("").KeysHash()
```

### 操作键值（Value）

获取一个类型为字符串（string）的值：

```go
val := cfg.Section("").Key("key name").String()
```

获取值的同时通过自定义函数进行处理验证：

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

如果您不需要任何对值的自动转变功能（例如递归读取），可以直接获取原值（这种方式性能最佳）：

```go
val := cfg.Section("").Key("key name").Value()
```

判断某个原值是否存在：

```go
yes := cfg.Section("").HasValue("test value")
```

获取其它类型的值：

```go
// 布尔值的规则：
// true 当值为：1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false 当值为：0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// 由 Must 开头的方法名允许接收一个相同类型的参数来作为默认值，
// 当键不存在或者转换失败时，则会直接返回该默认值。
// 但是，MustString 方法必须传递一个默认值。

v = cfg.Seciont("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

如果我的值有好多行怎么办？

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

嗯哼？小 case！

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

赞爆了！那要是我属于一行的内容写不下想要写到第二行怎么办？

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

简直是小菜一碟！

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

可是我有时候觉得两行连在一起特别没劲，怎么才能不自动连接两行呢？

```go
cfg, err := ini.LoadSources(ini.LoadOptions{
	IgnoreContinuation: true,
}, "filename")
```

哇靠给力啊！

需要注意的是，值两侧的单引号会被自动剔除：

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

这就是全部了？哈哈，当然不是。

#### 操作键值的辅助方法

获取键值时设定候选值：

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

如果获取到的值不是候选值的任意一个，则会返回默认值，而默认值不需要是候选值中的一员。

验证获取的值是否在指定范围内：

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

##### 自动分割键值到切片（slice）

当存在无效输入时，使用零值代替：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [0.0 2.2 0.0 0.0]
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

从结果切片中剔除无效输入：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [2.2]
vals = cfg.Section("").Key("FLOAT64S").ValidFloat64s(",")
vals = cfg.Section("").Key("INTS").ValidInts(",")
vals = cfg.Section("").Key("INT64S").ValidInt64s(",")
vals = cfg.Section("").Key("UINTS").ValidUints(",")
vals = cfg.Section("").Key("UINT64S").ValidUint64s(",")
vals = cfg.Section("").Key("TIMES").ValidTimes(",")
```

当存在无效输入时，直接返回错误：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> error
vals = cfg.Section("").Key("FLOAT64S").StrictFloat64s(",")
vals = cfg.Section("").Key("INTS").StrictInts(",")
vals = cfg.Section("").Key("INT64S").StrictInt64s(",")
vals = cfg.Section("").Key("UINTS").StrictUints(",")
vals = cfg.Section("").Key("UINT64S").StrictUint64s(",")
vals = cfg.Section("").Key("TIMES").StrictTimes(",")
```

### 保存配置

终于到了这个时刻，是时候保存一下配置了。

比较原始的做法是输出配置到某个文件：

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

另一个比较高级的做法是写入到任何实现 `io.Writer` 接口的对象中：

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

默认情况下，空格将被用于对齐键值之间的等号以美化输出结果，以下代码可以禁用该功能：

```go
ini.PrettyFormat = false
``` 

## 高级用法

### 递归读取键值

在获取所有键值的过程中，特殊语法 `%(<name>)s` 会被应用，其中 `<name>` 可以是相同分区或者默认分区下的键名。字符串 `%(<name>)s` 会被相应的键值所替代，如果指定的键不存在，则会用空字符串替代。您可以最多使用 99 层的递归嵌套。

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### 读取父子分区

您可以在分区名称中使用 `.` 来表示两个或多个分区之间的父子关系。如果某个键在子分区中不存在，则会去它的父分区中再次寻找，直到没有父分区为止。

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### 获取上级父分区下的所有键名

```go
cfg.Section("package.sub").ParentKeys() // ["CLONE_URL"]
```

### 无法解析的分区

如果遇到一些比较特殊的分区，它们不包含常见的键值对，而是没有固定格式的纯文本，则可以使用 `LoadOptions.UnparsableSections` 进行处理：

```go
cfg, err := LoadSources(LoadOptions{UnparseableSections: []string{"COMMENTS"}}, `[COMMENTS]
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>`))

body := cfg.Section("COMMENTS").Body()

/* --- start ---
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>
------  end  --- */
```

### 读取自增键名

如果数据源中的键名为 `-`，则认为该键使用了自增键名的特殊语法。计数器从 1 开始，并且分区之间是相互独立的。

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### 映射到结构

想要使用更加面向对象的方式玩转 INI 吗？好主意。

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// 一切竟可以如此的简单。
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// 嗯哼？只需要映射一个分区吗？
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

结构的字段怎么设置默认值呢？很简单，只要在映射之前对指定字段进行赋值就可以了。如果键未找到或者类型错误，该值不会发生改变。

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

这样玩 INI 真的好酷啊！然而，如果不能还给我原来的配置文件，有什么卵用？

### 从结构反射

可是，我有说不能吗？

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string    `ini:"places,omitempty"`
	None   []int       `ini:",omitempty"`
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

瞧瞧，奇迹发生了。

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
places = HangZhou,Boston
```

#### 名称映射器（Name Mapper）

为了节省您的时间并简化代码，本库支持类型为 [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) 的名称映射器，该映射器负责结构字段名与分区名和键名之间的映射。

目前有 2 款内置的映射器：

- `AllCapsUnderscore`：该映射器将字段名转换至格式 `ALL_CAPS_UNDERSCORE` 后再去匹配分区名和键名。
- `TitleUnderscore`：该映射器将字段名转换至格式 `title_underscore` 后再去匹配分区名和键名。

使用方法：

```go
type Info struct{
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

使用函数 `ini.ReflectFromWithMapper` 时也可应用相同的规则。

#### 值映射器（Value Mapper）

值映射器允许使用一个自定义函数自动展开值的具体内容，例如：运行时获取环境变量：

```go
type Env struct {
	Foo string `ini:"foo"`
}

func main() {
	cfg, err := ini.Load([]byte("[env]\nfoo = ${MY_VAR}\n")
	cfg.ValueMapper = os.ExpandEnv
	// ...
	env := &Env{}
	err = cfg.Section("env").MapTo(env)
}
```

本例中，`env.Foo` 将会是运行时所获取到环境变量 `MY_VAR` 的值。

#### 映射/反射的其它说明

任何嵌入的结构都会被默认认作一个不同的分区，并且不会自动产生所谓的父子分区关联：

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

很好，但是，我就是要嵌入结构也在同一个分区。好吧，你爹是李刚！

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## 获取帮助

- [API 文档](https://gowalker.org/gopkg.in/ini.v1)
- [创建工单](https://github.com/go-ini/ini/issues/new)

## 常见问题

### 字段 `BlockMode` 是什么？

默认情况下，本库会在您进行读写操作时采用锁机制来确保数据时间。但在某些情况下，您非常确定只进行读操作。此时，您可以通过设置 `cfg.BlockMode = false` 来将读操作提升大约 **50-70%** 的性能。

### 为什么要写另一个 INI 解析库？

许多人都在使用我的 [goconfig](https://github.com/Unknwon/goconfig) 来完成对 INI 文件的操作，但我希望使用更加 Go 风格的代码。并且当您设置 `cfg.BlockMode = false` 时，会有大约 **10-30%** 的性能提升。

为了做出这些改变，我必须对 API 进行破坏，所以新开一个仓库是最安全的做法。除此之外，本库直接使用 `gopkg.in` 来进行版本化发布。（其实真相是导入路径更短了）
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
Provides a `Clock` interface, useful for injecting time dependencies in tests.
[![Gitter chat](http://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/opentracing/public) [![Build Status](https://travis-ci.org/opentracing/opentracing-go.svg?branch=master)](https://travis-ci.org/opentracing/opentracing-go) [![GoDoc](https://godoc.org/github.com/opentracing/opentracing-go?status.svg)](http://godoc.org/github.com/opentracing/opentracing-go)
[![Sourcegraph Badge](https://sourcegraph.com/github.com/opentracing/opentracing-go/-/badge.svg)](https://sourcegraph.com/github.com/opentracing/opentracing-go?badge)

# OpenTracing API for Go

This package is a Go platform API for OpenTracing.

## Required Reading

In order to understand the Go platform API, one must first be familiar with the
[OpenTracing project](http://opentracing.io) and
[terminology](http://opentracing.io/documentation/pages/spec.html) more specifically.

## API overview for those adding instrumentation

Everyday consumers of this `opentracing` package really only need to worry
about a couple of key abstractions: the `StartSpan` function, the `Span`
interface, and binding a `Tracer` at `main()`-time. Here are code snippets
demonstrating some important use cases.

#### Singleton initialization

The simplest starting point is `./default_tracer.go`. As early as possible, call

```go
    import "github.com/opentracing/opentracing-go"
    import ".../some_tracing_impl"

    func main() {
        opentracing.InitGlobalTracer(
            // tracing impl specific:
            some_tracing_impl.New(...),
        )
        ...
    }
```

##### Non-Singleton initialization

If you prefer direct control to singletons, manage ownership of the
`opentracing.Tracer` implementation explicitly.

#### Creating a Span given an existing Go `context.Context`

If you use `context.Context` in your application, OpenTracing's Go library will
happily rely on it for `Span` propagation. To start a new (blocking child)
`Span`, you can use `StartSpanFromContext`.

```go
    func xyz(ctx context.Context, ...) {
        ...
        span, ctx := opentracing.StartSpanFromContext(ctx, "operation_name")
        defer span.Finish()
        span.LogFields(
            log.String("event", "soft error"),
            log.String("type", "cache timeout"),
            log.Int("waited.millis", 1500))
        ...
    }
```

#### Starting an empty trace by creating a "root span"

It's always possible to create a "root" `Span` with no parent or other causal
reference.

```go
    func xyz() {
        ...
        sp := opentracing.StartSpan("operation_name")
        defer sp.Finish()
        ...
    }
```

#### Creating a (child) Span given an existing (parent) Span

```go
    func xyz(parentSpan opentracing.Span, ...) {
        ...
        sp := opentracing.StartSpan(
            "operation_name",
            opentracing.ChildOf(parentSpan.Context()))
        defer sp.Finish()
        ...
    }
```

#### Serializing to the wire

```go
    func makeSomeRequest(ctx context.Context) ... {
        if span := opentracing.SpanFromContext(ctx); span != nil {
            httpClient := &http.Client{}
            httpReq, _ := http.NewRequest("GET", "http://myservice/", nil)

            // Transmit the span's TraceContext as HTTP headers on our
            // outbound request.
            opentracing.GlobalTracer().Inject(
                span.Context(),
                opentracing.HTTPHeaders,
                opentracing.HTTPHeadersCarrier(httpReq.Header))

            resp, err := httpClient.Do(httpReq)
            ...
        }
        ...
    }
```

#### Deserializing from the wire

```go
    http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
        var serverSpan opentracing.Span
        appSpecificOperationName := ...
        wireContext, err := opentracing.GlobalTracer().Extract(
            opentracing.HTTPHeaders,
            opentracing.HTTPHeadersCarrier(req.Header))
        if err != nil {
            // Optionally record something about err here
        }

        // Create the span referring to the RPC client if available.
        // If wireContext == nil, a root span will be created.
        serverSpan = opentracing.StartSpan(
            appSpecificOperationName,
            ext.RPCServerOption(wireContext))

        defer serverSpan.Finish()

        ctx := opentracing.ContextWithSpan(context.Background(), serverSpan)
        ...
    }
```

#### Conditionally capture a field using `log.Noop`

In some situations, you may want to dynamically decide whether or not
to log a field.  For example, you may want to capture additional data,
such as a customer ID, in non-production environments:

```go
    func Customer(order *Order) log.Field {
        if os.Getenv("ENVIRONMENT") == "dev" {
            return log.String("customer", order.Customer.ID)
        }
        return log.Noop()
    }
```

#### Goroutine-safety

The entire public API is goroutine-safe and does not require external
synchronization.

## API pointers for those implementing a tracing system

Tracing system implementors may be able to reuse or copy-paste-modify the `basictracer` package, found [here](https://github.com/opentracing/basictracer-go). In particular, see `basictracer.New(...)`.

## API compatibility

For the time being, "mild" backwards-incompatible changes may be made without changing the major version number. As OpenTracing and `opentracing-go` mature, backwards compatibility will become more of a priority.
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

Please DO NOT file a public issue, instead send your report privately to
security@opencontainers.org.

The maintainers take security seriously. If you discover a security issue,
please bring it to their attention right away!

If you are reporting a security issue, do not create an issue or file a pull
request on GitHub. Instead, disclose the issue responsibly by sending an email
to security@opencontainers.org (which is inhabited only by the maintainers of
the various OCI projects).

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

The [GitHub milestones](https://github.com/opencontainers/image-spec/milestones) lay out the path to the future improvements.

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
# selinux

[![GoDoc](https://godoc.org/github.com/opencontainers/selinux?status.svg)](https://godoc.org/github.com/opencontainers/selinux) [![Go Report Card](https://goreportcard.com/badge/github.com/opencontainers/selinux)](https://goreportcard.com/report/github.com/opencontainers/selinux) [![Build Status](https://travis-ci.org/opencontainers/selinux.svg?branch=master)](https://travis-ci.org/opencontainers/selinux)

Common SELinux package used across the container ecosystem.

Please see the [godoc](https://godoc.org/github.com/opencontainers/selinux) for more information.
# `seed` - Quickly Seed Go's Random Number Generator

Boiler-plate to securely [seed](https://en.wikipedia.org/wiki/Random_seed) Go's
random number generator (if possible).  This library isn't anything fancy, it's
just a canonical way of seeding Go's random number generator. Cribbed from
[`Nomad`](https://github.com/hashicorp/nomad/commit/f89a993ec6b91636a3384dd568898245fbc273a1)
before it was moved into
[`Consul`](https://github.com/hashicorp/consul/commit/d695bcaae6e31ee307c11fdf55bb0bf46ea9fcf4)
and made into a helper function, and now further modularized to be a super
lightweight and reusable library.

Time is better than
[Go's default seed of `1`](https://golang.org/pkg/math/rand/#Seed), but friends
don't let friends use time as a seed to a random number generator.  Use
`seed.MustInit()` instead.

`seed.Init()` is an idempotent and reentrant call that will return an error if
it can't seed the value the first time it is called.  `Init()` is reentrant.

`seed.MustInit()` is idempotent and reentrant call that will `panic()` if it
can't seed the value the first time it is called.  `MustInit()` is reentrant.

## Usage

```
package mypackage

import (
  "github.com/sean-/seed"
)

// MustInit will panic() if it is unable to set a high-entropy random seed:
func init() {
  seed.MustInit()
}

// Or if you want to not panic() and can actually handle this error:
func init() {
  if secure, err := !seed.Init(); !secure {
    // Handle the error
    //panic(fmt.Sprintf("Unable to securely seed Go's RNG: %v", err))
  }
}
```
mux
===
[![GoDoc](https://godoc.org/github.com/gorilla/mux?status.svg)](https://godoc.org/github.com/gorilla/mux)
[![Build Status](https://travis-ci.org/gorilla/mux.svg?branch=master)](https://travis-ci.org/gorilla/mux)

http://www.gorillatoolkit.org/pkg/mux

Package `gorilla/mux` implements a request router and dispatcher.

The name mux stands for "HTTP request multiplexer". Like the standard `http.ServeMux`, `mux.Router` matches incoming requests against a list of registered routes and calls a handler for the route that matches the URL or other conditions. The main features are:

* Requests can be matched based on URL host, path, path prefix, schemes, header and query values, HTTP methods or using custom matchers.
* URL hosts and paths can have variables with an optional regular expression.
* Registered URLs can be built, or "reversed", which helps maintaining references to resources.
* Routes can be used as subrouters: nested routes are only tested if the parent route matches. This is useful to define groups of routes that share common conditions like a host, a path prefix or other repeated attributes. As a bonus, this optimizes request matching.
* It implements the `http.Handler` interface so it is compatible with the standard `http.ServeMux`.

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
vars := mux.Vars(request)
category := vars["category"]
```

And this is all you need to know about the basic usage. More advanced options are explained below.

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
s.HandleFunc("/articles/{category}/{id:[0-9]+}"), ArticleHandler)
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

This also works for host variables:

```go
r := mux.NewRouter()
r.Host("{subdomain}.domain.com").
  Path("/articles/{category}/{id:[0-9]+}").
  HandlerFunc(ArticleHandler).
  Name("article")

// url.String() will be "http://news.domain.com/articles/technology/42"
url, err := r.Get("article").URL("subdomain", "news",
                                 "category", "technology",
                                 "id", "42")
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

## Full Example

Here's a complete, runnable example of a small `mux` based server:

```go
package main

import (
	"net/http"

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
	http.ListenAndServe(":8000", r)
}
```

## License

BSD licensed. See the LICENSE file for details.
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

gorilla/context is a general purpose registry for global request variables.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/sirupsen/logrus.svg?branch=master)](https://travis-ci.org/sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/sirupsen/logrus?status.svg)](https://godoc.org/github.com/sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger.

**Seeing weird case-sensitive problems?** It's in the past been possible to
import Logrus as both upper- and lower-case. Due to the Go package environment,
this caused issues in the community and we needed a standard. Some environments
experienced problems with the upper-case variant, so the lower-case was decided.
Everything using `logrus` will need to use the lower-case:
`github.com/sirupsen/logrus`. Any package that isn't, should be changed.

To fix Glide, see [these
comments](https://github.com/sirupsen/logrus/issues/553#issuecomment-306591437).
For an in-depth explanation of the casing issue, see [this
comment](https://github.com/sirupsen/logrus/issues/570#issuecomment-313933276).

**Are you interested in assisting in maintaining Logrus?** Currently I have a
lot of obligations, and I am unable to provide Logrus with the maintainership it
needs. If you'd like to help, please reach out to me at `simon at author's
username dot com`.

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
  "gopkg.in/gemnasium/logrus-airbrake-hook.v2" // the package is named "airbrake"
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

A list of currently known of service hook can be found in this wiki [page](https://github.com/sirupsen/logrus/wiki/Hooks)


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
  * When colors are enabled, levels are truncated to 4 characters by default. To disable
    truncation set the `DisableLevelTruncation` field to `true`.
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#TextFormatter).
* `logrus.JSONFormatter`. Logs fields as JSON.
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#JSONFormatter).

Third party logging formatters:

* [`FluentdFormatter`](https://github.com/joonix/log). Formats entries that can be parsed by Kubernetes and Google Container Engine.
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
  "github.com/sirupsen/logrus/hooks/test"
  "github.com/stretchr/testify/assert"
  "testing"
)

func TestSomething(t*testing.T){
  logger, hook := test.NewNullLogger()
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

By default, Logger is protected by a mutex for concurrent writes. The mutex is held when calling hooks and writing logs.
If you are sure such locking is not needed, you can call logger.SetNoLock() to disable the locking.

Situation when locking is not needed includes:

* You have no hooks registered, or hooks calling is already thread-safe.

* Writing to logger.Out is already thread-safe, for example:

  1) logger.Out is protected by locks.

  2) logger.Out is a os.File handler opened with `O_APPEND` flag, and every write is smaller than 4k. (This allow multi-thread/multi-process writing)

     (Refer to http://www.notthewizard.com/2014/06/17/are-files-appends-really-atomic/)
Go-check
========

This is a fork of https://github.com/go-check/check

The intention of this fork is not to change any of the original behavior, but add
some specific behaviors needed for some of my projects already using this test suite.
For documentation on the main behavior of go-check see the aforementioned repo.

The original branch is intact at `orig_v1`
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

Please note that the API is considered unstable for now and may change without
further notice.

### License

go.dbus is available under the Simplified BSD License; see LICENSE for the full
text.

Nearly all of the credit for this library goes to github.com/guelfey/go.dbus.
# ttrpc

[![Build Status](https://travis-ci.org/containerd/ttrpc.svg?branch=master)](https://travis-ci.org/containerd/ttrpc)

GRPC for low-memory environments.

The existing grpc-go project requires a lot of memory overhead for importing
packages and at runtime. While this is great for many services with low density
requirements, this can be a problem when running a large number of services on
a single machine or on a machine with a small amount of memory.

Using the same GRPC definitions, this project reduces the binary size and
protocol overhead required. We do this by eliding the `net/http`, `net/http2`
and `grpc` package used by grpc replacing it with a lightweight framing
protocol. The result are smaller binaries that use less resident memory with
the same ease of use as GRPC.

Please note that while this project supports generating either end of the
protocol, the generated service definitions will be incompatible with regular
GRPC services, as they do not speak the same protocol.

# Usage

Create a gogo vanity binary (see
[`cmd/protoc-gen-gogottrpc/main.go`](cmd/protoc-gen-gogottrpc/main.go) for an
example with the ttrpc plugin enabled.

It's recommended to use [`protobuild`](https://github.com//stevvooe/protobuild)
to build the protobufs for this project, but this will work with protoc
directly, if required.

# Differences from GRPC

- The protocol stack has been replaced with a lighter protocol that doesn't
  require http, http2 and tls.
- The client and server interface are identical whereas in GRPC there is a
  client and server interface that are different.
- The Go stdlib context package is used instead.
- No support for streams yet.

# Status

Very new. YMMV.

TODO:

- [X] Plumb error codes and GRPC status
- [X] Remove use of any type and dependency on typeurl package
- [X] Ensure that protocol can support streaming in the future
- [ ] Document protocol layout
- [ ] Add testing under concurrent load to ensure
- [ ] Verify connection error handling
# typeurl

[![Build Status](https://travis-ci.org/containerd/typeurl.svg?branch=master)](https://travis-ci.org/containerd/typeurl)

[![codecov](https://codecov.io/gh/containerd/typeurl/branch/master/graph/badge.svg)](https://codecov.io/gh/containerd/typeurl)

A Go package for managing the registration, marshaling, and unmarshaling of encoded types.

This package helps when types are sent over a GRPC API and marshaled as a [protobuf.Any]().
# console

[![Build Status](https://travis-ci.org/containerd/console.svg?branch=master)](https://travis-ci.org/containerd/console)

Golang package for dealing with consoles.  Light on deps and a simple API.

## Modifying the current process

```go
current := console.Current()
defer current.Reset()

if err := current.SetRaw(); err != nil {
}
ws, err := current.Size()
current.Resize(ws)
```
# cgroups

[![Build Status](https://travis-ci.org/containerd/cgroups.svg?branch=master)](https://travis-ci.org/containerd/cgroups)

[![codecov](https://codecov.io/gh/containerd/cgroups/branch/master/graph/badge.svg)](https://codecov.io/gh/containerd/cgroups)

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
This package is for internal use only. It is intended to only have
temporary changes before they are upstreamed to golang.org/x/sys/
(a.k.a. https://github.com/golang/sys).
# go-runc

[![Build Status](https://travis-ci.org/containerd/go-runc.svg?branch=master)](https://travis-ci.org/containerd/go-runc)


This is a package for consuming the [runc](https://github.com/opencontainers/runc) binary in your Go applications.
It tries to expose all the settings and features of the runc CLI.  If there is something missing then add it, its opensource!

This needs runc @ [a9610f2c0](https://github.com/opencontainers/runc/commit/a9610f2c0237d2636d05a031ec8659a70e75ffeb)
or greater.

## Docs

Docs can be found at [godoc.org](https://godoc.org/github.com/containerd/go-runc).
![banner](https://github.com/containerd/containerd.io/blob/master/static/img/containerd-dark.png?raw=true)

[![GoDoc](https://godoc.org/github.com/containerd/containerd?status.svg)](https://godoc.org/github.com/containerd/containerd)
[![Build Status](https://travis-ci.org/containerd/containerd.svg?branch=master)](https://travis-ci.org/containerd/containerd)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fcontainerd%2Fcontainerd.svg?type=shield)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fcontainerd%2Fcontainerd?ref=badge_shield)
[![Go Report Card](https://goreportcard.com/badge/github.com/containerd/containerd)](https://goreportcard.com/report/github.com/containerd/containerd)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1271/badge)](https://bestpractices.coreinfrastructure.org/projects/1271)

containerd is an industry-standard container runtime with an emphasis on simplicity, robustness and portability. It is available as a daemon for Linux and Windows, which can manage the complete container lifecycle of its host system: image transfer and storage, container execution and supervision, low-level storage and network attachments, etc.

containerd is designed to be embedded into a larger system, rather than being used directly by developers or end-users.

![architecture](design/architecture.png)

## Getting Started

See our documentation on [containerd.io](https://containerd.io):
* [for ops and admins](docs/ops.md)
* [namespaces](docs/namespaces.md)
* [client options](docs/client-opts.md)

See how to build containerd from source at [BUILDING](BUILDING.md).

If you are interested in trying out containerd see our example at [Getting Started](docs/getting-started.md).


## Runtime Requirements

Runtime requirements for containerd are very minimal. Most interactions with
the Linux and Windows container feature sets are handled via [runc](https://github.com/opencontainers/runc) and/or
OS-specific libraries (e.g. [hcsshim](https://github.com/Microsoft/hcsshim) for Microsoft). The current required version of `runc` is always listed in [RUNC.md](/RUNC.md).

There are specific features
used by containerd core code and snapshotters that will require a minimum kernel
version on Linux. With the understood caveat of distro kernel versioning, a
reasonable starting point for Linux is a minimum 4.x kernel version.

The overlay filesystem snapshotter, used by default, uses features that were
finalized in the 4.x kernel series. If you choose to use btrfs, there may
be more flexibility in kernel version (minimum recommended is 3.18), but will
require the btrfs kernel module and btrfs tools to be installed on your Linux
distribution.

To use Linux checkpoint and restore features, you will need `criu` installed on
your system. See more details in [Checkpoint and Restore](#checkpoint-and-restore).

Build requirements for developers are listed in [BUILDING](BUILDING.md).

## Features

### Client

containerd offers a full client package to help you integrate containerd into your platform.

```go

import (
  "github.com/containerd/containerd"
  "github.com/containerd/containerd/cio"
)


func main() {
	client, err := containerd.New("/run/containerd/containerd.sock")
	defer client.Close()
}

```

### Namespaces

Namespaces allow multiple consumers to use the same containerd without conflicting with each other.  It has the benefit of sharing content but still having separation with containers and images.

To set a namespace for requests to the API:

```go
context = context.Background()
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
redis, err := client.NewContainer(context, "redis-master", containerd.WithNewSpec(oci.WithImageConfig(image)))
```

### Root Filesystems

containerd allows you to use overlay or snapshot filesystems with your containers.  It comes with builtin support for overlayfs and btrfs.

```go
// pull an image and unpack it into the configured snapshotter
image, err := client.Pull(context, "docker.io/library/redis:latest", containerd.WithPullUnpack)

// allocate a new RW root filesystem for a container based on the image
redis, err := client.NewContainer(context, "redis-master",
	containerd.WithNewSnapshot("redis-rootfs", image),
	containerd.WithNewSpec(oci.WithImageConfig(image)),
)

// use a readonly filesystem with multiple containers
for i := 0; i < 10; i++ {
	id := fmt.Sprintf("id-%s", i)
	container, err := client.NewContainer(ctx, id,
		containerd.WithNewSnapshotView(id, image),
		containerd.WithNewSpec(oci.WithImageConfig(image)),
	)
}
```

### Tasks

Taking a container object and turning it into a runnable process on a system is done by creating a new `Task` from the container.  A task represents the runnable object within containerd.

```go
// create a new task
task, err := redis.NewTask(context, cio.Stdio)
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
checkpoint, err := task.Checkpoint(context)

err := client.Push(context, "myregistry/checkpoints/redis:master", checkpoint)

// on a new machine pull the checkpoint and restore the redis container
image, err := client.Pull(context, "myregistry/checkpoints/redis:master")

checkpoint := image.Target()

redis, err = client.NewContainer(context, "redis-master", containerd.WithCheckpoint(checkpoint, "redis-rootfs"))
defer container.Delete(context)

task, err = redis.NewTask(context, cio.Stdio, containerd.WithTaskCheckpoint(checkpoint))
defer task.Delete(context)

err := task.Start(context)
```

### Snapshot Plugins

In addition to the built-in Snapshot plugins in containerd, additional external
plugins can be configured using GRPC. An external plugin is made available using
the configured name and appears as a plugin alongside the built-in ones.

To add an external snapshot plugin, add the plugin to containerd's config file
(by default at `/etc/containerd/config.toml`). The string following
`proxy_plugin.` will be used as the name of the snapshotter and the address
should refer to a socket with a GRPC listener serving containerd's Snapshot
GRPC API. Remember to restart containerd for any configuration changes to take
effect.

```
[proxy_plugins]
  [proxy_plugins.customsnapshot]
    type = "snapshot"
    address =  "/var/run/mysnapshotter.sock"
```

See [PLUGINS.md](PLUGINS.md) for how to create plugins

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

__If you are reporting a security issue, please reach out discreetly at security@containerd.io__.

## Licenses

The containerd codebase is released under the [Apache 2.0 license](LICENSE.code).
The README.md file, and files in the "docs" folder are licensed under the
Creative Commons Attribution 4.0 International License. You may obtain a
copy of the license, titled CC-BY-4.0, at http://creativecommons.org/licenses/by/4.0/.
This directory contains the GRPC API definitions for containerd.

All defined services and messages have been aggregated into `*.pb.txt`
descriptors files in this directory. Definitions present here are considered
frozen after the release.

At release time, the current `next.pb.txt` file will be moved into place to
freeze the API changes for the minor version. For example, when 1.0.0 is
released, `next.pb.txt` should be moved to `1.0.txt`. Notice that we leave off
the patch number, since the API will be completely locked down for a given
patch series.

We may find that by default, protobuf descriptors are too noisy to lock down
API changes. In that case, we may filter out certain fields in the descriptors,
possibly regenerating for old versions.

This process is similar to the [process used to ensure backwards compatibility
in Go](https://github.com/golang/go/tree/master/api).
# contrib

The `contrib` directory contains packages that do not belong in the core containerd packages but still contribute to overall containerd usability.

Package such as Apparmor or Selinux are placed in `contrib` because they are platform dependent and often require higher level tools and profiles to work.

Packaging and other built tools can be added to `contrib` to aid in packaging containerd for various distributions.

## Testing

Code in the `contrib` directory may or may not have been tested in the normal test pipeline for core components.
fluent-logger-golang
====

[![Build Status](https://travis-ci.org/fluent/fluent-logger-golang.png?branch=master)](https://travis-ci.org/fluent/fluent-logger-golang)

## A structured event logger for Fluentd (Golang)

## How to install

```
go get github.com/fluent/fluent-logger-golang/fluent
```

## Usage

Install the package with `go get` and use `import` to include it in your project.

```
import "github.com/fluent/fluent-logger-golang/fluent"
```

GoDoc: http://godoc.org/github.com/fluent/fluent-logger-golang/fluent

## Example

```go
package main

import (
  "github.com/fluent/fluent-logger-golang/fluent"
  "fmt"
  "time"
)

func main() {
  logger, err := fluent.New(fluent.Config{})
  if err != nil {
    fmt.Println(err)
  }
  defer logger.Close()
  tag := "myapp.access"
  var data = map[string]string{
    "foo":  "bar",
    "hoge": "hoge",
  }
  error := logger.Post(tag, data)
  // error := logger.PostWithTime(tag, time.Now(), data)
  if error != nil {
    panic(error)
  }
}
```

`data` must be a value like `map[string]literal`, `map[string]interface{}`, `struct` or [`msgp.Marshaler`](http://godoc.org/github.com/tinylib/msgp/msgp#Marshaler). Logger refers tags `msg` or `codec` of each fields of structs.

## Setting config values

```go
f := fluent.New(fluent.Config{FluentPort: 80, FluentHost: "example.com"})
```

### WriteTimeout

Sets the timeout for Write call of logger.Post.
Since the default is zero value, Write will not time out.

## Tests
```
go test
```
go-gelf - GELF Library and Writer for Go
========================================

[GELF] (Graylog Extended Log Format) is an application-level logging
protocol that avoids many of the shortcomings of [syslog]. While it
can be run over any stream or datagram transport protocol, it has
special support ([chunking]) to allow long messages to be split over
multiple datagrams.

Versions
--------

In order to enable versionning of this package with Go, this project
is using GoPkg.in. The default branch of this project will be v1
for some time to prevent breaking clients. We encourage all project
to change their imports to the new GoPkg.in URIs as soon as possible.

To see up to date code, make sure to switch to the master branch.

v1.0.0
------

This implementation currently supports UDP and TCP as a transport
protocol. TLS is unsupported.

The library provides an API that applications can use to log messages
directly to a Graylog server and an `io.Writer` that can be used to
redirect the standard library's log messages (`os.Stdout`) to a
Graylog server.

[GELF]: http://docs.graylog.org/en/2.2/pages/gelf.html
[syslog]: https://tools.ietf.org/html/rfc5424
[chunking]: http://docs.graylog.org/en/2.2/pages/gelf.html#chunked-gelf


Installing
----------

go-gelf is go get-able:

    go get gopkg.in/Graylog2/go-gelf.v1/gelf

    or

    go get github.com/Graylog2/go-gelf/gelf

This will get you version 1.0.0, with only UDP support and legacy API.
Newer versions are available through GoPkg.in:

    go get gopkg.in/Graylog2/go-gelf.v2/gelf

Usage
-----

The easiest way to integrate graylog logging into your go app is by
having your `main` function (or even `init`) call `log.SetOutput()`.
By using an `io.MultiWriter`, we can log to both stdout and graylog -
giving us both centralized and local logs.  (Redundancy is nice).

```golang
package main

import (
  "flag"
  "gopkg.in/Graylog2/go-gelf.v2/gelf"
  "io"
  "log"
  "os"
)

func main() {
  var graylogAddr string

  flag.StringVar(&graylogAddr, "graylog", "", "graylog server addr")
  flag.Parse()

  if graylogAddr != "" {
          // If using UDP
    gelfWriter, err := gelf.NewUDPWriter(graylogAddr)
          // If using TCP
          //gelfWriter, err := gelf.NewTCPWriter(graylogAddr)
    if err != nil {
      log.Fatalf("gelf.NewWriter: %s", err)
    }
    // log to both stderr and graylog2
    log.SetOutput(io.MultiWriter(os.Stderr, gelfWriter))
    log.Printf("logging to stderr & graylog2@'%s'", graylogAddr)
  }

  // From here on out, any calls to log.Print* functions
  // will appear on stdout, and be sent over UDP or TCP to the
  // specified Graylog2 server.

  log.Printf("Hello gray World")

  // ...
}
```
The above program can be invoked as:

    go run test.go -graylog=localhost:12201

When using UDP messages may be dropped or re-ordered. However, Graylog
server availability will not impact application performance; there is
a small, fixed overhead per log call regardless of whether the target
server is reachable or not.


To Do
-----

- WriteMessage example

License
-------

go-gelf is offered under the MIT license, see LICENSE for details.
[![Build Status](https://travis-ci.org/RackSec/srslog.svg?branch=master)](https://travis-ci.org/RackSec/srslog)

# srslog

Go has a `syslog` package in the standard library, but it has the following
shortcomings:

1. It doesn't have TLS support
2. [According to bradfitz on the Go team, it is no longer being maintained.](https://github.com/golang/go/issues/13449#issuecomment-161204716)

I agree that it doesn't need to be in the standard library. So, I've
followed Brad's suggestion and have made a separate project to handle syslog.

This code was taken directly from the Go project as a base to start from.

However, this _does_ have TLS support.

# Usage

Basic usage retains the same interface as the original `syslog` package. We
only added to the interface where required to support new functionality.

Switch from the standard library:

```
import(
    //"log/syslog"
    syslog "github.com/RackSec/srslog"
)
```

You can still use it for local syslog:

```
w, err := syslog.Dial("", "", syslog.LOG_ERR, "testtag")
```

Or to unencrypted UDP:

```
w, err := syslog.Dial("udp", "192.168.0.50:514", syslog.LOG_ERR, "testtag")
```

Or to unencrypted TCP:

```
w, err := syslog.Dial("tcp", "192.168.0.51:514", syslog.LOG_ERR, "testtag")
```

But now you can also send messages via TLS-encrypted TCP:

```
w, err := syslog.DialWithTLSCertPath("tcp+tls", "192.168.0.52:514", syslog.LOG_ERR, "testtag", "/path/to/servercert.pem")
```

And if you need more control over your TLS configuration :

```
pool := x509.NewCertPool()
serverCert, err := ioutil.ReadFile("/path/to/servercert.pem")
if err != nil {
    return nil, err
}
pool.AppendCertsFromPEM(serverCert)
config := tls.Config{
    RootCAs: pool,
}

w, err := DialWithTLSConfig(network, raddr, priority, tag, &config)
```

(Note that in both TLS cases, this uses a self-signed certificate, where the
remote syslog server has the keypair and the client has only the public key.)

And then to write log messages, continue like so:

```
if err != nil {
    log.Fatal("failed to connect to syslog:", err)
}
defer w.Close()

w.Alert("this is an alert")
w.Crit("this is critical")
w.Err("this is an error")
w.Warning("this is a warning")
w.Notice("this is a notice")
w.Info("this is info")
w.Debug("this is debug")
w.Write([]byte("these are some bytes"))
```

# Generating TLS Certificates

We've provided a script that you can use to generate a self-signed keypair:

```
pip install cryptography
python script/gen-certs.py
```

That outputs the public key and private key to standard out. Put those into
`.pem` files. (And don't put them into any source control. The certificate in
the `test` directory is used by the unit tests, and please do not actually use
it anywhere else.)

# Running Tests

Run the tests as usual:

```
go test
```

But we've also provided a test coverage script that will show you which
lines of code are not covered:

```
script/coverage --html
```

That will open a new browser tab showing coverage information.

# License

This project uses the New BSD License, the same as the Go project itself.

# Code of Conduct

Please note that this project is released with a Contributor Code of Conduct.
By participating in this project you agree to abide by its terms.
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
Native Go Zookeeper Client Library
===================================

[![Build Status](https://travis-ci.org/samuel/go-zookeeper.png)](https://travis-ci.org/samuel/go-zookeeper)

Documentation: http://godoc.org/github.com/samuel/go-zookeeper/zk

License
-------

3-clause BSD. See LICENSE file.
golang-lru
==========

This provides the `lru` package which implements a fixed-size
thread safe LRU cache. It is based on the cache in Groupcache.

Documentation
=============

Full docs are available on [Godoc](http://godoc.org/github.com/hashicorp/golang-lru)

Example
=======

Using the LRU is very simple:

```go
l, _ := New(128)
for i := 0; i < 256; i++ {
    l.Add(i, nil)
}
if l.Len() != 128 {
    panic(fmt.Sprintf("bad len: %v", l.Len()))
}
```
go-immutable-radix [![Build Status](https://travis-ci.org/hashicorp/go-immutable-radix.png)](https://travis-ci.org/hashicorp/go-immutable-radix)
=========

Provides the `iradix` package that implements an immutable [radix tree](http://en.wikipedia.org/wiki/Radix_tree).
The package only provides a single `Tree` implementation, optimized for sparse nodes.

As a radix tree, it provides the following:
 * O(k) operations. In many cases, this can be faster than a hash table since
   the hash function is an O(k) operation, and hash tables have very poor cache locality.
 * Minimum / Maximum value lookups
 * Ordered iteration

A tree supports using a transaction to batch multiple updates (insert, delete)
in a more efficient manner than performing each operation one at a time.

For a mutable variant, see [go-radix](https://github.com/armon/go-radix).

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/hashicorp/go-immutable-radix).

Example
=======

Below is a simple example of usage

```go
// Create a tree
r := iradix.New()
r, _, _ = r.Insert([]byte("foo"), 1)
r, _, _ = r.Insert([]byte("bar"), 2)
r, _, _ = r.Insert([]byte("foobar"), 2)

// Find the longest prefix match
m, _, _ := r.Root().LongestPrefix([]byte("foozip"))
if string(m) != "foo" {
    panic("should be foo")
}
```

# Serf

* Website: https://www.serfdom.io
* IRC: `#serfdom` on Freenode
* Mailing list: [Google Groups](https://groups.google.com/group/serfdom/)

Serf is a decentralized solution for service discovery and orchestration
that is lightweight, highly available, and fault tolerant.

Serf runs on Linux, Mac OS X, and Windows. An efficient and lightweight gossip
protocol is used to communicate with other nodes. Serf can detect node failures
and notify the rest of the cluster. An event system is built on top of
Serf, letting you use Serf's gossip protocol to propagate events such
as deploys, configuration changes, etc. Serf is completely masterless
with no single point of failure.

Here are some example use cases of Serf, though there are many others:

* Discovering web servers and automatically adding them to a load balancer
* Organizing many memcached or redis nodes into a cluster, perhaps with
  something like [twemproxy](https://github.com/twitter/twemproxy) or
  maybe just configuring an application with the address of all the
  nodes
* Triggering web deploys using the event system built on top of Serf
* Propagating changes to configuration to relevant nodes.
* Updating DNS records to reflect cluster changes as they occur.
* Much, much more.

## Quick Start

First, [download a pre-built Serf binary](https://www.serfdom.io/downloads.html)
for your operating system or [compile Serf yourself](#developing-serf).

Next, let's start a couple Serf agents. Agents run until they're told to quit
and handle the communication of maintenance tasks of Serf. In a real Serf
setup, each node in your system will run one or more Serf agents (it can
run multiple agents if you're running multiple cluster types. e.g. web
servers vs. memcached servers).

Start each Serf agent in a separate terminal session so that we can see
the output of each. Start the first agent:

```
$ serf agent -node=foo -bind=127.0.0.1:5000 -rpc-addr=127.0.0.1:7373
...
```

Start the second agent in another terminal session (while the first is still
running):

```
$ serf agent -node=bar -bind=127.0.0.1:5001 -rpc-addr=127.0.0.1:7374
...
```

At this point two Serf agents are running independently but are still
unaware of each other. Let's now tell the first agent to join an existing
cluster (the second agent). When starting a Serf agent, you must join an
existing cluster by specifying at least one existing member. After this,
Serf gossips and the remainder of the cluster becomes aware of the join.
Run the following commands in a third terminal session.

```
$ serf join 127.0.0.1:5001
...
```

If you're watching your terminals, you should see both Serf agents
become aware of the join. You can prove it by running `serf members`
to see the members of the Serf cluster:

```
$ serf members
foo    127.0.0.1:5000    alive
bar    127.0.0.1:5001    alive
...
```

At this point, you can ctrl-C or force kill either Serf agent, and they'll
update their membership lists appropriately. If you ctrl-C a Serf agent,
it will gracefully leave by notifying the cluster of its intent to leave.
If you force kill an agent, it will eventually (usually within seconds)
be detected by another member of the cluster which will notify the
cluster of the node failure.

## Documentation

Full, comprehensive documentation is viewable on the Serf website:

https://www.serfdom.io/docs

## Developing Serf

If you wish to work on Serf itself, you'll first need [Go](https://golang.org)
installed (version 1.2+ is _required_). Make sure you have Go properly 
[installed](https://golang.org/doc/install),
including setting up your [GOPATH](https://golang.org/doc/code.html#GOPATH).

Next, clone this repository into `$GOPATH/src/github.com/hashicorp/serf` and
then just type `make`. In a few moments, you'll have a working `serf` executable:

```
$ make
...
$ bin/serf
...
```

*note: `make` will also place a copy of the executable under $GOPATH/bin*

You can run tests by typing `make test`.

If you make any changes to the code, run `make format` in order to automatically
format the code according to Go standards.
# go-memdb

Provides the `memdb` package that implements a simple in-memory database
built on immutable radix trees. The database provides Atomicity, Consistency
and Isolation from ACID. Being that it is in-memory, it does not provide durability.
The database is instantiated with a schema that specifies the tables and indicies
that exist and allows transactions to be executed.

The database provides the following:

* Multi-Version Concurrency Control (MVCC) - By leveraging immutable radix trees
  the database is able to support any number of concurrent readers without locking,
  and allows a writer to make progress.

* Transaction Support - The database allows for rich transactions, in which multiple
  objects are inserted, updated or deleted. The transactions can span multiple tables,
  and are applied atomically. The database provides atomicity and isolation in ACID
  terminology, such that until commit the updates are not visible.

* Rich Indexing - Tables can support any number of indexes, which can be simple like
  a single field index, or more advanced compound field indexes. Certain types like
  UUID can be efficiently compressed from strings into byte indexes for reduces
  storage requirements.

For the underlying immutable radix trees, see [go-immutable-radix](https://github.com/hashicorp/go-immutable-radix).

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/hashicorp/go-memdb).

Example
=======

Below is a simple example of usage

```go
// Create a sample struct
type Person struct {
    Email string
    Name  string
    Age   int
}

// Create the DB schema
schema := &memdb.DBSchema{
    Tables: map[string]*memdb.TableSchema{
        "person": &memdb.TableSchema{
            Name: "person",
            Indexes: map[string]*memdb.IndexSchema{
                "id": &memdb.IndexSchema{
                    Name:    "id",
                    Unique:  true,
                    Indexer: &memdb.StringFieldIndex{Field: "Email"},
                },
            },
        },
    },
}

// Create a new data base
db, err := memdb.NewMemDB(schema)
if err != nil {
    panic(err)
}

// Create a write transaction
txn := db.Txn(true)

// Insert a new person
p := &Person{"joe@aol.com", "Joe", 30}
if err := txn.Insert("person", p); err != nil {
    panic(err)
}

// Commit the transaction
txn.Commit()

// Create read-only transaction
txn = db.Txn(false)
defer txn.Abort()

// Lookup by email
raw, err := txn.First("person", "id", "joe@aol.com")
if err != nil {
    panic(err)
}

// Say hi!
fmt.Printf("Hello %s!", raw.(*Person).Name)

```

# go

Collection of Open-Source Go libraries and tools.

## Codec

[Codec](https://github.com/ugorji/go/tree/master/codec#readme) is a High Performance and Feature-Rich Idiomatic encode/decode and rpc library for [msgpack](http://msgpack.org) and [Binc](https://github.com/ugorji/binc).

Online documentation is at [http://godoc.org/github.com/ugorji/go/codec].

Install using:

    go get github.com/ugorji/go/codec

# Codec

High Performance and Feature-Rich Idiomatic Go Library providing
encode/decode support for different serialization formats.

Supported Serialization formats are:

  - msgpack: [https://github.com/msgpack/msgpack]
  - binc: [http://github.com/ugorji/binc]

To install:

    go get github.com/ugorji/go/codec

Online documentation: [http://godoc.org/github.com/ugorji/go/codec]

The idiomatic Go support is as seen in other encoding packages in
the standard library (ie json, xml, gob, etc).

Rich Feature Set includes:

  - Simple but extremely powerful and feature-rich API
  - Very High Performance.   
    Our extensive benchmarks show us outperforming Gob, Json and Bson by 2-4X.
    This was achieved by taking extreme care on:
      - managing allocation
      - function frame size (important due to Go's use of split stacks),
      - reflection use (and by-passing reflection for common types)
      - recursion implications
      - zero-copy mode (encoding/decoding to byte slice without using temp buffers)
  - Correct.  
    Care was taken to precisely handle corner cases like: 
      overflows, nil maps and slices, nil value in stream, etc.
  - Efficient zero-copying into temporary byte buffers  
    when encoding into or decoding from a byte slice.
  - Standard field renaming via tags
  - Encoding from any value  
    (struct, slice, map, primitives, pointers, interface{}, etc)
  - Decoding into pointer to any non-nil typed value  
    (struct, slice, map, int, float32, bool, string, reflect.Value, etc)
  - Supports extension functions to handle the encode/decode of custom types
  - Support Go 1.2 encoding.BinaryMarshaler/BinaryUnmarshaler
  - Schema-less decoding  
    (decode into a pointer to a nil interface{} as opposed to a typed non-nil value).  
    Includes Options to configure what specific map or slice type to use 
    when decoding an encoded list or map into a nil interface{}
  - Provides a RPC Server and Client Codec for net/rpc communication protocol.
  - Msgpack Specific:
      - Provides extension functions to handle spec-defined extensions (binary, timestamp)
      - Options to resolve ambiguities in handling raw bytes (as string or []byte)  
        during schema-less decoding (decoding into a nil interface{})
      - RPC Server/Client Codec for msgpack-rpc protocol defined at: 
        https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md
  - Fast Paths for some container types:  
    For some container types, we circumvent reflection and its associated overhead
    and allocation costs, and encode/decode directly. These types are:  
	    []interface{}
	    []int
	    []string
	    map[interface{}]interface{}
	    map[int]interface{}
	    map[string]interface{}

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
    )

    mh.MapType = reflect.TypeOf(map[string]interface{}(nil))
    
    // configure extensions
    // e.g. for msgpack, define functions and enable Time support for tag 1
    // mh.AddExt(reflect.TypeOf(time.Time{}), 1, myMsgpackTimeEncodeExtFn, myMsgpackTimeDecodeExtFn)

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

## Representative Benchmark Results

A sample run of benchmark using "go test -bi -bench=. -benchmem":

    /proc/cpuinfo: Intel(R) Core(TM) i7-2630QM CPU @ 2.00GHz (HT)
    
    ..............................................
    BENCHMARK INIT: 2013-10-16 11:02:50.345970786 -0400 EDT
    To run full benchmark comparing encodings (MsgPack, Binc, JSON, GOB, etc), use: "go test -bench=."
    Benchmark: 
    	Struct recursive Depth:             1
    	ApproxDeepSize Of benchmark Struct: 4694 bytes
    Benchmark One-Pass Run:
    	 v-msgpack: len: 1600 bytes
    	      bson: len: 3025 bytes
    	   msgpack: len: 1560 bytes
    	      binc: len: 1187 bytes
    	       gob: len: 1972 bytes
    	      json: len: 2538 bytes
    ..............................................
    PASS
    Benchmark__Msgpack____Encode	   50000	     54359 ns/op	   14953 B/op	      83 allocs/op
    Benchmark__Msgpack____Decode	   10000	    106531 ns/op	   14990 B/op	     410 allocs/op
    Benchmark__Binc_NoSym_Encode	   50000	     53956 ns/op	   14966 B/op	      83 allocs/op
    Benchmark__Binc_NoSym_Decode	   10000	    103751 ns/op	   14529 B/op	     386 allocs/op
    Benchmark__Binc_Sym___Encode	   50000	     65961 ns/op	   17130 B/op	      88 allocs/op
    Benchmark__Binc_Sym___Decode	   10000	    106310 ns/op	   15857 B/op	     287 allocs/op
    Benchmark__Gob________Encode	   10000	    135944 ns/op	   21189 B/op	     237 allocs/op
    Benchmark__Gob________Decode	    5000	    405390 ns/op	   83460 B/op	    1841 allocs/op
    Benchmark__Json_______Encode	   20000	     79412 ns/op	   13874 B/op	     102 allocs/op
    Benchmark__Json_______Decode	   10000	    247979 ns/op	   14202 B/op	     493 allocs/op
    Benchmark__Bson_______Encode	   10000	    121762 ns/op	   27814 B/op	     514 allocs/op
    Benchmark__Bson_______Decode	   10000	    162126 ns/op	   16514 B/op	     789 allocs/op
    Benchmark__VMsgpack___Encode	   50000	     69155 ns/op	   12370 B/op	     344 allocs/op
    Benchmark__VMsgpack___Decode	   10000	    151609 ns/op	   20307 B/op	     571 allocs/op
    ok  	ugorji.net/codec	30.827s

To run full benchmark suite (including against vmsgpack and bson), 
see notes in ext\_dep\_test.go

# memberlist [![GoDoc](https://godoc.org/github.com/hashicorp/memberlist?status.png)](https://godoc.org/github.com/hashicorp/memberlist)

memberlist is a [Go](http://www.golang.org) library that manages cluster
membership and member failure detection using a gossip based protocol.

The use cases for such a library are far-reaching: all distributed systems
require membership, and memberlist is a re-usable solution to managing
cluster membership and node failure detection.

memberlist is eventually consistent but converges quickly on average.
The speed at which it converges can be heavily tuned via various knobs
on the protocol. Node failures are detected and network partitions are partially
tolerated by attempting to communicate to potentially dead nodes through
multiple routes.

## Building

If you wish to build memberlist you'll need Go version 1.2+ installed.

Please check your installation with:

```
go version
```

Run `make deps` to fetch dependencies before building

## Usage

Memberlist is surprisingly simple to use. An example is shown below:

```go
/* Create the initial memberlist from a safe configuration.
   Please reference the godoc for other default config types.
   http://godoc.org/github.com/hashicorp/memberlist#Config
*/
list, err := memberlist.Create(memberlist.DefaultLocalConfig())
if err != nil {
	panic("Failed to create memberlist: " + err.Error())
}

// Join an existing cluster by specifying at least one known member.
n, err := list.Join([]string{"1.2.3.4"})
if err != nil {
	panic("Failed to join cluster: " + err.Error())
}

// Ask for members of the cluster
for _, member := range list.Members() {
	fmt.Printf("Member: %s %s\n", member.Name, member.Addr)
}

// Continue doing whatever you need, memberlist will maintain membership
// information in the background. Delegates can be used for receiving
// events when members join or leave.
```

The most difficult part of memberlist is configuring it since it has many
available knobs in order to tune state propagation delay and convergence times.
Memberlist provides a default configuration that offers a good starting point,
but errs on the side of caution, choosing values that are optimized for
higher convergence at the cost of higher bandwidth usage.

For complete documentation, see the associated [Godoc](http://godoc.org/github.com/hashicorp/memberlist).

## Protocol

memberlist is based on ["SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol"](http://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf). However, we extend the protocol in a number of ways:

* Several extensions are made to increase propagation speed and
convergence rate.
* Another set of extensions, that we call Lifeguard, are made to make memberlist more robust in the presence of slow message processing (due to factors such as CPU starvation, and network delay or loss).

For details on all of these extensions, please read our paper "[Lifeguard : SWIM-ing with Situational Awareness](https://arxiv.org/abs/1707.00788)", along with the memberlist source.  We welcome any questions related
to the protocol on our issue tracker.
# Consul [![Build Status](https://travis-ci.org/hashicorp/consul.png)](https://travis-ci.org/hashicorp/consul)

* Website: http://www.consul.io
* IRC: `#consul` on Freenode
* Mailing list: [Google Groups](https://groups.google.com/group/consul-tool/)

Consul is a tool for service discovery and configuration. Consul is
distributed, highly available, and extremely scalable.

Consul provides several key features:

* **Service Discovery** - Consul makes it simple for services to register
  themselves and to discover other services via a DNS or HTTP interface.
  External services such as SaaS providers can be registered as well.

* **Health Checking** - Health Checking enables Consul to quickly alert
  operators about any issues in a cluster. The integration with service
  discovery prevents routing traffic to unhealthy hosts and enables service
  level circuit breakers.

* **Key/Value Storage** - A flexible key/value store enables storing
  dynamic configuration, feature flagging, coordination, leader election and
  more. The simple HTTP API makes it easy to use anywhere.

* **Multi-Datacenter** - Consul is built to be datacenter aware, and can
  support any number of regions without complex configuration.

Consul runs on Linux, Mac OS X, and Windows. It is recommended to run the
Consul servers only on Linux, however.

## Quick Start

An extensive quick quick start is viewable on the Consul website:

http://www.consul.io/intro/getting-started/install.html

## Documentation

Full, comprehensive documentation is viewable on the Consul website:

http://www.consul.io/docs

## Developing Consul

If you wish to work on Consul itself, you'll first need [Go](https://golang.org)
installed (version 1.4+ is _required_). Make sure you have Go properly installed,
including setting up your [GOPATH](https://golang.org/doc/code.html#GOPATH).

Next, clone this repository into `$GOPATH/src/github.com/hashicorp/consul` and
then just type `make`. In a few moments, you'll have a working `consul` executable:

```
$ go get -u ./...
$ make
...
$ bin/consul
...
```

*note: `make` will also place a copy of the binary in the first part of your $GOPATH*

You can run tests by typing `make test`.

If you make any changes to the code, run `make format` in order to automatically
format the code according to Go standards.

### Building Consul on Windows

Make sure Go 1.4+ is installed on your system and that the Go command is in your
%PATH%.

For building Consul on Windows, you also need to have MinGW installed.
[TDM-GCC](http://tdm-gcc.tdragon.net/) is a simple bundle installer which has all
the required tools for building Consul with MinGW.

Install TDM-GCC and make sure it has been added to your %PATH%.

If all goes well, you should be able to build Consul by running `make.bat` from a
command prompt.

See also [golang/winstrap](https://github.com/golang/winstrap) and
[golang/wiki/WindowsBuild](https://github.com/golang/go/wiki/WindowsBuild)
for more information of how to set up a general Go build environment on Windows
with MinGW.

Consul API client
=================

This package provides the `api` package which attempts to
provide programmatic access to the full Consul API.

Currently, all of the Consul APIs included in version 0.3 are supported.

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/hashicorp/consul/api)

Usage
=====

Below is an example of using the Consul client:

```go
// Get a new client, with KV endpoints
client, _ := api.NewClient(api.DefaultConfig())
kv := client.KV()

// PUT a new KV pair
p := &api.KVPair{Key: "foo", Value: []byte("test")}
_, err := kv.Put(p, nil)
if err != nil {
    panic(err)
}

// Lookup the pair
pair, _, err := kv.Get("foo", nil)
if err != nil {
    panic(err)
}
fmt.Printf("KV: %v", pair)

```

# go-multierror

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
# go-sockaddr

## `sockaddr` Library

Socket address convenience functions for Go.  `go-sockaddr` is a convenience
library that makes doing the right thing with IP addresses easy.  `go-sockaddr`
is loosely modeled after the UNIX `sockaddr_t` and creates a union of the family
of `sockaddr_t` types (see below for an ascii diagram).  Library documentation
is available
at
[https://godoc.org/github.com/hashicorp/go-sockaddr](https://godoc.org/github.com/hashicorp/go-sockaddr).
The primary intent of the library was to make it possible to define heuristics
for selecting the correct IP addresses when a configuration is evaluated at
runtime.  See
the
[docs](https://godoc.org/github.com/hashicorp/go-sockaddr),
[`template` package](https://godoc.org/github.com/hashicorp/go-sockaddr/template),
tests,
and
[CLI utility](https://github.com/hashicorp/go-sockaddr/tree/master/cmd/sockaddr)
for details and hints as to how to use this library.

For example, with this library it is possible to find an IP address that:

* is attached to a default route
  ([`GetDefaultInterfaces()`](https://godoc.org/github.com/hashicorp/go-sockaddr#GetDefaultInterfaces))
* is contained within a CIDR block ([`IfByNetwork()`](https://godoc.org/github.com/hashicorp/go-sockaddr#IfByNetwork))
* is an RFC1918 address
  ([`IfByRFC("1918")`](https://godoc.org/github.com/hashicorp/go-sockaddr#IfByRFC))
* is ordered
  ([`OrderedIfAddrBy(args)`](https://godoc.org/github.com/hashicorp/go-sockaddr#OrderedIfAddrBy) where
  `args` includes, but is not limited
  to,
  [`AscIfType`](https://godoc.org/github.com/hashicorp/go-sockaddr#AscIfType),
  [`AscNetworkSize`](https://godoc.org/github.com/hashicorp/go-sockaddr#AscNetworkSize))
* excludes all IPv6 addresses
  ([`IfByType("^(IPv4)$")`](https://godoc.org/github.com/hashicorp/go-sockaddr#IfByType))
* is larger than a `/32`
  ([`IfByMaskSize(32)`](https://godoc.org/github.com/hashicorp/go-sockaddr#IfByMaskSize))
* is not on a `down` interface
  ([`ExcludeIfs("flags", "down")`](https://godoc.org/github.com/hashicorp/go-sockaddr#ExcludeIfs))
* preferences an IPv6 address over an IPv4 address
  ([`SortIfByType()`](https://godoc.org/github.com/hashicorp/go-sockaddr#SortIfByType) +
  [`ReverseIfAddrs()`](https://godoc.org/github.com/hashicorp/go-sockaddr#ReverseIfAddrs)); and
* excludes any IP in RFC6890 address
  ([`IfByRFC("6890")`](https://godoc.org/github.com/hashicorp/go-sockaddr#IfByRFC))

Or any combination or variation therein.

There are also a few simple helper functions such as `GetPublicIP` and
`GetPrivateIP` which both return strings and select the first public or private
IP address on the default interface, respectively.  Similarly, there is also a
helper function called `GetInterfaceIP` which returns the first usable IP
address on the named interface.

## `sockaddr` CLI

Given the possible complexity of the `sockaddr` library, there is a CLI utility
that accompanies the library, also
called
[`sockaddr`](https://github.com/hashicorp/go-sockaddr/tree/master/cmd/sockaddr).
The
[`sockaddr`](https://github.com/hashicorp/go-sockaddr/tree/master/cmd/sockaddr)
utility exposes nearly all of the functionality of the library and can be used
either as an administrative tool or testing tool.  To install
the
[`sockaddr`](https://github.com/hashicorp/go-sockaddr/tree/master/cmd/sockaddr),
run:

```text
$ go get -u github.com/hashicorp/go-sockaddr/cmd/sockaddr
```

If you're familiar with UNIX's `sockaddr` struct's, the following diagram
mapping the C `sockaddr` (top) to `go-sockaddr` structs (bottom) and
interfaces will be helpful:

```
+-------------------------------------------------------+
|                                                       |
|                        sockaddr                       |
|                        SockAddr                       |
|                                                       |
| +--------------+ +----------------------------------+ |
| | sockaddr_un  | |                                  | |
| | SockAddrUnix | |           sockaddr_in{,6}        | |
| +--------------+ |                IPAddr            | |
|                  |                                  | |
|                  | +-------------+ +--------------+ | |
|                  | | sockaddr_in | | sockaddr_in6 | | |
|                  | |   IPv4Addr  | |   IPv6Addr   | | |
|                  | +-------------+ +--------------+ | |
|                  |                                  | |
|                  +----------------------------------+ |
|                                                       |
+-------------------------------------------------------+
```

## Inspiration and Design

There were many subtle inspirations that led to this design, but the most direct
inspiration for the filtering syntax was
OpenBSD's
[`pf.conf(5)`](https://www.freebsd.org/cgi/man.cgi?query=pf.conf&apropos=0&sektion=0&arch=default&format=html#PARAMETERS) firewall
syntax that lets you select the first IP address on a given named interface.
The original problem stemmed from:

* needing to create immutable images using [Packer](https://www.packer.io) that
  ran the [Consul](https://www.consul.io) process (Consul can only use one IP
  address at a time);
* images that may or may not have multiple interfaces or IP addresses at
  runtime; and
* we didn't want to rely on configuration management to render out the correct
  IP address if the VM image was being used in an auto-scaling group.

Instead we needed some way to codify a heuristic that would correctly select the
right IP address but the input parameters were not known when the image was
created.
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
    "net"
    "runtime"
    "github.com/vishvananada/netns"
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
    defer newns.Close()

    // Do something with tne network namespace
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
# libnetwork - networking for containers

[![Circle CI](https://circleci.com/gh/docker/libnetwork/tree/master.svg?style=svg)](https://circleci.com/gh/docker/libnetwork/tree/master) [![Coverage Status](https://coveralls.io/repos/docker/libnetwork/badge.svg)](https://coveralls.io/r/docker/libnetwork) [![GoDoc](https://godoc.org/github.com/docker/libnetwork?status.svg)](https://godoc.org/github.com/docker/libnetwork) [![Go Report Card](https://goreportcard.com/badge/github.com/docker/libnetwork)](https://goreportcard.com/report/github.com/docker/libnetwork)

Libnetwork provides a native Go implementation for connecting containers

The goal of libnetwork is to deliver a robust Container Network Model that provides a consistent programming interface and the required network abstractions for applications.

#### Design
Please refer to the [design](docs/design.md) for more information.

#### Using libnetwork

There are many networking solutions available to suit a broad range of use-cases. libnetwork uses a driver / plugin model to support all of these solutions while abstracting the complexity of the driver implementations by exposing a simple and consistent Network Model to users.


```go
import (
	"fmt"
	"log"

	"github.com/docker/docker/pkg/reexec"
	"github.com/docker/libnetwork"
	"github.com/docker/libnetwork/config"
	"github.com/docker/libnetwork/netlabel"
	"github.com/docker/libnetwork/options"
)

func main() {
	if reexec.Init() {
		return
	}

	// Select and configure the network driver
	networkType := "bridge"

	// Create a new controller instance
	driverOptions := options.Generic{}
	genericOption := make(map[string]interface{})
	genericOption[netlabel.GenericData] = driverOptions
	controller, err := libnetwork.New(config.OptionDriverConfig(networkType, genericOption))
	if err != nil {
		log.Fatalf("libnetwork.New: %s", err)
	}

	// Create a network for containers to join.
	// NewNetwork accepts Variadic optional arguments that libnetwork and Drivers can use.
	network, err := controller.NewNetwork(networkType, "network1", "")
	if err != nil {
		log.Fatalf("controller.NewNetwork: %s", err)
	}

	// For each new container: allocate IP and interfaces. The returned network
	// settings will be used for container infos (inspect and such), as well as
	// iptables rules for port publishing. This info is contained or accessible
	// from the returned endpoint.
	ep, err := network.CreateEndpoint("Endpoint1")
	if err != nil {
		log.Fatalf("network.CreateEndpoint: %s", err)
	}

	// Create the sandbox for the container.
	// NewSandbox accepts Variadic optional arguments which libnetwork can use.
	sbx, err := controller.NewSandbox("container1",
		libnetwork.OptionHostname("test"),
		libnetwork.OptionDomainname("docker.io"))
	if err != nil {
		log.Fatalf("controller.NewSandbox: %s", err)
	}

	// A sandbox can join the endpoint via the join api.
	err = ep.Join(sbx)
	if err != nil {
		log.Fatalf("ep.Join: %s", err)
	}

	// libnetwork client can check the endpoint's operational data via the Info() API
	epInfo, err := ep.DriverInfo()
	if err != nil {
		log.Fatalf("ep.DriverInfo: %s", err)
	}

	macAddress, ok := epInfo[netlabel.MacAddress]
	if !ok {
		log.Fatalf("failed to get mac address from endpoint info")
	}

	fmt.Printf("Joined endpoint %s (%s) to sandbox %s (%s)\n", ep.Name(), macAddress, sbx.ContainerID(), sbx.Key())
}
```

## Future
Please refer to [roadmap](ROADMAP.md) for more information.

## Contributing

Want to hack on libnetwork? [Docker's contributions guidelines](https://github.com/docker/docker/blob/master/CONTRIBUTING.md) apply.

## Copyright and license
Code and documentation copyright 2015 Docker, inc. Code released under the Apache 2.0 license. Docs released under Creative commons.
Package resolvconf provides utility code to query and update DNS configuration in /etc/resolv.conf
# libkv

[![GoDoc](https://godoc.org/github.com/docker/libkv?status.png)](https://godoc.org/github.com/docker/libkv)
[![Build Status](https://travis-ci.org/docker/libkv.svg?branch=master)](https://travis-ci.org/docker/libkv)
[![Coverage Status](https://coveralls.io/repos/docker/libkv/badge.svg)](https://coveralls.io/r/docker/libkv)
[![Go Report Card](https://goreportcard.com/badge/github.com/docker/libkv)](https://goreportcard.com/report/github.com/docker/libkv)

`libkv` provides a `Go` native library to store metadata.

The goal of `libkv` is to abstract common store operations for multiple distributed and/or local Key/Value store backends.

For example, you can use it to store your metadata or for service discovery to register machines and endpoints inside your cluster.

You can also easily implement a generic *Leader Election* on top of it (see the [docker/leadership](https://github.com/docker/leadership) repository).

As of now, `libkv` offers support for `Consul`, `Etcd`, `Zookeeper` (**Distributed** store) and `BoltDB` (**Local** store).

## Usage

`libkv` is meant to be used as an abstraction layer over existing distributed Key/Value stores. It is especially useful if you plan to support `consul`, `etcd` and `zookeeper` using the same codebase.

It is ideal if you plan for something written in Go that should support:

- A simple metadata storage, distributed or local
- A lightweight discovery service for your nodes
- A distributed lock mechanism

You can find examples of usage for `libkv` under in `docs/examples.go`. Optionally you can also take a look at the `docker/swarm` or `docker/libnetwork` repositories which are using `docker/libkv` for all the use cases listed above.

## Supported versions

`libkv` supports:
- Consul versions >= `0.5.1` because it uses Sessions with `Delete` behavior for the use of `TTLs` (mimics zookeeper's Ephemeral node support), If you don't plan to use `TTLs`: you can use Consul version `0.4.0+`.
- Etcd versions >= `2.0` because it uses the new `coreos/etcd/client`, this might change in the future as the support for `APIv3` comes along and adds more capabilities.
- Zookeeper versions >= `3.4.5`. Although this might work with previous version but this remains untested as of now.
- Boltdb, which shouldn't be subject to any version dependencies.

## Interface

A **storage backend** in `libkv` should implement (fully or partially) this interface:

```go
type Store interface {
	Put(key string, value []byte, options *WriteOptions) error
	Get(key string) (*KVPair, error)
	Delete(key string) error
	Exists(key string) (bool, error)
	Watch(key string, stopCh <-chan struct{}) (<-chan *KVPair, error)
	WatchTree(directory string, stopCh <-chan struct{}) (<-chan []*KVPair, error)
	NewLock(key string, options *LockOptions) (Locker, error)
	List(directory string) ([]*KVPair, error)
	DeleteTree(directory string) error
	AtomicPut(key string, value []byte, previous *KVPair, options *WriteOptions) (bool, *KVPair, error)
	AtomicDelete(key string, previous *KVPair) (bool, error)
	Close()
}
```

## Compatibility matrix

Backend drivers in `libkv` are generally divided between **local drivers** and **distributed drivers**. Distributed backends offer enhanced capabilities like `Watches` and/or distributed `Locks`.

Local drivers are usually used in complement to the distributed drivers to store informations that only needs to be available locally.

| Calls                 |   Consul   |  Etcd  |  Zookeeper  |  BoltDB  |
|-----------------------|:----------:|:------:|:-----------:|:--------:|
| Put                   |     X      |   X    |      X      |    X     |
| Get                   |     X      |   X    |      X      |    X     |
| Delete                |     X      |   X    |      X      |    X     |
| Exists                |     X      |   X    |      X      |    X     |
| Watch                 |     X      |   X    |      X      |          |
| WatchTree             |     X      |   X    |      X      |          |
| NewLock (Lock/Unlock) |     X      |   X    |      X      |          |
| List                  |     X      |   X    |      X      |    X     |
| DeleteTree            |     X      |   X    |      X      |    X     |
| AtomicPut             |     X      |   X    |      X      |    X     |
| Close                 |     X      |   X    |      X      |    X     |

## Limitations

Distributed Key/Value stores often have different concepts for managing and formatting keys and their associated values. Even though `libkv` tries to abstract those stores aiming for some consistency, in some cases it can't be applied easily.

Please refer to the `docs/compatibility.md` to see what are the special cases for cross-backend compatibility.

Other than those special cases, you should expect the same experience for basic operations like `Get`/`Put`, etc.

Calls like `WatchTree` may return different events (or number of events) depending on the backend (for now, `Etcd` and `Consul` will likely return more events than `Zookeeper` that you should triage properly). Although you should be able to use it successfully to watch on events in an interchangeable way (see the **docker/leadership** repository or the **pkg/discovery/kv** package in **docker/docker**).

## TLS

Only `Consul` and `etcd` have support for TLS and you should build and provide your own `config.TLS` object to feed the client. Support is planned for `zookeeper`.

## Roadmap

- Make the API nicer to use (using `options`)
- Provide more options (`consistency` for example)
- Improve performance (remove extras `Get`/`List` operations)
- Better key formatting
- New backends?

## Contributing

Want to hack on libkv? [Docker's contributions guidelines](https://github.com/docker/docker/blob/master/CONTRIBUTING.md) apply.

## Copyright and license

Copyright © 2014-2016 Docker, Inc. All rights reserved, except as follows. Code is released under the Apache 2.0 license. The README.md file, and files in the "docs" folder are licensed under the Creative Commons Attribution 4.0 International License under the terms and conditions set forth in the file "LICENSE.docs". You may obtain a duplicate copy of the same license, titled CC-BY-SA-4.0, at http://creativecommons.org/licenses/by/4.0/.
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

# go-metrics [![GoDoc](https://godoc.org/github.com/docker/go-metrics?status.svg)](https://godoc.org/github.com/docker/go-metrics) ![Badge Badge](http://doyouevenbadge.com/github.com/docker/go-metrics)

This package is small wrapper around the prometheus go client to help enforce convention and best practices for metrics collection in Docker projects.

## Best Practices

This packages is meant to be used for collecting metrics in Docker projects.
It is not meant to be used as a replacement for the prometheus client but to help enforce consistent naming across metrics collected.
If you have not already read the prometheus best practices around naming and labels you can read the page [here](https://prometheus.io/docs/practices/naming/).

The following are a few Docker specific rules that will help you name and work with metrics in your project.

1. Namespace and Subsystem

This package provides you with a namespace type that allows you to specify the same namespace and subsystem for your metrics.

```go
ns := metrics.NewNamespace("engine", "daemon", metrics.Labels{
        "version": dockerversion.Version,
        "commit":  dockerversion.GitCommit,
})
```

In the example above we are creating metrics for the Docker engine's daemon package.
`engine` would be the namespace in this example where `daemon` is the subsystem or package where we are collecting the metrics.

A namespace also allows you to attach constant labels to the metrics such as the git commit and version that it is collecting.

2. Declaring your Metrics

Try to keep all your metric declarations in one file.
This makes it easy for others to see what constant labels are defined on the namespace and what labels are defined on the metrics when they are created.

3. Use labels instead of multiple metrics

Labels allow you to define one metric such as the time it takes to perform a certain action on an object.
If we wanted to collect timings on various container actions such as create, start, and delete then we can define one metric called `container_actions` and use labels to specify the type of action.


```go
containerActions = ns.NewLabeledTimer("container_actions", "The number of milliseconds it takes to process each container action", "action")
```

The last parameter is the label name or key.
When adding a data point to the metric you will use the `WithValues` function to specify the `action` that you are collecting for.

```go
containerActions.WithValues("create").UpdateSince(start)
```

4. Always use a unit

The metric name should describe what you are measuring but you also need to provide the unit that it is being measured with.
For a timer, the standard unit is seconds and a counter's standard unit is a total.
For gauges you must provide the unit.
This package provides a standard set of units for use within the Docker projects.

```go
Nanoseconds Unit = "nanoseconds"
Seconds     Unit = "seconds"
Bytes       Unit = "bytes"
Total       Unit = "total"
```

If you need to use a unit but it is not defined in the package please open a PR to add it but first try to see if one of the already created units will work for your metric, i.e. seconds or nanoseconds vs adding milliseconds.

## Docs

Package documentation can be found [here](https://godoc.org/github.com/docker/go-metrics).

## Additional Metrics

Additional metrics are also defined here that are not avaliable in the prometheus client.
If you need a custom metrics and it is generic enough to be used by multiple projects, define it here.


## Copyright and license

Copyright © 2016 Docker, Inc. All rights reserved, except as follows. Code is released under the Apache 2.0 license. The README.md file, and files in the "docs" folder are licensed under the Creative Commons Attribution 4.0 International License under the terms and conditions set forth in the file "LICENSE.docs". You may obtain a duplicate copy of the same license, titled CC-BY-SA-4.0, at http://creativecommons.org/licenses/by/4.0/.
# [SwarmKit](https://github.com/docker/swarmkit)

[![GoDoc](https://godoc.org/github.com/docker/swarmkit?status.svg)](https://godoc.org/github.com/docker/swarmkit)
[![Circle CI](https://circleci.com/gh/docker/swarmkit.svg?style=shield&circle-token=a7bf494e28963703a59de71cf19b73ad546058a7)](https://circleci.com/gh/docker/swarmkit)
[![codecov.io](https://codecov.io/github/docker/swarmkit/coverage.svg?branch=master&token=LqD1dzTjsN)](https://codecov.io/github/docker/swarmkit?branch=master)
[![Badge Badge](http://doyouevenbadge.com/github.com/docker/swarmkit)](http://doyouevenbadge.com/report/github.com/docker/swarmkit)

*SwarmKit* is a toolkit for orchestrating distributed systems at any scale. It includes primitives for node discovery, raft-based consensus, task scheduling and more.

Its main benefits are:

-   **Distributed**: *SwarmKit* uses the [Raft Consensus Algorithm](https://raft.github.io/) in order to coordinate and does not rely on a single point of failure to perform decisions.
-   **Secure**: Node communication and membership within a *Swarm* are secure out of the box. *SwarmKit* uses mutual TLS for node *authentication*, *role authorization* and *transport encryption*, automating both certificate issuance and rotation.
-   **Simple**: *SwarmKit* is operationally simple and minimizes infrastructure dependencies. It does not need an external database to operate.

## Overview

Machines running *SwarmKit* can be grouped together in order to form a *Swarm*, coordinating tasks with each other.
Once a machine joins, it becomes a *Swarm Node*. Nodes can either be *worker* nodes or *manager* nodes.

-   **Worker Nodes** are responsible for running Tasks using an *Executor*. *SwarmKit* comes with a default *Docker Container Executor* that can be easily swapped out.
-   **Manager Nodes** on the other hand accept specifications from the user and are responsible for reconciling the desired state with the actual cluster state.

An operator can dynamically update a Node's role by promoting a Worker to Manager or demoting a Manager to Worker.

*Tasks* are organized in *Services*. A service is a higher level abstraction that allows the user to declare the desired state of a group of tasks.
Services define what type of task should be created as well as how to execute them (e.g. run this many replicas at all times) and how to update them (e.g. rolling updates).

## Features

Some of *SwarmKit*'s main features are:

-   **Orchestration**

    -   **Desired State Reconciliation**: *SwarmKit* constantly compares the desired state against the current cluster state and reconciles the two if necessary. For instance, if a node fails, *SwarmKit* reschedules its tasks onto a different node.

    -   **Service Types**: There are different types of services. The project currently ships with two of them out of the box

        -   **Replicated Services** are scaled to the desired number of replicas.
        -   **Global Services** run one task on every available node in the cluster.

    -   **Configurable Updates**: At any time, you can change the value of one or more fields for a service. After you make the update, *SwarmKit* reconciles the desired state by ensuring all tasks are using the desired settings. By default, it performs a lockstep update - that is, update all tasks at the same time. This can be configured through different knobs:

        -   **Parallelism** defines how many updates can be performed at the same time.
        -   **Delay** sets the minimum delay between updates. *SwarmKit* will start by shutting down the previous task, bring up a new one, wait for it to transition to the *RUNNING* state *then* wait for the additional configured delay. Finally, it will move onto other tasks.

    -   **Restart Policies**: The orchestration layer monitors tasks and reacts to failures based on the specified policy. The operator can define restart conditions, delays and limits (maximum number of attempts in a given time window). *SwarmKit* can decide to restart a task on a different machine. This means that faulty nodes will gradually be drained of their tasks.

-   **Scheduling**

    -   **Resource Awareness**: *SwarmKit* is aware of resources available on nodes and will place tasks accordingly.
    -   **Constraints**: Operators can limit the set of nodes where a task can be scheduled by defining constraint expressions. Multiple constraints find nodes that satisfy every expression, i.e., an `AND` match. Constraints can match node attributes in the following table. Note that `engine.labels` are collected from Docker Engine with information like operating system, drivers, etc. `node.labels` are added by cluster administrators for operational purpose. For example, some nodes have security compliant labels to run tasks with compliant requirements.

        | node attribute | matches | example |
        |:------------- |:-------------| :-------------|
        | node.id | node's ID | `node.id == 2ivku8v2gvtg4`|
        | node.hostname | node's hostname | `node.hostname != node-2`|
        | node.ip | node's IP address | `node.ip != 172.19.17.0/24`|
        | node.role |  node's manager or worker role | `node.role == manager`|
        | node.platform.os |  node's operating system | `node.platform.os == linux`|
        | node.platform.arch |  node's architecture | `node.platform.arch == x86_64`|
        | node.labels | node's labels added by cluster admins | `node.labels.security == high`|
        | engine.labels | Docker Engine's labels | `engine.labels.operatingsystem == ubuntu 14.04`|

    -   **Strategies**: The project currently ships with a *spread strategy* which will attempt to schedule tasks on the least loaded
    nodes, provided they meet the constraints and resource requirements.

-   **Cluster Management**

    -   **State Store**: Manager nodes maintain a strongly consistent, replicated (Raft based) and extremely fast (in-memory reads) view of the cluster which allows them to make quick scheduling decisions while tolerating failures.
    -   **Topology Management**: Node roles (*Worker* / *Manager*) can be dynamically changed through API/CLI calls.
    -   **Node Management**: An operator can alter the desired availability of a node: Setting it to *Paused* will prevent any further tasks from being scheduled to it while *Drained* will have the same effect while also re-scheduling its tasks somewhere else (mostly for maintenance scenarios).

-   **Security**

    -   **Mutual TLS**: All nodes communicate with each other using mutual *TLS*. Swarm managers act as a *Root Certificate Authority*, issuing certificates to new nodes.
    -   **Token-based Join**: All nodes require a cryptographic token to join the swarm, which defines that node's role. Tokens can be rotated as often as desired without affecting already-joined nodes.
    -   **Certificate Rotation**: TLS Certificates are rotated and reloaded transparently on every node, allowing a user to set how frequently rotation should happen (the current default is 3 months, the minimum is 30 minutes).

## Build

Requirements:

-   Go 1.6 or higher
-   A [working golang](https://golang.org/doc/code.html) environment
-   [Protobuf 3.x or higher](https://developers.google.com/protocol-buffers/docs/downloads) to regenerate protocol buffer files (e.g. using `make generate`)

*SwarmKit* is built in Go and leverages a standard project structure to work well with Go tooling.
If you are new to Go, please see [BUILDING.md](BUILDING.md) for a more detailed guide.

Once you have *SwarmKit* checked out in your `$GOPATH`, the `Makefile` can be used for common tasks.

From the project root directory, run the following to build `swarmd` and `swarmctl`:

```sh
$ make binaries
```

## Test

Before running tests for the first time, setup the tooling:

```sh
$ make setup
```

Then run:

```sh
$ make all
```

## Usage Examples

### Setting up a Swarm

These instructions assume that `swarmd` and `swarmctl` are in your PATH.

(Before starting, make sure `/tmp/node-N` don't exist)

Initialize the first node:

```sh
$ swarmd -d /tmp/node-1 --listen-control-api /tmp/node-1/swarm.sock --hostname node-1
```

Before joining cluster, the token should be fetched:

```  
$ export SWARM_SOCKET=/tmp/node-1/swarm.sock  
$ swarmctl cluster inspect default  
ID          : 87d2ecpg12dfonxp3g562fru1
Name        : default
Orchestration settings:
  Task history entries: 5
Dispatcher settings:
  Dispatcher heartbeat period: 5s
Certificate Authority settings:
  Certificate Validity Duration: 2160h0m0s
  Join Tokens:
    Worker: SWMTKN-1-3vi7ajem0jed8guusgvyl98nfg18ibg4pclify6wzac6ucrhg3-0117z3s2ytr6egmmnlr6gd37n
    Manager: SWMTKN-1-3vi7ajem0jed8guusgvyl98nfg18ibg4pclify6wzac6ucrhg3-d1ohk84br3ph0njyexw0wdagx
```

In two additional terminals, join two nodes. From the example below, replace `127.0.0.1:4242`
with the address of the first node, and use the `<Worker Token>` acquired above.
In this example, the `<Worker Token>` is `SWMTKN-1-3vi7ajem0jed8guusgvyl98nfg18ibg4pclify6wzac6ucrhg3-0117z3s2ytr6egmmnlr6gd37n`.
If the joining nodes run on the same host as `node-1`, select a different remote
listening port, e.g., `--listen-remote-api 127.0.0.1:4343`.

```sh
$ swarmd -d /tmp/node-2 --hostname node-2 --join-addr 127.0.0.1:4242 --join-token <Worker Token>
$ swarmd -d /tmp/node-3 --hostname node-3 --join-addr 127.0.0.1:4242 --join-token <Worker Token>
```

If joining as a manager, also specify the listen-control-api.

```sh
$ swarmd -d /tmp/node-4 --hostname node-4 --join-addr 127.0.0.1:4242 --join-token <Manager Token> --listen-control-api /tmp/node-4/swarm.sock --listen-remote-api 127.0.0.1:4245
```

In a fourth terminal, use `swarmctl` to explore and control the cluster. Before
running `swarmctl`, set the `SWARM_SOCKET` environment variable to the path of the
manager socket that was specified in `--listen-control-api` when starting the
manager.

To list nodes:

```
$ export SWARM_SOCKET=/tmp/node-1/swarm.sock
$ swarmctl node ls
ID                         Name    Membership  Status  Availability  Manager Status
--                         ----    ----------  ------  ------------  --------------
3x12fpoi36eujbdkgdnbvbi6r  node-2  ACCEPTED    READY   ACTIVE
4spl3tyipofoa2iwqgabsdcve  node-1  ACCEPTED    READY   ACTIVE        REACHABLE *
dknwk1uqxhnyyujq66ho0h54t  node-3  ACCEPTED    READY   ACTIVE
zw3rwfawdasdewfq66ho34eaw  node-4  ACCEPTED    READY   ACTIVE        REACHABLE


```

### Creating Services

Start a *redis* service:

```
$ swarmctl service create --name redis --image redis:3.0.5
08ecg7vc7cbf9k57qs722n2le
```

List the running services:

```
$ swarmctl service ls
ID                         Name   Image        Replicas
--                         ----   -----        --------
08ecg7vc7cbf9k57qs722n2le  redis  redis:3.0.5  1/1
```

Inspect the service:

```
$ swarmctl service inspect redis
ID                : 08ecg7vc7cbf9k57qs722n2le
Name              : redis
Replicas          : 1/1
Template
 Container
  Image           : redis:3.0.5

Task ID                      Service    Slot    Image          Desired State    Last State                Node
-------                      -------    ----    -----          -------------    ----------                ----
0xk1ir8wr85lbs8sqg0ug03vr    redis      1       redis:3.0.5    RUNNING          RUNNING 1 minutes ago    node-1
```

### Updating Services

You can update any attribute of a service.

For example, you can scale the service by changing the instance count:

```
$ swarmctl service update redis --replicas 6
08ecg7vc7cbf9k57qs722n2le

$ swarmctl service inspect redis
ID                : 08ecg7vc7cbf9k57qs722n2le
Name              : redis
Replicas          : 6/6
Template
 Container
  Image           : redis:3.0.5

Task ID                      Service    Slot    Image          Desired State    Last State                Node
-------                      -------    ----    -----          -------------    ----------                ----
0xk1ir8wr85lbs8sqg0ug03vr    redis      1       redis:3.0.5    RUNNING          RUNNING 3 minutes ago    node-1
25m48y9fevrnh77til1d09vqq    redis      2       redis:3.0.5    RUNNING          RUNNING 28 seconds ago    node-3
42vwc8z93c884anjgpkiatnx6    redis      3       redis:3.0.5    RUNNING          RUNNING 28 seconds ago    node-2
d41f3wnf9dex3mk6jfqp4tdjw    redis      4       redis:3.0.5    RUNNING          RUNNING 28 seconds ago    node-2
66lefnooz63met6yfrsk6myvg    redis      5       redis:3.0.5    RUNNING          RUNNING 28 seconds ago    node-1
3a2sawtoyk19wqhmtuiq7z9pt    redis      6       redis:3.0.5    RUNNING          RUNNING 28 seconds ago    node-3
```

Changing *replicas* from *1* to *6* forced *SwarmKit* to create *5* additional Tasks in order to
comply with the desired state.

Every other field can be changed as well, such as image, args, env, ...

Let's change the image from *redis:3.0.5* to *redis:3.0.6* (e.g. upgrade):

```
$ swarmctl service update redis --image redis:3.0.6
08ecg7vc7cbf9k57qs722n2le

$ swarmctl service inspect redis
ID                   : 08ecg7vc7cbf9k57qs722n2le
Name                 : redis
Replicas             : 6/6
Update Status
 State               : COMPLETED
 Started             : 3 minutes ago
 Completed           : 1 minute ago
 Message             : update completed
Template
 Container
  Image              : redis:3.0.6

Task ID                      Service    Slot    Image          Desired State    Last State              Node
-------                      -------    ----    -----          -------------    ----------              ----
0udsjss61lmwz52pke5hd107g    redis      1       redis:3.0.6    RUNNING          RUNNING 1 minute ago    node-3
b8o394v840thk10tamfqlwztb    redis      2       redis:3.0.6    RUNNING          RUNNING 1 minute ago    node-1
efw7j66xqpoj3cn3zjkdrwff7    redis      3       redis:3.0.6    RUNNING          RUNNING 1 minute ago    node-3
8ajeipzvxucs3776e4z8gemey    redis      4       redis:3.0.6    RUNNING          RUNNING 1 minute ago    node-2
f05f2lbqzk9fh4kstwpulygvu    redis      5       redis:3.0.6    RUNNING          RUNNING 1 minute ago    node-2
7sbpoy82deq7hu3q9cnucfin6    redis      6       redis:3.0.6    RUNNING          RUNNING 1 minute ago    node-1
```

By default, all tasks are updated at the same time.

This behavior can be changed by defining update options.

For instance, in order to update tasks 2 at a time and wait at least 10 seconds between updates:

```
$ swarmctl service update redis --image redis:3.0.7 --update-parallelism 2 --update-delay 10s
$ watch -n1 "swarmctl service inspect redis"  # watch the update
```

This will update 2 tasks, wait for them to become *RUNNING*, then wait an additional 10 seconds before moving to other tasks.

Update options can be set at service creation and updated later on. If an update command doesn't specify update options, the last set of options will be used.

### Node Management

*SwarmKit* monitors node health. In the case of node failures, it re-schedules tasks to other nodes.

An operator can manually define the *Availability* of a node and can *Pause* and *Drain* nodes.

Let's put `node-1` into maintenance mode:

```
$ swarmctl node drain node-1

$ swarmctl node ls
ID                         Name    Membership  Status  Availability  Manager Status
--                         ----    ----------  ------  ------------  --------------
3x12fpoi36eujbdkgdnbvbi6r  node-2  ACCEPTED    READY   ACTIVE
4spl3tyipofoa2iwqgabsdcve  node-1  ACCEPTED    READY   DRAIN         REACHABLE *
dknwk1uqxhnyyujq66ho0h54t  node-3  ACCEPTED    READY   ACTIVE

$ swarmctl service inspect redis
ID                   : 08ecg7vc7cbf9k57qs722n2le
Name                 : redis
Replicas             : 6/6
Update Status
 State               : COMPLETED
 Started             : 2 minutes ago
 Completed           : 1 minute ago
 Message             : update completed
Template
 Container
  Image              : redis:3.0.7

Task ID                      Service    Slot    Image          Desired State    Last State                Node
-------                      -------    ----    -----          -------------    ----------                ----
8uy2fy8dqbwmlvw5iya802tj0    redis      1       redis:3.0.7    RUNNING          RUNNING 23 seconds ago    node-2
7h9lgvidypcr7q1k3lfgohb42    redis      2       redis:3.0.7    RUNNING          RUNNING 2 minutes ago     node-3
ae4dl0chk3gtwm1100t5yeged    redis      3       redis:3.0.7    RUNNING          RUNNING 23 seconds ago    node-3
9fz7fxbg0igypstwliyameobs    redis      4       redis:3.0.7    RUNNING          RUNNING 2 minutes ago     node-3
drzndxnjz3c8iujdewzaplgr6    redis      5       redis:3.0.7    RUNNING          RUNNING 23 seconds ago    node-2
7rcgciqhs4239quraw7evttyf    redis      6       redis:3.0.7    RUNNING          RUNNING 2 minutes ago     node-2
```

As you can see, every Task running on `node-1` was rebalanced to either `node-2` or `node-3` by the reconciliation loop.
### Notice

Do not change .pb.go files directly. You need to change the corresponding .proto files and run the following command to regenerate the .pb.go files.
```
$ make generate
```

Click [here](https://github.com/google/protobuf) for more information about protobuf.

The `api.pb.txt` file contains merged descriptors of all defined services and messages.
Definitions present here are considered frozen after the release.

At release time, the current `api.pb.txt` file will be moved into place to
freeze the API changes for the minor version. For example, when 1.0.0 is
released, `api.pb.txt` should be moved to `1.0.txt`. Notice that we leave off
the patch number, since the API will be completely locked down for a given
patch series.

We may find that by default, protobuf descriptors are too noisy to lock down
API changes. In that case, we may filter out certain fields in the descriptors,
possibly regenerating for old versions.

This process is similar to the [process used to ensure backwards compatibility
in Go](https://github.com/golang/go/tree/master/api).
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
# Docker Events Package

[![GoDoc](https://godoc.org/github.com/docker/go-events?status.svg)](https://godoc.org/github.com/docker/go-events)
[![Circle CI](https://circleci.com/gh/docker/go-events.svg?style=shield)](https://circleci.com/gh/docker/go-events)

The Docker `events` package implements a composable event distribution package
for Go.

Originally created to implement the [notifications in Docker Registry
2](https://github.com/docker/distribution/blob/master/docs/notifications.md),
we've found the pattern to be useful in other applications. This package is
most of the same code with slightly updated interfaces. Much of the internals
have been made available.

## Usage

The `events` package centers around a `Sink` type.  Events are written with
calls to `Sink.Write(event Event)`. Sinks can be wired up in various
configurations to achieve interesting behavior.

The canonical example is that employed by the
[docker/distribution/notifications](https://godoc.org/github.com/docker/distribution/notifications)
package. Let's say we have a type `httpSink` where we'd like to queue
notifications. As a rule, it should send a single http request and return an
error if it fails:

```go
func (h *httpSink) Write(event Event) error {
	p, err := json.Marshal(event)
	if err != nil {
		return err
	}
	body := bytes.NewReader(p)
	resp, err := h.client.Post(h.url, "application/json", body)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	
	if resp.Status != 200 {
		return errors.New("unexpected status")
	}

	return nil
}

// implement (*httpSink).Close()
```

With just that, we can start using components from this package. One can call
`(*httpSink).Write` to send events as the body of a post request to a
configured URL.

### Retries

HTTP can be unreliable. The first feature we'd like is to have some retry:

```go
hs := newHTTPSink(/*...*/)
retry := NewRetryingSink(hs, NewBreaker(5, time.Second))
```

We now have a sink that will retry events against the `httpSink` until they
succeed. The retry will backoff for one second after 5 consecutive failures
using the breaker strategy.

### Queues

This isn't quite enough. We we want a sink that doesn't block while we are
waiting for events to be sent. Let's add a `Queue`:

```go
queue := NewQueue(retry)
```

Now, we have an unbounded queue that will work through all events sent with
`(*Queue).Write`. Events can be added asynchronously to the queue without
blocking the current execution path. This is ideal for use in an http request.

### Broadcast

It usually turns out that you want to send to more than one listener. We can
use `Broadcaster` to support this:

```go
var broadcast = NewBroadcaster() // make it available somewhere in your application.
broadcast.Add(queue) // add your queue!
broadcast.Add(queue2) // and another!
```

With the above, we can now call `broadcast.Write` in our http handlers and have
all the events distributed to each queue. Because the events are queued, not
listener blocks another.

### Extending

For the most part, the above is sufficient for a lot of applications. However,
extending the above functionality can be done implementing your own `Sink`. The
behavior and semantics of the sink can be completely dependent on the
application requirements. The interface is provided below for reference:

```go
type Sink {
	Write(Event) error
	Close() error
}
```

Application behavior can be controlled by how `Write` behaves. The examples
above are designed to queue the message and return as quickly as possible.
Other implementations may block until the event is committed to durable
storage.

## Copyright and license

Copyright © 2016 Docker, Inc. go-events is licensed under the Apache License,
Version 2.0. See [LICENSE](LICENSE) for the full license text.
[![GoDoc](https://godoc.org/github.com/docker/go-connections?status.svg)](https://godoc.org/github.com/docker/go-connections)

# Introduction

go-connections provides common package to work with network connections.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-connections) for examples and documentation.

## License

go-connections is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
This project was automatically exported from code.google.com/p/go-uuid

# uuid ![build status](https://travis-ci.org/pborman/uuid.svg?branch=master)
The uuid package generates and inspects UUIDs based on [RFC 412](http://tools.ietf.org/html/rfc4122) and DCE 1.1: Authentication and Security Services. 

###### Install
`go get github.com/pborman/uuid`

###### Documentation 
[![GoDoc](https://godoc.org/github.com/pborman/uuid?status.svg)](http://godoc.org/github.com/pborman/uuid)

Full `go doc` style documentation for the package can be viewed online without installing this package by using the GoDoc site here: 
http://godoc.org/github.com/pborman/uuid
# pty

Pty is a Go package for using unix pseudo-terminals.

## Install

    go get github.com/kr/pty

## Example

```go
package main

import (
	"github.com/kr/pty"
	"io"
	"os"
	"os/exec"
)

func main() {
	c := exec.Command("grep", "--color=auto", "bar")
	f, err := pty.Start(c)
	if err != nil {
		panic(err)
	}

	go func() {
		f.Write([]byte("foo\n"))
		f.Write([]byte("bar\n"))
		f.Write([]byte("baz\n"))
		f.Write([]byte{4}) // EOT
	}()
	io.Copy(os.Stdout, f)
}
```
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
consistency and thread safety. Bolt is currently in high-load production
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
	for k, v := c.Seek(prefix); bytes.HasPrefix(k, prefix); k, v = c.Next() {
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

If you are using Bolt in a project please send a pull request to add it to the list.
# Google Cloud Client Libraries for Go

[![GoDoc](https://godoc.org/cloud.google.com/go?status.svg)](https://godoc.org/cloud.google.com/go)

Go packages for [Google Cloud Platform](https://cloud.google.com) services.

``` go
import "cloud.google.com/go"
```

To install the packages on your system,

```
$ go get -u cloud.google.com/go/...
```

**NOTE:** Some of these packages are under development, and may occasionally
make backwards-incompatible changes.

**NOTE:** Github repo is a mirror of [https://code.googlesource.com/gocloud](https://code.googlesource.com/gocloud).

  * [News](#news)
  * [Supported APIs](#supported-apis)
  * [Go Versions Supported](#go-versions-supported)
  * [Authorization](#authorization)
  * [Cloud Datastore](#cloud-datastore-)
  * [Cloud Storage](#cloud-storage-)
  * [Cloud Pub/Sub](#cloud-pub-sub-)
  * [Cloud BigQuery](#cloud-bigquery-)
  * [Stackdriver Logging](#stackdriver-logging-)
  * [Cloud Spanner](#cloud-spanner-)


## News

_May 18, 2018_

*v0.23.0*

- bigquery: Add DDL stats to query statistics.
- bigtable:
  - cbt: Add cells-per-column limit for row lookup.
  - cbt: Make it possible to combine read filters.
- dlp: v2beta2 client removed. Use the v2 client instead.
- firestore, spanner: Fix compilation errors due to protobuf changes.

_May 8, 2018_

*v0.22.0*

- bigtable:
  - cbt: Support cells per column limit for row read.
  - bttest: Correctly handle empty RowSet.
  - Fix ReadModifyWrite operation in emulator.
  - Fix API path in GetCluster.

- bigquery:
  - BEHAVIOR CHANGE: Retry on 503 status code.
  - Add dataset.DeleteWithContents.
  - Add SchemaUpdateOptions for query jobs.
  - Add Timeline to QueryStatistics.
  - Add more stats to ExplainQueryStage.
  - Support Parquet data format.

- datastore:
  - Support omitempty for times.

- dlp:
  - **BREAKING CHANGE:** Remove v1beta1 client. Please migrate to the v2 client,
  which is now out of beta.
  - Add v2 client.

- firestore:
  - BEHAVIOR CHANGE: Treat set({}, MergeAll) as valid.

- iam:
  - Support JWT signing via SignJwt callopt.

- profiler:
  - BEHAVIOR CHANGE: PollForSerialOutput returns an error when context.Done.
  - BEHAVIOR CHANGE: Increase the initial backoff to 1 minute.
  - Avoid returning empty serial port output.

- pubsub:
  - BEHAVIOR CHANGE: Don't backoff during next retryable error once stream is healthy.
  - BEHAVIOR CHANGE: Don't backoff on EOF.
  - pstest: Support Acknowledge and ModifyAckDeadline RPCs.

- redis:
  - Add v1 beta Redis client.

- spanner:
  - Support SessionLabels.

- speech:
  - Add api v1 beta1 client.

- storage:
  - BEHAVIOR CHANGE: Retry reads when retryable error occurs.
  - Fix delete of object in requester-pays bucket.
  - Support KMS integration.

_April 9, 2018_

*v0.21.0*

- bigquery:
  - Add OpenCensus tracing.

- firestore:
  - **BREAKING CHANGE:** If a document does not exist, return a DocumentSnapshot
    whose Exists method returns false. DocumentRef.Get and Transaction.Get
    return the non-nil DocumentSnapshot in addition to a NotFound error.
    **DocumentRef.GetAll and Transaction.GetAll return a non-nil
    DocumentSnapshot instead of nil.**
  - Add DocumentIterator.Stop. **Call Stop whenever you are done with a
    DocumentIterator.**
  - Added Query.Snapshots and DocumentRef.Snapshots, which provide realtime
    notification of updates. See https://cloud.google.com/firestore/docs/query-data/listen.
  - Canceling an RPC now always returns a grpc.Status with codes.Canceled.

- spanner:
  - Add `CommitTimestamp`, which supports inserting the commit timestamp of a
    transaction into a column.

_March 22, 2018_

*v0.20.0*

- bigquery: Support SchemaUpdateOptions for load jobs.

- bigtable:
  - Add SampleRowKeys.
  - cbt: Support union, intersection GCPolicy.
  - Retry admin RPCS.
  - Add trace spans to retries.

- datastore: Add OpenCensus tracing.

- firestore:
  - Fix queries involving Null and NaN.
  - Allow Timestamp protobuffers for time values.

- logging: Add a WriteTimeout option.

- spanner: Support Batch API.

- storage: Add OpenCensus tracing.


_February 26, 2018_

*v0.19.0*

- bigquery:
  - Support customer-managed encryption keys.

- bigtable:
  - Improved emulator support.
  - Support GetCluster.

- datastore:
  - Add general mutations.
  - Support pointer struct fields.
  - Support transaction options.

- firestore:
  - Add Transaction.GetAll.
  - Support document cursors.

- logging:
  - Support concurrent RPCs to the service.
  - Support per-entry resources.

- profiler:
  - Add config options to disable heap and thread profiling.
  - Read the project ID from $GOOGLE_CLOUD_PROJECT when it's set.

- pubsub:
  - BEHAVIOR CHANGE: Release flow control after ack/nack (instead of after the
    callback returns).
  - Add SubscriptionInProject.
  - Add OpenCensus instrumentation for streaming pull.

- storage:
  - Support CORS.


_January 18, 2018_

*v0.18.0*

- bigquery:
  - Marked stable.
  - Schema inference of nullable fields supported.
  - Added TimePartitioning to QueryConfig.

- firestore: Data provided to DocumentRef.Set with a Merge option can contain
  Delete sentinels.

- logging: Clients can accept parent resources other than projects.

- pubsub:
  - pubsub/pstest: A lighweight fake for pubsub. Experimental; feedback welcome.
  - Support updating more subscription metadata: AckDeadline,
    RetainAckedMessages and RetentionDuration.

- oslogin/apiv1beta: New client for the Cloud OS Login API.

- rpcreplay: A package for recording and replaying gRPC traffic.

- spanner:
  - Add a ReadWithOptions that supports a row limit, as well as an index.
  - Support query plan and execution statistics.
  - Added [OpenCensus](http://opencensus.io) support.

- storage: Clarify checksum validation for gzipped files (it is not validated
  when the file is served uncompressed).


_December 11, 2017_

*v0.17.0*

- firestore BREAKING CHANGES:
  - Remove UpdateMap and UpdateStruct; rename UpdatePaths to Update.
    Change
        `docref.UpdateMap(ctx, map[string]interface{}{"a.b", 1})`
    to
        `docref.Update(ctx, []firestore.Update{{Path: "a.b", Value: 1}})`

    Change
        `docref.UpdateStruct(ctx, []string{"Field"}, aStruct)`
    to
        `docref.Update(ctx, []firestore.Update{{Path: "Field", Value: aStruct.Field}})`
  - Rename MergePaths to Merge; require args to be FieldPaths
  - A value stored as an integer can be read into a floating-point field, and vice versa.
- bigtable/cmd/cbt:
  - Support deleting a column.
  - Add regex option for row read.
- spanner: Mark stable.
- storage:
  - Add Reader.ContentEncoding method.
  - Fix handling of SignedURL headers.
- bigquery:
  - If Uploader.Put is called with no rows, it returns nil without making a
    call.
  - Schema inference supports the "nullable" option in struct tags for
    non-required fields.
  - TimePartitioning supports "Field".


[Older news](https://github.com/GoogleCloudPlatform/google-cloud-go/blob/master/old-news.md)

## Supported APIs

Google API                       | Status       | Package
---------------------------------|--------------|-----------------------------------------------------------
[BigQuery][cloud-bigquery]       | stable       | [`cloud.google.com/go/bigquery`][cloud-bigquery-ref]
[Bigtable][cloud-bigtable]       | stable       | [`cloud.google.com/go/bigtable`][cloud-bigtable-ref]
[Container][cloud-container]     | alpha        | [`cloud.google.com/go/container/apiv1`][cloud-container-ref]
[Data Loss Prevention][cloud-dlp]| alpha        | [`cloud.google.com/go/dlp/apiv2beta1`][cloud-dlp-ref]
[Datastore][cloud-datastore]     | stable       | [`cloud.google.com/go/datastore`][cloud-datastore-ref]
[Debugger][cloud-debugger]       | alpha        | [`cloud.google.com/go/debugger/apiv2`][cloud-debugger-ref]
[ErrorReporting][cloud-errors]   | alpha        | [`cloud.google.com/go/errorreporting`][cloud-errors-ref]
[Firestore][cloud-firestore]     | beta         | [`cloud.google.com/go/firestore`][cloud-firestore-ref]
[Language][cloud-language]       | stable       | [`cloud.google.com/go/language/apiv1`][cloud-language-ref]
[Logging][cloud-logging]         | stable       | [`cloud.google.com/go/logging`][cloud-logging-ref]
[Monitoring][cloud-monitoring]   | beta         | [`cloud.google.com/go/monitoring/apiv3`][cloud-monitoring-ref]
[OS Login][cloud-oslogin]        | alpha        | [`cloud.google.com/compute/docs/oslogin/rest`][cloud-oslogin-ref]
[Pub/Sub][cloud-pubsub]          | beta         | [`cloud.google.com/go/pubsub`][cloud-pubsub-ref]
[Spanner][cloud-spanner]         | stable       | [`cloud.google.com/go/spanner`][cloud-spanner-ref]
[Speech][cloud-speech]           | stable       | [`cloud.google.com/go/speech/apiv1`][cloud-speech-ref]
[Storage][cloud-storage]         | stable       | [`cloud.google.com/go/storage`][cloud-storage-ref]
[Translation][cloud-translation] | stable       | [`cloud.google.com/go/translate`][cloud-translation-ref]
[Video Intelligence][cloud-video]| beta         | [`cloud.google.com/go/videointelligence/apiv1beta1`][cloud-video-ref]
[Vision][cloud-vision]           | stable       | [`cloud.google.com/go/vision/apiv1`][cloud-vision-ref]


> **Alpha status**: the API is still being actively developed. As a
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

[snip]:# (auth)
```go
client, err := storage.NewClient(ctx)
```

To authorize using a
[JSON key file](https://cloud.google.com/iam/docs/managing-service-account-keys),
pass
[`option.WithServiceAccountFile`](https://godoc.org/google.golang.org/api/option#WithServiceAccountFile)
to the `NewClient` function of the desired package. For example:

[snip]:# (auth-JSON)
```go
client, err := storage.NewClient(ctx, option.WithServiceAccountFile("path/to/keyfile.json"))
```

You can exert more control over authorization by using the
[`golang.org/x/oauth2`](https://godoc.org/golang.org/x/oauth2) package to
create an `oauth2.TokenSource`. Then pass
[`option.WithTokenSource`](https://godoc.org/google.golang.org/api/option#WithTokenSource)
to the `NewClient` function:
[snip]:# (auth-ts)
```go
tokenSource := ...
client, err := storage.NewClient(ctx, option.WithTokenSource(tokenSource))
```

## Cloud Datastore [![GoDoc](https://godoc.org/cloud.google.com/go/datastore?status.svg)](https://godoc.org/cloud.google.com/go/datastore)

- [About Cloud Datastore][cloud-datastore]
- [Activating the API for your project][cloud-datastore-activation]
- [API documentation][cloud-datastore-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/datastore)
- [Complete sample program](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/datastore/tasks)

### Example Usage

First create a `datastore.Client` to use throughout your application:

[snip]:# (datastore-1)
```go
client, err := datastore.NewClient(ctx, "my-project-id")
if err != nil {
	log.Fatal(err)
}
```

Then use that client to interact with the API:

[snip]:# (datastore-2)
```go
type Post struct {
	Title       string
	Body        string `datastore:",noindex"`
	PublishedAt time.Time
}
keys := []*datastore.Key{
	datastore.NameKey("Post", "post1", nil),
	datastore.NameKey("Post", "post2", nil),
}
posts := []*Post{
	{Title: "Post 1", Body: "...", PublishedAt: time.Now()},
	{Title: "Post 2", Body: "...", PublishedAt: time.Now()},
}
if _, err := client.PutMulti(ctx, keys, posts); err != nil {
	log.Fatal(err)
}
```

## Cloud Storage [![GoDoc](https://godoc.org/cloud.google.com/go/storage?status.svg)](https://godoc.org/cloud.google.com/go/storage)

- [About Cloud Storage][cloud-storage]
- [API documentation][cloud-storage-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/storage)
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/storage)

### Example Usage

First create a `storage.Client` to use throughout your application:

[snip]:# (storage-1)
```go
client, err := storage.NewClient(ctx)
if err != nil {
	log.Fatal(err)
}
```

[snip]:# (storage-2)
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

## Cloud Pub/Sub [![GoDoc](https://godoc.org/cloud.google.com/go/pubsub?status.svg)](https://godoc.org/cloud.google.com/go/pubsub)

- [About Cloud Pubsub][cloud-pubsub]
- [API documentation][cloud-pubsub-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/pubsub)
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/pubsub)

### Example Usage

First create a `pubsub.Client` to use throughout your application:

[snip]:# (pubsub-1)
```go
client, err := pubsub.NewClient(ctx, "project-id")
if err != nil {
	log.Fatal(err)
}
```

Then use the client to publish and subscribe:

[snip]:# (pubsub-2)
```go
// Publish "hello world" on topic1.
topic := client.Topic("topic1")
res := topic.Publish(ctx, &pubsub.Message{
	Data: []byte("hello world"),
})
// The publish happens asynchronously.
// Later, you can get the result from res:
...
msgID, err := res.Get(ctx)
if err != nil {
	log.Fatal(err)
}

// Use a callback to receive messages via subscription1.
sub := client.Subscription("subscription1")
err = sub.Receive(ctx, func(ctx context.Context, m *pubsub.Message) {
	fmt.Println(m.Data)
	m.Ack() // Acknowledge that we've consumed the message.
})
if err != nil {
	log.Println(err)
}
```

## Cloud BigQuery [![GoDoc](https://godoc.org/cloud.google.com/go/bigquery?status.svg)](https://godoc.org/cloud.google.com/go/bigquery)

- [About Cloud BigQuery][cloud-bigquery]
- [API documentation][cloud-bigquery-docs]
- [Go client documentation][cloud-bigquery-ref]
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/bigquery)

### Example Usage

First create a `bigquery.Client` to use throughout your application:
[snip]:# (bq-1)
```go
c, err := bigquery.NewClient(ctx, "my-project-ID")
if err != nil {
	// TODO: Handle error.
}
```

Then use that client to interact with the API:
[snip]:# (bq-2)
```go
// Construct a query.
q := c.Query(`
    SELECT year, SUM(number)
    FROM [bigquery-public-data:usa_names.usa_1910_2013]
    WHERE name = "William"
    GROUP BY year
    ORDER BY year
`)
// Execute the query.
it, err := q.Read(ctx)
if err != nil {
	// TODO: Handle error.
}
// Iterate through the results.
for {
	var values []bigquery.Value
	err := it.Next(&values)
	if err == iterator.Done {
		break
	}
	if err != nil {
		// TODO: Handle error.
	}
	fmt.Println(values)
}
```


## Stackdriver Logging [![GoDoc](https://godoc.org/cloud.google.com/go/logging?status.svg)](https://godoc.org/cloud.google.com/go/logging)

- [About Stackdriver Logging][cloud-logging]
- [API documentation][cloud-logging-docs]
- [Go client documentation][cloud-logging-ref]
- [Complete sample programs](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/logging)

### Example Usage

First create a `logging.Client` to use throughout your application:
[snip]:# (logging-1)
```go
ctx := context.Background()
client, err := logging.NewClient(ctx, "my-project")
if err != nil {
	// TODO: Handle error.
}
```

Usually, you'll want to add log entries to a buffer to be periodically flushed
(automatically and asynchronously) to the Stackdriver Logging service.
[snip]:# (logging-2)
```go
logger := client.Logger("my-log")
logger.Log(logging.Entry{Payload: "something happened!"})
```

Close your client before your program exits, to flush any buffered log entries.
[snip]:# (logging-3)
```go
err = client.Close()
if err != nil {
	// TODO: Handle error.
}
```

## Cloud Spanner [![GoDoc](https://godoc.org/cloud.google.com/go/spanner?status.svg)](https://godoc.org/cloud.google.com/go/spanner)

- [About Cloud Spanner][cloud-spanner]
- [API documentation][cloud-spanner-docs]
- [Go client documentation](https://godoc.org/cloud.google.com/go/spanner)

### Example Usage

First create a `spanner.Client` to use throughout your application:

[snip]:# (spanner-1)
```go
client, err := spanner.NewClient(ctx, "projects/P/instances/I/databases/D")
if err != nil {
	log.Fatal(err)
}
```

[snip]:# (spanner-2)
```go
// Simple Reads And Writes
_, err = client.Apply(ctx, []*spanner.Mutation{
	spanner.Insert("Users",
		[]string{"name", "email"},
		[]interface{}{"alice", "a@example.com"})})
if err != nil {
	log.Fatal(err)
}
row, err := client.Single().ReadRow(ctx, "Users",
	spanner.Key{"alice"}, []string{"email"})
if err != nil {
	log.Fatal(err)
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

[cloud-firestore]: https://cloud.google.com/firestore/
[cloud-firestore-ref]: https://godoc.org/cloud.google.com/go/firestore
[cloud-firestore-docs]: https://cloud.google.com/firestore/docs
[cloud-firestore-activation]: https://cloud.google.com/firestore/docs/activate

[cloud-pubsub]: https://cloud.google.com/pubsub/
[cloud-pubsub-ref]: https://godoc.org/cloud.google.com/go/pubsub
[cloud-pubsub-docs]: https://cloud.google.com/pubsub/docs

[cloud-storage]: https://cloud.google.com/storage/
[cloud-storage-ref]: https://godoc.org/cloud.google.com/go/storage
[cloud-storage-docs]: https://cloud.google.com/storage/docs
[cloud-storage-create-bucket]: https://cloud.google.com/storage/docs/cloud-console#_creatingbuckets

[cloud-bigtable]: https://cloud.google.com/bigtable/
[cloud-bigtable-ref]: https://godoc.org/cloud.google.com/go/bigtable

[cloud-bigquery]: https://cloud.google.com/bigquery/
[cloud-bigquery-docs]: https://cloud.google.com/bigquery/docs
[cloud-bigquery-ref]: https://godoc.org/cloud.google.com/go/bigquery

[cloud-logging]: https://cloud.google.com/logging/
[cloud-logging-docs]: https://cloud.google.com/logging/docs
[cloud-logging-ref]: https://godoc.org/cloud.google.com/go/logging

[cloud-monitoring]: https://cloud.google.com/monitoring/
[cloud-monitoring-ref]: https://godoc.org/cloud.google.com/go/monitoring/apiv3

[cloud-vision]: https://cloud.google.com/vision
[cloud-vision-ref]: https://godoc.org/cloud.google.com/go/vision/apiv1

[cloud-language]: https://cloud.google.com/natural-language
[cloud-language-ref]: https://godoc.org/cloud.google.com/go/language/apiv1

[cloud-oslogin]: https://cloud.google.com/compute/docs/oslogin/rest
[cloud-oslogin-ref]: https://cloud.google.com/compute/docs/oslogin/rest

[cloud-speech]: https://cloud.google.com/speech
[cloud-speech-ref]: https://godoc.org/cloud.google.com/go/speech/apiv1

[cloud-spanner]: https://cloud.google.com/spanner/
[cloud-spanner-ref]: https://godoc.org/cloud.google.com/go/spanner
[cloud-spanner-docs]: https://cloud.google.com/spanner/docs

[cloud-translation]: https://cloud.google.com/translation
[cloud-translation-ref]: https://godoc.org/cloud.google.com/go/translation

[cloud-video]: https://cloud.google.com/video-intelligence/
[cloud-video-ref]: https://godoc.org/cloud.google.com/go/videointelligence/apiv1beta1

[cloud-errors]: https://cloud.google.com/error-reporting/
[cloud-errors-ref]: https://godoc.org/cloud.google.com/go/errorreporting

[cloud-container]: https://cloud.google.com/containers/
[cloud-container-ref]: https://godoc.org/cloud.google.com/go/container/apiv1

[cloud-debugger]: https://cloud.google.com/debugger/
[cloud-debugger-ref]: https://godoc.org/cloud.google.com/go/debugger/apiv2

[cloud-dlp]: https://cloud.google.com/dlp/
[cloud-dlp-ref]: https://godoc.org/cloud.google.com/go/dlp/apiv2beta1

[default-creds]: https://developers.google.com/identity/protocols/application-default-credentials
Auto-generated logging v2 clients
=================================

This package includes auto-generated clients for the logging v2 API.

Use the handwritten logging client (in the parent directory,
cloud.google.com/go/logging) in preference to this.

This code is EXPERIMENTAL and subject to CHANGE AT ANY TIME.


# OpenCensus Libraries for Go

[![Build Status][travis-image]][travis-url]
[![Windows Build Status][appveyor-image]][appveyor-url]
[![GoDoc][godoc-image]][godoc-url]
[![Gitter chat][gitter-image]][gitter-url]

OpenCensus Go is a Go implementation of OpenCensus, a toolkit for
collecting application performance and behavior monitoring data.
Currently it consists of three major components: tags, stats, and tracing.

## Installation

```
$ go get -u go.opencensus.io
```

The API of this project is still evolving, see: [Deprecation Policy](#deprecation-policy).
The use of vendoring or a dependency management tool is recommended.

## Prerequisites

OpenCensus Go libraries require Go 1.8 or later.

## Exporters

OpenCensus can export instrumentation data to various backends. 
Currently, OpenCensus supports:

* [Prometheus][exporter-prom] for stats
* [OpenZipkin][exporter-zipkin] for traces
* Stackdriver [Monitoring][exporter-stackdriver] and [Trace][exporter-stackdriver]
* [Jaeger][exporter-jaeger] for traces
* [AWS X-Ray][exporter-xray] for traces


## Overview

![OpenCensus Overview](https://i.imgur.com/cf4ElHE.jpg)

In a microservices environment, a user request may go through
multiple services until there is a response. OpenCensus allows
you to instrument your services and collect diagnostics data all
through your services end-to-end.

Start with instrumenting HTTP and gRPC clients and servers,
then add additional custom instrumentation if needed.

* [HTTP guide](https://github.com/census-instrumentation/opencensus-go/tree/master/examples/http)
* [gRPC guide](https://github.com/census-instrumentation/opencensus-go/tree/master/examples/grpc)


## Tags

Tags represent propagated key-value pairs. They are propagated using `context.Context`
in the same process or can be encoded to be transmitted on the wire. Usually, this will
be handled by an integration plugin, e.g. `ocgrpc.ServerHandler` and `ocgrpc.ClientHandler`
for gRPC.

Package tag allows adding or modifying tags in the current context.

[embedmd]:# (internal/readme/tags.go new)
```go
ctx, err = tag.New(ctx,
	tag.Insert(osKey, "macOS-10.12.5"),
	tag.Upsert(userIDKey, "cde36753ed"),
)
if err != nil {
	log.Fatal(err)
}
```

## Stats

OpenCensus is a low-overhead framework even if instrumentation is always enabled.
In order to be so, it is optimized to make recording of data points fast
and separate from the data aggregation.

OpenCensus stats collection happens in two stages:

* Definition of measures and recording of data points
* Definition of views and aggregation of the recorded data

### Recording

Measurements are data points associated with a measure.
Recording implicitly tags the set of Measurements with the tags from the
provided context:

[embedmd]:# (internal/readme/stats.go record)
```go
stats.Record(ctx, videoSize.M(102478))
```

### Views

Views are how Measures are aggregated. You can think of them as queries over the
set of recorded data points (measurements).

Views have two parts: the tags to group by and the aggregation type used.

Currently three types of aggregations are supported:
* CountAggregation is used to count the number of times a sample was recorded.
* DistributionAggregation is used to provide a histogram of the values of the samples.
* SumAggregation is used to sum up all sample values.

[embedmd]:# (internal/readme/stats.go aggs)
```go
distAgg := view.Distribution(0, 1<<32, 2<<32, 3<<32)
countAgg := view.Count()
sumAgg := view.Sum()
```

Here we create a view with the DistributionAggregation over our measure.

[embedmd]:# (internal/readme/stats.go view)
```go
if err := view.Register(&view.View{
	Name:        "my.org/video_size_distribution",
	Description: "distribution of processed video size over time",
	Measure:     videoSize,
	Aggregation: view.Distribution(0, 1<<32, 2<<32, 3<<32),
}); err != nil {
	log.Fatalf("Failed to subscribe to view: %v", err)
}
```

Subscribe begins collecting data for the view. Subscribed views' data will be
exported via the registered exporters.

## Traces

[embedmd]:# (internal/readme/trace.go startend)
```go
ctx, span := trace.StartSpan(ctx, "your choice of name")
defer span.End()
```

## Profiles

OpenCensus tags can be applied as profiler labels
for users who are on Go 1.9 and above.

[embedmd]:# (internal/readme/tags.go profiler)
```go
ctx, err = tag.New(ctx,
	tag.Insert(osKey, "macOS-10.12.5"),
	tag.Insert(userIDKey, "fff0989878"),
)
if err != nil {
	log.Fatal(err)
}
tag.Do(ctx, func(ctx context.Context) {
	// Do work.
	// When profiling is on, samples will be
	// recorded with the key/values from the tag map.
})
```

A screenshot of the CPU profile from the program above:

![CPU profile](https://i.imgur.com/jBKjlkw.png)

## Deprecation Policy

Before version 1.0.0, the following deprecation policy will be observed:

No backwards-incompatible changes will be made except for the removal of symbols that have
been marked as *Deprecated* for at least one minor release (e.g. 0.9.0 to 0.10.0). A release
removing the *Deprecated* functionality will be made no sooner than 28 days after the first 
release in which the functionality was marked *Deprecated*.

[travis-image]: https://travis-ci.org/census-instrumentation/opencensus-go.svg?branch=master
[travis-url]: https://travis-ci.org/census-instrumentation/opencensus-go
[appveyor-image]: https://ci.appveyor.com/api/projects/status/vgtt29ps1783ig38?svg=true
[appveyor-url]: https://ci.appveyor.com/project/opencensusgoteam/opencensus-go/branch/master
[godoc-image]: https://godoc.org/go.opencensus.io?status.svg
[godoc-url]: https://godoc.org/go.opencensus.io
[gitter-image]: https://badges.gitter.im/census-instrumentation/lobby.svg
[gitter-url]: https://gitter.im/census-instrumentation/lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


[new-ex]: https://godoc.org/go.opencensus.io/tag#example-NewMap
[new-replace-ex]: https://godoc.org/go.opencensus.io/tag#example-NewMap--Replace

[exporter-prom]: https://godoc.org/go.opencensus.io/exporter/prometheus
[exporter-stackdriver]: https://godoc.org/contrib.go.opencensus.io/exporter/stackdriver
[exporter-zipkin]: https://godoc.org/go.opencensus.io/exporter/zipkin
[exporter-jaeger]: https://godoc.org/go.opencensus.io/exporter/jaeger
[exporter-xray]: https://github.com/census-instrumentation/opencensus-go-exporter-aws
# Google APIs Client Library for Go

## Getting Started

```
$ go get google.golang.org/api/tasks/v1
$ go get google.golang.org/api/moderator/v1
$ go get google.golang.org/api/urlshortener/v1
... etc ...
```

and using:

```go
package main

import (
	"net/http"

	"google.golang.org/api/urlshortener/v1"
)

func main() {
	svc, err := urlshortener.New(http.DefaultClient)
	// ...
}
```

* For a longer tutorial, see the [Getting Started guide](https://github.com/google/google-api-go-client/blob/master/GettingStarted.md).
* For examples, see the [examples directory](https://github.com/google/google-api-go-client/tree/master/examples).
* For support, use the [golang-nuts](https://groups.google.com/group/golang-nuts) mailing list.

## Status
[![Build Status](https://travis-ci.org/google/google-api-go-client.png)](https://travis-ci.org/google/google-api-go-client)
[![GoDoc](https://godoc.org/google.golang.org/api?status.svg)](https://godoc.org/google.golang.org/api)

These are auto-generated Go libraries from the Google Discovery Service's JSON description files of the available "new style" Google APIs.

Due to the auto-generated nature of this collection of libraries, complete APIs or specific versions can appear or go away without notice.
As a result, you should always locally vendor any API(s) that your code relies upon.

These client libraries are officially supported by Google.  However, the libraries are considered complete and are in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

If you're working with Google Cloud Platform APIs such as Datastore or Pub/Sub,
consider using the
[Cloud Client Libraries for Go](https://github.com/GoogleCloudPlatform/google-cloud-go)
instead. These are the new and
idiomatic Go libraries targeted specifically at Google Cloud Platform Services.

The generator itself and the code it produces are beta. Some APIs are
alpha/beta, and indicated as such in the import path (e.g.,
"google.golang.org/api/someapi/v1alpha").

## Application Default Credentials Example

Application Default Credentials provide a simplified way to obtain credentials
for authenticating with Google APIs.

The Application Default Credentials authenticate as the application itself,
which make them great for working with Google Cloud APIs like Storage or
Datastore. They are the recommended form of authentication when building
applications that run on Google Compute Engine or Google App Engine.

Default credentials are provided by the `golang.org/x/oauth2/google` package. To use them, add the following import:

```go
import "golang.org/x/oauth2/google"
```

Some credentials types require you to specify scopes, and service entry points may not inject them. If you encounter this situation you may need to specify scopes as follows:

```go
import (
        "golang.org/x/net/context"
        "golang.org/x/oauth2/google"
        "google.golang.org/api/compute/v1"
)

func main() {
        // Use oauth2.NoContext if there isn't a good context to pass in.
        ctx := context.Background()

        client, err := google.DefaultClient(ctx, compute.ComputeScope)
        if err != nil {
                //...
        }
        computeService, err := compute.New(client)
        if err != nil {
                //...
        }
}
```

If you need a `oauth2.TokenSource`, use the `DefaultTokenSource` function:

```go
ts, err := google.DefaultTokenSource(ctx, scope1, scope2, ...)
if err != nil {
        //...
}
client := oauth2.NewClient(ctx, ts)
```

See also: [golang.org/x/oauth2/google](https://godoc.org/golang.org/x/oauth2/google) package documentation.
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
pkg/ is a collection of utility packages used by the Moby project without being specific to its internals.

Utility packages are kept separate from the moby core codebase to keep it as small and concise as possible.
If some utilities grow larger and their APIs stabilize, they may be moved to their own repository under the
Moby organization, to facilitate re-use by other projects. However that is not the priority.

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
	return i.data[name]
}

func (i *important) Create(name string, data interface{}) {
	i.locks.Lock(name)
	defer i.locks.Unlock(name)

	i.createImportant(data)

	i.mu.Lock()
	i.data[name] = data
	i.mu.Unlock()
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

With [vim-plug](https://github.com/junegunn/vim-plug)
  
    Plug 'docker/docker' , {'rtp': '/contrib/syntax/vim/'}   

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

If you're a *contributor* or aspiring contributor, you should read [CONTRIBUTING.md](../CONTRIBUTING.md).

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
daemon via the `--storage-opt dm.thinpooldev` option. Alternatively,
the device mapper graphdriver can setup a block device to handle this
for you via the `--storage-opt dm.directlvm_device` option.

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
# Docker Image Specification v1.

This directory contains documents about Docker Image Specification v1.X.

The v1 file layout and manifests are no longer used in Moby and Docker, except in `docker save` and `docker load`.

However, v1 Image JSON (`application/vnd.docker.container.image.v1+json`) has been still widely
used and officially adopted in [V2 manifest](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md)
and in [OCI Image Format Specification](https://github.com/opencontainers/image-spec).

## v1.X rough Changelog

All 1.X versions are compatible with older ones.

### [v1.2](v1.2.md)

* Implemented in Docker v1.12 (July, 2016)
* The official spec document was written in August 2016 ([#25750](https://github.com/moby/moby/pull/25750))

Changes:

* `Healthcheck` struct was added to Image JSON

### [v1.1](v1.1.md)

* Implemented in Docker v1.10 (February, 2016)
* The official spec document was written in April 2016 ([#22264](https://github.com/moby/moby/pull/22264))

Changes:

* IDs were made into SHA256 digest values rather than random values
* Layer directory names were made into deterministic values rather than random ID values
* `manifest.json` was added 

### [v1](v1.md)

* The initial revision
* The official spec document was written in late 2014 ([#9560](https://github.com/moby/moby/pull/9560)), but actual implementations had existed even earlier


## Related specifications

* [Open Containers Initiative (OCI) Image Format Specification v1.0.0](https://github.com/opencontainers/image-spec/tree/v1.0.0)
* [Docker Image Manifest Version 2, Schema 2](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md)
* [Docker Image Manifest Version 2, Schema 1](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-1.md) (*DEPRECATED*)
* [Docker Registry HTTP API V2](https://docs.docker.com/registry/spec/api/)
### Get set up for Moby development

 * [README first](who-written-for.md)
 * [Get the required software](software-required.md)
 * [Set up for development on Windows](software-req-win.md)
 * [Configure Git for contributing](set-up-git.md)
 * [Work with a development container](set-up-dev-env.md)
 * [Run tests and test documentation](test.md)
docker.go contains Docker daemon's main function.

This file provides first line CLI argument parsing and environment variable setting.
## About

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

## Vendor (vendor.sh)

A shell script that is a wrapper around Vndr. For information on how to use
this, please refer to [vndr's README](https://github.com/LK4D4/vndr/blob/master/README.md)
This directory holds scripts called by `make.sh` in the parent directory.

Each script is named after the bundle it creates.
They should not be called directly - instead, pass it as argument to make.sh, for example:

```
./hack/make.sh binary ubuntu

# Or to run all default bundles:
./hack/make.sh
```

To add a bundle:

* Create a shell-compatible file here
* Add it to $DEFAULT_BUNDLES in make.sh
# Integration Testing on Swarm

IT on Swarm allows you to execute integration test in parallel across a Docker Swarm cluster

## Architecture

### Master service

  - Works as a funker caller
  - Calls a worker funker (`-worker-service`) with a chunk of `-check.f` filter strings (passed as a file via `-input` flag, typically `/mnt/input`)

### Worker service

  - Works as a funker callee
  - Executes an equivalent of `TESTFLAGS=-check.f TestFoo|TestBar|TestBaz ... make test-integration` using the bind-mounted API socket (`docker.sock`)

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
