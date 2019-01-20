This is a export of the marketplace app data on:

    {{ date }}

For the site:

    {{ url }}

For more information on the contents, consult the API documentation:

    http://firefox-marketplace-api.readthedocs.org/en/latest/
This is an export of the marketplace user install data on:

    {{ date }}

For the site:

    {{ url }}
===================
Welcome to /locale/
===================



To Localizers:
--------------

The two files in your locale directories that are important are::

    django.po
    djangojs.po

Generally, legal documents are localized by lawyers and aren't in our gettext
process.  However, if you need to work with them, visit::

    https://github.com/mozilla/legal-docs

Also please make sure you're reading dev-l10n-web@lists.mozilla.org.  Thanks!



To Developers:
--------------
Run the omg_new_l10n.sh script from your project root.  You should definitely
read that script to make sure you meet all of its expectations 'cause it makes
assumptions and doesn't have much error checking.

Ask clouserw if there are any questions.
This is a fake language used for debugging the site.  Files generated with
podebug.  Ask clouserw for help.
This is a fake language used for debugging the site.  Files generated with
podebug.  Ask clouserw for help.
Sprite folders for creating sprites using Glue:
https://github.com/jorgebastida/glue

For example:
$ glue mkt-reviewer-icons mkt-reviewer-icons --less -crop

Then `mv` the file into place and edit the LESS using the Glue output as a
guide for the offsets.
When adding something, don't forget the .css file, and do add it to settings.py!
=====================
Zamboni Documentation
=====================

Within: documentation for the use of Zamboni and its services. All this
documentation here is contained in plain text files using
`reStructuredText <http://docutils.sourceforge.net/rst.html>`_ and
`Sphinx <http://sphinx-doc.org/>`_.

To install Sphinx and its dependencies (including Sphinx plugins and the MDN
documentation theme), activate your virtualenv and run ``pip install -r 
requirements/docs.txt``.

A daemon is included that can watch and regenerated the built HTML when
documentation source files are changed:
``python watcher.py 'make html' $(find . -name '*.rst')``.

There are two distinct documentation trees contained within this directory:


Zamboni
-------

Viewable at:
  http://zamboni.readthedocs.org/
Covers:
  Development using Zamboni, the source code for
  `Add-ons <https://addons.mozilla.org/>`_ and
  `Marketplace <http://marketplace.firefox.com/>`_.
Source location:
  `/docs <https://github.com/mozilla/zamboni/tree/master/docs>`_
Build by:
  Running ``make html`` from ``/docs``. The generated documentation will be
  located at ``/docs/_build/html``.


Marketplace API
---------------

Viewable at:
  http://firefox-marketplace-api.readthedocs.org/
Covers:
  Consumption of the Marketplace API.
Source location:
  `/docs/api`` <https://github.com/mozilla/zamboni/tree/master/docs/api>`_
Build by:
  Running ``make htmlapi`` from ``/docs``. The generated documentation will be
  located at ``/docs/api/_build/html``.
