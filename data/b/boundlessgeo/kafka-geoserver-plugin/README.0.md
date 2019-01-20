These files come from the OpenLayers distribution.

Originally, they were an svn link (using svn:externals),
but now we're shipping with the compressed OpenLayers.js
that can be found here:
http://trac.openlayers.org/wiki/HowToDownload

The img/ and themes/ directories are verbatim copies of
the OpenLayers distribution.

At the time of writing we're shipping with OpenLayers 2.8

Update this file every time you upgrade to track what's the
current version of OpenLayers we ship with.

This compressed build is a build of the full OpenLayers library.  
For production environments, it will likely be appropriate to use
a smaller build profile.

For information on building OpenLayers, see
http://trac.openlayers.org/wiki/ProfilesResources needed in teh image at build time should be placed here.
Download plugin zips and place them here when building to include them in
the container's GeoServer deployment.
To include files in the container file system at arbitrary locations, build
a directory structure from / here and include the files at the desired location.

For example, to include a static Tomcat setenv.sh in the build, place it at:

resources/overlays/usr/local/tomcat/bin/setenv.sh

Other overlay examples include static GeoServer data directories, the Marlin renderer, etc.

Note that overlay files will overwrite existing destination files, and that
files in the overlay root will be copied to the container root
(e.g. resources/overlay/somefile.txt will be copied to /somefile.txt).

Be careful!
Included Data
=============

This directory provides a GeoServer data directory packaged as part of our product downloads:

* http://geoserver.org/display/GEOS/Download

The data directory includes the following sets of information:

* arc_sample
* img_sample
* mosaic_sample
* nyc (giant polygon, poi, poly landmark, tiger roads)
* sf (archsites,bugsites,restricted,roads,streams, sfdem)
* shapefiles(states)
* taz_shapes( cities, roads, state boundaries, water bodies)

ARC Sample
----------

Data was provided by GeoSolutions with redistribution rights.

IMG Sample
----------

Data was provided by GeoSolutions with redistribution rights.

MOASIC Sample
-------------

Data was provided by GeoSolutions with redistribution rights.

New York City
-------------

Data was provided by the Open Planning Project, processed from United States Census Bureau's Topologically Integrated Geographic Encoding and Referencing (TIGER) dataset.

Spearfish
---------

Spearfish sample data has been provided by GRASS.

* http://grass.osgeo.org/download/sample-data/

To quote from the http://grass.osgeo.org/uploads/grass/sampledata/spearDB.pdf ::

    A majority of this spearfish database was initially provided to USACERL by the EROS Data Center
    (EDC) in Sioux Falls, SD. The GRASS Development staff expresses acknowledgement and thanks to: the
    U.S. Geological Survey (USGS) and EROS Data Center for allowing us to distribute this data with our
    release of GRASS software; and to the U.S. Census Bureau for their samples of TIGER/Line data and the
    STF1 data which were used in the development of the TIGER programs and tutorials. Thanks also to
    SPOT Image Corporation for providing multispectral and panchromatic satellite imagery for a portion of
    the spearfish data set and for allowing us to distribute this imagery with GRASS software. In addition to
    the data provided by the EDC and SPOT, researchers at USACERL have developed several new layers, thus
    enhancing the spearfish data set.

States
------

Coming from GeoTools sample data, simplified. The GeoTools file (statepop.shp) comes from Census data (by memory of people that imported it)

Tasmania
--------

The data is derived from the <Digital Chart of the World `http://en.wikipedia.org/wiki/Digital_Chart_of_the_World`> , which according to wikipedia is "is freely available as of 2006".

Referenced Copyright Statement:
http://en.wikipedia.org/wiki/Vector_map#Copyrights


The U.S. government has released the data into public domain, with the following conditions imposed (quotation from VMAP0 Copyright Statement)::

    As an agency of the United States government, NIMA makes no copyright claim under Title 17 of the United States Code with respect to any copyrightable material compiled in these products, nor requires compensation for their use.
    When incorporating the NIMA maps into your product, please include the following:
    a. "this product was developed using materials from the United States National Imagery and Mapping Agency and are reproduced with permission",
    b. "this product has neither been endorsed nor authorized by the United States National Imagery and Mapping Agency or the United States Department of Defense".

    With respect to any advertising, promoting or publicizing of this product, NIMA requires that you refrain from using the agency's name, seal, or initials. 

