# Mergo

A helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.

Also a lovely [comune](http://en.wikipedia.org/wiki/Mergo) (municipality) in the Province of Ancona in the Italian region Marche.

![Mergo dall'alto](http://www.comune.mergo.an.it/Siti/Mergo/Immagini/Foto/mergo_dall_alto.jpg)

## Status

It is ready for production use. It works fine although it may use more of testing. Some projects in the wild started using Mergo:

- [lynndylanhurley/defsynth-api](https://github.com/lynndylanhurley/defsynth-api)
- [russross/canvasassignments](https://github.com/russross/canvasassignments)
- [rdegges/cryptly-api](https://github.com/rdegges/cryptly-api)

[![Build Status][1]][2]
[![GoDoc](https://godoc.org/github.com/imdario/mergo?status.svg)](https://godoc.org/github.com/imdario/mergo)

[1]: https://travis-ci.org/imdario/mergo.png
[2]: https://travis-ci.org/imdario/mergo

## Installation

    go get github.com/imdario/mergo

    // use in your .go code
    import (
        "github.com/imdario/mergo"
    )

## Usage

You can only merge same-type structs with exported fields initialized as zero value of their type and same-types maps. Mergo won't merge unexported (private) fields but will do recursively any exported one. Also maps will be merged recursively except for structs inside maps (because they are not addressable using Go reflection).

    if err := mergo.Merge(&dst, src); err != nil {
        // ...
    }

Additionally, you can map a map[string]interface{} to a struct (and otherwise, from struct to map), following the same restrictions as in Merge(). Keys are capitalized to find each corresponding exported field.

    if err := mergo.Map(&dst, srcMap); err != nil {
        // ...
    }

Warning: if you map a struct to map, it won't do it recursively. Don't expect Mergo to map struct members of your struct as map[string]interface{}. They will be just assigned as values.

More information and examples in [godoc documentation](http://godoc.org/github.com/imdario/mergo).

Note: if test are failing due missing package, please execute:

    go get gopkg.in/yaml.v1

## Contact me

If I can help you, you have an idea or you are using Mergo in your projects, don't hesitate to drop me a line (or a pull request): [@im_dario](https://twitter.com/im_dario)

## About

Written by [Dario Castañé](http://dario.im).

## License

[BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) license, as [Go language](http://golang.org/LICENSE).
# YAML support for the Go language

Introduction
------------

The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within [Canonical](https://www.canonical.com) as
part of the [juju](https://juju.ubuntu.com) project, and is based on a
pure Go port of the well-known [libyaml](http://pyyaml.org/wiki/LibYAML)
C library to parse and generate YAML data quickly and reliably.

Compatibility
-------------

The yaml package is almost compatible with YAML 1.1, including support for
anchors, tags, etc. There are still a few missing bits, such as document
merging, base-60 floats (huh?), and multi-document unmarshalling. These
features are not hard to add, and will be introduced as necessary.

Installation and usage
----------------------

The import path for the package is *gopkg.in/yaml.v1*.

To install it, run:

    go get gopkg.in/yaml.v1

API documentation
-----------------

If opened in a browser, the import path itself leads to the API documentation:

  * [https://gopkg.in/yaml.v1](https://gopkg.in/yaml.v1)

API stability
-------------

The package API for yaml v1 will remain stable as described in [gopkg.in](https://gopkg.in).


License
-------

The yaml package is licensed under the LGPL with an exception that allows it to be linked statically. Please see the LICENSE file for details.


Example
-------

```Go
package main

import (
        "fmt"
        "log"

        "gopkg.in/yaml.v1"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

type T struct {
        A string
        B struct{C int; D []int ",flow"}
}

func main() {
        t := T{}
    
        err := yaml.Unmarshal([]byte(data), &t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t:\n%v\n\n", t)
    
        d, err := yaml.Marshal(&t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t dump:\n%s\n\n", string(d))
    
        m := make(map[interface{}]interface{})
    
        err = yaml.Unmarshal([]byte(data), &m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)
    
        d, err = yaml.Marshal(&m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m dump:\n%s\n\n", string(d))
}
```

This example will generate the following output:

```
--- t:
{Easy! {2 [3 4]}}

--- t dump:
a: Easy!
b:
  c: 2
  d: [3, 4]


--- m:
map[a:Easy! b:map[c:2 d:[3 4]]]

--- m dump:
a: Easy!
b:
  c: 2
  d:
  - 3
  - 4
```

# Miniredis

Pure Go Redis test server, used in Go unittests.


##

Sometimes you want to test code which uses Redis, without making it a full-blown
integration test.
Miniredis implements (parts of) the Redis server, to be used in unittests. It
enables a simple, cheap, in-memory, Redis replacement, with a real TCP interface. Think of it as the Redis version of `net/http/httptest`.

It saves you from using mock code, and since the redis server lives in the
test process you can query for values directly, without going through the server
stack.

There are no dependencies on external binaries, so you can easily integrate it in automated build processes.

## 1.0.0 incompatiliby notice

2.0.0 improves TTLs to be `time.Duration` values. `.Expire()` is removed and
replaced by `.TTL()`, which returns the TTL as a `time.Duration`.
This should be the change needed to upgrade:

1.0.0:

    m.Expire() == 4
   
2.0.0:

    m.TTL() == 4 * time.Second

Furthermore, `.SetTime()` is added to help with `EXPIREAT` commands, and `.FastForward()` is introduced to test keys expiration.


## Commands

Implemented commands:

 - Connection (complete)
   - AUTH -- see RequireAuth()
   - ECHO
   - PING
   - SELECT
   - QUIT
 - Key 
   - DEL
   - EXISTS
   - EXPIRE
   - EXPIREAT
   - KEYS
   - MOVE
   - PERSIST
   - PEXPIRE
   - PEXPIREAT
   - PTTL
   - RENAME
   - RENAMENX
   - RANDOMKEY -- call math.rand.Seed(...) once before using.
   - TTL
   - TYPE
   - SCAN
 - Transactions (complete)
   - DISCARD
   - EXEC
   - MULTI
   - UNWATCH
   - WATCH
 - Server
   - DBSIZE
   - FLUSHALL
   - FLUSHDB
 - String keys (complete)
   - APPEND
   - BITCOUNT
   - BITOP
   - BITPOS
   - DECR
   - DECRBY
   - GET
   - GETBIT
   - GETRANGE
   - GETSET
   - INCR
   - INCRBY
   - INCRBYFLOAT
   - MGET
   - MSET
   - MSETNX
   - PSETEX
   - SET
   - SETBIT
   - SETEX
   - SETNX
   - SETRANGE
   - STRLEN
 - Hash keys (complete)
   - HDEL
   - HEXISTS
   - HGET
   - HGETALL
   - HINCRBY
   - HINCRBYFLOAT
   - HKEYS
   - HLEN
   - HMGET
   - HMSET
   - HSET
   - HSETNX
   - HVALS
   - HSCAN
 - List keys (complete)
   - BLPOP
   - BRPOP
   - BRPOPLPUSH
   - LINDEX
   - LINSERT
   - LLEN
   - LPOP
   - LPUSH
   - LPUSHX
   - LRANGE
   - LREM
   - LSET
   - LTRIM
   - RPOP
   - RPOPLPUSH
   - RPUSH
   - RPUSHX
 - Set keys (complete)
   - SADD
   - SCARD
   - SDIFF
   - SDIFFSTORE
   - SINTER
   - SINTERSTORE
   - SISMEMBER
   - SMEMBERS
   - SMOVE
   - SPOP -- call math.rand.Seed(...) once before using.
   - SRANDMEMBER -- call math.rand.Seed(...) once before using.
   - SREM
   - SUNION
   - SUNIONSTORE
   - SSCAN
 - Sorted Set keys (complete)
   - ZADD
   - ZCARD
   - ZCOUNT
   - ZINCRBY
   - ZINTERSTORE
   - ZLEXCOUNT
   - ZRANGE
   - ZRANGEBYLEX
   - ZRANGEBYSCORE
   - ZRANK
   - ZREM
   - ZREMRANGEBYLEX
   - ZREMRANGEBYRANK
   - ZREMRANGEBYSCORE
   - ZREVRANGE
   - ZREVRANGEBYSCORE
   - ZREVRANK
   - ZSCORE
   - ZUNIONSTORE
   - ZSCAN


Since miniredis is intended to be used in unittests TTLs don't decrease
automatically. You can use `TTL()` to get the TTL (as a time.Duration) of a
key. It will return 0 when no TTL is set. EXPIREAT and PEXPIREAT values will be
converted to a duration. For that you can either set m.SetTime(t) to use that
time as the base for the (P)EXPIREAT conversion, or don't call SetTime(), in
which case time.Now() will be used.
`m.FastForward(d)` can be used to decrement all TTLs. All TTLs which become <=
0 will be removed.

## Example

``` Go
func TestSomething(t *testing.T) {
	s, err := miniredis.Run()
	if err != nil {
		panic(err)
	}
	defer s.Close()

	// Optionally set some keys your code expects:
	s.Set("foo", "bar")
	s.HSet("some", "other", "key")

	// Run your code and see if it behaves.
	// An example using the redigo library from "github.com/garyburd/redigo/redis":
	c, err := redis.Dial("tcp", s.Addr())
	_, err = c.Do("SET", "foo", "bar")

	// Optionally check values in redis...
	if got, err := s.Get("foo"); err != nil || got != "bar" {
        t.Error("'foo' has the wrong value")
    }
    // ... or use a helper for that:
    s.CheckGet(t, "foo", "bar")

    // TTL and expiration:
    s.Set("foo", "bar")
    s.SetTTL("foo", 10 * time.Second)
    s.FastForward(11 * time.Second)
    if s.Exists("foo") {
        t.Fatal("'foo' should not have existed anymore")
    }
}
```

## Not supported

Commands which will probably not be implemented:

 - CLUSTER (all)
    - ~~CLUSTER *~~
    - ~~READONLY~~
    - ~~READWRITE~~
 - GEO (all) -- unless someone needs these
    - ~~GEOADD~~
    - ~~GEODIST~~
    - ~~GEOHASH~~
    - ~~GEOPOS~~
    - ~~GEORADIUS~~
    - ~~GEORADIUSBYMEMBER~~
 - HyperLogLog (all) -- unless someone needs these
    - ~~PFADD~~
    - ~~PFCOUNT~~
    - ~~PFMERGE~~
 - Key
    - ~~DUMP~~
    - ~~MIGRATE~~
    - ~~OBJECT~~
    - ~~RESTORE~~
    - ~~WAIT~~
 - Pub/Sub (all)
    - ~~PSUBSCRIBE~~
    - ~~PUBLISH~~
    - ~~PUBSUB~~
    - ~~PUNSUBSCRIBE~~
    - ~~SUBSCRIBE~~
    - ~~UNSUBSCRIBE~~
 - Scripting (all)
    - ~~EVAL~~
    - ~~EVALSHA~~
    - ~~SCRIPT *~~
 - Server
    - ~~BGSAVE~~
    - ~~BGWRITEAOF~~
    - ~~CLIENT *~~
    - ~~COMMAND *~~
    - ~~CONFIG *~~
    - ~~DEBUG *~~
    - ~~INFO~~
    - ~~LASTSAVE~~
    - ~~MONITOR~~
    - ~~ROLE~~
    - ~~SAVE~~
    - ~~SHUTDOWN~~
    - ~~SLAVEOF~~
    - ~~SLOWLOG~~
    - ~~SYNC~~
    - ~~TIME~~
    

## &c.

See https://github.com/alicebob/miniredis_vs_redis for tests comparing
miniredis against the real thing. Tests are run against Redis 3.2.5 (Debian).


[![Build Status](https://travis-ci.org/alicebob/miniredis.svg?branch=master)](https://travis-ci.org/alicebob/miniredis) 
[![GoDoc](https://godoc.org/github.com/alicebob/miniredis?status.svg)](https://godoc.org/github.com/alicebob/miniredis)
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

If you want to connect to local syslog (Ex. "/dev/log" or "/var/run/syslog" or "/var/run/log"). Just assign empty string to the first two parameters of `NewSyslogHook`. It should look like the following.

```go
import (
  "log/syslog"
  "github.com/Sirupsen/logrus"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
)

func main() {
  log       := logrus.New()
  hook, err := logrus_syslog.NewSyslogHook("", "", syslog.LOG_INFO, "")

  if err == nil {
    log.Hooks.Add(hook)
  }
}
```# Gorilla WebSocket

Gorilla WebSocket is a [Go](http://golang.org/) implementation of the
[WebSocket](http://www.rfc-editor.org/rfc/rfc6455.txt) protocol.

### Documentation

* [API Reference](http://godoc.org/github.com/gorilla/websocket)
* [Chat example](https://github.com/gorilla/websocket/tree/master/examples/chat)
* [File watch example](https://github.com/gorilla/websocket/tree/master/examples/filewatch)

### Status

The Gorilla WebSocket package provides a complete and tested implementation of
the [WebSocket](http://www.rfc-editor.org/rfc/rfc6455.txt) protocol. The
package API is stable.

### Installation

    go get github.com/gorilla/websocket

### Protocol Compliance

The Gorilla WebSocket package passes the server tests in the [Autobahn Test
Suite](http://autobahn.ws/testsuite) using the application in the [examples/autobahn
subdirectory](https://github.com/gorilla/websocket/tree/master/examples/autobahn).

### Gorilla WebSocket compared with other packages

<table>
<tr>
<th></th>
<th><a href="http://godoc.org/github.com/gorilla/websocket">gorilla</a></th>
<th><a href="http://godoc.org/code.google.com/p/go.net/websocket">go.net</a></th>
</tr>
<tr>
<tr><td colspan="3"><a href="http://tools.ietf.org/html/rfc6455">RFC 6455</a> Features</td></tr>
<tr><td>Passes <a href="http://autobahn.ws/testsuite/">Autobahn Test Suite</a></td><td><a href="https://github.com/gorilla/websocket/tree/master/examples/autobahn">Yes</a></td><td>No</td></tr>
<tr><td>Receive <a href="https://tools.ietf.org/html/rfc6455#section-5.4">fragmented</a> message<td>Yes</td><td><a href="https://code.google.com/p/go/issues/detail?id=7632">No</a>, see note 1</td></tr>
<tr><td>Send <a href="https://tools.ietf.org/html/rfc6455#section-5.5.1">close</a> message</td><td><a href="http://godoc.org/github.com/gorilla/websocket#hdr-Control_Messages">Yes</a></td><td><a href="https://code.google.com/p/go/issues/detail?id=4588">No</a></td></tr>
<tr><td>Send <a href="https://tools.ietf.org/html/rfc6455#section-5.5.2">pings</a> and receive <a href="https://tools.ietf.org/html/rfc6455#section-5.5.3">pongs</a></td><td><a href="http://godoc.org/github.com/gorilla/websocket#hdr-Control_Messages">Yes</a></td><td>No</td></tr>
<tr><td>Get the <a href="https://tools.ietf.org/html/rfc6455#section-5.6">type</a> of a received data message</td><td>Yes</td><td>Yes, see note 2</td></tr>
<tr><td colspan="3">Other Features</tr></td>
<tr><td>Limit size of received message</td><td><a href="http://godoc.org/github.com/gorilla/websocket#Conn.SetReadLimit">Yes</a></td><td><a href="https://code.google.com/p/go/issues/detail?id=5082">No</a></td></tr>
<tr><td>Read message using io.Reader</td><td><a href="http://godoc.org/github.com/gorilla/websocket#Conn.NextReader">Yes</a></td><td>No, see note 3</td></tr>
<tr><td>Write message using io.WriteCloser</td><td><a href="http://godoc.org/github.com/gorilla/websocket#Conn.NextWriter">Yes</a></td><td>No, see note 3</td></tr>
</table>

Notes: 

1. Large messages are fragmented in [Chrome's new WebSocket implementation](http://www.ietf.org/mail-archive/web/hybi/current/msg10503.html).
2. The application can get the type of a received data message by implementing
   a [Codec marshal](http://godoc.org/code.google.com/p/go.net/websocket#Codec.Marshal)
   function.
3. The go.net io.Reader and io.Writer operate across WebSocket frame boundaries.
  Read returns when the input buffer is full or a frame boundary is
  encountered, Each call to Write sends a single frame message. The Gorilla
  io.Reader and io.WriteCloser operate on a single WebSocket message.

# Chat Example

This application shows how to use use the
[websocket](https://github.com/gorilla/websocket) package and
[jQuery](http://jquery.com) to implement a simple web chat application.

## Running the example

The example requires a working Go development environment. The [Getting
Started](http://golang.org/doc/install) page describes how to install the
development environment.

Once you have Go up and running, you can download, build and run the example
using the following commands.

    $ go get github.com/gorilla/websocket
    $ cd `go list -f '{{.Dir}}' github.com/gorilla/websocket/examples/chat`
    $ go run *.go

# Test Server

This package contains a server for the [Autobahn WebSockets Test Suite](http://autobahn.ws/testsuite).

To test the server, run

    go run server.go

and start the client test driver

    wstest -m fuzzingclient -s fuzzingclient.json

When the client completes, it writes a report to reports/clients/index.html.
# File Watch example.

This example sends a file to the browser client for display whenever the file is modified.

    $ go get github.com/gorilla/websocket
    $ cd `go list -f '{{.Dir}}' github.com/gorilla/websocket/examples/filewatch`
    $ go run main.go <name of file to watch>
    # Open http://localhost:8080/ .
    # Modify the file to see it update in the browser.
go-metrics
==========

Go port of Coda Hale's Metrics library: <https://github.com/codahale/metrics>.

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
go metrics.Log(metrics.DefaultRegistry, 60e9, log.New(os.Stderr, "metrics: ", log.Lmicroseconds))
```

Periodically log every metric in slightly-more-parseable form to syslog:

```go
w, _ := syslog.Dial("unixgram", "/dev/log", syslog.LOG_INFO, "metrics")
go metrics.Syslog(metrics.DefaultRegistry, 60e9, w)
```

Periodically emit every metric to Graphite:

```go
addr, _ := net.ResolveTCPAddr("tcp", "127.0.0.1:2003")
go metrics.Graphite(metrics.DefaultRegistry, 10e9, "metrics", addr)
```

Periodically emit every metric into InfluxDB:

```go
import "github.com/rcrowley/go-metrics/influxdb"

go influxdb.Influxdb(metrics.DefaultRegistry, 10e9, &influxdb.Config{
    Host:     "127.0.0.1:8086",
    Database: "metrics",
    Username: "test",
    Password: "test",
})
```

Periodically upload every metric to Librato:

```go
import "github.com/rcrowley/go-metrics/librato"

go librato.Librato(metrics.DefaultRegistry,
    10e9,                  // interval
    "example@example.com", // account owner email address
    "token",               // Librato API token
    "hostname",            // source
    []float64{95},         // precentiles to send
    time.Millisecond,      // time unit
)
```

Periodically emit every metric to StatHat:

```go
import "github.com/rcrowley/go-metrics/stathat"

go stathat.Stathat(metrics.DefaultRegistry, 10e9, "example@example.com")
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
go-flags: a go library for parsing command line arguments
=========================================================

This library provides similar functionality to the builtin flag library of
go, but provides much more functionality and nicer formatting. From the
documentation:

Package flags provides an extensive command line option parser.
The flags package is similar in functionality to the go builtin flag package
but provides more options and uses reflection to provide a convenient and
succinct way of specifying command line options.

Supported features:
* Options with short names (-v)
* Options with long names (--verbose)
* Options with and without arguments (bool v.s. other type)
* Options with optional arguments and default values
* Multiple option groups each containing a set of options
* Generate and print well-formatted help message
* Passing remaining command line arguments after -- (optional)
* Ignoring unknown command line options (optional)
* Supports -I/usr/include -I=/usr/include -I /usr/include option argument specification
* Supports multiple short options -aux
* Supports all primitive go types (string, int{8..64}, uint{8..64}, float)
* Supports same option multiple times (can store in slice or last option counts)
* Supports maps
* Supports function callbacks

The flags package uses structs, reflection and struct field tags
to allow users to specify command line options. This results in very simple
and consise specification of your application options. For example:

    type Options struct {
        Verbose []bool `short:"v" long:"verbose" description:"Show verbose debug information"`
    }

This specifies one option with a short name -v and a long name --verbose.
When either -v or --verbose is found on the command line, a 'true' value
will be appended to the Verbose field. e.g. when specifying -vvv, the
resulting value of Verbose will be {[true, true, true]}.

Example:
--------
	var opts struct {
		// Slice of bool will append 'true' each time the option
		// is encountered (can be set multiple times, like -vvv)
		Verbose []bool `short:"v" long:"verbose" description:"Show verbose debug information"`

		// Example of automatic marshalling to desired type (uint)
		Offset uint `long:"offset" description:"Offset"`

		// Example of a callback, called each time the option is found.
		Call func(string) `short:"c" description:"Call phone number"`

		// Example of a required flag
		Name string `short:"n" long:"name" description:"A name" required:"true"`

		// Example of a value name
		File string `short:"f" long:"file" description:"A file" value-name:"FILE"`

		// Example of a pointer
		Ptr *int `short:"p" description:"A pointer to an integer"`

		// Example of a slice of strings
		StringSlice []string `short:"s" description:"A slice of strings"`

		// Example of a slice of pointers
		PtrSlice []*string `long:"ptrslice" description:"A slice of pointers to string"`

		// Example of a map
		IntMap map[string]int `long:"intmap" description:"A map from string to int"`
	}

	// Callback which will invoke callto:<argument> to call a number.
	// Note that this works just on OS X (and probably only with
	// Skype) but it shows the idea.
	opts.Call = func(num string) {
		cmd := exec.Command("open", "callto:"+num)
		cmd.Start()
		cmd.Process.Release()
	}

	// Make some fake arguments to parse.
	args := []string{
		"-vv",
		"--offset=5",
		"-n", "Me",
		"-p", "3",
		"-s", "hello",
		"-s", "world",
		"--ptrslice", "hello",
		"--ptrslice", "world",
		"--intmap", "a:1",
		"--intmap", "b:5",
		"arg1",
		"arg2",
		"arg3",
	}

	// Parse flags from `args'. Note that here we use flags.ParseArgs for
	// the sake of making a working example. Normally, you would simply use
	// flags.Parse(&opts) which uses os.Args
	args, err := flags.ParseArgs(&opts, args)

	if err != nil {
		panic(err)
		os.Exit(1)
	}

	fmt.Printf("Verbosity: %v\n", opts.Verbose)
	fmt.Printf("Offset: %d\n", opts.Offset)
	fmt.Printf("Name: %s\n", opts.Name)
	fmt.Printf("Ptr: %d\n", *opts.Ptr)
	fmt.Printf("StringSlice: %v\n", opts.StringSlice)
	fmt.Printf("PtrSlice: [%v %v]\n", *opts.PtrSlice[0], *opts.PtrSlice[1])
	fmt.Printf("IntMap: [a:%v b:%v]\n", opts.IntMap["a"], opts.IntMap["b"])
	fmt.Printf("Remaining args: %s\n", strings.Join(args, " "))

	// Output: Verbosity: [true true]
	// Offset: 5
	// Name: Me
	// Ptr: 3
	// StringSlice: [hello world]
	// PtrSlice: [hello world]
	// IntMap: [a:1 b:5]
	// Remaining args: arg1 arg2 arg3

More information can be found in the godocs: <http://godoc.org/github.com/jessevdk/go-flags>
# Logri

Logri is a wrapper for [Logrus](https://github.com/Sirupsen/logrus) that
provides **hierarchical, configurable, structured logging**. 

Like Logrus, it's a drop-in replacement for Go's standard logging library, but
it adds the ability to:

* Define loggers that inherit their log levels and output streams from parent loggers
* Configure loggers from a YAML file
* Update configuration on the fly
* Optionally watch a logging configuration file for changes

And, of course, it retains Logrus's excellent structured logging capabilities.

## Usage

You can drop Logri in to replace logging or Logrus very simply:

```go
package main


import (
        "github.com/Sirupsen/logrus"
    log "github.com/zenoss/logri"
)

func main() {

    log.Infof("Logri can replace the %s package", "logging")

    log.WithFields(logrus.Fields{
        "package": "logrus",
    }).Infof("Or another popular logging package")
}
```

### Named loggers

The power of Logri comes in with named hierarchical loggers. Use
`logri.GetLogger(name)` with a dotted name to return an individual logger that
inherits its log level and outputs from its parent, but can add or override its
own.

```go
package main

import (
    "github.com/Sirupsen/logrus"
    "github.com/zenoss/logri"
)

var (
    pkglog = logri.GetLogger("package")
    cmplog = logri.GetLogger("package.component")
    subcmplog = logri.GetLogger("package.component.subcomponent")
)

func main() {

    pkglog.SetLevel(logrus.DebugLevel, true) // Second argument makes it inherited
    // package.component and package.component.subcomponent are also Debug level now

    // Quiet package.component down but leave subcomponent at debug
    cmplog.SetLevel(logrus.ErrorLevel, false) // Second argument false means
                                              // local to this logger only
}
```

Further calls to `logri.GetLogger(name)` will retrieve the same logger
instance, so there's no need to jump through hoops exporting loggers to share
them among packages.

### Configuration via file

You can also configure Logri using a YAML file. Given a file `/etc/logging.conf`
with these contents:

```yaml
- logger: '*'
  level: debug
  out:
  - type: stderr
  - type: file
    options:
      file: /var/log/app.log
- logger: package
  level: warn
  local: true
  out:
  - type: file
    local: true
    options:
      file: /var/log/package.warn.log
- logger: package.component
  level: error
  out:
  - type: file
    options:
      file: /var/log/package.component.error.log
```

You can configure the loggers defined above very simply:

```go
logri.ApplyConfigFromFile("/etc/logging.conf")
```

That can be called at any time, and it will reconfigure loggers to match the
config at that time, with no need to restart or recreate loggers.

You can also watch that file for changes, rather than listening for a signal to
reload logging config:

```go
package main

import (
    "github.com/zenoss/logri"
)

func main() {

    // Start watching the logging config for changes
    go logri.WatchConfigFile("/etc/logging.conf")

    doStuff()
}
```websocket
=========

a clone of https://code.google.com/p/go.net/ with support for metering
glog
====

Leveled execution logs for Go.

This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package
	http://code.google.com/p/google-glog

By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control over logging at the file level.

The comment from glog.go introduces the ideas:

	Package glog implements logging analogous to the Google-internal
	C++ INFO/ERROR/V setup.  It provides functions Info, Warning,
	Error, Fatal, plus formatting variants such as Infof. It
	also provides V-style logging controlled by the -v and
	-vmodule=file=2 flags.
	
	Basic examples:
	
		glog.Info("Prepare to repel boarders")
	
		glog.Fatalf("Initialization failed: %s", err)
	
	See the documentation for the V function for an explanation
	of these examples:
	
		if glog.V(2) {
			glog.Info("Starting transaction...")
		}
	
		glog.V(2).Infoln("Processed", nItems, "elements")


The repository contains an open source version of the log package
used inside Google. The master copy of the source lives inside
Google, not here. The code in this repo is for export only and is not itself
under development. Feature requests will be ignored.

Send bug reports to golang-nuts@googlegroups.com.
