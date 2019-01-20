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

The yaml package is licensed under the Apache License 2.0. Please see the LICENSE file for details.


Example
-------

Some more examples can be found in the "examples" folder.

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

drone-plugin-go
===============

This is a package with simple support for writing Drone plugins in Go.

## Overview

Plugins are executable files run by Drone to customize the build lifecycle. Plugins receive input data from `stdin` (or `arg[1]`) and write the results to `stdout`

```sh
./slack-plugin <<EOF
{
    "repo" : {
        "owner": "foo",
        "name": "bar",
        "full_name": "foo/bar"
    },
    "build" : {
        "number": 1
        "status": "success",
        "started_at": 1421029603,
        "finished_at": 1421029813,
        "head_commit" : {
            "sha": "9f2849d5",
            "ref": "refs/heads/master"
            "branch": "master",
            "message": "Update the Readme",
            "author": {
                "login": "johnsmith"
                "email": "john.smith@gmail.com",
            }
        }
    },
    "job" : {
        "number": 1,
        "status": "success",
        "started_at": 1421029603,
        "finished_at": 1421029813,
        "exit_code": 0,
        "environment": { "GO_VERSION": "1.4" }
    }
    "clone" : {
        "branch": "master",
        "remote": "git://github.com/drone/drone",
        "dir": "/drone/src/github.com/drone/drone",
        "ref": "refs/heads/master",
        "sha": "436b7a6e2abaddfd35740527353e78a227ddcb2c"
    },
    "vargs": {
        "webhook_url": "https://hooks.slack.com/services/...",
        "username": "drone",
        "channel": "#dev"
    }
}
EOF
```

Use this `plugin` package to retrieve and parse input parameters:

```Go
var repo = plugin.Repo{}
var build = plugin.Build{}
var slack = struct {
    URL      string `json:"webhook_url"`
    Username string `json:"username"`
    Channel  string `json:"channel"`
}{}

plugin.Param("repo", &repo)
plugin.Param("build", &build)
plugin.Param("vargs", &slack)
plugin.Parse()
```

Note that your plugin configuration data (declared in the `.drone.yml` file) will be provided in the `vargs` section of the JSON input.

### Shared Volumes

The repository clone directory (specified in the `clone.dir` input parameter) will be shared across all plugins as a [container volume](https://docs.docker.com/userguide/dockervolumes/#creating-and-mounting-a-data-volume-container). This means that any files in your repository directory or subdirectories are accessible to plugins. This is useful for plugins that analyze or archive files, such as an S3 plugin.

### Publishing

Drone plugins are distributed as Docker images. We therefore recommend publishing your plugins to [Docker Hub](https://index.docker.io).

The `ENTRYPOINT` must be defined and must point to your executable file. The `CMD` section will be overridden by Drone and will be used to send the JSON encoded data in `arg[1]`. An example Dockerfile for your plugin might look like this:

```Dockerfile
# Docker image for Drone's git-clone plugin
#
#     docker build -t drone/drone-clone-git .

FROM library/golang:1.4

# copy the local src files to the container's workspace.
ADD . /go/src/github.com/drone/drone-clone-git/

# build the git-clone plugin inside the container.
RUN go get github.com/drone/drone-clone-git/... && \
    go install github.com/drone/drone-clone-git

# run the git-clone plugin when the container starts
ENTRYPOINT ["/go/bin/drone-clone-git"]
```
# errors [![Travis-CI](https://travis-ci.org/pkg/errors.svg)](https://travis-ci.org/pkg/errors) [![AppVeyor](https://ci.appveyor.com/api/projects/status/b98mptawhudj53ep/branch/master?svg=true)](https://ci.appveyor.com/project/davecheney/errors/branch/master) [![GoDoc](https://godoc.org/github.com/pkg/errors?status.svg)](http://godoc.org/github.com/pkg/errors) [![Report card](https://goreportcard.com/badge/github.com/pkg/errors)](https://goreportcard.com/report/github.com/pkg/errors)

Package errors provides simple error handling primitives.

`go get github.com/pkg/errors`

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
# YAML marshaling and unmarshaling support for Go

[![Build Status](https://travis-ci.org/ghodss/yaml.svg)](https://travis-ci.org/ghodss/yaml)

## Introduction

A wrapper around [go-yaml](https://github.com/go-yaml/yaml) designed to enable a better way of handling YAML when marshaling to and from structs.

In short, this library first converts YAML to JSON using go-yaml and then uses `json.Marshal` and `json.Unmarshal` to convert to or from the struct. This means that it effectively reuses the JSON struct tags as well as the custom JSON methods `MarshalJSON` and `UnmarshalJSON` unlike go-yaml. For a detailed overview of the rationale behind this method, [see this blog post](http://ghodss.com/2014/the-right-way-to-handle-yaml-in-golang/).

## Compatibility

This package uses [go-yaml](https://github.com/go-yaml/yaml) and therefore supports [everything go-yaml supports](https://github.com/go-yaml/yaml#compatibility).

## Caveats

**Caveat #1:** When using `yaml.Marshal` and `yaml.Unmarshal`, binary data should NOT be preceded with the `!!binary` YAML tag. If you do, go-yaml will convert the binary data from base64 to native binary data, which is not compatible with JSON. You can still use binary in your YAML files though - just store them without the `!!binary` tag and decode the base64 in your code (e.g. in the custom JSON methods `MarshalJSON` and `UnmarshalJSON`). This also has the benefit that your YAML and your JSON binary data will be decoded exactly the same way. As an example:

```
BAD:
	exampleKey: !!binary gIGC

GOOD:
	exampleKey: gIGC
... and decode the base64 data in your code.
```

**Caveat #2:** When using `YAMLToJSON` directly, maps with keys that are maps will result in an error since this is not supported by JSON. This error will occur in `Unmarshal` as well since you can't unmarshal map keys anyways since struct fields can't be keys.

## Installation and usage

To install, run:

```
$ go get github.com/ghodss/yaml
```

And import using:

```
import "github.com/ghodss/yaml"
```

Usage is very similar to the JSON library:

```go
package main

import (
	"fmt"

	"github.com/ghodss/yaml"
)

type Person struct {
	Name string `json:"name"` // Affects YAML field names too.
	Age  int    `json:"age"`
}

func main() {
	// Marshal a Person struct to YAML.
	p := Person{"John", 30}
	y, err := yaml.Marshal(p)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(y))
	/* Output:
	age: 30
	name: John
	*/

	// Unmarshal the YAML back into a Person struct.
	var p2 Person
	err = yaml.Unmarshal(y, &p2)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(p2)
	/* Output:
	{John 30}
	*/
}
```

`yaml.YAMLToJSON` and `yaml.JSONToYAML` methods are also available:

```go
package main

import (
	"fmt"

	"github.com/ghodss/yaml"
)

func main() {
	j := []byte(`{"name": "John", "age": 30}`)
	y, err := yaml.JSONToYAML(j)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(y))
	/* Output:
	name: John
	age: 30
	*/
	j2, err := yaml.YAMLToJSON(y)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(j2))
	/* Output:
	{"age":30,"name":"John"}
	*/
}
```
