demo_geomapfish project
===================

Read the `Documentation <https://camptocamp.github.io/c2cgeoportal/2.4/>`_

Checkout
--------

.. code::

   git clone git@github.com:camptocamp/demo_geomapfish.git

   cd demo_geomapfish

Build
-----

.. code::

  ./docker-run make --makefile=<user.mk> build

If you want to work on your own instance, create a ${USER}.mk file like that:

.. script::

  INSTANCE=myUserName
  include Makefile

Run
---

.. code::

   docker-compose up

If the project is configured with a global front (for being able the run more than one instance at the same
time:

.. script::

  (cd global-front; docker-compose -p global up --build)

.. Feel free to add project-specific things.