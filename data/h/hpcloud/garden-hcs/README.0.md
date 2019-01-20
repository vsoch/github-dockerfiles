lager
=====

**Note**: This repository should be imported as `code.cloudfoundry.org/lager`.

Lager is a logging library for go.

## Usage

Instantiate a logger with the name of your component.

```go
import (
  "code.cloudfoundry.org/lager"
)

logger := lager.NewLogger("my-app")
```

### Sinks

Lager can write logs to a variety of destinations. You can specify the destinations
using Lager sinks:

To write to an arbitrary `Writer` object:

```go
logger.RegisterSink(lager.NewWriterSink(myWriter, lager.INFO))
```

### Emitting logs

Lager supports the usual level-based logging, with an optional argument for arbitrary key-value data.

```go
logger.Info("doing-stuff", lager.Data{
  "informative": true,
})
```

output:
```json
{ "source": "my-app", "message": "doing-stuff", "data": { "informative": true }, "timestamp": 1232345, "log_level": 1 }
```

Error messages also take an `Error` object:

```go
logger.Error("failed-to-do-stuff", errors.New("Something went wrong"))
```

output:
```json
{ "source": "my-app", "message": "failed-to-do-stuff", "data": { "error": "Something went wrong" }, "timestamp": 1232345, "log_level": 1 }
```

### Sessions

You can avoid repetition of contextual data using 'Sessions':

```go

contextualLogger := logger.Session("my-task", lager.Data{
  "request-id": 5,
})

contextualLogger.Info("my-action")
```

output:

```json
{ "source": "my-app", "message": "my-task.my-action", "data": { "request-id": 5 }, "timestamp": 1232345, "log_level": 1 }
```

## License

Lager is [Apache 2.0](https://github.com/cloudfoundry/lager/blob/master/LICENSE) licensed.
cflager
========

**Note**: This repository should be imported as `code.cloudfoundry.org/cflager`.

A thin wrapper around [github.com/cloudfoundry/lager](https://github.com/cloudfoundry/lager) for easy use in CF components.

This library provides a flag called `logLevel`. By importing this library, various CF components can share the same name, description, and default value ("info") for this flag.

The logger returned by `cflager.New()` will write all logs to `os.Stdout`.

To use, simply import this package in your `main.go` and call `cflager.New(COMPONENT_NAME)` to get a logger.

For example:

```golang
package main

import (
    "flag"
    "fmt"

    "github.com/cloudfoundry/cflager"
    "github.com/cloudfoundry/lager"
)

func main() {
    cflager.AddFlags(flag.CommandLine)

    flag.Parse()

    logger, reconfigurableSink := cflager.New("my-component")
    logger.Info("starting")

    // Display the current minimum log level
    fmt.Printf("Current log level is ")
    switch reconfigurableSink.GetMinLevel() {
    case lager.DEBUG:
        fmt.Println("debug")
    case lager.INFO:
        fmt.Println("info")
    case lager.ERROR:
        fmt.Println("error")
    case lager.FATAL:
        fmt.Println("fatal")
    }

    // Change the minimum log level dynamically
    reconfigurableSink.SetMinLevel(lager.ERROR)
    logger.Debug("will-not-log")
}
```

Running the program above as `go run main.go --logLevel debug` will generate the following output:

```
{"timestamp":"1464388983.540486336","source":"my-component","message":"my-component.starting","log_level":1,"data":{}}
Current log level is debug
```
```
                                                 ,-.
                                                  ) \
                                              .--'   |
                                             /       /
                                             |_______|
                                            (  O   O  )
                                             {'-(_)-'}
                                           .-{   ^   }-.
                                          /   '.___.'   \
                                         /  |    o    |  \
                                         |__|    o    |__|
                                         (((\_________/)))
                                             \___|___/
                                        jgs.--' | | '--.
                                           \__._| |_.__/
```

**Note**: This repository should be imported as `code.cloudfoundry.org/garden`.

A rich golang client and server for container creation and management with pluggable backends for [linux](https://github.com/cloudfoundry/garden-linux/), [windows](https://github.com/cloudfoundry/garden-windows) and [The Open Container Initiative Spec](https://github.com/cloudfoundry/guardian/).

Garden is a platform-agnostic Go API for container creation and management, with pluggable backends for different platforms and runtimes.
This package contains the canonical client, as well as a server package containing an interface to be implemented by backends.

If you're just getting started, you probably want to begin by setting up one of the [backends](#backends) listed below.
If you want to use the Garden client to manage containers, see the [Client API](#client-api) section.

# Backends

Backends implement support for various specific platforms.
So far, the list of backends is as follows:

 - [Garden Linux](https://github.com/cloudfoundry/garden-linux/) - Linux backend
 - [Guardian](https://github.com/cloudfoundry/guardian/) - Linux backend using [runc](https://github.com/opencontainers/runc)
 - [Greenhouse](https://github.com/cloudfoundry/garden-windows) - Windows backend

# Client API

The canonical API for Garden is defined as a collection of Go interfaces.
See the [godoc documentation](http://godoc.org/code.cloudfoundry.org/garden) for details.

## Example use

_Error checking ignored for brevity._

Import these packages:
```
"code.cloudfoundry.org/garden"
"code.cloudfoundry.org/garden/client"
"code.cloudfoundry.org/garden/client/connection"
```

Create a client:
```
gardenClient := client.New(connection.New("tcp", "127.0.0.1:7777"))
```

Create a container:
```
container, _ := gardenClient.Create(garden.ContainerSpec{})
```

Run a process:
```
buffer := &bytes.Buffer{}
process, _ := container.Run(garden.ProcessSpec{
  User: "alice",
  Path: "echo",
  Args: []string{"hello from the container"},
}, garden.ProcessIO{
  Stdout: buffer,
  Stderr: buffer,
})
exitCode := process.Wait()
fmt.Println(buffer.String())
```

# Development

## Prerequisites

* [go](https://golang.org)
* [git](http://git-scm.com/) (for garden and its dependencies)
* [mercurial](http://mercurial.selenic.com/) (for some other dependencies not using git)

## Running the tests

Assuming go is installed and `$GOPATH` is set:
```
mkdir -p $GOPATH/src/code.cloudfoundry.org
cd $GOPATH/src/code.cloudfoundry.org
git clone git@github.com:cloudfoundry/garden
cd garden
go get -t -u ./...
go install github.com/onsi/ginkgo/ginkgo
ginkgo -r
```
# Rata: It's a smat rata. Wicked smat.
Rata is a router with Pat-style path patterns, plus more.

API Docs: https://godoc.org/github.com/tedsuo/rata

Package rata provides three things: Routes, a Router, and a RequestGenerator.

Routes are structs that define which Method and Path each associated http handler
should respond to. Unlike many router implementations, the routes and the handlers
are defined separately.  This allows for the routes to be reused in multiple contexts.
For example, a proxy server and a backend server can be created by having one set of
Routes, but two sets of Handlers (one handler that proxies, another that serves the
request). Likewise, your client code can use the routes with the RequestGenerator to
create requests that use the same routes.  Then, if the routes change, unit tests in
the client and proxy service will warn you of the problem.  This contract helps components
stay in sync while relying less on integration tests.

For example, let's imagine that you want to implement a "pet" resource that allows
you to view, create, update, and delete which pets people own.  Also, you would
like to include the owner_id and pet_id as part of the URL path.

First off, the routes might look like this:
```go
  petRoutes := rata.Routes{
    {Name: "get_pet",    Method: rata.GET,    Path: "/people/:owner_id/pets/:pet_id"},
    {Name: "create_pet", Method: rata.POST,   Path: "/people/:owner_id/pets"},
    {Name: "update_pet", Method: rata.PUT,    Path: "/people/:owner_id/pets/:pet_id"},
    {Name: "delete_pet", Method: rata.DELETE, Path: "/people/:owner_id/pets/:pet_id"},
  }
```

On the server, create a matching set of http handlers, one for each route:
```go
  petHandlers := rata.Handlers{
    "get_pet":    newGetPetHandler(),
    "create_pet": newCreatePetHandler(),
    "update_pet": newUpdatePetHandler(),
    "delete_pet": newDeletePetHandler()
  }
```

You can create a router by mixing the routes and handlers together:
```go
  router, err := rata.NewRouter(petRoutes, petHandlers)
  if err != nil {
    panic(err)
  }

  // The router is just an http.Handler, so it can be used to create a server in the usual fashion:
  server := httptest.NewServer(router)
```

Handlers can obtain parameters derived from the URL path:
```go
  ownerId := rata.Param(request, "owner_id")
```

Meanwhile, on the client side, you can create a request generator:
```go
  requestGenerator := rata.NewRequestGenerator(server.URL, petRoutes)

  // You can use the request generator to ensure you are creating a valid request:
  req, err := requestGenerator.CreateRequest("get_pet", rata.Params{"owner_id": "123", "pet_id": "5"}, nil)

  // The generated request can be used like any other http.Request object:
  res, err := http.DefaultClient.Do(req)
```
# hcsshim

This package supports launching Windows Server containers from Go. It is
primarily used in the [Docker Engine](https://github.com/docker/docker) project,
but it can be freely used by other projects as well.

This project has adopted the [Microsoft Open Source Code of
Conduct](https://opensource.microsoft.com/codeofconduct/). For more information
see the [Code of Conduct
FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact
[opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional
questions or comments.
# go-winio

This repository contains utilities for efficiently performing Win32 IO operations in
Go. Currently, this is focused on accessing named pipes and other file handles, and
for using named pipes as a net transport.

This code relies on IO completion ports to avoid blocking IO on system threads, allowing Go
to reuse the thread to schedule another goroutine. This limits support to Windows Vista and
newer operating systems. This is similar to the implementation of network sockets in Go's net
package.

Please see the LICENSE file for licensing information.

This project has adopted the [Microsoft Open Source Code of
Conduct](https://opensource.microsoft.com/codeofconduct/). For more information
see the [Code of Conduct
FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact
[opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional
questions or comments.

Thanks to natefinch for the inspiration for this library. See https://github.com/natefinch/npipe
for another named pipe implementation.
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
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |


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
# pat (formerly pat.go) - A Sinatra style pattern muxer for Go's net/http library

[![GoDoc](https://godoc.org/github.com/bmizerany/pat?status.svg)](https://godoc.org/github.com/bmizerany/pat) 

## INSTALL

	$ go get github.com/bmizerany/pat

## USE

```go
package main

import (
	"io"
	"net/http"
	"github.com/bmizerany/pat"
	"log"
)

// hello world, the web server
func HelloServer(w http.ResponseWriter, req *http.Request) {
	io.WriteString(w, "hello, "+req.URL.Query().Get(":name")+"!\n")
}

func main() {
	m := pat.New()
	m.Get("/hello/:name", http.HandlerFunc(HelloServer))

	// Register this pat with the default serve mux so that other packages
	// may also be exported. (i.e. /debug/pprof/*)
	http.Handle("/", m)
	err := http.ListenAndServe(":12345", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
```

It's that simple.

For more information, see:
http://godoc.org/github.com/bmizerany/pat

## CONTRIBUTORS

* Alexis Svinartchouk (@zvin)
* Blake Mizerany (@bmizerany)
* Brian Ketelsen (@bketelsen)
* Bryan Matsuo (@bmatsuo)
* Caleb Spare (@cespare)
* Evan Shaw (@edsrzf)
* Gary Burd (@garyburd)
* George Rogers (@georgerogers42)
* Keith Rarick (@kr)
* Matt Williams (@mattyw)
* Mike Stipicevic (@wickedchicken)
* Nick Saika (@nesv)
* Timothy Cyrus (@tcyrus)
* binqin (@binku87)

## LICENSE

Copyright (C) 2012 by Keith Rarick, Blake Mizerany

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
This package provides helper functions for dealing with string identifiers
This project was automatically exported from code.google.com/p/go-uuid

# uuid ![build status](https://travis-ci.org/pborman/uuid.svg?branch=master)
The uuid package generates and inspects UUIDs based on [RFC 412](http://tools.ietf.org/html/rfc4122) and DCE 1.1: Authentication and Security Services. 

###### Install
`go get github.com/pborman/uuid`

###### Documentation 
[![GoDoc](https://godoc.org/github.com/pborman/uuid?status.svg)](http://godoc.org/github.com/pborman/uuid)

Full `go doc` style documentation for the package can be viewed online without installing this package by using the GoDoc site here: 
http://godoc.org/github.com/pborman/uuid
# Windows 2016 Cell for Cloud Foundry with bosh-lite

## Requirements
- Running Bosh Lite - https://github.com/cloudfoundry/bosh-lite
- Cloud Foundry deployment on Bosh Lite - https://github.com/cloudfoundry/cf-release
- Diego deployment ( v0.1486.0 ) on Bosh Lite - https://github.com/cloudfoundry/diego-release/tree/develop/examples/bosh-lite
- Vagrant ( >= 1.8.6) and Virtualbox
- Add the [Windows 2016 lifecycle](https://github.com/stefanschneider/windows_app_lifecycle/tree/w2016) to diego lifecycle_bundles: "buildpack/windows2016:windows2016_app_lifecycle/windows2016_app_lifecycle.tgz"

```
# Run the following script to change the diego deployment manifest to add the extra windows2016 lifecycle_bundle

cd ~/workspace/diego-release

git apply << EOM
diff --git a/manifest-generation/diego.yml b/manifest-generation/diego.yml
index b20b724..9d64b4f 100644
--- a/manifest-generation/diego.yml
+++ b/manifest-generation/diego.yml
@@ -602,6 +602,12 @@ properties:
       dropsonde_port: (( config_from_cf.metron_agent.dropsonde_incoming_port ))
       log_level: (( property_overrides.cc_uploader.log_level || nil ))
     nsync:
+      lifecycle_bundles:
+        - "buildpack/cflinuxfs2:buildpack_app_lifecycle/buildpack_app_lifecycle.tgz"
+        - "buildpack/windows2012R2:windows_app_lifecycle/windows_app_lifecycle.tgz"
+        - "buildpack/windows2016:windows2016_app_lifecycle/windows2016_app_lifecycle.tgz"
+        - "docker:docker_app_lifecycle/docker_app_lifecycle.tgz"
+
       diego_privileged_containers: (( property_overrides.nsync.diego_privileged_containers || nil ))
       dropsonde_port: (( config_from_cf.metron_agent.dropsonde_incoming_port ))
       bbs:
@@ -618,6 +624,12 @@ properties:
         basic_auth_password: (( config_from_cf.cc.internal_api_password ))
       log_level: (( property_overrides.nsync.log_level || nil ))
     stager:
+      lifecycle_bundles:
+        - "buildpack/cflinuxfs2:buildpack_app_lifecycle/buildpack_app_lifecycle.tgz"
+        - "buildpack/windows2012R2:windows_app_lifecycle/windows_app_lifecycle.tgz"
+        - "buildpack/windows2016:windows2016_app_lifecycle/windows2016_app_lifecycle.tgz"
+        - "docker:docker_app_lifecycle/docker_app_lifecycle.tgz"
+
       diego_privileged_containers: (( property_overrides.stager.diego_privileged_containers || nil ))
       dropsonde_port: (( config_from_cf.metron_agent.dropsonde_incoming_port ))
       cc:
EOM

./scripts/generate-bosh-lite-manifests
bosh -n --deployment ~/workspace/diego-release/bosh-lite/deployments/diego.yml deploy
```

- Upload the [Windows 2016 lifecycle build](https://ci.appveyor.com/project/StefanSchneider/windows-app-lifecycle-qc4gr/build/artifacts) to "access_z1" bosh job

```
# Use the following script to upload the new lifecycle.
# N.B. Run this script again if the bosh job is restarted or recreated

cd /tmp
bosh -n target 192.168.50.4 lite
bosh -n login admin admin
bosh -n download manifest cf-warden-diego cf-warden-diego.yml
bosh deployment cf-warden-diego.yml

curl -L -o windows2016_app_lifecycle.tgz "https://ci.appveyor.com/api/buildjobs/ov1lgry9q45deebg/artifacts/output%2Fwindows_app_lifecycle-1c8273c.tgz"
bosh scp access_z1/0 windows2016_app_lifecycle.tgz /tmp/windows2016_app_lifecycle.tgz  --upload
bosh ssh access_z1/0 -- sudo mkdir -p /var/vcap/jobs/file_server/packages/windows2016_app_lifecycle "&&" sudo cp /tmp/windows2016_app_lifecycle.tgz /var/vcap/jobs/file_server/packages/windows2016_app_lifecycle/windows2016_app_lifecycle.tgz
```
- Add windows2016 stack to Cloud Foundry deployment
```
cf curl /v2/stacks -X POST -d '{"name":"windows2016","description":"Windows Server Core 2016"}'
```

## Create a Windows 2016 vagrant box for VirtualBox
Install VirtualBox, [packer](https://www.packer.io/), get the [Windows Server 2016 Evaluation ISO](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2016)  and download the following packer bundle https://github.com/StefanScherer/packer-windows/tree/b2a7684f75b533091733ae5fb25609af233e1284

To build the vagrant box run the following command from the packer-windows directory:
```
packer build --only=virtualbox-iso ^
 --var 'iso_url=D:/software/14393.0.160715-1616.RS1_RELEASE_SERVER_EVAL_X64FRE_EN-US.ISO' ^
 ./windows_2016_docker.json
```

N.B: The build usually takes a couple of hours, depending on your internet connection quality.

After the packer build is finished, add the box to vagrant:
```
vagrant box add windows_2016_docker_virtualbox.box   --name windows_2016_docker_virtualbox_rs1_v1
```


## Usage
Run `vagrant up` from the dev-box directory and wait for the deployment to complete.
To access the Windows VM use `vagrant rdp`, or connect directly to `192.168.50.16` using Remote Desktop Connection.
