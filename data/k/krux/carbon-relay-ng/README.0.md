Go library for in-process single-topic pub-sub
==============================================

behaves like tv42/topic, except doesn't kick out slow consumers.

Use the Go import path

    github.com/Dieterbe/topic

Documentation at http://godoc.org/github.com/tv42/topic
simple statsd client in go. supports gauge, counters, timings, sampling.
Note: temporary fork until all PR's are merged into rcrowley's version.

go-metrics
==========

Go port of Coda Hale's Metrics library: <https://github.com/codahale/metrics>.

Documentation: <http://godoc.org/github.com/Dieterbe/go-metrics>.

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

Periodically log every metric in human-readable form to standard error:

```go
go metrics.Log(metrics.DefaultRegistry, 60e9, log.New(os.Stderr, "metrics: ", log.Lmicroseconds))
```

Periodically log every metric in slightly-more-parseable form to syslog:

```go
w, _ := syslog.Dial("unixgram", "/dev/log", syslog.LOG_INFO, "metrics")
go metrics.Syslog(metrics.DefaultRegistry, 60e9, w)
```

Periodically emit every metric to Graphite:

```go
addr, _ := net.ResolveTCPAddr("tcp", "127.0.0.1:2003")
go metrics.Graphite(metrics.DefaultRegistry, 10e9, "metrics.", addr)
```

Periodically emit every metric into InfluxDB:

```go
import "github.com/Dieterbe/go-metrics/influxdb"

go influxdb.Influxdb(metrics.DefaultRegistry, 10e9, &influxdb.Config{
    Host:     "127.0.0.1:8086",
    Database: "metrics",
    Username: "test",
    Password: "test",
})
```

Periodically upload every metric to Librato:

```go
import "github.com/Dieterbe/go-metrics/librato"

go librato.Librato(metrics.DefaultRegistry,
    10e9,                  // interval
    "example@example.com", // account owner email address
    "token",               // Librato API token
    "hostname",            // source
    []float64{0.95},       // precentiles to send
    time.Millisecond,      // time unit
)
```

Periodically emit every metric to StatHat:

```go
import "github.com/Dieterbe/go-metrics/stathat"

go stathat.Stathat(metrics.DefaultRegistry, 10e9, "example@example.com")
```

Maintain all metrics along with expvars at `/debug/vars2`:

This uses the same mechanism as [the official expvar](http://golang.org/pkg/expvar/)
but exposed under `/debug/vars2`, which shows a json representation of all your usual expvars
as well as all your go-metrics.


```go
import "github.com/Dieterbe/go-metrics/exp"

exp.Exp(metrics.DefaultRegistry)
```

Installation
------------

```sh
go get github.com/Dieterbe/go-metrics
```

StatHat support additionally requires their Go client:

```sh
go get github.com/stathat/go
```
toki
====

Regexp tokenizer/scanner in Go.

The scanner takes in a list of token definitions and string input. 
it is general and easy to use.

token definition
================
a token is a pair of constant and regexp string.

og-rek
======

ogórek is a Go library for encoding and decoding pickles.
# Assert (c) Blake Mizerany and Keith Rarick -- MIT LICENCE

## Assertions for Go tests

## Install

    $ go get github.com/bmizerany/assert

## Use

**point.go**

    package point

    type Point struct {
        x, y int
    }

**point_test.go**


    package point

    import (
        "testing"
        "github.com/bmizerany/assert"
    )

    func TestAsserts(t *testing.T) {
        p1 := Point{1, 1}
        p2 := Point{2, 1}

        assert.Equal(t, p1, p2)
    }

**output**
    $ go test
     --- FAIL: TestAsserts (0.00 seconds)
	 assert.go:15: /Users/flavio.barbosa/dev/stewie/src/point_test.go:12
         assert.go:24: ! X: 1 != 2
	 FAIL

## Docs

    http://github.com/bmizerany/assert
mux
===
[![Build Status](https://travis-ci.org/gorilla/mux.png?branch=master)](https://travis-ci.org/gorilla/mux)

gorilla/mux is a powerful URL router and dispatcher.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/mux
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

gorilla/context is a general purpose registry for global request variables.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
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
        &assetfs.AssetFS{Asset: Asset, AssetDir: AssetDir, Prefix: "data"}))

to serve files embedded from the `data` directory.
goagain
=======

Zero-downtime restarts in Go
----------------------------

The `goagain` package provides primitives for bringing zero-downtime restarts to Go applications that accept connections from a [`net.TCPListener`](http://golang.org/pkg/net/#TCPListener) or [`net.UnixListener`](http://golang.org/pkg/net/#UnixListener).

Have a look at the examples because it isn't just a matter of importing the library and everything working.  Your `main` function will have to accomodate the `goagain` protocols and your process will have to have some definition (however contrived you like) of a graceful shutdown process.

Installation
------------

	go get github.com/rcrowley/goagain

Usage
-----

Send `SIGUSR2` to a process using `goagain` and it will restart without downtime.

[`example/single/main.go`](https://github.com/rcrowley/goagain/blob/master/example/single/main.go):  The `Single` strategy (named because it calls `execve`(2) once) operates similarly to Nginx and Unicorn.  The parent forks a child, the child execs, and then the child kills the parent.  This is easy to understand but doesn't play nicely with Upstart and similar direct-supervision `init`(8) daemons.  It should play nicely with `systemd`.

[`example/double/main.go`](https://github.com/rcrowley/goagain/blob/master/example/double/main.go):  The `Double` strategy (named because it calls `execve`(2) twice) is **experimental** so proceed with caution.  The parent forks a child, the child execs, the child signals the parent, the parent execs, and finally the parent kills the child.  This is regrettably much more complicated but plays nicely with Upstart and similar direct-supervision `init`(8) daemons.
## Golang logging library

[![godoc](http://img.shields.io/badge/godoc-reference-blue.svg?style=flat)](https://godoc.org/github.com/op/go-logging) [![build](https://img.shields.io/travis/op/go-logging.svg?style=flat)](https://travis-ci.org/op/go-logging)

Package logging implements a logging infrastructure for Go. Its output format
is customizable and supports different logging backends like syslog, file and
memory. Multiple backends can be utilized with different log levels per backend
and logger.

## Example

Let's have a look at an [example](examples/example.go) which demonstrates most
of the features found in this library.

[![Example Output](examples/example.png)](examples/example.go)

```go
package main

import (
	"os"

	"github.com/op/go-logging"
)

var log = logging.MustGetLogger("example")

// Example format string. Everything except the message has a custom color
// which is dependent on the log level. Many fields have a custom output
// formatting too, eg. the time returns the hour down to the milli second.
var format = logging.MustStringFormatter(
	"%{color}%{time:15:04:05.000} %{shortfunc} ▶ %{level:.4s} %{id:03x}%{color:reset} %{message}",
)

// Password is just an example type implementing the Redactor interface. Any
// time this is logged, the Redacted() function will be called.
type Password string

func (p Password) Redacted() interface{} {
	return logging.Redact(string(p))
}

func main() {
	// For demo purposes, create two backend for os.Stderr.
	backend1 := logging.NewLogBackend(os.Stderr, "", 0)
	backend2 := logging.NewLogBackend(os.Stderr, "", 0)

	// For messages written to backend2 we want to add some additional
	// information to the output, including the used log level and the name of
	// the function.
	backend2Formatter := logging.NewBackendFormatter(backend2, format)

	// Only errors and more severe messages should be sent to backend1
	backend1Leveled := logging.AddModuleLevel(backend1)
	backend1Leveled.SetLevel(logging.ERROR, "")

	// Set the backends to be used.
	logging.SetBackend(backend1Leveled, backend2Formatter)

	log.Debug("debug %s", Password("secret"))
	log.Info("info")
	log.Notice("notice")
	log.Warning("warning")
	log.Error("err")
	log.Critical("crit")
}
```

## Installing

### Using *go get*

    $ go get github.com/op/go-logging

After this command *go-logging* is ready to use. Its source will be in:

    $GOROOT/src/pkg/github.com/op/go-logging

You can use `go get -u` to update the package.

## Documentation

For docs, see http://godoc.org/github.com/op/go-logging or run:

    $ godoc github.com/op/go-logging

## Additional resources

* [wslog](https://godoc.org/github.com/cryptix/go/logging/wslog) -- exposes log messages through a WebSocket.
helper functions to detect metric format and convey operations by modifying string identifiers, in both legacy (~statsd) and metrics 2.0 format
