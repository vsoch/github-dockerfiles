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
# Go Cryptography

This repository holds supplementary Go cryptography libraries.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/crypto/...`. You
can also manually git clone the repository to `$GOPATH/src/golang.org/x/crypto`.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the crypto repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/crypto:" in the
subject line, so it is easy to find.

Note that contributions to the cryptography package receive additional scrutiny
due to their sensitive nature. Patches may take longer than normal to receive
feedback.
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/sirupsen/logrus.svg?branch=master)](https://travis-ci.org/sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/sirupsen/logrus?status.svg)](https://godoc.org/github.com/sirupsen/logrus)

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger.

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

* [`FluentdFormatter`](https://github.com/joonix/log). Formats entries that can by parsed by Kubernetes and Google Container Engine.
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
# <img alt="chi" src="https://cdn.rawgit.com/go-chi/chi/master/_examples/chi.svg" width="220" />


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
parts. The core router `github.com/go-chi/chi` is quite small (less than 1000 LOC), but we've also
included some useful/optional subpackages: [middleware](/middleware), [render](https://github.com/go-chi/render) and [docgen](https://github.com/go-chi/docgen). We hope you enjoy it too!

## Install

`go get -u github.com/go-chi/chi`


## Features

* **Lightweight** - cloc'd in ~1000 LOC for the chi router
* **Fast** - yes, see [benchmarks](#benchmarks)
* **100% compatible with net/http** - use any http or middleware pkg in the ecosystem that is also compatible with `net/http`
* **Designed for modular/composable APIs** - middlewares, inline middlewares, route groups and subrouter mounting
* **Context control** - built on new `context` package, providing value chaining, cancelations and timeouts
* **Robust** - in production at Pressly, CloudFlare, Heroku, 99Designs, and many others (see [discussion](https://github.com/go-chi/chi/issues/91))
* **Doc generation** - `docgen` auto-generates routing documentation from your source to JSON or Markdown
* **No external dependencies** - plain ol' Go 1.7+ stdlib + net/http


## Examples

* [rest](https://github.com/go-chi/chi/blob/master/_examples/rest/main.go) - REST APIs made easy, productive and maintainable
* [logging](https://github.com/go-chi/chi/blob/master/_examples/logging/main.go) - Easy structured logging for any backend
* [limits](https://github.com/go-chi/chi/blob/master/_examples/limits/main.go) - Timeouts and Throttling
* [todos-resource](https://github.com/go-chi/chi/blob/master/_examples/todos-resource/main.go) - Struct routers/handlers, an example of another code layout style
* [versions](https://github.com/go-chi/chi/blob/master/_examples/versions/main.go) - Demo of `chi/render` subpkg
* [fileserver](https://github.com/go-chi/chi/blob/master/_examples/fileserver/main.go) - Easily serve static files
* [graceful](https://github.com/go-chi/chi/blob/master/_examples/graceful/main.go) - Graceful context signaling and server shutdown


**As easy as:**

```go
package main

import (
	"net/http"
	"github.com/go-chi/chi"
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
in JSON ([routes.json](https://github.com/go-chi/chi/blob/master/_examples/rest/routes.json)) and in
Markdown ([routes.md](https://github.com/go-chi/chi/blob/master/_examples/rest/routes.md)).

I highly recommend reading the source of the [examples](#examples) listed above, they will show you all the features
of chi and serve as a good form of documentation.

```go
import (
  //...
  "context"
  "github.com/go-chi/chi"
  "github.com/go-chi/chi/middleware"
)

func main() {
  r := chi.NewRouter()

  // A good base middleware stack
  r.Use(middleware.RequestID)
  r.Use(middleware.RealIP)
  r.Use(middleware.Logger)
  r.Use(middleware.Recoverer)

  // Set a timeout value on the request context (ctx), that will signal
  // through ctx.Done() that the request has timed out and further
  // processing should be stopped.
  r.Use(middleware.Timeout(60 * time.Second))

  r.Get("/", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("hi"))
  })

  // RESTy routes for "articles" resource
  r.Route("/articles", func(r chi.Router) {
    r.With(paginate).Get("/", listArticles)                           // GET /articles
    r.With(paginate).Get("/{month}-{day}-{year}", listArticlesByDate) // GET /articles/01-16-2017

    r.Post("/", createArticle)                                        // POST /articles
    r.Get("/search", searchArticles)                                  // GET /articles/search

    // Regexp url parameters:
    r.Get("/{articleSlug:[a-z-]+}", getArticleBySlug)                // GET /articles/home-is-toronto
    
    // Subrouters:
    r.Route("/{articleID}", func(r chi.Router) {
      r.Use(ArticleCtx)
      r.Get("/", getArticle)                                          // GET /articles/123
      r.Put("/", updateArticle)                                       // PUT /articles/123
      r.Delete("/", deleteArticle)                                    // DELETE /articles/123
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

	// Method and MethodFunc adds routes for `pattern` that matches
	// the `method` HTTP method.
	Method(method, pattern string, h http.Handler)
	MethodFunc(method, pattern string, h http.HandlerFunc)

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

	// MethodNotAllowed defines a handler to respond whenever a method is
	// not allowed.
	MethodNotAllowed(h http.HandlerFunc)
}

// Routes interface adds two methods for router traversal, which is also
// used by the `docgen` subpackage to generation documentation for Routers.
type Routes interface {
	// Routes returns the routing tree in an easily traversable structure.
	Routes() []Route

	// Middlewares returns the list of middlewares in use by the router.
	Middlewares() Middlewares

	// Match searches the routing tree for a handler that matches
	// the method/path - similar to routing a http request, but without
	// executing the handler thereafter.
	Match(rctx *Context, method, path string) bool
}
```

Each routing method accepts a URL `pattern` and chain of `handlers`. The URL pattern
supports named params (ie. `/users/{userID}`) and wildcards (ie. `/admin/*`). URL parameters
can be fetched at runtime by calling `chi.URLParam(r, "userID")` for named parameters
and `chi.URLParam(r, "*")` for a wildcard parameter.


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
  userID := chi.URLParam(r, "userID") // from a route like /users/{userID}

  ctx := r.Context()
  key := ctx.Value("key").(string)

  w.Write([]byte(fmt.Sprintf("hi %v, %v", userID, key)))
}
```


## Middlewares

chi comes equipped with an optional `middleware` package, providing a suite of standard
`net/http` middlewares. Please note, any middleware in the ecosystem that is also compatible
with `net/http` can be used with chi's mux.

### Core middlewares

-----------------------------------------------------------------------------------------------------------
| chi/middlware Handler | description                                                                     |
|:----------------------|:---------------------------------------------------------------------------------
| Compress              | Gzip compression for clients that accept compressed responses                   |
| GetHead               | Automatically route undefined HEAD requests to GET handlers                     |
| Heartbeat             | Monitoring endpoint to check the servers pulse                                  |
| Logger                | Logs the start and end of each request with the elapsed processing time         |
| NoCache               | Sets response headers to prevent clients from caching                           |
| Profiler              | Easily attach net/http/pprof to your routers                                    |
| RealIP                | Sets a http.Request's RemoteAddr to either X-Forwarded-For or X-Real-IP         |
| Recoverer             | Gracefully absorb panics and prints the stack trace                             |
| RequestID             | Injects a request ID into the context of each request                           |
| RedirectSlashes       | Redirect slashes on routing paths                                               |
| StripSlashes          | Strip slashes on routing paths                                                  |
| Throttle              | Puts a ceiling on the number of concurrent requests                             |
| Timeout               | Signals to the request context when the timeout deadline is reached             |
| URLFormat             | Parse extension from url and put it on request context                          |
| WithValue             | Short-hand middleware to set a key/value on the request context                 |
-----------------------------------------------------------------------------------------------------------

### Auxiliary middlewares

-----------------------------------------------------------------------------------------------------------
| package                                          | description                                          |
|:-------------------------------------------------|:------------------------------------------------------
| [cors](https://github.com/go-chi/cors)           | Cross-origin resource sharing (CORS)                 |
| [jwtauth](https://github.com/go-chi/jwtauth)     | JWT authentication                                   |
| [httpcoala](https://github.com/go-chi/httpcoala) | HTTP request coalescer                               |
| [chi-authz](https://github.com/casbin/chi-authz) | Request ACL via https://github.com/hsluoyz/casbin    | 
-----------------------------------------------------------------------------------------------------------

please [submit a PR](./CONTRIBUTING.md) if you'd like to include a link to a chi-compatible middleware


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

Results as of Aug 31, 2017 on Go 1.9.0

```shell
BenchmarkChi_Param        	 3000000	       607 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_Param5       	 2000000	       935 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_Param20      	 1000000	      1944 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_ParamWrite   	 2000000	       664 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_GithubStatic 	 2000000	       627 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_GithubParam  	 2000000	       847 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_GithubAll    	   10000	    175556 ns/op	   87700 B/op	     609 allocs/op
BenchmarkChi_GPlusStatic  	 3000000	       566 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_GPlusParam   	 2000000	       652 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_GPlus2Params 	 2000000	       767 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_GPlusAll     	  200000	      9794 ns/op	    5616 B/op	      39 allocs/op
BenchmarkChi_ParseStatic  	 3000000	       590 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_ParseParam   	 2000000	       656 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_Parse2Params 	 2000000	       715 ns/op	     432 B/op	       3 allocs/op
BenchmarkChi_ParseAll     	  100000	     18045 ns/op	   11232 B/op	      78 allocs/op
BenchmarkChi_StaticAll    	   10000	    108871 ns/op	   67827 B/op	     471 allocs/op
```

Comparison with other routers: https://gist.github.com/pkieltyka/c089f309abeb179cfc4deaa519956d8c

NOTE: the allocs in the benchmark above are from the calls to http.Request's
`WithContext(context.Context)` method that clones the http.Request, sets the `Context()`
on the duplicated (alloc'd) request and returns it the new request object. This is just
how setting context on a request in Go 1.7+ works.


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

[GoDoc]: https://godoc.org/github.com/go-chi/chi
[GoDoc Widget]: https://godoc.org/github.com/go-chi/chi?status.svg
[Travis]: https://travis-ci.org/go-chi/chi
[Travis Widget]: https://travis-ci.org/go-chi/chi.svg?branch=master
