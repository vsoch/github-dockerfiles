Step 1, Create a Rails app :
```no-highlight
docker run --name any_temporary_container_name -ti -v `pwd`:/app clmntlxndr/rails new APP_NAME .
```

Step 2, Commit image with bundled dependencies :

```no-highlight
docker commit any_temporary_container_name APP_NAME
docker rm any_temporary_container
```

Step 3, Start the app :

```no-highlight
cd APP_NAME
docker run --rm any_temporary_container_name -ti -v `pwd`:/app APP_NAME
```

-------

Update gems and recreate image :

```no-highlight
docker run --name any_temporary_container_name -ti -v --entrypoint bundle `pwd`:/app APP_NAME install
docker commit any_temporary_container_name APP_NAME
docker run --name any_other_temporary_container_name -ti --entrypoint rails APP_NAME s -b 0.0.0.0 -p 3000
docker commit any_other_temporary_container_name APP_NAME
docker rm any_temporary_container_name any_other_temporary_container_name
```

You can then start updated image from Step 3

--------

This Dockerfile plays nice with my [docker-compose rails boilerplate](https://github.com/clm-a/Dockerthings/tree/master/docker-compose-boilerplates/rails) to avoid entrypoints and command overrides
(Dockerfile in the boilerplate is a copy of the one here)
