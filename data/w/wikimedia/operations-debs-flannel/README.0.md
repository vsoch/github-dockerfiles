## Doing a release

To do a release, e.g. version 0.5.0, do the following steps.
This assumes that the remote that's hosting the project (i.e. https://github.com/coreos/flannel) is named "upstream".

```
VER=0.5.0
cd ./dist`

# Make two commits: v0.5.0 and v0.5.0+git; create a tag v0.5.0; push commits and tags to $ORIGIN
ORIGIN=upstream ./bump-release.sh $VER

# Build docker, ACI images and tarball
./build-release.sh $VER

# Publish to quay.io (credentials required)
./publish.sh $VER
```
go-ini
======

INI parsing library for Go (golang).

View the API documentation [here](http://godoc.org/github.com/vaughan0/go-ini).

Usage
-----

Parse an INI file:

```go
import "github.com/vaughan0/go-ini"

file, err := ini.LoadFile("myfile.ini")
```

Get data from the parsed file:

```go
name, ok := file.Get("person", "name")
if !ok {
  panic("'name' variable missing from 'person' section")
}
```

Iterate through values in a section:

```go
for key, value := range file["mysection"] {
  fmt.Printf("%s => %s\n", key, value)
}
```

Iterate through sections in a file:

```go
for name, section := range file {
  fmt.Printf("Section name: %s\n", name)
}
```

File Format
-----------

INI files are parsed by go-ini line-by-line. Each line may be one of the following:

  * A section definition: [section-name]
  * A property: key = value
  * A comment: #blahblah _or_ ;blahblah
  * Blank. The line will be ignored.

Properties defined before any section headers are placed in the default section, which has
the empty string as it's key.

Example:

```ini
# I am a comment
; So am I!

[apples]
colour = red or green
shape = applish

[oranges]
shape = square
colour = blue
```
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
mux
===
[![Build Status](https://travis-ci.org/gorilla/mux.png?branch=master)](https://travis-ci.org/gorilla/mux)

gorilla/mux is a powerful URL router and dispatcher.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/mux
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

gorilla/context is a general purpose registry for global request variables.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
# netns - network namespaces in go #

The netns package provides an ultra-simple interface for handling
network namespaces in go. Changing namespaces requires elevated
privileges, so in most cases this code needs to be run as root.

## Local Build and Test ##

You can use go get command:

    go get github.com/vishvananda/netns

Testing (requires root):

    sudo -E go test github.com/vishvananda/netns

## Example ##

```go
package main

import (
    "net"
    "runtime"
    "github.com/vishvananada/netns"
)

func main() {
    // Lock the OS Thread so we don't accidentally switch namespaces
    runtime.LockOSThread()
    defer runtime.UnlockOSThread()

    // Save the current network namespace
    origns, _ := netns.Get()
    defer origns.Close()

    // Create a new network namespace
    newns, _ := netns.New()
    defer newns.Close()

    // Do something with tne network namespace
    ifaces, _ := net.Interfaces()
    fmt.Printf("Interfaces: %v\n", ifaces)

    // Switch back to the original namespace
    netns.Set(origns)
}

```
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
