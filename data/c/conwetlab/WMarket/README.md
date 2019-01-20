# WMarket

 [![License](https://img.shields.io/badge/license-BSD%203%20Clause-blue.svg?style=flat)](https://opensource.org/licenses/BSD-3-Clause) [![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](http://wmarket.readthedocs.org/en/latest/)  [![Docker](https://img.shields.io/docker/pulls/fiware/wmarket.svg)](https://hub.docker.com/r/fiware/wmarket) [![Support](https://img.shields.io/badge/support-askbot-yellowgreen.svg)](https://ask.fiware.org) [![Build Status](https://build.conwet.fi.upm.es/jenkins/buildStatus/icon?job=WMarket)](https://build.conwet.fi.upm.es/jenkins/job/WMarket/)

 * [Introduction](#introduction)
 * [GEi overall description](#gei-overall-description)
 * [Build and Install](#build-and-install)
 * [API Overview](#api-overview)
 * [API Reference](#api-reference)
 * [Testing](#testing)
 * [Advanced Topics](#advanced-topics)


## Introduction

This is the code repository for WMarket, the reference implementation of the Marketplace.

This project is part of [FIWARE](http://www.fiware.org). Check also the [FIWARE Catalogue entry for WMarket](http://catalogue.fiware.org/enablers/marketplace-wmarket)!

Any feedback is highly welcome, including bugs, typos or things you think should be included but aren't. You can use [GitHub Issues](https://github.com/conwetlab/WMarket/issues/new) to provide feedback.

You can find the User & Programmer's Manual and the Administration Guide on [readthedocs.org](https://wmarket.readthedocs.org)


## GEi overall description

WMarket provides functionality necessary for bringing together offering and demand for making business. These functions include basic services for registering business entities, publishing and retrieving offerings and demands, search and discover offerings according to specific consumer requirements as well as lateral functions like review, rating and recommendation. Besides the core functions, the Marketplace may offer value because of its "knowledge" about the market in terms of market intelligence services, pricing support, advertising, information subscription and more.


## Build and Install

The instructions to install WMarket can be found at [the Installation Guide](http://wmarket.readthedocs.org/en/latest/installation-guide.html). You can install the software in three different ways:

* With the provided script (included in the `utils` folder)
* With a [Docker Container](https://hub.docker.com/r/conwetlab/wmarket/)
* Manually

If you opt for building WMarket, you can refer to [the Building from Sources Guide](http://wmarket.readthedocs.org/en/latest/building-from-sources-guide.html)


## API Overview

WMarket API is very easy. The API is available under the `/api/v2/` path and the available resources are:

* Users: `/api/v2/user`
* Stores: `/api/v2/store`
* Descriptions: `/api/v2/store/STORE_NAME/description`
* Offerings: `/api/v2/store/STORE_NAME/description/DESCRIPTION_NAME/offering`

The API is fully RESTful so:

* You can use `POST` requests to create resources.
 * Create a user making a `POST` request to `/api/v2/user`
 * Create a store making a `POST` request to `/api/v2/store`
 * Create a description making a `POST` request to `/api/v2/store/STORE_NAME/description`
* You can use `POST` requests to update resources partially.
 * Update a user making a `POST` request to `/api/v2/user/USER_NAME`
 * Update a store making a `POST` request to `/api/v2/store/STORE_NAME`
 * Update a description making a `POST` request to `/api/v2/store/STORE_NAME/description/DESCRIPTION_NAME`
* You can use `GET` requests to retrieve an entity.
 * Retrieve a user making a `GET` request to `/api/v2/user/USER_NAME`
 * Retrieve a store making a `GET` request to `/api/v2/store/STORE_NAME`
 * Retrieve a description making a `GET` request to `/api/v2/store/STORE_NAME/description/DESCRIPTION_NAME`
 * Retrieve an offering making a `GET` request to `/api/v2/store/STORE_NAME/description/DESCRIPTION_NAME/offering/OFFERING_NAME`
* You can use `DELETE` requests to delete an entity.
 * Delete a user marking a `DELETE` request to `/api/v2/user/USER_NAME`
 * Delete a store making a `DELETE` request to `/api/v2/store/STORE_NAME`
 * Delete a description making a `DELETE` request to `/api/v2/store/STORE_NAME/description/DESCRIPTION_NAME`


## API Reference

For further documentation, you can check the API Reference available at:

* [Apiary](http://docs.fiwaremarketplace.apiary.io)
* [GitHub Pages](http://conwetlab.github.io/WMarket)


## Testing

### End-to-End tests

End-to-End tests are described in the [Installation Guide](http://wmarket.readthedocs.org/en/latest/installation-guide.html#end-to-end-testing)

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
* [Administration Guide](doc/administration-guide.rst)
* [Building from Sources Guide](doc/building-from-sources-guide.rst)

You can also find this documentation on [ReadTheDocs](http://wmarket.readthedocs.org)
