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
# TensorFlow in Go

Construct and execute TensorFlow graphs in Go.

[![GoDoc](https://godoc.org/github.com/tensorflow/tensorflow/tensorflow/go?status.svg)](https://godoc.org/github.com/tensorflow/tensorflow/tensorflow/go)

> *WARNING*: The API defined in this package is not stable and can change
> without notice. The same goes for the awkward package path
> (`github.com/tensorflow/tensorflow/tensorflow/go`).

## Quickstart

Refer to [Installing TensorFlow for Go](https://www.tensorflow.org/install/install_go)

## Building the TensorFlow C library from source

If the "Quickstart" instructions above do not work (perhaps the release archives
are not available for your operating system or architecture, or you're using a
different version of CUDA/cuDNN), then the TensorFlow C library must be built
from source.

### Prerequisites

-   [bazel](https://www.bazel.build/versions/master/docs/install.html)
-   Environment to build TensorFlow from source code
    ([Linux](https://www.tensorflow.org/install/install_sources#PrepareLinux)
    or [OS
    X](https://www.tensorflow.org/install/install_sources#PrepareMac)).
    If you don't need GPU support, then try the following:

    ```sh
    sudo apt-get install python swig python-numpy # Linux
    brew install swig                             # OS X with homebrew
    ```

### Build

1.  Download the source code

    ```sh
    go get -d github.com/tensorflow/tensorflow/tensorflow/go
    ```

2.  Build the TensorFlow C library:

    ```sh
    cd ${GOPATH}/src/github.com/tensorflow/tensorflow
    ./configure
    bazel build --config opt //tensorflow:libtensorflow.so
    ```

    This can take a while (tens of minutes, more if also building for GPU).

3.  Make `libtensorflow.so` available to the linker. This can be done by either:

    a. Copying it to a system location, e.g.,

    ```sh
    sudo cp ${GOPATH}/src/github.com/tensorflow/tensorflow/bazel-bin/tensorflow/libtensorflow.so /usr/local/lib
    ```

    OR

    b. Setting environment variables:

    ```sh
    export LIBRARY_PATH=${GOPATH}/src/github.com/tensorflow/tensorflow/bazel-bin/tensorflow
    # Linux
    export LD_LIBRARY_PATH=${GOPATH}/src/github.com/tensorflow/tensorflow/bazel-bin/tensorflow
    # OS X
    export DYLD_LIBRARY_PATH=${GOPATH}/src/github.com/tensorflow/tensorflow/bazel-bin/tensorflow
    ```

4.  Build and test:

    ```sh
    go test github.com/tensorflow/tensorflow/tensorflow/go
    ```

### Generate wrapper functions for ops

Go functions corresponding to TensorFlow operations are generated in `op/wrappers.go`. To regenerate them:

Prerequisites:
- [Protocol buffer compiler (protoc) 3.x](https://github.com/google/protobuf/releases/)
- The TensorFlow repository under GOPATH

```sh
go generate github.com/tensorflow/tensorflow/tensorflow/go/op
```

## Support

Use [stackoverflow](http://stackoverflow.com/questions/tagged/tensorflow) and/or
[Github issues](https://github.com/tensorflow/tensorflow/issues).

## Contributions

Contributions are welcome. If making any signification changes, probably best to
discuss on a [Github issue](https://github.com/tensorflow/tensorflow/issues)
before investing too much time. Github pull requests are used for contributions.
# gRPC-Go

[![Build Status](https://travis-ci.org/grpc/grpc-go.svg)](https://travis-ci.org/grpc/grpc-go) [![GoDoc](https://godoc.org/google.golang.org/grpc?status.svg)](https://godoc.org/google.golang.org/grpc) [![GoReportCard](https://goreportcard.com/badge/grpc/grpc-go)](https://goreportcard.com/report/github.com/grpc/grpc-go)

The Go implementation of [gRPC](https://grpc.io/): A high performance, open source, general RPC framework that puts mobile and HTTP/2 first. For more information see the [gRPC Quick Start: Go](https://grpc.io/docs/quickstart/go.html) guide.

Installation
------------

To install this package, you need to install Go and setup your Go workspace on your computer. The simplest way to install the library is to run:

```
$ go get -u google.golang.org/grpc
```

Prerequisites
-------------

This requires Go 1.6 or later. Go 1.7 will be required soon.

Constraints
-----------
The grpc package should only depend on standard Go packages and a small number of exceptions. If your contribution introduces new dependencies which are NOT in the [list](http://godoc.org/google.golang.org/grpc?imports), you need a discussion with gRPC-Go authors and consultants.

Documentation
-------------
See [API documentation](https://godoc.org/google.golang.org/grpc) for package and API descriptions and find examples in the [examples directory](examples/).

Performance
-----------
See the current benchmarks for some of the languages supported in [this dashboard](https://performance-dot-grpc-testing.appspot.com/explore?dashboard=5652536396611584&widget=490377658&container=1286539696).

Status
------
General Availability [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages).

FAQ
---

#### Compiling error, undefined: grpc.SupportPackageIsVersion

Please update proto package, gRPC package and rebuild the proto files:
 - `go get -u github.com/golang/protobuf/{proto,protoc-gen-go}`
 - `go get -u google.golang.org/grpc`
 - `protoc --go_out=plugins=grpc:. *.proto`
[![GoDoc](https://godoc.org/github.com/Applifier/go-tensorflow/serving?status.svg)](http://godoc.org/github.com/Applifier/go-tensorflow/serving)

# Tensorflow Serving client for go
Go client for [Tensorflow Serving](https://github.com/tensorflow/serving)

### Example

Example uses pre-trained model found under testdata/models [wide_deep](https://github.com/tensorflow/models/tree/master/official/wide_deep)

```go
import "github.com/Applifier/go-tensorflow/serving"
```

```go

// Init client
cli, _ := serving.NewModelPredictionClientFromAddr(
    getServingAddr(),
    "wide_deep",
    "serving_default",
    1527087570,
)

// Create Example and Features
example, _ := serving.NewExampleFromMap(map[string]interface{}{
    "age":            35.0,
    "capital_gain":   0.0,
    "capital_loss":   0.0,
    "education":      "Masters",
    "education_num":  14.0,
    "gender":         "Female",
    "hours_per_week": 29.0,
    "native_country": "United-States",
    "occupation":     "Prof-specialty",
    "relationship":   "Husband",
    "workclass":      "Private",
})

// Convert example to protobuf
exampleSerialized, _ := example.Marshal()

// Convert serialized example to tensor
tensor, _ := NewTensor([][]byte{exampleSerialized})

res, _ := cli.Predict(context.Background(), serving.TensorMap{
    "inputs": tensor,
}, nil)

fmt.Printf("scores %+v\n", res.Outputs["scores"].FloatVal)

// Output: scores [0.54612064 0.45387936]

```# SavedModel Utils

Utils for making using of SavedModels in Go more similar to TensorFlow Serving
Tool for testing a saved model

```sh
$ go run main.go --modelpath ../../testdata/models/wide_deep/1527087570 -input '{"inputs": {"age":35,"capital_gain":0,"capital_loss":0,"education":"Masters","education_num":14,"gender":"Female","hours_per_week":29,"native_country":"United-States","occupation":"Prof-specialty","relationship":"Husband","workclass":"Private"}}'
Input: map[inputs:map[occupation:Prof-specialty relationship:Husband workclass:Private education:Masters education_num:14 hours_per_week:29 native_country:United-States age:35 capital_gain:0 capital_loss:0 gender:Female]]
2018-09-04 11:44:26.398483: I tensorflow/cc/saved_model/reader.cc:31] Reading SavedModel from: ../../testdata/models/wide_deep/1527087570
2018-09-04 11:44:26.404779: I tensorflow/cc/saved_model/reader.cc:54] Reading meta graph with tags { serve }
2018-09-04 11:44:26.414817: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.2 AVX AVX2 FMA
2018-09-04 11:44:26.434207: I tensorflow/cc/saved_model/loader.cc:113] Restoring SavedModel bundle.
2018-09-04 11:44:26.456225: I tensorflow/cc/saved_model/loader.cc:148] Running LegacyInitOp on SavedModel bundle.
2018-09-04 11:44:26.500136: I tensorflow/cc/saved_model/loader.cc:233] SavedModel load for tags { serve }; Status: success. Took 101670 microseconds.
Output:
{
  "classes": [
    [
      "0",
      "1"
    ]
  ],
  "scores": [
    [
      0.54612064,
      0.45387936
    ]
  ]
}
```