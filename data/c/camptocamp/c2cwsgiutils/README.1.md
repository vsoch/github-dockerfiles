A sample acceptance test image
==============================

This directory is used to build a Docker image that runs acceptance
tests against the sample application.

When a container is run with this image, it will start tests. A typical
test session runs like that:

* Start a test composition (see the [composition](tests/conftest.py)
  fixture):
  * The sample application
  * Two instances of PostgresQL (master and slave), with the test table
    and some test data in them (done in the
    [master_db_setup and slave_db_setup](tests/conftest.py) fixtures).

* For each test:
  * Establish an HTTP session with the sample application (see the
    [app_connection](tests/conftest.py) fixture)
  * Exercise the application's API and check the results
