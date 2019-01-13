================
geonode-exchange
================

.. image:: https://codecov.io/gh/boundlessgeo/exchange/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/boundlessgeo/exchange

.. image:: https://travis-ci.org/boundlessgeo/exchange.svg?branch=master
    :target: https://travis-ci.org/boundlessgeo/exchange

geonode-exchange is a django project built on GeoNode.

---------
Run Tests
---------
Steps to run tests locally:

.. code-block:: bash

   pip install pytest-cov
   export DJANGO_SETTINGS_MODULE='exchange.settings'

   # see __init__.py and test_settings.py in exchange/settings/
   export PYTEST=1
   python manage.py migrate
   python manage.py collectstatic --noinput
   py.test --ignore=tests/ \
           --cov-report html:cov_html \
           --cov=exchange exchange/tests/

Steps to run tests in docker environment:

.. code-block:: bash

   # enter docker container environment
   sudo docker-compose exec exchange /bin/bash

   source /env/bin/activate
   cd /mnt/exchange
   ./dev/run_tests.sh


----------------------
Settings Configuration
----------------------

**AUDITING**

NOTE: All setting are configurable as environment variables

- AUDIT_ENABLED - Boolean (default is True`)
- AUDIT_TO_FILE - Boolean (default is False)
- AUDIT_LOGFILE_LOCATION - Full path with filename (default is setting directory filename exchange_audit_log.json)
