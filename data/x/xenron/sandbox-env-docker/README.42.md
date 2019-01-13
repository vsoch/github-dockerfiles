
# Kafka Standalone
build image
```bash
# Default Version Setting
# Java:1.8.0_102
# Scala:2.11
# Kafka=0.8.2.2
docker build -t xenron/kafka_standalone:0.8.2.2 -f Dockerfile .

# Kafka=0.9.0.0
docker build -t xenron/kafka_standalone:0.9.0.0 --build-arg KafkaVersion=0.9.0.0 -f Dockerfile .

# Scala:2.10, Kafka=0.9.0.0
docker build -t xenron/kafka_standalone:0.9.0.0 --build-arg ScalaVersion=2.10 --build-arg KafkaVersion=0.9.0.0 -f Dockerfile .

# Java:1.8.0_101, Scala:2.10, Kafka=0.9.0.0
JavaInfoForDockerBuild=`python get_java_version.py 1.8`
JavaVersionForDockerBuild=${JavaInfoForDockerBuild/|*/}
JavaDownloadForDockerBuild=${JavaInfoForDockerBuild/*|/}
docker build -t xenron/kafka_standalone:0.9.0.0 \
--build-arg JavaVersion=${JavaVersionForDockerBuild} \
--build-arg JavaDownload=${JavaDownloadForDockerBuild} \
--build-arg ScalaVersion=2.11 \
--build-arg KafkaVersion=0.9.0.0 \
-f Dockerfile .
```

# Kafka Simple Test
```bash
# start container
docker run -itd --name kafka -h kafka -p9092:9092 xenron/kafka_standalone:0.8.2.2 bash
docker exec -it kafka bash
source /root/.bash_profile
cd /opt/kafka/kafka_2.11-0.8.2.2
./bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic test1 --partitions 3 --replication-factor 1
./bin/kafka-topics.sh --zookeeper localhost:2181 --describe --topic test1
./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test1
# input serval string
./bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test1 --from-beginning
```


