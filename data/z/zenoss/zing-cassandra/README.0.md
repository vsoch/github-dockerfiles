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
[Microservice Job Builder](http://jenkins.zing.zenoss.eng/job/job_create/parambuild/?service=zing-cassandra).
More information about the job builder is found 
[here](https://github.com/zenoss/zing-ci/blob/master/jenkins-job-builder/README.md).`

