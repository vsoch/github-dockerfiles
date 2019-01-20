# Ghost S3

This is an S3 file module for Ghost blogs.



## Install

	npm install --save ghost-s3


## Configure

In your ghost config.js file under "development" and "production" add

	aws: {
	    accessKeyId: 'your aws access key id>',
	    secretAccessKey: 'your AWS secret access key>',
	    bucket: 'your-bucket-name',
	    region: 'the AWS region your bucket is in'
	},


## Plug In

Until Ghost has a file module system, you will have to change the file ```storage/index```

```javascript
	storage = require('./' + storageChoice);
```

becomes

```javascript
	storage = require('ghost-s3')({
	    errors: errors,
	    config: require('../config')().aws
	});
```


# AWS SDK for JavaScript [![Version](https://badge.fury.io/js/aws-sdk.png)](http://badge.fury.io/js/aws-sdk) [![Build Status](https://travis-ci.org/aws/aws-sdk-js.png?branch=master)](https://travis-ci.org/aws/aws-sdk-js)

The official AWS SDK for JavaScript, available for browsers and mobile devices,
or Node.js backends

Release notes can be found at http://aws.amazon.com/releasenotes/SDK/JavaScript

## Installing

### In the Browser

To use the SDK in the browser, simply add the following script tag to your
HTML pages:

    <script src="https://sdk.amazonaws.com/js/aws-sdk-2.0.0-rc9.min.js"></script>

### In Node.js

The preferred way to install the AWS SDK for Node.js is to use the
[npm](http://npmjs.org) package manager for Node.js. Simply type the following
into a terminal window:

```sh
npm install aws-sdk
```

## Usage and Getting Started

You can find a getting started guide at:

http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/

## Supported Services

The SDK currently supports the following services:

<table>
  <thead>
    <th>Service Name</th>
    <th>Class Name</th>
    <th>API Version</th>
  </thead>
  <tbody>
    <tr><td rowspan="2">Amazon CloudFront</td><td rowspan="2">AWS.CloudFront</td><td>2012-05-05</td></tr>
    <tr><td>2013-11-11</td></tr>
    <tr><td>Amazon CloudSearch</td><td>AWS.CloudSearch</td><td>2011-02-01</td></tr>
    <tr><td>Amazon CloudWatch</td><td>AWS.CloudWatch</td><td>2010-08-01</td></tr>
    <tr><td rowspan="2">Amazon DynamoDB</td><td rowspan="2">AWS.DynamoDB</td><td>2011-12-05</td></tr>
    <tr><td>2012-08-10</td></tr>
    <tr><td>Amazon Elastic Compute Cloud</td><td>AWS.EC2</td><td>2013-10-15</td></tr>
    <tr><td>Amazon Elastic MapReduce</td><td>AWS.EMR</td><td>2009-03-31</td></tr>
    <tr><td>Amazon Elastic Transcoder</td><td>AWS.ElasticTranscoder</td><td>2012-09-25</td></tr>
    <tr><td>Amazon ElastiCache</td><td>AWS.ElastiCache</td><td>2013-06-15</td></tr>
    <tr><td>Amazon Glacier</td><td>AWS.Glacier</td><td>2012-06-01</td></tr>
    <tr><td>Amazon Kinesis</td><td>AWS.Kinesis</td><td>2013-12-02</td></tr>
    <tr><td>Amazon Redshift</td><td>AWS.Redshift</td><td>2012-12-01</td></tr>
    <tr><td rowspan="3">Amazon Relational Database Service</td><td rowspan="3">AWS.RDS</td><td>2013-01-10</td></tr>
    <tr><td>2013-02-12</td></tr>
    <tr><td>2013-09-09</td></tr>
    <tr><td>Amazon Route 53</td><td>AWS.Route53</td><td>2012-12-12</td></tr>
    <tr><td>Amazon Simple Email Service</td><td>AWS.SES</td><td>2010-12-01</td></tr>
    <tr><td>Amazon Simple Notification Service</td><td>AWS.SNS</td><td>2010-03-31</td></tr>
    <tr><td>Amazon Simple Queue Service</td><td>AWS.SQS</td><td>2012-11-05</td></tr>
    <tr><td>Amazon Simple Storage Service</td><td>AWS.S3</td><td>2006-03-01</td></tr>
    <tr><td>Amazon Simple Workflow Service</td><td>AWS.SimpleWorkflow</td><td>2012-01-25</td></tr>
    <tr><td>Amazon SimpleDB</td><td>AWS.SimpleDB</td><td>2009-04-15</td></tr>
    <tr><td>Auto Scaling</td><td>AWS.AutoScaling</td><td>2011-01-01</td></tr>
    <tr><td>AWS CloudFormation</td><td>AWS.CloudFormation</td><td>2010-05-15</td></tr>
    <tr><td>AWS CloudTrail</td><td>AWS.CloudTrail</td><td>2013-11-01</td></tr>
    <tr><td>AWS Data Pipeline</td><td>AWS.DataPipeline</td><td>2012-10-29</td></tr>
    <tr><td>AWS Direct Connect</td><td>AWS.DirectConnect</td><td>2012-10-25</td></tr>
    <tr><td>AWS Elastic Beanstalk</td><td>AWS.ElasticBeanstalk</td><td>2010-12-01</td></tr>
    <tr><td>AWS Identity and Access Management</td><td>AWS.IAM</td><td>2010-05-08</td></tr>
    <tr><td>AWS Import/Export</td><td>AWS.ImportExport</td><td>2010-06-01</td></tr>
    <tr><td>AWS OpsWorks</td><td>AWS.OpsWorks</td><td>2013-02-18</td></tr>
    <tr><td>AWS Security Token Service</td><td>AWS.STS</td><td>2011-06-15</td></tr>
    <tr><td rowspan="2">AWS Storage Gateway</td><td rowspan="2">AWS.StorageGateway</td><td>2012-06-30</td></tr>
    <tr><td>2013-06-30</td></tr>
    <tr><td>AWS Support</td><td>AWS.Support</td><td>2013-04-15</td></tr>
    <tr><td>Elastic Load Balancing</td><td>AWS.ELB</td><td>2012-06-01</td></tr>
  </tbody>
</table>

## License

This SDK is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

```no-highlight
Copyright 2012-2014. Amazon Web Services, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# xmlbuilder-js

An XMLBuilder for [node.js](http://nodejs.org/) similar to 
[java-xmlbuilder](http://code.google.com/p/java-xmlbuilder/).

[![Build Status](https://secure.travis-ci.org/oozcitak/xmlbuilder-js.png)](http://travis-ci.org/oozcitak/xmlbuilder-js)

### Installation:

``` sh
npm install xmlbuilder
```

### Important:

I had to break compatibility while adding multiple instances in 0.1.3. 
As a result, version from v0.1.3 are **not** compatible with previous versions.

### Usage:

``` js
var builder = require('xmlbuilder');
var xml = builder.create('root')
  .ele('xmlbuilder', {'for': 'node-js'})
    .ele('repo', {'type': 'git'}, 'git://github.com/oozcitak/xmlbuilder-js.git')
  .end({ pretty: true});
    
console.log(xml);
```

will result in:

``` xml
<?xml version="1.0"?>
<root>
  <xmlbuilder for="node-js">
    <repo type="git">git://github.com/oozcitak/xmlbuilder-js.git</repo>
  </xmlbuilder>
</root>
```

If you need to do some processing:

``` js
var root = builder.create('squares');
root.com('f(x) = x^2');
for(var i = 1; i <= 5; i++)
{
  var item = root.ele('data');
  item.att('x', i);
  item.att('y', i * i);
}
```

This will result in:

``` xml
<?xml version="1.0"?>
<squares>
  <!-- f(x) = x^2 -->
  <data x="1" y="1"/>
  <data x="2" y="4"/>
  <data x="3" y="9"/>
  <data x="4" y="16"/>
  <data x="5" y="25"/>
</squares>
```

See the [Usage](https://github.com/oozcitak/xmlbuilder-js/wiki/Usage) page in the wiki for more detailed instructions.

### License:

`xmlbuilder-js` is [MIT Licensed](http://opensource.org/licenses/mit-license.php).
node-xml2js
===========

Ever had the urge to parse XML? And wanted to access the data in some sane,
easy way? Don't want to compile a C parser, for whatever reason? Then xml2js is
what you're looking for!

Description
===========

Simple XML to JavaScript object converter. Uses
[sax-js](https://github.com/isaacs/sax-js/).

Note: If you're looking for a full DOM parser, you probably want
[JSDom](https://github.com/tmpvar/jsdom).

Installation
============

Simplest way to install `xml2js` is to use [npm](http://npmjs.org), just `npm
install xml2js` which will download xml2js and all dependencies.

Usage
=====

No extensive tutorials required because you are a smart developer! The task of
parsing XML should be an easy one, so let's make it so! Here's some examples.

Shoot-and-forget usage
----------------------

You want to parse XML as simple and easy as possible? It's dangerous to go
alone, take this:

```javascript
var parseString = require('xml2js').parseString;
var xml = "<root>Hello xml2js!</root>"
parseString(xml, function (err, result) {
    console.dir(result);
});
```

Can't get easier than this, right? This works starting with `xml2js` 0.2.3.
With CoffeeScript it looks like this:

```coffeescript
parseString = require('xml2js').parseString
xml = "<root>Hello xml2js!</root>"
parseString xml, (err, result) ->
    console.dir result
```

If you need some special options, fear not, `xml2js` supports a number of
options (see below), you can specify these as second argument:

```javascript
parseString(xml, {trim: true}, function (err, result) {
});
```

Simple as pie usage
-------------------

That's right, if you have been using xml-simple or a home-grown
wrapper, this is was added in 0.1.11 just for you:

```javascript
var fs = require('fs'),
    xml2js = require('xml2js');

var parser = new xml2js.Parser();
fs.readFile(__dirname + '/foo.xml', function(err, data) {
    parser.parseString(data, function (err, result) {
        console.dir(result);
        console.log('Done');
    });
});
```

Look ma, no event listeners!

You can also use `xml2js` from
[CoffeeScript](http://jashkenas.github.com/coffee-script/), further reducing
the clutter:

```coffeescript
fs = require 'fs',
xml2js = require 'xml2js'

parser = new xml2js.Parser()
fs.readFile __dirname + '/foo.xml', (err, data) ->
  parser.parseString data, (err, result) ->
    console.dir result
    console.log 'Done.'
```

"Traditional" usage
-------------------

Alternatively you can still use the traditional `addListener` variant that was
supported since forever:

```javascript
var fs = require('fs'),
    xml2js = require('xml2js');

var parser = new xml2js.Parser();
parser.addListener('end', function(result) {
    console.dir(result);
    console.log('Done.');
});
fs.readFile(__dirname + '/foo.xml', function(err, data) {
    parser.parseString(data);
});
```

If you want to parse multiple files, you have multiple possibilites:

  * You can create one `xml2js.Parser` per file. That's the recommended one
    and is promised to always *just work*.
  * You can call `reset()` on your parser object.
  * You can hope everything goes well anyway. This behaviour is not
    guaranteed work always, if ever. Use option #1 if possible. Thanks!

So you wanna some JSON?
-----------------------

Just wrap the `result` object in a call to `JSON.stringify` like this
`JSON.stringify(result)`. You get a string containing the JSON representation
of the parsed object that you can feed to JSON-hungry consumers.

Displaying results
------------------

You might wonder why, using `console.dir` or `console.log` the output at some
level is only `[Object]`. Don't worry, this is not because xml2js got lazy.
That's because Node uses `util.inspect` to convert the object into strings and
that function stops after `depth=2` which is a bit low for most XML.

To display the whole deal, you can use `console.log(util.inspect(result, false,
null))`, which displays the whole result.

So much for that, but what if you use
[eyes](https://github.com/cloudhead/eyes.js) for nice colored output and it
truncates the output with `…`? Don't fear, there's also a solution for that,
you just need to increase the `maxLength` limit by creating a custom inspector
`var inspect = require('eyes').inspector({maxLength: false})` and then you can
easily `inspect(result)`.

Options
=======

Apart from the default settings, there is a number of options that can be
specified for the parser. Options are specified by ``new Parser({optionName:
value})``. Possible options are:

  * `attrkey` (default: `$`): Prefix that is used to access the attributes.
    Version 0.1 default was `@`.
  * `charkey` (default: `_`): Prefix that is used to access the character
    content. Version 0.1 default was `#`.
  * `explicitCharkey` (default: `false`)
  * `trim` (default: `false`): Trim the whitespace at the beginning and end of
    text nodes.
  * `normalizeTags` (default: `false`): Normalize all tag names to lowercase.
  * `normalize` (default: `false`): Trim whitespaces inside text nodes.
  * `explicitRoot` (default: `true`): Set this if you want to get the root
    node in the resulting object.
  * `emptyTag` (default: `undefined`): what will the value of empty nodes be.
    Default is `{}`.
  * `explicitArray` (default: `true`): Always put child nodes in an array if
    true; otherwise an array is created only if there is more than one.
  * `ignoreAttrs` (default: `false`): Ignore all XML attributes and only create
    text nodes.
  * `mergeAttrs` (default: `false`): Merge attributes and child elements as
    properties of the parent, instead of keying attributes off a child
    attribute object. This option is ignored if `ignoreAttrs` is `false`.
  * `validator` (default `null`): You can specify a callable that validates
    the resulting structure somehow, however you want. See unit tests
    for an example.
  * `xmlns` (default `false`): Give each element a field usually called '$ns'
    (the first character is the same as attrkey) that contains its local name
    and namespace URI.

Updating to new version
=======================

Version 0.2 changed the default parsing settings, but version 0.1.14 introduced
the default settings for version 0.2, so these settings can be tried before the
migration.

```javascript
var xml2js = require('xml2js');
var parser = new xml2js.Parser(xml2js.defaults["0.2"]);
```

To get the 0.1 defaults in version 0.2 you can just use
`xml2js.defaults["0.1"]` in the same place. This provides you with enough time
to migrate to the saner way of parsing in xml2js 0.2. We try to make the
migration as simple and gentle as possible, but some breakage cannot be
avoided.

So, what exactly did change and why? In 0.2 we changed some defaults to parse
the XML in a more universal and sane way. So we disabled `normalize` and `trim`
so xml2js does not cut out any text content. You can reenable this at will of
course. A more important change is that we return the root tag in the resulting
JavaScript structure via the `explicitRoot` setting, so you need to access the
first element. This is useful for anybody who wants to know what the root node
is and preserves more information. The last major change was to enable
`explicitArray`, so everytime it is possible that one might embed more than one
sub-tag into a tag, xml2js >= 0.2 returns an array even if the array just
includes one element. This is useful when dealing with APIs that return
variable amounts of subtags.

Running tests, development
==========================

[![Build Status](https://secure.travis-ci.org/Leonidas-from-XIV/node-xml2js.png?branch=master)](https://travis-ci.org/Leonidas-from-XIV/node-xml2js)

The development requirements are handled by npm, you just need to install them.
We also have a number of unit tests, they can be run using `npm test` directly
from the project root. This runs zap to discover all the tests and execute
them.

If you like to contribute, keep in mind that xml2js is written in CoffeeScript,
so don't develop on the JavaScript files that are checked into the repository
for convenience reasons. Also, please write some unit test to check your
behaviour and if it is some user-facing thing, add some documentation to this
README, so people will know it exists. Thanks in advance!
# sax js

A sax-style parser for XML and HTML.

Designed with [node](http://nodejs.org/) in mind, but should work fine in
the browser or other CommonJS implementations.

## What This Is

* A very simple tool to parse through an XML string.
* A stepping stone to a streaming HTML parser.
* A handy way to deal with RSS and other mostly-ok-but-kinda-broken XML
  docs.

## What This Is (probably) Not

* An HTML Parser - That's a fine goal, but this isn't it.  It's just
  XML.
* A DOM Builder - You can use it to build an object model out of XML,
  but it doesn't do that out of the box.
* XSLT - No DOM = no querying.
* 100% Compliant with (some other SAX implementation) - Most SAX
  implementations are in Java and do a lot more than this does.
* An XML Validator - It does a little validation when in strict mode, but
  not much.
* A Schema-Aware XSD Thing - Schemas are an exercise in fetishistic
  masochism.
* A DTD-aware Thing - Fetching DTDs is a much bigger job.

## Regarding `<!DOCTYPE`s and `<!ENTITY`s

The parser will handle the basic XML entities in text nodes and attribute
values: `&amp; &lt; &gt; &apos; &quot;`. It's possible to define additional
entities in XML by putting them in the DTD. This parser doesn't do anything
with that. If you want to listen to the `ondoctype` event, and then fetch
the doctypes, and read the entities and add them to `parser.ENTITIES`, then
be my guest.

Unknown entities will fail in strict mode, and in loose mode, will pass
through unmolested.

## Usage

```javascript
var sax = require("./lib/sax"),
  strict = true, // set to false for html-mode
  parser = sax.parser(strict);

parser.onerror = function (e) {
  // an error happened.
};
parser.ontext = function (t) {
  // got some text.  t is the string of text.
};
parser.onopentag = function (node) {
  // opened a tag.  node has "name" and "attributes"
};
parser.onattribute = function (attr) {
  // an attribute.  attr has "name" and "value"
};
parser.onend = function () {
  // parser stream is done, and ready to have more stuff written to it.
};

parser.write('<xml>Hello, <who name="world">world</who>!</xml>').close();

// stream usage
// takes the same options as the parser
var saxStream = require("sax").createStream(strict, options)
saxStream.on("error", function (e) {
  // unhandled errors will throw, since this is a proper node
  // event emitter.
  console.error("error!", e)
  // clear the error
  this._parser.error = null
  this._parser.resume()
})
saxStream.on("opentag", function (node) {
  // same object as above
})
// pipe is supported, and it's readable/writable
// same chunks coming in also go out.
fs.createReadStream("file.xml")
  .pipe(saxStream)
  .pipe(fs.createWriteStream("file-copy.xml"))
```


## Arguments

Pass the following arguments to the parser function.  All are optional.

`strict` - Boolean. Whether or not to be a jerk. Default: `false`.

`opt` - Object bag of settings regarding string formatting.  All default to `false`.

Settings supported:

* `trim` - Boolean. Whether or not to trim text and comment nodes.
* `normalize` - Boolean. If true, then turn any whitespace into a single
  space.
* `lowercase` - Boolean. If true, then lowercase tag names and attribute names
  in loose mode, rather than uppercasing them.
* `xmlns` - Boolean. If true, then namespaces are supported.
* `position` - Boolean. If false, then don't track line/col/position.
* `strictEntities` - Boolean. If true, only parse [predefined XML
  entities](http://www.w3.org/TR/REC-xml/#sec-predefined-ent)
  (`&amp;`, `&apos;`, `&gt;`, `&lt;`, and `&quot;`)

## Methods

`write` - Write bytes onto the stream. You don't have to do this all at
once. You can keep writing as much as you want.

`close` - Close the stream. Once closed, no more data may be written until
it is done processing the buffer, which is signaled by the `end` event.

`resume` - To gracefully handle errors, assign a listener to the `error`
event. Then, when the error is taken care of, you can call `resume` to
continue parsing. Otherwise, the parser will not continue while in an error
state.

## Members

At all times, the parser object will have the following members:

`line`, `column`, `position` - Indications of the position in the XML
document where the parser currently is looking.

`startTagPosition` - Indicates the position where the current tag starts.

`closed` - Boolean indicating whether or not the parser can be written to.
If it's `true`, then wait for the `ready` event to write again.

`strict` - Boolean indicating whether or not the parser is a jerk.

`opt` - Any options passed into the constructor.

`tag` - The current tag being dealt with.

And a bunch of other stuff that you probably shouldn't touch.

## Events

All events emit with a single argument. To listen to an event, assign a
function to `on<eventname>`. Functions get executed in the this-context of
the parser object. The list of supported events are also in the exported
`EVENTS` array.

When using the stream interface, assign handlers using the EventEmitter
`on` function in the normal fashion.

`error` - Indication that something bad happened. The error will be hanging
out on `parser.error`, and must be deleted before parsing can continue. By
listening to this event, you can keep an eye on that kind of stuff. Note:
this happens *much* more in strict mode. Argument: instance of `Error`.

`text` - Text node. Argument: string of text.

`doctype` - The `<!DOCTYPE` declaration. Argument: doctype string.

`processinginstruction` - Stuff like `<?xml foo="blerg" ?>`. Argument:
object with `name` and `body` members. Attributes are not parsed, as
processing instructions have implementation dependent semantics.

`sgmldeclaration` - Random SGML declarations. Stuff like `<!ENTITY p>`
would trigger this kind of event. This is a weird thing to support, so it
might go away at some point. SAX isn't intended to be used to parse SGML,
after all.

`opentag` - An opening tag. Argument: object with `name` and `attributes`.
In non-strict mode, tag names are uppercased, unless the `lowercase`
option is set.  If the `xmlns` option is set, then it will contain
namespace binding information on the `ns` member, and will have a
`local`, `prefix`, and `uri` member.

`closetag` - A closing tag. In loose mode, tags are auto-closed if their
parent closes. In strict mode, well-formedness is enforced. Note that
self-closing tags will have `closeTag` emitted immediately after `openTag`.
Argument: tag name.

`attribute` - An attribute node.  Argument: object with `name` and `value`.
In non-strict mode, attribute names are uppercased, unless the `lowercase`
option is set.  If the `xmlns` option is set, it will also contains namespace
information.

`comment` - A comment node.  Argument: the string of the comment.

`opencdata` - The opening tag of a `<![CDATA[` block.

`cdata` - The text of a `<![CDATA[` block. Since `<![CDATA[` blocks can get
quite large, this event may fire multiple times for a single block, if it
is broken up into multiple `write()`s. Argument: the string of random
character data.

`closecdata` - The closing tag (`]]>`) of a `<![CDATA[` block.

`opennamespace` - If the `xmlns` option is set, then this event will
signal the start of a new namespace binding.

`closenamespace` - If the `xmlns` option is set, then this event will
signal the end of a namespace binding.

`end` - Indication that the closed stream has ended.

`ready` - Indication that the stream has reset, and is ready to be written
to.

`noscript` - In non-strict mode, `<script>` tags trigger a `"script"`
event, and their contents are not checked for special xml characters.
If you pass `noscript: true`, then this behavior is suppressed.

## Reporting Problems

It's best to write a failing test if you find an issue.  I will always
accept pull requests with failing tests if they demonstrate intended
behavior, but it is very hard to figure out what issue you're describing
without a test.  Writing a test is also the best way for you yourself
to figure out if you really understand the issue you think you have with
sax-js.
<a href="http://promises-aplus.github.com/promises-spec"><img src="http://promises-aplus.github.com/promises-spec/assets/logo-small.png" alt="Promises/A+ logo" align="right" /></a>

[![Build Status](https://secure.travis-ci.org/cujojs/when.png)](http://travis-ci.org/cujojs/when) 

# when.js

When.js is cujoJS's lightweight [Promises/A+](http://promises-aplus.github.com/promises-spec) and `when()` implementation that powers the async core of [wire.js](https://github.com/cujojs/wire), cujoJS's IOC Container.  It features:

* A rock solid, battle-tested Promise implementation
* Resolving, settling, mapping, and reducing arrays of promises
* Executing tasks in parallel and sequence
* Transforming Node-style and other callback-based APIs into promise-based APIs

It passes the [Promises/A+ Test Suite](https://github.com/promises-aplus/promises-tests), is [very fast](https://github.com/cujojs/promise-perf-tests#test-results) and compact, and has no external dependencies.

- [What's new](CHANGES.md)
- [API docs](docs/api.md#api)
- [Examples](https://github.com/cujojs/when/wiki/Examples)
- [More info on the wiki](https://github.com/cujojs/when/wiki)

Quick Start
-----------

#### AMD

1. Get it
	- `bower install when` or `yeoman install when`, *or*
	- `git clone https://github.com/cujojs/when` or `git submodule add https://github.com/cujojs/when`
1. Configure your loader with a package:

	```js
	packages: [
		{ name: 'when', location: 'path/to/when/', main: 'when' },
		// ... other packages ...
	]
	```

1. `define(['when', ...], function(when, ...) { ... });` or `require(['when', ...], function(when, ...) { ... });`

#### Node

1. `npm install when`
1. `var when = require('when');`

#### RingoJS

1. `ringo-admin install cujojs/when`
1. `var when = require('when');`

#### Ender

1. `ender add cujojs/when`
2. `var when = require('when');`

#### Legacy environments (via browserify)

1. `git clone https://github.com/cujojs/when`
1. `npm install`
1. `npm run browserify` to generate `build/when.js`
	1. Or `npm run browserify-debug` to build with [when/monitor/console](docs/api.md#debugging-promises) enabled
1. `<script src="path/to/when/build/when.js"></script>`
	1. `when` will be available as `window.when`
	1. Other modules will be available as sub-objects/functions, e.g. `window.when.fn.lift`, `window.when.sequence`.  See the [full sub-namespace list in the browserify build file](build/when.browserify.js)

Running the Unit Tests
----------------------

#### Node

Note that when.js includes the [Promises/A+ Test Suite](https://github.com/promises-aplus/promise-tests).  Running unit tests in Node will run both when.js's own test suite, and the Promises/A+ Test Suite.

1. `npm install`
2. `npm test`

#### Browsers

1. `npm install`
2. `npm start` - starts buster server & prints a url
3. Point browsers at <buster server url>/capture, e.g. `localhost:1111/capture`
4. `npm run-script test-browser`

References
----------

Much of this code was inspired by the async innards of [wire.js](https://github.com/cujojs/wire), and has been influenced by the great work in [Q](https://github.com/kriskowal/q), [Dojo's Deferred](https://github.com/dojo/dojo), and [uber.js](https://github.com/phiggins42/uber.js).
# Promise monitoring and debugging

This dir contains experimental new promise monitoring and debugging utilities for when.js.  See [the docs](../docs/api.md#debugging-promises).
# Content / Data

This is the home of your Ghost database, do not overwrite this folder or any of the files inside of it.# Content / Images

If using the standard file storage, Ghost will upload images to this directory.# Casper

The default theme for [Ghost](http://github.com/tryghost/ghost/).

To download, visit the [releases](https://github.com/TryGhost/Casper/releases) page.

## Copyright & License

Copyright (c) 2013-2015 Ghost Foundation - Released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Content / Apps

Coming soon, Ghost apps will appear here.