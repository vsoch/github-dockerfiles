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
Keyring
=======
[![Build Status](https://travis-ci.org/99designs/keyring.svg?branch=master)](https://travis-ci.org/99designs/keyring)
[![Documentation](https://godoc.org/github.com/99designs/keyring?status.svg)](https://godoc.org/github.com/99designs/keyring)

Keyring provides utility functions for and a common interface to a range of secure credential storage services. Originally developed as part of [AWS Vault](https://github.com/99designs/aws-vault), a command line tool for securely managing AWS access from developer workstations.

Currently Keyring supports the following backends
  * macOS/OSX Keychain
  * Windows credential store
  * [Pass](https://www.passwordstore.org/)
  * [Secret Service](https://github.com/99designs/aws-vault/pull/98)
  * [KDE Wallet](https://github.com/99designs/aws-vault/pull/27)
  * [Encrypted File](https://github.com/99designs/aws-vault/pull/63)

## Installing

`go get github.com/99designs/keyring`

## Usage

The short version of how to use keyring is shown below.

```go
ring, _ := keyring.Open(keyring.Config{
  ServiceName: "example",
})

_ = ring.Set(keyring.Item{
	Key: "foo",
	Data: []byte("secret-bar"),
})

i, _ := ring.Get("foo")

fmt.Printf("%s", i.Data)
```

For more detail on the API please check [the keyring godocs](https://godoc.org/github.com/99designs/keyring)

## Development & Contributing

Contributions to the keyring package are most welcome from engineers of all backgrounds and skill levels. In particular the addition of extra backends across popular operating systems would be appreciated.

This project will adhere to the [Go Community Code of Conduct](https://golang.org/conduct) in the github provided discussion spaces, with the moderators being the 99designs engineering team.

To make a contribution:

  * Fork the repository
  * Make your changes on the fork
  * Submit a pull request back to this repo with a clear description of the problem you're solving
  * Ensure your PR passes all current (and new) tests
  * Ideally verify that [aws-vault](https://github.com/99designs/aws-vault) works with your changes (optional)

...and we'll do our best to get your work merged in
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

Please note that the API is considered unstable for now and may change without
further notice.

### License

go.dbus is available under the Simplified BSD License; see LICENSE for the full
text.

Nearly all of the credit for this library goes to github.com/guelfey/go.dbus.
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

The minimum requirement of Go is **1.6**.

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
wincred
=======

Go wrapper around the Windows Credential Manager API functions.

[![Build status](https://ci.appveyor.com/api/projects/status/eclecjwniu2n4u3w/branch/master?svg=true)](https://ci.appveyor.com/project/danieljoos/wincred/branch/master)
[![GoDoc](https://godoc.org/github.com/danieljoos/wincred?status.svg)](https://godoc.org/github.com/danieljoos/wincred)


Installation
------------

```Go
go get github.com/danieljoos/wincred
```


Usage
-----

See the following examples:

### Create and store a new generic credential object
```Go
package main

import (
    "fmt"
    "github.com/danieljoos/wincred"
)

func main() {
    cred := wincred.NewGenericCredential("myGoApplication")
    cred.CredentialBlob = []byte("my secret")
    err := cred.Write()
    
    if err != nil {
        fmt.Println(err)
    }
} 
```

### Retrieve a credential object
```Go
package main

import (
    "fmt"
    "github.com/danieljoos/wincred"
)

func main() {
    cred, err := wincred.GetGenericCredential("myGoApplication")
    if err == nil {
        fmt.Println(string(cred.CredentialBlob))
    }
} 
```

### Remove a credential object
```Go
package main

import (
    "fmt"
    "github.com/danieljoos/wincred"
)

func main() {
    cred, err := wincred.GetGenericCredential("myGoApplication")
    if err != nil {
        fmt.Println(err)
        return
    }
    cred.Delete()
} 
```

### List all available credentials
```Go
package main

import (
    "fmt"
    "github.com/danieljoos/wincred"
)

func main() {
    creds, err := wincred.List()
    if err != nil {
        fmt.Println(err)
        return
    }
    for i := range(creds) {
        fmt.Println(creds[i].TargetName)
    }
}
```
# Go Keychain

A library for accessing the Keychain for macOS and iOS in Go (golang).

Requires macOS 10.9 or greater and iOS 8 or greater.

```go
import "github.com/keybase/go-keychain"
```


## Usage

The API is meant to mirror the macOS/iOS Keychain API and is not necessarily idiomatic go.

#### Add Item

```go
item := keychain.NewItem()
item.SetSecClass(keychain.SecClassGenericPassword)
item.SetService("MyService")
item.SetAccount("gabriel")
item.SetLabel("A label")
item.SetAccessGroup("A123456789.group.com.mycorp")
item.SetData([]byte("toomanysecrets"))
item.SetSynchronizable(keychain.SynchronizableNo)
item.SetAccessible(keychain.AccessibleWhenUnlocked)
err := keychain.AddItem(item)

if err == keychain.ErrorDuplicateItem {
  // Duplicate
}
```

#### Query Item

Query for multiple results, returning attributes:

```go
query := keychain.NewItem()
query.SetSecClass(keychain.SecClassGenericPassword)
query.SetService(service)
query.SetAccount(account)
query.SetAccessGroup(accessGroup)
query.SetMatchLimit(keychain.MatchLimitAll)
query.SetReturnAttributes(true)
results, err := keychain.QueryItem(query)
if err != nil {
  // Error
} else {
  for _, r := range results {
    fmt.Printf("%#v\n", r)
  }
}
```

Query for a single result, returning data:

```go
query := keychain.NewItem()
query.SetSecClass(keychain.SecClassGenericPassword)
query.SetService(service)
query.SetAccount(account)
query.SetAccessGroup(accessGroup)
query.SetMatchLimit(keychain.MatchLimitOne)
query.SetReturnData(true)
results, err := keychain.QueryItem(query)
if err != nil {
  // Error
} else if len(results) != 1 {
  // Not found
} else {
  password := string(results[0].Data)
}
```

#### Delete Item

Delete a generic password item with service and account:

```go
item := keychain.NewItem()
item.SetSecClass(keychain.SecClassGenericPassword)
item.SetService(service)
item.SetAccount(account)
err := keychain.DeleteItem(item)
```

### Other

There are some convenience methods for generic password:

```go
// Create generic password item with service, account, label, password, access group
item := keychain.NewGenericPassword("MyService", "gabriel", "A label", []byte("toomanysecrets"), "A123456789.group.com.mycorp")
item.SetSynchronizable(keychain.SynchronizableNo)
item.SetAccessible(keychain.AccessibleWhenUnlocked)
err := keychain.AddItem(item)
if err == keychain.ErrorDuplicateItem {
  // Duplicate
}

accounts, err := keychain.GetGenericPasswordAccounts("MyService")
// Should have 1 account == "gabriel"

err := keychain.DeleteGenericPasswordItem("MyService", "gabriel")
if err == keychain.ErrorNotFound {
  // Not found
}
```

### OS X

Creating a new keychain and add an item to it:

```go

// Add a new key chain into ~/Application Support/Keychains, with the provided password
k, err := keychain.NewKeychain("mykeychain.keychain", "my keychain password")
if err != nil {
  // Error creating
}

// Create generic password item with service, account, label, password, access group
item := keychain.NewGenericPassword("MyService", "gabriel", "A label", []byte("toomanysecrets"), "A123456789.group.com.mycorp")
item.UseKeychain(k)
err := keychain.AddItem(item)
if err != nil {
  // Error creating
}
```

Using a Keychain at path:

```go
k, err := keychain.NewWithPath("mykeychain.keychain")
```

Set a trusted applications for item (OS X only):

```go
item := keychain.NewGenericPassword("MyService", "gabriel", "A label", []byte("toomanysecrets"), "A123456789.group.com.mycorp")
trustedApplications := []string{"/Applications/Mail.app"}
item.SetAccess(&keychain.Access{Label: "Mail", TrustedApplications: trustedApplications})
err := keychain.AddItem(item)
```

## iOS

Bindable package in `bind`. iOS project in `ios`. Run that project to test iOS.

To re-generate framework:

```
(cd bind && gomobile bind -target=ios -tags=ios -o ../ios/bind.framework)
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

This packages requires Go 1.7. If you installed it and set up your GOPATH, just run:

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
# Golang (GO) Javascript Object Signing and Encryption (JOSE) and JSON Web Token (JWT) implementation

[![GoDoc](https://godoc.org/github.com/dvsekhvalnov/jose2go?status.svg)](http://godoc.org/github.com/dvsekhvalnov/jose2go)

Pure Golang (GO) library for generating, decoding and encrypting [JSON Web Tokens](https://tools.ietf.org/html/rfc7519). Zero dependency, relies only
on standard library.

Supports full suite of signing, encryption and compression algorithms defined by [JSON Web Algorithms](https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-31) as of July 4, 2014 version.

Extensively unit tested and cross tested (100+ tests) for compatibility with [jose.4.j](https://bitbucket.org/b_c/jose4j/wiki/Home), [Nimbus-JOSE-JWT](https://bitbucket.org/nimbusds/nimbus-jose-jwt/wiki/Home), [json-jwt](https://github.com/nov/json-jwt) and
[jose-jwt](https://github.com/dvsekhvalnov/jose-jwt) libraries.


## Status
Used in production. GA ready. Current version is 1.3.

## Important
v1.3 fixed potential Invalid Curve Attack on NIST curves within ECDH key management.
Upgrade strongly recommended.

v1.2 breaks `jose.Decode` interface by returning 3 values instead of 2.

v1.2 deprecates `jose.Compress` method in favor of using configuration options to `jose.Encrypt`,
the method will be removed in next release.

### Migration to v1.2
Pre v1.2 decoding:

```Go
payload,err := jose.Decode(token,sharedKey)
```

Should be updated to v1.2:

```Go
payload, headers, err := jose.Decode(token,sharedKey)
```

Pre v1.2 compression:

```Go
token,err := jose.Compress(payload,jose.DIR,jose.A128GCM,jose.DEF, key)
```

Should be update to v1.2:

```Go
token, err := jose.Encrypt(payload, jose.DIR, jose.A128GCM, key, jose.Zip(jose.DEF))
```

## Supported JWA algorithms

**Signing**
- HMAC signatures with HS256, HS384 and HS512.
- RSASSA-PKCS1-V1_5 signatures with RS256, RS384 and RS512.
- RSASSA-PSS signatures (probabilistic signature scheme with appendix) with PS256, PS384 and PS512.
- ECDSA signatures with ES256, ES384 and ES512.
- NONE (unprotected) plain text algorithm without integrity protection

**Encryption**
- RSAES OAEP (using SHA-1 and MGF1 with SHA-1) encryption with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- RSAES OAEP 256 (using SHA-256 and MGF1 with SHA-256) encryption with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- RSAES-PKCS1-V1_5 encryption with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- A128KW, A192KW, A256KW encryption with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- A128GCMKW, A192GCMKW, A256GCMKW encryption with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- ECDH-ES with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- ECDH-ES+A128KW, ECDH-ES+A192KW, ECDH-ES+A256KW with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- PBES2-HS256+A128KW, PBES2-HS384+A192KW, PBES2-HS512+A256KW with A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM, A256GCM
- Direct symmetric key encryption with pre-shared key A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128GCM, A192GCM and A256GCM

**Compression**
- DEFLATE compression

## Installation
### Grab package from github
`go get github.com/dvsekhvalnov/jose2go` or `go get -u github.com/dvsekhvalnov/jose2go` to update to latest version

### Import package
```Go
import (
	"github.com/dvsekhvalnov/jose2go"
)
```

## Usage
#### Creating Plaintext (unprotected) Tokens

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	token,err := jose.Sign(payload,jose.NONE, nil)

	if(err==nil) {
		//go use token
		fmt.Printf("\nPlaintext = %v\n",token)
	}
}
```

### Creating signed tokens
#### HS-256, HS-384 and HS-512
Signing with HS256, HS384, HS512 expecting `[]byte` array key of corresponding length:

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	key := []byte{97,48,97,50,97,98,100,56,45,54,49,54,50,45,52,49,99,51,45,56,51,100,54,45,49,99,102,53,53,57,98,52,54,97,102,99}

	token,err := jose.Sign(payload,jose.HS256,key)

	if(err==nil) {
		//go use token
		fmt.Printf("\nHS256 = %v\n",token)
	}
}
```

#### RS-256, RS-384 and RS-512, PS-256, PS-384 and PS-512
Signing with RS256, RS384, RS512, PS256, PS384, PS512 expecting `*rsa.PrivateKey` private key of corresponding length. **jose2go** [provides convenient utils](#dealing-with-keys) to construct `*rsa.PrivateKey` instance from PEM encoded PKCS1 or PKCS8 data: `Rsa.ReadPrivate([]byte)` under `jose2go/keys/rsa` package.

```Go
package main

import (
	"fmt"
	"io/ioutil"
	Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	keyBytes,err := ioutil.ReadFile("private.key")

	if(err!=nil) {
		panic("invalid key file")
	}

	privateKey,e:=Rsa.ReadPrivate(keyBytes)

	if(e!=nil) {
		panic("invalid key format")
	}

	token,err := jose.Sign(payload,jose.RS256, privateKey)

	if(err==nil) {
		//go use token
		fmt.Printf("\nRS256 = %v\n",token)
	}
}
```

#### ES-256, ES-384 and ES-512
ES256, ES384, ES512 ECDSA signatures expecting `*ecdsa.PrivateKey` private elliptic curve key of corresponding length.  **jose2go** [provides convenient utils](#dealing-with-keys) to construct `*ecdsa.PrivateKey` instance from PEM encoded PKCS1 or PKCS8 data: `ecc.ReadPrivate([]byte)` or directly from `X,Y,D` parameters: `ecc.NewPrivate(x,y,d []byte)` under `jose2go/keys/ecc` package.

```Go
package main

import (
    "fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    payload := `{"hello":"world"}`

	privateKey:=ecc.NewPrivate([]byte{4, 114, 29, 223, 58, 3, 191, 170, 67, 128, 229, 33, 242, 178, 157, 150, 133, 25, 209, 139, 166, 69, 55, 26, 84, 48, 169, 165, 67, 232, 98, 9},
	 			 			   []byte{131, 116, 8, 14, 22, 150, 18, 75, 24, 181, 159, 78, 90, 51, 71, 159, 214, 186, 250, 47, 207, 246, 142, 127, 54, 183, 72, 72, 253, 21, 88, 53},
							   []byte{ 42, 148, 231, 48, 225, 196, 166, 201, 23, 190, 229, 199, 20, 39, 226, 70, 209, 148, 29, 70, 125, 14, 174, 66, 9, 198, 80, 251, 95, 107, 98, 206 })

    token,err := jose.Sign(payload, jose.ES256, privateKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\ntoken = %v\n",token)
    }
}
```

### Creating encrypted tokens
#### RSA-OAEP-256, RSA-OAEP and RSA1\_5 key management algorithm
RSA-OAEP-256, RSA-OAEP and RSA1_5 key management expecting `*rsa.PublicKey` public key of corresponding length.

```Go
package main

import (
    "fmt"
    "io/ioutil"
    Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	keyBytes,err := ioutil.ReadFile("public.key")

	if(err!=nil) {
		panic("invalid key file")
	}

	publicKey,e:=Rsa.ReadPublic(keyBytes)

	if(e!=nil) {
		panic("invalid key format")
	}

	//OR:
	//token,err := jose.Encrypt(payload, jose.RSA1_5, jose.A256GCM, publicKey)
	token,err := jose.Encrypt(payload, jose.RSA_OAEP, jose.A256GCM, publicKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\ntoken = %v\n",token)
    }
}  
```

#### AES Key Wrap key management family of algorithms
AES128KW, AES192KW and AES256KW key management requires `[]byte` array key of corresponding length

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	sharedKey :=[]byte{194,164,235,6,138,248,171,239,24,216,11,22,137,199,215,133}

	token,err := jose.Encrypt(payload,jose.A128KW,jose.A128GCM,sharedKey)

	if(err==nil) {
		//go use token
		fmt.Printf("\nA128KW A128GCM = %v\n",token)
	}
}
```

#### AES GCM Key Wrap key management family of algorithms
AES128GCMKW, AES192GCMKW and AES256GCMKW key management requires `[]byte` array key of corresponding length

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	sharedKey :=[]byte{194,164,235,6,138,248,171,239,24,216,11,22,137,199,215,133}

	token,err := jose.Encrypt(payload,jose.A128GCMKW,jose.A128GCM,sharedKey)

	if(err==nil) {
		//go use token
		fmt.Printf("\nA128GCMKW A128GCM = %v\n",token)
	}
}
```

#### ECDH-ES and ECDH-ES with AES Key Wrap key management family of algorithms
ECDH-ES and ECDH-ES+A128KW, ECDH-ES+A192KW, ECDH-ES+A256KW key management requires `*ecdsa.PublicKey` elliptic curve key of corresponding length. **jose2go** [provides convenient utils](#dealing-with-keys) to construct `*ecdsa.PublicKey` instance from PEM encoded PKCS1 X509 certificate or PKIX data: `ecc.ReadPublic([]byte)` or directly from `X,Y` parameters: `ecc.NewPublic(x,y []byte)`under `jose2go/keys/ecc` package:

```Go
package main

import (
    "fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    payload := `{"hello":"world"}`

    publicKey:=ecc.NewPublic([]byte{4, 114, 29, 223, 58, 3, 191, 170, 67, 128, 229, 33, 242, 178, 157, 150, 133, 25, 209, 139, 166, 69, 55, 26, 84, 48, 169, 165, 67, 232, 98, 9},
                             []byte{131, 116, 8, 14, 22, 150, 18, 75, 24, 181, 159, 78, 90, 51, 71, 159, 214, 186, 250, 47, 207, 246, 142, 127, 54, 183, 72, 72, 253, 21, 88, 53})

    token,err := jose.Encrypt(payload, jose.ECDH_ES, jose.A128CBC_HS256, publicKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\ntoken = %v\n",token)
    }
}  
```

#### PBES2 using HMAC SHA with AES Key Wrap key management family of algorithms
PBES2-HS256+A128KW, PBES2-HS384+A192KW, PBES2-HS512+A256KW key management requires `string` passphrase from which actual key will be derived

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	passphrase := `top secret`

	token,err := jose.Encrypt(payload,jose.PBES2_HS256_A128KW,jose.A256GCM,passphrase)

	if(err==nil) {
		//go use token
		fmt.Printf("\nPBES2_HS256_A128KW A256GCM = %v\n",token)
	}
}
```

#### DIR direct pre-shared symmetric key management
Direct key management with pre-shared symmetric keys expecting `[]byte` array key of corresponding length:

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload :=  `{"hello": "world"}`

	sharedKey :=[]byte{194,164,235,6,138,248,171,239,24,216,11,22,137,199,215,133}

	token,err := jose.Encrypt(payload,jose.DIR,jose.A128GCM,sharedKey)

	if(err==nil) {
		//go use token
		fmt.Printf("\nDIR A128GCM = %v\n",token)
	}
}
```

### Creating compressed & encrypted tokens
#### DEFLATE compression
**jose2go** supports optional DEFLATE compression of payload before encrypting, can be used with all supported encryption and key management algorithms:

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	payload := `{"hello": "world"}`

	sharedKey := []byte{194, 164, 235, 6, 138, 248, 171, 239, 24, 216, 11, 22, 137, 199, 215, 133}

	token, err := jose.Encrypt(payload, jose.DIR, jose.A128GCM, sharedKey, jose.Zip(jose.DEF))

	if err == nil {
		//go use token
		fmt.Printf("\nDIR A128GCM DEFLATED= %v\n", token)
	}
}
```

### Verifying, Decoding and Decompressing tokens
Decoding json web tokens is fully symmetric to creating signed or encrypted tokens (with respect to public/private cryptography), decompressing deflated payloads is handled automatically:

As of v1.2 decode method defined as `jose.Decode() payload string, headers map[string]interface{}, err error` and returns both payload as unprocessed string and headers as map.

**HS256, HS384, HS512** signatures, **A128KW, A192KW, A256KW**,**A128GCMKW, A192GCMKW, A256GCMKW** and **DIR** key management algorithm expecting `[]byte` array key:

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	token := "eyJhbGciOiJIUzI1NiIsImN0eSI6InRleHRcL3BsYWluIn0.eyJoZWxsbyI6ICJ3b3JsZCJ9.chIoYWrQMA8XL5nFz6oLDJyvgHk2KA4BrFGrKymjC8E"

	sharedKey :=[]byte{97,48,97,50,97,98,100,56,45,54,49,54,50,45,52,49,99,51,45,56,51,100,54,45,49,99,102,53,53,57,98,52,54,97,102,99}

	payload, headers, err := jose.Decode(token,sharedKey)

	if(err==nil) {
		//go use token
		fmt.Printf("\npayload = %v\n",payload)

        //and/or use headers
        fmt.Printf("\nheaders = %v\n",headers)
	}
}
```

**RS256, RS384, RS512**,**PS256, PS384, PS512** signatures expecting `*rsa.PublicKey` public key of corresponding length. **jose2go** [provides convenient utils](#dealing-with-keys) to construct `*rsa.PublicKey` instance from PEM encoded PKCS1 X509 certificate or PKIX data: `Rsa.ReadPublic([]byte)` under `jose2go/keys/rsa` package:

```Go
package main

import (
    "fmt"
    "io/ioutil"
    Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    token := "eyJhbGciOiJSUzI1NiIsImN0eSI6InRleHRcL3BsYWluIn0.eyJoZWxsbyI6ICJ3b3JsZCJ9.NL_dfVpZkhNn4bZpCyMq5TmnXbT4yiyecuB6Kax_lV8Yq2dG8wLfea-T4UKnrjLOwxlbwLwuKzffWcnWv3LVAWfeBxhGTa0c4_0TX_wzLnsgLuU6s9M2GBkAIuSMHY6UTFumJlEeRBeiqZNrlqvmAzQ9ppJHfWWkW4stcgLCLMAZbTqvRSppC1SMxnvPXnZSWn_Fk_q3oGKWw6Nf0-j-aOhK0S0Lcr0PV69ZE4xBYM9PUS1MpMe2zF5J3Tqlc1VBcJ94fjDj1F7y8twmMT3H1PI9RozO-21R0SiXZ_a93fxhE_l_dj5drgOek7jUN9uBDjkXUwJPAyp9YPehrjyLdw"

    keyBytes, err := ioutil.ReadFile("public.key")

    if(err!=nil) {
        panic("invalid key file")
    }

    publicKey, e:=Rsa.ReadPublic(keyBytes)

    if(e!=nil) {
        panic("invalid key format")
    }

    payload, headers, err := jose.Decode(token, publicKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\npayload = %v\n",payload)

        //and/or use headers
        fmt.Printf("\nheaders = %v\n",headers)
    }
}  
```

**RSA-OAEP-256**, **RSA-OAEP** and **RSA1_5** key management algorithms expecting `*rsa.PrivateKey` private key of corresponding length:

```Go
package main

import (
    "fmt"
    "io/ioutil"
    Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    token := "eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMjU2R0NNIn0.ixD3WVOkvaxeLKi0kyVqTzM6W2EW25SHHYCAr9473Xq528xSK0AVux6kUtv7QMkQKgkMvO8X4VdvonyGkDZTK2jgYUiI06dz7I1sjWJIbyNVrANbBsmBiwikwB-9DLEaKuM85Lwu6gnzbOF6B9R0428ckxmITCPDrzMaXwYZHh46FiSg9djChUTex0pHGhNDiEIgaINpsmqsOFX1L2Y7KM2ZR7wtpR3kidMV3JlxHdKheiPKnDx_eNcdoE-eogPbRGFdkhEE8Dyass1ZSxt4fP27NwsIer5pc0b922_3XWdi1r1TL_fLvGktHLvt6HK6IruXFHpU4x5Z2gTXWxEIog.zzTNmovBowdX2_hi.QSPSgXn0w25ugvzmu2TnhePn.0I3B9BE064HFNP2E0I7M9g"

    keyBytes, err := ioutil.ReadFile("private.key")

    if(err!=nil) {
        panic("invalid key file")
    }

    privateKey, e:=Rsa.ReadPrivate(keyBytes)

    if(e!=nil) {
        panic("invalid key format")
    }

    payload, headers, err := jose.Decode(token, privateKey)

    if(err==nil) {
        //go use payload
        fmt.Printf("\npayload = %v\n",payload)

        //and/or use headers
        fmt.Printf("\nheaders = %v\n",headers)
    }
}  
```

**PBES2-HS256+A128KW, PBES2-HS384+A192KW, PBES2-HS512+A256KW** key management algorithms expects `string` passpharase as a key

```Go
package main

import (
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	token :=  `eyJhbGciOiJQQkVTMi1IUzI1NitBMTI4S1ciLCJlbmMiOiJBMjU2R0NNIiwicDJjIjo4MTkyLCJwMnMiOiJlZWpFZTF0YmJVbU5XV2s2In0.J2HTgltxH3p7A2zDgQWpZPgA2CHTSnDmMhlZWeSOMoZ0YvhphCeg-w.FzYG5AOptknu7jsG.L8jAxfxZhDNIqb0T96YWoznQ.yNeOfQWUbm8KuDGZ_5lL_g`

	passphrase := `top secret`

	payload, headers, err := jose.Decode(token,passphrase)

	if(err==nil) {
		//go use token
		fmt.Printf("\npayload = %v\n",payload)

        //and/or use headers
        fmt.Printf("\nheaders = %v\n",headers)
	}
}
```

**ES256, ES284, ES512** signatures expecting `*ecdsa.PublicKey` public elliptic curve key of corresponding length. **jose2go** [provides convenient utils](#dealing-with-keys) to construct `*ecdsa.PublicKey` instance from PEM encoded PKCS1 X509 certificate or PKIX data: `ecc.ReadPublic([]byte)` or directly from `X,Y` parameters: `ecc.NewPublic(x,y []byte)`under `jose2go/keys/ecc` package:

```Go
package main

import (
    "fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    token := "eyJhbGciOiJFUzI1NiIsImN0eSI6InRleHRcL3BsYWluIn0.eyJoZWxsbyI6ICJ3b3JsZCJ9.EVnmDMlz-oi05AQzts-R3aqWvaBlwVZddWkmaaHyMx5Phb2NSLgyI0kccpgjjAyo1S5KCB3LIMPfmxCX_obMKA"

	publicKey:=ecc.NewPublic([]byte{4, 114, 29, 223, 58, 3, 191, 170, 67, 128, 229, 33, 242, 178, 157, 150, 133, 25, 209, 139, 166, 69, 55, 26, 84, 48, 169, 165, 67, 232, 98, 9},
	 			 			 []byte{131, 116, 8, 14, 22, 150, 18, 75, 24, 181, 159, 78, 90, 51, 71, 159, 214, 186, 250, 47, 207, 246, 142, 127, 54, 183, 72, 72, 253, 21, 88, 53})

    payload, headers, err := jose.Decode(token, publicKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\npayload = %v\n",payload)

        //and/or use headers
        fmt.Printf("\nheaders = %v\n",headers)
    }
}
```

**ECDH-ES** and **ECDH-ES+A128KW**, **ECDH-ES+A192KW**, **ECDH-ES+A256KW** key management expecting `*ecdsa.PrivateKey` private elliptic curve key of corresponding length.  **jose2go** [provides convenient utils](#dealing-with-keys) to construct `*ecdsa.PrivateKey` instance from PEM encoded PKCS1 or PKCS8 data: `ecc.ReadPrivate([]byte)` or directly from `X,Y,D` parameters: `ecc.NewPrivate(x,y,d []byte)` under `jose2go/keys/ecc` package:

```Go
package main

import (
    "fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    token := "eyJhbGciOiJFQ0RILUVTIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImVwayI6eyJrdHkiOiJFQyIsIngiOiItVk1LTG5NeW9IVHRGUlpGNnFXNndkRm5BN21KQkdiNzk4V3FVMFV3QVhZIiwieSI6ImhQQWNReTgzVS01Qjl1U21xbnNXcFZzbHVoZGJSZE1nbnZ0cGdmNVhXTjgiLCJjcnYiOiJQLTI1NiJ9fQ..UA3N2j-TbYKKD361AxlXUA.XxFur_nY1GauVp5W_KO2DEHfof5s7kUwvOgghiNNNmnB4Vxj5j8VRS8vMOb51nYy2wqmBb2gBf1IHDcKZdACkCOMqMIcpBvhyqbuKiZPLHiilwSgVV6ubIV88X0vK0C8ZPe5lEyRudbgFjdlTnf8TmsvuAsdtPn9dXwDjUR23bD2ocp8UGAV0lKqKzpAw528vTfD0gwMG8gt_op8yZAxqqLLljMuZdTnjofAfsW2Rq3Z6GyLUlxR51DAUlQKi6UpsKMJoXTrm1Jw8sXBHpsRqA.UHCYOtnqk4SfhAknCnymaQ"

	privateKey:=ecc.NewPrivate([]byte{4, 114, 29, 223, 58, 3, 191, 170, 67, 128, 229, 33, 242, 178, 157, 150, 133, 25, 209, 139, 166, 69, 55, 26, 84, 48, 169, 165, 67, 232, 98, 9},
	 			 			   []byte{131, 116, 8, 14, 22, 150, 18, 75, 24, 181, 159, 78, 90, 51, 71, 159, 214, 186, 250, 47, 207, 246, 142, 127, 54, 183, 72, 72, 253, 21, 88, 53},
							   []byte{ 42, 148, 231, 48, 225, 196, 166, 201, 23, 190, 229, 199, 20, 39, 226, 70, 209, 148, 29, 70, 125, 14, 174, 66, 9, 198, 80, 251, 95, 107, 98, 206 })

    payload, headers, err := jose.Decode(token, privateKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\npayload = %v\n",payload)

        //and/or use headers
        fmt.Printf("\nheaders = %v\n",headers)
    }
}
```

### Adding extra headers
It's possible to pass additional headers while encoding token. **jose2go** provides convenience configuration helpers: `Header(name string, value interface{})` and `Headers(headers map[string]interface{})` that can be passed to `Sign(..)` and `Encrypt(..)` calls.

Note: **jose2go** do not allow to override `alg`, `enc` and `zip` headers.

Example of signing with extra headers:
```Go
	token, err := jose.Sign(payload, jose.ES256, key,
                    		jose.Header("keyid", "111-222-333"),
                    		jose.Header("trans-id", "aaa-bbb"))
```

Encryption with extra headers:
```Go
token, err := jose.Encrypt(payload, jose.DIR, jose.A128GCM, sharedKey,
                    jose.Headers(map[string]interface{}{"keyid": "111-22-33", "cty": "text/plain"}))
```

### Two phase validation
In some cases validation (decoding) key can be unknown prior to examining token content. For instance one can use different keys per token issuer or rely on headers information to determine which key to use, do logging or other things.

**jose2go** allows to pass `func(headers map[string]interface{}, payload string) key interface{}` callback instead of key to `jose.Decode(..)`. Callback will be executed prior to decoding and integrity validation and will recieve parsed headers and payload as is (for encrypted tokens it will be cipher text). Callback should return key to be used for actual decoding process or `error` if decoding should be stopped, given error object will be returned from `jose.Decode(..)` call.

Example of decoding token with callback:

```Go
package main

import (
	"crypto/rsa"
	"fmt"
	"github.com/dvsekhvalnov/jose2go"
	"github.com/dvsekhvalnov/jose2go/keys/rsa"
	"io/ioutil"
	"errors"
)

func main() {

	token := "eyJhbGciOiJSUzI1NiIsImN0eSI6InRleHRcL3BsYWluIn0.eyJoZWxsbyI6ICJ3b3JsZCJ9.NL_dfVpZkhNn4bZpCyMq5TmnXbT4yiyecuB6Kax_lV8Yq2dG8wLfea-T4UKnrjLOwxlbwLwuKzffWcnWv3LVAWfeBxhGTa0c4_0TX_wzLnsgLuU6s9M2GBkAIuSMHY6UTFumJlEeRBeiqZNrlqvmAzQ9ppJHfWWkW4stcgLCLMAZbTqvRSppC1SMxnvPXnZSWn_Fk_q3oGKWw6Nf0-j-aOhK0S0Lcr0PV69ZE4xBYM9PUS1MpMe2zF5J3Tqlc1VBcJ94fjDj1F7y8twmMT3H1PI9RozO-21R0SiXZ_a93fxhE_l_dj5drgOek7jUN9uBDjkXUwJPAyp9YPehrjyLdw"

	payload, _, err := jose.Decode(token,
		func(headers map[string]interface{}, payload string) interface{} {
            //log something
			fmt.Printf("\nHeaders before decoding: %v\n", headers)
			fmt.Printf("\nPayload before decoding: %v\n", payload)

            //lookup key based on keyid header as en example
            //or lookup based on something from payload, e.g. 'iss' claim for instance
            key := FindKey(headers['keyid'])

            if(key==nil) {
                return errors.New("Key not found")
            }

            return key;
		})

	if err == nil {
		//go use token
		fmt.Printf("\ndecoded payload = %v\n", payload)
	}
}
```

### Working with binary payload
In addition to work with string payloads (typical use-case) `jose2go` supports
encoding and decoding of raw binary data. `jose.DecodeBytes`, `jose.SignBytes`
and `jose.EncryptBytes` functions provides similar interface but accepting
`[]byte` payloads.

Examples:

```Go
package main

import (
	"github.com/dvsekhvalnov/jose2go"
)

func main() {

	token :=  `eyJhbGciOiJQQkVTMi1IUzI1NitBMTI4S1ciLCJlbmMiOiJBMjU2R0NNIiwicDJjIjo4MTkyLCJwMnMiOiJlZWpFZTF0YmJVbU5XV2s2In0.J2HTgltxH3p7A2zDgQWpZPgA2CHTSnDmMhlZWeSOMoZ0YvhphCeg-w.FzYG5AOptknu7jsG.L8jAxfxZhDNIqb0T96YWoznQ.yNeOfQWUbm8KuDGZ_5lL_g`

	passphrase := `top secret`

	payload, headers, err := jose.DecodeBytes(token,passphrase)

	if(err==nil) {
		//go use token
		//payload = []byte{....}
	}
}
```

```Go
package main

import (
    "fmt"
    "io/ioutil"
    Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    payload :=  []byte {0x01, 0x02, 0x03, 0x04}

    keyBytes,err := ioutil.ReadFile("private.key")

    if(err!=nil) {
        panic("invalid key file")
    }

    privateKey,e:=Rsa.ReadPrivate(keyBytes)

    if(e!=nil) {
        panic("invalid key format")
    }

    token,err := jose.SignBytes(payload,jose.RS256, privateKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\nRS256 = %v\n",token)
    }
}
```

```Go
package main

import (
    "fmt"
    "io/ioutil"
    Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
    "github.com/dvsekhvalnov/jose2go"
)

func main() {

    payload :=  []byte {0x01, 0x02, 0x03, 0x04}

    keyBytes,err := ioutil.ReadFile("public.key")

    if(err!=nil) {
        panic("invalid key file")
    }

    publicKey,e:=Rsa.ReadPublic(keyBytes)

    if(e!=nil) {
        panic("invalid key format")
    }

    token,err := jose.EncryptBytes(payload, jose.RSA_OAEP, jose.A256GCM, publicKey)

    if(err==nil) {
        //go use token
        fmt.Printf("\ntoken = %v\n",token)
    }
}  
```
### Dealing with keys
**jose2go** provides several helper methods to simplify loading & importing of elliptic and rsa keys. Import `jose2go/keys/rsa` or `jose2go/keys/ecc` respectively:

#### RSA keys
1. `Rsa.ReadPrivate(raw []byte) (key *rsa.PrivateKey,err error)` attempts to parse RSA private key from PKCS1 or PKCS8 format (`BEGIN RSA PRIVATE KEY` and `BEGIN PRIVATE KEY` headers)

```Go
package main

import (
	"fmt"
	Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
	"io/ioutil"
)

func main() {

    keyBytes, _ := ioutil.ReadFile("private.key")

    privateKey, err:=Rsa.ReadPrivate(keyBytes)

    if(err!=nil) {
        panic("invalid key format")
    }

	fmt.Printf("privateKey = %v\n",privateKey)
}
```

2. `Rsa.ReadPublic(raw []byte) (key *rsa.PublicKey,err error)` attempts to parse RSA public key from PKIX key format or PKCS1 X509 certificate (`BEGIN PUBLIC KEY` and `BEGIN CERTIFICATE` headers)

```Go
package main

import (
	"fmt"
	Rsa "github.com/dvsekhvalnov/jose2go/keys/rsa"
	"io/ioutil"
)

func main() {

    keyBytes, _ := ioutil.ReadFile("public.cer")

    publicKey, err:=Rsa.ReadPublic(keyBytes)

    if(err!=nil) {
        panic("invalid key format")
    }

	fmt.Printf("publicKey = %v\n",publicKey)
}
```

#### ECC keys
1. `ecc.ReadPrivate(raw []byte) (key *ecdsa.PrivateKey,err error)` attemps to parse elliptic curve private key from PKCS1 or PKCS8 format (`BEGIN EC PRIVATE KEY` and `BEGIN PRIVATE KEY` headers)

```Go
package main

import (
	"fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
	"io/ioutil"
)

func main() {

    keyBytes, _ := ioutil.ReadFile("ec-private.pem")

    ecPrivKey, err:=ecc.ReadPrivate(keyBytes)

    if(err!=nil) {
        panic("invalid key format")
    }

	fmt.Printf("ecPrivKey = %v\n",ecPrivKey)
}
```

2. `ecc.ReadPublic(raw []byte) (key *ecdsa.PublicKey,err error)` attemps to parse elliptic curve public key from PKCS1 X509 or PKIX format (`BEGIN PUBLIC KEY` and `BEGIN CERTIFICATE` headers)

```Go
package main

import (
	"fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
	"io/ioutil"
)

func main() {

    keyBytes, _ := ioutil.ReadFile("ec-public.key")

    ecPubKey, err:=ecc.ReadPublic(keyBytes)

    if(err!=nil) {
        panic("invalid key format")
    }

	fmt.Printf("ecPubKey = %v\n",ecPubKey)
}
```

3. `ecc.NewPublic(x,y []byte) (*ecdsa.PublicKey)` constructs elliptic public key from (X,Y) represented as bytes. Supported are NIST curves P-256,P-384 and P-521. Curve detected automatically by input length.

```Go
package main

import (
	"fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
)

func main() {

    ecPubKey:=ecc.NewPublic([]byte{4, 114, 29, 223, 58, 3, 191, 170, 67, 128, 229, 33, 242, 178, 157, 150, 133, 25, 209, 139, 166, 69, 55, 26, 84, 48, 169, 165, 67, 232, 98, 9},
		 				    []byte{131, 116, 8, 14, 22, 150, 18, 75, 24, 181, 159, 78, 90, 51, 71, 159, 214, 186, 250, 47, 207, 246, 142, 127, 54, 183, 72, 72, 253, 21, 88, 53})

	fmt.Printf("ecPubKey = %v\n",ecPubKey)
}
```

4. `ecc.NewPrivate(x,y,d []byte) (*ecdsa.PrivateKey)` constructs elliptic private key from (X,Y) and D represented as bytes. Supported are NIST curves P-256,P-384 and P-521. Curve detected automatically by input length.

```Go
package main

import (
	"fmt"
    "github.com/dvsekhvalnov/jose2go/keys/ecc"
)

func main() {

    ecPrivKey:=ecc.NewPrivate([]byte{4, 114, 29, 223, 58, 3, 191, 170, 67, 128, 229, 33, 242, 178, 157, 150, 133, 25, 209, 139, 166, 69, 55, 26, 84, 48, 169, 165, 67, 232, 98, 9},
		 					  []byte{131, 116, 8, 14, 22, 150, 18, 75, 24, 181, 159, 78, 90, 51, 71, 159, 214, 186, 250, 47, 207, 246, 142, 127, 54, 183, 72, 72, 253, 21, 88, 53},
							  []byte{ 42, 148, 231, 48, 225, 196, 166, 201, 23, 190, 229, 199, 20, 39, 226, 70, 209, 148, 29, 70, 125, 14, 174, 66, 9, 198, 80, 251, 95, 107, 98, 206 })

	fmt.Printf("ecPrivKey = %v\n",ecPrivKey)
}
```

### More examples
Checkout `jose_test.go` for more examples.

## Changelog
### 1.2
- interface to access token headers after decoding
- interface to provide extra headers for token encoding
- two-phase validation support

### 1.1
- security and bug fixes

### 1.0
- initial stable version with full suite JOSE spec support
