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
Consul API client
=================

This package provides the `api` package which attempts to
provide programmatic access to the full Consul API.

Currently, all of the Consul APIs included in version 0.6.0 are supported.

Documentation
=============

The full documentation is available on [Godoc](https://godoc.org/github.com/hashicorp/consul/api)

Usage
=====

Below is an example of using the Consul client:

```go
// Get a new client
client, err := api.NewClient(api.DefaultConfig())
if err != nil {
    panic(err)
}

// Get a handle to the KV API
kv := client.KV()

// PUT a new KV pair
p := &api.KVPair{Key: "foo", Value: []byte("test")}
_, err = kv.Put(p, nil)
if err != nil {
    panic(err)
}

// Lookup the pair
pair, _, err := kv.Get("foo", nil)
if err != nil {
    panic(err)
}
fmt.Printf("KV: %v", pair)

```
# RabbitMQ Scraping

This is an example on how to setup RabbitMQ so Prometheus can scrape data from it.
It uses a third party [RabbitMQ exporter](https://github.com/kbudde/rabbitmq_exporter).

Since the [RabbitMQ exporter](https://github.com/kbudde/rabbitmq_exporter) needs to
scrape the RabbitMQ management API to scrape data, and it defaults to localhost, it is
easier to simply embed the **kbudde/rabbitmq-exporter** on the same pod as RabbitMQ,
this way they share the same network.

With this pod running you will have the exporter scraping data, but Prometheus has not
yet found the exporter and is not scraping data from it.

For more details on how to use Kubernetes service discovery take a look at the 
[documentation](http://prometheus.io/docs/operating/configuration/#kubernetes-sd-configurations-kubernetes_sd_config)
and at the [available examples](./documentation/examples).

After you got Kubernetes service discovery up and running you just need to advertise that RabbitMQ
is exposing metrics. To do that you need to define a service that:

* Exposes the exporter port
* Has a **prometheus.io/scrape: "true"** annotation
* Has a **prometheus.io/port: "9090"** annotation

And you should be able to see your RabbitMQ exporter being scraped on the Prometheus status page.
Since the IP that will be scraped will be the pod endpoint it is important that the node
where Prometheus is running has access to the Kubernetes overlay network
(flannel, Weave, AWS, or any of the other options that Kubernetes gives to you).
## Remote Write Adapter Example

This is a simple example of how to write a server to
receive samples from the remote storage output.

To use it:

```
go build
./example_write_adapter
```

...and then add the following to your `prometheus.yml`:

```yaml
remote_write:
  url: "http://localhost:1234/receive"
```

Then start Prometheus:

```
./prometheus
```
# Remote storage adapter

This is a write adapter that receives samples via Prometheus's remote write
protocol and stores them in Graphite, InfluxDB, or OpenTSDB. It is meant as a
replacement for the built-in specific remote storage implementations that have
been removed from Prometheus.

For InfluxDB, this binary is also a read adapter that supports reading back
data through Prometheus via Prometheus's remote read protocol.

## Building

```
go build
```

## Running

Graphite example:

```
./remote_storage_adapter -graphite-address=localhost:8080
```

OpenTSDB example:

```
./remote_storage_adapter -opentsdb-url=http://localhost:8081/
```

InfluxDB example:

```
./remote_storage_adapter -influxdb-url=http://localhost:8086/ -influxdb.database=prometheus -influxdb.retention-policy=autogen
```

To show all flags:

```
./remote_storage_adapter -h
```

## Configuring Prometheus

To configure Prometheus to send samples to this binary, add the following to your `prometheus.yml`:

```yaml
# Remote write configuration (for Graphite, OpenTSDB, or InfluxDB).
remote_write:
  - url: "http://localhost:9201/write"

# Remote read configuration (for InfluxDB only at the moment).
remote_read:
  - url: "http://localhost:9201/read"
```
The `ui` package contains static files and templates used in the web UI. For
easier distribution they are statically compiled into the Prometheus binary
using the go-bindata tool (c.f. Makefile).

During development it is more convenient to always use the files on disk to
directly see changes without recompiling.
Set the environment variable `DEBUG=1` and compile Prometheus for this to work.
This is for development purposes only.

After making changes to any file, run `make assets` before committing to update
the generated inline version of the file.
### Service Discovery

This directory contains the service discovery (SD) component of Prometheus.



## Design of a Prometheus SD

There are many requests to add new SDs to Prometheus, this section looks at
what makes a good SD and covers some of the common implementation issues.

### Does this make sense as an SD?

The first question to be asked is does it make sense to add this particular
SD? An SD mechanism should be reasonably well established, and at a minimum in
use across multiple organisations. It should allow discovering of machines
and/or services running somewhere. When exactly an SD is popular enough to
justify being added to Prometheus natively is an open question.

It should not be a brand new SD mechanism, or a variant of an established
mechanism. We want to integrate Prometheus with the SD that's already there in
your infrastructure, not invent yet more ways to do service discovery. We also
do not add mechanisms to work around users lacking service discovery and/or
configuration management infrastructure.

SDs that merely discover other applications running the same software (e.g.
talk to one Kafka or Cassandra server to find the others) are not service
discovery. In that case the SD you should be looking at is whatever decides
that a machine is going to be a Kafka server, likely a machine database or
configuration management system.

If something is particularly custom or unusual, `file_sd` is the generic
mechanism provided for users to hook in. Generally with Prometheus we offer a
single generic mechanism for things with infinite variations, rather than
trying to support everything natively (see also, alertmanager webhook, remote
read, remote write, node exporter textfile collector). For example anything
that would involve talking to a relational database should use `file_sd`
instead.

For configuration management systems like Chef, while they do have a
database/API that'd in principle make sense to talk to for service discovery,
the idiomatic approach is to use Chef's templating facilities to write out a
file for use with `file_sd`.


### Mapping from SD to Prometheus

The general principle with SD is to extract all the potentially useful
information we can out of the SD, and let the user choose what they need of it
using
[relabelling](https://prometheus.io/docs/operating/configuration/#<relabel_config>).
This information is generally termed metadata.

Metadata is exposed as a set of key/value pairs (labels) per target. The keys
are prefixed with `__meta_<sdname>_<key>`, and there should also be an `__address__`
label with the host:port of the target (preferably an IP address to avoid DNS
lookups). No other labelnames should be exposed.

It is very common for initial pull requests for new SDs to include hardcoded
assumptions that make sense for the the author's setup. SD should be generic,
any customisation should be handled via relabelling. There should be basically
no business logic, filtering, or transformations of the data from the SD beyond
that which is needed to fit it into the metadata data model. 

Arrays (e.g. a list of tags) should be converted to a single label with the
array values joined with a comma. Also prefix and suffix the value with a
comma. So for example the array `[a, b, c]` would become `,a,b,c,`. As
relabelling regexes are fully anchored, this makes it easier to write correct
regexes against (`.*,a,.*` works no matter where `a` appears in the list). The
canonical example of this is `__meta_consul_tags`.

Maps, hashes and other forms of key/value pairs should be all prefixed and
exposed as labels. For example for EC2 tags, there would be
`__meta_ec2_tag_Description=mydescription` for the Description tag. Labelnames
may only contain `[_a-zA-Z0-9]`, sanitize by replacing with underscores as needed.

For targets with multiple potential ports, you can a) expose them as a list, b)
if they're named expose them as a map or c) expose them each as their own
target. Kubernetes SD takes the target per port approach. a) and b) can be
combined.

For machine-like SDs (OpenStack, EC2, Kubernetes to some extent) there may
be multiple network interfaces for a target. Thus far reporting the details
of only the first/primary network interface has sufficed.


### Other implementation considerations

SDs are intended to dump all possible targets. For example the optional use of
EC2 service discovery would be to take the entire region's worth of EC2
instances it provides and do everything needed in one `scrape_config`. For
large deployments where you are only interested in a small proportion of the
returned targets, this may cause performance issues. If this occurs it is
acceptable to also offer filtering via whatever mechanisms the SD exposes. For
EC2 that would be the `Filter` option on `DescribeInstances`. Keep in mind that
this is a performance optimisation, it should be possible to do the same
filtering using relabelling alone. As with SD generally, we do not invent new
ways to filter targets (that is what relabelling is for), merely offer up
whatever functionality the SD itself offers.

It is a general rule with Prometheus that all configuration comes from the
configuration file. While the libraries you use to talk to the SD may also
offer other mechanisms for providing configuration/authentication under the
covers (EC2's use of environment variables being a prime example), using your SD
mechanism should not require this. Put another way, your SD implementation
should not read environment variables or files to obtain configuration.

Some SD mechanisms have rate limits that make them challenging to use. As an
example we have unfortunately had to reject Amazon ECS service discovery due to
the rate limits being so low that it would not be usable for anything beyond
small setups.

If a system offers multiple distinct types of SD, select which is in use with a
configuration option rather than returning them all from one mega SD that
requires relabelling to select just the one you want. So far we have only seen
this with Kubernetes. When a single SD with a selector vs.  multiple distinct
SDs makes sense is an open question.

If there is a failure while processing talking to the SD, abort rather than
returning partial data. It is better to work from stale targets than partial
or incorrect metadata.

The information obtained from service discovery is not considered sensitive
security wise. Do not return secrets in metadata, anyone with access to
the Prometheus server will be able to see them.


## Writing an SD mechanism

### The SD interface

A Service Discovery (SD) mechanism has to discover targets and provide them to Prometheus. We expect similar targets to be grouped together, in the form of a [`TargetGroup`](https://godoc.org/github.com/prometheus/prometheus/config#TargetGroup). The SD mechanism sends the targets down to prometheus as list of `TargetGroups`.

An SD mechanism has to implement the `TargetProvider` Interface:
```go
type TargetProvider interface {
	Run(ctx context.Context, up chan<- []*config.TargetGroup)
}
```

Prometheus will call the `Run()` method on a provider to initialise the discovery mechanism. The mechanism will then send *all* the `TargetGroup`s into the channel. Now the mechanism will watch for changes and then send only changed and new `TargetGroup`s down the channel.

For example if we had a discovery mechanism and it retrieves the following groups:

```
[]config.TargetGroup{
  {
    Targets: []model.LabelSet{
       {
          "__instance__": "10.11.150.1:7870",
          "hostname": "demo-target-1",
          "test": "simple-test",
       },
       {
          "__instance__": "10.11.150.4:7870",
          "hostname": "demo-target-2",
          "test": "simple-test",
       },
    },
    Labels: map[LabelName][LabelValue] {
      "job": "mysql",
    },
    "Source": "file1", 
  },
  {
    Targets: []model.LabelSet{
       {
          "__instance__": "10.11.122.11:6001",
          "hostname": "demo-postgres-1",
          "test": "simple-test",
       },
       {
          "__instance__": "10.11.122.15:6001",
          "hostname": "demo-postgres-2",
          "test": "simple-test",
       },
    },
    Labels: map[LabelName][LabelValue] {
      "job": "postgres",
    },
    "Source": "file2", 
  },
}
```

Here there are two `TargetGroups` one group with source `file1` and another with `file2`. The grouping is implementation specific and could even be one target per group. But, one has to make sure every target group sent by an SD instance should have a `Source` which is unique across all the `TargetGroup`s of that SD instance. 

In this case, both the `TargetGroup`s are sent down the channel the first time `Run()` is called. Now, for an update, we need to send the whole _changed_ `TargetGroup` down the channel. i.e, if the target with `hostname: demo-postgres-2` goes away, we send:
```
&config.TargetGroup{
  Targets: []model.LabelSet{
     {
        "__instance__": "10.11.122.11:6001",
        "hostname": "demo-postgres-1",
        "test": "simple-test",
     },
  },
  Labels: map[LabelName][LabelValue] {
    "job": "postgres",
  },
  "Source": "file2", 
}
```
down the channel.

If all the targets in a group go away, we need to send the target groups with empty `Targets` down the channel. i.e, if all targets with `job: postgres` go away, we send:
```
&config.TargetGroup{
  Targets: nil,
  "Source": "file2", 
}
```
down the channel.

<!-- TODO: Add best-practices -->
Place here console templates for Prometheus.

In /usr/share/doc/prometheus/examples/ are sample templates that show what can
be done with Prometheus' templating language. They only cover some generic
cases, and you are encouraged to modify and expand them.

See http://prometheus.io/docs/visualization/consoles/ for more information.
