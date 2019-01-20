# FiwareRepository Docker Image

Stating on version 4.4.3, you are able to run Repository-RI with Docker. As you may know, Respository-RI needs a Virtuoso triple store and a Mongo database to store some information. For this reason, you must create an additional containers to run them. You can do it automatically with `docker-compose` or manually by following the given steps.

## Automatically

You can install Respository-RI automatically if you have `docker-compose` installed in your machine. To do so, you must create a folder to place a new file file called `docker-compose.yml` that should include the following content:

```
repository-ri_virtuoso:
    restart: always
    image: tenforce/virtuoso
    ports:
        - 8890:8890
        - 1111:1111
    environment:
        - DBA_PASSWORD=dba
        - SPARQL_UPDATE=true
        - DEFAULT_GRAPH=http://localhost:8890/DAV
    volumes:
        - ~/Repository-RI/virtuosodb:/var/lib/virtuoso/db

repository-ri_mongodb:
    restart: always
    image: mongo:2.4.14
    volumes:
        - ~/Repository-RI/mongodb:/data/db

repository-ri:
    restart: always
    image: conwetlab/repository-ri
    ports:
        - "80:8080"
    links:
        - repository-ri_virtuoso
        - repository-ri_mongodb
```

Once that you have created the file, run the following command:

```
docker-compose up
```

Then, Respository-RI should be up and running in `http://YOUR_HOST:80/FiwareRepository/v2/`.