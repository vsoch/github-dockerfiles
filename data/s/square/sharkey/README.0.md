This repository holds supplementary Go cryptography libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
# Kingpin - A Go (golang) command line and flag parser [![](https://godoc.org/github.com/alecthomas/kingpin?status.svg)](http://godoc.org/github.com/alecthomas/kingpin) [![Build Status](https://travis-ci.org/alecthomas/kingpin.png)](https://travis-ci.org/alecthomas/kingpin)

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

More [examples](https://github.com/alecthomas/kingpin/tree/master/examples) are available.

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
    - Exposed `HelpFlag` and `VersionFlag` for further cusomisation.
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

The yaml package is licensed under the LGPL with an exception that allows it to be linked statically. Please see the LICENSE file for details.


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

# goose

goose is a database migration tool.

You can manage your database's evolution by creating incremental SQL or Go scripts.

[![Build Status](https://drone.io/bitbucket.org/liamstask/goose/status.png)](https://drone.io/bitbucket.org/liamstask/goose/latest)

# Install

    $ go get bitbucket.org/liamstask/goose/cmd/goose

This will install the `goose` binary to your `$GOPATH/bin` directory.

You can also build goose into your own applications by importing `bitbucket.org/liamstask/goose/lib/goose`. Documentation is available at [godoc.org](http://godoc.org/bitbucket.org/liamstask/goose/lib/goose).

NOTE: the API is still new, and may undergo some changes.

# Usage

goose provides several commands to help manage your database schema.

## create

Create a new Go migration.

    $ goose create AddSomeColumns
    $ goose: created db/migrations/20130106093224_AddSomeColumns.go

Edit the newly created script to define the behavior of your migration.

You can also create an SQL migration:

    $ goose create AddSomeColumns sql
    $ goose: created db/migrations/20130106093224_AddSomeColumns.sql

## up

Apply all available migrations.

    $ goose up
    $ goose: migrating db environment 'development', current version: 0, target: 3
    $ OK    001_basics.sql
    $ OK    002_next.sql
    $ OK    003_and_again.go

### option: pgschema

Use the `pgschema` flag with the `up` command specify a postgres schema.

    $ goose -pgschema=my_schema_name up
    $ goose: migrating db environment 'development', current version: 0, target: 3
    $ OK    001_basics.sql
    $ OK    002_next.sql
    $ OK    003_and_again.go

## down

Roll back a single migration from the current version.

    $ goose down
    $ goose: migrating db environment 'development', current version: 3, target: 2
    $ OK    003_and_again.go

## redo

Roll back the most recently applied migration, then run it again.

    $ goose redo
    $ goose: migrating db environment 'development', current version: 3, target: 2
    $ OK    003_and_again.go
    $ goose: migrating db environment 'development', current version: 2, target: 3
    $ OK    003_and_again.go

## status

Print the status of all migrations:

    $ goose status
    $ goose: status for environment 'development'
    $   Applied At                  Migration
    $   =======================================
    $   Sun Jan  6 11:25:03 2013 -- 001_basics.sql
    $   Sun Jan  6 11:25:03 2013 -- 002_next.sql
    $   Pending                  -- 003_and_again.go

## dbversion

Print the current version of the database:

    $ goose dbversion
    $ goose: dbversion 002


`goose -h` provides more detailed info on each command.


# Migrations

goose supports migrations written in SQL or in Go - see the `goose create` command above for details on how to generate them.

## SQL Migrations

A sample SQL migration looks like:

```sql
-- +goose Up
CREATE TABLE post (
    id int NOT NULL,
    title text,
    body text,
    PRIMARY KEY(id)
);

-- +goose Down
DROP TABLE post;
```

Notice the annotations in the comments. Any statements following `-- +goose Up` will be executed as part of a forward migration, and any statements following `-- +goose Down` will be executed as part of a rollback.

By default, SQL statements are delimited by semicolons - in fact, query statements must end with a semicolon to be properly recognized by goose.

More complex statements (PL/pgSQL) that have semicolons within them must be annotated with `-- +goose StatementBegin` and `-- +goose StatementEnd` to be properly recognized. For example:

```sql
-- +goose Up
-- +goose StatementBegin
CREATE OR REPLACE FUNCTION histories_partition_creation( DATE, DATE )
returns void AS $$
DECLARE
  create_query text;
BEGIN
  FOR create_query IN SELECT
      'CREATE TABLE IF NOT EXISTS histories_'
      || TO_CHAR( d, 'YYYY_MM' )
      || ' ( CHECK( created_at >= timestamp '''
      || TO_CHAR( d, 'YYYY-MM-DD 00:00:00' )
      || ''' AND created_at < timestamp '''
      || TO_CHAR( d + INTERVAL '1 month', 'YYYY-MM-DD 00:00:00' )
      || ''' ) ) inherits ( histories );'
    FROM generate_series( $1, $2, '1 month' ) AS d
  LOOP
    EXECUTE create_query;
  END LOOP;  -- LOOP END
END;         -- FUNCTION END
$$
language plpgsql;
-- +goose StatementEnd
```

## Go Migrations

A sample Go migration looks like:

```go
package main

import (
    "database/sql"
    "fmt"
)

func Up_20130106222315(txn *sql.Tx) {
    fmt.Println("Hello from migration 20130106222315 Up!")
}

func Down_20130106222315(txn *sql.Tx) {
    fmt.Println("Hello from migration 20130106222315 Down!")
}
```

`Up_20130106222315()` will be executed as part of a forward migration, and `Down_20130106222315()` will be executed as part of a rollback.

The numeric portion of the function name (`20130106222315`) must be the leading portion of migration's filename, such as `20130106222315_descriptive_name.go`. `goose create` does this by default.

A transaction is provided, rather than the DB instance directly, since goose also needs to record the schema version within the same transaction. Each migration should run as a single transaction to ensure DB integrity, so it's good practice anyway.


# Configuration

goose expects you to maintain a folder (typically called "db"), which contains the following:

* a `dbconf.yml` file that describes the database configurations you'd like to use
* a folder called "migrations" which contains `.sql` and/or `.go` scripts that implement your migrations

You may use the `-path` option to specify an alternate location for the folder containing your config and migrations.

A sample `dbconf.yml` looks like

```yml
development:
    driver: postgres
    open: user=liam dbname=tester sslmode=disable
```

Here, `development` specifies the name of the environment, and the `driver` and `open` elements are passed directly to database/sql to access the specified database.

You may include as many environments as you like, and you can use the `-env` command line option to specify which one to use. goose defaults to using an environment called `development`.

goose will expand environment variables in the `open` element. For an example, see the Heroku section below.

## Other Drivers
goose knows about some common SQL drivers, but it can still be used to run Go-based migrations with any driver supported by `database/sql`. An import path and known dialect are required.

Currently, available dialects are: "postgres", "mysql", or "sqlite3"

To run Go-based migrations with another driver, specify its import path and dialect, as shown below.

```yml
customdriver:
    driver: custom
    open: custom open string
    import: github.com/custom/driver
    dialect: mysql
```

NOTE: Because migrations written in SQL are executed directly by the goose binary, only drivers compiled into goose may be used for these migrations.

## Using goose with Heroku

These instructions assume that you're using [Keith Rarick's Heroku Go buildpack](https://github.com/kr/heroku-buildpack-go). First, add a file to your project called (e.g.) `install_goose.go` to trigger building of the goose executable during deployment, with these contents:

```go
// use build constraints to work around http://code.google.com/p/go/issues/detail?id=4210
// +build heroku

// note: need at least one blank line after build constraint
package main

import _ "bitbucket.org/liamstask/goose/cmd/goose"
```

[Set up your Heroku database(s) as usual.](https://devcenter.heroku.com/articles/heroku-postgresql)

Then make use of environment variable expansion in your `dbconf.yml`:

```yml
production:
    driver: postgres
    open: $DATABASE_URL
```

To run goose in production, use `heroku run`:

    heroku run goose -env production up

# Contributors

Thank you!

* Josh Bleecher Snyder (josharian)
* Abigail Walthall (ghthor)
* Daniel Heath (danielrheath)
* Chris Baynes (chris_baynes)
* Michael Gerow (gerow)
* Vytautas Šaltenis (rtfb)
* James Cooper (coopernurse)
* Gyepi Sam (gyepisam)
* Matt Sherman (clipperhouse)
* runner_mei
* John Luebs (jkl1337)
* Luke Hutton (lukehutton)
* Kevin Gorjan (kevingorjan)
* Brendan Fosberry (Fozz)
* Nate Guerin (gusennan)
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
# pq - A pure Go postgres driver for Go's database/sql package

[![Build Status](https://travis-ci.org/lib/pq.png?branch=master)](https://travis-ci.org/lib/pq)

## Install

	go get github.com/lib/pq

## Docs

For detailed documentation and basic usage examples, please see the package
documentation at <http://godoc.org/github.com/lib/pq>.

## Tests

`go test` is used for testing.  A running PostgreSQL server is
required, with the ability to log in.  The default database to connect
to test with is "pqgotest," but it can be overridden using environment
variables.

Example:

	PGHOST=/run/postgresql go test github.com/lib/pq

Optionally, a benchmark suite can be run as part of the tests:

	PGHOST=/run/postgresql go test -bench .

## Features

* SSL
* Handles bad connections for `database/sql`
* Scan `time.Time` correctly (i.e. `timestamp[tz]`, `time[tz]`, `date`)
* Scan binary blobs correctly (i.e. `bytea`)
* Package for `hstore` support
* COPY FROM support
* pq.ParseURL for converting urls to connection strings for sql.Open.
* Many libpq compatible environment variables
* Unix socket support
* Notifications: `LISTEN`/`NOTIFY`
* pgpass support

## Future / Things you can help with

* Better COPY FROM / COPY TO (see discussion in #181)

## Thank you (alphabetical)

Some of these contributors are from the original library `bmizerany/pq.go` whose
code still exists in here.

* Andy Balholm (andybalholm)
* Ben Berkert (benburkert)
* Benjamin Heatwole (bheatwole)
* Bill Mill (llimllib)
* Bjørn Madsen (aeons)
* Blake Gentry (bgentry)
* Brad Fitzpatrick (bradfitz)
* Charlie Melbye (cmelbye)
* Chris Bandy (cbandy)
* Chris Gilling (cgilling)
* Chris Walsh (cwds)
* Dan Sosedoff (sosedoff)
* Daniel Farina (fdr)
* Eric Chlebek (echlebek)
* Eric Garrido (minusnine)
* Eric Urban (hydrogen18)
* Everyone at The Go Team
* Evan Shaw (edsrzf)
* Ewan Chou (coocood)
* Fazal Majid (fazalmajid)
* Federico Romero (federomero)
* Fumin (fumin)
* Gary Burd (garyburd)
* Heroku (heroku)
* James Pozdena (jpoz)
* Jason McVetta (jmcvetta)
* Jeremy Jay (pbnjay)
* Joakim Sernbrant (serbaut)
* John Gallagher (jgallagher)
* Jonathan Rudenberg (titanous)
* Joël Stemmer (jstemmer)
* Kamil Kisiel (kisielk)
* Kelly Dunn (kellydunn)
* Keith Rarick (kr)
* Kir Shatrov (kirs)
* Lann Martin (lann)
* Maciek Sakrejda (uhoh-itsmaciek)
* Marc Brinkmann (mbr)
* Marko Tiikkaja (johto)
* Matt Newberry (MattNewberry)
* Matt Robenolt (mattrobenolt)
* Martin Olsen (martinolsen)
* Mike Lewis (mikelikespie)
* Nicolas Patry (Narsil)
* Oliver Tonnhofer (olt)
* Patrick Hayes (phayes)
* Paul Hammond (paulhammond)
* Ryan Smith (ryandotsmith)
* Samuel Stauffer (samuel)
* Timothée Peignier (cyberdelia)
* Travis Cline (tmc)
* TruongSinh Tran-Nguyen (truongsinh)
* Yaismel Miranda (ympons)
* notedit (notedit)
This directory contains certificates and private keys for testing some
SSL-related functionality in Travis.  Do NOT use these certificates for
anything other than testing.
# Go-MySQL-Driver

A MySQL-Driver for Go's [database/sql](http://golang.org/pkg/database/sql) package

![Go-MySQL-Driver logo](https://raw.github.com/wiki/go-sql-driver/mysql/gomysql_m.png "Golang Gopher holding the MySQL Dolphin")

**Latest stable Release:** [Version 1.2 (June 03, 2014)](https://github.com/go-sql-driver/mysql/releases)

[![Build Status](https://travis-ci.org/go-sql-driver/mysql.png?branch=master)](https://travis-ci.org/go-sql-driver/mysql)

---------------------------------------
  * [Features](#features)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Usage](#usage)
    * [DSN (Data Source Name)](#dsn-data-source-name)
      * [Password](#password)
      * [Protocol](#protocol)
      * [Address](#address)
      * [Parameters](#parameters)
      * [Examples](#examples)
    * [LOAD DATA LOCAL INFILE support](#load-data-local-infile-support)
    * [time.Time support](#timetime-support)
    * [Unicode support](#unicode-support)
  * [Testing / Development](#testing--development)
  * [License](#license)

---------------------------------------

## Features
  * Lightweight and [fast](https://github.com/go-sql-driver/sql-benchmark "golang MySQL-Driver performance")
  * Native Go implementation. No C-bindings, just pure Go
  * Connections over TCP/IPv4, TCP/IPv6, Unix domain sockets or [custom protocols](http://godoc.org/github.com/go-sql-driver/mysql#DialFunc)
  * Automatic handling of broken connections
  * Automatic Connection Pooling *(by database/sql package)*
  * Supports queries larger than 16MB
  * Full [`sql.RawBytes`](http://golang.org/pkg/database/sql/#RawBytes) support.
  * Intelligent `LONG DATA` handling in prepared statements
  * Secure `LOAD DATA LOCAL INFILE` support with file Whitelisting and `io.Reader` support
  * Optional `time.Time` parsing
  * Optional placeholder interpolation

## Requirements
  * Go 1.2 or higher
  * MySQL (4.1+), MariaDB, Percona Server, Google CloudSQL or Sphinx (2.2.3+)

---------------------------------------

## Installation
Simple install the package to your [$GOPATH](http://code.google.com/p/go-wiki/wiki/GOPATH "GOPATH") with the [go tool](http://golang.org/cmd/go/ "go command") from shell:
```bash
$ go get github.com/go-sql-driver/mysql
```
Make sure [Git is installed](http://git-scm.com/downloads) on your machine and in your system's `PATH`.

## Usage
_Go MySQL Driver_ is an implementation of Go's `database/sql/driver` interface. You only need to import the driver and can use the full [`database/sql`](http://golang.org/pkg/database/sql) API then.

Use `mysql` as `driverName` and a valid [DSN](#dsn-data-source-name)  as `dataSourceName`:
```go
import "database/sql"
import _ "github.com/go-sql-driver/mysql"

db, err := sql.Open("mysql", "user:password@/dbname")
```

[Examples are available in our Wiki](https://github.com/go-sql-driver/mysql/wiki/Examples "Go-MySQL-Driver Examples").


### DSN (Data Source Name)

The Data Source Name has a common format, like e.g. [PEAR DB](http://pear.php.net/manual/en/package.database.db.intro-dsn.php) uses it, but without type-prefix (optional parts marked by squared brackets):
```
[username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]
```

A DSN in its fullest form:
```
username:password@protocol(address)/dbname?param=value
```

Except for the databasename, all values are optional. So the minimal DSN is:
```
/dbname
```

If you do not want to preselect a database, leave `dbname` empty:
```
/
```
This has the same effect as an empty DSN string:
```

```

Alternatively, [Config.FormatDSN](https://godoc.org/github.com/go-sql-driver/mysql#Config.FormatDSN) can be used to create a DSN string by filling a struct.

#### Password
Passwords can consist of any character. Escaping is **not** necessary.

#### Protocol
See [net.Dial](http://golang.org/pkg/net/#Dial) for more information which networks are available.
In general you should use an Unix domain socket if available and TCP otherwise for best performance.

#### Address
For TCP and UDP networks, addresses have the form `host:port`.
If `host` is a literal IPv6 address, it must be enclosed in square brackets.
The functions [net.JoinHostPort](http://golang.org/pkg/net/#JoinHostPort) and [net.SplitHostPort](http://golang.org/pkg/net/#SplitHostPort) manipulate addresses in this form.

For Unix domain sockets the address is the absolute path to the MySQL-Server-socket, e.g. `/var/run/mysqld/mysqld.sock` or `/tmp/mysql.sock`.

#### Parameters
*Parameters are case-sensitive!*

Notice that any of `true`, `TRUE`, `True` or `1` is accepted to stand for a true boolean value. Not surprisingly, false can be specified as any of: `false`, `FALSE`, `False` or `0`.

##### `allowAllFiles`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`allowAllFiles=true` disables the file Whitelist for `LOAD DATA LOCAL INFILE` and allows *all* files.
[*Might be insecure!*](http://dev.mysql.com/doc/refman/5.7/en/load-data-local.html)

##### `allowCleartextPasswords`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`allowCleartextPasswords=true` allows using the [cleartext client side plugin](http://dev.mysql.com/doc/en/cleartext-authentication-plugin.html) if required by an account, such as one defined with the [PAM authentication plugin](http://dev.mysql.com/doc/en/pam-authentication-plugin.html). Sending passwords in clear text may be a security problem in some configurations. To avoid problems if there is any possibility that the password would be intercepted, clients should connect to MySQL Server using a method that protects the password. Possibilities include [TLS / SSL](#tls), IPsec, or a private network.

##### `allowOldPasswords`

```
Type:           bool
Valid Values:   true, false
Default:        false
```
`allowOldPasswords=true` allows the usage of the insecure old password method. This should be avoided, but is necessary in some cases. See also [the old_passwords wiki page](https://github.com/go-sql-driver/mysql/wiki/old_passwords).

##### `charset`

```
Type:           string
Valid Values:   <name>
Default:        none
```

Sets the charset used for client-server interaction (`"SET NAMES <value>"`). If multiple charsets are set (separated by a comma), the following charset is used if setting the charset failes. This enables for example support for `utf8mb4` ([introduced in MySQL 5.5.3](http://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html)) with fallback to `utf8` for older servers (`charset=utf8mb4,utf8`).

Usage of the `charset` parameter is discouraged because it issues additional queries to the server.
Unless you need the fallback behavior, please use `collation` instead.

##### `collation`

```
Type:           string
Valid Values:   <name>
Default:        utf8_general_ci
```

Sets the collation used for client-server interaction on connection. In contrast to `charset`, `collation` does not issue additional queries. If the specified collation is unavailable on the target server, the connection will fail.

A list of valid charsets for a server is retrievable with `SHOW COLLATION`.

##### `clientFoundRows`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`clientFoundRows=true` causes an UPDATE to return the number of matching rows instead of the number of rows changed.

##### `columnsWithAlias`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

When `columnsWithAlias` is true, calls to `sql.Rows.Columns()` will return the table alias and the column name separated by a dot. For example:

```
SELECT u.id FROM users as u
```

will return `u.id` instead of just `id` if `columnsWithAlias=true`.

##### `interpolateParams`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

If `interpolateParams` is true, placeholders (`?`) in calls to `db.Query()` and `db.Exec()` are interpolated into a single query string with given parameters. This reduces the number of roundtrips, since the driver has to prepare a statement, execute it with given parameters and close the statement again with `interpolateParams=false`.

*This can not be used together with the multibyte encodings BIG5, CP932, GB2312, GBK or SJIS. These are blacklisted as they may [introduce a SQL injection vulnerability](http://stackoverflow.com/a/12118602/3430118)!*

##### `loc`

```
Type:           string
Valid Values:   <escaped name>
Default:        UTC
```

Sets the location for time.Time values (when using `parseTime=true`). *"Local"* sets the system's location. See [time.LoadLocation](http://golang.org/pkg/time/#LoadLocation) for details.

Note that this sets the location for time.Time values but does not change MySQL's [time_zone setting](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html). For that see the [time_zone system variable](#system-variables), which can also be set as a DSN parameter.

Please keep in mind, that param values must be [url.QueryEscape](http://golang.org/pkg/net/url/#QueryEscape)'ed. Alternatively you can manually replace the `/` with `%2F`. For example `US/Pacific` would be `loc=US%2FPacific`.

##### `multiStatements`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

Allow multiple statements in one query. While this allows batch queries, it also greatly increases the risk of SQL injections. Only the result of the first query is returned, all other results are silently discarded.

When `multiStatements` is used, `?` parameters must only be used in the first statement.


##### `parseTime`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`parseTime=true` changes the output type of `DATE` and `DATETIME` values to `time.Time` instead of `[]byte` / `string`


##### `readTimeout`

```
Type:           decimal number
Default:        0
```

I/O read timeout. The value must be a decimal number with an unit suffix ( *"ms"*, *"s"*, *"m"*, *"h"* ), such as *"30s"*, *"0.5m"* or *"1m30s"*.


##### `strict`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`strict=true` enables the strict mode in which MySQL warnings are treated as errors.

By default MySQL also treats notes as warnings. Use [`sql_notes=false`](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_sql_notes) to ignore notes. See the [examples](#examples) for an DSN example.


##### `timeout`

```
Type:           decimal number
Default:        OS default
```

*Driver* side connection timeout. The value must be a decimal number with an unit suffix ( *"ms"*, *"s"*, *"m"*, *"h"* ), such as *"30s"*, *"0.5m"* or *"1m30s"*. To set a server side timeout, use the parameter [`wait_timeout`](http://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html#sysvar_wait_timeout).


##### `tls`

```
Type:           bool / string
Valid Values:   true, false, skip-verify, <name>
Default:        false
```

`tls=true` enables TLS / SSL encrypted connection to the server. Use `skip-verify` if you want to use a self-signed or invalid certificate (server side). Use a custom value registered with [`mysql.RegisterTLSConfig`](http://godoc.org/github.com/go-sql-driver/mysql#RegisterTLSConfig).


##### `writeTimeout`

```
Type:           decimal number
Default:        0
```

I/O write timeout. The value must be a decimal number with an unit suffix ( *"ms"*, *"s"*, *"m"*, *"h"* ), such as *"30s"*, *"0.5m"* or *"1m30s"*.


##### System Variables

All other parameters are interpreted as system variables:
  * `autocommit`: `"SET autocommit=<value>"`
  * [`time_zone`](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html): `"SET time_zone=<value>"`
  * [`tx_isolation`](https://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_tx_isolation): `"SET tx_isolation=<value>"`
  * `param`: `"SET <param>=<value>"`

*The values must be [url.QueryEscape](http://golang.org/pkg/net/url/#QueryEscape)'ed!*

#### Examples
```
user@unix(/path/to/socket)/dbname
```

```
root:pw@unix(/tmp/mysql.sock)/myDatabase?loc=Local
```

```
user:password@tcp(localhost:5555)/dbname?tls=skip-verify&autocommit=true
```

Use the [strict mode](#strict) but ignore notes:
```
user:password@/dbname?strict=true&sql_notes=false
```

TCP via IPv6:
```
user:password@tcp([de:ad:be:ef::ca:fe]:80)/dbname?timeout=90s&collation=utf8mb4_unicode_ci
```

TCP on a remote host, e.g. Amazon RDS:
```
id:password@tcp(your-amazonaws-uri.com:3306)/dbname
```

Google Cloud SQL on App Engine:
```
user@cloudsql(project-id:instance-name)/dbname
```

TCP using default port (3306) on localhost:
```
user:password@tcp/dbname?charset=utf8mb4,utf8&sys_var=esc%40ped
```

Use the default protocol (tcp) and host (localhost:3306):
```
user:password@/dbname
```

No Database preselected:
```
user:password@/
```

### `LOAD DATA LOCAL INFILE` support
For this feature you need direct access to the package. Therefore you must change the import path (no `_`):
```go
import "github.com/go-sql-driver/mysql"
```

Files must be whitelisted by registering them with `mysql.RegisterLocalFile(filepath)` (recommended) or the Whitelist check must be deactivated by using the DSN parameter `allowAllFiles=true` ([*Might be insecure!*](http://dev.mysql.com/doc/refman/5.7/en/load-data-local.html)).

To use a `io.Reader` a handler function must be registered with `mysql.RegisterReaderHandler(name, handler)` which returns a `io.Reader` or `io.ReadCloser`. The Reader is available with the filepath `Reader::<name>` then. Choose different names for different handlers and `DeregisterReaderHandler` when you don't need it anymore.

See the [godoc of Go-MySQL-Driver](http://godoc.org/github.com/go-sql-driver/mysql "golang mysql driver documentation") for details.


### `time.Time` support
The default internal output type of MySQL `DATE` and `DATETIME` values is `[]byte` which allows you to scan the value into a `[]byte`, `string` or `sql.RawBytes` variable in your programm.

However, many want to scan MySQL `DATE` and `DATETIME` values into `time.Time` variables, which is the logical opposite in Go to `DATE` and `DATETIME` in MySQL. You can do that by changing the internal output type from `[]byte` to `time.Time` with the DSN parameter `parseTime=true`. You can set the default [`time.Time` location](http://golang.org/pkg/time/#Location) with the `loc` DSN parameter.

**Caution:** As of Go 1.1, this makes `time.Time` the only variable type you can scan `DATE` and `DATETIME` values into. This breaks for example [`sql.RawBytes` support](https://github.com/go-sql-driver/mysql/wiki/Examples#rawbytes).

Alternatively you can use the [`NullTime`](http://godoc.org/github.com/go-sql-driver/mysql#NullTime) type as the scan destination, which works with both `time.Time` and `string` / `[]byte`.


### Unicode support
Since version 1.1 Go-MySQL-Driver automatically uses the collation `utf8_general_ci` by default.

Other collations / charsets can be set using the [`collation`](#collation) DSN parameter.

Version 1.0 of the driver recommended adding `&charset=utf8` (alias for `SET NAMES utf8`) to the DSN to enable proper UTF-8 support. This is not necessary anymore. The [`collation`](#collation) parameter should be preferred to set another collation / charset than the default.

See http://dev.mysql.com/doc/refman/5.7/en/charset-unicode.html for more details on MySQL's Unicode support.


## Testing / Development
To run the driver tests you may need to adjust the configuration. See the [Testing Wiki-Page](https://github.com/go-sql-driver/mysql/wiki/Testing "Testing") for details.

Go-MySQL-Driver is not feature-complete yet. Your help is very appreciated.
If you want to contribute, you can work on an [open issue](https://github.com/go-sql-driver/mysql/issues?state=open) or review a [pull request](https://github.com/go-sql-driver/mysql/pulls).

See the [Contribution Guidelines](https://github.com/go-sql-driver/mysql/blob/master/CONTRIBUTING.md) for details.

---------------------------------------

## License
Go-MySQL-Driver is licensed under the [Mozilla Public License Version 2.0](https://raw.github.com/go-sql-driver/mysql/master/LICENSE)

Mozilla summarizes the license scope as follows:
> MPL: The copyleft applies to any files containing MPLed code.


That means:
  * You can **use** the **unchanged** source code both in private and commercially
  * When distributing, you **must publish** the source code of any **changed files** licensed under the MPL 2.0 under a) the MPL 2.0 itself or b) a compatible license (e.g. GPL 3.0 or Apache License 2.0)
  * You **needn't publish** the source code of your library as long as the files licensed under the MPL 2.0 are **unchanged**

Please read the [MPL 2.0 FAQ](http://www.mozilla.org/MPL/2.0/FAQ.html) if you have further questions regarding the license.

You can read the full terms here: [LICENSE](https://raw.github.com/go-sql-driver/mysql/master/LICENSE)

![Go Gopher and MySQL Dolphin](https://raw.github.com/wiki/go-sql-driver/mysql/go-mysql-driver_m.jpg "Golang Gopher transporting the MySQL Dolphin in a wheelbarrow")

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

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
gorilla/handlers
================
[![GoDoc](https://godoc.org/github.com/gorilla/handlers?status.svg)](https://godoc.org/github.com/gorilla/handlers) [![Build Status](https://travis-ci.org/gorilla/handlers.svg?branch=master)](https://travis-ci.org/gorilla/handlers)

Package handlers is a collection of handlers (aka "HTTP middleware") for use
with Go's `net/http` package (or any framework supporting `http.Handler`), including:

* [**LoggingHandler**](https://godoc.org/github.com/gorilla/handlers#LoggingHandler) for logging HTTP requests in the Apache [Common Log
  Format](http://httpd.apache.org/docs/2.2/logs.html#common).
* [**CombinedLoggingHandler**](https://godoc.org/github.com/gorilla/handlers#CombinedLoggingHandler) for logging HTTP requests in the Apache [Combined Log
  Format](http://httpd.apache.org/docs/2.2/logs.html#combined) commonly used by
  both Apache and nginx.
* [**CompressHandler**](https://godoc.org/github.com/gorilla/handlers#CompressHandler) for gzipping responses.
* [**ContentTypeHandler**](https://godoc.org/github.com/gorilla/handlers#ContentTypeHandler) for validating requests against a list of accepted
  content types.
* [**MethodHandler**](https://godoc.org/github.com/gorilla/handlers#MethodHandler) for matching HTTP methods against handlers in a
  `map[string]http.Handler`
* [**ProxyHeaders**](https://godoc.org/github.com/gorilla/handlers#ProxyHeaders) for populating `r.RemoteAddr` and `r.URL.Scheme` based on the
  `X-Forwarded-For`, `X-Real-IP`, `X-Forwarded-Proto` and RFC7239 `Forwarded`
  headers when running a Go server behind a HTTP reverse proxy.
* [**CanonicalHost**](https://godoc.org/github.com/gorilla/handlers#CanonicalHost) for re-directing to the preferred host when handling multiple 
  domains (i.e. multiple CNAME aliases).
* [**RecoveryHandler**](https://godoc.org/github.com/gorilla/handlers#RecoveryHandler) for recovering from unexpected panics.

Other handlers are documented [on the Gorilla
website](http://www.gorillatoolkit.org/pkg/handlers).

## Example

A simple example using `handlers.LoggingHandler` and `handlers.CompressHandler`:

```go
import (
    "net/http"
    "github.com/gorilla/handlers"
)

func main() {
    r := http.NewServeMux()

    // Only log requests to our admin dashboard to stdout
    r.Handle("/admin", handlers.LoggingHandler(os.Stdout, http.HandlerFunc(ShowAdminDashboard)))
    r.HandleFunc("/", ShowIndex)

    // Wrap our server with our gzip handler to gzip compress all responses.
    http.ListenAndServe(":8000", handlers.CompressHandler(r))
}
```

## License

BSD licensed. See the included LICENSE file for details.

// Copyright 2013 Google, Inc.  All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Gypsy is a simplified YAML parser written in Go.  It is intended to be used as
// a simple configuration file, and as such does not support a lot of the more
// nuanced syntaxes allowed in full-fledged YAML.  YAML does not allow indent with
// tabs, and GYPSY does not ever consider a tab to be a space character.  It is
// recommended that your editor be configured to convert tabs to spaces when
// editing Gypsy config files.
//
// Gypsy understands the following to be a list:
//
//     - one
//     - two
//     - three
//
// This is parsed as a `yaml.List`, and can be retrieved from the
// `yaml.Node.List()` method.  In this case, each element of the `yaml.List` would
// be a `yaml.Scalar` whose value can be retrieved with the `yaml.Scalar.String()`
// method.
//
// Gypsy understands the following to be a mapping:
//
//     key:     value
//     foo:     bar
//     running: away
//
// A mapping is an unordered list of `key:value` pairs.  All whitespace after the
// colon is stripped from the value and is used for alignment purposes during
// export.  If the value is not a list or a map, everything after the first
// non-space character until the end of the line is used as the `yaml.Scalar`
// value.
//
// Gypsy allows arbitrary nesting of maps inside lists, lists inside of maps, and
// maps and/or lists nested inside of themselves.
//
// A map inside of a list:
//
//     - name: John Smith
//       age:  42
//     - name: Jane Smith
//       age:  45
//
// A list inside of a map:
//
//     schools:
//       - Meadow Glen
//       - Forest Creek
//       - Shady Grove
//     libraries:
//       - Joseph Hollingsworth Memorial
//       - Andrew Keriman Memorial
//
// A list of lists:
//
//     - - one
//       - two
//       - three
//     - - un
//       - deux
//       - trois
//     - - ichi
//       - ni
//       - san
//
// A map of maps:
//
//     google:
//       company: Google, Inc.
//       ticker:  GOOG
//       url:     http://google.com/
//     yahoo:
//       company: Yahoo, Inc.
//       ticker:  YHOO
//       url:     http://yahoo.com/
//
// In the case of a map of maps, all sub-keys must be on subsequent lines and
// indented equally.  It is allowable for the first key/value to be on the same
// line if there is more than one key/value pair, but this is not recommended.
//
// Values can also be expressed in long form (leading whitespace of the first line
// is removed from it and all subsequent lines).  In the normal (baz) case,
// newlines are treated as spaces, all indentation is removed.  In the folded case
// (bar), newlines are treated as spaces, except pairs of newlines (e.g. a blank
// line) are treated as a single newline, only the indentation level of the first
// line is removed, and newlines at the end of indented lines are preserved.  In
// the verbatim (foo) case, only the indent at the level of the first line is
// stripped.  The example:
//
//     foo: |
//       lorem ipsum dolor
//       sit amet
//     bar: >
//       lorem ipsum
//
//         dolor
//
//       sit amet
//     baz:
//       lorem ipsum
//        dolor sit amet
//
// The YAML subset understood by Gypsy can be expressed (loosely) in the following
// grammar (not including comments):
//
//               OBJECT = MAPPING | SEQUENCE | SCALAR .
//         SHORT-OBJECT = SHORT-MAPPING | SHORT-SEQUENCE | SHORT-SCALAR .
//                  EOL = '\n'
//
//              MAPPING = { LONG-MAPPING | SHORT-MAPPING } .
//             SEQUENCE = { LONG-SEQUENCE | SHORT-SEQUENCE } .
//               SCALAR = { LONG-SCALAR | SHORT-SCALAR } .
//
//         LONG-MAPPING = { INDENT KEY ':' OBJECT EOL } .
//        SHORT-MAPPING = '{' KEY ':' SHORT-OBJECT { ',' KEY ':' SHORT-OBJECT } '}' EOL .
//
//        LONG-SEQUENCE = { INDENT '-' OBJECT EOL } EOL .
//       SHORT-SEQUENCE = '[' SHORT-OBJECT { ',' SHORT-OBJECT } ']' EOL .
//
//          LONG-SCALAR = ( '|' | '>' | ) EOL { INDENT SHORT-SCALAR EOL }
//         SHORT-SCALAR = { alpha | digit | punct | ' ' | '\t' } .
//
//                  KEY = { alpha | digit }
//               INDENT = { ' ' }
//
// Any line where the first non-space character is a sharp sign (#) is a comment.
// It will be ignored.
// Only full-line comments are allowed.
package yaml

// BUG(kevlar): Multi-line strings are currently not supported.
Sorry for my poor English. If you can help with improving the English in this documentation, please contact me.

## MyMySQL v1.5.4 (2015-01-08)

This package contains MySQL client API written entirely in Go. It is designed
to work with the MySQL protocol version 4.1 or greater. It definitely works
well with MySQL server version 5.0 and 5.1 (I use these versions of MySQL
servers for my applications). Some people claim that mymysql works with older
versions of MySQL protocol too.

## Changelog

v1.5.4: Bugs fixed in native and godrv packages.

v1.5.3: Bugs fixed in new godrv code.

v1.5.1: Conn.NetConn method added. 

v1.5: Needs Go 1.1 (time.ParseInLocation and net.Dialer) to compile.

v1.4: `Stmt.ResetParams`, `Stmt.Map` and `Stmt.NumFields` methods disappeared.
New `Stmt.Fields` method. *godrv* implements `driver.Queryer` interface which
improves performance when compiled with Go tip.

v1.3: Overall performance improved by factor 1.5 to 1.8. All Encode* functions
now accept properly sized `[]byte` slice as first argument.

v1.2: Faster execution of simple queries in *mymysql/godrv*. `EscapeString`
method renamed to `Escape`.

v1.1: Client error codes moved from *mymysql/native* pacage to *mymysql/mysql*.

v1.0: Transactions added to autorc, new Transaction.IsValid method. I think
this library is mature enough to release it as v1.0

v0.4.11: Add Reconnect, Register, SetMaxPktSize, Bind to autorc.

v0.4.10: New *Clone* method for create connection from other connection.

v0.4.9: New method for create connection from configuration in file: *NewFromCF*.

v0.4.8: New methods for obtain only first/last row from result set. Better
implementation of discarding rows in End method.

v0.4.7: ScanRow and MakeRow methods addad. ScanRow is more efficient than GetRow because it doesn't allocate memory for every row received from the server. *godrv* Value.Next method now uses the new ScanRow method.

v0.4.6: StatusOnly method added to mysql.Result.

v0.4.5: New autorc.Conn.PrepareOnce method.

v0.4.4:

1. Row.Int, Row.Uint, Row.Int64, ... methods now panic in case of error.
2. New Row.Float method.

v0.4.3:

1. Fixed issue with panic when the server returns MYSQL_TYPE_NEWDECIMAL.
2. Decimals are returned as float64 (previously they were returned as []byte).

v0.4.2:

1. A lot of changes with MySQL time handling:

- Datetime type replaced by time.Time.
- Time type replaced by time.Duration.
- Support for time.Time type added to godrv.

2. row.Int64/row.Uint64 methods added.

3. Rename BindParams to Bind.

v0.4.1:

BindParams supports Go bool type. 

v0.4:

1. Modular design:

- MySQL wire protocol handling moved to *mymysql/native*
- Thread safe wrapper of *native* engine in separate *mymysql/thrsafe*
- *mymysql/mysql* package contains definitions of interfaces to engines and
common (engine-independent) functions.
- Automatic reconnect interface moved to *mymysql/autorc*.

2. *mysql.New* and other functions returns mostly interface types. So all
previously exported members were converted to methods (with except *mysql.Row*
and *mysql.Field* - their definition didn't changed).

3. Transactions added. If you use *mymysql/thrsafe" engine transactions are
fully thread safe.

4. Driver for *exp/sql*.

## Installing

To install all subpackages of *mymysql* you need to goinstal three of them:

	$ go get github.com/ziutek/mymysql/thrsafe
	$ go get github.com/ziutek/mymysql/autorc
	$ go get github.com/ziutek/mymysql/godrv

*go get* automagically selects the proper version of *mymysql* for your Go 
release. After this command *mymysql* is ready to use.

## Testing

For testing you will need to create the test database and a test user:

	mysql> create database test;
	mysql> grant all privileges on test.* to testuser@localhost;
	mysql> set password for testuser@localhost = password("TestPasswd9");

Make sure that MySQL *max_allowed_packet* variable in *my.cnf* is equal or greater than 34M (In order to test long packets).

The default MySQL server address is *127.0.0.1:3306*.

Next run tests:

	$ cd $GOPATH/src/github.com/ziutek/mymysql
	$ ./all.bash test

## Examples

### Example 1

	package main

	import (
		"os"
		"github.com/ziutek/mymysql/mysql"
		_ "github.com/ziutek/mymysql/native" // Native engine
		// _ "github.com/ziutek/mymysql/thrsafe" // Thread safe engine
	)

	func main() {
		db := mysql.New("tcp", "", "127.0.0.1:3306", user, pass, dbname)

		err := db.Connect()
		if err != nil {
			panic(err)
		}

		rows, res, err := db.Query("select * from X where id > %d", 20)
		if err != nil {
			panic(err)
		}

		for _, row := range rows {
			for _, col := range row {
				if col == nil {
					// col has NULL value
				} else {
					// Do something with text in col (type []byte)
				}
			}
			// You can get specific value from a row
			val1 := row[1].([]byte)

			// You can use it directly if conversion isn't needed
			os.Stdout.Write(val1)

			// You can get converted value
			number := row.Int(0)      // Zero value
			str    := row.Str(1)      // First value
			bignum := row.MustUint(2) // Second value

			// You may get values by column name
			first := res.Map("FirstColumn")
			second := res.Map("SecondColumn")
			val1, val2 := row.Int(first), row.Str(second)
		}
	}

If you do not want to load the entire result into memory you may use
*Start* and *GetRow* methods:

	res, err := db.Start("select * from X")
	checkError(err)

	// Print fields names
	for _, field := range res.Fields() {
		fmt.Print(field.Name, " ")
	}
	fmt.Println()

	// Print all rows
	for {
		row, err := res.GetRow()
			checkError(err)

			if row == nil {
				// No more rows
				break
			}

		// Print all cols
		for _, col := range row {
			if col == nil {
				fmt.Print("<NULL>")
			} else {
				os.Stdout.Write(col.([]byte))
			}
			fmt.Print(" ")
		}
		fmt.Println()
	}

GetRow method allocates a new chunk of memory for every received row. If your
query returns hundreds of rows you should opt for the ScanRow method to avoid
unnecessary allocations:

	// Print all rows
	row := res.MakeRow()
	for {
		err := res.ScanRow(row)
		if err == io.EOF {
			 // No more rows
			 break
		}
		checkError(err)

		// Print all cols
		// [...]
	}


### Example 2 - prepared statements

You can use *Run* or *Exec* method for prepared statements:

	stmt, err := db.Prepare("insert into X values (?, ?)")
	checkError(err)

	type Data struct {
		Id  int
		Tax *float32 // nil means NULL
	}

	data = new(Data)

	for {
		err := getData(data)
		if err == endOfData {
			 break       
		}
		checkError(err)

		_, err = stmt.Run(data.Id, data.Tax)
		checkError(err)
	}

*getData* is the function which retrieves data from somewhere and set *Id* and
*Tax* fields of the Data struct. In the case of *Tax* field *getData* may
assign a pointer the retrieved variable or nil if NULL should be stored in
database.

If you pass parameters to *Run* or *Exec* method, the data is rebound on every
method call. This isn't efficient if the statement will be executed more than once. 
You can bind parameters and use *Run* or *Exec* method without parameters, to avoid
these unnecessary rebinds. Warning! If you use *Bind* in multithreaded
applications, you should ensure that no other thread will use *Bind* for the
same statement, until you no longer need bound parameters.

The simplest way to bind parameters is:

	stmt.Bind(data.Id, data.Tax)

but you can't use it in our example, because parameters bound this way can't
be changed by *getData* function. You may modify bindings like this:

	stmt.Bind(&data.Id, &data.Tax)

and now it should work properly. But in our example there is better solution:

	stmt.Bind(data)

If *Bind* method has one parameter, and this parameter is a struct or
a pointer to the struct, it treats all fields of this struct as parameters and
binds them.

This is the improved code of the previous example:

	data = new(Data)
	stmt.Bind(data)

	for {
		err := getData(data)
		if isEndOfData(error) {
			 break       
		}
		checkError(err)

		_, err = stmt.Run()
		checkError(err)
	}

### Example 3 - using SendLongData in conjunction with http.Get

	_, err = db.Start("CREATE TABLE web (url VARCHAR(80), content LONGBLOB)")
	checkError(err)

	ins, err := db.Prepare("INSERT INTO web VALUES (?, ?)")
	checkError(err)

	var url string

	ins.Bind(&url, []byte(nil)) // []byte(nil) for properly type binding

	for  {
		// Read URL from stdin
		url = ""
		fmt.Scanln(&url)
		if len(url) == 0 {
			// Stop reading if URL is blank line
			break
		}

		// Make a connection
		resp, err := http.Get(url)
		checkError(err)

		// We can retrieve response directly into database because 
		// the resp.Body implements io.Reader. Use 8 kB buffer.
		err = ins.SendLongData(1, resp.Body, 8192)
		checkError(err)

		// Execute insert statement
		_, err = ins.Run()
		checkError(err)
	}

### Example 4 - multi statement / multi result

	res, err := db.Start("select id from M; select name from M")
	checkError(err)

	// Get result from first select
	for {
		row, err := res.GetRow()
		checkError(err)
		if row == nil {
			// End of first result
			break
		}

		// Do something with with the data
		functionThatUseId(row.Int(0))
	}

	// Get result from second select
	res, err = res.NextResult()
	checkError(err)
	if res == nil {
		panic("Hmm, there is no result. Why?!")
	}
	for {
		row, err := res.GetRow()
		checkError(err)
		if row == nil {
			// End of second result
			break
		}

		// Do something with with the data
		functionThatUseName(row.Str(0))
	}

### Example 5 - transactions

	import (
		"github.com/ziutek/mymysql/mysql"
		_ "github.com/ziutek/mymysql/thrsafe" // for thread safe transactions
	)
	// [...]

	// Statement prepared before transaction begins
	ins, err := db.Prepare("insert A values (?, ?)")
	checkError(err)

	// Begin a new transaction
	tr, err := db.Begin()
	checkError(err)

	// Now db is locked, so any method that uses db and sends commands to
	// MySQL server will be blocked until Commit or Rollback is called.

	// Commands in transaction are thread safe to
	go func() {
		_, err = tr.Start("insert A values (1, 'jeden')")
		checkError(err)
	} ()
	_, err = tr.Start("insert A values (2, 'dwa')")
	checkError(err)

	// You can't use statements prepared before transaction in the usual way,
	// because the connection is locked by the Begin method. You must bind the statement
	// to the transaction before using it.
	_, err = tr.Do(ins).Run(3, "three")
	checkError(err)
	
	// For a greater number of calls
	ti := tr.Do(ins)
	_, err = ti.Run(4, "four")
	checkError(err)
	_, err = ti.Run(5, "five")
	checkError(err)

	// At the end you can Commit or Rollback. tr is invalidated and using it
	// after Commit/Rollback will cause a panic.
	tr.Commit()

### Example 6 - autoreconn interface

	import (
		"github.com/ziutek/mymysql/autorc"
		_ "github.com/ziutek/mymysql/thrsafe" // You may also use the native engine
	)

	// [...]

	db := autorc.New("tcp", "", "127.0.0.1:3306", user, pass, dbname)

	// Initilisation commands. They will be executed after each connect.
	db.Register("set names utf8")

	// There is no need to explicity connect to the MySQL server
	rows, res, err := db.Query("SELECT * FROM R")
	checkError(err)

	// Now we are connected.

	// It does not matter if connection will be interrupted during sleep, eg
	// due to server reboot or network down.
	time.Sleep(9e9)

	// If we can reconnect in no more than db.MaxRetries attempts this
	// statement will be prepared.
	sel, err := db.Prepare("SELECT name FROM R where id > ?")
	checkError(err)

	// We can destroy our connection server side
	_, _, err = db.Query("kill %d", db.Raw.ThreadId())
	checkError(err)

	// But it doesn't matter
	sel.Bind(2)
	rows, res, err = sel.Exec()
	checkError(err)

### Example 7 - use database/sql with mymysql driver

    import (
        "database/sql"
        _"github.com/ziutek/mymysql/godrv"
    )

	// [...]

	// Open new connection. The uri need to have the following syntax:
	//
	//   [PROTOCOL_SPECFIIC*]DBNAME/USER/PASSWD
	//
	// where protocol specific part may be empty (this means connection to
	// local server using default protocol). Currently possible forms:
	//   DBNAME/USER/PASSWD
	//   unix:SOCKPATH*DBNAME/USER/PASSWD
	//   unix:SOCKPATH,OPTIONS*DBNAME/USER/PASSWD
	//   tcp:ADDR*DBNAME/USER/PASSWD
	//   tcp:ADDR,OPTIONS*DBNAME/USER/PASSWD
	//
	// OPTIONS can contain comma separated list of options in form:
	//   opt1=VAL1,opt2=VAL2,boolopt3,boolopt4
	// Currently implemented options:
	//   laddr   - local address/port (eg. 1.2.3.4:0)
	//   timeout - connect timeout in format accepted by time.ParseDuration

	// Register initialisation commands
	// (workaround, see http://codereview.appspot.com/5706047)
	godrv.Register("SET NAMES latin2") // Overrides default utf8
	godrv.Register("CREATE TABLE IF NOT EXISTS my_table ( ... )")

	// Create a connection handler
	db, err := sql.Open("mymysql", "test/testuser/TestPasswd9")
	checkErr(err)

	// For other information about database/sql see its documentation.

	ins, err := db.Prepare("INSERT my_table SET txt=?")
	checkErr(err)

	res, err := ins.Exec("some text")
	checkErr(err)

	id, err := res.LastInsertId()
	checkErr(err)

	checkErr(ins.Close(ins))

	rows, err := db.Query("SELECT * FROM go")
	checkErr(err)

	for rows.Next() {
		var id int
		var txt string
		checkErr(rows.Scan(&id, &txt))
		// Do something with id and txt
	}

	checkErr(db.Close())

### Example 8 - use stored procedures

	import (
		"github.com/ziutek/mymysql/mysql"
		_ "github.com/ziutek/mymysql/thrsafe" // or native
	)

	// [...]

	res, err := my.Start("CALL MyProcedure(1, 2, 3)")
	checkErr(err)

	// Procedure can return more than one result set so we have to read all
	// results up to the result that doesn't include result set (status only
	// result).
	for !res.StatusOnly() {
		rows, err := res.GetRows()
		checkErr(err)

		useRows(rows)		

		res, err := res.NextResult()
		checkErr(err)
		if res == nil {
			panic("nil result from procedure")
		}
	}

### Example 9 - transactions using autorc

	import (
		"github.com/ziutek/mymysql/autorc"
		_ "github.com/ziutek/mymysql/thrsafe" // You may also use the native engine
	)

	// [...]

	db := autorc.New("tcp", "", "127.0.0.1:3306", user, pass, dbname)

	var stmt1, stmt2 autorc.Stmt

	func updateDb() {
		err := db.PrepareOnce(&stmt1, someSQL1)
		checkDbErr(err)
		err = db.PrepareOnce(&stmt2, someSQL2)
		checkDbErr(err)

		err = db.Begin(func(tr mysql.Transaction, args ...interface{}) error {
			// This function will be called again if returns a recoverable error
			s1 := tr.Do(stmt1.Raw)
			s2 := tr.Do(stmt2.Raw)
			if _, err := s1.Run(); err != nil {
				return err
			}
			if _, err := s2.Run(); err != nil {
				return err
			}
			// You have to commit or rollback before return
			return tr.Commit()
		})
		checkDbErr(err)
	}

Additional examples are in *examples* directory.

## Type mapping

In the case of classic text queries, all variables that are sent to the MySQL
server are embedded in the text query. Thus you always convert them to a string and
send them embedded in an SQL query:

	rows, res, err := db.Query("select * from X where id > %d", id)

After text query you always receive a text result. Mysql text result
corresponds to *[]byte* type in mymysql. It isn't *string* type due to
avoidance of unnecessary type conversions. You can always convert *[]byte* to
*string* yourself:

	fmt.Print(string(rows[0][1].([]byte)))

or using *Str* helper method:

	fmt.Print(rows[0].Str(1))

There are other helper methods for data conversion like *Int* or *Uint*:

	fmt.Print(rows[0].Int(1))

All three above examples return value received in row 0 column 1. If you prefer
to use the column names, you can use *res.Map* which maps result field names to
corresponding indexes:

	name := res.Map("name")
	fmt.Print(rows[0].Str(name))

In case of prepared statements, the type mapping is slightly more complicated.
For parameters sent from the client to the server, Go/mymysql types are
mapped for MySQL protocol types as below:

	         string  -->  MYSQL_TYPE_STRING
	         []byte  -->  MYSQL_TYPE_VAR_STRING
	    int8, uint8  -->  MYSQL_TYPE_TINY
	  int16, uint16  -->  MYSQL_TYPE_SHORT
	  int32, uint32  -->  MYSQL_TYPE_LONG
	  int64, uint64  -->  MYSQL_TYPE_LONGLONG
	      int, uint  -->  protocol integer type which match size of int
	           bool  -->  MYSQL_TYPE_TINY
	        float32  -->  MYSQL_TYPE_FLOAT
	        float64  -->  MYSQL_TYPE_DOUBLE
	      time.Time  -->  MYSQL_TYPE_DATETIME
	mysql.Timestamp  -->  MYSQL_TYPE_TIMESTAMP
	     mysql.Date  -->  MYSQL_TYPE_DATE
	  time.Duration  -->  MYSQL_TYPE_TIME
	     mysql.Blob  -->  MYSQL_TYPE_BLOB
	            nil  -->  MYSQL_TYPE_NULL

The MySQL server maps/converts them to a particular MySQL storage type.

For received results MySQL storage types are mapped to Go/mymysql types as
below:

	                             TINYINT  -->  int8
	                    UNSIGNED TINYINT  -->  uint8
	                            SMALLINT  -->  int16
	                   UNSIGNED SMALLINT  -->  uint16
	                      MEDIUMINT, INT  -->  int32
	    UNSIGNED MEDIUMINT, UNSIGNED INT  -->  uint32
	                              BIGINT  -->  int64
	                     UNSIGNED BIGINT  -->  uint64
	                               FLOAT  -->  float32
	                              DOUBLE  -->  float64
	                             DECIMAL  -->  float64
	                 TIMESTAMP, DATETIME  -->  time.Time
	                                DATE  -->  mysql.Date
	                                TIME  -->  time.Duration
	                                YEAR  -->  int16
	    CHAR, VARCHAR, BINARY, VARBINARY  -->  []byte
	 TEXT, TINYTEXT, MEDIUMTEXT, LONGTEX  -->  []byte
	BLOB, TINYBLOB, MEDIUMBLOB, LONGBLOB  -->  []byte
	                                 BIT  -->  []byte
	                           SET, ENUM  -->  []byte
	                                NULL  -->  nil

## Big packets

This package can send and receive MySQL data packets that are biger than 16 MB.
This means that you can receive response rows biger than 16 MB and can execute
prepared statements with parameter data bigger than 16 MB without using
SendLongData method. If you want to use this feature you need to change the default
mymysql setting using the *Conn.SetMaxPktSize* method and change
*max_allowed_packet* value in your MySQL server configuration.

## Thread safe engine

If you import "mymysql/thrsafe" engine instead of "mymysql/native" engine all
methods are thread safe, unless the description of the method says something else.

If one thread is calling *Query* or *Exec* method, other threads will be
blocked if they call *Query*, *Start*, *Exec*, *Run* or other method which send
data to the server, until *Query*/*Exec* return in first thread.

If one thread is calling *Start* or *Run* method, other threads will be
blocked if they call *Query*, *Start*, *Exec*, *Run* or other method which send
data to the server,  until all results and all rows  will be readed from
the connection in first thread.

In most of my web applications I use the *autorecon* interface with *thrsafe* engine.
For any new connection, one gorutine is created. There is one persistant
connection to MySQL server shared by all gorutines. Applications are usually
running on dual-core machines with GOMAXPROCS=2. I use *siege* to test any
application befor put it into production. There is example output from siege:

	# siege my.httpserver.pl -c25 -d0 -t 30s
	** SIEGE 2.69
	** Preparing 25 concurrent users for battle.
    The server is now under siege...
	Lifting the server siege..      done.
    Transactions:                   3212 hits
    Availability:                 100.00 %
    Elapsed time:                  29.83 secs
	Data transferred:               3.88 MB
	Response time:                  0.22 secs
	Transaction rate:             107.68 trans/sec
	Throughput:	                    0.13 MB/sec
	Concurrency:                   23.43
	Successful transactions:        3218
	Failed transactions:               0
	Longest transaction:            9.28
	Shortest transaction:           0.01

## To do

1. Complete documentation

## Known bugs

1. There is MySQL "bug" in the *SUM* function. If you use prepared statements
*SUM* returns *DECIMAL* value, even if you sum integer column. mymysql returns
decimals as *float64* so cast result from sum to integer (or use *Row.Int*)
causes panic.

# Documentation

[mysql](http://godoc.org/pkg/github.com/ziutek/mymysql/mysql)
[native](http://godoc.org/pkg/github.com/ziutek/mymysql/native)
[thrsafe](http://godoc.org/pkg/github.com/ziutek/mymysql/thrsafe)
[autorc](http://godoc.org/pkg/github.com/ziutek/mymysql/autorc)
[godrv](http://godoc.org/pkg/github.com/ziutek/mymysql/godrv)
