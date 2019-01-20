# typedarray

TypedArray polyfill ripped from [this
module](https://raw.github.com/inexorabletash/polyfill).

[![build status](https://secure.travis-ci.org/substack/typedarray.png)](http://travis-ci.org/substack/typedarray)

[![testling badge](https://ci.testling.com/substack/typedarray.png)](https://ci.testling.com/substack/typedarray)

# example

``` js
var Uint8Array = require('typedarray').Uint8Array;
var ua = new Uint8Array(5);
ua[1] = 256 + 55;
console.log(ua[1]);
```

output:

```
55
```

# methods

``` js
var TA = require('typedarray')
```

The `TA` object has the following constructors:

* TA.ArrayBuffer
* TA.DataView
* TA.Float32Array
* TA.Float64Array
* TA.Int8Array
* TA.Int16Array
* TA.Int32Array
* TA.Uint8Array
* TA.Uint8ClampedArray
* TA.Uint16Array
* TA.Uint32Array

# install

With [npm](https://npmjs.org) do:

```
npm install typedarray
```

To use this module in the browser, compile with
[browserify](http://browserify.org)
or download a UMD build from browserify CDN:

http://wzrd.in/standalone/typedarray@latest

# license

MIT
# minimist

parse argument options

This module is the guts of optimist's argument parser without all the
fanciful decoration.

[![browser support](https://ci.testling.com/substack/minimist.png)](http://ci.testling.com/substack/minimist)

[![build status](https://secure.travis-ci.org/substack/minimist.png)](http://travis-ci.org/substack/minimist)

# example

``` js
var argv = require('minimist')(process.argv.slice(2));
console.dir(argv);
```

```
$ node example/parse.js -a beep -b boop
{ _: [], a: 'beep', b: 'boop' }
```

```
$ node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
{ _: [ 'foo', 'bar', 'baz' ],
  x: 3,
  y: 4,
  n: 5,
  a: true,
  b: true,
  c: true,
  beep: 'boop' }
```

# methods

``` js
var parseArgs = require('minimist')
```

## var argv = parseArgs(args, opts={})

Return an argument object `argv` populated with the array arguments from `args`.

`argv._` contains all the arguments that didn't have an option associated with
them.

Numeric-looking arguments will be returned as numbers unless `opts.string` or
`opts.boolean` is set for that argument name.

Any arguments after `'--'` will not be parsed and will end up in `argv._`.

options can be:

* `opts.string` - a string or array of strings argument names to always treat as
strings
* `opts.boolean` - a string or array of strings to always treat as booleans
* `opts.alias` - an object mapping string names to strings or arrays of string
argument names to use as aliases
* `opts.default` - an object mapping string argument names to default values

# install

With [npm](https://npmjs.org) do:

```
npm install minimist
```

# license

MIT
# minimist

parse argument options

This module is the guts of optimist's argument parser without all the
fanciful decoration.

[![browser support](https://ci.testling.com/substack/minimist.png)](http://ci.testling.com/substack/minimist)

[![build status](https://secure.travis-ci.org/substack/minimist.png)](http://travis-ci.org/substack/minimist)

# example

``` js
var argv = require('minimist')(process.argv.slice(2));
console.dir(argv);
```

```
$ node example/parse.js -a beep -b boop
{ _: [], a: 'beep', b: 'boop' }
```

```
$ node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
{ _: [ 'foo', 'bar', 'baz' ],
  x: 3,
  y: 4,
  n: 5,
  a: true,
  b: true,
  c: true,
  beep: 'boop' }
```

# methods

``` js
var parseArgs = require('minimist')
```

## var argv = parseArgs(args, opts={})

Return an argument object `argv` populated with the array arguments from `args`.

`argv._` contains all the arguments that didn't have an option associated with
them.

Numeric-looking arguments will be returned as numbers unless `opts.string` or
`opts.boolean` is set for that argument name.

Any arguments after `'--'` will not be parsed and will end up in `argv._`.

options can be:

* `opts.string` - a string or array of strings argument names to always treat as
strings
* `opts.boolean` - a boolean, string or array of strings to always treat as
booleans. if `true` will treat all double hyphenated arguments without equal signs
as boolean (e.g. affects `--foo`, not `-f` or `--foo=bar`)
* `opts.alias` - an object mapping string names to strings or arrays of string
argument names to use as aliases
* `opts.default` - an object mapping string argument names to default values
* `opts.stopEarly` - when true, populate `argv._` with everything after the
first non-option
* `opts['--']` - when true, populate `argv._` with everything before the `--`
and `argv['--']` with everything after the `--`. Here's an example:
* `opts.unknown` - a function which is invoked with a command line parameter not
defined in the `opts` configuration object. If the function returns `false`, the
unknown option is not added to `argv`.

```
> require('./')('one two three -- four five --six'.split(' '), { '--': true })
{ _: [ 'one', 'two', 'three' ],
  '--': [ 'four', 'five', '--six' ] }
```

Note that with `opts['--']` set, parsing for arguments still stops after the
`--`.

# install

With [npm](https://npmjs.org) do:

```
npm install minimist
```

# license

MIT
# minimist

parse argument options

This module is the guts of optimist's argument parser without all the
fanciful decoration.

[![browser support](https://ci.testling.com/substack/minimist.png)](http://ci.testling.com/substack/minimist)

[![build status](https://secure.travis-ci.org/substack/minimist.png)](http://travis-ci.org/substack/minimist)

# example

``` js
var argv = require('minimist')(process.argv.slice(2));
console.dir(argv);
```

```
$ node example/parse.js -a beep -b boop
{ _: [], a: 'beep', b: 'boop' }
```

```
$ node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
{ _: [ 'foo', 'bar', 'baz' ],
  x: 3,
  y: 4,
  n: 5,
  a: true,
  b: true,
  c: true,
  beep: 'boop' }
```

# methods

``` js
var parseArgs = require('minimist')
```

## var argv = parseArgs(args, opts={})

Return an argument object `argv` populated with the array arguments from `args`.

`argv._` contains all the arguments that didn't have an option associated with
them.

Numeric-looking arguments will be returned as numbers unless `opts.string` or
`opts.boolean` is set for that argument name.

Any arguments after `'--'` will not be parsed and will end up in `argv._`.

options can be:

* `opts.string` - a string or array of strings argument names to always treat as
strings
* `opts.boolean` - a string or array of strings to always treat as booleans
* `opts.alias` - an object mapping string names to strings or arrays of string
argument names to use as aliases
* `opts.default` - an object mapping string argument names to default values

# install

With [npm](https://npmjs.org) do:

```
npm install minimist
```

# license

MIT
# mkdirp

Like `mkdir -p`, but in node.js!

[![build status](https://secure.travis-ci.org/substack/node-mkdirp.png)](http://travis-ci.org/substack/node-mkdirp)

# example

## pow.js

```js
var mkdirp = require('mkdirp');
    
mkdirp('/tmp/foo/bar/baz', function (err) {
    if (err) console.error(err)
    else console.log('pow!')
});
```

Output

```
pow!
```

And now /tmp/foo/bar/baz exists, huzzah!

# methods

```js
var mkdirp = require('mkdirp');
```

## mkdirp(dir, opts, cb)

Create a new directory and any necessary subdirectories at `dir` with octal
permission string `opts.mode`. If `opts` is a non-object, it will be treated as
the `opts.mode`.

If `opts.mode` isn't specified, it defaults to `0777 & (~process.umask())`.

`cb(err, made)` fires with the error or the first directory `made`
that had to be created, if any.

You can optionally pass in an alternate `fs` implementation by passing in
`opts.fs`. Your implementation should have `opts.fs.mkdir(path, mode, cb)` and
`opts.fs.stat(path, cb)`.

## mkdirp.sync(dir, opts)

Synchronously create a new directory and any necessary subdirectories at `dir`
with octal permission string `opts.mode`. If `opts` is a non-object, it will be
treated as the `opts.mode`.

If `opts.mode` isn't specified, it defaults to `0777 & (~process.umask())`.

Returns the first directory that had to be created, if any.

You can optionally pass in an alternate `fs` implementation by passing in
`opts.fs`. Your implementation should have `opts.fs.mkdirSync(path, mode)` and
`opts.fs.statSync(path)`.

# usage

This package also ships with a `mkdirp` command.

```
usage: mkdirp [DIR1,DIR2..] {OPTIONS}

  Create each supplied directory including any necessary parent directories that
  don't yet exist.
  
  If the directory already exists, do nothing.

OPTIONS are:

  -m, --mode   If a directory needs to be created, set the mode as an octal
               permission string.

```

# install

With [npm](http://npmjs.org) do:

```
npm install mkdirp
```

to get the library, or

```
npm install -g mkdirp
```

to get the command.

# license

MIT
# mkdirp

Like `mkdir -p`, but in node.js!

[![build status](https://secure.travis-ci.org/substack/node-mkdirp.png)](http://travis-ci.org/substack/node-mkdirp)

# example

## pow.js

```js
var mkdirp = require('mkdirp');
    
mkdirp('/tmp/foo/bar/baz', function (err) {
    if (err) console.error(err)
    else console.log('pow!')
});
```

Output

```
pow!
```

And now /tmp/foo/bar/baz exists, huzzah!

# methods

```js
var mkdirp = require('mkdirp');
```

## mkdirp(dir, opts, cb)

Create a new directory and any necessary subdirectories at `dir` with octal
permission string `opts.mode`. If `opts` is a non-object, it will be treated as
the `opts.mode`.

If `opts.mode` isn't specified, it defaults to `0777 & (~process.umask())`.

`cb(err, made)` fires with the error or the first directory `made`
that had to be created, if any.

You can optionally pass in an alternate `fs` implementation by passing in
`opts.fs`. Your implementation should have `opts.fs.mkdir(path, mode, cb)` and
`opts.fs.stat(path, cb)`.

## mkdirp.sync(dir, opts)

Synchronously create a new directory and any necessary subdirectories at `dir`
with octal permission string `opts.mode`. If `opts` is a non-object, it will be
treated as the `opts.mode`.

If `opts.mode` isn't specified, it defaults to `0777 & (~process.umask())`.

Returns the first directory that had to be created, if any.

You can optionally pass in an alternate `fs` implementation by passing in
`opts.fs`. Your implementation should have `opts.fs.mkdirSync(path, mode)` and
`opts.fs.statSync(path)`.

# usage

This package also ships with a `mkdirp` command.

```
usage: mkdirp [DIR1,DIR2..] {OPTIONS}

  Create each supplied directory including any necessary parent directories that
  don't yet exist.
  
  If the directory already exists, do nothing.

OPTIONS are:

  -m, --mode   If a directory needs to be created, set the mode as an octal
               permission string.

```

# install

With [npm](http://npmjs.org) do:

```
npm install mkdirp
```

to get the library, or

```
npm install -g mkdirp
```

to get the command.

# license

MIT
# Form-Data [![NPM Module](https://img.shields.io/npm/v/form-data.svg)](https://www.npmjs.com/package/form-data) [![Join the chat at https://gitter.im/form-data/form-data](http://form-data.github.io/images/gitterbadge.svg)](https://gitter.im/form-data/form-data)

A library to create readable ```"multipart/form-data"``` streams. Can be used to submit forms and file uploads to other web applications.

The API of this library is inspired by the [XMLHttpRequest-2 FormData Interface][xhr2-fd].

[xhr2-fd]: http://dev.w3.org/2006/webapi/XMLHttpRequest-2/Overview.html#the-formdata-interface

[![Linux Build](https://img.shields.io/travis/form-data/form-data/master.svg?label=linux:4.x-9.x)](https://travis-ci.org/form-data/form-data)
[![MacOS Build](https://img.shields.io/travis/form-data/form-data/master.svg?label=macos:4.x-9.x)](https://travis-ci.org/form-data/form-data)
[![Windows Build](https://img.shields.io/appveyor/ci/alexindigo/form-data/master.svg?label=windows:4.x-9.x)](https://ci.appveyor.com/project/alexindigo/form-data)

[![Coverage Status](https://img.shields.io/coveralls/form-data/form-data/master.svg?label=code+coverage)](https://coveralls.io/github/form-data/form-data?branch=master)
[![Dependency Status](https://img.shields.io/david/form-data/form-data.svg)](https://david-dm.org/form-data/form-data)
[![bitHound Overall Score](https://www.bithound.io/github/form-data/form-data/badges/score.svg)](https://www.bithound.io/github/form-data/form-data)

## Install

```
npm install --save form-data
```

## Usage

In this example we are constructing a form with 3 fields that contain a string,
a buffer and a file stream.

``` javascript
var FormData = require('form-data');
var fs = require('fs');

var form = new FormData();
form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_file', fs.createReadStream('/foo/bar.jpg'));
```

Also you can use http-response stream:

``` javascript
var FormData = require('form-data');
var http = require('http');

var form = new FormData();

http.request('http://nodejs.org/images/logo.png', function(response) {
  form.append('my_field', 'my value');
  form.append('my_buffer', new Buffer(10));
  form.append('my_logo', response);
});
```

Or @mikeal's [request](https://github.com/request/request) stream:

``` javascript
var FormData = require('form-data');
var request = require('request');

var form = new FormData();

form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_logo', request('http://nodejs.org/images/logo.png'));
```

In order to submit this form to a web application, call ```submit(url, [callback])``` method:

``` javascript
form.submit('http://example.org/', function(err, res) {
  // res – response object (http.IncomingMessage)  //
  res.resume();
});

```

For more advanced request manipulations ```submit()``` method returns ```http.ClientRequest``` object, or you can choose from one of the alternative submission methods.

### Custom options

You can provide custom options, such as `maxDataSize`:

``` javascript
var FormData = require('form-data');

var form = new FormData({ maxDataSize: 20971520 });
form.append('my_field', 'my value');
form.append('my_buffer', /* something big */);
```

List of available options could be found in [combined-stream](https://github.com/felixge/node-combined-stream/blob/master/lib/combined_stream.js#L7-L15)

### Alternative submission methods

You can use node's http client interface:

``` javascript
var http = require('http');

var request = http.request({
  method: 'post',
  host: 'example.org',
  path: '/upload',
  headers: form.getHeaders()
});

form.pipe(request);

request.on('response', function(res) {
  console.log(res.statusCode);
});
```

Or if you would prefer the `'Content-Length'` header to be set for you:

``` javascript
form.submit('example.org/upload', function(err, res) {
  console.log(res.statusCode);
});
```

To use custom headers and pre-known length in parts:

``` javascript
var CRLF = '\r\n';
var form = new FormData();

var options = {
  header: CRLF + '--' + form.getBoundary() + CRLF + 'X-Custom-Header: 123' + CRLF + CRLF,
  knownLength: 1
};

form.append('my_buffer', buffer, options);

form.submit('http://example.com/', function(err, res) {
  if (err) throw err;
  console.log('Done');
});
```

Form-Data can recognize and fetch all the required information from common types of streams (```fs.readStream```, ```http.response``` and ```mikeal's request```), for some other types of streams you'd need to provide "file"-related information manually:

``` javascript
someModule.stream(function(err, stdout, stderr) {
  if (err) throw err;

  var form = new FormData();

  form.append('file', stdout, {
    filename: 'unicycle.jpg', // ... or:
    filepath: 'photos/toys/unicycle.jpg',
    contentType: 'image/jpeg',
    knownLength: 19806
  });

  form.submit('http://example.com/', function(err, res) {
    if (err) throw err;
    console.log('Done');
  });
});
```

The `filepath` property overrides `filename` and may contain a relative path. This is typically used when uploading [multiple files from a directory](https://wicg.github.io/entries-api/#dom-htmlinputelement-webkitdirectory).

For edge cases, like POST request to URL with query string or to pass HTTP auth credentials, object can be passed to `form.submit()` as first parameter:

``` javascript
form.submit({
  host: 'example.com',
  path: '/probably.php?extra=params',
  auth: 'username:password'
}, function(err, res) {
  console.log(res.statusCode);
});
```

In case you need to also send custom HTTP headers with the POST request, you can use the `headers` key in first parameter of `form.submit()`:

``` javascript
form.submit({
  host: 'example.com',
  path: '/surelynot.php',
  headers: {'x-test-header': 'test-header-value'}
}, function(err, res) {
  console.log(res.statusCode);
});
```

### Integration with other libraries

#### Request

Form submission using  [request](https://github.com/request/request):

```javascript
var formData = {
  my_field: 'my_value',
  my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
};

request.post({url:'http://service.com/upload', formData: formData}, function(err, httpResponse, body) {
  if (err) {
    return console.error('upload failed:', err);
  }
  console.log('Upload successful!  Server responded with:', body);
});
```

For more details see [request readme](https://github.com/request/request#multipartform-data-multipart-form-uploads).

#### node-fetch

You can also submit a form using [node-fetch](https://github.com/bitinn/node-fetch):

```javascript
var form = new FormData();

form.append('a', 1);

fetch('http://example.com', { method: 'POST', body: form })
    .then(function(res) {
        return res.json();
    }).then(function(json) {
        console.log(json);
    });
```

## Notes

- ```getLengthSync()``` method DOESN'T calculate length for streams, use ```knownLength``` options as workaround.
- Starting version `2.x` FormData has dropped support for `node@0.10.x`.

## License

Form-Data is released under the [MIT](License) license.
concat-map
==========

Concatenative mapdashery.

[![browser support](http://ci.testling.com/substack/node-concat-map.png)](http://ci.testling.com/substack/node-concat-map)

[![build status](https://secure.travis-ci.org/substack/node-concat-map.png)](http://travis-ci.org/substack/node-concat-map)

example
=======

``` js
var concatMap = require('concat-map');
var xs = [ 1, 2, 3, 4, 5, 6 ];
var ys = concatMap(xs, function (x) {
    return x % 2 ? [ x - 0.1, x, x + 0.1 ] : [];
});
console.dir(ys);
```

***

```
[ 0.9, 1, 1.1, 2.9, 3, 3.1, 4.9, 5, 5.1 ]
```

methods
=======

``` js
var concatMap = require('concat-map')
```

concatMap(xs, fn)
-----------------

Return an array of concatenated elements by calling `fn(x, i)` for each element
`x` and each index `i` in the array `xs`.

When `fn(x, i)` returns an array, its result will be concatenated with the
result array. If `fn(x, i)` returns anything else, that value will be pushed
onto the end of the result array.

install
=======

With [npm](http://npmjs.org) do:

```
npm install concat-map
```

license
=======

MIT

notes
=====

This module was written while sitting high above the ground in a tree.
concat-map
==========

Concatenative mapdashery.

[![browser support](http://ci.testling.com/substack/node-concat-map.png)](http://ci.testling.com/substack/node-concat-map)

[![build status](https://secure.travis-ci.org/substack/node-concat-map.png)](http://travis-ci.org/substack/node-concat-map)

example
=======

``` js
var concatMap = require('concat-map');
var xs = [ 1, 2, 3, 4, 5, 6 ];
var ys = concatMap(xs, function (x) {
    return x % 2 ? [ x - 0.1, x, x + 0.1 ] : [];
});
console.dir(ys);
```

***

```
[ 0.9, 1, 1.1, 2.9, 3, 3.1, 4.9, 5, 5.1 ]
```

methods
=======

``` js
var concatMap = require('concat-map')
```

concatMap(xs, fn)
-----------------

Return an array of concatenated elements by calling `fn(x, i)` for each element
`x` and each index `i` in the array `xs`.

When `fn(x, i)` returns an array, its result will be concatenated with the
result array. If `fn(x, i)` returns anything else, that value will be pushed
onto the end of the result array.

install
=======

With [npm](http://npmjs.org) do:

```
npm install concat-map
```

license
=======

MIT

notes
=====

This module was written while sitting high above the ground in a tree.
hat
===

Generate random IDs and avoid collisions.

![hat](http://substack.net/images/hat.png)

examples
========

hat
---

````javascript
var hat = require('hat');

var id = hat();
console.log(id);
````

output:

````
0c82a54f22f775a3ed8b97b2dea74036
````

rack
----

````javascript
var hat = require('hat');
var rack = hat.rack();

console.log(rack());
console.log(rack());
````

output:

````
1c24171393dc5de04ffcb21f1182ab28
fabe2323acc1b559dee43d4a1e16cbeb
````

methods
=======

var hat = require('hat');

hat(bits=128, base=16)
----------------------

Generate a random ID string with `bits` of data in a `base`.

Leading zeros are appended such that all outputs for a given number of bits have
equal length.

var rack = hat.rack(bits=128, base=16, expandBy)
------------------------------------------------

Make a new hat rack. Call `rack()` repeatedly to generate new IDs which are
checked for collisions.

If `expandBy` is specified, increment `bits` by this amount if too many
collisions occur. If `expandBy` isn't specified, `rack()` will throw if too many
collisions occur during generation.

Optionally call `var id = rack(data)` to store `data` at the new ID.

You can get the data out again with `rack.get(id)` and set the data with
`rack.set(id, value)`.
# require-directory

Recursively iterates over specified directory, `require()`'ing each file, and returning a nested hash structure containing those modules.

**[Follow me (@troygoode) on Twitter!](https://twitter.com/intent/user?screen_name=troygoode)**

[![NPM](https://nodei.co/npm/require-directory.png?downloads=true&stars=true)](https://nodei.co/npm/require-directory/)

[![build status](https://secure.travis-ci.org/troygoode/node-require-directory.png)](http://travis-ci.org/troygoode/node-require-directory)

## How To Use

### Installation (via [npm](https://npmjs.org/package/require-directory))

```bash
$ npm install require-directory
```

### Usage

A common pattern in node.js is to include an index file which creates a hash of the files in its current directory. Given a directory structure like so:

* app.js
* routes/
  * index.js
  * home.js
  * auth/
    * login.js
    * logout.js
    * register.js

`routes/index.js` uses `require-directory` to build the hash (rather than doing so manually) like so:

```javascript
var requireDirectory = require('require-directory');
module.exports = requireDirectory(module);
```

`app.js` references `routes/index.js` like any other module, but it now has a hash/tree of the exports from the `./routes/` directory:

```javascript
var routes = require('./routes');

// snip

app.get('/', routes.home);
app.get('/register', routes.auth.register);
app.get('/login', routes.auth.login);
app.get('/logout', routes.auth.logout);
```

The `routes` variable above is the equivalent of this:

```javascript
var routes = {
  home: require('routes/home.js'),
  auth: {
    login: require('routes/auth/login.js'),
    logout: require('routes/auth/logout.js'),
    register: require('routes/auth/register.js')
  }
};
```

*Note that `routes.index` will be `undefined` as you would hope.*

### Specifying Another Directory

You can specify which directory you want to build a tree of (if it isn't the current directory for whatever reason) by passing it as the second parameter. Not specifying the path (`requireDirectory(module)`) is the equivelant of `requireDirectory(module, __dirname)`:

```javascript
var requireDirectory = require('require-directory');
module.exports = requireDirectory(module, './some/subdirectory');
```

For example, in the [example in the Usage section](#usage) we could have avoided creating `routes/index.js` and instead changed the first lines of `app.js` to:

```javascript
var requireDirectory = require('require-directory');
var routes = requireDirectory(module, './routes');
```

## Options

You can pass an options hash to `require-directory` as the 2nd parameter (or 3rd if you're passing the path to another directory as the 2nd parameter already). Here are the available options:

### Whitelisting

Whitelisting (either via RegExp or function) allows you to specify that only certain files be loaded.

```javascript
var requireDirectory = require('require-directory'),
  whitelist = /onlyinclude.js$/,
  hash = requireDirectory(module, {include: whitelist});
```

```javascript
var requireDirectory = require('require-directory'),
  check = function(path){
    if(/onlyinclude.js$/.test(path)){
      return true; // don't include
    }else{
      return false; // go ahead and include
    }
  },
  hash = requireDirectory(module, {include: check});
```

### Blacklisting

Blacklisting (either via RegExp or function) allows you to specify that all but certain files should be loaded.

```javascript
var requireDirectory = require('require-directory'),
  blacklist = /dontinclude\.js$/,
  hash = requireDirectory(module, {exclude: blacklist});
```

```javascript
var requireDirectory = require('require-directory'),
  check = function(path){
    if(/dontinclude\.js$/.test(path)){
      return false; // don't include
    }else{
      return true; // go ahead and include
    }
  },
  hash = requireDirectory(module, {exclude: check});
```

### Visiting Objects As They're Loaded

`require-directory` takes a function as the `visit` option that will be called for each module that is added to module.exports.

```javascript
var requireDirectory = require('require-directory'),
  visitor = function(obj) {
    console.log(obj); // will be called for every module that is loaded
  },
  hash = requireDirectory(module, {visit: visitor});
```

The visitor can also transform the objects by returning a value:

```javascript
var requireDirectory = require('require-directory'),
  visitor = function(obj) {
    return obj(new Date());
  },
  hash = requireDirectory(module, {visit: visitor});
```

### Renaming Keys

```javascript
var requireDirectory = require('require-directory'),
  renamer = function(name) {
    return name.toUpperCase();
  },
  hash = requireDirectory(module, {rename: renamer});
```

### No Recursion

```javascript
var requireDirectory = require('require-directory'),
  hash = requireDirectory(module, {recurse: false});
```

## Run Unit Tests

```bash
$ npm run lint
$ npm test
```

## License

[MIT License](http://www.opensource.org/licenses/mit-license.php)

## Author

[Troy Goode](https://github.com/TroyGoode) ([troygoode@gmail.com](mailto:troygoode@gmail.com))

