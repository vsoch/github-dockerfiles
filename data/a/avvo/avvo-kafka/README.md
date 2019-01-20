# Avvo Kafka

This repo contains docker files that help us build Kafka and Zookeeper images that
mirror what we have in our production/test Cloudera clusters

These versions are built modified from Wurstmeister ([Kafka](https://github.com/wurstmeister/kafka-docker), [Zookeeper](https://github.com/wurstmeister/zookeeper-docker)). We have modified them to lock to the versions we need
because the tags on docker hub do not contain the versions we need.

## Current Versions

Kafka: 0.8.2.1
Zookeeper: 3.3.6 (3.3.5 is used in Cloudera but there is no current download available for it)

## Running

You can use the provided `docker-compose.yml` file to run zookeeper and kafka locally

# Rancher Kafka/Zookeeper

These images only work when used with rancher.

## Current Versions

Kafka: 0.10.2.0
Zookeeper: 3.4.9

## Environment Variables

Any environment variables that Kafka supports are usable.

These are the only mandatory variables:

Kafka:
* JMX_PORT: 9999 (port 9999 is the default for datadog monitoring)
* ZK_SERVICE: kafka/zk (format: stack/service)

Zookeeper:
* JMX_PORT: 9998 (port 9998 is the default but it's not in use)
* ZK_SERVICE: kafka/zk (format: stack/service)

