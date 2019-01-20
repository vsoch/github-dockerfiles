This repository holds supplementary Go networking libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
The *.dat files in this directory are copied from The WebKit Open Source
Project, specifically $WEBKITROOT/LayoutTests/html5lib/resources.
WebKit is licensed under a BSD style license.
http://webkit.org/coding/bsd-license.html says:

Copyright (C) 2009 Apple Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY APPLE INC. AND ITS CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL APPLE INC. OR ITS CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

These test cases come from
http://www.w3.org/International/tests/repository/html5/the-input-byte-stream/results-basics

Distributed under both the W3C Test Suite License
(http://www.w3.org/Consortium/Legal/2008/04-testsuite-license)
and the W3C 3-clause BSD License
(http://www.w3.org/Consortium/Legal/2008/03-bsd-license).
To contribute to a W3C Test Suite, see the policies and contribution
forms (http://www.w3.org/2004/10/27-testcases).
This is a work-in-progress HTTP/2 implementation for Go.

It will eventually live in the Go standard library and won't require
any changes to your code to use.  It will just be automatic.

Status:

* The server support is pretty good. A few things are missing
  but are being worked on.
* The client work has just started but shares a lot of code
  is coming along much quicker.

Docs are at https://godoc.org/golang.org/x/net/http2

Demo test server at https://http2.golang.org/

Help & bug reports welcome!

Contributing: https://golang.org/doc/contribute.html
Bugs:         https://golang.org/issue/new?title=x/net/http2:+
# h2i

**h2i** is an interactive HTTP/2 ("h2") console debugger. Miss the good ol'
days of telnetting to your HTTP/1.n servers? We're bringing you
back.

Features:
- send raw HTTP/2 frames
 - PING
 - SETTINGS
 - HEADERS
 - etc
- type in HTTP/1.n and have it auto-HPACK/frame-ify it for HTTP/2
- pretty print all received HTTP/2 frames from the peer (including HPACK decoding)
- tab completion of commands, options

Not yet features, but soon:
- unnecessary CONTINUATION frames on short boundaries, to test peer implementations 
- request bodies (DATA frames)
- send invalid frames for testing server implementations (supported by underlying Framer)

Later:
- act like a server

## Installation

```
$ go get golang.org/x/net/http2/h2i
$ h2i <host>
```

## Demo

```
$ h2i
Usage: h2i <hostname>
  
  -insecure
        Whether to skip TLS cert validation
  -nextproto string
        Comma-separated list of NPN/ALPN protocol names to negotiate. (default "h2,h2-14")

$ h2i google.com
Connecting to google.com:443 ...
Connected to 74.125.224.41:443
Negotiated protocol "h2-14"
[FrameHeader SETTINGS len=18]
  [MAX_CONCURRENT_STREAMS = 100]
  [INITIAL_WINDOW_SIZE = 1048576]
  [MAX_FRAME_SIZE = 16384]
[FrameHeader WINDOW_UPDATE len=4]
  Window-Increment = 983041
  
h2i> PING h2iSayHI
[FrameHeader PING flags=ACK len=8]
  Data = "h2iSayHI"
h2i> headers
(as HTTP/1.1)> GET / HTTP/1.1
(as HTTP/1.1)> Host: ip.appspot.com
(as HTTP/1.1)> User-Agent: h2i/brad-n-blake
(as HTTP/1.1)>  
Opening Stream-ID 1:
 :authority = ip.appspot.com
 :method = GET
 :path = /
 :scheme = https
 user-agent = h2i/brad-n-blake
[FrameHeader HEADERS flags=END_HEADERS stream=1 len=77]
  :status = "200"
  alternate-protocol = "443:quic,p=1"
  content-length = "15"
  content-type = "text/html"
  date = "Fri, 01 May 2015 23:06:56 GMT"
  server = "Google Frontend"
[FrameHeader DATA flags=END_STREAM stream=1 len=15]
  "173.164.155.78\n"
[FrameHeader PING len=8]
  Data = "\x00\x00\x00\x00\x00\x00\x00\x00"
h2i> ping  
[FrameHeader PING flags=ACK len=8]  
  Data = "h2i_ping"  
h2i> ping  
[FrameHeader PING flags=ACK len=8]
  Data = "h2i_ping"
h2i> ping
[FrameHeader GOAWAY len=22]
  Last-Stream-ID = 1; Error-Code = PROTOCOL_ERROR (1)

ReadFrame: EOF
```

## Status

Quick few hour hack. So much yet to do. Feel free to file issues for
bugs or wishlist items, but [@bmizerany](https://github.com/bmizerany/)
and I aren't yet accepting pull requests until things settle down.


Client:
 -- Firefox nightly with about:config network.http.spdy.enabled.http2draft set true
 -- Chrome: go to chrome://flags/#enable-spdy4, save and restart (button at bottom)

Make CA:
$ openssl genrsa -out rootCA.key 2048
$ openssl req -x509 -new -nodes -key rootCA.key -days 1024 -out rootCA.pem
... install that to Firefox

Make cert:
$ openssl genrsa -out server.key 2048
$ openssl req -new -key server.key -out server.csr
$ openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.crt -days 500


This is a fork of the encoding/xml package at ca1d6c4, the last commit before
https://go.googlesource.com/go/+/c0d6d33 "encoding/xml: restore Go 1.4 name
space behavior" made late in the lead-up to the Go 1.5 release.

The list of encoding/xml changes is at
https://go.googlesource.com/go/+log/master/src/encoding/xml

This fork is temporary, and I (nigeltao) expect to revert it after Go 1.6 is
released.

See http://golang.org/issue/11841
gotk3 [![GoDoc](https://godoc.org/github.com/gotk3/gotk3?status.svg)](https://godoc.org/github.com/gotk3/gotk3)
=====

[![Build Status](https://travis-ci.org/gotk3/gotk3.png?branch=master)](https://travis-ci.org/gotk3/gotk3)

The gotk3 project provides Go bindings for GTK+3 and dependent
projects.  Each component is given its own subdirectory, which is used
as the import path for the package.  Partial binding support for the
following libraries is currently implemented:

  - GTK+3 (3.12 and later)
  - GDK 3 (3.12 and later)
  - GLib 2 (2.36 and later)
  - Cairo (1.10 and later)

Care has been taken for memory management to work seamlessly with Go's
garbage collector without the need to use or understand GObject's
floating references.

## Sample Use

The following example can be found in [Examples](https://github.com/gotk3/gotk3-examples/).

```Go
package main

import (
	"github.com/gotk3/gotk3/gtk"
	"log"
)

func main() {
	// Initialize GTK without parsing any command line arguments.
	gtk.Init(nil)

	// Create a new toplevel window, set its title, and connect it to the
	// "destroy" signal to exit the GTK main loop when it is destroyed.
	win, err := gtk.WindowNew(gtk.WINDOW_TOPLEVEL)
	if err != nil {
		log.Fatal("Unable to create window:", err)
	}
	win.SetTitle("Simple Example")
	win.Connect("destroy", func() {
		gtk.MainQuit()
	})

	// Create a new label widget to show in the window.
	l, err := gtk.LabelNew("Hello, gotk3!")
	if err != nil {
		log.Fatal("Unable to create label:", err)
	}

	// Add the label to the window.
	win.Add(l)

	// Set the default window size.
	win.SetDefaultSize(800, 600)

	// Recursively show all widgets contained in this window.
	win.ShowAll()

	// Begin executing the GTK main loop.  This blocks until
	// gtk.MainQuit() is run. 
	gtk.Main()
}
```

To build the example:

```
$ go build example.go

```

To build this example with older gtk version you should use gtk_3_10 tag:

```
$ go build -tags gtk_3_10 example.go

```

### examples for gtk3

```Go
package main

import (
	"log"
	"os"

	"github.com/gotk3/gotk3/glib"
	"github.com/gotk3/gotk3/gtk"
)

// Simple Gtk3 Application written in go.
// This application creates a window on the application callback activate.
// More GtkApplication info can be found here -> https://wiki.gnome.org/HowDoI/GtkApplication

func main() {
	// Create Gtk Application, change appID to your application domain name reversed.
	const appID = "org.gtk.example"
	application, err := gtk.ApplicationNew(appID, glib.APPLICATION_FLAGS_NONE)
	// Check to make sure no errors when creating Gtk Application
	if err != nil {
		log.Fatal("Could not create application.", err)
	}
	// Application signals available
	// startup -> sets up the application when it first starts
	// activate -> shows the default first window of the application (like a new document). This corresponds to the application being launched by the desktop environment.
	// open -> opens files and shows them in a new window. This corresponds to someone trying to open a document (or documents) using the application from the file browser, or similar.
	// shutdown ->  performs shutdown tasks
	// Setup Gtk Application callback signals
	application.Connect("activate", func() { onActivate(application) })
	// Run Gtk application
	os.Exit(application.Run(os.Args))
}

// Callback signal from Gtk Application
func onActivate(application *gtk.Application) {
	// Create ApplicationWindow
	appWindow, err := gtk.ApplicationWindowNew(application)
	if err != nil {
		log.Fatal("Could not create application window.", err)
	}
	// Set ApplicationWindow Properties
	appWindow.SetTitle("Basic Application.")
	appWindow.SetDefaultSize(400, 400)
	appWindow.Show()
}
```


```Go
package main

import (
	"log"
	"os"

	"github.com/gotk3/gotk3/glib"
	"github.com/gotk3/gotk3/gtk"
)

// Simple Gtk3 Application written in go.
// This application creates a window on the application callback activate.
// More GtkApplication info can be found here -> https://wiki.gnome.org/HowDoI/GtkApplication

func main() {
	// Create Gtk Application, change appID to your application domain name reversed.
	const appID = "org.gtk.example"
	application, err := gtk.ApplicationNew(appID, glib.APPLICATION_FLAGS_NONE)
	// Check to make sure no errors when creating Gtk Application
	if err != nil {
		log.Fatal("Could not create application.", err)
	}

	// Application signals available
	// startup -> sets up the application when it first starts
	// activate -> shows the default first window of the application (like a new document). This corresponds to the application being launched by the desktop environment.
	// open -> opens files and shows them in a new window. This corresponds to someone trying to open a document (or documents) using the application from the file browser, or similar.
	// shutdown ->  performs shutdown tasks
	// Setup activate signal with a closure function.
	application.Connect("activate", func() {
		// Create ApplicationWindow
		appWindow, err := gtk.ApplicationWindowNew(application)
		if err != nil {
			log.Fatal("Could not create application window.", err)
		}
		// Set ApplicationWindow Properties
		appWindow.SetTitle("Basic Application.")
		appWindow.SetDefaultSize(400, 400)
		appWindow.Show()
	})
	// Run Gtk application
	application.Run(os.Args)
}
```

## Documentation

Each package's internal `go doc` style documentation can be viewed
online without installing this package by using the GoDoc site (links
to [cairo](http://godoc.org/github.com/gotk3/gotk3/cairo),
[glib](http://godoc.org/github.com/gotk3/gotk3/glib),
[gdk](http://godoc.org/github.com/gotk3/gotk3/gdk), and
[gtk](http://godoc.org/github.com/gotk3/gotk3/gtk) documentation).

You can also view the documentation locally once the package is
installed with the `godoc` tool by running `godoc -http=":6060"` and
pointing your browser to
http://localhost:6060/pkg/github.com/gotk3/gotk3

## Installation

gotk3 currently requires GTK 3.6-3.16, GLib 2.36-2.40, and
Cairo 1.10 or 1.12.  A recent Go (1.3 or newer) is also required.

For detailed instructions see the wiki pages: [installation](https://github.com/gotk3/gotk3/wiki#installation)

## TODO
- Add bindings for all of GTK+
- Add tests for each implemented binding

## License

Package gotk3 is licensed under the liberal ISC License.
## bulb - Is not stem
### Yawning Angel (yawning at torproject dot org)

bulb is a Go language interface to the Tor control port.  It is considerably
lighter in functionality than stem and other controller libraries, and is
intended to be used in combination with`control-spec.txt`.

It was written primarily as a not-invented-here hack, and the base interface is
more than likely to stay fairly low level, though useful helpers will be added
as I need them.

Things you should probably use instead:
 * [stem](https://stem.torproject.org)
 * [txtorcon](https://pypi.python.org/pypi/txtorcon)
 * [orc](https://github.com/sycamoreone/orc)

Bugs:
 * bulb does not send the 'QUIT' command before closing the connection.
