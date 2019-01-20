# Repository-RI

[![License](https://img.shields.io/badge/license-BSD%203%20Clause-blue.svg?style=flat)](https://opensource.org/licenses/BSD-3-Clause) [![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](http://repository-ri.readthedocs.org/en/latest/) [![Docker](https://img.shields.io/docker/pulls/fiware/repository-ri.svg)](https://hub.docker.com/r/fiware/repository-ri) [![Support](https://img.shields.io/badge/support-askbot-yellowgreen.svg)](https://ask.fiware.org) [![Build Status](https://build.conwet.fi.upm.es/jenkins/buildStatus/icon?job=Repository-Virtuoso)](https://build.conwet.fi.upm.es/jenkins/job/Repository-Virtuoso/)
 
 * [Introduction](#introduction)
 * [GEi overall description](#gei-overall-description)
 * [Build and Install](#build-and-install)
 * [API Overview](#api-overview)
 * [API Reference](#api-reference)
 * [Testing](#testing)
 * [Advanced Topics](#advanced-topics)


## Introduction

This is the code repository for Repository-RI, the reference implementation of the Marketplace.

This project is part of [FIWARE](http://www.fiware.org). Check also the [FIWARE Catalogue entry for Repository-RI](http://catalogue.fiware.org/enablers/repository-repository-ri)!

Any feedback is highly welcome, including bugs, typos or things you think should be included but aren't. You can use [GitHub Issues](https://github.com/conwetlab/Repository-RI/issues/new) to provide feedback.

You can find the User & Programmer's Manual and the Administration Guide on [readthedocs.org](https://repository-ri.readthedocs.org)

 
## GEi overall description

Repository-RI provides a consistent uniform API to access USDL descriptions and associated media files of applications offered in the FIWARE Business Framework. Its functionality includes basic services for create, store and obtain collections and resources which contains rdf descriptions, and a Sparql query service. Besides the core functions, the Repository-RI may offer value because of its "knowledge" about resources descriptions and linked data.


## Build and Install

The instructions to install Repository-RI can be found at [the Installation Guide](http://repository-ri.readthedocs.org/en/latest/installation-guide.html). You can install the software in three different ways:

* With the provided script (`install.sh`)
* With a [Docker Container](https://hub.docker.com/r/conwetlab/repository-ri/)
* Manually
 

## API Overview

Repository-RI API is very easy. The API is available under the `/v2/` path and the available resources are:

* Resources and Collections: `/v2/collec`
* Sparql: `/v2/service/query`

The API is fully RESTful so:

* You can use `POST` requests to create resources.
 * Create a resource making a `POST` request to `/v2/collec/COLLECTIONS`
 * Create a collection a `POST` request to `/v2/collec` or `/v2/collec/COLLECTIONS`
 * Execute a Sparql query making a `POST` request to `/v2/service/query`
* You can use `PUT` requests to update resources and resources content.
 * Update a resource making a `PUT` request to `/v2/collec/COLLECTIONS/RESOURCE.meta`
 * Update a resource content making a `PUT` request to `/v2/collec/COLLECTIONS/RESOURCE`
* You can use `GET` requests to retrieve an entity.
 * Retrieve a resource making a `GET` request to `/v2/collec/COLLECTIONS/RESOURCE.meta`
 * Retrieve a resource content a `GET` request to `/v2/collec/COLLECTIONS/RESOURCE`
 * Retrieve a collection a `GET` request to `/v2/collec/COLLECTIONS`
 * Execute a Sparql query making a `POST` request to `/v2/service/query?query=SPARQLQUERY`
 * Retrieve resource content by its url content making a `GET` request to `/v2/service/query/URL_CONTENT`
* You can use `DELETE` requests to delete an entity.
 * Delete a resource and its content marking a `DELETE` request to `/v2/collec/COLLECTIONS/RESOURCES`
 * Delete a collection and its content making a `DELETE` request to `/v2/collec/COLLECTIONS`


## API Reference

For further documentation, you can check the API Reference available at:

* [Apiary](http://docs.fiwarerepository.apiary.io)
* [GitHub Pages](http://conwetlab.github.io/Repository-RI)


## Testing

### End-to-End tests

End-to-End tests are described in the [Installation Guide](http://repository-ri.readthedocs.org/en/latest/installation-guide.html#end-to-end-testing)

### Unit tests

To execute the unit tests, just run:

```
mvn test
```

### Integration tests

To execute the integration tests, just run:

```
mvn integration-test
```

## Advanced Topics

* [User & Programmers Manual](doc/user-programmer-guide.rst)
* [Installation Guide](doc/installation-guide.rst)

You can also find this documentation on [ReadTheDocs](http://repository-ri.readthedocs.org)
