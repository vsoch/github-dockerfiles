# From Zero to Docker: Migrating to the Whale

Example Dockerfiles to ilustrate building applications as a pair of base and
main images, as described in the [blog post](https://blog.newrelic.com/zero-to-docker/).

The base image is provisioned using Ansible and on most of the builds, the
cached version is used (as long as the Ansible provisioning code hasn't
changed).

The main image is always forcibly rebuilt and contains the latest version of
the application.
