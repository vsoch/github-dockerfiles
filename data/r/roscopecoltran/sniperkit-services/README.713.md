scifgif
=======

[![Circle CI](https://circleci.com/gh/blacktop/scifgif.png?style=shield)](https://circleci.com/gh/blacktop/scifgif) [![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org) [![Docker Stars](https://img.shields.io/docker/stars/blacktop/scifgif.svg)](https://store.docker.com/community/images/blacktop/scifgif) [![Docker Pulls](https://img.shields.io/docker/pulls/blacktop/scifgif.svg)](https://store.docker.com/community/images/blacktop/scifgif) [![Docker Image](https://img.shields.io/badge/docker%20image-2GB-blue.svg)](https://store.docker.com/community/images/blacktop/scifgif)

> Humorous image microservice for isolated networks - `xkcd|giphy` + **keyword/phrase** search API

---

### Dependencies

-	[alpine:3.6](https://hub.docker.com/_/alpine/)
-	[blacktop/elasticsearch:5.5](https://hub.docker.com/r/blacktop/elasticsearch/)

### Image Tags

```bash
REPOSITORY           TAG                 SIZE
blacktop/scifgif     latest              2GB
blacktop/scifgif     0.2.0               2GB
blacktop/scifgif     0.1.0               2GB
```

> **NOTE:** the reason the docker image is so large is that it contains ~2000 animated gifs *(1500 reactions, 250 futurama and 250 star wars)*

Getting Started
---------------

```bash
$ docker run --init -d --name scifgif -p 3993:3993 blacktop/scifgif --host localhost
```

Documentation
-------------

-	[API Docs](http://docs.scifgif.apiary.io)
-	[Use with Mattermost](https://github.com/blacktop/scifgif/blob/master/docs/mattermost.md)

![mattermost](https://raw.githubusercontent.com/blacktop/scifgif/master/docs/imgs/mattermost.png)

### TODO

-	[x] Add meta-data DB for keyword text search (elasticsearch)
-	[x] Add docs for creating [Mattermost](https://github.com/mattermost/platform) slash command or integration
-	[ ] Add ability to use expansion packs (use tag to control types of images available)
-	[ ] Add ascii art emojis (table flippers etc)
-	[ ] Add ephemeral slash command help

### Issues

Find a bug? Want more features? Find something missing in the documentation? Let me know! Please don't hesitate to [file an issue](https://github.com/blacktop/scifgif/issues/new)

### License

MIT Copyright (c) 2017 **blacktop**

![giphy](https://raw.githubusercontent.com/blacktop/scifgif/master/docs/PoweredBy_200_Horizontal_Light-Backgrounds_With_Logo.gif)
This repository holds supplemental Go packages for low-level interactions with the operating system.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
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
# Elastic

Elastic is an [Elasticsearch](http://www.elasticsearch.org/) client for the
[Go](http://www.golang.org/) programming language.

[![Build Status](https://travis-ci.org/olivere/elastic.svg?branch=release-branch.v5)](https://travis-ci.org/olivere/elastic)
[![Godoc](http://img.shields.io/badge/godoc-reference-blue.svg?style=flat)](http://godoc.org/gopkg.in/olivere/elastic.v5)
[![license](http://img.shields.io/badge/license-MIT-red.svg?style=flat)](https://raw.githubusercontent.com/olivere/elastic/master/LICENSE)

See the [wiki](https://github.com/olivere/elastic/wiki) for additional information about Elastic.


## Releases

**The release branches (e.g. [`release-branch.v5`](https://github.com/olivere/elastic/tree/release-branch.v5))
are actively being worked on and can break at any time.
If you want to use stable versions of Elastic, please use the packages released via [gopkg.in](https://gopkg.in).**

Here's the version matrix:

Elasticsearch version | Elastic version -| Package URL
----------------------|------------------|------------
5.x                   | 5.0              | [`gopkg.in/olivere/elastic.v5`](https://gopkg.in/olivere/elastic.v5) ([source](https://github.com/olivere/elastic/tree/release-branch.v5) [doc](http://godoc.org/gopkg.in/olivere/elastic.v5))
2.x                   | 3.0              | [`gopkg.in/olivere/elastic.v3`](https://gopkg.in/olivere/elastic.v3) ([source](https://github.com/olivere/elastic/tree/release-branch.v3) [doc](http://godoc.org/gopkg.in/olivere/elastic.v3))
1.x                   | 2.0              | [`gopkg.in/olivere/elastic.v2`](https://gopkg.in/olivere/elastic.v2) ([source](https://github.com/olivere/elastic/tree/release-branch.v2) [doc](http://godoc.org/gopkg.in/olivere/elastic.v2))
0.9-1.3               | 1.0              | [`gopkg.in/olivere/elastic.v1`](https://gopkg.in/olivere/elastic.v1) ([source](https://github.com/olivere/elastic/tree/release-branch.v1) [doc](http://godoc.org/gopkg.in/olivere/elastic.v1))

**Example:**

You have installed Elasticsearch 5.0.0 and want to use Elastic.
As listed above, you should use Elastic 5.0.
So you first install the stable release of Elastic 5.0 from gopkg.in.

```sh
$ go get gopkg.in/olivere/elastic.v5
```

You then import it with this import path:

```go
import elastic "gopkg.in/olivere/elastic.v5"
```

### Elastic 5.0

Elastic 5.0 targets Elasticsearch 5.0.0 and later. Elasticsearch 5.0.0 was
[released on 26th October 2016](https://www.elastic.co/blog/elasticsearch-5-0-0-released).

Notice that there are will be a lot of [breaking changes in Elasticsearch 5.0](https://www.elastic.co/guide/en/elasticsearch/reference/5.0/breaking-changes-5.0.html)
and we used this as an opportunity to [clean up and refactor Elastic](https://github.com/olivere/elastic/blob/release-branch.v5/CHANGELOG-5.0.md)
as we did in the transition from Elastic 2.0 (for Elasticsearch 1.x) to Elastic 3.0 (for Elasticsearch 2.x).

Furthermore, the jump in version numbers will give us a chance to be in sync with the Elastic Stack.

### Elastic 3.0

Elastic 3.0 targets Elasticsearch 2.x and is published via [`gopkg.in/olivere/elastic.v3`](https://gopkg.in/olivere/elastic.v3).

Elastic 3.0 will only get critical bug fixes. You should update to a recent version.

### Elastic 2.0

Elastic 2.0 targets Elasticsearch 1.x and is published via [`gopkg.in/olivere/elastic.v2`](https://gopkg.in/olivere/elastic.v2).

Elastic 2.0 will only get critical bug fixes. You should update to a recent version.

### Elastic 1.0

Elastic 1.0 is deprecated. You should really update Elasticsearch and Elastic
to a recent version.

However, if you cannot update for some reason, don't worry. Version 1.0 is
still available. All you need to do is go-get it and change your import path
as described above.


## Status

We use Elastic in production since 2012. Elastic is stable but the API changes
now and then. We strive for API compatibility.
However, Elasticsearch sometimes introduces [breaking changes](https://www.elastic.co/guide/en/elasticsearch/reference/master/breaking-changes.html)
and we sometimes have to adapt.

Having said that, there have been no big API changes that required you
to rewrite your application big time. More often than not it's renaming APIs
and adding/removing features so that Elastic is in sync with Elasticsearch.

Elastic has been used in production with the following Elasticsearch versions:
0.90, 1.0-1.7, and 2.0-2.4.1. Furthermore, we use [Travis CI](https://travis-ci.org/)
to test Elastic with the most recent versions of Elasticsearch and Go.
See the [.travis.yml](https://github.com/olivere/elastic/blob/master/.travis.yml)
file for the exact matrix and [Travis](https://travis-ci.org/olivere/elastic)
for the results.

Elasticsearch has quite a few features. Most of them are implemented
by Elastic. I add features and APIs as required. It's straightforward
to implement missing pieces. I'm accepting pull requests :-)

Having said that, I hope you find the project useful.


## Getting Started

The first thing you do is to create a [Client](https://github.com/olivere/elastic/blob/master/client.go).
The client connects to Elasticsearch on `http://127.0.0.1:9200` by default.

You typically create one client for your app. Here's a complete example of
creating a client, creating an index, adding a document, executing a search etc.

```go
// Create a context
ctx := context.Background()

// Create a client
client, err := elastic.NewClient()
if err != nil {
    // Handle error
    panic(err)
}

// Create an index
_, err = client.CreateIndex("twitter").Do(ctx)
if err != nil {
    // Handle error
    panic(err)
}

// Add a document to the index
tweet := Tweet{User: "olivere", Message: "Take Five"}
_, err = client.Index().
    Index("twitter").
    Type("tweet").
    Id("1").
    BodyJson(tweet).
    Refresh("true").
    Do(ctx)
if err != nil {
    // Handle error
    panic(err)
}

// Search with a term query
termQuery := elastic.NewTermQuery("user", "olivere")
searchResult, err := client.Search().
    Index("twitter").   // search in index "twitter"
    Query(termQuery).   // specify the query
    Sort("user", true). // sort by "user" field, ascending
    From(0).Size(10).   // take documents 0-9
    Pretty(true).       // pretty print request and response JSON
    Do(ctx)             // execute
if err != nil {
    // Handle error
    panic(err)
}

// searchResult is of type SearchResult and returns hits, suggestions,
// and all kinds of other information from Elasticsearch.
fmt.Printf("Query took %d milliseconds\n", searchResult.TookInMillis)

// Each is a convenience function that iterates over hits in a search result.
// It makes sure you don't need to check for nil values in the response.
// However, it ignores errors in serialization. If you want full control
// over iterating the hits, see below.
var ttyp Tweet
for _, item := range searchResult.Each(reflect.TypeOf(ttyp)) {
    if t, ok := item.(Tweet); ok {
        fmt.Printf("Tweet by %s: %s\n", t.User, t.Message)
    }
}
// TotalHits is another convenience function that works even when something goes wrong.
fmt.Printf("Found a total of %d tweets\n", searchResult.TotalHits())

// Here's how you iterate through results with full control over each step.
if searchResult.Hits.TotalHits > 0 {
    fmt.Printf("Found a total of %d tweets\n", searchResult.Hits.TotalHits)

    // Iterate through results
    for _, hit := range searchResult.Hits.Hits {
        // hit.Index contains the name of the index

        // Deserialize hit.Source into a Tweet (could also be just a map[string]interface{}).
        var t Tweet
        err := json.Unmarshal(*hit.Source, &t)
        if err != nil {
            // Deserialization failed
        }

        // Work with tweet
        fmt.Printf("Tweet by %s: %s\n", t.User, t.Message)
    }
} else {
    // No hits
    fmt.Print("Found no tweets\n")
}

// Delete the index again
_, err = client.DeleteIndex("twitter").Do(ctx)
if err != nil {
    // Handle error
    panic(err)
}
```

Here's a [link to a complete working example](https://gist.github.com/olivere/114347ff9d9cfdca7bdc0ecea8b82263).

See the [wiki](https://github.com/olivere/elastic/wiki) for more details.


## API Status

### Document APIs

- [x] Index API
- [x] Get API
- [x] Delete API
- [x] Delete By Query API
- [x] Update API
- [x] Update By Query API
- [x] Multi Get API
- [x] Bulk API
- [x] Reindex API
- [x] Term Vectors
- [x] Multi termvectors API

### Search APIs

- [x] Search
- [x] Search Template
- [ ] Multi Search Template
- [ ] Search Shards API
- [x] Suggesters
  - [x] Term Suggester
  - [x] Phrase Suggester
  - [x] Completion Suggester
  - [x] Context Suggester
- [x] Multi Search API
- [x] Count API
- [ ] Search Exists API
- [ ] Validate API
- [x] Explain API
- [x] Profile API
- [x] Field Stats API

### Aggregations

- Metrics Aggregations
  - [x] Avg
  - [x] Cardinality
  - [x] Extended Stats
  - [x] Geo Bounds
  - [ ] Geo Centroid
  - [x] Max
  - [x] Min
  - [x] Percentiles
  - [x] Percentile Ranks
  - [ ] Scripted Metric
  - [x] Stats
  - [x] Sum
  - [x] Top Hits
  - [x] Value Count
- Bucket Aggregations
  - [x] Children
  - [x] Date Histogram
  - [x] Date Range
  - [x] Filter
  - [x] Filters
  - [x] Geo Distance
  - [ ] GeoHash Grid
  - [x] Global
  - [x] Histogram
  - [x] IP Range
  - [x] Missing
  - [x] Nested
  - [x] Range
  - [x] Reverse Nested
  - [x] Sampler
  - [x] Significant Terms
  - [x] Terms
- Pipeline Aggregations
  - [x] Avg Bucket
  - [x] Derivative
  - [x] Max Bucket
  - [x] Min Bucket
  - [x] Sum Bucket
  - [x] Stats Bucket
  - [ ] Extended Stats Bucket
  - [x] Percentiles Bucket
  - [x] Moving Average
  - [x] Cumulative Sum
  - [x] Bucket Script
  - [x] Bucket Selector
  - [x] Serial Differencing
- [x] Matrix Aggregations
  - [x] Matrix Stats
- [x] Aggregation Metadata

### Indices APIs

- [x] Create Index
- [x] Delete Index
- [x] Get Index
- [x] Indices Exists
- [x] Open / Close Index
- [x] Shrink Index
- [x] Rollover Index
- [x] Put Mapping
- [x] Get Mapping
- [x] Get Field Mapping
- [x] Types Exists
- [x] Index Aliases
- [x] Update Indices Settings
- [x] Get Settings
- [x] Analyze
- [x] Index Templates
- [ ] Shadow Replica Indices
- [x] Indices Stats
- [ ] Indices Segments
- [ ] Indices Recovery
- [ ] Indices Shard Stores
- [ ] Clear Cache
- [x] Flush
- [x] Refresh
- [x] Force Merge
- [ ] Upgrade

### cat APIs

The cat APIs are not implemented as of now. We think they are better suited for operating with Elasticsearch on the command line.

- [ ] cat aliases
- [ ] cat allocation
- [ ] cat count
- [ ] cat fielddata
- [ ] cat health
- [ ] cat indices
- [ ] cat master
- [ ] cat nodeattrs
- [ ] cat nodes
- [ ] cat pending tasks
- [ ] cat plugins
- [ ] cat recovery
- [ ] cat repositories
- [ ] cat thread pool
- [ ] cat shards
- [ ] cat segments
- [ ] cat snapshots

### Cluster APIs

- [x] Cluster Health
- [x] Cluster State
- [x] Cluster Stats
- [ ] Pending Cluster Tasks
- [ ] Cluster Reroute
- [ ] Cluster Update Settings
- [x] Nodes Stats
- [x] Nodes Info
- [x] Task Management API
- [ ] Nodes hot_threads
- [ ] Cluster Allocation Explain API

### Query DSL

- [x] Match All Query
- [x] Inner hits
- Full text queries
  - [x] Match Query
  - [x] Match Phrase Query
  - [x] Match Phrase Prefix Query
  - [x] Multi Match Query
  - [x] Common Terms Query
  - [x] Query String Query
  - [x] Simple Query String Query
- Term level queries
  - [x] Term Query
  - [x] Terms Query
  - [x] Range Query
  - [x] Exists Query
  - [x] Prefix Query
  - [x] Wildcard Query
  - [x] Regexp Query
  - [x] Fuzzy Query
  - [x] Type Query
  - [x] Ids Query
- Compound queries
  - [x] Constant Score Query
  - [x] Bool Query
  - [x] Dis Max Query
  - [x] Function Score Query
  - [x] Boosting Query
  - [x] Indices Query
- Joining queries
  - [x] Nested Query
  - [x] Has Child Query
  - [x] Has Parent Query
  - [x] Parent Id Query
- Geo queries
  - [ ] GeoShape Query
  - [x] Geo Bounding Box Query
  - [x] Geo Distance Query
  - [ ] Geo Distance Range Query
  - [x] Geo Polygon Query
  - [ ] Geohash Cell Query
- Specialized queries
  - [x] More Like This Query
  - [x] Template Query
  - [x] Script Query
  - [x] Percolate Query
- Span queries
  - [ ] Span Term Query
  - [ ] Span Multi Term Query
  - [ ] Span First Query
  - [ ] Span Near Query
  - [ ] Span Or Query
  - [ ] Span Not Query
  - [ ] Span Containing Query
  - [ ] Span Within Query
  - [ ] Span Field Masking Query
- [ ] Minimum Should Match
- [ ] Multi Term Query Rewrite

### Modules

- Snapshot and Restore
  - [x] Repositories
  - [ ] Snapshot
  - [ ] Restore
  - [ ] Snapshot status
  - [ ] Monitoring snapshot/restore status
  - [ ] Stopping currently running snapshot and restore

### Sorting

- [x] Sort by score
- [x] Sort by field
- [x] Sort by geo distance
- [x] Sort by script
- [x] Sort by doc

### Scrolling

Scrolling is supported via a  `ScrollService`. It supports an iterator-like interface.
The `ClearScroll` API is implemented as well.

A pattern for [efficiently scrolling in parallel](https://github.com/olivere/elastic/wiki/ScrollParallel)
is described in the [Wiki](https://github.com/olivere/elastic/wiki).

## How to contribute

Read [the contribution guidelines](https://github.com/olivere/elastic/blob/master/CONTRIBUTING.md).

## Credits

Thanks a lot for the great folks working hard on
[Elasticsearch](https://www.elastic.co/products/elasticsearch)
and
[Go](https://golang.org/).

Elastic uses portions of the
[uritemplates](https://github.com/jtacoma/uritemplates) library
by Joshua Tacoma,
[backoff](https://github.com/cenkalti/backoff) by Cenk Altı and
[leaktest](https://github.com/fortytw2/leaktest) by Ian Chiles.

## LICENSE

MIT-LICENSE. See [LICENSE](http://olivere.mit-license.org/)
or the LICENSE file provided in the repository for details.
# Cluster Test

This directory contains a program you can use to test a cluster.

Here's how:

First, install a cluster of Elasticsearch nodes. You can install them on
different computers, or start several nodes on a single machine.

Build cluster-test by `go build cluster-test.go` (or build with `make`).

Run `./cluster-test -h` to get a list of flags:

```sh
$ ./cluster-test -h
Usage of ./cluster-test:
  -errorlog="": error log file
  -healthcheck=true: enable or disable healthchecks
  -healthchecker=1m0s: healthcheck interval
  -index="twitter": name of ES index to use
  -infolog="": info log file
  -n=5: number of goroutines that run searches
  -nodes="": comma-separated list of ES URLs (e.g. 'http://192.168.2.10:9200,http://192.168.2.11:9200')
  -retries=0: number of retries
  -sniff=true: enable or disable sniffer
  -sniffer=15m0s: sniffer interval
  -tracelog="": trace log file
```

Example:

```sh
$ ./cluster-test -nodes=http://127.0.0.1:9200,http://127.0.0.1:9201,http://127.0.0.1:9202 -n=5 -index=twitter -retries=5 -sniff=true -sniffer=10s -healthcheck=true -healthchecker=5s -errorlog=error.log
```

The above example will create an index and start some search jobs on the
cluster defined by http://127.0.0.1:9200, http://127.0.0.1:9201,
and http://127.0.0.1:9202.

* It will create an index called `twitter` on the cluster (`-index=twitter`)
* It will run 5 search jobs in parallel (`-n=5`).
* It will retry failed requests 5 times (`-retries=5`).
* It will sniff the cluster periodically (`-sniff=true`).
* It will sniff the cluster every 10 seconds (`-sniffer=10s`).
* It will perform health checks periodically (`-healthcheck=true`).
* It will perform health checks on the nodes every 5 seconds (`-healthchecker=5s`).
* It will write an error log file (`-errorlog=error.log`).

If you want to test Elastic with nodes going up and down, you can use a
chaos monkey script like this and run it on the nodes of your cluster:

```sh
#!/bin/bash
while true
do
	echo "Starting ES node"
	elasticsearch -d -Xmx4g -Xms1g -Des.config=elasticsearch.yml -p es.pid
	sleep `jot -r 1 10 300` # wait for 10-300s
	echo "Stopping ES node"
	kill -TERM `cat es.pid`
	sleep `jot -r 1 10 60`  # wait for 10-60s
done
```
# goquery - a little like that j-thing, only in Go [![build status](https://secure.travis-ci.org/PuerkitoBio/goquery.png)](http://travis-ci.org/PuerkitoBio/goquery) [![GoDoc](https://godoc.org/github.com/PuerkitoBio/goquery?status.png)](http://godoc.org/github.com/PuerkitoBio/goquery)

goquery brings a syntax and a set of features similar to [jQuery][] to the [Go language][go]. It is based on Go's [net/html package][html] and the CSS Selector library [cascadia][]. Since the net/html parser returns nodes, and not a full-featured DOM tree, jQuery's stateful manipulation functions (like height(), css(), detach()) have been left off.

Also, because the net/html parser requires UTF-8 encoding, so does goquery: it is the caller's responsibility to ensure that the source document provides UTF-8 encoded HTML. See the [wiki][] for various options to do this.

Syntax-wise, it is as close as possible to jQuery, with the same function names when possible, and that warm and fuzzy chainable interface. jQuery being the ultra-popular library that it is, I felt that writing a similar HTML-manipulating library was better to follow its API than to start anew (in the same spirit as Go's `fmt` package), even though some of its methods are less than intuitive (looking at you, [index()][index]...).

## Installation

Please note that because of the net/html dependency, goquery requires Go1.1+.

    $ go get github.com/PuerkitoBio/goquery

(optional) To run unit tests:

    $ cd $GOPATH/src/github.com/PuerkitoBio/goquery
    $ go test

(optional) To run benchmarks (warning: it runs for a few minutes):

    $ cd $GOPATH/src/github.com/PuerkitoBio/goquery
    $ go test -bench=".*"

## Changelog

**Note that goquery's API is now stable, and will not break.**

*    **2017-02-12 (v1.1.0)** : Add `SetHtml` and `SetText` (thanks to @glebtv).
*    **2016-12-29 (v1.0.2)** : Optimize allocations for `Selection.Text` (thanks to @radovskyb).
*    **2016-08-28 (v1.0.1)** : Optimize performance for large documents.
*    **2016-07-27 (v1.0.0)** : Tag version 1.0.0.
*    **2016-06-15** : Invalid selector strings internally compile to a `Matcher` implementation that never matches any node (instead of a panic). So for example, `doc.Find("~")` returns an empty `*Selection` object.
*    **2016-02-02** : Add `NodeName` utility function similar to the DOM's `nodeName` property. It returns the tag name of the first element in a selection, and other relevant values of non-element nodes (see godoc for details). Add `OuterHtml` utility function similar to the DOM's `outerHTML` property (named `OuterHtml` in small caps for consistency with the existing `Html` method on the `Selection`).
*    **2015-04-20** : Add `AttrOr` helper method to return the attribute's value or a default value if absent. Thanks to [piotrkowalczuk][piotr].
*    **2015-02-04** : Add more manipulation functions - Prepend* - thanks again to [Andrew Stone][thatguystone].
*    **2014-11-28** : Add more manipulation functions - ReplaceWith*, Wrap* and Unwrap - thanks again to [Andrew Stone][thatguystone].
*    **2014-11-07** : Add manipulation functions (thanks to [Andrew Stone][thatguystone]) and `*Matcher` functions, that receive compiled cascadia selectors instead of selector strings, thus avoiding potential panics thrown by goquery via `cascadia.MustCompile` calls. This results in better performance (selectors can be compiled once and reused) and more idiomatic error handling (you can handle cascadia's compilation errors, instead of recovering from panics, which had been bugging me for a long time). Note that the actual type expected is a `Matcher` interface, that `cascadia.Selector` implements. Other matcher implementations could be used.
*    **2014-11-06** : Change import paths of net/html to golang.org/x/net/html (see https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA). Make sure to update your code to use the new import path too when you call goquery with `html.Node`s.
*    **v0.3.2** : Add `NewDocumentFromReader()` (thanks jweir) which allows creating a goquery document from an io.Reader.
*    **v0.3.1** : Add `NewDocumentFromResponse()` (thanks assassingj) which allows creating a goquery document from an http response.
*    **v0.3.0** : Add `EachWithBreak()` which allows to break out of an `Each()` loop by returning false. This function was added instead of changing the existing `Each()` to avoid breaking compatibility.
*    **v0.2.1** : Make go-getable, now that [go.net/html is Go1.0-compatible][gonet] (thanks to @matrixik for pointing this out).
*    **v0.2.0** : Add support for negative indices in Slice(). **BREAKING CHANGE** `Document.Root` is removed, `Document` is now a `Selection` itself (a selection of one, the root element, just like `Document.Root` was before). Add jQuery's Closest() method.
*    **v0.1.1** : Add benchmarks to use as baseline for refactorings, refactor Next...() and Prev...() methods to use the new html package's linked list features (Next/PrevSibling, FirstChild). Good performance boost (40+% in some cases).
*    **v0.1.0** : Initial release.

## API

goquery exposes two structs, `Document` and `Selection`, and the `Matcher` interface. Unlike jQuery, which is loaded as part of a DOM document, and thus acts on its containing document, goquery doesn't know which HTML document to act upon. So it needs to be told, and that's what the `Document` type is for. It holds the root document node as the initial Selection value to manipulate.

jQuery often has many variants for the same function (no argument, a selector string argument, a jQuery object argument, a DOM element argument, ...). Instead of exposing the same features in goquery as a single method with variadic empty interface arguments, statically-typed signatures are used following this naming convention:

*    When the jQuery equivalent can be called with no argument, it has the same name as jQuery for the no argument signature (e.g.: `Prev()`), and the version with a selector string argument is called `XxxFiltered()` (e.g.: `PrevFiltered()`)
*    When the jQuery equivalent **requires** one argument, the same name as jQuery is used for the selector string version (e.g.: `Is()`)
*    The signatures accepting a jQuery object as argument are defined in goquery as `XxxSelection()` and take a `*Selection` object as argument (e.g.: `FilterSelection()`)
*    The signatures accepting a DOM element as argument in jQuery are defined in goquery as `XxxNodes()` and take a variadic argument of type `*html.Node` (e.g.: `FilterNodes()`)
*    The signatures accepting a function as argument in jQuery are defined in goquery as `XxxFunction()` and take a function as argument (e.g.: `FilterFunction()`)
*    The goquery methods that can be called with a selector string have a corresponding version that take a `Matcher` interface and are defined as `XxxMatcher()` (e.g.: `IsMatcher()`)

Utility functions that are not in jQuery but are useful in Go are implemented as functions (that take a `*Selection` as parameter), to avoid a potential naming clash on the `*Selection`'s methods (reserved for jQuery-equivalent behaviour).

The complete [godoc reference documentation can be found here][doc].

Please note that Cascadia's selectors do not necessarily match all supported selectors of jQuery (Sizzle). See the [cascadia project][cascadia] for details. Invalid selector strings compile to a `Matcher` that fails to match any node. Behaviour of the various functions that take a selector string as argument follows from that fact, e.g. (where `~` is an invalid selector string):

* `Find("~")` returns an empty selection because the selector string doesn't match anything.
* `Add("~")` returns a new selection that holds the same nodes as the original selection, because it didn't add any node (selector string didn't match anything).
* `ParentsFiltered("~")` returns an empty selection because the selector string doesn't match anything.
* `ParentsUntil("~")` returns all parents of the selection because the selector string didn't match any element to stop before the top element.

## Examples

See some tips and tricks in the [wiki][].

Adapted from example_test.go:

```Go
package main

import (
  "fmt"
  "log"

  "github.com/PuerkitoBio/goquery"
)

func ExampleScrape() {
  doc, err := goquery.NewDocument("http://metalsucks.net")
  if err != nil {
    log.Fatal(err)
  }

  // Find the review items
  doc.Find(".sidebar-reviews article .content-block").Each(func(i int, s *goquery.Selection) {
    // For each item found, get the band and title
    band := s.Find("a").Text()
    title := s.Find("i").Text()
    fmt.Printf("Review %d: %s - %s\n", i, band, title)
  })
}

func main() {
  ExampleScrape()
}
```

## License

The [BSD 3-Clause license][bsd], the same as the [Go language][golic]. Cascadia's license is [here][caslic].

[jquery]: http://jquery.com/
[go]: http://golang.org/
[cascadia]: https://github.com/andybalholm/cascadia
[bsd]: http://opensource.org/licenses/BSD-3-Clause
[golic]: http://golang.org/LICENSE
[caslic]: https://github.com/andybalholm/cascadia/blob/master/LICENSE
[doc]: http://godoc.org/github.com/PuerkitoBio/goquery
[index]: http://api.jquery.com/index/
[gonet]: https://github.com/golang/net/
[html]: http://godoc.org/golang.org/x/net/html
[wiki]: https://github.com/PuerkitoBio/goquery/wiki/Tips-and-tricks
[thatguystone]: https://github.com/thatguystone
[piotr]: https://github.com/piotrkowalczuk
# errors [![Travis-CI](https://travis-ci.org/pkg/errors.svg)](https://travis-ci.org/pkg/errors) [![AppVeyor](https://ci.appveyor.com/api/projects/status/b98mptawhudj53ep/branch/master?svg=true)](https://ci.appveyor.com/project/davecheney/errors/branch/master) [![GoDoc](https://godoc.org/github.com/pkg/errors?status.svg)](http://godoc.org/github.com/pkg/errors) [![Report card](https://goreportcard.com/badge/github.com/pkg/errors)](https://goreportcard.com/report/github.com/pkg/errors)

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

## Licence

BSD-2-Clause
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/sirupsen/logrus.svg?branch=master)](https://travis-ci.org/sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/sirupsen/logrus?status.svg)](https://godoc.org/github.com/sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc].

**Seeing weird case-sensitive problems?** It's in the past been possible to
import Logrus as both upper- and lower-case. Due to the Go package environment,
this caused issues in the community and we needed a standard. Some environments
experienced problems with the upper-case variant, so the lower-case was decided.
Everything using `logrus` will need to use the lower-case:
`github.com/sirupsen/logrus`. Any package that isn't, should be changed.

To fix Glide, see [these
comments](https://github.com/sirupsen/logrus/issues/553#issuecomment-306591437).
For an in-depth explanation of the casing issue, see [this
comment](https://github.com/sirupsen/logrus/issues/570#issuecomment-313933276).

**Are you interested in assisting in maintaining Logrus?** Currently I have a
lot of obligations, and I am unable to provide Logrus with the maintainership it
needs. If you'd like to help, please reach out to me at `simon at author's
username dot com`.

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

#### Case-sensitivity

The organization's name was changed to lower-case--and this will not be changed
back. If you are getting import conflicts due to case sensitivity, please use
the lower-case import: `github.com/sirupsen/logrus`.

#### Example

The simplest way to use Logrus is simply the package-level exported logger:

```go
package main

import (
  log "github.com/sirupsen/logrus"
)

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
  }).Info("A walrus appears")
}
```

Note that it's completely api-compatible with the stdlib logger, so you can
replace your `log` imports everywhere with `log "github.com/sirupsen/logrus"`
and you'll now have the flexibility of Logrus. You can customize it all you
want:

```go
package main

import (
  "os"
  log "github.com/sirupsen/logrus"
)

func init() {
  // Log as JSON instead of the default ASCII formatter.
  log.SetFormatter(&log.JSONFormatter{})

  // Output to stdout instead of the default stderr
  // Can be any io.Writer, see below for File example
  log.SetOutput(os.Stdout)

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
  "os"
  "github.com/sirupsen/logrus"
)

// Create a new instance of the logger. You can have any number of instances.
var log = logrus.New()

func main() {
  // The API for setting attributes is a little different than the package level
  // exported logger. See Godoc.
  log.Out = os.Stdout

  // You could set this to any `io.Writer` such as a file
  // file, err := os.OpenFile("logrus.log", os.O_CREATE|os.O_WRONLY, 0666)
  // if err == nil {
  //  log.Out = file
  // } else {
  //  log.Info("Failed to log to file, using default stderr")
  // }

  log.WithFields(logrus.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")
}
```

#### Fields

Logrus encourages careful, structured logging through logging fields instead of
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

#### Default Fields

Often it's helpful to have fields _always_ attached to log statements in an
application or parts of one. For example, you may want to always log the
`request_id` and `user_ip` in the context of a request. Instead of writing
`log.WithFields(log.Fields{"request_id": request_id, "user_ip": user_ip})` on
every line, you can create a `logrus.Entry` to pass around instead:

```go
requestLogger := log.WithFields(log.Fields{"request_id": request_id, "user_ip": user_ip})
requestLogger.Info("something happened on that request") # will log request_id and user_ip
requestLogger.Warn("something not great happened")
```

#### Hooks

You can add hooks for logging levels. For example to send errors to an exception
tracking service on `Error`, `Fatal` and `Panic`, info to StatsD or log to
multiple places simultaneously, e.g. syslog.

Logrus comes with [built-in hooks](hooks/). Add those, or your custom hook, in
`init`:

```go
import (
  log "github.com/sirupsen/logrus"
  "gopkg.in/gemnasium/logrus-airbrake-hook.v2" // the package is named "aibrake"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
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
| [Airbrake "legacy"](https://github.com/gemnasium/logrus-airbrake-legacy-hook) | Send errors to an exception tracking service compatible with the Airbrake API V2. Uses [`airbrake-go`](https://github.com/tobi/airbrake-go) behind the scenes. |
| [Airbrake](https://github.com/gemnasium/logrus-airbrake-hook) | Send errors to the Airbrake API V3. Uses the official [`gobrake`](https://github.com/airbrake/gobrake) behind the scenes. |
| [Amazon Kinesis](https://github.com/evalphobia/logrus_kinesis) | Hook for logging to [Amazon Kinesis](https://aws.amazon.com/kinesis/) |
| [Amqp-Hook](https://github.com/vladoatanasov/logrus_amqp) | Hook for logging to Amqp broker (Like RabbitMQ) |
| [Bugsnag](https://github.com/Shopify/logrus-bugsnag/blob/master/bugsnag.go) | Send errors to the Bugsnag exception tracking service. |
| [DeferPanic](https://github.com/deferpanic/dp-logrus) | Hook for logging to DeferPanic |
| [Discordrus](https://github.com/kz/discordrus) | Hook for logging to [Discord](https://discordapp.com/) |
| [ElasticSearch](https://github.com/sohlich/elogrus) | Hook for logging to ElasticSearch|
| [Firehose](https://github.com/beaubrewer/logrus_firehose) | Hook for logging to [Amazon Firehose](https://aws.amazon.com/kinesis/firehose/)
| [Fluentd](https://github.com/evalphobia/logrus_fluent) | Hook for logging to fluentd |
| [Go-Slack](https://github.com/multiplay/go-slack) | Hook for logging to [Slack](https://slack.com) |
| [Graylog](https://github.com/gemnasium/logrus-graylog-hook) | Hook for logging to [Graylog](http://graylog2.org/) |
| [Hiprus](https://github.com/nubo/hiprus) | Send errors to a channel in hipchat. |
| [Honeybadger](https://github.com/agonzalezro/logrus_honeybadger) | Hook for sending exceptions to Honeybadger |
| [InfluxDB](https://github.com/Abramovic/logrus_influxdb) | Hook for logging to influxdb |
| [Influxus](http://github.com/vlad-doru/influxus) | Hook for concurrently logging to [InfluxDB](http://influxdata.com/) |
| [Journalhook](https://github.com/wercker/journalhook) | Hook for logging to `systemd-journald` |
| [KafkaLogrus](https://github.com/goibibo/KafkaLogrus) | Hook for logging to kafka |
| [LFShook](https://github.com/rifflock/lfshook) | Hook for logging to the local filesystem |
| [Logentries](https://github.com/jcftang/logentriesrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logentrus](https://github.com/puddingfactory/logentrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [Mail](https://github.com/zbindenren/logrus_mail) | Hook for sending exceptions via mail |
| [Mattermost](https://github.com/shuLhan/mattermost-integration/tree/master/hooks/logrus) | Hook for logging to [Mattermost](https://mattermost.com/) |
| [Mongodb](https://github.com/weekface/mgorus) | Hook for logging to mongodb |
| [NATS-Hook](https://github.com/rybit/nats_logrus_hook) | Hook for logging to [NATS](https://nats.io) |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [Papertrail](https://github.com/polds/logrus-papertrail-hook) | Send errors to the [Papertrail](https://papertrailapp.com) hosted logging service via UDP. |
| [PostgreSQL](https://github.com/gemnasium/logrus-postgresql-hook) | Send logs to [PostgreSQL](http://postgresql.org) |
| [Pushover](https://github.com/toorop/logrus_pushover) | Send error via [Pushover](https://pushover.net) |
| [Raygun](https://github.com/squirkle/logrus-raygun-hook) | Hook for logging to [Raygun.io](http://raygun.io/) |
| [Redis-Hook](https://github.com/rogierlommers/logrus-redis-hook) | Hook for logging to a ELK stack (through Redis) |
| [Rollrus](https://github.com/heroku/rollrus) | Hook for sending errors to rollbar |
| [Scribe](https://github.com/sagar8192/logrus-scribe-hook) | Hook for logging to [Scribe](https://github.com/facebookarchive/scribe)|
| [Sentry](https://github.com/evalphobia/logrus_sentry) | Send errors to the Sentry error logging and aggregation service. |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Stackdriver](https://github.com/knq/sdhook) | Hook for logging to [Google Stackdriver](https://cloud.google.com/logging/) |
| [Sumorus](https://github.com/doublefree/sumorus) | Hook for logging to [SumoLogic](https://www.sumologic.com/)|
| [Syslog](https://github.com/sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [Syslog TLS](https://github.com/shinji62/logrus-syslog-ng) | Send errors to remote syslog server with TLS support. |
| [TraceView](https://github.com/evalphobia/logrus_appneta) | Hook for logging to [AppNeta TraceView](https://www.appneta.com/products/traceview/) |
| [Typetalk](https://github.com/dragon3/logrus-typetalk-hook) | Hook for logging to [Typetalk](https://www.typetalk.in/) |
| [logz.io](https://github.com/ripcurld00d/logrus-logzio-hook) | Hook for logging to [logz.io](https://logz.io), a Log as a Service using Logstash |
| [SQS-Hook](https://github.com/tsarpaul/logrus_sqs) | Hook for logging to [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) |

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
  log "github.com/sirupsen/logrus"
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
    `DisableColors` field to `true`. For Windows, see
    [github.com/mattn/go-colorable](https://github.com/mattn/go-colorable).
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#TextFormatter).
* `logrus.JSONFormatter`. Logs fields as JSON.
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#JSONFormatter).

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

This means that we can override the standard library logger easily:

```go
logger := logrus.New()
logger.Formatter = &logrus.JSONFormatter{}

// Use logrus for standard log output
// Note that `log` here references stdlib's log
// Not logrus imported under the name `log`.
log.SetOutput(logger.Writer())
```

#### Rotation

Log rotation is not provided with Logrus. Log rotation should be done by an
external program (like `logrotate(8)`) that can compress and delete old log
entries. It should not be a feature of the application-level logger.

#### Tools

| Tool | Description |
| ---- | ----------- |
|[Logrus Mate](https://github.com/gogap/logrus_mate)|Logrus mate is a tool for Logrus to manage loggers, you can initial logger's level, hook and formatter by config file, the logger will generated with different config at different environment.|
|[Logrus Viper Helper](https://github.com/heirko/go-contrib/tree/master/logrusHelper)|An Helper around Logrus to wrap with spf13/Viper to load configuration with fangs! And to simplify Logrus configuration use some behavior of [Logrus Mate](https://github.com/gogap/logrus_mate). [sample](https://github.com/heirko/iris-contrib/blob/master/middleware/logrus-logger/example) |

#### Testing

Logrus has a built in facility for asserting the presence of log messages. This is implemented through the `test` hook and provides:

* decorators for existing logger (`test.NewLocal` and `test.NewGlobal`) which basically just add the `test` hook
* a test logger (`test.NewNullLogger`) that just records log messages (and does not output any):

```go
import(
  "github.com/sirupsen/logrus"
  "github.com/sirupsen/logrus/hooks/test"
  "github.com/stretchr/testify/assert"
  "testing"
)

func TestSomething(t*testing.T){
  logger, hook := test.NewNullLogger()
  logger.Error("Helloerror")

  assert.Equal(t, 1, len(hook.Entries))
  assert.Equal(t, logrus.ErrorLevel, hook.LastEntry().Level)
  assert.Equal(t, "Helloerror", hook.LastEntry().Message)

  hook.Reset()
  assert.Nil(t, hook.LastEntry())
}
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

#### Thread safety

By default Logger is protected by mutex for concurrent writes, this mutex is invoked when calling hooks and writing logs.
If you are sure such locking is not needed, you can call logger.SetNoLock() to disable the locking.

Situation when locking is not needed includes:

* You have no hooks registered, or hooks calling is already thread-safe.

* Writing to logger.Out is already thread-safe, for example:

  1) logger.Out is protected by locks.

  2) logger.Out is a os.File handler opened with `O_APPEND` flag, and every write is smaller than 4k. (This allow multi-thread/multi-process writing)

     (Refer to http://www.notthewizard.com/2014/06/17/are-files-appends-really-atomic/)
# Syslog Hooks for Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>

## Usage

```go
import (
  "log/syslog"
  "github.com/sirupsen/logrus"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```

If you want to connect to local syslog (Ex. "/dev/log" or "/var/run/syslog" or "/var/run/log"). Just assign empty string to the first two parameters of `NewSyslogHook`. It should look like the following.

```go
import (
  "log/syslog"
  "github.com/sirupsen/logrus"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("", "", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```
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
gorilla/mux
===
[![GoDoc](https://godoc.org/github.com/gorilla/mux?status.svg)](https://godoc.org/github.com/gorilla/mux)
[![Build Status](https://travis-ci.org/gorilla/mux.svg?branch=master)](https://travis-ci.org/gorilla/mux)
[![Sourcegraph](https://sourcegraph.com/github.com/gorilla/mux/-/badge.svg)](https://sourcegraph.com/github.com/gorilla/mux?badge)

![Gorilla Logo](http://www.gorillatoolkit.org/static/images/gorilla-icon-64.png)

http://www.gorillatoolkit.org/pkg/mux

Package `gorilla/mux` implements a request router and dispatcher for matching incoming requests to
their respective handler.

The name mux stands for "HTTP request multiplexer". Like the standard `http.ServeMux`, `mux.Router` matches incoming requests against a list of registered routes and calls a handler for the route that matches the URL or other conditions. The main features are:

* It implements the `http.Handler` interface so it is compatible with the standard `http.ServeMux`.
* Requests can be matched based on URL host, path, path prefix, schemes, header and query values, HTTP methods or using custom matchers.
* URL hosts and paths can have variables with an optional regular expression.
* Registered URLs can be built, or "reversed", which helps maintaining references to resources.
* Routes can be used as subrouters: nested routes are only tested if the parent route matches. This is useful to define groups of routes that share common conditions like a host, a path prefix or other repeated attributes. As a bonus, this optimizes request matching.

---

* [Install](#install)
* [Examples](#examples)
* [Matching Routes](#matching-routes)
* [Listing Routes](#listing-routes)
* [Static Files](#static-files)
* [Registered URLs](#registered-urls)
* [Full Example](#full-example)

---

## Install

With a [correctly configured](https://golang.org/doc/install#testing) Go toolchain:

```sh
go get -u github.com/gorilla/mux
```

## Examples

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
func ArticlesCategoryHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "Category: %v\n", vars["category"])
}
```

And this is all you need to know about the basic usage. More advanced options are explained below.

### Matching Routes

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
s.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler)
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

### Listing Routes

Routes on a mux can be listed using the Router.Walk method—useful for generating documentation:

```go
package main

import (
    "fmt"
    "net/http"
    "strings"

    "github.com/gorilla/mux"
)

func handler(w http.ResponseWriter, r *http.Request) {
    return
}

func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", handler)
    r.Methods("POST").HandleFunc("/products", handler)
    r.Methods("GET").HandleFunc("/articles", handler)
    r.Methods("GET", "PUT").HandleFunc("/articles/{id}", handler)
    r.Walk(func(route *mux.Route, router *mux.Router, ancestors []*mux.Route) error {
        t, err := route.GetPathTemplate()
        if err != nil {
            return err
        }
        // p will contain regular expression is compatible with regular expression in Perl, Python, and other languages.
        // for instance the regular expression for path '/articles/{id}' will be '^/articles/(?P<v0>[^/]+)$'
        p, err := route.GetPathRegexp()
        if err != nil {
            return err
        }
        m, err := route.GetMethods()
        if err != nil {
            return err
        }
        fmt.Println(strings.Join(m, ","), t, p)
        return nil
    })
    http.Handle("/", r)
}
```

### Static Files

Note that the path provided to `PathPrefix()` represents a "wildcard": calling
`PathPrefix("/static/").Handler(...)` means that the handler will be passed any
request that matches "/static/*". This makes it easy to serve static files with mux:

```go
func main() {
	var dir string

	flag.StringVar(&dir, "dir", ".", "the directory to serve files from. Defaults to the current dir")
	flag.Parse()
	r := mux.NewRouter()

	// This will serve files under http://localhost:8000/static/<filename>
	r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir(dir))))

	srv := &http.Server{
		Handler:      r,
		Addr:         "127.0.0.1:8000",
		// Good practice: enforce timeouts for servers you create!
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	log.Fatal(srv.ListenAndServe())
}
```

### Registered URLs

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
[![Sourcegraph](https://sourcegraph.com/github.com/gorilla/handlers/-/badge.svg)](https://sourcegraph.com/github.com/gorilla/handlers?badge)


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

# cascadia

[![](https://travis-ci.org/andybalholm/cascadia.svg)](https://travis-ci.org/andybalholm/cascadia)

The Cascadia package implements CSS selectors for use with the parse trees produced by the html package.

To test CSS selectors without writing Go code, check out [cascadia](https://github.com/suntong/cascadia) the command line tool, a thin wrapper around this package.
# [go-xkcd](https://github.com/nishanths/go-xkcd)

xkcd API client for Golang.

[![wercker status](https://app.wercker.com/status/6c1de0bfd64a428d6ece5a2337268160/s "wercker status")](https://app.wercker.com/project/bykey/6c1de0bfd64a428d6ece5a2337268160) [![Coverage Status](https://coveralls.io/repos/github/nishanths/go-xkcd/badge.svg?branch=master)](https://coveralls.io/github/nishanths/go-xkcd?branch=master)
[![GoDoc](https://godoc.org/github.com/nishanths/go-xkcd?status.svg)](https://godoc.org/github.com/nishanths/go-xkcd)

[<img alt="https://xkcd.com/1481/" title="https://xkcd.com/1481/" src="http://imgs.xkcd.com/comics/api.png" width="250">](https://xkcd.com/1481/)

Details on the xkcd API can be found [here](https://xkcd.com/json.html).

## Install

```
$ go get github.com/nishanths/go-xkcd
```

Import the package using `github.com/nishanths/go-xkcd` and refer to it as `xkcd`. 

Each major version has a separate branch. If you need a specific version, please clone the branch instead.

## Example

The following program prints details about [xkcd.com/599](http://xkcd.com/599):

```go
package main

import (
    "fmt"
    "log"

    "github.com/nishanths/go-xkcd"
)

func main() {
    client := xkcd.NewClient()
    comic, err := client.Get(599)

    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("%s: %s", comic.Title, comic.ImageURL) // Apocalypse: http://imgs.xkcd.com/comics/apocalypse.png
}

```

## Test

To run tests:

```
$ go test
```

## Documentation

View Go Doc [online](https://godoc.org/github.com/nishanths/go-xkcd).

To view go docs locally, after installing the package run:

```
$ godoc -http=:6060
```

Then visit [`http://localhost:6060/pkg/github.com/nishanths/go-xkcd/`](http://localhost:6060/pkg/github.com/nishanths/go-xkcd/) in your browser.

#### Methods

The following methods are available on the client. All the methods return `(Comic, error)`.

* `Latest()`
* `Get(number int)`
* `Random()`
* `RandomInRange(begin, end, latest int)`

The fields available on `Comic` are:

```
type Comic struct {
	Alt         string
	PublishDate time.Time
	ImageURL    string
	URL         string
	News        string
	Number      int
	SafeTitle   string
	Title       string
	Transcript  string
}
```

## Contributing

Pull requests and issues are welcome!

To create a new pull request:

1. Fork the repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request on GitHub

## License

The [MIT License](http://nishanths.mit-license.org). Copyright © [Nishanth Shanmugham](https://github.com/nishanths).
