synapse-tools
=============

[![Build Status](https://travis-ci.org/Yelp/synapse-tools.svg?branch=master)](https://travis-ci.org/Yelp/synapse-tools)
[![Download](https://api.bintray.com/packages/yelp/paasta/synapse-tools/images/download.svg)](https://bintray.com/yelp/paasta/synapse-tools/_latestVersion)


Tools for working with [synapse](https://github.com/airbnb/synapse).
This repo builds as a [dh_virtualenv](https://github.com/spotify/dh-virtualenv) package, and provides three entry points:

configure_synapse
-----------------

Creates a Synapse configuration and restarts Synapse when the config changes.


haproxy_synapse_reaper
----------------------

Kills old [HAProxy](http://www.haproxy.org) processes that are handling long-lived connections.
When HAProxy is reloaded, the old process sticks around until all its connections terminate.
Some protocols have connections that last a long time or indefinitely, leading to a buildup of HAProxy processes.
This script cleans those up.

synapse_qdisc_tool
------------------

Manages the plug queueing discipline to prevent connections from being dropped while reloading HAProxy.
See the help text for more info.

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
