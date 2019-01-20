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
# Kingpin - A Go (golang) command line and flag parser [![](https://godoc.org/github.com/alecthomas/kingpin?status.svg)](http://godoc.org/github.com/alecthomas/kingpin) [![Build Status](https://travis-ci.org/alecthomas/kingpin.svg?branch=master)](https://travis-ci.org/alecthomas/kingpin)

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
  fmt.Printf("Would ping: %s with timeout %s and count %d", *ip, *timeout, *count)
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
`Duration()` and `ExistingFile()`.

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
  target = new(http.Header)
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
func listHosts(args []string) []string {
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
go-sqlite3
==========

[![Build Status](https://travis-ci.org/mattn/go-sqlite3.svg?branch=master)](https://travis-ci.org/mattn/go-sqlite3)
[![Coverage Status](https://coveralls.io/repos/mattn/go-sqlite3/badge.svg?branch=master)](https://coveralls.io/r/mattn/go-sqlite3?branch=master)
[![GoDoc](https://godoc.org/github.com/mattn/go-sqlite3?status.svg)](http://godoc.org/github.com/mattn/go-sqlite3)

Description
-----------

sqlite3 driver conforming to the built-in database/sql interface

Installation
------------

This package can be installed with the go get command:

    go get github.com/mattn/go-sqlite3
    
_go-sqlite3_ is *cgo* package.
If you want to build your app using go-sqlite3, you need gcc.
However, if you install _go-sqlite3_ with `go install github.com/mattn/go-sqlite3`, you don't need gcc to build your app anymore.
    
Documentation
-------------

API documentation can be found here: http://godoc.org/github.com/mattn/go-sqlite3

Examples can be found under the `./_example` directory

FAQ
---

* Want to build go-sqlite3 with libsqlite3 on my linux.

    Use `go build --tags "libsqlite3 linux"`

* Want to build go-sqlite3 with libsqlite3 on OS X.

    Install sqlite3 from homebrew: `brew install sqlite3`

    Use `go build --tags "libsqlite3 darwin"`

* Want to build go-sqlite3 with icu extension.

   Use `go build --tags "icu"`

* Can't build go-sqlite3 on windows 64bit.

    > Probably, you are using go 1.0, go1.0 has a problem when it comes to compiling/linking on windows 64bit. 
    > See: https://github.com/mattn/go-sqlite3/issues/27

* Getting insert error while query is opened.

    > You can pass some arguments into the connection string, for example, a URI.
    > See: https://github.com/mattn/go-sqlite3/issues/39

* Do you want to cross compile? mingw on Linux or Mac?

    > See: https://github.com/mattn/go-sqlite3/issues/106
    > See also: http://www.limitlessfx.com/cross-compile-golang-app-for-windows-from-linux.html

* Want to get time.Time with current locale

    Use `loc=auto` in SQLite3 filename schema like `file:foo.db?loc=auto`.

License
-------

MIT: http://mattn.mit-license.org/2012

sqlite3-binding.c, sqlite3-binding.h, sqlite3ext.h

The -binding suffix was added to avoid build failures under gccgo.

In this repository, those files are an amalgamation of code that was copied from SQLite3. The license of that code is the same as the license of SQLite3.

Author
------

Yasuhiro Matsumoto (a.k.a mattn)
[![Build Status](https://travis-ci.org/miekg/dns.svg?branch=master)](https://travis-ci.org/miekg/dns)

# Alternative (more granular) approach to a DNS library

> Less is more.

Complete and usable DNS library. All widely used Resource Records are
supported, including the DNSSEC types. It follows a lean and mean philosophy.
If there is stuff you should know as a DNS programmer there isn't a convenience
function for it. Server side and client side programming is supported, i.e. you
can build servers and resolvers with it.

We try to keep the "master" branch as sane as possible and at the bleeding edge
of standards, avoiding breaking changes wherever reasonable. We support the last
two versions of Go, currently: 1.5 and 1.6.

# Goals

* KISS;
* Fast;
* Small API, if its easy to code in Go, don't make a function for it.

# Users

A not-so-up-to-date-list-that-may-be-actually-current:

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

Send pull request if you want to be listed here.

# Features

* UDP/TCP queries, IPv4 and IPv6;
* RFC 1035 zone file parsing ($INCLUDE, $ORIGIN, $TTL and $GENERATE (for all record types) are supported;
* Fast:
    * Reply speed around ~ 80K qps (faster hardware results in more qps);
    * Parsing RRs ~ 100K RR/s, that's 5M records in about 50 seconds;
* Server side programming (mimicking the net/http package);
* Client side programming;
* DNSSEC: signing, validating and key generation for DSA, RSA and ECDSA;
* EDNS0, NSID, Cookies;
* AXFR/IXFR;
* TSIG, SIG(0);
* DNS over TLS: optional encrypted connection between client and server;
* DNS name compression;
* Depends only on the standard library.

Have fun!

Miek Gieben  -  2010-2012  -  <miek@miek.nl>

# Building

Building is done with the `go` tool. If you have setup your GOPATH
correctly, the following should work:

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
* 7553 - URI record
* 7858 - DNS over TLS: Initiation and Performance Considerations (draft)
* 7873 - Domain Name System (DNS) Cookies (draft-ietf-dnsop-cookies)
* xxxx - EDNS0 DNS Update Lease (draft)

## Loosely based upon

* `ldns`
* `NSD`
* `Net::DNS`
* `GRONG`
# Circonus metrics tracking for Go applications

This library supports named counters, gauges and histograms.
It also provides convenience wrappers for registering latency
instrumented functions with Go's builtin http server.

Initializing only requires setting an ApiToken.

## Example

**rough and simple**

```go
package main

import (
	"log"
	"math/rand"
	"os"
	"time"

	cgm "github.com/circonus-labs/circonus-gometrics"
)

func main() {

	log.Println("Configuring cgm")

	cmc := &cgm.Config{}

	// Interval at which metrics are submitted to Circonus, default: 10 seconds
	cmc.Interval = "10s" // 10 seconds
	// Enable debug messages, default: false
	cmc.Debug = false
	// Send debug messages to specific log.Logger instance
	// default: if debug stderr, else, discard
	//cmc.CheckManager.Log = ...

	// Circonus API configuration options
	//
	// Token, no default (blank disables check manager)
	cmc.CheckManager.API.TokenKey = os.Getenv("CIRCONUS_API_TOKEN")
	// App name, default: circonus-gometrics
	cmc.CheckManager.API.TokenApp = os.Getenv("CIRCONUS_API_APP")
	// URL, default: https://api.circonus.com/v2
	cmc.CheckManager.API.URL = os.Getenv("CIRCONUS_API_URL")

	// Check configuration options
	//
	// precedence 1 - explicit submission_url
	// precedence 2 - specific check id (note: not a check bundle id)
	// precedence 3 - search using instanceId and searchTag
	// otherwise: if an applicable check is NOT specified or found, an
	//            attempt will be made to automatically create one
	//
	// Pre-existing httptrap check submission_url
	cmc.CheckManager.Check.SubmissionURL = os.Getenv("CIRCONUS_SUBMISION_URL")
	// Pre-existing httptrap check id (check not check bundle)
	cmc.CheckManager.Check.ID = ""
	// if neither a submission url nor check id are provided, an attempt will be made to find an existing
	// httptrap check by using the circonus api to search for a check matching the following criteria:
	//      an active check,
	//      of type httptrap,
	//      where the target/host is equal to InstanceId - see below
	//      and the check has a tag equal to SearchTag - see below
	// Instance ID - an identifier for the 'group of metrics emitted by this process or service'
	//               this is used as the value for check.target (aka host)
	// default: 'hostname':'program name'
	// note: for a persistent instance that is ephemeral or transient where metric continuity is
	//       desired set this explicitly so that the current hostname will not be used.
	cmc.CheckManager.Check.InstanceID = ""
	// Search tag - a specific tag which, when coupled with the instanceId serves to identify the
	// origin and/or grouping of the metrics
	// default: service:application name (e.g. service:consul)
	cmc.CheckManager.Check.SearchTag = ""
	// Check secret, default: generated when a check needs to be created
	cmc.CheckManager.Check.Secret = ""
	// Check tags, array of strings, additional tags to add to a new check, default: none
	//cmc.CheckManager.Check.Tags = []string{"category:tagname"}
	// max amount of time to to hold on to a submission url
	// when a given submission fails (due to retries) if the
	// time the url was last updated is > than this, the trap
	// url will be refreshed (e.g. if the broker is changed
	// in the UI) default 5 minutes
	cmc.CheckManager.Check.MaxURLAge = "5m"
	// custom display name for check, default: "InstanceId /cgm"
	cmc.CheckManager.Check.DisplayName = ""
    // force metric activation - if a metric has been disabled via the UI
	// the default behavior is to *not* re-activate the metric; this setting
	// overrides the behavior and will re-activate the metric when it is
	// encountered. "(true|false)", default "false"
	cmc.CheckManager.Check.ForceMetricActivation = "false"

	// Broker configuration options
	//
	// Broker ID of specific broker to use, default: random enterprise broker or
	// Circonus default if no enterprise brokers are available.
	// default: only used if set
	cmc.CheckManager.Broker.ID = ""
	// used to select a broker with the same tag (e.g. can be used to dictate that a broker
	// serving a specific location should be used. "dc:sfo", "location:new_york", "zone:us-west")
	// if more than one broker has the tag, one will be selected randomly from the resulting list
	// default: not used unless != ""
	cmc.CheckManager.Broker.SelectTag = ""
	// longest time to wait for a broker connection (if latency is > the broker will
	// be considered invalid and not available for selection.), default: 500 milliseconds
	cmc.CheckManager.Broker.MaxResponseTime = "500ms"
	// if broker Id or SelectTag are not specified, a broker will be selected randomly
	// from the list of brokers available to the api token. enterprise brokers take precedence
	// viable brokers are "active", have the "httptrap" module enabled, are reachable and respond
	// within MaxResponseTime.

	log.Println("Creating new cgm instance")

	metrics, err := cgm.NewCirconusMetrics(cmc)
	if err != nil {
		panic(err)
	}

	src := rand.NewSource(time.Now().UnixNano())
	rnd := rand.New(src)

	log.Println("Starting cgm internal auto-flush timer")
	metrics.Start()

	log.Println("Starting to send metrics")

	// number of "sets" of metrics to send (a minute worth)
	max := 60

	for i := 1; i < max; i++ {
		log.Printf("\tmetric set %d of %d", i, 60)
		metrics.Timing("ding", rnd.Float64()*10)
		metrics.Increment("dong")
		metrics.Gauge("dang", 10)
		time.Sleep(1000 * time.Millisecond)
	}

	log.Println("Flushing any outstanding metrics manually")
	metrics.Flush()

}
```

### HTTP Handler wrapping

```
http.HandleFunc("/", metrics.TrackHTTPLatency("/", handler_func))
```

### HTTP latency example

```
package main

import (
    "os"
    "fmt"
    "net/http"
    cgm "github.com/circonus-labs/circonus-gometrics"
)

func main() {
    cmc := &cgm.Config{}
    cmc.CheckManager.API.TokenKey = os.Getenv("CIRCONUS_API_TOKEN")
  
    metrics, err := cgm.NewCirconusMetrics(cmc)
    if err != nil {
        panic(err)
    }
    metrics.Start()

    http.HandleFunc("/", metrics.TrackHTTPLatency("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
    }))
    http.ListenAndServe(":8080", http.DefaultServeMux)
}

```
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
# Gotcha: Super Simple Assertions for Go

Don't want to have to run a code generator to write test assertions? Sick of dropping boilerplate test runner code in every test file? Gotcha is a super simple Assertion library that just works.

```go
package mymath

import (
	"testing"
	. "github.com/anthonybishopric/gotcha"
)

func TestBasicAddition(t *testing.T) {
	Assert(t).AreEqual(1 + 1, 2, "expected addition to work")
}

```

## Portable Implementation

The `Assert()` function takes an interface `Failer`, shown below:

```go
type Failer interface {
	Fatalf(string, ...interface{})
}

```
So while the `gotcha` package will work with tests, it will also work with instances of `log.Logger`, and can be reused as mainline Assertions.

## Simple Matcher

Flexible matching can be done by implementing the `Matcher` interface

```go
type Matcher (interface{}) bool
```

These can be used together with the `Matches()` function

```go

func ValidPassword(s interface{}) bool {
	 x := s.(string)
	 return len(x) > 6
}

Assert(t).Matches(password, ValidPassword)
```

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

circbuf
=======

This repository provides the `circbuf` package. This provides a `Buffer` object
which is a circular (or ring) buffer. It has a fixed size, but can be written
to infinitely. Only the last `size` bytes are ever retained. The buffer implements
the `io.Writer` interface.

Documentation
=============

Full documentation can be found on [Godoc](http://godoc.org/github.com/armon/circbuf)

Usage
=====

The `circbuf` package is very easy to use:

```go
buf, _ := NewBuffer(6)
buf.Write([]byte("hello world"))

if string(buf.Bytes()) != " world" {
    panic("should only have last 6 bytes!")
}

```

go-metrics
==========

This library provides a `metrics` package which can be used to instrument code,
expose application metrics, and profile runtime performance in a flexible manner.

Current API: [![GoDoc](https://godoc.org/github.com/armon/go-metrics?status.svg)](https://godoc.org/github.com/armon/go-metrics)

Sinks
=====

The `metrics` package makes use of a `MetricSink` interface to support delivery
to any type of backend. Currently the following sinks are provided:

* StatsiteSink : Sinks to a [statsite](https://github.com/armon/statsite/) instance (TCP)
* StatsdSink: Sinks to a [StatsD](https://github.com/etsy/statsd/) / statsite instance (UDP)
* PrometheusSink: Sinks to a [Prometheus](http://prometheus.io/) metrics endpoint (exposed via HTTP for scrapes)
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
    inm := metrics.NewInmemSink(10*time.Second, time.Minute)
    sig := metrics.DefaultInmemSignal(inm)
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

## Overview

Package `statsd` provides a Go [dogstatsd](http://docs.datadoghq.com/guides/dogstatsd/) client.  Dogstatsd extends Statsd, adding tags
and histograms.

## Get the code

    $ go get github.com/DataDog/datadog-go/statsd

## Usage

```go
// Create the client
c, err := statsd.New("127.0.0.1:8125")
if err != nil {
    log.Fatal(err)
}
// Prefix every metric with the app name
c.Namespace = "flubber."
// Send the EC2 availability zone as a tag with every metric
c.Tags = append(c.Tags, "us-east-1a")

// Do some metrics!
err = c.Gauge("request.queue_depth", 12, nil, 1)
err = c.Timing("request.duration", duration, nil, 1) // Uses a time.Duration!
err = c.TimeInMilliseconds("request", 12, nil, 1)
err = c.Incr("request.count_total", nil, 1)
err = c.Decr("request.count_total", nil, 1)
err = c.Count("request.count_total", 2, nil, 1)
```

## Buffering Client

DogStatsD accepts packets with multiple statsd payloads in them.  Using the BufferingClient via `NewBufferingClient` will buffer up commands and send them when the buffer is reached or after 100msec.

## Development

Run the tests with:

    $ go test

## Documentation

Please see: http://godoc.org/github.com/DataDog/datadog-go/statsd

## License

go-dogstatsd is released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).

## Credits

Original code by [ooyala](https://github.com/ooyala/go-dogstatsd).
# go-dockerclient

[![Travis](https://img.shields.io/travis/fsouza/go-dockerclient/master.svg?style=flat-square)](https://travis-ci.org/fsouza/go-dockerclient)
[![GoDoc](https://img.shields.io/badge/api-Godoc-blue.svg?style=flat-square)](https://godoc.org/github.com/fsouza/go-dockerclient)

This package presents a client for the Docker remote API. It also provides
support for the extensions in the [Swarm API](https://docs.docker.com/swarm/swarm-api/).
It currently supports the Docker API up to version 1.23.

This package also provides support for docker's network API, which is a simple
passthrough to the libnetwork remote API.  Note that docker's network API is
only available in docker 1.8 and above, and only enabled in docker if
DOCKER_EXPERIMENTAL is defined during the docker build process.

For more details, check the [remote API documentation](http://docs.docker.com/engine/reference/api/docker_remote_api/).

## Example

```go
package main

import (
	"fmt"

	"github.com/fsouza/go-dockerclient"
)

func main() {
	endpoint := "unix:///var/run/docker.sock"
	client, _ := docker.NewClient(endpoint)
	imgs, _ := client.ListImages(docker.ListImagesOptions{All: false})
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

In order to instantiate the client for a TLS-enabled daemon, you should use NewTLSClient, passing the endpoint and path for key and certificates as parameters.

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

If using [docker-machine](https://docs.docker.com/machine/), or another application that exports environment variables
`DOCKER_HOST, DOCKER_TLS_VERIFY, DOCKER_CERT_PATH`, you can use NewClientFromEnv.


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

* [golint](https://github.com/golang/lint)
* [go vet](https://godoc.org/golang.org/x/tools/cmd/vet)
* [gofmt](https://golang.org/cmd/gofmt)
* [go test](https://golang.org/cmd/go/#hdr-Test_packages)

Running `make test` will check all of these. If your editor does not automatically call gofmt, `make fmt` will format all go files in this repository.
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
[Serf](https://github.com/hashicorp/serf), and
[Consul](https://github.com/hashicorp/consul).

## Features

* Easy sub-command based CLIs: `cli foo`, `cli bar`, etc.

* Support for nested subcommands such as `cli foo bar`.

* Optional support for default subcommands so `cli` does something
  other than error.

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

# reflectwalk

reflectwalk is a Go library for "walking" a value in Go using reflection,
in the same way a directory tree can be "walked" on the filesystem. Walking
a complex structure can allow you to do manipulations on unknown structures
such as those decoded from JSON.
# mapstructure

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
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/Sirupsen/logrus.svg?branch=master)](https://travis-ci.org/Sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/Sirupsen/logrus?status.svg)](https://godoc.org/github.com/Sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc]. **Please note the Logrus API is not
yet stable (pre 1.0). Logrus itself is completely stable and has been used in
many large deployments. The core API is unlikely to change much but please
version control your Logrus to make sure you aren't fetching latest `master` on
every build.**

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

#### Example

The simplest way to use Logrus is simply the package-level exported logger:

```go
package main

import (
  log "github.com/Sirupsen/logrus"
)

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
  }).Info("A walrus appears")
}
```

Note that it's completely api-compatible with the stdlib logger, so you can
replace your `log` imports everywhere with `log "github.com/Sirupsen/logrus"`
and you'll now have the flexibility of Logrus. You can customize it all you
want:

```go
package main

import (
  "os"
  log "github.com/Sirupsen/logrus"
)

func init() {
  // Log as JSON instead of the default ASCII formatter.
  log.SetFormatter(&log.JSONFormatter{})

  // Output to stderr instead of stdout, could also be a file.
  log.SetOutput(os.Stderr)

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
  "github.com/Sirupsen/logrus"
)

// Create a new instance of the logger. You can have any number of instances.
var log = logrus.New()

func main() {
  // The API for setting attributes is a little different than the package level
  // exported logger. See Godoc.
  log.Out = os.Stderr

  log.WithFields(logrus.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")
}
```

#### Fields

Logrus encourages careful, structured logging though logging fields instead of
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

#### Hooks

You can add hooks for logging levels. For example to send errors to an exception
tracking service on `Error`, `Fatal` and `Panic`, info to StatsD or log to
multiple places simultaneously, e.g. syslog.

Logrus comes with [built-in hooks](hooks/). Add those, or your custom hook, in
`init`:

```go
import (
  log "github.com/Sirupsen/logrus"
  "gopkg.in/gemnasium/logrus-airbrake-hook.v2" // the package is named "aibrake"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
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
| [Airbrake](https://github.com/gemnasium/logrus-airbrake-hook) | Send errors to the Airbrake API V3. Uses the official [`gobrake`](https://github.com/airbrake/gobrake) behind the scenes. |
| [Airbrake "legacy"](https://github.com/gemnasium/logrus-airbrake-legacy-hook) | Send errors to an exception tracking service compatible with the Airbrake API V2. Uses [`airbrake-go`](https://github.com/tobi/airbrake-go) behind the scenes. |
| [Papertrail](https://github.com/polds/logrus-papertrail-hook) | Send errors to the [Papertrail](https://papertrailapp.com) hosted logging service via UDP. |
| [Syslog](https://github.com/Sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [Bugsnag](https://github.com/Shopify/logrus-bugsnag/blob/master/bugsnag.go) | Send errors to the Bugsnag exception tracking service. |
| [Sentry](https://github.com/evalphobia/logrus_sentry) | Send errors to the Sentry error logging and aggregation service. |
| [Hiprus](https://github.com/nubo/hiprus) | Send errors to a channel in hipchat. |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Journalhook](https://github.com/wercker/journalhook) | Hook for logging to `systemd-journald` |
| [Graylog](https://github.com/gemnasium/logrus-graylog-hook) | Hook for logging to [Graylog](http://graylog2.org/) |
| [Raygun](https://github.com/squirkle/logrus-raygun-hook) | Hook for logging to [Raygun.io](http://raygun.io/) |
| [LFShook](https://github.com/rifflock/lfshook) | Hook for logging to the local filesystem |
| [Honeybadger](https://github.com/agonzalezro/logrus_honeybadger) | Hook for sending exceptions to Honeybadger |
| [Mail](https://github.com/zbindenren/logrus_mail) | Hook for sending exceptions via mail |
| [Rollrus](https://github.com/heroku/rollrus) | Hook for sending errors to rollbar |
| [Fluentd](https://github.com/evalphobia/logrus_fluent) | Hook for logging to fluentd |
| [Mongodb](https://github.com/weekface/mgorus) | Hook for logging to mongodb |
| [Influxus] (http://github.com/vlad-doru/influxus) | Hook for concurrently logging to [InfluxDB] (http://influxdata.com/) |
| [InfluxDB](https://github.com/Abramovic/logrus_influxdb) | Hook for logging to influxdb |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [DeferPanic](https://github.com/deferpanic/dp-logrus) | Hook for logging to DeferPanic |
| [Redis-Hook](https://github.com/rogierlommers/logrus-redis-hook) | Hook for logging to a ELK stack (through Redis) |
| [Amqp-Hook](https://github.com/vladoatanasov/logrus_amqp) | Hook for logging to Amqp broker (Like RabbitMQ) |
| [KafkaLogrus](https://github.com/goibibo/KafkaLogrus) | Hook for logging to kafka |
| [Typetalk](https://github.com/dragon3/logrus-typetalk-hook) | Hook for logging to [Typetalk](https://www.typetalk.in/) |
| [ElasticSearch](https://github.com/sohlich/elogrus) | Hook for logging to ElasticSearch|
| [Sumorus](https://github.com/doublefree/sumorus) | Hook for logging to [SumoLogic](https://www.sumologic.com/)|
| [Scribe](https://github.com/sagar8192/logrus-scribe-hook) | Hook for logging to [Scribe](https://github.com/facebookarchive/scribe)|
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [logz.io](https://github.com/ripcurld00d/logrus-logzio-hook) | Hook for logging to [logz.io](https://logz.io), a Log as a Service using Logstash |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |
| [Pushover](https://github.com/toorop/logrus_pushover) | Send error via [Pushover](https://pushover.net) |


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
  log "github.com/Sirupsen/logrus"
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
    `DisableColors` field to `true`
* `logrus.JSONFormatter`. Logs fields as JSON.

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

#### Rotation

Log rotation is not provided with Logrus. Log rotation should be done by an
external program (like `logrotate(8)`) that can compress and delete old log
entries. It should not be a feature of the application-level logger.

#### Tools

| Tool | Description |
| ---- | ----------- |
|[Logrus Mate](https://github.com/gogap/logrus_mate)|Logrus mate is a tool for Logrus to manage loggers, you can initial logger's level, hook and formatter by config file, the logger will generated with different config at different environment.|
|[Logrus Viper Helper](https://github.com/heirko/go-contrib/tree/master/logrusHelper)|An Helper arround Logrus to wrap with spf13/Viper to load configuration with fangs! And to simplify Logrus configuration use some behavior of [Logrus Mate](https://github.com/gogap/logrus_mate). [sample](https://github.com/heirko/iris-contrib/blob/master/middleware/logrus-logger/example) |

#### Testing

Logrus has a built in facility for asserting the presence of log messages. This is implemented through the `test` hook and provides:

* decorators for existing logger (`test.NewLocal` and `test.NewGlobal`) which basically just add the `test` hook
* a test logger (`test.NewNullLogger`) that just records log messages (and does not output any):

```go
logger, hook := NewNullLogger()
logger.Error("Hello error")

assert.Equal(1, len(hook.Entries))
assert.Equal(logrus.ErrorLevel, hook.LastEntry().Level)
assert.Equal("Hello error", hook.LastEntry().Message)

hook.Reset()
assert.Nil(hook.LastEntry())
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

#### Thread safty

By default Logger is protected by mutex for concurrent writes, this mutex is invoked when calling hooks and writing logs.
If you are sure such locking is not needed, you can call logger.SetNoLock() to disable the locking.

Situation when locking is not needed includes:

* You have no hooks registered, or hooks calling is already thread-safe.

* Writing to logger.Out is already thread-safe, for example:

  1) logger.Out is protected by locks.

  2) logger.Out is a os.File handler opened with `O_APPEND` flag, and every write is smaller than 4k. (This allow multi-thread/multi-process writing)

     (Refer to http://www.notthewizard.com/2014/06/17/are-files-appends-really-atomic/)
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
# go-bindata-assetfs

Serve embedded files from [jteeuwen/go-bindata](https://github.com/jteeuwen/go-bindata) with `net/http`.

[GoDoc](http://godoc.org/github.com/elazarl/go-bindata-assetfs)

### Installation

Install with

    $ go get github.com/jteeuwen/go-bindata/...
    $ go get github.com/elazarl/go-bindata-assetfs/...

### Creating embedded data

Usage is identical to [jteeuwen/go-bindata](https://github.com/jteeuwen/go-bindata) usage,
instead of running `go-bindata` run `go-bindata-assetfs`.

The tool will create a `bindata_assetfs.go` file, which contains the embedded data.

A typical use case is

    $ go-bindata-assetfs data/...

### Using assetFS in your code

The generated file provides an `assetFS()` function that returns a `http.Filesystem`
wrapping the embedded files. What you usually want to do is:

    http.Handle("/", http.FileServer(assetFS()))

This would run an HTTP server serving the embedded files.

## Without running binary tool

You can always just run the `go-bindata` tool, and then

use

     import "github.com/elazarl/go-bindata-assetfs"
     ...
     http.Handle("/",
        http.FileServer(
        &assetfs.AssetFS{Asset: Asset, AssetDir: AssetDir, AssetInfo: AssetInfo, Prefix: "data"}))

to serve files embedded from the `data` directory.
go-metrics
==========

![travis build status](https://travis-ci.org/rcrowley/go-metrics.svg?branch=master)

Go port of Coda Hale's Metrics library: <https://github.com/dropwizard/metrics>.

Documentation: <http://godoc.org/github.com/rcrowley/go-metrics>.

Usage
-----

Create and update metrics:

```go
c := metrics.NewCounter()
metrics.Register("foo", c)
c.Inc(47)

g := metrics.NewGauge()
metrics.Register("bar", g)
g.Update(47)

r := NewRegistry()
g := metrics.NewRegisteredFunctionalGauge("cache-evictions", r, func() int64 { return cache.getEvictionsCount() })

s := metrics.NewExpDecaySample(1028, 0.015) // or metrics.NewUniformSample(1028)
h := metrics.NewHistogram(s)
metrics.Register("baz", h)
h.Update(47)

m := metrics.NewMeter()
metrics.Register("quux", m)
m.Mark(47)

t := metrics.NewTimer()
metrics.Register("bang", t)
t.Time(func() {})
t.Update(47)
```

Register() is not threadsafe. For threadsafe metric registration use
GetOrRegister:

```
t := metrics.GetOrRegisterTimer("account.create.latency", nil)
t.Time(func() {})
t.Update(47)
```

Periodically log every metric in human-readable form to standard error:

```go
go metrics.Log(metrics.DefaultRegistry, 5 * time.Second, log.New(os.Stderr, "metrics: ", log.Lmicroseconds))
```

Periodically log every metric in slightly-more-parseable form to syslog:

```go
w, _ := syslog.Dial("unixgram", "/dev/log", syslog.LOG_INFO, "metrics")
go metrics.Syslog(metrics.DefaultRegistry, 60e9, w)
```

Periodically emit every metric to Graphite using the [Graphite client](https://github.com/cyberdelia/go-metrics-graphite):

```go

import "github.com/cyberdelia/go-metrics-graphite"

addr, _ := net.ResolveTCPAddr("tcp", "127.0.0.1:2003")
go graphite.Graphite(metrics.DefaultRegistry, 10e9, "metrics", addr)
```

Periodically emit every metric into InfluxDB:

**NOTE:** this has been pulled out of the library due to constant fluctuations
in the InfluxDB API. In fact, all client libraries are on their way out. see
issues [#121](https://github.com/rcrowley/go-metrics/issues/121) and
[#124](https://github.com/rcrowley/go-metrics/issues/124) for progress and details.

```go
import "github.com/vrischmann/go-metrics-influxdb"

go influxdb.Influxdb(metrics.DefaultRegistry, 10e9, &influxdb.Config{
    Host:     "127.0.0.1:8086",
    Database: "metrics",
    Username: "test",
    Password: "test",
})
```

Periodically upload every metric to Librato using the [Librato client](https://github.com/mihasya/go-metrics-librato):

**Note**: the client included with this repository under the `librato` package
has been deprecated and moved to the repository linked above.

```go
import "github.com/mihasya/go-metrics-librato"

go librato.Librato(metrics.DefaultRegistry,
    10e9,                  // interval
    "example@example.com", // account owner email address
    "token",               // Librato API token
    "hostname",            // source
    []float64{0.95},       // percentiles to send
    time.Millisecond,      // time unit
)
```

Periodically emit every metric to StatHat:

```go
import "github.com/rcrowley/go-metrics/stathat"

go stathat.Stathat(metrics.DefaultRegistry, 10e9, "example@example.com")
```

Maintain all metrics along with expvars at `/debug/metrics`:

This uses the same mechanism as [the official expvar](http://golang.org/pkg/expvar/)
but exposed under `/debug/metrics`, which shows a json representation of all your usual expvars
as well as all your go-metrics.


```go
import "github.com/rcrowley/go-metrics/exp"

exp.Exp(metrics.DefaultRegistry)
```

Installation
------------

```sh
go get github.com/rcrowley/go-metrics
```

StatHat support additionally requires their Go client:

```sh
go get github.com/stathat/go
```

Publishing Metrics
------------------

Clients are available for the following destinations:

* Librato - [https://github.com/mihasya/go-metrics-librato](https://github.com/mihasya/go-metrics-librato)
* Graphite - [https://github.com/cyberdelia/go-metrics-graphite](https://github.com/cyberdelia/go-metrics-graphite)
* InfluxDB - [https://github.com/vrischmann/go-metrics-influxdb](https://github.com/vrischmann/go-metrics-influxdb)
* Ganglia - [https://github.com/appscode/metlia](https://github.com/appscode/metlia)
* Prometheus - [https://github.com/deathowl/go-metrics-prometheus](https://github.com/deathowl/go-metrics-prometheus)
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

## Thanks

Thanks to:

  * [@vstakhov](https://github.com/vstakhov) - The original libucl parser
    and syntax that HCL was based off of.

  * [@fatih](https://github.com/fatih) - The rewritten HCL parser
    in pure Go (no goyacc) and support for a printer.
raft-boltdb
===========

This repository provides the `raftboltdb` package. The package exports the
`BoltStore` which is an implementation of both a `LogStore` and `StableStore`.

It is meant to be used as a backend for the `raft` [package
here](https://github.com/hashicorp/raft).

This implementation uses [BoltDB](https://github.com/boltdb/bolt). BoltDB is
a simple key/value store implemented in pure Go, and inspired by LMDB.
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

raft [![Build Status](https://travis-ci.org/hashicorp/raft.png)](https://travis-ci.org/hashicorp/raft)
====

raft is a [Go](http://www.golang.org) library that manages a replicated
log and can be used with an FSM to manage replicated state machines. It
is library for providing [consensus](http://en.wikipedia.org/wiki/Consensus_(computer_science)).

The use cases for such a library are far-reaching as replicated state
machines are a key component of many distributed systems. They enable
building Consistent, Partition Tolerant (CP) systems, with limited
fault tolerance as well.

## Building

If you wish to build raft you'll need Go version 1.2+ installed.

Please check your installation with:

```
go version
```

## Documentation

For complete documentation, see the associated [Godoc](http://godoc.org/github.com/hashicorp/raft).

To prevent complications with cgo, the primary backend `MDBStore` is in a separate repository,
called [raft-mdb](http://github.com/hashicorp/raft-mdb). That is the recommended implementation
for the `LogStore` and `StableStore`.

A pure Go backend using [BoltDB](https://github.com/boltdb/bolt) is also available called
[raft-boltdb](https://github.com/hashicorp/raft-boltdb). It can also be used as a `LogStore`
and `StableStore`.

## Protocol

raft is based on ["Raft: In Search of an Understandable Consensus Algorithm"](https://ramcloud.stanford.edu/wiki/download/attachments/11370504/raft.pdf)

A high level overview of the Raft protocol is described below, but for details please read the full
[Raft paper](https://ramcloud.stanford.edu/wiki/download/attachments/11370504/raft.pdf)
followed by the raft source. Any questions about the raft protocol should be sent to the
[raft-dev mailing list](https://groups.google.com/forum/#!forum/raft-dev).

### Protocol Description

Raft nodes are always in one of three states: follower, candidate or leader. All
nodes initially start out as a follower. In this state, nodes can accept log entries
from a leader and cast votes. If no entries are received for some time, nodes
self-promote to the candidate state. In the candidate state nodes request votes from
their peers. If a candidate receives a quorum of votes, then it is promoted to a leader.
The leader must accept new log entries and replicate to all the other followers.
In addition, if stale reads are not acceptable, all queries must also be performed on
the leader.

Once a cluster has a leader, it is able to accept new log entries. A client can
request that a leader append a new log entry, which is an opaque binary blob to
Raft. The leader then writes the entry to durable storage and attempts to replicate
to a quorum of followers. Once the log entry is considered *committed*, it can be
*applied* to a finite state machine. The finite state machine is application specific,
and is implemented using an interface.

An obvious question relates to the unbounded nature of a replicated log. Raft provides
a mechanism by which the current state is snapshotted, and the log is compacted. Because
of the FSM abstraction, restoring the state of the FSM must result in the same state
as a replay of old logs. This allows Raft to capture the FSM state at a point in time,
and then remove all the logs that were used to reach that state. This is performed automatically
without user intervention, and prevents unbounded disk usage as well as minimizing
time spent replaying logs.

Lastly, there is the issue of updating the peer set when new servers are joining
or existing servers are leaving. As long as a quorum of nodes is available, this
is not an issue as Raft provides mechanisms to dynamically update the peer set.
If a quorum of nodes is unavailable, then this becomes a very challenging issue.
For example, suppose there are only 2 peers, A and B. The quorum size is also
2, meaning both nodes must agree to commit a log entry. If either A or B fails,
it is now impossible to reach quorum. This means the cluster is unable to add,
or remove a node, or commit any additional log entries. This results in *unavailability*.
At this point, manual intervention would be required to remove either A or B,
and to restart the remaining node in bootstrap mode.

A Raft cluster of 3 nodes can tolerate a single node failure, while a cluster
of 5 can tolerate 2 node failures. The recommended configuration is to either
run 3 or 5 raft servers. This maximizes availability without
greatly sacrificing performance.

In terms of performance, Raft is comparable to Paxos. Assuming stable leadership,
committing a log entry requires a single round trip to half of the cluster.
Thus performance is bound by disk I/O and network latency.

# uuid [![Build Status](https://travis-ci.org/hashicorp/go-uuid.svg?branch=master)](https://travis-ci.org/hashicorp/go-uuid)

Generates UUID-format strings using high quality, purely random bytes. It can also parse UUID-format strings into their component bytes.

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
go-syslog
=========

This repository provides a very simple `gsyslog` package. The point of this
package is to allow safe importing of syslog without introducing cross-compilation
issues. The stdlib `log/syslog` cannot be imported on Windows systems, and without
conditional compilation this adds complications.

Instead, `gsyslog` provides a very simple wrapper around `log/syslog` but returns
a runtime error if attempting to initialize on a non Linux or OSX system.

# Go Checkpoint Client

[Checkpoint](http://checkpoint.hashicorp.com) is an internal service at
Hashicorp that we use to check version information, broadcoast security
bulletins, etc.

We understand that software making remote calls over the internet
for any reason can be undesirable. Because of this, Checkpoint can be
disabled in all of our software that includes it. You can view the source
of this client to see that we're not sending any private information.

Each Hashicorp application has it's specific configuration option
to disable chekpoint calls, but the `CHECKPOINT_DISABLE` makes
the underlying checkpoint component itself disabled. For example
in the case of packer:
```
CHECKPOINT_DISABLE=1 packer build 
```

**Note:** This repository is probably useless outside of internal HashiCorp
use. It is open source for disclosure and because our open source projects
must be able to link to it.
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
	if errwrap.Contains(err, ErrNotExist) {
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

memberlist is based on ["SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol"](http://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf),
with a few minor adaptations, mostly to increase propagation speed and
convergence rate.

A high level overview of the memberlist protocol (based on SWIM) is
described below, but for details please read the full
[SWIM paper](http://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf)
followed by the memberlist source. We welcome any questions related
to the protocol on our issue tracker.

### Protocol Description

memberlist begins by joining an existing cluster or starting a new
cluster. If starting a new cluster, additional nodes are expected to join
it. New nodes in an existing cluster must be given the address of at
least one existing member in order to join the cluster. The new member
does a full state sync with the existing member over TCP and begins gossiping its
existence to the cluster.

Gossip is done over UDP with a configurable but fixed fanout and interval.
This ensures that network usage is constant with regards to number of nodes, as opposed to
exponential growth that can occur with traditional heartbeat mechanisms.
Complete state exchanges with a random node are done periodically over
TCP, but much less often than gossip messages. This increases the likelihood
that the membership list converges properly since the full state is exchanged
and merged. The interval between full state exchanges is configurable or can
be disabled entirely.

Failure detection is done by periodic random probing using a configurable interval.
If the node fails to ack within a reasonable time (typically some multiple
of RTT), then an indirect probe as well as a direct TCP probe are attempted. An
indirect probe asks a configurable number of random nodes to probe the same node,
in case there are network issues causing our own node to fail the probe. The direct
TCP probe is used to help identify the common situation where networking is
misconfigured to allow TCP but not UDP. Without the TCP probe, a UDP-isolated node
would think all other nodes were suspect and could cause churn in the cluster when
it attempts a TCP-based state exchange with another node. It is not desirable to
operate with only TCP connectivity because convergence will be much slower, but it
is enabled so that memberlist can detect this situation and alert operators.

If both our probe, the indirect probes, and the direct TCP probe fail within a
configurable time, then the node is marked "suspicious" and this knowledge is
gossiped to the cluster. A suspicious node is still considered a member of
cluster. If the suspect member of the cluster does not dispute the suspicion
within a configurable period of time, the node is finally considered dead,
and this state is then gossiped to the cluster.

This is a brief and incomplete description of the protocol. For a better idea,
please read the
[SWIM paper](http://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf)
in its entirety, along with the memberlist source code.

### Changes from SWIM

As mentioned earlier, the memberlist protocol is based on SWIM but includes
minor changes, mostly to increase propagation speed and convergence rates.

The changes from SWIM are noted here:

* memberlist does a full state sync over TCP periodically. SWIM only propagates
  changes over gossip. While both eventually reach convergence, the full state
  sync increases the likelihood that nodes are fully converged more quickly,
  at the expense of more bandwidth usage. This feature can be totally disabled
  if you wish.

* memberlist has a dedicated gossip layer separate from the failure detection
  protocol. SWIM only piggybacks gossip messages on top of probe/ack messages.
  memberlist also piggybacks gossip messages on top of probe/ack messages, but
  also will periodically send out dedicated gossip messages on their own. This
  feature lets you have a higher gossip rate (for example once per 200ms)
  and a slower failure detection rate (such as once per second), resulting
  in overall faster convergence rates and data propagation speeds. This feature
  can be totally disabed as well, if you wish.

* memberlist stores around the state of dead nodes for a set amount of time,
  so that when full syncs are requested, the requester also receives information
  about dead nodes. Because SWIM doesn't do full syncs, SWIM deletes dead node
  state immediately upon learning that the node is dead. This change again helps
  the cluster converge more quickly.
# net-rpc-msgpackrpc

This library provides the same functions as `net/rpc/jsonrpc` but for
communicating with [MessagePack](http://msgpack.org/) instead. The library
is modeled directly after the Go standard library so it should be easy to
use and obvious.

See the [GoDoc](http://godoc.org/github.com/hashicorp/net-rpc-msgpackrpc) for
API documentation.
# Consul `types` Package

The Go language has a strong type system built into the language.  The
`types` package corrals named types into a single package that is terminal in
`go`'s import graph.  The `types` package should not have any downstream
dependencies.  Each subsystem that defines its own set of types exists in its
own file, but all types are defined in the same package.

# Why

> Everything should be made as simple as possible, but not simpler.

`string` is a useful container and underlying type for identifiers, however
the `string` type is effectively opaque to the compiler in terms of how a
given string is intended to be used.  For instance, there is nothing
preventing the following from happening:

```go
// `map` of Widgets, looked up by ID
var widgetLookup map[string]*Widget
// ...
var widgetID string = "widgetID"
w, found := widgetLookup[widgetID]

// Bad!
var widgetName string = "name of widget"
w, found := widgetLookup[widgetName]
```

but this class of problem is entirely preventable:

```go
type WidgetID string
var widgetLookup map[WidgetID]*Widget
var widgetName
```

TL;DR: intentions and idioms aren't statically checked by compilers.  The
`types` package uses Go's strong type system to prevent this class of bug.
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
Consul Testing Utilities
========================

This package provides some generic helpers to facilitate testing in Consul.

TestServer
==========

TestServer is a harness for managing Consul agents and initializing them with
test data. Using it, you can form test clusters, create services, add health
checks, manipulate the K/V store, etc. This test harness is completely decoupled
from Consul's core and API client, meaning it can be easily imported and used in
external unit tests for various applications. It works by invoking the Consul
CLI, which means it is a requirement to have Consul installed in the `$PATH`.

Following is an example usage:

```go
package my_program

import (
	"testing"

	"github.com/hashicorp/consul/consul/structs"
	"github.com/hashicorp/consul/testutil"
)

func TestMain(t *testing.T) {
	// Create a test Consul server
	srv1 := testutil.NewTestServer(t)
	defer srv1.Stop()

	// Create a secondary server, passing in configuration
	// to avoid bootstrapping as we are forming a cluster.
	srv2 := testutil.NewTestServerConfig(t, func(c *testutil.TestServerConfig) {
		c.Bootstrap = false
	})
	defer srv2.Stop()

	// Join the servers together
	srv1.JoinLAN(srv2.LANAddr)

	// Create a test key/value pair
	srv1.SetKV("foo", []byte("bar"))

	// Create lots of test key/value pairs
	srv1.PopulateKV(map[string][]byte{
		"bar": []byte("123"),
		"baz": []byte("456"),
	})

	// Create a service
	srv1.AddService("redis", structs.HealthPassing, []string{"master"})

	// Create a service check
	srv1.AddCheck("service:redis", "redis", structs.HealthPassing)

	// Create a node check
	srv1.AddCheck("mem", "", structs.HealthCritical)

	// The HTTPAddr field contains the address of the Consul
	// API on the new test server instance.
	println(srv1.HTTPAddr)
}
```
go-retryablehttp
================

[![Build Status](http://img.shields.io/travis/hashicorp/go-retryablehttp.svg?style=flat-square)][travis]
[![Go Documentation](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)][godocs]

[travis]: http://travis-ci.org/hashicorp/go-retryablehttp
[godocs]: http://godoc.org/github.com/hashicorp/go-retryablehttp

The `retryablehttp` package provides a familiar HTTP client interface with
automatic retries and exponential backoff. It is a thin wrapper over the
standard `net/http` client library and exposes nearly the same public API. This
makes `retryablehttp` very easy to drop into existing programs.

`retryablehttp` performs automatic retries under certain conditions. Mainly, if
an error is returned by the client (connection errors, etc.), or if a 500-range
response code is received, then a retry is invoked after a wait period.
Otherwise, the response is returned and left to the caller to interpret.

The main difference from `net/http` is that requests which take a request body
(POST/PUT et. al) require an `io.ReadSeeker` to be provided. This enables the
request body to be "rewound" if the initial request fails so that the full
request can be attempted again.

Example Use
===========

Using this library should look almost identical to what you would do with
`net/http`. The most simple example of a GET request is shown below:

```go
resp, err := retryablehttp.Get("/foo")
if err != nil {
    panic(err)
}
```

The returned response object is an `*http.Response`, the same thing you would
usually get from `net/http`. Had the request failed one or more times, the above
call would block and retry with exponential backoff.

For more usage and examples see the
[godoc](http://godoc.org/github.com/hashicorp/go-retryablehttp).
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
# go-reap

Provides a super simple set of functions for reaping child processes. This is
useful for running applications as PID 1 in a Docker container.

Note that a mutex is supplied to allow your application to prevent reaping of
child processes during certain periods. You need to use care in order to
prevent the reaper from stealing your return values from uses of packages like
Go's exec. We use an `RWMutex` so that we don't serialize all of your
application's execution of sub processes with each other, but we do serialize
them with reaping. Your application should get a read lock when it wants to do
a wait and be safe from the reaper.

This should be supported on most UNIX flavors, but is not supported on Windows
or Solaris. Unsupported platforms have a stub implementation that's safe to call,
as well as an API to check if reaping is supported so that you can produce an
error in your application code.

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/hashicorp/go-reap).

Example
=======

Below is a simple example of usage

```go
// Reap children with no control or feedback.
go ReapChildren(nil, nil, nil)

// Get feedback on reaped children and errors.
if reap.IsSupported() {
	pids := make(reap.PidCh, 1)
	errors := make(reap.ErrorCh, 1)
	done := make(chan struct{})
	var reapLock sync.RWMutex
	go ReapChildren(pids, errors, done, &reapLock)
	// ...
	close(done)
} else {
	fmt.Println("Sorry, go-reap isn't supported on your platform.")
}
```

# SCADA Client

This library provides a Golang client for the [HashiCorp SCADA service](http://scada.hashicorp.com).
SCADA stands for Supervisory Control And Data Acquisition, and as the name implies it allows
[Atlas](https://atlas.hashicorp.com) to provide control functions and request data from the tools that integrate.

The technical details about how SCADA works are fairly simple. Clients first open a connection to
the SCADA service at scada.hashicorp.com on port 7223. This connection is secured by TLS, allowing
clients to verify the identity of the servers and to encrypt all communications. Once connected, a
handshake is performed where a client provides it's Atlas API credentials so that Atlas can verify
the client identity. Once complete, clients keep the connection open in an idle state waiting for
commands to be received. Commands map to APIs exposed by the product, and are subject to any ACLs,
authentication or authorization mechanisms of the client.

This library is used in various HashiCorp products to integrate with the SCADA system.

## Environmental Variables

This library respects the following environment variables:

* ATLAS_TOKEN: The Atlas token to use for authentication
* SCADA_ENDPOINT: Overrides the default SCADA endpoint

## Legacy API type versions

This package includes types for legacy API versions. The stable version of the API types live in `api/types/*.go`.

Consider moving a type here when you need to keep backwards compatibility in the API. This legacy types are organized by the latest API version they appear in. For instance, types in the `v1p19` package are valid for API versions below or equal `1.19`. Types in the `v1p20` package are valid for the API version `1.20`, since the versions below that will use the legacy types in `v1p19`.

### Package name conventions

The package name convention is to use `v` as a prefix for the version number and `p`(patch) as a separator. We use this nomenclature due to a few restrictions in the Go package name convention:

1. We cannot use `.` because it's interpreted by the language, think of `v1.20.CallFunction`.
2. We cannot use `_` because golint complains about it. The code is actually valid, but it looks probably more weird: `v1_20.CallFunction`.

For instance, if you want to modify a type that was available in the version `1.21` of the API but it will have different fields in the version `1.22`, you want to create a new package under `api/types/versions/v1p21`.
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

1. To automatically generate documentation.
2. To automatically generate the Go server and client. (A work-in-progress.)
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
This project was automatically exported from code.google.com/p/go-uuid

# uuid ![build status](https://travis-ci.org/pborman/uuid.svg?branch=master)
The uuid package generates and inspects UUIDs based on [RFC 412](http://tools.ietf.org/html/rfc4122) and DCE 1.1: Authentication and Security Services. 

###### Install
`go get github.com/pborman/uuid`

###### Documentation 
[![GoDoc](https://godoc.org/github.com/pborman/uuid?status.svg)](http://godoc.org/github.com/pborman/uuid)

Full `go doc` style documentation for the package can be viewed online without installing this package by using the GoDoc site here: 
http://godoc.org/github.com/pborman/uuid
Bolt [![Coverage Status](https://coveralls.io/repos/boltdb/bolt/badge.svg?branch=master)](https://coveralls.io/r/boltdb/bolt?branch=master) [![GoDoc](https://godoc.org/github.com/boltdb/bolt?status.svg)](https://godoc.org/github.com/boltdb/bolt) ![Version](https://img.shields.io/badge/version-1.0-green.svg)
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

Bolt is stable and the API is fixed. Full unit test coverage and randomized
black box testing are used to ensure database consistency and thread safety.
Bolt is currently in high-load production environments serving databases as
large as 1TB. Many companies such as Shopify and Heroku use Bolt-backed
services every day.

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
You can use the `Tx.Begin()` function directly but **please** be sure to close
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
        id, _ = b.NextSequence()
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
contstructor that takes in a filepath where the database file will be stored.
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
* [SkyDB](https://github.com/skydb/sky) - Behavioral analytics database.
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
* [Storm](https://github.com/asdine/storm) - A simple ORM around BoltDB.
* [GoWebApp](https://github.com/josephspurrier/gowebapp) - A basic MVC web application in Go using BoltDB.
* [SimpleBolt](https://github.com/xyproto/simplebolt) - A simple way to use BoltDB. Deals mainly with strings.
* [Algernon](https://github.com/xyproto/algernon) - A HTTP/2 web server with built-in support for Lua. Uses BoltDB as the default database backend.

If you are using Bolt in a project please send a pull request to add it to the list.
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
# Pods Library

This library provides functionality for launching and executing pod manifests. For integration with the intent store, see the intent package or preparer packages.# Replication: facilities for scheduling a pod across multiple nodes

The intent store is a relatively open book - for maintenance and introspection purposes, it should be modifable by users. This facility allows declarative management of a pod across multiple nodes, with potentially different leader/follower or other configurations.

Replication is managed by clients exclusively. The only state tracked by these utilities are the manifests found in the intent store.

# General usage

```
package mycorp

import (
    "fmt"

    "github.com/square/p2/pkg/allocation"
    "github.com/square/p2/pkg/health"
    "github.com/square/p2/pkg/pods"
    "github.com/square/p2/pkg/store/consul"
    "github.com/square/p2/pkg/replication"
    "github.com/mycorp/myp2allocator"
)

func LaunchMysqlPod(mysqlManfiest pods.PodManifest, allocator allocation.Allocator, store consul.Store, healthChecker *health.Checker) (replication.Result, error){
    request := allocation.Request {
        Manifest: mysqlManifest,
        Replicas: 3,
    }
    allocated, err := allocator.Allocate(request)
    master := allocated.MasterNode()
    if !master.Valid() {
        return nil, fmt.Errorf("No ste")
    }
    mysqlManifest.Config["master_node"] = master.Name
    if err != nil {
        return nil, fmt.Errorf("Could not allocate for pod %s: %s", mysqlManifest.Id, err)
    }

    replicator := replication.NewReplicator(mysqlManifest, allocated)
    replicator.MinimumNodes = 2
    return replicator.Enact(store, healthChecker)
}
```

This example code allocates and deploys 3 instances of the given MySQL pod to different nodes and updates the pod manifest's configuration.
# Go Language Utilities

Sparingly added utilities. New things in here should be thoughtful. Reflection utilities / AOP / other magic will be judged appropriately.# `p2` Hooks

Hooks are code that may execute at predefined moments in the `p2` preparer workflow. Hooks are registered in a fashion similar to pods, although several key differences exist between pods, intended as applications, and hooks.

Hooks can be declared and deployed using the `p2-hook` utility. Here is an example creating and deploying a hook that sets up the right application users before the application is launched. `p2-hook` can be run on any host with access to the Consul cluster.

```bash
$ echo '#!/bin/bash
useradd -D -d /data/pods/$POD_ID $POD_ID
' > ensure_user
$ chmod o+x ensure_user
$ MANIFEST=$(p2-bin2pod ensure_user | jq '.["manifest_path"]')
$ p2-schedule --hook-type before_install $MANIFEST
```

This hook establishes that the user running your application is present on the host before any launchable begins.

## Hook Constraints

Hooks are run as the user running the preparer. This will be root for most installations. Any future authentication mechanism will be required when scheduling hooks as they permit the rapid deployment of code that will execute as root in your cluster. Needless to say, `p2` is still in development and we do not recommend deploying it in production yet.

Hooks run with time restrictions. After 30 seconds, the preparer will send the hook SIGTERM and proceed with operations. At 60 seconds if the hook is still running, the preparer will send a SIGKILL.

Finally, hooks cannot alter the execution of the preparer, even if they fail. This is a safety feature similar to the timeouts. This prevents a broken hook from preventing deploys across your cluster.

## Fundamental Hooks Design

At its root, `p2`'s hooks are simply a directory of scripts that are executed during the install and launch phases of `p2` launchables. Each directory can be populated independently of `p2`. However, the `p2-preparer` comes with an option to register all pod manifests and their launchables at `/hooks` as scripts that will be symlinked into this directory. The option is on by default.

## Layout

Values in the `/hooks` keyspace are mapped to hooks on disk in the following manner. For a key value of `/hooks/{event}/{manifest}`, every preparer should install a new pod under `/data/hooks/pods/{event}/{manifest}`. The layout of the pod directory is identical to that of normal applications.

The layout of hooks on disk is somewhat complex, owing to the reuse of the pod design. While somewhat complex, this reuse gives hook implementors all the power of standard `p2` ideas. For the most part, clients shouldn't need to understand how `p2` lays out hooks on disk.

Instead of setting up runit services for each launch script, `p2` instead finds each launch file and symlinks it into the appropriate exec directory. For example, for a hook that adds appropriate sudoers entries given a manifest, if the hook script is in a pod identified as `system` under a launchable called `sudoers`, the hook script will be installed at `/data/hooks/pods/before_install/system/sudoers/current/bin/launch` and it will be symlinked to `/data/hooks/exec/before_install/system_sudoers_launch`.

For launch directories instead of launch scripts, each launch script will be installed into the event directory as needed.
# Functional Tests for P2

This directory contains test scripts that are run against an operating p2 cluster.

Tests have one or more (possibly para-)virtualized machines made accessible with a common setup. This includes:

* Installing the current version of Go
* Setting up important Go variables
* Installing all p2 binaries

## Test layout

```
|──integration
│   ├── common-provision.sh
│   ╰── single-node-slug-deploy
│       ├── check.go
│       ╰── Vagrantfile
```

In this example, `single-node-slug-deploy` is a test case that will execute in the context of the virtual machine spawned by the given Vagrantfile. Consequently, executions are limited to OS X for the time being.

Future versions of this may include the use of the [AWS provider in Vagrant](https://github.com/mitchellh/vagrant-aws) to host many nodes in a single p2 cluster.

## Running the integration tests

1) Install Vagrant
2) If you are using VirtualBox you will likely need the vagrant-vbguest plugin. This can be installed with the following command: vagrant plugin install vagrant-vbguest
3) From the root of the p2 repo run the following command: rake integration
# System Dependencies for P2

These are provided with zero guarantees about their stability or safety. It is strongly encouraged that real production environments establish their own build process for these RPMs.# Hello app

This directory contains the source for the "hello" pod which is used in the
integration tests. All it does is read the port it should run on from its
config and responds to HTTP requests to '/'. The binary is compiled and built
as a hoist artifact in hoisted-hello_def456.tar.gz so that the integration test
does not need to actually compile anyand built as a hoist artifact in
hoisted-hello_def456.tar.gz so that the integration test does not need to
actually compile anything.

## To update:

* modify the source
* $ go build # on linux 
* $ p2-bin2pod hello # generates a hoist artifact containing the binary
* $ mv <tar_gz_location> ../hoisted-hello_def456.tar.gz
* $ gpg --no-default-keyring --keyring integration/single-node-slug-deploy/pubring.gpg \
  --secret-keyring integration/single-node-slug-deploy/secring.gpg -u p2universe --out \
  integration/hoisted-hello_def456.tar.gz.sig --detach-sign integration/hoisted-hello_def456.tar.gz
* remove the other files

# config.json

config.json is a runc configuration file that is used to run hello as an
"opencontainer" launchable type. In order to do that, the "rootfs" directory
must be added alongside config.json containing all the files that should be present in the container's filesytem.

The integration tests (specifically integration/common-provision.sh and
integration/travis.sh) use docker to pull down a centos7 image, use "docker
extract" to turn it into a tar, and extract the tar in order to provide the
rootfs directory. This is to avoid putting the full image in git

The config.json file was generated by running "runc spec" to generate a default config.json file, and then the following modifications were made:

* set the terminal flag to "false"
* modify the arguments to be /usr/local/bin/hello (instead of /bin/sh)
* remove the network namespace. This is necessary so that the integration test
  running outside of the container can access the port that hello is running on
  inside the container
* remove the cgroups mount. It's not needed and it can cause problems if the
  host machine doesn't have cgroup capability
# p2-inspect

`p2-inspect` is a tool for examining the state of a p2 cluster. Given the address of any consul agent, it will pull the manifest SHAs and health checks for all the pods running in the cluster, across all its nodes. Example:

```bash
$ p2-inspect | python -mjson.tool
```

```json
{
    "isup": {
        "aws1.example.com": {
            "health_check": {
                "output": "[/data/pods/isup/isup/installs/isup_vsjlzlxvnkizuxmkutqmkqhwukyryztuxhusnkpm/bin/launch]\n[PATH=/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin TERM=linux RUNLEVEL=3 PREVLEVEL=N UPSTART_EVENTS=runlevel UPSTART_JOB=runit UPSTART_INSTANCE= CONFIG_PATH=/data/pods/isup/config/isup_717cc0d58df240e2668c865cdc063d715446e6db09ad4b64f7a2f0f4e361ea8f.yaml]\n",
                "status": "passing"
            },
            "intent_manifest_sha": "717cc0d58df240e2668c865cdc063d715446e6db09ad4b64f7a2f0f4e361ea8f",
            "reality_manifest_sha": "717cc0d58df240e2668c865cdc063d715446e6db09ad4b64f7a2f0f4e361ea8f"
        },
        "aws2.example.com": {
            "health_check": {
                "output": "[/data/pods/isup/isup/installs/isup_tkkhnurngovsomvzikznymgmluohzjvniwzrtpxq/bin/launch]\n[PATH=/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin TERM=linux RUNLEVEL=3 PREVLEVEL=N UPSTART_EVENTS=runlevel UPSTART_JOB=runit UPSTART_INSTANCE= CONFIG_PATH=/data/pods/isup/config/isup_b56d3c3fd3c264841c8aad6a9ce6f06271a62dc6daffeef0efb6b50d86424bc6.yaml]\n",
                "status": "passing"
            },
            "intent_manifest_sha": "b56d3c3fd3c264841c8aad6a9ce6f06271a62dc6daffeef0efb6b50d86424bc6",
            "reality_manifest_sha": "b56d3c3fd3c264841c8aad6a9ce6f06271a62dc6daffeef0efb6b50d86424bc6"
        }
    },
    "p2-preparer": {
        "aws1.example.com": {
            "intent_manifest_sha": "9b9c7cb38b9a68564d6d582c05298cd3dab02e9d22c8178e407eaaee0726169e",
            "reality_manifest_sha": "9b9c7cb38b9a68564d6d582c05298cd3dab02e9d22c8178e407eaaee0726169e"
        },
        "aws2.example.com": {
            "intent_manifest_sha": "9b9c7cb38b9a68564d6d582c05298cd3dab02e9d22c8178e407eaaee0726169e",
            "reality_manifest_sha": "9b9c7cb38b9a68564d6d582c05298cd3dab02e9d22c8178e407eaaee0726169e"
        },
        "aws3.example.com": {
            "intent_manifest_sha": "9b9c7cb38b9a68564d6d582c05298cd3dab02e9d22c8178e407eaaee0726169e",
            "reality_manifest_sha": "9b9c7cb38b9a68564d6d582c05298cd3dab02e9d22c8178e407eaaee0726169e"
        }
    }
}
```

This indicates that there are three nodes running the `p2-preparer` pod. This pod has no health check; hence there is no `health_check` object in the JSON. Meanwhile, there are also two instances of the `isup` pod. These pods both have passing health checks, and their health check scripts produced some output that you can see in the JSON above.

You can filter by pod ID, by node name, or by both:

```bash
$ p2-inspect --node aws1.example.com --pod isup | python -m json.tool
```

```json
{
    "isup": {
        "aws1.example.com": {
            "health_check": {
                "output": "[/data/pods/isup/isup/installs/isup_vsjlzlxvnkizuxmkutqmkqhwukyryztuxhusnkpm/bin/launch]\n[PATH=/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin TERM=linux RUNLEVEL=3 PREVLEVEL=N UPSTART_EVENTS=runlevel UPSTART_JOB=runit UPSTART_INSTANCE= CONFIG_PATH=/data/pods/isup/config/isup_717cc0d58df240e2668c865cdc063d715446e6db09ad4b64f7a2f0f4e361ea8f.yaml]\n",
                "status": "passing"
            },
            "intent_manifest_sha": "717cc0d58df240e2668c865cdc063d715446e6db09ad4b64f7a2f0f4e361ea8f",
            "reality_manifest_sha": "717cc0d58df240e2668c865cdc063d715446e6db09ad4b64f7a2f0f4e361ea8f"
        }
    }
}
```
# Platypus Bootstrap

This is a simple binary that sets up the necessary agents on a target host. The intent of bootstrap is to only be used during the very beginning of initialization of new nodes. Following that, the node should be self-updating using the same deployment mechanisms as other pods.

