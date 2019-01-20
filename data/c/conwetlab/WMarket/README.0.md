# Utilities

This folder contains utilities that can be used to install WMarket in a easier
way. To install WMarket, you can use these to scripts:

* `install.sh`:
 * Ready for Ubuntu 14.04 LTS & CentOS 7
 * It installs all the required dependencies
 * It requires interaction to set the following parameters:
   * **Database**: user name and password
   * **Index**: path to Store Lucene indexes
   * **Media**: path to Store media files and the maximum size of these files
   * **Autoupdate period**: period to upload the descriptions and retrieve new
     offerings
   * **OAuth2**: enable or disable OAuth2. If OAuth2 is enabled, some parameters
     will be required (IdM URL, client ID, client secret, machine IP...)
* `autoinstall.sh`:
  * Ready for Ubuntu 14.04 LTS
  * It installs all the required dependencies
  * It does not require interaction. Parameters are set with default values:
    * **Database**:
      * User: `root` 
      * Password: `admin`
    * **Index**: `/opt/index`
    * **Media**:
      * Path: `/opt/media`
      * Max Size: 3145728 (3 MB)
    * **Autoupdate period**: 43200 (1 day)
    * **OAuth2**: No

Additionally, you can use the `test.sh` script to check if the service is
properly running. The script needs to know the IP where the service is running.
You can specify it by setting the `IP` environment variable. For example, if
your instance is running on `localhost`, you can run the script by executing the
following commands:

```
export IP=127.0.0.1
./test.sh
```
# WMarket Docker Image

Stating on version 4.3.3, you are able to run WMarket with Docker. As you may know, WMarket needs a MySQL database to store some information. For this reason, you must create an additional container to run the database. You can do it automatically with `docker-compose` or manually by following the given steps.

## Automatically

You can install WMarket automatically if you have `docker-compose` installed in your machine. To do so, you must create a folder to place a new file file called `docker-compose.yml` that should include the following content:

```
wmarket_db:
    image: mysql:latest
    volumes:
         - /var/lib/mysql
    environment:
        - MYSQL_ROOT_PASSWORD=my-secret-pw
        - MYSQL_DATABASE=marketplace

wmarket:
    image: conwetlab/wmarket
    volumes:
        - /WMarket
    ports:
        - "80:8080"
    links:
        - wmarket_db
    command: bash -c 'sleep 15 && catalina.sh run'
```

Once that you have created the file, run the following command:

```
docker-compose up
```

Then, WMarket should be up and running in `http://YOUR_HOST:80/WMarket` replacing `YOUR_HOST` by the host of your machine.

## Manually

### 1) Creating a Container to host the Database

The first thing that you have to do is to create a docker container that will host the database used by WMarket. To do so, you can execute the following command:

```
docker run --name wmarket_db -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=marketplace -v /var/lib/mysql -d mysql
```

* As can be seen, some environment variables are set in this command to set up the data base. You must **not** change these variables, since their values are the ones expected by the WMarket image.

### 2) Deploying the WMarket Image

Once that the database is configured, you can deploy the image by running the following command (*replace `PORT` by the port of your local machine that will be used to access the service*):

```
docker run --name wmarket -v /WMarket -p PORT:8080 --link wmarket_db -d conwetlab/wmarket
```

Once that you have run these commands, WMarket should be up and running in `http://YOUR_HOST:PORT/WMarket` replacing `YOUR_HOST` by the host of your machine and `PORT` by the port selected in the previous step. 