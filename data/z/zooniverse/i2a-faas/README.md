# i2a-faas
## Functions as a Service for Intro2Astro

This repo contains the raw python3 functions for i2a as well as the [OpenFaaS](https://github.com/openfaas/faas)-built makings of a Docker container. The built container is located on [Dockerhub](https://hub.docker.com/r/zooniverse/func_i2a_hubble/). This container will live in Docker Swarm soon. It's designed to be used as an external extractor for [Caesar](https://github.com/zooniverse/caesar). 

The Hubble's Law function takes a Caesar-style Classification as its input and returns returns extracted and calculated values as JSON. To use locally, follow the instructions [here](https://blog.alexellis.io/first-faas-python-function/) using this cloned repo as your starting point.
