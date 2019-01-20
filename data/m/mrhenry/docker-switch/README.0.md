# Codec

High Performance, Feature-Rich Idiomatic Go codec/encoding library for
binc, msgpack, cbor, json.

Supported Serialization formats are:

  - msgpack: https://github.com/msgpack/msgpack
  - binc:    http://github.com/ugorji/binc
  - cbor:    http://cbor.io http://tools.ietf.org/html/rfc7049
  - json:    http://json.org http://tools.ietf.org/html/rfc7159
  - simple: 

To install:

    go get github.com/ugorji/go/codec

This package understands the `unsafe` tag, to allow using unsafe semantics:

  - When decoding into a struct, you need to read the field name as a string 
    so you can find the struct field it is mapped to.
    Using `unsafe` will bypass the allocation and copying overhead of `[]byte->string` conversion.

To use it, you must pass the `unsafe` tag during install:

```
go install -tags=unsafe github.com/ugorji/go/codec 
```

Online documentation: http://godoc.org/github.com/ugorji/go/codec  
Detailed Usage/How-to Primer: http://ugorji.net/blog/go-codec-primer

The idiomatic Go support is as seen in other encoding packages in
the standard library (ie json, xml, gob, etc).

Rich Feature Set includes:

  - Simple but extremely powerful and feature-rich API
  - Very High Performance.
    Our extensive benchmarks show us outperforming Gob, Json, Bson, etc by 2-4X.
  - Multiple conversions:
    Package coerces types where appropriate 
    e.g. decode an int in the stream into a float, etc.
  - Corner Cases: 
    Overflows, nil maps/slices, nil values in streams are handled correctly
  - Standard field renaming via tags
  - Support for omitting empty fields during an encoding
  - Encoding from any value and decoding into pointer to any value
    (struct, slice, map, primitives, pointers, interface{}, etc)
  - Extensions to support efficient encoding/decoding of any named types
  - Support encoding.(Binary|Text)(M|Unm)arshaler interfaces
  - Decoding without a schema (into a interface{}).
    Includes Options to configure what specific map or slice type to use
    when decoding an encoded list or map into a nil interface{}
  - Encode a struct as an array, and decode struct from an array in the data stream
  - Comprehensive support for anonymous fields
  - Fast (no-reflection) encoding/decoding of common maps and slices
  - Code-generation for faster performance.
  - Support binary (e.g. messagepack, cbor) and text (e.g. json) formats
  - Support indefinite-length formats to enable true streaming 
    (for formats which support it e.g. json, cbor)
  - Support canonical encoding, where a value is ALWAYS encoded as same sequence of bytes.
    This mostly applies to maps, where iteration order is non-deterministic.
  - NIL in data stream decoded as zero value
  - Never silently skip data when decoding.
    User decides whether to return an error or silently skip data when keys or indexes
    in the data stream do not map to fields in the struct.
  - Encode/Decode from/to chan types (for iterative streaming support)
  - Drop-in replacement for encoding/json. `json:` key in struct tag supported.
  - Provides a RPC Server and Client Codec for net/rpc communication protocol.
  - Handle unique idiosynchracies of codecs e.g. 
    - For messagepack, configure how ambiguities in handling raw bytes are resolved 
    - For messagepack, provide rpc server/client codec to support
      msgpack-rpc protocol defined at:
      https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md

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
      ch codec.CborHandle
    )

    mh.MapType = reflect.TypeOf(map[string]interface{}(nil))

    // configure extensions
    // e.g. for msgpack, define functions and enable Time support for tag 1
    // mh.SetExt(reflect.TypeOf(time.Time{}), 1, myExt)

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

# etcd/client

etcd/client is the Go client library for etcd.

[![GoDoc](https://godoc.org/github.com/coreos/etcd/client?status.png)](https://godoc.org/github.com/coreos/etcd/client)

etcd uses `cmd/vendor` directory to store external dependencies, which are
to be compiled into etcd release binaries. `client` can be imported without
vendoring. For full compatibility, it is recommended to vendor builds using
etcd's vendored packages, using tools like godep, as in
[vendor directories](https://golang.org/cmd/go/#hdr-Vendor_Directories).
For more detail, please read [Go vendor design](https://golang.org/s/go15vendor).

## Install

```bash
go get github.com/coreos/etcd/client
```

## Usage

```go
package main

import (
	"log"
	"time"

	"golang.org/x/net/context"
	"github.com/coreos/etcd/client"
)

func main() {
	cfg := client.Config{
		Endpoints:               []string{"http://127.0.0.1:2379"},
		Transport:               client.DefaultTransport,
		// set timeout per request to fail fast when the target endpoint is unavailable
		HeaderTimeoutPerRequest: time.Second,
	}
	c, err := client.New(cfg)
	if err != nil {
		log.Fatal(err)
	}
	kapi := client.NewKeysAPI(c)
	// set "/foo" key with "bar" value
	log.Print("Setting '/foo' key with 'bar' value")
	resp, err := kapi.Set(context.Background(), "/foo", "bar", nil)
	if err != nil {
		log.Fatal(err)
	} else {
		// print common key info
		log.Printf("Set is done. Metadata is %q\n", resp)
	}
	// get "/foo" key's value
	log.Print("Getting '/foo' key value")
	resp, err = kapi.Get(context.Background(), "/foo", nil)
	if err != nil {
		log.Fatal(err)
	} else {
		// print common key info
		log.Printf("Get is done. Metadata is %q\n", resp)
		// print value
		log.Printf("%q key has %q value\n", resp.Node.Key, resp.Node.Value)
	}
}
```

## Error Handling

etcd client might return three types of errors.

- context error

Each API call has its first parameter as `context`. A context can be canceled or have an attached deadline. If the context is canceled or reaches its deadline, the responding context error will be returned no matter what internal errors the API call has already encountered.

- cluster error

Each API call tries to send request to the cluster endpoints one by one until it successfully gets a response. If a requests to an endpoint fails, due to exceeding per request timeout or connection issues, the error will be added into a list of errors. If all possible endpoints fail, a cluster error that includes all encountered errors will be returned.

- response error

If the response gets from the cluster is invalid, a plain string error will be returned. For example, it might be a invalid JSON error.

Here is the example code to handle client errors:

```go
cfg := client.Config{Endpoints: []string{"http://etcd1:2379","http://etcd2:2379","http://etcd3:2379"}}
c, err := client.New(cfg)
if err != nil {
	log.Fatal(err)
}

kapi := client.NewKeysAPI(c)
resp, err := kapi.Set(ctx, "test", "bar", nil)
if err != nil {
	if err == context.Canceled {
		// ctx is canceled by another routine
	} else if err == context.DeadlineExceeded {
		// ctx is attached with a deadline and it exceeded
	} else if cerr, ok := err.(*client.ClusterError); ok {
		// process (cerr.Errors)
	} else {
		// bad cluster endpoints, which are not etcd servers
	}
}
```


## Caveat

1. etcd/client prefers to use the same endpoint as long as the endpoint continues to work well. This saves socket resources, and improves efficiency for both client and server side. This preference doesn't remove consistency from the data consumed by the client because data replicated to each etcd member has already passed through the consensus process.

2. etcd/client does round-robin rotation on other available endpoints if the preferred endpoint isn't functioning properly. For example, if the member that etcd/client connects to is hard killed, etcd/client will fail on the first attempt with the killed member, and succeed on the second attempt with another member. If it fails to talk to all available endpoints, it will return all errors happened.

3. Default etcd/client cannot handle the case that the remote server is SIGSTOPed now. TCP keepalive mechanism doesn't help in this scenario because operating system may still send TCP keep-alive packets. Over time we'd like to improve this functionality, but solving this issue isn't high priority because a real-life case in which a server is stopped, but the connection is kept alive, hasn't been brought to our attention.

4. etcd/client cannot detect whether the member in use is healthy when doing read requests. If the member is isolated from the cluster, etcd/client may retrieve outdated data. As a workaround, users could monitor experimental /health endpoint for member healthy information. We are improving it at [#3265](https://github.com/coreos/etcd/issues/3265).
# go-dockerclient

[![Travis](https://img.shields.io/travis/fsouza/go-dockerclient/master.svg?style=flat-square)](https://travis-ci.org/fsouza/go-dockerclient)
[![GoDoc](https://img.shields.io/badge/api-Godoc-blue.svg?style=flat-square)](https://godoc.org/github.com/fsouza/go-dockerclient)

This package presents a client for the Docker remote API. It also provides
support for the extensions in the [Swarm API](https://docs.docker.com/swarm/swarm-api/).
It currently supports the Docker API up to version 1.23.

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
