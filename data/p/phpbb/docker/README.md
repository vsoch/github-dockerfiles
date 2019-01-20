Docker for phpBB
================

This repository contains a set of scripts and Dockerfiles used to run the tests in various environment.

Dockerfiles
-----------

The directory `ìmages/php/` contains the dockerfiles of a set of images pre configured to run phpBB unit or functional tests. And `ìmages/bamboo/` a dockerfile which can be used to run an agent compatible with our Bamboo installation (NB: no need to try to use it, the agents needs to be manually authenticated).

`ìmages/` also contains a set of scripts which can be used to build and push all images easily.

Scripts
-------

`scripts/` contains a set of scripts used to run the tests on our Bamboo instance.
They can also be used to run the tests locally:

```
$ source docker/scripts/local-env-mapping.sh
$ docker/scripts/jobs/unit-tests.sh <db> <php version>
$ docker/scripts/jobs/functional-tests.sh <db> <php version>
```

db being: sqlite|postgres|mysql|oracle
and php version: 5.4|5.5|5.6|7.0
