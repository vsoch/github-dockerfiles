PySOA Example Service
=====================

This is meant to serve as an example of how to best write a PySOA service and handle a variety of different patterns.
All code is thoroughly commented, and suitable for copying to base a new service.

If you are developing a service internally for Eventbrite, the recommendations and suggestions in this document are
requirements rather than suggestions.

We recommend that any service you make have a README like this that briefly describes what's included in the service
and how to work with it. We further recommend detailed documentation for the service in the ``docs/`` directory,
containing at least ``index.rst``.

New PySOA services should use Python 3.5 or newer, not Python 2 or Python 3.1-3.4 (although PySOA will maintain
backward compatibility with Python 2 and Python 3.4 for a considerable time for legacy reasons).


Experimenting with this Example Service
---------------------------------------

This Example Service contains a ``Dockerfile`` and a ``docker_env`` executable that helps you start a fully-functional
remote Example Service with Redis Gateway transport. To get started, build the environment, which takes a few minutes
the first time, and a few seconds subsequent times, depending on your Internet speed::

    $ ./docker_env build

You can then start the ``pysoa-redis`` and ``example_service`` containers and shell into the ``example_service``
container as follows::

    $ ./docker_env shell

Once inside, you can run tests or run the service (the third command is a shortcut for the second command)::

    # pytest
    # python3 -m example_service.standalone -s example_service.settings.dev
    # rs

With the service running, you can press ``Ctrl-C`` to tell it to shut down, and then type ``exit`` to leave the
container. The ``pysoa-redis`` container will continue running in the background. ``./docker_env stop`` will stop it.

You can also start/run ``example_service`` in the background and run an ``example_service_client`` container to test
out the service communication::

    $ ./docker_env client
    # ./example_client.py status
    # ./example_client.py square 42

You can also start/run ``example_service`` in the background, and link ``pysoa-redis`` to your own client container to
test calling the service::

    $ ./docker_env
    $ docker run -it --name my_test_client --link pysoa-redis:redis --entrypoint=/bin/bash my_test_client


Suggested topics to include in your README
------------------------------------------

Purpose
+++++++

* What is this service in charge of and what questions does it answer?


Maintainer
++++++++++

* Which team maintains this service?


Dependencies
++++++++++++

* What external dependencies does this service have? One possible audience for this is your operations/production team,
  but this is also important for future maintainers and developers. Examples might be "Redis," "MySQL database,"
  "Kafka," or "Cassandra."


Developing for this service locally (Getting Started)
+++++++++++++++++++++++++++++++++++++++++++++++++++++

* General guidelines for working on the service
* Is there a specific core container to use?
* Is there a recommended profile?
* Any gotchas, common errors, or pitfalls?


How to Run Tests for this Service
+++++++++++++++++++++++++++++++++

* Running all tests
* Running a specific test


Release and Versioning
++++++++++++++++++++++

* Instructions on releasing this service standalone
* Instructions on managing service as a library/local service, if allowed
* Additional deployment steps if this service is remote


Suggested Project Layout
------------------------

We recommend that all services have their Python code in the top-level, with a ``setup.py`` file, a README file, and
the service package directly in that top level directory, like so::

    docs/
        index.rst
        ...
    example_service/
        __init__.py
        ...
        server.py
        standalone.py
        ...
        version.py
    tests/
        ...
    .gitignore
    README.rst
    setup.cfg
    setup.py

Don't put the code in a ``python/`` sub-directory or similar.


Building
--------

The service should be capable of being built using ``python3 setup.py test`` (which should install all dependencies and
run ``pytest`` as documented below).


Testing
-------

Use PyTest (``pytest``) to run tests. Do not use nosetests, as it is now deprecated and unmaintained, and not compatible
with certain features of PySOA.

The ``setup.cfg`` and ``setup.py`` files contained here use PyTest to run tests located in a ``tests/`` directory.
