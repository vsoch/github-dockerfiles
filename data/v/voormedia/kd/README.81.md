<img src="docs/images/notary-blk.svg" alt="Notary" width="400px"/>

[![Circle CI](https://circleci.com/gh/theupdateframework/notary/tree/master.svg?style=shield)](https://circleci.com/gh/theupdateframework/notary/tree/master) [![CodeCov](https://codecov.io/github/theupdateframework/notary/coverage.svg?branch=master)](https://codecov.io/github/theupdateframework/notary) [![GoReportCard](https://goreportcard.com/badge/theupdateframework/notary)](https://goreportcard.com/report/github.com/theupdateframework/notary)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftheupdateframework%2Fnotary.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftheupdateframework%2Fnotary?ref=badge_shield)

# Notice

The Notary project has officially been accepted in to the Cloud Native Computing Foundation (CNCF).
It has moved to https://github.com/theupdateframework/notary. Any downstream consumers should update
their Go imports to use this new location, which will be the canonical location going forward.

We have moved the repo in GitHub, which will allow existing importers to continue using the old
location via GitHub's redirect.

# Overview

The Notary project comprises a [server](cmd/notary-server) and a [client](cmd/notary) for running and interacting
with trusted collections. See the [service architecture](docs/service_architecture.md) documentation
for more information.

Notary aims to make the internet more secure by making it easy for people to
publish and verify content. We often rely on TLS to secure our communications
with a web server which is inherently flawed, as any compromise of the server
enables malicious content to be substituted for the legitimate content.

With Notary, publishers can sign their content offline using keys kept highly
secure. Once the publisher is ready to make the content available, they can
push their signed trusted collection to a Notary Server.

Consumers, having acquired the publisher's public key through a secure channel,
can then communicate with any notary server or (insecure) mirror, relying
only on the publisher's key to determine the validity and integrity of the
received content.

## Goals

Notary is based on [The Update Framework](https://www.theupdateframework.com/), a secure general design for the problem of software distribution and updates. By using TUF, notary achieves a number of key advantages:

* **Survivable Key Compromise**: Content publishers must manage keys in order to sign their content. Signing keys may be compromised or lost so systems must be designed in order to be flexible and recoverable in the case of key compromise. TUF's notion of key roles is utilized to separate responsibilities across a hierarchy of keys such that loss of any particular key (except the root role) by itself is not fatal to the security of the system.
* **Freshness Guarantees**: Replay attacks are a common problem in designing secure systems, where previously valid payloads are replayed to trick another system. The same problem exists in the software update systems, where old signed can be presented as the most recent. notary makes use of timestamping on publishing so that consumers can know that they are receiving the most up to date content. This is particularly important when dealing with software update where old vulnerable versions could be used to attack users.
* **Configurable Trust Thresholds**: Oftentimes there are a large number of publishers that are allowed to publish a particular piece of content. For example, open source projects where there are a number of core maintainers. Trust thresholds can be used so that content consumers require a configurable number of signatures on a piece of content in order to trust it. Using thresholds increases security so that loss of individual signing keys doesn't allow publishing of malicious content.
* **Signing Delegation**: To allow for flexible publishing of trusted collections, a content publisher can delegate part of their collection to another signer. This delegation is represented as signed metadata so that a consumer of the content can verify both the content and the delegation.
* **Use of Existing Distribution**: Notary's trust guarantees are not tied at all to particular distribution channels from which content is delivered. Therefore, trust can be added to any existing content delivery mechanism.
* **Untrusted Mirrors and Transport**: All of the notary metadata can be mirrored and distributed via arbitrary channels.

## Security

See Notary's [service architecture docs](docs/service_architecture.md#threat-model) for more information about our threat model, which details the varying survivability and severities for key compromise as well as mitigations.

Notary's last security audit was on July 31, 2015 by NCC ([results](docs/resources/ncc_docker_notary_audit_2015_07_31.pdf)).

Any security vulnerabilities can be reported to security@docker.com.

# Getting started with the Notary CLI

Get the Notary Client CLI binary from [the official releases page](https://github.com/theupdateframework/notary/releases) or you can [build one yourself](#building-notary).
The version of Notary server and signer should be greater than or equal to Notary CLI's version to ensure feature compatibility (ex: CLI version 0.2, server/signer version >= 0.2), and all official releases are associated with GitHub tags.

To use the Notary CLI with Docker hub images, have a look at Notary's
[getting started docs](docs/getting_started.md).

For more advanced usage, see the
[advanced usage docs](docs/advanced_usage.md).

To use the CLI against a local Notary server rather than against Docker Hub:

1. Ensure that you have [docker and docker-compose](http://docs.docker.com/compose/install/) installed.
1. `git clone https://github.com/theupdateframework/notary.git` and from the cloned repository path,
    start up a local Notary server and signer and copy the config file and testing certs to your
    local notary config directory:

    ```sh
    $ docker-compose build
    $ docker-compose up -d
    $ mkdir -p ~/.notary && cp cmd/notary/config.json cmd/notary/root-ca.crt ~/.notary
    ```

1. Add `127.0.0.1 notary-server` to your `/etc/hosts`, or if using docker-machine,
    add `$(docker-machine ip) notary-server`).

You can run through the examples in the
[getting started docs](docs/getting_started.md) and
[advanced usage docs](docs/advanced_usage.md), but
without the `-s` (server URL) argument to the `notary` command since the server
URL is specified already in the configuration, file you copied.

You can also leave off the `-d ~/.docker/trust` argument if you do not care
to use `notary` with Docker images.


## Building Notary

Note that Notary's [latest stable release](https://github.com/theupdateframework/notary/releases) is at the head of the
[releases branch](https://github.com/theupdateframework/notary/tree/releases).  The master branch is the development
branch and contains features for the next release.

Prerequisites:

- Go >= 1.7.1
- [godep](https://github.com/tools/godep) installed
- libtool development headers installed
    - Ubuntu: `apt-get install libltdl-dev`
    - CentOS/RedHat: `yum install libtool-ltdl-devel`
    - Mac OS ([Homebrew](http://brew.sh/)): `brew install libtool`

Run `make client`, which creates the Notary Client CLI binary at `bin/notary`.
Note that `make client` assumes a standard Go directory structure, in which
Notary is checked out to the `src` directory in your `GOPATH`. For example:
```
$GOPATH/
    src/
        github.com/
            theupdateframework/
                notary/
```

To build the server and signer, run `docker-compose build`.


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftheupdateframework%2Fnotary.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftheupdateframework%2Fnotary?ref=badge_large)## Credits

This implementation was originally forked from [flynn/go-tuf](https://github.com/flynn/go-tuf)

This implementation retains the same 3 Clause BSD license present on 
the original flynn implementation.
This directory contains sample repositories from different versions of Notary client (TUF metadata, trust anchor certificates, and private keys), in order to test backwards compatibility (that newer clients can read old-format repositories).

Notary client makes no guarantees of future-compatibility though (that is, repositories produced by newer clients may not be able to be read by old clients.)

Backwards compatibility has been tested in `client/backwards_compatibility_test.go`

Relevant information for repositories:

- `notary0.1`
	- GUN: `docker.com/notary0.1/samplerepo`
	- key passwords: "randompass"
	- targets:

		```
		   NAME                                  DIGEST                                SIZE (BYTES)
		---------------------------------------------------------------------------------------------
		  LICENSE   9395bac6fccb26bcb55efb083d1b4b0fe72a1c25f959f056c016120b3bb56a62   11309
  		```
  	- It also has a changelist to add a `.gitignore` target, that hasn't been published.

- `notary0.3`
	- GUN: `docker.com/notary0.3/samplerepo`
	- delegations: targets/releases
	- key passwords: "randompass"
	- targets:

		```
		NAME                                  DIGEST                                SIZE (BYTES)         ROLE        
        ----------------------------------------------------------------------------------------------------------------
          LICENSE   9395bac6fccb26bcb55efb083d1b4b0fe72a1c25f959f056c016120b3bb56a62   11309          targets           
          change    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855   0              targets           
          hello     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855   0              targets/releases
  		```
    - Has a delegation key in the targets/releases role and a corresponding key imported
    - It also has a changelist to add a `MAINTAINERS` target, that hasn't been published to testing publish success.
    - It also has a changelist to add a `Dockerfile` target (an empty file) in the targets/releases role, that hasn't been published to testing publish success with a delegation.
    - unpublished changes:
    
        ```
        Unpublished changes for docker.com/notary0.3/tst:
        
        action    scope     type        path
        ----------------------------------------------------
        create    targets   target      MAINTAINERS
        create    targets/releasestarget      Dockerfile
        ```
    $ bin/notary -c cmd/notary/config.json -d /tmp/notary0.1 list docker.com/notary0.1/samplerepo
   NAME                                  DIGEST                                SIZE (BYTES)  
---------------------------------------------------------------------------------------------
  LICENSE   9395bac6fccb26bcb55efb083d1b4b0fe72a1c25f959f056c016120b3bb56a62   11309         


$ bin/notary -c cmd/notary/config.json -d /tmp/notary0.1 status docker.com/notary0.1/samplerepo
Unpublished changes for docker.com/notary0.1/samplerepo:

action    scope     type        path
----------------------------------------------------
create    targets   target      .gitignore
<!--[metadata]>
+++
draft = true
+++
<![end-metadata]-->

# Contributing to the Docker Notary documentation

The documentation in this directory is part of the [https://docs.docker.com](https://docs.docker.com) website.  Docker uses [the Hugo static generator](http://gohugo.io/overview/introduction/) to convert project Markdown files to a static HTML site. 

You don't need to be a Hugo expert to contribute to the Notary documentation. If you are familiar with Markdown, you can modify the content in the `docs` files.  

If you want to add a new file or change the location of the document in the menu, you do need to know a little more.

## Documentation contributing workflow

1. Edit a Markdown file in the tree.

2. Save your changes.

3. Make sure you are in the `docs` subdirectory.

4. Build the documentation.

        $ make docs
         ---> ffcf3f6c4e97
        Removing intermediate container a676414185e8
        Successfully built ffcf3f6c4e97
        docker run --rm -it  -e AWS_S3_BUCKET -e NOCACHE -p 8000:8000 -e DOCKERHOST "docs-base:test-tooling" hugo server --port=8000 --baseUrl=192.168.59.103 --bind=0.0.0.0
        ERROR: 2015/06/13 MenuEntry's .Url is deprecated and will be removed in Hugo 0.15. Use .URL instead.
        0 of 4 drafts rendered
        0 future content 
        12 pages created
        0 paginator pages created
        0 tags created
        0 categories created
        in 55 ms
        Serving pages from /docs/public
        Web Server is available at http://0.0.0.0:8000/
        Press Ctrl+C to stop

5. Open the available server in your browser.

## Tips on Hugo metadata and menu positioning

The top of each Docker Notary documentation file contains TOML metadata. The metadata is commented out to prevent it from appearing in GitHub.

    <!--[metadata]>
    +++
    title = "Extending services in Notary"
    description = "How to use Docker Notary's extends keyword to share configuration between files and projects"
    keywords = ["fig, composition, Notary, docker, orchestration, documentation, docs"]
    [menu.main]
    parent="smn_workw_Notary"
    weight=2
    +++
    <![end-metadata]-->  

The metadata alone has this structure:

    +++
    title = "Extending services in Notary"
    description = "How to use Docker Notary's extends keyword to share configuration between files and projects"
    keywords = ["fig, composition, Notary, docker, orchestration, documentation, docs"]
    [menu.main]
    parent="smn_workw_Notary"
    weight=2
    +++
    
The `[menu.main]` section refers to navigation defined [in the main Docker menu](https://github.com/docker/docs-base/blob/hugo/config.toml). This metadata says *add a menu item called* Extending services in Notary *to the menu with the* `smn_workdw_Notary` *identifier*.  If you locate the menu in the configuration, you'll find *Create multi-container applications* is the menu title.

You can move an article in the tree by specifying a new parent. You can shift the location of the item by changing its weight.  Higher numbers are heavier and shift the item to the bottom of menu. Low or no numbers shift it up.


## Other key documentation repositories

The `docker/docs-base` repository contains [the Hugo theme and menu configuration](https://github.com/docker/docs-base). If you open the `Dockerfile` you'll see the `make docs` relies on this as a base image for building the Notary documentation.
    
The `docker/docs.docker.com` repository contains [build system for building the Docker documentation site](https://github.com/docker/docs.docker.com). Fork this repository to build the entire documentation site.
# Database Migrations

This directory contains database migrations for the server and signer. They
are being managed using [this tool](https://github.com/mattes/migrate).
Within each of the server and signer directories are directories for different
database backends. Notary server and signer use GORM and are therefore 
capable of running on a number of different databases, however migrations
may contain syntax specific to one backend.
