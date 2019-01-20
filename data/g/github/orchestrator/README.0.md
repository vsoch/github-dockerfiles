Gcfg reads INI-style configuration files into Go structs;
supports user-defined types and subsections.

Package docs: https://godoc.org/gopkg.in/gcfg.v1
# bpool [![GoDoc](https://godoc.org/github.com/oxtoacart/bpool?status.png)](https://godoc.org/github.com/oxtoacart/bpool)

Package bpool implements leaky pools of byte arrays and Buffers as bounded channels. 
It is based on the leaky buffer example from the Effective Go documentation: http://golang.org/doc/effective_go.html#leaky_buffer

bpool provides the following pool types:

* [bpool.BufferPool](https://godoc.org/github.com/oxtoacart/bpool#BufferPool)
  which provides a fixed-size pool of
  [bytes.Buffers](http://golang.org/pkg/bytes/#Buffer).
* [bpool.BytePool](https://godoc.org/github.com/oxtoacart/bpool#BytePool) which
  provides a fixed-size pool of `[]byte` slices with a pre-set width (length).
* [bpool.SizedBufferPool](https://godoc.org/github.com/oxtoacart/bpool#SizedBufferPool), 
  which is an alternative to `bpool.BufferPool` that pre-sizes the capacity of
  buffers issued from the pool and discards buffers that have grown too large
  upon return.

A common use case for this package is to use buffers to execute HTML templates
against (via ExecuteTemplate) or encode JSON into (via json.NewEncoder). This
allows you to catch any rendering or marshalling errors prior to writing to a
`http.ResponseWriter`, which helps to avoid writing incomplete or malformed data
to the response.

## Install

`go get github.com/oxtoacart/bpool`

## Documentation

See [godoc.org](http://godoc.org/github.com/oxtoacart/bpool) or use `godoc github.com/oxtoacart/bpool`

## Example

Here's a quick example for using `bpool.BufferPool`. We create a pool of the
desired size, call the `Get()` method to obtain a buffer for use, and call
`Put(buf)` to return the buffer to the pool.

```go

var bufpool *bpool.BufferPool

func main() {

    bufpool = bpool.NewBufferPool(48)

}

func someFunction() error {

     // Get a buffer from the pool
     buf := bufpool.Get()
     ...
     ...
     ...
     // Return the buffer to the pool
     bufpool.Put(buf)

     return nil
}
```

## License

Apache 2.0 Licensed. See the LICENSE file for details.

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

* Can use this in multiple routines concurrently?

    Yes for readonly. But, No for writable. See #50, #51, #209.

* Why is it racy if I use a `sql.Open("sqlite", ":memory:")` database?

    Each connection to :memory: opens a brand new in-memory sql database, so if
    the stdlib's sql engine happens to open another connection and you've only
    specified ":memory:", that connection will see a brand new database. A
    workaround is to use "file::memory:?mode=memory&cache=shared". Every
    connection to this string will point to the same in-memory database. See
    #204 for more info.

License
-------

MIT: http://mattn.mit-license.org/2012

sqlite3-binding.c, sqlite3-binding.h, sqlite3ext.h

The -binding suffix was added to avoid build failures under gccgo.

In this repository, those files are an amalgamation of code that was copied from SQLite3. The license of that code is the same as the license of SQLite3.

Author
------

Yasuhiro Matsumoto (a.k.a mattn)
# Stats [![][travis-svg]][travis-url] [![][coveralls-svg]][coveralls-url] [![][godoc-svg]][godoc-url] [![][license-svg]][license-url]

A statistics package with many functions missing from the Golang standard library. See the [CHANGELOG.md](https://github.com/montanaflynn/stats/blob/master/CHANGELOG.md) for API changes and tagged releases you can vendor into your projects.

> Statistics are used much like a drunk uses a lamppost: for support, not illumination. **- Vin Scully**

## Installation

```
go get github.com/montanaflynn/stats
```

**Protip:** `go get -u github.com/montanaflynn/stats` updates stats to the latest version.

## Usage

The [entire API documentation](http://godoc.org/github.com/montanaflynn/stats) is available on GoDoc.org

You can view docs offline with the following commands:

```
godoc ./
godoc ./ Median
godoc ./ Float64Data
```

**Protip:** Generate HTML docs with `godoc -http=:4444`

## Example

All the functions can be seen in [examples/main.go](https://github.com/montanaflynn/stats/blob/master/examples/main.go) but here's a little taste:

```go
// start with the some source data to use
var data = []float64{1, 2, 3, 4, 4, 5}

median, _ := stats.Median(data)
fmt.Println(median) // 3.5

roundedMedian, _ := stats.Round(median, 0)
fmt.Println(roundedMedian) // 4
```

**Protip:** You can [call methods](https://github.com/montanaflynn/stats/blob/master/examples/methods.go) on the data if using the Float64Data type:

```
var d stats.Float64Data = data

max, _ := d.Max()
fmt.Println(max) // 5
```

## Contributing

If you have any suggestions, criticism or bug reports please [create an issue](https://github.com/montanaflynn/stats/issues) and I'll do my best to accommodate you. In addition simply starring the repo would show your support for the project and be very much appreciated!

### Pull Requests

Pull request are always welcome no matter how big or small. Here's an easy way to do it:

1. Fork it and clone your fork
2. Create new branch (`git checkout -b some-thing`)
3. Make the desired changes
4. Ensure tests pass (`go test -cover` or `make test`)
5. Commit changes (`git commit -am 'Did something'`)
6. Push branch (`git push origin some-thing`)
7. Submit pull request

To make things as seamless as possible please also consider the following steps:

- Update `README.md` to include new public types or functions in the documentation section.
- Update `examples/main.go` with a simple example of the new feature.
- Keep 100% code coverage (you can check with `make coverage`).
- Run [`gometalinter`](https://github.com/alecthomas/gometalinter) and make your code pass.
- Squash needless commits into single units of work with `git rebase -i new-feature`.

#### Makefile

I've included a [Makefile](https://github.com/montanaflynn/stats/blob/master/Makefile) that has a lot of helper targets for common actions such as linting, testing, code coverage reporting and more.

**Protip:** `watch -n 1 make check` will continuously format and test your code.

## MIT License

Copyright (c) 2014-2015 Montana Flynn <http://anonfunction.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORpublicS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[travis-url]: https://travis-ci.org/montanaflynn/stats
[travis-svg]: https://img.shields.io/travis/montanaflynn/stats.svg

[coveralls-url]: https://coveralls.io/r/montanaflynn/stats?branch=master
[coveralls-svg]: https://img.shields.io/coveralls/montanaflynn/stats.svg

[godoc-url]: https://godoc.org/github.com/montanaflynn/stats
[godoc-svg]: https://godoc.org/github.com/montanaflynn/stats?status.svg

[license-url]: https://github.com/montanaflynn/stats/blob/master/LICENSE
[license-svg]: https://img.shields.io/badge/license-MIT-blue.svg
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

**NOTE:** The martini framework is no longer maintained.

Martini is a powerful package for quickly writing modular web applications/services in Golang.

Language Translations:
* [繁體中文](translations/README_zh_tw.md)
* [简体中文](translations/README_zh_cn.md)
* [Português Brasileiro (pt_BR)](translations/README_pt_br.md)
* [Español](translations/README_es_ES.md)
* [한국어 번역](translations/README_ko_kr.md)
* [Русский](translations/README_ru_RU.md)
* [日本語](translations/README_ja_JP.md)
* [French](translations/README_fr_FR.md)
* [Turkish](translations/README_tr_TR.md)
* [German](translations/README_de_DE.md)
* [Polski](translations/README_pl_PL.md)

## Getting Started

After installing Go and setting up your [GOPATH](http://golang.org/doc/code.html#GOPATH), create your first `.go` file. We'll call it `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

Then install the Martini package (**go 1.1** or greater is required):
~~~
go get github.com/go-martini/martini
~~~

Then run your server:
~~~
go run server.go
~~~

You will now have a Martini webserver running on `localhost:3000`.

## Getting Help

Join the [Mailing list](https://groups.google.com/forum/#!forum/martini-go)

Watch the [Demo Video](http://martini.codegangsta.io/#demo)

Ask questions on Stackoverflow using the [martini tag](http://stackoverflow.com/questions/tagged/martini)

GoDoc [documentation](http://godoc.org/github.com/go-martini/martini)


## Features
* Extremely simple to use.
* Non-intrusive design.
* Plays nice with other Golang packages.
* Awesome path matching and routing.
* Modular design - Easy to add functionality, easy to rip stuff out.
* Lots of good handlers/middlewares to use.
* Great 'out of the box' feature set.
* **Fully compatible with the [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc) interface.**
* Default document serving (e.g., for serving AngularJS apps in HTML5 mode).

## More Middleware
For more middleware and functionality, check out the repositories in the  [martini-contrib](https://github.com/martini-contrib) organization.

## Table of Contents
* [Classic Martini](#classic-martini)
  * [Handlers](#handlers)
  * [Routing](#routing)
  * [Services](#services)
  * [Serving Static Files](#serving-static-files)
* [Middleware Handlers](#middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
To get up and running quickly, [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) provides some reasonable defaults that work well for most web applications:
~~~ go
  m := martini.Classic()
  // ... middleware and routing goes here
  m.Run()
~~~

Below is some of the functionality [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) pulls in automatically:
  * Request/Response Logging - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Static File serving - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routing - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Handlers
Handlers are the heart and soul of Martini. A handler is basically any kind of callable function:
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Return Values
If a handler returns something, Martini will write the result to the current [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) as a string:
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

You can also optionally return a status code:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### Service Injection
Handlers are invoked via reflection. Martini makes use of *Dependency Injection* to resolve dependencies in a Handlers argument list. **This makes Martini completely  compatible with golang's `http.HandlerFunc` interface.**

If you add an argument to your Handler, Martini will search its list of services and attempt to resolve the dependency via type assertion:
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res and req are injected by Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

The following services are included with [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [*log.Logger](http://godoc.org/log#Logger) - Global logger for Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request context.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` of named params found by route matching.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Route helper service.
  * [martini.Route](http://godoc.org/github.com/go-martini/martini#Route) - Current active route.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response writer interface.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request.

### Routing
In Martini, a route is an HTTP method paired with a URL-matching pattern.
Each route can take one or more handler methods:
~~~ go
m.Get("/", func() {
  // show something
})

m.Patch("/", func() {
  // update something
})

m.Post("/", func() {
  // create something
})

m.Put("/", func() {
  // replace something
})

m.Delete("/", func() {
  // destroy something
})

m.Options("/", func() {
  // http options
})

m.NotFound(func() {
  // handle 404
})
~~~

Routes are matched in the order they are defined. The first route that
matches the request is invoked.

Route patterns may include named parameters, accessible via the [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) service:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

Routes can be matched with globs:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

Regular expressions can be used as well:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Take a look at the [Go documentation](http://golang.org/pkg/regexp/syntax/) for more info about regular expressions syntax .

Route handlers can be stacked on top of each other, which is useful for things like authentication and authorization:
~~~ go
m.Get("/secret", authorize, func() {
  // this will execute as long as authorize doesn't write a response
})
~~~

Route groups can be added too using the Group method.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Just like you can pass middlewares to a handler you can pass middlewares to groups.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Services
Services are objects that are available to be injected into a Handler's argument list. You can map a service on a *Global* or *Request* level.

#### Global Mapping
A Martini instance implements the inject.Injector interface, so mapping a service is easy:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // the service will be available to all handlers as *MyDatabase
// ...
m.Run()
~~~

#### Request-Level Mapping
Mapping on the request level can be done in a handler via [martini.Context](http://godoc.org/github.com/go-martini/martini#Context):
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // mapped as *MyCustomLogger
}
~~~

#### Mapping values to Interfaces
One of the most powerful parts about services is the ability to map a service to an interface. For instance, if you wanted to override the [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) with an object that wrapped it and performed extra operations, you can write the following handler:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // override ResponseWriter with our wrapper ResponseWriter
}
~~~

### Serving Static Files
A [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) instance automatically serves static files from the "public" directory in the root of your server.
You can serve from more directories by adding more [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) handlers.
~~~ go
m.Use(martini.Static("assets")) // serve from the "assets" directory as well
~~~

#### Serving a Default Document
You can specify the URL of a local file to serve when the requested URL is not
found. You can also specify an exclusion prefix so that certain URLs are ignored.
This is useful for servers that serve both static files and have additional
handlers defined (e.g., REST API). When doing so, it's useful to define the
static handler as a part of the NotFound chain.

The following example serves the `/index.html` file whenever any URL is
requested that does not match any local file and does not start with `/api/v`:
~~~ go
static := martini.Static("assets", martini.StaticOptions{Fallback: "/index.html", Exclude: "/api/v"})
m.NotFound(static, http.NotFound)
~~~

## Middleware Handlers
Middleware Handlers sit between the incoming http request and the router. In essence they are no different than any other Handler in Martini. You can add a middleware handler to the stack like so:
~~~ go
m.Use(func() {
  // do some middleware stuff
})
~~~

You can have full control over the middleware stack with the `Handlers` function. This will replace any handlers that have been previously set:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Middleware Handlers work really well for things like logging, authorization, authentication, sessions, gzipping, error pages and any other operations that must happen before or after an http request:
~~~ go
// validate an api key
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) is an optional function that Middleware Handlers can call to yield the until after the other Handlers have been executed. This works really well for any operations that must happen after an http request:
~~~ go
// log before and after a request
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("before a request")

  c.Next()

  log.Println("after a request")
})
~~~

## Martini Env

Some Martini handlers make use of the `martini.Env` global variable to provide special functionality for development environments vs production environments. It is recommended that the `MARTINI_ENV=production` environment variable to be set when deploying a Martini server into a production environment.

## FAQ

### Where do I find middleware X?

Start by looking in the [martini-contrib](https://github.com/martini-contrib) projects. If it is not there feel free to contact a martini-contrib team member about adding a new repo to the organization.

* [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler for parsing the `Accept-Language` HTTP header.
* [accessflags](https://github.com/martini-contrib/accessflags) - Handler to enable Access Control.
* [auth](https://github.com/martini-contrib/auth) - Handlers for authentication.
* [binding](https://github.com/martini-contrib/binding) - Handler for mapping/validating a raw request into a structure.
* [cors](https://github.com/martini-contrib/cors) - Handler that enables CORS support.
* [csrf](https://github.com/martini-contrib/csrf) - CSRF protection for applications
* [encoder](https://github.com/martini-contrib/encoder) - Encoder service for rendering data in several formats and content negotiation.
* [gzip](https://github.com/martini-contrib/gzip) - Handler for adding gzip compress to requests
* [gorelic](https://github.com/martini-contrib/gorelic) - NewRelic middleware
* [logstasher](https://github.com/martini-contrib/logstasher) - Middleware that prints logstash-compatiable JSON 
* [method](https://github.com/martini-contrib/method) - HTTP method overriding via Header or form fields.
* [oauth2](https://github.com/martini-contrib/oauth2) - Handler that provides OAuth 2.0 login for Martini apps. Google Sign-in, Facebook Connect and Github login is supported.
* [permissions2](https://github.com/xyproto/permissions2) - Handler for keeping track of users, login states and permissions.
* [render](https://github.com/martini-contrib/render) - Handler that provides a service for easily rendering JSON and HTML templates.
* [secure](https://github.com/martini-contrib/secure) - Implements a few quick security wins.
* [sessions](https://github.com/martini-contrib/sessions) - Handler that provides a Session service.
* [sessionauth](https://github.com/martini-contrib/sessionauth) - Handler that provides a simple way to make routes require a login, and to handle user logins in the session
* [strict](https://github.com/martini-contrib/strict) - Strict Mode 
* [strip](https://github.com/martini-contrib/strip) - URL Prefix stripping.
* [staticbin](https://github.com/martini-contrib/staticbin) - Handler for serving static files from binary data
* [throttle](https://github.com/martini-contrib/throttle) - Request rate throttling middleware.
* [vauth](https://github.com/rafecolton/vauth) - Handlers for vender webhook authentication (currently GitHub and TravisCI)
* [web](https://github.com/martini-contrib/web) - hoisie web.go's Context

### How do I integrate with existing servers?

A Martini instance implements `http.Handler`, so it can easily be used to serve subtrees
on existing Go servers. For example this is a working Martini app for Google App Engine:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### How do I change the port/host?

Martini's `Run` function looks for the PORT and HOST environment variables and uses those. Otherwise Martini will default to localhost:3000.
To have more flexibility over port and host, use the `martini.RunOnAddr` function instead.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Live code reload?

[gin](https://github.com/codegangsta/gin) and [fresh](https://github.com/pilu/fresh) both live reload martini apps.

## Contributing
Martini is meant to be kept tiny and clean. Most contributions should end up in a repository in the [martini-contrib](https://github.com/martini-contrib) organization. If you do have a contribution for the core of Martini feel free to put up a Pull Request.

## About

Inspired by [express](https://github.com/visionmedia/express) and [sinatra](https://github.com/sinatra/sinatra)

Martini is obsessively designed by none other than the [Code Gangsta](http://codegangsta.io/)
# Martini  [![wercker status](https://app.wercker.com/status/174bef7e3c999e103cacfe2770102266 "wercker status")](https://app.wercker.com/project/bykey/174bef7e3c999e103cacfe2770102266) [![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini是一个强大为了编写模块化Web应用而生的GO语言框架.

## 第一个应用

在你安装了GO语言和设置了你的[GOPATH](http://golang.org/doc/code.html#GOPATH)之后, 创建你的自己的`.go`文件, 这里我们假设它的名字叫做 `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

然后安装Martini的包. (注意Martini需要Go语言1.1或者以上的版本支持):
~~~
go get github.com/go-martini/martini
~~~

最后运行你的服务:
~~~
go run server.go
~~~

这时你将会有一个Martini的服务监听了, 地址是: `localhost:3000`.

## 获得帮助

请加入: [邮件列表](https://groups.google.com/forum/#!forum/martini-go)

或者可以查看在线演示地址: [演示视频](http://martini.codegangsta.io/#demo)

## 功能列表
* 使用极其简单.
* 无侵入式的设计.
* 很好的与其他的Go语言包协同使用.
* 超赞的路径匹配和路由.
* 模块化的设计 - 容易插入功能件，也容易将其拔出来.
* 已有很多的中间件可以直接使用.
* 框架内已拥有很好的开箱即用的功能支持.
* **完全兼容[http.HandlerFunc](http://godoc.org/net/http#HandlerFunc)接口.**

## 更多中间件
更多的中间件和功能组件, 请查看代码仓库: [martini-contrib](https://github.com/martini-contrib).

## 目录
* [核心 Martini](#classic-martini)
  * [处理器](#handlers)
  * [路由](#routing)
  * [服务](#services)
  * [服务静态文件](#serving-static-files)
* [中间件处理器](#middleware-handlers)
  * [Next()](#next)
* [常见问答](#faq)

## 核心 Martini
为了更快速的启用Martini, [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) 提供了一些默认的方便Web开发的工具:
~~~ go
  m := martini.Classic()
  // ... middleware and routing goes here
  m.Run()
~~~

下面是Martini核心已经包含的功能 [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * Request/Response Logging （请求/响应日志） - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery （容错） - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Static File serving （静态文件服务） - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routing （路由） - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### 处理器
处理器是Martini的灵魂和核心所在. 一个处理器基本上可以是任何的函数:
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### 返回值
当一个处理器返回结果的时候, Martini将会把返回值作为字符串写入到当前的[http.ResponseWriter](http://godoc.org/net/http#ResponseWriter)里面:
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

另外你也可以选择性的返回多一个状态码:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### 服务的注入
处理器是通过反射来调用的. Martini 通过*Dependency Injection* *（依赖注入）* 来为处理器注入参数列表. **这样使得Martini与Go语言的`http.HandlerFunc`接口完全兼容.**

如果你加入一个参数到你的处理器, Martini将会搜索它参数列表中的服务，并且通过类型判断来解决依赖关系:
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res 和 req 是通过Martini注入的
  res.WriteHeader(200) // HTTP 200
})
~~~

下面的这些服务已经被包含在核心Martini中: [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [*log.Logger](http://godoc.org/log#Logger) - Martini的全局日志.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request context （请求上下文）.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` of named params found by route matching. （名字和参数键值对的参数列表）
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Route helper service. （路由协助处理）
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response writer interface. (响应结果的流接口)
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request. （http请求)

### 路由
在Martini中, 路由是一个HTTP方法配对一个URL匹配模型. 每一个路由可以对应一个或多个处理器方法:
~~~ go
m.Get("/", func() {
  // 显示
})

m.Patch("/", func() {
  // 更新
})

m.Post("/", func() {
  // 创建
})

m.Put("/", func() {
  // 替换
})

m.Delete("/", func() {
  // 删除
})

m.Options("/", func() {
  // http 选项
})

m.NotFound(func() {
  // 处理 404
})
~~~

路由匹配的顺序是按照他们被定义的顺序执行的. 最先被定义的路由将会首先被用户请求匹配并调用.

路由模型可能包含参数列表, 可以通过[martini.Params](http://godoc.org/github.com/go-martini/martini#Params)服务来获取:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

路由匹配可以通过正则表达式或者glob的形式:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

也可以这样使用正则表达式:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
有关正则表达式的更多信息请参见[Go官方文档](http://golang.org/pkg/regexp/syntax/).


路由处理器可以被相互叠加使用, 例如很有用的地方可以是在验证和授权的时候:
~~~ go
m.Get("/secret", authorize, func() {
  // 该方法将会在authorize方法没有输出结果的时候执行.
})
~~~

也可以通过 Group 方法, 将 route 编成一組.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

就像为 handler 增加 middleware 方法一样, 你也可以为一组 routes 增加 middleware.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### 服务
服务即是被注入到处理器中的参数. 你可以映射一个服务到 *全局* 或者 *请求* 的级别.


#### 全局映射
如果一个Martini实现了inject.Injector的接口, 那么映射成为一个服务就非常简单:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // *MyDatabase 这个服务将可以在所有的处理器中被使用到.
// ...
m.Run()
~~~

#### 请求级别的映射
映射在请求级别的服务可以用[martini.Context](http://godoc.org/github.com/go-martini/martini#Context)来完成:
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // 映射成为了 *MyCustomLogger
}
~~~

#### 映射值到接口
关于服务最强悍的地方之一就是它能够映射服务到接口. 例如说, 假设你想要覆盖[http.ResponseWriter](http://godoc.org/net/http#ResponseWriter)成为一个对象, 那么你可以封装它并包含你自己的额外操作, 你可以如下这样来编写你的处理器:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // 覆盖 ResponseWriter 成为我们封装过的 ResponseWriter
}
~~~

### 服务静态文件
[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) 默认会服务位于你服务器环境根目录下的"public"文件夹.
你可以通过加入[martini.Static](http://godoc.org/github.com/go-martini/martini#Static)的处理器来加入更多的静态文件服务的文件夹.
~~~ go
m.Use(martini.Static("assets")) // 也会服务静态文件于"assets"的文件夹
~~~

## 中间件处理器
中间件处理器是工作于请求和路由之间的. 本质上来说和Martini其他的处理器没有分别. 你可以像如下这样添加一个中间件处理器到它的堆中:
~~~ go
m.Use(func() {
  // 做一些中间件该做的事情
})
~~~

你可以通过`Handlers`函数对中间件堆有完全的控制. 它将会替换掉之前的任何设置过的处理器:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

中间件处理器可以非常好处理一些功能，像logging(日志), authorization(授权), authentication(认证), sessions(会话), error pages(错误页面), 以及任何其他的操作需要在http请求发生之前或者之后的:

~~~ go
// 验证api密匙
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context)是一个可选的函数用于中间件处理器暂时放弃执行直到其他的处理器都执行完毕. 这样就可以很好的处理在http请求完成后需要做的操作.
~~~ go
// log 记录请求完成前后  (*译者注: 很巧妙，掌声鼓励.)
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("before a request")

  c.Next()

  log.Println("after a request")
})
~~~

## Martini Env
一些handler使用环境变量 `martini.Env` 对开发环境和生产环境提供特殊功能. 推荐在生产环境设置环境变量 `MARTINI_ENV=production`.


## 常见问答

### 我在哪里可以找到中间件资源?

可以查看 [martini-contrib](https://github.com/martini-contrib) 项目. 如果看了觉得没有什么好货色, 可以联系martini-contrib的团队成员为你创建一个新的代码资源库.

* [acceptlang](https://github.com/martini-contrib/acceptlang) - 解析`Accept-Language` HTTP报头的处理器。
* [accessflags](https://github.com/martini-contrib/accessflags) - 启用访问控制处理器.
* [auth](https://github.com/martini-contrib/auth) - 认证处理器。
* [binding](https://github.com/martini-contrib/binding) - 映射/验证raw请求到结构体(structure)里的处理器。
* [cors](https://github.com/martini-contrib/cors) - 提供支持 CORS 的处理器。
* [csrf](https://github.com/martini-contrib/csrf) - 为应用提供CSRF防护。
* [encoder](https://github.com/martini-contrib/encoder) - 提供用于多种格式的数据渲染或内容协商的编码服务。
* [gzip](https://github.com/martini-contrib/gzip) - 通过giz方式压缩请求信息的处理器。
* [gorelic](https://github.com/martini-contrib/gorelic) - NewRelic 中间件
* [logstasher](https://github.com/martini-contrib/logstasher) - logstash日志兼容JSON中间件 
* [method](https://github.com/martini-contrib/method) - 通过请求头或表单域覆盖HTTP方法。
* [oauth2](https://github.com/martini-contrib/oauth2) - 基于 OAuth 2.0 的应用登录处理器。支持谷歌、Facebook和Github的登录。
* [permissions2](https://github.com/xyproto/permissions2) - 跟踪用户，登录状态和权限控制器
* [render](https://github.com/martini-contrib/render) - 渲染JSON和HTML模板的处理器。
* [secure](https://github.com/martini-contrib/secure) - 提供一些安全方面的速效方案。
* [sessions](https://github.com/martini-contrib/sessions) - 提供`Session`服务支持的处理器。
* [sessionauth](https://github.com/martini-contrib/sessionauth) - 提供简单的方式使得路由需要登录, 并在Session中处理用户登录
* [strip](https://github.com/martini-contrib/strip) - 用于过滤指定的URL前缀。
* [strip](https://github.com/martini-contrib/strip) - URL前缀剥离。
* [staticbin](https://github.com/martini-contrib/staticbin) - 从二进制数据中提供静态文件服务的处理器。
* [throttle](https://github.com/martini-contrib/throttle) - 请求速率调节中间件.
* [vauth](https://github.com/rafecolton/vauth) - 负责webhook认证的处理器(目前支持GitHub和TravisCI)。
* [web](https://github.com/martini-contrib/web) - hoisie web.go's Context

### 我如何整合到我现有的服务器中?

由于Martini实现了 `http.Handler`, 所以它可以很简单的应用到现有Go服务器的子集中. 例如说这是一段在Google App Engine中的示例:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### 我如何修改port/host?

Martini的`Run`函数会检查PORT和HOST的环境变量并使用它们. 否则Martini将会默认使用localhost:3000
如果想要自定义PORT和HOST, 使用`martini.RunOnAddr`函数来代替.

~~~ go
  m := martini.Classic()
  // ...
  m.RunOnAddr(":8080")
~~~

## 贡献
Martini项目想要保持简单且干净的代码. 大部分的代码应该贡献到[martini-contrib](https://github.com/martini-contrib)组织中作为一个项目. 如果你想要贡献Martini的核心代码也可以发起一个Pull Request.

## 关于

灵感来自于 [express](https://github.com/visionmedia/express) 和 [sinatra](https://github.com/sinatra/sinatra)

Martini作者 [Code Gangsta](http://codegangsta.io/)
译者: [Leon](http://github.com/leonli)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini - мощный пакет для быстрой разработки веб приложений и сервисов на Golang.

## Начало работы

После установки Golang и настройки вашего [GOPATH](http://golang.org/doc/code.html#GOPATH), создайте ваш первый `.go` файл. Назовем его `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

Потом установите пакет Martini (требуется **go 1.1** или выше):
~~~
go get github.com/go-martini/martini
~~~

Потом запустите ваш сервер:
~~~
go run server.go
~~~

И вы получите запущенный Martini сервер на `localhost:3000`.

## Помощь

Присоединяйтесь к [рассылке](https://groups.google.com/forum/#!forum/martini-go)

Смотрите [демо видео](http://martini.codegangsta.io/#demo)

Задавайте вопросы на Stackoverflow используя [тэг martini](http://stackoverflow.com/questions/tagged/martini)

GoDoc [документация](http://godoc.org/github.com/go-martini/martini)


## Возможности
* Очень прост в использовании.
* Ненавязчивый дизайн.
* Хорошо сочетается с другими пакетами.
* Потрясающий роутинг и маршрутизация.
* Модульный дизайн - легко добавлять и исключать функциональность.
* Большое количество хороших обработчиков/middlewares, готовых к использованию.
* Отличный набор 'из коробки'.
* **Полностью совместим с интерфейсом [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc).**

## Больше Middleware
Смотрите репозитории организации [martini-contrib](https://github.com/martini-contrib), для большей информации о функциональности и middleware.

## Содержание
* [Classic Martini](#classic-martini)
  * [Обработчики](#%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B8)
  * [Роутинг](#%D0%A0%D0%BE%D1%83%D1%82%D0%B8%D0%BD%D0%B3)
  * [Сервисы](#%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B)
  * [Отдача статических файлов](#%D0%9E%D1%82%D0%B4%D0%B0%D1%87%D0%B0-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2)
* [Middleware обработчики](#middleware-%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B8)
  * [Next()](#next)
* [Окружение](#%D0%9E%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5)
* [FAQ](#faq)

## Classic Martini
Для быстрого старта [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) предлагает несколько предустановок, это используется для большинства веб приложений:
~~~ go
  m := martini.Classic()
  // ... middleware и роутинг здесь
  m.Run()
~~~

Ниже представлена уже подключенная [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) функциональность:  

  * Request/Response логгирование - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Отдача статики - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Роутинг - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Обработчики
Обработчики - это сердце и душа Martini. Обработчик - любая функция, которая может быть вызвана:
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Возвращаемые значения
Если обработчик возвращает что либо, Martini запишет это как результат в текущий [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter), в виде строки:
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

Так же вы можете возвращать код статуса, опционально:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### Внедрение сервисов
Обработчики вызываются посредством рефлексии. Martini использует **Внедрение зависимости** для разрешения зависимостей в списке аргумента обработчика. **Это делает Martini полностью совместимым с интерфейсом `http.HandlerFunc`.**

Если вы добавите аргументы в ваш обработчик, Martini будет пытаться найти этот список сервисов за счет проверки типов(type assertion):
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res и req будут внедрены  Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

Следующие сервисы включены в [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):

  * [*log.Logger](http://godoc.org/log#Logger) - Глобальный логгер для Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request контекст.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` именованых аргументов из роутера.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Хэлпер роутеров.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response writer интерфейс.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request.

### Роутинг
В Martini, роут - это объединенные паттерн и HTTP метод.
Каждый роут может принимать один или несколько обработчиков:
~~~ go
m.Get("/", func() {
  // показать что-то
})

m.Patch("/", func() {
  // обновить что-то
})

m.Post("/", func() {
  // создать что-то
})

m.Put("/", func() {
  // изменить что-то
})

m.Delete("/", func() {
  // удалить что-то
})

m.Options("/", func() {
  // http опции
})

m.NotFound(func() {
  // обработчик 404
})
~~~

Роуты могут сопоставляться с http запросами только в порядке объявления. Вызывается первый роут, который соответствует запросу.

Паттерны роутов могут включать именованные параметры, доступные через [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) сервис:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

Роуты можно объявлять как glob'ы:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

Так же могут использоваться регулярные выражения:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Синтаксис регулярных выражений смотрите [Go documentation](http://golang.org/pkg/regexp/syntax/).

Обработчики роутов так же могут быть выстроены в стек, друг перед другом. Это очень удобно для таких задач как авторизация и аутентификация:
~~~ go
m.Get("/secret", authorize, func() {
  // будет вызываться, в случае если authorize ничего не записал в ответ
})
~~~

Роуты так же могут быть объединены в группы, посредством метода Group:
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Так же как вы можете добавить middleware для обычного обработчика, вы можете добавить middleware и для группы.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Сервисы
Сервисы - это объекты, которые доступны для внедрения в аргументы обработчиков. Вы можете замапить сервисы на уровне всего приложения либо на уровне запроса.

#### Глобальный маппинг
Экземпляр Martini реализует интерфейс inject.Injector, поэтому замаппить сервис легко:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // сервис будет доступен для всех обработчиков как *MyDatabase
// ...
m.Run()
~~~

#### Маппинг уровня запроса
Маппинг на уровне запроса можно сделать при помощи [martini.Context](http://godoc.org/github.com/go-martini/martini#Context):
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // как *MyCustomLogger
}
~~~

#### Маппинг на определенный интерфейс
Одна из мощных частей, того что касается сервисов - маппинг сервиса на определенный интерфейс. Например, если вы хотите переопределить [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) объектом, который оборачивает и добавляет новые операции, вы можете написать следующее:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // переопределить ResponseWriter нашей оберткой
}
~~~

### Отдача статических файлов
Экземпляр [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) автоматически отдает статические файлы из директории "public" в корне, рядом с вашим файлом `server.go`.
Вы можете добавить еще директорий, добавляя [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) обработчики.  
~~~ go
m.Use(martini.Static("assets")) // отдача файлов из "assets" директории
~~~

## Middleware Обработчики
Middleware обработчики находятся между входящим http запросом и роутом. По сути, они ничем не отличаются от любого другого обработчика Martini. Вы можете добавить middleware обработчик в стек следующим образом:
~~~ go
m.Use(func() {
  // делать какую то middleware работу
})
~~~

Для полного контроля над стеком middleware существует метод `Handlers`. В этом примере будут заменены все обработчики, которые были до этого:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Middleware обработчики очень хорошо работают для таких вещей как логгирование, авторизация, аутентификация, сессии, сжатие, страницы ошибок и любые другие операции, которые должны быть выполнены до или после http запроса:
~~~ go
// валидация api ключа
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) опциональная функция, которая может быть вызвана в Middleware обработчике, для выхода из контекста, и возврата в него, после вызова всего стека обработчиков. Это можно использовать для операций, которые должны быть выполнены после http запроса:
~~~ go
// логгирование до и после http запроса
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("до запроса")

  c.Next()

  log.Println("после запроса")
})
~~~

## Окружение
Некоторые Martini обработчики используют глобальную переменную `martini.Env` для того, чтоб предоставить специальную функциональность для девелопмент и продакшн окружения. Рекомендуется устанавливать `MARTINI_ENV=production`, когда вы деплоите приложение на продакшн.

## FAQ

### Где найти готовые middleware?

Начните поиск с [martini-contrib](https://github.com/martini-contrib) проектов. Если нет ничего подходящего, без колебаний пишите члену команды martini-contrib о добавлении нового репозитория в организацию.

* [auth](https://github.com/martini-contrib/auth) - Обработчики для аутентификации.
* [binding](https://github.com/martini-contrib/binding) - Обработчик для маппинга/валидации сырого запроса в определенную структуру(struct).
* [gzip](https://github.com/martini-contrib/gzip) - Обработчик, добавляющий gzip сжатие для запросов.
* [render](https://github.com/martini-contrib/render) - Обработчик, которые предоставляет сервис для легкого рендеринга JSON и HTML шаблонов.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - Обработчик для парсинга `Accept-Language` HTTP заголовка.
* [sessions](https://github.com/martini-contrib/sessions) - Сервис сессий.
* [strip](https://github.com/martini-contrib/strip) - Удаление префиксов из URL.
* [method](https://github.com/martini-contrib/method) - Подмена HTTP метода через заголовок.
* [secure](https://github.com/martini-contrib/secure) - Набор для безопасности.
* [encoder](https://github.com/martini-contrib/encoder) - Сервис для представления данных в нескольких форматах и взаимодействия с контентом.
* [cors](https://github.com/martini-contrib/cors) - Поддержка CORS.
* [oauth2](https://github.com/martini-contrib/oauth2) - Обработчик, предоставляющий OAuth 2.0 логин для Martini приложений. Вход через Google, Facebook и через Github поддерживаются.

### Как интегрироваться с существуюшими серверами?

Экземпляр Martini реализует интерфейс `http.Handler`, потому - это очень просто использовать вместе с существующим Go проектом. Например, это работает для платформы Google App Engine:
~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### Как изменить порт и/или хост?
Функция `Run` смотрит переменные окружиения PORT и HOST, и использует их.
В противном случае Martini по умолчанию будет использовать `localhost:3000`.
Для большей гибкости используйте вместо этого функцию `martini.RunOnAddr`.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Живая перезагрузка кода?

[gin](https://github.com/codegangsta/gin) и [fresh](https://github.com/pilu/fresh) могут работать вместе с Martini.

## Вклад в обшее дело

Подразумевается что Martini чистый и маленький. Большинство улучшений должны быть в организации [martini-contrib](https://github.com/martini-contrib). Но если вы хотите улучшить ядро Martini, отправляйте пулл реквесты.

## О проекте

Вдохновлен [express](https://github.com/visionmedia/express) и [sinatra](https://github.com/sinatra/sinatra)

Martini создан [Code Gangsta](http://codegangsta.io/)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini Go dilinde hızlı ve modüler web uygulamaları ve servisleri için güçlü bir pakettir.


## Başlangıç

Go kurulumu ve [GOPATH](http://golang.org/doc/code.html#GOPATH) ayarını yaptıktan sonra, ilk `.go` uzantılı dosyamızı oluşturuyoruz. Bu oluşturduğumuz dosyayı `server.go` olarak adlandıracağız.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

Martini paketini kurduktan sonra (**go 1.1** ve daha üst go sürümü gerekmektedir.):

~~~
go get github.com/go-martini/martini
~~~

Daha sonra server'ımızı çalıştırıyoruz:

~~~
go run server.go
~~~

Şimdi elimizde çalışan bir adet Martini webserver `localhost:3000`  adresinde bulunmaktadır.


## Yardım Almak İçin 

[Mail Listesi](https://groups.google.com/forum/#!forum/martini-go)

[Örnek Video](http://martini.codegangsta.io/#demo)

Stackoverflow üzerinde [martini etiketine](http://stackoverflow.com/questions/tagged/martini) sahip sorular

[GO Diline ait Dökümantasyonlar](http://godoc.org/github.com/go-martini/martini)


## Özellikler 
* Oldukça basit bir kullanıma sahip.
* Kısıtlama yok.
* Golang paketleri ile rahat bir şekilde kullanılıyor.
* Müthiş bir şekilde path eşleştirme ve yönlendirme.
* Modüler dizayn - Kolay eklenen fonksiyonellik.
* handlers/middlewares kullanımı çok iyi.
* Büyük 'kutu dışarı' özellik seti.
* **[http.HandlerFunc](http://godoc.org/net/http#HandlerFunc) arayüzü ile tam uyumludur.**
* Varsayılan belgelendirme işlemleri (örnek olarak, AngularJS uygulamalarının HTML5 modunda servis edilmesi).

## Daha Fazla Middleware(Ara Katman)

Daha fazla ara katman ve fonksiyonellik için, şu repoları inceleyin [martini-contrib](https://github.com/martini-contrib).

## Tablo İçerikleri
* [Classic Martini](#classic-martini)
  * [İşleyiciler / Handlers](#handlers)
  * [Yönlendirmeler / Routing](#routing)
  * [Servisler](#services)
  * [Statik Dosyaların Sunumu](#serving-static-files)
* [Katman İşleyiciler / Middleware Handlers](#middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) hızlıca projeyi çalıştırır ve çoğu web uygulaması için iyi çalışan bazı makul varsayılanlar sağlar:

~~~ go
  m := martini.Classic()
  // ... middleware and routing goes here
  m.Run()
~~~

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) aşağıdaki bazı fonsiyonelleri  otomatik olarak çeker:

  * İstek/Yanıt Kayıtları (Request/Response Logging) - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Hataların Düzeltilmesi (Panic Recovery) - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Statik Dosyaların Sunumu (Static File serving) - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Yönlendirmeler (Routing) - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### İşleyiciler (Handlers)
İşleyiciler Martini'nin ruhu ve kalbidir. Bir işleyici temel olarak her türlü fonksiyonu çağırabilir:

~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Geriye Dönen Değerler

Eğer bir işleyici geriye bir şey dönderiyorsa, Martini string olarak sonucu [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) ile yazacaktır:

~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

Ayrıca isteğe bağlı bir durum kodu dönderebilir:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### Service Injection
İşlemciler yansıma yoluyla çağrılır. Martini *Dependency Injection* kullanarak arguman listesindeki bağımlıkları giderir.**Bu sayede Martini go programlama dilinin `http.HandlerFunc` arayüzü ile tamamen uyumlu hale getirilir.**

Eğer işleyiciye bir arguman eklersek, Martini "type assertion" ile servis listesinde arayacak ve bağımlılıkları çözmek için girişimde bulunacaktır:

~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res and req are injected by Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

Aşağıdaki servislerin içerikleri

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [*log.Logger](http://godoc.org/log#Logger) - Martini için Global loglayıcı.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request içereği.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` ile yol eşleme tarafından params olarak isimlendirilen yapılar bulundu.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Yönledirilme için yardımcı olan yapıdır.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http yanıtlarını yazacak olan yapıdır.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request(http isteği yapar).

### Yönlendirme - Routing
Martini'de bir yol HTTP metodu URL-matching pattern'i ile eşleştirilir.
Her bir yol bir veya daha fazla işleyici metod alabilir:
~~~ go
m.Get("/", func() {
  // show something
})

m.Patch("/", func() {
  // update something
})

m.Post("/", func() {
  // create something
})

m.Put("/", func() {
  // replace something
})

m.Delete("/", func() {
  // destroy something
})

m.Options("/", func() {
  // http options
})

m.NotFound(func() {
  // handle 404
})
~~~

Yollar sırayla tanımlandıkları şekilde eşleştirilir.Request ile eşleşen ilk rota çağrılır.

Yol patternleri [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) servisi tarafından adlandırılan parametreleri içerebilir:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

Yollar globaller ile eşleşebilir:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

Düzenli ifadeler kullanılabilir:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Düzenli ifadeler hakkında daha fazla bilgiyi [Go dökümanlarından](http://golang.org/pkg/regexp/syntax/) elde edebilirsiniz.

Yol işleyicileri birbirlerinin üstüne istiflenebilir. Bu durum doğrulama ve yetkilendirme(authentication and authorization) işlemleri için iyi bir yöntemdir: 
~~~ go
m.Get("/secret", authorize, func() {
  // this will execute as long as authorize doesn't write a response
})
~~~

Yol grupları Grup metodlar kullanılarak eklenebilir.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Tıpkı ara katmanların işleyiciler için bazı ara katman işlemlerini atlayabileceği gibi gruplar içinde atlayabilir.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Servisler

Servisler işleyicilerin arguman listesine enjekte edilecek kullanılabilir nesnelerdir. İstenildiği taktirde bir servis *Global* ve *Request* seviyesinde eşlenebilir.

#### Global Eşleme - Global Mapping

Bir martini örneği(instance) projeye enjekte edilir. 
A Martini instance implements the inject.Enjekte arayüzü, çok kolay bir şekilde servis eşlemesi yapar:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // the service will be available to all handlers as *MyDatabase
// ...
m.Run()
~~~

#### Request-Level Mapping
Request düzeyinde eşleme yapmak üzere işleyici [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) ile oluşturulabilir:
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // mapped as *MyCustomLogger
}
~~~

#### Arayüz Eşleme Değerleri
Servisler hakkındaki en güçlü şeylerden birisi bir arabirim ile bir servis eşleşmektedir. Örneğin, istenirse [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) yapısı paketlenmiş ve ekstra işlemleri gerçekleştirilen bir nesne ile  override edilebilir. Şu işleyici yazılabilir:

~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // override ResponseWriter with our wrapper ResponseWriter
}
~~~

### Statik Dosyaların Sunumu

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) örneği otomatik olarak statik dosyaları serverda root içinde yer alan "public" dizininden servis edilir.

Eğer istenirse daha fazla [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) işleyicisi eklenerek daha fazla dizin servis edilebilir.
~~~ go
m.Use(martini.Static("assets")) // serve from the "assets" directory as well
~~~

#### Standart Dökümanların Sunulması - Serving a Default Document

Eğer istenilen URL bulunamaz ise özel bir URL dönderilebilir. Ayrıca bir dışlama(exclusion) ön eki ile bazı URL'ler göz ardı edilir. Bu durum statik dosyaların ve ilave işleyiciler için kullanışlıdır(Örneğin, REST API). Bunu yaparken, bu işlem ile NotFound zincirinin bir parçası olan statik işleyiciyi tanımlamak kolaydır.

Herhangi bir URL isteği bir local dosya ile eşleşmediği ve `/api/v` ile başlamadığı zaman aşağıdaki örnek `/index.html` dosyasını sonuç olarak geriye döndürecektir.
~~~ go
static := martini.Static("assets", martini.StaticOptions{Fallback: "/index.html", Exclude: "/api/v"})
m.NotFound(static, http.NotFound)
~~~

## Ara Katman İşleyicileri
Ara katmana ait işleyiciler http isteği ve yönlendirici arasında bulunmaktadır. Özünde onlar diğer Martini işleyicilerinden farklı değildirler. İstenildiği taktirde bir yığına ara katman işleyicisi şu şekilde eklenebilir:
~~~ go
m.Use(func() {
  // do some middleware stuff
})
~~~

`Handlers` fonksiyonu ile ara katman yığını üzerinde tüm kontrole sahip olunabilir. Bu daha önceden ayarlanmış herhangi bir işleyicinin yerini alacaktır:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Orta katman işleyicileri loglama, giriş , yetkilendirme , sessionlar, sıkıştırma(gzipping) , hata sayfaları ve HTTP isteklerinden önce ve sonra herhangi bir olay sonucu oluşan durumlar için gerçekten iyi bir yapıya sahiptir:

~~~ go
// validate an api key
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) orta katman işleyicilerinin diğer işleyiciler yok edilmeden çağrılmasını sağlayan opsiyonel bir fonksiyondur.Bu iş http işlemlerinden sonra gerçekleşecek işlemler için gerçekten iyidir:
~~~ go
// log before and after a request
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("before a request")

  c.Next()

  log.Println("after a request")
})
~~~

## Martini Env

Bazı Martini işleyicileri `martini.Env` yapısının özel fonksiyonlarını kullanmak için geliştirici ortamları, üretici ortamları vs. kullanır.Bu üretim ortamına Martini sunucu kurulurken `MARTINI_ENV=production` şeklinde ortam değişkeninin ayarlanması gerekir.

## FAQ

### Ara Katmanda X'i Nerede Bulurum?

[martini-contrib](https://github.com/martini-contrib) projelerine bakarak başlayın. Eğer aradığınız şey orada mevcut değil ise yeni bir repo eklemek için martini-contrib takım üyeleri ile iletişime geçin.

* [auth](https://github.com/martini-contrib/auth) - Kimlik doğrulama için işleyiciler.
* [binding](https://github.com/martini-contrib/binding) - Mapping/Validating yapısı içinde ham request'i doğrulamak için kullanılan işleyici(handler)
* [gzip](https://github.com/martini-contrib/gzip) - İstekleri gzip sıkışıtırıp eklemek için kullanılan işleyici
* [render](https://github.com/martini-contrib/render) - Kolay bir şekilde JSON ve HTML şablonları oluşturmak için kullanılan işleyici.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - `Kabul edilen dile` göre HTTP başlığını oluşturmak için kullanılan işleyici.
* [sessions](https://github.com/martini-contrib/sessions) - Oturum hizmeti vermek için kullanılır.
* [strip](https://github.com/martini-contrib/strip) - İşleyicilere gitmeden önce URL'ye ait ön şeriti değiştirme işlemini yapar.
* [method](https://github.com/martini-contrib/method) - Formlar ve başlık için http metodunu override eder.
* [secure](https://github.com/martini-contrib/secure) - Birkaç hızlı güvenlik uygulaması ile kazanımda bulundurur.
* [encoder](https://github.com/martini-contrib/encoder) - Encoder servis veri işlemleri için çeşitli format ve içerik sağlar.
* [cors](https://github.com/martini-contrib/cors) - İşleyicilerin CORS desteği bulunur.
* [oauth2](https://github.com/martini-contrib/oauth2) - İşleyiciler OAuth 2.0 için Martini uygulamalarına giriş sağlar. Google , Facebook ve Github için desteği mevcuttur.
* [vauth](https://github.com/rafecolton/vauth) - Webhook için giriş izni sağlar. (şimdilik sadece GitHub ve TravisCI ile)

### Mevcut Sunucular ile Nasıl Entegre Edilir?

Bir martini örneği `http.Handler`'ı projeye dahil eder, bu sayde kolay bir şekilde mevcut olan Go sunucularında  bulunan alt ağaçlarda kullanabilir. Örnek olarak, bu olay Google App Engine için hazırlanmış Martini uygulamalarında kullanılmaktadır:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### port/hostu nasıl değiştiririm?

Martini'ye ait `Run` fonksiyounu PORT ve HOST'a ait ortam değişkenlerini arar ve bunları kullanır. Aksi taktirde standart olarak localhost:3000 adresini port ve host olarak kullanacaktır.

Port ve host için daha fazla esneklik isteniyorsa `martini.RunOnAddr` fonksiyonunu kullanın.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Anlık Kod Yüklemesi?

[gin](https://github.com/codegangsta/gin) ve [fresh](https://github.com/pilu/fresh) anlık kod yüklemeleri yapan martini uygulamalarıdır.

## Katkıda Bulunmak
Martini'nin temiz ve düzenli olaması gerekiyordu. 
Martini is meant to be kept tiny and clean. Tüm kullanıcılar katkı yapmak için [martini-contrib](https://github.com/martini-contrib) organizasyonunda yer alan repoları bitirmelidirler. Eğer martini core için katkıda bulunacaksanız fork işlemini yaparak başlayabilirsiniz.

## Hakkında 

[express](https://github.com/visionmedia/express) ve [sinatra](https://github.com/sinatra/sinatra) projelerinden esinlenmiştir.

Martini [Code Gangsta](http://codegangsta.io/) tarafından tasarlanılmıştır.
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

마티니(Martini)는 강력하고 손쉬운 웹애플리케이션 / 웹서비스개발을 위한 Golang 패키지입니다.

## 시작하기

Go 인스톨 및 [GOPATH](http://golang.org/doc/code.html#GOPATH) 환경변수 설정 이후에, `.go` 파일 하나를 만들어 보죠..흠... 일단 `server.go`라고 부르겠습니다.
~~~go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello, 세계!"
  })
  m.Run()
}
~~~

마티니 패키지를 인스톨 합니다. (**go 1.1** 혹은 그 이상 버젼 필요):
~~~
go get github.com/go-martini/martini
~~~

이제 서버를 돌려 봅시다:
~~~
go run server.go
~~~

마티니 웹서버가 `localhost:3000`에서 돌아가고 있는 것을 확인하실 수 있을 겁니다.

## 도움이 필요하다면?

[메일링 리스트](https://groups.google.com/forum/#!forum/martini-go)에 가입해 주세요

[데모 비디오](http://martini.codegangsta.io/#demo)도 있어요.

혹은 Stackoverflow에 [마티니 태크](http://stackoverflow.com/questions/tagged/martini)를 이용해서 물어봐 주세요

GoDoc [문서(documentation)](http://godoc.org/github.com/go-martini/martini)

문제는 전부다 영어로 되어 있다는 건데요 -_-;;;
나는 한글 아니면 보기 싫다! 하는 분들은 아래 링크를 참조하세요
- [golang-korea](https://code.google.com/p/golang-korea/)
- 혹은 ([RexK](http://github.com/RexK))의 이메일로 연락주세요.

## 주요기능
* 사용하기 엄청 쉽습니다.
* 비간섭(Non-intrusive) 디자인
* 다른 Golang 패키지들과 잘 어울립니다.
* 끝내주는 경로 매칭과 라우팅.
* 모듈형 디자인 - 기능추가가 쉽고, 코드 꺼내오기도 쉬움.
* 유용한 핸들러와 미들웨어가 많음.
* 훌륭한 패키지화(out of the box) 기능들
* **[http.HandlerFunc](http://godoc.org/net/http#HandlerFunc) 인터페이스와 호환율 100%**

## 미들웨어(Middleware)
미들웨어들과 추가기능들은 [martini-contrib](https://github.com/martini-contrib)에서 확인해 주세요.

## 목차
* [Classic Martini](#classic-martini)
  * [핸들러](#핸들러handlers)
  * [라우팅](#라우팅routing)
  * [서비스](#서비스services)
  * [정적파일 서빙](#정적파일-서빙serving-static-files)
* [미들웨어 핸들러](#미들웨어-핸들러middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
마티니를 쉽고 빠르게 이용하시려면, [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic)를 이용해 보세요. 보통 웹애플리케이션에서 사용하는 설정들이 이미 포함되어 있습니다.
~~~ go
  m := martini.Classic()
  // ... 미들웨어와 라우팅 설정은 이곳에 오면 작성하면 됩니다.
  m.Run()
~~~

아래는 [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic)에 자동으로 제공되는 기본 기능들 입니다.

  * Request/Response 로그 기능 - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * 패닉 리커버리 (Panic Recovery) - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * 정적 파일 서빙 - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * 라우팅(Routing) - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### 핸들러(Handlers)

핸들러(Handlers)는 마티니의 핵심입니다. 핸들러는 기본적으로 실행 가능한 모든 형태의 함수들입니다.
~~~ go
m.Get("/", func() {
  println("hello 세계")
})
~~~

#### 반환 값 (Return Values)
핸들러가 반환을 하는 함수라면, 마티니는 반환 값을 [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter)에 스트링으로 입력 할 것입니다.
~~~ go
m.Get("/", func() string {
  return "hello 세계" // HTTP 200 : "hello 세계"
})
~~~

원하신다면, 선택적으로 상태코드도 함께 반환 할 수 있습니다.
~~~ go
m.Get("/", func() (int, string) {
  return 418, "난 주전자야!" // HTTP 418 : "난 주전자야!"
})
~~~

#### 서비스 주입(Service Injection)
핸들러들은 리플렉션을 통해 호출됩니다. 마티니는 *의존성 주입*을 이용해서 핸들러의 인수들을 주입합니다. **이것이 마티니를 `http.HandlerFunc` 인터페이스와 100% 호환할 수 있게 해줍니다.**

핸들러의 인수를 입력했다면, 마티니가 서비스 목록들을 살펴본 후 타입확인(type assertion)을 통해 의존성문제 해결을 시도 할 것입니다.
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res와 req는 마티니에 의해 주입되었다.
  res.WriteHeader(200) // HTTP 200
})
~~~

아래 서비스들은 [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):에 포함되어 있습니다.
  * [*log.Logger](http://godoc.org/log#Logger) - 마티니의 글로벌(전역) 로그.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http 요청 컨텍스트.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - 루트 매칭으로 찾은 인자를 `map[string]string`으로 변형.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - 루트 도우미 서비스.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response writer 인터페이스.
  * [*http.Request](http://godoc.org/net/http/#Request) - http 리퀘스트.

### 라우팅(Routing)
마티니에서 루트는 HTTP 메소드와 URL매칭 패턴의 페어입니다.
각 루트는 하나 혹은 그 이상의 핸들러 메소드를 가질 수 있습니다.
~~~ go
m.Get("/", func() {
  // 보여줘 봐
})

m.Patch("/", func() {
  // 업데이트 좀 해
})

m.Post("/", func() {
  // 만들어봐
})

m.Put("/", func() {
  // 변경해봐
})

m.Delete("/", func() {
  // 없애버려!
})

m.Options("/", func() {
  // http 옵션 메소드
})

m.NotFound(func() {
  // 404 해결하기
})
~~~

루트들은 정의된 순서대로 매칭된다. 들어온 요구에 처음으로 매칭된 루트가 호출된다.

루트 패턴은 [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) service로 액세스 가능한 인자들을 포함하기도 한다:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]			// :name을 Params인자에서 추출
})
~~~

루트는 별표식(\*)으로 매칭 될 수도 있습니다:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

정규식도 사용가능합니다:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
정규식에 관하여 더 자세히 알고 싶다면 [Go documentation](http://golang.org/pkg/regexp/syntax/)을 참조해 주세요.

루트 핸들러는 스택을 쌓아 올릴 수 있습니다. 특히 유저 인증작업이나, 허가작업에 유용히 쓰일 수 있죠.
~~~ go
m.Get("/secret", authorize, func() {
  // 이 함수는 authorize 함수가 resopnse에 결과를 쓰지 않는이상 실행 될 거에요.
})
~~~

```RootGroup```은 루트들을 한 곳에 모아 정리하는데 유용합니다.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

핸들러에 미들웨어를 집어넣을 수 있는것과 같이, 그룹에도 미들웨어를 집어넣는 것이 가능합니다.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### 서비스(Services)
서비스는 핸들러의 인수목록에 주입 될 수 있는 오브젝트들을 말합니다. 서비스는 *글로벌* 혹은 *리퀘스트* 레벨단위로 주입이 가능합니다.

#### 글로벌 맵핑(Global Mapping)
마타니 인스턴스는 서비스 맵핑을 쉽게 하기 위해서 inject.Injector 인터페이스를 반형합니다:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // 서비스가 모든 핸들러에서 *MyDatabase로서 사용될 수 있습니다.
// ...
m.Run()
~~~

#### 리퀘스트 레벨 맵핑(Request-Level Mapping)
리퀘스트 레벨 맵핑은 핸들러안에서 [martini.Context](http://godoc.org/github.com/go-martini/martini#Context)를 사용하면 됩니다:
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // *MyCustomLogger로서 맵핑 됨
}
~~~

#### 인터페이스로 값들 맵핑(Mapping values to Interfaces)
서비스의 강력한 기능중 하나는 서비스를 인터페이스로 맵핑이 가능하다는 것입니다. 예를들어, [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter)를 재정의(override)해서 부가 기능들을 수행하게 하고 싶으시다면, 아래와 같이 핸들러를 작성 하시면 됩니다.

~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // ResponseWriter를 NewResponseWriter로 치환(override)
}
~~~

### 정적파일 서빙(Serving Static Files)
[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) 인스턴스는 "public" 폴더안에 있는 파일들을 정적파일로써 자동으로 서빙합니다. 더 많은 폴더들은 정적파일 폴더에 포함시키시려면 [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) 핸들러를 이용하시면 됩니다.

~~~ go
m.Use(martini.Static("assets")) // "assets" 폴더에서도 정적파일 서빙.
~~~

## 미들웨어 핸들러(Middleware Handlers)
미들웨어 핸들러는 http request와 라우팅 사이에서 작동합니다. 미들웨어 핸들러는 근본적으로 다른 핸들러들과는 다릅니다. 사용방법은 아래와 같습니다:
~~~ go
m.Use(func() {
  // 미들웨어 임무 수행!
})
~~~

`Handlers`를 이용하여 미들웨어 스택들의 완전 컨트롤이 가능합니다. 다만, 이렇게 설정하시면 이전에 `Handlers`를 이용하여 설정한 핸들러들은 사라집니다:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

미들웨어 핸들러는 로깅(logging), 허가(authorization), 인가(authentication), 세션, 압축(gzipping), 에러 페이지 등 등, http request의 전후로 실행되어야 할 일들을 처리하기 아주 좋습니다:
~~~ go
// API 키 확인작업
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "비밀암호!!!" {
    res.WriteHeader(http.StatusUnauthorized)	// HTTP 401
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context)는  선택적 함수입니다. 이 함수는 http request가 다 작동 될때까지 기다립니다.따라서 http request 이후에 실행 되어야 할 업무들을 수행하기 좋은 함수입니다.
~~~ go
// log before and after a request
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("request전입니다.")

  c.Next()

  log.Println("request후 입니다.")
})
~~~

## Martini Env
마티니 핸들러들은 `martini.Env` 글로벌 변수를 사용하여 개발환경에서는 프로덕션 환경과는 다르게 작동하기도 합니다. 따라서, 프로덕션 서버로 마티니 서버를 배포하시게 된다면 꼭 환경변수 `MARTINI_ENV=production`를 세팅해주시기 바랍니다.

## FAQ

### 미들웨어들을 어디서 찾아야 하나요?

깃헙에서 [martini-contrib](https://github.com/martini-contrib) 프로젝트들을 찾아보세요. 만약에 못 찾으시겠으면, martini-contrib 팀원들에게 연락해서 하나 만들어 달라고 해보세요.
* [auth](https://github.com/martini-contrib/auth) - 인증작업을 도와주는 핸들러.
* [binding](https://github.com/martini-contrib/binding) - request를 맵핑하고 검사하는 핸들러.
* [gzip](https://github.com/martini-contrib/gzip) - gzip 핸들러.
* [render](https://github.com/martini-contrib/render) - HTML 템플레이트들과 JSON를 사용하기 편하게 해주는 핸들러.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - `Accept-Language` HTTP 해더를 파싱 할 때 유용한 핸들러.
* [sessions](https://github.com/martini-contrib/sessions) - 세션 서비스를 제공하는 핸들러.
* [strip](https://github.com/martini-contrib/strip) - URL 프리틱스를 없애주는 핸들러.
* [method](https://github.com/martini-contrib/method) - 해더나 폼필드를 이용한 HTTP 메소드 치환.
* [secure](https://github.com/martini-contrib/secure) - 몇몇 보안설정을 위한 핸들러.
* [encoder](https://github.com/martini-contrib/encoder) - 데이터 렌더링과 컨텐트 타입을위한 인코딩 서비스.
* [cors](https://github.com/martini-contrib/cors) - CORS 서포트를 위한 핸들러.
* [oauth2](https://github.com/martini-contrib/oauth2) - OAuth2.0 로그인 핸들러. 페이스북, 구글, 깃헙 지원.

### 현재 작동중인 서버에 마티니를 적용하려면?

마티니 인스턴스는 `http.Handler` 인터페이스를 차용합니다. 따라서 Go 서버 서브트리로 쉽게 사용될 수 있습니다. 아래 코드는 구글 앱 엔진에서 작동하는 마티니 앱입니다:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello 세계!"
  })
  http.Handle("/", m)
}
~~~

### 포트와 호스트는 어떻게 바꾸나요?

마티니의 `Run` 함수는 PORT와 HOST 환경변수를 이용하는데, 설정이 안되어 있다면 localhost:3000으로 설정 되어 집니다.
좀더 유연하게 설정을 하고 싶다면, `martini.RunOnAddr`를 활용해 주세요.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### 라이브 코드 리로드?

[gin](https://github.com/codegangsta/gin) 과 [fresh](https://github.com/pilu/fresh) 가 마티니 앱의 라이브 리로드를 도와줍니다.

## 공헌하기(Contributing)

마티니는 간단하고 가벼운 패키지로 남을 것입니다. 따라서 보통 대부분의 공헌들은 [martini-contrib](https://github.com/martini-contrib) 그룹의 저장소로 가게 됩니다. 만약 마티니 코어에 기여하고 싶으시다면 주저없이 Pull Request를 해주세요.

## About

[express](https://github.com/visionmedia/express) 와 [sinatra](https://github.com/sinatra/sinatra)의 영향을 받았습니다.

마티니는 [Code Gangsta](http://codegangsta.io/)가 디자인 했습니다.
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

MartiniはGolangによる、モジュール形式のウェブアプリケーション/サービスを作成するパワフルなパッケージです。

## はじめに

Goをインストールし、[GOPATH](http://golang.org/doc/code.html#GOPATH)を設定した後、Martiniを始める最初の`.go`ファイルを作りましょう。これを`server.go`とします。

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

そのあとで、Martini パッケージをインストールします。(**go 1.1**か、それ以上のバーションが必要です。)

~~~
go get github.com/go-martini/martini
~~~

インストールが完了したら、サーバを起動しましょう。
~~~
go run server.go
~~~

そうすれば`localhost:3000`でMartiniのサーバが起動します。

## 分からないことがあったら？

[メーリングリスト](https://groups.google.com/forum/#!forum/martini-go)に入る

[デモビデオ](http://martini.codegangsta.io/#demo)をみる

Stackoverflowで[martini tag](http://stackoverflow.com/questions/tagged/martini)を使い質問する

GoDoc [documentation](http://godoc.org/github.com/go-martini/martini)


## 特徴
* 非常にシンプルに使用できる
* 押し付けがましくないデザイン
* 他のGolangパッケージとの協調性
* 素晴らしいパスマッチングとルーティング
* モジュラーデザイン - 機能性の付け外しが簡単
* たくさんの良いハンドラ/ミドルウェア
* 優れた 'すぐに使える' 機能たち
* **[http.HandlerFunc](http://godoc.org/net/http#HandlerFunc)との完全な互換性**

## もっとミドルウェアについて知るには？
さらに多くのミドルウェアとその機能について知りたいときは、[martini-contrib](https://github.com/martini-contrib) オーガナイゼーションにあるリポジトリを確認してください。

## 目次(Table of Contents)
* [Classic Martini](#classic-martini)
  * [ハンドラ](#handlers)
  * [ルーティング](#routing)
  * [サービス](#services)
  * [静的ファイル配信](#serving-static-files)
* [ミドルウェアハンドラ](#middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
立ち上げ、すぐ実行できるように、[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) はほとんどのウェブアプリケーションで機能する、標準的な機能を提供します。
~~~ go
  m := martini.Classic()
  // ... middleware and routing goes here
  m.Run()
~~~

下記が[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic)が自動的に読み込む機能の一覧です。
  * Request/Response Logging - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Static File serving - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routing - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### ハンドラ
ハンドラはMartiniのコアであり、存在意義でもあります。ハンドラには基本的に、呼び出し可能な全ての関数が適応できます。
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Return Values
もしハンドラが何かを返す場合、Martiniはその結果を現在の[http.ResponseWriter](http://godoc.org/net/http#ResponseWriter)にstringとして書き込みます。
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

任意でステータスコードを返すこともできます。
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### Service Injection
ハンドラはリフレクションによって実行されます。Martiniはハンドラの引数内の依存関係を**依存性の注入(Dependency Injection)**を使って解決しています。**これによって、Martiniはgolangの`http.HandlerFunc`と完全な互換性を備えています。**

ハンドラに引数を追加すると、Martiniは内部のサービスを検索し、依存性をtype assertionによって解決しようと試みます。
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res and req are injected by Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic)にはこれらのサービスが内包されています:
  * [*log.Logger](http://godoc.org/log#Logger) - Martiniのためのグローバルなlogger.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request context.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string`型の、ルートマッチングによって検出されたパラメータ
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Route helper service.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response writer interface.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request.

### ルーティング
Martiniでは、ルーティングはHTTPメソッドとURL-matching patternによって対になっており、それぞれが一つ以上のハンドラメソッドを持つことができます。
~~~ go
m.Get("/", func() {
  // show something
})

m.Patch("/", func() {
  // update something
})

m.Post("/", func() {
  // create something
})

m.Put("/", func() {
  // replace something
})

m.Delete("/", func() {
  // destroy something
})

m.Options("/", func() {
  // http options
})

m.NotFound(func() {
  // handle 404
})
~~~

ルーティングはそれらの定義された順番に検索され、最初にマッチしたルーティングが呼ばれます。

名前付きパラメータを定義することもできます。これらのパラメータは[martini.Params](http://godoc.org/github.com/go-martini/martini#Params)サービスを通じてアクセスすることができます:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

ワイルドカードを使用することができます:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

正規表現も、このように使うことができます:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~

もっと正規表現の構文をしりたい場合は、[Go documentation](http://golang.org/pkg/regexp/syntax/) を見てください。


ハンドラは互いの上に積み重ねてることができます。これは、認証や承認処理の際に便利です:
~~~ go
m.Get("/secret", authorize, func() {
  // this will execute as long as authorize doesn't write a response
})
~~~

ルーティンググループも、Groupメソッドを使用することで追加できます。
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

ハンドラにミドルウェアを渡せるのと同じように、グループにもミドルウェアを渡すことができます:
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### サービス
サービスはハンドラの引数として注入されることで利用可能になるオブジェクトです。これらは*グローバル*、または*リクエスト*のレベルでマッピングすることができます。

#### Global Mapping
Martiniのインスタンスはinject.Injectorのインターフェースを実装しています。なので、サービスをマッピングすることは簡単です:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // the service will be available to all handlers as *MyDatabase
// ...
m.Run()
~~~

#### Request-Level Mapping
リクエストレベルでのマッピングは[martini.Context](http://godoc.org/github.com/go-martini/martini#Context)を使い、ハンドラ内で行うことができます:
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // mapped as *MyCustomLogger
}
~~~

#### Mapping values to Interfaces
サービスの最も強力なことの一つは、インターフェースにサービスをマッピングできる機能です。例えば、[http.ResponseWriter](http://godoc.org/net/http#ResponseWriter)を機能を追加して上書きしたい場合、このようにハンドラを書くことができます:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // override ResponseWriter with our wrapper ResponseWriter
}
~~~

### 静的ファイル配信

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) インスタンスは、自動的にルート直下の "public" ディレクトリ以下の静的ファイルを配信します。[martini.Static](http://godoc.org/github.com/go-martini/martini#Static)を追加することで、もっと多くのディレクトリを配信することもできます:
~~~ go
m.Use(martini.Static("assets")) // serve from the "assets" directory as well
~~~

## ミドルウェア　ハンドラ
ミドルウェア ハンドラは次に来るhttpリクエストとルーターの間に位置します。本質的には、その他のハンドラとの違いはありません。ミドルウェア　ハンドラの追加はこのように行います:
~~~ go
m.Use(func() {
  // do some middleware stuff
})
~~~

`Handlers`関数を使えば、ミドルウェアスタックを完全に制御できます。これは以前に設定されている全てのハンドラを置き換えます:

~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

ミドルウェア ハンドラはロギング、認証、承認プロセス、セッション、gzipping、エラーページの表示、その他httpリクエストの前後で怒らなければならないような場合に素晴らしく効果を発揮します。
~~~ go
// validate an api key
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()

[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) は他のハンドラが実行されたことを取得するために使用する機能です。これはhttpリクエストのあとに実行したい任意の関数があるときに素晴らしく機能します:
~~~ go
// log before and after a request
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("before a request")

  c.Next()

  log.Println("after a request")
})
~~~

## Martini Env

いくつかのMartiniのハンドラはdevelopment環境とproduction環境で別々の動作を提供するために`martini.Env`グローバル変数を使用しています。Martiniサーバを本番環境にデプロイする際には、`MARTINI_ENV=production`環境変数をセットすることをおすすめします。

## FAQ

### Middlewareを見つけるには?

[martini-contrib](https://github.com/martini-contrib)プロジェクトをみることから始めてください。もし望みのものがなければ、新しいリポジトリをオーガナイゼーションに追加するために、martini-contribチームのメンバーにコンタクトを取ってみてください。

* [auth](https://github.com/martini-contrib/auth) - Handlers for authentication.
* [binding](https://github.com/martini-contrib/binding) - Handler for mapping/validating a raw request into a structure.
* [gzip](https://github.com/martini-contrib/gzip) - Handler for adding gzip compress to requests
* [render](https://github.com/martini-contrib/render) - Handler that provides a service for easily rendering JSON and HTML templates.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler for parsing the `Accept-Language` HTTP header.
* [sessions](https://github.com/martini-contrib/sessions) - Handler that provides a Session service.
* [strip](https://github.com/martini-contrib/strip) - URL Prefix stripping.
* [method](https://github.com/martini-contrib/method) - HTTP method overriding via Header or form fields.
* [secure](https://github.com/martini-contrib/secure) - Implements a few quick security wins.
* [encoder](https://github.com/martini-contrib/encoder) - Encoder service for rendering data in several formats and content negotiation.
* [cors](https://github.com/martini-contrib/cors) - Handler that enables CORS support.
* [oauth2](https://github.com/martini-contrib/oauth2) - Handler that provides OAuth 2.0 login for Martini apps. Google Sign-in, Facebook Connect and Github login is supported.

### 既存のサーバに組み込むには?

Martiniのインスタンスは`http.Handler`を実装しているので、既存のGoサーバ上でサブツリーを提供するのは簡単です。例えばこれは、Google App Engine上で動くMartiniアプリです:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### どうやってポート/ホストをかえるの?

Martiniの`Run`関数はPORTとHOSTという環境変数を探し、その値を使用します。見つからない場合はlocalhost:3000がデフォルトで使用されます。もっと柔軟性をもとめるなら、`martini.RunOnAddr`関数が役に立ちます:

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Live code reload?

[gin](https://github.com/codegangsta/gin) と [fresh](https://github.com/pilu/fresh) 両方がMartiniアプリケーションを自動リロードできます。

## Contributing
Martini本体は小さく、クリーンであるべきであり、ほとんどのコントリビューションは[martini-contrib](https://github.com/martini-contrib) オーガナイゼーション内で完結すべきですが、もしMartiniのコアにコントリビュートすることがあるなら、自由に行ってください。

## About

Inspired by [express](https://github.com/visionmedia/express) and [sinatra](https://github.com/sinatra/sinatra)

Martini is obsessively designed by none other than the [Code Gangsta](http://codegangsta.io/)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini es un poderoso paquete para escribir rápidamente aplicaciones/servicios web modulares en Golang.


## Vamos a iniciar

Después de instalar Go y de configurar su [GOPATH](http://golang.org/doc/code.html#GOPATH), cree su primer archivo `.go`. Vamos a llamar a este `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hola Mundo!"
  })
  m.Run()
}
~~~

Luego instale el paquete Martini (Es necesario **go 1.1** o superior):
~~~
go get github.com/go-martini/martini
~~~

Después corra su servidor:
~~~
go run server.go
~~~

Ahora tendrá un webserver Martini corriendo en el puerto `localhost:3000`.

## Obtenga ayuda

Suscribase a la [Lista de email](https://groups.google.com/forum/#!forum/martini-go)

Observe el [Video demostrativo](http://martini.codegangsta.io/#demo)

Use la etiqueta [martini](http://stackoverflow.com/questions/tagged/martini) para preguntas en Stackoverflow

GoDoc [documentation](http://godoc.org/github.com/go-martini/martini)


## Caracteríticas
* Extremadamente simple de usar.
* Diseño no intrusivo.
* Buena integración con otros paquetes Golang.
* Enrutamiento impresionante.
* Diseño modular - Fácil de añadir y remover funcionalidades.
* Muy buen uso de handlers/middlewares.
* Grandes características innovadoras.
* **Compatibilidad total con la interface [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc).**

## Más Middlewares
Para más middlewares y funcionalidades, revisar los repositorios en [martini-contrib](https://github.com/martini-contrib).

## Lista de contenidos
* [Classic Martini](#classic-martini)
  * [Handlers](#handlers)
  * [Routing](#routing)
  * [Services](#services)
  * [Serving Static Files](#serving-static-files)
* [Middleware Handlers](#middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
Para iniciar rápidamente, [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) prevee algunas herramientas que funcionan bien para la mayoría de aplicaciones web:
~~~ go
  m := martini.Classic()
  // middlewares y rutas aquí
  m.Run()
~~~

Algunas funcionalidades que [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) ofrece automáticamente son:
  * Request/Response Logging - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Static File serving - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routing - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Handlers
Handlers son el corazón y el alma de Martini. Un handler es básicamente cualquier tipo de función que puede ser llamada.
~~~ go
m.Get("/", func() {
  println("hola mundo")
})
~~~

#### Retorno de Valores
Si un handler retorna cualquier cosa, Martini escribirá el valor retornado como una cadena [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter):
~~~ go
m.Get("/", func() string {
  return "hola mundo" // HTTP 200 : "hola mundo"
})
~~~

Usted también puede retornar un código de estado:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "soy una tetera" // HTTP 418 : "soy una tetera"
})
~~~

#### Inyección de Servicios
Handlers son invocados vía reflexión. Martini utiliza *Inyección de Dependencia* para resolver dependencias en la lista de argumentos Handlers. **Esto hace que Martini sea completamente compatible con  la interface `http.HandlerFunc` de golang.**

Si agrega un argumento a su Handler, Martini buscará en su lista de servicios e intentará resolver su dependencia vía su tipo de aserción:
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res e req son inyectados por Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

Los siguientes servicios son incluidos con [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [*log.Logger](http://godoc.org/log#Logger) - Log Global para Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request context.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` de nombres de los parámetros buscados por la ruta.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Servicio de ayuda para las Rutas.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response escribe la interfaz.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request.

### Rutas
En Martini, una ruta es un método HTTP emparejado con un patrón URL. Cada ruta puede tener uno o más métodos handler:
~~~ go
m.Get("/", func() {
  // mostrar algo
})

m.Patch("/", func() {
  // actualizar algo
})

m.Post("/", func() {
  // crear algo
})

m.Put("/", func() {
  // reemplazar algo
})

m.Delete("/", func() {
  // destruir algo
})

m.Options("/", func() {
  // opciones HTTP
})

m.NotFound(func() {
  // manipula 404
})
~~~

Las rutas son emparejadas en el orden en que son definidas. La primera ruta que coincide con la solicitud es invocada.

Los patrones de rutas puede incluir nombres como parámetros accesibles vía el servicio [martini.Params](http://godoc.org/github.com/go-martini/martini#Params):
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

Las rutas se pueden combinar con globs:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

Las expresiones regulares puede ser usadas también:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Observe la [documentación](http://golang.org/pkg/regexp/syntax/) para mayor información sobre la sintaxis de expresiones regulares.


Handlers de ruta pueden ser empilados en la cima de otros, la cual es útil para cosas como autenticación y autorización:
~~~ go
m.Get("/secret", authorize, func() {
  // será ejecutado cuando autorice escribir una respuesta
})
~~~

Grupos de rutas puede ser añadidas usando el método Group.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Igualmente como puede pasar middlewares para un handler, usted puede pasar middlewares para grupos.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Servicios
Servicios son objetos que están disponibles para ser inyectados en una lista de argumentos Handler. Usted puede mapear un servicios a nivel *Global* o *Request*.

#### Mapeamento Global
Una instancia de Martini implementa la interface inject.Injector, entonces un mapeamiento de un servicio es fácil:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // el servicio estará disponible para todos los handlers como *MyDatabase.
// ...
m.Run()
~~~

#### Mapeamiento por Request
Mapeamiento a nivel de request se puede realizar un handler vía [martini.Context](http://godoc.org/github.com/go-martini/martini#Context):
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // mapeado como *MyCustomLogger
}
~~~

#### Valores de Mapeamiento para Interfaces
Una de las partes mas poderosas sobre servicios es la capadidad de mapear un servicio para una interface. Por ejemplo, si desea sobreescribir [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) con un objeto que envuelva y realice operaciones extra, puede escribir el siguiente handler:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // sobreescribir ResponseWriter con nuestro ResponseWriter
}
~~~

### Sirviendo Archivos Estáticos
Una instancia de [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) sirve automáticamente archivos estáticos del directorio "public" en la raíz de su servidor.
Usted puede servir más directorios, añadiendo más [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) handlers.
~~~ go
m.Use(martini.Static("assets")) // sirviendo los archivos del directorio "assets"
~~~

## Middleware Handlers
Middleware Handlers se sitúan entre una solicitud HTTP y un router. En esencia, ellos no son diferentes de cualquier otro Handler en Martini. Usted puede añadir un handler de middleware para la pila de la siguiente forma:
~~~ go
m.Use(func() {
  // Hacer algo con middleware
})
~~~

Puede tener el control total sobre la pila de middleware con la función `Handlers`. Esto reemplazará a cualquier handler que se ha establecido previamente:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Middleware Handlers trabaja realmente bien como logging, autorización, autenticación, sessión, gzipping, páginas de errores y una serie de otras operaciones que deben suceder antes de una solicitud http:
~~~ go
// Valida una llave de api
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) es una función opcional que Middleware Handlers puede llamar para aguardar una ejecución de otros Handlers. Esto trabaja muy bien para calquier operación que debe suceder antes de una solicitud http:
~~~ go
// log antes y después de una solicitud
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("antes de una solicitud")

  c.Next()

  log.Println("luego de una solicitud")
})
~~~

## Martini Env

Martini handlers hace uso de `martini.Env`, una variable global para proveer funcionalidad especial en ambientes de desarrollo y ambientes de producción. Es recomendado que una variable `MARTINI_ENV=production` sea definida cuando se despliegue en un ambiente de producción.

## FAQ

### ¿Dónde puedo encontrar una middleware X?

Inicie su búsqueda en los proyectos [martini-contrib](https://github.com/martini-contrib). Si no esta allí, no dude en contactar a algún miembro del equipo martini-contrib para adicionar un nuevo repositorio para la organización.

* [auth](https://github.com/martini-contrib/auth) - Handlers para autenticación.
* [binding](https://github.com/martini-contrib/binding) - Handler para mapeamiento/validación de un request en una estrutura.
* [gzip](https://github.com/martini-contrib/gzip) - Handler para agregar gzip comprimidos para requests
* [render](https://github.com/martini-contrib/render) - Handler que provee un servicio de fácil renderizado JSON y plantillas HTML.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler para analizar  `Accept-Language` header HTTP.
* [sessions](https://github.com/martini-contrib/sessions) - Handler que provee un servicio de sesión.
* [strip](https://github.com/martini-contrib/strip) - URL Prefix stripping.
* [method](https://github.com/martini-contrib/method) - HTTP método de sobreescritura vía header o campos de formulario.
* [secure](https://github.com/martini-contrib/secure) - Implementa rápidamente items de seguridad.
* [encoder](https://github.com/martini-contrib/encoder) - Servicio de encoder para renderización de datos en varios formatos y negocios de contenidos.
* [cors](https://github.com/martini-contrib/cors) - Handler que habilita suporte a CORS.
* [oauth2](https://github.com/martini-contrib/oauth2) - Handler que provee sistema de login OAuth 2.0 para aplicaciones Martini. Google Sign-in, Facebook Connect y Github login son soportados.

### ¿Cómo se integra con los servidores existentes?

Una instancia de Martini implementa `http.Handler`, de modo que puede ser fácilmente utilizado para servir sub-rutas y directorios en servidores Go existentes. Por ejemplo, este es un aplicativo Martini trabajando para Google App Engine:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hola Mundo!"
  })
  http.Handle("/", m)
}
~~~

### ¿Cómo cambiar el puerto/host?

La función `Run` de Martini observa las variables PORT e HOST para utilizarlas. Caso contrário, Martini asume por defecto localhost:3000. Para tener maayor flexibilidad sobre el puerto y host, use la función `martini.RunOnAddr`.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### ¿Servidor con autoreload?

[gin](https://github.com/codegangsta/gin) y [fresh](https://github.com/pilu/fresh) son aplicaciones para autorecarga de Martini.

## Contribuyendo
Martini se desea mantener pequeño y limpio. La mayoría de contribuciones deben realizarse en el repositorio [martini-contrib](https://github.com/martini-contrib). Si desea hacer una contribución al core de Martini es libre de realizar un Pull Request.

## Sobre

Inspirado por [express](https://github.com/visionmedia/express) y [sinatra](https://github.com/sinatra/sinatra)

Martini está diseñoado obsesivamente por nada menos que [Code Gangsta](http://codegangsta.io/)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini 是一個使用 Go 語言來快速開發模組化 Web 應用程式或服務的強大套件

## 開始

在您安裝Go語言以及設定好
[GOPATH](http://golang.org/doc/code.html#GOPATH)環境變數後,
開始寫您第一支`.go`檔, 我們將稱它為`server.go`

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello 世界!"
  })
  m.Run()
}
~~~

然後安裝Martini套件 (**go 1.1**以上的版本是必要的)
~~~
go get github.com/go-martini/martini
~~~

然後利用以下指令執行你的程式:
~~~
go run server.go
~~~

此時, 您將會看到一個 Martini Web 伺服器在`localhost:3000`上執行

## 尋求幫助

可以加入 [Mailing list](https://groups.google.com/forum/#!forum/martini-go)

觀看 [Demo Video](http://martini.codegangsta.io/#demo)

## 功能

* 超容易使用
* 非侵入式設計
* 很容易跟其他Go套件同時使用
* 很棒的路徑matching和routing方式
* 模組化設計 - 容易增加或移除功能
* 有很多handlers或middlewares可以直接使用
* 已經提供很多內建功能
* **跟[http.HandlerFunc](http://godoc.org/net/http#HandlerFunc) 介面**完全相容
* 預設document服務 (例如, 提供AngularJS在HTML5模式的服務)

## 其他Middleware
尋找更多的middleware或功能, 請到  [martini-contrib](https://github.com/martini-contrib)程式集搜尋

## 目錄
* [Classic Martini](#classic-martini)
* [Handlers](#handlers)
* [Routing](#routing)
* [Services (服務)](#services)
* [Serving Static Files (伺服靜態檔案)](#serving-static-files)
* [Middleware Handlers](#middleware-handlers)
* [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ (常見問題與答案)](#faq)

## Classic Martini

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic)
提供大部份web應用程式所需要的基本預設功能:

~~~ go
  m := martini.Classic()
  // ... middleware 或 routing 寫在這裡
  m.Run()
~~~
[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic)
 會自動提供以下功能
* Request/Response Logging - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
* Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
* Static File serving - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
* Routing - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)


### Handlers
Handlers 是 Martini 的核心, 每個 handler 就是一個基本的呼叫函式, 例如:
~~~ go
m.Get("/", func() {
  println("hello 世界")
})
~~~

#### 回傳值
如果一個 handler 有回傳值, Martini就會用字串的方式將結果寫回現在的
[http.ResponseWriter](http://godoc.org/net/http#ResponseWriter), 例如:
~~~ go
m.Get("/", func() string {
  return "hello 世界" // HTTP 200 : "hello 世界"
})
~~~

你也可以選擇回傳狀態碼, 例如:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "我是一個茶壺" // HTTP 418 : "我是一個茶壺"
})
~~~

#### 注入服務 (Service Injection)
Handlers 是透過 reflection 方式被喚起, Martini 使用 *Dependency Injection* 的方法
載入 Handler 變數所需要的相關物件 **這也是 Martini 跟 Go 語言`http.HandlerFunc`介面
完全相容的原因**

如果你在 Handler 裡加入一個變數, Martini 會嘗試著從它的服務清單裡透過 type assertion
方式將相關物件載入
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res 和 req 是由 Martini 注入
  res.WriteHeader(200) // HTTP 200
})
~~~

[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) 包含以下物件:
  * [*log.Logger](http://godoc.org/log#Logger) - Martini 的全區域 Logger.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request 內文.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` of named params found by route matching.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Route helper 服務.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http 回應 writer 介面.
  * [*http.Request](http://godoc.org/net/http/#Request) - http 請求.

### Routing
在 Martini 裡, 一個 route 就是一個 HTTP 方法與其 URL 的比對模式.
每個 route 可以有ㄧ或多個 handler 方法:
~~~ go
m.Get("/", func() {
  // 顯示（值）
})

m.Patch("/", func() {
  // 更新
})

m.Post("/", func() {
  // 產生
})

m.Put("/", func() {
  // 取代
})

m.Delete("/", func() {
  // 刪除
})

m.Options("/", func() {
  // http 選項
})

m.NotFound(func() {
  // handle 404
})
~~~

Routes 依照它們被定義時的順序做比對. 第一個跟請求 (request) 相同的 route 就被執行.

Route 比對模式可以包含變數部分, 可以透過 [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) 物件來取值:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

Routes 也可以用 "**" 來配對, 例如:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

也可以用正規表示法 (regular expressions) 來做比對, 例如:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
更多有關正規表示法文法的資訊, 請參考 [Go 文件](http://golang.org/pkg/regexp/syntax/).

Route handlers 也可以相互堆疊, 尤其是認證與授權相當好用:
~~~ go
m.Get("/secret", authorize, func() {
  // 這裏開始處理授權問題, 而非寫出回應
})
~~~

也可以用 Group 方法, 將 route 編成一組.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

跟對 handler 增加 middleware 方法一樣, 你也可以為一組 routes 增加 middleware.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Services
服務是一些物件可以被注入 Handler 變數裡的東西, 可以分對應到 *Global* 或 *Request* 兩種等級.

#### Global Mapping (全域級對應)
一個 Martini 實體 (instance) 實現了 inject.Injector 介面, 所以非常容易對應到所需要的服務, 例如:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // 所以 *MyDatabase 就可以被所有的 handlers 使用
// ...
m.Run()
~~~

#### Request-Level Mapping (請求級對應)
如果只在一個 handler 裡定義, 透由  [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) 獲得一個請求 (request) 級的對應:
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // 對應到 *MyCustomLogger
}
~~~

#### 透由介面對應
有關服務, 最強的部分是它還能對應到一個介面 (interface), 例如,
如果你想要包裹並增加一個變數而改寫 (override) 原有的 [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter), 你的 handler 可以寫成:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // 我們包裹的 ResponseWriter 蓋掉原始的 ResponseWrite
}
~~~

### Serving Static Files
一個[martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) 實體會將伺服器根目錄下 public 子目錄裡的檔案自動當成靜態檔案處理. 你也可以手動用 [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) 增加其他目錄, 例如.
~~~ go
m.Use(martini.Static("assets")) // "assets" 子目錄裡, 也視為靜態檔案
~~~

#### Serving a Default Document
當某些 URL 找不到時, 你也可以指定本地檔案的 URL 來顯示.
你也可以用開頭除外 (exclusion prefix) 的方式, 來忽略某些 URLs,
它尤其在某些伺服器同時伺服靜態檔案, 而且還有額外 handlers 處理 (例如 REST API) 時, 特別好用.
比如說, 在比對找不到之後, 想要用靜態檔來處理特別好用.

以下範例, 就是在 URL 開頭不是`/api/v`而且也不是本地檔案的情況下, 顯示`/index.html`檔:
~~~ go
static := martini.Static("assets", martini.StaticOptions{Fallback: "/index.html", Exclude: "/api/v"})
m.NotFound(static, http.NotFound)
~~~

## Middleware Handlers
Middleware Handlers 位於進來的 http 請求與 router 之間, 在 Martini 裡, 本質上它跟其他
 Handler 沒有什麼不同, 例如, 你可加入一個 middleware 方法如下
~~~ go
m.Use(func() {
  // 做 middleware 的事
})
~~~

你也可以用`Handlers`完全控制 middelware 層, 把先前設定的 handlers 都替換掉, 例如:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Middleware Handlers 成被拿來處理 http 請求之前和之後的事, 尤其是用來紀錄logs, 授權, 認證,
sessions, 壓縮 （gzipping), 顯示錯誤頁面等等, 都非常好用, 例如:
~~~ go
// validate an api key
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) 是 Middleware Handlers 可以呼叫的選項功能, 用來等到其他 handlers 處理完再開始執行.
它常常被用來處理那些必須在 http 請求之後才能發生的事件, 例如:
~~~ go
// 在請求前後加 logs
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("before a request")

  c.Next()

  log.Println("after a request")
})
~~~

## Martini Env

有些 Martini handlers 使用 `martini.Env` 全區域變數, 來當成開發環境或是上架 (production)
環境的設定判斷. 建議用 `MARTINI_ENV=production` 環境變數來設定 Martini 伺服器是上架與否.

## FAQ

### 我去哪可以找到 middleware X?

可以從 [martini-contrib](https://github.com/martini-contrib) 裡的專案找起.
如果那裡沒有, 請與 martini-contrib 團隊聯絡, 將它加入.

* [auth](https://github.com/martini-contrib/auth) - 處理認證的 Handler.
* [binding](https://github.com/martini-contrib/binding) -
處理一個單純的請求對應到一個結構體與確認內容正確與否的 Handler.
* [gzip](https://github.com/martini-contrib/gzip) - 對請求加 gzip 壓縮的 Handler.
* [render](https://github.com/martini-contrib/render) - 提供簡單處理 JSON 和
HTML 樣板成形 (rendering) 的 Handler.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - 解析 `Accept-Language` HTTP 檔頭的 Handler.
* [sessions](https://github.com/martini-contrib/sessions) - 提供 Session 服務的 Handler.
* [strip](https://github.com/martini-contrib/strip) - URL 字頭處理 (Prefix stripping).
* [method](https://github.com/martini-contrib/method) - 透過 Header 或表格 (form) 欄位蓋過 HTTP 方法 (method).
* [secure](https://github.com/martini-contrib/secure) - 提供一些簡單的安全機制.
* [encoder](https://github.com/martini-contrib/encoder) - 轉換資料格式之 Encoder 服務.
* [cors](https://github.com/martini-contrib/cors) - 啟動支援 CORS 之 Handler.
* [oauth2](https://github.com/martini-contrib/oauth2) - 讓 Martini 應用程式能提供 OAuth 2.0 登入的 Handler. 其中支援 Google 登錄, Facebook Connect 與 Github 的登入等.
* [vauth](https://github.com/rafecolton/vauth) - 處理 vender webhook 認證的 Handler (目前支援 GitHub 以及 TravisCI)

### 我如何整合到現有的伺服器?

Martini 實作 `http.Handler`,所以可以非常容易整合到現有的 Go 伺服器裡.
以下寫法, 是一個能在 Google App Engine 上運行的 Martini 應用程式:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### 我要如何改變 port/host?

Martini 的 `Run` 功能會看 PORT 及 HOST 當時的環境變數, 否則 Martini 會用 localhost:3000
當預設值. 讓 port 及 host 更有彈性, 可以用 `martini.RunOnAddr` 取代.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### 可以線上更新 (live reload) 嗎?

[gin](https://github.com/codegangsta/gin) 和 [fresh](https://github.com/pilu/fresh) 可以幫 Martini 程式做到線上更新.

## 貢獻
Martini 盡量保持小而美的精神, 大多數的程式貢獻者可以在 [martini-contrib](https://github.com/martini-contrib) 組織提供代碼. 如果你想要對 Martini 核心提出貢獻, 請丟出 Pull Request.

## 關於

靈感來自與 [express](https://github.com/visionmedia/express) 以及 [sinatra](https://github.com/sinatra/sinatra)

Martini 由 [Code Gangsta](http://codegangsta.io/) 公司設計出品 (著魔地)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini ist ein mächtiges Package zur schnellen Entwicklung von modularen Webanwendungen und -services in Golang. 

## Ein Projekt starten

Nach der Installation von Go und dem Einrichten des [GOPATH](http://golang.org/doc/code.html#GOPATH), erstelle Deine erste `.go`-Datei. Speichere sie unter `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hallo Welt!"
  })
  m.Run()
}
~~~

Installiere anschließend das Martini Package (**Go 1.1** oder höher wird vorausgesetzt):
~~~
go get github.com/go-martini/martini
~~~

Starte den Server:
~~~
go run server.go
~~~

Der Martini-Webserver ist nun unter `localhost:3000` erreichbar.

## Hilfe

Abonniere den [Emailverteiler](https://groups.google.com/forum/#!forum/martini-go)

Schaue das [Demovideo](http://martini.codegangsta.io/#demo)

Stelle Fragen auf Stackoverflow mit dem [Martini-Tag](http://stackoverflow.com/questions/tagged/martini)

GoDoc [Dokumentation](http://godoc.org/github.com/go-martini/martini)


## Eigenschaften
* Sehr einfach nutzbar
* Nicht-intrusives Design
* Leicht kombinierbar mit anderen Golang Packages
* Ausgezeichnetes Path Matching und Routing
* Modulares Design - einfaches Hinzufügen und Entfernen von Funktionen
* Eine Vielzahl von guten Handlern/Middlewares nutzbar
* Großer Funktionsumfang mitgeliefert
* **Voll kompatibel mit dem [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc) Interface.**
* Standardmäßiges Ausliefern von Dateien (z.B. von AngularJS-Apps im HTML5-Modus)

## Mehr Middleware
Mehr Informationen zur Middleware und Funktionalität findest Du in den Repositories der [martini-contrib](https://github.com/martini-contrib) Gruppe.

## Inhaltsverzeichnis
* [Classic Martini](#classic-martini)
  * [Handler](#handler)
  * [Routing](#routing)
  * [Services](#services)
  * [Statische Dateien bereitstellen](#statische-dateien-bereitstellen)
* [Middleware Handler](#middleware-handler)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
Einen schnellen Start in ein Projekt ermöglicht [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic), dessen Voreinstellungen sich für die meisten Webanwendungen eignen:
~~~ go
  m := martini.Classic()
  // ... Middleware und Routing hier einfügen
  m.Run()
~~~

Aufgelistet findest Du einige Aspekte, die [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) automatich berücksichtigt:

  * Request/Response Logging - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Static File serving - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routing - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Handler
Handler sind das Herz und die Seele von Martini. Ein Handler ist grundsätzlich jede Art von aufrufbaren Funktionen:
~~~ go
m.Get("/", func() {
  println("Hallo Welt")
})
~~~

#### Rückgabewerte
Wenn ein Handler Rückgabewerte beinhaltet, übergibt Martini diese an den aktuellen [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) in Form eines String:
~~~ go
m.Get("/", func() string {
  return "Hallo Welt" // HTTP 200 : "Hallo Welt"
})
~~~

Die Rückgabe eines Statuscode ist optional:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "Ich bin eine Teekanne" // HTTP 418 : "Ich bin eine Teekanne"
})
~~~

#### Service Injection
Handler werden per Reflection aufgerufen. Martini macht Gebrauch von *Dependency Injection*, um Abhängigkeiten in der Argumentliste von Handlern aufzulösen. **Dies macht Martini komplett inkompatibel mit Golangs `http.HandlerFunc` Interface.**

Fügst Du einem Handler ein Argument hinzu, sucht Martini in seiner Liste von Services und versucht, die Abhängigkeiten via Type Assertion aufzulösen. 
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res und req wurden von Martini injiziert
  res.WriteHeader(200) // HTTP 200
})
~~~

Die Folgenden Services sind Bestandteil von [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):

  * [*log.Logger](http://godoc.org/log#Logger) - Globaler Logger für Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request context.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` von benannten Parametern, welche durch Route Matching gefunden wurden.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Routen Hilfeservice.
  * [martini.Route](http://godoc.org/github.com/go-martini/martini#Route) - Aktuelle, aktive Route.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response writer interface.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request.

### Routing
Eine Route ist in Martini eine HTTP-Methode gepaart mit einem URL-Matching-Pattern. Jede Route kann eine oder mehrere Handler-Methoden übernehmen:
~~~ go
m.Get("/", func() {
  // zeige etwas an
})

m.Patch("/", func() {
  // aktualisiere etwas
})

m.Post("/", func() {
  // erstelle etwas
})

m.Put("/", func() {
  // ersetze etwas
})

m.Delete("/", func() {
  // lösche etwas
})

m.Options("/", func() {
  // HTTP-Optionen
})

m.NotFound(func() {
  // bearbeite 404-Fehler
})
~~~

Routen werden in der Reihenfolge, in welcher sie definiert wurden, zugeordnet. Die bei einer Anfrage zuerst zugeordnete Route wird daraufhin aufgerufen.  

Routenmuster enthalten ggf. benannte Parameter, die über den [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) Service abrufbar sind:
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hallo " + params["name"]
})
~~~

Routen können mit Globs versehen werden:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hallo " + params["_1"]
})
~~~

Reguläre Ausdrücke sind ebenfalls möglich:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hallo %s", params["name"])
})
~~~
Weitere Informationen zum Syntax regulärer Ausdrücke findest Du in der [Go Dokumentation](http://golang.org/pkg/regexp/syntax/).

Routen-Handler können auch ineinander verschachtelt werden. Dies ist bei der Authentifizierung und den Berechtigungen nützlich.
~~~ go
m.Get("/secret", authorize, func() {
  // wird ausgeführt, solange authorize nichts zurückgibt
})
~~~

Routengruppen können durch die Group-Methode hinzugefügt werden.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Sowohl Handlern als auch Middlewares können Gruppen übergeben werden.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Services
Services sind Objekte, welche der Argumentliste von Handlern beigefügt werden können.
Du kannst einem Service der *Global* oder *Request* Ebene zuordnen.

#### Global Mapping
Eine Martini-Instanz implementiert das inject.Injector Interface, sodass ein Service leicht zugeordnet werden kann:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // der Service ist allen Handlern unter *MyDatabase verfügbar
// ...
m.Run()
~~~

#### Request-Level Mapping
Das Zuordnen auf der Request-Ebene kann in einem Handler via  [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) realisiert werden:
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // zugeordnet als *MyCustomLogger
}
~~~

#### Werten einem Interface zuordnen
Einer der mächtigsten Aspekte von Services ist dessen Fähigkeit, einen Service einem Interface zuzuordnen. Möchtest Du den [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) mit einem Decorator (Objekt) und dessen Zusatzfunktionen überschreiben, definiere den Handler wie folgt:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // überschribe ResponseWriter mit dem  ResponseWriter Decorator
}
~~~

### Statische Dateien bereitstellen
Eine [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) Instanz übertragt automatisch statische Dateien aus dem "public"-Ordner im Stammverzeichnis Deines Servers. Dieses Verhalten lässt sich durch weitere [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) Handler auf andere Verzeichnisse übertragen.
~~~ go
m.Use(martini.Static("assets")) // überträgt auch vom "assets"-Verzeichnis
~~~

#### Eine voreingestelle Datei übertragen
Du kannst die URL zu einer lokalen Datei angeben, sollte die URL einer Anfrage nicht gefunden werden. Durch einen Präfix können bestimmte URLs ignoriert werden.
Dies ist für Server nützlich, welche statische Dateien übertragen und ggf. zusätzliche Handler defineren (z.B. eine REST-API). Ist dies der Fall, so ist das Anlegen eines Handlers in der NotFound-Reihe nützlich.

Das gezeigte Beispiel zeigt die `/index.html` immer an, wenn die angefrage URL keiner lokalen Datei zugeordnet werden kann bzw. wenn sie nicht mit `/api/v` beginnt:
~~~ go
static := martini.Static("assets", martini.StaticOptions{Fallback: "/index.html", Exclude: "/api/v"})
m.NotFound(static, http.NotFound)
~~~

## Middleware Handler
Middleware-Handler befinden sich logisch zwischen einer Anfrage via HTTP und dem Router. Im wesentlichen unterscheiden sie sich nicht von anderen Handlern in Martini.
Du kannst einen Middleware-Handler dem Stack folgendermaßen anfügen:
~~~ go
m.Use(func() {
  // durchlaufe die Middleware
})
~~~

Volle Kontrolle über den Middleware Stack erlangst Du mit der `Handlers`-Funktion.
Sie ersetzt jeden zuvor definierten Handler:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Middleware Handler arbeiten gut mit Aspekten wie Logging, Berechtigungen, Authentifizierung, Sessions, Komprimierung durch gzip, Fehlerseiten und anderen Operationen zusammen, die vor oder nach einer Anfrage passieren.
~~~ go
// überprüfe einen API-Schlüssel
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) ist eine optionale Funktion, die Middleware-Handler aufrufen können, um sie nach dem Beenden der anderen Handler auszuführen. Dies funktioniert besonders gut, wenn Operationen nach einer HTTP-Anfrage ausgeführt werden müssen.
~~~ go
// protokolliere vor und nach einer Anfrage
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("vor einer Anfrage")

  c.Next()

  log.Println("nach einer Anfrage")
})
~~~

## Martini Env

Einige Martini-Handler machen von der globalen `martini.Env` Variable gebrauch, die der Entwicklungsumgebung erweiterte Funktionen bietet, welche die Produktivumgebung nicht enthält. Es wird empfohlen, die `MARTINI_ENV=production` Umgebungsvariable zu setzen, sobald der Martini-Server in den Live-Betrieb übergeht.

## FAQ

### Wo finde ich eine bestimmte Middleware?

Starte die Suche mit einem Blick in die Projekte von [martini-contrib](https://github.com/martini-contrib). Solltest Du nicht fündig werden, kontaktiere ein Mitglied des martini-contrib Teams, um eine neue Repository anzulegen.

 * [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler zum Parsen des `Accept-Language` HTTP-Header.
 * [accessflags](https://github.com/martini-contrib/accessflags) - Handler zur Ermöglichung von Zugriffskontrollen.
 * [auth](https://github.com/martini-contrib/auth) - Handler zur Authentifizierung.
 * [binding](https://github.com/martini-contrib/binding) - Handler zum Zuordnen/Validieren einer Anfrage zu einem Struct.
 * [cors](https://github.com/martini-contrib/cors) - Handler für CORS-Support.
 * [csrf](https://github.com/martini-contrib/csrf) - CSRF-Schutz für Applikationen
 * [encoder](https://github.com/martini-contrib/encoder) - Enkodierungsservice zum Datenrendering in den verschiedensten Formaten.
 * [gzip](https://github.com/martini-contrib/gzip) - Handler zum Ermöglichen von gzip-Kompression bei HTTP-Anfragen.
 * [gorelic](https://github.com/martini-contrib/gorelic) - NewRelic Middleware
 * [logstasher](https://github.com/martini-contrib/logstasher) - Middlewaredie Logstashkompatibles JSON ausgibt
 * [method](https://github.com/martini-contrib/method) - Überschreibe eine HTTP-Method via Header oder Formularfelder.
 * [oauth2](https://github.com/martini-contrib/oauth2) - Handler der den Login mit OAuth 2.0 in Martinianwendungen ermöglicht. Google Sign-in, Facebook Connect und Github werden ebenfalls unterstützt.
 * [permissions2](https://github.com/xyproto/permissions2) - Handler zum Mitverfolgen von Benutzern, Loginstatus und Berechtigungen.
 * [render](https://github.com/martini-contrib/render) - Handler, der einen einfachen Service zum Rendern von JSON und HTML-Templates bereitstellt.
 * [secure](https://github.com/martini-contrib/secure) - Implementation von Sicherheitsfunktionen
 * [sessions](https://github.com/martini-contrib/sessions) - Handler mit einem Session service.
 * [sessionauth](https://github.com/martini-contrib/sessionauth) - Handler zur einfachen Aufforderung eines Logins für Routes und zur Bearbeitung von Benutzerlogins in der Sitzung
 * [strict](https://github.com/martini-contrib/strict) - Strikter Modus.
 * [strip](https://github.com/martini-contrib/strip) - URL-Prefix Stripping.
 * [staticbin](https://github.com/martini-contrib/staticbin) - Handler for serving static files from binary data
 * [throttle](https://github.com/martini-contrib/throttle) - Middleware zum Drosseln von HTTP-Anfragen.
 * [vauth](https://github.com/rafecolton/vauth) - Handler zur Webhook-Authentifizierung (momentan nur GitHub und TravisCI)
 * [web](https://github.com/martini-contrib/web) - hoisie web.go's Kontext

### Wie integriere ich in bestehende Systeme?

Eine Martiniinstanz implementiert `http.Handler`, sodass Subrouten in bestehenden Servern einfach genutzt werden können. Hier ist eine funktionierende Martinianwendungen für die Google App Engine:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hallo Welt!"
  })
  http.Handle("/", m)
}
~~~

### Wie ändere ich den Port/Host?

Martinis `Run` Funktion sucht automatisch nach den PORT und HOST Umgebungsvariablen, um diese zu nutzen. Andernfalls ist localhost:3000 voreingestellt.
Für mehr Flexibilität über den Port und den Host nutze stattdessen die `martini.RunOnAddr` Funktion.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Automatisches Aktualisieren?

[Gin](https://github.com/codegangsta/gin) und [Fresh](https://github.com/pilu/fresh) aktualisieren Martini-Apps live.

## Bei Martini mitwirken

Martinis Maxime ist Minimalismus und sauberer Code. Die meisten Beiträge sollten sich in den Repositories der [martini-contrib](https://github.com/martini-contrib) Gruppe wiederfinden. Beinhaltet Dein Beitrag Veränderungen am Kern von Martini, zögere nicht, einen Pull Request zu machen.

## Über das Projekt

Inspiriert von [Express](https://github.com/visionmedia/express) und [Sinatra](https://github.com/sinatra/sinatra)

Martini wird leidenschaftlich von niemand Geringerem als dem [Code Gangsta](http://codegangsta.io/) entwickelt
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini é um poderoso pacote para escrever aplicações/serviços modulares em Golang..


## Vamos começar

Após a instalação do Go e de configurar o [GOPATH](http://golang.org/doc/code.html#GOPATH), crie seu primeiro arquivo `.go`. Vamos chamá-lo de `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

Então instale o pacote do Martini (É necessário **go 1.1** ou superior):
~~~
go get github.com/go-martini/martini
~~~

Então rode o servidor:
~~~
go run server.go
~~~

Agora você tem um webserver Martini rodando na porta `localhost:3000`.

## Obtenha ajuda

Assine a [Lista de email](https://groups.google.com/forum/#!forum/martini-go)

Veja o [Vídeo demonstrativo](http://martini.codegangsta.io/#demo)

Use a tag [martini](http://stackoverflow.com/questions/tagged/martini) para perguntas no Stackoverflow



## Caracteríticas
* Extrema simplicidade de uso.
* Design não intrusivo.
* Boa integração com outros pacotes Golang.
* Router impressionante.
* Design modular - Fácil para adicionar e remover funcionalidades.
* Muito bom no uso handlers/middlewares.
* Grandes caracteríticas inovadoras.
* **Completa compatibilidade com a interface [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc).**

## Mais Middleware
Para mais middleware e funcionalidades, veja os repositórios em [martini-contrib](https://github.com/martini-contrib).

## Tabela de Conteudos
* [Classic Martini](#classic-martini)
  * [Handlers](#handlers)
  * [Routing](#routing)
  * [Services](#services)
  * [Serving Static Files](#serving-static-files)
* [Middleware Handlers](#middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
Para iniciar rapidamente, [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) provê algumas ferramentas razoáveis para maioria das aplicações web:
~~~ go
  m := martini.Classic()
  // ... middleware e rota aqui
  m.Run()
~~~

Algumas das funcionalidade que o [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) oferece automaticamente são:
  * Request/Response Logging - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Servidor de arquivos státicos - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Rotas - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Handlers
Handlers são o coração e a alma do Martini. Um handler é basicamente qualquer função que pode ser chamada:
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Retorno de Valores
Se um handler retornar alguma coisa, Martini irá escrever o valor retornado como uma string ao [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter):
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

Você também pode retornar o código de status:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "Eu sou um bule" // HTTP 418 : "Eu sou um bule"
})
~~~

#### Injeção de Serviços
Handlers são chamados via reflexão. Martini utiliza *Injeção de Dependencia* para resolver as dependencias nas listas de argumentos dos Handlers . **Isso faz Martini ser completamente compatível com a interface `http.HandlerFunc` do golang.**

Se você adicionar um argumento ao seu Handler, Martini ira procurar na sua lista de serviços e tentar resolver sua dependencia pelo seu tipo:
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res e req são injetados pelo Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

Os seguintes serviços são incluídos com [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [*log.Logger](http://godoc.org/log#Logger) - Log Global para Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - http request context.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` de nomes dos parâmetros buscados pela rota.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Serviço de auxílio as rotas.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - http Response escreve a interface.
  * [*http.Request](http://godoc.org/net/http/#Request) - http Request.

### Rotas
No Martini, uma rota é um método HTTP emparelhado com um padrão de URL de correspondência.
Cada rota pode ter um ou mais métodos handler:
~~~ go
m.Get("/", func() {
  // mostra alguma coisa
})

m.Patch("/", func() {
  // altera alguma coisa
})

m.Post("/", func() {
  // cria alguma coisa
})

m.Put("/", func() {
  // sobrescreve alguma coisa
})

m.Delete("/", func() {
  // destrói alguma coisa
})

m.Options("/", func() {
  // opções do HTTP
})

m.NotFound(func() {
  // manipula 404
})
~~~

As rotas são combinadas na ordem em que são definidas. A primeira rota que corresponde a solicitação é chamada.

O padrão de rotas pode incluir parâmetros que podem ser acessados via [martini.Params](http://godoc.org/github.com/go-martini/martini#Params):
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

As rotas podem ser combinados com expressões regulares e globs:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

Expressões regulares podem ser bem usadas:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Dê uma olhada na [documentação](http://golang.org/pkg/regexp/syntax/) para mais informações sobre expressões regulares.


Handlers de rota podem ser empilhados em cima uns dos outros, o que é útil para coisas como autenticação e autorização:
~~~ go
m.Get("/secret", authorize, func() {
  // Será executado quando authorize não escrever uma resposta
})
~~~

Grupos de rota podem ser adicionados usando o método Group.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Assim como você pode passar middlewares para um manipulador você pode passar middlewares para grupos.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Serviços
Serviços são objetos que estão disponíveis para ser injetado em uma lista de argumentos de Handler. Você pode mapear um serviço num nível *Global* ou *Request*.

#### Mapeamento Global
Um exemplo onde o Martini implementa a interface inject.Injector, então o mapeamento de um serviço é fácil:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // o serviço estará disponível para todos os handlers *MyDatabase.
// ...
m.Run()
~~~

#### Mapeamento por requisição
Mapeamento do nível de request pode ser feito via handler através [martini.Context](http://godoc.org/github.com/go-martini/martini#Context):
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // mapeamento é *MyCustomLogger
}
~~~

#### Valores de Mapeamento para Interfaces
Uma das partes mais poderosas sobre os serviços é a capacidade para mapear um serviço de uma interface. Por exemplo, se você quiser substituir o [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) com um objeto que envolveu-o e realizou operações extras, você pode escrever o seguinte handler:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // substituir ResponseWriter com nosso ResponseWriter invólucro
}
~~~

### Servindo Arquivos Estáticos
Uma instância de [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) serve automaticamente arquivos estáticos do diretório "public" na raiz do seu servidor.
Você pode servir de mais diretórios, adicionando mais [martini.Static](http://godoc.org/github.com/go-martini/martini#Static) handlers.
~~~ go
m.Use(martini.Static("assets")) // servindo os arquivos do diretório "assets"
~~~

## Middleware Handlers
Middleware Handlers ficam entre a solicitação HTTP e o roteador. Em essência, eles não são diferentes de qualquer outro Handler no Martini. Você pode adicionar um handler de middleware para a pilha assim:
~~~ go
m.Use(func() {
  // faz algo com middleware
})
~~~

Você pode ter o controle total sobre a pilha de middleware com a função `Handlers`. Isso irá substituir quaisquer manipuladores que foram previamente definidos:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Middleware Handlers trabalham muito bem com princípios com logging, autorização, autenticação, sessão, gzipping, páginas de erros e uma série de outras operações que devem acontecer antes ou depois de uma solicitação HTTP:
~~~ go
// Valida uma chave de API
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) é uma função opcional que Middleware Handlers podem chamar para aguardar a execução de outros Handlers. Isso funciona muito bem para operações que devem acontecer após uma requisição:
~~~ go
// log antes e depois do request
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("antes do request")

  c.Next()

  log.Println("depois do request")
})
~~~

## Martini Env

Martini handlers fazem uso do `martini.Env`, uma variável global para fornecer funcionalidade especial para ambientes de desenvolvimento e ambientes de produção. É recomendado que a variável `MARTINI_ENV=production` seja definida quando a implementação estiver em um ambiente de produção.

## FAQ

### Onde posso encontrar o middleware X?

Inicie sua busca nos projetos [martini-contrib](https://github.com/martini-contrib). Se ele não estiver lá não hesite em contactar um membro da equipe martini-contrib sobre como adicionar um novo repo para a organização.

* [auth](https://github.com/martini-contrib/auth) - Handlers para autenticação.
* [binding](https://github.com/martini-contrib/binding) - Handler para mapeamento/validação de um request a estrutura.
* [gzip](https://github.com/martini-contrib/gzip) - Handler para adicionar compreção gzip para o requests
* [render](https://github.com/martini-contrib/render) - Handler que providencia uma rederização simples para JSON e templates HTML.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler para parsing do `Accept-Language` no header HTTP.
* [sessions](https://github.com/martini-contrib/sessions) - Handler que prove o serviço de sessão.
* [strip](https://github.com/martini-contrib/strip) - URL Prefix stripping.
* [method](https://github.com/martini-contrib/method) - HTTP método de substituição via cabeçalho ou campos do formulário.
* [secure](https://github.com/martini-contrib/secure) - Implementa rapidamente itens de segurança.
* [encoder](https://github.com/martini-contrib/encoder) - Serviço Encoder para renderização de dados em vários formatos e negociação de conteúdo.
* [cors](https://github.com/martini-contrib/cors) - Handler que habilita suporte a CORS.
* [oauth2](https://github.com/martini-contrib/oauth2) - Handler que prove sistema de login OAuth 2.0 para aplicações Martini. Google Sign-in, Facebook Connect e Github login são suportados.

### Como faço para integrar com os servidores existentes?

Uma instância do Martini implementa `http.Handler`, de modo que pode ser facilmente utilizado para servir sub-rotas e diretórios
em servidores Go existentes. Por exemplo, este é um aplicativo Martini trabalhando para Google App Engine:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### Como faço para alterar a porta/host?

A função `Run` do Martini olha para as variáveis PORT e HOST para utilizá-las. Caso contrário o Martini assume como padrão localhost:3000.
Para ter mais flexibilidade sobre a porta e host use a função `martini.RunOnAddr`.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Servidor com autoreload?

[gin](https://github.com/codegangsta/gin) e [fresh](https://github.com/pilu/fresh) são aplicativos para autoreload do Martini.

## Contribuindo
Martini é feito para ser mantido pequeno e limpo. A maioria das contribuições devem ser feitas no repositório [martini-contrib](https://github.com/martini-contrib). Se quiser contribuir com o core do Martini fique livre para fazer um Pull Request.

## Sobre

Inspirado por [express](https://github.com/visionmedia/express) e [sinatra](https://github.com/sinatra/sinatra)

Martini is obsessively designed by none other than the [Code Gangsta](http://codegangsta.io/)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini to solidny framework umożliwiający sprawne tworzenie modularnych aplikacji internetowych i usług sieciowych w języku Go.

## Pierwsze kroki

Po zakończonej instalacji Go i ustawieniu zmiennej [GOPATH](http://golang.org/doc/code.html#GOPATH), utwórz swój pierwszy plik `.go`. Nazwijmy go `server.go`.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

Następnie zainstaluj pakiet Martini (środowisko **go** w wersji **1.1** lub nowszej jest wymagane):
~~~
go get github.com/go-martini/martini
~~~

Uruchom serwer:
~~~
go run server.go
~~~

W tym momencie webserwer Martini jest uruchomiony na `localhost:3000`.

## Uzyskiwanie pomocy

Dołącz do [grup dyskusyjnych](https://groups.google.com/forum/#!forum/martini-go)

Obejrzyj przygotowane [demo](http://martini.codegangsta.io/#demo)

Zadawaj pytania na Stackoverflow dodając [tag martini](http://stackoverflow.com/questions/tagged/martini)

GoDoc [dokumentacja](http://godoc.org/github.com/go-martini/martini)


## Cechy frameworka
* Bardzo prosty w użyciu.
* Posiada niewymagającą ingerencji budowę.
* Łatwo integruje się z innymi pakietami w języku Go.
* Sprawnie dopasowuje ścieżki i routing.
* Modularny projekt - łatwo dodać funkcję i łatwo usunąć.
* Bogate zasoby handlerów i middleware'ów do wykorzystania.
* Spora część funkcji działa 'z paczki'.
* **W pełni kompatybilny z interfejsem [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc).**
* Umożliwia serwowanie domyślnych stron (np. przy serwowaniu aplikacji napisanych w AngularJS w trybie HTML5).

## Więcej middleware'ów
W celu uzyskania więcej informacji o middleware'ach i ich możliwościach, przejrzyj repozytoria należące do organizacji [martini-contrib](https://github.com/martini-contrib).

## Spis treści
* [Domyślna konfiguracja (Martini Classic)](#domyślna-konfiguracja-martini-classic))
  * [Handlery](#handlery)
  * [Routing](#routing)
  * [Usługi](#usługi)
  * [Serwowanie plików statycznych](#serwowanie-plików-statycznych)
* [Handlery middleware'ów](#handlery-middlewareów)
  * [Next()](#next)
* [Zmienne środowiskowe Martini](#zmienne-środowiskowe-martini)
* [FAQ](#faq)

## Domyślna konfiguracja (Martini Classic)
Martini pozwala bardzo szybko uruchomić webserver korzystając przy tym z [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic). Standardowo Classic dostarcza domyślne ustawienia, które z powodzeniem pozwolą nam uruchomić wiele aplikacji internetowych:
~~~ go
  m := martini.Classic()
  // ... miejsce na middleware'y i routing
  m.Run()
~~~

Poniżej wymieniono kilka funkcji [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) dostarczanych automatycznie:
  * Logowanie żądań/odpowiedzi - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Panic Recovery - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Serwowanie plików statycznych - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routing - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Handlery
Handlery to serce i dusza Martini. Handlerem można nazwać każdą funkcję postaci:
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Wartości zwracane
Jeśli handler zwróci wartość, Martini przekaże ją do bieżącego [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) jako łańcuch znaków:
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~

Opcjonalnie można zwrócić także status HTTP:
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### Wstrzykiwanie usług
Handlery są wywoływane przez refleksję. Martini korzysta z *wstrzykiwania zależności* w celu rozwiązania tych, które występują na liście argumentów handlera. **To sprawia, że Martini jest w pełni zgodny z interfejsem `http.HandlerFunc`.**

Jeśli dodasz argument do handlera, Martini przeszuka swoja listę usług i spróbuje dopasować zależność na podstawie asercji typów:
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res i req są wstrzykiwane przez Martini
  res.WriteHeader(200) // HTTP 200
})
~~~

Następujące usługi są dostarczane razem z [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [*log.Logger](http://godoc.org/log#Logger) - globalny logger dla Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - kontekst żądania HTTP.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` przechowująca nazwane parametry, znalezione podczas dopasowywania _routes_.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - usługa wspierająca _route'y_.
  * [martini.Route](http://godoc.org/github.com/go-martini/martini#Route) - bieżacy aktywny _route_.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - interfejs zapisu odpowiedzi HTTP.
  * [*http.Request](http://godoc.org/net/http/#Request) - żądanie HTTP.

### Routing
W Martini, jako _route_ należy rozumieć metodę HTTP skojarzoną ze wzorcem dopasowującym adres URL.
Każdy wzorzec może być skojarzony z jedną lub więcej metod handlera:
~~~ go
m.Get("/", func() {
  // wyświetl coś
})

m.Patch("/", func() {
  // zaaktualizuj coś
})

m.Post("/", func() {
  // utwórz coś
})

m.Put("/", func() {
  // zamień coś
})

m.Delete("/", func() {
  // zniszcz coś
})

m.Options("/", func() {
  // opcje HTTP
})

m.NotFound(func() {
  // obsłuż 404
})
~~~

_Route'y_ są dopasowywane w kolejności ich definiowania. Pierwszy dopasowany _route_ zostanie wywołany. 

Wzorce ścieżek _route'ów_ mogą zawierać nazwane paremetry, dostępne poprzez usługę  [martini.Params](http://godoc.org/github.com/go-martini/martini#Params):
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

_Route'y_ mogą zostać dopasowane z wartościami globalnymi:
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~

Również wyrażenia regularne mogą zostać użyte:
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Więcej informacji o budowie wyrażeń regularnych znajdziesz w [dokumentacji Go](http://golang.org/pkg/regexp/syntax/).

Handlery można organizować w stosy wywołań, co przydaje się przy mechanizmach takich jak uwierzytelnianie i autoryzacja:
~~~ go
m.Get("/secret", authorize, func() {
  // funkcja będzie wywoływana dopóty, dopóki authorize nie zwróci odpowiedzi
})
~~~

Grupy _route'ów_ mogą zostać dodane przy pomocy metody Group.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

W taki sam sposób jak przekazujesz middleware'y do handlerów, to możesz przekazywać middleware'y do grup.
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Usługi
Usługi są obiektami możliwymi do wstrzyknięcia poprzez listę argumentów danego handlera i mogą być mapowane na poziomie *globalnym* lub *żądania*.

#### Mapowanie globalne
Instancja Martini implementuje interfejs inject.Injector interface, więc mapowanie jest bardzo proste:
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // usługa będzie dostępna dla wszystkich handlerów jako *MyDatabase
// ...
m.Run()
~~~

#### Mapowanie na poziomie żądania
Mapowanie na poziomie żądania może być wykonane w handlerze poprzez [martini.Context](http://godoc.org/github.com/go-martini/martini#Context):
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // zmapowany jako *MyCustomLogger
}
~~~

#### Mapowanie wartości na interfejsy
Jedną z mocnych stron usług jest możliwość zmapowania konkretnej usługi na interfejs. Dla przykładu, jeśli chcesz nadpisać [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) obiektem, który go opakowuje i wykonuje dodatkowe operacje, to możesz napisać następujący handler:
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // nadpisz oryginalny ResponseWriter naszym ResponseWriterem
}
~~~

### Serwowanie plików statycznych
Instancja [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) automatycznie serwuje statyczne pliki z katalogu "public" znajdującym się bezpośrednio w głównym katalogu serwera. Możliwe jest serwowanie dodatkowych katalogów poprzez dodanie handlerów [martini.Static](http://godoc.org/github.com/go-martini/martini#Static).
~~~ go
m.Use(martini.Static("assets")) // serwuj zasoby z katalogu "assets"
~~~

#### Serwowanie domyślnej strony
Możesz zdefiniować adres URL lokalnego pliku, który będzie serwowany gdy żądany adres URL nie zostanie znaleziony. Dodatkowo możesz zdefiniować prefiks wykluczający, który spowoduje, że niektórze adresy URL zostaną zignorowane. Jest to przydatna opcja dla serwerów, które jednocześnie serwują statyczne pliki i mają zdefiniowane handlery (np. REST API). Warto także rozważyć zdefiniowanie statycznych handlerów jako części łańcucha NotFound.

W poniższym przykładzie aplikacja serwuje plik `/index.html`, gdy tylko adres URL nie zostanie dopasowany do istniejącego lokalnego pliku i nie zaczyna się prefiksem `/api/v`:
~~~ go
static := martini.Static("assets", martini.StaticOptions{Fallback: "/index.html", Exclude: "/api/v"})
m.NotFound(static, http.NotFound)
~~~

## Handlery middleware'ów
Handlery middleware'ów są uruchamiane po otrzymaniu żądania HTTP a przed przekazaniem go do routera. W zasadzie nie ma różnicy między nimi a handlerami Martini. Handler middleware'a można dodać do stosu wywołań w następujący sposób:
~~~ go
m.Use(func() {
  // wykonaj operacje zdefiniowane przez middleware
})
~~~

Pełną kontrolę na stosem middleware'owym zapewnia funkcja `Handlers`. Poniższy przykład prezentuje, jak można zamienić poprzednio skonfigurowane handlery:
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~

Handlery middleware'ów sprawdzają się doskonale dla mechanizmów takich jak logowanie, autoryzacja, uwierzytelnianie, obsługa sesji, kompresja odpowiedzi, strony błędów i innych, których operacje muszą zostać wykonane przed i po obsłudze żądania HTTP:
~~~ go
// validate an api key
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next()
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) jest opcjonalną funkcją, którą handlery middleware'ów wywołują, żeby przekazać tymczasowo obsługę żadania do kolejnych handlerów, a później do niej wrócić. Mechanizm sprawdza się doskonale w przypadku wykonywania operacji po obsłudze żądania HTTP:
~~~ go
// zaloguj przed i po żądaniu
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("before a request")

  c.Next()

  log.Println("after a request")
})
~~~

## Zmienne środowiskowe Martini

Niektóre handlery Martini wykorzystują globalną zmienną `martini.Env` by dostarczać specjalne funkcje dla środowisk deweloperskich i produkcyjnych. Zaleca się ustawienie zmiennej `MARTINI_ENV=production` w środowisku produkcyjnym.

## FAQ

### Gdzie mam szukać middleware'u X?

Proponujemy zacząć poszukiwania od projektów należących do [martini-contrib](https://github.com/martini-contrib). Jeśli dany middleware się tam nie znajduje, skontaktuj się z członkiem zespołu martini-contrib i poproś go o dodanie nowego repozytorium do organizacji.

* [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler umożliwiający parsowanie nagłówka HTTP `Accept-Language`.
* [accessflags](https://github.com/martini-contrib/accessflags) - Handler dołączający obsługę kontroli dostępu.
* [auth](https://github.com/martini-contrib/auth) - Handlery uwierzytelniające.
* [binding](https://github.com/martini-contrib/binding) - Handler mapujący/walidujący żądanie na strukturę.
* [cors](https://github.com/martini-contrib/cors) - Handler dostarcza wsparcie dla CORS.
* [csrf](https://github.com/martini-contrib/csrf) - Ochrona CSRF dla aplikacji.
* [encoder](https://github.com/martini-contrib/encoder) - Usługa enkodująca treść odpowiedzi w różnych formatach, wspiera negocjacje formatu.
* [gzip](https://github.com/martini-contrib/gzip) - Handler dla kompresji GZIP żądań.
* [gorelic](https://github.com/martini-contrib/gorelic) - NewRelic middleware.
* [logstasher](https://github.com/martini-contrib/logstasher) - Middleware zwracający odpowiedź formacie kompatybilnym z logstash JSONem.
* [method](https://github.com/martini-contrib/method) - Nadpisywanie metod HTTP poprzez nagłówek.
* [oauth2](https://github.com/martini-contrib/oauth2) - Handler dostarczający logowanie OAuth 2.0 dla aplikacji Martini. Logowanie Google Sign-in, Facebook Connect i Github wspierane.
* [permissions2](https://github.com/xyproto/permissions2) - Handler śledzący użytkowników, ich logowania i uprawnienia.
* [render](https://github.com/martini-contrib/render) - Handler dostarczający usługę łatwo renderującą odpowiedź do formatu JSON i szablonów HTML.
* [secure](https://github.com/martini-contrib/secure) - Implementuje kilka szybkich "quick-wins" związanych z bezpieczeństwem.
* [sessions](https://github.com/martini-contrib/sessions) - Handler dostarcza usługę sesji.
* [sessionauth](https://github.com/martini-contrib/sessionauth) - Handler, który umożliwia w prosty sposób nałożenie reguły wymagania logowania dla konkretnych adresów oraz obsługę zalogowanych użytkowników w sesji. 
* [strict](https://github.com/martini-contrib/strict) - Strict Mode 
* [strip](https://github.com/martini-contrib/strip) - Pomijanie prefiksu URL.
* [staticbin](https://github.com/martini-contrib/staticbin) - Handler umożliwia serwowanie statycznych plików z zasobów binarnych.
* [throttle](https://github.com/martini-contrib/throttle) - Middleware kontrolujący przepustowość handlerów.
* [vauth](https://github.com/rafecolton/vauth) - Handlery wspierające vendorowe uwierzytelnianie (obecnie GitHub i TravisCI).
* [web](https://github.com/martini-contrib/web) - Kontekst znany z web.go.

### Jak mogę zintegrować Martini z istniejącymi serwerami?

Instacja Martini implementuje `http.Handler`, więc może być łatwo wykorzystana do serwowania całych drzew zasobów na istniejących serwerach Go. Przykład przedstawia działającą aplikację Martini dla Google App Engine:

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### Jak mogę zmienić host/port?

Funkcja `Run` sprawdza, czy są zdefiniowane zmienne środowiskowe HOST i PORT, i jeśli są to ich używa. W przeciwnym wypadku Martini uruchomi się z domyślnymi ustawieniami localhost:3000.
W celu uzyskania większej kontroli nad hostem i portem, skorzystaj z funkcji `martini.RunOnAddr`.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Automatyczne przeładowywanie kodu aplikacji (Live code reload)

[gin](https://github.com/codegangsta/gin) i [fresh](https://github.com/pilu/fresh) wspierają przeładowywanie kodu aplikacji.

## Rozwijanie
Martini w założeniu ma pozostać czysty i uporządkowany. Większość kontrybucji powinna trafić jako repozytorium organizacji [martini-contrib](https://github.com/martini-contrib). Jeśli masz kontrybucję do core'a projektu Martini, zgłoś Pull Requesta.

## O projekcie

Inspirowany [expressem](https://github.com/visionmedia/express) i [sinatrą](https://github.com/sinatra/sinatra)

Martini został obsesyjnie zaprojektowany przez nikogo innego jak przez [Code Gangsta](http://codegangsta.io/)
# Martini  [![wercker status](https://app.wercker.com/status/9b7dbc6e2654b604cd694d191c3d5487/s/master "wercker status")](https://app.wercker.com/project/bykey/9b7dbc6e2654b604cd694d191c3d5487)[![GoDoc](https://godoc.org/github.com/go-martini/martini?status.png)](http://godoc.org/github.com/go-martini/martini)

Martini est une puissante bibliothèque pour développer rapidement des applications et services web en Golang.


## Pour commencer

Après avoir installé Go et configuré le chemin d'accès pour [GOPATH](http://golang.org/doc/code.html#GOPATH), créez votre premier fichier '.go'. Nous l'appellerons 'server.go'.

~~~ go
package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Run()
}
~~~

Installez ensuite le paquet Martini (**go 1.1** ou supérieur est requis) :

~~~
go get github.com/go-martini/martini
~~~

La commande suivante vous permettra de lancer votre serveur :
~~~
go run server.go
~~~

Vous avez à présent un serveur web Martini à l'écoute sur l'adresse et le port suivants : `localhost:3000`.

## Besoin d'aide
- Souscrivez à la [Liste d'emails](https://groups.google.com/forum/#!forum/martini-go)
- Regardez les vidéos [Demo en vidéo](http://martini.codegangsta.io/#demo)
- Posez vos questions sur StackOverflow.com en utilisant le tag [martini](http://stackoverflow.com/questions/tagged/martini)
- La documentation GoDoc [documentation](http://godoc.org/github.com/go-martini/martini)


## Caractéristiques
* Simple d'utilisation
* Design non-intrusif
* Compatible avec les autres paquets Golang
* Gestionnaire d'URL et routeur disponibles
* Modulable, permettant l'ajout et le retrait de fonctionnalités
* Un grand nombre de handlers/middlewares disponibles
* Prêt pour une utilisation immédiate
* **Entièrement compatible avec l'interface [http.HandlerFunc](http://godoc.org/net/http#HandlerFunc).**

## Plus de Middleware
Pour plus de middlewares et de fonctionnalités, consultez le dépôt [martini-contrib](https://github.com/martini-contrib).

## Table des matières
* [Classic Martini](#classic-martini)
  * [Handlers](#handlers)
  * [Routage](#routing)
  * [Services](#services)
  * [Serveur de fichiers statiques](#serving-static-files)
* [Middleware Handlers](#middleware-handlers)
  * [Next()](#next)
* [Martini Env](#martini-env)
* [FAQ](#faq)

## Classic Martini
Pour vous faire gagner un temps précieux, [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) est configuré avec des paramètres qui devraient couvrir les besoins de la plupart des applications web :

~~~ go
  m := martini.Classic()
  // ... les middlewares and le routage sont insérés ici...
  m.Run()
~~~

Voici quelques handlers/middlewares que [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) intègre par défault :
  * Logging des requêtes/réponses - [martini.Logger](http://godoc.org/github.com/go-martini/martini#Logger)
  * Récupération sur erreur - [martini.Recovery](http://godoc.org/github.com/go-martini/martini#Recovery)
  * Serveur de fichiers statiques - [martini.Static](http://godoc.org/github.com/go-martini/martini#Static)
  * Routage - [martini.Router](http://godoc.org/github.com/go-martini/martini#Router)

### Handlers
Les Handlers sont le coeur et l'âme de Martini. N'importe quelle fonction peut être utilisée comme un handler.
~~~ go
m.Get("/", func() {
  println("hello world")
})
~~~

#### Valeurs retournées
Si un handler retourne une valeur, Martini écrira le résultat dans l'instance [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) courante sous forme de ```string```:
~~~ go
m.Get("/", func() string {
  return "hello world" // HTTP 200 : "hello world"
})
~~~
Vous pouvez aussi optionnellement renvoyer un code de statut HTTP :
~~~ go
m.Get("/", func() (int, string) {
  return 418, "i'm a teapot" // HTTP 418 : "i'm a teapot"
})
~~~

#### Injection de services
Les handlers sont appelés via réflexion. Martini utilise "l'injection par dépendance" pour résoudre les dépendances des handlers dans la liste d'arguments. **Cela permet à Martini d'être parfaitement compatible avec l'interface golang ```http.HandlerFunc```.**

Si vous ajoutez un argument à votre Handler, Martini parcourera la liste des services et essayera de déterminer ses dépendances selon son type :
~~~ go
m.Get("/", func(res http.ResponseWriter, req *http.Request) { // res and req are injected by Martini
  res.WriteHeader(200) // HTTP 200
})
~~~
Les services suivants sont inclus avec [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic):
  * [log.Logger](http://godoc.org/log#Logger) - Global logger for Martini.
  * [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) - Contexte d'une requête HTTP.
  * [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) - `map[string]string` contenant les paramètres retrouvés par correspondance des routes.
  * [martini.Routes](http://godoc.org/github.com/go-martini/martini#Routes) - Service d'aide au routage.
  * [http.ResponseWriter](http://godoc.org/net/http/#ResponseWriter) - Interface d'écriture de réponses HTTP.
  * [*http.Request](http://godoc.org/net/http/#Request) - Requête HTTP.

### Routeur
Dans Martini, un chemin est une méthode HTTP liée à un modèle d'adresse URL.
Chaque chemin peut avoir un seul ou plusieurs méthodes *handler* :
~~~ go
m.Get("/", func() {
  // show something
})

m.Patch("/", func() {
  // update something
})

m.Post("/", func() {
  // create something
})

m.Put("/", func() {
  // replace something
})

m.Delete("/", func() {
  // destroy something
})

m.Options("/", func() {
  // http options
})

m.NotFound(func() {
  // handle 404
})
~~~
Les chemins seront traités dans l'ordre dans lequel ils auront été définis. Le *handler* du premier chemin trouvé qui correspondra à la requête sera invoqué.


Les chemins peuvent inclure des paramètres nommés, accessibles avec le service [martini.Params](http://godoc.org/github.com/go-martini/martini#Params) :
~~~ go
m.Get("/hello/:name", func(params martini.Params) string {
  return "Hello " + params["name"]
})
~~~

Les chemins peuvent correspondre à des globs :
~~~ go
m.Get("/hello/**", func(params martini.Params) string {
  return "Hello " + params["_1"]
})
~~~
Les expressions régulières peuvent aussi être utilisées :
~~~go
m.Get("/hello/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
  return fmt.Sprintf ("Hello %s", params["name"])
})
~~~
Jetez un oeil à la documentation [Go documentation](http://golang.org/pkg/regexp/syntax/) pour plus d'informations sur la syntaxe des expressions régulières.

Les handlers d'un chemins peuvent être superposés, ce qui s'avère particulièrement pratique pour des tâches comme la gestion de l'authentification et des autorisations :
~~~ go
m.Get("/secret", authorize, func() {
  // this will execute as long as authorize doesn't write a response
})
~~~

Un groupe de chemins peut aussi être ajouté en utilisant la méthode ```Group``` :
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
})
~~~

Comme vous pouvez passer des middlewares à un handler, vous pouvez également passer des middlewares à des groupes :
~~~ go
m.Group("/books", func(r martini.Router) {
    r.Get("/:id", GetBooks)
    r.Post("/new", NewBook)
    r.Put("/update/:id", UpdateBook)
    r.Delete("/delete/:id", DeleteBook)
}, MyMiddleware1, MyMiddleware2)
~~~

### Services
Les services sont des objets injectés dans la liste d'arguments d'un handler. Un service peut être défini pour une *requête*, ou de manière *globale*.


#### Global Mapping
Les instances Martini implémentent l'interace inject.Injector, ce qui facilite grandement le mapping de services :
~~~ go
db := &MyDatabase{}
m := martini.Classic()
m.Map(db) // the service will be available to all handlers as *MyDatabase
// ...
m.Run()
~~~

#### Requête-Level Mapping
Pour une déclaration au niveau d'une requête, il suffit d'utiliser un handler via [martini.Context](http://godoc.org/github.com/go-martini/martini#Context) :
~~~ go
func MyCustomLoggerHandler(c martini.Context, req *http.Request) {
  logger := &MyCustomLogger{req}
  c.Map(logger) // mapped as *MyCustomLogger
}
~~~

#### Mapping de valeurs à des interfaces
L'un des aspects les plus intéressants des services réside dans le fait qu'ils peuvent être liés à des interfaces. Par exemple, pour surcharger [http.ResponseWriter](http://godoc.org/net/http#ResponseWriter) avec un objet qui l'enveloppe et étend ses fonctionnalités, vous pouvez utiliser le handler suivant :
~~~ go
func WrapResponseWriter(res http.ResponseWriter, c martini.Context) {
  rw := NewSpecialResponseWriter(res)
  c.MapTo(rw, (*http.ResponseWriter)(nil)) // override ResponseWriter with our wrapper ResponseWriter
}
~~~

### Serveur de fichiers statiques
Une instance [martini.Classic()](http://godoc.org/github.com/go-martini/martini#Classic) est déjà capable de servir les fichiers statiques qu'elle trouvera dans le dossier *public* à la racine de votre serveur.
Vous pouvez indiquer d'autres dossiers sources à l'aide du handler  [martini.Static](http://godoc.org/github.com/go-martini/martini#Static).
~~~ go
m.Use(martini.Static("assets")) // serve from the "assets" directory as well
~~~

## Les middleware Handlers
Les *middleware handlers* sont placés entre la requête HTTP entrante et le routeur. Ils ne sont aucunement différents des autres handlers présents dans Martini. Vous pouvez ajouter un middleware handler comme ceci :
~~~ go
m.Use(func() {
  // do some middleware stuff
})
~~~
Vous avez un contrôle total sur la structure middleware avec la fonction ```Handlers```. Son exécution écrasera tous les handlers configurés précédemment :
~~~ go
m.Handlers(
  Middleware1,
  Middleware2,
  Middleware3,
)
~~~
Middleware Handlers est très pratique pour automatiser des fonctions comme le logging, l'autorisation, l'authentification, sessions, gzipping, pages d'erreur, et toutes les opérations qui se font avant ou après chaque requête HTTP :
~~~ go
// validate an api key
m.Use(func(res http.ResponseWriter, req *http.Request) {
  if req.Header.Get("X-API-KEY") != "secret123" {
    res.WriteHeader(http.StatusUnauthorized)
  }
})
~~~

### Next() (Suivant)
[Context.Next()](http://godoc.org/github.com/go-martini/martini#Context) est une fonction optionnelle que les Middleware Handlers peuvent appeler pour patienter jusqu'à ce que tous les autres handlers aient été exécutés. Cela fonctionne très bien pour toutes opérations qui interviennent après une requête HTTP :
~~~ go
// log before and after a request
m.Use(func(c martini.Context, log *log.Logger){
  log.Println("avant la requête")

  c.Next()

  log.Println("après la requête")
})
~~~

## Martini Env
Plusieurs Martini handlers utilisent 'martini.Env' comme variable globale pour fournir des fonctionnalités particulières qui diffèrent entre l'environnement de développement et l'environnement de production. Il est recommandé que la variable 'MARTINI_ENV=production' soit définie pour déployer un serveur Martini en environnement de production.

## FAQ (Foire aux questions)

### Où puis-je trouver des middleware ?
Commencer par regarder dans le [martini-contrib](https://github.com/martini-contrib) projet. S'il n'y est pas, n'hésitez pas à contacter un membre de l'équipe martini-contrib pour ajouter un nouveau dépôt à l'organisation.

* [auth](https://github.com/martini-contrib/auth) - Handlers for authentication.
* [binding](https://github.com/martini-contrib/binding) - Handler for mapping/validating a raw request into a structure.
* [gzip](https://github.com/martini-contrib/gzip) - Handler for adding gzip compress to requests
* [render](https://github.com/martini-contrib/render) - Handler that provides a service for easily rendering JSON and HTML templates.
* [acceptlang](https://github.com/martini-contrib/acceptlang) - Handler for parsing the `Accept-Language` HTTP header.
* [sessions](https://github.com/martini-contrib/sessions) - Handler that provides a Session service.
* [strip](https://github.com/martini-contrib/strip) - URL Prefix stripping.
* [method](https://github.com/martini-contrib/method) - HTTP method overriding via Header or form fields.
* [secure](https://github.com/martini-contrib/secure) - Implements a few quick security wins.
* [encoder](https://github.com/martini-contrib/encoder) - Encoder service for rendering data in several formats and content negotiation.
* [cors](https://github.com/martini-contrib/cors) - Handler that enables CORS support.
* [oauth2](https://github.com/martini-contrib/oauth2) - Handler that provides OAuth 2.0 login for Martini apps. Google Sign-in, Facebook Connect and Github login is supported.
* [vauth](https://github.com/rafecolton/vauth) - Handlers for vender webhook authentication (currently GitHub and TravisCI)

### Comment puis-je m'intègrer avec des serveurs existants ?
Une instance Martini implémente ```http.Handler```. Elle peut donc utilisée pour alimenter des sous-arbres sur des serveurs Go existants. Voici l'exemple d'une application Martini pour Google App Engine :

~~~ go
package hello

import (
  "net/http"
  "github.com/go-martini/martini"
)

func init() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  http.Handle("/", m)
}
~~~

### Comment changer le port/adresse ?

La fonction ```Run``` de Martini utilise le port et l'adresse spécifiés dans les variables d'environnement. Si elles ne peuvent y être trouvées, Martini utilisera *localhost:3000* par default.
Pour avoir plus de flexibilité sur le port et l'adresse, utilisez la fonction `martini.RunOnAddr` à la place.

~~~ go
  m := martini.Classic()
  // ...
  log.Fatal(m.RunOnAddr(":8080"))
~~~

### Rechargement du code en direct ?

[gin](https://github.com/codegangsta/gin) et [fresh](https://github.com/pilu/fresh) sont tous les capables de recharger le code des applications martini chaque fois qu'il est modifié.

## Contribuer
Martini est destiné à rester restreint et épuré. Toutes les contributions doivent finir dans un dépot dans l'organisation [martini-contrib](https://github.com/martini-contrib). Si vous avez une contribution pour le noyau de Martini, n'hésitez pas à envoyer une Pull Request.

## A propos de Martini

Inspiré par [express](https://github.com/visionmedia/express) et [Sinatra](https://github.com/sinatra/sinatra), Martini est l'oeuvre de nul d'autre que [Code Gangsta](http://codegangsta.io/), votre serviteur.
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

Simply modify the import from `"github.com/rcrowley/go-metrics/librato"` to
`"github.com/cyberdelia/go-metrics-graphite"` and it should Just Work.
# getpasswd in Go [![GoDoc](https://godoc.org/github.com/howeyc/gopass?status.svg)](https://godoc.org/github.com/howeyc/gopass) [![Build Status](https://secure.travis-ci.org/howeyc/gopass.png?branch=master)](http://travis-ci.org/howeyc/gopass)

Retrieve password from user terminal or piped input without echo.

Verified on BSD, Linux, and Windows.

Example:
```go
package main

import "fmt"
import "github.com/howeyc/gopass"

func main() {
	fmt.Printf("Password: ")

	// Silent. For printing *'s use gopass.GetPasswdMasked()
	pass, err := gopass.GetPasswd()
	if err != nil {
		// Handle gopass.ErrInterrupted or getch() read error
	}

	// Do something with pass
}
```

Caution: Multi-byte characters not supported!
# Go-MySQL-Driver

A MySQL-Driver for Go's [database/sql](https://golang.org/pkg/database/sql/) package

![Go-MySQL-Driver logo](https://raw.github.com/wiki/go-sql-driver/mysql/gomysql_m.png "Golang Gopher holding the MySQL Dolphin")

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
    * [Connection pool and timeouts](#connection-pool-and-timeouts)
    * [context.Context Support](#contextcontext-support)
    * [ColumnType Support](#columntype-support)
    * [LOAD DATA LOCAL INFILE support](#load-data-local-infile-support)
    * [time.Time support](#timetime-support)
    * [Unicode support](#unicode-support)
  * [Testing / Development](#testing--development)
  * [License](#license)

---------------------------------------

## Features
  * Lightweight and [fast](https://github.com/go-sql-driver/sql-benchmark "golang MySQL-Driver performance")
  * Native Go implementation. No C-bindings, just pure Go
  * Connections over TCP/IPv4, TCP/IPv6, Unix domain sockets or [custom protocols](https://godoc.org/github.com/go-sql-driver/mysql#DialFunc)
  * Automatic handling of broken connections
  * Automatic Connection Pooling *(by database/sql package)*
  * Supports queries larger than 16MB
  * Full [`sql.RawBytes`](https://golang.org/pkg/database/sql/#RawBytes) support.
  * Intelligent `LONG DATA` handling in prepared statements
  * Secure `LOAD DATA LOCAL INFILE` support with file Whitelisting and `io.Reader` support
  * Optional `time.Time` parsing
  * Optional placeholder interpolation

## Requirements
  * Go 1.7 or higher. We aim to support the 3 latest versions of Go.
  * MySQL (4.1+), MariaDB, Percona Server, Google CloudSQL or Sphinx (2.2.3+)

---------------------------------------

## Installation
Simple install the package to your [$GOPATH](https://github.com/golang/go/wiki/GOPATH "GOPATH") with the [go tool](https://golang.org/cmd/go/ "go command") from shell:
```bash
$ go get -u github.com/go-sql-driver/mysql
```
Make sure [Git is installed](https://git-scm.com/downloads) on your machine and in your system's `PATH`.

## Usage
_Go MySQL Driver_ is an implementation of Go's `database/sql/driver` interface. You only need to import the driver and can use the full [`database/sql`](https://golang.org/pkg/database/sql/) API then.

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
See [net.Dial](https://golang.org/pkg/net/#Dial) for more information which networks are available.
In general you should use an Unix domain socket if available and TCP otherwise for best performance.

#### Address
For TCP and UDP networks, addresses have the form `host[:port]`.
If `port` is omitted, the default port will be used.
If `host` is a literal IPv6 address, it must be enclosed in square brackets.
The functions [net.JoinHostPort](https://golang.org/pkg/net/#JoinHostPort) and [net.SplitHostPort](https://golang.org/pkg/net/#SplitHostPort) manipulate addresses in this form.

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

##### `allowNativePasswords`

```
Type:           bool
Valid Values:   true, false
Default:        true
```
`allowNativePasswords=false` disallows the usage of MySQL native password method.

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

Sets the location for time.Time values (when using `parseTime=true`). *"Local"* sets the system's location. See [time.LoadLocation](https://golang.org/pkg/time/#LoadLocation) for details.

Note that this sets the location for time.Time values but does not change MySQL's [time_zone setting](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html). For that see the [time_zone system variable](#system-variables), which can also be set as a DSN parameter.

Please keep in mind, that param values must be [url.QueryEscape](https://golang.org/pkg/net/url/#QueryEscape)'ed. Alternatively you can manually replace the `/` with `%2F`. For example `US/Pacific` would be `loc=US%2FPacific`.

##### `maxAllowedPacket`
```
Type:          decimal number
Default:       4194304
```

Max packet size allowed in bytes. The default value is 4 MiB and should be adjusted to match the server settings. `maxAllowedPacket=0` can be used to automatically fetch the `max_allowed_packet` variable from server *on every connection*.

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
Type:           duration
Default:        0
```

I/O read timeout. The value must be a decimal number with a unit suffix (*"ms"*, *"s"*, *"m"*, *"h"*), such as *"30s"*, *"0.5m"* or *"1m30s"*.

##### `rejectReadOnly`

```
Type:           bool
Valid Values:   true, false
Default:        false
```


`rejectReadOnly=true` causes the driver to reject read-only connections. This
is for a possible race condition during an automatic failover, where the mysql
client gets connected to a read-only replica after the failover.

Note that this should be a fairly rare case, as an automatic failover normally
happens when the primary is down, and the race condition shouldn't happen
unless it comes back up online as soon as the failover is kicked off. On the
other hand, when this happens, a MySQL application can get stuck on a
read-only connection until restarted. It is however fairly easy to reproduce,
for example, using a manual failover on AWS Aurora's MySQL-compatible cluster.

If you are not relying on read-only transactions to reject writes that aren't
supposed to happen, setting this on some MySQL providers (such as AWS Aurora)
is safer for failovers.

Note that ERROR 1290 can be returned for a `read-only` server and this option will
cause a retry for that error. However the same error number is used for some
other cases. You should ensure your application will never cause an ERROR 1290
except for `read-only` mode when enabling this option.


##### `timeout`

```
Type:           duration
Default:        OS default
```

Timeout for establishing connections, aka dial timeout. The value must be a decimal number with a unit suffix (*"ms"*, *"s"*, *"m"*, *"h"*), such as *"30s"*, *"0.5m"* or *"1m30s"*.


##### `tls`

```
Type:           bool / string
Valid Values:   true, false, skip-verify, <name>
Default:        false
```

`tls=true` enables TLS / SSL encrypted connection to the server. Use `skip-verify` if you want to use a self-signed or invalid certificate (server side). Use a custom value registered with [`mysql.RegisterTLSConfig`](https://godoc.org/github.com/go-sql-driver/mysql#RegisterTLSConfig).


##### `writeTimeout`

```
Type:           duration
Default:        0
```

I/O write timeout. The value must be a decimal number with a unit suffix (*"ms"*, *"s"*, *"m"*, *"h"*), such as *"30s"*, *"0.5m"* or *"1m30s"*.


##### System Variables

Any other parameters are interpreted as system variables:
  * `<boolean_var>=<value>`: `SET <boolean_var>=<value>`
  * `<enum_var>=<value>`: `SET <enum_var>=<value>`
  * `<string_var>=%27<value>%27`: `SET <string_var>='<value>'`

Rules:
* The values for string variables must be quoted with `'`.
* The values must also be [url.QueryEscape](http://golang.org/pkg/net/url/#QueryEscape)'ed!
 (which implies values of string variables must be wrapped with `%27`).

Examples:
  * `autocommit=1`: `SET autocommit=1`
  * [`time_zone=%27Europe%2FParis%27`](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html): `SET time_zone='Europe/Paris'`
  * [`tx_isolation=%27REPEATABLE-READ%27`](https://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_tx_isolation): `SET tx_isolation='REPEATABLE-READ'`


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

Treat warnings as errors by setting the system variable [`sql_mode`](https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html):
```
user:password@/dbname?sql_mode=TRADITIONAL
```

TCP via IPv6:
```
user:password@tcp([de:ad:be:ef::ca:fe]:80)/dbname?timeout=90s&collation=utf8mb4_unicode_ci
```

TCP on a remote host, e.g. Amazon RDS:
```
id:password@tcp(your-amazonaws-uri.com:3306)/dbname
```

Google Cloud SQL on App Engine (First Generation MySQL Server):
```
user@cloudsql(project-id:instance-name)/dbname
```

Google Cloud SQL on App Engine (Second Generation MySQL Server):
```
user@cloudsql(project-id:regionname:instance-name)/dbname
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


### Connection pool and timeouts
The connection pool is managed by Go's database/sql package. For details on how to configure the size of the pool and how long connections stay in the pool see `*DB.SetMaxOpenConns`, `*DB.SetMaxIdleConns`, and `*DB.SetConnMaxLifetime` in the [database/sql documentation](https://golang.org/pkg/database/sql/). The read, write, and dial timeouts for each individual connection are configured with the DSN parameters [`readTimeout`](#readtimeout), [`writeTimeout`](#writetimeout), and [`timeout`](#timeout), respectively.

## `ColumnType` Support
This driver supports the [`ColumnType` interface](https://golang.org/pkg/database/sql/#ColumnType) introduced in Go 1.8, with the exception of [`ColumnType.Length()`](https://golang.org/pkg/database/sql/#ColumnType.Length), which is currently not supported.

## `context.Context` Support
Go 1.8 added `database/sql` support for `context.Context`. This driver supports query timeouts and cancellation via contexts.
See [context support in the database/sql package](https://golang.org/doc/go1.8#database_sql) for more details.


### `LOAD DATA LOCAL INFILE` support
For this feature you need direct access to the package. Therefore you must change the import path (no `_`):
```go
import "github.com/go-sql-driver/mysql"
```

Files must be whitelisted by registering them with `mysql.RegisterLocalFile(filepath)` (recommended) or the Whitelist check must be deactivated by using the DSN parameter `allowAllFiles=true` ([*Might be insecure!*](http://dev.mysql.com/doc/refman/5.7/en/load-data-local.html)).

To use a `io.Reader` a handler function must be registered with `mysql.RegisterReaderHandler(name, handler)` which returns a `io.Reader` or `io.ReadCloser`. The Reader is available with the filepath `Reader::<name>` then. Choose different names for different handlers and `DeregisterReaderHandler` when you don't need it anymore.

See the [godoc of Go-MySQL-Driver](https://godoc.org/github.com/go-sql-driver/mysql "golang mysql driver documentation") for details.


### `time.Time` support
The default internal output type of MySQL `DATE` and `DATETIME` values is `[]byte` which allows you to scan the value into a `[]byte`, `string` or `sql.RawBytes` variable in your program.

However, many want to scan MySQL `DATE` and `DATETIME` values into `time.Time` variables, which is the logical opposite in Go to `DATE` and `DATETIME` in MySQL. You can do that by changing the internal output type from `[]byte` to `time.Time` with the DSN parameter `parseTime=true`. You can set the default [`time.Time` location](https://golang.org/pkg/time/#Location) with the `loc` DSN parameter.

**Caution:** As of Go 1.1, this makes `time.Time` the only variable type you can scan `DATE` and `DATETIME` values into. This breaks for example [`sql.RawBytes` support](https://github.com/go-sql-driver/mysql/wiki/Examples#rawbytes).

Alternatively you can use the [`NullTime`](https://godoc.org/github.com/go-sql-driver/mysql#NullTime) type as the scan destination, which works with both `time.Time` and `string` / `[]byte`.


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
  * You can **use** the **unchanged** source code both in private and commercially.
  * When distributing, you **must publish** the source code of any **changed files** licensed under the MPL 2.0 under a) the MPL 2.0 itself or b) a compatible license (e.g. GPL 3.0 or Apache License 2.0).
  * You **needn't publish** the source code of your library as long as the files licensed under the MPL 2.0 are **unchanged**.

Please read the [MPL 2.0 FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) if you have further questions regarding the license.

You can read the full terms here: [LICENSE](https://raw.github.com/go-sql-driver/mysql/master/LICENSE).

![Go Gopher and MySQL Dolphin](https://raw.github.com/wiki/go-sql-driver/mysql/go-mysql-driver_m.jpg "Golang Gopher transporting the MySQL Dolphin in a wheelbarrow")

consul-api
==========

*DEPRECATED* Please use [consul api package](https://github.com/hashicorp/consul/tree/master/api) instead.
Godocs for that package [are here](http://godoc.org/github.com/hashicorp/consul/api).

This package provides the `consulapi` package which attempts to
provide programmatic access to the full Consul API.

Currently, all of the Consul APIs included in version 0.4 are supported.

Documentation
=============

The full documentation is available on [Godoc](http://godoc.org/github.com/armon/consul-api)

Usage
=====

Below is an example of using the Consul client:

```go
// Get a new client, with KV endpoints
client, _ := consulapi.NewClient(consulapi.DefaultConfig())
kv := client.KV()

// PUT a new KV pair
p := &consulapi.KVPair{Key: "foo", Value: []byte("test")}
_, err := kv.Put(p, nil)
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

```go
func SlowMethod() {
    // Profiling the runtime of a method
    defer metrics.MeasureSince([]string{"SlowMethod"}, time.Now())
}

// Configure a statsite sink as the global metrics sink
sink, _ := metrics.NewStatsiteSink("statsite:8125")
metrics.NewGlobal(metrics.DefaultConfig("service-name"), sink)

// Emit a Key/Value pair
metrics.EmitKey([]string{"questions", "meaning of life"}, 42)
```

Here is an example of setting up an signal handler:

```go
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
```

When a signal comes in, output like the following will be dumped to stderr:

    [2014-01-28 14:57:33.04 -0800 PST][G] 'foo': 42.000
    [2014-01-28 14:57:33.04 -0800 PST][P] 'bar': 30.000
    [2014-01-28 14:57:33.04 -0800 PST][C] 'baz': Count: 3 Min: 1.000 Mean: 41.000 Max: 80.000 Stddev: 39.509
    [2014-01-28 14:57:33.04 -0800 PST][S] 'method.wow': Count: 3 Min: 22.000 Mean: 54.667 Max: 100.000 Stddev: 40.513

## stopwatch

stopwatch - a simple package to provide timer functionality

While there are other stopwatch implementations none of them
seemed to exactly match what I was looking for. This is very
simple and intended for collecting run times inside an
application.

### Installation

Install the package with:
`go get github.com/sjmudd/stopwatch`

### Contributing

Patches and improvements to this package are welcome.

### Licensing

BSD 2-Clause License

### Feedback

Feedback and patches welcome.

Simon J Mudd
<sjmudd@pobox.com>

### Code Documenton
[godoc.org/github.com/sjmudd/stopwatch](http://godoc.org/github.com/sjmudd/stopwatch)
# go-cache

go-cache is an in-memory key:value store/cache similar to memcached that is
suitable for applications running on a single machine. Its major advantage is
that, being essentially a thread-safe `map[string]interface{}` with expiration
times, it doesn't need to serialize or transmit its contents over the network.

Any object can be stored, for a given duration or forever, and the cache can be
safely used by multiple goroutines.

Although go-cache isn't meant to be used as a persistent datastore, the entire
cache can be saved to and loaded from a file (using `c.Items()` to retrieve the
items map to serialize, and `NewFrom()` to create a cache from a deserialized
one) to recover from downtime quickly. (See the docs for `NewFrom()` for caveats.)

### Installation

`go get github.com/patrickmn/go-cache`

### Usage

```go
import (
	"fmt"
	"github.com/patrickmn/go-cache"
	"time"
)

func main() {
	// Create a cache with a default expiration time of 5 minutes, and which
	// purges expired items every 10 minutes
	c := cache.New(5*time.Minute, 10*time.Minute)

	// Set the value of the key "foo" to "bar", with the default expiration time
	c.Set("foo", "bar", cache.DefaultExpiration)

	// Set the value of the key "baz" to 42, with no expiration time
	// (the item won't be removed until it is re-set, or removed using
	// c.Delete("baz")
	c.Set("baz", 42, cache.NoExpiration)

	// Get the string associated with the key "foo" from the cache
	foo, found := c.Get("foo")
	if found {
		fmt.Println(foo)
	}

	// Since Go is statically typed, and cache values can be anything, type
	// assertion is needed when values are being passed to functions that don't
	// take arbitrary types, (i.e. interface{}). The simplest way to do this for
	// values which will only be used once--e.g. for passing to another
	// function--is:
	foo, found := c.Get("foo")
	if found {
		MyFunction(foo.(string))
	}

	// This gets tedious if the value is used several times in the same function.
	// You might do either of the following instead:
	if x, found := c.Get("foo"); found {
		foo := x.(string)
		// ...
	}
	// or
	var foo string
	if x, found := c.Get("foo"); found {
		foo = x.(string)
	}
	// ...
	// foo can then be passed around freely as a string

	// Want performance? Store pointers!
	c.Set("foo", &MyStruct, cache.DefaultExpiration)
	if x, found := c.Get("foo"); found {
		foo := x.(*MyStruct)
			// ...
	}
}
```

### Reference

`godoc` or [http://godoc.org/github.com/patrickmn/go-cache](http://godoc.org/github.com/patrickmn/go-cache)
Common Go libraries

To import & use:
```
go get "github.com/openark/golib/math"
go get "github.com/openark/golib/sqlutils"
go get "github.com/openark/golib/tests"
...
```
# auth [![wercker status](https://app.wercker.com/status/8e5237b01b52f169a1274fad9a89617b "wercker status")](https://app.wercker.com/project/bykey/8e5237b01b52f169a1274fad9a89617b)
Martini middleware/handler for http basic authentication.

[API Reference](http://godoc.org/github.com/martini-contrib/auth)

## Simple Usage

Use `auth.Basic` to authenticate against a pre-defined username and password:

~~~ go
import (
  "github.com/go-martini/martini"
  "github.com/martini-contrib/auth"
)

func main() {
  m := martini.Classic()
  // authenticate every request
  m.Use(auth.Basic("username", "secretpassword"))
  m.Run()
}
~~~

## Advanced Usage

Using `auth.BasicFunc` lets you authenticate on a per-user level, by checking
the username and password in the callback function:

~~~ go
import (
  "github.com/go-martini/martini"
  "github.com/martini-contrib/auth"
)

func main() {
  m := martini.Classic()
  // authenticate every request
  m.Use(auth.BasicFunc(func(username, password string) bool {
    return username == "admin" && password == "guessme"
  }))
  m.Run()
}
~~~

Note that checking usernames and passwords with string comparison might be
susceptible to timing attacks. To avoid that, use `auth.SecureCompare` instead:

~~~ go
  m.Use(auth.BasicFunc(func(username, password string) bool {
    return auth.SecureCompare(username, "admin") && auth.SecureCompare(password, "guessme")
  }))
}
~~~

Upon successful authentication, the username is available to all subsequent
handlers via the `auth.User` type:

~~~ go
  m.Get("/", func(user auth.User) string {
    return "Welcome, " + string(user)
  })
}
~~~

## Authors
* [Jeremy Saenz](http://github.com/codegangsta)
* [Brendon Murphy](http://github.com/bemurphy)
# render [![wercker status](https://app.wercker.com/status/fcf6b26a1b41f53540200b1949b48dec "wercker status")](https://app.wercker.com/project/bykey/fcf6b26a1b41f53540200b1949b48dec)
Martini middleware/handler for easily rendering serialized JSON, XML, and HTML template responses.

[API Reference](http://godoc.org/github.com/martini-contrib/render)

## Usage
render uses Go's [html/template](http://golang.org/pkg/html/template/) package to render html templates.

~~~ go
// main.go
package main

import (
  "github.com/go-martini/martini"
  "github.com/martini-contrib/render"
)

func main() {
  m := martini.Classic()
  // render html templates from templates directory
  m.Use(render.Renderer())

  m.Get("/", func(r render.Render) {
    r.HTML(200, "hello", "jeremy")
  })

  m.Run()
}

~~~

~~~ html
<!-- templates/hello.tmpl -->
<h2>Hello {{.}}!</h2>
~~~

### Options
`render.Renderer` comes with a variety of configuration options:

~~~ go
// ...
m.Use(render.Renderer(render.Options{
  Directory: "templates", // Specify what path to load the templates from.
  Layout: "layout", // Specify a layout template. Layouts can call {{ yield }} to render the current template.
  Extensions: []string{".tmpl", ".html"}, // Specify extensions to load for templates.
  Funcs: []template.FuncMap{AppHelpers}, // Specify helper function maps for templates to access.
  Delims: render.Delims{"{[{", "}]}"}, // Sets delimiters to the specified strings.
  Charset: "UTF-8", // Sets encoding for json and html content-types. Default is "UTF-8".
  IndentJSON: true, // Output human readable JSON
  IndentXML: true, // Output human readable XML
  HTMLContentType: "application/xhtml+xml", // Output XHTML content type instead of default "text/html"
}))
// ...
~~~

### Loading Templates
By default the `render.Renderer` middleware will attempt to load templates with a '.tmpl' extension from the "templates" directory. Templates are found by traversing the templates directory and are named by path and basename. For instance, the following directory structure:

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
### Layouts
`render.Renderer` provides a `yield` function for layouts to access:
~~~ go
// ...
m.Use(render.Renderer(render.Options{
  Layout: "layout",
}))
// ...
~~~

~~~ html
<!-- templates/layout.tmpl -->
<html>
  <head>
    <title>Martini Plz</title>
  </head>
  <body>
    <!-- Render the current template here -->
    {{ yield }}
  </body>
</html>
~~~

`current` can also be called to get the current template being rendered.
~~~ html
<!-- templates/layout.tmpl -->
<html>
  <head>
    <title>Martini Plz</title>
  </head>
  <body>
    This is the {{ current }} page.
  </body>
</html>
~~~

### Character Encodings
The `render.Renderer` middleware will automatically set the proper Content-Type header based on which function you call. See below for an example of what the default settings would output (note that UTF-8 is the default):
~~~ go
// main.go
package main

import (
  "encoding/xml"

  "github.com/go-martini/martini"
  "github.com/martini-contrib/render"
)

type Greeting struct {
  XMLName xml.Name `xml:"greeting"`
  One     string   `xml:"one,attr"`
  Two     string   `xml:"two,attr"`
}

func main() {
  m := martini.Classic()
  m.Use(render.Renderer())

  // This will set the Content-Type header to "text/html; charset=UTF-8"
  m.Get("/", func(r render.Render) {
    r.HTML(200, "hello", "world")
  })

  // This will set the Content-Type header to "application/json; charset=UTF-8"
  m.Get("/api", func(r render.Render) {
    r.JSON(200, map[string]interface{}{"hello": "world"})
  })

  // This will set the Content-Type header to "text/xml; charset=UTF-8"
  m.Get("/xml", func(r render.Render) {
    r.XML(200, Greeting{One: "hello", Two: "world"})
  })

  // This will set the Content-Type header to "text/plain; charset=UTF-8"
  m.Get("/text", func(r render.Render) {
    r.Text(200, "hello, world")
  })

  m.Run()
}

~~~

In order to change the charset, you can set the `Charset` within the `render.Options` to your encoding value:
~~~ go
// main.go
package main

import (
  "encoding/xml"

  "github.com/go-martini/martini"
  "github.com/martini-contrib/render"
)

type Greeting struct {
  XMLName xml.Name `xml:"greeting"`
  One     string   `xml:"one,attr"`
  Two     string   `xml:"two,attr"`
}

func main() {
  m := martini.Classic()
  m.Use(render.Renderer(render.Options{
    Charset: "ISO-8859-1",
  }))

  // This will set the Content-Type header to "text/html; charset=ISO-8859-1"
  m.Get("/", func(r render.Render) {
    r.HTML(200, "hello", "world")
  })

  // This will set the Content-Type header to "application/json; charset=ISO-8859-1"
  m.Get("/api", func(r render.Render) {
    r.JSON(200, map[string]interface{}{"hello": "world"})
  })

  // This will set the Content-Type header to "text/xml; charset=ISO-8859-1"
  m.Get("/xml", func(r render.Render) {
    r.XML(200, Greeting{One: "hello", Two: "world"})
  })

  // This will set the Content-Type header to "text/plain; charset=ISO-8859-1"
  m.Get("/text", func(r render.Render) {
    r.Text(200, "hello, world")
  })

  m.Run()
}

~~~

## Authors
* [Jeremy Saenz](http://github.com/codegangsta)
* [Cory Jacobsen](http://github.com/unrolled)
# gzip [![wercker status](https://app.wercker.com/status/186d65e4d8160cf274ffc5835e6d9795 "wercker status")](https://app.wercker.com/project/bykey/186d65e4d8160cf274ffc5835e6d9795)
Gzip middleware for Martini.

[API Reference](http://godoc.org/github.com/martini-contrib/gzip)

## Usage

~~~ go
import (
  "github.com/go-martini/martini"
  "github.com/martini-contrib/gzip"
)

func main() {
  m := martini.Classic()
  // gzip every request
  m.Use(gzip.All())
  m.Run()
}

~~~

Make sure to include the Gzip middleware above other middleware that alter the response body (like the render middleware).

## Changing compression level

You can set compression level using gzip.Options:

~~~ go
import (
  "github.com/go-martini/martini"
  "github.com/martini-contrib/gzip"
)

func main() {
  m := martini.Classic()
  // gzip every request with maximum compression level
  m.Use(gzip.All(gzip.Options{
    CompressionLevel: gzip.BestCompression,
  }))
  m.Run()
}
~~~

The compression level can be DefaultCompression or any integer value between BestSpeed and BestCompression inclusive.

## Authors
* [Jeremy Saenz](http://github.com/codegangsta)
* [Shane Logsdon](http://github.com/slogsdon)
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
import "github.com/rcrowley/go-metrics/influxdb"

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
Native Go Zookeeper Client Library
===================================

[![GoDoc](https://godoc.org/github.com/samuel/go-zookeeper?status.svg)](https://godoc.org/github.com/samuel/go-zookeeper)
[![Build Status](https://travis-ci.org/samuel/go-zookeeper.png)](https://travis-ci.org/samuel/go-zookeeper)
[![Coverage Status](https://coveralls.io/repos/github/samuel/go-zookeeper/badge.svg?branch=master)](https://coveralls.io/github/samuel/go-zookeeper?branch=master)

License
-------

3-clause BSD. See LICENSE file.
raft [![Build Status](https://travis-ci.org/hashicorp/raft.png)](https://travis-ci.org/hashicorp/raft)
====

raft is a [Go](http://www.golang.org) library that manages a replicated
log and can be used with an FSM to manage replicated state machines. It
is a library for providing [consensus](http://en.wikipedia.org/wiki/Consensus_(computer_science)).

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

# go

Collection of Open-Source Go libraries and tools.

## Codec

[Codec](https://github.com/ugorji/go/tree/master/codec#readme) is a High Performance and Feature-Rich Idiomatic encode/decode and rpc library for [msgpack](http://msgpack.org) and [Binc](https://github.com/ugorji/binc).

Online documentation is at [http://godoc.org/github.com/ugorji/go/codec].

Install using:

    go get github.com/ugorji/go/codec

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

# inject
--
    import "github.com/codegangsta/inject"

Package inject provides utilities for mapping and injecting dependencies in
various ways.

Language Translations:
* [简体中文](translations/README_zh_cn.md)

## Usage

#### func  InterfaceOf

```go
func InterfaceOf(value interface{}) reflect.Type
```
InterfaceOf dereferences a pointer to an Interface type. It panics if value is
not an pointer to an interface.

#### type Applicator

```go
type Applicator interface {
	// Maps dependencies in the Type map to each field in the struct
	// that is tagged with 'inject'. Returns an error if the injection
	// fails.
	Apply(interface{}) error
}
```

Applicator represents an interface for mapping dependencies to a struct.

#### type Injector

```go
type Injector interface {
	Applicator
	Invoker
	TypeMapper
	// SetParent sets the parent of the injector. If the injector cannot find a
	// dependency in its Type map it will check its parent before returning an
	// error.
	SetParent(Injector)
}
```

Injector represents an interface for mapping and injecting dependencies into
structs and function arguments.

#### func  New

```go
func New() Injector
```
New returns a new Injector.

#### type Invoker

```go
type Invoker interface {
	// Invoke attempts to call the interface{} provided as a function,
	// providing dependencies for function arguments based on Type. Returns
	// a slice of reflect.Value representing the returned values of the function.
	// Returns an error if the injection fails.
	Invoke(interface{}) ([]reflect.Value, error)
}
```

Invoker represents an interface for calling functions via reflection.

#### type TypeMapper

```go
type TypeMapper interface {
	// Maps the interface{} value based on its immediate type from reflect.TypeOf.
	Map(interface{}) TypeMapper
	// Maps the interface{} value based on the pointer of an Interface provided.
	// This is really only useful for mapping a value as an interface, as interfaces
	// cannot at this time be referenced directly without a pointer.
	MapTo(interface{}, interface{}) TypeMapper
	// Provides a possibility to directly insert a mapping based on type and value.
	// This makes it possible to directly map type arguments not possible to instantiate
	// with reflect like unidirectional channels.
	Set(reflect.Type, reflect.Value) TypeMapper
	// Returns the Value that is mapped to the current type. Returns a zeroed Value if
	// the Type has not been mapped.
	Get(reflect.Type) reflect.Value
}
```

TypeMapper represents an interface for mapping interface{} values based on type.
# inject
--
    import "github.com/codegangsta/inject"

inject包提供了多种对实体的映射和依赖注入方式。

## 用法

#### func  InterfaceOf

```go
func InterfaceOf(value interface{}) reflect.Type
```
函数InterfaceOf返回指向接口类型的指针。如果传入的value值不是指向接口的指针，将抛出一个panic异常。

#### type Applicator

```go
type Applicator interface {
    // 在Type map中维持对结构体中每个域的引用并用'inject'来标记
    // 如果注入失败将会返回一个error.
    Apply(interface{}) error
}
```

Applicator接口表示到结构体的依赖映射关系。

#### type Injector

```go
type Injector interface {
    Applicator
    Invoker
    TypeMapper
    // SetParent用来设置父injector. 如果在当前injector的Type map中找不到依赖，
    // 将会继续从它的父injector中找，直到返回error.
    SetParent(Injector)
}
```

Injector接口表示对结构体、函数参数的映射和依赖注入。

#### func  New

```go
func New() Injector
```
New创建并返回一个Injector.

#### type Invoker

```go
type Invoker interface {
    // Invoke尝试将interface{}作为一个函数来调用，并基于Type为函数提供参数。
    // 它将返回reflect.Value的切片，其中存放原函数的返回值。
    // 如果注入失败则返回error.
    Invoke(interface{}) ([]reflect.Value, error)
}
```

Invoker接口表示通过反射进行函数调用。

#### type TypeMapper

```go
type TypeMapper interface {
    // 基于调用reflect.TypeOf得到的类型映射interface{}的值。
    Map(interface{}) TypeMapper
    // 基于提供的接口的指针映射interface{}的值。
    // 该函数仅用来将一个值映射为接口，因为接口无法不通过指针而直接引用到。
    MapTo(interface{}, interface{}) TypeMapper
    // 为直接插入基于类型和值的map提供一种可能性。
    // 它使得这一类直接映射成为可能：无法通过反射直接实例化的类型参数，如单向管道。
    Set(reflect.Type, reflect.Value) TypeMapper
    // 返回映射到当前类型的Value. 如果Type没被映射，将返回对应的零值。
    Get(reflect.Type) reflect.Value
}
```

TypeMapper接口用来表示基于类型到接口值的映射。


## 译者

张强 (qqbunny@yeah.net)Orchestrator Vagrant Instructions
=================================

Orchestrator's Vagrant defaults to installing five (5) CentOS 6.6 boxes in the following replication topology, with a separate "admin" node:

```
db1<->db2
 |     |
 v     v
db3   db4
```

It is possible to override what gets installed by the use of environmental variables:

```
VAGRANT_SERVER_URL defaults to 'https://atlas.hashicorp.com'
VAGRANT_DEFAULT_PROVIDER defaults to 'virtualbox'
VAGRANT_BOX defaults to 'nrel/CentOS-6.6-x86_64'
```

The MySQL configuration is such that it is the minimum required to set up replication. For testing such features as delayed replication, RBR/SBR, GTID, it is simply a matter of editing the `vagrant/dbX-my.cnf` before running the `vagrant up` command.

FAQ
===

Q: By default, there are still a lot of steps that I have to do within each virtual machine to get going

A: That is by design.  Vagrant will execute `db-post-install.sh`, `dbX-post-install.sh`, and `admin-post-install.sh` in the `vagrant/` directory (they are `.gitignore`'d) for any custom work that you want to have done (i.e. build Orchestrator, etc etc)

Q: I run some other distribution of Linux.  Why don't you support that?

A: Pull Requests are welcome!  If you update any of the `vagrant/*.sh` scripts, they must work with at least CentOS 6 and Ubuntu 12

Tips & Tricks
=============

Specify GTID Usage
------------------

If you want to use GTID Replication, you must update all of the `vagrant/dbX-my.cnf` files with the following options in `[mysqld]`:

```
enforce-gtid-consistency
gtid-mode=ON
```

Specify RBR/SBR
---------------

`vagrant/dbX-my.cnf` files are copied directly to the virtual machines.  If you'd like to specify SBR/RBR/MIXED, add one of the following lines to the `[mysqld]` section of the `my.cnf` template:

```
binlog_format=MIXED
binlog_format=STATEMENT
binlog_format=ROW
```

This is not global because we want to be able to test out non-standard replication configurations.

Use VMWare vs. VirtualBox
-------------------------

```
%> export VAGRANT_DEFAULT_PROVIDER='vmware_fusion'
%> vagrant up
```

CentOS
------

This is the default.  Nothing special is required:

```
%> vagrant up
```

Ubuntu
------

```
%> export VAGRANT_SERVER_URL="https://atlas.hashicorp.com"
%> export VAGRANT_BOX='chef/ubuntu-12.04'
%> vagrant up
```

TO DO
=====

- Support other MySQL's (5.5, 5.7, MariaDB)
- Support customizable replication configurations
- Better `my.cnf` templates
# Table of Contents

#### Introduction
- [About](about.md)
- [License](license.md)
- [Download](download.md)
- [Requirements](requirements.md)

#### Setup
- [Installation](install.md): installing the service/binary
- [Configuration](configuration.md): breakdown of major configuration variables by topic.

#### Use
- [Execution](execution.md): running the `orchestrator` service.
- [Executing via command line](executing-via-command-line.md)
- [Using the web interface](using-the-web-interface.md)
- [Using the web API](using-the-web-api.md): achieving automation via HTTP GET requests
- [Using orchestrator-client](orchestrator-client.md): a no binary/config needed script that wraps API calls
- [Scripting samples](script-samples.md)

#### Deployment
- [High availability](high-availability.md): making `orchestrator` highly available
- [Deployment](deployment.md) instructions, hints and tips
- [Shared backend DB](deployment-shared-backend.md) deployment
- [orchestrator/raft](deployment-raft.md) deployment

#### Failure detection & recovery
- [Failure detection](failure-detection.md): how `orchestrator` detects failure, types of failures it can handle
- [Topology recovery](topology-recovery.md): recovery process, promotion and hooks.
- [Key-Value stores](kv.md): master discovery for your apps

#### Operation
- [Status Checks](status-checks.md)
- [Tags](tags.md)

#### Various
- [Docker](docker.md)
- [Security](security.md)
- [SSL and TLS](ssl-and-tls.md)
- [Pseudo GTID](pseudo-gtid.md): refactoring and high availability without using GTID.
- [Agents](agents.md)

#### Meta
- [Risks](risks.md)
- [Gotchas](gotchas.md)
- [Supported topologies and versions](supported-topologies-and-versions.md)
- [Bugs](bugs.md)
- [Contributions](contributions.md)
- [Who uses Orchestrator?](users.md)
- [Presentations](presentations.md)

#### Quick guides

- [FAQ](faq.md)
- [First steps](first-steps.md), a quick introduction to `orchestrator`
- Orchestrator for [developers](developers.md). Read this if you wish to develop/contribute to `orchestrator`.
