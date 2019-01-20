This compiled version of SlickGrid has been obtained with the Google Closure
Compiler, using the following command:

java -jar compiler.jar --js=slick.core.js --js=slick.grid.js --js=slick.editors.js --js_output_file=slick.grid.min.js

There are two other files required for the SlickGrid view to work properly:

 * jquery-ui-1.8.16.custom.min.js 
 * jquery.event.drag-2.0.min.js

These are included in the Recline source, but have not been included in the
built file to make easier to handle compatibility problems.

Please check SlickGrid license in the included MIT-LICENSE.txt file.

[1] https://developers.google.com/closure/compiler/
This compiled version of SlickGrid has been obtained with the Google Closure
Compiler, using the following command:

java -jar compiler.jar --js=slick.core.js --js=slick.grid.js --js_output_file=slick.grid.min.js

There are two other files required for the SlickGrid view to work properly:

 * jquery-ui-1.8.16.custom.min.js 
 * jquery.event.drag-2.0.min.js

These are included in the Recline source, but have not been included in the
built file to make easier to handle compatibility problems.

Please check SlickGrid license in the included MIT-LICENSE.txt file.

[1] https://developers.google.com/closure/compiler/
Select2
=======

Select2 is a jQuery-based replacement for select boxes. It supports searching, remote data sets, and infinite scrolling of results.

To get started, checkout examples and documentation at http://ivaynberg.github.com/select2

Use cases
---------

* Enhancing native selects with search.
* Enhancing native selects with a better multi-select interface.
* Loading data from JavaScript: easily load items via ajax and have them searchable.
* Nesting optgroups: native selects only support one level of nested. Select2 does not have this restriction.
* Tagging: ability to add new items on the fly.
* Working with large, remote datasets: ability to partially load a dataset based on the search term.
* Paging of large datasets: easy support for loading more pages when the results are scrolled to the end.
* Templating: support for custom rendering of results and selections.

Browser compatibility
---------------------
* IE 8+
* Chrome 8+
* Firefox 10+
* Safari 3+
* Opera 10.6+
 
Usage
-----
You can source Select2 directly from a [CDN like JSDliver](http://www.jsdelivr.com/#!select2), [download it from this GitHub repo](https://github.com/ivaynberg/select2/tags), or use one of the integrations below.

Integrations
------------

* [Wicket-Select2](https://github.com/ivaynberg/wicket-select2) (Java / [Apache Wicket](http://wicket.apache.org))
* [select2-rails](https://github.com/argerim/select2-rails) (Ruby on Rails)
* [AngularUI](http://angular-ui.github.com/#directives-select2) ([AngularJS](angularjs.org))
* [Django](https://github.com/applegrew/django-select2)
* [Symfony](https://github.com/19Gerhard85/sfSelect2WidgetsPlugin)
* [Symfony2](https://github.com/avocode/FormExtensions)
* [Bootstrap 2](https://github.com/t0m/select2-bootstrap-css) and [Bootstrap 3](https://github.com/t0m/select2-bootstrap-css/tree/bootstrap3) (CSS skins)
* [Meteor](https://github.com/nate-strauser/meteor-select2) (modern reactive JavaScript framework; + [Bootstrap 3 skin](https://github.com/esperadomedia/meteor-select2-bootstrap3-css/))
* [Yii 2.x](http://demos.krajee.com/widgets#select2)
* [Yii 1.x](https://github.com/tonybolzan/yii-select2)

Internationalization (i18n)
---------------------------

Select2 supports multiple languages by simply including the right
language JS file (`select2_locale_it.js`, `select2_locale_nl.js`, etc.).

Missing a language? Just copy `select2_locale_en.js.template`, translate
it, and make a pull request back to Select2 here on GitHub.

Bug tracker
-----------

Have a bug? Please create an issue here on GitHub!

https://github.com/ivaynberg/select2/issues

Mailing list
------------

Have a question? Ask on our mailing list!

select2@googlegroups.com

https://groups.google.com/d/forum/select2


Copyright and license
---------------------

Copyright 2012 Igor Vaynberg

This software is licensed under the Apache License, Version 2.0 (the "Apache License") or the GNU
General Public License version 2 (the "GPL License"). You may choose either license to govern your
use of this software only upon the condition that you accept all of the terms of either the Apache
License or the GPL License.

You may obtain a copy of the Apache License and the GPL License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0
http://www.gnu.org/licenses/gpl-2.0.html

Unless required by applicable law or agreed to in writing, software distributed under the Apache License
or the GPL License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the Apache License and the GPL License for the specific language governing
permissions and limitations under the Apache License and the GPL License.
rjsmin.py
is taken from the rjsmin project and licensed under Apache License, Version 2
http://opensource.perlig.de/rjsmin/

# Copyright 2011, 2012
# Andr\xe9 Malo or his licensors, as applicable
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

rcssmin.py
is taken from the rcssmin project and licensed under Apache License, Version 2
http://opensource.perlig.de/rcssmin/

# Copyright 2011, 2012
# Andr\xe9 Malo or his licensors, as applicable
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
CKAN Solr schema
================

This folder contains the Solr schema file used by CKAN (schema.xml).

Starting from 2.2 this is the only file that should be used by users and
modified by devs. The rest of files (schema-{version}.xml) are kept for
backwards compatibility purposes and should not be used, as they might be
removed in future versions.

When upgrading CKAN, always check the CHANGELOG on each release to see if
you need to update the schema file and reindex your datasets.
.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/{{ github_user_name }}/{{ project }}.svg?branch=master
    :target: https://travis-ci.org/{{ github_user_name }}/{{ project }}

.. image:: https://coveralls.io/repos/{{ github_user_name }}/{{ project }}/badge.png?branch=master
  :target: https://coveralls.io/r/{{ github_user_name }}/{{ project }}?branch=master

.. image:: https://pypip.in/download/{{ project }}/badge.svg
    :target: https://pypi.python.org/pypi//{{ project }}/
    :alt: Downloads

.. image:: https://pypip.in/version/{{ project }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ project }}/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/{{ project }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ project }}/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/{{ project }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ project }}/
    :alt: Development Status

.. image:: https://pypip.in/license/{{ project }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ project }}/
    :alt: License

=============
{{ project }}
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

For example, you might want to mention here which versions of CKAN this
extension works with.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install {{ project }}:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the {{ project }} Python package into your virtual environment::

     pip install {{ project }}

3. Add ``{{ project_shortname }}`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.{{ project_shortname }}.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install {{ project }} for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/{{ github_user_name }}/{{ project }}.git
    cd {{ project }}
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.{{ project_shortname }} --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering {{ project }} on PyPI
---------------------------------

{{ project }} should be availabe on PyPI as
https://pypi.python.org/pypi/{{ project }}. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of {{ project }}
----------------------------------------

{{ project }} is availabe on PyPI as https://pypi.python.org/pypi/{{ project }}.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags

This is a database migration repository.

More information at
http://code.google.com/p/sqlalchemy-migrate/
