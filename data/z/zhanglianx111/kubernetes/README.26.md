## libcontainer - reference implementation for containers [![Build Status](https://ci.dockerproject.com/github.com/docker/libcontainer/status.svg?branch=master)](https://ci.dockerproject.com/github.com/docker/libcontainer) 

### Note on API changes:

Please bear with us while we work on making the libcontainer API stable and something that we can support long term.  We are currently discussing the API with the community, therefore, if you currently depend on libcontainer please pin your dependency at a specific tag or commit id.  Please join the discussion and help shape the API.

#### Background

libcontainer specifies configuration options for what a container is.  It provides a native Go implementation for using Linux namespaces with no external dependencies.  libcontainer provides many convenience functions for working with namespaces, networking, and management.  


#### Container
A container is a self contained execution environment that shares the kernel of the host system and which is (optionally) isolated from other containers in the system.

libcontainer may be used to execute a process in a container. If a user tries to run a new process inside an existing container, the new process is added to the processes executing in the container.


#### Root file system

A container runs with a directory known as its *root file system*, or *rootfs*, mounted as the file system root. The rootfs is usually a full system tree.


#### Configuration

A container is initially configured by supplying configuration data when the container is created.


#### nsinit

`nsinit` is a cli application which demonstrates the use of libcontainer.  It is able to spawn new containers or join existing containers, based on the current directory.

To use `nsinit`, cd into a Linux rootfs and copy a `container.json` file into the directory with your specified configuration. Environment, networking, and different capabilities for the container are specified in this file. The configuration is used for each process executed inside the container.
                                                                                                                               
See the `sample_configs` folder for examples of what the container configuration should look like.

To execute `/bin/bash` in the current directory as a container just run the following **as root**:
```bash
nsinit exec /bin/bash
```

If you wish to spawn another process inside the container while your current bash session is running, run the same command again to get another bash shell (or change the command).  If the original process (PID 1) dies, all other processes spawned inside the container will be killed and the namespace will be removed. 

You can identify if a process is running in a container by looking to see if `state.json` is in the root of the directory.
   
You may also specify an alternate root place where the `container.json` file is read and where the `state.json` file will be saved.

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
## nsenter

The `nsenter` package registers a special init constructor that is called before the Go runtime has 
a chance to boot.  This provides us the ability to `setns` on existing namespaces and avoid the issues
that the Go runtime has with multiple threads.  This constructor is only called if this package is 
registered, imported, in your go application and the argv 0 is `nsenter`.
These configuration files can be used with `nsinit` to quickly develop, test,
and experiment with features of libcontainer.

When consuming these configuration files, copy them into your rootfs and rename
the file to `container.json` for use with `nsinit`.
