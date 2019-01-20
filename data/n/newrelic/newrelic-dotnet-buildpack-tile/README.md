---
# New Relic Dotnet Extension Buildpack for PCF (Public Beta)

---

<br/><br/>

<p class="note warning">
<strong>WARNING! </strong>
The first version of New Relic Dotnet Extension Buildpack for PCF was in private beta internally. It was used by New Relic and select number of customers before it was registered on PivNet. The product is currently in public beta and is intended for evaluation and testing purposes until further notice.
</p>



This document describes [New Relic Dotnet Extension Buildpack Tile for Pivotal Cloud Foundry (PCF)](https://network.pivotal.io/products/newrelic-dotnet-buildpack/) and instructions on how to install and use New Relic's Dotnet extension tile to bind New Relic agents to Dotnet Core or Dotnet Framework applications to monitor them in [Pivotal Cloud Foundry](https://pivotal.io/platform) (PCF) environment.

<br/>

<center>
    <img src="images/nr-black-256x256.png" alt="New Relic Dotnet Extension Buildpack" height="150" width="150"/>
</center>

<br/>


## <a id='overview'></a> Overview

New Relic Dotnet Extension Buildpack for PCF enables you to bind your Dotnet (Core and Framework) applications to New Relic Dotnet agents, and monitor the health and performance of these applications, analyze the data captured by agents, and aditionally correlate the captured agent data with PCF infrastructure which is collected by [New Relic Firehose Nozzle](https://network.pivotal.io/products/nr-firehose-nozzle/).

The extension buildpacks could be installed using the tile in OpsMgr, or alternatively you could extract the <strong>".pivotal"</strong> file, and install individual extension buildpack(s) using CF CLI command <strong>"cf create-buildpack"</strong> as you wish. 

Once you start monitoring your applications, you would also have the ability to set alerts based on any metrics that are collected by Dotnet agents using New Relic's alerting subsystem.


The tile installs one or more of the following 4 buildpacks depending on the tile configuration:

1. New Relic Dotnet Core Extension Buildpack for Dotnet Core Applications (Ubuntu Trusty & xenial)
1. New Relic Dotnet Core Extension Cached Buildpack for Dotnet Core Applications (Ubuntu Trusty & xenial) running in disconnected (isolated) PCF deployments
1. New Relic HWC  Extension Cached Buildpack for Dotnet Framework Applications (Windows 2012 R2 & Windows 2016)
1. New Relic HWC  Extension Buildpack for Dotnet Framework Applications (Windows 2012 R2 & Windows 2016) running in disconnected (isolated) PCF deployments

The first 2 extension buildpacks are for Dotnet Core applications running on Ubuntu Trusty (14.04) and Ubuntu Xenial (16.04). The first extension is non-cached, and the second one is cached version of buildpack for Dotnet Core.

The 3rd and 4th buildpacks are HWC extensions for Windows 2012 R2 and Windows 2016. The third extension is non-cached, and the fourth one is cached version of HWC extension buildpacks.

All 4 buildpacks use the multi-buildpack approach of Cloud Foundry and require either the standard Dotnet Core buildpack or HWC buildpack to be specified in the buildpack chain, either in application's manifest or in the CF CLI command line.



<br/>


## <a id="snapshot"></a> Product Snapshot

The following table provides version and version-support information about New Relic Dotnet Extension Buildpack for PCF.

<table class="nice">
    <th>Element</th>
    <th>Details</th>
    <tr>
        <td>Tile version</td>
        <td>1.0.1</td>
    </tr>
    <tr>
        <td>Release date</td>
        <td>November 8, 2018</td>
    </tr>
    <tr>
        <td>Software component version</td>
        <td>New Relic Dotnet Extension Buildpack v1.0.1 (Public Beta)</td>
    </tr>
    <tr>
        <td>Compatible Ops Manager version(s)</td>
        <td>v2.1.x, v2.2.x, and v2.3.x</td>
    </tr>
    <tr>
        <td>Compatible Pivotal Application Service versions</td>
        <td>v2.1.x, v2.2.x, and v2.3.x</td>
    </tr>
    <tr>
        <td>IaaS support</td>
        <td>AWS, GCP, Azure, and vSphere</td>
    </tr>
</table>


## <a id='compatibility'></a> Compatibility

This product has been tested and is compatible with PCF versions v2.1.x and above.


## <a id="reqs"></a> Requirements

As prerequisite you need to have the following
* An active New Relic account with a license key which is used to bind Dotnet applications to New Relic Dotnet agents.
* In order to use [multi-buildpacks in the application's manifest file](https://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html#buildpack), at a minimum you need to upgrade CF CLI to <strong>version 6.38</strong>.
* Dotnet HWC extension requires a minimum version of hwc buildpack 3.0.3.
* Dotnet Core extension requires a minimum version of dotnet core buildpack 2.1.5.


## <a id='trial'></a> Trial License

If you do not already have a New Relic account, you can obtain an account with [60-day free trial license](http://newrelic.com/signup?funnel=pivotal-cloud-foundry&partner=Pivotal+Cloud+Foundry&product_id=Standard&promo_code=PVCF60PRO).


## <a id="feedback"></a> Feedback

If you have feature requests, questions, or information about a bug, please submit an issue [on github](https://github.com/newrelic/newrelic-dotnet-buildpack-tile/issues).

<br/><br/><br/>
---
---
---
---
---
# Installing and Configuring New Relic Dotnet Extension Buildpack

---

This topic describes how to the installation and configuration of New Relic Dotnet Extension Buildpack(s) for Pivotal Cloud Foundry (PCF).

You can either install the buildpacks as a tile in Ops Manager, or push them individually as a separate buildpacks using CF CLI.


## <a id='install-opsmgr'></a> Install and Configure Dotnet Extension as a Tile in Ops Manager

1. Download the latest version of the tile (currently <strong>"newrelic-dotnet-buildpack-1.0.1.pivotal"</strong>) from [PivNet](https://network.pivotal.io/products/newrelic-dotnet-buildpack), or from New Relic's github repo under [releases](https://github.com/newrelic/newrelic-dotnet-buildpack-tile/releases).
1. Navigate to Ops Manager Installation Dashboard and click <strong>Import a Product</strong> to upload the product file.
1. Under the <strong>Import a Product</strong> button, click the <strong>"+"</strong> sign next to the version number of <strong>New Relic Dotnet Buildpack for PCF</strong>. This adds the tile to your staging area.
1. Click the newly added <strong>New Relic Dotnet Buildpack for PCF</strong> tile.
1. Install and configure the tile in OpsMgr. you can accept the default values and install all 4 buildpacks in your PCF foundation, or in <strong>Tile Configuration->New Relic Buildpack Selection</strong> you could select the checkbox for any of the buildpacks that you wish to install.
1. If you make any configuration changes, click the <strong>"Save"</strong> button on each tab at the bottom of the page.
1. Go to <strong>Installation UI</strong> of OpsMgr.
1. Click on the blue button on top right of the installation UI to <strong>Apply changes</strong>.

<br/>

## <a id='install-buildpack'></a> Install and Configure Dotnet Extension with CF CLI

If you do not wish to install the tile, you could alternatively unzip the downloaded <strong>.pivotal</strong> file, and install the buildpack(s) which you need using CF CLI command <strong>"cf create-buildpack ..."</strong>.

1. Unzip <strong>"newrelic-dotnet-buildpack-tile-*.pivotal"</strong> into a separate subdirectory<br/>
```
    unzip newrelic-dotnet-buildpack-tile-*.pivotal -d buildpack_tile
```

2. Change directory to buildpack_tile/releases<br/>
```
    cd buildpack_tile/releases
```

3. Create a subdirectory (i.e. tmp)<br/>
```
    mkdir tmp
```

4. Extract the <strong>.tgz</strong> file in releases folder into the <strong>tmp</strong> directory<br/>
```
    tar xvf newrelic-dotnet-buildpack-tile-*.tgz -C tmp
```

5. Change directory to <strong>tmp/packages</strong><br/>
```
    cd tmp/packages
```

6. Extract any of the individual buildpack <strong>.tgz</strong> files using the following command<br/>
```
    tar xvf <BUILDPACK_NAME>.tgz
```

this will create a folder by the name of the buildpack, and the newly created folder contains the zipped version of the buildpack. 

7. Upload the zipped buildpack file using CF CLI's <strong>"cf create-buildpack"</strong> command
```
    cf create-buildpack <BUILDPACK_NAME> <ZIPPED_BUILDPACK_NAME.zip> 99
```



<br/>


## <a id='buildpack-build-deploy'></a> Buildpack Build and Deploy Process


### <a id='build'></a> Build
The buildpacks in this tile are already built and ready to be used in Cloud Foundry. However, if you'd like to make changes to the buildpack, or update the cahced version of any buildpacks with newer version of dependencies, you could build your own copy. Please follow the instructions below to build your own copy of the buildpack(s):

1. Clone the buildpack repo to your system<br/>
``` 
git clone https://github.com/newrelic/newrelic-dotnetcore-extension-buildpack
or https://github.com/newrelic/newrelic-hwc-extension-buildpack
```

2. Change directory to the cloned buildpack

3. Source the <strong>.envrc</strong> file in the buildpack directory.
```
source .envrc
```

4. Install <strong>buildpack-packager</strong>
```
./scripts/install_tools.sh
```

5. Build the buildpack
```bash
buildpack-packager build [ --cached ] -any-stack
```


<br/>

### <a id='deploy'></a> Deploy

To deploy and use the buildpack in Cloud Foundry
Upload the buildpack to your Cloud Foundry and optionally specify it by name usinf CF CLI

```
cf create-buildpack [NEWRELIC_DOTNET_CORE_EXTENSION_BUILDPACK] [BUILDPACK_ZIP_FILE_PATH] 99
cf push my_app -b NEWRELIC_DOTNET_CORE_EXTENSION_BUILDPACK   -b DOTNET_CORE_BUILDPACK
```
<strong>Note:</strong> to create the HWC extension change the names from <strong>CORE</strong> to <strong>HWC</strong>.



<br/><br/><br/>
---
---
---
---
---
# Using New Relic Dotnet Extension Buildpack for PCF

---

This topic describes how to use New Relic Dotnet Buildpacks for Pivotal Cloud Foundry (PCF).


## <a id='using'></a> Using New Relic Dotnet Extension

New Relic extension buildpacks allow you to use Dotnet agents in various ways to make it easy and convenient for users to bind to New Relic service.

<br/>


### <a id='how-it-works'></a> How the Extension Buildpack Works

The buildpack extensions bind to New Relic Dotnet agent using one of the following ways as fits in your environment:

1. If an environment variable named <strong>"NEW_RELIC_DOWNLOAD_URL"</strong> is defined in the application's environment (manifest file, cf set-env, or set in AppsMgr), its value is used as the location to download the agent. This is used for environments where you have your own repository for downloading dependencies (i.e. Artifactory). If a second environment variable called <strong>"NEW_RELIC_DOWNLOAD_SHA256"</strong> is set in the application environment, it is expected to hold the downloaded agent's binary file SHA256 checksum. In this case the SHA256 checksum of the downloaded agent binary file is compared with this value, and in case of mismatch, the buildpack reports an error.

1. You could create a cached version of the buildpack using the <strong>"--cached"</strong> switch with New Relic agent embedded in the buildpack. This is mainly used in disconnected (isolated) environments where PCF does not have access to the outside world, and the buildpack cannot download the agent from New Relic's download site.

1. Use a specific version of New Relic agent by specifying the version in the buildack's manifest file at the time of packaging.

1. Set the version of the agent to <strong>"0.0.0.0"</strong>, <strong>"latest"</strong>, or <strong>"current"</strong> in buildpack's manifest file to download the latest version of the agent.

Except in the first case when the download url is specified, but sha-256 code is not available, in all other cases the buildpack checks the SHA256 checksum of the downloaded (or copied) agent to validate the download.

We always encourage you to use the latest version of New Relic agents unless there is a reason that keeps you from upgrading to newer releases of the agent.


<br/>


### <a id='precedence'></a> Order of Precedence

The order of precedence for which method to use to obtain New Relic agent is from the top to bottom. If <strong>"NEW_RELIC_DOWNLOAD_URL"</strong> is specified, it precedes the other options. If this environment variable is not specified, the cached buildpack takes precedence. Otherwise, the <strong>"version"</strong> property of the agent in the buildpack's manifest is used, and one of the other two options is used to download the agent, depending on the value of <strong>"version"</strong> property of the agent dependency (explicit version or "latest").



## <a id='how-it-operates'></a> How The Extension Buildpack Binds the Apps to New Relic Agent
The buildpack looks for several environment variables and files to determine how to bind the application to the agent.


### <a id='license-key'></a> Bind the Application to New Relic Agent
The license key for New Relic account must be specified in one of the following ways:<br/><br/>
* NEW_RELIC_LICENSE_KEY env var<br/>
* License key from User-Provided-Service<br/>
* License key from Service Broker Tile in Marketplace<br/>
* License key from newrelic.config<br/>

<strong>Note:</strong> environment variables override all other options.


### <a id='app-name'></a> Application Name in New Relic UI
The application name for New Relic is determined in the following order:<br/><br/>
* NEW_RELIC_APP_NAME env var<br/>
* App name from User-Provided-Service<br/>
* App name from PCF<br/>
* <strong>Note</strong> that currently App name in newrelic.config file is not used<br/>


### <a id='agent-config'></a> New Relic Agent Configuration File
New Relic configuration file (<strong>"newrelic.config"</strong>) would allow you to set a number of agent properties, and change the behavior of the agent as you wish. Refer to [.NET agent configuration](https://docs.newrelic.com/docs/agents/net-agent/configuration/net-agent-configuration) for more information on configuring the agent. You could make a copy of this file into the application's root directory, and change any of agent's settings. The buildpack looks for the agent's config file in the following order:<br/><br/>
* App root folder<br/>
* Buildpack folder<br/>
* Agent folder<br/>


### <a id='ups'></a> New Relic User-Provided-Services
If the application binds to a User-Provided-Service with the word <strong>"newrelic"</strong> as part of its name, the buildpack sets the credentials from this service in the application environment by setting environment variable for known New Relic properties. The known properties currently are:<br/><br/>
* NEW_RELIC_LICNESE_KEY<br/>
* NEW_RELIC_APP_NAME<br/>
* NEW_RELIC_DISTRIBUTED_TRACING_ENABLED<br/>


### <a id='proxy'></a> Use of Proxy
If you're using a proxy server in your environment, you need to make a copy of <strong>"newrelic.config"</strong> file of the agent in the application directory, and specify the [proxy information](https://docs.newrelic.com/docs/agents/net-agent/configuration/net-agent-configuration#proxy) as a child of the <strong>&lt;service&gt;</strong> element.<br/>
<strong>Example:</strong><br/>
<pre>
    &lt;service licenseKey="0123456789abcdef0123456789abcdef01234567"&gt;
      &lt;proxy name="my.proxy.address" port="proxy.port" /&gt;
    &lt;/service&gt;
</pre>




## <a id='tips-tricks'></a>Tips & Tricks

### <a id='using-nr-agent'></a>Using New Relic Agent

You need to specify a New Relic account <strong>license key</strong> in one of the following ways in order to bind your application to New Relic service:

* Bind your application to New Relic using a License Key

    The quickest and easiest way to bind your app to New Relic Dotnet agent is using the license key environment variable (<strong>"NEW_RELIC_LICNENSE_KEY"</strong>) and set it to your New Relic account's license key.

<br/>

* Bind your application to a local copy of New Relic Dotnet Agent

    If you are in a disconnected (isolated) environment, the easiest way is to obtain the latest version of New Relic Dotnet agent(s) from [New Relic download site](http://download.newrelic.com/dot_net_agent/) and upload them to your local repository (i.e. Artifactory). Then in the application's manifest file set <strong>"NEW_RELIC_DOWNLOAD_URL"</strong> environment variable to the  location of the agent download.


* Bind your application to New Relic using the Agent Tile in the Marketplace<br/>
    * From Marketplace<br/>
        - click on New Relic tile
        - select the plan that is associated with your new relic account (check with PCF admin)
        - specify the instance name
        - if you already have the application running on PCF you could specify the app name as well. Otherwise, once you push the app, from the app UI you could directly bind to an existing service instance (or create a new service instance)
        - click the <strong>CREATE</strong> button to create the service instance

        - once the service instance is created, you could also use the "services" stanza in your app manifest.yml file, and specify the name of the service you just created in the marketplace
        - restage the application using "cf restage YOUR_APPNAME" from the command line


    * From "Services" tab of the application in AppMgr
        - Push your application to PCF
        - In AppMgr click on your application
        - goto "Services" tab of your application
        - If you have already created a service instance:
            - select "BIND SERVICE".
            - select the desired service instance from the list
            - click "BIND"
        - If you have not created any service instances, and this is the first time:
            - select "NEW SERVICE"
            - click on the New Relic service tile
            - select the plan that is associated with your new relic account
            - click "SELECT PLAN" button
            - specify the instance name
            - click "CREATE"
        - "restage" the application using "cf restage YOUR_APPNAME" from the command line


* Bind your application to New Relic using User-Provided-Service
    - Create a user-provided-service with the word "newrelic" embedded as part of the service name 
    - add the following credentials to the user-rpovided-service:
        - "licenseKey" This is New Relic License Key - <strong>REQUIRED</strong>
        - "appName"    If you want to change the app name in New Relic use this property - <strong>OPTIONAL</strong>
        - sample CUPS command: ```cf cups my-newrelic-svc -p "licenseKey,appName"```
            - you will be prompted to provide values for licenseKey and appName<br/>
    - push your application in one of the following ways:
        - by adding the user-provided-service to the application manifest.yml before pushing the app
        - by adding the user-provided-service in AppMgr by binding an existing service instance, and restaging it after you bind the service


* Bind your application to New Relic using CF CLI
    - create an instance of New Relic service:
        <pre>
            cmd: cf create-service newrelic &lt;NEWRELIC_PLAN_NAME&gt; &lt;YOUR_NEWRELIC_SERVICE_INSTANCE_NAME&gt;
        </pre>
    - specify the newly created service instnace name in the <strong>"services"</strong> section of the application manifest (indented by two spaces):
        <pre>
              services:
              - YOUR_NEWRELIC_SERVICE_INSTANCE_NAME
        </pre>
    - push the application
        <pre>
            cmd: cf push<br/>
        </pre>

<br/>

### <a id='envvar-and-nrconfig'></a>Using Environment Variables and Agent Configuration

* You can use a combination of "newrelic.config" file and/or environment variables to configure New Relic Dotnet agent to report your application's health and performance to the designated New Relic account.

    - A copy of the 'newrelic.config' file is provided with the buildpack. If you need to add any agent features such as proxy settings, or change any other agent settings such as logging behavior, download <strong>newrelic.config</strong> file from New Relic into the application folder, and edit as required. You can refer to [New Relic Configuration documentation](https://docs.newrelic.com/docs/agents/net-agent/configuration/net-agent-configuration) for details on what properties are available. The following are some examples you can use:

        - <strong>new relic license key:</strong> add your New Relic license key:<br/>
            ```
              <service licenseKey="0123456789abcdef0123456789abcdef01234567">
            ```

        alternatively you can add the license key to application's 'manifest.yml' file as an environment variable "NEW_RELIC_LICENSE_KEY" in the "env" section


        - <strong>new relic app name:</strong> If you want the app name in New Relic be different than the app name in PCF, add the New Relic application name as you'd like it to appear in New Relic<br/>
        <pre>
              &lt;application&gt;
                &lt;name&gt;My Application&lt;/name&gt;
              &lt;/application&gt;
        </pre>

        alternatively you can add the New Relic app name to application's 'manifest.yml' file as an environment variable "NEW_RELIC_APP_NAME" in the "env" section


        - <strong>proxy setting:</strong> add proxy settings to the "service" element as a sub-element. example:<br/>
        <pre>
              &lt;service licenseKey="0123456789abcdef0123456789abcdef01234567"&gt;
                &lt;proxy host="my_proxy_server.com" port="9090" /&gt;
              &lt;/service&gt;
        </pre>


        - <strong>logging level:</strong> change agent logging level and destination<br/>
        <pre>
              &lt;log level="info" console="true" /&gt;
        </pre>

        - <strong>non-IIS executable instrumentation:</strong> since for dotnet framework apps 'hwc.exe' is the executable running your application, the copy of <strong>"newrelic.config"</strong> file that comes with the hwc extension contains the proper settings to tell the executable name to the agent. If you provide your own <strong>"newrelic.config"</strong> file, make sure it contains the following tag:
        <pre>
              &lt;instrumentation&gt;
                &lt;applications&gt;
                  &lt;application name="hwc.exe" /&gt;
                &lt;/applications&gt;
              &lt;/instrumentation&gt;
        </pre>
        
        Note:  Depending on your CI/CD pipeline, the Application directory may be created on-the-fly as part of the pipeline.  If that is the case and you are modifying this file, your pipeline will need to copy over the file to the Application directory before deploying/pushing the app to PCF.


    - Push your application to PCF using this buildpack. To do that, edit your manifest.yml and add/update the following entry.

        <pre>
            buildpacks:
            - &lt;NEWRELIC_EXTENSION_BUILDPACK_NAME&gt;
            - hwc_buildpack
        </pre>

        Then run "cf push".<br/>

        Note: If you use bamboo as your CI/CD pipeline tool, the "cf push" may not be required as your pipeline internally uses "cf push" to push the application to PCF.


<br/>

### <a id='envvar-and-nrconfig'></a>Debugging

* Set <strong>BP_DEBUG</strong> environment variable
        For troubleshooting purposes, you can set <strong>BP_DEBUG</strong> environment variable in your application environment to get more logging during the application push.


* Check the logs

    Use <strong>cf logs &lt;APP_NAME&gt;</strong> or <strong>cf logs &lt;APP_NAME&gt; --recent</strong>   to examine the application logs. It should display New Relic agent installation progress.


* User Cloud Foundry's [<strong>CF_TRACE</strong>](https://docs.cloudfoundry.org/devguide/deploy-apps/troubleshoot-app-health.html#trace-cloud-controller-rest-api-calls) to get detailed information about errors and unexpected behavior.



## <a id='examples'></a>Examples

### <a id='example-dotnet-core'></a>Push a Sample Dotnet Core Application to PCF
The following example uses <strong>"dotnet"</strong> CLI to create a sample Dotnet Core application, configures the app manifest to bind the application with New Relic Dotnet Core agent, and pushes the app to PCF. Note that the example uses environment variable to specify the license key for the New Relic account. You could explore this page for alternative ways to bind an application to the agent.

1- Create a sample dotnet MVC application (or use you existing dotnet Core application)<br/>
```
dotnet new mvc -n myapp
```

2- Test the app locally<br/>
```
cd myapp
dotnet run
```

3- Create a manifest.yml file for the application<br/>
<pre>
    ---
    applications:
    - name: myapp
      memory: 256M
      buildpacks:
        - nr_dotnetcore_extension_buildpack
        - dotnet_core_buildpack
      env:
        NEW_RELIC_LICENSE_KEY: 0123456789abcdef0123456789abcdef01234567

</pre>


4- Push the application to PCF<br/>
```
cf push
```


<br/>


### <a id='example-dotnet-framework'></a>Push a Sample Dotnet Framework Application to PCF

The following example shows the steps to configure the app manifest to bind a Dotnet Framework application New Relic Dotnet Framework agent using New Relic HWC extension buildpack and Cloud Foundry's standard HWC buildpack, and pushes the app to PCF. Note that the example uses environment variable to specify the license key for the New Relic account. You could explore this page for alternative ways to bind an application to the agent.

1- Create a sample dotnet framework application (or pick one of your dotnet framework apps)

2- Test the app locally and make sure it runs with no errors

3- Create a manifest.yml file for the application<br/>
<pre>
    ---
    applications:
    - name: myapp
      memory: 256M  # adjust as needed
      buildpacks:
        - nr_hwc_extension_buildpack
        - hwc_buildpack
      env:
        NEW_RELIC_LICENSE_KEY: 0123456789abcdef0123456789abcdef01234567

</pre>

4- Push the application to PCF<br/>
```
cf push
```

<br/><br/><br/>
---
---
---
---
---
# Release Notes for New Relic Dotnet Extension Buildpack for PCF

---

These are release notes for New Relic Dotnet Extension Buildpack for PCF.


## <a id="ver-1.0.1"></a> v1.0.1

<strong>Public Beta Release Date:</strong> November 8, 2018

Features included in this release:

* hwc extension buildpack for support of multi-buildpack approach
* added cached version of dotnet core buildpack
* hwc extension supports <strong>Windows 2012 R2, and 2016</strong>
* dotnet core extension supports <strong>ubuntu trusty and xenial</strong>
* code improvements in hwc and dotnet core extension buildpacks
* both hwc and dotnet core buildpacks support following ways to bind to new relic agent:
    * New Relic license environment variable
    * New Relic service broker
    * New Relic User-Provided-Services
    * New Relic agent confuration file


## <a id="ver-0.2.14"></a> v0.2.14

<strong>Initial Private Beta Release Date:</strong> June 20, 2018

Features included in this release:

* hwc buildpack with newrelic support
* hwc buildpack cached with newrelic support
* dotnet core multi-buildpack extension buildpack

<br/><br/><br/>
---
---
---
---
