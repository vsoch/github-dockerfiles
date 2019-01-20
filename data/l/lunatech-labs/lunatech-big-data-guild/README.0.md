to run spark streaming and store in cassandra

```
$ docker-compose up
$ docker-compose run storage
# cd project
# sbt "project storage-service"  run

```
## to check data in cassandra
go to docker folder and

```
../lunatech-big-data-guild/cryptocoinrisk/docker$ docker-compose exec cassandra bash
root@8670f02c49e9:/# cqlsh
Connected to Test Cluster at 127.0.0.1:9042.
[cqlsh 5.0.1 | Cassandra 3.11.3 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh> 
cqlsh> 
cqlsh> DESC KEYSPACES;

coin_risk  system_schema  system_auth  system  system_distributed  system_traces

cqlsh> use coin_risk;
cqlsh:coin_risk> 
cqlsh:coin_risk> 
cqlsh:coin_risk> DESC TABLES;

transactionby

cqlsh:coin_risk> SELECT * FROM transactionby ;

 market | time | priceincoin | priceindollar | transaction | transactionno
--------+------+-------------+---------------+-------------+---------------

(0 rows)
cqlsh:coin_risk> 
```

## to check data in psql
```
../lunatech-big-data-guild/cryptocoinrisk/docker$ docker-compose exec postgres bash
root@dc3928fff599:~# psql coinrisk postgres
coinrisk=# select count(*) from transactions ;
```