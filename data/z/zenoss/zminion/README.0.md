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
  cli.StringFlag{"lang", "english", "language for the greeting"},
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
  cli.StringFlag{"lang, l", "english", "language for the greeting"},
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
#go-dockerclient

[![Build Status](https://drone.io/github.com/fsouza/go-dockerclient/status.png)](https://drone.io/github.com/fsouza/go-dockerclient/latest)
[![Build Status](https://travis-ci.org/fsouza/go-dockerclient.png)](https://travis-ci.org/fsouza/go-dockerclient)

[![GoDoc](http://godoc.org/github.com/fsouza/go-dockerclient?status.png)](http://godoc.org/github.com/fsouza/go-dockerclient)

This package presents a client for the Docker remote API.

For more details, check the [remote API documentation](http://docs.docker.io/en/latest/reference/api/docker_remote_api/).

##Versioning

* Version 0.1 is compatible with Docker v0.7.1
* The master is compatible with Docker's master


## Example

    package main

    import (
            "fmt"
            "github.com/fsouza/go-dockerclient"
    )

    func main() {
            endpoint := "unix:///var/run/docker.sock"
            client, _ := docker.NewClient(endpoint)
            imgs, _ := client.ListImages(true)
            for _, img := range imgs {
                    fmt.Println("ID: ", img.ID)
                    fmt.Println("RepoTags: ", img.RepoTags)
                    fmt.Println("Created: ", img.Created)
                    fmt.Println("Size: ", img.Size)
                    fmt.Println("VirtualSize: ", img.VirtualSize)
                    fmt.Println("ParentId: ", img.ParentId)
                    fmt.Println("Repository: ", img.Repository)
            }
    }

## Developing

You can run the tests with:

    go get -d ./...
    go test ./...
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
