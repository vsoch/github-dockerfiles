[![Build Status](https://jenkins.dockerproject.org/buildStatus/icon?job=runc Master)](https://jenkins.dockerproject.org/job/runc Master)

## runc

`runc` is a CLI tool for spawning and running containers according to the OCF specification.

## State of the project

Currently `runc` is an implementation of the OCI specification.  We are currently sprinting
to have a v1 of the spec out. So the `runc` config format will be constantly changing until
the spec is finalized. However, we encourage you to try out the tool and give feedback.

### OCF

How does `runc` integrate with the Open Container Initiative Specification?
`runc` depends on the types specified in the
[specs](https://github.com/opencontainers/runtime-spec) repository. Whenever the
specification is updated and ready to be versioned `runc` will update its dependency
on the specs repository and support the update spec.

### Building:

At the time of writing, runc only builds on the Linux platform.

```bash
# create a 'github.com/opencontainers' in your GOPATH/src
cd github.com/opencontainers
git clone https://github.com/opencontainers/runc
cd runc
make
sudo make install
```

In order to enable seccomp support you will need to install libseccomp on your platform.
If you do not want to build `runc` with seccomp support you can add `BUILDTAGS=""` when running make.

#### Build Tags

`runc` supports optional build tags for compiling in support for various features.


| Build Tag | Feature                            | Dependency  |
|-----------|------------------------------------|-------------|
| seccomp   | Syscall filtering                  | libseccomp  |
| selinux   | selinux process and mount labeling | <none>      |
| apparmor  | apparmor profile support           | libapparmor |

### Testing:

You can run tests for runC by using command:

```bash
# make test
```

Note that test cases are run in Docker container, so you need to install
`docker` first. And test requires mounting cgroups inside container, it's
done by docker now, so you need a docker version newer than 1.8.0-rc2.

You can also run specific test cases by:

```bash
# make test TESTFLAGS="-run=SomeTestFunction"
```

### Using:

To run a container with the id "test", execute `runc start` with the containers id as arg one 
in the bundle's root directory:

```bash
runc start test
/ $ ps
PID   USER     COMMAND
1     daemon   sh
5     daemon   sh
/ $
```

### OCI Container JSON Format:

OCI container JSON format is based on OCI [specs](https://github.com/opencontainers/runtime-spec).
You can generate JSON files by using `runc spec`.
It assumes that the file-system is found in a directory called
`rootfs` and there is a user with uid and gid of `0` defined within that file-system.

### Examples:

#### Using a Docker image (requires version 1.3 or later)

To test using Docker's `busybox` image follow these steps:
* Install `docker` and download the `busybox` image: `docker pull busybox`
* Create a container from that image and export its contents to a tar file:
`docker export $(docker create busybox) > busybox.tar`
* Untar the contents to create your filesystem directory:
```
mkdir rootfs
tar -C rootfs -xf busybox.tar
```
* Create `config.json` by using `runc spec`.
* Execute `runc start` and you should be placed into a shell where you can run `ps`:
```
$ runc start test
/ # ps
PID   USER     COMMAND
    1 root     sh
    9 root     ps
```

#### Using runc with systemd

To use runc with systemd, you can create a unit file
`/usr/lib/systemd/system/minecraft.service` as below (edit your
own Description or WorkingDirectory or service name as you need).

```service
[Unit]
Description=Minecraft Build Server
Documentation=http://minecraft.net
After=network.target

[Service]
CPUQuota=200%
MemoryLimit=1536M
ExecStart=/usr/local/bin/runc start minecraft
Restart=on-failure
WorkingDirectory=/containers/minecraftbuild

[Install]
WantedBy=multi-user.target
```

Make sure you have the bundle's root directory and JSON configs in
your WorkingDirectory, then use systemd commands to start the service:

```bash
systemctl daemon-reload
systemctl start minecraft.service
```

Note that if you use JSON configs by `runc spec`, you need to modify
`config.json` and change `process.terminal` to false so runc won't
create tty, because we can't set terminal from the stdin when using
systemd service.
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
# Papertrail Hook for Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:" />

[Papertrail](https://papertrailapp.com) provides hosted log management. Once stored in Papertrail, you can [group](http://help.papertrailapp.com/kb/how-it-works/groups/) your logs on various dimensions, [search](http://help.papertrailapp.com/kb/how-it-works/search-syntax) them, and trigger [alerts](http://help.papertrailapp.com/kb/how-it-works/alerts).

In most deployments, you'll want to send logs to Papertrail via their [remote_syslog](http://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-text-log-files-in-unix/) daemon, which requires no application-specific configuration. This hook is intended for relatively low-volume logging, likely in managed cloud hosting deployments where installing `remote_syslog` is not possible.

## Usage

You can find your Papertrail UDP port on your [Papertrail account page](https://papertrailapp.com/account/destinations). Substitute it below for `YOUR_PAPERTRAIL_UDP_PORT`.

For `YOUR_APP_NAME`, substitute a short string that will readily identify your application or service in the logs.

```go
import (
  "log/syslog"
  "github.com/Sirupsen/logrus"
  "github.com/Sirupsen/logrus/hooks/papertrail"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_papertrail.NewPapertrailHook("logs.papertrailapp.com", YOUR_PAPERTRAIL_UDP_PORT, YOUR_APP_NAME)

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```
# Syslog Hooks for Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>

## Usage

```go
import (
  "log/syslog"
  "github.com/Sirupsen/logrus"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```
# Sentry Hook for Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:" />

[Sentry](https://getsentry.com) provides both self-hosted and hosted
solutions for exception tracking.
Both client and server are
[open source](https://github.com/getsentry/sentry).

## Usage

Every sentry application defined on the server gets a different
[DSN](https://www.getsentry.com/docs/). In the example below replace
`YOUR_DSN` with the one created for your application.

```go
import (
  "github.com/Sirupsen/logrus"
  "github.com/Sirupsen/logrus/hooks/sentry"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_sentry.NewSentryHook(YOUR_DSN, []logrus.Level{
    logrus.PanicLevel,
    logrus.FatalLevel,
    logrus.ErrorLevel,
  })

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```

## Special fields

Some logrus fields have a special meaning in this hook,
these are server_name and logger.
When logs are sent to sentry these fields are treated differently.
- server_name (also known as hostname) is the name of the server which
is logging the event (hostname.example.com)
- logger is the part of the application which is logging the event.
In go this usually means setting it to the name of the package.

## Timeout

`Timeout` is the time the sentry hook will wait for a response
from the sentry server.

If this time elapses with no response from
the server an error will be returned.

If `Timeout` is set to 0 the SentryHook will not wait for a reply
and will assume a correct delivery.

The SentryHook has a default timeout of `100 milliseconds` when created
with a call to `NewSentryHook`. This can be changed by assigning a value to the `Timeout` field:

```go
hook, _ := logrus_sentry.NewSentryHook(...)
hook.Timeout = 20*time.Second
```
dbus
----

dbus is a simple library that implements native Go client bindings for the
D-Bus message bus system.

### Features

* Complete native implementation of the D-Bus message protocol
* Go-like API (channels for signals / asynchronous method calls, Goroutine-safe connections)
* Subpackages that help with the introspection / property interfaces

### Installation

This packages requires Go 1.1. If you installed it and set up your GOPATH, just run:

```
go get github.com/godbus/dbus
```

If you want to use the subpackages, you can install them the same way.

### Usage

The complete package documentation and some simple examples are available at
[godoc.org](http://godoc.org/github.com/godbus/dbus). Also, the
[_examples](https://github.com/godbus/dbus/tree/master/_examples) directory
gives a short overview over the basic usage. 

#### Projects using godbus
- [notify](https://github.com/esiqveland/notify) provides desktop notifications over dbus into a library.

Please note that the API is considered unstable for now and may change without
further notice.

### License

go.dbus is available under the Simplified BSD License; see LICENSE for the full
text.

Nearly all of the credit for this library goes to github.com/guelfey/go.dbus.
[![Coverage](http://gocover.io/_badge/github.com/codegangsta/cli?0)](http://gocover.io/github.com/codegangsta/cli)
[![Build Status](https://travis-ci.org/codegangsta/cli.png?branch=master)](https://travis-ci.org/codegangsta/cli)
[![GoDoc](https://godoc.org/github.com/codegangsta/cli?status.svg)](https://godoc.org/github.com/codegangsta/cli)

# cli.go
`cli.go` is simple, fast, and fun package for building command line apps in Go. The goal is to enable developers to write fast and distributable command line applications in an expressive way.

## Overview
Command line apps are usually so tiny that there is absolutely no reason why your code should *not* be self-documenting. Things like generating help text and parsing command flags/options should not hinder productivity when writing a command line app.

**This is where `cli.go` comes into play.** `cli.go` makes command line programming fun, organized, and expressive!

## Installation
Make sure you have a working Go environment (go 1.1+ is *required*). [See the install instructions](http://golang.org/doc/install.html).

To install `cli.go`, simply run:
```
$ go get github.com/codegangsta/cli
```

Make sure your `PATH` includes to the `$GOPATH/bin` directory so your commands can be easily used:
```
export PATH=$PATH:$GOPATH/bin
```

## Getting Started
One of the philosophies behind `cli.go` is that an API should be playful and full of discovery. So a `cli.go` app can be as little as one line of code in `main()`.

``` go
package main

import (
  "os"
  "github.com/codegangsta/cli"
)

func main() {
  cli.NewApp().Run(os.Args)
}
```

This app will run and show help text, but is not very useful. Let's give an action to execute and some help documentation:

``` go
package main

import (
  "os"
  "github.com/codegangsta/cli"
)

func main() {
  app := cli.NewApp()
  app.Name = "boom"
  app.Usage = "make an explosive entrance"
  app.Action = func(c *cli.Context) {
    println("boom! I say!")
  }
  
  app.Run(os.Args)
}
```

Running this already gives you a ton of functionality, plus support for things like subcommands and flags, which are covered below.

## Example

Being a programmer can be a lonely job. Thankfully by the power of automation that is not the case! Let's create a greeter app to fend off our demons of loneliness!

Start by creating a directory named `greet`, and within it, add a file, `greet.go` with the following code in it:

``` go
package main

import (
  "os"
  "github.com/codegangsta/cli"
)

func main() {
  app := cli.NewApp()
  app.Name = "greet"
  app.Usage = "fight the loneliness!"
  app.Action = func(c *cli.Context) {
    println("Hello friend!")
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

`cli.go` also generates neat help text:

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
    --version	Shows version information
```

### Arguments
You can lookup arguments by calling the `Args` function on `cli.Context`.

``` go
...
app.Action = func(c *cli.Context) {
  println("Hello", c.Args()[0])
}
...
```

### Flags
Setting and querying flags is simple.
``` go
...
app.Flags = []cli.Flag {
  cli.StringFlag{
    Name: "lang",
    Value: "english",
    Usage: "language for the greeting",
  },
}
app.Action = func(c *cli.Context) {
  name := "someone"
  if len(c.Args()) > 0 {
    name = c.Args()[0]
  }
  if c.String("lang") == "spanish" {
    println("Hola", name)
  } else {
    println("Hello", name)
  }
}
...
```

You can also set a destination variable for a flag, to which the content will be scanned.
``` go
...
var language string
app.Flags = []cli.Flag {
  cli.StringFlag{
    Name:        "lang",
    Value:       "english",
    Usage:       "language for the greeting",
    Destination: &language,
  },
}
app.Action = func(c *cli.Context) {
  name := "someone"
  if len(c.Args()) > 0 {
    name = c.Args()[0]
  }
  if language == "spanish" {
    println("Hola", name)
  } else {
    println("Hello", name)
  }
}
...
```

See full list of flags at http://godoc.org/github.com/codegangsta/cli

#### Alternate Names

You can set alternate (or short) names for flags by providing a comma-delimited list for the `Name`. e.g.

``` go
app.Flags = []cli.Flag {
  cli.StringFlag{
    Name: "lang, l",
    Value: "english",
    Usage: "language for the greeting",
  },
}
```

That flag can then be set with `--lang spanish` or `-l spanish`. Note that giving two different forms of the same flag in the same command invocation is an error.

#### Values from the Environment

You can also have the default value set from the environment via `EnvVar`.  e.g.

``` go
app.Flags = []cli.Flag {
  cli.StringFlag{
    Name: "lang, l",
    Value: "english",
    Usage: "language for the greeting",
    EnvVar: "APP_LANG",
  },
}
```

The `EnvVar` may also be given as a comma-delimited "cascade", where the first environment variable that resolves is used as the default.

``` go
app.Flags = []cli.Flag {
  cli.StringFlag{
    Name: "lang, l",
    Value: "english",
    Usage: "language for the greeting",
    EnvVar: "LEGACY_COMPAT_LANG,APP_LANG,LANG",
  },
}
```

### Subcommands

Subcommands can be defined for a more git-like command line app.
```go
...
app.Commands = []cli.Command{
  {
    Name:      "add",
    Aliases:     []string{"a"},
    Usage:     "add a task to the list",
    Action: func(c *cli.Context) {
      println("added task: ", c.Args().First())
    },
  },
  {
    Name:      "complete",
    Aliases:     []string{"c"},
    Usage:     "complete a task on the list",
    Action: func(c *cli.Context) {
      println("completed task: ", c.Args().First())
    },
  },
  {
    Name:      "template",
    Aliases:     []string{"r"},
    Usage:     "options for task templates",
    Subcommands: []cli.Command{
      {
        Name:  "add",
        Usage: "add a new template",
        Action: func(c *cli.Context) {
            println("new task template: ", c.Args().First())
        },
      },
      {
        Name:  "remove",
        Usage: "remove an existing template",
        Action: func(c *cli.Context) {
          println("removed task template: ", c.Args().First())
        },
      },
    },
  },
}
...
```

### Bash Completion

You can enable completion commands by setting the `EnableBashCompletion`
flag on the `App` object.  By default, this setting will only auto-complete to
show an app's subcommands, but you can write your own completion methods for
the App or its subcommands.
```go
...
var tasks = []string{"cook", "clean", "laundry", "eat", "sleep", "code"}
app := cli.NewApp()
app.EnableBashCompletion = true
app.Commands = []cli.Command{
  {
    Name:  "complete",
    Aliases: []string{"c"},
    Usage: "complete a task on the list",
    Action: func(c *cli.Context) {
       println("completed task: ", c.Args().First())
    },
    BashComplete: func(c *cli.Context) {
      // This will complete if no args are passed
      if len(c.Args()) > 0 {
        return
      }
      for _, t := range tasks {
        fmt.Println(t)
      }
    },
  }
}
...
```

#### To Enable

Source the `autocomplete/bash_autocomplete` file in your `.bashrc` file while
setting the `PROG` variable to the name of your program:

`PROG=myprogram source /.../cli/autocomplete/bash_autocomplete`

#### To Distribute

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

## Contribution Guidelines
Feel free to put up a pull request to fix a bug or maybe add a feature. I will give it a code review and make sure that it does not break backwards compatibility. If I or any other collaborators agree that it is in line with the vision of the project, we will work with you to get the code into a mergeable state and merge it into the master branch.

If you have contributed something significant to the project, I will most likely add you as a collaborator. As a collaborator you are given the ability to merge others pull requests. It is very important that new code does not break existing code, so be careful about what code you do choose to merge. If you have any questions feel free to link @codegangsta to the issue in question and we can review it together.

If you feel like you have contributed to the project but have not yet been added as a collaborator, I probably forgot to add you. Hit @codegangsta up over email and we will get it figured out.
libseccomp-golang: Go Language Bindings for the libseccomp Project
===============================================================================
https://github.com/seccomp/libseccomp-golang
https://github.com/seccomp/libseccomp

The libseccomp library provides an easy to use, platform independent, interface
to the Linux Kernel's syscall filtering mechanism.  The libseccomp API is
designed to abstract away the underlying BPF based syscall filter language and
present a more conventional function-call based filtering interface that should
be familiar to, and easily adopted by, application developers.

The libseccomp-golang library provides a Go based interface to the libseccomp
library.

* Online Resources

The library source repository currently lives on GitHub at the following URLs:

	-> https://github.com/seccomp/libseccomp-golang
	-> https://github.com/seccomp/libseccomp

The project mailing list is currently hosted on Google Groups at the URL below,
please note that a Google account is not required to subscribe to the mailing
list.

	-> https://groups.google.com/d/forum/libseccomp
# netlink - netlink library for go #

[![Build Status](https://travis-ci.org/vishvananda/netlink.png?branch=master)](https://travis-ci.org/vishvananda/netlink) [![GoDoc](https://godoc.org/github.com/vishvananda/netlink?status.svg)](https://godoc.org/github.com/vishvananda/netlink)

The netlink package provides a simple netlink library for go. Netlink
is the interface a user-space program in linux uses to communicate with
the kernel. It can be used to add and remove interfaces, set ip addresses
and routes, and configure ipsec. Netlink communication requires elevated
privileges, so in most cases this code needs to be run as root. Since
low-level netlink messages are inscrutable at best, the library attempts
to provide an api that is loosely modeled on the CLI provied by iproute2.
Actions like `ip link add` will be accomplished via a similarly named
function like AddLink(). This library began its life as a fork of the
netlink functionality in
[docker/libcontainer](https://github.com/docker/libcontainer) but was
heavily rewritten to improve testability, performance, and to add new
functionality like ipsec xfrm handling.

## Local Build and Test ##

You can use go get command:

    go get github.com/vishvananda/netlink

Testing dependencies:

    go get github.com/vishvananda/netns

Testing (requires root):

    sudo -E go test github.com/vishvananda/netlink

## Examples ##

Add a new bridge and add eth1 into it:

```go
package main

import (
    "net"
    "github.com/vishvananda/netlink"
)

func main() {
    la := netlink.NewLinkAttrs()
    la.Name = "foo"
    mybridge := &netlink.Bridge{la}}
    _ := netlink.LinkAdd(mybridge)
    eth1, _ := netlink.LinkByName("eth1")
    netlink.LinkSetMaster(eth1, mybridge)
}

```
Note `NewLinkAttrs` constructor, it sets default values in structure. For now
it sets only `TxQLen` to `-1`, so kernel will set default by itself. If you're
using simple initialization(`LinkAttrs{Name: "foo"}`) `TxQLen` will be set to
`0` unless you specify it like `LinkAttrs{Name: "foo", TxQLen: 1000}`.

Add a new ip address to loopback:

```go
package main

import (
    "net"
    "github.com/vishvananda/netlink"
)

func main() {
    lo, _ := netlink.LinkByName("lo")
    addr, _ := netlink.ParseAddr("169.254.169.254/32")
    netlink.AddrAdd(lo, addr)
}

```

## Future Work ##

Many pieces of netlink are not yet fully supported in the high-level
interface. Aspects of virtually all of the high-level objects don't exist.
Many of the underlying primitives are there, so its a matter of putting
the right fields into the high-level objects and making sure that they
are serialized and deserialized correctly in the Add and List methods.

There are also a few pieces of low level netlink functionality that still
need to be implemented. Routing rules are not in place and some of the
more advanced link types. Hopefully there is decent structure and testing
in place to make these fairly straightforward to add.
# Introduction

go-units is a library to transform human friendly measurements into machine friendly values.

## Usage

See the [docs in godoc](https://godoc.org/github.com/docker/go-units) for examples and documentation.

## License

go-units is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
Package symlink implements EvalSymlinksInScope which is an extension of filepath.EvalSymlinks
from the [Go standard library](https://golang.org/pkg/path/filepath).

The code from filepath.EvalSymlinks has been adapted in fs.go.
Please read the LICENSE.BSD file that governs fs.go and LICENSE.APACHE for fs_test.go.
runc man pages
====================

This directory contains man pages for runc in markdown format.

To generate man pages from it, use this command

    ./md2man-all.sh

You will see man pages generated under the man8 directory.

Libcontainer provides a native Go implementation for creating containers
with namespaces, cgroups, capabilities, and filesystem access controls.
It allows you to manage the lifecycle of the container performing additional operations
after the container is created.


#### Container
A container is a self contained execution environment that shares the kernel of the
host system and which is (optionally) isolated from other containers in the system.

#### Using libcontainer

Because containers are spawned in a two step process you will need a binary that
will be executed as the init process for the container. In libcontainer, we use
the current binary (/proc/self/exe) to be executed as the init process, and use
arg "init", we call the first step process "bootstrap", so you always need a "init"
function as the entry of "bootstrap".

```go
func init() {
	if len(os.Args) > 1 && os.Args[1] == "init" {
		runtime.GOMAXPROCS(1)
		runtime.LockOSThread()
		factory, _ := libcontainer.New("")
		if err := factory.StartInitialization(); err != nil {
			logrus.Fatal(err)
		}
		panic("--this line should have never been executed, congratulations--")
	}
}
```

Then to create a container you first have to initialize an instance of a factory
that will handle the creation and initialization for a container.

```go
factory, err := libcontainer.New("/var/lib/container", libcontainer.Cgroupfs, libcontainer.InitArgs(os.Args[0], "init"))
if err != nil {
	logrus.Fatal(err)
	return
}
```

Once you have an instance of the factory created we can create a configuration
struct describing how the container is to be created. A sample would look similar to this:

```go
defaultMountFlags := syscall.MS_NOEXEC | syscall.MS_NOSUID | syscall.MS_NODEV
config := &configs.Config{
	Rootfs: "/your/path/to/rootfs",
	Capabilities: []string{
		"CAP_CHOWN",
		"CAP_DAC_OVERRIDE",
		"CAP_FSETID",
		"CAP_FOWNER",
		"CAP_MKNOD",
		"CAP_NET_RAW",
		"CAP_SETGID",
		"CAP_SETUID",
		"CAP_SETFCAP",
		"CAP_SETPCAP",
		"CAP_NET_BIND_SERVICE",
		"CAP_SYS_CHROOT",
		"CAP_KILL",
		"CAP_AUDIT_WRITE",
	},
	Namespaces: configs.Namespaces([]configs.Namespace{
		{Type: configs.NEWNS},
		{Type: configs.NEWUTS},
		{Type: configs.NEWIPC},
		{Type: configs.NEWPID},
		{Type: configs.NEWUSER},
		{Type: configs.NEWNET},
	}),
	Cgroups: &configs.Cgroup{
		Name:   "test-container",
		Parent: "system",
		Resources: &configs.Resources{
			MemorySwappiness: nil,
			AllowAllDevices:  false,
			AllowedDevices:   configs.DefaultAllowedDevices,
		},
	},
	MaskPaths: []string{
		"/proc/kcore",
	},
	ReadonlyPaths: []string{
		"/proc/sys", "/proc/sysrq-trigger", "/proc/irq", "/proc/bus",
	},
	Devices:  configs.DefaultAutoCreatedDevices,
	Hostname: "testing",
	Mounts: []*configs.Mount{
		{
			Source:      "proc",
			Destination: "/proc",
			Device:      "proc",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "tmpfs",
			Destination: "/dev",
			Device:      "tmpfs",
			Flags:       syscall.MS_NOSUID | syscall.MS_STRICTATIME,
			Data:        "mode=755",
		},
		{
			Source:      "devpts",
			Destination: "/dev/pts",
			Device:      "devpts",
			Flags:       syscall.MS_NOSUID | syscall.MS_NOEXEC,
			Data:        "newinstance,ptmxmode=0666,mode=0620,gid=5",
		},
		{
			Device:      "tmpfs",
			Source:      "shm",
			Destination: "/dev/shm",
			Data:        "mode=1777,size=65536k",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "mqueue",
			Destination: "/dev/mqueue",
			Device:      "mqueue",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "sysfs",
			Destination: "/sys",
			Device:      "sysfs",
			Flags:       defaultMountFlags | syscall.MS_RDONLY,
		},
	},
	UidMappings: []configs.IDMap{
		{
			ContainerID: 0,
			HostID: 1000,
			Size: 65536,
		},
	},
	GidMappings: []configs.IDMap{
		{
			ContainerID: 0,
			HostID: 1000,
			Size: 65536,
		},
	},
	Networks: []*configs.Network{
		{
			Type:    "loopback",
			Address: "127.0.0.1/0",
			Gateway: "localhost",
		},
	},
	Rlimits: []configs.Rlimit{
		{
			Type: syscall.RLIMIT_NOFILE,
			Hard: uint64(1025),
			Soft: uint64(1025),
		},
	},
}
```

Once you have the configuration populated you can create a container:

```go
container, err := factory.Create("container-id", config)
if err != nil {
	logrus.Fatal(err)
	return
}
```

To spawn bash as the initial process inside the container and have the
processes pid returned in order to wait, signal, or kill the process:

```go
process := &libcontainer.Process{
	Args:   []string{"/bin/bash"},
	Env:    []string{"PATH=/bin"},
	User:   "daemon",
	Stdin:  os.Stdin,
	Stdout: os.Stdout,
	Stderr: os.Stderr,
}

err := container.Start(process)
if err != nil {
	logrus.Fatal(err)
	container.Destroy()
	return
}

// wait for the process to finish.
_, err := process.Wait()
if err != nil {
	logrus.Fatal(err)
}

// destroy the container.
container.Destroy()
```

Additional ways to interact with a running container are:

```go
// return all the pids for all processes running inside the container.
processes, err := container.Processes()

// get detailed cpu, memory, io, and network statistics for the container and
// it's processes.
stats, err := container.Stats()

// pause all processes inside the container.
container.Pause()

// resume all paused processes.
container.Resume()

// send signal to container's init process.
container.Signal(signal)
```


#### Checkpoint & Restore

libcontainer now integrates [CRIU](http://criu.org/) for checkpointing and restoring containers.
This let's you save the state of a process running inside a container to disk, and then restore
that state into a new process, on the same machine or on another machine.

`criu` version 1.5.2 or higher is required to use checkpoint and restore.
If you don't already  have `criu` installed, you can build it from source, following the
[online instructions](http://criu.org/Installation). `criu` is also installed in the docker image
generated when building libcontainer with docker.


## Copyright and license

Code and documentation copyright 2014 Docker, inc. Code released under the Apache 2.0 license.
Docs released under Creative commons.

## nsenter

The `nsenter` package registers a special init constructor that is called before 
the Go runtime has a chance to boot.  This provides us the ability to `setns` on 
existing namespaces and avoid the issues that the Go runtime has with multiple 
threads.  This constructor will be called if this package is registered, 
imported, in your go application.

The `nsenter` package will `import "C"` and it uses [cgo](https://golang.org/cmd/cgo/)
package. In cgo, if the import of "C" is immediately preceded by a comment, that comment, 
called the preamble, is used as a header when compiling the C parts of the package.
So every time we  import package `nsenter`, the C code function `nsexec()` would be 
called. And package `nsenter` is now only imported in Docker execdriver, so every time 
before we call `execdriver.Exec()`, that C code would run.

`nsexec()` will first check the environment variable `_LIBCONTAINER_INITPID` 
which will give the process of the container that should be joined. Namespaces fd will 
be found from `/proc/[pid]/ns` and set by `setns` syscall.

And then get the pipe number from `_LIBCONTAINER_INITPIPE`, error message could
be transfered through it. If tty is added, `_LIBCONTAINER_CONSOLE_PATH` will 
have value and start a console for output.

Finally, `nsexec()` will clone a child process , exit the parent process and let 
the Go runtime take over.
