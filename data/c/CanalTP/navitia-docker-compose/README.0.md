# Navitia's dev image
Docker image used to build and run navitia's test

This image should be used only for dev purpose

# build

```
docker build -t navitia-local-builder .
```

Note: you can decide the number of thread you want the compilation to use with the env var NB_THREAD.

by default the compilation uses all it can

# run

the navitia dir needs to be given as a volume and mounted in build/navitia

We also need to give the docker socket to run docker tests inside the docker

```
docker run -v {you_path_to_navitia}:/work/navitia  -v /var/run/docker.sock:/var/run/docker.sock navitia-local-builder  
```   

If you plan to do it several times, you might want to cache the compilation

```
docker run -v {your_path_to_navitia}:/work/navitia -v ${pwd}/docker_build_dir:/work/build -v /var/run/docker.sock:/var/run/docker.sock navitia-local-builder  
```   

# misc

Note: don't forget to update the submodules in you local navitia sources