---
layout: default
title:  "Kubernetes Credentials Provider Plugin"
permalink: /
---

The *Kubernetes Credentials Provider* is a [Jenkins](https://jenkins.io) plugin to enable the retreival of [Credentials](https://plugins.jenkins.io/credentials) directly from Kubernetes.

The plugin supports most common credential types and defines an [`extension point`](https://jenkins.io/doc/developer/extensions/kubernetes-credentials-provider/) that can be implemented by other plugins to add support for custom Credential types. 

# Using

### Pre-requisites

- Jenkins must be running in a kubernetes cluster
- The pod running Jenkins must have a service account with a role that sets the following:
  - get/watch/list permissions for `secrets`[^AWS] 

[^AWS]: it is reported that running in KOPS on AWS you will also need permissions to get/watch/list `configmaps`

Because granting these permissions for secrets is not something that should be done lightly it is highly advised for security reasons that you both create a unique service account to run Jenkins as, and run Jenkins in a unique namespace.

## Managing credentials

### Adding credentials

Credentials are added by adding them as secrets to Kubernetes, this is covered in more detail in the [examples](examples) page.

### Updating credentials

Credentials are updated automatically when changes are made to the Kubernetes secret.

### Deleting credentials

Credentials are deleted automatically when the secret is deleted from Kubernetes. 

### Viewing credentials

Once added the credentials will be visible in Jenkins under the `/credentials/` page.
Any credentials that are loaded from Kubernetes can be identified by the Kubernetes provider icon in the view.

## Using the credentials inside Jenkins

To use credentials in a pipeline you do not need to do anything special, you access them just as you would for credentials stored in Jenkins. 

for example, if you had the follwing Secret defined in Kubernetes:
{% highlight yaml linenos %}
{% include_relative examples/username-pass.yaml %}
{% endhighlight %}

you could use it via the [Credentials Binding plugin](https://plugins.jenkins.io/credentials-binding) 

{% highlight groovy %}
withCredentials([usernamePassword(credentialsId: 'another-test-usernamepass',
                                  usernameVariable: 'USER', 
                                  passwordVariable: 'PASS')]) {
  sh 'curl -u $USER:$PASS https://some-api/'
}
{% endhighlight %}

or by passing the credentialId directly to the step requiring a credential:

{% highlight groovy %}
git credentialsId: 'another-test-usernamepass', url: 'https://github.com/foo/bar'
{% endhighlight %}

# Issue reporting

Any issues should be reporting in the main [Jenkins JIRA tracker](https://issues.jenkins-ci.org).
The issue tracker is not a help forum, for help please use [IRC](https://jenkins.io/chat/) or the [user mailing list](https://groups.google.com/forum/#!forum/jenkinsci-users) 

# Releases and Change logs

The [release notes](https://github.com/jenkinsci/kubernetes-credentials-provider-plugin/releases) are managed in GitHub. 
The latest release will be visible in the Jenkins Update center approximatly 8 hours after a release.

# Developing

This [page](dev/) contains more information on a developer environment.
---
layout: default
title:  "Kubernetes Credentials Provider Plugin : Examples"
permalink: /examples/
---

# Credential Examples

Credentials are added and updated by adding/updating them as secrets to Kubernetes.
The format of the Secret is different depending on the type of credential you wish to expose, but will all have several things in common: 
- the label  `"jenkins.io/credentials-type"` with a type that is known to the plugin (e.g. `certificate`, `secretFile`, `secretText`, `usernamePassword`, `basicSSHUserPrivateKey`)
- an annotation for the credential description: `"jenkins.io/credentials-description" : "certificate credential from Kubernetes"`

To add or update a Credential just execute the command `kubectl apply -f <nameOfFile.yaml>` 

The raw yaml for the following examples can be found in the GitHub [repository](https://github.com/jenkinsci/kubernetes-credentials-provider-plugin/tree/master/docs/examples)

Where Strings are encoded using base64 the bytes encoded should be from the UTF-8 representation of the String.

## UserName / Password credentials

The UserName password credentials are probably the most commonly uses.

{% highlight yaml linenos %}
{% include_relative username-pass.yaml %}
{% endhighlight %}


## Secret Text

{% highlight yaml linenos %}
{% include_relative secretText.yaml %}
{% endhighlight %}

## Secret File

{% highlight yaml linenos %}
{% include_relative secretFile.yaml %}
{% endhighlight %}

## Certificates

{% highlight yaml linenos %}
{% include_relative certificate.yaml %}
{% endhighlight %}

## Basic SSH Private Key

Without passphrase:
{% highlight yaml linenos %}
{% include_relative basic-ssh-username-private-key.yaml %}
{% endhighlight %}

With passphrase:
{% highlight yaml linenos %}
{% include_relative basic-ssh-username-private-key-passphrase.yaml %}
{% endhighlight %}


# Custom field mapping

Sometimes you may want the secret to be able to be consumed by another tool as well that has a different requirement for the data fields.
In order to facilitate this the plugin supports the remapping fields.
In order to achieve this you add an attribute begining with `jenkins.io/credentials-keybinding-` and ending with the normal field name and having the value of the new field name.
The following example remaps the `username` and `password` fields to `user` and `pass`:
{% highlight yaml linenos %}
{% include_relative username-pass-with-custom-mapping.yaml %}
{% endhighlight %}

---
layout: default
title:  "Kubernetes Credentials Provider Plugin: Development"
permalink: /dev/
---

# Helpful settings for testing

The plugin will run if you have configured kubectl locally (and have the permissions required to watch/list/read secrets).  
For full integration testing then this directory contains some files useful for *developer* testing the plugin inside a Jenkins running inside a kubernetes (tested with GKE).

They may require some small tweaks for your environment (as it will be different to mine), but if so please don't attempt to commit them back :-)

## Testing

All commands are run from `docs/dev` unless otherwise specified.

### Initial setup...

1. Create the testing namespace  `kubectl apply -f testing-namespace.yaml`
2. create a service user to run Jenkins  `kubectl apply -f service-account.yaml`
3. Create a role to allow secret reading `kubectl apply -f secret-reader-role.yaml`
4. Create a role binding to bind the role to the service user. `kubectl apply -f secret-reader-role-binding.yaml`

### Deploying / upgrading Jenkins / plugin

1. Build the plugin (`mvn verify`) (from the root of the repository)
2. build and tag the docker image
   ```
      docker build ../.. -f Dockerfile -t jenkins-k8s-creds
   ```
   e.g.
   ```
      docker build ../.. -f Dockerfile -t eu.gcr.io/myproject/jenkins-k8s-creds
   ```
3. push the docker image to the docker repo (specified in the app yaml)
   ```
      docker push [HOSTNAME]/[PROJECT-ID]/[IMAGE][:TAG]
   ```
   e.g.
   ```
      docker push eu.gcr.io/myproject/jenkins-k8s-creds      
   ```
4. deploy the application  `kubectl apply -f jenkins-kube-creds.yaml`
5. deploy service so that Jenkins is exposed (optional and one time only)  `kubectl apply -f service.yaml`

Note: [this page](https://cloud.google.com/container-registry/docs/pushing-and-pulling) is useful for setting up auth to push to GKE
In short: `gcloud docker -- push <image>`

## Documentation

Documentation can be generated locally for testing using `bundle exec jekyll serve` once [Jekyll](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/) is installed.
