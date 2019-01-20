.. contents:: Table of Contents
   :depth: 2

Perfmetrics configuration for Zope and Plone
============================================

zperfmetrics works like and depends on `perfmetrics <https://pypi.python.org/pypi/perfmetrics>`_, additional it:

- offers a ZConfig configuration for the statsd,
- uses the current requests path in the statd dotted path prefix,
- also provides a patch to measure plone.app.theming for diazo compile and diazo transform if Plone is available,


Installation
============

First get your ``statsd`` configured properly.
This is out of scope of this module.

Depend on this module in your packages ``setup.py``.

Given you use ``zc.builodut`` to set up your Zope2 or Plone,
add to your ``[instance]`` section or the section with ``recipe = plone.recipe.zope2instance`` the lines::

    [instance01]
    recipe = plone.recipe.zope2instance
    ...
    zope-conf-imports =
        zperfmetrics
    zope-conf-additional =
        <perfmetrics>
            uri statsd://localhost:8125
            before MyFancyProject
            hostname on
            virtualhost on
            after ${:_buildout_section_name_}
        </perfmetrics>
    ...

Given this runs on a host called ``w-plone1``,
this will result in a prefix ``MyFancyProject.w-plone1.instance01``.

uri
    Full URI of statd.

before
    Prefix path before the hostname.

hostname
    Get hostname and insert into prefix.
    (Boolean: ``on`` or ``off``)

virtualhost
    Get virtualhost and use in ZPerfmetrics after the static prefix.
    (Boolean: ``on`` or ``off``)

after
    Prefix path after the hostname.


Usage
=====

You need to decorate your code or use the ``with`` statement to measure a code block.

Usage::

    from zperfmetrics import ZMetric
    from zperfmetrics import zmetric
    from zperfmetrics import zmetricmethod

    @zmetric
    def some_function():
        # whole functions timing and call counts will be measured
        pass

    @ZMetric(stat='a_custom_prefix')
    def some_other_function():
        # set a custom prefix instead of module path and fucntion name.
        pass

    class Foo(object):

        @zmetricmethod
        def some_method(self):
            # whole methods timing and call counts will be measured
            pass

        @ZMetric(method=True, timing=False):
        def some_counted_method(self):
            # whole methods number of calls will be measured, but no times
            pass

        @ZMetric(method=True, count=False):
        def some_timed_method(self):
            # whole methods timing be measured, but no counts
            pass

        def some_method_partly_measured(self):
            # do something here you dont want to measure
            with ZMetric(stat='part_of_other_method_time'):
                # do something to measure
                # call counts and timing will be measured
                pass
            # do something here you dont want to measure

        @ZMetric(method=True, rate=0.5):
        def some_random_recorded_method(self):
            # randomly record 50% of the calls.
            pass


Request Lifecycle Integration
=============================

All ZPerfmetrics with a request passed in are considered to be under the ``request_lifecycle`` section.

All metrics in here are build like: ``$PREFIX.request_lifecycle.[$VIRTUAL_HOST].$PATH.*``.

Zope
----

This package provides subscribers to measure the time a request takes,
including some points in time between.

These subscribers are loaded via zcml and are logging under ``publish.*``:

``publish.traversal``
    time needed from publication start until traversal is finished.

``publish.rendering``
    time needed from traversal end until before commit begin.

    This value is a bit fuzzy and should be taken with a grain of salt,
    because there can be other subscribers to this event which take their time.
    Since the order of execution of the subscribers is not defined,
    processing may happen after this measurement

    If plone tranformchain is active,
    the rendering time is before transforms are starting.

``publish.finalize``
    time needed from rendering end (or transform end if plone.transformchain is active) until database commit is done.

``publish_all``
    whole time needed from publication start until request is completly processed.

Plone
-----

Installing this package in Plone by depending on ``zperfmetrics[plone]`` forces usage of ``plone.transformchain`` version 1.2 or newer.

First, ``publish.rendering`` gets less fuzzy because the expensive transforms (also subscribers to publish.beforecommit) are all done.

Then it introduces new measurements related to ``plone.transformchain``:

``publish.transform_all``
    time needed for all transforms in the ``plone.transformchain``.
    This usually includes Diazo.

``publish_transform_single.${ORDER}-${TRANSFORMNAME}``
    time needed for a specific single transform.
    transforms are ordered and named, both are replaced.


This package patches:

``diazo.setup`` metric
    ``plone.app.theming.transform.ThemeTransform.setupTransform`` is patched as a basic (path-less) perfmetrics ``Metric``.
    The setup of the transform happens once on startup and is the time needed to create the Diazo xslt from its rules.xml, index.html and related files.

Statd, Graphite & Grafana in Docker
===================================

Setting up Statsd, Graphite and Grafana can be complex.
For local testing - but also for production environments - firing up some docker containers comes in handy.

A very minimal version of such a `Statd, Graphite & Grafana in Docker setup <https://github.com/collective/zperfmetrics/tree/master/docker>`_ (`original <https://github.com/Ennexa/docker-graphite>`_) helps getting things initially up and running.
`Install Docker <https://docs.docker.com/engine/installation/>`_ and `install docker-compose <https://docs.docker.com/compose/install/>`_ (just ``pip install docker-compose``),
then just clone the repository and in its ``docker`` directory run ``docker-compose up -d``.

Let Zperfmetrics point to ``uri statsd://localhost:8125`` and collect some data.
Open Grafana in your browser at ``http://localhost:3000``.

Go first to `Grafana Getting Started <http://docs.grafana.org/guides/gettingstarted/>`_,
the 10 minute video *really helps* to find the hidden part of its UI.

Source Code
===========

The sources are in a GIT DVCS with its main branches at `github <https://github.com/collective/zperfmetrics>`_.

We'd be happy to see many branches, forks and pull-requests to make zperfmetrics even better.

Contributors
============

- Jens W. Klein <jens@bluedynamics.com>

- Zalán Somogyváry
