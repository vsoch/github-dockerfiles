drone-gdm
=========

[![Build Status](https://travis-ci.org/NYTimes/drone-gdm.svg?branch=master)](https://travis-ci.org/NYTimes/drone-gdm)

A simple drone plugin which wraps [Google Deployment Manager](https://cloud.google.com/deployment-manager/docs/).

### Docker Tags

#### All Versions
* [specific release number](https://github.com/NYTimes/drone-gdm/releases) (see [dockerhub repo](https://hub.docker.com/r/nytimes/drone-gdm/tags/)).
* the `develop` tag to get the last thing that _built_

#### 1.x Series
* the `latest` tag to get the latest *v1.x* _stable_
* the `beta` tag to get the latest _beta_ release
* the `alpha` tag to get the latest `alpha` release
* the `develop` tag to get the last thing that _built_
<sub>(alpha, beta, and develop tags introduced as of `1.2.1a`)</sub>

Starting with version `2.0.0a` the tag scheme is prefixed with major version, e.g:
* the `v2-alpha` tag to get the latest 2.x _alpha_ release
* the `v2-beta` tag to get the latest 2.x _beta_ release
* the `v2-stable` tag to get the latest 2.x _stable_ release
<sub>This pattern will continue with subsequent major version releases; enabling you to pin your build to the latest stable version of any given backwards-compatible, major-level release</sub>


### Features
 * Set the desired `state` (absent, present, or latest) and the plugin determines whether to create, update, or delete.
 * Support for [GDM Beta Composite Types](https://cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types)

### Compatibility
Drone-GDM has been tested with drone *0.4* and *0.8*.

Usage
-----
The bulk of the input parameters are mapped directly to `gcloud` command options.
Documentation follows for the handful of parameters which are particular to `drone-gdm`.

#### State and Action
The `state` can be one of `absent`, `present`, or `latest`.

| Plugin "state" | Object Exists? | Action      |
| -------------- | -------------- | ----------- |
| present        | no             | `create`    |
| present        | yes            | _no action_   |
| latest         | no             | `create`    |
| latest         | yes            | `update`    |
| absent         | no             | _no action_   |
| absent         | yes            | `delete`    |

The specific `action` selected by drone-gdm can be provided to your template
as a property, by specifying `passAction: true`. This will invoke your
configuration or template with `--properties=action:<action from table above>`.

### Variables
To circumvent data-type limitations imposed by the passing of properties via the
deployment manager `--properties` option, template and configurations files
passed to drone-gdm are first parsed as [golang templates](https://golang.org/pkg/text/template/) with the following
top-level interfaces available for variable interpolation:
 - `.drone` - Drone environment variables provided by the CI system during plugin invocation
 - `.plugin` - Plugin parameters passed via environment during plugin invocation
 - `.context` - Any variables defined in the `vars` section of the plugin invocation
 - `.config` - Any variables defined in the `vars` section of the configuration definition
 - `.properties` - Variables defined in the `properties` section of the configuration definition
 - `.gdm` - A dictionary containing:
   - `name` - entity name for the configuration/template/composite
   - `status` - the entity status (e.g. DEPRECATED, EXPERIMENTAL, SUPPORTED)
   - `project` - the GCP project name
   - `action` - the gcloud "action" parameter (i.e. `create`, `update`, or `delete`)

### Example with Inline Configurations
```Yaml
deploy:
  gdm:
    # Indicate where to acquire the image:
    image: nytimes/drone-gdm:2.0.0

    # Provided JSON auth token (from drone secrets):
    gcloudPath: /bin/gcloud   # path to gcloud executable
    verbose: false            # (optional)
    dryRun: false             # (optional)
    token: >
      $$GOOGLE_JSON_CREDENTIALS
    project: my-gcp-project   # Da--project
    preview: false            # --preview
    async: false              # --async
    vars:
    - myCtxVar: ctxVal1
    - myOtherCtxVar: ctxVal2

    configurations:
    - name:  my-deployment
      group: deployment
      state: present
      path: ./my-deployment.yaml
      description: A GDM Deployment
      vars:
      - myCfgVar: cfgVal1
      - myOtherCfgVar: cfgVal2
      properties:    # mapped to gcloud '--properties=...'
        myvar: myval # can be referenced in jinja as: {{ properties.myvar }}
      labels:        # mapped to '--labels' or '--update-labels', as appropriate
        mylabel: labelval
      autoRollbackOnError: false
      createPolicy: CREATE_OR_ACQUIRE # Optional: CREATE_OR_ACQUIRE or CREATE
      deletePolicy: DELETE # Optional: DELETE or ABANDON
      passAction: false # if true, pass action as property, e.g. "action:update"

    - name:  my-composite
      version: beta  # gcloud version to use
      group: composite
      state: present
      path: ./my-composite.jinja
      description: A GDM "Composite Type"
      labels: # mapped to '--labels' or '--update-labels', as appropriate
        mylabel: labelval
      status: SUPPORTED # Optional: SUPPORTED, DEPRECATED, or EXPERIMENTAL
      passAction: false

```

### Example with Inline and External Configurations
```Yaml
deploy:
  gdm:
    # Indicate where to acquire the image:
    image: nytimes/drone-gdm:2.0.0

    # Provided JSON auth token (from drone secrets):
    gcloudPath: /bin/gcloud   # path to gcloud executable
    verbose: false            # (optional)
    dryRun: false             # (optional)
    token: >
      $$GOOGLE_JSON_CREDENTIALS
    project: my-gcp-project   # Da--project
    preview: false            # --preview
    async: false              # --async

    vars:
       prefix: test1
    configFile: my-configurations.yml
    configurations:
    - name:  my-deployment
      group: deployment
      state: present
      path: ./my-deployment.yaml
      description: A GDM Deployment
      properties:    # mapped to gcloud '--properties=...'
        myvar: myval # can be referenced in jinja as: {{ properties.myvar }}
      labels:        # mapped to '--labels' or '--update-labels', as appropriate
        mylabel: labelval
      autoRollbackOnError: false
      createPolicy: CREATE_OR_ACQUIRE # Optional: CREATE_OR_ACQUIRE or CREATE
      deletePolicy: DELETE # Optional: DELETE or ABANDON
      passAction: false # if true, pass action as property, e.g. "action:update"
```

##### my-configurations.yml
``` Yaml
# Parsed as a golang template with variables populated from "vars" above.
- name:  {{.prefix}}-composite
  version: beta  # gcloud version to use
  group: composite
  state: present
  path: ./my-composite.jinja
  description: A GDM "Composite Type"
  labels: # mapped to '--labels' or '--update-labels', as appropriate
    mylabel: labelval
  status: SUPPORTED # Optional: SUPPORTED, DEPRECATED, or EXPERIMENTAL
  passAction: false

```

### Resources
 - [drone-gdm on Travis-CI](https://travis-ci.org/NYTimes/drone-gdm)
 - [drone-gdm on dockerhub](https://hub.docker.com/r/nytimes/drone-gdm/)
