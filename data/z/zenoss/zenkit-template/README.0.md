# {{Title}} ({{Name}})
{{Description}}

## Purpose
TODO: Describe what this service does in general terms.

## Metrics
TODO: Describe the metrics exposed by this service, and what they indicate.

## API
TODO: Describe the API endpoints this service provides, and what they do. No
need to go into as much specificity as the Swagger spec will, but be
descriptive.

## Configuration
* `{{replace Name "-" "_" -1 | toUpper}}_LOG_LEVEL`: Log level. Defaults to "info".
* `{{replace Name "-" "_" -1 | toUpper}}_LOG_STACKDRIVER`: Whether to format logs for Stackdriver. Defaults to true.
* `{{replace Name "-" "_" -1 | toUpper}}_AUTH_DISABLED`: Whether authentication is enforced. If true, middleware is used that injects an admin identity into unauthenticated requests.
* `{{replace Name "-" "_" -1 | toUpper}}_AUTH_DEV_TENANT`: When auth is disabled, the tenant name to use as the identity. Defaults to "ACME".
* `{{replace Name "-" "_" -1 | toUpper}}_AUTH_DEV_USER`: When auth is disabled, the user id to use as the identity. Defaults to "zcuser@acme.example.com".
* `{{replace Name "-" "_" -1 | toUpper}}_TRACING_ENABLED`: Whether request tracing is enabled.
* `{{replace Name "-" "_" -1 | toUpper}}_GRPC_LISTEN_ADDR`: The address on which the gRPC server should listen. Defaults to ":8080".
# ci
Resources related to continuous integration

## tl;dr

You probably don't need to care about this directory, but if you need to 
change the Jenkins jobs for this service, keep reading. 

## What's inside

* Jenkinsfile: contains the pipeline definition used by the pull-request job.
* service.groovy: contains variables shared by the pull-request and deployment jobs.

## Development

We use Jenkins for our CI process.  This microservice has a suite of Jenkins 
jobs associated with it.  The suite consists of a pull-request job and a 
deployment (or "master") job.  The pull-request job runs in response to a new 
or updated pull-request and is responsible for running all relevant tests.  
Once the pull-request is merged into the master branch, the deploy job runs 
in order to prepare the changes in the pull-request for deployment to production.

The jobs are created from a template. To update the jobs for, run the 
[Microservice Job Builder](http://jenkins.zing.zenoss.eng/job/job_create/parambuild/?service={{Name}}).
More information about the job builder is found 
[here](https://github.com/zenoss/zing-ci/blob/master/jenkins-job-builder/README.md).`

