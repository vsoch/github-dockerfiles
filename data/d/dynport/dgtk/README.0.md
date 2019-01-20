# PubSub

## Usage

    package main

    import (
      "github.com/dynport/dgtk/pubsub"
      "log"
    )

    func init() {
      log.SetFlags(0)
    }

    type User struct {
      name string
    }

    func main() {
      ps := pubsub.New()
      stringSubscription := ps.Subscribe(func(m string) {
        log.Printf("got string %q", m)
      })
      defer stringSubscription.Close()

      userSubscription := ps.Subscribe(func(u *User) {
        log.Printf("got user %+v", u)
      })
      defer userSubscription.Close()

      ps.Publish("hello")
      ps.Publish("world")

      ps.Publish(&User{name: "Hans"})
      ps.Publish(&User{name: "Meyer"})
    }
# txdbg

Debug SQL transactions inside tests

## Usage

See https://godoc.org/github.com/dynport/dgtk/txdbg
# expect

Custom assertions for go tests.

## Example

	func TestRun(t *testing.T) {
		expect := expect.New(t)

		expect(nil).ToBeNil()
		expect("").ToNotBeNil()

		expect("test").ToHavePrefix("te")
		expect("test").ToHaveSuffix("st")
		expect("test").ToContain("es")
		expect("a").ToNotBeNil()
		expect("a").ToEqual("a")
		expect("a").ToNotEqual("b")

		expect(int64(1)).ToEqual(1)
		expect(1).ToEqual(1)

		expect("test").ToContain("es")

		arr := []string{"a", "b", "c"}
		expect(arr).ToHaveLength(3)
		expect(arr).ToContain("a")
	}
# AMQP Wrapper

This is a simple more golang (use defaults where possible) style wrapper for [github.com/streadway/amqp](http://github.com/streadway/amqp)

## Bind to an exchange (auto-creates the necessary queue)
    package main

    import (
        "log"
        "github.com/dynport/dgtk/amqp"
    )

    func main() {
        connection := &amqp.Connection{
            Address: "amqp://127.0.0.1:5672",
        }
        defer connection.Close()
        queue := &amqp.Queue{
            Name:       "store_metrix",
            AutoDelete: true,
        }
        exchange := &amqp.Exchange{
            Name: "metrix",
        }
        binding := &amqp.Binding{
            Queue:    queue,
            Exchange: exchange,
        }
        e := connection.BindingBind(binding)
        if e != nil {
            return e
        }
        consumer := amqp.Consumer{
            Queue:      queue,
            Connection: connection,
        }
        c, e := consumer.Consume()
        if e != nil {
            log.Fatal(e)
        }
        for del := range c {
          log.Printf("%v", string(del.Body))
        }
    }

# goassets

goassets.go is a script to be put in your e.g. go web project for bundling assets into your binary. It is on purpose not a separate application to a) remove external build dependencies (only go and the go stdlib is needed) and b) so that all people building generate the same output.

## Generating

The final goassets.go file is generated from a 3 files: `tpl/goassets-script/tpl/goassets.go`, `tpl/goassets-tpl/gen.go` and `tpl/goassets-tpl/compiled.go.tpl`

* `tpl/goassets-tpl/comiled.go.tpl` is appended to tpl/goassets-tpl/gen.go (it includes go template code so it would not be compilable)
* `const tpl` in `tpl/goassets-script-tpl/goassets.go` is then replaced with the content of `tpl/gen.go` + `tpl/compiled.go.tpl`

The reason for this is to keep tpl/goassets-tpl/gen.go and tpl/goassets-script-tpl/goassets.go compilable to help editing those bits.

## Bundling

    go run goassets.go --file assets/assets.go assets

This call will bundle all files found in assets/ into the file assets/assets.go. The recommended interface to access assets is provided vi FileSystem() function which is compatible to `http.FileSystem`.

## Development

Set e.g. `assets.DevPath = os.Getenv("GOASSETS_PATH")` and start the program with `GOASSETS_PATH=/path/to/asset/root` to reload all assets from the file system. This way you e.g. do not need to recompile you web server for working on html/css/javascript.

## Examples

See `examples`
# dockerbuild

    Usage of dockerbuild:
      -H="": Docker Host (e.g. 127.0.0.1:4243)
      -R="": Git repository to add to docker archive (e.g. git@github.com:test/repo.git)
      -T="": Tag build with (e.g. elasticsearch)
      -X="": Http Proxy to use (e.g. http://127.0.0.1:1234)
# go-remote-build

Builds a go package on a *real* linux host (e.g. a local VM) and (optionally) uploads the binary to a specific host (via ssh) or S3 bucket.

All local dependencies are uploaded to the linux box before building (from the current GOPATH) so no extra dependencies need to be fetched on the linux host.

    Usage of go-remote-build:
      -bucket="": Upload binary to s3 bucket after building
      -deploy="": Deploy to host after building. Example: ubuntu@127.0.0.1
      -dir="": Dir to build. Default: current directory
      -host="ubuntu@172.16.223.140": Host to build on. Example: ubuntu@127.0.0.1
      -verbose=false: Build using -v flag
# cli

A library to easily create command line interfaces. This is driven by the desire to have a simple but powerful way to
generate those. The existing frameworks failed to deliver features for extended parsing of arguments.

The core ideas of cli are:

* Have routes to actions (like in a web API). There is a fuzzy matching for routes, that allows for giving short cuts
  (like `d s` for `do something`), as long as the given short cuts are unambiguous.
* Actions have parameters like options, flags and arguments. Each action is associated with a struct that has annotated
  fields. The annotations are used to fill the associated fields with the value given on the command line (or by the
  defaults). Action struct must implement the `Runner` interface.
* Options are given via a handle in short or long form (`-c` vs. `--config-file`) and have a value.
* Flags are options with a boolean value, that is set to `true` if the flag is given.
* Arguments are given additionally with out a special handle. This is why order and existence are essential!
* Actions can have hierarchies to facilitate reuse of code.


## Examples

The following example creates a simple CLI action for running commands at a remote host (like `example run on host -c
"uname -a" 192.168.1.1` given the binary has the `example` name and the `uname` command should be executed on
`192.168.1.1`).

	// Struct used to configure an action.
	type ExampleRunner struct {
		Verbose bool   `cli:"type=opt short=v long=verbose"`               // Flag (boolean option) example. This is either set or not.
		Command string `cli:"type=opt short=c long=command required=true"` // Option that has a default value.
		Hosts   string `cli:"type=arg required=true"`                      // Argument with at least one required.
	}
	
	// Run the action. Called when the cli.Run function is called with a route matching the one of this action.
	func (er *ExampleRunner) Run() error {
		// Called when action matches route.
		if er.Verbose {
			log.Printf("Going to execute %q at the following hosts: %v", er.Command, er.Hosts)
		}
		// [..] Executing the SSH command is left to the reader.
		return nil
	}
	
	// Basic example that shows how to register an action to a route and execute it.
	func Example_basic() {
		router := NewRouter()
		router.Register("run/on/hosts", &ExampleRunner{}, "This is an example that pretends to run a given command on a set of hosts.")
		router.Run("run", "on", "host", "-v", "-c", "uname -a", "192.168.1.1")
		router.RunWithArgs() // Run with args given on the command line.
	}

This example used the long notation of the annotation parser. The following would have the very same effect, but be much
more concise:

	// Struct used to configure an action.
	type ExampleRunner struct {
		Verbose bool   `cli:"opt -v --verbose"`          // Flag (boolean option) example. This is either set or not.
		Command string `cli:"opt -c --command required"` // Option that has a default value.
		Hosts   string `cli:"arg required"`              // Argument with at least one required.
	}

If an action doesn't need parameters it's also possible to directly register a function:

	router.RegisterFunc("do/something", func() error { return fmt.Errorf("I should do something") }, "do something")

If there is only a single action for a program the router is not required and this action can be registered directly:

	cli.RunActionWithArgs(&ExampleRunner{})

If you must know whether an option was set, or not you can use pointer values. Note that this has implications, as values must first be tested for nil (aka the option wasn't given on the command line) and must be dereferenced, to get the actual value. For booleans the flag mechanisms is deactivated, i.e. a value (true or false) must be given.

	// Struct used to configure an action.
	type ExampleRunner struct {
		Opt1 *string `cli:"opt -o"`
		Opt2 *int    `cli:"opt -i"`
		Opt3 *bool   `cli:"opt -t"`
	}

# RDS Offsite Backup

## Build

Building is possible using the go way (for further information see the [go website](http://golang.org)).


## Usage

Call the built binary with

	rds_backup snapshot backup <rds-instance-id> <database>

There are options to specify the user and password using the `-u` and `-p`
flags.


## Custom Policy

Having a dedicated user with credentials that are only allowed to execute the
actions required is advised to prevent misuse in case of leaked credentials.
The following IAM policies are required. Make sure to replace the
`account-id` and `<identifier>` placeholders to appropriate values. Changing
the region might be required, too.

	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {
	      "Sid": "Stmt1410789578000",
	      "Effect": "Allow",
	      "Action": [
	        "rds:DescribeDBSnapshots"
	      ],
	      "Resource": [
	        "arn:aws:rds:eu-west-1:<account-id>:db:<identifier>",
	      ]
	    },
	    {
	      "Sid": "Stmt1410790425000",
	      "Effect": "Allow",
	      "Action": [
	        "rds:CreateDBSecurityGroup",
	        "rds:DeleteDBSecurityGroup",
	        "rds:AuthorizeDBSecurityGroupIngress",
	        "rds:ModifyDBInstance"
	      ],
	      "Resource": [
	        "arn:aws:rds:eu-west-1:<account-id>:secgrp:sg-<identifier>-backup",
	      ]
	    },
	    {
	      "Sid": "Stmt1410790425001",
	      "Effect": "Allow",
	      "Action": [
	        "rds:RestoreDBInstanceFromDBSnapshot",
	        "rds:DescribeDBInstances",
	        "rds:ModifyDBInstance",
	        "rds:DeleteDBInstance"
	      ],
	      "Resource": [
	        "arn:aws:rds:eu-west-1:<account-id>:db:<identifier>-backup",
	        "arn:aws:rds:eu-west-1:<account-id>:snapshot:rds:<identifier>-*",
	      ]
	    }
	  ]
	}

# wunderproxy

wunderproxy is a tool to simply manage docker based deployments. It consists of two components:

* proxy:   Forward requests on a specified port to the currently deployed docker container.
* manager: Manage docker containers via an API.


## The Manager

The container manager is used to provide a simple API for handling docker containers and manage the proxy. It has the following actions:
 
* `/status`: This action returns status information on the currently active container, like the number of requests served.
* `/launch`: Will start a new container. The configuration identifier is read from the request body. The actual config file is fetched from S3. Using this information the container will be launched.
* `/switch`: Switches the proxy port to the container given.

The `launch` action fetches the actual configuration from S3 using the requested identifier (it's the hash of the configuration file) as last part of the S3 key. The JSON config expected under this key contains the following information:

* Docker image to launch
* Docker configuration for launching the container (e.g. exports, environment variables, etc.)
* Health check URL
* S3 bucket for image artifacts

The manager expects the currently running configuration to also be available with the `current.json` key suffix on S3. This is the container configuration that will be launched on startup.


## The Proxy

Using a reverse proxy approach the proxy will send incoming requests to a modifiable port. Some minor statistics are collected along the way, that can be retrieved using the manager's API. 


## Usage

The following options can be given to determine what happens when starting the wunderproxy:

* `ProxyAddress`: The listen address of the proxy. The default is to use `0.0.0.0:80`. This is the port that will be forwarded to the docker containers. 
* `ApiAddress`: The listen address of the manager API. The default is `0.0.0.0:8001`.
* `RegistryPort`: The current version of the wunderproxy relies on a local docker registry/distribution (see [here](https://github.com/docker/distribution/blob/master/docs/deploying.md)). The default is to expect the registry on port 8080.
* `ConfigFile`: This is a simple `key=value` based file that can be used to give static environment variables to containers. This is optional of course.

Besides these options there are three arguments required:

* The S3 bucket used to handle container launch configurations.
* The path prefix to be used in the S3 bucket.
* The name of the application handled. This is used as prefix for the containers images.


## Possible Improvements (TODO)

### 502 Handling

If the load is distributed over multiple machines the local wunderproxy instance could try to defer handling a certain requests to one of the other instances if a 502 status code was returned (i.e. if the container wasn't started or doesn't run any more).
 
* Those requests should get an extra header which mark them as `fallback requests`.
* Those requests should not be proxied again.
* The status action (used for health checks for example) shouldn't be forwarded of course.


### Status Page

The manager's status action could be improved to contain:

* the number of open connections by states
* historic status codes
* response times etc.


### Compression, SSL, etc.

Currently the wunderproxy just does the default buffering provided by the Go http library (we measured that to be about 1MB). For unicorn deployments this isn't sufficient to handle `slow clients` (see [unicorn philosophy](http://unicorn.bogomips.org/PHILOSOPHY.html)). We decided to simply use a nginx instance in front of wunderproxy, what of course adds another layer but is sufficient for our case. The nginx layer could be made disposable with an improved request handling in wunderproxy.


### Improved Container Switch

The old container should be kept around until all open connections are handled (or a timeout occurs).s# DynamoDB

## Usage

	package main

	import (
		"log"
		"os"
		"strings"

		"github.com/dynport/gocloud/aws"
		"github.com/dynport/gocloud/aws/dynamodb"
	)

	var tableName = os.Getenv("TABLE_NAME")

	func run() error {
		client := aws.NewFromEnv()

		// list tables
		header("ListTables")
		listTabels := &dynamodb.ListTables{}
		if rsp, e := listTabels.Execute(client); e != nil {
			return e
		} else {
			log.Printf("tables: %v", rsp.TableNames)
		}

		// describe table
		header("DescribeTable")
		describeTable := &dynamodb.DescribeTable{TableName: tableName}
		if rsp, e := describeTable.Execute(client); e != nil {
			return e
		} else if rsp.Table != nil {
			log.Printf("name: %q", rsp.Table.TableName)
			log.Printf("status: %q", rsp.Table.TableStatus)
			log.Printf("item count: %d", rsp.Table.ItemCount)
			log.Printf("size in bytes: %d", rsp.Table.TableSizesBytes)
			if rsp.Table.ProvisionedThroughput != nil {
				log.Printf("read: %d", rsp.Table.ProvisionedThroughput.ReadCapacityUnits)
				log.Printf("write: %d", rsp.Table.ProvisionedThroughput.WriteCapacityUnits)
				log.Printf("decreases: %d", rsp.Table.ProvisionedThroughput.NumberOfDecreasesToday)
			}
		}

		// put item
		header("PutItem")
		put := &dynamodb.PutItem{
			TableName: tableName,
			Item: dynamodb.Item{
				"Key":   {S: "hello"},
				"Value": {S: "world"},
			},
			ReturnConsumedCapacity: "TOTAL",
		}

		if _, e := put.Execute(client); e != nil {
			return e
		} else {
			log.Printf("put item!")
		}

		// get item
		header("GetItem")
		item := &dynamodb.Item{"Key": {S: "hello"}}
		getItem := &dynamodb.GetItem{
			TableName: tableName,
			Key:       item,
			ReturnConsumedCapacity: "TOTAL",
			ConsistentRead:         "true",
		}

		if rsp, e := getItem.Execute(client); e != nil {
			return e
		} else {
			if rsp.ConsumedCapacity != nil {
				log.Printf("consumed capacity: %.1f", rsp.ConsumedCapacity.CapacityUnits)
			}
			for k, v := range rsp.Item {
				log.Printf("%s: %#v", k, v)

			}
		}

		// scan
		header("Scan")
		scan := &dynamodb.Scan{
			TableName: tableName,
			Limit:     10,
			ReturnConsumedCapacity: "TOTAL",
		}
		if sr, e := scan.Execute(client); e != nil {
			return e
		} else {
			log.Printf("Count: %d", sr.Count)
			if sr.ConsumedCapacity != nil {
				log.Printf("ConsumedCapacity: %.1f", sr.ConsumedCapacity.CapacityUnits)
			}
			for _, i := range sr.Items {
				for k, v := range i {
					log.Printf("%s: %#v", k, v)

				}
			}
		}
		return nil
	}

	func main() {
		log.SetFlags(0)
		e := run()
		if e != nil {
			log.Printf("ERROR: %q", e.Error())
			log.Fatal(e)
		}
	}

	func header(message string) {
		log.Printf("%s %s %s", strings.Repeat("*", 50), message, strings.Repeat("*", 50))
	}
# cli

A library to easily create command line interfaces. This is driven by the desire to have a simple but powerful way to
generate those. The existing frameworks failed to deliver features for extended parsing of arguments.

The core ideas of cli are:

* Have routes to actions (like in a web API). There is a fuzzy matching for routes, that allows for giving short cuts
  (like `d s` for `do something`), as long as the given short cuts are unambiguous.
* Actions have parameters like options, flags and arguments. Each action is associated with a struct that has annotated
  fields. The annotations are used to fill the associated fields with the value given on the command line (or by the
  defaults). Action struct must implement the `Runner` interface.
* Options are given via a handle in short or long form (`-c` vs. `--config-file`) and have a value.
* Flags are options with a boolean value, that is set to `true` if the flag is given.
* Arguments are given additionally with out a special handle. This is why order and existence are essential!
* Actions can have hierarchies to facilitate reuse of code.


## Examples

The following example creates a simple CLI action for running commands at a remote host (like `example run on host -c
"uname -a" 192.168.1.1` given the binary has the `example` name and the `uname` command should be executed on
`192.168.1.1`).

	// Struct used to configure an action.
	type ExampleRunner struct {
		Verbose bool   `cli:"type=opt short=v long=verbose"`               // Flag (boolean option) example. This is either set or not.
		Command string `cli:"type=opt short=c long=command required=true"` // Option that has a default value.
		Hosts   string `cli:"type=arg required=true"`                      // Argument with at least one required.
	}
	
	// Run the action. Called when the cli.Run function is called with a route matching the one of this action.
	func (er *ExampleRunner) Run() error {
		// Called when action matches route.
		if er.Verbose {
			log.Printf("Going to execute %q at the following hosts: %v", er.Command, er.Hosts)
		}
		// [..] Executing the SSH command is left to the reader.
		return nil
	}
	
	// Basic example that shows how to register an action to a route and execute it.
	func Example_basic() {
		router := NewRouter()
		router.Register("run/on/hosts", &ExampleRunner{}, "This is an example that pretends to run a given command on a set of hosts.")
		router.Run("run", "on", "host", "-v", "-c", "uname -a", "192.168.1.1")
		router.RunWithArgs() // Run with args given on the command line.
	}

This example used the long notation of the annotation parser. The following would have the very same effect, but be much
more concise:

	// Struct used to configure an action.
	type ExampleRunner struct {
		Verbose bool   `cli:"opt -v --verbose"`          // Flag (boolean option) example. This is either set or not.
		Command string `cli:"opt -c --command required"` // Option that has a default value.
		Hosts   string `cli:"arg required"`              // Argument with at least one required.
	}

If an action doesn't need parameters it's also possible to directly register a function:

	router.RegisterFunc("do/something", func() error { return fmt.Errorf("I should do something") }, "do something")

If there is only a single action for a program the router is not required and this action can be registered directly:

	cli.RunActionWithArgs(&ExampleRunner{})

If you must know whether an option was set, or not you can use pointer values. Note that this has implications, as values must first be tested for nil (aka the option wasn't given on the command line) and must be dereferenced, to get the actual value. For booleans the flag mechanisms is deactivated, i.e. a value (true or false) must be given.

	// Struct used to configure an action.
	type ExampleRunner struct {
		Opt1 *string `cli:"opt -o"`
		Opt2 *int    `cli:"opt -i"`
		Opt3 *bool   `cli:"opt -t"`
	}

# wunderproxy

wunderproxy is a tool to simply manage docker based deployments. It consists of two components:

* proxy:   Forward requests on a specified port to the currently deployed docker container.
* manager: Manage docker containers via an API.


## The Manager

The container manager is used to provide a simple API for handling docker containers and manage the proxy. It has the following actions:
 
* `/status`: This action returns status information on the currently active container, like the number of requests served.
* `/launch`: Will start a new container. The configuration identifier is read from the request body. The actual config file is fetched from S3. Using this information the container will be launched.
* `/switch`: Switches the proxy port to the container given.

The `launch` action fetches the actual configuration from S3 using the requested identifier (it's the hash of the configuration file) as last part of the S3 key. The JSON config expected under this key contains the following information:

* Docker image to launch
* Docker configuration for launching the container (e.g. exports, environment variables, etc.)
* Health check URL
* S3 bucket for image artifacts

The manager expects the currently running configuration to also be available with the `current.json` key suffix on S3. This is the container configuration that will be launched on startup.


## The Proxy

Using a reverse proxy approach the proxy will send incoming requests to a modifiable port. Some minor statistics are collected along the way, that can be retrieved using the manager's API. 


## Usage

The following options can be given to determine what happens when starting the wunderproxy:

* `ProxyAddress`: The listen address of the proxy. The default is to use `0.0.0.0:80`. This is the port that will be forwarded to the docker containers. 
* `ApiAddress`: The listen address of the manager API. The default is `0.0.0.0:8001`.
* `RegistryPort`: The current version of the wunderproxy relies on a local docker registry/distribution (see [here](https://github.com/docker/distribution/blob/master/docs/deploying.md)). The default is to expect the registry on port 8080.
* `ConfigFile`: This is a simple `key=value` based file that can be used to give static environment variables to containers. This is optional of course.

Besides these options there are three arguments required:

* The S3 bucket used to handle container launch configurations.
* The path prefix to be used in the S3 bucket.
* The name of the application handled. This is used as prefix for the containers images.


## Possible Improvements (TODO)

### 502 Handling

If the load is distributed over multiple machines the local wunderproxy instance could try to defer handling a certain requests to one of the other instances if a 502 status code was returned (i.e. if the container wasn't started or doesn't run any more).
 
* Those requests should get an extra header which mark them as `fallback requests`.
* Those requests should not be proxied again.
* The status action (used for health checks for example) shouldn't be forwarded of course.


### Status Page

The manager's status action could be improved to contain:

* the number of open connections by states
* historic status codes
* response times etc.


### Compression, SSL, etc.

Currently the wunderproxy just does the default buffering provided by the Go http library (we measured that to be about 1MB). For unicorn deployments this isn't sufficient to handle `slow clients` (see [unicorn philosophy](http://unicorn.bogomips.org/PHILOSOPHY.html)). We decided to simply use a nginx instance in front of wunderproxy, what of course adds another layer but is sufficient for our case. The nginx layer could be made disposable with an improved request handling in wunderproxy.


### Improved Container Switch

The old container should be kept around until all open connections are handled (or a timeout occurs).s# gossh

Golang ssh library

## Example
    package main

    import (
      "github.com/dynport/gossh"
      "log"
    )

    // returns a function of type gossh.Writer func(...interface{})
    // MakeLogger just adds a prefix (DEBUG, INFO, ERROR)
    func MakeLogger(prefix string) gossh.Writer {
      return func(args ...interface{}) {
        log.Println((append([]interface{}{prefix}, args...))...)
      }
    }

    func main() {
      client := gossh.New("some.host", "user")
      // my default agent authentication is used. use
      // client.SetPassword("<secret>")
      // for password authentication
      client.DebugWriter = MakeLogger("DEBUG")
      client.InfoWriter = MakeLogger("INFO ")
      client.ErrorWriter = MakeLogger("ERROR")

      defer client.Close()
      rsp, e := client.Execute("uptime")
      if e != nil {
        client.ErrorWriter(e.Error())
      }
      client.InfoWriter(rsp.String())

      rsp, e = client.Execute("echo -n $(cat /proc/loadavg); cat /does/not/exists")
      if e != nil {
        client.ErrorWriter(e.Error())
        client.ErrorWriter("STDOUT: " + rsp.Stdout())
        client.ErrorWriter("STDERR: " + rsp.Stderr())
      }
    }

Prints this result:

    2013/08/25 00:31:40 DEBUG connecting some.host
    2013/08/25 00:31:41 INFO  [EXEC  ] uptime
    2013/08/25 00:31:41 DEBUG 22:31:41 up 375 days, 10:44,  0 users,  load average: 0.09, 0.13, 0.22
    2013/08/25 00:31:41 INFO  => 0.944143
    2013/08/25 00:31:41 INFO  map[stdout:72 bytes stderr:0 bytes runtime:0.944202 status:0]
    2013/08/25 00:31:41 DEBUG already connected
    2013/08/25 00:31:41 INFO  [EXEC  ] echo -n $(cat /proc/loadavg); cat /does/not/exists
    2013/08/25 00:31:41 DEBUG 0.09 0.13 0.22 1/455 23396
    2013/08/25 00:31:41 ERROR cat: /does/not/exists
    2013/08/25 00:31:41 ERROR : No such file or directory
    2013/08/25 00:31:41 INFO  => 0.067075
    2013/08/25 00:31:41 ERROR Process exited with: 1. Reason was:  ()
    2013/08/25 00:31:41 ERROR STDOUT: 0.09 0.13 0.22 1/455 23396
    2013/08/25 00:31:41 ERROR STDERR: cat: /does/not/exists: No such file or directory

## Tunnelling HTTP Connections
For services not bound to the public interface of a machine, tunnelling is a quite nice SSH feature. It allows to use a
remote service like it is running at the local machine. This concept is used in the HTTP client returned by the
NewHttpClient function. It is a common net/http.Client, but all requests are sent through the SSH connection given.
# tskip

A little bit more convenience and locality for writing go tests.

Introducing: "function based tests"

## What

tskip allows using the go test methods `testing.Log` etc. from inside test helpers without loosing locality. It can also fix the locality of errors in sub packages.

## How

The tskip library methods `found in tskip/tskip` uses `caller.Runtime` with the right skip values to get the location from where the function is called. It then prepends the output with `\r` to "remove" the location which is printed by the stdlib.

The vim quickfix window does not care about carriage returns though, so vim user would still be directed to location deleted by the carriage return. That is why tskip also provides a simple decorator binary/script which wraps `go test` and completely strips this not wanted output from what vim sees.

	tskip -v ./... # just decorates the output of go test -v ./...

As go changes to the directories of all subpackages when running tests, most testing output in go only displays file names which can be misleading also mess up the vim quickfix window. To fix this, tskip sets the `TEST_ROOT` to the directory from which tskip is executed so this prefix can be removed from the file names. If `TEST_ROOT` is not set the tskip library prints the full file path (which also does not break vim quickfix).

## What can I do with it?

With tskip you can write your own test helpers but also improve locality for table based tests by migrating them to "function based tests".


TODO: add example and explain why this is better

## Examples

See `main_test.go` for some examples.

Run 

	TEST_SIMULATE=true go run main.go -v ./...

to test the output on the command line or

	:make simulate

inside vim to see how this fixes the quickfix issue.
# Slack Notifier

This small helper will execute a given command and send a configured message to
slack that has

* status success on return value 0 of the command, and
* status error on any other return value.

For example

	slack_notify "testing slack_notify" do_something

would call the `do_something` command (that of course must be available in the
callers path) and send a message with the text "testing slack_notify" to the
slack organization and channel configured in the `${HOME}/.slack.conf` file.

The configuration file is in JSON format and has the following form:

	{
		"webhook_url": "https://hooks.slack.com/services/...",
		"channel": "#slack_notify_channel",
		"username": "Mr. Slack Notify",
		"emoji": ":ghost:"
	}

If `channel`, `username` or `emoji` are not specified the values of the given
webhook URL are used (see your slack integration configuration for that
respective webhook).
# es-dump dumps a given elasticsearch index

## Usage

		Usage of es-dump:
			-a="http://127.0.0.1:9200": Address
			-b=1000: Batch Size
			-i="": Index Name
			-o="": Output file
# bsondecoder

## Usage

    func run(bsonPath string) error {
      f, e := os.Open(bsonPath)
      if e != nil {
        return e
      }
      defer f.Close()

      dec := bsondecoder.New(f)
      for {
        var m bson.M
        if e = dec.Decode(&m); e != nil {
          return e
        }
        log.Printf("%#v", m)
      }
      return nil
    }
# Virtual Box Manager

This is a tool to easily manage virtual boxes. Goals are to:

* simplify usage of VirtualBox.
* have a set of machine images available that work out of the box.
* make cloning, starting, and deleting as fast as possible.


## Installation

Install [VirtualBox](http://download.virtualbox.org/virtualbox/4.3.6/VirtualBox-4.3.6-91406-OSX.dmg) and the vbox tool:

	go get github.com/dynport/dgtk/vbox

Now retrieve your local template engine.

	vbox get template ubuntu_precise.ova template

`ubuntu_precise.ova` is the image to be downloaded and `template` the name of the machine created (`template` is the
default in the `clone` command). The server can be provided using `--source` option.


## Usage

The following actions are available:

* `vbox list` will return the list of all available virtual machines (add `-r` to only show running machines).
* `vbox vm clone <vm>` will clone the template you just downloaded to a new machine with the `<vm>` name.
* `vbox vm start <vm>` will start the virtual machine with the given name.
* `vbox vm ssh into <vm>` will open an ssh connection to this machine (might take a few seconds as it tries to wait till
  the machine finished booting).

For more help run `vbox -h` or `vbox <command> -h`.


## Creating Images

Creating (or extending) images requires the following steps to be taken:

* Install or extend the image as wanted.
* Make sure the VirtualBox GuestAdditions are installed (for Linux remember to first install the `dkms` package).
* Remove the file `/etc/udev/rules.d/70-persistent-net.rules` so that the template's MAC is reset afterwards (otherwise
  networking will fail horribly).
* Shutdown the virtual machine.
* Create a snapshot. I prefer the `base` name as this is the default for the clone operation.
* For sharing export the machine to an `.ova` file.

# goup: Creating Upstart Scripts

Upstart is a mechanism to handle services on Ubuntu (like SysInitV used to do). Keep in mind that this stuff requires
quite some knowledge and understanding on how processes can daemonize.

Currently there is only support for a small subset of possible options. This will be expanded as required.

Usage is as simple as creating an value of the Upstart type and call it's `CreateScript() string` method to get the
string version of the resulting upstart script. Write that to the according location.


# Crypter

## Goal

Store encrypted BLOBs of data for multiple users on a server. New users can be added by all existing users, BLOBs can be changed by all users.

## Create user

* All user data is stored in a user specific directory `$ROOT/users/<login>`
* Creating of users requires the login name and a user specific password
* A new 4096 bit RSA keypair is created, the public key is stored unencrypted, the privat key is encrypted with AES and the provided password

## Store BLOB for a specific user

* a new 32 byte secret AES key is created
* the BLOB is encrypted and stored with the generated key `$ROOT/users/<login>/data.<version>
* the generated key is encrypted with the public key of the user

## Read BLOB by user

* the private RSA key of the user is decrypted by the user provided password
* the secret key of the BLOB is decrypted with private RSA key
* the BLOB es decrypted withg the secret key


## Approach

All users have secret 32 byte keys which are provided with each request.

## Requirements

All stored BLOBs need to have some version (or checksum) in their names.
# dp-es

CLI helper for ElasticSearch 

	aliases create     <Index> <AliasName>    Create alias       
	aliases ls                                List Aliases       
	aliases rm         <Index> <AliasName>    Delete alias       
	aliases swap       <NewIndex> <AliasName> Swap Alias         
	index dump         <IndexName>            Dump an index      
	index ls                                  List es indexes    
	index rm           <Name>                 Delete index       
	spy                <ESAddress>            Spy on es requests 
gocli
=====

[![Build Status](https://travis-ci.org/dynport/gocli.png?branch=master)](https://travis-ci.org/dynport/gocli)

Golang library for CLI applications
# aws-sts

Simple wrapper for the aws CLI tools to support authentication with MFA tokens.

## About

`aws-sts` uses "normal" AWS credentials and a provided MFA token to get STS tokens. These tokens are cached on disk so you are only asked for a new MFA token when the STS token expired.

Currently the default (and hardcoded) TTL for the STS token is 3600 seconds (so you will be asked for a new MFA token at most once an hour).

## Setup

`aws-sts` relies on the official AWS command lines tools which are best installed with `pip install awscli`.

`aws-sts` reads your original access key and secret from a JSON file containing these fields:

	{
		"aws_access_key_id": "YOUR_KEY",
		"aws_secret_access_key": "YOUR_SECRET",
		"aws_default_region": "DEFAULT_REGION"
	}

The location of that JSON file must be specified using the ENV variable `AWS_CREDENTIALS_PATH` 

You must also register one MFA device (currently the first mfa device found is used).

## Usage

### direct

		AWS_CREDENTIALS_PATH=/path/to/config.json aws-sts

### alias
Alternatively you can also create aliases for `aws-sts`

		alias aws="AWS_CREDENTIALS_PATH=/path/to/default.json aws-sts"
		alias aws-private="AWS_CREDENTIALS_PATH=/path/to/private.json aws-sts"
