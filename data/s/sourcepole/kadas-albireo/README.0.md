Model Test
----------

This is a simple tool from Qt for checking various errors of custom
implementations of models for item views.

http://developer.qt.nokia.com/wiki/Model_Test
Mac Notes

The 'cmake' folder scripts handle bundling dependent libraries in the QGIS
application package and fixing up the library paths.  It is automatic during
installation.  There are 2 levels currently, specified with the cmake config
option QGIS_MACAPP_BUNDLE, and one that always occurs:

0 = (default) fixup the library paths for all QGIS libraries if @loader_path
    is available in the system (OS X 10.5+)
1 = bundle Qt, PyQt, PyQwt and OSG/osgEarth
2 = additionally, bundle libraries, but not frameworks

A third level that is not finished will additionally bundle frameworks.
This would create the "standalone" QGIS.

There is also a configure option to set a user bundle script,
QGIS_MACAPP_BUNDLE_USER.  This specifies the path to a cmake bundle script
similar to the built-in bundle scripts for the defined levels. This script is
always run independent of and after the QGIS_MACAPP_BUNDLE level specified.
Running tests
=============

You can run all tests using "make check".

Individual tests can be run using ctest.
For example if the output of "make check" ends like this:

   The following tests FAILED:
         77 - PyQgsLocalServer (Failed)

You could re-run the failing test with:

   ctest -V -R PyQgsLocalServer

    Time measurement
   ------------------

For usable benchmarking we need a precise, reliable and repeatable time measurement. It seems to be easy? We are on computer right? Unfortunetly I found it almost impossible! Hopefully I am totaly wrong. 

Several "kind of time" exist: real (wall clock), user CPU time, system CPU time. What I believe we have to use is task user + system CPU time.

There are varions commands/functions which can be used to measure time, e.g.:

1) time command (real, user, sys time):

    time COMMAND

2) getrusage function (user, sys time):

    #include <sys/time.h>
    #include <sys/resource.h>
    struct rusage usage;
    getrusage( RUSAGE_SELF, &start);
    // measured code
    getrusage( RUSAGE_SELF, &end);
    double user_elapsed = end.ru_utime.tv_sec + end.ru_utime.tv_usec/1000000. - start.ru_utime.tv_sec - start.ru_utime.tv_usec/1000000.;
    double sys_elapsed = end.ru_stime.tv_sec + end.rs_utime.tv_usec/1000000. - start.ru_stime.tv_sec -start.ru_stime.tv_usec/1000000.;


3) times function (user, sys time):

    #include <sys/times.h>
    struct tms start, end;
    times(&start);
    // measured code
    times(&end);
    double user_elapsed = ((double)(end.tms_utime - start.tms_utime))/sysconf(_SC_CLK_TCK);
    double sys_elapsed = ((double)(end.tms_stime - start.tms_stime))/sysconf(_SC_CLK_TCK);

4) clock function (user + sys time ?):

    #include <time.h>
    clock_t start = clock();
    // measured code
    clock_t end = clock();
    double elapsed = ((double) (end - start)) / CLOCKS_PER_SEC;

5) clock_gettime functions (user + sys time ?):

    #include <time.h>
    struct timespec start, end;
    clock_gettime( CLOCK_PROCESS_CPUTIME_ID, &start );
    // measured code
    clock_gettime( CLOCK_PROCESS_CPUTIME_ID, &end );
    double elapsed = end.tv_sec + end.tv_nsec / 1000000000. - start.tv_sec - start.tv_nsec / 1000000000.;

6) QTime class (QElapsedTimer Qt >= 4.7) (real time):

    QTime time;
    time.start();
    // measured code
    double elapsed = time.elapsed() / 1000.;

I tried all of them and all are giving the same mostly useless values. If the same piece of code is measured more times, the results differ. It seems that all those functions read user time from the same place, kernel task_struct.utime. The problem is, if I understand correctly, how the task_struct.utime is updated. Whenever timer interrupt comes (every 1/HZ) to scheduler, it calls update_process_times->account_process_tick->irqtime_account_process_tick->account_user_time and increases task_struct.utime by cputime_one_jiffy (1/HZ). See kernel/sched.c and kernel/timer.c. It means, that utime is not increased by pure time when the the task code is running, but by fixed interval which includes some task switching overhead??? In a simple test, I could observe 30% increas of utime if another application was running at the same time.

Unfortunately I don't see anything better than user time + sys time, running test with highest priority and avoiding other use of computer when tests are running, e.g.:

    sudo chrt -f 99 COMMAND

To be sure that the measured values are correct, it is necessary to run more cycles and check some standard deviation or so.

There is also high level benchmark support available in QTestLib, it is possible to use QBENCHMARK macro + QTEST_MAIN to create easily test executable. Such test may be run with various options, some notes on modes/options:

-tickcounter - reads rdtsc register (on Linux), thus it counts real time, result is not constant

-callgrind - reruns the command with callgrind, number of 'instr. loads' is constant for constant number of iterations, number of instructions per iterarion decreases with number of iterarions (for small numbers of iterations) for a simple function the number of instractions of the second iteration may be 40% of the first one - cache, prediction??? Callgrind is realy very slow. I am not sure what 'instr. loads' exactly means and if it can be somehow converted to time, but I don't believe so. AFAIK each instruction need a different number of cycles and it may be different even for the same instruction because of CPU cache, then there are instruction pipelines etc.


    Build options
    -------------

CMAKE_BUILD_TYPE should be RelWithDebInfo so that it compiles with optimisations but also adds debug information so that it can be profiled with callgrind and visualized with kcachegrind.
Contained herin is the Bitstream Vera font family.

The Copyright information is found in the COPYRIGHT.TXT file (along
with being incoporated into the fonts themselves).

The releases notes are found in the file "RELEASENOTES.TXT".

We hope you enjoy Vera!

                        Bitstream, Inc.
			The Gnome Project
    WCS test server installation
    ----------------------------
WCS test server is based on UMN MapServer running on qgis.org. 

1. Install UMN MapServer (mapserver.org) version 6.0 or higher with WCS support (--with-wcs configure option if compiled from source)

2. Copy test data from qgis source tests/testdata/raster somewhere on server, for example to /var/www/data/test/1.9.0/tests/testdata/raster.

3. Edit WCS mapfile, for example /var/www/data/test/1.9.0/tests/testdata/raster/wcs.map and set SHAPEPATH to the path where data were copied, e.g.:
    SHAPEPATH "/var/www/data/test/1.9.0/tests/testdata/raster/"

4. Create script in cgi-bin dir where mapfile is specified, e.g. /usr/lib/cgi-bin/wcstest-1.9.0:

    #! /bin/sh
    MS_MAPFILE=/var/www/data/test/1.9.0/tests/testdata/raster/wcs.map
    export MS_MAPFILE
    ./mapserv

5. Configure Web server, for example if Apache is used, add rewrite rule to config file using /test/<version>/wcs path:

    RewriteRule /test/1.9.0/wcs /cgi-bin/wcstest-1.9.0 [PT]

6. WARNING: If possible, don't change WCS server URL for released versions. If the server URL has to be changed for development and future versions, change also the variable TEST_SERVER_URL in tests/src/providers/CMakeLists.txt.
*******************
Labeling Unit Tests
*******************

Design and Organization
=======================

The labeling unit tests are solely written in Python and are organized so that
individual tests are separated from, but inherited by, the output frameworks.
This allows maintaining output-agnostic units, focusing only on the code to be
tested, which the frameworks will use to generate as many tests as necessary,
cross-referencing outputs as needed.

The goal of this design, beyond API and regression testing, is to ensure labels
crafted by users have as close to a WYSIWYG rendering as possible across all
potential outputs and platforms. Exact parity is not achievable; so the test
suite is designed to be flexible enough to maintain a 'best case' scenario.

Modules
-------

test_qgspallabeling_base
    Provides the ``TestQgsPalLabeling`` base class, which is inherited by all
    other test classes. ``TestPALConfig`` tests the configuration of the PAL
    placement engine, and project and map layer settings.

test_qgspallabeling_tests
    Individual unit tests are to be placed here, unless a test *needs* to be
    placed in a specific test subclass. Tests are separated into logical
    groupings for labeling: `single point`, `single line`, `single polygon`,
    `multi-feature`, `placement`. Most label styling tests that are not
    feature-dependent are associated with `single point`.

    Almost all tests produce many images for comparison to controls. To keep
    the proliferation of control images to a minimum, several options can be
    grouped, e.g. SVG background, with buffer, offset and rotation. If such a
    grouping is found to be problematic, it can be separated later.

    Some values for specific, inherited class/function tests can be passed; for
    example, pixel mismatch and color tolerance values for image comparison::

        def test_default_label(self):
            # Default label placement, with text size in points
            self._Mismatches['TestComposerPdfVsComposerPoint'] = 760
            self._ColorTols['TestComposerPdfVsComposerPoint'] = 18
            self.checkTest()

    Values would replace the default values for the module or class, if any, for
    the ``TestComposerPdfVsComposerPoint.test_default_label`` generated test.

test_qgspallabeling_canvas
    ``TestCanvas*`` framework for map canvas output to `image`.

test_qgspallabeling_composer
    ``TestComposer*`` framework for composer map item output to `image`, `SVG`
    and `PDF`. Compares *composition->image* against *canvas->image*, and other
    composer outputs against *composition->image*.

    **Requires:** PDF->image conversion utility, e.g. Poppler, with Cairo
    support: `pdftocairo`.

test_qgspallabeling_server
    ``TestServer*`` framework for ``qgis_mapserv.fcgi`` output to `image`.
    Compares *qgis_mapserv->image* against *canvas->image*. Utilizes the
    ``qgis_local_server`` module.

qgis_local_server
    A local-only, on-demand server process controller to aid unit tests. It is
    launched with a custom configuration and independently manages the HTTP and
    FCGI server processes.

    **Requires:** HTTP and FCGI-spawning utilities, e.g. `lighttpd`
    and `spawn-fcgi`.

test_qgis_local_server
    Unit tests for ``qgis_local_server``.

Running the Suite
=================

Since the overall suite and frameworks will generate many units, making manual
management of label tests quite tedious, there are extra tools provided to aid
unit test authors. The tools are generally triggered via setting environment
variables, though some work sessions may require un/commenting configuration
lines in multiple files.

Test modules can be run on the command line using CTest's regex support. The
CTest name is listed in the module's docstring, e.g. PyQgsPalLabelingCanvas::

    # run just test_qgspallabeling_canvas in verbose mode
    $ ctest -R PyQgsPalLabelingCanvas -V

    # run all PAL test modules; all CTest names start with PyQgsPalLabeling
    $ ctest -R PyQgsPalLabeling

Environment variables
---------------------

These are all flags that only need to be set or unset, e.g. (using bash)::

    # set
    $ export PAL_VERBOSE=1

    # unset (note: export PAL_VERBOSE=0 will NOT work)
    $ unset PAL_VERBOSE

PAL_VERBOSE
    The Python unit test modules, as run via CTest, will not output individual
    class/function test results, only whether the module as a whole succeeded or
    failed. Setting this variable will print individually run class/function
    test results, up to the point where any exception is raised.

    In addition to setting the variable, CTest needs run in verbose mode.

    **Sample session**::

        $ cd <qgis-build-dir>
        $ export PAL_VERBOSE=1
        $ ctest -R PyQgsPalLabelingCanvas -V
        ...
        85: test_default_label (__main__.TestCanvasPoint) ... ok
        85: test_text_size_map_unit (__main__.TestCanvasPoint) ... ok
        85: test_text_color (__main__.TestCanvasPoint) ... ok
        85: test_background_rect (__main__.TestCanvasPoint) ... FAILED
        ...
        85: ----------------------------------------------------------
        85: Ran X tests in X.Xs

        1/1 Test #85: PyQgsPalLabelingCanvas ...........   FAILED    X.XX sec

        The following tests failed:
            PyQgsPalLabelingCanvas

PAL_REPORT
    Setting this variable will open an HTML report of any failed image
    comparisons as a grouped report in your default web browser. This is the
    HTML output from ``QgsRenderChecker`` wrapped in a local report. It is
    **highly recommended** setting this when creating new unit tests to visually
    debug any issues *before* committing. Otherwise, all other nightly test
    machines may build and run tests, flooding the online test collation server
    with possibly avoidable CDash failed test reports.

PAL_SUITE
    Since you cannot define specific class/function tests when running the
    modules via the CTest command, setting this variable will allow defining
    specific tests to run, e.g. any number of class/function tests, suite
    groupings, or all tests.

    All base units and suite groupings are listed in ``suiteTests()`` of
    ``test_qgspallabeling_tests``, with all unit tests commented out by default.
    (Please keep them commented out when committing.)

    Some modules, like ``test_qgspallabeling_composer``, generate tests for
    multiple outputs or cross-reference comparisons. Those files have the test
    suite separately extended, per line, to help define test selection.

    **Sample session**::

        $ cd <qgis-build-dir>
        $ export PAL_VERBOSE=1
        $ export PAL_SUITE=1

        $ nano <qgis-src-dir>/tests/src/python/test_qgspallabeling_tests.py
          # uncomment units you want to test
          # e.g. only 'test_default_label', is now active

        $ nano <qgis-src-dir>/tests/src/python/test_qgspallabeling_composer.py
          # comment-out undesired extended suite lines, i.e. suite.extend(*)
          # e.g. only 'suite.extend(sp_pvs)' is now active
          # note: this step is unnecessary for modules without extended suites
          # or when you wish to test all available suites

        $ ctest -R PyQgsPalLabelingComposer -V

    Above will only run ``TestComposerPdfVsComposerPoint.test_default_label`` in
    verbose mode and no other tests. This is especially useful for debugging a
    single test or group, and for (re)building control images.
    See PAL_CONTROL_IMAGE.

PAL_NO_MISMATCH and PAL_NO_COLORTOL
    Some test classes or units may have a default allowable pixel mismatch
    and/or color tolerance value for image comparison. Reset the allowable
    mismatch or tolerance to *zero* by setting one (or both) of these variables,
    effectively bypassing all defined defaults. Either of these, coupled with
    PAL_REPORT, helps determine actual differences and whether defaults are
    allowing (masking) a false positive result.

PAL_CONTROL_IMAGE
    Setting this variable will (re)build control images for selected tests.
    When being rebuilt, the associated unit test should *always* pass. Any class
    that contains a 'Vs' string, i.e. all cross-comparison checks, will not
    have images built, since the rendered test image is always compared against
    an existing control image of a different test class.

    **CAUTION:** Do not leave this set. Unset it immediately after building any
    needed control images. You can reset any accidentally overwritten control
    images using ``git``, however.

PAL_SERVER_TEMP
    Used only in ``test_qgspallabeling_server``. When set, opens the temporary
    HTML server directory, instead of deleting it, upon test class completion.
    This is useful when debugging tests, since the directory contains server
    process logs and the generated test project file.
QSPATIALITE driver derived from QSQLITE driver.

No actual changes except linking to spatialite and a call to
spatialite_init(0).

See the Qt SQL documentation for more information on compiling Qt SQL
driver plugins (sql-driver.html).
QOCISPATIAL driver derived from QOCI driver.

You will need the Oracle development headers and libraries installed
before compiling this plugin.

See the Qt SQL documentation for more information on compiling Qt SQL
driver plugins (sql-driver.html).
Welcome to your automatically generated plugin!
-------------------------------------------------------------

This is just a starting point. You now need to modify the code to make it do
something useful....read on for a more information to get yourself started.

Documentation:
-------------------------------------------------------------

You really need to read the QGIS API Documentation now at:

http://qgis.org/api/

In particular look at the following classes:

QGisInterface : http://qgis.org/api/classQgisInterface.html
QgsMapCanvas  : http://qgis.org/api/classQgsMapCanvas.html
QgsMapTool    : http://qgis.org/api/classQgsMapTool.html
QgisPlugin    : http://qgis.org/api/classQgisPlugin.html

QGisInterface is an abstract base class (ABC) that specifies what publicly
available features of QGIS are exposed to third party code and plugins. An
instance of the QgisInterface is passed to the plugin when it loads. Please
consult the QGIS development team if there is functionality required in the
QGisInterface that is not available.

QgsPlugin is an ABC that defines required behaviour your plugin must provide.
See below for more details.

What are all the files in my generated plugin directory for?
-------------------------------------------------------------

CMakeLists.txt
This is the generated CMake file that builds the plugin. You should add you
application specific dependencies and source files to this file.

[pluginlcasename].h
[pluginlcasename].cpp
This is the class that provides the 'glue' between your custom application
logic and the QGIS application. You will see that a number of methods are
already implemented for you - including some examples of how to add a raster or
vector layer to the main application map canvas. This class is a concrete
implementation of QgisPlugin (which defines required behaviour for a plugin).
In particular, a plugin has a number of static methods and members so that the
QgsPluginManager and plugin loader logic can identify each plugin, create an
appropriate menu entry for it etc. Note there is nothing stopping you creating
multiple toolbar icons and menu entries for a single plugin. By default though
a single menu entry and toolbar button is created and its pre-configured to
call the run() method in this class when selected. This default implementation
provided for you by the plugin builder is well documented, so please refer to
the code for further advice.

[pluginlcasename]gui.ui
This is a Qt designer 'ui' file. It defines the look of the default plugin
dialog without implementing any application logic. You can modify this form to
suite your needs or completely remove it if your plugin does not need to
display a user form (e.g. for custom MapTools).


[pluginlcasename]gui.cpp
[pluginlcasename]gui.h
This is the concrete class where application logic for the above mentioned
dialog should go. The world is your oyster here really....

[pluginlcasename].qrc
This is the Qt4 resources file for your plugin. The Makefile generated for your
plugin is all set up to compile the resource file so all you need to do is add
your additional icons etc using the simple xml file format. Note the namespace
used for all your resources e.g. (":/[pluginname]/"). It is important to use
this prefix for all your resources. We suggest you include any other images and
run time data in this resurce file too.

[pluginlcasename].png
This is the icon that will be used for your plugin menu entry and toolbar icon.
Simply replace this icon with your own icon to make your plugin disctinctive
from the rest.

README
This file contains the documentation you are reading now!


Getting developer help:
-------------------------------------------------------------

For Questions and Comments regarding the plugin builder template and creating
your features in QGIS using the plugin interface please contact us via:

 * the QGIS developers mailing list, or
 * IRC (#qgis on freenode.net)

QGIS is distributed under the Gnu Public License. If you create a useful plugin
please consider contributing it back to the community.

Have fun and thank you for choosing QGIS.

The QGIS Team
2007
##############################################
    QGIS PLUGIN TEMPLATE DIRECTORY

              T.Sutton 2004
##############################################

Please do not edit the files in this directory
unless you know exactly what you are doing -
these files are used as the basis for creating
new plugins. Altering these files may break
the automated plugin template generation process.

Please visit: http://qgis.org/pyqgis-cookbook/

For more information on creating plugins.
Spatial Query Plugin for QGIS

   Luiz Motta and Diego Moreira 2009

Plugin for make spatial query with two layers
where features of target layer are selected by topological operations
with reference layer
eVis - The Event Visualization Tool

Lead Developer: Peter J. Ersts
Concept and original documentation: Ned Horning and Kevin Koy

This plugin was originally written and distributed by the Center for Biodiversity and Conservation's Biodiversity Informtics Facility at the American Museum of Natural History -
http://biodiversityinformatics.amnh.org/open_source/evis/
eVis was contributed to the QGIS project on 2009-07-01.

eVis was started in 2007 with QGIS v0.7.0. It was our first experience with QGIS and QT. Since its early beginings, the QGIS API has under gone many changes and advances, and as a result there are still some old ideas in this code and much room for improvement. Were we to start this plugin now, we would have done it quite differently! There is still much room for imporovement. We hope the QGIS community will find eVis useful and extend its capabilities to make it even more robust.



A special "thank you" is extended to the following people who have contributed translations, comments, bug reports, and patches which have helped to make eVis a better tool:
Tim Sutton, Magnus Homann, John Tull, Agustin Lobo, Donald Schrupp, Muslim Bandishoev, Anousak Souphavanh, Ha Quy Quynh, Roberto García-Yunta, Tom Gottfried

This work was made possible through a grant by the John D. and Catherine T. MacArthur Foundation. Additionally, these products were prepared by the American Museum of Natural History under award No. NA05SEC46391002 from the National Oceanic and Atmospheric Administration, U.S. Department of Commerce. The statements, findings, conclusions, and recommendations are those of the author(s) and do not necessarily reflect the views of the National Oceanic and Atmospheric Administration or the Department of Commerce.
##############################################
    QGIS PLUGIN TEMPLATE DIRECTORY

              T.Sutton 2004
##############################################

Please do not edit the files in this directory
unless you know exactly what you are doing -
these files are used as the basis for creating
new plugins. Altering these files may break
the automated plugin template generation process.

Please visit: http://mrcc.com/qgiswiki/PluginDevelopersGuide

For more information on creating plugins.
Coordinate Capture Plugin for QGIS

       Tim Sutton 2008

A simple plugin that allows you to copy the
coordinates of mouse clicks to the clipboard.
/***************************************************************************
 *Copyright (C) 2008 Paolo L. Scala, Barbara Rita Barricelli, Marco Padula *
 * CNR, Milan Unit (Information Technology),                               *
 * Construction Technologies Institute.\n";                                *
 *                                                                         *
 * email : Paolo L. Scala <scala@itc.cnr.it>                               *
 *                                                                         *
 *   This is a plugin generated from the QGIS plugin template              *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 ***************************************************************************/
 DXF2SHP Plugin converter

We've just developed and partially tested this plugin that converts a DXF file
into one or more vector layers in QGIS;  it can also extract labels from the
DXF file and inserts the data (string, x, y, z, angle) in the dbf file of a new
point layer populated with points located where the labels should be rendered.
The purpose is to let Mapserver render them.

The plugin uses shapelib and dxflib to convert and create the shp files.
For any suggestion or criticism, please contact us at:

scala@itc.cnr.it
barricelli@itc.cnr.it
Notes on the usage of the QGIS custom designer plugins

                 Tim Sutton, 2006
--------------------------------------------------------

Introduction:

The purpose of the QGIS designer plugins is to enable all third
party developers to create GIS enabled Qt4 based applications
with minimal programming. The idea being that you use the
standard Qt4 Designer GUI design tool to create your user
interface and then add map canvas, legend, projection selector
etc. type of widgets from the toolbox of widgets in designer
- with QGIS having added its own group of custome widgets there.
The QGIS custom widgets can then be graphically 'programmed' by
setting widget properties and using interactive signal/slot
connectors.

Plugin Paths:

There are two options for having Qt4 Designer find your
plugins at startup:

1) copy the plugin from {QGIS Install Prefix}/lib/qgis/designer
   into the standard Qt4 designer plugin directory at
   $QTDIR/plugins/designer/

2) export the environment variable QT_PLUGIN_PATH with all the
   places designer should look for your plugins in. Separate
   each entry with a colon. So for example:

   export QT_PLUGIN_PATH={QGIS Install Prefix}/lib/qgis

   Note that the 'designer' directory is omitted from the path.

   Its probably a good idea to add the above export clause to
   your ~/.bash_profile or ~/.bashrc if you plan to use the
   designer plugins frequently.


Additional Notes:

If you built Qt4 in debug mode then the designer plugins must also
be built in debug mode or they will be ignored. The converse is also
true.

PLUGIN METADATA TAGS
=======================================================
id                  the key; C++ library base name or Python module name
plugin_id           for the official repository: an integer id. At the time, used for voting only.
name                human readable plugin name
description         short description of the plugin purpose only
about               longer description: how does it work, where does it install, how to run it?
category            isn't it depreciated?
tags                comma separated, spaces allowed
changelog           may be multiline
author_name         author name
author_email        author email
homepage            url to the plugin homepage
tracker             url to a tracker site
code_repository     url to the source code repository
version_installed   installed instance version
library             absolute path to the installed library / Python module
icon                path to the first of (INSTALLED | AVAILABLE) icon
pythonic            true | false (is plugin pythonic or cpp?)
readonly            true | false (is core plugin?)
installed           true | false
available           true | false
status              not installed | new    |   upgradeable | orphan | downgradeable *
error               NULL | broken | incompatible | dependent
error_details       error description
experimental        true if experimental, false if stable
version_available   available version
zip_repository      the remote repository id
download_url        url for downloading the plugin
filename            the zip file name to be unzipped after downloaded
downloads           number of dowloads
average_vote        average vote
rating_votes        number of votes

* status is only obligatory for Pythin plugins and it must match all the tags:
available, installed. version_available, version_installed.
orphan = installed and not available to download;
new = not installed and seen for the first time;
downgradeable = the available version is lower than installed one.

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<meta http-equiv="Content-Language" content="en" />
<meta name="Author" content="Marco Pasetti" />
<meta name="Description" content="How to prepare a MS-Windows QGIS Release" />

<title>WinQGIS Release How-To</title>

<style type="text/css" />

/* Wiki Pages Styles */

/* TableOfContents */

.table-of-contents	{ 
					border: 1px solid #bbbbbb;
					color: black; background-color: #eeeeee;
					font-size: small;
					text-align:left;
					margin: 0.5em; padding-left: 1em;
					width: 360;
					}

/* Contents */

html	{
		background-color: white;
		color: black;
		font-family: Arial, Lucida Grande, sans-serif;
		font-size: 10pt;
		}
		
body	{
		margin: 30;
		}
		
ol	{
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 10pt;
	margin-top: 0;
	margin-bottom: 0;
	margin-left: 0;
	}

h1	{
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 18pt;
	margin-top: 0;
	margin-bottom: 50;
	}

h2	{
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 16pt;
	margin-top: 60;
	margin-bottom: 20;
	}
	
h3	{
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 14pt;
	margin-top: 60;
	margin-bottom: 20;
	}

h4	{
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 11pt;
	margin-top: 0;
	margin-bottom: 0;
	}

p	{
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 10pt;
	margin-top: 10;
	margin-bottom: 10;
	}

code	{
		font-family: Courier-new, monospace;
		font-size: 10pt;
		margin-top: 10;
		margin-bottom: 10;
		}
		
pre	{
	padding: 1em;
	border: 1px dashed #2f6fab;
	color: black;
	background-color: #f9f9f9;
	line-height: 1.1em;
	}
	
	
/* Tables */

table
{
	margin: 0.5em 0 0 0.5em;
	border-collapse: collapse;
}

td
{
	padding: 0.25em 0.5em 0.25em 0.5em;
	border: 0pt solid #ADB9CC;
	font-family: Arial, Lucida Grande, sans-serif;
	font-size: 10pt;
}
		

/* Links */

a	{
	text-decoration: none;
	color: #002bb8;
	background: none;
	}
	
a:hover {
		text-decoration: underline;
		color: green;
		}
	
a:visited:hover	{
				text-decoration: underline;
				color: red;
				}
</style>

</head>

<body>

<h1>How to prepare a MS-Windows QGIS Release</h1>

<div class="table-of-contents">

<p><strong>Table of Contents</strong></p>

<p><a href="#Introduction">Introduction</a></p>

<p><ol>
<li><a href="#MSYS">MSYS</a></li>
<li><a href="#MinGW">MinGW</a></li>
<li><a href="#QGIS MSYS Environment">QGIS MSYS Environment</a></li>
<li><a href="#Qt OpenSource">Qt OpenSource</a></li>
<li><a href="#Python">Python</a></li>
<li><a href="#SIP">SIP</a></li>
<li><a href="#PyQt">PyQt</a></li>
<li><a href="#CMake">CMake</a></li>
<li><a href="#QGIS">QGIS Build</a></li>
<li><a href="#QGIS Package">QGIS self-contained Package</a></li>
<li><a href="#NSIS">NSIS</a></li>
<li><a href="#QGIS Installer">QGIS Installer</a></li>
</ol></p>

<p><a href="#Credits and Contacts">Credits and Contacts</a></p>

<br>

</div>



<div id="Introduction">

<p><h3>Introduction</h3></p>


<p>This document explains how to prepare a MS-Windows QGIS release (as a self-contained package installer)
using the scripts contained in the ms-windows folder. In order to avoid mistakes or misunderstandings,
I highly recommend to follow each step and command exactly as they are written in this document.</p>

</div>




<div id="MSYS">

<p><h3>1. MSYS (1.0.11)</h3></p>

<p>Download the <a target="_blank" href="http://prdownloads.sourceforge.net/mingw/MSYS-1.0.11-2004.04.30-1.exe">MSYS installer</a></p>

<p>Install to <code>c:\msys</code></p>

<p>At the command prompt question for post install, type <code>n</code> and then enter.</p>

<p>Download the <a target="_blank" href="http://downloads.sourceforge.net/mingw/coreutils-5.97-MSYS-1.0.11-snapshot.tar.bz2">
MSYS coreutils package</a></p>

<p>Unpack it to a temporary folder, then copy all the content of the <code>coreutils-5.97</code> folder to <code>c:\msys</code>
(overwrite the existing files when asked)</p>

</div>




<div id="MinGW">

<p><h3>2. MinGW (5.1.4)</h3></p>

<p>Download the <a target="_blank" href="http://downloads.sourceforge.net/mingw/MinGW-5.1.4.exe">MinGW installer</a></p>

<p>Select "Download and Install Current Version";</p>

<p>Install only "g++ compiler" and "MinGW Make";</p>

<p>Install to <code>c:\msys\mingw</code></p>

</div>




<div id="QGIS MSYS Environment">

<p><h3>3. QGIS MSYS Environment</h3></p>

<p>Download the <a target="_blank" href="http://download.osgeo.org/qgis/win32/msys.zip">
QGIS MSYS Environment</a></p>

<p>Extract the whole package to <code>c:\msys\local</code></p>

</div>



<div id="Qt OpenSource">

<p><h3>4. Qt OpenSource (4.4.0)</h3></p>

<p>
Download the <a target="_blank" href="ftp://ftp.trolltech.com/qt/source/qt-win-opensource-4.4.0-mingw.exe">Qt OpenSource installer</a>
</p>

<p>Install to <code>C:\DevTools\Qt-OpenSource</code></p>

<p>When the installer will ask for MinGW, you don't need to download and install it, just point the installer to
<code>c:\msys\mingw</code></p>

<p>At the alert message "The installer could not found a valid c:\msys\mingw\include\w32api.h", press "Yes" and continue.</p>

<p>When Qt installation is complete, edit <code>C:\DevTools\Qt-OpenSource\bin\qtvars.bat</code> and do as follows:</p>

<p>At line 8 replace:</p>
<pre><code>echo -- PATH set to C:\DevTools\Qt-OpenSource\bin</code></pre>

<p>with:</p>
<pre><code>echo -- Adding MSYS environment directories to PATH</code></pre>

<p>At line 14 replace:</p>
<pre><code>set PATH=C:\DevTools\Qt-OpenSource\bin</code></pre>

<p>with:</p>
<pre><code>set PATH=%PATH%;c:\msys\local\bin;c:\msys\local\sqlite\bin;c:\msys\local\pgsql\lib</code></pre>

<p>Finally, add <code>C:\DevTools\Qt-OpenSource\bin</code> to your <code>PATH</code> system variable.</p>

</div>




<div id="Python">

<p><h3>5. Python (2.5.2)</h3></p>

<p>
Download the <a target="_blank" href="http://www.python.org/ftp/python/2.5.2/python-2.5.2.msi">Python installer</a>
</p>

<p>Install to <code>C:\DevTools\Python</code></p>

<p>Add <code>C:\DevTools\Python</code> to your <code>PATH</code> system variable.</p>

</div>




<div id="SIP">

<p><h3>6. SIP (4.7.6)</h3></p>

<p>
Download the <a target="_blank" href="http://www.riverbankcomputing.com/static/Downloads/sip4/sip-4.7.6.zip">SIP source code</a>
</p>

<p>Unpack to <code>c:\msys\local\src</code></p>

<p>Open a Windows terminal and type:</p>
<pre><code>cd c:\msys\local\src\sip-4.7.6
qtvars
python configure.py -p win32-g++
make
make install</code></pre>

</div>




<div id="PyQt">

<p><h3>7. PyQt (4.4.2)</h3></p>

<p>
Download the <a target="_blank" href="http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-win-gpl-4.4.2.zip">PyQt source code</a>
</p>

<p>Unpack to <code>c:\msys\local\src</code></p>

<p>Open a Windows terminal and type:</p>
<pre><code>cd c:\msys\local\src\PyQt-win-gpl-4.4.2
qtvars
python configure.py
make
make install</code></pre>

</div>




<div id="CMake">

<p><h3>8. CMake (2.6.0)</h3></p>

<p>
Download the <a target="_blank" href="http://www.cmake.org/files/v2.6/cmake-2.6.0-win32-x86.exe">CMake installer</a>
</p>

<p>Launch the CMake installer and do as follows:</p>

<p>Select "Add CMake to the system PATH for all users"</p>

<p>Install to <code>C:\DevTools\CMake</code></p>

</div>




<div id="QGIS">

<p><h3>9. QGIS Build (0.11.0)</h3></p>

<p>
Download the <a target="_blank" href="http://download.osgeo.org/qgis/src/qgis_0.11.0.tar.gz">QGIS source code</a>
</td>
</tr></table>

<p>Unpack to <code>c:\msys\local\src</code></p>

<p>Open a Windows terminal and type:</p>
<pre><code>cd c:\msys\local\src\qgis_0.11.0
md build
cd build
qtvars
cmakesetup ..</code></pre>

<p>In CMake Setup utility press "Configure" button and, when asked, choose "MinGW Makefiles" as generator.</p>

<p>CMake Setup will alert you for missing dependencies; don't care, press OK and continue.</p>

<p>When finished, select "Show Advanced Values" checkbox.</p>

<p>For each item listed below, select the related box in the CMake Setup utility, type in the suggested value and then press enter
(we will perform a "bottom-up" procedure, editing last values of the CMake Setup list as first):</p>

<pre><code>SQLITE3_LIBRARY = c:/msys/local/sqlite/bin/libsqlite3-0.dll
SQLITE3_INCLUDE_DIR = c:/msys/local/sqlite/include
POSTGRES_INCLUDE_DIR = c:/msys/local/pgsql/include
GRASS_PREFIX = c:/msys/local/grass-6.3.0
CMAKE_INSTALL_PREFIX = c:/msys/local/qgis-0.11.0
CMAKE_CXX_FLAGS = -DGEOS_INLINE
CMAKE_BUILD_TYPE = Release</code></pre>

<p>When finished press OK button.</p>

<p>Finally, in the same terminal session, type:</p>
<pre><code>make
make install</code></pre>

</div>




<div id="QGIS Package">

<p><h3>10. QGIS self-contained Package</h3></p>

<p>Copy all the content of the ms-windows folder to a temporary directory, for example <code>c:\temp</code>.</p>

<p>Launch the file <code>c:\temp\QGIS-Packager.bat</code> and select the option number 2.</p>

<p>When finished, you should have a QGIS self-contained release package in <code>c:\temp\QGIS-Release-Package</code>.</p>

</div>




<div id="NSIS">

<p><h3>11. NSIS (2.38)</h3></p>

<p>Download the <a target="_blank" href="http://prdownloads.sourceforge.net/nsis/nsis-2.38-setup.exe">NSIS installer</a></p>

<p>Install to <code>c:\DevTools</code></p>

</div>




<div id="QGIS Installer">

<p><h3>12. QGIS Installer</h3></p>

<p>Open the the file <code>c:\temp\QGIS-Installer.nsi</code>.</p>

<p>At line 13 set the <code>INSTALLER_TYPE</code> variable to <code>"Release"</code>, then, at lines 19-22, set the
<code>RELEASE_VERSION_NUMBER</code>, the <code>RELEASE_VERSION_NAME</code>, the <code>RELEASE_SVN_REVISION</code> and
the <code>RELEASE_BINARY_REVISION</code> variables.</p>

<p>Finally, right click on the file <code>c:\temp\QGIS-Installer.nsi</code> and select <code>Compile NSIS Script</code>.</p>

<p>When finished, you should have the QGIS release installer in <code>c:\temp</code>.</p>

</div>




<div id="Credits and Contacts">

<p><h3>Credits and Contacts</h3></p>

<p>The QGIS MSYS Environment and the QGIS Packager and Installer scripts are provided by Marco Pasetti.</p>

<p>
To contact him, e-mail to: QGIS Development Mailing List
(<a target="_blank" href="http://lists.osgeo.org/mailman/listinfo/qgis-developer">http://lists.osgeo.org/mailman/listinfo/qgis-developer</a>).
</p>

<p>Edited by Marco Pasetti on 13 September 2008.</p>

</div>

</body>

</html>
For use in QGIS websites you also find the medals in 
https://github.com/qgis/QGIS/tree/master/images/sponsors/
Theme Originals
---------------

As of QGIS 2.0, all newly submitted or updated interface graphics need to be in
SVG format, or at least have SVG originals. Inkscape files are preferred; export
to SVG version 1.0 if using Adobe Illustrator.

There is an effort to switch current interface raster graphics to SVG. In the
meantime, any updated graphics to the theme directory that are not in SVG
format (e.g. PNG icon, because the code associated with it has not been updated
to work with SVGs yet, or may never) should have their SVG originals placed in
this directory.

Periodically, this directory will be cleared out when the SVGs here can be moved
into the themes directory. This directory will probably be removed when migration
to SVG-only has been completed.

Submissions here, the theme directory, or to the QGIS project will all probably
end up on the OSGeo graphics server: http://wiki.osgeo.org/wiki/OSGeo_Graphics.
Contact Robert Szczepanek for more info on contributing to OSGeo graphics.
If looking to work on a new graphic for QGIS consider looking there first.

All submissions need to be based on work uninhibited by intellectual property
restrictions and compatible with QGIS's licensing structure.



2013-02-07 Larry Shaffer - larrys [@] dakotacarto.com
Fonts used for the splash screen:
---------------------------------

QGIS : Lucida Sans Unicode Regular 272pt

Version X.X.X : Lucida Sans Unicode Regular 68pt

Release name : FreeSans Bold Oblique 197pt



Fonts used for the web page banner:
-----------------------------------

QGIS : Lucida Sans Unicode Regular 58pt

Version X.X.X : Lucida Sans Unicode Regular 14pt

Release name : FreeSans Bold Oblique 39pt

DB Manager * Copyright (c) 2011 Giuseppe Sucameli

DB Manager is a database manager plugin for QGIS.
It allows showing the DBs contents and run query on them.

In this moment DB Manager supports the following DBMS backends:
- PostgreSQL/PostGIS through the psycopg2 pymodule
- SQLite/SpatiaLite using the pyspatialite pymodule


For more info about the project, see at the wiki page:
    http://qgis.org/wiki/DB_Manager_plugin_GSoC_2011

or visit my GitHub repository:
    https://github.com/brushtyler/db_manager


Requirement
1) qgis
2) sextante_taudem (TauDEM-1.1.1.zip)
3) sextante (sextante-1.0.9.zip)
4) PYTHONPATH=.:/usr/lib/otb/python:/usr/share/qgis/python/plugins:~/.qgis2/python/plugins
5) ITK_AUTOLOAD_PATH=/usr/lib/otb/applications 

Creating xml files
cd .qgis2/python/plugin/sextante/otb/maintenance
python ./OTBHelper.py 
Building KADAS Albireo from source
==================================

Build
-----

Clone or download source code:

    git clone https://github.com/sourcepole/kadas-albireo.git
    cd kadas-albireo

Get the Docker image for building:

    docker pull sourcepole/kadas-mingw-buildenv

Build within Docker container with attached source code:

    docker run -v $PWD:/workspace sourcepole/kadas-mingw-buildenv ms-windows/mingwbuild.sh

Windows:

    docker run -v %CD%:/workspace sourcepole/kadas-mingw-buildenv ms-windows/mingwbuild.sh
Updating the srs.db
-------------------

The srs.db can be updated from the EPSG codes in the
GDAL installation:

1) Install latest GDAL, be sure to configure with --with-python.
2) Set PATH and PYTHONDIR if installed GDAL in non-standard location.
3) Run 'scripts/qgis_srs.sh > new_srs.sql'. It may take a minute or two.
4) Run 'sqlite3 new_srs.db < new_srs.sql'.'
4) Run 'sqlite3 new_srs.db <postprocess_srs.sql'

You can use sqlite3 to dump the contents from both srs.db and new_srs.db
before you decide to commit.

Magnus Homann 2009-08-19This package contains the gradients from the cpt-city 
collection. The archive's home is online at 

  http://soliton.vm.bytemark.co.uk/pub/cpt-city/

where the most recent version can be found.

The copyright of the gradient files is held by their 
authors, and details of these can be found in the 
COPYING.xml files. 

This package contains a selection of the cpt-city gradients for use by the QGIS application.

The gradients files chosen allow for redistribution and free use, 
subject to individual license information found in the COPYING.xml files.

