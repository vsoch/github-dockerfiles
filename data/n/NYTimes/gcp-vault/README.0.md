# `gcpvault` Examples

We've provided basic examples of applications capable of running on Google App Engine Standard or Flexbile environments, Serverless platform or even Kubernetes.

To run any examples locally, users must have the Vault CLI tool installed.

See [Vault's documentation](https://www.vaultproject.io/docs/install/index.html) for installation instructions.
# The Marvin/App Engine Standard Environment Example

This example shows how to use middleware in the [Marvin framework](https://github.com/NYTimes/marvin/) to fetch secrets from Vault.

To run this service, you must be using [Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/go/download) >= `162.0.0` or the "original" App Engine Go SDK >= `1.9.56`.

To run this against your own Vault installation, update the values in `server/app.yaml` for deployment and `server/make_local_yaml.sh` for local development.

The `server/run_local.sh` script wraps both the Vault login and App Engine's `dev_appserver.py` command to simplify running the server locally.

The app.yaml here is meant for actual deployments.

The `make_local_yaml` script here is a helper for devs to inject their github PAT into the local App Engine environment when running the service locally.

Users should first run `make_local_yaml` to generate a local.yaml file and then run the service via `dev_appserver.py local.yaml`
# The basic App Engine Standard Environment Example

This example shows how to use basic HTTP middleware to fetch secrets from Vault.

To run this service, you must be using [Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/go/download) >= `162.0.0` or the "original" App Engine Go SDK >= `1.9.56`.

To run this against your own Vault installation, update the values in `app.yaml` for deployment and `make_local_yaml.sh` for local development.

The `run_local.sh` script wraps both the Vault login and App Engine's `dev_appserver.py` command to simplify running the server locally.
# The Gizmo/Serverless Example

This example shows how to use service initiation in the [Gizmo server](https://godoc.org/github.com/NYTimes/gizmo/server) to fetch secrets from Vault.

To run this against your own Vault installation, update the values in `server/run_local.sh` for local development.
