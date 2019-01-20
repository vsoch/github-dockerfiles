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
# Objx
[![Build Status](https://travis-ci.org/stretchr/objx.svg?branch=master)](https://travis-ci.org/stretchr/objx)
[![Go Report Card](https://goreportcard.com/badge/github.com/stretchr/objx)](https://goreportcard.com/report/github.com/stretchr/objx)
[![Maintainability](https://api.codeclimate.com/v1/badges/1d64bc6c8474c2074f2b/maintainability)](https://codeclimate.com/github/stretchr/objx/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1d64bc6c8474c2074f2b/test_coverage)](https://codeclimate.com/github/stretchr/objx/test_coverage)
[![Sourcegraph](https://sourcegraph.com/github.com/stretchr/objx/-/badge.svg)](https://sourcegraph.com/github.com/stretchr/objx)
[![GoDoc](https://godoc.org/github.com/stretchr/objx?status.svg)](https://godoc.org/github.com/stretchr/objx)

Objx - Go package for dealing with maps, slices, JSON and other data.

Get started:

- Install Objx with [one line of code](#installation), or [update it with another](#staying-up-to-date)
- Check out the API Documentation http://godoc.org/github.com/stretchr/objx

## Overview
Objx provides the `objx.Map` type, which is a `map[string]interface{}` that exposes a powerful `Get` method (among others) that allows you to easily and quickly get access to data within the map, without having to worry too much about type assertions, missing data, default values etc.

### Pattern
Objx uses a preditable pattern to make access data from within `map[string]interface{}` easy. Call one of the `objx.` functions to create your `objx.Map` to get going:

    m, err := objx.FromJSON(json)

NOTE: Any methods or functions with the `Must` prefix will panic if something goes wrong, the rest will be optimistic and try to figure things out without panicking.

Use `Get` to access the value you're interested in.  You can use dot and array
notation too:

     m.Get("places[0].latlng")

Once you have sought the `Value` you're interested in, you can use the `Is*` methods to determine its type.

     if m.Get("code").IsStr() { // Your code... }

Or you can just assume the type, and use one of the strong type methods to extract the real value:

    m.Get("code").Int()

If there's no value there (or if it's the wrong type) then a default value will be returned, or you can be explicit about the default value.

     Get("code").Int(-1)

If you're dealing with a slice of data as a value, Objx provides many useful methods for iterating, manipulating and selecting that data.  You can find out more by exploring the index below.

### Reading data
A simple example of how to use Objx:

    // Use MustFromJSON to make an objx.Map from some JSON
    m := objx.MustFromJSON(`{"name": "Mat", "age": 30}`)

    // Get the details
    name := m.Get("name").Str()
    age := m.Get("age").Int()

    // Get their nickname (or use their name if they don't have one)
    nickname := m.Get("nickname").Str(name)

### Ranging
Since `objx.Map` is a `map[string]interface{}` you can treat it as such.  For example, to `range` the data, do what you would expect:

    m := objx.MustFromJSON(json)
    for key, value := range m {
      // Your code...
    }

## Installation
To install Objx, use go get:

    go get github.com/stretchr/objx

### Staying up to date
To update Objx to the latest version, run:

    go get -u github.com/stretchr/objx

### Supported go versions
We support the lastest three major Go versions, which are 1.8, 1.9 and 1.10 at the moment.

## Contributing
Please feel free to submit issues, fork the repository and send pull requests!
# Go Meta Linter
[![Build Status](https://travis-ci.org/alecthomas/gometalinter.svg)](https://travis-ci.org/alecthomas/gometalinter) [![Gitter chat](https://badges.gitter.im/alecthomas.svg)](https://gitter.im/alecthomas/Lobby)

<!-- MarkdownTOC -->

- [Installing](#installing)
- [Editor integration](#editor-integration)
- [Supported linters](#supported-linters)
- [Configuration file](#configuration-file)
    - [`Format` key](#format-key)
    - [Format Methods](#format-methods)
  - [Adding Custom linters](#adding-custom-linters)
- [Comment directives](#comment-directives)
- [Quickstart](#quickstart)
- [FAQ](#faq)
  - [Exit status](#exit-status)
  - [What's the best way to use `gometalinter` in CI?](#whats-the-best-way-to-use-gometalinter-in-ci)
  - [How do I make `gometalinter` work with Go 1.5 vendoring?](#how-do-i-make-gometalinter-work-with-go-15-vendoring)
  - [Why does `gometalinter --install` install a fork of gocyclo?](#why-does-gometalinter---install-install-a-fork-of-gocyclo)
  - [Many unexpected errors are being reported](#many-unexpected-errors-are-being-reported)
  - [Gometalinter is not working](#gometalinter-is-not-working)
    - [1. Update to the latest build of gometalinter and all linters](#1-update-to-the-latest-build-of-gometalinter-and-all-linters)
    - [2. Analyse the debug output](#2-analyse-the-debug-output)
    - [3. Report an issue.](#3-report-an-issue)
  - [How do I filter issues between two git refs?](#how-do-i-filter-issues-between-two-git-refs)
- [Checkstyle XML format](#checkstyle-xml-format)

<!-- /MarkdownTOC -->


The number of tools for statically checking Go source for errors and warnings
is impressive.

This is a tool that concurrently runs a whole bunch of those linters and
normalises their output to a standard format:

    <file>:<line>:[<column>]: <message> (<linter>)

eg.

    stutter.go:9::warning: unused global variable unusedGlobal (varcheck)
    stutter.go:12:6:warning: exported type MyStruct should have comment or be unexported (golint)

It is intended for use with editor/IDE integration.

## Installing

There are two options for installing gometalinter.

1. Install a stable version, eg. `go get -u gopkg.in/alecthomas/gometalinter.v2`.
   I will generally only tag a new stable version when it has passed the Travis
  regression tests. The downside is that the binary will be called `gometalinter.v2`.
2. Install from HEAD with: `go get -u github.com/alecthomas/gometalinter`.
   This has the downside that changes to gometalinter may break.

## Editor integration

- [SublimeLinter plugin](https://github.com/alecthomas/SublimeLinter-contrib-gometalinter).
- [Atom go-plus package](https://atom.io/packages/go-plus).
- [Emacs Flycheck checker](https://github.com/favadi/flycheck-gometalinter).
- [Go for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=lukehoban.Go).
- Vim/Neovim
    - [Neomake](https://github.com/neomake/neomake).
    - [Syntastic](https://github.com/scrooloose/syntastic/wiki/Go:---gometalinter) `let g:syntastic_go_checkers = ['gometalinter']`.
    - [ale](https://github.com/w0rp/ale) `let g:ale_linters = {'go': ['gometalinter']}`
    - [vim-go](https://github.com/fatih/vim-go) with the `:GoMetaLinter` command.

## Supported linters

- [go vet](https://golang.org/cmd/vet/) - Reports potential errors that otherwise compile.
- [go tool vet --shadow](https://golang.org/cmd/vet/#hdr-Shadowed_variables) - Reports variables that may have been unintentionally shadowed.
- [gotype](https://golang.org/x/tools/cmd/gotype) - Syntactic and semantic analysis similar to the Go compiler.
- [gotype -x](https://golang.org/x/tools/cmd/gotype) - Syntactic and semantic analysis in external test packages (similar to the Go compiler).
- [deadcode](https://github.com/tsenart/deadcode) - Finds unused code.
- [gocyclo](https://github.com/alecthomas/gocyclo) - Computes the cyclomatic complexity of functions.
- [golint](https://github.com/golang/lint) - Google's (mostly stylistic) linter.
- [varcheck](https://github.com/opennota/check) - Find unused global variables and constants.
- [structcheck](https://github.com/opennota/check) - Find unused struct fields.
- [maligned](https://github.com/mdempsky/maligned) -  Detect structs that would take less memory if their fields were sorted.
- [errcheck](https://github.com/kisielk/errcheck) - Check that error return values are used.
- [megacheck](https://github.com/dominikh/go-tools/tree/master/cmd/megacheck) - Run staticcheck, gosimple and unused, sharing work.
- [dupl](https://github.com/mibk/dupl) - Reports potentially duplicated code.
- [ineffassign](https://github.com/gordonklaus/ineffassign) - Detect when assignments to *existing* variables are not used.
- [interfacer](https://github.com/mvdan/interfacer) - Suggest narrower interfaces that can be used.
- [unconvert](https://github.com/mdempsky/unconvert) - Detect redundant type conversions.
- [goconst](https://github.com/jgautheron/goconst) - Finds repeated strings that could be replaced by a constant.
- [gosec](https://github.com/securego/gosec) - Inspects source code for security problems by scanning the Go AST.

Disabled by default (enable with `--enable=<linter>`):

- [testify](https://github.com/stretchr/testify) - Show location of failed testify assertions.
- [test](http://golang.org/pkg/testing/) - Show location of test failures from the stdlib testing module.
- [gofmt -s](https://golang.org/cmd/gofmt/) - Checks if the code is properly formatted and could not be further simplified.
- [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) - Checks missing or unreferenced package imports.
- [gosimple](https://github.com/dominikh/go-tools/tree/master/cmd/gosimple) - Report simplifications in code.
- [gochecknoinits](https://4d63.com/gochecknoinits) - Report init functions, to reduce side effects in code.
- [gochecknoglobals](https://4d63.com/gochecknoglobals) - Report global vars, to reduce side effects in code.
- [lll](https://github.com/walle/lll) - Report long lines (see `--line-length=N`).
- [misspell](https://github.com/client9/misspell) - Finds commonly misspelled English words.
- [nakedret](https://github.com/alexkohler/nakedret) - Finds naked returns.
- [unparam](https://github.com/mvdan/unparam) - Find unused function parameters.
- [unused](https://github.com/dominikh/go-tools/tree/master/cmd/unused) - Find unused variables.
- [safesql](https://github.com/stripe/safesql) - Finds potential SQL injection vulnerabilities.
- [staticcheck](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck) - Statically detect bugs, both obvious and subtle ones.

Additional linters can be added through the command line with `--linter=NAME:COMMAND:PATTERN` (see [below](#details)).

## Configuration file

gometalinter now supports a JSON configuration file called `.gometalinter.json` that can
be placed at the root of your project. The configuration file will be automatically loaded
from the working directory or any parent directory and can be overridden by passing
`--config=<file>` or ignored with `--no-config`. The format of this file is determined by
the `Config` struct in [config.go](https://github.com/alecthomas/gometalinter/blob/master/config.go).

The configuration file mostly corresponds to command-line flags, with the following exceptions:

- Linters defined in the configuration file will overlay existing definitions, not replace them.
- "Enable" defines the exact set of linters that will be enabled (default
  linters are disabled). `--help` displays the list of default linters with the exact names
  you must use.

Here is an example configuration file:

```json
{
  "Enable": ["deadcode", "unconvert"]
}
```

If a `.gometalinter.json` file is loaded, individual options can still be overridden by
passing command-line flags. All flags are parsed in order, meaning configuration passed
with the `--config` flag will override any command-line flags passed before and be
overridden by flags passed after.


#### `Format` key

The default `Format` key places the different fields of an `Issue` into a template. this
corresponds to the `--format` option command-line flag.

Default `Format`:
```
Format: "{{.Path}}:{{.Line}}:{{if .Col}}{{.Col}}{{end}}:{{.Severity}}: {{.Message}} ({{.Linter}})"
```

#### Format Methods

* `{{.Path.Relative}}` - equivalent to `{{.Path}}` which outputs a relative path to the file
* `{{.Path.Abs}}` - outputs an absolute path to the file

### Adding Custom linters

Linters can be added and customized from the config file using the `Linters` field.
Linters supports the following fields:

* `Command` - the path to the linter binary and any default arguments
* `Pattern` - a regular expression used to parse the linter output
* `IsFast` - if the linter should be run when the `--fast` flag is used
* `PartitionStrategy` - how paths args should be passed to the linter command:
  * `directories` - call the linter once with a list of all the directories
  * `files` - call the linter once with a list of all the files
  * `packages` - call the linter once with a list of all the package paths
  * `files-by-package` - call the linter once per package with a list of the
    files in the package.
  * `single-directory` - call the linter once per directory

The config for default linters can be overridden by using the name of the
linter.

Additional linters can be configured via the command line using the format
`NAME:COMMAND:PATTERN`.

Example:

```
$ gometalinter --linter='vet:go tool vet -printfuncs=Infof,Debugf,Warningf,Errorf:PATH:LINE:MESSAGE' .
```

## Comment directives

gometalinter supports suppression of linter messages via comment directives. The
form of the directive is:

```
// nolint[: <linter>[, <linter>, ...]]
```

Suppression works in the following way:

1. Line-level suppression

    A comment directive suppresses any linter messages on that line.

    eg. In this example any messages for `a := 10` will be suppressed and errcheck
    messages for `defer r.Close()` will also be suppressed.

    ```go
    a := 10 // nolint
    a = 2
    defer r.Close() // nolint: errcheck
    ```

2. Statement-level suppression

    A comment directive at the same indentation level as a statement it
    immediately precedes will also suppress any linter messages in that entire
    statement.

    eg. In this example all messages for `SomeFunc()` will be suppressed.

    ```go
    // nolint
    func SomeFunc() {
    }
    ```

Implementation details: gometalinter now performs parsing of Go source code,
to extract linter directives and associate them with line ranges. To avoid
unnecessary processing, parsing is on-demand: the first time a linter emits a
message for a file, that file is parsed for directives.

## Quickstart

Install gometalinter (see above).

Install all known linters:

```
$ gometalinter --install
Installing:
  structcheck
  maligned
  nakedret
  deadcode
  gocyclo
  ineffassign
  dupl
  golint
  gotype
  goimports
  errcheck
  varcheck
  interfacer
  goconst
  gosimple
  staticcheck
  unparam
  unused
  misspell
  lll
  gosec
  safesql
```

Run it:

```
$ cd example
$ gometalinter ./...
stutter.go:13::warning: unused struct field MyStruct.Unused (structcheck)
stutter.go:9::warning: unused global variable unusedGlobal (varcheck)
stutter.go:12:6:warning: exported type MyStruct should have comment or be unexported (golint)
stutter.go:16:6:warning: exported type PublicUndocumented should have comment or be unexported (golint)
stutter.go:8:1:warning: unusedGlobal is unused (deadcode)
stutter.go:12:1:warning: MyStruct is unused (deadcode)
stutter.go:16:1:warning: PublicUndocumented is unused (deadcode)
stutter.go:20:1:warning: duplicateDefer is unused (deadcode)
stutter.go:21:15:warning: error return value not checked (defer a.Close()) (errcheck)
stutter.go:22:15:warning: error return value not checked (defer a.Close()) (errcheck)
stutter.go:27:6:warning: error return value not checked (doit()           // test for errcheck) (errcheck)
stutter.go:29::error: unreachable code (vet)
stutter.go:26::error: missing argument for Printf("%d"): format reads arg 1, have only 0 args (vet)
```


Gometalinter also supports the commonly seen `<path>/...` recursive path
format. Note that this can be *very* slow, and you may need to increase the linter `--deadline` to allow linters to complete.

## FAQ

### Exit status

gometalinter sets two bits of the exit status to indicate different issues:

| Bit | Meaning
|-----|----------
| 0   | A linter generated an issue.
| 1   | An underlying error occurred; eg. a linter failed to execute. In this situation a warning will also be displayed.

eg. linter only = 1, underlying only = 2, linter + underlying = 3

### What's the best way to use `gometalinter` in CI?

There are two main problems running in a CI:

1. <s>Linters break, causing `gometalinter --install --update` to error</s> (this is no longer an issue as all linters are vendored).
2. `gometalinter` adds a new linter.

I have solved 1 by vendoring the linters.

For 2, the best option is to disable all linters, then explicitly enable the
ones you want:

    gometalinter --disable-all --enable=errcheck --enable=vet --enable=vetshadow ...

### How do I make `gometalinter` work with Go 1.5 vendoring?

`gometalinter` has a `--vendor` flag that just sets `GO15VENDOREXPERIMENT=1`, however the
underlying tools must support it. Ensure that all of the linters are up to date and built with Go 1.5
(`gometalinter --install --force`) then run `gometalinter --vendor .`. That should be it.

### Why does `gometalinter --install` install a fork of gocyclo?

I forked `gocyclo` because the upstream behaviour is to recursively check all
subdirectories even when just a single directory is specified. This made it
unusably slow when vendoring. The recursive behaviour can be achieved with
gometalinter by explicitly specifying `<path>/...`. There is a
[pull request](https://github.com/fzipp/gocyclo/pull/1) open.

### Many unexpected errors are being reported

If you see a whole bunch of errors being reported that you wouldn't expect,
such as compile errors, this typically means that something is wrong with your
Go environment. Try `go install` and fix any issues with your go installation,
then try gometalinter again.

### Gometalinter is not working

That's more of a statement than a question, but okay.

Sometimes gometalinter will not report issues that you think it should. There
are three things to try in that case:

#### 1. Update to the latest build of gometalinter and all linters

    go get -u github.com/alecthomas/gometalinter
    gometalinter --install

If you're lucky, this will fix the problem.

#### 2. Analyse the debug output

If that doesn't help, the problem may be elsewhere (in no particular order):

1. Upstream linter has changed its output or semantics.
2. gometalinter is not invoking the tool correctly.
3. gometalinter regular expression matches are not correct for a linter.
4. Linter is exceeding the deadline.

To find out what's going on run in debug mode:

    gometalinter --debug

This will show all output from the linters and should indicate why it is
failing.

#### 3. Report an issue.

Failing all else, if the problem looks like a bug please file an issue and
include the output of `gometalinter --debug`.

### How do I filter issues between two git refs?

[revgrep](https://github.com/bradleyfalzon/revgrep) can be used to filter the output of `gometalinter`
to show issues on lines that have changed between two git refs, such as unstaged changes, changes in
`HEAD` vs `master` and between `master` and `origin/master`. See the project's documentation and `-help`
usage for more information.

```
go get -u github.com/bradleyfalzon/revgrep/...
gometalinter |& revgrep               # If unstaged changes or untracked files, those issues are shown.
gometalinter |& revgrep               # Else show issues in the last commit.
gometalinter |& revgrep master        # Show issues between master and HEAD (or any other reference).
gometalinter |& revgrep origin/master # Show issues that haven't been pushed.
```

## Checkstyle XML format

`gometalinter` supports [checkstyle](http://checkstyle.sourceforge.net/)
compatible XML output format. It is triggered with `--checkstyle` flag:

	gometalinter --checkstyle

Checkstyle format can be used to integrate gometalinter with Jenkins CI with the
help of [Checkstyle Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Checkstyle+Plugin).


## gosec -Golang Security Checker

Inspects source code for security problems by scanning the Go AST.

### License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License [here](http://www.apache.org/licenses/LICENSE-2.0).

### Project status

[![Build Status](https://travis-ci.org/securego/gosec.svg?branch=master)](https://travis-ci.org/securego/gosec)
[![GoDoc](https://godoc.org/github.com/securego/gosec?status.svg)](https://godoc.org/github.com/securego/gosec)
[![Slack](http://securego.herokuapp.com/badge.svg)](http://securego.herokuapp.com)


### Install

`$ go get github.com/securego/gosec/cmd/gosec/...`

### Usage

Gosec can be configured to only run a subset of rules, to exclude certain file
paths, and produce reports in different formats. By default all rules will be
run against the supplied input files. To recursively scan from the current
directory you can supply './...' as the input argument.

#### Selecting rules

By default gosec will run all rules against the supplied file paths. It is however possible to select a subset of rules to run via the '-include=' flag,
or to specify a set of rules to explicitly exclude using the '-exclude=' flag.

##### Available rules

  - G101: Look for hardcoded credentials
  - G102: Bind to all interfaces
  - G103: Audit the use of unsafe block
  - G104: Audit errors not checked
  - G105: Audit the use of math/big.Int.Exp
  - G106: Audit the use of ssh.InsecureIgnoreHostKey
  - G201: SQL query construction using format string
  - G202: SQL query construction using string concatenation
  - G203: Use of unescaped data in HTML templates
  - G204: Audit use of command execution
  - G301: Poor file permissions used when creating a directory
  - G302: Poor file permisions used with chmod
  - G303: Creating tempfile using a predictable path
  - G304: File path provided as taint input
  - G305: File traversal when extracting zip archive
  - G401: Detect the usage of DES, RC4, or MD5
  - G402: Look for bad TLS connection settings
  - G403: Ensure minimum RSA key length of 2048 bits
  - G404: Insecure random number source (rand)
  - G501: Import blacklist: crypto/md5
  - G502: Import blacklist: crypto/des
  - G503: Import blacklist: crypto/rc4
  - G504: Import blacklist: net/http/cgi


```
# Run a specific set of rules
$ gosec -include=G101,G203,G401 ./...

# Run everything except for rule G303
$ gosec -exclude=G303 ./...
```

#### Excluding files:

gosec will ignore dependencies in your vendor directory any files
that are not considered build artifacts by the compiler (so test files).

#### Annotating code

As with all automated detection tools there will be cases of false positives. In cases where gosec reports a failure that has been manually verified as being safe it is possible to annotate the code with a '#nosec' comment.

The annotation causes gosec to stop processing any further nodes within the
AST so can apply to a whole block or more granularly to a single expression. 

```go

import "md5" // #nosec


func main(){

    /* #nosec */
    if x > y {
        h := md5.New() // this will also be ignored
    }

}

```

When a specific false positive has been identified and verified as safe, you may wish to suppress only that single rule (or a specific set of rules) within a section of code, while continuing to scan for other problems. To do this, you can list the rule(s) to be suppressed within the `#nosec` annotation, e.g: `/* #nosec G401 */` or `// #nosec G201 G202 G203 `

In some cases you may also want to revisit places where #nosec annotations
have been used. To run the scanner and ignore any #nosec annotations you
can do the following:

```
$ gosec -nosec=true ./...
```
#### Build tags

gosec is able to pass your [Go build tags](https://golang.org/pkg/go/build/) to the analyzer.
They can be provided as a comma separated list as follows:

```
$ gosec -tag debug,ignore ./...
```

### Output formats

gosec currently supports text, json, yaml, csv and JUnit XML output formats. By default
results will be reported to stdout, but can also be written to an output
file. The output format is controlled by the '-fmt' flag, and the output file is controlled by the '-out' flag as follows:

```
# Write output in json format to results.json
$ gosec -fmt=json -out=results.json *.go
```
### Development

#### Prerequisites

Install dep according to the instructions here: https://github.com/golang/dep
Install the latest version of golint: https://github.com/golang/lint

#### Build

```
make
```

#### Tests

```
make test
```

#### Release Build

Make sure you have installed the [goreleaser](https://github.com/goreleaser/goreleaser) tool and then you can release gosec as follows:
git tag 1.0.0
export GITHUB_TOKEN=<YOUR GITHUB TOKEN>
make release

The released version of the tool is available in the `dist` folder. The build information should be displayed in the usage text.

```
./dist/darwin_amd64/gosec -h
gosec  - Golang security checker

gosec analyzes Go source code to look for common programming mistakes that
can lead to security problems.

VERSION: 1.0.0
GIT TAG: 1.0.0
BUILD DATE: 2018-04-27T12:41:38Z
```

Note that all released archives are also uploaded to GitHub.

#### Docker image

You can execute a release and build the docker image as follows:

```
git tag <VERSION>
export GITHUB_TOKEN=<Your GitHub token>
make image
```

Now you can run the gosec tool in a container against your local workspace:

```
docker run -it -v <YOUR LOCAL WORKSPACE>:/workspace gosec /workspace
```

#### Generate TLS rule

The configuration of TLS rule can be generated from [Mozilla's TLS ciphers recommendation](https://statics.tls.security.mozilla.org/server-side-tls-conf.json).


First you need to install the generator tool:

```
go get github.com/securego/gosec/cmd/tlsconfig/...
```

You can invoke now the `go generate` in the root of the project:

```
go generate ./...
```

This will generate the `rules/tls_config.go` file with will contain the current ciphers recommendation from Mozilla.
