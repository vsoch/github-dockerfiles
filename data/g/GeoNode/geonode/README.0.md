This GeoNode contrib module was contributed by the MapStory project.

Function of the module:
Allow user to favorite content in Document, Layer, Map detail pages.
  - If user is not logged in, tell them to log in if want to use favorites.
  - If user is logged in, provide an 'Add Favorite' button, or a 'Delete Favorite' button.
Allow user to view a favorites list page with delete link for each.
Allow user to link to user favorites list page from each detail and user profile page and user modal list.

-----

To enable the module:
This contribution was initially contributed with hooks in the core GeoNode code so that enabling this module involved only one change in settings.py file.
Per GeoNode developer input, the core hooks have been removed and these instructions have been added.
It is up to the installing developer to add these to enable this module.

Steps to enable Favorites in GeoNode:

1. add the module to the geonode.settings.py file.

    # GeoNode Contrib Apps
    # 'geonode.contrib.dynamic',
    'geonode.contrib.favorite',

2. add Favorites urls to the geonode/urls.py.

    urlpatterns += patterns('',
                            (r'^favorite/', include('geonode.contrib.favorite.urls')),
                            )

3. to show Favorites on a detail page, make these additions to the View and the corresponding template files.

3a. template - add link to the Favorite tab on the 'tab switcher' on geonode/templates/_actions.html:
(this single change gets included on each detail pages)

    after GeoGig, approx ln 15, add:

    <li><a href="#favorite" data-toggle="tab"><i class="fa fa-star"></i>{% trans "Favorite" %}</a></li>

3b. view - add an import and a code block to <model>_detail method.  Using Map as example, geonode/maps/views.py:
(repeat 3b and 3c for each detail page)

    in imports:
    from geonode.contrib.favorite.utils import get_favorite_info

    in map_detail method:
    if request.user.is_authenticated():
        context_dict["favorite_info"] = get_favorite_info(request.user, map_obj)

3c. template - include the Favorite html and js.  Using Map as example, geonode/maps/templates/maps/map_detail.html: 

    after the social_links block for map (or after ratings block for document/map), add:

    <article class="tab-pane" id="favorite">
      {% include "favorite/_favorite.html" %}
    </article>

    in the {% block extra_script %}, add:

    {% include "favorite/_favorite_js.html" %}


4. Add link to Favorites list from user profile page, geonode/people/templates/people/profile_detail.html:

    after My Activities, approx ln 95, add:

    <ul class="list-group">
        <li class="list-group-item"><a href="{% url "favorite_list" %}"><i class="fa fa-star"></i> {% trans "Favorites" %}</a></li>
    </ul>


5. Add link to Favorites list from user modal, geonode/templates/base.html:

    after notifications, approx ln 216, add:

    <li><a href="{% url "favorite_list" %}"><i class="fa fa-star"></i> {% trans "Favorites" %}</a></li> 


6. Run migrate to create the new favorite_favorite table.# SPCgeonode [![CircleCI](https://circleci.com/gh/olivierdalang/geonode.svg?style=svg)](https://circleci.com/gh/olivierdalang/geonode)

SPCgeonode is a setup for Geonode deployement at SPC. It makes it easy to deploy a production ready Geonode. The setup aims for simplicity over flexibility, so that it will only apply for typical small scale Geonode installations.

The setup is also usable for Geonode developement or customization.


## Prerequisites

Make sure you have a version of Docker (tested with 17.12) and docker-compose.

- Linux : https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-from-a-package and https://docs.docker.com/compose/install/#install-compose 
- Windows : https://store.docker.com/editions/community/docker-ce-desktop-windows
- Mac : https://store.docker.com/editions/community/docker-ce-desktop-mac

## Usage

All the following commands happen from this folder :

```
cd /path/to/geonode/scripts/spcgeonode
```

### Development

To start only the main services (should be enough for developement) :
```
docker-compose up --build -d django geoserver postgres nginx
```

To start the whole stack :
```
docker-compose up --build -d
```

If not familiar with Docker, read below to know how to see what's happening. On first start, the containers will restart serveral times. Once everything started, you should be able to open http://127.0.0.1 in your browser. See how to edit the configuration below if you install on another computer.

### Production (using composer)

Using a text editor, edit the `.env` file (you can also override those with environment variables) :
```
# General configuration
nano .env
```

When ready, start the stack using this commands :
```
# Run the stack
docker-compose -f docker-compose.yml up -d --build
```

Alternatively, you can pull the images from dockerhub instead of rebuilding (only applies if you haven't changed the docker setup) :
```
# Pull the images and run the stack
docker-compose -f docker-compose.yml pull
docker-compose -f docker-compose.yml up -d
```

If not familiar with Docker, read below to know how to see what's happening. On first start, the containers will restart serveral times. Once everything started, you should be able to open http://your_http_host or https://your_https_host in your browser.

### Upgrade

If at some point you want to update the SPCgeonode setup (this will work only if you didn't do modifications, if you did, you need to merge them) :
```
# Get the update setup
git pull

# Upgrade the stack
docker-compose -f docker-compose.yml up -d --build
```

### Developpement vs Production

Difference of dev setup vs prod setup:

- Django source is mounted on the host and uwsgi does live reload (so that edits to the python code is reloaded live)
- Django static and media folder, Geoserver's data folder and Certificates folder are mounted on the host (just to easily see what's happening)
- Django debug is set to True
- Postgres's port 5432 is exposed (to allow debugging using pgadmin)
- Nginx debug mode is acticated (not really sure what this changes)
- Docker tags are set to dev instead of latest

### Releases


To make a release :

- checkout spcgeonode-release
- merge spcgeonode
- replace the version tag in docker-compose.yml with the version (format `x.x.x`)
- commit
- create a git tag (format `spc/x.x.x`)
- push spcgeonode-release with tags

This will trigger an automatic build on docker hub.

If you need to manually publish the image (e.g. dockerhub build fail) :

```
docker login
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml push
```

## FAQ

### Docker-primer - How to see what's happening ?

If not familiar with Docker, here are some useful commands :

- `docker ps` : list all containers and their status
- `docker-compose logs -f` : show live stdout from all containers
- `docker-compose logs -f django` : show live stdout from a specific container (replace `django` by `geoserver`, `postgres`, etc.)
- `docker-compose down -v` : brings the stack down including volumes, allowing you to restart from scratch **THIS WILL ERASE ALL DATA !!**

### During startup, a lot of container crash and restart, is it normal ?

This is the normal startup process. Due to the nature of the setup, the containers are very interdependant. Startup from scratch can take approx. 5-10 minutes, during which all containers may restart a lot of times.

In short, Django will restart until Postgres is up so it can migrate the database. Geoserver will restart until Django has configured OAuth so it can get OAuth2 configuration. Django will restart until Geoserver is running so it can reinitialize the master password.

### Backups

*Backups* are made using [RClone](https://rclone.org/docs/). RClone is a flexible file syncing tool that supports all commons cloud provider, regular file transfer protocols as well as local filesystem. It should be able to accomodate almost any setup.

The only available configuration provided with the setup assumes Amazon S3 is being used, in which case you need to replace the following parts of the `rclone.backup.config` file : `YOUR_S3_ACCESS_KEY_HERE`,`YOUR_S3_SECRET_KEY_HERE`,`YOUR_S3_REGION_HERE` and `THE_NAME_OF_YOUR_BUCKET_HERE` (watch [this](https://www.youtube.com/watch?v=BLTy2tQXQLY) to learn how to get these keys).

Also consider enabling *versionning* on the Bucket, so that if data won't get lost if deleted accidentally in GeoNode.

If you want to setup backups using another provider, check the [RClone documentation](https://rclone.org/docs/). It should be easy to add any RClone supported provider to SPCgeonode.

### How to migrate from an existing standard Geonode install

This section lists the steps done to migrate from an apt-get install of Geonode 2.4.1 (with Geoserver 2.7.4) to a fresh SPCGeonode 0.1 install. It is meant as a guide only as some steps may need some tweaking depending on your installation. Do not follow these steps if you don't understand what you're doing.

#### Prerequisites

- access to the original server
- a new server for the install (can be the same than the first one if you don’t fear losing all data) - ideally linux but should be OK as long as it runs docker (64bits)
- an external hard-drive to copy data over

#### On the old server

```
# Move to the external hard drive
cd /path/to/your/external/drive

# Find the current database password (look for DATABASE_PASSWORD, in my case it was XbFAyE4w)
more /etc/geonode/local_settings.py

# Dump the database content (you will be prompted several time for the password above)
pg_dumpall --host=127.0.0.1 --username=geonode --file=pg_dumpall.custom

# Copy all uploaded files
cp -r /var/www/geonode/uploaded uploaded

# Copy geoserver data directory
cp -r /usr/share/geoserver/data geodatadir
```

#### On the new server

Setup SPCGeonode by following the prerequisite and production steps on https://github.com/olivierdalang/SPCgeonode/tree/release up to (but not including) run the stack.

Then run these commands :

```
# Prepare the stack (without running)
docker-compose -f docker-compose.yml pull --no-parallel
docker-compose -f docker-compose.yml up --no-start

# Start the database
docker-compose -f docker-compose.yml up -d postgres

# Initialize geoserver (to create the geodatadir)
docker-compose -f docker-compose.yml run --rm geoserver true

# Go to the external drive
cd /path/to/drive/

# Restore the dump (this can take a while if you have data in postgres)
cat pg_dumpall.custom | docker exec -i spcgeonode_postgres_1 psql -U postgres
# Rename the database to postgres
docker exec -i spcgeonode_postgres_1 dropdb -U postgres postgres
docker exec -i spcgeonode_postgres_1 psql -d template1 -U postgres -c "ALTER DATABASE geonode RENAME TO postgres;"

# Restore the django uploaded files
docker cp uploaded/. spcgeonode_django_1:/spcgeonode-media/

# Restore the workspaces and styles of the geoserver data directory
docker cp geodatadir/styles/. spcgeonode_geoserver_1:/spcgeonode-geodatadir/styles
docker cp geodatadir/workspaces/. spcgeonode_geoserver_1:/spcgeonode-geodatadir/workspaces
docker cp geodatadir/data/. spcgeonode_geoserver_1:/spcgeonode-geodatadir/data

# Back to SPCgeonode
cd /path/to/SPCgeonode

# Fix some inconsistency that prevents migrations (public.layers_layer shouldn’t have service_id column)
docker exec -i spcgeonode_postgres_1 psql -U postgres -c "ALTER TABLE public.layers_layer DROP COLUMN service_id;"

# Migrate with fake initial
docker-compose -f docker-compose.yml run --rm --entrypoint "python manage.py migrate --fake-initial" django

# Create the SQL diff to fix the schema # TODO : upstream some changes to django-extensions for this to work directly
docker-compose -f docker-compose.yml run --rm --entrypoint '/bin/sh -c "DJANGO_COLORS=nocolor python manage.py sqldiff -ae"' django >> fix.sql

# Manually fix the SQL command until it runs (you can also drop the tables that have no model)
nano fix.sql

# Apply the SQL diff (review the sql file first as this may delete some important tables)
cat fix.sql | docker exec -i spcgeonode_postgres_1 psql -U postgres

# Set all layers as approved
docker exec -i spcgeonode_postgres_1 psql -U postgres -c 'UPDATE base_resourcebase SET is_approved = TRUE;'

# This time start the stack
docker-compose -f docker-compose.yml up -d
```

One last step was to connect to the GeoServer administration and change the PostGIS store host, user and password to 'postgres'.

### On windows, I have error like `standard_init_linux.go:190: exec user process caused "no such file or directory"`

This may be due to line endings. When checking out files, git optionnaly converts line endings to match the platform, which doesn't work well it `.sh` files.

To fix, use `git config --global core.autocrlf false` and checkout again.
# Letsencrypt service for SPCGeonode

This service generates SSL certificates to be used by Nginx.

## Let's Encrypt

Upon startup, it generates one SSL certificate from Let's Encrypt using Certbot. It then starts cron (in foreground) to renew the certificates using Certbot renew.

If for some reason getting the certificate fails, a placeholder certificate is generated. This certificate is invalid, but still allows to encrypt the data and to start the webserver.

To avoid hitting Let's Encrypt very low rate limits when developping or doing tests, LETSENCRYPT_MODE env var can be set to "disabled" (which will completely bypass Let'sEncrypt, simulating a failure) or to "staging" (using Let'sEncrypt test certificates with higher rates).

## Autoissued

An auto-issued certificate is also generate to be used on the LAN if needed. It is also renewed every now and then using the same cron process than above.
=========
GeoNode Cloud Scripts
=========

Summary
==================
GeoNode Admin is a set of scripts for launching GeoNode instances on ec2 or other cloud infrastructure.

Requirements
==================
* aws (http://aws.amazon.com/)
 - download geonode.pem from web interface
 - export AWS_ACCESS_KEY_ID='blahblah'
 - export AWS_SECRET_ACCESS_KEY='blebleble'
* boto (http://code.google.com/p/boto/)
 - easy_install boto 
* fabric (http://docs.fabfile.org/0.9.3/)
 - easy_install fabric

Usage 
==================
* ec2.py launch
* fab -i geonode.pem -H user@host geonode_dev
* fab -i geonode.pem -H user@host geonode_prod
* fab -i geonode.pem -H user@host update 
Installing GeoNode
==================

The easiest way to install GeoNode is using the official packages for one of the supported Operating Systems.
Please be advised that GeoNode requires at least 4GB of RAM (6GB including swap).

Ubuntu 12.04 
-----------------------------

Open a terminal and run the following commands::

    sudo add-apt-repository ppa:geonode/testing
    sudo apt-get update
    sudo apt-get install geonode


OSX, Windows and other operating systems
----------------------------------------

Our recommendation is to use a Virtual Machine with one of the supported Operating Systems.
If that is not an option then you could try to follow manually the steps of the install script
adjusting for paths and commands in your OS.

Manual installation
-------------------

This is mostly targeted to Linux based distributions,
it has only been tested in Ubuntu Linux but should work with minimal changes to the config file.

# First you need to install the OS specific dependencies,
here is the complete list (the actual package name may vary)::

    geoserver, python, python-support, python-dev, sun-java6-jre | openjdk-6-jre, tomcat6, postgresql-9.3, gcc, patch, zip,  python-imaging, gdal-bin, libgeos-dev, python-urlgrabber, python-pastescript, gettext, postgresql-contrib, postgresql-9.3-postgis-2.1,libpq-dev, unzip, libjpeg-dev, libpng-dev, python-gdal, libproj-dev, python-psycopg2, apache2, libapache2-mod-wsgi, libxml2-dev, libxslt1-dev

# Then you have to edit the config file that is in the support directory with the appropiate paths,
sample config files for Ubuntu and CentOS are distributed with the release packages.

# After that, open a terminal and run the following command as a super user::

    ./install.sh support/config.sh

# To test your GeoNode installation simply type the following in your terminal::

    geonode help

  You should also navigate to your browser window and type `http://localhost/`

# After you have installing your GeoNode we recommend you to read the following guide to learn how to create users,
serve the site on a DNS or IP address and optimize your GeoNode.
    http://docs.geonode.org/deploy/production.html 

Note for packagers
~~~~~~~~~~~~~~~~~~

There is an advanced flag for the install script called 'step'.
There are two main steps to install GeoNode,
the first one is to place the required files in the right places (referred to as pre-install) and
the other to create the postgis database and edit the required Django, GeoServer and Geonetwork config files (referred to as post-install).

By default the install script does both, but usually it is appropriate to perform the first of these steps during package creation and the second one at install time.

The step flag supports three values: 'pre', 'post' and 'all'. Default is 'all'. Here is usage example::

    # in debian/rules#install
    ./install.sh -s pre support/config.sh

    # in debian/postinst
    ./install.sh -s post support/config.sh


GPL License
===========

GeoNode is Copyright 2016 Open Source Geospatial Foundation (OSGeo).

GeoNode is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

GeoNode is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with GeoNode.  If not, see <http://www.gnu.org/licenses/>.
CentOS packaging scripts for GeoNode
====================================

This repository contains the scripts used to build the .rpm (CentOS) package
for GeoNode.  If you are interested in modifying GeoNode itself you may find
http://github.com/GeoNode/geonode more relevant.

Building
--------

To produce a .rpm package which can be redistributed:

* Install the rpm packaging tools::

    yum install rpmbuild rpm-devtools

* Run the rpmdev-setuptree tool to set up your user account for building RPMs::

    rpmdev-setuptree

* Point the BUILD and SPECS subdirectories of the RPM build tree at your
  checkout of this project::

    rmdir ~/rpmbuild/{BUILD,SPECS} &&
    ln -s ~/geonode-rpm/{BUILD,SPECS} ~/rpmbuild/

* Acquire a GeoNode tar.gz archive (by either building it from sources, or from
  http://dev.geonode.org/release/ ) and unpack it into
  :file:`geonode-rpm/BUILD/`.

* Fetch the psycopg2 sources from http://initd.org/psycopg/download/ and place
  the tarball in :file:`geonode-rpm/BUILD/deps`.

* You should now have a directory structure like so::

    geonode-rpm/
      + BUILD/
        + GeoNode-{version}/
        + deps/
          - psycopg2-2.3.1.tar.gz
        + scripts/
      + SPECS/
        - geonode.spec
        - opengeo.repo

* Now you can build the GeoNode RPM by using the ``rpmbuild`` command::

    rpmbuild -bb ~/rpmbuild/SPECS/geonode.spec

.. note::

    Currently, building on CentOS machines requires specifying the --buildroot
    option to rpmbuild, like so::

        rpmbuild -bb ~/rpmbuild/SPECS/geonode.spec \
          --buildroot=/home/rpmbuild/rpmbuild/BUILDROOT/

After running ``rpmbuild`` you should have the RPM package one directory level
in the :file:`rpmbuild` directory.

Installation
------------

As described in the GeoNode manual, you can access OpenGeo's YUM repository to
get pre-built GeoNode packages.  However, if you want to build a package and
install that instead, you can avoid the need for a repository of your own by
using the following command::

    yum localinstall geonode-{version}.rpm --nogpgcheck

As GeoNode depends on software not provided by the main CentOS distribution,
you will still need to enable some third-party repositories.  OpenGeo's
repository will mirror all GeoNode dependencies, or you can use
`EPEL<http://fedoraproject.org/wiki/EPEL>`_ and
`ELGIS<http://wiki.osgeo.org/wiki/Enterprise_Linux_GIS>`_ together.
To build the debian package, you need to do the following.

1. Download geoserver.war from the build server
2. Rename the war to zip and unzip in target/geoserver
3. Update debian/changelog with the new version
4. Run debuild -S -k<your-gpg-key-id>
5. dput ppa:geonode/testing ../geoserver-geonode*.sources
Debian packaging scripts for GeoNode
====================================

This repository contains the scripts used to build the .deb (Ubuntu) package
for GeoNode.  If you are interested in modifying GeoNode itself you may find
http://github.com/GeoNode/geonode more relevant.

Building
--------

To produce a .deb package which can be redistributed:

* Install the debian packaging tools::

    apt-get install debhelper devscripts

* Acquire a GeoNode tar.gz archive (by either building it from sources, or from
  http://dev.geonode.org/release/ ) and unpack it, so that you have a
  directory structure like so::
 
    geonode-deb/
       + debian/
       + GeoNode-{version}

* Run the debuild tool to build the package::

    debuild -uc -us -A

* geonode-{version}.deb will be produced in the parent directory (one level
  above the directory where you cloned this project).

Installation
------------

As described in the GeoNode manual, you can access OpenGeo's APT repository to
get pre-built GeoNode packages.  However, if you want to build a package and
install that instead, you can avoid the need for a repository of your own by
using the following command::

    dpkg -i geonode-{version}.deb

If dpkg reports an error about unmet dependencies, you can issue the following
command to fetch dependencies and re-attempt the installation::

    apt-get install -f

The Debian Package geonode
----------------------------

Comments regarding the Package

 -- root <root@thatserver.ca>  Thu, 04 Nov 2010 14:49:39 -0700
.. image:: https://coveralls.io/repos/github/GeoNode/geonode/badge.svg?branch=master
    :alt: Coverage Badge
    :target: https://coveralls.io/github/GeoNode/geonode?branch=master

.. image:: https://codecov.io/gh/GeoNode/geonode/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/GeoNode/geonode

.. image:: https://secure.travis-ci.org/GeoNode/geonode.png
    :alt: Build Status
    :target: http://travis-ci.org/GeoNode/geonode


GeoNode Support
===============

To get support, give feedback and suggestions please use the GeoNode official channels, the users mailing list: http://lists.osgeo.org/pipermail/geonode-users/ and the developers mailing list: http://lists.osgeo.org/pipermail/geonode-devel/.

This repository is used to track code changes and GeoNode issues, please DON'T open new issues to ask for support.


GeoNode Installation
====================

If you just want to try GeoNode, it is recommended to use Ubuntu 14.04 and install the latest stable release of GeoNode.::

    sudo add-apt-repository ppa:geonode/stable
    sudo apt-get update
    sudo apt-get install geonode

If instead, you are interested in doing development on the source code, here are the instructions: http://docs.geonode.org/en/master/tutorials/devel/devel_env/index.html

Development Installations
=========================

Docker Usage
------------

If you want to use Docker you can now::

    # build the docker container
    docker-compose build

    # run the docker container
    docker-compose up -f docker-compose.yml -f docker-compose.override.localhost.yml -d

    # turn it off
    docker-compose down

Or if you want to use the provided Makefile::

    # build the container
    make build

    # run the container
    make up

    # create database
    make sync

    # pull latest images
    make pull

    # complete development setup
    make develop

.. note:: For development you need to add ``geonode`` alias into ``/etc/hosts/`` file as following::

        $ sudo vim /etc/hosts
        ##
        # Host Database
        #
        # localhost is used to configure the loopback interface
        # when the system is booting.  Do not change this entry.
        ##
        127.0.0.1       localhost geonode
        255.255.255.255 broadcasthost
        ::1             localhost

To access GeoNode just enter the following url: http://geonode/ on your web browser.
For GeoServer: http://geonode/geoserver/web/

Ubuntu
------

Ubuntu development build instructions using an isolated virtual environment (tested on Ubuntu 16.04 LTS)::

    # Install Ubuntu dependencies
    sudo apt-get update
    sudo apt-get install python-virtualenv python-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev libpq-dev libgdal-dev git default-jdk

    # Install Java 8 (needed by latest GeoServer 2.9)
    sudo apt-add-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer

    # Create and activate the virtualenv
    virtualenv --no-site-packages venv
    source venv/bin/activate

    # git clone geonode
    git clone https://github.com/GeoNode/geonode
    cd geonode

    # Install pip dependencies
    pip install -r requirements.txt --upgrade
    pip install -e . --upgrade --no-cache
    pip install pygdal==1.11.3.3

For Ubuntu 16.04 you should create your virtual-env like this instead (so with site packages)::

    virtualenv venv

Instead of installing pygdal, you should do the following::

    # Install the system python-gdal
    sudo apt-get install python-gdal
    # Create a symbolic link in your virtualenv
    ln -s /usr/lib/python2.7/dist-packages/osgeo venv/lib/python2.7/site-packages/osgeo

You can now setup and start GeoNode::

    # Paver setup
    paver setup
    paver sync
    paver start

In case you want to be involved in static files development::

    sudo apt-get install npm
    sudo npm install -g bower
    sudo npm install -g grunt-cli


openSUSE
--------

openSUSE Development Build Instructions::

    # Add Application:Geo and Python repositories
    zypper -ar http://download.opensuse.org/repositories/Application:/Geo/openSUSE_12.2/ GEO
    zypper -ar http://download.opensuse.org/repositories/devel:/languages:/python/openSUSE_12.1/ python
    zypper refresh

    # Basic build packages
    zypper install gcc gcc-c++ python-devel libgeos-devel libproj-devel

    # Python native dependencies
    zypper install python-pip python-virtualenv python-imaging python-lxml python-gdal

    # Java dependencies
    zypper install java-1_7_0_openjdk-devel ant maven

    # Supporting tools
    zypper install git gettext-runtime

    # Create virtualenv and activate it
    virtualenv venv --system-site-packages
    source venv/bin/activate
    cd venv

    # Clone GeoNode
    git clone https://github.com/GeoNode/geonode.git

    # Install GeoNode in the local virtualenv
    pip install -e geonode --use-mirrors

    cd geonode

    # Compile GeoServer
    paver setup

    # Initialize database
    paver sync

    # Start the servers
    paver start

Windows
-------

Windows Development Build Instructions::


    Prerequisites:
    # Java JDK
    # Python 2.7 (32 bit)
    # ant (bin directory must be on system PATH)
    # maven2 (bin directory must be on system PATH)
    # Python distutils (easy_install)
    # GDAL Core Libraries
    # git

    # Install and configure from the windows command prompt
    If you don't already have python virtualenv installed, then do it now:
    easy_install virtualenv

    # Download and install http://download.gisinternals.com/sdk/downloads/release-1800-gdal-1-11-4-mapserver-6-4-3/gdal-111-1800-core.msi
    # Download and install http://download.gisinternals.com/sdk/downloads/release-1800-gdal-1-11-4-mapserver-6-4-3/GDAL-1.11.4.win32-py2.7.msi
    # Choose your 32 bit python as your install target
    # If you create your virtualenv before doing this, you can copy the <python>\lib\site-packages\osgeo and GDAL-* directory over to your <virtual env>\lib\site-packages directory

    # Create virtualenv and activate it
    cd <Directory to install the virtualenv & geonode into>
    virtualenv venv
    venv\scripts\activate

    # Clone GeoNode
    git clone https://github.com/GeoNode/geonode.git

    # Install compiled packages for Python 2.7 Win32
    cd geonode
    pip install paver
    pip install pyyaml
    paver win_install_deps

    # Install GeoNode in the local virtualenv, if you get an error about use-mirrors, just remove the argument
    pip install -e . --use-mirrors

    # Note, you may get errors due to certain dependencies not being installable on windows with pip, such as lxml and shapely.
    # For these, you can download a whl file (use cp27 / win32 version) from http://www.lfd.uci.edu/~gohlke/pythonlibs and then install them via pip.
    # Ex: pip install <Download Dir>\Shapely-1.5-16-cp27-cp27m-win32.whl
    #
    # Also note, you may have to adjust the dependencies in geonode\setup.py to say >= instead of ==,
    # ie "Shapely>=1.5.13", instead of "Shapely==1.5.13",

    # Compile GeoServer
    paver setup

    # Set GDAL environment info
    SET GDAL_LIBRARY_PATH=<GdalPath>\gdal111.dll
    SET GDAL_HOME=<GdalPath>
    SET GEOS_LIBRARY_PATH=<GdalPath>\geos_c.dll
    SET PATH=<GdalPath>;%PATH%

    # Initialize database
    paver sync

    # Start the servers
    paver start --java_path=C:/path/to/java/bin/java.exe



Mac OSX
-------

Mac OSX Development Build Instructions::

    # you may need brew install various dependencies

    mkdir -p ~/pyenv
    virtualenv ~/pyenv/geonode
    source ~/pyenv/geonode/bin/activate
    git clone https://github.com/GeoNode/geonode
    cd geonode
    pip install lxml
    pip install pyproj
    pip install nose
    pip install httplib2
    pip install shapely
    pip install pillow
    pip install paver

    # Node and tools required for static development
    brew install node
    npm install -g bower
    npm install -g grunt-cli

    #Install pip dependencies
    pip install -e . --upgrade --no-cache

    #Paver handles dependencies for Geonode, first setup (this will download and update your python dependencies - ensure you're in a virtualenv)
    paver setup
    paver sync
    paver start

    # Optional: To generate document thumbnails for PDFs and other ghostscripts file types
    # Then download ghostscript: https://www.macupdate.com/app/mac/9980/gpl-ghostscript
    brew install imagemagick
    pip install Wand==0.3.5

Once fully started, you should see a message indicating the address of your geonode.
The default username and password are ``admin`` and ``admin``::

  Development Geonode is running at http://localhost:8000/
  To stop the GeoNode machine run:
  paver stop

  Or quit the server by pressing
  CTRL-C to shut down

Before starting GeoNode (paver start), you could test your installation by running tests::

    paver test
    paver test_integration

In case you want to build yourself the documentation, you need to install Sphinx and the run 'make html' from within the docs directory::

    pip install Sphinx
    pip install sphinx_rtd_theme
    cd docs
    make html

You can eventually generate a pdf containing the whole documentation set. For this purpose, if using Ubuntu you will need to install the texlive-full package::

    sudo apt-get install texlive-full
    make latexpdf

.. note::

  When running ``virtualenv venv`` the ``--system-site-packages`` option is
  not required.  If not enabled, the bootstrap script will sandbox your virtual
  environment from any packages that are installed in the system, useful if
  you have incompatible versions of libraries such as Django installed
  system-wide.  On the other hand, most of the times it is useful to use a version of
  the Python Imaging Library provided by your operating system
  vendor, or packaged other than on PyPI.  When in doubt, however, just leave
  this option out.

Development Roadmap
===================

Geonode's development roadmap is documented in a series of Geonode Improvement Projects (GNIPS).
They are documented here: https://github.com/GeoNode/geonode/wiki/GeoNode-Improvement-Proposals.
GNIPS are considered to be large undertakings which will add a large amount of features to the project.
As such they are the topic of community dicussion and guidance.
The community discusses these on the developer mailing list: http://lists.osgeo.org/pipermail/geonode-devel/
Github issues tracks features and bugs, for new developers the tag 'easy-pick' indicates an
issue that should be relatively easy for new developers to understand and complete. Once you have completed an issue
a pull request should be submitted. This will then be reviewed by the community.

GPL License
===========

GeoNode is Copyright 2016 Open Source Geospatial Foundation (OSGeo).

GeoNode is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

GeoNode is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with GeoNode.  If not, see <http://www.gnu.org/licenses/>.
===============================
GeoSites: Multi-Tenancy GeoNode
===============================

GeoSites is a contrib module to GeoNode starting with 2.4. The GeoSites app is a way to run multiple websites with a single instance of GeoNode. Each GeoSite can have different templates, applications, and data permissions but share a single database, web mapping service (GeoServer), and CSW (pycsw).  This is useful when multiple websites are desired to support different sets of users, but with a similar set of data and overall look and feel of the sites.  Users can be given permission to access multiple sites if needed, which also allows administrative groups can be set up to support all sites with one account.

A GeoSites installation uses a 'master' GeoNode website that has access to all users, groups, and data. Through the Django admin page, Layers, Maps, Documents, Users, and Groups can be added and removed from all sites.  Users can be given access to any number of sites, and data may appear on only a single site, or all of them.  The master site need not be accessible from the outside so that it can be used as an internal tool to the organization. Users created on a site are created with access to just that site (but not the master site).  Data uploaded to a site is given permission on that site as well as the master site.


GeoSites Contrib App
============================

The GeoSites contrib app makes full use of the Django Site framework to separate the content between different GeoNode sites.
The Association of a resource to a site is done through a OneToMany table named “SiteResources” (a record for each site).
The table has two fields:
* site: a one to one relation with the Django Site
* resources: a many to many relation to the GeoNode ResourceBase model

This table is used by GeoSites to filter the resources per site. GeoSites also overrides all GeoNode data related endpoints (e.g., APIs, detail page, faceting facilities) to provide full multiple site support. Signals (post_save, post_delete) are used to ensure that when a Resource (layer, map, document) is saved (or deleted) it is added (or removed) to the SiteResource entry for the current site and for the Master site.


GeoSites Project
============================
A GeoSites project looks similar to a normal GeoNode project, but with additional folders for sites, and more settings files. In the project there is a directory for each site: 'master' and 'site2' in the example listing below. Each site folder contains a settings file (and optionally local_settings) with site specific settings, as well as directories for static files and Django templates. In addition are configuration files necessary to serve the site: nginx, gunicorn, and wsgi.py. GeoSites works via a hierarchy: first default GeoNode, then GeoSites settings, then project settings, then site specific settings. This hierachy is used for settings, templates, and static files.

The project_name folder contains common settings in the pre_settings.py, post_settings.py, and optionally local_settings.py files.  There is also a sites.json file, which is a JSON file of the sites database table.  This is for convenience, as the file will contain the site IDs and names for all currently enabled sites.  The urls file is a common urls file, although each site could have their own urls file if needed (by creating one and setting it in the site specific settings file).

The top level directory contains two manage scripts, and a typical setup script. The familiar manage.py is a regular Django manage file that uses the master site for the settings file. This is the command that should be used when doing many tasks such as inspecting the database, creating a super-user, or adding a new site.  The manage_all.py script is when a command should be run on all sites, migrate and collectstatic being the common ones.  The migrate command will call sync the DB to the settings file of each site, while collectstatic will loop through the sites and collect the static files of all sites in the common location they are served from.

~~~
geosites-project
├── project_name
│   ├── __init__.py
│   ├── local_settings.py
│   ├── master
│   │   ├── conf
│   │   │   ├── gunicorn
│   │   │   └── nginx
│   │   ├── __init__.py
│   │   ├── local_settings.py
│   │   ├── settings.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── site_base.css
│   │   │   ├── img
│   │   │   │   └── README
│   │   │   ├── js
│   │   │   │   └── README
│   │   │   └── README
│   │   ├── templates
│   │   │   ├── site_base.html
│   │   │   ├── site_index.html
│   │   └── wsgi.py
│   ├── post_settings.py
│   ├── pre_settings.py
│   ├── site2
│   │   ├── conf
│   │   │   ├── gunicorn
│   │   │   └── nginx
│   │   ├── __init__.py
│   │   ├── local_settings.py
│   │   ├── settings.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── site_base.css
│   │   │   ├── img
│   │   │   │   └── README
│   │   │   ├── js
│   │   │   │   └── README
│   │   │   └── README
│   │   ├── templates
│   │   │   ├── site_base.html
│   │   │   ├── site_index.html
│   │   └── wsgi.py
│   ├── sites.json
│   └── urls.py
├── manage_all.py
├── manage.py
├── README.rst
└── setup.py
~~~

Settings
============================
Site settings are managed through the use of common settings files as well as site specific settings files.   A simple site settings file looks like this:

~~~
import os
from geonode.contrib import geosites

# Read in GeoSites pre_settings
GEOSITES_ROOT = os.path.dirname(geosites.__file__)
execfile(os.path.join(GEOSITES_ROOT, 'pre_settings.py'))

# Site specific variables
SITE_ID = $SITE_ID
SITE_NAME = '$SITE_NAME'
SECRET_KEY = "fbk3CC3N6jt1AU9mGIcI"
SITE_APPS = ()
SITE_DATABASES = {}

# Overrides - common settings that might be overridden for site

# urls for all sites
# ROOT_URLCONF = 'projectname.urls'

# admin email
# THEME_ACCOUNT_CONTACT_EMAIL = ''

# Have GeoServer use this database for this site
# DATASTORE = ''

# Allow users to register
# REGISTRATION_OPEN = True

# Read in GeoSites post_settings
execfile(os.path.join(GEOSITES_ROOT, 'post_settings.py'))
~~~

This settings file first reads in the GeoSites pre_settings.py file, which in turns reads in the default GeoNode settings then overrides some of the values.  Then, site specific variables are set: the site ID, name, and secret key.  SITE_APPS are additional apps that should be added to this site, while SITE_DATABASES is used when a site should be using a separate database (such as for a datastore of geospatial data separate from other sites).  In this case add a geospatial DB to the SITE_DATABASES dictionary (or in the local_settings, see below), then set DATASTORE to the key of that database.

While Django apps on other sites are not automatically added, for single site administration they can be added to the master site through the master site settings.py file. 


##### Local Settings

Databases are usually set in a local_settings file, as are other production settings.  The local_settings file in the project directory is used by all sites, so it is here where the database is set for all sites.

~~~
# path for static and uploaded files
# SERVE_PATH = ''

"""
DATABASES = {
    'default' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
    # vector datastore for uploads
    # 'datastore' : {
    #    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #    'NAME': '',
    #    'USER' : '',
    #    'PASSWORD' : '',
    #    'HOST' : '',
    #    'PORT' : '',
    # }
}
"""

GEOSERVER_URL = 'http://localhost:8080/'
~~~

SERVE_PATH is the path used for serving of static files for all sites (it is also where webserver logs will be put). DATABASES are any production databases used by all sites. In the example above there is a database for the Django database, and another used for storing geospatial vector data served by GeoServer.  The GEOSERVER_URL is the internal URL (not the reverse proxy URL) of GeoServer, localhost port 8080 if running on the same machine.

Specific sites must also have a local_settings file in production environments.  This sets the SITEURL, as well as fixes the location of GeoServer for production.

~~~
import os

# Outside URL
SITEURL = 'http://$DOMAIN'

# databases unique to site if not defined in site settings
"""
SITE_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, '../development.db'),
    },
}
"""
~~~


Web and Application Servers
=====================
Created GeoSites have configuration files for nginx (as the web server) and gunicorn (as the application server).  While Apache config files (with mod_wsgi as the application server) are not currently genererated, Apache supports the same configuration necessary for GeoSites to work.

A single GeoServer instance is used to serve data to all of the GeoSites.  Each site proxies the /geoserver URL to the internal address of GeoServer.  The default GeoNode installation sets the URL of the GeoNode site in one of the GeoServer config files: GEOSERVER_DATA_DIR/security/auth/geonodeAuthProvider/config.xml  Change the baseUrl field to an empty string:

    <baseUrl></baseUrl>

When baseUrl is empty, GeoServer will attempt to authenticate against the requesting URL.  Since a reverse proxy to GeoServer is configured on the web servers the requesting URL can be used to determine the URL to GeoNode.

Databases
=====================
The master site, and all of the individual GeoSites, share a single database in a normal GeoSites setup. Objects, including users, groups, and data layers, all appear within the database but an additional sites table indicates which objects have access to which sites.  The geospatial data served by GeoServer (e.g., from PostGIS) can exist in the database like normal, since GeoServer will authenticate against the correct site, which will use it's database to determine permissions based on the object, current user, and site.


#### Adding New Sites

A management command exists to easily create a new site.  This will create all the needed directories, as well as a site specific settings file.  The command may also create a website configuration file.

    $ python manage.py addsite sitename sitedomain
    # example
    $ python manage.py addsite site3 site3.example.com

This will create a new directory of files:
~~~
│   ├── site3
│   │   ├── conf
│   │   │   ├── gunicorn
│   │   │   └── nginx
│   │   ├── __init__.py
│   │   ├── local_settings.py
│   │   ├── settings.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── site_base.css
│   │   │   ├── img
│   │   │   │   └── README
│   │   │   ├── js
│   │   │   │   └── README
│   │   │   └── README
│   │   ├── templates
│   │   │   ├── site_base.html
│   │   │   ├── site_index.html
│   │   └── wsgi.py
~~~


#### Templates and Static Files

As mentioned above, GeoSites uses a hierachy for static files and templates. The first template file found will be the one used so templates in the SITE_ROOT/templates directory will override those in PROJECT_ROOT/templates, which will override those in GEONODE_ROOT/templates.  Static files use a hierarchy similar to the the template directories.  However, they work differently because (on a production server) they are collected and stored in a single location.  Because of this care must be taken to avoid clobbering of files between sites, so each site directory should contain all static files in a subdirectory with the name of the site (e.g., static/siteA/logo.png )

The location of the proper static directory can then be found in the templates syntax such as:

    {{ STATIC_URL }}{{ SITENAME|lower }}/logo.png


#### Permissions by Site

Users are added by default to the site on where they are created and they belong to that site only. However, an admin can add or remvoe people from sites through the "Site People" admin panel (Admin->GeoSites->sitepeople). Select the desired site and move people between the boxes to enable or disable them from the site. 

By default data added to GeoNode is publicly available. In the case of GeoSites, new data will be publicly available, but only for the site it was added to, and the master site (all data is added to the master site). Sharing a resource with other sites involved altering the SiteResource table in the admin panel (Admin->GeoSites->SiteResource).  Add available data to a site or remove by moving resources between the two panels.  Once the changes are saved the sites will have the new resources added (or removed).








This directory is used to store static assets for your project. User media files
(FileFields/ImageFields) are not stored here.

The convention for this directory is:

 * css/ — stores CSS files
 * js/ — stores Javascript files
 * img/ — stores image files
This directory is used to store static assets for your project. User media files
(FileFields/ImageFields) are not stored here.

The convention for this directory is:

 * css/ — stores CSS files
 * js/ — stores Javascript files
 * img/ — stores image files
# SLACK Contrib App

Slack is a contrib app starting with GeoNode 2.4.  The slack contrib app is used for publishing messages to [Slack](https://slack.com/) channels.

## Settings

### Activation

To activate the slack contrib app, you need to add `geonode.contrib.slack` to `INSTALLED_APPS`.  For example, with:

```Python
GEONODE_CONTRIB_APPS = (
    'geonode.contrib.slack'
)
GEONODE_APPS = GEONODE_APPS + GEONODE_CONTRIB_APPS
```

### Configuration

The relevant section in [settings.py](https://github.com/GeoNode/geonode/blob/master/geonode/settings.py) starts at line [812](https://github.com/GeoNode/geonode/blob/master/geonode/settings.py#L812).
```Python
# Settings for Slack contrib app
SLACK_ENABLED = False
SLACK_WEBHOOK_URLS = [
    "https://hooks.slack.com/services/T000/B000/XX"
]
```

To enable the slack contrib app simply switch `SLACK_ENABLED` to `True` and replace the existing `SLACK_WEBHOOK_URLS` with the webhook urls you've gotten from your Slack incoming webhooks integration.

## Slack

Slack is a business productivity platform that replaces the need for email.  It's similar to a chatroom, but more sophisticated.  It provides a variety out of the box integrations as well as the ability to make custom integrations.  This provides new automated ways of synchronizing workflows across multiple platforms.  For instance, tracking GitHub commits, Tweets, and GeoNode posts all in one channel.

### Incoming Webhooks
[Incoming webhooks](https://api.slack.com/incoming-webhooks) are Slack's way of exposing an endpoint you can push messages through, like an email address.  You can learn more at https://api.slack.com/incoming-webhooks.  GeoNode posts a JSON payload to these urls.  Slack converts these JSON payloads into messages.  Generally speaking, it's one url per channel (you can override this though).

### Attachments
GeoNode uses Slack's [Attachments](https://api.slack.com/docs/attachments) API to build rich messages that include layer thumbnails and links to download shapefiles, view in Google Earth, etc.
# Exif Contrib App

Exif is a contrib app starting with GeoNode 2.4.  The exif contrib app extracts exif metadata from uploaded JPEG documents.  This contrib app helps automatically fill key metadata gaps, such as the date a picture was taken.  If a document has exif metadata, the exif metadata is visible on a new tab on the document detail page.

Exif data can contain very valuable metadata such as the date and time a picture was taken, the GPS location, and photometric properties.  Not all this metadata is currently used. 

## Settings

### Activation

To activate the exif contrib app, you need to add `geonode.contrib.exif` to `INSTALLED_APPS`.  For example, with:

```Python
GEONODE_CONTRIB_APPS = (
    'geonode.contrib.exif'
)
GEONODE_APPS = GEONODE_APPS + GEONODE_CONTRIB_APPS
```

### Configuration

The relevant section in [settings.py](https://github.com/GeoNode/geonode/blob/master/geonode/settings.py) starts at line [804](https://github.com/GeoNode/geonode/blob/master/geonode/settings.py#L804).

```Python
# Settings for Exif contrib app
EXIF_ENABLED = False
```

To enable the exif contrib app switch `EXIF_ENABLED` to `True`.

## Exif

See the Wikipedia article on Exif at https://en.wikipedia.org/wiki/Exchangeable_image_file_format to learn more.
# NLP Contrib App

NLP is a contrib app starting with GeoNode 2.4.  The nlp contrib app uses [MITIE](https://github.com/mit-nlp/MITIE) and natural language processing (NLP) techniques to infer additional metadata from the raw contents of new text documents and metadata xml uploaded with shapefiles.  This contrib app helps fill key metadata gaps.

## Settings

### Activation

To activate the nlp contrib app, you need to add `geonode.contrib.nlp` to `INSTALLED_APPS`.  For example, with:

```Python
GEONODE_CONTRIB_APPS = (
    'geonode.contrib.nlp'
)
GEONODE_APPS = GEONODE_APPS + GEONODE_CONTRIB_APPS
```

### Configuration

The relevant section in [settings.py](https://github.com/GeoNode/geonode/blob/master/geonode/settings.py) starts at line [806](https://github.com/GeoNode/geonode/blob/master/geonode/settings.py#L806).
```Python
# Settings for NLP contrib app
NLP_ENABLED = False
NLP_LOCATION_THRESHOLD = 1.0
NLP_LIBRARY_PATH = "/opt/MITIE/mitielib"
NLP_MODEL_PATH = "/opt/MITIE/MITIE-models/english/ner_model.dat"
```

To enable the nlp contrib app switch `NLP_ENABLED` to `True` and replace the existing `NLP_LIBRARY_PATH` and `NLP_MODEL_PATH` with the relevant paths.  `NLP_LIBRARY_PATH` points to the MITIE library folder.  `NLP_MODEL_PATH` points to the Named Entity Recognizer (NER) you will use to parse text.  The basic NER model is for English.  There's also a pre-built spanish version.  You can learn more at https://github.com/mit-nlp/MITIE/wiki/Evaluation.  You can train your own model, too; however, that requires a significant investment.  You can use https://github.com/Sotera/mitie-trainer or a command line workflow.  As new language models are built for MITIE, GeoNode should be able to cover multiple languages.

## MITIE

From MITIE's README:

*This project provides free (even for commercial use) state-of-the-art information extraction tools. The current release includes tools for performing named entity extraction and binary relation detection as well as tools for training custom extractors and relation detectors.*

*MITIE comes with trained models for English and Spanish. The English named entity recognition model is trained based on data from the English Gigaword news corpus, the CoNLL 2003 named entity recognition task, and ACE data. The Spanish model is based on the Spanish Gigaword corpus and CoNLL 2002 named entity recognition task. There are also 21 English binary relation extraction models provided which were trained on a combination of Wikipedia and Freebase data.*
# Metadata XSL output App

The ``metadataxsl`` contrib app provides a downloadable metadata having the same format as the ISO 
metadata, but having a header like 
```XML
      <?xml-stylesheet type="text/xsl" 
                       href="http://url.to.transfromation.xsl/this.is.the.xsl"?>
```
in order to have the metadata properly formatted on the browser.

The interface will present the link "ISO with XSL" along with the other output formats:
     ![image](https://cloud.githubusercontent.com/assets/717359/14913848/4663a80c-0e06-11e6-868d-0877acdb65d6.png)

In order to have a different output, you will only need to customize the XSL file and provide the CSS files if needed.

# Settings

## Activation

In the ``settings.py``(or local-settings) file, enable the ``geonode.contrib.metadataxsl`` app.  
e.g.::
```Python
    GEONODE_CONTRIB_APPS = (
        'geonode.contrib.metadataxsl'
    )
```

## Update the existing resources

In order to make it possibile for a resource to have its metadata exported as ISO+XSL, it needs to 
have a new entry in the ``base_link`` table.
The implementation will create the needed links every time a new resource is added, but we need to 
post-process the existing resources and add the missing links.

In order to add the missing links, you need to enter the geonode directory and issue the command:

        python manage.py addmissinglinks

For each resource having a link for the ISO metadata, a new link for the ISO+XSL will be created.

## Collect static files

This step is needed in order to copy in the static dir the ``.xsl`` file that will be referenced by the
exported metadata file, and one ``.css`` file that is referenced within the xsl file.

        python manage.py collectstatic

This means that any customization to the output format should be performed on these files.

# Other refs

Please check the issue https://github.com/GeoNode/geonode/issues/2453
# api_basemaps App

API Basemaps is a contrib app that is automatically loaded in settings.py. It will check if any of the below settings are set and then append them to the MAP_BASELAYERS list. Each value can also be added by setting an environment variable using the variable name shown below.

e.g. ```export ALT_OSM_BASEMAPS=True```

By default all values are set as False.

## Settings

Specific settings for map API providers:

* ALT_OSM_BASEMAPS set this variable to True if you want additional osm basemaps
* CARTODB_BASEMAPS set this variable to True if you want cartodb basemaps
* STAMEN_BASEMAPS set this variable to True if you want stamen basemaps
* THUNDERFOREST_BASEMAPS set this variable to True if you want thunderforest basemaps
* MAPBOX_ACCESS_TOKEN set this variable to your MapBox public token
* BING_API_KEY set this variable to your BING Map Key value
# To run the integration tests, do:
paver test_integration

# To run the csw tests, do:
paver test_integration -n geonode.tests.csw

# To run the bdd tests, do:
paver test_bdd --local true
[https://github.com/Kami/parallel-django-and-twisted-test-runner](https://github.com/Kami/parallel-django-and-twisted-test-runner)
# The `src/assets` Directory

There's really not much to say here. Every file in this directory is recursively transferred to `dist/assets/`.

To run the integration tests, make sure a the sqlite db is setup::

  python manage.py migrate

Run geoserver but ensure that the django server is _not_ running::

  paver start_geoserver

While geoserver is running, run tests::

  python manage.py test geonode.upload.tests.integration

Or, run a specific test class or single test (leave out the dot if no test)::

  python manage.py test geonode.upload.tests.integration:<class>.<test?>

These tests will internally run a django server and modify the settings as
needed to adjust differences in configuration. They will also create a user
named `test_uploader` and delete any layers this user owns prior to running.

The upload tests will load a settings module to allow specification of a postgres
database other than what you might use for other local purposes. This module is::

  geonode.upload.tests.test_settings

If the settings do not set the name of the OGC_SERVER DATASTORE option,
the importer tests that import into the database will not run.

The `test_settings` module must also be supplied when launching the tests to run
the full suite including the DATASTORE tests::

  DJANGO_SETTINGS_MODULE=geonode.upload.tests.test_settings python manage.py test geonode.upload.tests.integration
