urlesc [![Build Status](https://travis-ci.org/opennota/urlesc.png?branch=master)](https://travis-ci.org/opennota/urlesc) [![GoDoc](http://godoc.org/github.com/opennota/urlesc?status.svg)](http://godoc.org/github.com/opennota/urlesc)
======

Package urlesc implements query escaping as per RFC 3986.

It contains some parts of the net/url package, modified so as to allow
some reserved characters incorrectly escaped by net/url (see [issue 5684](https://github.com/golang/go/issues/5684)).

## Install

    go get github.com/opennota/urlesc

## License

MIT

# Purell

Purell is a tiny Go library to normalize URLs. It returns a pure URL. Pure-ell. Sanitizer and all. Yeah, I know...

Based on the [wikipedia paper][wiki] and the [RFC 3986 document][rfc].

[![build status](https://secure.travis-ci.org/PuerkitoBio/purell.png)](http://travis-ci.org/PuerkitoBio/purell)

## Install

`go get github.com/PuerkitoBio/purell`

## Changelog

*    **2016-07-27 (v1.0.0)** : Normalize IDN to ASCII (thanks to @zenovich).
*    **2015-02-08** : Add fix for relative paths issue ([PR #5][pr5]) and add fix for unnecessary encoding of reserved characters ([see issue #7][iss7]).
*    **v0.2.0** : Add benchmarks, Attempt IDN support.
*    **v0.1.0** : Initial release.

## Examples

From `example_test.go` (note that in your code, you would import "github.com/PuerkitoBio/purell", and would prefix references to its methods and constants with "purell."):

```go
package purell

import (
  "fmt"
  "net/url"
)

func ExampleNormalizeURLString() {
  if normalized, err := NormalizeURLString("hTTp://someWEBsite.com:80/Amazing%3f/url/",
    FlagLowercaseScheme|FlagLowercaseHost|FlagUppercaseEscapes); err != nil {
    panic(err)
  } else {
    fmt.Print(normalized)
  }
  // Output: http://somewebsite.com:80/Amazing%3F/url/
}

func ExampleMustNormalizeURLString() {
  normalized := MustNormalizeURLString("hTTpS://someWEBsite.com:443/Amazing%fa/url/",
    FlagsUnsafeGreedy)
  fmt.Print(normalized)

  // Output: http://somewebsite.com/Amazing%FA/url
}

func ExampleNormalizeURL() {
  if u, err := url.Parse("Http://SomeUrl.com:8080/a/b/.././c///g?c=3&a=1&b=9&c=0#target"); err != nil {
    panic(err)
  } else {
    normalized := NormalizeURL(u, FlagsUsuallySafeGreedy|FlagRemoveDuplicateSlashes|FlagRemoveFragment)
    fmt.Print(normalized)
  }

  // Output: http://someurl.com:8080/a/c/g?c=3&a=1&b=9&c=0
}
```

## API

As seen in the examples above, purell offers three methods, `NormalizeURLString(string, NormalizationFlags) (string, error)`, `MustNormalizeURLString(string, NormalizationFlags) (string)` and `NormalizeURL(*url.URL, NormalizationFlags) (string)`. They all normalize the provided URL based on the specified flags. Here are the available flags:

```go
const (
	// Safe normalizations
	FlagLowercaseScheme           NormalizationFlags = 1 << iota // HTTP://host -> http://host, applied by default in Go1.1
	FlagLowercaseHost                                            // http://HOST -> http://host
	FlagUppercaseEscapes                                         // http://host/t%ef -> http://host/t%EF
	FlagDecodeUnnecessaryEscapes                                 // http://host/t%41 -> http://host/tA
	FlagEncodeNecessaryEscapes                                   // http://host/!"#$ -> http://host/%21%22#$
	FlagRemoveDefaultPort                                        // http://host:80 -> http://host
	FlagRemoveEmptyQuerySeparator                                // http://host/path? -> http://host/path

	// Usually safe normalizations
	FlagRemoveTrailingSlash // http://host/path/ -> http://host/path
	FlagAddTrailingSlash    // http://host/path -> http://host/path/ (should choose only one of these add/remove trailing slash flags)
	FlagRemoveDotSegments   // http://host/path/./a/b/../c -> http://host/path/a/c

	// Unsafe normalizations
	FlagRemoveDirectoryIndex   // http://host/path/index.html -> http://host/path/
	FlagRemoveFragment         // http://host/path#fragment -> http://host/path
	FlagForceHTTP              // https://host -> http://host
	FlagRemoveDuplicateSlashes // http://host/path//a///b -> http://host/path/a/b
	FlagRemoveWWW              // http://www.host/ -> http://host/
	FlagAddWWW                 // http://host/ -> http://www.host/ (should choose only one of these add/remove WWW flags)
	FlagSortQuery              // http://host/path?c=3&b=2&a=1&b=1 -> http://host/path?a=1&b=1&b=2&c=3

	// Normalizations not in the wikipedia article, required to cover tests cases
	// submitted by jehiah
	FlagDecodeDWORDHost           // http://1113982867 -> http://66.102.7.147
	FlagDecodeOctalHost           // http://0102.0146.07.0223 -> http://66.102.7.147
	FlagDecodeHexHost             // http://0x42660793 -> http://66.102.7.147
	FlagRemoveUnnecessaryHostDots // http://.host../path -> http://host/path
	FlagRemoveEmptyPortSeparator  // http://host:/path -> http://host/path

	// Convenience set of safe normalizations
	FlagsSafe NormalizationFlags = FlagLowercaseHost | FlagLowercaseScheme | FlagUppercaseEscapes | FlagDecodeUnnecessaryEscapes | FlagEncodeNecessaryEscapes | FlagRemoveDefaultPort | FlagRemoveEmptyQuerySeparator

	// For convenience sets, "greedy" uses the "remove trailing slash" and "remove www. prefix" flags,
	// while "non-greedy" uses the "add (or keep) the trailing slash" and "add www. prefix".

	// Convenience set of usually safe normalizations (includes FlagsSafe)
	FlagsUsuallySafeGreedy    NormalizationFlags = FlagsSafe | FlagRemoveTrailingSlash | FlagRemoveDotSegments
	FlagsUsuallySafeNonGreedy NormalizationFlags = FlagsSafe | FlagAddTrailingSlash | FlagRemoveDotSegments

	// Convenience set of unsafe normalizations (includes FlagsUsuallySafe)
	FlagsUnsafeGreedy    NormalizationFlags = FlagsUsuallySafeGreedy | FlagRemoveDirectoryIndex | FlagRemoveFragment | FlagForceHTTP | FlagRemoveDuplicateSlashes | FlagRemoveWWW | FlagSortQuery
	FlagsUnsafeNonGreedy NormalizationFlags = FlagsUsuallySafeNonGreedy | FlagRemoveDirectoryIndex | FlagRemoveFragment | FlagForceHTTP | FlagRemoveDuplicateSlashes | FlagAddWWW | FlagSortQuery

	// Convenience set of all available flags
	FlagsAllGreedy    = FlagsUnsafeGreedy | FlagDecodeDWORDHost | FlagDecodeOctalHost | FlagDecodeHexHost | FlagRemoveUnnecessaryHostDots | FlagRemoveEmptyPortSeparator
	FlagsAllNonGreedy = FlagsUnsafeNonGreedy | FlagDecodeDWORDHost | FlagDecodeOctalHost | FlagDecodeHexHost | FlagRemoveUnnecessaryHostDots | FlagRemoveEmptyPortSeparator
)
```

For convenience, the set of flags `FlagsSafe`, `FlagsUsuallySafe[Greedy|NonGreedy]`, `FlagsUnsafe[Greedy|NonGreedy]` and `FlagsAll[Greedy|NonGreedy]` are provided for the similarly grouped normalizations on [wikipedia's URL normalization page][wiki]. You can add (using the bitwise OR `|` operator) or remove (using the bitwise AND NOT `&^` operator) individual flags from the sets if required, to build your own custom set.

The [full godoc reference is available on gopkgdoc][godoc].

Some things to note:

*    `FlagDecodeUnnecessaryEscapes`, `FlagEncodeNecessaryEscapes`, `FlagUppercaseEscapes` and `FlagRemoveEmptyQuerySeparator` are always implicitly set, because internally, the URL string is parsed as an URL object, which automatically decodes unnecessary escapes, uppercases and encodes necessary ones, and removes empty query separators (an unnecessary `?` at the end of the url). So this operation cannot **not** be done. For this reason, `FlagRemoveEmptyQuerySeparator` (as well as the other three) has been included in the `FlagsSafe` convenience set, instead of `FlagsUnsafe`, where Wikipedia puts it.

*    The `FlagDecodeUnnecessaryEscapes` decodes the following escapes (*from -> to*):
    -    %24 -> $
    -    %26 -> &
    -    %2B-%3B -> +,-./0123456789:;
    -    %3D -> =
    -    %40-%5A -> @ABCDEFGHIJKLMNOPQRSTUVWXYZ
    -    %5F -> _
    -    %61-%7A -> abcdefghijklmnopqrstuvwxyz
    -    %7E -> ~


*    When the `NormalizeURL` function is used (passing an URL object), this source URL object is modified (that is, after the call, the URL object will be modified to reflect the normalization).

*    The *replace IP with domain name* normalization (`http://208.77.188.166/ → http://www.example.com/`) is obviously not possible for a library without making some network requests. This is not implemented in purell.

*    The *remove unused query string parameters* and *remove default query parameters* are also not implemented, since this is a very case-specific normalization, and it is quite trivial to do with an URL object.

### Safe vs Usually Safe vs Unsafe

Purell allows you to control the level of risk you take while normalizing an URL. You can aggressively normalize, play it totally safe, or anything in between.

Consider the following URL:

`HTTPS://www.RooT.com/toto/t%45%1f///a/./b/../c/?z=3&w=2&a=4&w=1#invalid`

Normalizing with the `FlagsSafe` gives:

`https://www.root.com/toto/tE%1F///a/./b/../c/?z=3&w=2&a=4&w=1#invalid`

With the `FlagsUsuallySafeGreedy`:

`https://www.root.com/toto/tE%1F///a/c?z=3&w=2&a=4&w=1#invalid`

And with `FlagsUnsafeGreedy`:

`http://root.com/toto/tE%1F/a/c?a=4&w=1&w=2&z=3`

## TODOs

*    Add a class/default instance to allow specifying custom directory index names? At the moment, removing directory index removes `(^|/)((?:default|index)\.\w{1,4})$`.

## Thanks / Contributions

@rogpeppe
@jehiah
@opennota
@pchristopher1275
@zenovich

## License

The [BSD 3-Clause license][bsd].

[bsd]: http://opensource.org/licenses/BSD-3-Clause
[wiki]: http://en.wikipedia.org/wiki/URL_normalization
[rfc]: http://tools.ietf.org/html/rfc3986#section-6
[godoc]: http://go.pkgdoc.org/github.com/PuerkitoBio/purell
[pr5]: https://github.com/PuerkitoBio/purell/pull/5
[iss7]: https://github.com/PuerkitoBio/purell/issues/7
# CORS net/http middleware

(fork of github.com/rs/cors)

## Usage

```go
func main() {
  r := chi.NewRouter()

  // Basic CORS
  // for more ideas, see: https://developer.github.com/v3/#cross-origin-resource-sharing
  cors := cors.New(cors.Options{
    // AllowedOrigins: []string{"https://foo.com"}, // Use this to allow specific origin hosts
    AllowedOrigins:   []string{"*"},
    AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
    AllowedHeaders:   []string{"Accept", "Authorization", "Content-Type", "X-CSRF-Token"},
    ExposedHeaders:   []string{"Link"},
    AllowCredentials: true,
    MaxAge:           300, // Maximum value not ignored by any of major browsers
  })
  r.Use(cors.Handler)
  
  r.Get("/", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("welcome"))
  })
  
  http.ListenAndServe(":3000", r)
}
```

# Lg

`Lg` ("log") is a convenience wrapper pacakge for application logging backed by Logrus (https://github.com/Sirupsen/logrus). 


Once imported, it will pipe the stdlib "log" package to the backend setup with `lg`.
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

HTTP Coala
==========

Just a little bit of performance enhancing middleware -- HTTP Coala (aka Coalescer).

HTTP Coala is a middleware handler that routes multiple requests for the same URI
(and routed methods) to be processed as a single request. I don't recommend it
for every web service or handler chain, but for the computationally expensive
handlers that always yield the same response, HTTP Coala will give you a speed boost.

It's common among HTTP reverse proxy cache servers such as nginx,
Squid or Varnish - they all call it something else but works similarly.

* https://www.varnish-cache.org/docs/3.0/tutorial/handling_misbehaving_servers.html
* http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_lock
* http://wiki.squid-cache.org/Features/CollapsedForwarding


# Usage

Example with goji

```go
// from _example/main.go ....
func main() {
	r := chi.NewRouter()

	r.Use(middleware.Logger)
	r.Use(httpcoala.Route("HEAD", "GET")) // or, Route("*")
	// r.Use(otherMiddleware)

	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(100 * time.Millisecond) // expensive op
		w.WriteHeader(200)
		w.Write([]byte("hi"))
	})

	http.ListenAndServe(":1111", r)
}
```

as well, look at httpcoala_test.go


# Benchmarks

For a naive benchmark on my local Macbook pro, I used wrk with -c 100 and -t 100
on a web service that downloads an image and returns a resized version.

```
Without httpcoala middleware, Requests/sec:   7081.09
   With httpcoala middleware, Requests/sec:  18373.87
```

# TODO

* Allow a request key to be passed that determines when to coalesce requests.
  It would allow for more control such as grouping by a query param or header.

# License

Brought to you by the Pressly Go team - www.pressly.com / https://github.com/pressly

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# URLx
[Golang](http://golang.org/) pkg for URL parsing and normalization.

1. [Parsing URL](#parsing-url) ([GoDoc](https://godoc.org/github.com/goware/urlx#Parse))
2. [Normalizing URL](#normalizing-url)  ([GoDoc](https://godoc.org/github.com/goware/urlx#Normalize))
3. [Splitting host:port from URL](#splitting-hostport-from-url) ([GoDoc](https://godoc.org/github.com/goware/urlx#SplitHostPort))
4. [Resolving IP address from URL](#resolving-ip-address-from-url) ([GoDoc](https://godoc.org/github.com/goware/urlx#Resolve))

[![GoDoc](https://godoc.org/github.com/goware/urlx?status.png)](https://godoc.org/github.com/goware/urlx)
[![Travis](https://travis-ci.org/goware/urlx.svg?branch=master)](https://travis-ci.org/goware/urlx)

## Parsing URL

The [urlx.Parse()](https://godoc.org/github.com/goware/urlx#Parse) is compatible with the same function from [net/url](https://golang.org/pkg/net/url/#Parse) pkg, but has slightly different behavior. It enforces default scheme and favors absolute URLs over relative paths.

### Difference between [urlx](https://godoc.org/github.com/goware/urlx#Parse) and [net/url](https://golang.org/pkg/net/url/#Parse)

<table>
<thead>
<tr>
<th><a href="https://godoc.org/github.com/goware/urlx#Parse">github.com/goware/urlx</a></th>
<th><a href="https://golang.org/pkg/net/url/#Parse">net/url</a></th>
</tr>
</thead>
<tr>
<td>
<pre>
urlx.Parse("example.com")

&url.URL{
   Scheme:  "http",
   Host:    "example.com",
   Path:    "",
}
</pre>
</td>
<td>
<pre>
url.Parse("example.com")

&url.URL{
   Scheme:  "",
   Host:    "",
   Path:    "example.com",
}
</pre>
</td>
</tr>
<tr>
<td>
<pre>
urlx.Parse("localhost:8080")

&url.URL{
   Scheme:  "http",
   Host:    "localhost:8080",
   Path:    "",
   Opaque:  "",
}
</pre>
</td>
<td>
<pre>
url.Parse("localhost:8080")

&url.URL{
   Scheme:  "localhost",
   Host:    "",
   Path:    "",
   Opaque:  "8080",
}
</pre>
</td>
</tr>
<tr>
<td>
<pre>
urlx.Parse("user.local:8000/path")

&url.URL{
   Scheme:  "http",
   Host:    "user.local:8000",
   Path:    "/path",
   Opaque:  "",
}
</pre>
</td>
<td>
<pre>
url.Parse("user.local:8000/path")

&url.URL{
   Scheme:  "user.local",
   Host:    "",
   Path:    "",
   Opaque:  "8000/path",
}
</pre>
</td>
</tr>
</table>

### Usage

```go
import "github.com/goware/urlx"

func main() {
    url, _ := urlx.Parse("example.com")
    // url.Scheme == "http"
    // url.Host == "example.com"

    fmt.Print(url)
    // Prints http://example.com
}
```

## Normalizing URL

The [urlx.Normalize()](https://godoc.org/github.com/goware/urlx#Normalize) function normalizes the URL using the predefined subset of [Purell](https://github.com/PuerkitoBio/purell) flags.

### Usage

```go
import "github.com/goware/urlx"

func main() {
    url, _ := urlx.Parse("localhost:80///x///y/z/../././index.html?b=y&a=x#t=20")
    normalized, _ := urlx.Normalize(url)

    fmt.Print(normalized)
    // Prints http://localhost/x/y/index.html?a=x&b=y#t=20
}
```

## Splitting host:port from URL

The [urlx.SplitHostPort()](https://godoc.org/github.com/goware/urlx#SplitHostPort) is compatible with the same function from [net](https://golang.org/pkg/net/) pkg, but has slightly different behavior. It doesn't remove brackets from `[IPv6]` host.

### Usage

```go
import "github.com/goware/urlx"

func main() {
    url, _ := urlx.Parse("localhost:80")
    host, port, _ := urlx.SplitHostPort(url)

    fmt.Print(host)
    // Prints localhost

    fmt.Print(port)
    // Prints 80
}
```

## Resolving IP address from URL

The [urlx.Resolve()](https://godoc.org/github.com/goware/urlx#Resolve) is compatible with [ResolveIPAddr()](https://golang.org/pkg/net/#ResolveIPAddr) from [net](https://golang.org/pkg/net/).

### Usage

```go
url, _ := urlx.Parse("localhost")
ip, _ := urlx.Resolve(url)

fmt.Print(ip)
// Prints 127.0.0.1
```

## License
URLx is licensed under the [MIT License](./LICENSE).
go-ini
======

INI parsing library for Go (golang).

View the API documentation [here](http://godoc.org/github.com/vaughan0/go-ini).

Usage
-----

Parse an INI file:

```go
import "github.com/vaughan0/go-ini"

file, err := ini.LoadFile("myfile.ini")
```

Get data from the parsed file:

```go
name, ok := file.Get("person", "name")
if !ok {
  panic("'name' variable missing from 'person' section")
}
```

Iterate through values in a section:

```go
for key, value := range file["mysection"] {
  fmt.Printf("%s => %s\n", key, value)
}
```

Iterate through sections in a file:

```go
for name, section := range file {
  fmt.Printf("Section name: %s\n", name)
}
```

File Format
-----------

INI files are parsed by go-ini line-by-line. Each line may be one of the following:

  * A section definition: [section-name]
  * A property: key = value
  * A comment: #blahblah _or_ ;blahblah
  * Blank. The line will be ignored.

Properties defined before any section headers are placed in the default section, which has
the empty string as it's key.

Example:

```ini
# I am a comment
; So am I!

[apples]
colour = red or green
shape = applish

[oranges]
shape = square
colour = blue
```
Config
======

set airbrake.Endpoint and airbrake.ApiKey globals

Methods
=======

airbrake.Error(err) reports an error

airbrake.RequestError(err, *http.Request) can be used to add more context if you are in a http context


You can also automatically have this library report panics, use this method:

airbrake.CapturePanic(*http.Request)


example:

  func serve(w http.ResponseWriter, r *http.Request) {
      defer airbrake.CapturePanic(r)
      
      [...]

      panic("Oh no :-(") // will be recorded by airbrake 

  }# Render [![GoDoc](http://godoc.org/github.com/unrolled/render?status.svg)](http://godoc.org/github.com/unrolled/render) [![Build Status](https://travis-ci.org/unrolled/render.svg)](https://travis-ci.org/unrolled/render)

Render is a package that provides functionality for easily rendering JSON, XML, text, binary data, and HTML templates. This package is based on the [Martini](https://github.com/go-martini/martini) [render](https://github.com/martini-contrib/render) work.

## Block Deprecation Notice
Go 1.6 introduces a new [block](https://github.com/golang/go/blob/release-branch.go1.6/src/html/template/example_test.go#L128) action. This conflicts with Render's included `block` template function. To provide an easy migration path, a new function was created called `partial`. It is a duplicate of the old `block` function. It is advised that all users of the `block` function update their code to avoid any issues in the future. Previous to Go 1.6, Render's `block` functionality will continue to work but a message will be logged urging you to migrate to the new `partial` function.

## Usage
Render can be used with pretty much any web framework providing you can access the `http.ResponseWriter` from your handler. The rendering functions simply wraps Go's existing functionality for marshaling and rendering data.

- HTML: Uses the [html/template](http://golang.org/pkg/html/template/) package to render HTML templates.
- JSON: Uses the [encoding/json](http://golang.org/pkg/encoding/json/) package to marshal data into a JSON-encoded response.
- XML: Uses the [encoding/xml](http://golang.org/pkg/encoding/xml/) package to marshal data into an XML-encoded response.
- Binary data: Passes the incoming data straight through to the `http.ResponseWriter`.
- Text: Passes the incoming string straight through to the `http.ResponseWriter`.

~~~ go
// main.go
package main

import (
    "encoding/xml"
    "net/http"

    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

type ExampleXml struct {
    XMLName xml.Name `xml:"example"`
    One     string   `xml:"one,attr"`
    Two     string   `xml:"two,attr"`
}

func main() {
    r := render.New()
    mux := http.NewServeMux()

    mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
        w.Write([]byte("Welcome, visit sub pages now."))
    })

    mux.HandleFunc("/data", func(w http.ResponseWriter, req *http.Request) {
        r.Data(w, http.StatusOK, []byte("Some binary data here."))
    })

    mux.HandleFunc("/text", func(w http.ResponseWriter, req *http.Request) {
        r.Text(w, http.StatusOK, "Plain text here")
    })

    mux.HandleFunc("/json", func(w http.ResponseWriter, req *http.Request) {
        r.JSON(w, http.StatusOK, map[string]string{"hello": "json"})
    })

    mux.HandleFunc("/jsonp", func(w http.ResponseWriter, req *http.Request) {
        r.JSONP(w, http.StatusOK, "callbackName", map[string]string{"hello": "jsonp"})
    })

    mux.HandleFunc("/xml", func(w http.ResponseWriter, req *http.Request) {
        r.XML(w, http.StatusOK, ExampleXml{One: "hello", Two: "xml"})
    })

    mux.HandleFunc("/html", func(w http.ResponseWriter, req *http.Request) {
        // Assumes you have a template in ./templates called "example.tmpl"
        // $ mkdir -p templates && echo "<h1>Hello {{.}}.</h1>" > templates/example.tmpl
        r.HTML(w, http.StatusOK, "example", "World")
    })

    http.ListenAndServe("127.0.0.1:3000", mux)
}
~~~

~~~ html
<!-- templates/example.tmpl -->
<h1>Hello {{.}}.</h1>
~~~

### Available Options
Render comes with a variety of configuration options _(Note: these are not the default option values. See the defaults below.)_:

~~~ go
// ...
r := render.New(render.Options{
    Directory: "templates", // Specify what path to load the templates from.
    Asset: func(name string) ([]byte, error) { // Load from an Asset function instead of file.
      return []byte("template content"), nil
    },
    AssetNames: func() []string { // Return a list of asset names for the Asset function
      return []string{"filename.tmpl"}
    },
    Layout: "layout", // Specify a layout template. Layouts can call {{ yield }} to render the current template or {{ partial "css" }} to render a partial from the current template.
    Extensions: []string{".tmpl", ".html"}, // Specify extensions to load for templates.
    Funcs: []template.FuncMap{AppHelpers}, // Specify helper function maps for templates to access.
    Delims: render.Delims{"{[{", "}]}"}, // Sets delimiters to the specified strings.
    Charset: "UTF-8", // Sets encoding for json and html content-types. Default is "UTF-8".
    IndentJSON: true, // Output human readable JSON.
    IndentXML: true, // Output human readable XML.
    PrefixJSON: []byte(")]}',\n"), // Prefixes JSON responses with the given bytes.
    PrefixXML: []byte("<?xml version='1.0' encoding='UTF-8'?>"), // Prefixes XML responses with the given bytes.
    HTMLContentType: "application/xhtml+xml", // Output XHTML content type instead of default "text/html".
    IsDevelopment: true, // Render will now recompile the templates on every HTML response.
    UnEscapeHTML: true, // Replace ensure '&<>' are output correctly (JSON only).
    StreamingJSON: true, // Streams the JSON response via json.Encoder.
    RequirePartials: true, // Return an error if a template is missing a partial used in a layout.
    DisableHTTPErrorRendering: true, // Disables automatic rendering of http.StatusInternalServerError when an error occurs.
})
// ...
~~~

### Default Options
These are the preset options for Render:

~~~ go
r := render.New()

// Is the same as the default configuration options:

r := render.New(render.Options{
    Directory: "templates",
    Asset: nil,
    AssetNames: nil,
    Layout: "",
    Extensions: []string{".tmpl"},
    Funcs: []template.FuncMap{},
    Delims: render.Delims{"{{", "}}"},
    Charset: "UTF-8",
    IndentJSON: false,
    IndentXML: false,
    PrefixJSON: []byte(""),
    PrefixXML: []byte(""),
    HTMLContentType: "text/html",
    IsDevelopment: false,
    UnEscapeHTML: false,
    StreamingJSON: false,
    RequirePartials: false,
    DisableHTTPErrorRendering: false,
})
~~~

### JSON vs Streaming JSON
By default, Render does **not** stream JSON to the `http.ResponseWriter`. It instead marshalls your object into a byte array, and if no errors occurred, writes that byte array to the `http.ResponseWriter`. This is ideal as you can catch errors before sending any data.

If however you have the need to stream your JSON response (ie: dealing with massive objects), you can set the `StreamingJSON` option to true. This will use the `json.Encoder` to stream the output to the `http.ResponseWriter`. If an error occurs, you will receive the error in your code, but the response will have already been sent. Also note that streaming is only implemented in `render.JSON` and not `render.JSONP`, and the `UnEscapeHTML` and `Indent` options are ignored when streaming.

### Loading Templates
By default Render will attempt to load templates with a '.tmpl' extension from the "templates" directory. Templates are found by traversing the templates directory and are named by path and basename. For instance, the following directory structure:

~~~
templates/
  |
  |__ admin/
  |      |
  |      |__ index.tmpl
  |      |
  |      |__ edit.tmpl
  |
  |__ home.tmpl
~~~

Will provide the following templates:
~~~
admin/index
admin/edit
home
~~~

You can also load templates from memory by providing the Asset and AssetNames options,
e.g. when generating an asset file using [go-bindata](https://github.com/jteeuwen/go-bindata).

### Layouts
Render provides `yield` and `partial` functions for layouts to access:
~~~ go
// ...
r := render.New(render.Options{
    Layout: "layout",
})
// ...
~~~

~~~ html
<!-- templates/layout.tmpl -->
<html>
  <head>
    <title>My Layout</title>
    <!-- Render the partial template called `css-$current_template` here -->
    {{ partial "css" }}
  </head>
  <body>
    <!-- render the partial template called `header-$current_template` here -->
    {{ partial "header" }}
    <!-- Render the current template here -->
    {{ yield }}
    <!-- render the partial template called `footer-$current_template` here -->
    {{ partial "footer" }}
  </body>
</html>
~~~

`current` can also be called to get the current template being rendered.
~~~ html
<!-- templates/layout.tmpl -->
<html>
  <head>
    <title>My Layout</title>
  </head>
  <body>
    This is the {{ current }} page.
  </body>
</html>
~~~

Partials are defined by individual templates as seen below. The partial template's
name needs to be defined as "{partial name}-{template name}".
~~~ html
<!-- templates/home.tmpl -->
{{ define "header-home" }}
<h1>Home</h1>
{{ end }}

{{ define "footer-home"}}
<p>The End</p>
{{ end }}
~~~

By default, the template is not required to define all partials referenced in the
layout. If you want an error to be returned when a template does not define a
partial, set `Options.RequirePartials = true`.

### Character Encodings
Render will automatically set the proper Content-Type header based on which function you call. See below for an example of what the default settings would output (note that UTF-8 is the default, and binary data does not output the charset):
~~~ go
// main.go
package main

import (
    "encoding/xml"
    "net/http"

    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

type ExampleXml struct {
    XMLName xml.Name `xml:"example"`
    One     string   `xml:"one,attr"`
    Two     string   `xml:"two,attr"`
}

func main() {
    r := render.New(render.Options{})
    mux := http.NewServeMux()

    // This will set the Content-Type header to "application/octet-stream".
    // Note that this does not receive a charset value.
    mux.HandleFunc("/data", func(w http.ResponseWriter, req *http.Request) {
        r.Data(w, http.StatusOK, []byte("Some binary data here."))
    })

    // This will set the Content-Type header to "application/json; charset=UTF-8".
    mux.HandleFunc("/json", func(w http.ResponseWriter, req *http.Request) {
        r.JSON(w, http.StatusOK, map[string]string{"hello": "json"})
    })

    // This will set the Content-Type header to "text/xml; charset=UTF-8".
    mux.HandleFunc("/xml", func(w http.ResponseWriter, req *http.Request) {
        r.XML(w, http.StatusOK, ExampleXml{One: "hello", Two: "xml"})
    })

    // This will set the Content-Type header to "text/plain; charset=UTF-8".
    mux.HandleFunc("/text", func(w http.ResponseWriter, req *http.Request) {
        r.Text(w, http.StatusOK, "Plain text here")
    })

    // This will set the Content-Type header to "text/html; charset=UTF-8".
    mux.HandleFunc("/html", func(w http.ResponseWriter, req *http.Request) {
        // Assumes you have a template in ./templates called "example.tmpl"
        // $ mkdir -p templates && echo "<h1>Hello {{.}}.</h1>" > templates/example.tmpl
        r.HTML(w, http.StatusOK, "example", "World")
    })

    http.ListenAndServe("127.0.0.1:3000", mux)
}
~~~

In order to change the charset, you can set the `Charset` within the `render.Options` to your encoding value:
~~~ go
// main.go
package main

import (
    "encoding/xml"
    "net/http"

    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

type ExampleXml struct {
    XMLName xml.Name `xml:"example"`
    One     string   `xml:"one,attr"`
    Two     string   `xml:"two,attr"`
}

func main() {
    r := render.New(render.Options{
        Charset: "ISO-8859-1",
    })
    mux := http.NewServeMux()

    // This will set the Content-Type header to "application/octet-stream".
    // Note that this does not receive a charset value.
    mux.HandleFunc("/data", func(w http.ResponseWriter, req *http.Request) {
        r.Data(w, http.StatusOK, []byte("Some binary data here."))
    })

    // This will set the Content-Type header to "application/json; charset=ISO-8859-1".
    mux.HandleFunc("/json", func(w http.ResponseWriter, req *http.Request) {
        r.JSON(w, http.StatusOK, map[string]string{"hello": "json"})
    })

    // This will set the Content-Type header to "text/xml; charset=ISO-8859-1".
    mux.HandleFunc("/xml", func(w http.ResponseWriter, req *http.Request) {
        r.XML(w, http.StatusOK, ExampleXml{One: "hello", Two: "xml"})
    })

    // This will set the Content-Type header to "text/plain; charset=ISO-8859-1".
    mux.HandleFunc("/text", func(w http.ResponseWriter, req *http.Request) {
        r.Text(w, http.StatusOK, "Plain text here")
    })

    // This will set the Content-Type header to "text/html; charset=ISO-8859-1".
    mux.HandleFunc("/html", func(w http.ResponseWriter, req *http.Request) {
        // Assumes you have a template in ./templates called "example.tmpl"
        // $ mkdir -p templates && echo "<h1>Hello {{.}}.</h1>" > templates/example.tmpl
        r.HTML(w, http.StatusOK, "example", "World")
    })

    http.ListenAndServe("127.0.0.1:3000", mux)
}
~~~

### Error Handling

The rendering functions return any errors from the rendering engine.
By default, they will also write the error to the HTTP response and set the status code to 500. You can disable
this behavior so that you can handle errors yourself by setting
`Options.DisableHTTPErrorRendering: true`.

~~~go
r := render.New(render.Options{
  DisableHTTPErrorRendering: true,
})

//...

err := r.HTML(w, http.StatusOK, "example", "World")
if err != nil{
  http.Redirect(w, r, "/my-custom-500", http.StatusFound)
}
~~~

## Integration Examples

### [Echo](https://github.com/labstack/echo)
~~~ go
// main.go
package main

import (
    "io"
    "net/http"

    "github.com/labstack/echo"
    "github.com/labstack/echo/engine/standard"
    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

type RenderWrapper struct { // We need to wrap the renderer because we need a different signature for echo.
    rnd *render.Render
}

func (r *RenderWrapper) Render(w io.Writer, name string, data interface{},c echo.Context) error {
    return r.rnd.HTML(w, 0, name, data) // The zero status code is overwritten by echo.
}

func main() {
    r := &RenderWrapper{render.New()}

    e := echo.New()

    e.SetRenderer(r)
    
    e.GET("/", func(c echo.Context) error {
        return c.Render(http.StatusOK, "TemplateName", "TemplateData")
    })

    e.Run(standard.New(":1323"))
}
~~~

### [Gin](https://github.com/gin-gonic/gin)
~~~ go
// main.go
package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

func main() {
    r := render.New(render.Options{
        IndentJSON: true,
    })

    router := gin.Default()

    router.GET("/", func(c *gin.Context) {
        r.JSON(c.Writer, http.StatusOK, map[string]string{"welcome": "This is rendered JSON!"})
    })

    router.Run(":3000")
}
~~~

### [Goji](https://github.com/zenazn/goji)
~~~ go
// main.go
package main

import (
    "net/http"

    "github.com/zenazn/goji"
    "github.com/zenazn/goji/web"
    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

func main() {
    r := render.New(render.Options{
        IndentJSON: true,
    })

    goji.Get("/", func(c web.C, w http.ResponseWriter, req *http.Request) {
        r.JSON(w, http.StatusOK, map[string]string{"welcome": "This is rendered JSON!"})
    })
    goji.Serve()  // Defaults to ":8000".
}
~~~

### [Negroni](https://github.com/codegangsta/negroni)
~~~ go
// main.go
package main

import (
    "net/http"

    "github.com/codegangsta/negroni"
    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

func main() {
    r := render.New(render.Options{
        IndentJSON: true,
    })
    mux := http.NewServeMux()

    mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
        r.JSON(w, http.StatusOK, map[string]string{"welcome": "This is rendered JSON!"})
    })

    n := negroni.Classic()
    n.UseHandler(mux)
    n.Run(":3000")
}
~~~

### [Traffic](https://github.com/pilu/traffic)
~~~ go
// main.go
package main

import (
    "net/http"

    "github.com/pilu/traffic"
    "github.com/unrolled/render"  // or "gopkg.in/unrolled/render.v1"
)

func main() {
    r := render.New(render.Options{
        IndentJSON: true,
    })

    router := traffic.New()
    router.Get("/", func(w traffic.ResponseWriter, req *traffic.Request) {
        r.JSON(w, http.StatusOK, map[string]string{"welcome": "This is rendered JSON!"})
    })

    router.Run()
}
~~~
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
| [PostgreSQL](https://github.com/gemnasium/logrus-postgresql-hook) | Send logs to [PostgreSQL](http://postgresql.org) |


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
<img alt="chi" src="https://cdn.rawgit.com/pressly/chi/master/_examples/chi.svg" width="220" />
===

[![GoDoc Widget]][GoDoc] [![Travis Widget]][Travis]

`chi` is a lightweight, idiomatic and composable router for building Go 1.7+ HTTP services. It's
especially good at helping you write large REST API services that are kept maintainable as your
project grows and changes. `chi` is built on the new `context` package introduced in Go 1.7 to
handle signaling, cancelation and request-scoped values across a handler chain.

The focus of the project has been to seek out an elegant and comfortable design for writing
REST API servers, written during the development of the Pressly API service that powers our
public API service, which in turn powers all of our client-side applications.

The key considerations of chi's design are: project structure, maintainability, standard http
handlers (stdlib-only), developer productivity, and deconstructing a large system into many small
parts. The core router `github.com/pressly/chi` is quite small (less than 1000 LOC), but we've also
included some useful/optional subpackages: `middleware`, `render` and `docgen`. We hope you enjoy it too!


## Features

* **Lightweight** - cloc'd in <1000 LOC for the chi router
* **Fast** - yes, see [benchmarks](#benchmarks)
* **100% compatible with net/http** - use any http or middleware pkg in the ecosystem that is also compat with `net/http`
* **Designed for modular/composable APIs** - middlewares, inline middlewares, route groups and subrouter mounting
* **Context control** - built on new `context` package, providing value chaining, cancelations and timeouts
* **Robust** - tested / used in production at Pressly.com, and many others
* **Doc generation** - `docgen` auto-generates routing documentation from your source to JSON or Markdown
* **No external dependencies** - plain ol' Go 1.7+ stdlib + net/http


## Examples

* [rest](https://github.com/pressly/chi/blob/master/_examples/rest/main.go) - REST APIs made easy, productive and maintainable
* [logging](https://github.com/pressly/chi/blob/master/_examples/logging/main.go) - Easy structured logging for any backend
* [limits](https://github.com/pressly/chi/blob/master/_examples/limits/main.go) - Timeouts and Throttling
* [todos-resource](https://github.com/pressly/chi/blob/master/_examples/todos-resource/main.go) - Struct routers/handlers, an example of another code layout style
* [versions](https://github.com/pressly/chi/blob/master/_examples/versions/main.go) - Demo of `chi/render` subpkg
* [fileserver](https://github.com/pressly/chi/blob/master/_examples/fileserver/main.go) - Easily serve static files
* [graceful](https://github.com/pressly/chi/blob/master/_examples/graceful/main.go) - Graceful context signaling and server shutdown


**As easy as:**

```go
package main

import (
	"net/http"
	"github.com/pressly/chi"
)

func main() {
	r := chi.NewRouter()
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("welcome"))
	})
	http.ListenAndServe(":3000", r)
}
```

**REST Preview:**

Here is a little preview of how routing looks like with chi. Also take a look at the generated routing docs
in JSON ([routes.json](https://github.com/pressly/chi/blob/master/_examples/rest/routes.json)) and in
Markdown ([routes.md](https://github.com/pressly/chi/blob/master/_examples/rest/routes.md)).

I highly recommend reading the source of the [examples](#examples) listed above, they will show you all the features
of chi and serve as a good form of documentation.

```go
import (
  //...
  "context"
  "github.com/pressly/chi"
  "github.com/pressly/chi/middleware"
)

func main() {
  r := chi.NewRouter()

  // A good base middleware stack
  r.Use(middleware.RequestID)
  r.Use(middleware.RealIP)
  r.Use(middleware.Logger)
  r.Use(middleware.Recoverer)

  // When a client closes their connection midway through a request, the
  // http.CloseNotifier will cancel the request context (ctx).
  r.Use(middleware.CloseNotify)

  // Set a timeout value on the request context (ctx), that will signal
  // through ctx.Done() that the request has timed out and further
  // processing should be stopped.
  r.Use(middleware.Timeout(60 * time.Second))

  r.Get("/", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("hi"))
  })

  // RESTy routes for "articles" resource
  r.Route("/articles", func(r chi.Router) {
    r.With(paginate).Get("/", listArticles)  // GET /articles
    r.Post("/", createArticle)               // POST /articles
    r.Get("/search", searchArticles)         // GET /articles/search

    r.Route("/:articleID", func(r chi.Router) {
      r.Use(ArticleCtx)
      r.Get("/", getArticle)                 // GET /articles/123
      r.Put("/", updateArticle)              // PUT /articles/123
      r.Delete("/", deleteArticle)           // DELETE /articles/123
    })
  })

  // Mount the admin sub-router
  r.Mount("/admin", adminRouter())

  http.ListenAndServe(":3333", r)
}

func ArticleCtx(next http.Handler) http.Handler {
  return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    articleID := chi.URLParam(r, "articleID")
    article, err := dbGetArticle(articleID)
    if err != nil {
      http.Error(w, http.StatusText(404), 404)
      return
    }
    ctx := context.WithValue(r.Context(), "article", article)
    next.ServeHTTP(w, r.WithContext(ctx))
  })
}

func getArticle(w http.ResponseWriter, r *http.Request) {
  ctx := r.Context()
  article, ok := ctx.Value("article").(*Article)
  if !ok {
    http.Error(w, http.StatusText(422), 422)
    return
  }
  w.Write([]byte(fmt.Sprintf("title:%s", article.Title)))
}

// A completely separate router for administrator routes
func adminRouter() http.Handler {
  r := chi.NewRouter()
  r.Use(AdminOnly)
  r.Get("/", adminIndex)
  r.Get("/accounts", adminListAccounts)
  return r
}

func AdminOnly(next http.Handler) http.Handler {
  return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    perm, ok := ctx.Value("acl.permission").(YourPermissionType)
    if !ok || !perm.IsAdmin() {
      http.Error(w, http.StatusText(403), 403)
      return
    }
    next.ServeHTTP(w, r)
  })
}
```


## Router design

chi's router is based on a kind of [Patricia Radix trie](https://en.wikipedia.org/wiki/Radix_tree).
The router is fully compatible with `net/http`.

Built on top of the tree is the `Router` interface:

```go
// Router consisting of the core routing methods used by chi's Mux,
// using only the standard net/http.
type Router interface {
	http.Handler
	Routes

	// Use appends one of more middlewares onto the Router stack.
	Use(middlewares ...func(http.Handler) http.Handler)

	// With adds inline middlewares for an endpoint handler.
	With(middlewares ...func(http.Handler) http.Handler) Router

	// Group adds a new inline-Router along the current routing
	// path, with a fresh middleware stack for the inline-Router.
	Group(fn func(r Router)) Router

	// Route mounts a sub-Router along a `pattern`` string.
	Route(pattern string, fn func(r Router)) Router

	// Mount attaches another http.Handler along ./pattern/*
	Mount(pattern string, h http.Handler)

	// Handle and HandleFunc adds routes for `pattern` that matches
	// all HTTP methods.
	Handle(pattern string, h http.Handler)
	HandleFunc(pattern string, h http.HandlerFunc)

	// HTTP-method routing along `pattern`
	Connect(pattern string, h http.HandlerFunc)
	Delete(pattern string, h http.HandlerFunc)
	Get(pattern string, h http.HandlerFunc)
	Head(pattern string, h http.HandlerFunc)
	Options(pattern string, h http.HandlerFunc)
	Patch(pattern string, h http.HandlerFunc)
	Post(pattern string, h http.HandlerFunc)
	Put(pattern string, h http.HandlerFunc)
	Trace(pattern string, h http.HandlerFunc)

	// NotFound defines a handler to respond whenever a route could
	// not be found.
	NotFound(h http.HandlerFunc)
}

// Routes interface adds two methods for router traversal, which is also
// used by the `docgen` subpackage to generation documentation for Routers.
type Routes interface {
	// Routes returns the routing tree in an easily traversable structure.
	Routes() []Route

	// Middlewares returns the list of middlewares in use by the router.
	Middlewares() Middlewares
}
```

Each routing method accepts a URL `pattern` and chain of `handlers`. The URL pattern
supports named params (ie. `/users/:userID`) and wildcards (ie. `/admin/*`).


### Middleware handlers

chi's middlewares are just stdlib net/http middleware handlers. There is nothing special
about them, which means the router and all the tooling is designed to be compatible and
friendly with any middleware in the community. This offers much better extensibility and reuse
of packages and is at the heart of chi's purpose.

Here is an example of a standard net/http middleware handler using the new request context
available in Go 1.7+. This middleware sets a hypothetical user identifier on the request
context and calls the next handler in the chain.

```go
// HTTP middleware setting a value on the request context
func MyMiddleware(next http.Handler) http.Handler {
  return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    ctx := context.WithValue(r.Context(), "user", "123")
    next.ServeHTTP(w, r.WithContext(ctx))
  })
}
```


### Request handlers

chi uses standard net/http request handlers. This little snippet is an example of a http.Handler
func that reads a user identifier from the request context - hypothetically, identifying
the user sending an authenticated request, validated+set by a previous middleware handler.

```go
// HTTP handler accessing data from the request context.
func MyRequestHandler(w http.ResponseWriter, r *http.Request) {
  user := r.Context().Value("user").(string)
  w.Write([]byte(fmt.Sprintf("hi %s", user)))
}
```


### URL parameters

chi's router parses and stores URL parameters right onto the request context. Here is
an example of how to access URL params in your net/http handlers. And of course, middlewares
are able to access the same information.

```go
// HTTP handler accessing the url routing parameters.
func MyRequestHandler(w http.ResponseWriter, r *http.Request) {
  userID := chi.URLParam(r, "userID") // from a route like /users/:userID

  ctx := r.Context()
  key := ctx.Value("key").(string)

  w.Write([]byte(fmt.Sprintf("hi %v, %v", userID, key)))
}
```


## Middlewares

chi comes equipped with an optional `middleware` package, providing a suite of standard
`net/http` middlewares. Please note, any middleware in the ecosystem that is also compatible
with `net/http` can be used with chi's mux.

--------------------------------------------------------------------------------------------------
| Middleware   | Description                                                                     |
|:-------------|:---------------------------------------------------------------------------------
| RequestID    | Injects a request ID into the context of each request.                          |
| RealIP       | Sets a http.Request's RemoteAddr to either X-Forwarded-For or X-Real-IP.        |
| Logger       | Logs the start and end of each request with the elapsed processing time.        |
| Recoverer    | Gracefully absorb panics and prints the stack trace.                            |
| NoCache      | Sets response headers to prevent clients from caching.                          |
| CloseNotify  | Signals to the request context when a client has closed their connection.       |
| Timeout      | Signals to the request context when the timeout deadline is reached.            |
| Throttle     | Puts a ceiling on the number of concurrent requests.                            |
| Compress     | Gzip compression for clients that accept compressed responses.                  |
| Profiler     | Easily attach net/http/pprof to your routers.                                   |
| Slashes      | Strip and redirect slashes on routing paths.                                    |
| WithValue    | Short-hand middleware to set a key/value on the request context.                |
| Heartbeat    | Monitoring endpoint to check the servers pulse.                                 |
--------------------------------------------------------------------------------------------------

Other cool net/http middlewares:

* [jwtauth](https://github.com/goware/jwtauth) - JWT authenticator
* [cors](https://github.com/goware/cors) - CORS middleware
* [httpcoala](https://github.com/goware/httpcoala) - Request coalescer

please [submit a PR](./CONTRIBUTING.md) if you'd like to include a link to a chi middleware


## context?

`context` is a tiny pkg that provides simple interface to signal context across call stacks
and goroutines. It was originally written by [Sameer Ajmani](https://github.com/Sajmani)
and is available in stdlib since go1.7.

Learn more at https://blog.golang.org/context

and..
* Docs: https://golang.org/pkg/context
* Source: https://github.com/golang/go/tree/master/src/context


## Benchmarks

The benchmark suite: https://github.com/pkieltyka/go-http-routing-benchmark

Comparison with other routers (as of Aug 1/16): https://gist.github.com/pkieltyka/76a59d33492dd2732e691ad8c0b274a4

```shell
BenchmarkChi_Param        	 5000000	       251 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_Param5       	 5000000	       393 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_Param20      	 1000000	      1012 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_ParamWrite   	 5000000	       301 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_GithubStatic 	 5000000	       287 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_GithubParam  	 3000000	       442 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_GithubAll    	   20000	     90855 ns/op	   48723 B/op	     203 allocs/op
BenchmarkChi_GPlusStatic  	 5000000	       250 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_GPlusParam   	 5000000	       280 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_GPlus2Params 	 5000000	       337 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_GPlusAll     	  300000	      4128 ns/op	    3120 B/op	      13 allocs/op
BenchmarkChi_ParseStatic  	 5000000	       250 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_ParseParam   	 5000000	       275 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_Parse2Params 	 5000000	       305 ns/op	     240 B/op	       1 allocs/op
BenchmarkChi_ParseAll     	  200000	      7671 ns/op	    6240 B/op	      26 allocs/op
BenchmarkChi_StaticAll    	   30000	     55497 ns/op	   37682 B/op	     157 allocs/op
```

NOTE: the allocs in the benchmark above are from the calls to http.Request's
`WithContext(context.Context)` method that clones the http.Request, sets the `Context()`
on the duplicated (alloc'd) request and returns it the new request object. This is just
how setting context on a request in Go 1.7 works. 


## Credits

* Carl Jackson for https://github.com/zenazn/goji
  * Parts of chi's thinking comes from goji, and chi's middleware package
    sources from goji.
* Armon Dadgar for https://github.com/armon/go-radix
* Contributions: [@VojtechVitek](https://github.com/VojtechVitek)

We'll be more than happy to see [your contributions](./CONTRIBUTING.md)!


## Beyond REST

chi is just a http router that lets you decompose request handling into many smaller layers.
Many companies including Pressly.com (of course) use chi to write REST services for their public
APIs. But, REST is just a convention for managing state via HTTP, and there's a lot of other pieces
required to write a complete client-server system or network of microservices.

Looking ahead beyond REST, I also recommend some newer works in the field coming from
[gRPC](https://github.com/grpc/grpc-go), [NATS](https://nats.io), [go-kit](https://github.com/go-kit/kit)
and even [graphql](https://github.com/graphql-go/graphql). They're all pretty cool with their
own unique approaches and benefits. Specifically, I'd look at gRPC since it makes client-server
communication feel like a single program on a single computer, no need to hand-write a client library
and the request/response payloads are typed contracts. NATS is pretty amazing too as a super
fast and lightweight pub-sub transport that can speak protobufs, with nice service discovery - 
an excellent combination with gRPC.


## License

Copyright (c) 2015-present [Peter Kieltyka](https://github.com/pkieltyka)

Licensed under [MIT License](./LICENSE)

[GoDoc]: https://godoc.org/github.com/pressly/chi
[GoDoc Widget]: https://godoc.org/github.com/pressly/chi?status.svg
[Travis]: https://travis-ci.org/pressly/chi
[Travis Widget]: https://travis-ci.org/pressly/chi.svg?branch=master
# Consistent Road

Go net/http middleware that turns your http server into a basic load balancer based
on a consistent hash-ring scheme. Most balancers are just round-robin, but for
http apps that are a bit more intensive to compute something, and perhaps with some local
caching on that node, Consistent Rd will distribute the requests to the same nodes
that originally processed it on the cluster. For ex, an image resizing server with locally
cached image sizes.

This adds a bit of overhead to your response since it'll have to balance/proxy the request
to the other nodes on the cluster. On my system I've found it to be marginal though,
about 0.5 to 1 ms. 

## License

Copyright (c) 2014 Peter Kieltyka / Pressly Inc. www.pressly.com

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Chainstore

Chainstore is simple key-value interface to a variety of storage engines
organized as a chain of operations. A store adapter is just an engine interface
to `Open`, `Close`, `Put`, `Get`, and `Del` . Each store has their own inherent
properties and so when chained together, it makes for a useful combinations of
data caching, flow and persistence depending on your application.

Here is an example of Boltdb and S3 stores chained together to provide fast
read/writes to a local working dataset of 500MB and async S3 access for
long-term persistence / retrieval. Check out the LRUManager below too, its
wrapped around Boltdb to make sure only the least-recently-used key/values are
persisted -- the manager can be used with any of the stores and with the chain,
which is pretty nifty. This example is also here:
[example/main.go](example/main.go).

```go
package main

import (
	"fmt"
	"os"
	"time"
	"log"

	"github.com/pressly/chainstore"
	"github.com/pressly/chainstore/boltstore"
	"github.com/pressly/chainstore/lrumgr"
	"github.com/pressly/chainstore/metricsmgr"
	"github.com/pressly/chainstore/s3store"
	"golang.org/x/net/context"
)

var (
	bucketID  string
	accessKey string
	secretKey string
)

func init() {
	bucketID = os.Getenv("S3_BUCKET")
	accessKey = os.Getenv("S3_ACCESS_KEY")
	secretKey = os.Getenv("S3_SECRET_KEY")
}

func main() {
	ctx := context.Background()

	diskStore := lrumgr.New(500*1024*1024, // 500MB of working data
		metricsmgr.New("chainstore.ex.bolt",
			boltstore.New("/tmp/store.db", "myBucket"),
		),
	)

	remoteStore := metricsmgr.New("chainstore.ex.s3",
		// NOTE: you'll have to supply your own keys in order for this example to work properly
		s3store.New(bucketID, accessKey, secretKey),
	)

	dataStore := chainstore.New(diskStore, remoteStore)

	// OR.. define inline. Except, I wanted to show store independence & state.
	/*
		dataStore := chainstore.New(
			lrumgr.New(500*1024*1024, // 500MB of working data
				metricsmgr.New("chainstore.ex.bolt",
					boltstore.New("/tmp/store.db", "myBucket"),
				),
			),
			metricsmgr.New("chainstore.ex.s3",
				// NOTE: you'll have to supply your own keys in order for this example to work properly
				s3store.New("myBucket", "access-key", "secret-key"),
			),
		)
	*/

	var err error

	err = dataStore.Open()
	if err != nil {
		log.Fatalf("Open: %q", err)
	}

	// Since we've used the metricsManager above (metricsmgr), any calls to the boltstore
	// and s3store will be measured. Next is to send metrics to librato, graphite, influxdb,
	// whatever.. via github.com/goware/go-metrics
	// go librato.Librato(metrics.DefaultRegistry, 10e9, ...)

	//--

	// Save the object in the chain. It will be Put() synchronously into diskStore,
	// the boltdb engine, and then immediately dispatch background Put()'s to the
	// other stores down the chain, in this case S3.
	fmt.Println("Example 1...")
	obj := []byte{1, 2, 3}
	err = dataStore.Put(ctx, "k", obj)
	if err != nil {
		log.Fatalf("Put: %q", err)
	}
	fmt.Println("Put 'k':", obj, "in the chain")

	v, err := dataStore.Get(ctx, "k")
	if err != nil {
		log.Fatalf("Put: %q", err)
	}
	fmt.Println("Grabbing 'k' from the chain:", v) // => [1 2 3]

	// For demonstration, let's grab the key directly from the store instead of
	// through the chain. This is pretty much the same as above, as the chain's Get()
	// stops once it finds the object.
	v, err = diskStore.Get(ctx, "k")
	if err != nil {
		log.Fatalf("Put: %q", err)
	}
	fmt.Println("Grabbing 'k' directly from boltdb:", v) // => [1 2 3]

	// lets pause for a moment and then try to retrieve the value from the s3 store
	time.Sleep(1e9)

	// Grab the object from s3
	v, err = remoteStore.Get(ctx, "k")
	if err != nil {
		log.Fatalf("Put: %q", err)
	}
	fmt.Println("Grabbing 'k' directly from s3:", v) // => [1 2 3]

	// Delete the object from everywhere
	dataStore.Del(ctx, "k")
	time.Sleep(1e9) // pause for s3 demo
	v, _ = dataStore.Get(ctx, "k")
	fmt.Println("Deleted 'k' from the chain (all stores). Get(k) returns:", v)

	//--

	// Another interesting behavior of the chain is when doing a Get(), it goes down
	// the entire chain looking for the value, and when found, it will Put() that
	// object back up the chain for subsequent retrievals. Lets see..
	fmt.Println("Example 2...")
	obj = []byte("hope you enjoy")
	err = dataStore.Put(ctx, "hi", obj)
	if err != nil {
		log.Fatalf("Put: %q", err)
	}
	fmt.Println("Put 'hi':", obj, "in the chain")
	time.Sleep(1e9) // lets wait for s3 again with more then enough time

	err = diskStore.Del(ctx, "hi")
	if err != nil {
		log.Fatalf("Get: %q", err)
	}

	v, _ = diskStore.Get(ctx, "hi")
	fmt.Println("Delete 'hi' from boltdb. diskStore.Get(k) returns:", v)

	v, err = dataStore.Get(ctx, "hi")
	if err != nil {
		log.Fatalf("Get: %q", err)
	}
	fmt.Println("Let's ask the chain for 'hi':", v)
	time.Sleep(1e9) // pause for bg routine to fill our local cache

	// The diskStore now has the value again from remoteStore lower down the chain.
	v, err = diskStore.Get(ctx, "hi")
	if err != nil {
		log.Fatalf("Get: %q", err)
	}
	fmt.Println("Now, let's ask our diskStore again! diskStore.Get(k) returns:", v)

	// Also.. even though it hasn't been demonstrated here, the diskStore will only
	// store a max of 500MB (as defined with diskLru) worth of objects. Give it a shot.
}

/* OUTPUT:

Example 1...
Put 'k': [1 2 3] in the chain
Grabbing 'k' from the chain: [1 2 3]
Grabbing 'k' directly from boltdb: [1 2 3]
Grabbing 'k' directly from s3: [1 2 3]
Deleted 'k' from the chain (all stores). Get(k) returns: []
Example 2...
Put 'hi': [104 111 112 101 32 121 111 117 32 101 110 106 111 121] in the chain
Delete 'hi' from boltdb. diskStore.Get(k) returns: []
Let's ask the chain for 'hi': [104 111 112 101 32 121 111 117 32 101 110 106 111 121]
Now, let's ask our diskStore again! diskStore.Get(k) returns: [104 111 112 101 32 121 111 117 32 101 110 106 111 121]

*/
```

Currently supported stores: memory, filesystem, boltdb, leveldb, s3, a lru
manager, and a metrics manager that can be layered ontop. You can chain these
together for different behaviours, for example the `memstore` implementation is
just a simple `map[string][]byte` with the LRU cache manager (`lrumgr`).

Thx to other great projects:

- [github.com/boltdb/bolt](https://github.com/boltdb/bolt)
- [github.com/mitchellh/goamz](https://github.com/mitchellh/goamz)
- [github.com/syndtr/goleveldb](https://github.com/syndtr/goleveldb)

## Changelog

- Oct 2015. Added support for
  [context.Context](https://godoc.org/golang.org/x/net/context). Please
  checkout tag
  [before-context](https://github.com/pressly/chainstore/tree/before-context)
  to browse the original source tree.

# TODO / Ideas

- Error channel where bad puts are communicated so they can be properly handled
	further down the chain

- Idea: provide option to hash the input keys which would make each key
	fixed-length and smaller footprint everywhere

- Timeout (with error notification) when adding an item to a store (ie. 60
	seconds max to confirm)

- Consider a 'config' structure to pass to stores that can configure things
	like:
		* For s3 store, add ACL with options: private, public_read,
			public_read_write, authenticated_read

## License

> Copyright (c) 2014-2015 Peter Kieltyka / Pressly Inc. www.pressly.com
>
> MIT License
>
> Permission is hereby granted, free of charge, to any person obtaining
> a copy of this software and associated documentation files (the
> "Software"), to deal in the Software without restriction, including
> without limitation the rights to use, copy, modify, merge, publish,
> distribute, sublicense, and/or sell copies of the Software, and to
> permit persons to whom the Software is furnished to do so, subject to
> the following conditions:
>
> The above copyright notice and this permission notice shall be
> included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
> NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
> LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
> OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
> WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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

Bolt [![Coverage Status](https://coveralls.io/repos/boltdb/bolt/badge.svg?branch=master)](https://coveralls.io/r/boltdb/bolt?branch=master) [![GoDoc](https://godoc.org/github.com/boltdb/bolt?status.svg)](https://godoc.org/github.com/boltdb/bolt) ![Version](https://img.shields.io/badge/version-1.2.1-green.svg)
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

Bolt is stable, the API is fixed, and the file format is fixed. Full unit
test coverage and randomized black box testing are used to ensure database
consistency and thread safety. Bolt is currently used in high-load production
environments serving databases as large as 1TB. Many companies such as
Shopify and Heroku use Bolt-backed services every day.

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
You can use the `DB.Begin()` function directly but **please** be sure to close
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
        id, _ := b.NextSequence()
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

Please note that keys and values in `ForEach()` are only valid while
the transaction is open. If you need to use a key or value outside of
the transaction, you must use `copy()` to copy it to another byte
slice.

### Nested buckets

You can also store a bucket in a key to create nested buckets. The API is the
same as the bucket management API on the `DB` object:

```go
func (*Bucket) CreateBucket(key []byte) (*Bucket, error)
func (*Bucket) CreateBucketIfNotExists(key []byte) (*Bucket, error)
func (*Bucket) DeleteBucket(key []byte) error
```

Say you had a multi-tenant application where the root level bucket was the account bucket. Inside of this bucket was a sequence of accounts which themselves are buckets. And inside the sequence bucket you could have many buckets pertaining to the Account itself (Users, Notes, etc) isolating the information into logical groupings.

```go

// createUser creates a new user in the given account.
func createUser(accountID int, u *User) error {
    // Start the transaction.
    tx, err := db.Begin(true)
    if err != nil {
        return err
    }
    defer tx.Rollback()

    // Retrieve the root bucket for the account.
    // Assume this has already been created when the account was set up.
    root := tx.Bucket([]byte(strconv.FormatUint(accountID, 10)))

    // Setup the users bucket.
    bkt, err := root.CreateBucketIfNotExists([]byte("USERS"))
    if err != nil {
        return err
    }

    // Generate an ID for the new user.
    userID, err := bkt.NextSequence()
    if err != nil {
        return err
    }
    u.ID = userID

    // Marshal and save the encoded user.
    if buf, err := json.Marshal(u); err != nil {
        return err
    } else if err := bkt.Put([]byte(strconv.FormatUint(u.ID, 10)), buf); err != nil {
        return err
    }

    // Commit the transaction.
    if err := tx.Commit(); err != nil {
        return err
    }

    return nil
}

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
constructor that takes in a filepath where the database file will be stored.
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

* [BoltDbWeb](https://github.com/evnix/boltdbweb) - A web based GUI for BoltDB files.
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
* [Storm](https://github.com/asdine/storm) - Simple and powerful ORM for BoltDB.
* [GoWebApp](https://github.com/josephspurrier/gowebapp) - A basic MVC web application in Go using BoltDB.
* [SimpleBolt](https://github.com/xyproto/simplebolt) - A simple way to use BoltDB. Deals mainly with strings.
* [Algernon](https://github.com/xyproto/algernon) - A HTTP/2 web server with built-in support for Lua. Uses BoltDB as the default database backend.
* [MuLiFS](https://github.com/dankomiocevic/mulifs) - Music Library Filesystem creates a filesystem to organise your music files.
* [GoShort](https://github.com/pankajkhairnar/goShort) - GoShort is a URL shortener written in Golang and BoltDB for persistent key/value storage and for routing it's using high performent HTTPRouter.
* [torrent](https://github.com/anacrolix/torrent) - Full-featured BitTorrent client package and utilities in Go. BoltDB is a storage backend in development.
* [gopherpit](https://github.com/gopherpit/gopherpit) - A web service to manage Go remote import paths with custom domains
* [bolter](https://github.com/hasit/bolter) - Command-line app for viewing BoltDB file in your terminal.
* [btcwallet](https://github.com/btcsuite/btcwallet) - A bitcoin wallet.
* [dcrwallet](https://github.com/decred/dcrwallet) - A wallet for the Decred cryptocurrency.
* [Ironsmith](https://github.com/timshannon/ironsmith) - A simple, script-driven continuous integration (build - > test -> release) tool, with no external dependencies
* [BoltHold](https://github.com/timshannon/bolthold) - An embeddable NoSQL store for Go types built on BoltDB

If you are using Bolt in a project please send a pull request to add it to the list.
consistent
==========

Consistent hash package for Go.

Installation
------------

    go get stathat.com/c/consistent

Examples
--------

Look at the [godoc](http://godoc.org/stathat.com/c/consistent).

Status
------

This package was extracted from production code powering [StatHat](http://www.stathat.com),
so clearly we feel that it is production-ready, but it should still be considered
experimental as other uses of it could reveal issues we aren't experiencing.

Contact us
----------

We'd love to hear from you if you are using `consistent`.
Get in touch:  [@stathat](http://twitter.com/stathat) or [contact us here](http://www.stathat.com/docs/contact).

About
-----

Written by Patrick Crosby at [StatHat](http://www.stathat.com).  Twitter:  [@stathat](http://twitter.com/stathat)
