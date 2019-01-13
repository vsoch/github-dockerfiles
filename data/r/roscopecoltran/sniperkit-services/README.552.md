[Advanced Nagios Plugins Collection](https://github.com/HariSekhon/nagios-plugins)
==================================
[![Build Status](https://travis-ci.org/HariSekhon/nagios-plugins.svg?branch=master)](https://travis-ci.org/HariSekhon/nagios-plugins) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/e6fcf7cb4dcc4905ab0a4cb91567fdda)](https://www.codacy.com/app/harisekhon/nagios-plugins) [![GitHub stars](https://img.shields.io/github/stars/harisekhon/nagios-plugins.svg)](https://github.com/harisekhon/nagios-plugins/stargazers) [![GitHub forks](https://img.shields.io/github/forks/harisekhon/nagios-plugins.svg)](https://github.com/harisekhon/nagios-plugins/network) [![Dependency Status](https://gemnasium.com/badges/github.com/HariSekhon/nagios-plugins.svg)](https://gemnasium.com/github.com/HariSekhon/nagios-plugins) [![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20OS%20X-blue.svg)](https://github.com/harisekhon/nagios-plugins#advanced-nagios-plugins-collection) [![DockerHub](https://img.shields.io/badge/docker-available-blue.svg)](https://hub.docker.com/r/harisekhon/nagios-plugins/) [![](https://images.microbadger.com/badges/image/harisekhon/nagios-plugins.svg)](http://microbadger.com/#/images/harisekhon/nagios-plugins)

Docker image containing the [Advanced Nagios Plugins Collection](https://github.com/HariSekhon/nagios-plugins) - the largest, most advanced collection of production-grade Nagios monitoring code (over 350 programs).

<!-- the DockerHub page for harisekhon/nagios-plugins will show the README of the latest build so make all of them generic enough -->
This docker image contains all dependencies pre-built on Alpine, CentOS, Debian and Ubuntu latest docker base images and are tagged as `:latest`, `:centos`, `:debian` and `:ubuntu` respectively. The source for each OS build is available in adjacent directories in the [Dockerfiles GitHub repo](https://github.com/HariSekhon/Dockerfiles/).

Specialised plugins for Hadoop, Big Data & NoSQL technologies, written by a former Clouderan ([Cloudera](http://www.cloudera.com) was the first Hadoop Big Data vendor) and current [Hortonworks](http://www.hortonworks.com) consultant.

Hadoop and extensive API integration with all major Hadoop vendors ([Hortonworks](http://www.hortonworks.com), [Cloudera](http://www.cloudera.com), [MapR](http://www.mapr.com), [IBM BigInsights](http://www-03.ibm.com/software/products/en/ibm-biginsights-for-apache-hadoop)), as well as most major open source NoSQL technologies, Pub-Sub / Message Buses, CI, Web and Linux based infrastructure.

Most enterprise monitoring systems come with basic generic checks, while this project extends their monitoring capabilities significantly further in to advanced infrastructure, application layer, APIs etc.

For more documentation on the Nagios Plugins contained in this image, see the [GitHub project page](https://github.com/HariSekhon/nagios-plugins#usage---help)

List all plugins:

```
docker run harisekhon/nagios-plugins
```

Run any given plugin by suffixing it to the docker run command:

```
docker run harisekhon/nagios-plugins <program> <args>
```

eg.

```
docker run harisekhon/nagios-plugins check_ssl_cert.pl --help
```

Supports a a wide variety of [compatible Enterprise Monitoring servers](https://github.com/harisekhon/nagios-plugins#enterprise-monitoring-systems).

The project is a treasure trove of essentials for every single "DevOp" / sysadmin / engineer, with extensive goodies for people running:

* Web Infrastructure
* [Hadoop](http://hadoop.apache.org/)
* [Kafka](http://kafka.apache.org/)
* [RabbitMQ](http://www.rabbitmq.com/)
* [Mesos](http://mesos.apache.org/)
* [Consul](https://www.consul.io/)

NoSQL technologies:

* [Cassandra](http://cassandra.apache.org/)
* [HBase](https://hbase.apache.org/)
* [MongoDB](https://www.mongodb.com/)
* [Memcached](https://memcached.org/)
* [Couchbase](http://www.couchbase.com/)
* [Redis](http://redis.io/)
* [Riak](http://basho.com/products/)
* [Solr / SolrCloud](http://lucene.apache.org/solr/)
* [Elasticsearch](https://www.elastic.co/products/elasticsearch)

Linux & Infrastructure technologies:

* [Jenkins](https://jenkins.io/)
* [Travis CI](https://travis-ci.org/)
* SSL Certificate expiry
* advanced DNS record checks
* Whois domain expiry check
* [MySQL](https://www.mysql.com/)

and many more ...

Related Docker images can be found for many Open Source, Big Data and NoSQL technologies on [my DockerHub profile](https://hub.docker.com/r/harisekhon). The source for them all can be found in the [master Dockerfiles GitHub repo](https://github.com/HariSekhon/Dockerfiles/).
