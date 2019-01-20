This nodejs application uses code from the cryptocompare.com socket code example:

[https://github.com/cryptoqween/cryptoqween.github.io]()

See also:
[https://www.cryptocompare.com/api/]()


It is javascript for a web application that was adapted to run with nodejs.

## Run local

Prerequisite is to have kafka running, messages are published on ` test` topic, connecting to ` zookeeper:2181`.

Environment variables can be set, with the following default values:

```
fromSymbol=ETH
toSymbol=USD
zkConnect=zookeeper:2181
topic=test
```


Usage:
```
node stream.js
```
Dependencies are `request`, `socket.io`, and `kafka-node` node modules.

## Run with docker-compose

Optionally set the environment variables in a `.env` file, then:

```
docker-compose up
```

will start the collector, publishing into kafka.

*The Dockerfile sets zkConnect to kafka:2181 to match spotify image setup where kafka and zookeeper are the same container image*
