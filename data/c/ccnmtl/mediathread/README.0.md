# OpenLayers

Copyright (c) 2005-2013 OpenLayers Contributors. See authors.txt for
more details.

OpenLayers is a JavaScript library for building map applications
on the web. OpenLayers is made available under a BSD-license.
Please see license.txt in this distribution for more details.

## Getting OpenLayers

OpenLayers lives at http://www.openlayers.org/.  Find details on downloading stable releases or the development version the [development site](http://trac.osgeo.org/openlayers/wiki/HowToDownload).

## Installing OpenLayers

You can use OpenLayers as-is by copying build/OpenLayers.js and the
entire theme/ and img/ directories up to your webserver and putting them 
in the same directory. The files can be in subdirectories on your website, 
or right in the root of the site, as in these examples. 
To include the OpenLayers library in your web page from the root of the site, use:

    <script type="text/javascript" src="/OpenLayers.js" />

As an example, using bash (with the release files in ~/openlayers):

    $ cd /var/www/html
    $ cp ~/openlayers/OpenLayers.js ./
    $ cp -R ~/openlayers/theme ./
    $ cp -R ~/openlayers/img ./

If you want to use the multiple-file version of OpenLayers (for, say,
debugging or development purposes), copy the lib/ directory up to your
webserver in the same directory you put the img/ folder. Then add
the following to your web page instead:

    <script type="text/javascript" src="/lib/OpenLayers.js" />

As an example, using bash (with the release files in ~/openlayers):

    $ cd /var/www/html
    $ cp -R ~/openlayers/lib ./
    $ cp -R ~/openlayers/theme ./
    $ cp -R ~/openlayers/img ./

## Alternate OpenLayers Versions in this Release

The following versions of OpenLayers single file builds are included in this release 
and can be used in place of OpenLayers.js in any of the above instructions:

1. OpenLayers.js - full build --> Includes everything except the alternate language
    translations and deprecated classes.
2. OpenLayers.mobile.js - a mobile focused build --> Includes a subset of the OpenLayers 
    library to serve common mobile web app use cases. This build provides access to 
    OpenStreetMap, Bing, WMS, WFS and vector layers; touch optimized controls; geolocation;
    vector editing and interaction tools. The examples tagged ``mobile`` can use this build.
3. OpenLayers.light.js - a simple use case focused build --> Includes a subset of the
    OpenLayers library to serve the basic use case of displaying points and polygons
    on a map. This build provides access to OpenStreetMap, Bing, Google, WMS, and 
    vector layers; basic map controls; and vector interaction tools. The examples
    tagged ``light`` can use this build.
    
## Using OpenLayers in Your Own Website

The [examples directory](http://openlayers.org/dev/examples/) is full of useful examples.

Documentation is available at http://trac.osgeo.org/openlayers/wiki/Documentation.
You can generate the API documentation with http://www.naturaldocs.org/
As an example, using bash (with the release files in ~/openlayers):

    $ cd ~/openlayers/
    $ /path/to/NaturalDocs -i lib/ -o HTML doc/ -p doc_config/ -s Default OL

Information on changes in the API is available in release notes found in the notes folder.

## Contributing to OpenLayers

Please join the email lists at http://openlayers.org/mailman/listinfo
Patches are welcome!

This directory contains the source for Firebug Lite
(http://www.getfirebug.com/lite.html).  This code is distributed with a
BSD License, Copyright (c) 2007, Parakey Inc.  See the included license.txt
for the full text of the license.

This is a patched version of the trunk from
http://fbug.googlecode.com/svn/trunk.

Revision 36 was patched to resolve the issue described here
http://code.google.com/p/fbug/issues/detail?id=85

When this issue is resolved, Firebug Lite can be used directly - no further
modifications are needed for OpenLayers.This is where language files should be placed.

Please DO NOT translate these directly use this service: https://www.transifex.com/projects/p/tinymce/
This directory contains unit tests for the OpenLayers library.

Tests use the Test.AnotherWay library from <http://openjsan.org>. The test
runner is 'run-tests.html' and new test files need to be added to
'list-tests.html'.

The following file naming conventions are used:

  * A filename that starts with `test_` and has an `.html` extension
    contains tests. These should contain tests for a specific class.

  * A filename starting with `page_` and has an `.html` extension is a
    supporting HTML file used in one or more tests.

  * A filename starting with 'data_` is a supporting data file used in one
    or more tests.
The OpenLayers build tool supports several different
forms of compressing your javascript code, and a method
of describing build profiles to create customized 
OpenLayers builds with only the components you need.

When building a file, you can choose to build with several
different compression options to the Python-based build.py
script. The following is an example script:

python build.py -c closure full OpenLayers-closure.js

This script selects the 'closure' compression mechanism,
uses a config file called 'full.cfg', and writes the output
to OpenLayers-closure.js.

The options available for compression are:

 * closure
   This requires you to have a closure-compiler.jar in your
   tools directory. You can do this by fetching the compiler
   from:

     http://closure-compiler.googlecode.com/files/compiler-latest.zip

   Then unzipping that file, and placing compiler.jar into tools
   and renaming it closure-compiler.jar.

 * closure_ws
   This uses the closure compiler webservice. This will only work
   for files source Javascript files which are under 1MB. (Note that
   the default OpenLayers full build is not under 1MB.)

 * jsmin
   jsmin is the default compiler, and uses the Python-based
   jsmin script to compress the Javascript. 

 * minimize
   This is a simple whitespace removing Python script, designed
   to fill in when other tools are unavailable.

 * none
   None will leave the Javascript uncompressed.


For more information on the build script and custom build profiles,
see http://docs.openlayers.org/library/deploying.html
This directory contains tools used in the packaging or deployment of OpenLayers.

Javascript minimizing tools:

 * jsmin.c, jsmin.py:
   jsmin.py is a direct translation of the jsmin.c code into Python. jsmin.py
   will therefore run anyplace Python runs... but at significantly slower speed.
 
 * shrinksafe.py
   shrinksafe.py calls out to a third party javascript shrinking service. This 
   creates file sizes about 4% smaller (as of commit 501) of the OpenLayers 
   code. However, this also has the side effect of making you dependant on the 
   web service -- and since that service sometimes goes dead, it's risky to 
   depend on it.
/*
 * Copyright 2009 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

//
// Contents
//

The Closure Compiler performs checking, instrumentation, and
optimizations on JavaScript code. The purpose of this README is to
explain how to build and run the Closure Compiler.

The Closure Compiler requires Java 6 or higher.
http://www.java.com/


//
// Building The Closure Compiler
//

There are three ways to get a Closure Compiler executable.

1) Use one we built for you.

Pre-built Closure binaries can be found at
http://code.google.com/p/closure-compiler/downloads/list


2) Check out the source and build it with Apache Ant.

First, check out the full source tree of the Closure Compiler. There
are instructions on how to do this at the project site.
http://code.google.com/p/closure-compiler/source/checkout

Apache Ant is a cross-platform build tool.
http://ant.apache.org/

At the root of the source tree, there is an Ant file named
build.xml. To use it, navigate to the same directory and type the
command

ant jar

This will produce a jar file called "build/compiler.jar".


3) Check out the source and build it with Eclipse.

Eclipse is a cross-platform IDE.
http://www.eclipse.org/

Under Eclipse's File menu, click "New > Project ..." and create a
"Java Project."  You will see an options screen. Give the project a
name, select "Create project from existing source," and choose the
root of the checked-out source tree as the existing directory. Verify
that you are using JRE version 6 or higher.

Eclipse can use the build.xml file to discover rules. When you
navigate to the build.xml file, you will see all the build rules in
the "Outline" pane. Run the "jar" rule to build the compiler in
build/compiler.jar.


//
// Running The Closure Compiler
//

Once you have the jar binary, running the Closure Compiler is straightforward.

On the command line, type

java -jar compiler.jar

This starts the compiler in interactive mode. Type

var x = 17 + 25;

then hit "Enter", then hit "Ctrl-Z" (on Windows) or "Ctrl-D" (on Mac or Linux)
and "Enter" again. The Compiler will respond:

var x=42;

The Closure Compiler has many options for reading input from a file,
writing output to a file, checking your code, and running
optimizations. To learn more, type

java -jar compiler.jar --help

You can read more detailed documentation about the many flags at
http://code.google.com/closure/compiler/docs/gettingstarted_app.html


//
// Compiling Multiple Scripts
//

If you have multiple scripts, you should compile them all together with
one compile command.

java -jar compiler.jar --js=in1.js --js=in2.js ... --js_output_file=out.js

The Closure Compiler will concatenate the files in the order they're
passed at the command line.

If you need to compile many, many scripts together, you may start to
run into problems with managing dependencies between scripts. You
should check out the Closure Library. It contains functions for
enforcing dependencies between scripts, and a tool called calcdeps.py
that knows how to give scripts to the Closure Compiler in the right
order.

http://code.google.com/p/closure-library/

//
// Licensing
//

Unless otherwise stated, all source files are licensed under
the Apache License, Version 2.0.


-----
Code under:
src/com/google/javascript/rhino
test/com/google/javascript/rhino

URL: http://www.mozilla.org/rhino
Version:  1.5R3, with heavy modifications
License:  Netscape Public License and MPL / GPL dual license

Description: A partial copy of Mozilla Rhino. Mozilla Rhino is an
implementation of JavaScript for the JVM.  The JavaScript parser and
the parse tree data structures were extracted and modified
significantly for use by Google's JavaScript compiler.

Local Modifications: The packages have been renamespaced. All code not
relavant to parsing has been removed. A JSDoc parser and static typing
system have been added.


-----
Code in:
lib/libtrunk_rhino_parser_jarjared.jar

Rhino
URL: http://www.mozilla.org/rhino
Version:  Trunk
License:  Netscape Public License and MPL / GPL dual license

Description: Mozilla Rhino is an implementation of JavaScript for the JVM.

Local Modifications: None. We've used JarJar to renamespace the code
post-compilation. See:
http://code.google.com/p/jarjar/


-----
Code in:
lib/google_common_deploy.jar

Guava Libraries
URL: http://code.google.com/p/guava-libraries/
Version:  Trunk
License: Apache License 2.0

Description: Google's core Java libraries.

Local Modifications: None.


----
Code in:
lib/junit.jar

JUnit
URL: http://sourceforge.net/projects/junit/
Version: 3.8.1
License: Common Public License 1.0

Description: A framework for writing and running automated tests in Java.

Local Modifications: None.


---
Code in:
lib/protobuf_deploy.jar

Protocol Buffers
URL: http://code.google.com/p/protobuf/
Version: 2.2.0a
License: New BSD License

Description: Supporting libraries for protocol buffers,
an encoding of structured data.

Local Modifications: None


---
Code in:
lib/ant_deploy.jar

URL: http://ant.apache.org/bindownload.cgi
Version: 1.6.5
License: Apache License 2.0
Description:
  Ant is a Java based build tool. In theory it is kind of like "make"
  without make's wrinkles and with the full portability of pure java code.

Local Modifications:
  Modified apache-ant-1.6.5/bin/ant to look in the ant.runfiles directory
