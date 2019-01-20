This is a placeholder to put Hadoop native libraries -it's a component
that contains platform-specific native code that significantly speeds up
data (de)compression. Since there are no maven artifacts for this component
the build process can't automatically download it.

These libraries are purely optional, and if they are missing Hadoop will
use corresponding pure Java components. The impact of native compression
becomes noticeable with larger datasets and weaker CPU-s - if you notice
that the CPU is routinely saturated when a job is sorting or reducing,
then using these libs may help.

Installation instructions
=========================
You can obtain the necessary files from a distribution package of Hadoop,
e.g. hadoop-0.20.2.tar.gz. Unpack this archive, and copy the content of
lib/native here, so that the layout looks like this:

<Nutch home>/lib/native/Linux-amd64-64/...
<Nutch home>/lib/native/Linux-i386-32/...

Local runtime
-------------
The build process will include these native libraries when preparing
the /runtime/local environment for running in local mode.

/runtime/local/bin/nutch knows how to use these libs - if they are
found and correctly used that's fine, however if they are not and you
see WARN, don't worry, however you will see lines like this in your logs:

15:36:02,126 WARN org.apache.hadoop.util.NativeCodeLoader: Unable to load
native-hadoop library for your platform... using builtin-java classes where
applicable
...
probably quite a few more of the same
...

Distributed runtime
-------------------
If you want to use this component in an existing Hadoop cluster (when using
/runtime/deploy artifacts) you need to make sure these files are placed in
Hadoop/lib/native directory on each node, and then restart the cluster. If
you installed the cluster from a distribution package of Hadoop then these
libraries should already be in the right place and you shouldn't need to do
anything else.
Parsefilter-regex plugin

Allow parsing and set custom defined fields using regex. Rules can be defined
in a separate rule file or in the nutch configuration.

If a rule file is used, should create a text file regex-parsefilter.txt (which
is the default name of the rules file). To use a different filename, either
update the file value in plugin’s build.xml or add parsefilter.regex.file
config to the nutch config.

ie:
    <property>
      <name>parsefilter.regex.file</name>
      <value>
	/path/to/rulefile
      </value>
    </property


Format of rules: <name>\t<source>\t<regex>\n

ie:
	my_first_field		html	h1
	my_second_field		text	my_pattern


If a rule file is not used, rules can be directly set in the nutch config:

ie:
    <property>
      <name>parsefilter.regex.rules</name>
      <value>
	my_first_field		html	h1
	my_second_field		text	my_pattern
      </value>
    </property

source can be either html or text. If source is html, the regex is applied to
the entire HTML tree. If source is text, the regex is applied to the
extracted text.

IndexReplace plugin

Allows indexing-time regexp replace manipulation of metadata fields.

Configuration Example
    <property>
      <name>index.replace.regexp</name>
      <value>
        id=/file\:/http\:my.site.com/
        url=/file\:/http\:my.site.com/2
      </value>
    </property

Property format: index.replace.regexp
    The format of the property is a list of regexp replacements, one line per field being
    modified.  Field names would be one of those from https://wiki.apache.org/nutch/IndexStructure.

    The fieldname precedes the equal sign.  The first character after the equal sign signifies
    the delimiter for the regexp, the replacement value and the flags.

Replacement Sequence
    The replacements will happen in the order listed. If a field needs multiple replacement operations
    they may be listed more than once.

RegExp Format
    The regexp and the optional flags should correspond to Pattern.compile(String regexp, int flags) defined
    here: http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html#compile%28java.lang.String,%20int%29
    Patterns are compiled when the plugin is initialized for efficiency.

Replacement Format
    The replacement value should correspond to Java Matcher(CharSequence input).replaceAll(String replacement):
    http://docs.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html#replaceAll%28java.lang.String%29

Flags
    The flags is an integer sum of the flag values defined in
    http://docs.oracle.com/javase/7/docs/api/constant-values.html (Sec: java.util.regex.Pattern)

Creating New Fields
    If you express the fieldname as fldname1:fldname2=[replacement], then the replacer will create a new field
    from the source field.  The source field remains unmodified.  This is an alternative to solrindex-mapping
    which is only able to copy fields verbatim.

Multi-valued Fields
    If a field has multiple values, the replacement will be applied to each value in turn.

Non-string Datatypes
    Replacement is possible only on String field datatypes.  If the field you name in the property is
    not a String datatype, it will be silently ignored.

Host and URL specific replacements.
    If the replacements should apply only to specific pages, then add a sequence like

    hostmatch=hostmatchpattern
    fld1=/regexp/replace/flags
    fld2=/regexp/replace/flags

    or
    urlmatch=urlmatchpattern
    fld1=/regexp/replace/flags
    fld2=/regexp/replace/flags

When using Host and URL replacements, all replacements preceding the first hostmatch or urlmatch
will apply to all parsed pages.  Replacements following a hostmatch or urlmatch will be applied
to pages which match the host or url field (up to the next hostmatch or urlmatch line).  hostmatch
and urlmatch patterns must be unique in this property.

Plugin order
    In most cases you will want this plugin to run last.

Testing your match patterns
    Online Regexp testers like http://www.regexplanet.com/advanced/java/index.html
    can help get the basics of your pattern working.
    To test in nutch: 
        Prepare a test HTML file with the field contents you want to test. 
        Place this in a directory accessible to nutch.
        Use the file:/// syntax to list the test file(s) in a test/urls seed list.
        See the nutch faq "index my local file system" for conf settings you will need.
        (Note the urlmatch and hostmatch patterns may not conform to your test file host and url; This
        test approach confirms only how your global matches behave, unless your urlmatch and hostmatch
        patterns also match the file: URL pattern)
 
    Run..
        bin/nutch inject crawl/crawldb test
        bin/nutch generate crawl/crawldb crawl/segments
        bin/nutch fetch crawl/segments/[segment]
        bin/nutch parse crawl/segments/[segment]
        bin/nutch invertlinks crawl/linkdb -dir crawl/segments
        ...index your document, for example with SOLR...
        bin/nutch solrindex http://localhost:8983/solr crawl/crawldb/ -linkdb crawl/linkdb/ crawl/segement[segment] -filter -normalize

    Inspect hadoop.log for info about pattern parsing and compilation..
        grep replace logs/hadoop.log

    To inspect your index with the solr admin panel...
        http://localhost:8983/solr/#/
Nutch Interactive Selenium
==========================

This protocol plugin allows you to fetch and interact with pages using [Selenium](http://www.seleniumhq.org/).

# Dependencies and Configuration

You will need to have [Selenium](http://www.seleniumhq.org/) and a compatible version of Firefox installed to use this plugin.

Set the protocol to be used in your Nutch configuration files.
```
<!-- NUTCH_HOME/conf/nutch-site.xml -->

<configuration>
  ...
  <property>
    <name>plugin.includes</name>
    <value>protocol-interactiveselenium|urlfilter-regex| ... </value>
    <description></description>
  </property>
```

# Custom Handlers

Only basic functionality is included in the DefaultHandler that comes with the plugin. If you want additional functionality you can implement custom handlers by implementing the InteractiveSeleniumHandler interface in the plugin package. Be sure to also update the plugin config to include your new handler.

```
<!-- NUTCH_HOME/conf/nutch-site.xml -->
<property>
  <name>interactiveselenium.handlers</name>
  <value>NewCustomHandler,DefaultHandler</value>
  <description></description>
</property>
```

# Handler Info

Handlers are called in the order that they're specified in the configuration. A "clean" driver is used for each handler so multiple handlers won't interfere with each other. Page content is appended together from each handler and returned for the request.
AWS CloudSearch plugin for Nutch 
================================

See [http://aws.amazon.com/cloudsearch/] for information on AWS CloudSearch.

Steps to use :

From runtime/local/bin

* Configure the AWS credentials 

Edit `~/.aws/credentials`, see [http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html] for details. Note that this should not be necessary when running Nutch on EC2.

* Edit ../conf/nutch-site.xml and check that 'plugin.includes' contains 'indexer-cloudsearch'. 

* (Optional) Test the indexing 

`./nutch indexchecker -D doIndex=true -D cloudsearch.batch.dump=true "http://nutch.apache.org/"`

if the agent name hasn't been configured in nutch-site.xml, it can be added on the command line with `-D http.agent.name=whateverValueDescribesYouBest`

you should see the fields extracted for the indexing coming up on the console.

Using the `cloudsearch.batch.dump` parameter allows to dump the batch to the local temp dir. The files has the prefix "CloudSearch_" e.g. `/tmp/CloudSearch_4822180575734804454.json`. This temp file can be used as a template when defining the fields in the domain creation (see below).

* Create a CloudSearch domain

This can be done using the web console [https://eu-west-1.console.aws.amazon.com/cloudsearch/home?region=eu-west-1#]. You can use the temp file generated above to bootstrap the field definition. 

You can also create the domain using the AWS CLI [http://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html] and the `createCSDomain.sh` example script provided. This script is merely as starting point which you should further improve and fine tune. 

Note that the creation of the domain can take some time. Once it is complete, note the document endpoint, or alternatively verify the region and domain name.

* Edit ../conf/nutch-site.xml and add `cloudsearch.endpoint` and `cloudsearch.region`. 

* Re-test the indexing

`./nutch indexchecker -D doIndex=true "http://nutch.apache.org/"`

and check in the CloudSearch console that the document has been succesfully indexed.

Additional parameters

* `cloudsearch.batch.maxSize` \: can be used to limit the size of the batches sent to CloudSearch to N documents. Note that the default limitations still apply.

* `cloudsearch.batch.dump` \: see above. Stores the JSON representation of the document batch in the local temp dir, useful for bootstrapping the index definition.

Note

The CloudSearchIndexWriter will log any errors while sending the batches to CloudSearch and will resume the process without breaking. This means that you might not get all the documents in the index. You should check the log files for errors. Using small batch sizes will limit the number of documents skipped in case of error.

Any fields not defined in the CloudSearch domain will be ignored by the CloudSearchIndexWriter. Again, the logs will contain a trace of any field names skipped.



  


urlfilter-ignoreexempt
======================
  This plugin allows certain urls to be exempted when the external links are configured to be ignored.
  This is useful when focused crawl is setup but some resources like static files are linked from CDNs (external domains).

# How to enable ?
Add `urlfilter-ignoreexempt` value to `plugin.includes` property
```xml
<property>
  <name>plugin.includes</name>
  <value>protocol-http|urlfilter-(regex|ignoreexempt)...</value>
</property>
```

# How to configure rules?

open `conf/db-ignore-external-exemptions.txt` and add the regex rules.

## Format :

The format is same same as `regex-urlfilter.txt`.
 Each non-comment, non-blank line contains a regular expression
 prefixed by '+' or '-'.  The first matching pattern in the file
 determines whether a URL is exempted or ignored.  If no pattern
 matches, the URL is ignored.


## Example :

 To exempt urls ending with image extensions, use this rule

`+(?i)\.(jpg|png|gif)$`

   
   
## Testing the Rules :

After enabling the plugin and adding your rules to `conf/db-ignore-external-exemptions.txt`, run:
   
`bin/nutch plugin urlfilter-ignoreexempt  org.apache.nutch.urlfilter.ignoreexempt.ExemptionUrlFilter http://yoururl.here`


This should print `true` for urls which are accepted by configured rules.Support for crawling and searching Creative-Commons licensed content. 
For brief description about this plugin see
src/java/org/apache/nutch/collection/package.html

Basically:
You need to enable this during indexing and during searching

After indexing you can limit your searches to certain
subcollection with keyword subcollection, eg. 

"subcollection:nutch hadoop"
Nutch Selenium
==============

# Introduction

This plugin allows you to fetch Javascript pages using [Selenium](http://www.seleniumhq.org/), while relying on the rest of the awesome Nutch stack!

The underlying code is based on the nutch-htmlunit plugin, which was in turn based on nutch-httpclient.

There are essentially two ways in which Nutch can be used with Selenium.

 * Locally (on each node) as a self contained process, or
 * via the RemoteWebDriver which connects to [Selenium-Grid](http://www.seleniumhq.org/docs/07_selenium_grid.jsp). A grid consists of a single hub, and one or more nodes.

# Installation

## Part 1:

### A) Setting up Selenium (local mode)

 * Ensure that you have your prefered browser installed. Currently Chrome, Safari, Opera, PhantomJS and Firefox are supported. Here there example of installing Firefox is provided. More info about the package @ [launchpad](https://launchpad.net/ubuntu/trusty/+source/firefox)
```
sudo apt-get install firefox
```

 * Install Xvfb and its associates

This step is not necessary for the PhantomJs broswer and may not be needed for all browsers.

```
sudo apt-get install xorg synaptic xvfb gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi \
    xfonts-75dpi xfonts-base xfonts-scalable freeglut3-dev dbus-x11 openbox x11-xserver-utils \
    libxrender1 cabextract
```

 * Set a display for Xvfb, so that firefox believes a display is connected

```
sudo /usr/bin/Xvfb :11 -screen 0 1024x768x24 &
sudo export DISPLAY=:11
```
### B) Setting up a Selenium Grid

Using the Selenium Grid will allow you to parallelize the job by facilitating access of several instances of browsers whether on one machine or on several machines. Note that grid facilitates heterogeneity with regards to browser types used. However, these steps have been tested using a homogenous Selenium Grid with Firefox and PhantomJS browsers.

 * Download the [Selenium Standalone Server](http://www.seleniumhq.org/download/) and follow the installation instructions.

 * Some important configurations to note while setting up the selenium-hub and the selenium-nodes are:
    * For the hub:
      - maxSession (how many browser sessions to allow on the grid at a time)
      - browserTimeout (how long to wait before timing out a browser session. This is dependent on the interactivity to be completed on the page)

    * For the nodes:
      - browserName=<browser>, maxInstances (the max number of instances of the same version browser to allow per a system)
      - browserName=<browser>, maxSession (the max number of sessions of any type of browser/version to allow per a system)

  * Go headless with your selenium Grid installation. There are different ways to this. See [this resource](http://elementalselenium.com/tips/38-headless) for further details.

  * For Nutch efficiency, and optimization of the grid, consider editing the following configs in **nutch-site.xml**
    - fetcher.threads.per.queue (change value to the value of the maxSession config on the hub)
    - fetcher.threads.fetch (change value to the value of the maxSession config on the hub)
    - fetcher.server.delay (As multiple threads may be accessing a single server at a time, consider changing this value to 4-5 seconds for politeness)
    - fetcher.server.min.delay (As multiple threads may be accessing a single server at a time, consider changing this values to 4-5 seconds for politeness)
    - Ensure all configs for the hub mentioned in Part 2 are appropriately set.

  * To activate the full selenium grid, edit **$NUTCH_HOME/runtime/local/bin/crawl** script:
    - numThreads = maxSession on nodes * num of nodes


## Part 2: Installing plugin for Nutch (where NUTCH_HOME is the root of your nutch install)

 * Ensure that the plugin will be used as the protocol parser in your config

```
<!-- NUTCH_HOME/conf/nutch-site.xml -->

<configuration>
  ...
  <property>
    <name>plugin.includes</name>
    <value>protocol-selenium|urlfilter-regex|parse-(html|tika)|index-(basic|anchor)|urlnormalizer-(pass|regex|basic)|scoring-opic</value>
    <description>Regular expression naming plugin directory names to
    include.  Any plugin not matching this expression is excluded.
    In any case you need at least include the nutch-extensionpoints plugin. By
    default Nutch includes crawling just HTML and plain text via HTTP,
    and basic indexing and search plugins. In order to use HTTPS please enable
    protocol-httpclient, but be aware of possible intermittent problems with the
    underlying commons-httpclient library.
    </description>
  </property>
```

* Then ensure that you have the correct configuration set within the following configuration options

```
<!-- protocol-selenium plugin properties -->

<property>
  <name>selenium.driver</name>
  <value>firefox</value>
  <description>
    A String value representing the flavour of Selenium
    WebDriver() to use. Currently the following options
    exist - 'firefox', 'chrome', 'safari', 'opera', 'phantomjs', and 'remote'.
    If 'remote' is used it is essential to also set correct properties for
    'selenium.hub.port', 'selenium.hub.path', 'selenium.hub.host' and
    'selenium.hub.protocol'.
  </description>
</property>

<property>
  <name>selenium.take.screenshot</name>
  <value>false</value>
  <description>
    Boolean property determining whether the protocol-selenium
    WebDriver should capture a screenshot of the URL. If set to
    true remember to define the 'selenium.screenshot.location'
    property as this determines the location screenshots should be
    persisted to on HDFS. If that property is not set, screenshots
    are simply discarded.
  </description>
</property>

<property>
  <name>selenium.screenshot.location</name>
  <value></value>
  <description>
    The location on disk where a URL screenshot should be saved
    to if the 'selenium.take.screenshot' proerty is set to true.
    By default this is null, in this case screenshots held in memory
    are simply discarded.
  </description>
</property>

<property>
  <name>selenium.hub.port</name>
  <value>4444</value>
  <description>Selenium Hub Location connection port</description>
</property>

<property>
  <name>selenium.hub.path</name>
  <value>/wd/hub</value>
  <description>Selenium Hub Location connection path</description>
</property>

<property>
  <name>selenium.hub.host</name>
  <value>localhost</value>
  <description>Selenium Hub Location connection host</description>
</property>

<property>
  <name>selenium.hub.protocol</name>
  <value>http</value>
  <description>Selenium Hub Location connection protocol</description>
</property>

<property>
  <name>selenium.grid.driver</name>
  <value>firefox</value>
  <description>A String value representing the flavour of Selenium
    WebDriver() used on the selenium grid. Currently the following options
    exist - 'firefox' or 'phantomjs' </description>
</property>

<property>
  <name>selenium.grid.binary</name>
  <value></value>
  <description>A String value representing the path to the browser binary
    location for each node
 </description>
</property>

<!-- lib-selenium configuration -->
<property>
  <name>libselenium.page.load.delay</name>
  <value>3</value>
  <description>
    The delay in seconds to use when loading a page with lib-selenium. This
    setting is used by protocol-selenium and protocol-interactiveselenium
    since they depending on lib-selenium for fetching.
  </description>
</property>
```
 * If you've selected 'remote' value for the 'selenium.driver' property, ensure that you've configured
 the additional properties based on your [Selenium-Grid installation](http://www.seleniumhq.org/docs/07_selenium_grid.jsp#installation).

 * Compile nutch
```
ant runtime
```

 * Start your web crawl (Ensure that you followed the above steps and have started your xvfb display as shown above)

## Part 3: Common Pitfalls

* Be sure your browser version and selenium version are compatible (See list in 'Tested configurations' section below)
* Be sure to start the Xvfb window then start selenium (not a necessary step for PhantomJS)
* Disconnecting and reconnect nodes after a hub config change has proven useful in our tests.
* Be sure that each browser session deallocates its webdriver resource independently of any other tests running on other broswers (check out driver.quit() and driver.close()).

### Tested configurations

* Firefox 31.4.0 and Selenium 2.48.2
* PhantomJS 2.1.1 and Selenium 2.48.2
* PhantomJS 2.1.1 and Selenium 2.53.0

Parse-metatags plugin

The parse-metatags plugin consists of a HTMLParserFilter which takes as parameter a list of metatag names with '*' as default value. The values are separated by ';'.
In order to extract the values of the metatags description and keywords, you must specify in nutch-site.xml

<property>
  <name>metatags.names</name>
  <value>description;keywords</value>
</property>

Prefixes the names with 'metatag.' in the parse-metadata. For instance to index description and keywords, you need to activate the plugin index-metadata and set the value of the parameter 'index.parse.md' to 'metatag.description;metatag.keywords'.
  
This code has been developed by DigitalPebble Ltd and offered to the community by ANT.com




indexer-links plugin for Nutch
==============================

This plugin provides the feature to index the inlinks and outlinks of a URL
into an indexing backend.

## Configuration

This plugin provides the following configuration options:

* `index.links.outlinks.host.ignore`: If true, the plugin will ignore outlinks
that point to the same host as the current URL. By default, all outlinks are
indexed. If `db.ignore.internal.links` is `true` (default value) this setting
is ignored because the internal links are already ignored.

* `index.links.inlinks.host.ignore`: If true, the plugin will ignore inlinks
coming from the same host as the current URL. By default, all inlinks are
indexed. If `db.ignore.internal.links` is `true` (default value) this setting
is ignored because the internal links are already ignored.

* `index.links.hosts.only`: If true, the plugin will index only the host portion of the inlinks/outlinks URLs.

## Fields

For this plugin to work 2 new fields have to be added/configured in your storage backend:

* `inlinks`
* `outlinks`

If the plugin is enabled these fields have to be added to your storage backend
configuration.

The specifics of how these fields are configured depends on your specific
backend. We provide here sane default values for Solr.

The following fields should be added to your backend storage. We provide
examples of default values for the Solr schema.

* Each outlink/inlink will be stored as a string without any tokenization.
* The `inlink`/`outlink` fields have to be multivalued, because normally a
given URL will have multiple inlinks and outlinks.

```
<fieldType name="string" class="solr.StrField" sortMissingLast="true" omitNorms="true"/>
```

The field configuration could look like:

```
<field name="inlinks" type="multiValuedString" stored="true" indexed="true" multiValued="true"/>

<field name="outlinks" type="multiValuedString" stored="true" indexed="true" multiValued="true"/>
```# Nutch Dockerfile #

Get up and running quickly with Nutch on Docker.

## What is Nutch?

![Nutch logo](https://wiki.apache.org/nutch/FrontPage?action=AttachFile&do=get&target=nutch_logo_medium.gif "Nutch")

Apache Nutch is a highly extensible and scalable open source web crawler software project.

Nutch can run on a single machine, but gains a lot of its strength from running in a Hadoop cluster

## Docker Image

Current configuration of this image consists of components:

*	Nutch 1.x

##  Base Image

* [ubuntu:14.04](https://registry.hub.docker.com/_/ubuntu/)

## Tips

You may need to alias docker to "docker --tls" if you see errors such as:

```
2015/04/07 09:19:56 Post http://192.168.59.103:2376/v1.14/containers/create?name=NutchContainer: malformed HTTP response "\x15\x03\x01\x00\x02\x02\x16"
```

The easiest way to do this:

1. ```alias docker="docker --tls"```

## Installation

1. Install [Docker](https://www.docker.com/).

2. Build from files in this directory:

	$(boot2docker shellinit | grep export)
	docker build -t apache/nutch .

## Usage

Start docker

	boot2docker up
	$(boot2docker shellinit | grep export)

Start up an image and attach to it

    docker run -t -i -d --name nutchcontainer apache/nutch /bin/bash
    docker attach --sig-proxy=false nutchcontainer

Nutch is located in ~/nutch and is almost ready to run.
You will need to set seed URLs and update the configuration with your crawler's Agent Name.
For additional "getting started" information checkout the [Nutch Tutorial](https://wiki.apache.org/nutch/NutchTutorial).
