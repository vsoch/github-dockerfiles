# Træfik Web UI

Access to Træfik Web UI, ex: http://localhost:8080

## Interface

Træfik Web UI provide 2 types of informations:
- Providers with their backends and frontends information.
- Health of the web server.

## How to build (for backends developer)

Use the make file :

```shell
make build           # Generate Docker image
make generate-webui  # Generate static contents in `traefik/static/` folder.
```

## How to build (only for frontends developer)

- prerequisite: [Node 4+](https://nodejs.org) [yarn](https://yarnpkg.com/)

  Note: In case of conflict with the Apache Hadoop Yarn Command Line Interface, use the `yarnpkg`
  alias.

- Go to the directory `webui`

- To install dependencies, execute the following commands:
  - `yarn install`

- Build static Web UI, execute the following command:
  - `yarn run build`

- Static contents are build in the directory `static`

**Don't change manually the files in the directory `static`**

- The build allow to:
  - optimize all JavaScript
  - optimize all CSS
  - add vendor prefixes to CSS (cross-bowser support)
  - add a hash in the file names to prevent browser cache problems
  - all images will be optimized at build
  - bundle JavaScript in one file


## How to edit (only for frontends developer)

**Don't change manually the files in the directory `static`**

- Go to the directory `webui`
- Edit files in `webui/src`

- Run in development mode :
  - `yarn run serve`

- Træfik API connections are defined in:
  - `webui/src/app/core/health.resource.js`
  - `webui/src/app/core/providers.resource.js`

- The pages contents are in the directory `webui/src/app/sections`.


## Libraries

- [Node](https://nodejs.org)
- [Yarn](https://yarnpkg.com/)
- [Generator FountainJS](https://github.com/FountainJS/generator-fountain-webapp)
- [Webpack](https://github.com/webpack/webpack)
- [AngularJS](https://docs.angularjs.org/api)
- [UI Router](https://github.com/angular-ui/ui-router)
  - [UI Router - Documentation](https://github.com/angular-ui/ui-router/wiki)
- [Bootstrap](http://getbootstrap.com)
- [Angular Bootstrap](https://angular-ui.github.io/bootstrap)
- [D3](http://d3js.org)
  - [D3 - Documentation](https://github.com/mbostock/d3/wiki)
- [NVD3](http://nvd3.org)
- [Angular nvD3](http://krispo.github.io/angular-nvd3)

<p align="center">
<img src="docs/img/traefik.logo.png" alt="Træfik" title="Træfik" />
</p>

[![Build Status SemaphoreCI](https://semaphoreci.com/api/v1/containous/traefik/branches/master/shields_badge.svg)](https://semaphoreci.com/containous/traefik)
[![Docs](https://img.shields.io/badge/docs-current-brightgreen.svg)](https://docs.traefik.io)
[![Go Report Card](https://goreportcard.com/badge/containous/traefik)](http://goreportcard.com/report/containous/traefik)
[![](https://images.microbadger.com/badges/image/traefik.svg)](https://microbadger.com/images/traefik)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/containous/traefik/blob/master/LICENSE.md)
[![Join the chat at https://traefik.herokuapp.com](https://img.shields.io/badge/style-register-green.svg?style=social&label=Slack)](https://traefik.herokuapp.com)
[![Twitter](https://img.shields.io/twitter/follow/traefikproxy.svg?style=social)](https://twitter.com/intent/follow?screen_name=traefikproxy)


Træfik (pronounced like [traffic](https://speak-ipa.bearbin.net/speak.cgi?speak=%CB%88tr%C3%A6f%C9%AAk)) is a modern HTTP reverse proxy and load balancer made to deploy microservices with ease.
It supports several backends ([Docker](https://www.docker.com/), [Swarm mode](https://docs.docker.com/engine/swarm/), [Kubernetes](http://kubernetes.io), [Marathon](https://mesosphere.github.io/marathon/), [Consul](https://www.consul.io/), [Etcd](https://coreos.com/etcd/), [Rancher](https://rancher.com), [Amazon ECS](https://aws.amazon.com/ecs), and a lot more) to manage its configuration automatically and dynamically.

---

| **[Overview](#overview)** |
**[Features](#features)** |
**[Supported backends](#supported-backends)** |
**[Quickstart](#quickstart)** |
**[Web UI](#web-ui)** |
**[Test it](#test-it)** |
**[Documentation](#documentation)** |
**[Support](#support)** |
**[Release cycle](#release-cycle)** |

| **[Contributing](#contributing)** |
**[Maintainers](#maintainers)** |
**[Plumbing](#plumbing)** |
**[Credits](#credits)** |

---

## Overview

Imagine that you have deployed a bunch of microservices on your infrastructure. You probably used a service registry (like etcd or consul) and/or an orchestrator (swarm, Mesos/Marathon) to manage all these services.
If you want your users to access some of your microservices from the Internet, you will have to use a reverse proxy and configure it using virtual hosts or prefix paths:

- domain `api.domain.com` will point the microservice `api` in your private network
- path `domain.com/web` will point the microservice `web` in your private network
- domain `backoffice.domain.com` will point the microservices `backoffice` in your private network, load-balancing between your multiple instances

But a microservices architecture is dynamic... Services are added, removed, killed or upgraded often, eventually several times a day.

Traditional reverse-proxies are not natively dynamic. You can't change their configuration and hot-reload easily.

Here enters Træfik.

![Architecture](docs/img/architecture.png)

Træfik can listen to your service registry/orchestrator API, and knows each time a microservice is added, removed, killed or upgraded, and can generate its configuration automatically.
Routes to your services will be created instantly.

Run it and forget it!


## Features

- [It's fast](http://docs.traefik.io/benchmarks)
- No dependency hell, single binary made with go
- [Tiny](https://microbadger.com/images/traefik) [official](https://hub.docker.com/r/_/traefik/) official docker image
- Rest API
- Hot-reloading of configuration. No need to restart the process
- Circuit breakers, retry
- Round Robin, rebalancer load-balancers
- Metrics (Rest, Prometheus, Datadog, Statd)
- Clean AngularJS Web UI
- Websocket, HTTP/2, GRPC ready
- Access Logs (JSON, CLF)
- [Let's Encrypt](https://letsencrypt.org) support (Automatic HTTPS with renewal)
- [Proxy Protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) support
- High Availability with cluster mode (beta)

## Supported backends

- [Docker](https://www.docker.com/) / [Swarm mode](https://docs.docker.com/engine/swarm/)
- [Kubernetes](http://kubernetes.io)
- [Mesos](https://github.com/apache/mesos) / [Marathon](https://mesosphere.github.io/marathon/)
- [Rancher](https://rancher.com) (API, Metadata)
- [Consul](https://www.consul.io/) / [Etcd](https://coreos.com/etcd/) / [Zookeeper](https://zookeeper.apache.org) / [BoltDB](https://github.com/boltdb/bolt)
- [Eureka](https://github.com/Netflix/eureka)
- [Amazon ECS](https://aws.amazon.com/ecs)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb)
- File
- Rest API

## Quickstart

You can have a quick look at Træfik in this [Katacoda tutorial](https://www.katacoda.com/courses/traefik/deploy-load-balancer) that shows how to load balance requests between multiple Docker containers. If you are looking for a more comprehensive and real use-case example, you can also check [Play-With-Docker](http://training.play-with-docker.com/traefik-load-balancing/) to see how to load balance between multiple nodes.

Here is a talk given by [Emile Vauge](https://github.com/emilevauge) at [GopherCon 2017](https://gophercon.com/).
You will learn Træfik basics in less than 10 minutes. 

[![Traefik GopherCon 2017](http://img.youtube.com/vi/RgudiksfL-k/0.jpg)](http://www.youtube.com/watch?v=RgudiksfL-k)

Here is a talk given by [Ed Robinson](https://github.com/errm) at [ContainerCamp UK](https://container.camp) conference.
You will learn fundamental Træfik features and see some demos with Kubernetes.

[![Traefik ContainerCamp UK](http://img.youtube.com/vi/aFtpIShV60I/0.jpg)](https://www.youtube.com/watch?v=aFtpIShV60I)


## Web UI

You can access the simple HTML frontend of Træfik.

![Web UI Providers](docs/img/web.frontend.png)
![Web UI Health](docs/img/traefik-health.png)


## Test it

- The simple way: grab the latest binary from the [releases](https://github.com/containous/traefik/releases) page and just run it with the [sample configuration file](https://raw.githubusercontent.com/containous/traefik/master/traefik.sample.toml):

```shell
./traefik --configFile=traefik.toml
```

- Use the tiny Docker image and just run it with the [sample configuration file](https://raw.githubusercontent.com/containous/traefik/master/traefik.sample.toml):

```shell
docker run -d -p 8080:8080 -p 80:80 -v $PWD/traefik.toml:/etc/traefik/traefik.toml traefik
```

- From sources:

```shell
git clone https://github.com/containous/traefik
```


## Documentation

You can find the complete documentation at [https://docs.traefik.io](https://docs.traefik.io).
A collection of contributions around Træfik can be found at [https://awesome.traefik.io](https://awesome.traefik.io). 


## Support

To get basic support, you can:
- join the Træfik community Slack channel: [![Join the chat at https://traefik.herokuapp.com](https://img.shields.io/badge/style-register-green.svg?style=social&label=Slack)](https://traefik.herokuapp.com) 
- use [Stack Overflow](https://stackoverflow.com/questions/tagged/traefik) (using the `traefik` tag)

If you prefer commercial support, please contact [containo.us](https://containo.us) by mail: <mailto:support@containo.us>.


## Release cycle

- Release: We try to release a new version every 2 months
  - i.e.: 1.3.0, 1.4.0, 1.5.0
- Release candidate: we do RC (1.**x**.0-rc**y**) before the final release (1.**x**.0)
  - i.e.: 1.1.0-rc1 -> 1.1.0-rc2 -> 1.1.0-rc3 -> 1.1.0-rc4 -> 1.1.0
- Bug-fixes: For each version we release bug fixes
  - i.e.: 1.1.1, 1.1.2, 1.1.3
  - those versions contain only bug-fixes
  - no additional features are delivered in those versions
- Each version is supported until the next one is released
  - i.e.: 1.1.x will be supported until 1.2.0 is out
- We use [Semantic Versioning](http://semver.org/)


## Contributing

Please refer to [contributing documentation](CONTRIBUTING.md).


### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.


## Maintainers

[Information about process and maintainers](MAINTAINER.md)


## Plumbing

- [Oxy](https://github.com/vulcand/oxy): an awesome proxy library made by Mailgun folks
- [Gorilla mux](https://github.com/gorilla/mux): famous request router
- [Negroni](https://github.com/urfave/negroni): web middlewares made simple
- [Lego](https://github.com/xenolf/lego): the best [Let's Encrypt](https://letsencrypt.org) library in go


## Credits

Kudos to [Peka](http://peka.byethost11.com/photoblog/) for his awesome work on the logo ![logo](docs/img/traefik.icon.png).
Traefik's logo licensed under the Creative Commons 3.0 Attributions license.

Traefik's logo was inspired by the gopher stickers made by Takuya Ueda (https://twitter.com/tenntenn).
The original Go gopher was designed by Renee French (http://reneefrench.blogspot.com/).
# How to generate the self-signed wildcard certificate

```bash
#!/usr/bin/env bash

# Specify where we will install
# the wildcard certificate
SSL_DIR="./ssl"

# Set the wildcarded domain
# we want to use
DOMAIN="*.acme.wtf"

# A blank passphrase
PASSPHRASE=""

# Set our CSR variables
SUBJ="
C=FR
ST=MP
O=
localityName=Toulouse
commonName=$DOMAIN
organizationalUnitName=Traefik
emailAddress=
"

# Create our SSL directory
# in case it doesn't exist
sudo mkdir -p "$SSL_DIR"

# Generate our Private Key, CSR and Certificate
sudo openssl genrsa -out "$SSL_DIR/wildcard.key" 2048
sudo openssl req -new -subj "$(echo -n "$SUBJ" | tr "\n" "/")" -key "$SSL_DIR/wildcard.key" -out "$SSL_DIR/wildcard.csr" -passin pass:$PASSPHRASE
sudo openssl x509 -req -days 3650 -in "$SSL_DIR/wildcard.csr" -signkey "$SSL_DIR/wildcard.key" -out "$SSL_DIR/wildcard.crt"
sudo rm -f "$SSL_DIR/wildcard.csr"
```# This is how the certs were created

```bash
openssl req -new -newkey rsa:2048 -x509 -days 3650 -extensions v3_ca -keyout ca1.pem -out ca1.crt
openssl req -new -newkey rsa:2048 -x509 -days 3650 -extensions v3_ca -keyout ca2.pem -out ca2.crt
openssl req -new -newkey rsa:2048 -x509 -days 3650 -extensions v3_ca -keyout ca3.pem -out ca3.crt
openssl rsa -in ca1.pem -out ca1.key
openssl rsa -in ca2.pem -out ca2.key
openssl rsa -in ca3.pem -out ca3.key
cat ca1.crt ca2.crt > ca1and2.crt
rm ca1.pem ca2.pem ca3.pem

openssl genrsa -out client1.key 2048
openssl genrsa -out client2.key 2048
openssl genrsa -out client3.key 2048

openssl req -key client1.key -new -out client1.csr
openssl req -key client2.key -new -out client2.csr
openssl req -key client3.key -new -out client3.csr

openssl x509 -req -days 3650 -in client1.csr -CA ca1.crt -CAkey ca1.key -CAcreateserial -out client1.crt
openssl x509 -req -days 3650 -in client2.csr -CA ca2.crt -CAkey ca2.key -CAcreateserial -out client2.crt
openssl x509 -req -days 3650 -in client3.csr -CA ca3.crt -CAkey ca3.key -CAcreateserial -out client3.crt

```
# TLS certificate description

## local.crt / local.key

Generate with
```bash
go run $GOROOT/src/crypto/tls/generate_cert.go  --rsa-bits 1024 --host 127.0.0.1,::1,localhost --ca --start-date "Jan 1 00:00:00 1970" --duration=1000000h
mv cert.pem local.cert
mv key.pem local.key
```
