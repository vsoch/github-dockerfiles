Sync AS Dockerfile

#docker run -ti --name sync_as --p 8080:8080 mmatoscom/sync-as

* to-do list:
- entrypoint
- volumes
- wget version (currently ADDing jdk and sync-as)


* build log:

$ docker build -t mmatoscom/sync-as .
Sending build context to Docker daemon 187.4 MB
Sending build context to Docker daemon 
Step 0 : FROM ubuntu:15.04
 ---> 314a1f078530
Step 1 : MAINTAINER Marco Matos docker@corp.mmatos.com
 ---> Using cache
 ---> 9148517d216a
Step 2 : RUN apt-get update && apt-get install
 ---> Using cache
 ---> c88afe52d783
Step 3 : RUN apt-get install -y wget --force-yes
 ---> Using cache
 ---> 0ca18f6a4c30
Step 4 : WORKDIR /
 ---> Using cache
 ---> a1ad4303da8b
Step 5 : ADD jdk-8u65-linux-x64.tar.gz /
 ---> Using cache
 ---> 40a9ab53f2bf
Step 6 : RUN ls /jdk1.8.0_65
 ---> Using cache
 ---> 40cffe6a35d6
Step 7 : ENV JRE_HOME /jdk1.8.0_65/jre
 ---> Using cache
 ---> 06347f52d23f
Step 8 : ENV JAVA_HOME /jdk1.8.0_65
 ---> Using cache
 ---> 7dfea934dfc6
Step 9 : ENV PATH /jdk1.8.0_65/bin/:$PATH
 ---> Using cache
 ---> 41f79b383e9c
Step 10 : RUN mkdir -p /opt/sync/as/
 ---> Using cache
 ---> c7ef1a23012e
Step 11 : ENV AS_FILE sync-as-0.1.2.tar.gz
 ---> Using cache
 ---> f48d28ec472d
Step 12 : ENV AS_FOLDER sync-as-0.1.2
 ---> Using cache
 ---> d59b34fa13fb
Step 13 : ENV AS_URL http://www.syncobjects.com/sync-as-0.1.2.tar.gz
 ---> Using cache
 ---> 5e36a3c08087
Step 14 : ENV AS_HOME /opt/sync/as/
 ---> Using cache
 ---> 832a25a778ed
Step 15 : ADD sync-as-0.1.2.tar.gz /opt/
 ---> 6cd4f384357c
Removing intermediate container b044be447e76
Step 16 : RUN ls /opt
 ---> Running in 8e353c2ea203
applications
lib
server.properties
sync
 ---> 081d4952b9ce
Removing intermediate container 8e353c2ea203
Successfully built 081d4952b9ce
