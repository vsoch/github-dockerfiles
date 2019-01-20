Filesystem Component
====================

The Filesystem component provides basic utilities for the filesystem.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/filesystem/index.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
Console Component
=================

The Console component eases the creation of beautiful and testable command line
interfaces.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/console/index.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)

Credits
-------

`Resources/bin/hiddeninput.exe` is a third party binary provided within this
component. Find sources and license at https://github.com/Seldaek/hidden-input.
Symfony Polyfill / Mbstring
===========================

This component provides a partial, native PHP implementation for the
[Mbstring](http://php.net/mbstring) extension.

More information can be found in the
[main Polyfill README](https://github.com/symfony/polyfill/blob/master/README.md).

License
=======

This library is released under the [MIT license](LICENSE).
Config Component
================

The Config component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (YAML, XML, INI files, or for instance a database).

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/config/index.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
Yaml Component
==============

The Yaml component loads and dumps YAML files.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/yaml/index.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
Debug Component
===============

The Debug component provides tools to ease debugging PHP code.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/debug/index.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
Symfony Debug Extension for PHP 5
=================================

This extension publishes several functions to help building powerful debugging tools.
It is compatible with PHP 5.3, 5.4, 5.5 and 5.6; with ZTS and non-ZTS modes.
It is not required thus not provided for PHP 7.

symfony_zval_info()
-------------------

- exposes zval_hash/refcounts, allowing e.g. efficient exploration of arbitrary structures in PHP,
- does work with references, preventing memory copying.

Its behavior is about the same as:

```php
<?php

function symfony_zval_info($key, $array, $options = 0)
{

    // $options is currently not used, but could be in future version.

    if (!array_key_exists($key, $array)) {
        return null;
    }

    $info = array(
        'type' => gettype($array[$key]),
        'zval_hash' => /* hashed memory address of $array[$key] */,
        'zval_refcount' => /* internal zval refcount of $array[$key] */,
        'zval_isref' => /* is_ref status of $array[$key] */,
    );

    switch ($info['type']) {
        case 'object':
            $info += array(
                'object_class' => get_class($array[$key]),
                'object_refcount' => /* internal object refcount of $array[$key] */,
                'object_hash' => spl_object_hash($array[$key]),
                'object_handle' => /* internal object handle $array[$key] */,
            );
            break;

        case 'resource':
            $info += array(
                'resource_handle' => (int) $array[$key],
                'resource_type' => get_resource_type($array[$key]),
                'resource_refcount' => /* internal resource refcount of $array[$key] */,
            );
            break;

        case 'array':
            $info += array(
                'array_count' => count($array[$key]),
            );
            break;

        case 'string':
            $info += array(
                'strlen' => strlen($array[$key]),
            );
            break;
    }

    return $info;
}
```

symfony_debug_backtrace()
-------------------------

This function works like debug_backtrace(), except that it can fetch the full backtrace in case of fatal errors:

```php
function foo() { fatal(); }
function bar() { foo(); }

function sd() { var_dump(symfony_debug_backtrace()); }

register_shutdown_function('sd');

bar();

/* Will output
Fatal error: Call to undefined function fatal() in foo.php on line 42
array(3) {
  [0]=>
  array(2) {
    ["function"]=>
    string(2) "sd"
    ["args"]=>
    array(0) {
    }
  }
  [1]=>
  array(4) {
    ["file"]=>
    string(7) "foo.php"
    ["line"]=>
    int(1)
    ["function"]=>
    string(3) "foo"
    ["args"]=>
    array(0) {
    }
  }
  [2]=>
  array(4) {
    ["file"]=>
    string(102) "foo.php"
    ["line"]=>
    int(2)
    ["function"]=>
    string(3) "bar"
    ["args"]=>
    array(0) {
    }
  }
}
*/
```

Usage
-----

To enable the extension from source, run:

```
    phpize
    ./configure
    make
    sudo make install
```
# [Phinx](https://phinx.org): Simple PHP Database Migrations

[![Build Status](https://travis-ci.org/robmorgan/phinx.png?branch=0.2.x-dev)](https://travis-ci.org/robmorgan/phinx)
[![Build status](https://ci.appveyor.com/api/projects/status/9vag4892hfq6effr)](https://ci.appveyor.com/project/robmorgan/phinx)
[![Code Coverage](https://scrutinizer-ci.com/g/robmorgan/phinx/badges/coverage.png?s=9776e35b967f5adb0f4958bd72b617e0a9519f7d)](https://scrutinizer-ci.com/g/robmorgan/phinx/)
[![Latest Stable Version](https://poser.pugx.org/robmorgan/phinx/version.png)](https://packagist.org/packages/robmorgan/phinx)
[![Total Downloads](https://poser.pugx.org/robmorgan/phinx/d/total.png)](https://packagist.org/packages/robmorgan/phinx)

Phinx makes it ridiculously easy to manage the database migrations for your PHP app. In less than 5 minutes you can install Phinx and create your first database migration. Phinx is just about migrations without all the bloat of a database ORM system or framework.

**Check out http://docs.phinx.org for the comprehensive documentation.**

![phinxterm](https://cloud.githubusercontent.com/assets/178939/3887559/e6b5e524-21f2-11e4-8256-0ba6040725fc.gif)

### Features

* Write database migrations using database agnostic PHP code.
* Migrate up and down.
* Migrate on deployment.
* Get going in less than 5 minutes.
* Stop worrying about the state of your database.
* Take advantage of SCM features such as branching.
* Integrate with any app.

### Supported Adapters

Phinx natively supports the following database adapters:

* MySQL
* PostgreSQL
* SQLite
* Microsoft SQL Server

## Install & Run

### Composer

The fastest way to install Phinx is to add it to your project using Composer (http://getcomposer.org/).

1. Install Composer:

    ```
    curl -s https://getcomposer.org/installer | php
    ```

1. Require Phinx as a dependency using Composer:

    ```
    php composer.phar require robmorgan/phinx
    ```

1. Install Phinx:

    ```
    php composer.phar install
    ```

1. Execute Phinx:

    ```
    php vendor/bin/phinx
    ```

### As a Phar

You can also use the Box application to build Phinx as a Phar archive (http://box-project.org/).

1. Clone Phinx from GitHub

    ```
    git clone git://github.com/robmorgan/phinx.git
    cd phinx
    ```

1. Install Composer

    ```
    curl -s https://getcomposer.org/installer | php
    ```

1. Install the Phinx dependencies

    ```
    php composer.phar install
    ```

1. Install Box:

    ```
    curl -LSs https://box-project.github.io/box2/installer.php | php
    ```

1. Create a Phar archive

    ```
    php box.phar build
    ```

## Documentation

Check out http://docs.phinx.org for the comprehensive documentation.

## Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) document.

## News & Updates

Follow Rob (@\_rjm\_) on Twitter to stay up to date (http://twitter.com/_rjm_)

## Misc

### Version History

**0.4.6** (Friday, 11th September 2015)

* You can now set custom migration templates in the config files
* Support for MySQL unsigned booleans
* Support for Postgres `smallint` column types
* Support for `AFTER` when using `changeColumn()` with MySQL
* Support for `precision` and `scale` when using the Postgres `decimal` type
* Fixed a bug where duplicate migration names could be used
* The schema table is now created with a primary key
* Fixed issues when using the MySQL `STRICT_TRANS_TABLE` mode
* Improved the docs in the default migration template
* Made Box PHAR ignore the bundled `phinx.yml` configuration file
* Updated Box installer URL
* Internal code improvements
* Documentation improvements

**0.4.5** (Tuesday, 1st September 2015)

* The rollback command now supports a date argument
* Fixed DBLIB DSN strings for Microsoft SQL Server
* Postgres support for `jsonb` columns added
* The `addTimestamps()` helper method no longer updates the `created_at` column
* Fix for Postgres named foreign keys
* Unit test improvements (including strict warnings)
* Documentation improvements

**0.4.4** (Sunday, 14th June 2015)

* The `change` method is now the default
* Added a generic adapter insert method. Warning: The implementation will change!
* Updated Symfony depdencies to ~2.7
* Support for MySQL `BLOB` column types
* SQLite migration fixes
* Documentation improvements

**0.4.3** (Monday, 23rd Feburary 2015)

* Postgres bugfix for modifying column DEFAULTs
* MySQL bugfix for setting column INTEGER lengths
* SQLite bugfix for creating multiple indexes with similar names

**0.4.2.1** (Saturday, 7th Feburary 2015)

* Proper release, updated docs

**0.4.2** (Friday, 6th Feburary 2015)

* Postgres support for `json` columns added
* MySQL support for `enum` and `set` columns added
* Allow setting `identity` option on columns
* Template configuration and generation made more extensible
* Created a base class for `ProxyAdapter` and `TablePrefixAdapter`
* Switched to PSR-4

**0.4.1** (Tuesday, 23rd December 2014)

* MySQL support for reserved words in hasColumn and getColumns methods
* Better MySQL Adapter test coverage and performance fixes
* Updated dependent Symfony components to 2.6.x

**0.4.0** (Sunday, 14th December 2014)

* Adding initial support for running Phinx via a web interface
* Support for table prefixes and suffixes
* Bugfix for foreign key options
* MySQL keeps column default when renaming columns
* MySQL support for tiny/medium and longtext columns added
* Changed SQL Server binary columns to varbinary
* MySQL supports table comments
* Postgres supports column comments
* Empty strings are now supported for default column values
* Booleans are now supported for default column values
* Fixed SQL Server default constraint error when changing column types
* Migration timestamps are now created in UTC
* Locked Symfony Components to 2.5.0
* Support for custom migration base classes
* Cleaned up source code formatting
* Migrations have access to the output stream
* Support for custom PDO connections when a PHP config
* Added support for Postgres UUID type
* Fixed issue with Postgres dropping foreign keys

**0.3.8** (Sunday, 5th October 2014)

* Added new CHAR & Geospatial column types
* Added MySQL unix socket support
* Added precision & scale support for SQL Server
* Several bug fixes for SQLite
* Improved error messages
* Overall code optimizations
* Optimizations to MySQL hasTable method

**0.3.7** (Tuesday, 12th August 2014)

* Smarter configuration file support
* Support for Postgres Schemas
* Fixed charset support for Microsoft SQL Server
* Fix for Unique indexes in all adapters
* Improvements for MySQL foreign key migration syntax
* Allow MySQL column types with extra info
* Fixed SQLite autoincrement behaviour
* PHPDoc improvements
* Documentation improvements
* Unit test improvements
* Removing primary_key as a type

**0.3.6** (Sunday, 29th June 2014)

* Add custom adapter support
* Fix PHP 5.3 compatibility for SQL Server

**0.3.5** (Saturday, 21st June 2014)

* Added Microsoft SQL Server support
* Removed Primary Key column type
* Cleaned up and optimized many methods
* Updated Symfony dependencies to v2.5.0
* PHPDoc improvements

**0.3.4** (Sunday, 27th April 2014)

* Added support MySQL unsigned integer, biginteger, float and decimal types
* Added JSON output support for the status command
* Fix a bug where Postgres couldnt rollback foreign keys
* Moved Phinx type references to interface constants
* Fixed a bug with SQLite in-memory databases

**0.3.3** (Saturday, 22nd March 2014)

* Added support for JSON configuration
* Named index support for all adapters (thanks @archer308)
* Updated Composer dependencies
* Fix for SQLite Integer Type
* Fix for MySQL port option

**0.3.2** (Monday, 24th February 2014)

* Adding better Postgres type support

**0.3.1** (Sunday, 23rd February 2014)

* Adding MySQL charset support to the YAML config
* Removing trailing spaces

**0.3.0** (Sunday, 2nd February 2014)

* PSR-2 support
* Method to add timestamps easily to tables
* Support for column comments in the Postgres adapter
* Fixes for MySQL driver options
* Fixes for MySQL biginteger type

**0.2.9** (Saturday, 16th November 2013)

* Added SQLite Support
* Improving the unit tests, especially on Windows

**0.2.8** (Sunday, 25th August 2013)

* Added PostgresSQL Support

**0.2.7** (Saturday, 24th August 2013)

* Critical fix for a token parsing bug
* Removed legacy build system
* Improving docs

**0.2.6** (Saturday, 24th August 2013)

* Added support for environment vars in config files
* Added support for environment vars to set the Phinx Env
* Improving docs
* Fixed a bug with column names in indexes
* Changes for developers in regards to the unit tests

**0.2.5** (Sunday, 26th May 2013)

* Added support for Box Phar Archive Packaging
* Added support for MYSQL_ATTR driver options
* Fixed a bug where foreign keys cannot be removed
* Added support for MySQL table collation
* Updated Composer dependencies
* Removed verbosity options, now relies on Symfony instead
* Improved unit tests

**0.2.4** (Saturday, 20th April 2013)

* The Rollback command supports the verbosity parameter
* The Rollback command has more detailed output
* Table::dropForeignKey now returns the table instance

**0.2.3** (Saturday, 6th April 2013)

* Fixed a reporting bug when Phinx couldn't connect to a database
* Added support for the MySQL 'ON UPDATE' function
* Phinx timestamp is now mapped to MySQL timestamp instead of datetime
* Fixed a docs typo for the minimum PHP version
* Added UTF8 support for migrations
* Changed regex to handle migration names differently
* Added support for custom MySQL table engines such as MyISAM
* Added the change method to the migration template

**0.2.2** (Sunday, 3rd March 2013)

* Added a new verbosity parameter to see more output when migrating
* Support for PHP config files

**0.2.1** (Sunday, 3rd March 2013)

* Broken Release. Do not use!
* Unit tests no longer rely on the default phinx.yml file
* Running migrate for the first time does not give php warnings
* `default_migration_table` is now actually supported
* Updated docblocks to 2013.

**0.2.0** (Sunday, 13th January 2013)

* First Birthday Release
* Added Reversible Migrations
* Removed options parameter from AdapterInterface::hasColumn()

**0.1.7** (Tuesday, 8th January 2013)

* Improved documentation on the YAML configuration file
* Removed options parameter from AdapterInterface::dropIndex()

**0.1.6** (Sunday, 9th December 2012)

* Added foreign key support
* Removed PEAR support
* Support for auto_increment on custom id columns
* Bugfix for column default value 0
* Documentation improvements

**0.1.5** (Sunday, 4th November 2012)

* Added a test command
* Added transactions for adapters that support it
* Changing the Table API to use pending column methods
* Fixed a bug when defining multiple indexes on a table

**0.1.4** (Sunday, 21st October 2012)

* Documentation Improvements

**0.1.3** (Saturday, 20th October 2012)

* Fixed broken composer support

**0.1.2** (Saturday, 20th October 2012)

* Added composer support
* Now forces migrations to be in CamelCase format
* Now specifies the database name when migrating
* Creates the internal log table using its API instead of raw SQL

**0.1.1** (Wednesday, 13th June 2012)

* First point release. Ready for limited production use.

**0.1.0** (Friday, 13th January 2012)

* Initial public release.

### License

(The MIT license)

Copyright (c) 2015 Rob Morgan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# JasperReports for PHP 

Package to generate reports with [JasperReports](http://community.jaspersoft.com/project/jasperreports-library) library through [JasperStarter](http://jasperstarter.sourceforge.net/) command-line tool.

##Introduction

This package aims to be a solution to compile and process JasperReports (.jrxml & .jasper files). 

###Why?

Did you ever had to create a good looking Invoice with a lot of fields for your great web app? 

I had to, and the solutions out there were not perfect. Generating *HTML* + *CSS* to make a *PDF*? WTF? That doesn't make any sense! :)

Then I found **JasperReports** the best open source solution for reporting.

###What can I do with this?

Well, everything. JasperReports is a powerful tool for **reporting** and **BI**. 

**From their website:**

> The JasperReports Library is the world's most popular open source reporting engine. It is entirely written in Java and it is able to use data coming from any kind of data source and produce pixel-perfect documents that can be viewed, printed or exported in a variety of document formats including HTML, PDF, Excel, OpenOffice and Word.

I recommend you to use [iReports designer](http://community.jaspersoft.com/project/ireport-designer) to build your reports, connect it to your datasource (ex: MySQL), loop thru the results and output it to PDF, XLS, DOC, RTF, ODF, etc.

*Some examples of what you can do:*

* Invoices
* Reports
* Listings

##Examples

###The *Hello World* example.

Go to the examples directory in the root of the repository (`vendor/cossou/jasperphp/examples`).
Open the `hello_world.jrxml` file with iReport or with your favorite text editor and take a look at the source code.

#### Compiling

First we need to compile our `JRXML` file into a `JASPER` binary file. We just have to do this one time. 

**Note:** You don't need to do this step if you are using *iReport Designer*. You can compile directly within the program.

	JasperPHP::compile(base_path() . '/vendor/cossou/jasperphp/examples/hello_world.jrxml')->execute();

This commando will compile the `hello_world.jrxml` source file to a `hello_world.jasper` file.

**Note:** If you are using Laravel 4 run `php artisan tinker` and copy & paste the command above.

####Processing

Now lets process the report that we compile before: 

	JasperPHP::process(
		base_path() . '/vendor/cossou/jasperphp/examples/hello_world.jasper', 
		false, 
		array("pdf", "rtf"), 
		array("php_version" => phpversion())
	)->execute();

Now check the examples folder! :) Great right? You now have 2 files, `hello_world.pdf` and `hello_world.rtf`.

Check the *API* of the  `compile` and `process` functions in the file `src/JasperPHP/JasperPHP.php` file.

###Advanced example

TODO.

##Requirements

* Java JDK 1.6
* PHP [exec()](http://php.net/manual/function.exec.php) function
* [optional] [Mysql Connector](http://dev.mysql.com/downloads/connector/j/) (if you want to use database) 
* [optional] [iReports](http://community.jaspersoft.com/project/ireport-designer) (to draw and compile your reports) 


##Installation

###Java

Check if you already have Java installed:
```java	
	$ java -version
	java version "1.6.0_51"
	Java(TM) SE Runtime Environment (build 1.6.0_51-b11-457-11M4509)
	Java HotSpot(TM) 64-Bit Server VM (build 20.51-b01-457, mixed mode)
```
If you get:
	
	command not found: java 

Then install it with: (Ubuntu/Debian)

	$ sudo apt-get install default-jdk

Now run the `java -version` again and check if the output is ok.

###Composer

Install [Composer](http://getcomposer.org) if you don't have it.

Now in your `composer.json` file add:
```javascript
{
    "require": {
	"cossou/jasperphp": "dev-master",
    }
}
```
	
And the just run:

	composer update

and thats it.	

###Using Laravel 4?

Add to your `app/config/app.php` providers array:
```php
'JasperPHP\JasperPHPServiceProvider',
```	
Now you will have the `JasperPHP` alias available.

###MySQL

If you want to use MySQL in your report datasource, please add the `JAR` to the `/src/JasperStarter/jdbc/` directory. Download it [here](http://dev.mysql.com/downloads/connector/j/).

##Performance

Depends on the complexity, amount of data and the resources of your machine (let me know your use case).

I have a report that generates a *Invoice* with a DB connection, images and multiple pages and it takes about **3/4 seconds** to process. I suggest that you use the [Laravel 4 Queue](#) feature.


##Thanks

Thanks to [Cenote GmbH](http://www.cenote.de/) for the [JasperStarter](http://jasperstarter.sourceforge.net/) tool.

##Questions?

Drop me a line on Twitter [@cossou](https://twitter.com/cossou).


##License

MIT

JasperStarter - Running JasperReports from command line
--------------------------------------------------------

JasperStarter is an opensource command line launcher and batch compiler for
[JasperReports][].

It has the following features:

  * Run any JasperReport that needs a jdbc, csv, xml or empty datasource
  * Use with any database for which a jdbc driver is available
  * Execute reports that need runtime parameters. Any parameter whose class has
    a string constructor is accepted. Additionally the following types are
    supported or have special handlers:
    * date, image (see usage), locale
  * Optionally prompt for report parameters
  * Print directly to system default or given printer
  * Optionally show printer dialog to choose printer
  * Optionally show printpreview
  * Export to file in the following formats:
    * pdf, rtf, xls, xlsx, docx, odt, ods, pptx, csv, html, xhtml, xml, jrprint
  * Export multiple formats in one commanding call
  * Compile, Print and export in one commanding call
  * View, print or export previously filled reports (use jrprint file as input)
  * Can compile a whole directory of .jrxml files.
  * Integrate in non Java applications (for example PHP, Python)
  * Binary executable on Windows
  * Includes JasperReports so this is the only tool you need to install

Requirements

  * Java 1.6 or higher.
  * A JDBC 2.1 driver for your database


### Quickstart

  * Download JasperStarter from [Sourceforge][]
  * Extract the distribution archive to any directory on your system.
  * Add the _./bin_ directoy of your installation to your searchpath.

  * or just invoke _setup.exe_ on Windows

  * Put your jdbc drivers in the _./jdbc_ directory of your installation or
    use _\--jdbc-dir_ to point to a different directory.

Invoke JasperStarter with _\-h_ to get an overview:

    $ jasperstarter -h

Invoke JasperStarter with _process \-h_ to get help on the process command:

    $ jasperstarter process -h

Example with reportparameters:

    $ jasperstarter pr report.jasper -t mysql -u myuser -f pdf -H myhost \
     -n mydb -o report -p secret -P CustomerNo=10 StartFrom=2012-10-01

Example with hsql using database type generic:

    $ jasperstarter pr report.jasper -t generic -f pdf -o report -u sa \
    --db-driver org.hsqldb.jdbcDriver \
    --db-url jdbc:hsqldb:hsql://localhost

For more information take a look in the docs directory of the distibution
archive or read the [Usage][] page online.


### Release Notes

See CHANGES file for a history of changes.


#### Known Bugs

For upcoming issues see [Issues][]


### Feedback

Feedback is always welcome! If you have any questions or proposals, don't
hesitate to write to our [discussion][] forum.
If you found a bug or you are missing a feature, log into our [Issuetracker][]
and create a bug or feature request.

If you like the software you can write a [review][] :-)


### Developement

The sourcecode is available at [bitbucket.org/cenote/jasperstarter][], the
project website is hosted at [Sourceforge][].

JasperStarter is build with [Maven][]. To get a distribution package run:

    $ mvn package -P release

or if you build from the current default branch you better use:

    $ mvn package -P release,snapshot

**Attention! You cannot execute** `target/jasperstarter.jar`
**without having it\'s dependencies in** `../lib` ! See **dev** profile below!

If you want to build the Windows setup.exe, you need to have _nsis_ in your
search path (works on linux too, you can find a compiled release in the 
sourceforge download folder _build-tools_ for your convenience)
an add the **windows-setup** profile to your build:

    $ mvn package -P release,windows-setup

or

    $ mvn package -P release,windows-setup,snapshot

While developing you may want to have a quicker build. The **dev** profile
excludes some long running reports and the compressed archives. Instead it puts
the build result into _target/jasperstarter-dev-bin_.

    $ mvn package -P dev

Now you can execute JasperStarter without IDE:

    $ target/jasperstarter-dev-bin/bin/jasperstarter

or

    $ java -jar target/jasperstarter-dev-bin/lib/jasperstarter.jar

During development you might want not to be annoyed by tests. So the following
options are useful:

    $ package -P dev -D skipTests

or

    $ package -P dev -D maven.test.failure.ignore=true

To run JasperStarter from within your IDE add _\--jdbc-dir jdbc_ to the argument
list of your run configuration. Otherwise you will get an error:

    Error, (...)/JasperStarter/target/classes/jdbc is not a directory!

Put your jdbc drivers in the _./jdbc_ directory of the project to invoke
JasperStarter from within your IDE to call up a database based report.


### License

Copyright 2012, 2013, 2014 Cenote GmbH.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[JasperReports]:http://community.jaspersoft.com/project/jasperreports-library
[Maven]:http://maven.apache.org/
[Sourceforge]:http://sourceforge.net/projects/jasperstarter/
[bitbucket.org/cenote/jasperstarter]:http://bitbucket.org/cenote/jasperstarter
[review]:http://sourceforge.net/projects/jasperstarter/reviews
[discussion]:http://sourceforge.net/p/jasperstarter/discussion/
[Issuetracker]:https://cenote-issues.atlassian.net/browse/JAS
[Usage]:http://jasperstarter.sourceforge.net/usage.html
[Issues]:https://cenote-issues.atlassian.net/browse/JAS
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
