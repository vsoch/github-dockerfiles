# API v2
[![Build Status](https://semaphoreci.com/api/v1/projects/8dec2741-95b9-4746-9203-6d4acb1f06f3/548342/badge.svg)](https://semaphoreci.com/renderedtext/api)

Semaphore public API v2 - RAML specification.

## Where can you find the api specification?

Every time we merge into master, the new specification is pushed to S3.

Visit [api-v2-specs.semaphoreci.com](http://api-v2-specs.semaphoreci.com) to get
a list of currently published APi v2 specifications.

## Setting up a development environment

1. Install docker-compose:

``` bash
sudo pip install docker-compose
```

2. In the root of the project, type:

``` bash
docker-compose up
```

_note_: This will take a while the first time.

## Generating a JSON RAML spec

```
docker-compose run app scripts/compile
```
