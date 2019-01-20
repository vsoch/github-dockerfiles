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
# String globbing in golang [![Build Status](https://travis-ci.org/ryanuber/go-glob.svg)](https://travis-ci.org/ryanuber/go-glob)

`go-glob` is a single-function library implementing basic string glob support.

Globs are an extremely user-friendly way of supporting string matching without
requiring knowledge of regular expressions or Go's particular regex engine. Most
people understand that if you put a `*` character somewhere in a string, it is
treated as a wildcard. Surprisingly, this functionality isn't found in Go's
standard library, except for `path.Match`, which is intended to be used while
comparing paths (not arbitrary strings), and contains specialized logic for this
use case. A better solution might be a POSIX basic (non-ERE) regular expression
engine for Go, which doesn't exist currently.

Example
=======

```
package main

import "github.com/ryanuber/go-glob"

func main() {
    glob.Glob("*World!", "Hello, World!") // true
    glob.Glob("Hello,*", "Hello, World!") // true
    glob.Glob("*ello,*", "Hello, World!") // true
    glob.Glob("World!", "Hello, World!")  // false
    glob.Glob("/home/*", "/home/ryanuber/.bashrc") // true
}
```
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
# rootcerts

Functions for loading root certificates for TLS connections.

-----

Go's standard library `crypto/tls` provides a common mechanism for configuring
TLS connections in `tls.Config`. The `RootCAs` field on this struct is a pool
of certificates for the client to use as a trust store when verifying server
certificates.

This library contains utility functions for loading certificates destined for
that field, as well as one other important thing:

When the `RootCAs` field is `nil`, the standard library attempts to load the
host's root CA set.  This behavior is OS-specific, and the Darwin
implementation contains [a bug that prevents trusted certificates from the
System and Login keychains from being loaded][1]. This library contains
Darwin-specific behavior that works around that bug.

[1]: https://github.com/golang/go/issues/14514

## Example Usage

Here's a snippet demonstrating how this library is meant to be used:

```go
func httpClient() (*http.Client, error)
	tlsConfig := &tls.Config{}
	err := rootcerts.ConfigureTLS(tlsConfig, &rootcerts.Config{
		CAFile: os.Getenv("MYAPP_CAFILE"),
		CAPath: os.Getenv("MYAPP_CAPATH"),
	})
	if err != nil {
		return nil, err
	}
	c := cleanhttp.DefaultClient()
	t := cleanhttp.DefaultTransport()
	t.TLSClientConfig = tlsConfig
	c.Transport = t
	return c, nil
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
This would be equivalent to the following json:
``` json
{
  "variable": {
      "ami": {
          "description": "the AMI to use"
        }
    }
}
```

## Thanks

Thanks to:

  * [@vstakhov](https://github.com/vstakhov) - The original libucl parser
    and syntax that HCL was based off of.

  * [@fatih](https://github.com/fatih) - The rewritten HCL parser
    in pure Go (no goyacc) and support for a printer.
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
response code is received (except 501), then a retry is invoked after a wait
period.  Otherwise, the response is returned and left to the caller to
interpret.

The main difference from `net/http` is that requests which take a request body
(POST/PUT et. al) can have the body provided in a number of ways (some more or
less efficient) that allow "rewinding" the request body if the initial request
fails so that the full request can be attempted again. See the
[godoc](http://godoc.org/github.com/hashicorp/go-retryablehttp) for more
details.

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
cli
===

[![Build Status](https://travis-ci.org/urfave/cli.svg?branch=master)](https://travis-ci.org/urfave/cli)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/rtgk5xufi932pb2v?svg=true)](https://ci.appveyor.com/project/urfave/cli)
[![GoDoc](https://godoc.org/github.com/urfave/cli?status.svg)](https://godoc.org/github.com/urfave/cli)
[![codebeat](https://codebeat.co/badges/0a8f30aa-f975-404b-b878-5fab3ae1cc5f)](https://codebeat.co/projects/github-com-urfave-cli)
[![Go Report Card](https://goreportcard.com/badge/urfave/cli)](https://goreportcard.com/report/urfave/cli)
[![top level coverage](https://gocover.io/_badge/github.com/urfave/cli?0 "top level coverage")](http://gocover.io/github.com/urfave/cli) /
[![altsrc coverage](https://gocover.io/_badge/github.com/urfave/cli/altsrc?0 "altsrc coverage")](http://gocover.io/github.com/urfave/cli/altsrc)

**Notice:** This is the library formerly known as
`github.com/codegangsta/cli` -- Github will automatically redirect requests
to this repository, but we recommend updating your references for clarity.

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
    + [Values from alternate input sources (YAML, TOML, and others)](#values-from-alternate-input-sources-yaml-toml-and-others)
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
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.NewApp().Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Action = func(c *cli.Context) error {
    fmt.Printf("Hello %q", c.Args().Get(0))
    return nil
  }

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
}
```

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

Currently only the aboved specified formats are supported but developers can
add support for other input sources by implementing the
altsrc.InputSourceContext for their given sources.

Here is a more complete sample of a command using YAML support:

<!-- {
  "args": ["test-cmd", "&#45;&#45;help"],
  "output": "&#45&#45;test value.*default: 0"
} -->
``` go
package notmain

import (
  "fmt"
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

  app.Run(os.Args)
}
```

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

  app.Run(os.Args)
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
      Category: "template",
    },
    {
      Name:     "remove",
      Category: "template",
    },
  }

  app.Run(os.Args)
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

  app.Run(os.Args)
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

  app.Run(os.Args)
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
  app.Run(os.Args)
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

  cli.NewApp().Run(os.Args)
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
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.HelpFlag = cli.BoolFlag{
    Name: "halp, haaaaalp",
    Usage: "HALP",
    EnvVar: "SHOW_HALP,HALPPLZ",
  }

  cli.NewApp().Run(os.Args)
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
  app.Run(os.Args)
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
  app.Run(os.Args)
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
    return ec
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

  app.Run(os.Args)
}

func wopAction(c *cli.Context) error {
  fmt.Fprintf(c.App.Writer, ":wave: over here, eh\n")
  return nil
}
```

## Contribution Guidelines

Feel free to put up a pull request to fix a bug or maybe add a feature. I will
give it a code review and make sure that it does not break backwards
compatibility. If I or any other collaborators agree that it is in line with
the vision of the project, we will work with you to get the code into
a mergeable state and merge it into the master branch.

If you have contributed something significant to the project, we will most
likely add you as a collaborator. As a collaborator you are given the ability
to merge others pull requests. It is very important that new code does not
break existing code, so be careful about what code you do choose to merge.

If you feel like you have contributed to the project but have not yet been
added as a collaborator, we probably forgot to add you, please open an issue.
## Terrahelp examples 

* [encryption / decryption](https://github.com/opencredo/terrahelp/tree/master/examples/tfstate-encrypt) 
* [masking](https://github.com/opencredo/terrahelp/tree/master/examples/mask)
 
## Terrahelp example - masking sensitive data 

This example contains a very simple terraform setup composed entirely of local resources (e.g. template resource) and exists in order to demonstrate how you can do masking of sensitive data which may be output from varius terraform commands.
 
This example is completely safe to run and will not land up costing you any money in a cloud provider! It currently demonstrates a terraform 0.7.7 based setup which includes the new lists and maps functionality.
 
The CLI itself offers a more comprehensive view of the various options available, so please use this if you need more info.

### Simple inline masking of terraform output

This example will demonstrate how you can use the `mask` command in order to mask sensitive data which may be exposed when performing terraform actions.

* Run a `terraform plan` as normal

        terraform plan
        
* Inspect the result which should look something like below:        
        
        Refreshing Terraform state in-memory prior to plan...
        The refreshed state will be used to calculate this plan, but
        will not be persisted to local or remote state storage.
        
        ...
        
        <= data.template_file.example
            rendered:  "<computed>"
            template:  "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}\nmsg4 = ${msg4}\nmsg5 = ${msg5}\nmsg6 = ${msg6}\nmsg7 = ${msg7}"
            vars.%:    "7"
            vars.msg1: "sensitive-value-1-AK#%DJGHS*G"
            vars.msg2: "normal value 1"
            vars.msg3: "sensitive-value-3-//dfhs//"
            vars.msg4: "sensitive-value-4 with equals sign i.e. ff=yy"
            vars.msg5: "sensitive-list-val-1"
            vars.msg6: "sensitive-flatmap-val-foo"
            vars.msg7: "sensitive-flatmap-val"
        
        
        Plan: 0 to add, 0 to change, 0 to destroy.
                


* Run the same command, but pipe the output through the `terrahelp mask` command. 

        terraform plan | terrahelp mask  

* The result should now look something like below:

        Refreshing Terraform state in-memory prior to plan...
        The refreshed state will be used to calculate this plan, but
        will not be persisted to local or remote state storage.
        
        ...
        
        <= data.template_file.example
            rendered:  "<computed>"
            template:  "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}\nmsg4 = ${msg4}\nmsg5 = ${msg5}\nmsg6 = ${msg6}\nmsg7 = ${msg7}"
            vars.%:    "7"
            vars.msg1: "******"
            vars.msg2: "normal value 1"
            vars.msg3: "******"
            vars.msg4: "******"
            vars.msg5: "******"
            vars.msg6: "******"
            vars.msg7: "******"
        
        
        Plan: 0 to add, 0 to change, 0 to destroy.

To change the mask character and/or length, you can use the `-maskchar` and `-numchars` flags, e.g. `terraform plan | terrahelp mask -maskchar=# -numchars=3`

By default, the mask command will also attempt to detect whether any previous sensitive data may be exposed, and if so will mask this as well. This may happen for example when changing the value of one sensitive value to another e.g.

        + template_file.example
            rendered:  "" => "<computed>"
            template:  "" => "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}"
            vars.#:    "" => "3"
            vars.msg1: "old-sensitive-value" => "sensitive-value-1-AK#%DJGHS*G"
            vars.msg2: "" => "normal value 1"
            vars.msg3: "" => "sensitive-value-3-//dfhs//"

In which case the resulting mask will look as follows 

        + template_file.example
            rendered:  "" => "<computed>"
            template:  "" => "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}"
            vars.#:    "" => "3"
            vars.msg1: "******" => "******"
            vars.msg2: "" => "normal value 1"
            vars.msg3: "" => "******"

If you want to suppress this default behaviour you can use the `-prev=false`
            
### How does it work out what is considered sensitive?
At present, `terrahelp` relies on using the `terraform.tfvars` file as the mechanism to indicate which values should be considered sensitive, and thus masked out when detected.  

## Terrahelp example - encryption & decryption 

This example contains a very simple terraform setup composed entirely of local resources (e.g. template resource) and exists in order to demonstrate how you can do basic encryption and decryption functionality in the absence of a formal solution (ref https://github.com/hashicorp/terraform/issues/516).
 
This example is completely safe to run and will not land up costing you any money in a cloud provider! It currently demonstrates a terraform 0.7.7 based setup which includes the new lists and maps functionality.
 
The CLI itself offers a more comprehensive view of the various options available, so please use this if you need more info.
Additionally you can read this corresponding blog which gives a more detailed explanation of this functionality and its usage: [Securing Terraform State with Vault](https://www.opencredo.com/securing-terraform-state-with-vault).

### Simple inline encryption of terraform output

This example will demonstrate _inline_ encryption and decryption using the _simple_ encryption provider where we will pipe the content (`terraform plan` in this case) directly into it. This specific example uses the basic command line arguments as opposed to environment variables to control the process, and assumes you have opened a terminal window in this directory and have the terraform binary available on your path.

* Run a `terraform plan` as normal

        terraform plan
        
* Inspect the result which should look something like below:        
        
        Refreshing Terraform state in-memory prior to plan...
        The refreshed state will be used to calculate this plan, but
        will not be persisted to local or remote state storage.
        
        ...
                
        <= data.template_file.example
            rendered:  "<computed>"
            template:  "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}\nmsg4 = ${msg4}\nmsg5 = ${msg5}\nmsg6 = ${msg6}\nmsg7 = ${msg7}"
            vars.%:    "7"
            vars.msg1: "sensitive-value-1-AK#%DJGHS*G"
            vars.msg2: "normal value 1"
            vars.msg3: "sensitive-value-3-//dfhs//"
            vars.msg4: "sensitive-value-4 with equals sign i.e. ff=yy"
            vars.msg5: "sensitive-list-val-1"
            vars.msg6: "sensitive-flatmap-val-foo"
            vars.msg7: "sensitive-flatmap-val"
        
        
        Plan: 0 to add, 0 to change, 0 to destroy.

* Run the same command, but pipe the output into the `terrahelp encrypt` command. The default provider is the simple provider so you do not need to explicitly set this, although you do need to provide and encryption key.

        terraform plan | terrahelp encrypt -mode=inline -simple-key=AES256Key-32Characters0987654321 

* The result should now look something like below:

        Refreshing Terraform state in-memory prior to plan...
        The refreshed state will be used to calculate this plan, but
        will not be persisted to local or remote state storage.
        
        ...
        
        <= data.template_file.example
            rendered:  "<computed>"
            template:  "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}\nmsg4 = ${msg4}\nmsg5 = ${msg5}\nmsg6 = ${msg6}\nmsg7 = ${msg7}"
            vars.%:    "7"
            vars.msg1: "@terrahelp-encrypted(xufN6OOCI2TWDp793/zlba4nt3dUnsbbQpB64HTykYPr3+ZUKgze+fgbj2zW)"
            vars.msg2: "normal value 1"
            vars.msg3: "@terrahelp-encrypted(v6Wt2f1w2xvjHI8bsTXK51hrLOtQPswvTzWv+kGj7ojZAJcgf5POFT08)"
            vars.msg4: "@terrahelp-encrypted(iobUvjF5d4rc3q4GCrED3vUSz7gpCNnXM/Taah9OuVV5WDXEMRgxCGIxIiN5Die/JFkCgt+IoOiEL7nOcQ==)"
            vars.msg5: "@terrahelp-encrypted(7cZ2iwc00eLcDOBrP9pVtdlZErRHGr6hl++UynU1jnhRVjwV)"
            vars.msg6: "@terrahelp-encrypted(/kYPdcP3ROpchiHjGv7fysPIZfCnTYpR4XX841jAz2R317QYO/A+nf0=)"
            vars.msg7: "@terrahelp-encrypted(oIdMOgF6Wzg/s6KpRmYTZCDP7RiHw3EZwyc2+A4PSouEkD07GA==)"

* For decryption, you could pipe the output again into the `terrahelp decrypt` command, however more than likely, you will probably want to save the results into a file and then decrypt that. The sequence of commands to do that would be something as follows:
  
        terraform plan -out=my-infra.plan
        
        terrahelp encrypt -mode=inline -simple-key=AES256Key-32Characters0987654321 -file=my-infra.plan
        
        terrahelp decrypt -mode=inline -simple-key=AES256Key-32Characters0987654321 -file=my-infra.plan        

### Simple inline encryption of tfstate files

This example will also demonstrate _inline_ encryption and decryption using the _simple_ encryption provider using explicit command line arguments (an example using environment variables is shown with the Vault provider example), however unlike the example above, will operate over the main terraform tfstate files.

* Run terraform as normal, including apply

        terraform plan
        terraform apply

* Verify `terraform.tfstate` contents before encryption (e.g. by doing a `cat terraform.tfstate`).
This should look something like below:
    
        {
            "version": 3,
            "terraform_version": "0.7.7",
            "serial": 0,
            "lineage": "dfb415f5-07c5-478b-945e-a592f1cf09b6",
            "modules": [
                {
                    "path": [
                        "root"
                    ],
                    "outputs": {
                        "normal_val_2": {
                            "sensitive": false,
                            "type": "string",
                            "value": "normal value 2"
                        },
                        "rendered": {
                            "sensitive": false,
                            "type": "string",
                            "value": "\nmsg1 = sensitive-value-1-AK#%DJGHS*G\nmsg2 = normal value 1\nmsg3 = sensitive-value-3-//dfhs//\nmsg4 = sensitive-value-4 with equals sign i.e. ff=yy\nmsg5 = sensitive-list-val-1\nmsg6 = sensitive-flatmap-val-foo\nmsg7 = sensitive-flatmap-val"
                        }
                    },
                    "resources": {
                        "data.template_file.example": {
                            "type": "template_file",
                            "depends_on": [],
                            "primary": {
                                "id": "88dafb613a33265583a1ba802edb4d9ffafe604602d764c780b1db8c76c6c7fe",
                                "attributes": {
                                    "id": "88dafb613a33265583a1ba802edb4d9ffafe604602d764c780b1db8c76c6c7fe",
                                    "rendered": "\nmsg1 = sensitive-value-1-AK#%DJGHS*G\nmsg2 = normal value 1\nmsg3 = sensitive-value-3-//dfhs//\nmsg4 = sensitive-value-4 with equals sign i.e. ff=yy\nmsg5 = sensitive-list-val-1\nmsg6 = sensitive-flatmap-val-foo\nmsg7 = sensitive-flatmap-val",
                                    "template": "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}\nmsg4 = ${msg4}\nmsg5 = ${msg5}\nmsg6 = ${msg6}\nmsg7 = ${msg7}",
                                    "vars.%": "7",
                                    "vars.msg1": "sensitive-value-1-AK#%DJGHS*G",
                                    "vars.msg2": "normal value 1",
                                    "vars.msg3": "sensitive-value-3-//dfhs//",
                                    "vars.msg4": "sensitive-value-4 with equals sign i.e. ff=yy",
                                    "vars.msg5": "sensitive-list-val-1",
                                    "vars.msg6": "sensitive-flatmap-val-foo",
                                    "vars.msg7": "sensitive-flatmap-val"
                                },
                                "meta": {},
                                "tainted": false
                            },
                            "deposed": [],
                            "provider": ""
                        }
                    },
                    "depends_on": []
                }
            ]
        }

* Run the `terrahelp encrypt` command, except this time you will explicitly specify the file to encrypt (i.e. `terraform.tfstate`). In the absence of a `-file` argument, terrahelp will assume you are piping the input stream in.

        terrahelp encrypt -mode=inline -simple-key=AES256Key-32Characters0987654321 -file=terraform.tfstate

* Inspect `terraform.tfstate` content after encryption. Note how all the sensitive values, as detected in the `terraform.tfvars` file, have now been replaced with encrypted versions. The content should look something like that below: 

        {
            "version": 3,
            "terraform_version": "0.7.7",
            "serial": 0,
            "lineage": "07ecb11e-8b77-41c5-a07b-ca924adaf6bb",
            "modules": [
                {
                    "path": [
                        "root"
                    ],
                    "outputs": {
                        "normal_val_2": {
                            "sensitive": false,
                            "type": "string",
                            "value": "normal value 2"
                        },
                        "rendered": {
                            "sensitive": false,
                            "type": "string",
                            "value": "\nmsg1 = @terrahelp-encrypted(mWlSsFQFNaK0pubo17cx8ruVMmldpUYyhx83nDtRvASKReXeQhVQEXaWCsRg)\nmsg2 = normal value 1\nmsg3 = @terrahelp-encrypted(W+236mopyxfruRnmXqo5tMhCjS1h7Al4kAp5yZ+vT9wb2VS35js4T4NJ)\nmsg4 = @terrahelp-encrypted(qqscl1+HMyCxnSw9sSLbVE05CZ+LIOvpNFtpRflp5H7HTp0NK1SLRhsjG775KdB3mrLB5yYJ9uv0fjPbpw==)\nmsg5 = @terrahelp-encrypted(5mubnPPs0P7wndVFh6H0wG20V+ljzqg7+ZNv5jWcWyTEHk54)\nmsg6 = @terrahelp-encrypted(oX+He8/1SlU6vFIyWbklTqxOAoiQrcLUaEcsqjkkFH1kcjDTOncZNLc=)\nmsg7 = @terrahelp-encrypted(kNEhI+mAkHVaGczjIYH4peO0CLsNDZsZIAFH6jE9ReJqynE4Dw==)"
                        }
                    },
                    "resources": {
                        "data.template_file.example": {
                            "type": "template_file",
                            "depends_on": [],
                            "primary": {
                                "id": "88dafb613a33265583a1ba802edb4d9ffafe604602d764c780b1db8c76c6c7fe",
                                "attributes": {
                                    "id": "88dafb613a33265583a1ba802edb4d9ffafe604602d764c780b1db8c76c6c7fe",
                                    "rendered": "\nmsg1 = @terrahelp-encrypted(mWlSsFQFNaK0pubo17cx8ruVMmldpUYyhx83nDtRvASKReXeQhVQEXaWCsRg)\nmsg2 = normal value 1\nmsg3 = @terrahelp-encrypted(W+236mopyxfruRnmXqo5tMhCjS1h7Al4kAp5yZ+vT9wb2VS35js4T4NJ)\nmsg4 = @terrahelp-encrypted(qqscl1+HMyCxnSw9sSLbVE05CZ+LIOvpNFtpRflp5H7HTp0NK1SLRhsjG775KdB3mrLB5yYJ9uv0fjPbpw==)\nmsg5 = @terrahelp-encrypted(5mubnPPs0P7wndVFh6H0wG20V+ljzqg7+ZNv5jWcWyTEHk54)\nmsg6 = @terrahelp-encrypted(oX+He8/1SlU6vFIyWbklTqxOAoiQrcLUaEcsqjkkFH1kcjDTOncZNLc=)\nmsg7 = @terrahelp-encrypted(kNEhI+mAkHVaGczjIYH4peO0CLsNDZsZIAFH6jE9ReJqynE4Dw==)",
                                    "template": "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}\nmsg4 = ${msg4}\nmsg5 = ${msg5}\nmsg6 = ${msg6}\nmsg7 = ${msg7}",
                                    "vars.%": "7",
                                    "vars.msg1": "@terrahelp-encrypted(mWlSsFQFNaK0pubo17cx8ruVMmldpUYyhx83nDtRvASKReXeQhVQEXaWCsRg)",
                                    "vars.msg2": "normal value 1",
                                    "vars.msg3": "@terrahelp-encrypted(W+236mopyxfruRnmXqo5tMhCjS1h7Al4kAp5yZ+vT9wb2VS35js4T4NJ)",
                                    "vars.msg4": "@terrahelp-encrypted(qqscl1+HMyCxnSw9sSLbVE05CZ+LIOvpNFtpRflp5H7HTp0NK1SLRhsjG775KdB3mrLB5yYJ9uv0fjPbpw==)",
                                    "vars.msg5": "@terrahelp-encrypted(5mubnPPs0P7wndVFh6H0wG20V+ljzqg7+ZNv5jWcWyTEHk54)",
                                    "vars.msg6": "@terrahelp-encrypted(oX+He8/1SlU6vFIyWbklTqxOAoiQrcLUaEcsqjkkFH1kcjDTOncZNLc=)",
                                    "vars.msg7": "@terrahelp-encrypted(kNEhI+mAkHVaGczjIYH4peO0CLsNDZsZIAFH6jE9ReJqynE4Dw==)"
                                },
                                "meta": {},
                                "tainted": false
                            },
                            "deposed": [],
                            "provider": ""
                        }
                    },
                    "depends_on": []
                }
            ]
        }

* To get your normal `terraform.tfstate` content back, simply run the `decrypt` command with the same arguments as above.

        terrahelp decrypt -mode=inline -simple-key=AES256Key-32Characters0987654321 -file=terraform.tfstate 

* Again verify `terraform.tfstate` content after decryption. This should now look exactly the same as it did before doing the encryption


### Vault full encryption of tfstate files

This example will demonstrate _full_ encryption and decryption using the _vault_ encryption provider (tested against Vault Server 0.5.2). On this occasion, instead of explicitly configuring the process via command line arguments, we will use environment variables.

* First, you will need to ensure you have a running Vault server available. You can quite easily download the latest version from [here](https://www.vaultproject.io/downloads.html), then open up a new terminal, and for experimentation purposes, simply run the server in dev mode as below:

        vault server -dev -dev-root-token-id="terrahelp-devonly-vault-root-token"

* In a separate terminal, ensure you change into this example project folder again, and setup the necessary environment variables required for us to talk to our dev Vault server, as well as run the next set of `terrahelp` commands. Specifically will also run the `vault-autoconfig` command to configure Vault with the named encryption key we wnat to use. i.e.

        export VAULT_TOKEN="terrahelp-devonly-vault-root-token"
        export VAULT_ADDR="http://127.0.0.1:8200"
        export VAULT_SKIP_VERIFY="true"
        
        export TH_ENCRYPTION_PROVIDER="vault"
        export TH_ENCRYPTION_MODE="full"
        export TH_VAULT_NAMED_KEY="examplekey"
        
        terrahelp vault-autoconfig

* Run terraform as normal and inspect the terraform.tfstate content before encryption is applied

        terraform plan
        terraform apply

* Verify `terraform.tfstate` contents before encryption (e.g. by doing a `cat terraform.tfstate`).
This should look something like below:
    
        {
            "version": 1,
            "serial": 1,
            "modules": [
                {
                    "path": [
                        "root"
                    ],
                    "outputs": {
                        "normal_val_2": "normal value 2",
                        "rendered": "\nmsg1 = sensitive-value-1-AK#%DJGHS*G\nmsg2 = normal value 1\nmsg3 = sensitive-value-3-//dfhs//"
                    },
                    "resources": {
                        "template_file.example": {
                            "type": "template_file",
                            "primary": {
                                "id": "b2cc7afb65fe7b6ac21328905d82e28fcbcdad1992cefce82cfa91691af24b91",
                                "attributes": {
                                    "id": "b2cc7afb65fe7b6ac21328905d82e28fcbcdad1992cefce82cfa91691af24b91",
                                    "rendered": "\nmsg1 = sensitive-value-1-AK#%DJGHS*G\nmsg2 = normal value 1\nmsg3 = sensitive-value-3-//dfhs//",
                                    "template": "\nmsg1 = ${msg1}\nmsg2 = ${msg2}\nmsg3 = ${msg3}",
                                    "vars.#": "3",
                                    "vars.msg1": "sensitive-value-1-AK#%DJGHS*G",
                                    "vars.msg2": "normal value 1",
                                    "vars.msg3": "sensitive-value-3-//dfhs//"
                                }
                            }
                        }
                    }
                }
            ]
        }


* Run the `terrahelp encrypt` command, specifying the file to encrypt (i.e. `terraform.tfstate`). In the absence of a `-file` argument, terrahelp will assume you are piping the input stream in. The other arguments should be picked up from the environment variables.

         terrahelp encrypt -file=terraform.tfstate   

* Inspect `terraform.tfstate` content after encryption. Note how all the sensitive values, as detected in the terraform.tfvars file, have now been replaced with encrypted versions, and will look something like below: 

        @terrahelp-encrypted(vault:v1:h7Yx1VAYvd2pyW0dd/iWifSe6yFB8QI7Zv2KjlW5USM5AyT9o3g3U2bU3
        vbDweRCGUXq2P8qpNcp8LUXDUon2Q6ee8I20X6yJyj5I2AS9V9ec4YcFOS9odqG+6dFqdlgWUkvEXPsH6puL0rX
        depvR17dvK1QTID0iE14HS7b4UnwI0Ti+f2VX4GvKHhnfKwCejKVu3g2bXdjn35h+EH9cHonSTx24SI6mM5k9Uy
        L7ht7AfPtPkdiUW7XSiW69UsZ+ZWrz8  ...  Ej3NYiY71Z/B2Rfm3M3V22BjfCsoUAHR1gL8acb5xQryuk+B/
        zQdLx7fXgxS8rMPKFwrJVRVtdcJtLFtLLf42AV1oUCqYvvusyNiGkQ6p3/2cgbkWsm/gN2lc26AuD6wVtd44qi
        CKK5iBZU4HQH6P5dycL0Sjgg4vJvcve85fQOLtfrr+UnQP0hdTSfSUl5cjPZlW2s9AX3Y1UCdAhsJ2pajJHdRp
        rhpbhTC+E/tlm3ndCeT/nxj8w==)

* To get your normal tfstate content back, simply run the `decrypt` version of the above command i.e.

        terrahelp decrypt -file=terraform.tfstate  

* Verify `terraform.tfstate` contents after decryption. This should now look exactly the same as it did before doing the encryption


### How does it work out what is considered sensitive?
At present, `terrahelp` relies on using the `terraform.tfvars` file as the mechanism to indicate which values should be considered sensitive, and thus encrypted when detected. 
