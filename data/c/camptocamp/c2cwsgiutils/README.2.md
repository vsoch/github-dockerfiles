A sample application
====================

This is a sample application shipped as a Docker Image.

It's used for testing the library. Because we want to test the currently
checked out version of the library, it is not in the requirements.txt
file. The root Makefile copies the library inline with the application
before building the Docker image.
