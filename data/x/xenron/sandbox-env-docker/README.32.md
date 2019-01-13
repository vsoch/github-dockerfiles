xPatterns Hadoop
=============

Summary
-------
Simple hadoop docker used to run xPatterns. 

 * HDFS : 50070
 * Hive Metastore 
 * JobHistoryServer : 19888
 * Hue : 8888
 * Oozie : 11000
 * Yarn : 8088
 * Spark History Server : 18080

Dependencies
-------
 * Ubuntu >= 12.04, Centos >= 6.5
 * docker >= 1.8.1 (https://docs.docker.com/installation/)

Installation 
-------
 * Pull the latest Hadoop docker container. $`docker pull xpatterns/hadoop`

Running
-------
 * Launch the Hadoop docker container $`docker run -it -p 50070:50070 -p 8088:8088 -p 8040:8040 -p 19888:19888 -p 11000:11000 -p 8888:8888 -p 18080:18080 xpatterns/hadoop`

Testing
-------
 * From host machine: $`docker ps`

Example
-------


Notes
-------

xPatterns Hadoop
=============

Summary
-------
Simple hadoop docker used to run xPatterns. 

 * HDFS : 50070
 * Hive Metastore 
 * JobHistoryServer : 19888
 * Hue : 8888
 * Oozie : 11000
 * Yarn : 8088
 * Spark History Server : 18080

Dependencies
-------
 * Ubuntu >= 12.04, Centos >= 6.5
 * docker >= 1.8.1 (https://docs.docker.com/installation/)

Installation 
-------
 * Pull the latest Hadoop docker container. $`docker pull xpatterns/hadoop`

Running
-------
 * Launch the Hadoop docker container $`docker run -it -p 50070:50070 -p 8088:8088 -p 8040:8040 -p 19888:19888 -p 11000:11000 -p 8888:8888 -p 18080:18080 xpatterns/hadoop`

Testing
-------
 * From host machine: $`docker ps`

Example
-------


Notes
-------

