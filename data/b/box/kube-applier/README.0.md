# procfs

This procfs package provides functions to retrieve system, kernel and process
metrics from the pseudo-filesystem proc.

*WARNING*: This package is a work in progress. Its API may still break in
backwards-incompatible ways without warnings. Use it at your own risk.

[![GoDoc](https://godoc.org/github.com/prometheus/procfs?status.png)](https://godoc.org/github.com/prometheus/procfs)
[![Build Status](https://travis-ci.org/prometheus/procfs.svg?branch=master)](https://travis-ci.org/prometheus/procfs)
# Overview
This is the [Prometheus](http://www.prometheus.io) telemetric
instrumentation client [Go](http://golang.org) client library.  It
enable authors to define process-space metrics for their servers and
expose them through a web service interface for extraction,
aggregation, and a whole slew of other post processing techniques.

# Installing
    $ go get github.com/prometheus/client_golang/prometheus

# Example
```go
package main

import (
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
)

var (
	indexed = prometheus.NewCounter(prometheus.CounterOpts{
		Namespace: "my_company",
		Subsystem: "indexer",
		Name:      "documents_indexed",
		Help:      "The number of documents indexed.",
	})
	size = prometheus.NewGauge(prometheus.GaugeOpts{
		Namespace: "my_company",
		Subsystem: "storage",
		Name:      "documents_total_size_bytes",
		Help:      "The total size of all documents in the storage.",
	})
)

func main() {
	http.Handle("/metrics", prometheus.Handler())

	indexed.Inc()
	size.Set(5)

	http.ListenAndServe(":8080", nil)
}

func init() {
	prometheus.MustRegister(indexed)
	prometheus.MustRegister(size)
}
```

# Documentation

[![GoDoc](https://godoc.org/github.com/prometheus/client_golang?status.png)](https://godoc.org/github.com/prometheus/client_golang)
PACKAGE

package goautoneg
import "bitbucket.org/ww/goautoneg"

HTTP Content-Type Autonegotiation.

The functions in this package implement the behaviour specified in
http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html

Copyright (c) 2011, Open Knowledge Foundation Ltd.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.

    Neither the name of the Open Knowledge Foundation Ltd. nor the
    names of its contributors may be used to endorse or promote
    products derived from this software without specific prior written
    permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


FUNCTIONS

func Negotiate(header string, alternatives []string) (content_type string)
Negotiate the most appropriate content_type given the accept header
and a list of alternatives.

func ParseAccept(header string) (accept []Accept)
Parse an Accept Header string returning a sorted list
of clauses


TYPES

type Accept struct {
    Type, SubType string
    Q             float32
    Params        map[string]string
}
Structure to represent a clause in an HTTP Accept Header


SUBDIRECTORIES

	.hg
# Demo

An example Deployment and Service spec for kube-applier, with git-sync as a sidecar container.