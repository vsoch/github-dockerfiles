Dockerfile for Base Container for Travis CI
===========================================

This is a basic container that was built upon the centos 6 container. It
includes jetty-runner and yum core libraries needed to build exchange in
Travis.


Installation
-------------

.. code-block:: bash

   cd exchange
   docker build -t boundlessgeo/ci-exchange-el6:2.1.0b2 -f docker/travis/dockerhub/Dockerfile .
   docker push boundlessgeo/ci-exchange-el6:2.1.0b2
