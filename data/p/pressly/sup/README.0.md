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

The yaml package supports most of YAML 1.1 and 1.2, including support for
anchors, tags, map merging, etc. Multi-document unmarshalling is not yet
implemented, and base-60 floats from YAML 1.1 are purposefully not
supported since they're a poor design and are gone in YAML 1.2.

Installation and usage
----------------------

The import path for the package is *gopkg.in/yaml.v2*.

To install it, run:

    go get gopkg.in/yaml.v2

API documentation
-----------------

If opened in a browser, the import path itself leads to the API documentation:

  * [https://gopkg.in/yaml.v2](https://gopkg.in/yaml.v2)

API stability
-------------

The package API for yaml v2 will remain stable as described in [gopkg.in](https://gopkg.in).


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

        "gopkg.in/yaml.v2"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

type T struct {
        A string
        B struct {
                RenamedC int   `yaml:"c"`
                D        []int `yaml:",flow"`
        }
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

# Prefixer
[Golang](http://golang.org/)'s [io.Reader](http://golang.org/pkg/io/#Reader) wrapper prepending every line with a given string.

[![GoDoc](https://godoc.org/github.com/goware/prefixer?status.png)](https://godoc.org/github.com/goware/prefixer)
[![Travis](https://travis-ci.org/goware/prefixer.svg?branch=master)](https://travis-ci.org/goware/prefixer)


## Use cases
1. Logger that prefixes every line with a timestamp etc.
    ```bash
    16:54:49 My awesome server | Creating etcd client pointing to http://localhost:4001
    16:54:49 My awesome server | Listening on http://localhost:8080
    16:54:49 My awesome server | [restful/swagger] listing is available at 127.0.0.1:8080/swaggerapi
    ```

2. SSH multiplexer prepending output from multiple servers with a hostname
    ```bash
    host1.example.com | SUCCESS
    host2.example.com | SUCCESS
    host3.example.com | -bash: cd: workdir: No such file or directory
    host4.example.com | SUCCESS
    ```

3. Create an email reply (`"> "` prefix) from any text easily.
    ```bash
    $ ./prefix
    Dear John,               
    did you know that https://github.com/goware/prefixer is a golang pkg
    that prefixes every line with a given string and accepts any io.Reader?

    Cheers,
    - Jane
    ^D     
    > Dear John,               
    > did you know that https://github.com/goware/prefixer is a golang pkg
    > that prefixes every line with a given string and accepts any io.Reader?
    >
    > Cheers,
    > - Jane
    ```

## Example

See the ["Prefix Line Reader" example](./example).

```go
package main

import (
    "io/ioutil"
    "os"

    "github.com/goware/prefixer"
)

func main() {
    // Prefixer accepts anything that implements io.Reader interface
    prefixReader := prefixer.New(os.Stdin, "> ")

    // Read all prefixed lines from STDIN into a buffer
    buffer, _ := ioutil.ReadAll(prefixReader)

    // Write buffer to STDOUT
    os.Stdout.Write(buffer)
}
```

## License
Prefixer is licensed under the [MIT License](./LICENSE).
# OpenSSH config parser for golang

[![Build Status](https://travis-ci.org/mikkeloscar/sshconfig.svg?branch=master)](https://travis-ci.org/mikkeloscar/sshconfig)
[![GoDoc](https://godoc.org/github.com/mikkeloscar/sshconfig?status.svg)](https://godoc.org/github.com/mikkeloscar/sshconfig)
[![Go Report Card](https://goreportcard.com/badge/github.com/mikkeloscar/sshconfig)](https://goreportcard.com/report/github.com/mikkeloscar/sshconfig)
[![Coverage Status](https://coveralls.io/repos/github/mikkeloscar/sshconfig/badge.svg)](https://coveralls.io/github/mikkeloscar/sshconfig)

Parses the config usually found in `~/.ssh/config` or `/etc/ssh/ssh_config`.
Only `Host`, `HostName`, `User`, `Port` and `ProxyCommand` is implemented at
this point.

[OpenSSH Reference.][openssh_man]

## Usage

Example usage

```go
package main

import (
    "fmt"

    "github.com/mikkeloscar/sshconfig"
)

func main() {
    hosts, err := ParseSSHConfig("/path/to/ssh_config")
    if err != nil {
        fmt.Println(err)
    }

    for _, host := range hosts {
       fmt.Printf("Hostname: %s", host.HostName)
    }
}
```

## LICENSE

Copyright (C) 2016  Mikkel Oscar Lyderik Larsen & Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

[openssh_man]: http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man5/ssh_config.5?query=ssh_config&sec=5
# errors [![Travis-CI](https://travis-ci.org/pkg/errors.svg)](https://travis-ci.org/pkg/errors) [![AppVeyor](https://ci.appveyor.com/api/projects/status/b98mptawhudj53ep/branch/master?svg=true)](https://ci.appveyor.com/project/davecheney/errors/branch/master) [![GoDoc](https://godoc.org/github.com/pkg/errors?status.svg)](http://godoc.org/github.com/pkg/errors) [![Report card](https://goreportcard.com/badge/github.com/pkg/errors)](https://goreportcard.com/report/github.com/pkg/errors)

Package errors provides simple error handling primitives.

The traditional error handling idiom in Go is roughly akin to
```go
if err != nil {
        return err
}
```
which applied recursively up the call stack results in error reports without context or debugging information. The errors package allows programmers to add context to the failure path in their code in a way that does not destroy the original value of the error.

## Adding context to an error

The errors.Wrap function returns a new error that adds context to the original error. For example
```go
_, err := ioutil.ReadAll(r)
if err != nil {
        return errors.Wrap(err, "read failed")
}
```
## Retrieving the cause of an error

Using `errors.Wrap` constructs a stack of errors, adding context to the preceding error. Depending on the nature of the error it may be necessary to reverse the operation of errors.Wrap to retrieve the original error for inspection. Any error value which implements this interface can be inspected by `errors.Cause`.
```go
type causer interface {
        Cause() error
}
```
`errors.Cause` will recursively retrieve the topmost error which does not implement `causer`, which is assumed to be the original cause. For example:
```go
switch err := errors.Cause(err).(type) {
case *MyError:
        // handle specifically
default:
        // unknown error
}
```

[Read the package documentation for more information](https://godoc.org/github.com/pkg/errors).

## Contributing

We welcome pull requests, bug fixes and issue reports. With that said, the bar for adding new symbols to this package is intentionally set high.

Before proposing a change, please discuss your change by raising an issue.

## Licence

BSD-2-Clause
