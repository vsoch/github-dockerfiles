docker-compose up -d kafka zookeeper pgqd postgres

docker-compose run -e PGHOST=postgres -e PGUSER=postgres --rm --entrypoint=bash postgres

psql -c 'CREATE DATABASE source'
pgbench -i source
psql -c 'CREATE DATABASE destination'
pg_dump -i --schema-only source | psql destination

docker-compose run --rm --entrypoint=bash pgshovel

python -m pgshovel.administration cluster initialize
python example/set.py postgres:///source | python -m pgshovel.administration set create example
python -m pgshovel.relay example/configurations/relay.yml example

pgbench source

python -m pgshovel.replication example/configurations/replication.yml example

docker-compose stop && docker-compose rm -fv
This folder contains a Dockerfile to build and execute the Protocol Buffer compiler.
This folder contains a Dockerfile to build PostgreSQL with the `plpython`_
procedural language and the SkyTools_ extension.

.. _SkyTools: https://wiki.postgresql.org/wiki/SkyTools
.. _plpython: http://www.postgresql.org/docs/9.3/static/plpython.html
