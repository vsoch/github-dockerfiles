# OAuth2 for Go

[![Build Status](https://travis-ci.org/golang/oauth2.svg?branch=master)](https://travis-ci.org/golang/oauth2)
[![GoDoc](https://godoc.org/golang.org/x/oauth2?status.svg)](https://godoc.org/golang.org/x/oauth2)

oauth2 package contains a client implementation for OAuth 2.0 spec.

## Installation

~~~~
go get golang.org/x/oauth2
~~~~

See godoc for further documentation and examples.

* [godoc.org/golang.org/x/oauth2](http://godoc.org/golang.org/x/oauth2)
* [godoc.org/golang.org/x/oauth2/google](http://godoc.org/golang.org/x/oauth2/google)


## App Engine

In change 96e89be (March 2015) we removed the `oauth2.Context2` type in favor
of the [`context.Context`](https://golang.org/x/net/context#Context) type from
the `golang.org/x/net/context` package

This means its no longer possible to use the "Classic App Engine"
`appengine.Context` type with the `oauth2` package. (You're using
Classic App Engine if you import the package `"appengine"`.)

To work around this, you may use the new `"google.golang.org/appengine"`
package. This package has almost the same API as the `"appengine"` package,
but it can be fetched with `go get` and used on "Managed VMs" and well as
Classic App Engine.

See the [new `appengine` package's readme](https://github.com/golang/appengine#updating-a-go-app-engine-app)
for information on updating your app.

If you don't want to update your entire app to use the new App Engine packages,
you may use both sets of packages in parallel, using only the new packages
with the `oauth2` package.

	import (
		"golang.org/x/net/context"
		"golang.org/x/oauth2"
		"golang.org/x/oauth2/google"
		newappengine "google.golang.org/appengine"
		newurlfetch "google.golang.org/appengine/urlfetch"

		"appengine"
	)

	func handler(w http.ResponseWriter, r *http.Request) {
		var c appengine.Context = appengine.NewContext(r)
		c.Infof("Logging a message with the old package")

		var ctx context.Context = newappengine.NewContext(r)
		client := &http.Client{
			Transport: &oauth2.Transport{
				Source: google.AppEngineTokenSource(ctx, "scope"),
				Base:   &newurlfetch.Transport{Context: ctx},
			},
		}
		client.Get("...")
	}

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
# Go support for Protocol Buffers

Google's data interchange format.
Copyright 2010 The Go Authors.
https://github.com/golang/protobuf

This package and the code it generates requires at least Go 1.4.

This software implements Go bindings for protocol buffers.  For
information about protocol buffers themselves, see
	https://developers.google.com/protocol-buffers/

## Installation ##

To use this software, you must:
- Install the standard C++ implementation of protocol buffers from
	https://developers.google.com/protocol-buffers/
- Of course, install the Go compiler and tools from
	https://golang.org/
  See
	https://golang.org/doc/install
  for details or, if you are using gccgo, follow the instructions at
	https://golang.org/doc/install/gccgo
- Grab the code from the repository and install the proto package.
  The simplest way is to run `go get -u github.com/golang/protobuf/{proto,protoc-gen-go}`.
  The compiler plugin, protoc-gen-go, will be installed in $GOBIN,
  defaulting to $GOPATH/bin.  It must be in your $PATH for the protocol
  compiler, protoc, to find it.

This software has two parts: a 'protocol compiler plugin' that
generates Go source files that, once compiled, can access and manage
protocol buffers; and a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers.

There is support for gRPC in Go using protocol buffers.
See the note at the bottom of this file for details.

There are no insertion points in the plugin.


## Using protocol buffers with Go ##

Once the software is installed, there are two steps to using it.
First you must compile the protocol buffer definitions and then import
them, with the support library, into your program.

To compile the protocol buffer definition, run protoc with the --go_out
parameter set to the directory you want to output the Go code to.

	protoc --go_out=. *.proto

The generated files will be suffixed .pb.go.  See the Test code below
for an example using such a file.


The package comment for the proto library contains text describing
the interface provided in Go for protocol buffers. Here is an edited
version.

==========

The proto package converts data structures to and from the
wire format of protocol buffers.  It works in concert with the
Go source code generated for .proto files by the protocol compiler.

A summary of the properties of the protocol buffer interface
for a protocol buffer variable v:

  - Names are turned from camel_case to CamelCase for export.
  - There are no methods on v to set fields; just treat
  	them as structure fields.
  - There are getters that return a field's value if set,
	and return the field's default value if unset.
	The getters work even if the receiver is a nil message.
  - The zero value for a struct is its correct initialization state.
	All desired fields must be set before marshaling.
  - A Reset() method will restore a protobuf struct to its zero state.
  - Non-repeated fields are pointers to the values; nil means unset.
	That is, optional or required field int32 f becomes F *int32.
  - Repeated fields are slices.
  - Helper functions are available to aid the setting of fields.
	Helpers for getting values are superseded by the
	GetFoo methods and their use is deprecated.
		msg.Foo = proto.String("hello") // set field
  - Constants are defined to hold the default values of all fields that
	have them.  They have the form Default_StructName_FieldName.
	Because the getter methods handle defaulted values,
	direct use of these constants should be rare.
  - Enums are given type names and maps from names to values.
	Enum values are prefixed with the enum's type name. Enum types have
	a String method, and a Enum method to assist in message construction.
  - Nested groups and enums have type names prefixed with the name of
  	the surrounding message type.
  - Extensions are given descriptor names that start with E_,
	followed by an underscore-delimited list of the nested messages
	that contain it (if any) followed by the CamelCased name of the
	extension field itself.  HasExtension, ClearExtension, GetExtension
	and SetExtension are functions for manipulating extensions.
  - Oneof field sets are given a single field in their message,
	with distinguished wrapper types for each possible field value.
  - Marshal and Unmarshal are functions to encode and decode the wire format.

When the .proto file specifies `syntax="proto3"`, there are some differences:

  - Non-repeated fields of non-message type are values instead of pointers.
  - Getters are only generated for message and oneof fields.
  - Enum types do not get an Enum method.

Consider file test.proto, containing

```proto
	package example;
	
	enum FOO { X = 17; };
	
	message Test {
	  required string label = 1;
	  optional int32 type = 2 [default=77];
	  repeated int64 reps = 3;
	  optional group OptionalGroup = 4 {
	    required string RequiredField = 5;
	  }
	}
```

To create and play with a Test object from the example package,

```go
	package main

	import (
		"log"

		"github.com/golang/protobuf/proto"
		"path/to/example"
	)

	func main() {
		test := &example.Test {
			Label: proto.String("hello"),
			Type:  proto.Int32(17),
			Reps:  []int64{1, 2, 3},
			Optionalgroup: &example.Test_OptionalGroup {
				RequiredField: proto.String("good bye"),
			},
		}
		data, err := proto.Marshal(test)
		if err != nil {
			log.Fatal("marshaling error: ", err)
		}
		newTest := &example.Test{}
		err = proto.Unmarshal(data, newTest)
		if err != nil {
			log.Fatal("unmarshaling error: ", err)
		}
		// Now test and newTest contain the same data.
		if test.GetLabel() != newTest.GetLabel() {
			log.Fatalf("data mismatch %q != %q", test.GetLabel(), newTest.GetLabel())
		}
		// etc.
	}
```

## Parameters ##

To pass extra parameters to the plugin, use a comma-separated
parameter list separated from the output directory by a colon:


	protoc --go_out=plugins=grpc,import_path=mypackage:. *.proto


- `import_prefix=xxx` - a prefix that is added onto the beginning of
  all imports. Useful for things like generating protos in a
  subdirectory, or regenerating vendored protobufs in-place.
- `import_path=foo/bar` - used as the package if no input files
  declare `go_package`. If it contains slashes, everything up to the
  rightmost slash is ignored.
- `plugins=plugin1+plugin2` - specifies the list of sub-plugins to
  load. The only plugin in this repo is `grpc`.
- `Mfoo/bar.proto=quux/shme` - declares that foo/bar.proto is
  associated with Go package quux/shme.  This is subject to the
  import_prefix parameter.

## gRPC Support ##

If a proto file specifies RPC services, protoc-gen-go can be instructed to
generate code compatible with gRPC (http://www.grpc.io/). To do this, pass
the `plugins` parameter to protoc-gen-go; the usual way is to insert it into
the --go_out argument to protoc:

	protoc --go_out=plugins=grpc:. *.proto

## Compatibility ##

The library and the generated code are expected to be stable over time.
However, we reserve the right to make breaking changes without notice for the
following reasons:

- Security. A security issue in the specification or implementation may come to
  light whose resolution requires breaking compatibility. We reserve the right
  to address such security issues.
- Unspecified behavior.  There are some aspects of the Protocol Buffers
  specification that are undefined.  Programs that depend on such unspecified
  behavior may break in future releases.
- Specification errors or changes. If it becomes necessary to address an
  inconsistency, incompleteness, or change in the Protocol Buffers
  specification, resolving the issue could affect the meaning or legality of
  existing programs.  We reserve the right to address such issues, including
  updating the implementations.
- Bugs.  If the library has a bug that violates the specification, a program
  that depends on the buggy behavior may break if the bug is fixed.  We reserve
  the right to fix such bugs.
- Adding methods or fields to generated structs.  These may conflict with field
  names that already exist in a schema, causing applications to break.  When the
  code generator encounters a field in the schema that would collide with a
  generated field or method name, the code generator will append an underscore
  to the generated field or method name.
- Adding, removing, or changing methods or fields in generated structs that
  start with `XXX`.  These parts of the generated code are exported out of
  necessity, but should not be considered part of the public API.
- Adding, removing, or changing unexported symbols in generated code.

Any breaking changes outside of these will be announced 6 months in advance to
protobuf@googlegroups.com.

You should, whenever possible, use generated code created by the `protoc-gen-go`
tool built at the same commit as the `proto` package.  The `proto` package
declares package-level constants in the form `ProtoPackageIsVersionX`.
Application code and generated code may depend on one of these constants to
ensure that compilation will fail if the available version of the proto library
is too old.  Whenever we make a change to the generated code that requires newer
library support, in the same commit we will increment the version number of the
generated code and declare a new package-level constant whose name incorporates
the latest version number.  Removing a compatibility constant is considered a
breaking change and would be subject to the announcement policy stated above.

The `protoc-gen-go/generator` package exposes a plugin interface,
which is used by the gRPC code generation. This interface is not
supported and is subject to incompatible changes without notice.
# Google Cloud for Go

[![Build Status](https://travis-ci.org/GoogleCloudPlatform/google-cloud-go.svg?branch=master)](https://travis-ci.org/GoogleCloudPlatform/google-cloud-go)
[![GoDoc](https://godoc.org/cloud.google.com/go?status.svg)](https://godoc.org/cloud.google.com/go)

``` go
import "cloud.google.com/go"
```

Go packages for Google Cloud Platform services.

**NOTE:** These packages are under development, and may occasionally make
backwards-incompatible changes.

**NOTE:** Github repo is a mirror of [https://code.googlesource.com/gocloud](https://code.googlesource.com/gocloud).

## News

_September 8, 2016_

* New clients for some of Google's Machine Learning APIs: Vision, Speech, and
Natural Language.

* Preview version of a new [Stackdriver Logging][cloud-logging] client in
[`cloud.google.com/go/preview/logging`](https://godoc.org/cloud.google.com/go/preview/logging).
This client uses gRPC as its transport layer, and supports log reading, sinks
and metrics. It will replace the current client at `cloud.google.com/go/logging` shortly.

## Supported APIs

Google API                     | Status       | Package
-------------------------------|--------------|-----------------------------------------------------------
[Datastore][cloud-datastore]   | beta         | [`cloud.google.com/go/datastore`][cloud-datastore-ref]
[Storage][cloud-storage]       | beta         | [`cloud.google.com/go/storage`][cloud-storage-ref]
[Pub/Sub][cloud-pubsub]        | experimental | [`cloud.google.com/go/pubsub`][cloud-pubsub-ref]
[Bigtable][cloud-bigtable]     | beta         | [`cloud.google.com/go/bigtable`][cloud-bigtable-ref]
[BigQuery][cloud-bigquery]     | experimental | [`cloud.google.com/go/bigquery`][cloud-bigquery-ref]
[Logging][cloud-logging]       | experimental | [`cloud.google.com/go/logging`][cloud-logging-ref]
[Vision][cloud-vision]         | experimental | [`cloud.google.com/go/vision`][cloud-vision-ref]
[Language][cloud-language]     | experimental | [`cloud.google.com/go/language/apiv1beta1`][cloud-language-ref]
[Speech][cloud-speech]         | experimental | [`cloud.google.com/go/speech/apiv1beta`][cloud-speech-ref]


> **Experimental status**: the API is still being actively developed. As a
> result, it might change in backward-incompatible ways and is not recommended
> for production use.
>
> **Beta status**: the API is largely complete, but still has outstanding
> features and bugs to be addressed. There may be minor backwards-incompatible
> changes where necessary.
>
> **Stable status**: the API is mature and ready for production use. We will
> continue addressing bugs and feature requests.

Documentation and examples are available at
https://godoc.org/cloud.google.com/go

Visit or join the
[google-api-go-announce group](https://groups.google.com/forum/#!forum/google-api-go-announce)
for updates on these packages.

## Go Versions Supported

We support the two most recent major versions of Go. If Google App Engine uses
an older version, we support that as well. You can see which versions are
currently supported by looking at the lines following `go:` in
[`.travis.yml`](.travis.yml).

## Authorization

By default, each API will use [Google Application Default Credentials][default-creds]
for authorization credentials used in calling the API endpoints. This will allow your
application to run in many environments without requiring explicit configuration.

Manually-configured authorization can be achieved using the
[`golang.org/x/oauth2`](https://godoc.org/golang.org/x/oauth2) package to
create an `oauth2.TokenSource`. This token source can be passed to the `NewClient`
function for the relevant API using a
[`option.WithTokenSource`](https://godoc.org/google.golang.org/api/option#WithTokenSource)
option.

## Google Cloud Datastore [![GoDoc](https://godoc.org/cloud.google.com/go/datastore?status.svg)](https://godoc.org/cloud.google.com/go/datastore)

[Google Cloud Datastore][cloud-datastore] ([docs][cloud-datastore-docs]) is a fully-
managed, schemaless database for storing non-relational data. Cloud Datastore
automatically scales with your users and supports ACID transactions, high availability
of reads and writes, strong consistency for reads and ancestor queries, and eventual
consistency for all other queries.

Follow the [activation instructions][cloud-datastore-activation] to use the Google
Cloud Datastore API with your project.

First create a `datastore.Client` to use throughout your application:

```go
client, err := datastore.NewClient(ctx, "my-project-id")
if err != nil {
	log.Fatalln(err)
}
```

Then use that client to interact with the API:

```go
type Post struct {
	Title       string
	Body        string `datastore:",noindex"`
	PublishedAt time.Time
}
keys := []*datastore.Key{
	datastore.NewKey(ctx, "Post", "post1", 0, nil),
	datastore.NewKey(ctx, "Post", "post2", 0, nil),
}
posts := []*Post{
	{Title: "Post 1", Body: "...", PublishedAt: time.Now()},
	{Title: "Post 2", Body: "...", PublishedAt: time.Now()},
}
if _, err := client.PutMulti(ctx, keys, posts); err != nil {
	log.Fatal(err)
}
```

## Google Cloud Storage [![GoDoc](https://godoc.org/cloud.google.com/go/storage?status.svg)](https://godoc.org/cloud.google.com/go/storage)

[Google Cloud Storage][cloud-storage] ([docs][cloud-storage-docs]) allows you to store
data on Google infrastructure with very high reliability, performance and availability,
and can be used to distribute large data objects to users via direct download.

https://godoc.org/cloud.google.com/go/storage

First create a `storage.Client` to use throughout your application:

```go
client, err := storage.NewClient(ctx)
if err != nil {
	log.Fatal(err)
}
```

```go
// Read the object1 from bucket.
rc, err := client.Bucket("bucket").Object("object1").NewReader(ctx)
if err != nil {
	log.Fatal(err)
}
defer rc.Close()
body, err := ioutil.ReadAll(rc)
if err != nil {
	log.Fatal(err)
}
```

## Google Cloud Pub/Sub [![GoDoc](https://godoc.org/cloud.google.com/go/pubsub?status.svg)](https://godoc.org/cloud.google.com/go/pubsub)

[Google Cloud Pub/Sub][cloud-pubsub] ([docs][cloud-pubsub-docs]) allows you to connect
your services with reliable, many-to-many, asynchronous messaging hosted on Google's
infrastructure. Cloud Pub/Sub automatically scales as you need it and provides a foundation
for building your own robust, global services.

First create a `pubsub.Client` to use throughout your application:

```go
client, err := pubsub.NewClient(ctx, "project-id")
if err != nil {
	log.Fatal(err)
}
```

```go
// Publish "hello world" on topic1.
topic := client.Topic("topic1")
msgIDs, err := topic.Publish(ctx, &pubsub.Message{
	Data: []byte("hello world"),
})
if err != nil {
	log.Fatal(err)
}

// Create an iterator to pull messages via subscription1.
it, err := client.Subscription("subscription1").Pull(ctx)
if err != nil {
	log.Println(err)
}
defer it.Stop()

// Consume N messages from the iterator.
for i := 0; i < N; i++ {
	msg, err := it.Next()
	if err == pubsub.Done {
		break
	}
	if err != nil {
		log.Fatalf("Failed to retrieve message: %v", err)
	}

	fmt.Printf("Message %d: %s\n", i, msg.Data)
	msg.Done(true) // Acknowledge that we've consumed the message.
}
```

## Contributing

Contributions are welcome. Please, see the
[CONTRIBUTING](https://github.com/GoogleCloudPlatform/google-cloud-go/blob/master/CONTRIBUTING.md)
document for details. We're using Gerrit for our code reviews. Please don't open pull
requests against this repo, new pull requests will be automatically closed.

Please note that this project is released with a Contributor Code of Conduct.
By participating in this project you agree to abide by its terms.
See [Contributor Code of Conduct](https://github.com/GoogleCloudPlatform/google-cloud-go/blob/master/CONTRIBUTING.md#contributor-code-of-conduct)
for more information.

[cloud-datastore]: https://cloud.google.com/datastore/
[cloud-datastore-ref]: https://godoc.org/cloud.google.com/go/datastore
[cloud-datastore-docs]: https://cloud.google.com/datastore/docs
[cloud-datastore-activation]: https://cloud.google.com/datastore/docs/activate

[cloud-pubsub]: https://cloud.google.com/pubsub/
[cloud-pubsub-ref]: https://godoc.org/cloud.google.com/go/pubsub
[cloud-pubsub-docs]: https://cloud.google.com/pubsub/docs

[cloud-storage]: https://cloud.google.com/storage/
[cloud-storage-ref]: https://godoc.org/cloud.google.com/go/storage
[cloud-storage-docs]: https://cloud.google.com/storage/docs/overview
[cloud-storage-create-bucket]: https://cloud.google.com/storage/docs/cloud-console#_creatingbuckets

[cloud-bigtable]: https://cloud.google.com/bigtable/
[cloud-bigtable-ref]: https://godoc.org/cloud.google.com/go/bigtable

[cloud-bigquery]: https://cloud.google.com/bigquery/
[cloud-bigquery-ref]: https://godoc.org/cloud.google.com/go/bigquery

[cloud-logging]: https://cloud.google.com/logging/
[cloud-logging-ref]: https://godoc.org/cloud.google.com/go/logging

[cloud-vision]: https://cloud.google.com/vision/
[cloud-vision-ref]: https://godoc.org/cloud.google.com/go/vision

[cloud-language]: https://cloud.google.com/natural-language
[cloud-language-ref]: https://godoc.org/cloud.google.com/go/language/apiv1beta1

[cloud-speech]: https://cloud.google.com/speech
[cloud-speech-ref]: https://godoc.org/cloud.google.com/go/speech/apiv1beta1

[default-creds]: https://developers.google.com/identity/protocols/application-default-credentials
Auto-generated pubsub v1 clients
=================================

This package includes auto-generated clients for the pubsub v1 API.

Use the handwritten logging client (in the parent directory,
cloud.google.com/go/pubsub) in preference to this.

This code is EXPERIMENTAL and subject to CHANGE AT ANY TIME.


# User Counter
# (Cloud Bigtable on Managed VMs using Go)

This app counts how often each user visits. The app uses Cloud Bigtable to store the visit counts for each user.

## Prerequisites

1. Set up Cloud Console.
  1. Go to the [Cloud Console](https://cloud.google.com/console) and create or select your project.
     You will need the project ID later.
  1. Go to **Settings > Project Billing Settings** and enable billing.
  1. Select **APIs & Auth > APIs**.
  1. Enable the **Cloud Bigtable API** and the **Cloud Bigtable Admin API**.
  (You may need to search for the API).
1. Set up gcloud.
  1. `gcloud components update`
  1. `gcloud auth login`
  1. `gcloud config set project PROJECT_ID`
1. Download App Engine SDK for Go.
  1. `go get -u google.golang.org/appengine/...`
1. In main.go, change the `project` and `instance` constants.

## Running locally

1. From the sample project folder, `dev_appserver.py app.yaml`.

## Deploying on Google App Engine flexible environment

Follow the [deployment instructions](https://cloud.google.com/appengine/docs/flexible/go/testing-and-deploying-your-app).
# Cloud Bigtable Hello World in Go

This is a simple application that demonstrates using the [Google Cloud APIs Go
Client Library](https://github.com/GoogleCloudPlatform/google-cloud-go) to connect
to and interact with Cloud Bigtable.

## Prerequisites

1. Set up Cloud Console.
  1. Go to the [Cloud Console](https://cloud.google.com/console) and create or select your project.
     You will need the project ID later.
  1. Go to **Settings > Project Billing Settings** and enable billing.
  1. Select **APIs & Auth > APIs**.
  1. Enable the **Cloud Bigtable API** and the **Cloud Bigtable Admin API**.
  (You may need to search for the API).
1. Set up gcloud.
  1. `gcloud components update`
  1. `gcloud auth login`
  1. `gcloud config set project PROJECT_ID`
1. Provision a Cloud Bigtable instance
  1. Follow the instructions in the [user
documentation](https://cloud.google.com/bigtable/docs/creating-instance) to
create a Google Cloud Platform project and Cloud Bigtable instance if necessary.
  1. You'll need to reference your project id and instance id to run the application.

## Running

1. From the hello_world example folder, `go run main.go -project PROJECT_ID -instance INSTANCE_ID`, substituting your project id and instance id.

## Cleaning up

To avoid incurring extra charges to your Google Cloud Platform account, remove
the resources created for this sample.

1.  Go to the Clusters page in the [Cloud
    Console](https://console.cloud.google.com).

    [Go to the Clusters page](https://console.cloud.google.com/project/_/bigtable/clusters)

1.  Click the cluster name.

1.  Click **Delete**.

    ![Delete](https://cloud.google.com/bigtable/img/delete-quickstart-cluster.png)

1. Type the cluster ID, then click **Delete** to delete the cluster.
The following files were copied from https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/data:
cat.jpg
face.jpg
faulkner.jpg
mountain.jpg
no-text.jpg

eiffel-tower.jpg is from
https://commons.wikimedia.org/wiki/File:Tour_Eiffel_Wikimedia_Commons_(cropped).jpg.

google.png is from the Google home page:
https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png.




Auto-generated logging v2 clients
=================================

This package includes auto-generated clients for the logging v2 API.

Use the handwritten logging client (in the parent directory,
cloud.google.com/go/logging) in preference to this.

This code is EXPERIMENTAL and subject to CHANGE AT ANY TIME.


# Google APIs Client Library for Go

## Status
[![Build Status](https://travis-ci.org/google/google-api-go-client.png)](https://travis-ci.org/google/google-api-go-client)

These are auto-generated Go libraries from the Google Discovery Service's JSON description files of the available "new style" Google APIs.

Due to the auto-generated nature of this collection of libraries, complete APIs or specific versions can appear or go away without notice.
As a result, you should always locally vendor any API(s) that your code relies upon.

Announcement email:

* http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Getting started documentation:

* https://github.com/google/google-api-go-client/blob/master/GettingStarted.md

In summary:

```
$ go get google.golang.org/api/storage/v1
$ go get google.golang.org/api/tasks/v1
$ go get google.golang.org/api/moderator/v1
... etc ...
```

For docs, see e.g.:

* https://godoc.org/google.golang.org/api/storage/v1

The package of a given import is the second-to-last component, before the version number.

For examples, see:

* https://github.com/google/google-api-go-client/tree/master/examples

For support, use the golang-nuts@ mailing list:

* https://groups.google.com/group/golang-nuts

## Application Default Credentials Example

Application Default Credentials provide a simplified way to obtain credentials
for authenticating with Google APIs.

The Application Default Credentials authenticate as the application itself,
which make them great for working with Google Cloud APIs like Storage or
Datastore. They are the recommended form of authentication when building
applications that run on Google Compute Engine or Google App Engine.

Default credentials are provided by the `golang.org/x/oauth2/google` package. To use them, add the following import:

```
import "golang.org/x/oauth2/google"
```

Some credentials types require you to specify scopes, and service entry points may not inject them. If you encounter this situation you may need to specify scopes as follows:

```
import (
        "golang.org/x/net/context"
        "golang.org/x/oauth2/google"
        "google.golang.org/api/compute/v1"
)

func main() {
        // Use oauth2.NoContext if there isn't a good context to pass in.
        ctx := context.Background()

        client, err := google.DefaultClient(ctx, compute.ComputeScope)
        if err != nil {
                //...
        }
        computeService, err := compute.New(client)
        if err != nil {
                //...
        }
}
```

If you need a `oauth2.TokenSource`, use the `DefaultTokenSource` function:

```
ts, err := google.DefaultTokenSource(ctx, scope1, scope2, ...)
if err != nil {
        //...
}
client := oauth2.NewClient(ctx, ts)
```

See also: [golang.org/x/oauth2/google](https://godoc.org/golang.org/x/oauth2/google) package documentation.
# Go App Engine packages

[![Build Status](https://travis-ci.org/golang/appengine.svg)](https://travis-ci.org/golang/appengine)

This repository supports the Go runtime on App Engine,
including both the standard App Engine and the
"App Engine flexible environment" (formerly known as "Managed VMs").
It provides APIs for interacting with App Engine services.
Its canonical import path is `google.golang.org/appengine`.

See https://cloud.google.com/appengine/docs/go/
for more information.

File issue reports and feature requests on the [Google App Engine issue
tracker](https://code.google.com/p/googleappengine/issues/entry?template=Go%20defect).

## Directory structure
The top level directory of this repository is the `appengine` package. It
contains the
basic APIs (e.g. `appengine.NewContext`) that apply across APIs. Specific API
packages are in subdirectories (e.g. `datastore`).

There is an `internal` subdirectory that contains service protocol buffers,
plus packages required for connectivity to make API calls. App Engine apps
should not directly import any package under `internal`.

## Updating a Go App Engine app

This section describes how to update an older Go App Engine app to use
these packages. A provided tool, `aefix`, can help automate steps 2 and 3
(run `go get google.golang.org/appengine/cmd/aefix` to install it), but
read the details below since `aefix` can't perform all the changes.

### 1. Update YAML files (App Engine flexible environment / Managed VMs only)

The `app.yaml` file (and YAML files for modules) should have these new lines added:
```
vm: true
```
See https://cloud.google.com/appengine/docs/go/modules/#Go_Instance_scaling_and_class for details.

### 2. Update import paths

The import paths for App Engine packages are now fully qualified, based at `google.golang.org/appengine`.
You will need to update your code to use import paths starting with that; for instance,
code importing `appengine/datastore` will now need to import `google.golang.org/appengine/datastore`.

### 3. Update code using deprecated, removed or modified APIs

Most App Engine services are available with exactly the same API.
A few APIs were cleaned up, and some are not available yet.
This list summarises the differences:

* `appengine.Context` has been replaced with the `Context` type from `golang.org/x/net/context`.
* Logging methods that were on `appengine.Context` are now functions in `google.golang.org/appengine/log`.
* `appengine.Timeout` has been removed. Use `context.WithTimeout` instead.
* `appengine.Datacenter` now takes a `context.Context` argument.
* `datastore.PropertyLoadSaver` has been simplified to use slices in place of channels.
* `delay.Call` now returns an error.
* `search.FieldLoadSaver` now handles document metadata.
* `urlfetch.Transport` no longer has a Deadline field; set a deadline on the
  `context.Context` instead.
* `aetest` no longer declares its own Context type, and uses the standard one instead.
* `taskqueue.QueueStats` no longer takes a maxTasks argument. That argument has been
  deprecated and unused for a long time.
* `appengine.BackendHostname` and `appengine.BackendInstance` were for the deprecated backends feature.
  Use `appengine.ModuleHostname`and `appengine.ModuleName` instead.
* Most of `appengine/file` and parts of `appengine/blobstore` are deprecated.
  Use [Google Cloud Storage](https://godoc.org/google.golang.org/cloud/storage) instead.
* `appengine/socket` is not required on App Engine flexible environment / Managed VMs.
  Use the standard `net` package instead.
