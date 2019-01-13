crits_docker
============

## Synopsis

Configurations for building docker.io containers for CRITs.  Enables rapid deployment of both development and production docker containers for running CRITs.

<!--- Build terminal gif --->
<!---
## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.
--->

## Motivation

[Crits](https://crits.github.io/) is a great open source malware and threat repository.  It comes with a specification to create a local development environment (using [vagrant](https://www.vagrantup.com/) and [salt](http://www.saltstack.com/)), but this requires:
1. A host that can run VirtualBox/VMWare
1. Running CRITs in a single instance

[Docker](https://www.docker.com/) provides a lightweight, highly performant means of provisioning containers for software.  This is ideally suited for quickly provisioning both development instances, as well as fully functional and performant production instances.

This project provides the Docker configurations and scripts for standing up a fully functional, 2-node (Mongo backend + web frontend) CRITs system.

## Installation

1. Install Docker
<!--- Expand --->
1. Install Fig
<!--- Expand --->
1. Build Images
<!--- Expand --->
1. Start containers (using fig)
<!--- Expand --->
1. Initialize DB
<!--- Expand --->
1. Profit
<!--- Expand --->

## Contributors

* Adam Sealey
 * <asealey@gmail.com>
 * [@AdamSealey](https://twitter.com/adamsealey)

## License

This work is licensed under [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.html).
