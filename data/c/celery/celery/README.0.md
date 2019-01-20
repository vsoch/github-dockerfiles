.. image:: http://docs.celeryproject.org/en/latest/_images/celery-banner-small.png

|build-status| |license| |wheel| |pyversion| |pyimp|

.. include:: ../includes/introduction.txt

.. include:: ../includes/installation.txt

.. include:: ../includes/resources.txt

.. |build-status| image:: https://secure.travis-ci.org/celery/celery.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/celery

.. |coverage| image:: https://codecov.io/github/celery/celery/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/celery?branch=master

.. |license| image:: https://img.shields.io/pypi/l/celery.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/celery.svg
    :alt: Celery can be installed via wheel
    :target: https://pypi.org/project/celery/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/celery.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/celery/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/celery.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/celery/
=================
 Celery Examples
=================


* pythonproject

Example Python project using celery.

* httpexample

Example project using remote tasks (webhook tasks)

* celery_http_gateway

Example HTTP service exposing the ability to apply tasks and query the
resulting status/return value.

==============================================================
 Example Django project using Celery
==============================================================

Contents
========

``proj/``
---------

This is a project in itself, created using
``django-admin.py startproject proj``, and then the settings module
(``proj/settings.py``) was modified to add ``demoapp`` to
``INSTALLED_APPS``

``proj/celery.py``
----------

This module contains the Celery application instance for this project,
we take configuration from Django settings and use ``autodiscover_tasks`` to
find task modules inside all packages listed in ``INSTALLED_APPS``.

``demoapp/``
------------

Example generic app.  This is decoupled from the rest of the project by using
the ``@shared_task`` decorator.  This decorator returns a proxy that always
points to the currently active Celery instance.

Installing requirements
=======================

The settings file assumes that ``rabbitmq-server`` is running on ``localhost``
using the default ports. More information here:

http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html

In addition, some Python requirements must also be satisfied:

.. code-block:: console

    $ pip install -r requirements.txt

Starting the worker
===================

.. code-block:: console

    $ celery -A proj worker -l info

Running a task
===================

.. code-block:: console

    $ python ./manage.py shell
    >>> from demoapp.tasks import add, mul, xsum
    >>> res = add.delay(2,3)
    >>> res.get()
    5
==============================
 Example Celery->HTTP Gateway
==============================

This is an example service exposing the ability to apply tasks and query
statuses/results over HTTP.

Some familiarity with Django is recommended.

`settings.py` contains the celery settings, you probably want to configure
at least the broker related settings.

To run the service you have to run the following commands::

    $ python manage.py syncdb # (if running the database backend)

    $ python manage.py runserver


The service is now running at http://localhost:8000


You can apply tasks, with the `/apply/<task_name>` URL::

    $ curl http://localhost:8000/apply/celery.ping/
    {"ok": "true", "task_id": "e3a95109-afcd-4e54-a341-16c18fddf64b"}

Then you can use the resulting task-id to get the return value::

    $ curl http://localhost:8000/e3a95109-afcd-4e54-a341-16c18fddf64b/status/
    {"task": {"status": "SUCCESS", "result": "pong", "id": "e3a95109-afcd-4e54-a341-16c18fddf64b"}}


If you don't want to expose all tasks there're a few possible
approaches. For instance you can extend the `apply` view to only
accept a white-list. Another possibility is to just make views for every task you want to
expose. We made on such view for ping in `views.ping`::

    $ curl http://localhost:8000/ping/
    {"ok": "true", "task_id": "383c902c-ba07-436b-b0f3-ea09cc22107c"}
==================================
  Example using the Eventlet Pool
==================================

Introduction
============

This is a Celery application containing two example tasks.

First you need to install Eventlet, and also recommended is the `dnspython`
module (when this is installed all name lookups will be asynchronous)::

    $ pip install eventlet
    $ pip install dnspython
    $ pip install requests

Before you run any of the example tasks you need to start
the worker::

    $ cd examples/eventlet
    $ celery worker -l info --concurrency=500 --pool=eventlet

As usual you need to have RabbitMQ running, see the Celery getting started
guide if you haven't installed it yet.

Tasks
=====

* `tasks.urlopen`

This task simply makes a request opening the URL and returns the size
of the response body::

    $ cd examples/eventlet
    $ python
    >>> from tasks import urlopen
    >>> urlopen.delay('http://www.google.com/').get()
    9980

To open several URLs at once you can do::

    $ cd examples/eventlet
    $ python
    >>> from tasks import urlopen
    >>> from celery import group
    >>> result = group(urlopen.s(url)
    ...                     for url in LIST_OF_URLS).apply_async()
    >>> for incoming_result in result.iter_native():
    ...     print(incoming_result)

* `webcrawler.crawl`

This is a simple recursive web crawler.  It will only crawl
URLs for the current host name.  Please see comments in the
`webcrawler.py` file.
========================
 pip requirements files
========================


Index
=====

* :file:`requirements/default.txt`

    Default requirements for Python 2.7+.

* :file:`requirements/jython.txt`

    Extra requirements needed to run on Jython 2.5

* :file:`requirements/security.txt`

    Extra requirements needed to use the message signing serializer,
    see the Security Guide.

* :file:`requirements/test.txt`

    Requirements needed to run the full unittest suite.

* :file:`requirements/test-ci-base.txt`

    Extra test requirements required by the CI suite (Tox).

* :file:`requirements/test-ci-default.txt`

    Extra test requirements required for Python 2.7 by the CI suite (Tox).

* :file:`requirements/test-integration.txt`

    Extra requirements needed when running the integration test suite.

* :file:`requirements/doc.txt`

    Extra requirements required to build the Sphinx documentation.

* :file:`requirements/pkgutils.txt`

    Extra requirements required to perform package distribution maintenance.

* :file:`requirements/dev.txt`

    Requirement file installing the current dev branch of Celery and
    dependencies (will not be present in stable branches).

Examples
========

Installing requirements
-----------------------

::

    $ pip install -U -r requirements/default.txt


Running the tests
-----------------

::

    $ pip install -U -r requirements/default.txt
    $ pip install -U -r requirements/test.txt
