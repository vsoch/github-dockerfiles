# Ec2 Consistent Snapshot

How to take an ec2 consistent snapshot of a mongodb database on an amazonaws ubuntu instance using docker.

## 1. Create an AWS ubuntu instance

* go to the AWS console on the web browser
* click on EC2 then instances and click on Launch Instance
* create an instance based on Ubuntu 13 or 14
* pass #include https://get.docker.io to the userdata
* download .pem file and follow aws instructions to finish creating the instance

## 2. Getting Started With Docker

* ssh into the ubuntu instance with the .pem file, your username and public dns
```
ssh -i key-pair.pem username@ec2-198-51-100-1.compute-1.amazonaws.com
```
* become the root user
```
sudo su
```
* use docker to pull and run the mongodb image
```
docker run --name sync_mongo -d mongo
```
* now run the ec2-consistent-snapshot image and connect it to the mongo container with the following command
```
docker run -it -e AWS_ACCESS_KEY_ID=accesskey -e AWS_SECRET_ACCESS_KEY=secretaccesskey --volumes-from sync_mongo --link sync_mongo:mongo synctree/ec2-consistent-snapshot bin/bash 
```
## 3. Running Ec2 Consistent Snapshot

* run the ec2-consistent-snapshot with the following command
```
ec2-consistent-snapshot --mongo --mongo-host $MONGO_PORT_27017_TCP_ADDR --mongo-port $MONGO_PORT_27017_TCP_PORT vol-volumeId
result: snap-somenumber
```
-the volumeId is the id of the volume that has the aws instance and the snap-*somenumber* is the id of the snapshot

### It should show that a snapshot is being taken on the aws console on the web browser

Thats it! 
