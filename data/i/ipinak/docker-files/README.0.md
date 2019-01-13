
# DjangoPypi Server


## Installation

To get setup with the server you must have the follow installed:

1. docker

## Configuration

1. Set your smtp server in settings.json
2. Set your domain name and default account in setup_script.py

## Build & Run

Add a share folder for keep sqlite db and packages.

``` shell
$ mkdir -p /var/docker/djangopypi2
```

Build docker images

``` shell
$ docker pull ubuntu:13.10
$ docker build -t pypi:latest Djangopypi2-Dockerfile
```

Run this container:

``` shell
$ docker run -i -t -p 80:80 -v /var/docker/djangopypi2:/var/data pypi:latest
```
