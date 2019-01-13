======================================
Steps to Build Static JavaScript Files
======================================

.. code-block:: bash

   cd exchange/static
   bower install

copy required javascript files from exchange/static/vendor to exchange/static/js

Files Added
-----------

clipboard.min.js - 15OCT2016 (NODE-479)
## start in development mode
```bash
$ vagrant up
$ vagrant ssh
$ django-runserver
```

## provision the vm
(clean geoserver data directory and postgres databases)

```bash
$ vagrant provision
```
rerun the steps to start in development mode.

## setup for maploom development

clone the maploom repo as a sibling of exchange-dev

Example:
```

parent_dir
|
├─── exchange
|        Vagrantfile
|
└─── MapLoom
```
Build MapLoom
```
$ cd MapLoom
$ sudo npm -g install grunt-cli karma bower
$ npm install
$ bower install
$ grunt watch
```

uncomment the following line in the Vagrantfile
```
# config.vm.synced_folder "../MapLoom", "/MapLoom"
```

provision the vm
```bash
$ vagrant provision
```

```bash
$ vagrant ssh
$ dev/setup_maploom_dev.sh
$ django-collectstatic
```
__Note:__  each time you provision the vm, you will need to rerun the last steps above.

## manage exchange services

```bash
$ sudo service exchange {start | stop | restart}
```
## logs
```
/vagrant/dev/.logs/
|
├─── geoserver_error.log    <-- geoserver error log
├─── geoserver.log          <-- geoserver stdout log
├─── supervisor.log         <-- process that runs geoserver log
```
Docker Dev Environment for Exchange
===================================

This is a set of configuration files which automate the creation of a
convenient dev environment for Exchange and GeoNode. It uses some of Docker's
features to reduce pains we've had working with our Vagrant config, such as
frequent waits for a slow provisioning process.


Installation
-------------

1. Install Docker.

   Follow instructions at https://docs.docker.com/engine/installation/

   You will need a recent version of Docker; 1.12 works. The version in
   e.g. the Ubuntu repositories is very old and will waste your time.

   Depending on platform, Docker's install instructions and packages sometimes
   set things up so that you do not have to use `sudo docker`, e.g. by putting
   your user in the `docker` group. Other times, you will have to perform such
   steps yourself, according to the instructions, then log out and back in.
   In some environments, such as Arch Linux, you may need to manually start the
   docker service after installing Docker.

2. Install `docker-compose`.

   Follow instructions at https://docs.docker.com/compose/install/

   You probably need a recent version. 1.7.1 works.

   If you follow the instructions, you should be fine. If you prefer to install
   docker-compose using pip, that works well too, but don't run `sudo pip`;
   install Python tools with `pip install --user` or use plain
   `pip install docker-compose` in a virtualenv.

3. Clone repositories.

   If you already cloned these, great - just go to the next step.

   If you don't already have SSH keys set up with Github, you need to do that;
   check out https://help.github.com/categories/ssh/

   If you need to check out the code and you are set up on Github, refer to the
   following example, which assumes I keep my work repos under `~/boundless`::

       cd ~/boundless
       git clone https://github.com/geonode/geonode
       git clone https://github.com/boundlessgeo/exchange.git
       git clone https://github.com/boundlessgeo/MapLoom.git

4. Build local MapLoom

   MapLoom is a JavaScript application that needs to be built locally at least
   once before it can be used in Exchange development. As before, if you've
   already done this just go on to the next step.

   Before running this step, you'll need npm (the Node Package Manager)
   installed on your dev machine. Follow the installation instructions for your
   platform at https://nodejs.org/en/download/.

   Next, do the following locally ::

       cd ~/boundless/MapLoom
       npm install -g grunt-cli karma bower
       npm install
       bower install
       grunt watch

5. Edit `.env` to reflect where you keep checkouts of Exchange, GeoNode, and
   MapLoom.

   At the root of the Exchange repo, if you are in the docker branch, you
   should find a file called `.env`. Edit `.env` e.g. with::

       GEONODE_HOME=/wherever/you/keep/geonode
       EXCHANGE_HOME=/wherever/you/keep/exchange
       MAPLOOM_HOME=/wherever/you/keep/MapLoom

   Why is this necessary? `.env` is read by `docker-compose` so that it knows
   where on your computer to find the directories which will be mounted inside
   the containers as `/mnt/exchange`, `/mnt/geonode` and `/mnt/maploom`. If
   these are not set accurately, then the exchange container and the Celery
   worker container will not be able to start properly because they won't have
   code to start with.

   Using host directories like this isn't a Docker thing, just a convenience
   carried over from the Vagrant dev config.


Preparations
------------

Each time you want to start the app, it helps to verify that you have checked
out the right versions of Exchange and GeoNode. Notably, Exchange depends on
the version of GeoNode mentioned in Exchange's requirements.txt, and is liable
to break if you have checked out GeoNode master instead.

Before you start containers, you need to change directory to where you have
Exchange checked out, e.g.::

    cd ~/boundless/exchange

If you see messages like `"WARNING: The GEONODE_HOME variable is not set"` then
you are not at the root directory of an Exchange checkout. The reason is that
docker-compose will not read `.env` to get the paths you configured unless you
are in the same directory as `.env`. (If this is too annoying, we can just
eliminate `.env` and instead make everyone edit `docker-compose.yml` directly.)


Starting Containers
-------------------

In this Docker configuration, the whole application is made up of a set of
containers that run together.

To start all the containers at once in the background, you can issue this
command::

    docker-compose up -d

If some containers haven't built yet, this builds them automatically and then
starts them. docker-compose tries to start everything in the right order based
on its understanding of the service dependencies. But it often takes a few
seconds for services to enter a working state. So certain containers have
scripts which wait for other containers to come up.

Whenever you want to see what containers are currently running, use::

    docker-compose ps

This can tell you, for example, if a container stopped and with what exit code.

After some seconds, the site should be ready to go. (If it is useful to you to
be notified when this happens, you can follow the log for the Exchange
container, because its startup script is written to monitor these events and
give notification of them. See the "Viewing Logs" section.)

If you are interested in why startup is slow, see the section of this document
titled "Why is Startup Slow?"


Using Exchange
--------------

From your browser running on the same machine that is running docker, you can
then browse to Exchange at

    http://172.16.238.2

If you happen to see a 502 error, that's probably coming from proxy (nginx) and
it probably means that proxy is waiting on Exchange to come up. The logs will
tell the tale.

You can log in with username `admin` and password `exchange`.


Using GeoServer
---------------

GeoServer can be browsed at

    http://172.16.238.2/geoserver

If you want to log in from the GeoServer interface, you can use username
`admin` and password `geoserver`.


Restarting Containers
---------------------

Whenever you need to restart a service, just restart its container. For
example, this is how you would restart the exchange container::

    docker-compose restart exchange

You shouldn't normally need to go into containers to manually fiddle with
processes or services.

These configs use the Django server as the Vagrant config did, which means that
sometimes it auto-reloads when you change things, but sometimes it doesn't.
Unfortunately, this is inherent to the Django reloading mechanism.
Should we use something else? Submit a PR!


Viewing Logs
------------

If you are developing Exchange, GeoNode, GeoServer, etc. then it probably isn't
enough just to run the apps. You want to see what they are doing.

You don't need to know log locations or dig around for logs inside the
containers, because docker-compose will bring them right to you.

To view the log of a container (e.g. the exchange container) up til now,
then exit immediately::

    docker-compose logs exchange

To follow the logs for all containers at once (confusing)::

    docker-compose logs -f

To follow the log for a particular container::

    docker-compose logs -f exchange

Hit Ctrl-C to bring down this log follower, but not any containers.

The same trick works for multiple containers, e.g.::

    docker-compose logs -f exchange geoserver


Stopping Containers
-------------------

You can stop any one specific container without bringing down others, as in::

    docker-compose stop exchange

It tries to gracefully stop containers, so it may take a few seconds. In
particular, Celery often takes a while to shut down. This is not specific to
Exchange and is nothing to worry about.

Naturally, containers which depend on each other may complain if other
containers go down. For example, starting `proxy` (nginx) when Exchange or
Geoserver are not up might cause it to die, citing the absence of an upstream.
Sometimes this can actually be useful for quickly testing what happens when
something fails.

When you want to bring all the containers down in parallel::

    docker-compose down


Stupid Container Tricks
-----------------------

See `docker-compose help` to see some of the many other things you can do.

You should not normally need anything like 'vagrant ssh'. But if you feel the
need to mess up a container as quickly as possible, you can use e.g.
`docker-compose exec exchange /bin/bash`. This tends to create weird states
that can take a long time to debug, so please avoid it if you can. If the
config is broken, let's work together to fix it and share the fixes so that we
always have working automation.

If you want to see a lot of metadata about a running container, you can
use `docker ps` to get the container id that you are interested in (suppose for
example it is '29358') and then use `docker inspect 29358`.


Diagnostics
-----------

`172.16.238.2` is the normal web access for your Exchange instance, but that IP
is actually an nginx reverse proxy that is named `proxy` in
`docker-compose.yml`.

Other containers have intentionally been exposed to the host with certain fixed
IPs for diagnostic convenience (the default and convention with Docker is not
to use fixed IPs, and usually not to use IPs at all).

If you want to directly inspect the Django box without going through proxy, use

    http://172.16.238.3

If you want to directly inspect the GeoServer box without going through proxy,

    http://172.16.238.4:8080/geoserver

The Tomcat page is at

    http://172.16.238.4:8080

These diagnostic URLs are only available because we are fixing IPs in the
docker-compose.yml. That is not recommended practice for production uses of
docker, but this is a dev environment and we just need a URL to hit.


Scratch Volume
--------------

Since different services have been put into different containers, and
containers do not share a filesystem by default, you will find that the various
services used by exchange do not share a filesystem.

For the purpose of allowing some state sharing to occur but also labeling the
places where it happens better, there is defined in `docker-compose.yml` (in
the top-level `volumes:` section) a shared named volume called `scratch`, which
containers mount at `/scratch/`. While this directory is technically possible
to see from the host, there is no guaranteed path and it's not recommended to
use it.

Note that any code or configuration which depends on the presence of this
shared volume effectively requires services to be run on the same machine,
which places an obstacle to distributing work across machines.


Why is Startup Slow?
--------------------

It is a known issue that the Exchange container takes a little while to start.
There are two reasons for this which seem hard to avoid.

1. It is necessary to check for necessary dependency upgrades at each boot,
   because developers editing the files in the shared mounts may change (e.g.)
   Exchange requirements.txt or GeoNode setup.py in arbitrary ways between
   executions.

2. It is necessary to run migrations at each boot, because the database could
   be in any state, and the migrations could be in any state.

Similar considerations apply to the celery worker.

We could make startup faster by baking more changes into the container images.

If you have any ideas or patches to speed this up, please share them!
Dockerfile for Base Container for Travis CI
===========================================

This is a basic container that was built upon the centos 6 container. It
includes jetty-runner and yum core libraries needed to build exchange in
Travis.


Installation
-------------

.. code-block:: bash

   cd exchange
   docker build -t boundlessgeo/ci-exchange-el6:2.1.0b2 -f docker/travis/dockerhub/Dockerfile .
   docker push boundlessgeo/ci-exchange-el6:2.1.0b2
