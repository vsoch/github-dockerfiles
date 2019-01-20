nerve-tools
===========
[![Build Status](https://travis-ci.org/Yelp/nerve-tools.svg?branch=master)](https://travis-ci.org/Yelp/nerve-tools)

Tools for working with [nerve](https://github.com/airbnb/nerve).
This repo builds as a [dh_virtualenv](https://github.com/spotify/dh_virtualenv) package, and provides three entry points:

configure_nerve
---------------

Determines the list of services running on the local box (scheduled by [Paasta](https://github.com/Yelp/paasta) or manually configured), writes out a nerve config, and restarts nerve.

updown_service
--------------

De-register a service.
Tells [hacheck](https://github.com/uber/hacheck) to fail healthchecks for a service,
and waits until the deregistration has propagated to the local [synapse](https://github.com/airbnb/synapse).

clean_nerve
-----------

Clean up orphaned ZK nodes left by nerve.


Configuration
=============

This package uses [environment_tools](https://github.com/yelp/environment_tools) to reason about location hierarchies;
you must have a `location_types.json` and `location_mapping.json` describing your environments.

You will also need zookeeper topology files, at `/nail/etc/zookeeper_discovery/infrastructure/{superregion}.yaml`.
This must parse as a list of servers; each server is represented as a list of `[hostname, port]`.

For example:
```yaml
---
 - ["hostname1", 2181]
 - ["hostname2", 2181]
 - ["hostname3", 2181]
```

See the [Paasta documentation for per-service info](http://paasta.readthedocs.org/en/latest/yelpsoa_configs.html#smartstack-yaml).
