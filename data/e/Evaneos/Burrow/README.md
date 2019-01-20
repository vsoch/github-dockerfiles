Burrow
======

[![Build Status](https://scrutinizer-ci.com/g/Evaneos/Burrow/badges/build.png?b=master)](https://scrutinizer-ci.com/g/Evaneos/Burrow/build-status/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Evaneos/Burrow/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Evaneos/Burrow/?branch=master)
[![Packagist Version](https://img.shields.io/packagist/v/evaneos/burrow.svg?style=flat-square)](https://packagist.org/packages/evaneos/burrow)
[![Code Coverage](https://scrutinizer-ci.com/g/Evaneos/Burrow/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/Evaneos/Burrow/?branch=master)

Evaneos AMQP library able to use both [php-amqplib](https://github.com/php-amqplib/php-amqplib)
and [pecl amqp C librairy](https://github.com/pdezwart/php-amqp)

Installation
------------
```bash
composer require evaneos/burrow
```
Usage
-----

See examples directory for more details  
To test it, you may use a rabbitmq container, this one feets perfectly 
```bash
docker run -d -p 5672:5672 rabbitmq
```

### Declare an exchange and bind a queue with RabbitMQ
```php
$admin = DriverFactory::getDriver([
    'host' => 'localhost',
    'port' => '5672',
    'user' => 'guest',
    'pwd' => 'guest'
]);
$admin->declareExchange('exchange');
$admin->declareAndBindQueue('exchange', 'my_queue');
```

Asynchronous management
-----------------------

#### Dispatching an async message with RabbitMQ
```php
$driver = DriverFactory::getDriver([
    'host' => 'localhost',
    'port' => '5672',
    'user' => 'guest',
    'pwd' => 'guest'
]);
$publisher = new AsyncPublisher($driver, 'exchange');
$publisher->publish('message', 'routing_key', [ 'meta' => 'data' ]);
```

#### Write a daemon to consume async messages from RabbitMQ
```php
$driver = DriverFactory::getDriver([
    'host' => 'default',
    'port' => '5672',
    'user' => 'guest',
    'pwd' => 'guest'
]);
$handlerBuilder = new HandlerBuilder($driver);
$handler = $handlerBuilder->async()->build(new EchoConsumer());
$daemon = new QueueHandlingDaemon($driver, $handler, 'test');
$worker = new Worker($daemon);
$worker->run();
```

In the command-line, launch both scripts from a different terminal, the message 'my_message', should be displayed in the
worker terminal.

Synchronous management
-----------------------

#### Dispatching an async message with RabbitMQ
```php
$driver = DriverFactory::getDriver([
   'host' => 'default',
   'port' => '5672',
   'user' => 'guest',
   'pwd' => 'guest'
]);
$publisher = new SyncPublisher($driver, 'xchange');
$publisher->publish('my_message', 'routing_key', [ 'meta' => 'data' ]);
```

#### Write a daemon to consume async messages from RabbitMQ
```php
$driver = DriverFactory::getDriver([
   'host' => 'default',
   'port' => '5672',
   'user' => 'guest',
   'pwd' => 'guest'
]);

$handlerBuilder = new HandlerBuilder($driver);
$handler = $handlerBuilder->sync()->build(new ReturnConsumer());
$daemon = new QueueHandlingDaemon($driver, $handler, 'test');
$worker = new Worker($daemon);
$worker->run();
```

In the command-line, launch both scripts from a different terminal, the message 'my_message', should be displayed in the
publisher terminal.

Events
-------

You can add your emitter to subscribe events:
- [DaemonStart](src/Event/DaemonStarted.php)
- [DaemonStopped](src/Event/DaemonStopped.php)
- [MessageReceived](src/Event/MessageReceived.php)
- [MessageConsumed](src/Event/MessageStopped.php)

```php
$emitter = new League\Event\Emitter();
$emitter->addListener(new MyListener());

new QueueHandlingDaemon([..], $emitter);
```

Metrics
-------

Based on events, you can subscribe a built-in metric publisher which will send this metrics:
- `daemon.started` (increment)
- `daemon.stopped` (increment)
- `daemon.message_received` (increment)
- `daemon.message_consumed` (increment)
- `daemon.message_processing_time` (timing)

There is an implementation for StatsD and DogStatsD.

```php
$config = ['host' => 'host', 'port' => 'port'];

// StatsD
$metricService = MetricServiceFactory::create('statsd', $config);
// DogStatsD
$tags = ['service' => 'myService']; // This tags will be sent with all the metrics
$metricService = MetricServiceFactory::create('dogstats', $config, $tags);

$emitter = new League\Event\Emitter();
$emitter->useListenerProvider(new SendMetricListenerProvider($metricService));

new QueueHandlingDaemon([..], $emitter);
```

Examples
--------

All these examples are also available in the `example` directory.


Handlers
--------

You can now use handlers to modify the consumption behaviour. For retro-compatibility reasons, a
`ContinueOnFailureHandler` has been created to reproduce the previous default behaviour. Please, do not use it anymore
 as it is quite dangerous to allow the worker to continue when receiving an error.
 
 To ease the use of the handlers, please build the handler stack using `HandlerBuilder`. 
