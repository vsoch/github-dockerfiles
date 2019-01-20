ImmerCV
=======

ImmerCV produces tailor-made CVs and résumés.
With it, you build and navigate a professional biography,
then select individual elements for each CV.

Print-friendly CVs provide a link back to the website,
providing the opportunity for an immersive look at past and present work.

In addition to producing CVs, ImmerCV can be a blogging platform.
It publishes RSS feeds for experiences, notes, and links,
and every page is search-engine friendly.

LICENSE: BSD


IMPORTANT NOTE
--------------

This is in "release early" stage and as such, this README does not yet
reflect an ideal state of helping you set up

Please submit Github tickets if you have questions,
and we'll update docs as needed based on interest and demand.

This project made use of the `cookiecutter-django`_ project template.

..  _cookiecutter-django:
    http://cookiecutter-django.readthedocs.org/en/latest/


Technology used
---------------

- Python 3.5
- Django 1.8
- Neo4j
- PostgreSQL
- Docker


Examples of ImmerCV in action
-----------------------------

- `Matthew Scott's ImmerCV <http://cv.11craft.com/>`__

Settings
--------

See also `cookiecutter-django settings`_.

..  _cookiecutter-django settings:
    http://cookiecutter-django.readthedocs.org/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

The system is built only to support a single "Person" node,
attached to the superuser account. Account signup via the web
is disabled.

To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

Once you log in you'll need to configure your email account.

For convenience, you can keep your superuser logged in on Chrome
and your anonymous user logged in on Firefox (or similar),
so that you can see how the site behaves for both kinds of users.


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.org/en/latest/live-reloading-and-sass-compilation.html


Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use `MailHog`_ when generating the project a local SMTP server with a web interface will be available.

.. _mailhog: https://github.com/mailhog/MailHog

To start the service, make sure you have nodejs installed, and then type the following::

    $ npm install
    $ grunt serve

(After the first run you only need to type ``grunt serve``) This will start an email server that listens on ``127.0.0.1:1025`` in addition to starting your Django project and a watch task for live reload.

To view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

The email server will exit when you exit the Grunt task on the CLI with Ctrl+C.





It's time to write the code!!!


Running end to end integration tests
------------------------------------

N.B. The integration tests will not run on Windows.

To install the test runner::

  $ pip install hitch

To run the tests, enter the immercv/tests directory and run the following commands::

  $ hitch init

Then run the stub test::

  $ hitch test stub.test

This will download and compile python, postgres and redis and install all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.


Deployment
----------

We providing tools and instructions for deploying using Docker and Heroku.

Heroku
^^^^^^

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-on-heroku.html

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-with-docker.html
