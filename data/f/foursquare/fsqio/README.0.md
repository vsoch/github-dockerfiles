# Fsq.io scripts #

Miscellaneous scripts and files that are not managed by Pants.
Every file in under this directory is made publicly available in Fsq.io
# Fsq.io Intellij helpers

## Lists.scala for Intellij

### Background

scala/Lists.scala uses Type Constructors which IntelliJ can't parse ([issue](https://youtrack.jetbrains.com/issue/SCL-7974)).

We created `scripts/fsqio/IntelliJ/Lists.scala` which features simpler interfaces specifically for the IntelliJ presentation compiler.

### Usage
Compile Lists.Implicits._
Right-click `src/jvm/io/fsq/common/scala/Lists.scala` and select Mark as Plain Text


## Spindle stubs for Intellij

### Background

Our generated code is enormous and may be the source of slow indexing and memory issues, especially when running multiple projects. By stubbing out our codegen we can significantly reduce the size and complexity of the classes that IntelliJ has to index and this seems to improve performance.

The code generation templates for the stub classes can be tweaked in the template files under `src/resources/io/fsq/ssp/codegen/scalainterface`

Note that currently only the spindle classes are included. We could extend this to cover soy template and other generated classes as well if it is important for you to have those analyzed by the IDE.


### Usage

Generate an interface-only stub version of the codegen classes:

      ./pants ide-gen src/thrift::

* Be sure to include `scripts/fsqio/IntelliJ` as a source directory in your project.
* You do not need to include anything under `.pants.d`.
* You can exclude the `scripts/fsqio/IntelliJ/spindle_stubs/scalate_workdir` subdirectory created during codegen.

For now, you will need to re-run the ide-gen command any time you update the stub classes.
[![Build Status](https://travis-ci.org/foursquare/twofishes.svg?branch=master)](https://travis-ci.org/foursquare/twofishes)

A coarse, splitting geocoder and reverse geocoder in scala -- Prebuilt indexes and binaries available at [twofishes.net](http://twofishes.net/). Discussion at [google groups](https://groups.google.com/forum/?fromgroups#!forum/twofishes).

What is a Geocoder?
===================

A geocoder is a piece of software that translates from strings to coordinates. "New York, NY" to "40.74,  -74.0". This is an implementation of a coarse (city level, meaning it can't understand street addresses) geocoder that also supports splitting (breaking off the non-geocoded part in the final response).

Overview
========

This geocoder was designed around the geonames data, which is relatively small, and easy to parse in a short amount of time in a single thread without much post-processing. Geonames is a collection of simple text files that represent political features across the world. The geonames data has the nice property that all the features are listed with stable identifiers for their parents, the bigger political features that contain them (rego park -> queens county -> new york state -> united states). In one pass, we can build a database where each entry is a feature with a list of names for indexing, names for display, and a list of parents.

The Data
========

- [Twofishes Input Data File Documentation](docs/twofishes_inputs.md)


Geonames is great, but not perfect. Southeast Asia doesn't have the most comprehensive coverage. Geonames doesn't have bounding boxes, so we add some of those from http://code.flickr.com/blog/2011/01/08/flickr-shapefiles-public-dataset-2-0/ where possible.

Geonames is licensed under CC-BY http://www.geonames.org/. They take a pretty liberal interpretation of this and just ask for about page attribution if you make use of the data.
Flickr shapefiles are public domain

Reverse Geocoding and Polygons
==============================
To enable reverse geocoding in twofishes, you need to add polygon data to the inputs. geonames does not distribute polygons, nor does the twofishes distribution contain shapefiles. Shapefiles must be in epsg:4326 projection. The following script will write a copy of your shapefile with an extra property that is the geonameid of the matching feature.

I will add automated scripts for this soon, but for now, if you have shapefiles that map to existing geonames features that you want to put into twofishes
*   load geonames in postgis accoridng to https://github.com/colemanm/gazetteer/blob/master/docs/geonames_postgis_import.md
*   run the shape-gn-matchr script from  https://github.com/blackmad/shputils (see instructions below)
*   take the resulting shapefile (the shp, shx, cpg, dbf) and put them in data/private/polygons

examples:

US place (locality) data -- ftp://ftp2.census.gov/geo/tiger/TIGER2010/PLACE/2010/
~/shputils/shape-gn-matchr.py --shp_name_keys=NAME10 tl_2010_35_place10.shp gn-tl_2010_35_place10.shp

US county data -- ftp://ftp2.census.gov/geo/tiger/TIGER2010/COUNTY/2010/
../shputils/shape-gn-matchr.py --dbname=gis --shp_name_keys=NAME10 --allowed_gn_classes='' --allowed_gn_codes=ADM2 --fallback_allowed_gn_classes='' --fallback_allowed_gn_codes='' tl_2010_us_county10.shp gn-us-adm2.shp

MX locality data -- http://blog.diegovalle.net/2013/02/download-shapefiles-of-mexico.html
ogr2ogr -t_srs EPSG:4326  mx-4326.shp MUNICIPIOS.shp
./shputils/shape-gn-matchr.py --dbname=gis --shp_name_keys=NOM_MUN mx-4326.shp gn-mx-localities.shp

Requirements
============
*   Java (jre and jdk)
*   [Mongo](http://www.mongodb.org/display/DOCS/Quickstart)
*   curl
*   unzip

First time setup
================
*   clone the fsqio repo: `git clone https://github.com/foursquare/fsqio.git`
*   If you want to download country: ./src/jvm/io/fsq/twofishes/scripts/download-country.sh [ISO 3166 country code] (For example US, GB, etc)
*   If you want to download world: ./src/jvm/io/fsq/twofishes/scripts/download-world.sh

Data import
===========
*   mongod --dbpath /local/directory/for/output/
*   If you want to import countries: ./src/jvm/io/fsq/twofishes/scripts/parse.py -c US /output/dir (Note that you can specify list of countries separating them by comma: US,GB,RU)
*   If you want to import world: ./src/jvm/io/fsq/twofishes/scripts/parse.py -w /output/dir

Serving
=======
*   ./src/jvm/io/fsq/twofishes/scripts/serve.py -p 8080 /output/dir – Where /output/dir will contain a subdirectory whose name will be the date of the most recent build, for example `2013-02-25-01-08-23.803740`. You need to point to this subdirectory or to a folder called `latest` which is created during the build process (in the twofishes directory) and is a symlink to the most recent dated subdirectory.
*   server should be responding to finagle-thrift on the port specified (8080 by default), and responding to http requests at the next port up: <http://localhost:8081/?query=rego+park+ny> <http://localhost:8081/twofishes-static/geocoder.html#rego+park>
*   use the --host flag to specify a bind address (defaults to 0.0.0.0)
*   to enable hotfixes and allow refreshing, use the --hotfix\_basepath and --enable\_private\_endpoints params as detailed under [Hotfixes](#hotfixes) below 

NOTE: mongod is not required for serving, only index building.

Hotfixes
========
<a name="hotfixes"></a>
Hotfixes are expressed as fine-grained edits on top of features in the index. Features can be quickly added, removed or modified on a live server without requiring a full index rebuild and redeploy. Most fields on a [GeocodeServingFeature](https://github.com/foursquare/fsqio/blob/master/src/thrift/io/fsq/twofishes/geocoder.thrift#L225) and fields on its nested structs can be edited via a [GeocodeServingFeatureEdit](https://github.com/foursquare/fsqio/blob/master/src/thrift/io/fsq/twofishes/feature_edits.thrift#L35) object.

To enable hotfix support, the server can be pointed to a hotfix directory at startup via the --hotfix\_basepath param. Any .json files found in this directory will be deserialized from JSON to Thrift.

There is only basic tooling to build these JSON hotfix files at present. In [JsonHotfixFileBuilder.scala](https://github.com/foursquare/fsqio/blob/master/src/jvm/io/fsq/twofishes/server/JsonHotfixFileBuilder.scala), use `GeocodeServingFeatureEdit.newBuilder` to build up individual hotfixes in code. Then run src/jvm/io/fsq/twofishes/scripts/build-hotfix-file.py specifying an output file. I will provide a better way shortly.

The server can reload hotfixes on-demand via the /refreshStore endpoint. There is no authentication on this endpoint (or any other private endpoints), so it is disabled by default. Use the --enable\_private\_endpoints param to enable at your own risk, only if your servers are not publicly accessible. When enabled, calling this endpoint on an individual server will cause it to re-scan the hotfix_basepath directory. Use the helper script src/jvm/io/fsq/twofishes/scripts/refresh-store.py.

Troubleshooting
===============
If you see a java OutOfMemory error at start, you may need to up your # of mapped files

on linux: sysctl -w vm.max\_map\_count = 131072

Talking to the Server
=====================
- [Twofishes Request Format Documentation](docs/twofishes_requests.md)

Technical Details
=================
I use mongo to save state during the index building phase (so that, for instance, we can parse the alternateNames file, which adds name+lang pairs to features defined in a separate file, or adding the flickr bounding boxes). A final pass goes over the database, dereferences ids and outputs some hadoop mapfiles and hfiles. These two hfiles are all that is required for serving the data.

If we were doing heavier processing on the incoming data, a mapreduce that spits out hfiles might make more sense.

When we parse a query, we do a rough recursive descent parse, starting from the left. If being used to split geographic queries like "pizza new york" we expect the "what" to be on the left. All of the features found in a parse must be parents of the smallest

The geocoder currently may return multiple valid parses, however, it only returns the longest possible parses. For "Springfield, US" we will return multiple features that match that query (there are dozens of springfields in the US). It will not return a parse of "Springfield" near "US" with only US geocoded if it can find a longer parse, but it will return multiple valid interpretations of the longest parse.

Performance
===========
Twofishes can handle 100s of queries a second at < 5ms/query on average.

Point reverse geocoding is absurdly performant -- 1000s of queries a second at < 1ms/query.

Future
======
I'd like to integrate more data from OSM and possibly an entire build solely from OSM. I'd also like to get supplemental data from the Foursquare database where possible. If I was feeling more US-centric, I'd parse the TIGER-line data for US polygons, but I'm expecting those to mostly be in OSM.

Also US-centric are zillow neighborhood polygons, also CC-by-SA. I might add an "attribution" field to the response for certain datasources. I'm not looking forward to writing a conflater with precedence for overlapping features from different data sets.

Contributors
============
* David Blackman <blackmad@twitter.com>
* Rahul Maddimsetty <rahul@foursquare.com>
* John Gallagher <john@foursquare.com>
* Jeff Kao <jeffk@foursquare.com>
* Arkadiy Kukarkin <parkan@gmail.com>
* Neil Sanchala

Many thanks for assistance:
* Jorge Ortiz

Unrelated
=========
These are the two fishes I grilled the night I started coding the original python implementation <https://twitter.com/#!/whizziwig/statuses/154431957630066688>

mongo2postgis.py
----------------

Dump polygons from the indexer's intermediate mongo to PostGIS for easy visualization of shapes by woeType and source, using Tilestache + Mapnik, for example.
##########
# Wicket #
##########

Updated **February 4, 2013** by K. Arthur Endsley. Check out the [live demo](http://geojam.net/static/wicket/doc/).

#############
## License ##
#############

Wicket is released under the [GNU General Public License version 3 (GPLv3)](http://www.gnu.org/licenses/gpl.html).
Accordingly:

> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.

################
## Motivation ##
################

Wicket was created out of the need for a lightweight Javascript library that can translate Well-Known Text (WKT) strings into geographic features.
This problem arose in the context of [OpenClimateGIS](https://github.com/arthur-e/OpenClimateGIS), a web framework for accessing and subsetting online climate data.

OpenClimateGIS emits WKT representations of user-defined geometry.
The API Explorer allowed users to define arbitrary areas-of-interest (AOIs) and view predefined AOIs on a Google Maps API instance.
So, initially, the problem was converting between WKT strings and Google Maps API features.
While other mapping libraries, such as [OpenLayers](http://www.openlayers.org), have very nice WKT libraries built-in, the Google Maps API, as of this writing, does not.
In the (apparent) absence of a lightweight, easy-to-use WKT library in Javascript, I set out to create one.

That is what Wicket aspires to be: lightweight, framework-agnostic, and useful.
I hope it achieves these goals.
If you find it isn't living up to that and you have ideas on how to improve it, please fork the code or [drop me a line](mailto:kaendsle@mtu.edu).

##############
## Colophon ##
##############

########################
### Acknowledgements ###
########################

Many thanks to the following sources of inspiration, which retain all their original rights:

* The OpenLayers 2.7 WKT module (OpenLayers.Format.WKT)
* Chris Pietshmann's [article on converting Bing Maps shapes (VEShape) to WKT](http://pietschsoft.com/post/2009/04/04/Virtual-Earth-Shapes-%28VEShape%29-to-WKT-%28Well-Known-Text%29-and-Back-using-JavaScript.aspx)
* Charles R. Schmidt's and the Python Spatial Analysis Laboratory's (PySAL) WKT writer

Contributors:
* [cuyahoga](https://github.com/cuyahoga) - Option to reverse inner ring geometry in Google Maps API extension
* [Tom Nightingale (thegreat)](https://github.com/thegreat) - **Leaflet extension!**
* [Aaron Ogle](https://github.com/atogle)

#########################
### Build Information ###
#########################

Minified versions of JavaScript files were generated using Google's [Closure compiler](https://developers.google.com/closure/compiler/docs/gettingstarted_app).
Once installed, minification can be invoked at the command line, as in the following example:

    java -jar /usr/local/closure/compiler.jar --compilation_level WHITESPACE_ONLY --js wicket-leaflet.src.js --js_output_file wicket-leaflet.js 

###################
### Conventions ###
###################

The base library, wicket.js, contains the Wkt.Wkt base object.
This object doesn't do anything on its own except read in WKT strings, allow the underlying geometry to be manipulated programmatically, and write WKT strings.
By loading additional libraries, such as wicket-gmap3.js, users can transform between between WKT and the features of a given framework (e.g. google.maps.Polygon instances). 
he intent is to add support for new frameworks as additional Javascript files that alter the Wkt.Wkt prototype.

**To extend Wicket**, nominally by writing bindings for a new mapping library, add a new file with a name like wicket-libname.src.js (and corresponding minified version wicket-libname.js) where "libname" is some reasonably short, well-known name for the mapping library.

##############
## Concepts ##
##############

WKT geometries are stored internally using the following convention. The atomic unit of geometry is the coordinate pair (e.g. latitude and longitude) which is represented by an Object with x and y properties. An Array with a single coordinate pair represents a a single point (i.e. POINT feature)

    [ {x: -83.123, y: 42.123} ]

An Array of multiple points (an Array of Arrays) specifies a "collection" of points (i.e. a MULTIPOINT feature):

    [
        [ {x: -83.123, y: 42.123} ],
        [ {x: -83.234, y: 42.234} ]
    ]

An Array of multiple coordinates specifies a collection of connected points in an ordered sequence (i.e. LINESTRING feature):

    [
        {x: -83.12, y: 42.12},
        {x: -83.23, y: 42.23},
        {x: -83.34, y: 42.34}
    ]

An Array can also contain other Arrays. In these cases, the contained Array(s) can each represent one of two geometry types. The contained Array might reprsent a single polygon (i.e. POLYGON feature):

    [
        [
            {x: -83, y: 42},
            {x: -83, y: 43},
            {x: -82, y: 43},
            {x: -82, y: 42},
            {x: -83, y: 42}
        ]
    ]

It might also represent a LINESTRING feature. Both POLYGON and LINESTRING features are internally represented the same way. The difference between the two is specified elsewhere (in the Wkt instance's type) and must be retained. In this particular example (above), we can see that the first coordinate in the Array is repeated at the end, meaning that the geometry is closed. We can therefore infer it represents a POLYGON and not a LINESTRING even before we plot it. Wicket retains the *type* of the feature and will always remember which it is.

Similarly, multiple nested Arrays might reprsent a MULTIPOLYGON feature:

    [ 
        [
            [
                {x: -83, y: 42},
                {x: -83, y: 43},
                {x: -82, y: 43},
                {x: -82, y: 42},
                {x: -83, y: 42}
            ]
        ],
        [ 
            [
                {x: -70, y: 40},
                {x: -70, y: 41},
                {x: -69, y: 41},
                {x: -69, y: 40},
                {x: -70, y: 40}
            ]
        ]
    ]

Or a POLYGON with inner rings (holes) in it where the outer ring is the polygon envelope and comes first; subsequent Arrays are inner rings (holes):

    [ 
        [
            {x: 35, y: 10},
            {x: 10, y: 20},
            {x: 15, y: 40},
            {x: 45, y: 45},
            {x: 35, y: 10}
        ],
        [
            {x: 20, y: 30},
            {x: 35, y: 35},
            {x: 30, y: 20},
            {x: 20, y: 30}
        ]
    ]

Or they might represent a MULTILINESTRING where each nested Array is a different LINESTRING in the collection. Again, Wicket remembers the correct *type* of feature even though the internal representation is ambiguous.
Exceptionator
===============

An exception aggregator built on top of twitter finagle and mongodb.

![Exceptionator screenshot](http://cl.ly/image/1I2c2H0W1N3V/exceptionator-screenshot.png)


Usage
-----

#### Setup:

Download MongoDB [here](https://www.mongodb.org/downloads).

At Foursquare, we run a single instance of exceptionator next to a standalone `mongod` process, which is enough to handle the exception load of our production JVM fleet. To do this yourself:

```
mkdir mongo_data
path_to_mongo_download/bin/mongod --dbpath mongo_data
```

Note that exceptionator's data is ephemeral by nature, but you may still wish to run using a replica set or a sharded cluster. This will not be covered here.

For testing purposes, this is all that is needed. See the `History` section below for some additional recommended setup for a long-running deployment.

#### Running locally:

Exceptionator can be started locally with a single `./pants run` command. This will execute a pom resolve and compile, if necessary, before booting the server using settings in the included [config.json](https://github.com/foursquare/fsqio/blob/master/src/resources/io/fsq/exceptionator/config/config.json) file:

```
./pants run src/jvm/io/fsq/exceptionator
```

#### Deployment:

Exceptionator can also be bundled into a self-contained, runnable jar file (it will appear in the `dist` folder):

```
./pants binary src/jvm/io/fsq/exceptionator
```

The jar file will run standalone, so just copy it where needed and run with `java -jar`. To customize the server configuration when using this method, either modify the in-repo [config.json](https://github.com/foursquare/fsqio/blob/master/src/resources/io/fsq/exceptionator/config/config.json) prior to running `./pants binary` or place a new `config.json` in the working directory. Configuration can also be overridden as JVM properties on the command line.


Options and Defaults
--------------------

Configuration is json-based using a thin wrapper around the [Typesafe Config library](https://github.com/typesafehub/config).  A sample config file (just fill in any email account information) is provided [here](https://github.com/foursquare/fsqio/blob/master/src/resources/io/fsq/exceptionator/config/config.json). The default file location is `-Dconfig=config.json`, with fallback to the included sample file.

Some default values to note:

```
http.port: 8080
db.host: localhost:27017
db.name: test
git.repo: undefined
```


History
-------

#### Using:

Exceptionator is primarily useful for live monitoring, but it also supports sampled replay of exception notices that are no longer visible in the live UI. Simply click into any UI graph to access a realtime playback of history from that point in time.

History sampling is controlled through two config options. The defaults here will uniformly sample 50 notices from every 30 second time window:

```
history.sampleRate: 50
history.sampleWindowSeconds: 30
```

Note that if there are fewer than `sampleRate` total notices in a time window they will all be recorded.

#### Mongo setup:

Generally, exceptionator will handle creation of its collections and indexes on startup, and, assuming you are happy with the defaults mongo provides, there is no setup work required on the part of the user. The sole exception to this is the `history` collection which should be created as a capped collection. This is easy to do through a mongo shell after starting the `mongod` instance but before booting exceptionator for the first time:

```
path_to_mongo_download/bin/mongo localhost:27017
// in the mongo shell:
use test
var max_size_in_bytes = 10*1024*1024
db.createCollection('history', { capped: true, size: max_size_in_bytes })
// verify collection details, specifically that 'capped' and 'maxSize' are correct
db.history.stats()
exit
```

It is possible to forgo this step and cap the history collection later using the [convertToCapped](https://docs.mongodb.org/manual/reference/command/convertToCapped) command, but existing indexes will have to be recreated manually (or by restarting exceptionator).

Note that this could theoretically be handled by exceptionator itself. However, due to the ease of shooting oneself in the foot when working with capped collections (ex- resizing a capped collection requires dropping and recreating it from scratch), setup is being left to the user.


Git Blame Support
-----------------

Prerequisites:

*  Ensure that the running user has access to fetch new commits from git without entering credentials
*  Supply a valid git revision as `"v": "<revision>"` or as `"env": { "git": "<revision>" }`

To enable and configure git blame support:

*  Supply a local clone of the git repository in the `git.repo` option
*  Configure `backtrace.interesting.filter`, a list of regular expressions specifying lines to include when traversing down the stack to find who to blame (match at least one)
*  Optionally supply `backtrace.interesting.filterNot`, a list of regular expressions specifying lines to exclude when traversing down the stack to find who to blame (must match none)
*  Optionally supply `email.drop.excs`.  If a notice contains any of these exceptions, an email will not be sent.


Example Message
---------------

```json
{
  "bt": [
    "com.foursquare.lib.SoftError$.error (SoftError.scala:18)",
    "com.foursquare.api2.endpoints.Endpoint.handle (Endpoint.scala:45)",
    "com.foursquare.api2.RestAPIV2$$anon$1$$anonfun$apply$1.apply (RestAPIV2.scala:69)",
    "com.foursquare.api2.RestAPIV2$$anon$1$$anonfun$apply$1.apply (RestAPIV2.scala:65)",
    "net.liftweb.http.LiftServlet$$anonfun$1$$anonfun$apply$mcZ$sp$1.apply (LiftServlet.scala:260)",
    "net.liftweb.http.LiftServlet$$anonfun$1$$anonfun$apply$mcZ$sp$1.apply (LiftServlet.scala:260)",
    "net.liftweb.common.Full.map (Box.scala:491)",
    "net.liftweb.http.LiftServlet$$anonfun$1.apply$mcZ$sp (LiftServlet.scala:260)",
    ":------------------------------- SNIP -------------------------------"
  ],
  "env": {
    "cmd": "/data/loko/foursquare.web-api-jetty-r010837p1/bin/java -server -cp /data/loko/foursquare.web-api-jetty-r010837p1/webapp/ StartJetty",
    "mode": "Staging",
    "pid": "4165"
  },
  "excs": [
    "com.foursquare.lib.SoftException"
  ],
  "h": "dev-10.prod.foursquare.com",
  "msgs": [
    "com.foursquare.lib.SoftException: Indexing error: Query does not match an index! query: db.tiplists.find"
  ],
  "sess": {
    "domain": "general",
    "url": "soft error"
  },
  "v": "r010837"
}
```
# Rogue-Field

Rogue-Field is a set of interfaces for defining the fields of models.
It is used in [Rogue](https://github.com/foursquare/rogue),
a type-safe Scala DSL for executing queries against mongo,
and [Spindle](https://github.com/foursquare/spindle),
a Scala code generator for Thrift.


## Installation

In sbt, add:

    val rogueField      = "com.foursquare" %% "rogue-field"         % "2.2.2"

Join the [rogue-users google group](http://groups.google.com/group/rogue-users) for help, bug reports,
feature requests, and general discussion on Rogue.


## Releases

The latest release is 2.2.2. See the [changelog](https://github.com/foursquare/rogue-field/blob/master/CHANGELOG.md) for more details.

Major changes in 2.2.2:

- drop support for scala 2.9.2, add support for scala 2.11
# Spindle

Spindle is a Scala code generator for Thrift.
The complete documentation lives [here](http://spindle.readthedocs.org/en/v1.8/).

## Installation

Because Spindle is a code generator, it needs to plug into your build system.

If you're using sbt 0.12, you can use Spindle's thrift-codegen-plugin. In your project/plugins.sbt,
add the following line:

    addSbtPlugin("com.foursquare" % "spindle-codegen-plugin" % "1.8.3")

Then, in the build.sbt for the project with the *.thrift files to compile, add the following line:

    seq(thriftSettings: _*)

By default, the plugin will compile all *.thrift sources in src/main/thrift, though this is
configurable.

Keep in mind that this will add a few library dependencies to your project. Currently, this
includes spindle-runtime, apache thrift, joda-time, jackson, rogue-field, finagle-thrift, and
scalaj-collection. If you need a specific version of any of these dependencies, the plugin can be
configured to use those.

## Releases

The latest release is 1.8.3. See the [changelog](https://github.com/foursquare/spindle/blob/master/CHANGELOG.md) for more details.

Major changes in 1.8.x:

- Support for hashed, 2dsphere and text indices
- Map support in TReadableJSONProtocol
- TBSONProtocol improvements
- Unknown field handling for forwards-compatibility
- Codegen newtype implicits
- Groundwork for optional proxy generation
- Hooks for alternateFk

## Dependencies

Apache thrift, joda-time, jackson, rogue-field, finagle-thrift, and scalaj-collection.

## Contributors

Spindle was initially developed by Foursquare Labs for internal use.
Many people have contributed:

- Adam Powslowsky
- Ben Lee
- Benjy Weinberger
- Daniel Harrison
- Daniel Salinas
- David Blackman
- David Taylor
- Jackson Davis
- Jacob Van De Weert
- Jason Liszka
- Jorge Ortiz
- Matthew Rathbone
- Neil Sanchala
- Tom Dyas

Further contributions welcome!
## Spindle codegen package

The Spindle codegen binary(`src/jvm/io/fsq/spindle/codegen:binary`) has a circular dependency on
generated Spindle. If you want to make a change to Spindle codegen files, you must
have Spindle-generated thrift descriptors in order to compile that change.

This poses a problem.

We were forced to make a custom Pants plugin to handle this reality. This included checking-in
some known-good Spindle codegen, to be used solely during compiles of the Spindle codegen binary.
Upon changes to the codegen binary source, the plugin shells out to Pants mid-execution and
compiles only the codegenerator targets (and dependencies) in a Spindle-isolated sub run.

The workflow looks something like:

Run Pants
  do stuff
    if spindle transitive deps change:
       compile Spindle
  Spindle codegen rest of world
  compile rest of world
exit

You can see that process in the src/fsqio/pants/spindle files.

### Tags
All dependencies of src/jvm/io/fsq/spindle/codegen:binary must have the spindle_codegen tag,
and cannot have the spindle_runtime tag. This requirement hopes to keep the shelled run
from growing to include any more targets.
## DO NOT EDIT

These files are strictly for Spindle bootstrapping and should not
be changed.
## Spindle annotations

The `SpindleAnnotations` class is for accessing thrift annotations from scala code.

### What is an annotation?

```thrift
struct CarPartsOrder {
  1: optional int orderId
  2: optional int orderValue (currency="dollars")
  3: optional list<int> productids
} (
  table_name="car_parts_orders"
)
```

* `table_name` is a struct annotation
* `currency` is a field annotation -- SpindleAnnotations doesn't make these available yet

### Example

```ini
# pants.ini

[gen.spindle]
write_annotations_json: true
```

```scala
// Whatever.scala

// This will be a Map[String, Map[String, String]].
// i.e. {classBinaryName: {key: value}}
val map = SpindleAnnotations.mergedAnnotations()
```
# simple-macros #
A collection of simple Scala [macros](http://docs.scala-lang.org/overviews/macros/overview.html)

## Adding simple macros to your build ##
The project is compiled for Scala 2.10.4. In your build.sbt, add:

    "com.foursquare" %% "simple-macros" % "0.6"


## How to build ##
    ./sbt compile
    ./sbt test

## How to use ##
[API Documentation](http://foursquare.github.io/simple-macros/api)

## CodeRef Example ##
```scala
import com.foursquare.macros.CodeRef
import com.foursquare.macros.CodeRef._

// Explicit call. here now contains the
// current file (path relative to compiler wd)
// and line number
val here: CodeRef = CODEREF

// Implicit reference to caller.  Gives you the
// line from which the method was called without
// taking a stack trace.
def foo(bar: Int)(implicit caller: CodeRef) {
  println("called foo(" + bar + ") at " + caller)
}
foo(1)
```

## StackElement Example ##

```scala
import com.foursquare.macros.StackElement
import com.foursquare.macros.StackElement._

// Explicit call. here now contains the
// standard StackTraceElement (implicit from StackElement -> StackTraceElement)
scala> val here: StackTraceElement = STACKELEMENT

// Implicit reference to caller.  Gives you the
// StackTraceElement from which the method was called without
// taking a stack trace.
def foo(bar: Int)(implicit caller: StackElement) {
  println("called foo(" + bar + ") at " + caller)
}

foo(2)
```

## Contributors ##
- Jeff Jenkins
- John Gallagher
country_revgeo
==============

This library was imported from http://github.com/foursquare/cc-shapefiles.

The resources are fetched at build time from that same repo.
# Rogue

Rogue is a type-safe internal Scala DSL for constructing and executing find and modify commands against
MongoDB in the Lift web framework. It is fully expressive with respect to the basic options provided
by MongoDB's native query language, but in a type-safe manner, building on the record types specified in
your Lift models. An example:

    Venue.where(_.mayor eqs 1234).and(_.tags contains "Thai").fetch(10)

The type system enforces the following constraints:

- the fields must actually belong to the record (e.g., mayor is a field on the Venue record)
- the field type must match the operand type (e.g., mayor is an IntField)
- the operator must make sense for the field type (e.g., categories is a MongoListField[String])

In addition, the type system ensures that certain builder methods are only used in certain circumstances.
For example, take this more complex query:

    Venue.where(_.closed eqs false).orderAsc(_.popularity).limit(10).modify(_.closed setTo true).updateMulti

This query purportedly finds the 10 least popular open venues and closes them. However, MongoDB
does not (currently) allow you to specify limits on modify queries, so Rogue won't let you either.
The above will generate a compiler error.

Constructions like this:

    def myMayorships = Venue.where(_.mayor eqs 1234).limit(5)
    ...
    myMayorships.fetch(10)

will also not compile, here because a limit is being specified twice. Other similar constraints
are in place to prevent you from accidentally doing things you don't want to do anyway.

## Installation

Because Rogue is designed to work with several versions of lift-mongodb-record,
you'll want to declare your dependency on Rogue as `intransitive` and declare an explicit dependency
on the version of Lift you want to target. In sbt, that would look like the following:

    val rogueField      = "com.foursquare" %% "rogue-field"         % "2.5.0" intransitive()
    val rogueCore       = "com.foursquare" %% "rogue-core"          % "2.5.1" intransitive()
    val rogueLift       = "com.foursquare" %% "rogue-lift"          % "2.5.1" intransitive()
    val rogueIndex      = "com.foursquare" %% "rogue-index"         % "2.5.1" intransitive()
    val liftMongoRecord = "net.liftweb"    %% "lift-mongodb-record" % "2.6"

Rogue 2.5.x requires Lift 2.6-RC1 or later. For support for earlier versions of Lift, use Rogue 2.4.0 or earlier.
If you encounter problems using Rogue with other versions of Lift, please let us know.

Join the [rogue-users google group](http://groups.google.com/group/rogue-users) for help, bug reports,
feature requests, and general discussion on Rogue.

## Setup

Define your record classes in Lift like you would normally (see [TestModels.scala](https://github.com/foursquare/rogue/blob/master/rogue-lift/src/test/scala/com/foursquare/rogue/TestModels.scala) for examples).

Then anywhere you want to use rogue queries against these records, import the following:

    import com.foursquare.rogue.LiftRogue._

See [EndToEndTest.scala](https://github.com/foursquare/rogue/blob/master/rogue-lift/src/test/scala/com/foursquare/rogue/EndToEndTest.scala) for a complete working example.

## More Examples

[QueryTest.scala](https://github.com/foursquare/rogue/blob/master/rogue-lift/src/test/scala/com/foursquare/rogue/QueryTest.scala) contains sample Records and examples of every kind of query supported by Rogue.
It also indicates what each query translates to in MongoDB's JSON query language.
It's a good place to look when getting started using Rogue.

NB: The examples in QueryTest only construct query objects; none are actually executed.
Once you have a query object, the following operations are supported (listed here because
they are not demonstrated in QueryTest):

For "find" query objects

    val query = Venue.where(_.venuename eqs "Starbucks")
    query.count()
    query.countDistinct(_.mayor)
    query.fetch()
    query.fetch(n)
    query.get()     // equivalent to query.fetch(1).headOption
    query.exists()  // equivalent to query.fetch(1).size > 0
    query.foreach{v: Venue => ... }
    query.paginate(pageSize)
    query.fetchBatch(pageSize){vs: List[Venue] => ...}
    query.bulkDelete_!!(WriteConcern.ACKNOWLEDGED)
    query.findAndDeleteOne()
    query.explain()
    query.iterate(handler)
    query.iterateBatch(batchSize, handler)

For "modify" query objects

    val modify = query.modify(_.mayor_count inc 1)
    modify.updateMulti()
    modify.updateOne()
    modify.upsertOne()

for "findAndModify" query objects

    val modify = query.where(_.legacyid eqs 222).findAndModify(_.closed setTo true)
    modify.updateOne(returnNew = ...)
    modify.upsertOne(returnNew = ...)

## Releases

The latest release is 2.5.1. See the [changelog](https://github.com/foursquare/rogue/blob/master/CHANGELOG.md) for more details.

## Dependencies

lift-mongodb-record, mongodb, joda-time, junit. These dependencies are managed by the build system.

## Maintainers

Rogue was initially developed by Foursquare Labs for internal use --
nearly all of the MongoDB queries in foursquare's code base go through this library.
The current maintainers are:

- Jason Liszka jliszka@foursquare.com
- Jorge Ortiz jorge@foursquare.com
- Neil Sanchala nsanch@foursquare.com

Contributions welcome!
# Foursquare Finagle Http Library #

[Finagle](https://github.com/twitter/finagle) is a wonderful protocol agnostic communication library.
Building an http client using finagle is simple. However, building an http request and
parsing the response can ba a chore.
FHttp is a scala-idiomatic request building interface similar to
[scalaj-http](https://github.com/scalaj/scalaj-http) for finagle http clients.

Like [scalaj-http](https://github.com/scalaj/scalaj-http), it supports multipart data and oauth1.

You will probably want to override FHttpClient.service to add your own logging and tracing filters.

##How to Build##
    ./pants compile src/jvm/io/fsq/fhttp/
    ./pants test test/jvm/io/fsq/fhttp/test/

##[API Docs](http://foursquare.github.io.fsq.fhttp/api/)##


## Some Simple Examples ##
you can try these in `./pants repl src/jvm/io/fsq/fhttp/`


    import io.fsq.fhttp._
    import io.fsq.fhttp.FHttpRequest._
    import com.twitter.conversions.storage._
    import com.twitter.conversions.time._
    import com.twitter.finagle.builder.ClientBuilder
    import com.twitter.finagle.http.Http

    // Create the singleton client object using a default client spec (hostConnectionLimit=1, no SSL)
    val clientDefault = new FHttpClient("test", "localhost:80").releaseOnShutdown()

    // or customize the ClientBuilder
    val client = new FHttpClient("test2", "localhost:80",
        ClientBuilder()
          .codec(Http(_maxRequestSize = 1024.bytes,_maxResponseSize = 1024.bytes))
          .hostConnectionLimit(15)
          .tcpConnectTimeout(30.milliseconds)
          .retries(0)).releaseOnShutdown()

    // add parameters
    val clientWParams = client("/path").params("msg"->"hello", "to"->"world").params(List("from"->"scala"))

    // or headers
    val clientWParamsWHeaders = clientWParams.headers(List("a_header"->"a_value"))

    // non-blocking POST
    val responseFut = clientWParamsWHeaders.postFuture()

    // or issue a blocking request
    clientWParamsWHeaders.getOption()



## OAuth Example ##
    import io.fsq.fhttp._
    import io.fsq.fhttp.FHttpRequest._

    // Create the singleton client object using a default client spec
    val client = new FHttpClient("oauth", "oauthbin.appspot.com:80")
    val consumer = Token("key", "secret")

    // Get the request token
    val token = client("/v1/request-token").oauth(consumer).get_!(asOAuth1Token)

    // Get the access token
    val accessToken = client("/v1/access-token").oauth(consumer, token).get_!(asOAuth1Token)

    // Try some queries
    client("/v1/echo").params("k1"->"v1", "k2"->"v2").oauth(consumer, accessToken).get_!()
    // res0: String = k1=v1&k2=v2


## Dropbox OAuth Example ##
Here's a slightly more complicated oauth (and HTTPS) example, using a [Dropbox API](https://www.dropbox.com/developers/apps) account.

    import io.fsq.fhttp._
    import io.fsq.fhttp.FHttpRequest._
    import com.twitter.conversions.storage._
    import com.twitter.conversions.time._
    import com.twitter.finagle.builder.ClientBuilder
    import com.twitter.finagle.http.Http

    // Using the App key and App Secret, fill out the consumer token here:
    val consumer = Token(dbApiKey, dbApiSecret)

    val api = new FHttpClient("dropbox-api", "api.dropbox.com:443",
        ClientBuilder()
          .codec(Http())
          .tls("api.dropbox.com")
          .tcpConnectTimeout(1.second)
          .hostConnectionLimit(1)
          .retries(0))

    val reqToken = api("/1/oauth/request_token").oauth(consumer).post_!("", asOAuth1Token)

    // Go authorize usage of the app in a web browser using this link:
    println("""go visit

    https://www.dropbox.com/1/oauth/authorize?oauth_token=%s&oauth_token_secret=%s

    and accept the app!""".format(reqToken.key, reqToken.secret))


    // wait for the app to be accepted by the user


    // Finally, get the access token
    val accessToken = api("/1/oauth/access_token").oauth(consumer, reqToken).post_!("", asOAuth1Token)


    // and go do some stuff with it.
    api("/1/account/info").oauth(consumer, accessToken).get_!()
# Pants plugins

Foursquare's opensource Pants plugins are under this root.

## Available as plugins from PyPi
[We publish some of these plugins on PyPi](https://pypi.python.org/pypi?%3Aaction=search&term=fsqio&submit=search), including buildgen and pom-resolve.

Publishing as plugins means enables arbitrary Pants projects can consume just by adding config. There is some light documentation on how to do that at the buildgen [`README`](/src/python/fsqio/pants/buildgen/).

### How to publish to PyPi

The `Fsq.io` packages are registered to PyPi under the `opensource@foursquare.com` address email. Publishing an updated module requires the Fsq.io GPG key, you should ask the infrastructure team who has access to that.

### 1. Package the modules as sdists

1. Bump the version!
    - Set in the BUILD file for the target `python_library`
    - e.g. [fsqio.pants.buildgen.core](src/python/fsqio/pants/buildgen/core/BUILD)
1. Build the modules
    - `./pants setup-py src/python/fsqio::`
    - Look for the output tar.gz files in `dist/`
1. Optionally verify that the new tarballs work.

### 2. Publish to PyPI
Now that you have built the packages, we can upload them to PyPi. I use `twine` to handle the sign/upload.

1. Use your registered `foursquare.com` GPG key and password
    - This key must be registered to an owner of the `fsqio` account on PyPi.
    - Make sure that you see the key when you run `gpg --list-keys`.
1. Install `twine`.
      - `pip install twine`
1. Configure your pypi credentials
      - Create a `~/.pypirc` file:

            [pypi]
            username: <name>
            password: <password>

            [server-login]
            username: <name>
            password:<password>

1. Sign each `fsqio` buildgen package under `dist` in the pants checkout.
      - I use the `-u` flag to make sure I am using the correct GPG key

            cd dist
            gpg --detach-sign -u $PUB-KEY_DIGEST -a fsqio.pants.<package>-1.?.?.tar.gz

      - The `dist` folder should now have an `.asc` file for each of the buildgen modules.
1. Upload to PyPi

      - The `.asc` must be uploaded along with the package so that the signature can be verified.

             twine upload fsqio.pants.<package>-1.?.?.tar.gz fsqio.pants.<package>-1.?.?.tar.gz.asc

Now go to PyPi and make sure that the packages are there. You are done!
## Tag validation

Tags are used to enforce rules upon the build graph.
The common case is to restrict what can depend upon a given target, or to restrict the dependees of a target.

### Supported Tag types

      dependees_must_have
      dependencies_must_have
      dependencies_cannot_have

Tag validation is forced to happen as a prerequisite of codegen (`./pants gen` or a dependent task like compile/test).

Note: We exempt 3rdparty from tag requirements. Exemptions are done at directory level, not target level.
### Usage

An example using `dependencies_must_have`:

      scala_library(
        name = 'util',
        sources = globs('*.scala'),
        tags = ['fscommon', 'dependencies_must_have:fscommon'],
        dependencies = [
          '3rdparty:mongodb',
        ],
      )

Adding dependencies without that tag causes build failures.

      17:00:20 00:00     [parse]
                     Executing tasks in goals: tag -> validate
                     17:00:20 00:00   [tag]
      17:00:20 00:00     [tag]
      17:00:20 00:00   [validate]
      17:00:20 00:00     [validate]
                         Invalidated 4 targets.
                         src/jvm/io/fsq/foo:foo requires dependencies to have tag fscommon and thus cannot depend on src/jvm/io/fsq/bar:bar

### Using in a separate Pants repo
This should be a published Pants plugin on Pypi. But we haven't gotten to that. In the interim:

1. Copy these files from the foursquare/fsqio repo to your repo:

       src/python/fsqio/__init__.py
       src/python/fsqio/pants/__init__.py
       src/python/fsqio/pants/tags/__init__.py
       src/python/fsqio/pants/tags/register.py
       src/python/fsqio/pants/tags/validate.py

2. Add config similar to below.

       [GLOBAL]
       pythonpath: +[
           "%(buildroot)s/src/python",
         ]
         backend_packages: +[
           "fsqio.pants.tags",
         ]

         [tag]
       by_prefix:  {
           "3rdparty": ["exempt"],
           "tests": ["tests"],
           "src": ["dependencies_cannot_have:tests"]
         }
# Custom Export Task
This export task overrides the pants base task to accomplish two main purposes:
1. autogenerate the stubs used by IntelliJ to ease indexing pains
1. Filter out actual generated code for same reason

# Longer term approach (AKA TODO)
There are two possible approaches to the root cause (massive amounts of generated code chokes IntelliJ)
1. Allowing stub registration and a hot-swap from generated code to a generated stub within pants, submitting this product enhancement into mainline of pants and removing this customization
1. Reworking spindle code to interface --> implementation and programming to the interfaces rather than the concrete implementations. This is non-trivial and potentially impossible with the size of our code base, but it likely the "Most Correct" way of dealing with this issue. 

# Backing this customization out:
* Remove export reference from the pants.ini and pants-internal.ini
* Remove foursquare.web/src/python/fsqio/pants/export
* If a middle ground is required (keeping customization but refactoring it) the export_filtered.py file has TODO markings where the original code was altered. 

## Buildgen

Buildgen lexically parses import statements and updates existing BUILD files, ensuring correctness and removing human error.

### Installation
Buildgen for Scala projects requires a scalac plugin.This is also published from Fsq.io. Look at [BUILD.opensource](/BUILD.opensource) for an in-repo example on how to consume those.

The buildgen modules are [published to Pypi](https://pypi.python.org/pypi/fsqio.pants.buildgen.core) as [Pants plugins](https://www.pantsbuild.org/howto_plugin.html).
=======


To install from the published plugins, you can try using the upstream Pants `plugins` to automatically consume from pypi.

      plugins: [
          "fsqio.pants.buildgen.core==1.3.0",
          "fsqio.pants.buildgen.jvm==1.3.0",
          "fsqio.pants.buildgen.python==1.3.0",
        ]

      backend_packages: +[
          "fsqio.pants.buildgen.core",
          "fsqio.pants.buildgen.jvm",
          "fsqio.pants.buildgen.python",
      ]

Some people have had trouble getting their Pants virtualenv to play nicely with the buildgen modules.
In that case, an escape hatch can be to install into the Pants virtualenv by hand.

Assuming you use the standard location for your bootstrapped Pants install:

        ~/.cache/pants/setup/bootstrap/${pants_version}/bin/pip install fsqio.pants.buildgen.core fsqio.pants.buildgen.jvm fsqio.pants.buildgen.python

That should be it!




#### Submodule Installation

##### Scala
Add a `BUILD.tools` to the root of your repo with the following to bootstrap a required scalac plugin:
```
jar_library(
  name = 'buildgen-emit-exported-symbols',
  jars = [
    scala_jar(org = 'io.fsq', name = 'buildgen-emit-exported-symbols', rev = '1.2.0'),
  ],
)


jar_library(
  name = 'buildgen-emit-used-symbols',
  jars = [
    scala_jar(org = 'io.fsq', name = 'buildgen-emit-used-symbols', rev = '1.2.0'),
  ],
)
```

The versions in this code should work with any version of the PyPi module and no updates are expected.

##### Spindle
We now also publish a buildgen module for Spindle support.
Just follow the above pattern for `fsqio.pants.buildgen.spindle`


#### Troubleshooting
If you have multiple virtualenvs (or if Pants just can't find the buildgen backend),
you can add the installation path to your pythonpath in pants.ini


      [GLOBAL]

       pythonpath: [
           "%(homedir)s/.cache/pants/setup/bootstrap/1.3.1rc1/lib/python2.7/site-packages"
          ]


### Publishing

If you update this code in Fsq.io, you may want to publish an updated module to PyPi. You can follow the [standard plugin README](/src/python/fsqio/pants/README.md), with an additional step of potentially publishing the buildgen scalac plugin as jars.

**You should always be able to skip the scalac jar publish unless you have explicit reason not to!** Those jars are [already published](https://repo1.maven.org/maven2/io/fsq/) and basically never need to be updated.

##### Steps
1. Optional: Build and publish the Scala compiler plugins for JVM buildgen.
1. [Publish the buildgen plugins to PyPi](/src/python/fsqio/pants/).
## Formatting

### File template
Consider file `thrift_demo.thrift` below

```
namespace java io.fsq.XX.YY.gen

include "io/fsq/ids/ids.thrift"
include "io/fsq/common/types/types.thrift"

enum DemoEnum {
  firstValue = 0
  secondValue = 1
}

const i32 DemoConstant1 = 123
const DemoEnum DemoConstant2 = DemoEnum.firstValue

struct DemoStruct {
  1: optional ids.VenueId venueId (wire_name="_id")
  2: optional types.DateTime date (wire_name="dt", builder_required="true")
  4: optional i32 count (wire_name="c")
  6: optional ids.UserId userId (wire_name="u")
} (
  primary_key="venueId"
  foreign_key="userId"
  index="userId:asc"
  mongo_collection="demo"
  mongo_identifier="uva"
  retired_ids="3,5"
  retired_wire_names="a,b"
)
```

### Namespace and location
 * **Do not** add the python namespace unless you are **sure** you need it.
 * The namespace should be the path under `src/thrift/` plus `.gen`
   * test namespaces should end with `.test.gen`
 * The directory structure should exactly correspond to the namespace
    * `namespace java io.fsq.foo.gen` defined in `src/thrift/io/fsq/foo/gen/bar.thrift`
    * `namespace java io.fsq.foo.test.gen` defined in `test/thrift/io/fsq/foo/test/gen/bar.thrift`
 * This exactly matches the generated package structure
 * This is not always correctly done but should be followed as of this wiki page.

### Naming
 * Enums/Consts/Structs/Services are PascalCase
 * Members of those should be camelCase, outside of some cases which are kept inline with corresponding lift models
 * Annotations are c_style_casing
 * Filenames are c_style_casing

### Whitespace

* Follow the same general rules as scala (2 space indents, 120 chars, no trailing whitespace, blank lines between structs, etc)
* No spaces around the = for annotations

### Comments

Thrift also follows the same rules as scala (`//...` for single line, `/* */` for multiline)

### Field definitions
* Field ids start at 1 and increment from there.
* All structure fields must specify `optional`. You should never add a `required` field and be very careful with existing `required` fields. All fields in a struct saved to mongo (including the `_id`) should be optional. If you want to ensure a field as part of an object, use the `builder_requred="true"` annotation. Never change an optional field to be required
* Prefer our typesafe ids (eg `ids.VenueId` from `src/thrift/io/fsq/common/types/types.thrift`) to a standard `ObjectId` or creating your own.
* Fields are to be immutable after their creation, with the possible exception of some annotations. **Never change a field's id or type.**
* All structs being saved in mongo should have a `wire_name` annotation on every field. This is unnecessary for ones only being used elsewhere.
* Maps being stored in mongo must be string keyed because that is all that BSON supports.

### Structures
* Fields should be ordered by their field ids
* Whenever you remove a field, you must add the id to the `retired_ids` annotation and the wire name to the `retired_wire_names` annotation for mongo structs (if the field didn't have a defined `wire_name`, it was stored using the field's name)

### Annotations

Here is a incomplete list of important annotations you will probably run across or need. An important gotcha: when an annotation refers to a field it requires the fields thrift name not the wire_name.

* Anything going into mongo requires
  * `mongo_collection="bar"` The name of the collection to read/write from.
  * `mongo_identifier="foo"` The name of the mongo to read/write from.
  * `primary_key="fieldName"` The primary key of the collection (almost always whatever has the `wire_name="_id"`)
* Other mongo fields include
  * `foreign_key="fieldName"` Name any foreign keys with this annotation.
  * `index="fieldName:[asc,desc,hashed][,...]"` All indexes should be annotated on the record.
* delta service annotations
  * `soft_delete_field="deleted"` names the field to use as a tombstone to mark a record deleted. records with this annotation should *not* be deleted directly from mongo or bad things will happen.
  * `ttl_field="lastModifiedTimestamp"` is the name of the timestamp field. this is generally an index in mongo used to prune old records
  * `meta_extends="io.fsq.spindle.types.MongoDisallowed"` allows you to extend the MetaRecord class with arbitrary classes. in this specific case we use it to create a phantom type that disallows using our services.db directly with the record.
* Retired fields
  * `retired_ids="2,11,14"` Add or add to this annotation when you remove a field from a record
  * `retired_wire_names="latestNonSpecialUpdate,lu,c"` Add the `wire_name` or the field name to this annotation when you remove a field
* Proxies
  * `generate_proxy="1"` Creates a Proxy class that passes all methods through to an underlying Thrift object while allowing you to add your own methods. Ex: if you have a Foo Thrift model, this would generate a FooProxy class that you can inherit from while overriding `underlying: Foo`. It has all the methods that the original Foo model has (like `whateverFieldOption`, `whateverFieldOrThrow`, etc.), but by inheriting from the Proxy you can add your own extra methods.
* I don't remember what these do??
  * `generate_lift_adapter="1"`
  * `messageset_id="1359558803000"`

### Enum
* When deprecating an enum value, don't remove it. Rather, rename it from `foo` to `DEPRECATED_foo`. This way existing data with this enum will still make sense.
* `string_value`: useful when converting from scala enum and when the output ultimately ends up in an api response
* In general, avoid renaming enums since they might get denormalized to their name in redshift or elsewhere.

### Const
* Spindle gathers all constants into a single codegen-ed object whose name is derived by converting the thrift filename from c_style_casing to PascalCase and appending `Constants`. In the example above, the object is `com.foursquare.XX.YY.gen.ThriftDemoConstants`.
Mongo models used (via Rogue) by the Twofishes index builder script.
# JVM Properties file

The logging.properties is the default config for the JUL logger (aka `java.util.logging`).

## Motivation
The JVM loads logging framework based off classpath contents, which means that if a target doesn't explicitly depend on a specific logging framework, the JVM falls back the JUL.

For instance, when run internally, [Rogue](../../../../jvm/io/fsq/rogue) uses Foursquare's `slf4j` wrapper - but when run in the strict context of Fsq.io, it falls back to JUL logging.

#### Example
The primary use case here is for Fsq.io, since internally we configure these modules to use slf4j. The properties file here quiets the **very** chatty `mongodb` logging

* **Without** logging config:

        <much snipping>
        Aug 24, 2018 9:35:09 AM com.mongodb.diagnostics.logging.JULLogger log
        INFO: Opened connection [connectionId{localValue:59, serverValue:199}] to localhost:27017
        Aug 24, 2018 9:35:09 AM com.mongodb.diagnostics.logging.JULLogger log
        INFO: Opened connection [connectionId{localValue:63, serverValue:200}] to localhost:27017
        ......
        Time: 0

* **With** logging config:

        OK (0 tests)

        ........................................................................................................................................................................
        Time: 0


## Config
Passing logging config to the JUL backend is done through a JVM option:

        -Djava.util.logging.config.file=${BUILD_ROOT}/src/resources/props/logging.properties

We export this to Pants as an environmental variable, see `PANTS_JVM_TEST_JUNIT_OPTIONS` in the env.sh file.
## Pants Artifact Cache (HTTP) (v2)

DEPRECATED(mateo): We now [use s3 for the artifact cache](https://github.com/foursquare/pants/commit/0e1cd99ff611ae28703eaa6366e678dedea4fabd).

### Pants Setup
* In `pants.ini`, point Pants at

If your cache server is available at `http://your-dns-rr` where `your-dns-rr` answers with `A` records for your proxy nodes, configure Pants by editing `pants.ini`:

    [DEFAULT]

    local_artifact_caches: ["%(pants_bootstrapdir)s/artifact_cache"]
    remote_artifact_caches: ["http://your-dns-rr"]
    all_artifact_caches: [
        "%(local_artifact_cache)s",
        "%(remote_artifact_cache)s"
      ]

      [cache]
      read_from: ["%(all_artifact_caches)s"]
      write_to: ["%(local_artifact_cache)s"]

This config allows local developers to consume the remote cache and write locally. Update your CI config to allow writes to the remote cache (e.g. `pants-jenkins.ini`).

### Cache Server
* We use nginx as the underlying RESTful server, as it supports `GET`, `HEAD`, `PUT` and `DELETE`. It stores the artifact files on three nginx servers at `/export/hd[bcd]` which are hit in round robin. See `/etc/nginx/nginx.conf` for details.

![artifact cache topology](resources/docs/images/artifact_cache_topology-v2.png)

The `nginx.conf` is checked into the repo at `v2/nginx/nginx.conf`

### Cache Server setup
* Add servers to the `nginx.conf` (as many as you like).

For `HEAD`s and `PUT`s we have to proxy the traffic because Pants cannot follow redirects for those verbs. `PUT`s are low traffic and `HEAD`s aren’t too expensive to proxy. If a `GET` is sent to the wrong server then redirect.

Since we are using SSDs, we are omitting varnish for simplicity of design and can add it later if we need it.

### Endpoints
Each nginx node represents two endpoints: one for proxying to the right shard, and one for serving requests.
#### The proxy node (port 80)
* Use consistent hashing to figure out which node in the fleet is the correct shard.
* Proxy (stream) all requests through to that node.
* Set a header (the hostname of the proxy node) to make it possible for the upstream backend node to return a redirect if necessary.

#### The backend node (port 8080)
* Serve `HEAD` and `PUT` requests directly using normal DAV operations on a directory.
* For `GET` requests where the proxy node is the same as the backend node, serve the request directly.
* For `GET` requests where the proxy node is not the same as the backend node, return a redirect to the current backend node.  Pants will follow this redirect, and we get to avoid proxying the large data stream through the proxy node (pants fetches it directly after following the redirect).
* For `GET` requests where the proxy node header isn't set, assume we are satisfying a redirect and serve the request directly.

With DNS RR, we get easy load balancing among the proxy nodes while maintaining sharding for the highest throughput access (lots of `GET`s).

### Configuration files
The `nginx.conf` should be placed on the artifact cache machine at `/etc/nginx/nginx.conf`.


### Cleanup
The hosts relied on a cron job that cleaned old artifacts:

    SHELL=/bin/bash
    PATH=/sbin:/bin:/usr/sbin:/usr/bin
    MAILTO=root
    HOME=/

    # For details see man 4 crontabs

    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed
      0  2  *  *  * nginx tmpwatch 3d /export/hdd3/data/appdata/nginx/pantscache/ /export/hdd3/data/appdata/nginx/tmp/
## Publish Pushdb

The pushdb is Pants database of publish information. Each published jar will have an entry with the library's version and commit it was created from.


### Fsq.io
Fsq.io is generally a strict subset of our internal repo - changes only originate internally and are migrated out to Fsq.io.

The pushdb is the only exception - these files originate in Fsq.io and are backported internally. Jars are published directly from a checkout of Fsq.io, _not_ our internal repo.

      cd fsqio
      ./pants publish \
      --no-gen-spindle-write-annotations-json \
      --doc-scaladoc-include-codegen \
      src/jvm/io::

This is so external consumers of an Fsq.io library can cross-reference the jars and have commits that represent the actual publish.
