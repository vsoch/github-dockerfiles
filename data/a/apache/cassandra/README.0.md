Cassandra Trigger Example:
==========================

The AuditTrigger class will create a basic audit of
activity on a table.

Installation:
============
change directory to <cassandra_src_dir>/examples/triggers
run "ant jar"
Copy build/trigger-example.jar to <cassandra_conf>/triggers/
Copy conf/* to <cassandra_home>/conf/

Create the keyspace and table configured in AuditTrigger.properties:
    CREATE KEYSPACE test WITH REPLICATION =
        { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };
    CREATE TABLE test.audit (key timeuuid, keyspace_name text,
        table_name text, primary_key text, PRIMARY KEY(key));

Create a table to add the trigger to:
    CREATE TABLE test.test (key text, value text, PRIMARY KEY(key));
    Note: The example currently only handles non-composite partition keys

Configure the trigger on the table:
    CREATE TRIGGER test1 ON test.test
        USING 'org.apache.cassandra.triggers.AuditTrigger';

Start inserting data to the table that has the trigger. For each
partition added to the table an entry should appear in the 'audit' table:
    INSERT INTO test.test (key, value) values ('1', '1');
    SELECT * FROM test.audit;

    key                                  | keyspace_name | primary_key | table_name
   --------------------------------------+---------------+-------------+------------
    7dc75b60-770f-11e5-9019-033d8af33e6f |          test |           1 |       test

Required configuration files
============================

cassandra.yaml: main Cassandra configuration file
logback.xml: logback configuration file for Cassandra server


Optional configuration files
============================

cassandra-topology.properties: used by PropertyFileSnitch


Place triggers to be loaded in this directory, as jar files.
# Apache Cassandra rpmbuild

### Requirements:
- The build system needs to have Apache Cassandra `ant artifacts` build dependencies installed.
- Since Apache Cassandra depends on Python 2.7, the earliest version supported is RHEL/CentOS 7.0.

### Step 1:
- Build and copy sources to build tree:
```
ant artifacts -Drelease=true
```

### Step 2:
- Since there is no version specified in the SPEC file, one needs to be passed at `rpmbuild` time (example with 4.0):
```
mkdir -p build/rpmbuild/{BUILD,RPMS,SPECS,SRPMS}
rpmbuild --define="version 4.0" \
    --define="revision $(date +"%Y%m%d")git$(git rev-parse --short HEAD)%{?dist}" \
    --define "_topdir $(pwd)/build/rpmbuild" \
    --define "_sourcedir $(pwd)/build" \
    -ba redhat/cassandra.spec
```

Use revision value in the example above for git based snapshots. Change to `--define="revision 1"` for non-snapshot releases.

- RPM files can be found in their respective build tree directories:
```
ls -l build/rpmbuild/{SRPMS,RPMS}/
```

### Hint:
- Don't build packages as root..
Cassandra for Debian
====================

This package is not a part of Debian, (and there are no immediate plans
to have it added). Bugs should be sent to the Apache Cassandra JIRA, *not*
filed in the Debian BTS.

  https://issues.apache.org/jira/browse/CASSANDRA

Apache Cassandra documentation directory
========================================

This directory contains the documentation maintained in-tree for Apache
Cassandra. This directory contains the following documents:
- The source of the official Cassandra documentation, in the `source/`
  subdirectory. See below for more details on how to edit/build that
  documentation.
- The specification(s) for the supported versions of native transport protocol.
- Additional documentation on the SASI implementation (`SASI.md`). TODO: we
  should probably move the first half of that documentation to the general
  documentation, and the implementation explanation parts into the wiki.


Official documentation
----------------------

The source for the official documentation for Apache Cassandra can be found in
the `source` subdirectory. The documentation uses [sphinx](http://www.sphinx-doc.org/)
and is thus written in [reStructuredText](http://docutils.sourceforge.net/rst.html).

To build the HTML documentation, you will need to first install sphinx and the
[sphinx ReadTheDocs theme](https://pypi.org/project/sphinx_rtd_theme/).
When using Python 3.6 on Windows, use `py -m pip install sphinx sphinx_rtd_theme`, on unix
use:
```
pip install sphinx sphinx_rtd_theme
```

The documentation can then be built from this directory by calling `make html`
(or `make.bat html` on windows). Alternatively, the top-level `ant gen-doc`
target can be used.  When using Python 3.6 on Windows, use `sphinx_build -b html source build`.

To build the documentation with Docker Compose, run:

```bash
cd ./doc

# build the Docker image
docker-compose build build-docs

# build the documentation
docker-compose run build-docs
```

To regenerate the documentation from scratch, run:

```bash
# return to the root directory of the Cassandra project
cd ..

# remove all generated documentation files based on the source code
ant realclean
```
cassandra-stress
======

Setup
-----
Run `ant` from the Cassandra source directory, then cassandra-stress can be invoked from tools/bin/cassandra-stress.
cassandra-stress supports benchmarking any Cassandra cluster of version 2.0+.

Usage & Examples
----------------

See: https://cassandra.apache.org/doc/latest/tools/cassandra_stress.html

