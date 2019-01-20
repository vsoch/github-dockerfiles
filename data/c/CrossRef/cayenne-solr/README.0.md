Apache Solr UIMA Metadata Extraction Library

Introduction
------------
This module is intended to be used both as an UpdateRequestProcessor while indexing documents and as a set of tokenizer/filters
to be configured inside the schema.xml for use during analysis phase.
UIMAUpdateRequestProcessor purpose is to provide additional on the fly automatically generated fields to the Solr index.
Such fields could be language, concepts, keywords, sentences, named entities, etc.
UIMA based tokenizers/filters can be used either inside plain Lucene or as index/query analyzers to be defined
inside the schema.xml of a Solr core to create/filter tokens using specific UIMA annotations.


Getting Started
---------------
To start using Solr UIMA Metadata Extraction Library you should go through the following configuration steps:

1. copy generated solr-uima jar and its libs (under contrib/uima/lib) inside a Solr libraries directory.
   or set <lib/> tags in solrconfig.xml appropriately to point those jar files.

   <lib dir="../../contrib/uima/lib" />
   <lib dir="../../contrib/uima/lucene-libs" />
   <lib dir="../../dist/" regex="solr-uima-\d.*\.jar" />

2. modify your schema.xml adding the fields you want to be hold metadata specifying proper values for type, indexed, stored and multiValued options:

   for example you could specify the following

  <field name="language" type="string" indexed="true" stored="true" required="false"/>
  <field name="concept" type="string" indexed="true" stored="true" multiValued="true" required="false"/>
  <field name="sentence" type="text" indexed="true" stored="true" multiValued="true" required="false" />

3. modify your solrconfig.xml adding the following snippet:

  <updateRequestProcessorChain name="uima">
    <processor class="org.apache.solr.uima.processor.UIMAUpdateRequestProcessorFactory">
      <lst name="uimaConfig">
        <lst name="runtimeParameters">
          <str name="keyword_apikey">VALID_ALCHEMYAPI_KEY</str>
          <str name="concept_apikey">VALID_ALCHEMYAPI_KEY</str>
          <str name="lang_apikey">VALID_ALCHEMYAPI_KEY</str>
          <str name="cat_apikey">VALID_ALCHEMYAPI_KEY</str>
          <str name="entities_apikey">VALID_ALCHEMYAPI_KEY</str>
          <str name="oc_licenseID">VALID_OPENCALAIS_KEY</str>
        </lst>
        <str name="analysisEngine">/org/apache/uima/desc/OverridingParamsExtServicesAE.xml</str>
        <!-- Set to true if you want to continue indexing even if text processing fails.
             Default is false. That is, Solr throws RuntimeException and
             never indexed documents entirely in your session. -->
        <bool name="ignoreErrors">true</bool>
        <!-- This is optional. It is used for logging when text processing fails.
             If logField is not specified, uniqueKey will be used as logField.
        <str name="logField">id</str>
        -->
        <lst name="analyzeFields">
          <bool name="merge">false</bool>
          <arr name="fields">
            <str>text</str>
          </arr>
        </lst>
        <lst name="fieldMappings">
          <lst name="type">
            <str name="name">org.apache.uima.alchemy.ts.concept.ConceptFS</str>
            <lst name="mapping">
              <str name="feature">text</str>
              <str name="field">concept</str>
            </lst>
          </lst>
          <lst name="type">
            <str name="name">org.apache.uima.alchemy.ts.language.LanguageFS</str>
            <lst name="mapping">
              <str name="feature">language</str>
              <str name="field">language</str>
            </lst>
          </lst>
          <lst name="type">
            <str name="name">org.apache.uima.SentenceAnnotation</str>
            <lst name="mapping">
              <str name="feature">coveredText</str>
              <str name="field">sentence</str>
            </lst>
          </lst>
        </lst>
      </lst>
    </processor>
    <processor class="solr.LogUpdateProcessorFactory" />
    <processor class="solr.RunUpdateProcessorFactory" />
  </updateRequestProcessorChain>

   where VALID_ALCHEMYAPI_KEY is your AlchemyAPI Access Key. You need to register AlchemyAPI Access
   key to exploit the AlchemyAPI services: http://www.alchemyapi.com/api/register.html

   where VALID_OPENCALAIS_KEY is your Calais Service Key. You need to register Calais Service
   key to exploit the Calais services: http://www.opencalais.com/apikey
  
   the analysisEngine must contain an AE descriptor inside the specified path in the classpath

   the analyzeFields must contain the input fields that need to be analyzed by UIMA,
   if merge=true then their content will be merged and analyzed only once

   field mapping describes which features of which types should go in a field

4. in your solrconfig.xml replace the existing default (<requestHandler name="/update"...)  or create a new UpdateRequestHandler with the following:
  <requestHandler name="/update" class="solr.XmlUpdateRequestHandler">
    <lst name="defaults">
      <str name="update.processor">uima</str>
    </lst>
  </requestHandler>

Once you're done with the configuration you can index documents which will be automatically enriched with the specified fields
Apache Solr Morphlines-Cell

*Experimental* - This contrib is currently subject to change in ways that may 
break back compatibility.

This contrib provides a variety of Kite Morphlines features for Solr Cell type functionality.The test-files by this module are located in the morphlines-core module.
Apache Solr Language Identifier


Introduction
------------
This module is intended to be used while indexing documents.
It is implemented as an UpdateProcessor to be placed in an UpdateChain.
Its purpose is to identify language from documents and tag the document with language code.
The module can optionally map field names to their language specific counterpart,
e.g. if the input is "title" and language is detected as "en", map to "title_en".
Language may be detected globally for the document, and/or individually per field.
Language detector implementations are pluggable.

Getting Started
---------------
Please refer to the module documentation at http://wiki.apache.org/solr/LanguageDetection

Dependencies
------------
The Tika detector depends on Tika Core (which is part of extraction contrib)
The Langdetect detector depends on LangDetect library                    Apache Solr - DataImportHandler

Introduction
------------
DataImportHandler is a data import tool for Solr which makes importing data from Databases, XML files and
HTTP data sources quick and easy.

Important Note
--------------
Although Solr strives to be agnostic of the Locale where the server is
running, some code paths in DataImportHandler are known to depend on the
System default Locale, Timezone, or Charset.  It is recommended that when
running Solr you set the following system properties:
  -Duser.language=xx -Duser.country=YY -Duser.timezone=ZZZ

where xx, YY, and ZZZ are consistent with any database server's configuration.
The analysis-extras plugin provides additional analyzers that rely
upon large dependencies/dictionaries.

It includes integration with ICU for multilingual support, and 
analyzers for Chinese and Polish.

ICU relies upon lucene-libs/lucene-analyzers-icu-X.Y.jar
and lib/icu4j-X.Y.jar

Smartcn relies upon lucene-libs/lucene-analyzers-smartcn-X.Y.jar

Stempel relies on lucene-libs/lucene-analyzers-stempel-X.Y.jar

Morfologik relies on lucene-libs/lucene-analyzers-morfologik-X.Y.jar
and lib/morfologik-*.jar
 
Apache Solr Content Extraction Library (Solr Cell)

Introduction
------------

Apache Solr Extraction provides a means for extracting and indexing content contained in "rich" documents, such
as Microsoft Word, Adobe PDF, etc.  (Each name is a trademark of their respective owners)  This contrib module
uses Apache Tika to extract content and metadata from the files, which can then be indexed.  For more information,
see http://wiki.apache.org/solr/ExtractingRequestHandler

Getting Started
---------------
You will need Solr up and running.  Then, simply add the extraction JAR file, plus the Tika dependencies (in the ./lib folder)
to your Solr Home lib directory.  See http://wiki.apache.org/solr/ExtractingRequestHandler for more details on hooking it in
 and configuring.

Apache Solr Morphlines-Core

*Experimental* - This contrib is currently subject to change in ways that may 
break back compatibility.

This contrib provides a variety of Kite Morphlines features for Solr.Apache Solr MapReduce

*Experimental* - This contrib is currently subject to change in ways that may 
break back compatibility.

The Solr MapReduce contrib provides an a mapreduce job that allows you to build
Solr indexes and optionally merge them into a live Solr cluster.

Example:

# Build an index with map-reduce and deploy it to SolrCloud

source $solr_distrib/example/scripts/map-reduce/set-map-reduce-classpath.sh

$hadoop_distrib/bin/hadoop --config $hadoop_conf_dir jar \
$solr_distrib/dist/solr-map-reduce-*.jar -D 'mapred.child.java.opts=-Xmx500m' \
-libjars "$HADOOP_LIBJAR" --morphline-file readAvroContainer.conf \
--zk-host 127.0.0.1:9983 --output-dir hdfs://127.0.0.1:8020/outdir \
--collection $collection --log4j log4j.properties --go-live \
--verbose "hdfs://127.0.0.1:8020/indir"The test-files by this module are located in the morphlines-core module.
The Clustering contrib plugin for Solr provides a generic mechanism for plugging in third party clustering implementations.
It currently provides clustering support for search results using the Carrot2 project.

See http://wiki.apache.org/solr/ClusteringComponent for how to get started.
Welcome to Apache Solr Learning to Rank!
========

Apache Solr Learning to Rank (LTR) provides a way for you to extract features
directly inside Solr for use in training a machine learned model.  You can then
deploy that model to Solr and use it to rerank your top X search results.

# Getting Started With Solr Learning To Rank

For information on how to get started with solr ltr please see:
 * [Solr Reference Guide's section on Learning To Rank](https://cwiki.apache.org/confluence/display/solr/Learning+To+Rank)

# Getting Started With Solr

For information on how to get started with solr please see:
 * [solr/README.txt](../../README.txt)
 * [Solr Quick Start](http://lucene.apache.org/solr/quickstart.html)

# How To Contribute

For information on how to contribute see:
 * http://wiki.apache.org/lucene-java/HowToContribute
 * http://wiki.apache.org/solr/HowToContribute

The Solr test-framework products base classes and utility classes for 
writting JUnit tests excercising Solr functionality.

This test framework relies on the lucene components found in in the 
./lucene-libs/ directory, as well as the third-party libraries found 
in the ./lib directory.
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Solr server
------------

This directory contains an instance of the Jetty Servlet container setup to 
run Solr.

To run Solr:

  cd $SOLR_INSTALL
  bin/solr start

where $SOLR_INSTALL is the location where you extracted the Solr installation bundle.

Server directory layout
-----------------------

server/contexts

  This directory contains the Jetty Web application deployment descriptor for the Solr Web app.

server/etc

  Jetty configuration and example SSL keystore

server/lib

  Jetty and other 3rd party libraries

server/logs

  Solr log files

server/resources

  Contains configuration files, such as the Log4j configuration (log4j.properties) for configuring Solr loggers.

server/scripts/cloud-scripts

  Command-line utility for working with ZooKeeper when running in SolrCloud mode, see zkcli.sh / .cmd for
  usage information.

server/solr

  Default solr.solr.home directory where Solr will create core directories; must contain solr.xml

server/solr/configsets

  Directories containing different configuration options for running Solr.

    basic_configs               : Bare minimum configuration settings needed to run Solr.

    data_driven_schema_configs  : Field-guessing and managed schema mode; use this configuration if you want
                                  to start indexing data in Solr without having to design a schema upfront.
                                  You can use the REST API to manage your schema as you refine your index
                                  requirements.

    sample_techproducts_configs : Comprehensive example configuration that demonstrates many of the powerful
                                  features of Solr, based on the use case of building a search solution for
                                  tech products.

server/solr-webapp

  Contains files used by the Solr server; do not edit files in this directory (Solr is not a Java Web application).


Notes About Solr Examples
--------------------------

* SolrHome *

By default, start.jar starts Solr in Jetty using the default Solr Home
directory of "./solr/" (relative to the working directory of the servlet 
container).

* References to Jar Files Outside This Directory *

Various example SolrHome dirs contained in this directory may use "<lib>"
statements in the solrconfig.xml file to reference plugin jars outside of 
this directory for loading "contrib" plugins via relative paths.  

If you make a copy of this example server and wish to use the 
ExtractingRequestHandler (SolrCell), DataImportHandler (DIH), UIMA, the 
clustering component, or any other modules in "contrib", you will need to 
copy the required jars or update the paths to those jars in your 
solrconfig.xml.

* Logging *

By default, Jetty & Solr will log to the console and logs/solr.log. This can
be convenient when first getting started, but eventually you will want to
log just to a file. To configure logging, edit the log4j.properties file in
"resources".
 
It is also possible to setup log4j or other popular logging frameworks.

http://www.splitbrain.org/projects/file_icons

Released to the Public Domain
Free to use. Provided as is. No warranties.

Note: The big majority of icons where created by the creators listed
      below. Only a few ones where found on the net. They were too
      widespread to determine the original author and thus were
      considered public domain.
      If you are the author of one of those icons just send a short
      mail to either be included in the list below or have the icon
      removed from the package.

Creators:

  Andreas Gohr <andi@splitbrain.org>
  Michael Klier <chi@chimeric.de>
  Andreas Barton <andreas.barton@web.de>
  Hubert Chathi <hubert@uhoreg.ca>
  Johan Koehne <johankohne@gmail.com>
  Rudi von Staden <rudivs@iafrica.com>
  Daniel Darvish <ddarvish@hibm.org>
  Andy Pascall <apascall@engineering.ucsb.edu>
  Seth <seth.holcomb@gmail.com>
  David Carella <david.carella@gmail.com>
  Tom N. Harris <telliamed@fastmail.us>
  Brandon Carmon Colvin <b.carmon.colvin@gmail.com>
