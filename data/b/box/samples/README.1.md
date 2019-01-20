# box-java-servlet-skeleton-app

## Prerequisites

In order to run this example you will need to have Maven installed. On a Mac, you can install Maven with [brew](http://brew.sh/):

```sh
brew install maven
```

Check that your maven version is 3.0.x or above:
```sh
mvn -v
```

#### Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files
*Note: If you utilize the Docker container contained in this project, you won't need to alter the installed Java version on your local machine.*

If you don't install this, you'll get an exception about key length. This is not a Box thing, this is a U.S. Government requirement concerning strong encryption. Please follow the instructions *exactly*.
> [Java 7 installer](http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html)

> [Java 8 installer](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)

### Configuration
#### Box Platform Configuration
#### Step 1. Create a Box Application
1. Sign up for a [free Box Developer account](https://account.box.com/signup/n/developer) or log in to the [Box Developer Console](https://app.box.com/developers/console).
2. Select "Create New App".
    * Select "Custom App" and click "Next".
    * Select "OAuth 2.0 with JWT (Server Authentication)" and click "Next".
    * Name the application "Box Java Servlet Sample - YOUR NAME".
        * *Application names must be unique across Box.*
    * Click "Create App" and then "View Your App".
3. Click "Generate a Public/Private Keypair".
    * *You may need to enter a 2-factor confirmation code.*
    * Save the JSON config file -- this config file also contains the private key generated for your application.
        * *Note: Box does not store the generated private key and this config file is the only copy of the private key. You can always delete this keypair from your application and generate a new keypair if you lose this config file.*
4. Be sure to add your configuration file to the root of this project directory.
5. In the "CORS Allowed Origins" section, add `http://localhost:8080`.

#### Step 2. Authorize the Application in Your Box Account
1. In a new tab, log in to your Box account with the admin account and go to the Admin Console.
    * Applications that use Server Authentication must be authorized by the admin of the account.
    * Signing up for a [free Box Developer account](https://account.box.com/signup/n/developer) gives you access to a Box Enterprise.
2. Under the gear icon, go to Enterprise Settings (or Business Settings, depending on your account type).
3. Navigate to the Apps tab.
4. Under "Custom Applications", click "Authorize New App".
5. Enter the "Client ID" value from your Box application in the "API Key" field.
    * Your application is now authorized to access your Box account.

##### Step 3. Add Configuration File to the Java App
1. Add your generated Box config file to the root of this project and name the file `config.json`.

#### Auth0 Configuration
Additionally, since you manage the identity and authorization for your Box App Users within your Java application, you'll need an identity service to fully utilize JWT authentication on behalf of your App Users.

For that reason, we've included the needed code and setup for an identity service provider named Auth0. You'll need to sign up for a free Auth0 account.

##### Step 1. Sign Up for a Free Auth0 Account and Configure Your First Client.
1. Sign up for a free trial account at [Auth0's site](https://auth0.com/).
2. You can optionally view their setup and quickstart materials by selecting **Web App** from their [documentation page](https://auth0.com/docs).
3. Navigate to the [clients page](https://manage.auth0.com/#/clients). You should automatically have a client name **Default**.
4. In the "Allowed Callback URLs" section, add `http://localhost:8080/callback`.
5. Retrieve the following values:
    * Domain
    * Client ID
    * Client Secret

#### Step 2. Add Auth0 Configuration Values to the Java application.
1. Navigate to `box-java-servlet-skeleton-app` > `src` > `main` > `webapp` > `WEB-INF` > `web.xml`
2. In the `web.xml` file, in the `<!-- Auth0 Configuration -->` section, find each value you retrieved from the Auth0 client in the previous step.
3. In the `<param-value>` portion of each setting, replace with the values you retrieved from your default Auth0 client.


### Build and Run

In order to build and run the project locally, you must execute:
```sh
mvn clean install org.mortbay.jetty:jetty-maven-plugin:run
```

If you have Docker installed, you can run the following to use the Docker configuration included in this repo:
```sh
mvn clean package
docker-compose up --build
```

Then, go to [http://localhost:8080/login](http://localhost:8080/login).

Support
-------

Need to contact us directly? You can post to the
[Box Developer Forum](https://community.box.com/t5/Developer-Forum/bd-p/DeveloperForum).

Copyright and License
---------------------

Copyright 2017 Box, Inc. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
   Unlimited Strength Java(TM) Cryptography Extension Policy Files
  for the Java(TM) Platform, Standard Edition Runtime Environment 8

                               README

----------------------------------------------------------------------
CONTENTS
----------------------------------------------------------------------

     o Introduction
     o License and Terms
     o Understanding The Export/Import Issues
     o Where To Find Documentation
     o Installation
     o Questions, Support, Reporting Bugs


----------------------------------------------------------------------
Introduction
----------------------------------------------------------------------

Thank you for downloading the Unlimited Strength Java(TM) Cryptography
Extension (JCE) Policy Files for the Java(TM) Platform, Standard
Edition (Java SE) Runtime Environment 8.

Due to import control restrictions of some countries, the version of
the JCE policy files that are bundled in the Java Runtime Environment,
or JRE(TM), 8 environment allow "strong" but limited cryptography to be
used. This download bundle (the one including this README file)
provides "unlimited strength" policy files which contain no
restrictions on cryptographic strengths.

Please note that this download file does NOT contain any encryption
functionality as all such functionality is contained within Oracle's
JRE 8. This bundles assumes that the JRE 8 has already been installed.


----------------------------------------------------------------------
License and Terms
----------------------------------------------------------------------

This download bundle is part of the Java SE Platform products and is
governed by same License and Terms notices. These notices can be found
on the Java SE download site:

    http://www.oracle.com/technetwork/java/javase/documentation/index.html


----------------------------------------------------------------------
Understanding The Export/Import Issues
----------------------------------------------------------------------

JCE for Java SE 8 has been through the U.S. export review process.  The
JCE framework, along with the various JCE providers that come standard
with it (SunJCE, SunEC, SunPKCS11, SunMSCAPI, etc), is exportable.

The JCE architecture allows flexible cryptographic strength to be
configured via jurisdiction policy files. Due to the import
restrictions of some countries, the jurisdiction policy files
distributed with the Java SE 8 software have built-in restrictions on
available cryptographic strength. The jurisdiction policy files in this
download bundle (the bundle including this README file) contain no
restrictions on cryptographic strengths.  This is appropriate for most
countries. Framework vendors can create download bundles that include
jurisdiction policy files that specify cryptographic restrictions
appropriate for countries whose governments mandate restrictions. Users
in those countries can download an appropriate bundle, and the JCE
framework will enforce the specified restrictions.

You are advised to consult your export/import control counsel or
attorney to determine the exact requirements.


----------------------------------------------------------------------
Where To Find Documentation
----------------------------------------------------------------------

The following documents may be of interest to you:

    o  The Java(TM) Cryptography Architecture (JCA) Reference Guide at:

       http://docs.oracle.com/javase/8/docs/technotes/guides/security

    o  The Java SE Security web site has more information about JCE,
       plus additional information about the Java SE Security Model.
       Please see:

       http://www.oracle.com/technetwork/java/javase/tech/index-jsp-136007.html


----------------------------------------------------------------------
Installation
----------------------------------------------------------------------

Notes:

  o Unix (Solaris/Linux/Mac OS X) and Windows use different pathname
    separators, so please use the appropriate one ("\", "/") for your
    environment.

  o <java-home> (below) refers to the directory where the JRE was
    installed. It is determined based on whether you are running JCE
    on a JRE or a JRE contained within the Java Development Kit, or
    JDK(TM). The JDK contains the JRE, but at a different level in the
    file hierarchy. For example, if the JDK is installed in
    /home/user1/jdk1.8.0 on Unix or in C:\jdk1.8.0 on Windows, then
    <java-home> is:

        /home/user1/jdk1.8.0/jre           [Unix]
        C:\jdk1.8.0\jre                    [Windows]

    If on the other hand the JRE is installed in /home/user1/jre1.8.0
    on Unix or in C:\jre1.8.0 on Windows, and the JDK is not
    installed, then <java-home> is:

        /home/user1/jre1.8.0               [Unix]
        C:\jre1.8.0                        [Windows]

  o On Windows, for each JDK installation, there may be additional
    JREs installed under the "Program Files" directory. Please make
    sure that you install the unlimited strength policy JAR files
    for all JREs that you plan to use.


Here are the installation instructions:

1)  Download the unlimited strength JCE policy files.

2)  Uncompress and extract the downloaded file.

    This will create a subdirectory called jce.
    This directory contains the following files:

        README.txt                   This file
        local_policy.jar             Unlimited strength local policy file
        US_export_policy.jar         Unlimited strength US export policy file

3)  Install the unlimited strength policy JAR files.

    In case you later decide to revert to the original "strong" but
    limited policy versions, first make a copy of the original JCE
    policy files (US_export_policy.jar and local_policy.jar). Then
    replace the strong policy files with the unlimited strength
    versions extracted in the previous step.

    The standard place for JCE jurisdiction policy JAR files is:

        <java-home>/lib/security           [Unix]
        <java-home>\lib\security           [Windows]


-----------------------------------------------------------------------
Questions, Support, Reporting Bugs
-----------------------------------------------------------------------

Questions
---------

For miscellaneous questions about JCE usage and deployment, we
encourage you to read:

    o Information on the Java SE Security web site

      http://www.oracle.com/technetwork/java/javase/tech/index-jsp-136007.html

    o The Oracle Online Community Forums, specifically the Java
      Cryptography forum. The forums allow you to tap into the
      experience of other users, ask questions, or offer tips to others
      on a variety of Java-related topics, including JCE. There is no
      fee to participate.

      http://forums.oracle.com/
      http://forums.oracle.com/forums/forum.jspa?forumID=964  (JCE
      forum)


Support
-------

For more extensive JCE questions or deployment issues, please contact
our Technical Support staff at:

    http://support.oracle.com


Reporting Bugs
--------------

To report bugs (with sample code) or request a feature, please see:

    http://bugs.sun.com/
    http://bugreport.sun.com/bugreport/

Bug reports with specific, reproducible test cases are greatly
appreciated!
