# NodePool plugin

This repository contains a Jenkins plugin to perform builds on cloud instance  nodes sourced
from [NodePool](https://docs.openstack.org/infra/nodepool/).

## Pipeline Steps
### nodePoolHold
This step allows a user to hold the current node from within a job, assuming
the current node is a node pool node.

Usage:
```
    node("nodepool-debian"){
        nodePoolHold() // hold for one day
        nodePoolHold(duration: "1w") // hold for one week
        nodePoolHold(duration: "1w", reason: "Investigating issue IS-123") // specify reason
    }
```
The hold end time will be calculated from the specified duration
and is visible on the Computer page in the Jenkins UI for each
nodepool node. The reason is also visible in the same place.

## Structure

The implementation consists of a listener class that creates agents (slaves) when a item with a
matching label enters the Jenkins build queue.  There is also another listener that releases each
node after it is used once.

## Building Prerequisites

To build the NodePool plugin from the source, the following tools are needed:

* Java JDK 8
* Apache Maven 3.x

## Building

To build the project from source, run the following command:

```bash
mvn clean compile test findbugs:findbugs
```

It's highly recommended to run the `findbugs` target to discover any issues prior to submitting a pull request.  The 
Jenkins CI system will run the `findbugs` target anyway, but it's convenient to catch the issues early. The
`findbugs:gui` target will launch a tool to display any errors - otherwise the results will be in the `target` folder. 
The CI system uses a more elaborate command line (which may change in the future). Here's an example:

```bash
mvn --batch-mode \
  --errors \
  -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn \
  --update-snapshots \
  -Dmaven.test.failure.ignore \
  clean install
```

To generate the `hpi` installation file for Jenkins, run:

```bash
mvn hpi:hpi
```
 
## Running

To launch Jenkins with the NodePool plugin from the command line, run:

```bash
mvn hpi:run
```

## Releasing

The following are instructions to release a new version of the plugin so it will appear as an available plugins under `Manage Plugins` in the Jenkins UI.  For more information, see [here](https://wiki.jenkins.io/display/JENKINS/Hosting+Plugins#HostingPlugins-Releasingtojenkins-ci.org).

Steps:

1. Edit `~/.m2/settings.xml` to add your [Jenkins CI](https://accounts.jenkins.io/login) username and password.  Add this block to the XML:

  ```xml
  <servers>
    <server>
      <id>maven.jenkins-ci.org</id> <!-- For parent 1.397 or newer; this ID is used for historical reasons and independent of the actual host name -->
      <username>username</username>
      <password>password</password>
    </server>
  </servers>
  ```

2. Confirm the `pom.xml` in the master branch of the repository has a tag containing `SNAPSHOT`.

3. Run the maven release plugin: `mvn [-B] mvn release:prepare release:perform`
  * The `-B` flag is optional to accept all default choices.
 
4. After this completes, edit the wiki to add a new version to the history [here](https://wiki.jenkins.io/display/JENKINS/NodePool+Agents+Plugin).

### The maven release plugin will do the following:

* Run unit tests
* Build a new plugin version
* Upload the new plugin artifact to the maven repository [here](https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/nodepool-agents/).
* Tag git with the new plugin version.
* Update the git master branch `pom.xml` with a SNAPSHOT tag representing the next (unreleased) development version.

### Availability
* [The new plugin version will *not* be instantly available for use in the Jenkins UI under `Manage Plugins`](https://wiki.jenkins.io/display/JENKINS/Hosting+Plugins#HostingPlugins-Help!Mypluginisnotshowingupintheupdatecenter).
* It will take a maximum of **8 hours** for the new version to appear in the [json file](https://updates.jenkins-ci.org/current/update-center.json) that the UI consumes.
* Once the version is listed in the `update-center.json` file, it should be available to install in the UI.  You may need to click `Check Now` to update the list of available plugins.

### Experimental Versioning

**NOTE**  that installation of experimental plugins in Jenkins seems to be broken!

  * Trying to change the update center URL fails with error: `None of the tool installer metadata passed the signature check`
  * See [https://issues.jenkins-ci.org/browse/INFRA-1051](https://issues.jenkins-ci.org/browse/INFRA-1051).
    
#### Releasing experimental plugins

To release an experimental version of a plugin, put *alpha* or *beta* in the version string.

#### Installing experimental plugins

*(Assuming the above issue gets fixed)*

To install an experimental plugin:

* Go to `Manager Plugins`
* Click `Advanced`
* Enter [http://updates.jenkins-ci.org/experimental/update-center.json](http://updates.jenkins-ci.org/experimental/update-center.json) in the `Update Site` URL field.

Full details on experimental plugins are [here](https://jenkins.io/blog/2013/09/23/experimental-plugins-update-center/).

