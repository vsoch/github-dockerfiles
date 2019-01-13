## Celery Dockerfile


This repository contains **Dockerfile** of [Celery](http://www.celeryproject.org/) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/celery/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).


### Base Docker Image

* [dockerfile/python](http://dockerfile.github.io/#/python)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/celery/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/celery`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/celery" github.com/dockerfile/celery`)


### Usage

    docker run -it --rm dockerfile/celery
