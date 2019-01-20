# kafka-helper

kafka-helper is a command-line tool that can check on Kafka for you, without
requiring a Kafka environment or Java.

Specify a broker using either `--broker/-b` or the `KAFKA_HELPER_BROKERS`
environment variable. You can specify `-b` multiple times. The default is
`kafka:9092`, which may make things easier for some people, not saying who.

It only does two things right now:

* `kafka-helper check-ready` -- Checks if a client connection can be
  established to Kafka. Exits 0 on success, 1 on failure.

* `kafka-helper topic-exists --topic TOPIC` -- Checks if a topic exists. Exits
  0 on success, 1 on failure.
