[![Go Report Card](https://goreportcard.com/badge/github.com/mesos/mr-redis)](https://goreportcard.com/report/github.com/mesos/mr-redis)
[![GoDoc](https://godoc.org/github.com/mesos/mr-redis?status.svg)](https://godoc.org/github.com/mesos/mr-redis)
[![Build Status](https://travis-ci.org/mesos/mr-redis.svg?branch=master)](https://travis-ci.org/mesos/mr-redis)
# mr-redis  

Mesos runs Redis.

<img src="./logo.jpg" width="20%" height="20%"> 

A minimalistic framework for Redis workload on Apache Mesos

This framework supports the following features

 * Creates/Maintains Single Redis-instance
 * Creates/Maintains Redis-Instances with Master-Slave setup 
 * A centralized persistence layer currently enabled by etcd

## Why mr-redis?

At [Huawei] (http://www.huawei.com/en/) we foresee creating, running and maintaining huge number of redis instances on our datacenters.  We intially evaluated few cluster managers for this job, but due to the specific requirements of 'redis' itself those solutions did not satisfy most of our needs.  We quickly did a POC by writing a framework exclusively for Redis on Apache Mesos. Based on the outcome we decided to initate this project and work with the opensource community to build a robust custom framework for Redis which will be useful for Huawei as well as for the rest of the world.

##Project Status is Alpha.
 We have built a basic working functionality and would like to build a strong functional framework for Redis along with the community.  In the meanwhile please feel free to try this out and give us feedback by creating PR and Issues. 

## Who should use mr-redis 
* If your organization has a requirement for creating and maintaining huge number of redis service instances
* If you are planning to host 'redis' as a Service 
* If redis instances need to be created in seconds and not in minutes
* If you are already using Apache Mesos as a Resource Manager for your datacenter and want to add Redis (as a service) workload to it

## Installation Instructions

### Prerequisite
For Mr-Redis to work you will need below software packages already available in your datacenter (Cloud)
* [Apache Mesos](http://mesos.apache.org/gettingstarted/) :- The Resource Manager of your DC to which mr-redis scheduler will connect to.
* [Golang Dev Environment] (https://golang.org/doc/install) :- If you are planning to build mr-redis from source you will need to setup standard golang development environment. 
* [etcd](https://github.com/coreos/etcd#getting-started) or [ZooKeeper](http://zookeeper.apache.org/doc/trunk/zookeeperStarted.html) :- mr-redis uses etcd/ZK to store its state information so a running instance of either etcd or ZK is required in your datacenter
* [redis-server](https://hub.docker.com/r/library/redis) :- mr-redis scheduler is capable of pulling the redis docker image and executing it. (new) You no longer need to supply a Redis binary

Installing the scheduler/framework can be done in three ways

### From source code (Developer)
```
$git clone https://github.com/mesos/mr-redis.git ${GOPATH}/src/github.com/mesos/mr-redis
$go get github.com/tools/godep
$cd ${GOPATH}/src/github.com/mesos/mr-redis/sched
$godep go build .
$cd ../exec/
$godep go build -o MrRedisExecutor .
$cd ../cli/
$godep go build -o mrr .
```
### From RELEASE (Alpha V1)
```
$mkdir mr-redis
$cd mr-redis
$wget https://github.com/mesos/mr-redis/releases/download/v0.01-alpha/sched
$wget https://github.com/mesos/mr-redis/releases/download/v0.01-alpha/MrRedisExecutor
```
Linux CLI
```
$wget https://github.com/mesos/mr-redis/releases/download/v0.01-alpha/mrr_linux_amd64
```
Windows CLI
```
$wget https://github.com/mesos/mr-redis/releases/download/v0.01-alpha/mrr_win_amd64.exe
```
Darwin (MAC) CLI
```
$wget https://github.com/mesos/mr-redis/releases/download/v0.01-alpha/mrr_darwin_amd64
```
Mark them as binaries 
```
$chmod u+x *
```
Create a link or alias for ease of use, for example in Linux perform below to create a link
```
$ln -s mrr_linux_amd64 mrr
```

### DC/OS
MrRedis is integrated with DC/OS's universe, it should be pretty straight forward to install it like any other package.
```
$dcos package install mr-redis
```
#### NOTE for DC/OS Users:
Unlike ETCD, Cassandra and other database frameworks installing mr-redis (scheduler) itself will not create any redis instance in your DC/OS environment, you have to further download and use the CLI (mrr) in order to create redis instances.  

#### Reaching the framework
The scheduler binds itself with the port 5656, so from a node within the cluster or from a node from which mrredis.mesos is resolvable try to create an instance with the below configuration. {InstanceName : "TestInstance"; MemoryCapacity : 100 MB; Number of Slaves : 2;}
```
$curl -X "POST" mrredis.mesos:5656/v1/CREATE/TestInstance/100/1/2
Request Accepted, Instance will be created.
```

#### Status of created Instance
Try the below curl command.  This gives a json response about this instance.
```
$curl mrredis.mesos:5656/v1/STATUS/TestInstance
{"Name":"TestInstance","Type":"MS","Status":"RUNNING","Capacity":200,"Master":{"IP":"10.11.12.123","Port":"6382","MemoryCapacity":200,"MemoryUsed":1904432,"Uptime":1623,"ClientsConnected":1,"LastSyncedToMaster":0},"Slaves":[{"IP":"10.11.12.121","Port":"6381","MemoryCapacity":200,"MemoryUsed":834904,"Uptime":1619,"ClientsConnected":2,"LastSyncedToMaster":9},{"IP":"10.11.12.121","Port":"6382","MemoryCapacity":200,"MemoryUsed":834904,"Uptime":1619,"ClientsConnected":2,"LastSyncedToMaster":9}]}
```
OR try the CLI
```
$mrr status -n TestInstance
Status = RUNNING
Type = MS
Capacity = 200
Master = 10.11.12.123:6382
        Slave0 = 10.11.12.121:6381
        Slave1 = 10.11.12.121:6382
```

#### Connecting to an Instance
From the above json response information related to Master are as follows.
```
	"Master": {
		"IP": "10.11.12.123",
		"Port": "6382",
		"MemoryCapacity": 200,
		"MemoryUsed": 1904432,
		"Uptime": 1623,
		"ClientsConnected": 1,
		"LastSyncedToMaster": 0
	}
```
You could use any redis [client] (http://redis.io/clients) and connect to the master or use the redis-cli to test the instance.
```
$redis-cli -h 10.11.12.123 -p 6382
10.11.12.123:6381> set foo bar
OK
10.11.12.123:6381> get foo
"bar"
10.11.12.123:6381> exit
```

## Starting the Scheduler (not applicable to DC/OS users)
MrRedis scheduler binary is usually referred as `sched`, the scheduler hosts a file-server which can distribute redis binary and custom Executor.

The scheduler takes only one argument which is the config file,

```
$./sched -config="./config.json"
2016/01/17 16:35:11 *****************************************************************
2016/01/17 16:35:11 *********************Starting MrRedis-Scheduler******************
2016/01/17 16:35:11 *****************************************************************
2016/01/17 16:35:11 Starting the HTTP server at port 8080
.
.
```
The configuration file should be of json format, below is an example
```
$cat config.json
{
   "UserName": "ubuntu",
   "FrameworkName": "MrRedis",
   "Master": "127.0.0.1:5050",
   "ExecutorPath": "./MrRedisExecutor",
   "RedisImage": "redis:3.0-alpine",
```
you can configure Zookeeper as the KV store 
```
   "DBType": "zookeeper",, 
   "DBEndPoint": "127.0.0.1:2181"", 
```
OR use ETCD
```
   "DBType": "etcd", 
   "DBEndPoint": "127.0.0.1:2379", 
```
```   
   "LogFile": "stderr",
   "ArtifactIP": "127.0.0.1",
   "ArtifactPort": "5454",
   "HTTPPort": "5656"
}
```
Please substitute appropriate values with respect to your environment  for MasterIP/Port, ExecutorPath, DBEndPoint and IP address of this scheduler's VM that is accessible from the slaves for artifactIP

if you want to get an empty config for you to start working on you could do this and the scheduler will print you a dummy structure for you to start working on.
```
$./sched -DumpEmptyConfig
{
   "UserName": "ubuntu",
   "FrameworkName": "MrRedis",
   "Master": "127.0.0.1:5050",
   "ExecutorPath": "./MrRedisExecutor",
   "RedisImage": "redis:3.0-alpine",
   "DBType": "etcd",
   "DBEndPoint": "127.0.0.1:2379",
   "LogFile": "stderr",
   "ArtifactIP": "127.0.0.1",
   "ArtifactPort": "5454",
   "HTTPPort": "5656"
}
```

### Distribution of redis processes among Mesos Agents.
'Distribution' : An integer representing number of 'redis-servers' can be start in One agent belonging to this Instance
This attribute needs to be supplied while you create an Instances, by default the distribution Value is set to 1.
#### Scenario 
Mesos cluster with three Agents A1, A2 and A3 then
#### Case 1:
If you create an instance with M and 2 Slaves namely S1 & S2 (default Distribution Value)

| A1 | A2 | A3 |
| --- | --- | --- |
| M | S1 | S1 |

roughly should be the distribution,
#### Case 2:
If you create an Redis Instance with M and 5 Slaves namely S1,S2,S3,S4,S5 (distribution Value is 2)

| A1 | A2 | A3 |
| --- | --- | --- |
| M | S1 | S1 |
| S3 | S4 | S5 |

The json file to be supplied along with 'CREATE' call should be like below
```
cat d.json
{
        "Distribution": 2
}
```
The cli(mrr) create sub-command has a new `-f` option to supply addition json file. If you are using curl to create instances then supply it like this
```
curl http://<ENDPOINT>/v1/CREATE/testInstance/100/1/2 -X "POST" --header "Content-Type: application/json" -d @d.json
```
### Creating Instances
This can be done in 3 ways.
<img src="./CreateInstance.gif" width="100%" height="100%"> 

### Creating Multiple Redis Instances:
How much time does it take to create 70 single redis instances ?
<img src="./MultiInstanceCreation.gif" width="100%" height="100%"> 

### Master-Slave Promotion:
Scheduler automatically promotes a slave when a master fails.
<img src="./MasterSlavePromotion.gif" width="100%" height="100%"> 

## Using the CLI
mr-redis has built-in cli for creating and destroying redis instances.

CLI should first be initialized with the scheduler with this simple command

```
$mrr init http://<schedulerIP>:<schedulerPORT>
```
If you want to explore other commands below is the help screen
```
$mrr help
NAME:
   mrr - MrRedis Command Line Interface

USAGE:
   mrr [global options] command [command options] [arguments...]

VERSION:
   0.0.0

COMMANDS:
   init, i      $mrr init <http://MrRedisEndPoint>
   create, c    Create a Redis Instance
   status, s    Status of a Redis Instance
   delete, d    Delete a Redis Instance
   help, h      Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --help, -h   show help
```

Help on a specific command
```
$mrr help create
NAME:
   mrr create - Create a Redis Instance

USAGE:
   mrr create [command options] [arguments...]

OPTIONS:
   --name, -n           Name of the Redis Instance
   --memory, -m "0"     Memory in MB
   --slaves, -s "0"     Number of Slaves
   --wait, -w           Wait for the Instance to be created (by default the command is async)
   --file, -f           Location of the config file for this instance, to specify Distribution Value
```

## More Examples of Using the CLI
### Example 1:
The cli itself will be async by default as it does not wait for the operation to complete

```
$mrr create -n testInst -m 200 -s 1
Attempting to Creating a Redis Instance (testInst) with mem=200 slaves=1
Instance Creation accepted..
Check $mrr status -n testInst for status
```

```
$mrr status -n testInst
Status = RUNNING
Type = MS
Capacity = 200
Master = 10.11.12.33:6389
        Slave0 = 10.11.12.32:6380
```

### Example 2:
If you have a complicated Redis requirement then a simple command like the one below will result in creating one redis instance with 1 master and 50 Slaves in less than 15 secs, Simple :-)
```
$time mrr create -n hello50 -m 100 -s 50 -w true
Attempting to Creating a Redis Instance (hello50) with mem=100 slaves=50
Instance Creation accepted................
Instance Created.

real    0m14.269s
user    0m0.033s
sys     0m0.037s
```
To find the status of the redis instance you have created, below is the command
```
$mrr status -n hello50
Status = RUNNING
Type = MS
Capacity = 100
Master = 10.11.12.21:6380
        Slave0 = 10.11.12.31:6381
        Slave1 = 10.11.12.31:6383
        Slave2 = 10.11.12.31:6384
        Slave3 = 10.11.12.31:6385
        Slave4 = 10.11.12.31:6382
        Slave5 = 10.11.12.31:6386
        Slave6 = 10.11.12.31:6387
        Slave7 = 10.11.12.31:6388
        Slave8 = 10.11.12.31:6391
        Slave9 = 10.11.12.31:6392
        Slave10 = 10.11.12.31:6390
        Slave11 = 10.11.12.31:6389
        Slave12 = 10.11.12.31:6393
        Slave13 = 10.11.12.31:6394
        Slave14 = 10.11.12.31:6395
        Slave15 = 10.11.12.20:6380
        Slave16 = 10.11.12.20:6381
        Slave17 = 10.11.12.20:6383
        Slave18 = 10.11.12.20:6384
        Slave19 = 10.11.12.20:6387
        Slave20 = 10.11.12.20:6385
        Slave21 = 10.11.12.20:6386
        Slave22 = 10.11.12.20:6382
        Slave23 = 10.11.12.29:6380
        Slave24 = 10.11.12.29:6381
        Slave25 = 10.11.12.29:6382
        Slave26 = 10.11.12.29:6384
        Slave27 = 10.11.12.29:6385
        Slave28 = 10.11.12.29:6383
        Slave29 = 10.11.12.29:6387
        Slave30 = 10.11.12.29:6386
        Slave31 = 10.11.12.29:6389
        Slave32 = 10.11.12.29:6391
        Slave33 = 10.11.12.29:6392
        Slave34 = 10.11.12.29:6388
        Slave35 = 10.11.12.29:6390
        Slave36 = 10.11.12.29:6394
        Slave37 = 10.11.12.29:6395
        Slave38 = 10.11.12.29:6393
        Slave39 = 10.11.12.21:6383
        Slave40 = 10.11.12.21:6384
        Slave41 = 10.11.12.21:6386
        Slave42 = 10.11.12.21:6385
        Slave43 = 10.11.12.21:6387
        Slave44 = 10.11.12.21:6388
        Slave45 = 10.11.12.21:6390
        Slave46 = 10.11.12.21:6389
        Slave47 = 10.11.12.21:6391
        Slave48 = 10.11.12.21:6381
        Slave49 = 10.11.12.21:6382
```

### Proxy in Progress 
We are writing a proxy that will be installed with every redis instances especially with Master-Slave setup.  The proxy should be a simple pass-through.  Should be capable of accepting new configuration changes without needing to restart it.  Below is some performance stats comparing different available proxies and ours.

```
$redis-benchmark -h <IP> -p <PORT>  -q -r 100000
```


<img src="./ProxyCompare.PNG" width="100%" height="100%"> 


### Contribution Guidelines
Go already provides a nice documentation on coding conventions and guidelines; just try to adhere to that [Effective Go](https://golang.org/doc/effective_go.html) :-) 

##Specifically 
- Format code using go fmt, if an already prebuilt auto formatter is not their in your editor
- We suggest using extensive comments, as this code base is still evolving
- Try to stress on error handling as per [Effective error handling in Go](https://golang.org/doc/effective_go.html#errors) (which we ourselves have probably missed at places)
- Please use this framework; We are looking forward for issues, and nothing greater than an issue and a fix. Nonetheless, if interested in contributing something specific, please raise an issue outright to let us know that you are doing "this"
- We have not set up tests and test code yet, this is one obvious area to contribute without saying.

### Future Plans

- [ ] Support REDIS 3.0 Cluster 
- [ ] Support a Proxy mechanism to expose Redis Instance Endpoint
- [ ] Build a UI for Create/Maintain/Monitor the entire redis framework
- [ ] Benchmark Utility for testing the RedisFramework 

##License
Copyright 2015 Huawei Technologies Co. Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this project except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
