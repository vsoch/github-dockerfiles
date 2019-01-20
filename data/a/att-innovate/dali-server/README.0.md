Run Mongo DB

Based on: https://github.com/docker-library/mongo/tree/master/3.4

Run Mongo database, replace /tmp with the path to your local persistent directory
$ docker run -d --name dali-mongo -p 27017:27017 -v /tmp:/data dali-mongo

Run Mongo shell same host as the database
$ docker run -ti --net=host dali-mongo mongo

To use Mongo shell to access remote database, replace HOST-IP with the IP of your mongo host.
$ docker run -ti dali-mongo mongo HOST-IP:27017

