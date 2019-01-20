# Docker for Protonet Platform System Integrators

First steps leading to a local installation suitable for all tasks regarding the integration of an existing application into Protonet Platform.

## Installation

Initial requirements are  `docker`, `docker-compose` and if the development machine does run OS X instead of linux, `docker-machine`. As OS X does not support docker directly VirtualBox will be used to run a linux machine.

On Linux [docker](https://docs.docker.com/linux/step_one/) and [docker-compose](https://docs.docker.com/engine/installation/ubuntulinux/) should be readily available, on OS X the [Docker Toolbox](https://www.docker.com/docker-toolbox) installs all requirements.

## Basics

Protonet Platform provides persistent storage as file system (mounted on `/data/`), as well as multiple structured storage services (for example Elasticsearch, MySQL, and PostgreSQL).

For local development and testing these are provided by simple docker containers. Dependencies and different independent testing environments are managed using `docker-compose`.

## Initial Configuration

For local development, we start by providing the service dependencies that will later be provided by the Platform using a minimal `docker-compose.yml`:

```yaml
kibana:
  image: kibana@4
  links:
    - elasticsearch
  ports:
    - "80:5601"
  
elasticsearch:
  image: elasticsearch@2
```

Start the composition with `docker-compose up` and Elasticsearch and Kibana will come up.

In this case we use [Elasticsearch](https://hub.docker.com/_/elasticsearch/) but [MySQL](https://hub.docker.com/_/mysql/), [PostgreSQL](https://hub.docker.com/_/postgres/) and many more are easily available.

## Adding custom components

As a next step, you will need to specify how to create a Docker image for your software. You will need to create a `Dockerfile` and tell docker-compose where to find it.

In most cases products consist of one ore more components, for example a worker, a dispatcher and a web interface. We suggest to run a separate docker container for each component to ensure separation of concerns. Of course, these containers can all be based on the same image or entirely separate ones ([What's the difference between docker images and cointainers?](http://stackoverflow.com/questions/21498832/in-docker-whats-the-difference-between-a-container-and-an-image)).

As these components are not available from the docker hub we need to build them ourselves:

  1. Create a directory for each component.
  2. Add any needed configuration files
  3. Create a suitable `Dockerfile`
  4. Extend the docker-compose.yml

The docker community [provides various base images for popular programming languages](https://blog.docker.com/2014/09/docker-hub-official-repos-announcing-language-stacks/) and versions that you can use for containerizing your software.

**Note**: Building and packaging of the software typically is usually done in a prior step (most likely by a CI) and thus not part of this tutorial. The steps taken by your Continuous Integration solution would be to build a docker image, run your test suite inside the container, then on success push the image to a [Docker Registry](https://docs.docker.com/registry/)

To understand best practice regarding building a `Dockerfile` and thus containerizing software we strongly suggest reviewing the following documentation:

  * [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
  * [Dockerfile best practices](https://docs.docker.com/engine/articles/dockerfile_best-practices/)
  * [Tutorials on Dockerizing various services in the Docker documentation](https://docs.docker.com/engine/examples/)

A highly recommended, more generic overview of core principles useful when working in a containerized environment, but not specific to Docker or Protonet Platform is **[The Twelve-Factor App](http://12factor.net/)**

## Example Integrations

Enough with all the theory - we have fully documented and working examples that you can use as reference on getting started with Docker integration. All examples are selected so that minimal code is needed.

  * **[Logstash](example-logstash/)** - A fully working example that creates a custom logstash image that consumes the heise.de RSS feed, puts it into Elasticsearch and makes it searchable using Kibana
  * **[Ruby Web App](example-ruby-webapp/)** - Shows how to containerize a Ruby web application using the community-provided [Ruby docker base image](https://hub.docker.com/_/ruby/)

## Cookbook

For some useful tips for solving common problems while developing against platform, we have a **[Cookbook](COOKBOOK.md)**