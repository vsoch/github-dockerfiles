Boundless Server
================

These instructions describe how to build platform independent components of Boundless Server.

## Prerequisites

The following base software packages are required.

* Java 8 - [Java Development Kit (JDK)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) - 1.8+ or [Open JDK](http://openjdk.java.net/install/)
* [Apache Ant](http://ant.apache.org/bindownload.cgi) - 1.8+
* [Git](http://git-scm.com/) - 1.7.10+*

Some modules require additional packages:

* [Apache Maven](http://maven.apache.org/download.html) - 3.0+
* [Python 2](https://www.python.org/downloads/)
* [JSTools](https://github.com/whitmo/jstools) - Latest
* [Sphinx](http://sphinx.pocoo.org/) - 1.0+ (the full build requires LaTeX support)
* [NodeJS](http://nodejs.org/) - Latest version
  * [Bower](http://bower.io/) - `npm install -g bower`
  * [Grunt](http://gruntjs.com/) - `npm install -g grunt-cli`
  * [Gulp](http://gulpjs.com/) - `npm install -g gulp`
* [GDAL](https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries) - 1.9.1 or newer, must include ogr2ogr

Ensure that all the above are installed so that the associated executables are on the 
`PATH` of the user building the server. 

## Developer Guide

If you just want to build server locally, and do not intend to contribute changes, you can skip this section and proceed to the [Quickstart](#quickstart).

### Getting Started

1. [Fork](https://guides.github.com/activities/forking/) the server projuct to your github account. This fork will be used to stage your changes.

1. Clone your fork of server in the desktop:

        % git clone git://github.com/<yourusername>/server.git server
        % cd server

1. Add an upstream remote pointing to the boundless server project:

        % git remote add upstream https://www.github.com/boundlessgeo/server.git server

1. This remote will be used to update your fork of server to the latest from the boundless suie repository. Any time you want to get the latest changes, simply pull from the upstream remote:

        % git pull upstream master

### Submodules

Server includes code from several other projects by way of [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Most server submodules are in [geoserver/externals](https://github.com/boundlessgeo/server/tree/master/geoserver/externals). Submodules function like a link to a specific revision of a project. When using git on the desktop, submodules behave like single files as long as you are outside of them. However, they can be traversed like directories and once inside a submodule, git behaves as if you are in a checkout of the submodule project itself. 

1. When inside a submodule, you can update the revision it links to by pulling from a remote. Many submodules link to a specific branch, so make sure you get the right one (ask a developer if you are unsure)!

        % cd geoserver/externals/geoserver
        % git pull origin 2.7.x

2. In order for this update to be reflected in the server project, it must be commited like any other change:

        % cd ../
        % git add geoserver
        % git commit -m "update geoserver submodule"

3. You can then push this change to your fork and create a pull request, like any other commit.

### Release Branches

During regular development, server changes are commited to the master branch. Prior to a release, a release branch (of the form `r4.7`) is created. Any changes should be made against that branch instead, and backported to master if necessary. 

1. When commiting a change to the release branch, note the commit id:

        [r4.7 0c66de5] update geoserver submodule

2. To backport this commit to master, switch to the master branch and use `cherry-pick` to copy the commit. Remember to push your change up to the server repository:

        % git checkout master
        % git cherry-pick 0c66de5
        % git push upstream master

Certain submodules (mainly geoserver) will also have release specific branches. If you are updating a submodule on the release branch, first check if it has its own branch for this release (usually of the form `server-4.7`). Ask a developer if you are unsure.

### What's next

To build Boundless Server, go to step 2 of the [Quickstart](#quickstart).

For more information about the build system, see the [Build System Overview](#build-system-overview).

For information on the individual components that comprise server, follow the links in the [Modules](#modules) section.

If you are preparing for a new release of Boundless Server, refer to the [Release Procedure](#release-procedure) section.

## Quickstart

1. Clone the repository:

        % git clone git://github.com/boundlessgeo/server.git server
        % cd server

1. Initialize submodule dependencies:

        % git submodule update --init --recursive

1. Do a full build:

        % ant

1. Or build the module of your choice:

        % cd docs
        % ant 

## Build System Overview

The server repository is made up a number of modules (ie projects). During development 
typically modules are built individually as opposed to all at once. The primary build 
tool for server is Ant. For some modules the ant script delegates to the modules native build tool such as Maven or Sphinx. 

All top level modules have a `build.xml` that defines the following targets:

1. `build` - Builds the project, the result of this is something deployable in the development environment. This target is the default.
1. `clean` - Cleans the project deleting all build artifacts. 
1. `assemble` - Assembles the project into a zip archive suitable for deployment in production. This is the artifact consumed by installer builders. 
1. `publish` - Publishes the zip archive to a final location.
1. `all` - Runs all the above targets.

Building for development purposes typically looks like:

    ant clean build

Building for deployment purposes typically looks like:

    ant clean build assemble

Or to build everything:

    ant all

The highest level build files simply delegate to the lower level build files. This means that performing a top level build and performing a build for a specific module will result in the same artifacts being produced for that module.

The [build](build) directory contains common build files used by modules.

 * [common.xml](build/common.xml) - Common ant targets used by module 
 build files. Every module build file imports this file as the first step.
 * [build.properties](build/build.properties) - Default build properties that can
 be overridden on a global or per module basis.
 * [build_properties.py](build/build_properties.py) - Used by the doc build to parse properties from [build.properties](build/build.properties) into the server build environment.

### Build Properties

Many aspects of the server build such as file locations, executable names, etc... are 
parameterized into build properties. The default [build.properties](build/build.properties)
contains a list of default values. Often these default properties must be overridden to 
cater to the environment (eg. Windows vs Unix) or to cater to specifics of a particular module. 

There are two ways to override build properties: 

1. The first is to specify them directly to the ant build command with the Java system property (-D) syntax. For example:

          % ant -Dserver.build_cat=release build

1. Creating a file named `local.properties` either at the global level or at the module level. The global `local.properties` is located in the [build](build) directory next to 
`build.properties`. Module specific `local.properties` files are located next to the module `build.xml` file. Naturally the module specific local properties file overrides properties from its global counterpart. 

Using any combination of the above method it should never be necessary to modify the `build.properties` file directly.

The build.properties file *should* be modified when development begins on a new server version, in order to update the appropriate version numbers and geoserver extensions.

### Release Procedure

When performing a new Server release, there are several changes that should be made in this repo to prepare for the release.

## Update Versions

In [build.properties](build/build.properties), update the following properties:

* `server.version` - This controls the version that is displayed on the Dashboard and in the Docs, and should be updated for every release.

If this release includes a change to the geoserver major version (For example, from 2.12 to 2.13), you also need to update the following properties:

* `gt.major_version`
* `gwc.major_version`
* `gs.major_version`

Additionally, you will need to update the GeoTools, GeoWebcache, and GeoServer versions in the following files:

* geoserver/webapp/pom.xml
* geowebcache/pom.xml


## Update Submodules

[Update any submodules](#submodules) that have changed since the last release. For a minor release, this is usually just [geotools](geoserver/geotools), [geowebcache](geoserver/geowebcache), and [geoserver](geoserver/geoserver). This should typically be updated to the latest commit in the stable branch.

For a major release, also be sure to update [geomesa](geoserver/externals/geomesa) and [geoserver-exts](geoserver/externals/geoserver-exts) to a version that supports the new geotools/geoserver major versions.

## Update Docs

Update the [What's new](docs/usermanual/source/whatsnew.rst) page with a short, user-friendly list of the highlights of the current release.

If there have been any changes in the packaging or install procedures, update the [installation instructions](docs/usermanual/source/install) accordingly. This is usually only necessary for major releases.

### Versioned build

To build server with a specific minor version assigned to geotools, geowebcache, and geoserver (instead of -SNAPSHOT), use the [build/versions.xml](build/versions.xml) ant script to set a custom version. For example, to build server 4.9-beta1:

        % ant -f build/versions.xml set-versions -Dserver.minor_version=-beta1
        % ant all -Dserver.minor_version=-beta1

To undo this action and reset te versions back to -SNAPSHOT:

       % git reset --hard HEAD
       % git submodule foreach --recursive git reset --hard

### Custom-building a GeoServer extension for Support

Occasionally, we will have to build (or re-build) an extension or jar after a server release has gone out.
I will be using Server 4.9.1 as the server version for the purposes of this example.

1. Checkout the correct server branch and update submodules:

        % git checkout r4.9.1
        % git submodule update --init --recursive

1. Set the server version for the geoserver artifacts:

        % ant -f build/versions.xml set-versions -Dserver.minor_version=-server-4.9.1

1. If you are building an extension that does not normally ship with server, modify `build/build.properties` and add that module to `gs.exts_core` or `gs.exts_comm` (depending upon whether or not it is a community module).

1. Change to the `geoserver` directory and run a build.

        % cd geoserver
        % ant clean build assemble -Dserver.minor_version=-server-4.9.1

1. The geoserver artifacts will be in `geoserver/geoserver/src/target/release`. The server war will be in `webapp/target`.

## Modules

The server repository is composed of the following modules:

* [composer](composer/README.md)
* [dashboard](dashboard/README.md)
* [docs](docs/README.md)
* [geoserver](geoserver/README.md)
* [geowebcache](geowebcache/README.md)
* [wpsbuilder](wpsbuilder/README.md)

Consult the module README files for module specific information.
