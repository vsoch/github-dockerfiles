[![dockeri.co](http://dockeri.co/image/bandsintown/alpine)](https://hub.docker.com/r/bandsintown/alpine/)

[![Build status](https://badge.buildkite.com/f78e045c0b561ba33f80f3c996ccfe89b49ade24b832f92bfd.svg)](https://buildkite.com/bandsintown/docker-alpine)
[![GitHub issues](https://img.shields.io/github/issues/bandsintown/docker-alpine.svg "GitHub issues")](https://github.com/bandsintown/docker-alpine)
[![GitHub stars](https://img.shields.io/github/stars/bandsintown/docker-alpine.svg "GitHub stars")](https://github.com/bandsintown/docker-alpine)
[![Docker layers](https://images.microbadger.com/badges/image/bandsintown/alpine.svg)](http://microbadger.com/images/bandsintown/alpine)
	
# What is Alpine Linux?

![logo](https://github.com/bandsintown/docker-alpine/blob/master/logo.png)

[Alpine Linux](http://alpinelinux.org/) is a very small Linux distribution built around [musl libc](http://www.musl-libc.org/) and [BusyBox](http://www.busybox.net/).

This makes Alpine Linux a great image base for utilities and even production applications. [Read more about Alpine Linux here](https://www.alpinelinux.org/about/) and you can see how their mantra fits in right at home with Docker images.


# About

This image is derived from the well tested and documented [Alpine Docker image](http://gliderlabs.viewdocs.io/docker-alpine/) image adding: 
 - the [s6 supervisor for containers](https://github.com/just-containers/s6-overlay) 
 - a lightweight [DNS resolver](https://github.com/janeczku/go-dnsmasq) with minimal runtime and filesystem overhead 
 - [Consul Template](https://github.com/hashicorp/consul-template) for service discovery and configuration management
 - some useful packages: `bash`, `tree`, `curl`, `wget`, 
 - since 3.5 this packages have been added:`jq`, `bind-tools`, `consul`

## Motivation

Alpine Linux does not support the `search` keyword in resolv.conf. This breaks many tools that rely on DNS service discovery (e.g. Kubernetes, Tutum.co, Consul).

Additionally Alpine Linux deviates from the established concept of primary and secondary nameservers. This leads to problems in cases where the container is configured with multiple nameserver with inconsistent records (e.g. one Consul server and one recursing server).
    
To overcome these issues the image includes a lightweight (1.2 MB) container-only [DNS resolver](https://github.com/janeczku/go-dnsmasq) that replicates the behavior of GNU libc's stub-resolver.

## How it works

On container start the DNS resolver parses the `nameserver` and `search` entries from `resolv.conf` and configures itself as nameserver for the container. DNS queries from local processes are handled following these conventions:
* The nameserver listed first in resolv.conf is always queried first. Additional nameservers are treated as fallbacks.
* Hostnames are qualified by appending the domains configured with the `search` keyword in resolv.conf
* Single-label hostnames (e.g.: "redis-master") are always qualified with search domains
* Multi-label hostnames are first tried as absolute names and only then qualified with search domains


# Usage

The official Alpine Docker image is well documented, so check out [their documentation](http://gliderlabs.viewdocs.io/docker-alpine) to learn more about building micro Docker images with Alpine Linux.

## Basic usage    

Building your own image based on this image is as easy as:


```Dockerfile
FROM bandsintown/alpine
RUN apk-install <package_name>

CMD ["/bin/bash"]
```

or :

```
docker run -ti bandsintown/alpine
```

## Supervised services

By default the [s6 supervisor](https://github.com/just-containers/s6-overlay) is enabled because the `ENTRYPOINT` is  defined to `/init`.

### DNS resolver

In the case you need to disable the [DNS resolver](https://github.com/janeczku/go-dnsmasq) you can just pass the environment variable `DISABLE_DNSMASQ`:

```
docker run -ti --entrypoint=/init -e DISABLE_DNSMASQ=true bandsintown/alpine bash 
```

### Consul Template

In the case you need to disable [Consul Template](https://github.com/hashicorp/consul-template) you can just pass the environment variable `DISABLE_CONSUL_TEMPLATE`:

```
docker run -ti --entrypoint=/init -e DISABLE_CONSUL_TEMPLATE=true bandsintown/alpine bash 
```

The `CONSUL_HTTP_ADDR` might be passed as an environment variable to define the address of Consul:

```
docker run -ti --entrypoint=/init -e CONSUL_HTTP_ADDR=demo.consul.io bandsintown/alpine bash 
```


Alternatively if you run your containers on AWS and you need to get the host IP, you can use the variable `RUN_ON_AWS`:

```
docker run -ti --entrypoint=/init -e RUN_ON_AWS=true bandsintown/alpine bash 
```

The configuration of Consul template must be located in `/etc/consul-template/conf`.


# Build

This project is configured as an [automated build in Dockerhub](https://hub.docker.com/r/bandsintown/alpine/).

Each branch give the related image tag.  

# License

All the code contained in this repository, unless explicitly stated, is
licensed under ISC license.

A copy of the license can be found inside the [LICENSE](LICENSE) file.