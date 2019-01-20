# Hibernate ORM OSGi Tutorial: Unmanaged JPA

This tutorial demonstrates the use of Hibernate's "unmanaged JPA" configuration in your OSGi container.  Unlike
"managed JPA", which uses Enterprise OSGi JPA (ie, Apache Aries JPA) to manage the EntityManagerFactory, the client
bundle is instead in charge of creating it manually.

This tutorial also demonstrates how to register custom impls of Hibernate ORM extension points, registered through the
use of OSGi Blueprint (blueprint.xml).

## Running the Tutorial

To run the tutorial, use the following commands in the Karaf console:

- feature:repo-add mvn:org.hibernate/hibernate-osgi/[VERSION]/xml/karaf
- feature:install hibernate-orm
- feature:repo-add file:/[PATH]/hibernate-demos/hibernate-orm/osgi/unmanaged-jpa/features.xml
- feature:install hibernate-osgi-unmanaged-jpa

Note that this project is not deployed in Hibernate's Nexus group, so it must be built and installed to your local
repo.  Then take a look at Karaf's etc/org.ops4j.pax.url.mvn.cfg local Maven settings, in order for it to find the
artifacts in the local repo.
# Hibernate ORM OSGi Tutorial: Managed JPA through Enterprise OSGi JPA

This tutorial demonstrates the use of Enterprise OSGi JPA to create a "managed JPA" environment in your OSGi container.
More specifically, this is based on Apache Karaf 3.0.4 and Apache Aries JPA.  See the Hibernate ORM User Guide's OSGi
chapter for more information!

## Running the Tutorial

To run the tutorial, use the following commands in the Karaf console:

- feature:repo-add mvn:org.hibernate/hibernate-osgi/[VERSION]/xml/karaf
- feature:install hibernate-orm
- feature:repo-add file:/[PATH]/hibernate-demos/hibernate-orm/osgi/managed-jpa/features.xml
- feature:install hibernate-osgi-managed-jpa

IMPORTANT: You'll also need to update the following path within this demo's features.xml:

\<bundle\>blueprint:file:/[PATH]/datasource-h2.xml\</bundle\>

Note that this project is not deployed in Hibernate's Nexus group, so it must be built and installed to your local
repo.  Then take a look at Karaf's etc/org.ops4j.pax.url.mvn.cfg local Maven settings, in order for it to find the
artifacts in the local repo.
# Hibernate ORM OSGi Tutorial: Unmanaged Native

This tutorial demonstrates the use of Hibernate's "unmanaged native" configuration in your OSGi container.  In this
configuration, the client bundle is in charge of manually creating the Hibernate SessionFactory, instead of using JPA.

This tutorial also demonstrates how to register custom impls of Hibernate ORM extension points, registered through the
use of OSGi Blueprint (blueprint.xml).

## Running the Tutorial

To run the tutorial, use the following commands in the Karaf console:

- feature:repo-add mvn:org.hibernate/hibernate-osgi/[VERSION]/xml/karaf
- feature:install hibernate-orm
- feature:repo-add file:/[PATH]/hibernate-demos/hibernate-orm/osgi/unmanaged-native/features.xml
- feature:install hibernate-osgi-unmanaged-native

Note that this project is not deployed in Hibernate's Nexus group, so it must be built and installed to your local
repo.  Then take a look at Karaf's etc/org.ops4j.pax.url.mvn.cfg local Maven settings, in order for it to find the
artifacts in the local repo.# Setting up the environment

## Services

Install docker and docker-compose, then run this from the root of the project:

```
sudo docker-compose -f environment-stack.yml -p hsearch-elasticsearch-wikipedia up
```

You can later remove the created services and volumes with this command:

```
sudo docker-compose -f environment-stack.yml -p hsearch-elasticsearch-wikipedia down -v
```

## Data

You can try a fully automated initialization using this command:

```
./src/init/init
```

If this succeeds, you're all set, you can go to the next step.

Otherwise, Wikipedia's dumps page structure probably changed, but you can proceed as explained below.

Retrieve a dataset of current pages (one of those described as "All pages, current versions only.")
from [Wikipedia's dumps page](https://dumps.wikimedia.org/enwiki/) (or a [mirror](https://dumps.wikimedia.org/mirrors.html)).

Example: `enwiki-20170220-pages-meta-current1.xml-p000000010p000030303.bz2`

Extract the dump:

```
bunzip2 <the dump>
```

Initialize the database using the provided script:

```
./src/init/init -f <path to the uncompressed dump>
```

# Running the project

You must have [Maven (`mvn`)](https://maven.apache.org/) in your path, version 3.2 or later.
You must use Java 8.

Execute the following command:

```
mvn clean spring-boot:run
```

You can trigger reindexing with:

```
curl -XPOST http://localhost:8080/admin/reindex
```

The progress will be updated in the application logs.

Then you can query the index with:

```
curl http://localhost:8080/page/search/?q=<sometext>
```

For instance:

```
curl http://localhost:8080/page/search/?q=car
```

Finally, you can retrieve a page with:

```
curl http://localhost:8080/page/<page ID>/
```

## Other implementations

Alternative implementations of the search are demonstrated in previous commit.

See the git history and check out the relevant commit to see those implementations in action:

 * Naïve SQL implementation with `ILIKE`
 * Embedded Lucene implementation 

# hibernate-ogm-hiking-demo

This is a demo project used for the talk [Hibernate OGM: Talking to NoSQL in Red Hat JBoss EAP](http://www.redhat.com/summit/sessions/index.html#274) presented at Red Hat Summit 2014. It shows how to use MongoDB as data store in a Java EE application through JPA / Hibernate OGM.

The application allows to manage (create, list, update, delete) hikes. It exposes a REST API using JAX-RS. The web client is built using AngularJS and invokes this API to display/update the data.

## Building the project

Execute the following command to build the project:

    mvn clean install

This will execute some simple JUnit tests which use JPA's RESOURCE_LOCAL mode to access the datastore as well as some integration tests which run on the application server (executed via Arquillian) using the JTA mode. This requires a MongoDB server to be installed and running locally.

By default, the integration tests are executed on the WildFly 8 application server, which is downloaded, unzipped, updated with the required modules for Hibernate OGM and started automatically.

Alternatively, you can execute the integration tests on a locally installed instance of JBoss EAP 6. To do so, get the ZIP archive with the required modules of Hibernate OGM from [here](https://repository.jboss.org/nexus/content/groups/public/org/hibernate/ogm/hibernate-ogm-modules-eap6/) and unzip it into the modules directory of the JBoss EAP installation. Then start the server and run the following command:

    mvn clean install -Peap-remote

## Deploying the application on a local application server

To deploy the application on a local application server (which must have been started before), run the following command for WildFly 8:

    mvn wildfly:deploy -DskipTests=true

And the following to deploy to JBoss EAP:

    mvn jboss-as:deploy -DskipTests=true

In both cases you can access the application at the following URL once the deployment has finished:

    http://localhost:8080/hibernate-ogm-hiking-demo-1.0-SNAPSHOT/hikes.html

You can then create hikes with sections and organizers. You also can search for hikes. Currently the UI does not allow to create persons which can be referenced from hikes. But there is a REST call for this, so you can e.g. use curl to create persons as follows:

    curl -X POST -d '{"name":"Bob"}' -H "Accept: application/json" -H "Content-type: application/json" http://localhost:8080/hibernate-ogm-hiking-demo-1.0-SNAPSHOT/hiking-manager/persons

## Deploying the application on OpenShift

The demo is prepared to be deployed and run on Red Hat's platform-as-a-service, OpenShift.

This requires an OpenShift application to be set up with the JBoss EAP 6 cartridge and the MongoDB cartridge. Refer to the official documentation for instructions how to set up an application. You also need to add the application's git repository on OpenShift as a remote to your copy of the project.

The project contains the required modules for Hibernate OGM in the _.openshift/config/modules/_ folder; They will be added automatically to the server's module path upon start-up. In order to configure the database credentials, you need to log into your instance via SSH and run the following command once:

    echo "-Dhibernate.ogm.datastore.host=$OPENSHIFT_MONGODB_DB_HOST \
        -Dhibernate.ogm.datastore.port=$OPENSHIFT_MONGODB_DB_PORT \
        -Dhibernate.ogm.datastore.username=$OPENSHIFT_MONGODB_DB_USERNAME \
        -Dhibernate.ogm.datastore.password=$OPENSHIFT_MONGODB_DB_PASSWORD \
        -Dhibernate.ogm.datastore.database=ogm" \
        > .env/user_vars/JAVA_OPTS_EXT

OpenShift makes MongoDB's host, user etc. available via environment variables. This command puts them into the _JAVA\_OPTS\_EXT_ variable which contains the VM arguments passed to the server upon startup. That way Hibernate OGM can access the credentials.

When you then have done a deployment (e.g. by pushing the application code to the OpenShift remote or through rhc), you can access the application in the Cloud at

    http://<%app-name%>-<%domain-name%>.rhcloud.com/hikes.html
    
Any feedback on the demo is highly welcome, just send a mail to the hibernate-dev mailing list.
For information about action hooks supported by OpenShift, consult the documentation:

https://github.com/openshift/origin-server/tree/master/node/README.writing_applications.md#action-hooks
Place your JBoss AS7 modules in this directory. This directory is added to the
module path of the AS7 server associated with your application. It has the
same structure as the standard AS7 modules directory.

The modules placed in this directory will be added to or override the default modules
provided by the OpenShift JBoss AS7 cartridge.

Scenarios:
1) Replace a default module with a new module that contains a bug fix or new feature
2) Add a module that does not exist in the base OpenShift AS7 cartridge in order to add
a new component. Typically these new modules will need to be enabled and configured in
standalone.xml

Unless one of the above scenarios is required there is no need to modify the 
modules directory.

NOTE: Replacing default modules as in scenario 1 can cause conflicts between modules so
should be done with caution and adequate testing.
Run scripts or jobs on a periodic basis
=======================================
Any scripts or jobs added to the minutely, hourly, daily, weekly or monthly
directories will be run on a scheduled basis (frequency is as indicated by the
name of the directory) using run-parts.

run-parts ignores any files that are hidden or dotfiles (.*) or backup
files (*~ or *,)  or named *.{rpmsave,rpmorig,rpmnew,swp,cfsaved}

The presence of two specially named files jobs.deny and jobs.allow controls
how run-parts executes your scripts/jobs.
   jobs.deny  ===> Prevents specific scripts or jobs from being executed.
   jobs.allow ===> Only execute the named scripts or jobs (all other/non-named
                   scripts that exist in this directory are ignored).

The principles of jobs.deny and jobs.allow are the same as those of cron.deny
and cron.allow and are described in detail at: 
   http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/ch-Automating_System_Tasks.html#s2-autotasks-cron-access

See: man crontab or above link for more details and see the the weekly/
     directory for an example.

PLEASE NOTE: The Cron cartridge must be installed in order to run the configured jobs.
Run scripts or jobs on a weekly basis
=====================================
Any scripts or jobs added to this directory will be run on a scheduled basis
(weekly) using run-parts.

run-parts ignores any files that are hidden or dotfiles (.*) or backup
files (*~ or *,)  or named *.{rpmsave,rpmorig,rpmnew,swp,cfsaved} and handles
the files named jobs.deny and jobs.allow specially.

In this specific example, the chronograph script is the only script or job file
executed on a weekly basis (due to white-listing it in jobs.allow). And the
README and chrono.dat file are ignored either as a result of being black-listed
in jobs.deny or because they are NOT white-listed in the jobs.allow file.

For more details, please see ../README.cron file.

# ThreeTen Extra Validator Example

This is a demo project used in the examples for the blog post
 [Adding custom constraint definitions via the Java service loader](http://in.relation.to/2017/03/02/adding-custom-constraint-definitions-via-the-java-service-loader/)
 It contains validators of `org.threeten.extra.YearQuarter` and `org.threeten.extra.YearWeek` types
 for `@Future` / `@Past` annotations.

## Building the project

Execute the following command to build the project:

    mvn clean install

This will execute some simple JUnit tests and package a jar file with constraint
validators implemented in this demo project.
# Java time Duration Validator Example

This is a demo project used in the examples for the blog post
 [Adding custom constraint definitions via the Java service loader](http://in.relation.to/2017/03/02/adding-custom-constraint-definitions-via-the-java-service-loader/).
 It contains a constraint annotation `@DurationMin` and corresponding validator for `java.time.Duration`.

## Building the project

Execute the following command to build the project:

    mvn clean install

This will execute some simple JUnit tests and package a jar file with constraint
validators implemented in this demo project.
# Updating Hibernate Validator in WildFly 10

This project shows how to use the patch file provided by Hibernate Validator to
update a given instance of WildFly to the latest Hibernate Validator and Bean
Validation modules.

It accompanies the blog post [Using Bean Validation 2.0 on WildFly 10](http://in.relation.to/2017/04/04/testing-bean-validation-2-0-on-wildfly-10/).

## Building the project

Execute the following command to build the project:

    mvn clean install

This will download WildFly 10.1, the Hibernate Validator 6 patch file, apply the
patch to the server and run a simple integration test using Bean Validation 2.0
functionality via Arquillian.
# Custom Bean Validation Value Extractors

This project shows how to implement custom value extractors for Bean Validation,
allowing to put constraints to the elements of Google Guava `Multimap` objects.

It accompanies the blog post [Putting Bean Validation Constraints to Guava's Multimap](http://in.relation.to/2018/02/26/putting-bean-validation-constraints-to-multimaps/).

## Building the project

Execute the following command to build the project:

    mvn clean install
# Hibernate Demo: Message Board
Data MicroService Demo.

Made with Hibernate ORM, Hibernate OGM and Infinispan for OpenShift Container Platform. 

## Installing the demo

### Pre-Requirement

* Java 8
* Maven 3+
* NPM (https://www.npmjs.com/)
* Angular Cli (npm install -g @angular/cli) [avoid 6.1.x]
* OpenShift (3.7+) client

### Build demo
----
mvn clean install -s settings.xml
----

### Install demo
----
cd script

( oc login -u [YOUR-USER-NAME] ) <<optional>>
( oc new-project [YOUR-PROJECT-NAME] ) <<optional>>

sh ./install-all.sh
----

## Additional scripts

If you need to update only some parts of the demo
you can use the following scripts:

### Update Account MicroService
----
cd script
sh ./binary-build-account.sh
----

### Update Message MicroService
----
cd script
sh ./binary-build-message.sh
----

### Update Web App
----
cd script
sh ./binary-build-web.sh
----

## Web [FORM]

[YOUR-USER-NAME] is your OCP username like **developer**
[YOUR-PROJECT-NAME] is your OCP project like **message-board**
[YOUR-IP] is a generate IP by OCP like **192.168.42.120**

----
http://web-message-board.[YOUR-IP].nip.io
----

click on __andrea__ or __fabio__

### Message MicroService [REST]
#### with proxy
----
http://web-message-board.[YOUR-IP].nip.io/message-service/messages?username=andrea
----
#### without proxy
----
http://message-service-message-board.[YOUR-IP].nip.io/message-service/messages?username=andrea
----

### Account MicroService [REST]
#### with proxy
----
http://web-message-board.[YOUR-IP].nip.io/account-service/user
----
#### without proxy
----
http://account-service-message-board.[YOUR-IP].nip.io/account-service/user
----

## Known Issues

### NodeJs module Angular cli 6.1.x
It seems there is an issue on angular-cli versions 6.1.0 and 6.1.1.
It might need to downgrade angular-cli version:
----
sudo -s npm uninstall -g @angular/cli
sudo -s npm install -g @angular/cli@6.0.8
----
For more information see https://github.com/angular/angular-cli/issues/11661[Issue Page].

### MiniShift CDK v3.5.0-1
Actually there is an issue with MiniShift v1.20.0+1bd6d5c, CDK v3.5.0-1.
The persistent volume for Infinispan server pod is mounted as root user.
# Micro Service: Post
# Micro Service: Account
