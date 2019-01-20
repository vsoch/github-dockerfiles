cayenne-solr
============

A configuration of Solr for the Cayenne loader / API / CrossRef Metadata Search.

## Run as master

> ./bin/solr start -p 8983 -q -Denable.master=true

## Run as a replicating slave

> ./bin/solr start -p 8983 -q -Denable.slave=true -Dmaster.url=http://somehost:8983/solr/crmds1

## Environment

`ulimit -v` and `ulimit -m` should report `unlimited`. `ulimit -n` shoul be large, at least
`30,000`.

Leave a large amount of RAM unallocated and thus available for OS disk cache. At least 50%
of the index size.


