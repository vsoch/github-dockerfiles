This directory structure contains the settings and configuration files specific
to your site or sites and is an integral part of multisite configurations.

It is now recommended to place your custom and downloaded extensions in the
/modules, /themes, and /profiles directories located in the Drupal root. The
sites/all/ subdirectory structure, which was recommended in previous versions
of Drupal, is still supported.

See core/INSTALL.txt for information about single-site installation or
multisite configuration.
# Symfony CMF Routing Component

[![Build Status](https://secure.travis-ci.org/symfony-cmf/Routing.png)](http://travis-ci.org/symfony-cmf/Routing)
[![Latest Stable Version](https://poser.pugx.org/symfony-cmf/routing/version.png)](https://packagist.org/packages/symfony-cmf/routing)
[![Total Downloads](https://poser.pugx.org/symfony-cmf/routing/d/total.png)](https://packagist.org/packages/symfony-cmf/routing)

The Symfony CMF Routing component extends the Symfony2 core routing component.
It provides:

 * A ChainRouter to run several routers in parallel
 * A DynamicRouter that can load routes from any database and can generate
   additional information in the route match.

Even though it has Symfony in its name, the Routing component does not need the
full Symfony2 Framework and can be used in standalone projects.

For Symfon2 projects, an optional
[RoutingBundle](https://github.com/symfony-cmf/RoutingBundle)
is also available.

This library is provided by the [Symfony Content Management Framework (CMF) project](http://cmf.symfony.com/)
and licensed under the [MIT License](LICENSE).


## Requirements

* The Symfony Routing component (>= 2.2.0)
* See also the `require` section of [composer.json](composer.json)


## Documentation

For the install guide and reference, see:

* [Routing component documentation](http://symfony.com/doc/master/cmf/components/routing.html)

See also:

* [All Symfony CMF documentation](http://symfony.com/doc/master/cmf/index.html) - complete Symfony CMF reference
* [Symfony CMF Website](http://cmf.symfony.com/) - introduction, live demo, support and community links


## Contributing

Pull requests are welcome. Please see our
[CONTRIBUTING](https://github.com/symfony-cmf/symfony-cmf/blob/master/CONTRIBUTING.md)
guide.

Unit and/or functional tests exist for this component. See the
[Testing documentation](http://symfony.com/doc/master/cmf/components/testing.html)
for a guide to running the tests.

Thanks to
[everyone who has contributed](https://github.com/symfony-cmf/Routing/contributors) already.
HttpKernel Component
====================

HttpKernel provides the building blocks to create flexible and fast HTTP-based
frameworks.

``HttpKernelInterface`` is the core interface of the Symfony2 full-stack
framework:

    interface HttpKernelInterface
    {
        /**
         * Handles a Request to convert it to a Response.
         *
         * @param  Request $request A Request instance
         *
         * @return Response A Response instance
         */
        function handle(Request $request, $type = self::MASTER_REQUEST, $catch = true);
    }

It takes a ``Request`` as an input and should return a ``Response`` as an
output. Using this interface makes your code compatible with all frameworks
using the Symfony2 components. And this will give you many cool features for
free.

Creating a framework based on the Symfony2 components is really easy. Here is
a very simple, but fully-featured framework based on the Symfony2 components:

    $routes = new RouteCollection();
    $routes->add('hello', new Route('/hello', array('_controller' =>
        function (Request $request) {
            return new Response(sprintf("Hello %s", $request->get('name')));
        }
    )));

    $request = Request::createFromGlobals();

    $context = new RequestContext();
    $context->fromRequest($request);

    $matcher = new UrlMatcher($routes, $context);

    $dispatcher = new EventDispatcher();
    $dispatcher->addSubscriber(new RouterListener($matcher));

    $resolver = new ControllerResolver();

    $kernel = new HttpKernel($dispatcher, $resolver);

    $kernel->handle($request)->send();

This is all you need to create a flexible framework with the Symfony2
components.

Want to add an HTTP reverse proxy and benefit from HTTP caching and Edge Side
Includes?

    $kernel = new HttpKernel($dispatcher, $resolver);

    $kernel = new HttpCache($kernel, new Store(__DIR__.'/cache'));

Want to functional test this small framework?

    $client = new Client($kernel);
    $crawler = $client->request('GET', '/hello/Fabien');

    $this->assertEquals('Fabien', $crawler->filter('p > span')->text());

Want nice error pages instead of ugly PHP exceptions?

    $dispatcher->addSubscriber(new ExceptionListener(function (Request $request) {
        $msg = 'Something went wrong! ('.$request->get('exception')->getMessage().')';

        return new Response($msg, 500);
    }));

And that's why the simple looking ``HttpKernelInterface`` is so powerful. It
gives you access to a lot of cool features, ready to be used out of the box,
with no efforts.

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/HttpKernel/
    $ composer.phar install
    $ phpunit
Serializer Component
====================

With the Serializer component its possible to handle serializing data structures,
including object graphs, into array structures or other formats like XML and JSON.
It can also handle deserializing XML and JSON back to object graphs.

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Serializer/
    $ composer.phar install
    $ phpunit
PropertyAccess Component
========================

PropertyAccess reads/writes values from/to object/array graphs using a simple
string notation.

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/PropertyAccess/
    $ composer.phar install
    $ phpunit
DependencyInjection Component
=============================

DependencyInjection manages your services via a robust and flexible Dependency
Injection Container.

Here is a simple example that shows how to register services and parameters:

    use Symfony\Component\DependencyInjection\ContainerBuilder;
    use Symfony\Component\DependencyInjection\Reference;

    $sc = new ContainerBuilder();
    $sc
        ->register('foo', '%foo.class%')
        ->addArgument(new Reference('bar'))
    ;
    $sc->setParameter('foo.class', 'Foo');

    $sc->get('foo');

Method Calls (Setter Injection):

    $sc = new ContainerBuilder();

    $sc
        ->register('bar', '%bar.class%')
        ->addMethodCall('setFoo', array(new Reference('foo')))
    ;
    $sc->setParameter('bar.class', 'Bar');

    $sc->get('bar');

Factory Class:

If your service is retrieved by calling a static method:

    $sc = new ContainerBuilder();

    $sc
        ->register('bar', '%bar.class%')
        ->setFactoryClass('%bar.class%')
        ->setFactoryMethod('getInstance')
        ->addArgument('Aarrg!!!')
    ;
    $sc->setParameter('bar.class', 'Bar');

    $sc->get('bar');

File Include:

For some services, especially those that are difficult or impossible to
autoload, you may need the container to include a file before
instantiating your class.

    $sc = new ContainerBuilder();

    $sc
        ->register('bar', '%bar.class%')
        ->setFile('/path/to/file')
        ->addArgument('Aarrg!!!')
    ;
    $sc->setParameter('bar.class', 'Bar');

    $sc->get('bar');

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/DependencyInjection/
    $ composer.phar install
    $ phpunit
EventDispatcher Component
=========================

The Symfony2 EventDispatcher component implements the Mediator pattern in a
simple and effective way to make your projects truly extensible.

    use Symfony\Component\EventDispatcher\EventDispatcher;
    use Symfony\Component\EventDispatcher\Event;

    $dispatcher = new EventDispatcher();

    $dispatcher->addListener('event_name', function (Event $event) {
        // ...
    });

    $dispatcher->dispatch('event_name');

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/EventDispatcher/
    $ composer.phar install
    $ phpunit
ClassLoader Component
=====================

ClassLoader loads your project classes automatically if they follow some
standard PHP conventions.

The Universal ClassLoader is able to autoload classes that implement the PSR-0
standard or the PEAR naming convention.

First, register the autoloader:

    require_once __DIR__.'/src/Symfony/Component/ClassLoader/UniversalClassLoader.php';

    use Symfony\Component\ClassLoader\UniversalClassLoader;

    $loader = new UniversalClassLoader();
    $loader->register();

Then, register some namespaces with the `registerNamespace()` method:

    $loader->registerNamespace('Symfony', __DIR__.'/src');
    $loader->registerNamespace('Monolog', __DIR__.'/vendor/monolog/src');

The `registerNamespace()` method takes a namespace prefix and a path where to
look for the classes as arguments.

You can also register a sub-namespaces:

    $loader->registerNamespace('Doctrine\\Common', __DIR__.'/vendor/doctrine-common/lib');

The order of registration is significant and the first registered namespace
takes precedence over later registered one.

You can also register more than one path for a given namespace:

    $loader->registerNamespace('Symfony', array(__DIR__.'/src', __DIR__.'/symfony/src'));

Alternatively, you can use the `registerNamespaces()` method to register more
than one namespace at once:

    $loader->registerNamespaces(array(
        'Symfony'          => array(__DIR__.'/src', __DIR__.'/symfony/src'),
        'Doctrine\\Common' => __DIR__.'/vendor/doctrine-common/lib',
        'Doctrine'         => __DIR__.'/vendor/doctrine/lib',
        'Monolog'          => __DIR__.'/vendor/monolog/src',
    ));

For better performance, you can use the APC based version of the universal
class loader:

    require_once __DIR__.'/src/Symfony/Component/ClassLoader/UniversalClassLoader.php';
    require_once __DIR__.'/src/Symfony/Component/ClassLoader/ApcUniversalClassLoader.php';

    use Symfony\Component\ClassLoader\ApcUniversalClassLoader;

    $loader = new ApcUniversalClassLoader('apc.prefix.');

Furthermore, the component provides tools to aggregate classes into a single
file, which is especially useful to improve performance on servers that do not
provide byte caches.

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/ClassLoader/
    $ composer.phar install
    $ phpunit
Process Component
=================

Process executes commands in sub-processes.

In this example, we run a simple directory listing and get the result back:

    use Symfony\Component\Process\Process;

    $process = new Process('ls -lsa');
    $process->setTimeout(3600);
    $process->run();
    if (!$process->isSuccessful()) {
        throw new RuntimeException($process->getErrorOutput());
    }

    print $process->getOutput();

You can think that this is easy to achieve with plain PHP but it's not especially
if you want to take care of the subtle differences between the different platforms.

And if you want to be able to get some feedback in real-time, just pass an
anonymous function to the ``run()`` method and you will get the output buffer
as it becomes available:

    use Symfony\Component\Process\Process;

    $process = new Process('ls -lsa');
    $process->run(function ($type, $buffer) {
        if ('err' === $type) {
            echo 'ERR > '.$buffer;
        } else {
            echo 'OUT > '.$buffer;
        }
    });

That's great if you want to execute a long running command (like rsync-ing files to a
remote server) and give feedback to the user in real-time.

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/XXX/
    $ composer.phar install --dev
    $ phpunit
Yaml Component
==============

YAML implements most of the YAML 1.2 specification.

    use Symfony\Component\Yaml\Yaml;

    $array = Yaml::parse($file);

    print Yaml::dump($array);

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Yaml/
    $ composer.phar install
    $ phpunit
HttpFoundation Component
========================

HttpFoundation defines an object-oriented layer for the HTTP specification.

It provides an abstraction for requests, responses, uploaded files, cookies,
sessions, ...

In this example, we get a Request object from the current PHP global
variables:

    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\HttpFoundation\Response;

    $request = Request::createFromGlobals();
    echo $request->getPathInfo();

You can also create a Request directly -- that's interesting for unit testing:

    $request = Request::create('/?foo=bar', 'GET');
    echo $request->getPathInfo();

And here is how to create and send a Response:

    $response = new Response('Not Found', 404, array('Content-Type' => 'text/plain'));
    $response->send();

The Request and the Response classes have many other methods that implement
the HTTP specification.

Loading
-------

If you are not using Composer but are using PHP 5.3.x, you must add the following to your autoloader:

    // SessionHandlerInterface
    if (!interface_exists('SessionHandlerInterface')) {
        $loader->registerPrefixFallback(__DIR__.'/../vendor/symfony/src/Symfony/Component/HttpFoundation/Resources/stubs');
    }

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/HttpFoundation/
    $ composer.phar install
    $ phpunit
Debug Component
===============

Debug provides tools to make debugging easier.

Enabling all debug tools is as easy as calling the `enable()` method on the
main `Debug` class:

    use Symfony\Component\Debug\Debug;

    Debug::enable();

You can also use the tools individually:

    use Symfony\Component\Debug\ErrorHandler;
    use Symfony\Component\Debug\ExceptionHandler;

    error_reporting(-1);

    ErrorHandler::register($errorReportingLevel);
    if ('cli' !== php_sapi_name()) {
        ExceptionHandler::register();
    } elseif (!ini_get('log_errors') || ini_get('error_log')) {
        ini_set('display_errors', 1);
    }

Note that the `Debug::enable()` call also registers the debug class loader
from the Symfony ClassLoader component when available.

This component can optionally take advantage of the features of the HttpKernel
and HttpFoundation components.

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Debug/
    $ composer.phar install --dev
    $ phpunit
Routing Component
=================

Routing associates a request with the code that will convert it to a response.

The example below demonstrates how you can set up a fully working routing
system:

    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\Routing\Matcher\UrlMatcher;
    use Symfony\Component\Routing\RequestContext;
    use Symfony\Component\Routing\RouteCollection;
    use Symfony\Component\Routing\Route;

    $routes = new RouteCollection();
    $routes->add('hello', new Route('/hello', array('controller' => 'foo')));

    $context = new RequestContext();

    // this is optional and can be done without a Request instance
    $context->fromRequest(Request::createFromGlobals());

    $matcher = new UrlMatcher($routes, $context);

    $parameters = $matcher->match('/hello');

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Routing/
    $ composer.phar install
    $ phpunit
Validator Component
===================

This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

Usage
-----

The component provides "validation constraints", which are simple objects
containing the rules for the validation. Let's validate a simple string
as an example:

    use Symfony\Component\Validator\Validation;
    use Symfony\Component\Validator\Constraints\Length;

    $validator = Validation::createValidator();

    $violations = $validator->validateValue('Bernhard', new Length(array('min' => 10)));

This validation will fail because the given string is shorter than ten
characters. The precise errors, here called "constraint violations",  are
returned by the validator. You can analyze these or return them to the user.
If the violation list is empty, validation succeeded.

Validation of arrays is possible using the `Collection` constraint:

    use Symfony\Component\Validator\Validation;
    use Symfony\Component\Validator\Constraints as Assert;

    $validator = Validation::createValidator();

    $constraint = new Assert\Collection(array(
        'name' => new Assert\Collection(array(
            'first_name' => new Assert\Length(array('min' => 101)),
            'last_name'  => new Assert\Length(array('min' => 1)),
        )),
        'email'    => new Assert\Email(),
        'simple'   => new Assert\Length(array('min' => 102)),
        'gender'   => new Assert\Choice(array(3, 4)),
        'file'     => new Assert\File(),
        'password' => new Assert\Length(array('min' => 60)),
    ));

    $violations = $validator->validateValue($input, $constraint);

Again, the validator returns the list of violations.

Validation of objects is possible using "constraint mapping". With such
a mapping you can put constraints onto properties and objects of classes.
Whenever an object of this class is validated, its properties and
method results are matched against the constraints.

    use Symfony\Component\Validator\Validation;
    use Symfony\Component\Validator\Constraints as Assert;

    class User
    {
        /**
         * @Assert\Length(min = 3)
         * @Assert\NotBlank
         */
        private $name;

        /**
         * @Assert\Email
         * @Assert\NotBlank
         */
        private $email;

        public function __construct($name, $email)
        {
            $this->name = $name;
            $this->email = $email;
        }

        /**
         * @Assert\True(message = "The user should have a Google Mail account")
         */
        public function isGmailUser()
        {
            return false !== strpos($this->email, '@gmail.com');
        }
    }

    $validator = Validation::createValidatorBuilder()
        ->enableAnnotationMapping()
        ->getValidator();

    $user = new User('John Doe', 'john@example.com');

    $violations = $validator->validate($user);

This example uses the annotation support of Doctrine Common to
map constraints to properties and methods. You can also map constraints
using XML, YAML or plain PHP, if you dislike annotations or don't want
to include Doctrine. Check the documentation for more information about
these drivers.

Resources
---------

Silex integration:

https://github.com/fabpot/Silex/blob/master/src/Silex/Provider/ValidatorServiceProvider.php

Documentation:

http://symfony.com/doc/2.4/book/validation.html

JSR-303 Specification:

http://jcp.org/en/jsr/detail?id=303

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Validator/
    $ composer.phar install
    $ phpunit
# PHP_CodeCoverage

**PHP_CodeCoverage** is a library that provides collection, processing, and rendering functionality for PHP code coverage information.

## Requirements

* PHP_CodeCoverage 1.2 requires PHP 5.3.3 (or later) but PHP 5.4.7 (or later) is highly recommended.
* [Xdebug](http://xdebug.org/) 2.0.5 (or later) is required but Xdebug 2.2.1 (or later) is highly recommended.

## Installation

You can use the [PEAR Installer](http://pear.php.net/manual/en/guide.users.commandline.cli.php) or [Composer](http://getcomposer.org/) to download and install PHP_CodeCoverage as well as its dependencies

### PEAR Installer

Depending on your OS distribution and/or your PHP environment, you may need to install PEAR or update your existing PEAR installation before you can proceed with the following instructions. `sudo pear upgrade PEAR` usually suffices to upgrade an existing PEAR installation. The [PEAR Manual ](http://pear.php.net/manual/en/installation.getting.php) explains how to perform a fresh installation of PEAR.

The following two commands (which you may have to run as `root`) are all that is required to install PHP_CodeCoverage using the PEAR Installer:

    pear config-set auto_discover 1
    pear install pear.phpunit.de/PHP_CodeCoverage

After the installation you can find the PHP_CodeCoverage source files inside your local PEAR directory; the path is usually `/usr/lib/php/PHP/CodeCoverage`.

### Composer

To add PHP_CodeCoverage as a local, per-project dependency to your project, simply add a dependency on `phpunit/php-code-coverage` to your project's `composer.json` file. Here is a minimal example of a `composer.json` file that just defines a dependency on PHP_CodeCoverage 1.2:

    {
        "require": {
            "phpunit/php-code-coverage": ">=1.2.10,<1.3.0"
        }
    }

## Using the PHP_CodeCoverage API

```php
<?php
require 'PHP/CodeCoverage/Autoload.php';

$coverage = new PHP_CodeCoverage;
$coverage->start('<name of test>');

// ...

$coverage->stop();

$writer = new PHP_CodeCoverage_Report_Clover;
$writer->process($coverage, '/tmp/clover.xml');

$writer = new PHP_CodeCoverage_Report_HTML;
$writer->process($coverage, '/tmp/code-coverage-report');
```# PHPUnit

PHPUnit is the de-facto standard for unit testing in PHP projects. It provides both a framework that makes the writing of tests easy as well as the functionality to easily run the tests and analyse their results.

[![Build Status](https://travis-ci.org/sebastianbergmann/phpunit.png?branch=3.7)](https://travis-ci.org/sebastianbergmann/phpunit)

## Requirements

* PHPUnit 3.7 requires PHP 5.3.3 (or later) but PHP 5.4.6 (or later) is highly recommended.
* [PHP_CodeCoverage](http://github.com/sebastianbergmann/php-code-coverage), the library that is used by PHPUnit to collect and process code coverage information, depends on [Xdebug](http://xdebug.org/) 2.0.5 (or later) but Xdebug 2.2.1 (or later) is highly recommended.

## Installation

There are three supported ways of installing PHPUnit.

You can use the [PEAR Installer](http://pear.php.net/manual/en/guide.users.commandline.cli.php) or [Composer](http://getcomposer.org/) to download and install PHPUnit as well as its dependencies. You can also download a [PHP Archive (PHAR)](http://php.net/phar) of PHPUnit that has all required (as well as some optional) dependencies of PHPUnit bundled in a single file.

### PEAR Installer

The following two commands (which you may have to run as `root`) are all that is required to install PHPUnit using the PEAR Installer:

    pear config-set auto_discover 1
    pear install pear.phpunit.de/PHPUnit

### Composer

To add PHPUnit as a local, per-project dependency to your project, simply add a dependency on `phpunit/phpunit` to your project's `composer.json` file. Here is a minimal example of a `composer.json` file that just defines a development-time dependency on PHPUnit 3.7:

    {
        "require-dev": {
            "phpunit/phpunit": "3.7.*"
        }
    }

### PHP Archive (PHAR)

    wget http://pear.phpunit.de/get/phpunit.phar
    chmod +x phpunit.phar

## Documentation

The documentation for PHPUnit is available in different formats:

* [English, multiple HTML files](http://www.phpunit.de/manual/3.7/en/index.html)
* [English, single HTML file](http://www.phpunit.de/manual/3.7/en/phpunit-book.html)
* [English, PDF](http://www.phpunit.de/manual/3.7/en/phpunit-book.pdf)
* [English, ePub](http://www.phpunit.de/manual/3.7/en/phpunit-book.epub)
* [Brazilian Portuguese, multiple HTML files](http://www.phpunit.de/manual/3.7/pt_br/index.html)
* [Brazilian Portuguese, single HTML file](http://www.phpunit.de/manual/3.7/pt_br/phpunit-book.html)
* [Brazilian Portuguese, PDF](http://www.phpunit.de/manual/3.7/pt_br/phpunit-book.pdf)
* [Brazilian Portuguese, ePub](http://www.phpunit.de/manual/3.7/pt_br/phpunit-book.epub)
* [French, multiple HTML files](http://www.phpunit.de/manual/3.7/fr/index.html)
* [French, single HTML file](http://www.phpunit.de/manual/3.7/fr/phpunit-book.html)
* [French, PDF](http://www.phpunit.de/manual/3.7/fr/phpunit-book.pdf)
* [French, ePub](http://www.phpunit.de/manual/3.7/fr/phpunit-book.epub)
* [Japanese, multiple HTML files](http://www.phpunit.de/manual/3.7/ja/index.html)
* [Japanese, single HTML file](http://www.phpunit.de/manual/3.7/ja/phpunit-book.html)
* [Japanese, PDF](http://www.phpunit.de/manual/3.7/ja/phpunit-book.pdf)
* [Japanese, ePub](http://www.phpunit.de/manual/3.7/ja/phpunit-book.epub)

## IRC

The [#phpunit channel on the Freenode IRC network](irc://irc.freenode.net/phpunit) is a place to chat about PHPUnit.

## List of Contributors

Thanks to everyone who has contributed to PHPUnit! You can find a detailed list of contributors on every PHPUnit related package on GitHub. This list shows only the major components:

* [PHPUnit](https://github.com/sebastianbergmann/phpunit/graphs/contributors)
* [PHP_CodeCoverage](https://github.com/sebastianbergmann/php-code-coverage/graphs/contributors)
* [PHPUnit_MockObject](https://github.com/sebastianbergmann/phpunit-mock-objects/graphs/contributors)

A very special thanks to everyone who has contributed to the documentation and helps maintaining the translations:

* [PHPUnit Documentation](https://github.com/sebastianbergmann/phpunit-documentation/graphs/contributors)

Please refer to [CONTRIBUTING.md](https://github.com/sebastianbergmann/phpunit/blob/master/CONTRIBUTING.md) for information on how to contribute to PHPUnit and its related projects.
PHP_Timer
=========

Installation
------------

PHP_Timer should be installed using the [PEAR Installer](http://pear.php.net/). This installer is the backbone of PEAR, which provides a distribution system for PHP packages, and is shipped with every release of PHP since version 4.3.0.

The PEAR channel (`pear.phpunit.de`) that is used to distribute PHP_Timer needs to be registered with the local PEAR environment:

    sb@ubuntu ~ % pear channel-discover pear.phpunit.de
    Adding Channel "pear.phpunit.de" succeeded
    Discovery of channel "pear.phpunit.de" succeeded

This has to be done only once. Now the PEAR Installer can be used to install packages from the PHPUnit channel:

    sb@vmware ~ % pear install phpunit/PHP_Timer
    downloading PHP_Timer-1.0.0.tgz ...
    Starting to download PHP_Timer-1.0.0.tgz (2,536 bytes)
    ....done: 2,536 bytes
    install ok: channel://pear.phpunit.de/PHP_Timer-1.0.0

After the installation you can find the PHP_Timer source files inside your local PEAR directory; the path is usually `/usr/lib/php/PHP`.
File_Iterator
=============

Installation
------------

File_Iterator should be installed using the [PEAR Installer](http://pear.php.net/). This installer is the backbone of PEAR, which provides a distribution system for PHP packages, and is shipped with every release of PHP since version 4.3.0.

The PEAR channel (`pear.phpunit.de`) that is used to distribute File_Iterator needs to be registered with the local PEAR environment:

    sb@ubuntu ~ % pear channel-discover pear.phpunit.de
    Adding Channel "pear.phpunit.de" succeeded
    Discovery of channel "pear.phpunit.de" succeeded

This has to be done only once. Now the PEAR Installer can be used to install packages from the PHPUnit channel:

    sb@vmware ~ % pear install phpunit/File_Iterator
    downloading File_Iterator-1.1.1.tgz ...
    Starting to download File_Iterator-1.1.1.tgz (3,173 bytes)
    ....done: 3,173 bytes
    install ok: channel://pear.phpunit.de/File_Iterator-1.1.1

After the installation you can find the File_Iterator source files inside your local PEAR directory; the path is usually `/usr/lib/php/File`.
Text_Template
=============

Installation
------------

Text_Template should be installed using the [PEAR Installer](http://pear.php.net/). This installer is the backbone of PEAR, which provides a distribution system for PHP packages, and is shipped with every release of PHP since version 4.3.0.

The PEAR channel (`pear.phpunit.de`) that is used to distribute Text_Template needs to be registered with the local PEAR environment:

    sb@ubuntu ~ % pear channel-discover pear.phpunit.de
    Adding Channel "pear.phpunit.de" succeeded
    Discovery of channel "pear.phpunit.de" succeeded

This has to be done only once. Now the PEAR Installer can be used to install packages from the PHPUnit channel:

    sb@vmware ~ % pear install phpunit/Text_Template
    downloading Text_Template-1.0.0.tgz ...
    Starting to download Text_Template-1.0.0.tgz (2,493 bytes)
    ....done: 2,493 bytes
    install ok: channel://pear.phpunit.de/Text_Template-1.0.0

After the installation you can find the Text_Template source files inside your local PEAR directory; the path is usually `/usr/lib/php/Text`.
PHP_TokenStream
===============

Installation
------------

PHP_TokenStream should be installed using the [PEAR Installer](http://pear.php.net/). This installer is the backbone of PEAR, which provides a distribution system for PHP packages, and is shipped with every release of PHP since version 4.3.0.

The PEAR channel (`pear.phpunit.de`) that is used to distribute PHP_TokenStream needs to be registered with the local PEAR environment:

    sb@ubuntu ~ % pear channel-discover pear.phpunit.de
    Adding Channel "pear.phpunit.de" succeeded
    Discovery of channel "pear.phpunit.de" succeeded

This has to be done only once. Now the PEAR Installer can be used to install packages from the PHPUnit channel:

    sb@ubuntu tokenstream % pear install phpunit/PHP_TokenStream-beta
    downloading PHP_TokenStream-0.9.1.tgz ...
    Starting to download PHP_TokenStream-0.9.1.tgz (5,113 bytes)
    ...done: 5,113 bytes
    install ok: channel://pear.phpunit.de/PHP_TokenStream-0.9.1

After the installation you can find the PHP_TokenStream source files inside your local PEAR directory; the path is usually `/usr/lib/php/PHP`.
# Assetic [![Build Status](https://travis-ci.org/kriswallsmith/assetic.png?branch=master)](https://travis-ci.org/kriswallsmith/assetic) ![project status](http://stillmaintained.com/kriswallsmith/assetic.png) #

Assetic is an asset management framework for PHP.

``` php
<?php

use Assetic\Asset\AssetCollection;
use Assetic\Asset\FileAsset;
use Assetic\Asset\GlobAsset;

$js = new AssetCollection(array(
    new GlobAsset('/path/to/js/*'),
    new FileAsset('/path/to/another.js'),
));

// the code is merged when the asset is dumped
echo $js->dump();
```

Assets
------

An Assetic asset is something with filterable content that can be loaded and
dumped. An asset also includes metadata, some of which can be manipulated and
some of which is immutable.

| **Property** | **Accessor**    | **Mutator**   |
|--------------|-----------------|---------------|
| content      | getContent      | setContent    |
| mtime        | getLastModified | n/a           |
| source root  | getSourceRoot   | n/a           |
| source path  | getSourcePath   | n/a           |
| target path  | getTargetPath   | setTargetPath |

Filters
-------

Filters can be applied to manipulate assets.

``` php
<?php

use Assetic\Asset\AssetCollection;
use Assetic\Asset\FileAsset;
use Assetic\Asset\GlobAsset;
use Assetic\Filter\LessFilter;
use Assetic\Filter\Yui;

$css = new AssetCollection(array(
    new FileAsset('/path/to/src/styles.less', array(new LessFilter())),
    new GlobAsset('/path/to/css/*'),
), array(
    new Yui\CssCompressorFilter('/path/to/yuicompressor.jar'),
));

// this will echo CSS compiled by LESS and compressed by YUI
echo $css->dump();
```

The filters applied to the collection will cascade to each asset leaf if you
iterate over it.

``` php
<?php

foreach ($css as $leaf) {
    // each leaf is compressed by YUI
    echo $leaf->dump();
}
```

The core provides the following filters in the `Assetic\Filter` namespace:

 * `CoffeeScriptFilter`: compiles CoffeeScript into Javascript
 * `CompassFilter`: Compass CSS authoring framework
 * `CssEmbedFilter`: embeds image data in your stylesheets
 * `CssImportFilter`: inlines imported stylesheets
 * `CssMinFilter`: minifies CSS
 * `CssRewriteFilter`: fixes relative URLs in CSS assets when moving to a new URL
 * `DartFilter`: compiles Javascript using dart2js
 * `EmberPrecompileFilter`: precompiles Handlebars templates into Javascript for use in the Ember.js framework
 * `GoogleClosure\CompilerApiFilter`: compiles Javascript using the Google Closure Compiler API
 * `GoogleClosure\CompilerJarFilter`: compiles Javascript using the Google Closure Compiler JAR
 * `GssFilter`: compliles CSS using the Google Closure Stylesheets Compiler
 * `HandlebarsFilter`: compiles Handlebars templates into Javascript
 * `JpegoptimFilter`: optimize your JPEGs
 * `JpegtranFilter`: optimize your JPEGs
 * `JSMinFilter`: minifies Javascript
 * `JSMinPlusFilter`: minifies Javascript
 * `LessFilter`: parses LESS into CSS (using less.js with node.js)
 * `LessphpFilter`: parses LESS into CSS (using lessphp)
 * `OptiPngFilter`: optimize your PNGs
 * `PackagerFilter`: parses Javascript for packager tags
 * `PackerFilter`: compresses Javascript using Dean Edwards's Packer
 * `PhpCssEmbedFilter`: embeds image data in your stylesheet
 * `PngoutFilter`: optimize your PNGs
 * `Sass\SassFilter`: parses SASS into CSS
 * `Sass\ScssFilter`: parses SCSS into CSS
 * `ScssphpFilter`: parses SCSS using scssphp
 * `SprocketsFilter`: Sprockets Javascript dependency management
 * `StylusFilter`: parses STYL into CSS
 * `TypeScriptFilter`: parses TypeScript into Javascript
 * `UglifyCssFilter`: minifies CSS
 * `UglifyJs2Filter`: minifies Javascript
 * `UglifyJsFilter`: minifies Javascript
 * `Yui\CssCompressorFilter`: compresses CSS using the YUI compressor
 * `Yui\JsCompressorFilter`: compresses Javascript using the YUI compressor

Asset Manager
-------------

An asset manager is provided for organizing assets.

``` php
<?php

use Assetic\AssetManager;
use Assetic\Asset\FileAsset;
use Assetic\Asset\GlobAsset;

$am = new AssetManager();
$am->set('jquery', new FileAsset('/path/to/jquery.js'));
$am->set('base_css', new GlobAsset('/path/to/css/*'));
```

The asset manager can also be used to reference assets to avoid duplication.

``` php
<?php

use Assetic\Asset\AssetCollection;
use Assetic\Asset\AssetReference;
use Assetic\Asset\FileAsset;

$am->set('my_plugin', new AssetCollection(array(
    new AssetReference($am, 'jquery'),
    new FileAsset('/path/to/jquery.plugin.js'),
)));
```

Filter Manager
--------------

A filter manager is also provided for organizing filters.

``` php
<?php

use Assetic\FilterManager;
use Assetic\Filter\Sass\SassFilter;
use Assetic\Filter\Yui;

$fm = new FilterManager();
$fm->set('sass', new SassFilter('/path/to/parser/sass'));
$fm->set('yui_css', new Yui\CssCompressorFilter('/path/to/yuicompressor.jar'));
```

Asset Factory
-------------

If you'd rather not create all these objects by hand, you can use the asset
factory, which will do most of the work for you.

``` php
<?php

use Assetic\Factory\AssetFactory;

$factory = new AssetFactory('/path/to/asset/directory/');
$factory->setAssetManager($am);
$factory->setFilterManager($fm);
$factory->setDebug(true);

$css = $factory->createAsset(array(
    '@reset',         // load the asset manager's "reset" asset
    'css/src/*.scss', // load every scss files from "/path/to/asset/directory/css/src/"
), array(
    'scss',           // filter through the filter manager's "scss" filter
    '?yui_css',       // don't use this filter in debug mode
));

echo $css->dump();
```

Prefixing a filter name with a question mark, as `yui_css` is here, will cause
that filter to be omitted when the factory is in debug mode.

Caching
-------

A simple caching mechanism is provided to avoid unnecessary work.

``` php
<?php

use Assetic\Asset\AssetCache;
use Assetic\Asset\FileAsset;
use Assetic\Cache\FilesystemCache;
use Assetic\Filter\Yui;

$yui = new Yui\JsCompressorFilter('/path/to/yuicompressor.jar');
$js = new AssetCache(
    new FileAsset('/path/to/some.js', array($yui)),
    new FilesystemCache('/path/to/cache')
);

// the YUI compressor will only run on the first call
$js->dump();
$js->dump();
$js->dump();
```

Cache Busting
-------------

You can use the CacheBustingWorker to provide unique names.

Two strategies are provided: CacheBustingWorker::STRATEGY_CONTENT (content based), CacheBustingWorker::STRATEGY_MODIFICATION (modification time based)

``` php
<?php

use Assetic\Factory\AssetFactory;
use Assetic\Factory\Worker\CacheBustingWorker;

$factory = new AssetFactory('/path/to/asset/directory/');
$factory->setAssetManager($am);
$factory->setFilterManager($fm);
$factory->setDebug(true);
$factory->addWorker(new CacheBustingWorker(CacheBustingWorker::STRATEGY_CONTENT));

$css = $factory->createAsset(array(
    '@reset',         // load the asset manager's "reset" asset
    'css/src/*.scss', // load every scss files from "/path/to/asset/directory/css/src/"
), array(
    'scss',           // filter through the filter manager's "scss" filter
    '?yui_css',       // don't use this filter in debug mode
));

echo $css->dump();
```

Static Assets
-------------

Alternatively you can just write filtered assets to your web directory and be
done with it.

``` php
<?php

use Assetic\AssetWriter;

$writer = new AssetWriter('/path/to/web');
$writer->writeManagerAssets($am);
```

Twig
----

To use the Assetic [Twig][3] extension you must register it to your Twig
environment:

``` php
<?php

$twig->addExtension(new AsseticExtension($factory, $debug));
```

Once in place, the extension exposes a stylesheets and a javascripts tag with a syntax similar
to what the asset factory uses:

``` html+jinja
{% stylesheets '/path/to/sass/main.sass' filter='sass,?yui_css' output='css/all.css' %}
    <link href="{{ asset_url }}" type="text/css" rel="stylesheet" />
{% endstylesheets %}
```

This example will render one `link` element on the page that includes a URL
where the filtered asset can be found.

When the extension is in debug mode, this same tag will render multiple `link`
elements, one for each asset referenced by the `css/src/*.sass` glob. The
specified filters will still be applied, unless they are marked as optional
using the `?` prefix.

This behavior can also be triggered by setting a `debug` attribute on the tag:

``` html+jinja
{% stylesheets 'css/*' debug=true %} ... {% stylesheets %}
```

These assets need to be written to the web directory so these URLs don't
return 404 errors.

``` php
<?php

use Assetic\AssetWriter;
use Assetic\Extension\Twig\TwigFormulaLoader;
use Assetic\Extension\Twig\TwigResource;
use Assetic\Factory\LazyAssetManager;

$am = new LazyAssetManager($factory);

// enable loading assets from twig templates
$am->setLoader('twig', new TwigFormulaLoader($twig));

// loop through all your templates
foreach ($templates as $template) {
    $resource = new TwigResource($twigLoader, $template);
    $am->addResource($resource, 'twig');
}

$writer = new AssetWriter('/path/to/web');
$writer->writeManagerAssets($am);
```

---

Assetic is based on the Python [webassets][1] library (available on
[GitHub][2]).

[1]: http://elsdoerfer.name/docs/webassets
[2]: https://github.com/miracle2k/webassets
[3]: http://twig.sensiolabs.org
# Doctrine Inflector

Doctrine Inflector is a small library that can perform string manipulations
with regard to upper-/lowercase and singular/plural forms of words.
# Doctrine Annotations

[![Build Status](https://travis-ci.org/doctrine/annotations.png?branch=master)](https://travis-ci.org/doctrine/annotations)

Docblock Annotations Parser library (extracted from Doctrine Common).

## Changelog

### v1.1

* Add Exception when ZendOptimizer+ or Opcache is configured to drop comments
# Doctrine Lexer

Base library for a lexer that can be used in Top-Down, Recursive Descent Parsers.

This lexer is used in Doctrine Annotations and in Doctrine ORM (DQL).
# Doctrine Cache

Cache component extracted from the Doctrine Common project.
# Doctrine Collections

Collections Abstraction library
# Doctrine Common

[![Build Status](https://secure.travis-ci.org/doctrine/common.png)](http://travis-ci.org/doctrine/common)

The Doctrine Common project is a library that provides extensions to core PHP functionality.

## More resources:

* [Website](http://www.doctrine-project.org)
* [Documentation](http://www.doctrine-project.org/projects/common/current/docs/en)
* [Issue Tracker](http://www.doctrine-project.org/jira/browse/DCOM)
* [Downloads](http://github.com/doctrine/common/downloads)
# Running the Doctrine 2 Testsuite

## Running tests

Execute PHPUnit in the root folder of your doctrine-common clone.

    phpunit

## Testing Lock-Support

The Lock support in Doctrine 2 is tested using Gearman, which allows to run concurrent tasks in parallel.
Install Gearman with PHP as follows:

1. Go to http://www.gearman.org and download the latest Gearman Server
2. Compile it and then call ldconfig
3. Start it up "gearmand -vvvv"
4. Install pecl/gearman by calling "gearman-beta"

You can then go into tests/ and start up two workers:

    php Doctrine/Tests/ORM/Functional/Locking/LockAgentWorker.php

Then run the locking test-suite:

    phpunit --configuration <myconfig.xml> Doctrine/Tests/ORM/Functional/Locking/GearmanLockTest.php

This can run considerable time, because it is using sleep() to test for the timing ranges of locks.EasyRdf
=======
EasyRdf is a PHP library designed to make it easy to consume and produce [RDF].
It was designed for use in mixed teams of experienced and inexperienced RDF
developers. It is written in Object Oriented PHP and has been tested
extensively using PHPUnit.

After parsing EasyRdf builds up a graph of PHP objects that can then be walked
around to get the data to be placed on the page. Dump methods are available to
inspect what data is available during development.

Data is typically loaded into a [EasyRdf_Graph] object from source RDF
documents, loaded from the web via HTTP. The [EasyRdf_GraphStore] class
simplifies loading and saving data to a SPARQL 1.1 Graph Store.

SPARQL queries can be made over HTTP to a Triplestore using the
[EasyRdf_Sparql_Client] class. SELECT and ASK queries will return an
[EasyRdf_Sparql_Result] object and CONSTRUCT and DESCRIBE queries will return
an [EasyRdf_Graph] object.

### Example ###

    $foaf = new EasyRdf_Graph("http://njh.me/foaf.rdf");
    $foaf->load();
    $me = $foaf->primaryTopic();
    echo "My name is: ".$me->get('foaf:name')."\n";


Downloads
---------

The latest _stable_ version of EasyRdf can be [downloaded from the EasyRdf website].


Links
-----

* [EasyRdf Homepage](http://www.easyrdf.org/)
* [API documentation](http://www.easyrdf.org/docs/api)
* [Change Log](http://github.com/njh/easyrdf/blob/master/CHANGELOG.md)
* Source Code: <http://github.com/njh/easyrdf>
* Issue Tracker: <http://github.com/njh/easyrdf/issues>


Requirements
------------

* PHP 5.2.8 or higher


Features
--------

* API documentation written in phpdoc
* Extensive unit tests written using phpunit
  * Automated testing against PHP 5.2, 5.3 and 5.4
* Built-in parsers and serialisers: RDF/JSON, N-Triples, RDF/XML, Turtle
* Optional parsing support for: [ARC2], [Redland Bindings], [rapper]
* Optional support for [Zend_Http_Client]
* No required external dependancies upon other libraries (PEAR, Zend, etc...)
* Complies with Zend Framework coding style.
* Type mapper - resources of type foaf:Person can be mapped into PHP object of class Foaf_Person
* Support for visualisation of graphs using [GraphViz]
* Comes with a number of examples


More Examples
-------------

* [artistinfo.php](https://github.com/njh/easyrdf/blob/master/examples/artistinfo.php#slider) - Example of mapping an RDF class type to a PHP Class
* [basic.php](https://github.com/njh/easyrdf/blob/master/examples/basic.php#slider) - Basic "Hello World" type example
* [basic_sparql.php](https://github.com/njh/easyrdf/blob/master/examples/basic_sparql.php#slider) - Example of making a SPARQL SELECT query
* [converter.php](https://github.com/njh/easyrdf/blob/master/examples/converter.php#slider) - Convert RDF from one format to another
* [dump.php](https://github.com/njh/easyrdf/blob/master/examples/dump.php#slider) - Display the contents of a graph
* [foafinfo.php](https://github.com/njh/easyrdf/blob/master/examples/foafinfo.php#slider) - Display the basic information in a FOAF document
* [foafmaker.php](https://github.com/njh/easyrdf/blob/master/examples/foafmaker.php#slider) - Construct a FOAF document with a choice of serialisations
* [graph_direct.php](https://github.com/njh/easyrdf/blob/master/examples/graph_direct.php#slider) - Example of using EasyRdf_Graph directly without EasyRdf_Resource
* [graphstore.php](https://github.com/njh/easyrdf/blob/master/examples/graphstore.php#slider) - Store and retrieve data from a SPARQL 1.1 Graph Store
* [graphviz.php](https://github.com/njh/easyrdf/blob/master/examples/graphviz.php#slider) - GraphViz rendering example
* [html_tag_helpers.php](https://github.com/njh/easyrdf/blob/master/examples/html_tag_helpers.php#slider) - Rails Style html tag helpers to make the EasyRdf examples simplier
* [httpget.php](https://github.com/njh/easyrdf/blob/master/examples/httpget.php#slider) - No RDF, just test EasyRdf_Http_Client
* [serialise.php](https://github.com/njh/easyrdf/blob/master/examples/serialise.php#slider) - Basic serialisation example
* [sparql_queryform.php](https://github.com/njh/easyrdf/blob/master/examples/sparql_queryform.php#slider) - Form to submit SPARQL queries and display the result
* [uk_postcode.php](https://github.com/njh/easyrdf/blob/master/examples/uk_postcode.php#slider) - Example of resolving UK postcodes using uk-postcodes.com
* [villages.php](https://github.com/njh/easyrdf/blob/master/examples/villages.php#slider) - Fetch and information about villages in Fife from dbpedialite.org
* [zend_framework.php](https://github.com/njh/easyrdf/blob/master/examples/zend_framework.php#slider) - Example of using Zend_Http_Client and Zend_Loader_Autoloader with EasyRdf



Licensing
---------

The EasyRdf library and tests are licensed under the [BSD-3-Clause] license.
The examples are in the public domain, for more information see [UNLICENSE].



[EasyRdf_Graph]:http://www.easyrdf.org/docs/api/EasyRdf_Graph.html
[EasyRdf_GraphStore]:http://www.easyrdf.org/docs/api/EasyRdf_GraphStore.html
[EasyRdf_Sparql_Client]:http://www.easyrdf.org/docs/api/EasyRdf_Sparql_Client.html
[EasyRdf_Sparql_Result]:http://www.easyrdf.org/docs/api/EasyRdf_Sparql_Result.html

[ARC2]:http://github.com/semsol/arc2/
[BSD-3-Clause]:http://www.opensource.org/licenses/BSD-3-Clause
[downloaded from the EasyRdf website]:http://www.easyrdf.org/downloads
[GraphViz]:http://www.graphviz.org/
[rapper]:http://librdf.org/raptor/rapper.html
[RDF]:http://en.wikipedia.org/wiki/Resource_Description_Framework
[Redland Bindings]:http://librdf.org/bindings/
[SPARQL 1.1 query language]:http://www.w3.org/TR/sparql11-query/
[UNLICENSE]:http://unlicense.org/
[Zend_Http_Client]:http://framework.zend.com/manual/en/zend.http.client.html
PSR Log
=======

This repository holds all interfaces/classes/traits related to
[PSR-3](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md).

Note that this is not a logger of its own. It is merely an interface that
describes a logger. See the specification for more details.

Usage
-----

If you need a logger, you can use the interface like this:

```php
<?php

use Psr\Log\LoggerInterface;

class Foo
{
    private $logger;

    public function __construct(LoggerInterface $logger = null)
    {
        $this->logger = $logger;
    }

    public function doSomething()
    {
        if ($this->logger) {
            $this->logger->info('Doing work');
        }

        // do something useful
    }
}
```

You can then pick one of the implementations of the interface to get a logger.

If you want to implement the interface, you can require this package and
implement `Psr\Log\LoggerInterface` in your code. Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md)
for details.
Stdlib Component from ZF2
=========================

This is the Stdlib component for ZF2.

- File issues at https://github.com/zendframework/zf2/issues
- Create pull requests against https://github.com/zendframework/zf2
- Documentation is at http://framework.zend.com/docs

LICENSE
-------

The files in this archive are released under the [Zend Framework
license](http://framework.zend.com/license), which is a 3-clause BSD license.

Escaper Component from ZF2
==========================

This is the Escaper component for ZF2.

- File issues at https://github.com/zendframework/zf2/issues
- Create pull requests against https://github.com/zendframework/zf2
- Documentation is at http://framework.zend.com/docs

LICENSE
-------

The files in this archive are released under the [Zend Framework
license](http://framework.zend.com/license), which is a 3-clause BSD license.

Feed Component from ZF2
=======================

This is the Feed component for ZF2.

- File issues at https://github.com/zendframework/zf2/issues
- Create pull requests against https://github.com/zendframework/zf2
- Documentation is at http://framework.zend.com/docs

LICENSE
-------

The files in this archive are released under the [Zend Framework
license](http://framework.zend.com/license), which is a 3-clause BSD license.

# Gliph

[![Build Status](https://travis-ci.org/sdboyer/gliph.png?branch=php53)](https://travis-ci.org/sdboyer/gliph)
[![Latest Stable Version](https://poser.pugx.org/sdboyer/gliph/v/stable.png)](https://packagist.org/packages/sdboyer/gliph)

Gliph is a **g**raph **li**brary for **PH**P. It provides graph building blocks and datastructures for use by other PHP applications. It is (currently) designed for use with in-memory graphs, not for interaction with a graph database like [Neo4J](http://neo4j.org/).

Gliph is designed with performance in mind, but primarily to provide a sane interface. Graphs are hard enough without an arcane API making it worse.

## Core Concepts

Gliph has several components that work together: graph classes, algorithms, and visitors. Generally speaking, Gliph is patterned after the [C++ Boost Graph Library](http://www.boost.org/libs/graph/doc); reading their documentation can yield a lot of insight into how Gliph is intended to work.

Note that Gliph is currently written for compatibility with PHP 5.3, but it is intended to port the library to PHP 5.5. The availability of traits, non-scalar/object keys returnable from iterators, and generators will considerably change both the internal and public-facing implementations.

### Graphs

There are a number of different strategies for representing graphs; these strategies are more or less efficient depending on certain properties the graph, and what needs to be done to the graph. The approach taken in Gliph is to offer a roughly consistent 'Graph' interface that is common to all these different strategies. The strategies will have varying levels of efficiency at meeting this common interface, so it is the responsibility of the user to select a graph implementation that is appropriate for their use case. This approach draws heavily from the [taxonomy of graphs](http://www.boost.org/doc/libs/1_54_0/libs/graph/doc/graph_concepts.html) established by the BGL.

Gliph currently implements only an adjacency list graph strategy, in both directed and undirected flavors. Adjacency lists offer efficient access to out-edges, but inefficient access to in-edges (in a directed graph - in an undirected graph, in-edges and out-edges are the same). Adjacency lists and are generally more space-efficient for sparse graphs.

## TODOs

Lots. But, to start with:

- Port to, or provide a parallel implementation in, PHP 5.5. Generators and non-scalar keys from iterators make this all SO much better. In doing that, also shift as much over to traits as possible.
- Implement a generic breadth-first algorithm and its corresponding visitors.
- Implement a generic iterative deepening depth-first algorithm, and its corresponding visitors.
- Implement other popular connected components algorithms, as well as some shortest path algorithms (starting with Dijkstra)
- Write up some examples showing how to actually use the library.

## Acknowledgements

This library draws heavy inspiration from the [C++ Boost Graph Library](http://www.boost.org/libs/graph/doc).

## License

MIT
Guzzle, PHP HTTP client and webservice framework
================================================

[![Build Status](https://secure.travis-ci.org/guzzle/guzzle.png?branch=master)](http://travis-ci.org/guzzle/guzzle)

Guzzle is a PHP HTTP client that makes it easy to work with HTTP/1.1 and takes
the pain out of consuming web services.

```php
$client = new GuzzleHttp\Client();
$response = $client->get('http://guzzlephp.org');
$res = $client->get('https://api.github.com/user', ['auth' =>  ['user', 'pass']]);
echo $res->getStatusCode();
// 200
echo $res->getHeader('content-type');
// 'application/json; charset=utf8'
echo $res->getBody();
// {"type":"User"...'
var_export($res->json());
// Outputs the JSON decoded data
```

- Pluggable HTTP adapters that can send requests serially or in parallel
- Doesn't require cURL, but uses cURL by default
- Streams data for both uploads and downloads
- Provides event hooks & plugins for cookies, caching, logging, OAuth, mocks,
  etc...
- Keep-Alive & connection pooling
- SSL Verification
- Automatic decompression of response bodies
- Streaming multipart file uploads
- Connection timeouts

Get more information and answers with the
[Documentation](http://guzzlephp.org/),
[Forums](https://groups.google.com/forum/?hl=en#!forum/guzzle),
and IRC ([#guzzlephp](irc://irc.freenode.net/#guzzlephp) @ irc.freenode.net).

### Installing via Composer

The recommended way to install Guzzle is through
[Composer](http://getcomposer.org).

```bash
# Install Composer
curl -sS https://getcomposer.org/installer | php
```

Next, update your project's composer.json file to include Guzzle:

```javascript
{
    "require": {
        "guzzlehttp/guzzle": "~4.0"
    }
}
```

After installing, you need to require Composer's autoloader:

```php
require 'vendor/autoload.php';
```

### Documentation

More information can be found in the online documentation at
http://guzzlephp.org/.
==============
Guzzle Streams
==============

Provides a simple abstraction over streams of data.

This library is used in `Guzzle 4 <https://github.com/guzzle/guzzle>`_ and is
an implementation of the proposed `PSR-7 stream interface <https://github.com/php-fig/fig-standards/blob/master/proposed/http-message.md#34-psrhttpstreaminterface>`_.

Installation
============

This package can be installed easily using `Composer <http://getcomposer.org>`_.
Simply add the following to the composer.json file at the root of your project:

.. code-block:: javascript

    {
      "require": {
        "guzzlehttp/streams": "1.*"
      }
    }

Then install your dependencies using ``composer.phar install``.

Documentation
=============

The documentation for this package can be found on the main Guzzle website at
http://docs.guzzlephp.org/en/guzzle4/streams.html.

Testing
=======

This library is tested using PHPUnit. You'll need to install the dependencies
using `Composer <http://getcomposer.org>`_ then run ``make test``.
Twig, the flexible, fast, and secure template language for PHP
==============================================================

Twig is a template language for PHP, released under the new BSD license (code
and documentation).

Twig uses a syntax similar to the Django and Jinja template languages which
inspired the Twig runtime environment.

More Information
----------------

Read the `documentation`_ for more information.

.. _documentation: http://twig.sensiolabs.org/documentation
The core/lib directory is for classes provided by Drupal Core that are original
to Drupal.  All Drupal-originated code must follow the PSR-0 naming convention
for classes and namespaces as documented here:

https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md

The vendor namespace for Drupal-originated code is "Drupal".
Code in the Drupal\Core namespace represents Drupal Subsystems provided by the
base system.  These subsystems MAY depend on Drupal Components and other
Subsystems, but MAY NOT depend on any code in a module.

Each Subsystem should be in its own namespace, and should be as self-contained
as possible.
Drupal Components are independent libraries that do not depend on the rest of
Drupal in order to function.  Components MAY depend on other Components, but
that is discouraged. Components MAY NOT depend on any code that is not part of
PHP itself or another Drupal Component.

Each Component should be in its own namespace, and should be as self-contained
as possible.  It should be possible to split a Component off to its own
repository and use as a stand-alone library, independently of Drupal.
[jQuery UI](http://jqueryui.com/) - Interactions and Widgets for the web
================================

jQuery UI provides interactions like Drag and Drop and widgets like Autocomplete, Tabs and Slider and makes these as easy to use as jQuery itself.

If you want to use jQuery UI, go to [jqueryui.com](http://jqueryui.com) to get started. Or visit the [Using jQuery UI Forum](http://forum.jquery.com/using-jquery-ui) for discussions and questions.

If you are interested in helping develop jQuery UI, you are in the right place.
To discuss development with team members and the community, visit the [Developing jQuery UI Forum](http://forum.jquery.com/developing-jquery-ui) or in #jquery on irc.freednode.net.


For contributors
---

If you want to help and provide a patch for a bugfix or new feature, please take
a few minutes and look at [our Getting Involved guide](http://wiki.jqueryui.com/w/page/35263114/Getting-Involved).
In particular check out the [Coding standards](http://wiki.jqueryui.com/w/page/12137737/Coding-standards)
and [Commit Message Style Guide](http://wiki.jqueryui.com/w/page/25941597/Commit-Message-Style-Guide).

In general, fork the project, create a branch for a specific change and send a
pull request for that branch. Don't mix unrelated changes. You can use the commit
message as the description for the pull request.


Running the Unit Tests
---

Run the unit tests with a local server that supports PHP. No database is required. Pre-configured php local servers are available for Windows and Mac. Here are some options:

- Windows: [WAMP download](http://www.wampserver.com/en/)
- Mac: [MAMP download](http://www.mamp.info/en/index.html)
- Linux: [Setting up LAMP](https://www.linux.com/learn/tutorials/288158-easy-lamp-server-installation)
- [Mongoose (most platforms)](http://code.google.com/p/mongoose/)


Building jQuery UI
---

jQuery UI uses the [grunt](http://github.com/cowboy/grunt) build system. Building jQuery UI requires node.js and a command line zip program.

Install grunt.

`npm install grunt -g`

Clone the jQuery UI git repo.

`git clone git://github.com/jquery/jquery-ui.git`

`cd jquery-ui`

Install node modules.

`npm install`

Run grunt.

`grunt build`

There are many other tasks that can be run through grunt. For a list of all tasks:

`grunt --help`


For committers
---

When looking at pull requests, first check for [proper commit messages](http://wiki.jqueryui.com/w/page/12137724/Bug-Fixing-Guide).

Do not merge pull requests directly through GitHub's interface.
Most pull requests are a single commit; cherry-picking will avoid creating a merge commit.
It's also common for contributors to make minor fixes in an additional one or two commits.
These should be squashed before landing in master.

**Make sure the author has a valid name and email address associated with the commit.**

Fetch the remote first:

    git fetch [their-fork.git] [their-branch]

Then cherry-pick the commit(s):

	git cherry-pick [sha-of-commit]

If you need to edit the commit message:

    git cherry-pick -e [sha-of-commit]

If you need to edit the changes:

	git cherry-pick -n [sha-of-commit]
	# make changes
	git commit --author="[author-name-and-email]"

If it should go to the stable brach, cherry-pick it to stable:

    git checkout 1-8-stable
    git cherry-pick -x [sha-of-commit-from-master]

*NOTE: Do not cherry-pick into 1-8-stable until you have pushed the commit from master upstream.*
# normalize.css v3

Normalize.css is a customisable CSS file that makes browsers render all
elements more consistently and in line with modern standards.

The project relies on researching the differences between default browser
styles in order to precisely target only the styles that need or benefit from
normalizing.

[View the test file](http://necolas.github.io/normalize.css/latest/test.html)

## Install

Download from the [project page](http://necolas.github.io/normalize.css/).

Install with [Component(1)](https://github.com/component/component/): `component install necolas/normalize.css`

Install with [npm](http://npmjs.org/): `npm install --save normalize.css`

Install with [Bower](http://bower.io/): `bower install --save normalize.css`

## What does it do?

* Preserves useful defaults, unlike many CSS resets.
* Normalizes styles for a wide range of elements.
* Corrects bugs and common browser inconsistencies.
* Improves usability with subtle improvements.
* Explains what code does using detailed comments.

## How to use it

No other styles should come before Normalize.css.

It is recommended that you include the `normalize.css` file as untouched
library code.

## Browser support

* Google Chrome (latest)
* Mozilla Firefox (latest)
* Mozilla Firefox 4
* Opera (latest)
* Apple Safari 6+
* Internet Explorer 8+

[Normalize.css v1 provides legacy browser
support](https://github.com/necolas/normalize.css/tree/v1) (IE 6+, Safari 4+),
but is no longer actively developed.

## Contributing

Please read the CONTRIBUTING.md

## Acknowledgements

Normalize.css is a project by [Nicolas Gallagher](https://github.com/necolas),
co-created with [Jonathan Neal](https://github.com/jonathantneal).
classList.js is a cross-browser JavaScript shim that fully implements `element.classList`. Refer to [the MDN page on `element.classList`][1] for more information.


![Tracking image](https://in.getclicky.com/212712ns.gif)


  [1]: https://developer.mozilla.org/en/DOM/element.classList "MDN / DOM / element.classList"

ABOUT STARK
-----------

The Stark theme is provided for demonstration purposes; it uses Drupal's
default HTML markup and CSS styles. It can be used as a troubleshooting tool to
determine whether module-related CSS and JavaScript are interfering with a more
complex theme, and can be used by designers interested in studying Drupal's
default markup without the interference of changes commonly made by more
complex themes.

To avoid obscuring CSS added to the page by Drupal or a contrib module, the
Stark theme itself has no styling, except just enough CSS to arrange the page
in a traditional "Header, sidebars, content, and footer" layout. See the
layout.css file for more information.


ABOUT DRUPAL THEMING
--------------------

To learn how to build your own custom theme and override Drupal's default code,
see the Theming Guide: http://drupal.org/theme-guide

See the themes/README.txt for more information on where to place your
custom themes to ensure easy maintenance and upgrades.

These files are useful in tests that upload files or otherwise need to
manipulate files, in which case they are copied to the files directory as
specified in the site settings. Dummy files can also be generated by tests in
order to save space.
The classes in this directory act as a mock plugin type to test annotated class
discovery. See the corresponding test file:
/core/modules/system/lib/Drupal/system/Tests/Plugin/Discovery/AnnotatedClassDiscoveryTest.php
Place downloaded and custom installation profiles in this directory to ensure
separation from Drupal core profiles and to facilitate safe, self-contained code
updates.

In multisite configuration, installation profiles found in this directory are
available to all sites during their initial site installation. Shared common
profiles may also be kept in the sites/all/profiles directory and will take
precedence over profiles in this directory. Alternatively, the
sites/your_site_name/profiles directory pattern may be used to restrict a
profile's availability to a specific site instance.

Additionally, modules and themes may be placed inside subdirectories in a
specific installation profile such as profiles/your_site_profile/modules and
profiles/your_site_profile/themes respectively to restrict their usage to only
sites that were installed with that specific profile.

Refer to the "Installation Profiles" section of the README.txt in the Drupal
root directory for further information.
Place downloaded and custom themes that modify your site's appearance in this
directory to ensure clean separation from Drupal core and to facilitate safe,
self-contained code updates. Contributed themes from the Drupal community may
be downloaded at http://drupal.org/project/themes.

It is safe to organize themes into subdirectories and is recommended to use
Drupal's sub-theme functionality to ensure easy maintenance and upgrades.

In multisite configuration, themes found in this directory are available to
all sites. In addition to this directory, shared common themes may also be kept
in the sites/all/themes directory and will take precedence over themes in this
directory. Alternatively, the sites/your_site_name/themes directory pattern may
be used to restrict themes to a specific site instance.

Refer to the "Appearance" section of the README.txt in the Drupal root
directory for further information on theming.
Deployotron
===========

Deployotron is a Drush command to simplify deploying new code to a
Drupal site.

There's already a lot of ways to deploy ones Drupal site, from FTPing
up the files to having Capistrano deploy the site when the build
passes in Jenkins. Deployotron aims to be simple to use, but also
usable as a part of a bigger setup.

[![Build Status](https://travis-ci.org/reload/deployotron.png?branch=master)](https://travis-ci.org/reload/deployotron)
[![Code Coverage](https://scrutinizer-ci.com/g/reload/deployotron/badges/coverage.png?s=0f0d54845fc1c45affcc0ad8c111e40f4e40c359)](https://scrutinizer-ci.com/g/reload/deployotron/)
[![Scrutinizer Quality Score](https://scrutinizer-ci.com/g/reload/deployotron/badges/quality-score.png?s=cd9fde12be1b74734b00d59618d4eb6c1bf5bfb0)](https://scrutinizer-ci.com/g/reload/deployotron/)

Overview
========

In order to keep things simple, we're working with a few assumptions:

That the code is in GIT, and that the root of the site is checked in.

That you can run Drush commands and GIT on the live webserver and the
root of the site on the webserver is a git checkout, and

That you've set up Drush aliases to reach the live webserver.

For everyone's sanity, we suggest having a Drush alias file in
`sites/all/drush/<short-site-alias>.aliases.drushrc.php` that defines
relevant environments (production, dev, etc.), so that everybody is
using the same settings.

And we suggest that deployotron is installed by copying it into the
`sites/all/drush` folder and committed to the site repository. This
ensures that everyone is running the exact same version of deployotron
when deploying.

Setup
=====

Clone Deployotron into `sites/all/drush`. 

Create a `<sitename>.aliases.drushrc.php` file in the same directory,
with the definition of the different environments.

Deployotron is configured for each alias by adding an array of options
in the `'deployotron'` key of the alias array (see the example later,
if that didn't make any sense). All the double-dash options the deploy
command takes can be specified this way, and it's recommended to at
least define the `'branch'` option to select a default branch to
deploy.

Initialize the environments by doing an initial git clone of the
codebase in the destination directories.

Usage
=====

Deploying
---------

To run the deployment, use a command like:

    /var/www/site$ drush deploy @alias

To get a listing of all supported command line options, do a `drush
help deploy`.

In order to be able to restart Apache2/Varnish, sudo needs to be set
up to allow the deploying user to restart the services. See "Sudo
setup" for details.

Example configuration:

    $aliases['staging'] = array(
      'remote-host' => 'example.com',
      'remote-user' => 'deploy_user',
      'uri' => 'default',
      'root' => '/path',
      'deployotron' => array(
        'branch' => 'develop',
        'dump-dir' => '/backups',
        'restart-apache2' => TRUE,
      ),
    );

In addition to command line options you can add messages to be
displayed to the deploying user by using the following keys:


 * `message`: Shown at confirmation and after deployment.
 * `confirm_message`: Shown at confirmation.
 * `done_message`: Shown after deployment.
 * `confirm_message_<command>`: Shown at confirmation for the
   `<command>`.
 * `done_message_<command>`: Shown after deployment for the
   `<command>`.

These can be useful to remind the user of extra manual steps, or other
things they should be aware.

Recovering
----------

In case everything goes to hell after a deployment, you can do another
deployment using a known good revision, or use:

    /var/www/site$ drush omg @alias

This will try to find recent database dumps, ask which to use and
attempt to import the database and revert the codebase to the previous
revision. It will not attempt to clear caches or restarting any
services.

Help
----

Running `drush deployotron-actions` will give a full list of which
commands uses which actions, and the options of all actions.

Sudo setup
==========

To give the deploying user (`remote-user` in the alias) permission to
restart apache2/varnish, you need to configure sudo. Use the following
command to edit a sudoers.d config file:

    sudo visudo -f /etc/sudoers.d/deployotron

And add the following to the file (replacing `deploy_user` with the
`remote-user` of the alias used for deployment):

    deploy_user          ALL=(root) NOPASSWD: /usr/sbin/service apache2 restart,/usr/sbin/service varnish restart
Place downloaded and custom modules that extend your site functionality beyond
Drupal core in this directory to ensure clean separation from core modules and
to facilitate safe, self-contained code updates. Contributed modules from the
Drupal community may be downloaded at http://drupal.org/project/modules.

It is safe to organize modules into subdirectories, such as "contrib" for
contributed modules, and "custom" for custom modules. Note that if you move a
module to a subdirectory after it has been enabled, you may need to clear the
Drupal cache so that it can be found.

In multisite configuration, modules found in this directory are available to
all sites. In addition to this directory, shared common modules may also be kept
in the sites/all/modules directory and will take precedence over modules in this
directory. Alternatively, the sites/your_site_name/modules directory pattern may
be used to restrict modules to a specific site instance.

Refer to the "Developing for Drupal" section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom modules.
