# folio-deployment
Deploy Folio to our Infrastructure

## Installation
After cloning this repository, run the following to install the command-line
clients:

```
bundle --binstubs=.binstubs --force
```
This installs dependencies and makes certain scripts available for execution from any
directory (although commands should generally be run somewhere inside
the project directory).  We're primarily interested in these two CLI tools:

- [okapi](https://github.com/thefrontside/okapi.rb): Useful for interacting with
  the Okapi gateway.  Makes module registration, discovery and installation
  easier.
- `okubi`: Used to deploy the FOLIO ecosystem to one of our Kubernetes clusters.

This is primarily an internal tool that is specific our organization's
infrastructure.  While it stands on its own as a proof of concept for FOLIO on
Kubernetes, it isn't intended for use by the general public.


## Deploying FOLIO
Currently the `okubi` tool only understands two subcommands: `deploy` and
`teardown`.

The `deploy` command takes a mandatory `--environment` flag, which maps to a
top-level key in the `folio.conf` file.

For example, to deploy the sandbox environment:
```
okubi deploy --environment sandbox
```
And to production:

```
okubi deploy --environment production
```

### folio.conf
The `folio.conf` file contains your configuration data namespaced by
environment.  `okubi` will process this data into templates in order to deploy
your FOLIO backend modules as Pods in the Kubernetes ecosystem.




## Deploy to Production Cluster:



3. Update the host, context and instance.

   File: `folio.conf`
    * `host: https://okapi.frontside.io`
    * `context: [project-name]_us-central1-a_okapi`
    * `instance: [project-name]:us-east1:folio-v2`



## Deploy to Development Cluster:
1. Update url in

   File: `vendor/folio_deployment/lib/folio_deployment/cli/commands/base.rb`
   ```
    @okapi ||= Okapi::Client.new('https://okapi-sandbox.frontside.io', 'fs', nil)
   ```

2. Change the cloudsql instance address. You can get the full address from the google container engine console dashboard under the sql tab if needed.

   File: `kubernetes/okapi.yaml`

   ```
    host:
    - -instances=[cloudsql-instance-name-from-gke]:okapi-sandbox=tcp:5432
   ```

3. Update the host, context and instance.

   File: `folio.conf`

    * `host: https://okapi-sandbox.frontside.io`
    * `context: [project-name]_us-central1-a_okapi-sandbox`
    * `instance: [project-name]:us-east1:okapi-sandbox`

4. Update the hosts and host url.

   File: `kubernets/ingress/ingress-tls.yaml`

   ```
    hosts:
    - okapi-sandbox.frontside.io
    rules:
    - host: okapi-sandbox.frontside.io
   ```
5. Update host url.

    File: `kubernetes/ingress/ingress.yaml`
    * `host: okapi-sandbox.frontside.io`
