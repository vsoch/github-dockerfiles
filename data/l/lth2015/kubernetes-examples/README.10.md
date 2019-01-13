For the latest information about ZooKeeper, please visit our website at:

   http://zookeeper.apache.org/

and our wiki, at:

   https://cwiki.apache.org/confluence/display/ZOOKEEPER

Full documentation for this release can also be found in docs/index.html

---------------------------
Packaging/release artifacts

The release artifact contains the following jar file at the toplevel:

zookeeper-<version>.jar         - legacy jar file which contains all classes
                                  and source files. Prior to version 3.3.0 this
                                  was the only jar file available. It has the 
                                  benefit of having the source included (for
                                  debugging purposes) however is also larger as
                                  a result

The release artifact contains the following jar files in "dist-maven" directory:

zookeeper-<version>.jar         - bin (binary) jar - contains only class (*.class) files
zookeeper-<version>-sources.jar - contains only src (*.java) files
zookeeper-<version>-javadoc.jar - contains only javadoc files

These bin/src/javadoc jars were added specifically to support Maven/Ivy which have 
the ability to pull these down automatically as part of your build process. 
The content of the legacy jar and the bin+sources jar are the same.

As of version 3.3.0 bin/sources/javadoc jars contained in dist-maven directory
are deployed to the Apache Maven repository after the release has been accepted
by Apache:
  http://people.apache.org/repo/m2-ibiblio-rsync-repository/
README file for Packaging Notes

Requirement
-----------

gcc, cppunit and python-setuptools are required to build 
C and python bindings.

On RHEL machine:

yum install cppunit
yum install python-setuptools

On Ubuntu:

apt-get --install cppunit
apt-get --install python-setuptools

Package build command
---------------------

Command to build Debian package: ant deb
Command to build RPM Package: ant rpm

rpm and deb packages are generated and placed in:

build/zookeeper*.[rpm|deb]
build/contrib/**.[rpm|deb]

Default package file structure layout

  /usr/bin                           - User executable
  /usr/sbin                          - System executable
  /usr/libexec                       - Configuration boot trap script
  /usr/lib                           - Native libraries
  /usr/share/doc/zookeeper           - Documents
  /usr/share/zookeeper               - Project files
  /usr/share/zookeeper/template/conf - Configuration template files
  /etc/zookeeper                     - Configuration files
  /etc/init.d/zookeeper              - OS startup script

Source file structure layout
---------------------

src/packages/update-zookeeper-env.sh 
  - setup environment variables and symlink $PREFIX/etc/zookeeper to 
    /etc/zookeeper.
  - This script is designed to run in post installation, and pre-remove 
    phase of ZooKeeper package.
  - Run update-zookeeper-env.sh -h to get a list of supported parameters.

src/packages/template
  - Standard configuration template

src/packages/deb 
  Meta data for creating Debian package

src/packages/deb/init.d
  Daemon start/stop script for Debian flavor of Linux

src/packages/rpm 
  Meta data for creating RPM package

src/packages/rpm/init.d
  Daemon start/stop script for Redhat flavor of Linux
                     Zookeeper C queue client library 


INSTALLATION

If you're building the client from a source checkout you need to
follow the steps outlined below. If you're building from a release
tar downloaded from Apache please skip to step 2.

This recipe does not handle ZCONNECTIONLOSS. It will only work correctly once ZOOKEEPER-22 https://issues.apache.org/jira/browse/ZOOKEEPER-22 is resolved.

1) make sure that you compile the main zookeeper c client library.
 
2) change directory to src/recipes/queue/src/c 
    and do a "autoreconf -if" to bootstrap
   autoconf, automake and libtool. Please make sure you have autoconf
   version 2.59 or greater installed.
3) do a "./configure [OPTIONS]" to generate the makefile. See INSTALL
   for general information about running configure.

4) do a "make" or "make install" to build the libraries and install them. 
   Alternatively, you can also build and run a unit test suite (and
   you probably should).  Please make sure you have cppunit-1.10.x or
   higher installed before you execute step 4.  Once ./configure has
   finished, do a "make run-check". It will build the libraries, build
   the tests and run them.
5) to generate doxygen documentation do a "make doxygen-doc". All
   documentations will be placed to a new subfolder named docs. By
   default only HTML documentation is generated.  For information on
   other document formats please use "./configure --help"
                     Zookeeper C lock client library 


INSTALLATION

If you're building the client from a source checkout you need to
follow the steps outlined below. If you're building from a release
tar downloaded from Apache please skip to step 2.

1) make sure that you compile the main zookeeper c client library.
 
2) change directory to src/recipes/lock/src/c 
    and do a "autoreconf -if" to bootstrap
   autoconf, automake and libtool. Please make sure you have autoconf
   version 2.59 or greater installed.
3) do a "./configure [OPTIONS]" to generate the makefile. See INSTALL
   for general information about running configure.

4) do a "make" or "make install" to build the libraries and install them. 
   Alternatively, you can also build and run a unit test suite (and
   you probably should).  Please make sure you have cppunit-1.10.x or
   higher installed before you execute step 4.  Once ./configure has
   finished, do a "make run-check". It will build the libraries, build
   the tests and run them.
5) to generate doxygen documentation do a "make doxygen-doc". All
   documentations will be placed to a new subfolder named docs. By
   default only HTML documentation is generated.  For information on
   other document formats please use "./configure --help"
Download the cobertura binary from the following location and unpack it into this directory. Run "cobertura-report" target from build.xml to generate coverage report.

http://cobertura.sourceforge.net/download.html
==========================================
zktreeutil - Zookeeper Tree Data Utility
Author: Anirban Roy
Organization: Yahoo Inc.
==========================================

zktreeutil program is intended to manage and manipulate zk-tree data quickly, effi-
ciently and with ease. The utility operates on free-form ZK-tree and hence can be used
for any cluster managed by Zookeeper. Here are the basic functionalities -

EXPORT: The whole/partial ZK-tree is exported into a XML file. This helps in
capturing a current snapshot of the data for backup/analysis. For a subtree
export, one need to specify the path to the ZK-subtree with proper option.

IMPORT: The ZK-tree can be imported from XML into ZK cluster. This helps in priming
the new ZK cluster with static configuration. The import can be non-intrusive by
making only the additions in the existing data. The import of subtree is also
possible by optionally providing the path to the ZK-subtree.

DIFF: Creates a diff between live ZK data vs data saved in XML file. Diff can ignore
some ZK-tree branches (possibly dynamic data) on reading the optional ignore flag
from XML file. Diffing on a ZK-subtree achieved by providing path to ZK-subtree with
diff command.

UPDATE: Make the incremental changes into the live ZK-tree from saved XML, essentia-
lly after running the diff.

DUMP: Dumps the ZK-tree on the standard output device reading either from live ZK
server or XML file. Like export, ZK-subtree can be dumped with optionaly
providing the path to the ZK-subtree, and till a certain depth of the (sub)tree.

The exported ZK data into XML file can be shortened by only keeping the static ZK
nodes which are required to prime a cluster. The dynamic zk nodes (created on-the-
fly) can be ignored by setting a 'ignore' attribute at the root node of the dynamic
subtree (see tests/zk_sample.xml), possibly deleting all inner ZK nodes under that.
Once ignored, the whole subtree is ignored during DIFF, UPDATE and WRITE.

Pre-requisites
--------------
1. Linux system with 2.6.X kernel.
2. Zookeeper C client library (locally built at ../../c/.libs) >= 3.X.X
3. Development build libraries (rpm packages):
  a. boost-devel >= 1.32.0
  b. libxml2-devel >= 2.7.3
  c. log4cxx0100-devel >= 0.10.0

Build instructions
------------------
1. cd into this directory
2. autoreconf -if
3. ./configure
4. make
5. 'zktreeutil' binary created under src directory

Limitations
-----------
Current version works with text data only, binary data will be supported in future
versions.

Testing  and usage of zktreeutil
--------------------------------
1.  Run Zookeeper server locally on port 2181
2.  export LD_LIBRARY_PATH=../../c/.libs/:/usr/local/lib/
3.  ./src/zktreeutil --help # show help
4.  ./src/zktreeutil --zookeeper=localhost:2181 --import --xmlfile=tests/zk_sample.xml 2>/dev/null                 # import sample ZK tree
5.  ./src/zktreeutil --zookeeper=localhost:2181 --dump --path=/myapp/version-1.0 2>/dev/null                         # dump Zk subtree 
5.  ./src/zktreeutil --zookeeper=localhost:2181 --dump --depth=3 2>/dev/null                                                 # dump Zk tree till certain depth
6.  ./src/zktreeutil --xmlfile=zk_sample.xml -D 2>/dev/null                                                                     # dump the xml data
7.  Change zk_sample.xml with adding/deleting/chaging some nodes 
8.  ./src/zktreeutil -z localhost:2181 -F -x zk_sample.xml -p /myapp/version-1.0/configuration 2>/dev/null          # take a diff of changes
9.  ./src/zktreeutil -z localhost:2181 -E 2>/dev/null > zk_sample2.xml                                                         # export the mofied ZK tree
10. ./src/zktreeutil -z localhost:2181 -U -x zk_sample.xml -p /myapp/version-1.0/distributions 2>/dev/null        # update with incr. changes
11. ./src/zktreeutil --zookeeper=localhost:2181 --import --force --xmlfile=zk_sample2.xml 2>/dev/null             # re-prime the ZK tree

Net::ZooKeeper - Perl extension for Apache ZooKeeper
====================================================

Net::ZooKeeper provides a Perl interface to the synchronous C API
of Apache ZooKeeper.  ZooKeeper is coordination service for
distributed applications.
For details see the ZooKeeper home page at:

http://zookeeper.apache.org/

INSTALLATION

To install this module type the following, first install the
zookeeper C client, then:

    perl Makefile.PL
    make
    ZK_TEST_HOSTS=host:port,... make test
    make install

If the C headers and library are installed in non-standard
locations, specify them as arguments to Makefile.PL:
    
    perl Makefile.PL \
        --zookeeper-include=/path/to/zookeeper/client/include \
        --zookeeper-lib=/path/to/zookeeper/client/lib

The path supplied to the --zookeeper-include option should
identify the directory that contains the zookeeper.h and other
ZooKeeper C include files.

The path supplied to the --zookeeper-lib option should identify
the directory that contains the libzookeeper_mt library.

When running "make test", if no ZK_TEST_HOSTS environment
variable is set, many tests will be skipped because no connection
to a ZooKeeper server is available.  To execute these tests,
the ZK_TEST_HOSTS variable may be assigned a list of one or more
ZooKeeper host:port pairs, e.g., "localhost:7100,otherhost:7200".

The ZK_TEST_PATH environment variable, if defined, specifies
the ZooKeeper path under which all test nodes should be created.
The tests expect to have full read/write/create/delete/admin
ZooKeeper permissions under this path.  If no ZK_TEST_PATH
variable is defined, the root ZooKeeper path ("/") is used.

DEPENDENCIES

Version 3.1.1 of ZooKeeper is required at a minimum.

For version 3.1.1, you may also want to apply some of these
additional patches to the ZooKeeper C API code:

https://issues.apache.org/jira/browse/ZOOKEEPER-262
https://issues.apache.org/jira/browse/ZOOKEEPER-318

For version 3.1.1, you may also want to apply some of these
additional patches to the ZooKeeper C API code:

https://issues.apache.org/jira/browse/ZOOKEEPER-262
https://issues.apache.org/jira/browse/ZOOKEEPER-466

This module requires that the multi-threaded version of the
ZooKeeper C API client library be available on your system.

This in turn implies that the POSIX pthread library is available
as well.

COPYRIGHT AND LICENCE

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Original authors of zkfuse are Swee Lim & Bartlomiej M Niechwiej of Yahoo.
'
ZooKeeper FUSE (File System in Userspace)
=========================================

Pre-requisites
--------------
1. Linux system with 2.6.X kernel.
2. Fuse (Filesystem in Userspace) must be installed on the build node. 
3. Development build libraries:
  a. fuse
  b. log4cxx
  c. pthread
  d. boost

Build instructions
------------------
1. cd into this directory
2. autoreconf -if
3. ./configure
4. make
5. zkfuse binary is under the src directory

Testing Zkfuse
--------------
1. Depending on permission on /dev/fuse, you may need to sudo -u root.
   * If /dev/fuse has permissions 0600, then you have to run Zkfuse as root.
   * If /dev/fuse has permissions 0666, then you can run Zkfuse as any user.
2. Create or find a mount point that you have "rwx" permission. 
   * e.g. mkdir -p /tmp/zkfuse
3. Run Zkfuse as follows:
   zkfuse -z <hostspec> -m /tmp/zkfuse -d
   -z specifies ZooKeeper address(es) <host>:<port>
   -m specifies the mount point
   -d specifies the debug mode.
   For additional command line options, try "zkfuse -h".

FAQ
---
Q. How to fix "warning: macro `AM_PATH_CPPUNIT' not found in library"?
A. * install cppunit (src or pkg) on build machine

Q. Why can't Zkfuse cannot write to current directory?
A. * If Zkfuse is running as root on a NFS mounted file system, it will not
     have root permissions because root user is mapped to another user by
     NFS admin.
   * If you run Zkfuse as root, it is a good idea to run Zkfuse from a
     directory that you have write access to. This will allow core files
     to be saved.

Q. Why Zkfuse cannot mount?
A. * Check that the mount point exists and you have "rwx" permissions.
   * Check that previous mounts have been umounted. If Zkfuse does not 
     exit cleanly, its mount point may have to be umounted manually. 
     If you cannot umount manually, make sure that there no files is open 
     within the mount point.

Q. Why does Zkfuse complain about logging at startup?
A. * Zkfuse uses log4cxx for logging. It is looking for log4cxx.properties
     file to obtain its logging configuration.
   * There is an example log4cxx.properties file in the Zkfuse source 
     directory.

Early version of ZooKeeper bindings for Python. All functions are imported as methods into the zookeeper module.

Please do not rely on APIs staying constant in the short term. The handling of exceptions and failure modes is one area that is subject to change. 

DEPENDENCIES:
-------------

This has only been tested against SVN (i.e. 3.2.0 in development) but should work against 3.1.1. 

You will need the Python development headers installed to build the module - on many package-management systems, these can be found in python-devel.

Python >= 2.6 is required. We have tested against 2.6. We have not tested against 3.x. 

BUILD AND INSTALL:
-------------------

To install, make sure that the C client has been built and that the libraries are installed in /usr/local/lib (or change this directory in setup.py). Then run:

ant install

from zookeeper/src/contrib/zkpython/.

To test, run ant test from the same directory. 

You can compile the module without installing by running

ant compile

In order to use the module, zookeeper.so must be in your PYTHONPATH or in one of the directories referenced by sys.path. Running ant install should make sure that this is the case, but if you only run ant compile you probably need to add build/contrib/zkpython/* to PYTHONPATH to find the module. The C client libraries must be in a system library path, or LD_LIBRARY_PATH or DYLD_LIBRARY_PATH (Mac OS) for the module to work correctly, otherwise you will see a library not found error when trying to import the module. 

NAMING CONVENTIONS:
--------------------

All methods that in the C library are zoo_fn_name have been implemented as zookeeper.fn_name. The exception is any function that has a watch function argument is named without the 'w' prefix (for example, zoo_wexists becomes zookeeper.exists). The variants of these functions without the watch argument (i.e. zoo_exists) have not been implemented on the understanding that they are superseded by the zoo_w* API. 

Enums and integer constants that begin ZOO_int_name are named as zookeeper.int_name.

PARAMETER CHANGES:
------------------

Zookeeper handles are represented as integers to avoid marshalling the entire structure for every call. Therefore they are opaque from Python. 

Any parameter that is used to provide arguments to callback methods is not exposed in the API. Python provides better mechanisms for providing a closure to be called in the future.

Every callback gets passed the handle of the ZooKeeper instance used to register the callback.

DATA TYPES:
-----------

ACL_vectors are lists of dictionaries. Stat structures are dictionaries. String_vectors are lists of strings.

EXCEPTIONS AND ERROR HANDLING:
------------------------------

Currently synchronous calls indicate failure by throwing an exception (note that this includes the synchronous calls to set up asynchronous completion callbacks!). Success is returned as an integer. 

Callbacks signify failure by having the integer response code passed in. 

WHAT'S NEW IN 0.4:
------------------

More test coverage. 

Better reference counting, fixing at least two serious bugs.

Out-of-range zhandles are now checked, fixing a potential security hole.

Docstrings! Editing and cleanup required, but most of the text is there.

zookeeper.set_watcher is now implemented correctly.

zookeeper.client_id is now implemented correctly. zookeeper.init now respects the client_id parameter.

get_context and set_context have been removed from the API. The context mechanism is used by PyZK to store the callables that are dispatched by C-side watchers. Messing with this from Python-side causes bugs very quickly. You should wrap all desired context up in a callable and then use zookeeper.set_watcher to attach it to the global watcher. 

Many methods now have optional parameters (usually if you can specify a watch, it's optional). The only time where genuinely optional parameters are still mandatory is when a required parameters comes after it. Currently we still respect the ZK C client parameter ordering. For example, you can simply connect with zookeeper.init("host:port") and ignore the other three parameters.


WHAT'S NEW IN 0.3:
------------------

Some tests in zkpython/test. More to follow!

A variety of bugfixes.

Changed the way methods return results - all responses are integers now, for the client to convert to a string if it needs.

WHAT'S NEW IN 0.2:
------------------

The asynchronous API is now implemented (see zookeeper.a*).

Most enums defined in zookeeper.h are now added as constants to the module.

_set2 and a few other edge API calls have been implemented. The module is now nearly 100% feature complete!

A reference count error was tracked down and killed. More probably lurk in there!

WHAT'S NOT DONE / KNOWN ISSUES / FUTURE WORK:
---------------------------------------------

1. There may well be more memory leaks / reference count issues; however I am more confident that common paths are relatively safe. 
2. There probably needs to be a more Pythonic Python-side wrapper for these functions (e.g. a zookeeper object, the ability to iterate through a tree of zk nodes)
3. Docstrings need a cleanup.
4. The way exceptions and error codes are returned needs looking at. Currently synchronous calls throw exceptions on everything but ZOK return, but asynchronous completions are simply passed the error code. Async. functions should never throw an exception on the C-side as they are practically impossible to catch. For the sync. functions, exceptions seem more reasonable, but some cases are certainly not exceptional. 

Bug reports / comments very welcome!

Henry Robinson henry@cloudera.com

This folder contains sample showing how you can use ZooKeeper from Python.

You should also check the following projects:

* http://github.com/phunt/zk-smoketest
* http://github.com/henryr/pyzk-recipes 

Download the cobertura binary from the following location and unpack it into this directory. Run "cobertura-report" target from build.xml to generate coverage report.

http://cobertura.sourceforge.net/download.html
To run the system test we need to create processing containers that we can
spawn tasks, called Instances, in. (how is that for a dangling preposition!?!)
Start up InstanceContainers first. Then run the system test. The system test
finds the InstanceContainers and directs them through ZooKeeper, so you are
going to need an instance of ZooKeeper running that they can all access.
The easiest way to do all of this is to use the zookeeper fat jar.

Steps to run system test
------------------------
1) transfer the fatjar from the release directory to all systems
   participating in the test. fatjar is in contrib/fatjar directory.

   (developers can generate by running "ant jar compile-test"
   targets in trunk, then compiling using "ant jar" in src/contrib/jarjar)

2) run a zookeeper standalone instance (cluster is ok too)

e.g. java -jar zookeeper-<version>-fatjar.jar server <zoo.cfg>

Note: you must provide zoo.cfg, see sample in conf directory

3) on each host start the system test container

e.g. java -jar zookeeper-<version>-fatjar.jar ic <name> <zkHostPort> /sysTest

name : name of the test container - must be unique 
  typically it's a good idea to name after the host to aid debugging

zkHostPort : the host:port of the server from step 2)

4) initiate the system test using the fatjar:

java -jar build/contrib/fatjar/zookeeper-<version>-fatjar.jar systest org.apache.zookeeper.test.system.SimpleSysTest

by default it will access the zk server started in 2) on localhost:2181 

or you can specify a remote host:port using
  -DsysTest.zkHostPort=<host>:<port>,<host>:<port>,...

java -DsysTest.zkHostPort=hostA:2181  -jar build/contrib/fatjar/zookeeper-<version>-fatjar.jar systest org.apache.zookeeper.test.system.SimpleSysTest

where hostA is running the zk server started in step 2) above

InstanceContainers can also be used to run a the saturation benchmark. The
first two steps are the same as the system test. Step 3 is almost the same:

3) start the InstanceContainer on each host:

e.g. java -jar zookeeper-<version>-fatjar.jar ic <name> <zkHostPort> <prefix>

note prefix can be /sysTest or any other path. If you do use /sysTest, make
sure the system test isn't running when you run the benchmark.

4) run GenerateLoad using the following

java -jar build/contrib/fatjar/zookeeper-<version>-fatjar.jar generateLoad <zkHostPort> <prefix> #servers #clients

Once GenerateLoad is started, it will read commands from stdin. Usually
the only command you need to know is "percentage" which sets the percentage
of writes to use in the requests. Once a percentage is set, the benchmark
will start. "percentage 0" will cause only reads to be issued and
"percentage 100" will cause only writes to be issued.
1) This source directory contains various Zookeeper recipe implementations. 

2) The recipe directory name should specify the name of the recipe you are implementing - eg. lock/.

3) It would be great if you can provide both the java and c recipes for the zookeeper recipes.
The c recipes go in to recipe-name/src/c and the java implementation goes into recipe-name/src/java.

4) The recipes hold high standards like our zookeeper c/java libraries, so make sure that you include
some unit testing with both the c and java recipe code.

5) Also, please name your c client public methods as
zkr_recipe-name_methodname
(eg. zkr_lock_lock in lock/src/c)

6) The various recipes are in ../../docs/recipes.html or
../../docs/reciped.pdf. Also, this is not an exhaustive list by any chance.
Zookeeper is used (and can be used) for more than what we have listed in the docs.

7) To run the c tests in all the recipes, 
- make sure the main zookeeper c libraries in
{top}/src/c/ are compiled. Run autoreconf -if;./configure; make. The libaries
will be installed in {top}/src/c/.libs. 
- run autoreconf if;./configure;make run-check 
  in src/recipes/$recipename/src/c

<!--
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

1) This election interface recipe implements the leader election recipe
mentioned in ../../../docs/recipes.[html,pdf].

2) To compile the leader election java recipe you can just run ant jar from
this directory.
Please report any bugs on the jira 

http://issues.apache.org/jira/browse/ZOOKEEPER

  
<!--
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

1) This queue interface recipe implements the queue recipe
mentioned in ../../../docs/recipes.[html,pdf].
A more detailed explanation is at http://www.cloudera.com/blog/2009/05/28/building-a-distributed-concurrent-queue-with-apache-zookeeper/

2) This recipe does not handle KeeperException.ConnectionLossException or ZCONNECTIONLOSS. It will only work correctly once ZOOKEEPER-22 https://issues.apache.org/jira/browse/ZOOKEEPER-22 is resolved.

3) To compile the queue java recipe you can just run ant jar from 
this directory. 
Please report any bugs on the jira 

http://issues.apache.org/jira/browse/ZOOKEEPER

  
                     Zookeeper C queue client library 


INSTALLATION

If you're building the client from a source checkout you need to
follow the steps outlined below. If you're building from a release
tar downloaded from Apache please skip to step 2.

This recipe does not handle ZCONNECTIONLOSS. It will only work correctly once ZOOKEEPER-22 https://issues.apache.org/jira/browse/ZOOKEEPER-22 is resolved.

1) make sure that you compile the main zookeeper c client library.
 
2) change directory to src/recipes/queue/src/c 
    and do a "autoreconf -if" to bootstrap
   autoconf, automake and libtool. Please make sure you have autoconf
   version 2.59 or greater installed.
3) do a "./configure [OPTIONS]" to generate the makefile. See INSTALL
   for general information about running configure.

4) do a "make" or "make install" to build the libraries and install them. 
   Alternatively, you can also build and run a unit test suite (and
   you probably should).  Please make sure you have cppunit-1.10.x or
   higher installed before you execute step 4.  Once ./configure has
   finished, do a "make run-check". It will build the libraries, build
   the tests and run them.
5) to generate doxygen documentation do a "make doxygen-doc". All
   documentations will be placed to a new subfolder named docs. By
   default only HTML documentation is generated.  For information on
   other document formats please use "./configure --help"
<!--
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

1) This lock interface recipe implements the lock recipe
mentioned in ../../../docs/recipes.[html,pdf].

2) To compile the lock java recipe you can just run ant jar from 
this directory. For compiling the c libarary go to src/c and read
the INSTALLATION instructions. 
Please report any bugs on the jira 

http://issues.apache.org/jira/browse/ZOOKEEPER

  
                     Zookeeper C lock client library 


INSTALLATION

If you're building the client from a source checkout you need to
follow the steps outlined below. If you're building from a release
tar downloaded from Apache please skip to step 2.

1) make sure that you compile the main zookeeper c client library.
 
2) change directory to src/recipes/lock/src/c 
    and do a "autoreconf -if" to bootstrap
   autoconf, automake and libtool. Please make sure you have autoconf
   version 2.59 or greater installed.
3) do a "./configure [OPTIONS]" to generate the makefile. See INSTALL
   for general information about running configure.

4) do a "make" or "make install" to build the libraries and install them. 
   Alternatively, you can also build and run a unit test suite (and
   you probably should).  Please make sure you have cppunit-1.10.x or
   higher installed before you execute step 4.  Once ./configure has
   finished, do a "make run-check". It will build the libraries, build
   the tests and run them.
5) to generate doxygen documentation do a "make doxygen-doc". All
   documentations will be placed to a new subfolder named docs. By
   default only HTML documentation is generated.  For information on
   other document formats please use "./configure --help"
==========================================
zktreeutil - Zookeeper Tree Data Utility
Author: Anirban Roy
Organization: Yahoo Inc.
==========================================

zktreeutil program is intended to manage and manipulate zk-tree data quickly, effi-
ciently and with ease. The utility operates on free-form ZK-tree and hence can be used
for any cluster managed by Zookeeper. Here are the basic functionalities -

EXPORT: The whole/partial ZK-tree is exported into a XML file. This helps in
capturing a current snapshot of the data for backup/analysis. For a subtree
export, one need to specify the path to the ZK-subtree with proper option.

IMPORT: The ZK-tree can be imported from XML into ZK cluster. This helps in priming
the new ZK cluster with static configuration. The import can be non-intrusive by
making only the additions in the existing data. The import of subtree is also
possible by optionally providing the path to the ZK-subtree.

DIFF: Creates a diff between live ZK data vs data saved in XML file. Diff can ignore
some ZK-tree branches (possibly dynamic data) on reading the optional ignore flag
from XML file. Diffing on a ZK-subtree achieved by providing path to ZK-subtree with
diff command.

UPDATE: Make the incremental changes into the live ZK-tree from saved XML, essentia-
lly after running the diff.

DUMP: Dumps the ZK-tree on the standard output device reading either from live ZK
server or XML file. Like export, ZK-subtree can be dumped with optionaly
providing the path to the ZK-subtree, and till a certain depth of the (sub)tree.

The exported ZK data into XML file can be shortened by only keeping the static ZK
nodes which are required to prime a cluster. The dynamic zk nodes (created on-the-
fly) can be ignored by setting a 'ignore' attribute at the root node of the dynamic
subtree (see tests/zk_sample.xml), possibly deleting all inner ZK nodes under that.
Once ignored, the whole subtree is ignored during DIFF, UPDATE and WRITE.

Pre-requisites
--------------
1. Linux system with 2.6.X kernel.
2. Zookeeper C client library (locally built at ../../c/.libs) >= 3.X.X
3. Development build libraries (rpm packages):
  a. boost-devel >= 1.32.0
  b. libxml2-devel >= 2.7.3
  c. log4cxx0100-devel >= 0.10.0

Build instructions
------------------
1. cd into this directory
2. autoreconf -if
3. ./configure
4. make
5. 'zktreeutil' binary created under src directory

Limitations
-----------
Current version works with text data only, binary data will be supported in future
versions.

Testing  and usage of zktreeutil
--------------------------------
1.  Run Zookeeper server locally on port 2181
2.  export LD_LIBRARY_PATH=../../c/.libs/:/usr/local/lib/
3.  ./src/zktreeutil --help # show help
4.  ./src/zktreeutil --zookeeper=localhost:2181 --import --xmlfile=tests/zk_sample.xml 2>/dev/null                 # import sample ZK tree
5.  ./src/zktreeutil --zookeeper=localhost:2181 --dump --path=/myapp/version-1.0 2>/dev/null                         # dump Zk subtree 
5.  ./src/zktreeutil --zookeeper=localhost:2181 --dump --depth=3 2>/dev/null                                                 # dump Zk tree till certain depth
6.  ./src/zktreeutil --xmlfile=zk_sample.xml -D 2>/dev/null                                                                     # dump the xml data
7.  Change zk_sample.xml with adding/deleting/chaging some nodes 
8.  ./src/zktreeutil -z localhost:2181 -F -x zk_sample.xml -p /myapp/version-1.0/configuration 2>/dev/null          # take a diff of changes
9.  ./src/zktreeutil -z localhost:2181 -E 2>/dev/null > zk_sample2.xml                                                         # export the mofied ZK tree
10. ./src/zktreeutil -z localhost:2181 -U -x zk_sample.xml -p /myapp/version-1.0/distributions 2>/dev/null        # update with incr. changes
11. ./src/zktreeutil --zookeeper=localhost:2181 --import --force --xmlfile=zk_sample2.xml 2>/dev/null             # re-prime the ZK tree

﻿==========================================
ZooInspector - Browser and Editor for ZooKeeper Instances
Author: Colin Goodheart-Smithe
Date: February 2010
==========================================

ZooInspector is a Java Swing based application for browsing and editing ZooKeeper instances.

Contents
--------
	- Features
	- Pre-requisites
	- Build Instructions
	- Using ZooInspector
	- Creating and Using Plugins
	
Features
--------
	Below is a list of features in the current release of ZooInspector.
	- Load connection settings from a zookeeper properties file
	- Plugable DataEncryptionManagers to specify how data should be encrypted and decrypted in the Zookeeper instance
	- Browseable tree view of the ZooKeeper instance
	- View the data in a node
	- View the ACL's currently applied to a node
	- View the metadata for a node (Version, Number of Children, Last modified Tiem, etc.)
	- Plugable NodeViewers interface
	- Ability to save/load and set default Node Viewers
	
Pre-requisites
--------------
	- The main zookeeper build script must have been run before building this module
	
Build Instructions
------------------
	1. Open a command line.
	2. cd into this directory
	3. Run command: ant
	4. ZooInspector will be built to ../../../build/contrib/ZooInspector
	5. Copy zookeeper-3.x.x.jar into the lib sub-directory (if you are using zookeeper-3.3.0.jar it will have been
       copied to this directory during the build
	6. By default the zookeeper.cmd and zookeeper.sh files expect zookeeper-3.3.0.jar.  If you are using another version
	   you will need to change these files to point to the zookeeper-3.x.x.jar you copied to the lib directory
	7. To run ZooInspector run zooInspector.cmd (on Windows) or zooInspector.sh (on Linux).  If you are using 
	   zookeeper-3.3.0.jar and do not require any classpath changes you can run the zookeeper-dev-ZooInspector.jar
	   directly

Using ZooInspector
------------------
	To start ZooInspector run zooInspector.cmd (on Windows) or zooInspector.sh (on Linux).  If you are using 
	zookeeper-3.3.0.jar and do not require any classpath changes you can run the zookeeper-dev-ZooInspector.jar
	directly.
	
	Click the play button on the toolbar to bring up the connection dialog.  From here you can enter connection 
	information for your zookeeper instance.  You can also load the connection properties from a file.  This file can 
	have the format as a normal zookeeper properties file (i.e. hosts and timeout key-value pairs) and van optional have
	an encryptionManager key-value pair to specify the DataEncryptionManager to use for this connection 
	(DataEncryptionManagers are explained in further detail in the 'Creating and Using Plugins' section below).  You can
	also set the entered information as the defaults so that when you first start ZooInspector these settings are 
	automatically loaded into this dialog.  Pressing the OK button with connect to your ZooKeeper instance and show the
	current node tree on the left of the main panel.
	
	Clicking a node in the node tree will load the data for that node into the node viewers.  Three node viewers are 
	currently distributed with ZooInspector:
		1. Node Data - This enables you to see the data current stored on that node.  This data can be modified and 
		   saved.  The data is decrypted and encrypted using the DataEncryptionManager specified on the connection 
		   dialog.
		2. Node Metadata - This enables you to see the metadata associiated with this node.  This is Essentially the data
		   obtained from the Stat object for this node.
		3. Node ACLs - This allows you to see the ACLs currently applied to this node.  Currently there is no ability
		   to change the ACLs on a node, but it is a feature I would like to add.
	Other custom Node Viewers can be added, this is explained in the 'Creating and Using Plugins' section below.
	

Creating and Using Plugins
--------------------------
	There are two types of plugin which can be used with ZooInspector:
		1. DataEncryptionManager - This specifies how data should be encrypted and decrypted when working with a 
		   zookeeper instance.
		2. ZooInspectorNodeViewer - This is a GUI panel which provides a view of visualisation on a node.
	More information on these interfaces can be found in the javadocs for this module.
	
	To use a plugin in ZooInspector, build the plugin to a jar and copy the jar to the lib sub-directory.  Edit the 
	zooInspector.cmd and/or zooInspector.sh files to include your new jar on the classpath and run ZooInspector.
	
	For DataEncryptionManagers, click the play button to open the connection dialog and enter the full class name of 
	your DataEncryptionManager in the 'Data Encryption Manager' field.  You can make this Data Encryption Manager the 
	default by clicking 'Set As Default'.  Click the 'OK' button to instantiate and use your plugin.
	
	For ZooInspectorNodeViewers, Click the 'Change Node Viewers' button on the toolbar (looks like a tree with a pencil)
	and enter the full classname for your Node Viewer in the field left of the 'Add' button, then click the 'Add' 
	button.  The Node Viewer will be instantiated and should appear in the list.  You can change the order of the Node 
	viewers by clicking the up and dpwn buttons and delete a Node Viewer by clicking the delete button.  You can save 
	to configuration to a file or set it as the default if necessary. Then click the 'OK' button and your Node Viewer 
	should appear in the tabs on the right of the main panel.
ZooKeeper REST implementation using Jersey JAX-RS.
--------------------------------------------------

This is an implementation of version 2 of the ZooKeeper REST spec.

Note: This interface is currently experimental, may change at any time,
etc... In general you should be using the Java/C client bindings to access
the ZooKeeper server.

This REST ZooKeeper gateway is useful because most of the languages
have built-in support for working with HTTP based protocols.

See SPEC.txt for details on the REST binding.

Quickstart:
-----------

1) start a zookeeper server on localhost port 2181

2) run "ant run"

3) use a REST client to access the data (see below for more details)

  curl http://localhost:9998/znodes/v1/

or use the provided src/python scripts 

  zk_dump_tree.py


Tests:
----------

1) the full testsuite can be run via "ant test" target
2) the python client library also contains a test suite

Examples Using CURL
-------------------

First review the spec SPEC.txt in this directory.

#get the root node data
curl http://localhost:9998/znodes/v1/

#get children of the root node
curl http://localhost:9998/znodes/v1/?view=children

#get "/cluster1/leader" as xml (default is json)
curl -H'Accept: application/xml' http://localhost:9998/znodes/v1/cluster1/leader

#get the data as text
curl -w "\n%{http_code}\n" "http://localhost:9998/znodes/v1/cluster1/leader?dataformat=utf8"

#set a node (data.txt contains the ascii text you want to set on the node)
curl -T data.txt -w "\n%{http_code}\n" "http://localhost:9998/znodes/v1/cluster1/leader?dataformat=utf8"

#create a node
curl -d "data1" -H'Content-Type: application/octet-stream' -w "\n%{http_code}\n" "http://localhost:9998/znodes/v1/?op=create&name=cluster2&dataformat=utf8"

curl -d "data2" -H'Content-Type: application/octet-stream' -w "\n%{http_code}\n" "http://localhost:9998/znodes/v1/cluster2?op=create&name=leader&dataformat=utf8"

#create a new session
curl -d "" -H'Content-Type: application/octet-stream' -w "\n%{http_code}\n" "http://localhost:9998/sessions/v1/?op=create&expire=10"

#session heartbeat
curl -X "PUT" -H'Content-Type: application/octet-stream' -w "\n%{http_code}\n" "http://localhost:9998/sessions/v1/02dfdcc8-8667-4e53-a6f8-ca5c2b495a72"

#delete a session
curl -X "DELETE" -H'Content-Type: application/octet-stream' -w "\n%{http_code}\n" "http://localhost:9998/sessions/v1/02dfdcc8-8667-4e53-a6f8-ca5c2b495a72"



In order to generate .jks (java keystore files) you need to use keytool.

The password for the existing .jks is "123456" (without quotes).

Some tutorials:
 - http://www.mobilefish.com/tutorials/java/java_quickguide_keytool.html

Some basic python scripts which use the REST interface:

zkrest.py -- basic REST ZooKeeper client
demo_master_election.py -- shows how to implement master election
demo_queue.py -- basic queue
zk_dump_tree.py -- dumps the nodes & data of a znode hierarchy

Generally these scripts require:
  * simplejson
Net::ZooKeeper - Perl extension for Apache ZooKeeper
====================================================

Net::ZooKeeper provides a Perl interface to the synchronous C API
of Apache ZooKeeper.  ZooKeeper is coordination service for
distributed applications.
For details see the ZooKeeper home page at:

http://zookeeper.apache.org/

INSTALLATION

To install this module type the following, first install the
zookeeper C client, then:

    perl Makefile.PL
    make
    ZK_TEST_HOSTS=host:port,... make test
    make install

If the C headers and library are installed in non-standard
locations, specify them as arguments to Makefile.PL:
    
    perl Makefile.PL \
        --zookeeper-include=/path/to/zookeeper/client/include \
        --zookeeper-lib=/path/to/zookeeper/client/lib

The path supplied to the --zookeeper-include option should
identify the directory that contains the zookeeper.h and other
ZooKeeper C include files.

The path supplied to the --zookeeper-lib option should identify
the directory that contains the libzookeeper_mt library.

When running "make test", if no ZK_TEST_HOSTS environment
variable is set, many tests will be skipped because no connection
to a ZooKeeper server is available.  To execute these tests,
the ZK_TEST_HOSTS variable may be assigned a list of one or more
ZooKeeper host:port pairs, e.g., "localhost:7100,otherhost:7200".

The ZK_TEST_PATH environment variable, if defined, specifies
the ZooKeeper path under which all test nodes should be created.
The tests expect to have full read/write/create/delete/admin
ZooKeeper permissions under this path.  If no ZK_TEST_PATH
variable is defined, the root ZooKeeper path ("/") is used.

DEPENDENCIES

Version 3.1.1 of ZooKeeper is required at a minimum.

For version 3.1.1, you may also want to apply some of these
additional patches to the ZooKeeper C API code:

https://issues.apache.org/jira/browse/ZOOKEEPER-262
https://issues.apache.org/jira/browse/ZOOKEEPER-318

For version 3.1.1, you may also want to apply some of these
additional patches to the ZooKeeper C API code:

https://issues.apache.org/jira/browse/ZOOKEEPER-262
https://issues.apache.org/jira/browse/ZOOKEEPER-466

This module requires that the multi-threaded version of the
ZooKeeper C API client library be available on your system.

This in turn implies that the POSIX pthread library is available
as well.

COPYRIGHT AND LICENCE

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Original authors of zkfuse are Swee Lim & Bartlomiej M Niechwiej of Yahoo.
'
ZooKeeper FUSE (File System in Userspace)
=========================================

Pre-requisites
--------------
1. Linux system with 2.6.X kernel.
2. Fuse (Filesystem in Userspace) must be installed on the build node. 
3. Development build libraries:
  a. fuse
  b. log4cxx
  c. pthread
  d. boost

Build instructions
------------------
1. cd into this directory
2. autoreconf -if
3. ./configure
4. make
5. zkfuse binary is under the src directory

Testing Zkfuse
--------------
1. Depending on permission on /dev/fuse, you may need to sudo -u root.
   * If /dev/fuse has permissions 0600, then you have to run Zkfuse as root.
   * If /dev/fuse has permissions 0666, then you can run Zkfuse as any user.
2. Create or find a mount point that you have "rwx" permission. 
   * e.g. mkdir -p /tmp/zkfuse
3. Run Zkfuse as follows:
   zkfuse -z <hostspec> -m /tmp/zkfuse -d
   -z specifies ZooKeeper address(es) <host>:<port>
   -m specifies the mount point
   -d specifies the debug mode.
   For additional command line options, try "zkfuse -h".

FAQ
---
Q. How to fix "warning: macro `AM_PATH_CPPUNIT' not found in library"?
A. * install cppunit (src or pkg) on build machine

Q. Why can't Zkfuse cannot write to current directory?
A. * If Zkfuse is running as root on a NFS mounted file system, it will not
     have root permissions because root user is mapped to another user by
     NFS admin.
   * If you run Zkfuse as root, it is a good idea to run Zkfuse from a
     directory that you have write access to. This will allow core files
     to be saved.

Q. Why Zkfuse cannot mount?
A. * Check that the mount point exists and you have "rwx" permissions.
   * Check that previous mounts have been umounted. If Zkfuse does not 
     exit cleanly, its mount point may have to be umounted manually. 
     If you cannot umount manually, make sure that there no files is open 
     within the mount point.

Q. Why does Zkfuse complain about logging at startup?
A. * Zkfuse uses log4cxx for logging. It is looking for log4cxx.properties
     file to obtain its logging configuration.
   * There is an example log4cxx.properties file in the Zkfuse source 
     directory.


Tools and Recipes for ZooKeeper Monitoring
------------------------------------------

How To Monitor
--------------

A ZooKeeper cluster can be monitored in two ways:
 1. by using the 'mntr' 4letterword command
 2. by using JMX to query the MBeans 

This repo contains tools and recipes for monitoring ZooKeeper using the first method. 

Check the file JMX-RESOURCE for some links to resources that could help you monitor a ZooKeeper cluster using the JMX interface. 

Requirements
------------

ZooKeeper 3.4.0 or later or you can apply ZOOKEEPER-744 patch over the latest 3.3.x release.
The server should understand the 'mntr' 4letterword command. 

$ echo 'mntr' | nc localhost 2181
zk_version  3.4.0--1, built on 06/19/2010 15:07 GMT
zk_avg_latency  141
zk_max_latency  1788
zk_min_latency  0
zk_packets_received 385466
zk_packets_sent 435364
zk_outstanding_requests 0
zk_server_state follower
zk_znode_count  5
zk_watch_count  0
zk_ephemerals_count 0
zk_approximate_data_size    41
zk_open_file_descriptor_count   20
zk_max_file_descriptor_count    1024

Python 2.6 (maybe it works on previous version but it's not tested yet).

In a nutshell
-------------

All you need is check_zookeeper.py It has no external dependencies. 


*** On Nagios call the script like this:

./check_zookeeper.py -o nagios -s "<server-or-list-of-servers>" -k <key> -w <warning> -c <critical>


*** On Cacti define a custom data input method using the script like this:

./check_zookeeper.py -o cacti -s "<list-of-servers>" -k <key> --leader

-- outputs a single value for the given key fetched from the cluster leader

OR 

./check_zookeeper.py -o cacti -s "<list-of-servers>" -k <key> 

-- outputs multiple values on for each cluster node
ex: localhost_2182:0  localhost_2183:0  localhost_2181:0  localhost_2184:0  localhost_2185:0

*** On Ganglia:

install the plugin found in the ganglia/ subfolder OR

./check_zookeeper.py -o ganglia -s "<current-zookeeper-node>"

it will use gmetric to send zookeeper node status data.


Check the subfolders for configuration details and samples for each platform.

License
-------

Apache License 2.0 or later.

ZooKeeper 4letterwords Commands
-------------------------------

http://zookeeper.apache.org/docs/current/zookeeperAdmin.html#sc_zkCommands

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Configuration Recipe for monitoring ZooKeeper using Nagios
----------------------------------------------------------

I will start by making the assumption that you already have an working Nagios install.

WARNING: I have wrote these instructions while installing and configuring the plugin on my desktop computer running Ubuntu 9.10. I've installed Nagios using apt-get.

WARNING: You should customize the config files as suggested in order to match your Nagios and Zookeeper install. 

WARNING: This README assumes you know how to configure Nagios and how it works. 

WARNING: You should customize the warning and critical levels on service checks to meet your own needs. 

1. Install the plugin

$ cp check_zookeeper.py /usr/lib/nagios/plugins/

2. Install the new commands

$ cp zookeeper.cfg /etc/nagios-plugins/config

3. Update the list of servers in zookeeper.cfg for the command 'check_zookeeper' and update the port for the command 'check_zk_node' (default: 2181)

4. Create a virtual host in Nagios used for monitoring the cluster as a whole -OR-  Create a hostgroup named 'zookeeper-servers' and add all the zookeeper cluster nodes. 

5. Define service checks like I have ilustrated bellow or just use the provided definitions.

define service {
    use         generic-service
    host_name   zookeeper-cluster
    service_description ...
    check_command check_zookeeper!<exported-var>!<warning-level>!<critical-level>
}

define service {
    hostgroup_name  zookeeper-servers                    
    use generic-service                                  
    service_description ZK_Open_File_Descriptors_Count   
    check_command check_zk_node!<exported-var>!<warning-level>!<critical-level>
}

Ex: 

a. check the number of open file descriptors

define service{
        use         generic-service
        host_name   zookeeper-cluster
        service_description ZK_Open_File_Descriptor_Count
        check_command check_zookeeper!zk_open_file_descriptor_count!500!800
}

b. check the number of ephemerals nodes

define service {
        use generic-service
        host_name localhost
        service_description ZK_Ephemerals_Count
        check_command check_zookeeper!zk_ephemerals_count!10000!100000
}

c. check the number of open file descriptors for each host in the group

define service {
    hostgroup_name  zookeeper-servers                    
    use generic-service                                  
    service_description ZK_Open_File_Descriptors_Count   
    check_command check_zk_node!zk_open_file_descriptor_count!500!800
}

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Recipes for ZooKeeper monitoring using Ganglia
----------------------------------------------

Ganglia Install guide: http://sourceforge.net/apps/trac/ganglia/wiki/Ganglia%203.1.x%20Installation%20and%20Configuration 

Gmond configuration: http://sourceforge.net/apps/trac/ganglia/wiki/Gmond%203.1.x%20General%20Configuration 

WARNING: I have wrote these instructions while installing and configuring the plugin on my desktop computer running Ubuntu 9.10. I've installed Ganglia using apt-get.

WARNING: I'm going to make the assumption that you know how to work with Ganglia. I'm also going to assume that you have already installed Gangli and everything works as expected.

You can monitoring ZooKeeper using Ganglia in two ways:

1. Using a python module:

    WARNING! The python module only works with Ganglia 3.1.x 

    a. enable python modules: you can find instructions in modpython.confg
    b. copy zookeeper.pyconf in /etc/ganglia/conf.d/
    c. copy zookeeper_ganglia.py in /usr/lib/ganglia/python_plugins
    d. restart the ganglia-monitor

    This is the recommended way!

2. OR Using check_zookeeper.py and gmetric:

    Monitoring ZooKeeper using Ganglia is a simple as calling:

    ./check_zookeeper.py -o ganglia -s localhost:2181 

    on each of the ZooKeeper cluster nodes. I'm making the assumption that you have already configured gmond and installed gmetric on each node.

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Recipes for ZooKeeper monitoring using Cacti
--------------------------------------------

Cacti install guide: https://help.ubuntu.com/community/Cacti

Cacti Manual: http://www.cacti.net/downloads/docs/html/
PDF version: http://www.cacti.net/downloads/docs/pdf/manual.pdf 

Check Chapter 16: Simplest Method of Going from Script to Graph
    http://www.cacti.net/downloads/docs/html/how_to.html#SCRIPT_TO_GRAPH

WARNING: I have wrote these instructions while installing and configuring the plugin on my desktop computer running Ubuntu 9.10. I've installed Cacti using apt-get.

WARNING: I'm going to make the assumption that you know how to work with Cacti and how to setup Data Input Methods for custom scripts. I'm also going to assume that you have already installed Cacti and everything works as expected.

You can extend the Cacti's data gathering functionality through external scripts. Cacti comes with a number of scripts out of the box wich are localted in the scripts/ directory. 


The check_zookeeper.py script can be used a  custom data input method for Cacti.

Single value (check cluster status by sending queries to the leader):
---------------------------------------------------------------------

python <path_cacti>scripts/check_zookeeper.py -s "localhost:2181,localhost:2182,localhost:2183,localhost:2184,localhost:2185" -k <key> -o cacti --leader

When you will call the script this way it will about a single value representing the value attached to this <key>.


Multiple values (one for each cluster node):
--------------------------------------------

python <path_cacti>scripts/check_zookeeper.py -s "localhost:2181,localhost:2182,localhost:2183,localhost:2184,localhost:2185" -k <key> -o cacti

Output:
localhost_2182:0  localhost_2183:0  localhost_2181:0  localhost_2184:0  localhost_2185:0


TBD: Step by step guide


LogGraph README

1 - About
LogGraph is an application for viewing and filtering zookeeper logs. It can handle transaction logs and message logs. 

2 - Compiling

Run "ant jar" in src/contrib/loggraph/. This will download all dependencies and compile all the loggraph code.

Once compilation has finished, you can run it the the loggraph.sh script in src/contrib/loggraph/bin. This will start and embedded web server on your machine. 
Navigate to http://localhost:8182/graph/main.html

3 - Usage
LogGraph presents the user with 4 views, 
 
  a) Simple log view
     This view simply displays the log text. This isn't very useful without filters (see "Filtering the logs").

  b) Server view
     The server view shows the interactions between the different servers in an ensemble. The X axis represents time. 
        * Exceptions show up as red dots. Hovering your mouse over them will give you more details of the exception
	* The colour of the line represents the election state of the server. 
	   - orange means LOOKING for leader
	   - dark green means the server is the leader
	   - light green means the server is following a leader
	   - yellow means there isn't enough information to determine the state of the server. 
	* The gray arrows denote election messages between servers. Pink dashed arrows are messages that were sent but never delivered.

  c) Session view
     The session view shows the lifetime of sessions on a server. Use the time filter to narrow down the view. Any more than about 2000 events will take a long time to view in your browser. 
     The X axis represents time. Each line is a session. The black dots represent events on the session. You can click on the black dots for more details of the event.

  d) Stats view
     There is currently only one statistics view, Transactions/minute. Suggestions for other statistic views are very welcome.

4 - Filtering the logs
The logs can be filtered in 2 ways, by time and by content. 

To filter by time simply move the slider to the desired start time. The time window specifies how many milliseconds after and including the start time will be displayed.

Content filtering uses a adhoc filtering language, using prefix notation. The language looks somewhat similar to lisp. A statement in the language takes the form (op arg arg ....). A statement resolves to a boolean value. Statements can be nested. 

4.1 - Filter arguments
An argument can be a number, a string or a symbol. A number is any argument which starts with -, + or 0 to 9. If the number starts with 0x it is interpretted as hexidecimal. Otherwise it is interpretted as decimal. If the argument begins with a double-quote, (") it is interpretted as a string. Anything else is interpretted as a symbol.

4.2 - Filter symbols
The possible filter symbols are: 

client-id : number, the session id of the client who initiated a transaction.
cxid : number, the cxid of a transaction
zxid : number, the zxid of a transaction
operation : string, the operation being performed, for example "setData", "createSession", "closeSession", "error", "create"

4.3 - Filter operations
The possible filter operations are:

or : logical or, takes 1 or more arguments which must be other statements.
and : logical and, takes 1 or more arguments which must be other statements.
not : logical not, takes 1 argument which must be another statement.
xor : exclusive or, takes 1 or more arguments which must be other statements.
= : equals, takes 1 or more arguments, which must all be equal to each other to return true.
> : greater than, takes 1 or more arguments, to return true the 1st argument must be greater than the 2nd argument which must be greater than the 3rd argument and so on... 
< : less than, takes 1 or more arguments, to return true the 1st argument must be less than the 2nd argument which must be less than the 3rd argument and so on... 

4.3 - Filter examples
Give me all the setData operations with session id 0xdeadbeef or 0xcafeb33r but not with zxid 0x12341234 ->

(and (= operation "setData") (or (= client-id 0xdeadbeef) (= client-id 0xcafeb33r)) (not (= zxid 0x12341234)))

This package contains build to create a fat zookeeper jar. You need to run ant to create the fat jar.
To run the fatjar you can use. java -jar zoookeeper-*fatjar.jar 
Early version of ZooKeeper bindings for Python. All functions are imported as methods into the zookeeper module.

Please do not rely on APIs staying constant in the short term. The handling of exceptions and failure modes is one area that is subject to change. 

DEPENDENCIES:
-------------

This has only been tested against SVN (i.e. 3.2.0 in development) but should work against 3.1.1. 

You will need the Python development headers installed to build the module - on many package-management systems, these can be found in python-devel.

Python >= 2.6 is required. We have tested against 2.6. We have not tested against 3.x. 

BUILD AND INSTALL:
-------------------

To install, make sure that the C client has been built and that the libraries are installed in /usr/local/lib (or change this directory in setup.py). Then run:

ant install

from zookeeper/src/contrib/zkpython/.

To test, run ant test from the same directory. 

You can compile the module without installing by running

ant compile

In order to use the module, zookeeper.so must be in your PYTHONPATH or in one of the directories referenced by sys.path. Running ant install should make sure that this is the case, but if you only run ant compile you probably need to add build/contrib/zkpython/* to PYTHONPATH to find the module. The C client libraries must be in a system library path, or LD_LIBRARY_PATH or DYLD_LIBRARY_PATH (Mac OS) for the module to work correctly, otherwise you will see a library not found error when trying to import the module. 

NAMING CONVENTIONS:
--------------------

All methods that in the C library are zoo_fn_name have been implemented as zookeeper.fn_name. The exception is any function that has a watch function argument is named without the 'w' prefix (for example, zoo_wexists becomes zookeeper.exists). The variants of these functions without the watch argument (i.e. zoo_exists) have not been implemented on the understanding that they are superseded by the zoo_w* API. 

Enums and integer constants that begin ZOO_int_name are named as zookeeper.int_name.

PARAMETER CHANGES:
------------------

Zookeeper handles are represented as integers to avoid marshalling the entire structure for every call. Therefore they are opaque from Python. 

Any parameter that is used to provide arguments to callback methods is not exposed in the API. Python provides better mechanisms for providing a closure to be called in the future.

Every callback gets passed the handle of the ZooKeeper instance used to register the callback.

DATA TYPES:
-----------

ACL_vectors are lists of dictionaries. Stat structures are dictionaries. String_vectors are lists of strings.

EXCEPTIONS AND ERROR HANDLING:
------------------------------

Currently synchronous calls indicate failure by throwing an exception (note that this includes the synchronous calls to set up asynchronous completion callbacks!). Success is returned as an integer. 

Callbacks signify failure by having the integer response code passed in. 

WHAT'S NEW IN 0.4:
------------------

More test coverage. 

Better reference counting, fixing at least two serious bugs.

Out-of-range zhandles are now checked, fixing a potential security hole.

Docstrings! Editing and cleanup required, but most of the text is there.

zookeeper.set_watcher is now implemented correctly.

zookeeper.client_id is now implemented correctly. zookeeper.init now respects the client_id parameter.

get_context and set_context have been removed from the API. The context mechanism is used by PyZK to store the callables that are dispatched by C-side watchers. Messing with this from Python-side causes bugs very quickly. You should wrap all desired context up in a callable and then use zookeeper.set_watcher to attach it to the global watcher. 

Many methods now have optional parameters (usually if you can specify a watch, it's optional). The only time where genuinely optional parameters are still mandatory is when a required parameters comes after it. Currently we still respect the ZK C client parameter ordering. For example, you can simply connect with zookeeper.init("host:port") and ignore the other three parameters.


WHAT'S NEW IN 0.3:
------------------

Some tests in zkpython/test. More to follow!

A variety of bugfixes.

Changed the way methods return results - all responses are integers now, for the client to convert to a string if it needs.

WHAT'S NEW IN 0.2:
------------------

The asynchronous API is now implemented (see zookeeper.a*).

Most enums defined in zookeeper.h are now added as constants to the module.

_set2 and a few other edge API calls have been implemented. The module is now nearly 100% feature complete!

A reference count error was tracked down and killed. More probably lurk in there!

WHAT'S NOT DONE / KNOWN ISSUES / FUTURE WORK:
---------------------------------------------

1. There may well be more memory leaks / reference count issues; however I am more confident that common paths are relatively safe. 
2. There probably needs to be a more Pythonic Python-side wrapper for these functions (e.g. a zookeeper object, the ability to iterate through a tree of zk nodes)
3. Docstrings need a cleanup.
4. The way exceptions and error codes are returned needs looking at. Currently synchronous calls throw exceptions on everything but ZOK return, but asynchronous completions are simply passed the error code. Async. functions should never throw an exception on the C-side as they are practically impossible to catch. For the sync. functions, exceptions seem more reasonable, but some cases are certainly not exceptional. 

Bug reports / comments very welcome!

Henry Robinson henry@cloudera.com

This folder contains sample showing how you can use ZooKeeper from Python.

You should also check the following projects:

* http://github.com/phunt/zk-smoketest
* http://github.com/henryr/pyzk-recipes 


ZooKeeper Browser - Hue Application
===================================

The ZooKeeper Browser application allows you to see how the cluster nodes are working and also allows you to do CRUD operations on the znode hierarchy.

Requirements
------------

Hue-1.0:
  * http://github.com/downloads/cloudera/hue/hue-1.0.tgz
  * http://github.com/downloads/cloudera/hue/release-notes-1.0.html

ZooKeeper REST gateway:
  * available as contrib: contrib/rest

How to install?
---------------

First of all you need to install Hue 1.0 release:

  * http://archive.cloudera.com/cdh/3/hue/sdk/sdk.html
  * http://github.com/cloudera/hue/tree/release-1.0

After you finish the previous step you should copy the zkui/ folder to apps/ and register the new application:

  * $ ./build/env/bin/python tools/app_reg/app_reg.py --install apps/zkui
  * $ ./build/env/bin/python tools/app_reg/app_reg.py --list 2>&1 | grep zkui
    zkui           0.1     /Users/philip/src/hue/apps/zkui


And restart the Hue application server.

Configuration
-------------

Edit zkui/src/zkui/settings.py:

CLUSTERS = [{
        'nice_name': 'Default',
        'hostport': 'localhost:2181,localhost:2182,localhost:2183',
        'rest_gateway': 'http://localhost:9998'
    }, {
      # ... and more clusters
    }
]

What is Hue?
------------

Wiki: http://wiki.github.com/cloudera/hue/
Main Repo: http://github.com/cloudera/hue 

Hue is both a web UI for Hadoop and a framework to create interactive web applications. It features a FileBrowser for accessing HDFS, JobSub and JobBrowser applications for submitting and viewing MapReduce jobs, a Beeswax application for interacting with Hive. On top of that, the web frontend is mostly built from declarative widgets that require no JavaScript and are easy to learn.

What is ZooKeeper?
------------------

http://zookeeper.apache.org/

ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them ,which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.

                     Zookeeper C client library 


This package provides a C client interface to Zookeeper server.

For the latest information about ZooKeeper, please visit our website at:
   http://zookeeper.apache.org/
and our wiki, at:
   https://cwiki.apache.org/confluence/display/ZOOKEEPER

Full documentation for this release can also be found in ../../docs/index.html


OVERVIEW

The client supports two types of APIs -- synchronous and asynchronous.

Asynchronous API provides non-blocking operations with completion callbacks and 
relies on the application to implement event multiplexing on its behalf.

On the other hand, Synchronous API provides a blocking flavor of
zookeeper operations and runs its own event loop in a separate thread.

Sync and Async APIs can be mixed and matched within the same application.

The package includes two shared libraries: zookeeper_st and
zookeeper_mt. The former only provides the Async API and is not
thread-safe. The only reason this library exists is to support the
platforms were pthread library is not available or unstable
(i.e. FreeBSD 4.x). In all other cases the application developers are
advised to link against zookeeper_mt as it includes support for both
Sync and Async API.


INSTALLATION

If you're building the client from a source checkout you need to
follow the steps outlined below. If you're building from a release
tar downloaded from Apache please skip to step 2.

1) do a "ant compile_jute" from the zookeeper top level directory (.../trunk).
   This will create a directory named "generated" under src/c.  Skip to step 3.
2) unzip/untar the source tarball and cd to the zookeeper-x.x.x/src/c directory
3) change directory to src/c and do a "autoreconf -if" to bootstrap
   autoconf, automake and libtool. Please make sure you have autoconf
   version 2.59 or greater installed. If cppunit is installed in a non-standard
   directory, you need to specify where to find cppunit.m4. For example, if
   cppunit is installed under /usr/local, run:
   
       ACLOCAL="aclocal -I /usr/local/share/aclocal" autoreconf -if

4) do a "./configure [OPTIONS]" to generate the makefile. See INSTALL
   for general information about running configure. Additionally, the
   configure supports the following options:
   --enable-debug     enables optimization and enables debug info compiler
                      options, disabled by default
   --without-syncapi  disables Sync API support; zookeeper_mt library won't
                      be built, enabled by default
   --disable-static   do not build static libraries, enabled by default
   --disable-shared   do not build shared libraries, enabled by default
   --without-cppunit  do not build the test library, enabled by default.

5) do a "make" or "make install" to build the libraries and install them. 
   Alternatively, you can also build and run a unit test suite (and
   you probably should).  Please make sure you have cppunit-1.10.x or
   higher installed before you execute step 4.  Once ./configure has
   finished, do a "make run-check". It will build the libraries, build
   the tests and run them.
6) to generate doxygen documentation do a "make doxygen-doc". All
   documentations will be placed to a new subfolder named docs. By
   default only HTML documentation is generated.  For information on
   other document formats please use "./configure --help"


USING THE CLIENT

You can test your client by running a zookeeper server (see
instructions on the project wiki page on how to run it) and connecting
to it using the zookeeper shell application cli that is built as part
of the installation procedure.

cli_mt (multithreaded, built against zookeeper_mt library) is shown in
this example, but you could also use cli_st (singlethreaded, built
against zookeeper_st library):

$ cli_mt zookeeper_host:9876

This is a client application that gives you a shell for executing
simple zookeeper commands. Once successfully started and connected to
the server it displays a shell prompt.

You can now enter zookeeper commands. For example, to create a node:

> create /my_new_node

To verify that the node's been created:

> ls /

You should see a list of nodes who are the children of the root node "/".

Here's a list of command supported by the cli shell:

ls <path>             -- list children of a znode identified by <path>. The
                         command set a children watch on the znode.
get <path>            -- get the value of a znode at <path>
set <path> <value>    -- set the value of a znode at <path> to <value>
create [+e|+s] <path> -- create a znode as a child of znode <path>; 
                         use +e option to create an ephemeral znode,
                         use +s option to create a znode with a sequence number 
                         appended to the name. The operation will fail if 
                         the parent znode (the one identified by <path>) doesn't
                         exist.
delete <path>         -- delete the znode at <path>. The command will fail if the znode
                         has children.
sync <path>           -- make sure all pending updates have been applied to znode at <path>
exists <path>         -- returns a result code indicating whether the znode at <path>
                         exists. The command also sets a znode watch.
myid                  -- prints out the current zookeeper session id.
quit                  -- exit the shell.

In order to be able to use the zookeeper API in your application you have to
1) remember to include the zookeeper header 
   #include <zookeeper/zookeeper.h>
2) use -DTHREADED compiler option to enable Sync API; in this case you should
   be linking your code against zookeeper_mt library

Please take a look at cli.c to understand how to use the two API types. 
(TODO: some kind of short tutorial would be helpful, I guess)
This is the base documentation directory.

skinconf.xml     # This file customizes Forrest for your project. In it, you
                 # tell forrest the project name, logo, copyright info, etc

sitemap.xmap     # Optional. This sitemap is consulted before all core sitemaps.
                 # See http://forrest.apache.org/docs/project-sitemap.html
The images in this directory are used if the current skin lacks them.
This directory contain scripts that allow easy access (classpath in particular)
to the ZooKeeper server and command line client.

Files ending in .sh are unix and cygwin compatible

Files ending in .cmd are msdos/windows compatible
