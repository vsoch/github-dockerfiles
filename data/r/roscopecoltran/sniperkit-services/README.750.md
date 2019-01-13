## Apache Kafka 0.10.2.0 Docker image

> This Docker image is based on openjdk:8u131-jdk-alpine image.

> Kafka ver: "0.10.2.0" Scala ver: "2.11"

You can run:
```
docker run \
  -d \
  --name=kafka \
  --hostname=kafka \
  -p 9092:9092 \
  -e KAFKA_ADVERTISED_LISTENERS=172.17.0.1 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  giabar/gb-kafka
```
The KAFKA_ADVERTISED_LISTENERS variable contains the Docker host ip.

See the official documentation to get more info about parameters: https://kafka.apache.org/documentation/#configuration

This image is configured with a volume at 
* /kafka
to hold the persisted index data.

Use that paths if you would like to keep the data in a mounted volume:
```
docker run \
  -d \
  --name=kafka \
  --hostname=kafka \
  -p 9092:9092 \
  -e KAFKA_ADVERTISED_LISTENERS=172.17.0.1 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/kafka:/kafka \
  giabar/gb-kafka
```

This image exposes the 9092 (Kafka) and 2181 (Zookeeper) TCP ports.

This image is on Docker Hub @ https://hub.docker.com/r/giabar/gb-kafka/ 
