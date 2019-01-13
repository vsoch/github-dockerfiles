1. Start with following docs/installation.rst and docs/configuration.rst.

2. Bootstrap the local eduid_am database

$ mongo localhost:27017/eduid_am eduid_am_initial.js

3. Add the following line to the configuration file for local development.

# Set development to true for SAML2 decoupling.
development = true
# admin, helpdesk, user1, user2
development_user = admin
$ sudo systemctl start docker

$ cat mongodb | docker build -t="enriquepablo/mongodb:0.1" -

$ cat basic-rabbitmq | docker build -t="enriquepablo/rabbitmq:0.1" -

$ cat eduid-rabbitmq | docker build -t="eduid/rabbitmq:0.1" -

$ cat eduid-am | docker build -t="eduid/am:0.1" -

$ cat eduid-msg | docker build -t="eduid/msg:0.1" -

$ cat eduid-vccs | docker build -t="eduid/vccs:0.1" -

$ cat smtp-debug | docker build -t="enriquepablo/smtp-debug:0.1" -

$ cat eduid-dashboard | docker build -t="eduid/dashboard:0.1" -

$ docker run -d --name mongo enriquepablo/mongodb:0.1

$ docker run -d --name rabbitmq eduid/rabbitmq:0.1

$ docker run -d -p 8550:8550 --name vccs eduid/vccs:0.1

$ docker run -d -p 2525:2525 --name smtp-debug enriquepablo/smtp-debug:0.1

$ docker run -d --name eduid_am --link mongo:mongo --link rabbitmq:rabbitmq eduid/am:0.1

$ docker run -d --name eduid_msg --link mongo:mongo --link rabbitmq:rabbitmq eduid/msg:0.1

$ docker run -d -p 6545:6544 --name eduid_dashboard_1 --link mongo:mongo --link rabbitmq:rabbitmq --link smtp-debug:smtp-debug --link vccs:vccs -e EDUID_DASHBOARD_BASE_URL="http://192.168.122.1:6545/" eduid/dashboard:0.1

$ docker run -d -p 6546:6544 --name eduid_dashboard_2 --link mongo:mongo --link rabbitmq:rabbitmq --link smtp-debug:smtp-debug --link vccs:vccs -e EDUID_DASHBOARD_BASE_URL="http://192.168.122.1:6546/" -v /home/eperez/src/git/eduid-dashboard/eduiddashboard:/opt/eduid-dashboard/eduiddashboard eduid/dashboard:0.1

$ docker run -d -p 6543:6543 --name eduid_signup_1 --link mongo:mongo --link rabbitmq:rabbitmq --link smtp-debug:smtp-debug --link vccs:vccs --link eduid_dashboard_1:dashboard -v /home/eperez/src/git/eduid-signup/eduid_signup:/opt/eduid-signup/eduid_signup eduid/signup:0.1

$ docker start rabbitmq mongo eduid_am eduid_msg vccs smtp-debug eduid_dashboard_1 eduid_dashboard_2 eduid_signup_1

$ docker stop eduid_signup_1 eduid_dashboard_2 eduid_dashboard_1 smtp-debug vccs eduid_msg eduid_am mongo rabbitmq

################################################

# We must copy the certificates generated in the dashboards to the idp.
# They are in the dashboard container, in /opt/eduid-dashboard/certs/server.crt
# And must be copied to the idp, to: /var/www/idp/simplesamlphp/metadata/saml20-sp-remote.php

# We must add some document to the mongodb://eduid_am/attributes collection.
# E.g.:

#  yaco@ubuntu:~$ mongo eduid_am
#  MongoDB shell version: 2.0.4
#  connecting to: eduid_am
#  > db.attributes.find({})
#  { "_id" : ObjectId("52d3efc66a9089aebbf24803"), "date" : ISODate("2013-09-02T10:23:25.967Z"), "displayName" : "Enrique Pérez", "eduPersonEntitlement" : [      "urn:mace:eduid.se:role:admin",         "urn:mace:eduid.se:role:manager",       "urn:mace:eduid.se:role:consultant" ], "givenName" : "Enrique", "mail" : "eperez@yaco.es", "mailAliases" : [   {       "verified" : true,      "email" : "eperez@yaco.es" },   {       "verified" : true,      "email" : "eperez2@yaco.es" },         {       "verified" : true,      "email" : "eperez234@yaco.es" } ], "mobile" : [ { "mobile" : "+03666666666", "verified" : false, "primary" : false } ], "norEduPersonNIN" : [ "123412341234" ], "preferredLanguage" : "en", "sn" : "Pérez-Corri" }

# Enter the mongo container and add it to it:

#  [0] eperez@ave$ docker inspect --format '{{.State.Pid}}' mongo
#  2076
#  (~)
#  [0] eperez@ave$ sudo nsenter --target 2076 --mount --uts --ipc --net --pid
#  root@e867efa68b2f:/# mongo eduid_am
#  MongoDB shell version: 2.0.6
#  connecting to: eduid_am
#  > db.attributes.insert( { "_id" : ObjectId("52d3efc66a9089aebbf24803"), <...>  3666666666", "verified" : false, "primary" : false } ], "norEduPersonNIN" : [ "123412341234" ], "preferredLanguage" : "en", "sn" : "Pérez-Corri" })
