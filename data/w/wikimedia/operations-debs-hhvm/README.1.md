## Proxygen: Facebook's C++ HTTP Libraries

This project comprises the core C++ HTTP abstractions used at
Facebook. Internally, it is used as the basis for building many HTTP
servers, proxies, and clients. This release focuses on the common HTTP
abstractions and our simple HTTPServer framework. Future releases will
provide simple client APIs as well. The framework supports HTTP/1.1,
SPDY/3, and SPDY/3.1. HTTP/2 support is in progress. The goal is to
provide a simple, performant, and modern C++ HTTP library.

We have a Google group for general discussions at https://groups.google.com/d/forum/facebook-proxygen.

The [original blog post](https://code.facebook.com/posts/1503205539947302)
also has more background on the project.

Build Status: [![Build Status](https://travis-ci.org/facebook/proxygen.svg?branch=master)](https://travis-ci.org/facebook/proxygen)

### Installing

Note that currently this project has only been tested on Ubuntu 14.04,
although it likely works on many other platforms. Support for Mac OSX is
incomplete.

You will need at least 2 GiB of memory to compile proxygen and its
dependencies.

##### Easy Install

Just run `./deps.sh` from the `proxygen/` directory to get and build all
the dependencies and proxygen. It will also run all the tests. Then run
`./reinstall.sh` to install it. You can run `./deps.sh && ./reinstall.sh`
whenever to rebase the dependencies, and then rebuild and reinstall proxygen.

A note on compatibility: this project relies on system installed fbthrift
and folly. If you rebase proxygen and `make` starts to fail, you likely
need to update to the latest version of fbthrift and folly. Running
`./deps.sh && ./reinstall.sh` will do this for you. We are still working
on a solution to manage depencies more predictably.

##### Other Platforms

If you are running on another platform, you may need to install several
packages first. Proxygen, fbthrift, and folly are all autotools based projects.

### Introduction

Directory structure and contents:

| Directory                  | Purpose                                                                       |
|----------------------------|-------------------------------------------------------------------------------|
| `proxygen/external/`       | Contains non-installed 3rd-party code proxygen depends on.                    |
| `proxygen/lib/`            | Core networking abstractions.                                                 |
| `proxygen/lib/http/`       | HTTP specific code.                                                           |
| `proxygen/lib/services/`   | Connection management and server code.                                        |
| `proxygen/lib/ssl/`        | TLS abstractions and OpenSSL wrappers.                                        |
| `proxygen/lib/utils/`      | Miscellaneous helper code.                                                    |
| `proxygen/httpserver/`     | Contains code wrapping `proxygen/lib/` for building simple C++ http servers. We recommend building on top of these APIs. |

### Architecture

The central abstractions to understand in `proxygen/lib` are the session, codec,
transaction, and handler. These are the lowest level abstractions, and we
don't generally recommend building off of these directly.

When bytes are read off the wire, the `HTTPCodec` stored inside
`HTTPSession` parses these into higher level objects and associates with
it a transaction identifier. The codec then calls into `HTTPSession` which
is responsible for maintaining the mapping between transaction identifier
and `HTTPTransaction` objects. Each HTTP request/response pair has a
separate `HTTPTransaction` object. Finally, `HTTPTransaction` forwards the
call to a handler object which implements `HTTPTransaction::Handler`. The
handler is responsible for implementing business logic for the request or
response.

The handler then calls back into the transaction to generate egress
(whether the egress is a request or response). The call flows from the
transaction back to the session, which uses the codec to convert the
higher level semantics of the particular call into the appropriate bytes
to send on the wire.

The same handler and transaction interfaces are used to both create requests
and handle responses. The API is generic enough to allow
both. `HTTPSession` is specialized slightly differently depending on
whether you are using the connection to issue or respond to HTTP
requests.

![Core Proxygen Architecture](CoreProxygenArchitecture.png)

Moving into higher levels of abstraction, `proxygen/httpserver` has a
simpler set of APIs and is the recommended way to interface with proxygen
when acting as a server if you don't need the full control of the lower
level abstractions.

The basic components here are `HTTPServer`, `RequestHandlerFactory`, and
`RequestHandler`. An `HTTPServer` takes some configuration and is given a
`RequestHandlerFactory`. Once the server is started, the installed
`RequestHandlerFactory` spawns a `RequestHandler` for each HTTP
request. `RequestHandler` is a simple interface users of the library
implement. Subclasses of `RequestHandler` should use the inherited
protected member `ResponseHandler* downstream_` to send the response.

### Using it

Proxygen is a library. After installing it, you can build your own C++
server. Try `cd`ing to the directory containing the echo server at
`proxygen/httpserver/samples/echo/`. You can then build it with this one
liner:

<code>
g++ -std=c++11 -o my_echo EchoServer.cpp EchoHandler.cpp -lproxygenhttpserver -lfolly -lglog -lgflags -pthread
</code>

After running `./my_echo`, we can verify it works using curl in a different terminal:
```shell
$ curl -v http://localhost:11000/
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 11000 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:11000
> Accept: */*
>
< HTTP/1.1 200 OK
< Request-Number: 1
< Date: Thu, 30 Oct 2014 17:07:36 GMT
< Connection: keep-alive
< Content-Length: 0
<
* Connection #0 to host localhost left intact
```

### Documentation

We use Doxygen for Proxygen's internal documentation. You can generate a
copy of these docs by running `doxygen Doxyfile` from the project
root. You'll want to look at `html/namespaceproxygen.html` to start. This
will also generate folly and thrift documentation.

### Contributing
Contribututions to Proxygen are more than welcome. [Read the guidelines in CONTRIBUTING.md](CONTRIBUTING.md).
Make sure you've [signed the CLA](https://code.facebook.com/cla) before sending in a pull request.

### Whitehat

Facebook has a [bounty program](https://www.facebook.com/whitehat/) for
the safe disclosure of security bugs. If you find a vulnerability, please
go through the process outlined on that page and do not file a public issue.
This directory contains experimental codecs that have not been run in 
production.  

Use with due caution, and please report bugs
This directory contains experimental codecs that have not been run in 
production.  

Use with due caution, and please report bugs
HTTP Parser
===========

This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP
applications. It does not make any syscalls nor allocations, it does not
buffer data, it can be interrupted at anytime. Depending on your
architecture, it only requires about 40 bytes of data per message
stream (in a web server that is per connection).

Features:

  * No dependencies
  * Handles persistent streams (keep-alive).
  * Decodes chunked encoding.
  * Upgrade support
  * Defends against buffer overflow attacks.

The parser extracts the following information from HTTP messages:

  * Header fields and values
  * Content-Length
  * Request method
  * Response status code
  * Transfer-Encoding
  * HTTP version
  * Request URL
  * Message body


Usage
-----

One `http_parser` object is used per TCP connection. Initialize the struct
using `http_parser_init()` and set the callbacks. That might look something
like this for a request parser:

    http_parser_settings settings;
    settings.on_path = my_path_callback;
    settings.on_header_field = my_header_field_callback;
    /* ... */

    http_parser *parser = malloc(sizeof(http_parser));
    http_parser_init(parser, HTTP_REQUEST);
    parser->data = my_socket;

When data is received on the socket execute the parser and check for errors.

    size_t len = 80*1024, nparsed;
    char buf[len];
    ssize_t recved;

    recved = recv(fd, buf, len, 0);

    if (recved < 0) {
      /* Handle error. */
    }

    /* Start up / continue the parser.
     * Note we pass recved==0 to signal that EOF has been recieved.
     */
    nparsed = http_parser_execute(parser, &settings, buf, recved);

    if (parser->upgrade) {
      /* handle new protocol */
    } else if (nparsed != recved) {
      /* Handle error. Usually just close the connection. */
    }

HTTP needs to know where the end of the stream is. For example, sometimes
servers send responses without Content-Length and expect the client to
consume input (for the body) until EOF. To tell http_parser about EOF, give
`0` as the forth parameter to `http_parser_execute()`. Callbacks and errors
can still be encountered during an EOF, so one must still be prepared
to receive them.

Scalar valued message information such as `status_code`, `method`, and the
HTTP version are stored in the parser structure. This data is only
temporally stored in `http_parser` and gets reset on each new message. If
this information is needed later, copy it out of the structure during the
`headers_complete` callback.

The parser decodes the transfer-encoding for both requests and responses
transparently. That is, a chunked encoding is decoded before being sent to
the on_body callback.


The Special Problem of Upgrade
------------------------------

HTTP supports upgrading the connection to a different protocol. An
increasingly common example of this is the Web Socket protocol which sends
a request like

        GET /demo HTTP/1.1
        Upgrade: WebSocket
        Connection: Upgrade
        Host: example.com
        Origin: http://example.com
        WebSocket-Protocol: sample

followed by non-HTTP data.

(See http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-75 for more
information the Web Socket protocol.)

To support this, the parser will treat this as a normal HTTP message without a
body. Issuing both on_headers_complete and on_message_complete callbacks. However
http_parser_execute() will stop parsing at the end of the headers and return.

The user is expected to check if `parser->upgrade` has been set to 1 after
`http_parser_execute()` returns. Non-HTTP data begins at the buffer supplied
offset by the return value of `http_parser_execute()`.


Callbacks
---------

During the `http_parser_execute()` call, the callbacks set in
`http_parser_settings` will be executed. The parser maintains state and
never looks behind, so buffering the data is not necessary. If you need to
save certain data for later usage, you can do that from the callbacks.

There are two types of callbacks:

* notification `typedef int (*http_cb) (http_parser*);`
    Callbacks: on_message_begin, on_headers_complete, on_message_complete.
* data `typedef int (*http_data_cb) (http_parser*, const char *at, size_t length);`
    Callbacks: (requests only) on_uri,
               (common) on_header_field, on_header_value, on_body;

Callbacks must return 0 on success. Returning a non-zero value indicates
error to the parser, making it exit immediately.

In case you parse HTTP message in chunks (i.e. `read()` request line
from socket, parse, read half headers, parse, etc) your data callbacks
may be called more than once. Http-parser guarantees that data pointer is only
valid for the lifetime of callback. You can also `read()` into a heap allocated
buffer to avoid copying memory around if this fits your application.

Reading headers may be a tricky task if you read/parse headers partially.
Basically, you need to remember whether last header callback was field or value
and apply following logic:

    (on_header_field and on_header_value shortened to on_h_*)
     ------------------------ ------------ --------------------------------------------
    | State (prev. callback) | Callback   | Description/action                         |
     ------------------------ ------------ --------------------------------------------
    | nothing (first call)   | on_h_field | Allocate new buffer and copy callback data |
    |                        |            | into it                                    |
     ------------------------ ------------ --------------------------------------------
    | value                  | on_h_field | New header started.                        |
    |                        |            | Copy current name,value buffers to headers |
    |                        |            | list and allocate new buffer for new name  |
     ------------------------ ------------ --------------------------------------------
    | field                  | on_h_field | Previous name continues. Reallocate name   |
    |                        |            | buffer and append callback data to it      |
     ------------------------ ------------ --------------------------------------------
    | field                  | on_h_value | Value for current header started. Allocate |
    |                        |            | new buffer and copy callback data to it    |
     ------------------------ ------------ --------------------------------------------
    | value                  | on_h_value | Value continues. Reallocate value buffer   |
    |                        |            | and append callback data to it             |
     ------------------------ ------------ --------------------------------------------


See examples of reading in headers:

* [partial example](http://gist.github.com/155877) in C
* [from http-parser tests](http://github.com/ry/http-parser/blob/37a0ff8928fb0d83cec0d0d8909c5a4abcd221af/test.c#L403) in C
* [from Node library](http://github.com/ry/node/blob/842eaf446d2fdcb33b296c67c911c32a0dabc747/src/http.js#L284) in Javascript
