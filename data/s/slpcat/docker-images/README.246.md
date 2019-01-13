# Prometheus [![Build Status](https://travis-ci.org/prometheus/prometheus.svg)][travis]

[![CircleCI](https://circleci.com/gh/prometheus/prometheus/tree/master.svg?style=shield)][circleci]
[![Docker Repository on Quay](https://quay.io/repository/prometheus/prometheus/status)][quay]
[![Docker Pulls](https://img.shields.io/docker/pulls/prom/prometheus.svg?maxAge=604800)][hub]
[![Go Report Card](https://goreportcard.com/badge/github.com/prometheus/prometheus)](https://goreportcard.com/report/github.com/prometheus/prometheus)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/486/badge)](https://bestpractices.coreinfrastructure.org/projects/486)

Visit [prometheus.io](https://prometheus.io) for the full documentation,
examples and guides.

Prometheus, a [Cloud Native Computing Foundation](https://cncf.io/) project, is a systems and service monitoring system. It collects metrics
from configured targets at given intervals, evaluates rule expressions,
displays the results, and can trigger alerts if some condition is observed
to be true.

Prometheus' main distinguishing features as compared to other monitoring systems are:

- a **multi-dimensional** data model (timeseries defined by metric name and set of key/value dimensions)
- a **flexible query language** to leverage this dimensionality
- no dependency on distributed storage; **single server nodes are autonomous**
- timeseries collection happens via a **pull model** over HTTP
- **pushing timeseries** is supported via an intermediary gateway
- targets are discovered via **service discovery** or **static configuration**
- multiple modes of **graphing and dashboarding support**
- support for hierarchical and horizontal **federation**

## Architecture overview

![](https://cdn.rawgit.com/prometheus/prometheus/c34257d069c630685da35bcef084632ffd5d6209/documentation/images/architecture.svg)

## Install

There are various ways of installing Prometheus.

### Precompiled binaries

Precompiled binaries for released versions are available in the
[*download* section](https://prometheus.io/download/)
on [prometheus.io](https://prometheus.io). Using the latest production release binary
is the recommended way of installing Prometheus.
See the [Installing](https://prometheus.io/docs/introduction/install/)
chapter in the documentation for all the details.

Debian packages [are available](https://packages.debian.org/sid/net/prometheus).

### Docker images

Docker images are available on [Quay.io](https://quay.io/repository/prometheus/prometheus).

You can launch a Prometheus container for trying it out with

    $ docker run --name prometheus -d -p 127.0.0.1:9090:9090 quay.io/prometheus/prometheus

Prometheus will now be reachable at http://localhost:9090/.

### Building from source

To build Prometheus from the source code yourself you need to have a working
Go environment with [version 1.10 or greater installed](http://golang.org/doc/install).

You can directly use the `go` tool to download and install the `prometheus`
and `promtool` binaries into your `GOPATH`:

    $ go get github.com/prometheus/prometheus/cmd/...
    $ prometheus --config.file=your_config.yml

You can also clone the repository yourself and build using `make`:

    $ mkdir -p $GOPATH/src/github.com/prometheus
    $ cd $GOPATH/src/github.com/prometheus
    $ git clone https://github.com/prometheus/prometheus.git
    $ cd prometheus
    $ make build
    $ ./prometheus --config.file=your_config.yml

The Makefile provides several targets:

  * *build*: build the `prometheus` and `promtool` binaries
  * *test*: run the tests
  * *test-short*: run the short tests
  * *format*: format the source code
  * *vet*: check the source code for common errors
  * *assets*: rebuild the static assets
  * *docker*: build a docker container for the current `HEAD`

## More information

  * The source code is periodically indexed: [Prometheus Core](http://godoc.org/github.com/prometheus/prometheus).
  * You will find a Travis CI configuration in `.travis.yml`.
  * See the [Community page](https://prometheus.io/community) for how to reach the Prometheus developers and users on various communication channels.

## Contributing

Refer to [CONTRIBUTING.md](https://github.com/prometheus/prometheus/blob/master/CONTRIBUTING.md)

## License

Apache License 2.0, see [LICENSE](https://github.com/prometheus/prometheus/blob/master/LICENSE).


[travis]: https://travis-ci.org/prometheus/prometheus
[hub]: https://hub.docker.com/r/prom/prometheus/
[circleci]: https://circleci.com/gh/prometheus/prometheus
[quay]: https://quay.io/repository/prometheus/prometheus
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

oauth2 package contains a client implementation for OAuth 2.0 spec.

## Installation

~~~~
go get golang.org/x/oauth2
~~~~

See godoc for further documentation and examples.

* [godoc.org/golang.org/x/oauth2](http://godoc.org/golang.org/x/oauth2)
* [godoc.org/golang.org/x/oauth2/google](http://godoc.org/golang.org/x/oauth2/google)


## App Engine

In change 96e89be (March 2015) we removed the `oauth2.Context2` type in favor
of the [`context.Context`](https://golang.org/x/net/context#Context) type from
the `golang.org/x/net/context` package

This means its no longer possible to use the "Classic App Engine"
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
# Kingpin - A Go (golang) command line and flag parser
[![](https://godoc.org/github.com/alecthomas/kingpin?status.svg)](http://godoc.org/github.com/alecthomas/kingpin) [![Build Status](https://travis-ci.org/alecthomas/kingpin.svg?branch=master)](https://travis-ci.org/alecthomas/kingpin) [![Gitter chat](https://badges.gitter.im/alecthomas.png)](https://gitter.im/alecthomas/Lobby)



<!-- MarkdownTOC -->

- [Overview](#overview)
- [Features](#features)
- [User-visible changes between v1 and v2](#user-visible-changes-between-v1-and-v2)
  - [Flags can be used at any point after their definition.](#flags-can-be-used-at-any-point-after-their-definition)
  - [Short flags can be combined with their parameters](#short-flags-can-be-combined-with-their-parameters)
- [API changes between v1 and v2](#api-changes-between-v1-and-v2)
- [Versions](#versions)
  - [V2 is the current stable version](#v2-is-the-current-stable-version)
  - [V1 is the OLD stable version](#v1-is-the-old-stable-version)
- [Change History](#change-history)
- [Examples](#examples)
  - [Simple Example](#simple-example)
  - [Complex Example](#complex-example)
- [Reference Documentation](#reference-documentation)
  - [Displaying errors and usage information](#displaying-errors-and-usage-information)
  - [Sub-commands](#sub-commands)
  - [Custom Parsers](#custom-parsers)
  - [Repeatable flags](#repeatable-flags)
  - [Boolean Values](#boolean-values)
  - [Default Values](#default-values)
  - [Place-holders in Help](#place-holders-in-help)
  - [Consuming all remaining arguments](#consuming-all-remaining-arguments)
  - [Bash/ZSH Shell Completion](#bashzsh-shell-completion)
  - [Supporting -h for help](#supporting--h-for-help)
  - [Custom help](#custom-help)

<!-- /MarkdownTOC -->

## Overview

Kingpin is a [fluent-style](http://en.wikipedia.org/wiki/Fluent_interface),
type-safe command-line parser. It supports flags, nested commands, and
positional arguments.

Install it with:

    $ go get gopkg.in/alecthomas/kingpin.v2

It looks like this:

```go
var (
  verbose = kingpin.Flag("verbose", "Verbose mode.").Short('v').Bool()
  name    = kingpin.Arg("name", "Name of user.").Required().String()
)

func main() {
  kingpin.Parse()
  fmt.Printf("%v, %s\n", *verbose, *name)
}
```

More [examples](https://github.com/alecthomas/kingpin/tree/master/_examples) are available.

Second to parsing, providing the user with useful help is probably the most
important thing a command-line parser does. Kingpin tries to provide detailed
contextual help if `--help` is encountered at any point in the command line
(excluding after `--`).

## Features

- Help output that isn't as ugly as sin.
- Fully [customisable help](#custom-help), via Go templates.
- Parsed, type-safe flags (`kingpin.Flag("f", "help").Int()`)
- Parsed, type-safe positional arguments (`kingpin.Arg("a", "help").Int()`).
- Parsed, type-safe, arbitrarily deep commands (`kingpin.Command("c", "help")`).
- Support for required flags and required positional arguments (`kingpin.Flag("f", "").Required().Int()`).
- Support for arbitrarily nested default commands (`command.Default()`).
- Callbacks per command, flag and argument (`kingpin.Command("c", "").Action(myAction)`).
- POSIX-style short flag combining (`-a -b` -> `-ab`).
- Short-flag+parameter combining (`-a parm` -> `-aparm`).
- Read command-line from files (`@<file>`).
- Automatically generate man pages (`--help-man`).

## User-visible changes between v1 and v2

### Flags can be used at any point after their definition.

Flags can be specified at any point after their definition, not just
*immediately after their associated command*. From the chat example below, the
following used to be required:

```
$ chat --server=chat.server.com:8080 post --image=~/Downloads/owls.jpg pics
```

But the following will now work:

```
$ chat post --server=chat.server.com:8080 --image=~/Downloads/owls.jpg pics
```

### Short flags can be combined with their parameters

Previously, if a short flag was used, any argument to that flag would have to
be separated by a space. That is no longer the case.

## API changes between v1 and v2

- `ParseWithFileExpansion()` is gone. The new parser directly supports expanding `@<file>`.
- Added `FatalUsage()` and `FatalUsageContext()` for displaying an error + usage and terminating.
- `Dispatch()` renamed to `Action()`.
- Added `ParseContext()` for parsing a command line into its intermediate context form without executing.
- Added `Terminate()` function to override the termination function.
- Added `UsageForContextWithTemplate()` for printing usage via a custom template.
- Added `UsageTemplate()` for overriding the default template to use. Two templates are included:
    1. `DefaultUsageTemplate` - default template.
    2. `CompactUsageTemplate` - compact command template for larger applications.

## Versions

Kingpin uses [gopkg.in](https://gopkg.in/alecthomas/kingpin) for versioning.

The current stable version is [gopkg.in/alecthomas/kingpin.v2](https://gopkg.in/alecthomas/kingpin.v2). The previous version, [gopkg.in/alecthomas/kingpin.v1](https://gopkg.in/alecthomas/kingpin.v1), is deprecated and in maintenance mode.

### [V2](https://gopkg.in/alecthomas/kingpin.v2) is the current stable version

Installation:

```sh
$ go get gopkg.in/alecthomas/kingpin.v2
```

### [V1](https://gopkg.in/alecthomas/kingpin.v1) is the OLD stable version

Installation:

```sh
$ go get gopkg.in/alecthomas/kingpin.v1
```

## Change History

- *2015-09-19* -- Stable v2.1.0 release.
    - Added `command.Default()` to specify a default command to use if no other
      command matches. This allows for convenient user shortcuts.
    - Exposed `HelpFlag` and `VersionFlag` for further customisation.
    - `Action()` and `PreAction()` added and both now support an arbitrary
      number of callbacks.
    - `kingpin.SeparateOptionalFlagsUsageTemplate`.
    - `--help-long` and `--help-man` (hidden by default) flags.
    - Flags are "interspersed" by default, but can be disabled with `app.Interspersed(false)`.
    - Added flags for all simple builtin types (int8, uint16, etc.) and slice variants.
    - Use `app.Writer(os.Writer)` to specify the default writer for all output functions.
    - Dropped `os.Writer` prefix from all printf-like functions.

- *2015-05-22* -- Stable v2.0.0 release.
    - Initial stable release of v2.0.0.
    - Fully supports interspersed flags, commands and arguments.
    - Flags can be present at any point after their logical definition.
    - Application.Parse() terminates if commands are present and a command is not parsed.
    - Dispatch() -> Action().
    - Actions are dispatched after all values are populated.
    - Override termination function (defaults to os.Exit).
    - Override output stream (defaults to os.Stderr).
    - Templatised usage help, with default and compact templates.
    - Make error/usage functions more consistent.
    - Support argument expansion from files by default (with @<file>).
    - Fully public data model is available via .Model().
    - Parser has been completely refactored.
    - Parsing and execution has been split into distinct stages.
    - Use `go generate` to generate repeated flags.
    - Support combined short-flag+argument: -fARG.

- *2015-01-23* -- Stable v1.3.4 release.
    - Support "--" for separating flags from positional arguments.
    - Support loading flags from files (ParseWithFileExpansion()). Use @FILE as an argument.
    - Add post-app and post-cmd validation hooks. This allows arbitrary validation to be added.
    - A bunch of improvements to help usage and formatting.
    - Support arbitrarily nested sub-commands.

- *2014-07-08* -- Stable v1.2.0 release.
    - Pass any value through to `Strings()` when final argument.
      Allows for values that look like flags to be processed.
    - Allow `--help` to be used with commands.
    - Support `Hidden()` flags.
    - Parser for [units.Base2Bytes](https://github.com/alecthomas/units)
      type. Allows for flags like `--ram=512MB` or `--ram=1GB`.
    - Add an `Enum()` value, allowing only one of a set of values
      to be selected. eg. `Flag(...).Enum("debug", "info", "warning")`.

- *2014-06-27* -- Stable v1.1.0 release.
    - Bug fixes.
    - Always return an error (rather than panicing) when misconfigured.
    - `OpenFile(flag, perm)` value type added, for finer control over opening files.
    - Significantly improved usage formatting.

- *2014-06-19* -- Stable v1.0.0 release.
    - Support [cumulative positional](#consuming-all-remaining-arguments) arguments.
    - Return error rather than panic when there are fatal errors not caught by
      the type system. eg. when a default value is invalid.
    - Use gokpg.in.

- *2014-06-10* -- Place-holder streamlining.
    - Renamed `MetaVar` to `PlaceHolder`.
    - Removed `MetaVarFromDefault`. Kingpin now uses [heuristics](#place-holders-in-help)
      to determine what to display.

## Examples

### Simple Example

Kingpin can be used for simple flag+arg applications like so:

```
$ ping --help
usage: ping [<flags>] <ip> [<count>]

Flags:
  --debug            Enable debug mode.
  --help             Show help.
  -t, --timeout=5s   Timeout waiting for ping.

Args:
  <ip>        IP address to ping.
  [<count>]   Number of packets to send
$ ping 1.2.3.4 5
Would ping: 1.2.3.4 with timeout 5s and count 0
```

From the following source:

```go
package main

import (
  "fmt"

  "gopkg.in/alecthomas/kingpin.v2"
)

var (
  debug   = kingpin.Flag("debug", "Enable debug mode.").Bool()
  timeout = kingpin.Flag("timeout", "Timeout waiting for ping.").Default("5s").OverrideDefaultFromEnvar("PING_TIMEOUT").Short('t').Duration()
  ip      = kingpin.Arg("ip", "IP address to ping.").Required().IP()
  count   = kingpin.Arg("count", "Number of packets to send").Int()
)

func main() {
  kingpin.Version("0.0.1")
  kingpin.Parse()
  fmt.Printf("Would ping: %s with timeout %s and count %d\n", *ip, *timeout, *count)
}
```

### Complex Example

Kingpin can also produce complex command-line applications with global flags,
subcommands, and per-subcommand flags, like this:

```
$ chat --help
usage: chat [<flags>] <command> [<flags>] [<args> ...]

A command-line chat application.

Flags:
  --help              Show help.
  --debug             Enable debug mode.
  --server=127.0.0.1  Server address.

Commands:
  help [<command>]
    Show help for a command.

  register <nick> <name>
    Register a new user.

  post [<flags>] <channel> [<text>]
    Post a message to a channel.

$ chat help post
usage: chat [<flags>] post [<flags>] <channel> [<text>]

Post a message to a channel.

Flags:
  --image=IMAGE  Image to post.

Args:
  <channel>  Channel to post to.
  [<text>]   Text to post.

$ chat post --image=~/Downloads/owls.jpg pics
...
```

From this code:

```go
package main

import (
  "os"
  "strings"
  "gopkg.in/alecthomas/kingpin.v2"
)

var (
  app      = kingpin.New("chat", "A command-line chat application.")
  debug    = app.Flag("debug", "Enable debug mode.").Bool()
  serverIP = app.Flag("server", "Server address.").Default("127.0.0.1").IP()

  register     = app.Command("register", "Register a new user.")
  registerNick = register.Arg("nick", "Nickname for user.").Required().String()
  registerName = register.Arg("name", "Name of user.").Required().String()

  post        = app.Command("post", "Post a message to a channel.")
  postImage   = post.Flag("image", "Image to post.").File()
  postChannel = post.Arg("channel", "Channel to post to.").Required().String()
  postText    = post.Arg("text", "Text to post.").Strings()
)

func main() {
  switch kingpin.MustParse(app.Parse(os.Args[1:])) {
  // Register user
  case register.FullCommand():
    println(*registerNick)

  // Post message
  case post.FullCommand():
    if *postImage != nil {
    }
    text := strings.Join(*postText, " ")
    println("Post:", text)
  }
}
```

## Reference Documentation

### Displaying errors and usage information

Kingpin exports a set of functions to provide consistent errors and usage
information to the user.

Error messages look something like this:

    <app>: error: <message>

The functions on `Application` are:

Function | Purpose
---------|--------------
`Errorf(format, args)` | Display a printf formatted error to the user.
`Fatalf(format, args)` | As with Errorf, but also call the termination handler.
`FatalUsage(format, args)` | As with Fatalf, but also print contextual usage information.
`FatalUsageContext(context, format, args)` | As with Fatalf, but also print contextual usage information from a `ParseContext`.
`FatalIfError(err, format, args)` | Conditionally print an error prefixed with format+args, then call the termination handler

There are equivalent global functions in the kingpin namespace for the default
`kingpin.CommandLine` instance.

### Sub-commands

Kingpin supports nested sub-commands, with separate flag and positional
arguments per sub-command. Note that positional arguments may only occur after
sub-commands.

For example:

```go
var (
  deleteCommand     = kingpin.Command("delete", "Delete an object.")
  deleteUserCommand = deleteCommand.Command("user", "Delete a user.")
  deleteUserUIDFlag = deleteUserCommand.Flag("uid", "Delete user by UID rather than username.")
  deleteUserUsername = deleteUserCommand.Arg("username", "Username to delete.")
  deletePostCommand = deleteCommand.Command("post", "Delete a post.")
)

func main() {
  switch kingpin.Parse() {
  case "delete user":
  case "delete post":
  }
}
```

### Custom Parsers

Kingpin supports both flag and positional argument parsers for converting to
Go types. For example, some included parsers are `Int()`, `Float()`,
`Duration()` and `ExistingFile()` (see [parsers.go](./parsers.go) for a complete list of included parsers).

Parsers conform to Go's [`flag.Value`](http://godoc.org/flag#Value)
interface, so any existing implementations will work.

For example, a parser for accumulating HTTP header values might look like this:

```go
type HTTPHeaderValue http.Header

func (h *HTTPHeaderValue) Set(value string) error {
  parts := strings.SplitN(value, ":", 2)
  if len(parts) != 2 {
    return fmt.Errorf("expected HEADER:VALUE got '%s'", value)
  }
  (*http.Header)(h).Add(parts[0], parts[1])
  return nil
}

func (h *HTTPHeaderValue) String() string {
  return ""
}
```

As a convenience, I would recommend something like this:

```go
func HTTPHeader(s Settings) (target *http.Header) {
  target = &http.Header{}
  s.SetValue((*HTTPHeaderValue)(target))
  return
}
```

You would use it like so:

```go
headers = HTTPHeader(kingpin.Flag("header", "Add a HTTP header to the request.").Short('H'))
```

### Repeatable flags

Depending on the `Value` they hold, some flags may be repeated. The
`IsCumulative() bool` function on `Value` tells if it's safe to call `Set()`
multiple times or if an error should be raised if several values are passed.

The built-in `Value`s returning slices and maps, as well as `Counter` are
examples of `Value`s that make a flag repeatable.

### Boolean values

Boolean values are uniquely managed by Kingpin. Each boolean flag will have a negative complement:
`--<name>` and `--no-<name>`.

### Default Values

The default value is the zero value for a type. This can be overridden with
the `Default(value...)` function on flags and arguments. This function accepts
one or several strings, which are parsed by the value itself, so they *must*
be compliant with the format expected.

### Place-holders in Help

The place-holder value for a flag is the value used in the help to describe
the value of a non-boolean flag.

The value provided to PlaceHolder() is used if provided, then the value
provided by Default() if provided, then finally the capitalised flag name is
used.

Here are some examples of flags with various permutations:

    --name=NAME           // Flag(...).String()
    --name="Harry"        // Flag(...).Default("Harry").String()
    --name=FULL-NAME      // flag(...).PlaceHolder("FULL-NAME").Default("Harry").String()

### Consuming all remaining arguments

A common command-line idiom is to use all remaining arguments for some
purpose. eg. The following command accepts an arbitrary number of
IP addresses as positional arguments:

    ./cmd ping 10.1.1.1 192.168.1.1

Such arguments are similar to [repeatable flags](#repeatable-flags), but for
arguments. Therefore they use the same `IsCumulative() bool` function on the
underlying `Value`, so the built-in `Value`s for which the `Set()` function
can be called several times will consume multiple arguments.

To implement the above example with a custom `Value`, we might do something
like this:

```go
type ipList []net.IP

func (i *ipList) Set(value string) error {
  if ip := net.ParseIP(value); ip == nil {
    return fmt.Errorf("'%s' is not an IP address", value)
  } else {
    *i = append(*i, ip)
    return nil
  }
}

func (i *ipList) String() string {
  return ""
}

func (i *ipList) IsCumulative() bool {
  return true
}

func IPList(s Settings) (target *[]net.IP) {
  target = new([]net.IP)
  s.SetValue((*ipList)(target))
  return
}
```

And use it like so:

```go
ips := IPList(kingpin.Arg("ips", "IP addresses to ping."))
```

### Bash/ZSH Shell Completion

By default, all flags and commands/subcommands generate completions 
internally.

Out of the box, CLI tools using kingpin should be able to take advantage 
of completion hinting for flags and commands. By specifying 
`--completion-bash` as the first argument, your CLI tool will show 
possible subcommands. By ending your argv with `--`, hints for flags 
will be shown.

To allow your end users to take advantage you must package a 
`/etc/bash_completion.d` script with your distribution (or the equivalent 
for your target platform/shell). An alternative is to instruct your end 
user to source a script from their `bash_profile` (or equivalent).

Fortunately Kingpin makes it easy to generate or source a script for use
with end users shells. `./yourtool --completion-script-bash` and 
`./yourtool --completion-script-zsh` will generate these scripts for you.

**Installation by Package**

For the best user experience, you should bundle your pre-created 
completion script with your CLI tool and install it inside 
`/etc/bash_completion.d` (or equivalent). A good suggestion is to add 
this as an automated step to your build pipeline, in the implementation 
is improved for bug fixed.

**Installation by `bash_profile`**

Alternatively, instruct your users to add an additional statement to 
their `bash_profile` (or equivalent):

```
eval "$(your-cli-tool --completion-script-bash)"
```

Or for ZSH

```
eval "$(your-cli-tool --completion-script-zsh)"
```

#### Additional API
To provide more flexibility, a completion option API has been
exposed for flags to allow user defined completion options, to extend
completions further than just EnumVar/Enum. 


**Provide Static Options**

When using an `Enum` or `EnumVar`, users are limited to only the options 
given. Maybe we wish to hint possible options to the user, but also 
allow them to provide their own custom option. `HintOptions` gives
this functionality to flags.

```
app := kingpin.New("completion", "My application with bash completion.")
app.Flag("port", "Provide a port to connect to").
    Required().
    HintOptions("80", "443", "8080").
    IntVar(&c.port)
```

**Provide Dynamic Options**
Consider the case that you needed to read a local database or a file to 
provide suggestions. You can dynamically generate the options

```
func listHosts() []string {
  // Provide a dynamic list of hosts from a hosts file or otherwise
  // for bash completion. In this example we simply return static slice.

  // You could use this functionality to reach into a hosts file to provide
  // completion for a list of known hosts.
  return []string{"sshhost.example", "webhost.example", "ftphost.example"}
}

app := kingpin.New("completion", "My application with bash completion.")
app.Flag("flag-1", "").HintAction(listHosts).String()
```

**EnumVar/Enum**
When using `Enum` or `EnumVar`, any provided options will be automatically
used for bash autocompletion. However, if you wish to provide a subset or 
different options, you can use `HintOptions` or `HintAction` which will override
the default completion options for `Enum`/`EnumVar`.


**Examples**
You can see an in depth example of the completion API within 
`examples/completion/main.go`


### Supporting -h for help

`kingpin.CommandLine.HelpFlag.Short('h')`

### Custom help

Kingpin v2 supports templatised help using the text/template library (actually, [a fork](https://github.com/alecthomas/template)).

You can specify the template to use with the [Application.UsageTemplate()](http://godoc.org/gopkg.in/alecthomas/kingpin.v2#Application.UsageTemplate) function.

There are four included templates: `kingpin.DefaultUsageTemplate` is the default,
`kingpin.CompactUsageTemplate` provides a more compact representation for more complex command-line structures,
`kingpin.SeparateOptionalFlagsUsageTemplate` looks like the default template, but splits required
and optional command flags into separate lists, and `kingpin.ManPageTemplate` is used to generate man pages.

See the above templates for examples of usage, and the the function [UsageForContextWithTemplate()](https://github.com/alecthomas/kingpin/blob/master/usage.go#L198) method for details on the context.

#### Default help template

```
$ go run ./examples/curl/curl.go --help
usage: curl [<flags>] <command> [<args> ...]

An example implementation of curl.

Flags:
  --help            Show help.
  -t, --timeout=5s  Set connection timeout.
  -H, --headers=HEADER=VALUE
                    Add HTTP headers to the request.

Commands:
  help [<command>...]
    Show help.

  get url <url>
    Retrieve a URL.

  get file <file>
    Retrieve a file.

  post [<flags>] <url>
    POST a resource.
```

#### Compact help template

```
$ go run ./examples/curl/curl.go --help
usage: curl [<flags>] <command> [<args> ...]

An example implementation of curl.

Flags:
  --help            Show help.
  -t, --timeout=5s  Set connection timeout.
  -H, --headers=HEADER=VALUE
                    Add HTTP headers to the request.

Commands:
  help [<command>...]
  get [<flags>]
    url <url>
    file <file>
  post [<flags>] <url>
```
# File system notifications for Go

[![GoDoc](https://godoc.org/github.com/fsnotify/fsnotify?status.svg)](https://godoc.org/github.com/fsnotify/fsnotify) [![Go Report Card](https://goreportcard.com/badge/github.com/fsnotify/fsnotify)](https://goreportcard.com/report/github.com/fsnotify/fsnotify) [![Coverage](http://gocover.io/_badge/github.com/fsnotify/fsnotify)](http://gocover.io/github.com/fsnotify/fsnotify) 

fsnotify utilizes [golang.org/x/sys](https://godoc.org/golang.org/x/sys) rather than `syscall` from the standard library. Ensure you have the latest version installed by running:

```console
go get -u golang.org/x/sys/...
```

Cross platform: Windows, Linux, BSD and OS X.

|Adapter   |OS        |Status    |
|----------|----------|----------|
|inotify   |Linux 2.6.27 or later, Android\*|Supported [![Build Status](https://travis-ci.org/fsnotify/fsnotify.svg?branch=master)](https://travis-ci.org/fsnotify/fsnotify)|
|kqueue    |BSD, OS X, iOS\*|Supported [![Build Status](https://travis-ci.org/fsnotify/fsnotify.svg?branch=master)](https://travis-ci.org/fsnotify/fsnotify)|
|ReadDirectoryChangesW|Windows|Supported [![Build status](https://ci.appveyor.com/api/projects/status/ivwjubaih4r0udeh/branch/master?svg=true)](https://ci.appveyor.com/project/NathanYoungman/fsnotify/branch/master)|
|FSEvents  |OS X          |[Planned](https://github.com/fsnotify/fsnotify/issues/11)|
|FEN       |Solaris 11    |[In Progress](https://github.com/fsnotify/fsnotify/issues/12)|
|fanotify  |Linux 2.6.37+ | |
|USN Journals |Windows    |[Maybe](https://github.com/fsnotify/fsnotify/issues/53)|
|Polling   |*All*         |[Maybe](https://github.com/fsnotify/fsnotify/issues/9)|

\* Android and iOS are untested.

Please see [the documentation](https://godoc.org/github.com/fsnotify/fsnotify) for usage. Consult the [Wiki](https://github.com/fsnotify/fsnotify/wiki) for the FAQ and further information.

## API stability

fsnotify is a fork of [howeyc/fsnotify](https://godoc.org/github.com/howeyc/fsnotify) with a new API as of v1.0. The API is based on [this design document](http://goo.gl/MrYxyA). 

All [releases](https://github.com/fsnotify/fsnotify/releases) are tagged based on [Semantic Versioning](http://semver.org/). Further API changes are [planned](https://github.com/fsnotify/fsnotify/milestones), and will be tagged with a new major revision number.

Go 1.6 supports dependencies located in the `vendor/` folder. Unless you are creating a library, it is recommended that you copy fsnotify into `vendor/github.com/fsnotify/fsnotify` within your project, and likewise for `golang.org/x/sys`.

## Contributing

Please refer to [CONTRIBUTING][] before opening an issue or pull request.

## Example

See [example_test.go](https://github.com/fsnotify/fsnotify/blob/master/example_test.go).

[contributing]: https://github.com/fsnotify/fsnotify/blob/master/CONTRIBUTING.md

## Related Projects

* [notify](https://github.com/rjeczalik/notify)
* [fsevents](https://github.com/fsnotify/fsevents)

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

# Go tracing and monitoring (Prometheus) for `net.Conn`

[![Travis Build](https://travis-ci.org/mwitkow/go-conntrack.svg)](https://travis-ci.org/mwitkow/go-conntrack)
[![Go Report Card](https://goreportcard.com/badge/github.com/mwitkow/go-conntrack)](http://goreportcard.com/report/mwitkow/go-conntrack)
[![GoDoc](http://img.shields.io/badge/GoDoc-Reference-blue.svg)](https://godoc.org/github.com/mwitkow/go-conntrack)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[Prometheus](https://prometheus.io/) monitoring and [`x/net/trace`](https://godoc.org/golang.org/x/net/trace#EventLog) tracing wrappers `net.Conn`, both inbound (`net.Listener`) and outbound (`net.Dialer`).

## Why?

Go standard library does a great job of doing "the right" things with your connections: `http.Transport` pools outbound ones, and `http.Server` sets good *Keep Alive* defaults.
However, it is still easy to get it wrong, see the excellent [*The complete guide to Go net/http timeouts*](https://blog.cloudflare.com/the-complete-guide-to-golang-net-http-timeouts/). 

That's why you should be able to monitor (using Prometheus) how many connections your Go frontend servers have inbound, and how big are the connection pools to your backends. You should also be able to inspect your connection without `ssh` and `netstat`.

![Events page with connections](https://raw.githubusercontent.com/mwitkow/go-conntrack/images/events.png)

## How to use?

All of these examples can be found in [`example/server.go`](example/server.go):

### Conntrack Dialer for HTTP DefaultClient
 
Most often people use the default `http.DefaultClient` that uses `http.DefaultTransport`. The easiest way to make sure all your outbound connections monitored and trace is:

```go
http.DefaultTransport.(*http.Transport).DialContext = conntrack.NewDialContextFunc(
    conntrack.DialWithTracing(),
    conntrack.DialWithDialer(&net.Dialer{
        Timeout:   30 * time.Second,
        KeepAlive: 30 * time.Second,
    }),
)
```

#### Dialer Name

Tracked outbound connections are organised by *dialer name* (with `default` being default). The *dialer name* is used for monitoring (`dialer_name` label) and tracing (`net.ClientConn.<dialer_name>` family). 

You can pass `conntrack.WithDialerName()` to `NewDialContextFunc` to set the name for the dialer. Moreover, you can set the *dialer name* per invocation of the dialer, by passing it in the `Context`. For example using the [`ctxhttp`](https://godoc.org/golang.org/x/net/context/ctxhttp) lib:

```go
callCtx := conntrack.DialNameToContext(parentCtx, "google")
ctxhttp.Get(callCtx, http.DefaultClient, "https://www.google.com")
```

### Conntrack Listener for HTTP Server

Tracked inbound connections are organised by *listener name* (with `default` being default). The *listener name* is used for monitoring (`listener_name` label) and tracing (`net.ServerConn.<listener_name>` family). For example, a simple `http.Server` can be instrumented like this:

```go
listener, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
listener = conntrack.NewListener(listener, 
    conntrack.TrackWithName("http"), 
    conntrack.TrackWithTracing(),
    conntrack.TrackWithTcpKeepAlive(5 * time.Minutes))
httpServer.Serve(listener) 
```

Note, the `TrackWithTcpKeepAlive`. The default `http.ListenAndServe` adds a tcp keep alive wrapper to inbound TCP connections. `conntrack.NewListener` allows you to do that without another layer of wrapping.

#### TLS server example

The standard lobrary `http.ListenAndServerTLS` does a lot to bootstrap TLS connections, including supporting HTTP2 negotiation. Unfortunately, that is hard to do if you want to provide your own `net.Listener`. That's why this repo comes with `connhelpers` package, which takes care of configuring `tls.Config` for that use case. Here's an example of use:

```go
listener, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
listener = conntrack.NewListener(listener, 
    conntrack.TrackWithName("https"), 
    conntrack.TrackWithTracing(),
    conntrack.TrackWithTcpKeepAlive(5 * time.Minutes))
tlsConfig, err := connhelpers.TlsConfigForServerCerts(*tlsCertFilePath, *tlsKeyFilePath)
tlsConfig, err = connhelpers.TlsConfigWithHttp2Enabled(tlsConfig)
tlsListener := tls.NewListener(listener, tlsConfig)
httpServer.Serve(listener) 
```

# Status

This code is used by Improbable's HTTP frontending and proxying stack for debuging and monitoring of established user connections.

Additional tooling will be added if needed, and contributions are welcome.

#License

`go-conntrack` is released under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.

lockfile
=========
Handle locking via pid files.

[![Build Status Unix][1]][2]
[![Build status Windows][3]][4]

[1]: https://secure.travis-ci.org/nightlyone/lockfile.png
[2]: https://travis-ci.org/nightlyone/lockfile
[3]: https://ci.appveyor.com/api/projects/status/7mojkmauj81uvp8u/branch/master?svg=true
[4]: https://ci.appveyor.com/project/nightlyone/lockfile/branch/master



install
-------
Install [Go 1][5], either [from source][6] or [with a prepackaged binary][7].
For Windows suport, Go 1.4 or newer is required.

Then run

	go get github.com/nightlyone/lockfile

[5]: http://golang.org
[6]: http://golang.org/doc/install/source
[7]: http://golang.org/doc/install

LICENSE
-------
BSD

documentation
-------------
[package documentation at godoc.org](http://godoc.org/github.com/nightlyone/lockfile)

install
-------------------
	go get github.com/nightlyone/lockfile


contributing
============

Contributions are welcome. Please open an issue or send me a pull request for a dedicated branch.
Make sure the git commit hooks show it works.

git commit hooks
-----------------------
enable commit hooks via

        cd .git ; rm -rf hooks; ln -s ../git-hooks hooks ; cd ..

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
[![GoDoc](https://godoc.org/github.com/go-stack/stack?status.svg)](https://godoc.org/github.com/go-stack/stack)
[![Go Report Card](https://goreportcard.com/badge/go-stack/stack)](https://goreportcard.com/report/go-stack/stack)
[![TravisCI](https://travis-ci.org/go-stack/stack.svg?branch=master)](https://travis-ci.org/go-stack/stack)
[![Coverage Status](https://coveralls.io/repos/github/go-stack/stack/badge.svg?branch=master)](https://coveralls.io/github/go-stack/stack?branch=master)

# stack

Package stack implements utilities to capture, manipulate, and format call
stacks. It provides a simpler API than package runtime.

The implementation takes care of the minutia and special cases of interpreting
the program counter (pc) values returned by runtime.Callers.

## Versioning

Package stack publishes releases via [semver](http://semver.org/) compatible Git
tags prefixed with a single 'v'. The master branch always contains the latest
release. The develop branch contains unreleased commits.

## Formatting

Package stack's types implement fmt.Formatter, which provides a simple and
flexible way to declaratively configure formatting when used with logging or
error tracking packages.

```go
func DoTheThing() {
    c := stack.Caller(0)
    log.Print(c)          // "source.go:10"
    log.Printf("%+v", c)  // "pkg/path/source.go:10"
    log.Printf("%n", c)   // "DoTheThing"

    s := stack.Trace().TrimRuntime()
    log.Print(s)          // "[source.go:15 caller.go:42 main.go:14]"
}
```

See the docs for all of the supported formatting options.
The Snappy compression format in the Go programming language.

To download and install from source:
$ go get github.com/golang/snappy

Unless otherwise noted, the Snappy-Go source files are distributed
under the BSD-style license found in the LICENSE file.



Benchmarks.

The golang/snappy benchmarks include compressing (Z) and decompressing (U) ten
or so files, the same set used by the C++ Snappy code (github.com/google/snappy
and note the "google", not "golang"). On an "Intel(R) Core(TM) i7-3770 CPU @
3.40GHz", Go's GOARCH=amd64 numbers as of 2016-05-29:

"go test -test.bench=."

_UFlat0-8         2.19GB/s ± 0%  html
_UFlat1-8         1.41GB/s ± 0%  urls
_UFlat2-8         23.5GB/s ± 2%  jpg
_UFlat3-8         1.91GB/s ± 0%  jpg_200
_UFlat4-8         14.0GB/s ± 1%  pdf
_UFlat5-8         1.97GB/s ± 0%  html4
_UFlat6-8          814MB/s ± 0%  txt1
_UFlat7-8          785MB/s ± 0%  txt2
_UFlat8-8          857MB/s ± 0%  txt3
_UFlat9-8          719MB/s ± 1%  txt4
_UFlat10-8        2.84GB/s ± 0%  pb
_UFlat11-8        1.05GB/s ± 0%  gaviota

_ZFlat0-8         1.04GB/s ± 0%  html
_ZFlat1-8          534MB/s ± 0%  urls
_ZFlat2-8         15.7GB/s ± 1%  jpg
_ZFlat3-8          740MB/s ± 3%  jpg_200
_ZFlat4-8         9.20GB/s ± 1%  pdf
_ZFlat5-8          991MB/s ± 0%  html4
_ZFlat6-8          379MB/s ± 0%  txt1
_ZFlat7-8          352MB/s ± 0%  txt2
_ZFlat8-8          396MB/s ± 1%  txt3
_ZFlat9-8          327MB/s ± 1%  txt4
_ZFlat10-8        1.33GB/s ± 1%  pb
_ZFlat11-8         605MB/s ± 1%  gaviota



"go test -test.bench=. -tags=noasm"

_UFlat0-8          621MB/s ± 2%  html
_UFlat1-8          494MB/s ± 1%  urls
_UFlat2-8         23.2GB/s ± 1%  jpg
_UFlat3-8         1.12GB/s ± 1%  jpg_200
_UFlat4-8         4.35GB/s ± 1%  pdf
_UFlat5-8          609MB/s ± 0%  html4
_UFlat6-8          296MB/s ± 0%  txt1
_UFlat7-8          288MB/s ± 0%  txt2
_UFlat8-8          309MB/s ± 1%  txt3
_UFlat9-8          280MB/s ± 1%  txt4
_UFlat10-8         753MB/s ± 0%  pb
_UFlat11-8         400MB/s ± 0%  gaviota

_ZFlat0-8          409MB/s ± 1%  html
_ZFlat1-8          250MB/s ± 1%  urls
_ZFlat2-8         12.3GB/s ± 1%  jpg
_ZFlat3-8          132MB/s ± 0%  jpg_200
_ZFlat4-8         2.92GB/s ± 0%  pdf
_ZFlat5-8          405MB/s ± 1%  html4
_ZFlat6-8          179MB/s ± 1%  txt1
_ZFlat7-8          170MB/s ± 1%  txt2
_ZFlat8-8          189MB/s ± 1%  txt3
_ZFlat9-8          164MB/s ± 1%  txt4
_ZFlat10-8         479MB/s ± 1%  pb
_ZFlat11-8         270MB/s ± 1%  gaviota



For comparison (Go's encoded output is byte-for-byte identical to C++'s), here
are the numbers from C++ Snappy's

make CXXFLAGS="-O2 -DNDEBUG -g" clean snappy_unittest.log && cat snappy_unittest.log

BM_UFlat/0     2.4GB/s  html
BM_UFlat/1     1.4GB/s  urls
BM_UFlat/2    21.8GB/s  jpg
BM_UFlat/3     1.5GB/s  jpg_200
BM_UFlat/4    13.3GB/s  pdf
BM_UFlat/5     2.1GB/s  html4
BM_UFlat/6     1.0GB/s  txt1
BM_UFlat/7   959.4MB/s  txt2
BM_UFlat/8     1.0GB/s  txt3
BM_UFlat/9   864.5MB/s  txt4
BM_UFlat/10    2.9GB/s  pb
BM_UFlat/11    1.2GB/s  gaviota

BM_ZFlat/0   944.3MB/s  html (22.31 %)
BM_ZFlat/1   501.6MB/s  urls (47.78 %)
BM_ZFlat/2    14.3GB/s  jpg (99.95 %)
BM_ZFlat/3   538.3MB/s  jpg_200 (73.00 %)
BM_ZFlat/4     8.3GB/s  pdf (83.30 %)
BM_ZFlat/5   903.5MB/s  html4 (22.52 %)
BM_ZFlat/6   336.0MB/s  txt1 (57.88 %)
BM_ZFlat/7   312.3MB/s  txt2 (61.91 %)
BM_ZFlat/8   353.1MB/s  txt3 (54.99 %)
BM_ZFlat/9   289.9MB/s  txt4 (66.26 %)
BM_ZFlat/10    1.2GB/s  pb (19.68 %)
BM_ZFlat/11  527.4MB/s  gaviota (37.72 %)
glog
====

Leveled execution logs for Go.

This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package
	http://code.google.com/p/google-glog

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
# xxhash

[![GoDoc](https://godoc.org/github.com/cespare/mph?status.svg)](https://godoc.org/github.com/cespare/xxhash)

xxhash is a Go implementation of the 64-bit
[xxHash](http://cyan4973.github.io/xxHash/) algorithm, XXH64. This is a
high-quality hashing algorithm that is much faster than anything in the Go
standard library.

The API is very small, taking its cue from the other hashing packages in the
standard library:

    $ go doc github.com/cespare/xxhash                                                                                                                                                                                              !
    package xxhash // import "github.com/cespare/xxhash"

    Package xxhash implements the 64-bit variant of xxHash (XXH64) as described
    at http://cyan4973.github.io/xxHash/.

    func New() hash.Hash64
    func Sum64(b []byte) uint64

This implementation provides a fast pure-Go implementation and an even faster
assembly implementation for amd64.

Here are some quick benchmarks comparing the pure-Go and assembly
implementations of Sum64 against another popular Go XXH64 implementation,
[github.com/OneOfOne/xxhash](https://github.com/OneOfOne/xxhash):

| input size | OneOfOne | cespare (noasm) | cespare |
| --- | --- | --- | --- |
| 5 B   |  438.34 MB/s |  596.40 MB/s |  711.11 MB/s  |
| 100 B | 3676.54 MB/s | 4301.40 MB/s | 4598.95 MB/s  |
| 4 KB  | 8128.64 MB/s | 8840.83 MB/s | 10549.72 MB/s |
| 10 MB | 7335.19 MB/s | 7736.64 MB/s | 9024.04 MB/s  |
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
A [go](http://www.golang.org) (or 'golang' for search engine friendliness) implementation of [JSON Web Tokens](http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html)

[![Build Status](https://travis-ci.org/dgrijalva/jwt-go.svg?branch=master)](https://travis-ci.org/dgrijalva/jwt-go)

**BREAKING CHANGES:*** Version 3.0.0 is here. It includes _a lot_ of changes including a few that break the API.  We've tried to break as few things as possible, so there should just be a few type signature changes.  A full list of breaking changes is available in `VERSION_HISTORY.md`.  See `MIGRATION_GUIDE.md` for more information on updating your code.

**NOTICE:** A vulnerability in JWT was [recently published](https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/).  As this library doesn't force users to validate the `alg` is what they expected, it's possible your usage is effected.  There will be an update soon to remedy this, and it will likey require backwards-incompatible changes to the API.  In the short term, please make sure your implementation verifies the `alg` is what you expect.


## What the heck is a JWT?

JWT.io has [a great introduction](https://jwt.io/introduction) to JSON Web Tokens.

In short, it's a signed JSON object that does something useful (for example, authentication).  It's commonly used for `Bearer` tokens in Oauth 2.  A token is made of three parts, separated by `.`'s.  The first two parts are JSON objects, that have been [base64url](http://tools.ietf.org/html/rfc4648) encoded.  The last part is the signature, encoded the same way.

The first part is called the header.  It contains the necessary information for verifying the last part, the signature.  For example, which encryption method was used for signing and what key was used.

The part in the middle is the interesting bit.  It's called the Claims and contains the actual stuff you care about.  Refer to [the RFC](http://self-issued.info/docs/draft-jones-json-web-token.html) for information about reserved keys and the proper way to add your own.

## What's in the box?

This library supports the parsing and verification as well as the generation and signing of JWTs.  Current supported signing algorithms are HMAC SHA, RSA, RSA-PSS, and ECDSA, though hooks are present for adding your own.

## Examples

See [the project documentation](https://godoc.org/github.com/dgrijalva/jwt-go) for examples of usage:

* [Simple example of parsing and validating a token](https://godoc.org/github.com/dgrijalva/jwt-go#example-Parse--Hmac)
* [Simple example of building and signing a token](https://godoc.org/github.com/dgrijalva/jwt-go#example-New--Hmac)
* [Directory of Examples](https://godoc.org/github.com/dgrijalva/jwt-go#pkg-examples)

## Extensions

This library publishes all the necessary components for adding your own signing methods.  Simply implement the `SigningMethod` interface and register a factory method using `RegisterSigningMethod`.  

Here's an example of an extension that integrates with the Google App Engine signing tools: https://github.com/someone1/gcp-jwt-go

## Compliance

This library was last reviewed to comply with [RTF 7519](http://www.rfc-editor.org/info/rfc7519) dated May 2015 with a few notable differences: 

* In order to protect against accidental use of [Unsecured JWTs](http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html#UnsecuredJWT), tokens using `alg=none` will only be accepted if the constant `jwt.UnsafeAllowNoneSignatureType` is provided as the key.

## Project Status & Versioning

This library is considered production ready.  Feedback and feature requests are appreciated.  The API should be considered stable.  There should be very few backwards-incompatible changes outside of major version updates (and only with good reason).

This project uses [Semantic Versioning 2.0.0](http://semver.org).  Accepted pull requests will land on `master`.  Periodically, versions will be tagged from `master`.  You can find all the releases on [the project releases page](https://github.com/dgrijalva/jwt-go/releases).

While we try to make it obvious when we make breaking changes, there isn't a great mechanism for pushing announcements out to users.  You may want to use this alternative package include: `gopkg.in/dgrijalva/jwt-go.v2`.  It will do the right thing WRT semantic versioning.

## Usage Tips

### Signing vs Encryption

A token is simply a JSON object that is signed by its author. this tells you exactly two things about the data:

* The author of the token was in the possession of the signing secret
* The data has not been modified since it was signed

It's important to know that JWT does not provide encryption, which means anyone who has access to the token can read its contents. If you need to protect (encrypt) the data, there is a companion spec, `JWE`, that provides this functionality. JWE is currently outside the scope of this library.

### Choosing a Signing Method

There are several signing methods available, and you should probably take the time to learn about the various options before choosing one.  The principal design decision is most likely going to be symmetric vs asymmetric.

Symmetric signing methods, such as HSA, use only a single secret. This is probably the simplest signing method to use since any `[]byte` can be used as a valid secret. They are also slightly computationally faster to use, though this rarely is enough to matter. Symmetric signing methods work the best when both producers and consumers of tokens are trusted, or even the same system. Since the same secret is used to both sign and validate tokens, you can't easily distribute the key for validation.

Asymmetric signing methods, such as RSA, use different keys for signing and verifying tokens. This makes it possible to produce tokens with a private key, and allow any consumer to access the public key for verification.

### JWT and OAuth

It's worth mentioning that OAuth and JWT are not the same thing. A JWT token is simply a signed JSON object. It can be used anywhere such a thing is useful. There is some confusion, though, as JWT is the most common type of bearer token used in OAuth2 authentication.

Without going too far down the rabbit hole, here's a description of the interaction of these technologies:

* OAuth is a protocol for allowing an identity provider to be separate from the service a user is logging in to.  For example, whenever you use Facebook to log into a different service (Yelp, Spotify, etc), you are using OAuth.
* OAuth defines several options for passing around authentication data. One popular method is called a "bearer token". A bearer token is simply a string that _should_ only be held by an authenticated user. Thus, simply presenting this token proves your identity. You can probably derive from here why a JWT might make a good bearer token.
* Because bearer tokens are used for authentication, it's important they're kept secret. This is why transactions that use bearer tokens typically happen over SSL.
 
## More

Documentation can be found [on godoc.org](http://godoc.org/github.com/dgrijalva/jwt-go).

The command line utility included in this project (cmd/jwt) provides a straightforward example of token creation and parsing as well as a useful tool for debugging your own integration.  You'll also find several implementation examples in to documentation.
# Gophercloud: an OpenStack SDK for Go
[![Build Status](https://travis-ci.org/gophercloud/gophercloud.svg?branch=master)](https://travis-ci.org/gophercloud/gophercloud)
[![Coverage Status](https://coveralls.io/repos/github/gophercloud/gophercloud/badge.svg?branch=master)](https://coveralls.io/github/gophercloud/gophercloud?branch=master)

Gophercloud is an OpenStack Go SDK.

## Useful links

* [Reference documentation](http://godoc.org/github.com/gophercloud/gophercloud)
* [Effective Go](https://golang.org/doc/effective_go.html)

## How to install

Before installing, you need to ensure that your [GOPATH environment variable](https://golang.org/doc/code.html#GOPATH)
is pointing to an appropriate directory where you want to install Gophercloud:

```bash
mkdir $HOME/go
export GOPATH=$HOME/go
```

To protect yourself against changes in your dependencies, we highly recommend choosing a
[dependency management solution](https://github.com/golang/go/wiki/PackageManagementTools) for
your projects, such as [godep](https://github.com/tools/godep). Once this is set up, you can install
Gophercloud as a dependency like so:

```bash
go get github.com/gophercloud/gophercloud

# Edit your code to import relevant packages from "github.com/gophercloud/gophercloud"

godep save ./...
```

This will install all the source files you need into a `Godeps/_workspace` directory, which is
referenceable from your own source files when you use the `godep go` command.

## Getting started

### Credentials

Because you'll be hitting an API, you will need to retrieve your OpenStack
credentials and either store them as environment variables or in your local Go
files. The first method is recommended because it decouples credential
information from source code, allowing you to push the latter to your version
control system without any security risk.

You will need to retrieve the following:

* username
* password
* a valid Keystone identity URL

For users that have the OpenStack dashboard installed, there's a shortcut. If
you visit the `project/access_and_security` path in Horizon and click on the
"Download OpenStack RC File" button at the top right hand corner, you will
download a bash file that exports all of your access details to environment
variables. To execute the file, run `source admin-openrc.sh` and you will be
prompted for your password.

### Authentication

Once you have access to your credentials, you can begin plugging them into
Gophercloud. The next step is authentication, and this is handled by a base
"Provider" struct. To get one, you can either pass in your credentials
explicitly, or tell Gophercloud to use environment variables:

```go
import (
  "github.com/gophercloud/gophercloud"
  "github.com/gophercloud/gophercloud/openstack"
  "github.com/gophercloud/gophercloud/openstack/utils"
)

// Option 1: Pass in the values yourself
opts := gophercloud.AuthOptions{
  IdentityEndpoint: "https://openstack.example.com:5000/v2.0",
  Username: "{username}",
  Password: "{password}",
}

// Option 2: Use a utility function to retrieve all your environment variables
opts, err := openstack.AuthOptionsFromEnv()
```

Once you have the `opts` variable, you can pass it in and get back a
`ProviderClient` struct:

```go
provider, err := openstack.AuthenticatedClient(opts)
```

The `ProviderClient` is the top-level client that all of your OpenStack services
derive from. The provider contains all of the authentication details that allow
your Go code to access the API - such as the base URL and token ID.

### Provision a server

Once we have a base Provider, we inject it as a dependency into each OpenStack
service. In order to work with the Compute API, we need a Compute service
client; which can be created like so:

```go
client, err := openstack.NewComputeV2(provider, gophercloud.EndpointOpts{
  Region: os.Getenv("OS_REGION_NAME"),
})
```

We then use this `client` for any Compute API operation we want. In our case,
we want to provision a new server - so we invoke the `Create` method and pass
in the flavor ID (hardware specification) and image ID (operating system) we're
interested in:

```go
import "github.com/gophercloud/gophercloud/openstack/compute/v2/servers"

server, err := servers.Create(client, servers.CreateOpts{
  Name:      "My new server!",
  FlavorRef: "flavor_id",
  ImageRef:  "image_id",
}).Extract()
```

The above code sample creates a new server with the parameters, and embodies the
new resource in the `server` variable (a
[`servers.Server`](http://godoc.org/github.com/gophercloud/gophercloud) struct).

## Advanced Usage

Have a look at the [FAQ](./FAQ.md) for some tips on customizing the way Gophercloud works.

## Backwards-Compatibility Guarantees

None. Vendor it and write tests covering the parts you use.

## Contributing

See the [contributing guide](./.github/CONTRIBUTING.md).

## Help and feedback

If you're struggling with something or have spotted a potential bug, feel free
to submit an issue to our [bug tracker](/issues).
# TSDB

This repository contains the new Prometheus storage layer that will be used in its 2.0 release.

A writeup of its design can be found [here](https://fabxc.org/blog/2017-04-10-writing-a-tsdb/).
# procfs

This procfs package provides functions to retrieve system, kernel and process
metrics from the pseudo-filesystem proc.

*WARNING*: This package is a work in progress. Its API may still break in
backwards-incompatible ways without warnings. Use it at your own risk.

[![GoDoc](https://godoc.org/github.com/prometheus/procfs?status.png)](https://godoc.org/github.com/prometheus/procfs)
[![Build Status](https://travis-ci.org/prometheus/procfs.svg?branch=master)](https://travis-ci.org/prometheus/procfs)
See [![go-doc](https://godoc.org/github.com/prometheus/client_golang/prometheus?status.svg)](https://godoc.org/github.com/prometheus/client_golang/prometheus).
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
# HttpRouter [![Build Status](https://travis-ci.org/julienschmidt/httprouter.png?branch=master)](https://travis-ci.org/julienschmidt/httprouter) [![Coverage](http://gocover.io/_badge/github.com/julienschmidt/httprouter?0)](http://gocover.io/github.com/julienschmidt/httprouter) [![GoDoc](http://godoc.org/github.com/julienschmidt/httprouter?status.png)](http://godoc.org/github.com/julienschmidt/httprouter)

HttpRouter is a lightweight high performance HTTP request router
(also called *multiplexer* or just *mux* for short) for [Go](http://golang.org/).

In contrast to the [default mux](http://golang.org/pkg/net/http/#ServeMux) of Go's net/http package, this router supports
variables in the routing pattern and matches against the request method.
It also scales better.

The router is optimized for high performance and a small memory footprint.
It scales well even with very long paths and a large number of routes.
A compressing dynamic trie (radix tree) structure is used for efficient matching.

## Features
**Only explicit matches:** With other routers, like [http.ServeMux](http://golang.org/pkg/net/http/#ServeMux),
a requested URL path could match multiple patterns. Therefore they have some
awkward pattern priority rules, like *longest match* or *first registered,
first matched*. By design of this router, a request can only match exactly one
or no route. As a result, there are also no unintended matches, which makes it
great for SEO and improves the user experience.

**Stop caring about trailing slashes:** Choose the URL style you like, the
router automatically redirects the client if a trailing slash is missing or if
there is one extra. Of course it only does so, if the new path has a handler.
If you don't like it, you can [turn off this behavior](http://godoc.org/github.com/julienschmidt/httprouter#Router.RedirectTrailingSlash).

**Path auto-correction:** Besides detecting the missing or additional trailing
slash at no extra cost, the router can also fix wrong cases and remove
superfluous path elements (like `../` or `//`).
Is [CAPTAIN CAPS LOCK](http://www.urbandictionary.com/define.php?term=Captain+Caps+Lock) one of your users?
HttpRouter can help him by making a case-insensitive look-up and redirecting him
to the correct URL.

**Parameters in your routing pattern:** Stop parsing the requested URL path,
just give the path segment a name and the router delivers the dynamic value to
you. Because of the design of the router, path parameters are very cheap.

**Zero Garbage:** The matching and dispatching process generates zero bytes of
garbage. In fact, the only heap allocations that are made, is by building the
slice of the key-value pairs for path parameters. If the request path contains
no parameters, not a single heap allocation is necessary.

**Best Performance:** [Benchmarks speak for themselves](https://github.com/julienschmidt/go-http-routing-benchmark).
See below for technical details of the implementation.

**No more server crashes:** You can set a [Panic handler](http://godoc.org/github.com/julienschmidt/httprouter#Router.PanicHandler) to deal with panics
occurring during handling a HTTP request. The router then recovers and lets the
PanicHandler log what happened and deliver a nice error page.

Of course you can also set **custom [NotFound](http://godoc.org/github.com/julienschmidt/httprouter#Router.NotFound) and  [MethodNotAllowed](http://godoc.org/github.com/julienschmidt/httprouter#Router.MethodNotAllowed) handlers** and [**serve static files**](http://godoc.org/github.com/julienschmidt/httprouter#Router.ServeFiles).

## Usage
This is just a quick introduction, view the [GoDoc](http://godoc.org/github.com/julienschmidt/httprouter) for details.

Let's start with a trivial example:
```go
package main

import (
    "fmt"
    "github.com/julienschmidt/httprouter"
    "net/http"
    "log"
)

func Index(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Welcome!\n")
}

func Hello(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
    fmt.Fprintf(w, "hello, %s!\n", ps.ByName("name"))
}

func main() {
    router := httprouter.New()
    router.GET("/", Index)
    router.GET("/hello/:name", Hello)

    log.Fatal(http.ListenAndServe(":8080", router))
}
```

### Named parameters
As you can see, `:name` is a *named parameter*.
The values are accessible via `httprouter.Params`, which is just a slice of `httprouter.Param`s.
You can get the value of a parameter either by its index in the slice, or by using the `ByName(name)` method:
`:name` can be retrived by `ByName("name")`.

Named parameters only match a single path segment:
```
Pattern: /user/:user

 /user/gordon              match
 /user/you                 match
 /user/gordon/profile      no match
 /user/                    no match
```

**Note:** Since this router has only explicit matches, you can not register static routes and parameters for the same path segment. For example you can not register the patterns `/user/new` and `/user/:user` for the same request method at the same time. The routing of different request methods is independent from each other.

### Catch-All parameters
The second type are *catch-all* parameters and have the form `*name`.
Like the name suggests, they match everything.
Therefore they must always be at the **end** of the pattern:
```
Pattern: /src/*filepath

 /src/                     match
 /src/somefile.go          match
 /src/subdir/somefile.go   match
```

## How does it work?
The router relies on a tree structure which makes heavy use of *common prefixes*,
it is basically a *compact* [*prefix tree*](http://en.wikipedia.org/wiki/Trie)
(or just [*Radix tree*](http://en.wikipedia.org/wiki/Radix_tree)).
Nodes with a common prefix also share a common parent. Here is a short example
what the routing tree for the `GET` request method could look like:

```
Priority   Path             Handle
9          \                *<1>
3          ├s               nil
2          |├earch\         *<2>
1          |└upport\        *<3>
2          ├blog\           *<4>
1          |    └:post      nil
1          |         └\     *<5>
2          ├about-us\       *<6>
1          |        └team\  *<7>
1          └contact\        *<8>
```
Every `*<num>` represents the memory address of a handler function (a pointer).
If you follow a path trough the tree from the root to the leaf, you get the
complete route path, e.g `\blog\:post\`, where `:post` is just a placeholder
([*parameter*](#named-parameters)) for an actual post name. Unlike hash-maps, a
tree structure also allows us to use dynamic parts like the `:post` parameter,
since we actually match against the routing patterns instead of just comparing
hashes. [As benchmarks show](https://github.com/julienschmidt/go-http-routing-benchmark),
this works very well and efficient.

Since URL paths have a hierarchical structure and make use only of a limited set
of characters (byte values), it is very likely that there are a lot of common
prefixes. This allows us to easily reduce the routing into ever smaller problems.
Moreover the router manages a separate tree for every request method.
For one thing it is more space efficient than holding a method->handle map in
every single node, for another thing is also allows us to greatly reduce the
routing problem before even starting the look-up in the prefix-tree.

For even better scalability, the child nodes on each tree level are ordered by
priority, where the priority is just the number of handles registered in sub
nodes (children, grandchildren, and so on..).
This helps in two ways:

1. Nodes which are part of the most routing paths are evaluated first. This
helps to make as much routes as possible to be reachable as fast as possible.
2. It is some sort of cost compensation. The longest reachable path (highest
cost) can always be evaluated first. The following scheme visualizes the tree
structure. Nodes are evaluated from top to bottom and from left to right.

```
├------------
├---------
├-----
├----
├--
├--
└-
```


## Why doesn't this work with http.Handler?
**It does!** The router itself implements the http.Handler interface.
Moreover the router provides convenient [adapters for http.Handler](http://godoc.org/github.com/julienschmidt/httprouter#Router.Handler)s and [http.HandlerFunc](http://godoc.org/github.com/julienschmidt/httprouter#Router.HandlerFunc)s
which allows them to be used as a [httprouter.Handle](http://godoc.org/github.com/julienschmidt/httprouter#Router.Handle) when registering a route.
The only disadvantage is, that no parameter values can be retrieved when a
http.Handler or http.HandlerFunc is used, since there is no efficient way to
pass the values with the existing function parameters.
Therefore [httprouter.Handle](http://godoc.org/github.com/julienschmidt/httprouter#Router.Handle) has a third function parameter.

Just try it out for yourself, the usage of HttpRouter is very straightforward. The package is compact and minimalistic, but also probably one of the easiest routers to set up.


## Where can I find Middleware *X*?
This package just provides a very efficient request router with a few extra
features. The router is just a [http.Handler](http://golang.org/pkg/net/http/#Handler),
you can chain any http.Handler compatible middleware before the router,
for example the [Gorilla handlers](http://www.gorillatoolkit.org/pkg/handlers).
Or you could [just write your own](http://justinas.org/writing-http-middleware-in-go/),
it's very easy!

Alternatively, you could try [a web framework based on HttpRouter](#web-frameworks-based-on-httprouter).

### Multi-domain / Sub-domains
Here is a quick example: Does your server serve multiple domains / hosts?
You want to use sub-domains?
Define a router per host!
```go
// We need an object that implements the http.Handler interface.
// Therefore we need a type for which we implement the ServeHTTP method.
// We just use a map here, in which we map host names (with port) to http.Handlers
type HostSwitch map[string]http.Handler

// Implement the ServerHTTP method on our new type
func (hs HostSwitch) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// Check if a http.Handler is registered for the given host.
	// If yes, use it to handle the request.
	if handler := hs[r.Host]; handler != nil {
		handler.ServeHTTP(w, r)
	} else {
		// Handle host names for wich no handler is registered
		http.Error(w, "Forbidden", 403) // Or Redirect?
	}
}

func main() {
	// Initialize a router as usual
	router := httprouter.New()
	router.GET("/", Index)
	router.GET("/hello/:name", Hello)

	// Make a new HostSwitch and insert the router (our http handler)
	// for example.com and port 12345
	hs := make(HostSwitch)
	hs["example.com:12345"] = router

	// Use the HostSwitch to listen and serve on port 12345
	log.Fatal(http.ListenAndServe(":12345", hs))
}
```

### Basic Authentication
Another quick example: Basic Authentification (RFC 2617) for handles:

```go
package main

import (
    "bytes"
    "encoding/base64"
    "fmt"
    "github.com/julienschmidt/httprouter"
    "net/http"
    "log"
    "strings"
)

func BasicAuth(h httprouter.Handle, user, pass []byte) httprouter.Handle {
	return func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
		const basicAuthPrefix string = "Basic "

		// Get the Basic Authentication credentials
		auth := r.Header.Get("Authorization")
		if strings.HasPrefix(auth, basicAuthPrefix) {
			// Check credentials
			payload, err := base64.StdEncoding.DecodeString(auth[len(basicAuthPrefix):])
			if err == nil {
				pair := bytes.SplitN(payload, []byte(":"), 2)
				if len(pair) == 2 &&
					bytes.Equal(pair[0], user) &&
					bytes.Equal(pair[1], pass) {

					// Delegate request to the given handle
					h(w, r, ps)
					return
				}
			}
		}

		// Request Basic Authentication otherwise
		w.Header().Set("WWW-Authenticate", "Basic realm=Restricted")
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
	}
}

func Index(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Not protected!\n")
}

func Protected(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Protected!\n")
}

func main() {
    user := []byte("gordon")
    pass := []byte("secret!")
    
    router := httprouter.New()
    router.GET("/", Index)
    router.GET("/protected/", BasicAuth(Protected, user, pass))

    log.Fatal(http.ListenAndServe(":8080", router))
}
```

## Chaining with the NotFound handler

**NOTE: It might be required to set [Router.HandleMethodNotAllowed](http://godoc.org/github.com/julienschmidt/httprouter#Router.HandleMethodNotAllowed) to `false` to avoid problems.**

You can use another [http.Handler](http://golang.org/pkg/net/http/#Handler), for example another router, to handle requests which could not be matched by this router by using the [Router.NotFound](http://godoc.org/github.com/julienschmidt/httprouter#Router.NotFound) handler. This allows chaining.

### Static files
The `NotFound` handler can for example be used to serve static files from the root path `/` (like an index.html file along with other assets):
```go
// Serve static files from the ./public directory
router.NotFound = http.FileServer(http.Dir("public")).ServeHTTP
```

But this approach sidesteps the strict core rules of this router to avoid routing problems. A cleaner approach is to use a distinct sub-path for serving files, like `/static/*filepath` or `/files/*filepath`.

## Web Frameworks based on HttpRouter
If the HttpRouter is a bit too minimalistic for you, you might try one of the following more high-level 3rd-party web frameworks building upon the HttpRouter package:
* [Ace](https://github.com/plimble/ace): Blazing fast Go Web Framework
* [api2go](https://github.com/univedo/api2go): A JSON API Implementation for Go
* [Gin](https://github.com/gin-gonic/gin): Features a martini-like API with much better performance
* [Goat](https://github.com/bahlo/goat): A minimalistic REST API server in Go
* [Hikaru](https://github.com/najeira/hikaru): Supports standalone and Google AppEngine
* [Hitch](https://github.com/nbio/hitch): Hitch ties httprouter, [httpcontext](https://github.com/nbio/httpcontext), and middleware up in a bow
* [kami](https://github.com/guregu/kami): A tiny web framework using x/net/context
* [Medeina](https://github.com/imdario/medeina): Inspired by Ruby's Roda and Cuba
* [Neko](https://github.com/rocwong/neko): A lightweight web application framework for Golang
* [Roxanna](https://github.com/iamthemuffinman/Roxanna): An amalgamation of httprouter, better logging, and hot reload
* [siesta](https://github.com/VividCortex/siesta): Composable HTTP handlers with contexts
# go-jmespath - A JMESPath implementation in Go

[![Build Status](https://img.shields.io/travis/jmespath/go-jmespath.svg)](https://travis-ci.org/jmespath/go-jmespath)



See http://jmespath.org for more info.
# Units - Helpful unit multipliers and functions for Go

The goal of this package is to have functionality similar to the [time](http://golang.org/pkg/time/) package.

It allows for code like this:

```go
n, err := ParseBase2Bytes("1KB")
// n == 1024
n = units.Mebibyte * 512
```
# Go's `text/template` package with newline elision

This is a fork of Go 1.4's [text/template](http://golang.org/pkg/text/template/) package with one addition: a backslash immediately after a closing delimiter will delete all subsequent newlines until a non-newline.

eg.

```
{{if true}}\
hello
{{end}}\
```

Will result in:

```
hello\n
```

Rather than:

```
\n
hello\n
\n
```
INI [![Build Status](https://travis-ci.org/go-ini/ini.svg?branch=master)](https://travis-ci.org/go-ini/ini)
===

![](https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

[简体中文](README_ZH.md)

## Feature

- Load multiple data sources(`[]byte` or file) with overwrites.
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

A **Data Source** is either raw data in type `[]byte` or a file name with type `string` and you can load **as many data sources as you want**. Passing other types will simply return an error.

```go
cfg, err := ini.Load([]byte("raw data"), "filename")
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
section := cfg.Section("")
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

- 支持覆盖加载多个数据源（`[]byte` 或文件）
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

一个 **数据源** 可以是 `[]byte` 类型的原始数据，或 `string` 类型的文件路径。您可以加载 **任意多个** 数据源。如果您传递其它类型的数据源，则会直接返回错误。

```go
cfg, err := ini.Load([]byte("raw data"), "filename")
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
section := cfg.Section("")
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

### 高级用法

#### 递归读取键值

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

#### 读取父子分区

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

#### 读取自增键名

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
[![Gitter chat](http://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/opentracing/public) [![Build Status](https://travis-ci.org/opentracing/opentracing-go.svg?branch=master)](https://travis-ci.org/opentracing/opentracing-go) [![GoDoc](https://godoc.org/github.com/opentracing/opentracing-go?status.svg)](http://godoc.org/github.com/opentracing/opentracing-go)

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
            tracer.Inject(
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

#### Goroutine-safety

The entire public API is goroutine-safe and does not require external
synchronization.

## API pointers for those implementing a tracing system

Tracing system implementors may be able to reuse or copy-paste-modify the `basictracer` package, found [here](https://github.com/opentracing/basictracer-go). In particular, see `basictracer.New(...)`.

## API compatibility

For the time being, "mild" backwards-incompatible changes may be made without changing the major version number. As OpenTracing and `opentracing-go` mature, backwards compatibility will become more of a priority.
# goid [![Build Status](https://travis-ci.org/petermattis/goid.svg?branch=master)](https://travis-ci.org/petermattis/goid)

Programatically retrieve the current goroutine's ID. See [the CI
configuration](.travis.yml) for supported Go versions.
[![GoDoc](https://godoc.org/github.com/go-logfmt/logfmt?status.svg)](https://godoc.org/github.com/go-logfmt/logfmt)
[![Go Report Card](https://goreportcard.com/badge/go-logfmt/logfmt)](https://goreportcard.com/report/go-logfmt/logfmt)
[![TravisCI](https://travis-ci.org/go-logfmt/logfmt.svg?branch=master)](https://travis-ci.org/go-logfmt/logfmt)
[![Coverage Status](https://coveralls.io/repos/github/go-logfmt/logfmt/badge.svg?branch=master)](https://coveralls.io/github/go-logfmt/logfmt?branch=master)

# logfmt

Package logfmt implements utilities to marshal and unmarshal data in the [logfmt
format](https://brandur.org/logfmt). It provides an API similar to
[encoding/json](http://golang.org/pkg/encoding/json/) and
[encoding/xml](http://golang.org/pkg/encoding/xml/).

The logfmt format was first documented by Brandur Leach in [this
article](https://brandur.org/logfmt). The format has not been formally
standardized. The most authoritative public specification to date has been the
documentation of a Go Language [package](http://godoc.org/github.com/kr/logfmt)
written by Blake Mizerany and Keith Rarick.

## Goals

This project attempts to conform as closely as possible to the prior art, while
also removing ambiguity where necessary to provide well behaved encoder and
decoder implementations.

## Non-goals

This project does not attempt to formally standardize the logfmt format. In the
event that logfmt is standardized this project would take conforming to the
standard as a goal.

## Versioning

Package logfmt publishes releases via [semver](http://semver.org/) compatible Git tags prefixed with a single 'v'.
# Universally Unique Lexicographically Sortable Identifier

![Project status](https://img.shields.io/badge/version-0.3.0-yellow.svg)
[![Build Status](https://secure.travis-ci.org/oklog/ulid.png)](http://travis-ci.org/oklog/ulid)
[![Go Report Card](https://goreportcard.com/badge/oklog/ulid?cache=0)](https://goreportcard.com/report/oklog/ulid)
[![Coverage Status](https://coveralls.io/repos/github/oklog/ulid/badge.svg?branch=master&cache=0)](https://coveralls.io/github/oklog/ulid?branch=master)
[![GoDoc](https://godoc.org/github.com/oklog/ulid?status.svg)](https://godoc.org/github.com/oklog/ulid)
[![Apache 2 licensed](https://img.shields.io/badge/license-Apache2-blue.svg)](https://raw.githubusercontent.com/oklog/ulid/master/LICENSE)

A Go port of [alizain/ulid](https://github.com/alizain/ulid) with binary format implemented.

## Background

A GUID/UUID can be suboptimal for many use-cases because:

- It isn't the most character efficient way of encoding 128 bits
- UUID v1/v2 is impractical in many environments, as it requires access to a unique, stable MAC address
- UUID v3/v5 requires a unique seed and produces randomly distributed IDs, which can cause fragmentation in many data structures
- UUID v4 provides no other information than randomness which can cause fragmentation in many data structures

A ULID however:

- Is compatible with UUID/GUID's
- 1.21e+24 unique ULIDs per millisecond (1,208,925,819,614,629,174,706,176 to be exact)
- Lexicographically sortable
- Canonically encoded as a 26 character string, as opposed to the 36 character UUID
- Uses Crockford's base32 for better efficiency and readability (5 bits per character)
- Case insensitive
- No special characters (URL safe)

## Install

```shell
go get github.com/oklog/ulid
```

## Usage

An ULID is constructed with a `time.Time` and an `io.Reader` entropy source.
This design allows for greater flexibility in choosing your trade-offs.

Please note that `rand.Rand` from the `math` package is *not* safe for concurrent use.
Instantiate one per long living go-routine or use a `sync.Pool` if you want to avoid the potential contention of a locked `rand.Source` as its been frequently observed in the package level functions.

```go
func ExampleULID() {
	t := time.Unix(1000000, 0)
	entropy := rand.New(rand.NewSource(t.UnixNano()))
	fmt.Println(ulid.MustNew(ulid.Timestamp(t), entropy))
	// Output: 0000XSNJG0MQJHBF4QX1EFD6Y3
}

```

## Specification

Below is the current specification of ULID as implemented in this repository.

### Components

**Timestamp**
- 48 bits
- UNIX-time in milliseconds
- Won't run out of space till the year 10895 AD

**Entropy**
- 80 bits
- User defined entropy source.

### Encoding

[Crockford's Base32](http://www.crockford.com/wrmg/base32.html) is used as shown.
This alphabet excludes the letters I, L, O, and U to avoid confusion and abuse.

```
0123456789ABCDEFGHJKMNPQRSTVWXYZ
```

### Binary Layout and Byte Order

The components are encoded as 16 octets. Each component is encoded with the Most Significant Byte first (network byte order).

```
0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                      32_bit_uint_time_high                    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     16_bit_uint_time_low      |       16_bit_uint_random      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       32_bit_uint_random                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       32_bit_uint_random                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### String Representation

```
 01AN4Z07BY      79KA1307SR9X4MV3
|----------|    |----------------|
 Timestamp           Entropy
  10 chars           16 chars
   48bits             80bits
   base32             base32
```

## Test

```shell
go test ./...
```

## Benchmarks

On a Intel Core i7 Ivy Bridge 2.7 GHz, MacOS 10.12.1 and Go 1.8.0beta1

```
BenchmarkNew/WithCryptoEntropy-8      2000000        771 ns/op      20.73 MB/s   16 B/op   1 allocs/op
BenchmarkNew/WithEntropy-8            20000000      65.8 ns/op     243.01 MB/s   16 B/op   1 allocs/op
BenchmarkNew/WithoutEntropy-8         50000000      30.0 ns/op     534.06 MB/s   16 B/op   1 allocs/op
BenchmarkMustNew/WithCryptoEntropy-8  2000000        781 ns/op      20.48 MB/s   16 B/op   1 allocs/op
BenchmarkMustNew/WithEntropy-8        20000000      70.0 ns/op     228.51 MB/s   16 B/op   1 allocs/op
BenchmarkMustNew/WithoutEntropy-8     50000000      34.6 ns/op     462.98 MB/s   16 B/op   1 allocs/op
BenchmarkParse-8                      50000000      30.0 ns/op     866.16 MB/s    0 B/op   0 allocs/op
BenchmarkMustParse-8                  50000000      35.2 ns/op     738.94 MB/s    0 B/op   0 allocs/op
BenchmarkString-8                     20000000      64.9 ns/op     246.40 MB/s   32 B/op   1 allocs/op
BenchmarkMarshal/Text-8               20000000      55.8 ns/op     286.84 MB/s   32 B/op   1 allocs/op
BenchmarkMarshal/TextTo-8             100000000     22.4 ns/op     714.91 MB/s    0 B/op   0 allocs/op
BenchmarkMarshal/Binary-8             300000000     4.02 ns/op    3981.77 MB/s    0 B/op   0 allocs/op
BenchmarkMarshal/BinaryTo-8           2000000000    1.18 ns/op   13551.75 MB/s    0 B/op   0 allocs/op
BenchmarkUnmarshal/Text-8             100000000     20.5 ns/op    1265.27 MB/s    0 B/op   0 allocs/op
BenchmarkUnmarshal/Binary-8           300000000     4.94 ns/op    3240.01 MB/s    0 B/op   0 allocs/op
BenchmarkNow-8                        100000000     15.1 ns/op     528.09 MB/s    0 B/op   0 allocs/op
BenchmarkTimestamp-8                  2000000000    0.29 ns/op   27271.59 MB/s    0 B/op   0 allocs/op
BenchmarkTime-8                       2000000000    0.58 ns/op   13717.80 MB/s    0 B/op   0 allocs/op
BenchmarkSetTime-8                    2000000000    0.89 ns/op    9023.95 MB/s    0 B/op   0 allocs/op
BenchmarkEntropy-8                    200000000     7.62 ns/op    1311.66 MB/s    0 B/op   0 allocs/op
BenchmarkSetEntropy-8                 2000000000    0.88 ns/op   11376.54 MB/s    0 B/op   0 allocs/op
BenchmarkCompare-8                    200000000     7.34 ns/op    4359.23 MB/s    0 B/op   0 allocs/op
```

## Prior Art

- [alizain/ulid](https://github.com/alizain/ulid)
- [RobThree/NUlid](https://github.com/RobThree/NUlid)
- [imdario/go-ulid](https://github.com/imdario/go-ulid)
# cmux: Connection Mux [![Build Status](https://travis-ci.org/cockroachdb/cmux.svg?branch=master)](https://travis-ci.org/cockroachdb/cmux) [![GoDoc](https://godoc.org/github.com/cockroachdb/cmux?status.svg)](https://godoc.org/github.com/cockroachdb/cmux)

cmux is a generic Go library to multiplex connections based on their payload.
Using cmux, you can serve gRPC, SSH, HTTPS, HTTP, Go RPC, and pretty much any
other protocol on the same TCP listener.

## How-To
Simply create your main listener, create a cmux for that listener,
and then match connections:
```go
// Create the main listener.
l, err := net.Listen("tcp", ":23456")
if err != nil {
	log.Fatal(err)
}

// Create a cmux.
m := cmux.New(l)

// Match connections in order:
// First grpc, then HTTP, and otherwise Go RPC/TCP.
grpcL := m.Match(cmux.HTTP2HeaderField("content-type", "application/grpc"))
httpL := m.Match(cmux.HTTP1Fast())
trpcL := m.Match(cmux.Any()) // Any means anything that is not yet matched.

// Create your protocol servers.
grpcS := grpc.NewServer()
grpchello.RegisterGreeterServer(grpcs, &server{})

httpS := &http.Server{
	Handler: &helloHTTP1Handler{},
}

trpcS := rpc.NewServer()
s.Register(&ExampleRPCRcvr{})

// Use the muxed listeners for your servers.
go grpcS.Serve(grpcL)
go httpS.Serve(httpL)
go trpcS.Accept(trpcL)

// Start serving!
m.Serve()
```

There are [more examples on GoDoc](https://godoc.org/github.com/cockroachdb/cmux#pkg-examples).

## Performance
Since we are only matching the very first bytes of a connection, the
performance overhead on long-lived connections (i.e., RPCs and pipelined HTTP
streams) is negligible.

## Limitations
* *TLS*: `net/http` uses a [type assertion](https://github.com/golang/go/issues/14221)
to identify TLS connections; since cmux's lookahead-implementing connection
wraps the underlying TLS connection, this type assertion fails. This means you
can serve HTTPS using cmux but `http.Request.TLS` will not be set in your
handlers. If you are able to wrap TLS around cmux, you can work around this
limitation. See https://github.com/cockroachdb/cockroach/commit/83caba2 for an
example of this approach.

* *Different Protocols on The Same Connection*: `cmux` matches the connection
when it's accepted. For example, one connection can be either gRPC or REST, but
not both. That is, we assume that a client connection is either used for gRPC
or REST.

# Copyright and License
Copyright 2016 The CMux Authors. All rights reserved.

See [CONTRIBUTORS](https://github.com/cockroachdb/cmux/blob/master/CONTRIBUTORS)
for the CMux Authors. Code is released under
[the Apache 2 license](https://github.com/cockroachdb/cmux/blob/master/LICENSE).
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
Consul API client
=================

This package provides the `api` package which attempts to
provide programmatic access to the full Consul API.

Currently, all of the Consul APIs included in version 0.6.0 are supported.

Documentation
=============

The full documentation is available on [Godoc](https://godoc.org/github.com/hashicorp/consul/api)

Usage
=====

Below is an example of using the Consul client:

```go
// Get a new client
client, err := api.NewClient(api.DefaultConfig())
if err != nil {
    panic(err)
}

// Get a handle to the KV API
kv := client.KV()

// PUT a new KV pair
p := &api.KVPair{Key: "foo", Value: []byte("test")}
_, err = kv.Put(p, nil)
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
# package log

`package log` provides a minimal interface for structured logging in services.
It may be wrapped to encode conventions, enforce type-safety, provide leveled
logging, and so on. It can be used for both typical application log events,
and log-structured data streams.

## Structured logging

Structured logging is, basically, conceding to the reality that logs are
_data_, and warrant some level of schematic rigor. Using a stricter,
key/value-oriented message format for our logs, containing contextual and
semantic information, makes it much easier to get insight into the
operational activity of the systems we build. Consequently, `package log` is
of the strong belief that "[the benefits of structured logging outweigh the
minimal effort involved](https://www.thoughtworks.com/radar/techniques/structured-logging)".

Migrating from unstructured to structured logging is probably a lot easier
than you'd expect.

```go
// Unstructured
log.Printf("HTTP server listening on %s", addr)

// Structured
logger.Log("transport", "HTTP", "addr", addr, "msg", "listening")
```

## Usage

### Typical application logging

```go
w := log.NewSyncWriter(os.Stderr)
logger := log.NewLogfmtLogger(w)
logger.Log("question", "what is the meaning of life?", "answer", 42)

// Output:
// question="what is the meaning of life?" answer=42
```

### Contextual Loggers

```go
func main() {
	var logger log.Logger
	logger = log.NewLogfmtLogger(log.NewSyncWriter(os.Stderr))
	logger = log.With(logger, "instance_id", 123)

	logger.Log("msg", "starting")
	NewWorker(log.With(logger, "component", "worker")).Run()
	NewSlacker(log.With(logger, "component", "slacker")).Run()
}

// Output:
// instance_id=123 msg=starting
// instance_id=123 component=worker msg=running
// instance_id=123 component=slacker msg=running
```

### Interact with stdlib logger

Redirect stdlib logger to Go kit logger.

```go
import (
	"os"
	stdlog "log"
	kitlog "github.com/go-kit/kit/log"
)

func main() {
	logger := kitlog.NewJSONLogger(kitlog.NewSyncWriter(os.Stdout))
	stdlog.SetOutput(kitlog.NewStdlibAdapter(logger))
	stdlog.Print("I sure like pie")
}

// Output:
// {"msg":"I sure like pie","ts":"2016/01/01 12:34:56"}
```

Or, if, for legacy reasons, you need to pipe all of your logging through the
stdlib log package, you can redirect Go kit logger to the stdlib logger.

```go
logger := kitlog.NewLogfmtLogger(kitlog.StdlibWriter{})
logger.Log("legacy", true, "msg", "at least it's something")

// Output:
// 2016/01/01 12:34:56 legacy=true msg="at least it's something"
```

### Timestamps and callers

```go
var logger log.Logger
logger = log.NewLogfmtLogger(log.NewSyncWriter(os.Stderr))
logger = log.With(logger, "ts", log.DefaultTimestampUTC, "caller", log.DefaultCaller)

logger.Log("msg", "hello")

// Output:
// ts=2016-01-01T12:34:56Z caller=main.go:15 msg=hello
```

## Supported output formats

- [Logfmt](https://brandur.org/logfmt) ([see also](https://blog.codeship.com/logfmt-a-log-format-thats-easy-to-read-and-write))
- JSON

## Enhancements

`package log` is centered on the one-method Logger interface.

```go
type Logger interface {
	Log(keyvals ...interface{}) error
}
```

This interface, and its supporting code like is the product of much iteration
and evaluation. For more details on the evolution of the Logger interface,
see [The Hunt for a Logger Interface](http://go-talks.appspot.com/github.com/ChrisHines/talks/structured-logging/structured-logging.slide#1),
a talk by [Chris Hines](https://github.com/ChrisHines).
Also, please see
[#63](https://github.com/go-kit/kit/issues/63),
[#76](https://github.com/go-kit/kit/pull/76),
[#131](https://github.com/go-kit/kit/issues/131),
[#157](https://github.com/go-kit/kit/pull/157),
[#164](https://github.com/go-kit/kit/issues/164), and
[#252](https://github.com/go-kit/kit/pull/252)
to review historical conversations about package log and the Logger interface.

Value-add packages and suggestions,
like improvements to [the leveled logger](https://godoc.org/github.com/go-kit/kit/log/level),
are of course welcome. Good proposals should

- Be composable with [contextual loggers](https://godoc.org/github.com/go-kit/kit/log#With),
- Not break the behavior of [log.Caller](https://godoc.org/github.com/go-kit/kit/log#Caller) in any wrapped contextual loggers, and
- Be friendly to packages that accept only an unadorned log.Logger.

## Benchmarks & comparisons

There are a few Go logging benchmarks and comparisons that include Go kit's package log.

- [imkira/go-loggers-bench](https://github.com/imkira/go-loggers-bench) includes kit/log
- [uber-common/zap](https://github.com/uber-common/zap), a zero-alloc logging library, includes a comparison with kit/log
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
# Go App Engine packages

[![Build Status](https://travis-ci.org/golang/appengine.svg)](https://travis-ci.org/golang/appengine)

This repository supports the Go runtime on App Engine,
including both the standard App Engine and the
"App Engine flexible environment" (formerly known as "Managed VMs").
It provides APIs for interacting with App Engine services.
Its canonical import path is `google.golang.org/appengine`.

See https://cloud.google.com/appengine/docs/go/
for more information.

File issue reports and feature requests on the [Google App Engine issue
tracker](https://code.google.com/p/googleappengine/issues/entry?template=Go%20defect).

## Directory structure
The top level directory of this repository is the `appengine` package. It
contains the
basic APIs (e.g. `appengine.NewContext`) that apply across APIs. Specific API
packages are in subdirectories (e.g. `datastore`).

There is an `internal` subdirectory that contains service protocol buffers,
plus packages required for connectivity to make API calls. App Engine apps
should not directly import any package under `internal`.

## Updating a Go App Engine app

This section describes how to update an older Go App Engine app to use
these packages. A provided tool, `aefix`, can help automate steps 2 and 3
(run `go get google.golang.org/appengine/cmd/aefix` to install it), but
read the details below since `aefix` can't perform all the changes.

### 1. Update YAML files (App Engine flexible environment / Managed VMs only)

The `app.yaml` file (and YAML files for modules) should have these new lines added:
```
vm: true
```
See https://cloud.google.com/appengine/docs/go/modules/#Go_Instance_scaling_and_class for details.

### 2. Update import paths

The import paths for App Engine packages are now fully qualified, based at `google.golang.org/appengine`.
You will need to update your code to use import paths starting with that; for instance,
code importing `appengine/datastore` will now need to import `google.golang.org/appengine/datastore`.

### 3. Update code using deprecated, removed or modified APIs

Most App Engine services are available with exactly the same API.
A few APIs were cleaned up, and some are not available yet.
This list summarises the differences:

* `appengine.Context` has been replaced with the `Context` type from `golang.org/x/net/context`.
* Logging methods that were on `appengine.Context` are now functions in `google.golang.org/appengine/log`.
* `appengine.Timeout` has been removed. Use `context.WithTimeout` instead.
* `appengine.Datacenter` now takes a `context.Context` argument.
* `datastore.PropertyLoadSaver` has been simplified to use slices in place of channels.
* `delay.Call` now returns an error.
* `search.FieldLoadSaver` now handles document metadata.
* `urlfetch.Transport` no longer has a Deadline field; set a deadline on the
  `context.Context` instead.
* `aetest` no longer declares its own Context type, and uses the standard one instead.
* `taskqueue.QueueStats` no longer takes a maxTasks argument. That argument has been
  deprecated and unused for a long time.
* `appengine.BackendHostname` and `appengine.BackendInstance` were for the deprecated backends feature.
  Use `appengine.ModuleHostname`and `appengine.ModuleName` instead.
* Most of `appengine/file` and parts of `appengine/blobstore` are deprecated.
  Use [Google Cloud Storage](https://godoc.org/google.golang.org/cloud/storage) instead.
* `appengine/socket` is not required on App Engine flexible environment / Managed VMs.
  Use the standard `net` package instead.
# RabbitMQ Scraping

This is an example on how to setup RabbitMQ so Prometheus can scrape data from it.
It uses a third party [RabbitMQ exporter](https://github.com/kbudde/rabbitmq_exporter).

Since the [RabbitMQ exporter](https://github.com/kbudde/rabbitmq_exporter) needs to
scrape the RabbitMQ management API to scrape data, and it defaults to localhost, it is
easier to simply embed the **kbudde/rabbitmq-exporter** on the same pod as RabbitMQ,
this way they share the same network.

With this pod running you will have the exporter scraping data, but Prometheus has not
yet found the exporter and is not scraping data from it.

For more details on how to use Kubernetes service discovery take a look at the 
[documentation](http://prometheus.io/docs/operating/configuration/#kubernetes-sd-configurations-kubernetes_sd_config)
and at the [available examples](./documentation/examples).

After you got Kubernetes service discovery up and running you just need to advertise that RabbitMQ
is exposing metrics. To do that you need to define a service that:

* Exposes the exporter port
* Has a **prometheus.io/scrape: "true"** annotation
* Has a **prometheus.io/port: "9090"** annotation

And you should be able to see your RabbitMQ exporter being scraped on the Prometheus status page.
Since the IP that will be scraped will be the pod endpoint it is important that the node
where Prometheus is running has access to the Kubernetes overlay network
(flannel, Weave, AWS, or any of the other options that Kubernetes gives to you).
## Remote Write Adapter Example

This is a simple example of how to write a server to
receive samples from the remote storage output.

To use it:

```
go build
./example_write_adapter
```

...and then add the following to your `prometheus.yml`:

```yaml
remote_write:
  - url: "http://localhost:1234/receive"
```

Then start Prometheus:

```
./prometheus
```
# Remote storage adapter

This is a write adapter that receives samples via Prometheus's remote write
protocol and stores them in Graphite, InfluxDB, or OpenTSDB. It is meant as a
replacement for the built-in specific remote storage implementations that have
been removed from Prometheus.

For InfluxDB, this binary is also a read adapter that supports reading back
data through Prometheus via Prometheus's remote read protocol.

## Building

```
go build
```

## Running

Graphite example:

```
./remote_storage_adapter -graphite-address=localhost:8080
```

OpenTSDB example:

```
./remote_storage_adapter -opentsdb-url=http://localhost:8081/
```

InfluxDB example:

```
./remote_storage_adapter -influxdb-url=http://localhost:8086/ -influxdb.database=prometheus -influxdb.retention-policy=autogen
```

To show all flags:

```
./remote_storage_adapter -h
```

## Configuring Prometheus

To configure Prometheus to send samples to this binary, add the following to your `prometheus.yml`:

```yaml
# Remote write configuration (for Graphite, OpenTSDB, or InfluxDB).
remote_write:
  - url: "http://localhost:9201/write"

# Remote read configuration (for InfluxDB only at the moment).
remote_read:
  - url: "http://localhost:9201/read"
```
The `ui` package contains static files and templates used in the web UI. For
easier distribution they are statically compiled into the Prometheus binary
using the go-bindata tool (c.f. Makefile).

During development it is more convenient to always use the files on disk to
directly see changes without recompiling.
Set the environment variable `DEBUG=1` and run `make assets` for this to work. 
This will put `go-bindata` in DEBUG mode where it serves from your local filesystem.
This is for development purposes only.

After making changes to any file, run `make assets` (without the `DEBUG=1`) before committing to update
the generated inline version of the file.
### Service Discovery

This directory contains the service discovery (SD) component of Prometheus.

There is currently a moratorium on new service discovery mechanisms being added
to Prometheus due to a lack of developer capacity. In the meantime `file_sd` 
remains available.

## Design of a Prometheus SD

There are many requests to add new SDs to Prometheus, this section looks at
what makes a good SD and covers some of the common implementation issues.

### Does this make sense as an SD?

The first question to be asked is does it make sense to add this particular
SD? An SD mechanism should be reasonably well established, and at a minimum in
use across multiple organisations. It should allow discovering of machines
and/or services running somewhere. When exactly an SD is popular enough to
justify being added to Prometheus natively is an open question.

It should not be a brand new SD mechanism, or a variant of an established
mechanism. We want to integrate Prometheus with the SD that's already there in
your infrastructure, not invent yet more ways to do service discovery. We also
do not add mechanisms to work around users lacking service discovery and/or
configuration management infrastructure.

SDs that merely discover other applications running the same software (e.g.
talk to one Kafka or Cassandra server to find the others) are not service
discovery. In that case the SD you should be looking at is whatever decides
that a machine is going to be a Kafka server, likely a machine database or
configuration management system.

If something is particularly custom or unusual, `file_sd` is the generic
mechanism provided for users to hook in. Generally with Prometheus we offer a
single generic mechanism for things with infinite variations, rather than
trying to support everything natively (see also, alertmanager webhook, remote
read, remote write, node exporter textfile collector). For example anything
that would involve talking to a relational database should use `file_sd`
instead.

For configuration management systems like Chef, while they do have a
database/API that'd in principle make sense to talk to for service discovery,
the idiomatic approach is to use Chef's templating facilities to write out a
file for use with `file_sd`.


### Mapping from SD to Prometheus

The general principle with SD is to extract all the potentially useful
information we can out of the SD, and let the user choose what they need of it
using
[relabelling](https://prometheus.io/docs/operating/configuration/#<relabel_config>).
This information is generally termed metadata.

Metadata is exposed as a set of key/value pairs (labels) per target. The keys
are prefixed with `__meta_<sdname>_<key>`, and there should also be an `__address__`
label with the host:port of the target (preferably an IP address to avoid DNS
lookups). No other labelnames should be exposed.

It is very common for initial pull requests for new SDs to include hardcoded
assumptions that make sense for the the author's setup. SD should be generic,
any customisation should be handled via relabelling. There should be basically
no business logic, filtering, or transformations of the data from the SD beyond
that which is needed to fit it into the metadata data model. 

Arrays (e.g. a list of tags) should be converted to a single label with the
array values joined with a comma. Also prefix and suffix the value with a
comma. So for example the array `[a, b, c]` would become `,a,b,c,`. As
relabelling regexes are fully anchored, this makes it easier to write correct
regexes against (`.*,a,.*` works no matter where `a` appears in the list). The
canonical example of this is `__meta_consul_tags`.

Maps, hashes and other forms of key/value pairs should be all prefixed and
exposed as labels. For example for EC2 tags, there would be
`__meta_ec2_tag_Description=mydescription` for the Description tag. Labelnames
may only contain `[_a-zA-Z0-9]`, sanitize by replacing with underscores as needed.

For targets with multiple potential ports, you can a) expose them as a list, b)
if they're named expose them as a map or c) expose them each as their own
target. Kubernetes SD takes the target per port approach. a) and b) can be
combined.

For machine-like SDs (OpenStack, EC2, Kubernetes to some extent) there may
be multiple network interfaces for a target. Thus far reporting the details
of only the first/primary network interface has sufficed.


### Other implementation considerations

SDs are intended to dump all possible targets. For example the optional use of
EC2 service discovery would be to take the entire region's worth of EC2
instances it provides and do everything needed in one `scrape_config`. For
large deployments where you are only interested in a small proportion of the
returned targets, this may cause performance issues. If this occurs it is
acceptable to also offer filtering via whatever mechanisms the SD exposes. For
EC2 that would be the `Filter` option on `DescribeInstances`. Keep in mind that
this is a performance optimisation, it should be possible to do the same
filtering using relabelling alone. As with SD generally, we do not invent new
ways to filter targets (that is what relabelling is for), merely offer up
whatever functionality the SD itself offers.

It is a general rule with Prometheus that all configuration comes from the
configuration file. While the libraries you use to talk to the SD may also
offer other mechanisms for providing configuration/authentication under the
covers (EC2's use of environment variables being a prime example), using your SD
mechanism should not require this. Put another way, your SD implementation
should not read environment variables or files to obtain configuration.

Some SD mechanisms have rate limits that make them challenging to use. As an
example we have unfortunately had to reject Amazon ECS service discovery due to
the rate limits being so low that it would not be usable for anything beyond
small setups.

If a system offers multiple distinct types of SD, select which is in use with a
configuration option rather than returning them all from one mega SD that
requires relabelling to select just the one you want. So far we have only seen
this with Kubernetes. When a single SD with a selector vs.  multiple distinct
SDs makes sense is an open question.

If there is a failure while processing talking to the SD, abort rather than
returning partial data. It is better to work from stale targets than partial
or incorrect metadata.

The information obtained from service discovery is not considered sensitive
security wise. Do not return secrets in metadata, anyone with access to
the Prometheus server will be able to see them.


## Writing an SD mechanism

### The SD interface

A Service Discovery (SD) mechanism has to discover targets and provide them to Prometheus. We expect similar targets to be grouped together, in the form of a [`TargetGroup`](https://godoc.org/github.com/prometheus/prometheus/config#TargetGroup). The SD mechanism sends the targets down to prometheus as list of `TargetGroups`.

An SD mechanism has to implement the `Discoverer` Interface:
```go
type Discoverer interface {
	Run(ctx context.Context, up chan<- []*config.TargetGroup)
}
```

Prometheus will call the `Run()` method on a provider to initialise the discovery mechanism. The mechanism will then send *all* the `TargetGroup`s into the channel. 
Now the mechanism will watch for changes. For each update it can send all `TargetGroup`s, or only changed and new `TargetGroup`s, down the channel. `Manager` will handle 
both cases.

For example if we had a discovery mechanism and it retrieves the following groups:

```
[]config.TargetGroup{
  {
    Targets: []model.LabelSet{
       {
          "__instance__": "10.11.150.1:7870",
          "hostname": "demo-target-1",
          "test": "simple-test",
       },
       {
          "__instance__": "10.11.150.4:7870",
          "hostname": "demo-target-2",
          "test": "simple-test",
       },
    },
    Labels: map[LabelName][LabelValue] {
      "job": "mysql",
    },
    "Source": "file1", 
  },
  {
    Targets: []model.LabelSet{
       {
          "__instance__": "10.11.122.11:6001",
          "hostname": "demo-postgres-1",
          "test": "simple-test",
       },
       {
          "__instance__": "10.11.122.15:6001",
          "hostname": "demo-postgres-2",
          "test": "simple-test",
       },
    },
    Labels: map[LabelName][LabelValue] {
      "job": "postgres",
    },
    "Source": "file2", 
  },
}
```

Here there are two `TargetGroups` one group with source `file1` and another with `file2`. The grouping is implementation specific and could even be one target per group. But, one has to make sure every target group sent by an SD instance should have a `Source` which is unique across all the `TargetGroup`s of that SD instance. 

In this case, both the `TargetGroup`s are sent down the channel the first time `Run()` is called. Now, for an update, we need to send the whole _changed_ `TargetGroup` down the channel. i.e, if the target with `hostname: demo-postgres-2` goes away, we send:
```
&config.TargetGroup{
  Targets: []model.LabelSet{
     {
        "__instance__": "10.11.122.11:6001",
        "hostname": "demo-postgres-1",
        "test": "simple-test",
     },
  },
  Labels: map[LabelName][LabelValue] {
    "job": "postgres",
  },
  "Source": "file2", 
}
```
down the channel.

If all the targets in a group go away, we need to send the target groups with empty `Targets` down the channel. i.e, if all targets with `job: postgres` go away, we send:
```
&config.TargetGroup{
  Targets: nil,
  "Source": "file2", 
}
```
down the channel.

<!-- TODO: Add best-practices -->
