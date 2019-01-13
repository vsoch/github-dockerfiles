## FPM Dockerfile


This repository contains **Dockerfile** of [FPM](https://github.com/jordansissel/fpm) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/fpm/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).


### Base Docker Image

* [dockerfile/ruby](http://dockerfile.github.io/#/ruby)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/fpm/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/fpm`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/fpm" github.com/dockerfile/fpm`)


### Usage

    docker run -it --rm dockerfile/fpm

#### Run `fpm`

    docker run -it --rm dockerfile/fpm fpm
