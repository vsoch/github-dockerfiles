package main

import (
	"fmt"
	"log"

	"github.com/docker/docker/pkg/reexec"
	"github.com/docker/libnetwork"
	"github.com/docker/libnetwork/config"
	"github.com/docker/libnetwork/netlabel"
	"github.com/docker/libnetwork/options"
)

func main() {
	if reexec.Init() {
		return
	}

	// Select and configure the network driver
	networkType := "bridge"

	// Create a new controller instance
	driverOptions := options.Generic{}
	genericOption := make(map[string]interface{})
	genericOption[netlabel.GenericData] = driverOptions
	controller, err := libnetwork.New(config.OptionDriverConfig(networkType, genericOption))
	if err != nil {
		log.Fatalf("libnetwork.New: %s", err)
	}

	// Create a network for containers to join.
	// NewNetwork accepts Variadic optional arguments that libnetwork and Drivers can use.
	network, err := controller.NewNetwork(networkType, "network1", "")
	if err != nil {
		log.Fatalf("controller.NewNetwork: %s", err)
	}

	// For each new container: allocate IP and interfaces. The returned network
	// settings will be used for container infos (inspect and such), as well as
	// iptables rules for port publishing. This info is contained or accessible
	// from the returned endpoint.
	ep, err := network.CreateEndpoint("Endpoint1")
	if err != nil {
		log.Fatalf("network.CreateEndpoint: %s", err)
	}

	// Create the sandbox for the container.
	// NewSandbox accepts Variadic optional arguments which libnetwork can use.
	sbx, err := controller.NewSandbox("container1",
		libnetwork.OptionHostname("test"),
		libnetwork.OptionDomainname("docker.io"))
	if err != nil {
		log.Fatalf("controller.NewSandbox: %s", err)
	}

	// A sandbox can join the endpoint via the join api.
	err = ep.Join(sbx)
	if err != nil {
		log.Fatalf("ep.Join: %s", err)
	}

	// libnetwork client can check the endpoint's operational data via the Info() API
	epInfo, err := ep.DriverInfo()
	if err != nil {
		log.Fatalf("ep.DriverInfo: %s", err)
	}

	macAddress, ok := epInfo[netlabel.MacAddress]
	if !ok {
		log.Fatal("failed to get mac address from endpoint info")
	}

	fmt.Printf("Joined endpoint %s (%s) to sandbox %s (%s)\n", ep.Name(), macAddress, sbx.ContainerID(), sbx.Key())
}
# libnetwork - networking for containers

[![Circle CI](https://circleci.com/gh/docker/libnetwork/tree/master.svg?style=svg)](https://circleci.com/gh/docker/libnetwork/tree/master) [![Coverage Status](https://coveralls.io/repos/docker/libnetwork/badge.svg)](https://coveralls.io/r/docker/libnetwork) [![GoDoc](https://godoc.org/github.com/docker/libnetwork?status.svg)](https://godoc.org/github.com/docker/libnetwork) [![Go Report Card](https://goreportcard.com/badge/github.com/docker/libnetwork)](https://goreportcard.com/report/github.com/docker/libnetwork)

Libnetwork provides a native Go implementation for connecting containers

The goal of libnetwork is to deliver a robust Container Network Model that provides a consistent programming interface and the required network abstractions for applications.

#### Design
Please refer to the [design](docs/design.md) for more information.

#### Using libnetwork

There are many networking solutions available to suit a broad range of use-cases. libnetwork uses a driver / plugin model to support all of these solutions while abstracting the complexity of the driver implementations by exposing a simple and consistent Network Model to users.


```go
import (
	"fmt"
	"log"

	"github.com/docker/docker/pkg/reexec"
	"github.com/docker/libnetwork"
	"github.com/docker/libnetwork/config"
	"github.com/docker/libnetwork/netlabel"
	"github.com/docker/libnetwork/options"
)

func main() {
	if reexec.Init() {
		return
	}

	// Select and configure the network driver
	networkType := "bridge"

	// Create a new controller instance
	driverOptions := options.Generic{}
	genericOption := make(map[string]interface{})
	genericOption[netlabel.GenericData] = driverOptions
	controller, err := libnetwork.New(config.OptionDriverConfig(networkType, genericOption))
	if err != nil {
		log.Fatalf("libnetwork.New: %s", err)
	}

	// Create a network for containers to join.
	// NewNetwork accepts Variadic optional arguments that libnetwork and Drivers can use.
	network, err := controller.NewNetwork(networkType, "network1", "")
	if err != nil {
		log.Fatalf("controller.NewNetwork: %s", err)
	}

	// For each new container: allocate IP and interfaces. The returned network
	// settings will be used for container infos (inspect and such), as well as
	// iptables rules for port publishing. This info is contained or accessible
	// from the returned endpoint.
	ep, err := network.CreateEndpoint("Endpoint1")
	if err != nil {
		log.Fatalf("network.CreateEndpoint: %s", err)
	}

	// Create the sandbox for the container.
	// NewSandbox accepts Variadic optional arguments which libnetwork can use.
	sbx, err := controller.NewSandbox("container1",
		libnetwork.OptionHostname("test"),
		libnetwork.OptionDomainname("docker.io"))
	if err != nil {
		log.Fatalf("controller.NewSandbox: %s", err)
	}

	// A sandbox can join the endpoint via the join api.
	err = ep.Join(sbx)
	if err != nil {
		log.Fatalf("ep.Join: %s", err)
	}

	// libnetwork client can check the endpoint's operational data via the Info() API
	epInfo, err := ep.DriverInfo()
	if err != nil {
		log.Fatalf("ep.DriverInfo: %s", err)
	}

	macAddress, ok := epInfo[netlabel.MacAddress]
	if !ok {
		log.Fatalf("failed to get mac address from endpoint info")
	}

	fmt.Printf("Joined endpoint %s (%s) to sandbox %s (%s)\n", ep.Name(), macAddress, sbx.ContainerID(), sbx.Key())
}
```

## Future
Please refer to [roadmap](ROADMAP.md) for more information.

## Contributing

Want to hack on libnetwork? [Docker's contributions guidelines](https://github.com/docker/docker/blob/master/CONTRIBUTING.md) apply.

## Copyright and license
Code and documentation copyright 2015 Docker, inc. Code released under the Apache 2.0 license. Docs released under Creative commons.
# LibNetwork Integration Tests

Integration tests provide end-to-end testing of LibNetwork and Drivers.

While unit tests verify the code is working as expected by relying on mocks and
artificially created fixtures, integration tests actually use real docker
engines and communicate to it through the CLI.

Note that integration tests do **not** replace unit tests and Docker is used as a good use-case.

As a rule of thumb, code should be tested thoroughly with unit tests.
Integration tests on the other hand are meant to test a specific feature end to end.

Integration tests are written in *bash* using the
[bats](https://github.com/sstephenson/bats) framework.

## Pre-Requisites

1. Bats (https://github.com/sstephenson/bats#installing-bats-from-source)
2. Docker Machine (https://github.com/docker/machine)
3. Virtualbox (as a Docker machine driver)

## Running integration tests

* Start by [installing] (https://github.com/sstephenson/bats#installing-bats-from-source) *bats* on your system.
* If not done already, [install](https://docs.docker.com/machine/) *docker-machine* into /usr/bin
* Make sure Virtualbox is installed as well, which will be used by docker-machine as a driver to launch VMs

In order to run all integration tests, pass *bats* the test path:
```
$ bats test/integration/daemon-configs.bats
```


Package resolvconf provides utility code to query and update DNS configuration in /etc/resolv.conf
SERVER

cd test/networkdb
env GOOS=linux go build -v testMain.go && docker build -t dockereng/e2e-networkdb .
(only for testkit case) docker push dockereng/e2e-networkdb

Run server: docker service create --name testdb --network net1 --replicas 3 --env TASK_ID="{{.Task.ID}}" -p mode=host,target=8000 dockereng/e2e-networkdb server 8000

CLIENT

cd test/networkdb
Join cluster: docker run -it --network net1 dockereng/e2e-networkdb client join testdb 8000
Join network: docker run -it --network net1 dockereng/e2e-networkdb client join-network testdb 8000 test
Run test: docker run -it --network net1 dockereng/e2e-networkdb client write-delete-unique-keys testdb 8000 test tableBla 3 10
check table: curl "localhost:32768/gettable?nid=test&tname=table_name"
---
description: Learn to use the built-in network debugger to debug overlay networking problems
keywords: network, troubleshooting, debug
title: Debug overlay or swarm networking issues
---

**WARNING**
This tool can change the internal state of the libnetwork API, be really mindful
on its use and read carefully the following guide. Improper use of it will damage
or permanently destroy the network configuration.


Docker CE 17.12 and higher introduce a network debugging tool designed to help
debug issues with overlay networks and swarm services running on Linux hosts.
When enabled, a network diagnostic server listens on the specified port and
provides diagnostic information. The network debugging tool should only be
started to debug specific issues, and should not be left running all the time.

Information about networks is stored in the database, which can be examined using
the API. Currently the database contains information about the overlay network
as well as the service discovery data.

The Docker API exposes endpoints to query and control the network debugging
tool. CLI integration is provided as a preview, but the implementation is not
yet considered stable and commands and options may change without notice.

The tool is available into 2 forms:
1) client only: dockereng/network-diagnostic:onlyclient
2) docker in docker version: dockereng/network-diagnostic:17.12-dind
The latter allows to use the tool with a cluster running an engine older than 17.12

## Enable the diagnostic server

The tool currently only works on Docker hosts running on Linux. To enable it on a node
follow the step below.

1.  Set the `network-diagnostic-port` to a port which is free on the Docker
    host, in the `/etc/docker/daemon.json` configuration file.

    ```json
    “network-diagnostic-port”: <port>
    ```

2.  Get the process ID (PID) of the `dockerd` process. It is the second field in
    the output, and is typically a number from 2 to 6 digits long.

    ```bash
    $ ps aux |grep dockerd | grep -v grep
    ```

3.  Reload the Docker configuration without restarting Docker, by sending the
    `HUP` signal to the PID you found in the previous step.

    ```bash
    kill -HUP <pid-of-dockerd>
    ```

If systemd is used the command `systemctl reload docker` will be enough


A message like the following will appear in the Docker host logs:

```none
Starting the diagnostic server listening on <port> for commands
```

## Disable the diagnostic tool

Repeat these steps for each node participating in the swarm.

1.  Remove the `network-diagnostic-port` key from the `/etc/docker/daemon.json`
    configuration file.

2.  Get the process ID (PID) of the `dockerd` process. It is the second field in
    the output, and is typically a number from 2 to 6 digits long.

    ```bash
    $ ps aux |grep dockerd | grep -v grep
    ```

3.  Reload the Docker configuration without restarting Docker, by sending the
    `HUP` signal to the PID you found in the previous step.

    ```bash
    kill -HUP <pid-of-dockerd>
    ```

A message like the following will appear in the Docker host logs:

```none
Disabling the diagnostic server
```

## Access the diagnostic tool's API

The network diagnostic tool exposes its own RESTful API. To access the API,
send a HTTP request to the port where the tool is listening. The following
commands assume the tool is listening on port 2000.

Examples are not given for every endpoint.

### Get help

```bash
$ curl localhost:2000/help

OK
/updateentry
/getentry
/gettable
/leavenetwork
/createentry
/help
/clusterpeers
/ready
/joinnetwork
/deleteentry
/networkpeers
/
/join
```

### Join or leave the network database cluster

```bash
$ curl localhost:2000/join?members=ip1,ip2,...
```

```bash
$ curl localhost:2000/leave?members=ip1,ip2,...
```

`ip1`, `ip2`, ... are the swarm node ips (usually one is enough)

### Join or leave a network

```bash
$ curl localhost:2000/joinnetwork?nid=<network id>
```

```bash
$ curl localhost:2000/leavenetwork?nid=<network id>
```

`network id` can be retrieved on the manager with `docker network ls --no-trunc` and has
to be the full length identifier

### List cluster peers

```bash
$ curl localhost:2000/clusterpeers
```

### List nodes connected to a given network

```bash
$ curl localhost:2000/networkpeers?nid=<network id>
```
`network id` can be retrieved on the manager with `docker network ls --no-trunc` and has
to be the full length identifier

### Dump database tables

The tables are called `endpoint_table` and `overlay_peer_table`.
The `overlay_peer_table` contains all the overlay forwarding information
The `endpoint_table` contains all the service discovery information

```bash
$ curl localhost:2000/gettable?nid=<network id>&tname=<table name>
```

### Interact with a specific database table

The tables are called `endpoint_table` and `overlay_peer_table`.

```bash
$ curl localhost:2000/<method>?nid=<network id>&tname=<table name>&key=<key>[&value=<value>]
```

Note:
operations on tables have node ownership, this means that are going to remain persistent till
the node that inserted them is part of the cluster

## Access the diagnostic tool's CLI

The CLI is provided as a preview and is not yet stable. Commands or options may
change at any time.

The CLI executable is called `diagnosticClient` and is made available using a
standalone container.

`docker run --net host dockereng/network-diagnostic:onlyclient -v -net <full network id> -t sd`

The following flags are supported:

| Flag          | Description                                     |
|---------------|-------------------------------------------------|
| -t <string>   | Table one of `sd` or `overlay`.                 |
| -ip <string>  | The IP address to query. Defaults to 127.0.0.1. |
| -net <string> | The target network ID.                          |
| -port <int>   | The target port. (default port is 2000)         |
| -a            | Join/leave network                              |
| -v            | Enable verbose output.                          |

*NOTE*
By default the tool won't try to join the network. This is following the intent to not change
the state on which the node is when the diagnostic client is run. This means that it is safe
to run the diagnosticClient against a running daemon because it will just dump the current state.
When using instead the diagnosticClient in the containerized version the flag `-a` MUST be passed
to avoid retrieving empty results. On the other side using the `-a` flag against a loaded daemon
will have the undesirable side effect to leave the network and so cutting down the data path for
that daemon.

### Container version of the diagnostic tool

The CLI is provided as a container with a 17.12 engine that needs to run using privileged mode.
*NOTE*
Remember that table operations have ownership, so any `create entry` will be persistent till
the diagnostic container is part of the swarm.

1.  Make sure that the node where the diagnostic client will run is not part of the swarm, if so do `docker swarm leave -f`

2.  To run the container, use a command like the following:

    ```bash
    $ docker container run --name net-diagnostic -d --privileged --network host dockereng/network-diagnostic:17.12-dind
    ```

3.  Connect to the container using `docker exec -it <container-ID> sh`,
    and start the server using the following command:

    ```bash
    $ kill -HUP 1
    ```

4.  Join the diagnostic container to the swarm, then run the diagnostic CLI within the container.

    ```bash
    $ ./diagnosticClient <flags>...
    ```

4.  When finished debugging, leave the swarm and stop the container.

### Examples

The following commands dump the service discovery table and verify node
ownership.

*NOTE*
Remember to use the full network ID, you can easily find that with `docker network ls --no-trunc`

**Service discovery and load balancer:**

```bash
$ diagnostiClient -t sd -v -net n8a8ie6tb3wr2e260vxj8ncy4 -a
```

**Overlay network:**

```bash
$ diagnostiClient -port 2001 -t overlay -v -net n8a8ie6tb3wr2e260vxj8ncy4 -a
```
# Docker Swarm Service Driller(ssd)

ssd is a troubleshooting utility for Docker swarm networks. 

### control-plane and datapath consistency check on a node
ssd checks for the consistency between docker network control-plane (from the docker daemon in-memory state) and kernel data path programming. Currently the tool checks only for the consistency of the Load balancer (implemented using IPVS).

In a three node swarm cluser ssd status for a overlay network `ov2` which has three services running, each replicated to 3 instances.

````bash
vagrant@net-1:~/code/go/src/github.com/docker/docker-e2e/tests$ docker run -v /var/run/docker.sock:/var/run/docker.sock -v /var/run/docker/netns:/var/run/docker/netns --privileged --net=host sanimej/ssd ov2
Verifying LB programming for containers on network ov2
Verifying container /s2.3.ltrdwef0iqf90rqauw3ehcs56...
service s2... OK
service s3... OK
service s1... OK
Verifying container /s3.3.nyhwvdvnocb4wftyhb8dr4fj8...
service s2... OK
service s3... OK
service s1... OK
Verifying container /s1.3.wwx5tuxhnvoz5vrb8ohphby0r...
service s2... OK
service s3... OK
service s1... OK
Verifying LB programming for containers on network ingress
Verifying container Ingress...
service web... OK
````

ssd checks the required iptables programming to direct an incoming packet with the <host ip>:<published port> to the right <backend ip>:<target port>

### control-plane consistency check across nodes in a cluster

Docker networking uses a gossip protocol to synchronize networking state across nodes  in a cluster. ssd's `gossip-consistency` command verifies if the state maintained by all the nodes are consistent.

````bash
In a three node cluster with services running on an overlay network ov2 ssd consistency-checker shows 

vagrant@net-1:~/code/go/src/github.com/docker/docker-e2e/tests$ docker run -v /var/run/docker.sock:/var/run/docker.sock -v /var/run/docker/netns:/var/run/docker/netns --privileged sanimej/ssd ov2 gossip-consistency
Node id: sjfp0ca8f43rvnab6v7f21gq0 gossip hash c57d89094dbb574a37930393278dc282

Node id: bg228r3q9095grj4wxkqs80oe gossip hash c57d89094dbb574a37930393278dc282

Node id: 6jylcraipcv2pxdricqe77j5q gossip hash c57d89094dbb574a37930393278dc282
````

This is hash digest of the control-plane state for the network `ov2` from all the cluster nodes. If the values have a mismatch `docker network inspect --verbose` on the individual nodes can help in identifying what the specific difference is.
Package mflag (aka multiple-flag) implements command-line flag parsing.  
It's an **hacky** fork of the [official golang package](http://golang.org/pkg/flag/)

It adds:

* both short and long flag version  
`./example -s red` `./example --string blue`

* multiple names for the same option  
```
$>./example -h
Usage of example:
  -s, --string="": a simple string
```

___
It is very flexible on purpose, so you can do things like:  
```
$>./example -h
Usage of example:
  -s, -string, --string="": a simple string
```

Or:  
```
$>./example -h
Usage of example:
  -oldflag, --newflag="": a simple string
```

You can also hide some flags from the usage, so if we want only `--newflag`:  
```
$>./example -h
Usage of example:
  --newflag="": a simple string
$>./example -oldflag str
str
```

See [example.go](example/example.go) for more details.
Usage: docker run -v /var/run:/var/run  --network host --privileged dockereng/network-diagnostic:support.sh
