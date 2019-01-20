[![Build Status](https://travis-ci.org/valyala/fasthttp.svg)](https://travis-ci.org/valyala/fasthttp)
[![GoDoc](https://godoc.org/github.com/valyala/fasthttp?status.svg)](http://godoc.org/github.com/valyala/fasthttp)
[![Coverage](http://gocover.io/_badge/github.com/valyala/fasthttp)](http://gocover.io/github.com/valyala/fasthttp)
[![Go Report](http://goreportcard.com/badge/valyala/fasthttp)](http://goreportcard.com/report/valyala/fasthttp)

# fasthttp
Fast HTTP implementation for Go.

Currently fasthttp is successfully used by [VertaMedia](https://vertamedia.com/)
in a production serving 100K rps from more than 1M concurrent keep-alive
connections per physical server.

[TechEmpower Benchmark round 12 results](https://www.techempower.com/benchmarks/#section=data-r12&hw=peak&test=plaintext)

[Server Benchmarks](#http-server-performance-comparison-with-nethttp)

[Client Benchmarks](#http-client-comparison-with-nethttp)

[Documentation](https://godoc.org/github.com/valyala/fasthttp)

[Examples from docs](https://godoc.org/github.com/valyala/fasthttp#pkg-examples)

[Code examples](examples)

[Switching from net/http to fasthttp](#switching-from-nethttp-to-fasthttp)

[Fasthttp best practices](#fasthttp-best-practices)

[Tricks with byte buffers](#tricks-with-byte-buffers)

[FAQ](#faq)

# HTTP server performance comparison with [net/http](https://golang.org/pkg/net/http/)

In short, fasthttp server is up to 10 times faster than net/http.
Below are benchmark results.

*GOMAXPROCS=1*

net/http server:
```
$ GOMAXPROCS=1 go test -bench=NetHTTPServerGet -benchmem -benchtime=10s
BenchmarkNetHTTPServerGet1ReqPerConn                	 1000000	     12052 ns/op	    2297 B/op	      29 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn                	 1000000	     12278 ns/op	    2327 B/op	      24 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn               	 2000000	      8903 ns/op	    2112 B/op	      19 allocs/op
BenchmarkNetHTTPServerGet10KReqPerConn              	 2000000	      8451 ns/op	    2058 B/op	      18 allocs/op
BenchmarkNetHTTPServerGet1ReqPerConn10KClients      	  500000	     26733 ns/op	    3229 B/op	      29 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn10KClients      	 1000000	     23351 ns/op	    3211 B/op	      24 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn10KClients     	 1000000	     13390 ns/op	    2483 B/op	      19 allocs/op
BenchmarkNetHTTPServerGet100ReqPerConn10KClients    	 1000000	     13484 ns/op	    2171 B/op	      18 allocs/op
```

fasthttp server:
```
$ GOMAXPROCS=1 go test -bench=kServerGet -benchmem -benchtime=10s
BenchmarkServerGet1ReqPerConn                       	10000000	      1559 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet2ReqPerConn                       	10000000	      1248 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet10ReqPerConn                      	20000000	       797 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet10KReqPerConn                     	20000000	       716 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet1ReqPerConn10KClients             	10000000	      1974 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet2ReqPerConn10KClients             	10000000	      1352 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet10ReqPerConn10KClients            	20000000	       789 ns/op	       2 B/op	       0 allocs/op
BenchmarkServerGet100ReqPerConn10KClients           	20000000	       604 ns/op	       0 B/op	       0 allocs/op
```

*GOMAXPROCS=4*

net/http server:
```
$ GOMAXPROCS=4 go test -bench=NetHTTPServerGet -benchmem -benchtime=10s
BenchmarkNetHTTPServerGet1ReqPerConn-4                  	 3000000	      4529 ns/op	    2389 B/op	      29 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn-4                  	 5000000	      3896 ns/op	    2418 B/op	      24 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn-4                 	 5000000	      3145 ns/op	    2160 B/op	      19 allocs/op
BenchmarkNetHTTPServerGet10KReqPerConn-4                	 5000000	      3054 ns/op	    2065 B/op	      18 allocs/op
BenchmarkNetHTTPServerGet1ReqPerConn10KClients-4        	 1000000	     10321 ns/op	    3710 B/op	      30 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn10KClients-4        	 2000000	      7556 ns/op	    3296 B/op	      24 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn10KClients-4       	 5000000	      3905 ns/op	    2349 B/op	      19 allocs/op
BenchmarkNetHTTPServerGet100ReqPerConn10KClients-4      	 5000000	      3435 ns/op	    2130 B/op	      18 allocs/op
```

fasthttp server:
```
$ GOMAXPROCS=4 go test -bench=kServerGet -benchmem -benchtime=10s
BenchmarkServerGet1ReqPerConn-4                         	10000000	      1141 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet2ReqPerConn-4                         	20000000	       707 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet10ReqPerConn-4                        	30000000	       341 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet10KReqPerConn-4                       	50000000	       310 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet1ReqPerConn10KClients-4               	10000000	      1119 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet2ReqPerConn10KClients-4               	20000000	       644 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet10ReqPerConn10KClients-4              	30000000	       346 ns/op	       0 B/op	       0 allocs/op
BenchmarkServerGet100ReqPerConn10KClients-4             	50000000	       282 ns/op	       0 B/op	       0 allocs/op
```

# HTTP client comparison with net/http

In short, fasthttp client is up to 10 times faster than net/http.
Below are benchmark results.

*GOMAXPROCS=1*

net/http client:
```
$ GOMAXPROCS=1 go test -bench='HTTPClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
BenchmarkNetHTTPClientDoFastServer                  	 1000000	     12567 ns/op	    2616 B/op	      35 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1TCP               	  200000	     67030 ns/op	    5028 B/op	      56 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10TCP              	  300000	     51098 ns/op	    5031 B/op	      56 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100TCP             	  300000	     45096 ns/op	    5026 B/op	      55 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1Inmemory          	  500000	     24779 ns/op	    5035 B/op	      57 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10Inmemory         	 1000000	     26425 ns/op	    5035 B/op	      57 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100Inmemory        	  500000	     28515 ns/op	    5045 B/op	      57 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1000Inmemory       	  500000	     39511 ns/op	    5096 B/op	      56 allocs/op
```

fasthttp client:
```
$ GOMAXPROCS=1 go test -bench='kClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
BenchmarkClientDoFastServer                         	20000000	       865 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd1TCP                      	 1000000	     18711 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd10TCP                     	 1000000	     14664 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd100TCP                    	 1000000	     14043 ns/op	       1 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd1Inmemory                 	 5000000	      3965 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd10Inmemory                	 3000000	      4060 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd100Inmemory               	 5000000	      3396 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd1000Inmemory              	 5000000	      3306 ns/op	       2 B/op	       0 allocs/op
```

*GOMAXPROCS=4*

net/http client:
```
$ GOMAXPROCS=4 go test -bench='HTTPClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
BenchmarkNetHTTPClientDoFastServer-4                    	 2000000	      8774 ns/op	    2619 B/op	      35 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1TCP-4                 	  500000	     22951 ns/op	    5047 B/op	      56 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10TCP-4                	 1000000	     19182 ns/op	    5037 B/op	      55 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100TCP-4               	 1000000	     16535 ns/op	    5031 B/op	      55 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1Inmemory-4            	 1000000	     14495 ns/op	    5038 B/op	      56 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10Inmemory-4           	 1000000	     10237 ns/op	    5034 B/op	      56 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100Inmemory-4          	 1000000	     10125 ns/op	    5045 B/op	      56 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1000Inmemory-4         	 1000000	     11132 ns/op	    5136 B/op	      56 allocs/op
```

fasthttp client:
```
$ GOMAXPROCS=4 go test -bench='kClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
BenchmarkClientDoFastServer-4                           	50000000	       397 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd1TCP-4                        	 2000000	      7388 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd10TCP-4                       	 2000000	      6689 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd100TCP-4                      	 3000000	      4927 ns/op	       1 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd1Inmemory-4                   	10000000	      1604 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd10Inmemory-4                  	10000000	      1458 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd100Inmemory-4                 	10000000	      1329 ns/op	       0 B/op	       0 allocs/op
BenchmarkClientGetEndToEnd1000Inmemory-4                	10000000	      1316 ns/op	       5 B/op	       0 allocs/op
```

# Switching from net/http to fasthttp

Unfortunately, fasthttp doesn't provide API identical to net/http.
See the [FAQ](#faq) for details.
There is [net/http -> fasthttp handler converter](https://godoc.org/github.com/valyala/fasthttp/fasthttpadaptor),
but it is advisable writing fasthttp request handlers by hands for gaining
all the fasthttp advantages (especially high performance :) ).

Important points:

* Fasthttp works with [RequestHandler functions](https://godoc.org/github.com/valyala/fasthttp#RequestHandler)
instead of objects implementing [Handler interface](https://golang.org/pkg/net/http/#Handler).
Fortunately, it is easy to pass bound struct methods to fasthttp:

  ```go
  type MyHandler struct {
  	foobar string
  }

  // request handler in net/http style, i.e. method bound to MyHandler struct.
  func (h *MyHandler) HandleFastHTTP(ctx *fasthttp.RequestCtx) {
  	// notice that we may access MyHandler properties here - see h.foobar.
  	fmt.Fprintf(ctx, "Hello, world! Requested path is %q. Foobar is %q",
  		ctx.Path(), h.foobar)
  }

  // request handler in fasthttp style, i.e. just plain function.
  func fastHTTPHandler(ctx *fasthttp.RequestCtx) {
  	fmt.Fprintf(ctx, "Hi there! RequestURI is %q", ctx.RequestURI())
  }

  // pass bound struct method to fasthttp
  myHandler := &MyHandler{
  	foobar: "foobar",
  }
  fasthttp.ListenAndServe(":8080", myHandler.HandleFastHTTP)

  // pass plain function to fasthttp
  fasthttp.ListenAndServe(":8081", fastHTTPHandler)
  ```

* The [RequestHandler](https://godoc.org/github.com/valyala/fasthttp#RequestHandler)
accepts only one argument - [RequestCtx](https://godoc.org/github.com/valyala/fasthttp#RequestCtx).
It contains all the functionality required for http request processing
and response writing. Below is an example of a simple request handler conversion
from net/http to fasthttp.

  ```go
  // net/http request handler
  requestHandler := func(w http.ResponseWriter, r *http.Request) {
  	switch r.URL.Path {
  	case "/foo":
  		fooHandler(w, r)
  	case "/bar":
  		barHandler(w, r)
  	default:
  		http.Error(w, "Unsupported path", http.StatusNotFound)
  	}
  }
  ```

  ```go
  // the corresponding fasthttp request handler
  requestHandler := func(ctx *fasthttp.RequestCtx) {
  	switch string(ctx.Path()) {
  	case "/foo":
  		fooHandler(ctx)
  	case "/bar":
  		barHandler(ctx)
  	default:
  		ctx.Error("Unsupported path", fasthttp.StatusNotFound)
  	}
  }
  ```

* Fasthttp allows setting response headers and writing response body
in arbitrary order. There is no 'headers first, then body' restriction
like in net/http. The following code is valid for fasthttp:

  ```go
  requestHandler := func(ctx *fasthttp.RequestCtx) {
  	// set some headers and status code first
  	ctx.SetContentType("foo/bar")
  	ctx.SetStatusCode(fasthttp.StatusOK)

  	// then write the first part of body
  	fmt.Fprintf(ctx, "this is the first part of body\n")

  	// then set more headers
  	ctx.Response.Header.Set("Foo-Bar", "baz")

  	// then write more body
  	fmt.Fprintf(ctx, "this is the second part of body\n")

  	// then override already written body
  	ctx.SetBody([]byte("this is completely new body contents"))

  	// then update status code
  	ctx.SetStatusCode(fasthttp.StatusNotFound)

  	// basically, anything may be updated many times before
  	// returning from RequestHandler.
  	//
  	// Unlike net/http fasthttp doesn't put response to the wire until
  	// returning from RequestHandler.
  }
  ```

* Fasthttp doesn't provide [ServeMux](https://golang.org/pkg/net/http/#ServeMux),
but there are more powerful third-party routers and web frameworks
with fasthttp support exist:

  * [Iris](https://github.com/kataras/iris)
  * [fasthttp-routing](https://github.com/qiangxue/fasthttp-routing)
  * [fasthttprouter](https://github.com/buaazp/fasthttprouter)
  * [echo v2](https://github.com/labstack/echo)

  Net/http code with simple ServeMux is trivially converted to fasthttp code:

  ```go
  // net/http code

  m := &http.ServeMux{}
  m.HandleFunc("/foo", fooHandlerFunc)
  m.HandleFunc("/bar", barHandlerFunc)
  m.Handle("/baz", bazHandler)

  http.ListenAndServe(":80", m)
  ```

  ```go
  // the corresponding fasthttp code
  m := func(ctx *fasthttp.RequestCtx) {
  	switch string(ctx.Path()) {
  	case "/foo":
  		fooHandlerFunc(ctx)
  	case "/bar":
  		barHandlerFunc(ctx)
  	case "/baz":
  		bazHandler.HandlerFunc(ctx)
  	default:
  		ctx.Error("not found", fasthttp.StatusNotFound)
  	}
  }

  fastttp.ListenAndServe(":80", m)
  ```

* net/http -> fasthttp conversion table:

  * All the pseudocode below assumes w, r and ctx have these types:
  ```go
	var (
		w http.ResponseWriter
		r *http.Request
		ctx *fasthttp.RequestCtx
	)
  ```
  * r.Body -> [ctx.PostBody()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.PostBody)
  * r.URL.Path -> [ctx.Path()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Path)
  * r.URL -> [ctx.URI()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.URI)
  * r.Method -> [ctx.Method()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Method)
  * r.Header -> [ctx.Request.Header](https://godoc.org/github.com/valyala/fasthttp#RequestHeader)
  * r.Header.Get() -> [ctx.Request.Header.Peek()](https://godoc.org/github.com/valyala/fasthttp#RequestHeader.Peek)
  * r.Host -> [ctx.Host()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Host)
  * r.Form -> [ctx.QueryArgs()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.QueryArgs) +
  [ctx.PostArgs()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.PostArgs)
  * r.PostForm -> [ctx.PostArgs()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.PostArgs)
  * r.FormValue() -> [ctx.FormValue()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.FormValue)
  * r.FormFile() -> [ctx.FormFile()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.FormFile)
  * r.MultipartForm -> [ctx.MultipartForm()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.MultipartForm)
  * r.RemoteAddr -> [ctx.RemoteAddr()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.RemoteAddr)
  * r.RequestURI -> [ctx.RequestURI()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.RequestURI)
  * r.TLS -> [ctx.IsTLS()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.IsTLS)
  * r.Cookie() -> [ctx.Request.Header.Cookie()](https://godoc.org/github.com/valyala/fasthttp#RequestHeader.Cookie)
  * r.Referer() -> [ctx.Referer()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Referer)
  * r.UserAgent() -> [ctx.UserAgent()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.UserAgent)
  * w.Header() -> [ctx.Response.Header](https://godoc.org/github.com/valyala/fasthttp#ResponseHeader)
  * w.Header().Set() -> [ctx.Response.Header.Set()](https://godoc.org/github.com/valyala/fasthttp#ResponseHeader.Set)
  * w.Header().Set("Content-Type") -> [ctx.SetContentType()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.SetContentType)
  * w.Header().Set("Set-Cookie") -> [ctx.Response.Header.SetCookie()](https://godoc.org/github.com/valyala/fasthttp#ResponseHeader.SetCookie)
  * w.Write() -> [ctx.Write()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Write),
  [ctx.SetBody()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.SetBody),
  [ctx.SetBodyStream()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.SetBodyStream),
  [ctx.SetBodyStreamWriter()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.SetBodyStreamWriter)
  * w.WriteHeader() -> [ctx.SetStatusCode()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.SetStatusCode)
  * w.(http.Hijacker).Hijack() -> [ctx.Hijack()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Hijack)
  * http.Error() -> [ctx.Error()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Error)
  * http.FileServer() -> [fasthttp.FSHandler()](https://godoc.org/github.com/valyala/fasthttp#FSHandler),
  [fasthttp.FS](https://godoc.org/github.com/valyala/fasthttp#FS)
  * http.ServeFile() -> [fasthttp.ServeFile()](https://godoc.org/github.com/valyala/fasthttp#ServeFile)
  * http.Redirect() -> [ctx.Redirect()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Redirect)
  * http.NotFound() -> [ctx.NotFound()](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.NotFound)
  * http.StripPrefix() -> [fasthttp.PathRewriteFunc](https://godoc.org/github.com/valyala/fasthttp#PathRewriteFunc)

* *VERY IMPORTANT!* Fasthttp disallows holding references
to [RequestCtx](https://godoc.org/github.com/valyala/fasthttp#RequestCtx) or to its'
members after returning from [RequestHandler](https://godoc.org/github.com/valyala/fasthttp#RequestHandler).
Otherwise [data races](http://blog.golang.org/race-detector) are inevitable.
Carefully inspect all the net/http request handlers converted to fasthttp whether
they retain references to RequestCtx or to its' members after returning.
RequestCtx provides the following _band aids_ for this case:

  * Wrap RequestHandler into [TimeoutHandler](https://godoc.org/github.com/valyala/fasthttp#TimeoutHandler).
  * Call [TimeoutError](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.TimeoutError)
  before returning from RequestHandler if there are references to RequestCtx or to its' members.
  See [the example](https://godoc.org/github.com/valyala/fasthttp#example-RequestCtx-TimeoutError)
  for more details.

Use brilliant tool - [race detector](http://blog.golang.org/race-detector) -
for detecting and eliminating data races in your program. If you detected
data race related to fasthttp in your program, then there is high probability
you forgot calling [TimeoutError](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.TimeoutError)
before returning from [RequestHandler](https://godoc.org/github.com/valyala/fasthttp#RequestHandler).

* Blind switching from net/http to fasthttp won't give you performance boost.
While fasthttp is optimized for speed, its' performance may be easily saturated
by slow [RequestHandler](https://godoc.org/github.com/valyala/fasthttp#RequestHandler).
So [profile](http://blog.golang.org/profiling-go-programs) and optimize your
code after switching to fasthttp. For instance, use [quicktemplate](https://github.com/valyala/quicktemplate)
instead of [html/template](https://golang.org/pkg/html/template/).

* See also [fasthttputil](https://godoc.org/github.com/valyala/fasthttp/fasthttputil),
[fasthttpadaptor](https://godoc.org/github.com/valyala/fasthttp/fasthttpadaptor) and
[expvarhandler](https://godoc.org/github.com/valyala/fasthttp/expvarhandler).


# Performance optimization tips for multi-core systems

* Use [reuseport](https://godoc.org/github.com/valyala/fasthttp/reuseport) listener.
* Run a separate server instance per CPU core with GOMAXPROCS=1.
* Pin each server instance to a separate CPU core using [taskset](http://linux.die.net/man/1/taskset).
* Ensure the interrupts of multiqueue network card are evenly distributed between CPU cores.
  See [this article](https://blog.cloudflare.com/how-to-achieve-low-latency/) for details.
* Use Go 1.6 as it provides some considerable performance improvements.


# Fasthttp best practices

* Do not allocate objects and `[]byte` buffers - just reuse them as much
  as possible. Fasthttp API design encourages this.
* [sync.Pool](https://golang.org/pkg/sync/#Pool) is your best friend.
* [Profile your program](http://blog.golang.org/profiling-go-programs)
  in production.
  `go tool pprof --alloc_objects your-program mem.pprof` usually gives better
  insights for optimization opportunities than `go tool pprof your-program cpu.pprof`.
* Write [tests and benchmarks](https://golang.org/pkg/testing/) for hot paths.
* Avoid conversion between `[]byte` and `string`, since this may result in memory
  allocation+copy. Fasthttp API provides functions for both `[]byte` and `string` -
  use these functions instead of converting manually between `[]byte` and `string`.
  There are some exceptions - see [this wiki page](https://github.com/golang/go/wiki/CompilerOptimizations#string-and-byte)
  for more details.
* Verify your tests and production code under
  [race detector](https://golang.org/doc/articles/race_detector.html) on a regular basis.
* Prefer [quicktemplate](https://github.com/valyala/quicktemplate) instead of
  [html/template](https://golang.org/pkg/html/template/) in your webserver.


# Tricks with `[]byte` buffers

The following tricks are used by fasthttp. Use them in your code too.

* Standard Go functions accept nil buffers
```go
var (
	// both buffers are uninitialized
	dst []byte
	src []byte
)
dst = append(dst, src...)  // is legal if dst is nil and/or src is nil
copy(dst, src)  // is legal if dst is nil and/or src is nil
(string(src) == "")  // is true if src is nil
(len(src) == 0)  // is true if src is nil
src = src[:0]  // works like a charm with nil src

// this for loop doesn't panic if src is nil
for i, ch := range src {
	doSomething(i, ch)
}
```

So throw away nil checks for `[]byte` buffers from you code. For example,
```go
srcLen := 0
if src != nil {
	srcLen = len(src)
}
```

becomes

```go
srcLen := len(src)
```

* String may be appended to `[]byte` buffer with `append`
```go
dst = append(dst, "foobar"...)
```

* `[]byte` buffer may be extended to its' capacity.
```go
buf := make([]byte, 100)
a := buf[:10]  // len(a) == 10, cap(a) == 100.
b := a[:100]  // is valid, since cap(a) == 100.
```

* All fasthttp functions accept nil `[]byte` buffer
```go
statusCode, body, err := fasthttp.Get(nil, "http://google.com/")
uintBuf := fasthttp.AppendUint(nil, 1234)
```

# FAQ

* *Why creating yet another http package instead of optimizing net/http?*

  Because net/http API limits many optimization opportunities.
  For example:
  * net/http Request object lifetime isn't limited by request handler execution
    time. So the server must create new request object per each request instead
    of reusing existing objects like fasthttp do.
  * net/http headers are stored in a `map[string][]string`. So the server
    must parse all the headers, convert them from `[]byte` to `string` and put
    them into the map before calling user-provided request handler.
    This all requires unnecessary memory allocations avoided by fasthttp.
  * net/http client API requires creating new response object per each request.

* *Why fasthttp API is incompatible with net/http?*

  Because net/http API limits many optimization opportunities. See the answer
  above for more details. Also certain net/http API parts are suboptimal
  for use:
  * Compare [net/http connection hijacking](https://golang.org/pkg/net/http/#Hijacker)
    to [fasthttp connection hijacking](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Hijack).
  * Compare [net/http Request.Body reading](https://golang.org/pkg/net/http/#Request)
    to [fasthttp request body reading](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.PostBody).

* *Why fasthttp doesn't support HTTP/2.0 and WebSockets?*

  There are [plans](TODO) for adding HTTP/2.0 and WebSockets support
  in the future.
  In the mean time, third parties may use [RequestCtx.Hijack](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.Hijack)
  for implementing these goodies. See [the first third-party websocket implementation on the top of fasthttp](https://github.com/leavengood/websocket).

* *Are there known net/http advantages comparing to fasthttp?*

  Yes:
  * net/http supports [HTTP/2.0 starting from go1.6](https://http2.golang.org/).
  * net/http API is stable, while fasthttp API constantly evolves.
  * net/http handles more HTTP corner cases.
  * net/http should contain less bugs, since it is used and tested by much
    wider audience.
  * net/http works on Go older than 1.5.

* *Why fasthttp API prefers returning `[]byte` instead of `string`?*

  Because `[]byte` to `string` conversion isn't free - it requires memory
  allocation and copy. Feel free wrapping returned `[]byte` result into
  `string()` if you prefer working with strings instead of byte slices.
  But be aware that this has non-zero overhead.

* *Which GO versions are supported by fasthttp?*

  Go1.5+. Older versions won't be supported, since their standard package
  [miss useful functions](https://github.com/valyala/fasthttp/issues/5).

* *Please provide real benchmark data and sever information*

  See [this issue](https://github.com/valyala/fasthttp/issues/4).

* *Are there plans to add request routing to fasthttp?*

  There are no plans to add request routing into fasthttp.
  Use third-party routers and web frameworks with fasthttp support:

    * [Iris](https://github.com/kataras/iris)
    * [fasthttp-routing](https://github.com/qiangxue/fasthttp-routing)
    * [fasthttprouter](https://github.com/buaazp/fasthttprouter)
    * [echo v2](https://github.com/labstack/echo)

  See also [this issue](https://github.com/valyala/fasthttp/issues/9) for more info.

* *I detected data race in fasthttp!*

  Cool! [File a bug](https://github.com/valyala/fasthttp/issues/new). But before
  doing this check the following in your code:

  * Make sure there are no references to [RequestCtx](https://godoc.org/github.com/valyala/fasthttp#RequestCtx)
  or to its' members after returning from [RequestHandler](https://godoc.org/github.com/valyala/fasthttp#RequestHandler).
  * Make sure you call [TimeoutError](https://godoc.org/github.com/valyala/fasthttp#RequestCtx.TimeoutError)
  before returning from [RequestHandler](https://godoc.org/github.com/valyala/fasthttp#RequestHandler)
  if there are references to [RequestCtx](https://godoc.org/github.com/valyala/fasthttp#RequestCtx)
  or to its' members, which may be accessed by other goroutines.

* *I didn't find an answer for my question here*

  Try exploring [these questions](https://github.com/valyala/fasthttp/issues?q=label%3Aquestion).
![Gomega: Ginkgo's Preferred Matcher Library](http://onsi.github.io/gomega/images/gomega.png)

[![Build Status](https://travis-ci.org/onsi/gomega.png)](https://travis-ci.org/onsi/gomega)

Jump straight to the [docs](http://onsi.github.io/gomega/) to learn about Gomega, including a list of [all available matchers](http://onsi.github.io/gomega/#provided-matchers).

To discuss Gomega and get updates, join the [google group](https://groups.google.com/d/forum/ginkgo-and-gomega).

## [Ginkgo](http://github.com/onsi/ginkgo): a BDD Testing Framework for Golang

Learn more about Ginkgo [here](http://onsi.github.io/ginkgo/)

## License

Gomega is MIT-Licensed

The `ConsistOf` matcher uses [goraph](https://github.com/amitkgupta/goraph) which is embedded in the source to simplify distribution.  goraph has an MIT license.
![Ginkgo: A Golang BDD Testing Framework](http://onsi.github.io/ginkgo/images/ginkgo.png)

[![Build Status](https://travis-ci.org/onsi/ginkgo.png)](https://travis-ci.org/onsi/ginkgo)

Jump to the [docs](http://onsi.github.io/ginkgo/) to learn more.  To start rolling your Ginkgo tests *now* [keep reading](#set-me-up)!

To discuss Ginkgo and get updates, join the [google group](https://groups.google.com/d/forum/ginkgo-and-gomega).

## Feature List

- Ginkgo uses Go's `testing` package and can live alongside your existing `testing` tests.  It's easy to [bootstrap](http://onsi.github.io/ginkgo/#bootstrapping-a-suite) and start writing your [first tests](http://onsi.github.io/ginkgo/#adding-specs-to-a-suite)

- Structure your BDD-style tests expressively:
    - Nestable [`Describe` and `Context` container blocks](http://onsi.github.io/ginkgo/#organizing-specs-with-containers-describe-and-context)
    - [`BeforeEach` and `AfterEach` blocks](http://onsi.github.io/ginkgo/#extracting-common-setup-beforeeach) for setup and teardown
    - [`It` blocks](http://onsi.github.io/ginkgo/#individual-specs-) that hold your assertions
    - [`JustBeforeEach` blocks](http://onsi.github.io/ginkgo/#separating-creation-and-configuration-justbeforeeach) that separate creation from configuration (also known as the subject action pattern).
    - [`BeforeSuite` and `AfterSuite` blocks](http://onsi.github.io/ginkgo/#global-setup-and-teardown-beforesuite-and-aftersuite) to prep for and cleanup after a suite.

- A comprehensive test runner that lets you:
    - Mark specs as [pending](http://onsi.github.io/ginkgo/#pending-specs)
    - [Focus](http://onsi.github.io/ginkgo/#focused-specs) individual specs, and groups of specs, either programmatically or on the command line
    - Run your tests in [random order](http://onsi.github.io/ginkgo/#spec-permutation), and then reuse random seeds to replicate the same order.
    - Break up your test suite into parallel processes for straightforward [test parallelization](http://onsi.github.io/ginkgo/#parallel-specs)

- `ginkgo`: a command line interface with plenty of handy command line arguments for [running your tests](http://onsi.github.io/ginkgo/#running-tests) and [generating](http://onsi.github.io/ginkgo/#generators) test files.  Here are a few choice examples:
    - `ginkgo -nodes=N` runs your tests in `N` parallel processes and print out coherent output in realtime
    - `ginkgo -cover` runs your tests using Golang's code coverage tool
    - `ginkgo convert` converts an XUnit-style `testing` package to a Ginkgo-style package
    - `ginkgo -focus="REGEXP"` and `ginkgo -skip="REGEXP"` allow you to specify a subset of tests to run via regular expression
    - `ginkgo -r` runs all tests suites under the current directory
    - `ginkgo -v` prints out identifying information for each tests just before it runs

    And much more: run `ginkgo help` for details!

    The `ginkgo` CLI is convenient, but purely optional -- Ginkgo works just fine with `go test`

- `ginkgo watch` [watches](https://onsi.github.io/ginkgo/#watching-for-changes) packages *and their dependencies* for changes, then reruns tests.  Run tests immediately as you develop!

- Built-in support for testing [asynchronicity](http://onsi.github.io/ginkgo/#asynchronous-tests)

- Built-in support for [benchmarking](http://onsi.github.io/ginkgo/#benchmark-tests) your code.  Control the number of benchmark samples as you gather runtimes and other, arbitrary, bits of numerical information about your code. 

- [Completions for Sublime Text](https://github.com/onsi/ginkgo-sublime-completions): just use [Package Control](https://sublime.wbond.net/) to install `Ginkgo Completions`.

- Straightforward support for third-party testing libraries such as [Gomock](https://code.google.com/p/gomock/) and [Testify](https://github.com/stretchr/testify).  Check out the [docs](http://onsi.github.io/ginkgo/#third-party-integrations) for details.

- A modular architecture that lets you easily:
    - Write [custom reporters](http://onsi.github.io/ginkgo/#writing-custom-reporters) (for example, Ginkgo comes with a [JUnit XML reporter](http://onsi.github.io/ginkgo/#generating-junit-xml-output) and a TeamCity reporter).
    - [Adapt an existing matcher library (or write your own!)](http://onsi.github.io/ginkgo/#using-other-matcher-libraries) to work with Ginkgo

## [Gomega](http://github.com/onsi/gomega): Ginkgo's Preferred Matcher Library

Ginkgo is best paired with Gomega.  Learn more about Gomega [here](http://onsi.github.io/gomega/)

## [Agouti](http://github.com/sclevine/agouti): A Golang Acceptance Testing Framework

Agouti allows you run WebDriver integration tests.  Learn more about Agouti [here](http://agouti.org)

## Set Me Up!

You'll need Golang v1.3+ (Ubuntu users: you probably have Golang v1.0 -- you'll need to upgrade!)

```bash

go get github.com/onsi/ginkgo/ginkgo  # installs the ginkgo CLI
go get github.com/onsi/gomega         # fetches the matcher library

cd path/to/package/you/want/to/test

ginkgo bootstrap # set up a new ginkgo suite
ginkgo generate  # will create a sample test file.  edit this file and add your tests then...

go test # to run your tests

ginkgo  # also runs your tests

```

## I'm new to Go: What are my testing options?

Of course, I heartily recommend [Ginkgo](https://github.com/onsi/ginkgo) and [Gomega](https://github.com/onsi/gomega).  Both packages are seeing heavy, daily, production use on a number of projects and boast a mature and comprehensive feature-set.

With that said, it's great to know what your options are :)

### What Golang gives you out of the box

Testing is a first class citizen in Golang, however Go's built-in testing primitives are somewhat limited: The [testing](http://golang.org/pkg/testing) package provides basic XUnit style tests and no assertion library.

### Matcher libraries for Golang's XUnit style tests

A number of matcher libraries have been written to augment Go's built-in XUnit style tests.  Here are two that have gained traction:

- [testify](https://github.com/stretchr/testify)
- [gocheck](http://labix.org/gocheck)

You can also use Ginkgo's matcher library [Gomega](https://github.com/onsi/gomega) in [XUnit style tests](http://onsi.github.io/gomega/#using-gomega-with-golangs-xunitstyle-tests)

### BDD style testing frameworks

There are a handful of BDD-style testing frameworks written for Golang.  Here are a few:

- [Ginkgo](https://github.com/onsi/ginkgo) ;)
- [GoConvey](https://github.com/smartystreets/goconvey) 
- [Goblin](https://github.com/franela/goblin)
- [Mao](https://github.com/azer/mao)
- [Zen](https://github.com/pranavraja/zen)

Finally, @shageman has [put together](https://github.com/shageman/gotestit) a comprehensive comparison of golang testing libraries.

Go explore!

## License

Ginkgo is MIT-Licensed
# go-dockerclient

[![Travis](https://img.shields.io/travis/fsouza/go-dockerclient.svg?style=flat-square)](https://travis-ci.org/fsouza/go-dockerclient)
[![GoDoc](https://img.shields.io/badge/api-Godoc-blue.svg?style=flat-square)](https://godoc.org/github.com/fsouza/go-dockerclient)

This package presents a client for the Docker remote API. It also provides
support for the extensions in the [Swarm API](https://docs.docker.com/swarm/swarm-api/).

This package also provides support for docker's network API, which is a simple
passthrough to the libnetwork remote API.  Note that docker's network API is
only available in docker 1.8 and above, and only enabled in docker if
DOCKER_EXPERIMENTAL is defined during the docker build process.

For more details, check the [remote API documentation](http://docs.docker.com/engine/reference/api/docker_remote_api/).

## Vendoring

If you are having issues with Go 1.5 and have `GO15VENDOREXPERIMENT` set with an application that has go-dockerclient vendored,
please update your vendoring of go-dockerclient :) We recently moved the `vendor` directory to `external` so that go-dockerclient
is compatible with this configuration. See [338](https://github.com/fsouza/go-dockerclient/issues/338) and [339](https://github.com/fsouza/go-dockerclient/pull/339)
for details.

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
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/Sirupsen/logrus.svg?branch=master)](https://travis-ci.org/Sirupsen/logrus)&nbsp;[![godoc reference](https://godoc.org/github.com/Sirupsen/logrus?status.png)][godoc]

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc]. **Please note the Logrus API is not
yet stable (pre 1.0). Logrus itself is completely stable and has been used in
many large deployments. The core API is unlikely to change much but please
version control your Logrus to make sure you aren't fetching latest `master` on
every build.**

Nicely color-coded in development (when a TTY is attached, otherwise just
plain text):

![Colored](http://i.imgur.com/PY7qMwd.png)

With `log.Formatter = new(logrus.JSONFormatter)`, for easy parsing by logstash
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

With the default `log.Formatter = new(&log.TextFormatter{})` when a TTY is not
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
| [InfluxDB](https://github.com/Abramovic/logrus_influxdb) | Hook for logging to influxdb |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [DeferPanic](https://github.com/deferpanic/dp-logrus) | Hook for logging to DeferPanic |

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
* `logrus/formatters/logstash.LogstashFormatter`. Logs fields as [Logstash](http://logstash.net) Events.

    ```go
      logrus.SetFormatter(&logstash.LogstashFormatter{Type: "application_name"})
    ```

Third party logging formatters:

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

[godoc]: https://godoc.org/github.com/Sirupsen/logrus
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
[![GoDoc](https://godoc.org/github.com/docker/go-units?status.svg)](https://godoc.org/github.com/docker/go-units)

# Introduction

go-units is a library to transform human friendly measurements into machine friendly values.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-units) for examples and documentation.

## Copyright and license

Copyright © 2015 Docker, Inc. All rights reserved, except as follows. Code
is released under the Apache 2.0 license. The README.md file, and files in the
"docs" folder are licensed under the Creative Commons Attribution 4.0
International License under the terms and conditions set forth in the file
"LICENSE.docs". You may obtain a duplicate copy of the same license, titled
CC-BY-SA-4.0, at http://creativecommons.org/licenses/by/4.0/.
This code provides helper functions for dealing with archive files.
# go-jmespath - A JMESPath implementation in Go

[![Build Status](https://img.shields.io/travis/jmespath/go-jmespath.svg)](https://travis-ci.org/jmespath/go-jmespath)



See http://jmespath.org for more info.
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/Sirupsen/logrus.svg?branch=master)](https://travis-ci.org/Sirupsen/logrus)&nbsp;[![godoc reference](https://godoc.org/github.com/Sirupsen/logrus?status.png)][godoc]

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc]. **Please note the Logrus API is not
yet stable (pre 1.0). Logrus itself is completely stable and has been used in
many large deployments. The core API is unlikely to change much but please
version control your Logrus to make sure you aren't fetching latest `master` on
every build.**

Nicely color-coded in development (when a TTY is attached, otherwise just
plain text):

![Colored](http://i.imgur.com/PY7qMwd.png)

With `log.Formatter = new(logrus.JSONFormatter)`, for easy parsing by logstash
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

With the default `log.Formatter = new(logrus.TextFormatter)` when a TTY is not
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
  "github.com/Sirupsen/logrus/hooks/airbrake"
)

func init() {
  // Log as JSON instead of the default ASCII formatter.
  log.SetFormatter(&log.JSONFormatter{})

  // Use the Airbrake hook to report errors that have Error severity or above to
  // an exception tracker. You can create custom hooks, see the Hooks section.
  log.AddHook(airbrake.NewHook("https://example.com", "xyz", "development"))

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
  "github.com/Sirupsen/logrus/hooks/airbrake"
  "github.com/Sirupsen/logrus/hooks/syslog"
  "log/syslog"
)

func init() {
  log.AddHook(airbrake.NewHook("https://example.com", "xyz", "development"))

  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")
  if err != nil {
    log.Error("Unable to connect to local syslog daemon")
  } else {
    log.AddHook(hook)
  }
}
```


| Hook  | Description |
| ----- | ----------- |
| [Airbrake](https://github.com/Sirupsen/logrus/blob/master/hooks/airbrake/airbrake.go) | Send errors to an exception tracking service compatible with the Airbrake API. Uses [`airbrake-go`](https://github.com/tobi/airbrake-go) behind the scenes. |
| [Papertrail](https://github.com/Sirupsen/logrus/blob/master/hooks/papertrail/papertrail.go) | Send errors to the Papertrail hosted logging service via UDP. |
| [Syslog](https://github.com/Sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [BugSnag](https://github.com/Sirupsen/logrus/blob/master/hooks/bugsnag/bugsnag.go) | Send errors to the Bugsnag exception tracking service. |
| [Hiprus](https://github.com/nubo/hiprus) | Send errors to a channel in hipchat. |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Journalhook](https://github.com/wercker/journalhook) | Hook for logging to `systemd-journald` |
| [Graylog](https://github.com/gemnasium/logrus-hooks/tree/master/graylog) | Hook for logging to [Graylog](http://graylog2.org/) |

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
    log.SetFormatter(logrus.JSONFormatter)
  } else {
    // The TextFormatter is default, you don't actually have to do this.
    log.SetFormatter(logrus.TextFormatter)
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
* `logrus_logstash.LogstashFormatter`. Logs fields as Logstash Events (http://logstash.net).

    ```go
      logrus.SetFormatter(&logrus_logstash.LogstashFormatter{Type: “application_name"})
    ```

Third party logging formatters:

* [`zalgo`](https://github.com/aybabtme/logzalgo): invoking the P͉̫o̳̼̊w̖͈̰͎e̬͔̭͂r͚̼̹̲ ̫͓͉̳͈ō̠͕͖̚f̝͍̠ ͕̲̞͖͑Z̖̫̤̫ͪa͉̬͈̗l͖͎g̳̥o̰̥̅!̣͔̲̻͊̄ ̙̘̦̹̦.

You can define your formatter by implementing the `Formatter` interface,
requiring a `Format` method. `Format` takes an `*Entry`. `entry.Data` is a
`Fields` type (`map[string]interface{}`) with all your fields as well as the
default ones (see Entries section above):

```go
type MyJSONFormatter struct {
}

log.SetFormatter(new(MyJSONFormatter))

func (f *JSONFormatter) Format(entry *Entry) ([]byte, error) {
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

Logrus can be transormed into an `io.Writer`. That writer is the end of an `io.Pipe` and it is your responsibility to close it.

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


[godoc]: https://godoc.org/github.com/Sirupsen/logrus
ini [![Build Status](https://drone.io/github.com/go-ini/ini/status.png)](https://drone.io/github.com/go-ini/ini/latest) [![](http://gocover.io/_badge/github.com/go-ini/ini)](http://gocover.io/github.com/go-ini/ini)
===

![](https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

[简体中文](README_ZH.md)

## Feature

- Load multiple data sources(`[]byte` or file) with overwrites.
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

To use a tagged revision:

	go get gopkg.in/ini.v1

To use with latest changes:

	go get github.com/go-ini/ini

### Testing

If you want to test on your machine, please apply `-t` flag:

	go get -t gopkg.in/ini.v1

## Getting Started

### Loading from data sources

A **Data Source** is either raw data in type `[]byte` or a file name with type `string` and you can load **as many as** data sources you want. Passing other types will simply return an error.

```go
cfg, err := ini.Load([]byte("raw data"), "filename")
```

Or start with an empty object:

```go
cfg := ini.Empty()
```

When you cannot decide how many data sources to load at the beginning, you still able to **Append()** them later.

```go
err := cfg.Append("other file", []byte("other raw data"))
```

### Working with sections

To get a section, you would need to:

```go
section, err := cfg.GetSection("section name")
```

For a shortcut for default section, just give an empty string as name:

```go
section, err := cfg.GetSection("")
```

When you're pretty sure the section exists, following code could make your life easier:

```go
section := cfg.Section("")
```

What happens when the section somehow does not exist? Don't panic, it automatically creates and returns a new section to you.

To create a new section:

```go
err := cfg.NewSection("new section")
```

To get a list of sections or section names:

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### Working with keys

To get a key under a section:

```go
key, err := cfg.Section("").GetKey("key name")
```

Same rule applies to key operations:

```go
key := cfg.Section("").Key("key name")
```

To check if a key exists:

```go
yes := cfg.Section("").HasKey("key name")
```

To create a new key:

```go
err := cfg.Section("").NewKey("name", "value")
```

To get a list of keys or key names:

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

To get a clone hash of keys and corresponding values:

```go
hash := cfg.GetSection("").KeysHash()
```

### Working with values

To get a string value:

```go
val := cfg.Section("").Key("key name").String()
```

To validate key value on the fly:

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

If you do not want any auto-transformation (such as recursive read) for the values, you can get raw value directly (this way you get much better performance):

```go
val := cfg.Section("").Key("key name").Value()
```

To check if raw value exists:

```go
yes := cfg.Section("").HasValue("test value")
```

To get value with types:

```go
// For boolean values:
// true when value is: 1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false when value is: 0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// Methods start with Must also accept one argument for default value
// when key not found or fail to parse value to given type.
// Except method MustString, which you have to pass a default value.

v = cfg.Section("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

What if my value is three-line long?

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

Not a problem!

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

That's cool, how about continuation lines?

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

Piece of cake!

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

Note that single quotes around values will be stripped:

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

That's all? Hmm, no.

#### Helper methods of working with values

To get value with given candidates:

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

Default value will be presented if value of key is not in candidates you given, and default value does not need be one of candidates.

To validate value in a given range:

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

To auto-split value into slice:

```go
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

### Save your configuration

Finally, it's time to save your configuration to somewhere.

A typical way to save configuration is writing it to a file:

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

Another way to save is writing to a `io.Writer` interface:

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

## Advanced Usage

### Recursive Values

For all value of keys, there is a special syntax `%(<name>)s`, where `<name>` is the key name in same section or default section, and `%(<name>)s` will be replaced by corresponding value(empty string if key not found). You can use this syntax at most 99 level of recursions.

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### Parent-child Sections

You can use `.` in section name to indicate parent-child relationship between two or more sections. If the key not found in the child section, library will try again on its parent section until there is no parent section.

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

### Auto-increment Key Names

If key name is `-` in data source, then it would be seen as special syntax for auto-increment key name start from 1, and every section is independent on counter.

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### Map To Struct

Want more objective way to play with INI? Cool.

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// Things can be simpler.
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// Just map a section? Fine.
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

Can I have default value for field? Absolutely.

Assign it before you map to struct. It will keep the value as it is if the key is not presented or got wrong type.

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

It's really cool, but what's the point if you can't give me my file back from struct?

### Reflect From Struct

Why not?

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string
	None   []int
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

So, what do I get?

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
Places = HangZhou,Boston
None =
```

#### Name Mapper

To save your time and make your code cleaner, this library supports [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) between struct field and actual section and key name.

There are 2 built-in name mappers:

- `AllCapsUnderscore`: it converts to format `ALL_CAPS_UNDERSCORE` then match section or key.
- `TitleUnderscore`: it converts to format `title_underscore` then match section or key.

To use them:

```go
type Info struct {
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

Same rules of name mapper apply to `ini.ReflectFromWithMapper` function.

#### Other Notes On Map/Reflect

Any embedded struct is treated as a section by default, and there is no automatic parent-child relations in map/reflect feature:

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

What if, yes, I'm paranoid, I want embedded struct to be in the same section. Well, all roads lead to Rome.

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## Getting Help

- [API Documentation](https://gowalker.org/gopkg.in/ini.v1)
- [File An Issue](https://github.com/go-ini/ini/issues/new)

## FAQs

### What does `BlockMode` field do?

By default, library lets you read and write values so we need a locker to make sure your data is safe. But in cases that you are very sure about only reading data through the library, you can set `cfg.BlockMode = false` to speed up read operations about **50-70%** faster.

### Why another INI library?

Many people are using my another INI library [goconfig](https://github.com/Unknwon/goconfig), so the reason for this one is I would like to make more Go style code. Also when you set `cfg.BlockMode = false`, this one is about **10-30%** faster.

To make those changes I have to confirm API broken, so it's safer to keep it in another place and start using `gopkg.in` to version my package at this time.(PS: shorter import path)

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.
本包提供了 Go 语言中读写 INI 文件的功能。

## 功能特性

- 支持覆盖加载多个数据源（`[]byte` 或文件）
- 支持递归读取键值
- 支持读取父子分区
- 支持读取自增键名
- 支持读取多行的键值
- 支持大量辅助方法
- 支持在读取时直接转换为 Go 语言类型
- 支持读取和 **写入** 分区和键的注释
- 轻松操作分区、键值和注释
- 在保存文件时分区和键值会保持原有的顺序

## 下载安装

使用一个特定版本：

    go get gopkg.in/ini.v1

使用最新版：

	go get github.com/go-ini/ini

### 测试安装

如果您想要在自己的机器上运行测试，请使用 `-t` 标记：

	go get -t gopkg.in/ini.v1

## 开始使用

### 从数据源加载

一个 **数据源** 可以是 `[]byte` 类型的原始数据，或 `string` 类型的文件路径。您可以加载 **任意多个** 数据源。如果您传递其它类型的数据源，则会直接返回错误。

```go
cfg, err := ini.Load([]byte("raw data"), "filename")
```

或者从一个空白的文件开始：

```go
cfg := ini.Empty()
```

当您在一开始无法决定需要加载哪些数据源时，仍可以使用 **Append()** 在需要的时候加载它们。

```go
err := cfg.Append("other file", []byte("other raw data"))
```

### 操作分区（Section）

获取指定分区：

```go
section, err := cfg.GetSection("section name")
```

如果您想要获取默认分区，则可以用空字符串代替分区名：

```go
section, err := cfg.GetSection("")
```

当您非常确定某个分区是存在的，可以使用以下简便方法：

```go
section := cfg.Section("")
```

如果不小心判断错了，要获取的分区其实是不存在的，那会发生什么呢？没事的，它会自动创建并返回一个对应的分区对象给您。

创建一个分区：

```go
err := cfg.NewSection("new section")
```

获取所有分区对象或名称：

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### 操作键（Key）

获取某个分区下的键：

```go
key, err := cfg.Section("").GetKey("key name")
```

和分区一样，您也可以直接获取键而忽略错误处理：

```go
key := cfg.Section("").Key("key name")
```

判断某个键是否存在：

```go
yes := cfg.Section("").HasKey("key name")
```

创建一个新的键：

```go
err := cfg.Section("").NewKey("name", "value")
```

获取分区下的所有键或键名：

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

获取分区下的所有键值对的克隆：

```go
hash := cfg.GetSection("").KeysHash()
```

### 操作键值（Value）

获取一个类型为字符串（string）的值：

```go
val := cfg.Section("").Key("key name").String()
```

获取值的同时通过自定义函数进行处理验证：

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

如果您不需要任何对值的自动转变功能（例如递归读取），可以直接获取原值（这种方式性能最佳）：

```go
val := cfg.Section("").Key("key name").Value()
```

判断某个原值是否存在：

```go
yes := cfg.Section("").HasValue("test value")
```

获取其它类型的值：

```go
// 布尔值的规则：
// true 当值为：1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false 当值为：0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// 由 Must 开头的方法名允许接收一个相同类型的参数来作为默认值，
// 当键不存在或者转换失败时，则会直接返回该默认值。
// 但是，MustString 方法必须传递一个默认值。

v = cfg.Seciont("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

如果我的值有好多行怎么办？

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

嗯哼？小 case！

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

赞爆了！那要是我属于一行的内容写不下想要写到第二行怎么办？

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

简直是小菜一碟！

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

需要注意的是，值两侧的单引号会被自动剔除：

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

这就是全部了？哈哈，当然不是。

#### 操作键值的辅助方法

获取键值时设定候选值：

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

如果获取到的值不是候选值的任意一个，则会返回默认值，而默认值不需要是候选值中的一员。

验证获取的值是否在指定范围内：

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

自动分割键值为切片（slice）：

```go
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

### 保存配置

终于到了这个时刻，是时候保存一下配置了。

比较原始的做法是输出配置到某个文件：

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

另一个比较高级的做法是写入到任何实现 `io.Writer` 接口的对象中：

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

### 高级用法

#### 递归读取键值

在获取所有键值的过程中，特殊语法 `%(<name>)s` 会被应用，其中 `<name>` 可以是相同分区或者默认分区下的键名。字符串 `%(<name>)s` 会被相应的键值所替代，如果指定的键不存在，则会用空字符串替代。您可以最多使用 99 层的递归嵌套。

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

#### 读取父子分区

您可以在分区名称中使用 `.` 来表示两个或多个分区之间的父子关系。如果某个键在子分区中不存在，则会去它的父分区中再次寻找，直到没有父分区为止。

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### 读取自增键名

如果数据源中的键名为 `-`，则认为该键使用了自增键名的特殊语法。计数器从 1 开始，并且分区之间是相互独立的。

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### 映射到结构

想要使用更加面向对象的方式玩转 INI 吗？好主意。

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// 一切竟可以如此的简单。
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// 嗯哼？只需要映射一个分区吗？
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

结构的字段怎么设置默认值呢？很简单，只要在映射之前对指定字段进行赋值就可以了。如果键未找到或者类型错误，该值不会发生改变。

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

这样玩 INI 真的好酷啊！然而，如果不能还给我原来的配置文件，有什么卵用？

### 从结构反射

可是，我有说不能吗？

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string
	None   []int
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

瞧瞧，奇迹发生了。

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
Places = HangZhou,Boston
None =
```

#### 名称映射器（Name Mapper）

为了节省您的时间并简化代码，本库支持类型为 [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) 的名称映射器，该映射器负责结构字段名与分区名和键名之间的映射。

目前有 2 款内置的映射器：

- `AllCapsUnderscore`：该映射器将字段名转换至格式 `ALL_CAPS_UNDERSCORE` 后再去匹配分区名和键名。
- `TitleUnderscore`：该映射器将字段名转换至格式 `title_underscore` 后再去匹配分区名和键名。

使用方法：

```go
type Info struct{
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

使用函数 `ini.ReflectFromWithMapper` 时也可应用相同的规则。

#### 映射/反射的其它说明

任何嵌入的结构都会被默认认作一个不同的分区，并且不会自动产生所谓的父子分区关联：

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

很好，但是，我就是要嵌入结构也在同一个分区。好吧，你爹是李刚！

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## 获取帮助

- [API 文档](https://gowalker.org/gopkg.in/ini.v1)
- [创建工单](https://github.com/go-ini/ini/issues/new)

## 常见问题

### 字段 `BlockMode` 是什么？

默认情况下，本库会在您进行读写操作时采用锁机制来确保数据时间。但在某些情况下，您非常确定只进行读操作。此时，您可以通过设置 `cfg.BlockMode = false` 来将读操作提升大约 **50-70%** 的性能。

### 为什么要写另一个 INI 解析库？

许多人都在使用我的 [goconfig](https://github.com/Unknwon/goconfig) 来完成对 INI 文件的操作，但我希望使用更加 Go 风格的代码。并且当您设置 `cfg.BlockMode = false` 时，会有大约 **10-30%** 的性能提升。

为了做出这些改变，我必须对 API 进行破坏，所以新开一个仓库是最安全的做法。除此之外，本库直接使用 `gopkg.in` 来进行版本化发布。（其实真相是导入路径更短了）
# crc32
CRC32 hash with x64 optimizations

This package is a drop-in replacement for the standard library `hash/crc32` package, that features SSE 4.2 optimizations on x64 platforms, for a 10x speedup.

[![Build Status](https://travis-ci.org/klauspost/crc32.svg?branch=master)](https://travis-ci.org/klauspost/crc32)

# usage

Install using `go get github.com/klauspost/crc32`. This library is based on Go 1.5 code and requires Go 1.3 or newer.

Replace `import "hash/crc32"` with `import "github.com/klauspost/crc32"` and you are good to go.

# changes

* Dec 4, 2015: Uses the "slice-by-8" trick more extensively, which gives a 1.5 to 2.5x speedup if assembler is unavailable.


# performance

For IEEE tables (the most common), there is approximately a factor 10 speedup with "CLMUL" (Carryless multiplication) instruction:
```
benchmark            old ns/op     new ns/op     delta
BenchmarkCrc32KB     99955         10258         -89.74%

benchmark            old MB/s     new MB/s     speedup
BenchmarkCrc32KB     327.83       3194.20      9.74x
```

For other tables and "CLMUL"  capable machines the performance is the same as the standard library.

Here are some detailed benchmarks, comparing to go 1.5 standard library with and without assembler enabled.

```
Std:   Standard Go 1.5 library
Crc:   Indicates IEEE type CRC.
40B:   Size of each slice encoded.
NoAsm: Assembler was disabled (ie. not an AMD64 or SSE 4.2+ capable machine).
Castagnoli: Castagnoli CRC type.

BenchmarkStdCrc40B-4            10000000               158 ns/op         252.88 MB/s
BenchmarkCrc40BNoAsm-4          20000000               105 ns/op         377.38 MB/s (slice8)
BenchmarkCrc40B-4               20000000               105 ns/op         378.77 MB/s (slice8)

BenchmarkStdCrc1KB-4              500000              3604 ns/op         284.10 MB/s
BenchmarkCrc1KBNoAsm-4           1000000              1463 ns/op         699.79 MB/s (slice8)
BenchmarkCrc1KB-4                3000000               396 ns/op        2583.69 MB/s (asm)

BenchmarkStdCrc8KB-4              200000             11417 ns/op         717.48 MB/s (slice8)
BenchmarkCrc8KBNoAsm-4            200000             11317 ns/op         723.85 MB/s (slice8)
BenchmarkCrc8KB-4                 500000              2919 ns/op        2805.73 MB/s (asm)

BenchmarkStdCrc32KB-4              30000             45749 ns/op         716.24 MB/s (slice8)
BenchmarkCrc32KBNoAsm-4            30000             45109 ns/op         726.42 MB/s (slice8)
BenchmarkCrc32KB-4                100000             11497 ns/op        2850.09 MB/s (asm)

BenchmarkStdNoAsmCastagnol40B-4 10000000               161 ns/op         246.94 MB/s
BenchmarkStdCastagnoli40B-4     50000000              28.4 ns/op        1410.69 MB/s (asm)
BenchmarkCastagnoli40BNoAsm-4   20000000               100 ns/op         398.01 MB/s (slice8)
BenchmarkCastagnoli40B-4        50000000              28.2 ns/op        1419.54 MB/s (asm)

BenchmarkStdNoAsmCastagnoli1KB-4  500000              3622 ns/op        282.67 MB/s
BenchmarkStdCastagnoli1KB-4     10000000               144 ns/op        7099.78 MB/s (asm)
BenchmarkCastagnoli1KBNoAsm-4    1000000              1475 ns/op         694.14 MB/s (slice8)
BenchmarkCastagnoli1KB-4        10000000               146 ns/op        6993.35 MB/s (asm)

BenchmarkStdNoAsmCastagnoli8KB-4  50000              28781 ns/op         284.63 MB/s
BenchmarkStdCastagnoli8KB-4      1000000              1029 ns/op        7957.89 MB/s (asm)
BenchmarkCastagnoli8KBNoAsm-4     200000             11410 ns/op         717.94 MB/s (slice8)
BenchmarkCastagnoli8KB-4         1000000              1000 ns/op        8188.71 MB/s (asm)

BenchmarkStdNoAsmCastagnoli32KB-4  10000            115426 ns/op         283.89 MB/s
BenchmarkStdCastagnoli32KB-4      300000              4065 ns/op        8059.13 MB/s (asm)
BenchmarkCastagnoli32KBNoAsm-4     30000             45171 ns/op         725.41 MB/s (slice8)
BenchmarkCastagnoli32KB-4         500000              4077 ns/op        8035.89 MB/s (asm)
```

The IEEE assembler optimizations has been submitted and will be part of the Go 1.6 standard library.

However, the improved use of slice-by-8 has not, but will probably be submitted for Go 1.7.

# license

Standard Go license. Changes are Copyright (c) 2015 Klaus Post under same conditions.
# cpuid
Package cpuid provides information about the CPU running the current program.

CPU features are detected on startup, and kept for fast access through the life of the application.
Currently x86 / x64 (AMD64) is supported, and no external C (cgo) code is used, which should make the library very easy to use.

You can access the CPU information by accessing the shared CPU variable of the cpuid library.

Package home: https://github.com/klauspost/cpuid

[![GoDoc][1]][2] [![Build Status][3]][4]

[1]: https://godoc.org/github.com/klauspost/cpuid?status.svg
[2]: https://godoc.org/github.com/klauspost/cpuid
[3]: https://travis-ci.org/klauspost/cpuid.svg
[4]: https://travis-ci.org/klauspost/cpuid

# features
## CPU Instructions
*  **CMOV** (i686 CMOV)
*  **NX** (NX (No-Execute) bit)
*  **AMD3DNOW** (AMD 3DNOW)
*  **AMD3DNOWEXT** (AMD 3DNowExt)
*  **MMX** (standard MMX)
*  **MMXEXT** (SSE integer functions or AMD MMX ext)
*  **SSE** (SSE functions)
*  **SSE2** (P4 SSE functions)
*  **SSE3** (Prescott SSE3 functions)
*  **SSSE3** (Conroe SSSE3 functions)
*  **SSE4** (Penryn SSE4.1 functions)
*  **SSE4A** (AMD Barcelona microarchitecture SSE4a instructions)
*  **SSE42** (Nehalem SSE4.2 functions)
*  **AVX** (AVX functions)
*  **AVX2** (AVX2 functions)
*  **FMA3** (Intel FMA 3)
*  **FMA4** (Bulldozer FMA4 functions)
*  **XOP** (Bulldozer XOP functions)
*  **F16C** (Half-precision floating-point conversion)
*  **BMI1** (Bit Manipulation Instruction Set 1)
*  **BMI2** (Bit Manipulation Instruction Set 2)
*  **TBM** (AMD Trailing Bit Manipulation)
*  **LZCNT** (LZCNT instruction)
*  **POPCNT** (POPCNT instruction)
*  **AESNI** (Advanced Encryption Standard New Instructions)
*  **CLMUL** (Carry-less Multiplication)
*  **HTT** (Hyperthreading (enabled))
*  **HLE** (Hardware Lock Elision)
*  **RTM** (Restricted Transactional Memory)
*  **RDRAND** (RDRAND instruction is available)
*  **RDSEED** (RDSEED instruction is available)
*  **ADX** (Intel ADX (Multi-Precision Add-Carry Instruction Extensions))
*  **SHA** (Intel SHA Extensions)
*  **AVX512F** (AVX-512 Foundation)
*  **AVX512DQ** (AVX-512 Doubleword and Quadword Instructions)
*  **AVX512IFMA** (AVX-512 Integer Fused Multiply-Add Instructions)
*  **AVX512PF** (AVX-512 Prefetch Instructions)
*  **AVX512ER** (AVX-512 Exponential and Reciprocal Instructions)
*  **AVX512CD** (AVX-512 Conflict Detection Instructions)
*  **AVX512BW** (AVX-512 Byte and Word Instructions)
*  **AVX512VL** (AVX-512 Vector Length Extensions)
*  **AVX512VBMI** (AVX-512 Vector Bit Manipulation Instructions)
*  **MPX** (Intel MPX (Memory Protection Extensions))
*  **ERMS** (Enhanced REP MOVSB/STOSB)
*  **RDTSCP** (RDTSCP Instruction)
*  **CX16** (CMPXCHG16B Instruction)
*  **SGX** (Software Guard Extensions, with activation details)

## Performance
*  **RDTSCP()** Returns current cycle count. Can be used for benchmarking.
*  **SSE2SLOW** (SSE2 is supported, but usually not faster)
*  **SSE3SLOW** (SSE3 is supported, but usually not faster)
*  **ATOM** (Atom processor, some SSSE3 instructions are slower)
*  **Cache line** (Probable size of a cache line).
*  **L1, L2, L3 Cache size** on newer Intel/AMD CPUs.

## Cpu Vendor/VM
* **Intel**
* **AMD**
* **VIA**
* **Transmeta**
* **NSC**
* **KVM**  (Kernel-based Virtual Machine)
* **MSVM** (Microsoft Hyper-V or Windows Virtual PC)
* **VMware**
* **XenHVM**

# installing

```go get github.com/klauspost/cpuid```

# example

```Go
package main

import (
	"fmt"
	"github.com/klauspost/cpuid"
)

func main() {
	// Print basic CPU information:
	fmt.Println("Name:", cpuid.CPU.BrandName)
	fmt.Println("PhysicalCores:", cpuid.CPU.PhysicalCores)
	fmt.Println("ThreadsPerCore:", cpuid.CPU.ThreadsPerCore)
	fmt.Println("LogicalCores:", cpuid.CPU.LogicalCores)
	fmt.Println("Family", cpuid.CPU.Family, "Model:", cpuid.CPU.Model)
	fmt.Println("Features:", cpuid.CPU.Features)
	fmt.Println("Cacheline bytes:", cpuid.CPU.CacheLine)
	fmt.Println("L1 Data Cache:", cpuid.CPU.Cache.L1D, "bytes")
	fmt.Println("L1 Instruction Cache:", cpuid.CPU.Cache.L1D, "bytes")
	fmt.Println("L2 Cache:", cpuid.CPU.Cache.L2, "bytes")
	fmt.Println("L3 Cache:", cpuid.CPU.Cache.L3, "bytes")

	// Test if we have a specific feature:
	if cpuid.CPU.SSE() {
		fmt.Println("We have Streaming SIMD Extensions")
	}
}
```

Sample output:
```
>go run main.go
Name: Intel(R) Core(TM) i5-2540M CPU @ 2.60GHz
PhysicalCores: 2
ThreadsPerCore: 2
LogicalCores: 4
Family 6 Model: 42
Features: CMOV,MMX,MMXEXT,SSE,SSE2,SSE3,SSSE3,SSE4.1,SSE4.2,AVX,AESNI,CLMUL
Cacheline bytes: 64
We have Streaming SIMD Extensions
```

# private package

In the "private" folder you can find an autogenerated version of the library you can include in your own packages.

For this purpose all exports are removed, and functions and constants are lowercased.

This is not a recommended way of using the library, but provided for convenience, if it is difficult for you to use external packages.

# license

This code is published under an MIT license. See LICENSE file for more information.
