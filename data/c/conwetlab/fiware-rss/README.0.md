
# FIWARE-RSS MODULE

This module contains the source code corresponding to RSS System and the web develop to its administration.

The result of the compilation of this modulo, it is the fiware-rss war file to be deployed in a Apache Tomcat Server
that it is contained in target folder.
# EXPENDITURE LIMIT MODULE

This module contains the source code corresponding to Expenditure Limit service.

The result of the compilation of this module, it is the expenditureLimit war file to be deployed in a Apache Tomcat Server
that is contained in el-server module target folder.# RSS Docker Image

Stating on version 4.4.3, you are able to run the Revenue Sharing System with Docker. As you may know, the RSS needs a MySQL database to store some information. For this reason, you must create an additional container to run the database. You can do it automatically with `docker-compose` or manually by following the given steps.

## OAuth2 Authentication

The RSS authenticates with the [FIWARE Lab identity manager](https://account.lab.fiware.org). In this regard, it is needed to register an application in this portal in order to acquire the OAuth2 credentials, required for configuring the RSS.

To register this new application, you will need to provide the following information:

* Description
* URl: Must be `http://YOUR\_HOST:PORT/fiware-rss/`
* Callback URL: Must be `http://YOUR\_HOST:PORT/fiware-rss/callback?client\_name=FIWAREClient`

## Automatically

You can install the RSS automatically if you have `docker-compose` installed in your machine. To do so, you must create a folder to place a new file file called `docker-compose.yml` that should include the following content:

```
rss_db:
    image: mysql:latest
    volumes:
        - /var/lib/mysql
    environment:
        - MYSQL_ROOT_PASSWORD=my-secret-pw
        - MYSQL_DATABASE=rss

rss:
    image: rss
    ports:
        - "PORT:8080"
    links:
        - rss_db
    environment:
        - RSS_CLIENT_ID=YOUR_CLIENT_ID
        - RSS_SECRET=YOUR_CLIENT_SECRET
        - RSS_URL=http://YOUR_HOST:PORT
```

**Note**: You must include the OAuth2 credentials of your application as well as its URL.

Once you have created the file, run the following command:

```
docker-compose up
```

Then, the RSS should be up and running in `http://YOUR_HOST:9999/fiware-rss` replacing `YOUR_HOST` by the host of your machine and `PORT` by the port selected in the previous step. 

## Manually

### 1) Creating a Container to host the Database

The first thing that you have to do is to create a docker container that will host the database used by the RSS. To do so, you can execute the following command:

```
docker run --name rss_db -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=rss -v /var/lib/mysql -d mysql
```

* As can be seen, some environment variables are set in this command to set up the data base. You must **not** change these variables, since their values are the ones expected by the RSS image.

### 2) Deploying the RSS Image

Once that the database is configured, you can deploy the image by running the following command:

```
docker run -e RSS_CLIENT_ID=YOUR_CLIENT_ID -e RSS_SECRET=YOUR_CLIENT_SECRET -e RSS_URL=http://YOUR_HOST:PORT -p PORT:8080 --link rss_db rss
```

**Note**: You must include the OAuth2 credentials of your application as well as its URL.

Once that you have run these commands, the RSS should be up and running in `http://YOUR_HOST:PORT/fiware-rss` replacing `YOUR_HOST` by the host of your machine and `PORT` by the port selected in the previous step. 
