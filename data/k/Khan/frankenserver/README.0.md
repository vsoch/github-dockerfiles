Copyright 2008 Google Inc.
All rights reserved.

App Engine SDK - Development tools for Google App Engine

CONTENTS
========

   * Installing on Mac OSX
   * Installing on Windows
   * Installing on Linux and other platforms
   * Running the SDK
   * Using the SDK
   * Using the App Engine Launcher


INSTALLING ON Mac OSX
=====================
1) Download and install Python 2.7 from http://www.python.org/download/
2) Download the SDK installer from
https://developers.google.com/appengine/downloads
3) Install the SDK by double-clicking on the GoogleAppEngine.dmg file and
running the installer.


INSTALLING ON WINDOWS
=====================
1) Download and install Python 2.7 from http://www.python.org/download/
2) Download the SDK installer from
https://developers.google.com/appengine/downloads
3) Install the SDK by double-clicking on the GoogleAppEngine.msi file and
running the installer.


INSTALLING ON LINUX AND OTHER PLATFORMS
===============================
1) Download and install Python 2.7 from http://www.python.org/download/
2) Download the SDK zip file from
https://developers.google.com/appengine/downloads
3) Unpack the zip file.


RUNNING THE SDK
=========================
You can run the SDK with the following command:

dev_appserver.py [options] <application root>

Application root must be the path to the application to run in this server.
Must contain a valid app.yaml or app.yml file.

Options:
  --address=ADDRESS, -a ADDRESS
                             Address to which this server should bind. (Default
                             localhost).
  --clear_datastore, -c      Clear the Datastore on startup. (Default false)
  --debug, -d                Use debug logging. (Default false)
  --help, -h                 View this helpful message.
  --port=PORT, -p PORT       Port for the server to run on. (Default 8080)

  --allow_skipped_files      Allow access to files matched by app.yaml's
                             skipped_files (default False)
  --auth_domain              Authorization domain that this app runs in.
                             (Default gmail.com)
  --auto_id_policy=POLICY    Dictate how automatic IDs are assigned by the
                             datastore stub, "sequential" or "scattered".
                             (Default sequential)
  --backends                 Run the dev_appserver with backends support
                             (multiprocess mode).
  --blobstore_path=DIR       Path to directory to use for storing Blobstore
                             file stub data.
  --clear_prospective_search Clear the Prospective Search subscription index
                             (Default false).
  --clear_search_indexes     Clear the Full Text Search indexes (Default false).
  --datastore_path=DS_FILE   Path to file to use for storing Datastore file
                             stub data.
                             (Default /tmp/dev_appserver.datastore)
  --debug_imports            Enables debug logging for module imports, showing
                             search paths used for finding modules and any
                             errors encountered during the import process.
  --default_partition        Default partition to use in the APPLICATION_ID.
                             (Default dev)
  --disable_static_caching   Never allow the browser to cache static files.
                             (Default enable if expiration set in app.yaml)
  --disable_task_running     When supplied, tasks will not be automatically
                             run after submission and must be run manually
                             in the local admin console.
  --enable_sendmail          Enable sendmail when SMTP not configured.
                             (Default false)
  --high_replication         Use the high replication datastore consistency
                             model. (Default false).
  --history_path=PATH        Path to use for storing Datastore history.
                             (Default /tmp/dev_appserver.datastore.history)
  --persist_logs             Enables storage of all request and application
                             logs to enable later access. (Default false).
  --logs_path=LOGS_FILE      Path to use for storing request logs. If this is
                             set, logs will be persisted to the given path. If
                             this is not set and --persist_logs is true, logs
                             are stored in /tmp/dev_appserver.logs.
  --multiprocess_min_port    When running in multiprocess mode, specifies the
                             lowest port value to use when choosing ports. If
                             set to 0, select random ports.
                             (Default 9000)
  --mysql_host=HOSTNAME      MySQL database host that the rdbms API will use.
                             (Default localhost)
  --mysql_port=PORT          MySQL port to connect to.
                             (Default 3306)
  --mysql_user=USER          MySQL user to connect as.
                             (Default '')
  --mysql_password=PASSWORD  MySQL password to use.
                             (Default '')
  --mysql_socket=PATH        MySQL Unix socket file path.
                             (Default '%(mysql_socket)s')
  --require_indexes          Disallows queries that require composite indexes
                             not defined in index.yaml.
  --search_indexes_path=PATH Path to file to use for storing Full Text Search
                             indexes (Default %(search_indexes_path)s).
  --show_mail_body           Log the body of emails in mail stub.
                             (Default false)
  --skip_sdk_update_check    Skip checking for SDK updates. If false, fall back
                             to opt_in setting specified in .appcfg_nag
                             (Default false)
  --smtp_host=HOSTNAME       SMTP host to send test mail to.  Leaving this
                             unset will disable SMTP mail sending.
                             (Default '')
  --smtp_port=PORT           SMTP port to send test mail to.
                             (Default 25)
  --smtp_user=USER           SMTP user to connect as.  Stub will only attempt
                             to login if this field is non-empty.
                             (Default '').
  --smtp_password=PASSWORD   Password for SMTP server.
                             (Default '')
  --task_retry_seconds       How long to wait in seconds before retrying a
                             task after it fails during execution.
                             (Default '30')
  --use_sqlite               Use the new, SQLite based datastore stub.
                             (Default false)
  --port_sqlite_data         Converts the data from the file based datastore
                             stub to the new SQLite stub, one time use only.
                             Requires enough RAM to hold all of the entities.
                             (Default false)
  --[enable|disable]_console Enables/disables the interactive console.
                             (Default enabled if --address is unset,
                              disabled if --address is set)


USING THE SDK
=======================
For instructions on getting started with Google App Engine, please see the
Google App Engine Getting Started Guide

https://developers.google.com/appengine/docs/python/gettingstarted


USING THE APP ENGINE LAUNCHER
=============================
The Windows and Mac OSX Python SDKs include an additional development tool
called the App Engine Launcher.  This tool provides a simple graphical
interface to create projects, run them locally, and deploy them to Google's App
Engine servers. It can be used in place of the dev_appserver and appcfg
command-line tools.

The Windows SDK can optionally install a desktop short-cut during
installation. If you are missing the short-cut, you can find the launcher in
the launcher subdirectory of your App Engine installation. The default
location is
C:\Program Files\Google\google_appengine\launcher\GoogleAppEngineLauncher.exe

In Mac OSX, the Launcher is installed by dragging it out of the .dmg to a
location specified by the user. The Launcher contains the SDK inside of it.
A typical drag-install destination for the Launcher and SDK is
/Applications/GoogleAppEngineLauncher.app
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

All documentation is in the "docs" directory and online at
http://docs.djangoproject.com/en/dev/. If you're just getting started, here's
how we recommend you read the docs:

    * First, read docs/intro/install.txt for instructions on installing Django.

    * Next, work through the tutorials in order (docs/intro/tutorial01.txt,
      docs/intro/tutorial02.txt, etc.).

    * If you want to set up an actual deployment server, read
      docs/howto/deployment/index.txt for instructions.

    * You'll probably want to read through the topical guides (in docs/topics)
      next; from there you can jump to the HOWTOs (in docs/howto) for specific
      problems, and check out the reference (docs/ref) for gory details.

    * See docs/README for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think they
should be clarified in any way, please take 30 seconds to fill out a ticket
here:

http://code.djangoproject.com/newticket

To get more help:

    * Join the #django channel on irc.freenode.net. Lots of helpful people
      hang out there. Read the archives at http://botland.oebfare.com/logger/django/.

    * Join the django-users mailing list, or read the archives, at
      http://groups.google.com/group/django-users.

To contribute to Django:

    * Check out http://www.djangoproject.com/community/ for information
      about getting involved.

To run Django's test suite:

    * Follow the instructions in the "Unit tests" section of
      docs/internals/contributing.txt, published online at
      https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests

This directory contains extra stuff that can improve your Django experience.
This repository contains a python implementation of the Google commandline
flags module.

 GFlags defines a *distributed* command line system, replacing systems like
 getopt(), optparse and manual argument processing. Rather than an application
 having to define all flags in or near main(), each python module defines flags
 that are useful to it.  When one python module imports another, it gains
 access to the other's flags.

 It includes the ability to define flag types (boolean, float, interger, list),
 autogeneration of help (in both human and machine readable format) and reading
 arguments from a file. It also includes the ability to automatically generate
 man pages from the help flags.

Documentation for implementation is at the top of gflags.py file.

To install the python module, run
   python ./setup.py install

When you install this library, you also get a helper application,
gflags2man.py, installed into /usr/local/bin.  You can run gflags2man.py to
create an instant man page, with all the commandline flags and their docs, for
any C++ or python program you've written using the gflags library.
The list of files here isn't complete.  For a step-by-step guide on
how to set this package up correctly, check out
    http://www.debian.org/doc/maint-guide/

Most of the files that are in this directory are boilerplate.
However, you may need to change the list of binary-arch dependencies
in 'rules'.
Flask Sphinx Styles
===================

This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

1. put this folder as _themes into your docs folder.  Alternatively
   you can also use git submodules to check out the contents there.
2. add this to your conf.py:

   sys.path.append(os.path.abspath('_themes'))
   html_theme_path = ['_themes']
   html_theme = 'flask'

The following themes exist:

- 'flask' - the standard flask documentation theme for large
  projects
- 'flask_small' - small one-page theme.  Intended to be used by
  very small addon libraries for flask.

The following options exist for the flask_small theme:

   [options]
   index_logo = ''              filename of a picture in _static
                                to be used as replacement for the
                                h1 in the index.rst file.
   index_logo_height = 120px    height of the index logo
   github_fork = ''             repository name on github for the
                                "fork me" badge
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "docs" directory and online at
https://docs.djangoproject.com/en/stable/. If you're just getting started,
here's how we recommend you read the docs:

* First, read docs/intro/install.txt for instructions on installing Django.

* Next, work through the tutorials in order (docs/intro/tutorial01.txt,
  docs/intro/tutorial02.txt, etc.).

* If you want to set up an actual deployment server, read
  docs/howto/deployment/index.txt for instructions.

* You'll probably want to read through the topical guides (in docs/topics)
  next; from there you can jump to the HOWTOs (in docs/howto) for specific
  problems, and check out the reference (docs/ref) for gory details.

* See docs/README for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think
they should be clarified in any way, please take 30 seconds to fill out a
ticket here: https://code.djangoproject.com/newticket

To get more help:

* Join the #django channel on irc.freenode.net. Lots of helpful people hang out
  there. Read the archives at http://django-irc-logs.com/.

* Join the django-users mailing list, or read the archives, at
  https://groups.google.com/group/django-users.

To contribute to Django:

* Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for
  information about getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  docs/internals/contributing/writing-code/unit-tests.txt, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests
This directory contains extra stuff that can improve your Django experience.
All icons are taken from Font Awesome (http://fontawesome.io/) project.
The Font Awesome font is licensed under the SIL OFL 1.1:
- http://scripts.sil.org/OFL

SVG icons source: https://github.com/encharm/Font-Awesome-SVG-PNG
Font-Awesome-SVG-PNG is licensed under the MIT license (see file license
in current folder).
Roboto webfont source: https://www.google.com/fonts/specimen/Roboto
Weights used in this project: Light (300), Regular (400), Bold (700)
ipaddr.py is a library for working with IP addresses, both IPv4 and IPv6.
It was developed by Google for internal use, and is now open source.

Project home page: https://github.com/google/ipaddr-py

Please send contributions to ipaddr-py-dev@googlegroups.com.  Code should
include unit tests and follow the Google Python style guide:
http://code.google.com/p/soc/wiki/PythonStyleGuide
MarkupSafe
==========

Implements a unicode subclass that supports HTML strings:

>>> from markupsafe import Markup, escape
>>> escape("<script>alert(document.cookie);</script>")
Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')
>>> tmpl = Markup("<em>%s</em>")
>>> tmpl % "Peter > Lustig"
Markup(u'<em>Peter &gt; Lustig</em>')

If you want to make an object unicode that is not yet unicode
but don't want to lose the taint information, you can use the
`soft_unicode` function.  (On Python 3 you can also use `soft_str` which
is a different name for the same function).

>>> from markupsafe import soft_unicode
>>> soft_unicode(42)
u'42'
>>> soft_unicode(Markup('foo'))
Markup(u'foo')

HTML Representations
--------------------

Objects can customize their HTML markup equivalent by overriding
the `__html__` function:

>>> class Foo(object):
...  def __html__(self):
...   return '<strong>Nice</strong>'
...
>>> escape(Foo())
Markup(u'<strong>Nice</strong>')
>>> Markup(Foo())
Markup(u'<strong>Nice</strong>')

Silent Escapes
--------------

Since MarkupSafe 0.10 there is now also a separate escape function
called `escape_silent` that returns an empty string for `None` for
consistency with other systems that return empty strings for `None`
when escaping (for instance Pylons' webhelpers).

If you also want to use this for the escape method of the Markup
object, you can create your own subclass that does that::

    from markupsafe import Markup, escape_silent as escape

    class SilentMarkup(Markup):
        __slots__ = ()

        @classmethod
        def escape(cls, s):
            return cls(escape(s))

New-Style String Formatting
---------------------------

Starting with MarkupSafe 0.21 new style string formats from Python 2.6 and
3.x are now fully supported.  Previously the escape behavior of those
functions was spotty at best.  The new implementations operates under the
following algorithm:

1.  if an object has an ``__html_format__`` method it is called as
    replacement for ``__format__`` with the format specifier.  It either
    has to return a string or markup object.
2.  if an object has an ``__html__`` method it is called.
3.  otherwise the default format system of Python kicks in and the result
    is HTML escaped.

Here is how you can implement your own formatting::

    class User(object):

        def __init__(self, id, username):
            self.id = id
            self.username = username

        def __html_format__(self, format_spec):
            if format_spec == 'link':
                return Markup('<a href="/user/{0}">{1}</a>').format(
                    self.id,
                    self.__html__(),
                )
            elif format_spec:
                raise ValueError('Invalid format spec')
            return self.__html__()

        def __html__(self):
            return Markup('<span class=user>{0}</span>').format(self.username)

And to format that user:

>>> user = User(1, 'foo')
>>> Markup('<p>User: {0:link}').format(user)
Markup(u'<p>User: <a href="/user/1"><span class=user>foo</span></a>')
This is python client library for Google's discovery based APIs.


Installation
============

To install, simply say

   $ easy_install --upgrade google-api-python-client


Running
=======

After following the install directions (using setup.py or setpath.sh) you
should be able to cd to samples/plus and run plus.py from there, which will use
the apiclient library to retrieve a snippet of text from each entry in Google
Plus. The first time you run it you will be prompted to authorize the
application to access your plus information.

   $ python samples/plus/plus.py


Third Party Libraries
=====================

These libraries will be installed when you install the client library:

http://code.google.com/p/httplib2
http://code.google.com/p/uri-templates
http://code.google.com/p/python-gflags
http://github.com/simplegeo/python-oauth2

Depending on your version of Python, these libraries may also be installed:

http://pypi.python.org/pypi/simplejson/

For development you will also need:

http://pythonpaste.org/webtest/
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

All documentation is in the "docs" directory and online at
http://docs.djangoproject.com/en/dev/. If you're just getting started, here's
how we recommend you read the docs:

    * First, read docs/intro/install.txt for instructions on installing Django.

    * Next, work through the tutorials in order (docs/intro/tutorial01.txt,
      docs/intro/tutorial02.txt, etc.).

    * If you want to set up an actual deployment server, read
      docs/howto/deployment/index.txt for instructions.

    * You'll probably want to read through the topical guides (in docs/topics)
      next; from there you can jump to the HOWTOs (in docs/howto) for specific
      problems, and check out the reference (docs/ref) for gory details.

    * See docs/README for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think they
should be clarified in any way, please take 30 seconds to fill out a ticket
here:

http://code.djangoproject.com/newticket

To get more help:

    * Join the #django channel on irc.freenode.net. Lots of helpful people
      hang out there. Read the archives at http://django-irc-logs.com/.

    * Join the django-users mailing list, or read the archives, at
      http://groups.google.com/group/django-users.

To contribute to Django:

    * Check out http://www.djangoproject.com/community/ for information
      about getting involved.

To run Django's test suite:

    * Follow the instructions in the "Unit tests" section of
      docs/internals/contributing/writing-code/unit-tests.txt, published online at
      https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests
This directory contains extra stuff that can improve your Django experience.
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "``docs``" directory and online at
https://docs.djangoproject.com/en/stable/. If you're just getting started,
here's how we recommend you read the docs:

* First, read ``docs/intro/install.txt`` for instructions on installing Django.

* Next, work through the tutorials in order (``docs/intro/tutorial01.txt``,
  ``docs/intro/tutorial02.txt``, etc.).

* If you want to set up an actual deployment server, read
  ``docs/howto/deployment/index.txt`` for instructions.

* You'll probably want to read through the topical guides (in ``docs/topics``)
  next; from there you can jump to the HOWTOs (in ``docs/howto``) for specific
  problems, and check out the reference (``docs/ref``) for gory details.

* See ``docs/README`` for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think
they should be clarified in any way, please take 30 seconds to fill out a
ticket here: https://code.djangoproject.com/newticket

To get more help:

* Join the ``#django`` channel on irc.freenode.net. Lots of helpful people hang out
  there. Read the archives at http://django-irc-logs.com/.

* Join the django-users mailing list, or read the archives, at
  https://groups.google.com/group/django-users.

To contribute to Django:

* Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for
  information about getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  ``docs/internals/contributing/writing-code/unit-tests.txt``, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests
This directory contains extra stuff that can improve your Django experience.
All icons are taken from Font Awesome (http://fontawesome.io/) project.
The Font Awesome font is licensed under the SIL OFL 1.1:
- http://scripts.sil.org/OFL

SVG icons source: https://github.com/encharm/Font-Awesome-SVG-PNG
Font-Awesome-SVG-PNG is licensed under the MIT license (see file license
in current folder).
Roboto webfont source: https://www.google.com/fonts/specimen/Roboto
Weights used in this project: Light (300), Regular (400), Bold (700)
MarkupSafe
==========

Implements a unicode subclass that supports HTML strings:

>>> from markupsafe import Markup, escape
>>> escape("<script>alert(document.cookie);</script>")
Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')
>>> tmpl = Markup("<em>%s</em>")
>>> tmpl % "Peter > Lustig"
Markup(u'<em>Peter &gt; Lustig</em>')

If you want to make an object unicode that is not yet unicode
but don't want to lose the taint information, you can use the
`soft_unicode` function:

>>> from markupsafe import soft_unicode
>>> soft_unicode(42)
u'42'
>>> soft_unicode(Markup('foo'))
Markup(u'foo')

Objects can customize their HTML markup equivalent by overriding
the `__html__` function:

>>> class Foo(object):
...  def __html__(self):
...   return '<strong>Nice</strong>'
...
>>> escape(Foo())
Markup(u'<strong>Nice</strong>')
>>> Markup(Foo())
Markup(u'<strong>Nice</strong>')

Since MarkupSafe 0.10 there is now also a separate escape function
called `escape_silent` that returns an empty string for `None` for
consistency with other systems that return empty strings for `None`
when escaping (for instance Pylons' webhelpers).

If you also want to use this for the escape method of the Markup
object, you can create your own subclass that does that::

    from markupsafe import Markup, escape_silent as escape

    class SilentMarkup(Markup):
        __slots__ = ()

        @classmethod
        def escape(cls, s):
            return cls(escape(s))
The argparse module makes it easy to write user friendly command line
interfaces.

The program defines what arguments it requires, and argparse will figure out
how to parse those out of sys.argv. The argparse module also automatically
generates help and usage messages and issues errors when users give the
program invalid arguments.

As of Python >= 2.7 and >= 3.2, the argparse module is maintained within the
Python standard library. For users who still need to support Python < 2.7 or
< 3.2, it is also provided as a separate package, which tries to stay
compatible with the module in the standard library, but also supports older
Python versions.

argparse is licensed under the Python license, for details see LICENSE.txt.


Compatibility
-------------

argparse should work on Python >= 2.3, it was tested on:

* 2.3.5, 2.4.4, 2.5.5, 2.6.5 and 2.7
* 3.1, 3.2


Installation
------------

Try one of these:

    python setup.py install

    easy_install argparse

    pip install argparse

    putting argparse.py in some directory listed in sys.path should also work


Bugs
----

If you find a bug, please try to reproduce it with python 2.7.

If it happens there also, please file a bug in the python.org issue tracker.
If it does not happen in 2.7, file a bug in the argparse package issue tracker.

The [Grizzled Python Utility Library][] is a general-purpose Python library
with a variety of different modules and packages. It's roughly organized
into subpackages that group different kinds of utility functions and
classes.

Grizzled is copyright &copy; 2008-2010 by Brian M. Clapper and is released
under a BSD license.

[Grizzled Python Utility Library]: http://software.clapper.org/grizzled-python/
The tests in this directory are intended to be run via Nose.
Requests: HTTP for Humans
=========================

.. image:: https://img.shields.io/pypi/v/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://img.shields.io/pypi/dm/requests.svg
        :target: https://pypi.python.org/pypi/requests

Requests is the only *Non-GMO* HTTP library for Python, safe for human
consumption.

**Warning:** Recreational use of other HTTP libraries may result in dangerous side-effects,
including: security vulnerabilities, verbose code, reinventing the wheel,
constantly reading documentation, depression, headaches, or even death.

Behold, the power of Requests:

.. code-block:: python

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'disk_usage': 368627, u'private_gists': 484, ...}

See `the similar code, sans Requests <https://gist.github.com/973705>`_.

Requests allows you to send *organic, grass-fed* HTTP/1.1 requests, without the
need for manual labor. There's no need to manually add query strings to your
URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling
are 100% automatic, powered by `urllib3 <https://github.com/shazow/urllib3>`_,
which is embedded within Requests.

Besides, all the cool kids are doing it. Requests is one of the most
downloaded Python packages of all time, pulling in over 7,000,000 downloads
every month. You don't want to be left out!

Feature Support
---------------

Requests is ready for today's web.

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Sessions with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Automatic Content Decoding
- Unicode Response Bodies
- Multipart File Uploads
- HTTP(S) Proxy Support
- Connection Timeouts
- Streaming Downloads
- ``.netrc`` Support
- Chunked Requests
- Thread-safety

Requests supports Python 2.6 — 3.5, and runs great on PyPy.

Installation
------------

To install Requests, simply:

.. code-block:: bash

    $ pip install requests
    ✨🍰✨

Satisfaction, guaranteed.

Documentation
-------------

Fantastic documentation is available at http://docs.python-requests.org/, for a limited time only.


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a `Contributor Friendly`_ tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/kennethreitz/requests
.. _AUTHORS: https://github.com/kennethreitz/requests/blob/master/AUTHORS.rst
.. _Contributor Friendly: https://github.com/kennethreitz/requests/issues?direction=desc&labels=Contributor+Friendly&page=1&sort=updated&state=open
1) ABOUT
========

This is the Python package 'antlr3', which is required to use parsers created
by the ANTLR3 tool. See <http://www.antlr.org/> for more information about
ANTLR3.


2) STATUS
=========

The Python target for ANTLR3 is still in beta. Documentation is lacking, some
bits of the code is not yet done, some functionality has not been tested yet.
Also the API might change a bit - it currently mimics the Java implementation,
but it may be made a bit more pythonic here and there.

WARNING: Currently the runtime library for V3.1 is not compatible with
recognizers generated by ANTLR V3.0.x. If you are an application developer,
then the suggested way to solve this is to package the correct runtime with
your application. Installing the runtime in the global site-packages directory
may not be a good idea.
It is still undetermined, if a future release of the V3.1 runtime will be
compatible with V3.0.x recognizers or if future runtimes V3.2+ will be
compatible with V3.1 recognizers.
Sorry for the inconvenience.


3) DOWNLOAD
===========

This runtime is part of the ANTLR distribution. The latest version can be found
at <http://www.antlr.org/download.html>.

If you are interested in the latest, most bleeding edge version, have a look at
the perforce depot at <http://fisheye2.cenqua.com/browse/antlr>. There are
tarballs ready to download, so you don't have to install the perforce client.


4) INSTALLATION
===============

Just like any other Python package:
$ python setup.py install

See <http://docs.python.org/inst/> for more information.


5) DOCUMENTATION
================

Documentation (as far as it exists) can be found in the wiki
<http://www.antlr.org/wiki/display/ANTLR3/Antlr3PythonTarget>


6) REPORTING BUGS
=================

Please send bug reports to the ANTLR mailing list 
<http://www.antlr.org:8080/mailman/listinfo/antlr-interest> or
<pink@odahoda.de>.

Existing bugs may appear someday in the bugtracker:
<http://www.antlr.org:8888/browse/ANTLR>


7) HACKING
==========

Only the runtime package can be found here. There are also some StringTemplate
files in 'src/org/antlr/codegen/templates/Python/' and some Java code in
'src/org/antlr/codegen/PythonTarget.java' (of the main ANTLR3 source
distribution).

If there are no directories 'tests' and 'unittests' in 'runtime/Python', you
should fetch the latest ANTLR3 version from the perforce depot. See section
DOWNLOAD.
You'll need java and ant in order to compile and use the tool.
Be sure to properly setup your CLASSPATH.
(FIXME: is there some generic information, how to build it yourself? I should
point to it to avoid duplication.)

You can then use the commands
$ python setup.py unittest
$ python setup.py functest
to ensure that changes do not break existing behaviour.

Please send patches to <pink@odahoda.de>. For larger code contributions you'll
have to sign the "Developer's Certificate of Origin", which can be found on
<http://www.antlr.org/license.html> or use the feedback form at
<http://www.antlr.org/misc/feedback>.
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

All documentation is in the "docs" directory and online at
http://docs.djangoproject.com/en/dev/. If you're just getting started, here's
how we recommend you read the docs:

    * First, read docs/intro/install.txt for instructions on installing Django.

    * Next, work through the tutorials in order (docs/intro/tutorial01.txt,
      docs/intro/tutorial02.txt, etc.).

    * If you want to set up an actual deployment server, read
      docs/howto/deployment/index.txt for instructions.

    * You'll probably want to read through the topical guides (in docs/topics)
      next; from there you can jump to the HOWTOs (in docs/howto) for specific
      problems, and check out the reference (docs/ref) for gory details.

Docs are updated rigorously. If you find any problems in the docs, or think they
should be clarified in any way, please take 30 seconds to fill out a ticket
here:

http://code.djangoproject.com/newticket

To get more help:

    * Join the #django channel on irc.freenode.net. Lots of helpful people
      hang out there. Read the archives at http://botland.oebfare.com/logger/django/.

    * Join the django-users mailing list, or read the archives, at
      http://groups.google.com/group/django-users.

To contribute to Django:

    * Check out http://www.djangoproject.com/community/ for information
      about getting involved.

To run Django's test suite:

    * Follow the instructions in the "Unit tests" section of
      docs/internals/contributing.txt, published online at
      http://docs.djangoproject.com/en/dev/internals/contributing/#running-the-unit-tests
This directory contains extra stuff that can improve your Django experience.
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "docs" directory and online at
http://docs.djangoproject.com/en/dev/. If you're just getting started, here's
how we recommend you read the docs:

* First, read docs/intro/install.txt for instructions on installing Django.

* Next, work through the tutorials in order (docs/intro/tutorial01.txt,
  docs/intro/tutorial02.txt, etc.).

* If you want to set up an actual deployment server, read
  docs/howto/deployment/index.txt for instructions.

* You'll probably want to read through the topical guides (in docs/topics)
  next; from there you can jump to the HOWTOs (in docs/howto) for specific
  problems, and check out the reference (docs/ref) for gory details.

* See docs/README for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think they
should be clarified in any way, please take 30 seconds to fill out a ticket
here:

http://code.djangoproject.com/newticket

To get more help:

* Join the #django channel on irc.freenode.net. Lots of helpful people hang out
  there. Read the archives at http://django-irc-logs.com/.

* Join the django-users mailing list, or read the archives, at
  http://groups.google.com/group/django-users.

To contribute to Django:

* Check out http://www.djangoproject.com/community/ for information about
  getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  docs/internals/contributing/writing-code/unit-tests.txt, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests
This directory contains extra stuff that can improve your Django experience.
PyYAML - The next generation YAML parser and emitter for Python.

To install, type 'python setup.py install'.

You may build faster LibYAML based parser and emitter with
'python setup_with_libyaml.py install'.
Then you may use the LibYAML based parser this way:
    >>> yaml.load(stream, Loader=yaml.CLoader)
    >>> yaml.dump(data, Dumper=yaml.CDumper)

For more information, check the PyYAML homepage:
'http://pyyaml.org/wiki/PyYAML'.

Documentation (rough and incomplete though):
'http://pyyaml.org/wiki/PyYAMLDocumentation'.

Post your questions and opinions to the YAML-Core mailing list:
'http://lists.sourceforge.net/lists/listinfo/yaml-core'.

Submit bug reports and feature requests to the PyYAML bug tracker:
'http://pyyaml.org/newticket?component=pyyaml'.

PyYAML is written by Kirill Simonov <xi@resolvent.net>.  It is released
under the MIT license. See the file LICENSE for more details.
# sqlcmd: A SQL command interpreter

This is _sqlcmd_, a SQL command interpreter. See the [User's Guide][] for
complete details.

**NOTICE: I no longer maintain _sqlcmd_. It has been superceded by my 
Scala-based [sqlshell][] tool.**

[sqlshell]: http://bmc.github.com/sqlshell/

To install _sqlcmd_ in the default location, type:

    python setup.py install

To install it somewhere else, such as your home directory, type:

    python setup.py install --prefix=$HOME

[User's Guide]: https://github.com/bmc/sqlcmd/blob/master/doc/users_guide.rst
This directory contains the Distutils package.

There's a full documentation available at:

    http://docs.python.org/distutils/

The Distutils-SIG web page is also a good starting point:

    http://www.python.org/sigs/distutils-sig/

WARNING : Distutils must remain compatible with 2.3

$Id$
The httplib2 code in this directory was integrated from the httplib2 code in
//third_party/py/httplib2.

Local modifications from the original //third_party/py/httplib2 code that have
been maintained:
1. Added httplib2_test.py for minimal validation.
2. Use only the python2/httplib2 subdirectory from github.

Local modifications on top of the //third_party/py/httplib2 code:
1. socks.py from the original commit is included. Comparatively,
//third_party/py/httplib2 uses //third_party/py/socks.
2. Passing the HTTPS host into the _ssl_wrap_socket method (as in cl/152201465).
docker-py
=========

[![Build Status](https://travis-ci.org/docker/docker-py.png)](https://travis-ci.org/docker/docker-py)

An API client for docker written in Python

Installation
------------

Our latest stable is always available on PyPi.

    pip install docker-py

Documentation
------------

[![Documentation Status](https://readthedocs.org/projects/docker-py/badge/?version=latest)](https://readthedocs.org/projects/docker-py/?badge=latest)

Full documentation is hosted on [ReadTheDocs](http://docker-py.readthedocs.org/en/latest/). 
Sources are available in the `docs/` directory.


License
-------
Docker is licensed under the Apache License, Version 2.0. See LICENSE for full license text
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

All documentation is in the "docs" directory and online at
http://www.djangoproject.com/documentation/.  If you're just getting started,
here's how we recommend you read the docs:

    * First, read docs/install.txt for instructions on installing Django.

    * Next, work through the tutorials in order (docs/tutorial01.txt,
      docs/tutorial02.txt, etc.).

    * If you want to set up an actual deployment server, read docs/modpython.txt
      for instructions on running Django under mod_python.

    * The rest of the documentation is of the reference-manual variety.
      Read it -- and the FAQ -- as you run into problems.

Docs are updated rigorously. If you find any problems in the docs, or think they
should be clarified in any way, please take 30 seconds to fill out a ticket
here:

http://code.djangoproject.com/newticket

To get more help:

    * Join the #django channel on irc.freenode.net. Lots of helpful people
      hang out there. Read the archives at http://simon.bofh.ms/logger/django/ .

    * Join the django-users mailing list, or read the archives, at
      http://groups.google.com/group/django-users.

To contribute to Django:

    * Check out http://www.djangoproject.com/community/ for information
      about getting involved.

=================
websocket-client
=================

websocket-client module  is WebSocket client for python. This provide the low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

License
============

 - LGPL

Installation
=============

This module is tested on only Python 2.7.

Type "python setup.py install" or "pip install websocket-client" to install.

This module does not depend on any other module.

How about Python 3
===========================

py3( https://github.com/liris/websocket-client/tree/py3 ) branch is for python 3.3. Every test case is passed.
If you are using python3, please check it.

Example
============

Low Level API example::

    from websocket import create_connection
    ws = create_connection("ws://echo.websocket.org/")
    print "Sending 'Hello, World'..."
    ws.send("Hello, World")
    print "Sent"
    print "Reeiving..."
    result =  ws.recv()
    print "Received '%s'" % result
    ws.close()

If you want to customize socket options, set sockopt.

sockopt example:

    from websocket import create_connection
    ws = create_connection("ws://echo.websocket.org/".
                            sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY),) )


JavaScript websocket-like API example::

  import websocket
  import thread
  import time
  
  def on_message(ws, message):
      print message
  
  def on_error(ws, error):
      print error
  
  def on_close(ws):
      print "### closed ###"
  
  def on_open(ws):
      def run(*args):
          for i in range(3):
              time.sleep(1)
              ws.send("Hello %d" % i)
          time.sleep(1)
          ws.close()
          print "thread terminating..."
      thread.start_new_thread(run, ())
  
  
  if __name__ == "__main__":
      websocket.enableTrace(True)
      ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                                  on_message = on_message,
                                  on_error = on_error,
                                  on_close = on_close)
      ws.on_open = on_open
      
      ws.run_forever()


wsdump.py
============

wsdump.py is simple WebSocket test(debug) tool.

sample for echo.websocket.org::

  $ wsdump.py ws://echo.websocket.org/
  Press Ctrl+C to quit
  > Hello, WebSocket
  < Hello, WebSocket
  > How are you?
  < How are you?

Usage
---------

usage::
  wsdump.py [-h] [-v [VERBOSE]] ws_url

WebSocket Simple Dump Tool

positional arguments:
  ws_url                websocket url. ex. ws://echo.websocket.org/

optional arguments:
  -h, --help                           show this help message and exit

  -v VERBOSE, --verbose VERBOSE    set verbose mode. If set to 1, show opcode. If set to 2, enable to trace websocket module

example::

  $ wsdump.py ws://echo.websocket.org/
  $ wsdump.py ws://echo.websocket.org/ -v
  $ wsdump.py ws://echo.websocket.org/ -vv

ChangeLog
============

- v0.9.0

  - allow to set opcode in WebSocketApp.send(ISSUE#25)
  - allow to modify Origin(ISSUE#26)

- v0.8.0

  - many bug fix
  - some performance improvement

- v0.7.0

  - fixed problem to read long data.(ISSUE#12)
  - fix buffer size boundary violation

- v0.6.0

  - Patches: UUID4, self.keep_running, mask_key (ISSUE#11)
  - add wsdump.py tool 

- v0.5.2

  - fix Echo App Demo Throw Error: 'NoneType' object has no attribute 'opcode  (ISSUE#10)

- v0.5.1

  - delete invalid print statement.

- v0.5.0

  - support hybi-13 protocol.

- v0.4.1

  - fix incorrect custom header order(ISSUE#1)
   
