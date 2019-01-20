demo_geomapfish project
===================

Read the `Documentation <http://docs.camptocamp.net/c2cgeoportal/>`_

Checkout
--------

.. code:: bash

   git clone git@github.com:camptocamp/demo_geomapfish.git

Build
-----

.. code:: bash

  cd demo_geomapfish

  make -f <user>.mk build

.. Feel free to add project-specific things.
Directives and their partials are structured by components

A subdirectory is created for each component.
The component partials are directly stored in the subdirectory.

The partials are loaded individually at runtime in debug mode but preloaded in a template cache for production.
For this mechanism to work correctly the directive template URL must follow some conventions:

In the directive, the template url is written as follow: "templateUrl: demo.baseTemplateUrl + '/<component>/<partial>.html'".

In the main html file, the debug section should contain "demo.baseTemplateUrl = '${request.static_url("demo:static-ngeo/components")}';"
add the following to your Apache config:

Include ${directory}/apache/*.conf
