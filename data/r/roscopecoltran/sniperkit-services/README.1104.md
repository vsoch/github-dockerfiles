# docker-hdocdb

[HDocDB](https://github.com/rayokota/hdocdb) (HBase as a JSON Document Database) docker images based on alpine

## Small setup
```
# build docker image
docker build --build-arg "VERSION=0.0.3" -t local/hdocdb .

# network 
docker network create vnet

# hadoop+hbase+hdocdb startup
docker-compose up -d

# tail logs for a while
docker-compose logs -f

# check ps
docker-compose ps

     Name                   Command               State                  Ports                
---------------------------------------------------------------------------------------------
datanode-1       entrypoint.sh datanode           Up      50010/tcp, 50020/tcp, 50075/tcp     
hmaster-1        entrypoint.sh hmaster-1          Up      16000/tcp, 0.0.0.0:32785->16010/tcp 
namenode-1       entrypoint.sh namenode-1         Up      0.0.0.0:32782->50070/tcp, 8020/tcp  
regionserver-1   entrypoint.sh regionserver       Up      16020/tcp, 16030/tcp                
zookeeper-1      entrypoint.sh -server 1 1 vnet   Up      2181/tcp, 2888/tcp, 3888/tcp

# hdocdb shell via nashorn
docker-compose exec regionserver-1 sh
> /usr/local/hdocdb # jrunscript -cp lib/hdocdb-0.0.3.jar -f lib/hdocdb.js -f -

nashorn> db.mycoll.insert( { _id: "jdoe", first_name: "John", last_name: "Doe" } )
nashorn> var doc = db.mycoll.find( { last_name: "Doe" } )[0]
nashorn> print(doc)
{"_id":"jdoe","first_name":"John","last_name":"Doe"}
nashorn> db.mycoll.update( { last_name: "Doe" }, { $set: { first_name: "Jim" } } )
nashorn> var doc = db.mycoll.find( { last_name: "Doe" } )[0]
nashorn> print(doc)
{"_id":"jdoe","first_name":"Jim","last_name":"Doe"}
nashorn> db.mycoll.delete( "jdoe" )

```