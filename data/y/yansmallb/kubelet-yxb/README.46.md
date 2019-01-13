## libcontainer - reference implementation for containers [![Build Status](https://jenkins.dockerproject.org/buildStatus/icon?job=Libcontainer%20Master)](https://jenkins.dockerproject.org/job/Libcontainer%20Master/)

Libcontainer provides a native Go implementation for creating containers
with namespaces, cgroups, capabilities, and filesystem access controls.
It allows you to manage the lifecycle of the container performing additional operations
after the container is created.


#### Container
A container is a self contained execution environment that shares the kernel of the
host system and which is (optionally) isolated from other containers in the system.

#### Using libcontainer

To create a container you first have to initialize an instance of a factory
that will handle the creation and initialization for a container.

Because containers are spawned in a two step process you will need to provide
arguments to a binary that will be executed as the init process for the container.
To use the current binary that is spawning the containers and acting as the parent
you can use `os.Args[0]` and we have a command called `init` setup.

```go
root, err := libcontainer.New("/var/lib/container", libcontainer.InitArgs(os.Args[0], "init"))
if err != nil {
    log.Fatal(err)
}
```

Once you have an instance of the factory created we can create a configuration
struct describing how the container is to be created.  A sample would look similar to this:

```go
config := &configs.Config{
    Rootfs: rootfs,
    Capabilities: []string{
        "CHOWN",
        "DAC_OVERRIDE",
        "FSETID",
        "FOWNER",
        "MKNOD",
        "NET_RAW",
        "SETGID",
        "SETUID",
        "SETFCAP",
        "SETPCAP",
        "NET_BIND_SERVICE",
        "SYS_CHROOT",
        "KILL",
        "AUDIT_WRITE",
    },
    Namespaces: configs.Namespaces([]configs.Namespace{
        {Type: configs.NEWNS},
        {Type: configs.NEWUTS},
        {Type: configs.NEWIPC},
        {Type: configs.NEWPID},
        {Type: configs.NEWNET},
    }),
    Cgroups: &configs.Cgroup{
        Name:            "test-container",
        Parent:          "system",
        AllowAllDevices: false,
        AllowedDevices:  configs.DefaultAllowedDevices,
    },

    Devices:  configs.DefaultAutoCreatedDevices,
    Hostname: "testing",
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
            Hard: uint64(1024),
            Soft: uint64(1024),
        },
    },
}
```

Once you have the configuration populated you can create a container:

```go
container, err := root.Create("container-id", config)
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
    log.Fatal(err)
}

// wait for the process to finish.
status, err := process.Wait()
if err != nil {
    log.Fatal(err)
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
```


#### nsinit

`nsinit` is a cli application which demonstrates the use of libcontainer.
It is able to spawn new containers or join existing containers.  A root
filesystem must be provided for use along with a container configuration file.

To build `nsinit`, run `make binary`. It will save the binary into
`bundles/nsinit`.

To use `nsinit`, cd into a Linux rootfs and copy a `container.json` file into
the directory with your specified configuration. Environment, networking,
and different capabilities for the container are specified in this file.
The configuration is used for each process executed inside the container.

See the `sample_configs` folder for examples of what the container configuration should look like.

To execute `/bin/bash` in the current directory as a container just run the following **as root**:
```bash
nsinit exec --tty /bin/bash
```

If you wish to spawn another process inside the container while your
current bash session is running, run the same command again to
get another bash shell (or change the command).  If the original
process (PID 1) dies, all other processes spawned inside the container
will be killed and the namespace will be removed.

You can identify if a process is running in a container by
looking to see if `state.json` is in the root of the directory.

You may also specify an alternate root place where
the `container.json` file is read and where the `state.json` file will be saved.


#### Checkpoint & Restore

libcontainer now integrates [CRIU](http://criu.org/) for checkpointing and restoring containers.
This let's you save the state of a process running inside a container to disk, and then restore
that state into a new process, on the same machine or on another machine.

`criu` version 1.5.2 or higher is required to use checkpoint and restore.
If you don't already  have `criu` installed, you can build it from source, following the
[online instructions](http://criu.org/Installation). `criu` is also installed in the docker image
generated when building libcontainer with docker.

To try an example with `nsinit`, open two terminals to the same busybox directory.
In the first terminal, run a command like this one:
```bash
nsinit exec -- sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
```

You should see logs printing to the terminal every second. Now, in the second terminal, run:
```bash
nsinit checkpoint --image-path=/tmp/criu
```

The logs in your first terminal will stop and the process will exit. Finally, in the second
terminal, run the restore command:
```bash
nsinit restore --image-path=/tmp/criu
```

The process will resume counting where it left off and printing to the new terminal window.


#### Future
See the [roadmap](ROADMAP.md).

## Copyright and license

Code and documentation copyright 2014 Docker, inc. Code released under the Apache 2.0 license.
Docs released under Creative commons.

## Hacking on libcontainer

First of all, please familiarise yourself with the [libcontainer Principles](PRINCIPLES.md).

If you're a *contributor* or aspiring contributor, you should read the [Contributors' Guide](CONTRIBUTING.md).

If you're a *maintainer* or aspiring maintainer, you should read the [Maintainers' Guide](MAINTAINERS_GUIDE.md) and
"How can I become a maintainer?" in the Contributors' Guide.
# go-systemd

Go bindings to systemd. The project has three packages:

- activation - for writing and using socket activation from Go
- journal - for writing to systemd's logging service, journal
- dbus - for starting/stopping/inspecting running services and units

Go docs for the entire project are here:

http://godoc.org/github.com/coreos/go-systemd

## Socket Activation

An example HTTP server using socket activation can be quickly setup by
following this README on a Linux machine running systemd:

https://github.com/coreos/go-systemd/tree/master/examples/activation/httpserver

## Journal

Using this package you can submit journal entries directly to systemd's journal taking advantage of features like indexed key/value pairs for each log entry.

## D-Bus

The D-Bus API lets you start, stop and introspect systemd units. The API docs are here:

http://godoc.org/github.com/coreos/go-systemd/dbus

### Debugging

Create `/etc/dbus-1/system-local.conf` that looks like this:

```
<!DOCTYPE busconfig PUBLIC
"-//freedesktop//DTD D-Bus Bus Configuration 1.0//EN"
"http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>
    <policy user="root">
        <allow eavesdrop="true"/>
        <allow eavesdrop="true" send_destination="*"/>
    </policy>
</busconfig>
```
## socket activated http server

This is a simple example of using socket activation with systemd to serve a
simple HTTP server on http://127.0.0.1:8076

To try it out `go get` the httpserver and run it under the systemd-activate helper

```
export GOPATH=`pwd`
go get github.com/coreos/go-systemd/examples/activation/httpserver
sudo /usr/lib/systemd/systemd-activate -l 127.0.0.1:8076 ./bin/httpserver
```

Then curl the URL and you will notice that it starts up:

```
curl 127.0.0.1:8076
hello socket activated world!
```
Go support for Protocol Buffers - Google's data interchange format
Copyright 2010 The Go Authors.
https://github.com/golang/protobuf

This package and the code it generates requires at least Go 1.2.

This software implements Go bindings for protocol buffers.  For
information about protocol buffers themselves, see
	https://developers.google.com/protocol-buffers/
To use this software, you must first install the standard C++
implementation of protocol buffers from
	https://developers.google.com/protocol-buffers/
And of course you must also install the Go compiler and tools from
	https://golang.org/
See
	https://golang.org/doc/install
for details or, if you are using gccgo, follow the instructions at
	https://golang.org/doc/install/gccgo

This software has two parts: a 'protocol compiler plugin' that
generates Go source files that, once compiled, can access and manage
protocol buffers; and a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers.

There is no support for RPC in Go using protocol buffers.  It may come
once a standard RPC protocol develops for protobufs.

There are no insertion points in the plugin.

To install this code:

The simplest way is to run go get.

	# Grab the code from the repository and install the proto package.
	go get -u github.com/golang/protobuf/{proto,protoc-gen-go}

The compiler plugin, protoc-gen-go, will be installed in $GOBIN,
defaulting to $GOPATH/bin.  It must be in your $PATH for the protocol
compiler, protoc, to find it.

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
  - Marshal and Unmarshal are functions to encode and decode the wire format.

Consider file test.proto, containing

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

To create and play with a Test object from the example package,

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

Please note that the API is considered unstable for now and may change without
further notice.

### License

go.dbus is available under the Simplified BSD License; see LICENSE for the full
text.

Nearly all of the credit for this library goes to github.com/guelfey/go.dbus.
[![Build Status](https://travis-ci.org/codegangsta/cli.png?branch=master)](https://travis-ci.org/codegangsta/cli)

# cli.go
cli.go is simple, fast, and fun package for building command line apps in Go. The goal is to enable developers to write fast and distributable command line applications in an expressive way.

You can view the API docs here:
http://godoc.org/github.com/codegangsta/cli

## Overview
Command line apps are usually so tiny that there is absolutely no reason why your code should *not* be self-documenting. Things like generating help text and parsing command flags/options should not hinder productivity when writing a command line app.

This is where cli.go comes into play. cli.go makes command line programming fun, organized, and expressive!

## Installation
Make sure you have a working Go environment (go 1.1 is *required*). [See the install instructions](http://golang.org/doc/install.html).

To install cli.go, simply run:
```
$ go get github.com/codegangsta/cli
```

Make sure your PATH includes to the `$GOPATH/bin` directory so your commands can be easily used:
```
export PATH=$PATH:$GOPATH/bin
```

## Getting Started
One of the philosophies behind cli.go is that an API should be playful and full of discovery. So a cli.go app can be as little as one line of code in `main()`. 

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

``` go
/* greet.go */
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

cli.go also generates some bitchass help text:
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
You can lookup arguments by calling the `Args` function on cli.Context.

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
  cli.StringFlag{Name: "lang", Value: "english", Usage: "language for the greeting"},
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

#### Alternate Names

You can set alternate (or short) names for flags by providing a comma-delimited list for the Name. e.g.

``` go
app.Flags = []cli.Flag {
  cli.StringFlag{Name: "lang, l", Value: "english", Usage: "language for the greeting"},
}
```

That flag can then be set with `--lang spanish` or `-l spanish`. Note that giving two different forms of the same flag in the same command invocation is an error.

### Subcommands

Subcommands can be defined for a more git-like command line app.
```go
...
app.Commands = []cli.Command{
  {
    Name:      "add",
    ShortName: "a",
    Usage:     "add a task to the list",
    Action: func(c *cli.Context) {
      println("added task: ", c.Args().First())
    },
  },
  {
    Name:      "complete",
    ShortName: "c",
    Usage:     "complete a task on the list",
    Action: func(c *cli.Context) {
      println("completed task: ", c.Args().First())
    },
  },
  {
    Name:      "template",
    ShortName: "r",
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

You can enable completion commands by setting the EnableBashCompletion
flag on the App object.  By default, this setting will only auto-complete to
show an app's subcommands, but you can write your own completion methods for
the App or its subcommands.
```go
...
var tasks = []string{"cook", "clean", "laundry", "eat", "sleep", "code"}
app := cli.NewApp()
app.EnableBashCompletion = true
app.Commands = []cli.Command{
  {
    Name: "complete",
    ShortName: "c",
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
        println(t)
      }
    },
  }
}
...
```

#### To Enable

Source the autocomplete/bash_autocomplete file in your .bashrc file while
setting the PROG variable to the name of your program:

`PROG=myprogram source /.../cli/autocomplete/bash_autocomplete`


## About
cli.go is written by none other than the [Code Gangsta](http://codegangsta.io)
## nsinit

`nsinit` is a cli application which demonstrates the use of libcontainer.
It is able to spawn new containers or join existing containers. 

### How to build?

First add the `libcontainer/vendor` into your GOPATH. It's because libcontainer
vendors all its dependencies, so it can be built predictably.

```
export GOPATH=$GOPATH:/your/path/to/libcontainer/vendor
```

Then get into the nsinit folder and get the imported file. Use `make` command
to make the nsinit binary.

```
cd libcontainer/nsinit
go get
make
```

We have finished compiling the nsinit package, but a root filesystem must be
provided for use along with a container configuration file.

Choose a proper place to run your container. For example we use `/busybox`.

```
mkdir /busybox 
curl -sSL 'https://github.com/jpetazzo/docker-busybox/raw/buildroot-2014.11/rootfs.tar' | tar -xC /busybox
```

Then you may need to write a configuration file named `container.json` in the
`/busybox` folder. Environment, networking, and different capabilities for
the container are specified in this file. The configuration is used for each
process executed inside the container.

See the `sample_configs` folder for examples of what the container configuration
should look like.

```
cp libcontainer/sample_configs/minimal.json /busybox/container.json
cd /busybox
```

You can customize `container.json` per your needs. After that, nsinit is
ready to work.

To execute `/bin/bash` in the current directory as a container just run the
following **as root**:

```bash
nsinit exec --tty --config container.json /bin/bash
```

If you wish to spawn another process inside the container while your current
bash session is running, run the same command again to get another bash shell
(or change the command).  If the original process (PID 1) dies, all other
processes spawned inside the container will be killed and the namespace will
be removed.

You can identify if a process is running in a container by looking to see if
`state.json` is in the root of the directory.
   
You may also specify an alternate root directory from where the `container.json`
file is read and where the `state.json` file will be saved.

### How to use?

Currently nsinit has 9 commands. Type `nsinit -h` to list all of them.
And for every alternative command, you can also use `--help` to get more
detailed help documents. For example, `nsinit config --help`.

`nsinit` cli application is implemented using [cli.go](https://github.com/codegangsta/cli).
Lots of details are handled in cli.go, so the implementation of `nsinit` itself
is very clean and clear.

*   **config**	
It will generate a standard configuration file for a container.  By default, it
will generate as the template file in [config.go](https://github.com/docker/libcontainer/blob/f28dff5539855bac2adbc5699f57f84349605b5f/nsinit/config.go#L234). 
It will modify the template if you have specified some configuration by options.
*   **exec**	
Starts a container and execute a new command inside it. Besides common options, it
has some special options as below.
	- `--tty,-t`: allocate a TTY to the container.
	- `--config`: you can specify a configuration file. By default, it will use
	template configuration.
	- `--id`: specify the ID for a container. By default, the id is "nsinit".
	- `--user,-u`: set the user, uid, and/or gid for the process. By default the
	value is "root".
	- `--cwd`: set the current working dir.
	- `--env`: set environment variables for the process.
*   **init**		
It's an internal command that is called inside the container's namespaces to
initialize the namespace and exec the user's process. It should not be called
externally.
*   **oom**		
Display oom notifications for a container, you should specify container id.
*   **pause**	
Pause the container's processes, you should specify container id. It will use
cgroup freeze subsystem to help.
*   **unpause**		
Unpause the container's processes. Same with `pause`.
*   **stats**	
Display statistics for the container, it will mainly show cgroup and network
statistics.
*   **state**	
Get the container's current state. You can also read the state from `state.json`
in your container_id folder.
*   **checkpoint**
Checkpoint a running container. You can read [this](http://criu.org/Advanced_usage)
for more detailed information about options.
	- `--id`： specify the ID for a container. By default, the id is "nsinit".
	- `--image-path`： path for saving criu image files. You must specify this option.
	- `--work-path`: path for saving work files and logs. By default it will
	generate a folder named "criu.work" in root directory.
	- `--leave-running`: leave the process running after checkpointing.
	- `--tcp-established`: allow open tcp connections.
	- `--ext-unix-sk`: allow external unix sockets.
	- `--shell-job`: allow shell jobs.
	- `--page-server`: ADDRESS:PORT of the page server. The dump image can be
	sent to a criu page server if we have a page server.
*   **restore**
Restore a container from a previous checkpoint. Options are almost the same
with checkpoint and `--image-path` must be specified.
*   **help, h**		
Shows a list of commands or help for one command.
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
These configuration files can be used with `nsinit` to quickly develop, test,
and experiment with features of libcontainer.

When consuming these configuration files, copy them into your rootfs and rename
the file to `container.json` for use with `nsinit`.
