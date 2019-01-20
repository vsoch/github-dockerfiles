## How To
```sh
$ docker run -ti --rm --net=host jdef/example-scheduler-httpv1 -server.address=10.2.0.5 \
    -url=http://10.2.0.7:5050/api/v1/scheduler -tasks=10 -verbose
```
# Go bindings for Apache Mesos

Very early version of a pure Go language bindings for Apache Mesos. As with other pure implementation, mesos-go uses the HTTP wire protocol to communicate directly with  a running Mesos master and its slave instances. One of the objectives of this project is to provide an idiomatic Go API that makes it super easy to create Mesos frameworks using Go. 

## Status
The Mesos v0 API version of the bindings are considered **alpha** and won't
see any major development besides critical compatibility and bug fixes.

New projects should use the Mesos v1 API bindings, located in `api/v1`.

### Features
- The SchedulerDriver API implemented
- The ExecutorDriver API implemented
- Stable API (based on the core Mesos code)
- Plenty of unit and integrative of tests
- Modular design for easy readability/extensibility
- Example programs on how to use the API
- Leading master detection
- Authentication via SASL/CRAM-MD5

### Pre-Requisites
- Go 1.3 or higher
- A standard and working Go workspace setup
- Apache Mesos 0.19 or newer

## Installing
Users of this library are encouraged to vendor it. API stability isn't guaranteed at this stage.
```shell
$ go get github.com/mesos/mesos-go
```

## Testing
```shell
$ (cd $GOPATH/src/github.com/mesos/mesos-go/api/v0; go test -race ./...)
```
####Benchmark of the messenger.

```shell
$ go test -v -run=Benckmark* -bench=. 
PASS
BenchmarkMessengerSendSmallMessage	   50000	     70568 ns/op
BenchmarkMessengerSendMediumMessage	   50000	     70265 ns/op
BenchmarkMessengerSendBigMessage	   50000	     72693 ns/op
BenchmarkMessengerSendLargeMessage	   50000	     72896 ns/op
BenchmarkMessengerSendMixedMessage	   50000	     72631 ns/op
BenchmarkMessengerSendRecvSmallMessage	   20000	     78409 ns/op
BenchmarkMessengerSendRecvMediumMessage	   20000	     80471 ns/op
BenchmarkMessengerSendRecvBigMessage	   20000	     82629 ns/op
BenchmarkMessengerSendRecvLargeMessage	   20000	     85987 ns/op
BenchmarkMessengerSendRecvMixedMessage	   20000	     83678 ns/op
ok  	github.com/mesos/mesos-go/messenger	115.135s

$ go test -v -run=Benckmark* -bench=. -cpu=4 -send-routines=4 2>/dev/null
PASS
BenchmarkMessengerSendSmallMessage-4	   50000	     35529 ns/op
BenchmarkMessengerSendMediumMessage-4	   50000	     35997 ns/op
BenchmarkMessengerSendBigMessage-4	   50000	     36871 ns/op
BenchmarkMessengerSendLargeMessage-4	   50000	     37310 ns/op
BenchmarkMessengerSendMixedMessage-4	   50000	     37419 ns/op
BenchmarkMessengerSendRecvSmallMessage-4	   50000	     39320 ns/op
BenchmarkMessengerSendRecvMediumMessage-4	   50000	     41990 ns/op
BenchmarkMessengerSendRecvBigMessage-4	   50000	     42157 ns/op
BenchmarkMessengerSendRecvLargeMessage-4	   50000	     45472 ns/op
BenchmarkMessengerSendRecvMixedMessage-4	   50000	     47393 ns/op
ok  	github.com/mesos/mesos-go/messenger	105.173s
```
 
####environment:

```
OS: Linux yifan-laptop 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
CPU: Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz
MEM: 4G DDR3 1600MHz
```
# Examples

## Building
```
$ go get github.com/tools/godep
$ make
```

## Running
### Start Mesos
You will need a running Mesos master and slaves to run the examples.   For instance, start a local Mesos:
```
$ <mesos-build-install>/bin/mesos-local --ip=127.0.0.1 --port=5050 --roles=golang
```
See http://mesos.apache.org/gettingstarted/ for getting started with Apache Mesos.

### Start the Go scheduler/executor examples
```
$ export EXECUTOR_BIN=$(pwd)/_output/executor
$ ./_output/scheduler -master=127.0.0.1:5050 -executor="$EXECUTOR_BIN" -logtostderr=true
```
If all goes well, you should see output about task completion.
You can also point your browser to the Mesos GUI http://127.0.0.1:5050/ to validate the framework activities.

### Start the Go scheduler with other executors
You can also use the Go `example-scheduler` with executors written in other languages such as  `Python` or `Java`  for further validation (note: to use these executors requires a build of the mesos source code with `make check`):
```
$ ./_output/scheduler -master=127.0.0.1:5050 -executor="<mesos-build>/src/examples/python/test-executor" -logtostderr=true
```
Similarly for the Java version:
```
$ ./_output/scheduler -master=127.0.0.1:5050 -executor="<mesos-build>/src/examples/java/test-executor" -logtostderr=true
```

### Start the Go persistent scheduler/executor examples
```
$ export EXECUTOR_BIN=$(pwd)/_output/executor
$ ./_output/persistent_scheduler -master=127.0.0.1:5050 -executor="$EXECUTOR_BIN" -logtostderr=true -role=golang -mesos_authentication_principal=golang
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
# objx

  * Jump into the [API Documentation](http://godoc.org/github.com/stretchr/objx)
