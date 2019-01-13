## ISSUE

hello/server/datasources.json with $DB_1_PORT_27017_TCP_ADDR:$DB_1_PORT_27017_TCP_PORT ?
sed ?

## dev log

```
$ cd 
$ sudo npm install -g strongloop
$ slc loopback
$ cd hello
$ sudo npm install
$ slc loopback:model
$ slc run
$ curl http://localhost:3000/explorer/

$ slc loopback:datasource
 datasource name : mongodb

$ sudo docker build -t=test/splb .

```## Client

This is the place for your application front-end files.
