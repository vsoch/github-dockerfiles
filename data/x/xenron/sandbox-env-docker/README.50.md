docker build -t dajobe/hbase -f hbase-volumn.Dockerfile .
docker run --name=hbase-docker -h hbase-docker -d dajobe/hbase


HBase in Docker
===============

This configuration builds a docker container to run HBase (with
embedded Zookeeper) running on the files inside the container.

NOTE
----

The approach here requires editing the local server's `/etc/hosts`
file to add an entry for the container hostname.  This is because
HBase uses hostnames to pass connection data back out of the
container (from it's internal Zookeeper).

Hopefully this can be improved with Docker's newer networking
but this hasn't been fixed yet.


Build Image
-----------

    $ docker build -t dajobe/hbase .


Pull image
----------

If you want to pull the image already built then use this

    $ docker pull dajobe/hbase

More details at https://hub.docker.com/r/dajobe/hbase/


Run HBase
---------

To run HBase by hand:

    $ mkdir data
    $ id=$(docker run --name=hbase-docker -h hbase-docker -d -v $PWD/data:/data dajobe/hbase)

To run it and adjust the host system's locally by editing
`/etc/hosts` to alias the DNS hostname 'hbase-docker' to the
container, use this:

    $ ./start-hbase.sh

This will require you to enter your sudo password to edit the host
machine's `/etc/hosts` file


Find Hbase status
-----------------

Master status if docker container DNS name is 'hbase-docker'

    http://hbase-docker:16010/master-status

The region servers status pages are linked from the above page.

Thrift UI

    http://hbase-docker:9095/thrift.jsp

REST server UI

    http://hbase-docker:8085/rest.jsp

(Embedded) Zookeeper status

    http://hbase-docker:16010/zk.jsp


See HBase Logs
--------------

If you want to see the latest logs live use:

    $ docker attach $id

Then ^C to detach.

To see all the logs since the HBase server started, use:

    $ docker logs $id

and ^C to detach again.

To see the individual log files without using `docker`, look into
the data volume dir eg $PWD/data/logs if invoked as above.


Test HBase is working via python over Thrift
--------------------------------------------

Here I am connecting to a docker container with the name 'hbase-docker'
(such as created by the start-hbase.sh script).  The port 9090 is the
Thrift API port because [Happybase][1] [2] uses Thrift to talk to HBase.

    $ ipython
    Python 2.7.9 (default, Mar  1 2015, 12:57:24)
    Type "copyright", "credits" or "license" for more information.
    
    IPython 2.3.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    
    In [1]: import happybase
    
    In [2]: connection = happybase.Connection('hbase-docker', 9090)
    
    In [3]: connection.create_table('table-name', { 'family': dict() } )
    
    In [4]: connection.tables()
    Out[4]: ['table-name']
    
    In [5]: table = connection.table('table-name')
    
    In [6]: table.put('row-key', {'family:qual1': 'value1', 'family:qual2': 'value2'})
    
    In [7]: for k, data in table.scan():
       ...:     print k, data
       ...:
    row-key {'family:qual1': 'value1', 'family:qual2': 'value2'}
    
    In [8]:
    Do you really want to exit ([y]/n)? y
    $

(Simple install for happybase: `sudo pip install happybase` although I
use `pip install --user happybase` to get it just for me)


Test HBase is working from Java
-------------------------------

    $ docker run --rm -it --link $id:hbase-docker dajobe/hbase hbase shell
    HBase Shell; enter 'help<RETURN>' for list of supported commands.
    Type "exit<RETURN>" to leave the HBase Shell
    Version 0.94.11, r1513697, Wed Aug 14 04:54:46 UTC 2013

    hbase(main):001:0> status
    1 servers, 0 dead, 3.0000 average load

    hbase(main):002:0> list
    TABLE
    table-name
    1 row(s) in 0.0460 seconds

Showing the `table-name` table made in the happybase example above.

Alternatively if you have the Hbase distribution available on the
host you can use `bin/hbase shell` if the hbase configuration has
been set up to connect to host `hbase-docker` zookeeper port 2181 to
get the servers via configuration property `hbase.zookeeper.quorum`



Proxy HBase UIs locally
-----------------------

If you are running docker on a remote machine, it is handy to see
these server-private urls in a local browser so here is a
~/.ssh/config fragment to do that

    Host my-docker-server
    Hostname 1.2.3.4
        LocalForward 127.0.0.1:16010 127.0.0.1:16010
        LocalForward 127.0.0.1:9095 127.0.0.1:9095
        LocalForward 127.0.0.1:8085 127.0.0.1:8085

When you `ssh my-docker-server` ssh connects to the docker server and
forwards request on your local machine on ports 16010 / 16030 to the
remote ports that are attached to the hbase container.

The bottom line, you can use these URLs to see what's going on:

  * http://localhost:16010/master-status for the Master Server
  * http://localhost:9095/thrift.jsp for the thrift UI
  * http://localhost:8085/rest.jsp for the REST server UI
  * http://localhost:16010/zk.jsp for the embedded Zookeeper

to see what's going on in the container and since both your local
machine and the container are using localhost (aka 127.0.0.1), even
the links work!





Notes
-----

[1] http://happybase.readthedocs.org/en/latest/

[2] https://github.com/wbolster/happybase
