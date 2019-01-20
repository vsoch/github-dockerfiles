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
