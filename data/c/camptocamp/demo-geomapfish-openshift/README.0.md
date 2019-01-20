Directives and their partials are structured by components

A subdirectory is created for each component.
The component partials are directly stored in the subdirectory.

The partials are loaded individually at runtime in debug mode but preloaded in a template cache for production.
For this mechanism to work correctly the directive template URL must follow some conventions:

In the directive, the template url is written as follow: "templateUrl: demo.baseTemplateUrl + '/<component>/<partial>.html'".

In the main html file, the debug section should contain "demo.baseTemplateUrl = '${request.static_url("demo:static-ngeo/components")}';"
sudo -u postgres pg_dump --schema-only --dbname=${db} --schema=geodata > 15-schema-geodata.sql
sudo -u postgres pg_dump --schema-only --dbname=${db} --schema=edit > 16-schema-edit.sql
sudo -u postgres pg_dump --data-only --dbname=${db} --schema=${schema} > 18-data-main.sql
sudo -u postgres pg_dump --data-only --dbname=${db} --schema=${schema}_static > 19-data-main-static.sql
#sudo -u postgres pg_dump --format=c --table=planet_osm_point --dbname=osm > osm.dump
sudo -u postgres pg_dump --insert --table=planet_osm_point --dbname=osm > osm.sql
demo_geomapfish project
===================

Read the `Documentation <http://docs.camptocamp.net/c2cgeoportal/>`_

Checkout
--------

.. code:: bash

   git clone git@github.com:camptocamp/demo_geomapfish.git

Build
-----

.. code:: bash

  cd demo_geomapfish

  make -f <user>.mk build

.. Feel free to add project-specific things.
Directives and their partials are structured by components

A subdirectory is created for each component.
The component partials are directly stored in the subdirectory.

The partials are loaded individually at runtime in debug mode but preloaded in a template cache for production.
For this mechanism to work correctly the directive template URL must follow some conventions:

In the directive, the template url is written as follow: "templateUrl: demo.baseTemplateUrl + '/<component>/<partial>.html'".

In the main html file, the debug section should contain "demo.baseTemplateUrl = '${request.static_url("demo:static-ngeo/components")}';"
add the following to your Apache config:

Include ${directory}/apache/*.conf
# openshift-jenkins-custom

## Add ssh key to deploy from private git repo

OpenShift will not be able to download the source code as it will not have the credentials to authenticate itself against the git repository.

We will upload a private key to OpenShift and authorize its public counterpart at the git hosting, and with those in place, OpenShift will be able to access our private git repository.

First we had to generate an RSA key that is going to be uploaded to OpenShift.
This step is already done and you can find the keys in pass with:

```
pass c2c_mgmtsrv/github-c2c-admin-ci | jq -r '.ssh_private_key' > $HOME/.ssh/id_rsa_github_c2c_admin_ci
chmod 400 $HOME/.ssh/id_rsa_github_c2c_admin_ci
```

Then, upload the key to OpenShift:
```
oc secrets new-sshauth ssh-github-c2c-ci-secret --ssh-privatekey=$HOME/.ssh/id_rsa_github_c2c_admin_ci
```

You have to provide this key to the builder service account:

```
oc secrets link builder ssh-github-c2c-ci-secret
```

We will update our build configuration with this secret later as it does not yet exist.

## Create the jenkins custom image

OpenShift provides a certified Jenkins docker image which a set of common plugins pre-configured on it. The provided Jenkins docker image supports Source-To-Image (S2I) builds in order to easily and without hassle be able to customize the Jenkins docker image with plugins, job definitions, global configurations, etc and produce a customized Jenkins docker image to be used within our projects.

The first step is to create a project and an S2I build to customize the Jenkins docker image and install the additional plugin on it. All we need to do is to create a file called plugins.txt which lists the Jenkins plugins we want to install in the root of a Git repository and point the S2I buildconfig to that Git repo. We also add some groovy scripts to be run at the very first run of Jenkins.

Notes:
 * The build will fail here, as it tries to get a private repo from github and we have not yet updated the build config with the secret key.
 * The github url must be a ssh url as we want to use our ssh-key on this private repo.

```
oc new-project ci
oc new-build jenkins:2~git@github.com:camptocamp/openshift-jenkins-custom.git --name=jenkins-custom
```

A build called jenkins-custom is created and is running to produce our customized Jenkins docker image with the desired plugins and configurations installed. You can see the logs as the build runs using OpenShift CLI or OpenShift Web Console:

```
oc logs -f bc/jenkins-custom
```

It fails with 'error: build error: Host key verification failed.' and its normal, we have to update the build configuration with our ssh-key first:

```
oc patch buildConfig jenkins-custom -p '{"spec":{"source":{"sourceSecret":{"name":"ssh-github-c2c-ci-secret"}}}}'
```

You can now start the build again with the new config.

```
oc start-build bc/jenkins-custom
```

And it should start building our jenkins image. You can follow the build with:

```
oc logs -f bc/jenkins-custom
```

Finnaly you should see the builded image pushed in our local registry:

```
oc get is
```

## Create the jenkins custom template

We also have create a custom jenkins ephemeral template to add some environment variable needed for the jenkins base configuration such as mail, github credentials, shared library, timezone, etc...

The data values are defined separately in a data repo to be able to use different data sets. Two kind of values are defined (configMaps and secrets).

Clone the data repo, you already have the ssh key to be able to clone.

```
git clone git@github.com:camptocamp/openshift-jenkins-custom-data.git
```

### Create the configMaps

These values should not be sensitive

```
 oc create -f openshift-jenkins-custom-data/configMaps/openshift-jenkins-custom-config.yaml
```

Note that we do not add the snmp password here. We'll use secrets for this.

### Create the secrets

These values are sensitive.

So far we used a secret for the ssh-key. We will create an other secret for the smtp password:

```
oc create -f openshift-jenkins-custom-data/secrets/openshift-jenkins-custom-secrets.yaml
```

### Create the template
Clone the template repo, you already have the ssh key to be able to clone.

```
git clone git@github.com:camptocamp/openshift-jenkins-custom.git
```

And create the template

```
oc create -f openshift-jenkins-custom/template/jenkins-ephemeral-custom.yaml -n openshift
```

### Deploy the jenkins custom App

Finaly, we can deploy our jenkins app based on our customized Jenkins docker image using our customized Jenkins templates available in OpenShift and injecting configmaps and secrets. (this is defined in the yaml template)

```
oc new-app jenkins-ephemeral-custom \
    -p MEMORY_LIMIT=2Gi
```

oc describe sa jenkins

oc describe secret <jenkins-token>



### Permissions

```
oc policy add-role-to-user edit system:serviceaccount:geomapfish-dev:jenkins -n geomapfish-testing
```

### demo change

demo/static-ngeo/less/desktop.less b/demo/static-ngeo/less/desktop.less

```
...
+// @brand-primary: #9FB6CC;
+// @brand-secondary: #D3DBE3;
...
```# openshift-jenkins-custom

## Add ssh key to deploy from private git repo

OpenShift will not be able to download the source code as it will not have the credentials to authenticate itself against the git repository.

We will upload a private key to OpenShift and authorize its public counterpart at the git hosting, and with those in place, OpenShift will be able to access our private git repository.

First we had to generate an RSA key that is going to be uploaded to OpenShift.
This step is already done and you can find the keys in pass with:

```
pass c2c_mgmtsrv/github-c2c-admin-ci | jq -r '.ssh_private_key' > $HOME/.ssh/id_rsa_github_c2c_admin_ci
chmod 400 $HOME/.ssh/id_rsa_github_c2c_admin_ci
```

Then, upload the key to OpenShift:
```
oc secrets new-sshauth ssh-github-c2c-ci-secret --ssh-privatekey=$HOME/.ssh/id_rsa_github_c2c_admin_ci
```

You have to provide this key to the builder service account:

```
oc secrets link builder ssh-github-c2c-ci-secret
```

We will update our build configuration with this secret later as it does not yet exist.

## Create the jenkins custom image

OpenShift provides a certified Jenkins docker image which a set of common plugins pre-configured on it. The provided Jenkins docker image supports Source-To-Image (S2I) builds in order to easily and without hassle be able to customize the Jenkins docker image with plugins, job definitions, global configurations, etc and produce a customized Jenkins docker image to be used within our projects.

The first step is to create a project and an S2I build to customize the Jenkins docker image and install the additional plugin on it. All we need to do is to create a file called plugins.txt which lists the Jenkins plugins we want to install in the root of a Git repository and point the S2I buildconfig to that Git repo. We also add some groovy scripts to be run at the very first run of Jenkins.

Notes:
 * The build will fail here, as it tries to get a private repo from github and we have not yet updated the build config with the secret key.
 * The github url must be a ssh url as we want to use our ssh-key on this private repo.

```
oc new-project ci
oc new-build jenkins:2~git@github.com:camptocamp/openshift-jenkins-custom.git --name=jenkins-custom
```

A build called jenkins-custom is created and is running to produce our customized Jenkins docker image with the desired plugins and configurations installed. You can see the logs as the build runs using OpenShift CLI or OpenShift Web Console:

```
oc logs -f bc/jenkins-custom
```

It fails with 'error: build error: Host key verification failed.' and its normal, we have to update the build configuration with our ssh-key first:

```
oc patch buildConfig jenkins-custom -p '{"spec":{"source":{"sourceSecret":{"name":"ssh-github-c2c-ci-secret"}}}}'
```

You can now start the build again with the new config.

```
oc start-build bc/jenkins-custom
```

And it should start building our jenkins image. You can follow the build with:

```
oc logs -f bc/jenkins-custom
```

Finnaly you should see the builded image pushed in our local registry:

```
oc get is
```

## Create the jenkins custom template

We also have create a custom jenkins ephemeral template to add some environment variable needed for the jenkins base configuration such as mail, github credentials, shared library, timezone, etc...

The data values are defined separately in a data repo to be able to use different data sets. Two kind of values are defined (configMaps and secrets).

Clone the data repo, you already have the ssh key to be able to clone.

```
git clone git@github.com:camptocamp/openshift-jenkins-custom-data.git
```

### Create the configMaps

These values should not be sensitive

```
 oc create -f openshift-jenkins-custom-data/configMaps/openshift-jenkins-custom-config.yaml
```

Note that we do not add the snmp password here. We'll use secrets for this.

### Create the secrets

These values are sensitive.

So far we used a secret for the ssh-key. We will create an other secret for the smtp password:

```
oc create -f openshift-jenkins-custom-data/secrets/openshift-jenkins-custom-secrets.yaml
```

### Create the template
Clone the template repo, you already have the ssh key to be able to clone.

```
git clone git@github.com:camptocamp/openshift-jenkins-custom.git
```

And create the template

```
oc create -f openshift-jenkins-custom/template/jenkins-ephemeral-custom.yaml -n openshift
```

### Deploy the jenkins custom App

Finaly, we can deploy our jenkins app based on our customized Jenkins docker image using our customized Jenkins templates available in OpenShift and injecting configmaps and secrets. (this is defined in the yaml template)

```
oc new-app jenkins-ephemeral-custom \
    -p MEMORY_LIMIT=2Gi
```

# openshift-jenkins-slave-geomapfish

This is the builder image code for geomapfish

Initial build was tarted with

```
oc new-build https://github.com/camptocamp/openshift-jenkins-slave-geomapfish.git
```

To see build logs

```
oc logs -f bc/openshift-jenkins-slave-geomapfish
```

to create the pipeline:

```
oc new-build --strategy pipeline https://github.com/camptocamp/demo_geomapfish.git#openshift --name demo-geomapfish
```add the following to your Apache config:

Include ${directory}/apache/*.conf
