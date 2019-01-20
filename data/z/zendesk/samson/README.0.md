
To start creating your plugin, navigate to the 'samson_plugin.rb' file
in the new plugin directory above and register for the various hooks
to add views/assets/models to Samson.

This plugin acts mostly like a Rails Engine, so it can contain controllers/
models/routes/migrations/etc...

Amend core models by defining app/decorators/{model}_decorator.rb, it
will be auto-loaded when the underlying model is loaded.

Remember to run 'bundle install' now to get it loaded into Samson for testing!


Happy Coding!
<3 The Samson Team
Flowdock notification.
 - Display newrelic graphs during/after deploy, with `NEW_RELIC_API_KEY`
 - Add Newrelic instrumentation, with `NEW_RELIC_LICENSE_KEY`
Github integration.

 - comments on PRs when they are deployed
 - adds deployment for each commit that is deployed via Github deployment api
# Prerequisite Stages

Allows users to enforce that a reference has been deployed to a stage's prerequisite stages before it is allowed to be deployed.
Notify slack channels before/after deploy/on buddy request.

Additionally allows all requests to be sent to a single channel with `SLACK_GLOBAL_BUDDY_REQUEST`, see `.env.example`.
Start and track jenkins jobs after deploys.
# Deploy ENV Vars

This plugin allows each deploy to have environment variables on its own. Same as
projects or stages.

This can be used to have generic stages to run one-off jobs or other tasks that need to be parameterized on each run.
# Airbrake Plugin

Plugin that notifies Airbrake of errors
## Env Plugin
Plugin to manage ENV settings for projects and write .env files during deploy.

Includes `/projects/:permalink/environment?deploy_group=permalink` endpoint that returns the `.env` content
for a project and deploy_group.

## GitHub to manage environment variables
This plugin has an option to use a GitHub repository as source for environment variables. 
The DEPLOYMENT_ENV_REPO must be set in samson's start up to be the `organization/repo`.   

Each project must opt-in to it via project settings.

The expected structure of this repository is a directory named `generated` with a sub directory for each 
_project permalink_ samson deploys.  Within this directory for a project are the deploy group .env files using the name
of the _deploy group permalink_ with a `.env` extension.  For a project with the permalink `data_processor` and 
the deploy group permalinks `staging1`, `prod1` and `prod2` samson expects to see this directory tree:
```bash
.
├── deploy_groups.yml
├── generated
│   └── fake_project
│       ├── staging1.env
│       ├── prod1.env
│       └── prod2.env
├── projects
│   └── fake_project.env.erb
└── shared
    └── env_three.env.erb
```
The contents of the `.env` file is a sequence of environment variable key and value pairs.
```bash
# cat generated/fake_project/staging1.env
MAX_RETRY_ATTEMPTS=10
SECRETE_TOKEN=/secrets/SECRET_TOKEN
RAILS_THREAD_MIN=3
RAILS_THREAD_MAX=5 
```
###### Merging enviroment variables stored in the database with those in the repo 
The generated enviornment variables is the merger of deploy_group env variables, if the samson `deploy_group plugin` is 
activated, the `project` environment variables in the samson database and the environment variables in the github `repo`.
The order of precedence for variables with the same key name: `deploy_group` replaces `project` which replaces `repo` variables.

*The variables in the Samson database overwrite any variables in the repo.*
# Ledger Plugin

Plugin that allows samson to post events to ledger (an internal Zendesk system)

Requires 2 ENV vars to be set in order to work
LEDGER_BASE_URL="https://ledger.mydomain.com" # base url of the ledger api host (http or https)
LEDGER_TOKEN="thisismytoken" # api access token for that system                                                                 
# AWS STS Plugin

Inject temporary AWS Role credentials into a deploy environment using [AWS STS](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) and [Assume role](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).

## Overview

The plugin uses the assume role feature of STS and exposes the generated credentials
as environment variables:
  - STS_AWS_ACCESS_KEY_ID
  - STS_AWS_SECRET_ACCESS_KEY
  - STS_AWS_SESSION_TOKEN

The plugin authenticates with AWS using the following samson environment variables:
  - SAMSON_STS_AWS_ACCESS_KEY_ID
  - SAMSON_STS_AWS_SECRET_ACCESS_KEY
  - SAMSON_STS_AWS_REGION

Specify the Amazon Resource Name (ARN) of the role to assume in the stage's settings page.
# Gcloud Plugin

## Image tagging

Tag gcloud images with the stage permalink they deployed to, so developers can pull down the a specific stage's image.
If the stage is a production stage, the image is also tagged with 'production'.

## Image building

Check the "build with GCR" checkbox on the project edit page.
Images will be built using `gcloud container build submit`, which can be slow for large projects.
If the file upload takes too long or you have a custom cloudbuild.yaml, use build triggers instead and
notify samson of the finished builds via the build api.

## Image scanning

If a project opts in to "Show GCR Vulnerabilities", show GCR build vulnerabilities scan result on the build page and during deploy.
If the stage opts in to "Block deploy of vulnerable images", then deploys will fail when vulnerabilities are found.

Note: because of a bug in gcloud api vulnerability scans results are only available 10 minutes after the build completes.

## Setup

 - enable [cloudbuild api](https://console.cloud.google.com/apis/api/cloudbuild.googleapis.com/overview)
 - create a gcloud service account with "Cloud Container Builder" and "Storage Object Creator"
 - download credentials for that account
 - run `gcloud auth activate-service-account --key-file <YOUR-KEY>` on the samson host
 - run `gcloud config set account $(jq -r .client_email < <YOUR-KEY>)` on the samson host

## ENV Vars

  - `GCLOUD_PROJECT` - project to use
  - `GCLOUD_ACCOUNT` - account to use
  - `GCLOUD_OPTIONS` - additional commandline options
  - `GCLOUD_IMAGE_TAGGER` - set to `true` to enable tagging on deploy
  - `GCLOUD_IMAGE_SCANNER` - set to `true` to enable build scanning 
  - `GCLOUD_GKE_CLUSTERS_FOLDER` - set to folder where gke clusters config should be stored to enable gke cluster UI
### Description

This plugin shows failing jenkins jobs when users try to create a new deploy. This only shows for production. It shares the jenkins credentials with the jenkins plugin. The jobs are selected from a view defined by JENKINS_STATUS_CHECKER env var.

### Setup

1. Required Environment Variables

```
JENKINS_STATUS_CHECKER # /view/StagingStatus, the checklist view
JENKINS_URL            # 'https://jenkins.yourcompany.com', shared by jenkins plugin
JENKINS_USERNAME       # shared by jenkins plugin
JENKINS_API_KEY        # shared by jenkins plugin
```

2. Enable plugin on a per project basis by ticking the "Enable Jenkins Status Checker" checkbox at `projects/[your-project]/edit`
Datadog monitoring and deploy tracking
# Rollbar Hook Plugin

This plugin adds deploy tracking for [Rollbar](https://rollbar.com/)

1. Add `https://api.rollbar.com/api/1/deploy/` to the the webhook URL, unless you're using a self-hosted instance of Rollbar.
2. Sign in to Rollbar and go to the "Deploys" area.
3. copy the `access_token` to Samson or add is as project secret and use `secret://rollbar_access_token`
4. The `environment` name must match one from Rollbar "Settings > General > Environments".
# AWS ECR Plugin

This plugin allows integration between Samson and
[AWS ECR](http://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html),
which is the Docker registry service managed by AWS.

## Overview

AWS ECR requires you to refresh your registry credentials every 12 hours (approximately).
Because Samson only supports to set credentials through the environment, this plugin
runs a callback before every build, requesting AWS for the new credentials. Then sets
these credentials to the environment so the normal docker build process can use them.

It also tries to create a new repository if it does not already exist.

To configure this plugin you need to:

* Enable docker in samson (DOCKER_FEATURE=1)
* Set your ECR registry (DOCKER_REGISTRIES=<account>.dkr.ecr.<aws-region>.amazonaws.com)
* Set your [AWS credentials](http://docs.aws.amazon.com/sdkforruby/api/#Configuration)
* Ensure permissions "ecr:DescribeRepositories" and "ecr:CreateRepository" are available.
Update a zendesk ticket after deploy.
# Rollbar Plugin

Plugin that notifies Rollbar of errors
# Rollbar Dashboards Plugin

A plugin which displays the top Rollbar items for projects and deploys.
Notify Assertible after successful deploys.

Following environment variables must be set:
 - `ASSERTIBLE_DEPLOY_TOKEN`
 - `ASSERTIBLE_SERVICE_KEY`
 
 They can be found in Assertible by going to the `Deployments` tab from a 
 service's dashboard.
# Slack App Plugin

This plugin adds a `/deploy` command to Slack which creates Samson deployments.
To activate:

1. Go over to Slack and create a [new app](https://api.slack.com/apps/new). Many of the fields are completely up to you, but these are important:
  - Add `https://your.samson.tld/slack_app/oauth` as a redirect URI.
  - Enable interactive messages, and set the URI to `https://your.samson.tld/slack_app/interact`.
  - Add a `/deploy` slash-command, and set its URL to `https://your.samson.tld/slack_app/command`.
  - Grab the Client ID and secret and verification token, and record them in your environment as `SLACK_CLIENT_ID`, `SLACK_CLIENT_SECRET`, and `SLACK_VERIFICATION_TOKEN`.
2. Visit https://your.samson.tld/slack_app/oauth, and click the "Connect to Slack" button.
3. Switch back over to Slack, and try out the `/deploy` command!
Notify airbrake after deploys if, to resolve all old errors if:
 - deploy groups are used
 - deploy was a success
 - stage has notify_airbrake enabled
 - environment name is simple / looks like a rail env (staging/production)
 - `airbrake_api_key` is set as secret for the given project/deploy-group
# Datadog Plugin

Plugin that trace requests and notify to Datadog APM
# Kubernetes Plugin

Allows Samson to be able to deploy to [Kubernetes](kubernetes.io), and includes various validations and dashboards.

## Overview

Samson will talk to N Kubernetes clusters via their API.
Clusters can be running locally (Docker For Mac / Minikube), in a datacenter,
on EKS, or GKE.

Workflow:
1. Enable the Docker feature by adding `DOCKER_FEATURE=1` to your `.env` file
1. Enable the [Deploy Group](/docs/extra_features.md) feature by adding `DEPLOY_GROUP_FEATURE=1` to your `.env` file
1. Configure Kubernetes cluster(s) on `/kubernetes/clusters`
1. Create a project containing a `Dockerfile`
1. Add [Kubernetes role files](#kubernetes-roles) to your project repository
1. Configure "Roles" for the project `/projects/<PROJECT>/kubernetes/roles`
1. Create a stage that's connected to N deploy groups
1. Configure how many replicas, CPU, and memory each deploy group should use
1. Click 'Deploy' 🎉

## Configuring the Cluster

Use Samson cluster UI (`/kubernetes/clusters`) to configure where the [kubeconfig file](http://kubernetes.io/v1.0/docs/user-guide/kubeconfig-file.html)
for your cluster is and what context (custer/user pair) to use. You need to be a Super Admin to create a cluster.

### Mapping DeployGroups to Clusters

In the "Edit Deploy Group" UI `/deploy_groups`, select a Kubernetes cluster and a namespace.

Background:
Kubernetes has the concept of a [Namespace](http://kubernetes.io/v1.0/docs/user-guide/namespaces.html),
which means a virtual cluster inside of a single physical cluster. This can be
useful if you want to have a single Kubernetes cluster running in AWS or a
datacenter, but logically divide them between a "staging" and "production"
namespace.

## Project Configuration

Project pages will have a Kubernetes link (white wheel on a blue background).

### Kubernetes Roles

A "role" is not a concept in Kubernetes itself. It is specific to Samson.

It refers to the different ways that a project can be run, that may want to
be scaled separately. For each role, Samson allows configuring CPU (requests and limits),
memory (requests and limits), and replicas per deploy group.

Each time this project is deployed, it deploys all roles.

For example, a Ruby on Rails project that uses Resque for background
job processing. This project will likely have 4 roles:

1. The "Migration" role that runs database migrations, 1 replica, low cpu
1. The "App Server" role, that runs the Rails server, 3 replicas, high cpu
1. The "Resque Worker" role, that runs instances of the workers, 5 replicas, high cpu
1. The "Resque Scheduler" role, a singleton process that manages recurring jobs, 1 replica, low cpu

### Configuration Files

Each [Kubernetes role](#kubernetes-roles) is read from a file in the project's repository
. It has to contain the definitions of N Deployment/Daemonset/Service/Job/ConfigMap/etc. Samson's `TemplateFiller`
then augments the definitions by adding docker repo digest, labels, annotations, resource limits,
environment variables, secrets, etc and then sends them to the Kubernetes API.

Multiple roles will likely be similar, but have different commands or liveness probes.
([kucodiff](https://github.com/grosser/kucodiff) can be used to make sure they stay in sync).

Validate required environment variables are set by adding `metadata.annotations.samson/required_env` (space separated).

```
samson/required_env: >
  RAILS_ENV
  OTHER_STUFF

```

### Limits

Samson allows limiting how many resources each project can use per Deploy Group, see `/kubernetes/usage_limits`.

To forbid deployment of anything without a limit, add a `All/All` limit with 0 cpu and memory.

To allow creating limits without scoped or project, set `KUBERNETES_ALLOW_WILDCARD_LIMITS=true`.

## Deploying to Kubernetes

Each deploy selects a Git SHA and N deploy groups to deploy to. For this Git SHA Samson finds or creates all builds that
were requested in the [Kubernetes role config files](#configuration-files).

### Record Keeping

For each deploy, a `Kubernetes::Release` is created, which tracks which `Build` was deployed and
who executed it.

For each `DeployGroup` and `Kubernetes::Role` in the deploy, a `Kubernetes::ReleaseDoc` is created, which tracks what kubernetes
configuration was used.

```
Kubernetes::Release
  |
   -> Kubernetes::ReleaseDoc (1 per role and DeployGroup)
      |
      -> Kubernetes Pods (how ever many replicas specified)
```

### Docker Images

(To opt out of this feature set `containers[].samson/dockerfile: none` or `metadata.annotations.container-nameofcontainer-samson/dockerfile: none`)

For each container (including init containers) Samson finds or creates a matching Docker image for the Git SHA that is being deployed.
Samson always sets the Docker digest, and not a tag, to make deployments immutable.

If `KUBERNETES_ADDITIONAL_CONTAINERS_WITHOUT_DOCKERFILE=true` is set, it will only enforce this for the first container.

Samson matches builds to containers by looking at the `containers[].samson/dockerfile` attribute or the
base image name (part after the last `/`), if the project has enabled `Docker images built externally`.

Images can be built locally via `docker build`, or via `gcloud` CLI (see Gcloud plugin), or externally and then sent to Samson via the
API (`POST /builds.json`).

### Injected config

Via [Template filler](/plugins/kubernetes/app/models/kubernetes/template_filler.rb)

 - Docker image
 - Limits + replicas
 - Environment variables: POD_NAME, POD_NAMESPACE, POD_IP, REVISION, TAG, DEPLOY_ID, DEPLOY_GROUP, PROJECT, ROLE,
   KUBERNETES_CLUSTER_NAME, and environment variables defined via [env](/plugins/env) plugin.
 - Secret puller and secret annotations (if secret puller + vault is used)

### Migrations / Prerequisite

Add a role with only a `Pod`, `metadata.annotations.samson/prerequisite: 'true'`, and command to run a migrations.
It will be executed before the rest is deployed.

For default it waits for 10 minutes before timeout, you can change the timeout
using KUBERNETES_WAIT_FOR_PREREQUISITES env variable (specified in seconds).

### Deployment timeouts

A deploy will wait for 10 minutes for pods to come alive. You can adjust this
timeout using KUBERNETES_WAIT_FOR_LIVE (specified in seconds).

### Deployment stability check

A deploy will get checked for stability every 2 seconds for a minute, before being marked as stable.
These can be configured (in seconds) using `KUBERNETES_STABILITY_CHECK_DURATION` and `KUBERNETES_STABILITY_CHECK_TICK` environment variables.

### StatefulSet

On kubernetes <1.7 they can only be updated with `OnDelete` updateStrategy,
which is supported by updating only the pod containers and replica count (not set metadata/annotations).
Prefer `RollingUpdate` if possible instead.

### Duplicate deployments

To deploy the same repository multiple times, create separate projects and then set `metadata.annotations.samson/override_project_label: "true"`,
samson will then override the `project` labels and keep deployments/services unique.

### Service updates

Too keep fields/labels that are manually managed persistent during updates, use `KUBERNETES_SERVICE_PERSISTENT_FIELDS`, see .env.example
or set `metadata.annotations.samson/persistent_fields`

### PodDisruptionBudget

Samson can add a dynamic PodDisruptionBudget by setting `metadata.annotations.samson/minAvailable: 30%`, it calculates the ceil of this with the configured replicas.
(also supports absolute values like `"1"`)

To remove it, set to '0', deploy, delete it from the template.

Samson can auto-add a `PodDisruptionBudget` for every `Deployment` by setting for example `KUBERNETES_AUTO_MIN_AVAILABLE=80%`.
Users can opt-out by setting `metadata.annotations.samson/minAvailable: disabled`.

### Blue/Green Deployment

Can be enabled per role, it then starts a new isolated deployment shifting between blue and green sufixes,
switching service selectors if successfully deployed and deleting previous resources.
All active resources must be deleted manually when switching to blue/green from regular deployment.

### Resources without cpu limits

Set `KUBERNETES_NO_CPU_LIMIT_ALLOWED=1`, see [#2820](https://github.com/zendesk/samson/issues/2820) for why this can be useful.

### Enforcing team ownership

Knowing which team owns each component is useful, set `KUBERNETES_ENFORCE_TEAMS=true`
to make all kubernetes deploys that do not use a `metadata.labels.team` / `spec.template.metadata.labels.team` fail.

### Using custom namespace

Samson overrides each resources namespace with to the deploygroups `kubernetes_namespace`.
To make samson not override the namespace, set `metadata.kubernetes.io/cluster-service: 'true'`

### Preventing request loss with preStop

To enable the following functionality you need to set `KUBERNETES_ADD_PRESTOP=true`.

Samson automatically adds `container[].lifecycle.preStop` `sleep 3` if a preStop hook is not set and
`container[].samson/preStop` is not set to `disabled`, to prevent in-flight requests from getting lost when taking a pod
out of rotation (alternatively set `metadata.annoations.container-nameofcontainer-samson/preStop: disabled`).

### Showing logs on successful deploys

Set `metadata.annoations.samson/show_logs_on_deploy: 'true'` on pods, to see logs when the deploy succeeds.
This can be useful for Migrations (see above).
(On failure, samson always shows all pod logs)

### Changing templates via ENV

For custom things that need to be different between environments/deploy-groups.

Use an annotation to configure what will to be replaced:
```
metadata.annotations.samson/set_via_env_json-metadata.labels.custom: SOME_ENV_VAR
```
Then configure an ENV var with that same name and a value that is valid JSON.

### Allow randomly not-ready pods during redines check

Set `KUBERNETES_ALLOW_NOT_READY_PERCENT=10` to allow up to 10% of pods being not-ready,
this is useful when dealing with large deployments that have some random failures.

### Disabling service selector validation

To debug services or to create resources that needs to reference a selector that doesn't include team/role (like a Gateway), you can disable selector validation with:

`metadata.annotations.samson/service_selector_across_roles: "true"`
Pipeline deploys: a successful deploy kicks off the next deploy.
