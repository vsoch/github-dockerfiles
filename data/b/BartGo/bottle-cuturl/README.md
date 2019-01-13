

=============
Bottle-cuturl
=============

v0.0.22

A simple favourites / URL shortening app in Python. Work in progress.
The idea is to have a simple, working web application linked with a set 
of tools - which could be used in larger projects.

Uses:

- `Bottle`_ (microframework), Skeleton

- PostgreSQL with `SQLAlchemy`_ (ORM), fallback to SQLite

- `cookiecutter-bottle`_ template, `bumpversion`, `vendor`, `crashreporter`

- playing with testing, using `unittest`, `nosetests`, `tox`, `behave`, `WebTest`

Works with Travis CI, successfull builds are deployed to Heroku:

http://fathomless-everglades-8154.herokuapp.com/

You can do the same:

.. image:: https://www.herokucdn.com/deploy/button.svg
    :target: https://heroku.com/deploy?template=https://github.com/bartgo/bottle-cuturl/production

Deployment to Heroku is done against the version defined in runtime.txt, as specified in

https://github.com/heroku/heroku-buildpack-python

At some moment automatic deployments will work with Openshift as well.

Quickstart
----------

Running in development mode (prepare virtual environment and run the app inside):

.. code-block:: bash

    devinit.sh
    devrun.sh

I am struggling a bit with releasing to PyPi, it will work soon.

.. code-block:: bash

    # no uncommited changes at this point
    devucl.sh
    bumpversion --allow-dirty patch
    git add .
    git commit -m "Bump version: x.x.x → y.y.y"
    git tag vy.y.y
    git push
    git push --tags
    # .pypirc must be prepared, see http://peterdowns.com/posts/first-time-with-pypi.html
    # python setup.py register -r pypitest
    # python setup.py sdist upload -r pypitest
    # python setup.py register -r pypi
    # python setup.py sdist upload -r pypi
    # python setup.py sdist bdist_wheel upload

.. image:: https://travis-ci.org/BartGo/bottle-cuturl.svg?branch=master
    :target: https://travis-ci.org/BartGo/bottle-cuturl

.. image:: https://semaphoreci.com/api/v1/projects/82f94cd9-6144-4e99-966e-649ca567a603/531764/badge.svg
    :target: https://semaphoreci.com/bartgo/bottle-cuturl

.. image:: https://codeship.com/projects/b9cd91a0-0880-0133-b16d-52c6dae51101/status?branch=master
    :target: https://codeship.com/projects/90320
    :alt: Codeship Status

.. image:: https://circleci.com/gh/BartGo/bottle-cuturl/tree/master.svg?style=svg
    :target: https://circleci.com/gh/BartGo/bottle-cuturl/tree/master

.. image:: https://requires.io/github/BartGo/bottle-cuturl/requirements.svg?branch=master
     :target: https://requires.io/github/BartGo/bottle-cuturl/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://img.shields.io/gemnasium/BartGo/bottle-cuturl.svg
     :target: https://gemnasium.com/BartGo/bottle-cuturl
     :alt: Gemnasium Status

.. image:: https://codecov.io/gh/BartGo/bottle-cuturl/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/BartGo/bottle-cuturl
  
.. image:: http://img.shields.io/pypi/v/Bottle-Cuturl.svg
     :target: https://pypi.python.org/pypi/Bottle-Cuturl
     :alt: PyPI

.. _cookiecutter-bottle: https://github.com/avelino/cookiecutter-bottle
.. _bottle: http://bottlepy.org/docs/dev/index.html
.. _sqlalchemy: http://www.sqlalchemy.org/


