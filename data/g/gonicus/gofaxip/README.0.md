Package warnings implements error handling with non-fatal errors (warnings).

import path:   "gopkg.in/warnings.v0"
package docs:  https://godoc.org/gopkg.in/warnings.v0 
issues:        https://github.com/go-warnings/warnings/issues
pull requests: https://github.com/go-warnings/warnings/pulls

A recurring pattern in Go programming is the following:

 func myfunc(params) error {
     if err := doSomething(...); err != nil {
         return err
     }
     if err := doSomethingElse(...); err != nil {
         return err
     }
     if ok := doAnotherThing(...); !ok {
         return errors.New("my error")
     }
     ...
     return nil
 }

This pattern allows interrupting the flow on any received error. But what if
there are errors that should be noted but still not fatal, for which the flow
should not be interrupted? Implementing such logic at each if statement would
make the code complex and the flow much harder to follow.

Package warnings provides the Collector type and a clean and simple pattern
for achieving such logic. The Collector takes care of deciding when to break
the flow and when to continue, collecting any non-fatal errors (warnings)
along the way. The only requirement is that fatal and non-fatal errors can be
distinguished programmatically; that is a function such as

 IsFatal(error) bool

must be implemented. The following is an example of what the above snippet
could look like using the warnings package:

 import "gopkg.in/warnings.v0"

 func isFatal(err error) bool {
     _, ok := err.(WarningType)
     return !ok
 }

 func myfunc(params) error {
     c := warnings.NewCollector(isFatal)
     c.FatalWithWarnings = true
     if err := c.Collect(doSomething()); err != nil {
         return err
     }
     if err := c.Collect(doSomethingElse(...)); err != nil {
         return err
     }
     if ok := doAnotherThing(...); !ok {
         if err := c.Collect(errors.New("my error")); err != nil {
             return err
         }
     }
     ...
     return c.Done()
 }

Rules for using warnings

 - ensure that warnings are programmatically distinguishable from fatal
   errors (i.e. implement an isFatal function and any necessary error types)
 - ensure that there is a single Collector instance for a call of each
   exported function
 - ensure that all errors (fatal or warning) are fed through Collect
 - ensure that every time an error is returned, it is one returned by a
   Collector (from Collect or Done)
 - ensure that Collect is never called after Done
Gcfg reads INI-style configuration files into Go structs;
supports user-defined types and subsections.

Package docs: https://godoc.org/gopkg.in/gcfg.v1
**This package is currently in development and the API may not be stable.**

The API will become stable with v1.

# uuid ![build status](https://travis-ci.org/google/uuid.svg?branch=master)
The uuid package generates and inspects UUIDs based on
[RFC 4122](http://tools.ietf.org/html/rfc4122)
and DCE 1.1: Authentication and Security Services. 

This package is based on the github.com/pborman/uuid package (previously named
code.google.com/p/go-uuid).  It differs from these earlier packages in that
a UUID is a 16 byte array rather than a byte slice.  One loss due to this
change is the ability to represent an invalid UUID (vs a NIL UUID).

###### Install
`go get github.com/google/uuid`

###### Documentation 
[![GoDoc](https://godoc.org/github.com/google/uuid?status.svg)](http://godoc.org/github.com/google/uuid)

Full `go doc` style documentation for the package can be viewed online without
installing this package by using the GoDoc site here: 
http://godoc.org/github.com/google/uuid
# eventsocket

FreeSWITCH [Event Socket](http://wiki.freeswitch.org/wiki/Event_Socket) library
for the [Go programming language](http://golang.org).

It supports both inbound and outbound event socket connections, acting either
as a client connecting to FreeSWITCH or as a server accepting connections
from FreeSWITCH to control calls.

This code has not been tested in production and is considered alpha. Use at
your own risk.

## Installing

Make sure $GOPATH is set, and use the following command to install:

	go get github.com/fiorix/go-eventsocket/eventsocket

The library is currently a single file, so feel free to drop into any project
without bothering to install.

## Usage

There are simple and clear examples of usage under the *examples* directory. A
client that connects to FreeSWITCH and originate a call, pointing to an
Event Socket server, which answers the call and instructs FreeSWITCH to play
an audio file.
