# TiDB Operator

[![Build Status](https://internal.pingcap.net/jenkins/job/build_tidb_operator_master/badge/icon)](https://internal.pingcap.net/jenkins/job/build_tidb_operator_master)

TiDB Operator manages [TiDB](https://github.com/pingcap/tidb) clusters on [Kubernetes](https://kubernetes.io) and automates tasks related to operating a TiDB cluster. It makes TiDB a truly cloud-native database.

> **Warning:** Currently, TiDB Operator is work in progress [WIP] and is NOT ready for production. Use at your own risk.

## Features

- __Safely scaling the TiDB cluster__

    TiDB Operator empowers TiDB with horizontal scalability on the cloud.

- __Rolling update of the TiDB cluster__

    Gracefully perform rolling updates for the TiDB cluster in order, achieving zero-downtime of the TiDB cluster.

- __Multi-tenant support__

    Users can deploy and manage multiple TiDB clusters on a single Kubernetes cluster easily.

- __Automatic failover__ (WIP)

    TiDB Operator automatically performs failover for your TiDB cluster when node failures occur.

- __Kubernetes package manager support__

    By embracing Kubernetes package manager [Helm](https://helm.sh), users can easily deploy TiDB clusters with only one command.

- __Automatically monitoring TiDB cluster at creating__

    Automatically deploy Prometheus, Grafana for TiDB cluster monitoring.

## Roadmap

Read the [Roadmap](./ROADMAP.md).

## Quick start

Read the [Deploy TiDB using Kubernetes on Your Laptop for development and testing](./docs/local-dind-tutorial.md), or follow a [tutorial](./docs/google-kubernetes-tutorial.md) to launch in Google Kubernetes Engine:

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/pingcap/tidb-operator&tutorial=docs/google-kubernetes-tutorial.md)

## Contributing

Contributions are welcome and greatly appreciated. See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for details on submitting patches and the contribution workflow.

## License

TiDB is under the Apache 2.0 license. See the [LICENSE](./LICENSE) file for details.
# TiDB docker-compose

[![Build Status](https://travis-ci.org/pingcap/tidb-docker-compose.svg?branch=master)](https://travis-ci.org/pingcap/tidb-docker-compose)

## Requirements

* Docker >= 17.03
* Docker Compose >= 1.6.0

> **Note:** [Legacy Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_mac/) users must migrate to [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac), since it is tested that tidb-docker-compose cannot be started on Docker Toolbox and Docker Machine.

## Quick start

```bash
$ git clone https://github.com/pingcap/tidb-docker-compose.git
$ cd tidb-docker-compose && docker-compose pull # Get the latest Docker images
$ docker-compose up -d
$ mysql -h 127.0.0.1 -P 4000 -u root
```

* Access monitor at http://localhost:3000

Default user/password: admin/admin

* Access [tidb-vision](https://github.com/pingcap/tidb-vision) at http://localhost:8010

* Access Spark Web UI at http://localhost:8080
  and access [TiSpark](https://github.com/pingcap/tispark) through spark://127.0.0.1:7077

## Customize TiDB Cluster

### Configuration

* config/pd.toml is copied from [PD repo](https://github.com/pingcap/pd/tree/master/conf)
* config/tikv.toml is copied from [TiKV repo](https://github.com/pingcap/tikv/tree/master/etc)
* config/tidb.toml is copied from [TiDB repo](https://github.com/pingcap/tidb/tree/master/config)

If you find these configuration files outdated or mismatch with TiDB version, you can copy these files from their upstream repos and change their metrics addr with `pushgateway:9091`. Also `max-open-files` are configured to `1024` in tikv.toml to simplify quick start on Linux, because setting up ulimit on Linux with docker is quite tedious.

And config/*-dashboard.json are copied from [TiDB-Ansible repo](https://github.com/pingcap/tidb-ansible/tree/master/scripts)

You can customize TiDB cluster configuration by editing docker-compose.yml and the above config files if you know what you're doing.

But edit these files manually is tedious and error-prone, a template engine is strongly recommended. See the following steps

### Install Helm

[Helm](https://helm.sh) is used as a template render engine

```
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
```

Or if you use Mac, you can use homebrew to install Helm by `brew install kubernetes-helm`

### Bring up TiDB cluster

```bash
$ git clone https://github.com/pingcap/tidb-docker-compose.git
$ cd tidb-docker-compose
$ vi compose/values.yaml # custom cluster size, docker image, port mapping etc
$ helm template compose > generated-docker-compose.yaml
$ docker-compose -f generated-docker-compose.yaml pull # Get the latest Docker images
$ docker-compose -f generated-docker-compose.yaml up -d
```

You can build docker image yourself for development test.

* Build from binary

  For pd, tikv and tidb, comment their `image` and `buildPath` fields out. And then copy their binary files to pd/bin/pd-server, tikv/bin/tikv-server and tidb/bin/tidb-server.

  These binary files can be built locally or downloaded from https://download.pingcap.org/tidb-latest-linux-amd64.tar.gz

  For tidbVision, comment its `image` and `buildPath` fields out. And then copy tidb-vision repo to tidb-vision/tidb-vision.

* Build from source

  Leave pd, tikv, tidb and tidbVision `image` field empty and set their `buildPath` field to their source directory.

  For example, if your local tikv source directory is $GOPATH/src/github.com/pingcap/tikv, just set tikv `buildPath` to `$GOPATH/src/github.com/pingcap/tikv`

  *Note:* Compiling tikv from source consumes lots of memory, memory of Docker for Mac needs to be adjusted to greater than 6GB

[tidb-vision](https://github.com/pingcap/tidb-vision) is a visiualization page of TiDB Cluster, it's WIP project and can be disabled by commenting `tidbVision` out.

[TiSpark](https://github.com/pingcap/tispark) is a thin layer built for running Apache Spark on top of TiDB/TiKV to answer the complex OLAP queries.

#### Host network mode (Linux)

*Note:* Docker for Mac uses a Linux virtual machine, host network mode will not expose any services to host machine. So it's useless to use this mode.

When using TiKV directly without TiDB, host network mode must be enabled. This way all services use host network without isolation. So you can access all services on the host machine.

You can enable this mode by setting `networkMode: host` in compose/values.yaml and regenerate docker-compose.yml. When in this mode, prometheus address in configuration files should be changed from `prometheus:9090` to `127.0.0.1:9090`, and pushgateway address should be changed from `pushgateway:9091` to `127.0.0.1:9091`.

These modification can be done by:
```bash
# Note: this only needed when networkMode is `host`
sed -i 's/pushgateway:9091/127.0.0.1:9091/g' config/*
sed -i 's/prometheus:9090/127.0.0.1:9090/g' config/*
```

After all the above is done, you can start tidb-cluster as usual by `docker-compose -f generated-docker-compose.yml up -d`

### Debug TiDB/TiKV/PD instances
Prerequisites:

Pprof: This is a tool for visualization and analysis of profiling data. Follow [these instructions](https://github.com/google/pprof#building-pprof) to install pprof.

Graphviz: [http://www.graphviz.org/](http://www.graphviz.org/), used to generate graphic visualizations of profiles.

* debug TiDB or PD instances

```bash
### Use the following command to starts a web server for graphic visualizations of golang program profiles
$ ./tool/container_debug -s pd0 -p /pd-server -w
```
The above command will produce graphic visualizations of profiles of `pd0` that can be accessed through the browser.

* debug TiKV instances

```bash
### step 1: select a tikv instance(here is tikv0) and specify the binary path in container to enter debug container
$ ./tool/container_debug -s tikv0 -p /tikv-server

### after step 1, we can generate flame graph for tikv0 in debug container
$ ./run_flamegraph.sh 1  # 1 is the tikv0's process id

### also can fetch tikv0's stack informations with GDB in debug container
$ gdb /tikv-server 1 -batch -ex "thread apply all bt" -ex "info threads"
```

### Access TiDB cluster

TiDB uses ports: 4000(mysql) and 10080(status) by default

```bash
$ mysql -h 127.0.0.1 -P 4000 -u root
```

And Grafana uses port 3000 by default, so open your browser at http://localhost:3000 to view monitor dashboard

If you enabled tidb-vision, you can view it at http://localhost:8010

### Access Spark shell and load TiSpark

Insert some sample data to the TiDB cluster:

```bash
$ docker-compose exec tispark-master bash
$ cd /opt/spark/data/tispark-sample-data
$ mysql -h tidb -P 4000 -u root < dss.ddl
```

After the sample data is loaded into the TiDB cluster, you can access Spark Shell by `docker-compose exec tispark-master /opt/spark/bin/spark-shell`.

```bash
$ docker-compose exec tispark-master /opt/spark/bin/spark-shell
...
Spark context available as 'sc' (master = local[*], app id = local-1527045927617).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.1.1
      /_/

Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_172)
Type in expressions to have them evaluated.
Type :help for more information.

scala> import org.apache.spark.sql.TiContext
...
scala> val ti = new TiContext(spark)
...
scala> ti.tidbMapDatabase("TPCH_001")
...
scala> spark.sql("select count(*) from lineitem").show
+--------+
|count(1)|
+--------+
|   60175|
+--------+
```

You can also access Spark with Python or R using the following commands:

```
docker-compose exec tispark-master /opt/spark/bin/pyspark
docker-compose exec tispark-master /opt/spark/bin/sparkR
```

More documents about TiSpark can be found [here](https://github.com/pingcap/tispark).
## TiSparkR
TiSparkR is a thin layer built to support the R language with TiSpark.

### Usage
1. Download the TiSparkR source code and build a binary package (run `R CMD build R` in TiSpark root directory). Install it to your local R library (e.g. via `R CMD INSTALL TiSparkR_1.0.0.tar.gz`)

2. Build or download TiSpark dependency jar `tispark-core-1.0-RC1-jar-with-dependencies.jar` [here](https://github.com/pingcap/tispark).

3. `cd` to your Spark home directory, and run:
    ```
    ./bin/sparkR --jars /where-ever-it-is/tispark-core-${version}-jar-with-dependencies.jar
    ```
    Note that you should replace the `TiSpark` jar path with your own.

4. Use as below in your R console:
    ```R
    # import tisparkR library
    > library(TiSparkR)
    # create a TiContext instance
    > ti <- createTiContext(spark)
    # Map TiContext to database:tpch_test
    > tidbMapDatabase(ti, "tpch_test")

    # Run a sql query
    > customers <- sql("select * from customer")
    # Print schema
    > printSchema(customers)
    root
     |-- c_custkey: long (nullable = true)
     |-- c_name: string (nullable = true)
     |-- c_address: string (nullable = true)
     |-- c_nationkey: long (nullable = true)
     |-- c_phone: string (nullable = true)
     |-- c_acctbal: decimal(15,2) (nullable = true)
     |-- c_mktsegment: string (nullable = true)
     |-- c_comment: string (nullable = true)

    # Run a count query
    > count <- sql("select count(*) from customer")
    # Print count result
    > head(count)
      count(1)
    1      150
    ```
# TiDB dashboard installer

This image is used to configure Grafana datasource and dashboards for TiDB cluster. It is used in [tidb-docker-compose](https://github.com/pingcap/tidb-docker-compose) and [tidb-operator](https://github.com/pingcap/tidb-operator).

The JSON files in dashboards are copied from [tidb-ansible](https://github.com/pingcap/tidb-ansible/tree/master/scripts).

Grafana version prior to v5.0.0 can only use import API to automate datasource and dashboard configuration. So this image is needed to run in docker environment. It runs only once in this environment.

With Grafana v5.x, we can use [provisioning](http://docs.grafana.org/administration/provisioning) feature to statically provision datasources and dashboards. No need to use scripts to configure Grafana.

But currently, the dashboards in [tidb-ansible](https://github.com/pingcap/tidb-ansible/tree/master/scripts) repository are incompatible with Grafana v5.x and cannot be statically provisioned. So this image is still required.

In the future, we can use [grafonnet](https://github.com/grafana/grafonnet-lib) to migrate old dashboards and make dashboard updating reviewable.