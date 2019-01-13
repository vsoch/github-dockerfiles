## Apache Spark 2.1.1 Docker image

> This Docker image is based on the OpenJDK 1.8 Alpine image.

Run a Spark container:

```
docker run \
  -it \
  giabar/gb-spark
  bash
```

Now you're inside the Spark container and you can start a spark-shell:

```
spark-shell
```
