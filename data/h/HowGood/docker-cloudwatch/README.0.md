# howgood/docker-cloudwatch

This is a lightweight docker container that runs the [Cloudwatch Logs](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html)
agent. It is built on [gliderlabs/alpine](http://gliderlabs.viewdocs.io) to
be as minimal as possible.


## Building the container

Because the cloudwatch logs agent seems to only be downloadable from an
EC2 instance, this container can only be built on EC2.

```bash
$ docker build -t howgood/cloudwatch .
```


## Setup

1. Create a log configuration file, using the [configuration options
   documented here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/AgentReference.html).

2. Run the container with your configuration file mounted into the
   container, and pass it as an option:

```bash
$ docker run \
    --volume=/path/to/my-cloudwatch.conf:/etc/cloudwatch/awslogs.conf:ro \
    howgood/cloudwatch \
      push --config-file /etc/cloudwatch/awslogs.conf
```


The default configuration file that Amazon provides is [included as an
example](default.conf).
