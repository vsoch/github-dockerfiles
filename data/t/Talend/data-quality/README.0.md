for develeper, How to build the elastic search index files to Nexus server:

1. open the folder to \org.talend.dataquality.semantic\docker-container\tdq-elasticsearch\workdir\data
2. select elasticsearch folder and zip a elasticsearch.zip
3. run \org.talend.dataquality.semantic\deploy.bat
4. delete the \org.talend.dataquality.semantic\docker-container\tdq-elasticsearch\workdir\data\elasticsearch.zip


Command line to deploy the ontology repository index:
    mvn deploy:deploy-file -DgroupId=org.talend.elasticsearch \
      -DartifactId=tdq-semantic-index \
      -Dversion=6.0.0 \
      -Dpackaging=zip \
      -Dfile=/path/to/tdq-semantic-index-6.0.0.zip \
      -DrepositoryId=thirdparty-releases \
      -Durl=https://artifacts-zl.talend.com/nexus/content/repositories/thirdparty-releasessome parts of code comes from the Mural project. 
You can find them in the "contribs" package. org.talend.dataquality.survivorship
===================

Data Survivorship library.

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-survivorship/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-survivorship).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-survivorship).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-survivorship</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.sampling
===================

Reservoir sampling, data masking, data duplication

Changelog
-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-sampling/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-sampling).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-sampling).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-sampling</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.standardization
===================

Standardization library based on Apache Lucene

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-standardization/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-standardization).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-standardization).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-standardization</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.semantic
===================

API for semantic category analysis

Changelog
-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-semantic/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-semantic).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-semantic).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-semantic</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)

Lucene index tree
--------------------

```bash
.
├── shared
│   └── prod
│       ├── dictionary
│       │   ├── _0.cfe
│       │   ├── _0.cfs
│       │   └── _0.si
│       ├── keyword
│       │   ├── _0.cfe
│       │   ├── _0.cfs
│       │   └── _0.si
│       └── metadata
│           ├── _0.cfe
│           ├── _0.cfs
│           └── _0.si
└── <tenantId>
    ├── prod
    │   ├── dictionary
    │   │   ├── _0.cfe
    │   │   ├── _0.cfs
    │   │   └── _0.si
    │   └── metadata
    │       ├── _0.cfe
    │       ├── _0.cfs
    │       └── _0.si
    └── republish
        ├── dictionary
        │   ├── _0.cfe
        │   ├── _0.cfs
        │   └── _0.si
        └── metadata
            ├── _0.cfe
            ├── _0.cfs
            └── _0.si
```
The directory "shared" is always used in reading, never in writing.

We have as much "tenantId" directories as the number of tenants which modified the dictionary.

The directory "republish" is created while a republish process, then it will replace the "prod" directory and will be deleted.Jul. 2015
------------
**Source 1**: [http://data.okfn.org](http://data.okfn.org/data/country-codes), 
licensed by its maintainers under the [Public Domain Dedication and License](http://opendatacommons.org/licenses/pddl/1-0/).<br/>
**File**: *country-codes.csv*.

**Source 2**: Aicha BEN SALEM, PhD from University of Paris 13.<br/>
**16 Files**: *address_cleaned.csv*, *airport_cleaned.csv*, *animal_cleaned.csv*,<br/>
*city_cleaned.csv*, *civility_cleaned.csv*, *continent_cleaned.csv*,<br/>
*days_cleaned.csv*, *department_cleaned.csv*, *drug_cleaned.csv*,<br/>
*jobTitle_cleaned.csv*, *firstname_cleaned.csv*, *medical_tets_cleaned.csv*,<br/>
*months_cleaned.csv*, *gender_cleaned.csv*,*pharmacy_cleaned.csv*,<br/>
*speciality_field_cleaned.csv*.

Oct. 2015
-------------
#### Add 8 new files:

##### Source YAGO:
1. *wordnet_beverages_yago2.csv*, 
2. *wordnet_companies_yago2.csv*,
3. *wordnet_organizations_yago2.csv*,
4. *wordnet_museums_yago2.csv*.

##### Source Wikipedia
1. *us_counties.csv*: [Index of U.S. counties](https://en.wikipedia.org/wiki/Index_of_U.S._counties)
2. *airport-code-wiki.csv*: [List of airports](https://en.wikipedia.org/wiki/List_of_airports)
3. *airport-name-wiki.csv*: [List of airports](https://en.wikipedia.org/wiki/List_of_airports)

##### Others:
1. *industry_GICS_simplified.csv*, 
2. *unitOfMeasurement_cleaned.csv*.

For more details, please check jira issue: [TDQ-10903.](https://jira.talendforge.org/browse/TDQ-10903)

#### Remove 5 files:
1. *drug_cleaned.csv*, 
2. *medical_tets_cleaned.csv*, 
3. *pharmacy_cleaned.csv*, 
4. *speciality_field_cleaned.csv*,
5. *airport_cleaned.csv*,
6. *airport-codes_simplified.csv*: [Airport Codes](http://data.okfn.org/data/core/airport-codes)

#### Review all data source files and correct errors:
1. convert all files to utf 8
2. replace all "\&amp;" by "&"
3. optimize some source files by adding the synonims

Nov. 2015
-------------
#### Add 6 new files:
##### Source INSEE:
1. *comisimp2015.csv* for *FR_COMMUNE* index,
2. *depts2015.csv* for *FR_DEPARTEMENT* index,
3. *reg2015.csv* for *FR_REGION* index.

##### Source wikipedia:
*languages_code_name.csv* for indexes:
 *LANGUAGE*, *LANGUAGE_CODE_ISO2*, *LANGUAGE_CODE_ISO3*

##### Source [statoids.com](http://www.statoids.com/)
1. *ca_province_territory.csv* for the indexes: *CA_PROVINCE_TERRITORY*, *CA_PROVINCE_TERRITORY_CODE*
2. *mx_estado.csv* for the indexes: *MX_ESTADO*, *MX_ESTADO_CODE*

## Elasticsearch Dockerfile


This repository contains **Dockerfile** of [Elasticsearch](http://www.elasticsearch.org/) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/elasticsearch/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).


### Base Docker Image

* [dockerfile/java:oracle-java8](http://dockerfile.github.io/#/java)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/elasticsearch/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/elasticsearch`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/elasticsearch" github.com/dockerfile/elasticsearch`)


### Usage

    docker run -d -p 9200:9200 -p 9300:9300 dockerfile/elasticsearch

#### Attach persistent/shared directories

  1. Create a mountable data directory `<data-dir>` on the host.

  2. Create Elasticsearch config file at `<data-dir>/elasticsearch.yml`.

    ```yml
    path:
      logs: /data/log
      data: /data/data
    ```

  3. Start a container by mounting data directory and specifying the custom configuration file:

    ```sh
    docker run -d -p 9200:9200 -p 9300:9300 -v <data-dir>:/data dockerfile/elasticsearch /elasticsearch/bin/elasticsearch -Des.config=/data/elasticsearch.yml
    ```

After few seconds, open `http://<host>:9200` to see the result.

### Push to Talend Docker Registry 
    ```sh
    docker build -t talend/tdq-es:0.1 . 
    docker tag talend/tdq-es:0.1 tal-qa158.talend.lan:5000/talend/tdq-es:0.1
    docker push tal-qa158.talend.lan:5000/talend/tdq-es:0.1
    ```



h1. elasticsearch-head

h2. A web front end for an Elasticsearch cluster

h3. "http://mobz.github.io/elasticsearch-head":http://mobz.github.io/elasticsearch-head

h2. Installing and Running

There are two main ways of running and installing elasticsearch-head

h4. Running as a plugin of Elasticsearch

* @sudo elasticsearch/bin/plugin -install mobz/elasticsearch-head@
* @open http://localhost:9200/_plugin/head/@

This will automatically download the latest version of elasticsearch-head from github and run it as a plugin within the elasticsearch cluster. In this mode;
* elasticsearch-head automatically connects to the node that is running it
* If you've installed the .deb package, then the plugin exectuable will be available at /usr/share/elasticsearch/bin/plugin.

h4. Running with built in server

* @git clone git://github.com/mobz/elasticsearch-head.git@
* @cd elasticsearch-head@
* @npm install@
* @grunt server@
* @open@ "http://localhost:9100/":http://localhost:9100/

This will start a local webserver running on port 9100 serving elasticsearch-head
* Best option if you are likely to connect to serveral different clusters

h4. Alternatives

h5. Running from the filesystem

elastisearch-head is a standalone webapp written in good-ol' html5. This means, you can put it up on any webserver, run it directly from the filesystem, use it on an ipad, or put it on a floppy disk and carry it with you.

h4. URL Parameters

Parameters may be appended to the url set some initial state eg. @head/index.html?base_uri=http://node-01.example.com:9200@

* @base_uri@ force elasticsearch-head to connect to a particular node.
* @dashboard@ experimental feature to open elasticsearch-head in a mode suitable for dashboard / radiator. Accepts one parameter @dashboard=cluster@ 
* @auth_user@ adds basic auth credentials to http requests ( requires "elasticsearch-http-basic":https://github.com/karussell/elasticsearch-http-basic plugin or a reverse proxy )
* @auth_password@ basic auth password as above (note: without "additional security layers":http://security.stackexchange.com/questions/988/is-basic-auth-secure-if-done-over-https, passwords are sent over the network *in the clear* )

h4. Contributing

To contribute to elasticsearch-head you will need the following developer tools

# git and a "github":https://github.com/ account
# "node ( including npm )":http://nodejs.org/download
# "grunt-cli":http://gruntjs.com/getting-started
# (to run jasmine tests) "phantomjs":http://phantomjs.org

Then

# create a fork of elasticsearch-head on github
# clone your fork to your machine
# @cd elasticsearch-head@
# @npm install@ # downloads node dev dependencies
# @grunt dev@ # builds the distribution files, then watches the src directory for changes

Changes to both dist and src directories *must* be committed, to allow people to run head without running dev tools
and folllow existing dev patterns, such as indenting with tabs

h5. Contributing an Internationalisation

# English (primary) by "Ben Birch":https://twitter.com/mobz
# French by "David Pilato":https://twitter.com/dadoonet
# Portuguese by "caiodangelo":https://github.com/caiodangelo

To contribute an internationalisation

# Follow "Contributing" instructions above
# Find your 2-character "ISO 639-1 language code":http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
# edit index.html to add your 2 letter language code to the data-langs attribute of this line @<script src="dist/i18n.js" data-baseDir="dist/lang" data-langs="en,fr,your_lang_here"></script>@
# make a copy of @src/app/langs/en_strings.js@ prefixed with your langugae code
# convert english strings and fragments to your language. "Formatting Rules":http://docs.oracle.com/javase/tutorial/i18n/format/messageintro.html
# Submit a pull request

!http://mobz.github.com/elasticsearch-head/screenshots/clusterOverview.png(ClusterOverview Screenshot)!
org.talend.dataquality.email
===================

Email validation API

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-email/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-email).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-email).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-email</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.common
===================

Data Quality Common Library is the low level library containing interfaces and common utility classes.

Changelog
-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-common/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-common).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-common).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-common</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.semantic.model
===================

Semantic category model used for discovery/validation

Changelog
-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-semantic-model/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-semantic-model).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-semantic-model).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-semantic-model</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.converters
===================

API for all types of convert functions

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-converters/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-converters).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-converters).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-converters</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.record.linkage
===================

Record Matching algorithms, blocking key calculationn and T-Swoosh

Changelog
-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-record-linkage/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-record-linkage).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-record-linkage).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-record-linkage</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.text.japanese
===================

Japanese text analysis API

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-text-japanese/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-text-japanese).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-text-japanese).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-text-japanese</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.statistics
===================

API for data analysis and statistics

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-statistics/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-statistics).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-statistics).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-statistics</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
org.talend.dataquality.wordnet
===================

Content validation API based on WordNet dictionary

-------------

More information can be found [here](https://github.com/Talend/data-quality/blob/master/dataquality-wordnet/changelog.txt).

Where can I get the latest release?
-----------------------------------
You can download latest stable binaries from our [Release Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease/org/talend/dataquality/dataquality-wordnet).
or snapshot binaries from our [Snapshot Repository](https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceSnapshot/org/talend/dataquality/dataquality-wordnet).

Alternatively you can add the following repository into your pom.xml file:
```xml
<repositories>
  <repository>
    <id>TalendOpenSourceRelease</id>
    <url>https://artifacts-oss.talend.com/nexus/content/repositories/TalendOpenSourceRelease</url>
  </repository>
</repositories>
```

And include the following dependency:
```xml
<dependency>
  <groupId>org.talend.dataquality</groupId>
  <artifactId>dataquality-wordnet</artifactId>
  <version>LATEST</version>
</dependency>
```

License
-------
Code is under the [Apache Licence v2](https://www.apache.org/licenses/LICENSE-2.0.txt).

Additional Resources
--------------------

+ [Talend Homepage](http://www.talend.com/)
+ [Talend Bugtracker (JIRA)](https://jira.talendforge.org/)
