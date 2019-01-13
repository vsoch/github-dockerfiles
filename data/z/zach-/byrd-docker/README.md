Table of Contents
=================

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

-	[Table of Contents](#table-of-contents)
  -	[Docker](#docker)
  -	[Jetty](#Jetty)
  -	[Byrds Eye](#byrds-eye)
  -	[Instructions](#instructions)

<!-- /TOC -->

Docker
------

Used to deploy the app anywhere

Jetty
-----

Jetty 9 to deploy app

Byrds Eye
---------

My application, located in private repository https://github.com/zach-/byrds-eye

Instructions
------------

1.	Setup Docker
2.	Build each container using the following scripts respectively:<br>`docker build -t jetty`<br>`docker build -t mongo`
3.	Start the MonoDB container by using: `docker run -d --name mongodb mongo`
4.	Setup the MongoDB database named `zach` by using the following command:<br>`docker run -it --link mongodb:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'`<br>This will open a shell to mongo, type: `use zach` to create the database
5.	Close the mongo shell
6.	Run the following to create the jetty instance:<br>`docker run -p 8080:8080 -v /path/to/war/dir/:/opt/jetty/webapps --name byrd-docker --link mongodb:mongo-d jetty`
7.	Access your localhost on port 8080 and you should have a working application
