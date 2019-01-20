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
Would ping: 1.2.3.4 with timeout 5s and count 5
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
    --name=FULL-NAME      // Flag(...).PlaceHolder("FULL-NAME").Default("Harry").String()

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
**go-metrics-prometheus**
[![Build Status](https://api.travis-ci.org/deathowl/go-metrics-prometheus.svg)](https://travis-ci.org/deathowl/go-metrics-prometheus)

This is a reporter for the go-metrics library which will post the metrics to the prometheus client registry . It just updates the registry, taking care of exporting the metrics is still your responsibility.


Usage:

```

	import "github.com/deathowl/go-metrics-prometheus"
	import "github.com/prometheus/client_golang/prometheus"

    	prometheusRegistry := prometheus.NewRegistry()
        metricsRegistry := metrics.NewRegistry()
        pClient := NewPrometheusProvider(metricsRegistry, "test", "subsys", prometheusRegistry, 1*time.Second)
        go pClient.UpdatePrometheusMetrics()
```

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
# HTTP CONNECT tunneling Go Dialer

[![Travis Build](https://travis-ci.org/mwitkow/go-http-dialer.svg)](https://travis-ci.org/mwitkow/go-http-dialer)
[![Go Report Card](https://goreportcard.com/badge/github.com/mwitkow/go-http-dialer)](http://goreportcard.com/report/mwitkow/go-http-dialer)
[![GoDoc](http://img.shields.io/badge/GoDoc-Reference-blue.svg)](https://godoc.org/github.com/mwitkow/go-http-dialer)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A `net.Dialer` drop-in that establishes the TCP connection over an [HTTP CONNECT Tunnel](https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_tunneling).

## Why?!

Some enterprises have fairly restrictive networking environments. They typically operate [HTTP forward proxies](https://en.wikipedia.org/wiki/Proxy_server) that require user authentication. These proxies usually allow  HTTPS (TCP to `:443`) to pass through the proxy using the [`CONNECT`](https://tools.ietf.org/html/rfc2616#section-9.9) method. The `CONNECT` method is basically a HTTP-negotiated "end-to-end" TCP stream... which is exactly what [`net.Conn`](https://golang.org/pkg/net/#Conn) is :)

## But, really, why?

Because if you want to call [gRPC](http://www.grpc.io/) services which are exposed publicly over `:443` TLS over an HTTP proxy, you can't.

Also, this allows you to call any TCP service over HTTP `CONNECT`... if your proxy allows you to `¯\(ツ)/¯`

## Supported features

 - [x] unencrypted connection to proxy (e.g. `http://proxy.example.com:3128`
 - [x] TLS connection to proxy (customizeable) (e.g. `https://proxy.example.com`)
 - [x] customizeable for `Proxy-Authenticate`, with challenge-response semantics
 - [x] out of the box support for `Basic` auth
 - [ ] appropriate `RemoteAddr` remapping
 

## Usage with gRPC



## License

`go-http-dialer` is released under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.
# PKCS#11 [![Build Status](https://travis-ci.org/miekg/pkcs11.png?branch=master)](https://travis-ci.org/miekg/pkcs11) [![GoDoc](https://img.shields.io/badge/godoc-reference-blue.svg)](http://godoc.org/github.com/miekg/pkcs11)

This is a Go implementation of the PKCS#11 API. It wraps the library closely, but uses Go idiom
were it makes sense. It has been tested with SoftHSM.

## SoftHSM

* Make it use a custom configuration file `export SOFTHSM_CONF=$PWD/softhsm.conf`

* Then use `softhsm` to init it

        softhsm --init-token --slot 0 --label test --pin 1234

* Then use `libsofthsm.so` as the pkcs11 module:
```go
        p := pkcs11.New("/usr/lib/softhsm/libsofthsm.so")
```
## Examples

A skeleton program would look somewhat like this (yes, pkcs#11 is verbose):
```go
    p := pkcs11.New("/usr/lib/softhsm/libsofthsm.so")
    err := p.Initialize()
    if err != nil {
        panic(err)
    }

    defer p.Destroy()
    defer p.Finalize()

    slots, err := p.GetSlotList(true)
    if err != nil {
        panic(err)
    }

    session, err := p.OpenSession(slots[0], pkcs11.CKF_SERIAL_SESSION|pkcs11.CKF_RW_SESSION)
    if err != nil {
        panic(err)
    }
    defer p.CloseSession(session)

    err = p.Login(session, pkcs11.CKU_USER, "1234")
    if err != nil {
        panic(err)
    }
    defer p.Logout(session)

    p.DigestInit(session, []*pkcs11.Mechanism{pkcs11.NewMechanism(pkcs11.CKM_SHA_1, nil)})
    hash, err := p.Digest(session, []byte("this is a string"))
    if err != nil {
        panic(err)
    }

    for _, d := range hash {
            fmt.Printf("%x", d)
    }
    fmt.Println()
```
Further examples are included in the tests.

To expose PKCS#11 keys using the
[crypto.Signer interface](https://golang.org/pkg/crypto/#Signer),
please see [github.com/thalesignite/crypto11](https://github.com/thalesignite/crypto11).

# TODO

* Fix/double check endian stuff, see types.go NewAttribute()
* Look at the memory copying in fast functions (sign, hash etc)
GoUtils
===========
[![Stability: Maintenance](https://masterminds.github.io/stability/maintenance.svg)](https://masterminds.github.io/stability/maintenance.html)
[![GoDoc](https://godoc.org/github.com/Masterminds/goutils?status.png)](https://godoc.org/github.com/Masterminds/goutils) [![Build Status](https://travis-ci.org/Masterminds/goutils.svg?branch=master)](https://travis-ci.org/Masterminds/goutils) [![Build status](https://ci.appveyor.com/api/projects/status/sc2b1ew0m7f0aiju?svg=true)](https://ci.appveyor.com/project/mattfarina/goutils)


GoUtils provides users with utility functions to manipulate strings in various ways. It is a Go implementation of some
string manipulation libraries of Java Apache Commons. GoUtils includes the following Java Apache Commons classes:
* WordUtils    
* RandomStringUtils  
* StringUtils (partial implementation)

## Installation
If you have Go set up on your system, from the GOPATH directory within the command line/terminal, enter this:

	go get github.com/Masterminds/goutils

If you do not have Go set up on your system, please follow the [Go installation directions from the documenation](http://golang.org/doc/install), and then follow the instructions above to install GoUtils.


## Documentation
GoUtils doc is available here: [![GoDoc](https://godoc.org/github.com/Masterminds/goutils?status.png)](https://godoc.org/github.com/Masterminds/goutils)


## Usage
The code snippets below show examples of how to use GoUtils. Some functions return errors while others do not. The first instance below, which does not return an error, is the `Initials` function (located within the `wordutils.go` file).

    package main

    import (
        "fmt"
    	"github.com/Masterminds/goutils"
    )

    func main() {

    	// EXAMPLE 1: A goutils function which returns no errors
        fmt.Println (goutils.Initials("John Doe Foo")) // Prints out "JDF"

    }
Some functions return errors mainly due to illegal arguements used as parameters. The code example below illustrates how to deal with function that returns an error. In this instance, the function is the `Random` function (located within the `randomstringutils.go` file).

    package main

    import (
        "fmt"
        "github.com/Masterminds/goutils"
    )

    func main() {

        // EXAMPLE 2: A goutils function which returns an error
        rand1, err1 := goutils.Random (-1, 0, 0, true, true)  

        if err1 != nil {
			fmt.Println(err1) // Prints out error message because -1 was entered as the first parameter in goutils.Random(...)
		} else {
			fmt.Println(rand1)
		}

    }

## License
GoUtils is licensed under the Apache License, Version 2.0. Please check the LICENSE.txt file or visit http://www.apache.org/licenses/LICENSE-2.0 for a copy of the license.

## Issue Reporting
Make suggestions or report issues using the Git issue tracker: https://github.com/Masterminds/goutils/issues

## Website
* [GoUtils webpage](http://Masterminds.github.io/goutils/)
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
# Sprig: Template functions for Go templates
[![Stability: Sustained](https://masterminds.github.io/stability/sustained.svg)](https://masterminds.github.io/stability/sustained.html)
[![Build Status](https://travis-ci.org/Masterminds/sprig.svg?branch=master)](https://travis-ci.org/Masterminds/sprig)

The Go language comes with a [built-in template
language](http://golang.org/pkg/text/template/), but not
very many template functions. This library provides a group of commonly
used template functions.

It is inspired by the template functions found in
[Twig](http://twig.sensiolabs.org/documentation) and also in various
JavaScript libraries, such as [underscore.js](http://underscorejs.org/).

## Usage

Template developers can read the [Sprig function documentation](http://masterminds.github.io/sprig/) to
learn about the >100 template functions available.

For Go developers wishing to include Sprig as a library in their programs,
API documentation is available [at GoDoc.org](http://godoc.org/github.com/Masterminds/sprig), but
read on for standard usage.

### Load the Sprig library

To load the Sprig `FuncMap`:

```go

import (
  "github.com/Masterminds/sprig"
  "html/template"
)

// This example illustrates that the FuncMap *must* be set before the
// templates themselves are loaded.
tpl := template.Must(
  template.New("base").Funcs(sprig.FuncMap()).ParseGlob("*.html")
)


```

### Call the functions inside of templates

By convention, all functions are lowercase. This seems to follow the Go
idiom for template functions (as opposed to template methods, which are
TitleCase).


Example:

```
{{ "hello!" | upper | repeat 5 }}
```

Produces:

```
HELLO!HELLO!HELLO!HELLO!HELLO!
```

## Principles:

The following principles were used in deciding on which functions to add, and
determining how to implement them.

- Template functions should be used to build layout. Therefore, the following
  types of operations are within the domain of template functions:
  - Formatting
  - Layout
  - Simple type conversions
  - Utilities that assist in handling common formatting and layout needs (e.g. arithmetic)
- Template functions should not return errors unless there is no way to print
  a sensible value. For example, converting a string to an integer should not
  produce an error if conversion fails. Instead, it should display a default
  value that can be displayed.
- Simple math is necessary for grid layouts, pagers, and so on. Complex math
  (anything other than arithmetic) should be done outside of templates.
- Template functions only deal with the data passed into them. They never retrieve
  data from a source.
- Finally, do not override core Go template functions.
# SemVer

The `semver` package provides the ability to work with [Semantic Versions](http://semver.org) in Go. Specifically it provides the ability to:

* Parse semantic versions
* Sort semantic versions
* Check if a semantic version fits within a set of constraints
* Optionally work with a `v` prefix

[![Stability:
Active](https://masterminds.github.io/stability/active.svg)](https://masterminds.github.io/stability/active.html)
[![Build Status](https://travis-ci.org/Masterminds/semver.svg)](https://travis-ci.org/Masterminds/semver) [![Build status](https://ci.appveyor.com/api/projects/status/jfk66lib7hb985k8/branch/master?svg=true&passingText=windows%20build%20passing&failingText=windows%20build%20failing)](https://ci.appveyor.com/project/mattfarina/semver/branch/master) [![GoDoc](https://godoc.org/github.com/Masterminds/semver?status.svg)](https://godoc.org/github.com/Masterminds/semver) [![Go Report Card](https://goreportcard.com/badge/github.com/Masterminds/semver)](https://goreportcard.com/report/github.com/Masterminds/semver)

## Parsing Semantic Versions

To parse a semantic version use the `NewVersion` function. For example,

```go
    v, err := semver.NewVersion("1.2.3-beta.1+build345")
```

If there is an error the version wasn't parseable. The version object has methods
to get the parts of the version, compare it to other versions, convert the
version back into a string, and get the original string. For more details
please see the [documentation](https://godoc.org/github.com/Masterminds/semver).

## Sorting Semantic Versions

A set of versions can be sorted using the [`sort`](https://golang.org/pkg/sort/)
package from the standard library. For example,

```go
    raw := []string{"1.2.3", "1.0", "1.3", "2", "0.4.2",}
    vs := make([]*semver.Version, len(raw))
	for i, r := range raw {
		v, err := semver.NewVersion(r)
		if err != nil {
			t.Errorf("Error parsing version: %s", err)
		}

		vs[i] = v
	}

	sort.Sort(semver.Collection(vs))
```

## Checking Version Constraints

Checking a version against version constraints is one of the most featureful
parts of the package.

```go
    c, err := semver.NewConstraint(">= 1.2.3")
    if err != nil {
        // Handle constraint not being parseable.
    }

    v, _ := semver.NewVersion("1.3")
    if err != nil {
        // Handle version not being parseable.
    }
    // Check if the version meets the constraints. The a variable will be true.
    a := c.Check(v)
```

## Basic Comparisons

There are two elements to the comparisons. First, a comparison string is a list
of comma separated and comparisons. These are then separated by || separated or
comparisons. For example, `">= 1.2, < 3.0.0 || >= 4.2.3"` is looking for a
comparison that's greater than or equal to 1.2 and less than 3.0.0 or is
greater than or equal to 4.2.3.

The basic comparisons are:

* `=`: equal (aliased to no operator)
* `!=`: not equal
* `>`: greater than
* `<`: less than
* `>=`: greater than or equal to
* `<=`: less than or equal to

_Note, according to the Semantic Version specification pre-releases may not be
API compliant with their release counterpart. It says,_

> _A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version._

_SemVer comparisons without a pre-release value will skip pre-release versions.
For example, `>1.2.3` will skip pre-releases when looking at a list of values
while `>1.2.3-alpha.1` will evaluate pre-releases._

## Hyphen Range Comparisons

There are multiple methods to handle ranges and the first is hyphens ranges.
These look like:

* `1.2 - 1.4.5` which is equivalent to `>= 1.2, <= 1.4.5`
* `2.3.4 - 4.5` which is equivalent to `>= 2.3.4, <= 4.5`

## Wildcards In Comparisons

The `x`, `X`, and `*` characters can be used as a wildcard character. This works
for all comparison operators. When used on the `=` operator it falls
back to the pack level comparison (see tilde below). For example,

* `1.2.x` is equivalent to `>= 1.2.0, < 1.3.0`
* `>= 1.2.x` is equivalent to `>= 1.2.0`
* `<= 2.x` is equivalent to `<= 3`
* `*` is equivalent to `>= 0.0.0`

## Tilde Range Comparisons (Patch)

The tilde (`~`) comparison operator is for patch level ranges when a minor
version is specified and major level changes when the minor number is missing.
For example,

* `~1.2.3` is equivalent to `>= 1.2.3, < 1.3.0`
* `~1` is equivalent to `>= 1, < 2`
* `~2.3` is equivalent to `>= 2.3, < 2.4`
* `~1.2.x` is equivalent to `>= 1.2.0, < 1.3.0`
* `~1.x` is equivalent to `>= 1, < 2`

## Caret Range Comparisons (Major)

The caret (`^`) comparison operator is for major level changes. This is useful
when comparisons of API versions as a major change is API breaking. For example,

* `^1.2.3` is equivalent to `>= 1.2.3, < 2.0.0`
* `^1.2.x` is equivalent to `>= 1.2.0, < 2.0.0`
* `^2.3` is equivalent to `>= 2.3, < 3`
* `^2.x` is equivalent to `>= 2.0.0, < 3`

# Validation

In addition to testing a version against a constraint, a version can be validated
against a constraint. When validation fails a slice of errors containing why a
version didn't meet the constraint is returned. For example,

```go
    c, err := semver.NewConstraint("<= 1.2.3, >= 1.4")
    if err != nil {
        // Handle constraint not being parseable.
    }

    v, _ := semver.NewVersion("1.3")
    if err != nil {
        // Handle version not being parseable.
    }

    // Validate a version against a constraint.
    a, msgs := c.Validate(v)
    // a is false
    for _, m := range msgs {
        fmt.Println(m)

        // Loops over the errors which would read
        // "1.3 is greater than 1.2.3"
        // "1.3 is less than 1.4"
    }
```

# Contribute

If you find an issue or want to contribute please file an [issue](https://github.com/Masterminds/semver/issues)
or [create a pull request](https://github.com/Masterminds/semver/pulls).
This is a reporter for the [go-metrics](https://github.com/rcrowley/go-metrics)
library which will post the metrics to Graphite. It was originally part of the
`go-metrics` library itself, but has been split off to make maintenance of
both the core library and the client easier.

### Usage

```go
import "github.com/cyberdelia/go-metrics-graphite"


go graphite.Graphite(metrics.DefaultRegistry,
  1*time.Second, "some.prefix", addr)
```

### Migrating from `rcrowley/go-metrics` implementation

Simply modify the import from `"github.com/rcrowley/go-metrics/graphite"` to
`"github.com/cyberdelia/go-metrics-graphite"` and it should Just Work.
# uuid ![build status](https://travis-ci.org/google/uuid.svg?branch=master)
The uuid package generates and inspects UUIDs based on
[RFC 4122](http://tools.ietf.org/html/rfc4122)
and DCE 1.1: Authentication and Security Services. 

This package is based on the github.com/pborman/uuid package (previously named
code.google.com/p/go-uuid).  It differs from these earlier packages in that
a UUID is a 16 byte array rather than a byte slice.  One loss due to this
change is the ability to represent an invalid UUID (vs a NIL UUID).

###### Install
`go get github.com/google/uuid`

###### Documentation 
[![GoDoc](https://godoc.org/github.com/google/uuid?status.svg)](http://godoc.org/github.com/google/uuid)

Full `go doc` style documentation for the package can be viewed online without
installing this package by using the GoDoc site here: 
http://godoc.org/github.com/google/uuid
# GO_REUSEPORT

[![Build Status](https://travis-ci.org/kavu/go_reuseport.png?branch=master)](https://travis-ci.org/kavu/go_reuseport)
[![codecov](https://codecov.io/gh/kavu/go_reuseport/branch/master/graph/badge.svg)](https://codecov.io/gh/kavu/go_reuseport)
[![GoDoc](https://godoc.org/github.com/kavu/go_reuseport?status.png)](https://godoc.org/github.com/kavu/go_reuseport)

**GO_REUSEPORT** is a little expirement to create a `net.Listener` that supports [SO_REUSEPORT](http://lwn.net/Articles/542629/) socket option.

For now, Darwin and Linux (from 3.9) systems are supported. I'll be pleased if you'll test other systems and tell me the results.
 documentation on [godoc.org](http://godoc.org/github.com/kavu/go_reuseport "go_reuseport documentation").

## Example ##

```go
package main

import (
  "fmt"
  "html"
  "net/http"
  "os"
  "runtime"
  "github.com/kavu/go_reuseport"
)

func main() {
  listener, err := reuseport.Listen("tcp", "localhost:8881")
  if err != nil {
    panic(err)
  }
  defer listener.Close()

  server := &http.Server{}
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    fmt.Println(os.Getgid())
    fmt.Fprintf(w, "Hello, %q\n", html.EscapeString(r.URL.Path))
  })

  panic(server.Serve(listener))
}
```

Now you can run several instances of this tiny server without `Address already in use` errors.

## Thanks

Inspired by [Artur Siekielski](https://github.com/aartur) [post](http://freeprogrammersblog.vhex.net/post/linux-39-introdued-new-way-of-writing-socket-servers/2) about `SO_REUSEPORT`.

Metrics
=======

Shared metrics collection package for square/ghostunnel and square/keywhiz-fs.
# JCEKS

Package jceks parses JCEKS (Java Cryptogaphy Extension Key Store)
files and extracts keys and certificates. This module only implements
a fraction of the JCEKS cryptographic protocols. In particular, it
implements the SHA1 signature verification of the key store and the
PBEWithMD5AndDES3CBC cipher for encrypting private keys.
# xstrings #

[![Build Status](https://travis-ci.org/huandu/xstrings.svg?branch=master)](https://travis-ci.org/huandu/xstrings)
[![GoDoc](https://godoc.org/github.com/huandu/xstrings?status.svg)](https://godoc.org/github.com/huandu/xstrings)

Go package [xstrings](https://godoc.org/github.com/huandu/xstrings) is a collection of string functions, which are widely used in other languages but absent in Go package [strings](http://golang.org/pkg/strings).

All functions are well tested and carefully tuned for performance.

## Propose a new function ##

Please review [contributing guideline](CONTRIBUTING.md) and [create new issue](https://github.com/huandu/xstrings/issues) to state why it should be included.

## Install ##

Use `go get` to install this library.

	go get github.com/huandu/xstrings

## API document ##

See [GoDoc](https://godoc.org/github.com/huandu/xstrings) for full document.

## Function list ##

Go functions have a unique naming style. One, who has experience in other language but new in Go, may have difficulties to find out right string function to use.

Here is a list of functions in [strings](http://golang.org/pkg/strings) and [xstrings](https://godoc.org/github.com/huandu/xstrings) with enough extra information about how to map these functions to their friends in other languages. Hope this list could be helpful for fresh gophers.

### Package `xstrings` functions ###

*Keep this table sorted by Function in ascending order.*

| Function | Friends | # |
| -------- | ------- | --- |
| [Center](https://godoc.org/github.com/huandu/xstrings#Center) | `str.center` in Python; `String#center` in Ruby | [#30](https://github.com/huandu/xstrings/issues/30) |
| [Count](https://godoc.org/github.com/huandu/xstrings#Count) | `String#count` in Ruby | [#16](https://github.com/huandu/xstrings/issues/16) |
| [Delete](https://godoc.org/github.com/huandu/xstrings#Delete) | `String#delete` in Ruby | [#17](https://github.com/huandu/xstrings/issues/17) |
| [ExpandTabs](https://godoc.org/github.com/huandu/xstrings#ExpandTabs) | `str.expandtabs` in Python | [#27](https://github.com/huandu/xstrings/issues/27) |
| [FirstRuneToLower](https://godoc.org/github.com/huandu/xstrings#FirstRuneToLower) | `lcfirst` in PHP or Perl | [#15](https://github.com/huandu/xstrings/issues/15) |
| [FirstRuneToUpper](https://godoc.org/github.com/huandu/xstrings#FirstRuneToUpper) | `String#capitalize` in Ruby; `ucfirst` in PHP or Perl | [#15](https://github.com/huandu/xstrings/issues/15) |
| [Insert](https://godoc.org/github.com/huandu/xstrings#Insert) | `String#insert` in Ruby | [#18](https://github.com/huandu/xstrings/issues/18) |
| [LastPartition](https://godoc.org/github.com/huandu/xstrings#LastPartition) | `str.rpartition` in Python; `String#rpartition` in Ruby | [#19](https://github.com/huandu/xstrings/issues/19) |
| [LeftJustify](https://godoc.org/github.com/huandu/xstrings#LeftJustify) | `str.ljust` in Python; `String#ljust` in Ruby | [#28](https://github.com/huandu/xstrings/issues/28) |
| [Len](https://godoc.org/github.com/huandu/xstrings#Len) | `mb_strlen` in PHP | [#23](https://github.com/huandu/xstrings/issues/23) |
| [Partition](https://godoc.org/github.com/huandu/xstrings#Partition) | `str.partition` in Python; `String#partition` in Ruby | [#10](https://github.com/huandu/xstrings/issues/10) |
| [Reverse](https://godoc.org/github.com/huandu/xstrings#Reverse) | `String#reverse` in Ruby; `strrev` in PHP; `reverse` in Perl | [#7](https://github.com/huandu/xstrings/issues/7) |
| [RightJustify](https://godoc.org/github.com/huandu/xstrings#RightJustify) | `str.rjust` in Python; `String#rjust` in Ruby | [#29](https://github.com/huandu/xstrings/issues/29) |
| [RuneWidth](https://godoc.org/github.com/huandu/xstrings#RuneWidth) | - | [#27](https://github.com/huandu/xstrings/issues/27) |
| [Scrub](https://godoc.org/github.com/huandu/xstrings#Scrub) | `String#scrub` in Ruby | [#20](https://github.com/huandu/xstrings/issues/20) |
| [Shuffle](https://godoc.org/github.com/huandu/xstrings#Shuffle) | `str_shuffle` in PHP | [#13](https://github.com/huandu/xstrings/issues/13) |
| [ShuffleSource](https://godoc.org/github.com/huandu/xstrings#ShuffleSource) | `str_shuffle` in PHP | [#13](https://github.com/huandu/xstrings/issues/13) |
| [Slice](https://godoc.org/github.com/huandu/xstrings#Slice) | `mb_substr` in PHP | [#9](https://github.com/huandu/xstrings/issues/9) |
| [Squeeze](https://godoc.org/github.com/huandu/xstrings#Squeeze) | `String#squeeze` in Ruby | [#11](https://github.com/huandu/xstrings/issues/11) |
| [Successor](https://godoc.org/github.com/huandu/xstrings#Successor) | `String#succ` or `String#next` in Ruby | [#22](https://github.com/huandu/xstrings/issues/22) |
| [SwapCase](https://godoc.org/github.com/huandu/xstrings#SwapCase) | `str.swapcase` in Python; `String#swapcase` in Ruby | [#12](https://github.com/huandu/xstrings/issues/12) |
| [ToCamelCase](https://godoc.org/github.com/huandu/xstrings#ToCamelCase) | `String#camelize` in RoR | [#1](https://github.com/huandu/xstrings/issues/1) |
| [ToKebab](https://godoc.org/github.com/huandu/xstrings#ToKebabCase) | - | [#41](https://github.com/huandu/xstrings/issues/41) |
| [ToSnakeCase](https://godoc.org/github.com/huandu/xstrings#ToSnakeCase) | `String#underscore` in RoR | [#1](https://github.com/huandu/xstrings/issues/1) |
| [Translate](https://godoc.org/github.com/huandu/xstrings#Translate) | `str.translate` in Python; `String#tr` in Ruby; `strtr` in PHP; `tr///` in Perl | [#21](https://github.com/huandu/xstrings/issues/21) |
| [Width](https://godoc.org/github.com/huandu/xstrings#Width) | `mb_strwidth` in PHP | [#26](https://github.com/huandu/xstrings/issues/26) |
| [WordCount](https://godoc.org/github.com/huandu/xstrings#WordCount) | `str_word_count` in PHP | [#14](https://github.com/huandu/xstrings/issues/14) |
| [WordSplit](https://godoc.org/github.com/huandu/xstrings#WordSplit) | - | [#14](https://github.com/huandu/xstrings/issues/14) |

### Package `strings` functions ###

*Keep this table sorted by Function in ascending order.*

| Function | Friends |
| -------- | ------- |
| [Contains](http://golang.org/pkg/strings/#Contains) | `String#include?` in Ruby |
| [ContainsAny](http://golang.org/pkg/strings/#ContainsAny) | - |
| [ContainsRune](http://golang.org/pkg/strings/#ContainsRune) | - |
| [Count](http://golang.org/pkg/strings/#Count) | `str.count` in Python; `substr_count` in PHP |
| [EqualFold](http://golang.org/pkg/strings/#EqualFold) | `stricmp` in PHP; `String#casecmp` in Ruby |
| [Fields](http://golang.org/pkg/strings/#Fields) | `str.split` in Python; `split` in Perl; `String#split` in Ruby |
| [FieldsFunc](http://golang.org/pkg/strings/#FieldsFunc) | - |
| [HasPrefix](http://golang.org/pkg/strings/#HasPrefix) | `str.startswith` in Python; `String#start_with?` in Ruby |
| [HasSuffix](http://golang.org/pkg/strings/#HasSuffix) | `str.endswith` in Python; `String#end_with?` in Ruby |
| [Index](http://golang.org/pkg/strings/#Index) | `str.index` in Python; `String#index` in Ruby; `strpos` in PHP; `index` in Perl |
| [IndexAny](http://golang.org/pkg/strings/#IndexAny) | - |
| [IndexByte](http://golang.org/pkg/strings/#IndexByte) | - |
| [IndexFunc](http://golang.org/pkg/strings/#IndexFunc) | - |
| [IndexRune](http://golang.org/pkg/strings/#IndexRune) | - |
| [Join](http://golang.org/pkg/strings/#Join) | `str.join` in Python; `Array#join` in Ruby; `implode` in PHP; `join` in Perl |
| [LastIndex](http://golang.org/pkg/strings/#LastIndex) | `str.rindex` in Python; `String#rindex`; `strrpos` in PHP; `rindex` in Perl |
| [LastIndexAny](http://golang.org/pkg/strings/#LastIndexAny) | - |
| [LastIndexFunc](http://golang.org/pkg/strings/#LastIndexFunc) | - |
| [Map](http://golang.org/pkg/strings/#Map) | `String#each_codepoint` in Ruby |
| [Repeat](http://golang.org/pkg/strings/#Repeat) | operator `*` in Python and Ruby; `str_repeat` in PHP |
| [Replace](http://golang.org/pkg/strings/#Replace) | `str.replace` in Python; `String#sub` in Ruby; `str_replace` in PHP |
| [Split](http://golang.org/pkg/strings/#Split) | `str.split` in Python; `String#split` in Ruby; `explode` in PHP; `split` in Perl |
| [SplitAfter](http://golang.org/pkg/strings/#SplitAfter) | - |
| [SplitAfterN](http://golang.org/pkg/strings/#SplitAfterN) | - |
| [SplitN](http://golang.org/pkg/strings/#SplitN) | `str.split` in Python; `String#split` in Ruby; `explode` in PHP; `split` in Perl |
| [Title](http://golang.org/pkg/strings/#Title) | `str.title` in Python |
| [ToLower](http://golang.org/pkg/strings/#ToLower) | `str.lower` in Python; `String#downcase` in Ruby; `strtolower` in PHP; `lc` in Perl |
| [ToLowerSpecial](http://golang.org/pkg/strings/#ToLowerSpecial) | - |
| [ToTitle](http://golang.org/pkg/strings/#ToTitle) | - |
| [ToTitleSpecial](http://golang.org/pkg/strings/#ToTitleSpecial) | - |
| [ToUpper](http://golang.org/pkg/strings/#ToUpper) | `str.upper` in Python; `String#upcase` in Ruby; `strtoupper` in PHP; `uc` in Perl |
| [ToUpperSpecial](http://golang.org/pkg/strings/#ToUpperSpecial) | - |
| [Trim](http://golang.org/pkg/strings/#Trim) | `str.strip` in Python; `String#strip` in Ruby; `trim` in PHP |
| [TrimFunc](http://golang.org/pkg/strings/#TrimFunc) | - |
| [TrimLeft](http://golang.org/pkg/strings/#TrimLeft) | `str.lstrip` in Python; `String#lstrip` in Ruby; `ltrim` in PHP |
| [TrimLeftFunc](http://golang.org/pkg/strings/#TrimLeftFunc) | - |
| [TrimPrefix](http://golang.org/pkg/strings/#TrimPrefix) | - |
| [TrimRight](http://golang.org/pkg/strings/#TrimRight) | `str.rstrip` in Python; `String#rstrip` in Ruby; `rtrim` in PHP |
| [TrimRightFunc](http://golang.org/pkg/strings/#TrimRightFunc) | - |
| [TrimSpace](http://golang.org/pkg/strings/#TrimSpace) | `str.strip` in Python; `String#strip` in Ruby; `trim` in PHP |
| [TrimSuffix](http://golang.org/pkg/strings/#TrimSuffix) | `String#chomp` in Ruby; `chomp` in Perl |

## License ##

This library is licensed under MIT license. See LICENSE for details.
PKCS11Key
========

The pkcs11key package implements a crypto.Signer interface for a PKCS#11 private key.

[![Build Status](https://travis-ci.org/letsencrypt/pkcs11key.svg)](https://travis-ci.org/letsencrypt/pkcs11key)

## License summary
Some of this code is Copyright (c) 2014 CloudFlare Inc., some is Copyright (c)
2015 Internet Security Research Group.

The code is licensed under the BSD 2-clause license. See the LICENSE file for more details.
# procfs

This procfs package provides functions to retrieve system, kernel and process
metrics from the pseudo-filesystem proc.

*WARNING*: This package is a work in progress. Its API may still break in
backwards-incompatible ways without warnings. Use it at your own risk.

[![GoDoc](https://godoc.org/github.com/prometheus/procfs?status.png)](https://godoc.org/github.com/prometheus/procfs)
[![Build Status](https://travis-ci.org/prometheus/procfs.svg?branch=master)](https://travis-ci.org/prometheus/procfs)
[![Go Report Card](https://goreportcard.com/badge/github.com/prometheus/procfs)](https://goreportcard.com/report/github.com/prometheus/procfs)
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
# certstore [![GoDoc](https://godoc.org/github.com/mastahyeti/certstore?status.svg)](http://godoc.org/github.com/mastahyeti/certstore) [![Report card](https://goreportcard.com/badge/github.com/mastahyeti/certstore)](https://goreportcard.com/report/github.com/mastahyeti/certstore) [![OSX Build Status](https://travis-ci.org/mastahyeti/certstore.svg?branch=master)](https://travis-ci.org/mastahyeti/certstore) [![Windows Build status](https://ci.appveyor.com/api/projects/status/github/mastahyeti/certstore?branch=master&svg=true)](https://ci.appveyor.com/project/mastahyeti/certstore/branch/master)


Certstore is a Go library for accessing user identities stored in platform certificate stores. On Windows and macOS, certstore can enumerate user identities and sign messages with their private keys.

## Example

```go
package main

import (
	"crypto"
	"encoding/hex"
	"errors"
	"fmt"

	"crypto/rand"
	"crypto/sha256"

	"github.com/mastahyeti/certstore"
)

func main() {
	sig, err := signWithMyIdentity("Ben Toews", "hello, world!")
	if err != nil {
		panic(err)
	}

	fmt.Println(hex.EncodeToString(sig))
}

func signWithMyIdentity(cn, msg string) ([]byte, error) {
	// Open the certificate store for use. This must be Close()'ed once you're
	// finished with the store and any identities it contains.
	store, err := certstore.Open()
	if err != nil {
		return nil, err
	}
	defer store.Close()

	// Get an Identity slice, containing every identity in the store. Each of
	// these must be Close()'ed when you're done with them.
	idents, err := store.Identities()
	if err != nil {
		return nil, err
	}

	// Iterate through the identities, looking for the one we want.
	var me certstore.Identity
	for _, ident := range idents {
		defer ident.Close()

		crt, errr := ident.Certificate()
		if errr != nil {
			return nil, errr
		}

		if crt.Subject.CommonName == "Ben Toews" {
			me = ident
		}
	}

	if me == nil {
		return nil, errors.New("Couldn't find my identity")
	}

	// Get a crypto.Signer for the identity.
	signer, err := me.Signer()
	if err != nil {
		return nil, err
	}

	// Digest and sign our message.
	digest := sha256.Sum256([]byte(msg))
	signature, err := signer.Sign(rand.Reader, digest[:], crypto.SHA256)
	if err != nil {
		return nil, err
	}

	return signature, nil
}

```
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

```go
t := metrics.GetOrRegisterTimer("account.create.latency", nil)
t.Time(func() {})
t.Update(47)
```

**NOTE:** Be sure to unregister short-lived meters and timers otherwise they will
leak memory:

```go
// Will call Stop() on the Meter to allow for garbage collection
metrics.Unregister("quux")
// Or similarly for a Timer that embeds a Meter
metrics.Unregister("bang")
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

go influxdb.InfluxDB(metrics.DefaultRegistry,
  10e9, 
  "127.0.0.1:8086", 
  "database-name", 
  "username", 
  "password"
)
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

* Librato - https://github.com/mihasya/go-metrics-librato
* Graphite - https://github.com/cyberdelia/go-metrics-graphite
* InfluxDB - https://github.com/vrischmann/go-metrics-influxdb
* Ganglia - https://github.com/appscode/metlia
* Prometheus - https://github.com/deathowl/go-metrics-prometheus
* DataDog - https://github.com/syntaqx/go-metrics-datadog
* SignalFX - https://github.com/pascallouisperez/go-metrics-signalfx
* Honeycomb - https://github.com/getspine/go-metrics-honeycomb
* Wavefront - https://github.com/wavefrontHQ/go-metrics-wavefront
go-syslog
=========

This repository provides a very simple `gsyslog` package. The point of this
package is to allow safe importing of syslog without introducing cross-compilation
issues. The stdlib `log/syslog` cannot be imported on Windows systems, and without
conditional compilation this adds complications.

Instead, `gsyslog` provides a very simple wrapper around `log/syslog` but returns
a runtime error if attempting to initialize on a non Linux or OSX system.

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

Test keys
=========

The certificates and keys contained in this directory have been generated for
test/development purposes only. Do not use these files in production
deployments! You can regenerate them anytime by running `make all`.
