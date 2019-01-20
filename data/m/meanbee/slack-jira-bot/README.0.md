# Slack Jira Issue Expansion

[![Build Status](https://travis-ci.org/meanbee/slack-jira-bot.svg?branch=travis)](https://travis-ci.org/meanbee/slack-jira-bot)

> **Update 2017-08-24:** If you're looking to get setup quickly then you should check out https://slack.atlassian.io before using this image.  If that's not for you - come back!

A killer feature of the integration between Hipchat and Jira is the issue expansion.  Whenever a Jira issue is mention in the chat, the Jira integration would pop up some high level information about the issue and a link.

![](https://punkstar.keybase.pub/github/slack-jira-bot/screenshots/hipchat_example.png)

With the Jira integration in Slack being a bit light, we decided to implement a simple bot using the [Slack RTM API](https://api.slack.com/rtm):

![](https://punkstar.keybase.pub/github/slack-jira-bot/screenshots/message_example_with_attachment.png)

# Installation
    
## Docker Image

    docker run -it --restart=always -d \
        -e JIRA_BASEURL=https://yourjirainstall.atlassian.net \
        -e JIRA_USERNAME='yourjirausername' \
        -e JIRA_PASSWORD='yourjirapassword' \
        -e SLACK_API_KEY='yourslackapikey' \
        meanbee/slack-jira-bot:latest
    
# Configuration

The configuration is run of environment variables:

* `SLACK_API_KEY`
* `JIRA_BASEURL`, e.g. `https://yourcompany.atlassian.net`
* `JIRA_USERNAME`
* `JIRA_PASSWORD`
This repository holds supplementary Go networking libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
The *.dat files in this directory are copied from The WebKit Open Source
Project, specifically $WEBKITROOT/LayoutTests/html5lib/resources.
WebKit is licensed under a BSD style license.
http://webkit.org/coding/bsd-license.html says:

Copyright (C) 2009 Apple Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY APPLE INC. AND ITS CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL APPLE INC. OR ITS CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

These test cases come from
http://www.w3.org/International/tests/repository/html5/the-input-byte-stream/results-basics

Distributed under both the W3C Test Suite License
(http://www.w3.org/Consortium/Legal/2008/04-testsuite-license)
and the W3C 3-clause BSD License
(http://www.w3.org/Consortium/Legal/2008/03-bsd-license).
To contribute to a W3C Test Suite, see the policies and contribution
forms (http://www.w3.org/2004/10/27-testcases).
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
# h2i

**h2i** is an interactive HTTP/2 ("h2") console debugger. Miss the good ol'
days of telnetting to your HTTP/1.n servers? We're bringing you
back.

Features:
- send raw HTTP/2 frames
 - PING
 - SETTINGS
 - HEADERS
 - etc
- type in HTTP/1.n and have it auto-HPACK/frame-ify it for HTTP/2
- pretty print all received HTTP/2 frames from the peer (including HPACK decoding)
- tab completion of commands, options

Not yet features, but soon:
- unnecessary CONTINUATION frames on short boundaries, to test peer implementations 
- request bodies (DATA frames)
- send invalid frames for testing server implementations (supported by underlying Framer)

Later:
- act like a server

## Installation

```
$ go get golang.org/x/net/http2/h2i
$ h2i <host>
```

## Demo

```
$ h2i
Usage: h2i <hostname>
  
  -insecure
        Whether to skip TLS cert validation
  -nextproto string
        Comma-separated list of NPN/ALPN protocol names to negotiate. (default "h2,h2-14")

$ h2i google.com
Connecting to google.com:443 ...
Connected to 74.125.224.41:443
Negotiated protocol "h2-14"
[FrameHeader SETTINGS len=18]
  [MAX_CONCURRENT_STREAMS = 100]
  [INITIAL_WINDOW_SIZE = 1048576]
  [MAX_FRAME_SIZE = 16384]
[FrameHeader WINDOW_UPDATE len=4]
  Window-Increment = 983041
  
h2i> PING h2iSayHI
[FrameHeader PING flags=ACK len=8]
  Data = "h2iSayHI"
h2i> headers
(as HTTP/1.1)> GET / HTTP/1.1
(as HTTP/1.1)> Host: ip.appspot.com
(as HTTP/1.1)> User-Agent: h2i/brad-n-blake
(as HTTP/1.1)>  
Opening Stream-ID 1:
 :authority = ip.appspot.com
 :method = GET
 :path = /
 :scheme = https
 user-agent = h2i/brad-n-blake
[FrameHeader HEADERS flags=END_HEADERS stream=1 len=77]
  :status = "200"
  alternate-protocol = "443:quic,p=1"
  content-length = "15"
  content-type = "text/html"
  date = "Fri, 01 May 2015 23:06:56 GMT"
  server = "Google Frontend"
[FrameHeader DATA flags=END_STREAM stream=1 len=15]
  "173.164.155.78\n"
[FrameHeader PING len=8]
  Data = "\x00\x00\x00\x00\x00\x00\x00\x00"
h2i> ping  
[FrameHeader PING flags=ACK len=8]  
  Data = "h2i_ping"  
h2i> ping  
[FrameHeader PING flags=ACK len=8]
  Data = "h2i_ping"
h2i> ping
[FrameHeader GOAWAY len=22]
  Last-Stream-ID = 1; Error-Code = PROTOCOL_ERROR (1)

ReadFrame: EOF
```

## Status

Quick few hour hack. So much yet to do. Feel free to file issues for
bugs or wishlist items, but [@bmizerany](https://github.com/bmizerany/)
and I aren't yet accepting pull requests until things settle down.


Client:
 -- Firefox nightly with about:config network.http.spdy.enabled.http2draft set true
 -- Chrome: go to chrome://flags/#enable-spdy4, save and restart (button at bottom)

Make CA:
$ openssl genrsa -out rootCA.key 2048
$ openssl req -x509 -new -nodes -key rootCA.key -days 1024 -out rootCA.pem
... install that to Firefox

Make cert:
$ openssl genrsa -out server.key 2048
$ openssl req -new -key server.key -out server.csr
$ openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.crt -days 500


This is a fork of the encoding/xml package at ca1d6c4, the last commit before
https://go.googlesource.com/go/+/c0d6d33 "encoding/xml: restore Go 1.4 name
space behavior" made late in the lead-up to the Go 1.5 release.

The list of encoding/xml changes is at
https://go.googlesource.com/go/+log/master/src/encoding/xml

This fork is temporary, and I (nigeltao) expect to revert it after Go 1.6 is
released.

See http://golang.org/issue/11841
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

Instructions
============

Install the package with:

    go get gopkg.in/check.v1
    
Import it with:

    import "gopkg.in/check.v1"

and use _check_ as the package name inside the code.

For more details, visit the project page:

* http://labix.org/gocheck

and the API documentation:

* https://gopkg.in/check.v1
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

Testify - Thou Shalt Write Tests
================================

[![Build Status](https://travis-ci.org/stretchr/testify.svg)](https://travis-ci.org/stretchr/testify) [![Go Report Card](https://goreportcard.com/badge/github.com/stretchr/testify)](https://goreportcard.com/report/github.com/stretchr/testify) [![GoDoc](https://godoc.org/github.com/stretchr/testify?status.svg)](https://godoc.org/github.com/stretchr/testify)

Go code (golang) set of packages that provide many tools for testifying that your code will behave as you intend.

Features include:

  * [Easy assertions](#assert-package)
  * [Mocking](#mock-package)
  * [HTTP response trapping](#http-package)
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


[`http`](http://godoc.org/github.com/stretchr/testify/http "API documentation") package
---------------------------------------------------------------------------------------

The `http` package contains test objects useful for testing code that relies on the `net/http` package.  Check out the [(deprecated) API documentation for the `http` package](http://godoc.org/github.com/stretchr/testify/http).

We recommend you use [httptest](http://golang.org/pkg/net/http/httptest) instead.

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

    * Latest version: go get github.com/stretchr/testify
    * Specific version: go get gopkg.in/stretchr/testify.v1

This will then make the following packages available to you:

    github.com/stretchr/testify/assert
    github.com/stretchr/testify/mock
    github.com/stretchr/testify/http

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

Version History
===============

   * 1.0 - New package versioning strategy adopted.

------

Contributing
============

Please feel free to submit issues, fork the repository and send pull requests!

When submitting an issue, we ask that you please include a complete test function that demonstrates the issue.  Extra credit for those using Testify to write the test code that demonstrates it.

------

Licence
=======
Copyright (c) 2012 - 2013 Mat Ryer and Tyler Bunnell

Please consider promoting this project if you find it useful.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# objx

  * Jump into the [API Documentation](http://godoc.org/github.com/stretchr/objx)
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
# TOML Validator

If Go is installed, it's simple to try it out:

```bash
go get github.com/BurntSushi/toml/cmd/tomlv
tomlv some-toml-file.toml
```

You can see the types of every key in a TOML file with:

```bash
tomlv -types some-toml-file.toml
```

At the moment, only one error message is reported at a time. Error messages
include line numbers. No output means that the files given are valid TOML, or
there is a bug in `tomlv`.

Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)
# Implements the TOML test suite interface for TOML encoders

This is an implementation of the interface expected by
[toml-test](https://github.com/BurntSushi/toml-test) for the
[TOML encoder](https://github.com/BurntSushi/toml).
In particular, it maps JSON data on `stdin` to a TOML format on `stdout`.


Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

Compatible with `toml-test` version
[v0.2.0](https://github.com/BurntSushi/toml-test/tree/v0.2.0)
# Implements the TOML test suite interface

This is an implementation of the interface expected by
[toml-test](https://github.com/BurntSushi/toml-test) for my
[toml parser written in Go](https://github.com/BurntSushi/toml).
In particular, it maps TOML data on `stdin` to a JSON format on `stdout`.


Compatible with TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

Compatible with `toml-test` version
[v0.2.0](https://github.com/BurntSushi/toml-test/tree/v0.2.0)
go-jira-client
==============

go-jira-client is a simple client written in golang to consume jira API... and Tokyo.

[![Build Status](https://travis-ci.org/plouc/go-jira-client.png?branch=master)](https://travis-ci.org/plouc/go-jira-client)
![govend](art/govend.png)

# govend [![GoDoc](http://godoc.org/github.com/govend/govend?status.png)](http://godoc.org/github.com/govend/govend) [![Build Status](http://beta.drone.io/api/badges/govend/govend/status.svg)](http://beta.drone.io/govend/govend) [![Go Report Card](https://goreportcard.com/badge/github.com/govend/govend)](https://goreportcard.com/report/github.com/govend/govend) [![Join the chat at https://gitter.im/govend/govend](https://badges.gitter.im/govend/govend.svg)](https://gitter.im/govend/govend?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) ![](https://img.shields.io/badge/windows-ready-green.svg)

`govend` is a simple tool to vendor Go package dependencies.
It's like `go get`, but for vendoring external or third party packages.

**govend is:**
* like `go get`, but for vendoring packages
* compatible with any project directory structure
* designed to vendor nested dependencies to the nth degree
* compatible with Go versions 1.5+.

**govend does not:**
* wrap the `go` command
* try to create a new project
* force you to lock dependency versions
* generate temporary directories or files
* alter any Go environment variables, including `$GOPATH`

# Install

```bash
$ go get -u github.com/govend/govend
```

# Usage

### Small Project Usage

```bash
# ...                                        # code, code, code
$ govend github.com/gorilla/mux              # vendor a dependency
# ...                                        # code, code, code
$ go build                                   # go tools work normally
$ govend -u github.com/gorilla/mux           # updated a dependency
# ...                                        # code, code, code
$ go build                                   # go tools work normally
```

### Big Project Usage

```bash
# ...                  # code, code, code
$ govend -v            # scan your project and download all dependencies
# ...                  # code, code, code
$ go build             # go tools work normally
$ govend -u            # scan your project and update all dependencies
# ...                  # code, code, code
$ go build             # go tools work normally
```

### Team Usage
Sarah:
```bash
$ git init                     # start git project
# ...                          # code, code, code
$ govend -v -l                 # scan your project, download all dependencies,
                               # and create a vendor.yml file to lock
                               # dependency versions
# ...                          # code, code, code
$ go build                     # go tools work normally
$ govend -v -u                 # scan your project, update all dependencies,
                               # and update the vendor.yml revision versions
# ...                          # code, code, code
$ git push                     # push code to github
$ go build                     # go tools work normally
```

Mike:
```bash
$ git clone url       # grab all the code Sarah pushed
$ govend -v           # download all the dependencies in the vendor.yml file
                      # and use the same revision versions Sarah is using
$ go build            # build the exact same binary Sarah has
# ...                 # code, code, code
```

# Verbose Mode
As with most unixy programs, no news is good news.
Therefore, unless something goes wrong `govend` will not print anything to the
terminal.
If you want to see progress or proof something is happening use the `-v` flag
to print out package import paths as they are downloaded and vendored.

# The Dependency Tree
You can use the `-t` or `--tree` flag to view a rendition of the package
dependency tree. This is helpful to visualize and understand what packages your
dependencies rely on as well.

# Explicitly Vendor A Package
You can explicitly tell `govend` to vendor one or more packages.
It works the same way as `go get` but instead of running:

```Bash
$ go get github.com/gorilla/mux
```

which will download the gorilla `mux` package into your `$GOPATH`, run:

```Bash
$ govend github.com/gorilla/mux
```

which will download the gorilla `mux` package into your local project `vendor/`
directory.
If you want `govend` to download more than one package, just tack them on.
For example, you might want to vendor the gorilla `mux`, `http`, and
`securecookie` packages like so:

```Bash
$ govend github.com/gorilla/mux github.com/gorilla/http github.com/gorilla/securecookie
```

# Explicitly Update Packages

To update a package that has already been vendored, simply use the `-u` network
update flag.
This flag has the same meaning as `go get -u` and will always use the network
to download a fresh copy of the dependency.

To update the gorilla `mux` package in your `$GOPATH` you would run:

```Bash
$ go get -u github.com/gorilla/mux
```

To update the gorilla `mux` package in your local project `vendor/` directory
run:

```Bash
$ govend -u github.com/gorilla/mux
```

# Vendor Packages Automatically

It would get old to ask `govend` to download and vendor each individual package
when working on large Go projects.
Thankfully `govend` can scan your project source code and identify dependencies
for you.

`govend` assumes you want this behavior when no packages are explicitly
provided:

```Bash
$ cd project/root

$ govend
```

You can also show dependencies as they are vendored with the `-v` flag:

```Bash
$ cd project/root

$ govend -v
github.com/kr/fs
github.com/BurntSushi/toml
github.com/spf13/cobra
github.com/inconshreveable/mousetrap
github.com/spf13/pflag
gopkg.in/yaml.v2
gopkg.in/check.v1
```

If you would like to update all vendored packages in a project use the `-u`
flag:

```Bash
$ cd project/root

$ govend -v -u
github.com/kr/fs
github.com/BurntSushi/toml
github.com/spf13/cobra
github.com/inconshreveable/mousetrap
github.com/spf13/pflag
gopkg.in/yaml.v2
gopkg.in/check.v1
```

# Lock Packages

The command `govend` only scans for external packages and downloads them to the
`vendor/` directory in your project. You may need more control over versioning
your dependencies so that reliable reproducible builds are possible.

`govend` can save the path and commit revisions of each repository downloaded
in a `vendor.yml` file.
This is called vendor locking.
The format of the file can be specified to be `JSON` or `TOML`, `YAML` is used
by default.
Usually this file is located in the root directory of your project and should
be included in your version control system.

To generate a `vendor.yml` file use the `-l` flag:

```Bash
$ cd project/root

$ govend -v -l
github.com/kr/fs
github.com/BurntSushi/toml
github.com/spf13/cobra
github.com/inconshreveable/mousetrap
github.com/spf13/pflag
gopkg.in/yaml.v2
gopkg.in/check.v1
```

The resulting project structure should look something like:

```Bash
.
├── ...
├── code
├── README.md
├── vendor
└── vendor.yml
```

The contents of the generated `vendor.yml` file in this example would be:

```yaml
vendors:
- path: github.com/BurntSushi/toml
  rev: f772cd89eb0b33743387f826d1918df67f99cc7a
- path: github.com/inconshreveable/mousetrap
  rev: 76626ae9c91c4f2a10f34cad8ce83ea42c93bb75
- path: github.com/kr/fs
  rev: 2788f0dbd16903de03cb8186e5c7d97b69ad387b
- path: github.com/spf13/cobra
  rev: 65a708cee0a4424f4e353d031ce440643e312f92
- path: github.com/spf13/pflag
  rev: 7f60f83a2c81bc3c3c0d5297f61ddfa68da9d3b7
- path: gopkg.in/check.v1
  rev: 4f90aeace3a26ad7021961c297b22c42160c7b25
- path: gopkg.in/yaml.v2
  rev: f7716cbe52baa25d2e9b0d0da546fcf909fc16b4
```


You can now ignore the large `vendor/` directory and pass the small `vendor.yml`
file to your buddy.
Your buddy can run `$ govend` and will get the exact same dependency versions
as specified by `vendor.yml`.

This is how a team of developers can ensure reproducible builds if they do not
want to check the `vendor/` directory into a version control system.

> Note: It is still a best practice to check in the `vendor/` directory to your
VCS.

# Update Locked Packages

If you would like to update a particular vendored package to its latest version
use the `-u` flag:

```Bash
$ govend -u github.com/gorilla/mux
```

If you would like to update all the vendored packages to their latest versions
run:

```Bash
$ govend -u
```

If you want to update a particular vendored package to a particular revision,
update the relevant `rev:` value inside the `vendor.yml` file.
Then to update to that specific revision hash run:

```Bash
$ govend -l
```

# Prune Packages
Sometimes large repositories must be downloaded to satisfy a singular package
dependency. This generates a lot of dead files if you are checking in `vendor/`
to your VCS.

The `--prune` flag will use the known dependency tree to remove or prune out
all unused package leaving you with only relevant code.

> Note: When pruning occurs it removes not only unused packages, but also files
that start with `.`, `_` and files that end with `_test.go`. This is because
pruning is highly likely to break third party tests.

# Hold onto Packages
If you stop using or importing a package path in your project code, `govend`
will remove that package from your `vendor.yml`. Its how `govend` cleans up
after you and keeps `vendor.yml` tidy.

The `--hold` flag will tell `govend` to keep that dependency, even if its not
being used as an import by your project. This is great for versioning tooling
that you might want to ship with a project.

```Bash
$ govend --hold github.com/hashicorp/terraform
```

> Note: When using the `--hold` flag a manifest file like `vendor.yml` is
generated.  Essentially, opting into `--hold` is also opting into `--lock`.
Also because of the nature of hold, repos using hold cannot be pruned.

# Vendor Report Summary
If you would like to get a report summary of the number of unique packages
scanned, skipped and how many repositories were downloaded, run `govend -v -r`.

```bash
→ govend -v -r
github.com/kr/fs
github.com/BurntSushi/toml
github.com/spf13/cobra
github.com/inconshreveable/mousetrap
github.com/spf13/pflag
gopkg.in/yaml.v2
gopkg.in/check.v1

packages scanned: 7
packages skipped: 0
repos downloaded: 7
```

# Vendor Scan
You may want to scan your code to determine how many third party dependencies
are
in your project.
To do so run `govend -s <path/to/dir>`. You can also specify different output
formats.

**TXT**
```bash
$ govend -s packages
github.com/kr/fs
gopkg.in/yaml.v2
```

**JSON**
```bash
$ govend -s -f json packages
[
  "github.com/kr/fs",
  "gopkg.in/yaml.v2"
]
```

**YAML**
```bash
$ govend -s -f yaml packages
- github.com/kr/fs
- gopkg.in/yaml.v2
```
**XML**
```bash
$ govend -s -f xml packages
<string>gopkg.in/yaml.v2</string>
<string>github.com/kr/fs</string>
```

# More Flags

You can run `govend -h` to find more flags and options.

# Vendor Supported Go Versions

  * Go 1.4 or less - Go does not support vendoring
  * Go 1.5 - vendor via `GO15VENDOREXPERIMENT=1`
  * Go 1.6 - vendor unless `GO15VENDOREXPERIMENT=0`
  * Go 1.7+ - vendor always despite the value of `GO15VENDOREXPERIMENT`

For further explanation please read https://golang.org/doc/go1.6#go_command.

# Windows Support
`govend` works on Windows, but please report any bugs.

# Contributing
Simply fork the code and send a pull request.
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

[![Build Status](https://travis-ci.org/spf13/pflag.svg?branch=master)](https://travis-ci.org/spf13/pflag)

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
it was difficult to keep up with all of the the flag pointers in your code.
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
    flag.BoolVarP("boolname", "b", true, "help message")
}
flag.VarP(&flagVar, "varname", "v", 1234, "help message")
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

## More info

You can see the full reference documentation of the pflag package
[at godoc.org][3], or through go's standard documentation system by
running `godoc -http=:6060` and browsing to
[http://localhost:6060/pkg/github.com/ogier/pflag][2] after
installation.

[2]: http://localhost:6060/pkg/github.com/ogier/pflag
[3]: http://godoc.org/github.com/ogier/pflag
![cobra logo](https://cloud.githubusercontent.com/assets/173412/10886352/ad566232-814f-11e5-9cd0-aa101788c117.png)

Cobra is both a library for creating powerful modern CLI applications as well as a program to generate applications and command files.

Many of the most widely used Go projects are built using Cobra including:

* [Kubernetes](http://kubernetes.io/)
* [Hugo](http://gohugo.io)
* [rkt](https://github.com/coreos/rkt)
* [etcd](https://github.com/coreos/etcd)
* [Docker (distribution)](https://github.com/docker/distribution)
* [OpenShift](https://www.openshift.com/)
* [Delve](https://github.com/derekparker/delve)
* [GopherJS](http://www.gopherjs.org/)
* [CockroachDB](http://www.cockroachlabs.com/)
* [Bleve](http://www.blevesearch.com/)
* [ProjectAtomic (enterprise)](http://www.projectatomic.io/)
* [Parse (CLI)](https://parse.com/)
* [GiantSwarm's swarm](https://github.com/giantswarm/cli)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)


[![Build Status](https://travis-ci.org/spf13/cobra.svg "Travis CI status")](https://travis-ci.org/spf13/cobra)
[![CircleCI status](https://circleci.com/gh/spf13/cobra.png?circle-token=:circle-token "CircleCI status")](https://circleci.com/gh/spf13/cobra)

![cobra](https://cloud.githubusercontent.com/assets/173412/10911369/84832a8e-8212-11e5-9f82-cc96660a4794.gif)

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
* Easy generation of applications & commands with `cobra create appname` & `cobra add cmdname`
* Intelligent suggestions (`app srver`... did you mean `app server`?)
* Automatic help generation for commands and flags
* Automatic detailed help for `app help [command]`
* Automatic help flag recognition of `-h`, `--help`, etc.
* Automatically generated bash autocomplete for your application
* Automatically generated man pages for your application
* Command aliases so you can change things without breaking them
* The flexibilty to define your own help, usage, etc.
* Optional tight integration with [viper](http://github.com/spf13/viper) for 12-factor apps

Cobra has an exceptionally clean interface and simple design without needless
constructors or initialization methods.

Applications built with Cobra commands are designed to be as user-friendly as
possible. Flags can be placed before or after the command (as long as a
confusing space isn’t provided). Both short and long flags can be used. A
command need not even be fully typed.  Help is automatically generated and
available for the application or for a specific command using either the help
command or the `--help` flag.

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

    > hugo server --port=1313

In this command we are telling Git to clone the url bare.

    > git clone URL --bare

## Commands

Command is the central point of the application. Each interaction that
the application supports will be contained in a Command. A command can
have children commands and optionally run an action.

In the example above, 'server' is the command.

A Command has the following structure:

```go
type Command struct {
    Use string // The one-line usage message.
    Short string // The short description shown in the 'help' output.
    Long string // The long message shown in the 'help <this-command>' output.
    Run func(cmd *Command, args []string) // Run runs the command.
}
```

## Flags

A Flag is a way to modify the behavior of a command. Cobra supports
fully POSIX-compliant flags as well as the Go [flag package](https://golang.org/pkg/flag/).
A Cobra command can define flags that persist through to children commands
and flags that are only available to that command.

In the example above, 'port' is the flag.

Flag functionality is provided by the [pflag
library](https://github.com/ogier/pflag), a fork of the flag standard library
which maintains the same interface while adding POSIX compliance.

## Usage

Cobra works by creating a set of commands and then organizing them into a tree.
The tree defines the structure of the application.

Once each command is defined with its corresponding flags, then the
tree is assigned to the commander which is finally executed.

# Installing
Using Cobra is easy. First, use `go get` to install the latest version
of the library. This command will install the `cobra` generator executible
along with the library:

    > go get -v github.com/spf13/cobra/cobra

Next, include Cobra in your application:

```go
import "github.com/spf13/cobra"
```

# Getting Started

While you are welcome to provide your own organization, typically a Cobra based
application will follow the following organizational structure.

```
  ▾ appName/
    ▾ cmd/
        add.go
        your.go
        commands.go
        here.go
      main.go
```

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import "{pathToYourApp}/cmd"

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}
```

## Using the Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

### cobra init

The `cobra init [yourApp]` command will create your initial application code
for you. It is a very powerful application that will populate your program with
the right structure so you can immediately enjoy all the benefits of Cobra. It
will also automatically apply the license you specify to your application.

Cobra init is pretty smart. You can provide it a full path, or simply a path
similar to what is expected in the import.

```
cobra init github.com/spf13/newAppName
```

### cobra add

Once an application is initialized Cobra can create additional commands for you.
Let's say you created an app and you wanted the following commands for it:

* app serve
* app config
* app config create

In your project directory (where your main.go file is) you would run the following:

```
cobra add serve
cobra add config
cobra add create -p 'configCmd'
```

Once you have run these three commands you would have an app structure that would look like:

```
  ▾ app/
    ▾ cmd/
        serve.go
        config.go
        create.go
      main.go
```

at this point you can run `go run main.go` and it would run your app. `go run
main.go serve`, `go run main.go config`, `go run main.go config create` along
with `go run main.go help serve`, etc would all work.

Obviously you haven't added your own code to these yet, the commands are ready
for you to give them their tasks. Have fun.

### Configuring the cobra generator

The cobra generator will be easier to use if you provide a simple configuration
file which will help you eliminate providing a bunch of repeated information in
flags over and over.

an example ~/.cobra.yaml file:

```yaml
author: Steve Francia <spf@spf13.com>
license: MIT
```

## Manually implementing Cobra

To manually implement cobra you need to create a bare main.go file and a RootCmd file.
You will optionally provide additional commands as you see fit.

### Create the root command

The root command represents your binary itself.


#### Manually create rootCmd

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

for example cmd/root.go:

```go
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
```

### Create your main.go

With the root command you need to have your main function execute it.
Execute should be run on the root for clarity, though it can be called on any command.

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import "{pathToYourApp}/cmd"

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
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

### Attach command to its parent


If you notice in the above example we attach the command to its parent. In
this case the parent is the rootCmd. In this example we are attaching it to the
root, but commands can be attached at any level.

```go
RootCmd.AddCommand(versionCmd)
```

### Remove a command from its parent

Removing a command is not a common action in simple programs, but it allows 3rd
parties to customize an existing command tree.

In this example, we remove the existing `VersionCmd` command of an existing
root command, and we replace it with our own version:

```go
mainlib.RootCmd.RemoveCommand(mainlib.VersionCmd)
mainlib.RootCmd.AddCommand(versionCmd)
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
            For many years people have printed back to the screen.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdEcho = &cobra.Command{
		Use:   "echo [string to echo]",
		Short: "Echo anything to the screen",
		Long: `echo is for echoing anything back.
            Echo works a lot like print, except it has a child command.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdTimes = &cobra.Command{
		Use:   "times [# times] [string to echo]",
		Short: "Echo anything to the screen more times",
		Long: `echo things multiple times back to the user by providing
            a count and a string.`,
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

## The Help Command

Cobra automatically adds a help command to your application when you have subcommands.
This will be called when a user runs 'app help'. Additionally, help will also
support all other commands as input. Say, for instance, you have a command called
'create' without any additional configuration; Cobra will work when 'app help
create' is called.  Every command will automatically have the '--help' flag added.

### Example

The following output is automatically generated by Cobra. Nothing beyond the
command and flag definitions are needed.

    > hugo help

    hugo is the main command, used to build your Hugo site.

    Hugo is a Fast and Flexible Static Site Generator
    built with love by spf13 and friends in Go.

    Complete documentation is available at http://gohugo.io/.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

    Use "hugo [command] --help" for more information about a command.


Help is just a command like any other. There is no special logic or behavior
around it. In fact, you can provide your own if you want.

### Defining your own help

You can provide your own Help command or your own template for the default command to use.

The default help command is

```go
func (c *Command) initHelp() {
	if c.helpCommand == nil {
		c.helpCommand = &Command{
			Use:   "help [command]",
			Short: "Help about any command",
			Long: `Help provides help for any command in the application.
        Simply type ` + c.Name() + ` help [path to command] for full details.`,
			Run: c.HelpFunc(),
		}
	}
	c.AddCommand(c.helpCommand)
}
```

You can provide your own command, function or template through the following methods:

```go
command.SetHelpCommand(cmd *Command)

command.SetHelpFunc(f func(*Command, []string))

command.SetHelpTemplate(s string)
```

The latter two will also apply to any children commands.

## Usage

When the user provides an invalid flag or invalid command, Cobra responds by
showing the user the 'usage'.

### Example
You may recognize this from the help above. That's because the default help
embeds the usage as part of its output.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

### Defining your own usage
You can provide your own usage function or template for Cobra to use.

The default usage function is:

```go
return func(c *Command) error {
	err := tmpl(c.Out(), c.UsageTemplate(), c)
	return err
}
```

Like help, the function and template are overridable through public methods:

```go
command.SetUsageFunc(f func(*Command) error)

command.SetUsageTemplate(s string)
```

## PreRun or PostRun Hooks

It is possible to run functions before or after the main `Run` function of your command. The `PersistentPreRun` and `PreRun` functions will be executed before `Run`. `PersistentPostRun` and `PostRun` will be executed after `Run`.  The `Persistent*Run` functions will be inherrited by children if they do not declare their own.  These function are run in the following order:

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
	_ = rootCmd.Execute()
	fmt.Print("\n")
	rootCmd.SetArgs([]string{"sub", "arg1", "arg2"})
	_ = rootCmd.Execute()
}
```


## Alternative Error Handling

Cobra also has functions where the return signature is an error. This allows for errors to bubble up to the top, providing a way to handle the errors in one location. The current list of functions that return an error is:

* PersistentPreRunE
* PreRunE
* RunE
* PostRunE
* PersistentPostRunE

**Example Usage using RunE:**

```go
package main

import (
	"errors"
	"log"

	"github.com/spf13/cobra"
)

func main() {
	var rootCmd = &cobra.Command{
		Use:   "hugo",
		Short: "Hugo is a very fast static site generator",
		Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
		RunE: func(cmd *cobra.Command, args []string) error {
			// Do Stuff Here
			return errors.New("some random error")
		},
	}

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}
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

## Generating Markdown-formatted documentation for your command

Cobra can generate a Markdown-formatted document based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Markdown Docs](doc/md_docs.md).

## Generating man pages for your command

Cobra can generate a man page based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Man Docs](doc/man_docs.md).

## Generating bash completions for your command

Cobra can generate a bash-completion file. If you add more information to your command, these completions can be amazingly powerful and flexible.  Read more about it in [Bash Completions](bash_completions.md).

## Debugging

Cobra provides a ‘DebugFlags’ method on a command which, when called, will print
out everything Cobra knows about the flags for each command.

### Example

```go
command.DebugFlags()
```

## Release Notes
* **0.9.0** June 17, 2014
  * flags can appears anywhere in the args (provided they are unambiguous)
  * --help prints usage screen for app or command
  * Prefix matching for commands
  * Cleaner looking help and usage output
  * Extensive test suite
* **0.8.0** Nov 5, 2013
  * Reworked interface to remove commander completely
  * Command now primary structure
  * No initialization needed
  * Usage & Help templates & functions definable at any level
  * Updated Readme
* **0.7.0** Sept 24, 2013
  * Needs more eyes
  * Test suite
  * Support for automatic error messages
  * Support for help command
  * Support for printing to any io.Writer instead of os.Stderr
  * Support for persistent flags which cascade down tree
  * Ready for integration into Hugo
* **0.1.0** Sept 3, 2013
  * Implement first draft

## Extensions

Libraries for extending Cobra:

* [cmdns](https://github.com/gosuri/cmdns): Enables name spacing a command's immediate children. It provides an alternative way to structure subcommands, similar to `heroku apps:create` and `ovrclk clusters:launch`.

## ToDo
* Launch proper documentation site

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors

Names in no particular order:

* [spf13](https://github.com/spf13),
[eparis](https://github.com/eparis),
[bep](https://github.com/bep), and many more!

## License

Cobra is released under the Apache 2.0 license. See [LICENSE.txt](https://github.com/spf13/cobra/blob/master/LICENSE.txt)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/spf13/cobra/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
go-spew
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
* [Docker](https://github.com/docker/docker)
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


[![Build Status](https://travis-ci.org/spf13/cobra.svg "Travis CI status")](https://travis-ci.org/spf13/cobra)
[![CircleCI status](https://circleci.com/gh/spf13/cobra.png?circle-token=:circle-token "CircleCI status")](https://circleci.com/gh/spf13/cobra)
[![GoDoc](https://godoc.org/github.com/spf13/cobra?status.svg)](https://godoc.org/github.com/spf13/cobra)

![cobra](https://cloud.githubusercontent.com/assets/173412/10911369/84832a8e-8212-11e5-9f82-cc96660a4794.gif)

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
* Easy generation of applications & commands with `cobra create appname` & `cobra add cmdname`
* Intelligent suggestions (`app srver`... did you mean `app server`?)
* Automatic help generation for commands and flags
* Automatic detailed help for `app help [command]`
* Automatic help flag recognition of `-h`, `--help`, etc.
* Automatically generated bash autocomplete for your application
* Automatically generated man pages for your application
* Command aliases so you can change things without breaking them
* The flexibility to define your own help, usage, etc.
* Optional tight integration with [viper](http://github.com/spf13/viper) for 12-factor apps

Cobra has an exceptionally clean interface and simple design without needless
constructors or initialization methods.

Applications built with Cobra commands are designed to be as user-friendly as
possible. Flags can be placed before or after the command (as long as a
confusing space isn’t provided). Both short and long flags can be used. A
command need not even be fully typed.  Help is automatically generated and
available for the application or for a specific command using either the help
command or the `--help` flag.

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

    > hugo server --port=1313

In this command we are telling Git to clone the url bare.

    > git clone URL --bare

## Commands

Command is the central point of the application. Each interaction that
the application supports will be contained in a Command. A command can
have children commands and optionally run an action.

In the example above, 'server' is the command.

A Command has the following structure:

```go
type Command struct {
    Use string // The one-line usage message.
    Short string // The short description shown in the 'help' output.
    Long string // The long message shown in the 'help <this-command>' output.
    Run func(cmd *Command, args []string) // Run runs the command.
}
```

## Flags

A Flag is a way to modify the behavior of a command. Cobra supports
fully POSIX-compliant flags as well as the Go [flag package](https://golang.org/pkg/flag/).
A Cobra command can define flags that persist through to children commands
and flags that are only available to that command.

In the example above, 'port' is the flag.

Flag functionality is provided by the [pflag
library](https://github.com/ogier/pflag), a fork of the flag standard library
which maintains the same interface while adding POSIX compliance.

## Usage

Cobra works by creating a set of commands and then organizing them into a tree.
The tree defines the structure of the application.

Once each command is defined with its corresponding flags, then the
tree is assigned to the commander which is finally executed.

# Installing
Using Cobra is easy. First, use `go get` to install the latest version
of the library. This command will install the `cobra` generator executible
along with the library:

    > go get -v github.com/spf13/cobra/cobra

Next, include Cobra in your application:

```go
import "github.com/spf13/cobra"
```

# Getting Started

While you are welcome to provide your own organization, typically a Cobra based
application will follow the following organizational structure.

```
  ▾ appName/
    ▾ cmd/
        add.go
        your.go
        commands.go
        here.go
      main.go
```

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

## Using the Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

In order to use the cobra command, compile it using the following command:

    > go get github.com/spf13/cobra/cobra

This will create the cobra executable under your `$GOPATH/bin` directory.

### cobra init

The `cobra init [yourApp]` command will create your initial application code
for you. It is a very powerful application that will populate your program with
the right structure so you can immediately enjoy all the benefits of Cobra. It
will also automatically apply the license you specify to your application.

Cobra init is pretty smart. You can provide it a full path, or simply a path
similar to what is expected in the import.

```
cobra init github.com/spf13/newAppName
```

### cobra add

Once an application is initialized Cobra can create additional commands for you.
Let's say you created an app and you wanted the following commands for it:

* app serve
* app config
* app config create

In your project directory (where your main.go file is) you would run the following:

```
cobra add serve
cobra add config
cobra add create -p 'configCmd'
```

*Note: Use camelCase (not snake_case/snake-case) for command names.
Otherwise, you will become unexpected errors.
For example, `cobra add add-user` is incorrect, but `cobra add addUser` is valid.*

Once you have run these three commands you would have an app structure that would look like:

```
  ▾ app/
    ▾ cmd/
        serve.go
        config.go
        create.go
      main.go
```

at this point you can run `go run main.go` and it would run your app. `go run
main.go serve`, `go run main.go config`, `go run main.go config create` along
with `go run main.go help serve`, etc would all work.

Obviously you haven't added your own code to these yet, the commands are ready
for you to give them their tasks. Have fun.

### Configuring the cobra generator

The cobra generator will be easier to use if you provide a simple configuration
file which will help you eliminate providing a bunch of repeated information in
flags over and over.

An example ~/.cobra.yaml file:

```yaml
author: Steve Francia <spf@spf13.com>
license: MIT
```

You can specify no license by setting `license` to `none` or you can specify
a custom license:

```yaml
license:
  header: This file is part of {{ .appName }}.
  text: |
    {{ .copyright }}

    This is my license. There are many like it, but this one is mine.
    My license is my best friend. It is my life. I must master it as I must
    master my life.
```

You can also use built-in licenses. For example, **GPLv2**, **GPLv3**, **LGPL**,
**AGPL**, **MIT**, **2-Clause BSD** or **3-Clause BSD**.

## Manually implementing Cobra

To manually implement cobra you need to create a bare main.go file and a RootCmd file.
You will optionally provide additional commands as you see fit.

### Create the root command

The root command represents your binary itself.


#### Manually create rootCmd

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

for example cmd/root.go:

```go
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

### Attach command to its parent


If you notice in the above example we attach the command to its parent. In
this case the parent is the rootCmd. In this example we are attaching it to the
root, but commands can be attached at any level.

```go
RootCmd.AddCommand(versionCmd)
```

### Remove a command from its parent

Removing a command is not a common action in simple programs, but it allows 3rd
parties to customize an existing command tree.

In this example, we remove the existing `VersionCmd` command of an existing
root command, and we replace it with our own version:

```go
mainlib.RootCmd.RemoveCommand(mainlib.VersionCmd)
mainlib.RootCmd.AddCommand(versionCmd)
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
            For many years people have printed back to the screen.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdEcho = &cobra.Command{
		Use:   "echo [string to echo]",
		Short: "Echo anything to the screen",
		Long: `echo is for echoing anything back.
            Echo works a lot like print, except it has a child command.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdTimes = &cobra.Command{
		Use:   "times [# times] [string to echo]",
		Short: "Echo anything to the screen more times",
		Long: `echo things multiple times back to the user by providing
            a count and a string.`,
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

## The Help Command

Cobra automatically adds a help command to your application when you have subcommands.
This will be called when a user runs 'app help'. Additionally, help will also
support all other commands as input. Say, for instance, you have a command called
'create' without any additional configuration; Cobra will work when 'app help
create' is called.  Every command will automatically have the '--help' flag added.

### Example

The following output is automatically generated by Cobra. Nothing beyond the
command and flag definitions are needed.

    > hugo help

    hugo is the main command, used to build your Hugo site.

    Hugo is a Fast and Flexible Static Site Generator
    built with love by spf13 and friends in Go.

    Complete documentation is available at http://gohugo.io/.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

    Use "hugo [command] --help" for more information about a command.


Help is just a command like any other. There is no special logic or behavior
around it. In fact, you can provide your own if you want.

### Defining your own help

You can provide your own Help command or your own template for the default command to use.

The default help command is

```go
func (c *Command) initHelp() {
	if c.helpCommand == nil {
		c.helpCommand = &Command{
			Use:   "help [command]",
			Short: "Help about any command",
			Long: `Help provides help for any command in the application.
        Simply type ` + c.Name() + ` help [path to command] for full details.`,
			Run: c.HelpFunc(),
		}
	}
	c.AddCommand(c.helpCommand)
}
```

You can provide your own command, function or template through the following methods:

```go
command.SetHelpCommand(cmd *Command)

command.SetHelpFunc(f func(*Command, []string))

command.SetHelpTemplate(s string)
```

The latter two will also apply to any children commands.

## Usage

When the user provides an invalid flag or invalid command, Cobra responds by
showing the user the 'usage'.

### Example
You may recognize this from the help above. That's because the default help
embeds the usage as part of its output.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

### Defining your own usage
You can provide your own usage function or template for Cobra to use.

The default usage function is:

```go
return func(c *Command) error {
	err := tmpl(c.Out(), c.UsageTemplate(), c)
	return err
}
```

Like help, the function and template are overridable through public methods:

```go
command.SetUsageFunc(f func(*Command) error)

command.SetUsageTemplate(s string)
```

## PreRun or PostRun Hooks

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
	_ = rootCmd.Execute()
	fmt.Print("\n")
	rootCmd.SetArgs([]string{"sub", "arg1", "arg2"})
	_ = rootCmd.Execute()
}
```


## Alternative Error Handling

Cobra also has functions where the return signature is an error. This allows for errors to bubble up to the top,
providing a way to handle the errors in one location. The current list of functions that return an error is:

* PersistentPreRunE
* PreRunE
* RunE
* PostRunE
* PersistentPostRunE

If you would like to silence the default `error` and `usage` output in favor of your own, you can set `SilenceUsage`
and `SilenceErrors` to `true` on the command. A child command respects these flags if they are set on the parent
command.

**Example Usage using RunE:**

```go
package main

import (
	"errors"
	"log"

	"github.com/spf13/cobra"
)

func main() {
	var rootCmd = &cobra.Command{
		Use:   "hugo",
		Short: "Hugo is a very fast static site generator",
		Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
		RunE: func(cmd *cobra.Command, args []string) error {
			// Do Stuff Here
			return errors.New("some random error")
		},
	}

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}
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

## Generating Markdown-formatted documentation for your command

Cobra can generate a Markdown-formatted document based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Markdown Docs](doc/md_docs.md).

## Generating man pages for your command

Cobra can generate a man page based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Man Docs](doc/man_docs.md).

## Generating bash completions for your command

Cobra can generate a bash-completion file. If you add more information to your command, these completions can be amazingly powerful and flexible.  Read more about it in [Bash Completions](bash_completions.md).

## Debugging

Cobra provides a ‘DebugFlags’ method on a command which, when called, will print
out everything Cobra knows about the flags for each command.

### Example

```go
command.DebugFlags()
```

## Release Notes
* **0.9.0** June 17, 2014
  * flags can appears anywhere in the args (provided they are unambiguous)
  * --help prints usage screen for app or command
  * Prefix matching for commands
  * Cleaner looking help and usage output
  * Extensive test suite
* **0.8.0** Nov 5, 2013
  * Reworked interface to remove commander completely
  * Command now primary structure
  * No initialization needed
  * Usage & Help templates & functions definable at any level
  * Updated Readme
* **0.7.0** Sept 24, 2013
  * Needs more eyes
  * Test suite
  * Support for automatic error messages
  * Support for help command
  * Support for printing to any io.Writer instead of os.Stderr
  * Support for persistent flags which cascade down tree
  * Ready for integration into Hugo
* **0.1.0** Sept 3, 2013
  * Implement first draft

## Extensions

Libraries for extending Cobra:

* [cmdns](https://github.com/gosuri/cmdns): Enables name spacing a command's immediate children. It provides an alternative way to structure subcommands, similar to `heroku apps:create` and `ovrclk clusters:launch`.

## ToDo
* Launch proper documentation site

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors

Names in no particular order:

* [spf13](https://github.com/spf13),
[eparis](https://github.com/eparis),
[bep](https://github.com/bep), and many more!

## License

Cobra is released under the Apache 2.0 license. See [LICENSE.txt](https://github.com/spf13/cobra/blob/master/LICENSE.txt)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/spf13/cobra/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
Slack API in Go [![GoDoc](https://godoc.org/github.com/nlopes/slack?status.svg)](https://godoc.org/github.com/nlopes/slack) [![Build Status](https://travis-ci.org/nlopes/slack.svg)](https://travis-ci.org/nlopes/slack)
===============

This library supports most if not all of the `api.slack.com` REST
calls, as well as the Real-Time Messaging protocol over websocket, in
a fully managed way.


Note: If you just updated from master and it broke your implementation, please check [0.0.1](https://github.com/nlopes/slack/releases/tag/v0.0.1)

## Installing

### *go get*

    $ go get github.com/nlopes/slack

## Example

### Getting all groups

```golang
import (
	"fmt"

	"github.com/nlopes/slack"
)

func main() {
	api := slack.New("YOUR_TOKEN_HERE")
	// If you set debugging, it will log all requests to the console
	// Useful when encountering issues
	// api.SetDebug(true)
	groups, err := api.GetGroups(false)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	for _, group := range groups {
		fmt.Printf("ID: %s, Name: %s\n", group.ID, group.Name)
	}
}
```

### Getting User Information

```golang
import (
    "fmt"

    "github.com/nlopes/slack"
)

func main() {
    api := slack.New("YOUR_TOKEN_HERE")
    user, err := api.GetUserInfo("U023BECGF")
    if err != nil {
	    fmt.Printf("%s\n", err)
	    return
    }
    fmt.Printf("ID: %s, Fullname: %s, Email: %s\n", user.ID, user.Profile.RealName, user.Profile.Email)
}
```

## Minimal RTM usage:

See https://github.com/nlopes/slack/blob/master/examples/websocket/websocket.go


## Contributing

You are more than welcome to contribute to this project.  Fork and
make a Pull Request, or create an Issue if you see any problem.

## License

BSD 2 Clause license
