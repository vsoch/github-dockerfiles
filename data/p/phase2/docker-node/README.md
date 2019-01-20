# Outrigger Node

> Node image for a JavaScript server side platform.

[![GitHub tag](https://img.shields.io/github/tag/phase2/docker-node.svg)](https://github.com/phase2/docker-node)
[![Docker Stars](https://img.shields.io/docker/stars/outrigger/node.svg)](https://hub.docker.com/r/outrigger/node)
[![Docker Pulls](https://img.shields.io/docker/pulls/outrigger/node.svg)](https://hub.docker.com/r/outrigger/node)
[![MicroBadger](https://images.microbadger.com/badges/image/outrigger/node.svg)](https://microbadger.com/images/outrigger/node "Get your own image badge on microbadger.com")

For more documentation on how Outrigger images are constructed and how to work
with them, please [see the documentation](http://docs.outrigger.sh/).

## Node <= v6

Based on outrigger/servicebase, which provides a CentOS-base, s6 init system
and confd configuration templating.

## Node v8, v10

Based on official Node images, specifically the Alpine variant, and
adds special functionality on top. Currently that includes:

* tini init system
* Coordinated support for Yarn and npm
* Run services as the `node` user instead of as `root`.

We have switched to a simple templating mechanism to ease support for multiple node versions, assuming we want to handle future node versions in a manner identical
to v8.

## Usage Example

The examples in this repo use Yarn, but you can use npm as well.

### Docker Run - Node REPL

```bash
docker run --rm -it outrigger/node:8
```

### Docker Compose - Project-style

For a more thorough example of how you would use outrigger/node:2-node8 or greater
in a "real" project, check out ./examples.

```yaml
api: '3.4'
services:
  app:
    image: outrigger/node:8
    container_name: projectname_app
    command: "yarn install && yarn start"
    labels:
      com.dnsdock.name: app
      com.dnsdock.image: projectname
    network_mode: bridge
    volumes:
      - .:/code
```

### Node v4 and v6

In the current version of Node v4 and v6, npm install and start routines are
built-in to the image. This makes them more project-centric out of the box.

```bash
docker run --rm -v ~/Project/node-app:/code outrigger/node:6
```

## Environment Variables

Outrigger images use Environment Variables and [confd](https://github.com/kelseyhightower/confd)
to "templatize" a number of Docker environment configurations. These templates are
processed on startup with environment variables passed in via the docker run
command-line or via your docker-compose manifest file. Here are the "tunable"
configurations offered by this image.

This only applies to Node v4 and v6.

* `SKIP_NPM_INSTALL`: If this is set (to anything) it will not run `npm install` when the container boots.

## Security Reports

Please email outrigger@phase2technology.com with security concerns.

## Maintainers

[![Phase2 Logo](https://s3.amazonaws.com/phase2.public/logos/phase2-logo.png)](https://www.phase2technology.com)
