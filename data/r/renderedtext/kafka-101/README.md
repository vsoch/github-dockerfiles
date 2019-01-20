# Kafka-101

Simple Kafka Producer-Consumer communication. A base project for further
research and education.

### Setup

The project is docker based, and uses docker compose to spin up Kafka, Zookeper,
a Ruby based Producer service, and a Ruby Based Consumer service.

The Ruby services can be found in the `app` directory.

To build the docker images, run the following:

``` bash
docker-compose build
```

### Testing the system

Run the following command to start the communication between the services:

``` bash
docker-compose up --build
```

After Kafka and Zookeper finish with several pages of startup output, you will
see the output from the services. You should see an output like the following:

``` text
producer_1    | "Publishing: Hello, 25"
subscriber_1  | topic: greetings, partition: 0, offset: 257, key: , value: Hello, 25
producer_1    | "Publishing: Hello, 26"
subscriber_1  | topic: greetings, partition: 0, offset: 258, key: , value: Hello, 26
producer_1    | "Publishing: Hello, 27"
subscriber_1  | topic: greetings, partition: 0, offset: 259, key: , value: Hello, 27
producer_1    | "Publishing: Hello, 28"
subscriber_1  | topic: greetings, partition: 0, offset: 260, key: , value: Hello, 28
producer_1    | "Publishing: Hello, 29"
subscriber_1  | topic: greetings, partition: 0, offset: 261, key: , value: Hello, 29
producer_1    | "Publishing: Hello, 30"
subscriber_1  | topic: greetings, partition: 0, offset: 262, key: , value: Hello, 30
```

A new message is sent to Kafka every 10 seconds.
