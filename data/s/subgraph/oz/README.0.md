# go-acl

Golang POSIX.1e ACL bindings.
Essentially bindings to /usr/include/sys/acl.h
## notes

### mac os x
Mac OS X does not seem to support basic POSIX1.e ACLs. They do
provide the POSIX API for NFSv4 ACLs. It would be nice for this
package to also support NFSv4 ACLs.

### freebsd
By default, FreeBSD does not enable POSIX1.e ACLs on the root
partition. To enable them, reboot into single-user mode and execute:

    $ tunefs -a enable
    $ reboot

Source: https://www.freebsd.org/doc/handbook/fs-acl.html

## info

The IEEE POSIX.1e specification describes five security extensions to the base
POSIX.1 API: Access Control Lists (ACLs), Auditing, Capabilities,
Mandatory Access Control, and Information Flow Labels.
The specificaiton was abandoned before finalization, however most
UNIX-like operating systems have some form of ACL implementation.

Source: http://www.gsp.com/cgi-bin/man.cgi?section=3&topic=posix1e

## copying

Copyright (c) 2015 Joseph Naegele. See LICENSE file.

# Linux networking in Golang

**tenus** is a [Golang](http://golang.org/) package which allows you to configure and manage Linux network devices programmatically. It communicates with Linux Kernel via [netlink](http://man7.org/linux/man-pages/man7/netlink.7.html) to facilitate creation and configuration of network devices on the Linux host. The package also allows for more advanced network setups with Linux containers including [Docker](https://github.com/dotcloud/docker/).

**tenus** uses [runc](https://github.com/opencontainers/runc)'s implementation of **netlink** protocol. The package only works with newer Linux Kernels (3.10+) which are shipping reasonably new `netlink` protocol implementation, so **if you are running older kernel this package won't be of much use to you** I'm afraid. I have developed this package on Ubuntu [Trusty Tahr](http://releases.ubuntu.com/14.04/) which ships with 3.13+ and verified its functionality on [Precise Pangolin](http://releases.ubuntu.com/12.04/) with upgraded kernel to version 3.10. I could worked around the `netlink` issues by using `ioctl` syscalls, but I decided to prefer "pure netlink" implementation, so suck it old Kernels.

At the moment only functional tests are available, but the interface design should hopefully allow for easy (ish) unit testing in the future. I do appreciate that the package's **test coverage is not great at the moment**, but the core functionality should be covered. I would massively welcome PRs.

## Get started

There is a ```Vagrantfile``` available in the repo so using [vagrant](https://github.com/mitchellh/vagrant) is the easiest way to get started:

```bash
milosgajdos@bimbonet ~ $ git clone https://github.com/milosgajdos83/tenus.git
milosgajdos@bimbonet ~ $ vagrant up

```

**Note** using the provided ```Vagrantfile``` will take quite a long time to spin the VM as vagrant will setup Ubuntu Trusty VM with all the prerequisities: 

* it will install golang and docker onto the VM
* it will export ```GOPATH``` and ```go get``` the **tenus** package onto the VM
* it will also "**pull**" Docker ubuntu image so that you can run the tests once the VM is set up

At the moment running the tests require Docker to be installed, but in the future I'd love to separate tests per interface so that you can run only chosen test sets.

Once the VM is running, ```cd``` into particular repo directory and you can run the tests: 

```bash
milosgajdos@bimbonet ~ $ cd $GOPATH/src/github.com/milosgajdos83/tenus
milosgajdos@bimbonet ~ $ sudo go test
```

If you don't want to use the provided ```Vagrantfile```, you can simply run your own Linux VM (with 3.10+ kernel) and follow the regular golang development flow:

```bash
milosgajdos@bimbonet ~ $ go get github.com/milosgajdos83/tenus
milosgajdos@bimbonet ~ $ cd $GOPATH/src/github.com/milosgajdos83/tenus
milosgajdos@bimbonet ~ $ sudo go test
```

Once you've got the package and ran the tests (you don't need to run the tests!), you can start hacking. Below you can find simple code samples to get started with the package.

## Examples

Below you can find a few code snippets which can help you get started writing your own programs.

### New network bridge, add dummy link into it

The example below shows a simple program example which creates a new network bridge, a new dummy network link and adds it into the bridge.

```go
package main

import (
	"fmt"
	"log"

	"github.com/milosgajdos83/tenus"
)

func main() {
	// Create a new network bridge
	br, err := tenus.NewBridgeWithName("mybridge")
	if err != nil {
		log.Fatal(err)
	}

	// Bring the bridge up
	if err = br.SetLinkUp(); err != nil {
		fmt.Println(err)
	}

	// Create a dummy link
	dl, err := tenus.NewLink("mydummylink")
	if err != nil {
		log.Fatal(err)
	}

	// Add the dummy link into bridge
	if err = br.AddSlaveIfc(dl.NetInterface()); err != nil {
		log.Fatal(err)
	}

	// Bring the dummy link up
	if err = dl.SetLinkUp(); err != nil {
		fmt.Println(err)
	}
}
```

### New network bridge, veth pair, one peer in Docker

The example below shows how you can create a new network bride, configure its IP address, add a new veth pair and send one of the veth peers into Docker with a given name.

**!! You must make sure that particular Docker is runnig if you want the code sample below to work properly !!** So before you compile and run the program below you should create a particular docker with the below used name:

```bash
milosgajdos@bimbonet ~ $ docker run -i -t --rm --privileged -h vethdckr --name vethdckr ubuntu:14.04 /bin/bash
```

```go
package main

import (
	"fmt"
	"log"
	"net"

	"github.com/milosgajdos83/tenus"
)

func main() {
	// CREATE BRIDGE AND BRING IT UP
	br, err := tenus.NewBridgeWithName("vethbridge")
	if err != nil {
		log.Fatal(err)
	}

	brIp, brIpNet, err := net.ParseCIDR("10.0.41.1/16")
	if err != nil {
		log.Fatal(err)
	}

	if err := br.SetLinkIp(brIp, brIpNet); err != nil {
		fmt.Println(err)
	}

	if err = br.SetLinkUp(); err != nil {
		fmt.Println(err)
	}

	// CREATE VETH PAIR
	veth, err := tenus.NewVethPairWithOptions("myveth01", tenus.VethOptions{PeerName: "myveth02"})
	if err != nil {
		log.Fatal(err)
	}

	// ASSIGN IP ADDRESS TO THE HOST VETH INTERFACE
	vethHostIp, vethHostIpNet, err := net.ParseCIDR("10.0.41.2/16")
	if err != nil {
		log.Fatal(err)
	}

	if err := veth.SetLinkIp(vethHostIp, vethHostIpNet); err != nil {
		fmt.Println(err)
	}

	// ADD MYVETH01 INTERFACE TO THE MYBRIDGE BRIDGE
	myveth01, err := net.InterfaceByName("myveth01")
	if err != nil {
		log.Fatal(err)
	}

	if err = br.AddSlaveIfc(myveth01); err != nil {
		fmt.Println(err)
	}

	if err = veth.SetLinkUp(); err != nil {
		fmt.Println(err)
	}

	// PASS VETH PEER INTERFACE TO A RUNNING DOCKER BY PID
	pid, err := tenus.DockerPidByName("vethdckr", "/var/run/docker.sock")
	if err != nil {
		fmt.Println(err)
	}

	if err := veth.SetPeerLinkNsPid(pid); err != nil {
		log.Fatal(err)
	}

	// ALLOCATE AND SET IP FOR THE NEW DOCKER INTERFACE
	vethGuestIp, vethGuestIpNet, err := net.ParseCIDR("10.0.41.5/16")
	if err != nil {
		log.Fatal(err)
	}

	if err := veth.SetPeerLinkNetInNs(pid, vethGuestIp, vethGuestIpNet, nil); err != nil {
		log.Fatal(err)
	}
}
```

### Working with existing bridges and interfaces

The following examples show how to retrieve exisiting interfaces as a tenus link and bridge

```go
package main

import (
	"fmt"
	"log"
	"net"

	"github.com/milosgajdos83/tenus"
)

func main() {
	// RETRIEVE EXISTING BRIDGE
	br, err := tenus.BridgeFromName("bridge0")
	if err != nil {
		log.Fatal(err)
	}

	// REMOVING AN IP FROM A BRIDGE INTERFACE (BEFORE RECONFIGURATION)
	brIp, brIpNet, err := net.ParseCIDR("10.0.41.1/16")
	if err != nil {
		log.Fatal(err)
	}
	if err := br.UnsetLinkIp(brIp, brIpNet); err != nil {
		log.Fatal(err)
	}

	// RETRIEVE EXISTING INTERFACE
	dl, err := tenus.NewLinkFrom("eth0")
	if err != nil {
		log.Fatal(err)
	}

	// RENAMING AN INTERFACE BY NAME
	if err := tenus.RenameInterfaceByName("vethPSQSEl", "vethNEWNAME"); err != nil {
		log.Fatal(err)
	}

}
```

### VLAN and MAC VLAN interfaces

You can check out [VLAN](https://gist.github.com/milosgajdos83/9f68b1818dca886e9ae8) and [Mac VLAN](https://gist.github.com/milosgajdos83/296fb90d076f259a5b0a) examples, too.

### More examples

Repo contains few more code sample in ```examples``` folder so make sure to check them out if you're interested.

## TODO

This is just a rough beginning of the project which I put together over couple of weeks in my free time. I'd like to integrate this into my own Docker fork and test the advanced netowrking functionality with the core of Docker as oppose to configuring network interfaces from a separate golang program, because advanced networking in Docker was the main motivation for writing this package.

## Documentation

More in depth package documentation is available via [godoc](http://godoc.org/github.com/milosgajdos83/tenus)
# arping
  
arping is a native go library to ping a host per arp datagram, or query a host mac address 

The currently supported platforms are: Linux and BSD.
   

## Usage
### arping library

* import this library per `import "github.com/j-keck/arping"`
* export GOPATH if not already (`export GOPATH=$PWD`)
* download the library `go get`
* run it `sudo -E go run <YOUR PROGRAMM>` 
* or build it `go build`


The library requires raw socket access. So it must run as root, or with appropriate capabilities under linux: `sudo setcap cap_net_raw+ep <BIN>`.

For api doc and examples see: [godoc](http://godoc.org/github.com/j-keck/arping) or check the standalone under 'cmd/arping/main.go'.


    
### arping executable
   
To get a runnable pinger use `go get -u github.com/j-keck/arping/cmd/arping`. This will build the binary in $GOPATH/bin.

arping requires raw socket access. So it must run as root, or with appropriate capabilities under Linux: `sudo setcap cap_net_raw+ep <ARPING_PATH>`.

# gosecco - a library for parsing and managing seccomp-bpf rules

[![Build Status](https://travis-ci.org/twtiger/gosecco.svg?branch=master)](https://travis-ci.org/twtiger/gosecco)
[![Coverage Status](https://coveralls.io/repos/github/twtiger/gosecco/badge.svg?branch=master)](https://coveralls.io/github/twtiger/gosecco?branch=master)
[![GoDoc](https://godoc.org/github.com/twtiger/gosecco?status.svg)](https://godoc.org/github.com/twtiger/gosecco)

gosecco is a project to provide a full stack of tools necessary for working with SECCOMP BPF rules from Golang. The primary pieces of functionality are the parser and compiler - but the project also supports a rudimentary assembler and disassembler. It also supports an emulator that can be tweaked to provide output on whether your rules actually do what you think they should do or not. None of these tools are exposed as command line tools - they are meant to be used as libraries for higher level applications and systems.

gosecco is only compatible with Linux 3.7 and above. It has only been tested with Golang 1.6, and it assumes an amd64 architecture, although that is likely to change.

The language that gosecco parses and understands is documented in https://github.com/twtiger/gosecco/blob/master/docs/seccomp-policy-language.md.

## Libraries

gosecco is composed of several smaller libraries that provides different parts of the functionality. The gosecco package exposes the core functionality - see the godoc for more info: https://godoc.org/github.com/twtiger/gosecco.

The specific libraries used are these:

### asm

The asm package is mostly a self contained package that can be used to generate a simple form of BPF assembler, and read the same form of assembler into and out of slices of unix.SockFilter.

### checker

The checker package provides for type checking of a finished parse tree - but also makes sure that certain semantic constraints are fulfilled, such that there is not more than one rule for a specific syscall, or that all the syscalls referred actually exist.

### compiler

The compiler will take a parse tree and generate optimized BPF code in the form of a slice of unix.SockFilter - the intention is that the output of the compiler should be ready to install for a running program. The compiler doesn't implement many optimizations by itself, but it does try to be clever with jump layouts and so on. Simplification and normalization of the tree will already be done before the compiler starts working.

### constants

A helper package that contains many well known constants from the Linux environment, so that these are available to profiles written for seccomp.

### data

This package only contains the definition for the Seccomp Working memory data set, and is a helper package for the other packages.

### emulator

An emulator that takes a set of rules and an instance of working memory and executes the instructions therein. The emulation is extremely slow and obvious in order to make it easier to understand the implementation - this tool is primarily there as a basis for experiments and further evolution.

### parser

The parser is divided up into a tokenizer implemented using Ragel and a very simple recursive descent parser. The language parsed is described in the document referred to above. The output will be a raw policy document where macro definitions and rule definitions appear in the order they were defined.

### precompilation

The precompilation package contains some checks that make sure that everything is ready for being compiled. It doesn't provide error messages for users of packages, but for implementors. Basically speaking, if this ever triggers, it's because someone has wired something wrong.

### simplifier

The simplification phase takes a tree and tries to do as much optimization as possible before hand. This means basically reducing all arithmetic expressions as much as possible based on constants. We don't do more complicated optimizations such as reorderings or inversions of mathematical operations - we simple execute as much as possible beforehand. THe assumption is that there are no free variables or calls at this stage.

### tree

The tree defines the expression types and all subnodes of the AST. It also defines a Visitor that can be used to provide functionality on the AST.

### unifier

The unifier takes the set of rules and zero or more lists of macro definitions and resolves all free variables in the set of rules by replacing them with their macro content. The output will be a tree that is fit for simplification, type checking and compilation.

## Flow of execution

In general, this library will work by taking a file of definitions, parse it, compile it and install it. The specific flow of events looks like this:

- First, the file will be parsed
- Then, the unifier will take all the macro definitions and make sure the final tree is complete
- After that, the type checker will run to make sure everything looks correct
- Then, we use the simplifier to optimize and make everything smaller
- After simplification, the tree should be ready for compilation. The precompilation package checks that and ensures we are all good.
- Finally, the compiler takes the tree and turns it into bytecode
- Optionally, at this point we will install the bytecode into a running process using either the seccomp or the prctl system call.

The library can also check whether seccomp is supported. It supports the separation of macros and rules into several files. This composition cannot happen inside the files, but has to be done by the calling library. This allows for shared macros and rules. The language also supports default positive and negative actions, such that it's clear from the file itself whether it's a blacklist or a whitelist, for example. These default actions can also be specified programmatically. Finally, each rule can have custom positive or negative actions if needed.

Refer to the godoc for the API - we hope to have some usage examples up as soon as the library is finished.
Provides convenience functions for reading configuration and data files
according to the XDG Base Directory Specification:

http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

Install with

  go get github.com/BurntSushi/xdg

[![Coverage](http://gocover.io/_badge/github.com/codegangsta/cli?0)](http://gocover.io/github.com/codegangsta/cli)
[![Build Status](https://travis-ci.org/codegangsta/cli.svg?branch=master)](https://travis-ci.org/codegangsta/cli)
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
## Golang logging library

[![godoc](http://img.shields.io/badge/godoc-reference-blue.svg?style=flat)](https://godoc.org/github.com/op/go-logging) [![build](https://img.shields.io/travis/op/go-logging.svg?style=flat)](https://travis-ci.org/op/go-logging)

Package logging implements a logging infrastructure for Go. Its output format
is customizable and supports different logging backends like syslog, file and
memory. Multiple backends can be utilized with different log levels per backend
and logger.

## Example

Let's have a look at an [example](examples/example.go) which demonstrates most
of the features found in this library.

[![Example Output](examples/example.png)](examples/example.go)

```go
package main

import (
	"os"

	"github.com/op/go-logging"
)

var log = logging.MustGetLogger("example")

// Example format string. Everything except the message has a custom color
// which is dependent on the log level. Many fields have a custom output
// formatting too, eg. the time returns the hour down to the milli second.
var format = logging.MustStringFormatter(
	`%{color}%{time:15:04:05.000} %{shortfunc} ▶ %{level:.4s} %{id:03x}%{color:reset} %{message}`,
)

// Password is just an example type implementing the Redactor interface. Any
// time this is logged, the Redacted() function will be called.
type Password string

func (p Password) Redacted() interface{} {
	return logging.Redact(string(p))
}

func main() {
	// For demo purposes, create two backend for os.Stderr.
	backend1 := logging.NewLogBackend(os.Stderr, "", 0)
	backend2 := logging.NewLogBackend(os.Stderr, "", 0)

	// For messages written to backend2 we want to add some additional
	// information to the output, including the used log level and the name of
	// the function.
	backend2Formatter := logging.NewBackendFormatter(backend2, format)

	// Only errors and more severe messages should be sent to backend1
	backend1Leveled := logging.AddModuleLevel(backend1)
	backend1Leveled.SetLevel(logging.ERROR, "")

	// Set the backends to be used.
	logging.SetBackend(backend1Leveled, backend2Formatter)

	log.Debugf("debug %s", Password("secret"))
	log.Info("info")
	log.Notice("notice")
	log.Warning("warning")
	log.Error("err")
	log.Critical("crit")
}
```

## Installing

### Using *go get*

    $ go get github.com/op/go-logging

After this command *go-logging* is ready to use. Its source will be in:

    $GOROOT/src/pkg/github.com/op/go-logging

You can use `go get -u` to update the package.

## Documentation

For docs, see http://godoc.org/github.com/op/go-logging or run:

    $ godoc github.com/op/go-logging

## Additional resources

* [wslog](https://godoc.org/github.com/cryptix/go/logging/wslog) -- exposes log messages through a WebSocket.
# pty

Pty is a Go package for using unix pseudo-terminals.

## Install

    go get github.com/kr/pty

## Example

```go
package main

import (
	"github.com/kr/pty"
	"io"
	"os"
	"os/exec"
)

func main() {
	c := exec.Command("grep", "--color=auto", "bar")
	f, err := pty.Start(c)
	if err != nil {
		panic(err)
	}

	go func() {
		f.Write([]byte("foo\n"))
		f.Write([]byte("bar\n"))
		f.Write([]byte("baz\n"))
		f.Write([]byte{4}) // EOT
	}()
	io.Copy(os.Stdout, f)
}
```
