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
wmi
===

Package wmi provides a WQL interface to Windows WMI.

Note: It interfaces with WMI on the local machine, therefore it only runs on Windows.
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
#Go OLE

[![Build status](https://ci.appveyor.com/api/projects/status/qr0u2sf7q43us9fj?svg=true)](https://ci.appveyor.com/project/jacobsantos/go-ole-jgs28)
[![Build Status](https://travis-ci.org/go-ole/go-ole.svg?branch=master)](https://travis-ci.org/go-ole/go-ole)
[![GoDoc](https://godoc.org/github.com/go-ole/go-ole?status.svg)](https://godoc.org/github.com/go-ole/go-ole)

Go bindings for Windows COM using shared libraries instead of cgo.

By Yasuhiro Matsumoto.

## Install

To experiment with go-ole, you can just compile and run the example program:

```
go get github.com/go-ole/go-ole
cd /path/to/go-ole/
go test

cd /path/to/go-ole/example/excel
go run excel.go
```

## Continuous Integration

Continuous integration configuration has been added for both Travis-CI and AppVeyor. You will have to add these to your own account for your fork in order for it to run.

**Travis-CI**

Travis-CI was added to check builds on Linux to ensure that `go get` works when cross building. Currently, Travis-CI is not used to test cross-building, but this may be changed in the future. It is also not currently possible to test the library on Linux, since COM API is specific to Windows and it is not currently possible to run a COM server on Linux or even connect to a remote COM server.

**AppVeyor**

AppVeyor is used to build on Windows using the (in-development) test COM server. It is currently only used to test the build and ensure that the code works on Windows. It will be used to register a COM server and then run the test cases based on the test COM server.

The tests currently do run and do pass and this should be maintained with commits.

##Versioning

Go OLE uses [semantic versioning](http://semver.org) for version numbers, which is similar to the version contract of the Go language. Which means that the major version will always maintain backwards compatibility with minor versions. Minor versions will only add new additions and changes. Fixes will always be in patch. 

This contract should allow you to upgrade to new minor and patch versions without breakage or modifications to your existing code. Leave a ticket, if there is breakage, so that it could be fixed.

##LICENSE

Under the MIT License: http://mattn.mit-license.org/2013
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
| [Mattermost](https://github.com/shuLhan/mattermost-integration/tree/master/hooks/logrus) | Hook for logging to [Mattermost](https://mattermost.com/) |
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
| [Syslog](https://github.com/sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
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

* [`FluentdFormatter`](https://github.com/joonix/log). Formats entries that can by parsed by Kubernetes and Google Container Engine.
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

By default Logger is protected by mutex for concurrent writes, this mutex is invoked when calling hooks and writing logs.
If you are sure such locking is not needed, you can call logger.SetNoLock() to disable the locking.

Situation when locking is not needed includes:

* You have no hooks registered, or hooks calling is already thread-safe.

* Writing to logger.Out is already thread-safe, for example:

  1) logger.Out is protected by locks.

  2) logger.Out is a os.File handler opened with `O_APPEND` flag, and every write is smaller than 4k. (This allow multi-thread/multi-process writing)

     (Refer to http://www.notthewizard.com/2014/06/17/are-files-appends-really-atomic/)
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
[![GoDoc](https://godoc.org/github.com/docker/go-units?status.svg)](https://godoc.org/github.com/docker/go-units)

# Introduction

go-units is a library to transform human friendly measurements into machine friendly values.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-units) for examples and documentation.

## Copyright and license

Copyright © 2015 Docker, Inc.

go-units is licensed under the Apache License, Version 2.0.
See [LICENSE](LICENSE) for the full text of the license.
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
This code provides helper functions for dealing with archive files.
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
## Lumogon Examples

Lumogon's ability to inspect containers and return structured data can be useful
in a variety settings. Here are some examples to get you started.

* [Exploring Lumogon's JSON output with JQ](explore-lumogon-with-jq.md)
* [Scanning images with Lumogon](images-and-lumogon.md)
* [Testing image builds with Lumogon](testing-with-lumogon.md)
# Operating Systems Test Fixutres

This `docker-compose.yml` spins up a broad range of containers based on the most widely used base operating system images.

To start the containers in detached mode, run:
```
docker-compose up -d
```
To check the status of the OS containers, run:
```
docker-compose ps
```
To kill and remove the OS containers, run:
```
docker-compose kill
docker-compose rm
```# Lumogon type/provider for Puppet

## Overview

This module contains a custom type/provider for [Lumogon](https://lumogon.com), a container scanning and reporting tool. This custom type/provider exposes containers on a system as resources within Puppet to be consumed for discovery purposes.

## Requirements

* Puppet 4 or Later

## Usage

### Using `puppet resource`

```shell
$ puppet resource lumogon

lumogon { '/nginx':
  dpkg            => {'acl' => '2.2.52-2', 'adduser' => '3.113+nmu3', 'apt' => '1.0.9.8.4', 'base-files' => '8+deb8u7', 'base-passwd' => '3.5.37', 'bash' => '4.3-11+deb8u1', 'bsdutils' => '1:2.25.2-6', 'ca-certificates' => '20141019+deb8u2', 'coreutils' => '8.23-4', 'dash' => '0.5.7-4+b1', 'debconf' => '1.5.56', 'debconf-i18n' => '1.5.56', 'debian-archive-keyring' => '2014.3', 'debianutils' => '4.4+b1', 'diffutils' => '1:3.3-1+b1', 'dmsetup' => '2:1.02.90-2.2+deb8u1', 'dpkg' => '1.17.27', 'e2fslibs' => '1.42.12-2+b1', 'e2fsprogs' => '1.42.12-2+b1', 'findutils' => '4.4.2-9+b1', 'fontconfig-config' => '2.11.0-6.3+deb8u1', 'fonts-dejavu-core' => '2.34-1', 'gcc-4.8-base' => '4.8.4-1', 'gcc-4.9-base' => '4.9.2-10', 'gettext-base' => '0.19.3-2', 'gnupg' => '1.4.18-7+deb8u3', 'gpgv' => '1.4.18-7+deb8u3', 'grep' => '2.20-4.1', 'gzip' => '1.6-4', 'hostname' => '3.15', 'inetutils-ping' => '2:1.9.2.39.3a460-3', 'init' => '1.22', 'initscripts' => '2.88dsf-59', 'insserv' => '1.14.0-5', 'iproute2' => '3.16.0-2', 'libacl1' => '2.2.52-2', 'libapt-pkg4.12' => '1.0.9.8.4', 'libasprintf0c2' => '0.19.3-2', 'libattr1' => '1:2.4.47-2', 'libaudit-common' => '1:2.4-1', 'libaudit1' => '1:2.4-1+b1', 'libblkid1' => '2.25.2-6', 'libbz2-1.0' => '1.0.6-7+b3', 'libc-bin' => '2.19-18+deb8u7', 'libc6' => '2.19-18+deb8u7', 'libcap2' => '1:2.24-8', 'libcap2-bin' => '1:2.24-8', 'libcomerr2' => '1.42.12-2+b1', 'libcryptsetup4' => '2:1.6.6-5', 'libdb5.3' => '5.3.28-9', 'libdebconfclient0' => '0.192', 'libdevmapper1.02.1' => '2:1.02.90-2.2+deb8u1', 'libexpat1' => '2.1.0-6+deb8u3', 'libfontconfig1' => '2.11.0-6.3+deb8u1', 'libfreetype6' => '2.5.2-3+deb8u1', 'libgcc1' => '1:4.9.2-10', 'libgcrypt20' => '1.6.3-2+deb8u2', 'libgd3' => '2.1.0-5+deb8u9', 'libgdbm3' => '1.8.3-13.1', 'libgeoip1' => '1.6.2-4', 'libgpg-error0' => '1.17-3', 'libjbig0' => '2.1-3.1', 'libjpeg62-turbo' => '1:1.3.1-12', 'libkmod2' => '18-3', 'liblocale-gettext-perl' => '1.05-8+b1', 'liblzma5' => '5.1.1alpha+20120614-2+b3', 'libmount1' => '2.25.2-6', 'libncurses5' => '5.9+20140913-1+b1', 'libncursesw5' => '5.9+20140913-1+b1', 'libpam-modules' => '1.1.8-3.1+deb8u2', 'libpam-modules-bin' => '1.1.8-3.1+deb8u2', 'libpam-runtime' => '1.1.8-3.1+deb8u2', 'libpam0g' => '1.1.8-3.1+deb8u2', 'libpcre3' => '2:8.35-3.3+deb8u4', 'libperl5.20' => '5.20.2-3+deb8u6', 'libpng12-0' => '1.2.50-2+deb8u3', 'libprocps3' => '2:3.3.9-9', 'libreadline6' => '6.3-8+b3', 'libselinux1' => '2.3-2', 'libsemanage-common' => '2.3-1', 'libsemanage1' => '2.3-1+b1', 'libsepol1' => '2.3-2', 'libslang2' => '2.3.0-2', 'libsmartcols1' => '2.25.2-6', 'libss2' => '1.42.12-2+b1', 'libssl1.0.0' => '1.0.1t-1+deb8u6', 'libstdc++6' => '4.9.2-10', 'libsystemd0' => '215-17+deb8u6', 'libtext-charwidth-perl' => '0.04-7+b3', 'libtext-iconv-perl' => '1.7-5+b2', 'libtext-wrapi18n-perl' => '0.06-7', 'libtiff5' => '4.0.3-12.3+deb8u2', 'libtinfo5' => '5.9+20140913-1+b1', 'libudev1' => '215-17+deb8u6', 'libusb-0.1-4' => '2:0.1.12-25', 'libustr-1.0-1' => '1.0.4-3+b2', 'libuuid1' => '2.25.2-6', 'libvpx1' => '1.3.0-3', 'libx11-6' => '2:1.6.2-3', 'libx11-data' => '2:1.6.2-3', 'libxau6' => '1:1.0.8-1', 'libxcb1' => '1.10-3+b1', 'libxdmcp6' => '1:1.1.1-1+b1', 'libxml2' => '2.9.1+dfsg1-5+deb8u4', 'libxpm4' => '1:3.5.12-0+deb8u1', 'libxslt1.1' => '1.1.28-2+deb8u2', 'login' => '1:4.2-3+deb8u3', 'lsb-base' => '4.1+Debian13+nmu1', 'mawk' => '1.3.3-17', 'mount' => '2.25.2-6', 'multiarch-support' => '2.19-18+deb8u7', 'ncurses-base' => '5.9+20140913-1', 'ncurses-bin' => '5.9+20140913-1+b1', 'netbase' => '5.3', 'nginx' => '1.11.12-1~jessie', 'nginx-module-geoip' => '1.11.12-1~jessie', 'nginx-module-image-filter' => '1.11.12-1~jessie', 'nginx-module-njs' => '1.11.12.0.1.9-1~jessie', 'nginx-module-perl' => '1.11.12-1~jessie', 'nginx-module-xslt' => '1.11.12-1~jessie', 'openssl' => '1.0.1t-1+deb8u6', 'passwd' => '1:4.2-3+deb8u3', 'perl' => '5.20.2-3+deb8u6', 'perl-base' => '5.20.2-3+deb8u6', 'perl-modules' => '5.20.2-3+deb8u6', 'procps' => '2:3.3.9-9', 'readline-common' => '6.3-8', 'sed' => '4.2.2-4+deb8u1', 'sensible-utils' => '0.0.9', 'startpar' => '0.59-3', 'systemd' => '215-17+deb8u6', 'systemd-sysv' => '215-17+deb8u6', 'sysv-rc' => '2.88dsf-59', 'sysvinit-utils' => '2.88dsf-59', 'tar' => '1.27.1-2+deb8u1', 'tzdata' => '2017a-0+deb8u1', 'ucf' => '3.0030', 'udev' => '215-17+deb8u6', 'util-linux' => '2.25.2-6', 'zlib1g' => '1:1.2.8.dfsg-2+b1'},
  hostname        => 'ea100da360fe',
  id              => '0ea7bbc3d1815f3b7e159dce1e68755a99f8aee55f85911831d80ade99c4a605',
  os              => 'linux',
  platform        => 'debian',
  platformfamily  => 'debian',
  platformversion => '8.7',
}
```
