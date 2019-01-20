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
