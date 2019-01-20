
# Design In The Browser Bootstrap, Patternlab edition!

This project provides a starting point for prototypes, with tooling and an opinion on CSS and JS structure to allow for rapid development utilising Patternlab ensuring all work is as transferable and as maintainable as possible.

## What's required

It is assumed the developers computer is running OSX or Linux. Depending on your setup you may already have the below installed;

* [Node.js](http://nodejs.org) (version 4.x.x)
* [PHP](http://www.php.net/) (version 5.5+)
* Optional: [Yarn](https://yarnpkg.com/en/docs/install)

## What's included

* [Patternlab-PHP](https://github.com/pattern-lab/edition-php-twig-standard): Currently the most complete and stable version of patternlab, and supports [twig](http://twig.sensiolabs.org/).
* [SASS](http://sass-lang.com/) CSS with [auto-prefixing](https://github.com/postcss/autoprefixer).
* [Browsersync](https://www.browsersync.io) for autoreloading.
* [Rollup](https://rollupjs.org) and [Babel](https://babeljs.io) for ES2015 support with module loading.
* Rollup plugins (`rollup.config.js`):
  * eslint
  * uglifyjs with sourcemaps (disabled by default)
  * support for using any installed node modules on the webiste
  * display file size information
* Examples in `/site/javascript/main.js` showing...
  * how to import ES6 modules (`point.js`)
  * how to import CommonJS modules (`vendor/jquery.js` via `globals.js`)
  * how to expose variables like `jQuery` globally (`globals.js`)
  * how to import plain old javascript files that might depend on global variables (`vendor/jquery-test-plugin.js`)
  * how to use external global variables without importing them (`main.js` + `.eslintrc`)
* Consideration for images, currently copying the directory only - to avoid slowdowns and non-essential dependancies. We encourage using SVG for UI vectors and pre-optimised UI photograph assets.
* An automated way to upload your site to a staging server using [dploy](https://github.com/LeanMeanFightingMachine/dploy).
* [Build commands](#build-scripts) for generating testable or deployable assets only

## Installation

To start a prototype using this bootstrap;

- [ ] **Get the files:** Clone this repository to a new directory, for example;
`git clone https://github.com/torchbox/design-in-browser-bootstrap.git new-project`.
- [ ] **Name the project:** Open `package.json` and replace the `name` with your project name [following npm guidelines](http://browsenpm.org/package.json#name).
- [ ] **Setup git**: Run `npm run git:init` in the root of your new project to remove existing git links with this repository and create a fresh project with the directory as is committed.
- [ ] **Install dependencies** Run `yarn install` to run the install process. `npm install` will work too, see [section about yarn below](#using-yarn).


## Developing with it

* To start the development environment `npm run lab` - to stop this process press `ctrl + c`.
* This will start Browsersync and open your default browser after the startup process is complete. You can change this configuation by modifying the `browsersync.config.js` file, documented here https://www.browsersync.io/docs/options.
* Source files for developing your project are in `site` and the distribution folder for the compiled assets is `dist`. Any changes made to files in the `dist` directory will be overwritten.

### Using yarn

* Yarn is the recommended way to install and upgrade node modules. It's like npm but [handles dependencies better](http://stackoverflow.com/questions/40057469/what-is-the-difference-between-yarn-lock-and-npm-shrinkwrap#answer-40057535).
* Install yarn itself: https://yarnpkg.com/en/docs/install
* Install all packages from `package.json`: `yarn install`
* Add new packages with yarn: `yarn add --dev package_name` (this will add it to `package.json` and `yarn.lock` too)
* Upgrade packages: `yarn upgrade-interactive`
* Keep using `npm` for running npm scripts. Although `yarn run` seems to work as well but `npm-run-all` might not use yarn, so stick to `npm run` for now.


## Deploying it

### Deploy script

You can take advantage of the nodejs package [dploy](https://github.com/LeanMeanFightingMachine/dploy) to upload the `/dist` directory. To do so you will need to;

 * Make a copy of `example.dploy.yaml` and name it `dploy.yaml`.
 * Modify the `host` `user` and `path.remote` variables.
 * Run `npm run deploy` to start the deployment process.

### Build scripts

To only build assets for either development or production you can use

 * `npm run build` To build development assets
 * `npm run build:prod` To build assets with minification and vendor prefixes

### Debug script

To test production, minified and vendor prefixed assets you can use

 * `npm run debug` To develop with a simple http server, no browsersync and production assets


## Troubleshooting

### Installation
If you see the following error you can resolve node permissions using these steps: https://github.com/npm/npm/wiki/Troubleshooting#permission-error

```
npm WARN package.json globalwitness@0.0.1 No repository field.
npm ERR! Error: EACCES, mkdir '/Users/Dave/.npm/depd/1.0.0'
npm ERR!  { [Error: EACCES, mkdir '/Users/Dave/.npm/depd/1.0.0']
npm ERR!   errno: 3,
npm ERR!   code: 'EACCES',
npm ERR!   path: '/Users/Dave/.npm/depd/1.0.0',
npm ERR!   parent: 'connect' }
npm ERR!
npm ERR! Please try running this command again as root/Administrator.

```

## Technical Debt

 - 30 minute timeout from patternlab is hardcoded and within the vendor directory, a value has been modified in vendor/pattern-lab/core/src/PatternLab/Console/Commands/WatchCommand.php

## License

Copyright (c) 2016 Torchbox Ltd

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.![license](https://img.shields.io/github/license/pattern-lab/edition-php-twig-standard.svg)
[![Packagist](https://img.shields.io/packagist/v/pattern-lab/edition-twig-standard.svg)](https://packagist.org/packages/pattern-lab/edition-mustache-webdesignday) [![Gitter](https://img.shields.io/gitter/room/pattern-lab/php.svg)](https://gitter.im/pattern-lab/php)

# Pattern Lab Standard Edition for Twig

The Standard Edition for Twig gives developers and designers a clean and stable base from which to develop a Twig-based pattern library.

## Packaged Components

The Standard Edition for Twig comes with the following components:

* `pattern-lab/core`: [GitHub](https://github.com/pattern-lab/patternlab-php-core), [Packagist](https://packagist.org/packages/pattern-lab/core)
* `pattern-lab/patternengine-twig`: [documentation](https://github.com/pattern-lab/patternengine-php-twig#twig-patternengine-for-pattern-lab-php), [GitHub](https://github.com/pattern-lab/patternengine-php-twig), [Packagist](https://packagist.org/packages/pattern-lab/patternengine-twig)
* `pattern-lab/styleguidekit-assets-default`: [GitHub](https://github.com/pattern-lab/styleguidekit-assets-default), [Packagist](https://packagist.org/packages/pattern-lab/styleguidekit-assets-default)
* `pattern-lab/styleguidekit-twig-default`: [GitHub](https://github.com/pattern-lab/styleguidekit-twig-default), [Packagist](https://packagist.org/packages/pattern-lab/styleguidekit-twig-default)

## Installing

There are two methods for downloading and installing the Standard Edition for Twig:

* [Download a pre-built project](#download-a-pre-built-package)
* [Use Composer to create a project](#use-composer-to-create-a-project)

### Download a pre-built project

The fastest way to get started with the Standard Edition for Twig is to [download the pre-built version](https://github.com/pattern-lab/edition-php-twig-standard/releases) from the [releases page](https://github.com/pattern-lab/edition-php-twig-standard/releases). The pre-built project comes with the [Base StarterKit for Twig](https://github.com/pattern-lab/starterkit-twig-base) installed by default.

**Please note:** Pattern Lab uses [Composer](https://getcomposer.org/) to manage project dependencies. To upgrade the Standard Edition for Twig or to install plug-ins you'll need to [install Composer](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx). We recommend that you [install it globally](https://getcomposer.org/doc/00-intro.md#globally).

### Use Composer to create a project

Pattern Lab uses [Composer](https://getcomposer.org/) to manage project dependencies.

#### 1. Install Composer

Please follow the directions for [installing Composer](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx) on the Composer website. We recommend you [install it globally](https://getcomposer.org/doc/00-intro.md#globally).

#### 2. Install the Standard Edition for Twig

Use Composer's [`create-project` command](https://getcomposer.org/doc/03-cli.md#create-project) to install the Standard Edition for Twig into a location of your choosing. In Terminal type:

    cd install/location/
    composer create-project pattern-lab/edition-twig-standard your-project-name && cd $_

This will install the Standard Edition for Twig into a directory called `your-project-name` in `install/location/`. During the set-up process you will be asked to install an appropriate StarterKit. You will be automatically dropped into the project directory after the process is finished.

## Updating Pattern Lab

To update Pattern Lab please refer to each component's GitHub repository. The components are listed at the top of the README.

## Helpful Commands

These are some helpful commands you can use on the command line for working with Pattern Lab.

### List all of the available commands

To list all available commands type:

    php core/console --help

To list the options for a particular command type:

    php core/console --help --[command]

### Generate Pattern Lab

To generate the front-end for Pattern Lab type:

    php core/console --generate

### Watch for changes and re-generate Pattern Lab

To watch for changes and re-generate the front-end for Pattern Lab type:

    php core/console --watch

### Start a server to view Pattern Lab

You can use PHP's built-in web server to review your Pattern Lab project in a browser. In a seperate window type:

    php core/console --server

Then open [http://localhost:8080](http://localhost:8080) in your browser.

### Install a StarterKit

To install a near-empty StarterKit as a starting point for your project type:

    php core/console --starterkit --init

To install a specific StarterKit from GitHub type:

    php core/console --starterkit --install <starterkit-vendor/starterkit-name>
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
EventDispatcher Component
=========================

The EventDispatcher component provides tools that allow your application
components to communicate with each other by dispatching events and listening to
them.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/event_dispatcher/index.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
Process Component
=================

The Process component executes commands in sub-processes.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/process.html)
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
Finder Component
================

The Finder component finds files and directories via an intuitive fluent
interface.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/finder.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
JSON Lint
=========

[![Build Status](https://secure.travis-ci.org/Seldaek/jsonlint.png)](http://travis-ci.org/Seldaek/jsonlint)

Usage
-----

```php
use Seld\JsonLint\JsonParser;

$parser = new JsonParser();
    
// returns null if it's valid json, or a ParsingException object.
$parser->lint($json);

// Call getMessage() on the exception object to get
// a well formatted error message error like this

// Parse error on line 2:
// ... "key": "value"    "numbers": [1, 2, 3]
// ----------------------^
// Expected one of: 'EOF', '}', ':', ',', ']'

// Call getDetails() on the exception to get more info.

// returns parsed json, like json_decode() does, but slower, throws
// exceptions on failure.
$parser->parse($json);
```

Installation
------------

For a quick install with Composer use:

    $ composer require seld/jsonlint

JSON Lint can easily be used within another app if you have a
[PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)
autoloader, or it can be installed through [Composer](https://getcomposer.org/)
for use as a CLI util.
Once installed via Composer you can run the following command to lint a json file or URL:

    $ bin/jsonlint file.json

Requirements
------------

- PHP 5.3+
- [optional] PHPUnit 3.5+ to execute the test suite (phpunit --version)

Submitting bugs and feature requests
------------------------------------

Bugs and feature request are tracked on [GitHub](https://github.com/Seldaek/jsonlint/issues)

Author
------

Jordi Boggiano - <j.boggiano@seld.be> - <http://twitter.com/seldaek>

License
-------

JSON Lint is licensed under the MIT License - see the LICENSE file for details

Acknowledgements
----------------

This library is a port of the JavaScript [jsonlint](https://github.com/zaach/jsonlint) library.
[![Build Status](https://travis-ci.org/Shudrum/ArrayFinder.svg?branch=master)](https://travis-ci.org/Shudrum/ArrayFinder)

#ArrayFinder Component

The ArrayFinder component allow you to manage large nested arrays with ease.

Here is a simple example that shows how to easily get a value from an array:

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder([
    'level_1' => [
        'level_2' => [
            'level_3' => 'value',
        ],
    ],
]);

$myValue = $arrayFinder->get('level_1.level_2.level_3');
// OR
$myValue = $arrayFinder['level_1.level_2.level_3'];
```

To install this package, you can simply use composer:

```
composer require shudrum/array-finder
```

##Documentation

###Methods

####get($path)

You can get a value following a path separated by a '.'.

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder([
    'a' => [
        'b' => [
            'c' => 'value1',
        ],
        'value2',
    ],
    'value3',
]);

$myValue = $arrayFinder->get('a.b.c'); // value1
$myValue = $arrayFinder->get('a.0'); // value2
$myValue = $arrayFinder->get(0); // value3
```

If the path is `null`, all the content will be returned.

####set($path, $value)

You can add a value to a specific path separated by a '.'. If the nested arrays does not exists, it will be created.

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder();
$arrayFinder->set('a.b', 'value');

$arrayFinder->get(); // ['a' => ['b' => 'value]]
```

####changeSeparator($separator)

If the default separator (.) does not fit to your needs, you can call this method to change it.

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder([…]);

$myValue = $arrayFinder->changeSeparator('/');
$myValue = $arrayFinder->get('a/b/c');
```

###Implementations

The ArrayFinder component implements some usefull interfaces:

####ArrayAccess

You can use this object like an array:

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder([…]);

$value = $arrayFinder['a.b'];
$arrayFinder['a.b.c'] = 'value';
unset($arrayFinder['a.b']);
```

####Countable

You can use count on this object:

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder([…]);

count($arrayFinder);
count($arrayFinder['a.b']);
```

####Iterator

You can iterate on this object:

```php
use Shudrum\Component\ArrayFinder\ArrayFinder;

$arrayFinder = new ArrayFinder([…]);

foreach ($arrayFinder as $key => $value) {
    // …
}
```

####Serializable

You can easily serialize / unserialize this object.

##Resources

You can run the unit tests with the following command:

    $ cd path/to/Shudrum/Component/ArrayFinder/
    $ composer install
    $ phpunit
![license](https://img.shields.io/github/license/pattern-lab/patternlab-php-core.svg)
[![Packagist](https://img.shields.io/packagist/v/pattern-lab/core.svg)](https://packagist.org/packages/pattern-lab/core) [![Gitter](https://img.shields.io/gitter/room/pattern-lab/php.svg)](https://gitter.im/pattern-lab/php)

# Pattern Lab Core

This repository contains the core functionality for Pattern Lab. Pattern Lab Core is designed to be included as a dependency within Editions. Turn it up.
# Twig PatternEngine for Pattern Lab

The Twig PatternEngine allows you to use [Twig](http://twig.sensiolabs.org) as the template language for Pattern Lab PHP. Once the PatternEngine is installed you can use Twig-based StarterKits and StyleguideKits.

## Installation

The Twig PatternEngine comes pre-installed with the [Pattern Lab Standard Edition for Twig](https://github.com/pattern-lab/edition-php-twig-standard). Please start there for all your Twig needs.

### Composer

Pattern Lab PHP uses [Composer](https://getcomposer.org/) to manage project dependencies with Pattern Lab Editions. To add the Twig PatternEngine to the dependencies list for your Edition you can type the following in the command line at the base of your project:

    composer require pattern-lab/patternengine-twig

See Packagist for [information on the latest release](https://packagist.org/packages/pattern-lab/patternengine-twig).

## Overview

This document is broken into three parts:

* [Working with Patterns and Twig](#working-with-patterns-and-twig)
* [Extending Twig Further](#extending-twig-further)
* [Available Loaders for Plugin Developers](#available-loaders)

## Working with Patterns and Twig

Twig provides access to two features that may help you extend your patterns, [macros](http://twig.sensiolabs.org/doc/templates.html#macros) and layouts via[template inheritance](http://twig.sensiolabs.org/doc/templates.html#template-inheritance). The Twig PatternEngine also supports the [pattern partial syntax](http://patternlab.io/docs/pattern-including.html) to make including one pattern within another very easy.

* [Pattern includes](#pattern-includes)
* [Macros](#macros)
* [Template inheritance](#template-inheritance)

### Pattern includes

Pattern includes take advantage of the [pattern partial syntax](http://patternlab.io/docs/pattern-including.html) as a shorthand for referencing patterns from across the system without needing to rely on absolute paths. The format:

```
{% include "[patternType]-[patternName]" %}
```

For example, let's say we wanted to include the following pattern in a molecule:

```
source/_patterns/00-atoms/03-images/02-landscape-16x9.twig
```

The **pattern type** is _atoms_ (from `00-atoms`) and the **pattern name** is _landscape-16x9_ from (from `02-landscape-16x9.twig`). Pattern sub-types are never used in this format and any digits for re-ordering are dropped. The shorthand partial syntax for this pattern would be:

```
{% include "atoms-landscape-16x9" %}
```

### Macros

The requirements for using macros with Pattern Lab:

* Files must go in `source/_macros`
* Files must have the extension `.macro.twig` (_this can be modified in the config_)
* The filename will be used as the base variable name in Twig templates

**Please note:** ensure that there is no overlap between the keys for your macros and the keys for your data attributes. A macro with the name `forms.macro.twig` will conflict with a root key with the name `forms` in your JSON/YAML. Both are accessed via `{{ forms }}` in Twig.

An example of a simple macro called `forms.macro.twig` in `source/_macros`:

```twig
{% macro input(name) %}
    <input type="radio" name="{{ name }}" value="Dave" /> {{ name }}
{% endmacro %}
```

Would be used like this in a pattern:

```twig
{{ forms.input("First name") }}
```

### Template inheritance

How to use [Template Inheritance](http://twig.sensiolabs.org/doc/templates.html#template-inheritance) with Pattern Lab:

* Files must have the extension `.twig`.
* Files can be extended either by using Pattern Lab's normal shorthand syntax (e.g, `{% extends 'templates-extended-layout'%}`).
* Files can optionally go in `source/_layouts` in order to hide them from the list of patterns and then you can just use the filename as reference (e.g., `{% extends 'extended-layout'%}`).
* Files that are in the same directory can also just use the file name without the shorthand syntax (however, it must include the extension). So if `file1.twig` and `file2.twig` were in same directory, you could place this code in `file2.twig`: `{% extends 'file1.twig' %}`. 

An example of a simple layout called `base.twig` in `source/_layouts`:

```twig
<!DOCTYPE html>
<html>
    <head>
        {% block head %}
            <link rel="stylesheet" href="style.css" />
            <title>{% block title %}{% endblock %} - My Webpage</title>
        {% endblock %}
    </head>
    <body>
        <div id="content">{% block content %}{% endblock %}</div>
        <div id="footer">
            {% block footer %}
                &copy; Copyright 2011 by <a href="http://domain.invalid/">you</a>.
            {% endblock %}
        </div>
    </body>
</html>
```

Would be used like this in a pattern:

```twig
{% extends "base.twig" %}

{% block title %}Index{% endblock %}
{% block head %}
    {{ parent() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
        Welcome on my awesome homepage.
    </p>
{% endblock %}
```

All uses of `extends` above also work with `includes`, `embed` and most likely many other Twig Tags. Let us know if you run into interesting or unexpected use cases!

## Extending Twig Further

Twig comes with a number of ways to extend the underlying template parser. You can you can add [extra tags](http://twig.sensiolabs.org/doc/advanced.html#tags), [filters](http://twig.sensiolabs.org/doc/advanced.html#filters), [tests](http://twig.sensiolabs.org/doc/advanced.html#tests), and [functions](http://twig.sensiolabs.org/doc/advanced.html#functions). The Twig PatternEngine tries to simplify these extensions by allowing you to create files in specific folders and then auto-load the extensions for you. Learn more about:

* [Filters](#filters)
* [Functions](#functions)
* [Tags](#tags)
* [Tests](#tests)

You can also:

* [Enable `dump()`](#enable-dump)
* [Modify the Default Date and Interval Formats](#modify-the-default-date-and-interval-formats)
* [Quickly disable extensions](#quickly-disable-extensions)

### Filters

The requirements for using filters with Pattern Lab:

* Files must go in `source/_twig-components/filters`
* Files must have the extension `.filter.php` (_this can be modified in the config_)
* The filter **must** set the variable `$filter`
* Only one filter per file (_e.g. can only set `$filter` once per file_)

An example function called `rot13.filter.php` in `source/_twig-components/filters`:

```php
<?php

$filter = new Twig_SimpleFilter('rot13', function ($string) {
	return str_rot13($string);
});

?>
```

This filter would be used like this in a pattern:

```twig
{{ bar|rot13 }}
```

### Functions

The requirements for using functions with Pattern Lab:

* Files must go in `source/_twig-components/functions`
* Files must have the extension `.function.php` (_this can be modified in the config_)
* The function **must** set the variable `$function`
* Only one function per file (_e.g. can only set `$function` once per file_)

An example function called `boo.function.php` in `source/_twig-components/functions`:

```php
<?php

$function = new Twig_SimpleFunction('boo', function ($string) {
	return $string." boo! ";
});

?>
```

This function would be used like this in a pattern:

```twig
{{ boo("ghost says what?") }}
```

### Tests

The requirements for using tests with Pattern Lab:

* Files must go in `source/_twig-components/tests`
* Files must have the extension `.test.php` (_this can be modified in the config_)
* The test **must** set the variable `$test`
* Only one test per file (_e.g. can only set `$test` once per file_)

An example of a simple test called `red.test.php` in `source/_twig-components/tests`:

```php
<?php

$test = new Twig_SimpleTest('red', function ($value) {
	
	if (isset($value["color"]) && $value["color"] == 'red') {
		return true;
	}
	
	return false;
});

?>
```

This test would be used like this in a pattern:

```twig
{% if shirt is red %}
	Why did I ever sign-up with Starfleet?
{% endif %}
```

Where the JSON for the data to set `shirt` would be:

```json
"shirt": {
	"color": "red"
}
```

**Reminder:** all data in Pattern Lab is stored as an array and _not_ as an object. So `$object->attribute` won't work in tests.

### Tags

The requirements for using tags with Pattern Lab:

* Files must go in `source/_twig-components/tags`
* Files must have the extension `.tag.php` (_this can be modified in the config_)
* The filename **must** be reflected in class names. (e.g. `Project_{filename}_Node` and `Project_{filename}_TokenParser`)
* Only one tag per file

Tags are the most complicated extension to set-up with Pattern Lab. Three steps are needed to define a new tag in Twig:

* Defining a Token Parser class (_responsible for parsing the template code_)
* Defining a Node class (_responsible for converting the parsed code to PHP_)
* Registering the tag.

Pattern Lab takes care of the registering for you based on the file name.

An example of a simple tag called `setdupe.tag.php` in `source/_twig-components/tags` that mimics the default `set` tag. Please note all of the locations where class names incorporate the filename, `setdupe`.

```php
<?php

// these files are loaded three times and we can't re-set a class
if (!class_exists("Project_setdupe_Node")) {
	
	class Project_setdupe_Node extends Twig_Node {
		
		public function __construct($name, Twig_Node_Expression $value, $line, $tag = null) {
			parent::__construct(array('value' => $value), array('name' => $name), $line, $tag);
		}
		
		public function compile(Twig_Compiler $compiler) {
			$compiler
				->addDebugInfo($this)
				->write('$context[\''.$this->getAttribute('name').'\'] = ')
				->subcompile($this->getNode('value'))
				->raw(";\n");
		}
		
	}
	
}

// these files are loaded three times and we can't re-set a class
if (!class_exists("Project_setdupe_TokenParser")) {
	
	class Project_setdupe_TokenParser extends Twig_TokenParser {
		
		public function parse(Twig_Token $token) {
			
			$parser = $this->parser;
			$stream = $parser->getStream();
			
			$name = $stream->expect(Twig_Token::NAME_TYPE)->getValue();
			$stream->expect(Twig_Token::OPERATOR_TYPE, '=');
			$value = $parser->getExpressionParser()->parseExpression();
			$stream->expect(Twig_Token::BLOCK_END_TYPE);
			
			return new Project_setdupe_Node($name, $value, $token->getLine(), $this->getTag());
		}
		
		public function getTag() {
			return 'setdupe';
		}
		
	}
	
}

?>
```

This tag would be used like this in a pattern:

```
{% setdupe name = "Ziggy" %}
{{ name }}
```

### Enable `dump()`

To use `dump()` set `twigDebug` in `config/config.yml` to `true`.

### Modify the Default Date and Interval Formats

You can modify the default date and interval formats for Twig by editing the `twigDefaultDateFormat` and `twigDefaultIntervalFormat` in `config/config.yml`. Set them to an empty string to use Twig's default formats. **Please note:** both must be set for this feature to work.

### Quickly Disable Extensions

To disable extensions that you're no longer using simply add an underscore to the beginning of a filename and then re-generate your site. For example, the enabled rot13 filter:

    source/_twig-components/filters/rot13.filter.php

And the disabled rot13 filter:

    source/_twig-components/filters/_rot13.filter.php

Then re-generate your Pattern Lab site with:

    php core/console --generate

## Available Loaders

If you're building a plugin that will be parsing Twig files you have access to three loaders. It's recommended that you use these instead of accessing Twig directly as these loaders will work with other PatternEngines.

### The String Loader

The string loader takes a simple string and compiles it. To use:

```php
$data         = array("hello" => "world");
$string       = "If I say hello you say {{ hello }}.";
$stringLoader = \PatternLab\Template::getStringLoader();
$output       = $stringLoader->render(array("string" => $string, "data" => $data));
print $output; // outputs "If I say hello you say world."
```

### The Filesystem Loader

The filesystem loader will look for templates in the configured StyleguideKit directory and compile them. The template location for the filesystem loader can't be modified. To use:

```php
$data             = array(...);
$filesystemLoader = \PatternLab\Template::getFilesystemLoader();
$output           = $filesystemLoader->render(array("template" => "viewall", "data" => $data));
print $output; // outputs the viewall view from the configured styleguidekit
```

### The Pattern Loader

The pattern loader looks for patterns and allows the use of the Pattern Lab-specific partial syntax. To use:

```php
$data                  = array(...);
$patternContent        = file_get_contents("path/to/pattern");
$patternEngineBasePath = \PatternLab\PatternEngine::getInstance()->getBasePath();
$patternLoaderClass    = $patternEngineBasePath."\Loaders\PatternLoader";
$patternLoader         = new $patternLoaderClass($options);
$code                  = $patternLoader->render(array("pattern" => $patternContent, "data" => $data));
print $output; // outputs the given pattern
```
![license](https://img.shields.io/github/license/pattern-lab/styleguidekit-assets-default.svg)
[![Packagist](https://img.shields.io/packagist/v/pattern-lab/styleguidekit-assets-default.svg)](https://packagist.org/packages/pattern-lab/styleguidekit-assets-default) [![Gitter](https://img.shields.io/gitter/room/pattern-lab/frontend-viewer.svg)](https://gitter.im/pattern-lab/frontend-viewer)

# Static Assets for the Default StyleguideKit

These static assets are meant to be used with the default [Mustache](https://github.com/pattern-lab/styleguidekit-mustache-default) and [Twig](https://github.com/pattern-lab/styleguidekit-twig-default) StyleguideKits. They control the look, feel, and functionality of the front-end of Pattern Lab PHP.

## Installation

Pattern Lab PHP uses [Composer](https://getcomposer.org/) to manage project dependencies. To install the default static assets run:

    composer require pattern-lab/styleguidekit-assets-default

## Development Requirements

In order to modify these assets you need to install the following:

* the [Development Edition of Pattern Lab PHP](https://github.com/pattern-lab/edition-php-development)
* [Node.js](http://nodejs.org) and NPM
* [Bower](http://bower.io)
* [Ruby Sass](http://sass-lang.com/install)
	
## Development Set-up

Once you've installed the requirements do the following to set-up for development:

1. `cd /path/to/dev-edition/packages/pattern-lab/styleguidekit-assets-default`
2. `git config branch.dev.remote origin`
3. `npm install`
4. `bower install`

## Making Changes

To make changes **always edit files in `src/`**. To make sure that these changes are reflected in the front-end and `dist/` folder run the following:

    gulp --copy-dist=../../../public

To watch for changes you can use:

    gulp --watch --copy-dist=../../../public

At this point changes to the static assets should compile to the correct locations in the project as well as `dist/`.
# Twig Templates for the Default StyleguideKit

These Twig templates are meant to be used with the [static assets](https://github.com/pattern-lab/styleguidekit-assets-default) for the default StyleguideKit. The Twig templates are for the "view all" view in Pattern Lab PHP.

## Installation

Pattern Lab PHP uses [Composer](https://getcomposer.org/) to manage project dependencies. To install the Twig templates run:

    composer require pattern-lab/styleguidekit-twig-default

## Development Requirements

In order to modify these templates you need to install the following:

* the [Twig Development Edition of Pattern Lab PHP](https://github.com/pattern-lab/edition-php-twig-development)

## Development Set-up

Once you've installed the requirements do the following to set-up for development:

1. `cd /path/to/dev-edition/packages/pattern-lab/styleguidekit-twig-default`
2. `git config branch.dev.remote origin`

## Making Changes

Simply edit the files in `views/`.
There should be no reason to touch these files in day-to-day use.# Doctrine Collections

[![Build Status](https://travis-ci.org/doctrine/collections.svg?branch=master)](https://travis-ci.org/doctrine/collections)

Collections Abstraction library

## Changelog

### v1.3.0

* [Explicit casting of first and max results in criteria API](https://github.com/doctrine/collections/pull/26)
* [Keep keys when using `ArrayCollection#matching()` with sorting](https://github.com/doctrine/collections/pull/49)
* [Made `AbstractLazyCollection#$initialized` protected for extensibility](https://github.com/doctrine/collections/pull/52)

### v1.2.0

* Add a new ``AbstractLazyCollection``

### v1.1.0

* Deprecated ``Comparison::IS``, because it's only there for SQL semantics.
  These are fixed in the ORM instead.
* Add ``Comparison::CONTAINS`` to perform partial string matches:

        $criteria->andWhere($criteria->expr()->contains('property', 'Foo'));
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
