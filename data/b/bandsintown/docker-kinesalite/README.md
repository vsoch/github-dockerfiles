# What is Kinesalite ?

[Kinesalite](https://github.com/mhart/kinesalite) is an implementation of Amazon's Kinesis, focussed on correctness and performance, and built on LevelDB.

This project just bundle Kinesalite in a Docker image based on [bandsintown/node](https://github.com/bandsintown/docker-node) image.

# Usage

In order to run Kinesalite you just have to:

```
> docker run -ti bandsintown/kinesalite 
```

By default Kinesalite listen on port `4567` and the LevelDB database is store in `/db` folder.

You can customize the other parameters like that: 

```
> docker run -ti -p 3456 bandsintown/kinesalite kinesalite \
 --port 3456 \
 --path /mybd \
 --createStreamMs 250 \
 --deleteStreamMs 250 \
 --updateStreamMs 250 \
 --shardLimit 5
```

# Sample

This project provide a [sample](sample) showing how to integrate Kinesalite with an application sending events, 
and a Lambda functions consuming these events.

Please check it out.

# Build

This project is configured as an [automated build in Dockerhub](https://hub.docker.com/r/bandsintown/alpine/).

Each branch give the related image tag.  

# License

All the code contained in this repository, unless explicitly stated, is
licensed under ISC license.

A copy of the license can be found inside the [LICENSE](LICENSE) file.