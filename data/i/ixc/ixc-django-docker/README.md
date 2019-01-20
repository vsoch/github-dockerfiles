=========================================================
Run Django projects consistently, with and without Docker
=========================================================

Quick Start
===========

If you are running an existing ``ixc-django-docker`` project:

- see the notes on `How to run an ixc-django-docker project`_
- see also `How to run a remote debug server with pydevd <docs/how-tos.rst>`_
  if you like to debug within PyCharm

If you need to convert an existing project to use ``ixc-django-docker`` see
`How to dockerize an existing project <docs/how-tos.rst>`_ and be sure to read
and understand the rest of the documention.

About
=====

This project an effort to:

* Making it easier to run Django projects consistently with and without Docker
  (for Mac/Windows, Cloud, etc.), in development and production environments.

* Solving issues relating to horizontal scaling and ephemeral infrastructure,
  where you have no persistent local storage and requests are handled by
  multiple servers in a load balanced configuration.

* Providing a migration path towards Docker for legacy projects.

* Getting new projects up and running quickly with a consistent and familiar
  base to build from.

It includes:

* A reference Django project that *wraps* another Django project to provide
  sensible default settings plus many optional but commonly needed features.

* A *wrapped* Django project template that you can use as a starting point for
  new projects or when Dockerizing a legacy project.

See the `rationale <docs/rationale.rst>`_ documentation for more context about
how this project helps to solve common issues with scaling and ephemeral
infrastructure.

Django project wrapper
======================

The ``ixc_django_docker`` Python package is a Django project (settings, URLs,
etc.) that wraps another project by including additional settings, static files,
templates, URLs, etc., from the other project.

This makes it easy to enable optional but commonly needed features and evolve
our shared understanding of current best practices over time.

See the `Django project wrapper <docs/project-wrapper.rst>`_ documentation for
more details.


Wrapped Django project template
===============================

The ``project_template`` directory is an example *wrapped* Django project.

To create a new project from the template:

    $ bash <(curl -Ls https://raw.githubusercontent.com/ixc/ixc-django-docker/master/startproject.sh) PROJECT_NAME

To upgrade an existing ``ixc-django-docker`` project with the currently
installed version of the template:

    # TODO This command does not yet exist
    $ manage.py update_ixc_django_docker_project_template

Otherwise, see `How to dockerize an existing project <docs/how-tos.rst>`

See the `Django project template <docs/project-template.rst>`_ documentation
for more details.


Composable settings
===================

The ``ixc_django_docker.settings`` package includes many composable settings
modules that can be combined as required.

An ``ixc_django_docker`` project must set at least the following environment
variables: ``DOTENV`` and ``TRANSCRYPT_PASSWORD`` (or ``GPG_PASSPHRASE``).
You will likely also need to set project-specific ``BASE_SETTINGS`` and
``PROJECT_SETTINGS`` variables, as well as additional variables depending on
the features used in your project. The ``VAR_DIR`` environment variable is
also available if you'd like to specify where the var folder gets created.

See the `Composable settings <docs/composable-settings.rst>`_ documentation
for more details on how to set environment variables based on how you will
run a project, and a list of all the available settings modules.


Encrypted secrets
=================

Secrets should only be stored in ``*.secret*`` files which will be encrypted by
``transcrypt``.

To enable, set the ``TRANSCRYPT_PASSWORD`` environment variable in
``.env.local`` and Docker stack files. This password is generally available in
IC's 1Password for existing projects.

See the `Encrypted secrets <docs/secrets.rst>`_ documentation for more details
on how to use Transcrypt.


How to run an ixc-django-docker project
=======================================

To run an ``ixc-django-docker`` project there are two main steps:

- start an runtime environment with the required environment variables and
  settings prepared, see below
- use this project's commands within that environment to run the server,
  perform DB migrations, and so on. See `Commands in ixc-django-docker projects
  <docs/commands.rst>`_

How to run with Docker
----------------------

Running a project with Docker environment will run in an environment that is
almost identical to production, with no need to manage service dependencies.

The main drawback is that it can be significantly slower on macOS due to
performance issues with ``osxfs`` shared volumes. See:
https://forums.docker.com/t/file-access-in-mounted-volumes-extremely-slow-cpu-bound/8076/1

Build or re-build the project's Docker image, with ``--pulll`` if/when you want
to get the latest version of any base images::

    $ docker-compose build [--pull]

Run an interactive shell::

    $ docker-compose run --rm --service-ports bash

Start all services::

    $ docker-compose up -d haproxy

View logs for all services::

    $ docker-compose logs -f

Stop all services::

    $ docker-compose stop

How to run without Docker
-------------------------

Running a project via ``go.sh`` configures an interactive shell in such a way
that all our shell scripts and project configuration still works as it would
under Docker.

A project run this way will generally perform much quicker than with Docker, but
you will need to manage service dependencies manually.

However, you can still run those service dependencies via Docker, and as long as
they don't use an ``osxfs`` shared volume, performance should be acceptable.

Start services::

    $ docker-compose up -d elasticsearch postgres redis

Or:

    $ brew services start elasticsearch
    $ brew services start postgres
    $ brew services start redis

Run an interactive shell::

    $ ./go.sh

Run individual processes::

    $ celery.sh
    $ celerybeat.sh
    $ celeryflower.sh
    $ runserver.sh

Stop services::

    $ docker-compose stop

Or:

    $ brew services stop elasticsearch
    $ brew services stop postgres
    $ brew services stop redis


System requirements when running without Docker
-----------------------------------------------

* [Dockerize](https://github.com/jwilder/dockerize)
* [jq](https://stedolan.github.io/jq/)
* md5sum
* Nginx
* NPM
* [Pipe Viewer](http://www.ivarch.com/programs/pv.shtml)
* [PostgreSQL](https://postgresapp.com)
* Python 2.7 or 3.x
* Redis
* Supervisor
* [Transcrypt](https://github.com/elasticdog/transcrypt)
* Yarn

Optional:

* Elasticsearch 2.x (5.x is not compatible with ``django-haystack``)


macOS
^^^^^

Install Xcode command line tools::

    $ xcode-select --install

Install `Homebrew <http://brew.sh/>`__::

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install required system packages::

    $ brew cask install postgres
    $ brew install ixc/ixc/dockerize@0.5 jq md5sha1sum nginx node@8 pv redis supervisor transcrypt
    $ brew install yarn --without-node  # Avoid installing the latest non-LTS Node
    $ brew link --force dockerize@0.5

Start Redis::

    $ brew services start redis

Install optional system packages::

    $ brew install elasticsearch@2.4
    $ brew link elasticsearch@2.4 --force

Start Elasticsearch::

    $ brew services start elasticsearch
