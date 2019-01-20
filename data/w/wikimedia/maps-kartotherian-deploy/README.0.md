#through

[![build status](https://secure.travis-ci.org/dominictarr/through.png)](http://travis-ci.org/dominictarr/through)
[![testling badge](https://ci.testling.com/dominictarr/through.png)](https://ci.testling.com/dominictarr/through)

Easy way to create a `Stream` that is both `readable` and `writable`. 

* Pass in optional `write` and `end` methods.
* `through` takes care of pause/resume logic if you use `this.queue(data)` instead of `this.emit('data', data)`.
* Use `this.pause()` and `this.resume()` to manage flow.
* Check `this.paused` to see current flow state. (`write` always returns `!this.paused`).

This function is the basis for most of the synchronous streams in 
[event-stream](http://github.com/dominictarr/event-stream).

``` js
var through = require('through')

through(function write(data) {
    this.queue(data) //data *must* not be null
  },
  function end () { //optional
    this.queue(null)
  })
```

Or, can also be used _without_ buffering on pause, use `this.emit('data', data)`,
and this.emit('end')

``` js
var through = require('through')

through(function write(data) {
    this.emit('data', data)
    //this.pause() 
  },
  function end () { //optional
    this.emit('end')
  })
```

## Extended Options

You will probably not need these 99% of the time.

### autoDestroy=false

By default, `through` emits close when the writable
and readable side of the stream has ended.
If that is not desired, set `autoDestroy=false`.

``` js
var through = require('through')

//like this
var ts = through(write, end, {autoDestroy: false})
//or like this
var ts = through(write, end)
ts.autoDestroy = false
```

## License

MIT / Apache2
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
# shell-quote

Parse and quote shell commands.

[![build status](https://secure.travis-ci.org/substack/node-shell-quote.png)](http://travis-ci.org/substack/node-shell-quote)

[![browser support](https://ci.testling.com/substack/node-shell-quote.png)](https://ci.testling.com/substack/node-shell-quote)

# example

## quote

``` js
var quote = require('shell-quote').quote;
var s = quote([ 'a', 'b c d', '$f', '"g"' ]);
console.log(s);
```

output

```
a 'b c d' \$f '"g"'
```

## parse

``` js
var parse = require('shell-quote').parse;
var xs = parse('a "b c" \\$def \'it\\\'s great\'');
console.dir(xs);
```

output

```
[ 'a', 'b c', '\\$def', 'it\'s great' ]
```

## parse with an environment variable

``` js
var parse = require('shell-quote').parse;
var xs = parse('beep --boop="$PWD"', { PWD: '/home/robot' });
console.dir(xs);
```

output

```
[ 'beep', '--boop=/home/robot' ]
```

## parse with custom escape charcter

``` js
var parse = require('shell-quote').parse;
var xs = parse('beep --boop="$PWD"', { PWD: '/home/robot' }, { escape: '^' });
console.dir(xs);
```

output

```
[ 'beep', '--boop=/home/robot' ]
```

## parsing shell operators

``` js
var parse = require('shell-quote').parse;
var xs = parse('beep || boop > /byte');
console.dir(xs);
```

output:

```
[ 'beep', { op: '||' }, 'boop', { op: '>' }, '/byte' ]
```

## parsing shell comment

``` js
var parse = require('shell-quote').parse;
var xs = parse('beep > boop # > kaboom');
console.dir(xs);
```

output:

```
[ 'beep', { op: '>' }, 'boop', { comment: '> kaboom' } ]
```

# methods

``` js
var quote = require('shell-quote').quote;
var parse = require('shell-quote').parse;
```

## quote(args)

Return a quoted string for the array `args` suitable for using in shell
commands.

## parse(cmd, env={})

Return an array of arguments from the quoted string `cmd`.

Interpolate embedded bash-style `$VARNAME` and `${VARNAME}` variables with
the `env` object which like bash will replace undefined variables with `""`.

`env` is usually an object but it can also be a function to perform lookups.
When `env(key)` returns a string, its result will be output just like `env[key]`
would. When `env(key)` returns an object, it will be inserted into the result
array like the operator objects.

When a bash operator is encountered, the element in the array with be an object
with an `"op"` key set to the operator string. For example:

```
'beep || boop > /byte'
```

parses as:

```
[ 'beep', { op: '||' }, 'boop', { op: '>' }, '/byte' ]
```

# install

With [npm](http://npmjs.org) do:

```
npm install shell-quote
```

# license

MIT
# vm-browserify

emulate node's vm module for the browser

[![Build Status](https://travis-ci.org/browserify/vm-browserify.svg?branch=master)](https://travis-ci.org/browserify/vm-browserify)

# example

Just write some client-side javascript:

``` js
var vm = require('vm');

$(function () {
    var res = vm.runInNewContext('a + 5', { a : 100 });
    $('#res').text(res);
});
```

compile it with [browserify](http://github.com/substack/node-browserify):

```
browserify entry.js -o bundle.js
```

then whip up some html:

``` html
<html>
  <head>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script src="/bundle.js"></script>
  </head>
  <body>
    result = <span id="res"></span>
  </body>
</html>
```

and when you load the page you should see:

```
result = 105
```

# methods

## vm.runInNewContext(code, context={})

Evaluate some `code` in a new iframe with a `context`.

Contexts are like wrapping your code in a `with()` except slightly less terrible
because the code is sandboxed into a new iframe.

# install

This module is depended upon by browserify, so you should just be able to
`require('vm')` and it will just work. However if you want to use this module
directly you can install it with [npm](http://npmjs.org):

```
npm install vm-browserify
```

# license

MIT
# path-browserify

the path module from node core for browsers
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
# read-only-stream

wrap a readable/writable stream to be read-only
to prevent mucking up the input side

[![build status](https://secure.travis-ci.org/substack/read-only-stream.png)](http://travis-ci.org/substack/read-only-stream)

# example

Suppose you have a module that uses a readable/writable stream internally but
want to expose just the readable part of that internal stream. This is common if
you use the writable side internally and expose the readable side as the
interface.

Now we can write some code like this with a `through` stream internally for
convenience:

``` js
var through = require('through2');
var readonly = require('read-only-stream');

module.exports = function () {
    var stream = through();
    stream.end('wooooo\n');
    return readonly(stream);
};
```

but consumers won't be able to write to the input side and break the api:

``` js
var wrap = require('./wrap.js');
var ro = wrap(); // can't write to `ro` and muck up internal state
ro.pipe(process.stdout);
```

# methods

``` js
var readonly = require('read-only-stream')
```

## var ro = readonly(stream)

Return a readable stream `ro` that wraps the readable/writable `stream` argument
given to only expose the readable side.

`stream` can be a streams1 or streams2 stream.

# install

With [npm](https://npmjs.org) do:

```
npm install read-only-stream
```

# license

MIT
# https-browserify

https module compatability for browserify

# example

``` js
var https = require('https-browserify')
var r = https.request('https://github.com')
r.on('request', function (res) {
  console.log(res)
})
```

# methods

The API is the same as the client portion of the
[node core https module](http://nodejs.org/docs/latest/api/https.html).

# license

MIT
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
# browser-pack

pack node-style source files from a json stream into a browser bundle

[![build status](https://secure.travis-ci.org/browserify/browser-pack.png)](http://travis-ci.org/browserify/browser-pack)

# example

json input:

``` json
[
  {
    "id": "a1b5af78",
    "source": "console.log(require('./foo')(5))",
    "deps": { "./foo": "b8f69fa5" },
    "entry": true
  },
  {
    "id": "b8f69fa5",
    "source": "module.exports = function (n) { return n * 111 }",
    "deps": {}
  }
]
```

bundle script:

``` js
var pack = require('browser-pack')();
process.stdin.pipe(pack).pipe(process.stdout);
process.stdin.resume();
```

output:

```
$ browser-pack < input.json
(function(p,c,e){function r(n){if(!c[n]){c[n]={exports:{}};p[n][0](function(x){return r(p[n][1][x])},c[n],c[n].exports);}return c[n].exports}for(var i=0;i<e.length;i++)r(e[i]);return r})({"a1b5af78":[function(require,module,exports){console.log(require('./foo')(5))},{"./foo":"b8f69fa5"}],"b8f69fa5":[function(require,module,exports){module.exports = function (n) { return n * 111 }},{}]},{},["a1b5af78","b8f69fa5"])
```

# methods

``` js
var pack = require('browser-pack');
```

## pack(opts)

Return a through stream that takes a stream of json input and produces a stream
of javascript output. This module does not export its internal `require()`
function but you can prepend `'var require='` to the stream contents to get the
require function. `require()` will return `undefined` when a module hasn't been
defined to support splitting up modules across several bundles with custom
fallback logic.

If `opts.raw` is given, the writable end of the stream will expect objects to be
written to it instead of expecting a stream of json text it will need to parse.

If `opts.sourceMapPrefix` is given and source maps are computed, the
`opts.sourceMapPrefix` string will be used instead of `//#`.

If `opts.sourceRoot` is given and source maps are computed, the root for the
output source map will be defined. (default is no root)

Additionally, rows with a truthy `entry` may have an `order` field that
determines the numeric index to execute the entries in.

You can specify a custom prelude with `opts.prelude` but you should really know
what you're doing first. See the `prelude.js` file in this repo for the default
prelude. If you specify a custom prelude, you must also specify a valid
`opts.preludePath` to the prelude source file for sourcemaps to work.

`opts.standalone` external string name to use for umd

`opts.standaloneModule` sets the internal module name to export for standalone

`opts.hasExports` whether the bundle should include `require=` (or the
`opts.externalRequireName`) so that `require()` is available outside the bundle

# install

With [npm](https://npmjs.org), to get the library do:

```
npm install browser-pack
```

and to get the command-line tool do:

```
npm install -g browser-pack
```

# license

MIT
# resolve

implements the [node `require.resolve()`
algorithm](http://nodejs.org/docs/v0.4.8/api/all.html#all_Together...)
such that you can `require.resolve()` on behalf of a file asynchronously and
synchronously

[![build status](https://secure.travis-ci.org/substack/node-resolve.png)](http://travis-ci.org/substack/node-resolve)

# example

asynchronously resolve:

``` js
var resolve = require('resolve');
resolve('tap', { basedir: __dirname }, function (err, res) {
    if (err) console.error(err)
    else console.log(res)
});
```

```
$ node example/async.js
/home/substack/projects/node-resolve/node_modules/tap/lib/main.js
```

synchronously resolve:

``` js
var resolve = require('resolve');
var res = resolve.sync('tap', { basedir: __dirname });
console.log(res);
```

```
$ node example/sync.js
/home/substack/projects/node-resolve/node_modules/tap/lib/main.js
```

# methods

``` js
var resolve = require('resolve')
```

## resolve(id, opts={}, cb)

Asynchronously resolve the module path string `id` into `cb(err, res [, pkg])`, where `pkg` (if defined) is the data from `package.json`.

options are:

* opts.basedir - directory to begin resolving from

* opts.package - `package.json` data applicable to the module being loaded

* opts.extensions - array of file extensions to search in order

* opts.readFile - how to read files asynchronously

* opts.isFile - function to asynchronously test whether a file exists

* opts.packageFilter - transform the parsed package.json contents before looking
at the "main" field

* opts.pathFilter(pkg, path, relativePath) - transform a path within a package
  * pkg - package data
  * path - the path being resolved
  * relativePath - the path relative from the package.json location
  * returns - a relative path that will be joined from the package.json location

* opts.paths - require.paths array to use if nothing is found on the normal
node_modules recursive walk (probably don't use this)

* opts.moduleDirectory - directory (or directories) in which to recursively look for modules. default: `"node_modules"`

default `opts` values:

``` javascript
{
    paths: [],
    basedir: __dirname,
    extensions: [ '.js' ],
    readFile: fs.readFile,
    isFile: function (file, cb) {
        fs.stat(file, function (err, stat) {
            if (err && err.code === 'ENOENT') cb(null, false)
            else if (err) cb(err)
            else cb(null, stat.isFile())
        });
    },
    moduleDirectory: 'node_modules'
}
```

## resolve.sync(id, opts)

Synchronously resolve the module path string `id`, returning the result and
throwing an error when `id` can't be resolved.

options are:

* opts.basedir - directory to begin resolving from

* opts.extensions - array of file extensions to search in order

* opts.readFile - how to read files synchronously

* opts.isFile - function to synchronously test whether a file exists

* `opts.packageFilter(pkg, pkgfile)` - transform the parsed package.json
* contents before looking at the "main" field

* opts.paths - require.paths array to use if nothing is found on the normal
node_modules recursive walk (probably don't use this)

* opts.moduleDirectory - directory (or directories) in which to recursively look for modules. default: `"node_modules"`

default `opts` values:

``` javascript
{
    paths: [],
    basedir: __dirname,
    extensions: [ '.js' ],
    readFileSync: fs.readFileSync,
    isFile: function (file) {
        try { return fs.statSync(file).isFile() }
        catch (e) { return false }
    },
    moduleDirectory: 'node_modules'
}
````

## resolve.isCore(pkg)

Return whether a package is in core.

# install

With [npm](https://npmjs.org) do:

```
npm install resolve
```

# license

MIT
# detective

find all calls to `require()` by walking the AST

[![build status](https://secure.travis-ci.org/browserify/detective.png)](http://travis-ci.org/browserify/detective)

# example

## strings

strings_src.js:

``` js
var a = require('a');
var b = require('b');
var c = require('c');
```

strings.js:

``` js
var detective = require('detective');
var fs = require('fs');

var src = fs.readFileSync(__dirname + '/strings_src.js');
var requires = detective(src);
console.dir(requires);
```

output:

```
$ node examples/strings.js
[ 'a', 'b', 'c' ]
```

# methods

``` js
var detective = require('detective');
```

## detective(src, opts)

Give some source body `src`, return an array of all the `require()` calls with
string arguments.

The options parameter `opts` is passed along to `detective.find()`.

## var found = detective.find(src, opts)

Give some source body `src`, return `found` with:

* `found.strings` - an array of each string found in a `require()`
* `found.expressions` - an array of each stringified expression found in a
`require()` call
* `found.nodes` (when `opts.nodes === true`) - an array of AST nodes for each
argument found in a `require()` call

Optionally:

* `opts.word` - specify a different function name instead of `"require"`
* `opts.nodes` - when `true`, populate `found.nodes`
* `opts.isRequire(node)` - a function returning whether an AST `CallExpression`
node is a require call
* `opts.parse` - supply options directly to
[acorn](https://npmjs.org/package/acorn) with some support for esprima-style
options `range` and `loc`
* `opts.ecmaVersion` - default: 9

# install

With [npm](https://npmjs.org) do:

```
npm install detective
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
# subarg

parse arguments with recursive contexts using
[minimist](https://npmjs.org/package/minimist)

[![testling badge](https://ci.testling.com/substack/subarg.png)](https://ci.testling.com/substack/subarg)

[![build status](https://secure.travis-ci.org/substack/subarg.png)](http://travis-ci.org/substack/subarg)

This module is useful if you need to pass arguments into a piece of code without
coordinating ahead of time with the main program, like with a plugin system.

# example

``` js
var subarg = require('subarg');
var argv = subarg(process.argv.slice(2));
console.log(argv);
```

Contexts are denoted with square brackets:

```
$ node example/show.js rawr --beep [ boop -a 3 ] -n4 --robots [ -x 8 -y 6 ]
{ _: [ 'rawr' ],
  beep: { _: [ 'boop' ], a: 3 },
  n: 4,
  robots: { _: [], x: 8, y: 6 } }
```

# methods

``` js
var subarg = require('subarg')
```

## var argv = subarg(args, opts)

Parse the arguments array `args`, passing `opts` to
[minimist](https://npmjs.org/package/minimist).

An opening `[` in the `args` array creates a new context and a `]` closes a
context. Contexts may be nested.

# install

With [npm](https://npmjs.org) do:

```
npm install subarg
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
# insert-module-globals

insert implicit module globals
(`__filename`, `__dirname`, `process`, `global`, `setImmediate`, `clearImmediate` and `Buffer`)
as a browserify-style transform

[![build status](https://secure.travis-ci.org/browserify/insert-module-globals.png)](http://travis-ci.org/browserify/insert-module-globals)

# example

``` js
var mdeps = require('module-deps');
var bpack = require('browser-pack');
var insert = require('insert-module-globals');
function inserter (file) {
    return insert(file, { basedir: __dirname + '/files' });
}

var files = [ __dirname + '/files/main.js' ];
mdeps(files, { transform: inserter })
    .pipe(bpack({ raw: true }))
    .pipe(process.stdout)
;
```

```
$ node example/insert.js | node
in main.js: {"__filename":"/main.js","__dirname":"/"}
in foo/index.js: {"__filename":"/foo/index.js","__dirname":"/foo"}
```

or use the command-line scripts:

```
$ module-deps main.js | insert-module-globals | browser-pack | node
in main.js: {"__filename":"/main.js","__dirname":"/"}
in foo/index.js: {"__filename":"/foo/index.js","__dirname":"/foo"}
```

or use insert-module-globals as a transform:

```
$ module-deps main.js --transform insert-module-globals | browser-pack | node
in main.js: {"__filename":"/main.js","__dirname":"/"}
in foo/index.js: {"__filename":"/foo/index.js","__dirname":"/foo"}
```

# methods

``` js
var insertGlobals = require('insert-module-globals')
```

## var inserter = insertGlobals(file, opts)

Return a transform stream `inserter` for the filename `file` that will accept a
javascript file as input and will output the file with a closure around the
contents as necessary to define extra builtins.

When `opts.always` is true, wrap every file with all the global variables
without parsing. This is handy because parsing the scope can take a long time,
so you can prioritize fast builds over saving bytes in the final output. When
`opts.always` is truthy but not true, avoid parsing but perform a quick test to
determine if wrapping should be skipped.

Use `opts.vars` to override the default inserted variables, or set
`opts.vars[name]` to `undefined` to not insert a variable which would otherwise
be inserted.

`opts.vars` properties with a `.` in their name will be executed instead of the
parent object if ONLY that property is used. For example, `"Buffer.isBuffer"`
will mask `"Buffer"` only when there is a `Buffer.isBuffer()` call in a file and
no other references to `Buffer`.

If `opts.debug` is true, an inline source map will be generated to compensate
for the extra lines.

# events

## inserter.on('global', function (name) {})

When a global is detected, the inserter stream emits a `'global'` event.

# usage

```
usage: insert-module-globals {basedir}
```

# install

With [npm](https://npmjs.org), to get the library do:

```
npm install insert-module-globals
```

and to get the bin script do:

```
npm install -g insert-module-globals
```

# insert custom globals.

`insert-module-globals` can also insert arbitary globals into files.
Pass in an object of functions as the `vars` option.

``` js
var vars = {
    process: function (file, basedir) {
        return {
            id: "path/to/custom_process.js",
            source: customProcessContent
        }
    },
    Buffer: function (file, basedir) {
        return {
            id: 'path/to/custom_buffer.js',
            source: customProcessContent,
            //suffix is optional
            //it's used to extract the value from the module.
            //it becomes: require(...).Buffer in this case.
            suffix: '.Buffer'
        }
    },
    Math: function () {
        //if you return a string,
        //it's simply set as the value.
        return '{}'
        //^ any attempt to use Math[x] will throw!
    }
}

function inserter (file) {
    return insert(file, { vars: vars });
}
mdeps(files, { transform: inserter })
    .pipe(bpack({ raw: true }))
    .pipe(process.stdout)
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
# labeled-stream-splicer

[stream splicer](https://npmjs.org/package/stream-splicer) with labels

[![build status](https://secure.travis-ci.org/substack/labeled-stream-splicer.png)](http://travis-ci.org/substack/labeled-stream-splicer)

# example

Here's an example that exposes a label for `deps` and `pack`:

``` js
var splicer = require('labeled-stream-splicer');
var through = require('through2');
var deps = require('module-deps');
var pack = require('browser-pack');
var lstream = require('lstream');

var pipeline = splicer.obj([
    'deps', [ deps() ],
    'pack', [ pack({ raw: true }) ]
]);

pipeline.get('deps').unshift(lstream());

pipeline.get('deps').push(through.obj(function (row, enc, next) {
    row.source = row.source.toUpperCase();
    this.push(row);
    next();
}));

process.stdin.pipe(pipeline).pipe(process.stdout);
```

Here the `deps` sub-pipeline is augmented with a post-transformation that
uppercases its source input.

# methods

``` js
var splicer = require('labeled-stream-splicer')
```

The API is the same as
[stream-splicer](https://npmjs.org/package/stream-splicer),
except that `pipeline.get()`, `pipeline.splice()`, and `pipeline.indexOf()` can
accept string labels in addition to numeric indexes.

## var pipeline = splicer(streams, opts)

Create a `pipeline` duplex stream given an array of `streams`. Each `stream`
will be piped to the next. Writes to `pipeline` get written to the first stream
and data for reads from `pipeline` come from the last stream.

To signify a label, a stream may have a `.label` property or a string may be
placed in the `streams` array.

For example, for streams `[ a, 'foo', b, c, 'bar', d ]`, this pipeline is
constructed internally:

```
a.pipe(b).pipe(c).pipe(d)
```

with a label `'foo`' that points to `b` and a label `'bar'` that points to `d`.
If `a` or `c` has a `.label` property, that label would be used for addressing.

Input will get written into `a`. Output will be read from `d`.

If any of the elements in `streams` are arrays, they will be converted into
nested labeled pipelines. This is useful if you want to expose a hookable
pipeline with grouped insertion points.

## var pipeline = splicer.obj(streams, opts)

Create a `pipeline` with `opts.objectMode` set to true for convenience.

## var removed = pipeline.splice(index, howMany, stream, ...)

Splice the pipeline starting at `index`, removing `howMany` streams and
replacing them with each additional `stream` argument provided.

The streams that were removed from the splice and returned.

`index` can be an integer index or a label.

## pipeline.push(stream, ...)

Push one or more streams to the end of the pipeline.

The stream arguments may have a `label` property that will be used for string
lookups.

## var stream = pipeline.pop()

Pop a stream from the end of the pipeline.

## pipeline.unshift(stream, ...)

Unshift one or more streams to the begining of the pipeline.

The stream arguments may have a `label` property that will be used for string
lookups.

## var stream = pipeline.shift()

Shift a stream from the begining of the pipeline.

## var stream = pipeline.get(index)

Return the stream at index `index`.

`index` can be an integer or a string label.

# install

With [npm](https://npmjs.org) do:

```
npm install labeled-stream-splicer
```

# license

MIT
# json-stable-stringify

deterministic version of `JSON.stringify()` so you can get a consistent hash
from stringified results

You can also pass in a custom comparison function.

[![browser support](https://ci.testling.com/substack/json-stable-stringify.png)](https://ci.testling.com/substack/json-stable-stringify)

[![build status](https://secure.travis-ci.org/substack/json-stable-stringify.png)](http://travis-ci.org/substack/json-stable-stringify)

# example

``` js
var stringify = require('json-stable-stringify');
var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
console.log(stringify(obj));
```

output:

```
{"a":3,"b":[{"x":4,"y":5,"z":6},7],"c":8}
```

# methods

``` js
var stringify = require('json-stable-stringify')
```

## var str = stringify(obj, opts)

Return a deterministic stringified string `str` from the object `obj`.

If `opts` is given, you can supply an `opts.cmp` to have a custom comparison
function for object keys. Your function `opts.cmp` is called with these
parameters:

``` js
opts.cmp({ key: akey, value: avalue }, { key: bkey, value: bvalue })
```

For example, to sort on the object key names in reverse order you could write:

``` js
var stringify = require('json-stable-stringify');

var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
var s = stringify(obj, function (a, b) {
    return a.key < b.key ? 1 : -1;
});
console.log(s);
```

which results in the output string:

```
{"c":8,"b":[{"z":6,"y":5,"x":4},7],"a":3}
```

Or if you wanted to sort on the object values in reverse order, you could write:

```
var stringify = require('json-stable-stringify');

var obj = { d: 6, c: 5, b: [{z:3,y:2,x:1},9], a: 10 };
var s = stringify(obj, function (a, b) {
    return a.value < b.value ? 1 : -1;
});
console.log(s);
```

which outputs:

```
{"d":6,"c":5,"b":[{"z":3,"y":2,"x":1},9],"a":10}
```

# install

With [npm](https://npmjs.org) do:

```
npm install json-stable-stringify
```

# license

MIT
# syntax-error

Detect and report syntax errors in source code strings.

[![build status](https://secure.travis-ci.org/substack/node-syntax-error.png)](http://travis-ci.org/substack/node-syntax-error)

When you type `node src.js` you get a friendly error report about exactly where
the syntax error is. This module lets you check for syntax errors and report
them in a similarly friendly format that wrapping a try/catch around
`Function()` or `vm.runInNewContext()` doesn't get you.

# example

``` js
var fs = require('fs');
var check = require('syntax-error');

var file = __dirname + '/src.js';
var src = fs.readFileSync(file);

var err = check(src, file);
if (err) {
    console.error('ERROR DETECTED' + Array(62).join('!'));
    console.error(err);
    console.error(Array(76).join('-'));
}
```

---

```
$ node check.js
ERROR DETECTED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

/home/substack/projects/node-syntax-error/example/src.js:5
        if (Array.isArray(x) res.push.apply(res, x);
                             ^
ParseError: Unexpected identifier
---------------------------------------------------------------------------
```

# methods

``` js
var check = require('syntax-error')
```

## var err = check(src, file, opts={})

Check the source code string `src` for syntax errors.
Optionally you can specify a filename `file` that will show up in the output.

If `src` has a syntax error, return an error object `err` that can be printed or
stringified.

If there are no syntax errors in `src`, return `undefined`.

Options will be passed through to [acorn-node](https://github.com/browserify/acorn-node).
acorn-node defaults to options that match the most recent Node versions.

## err.toString()

Return the long string description with a source snippet and a `^` under
pointing exactly where the error was detected.

# attributes

## err.message

short string description of the error type

## err.line

line number of the error in the original source (indexing starts at 1)

## err.column

column number of the error in the original source (indexing starts at 1)

# install

With [npm](http://npmjs.org) do:

```
npm install syntax-error
```

# license

MIT
# json-stable-stringify

deterministic version of `JSON.stringify()` so you can get a consistent hash
from stringified results

You can also pass in a custom comparison function.

[![browser support](https://ci.testling.com/substack/json-stable-stringify.png)](https://ci.testling.com/substack/json-stable-stringify)

[![build status](https://secure.travis-ci.org/substack/json-stable-stringify.png)](http://travis-ci.org/substack/json-stable-stringify)

# example

``` js
var stringify = require('json-stable-stringify');
var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
console.log(stringify(obj));
```

output:

```
{"a":3,"b":[{"x":4,"y":5,"z":6},7],"c":8}
```

# methods

``` js
var stringify = require('json-stable-stringify')
```

## var str = stringify(obj, opts)

Return a deterministic stringified string `str` from the object `obj`.

## options

### cmp

If `opts` is given, you can supply an `opts.cmp` to have a custom comparison
function for object keys. Your function `opts.cmp` is called with these
parameters:

``` js
opts.cmp({ key: akey, value: avalue }, { key: bkey, value: bvalue })
```

For example, to sort on the object key names in reverse order you could write:

``` js
var stringify = require('json-stable-stringify');

var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
var s = stringify(obj, function (a, b) {
    return a.key < b.key ? 1 : -1;
});
console.log(s);
```

which results in the output string:

```
{"c":8,"b":[{"z":6,"y":5,"x":4},7],"a":3}
```

Or if you wanted to sort on the object values in reverse order, you could write:

```
var stringify = require('json-stable-stringify');

var obj = { d: 6, c: 5, b: [{z:3,y:2,x:1},9], a: 10 };
var s = stringify(obj, function (a, b) {
    return a.value < b.value ? 1 : -1;
});
console.log(s);
```

which outputs:

```
{"d":6,"c":5,"b":[{"z":3,"y":2,"x":1},9],"a":10}
```

### space

If you specify `opts.space`, it will indent the output for pretty-printing.
Valid values are strings (e.g. `{space: \t}`) or a number of spaces
(`{space: 3}`).

For example:

```js
var obj = { b: 1, a: { foo: 'bar', and: [1, 2, 3] } };
var s = stringify(obj, { space: '  ' });
console.log(s);
```

which outputs:

```
{
  "a": {
    "and": [
      1,
      2,
      3
    ],
    "foo": "bar"
  },
  "b": 1
}
```

### replacer

The replacer parameter is a function `opts.replacer(key, value)` that behaves
the same as the replacer
[from the core JSON object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_native_JSON#The_replacer_parameter).

# install

With [npm](https://npmjs.org) do:

```
npm install json-stable-stringify
```

# license

MIT
# defined

return the first argument that is `!== undefined`

[![browser support](http://ci.testling.com/substack/defined.png)](http://ci.testling.com/substack/defined)

[![build status](https://secure.travis-ci.org/substack/defined.png)](http://travis-ci.org/substack/defined)

Most of the time when I chain together `||`s, I actually just want the first
item that is not `undefined`, not the first non-falsy item.

This module is like the defined-or (`//`) operator in perl 5.10+.

# example

``` js
var defined = require('defined');
var opts = { y : false, w : 4 };
var x = defined(opts.x, opts.y, opts.w, 100);
console.log(x);
```

```
$ node example/defined.js
false
```

The return value is `false` because `false` is the first item that is
`!== undefined`.

# methods

``` js
var defined = require('defined')
```

## var x = defined(a, b, c...)

Return the first item in the argument list `a, b, c...` that is `!== undefined`.

If all the items are `=== undefined`, return undefined.

# install

With [npm](https://npmjs.org) do:

```
npm install defined
```

# license

MIT
# module-deps

walk the dependency graph to generate json output that can be fed into
[browser-pack](https://github.com/browserify/browser-pack)

[![build status](https://secure.travis-ci.org/browserify/module-deps.png)](http://travis-ci.org/browserify/module-deps)

# example

``` js
var mdeps = require('module-deps');
var JSONStream = require('JSONStream');

var md = mdeps();
md.pipe(JSONStream.stringify()).pipe(process.stdout);
md.end({ file: __dirname + '/files/main.js' });
```

output:

```json
$ node example/deps.js
[
{"id":"/home/substack/projects/module-deps/example/files/main.js","source":"var foo = require('./foo');\nconsole.log('main: ' + foo(5));\n","entry":true,"deps":{"./foo":"/home/substack/projects/module-deps/example/files/foo.js"}}
,
{"id":"/home/substack/projects/module-deps/example/files/foo.js","source":"var bar = require('./bar');\n\nmodule.exports = function (n) {\n    return n * 111 + bar(n);\n};\n","deps":{"./bar":"/home/substack/projects/module-deps/example/files/bar.js"}}
,
{"id":"/home/substack/projects/module-deps/example/files/bar.js","source":"module.exports = function (n) {\n    return n * 100;\n};\n","deps":{}}
]
```

and you can feed this json data into
[browser-pack](https://github.com/browserify/browser-pack):

```bash
$ node example/deps.js | browser-pack | node
main: 1055
```

# usage

```
usage: module-deps [files]

  generate json output from each entry file

```

# methods

``` js
var mdeps = require('module-deps')
```

## var d = mdeps(opts={})

Return an object transform stream `d` that expects entry filenames or
`{ id: ..., file: ... }` objects as input and produces objects for every
dependency from a recursive module traversal as output.

Each file in `files` can be a string filename or a stream.

Optionally pass in some `opts`:

* `opts.transform` - a string or array of string transforms (see below)

* `opts.transformKey` - an array path of strings showing where to look in the
package.json for source transformations. If falsy, don't look at the
package.json at all.

* `opts.resolve` - custom resolve function using the
`opts.resolve(id, parent, cb)` signature that
[browser-resolve](https://github.com/shtylman/node-browser-resolve) has

* `opts.detect` - a custom dependency detection function. `opts.detect(source)`
should return an array of dependency module names. By default
[detective](https://github.com/browserify/detective) is used.

* `opts.filter` - a function (id) to skip resolution of some module `id` strings.
If defined, `opts.filter(id)` should return truthy for all the ids to include
and falsey for all the ids to skip.

* `opts.postFilter` - a function (id, file, pkg) that gets called after `id` has
been resolved. Return false to skip this file.

* `opts.packageFilter` - transform the parsed package.json contents before using
the values. `opts.packageFilter(pkg, dir)` should return the new `pkg` object to
use.

* `opts.noParse` - an array of absolute paths to not parse for dependencies. Use
this for large dependencies like jquery or threejs which take forever to parse.

* `opts.cache` - an object mapping filenames to file objects to skip costly io

* `opts.packageCache` - an object mapping filenames to their parent package.json
contents for browser fields, main entries, and transforms

* `opts.fileCache` - an object mapping filenames to raw source to avoid reading
from disk.

* `opts.persistentCache` - a complex cache handler that allows async and persistent
    caching of data. A `persistentCache` needs to follow this interface:
    ```js
    function persistentCache (
        file, // the path to the file that is loaded
        id,   // the id that is used to reference this file
        pkg,  // the package that this file belongs to fallback
        fallback, // async fallback handler to be called if the cache doesn't hold the given file 
        cb    // callback handler that receives the cache data
    ) {
        if (hasError()) {
            return cb(error) // Pass any error to the callback
        }

        var fileData = fs.readFileSync(file)
        var key = keyFromFile(file, fileData)

        if (db.has(key)) {
            return cb(null, {
                source: db.get(key).toString(),
                package: pkg, // The package for housekeeping
                deps: {
                    'id':  // id that is used to reference a required file
                    'file' // file path to the required file
                }
            })
        }
        //
        // The fallback will process the file in case the file is not
        // in cache.
        //
        // Note that if your implementation doesn't need the file data
        // then you can pass `null` instead of the source and the fallback will
        // fetch the data by itself.
        //
        fallback(fileData, function (error, cacheableEntry) {
            if (error) {
                return cb(error)
            }
            db.addToCache(key, cacheableEntry)
            cb(null, cacheableEntry)
        })
    }
    ```

* `opts.paths` - array of global paths to search. Defaults to splitting on `':'`
in `process.env.NODE_PATH`

* `opts.ignoreMissing` - ignore files that failed to resolve

# input objects

Input objects should be string filenames or objects with these parameters:

* `row.file` - filename
* `row.entry` - whether to treat this file as an entry point, defaults to
  `true`. Set to `false` to include this file, but not run it automatically.
* `row.expose` - name to be exposed as
* `row.noparse` - when true, don't parse the file contents for dependencies

or objects can specify transforms:

* `row.transform` - string name, path, or function
* `row.options` - transform options as an object
* `row.global` - boolean, whether the transform is global

# output objects

Output objects describe files with dependencies. They have these properties:

* `row.id` - an identifier for the file, used in the `row.deps` prperty
* `row.file` - path to the source file
* `row.entry` - true if the file is an entry point
* `row.expose` - name to be exposed as
* `row.source` - source file content as a string
* `row.deps` - object describing dependencies. The keys are strings as used
  in `require()` calls in the file, and values are the row IDs (file paths)
  of dependencies.

# events

## d.on('transform', function (tr, file) {})

Every time a transform is applied to a `file`, a `'transform'` event fires with
the instantiated transform stream `tr`.

## d.on('file', function (file) {})

Every time a file is read, this event fires with the file path.

## d.on('missing', function (id, parent) {})

When `opts.ignoreMissing` is enabled, this event fires for each missing package.

## d.on('package', function (pkg) {})

Every time a package is read, this event fires. The directory name of the
package is available in `pkg.__dirname`.

# transforms

module-deps can be configured to run source transformations on files before
parsing them for `require()` calls. These transforms are useful if you want to
compile a language like [coffeescript](http://coffeescript.org/) on the fly or
if you want to load static assets into your bundle by parsing the AST for
`fs.readFileSync()` calls.

If the transform is a function, it should take the `file` name as an argument
and return a through stream that will be written file contents and should output
the new transformed file contents.

If the transform is a string, it is treated as a module name that will resolve
to a module that is expected to follow this format:

``` js
var through = require('through2');
module.exports = function (file, opts) { return through() };
```

You don't necessarily need to use the
[through2](https://github.com/rvagg/through2) module to create a
readable/writable filter stream for transforming file contents, but this is an
easy way to do it.

module-deps looks for `require()` calls and adds their arguments as dependencies
of a file. Transform streams can emit `'dep'` events to include additional
dependencies that are not consumed with `require()`.

When you call `mdeps()` with an `opts.transform`, the transformations you
specify will not be run for any files in node_modules/. This is because modules
you include should be self-contained and not need to worry about guarding
themselves against transformations that may happen upstream.

Modules can apply their own transformations by setting a transformation pipeline
in their package.json at the `opts.transformKey` path. These transformations
only apply to the files directly in the module itself, not to the module's
dependants nor to its dependencies.

## package.json transformKey

Transform keys live at a configurable location in the package.json denoted by
the `opts.transformKey` array.

For a transformKey of `['foo','bar']`, the transformKey can be a single string
(`"fff"`):

``` json
{
  "foo": {
    "bar": "fff"
  }
}
```

or an array of strings (`["fff","ggg"]`):

``` json
{
  "foo": {
    "bar": ["fff","ggg"]
  }
}
```

If you want to pass options to the transforms, you can use a 2-element array
inside of the primary array. Here `fff` gets an options object with `{"x":3}`
and `ggg` gets `{"y":4}`:

``` json
{
  "foo": {
    "bar": [["fff",{"x":3}],["ggg",{"y":4}]]
  }
}
```

Options sent to the module-deps constructor are also provided under
`opts._flags`. These options are sometimes required if your transform
needs to do something different when browserify is run in debug mode, for
example.

# usage

```
module-deps [FILES] OPTIONS

  Generate json output for the entry point FILES.

OPTIONS are:

  -t TRANSFORM  Apply a TRANSFORM.
  -g TRANSFORM  Apply a global TRANSFORM.

```

# install

With [npm](http://npmjs.org), to get the module do:

```
npm install module-deps
```

and to get the `module-deps` command do:

```
npm install -g module-deps
```

# license

MIT
# Split (matcher)

[![build status](https://secure.travis-ci.org/dominictarr/split.png)](http://travis-ci.org/dominictarr/split)

Break up a stream and reassemble it so that each line is a chunk. matcher may be a `String`, or a `RegExp` 

Example, read every line in a file ...

``` js
  fs.createReadStream(file)
    .pipe(split())
    .on('data', function (line) {
      //each chunk now is a seperate line!
    })

```

`split` takes the same arguments as `string.split` except it defaults to '/\r?\n/' instead of ',', and the optional `limit` paremeter is ignored.
[String#split](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/String/split)

`split` takes an optional options object on it's third argument.

``` js
  split(matcher, mapper, options)
```

Valid options:

* maxLength - The maximum buffer length without seeing a newline or `matcher`,
  if a single line exceeds this, the split stream will emit an error.

``` js
  split(JSON.parse, null, { maxLength: 2})
```

## keep matched splitter

As with `Array#split`, if you split by a regular expression with a matching group,
the matches will be retained in the collection.

```
stdin
.pipe(split(/(\r?\n)/))
... //lines + separators.
```


# NDJ - Newline Delimited Json

`split` accepts a function which transforms each line.

``` js
fs.createReadStream(file)
  .pipe(split(JSON.parse))
  .on('data', function (obj) {
    //each chunk now is a a js object
  })
  .on('error', function (err) {
    //syntax errors will land here
    //note, this ends the stream.
  })
```

# License

MIT
# array-reduce

`[].reduce()` for old browsers

[![testling badge](https://ci.testling.com/substack/array-reduce.png)](https://ci.testling.com/substack/array-reduce)

[![build status](https://secure.travis-ci.org/substack/array-reduce.png)](http://travis-ci.org/substack/array-reduce)

# example

```
var reduce = require('array-reduce');
var xs = [ 1, 2, 3, 4 ];
var sum = reduce(xs, function (acc, x) { return acc + x }, 0);
console.log(sum);
```

output:

```
10
```

# methods

``` js
var reduce = require('array-reduce')
```

## var res = reduce(xs, f, init)

Create a result `res` by folding `acc = f(acc, xs[i], i)` over each element in
the array `xs` at element `i`. If `init` is given, the first `acc` value is
`init`, otherwise `xs[0]` is used.

# install

With [npm](https://npmjs.org) do:

```
npm install array-reduce
```

# license

MIT
# parents

Return all the parent directories of a directory, inclusive of that directory.

[![build status](https://secure.travis-ci.org/substack/node-parents.png)](http://travis-ci.org/substack/node-parents)

# example

## dirname

``` js
var parents = require('parents');
var dirs = parents(__dirname);
console.dir(dirs);
```

***

```
[ '/home/substack/projects/node-parents/example',
  '/home/substack/projects/node-parents',
  '/home/substack/projects',
  '/home/substack',
  '/home',
  '/' ]
```

## win32

``` js
var parents = require('parents');
var dir = 'C:\\Program Files\\Maxis\\Sim City 2000\\cities';

var dirs = parents(dir, { platform : 'win32' });
console.dir(dirs);
```

***

```
[ 'C:\\Program Files\\Maxis\\Sim City 2000\\cities',
  'C:\\Program Files\\Maxis\\Sim City 2000',
  'C:\\Program Files\\Maxis',
  'C:\\Program Files',
  'C:' ]
```

# methods

``` js
var parents = require('parents')
```

## parents(dir, opts)

Return an array of the parent directories of `dir`, including and starting with
`dir`. If a `dir` isn't specified, `process.cwd()` will be used.

Optionally specify an `opts.platform` to control whether the separator and paths
works the unixy way with `'/'` or the windowsy way where sometimes things use
`'/'` and sometimes they use `'\\'` and also there are leading drive letters and
other exotic features. If `opts.platform` isn't specified, `process.platform`
will be used. Anything that matches `/^win/` will use the windowsy behavior.

# install

With [npm](http://npmjs.org) do:

```
npm install parents
```

# licence

MIT
# json-stable-stringify

deterministic version of `JSON.stringify()` so you can get a consistent hash
from stringified results

You can also pass in a custom comparison function.

[![browser support](https://ci.testling.com/substack/json-stable-stringify.png)](https://ci.testling.com/substack/json-stable-stringify)

[![build status](https://secure.travis-ci.org/substack/json-stable-stringify.png)](http://travis-ci.org/substack/json-stable-stringify)

# example

``` js
var stringify = require('json-stable-stringify');
var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
console.log(stringify(obj));
```

output:

```
{"a":3,"b":[{"x":4,"y":5,"z":6},7],"c":8}
```

# methods

``` js
var stringify = require('json-stable-stringify')
```

## var str = stringify(obj, opts)

Return a deterministic stringified string `str` from the object `obj`.

## options

### cmp

If `opts` is given, you can supply an `opts.cmp` to have a custom comparison
function for object keys. Your function `opts.cmp` is called with these
parameters:

``` js
opts.cmp({ key: akey, value: avalue }, { key: bkey, value: bvalue })
```

For example, to sort on the object key names in reverse order you could write:

``` js
var stringify = require('json-stable-stringify');

var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
var s = stringify(obj, function (a, b) {
    return a.key < b.key ? 1 : -1;
});
console.log(s);
```

which results in the output string:

```
{"c":8,"b":[{"z":6,"y":5,"x":4},7],"a":3}
```

Or if you wanted to sort on the object values in reverse order, you could write:

```
var stringify = require('json-stable-stringify');

var obj = { d: 6, c: 5, b: [{z:3,y:2,x:1},9], a: 10 };
var s = stringify(obj, function (a, b) {
    return a.value < b.value ? 1 : -1;
});
console.log(s);
```

which outputs:

```
{"d":6,"c":5,"b":[{"z":3,"y":2,"x":1},9],"a":10}
```

### space

If you specify `opts.space`, it will indent the output for pretty-printing.
Valid values are strings (e.g. `{space: \t}`) or a number of spaces
(`{space: 3}`).

For example:

```js
var obj = { b: 1, a: { foo: 'bar', and: [1, 2, 3] } };
var s = stringify(obj, { space: '  ' });
console.log(s);
```

which outputs:

```
{
  "a": {
    "and": [
      1,
      2,
      3
    ],
    "foo": "bar"
  },
  "b": 1
}
```

### replacer

The replacer parameter is a function `opts.replacer(key, value)` that behaves
the same as the replacer
[from the core JSON object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_native_JSON#The_replacer_parameter).

# install

With [npm](https://npmjs.org) do:

```
npm install json-stable-stringify
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
// Load modules

var Code = require('code');
var Hawk = require('../lib');
var Hoek = require('hoek');
var Lab = require('lab');


// Declare internals

var internals = {};


// Test shortcuts

var lab = exports.lab = Lab.script();
var describe = lab.experiment;
var it = lab.test;
var expect = Code.expect;


describe('README', function () {

    describe('core', function () {

        var credentials = {
            id: 'dh37fgj492je',
            key: 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn',
            algorithm: 'sha256'
        };

        var options = {
            credentials: credentials,
            timestamp: 1353832234,
            nonce: 'j4h3g2',
            ext: 'some-app-ext-data'
        };

        it('should generate a header protocol example', function (done) {

            var header = Hawk.client.header('http://example.com:8000/resource/1?b=1&a=2', 'GET', options).field;

            expect(header).to.equal('Hawk id="dh37fgj492je", ts="1353832234", nonce="j4h3g2", ext="some-app-ext-data", mac="6R4rV5iE+NPoym+WwjeHzjAGXUtLNIxmo1vpMofpLAE="');
            done();
        });

        it('should generate a normalized string protocol example', function (done) {

            var normalized = Hawk.crypto.generateNormalizedString('header', {
                credentials: credentials,
                ts: options.timestamp,
                nonce: options.nonce,
                method: 'GET',
                resource: '/resource?a=1&b=2',
                host: 'example.com',
                port: 8000,
                ext: options.ext
            });

            expect(normalized).to.equal('hawk.1.header\n1353832234\nj4h3g2\nGET\n/resource?a=1&b=2\nexample.com\n8000\n\nsome-app-ext-data\n');
            done();
        });

        var payloadOptions = Hoek.clone(options);
        payloadOptions.payload = 'Thank you for flying Hawk';
        payloadOptions.contentType = 'text/plain';

        it('should generate a header protocol example (with payload)', function (done) {

            var header = Hawk.client.header('http://example.com:8000/resource/1?b=1&a=2', 'POST', payloadOptions).field;

            expect(header).to.equal('Hawk id="dh37fgj492je", ts="1353832234", nonce="j4h3g2", hash="Yi9LfIIFRtBEPt74PVmbTF/xVAwPn7ub15ePICfgnuY=", ext="some-app-ext-data", mac="aSe1DERmZuRl3pI36/9BdZmnErTw3sNzOOAUlfeKjVw="');
            done();
        });

        it('should generate a normalized string protocol example (with payload)', function (done) {

            var normalized = Hawk.crypto.generateNormalizedString('header', {
                credentials: credentials,
                ts: options.timestamp,
                nonce: options.nonce,
                method: 'POST',
                resource: '/resource?a=1&b=2',
                host: 'example.com',
                port: 8000,
                hash: Hawk.crypto.calculatePayloadHash(payloadOptions.payload, credentials.algorithm, payloadOptions.contentType),
                ext: options.ext
            });

            expect(normalized).to.equal('hawk.1.header\n1353832234\nj4h3g2\nPOST\n/resource?a=1&b=2\nexample.com\n8000\nYi9LfIIFRtBEPt74PVmbTF/xVAwPn7ub15ePICfgnuY=\nsome-app-ext-data\n');
            done();
        });
    });
});

# stream-splicer

streaming pipeline with a mutable configuration

This module is similar to
[stream-combiner](https://npmjs.org/package/stream-combiner),
but with a pipeline configuration that can be changed at runtime.

[![build status](https://travis-ci.org/substack/stream-splicer.png?branch=master)](http://travis-ci.org/substack/stream-splicer)

# example

This example begins with an HTTP header parser that waits for an empty line to
signify the end of the header. At that point, it switches to a streaming json
parser to operate on the HTTP body.

``` js
var splicer = require('stream-splicer');
var through = require('through2');
var JSONStream = require('JSONStream');
var split = require('split');

var headerData = {};
var headers = through.obj(function (buf, enc, next) {
    var line = buf.toString('utf8');
    if (line === '') {
        this.push(headerData);
        pipeline.splice(1, 1, JSONStream.parse([ 'rows', true ]));
    }
    else {
        var m = /^(\S+):(.+)/.exec(line);
        var key = m && m[1].trim();
        var value = m && m[2].trim();
        if (m) headerData[key] = value;
    }
    next();
});
var pipeline = splicer([ split(), headers, JSONStream.stringify() ]);
process.stdin.pipe(pipeline).pipe(process.stdout);
```

intput:

```
GET / HTTP/1.1
Host: substack.net
User-Agent: echo

{"rows":["beep","boop"]}
```

output:

```
$ echo -ne 'GET / HTTP/1.1\nHost: substack.net\nUser-Agent: echo\n\n{"rows":["beep","boop"]}\n' | node example/header.js
[
{"Host":"substack.net","User-Agent":"echo"}
,
"beep"
,
"boop"
]
```

# methods

``` js
var splicer = require('stream-splicer')
```

## var pipeline = splicer(streams, opts)

Create a `pipeline` duplex stream given an array of `streams`. Each `stream`
will be piped to the next. Writes to `pipeline` get written to the first stream
and data for reads from `pipeline` come from the last stream.

For example, for streams `[ a, b, c, d ]`, this pipeline is constructed
internally:

```
a.pipe(b).pipe(c).pipe(d)
```

Input will get written into `a`. Output will be read from `d`.

If any of the elements in `streams` are arrays, they will be converted into
nested pipelines. This is useful if you want to expose a hookable pipeline with
grouped insertion points.

## var pipeline = splicer.obj(streams, opts)

Create a `pipeline` with `opts.objectMode` set to true for convenience.

## var removed = pipeline.splice(index, howMany, stream, ...)

Splice the pipeline starting at `index`, removing `howMany` streams and
replacing them with each additional `stream` argument provided.

The streams that were removed from the splice and returned.

## pipeline.push(stream, ...)

Push one or more streams to the end of the pipeline.

## var stream = pipeline.pop()

Pop a stream from the end of the pipeline.

## pipeline.unshift(stream, ...)

Unshift one or more streams to the begining of the pipeline.

## var stream = pipeline.shift()

Shift a stream from the begining of the pipeline.

## var stream = pipeline.get(index, ...)

Return the stream at index `index, ...`. Indexes can be negative.

Multiple indexes will traverse into nested pipelines.

# attributes

## pipeline.length

The number of streams in the pipeline

# install

With [npm](https://npmjs.org) do:

```
npm install stream-splicer
```

# license

MIT
# JSONStream

streaming JSON.parse and stringify

![](https://secure.travis-ci.org/dominictarr/JSONStream.png?branch=master)

## install
```npm install JSONStream```

## example

``` js

var request = require('request')
  , JSONStream = require('JSONStream')
  , es = require('event-stream')

request({url: 'http://isaacs.couchone.com/registry/_all_docs'})
  .pipe(JSONStream.parse('rows.*'))
  .pipe(es.mapSync(function (data) {
    console.error(data)
    return data
  }))
```

## JSONStream.parse(path)

parse stream of values that match a path

``` js
  JSONStream.parse('rows.*.doc')
```

The `..` operator is the recursive descent operator from [JSONPath](http://goessner.net/articles/JsonPath/), which will match a child at any depth (see examples below).

If your keys have keys that include `.` or `*` etc, use an array instead.
`['row', true, /^doc/]`.

If you use an array, `RegExp`s, booleans, and/or functions. The `..` operator is also available in array representation, using `{recurse: true}`.
any object that matches the path will be emitted as 'data' (and `pipe`d down stream)

If `path` is empty or null, no 'data' events are emitted.

If you want to have keys emitted, you can prefix your `*` operator with `$`: `obj.$*` - in this case the data passed to the stream is an object with a `key` holding the key and a `value` property holding the data.

### Examples

query a couchdb view:

``` bash
curl -sS localhost:5984/tests/_all_docs&include_docs=true
```
you will get something like this:

``` js
{"total_rows":129,"offset":0,"rows":[
  { "id":"change1_0.6995461115147918"
  , "key":"change1_0.6995461115147918"
  , "value":{"rev":"1-e240bae28c7bb3667f02760f6398d508"}
  , "doc":{
      "_id":  "change1_0.6995461115147918"
    , "_rev": "1-e240bae28c7bb3667f02760f6398d508","hello":1}
  },
  { "id":"change2_0.6995461115147918"
  , "key":"change2_0.6995461115147918"
  , "value":{"rev":"1-13677d36b98c0c075145bb8975105153"}
  , "doc":{
      "_id":"change2_0.6995461115147918"
    , "_rev":"1-13677d36b98c0c075145bb8975105153"
    , "hello":2
    }
  },
]}

```

we are probably most interested in the `rows.*.doc`

create a `Stream` that parses the documents from the feed like this:

``` js
var stream = JSONStream.parse(['rows', true, 'doc']) //rows, ANYTHING, doc

stream.on('data', function(data) {
  console.log('received:', data);
});
//emits anything from _before_ the first match
stream.on('header', function (data) {
  console.log('header:', data) // => {"total_rows":129,"offset":0}
})

```
awesome!

In case you wanted the contents the doc emitted:

``` js
var stream = JSONStream.parse(['rows', true, 'doc', {emitKey: true}]) //rows, ANYTHING, doc, items in docs with keys

stream.on('data', function(data) {
  console.log('key:', data.key);
  console.log('value:', data.value);
});

```

You can also emit the path:

``` js
var stream = JSONStream.parse(['rows', true, 'doc', {emitPath: true}]) //rows, ANYTHING, doc, items in docs with keys

stream.on('data', function(data) {
  console.log('path:', data.path);
  console.log('value:', data.value);
});

```

### recursive patterns (..)

`JSONStream.parse('docs..value')` 
(or `JSONStream.parse(['docs', {recurse: true}, 'value'])` using an array)
will emit every `value` object that is a child, grand-child, etc. of the 
`docs` object. In this example, it will match exactly 5 times at various depth
levels, emitting 0, 1, 2, 3 and 4 as results.

```js
{
  "total": 5,
  "docs": [
    {
      "key": {
        "value": 0,
        "some": "property"
      }
    },
    {"value": 1},
    {"value": 2},
    {"blbl": [{}, {"a":0, "b":1, "value":3}, 10]},
    {"value": 4}
  ]
}
```

## JSONStream.parse(pattern, map)

provide a function that can be used to map or filter
the json output. `map` is passed the value at that node of the pattern,
if `map` return non-nullish (anything but `null` or `undefined`)
that value will be emitted in the stream. If it returns a nullish value,
nothing will be emitted.

`JSONStream` also emits `'header'` and `'footer'` events,
the `'header'` event contains anything in the output that was before
the first match, and the `'footer'`, is anything after the last match.

## JSONStream.stringify(open, sep, close)

Create a writable stream.

you may pass in custom `open`, `close`, and `seperator` strings.
But, by default, `JSONStream.stringify()` will create an array,
(with default options `open='[\n', sep='\n,\n', close='\n]\n'`)

If you call `JSONStream.stringify(false)`
the elements will only be seperated by a newline.

If you only write one item this will be valid JSON.

If you write many items,
you can use a `RegExp` to split it into valid chunks.

## JSONStream.stringifyObject(open, sep, close)

Very much like `JSONStream.stringify`,
but creates a writable stream for objects instead of arrays.

Accordingly, `open='{\n', sep='\n,\n', close='\n}\n'`.

When you `.write()` to the stream you must supply an array with `[ key, data ]`
as the first argument.

## unix tool

query npm to see all the modules that browserify has ever depended on.

``` bash
curl https://registry.npmjs.org/browserify | JSONStream 'versions.*.dependencies'
```

## numbers

numbers will be emitted as numbers.
huge numbers that cannot be represented in memory as javascript numbers will be emitted as strings.
cf https://github.com/creationix/jsonparse/commit/044b268f01c4b8f97fb936fc85d3bcfba179e5bb for details.

## Acknowlegements

this module depends on https://github.com/creationix/jsonparse
by Tim Caswell
and also thanks to Florent Jaby for teaching me about parsing with:
https://github.com/Floby/node-json-streams

## license

Dual-licensed under the MIT License or the Apache License, version 2.0

# Split (matcher)

[![build status](https://secure.travis-ci.org/dominictarr/split.png)](http://travis-ci.org/dominictarr/split)

Break up a stream and reassemble it so that each line is a chunk. matcher may be a `String`, or a `RegExp`

Example, read every line in a file ...

``` js
  fs.createReadStream(file)
    .pipe(split())
    .on('data', function (line) {
      //each chunk now is a separate line!
    })

```

`split` takes the same arguments as `string.split` except it defaults to '/\r?\n/' instead of ',', and the optional `limit` parameter is ignored.
[String#split](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/String/split)

`split` takes an optional options object on its third argument.

``` js
  split(matcher, mapper, options)
```

Valid options:

* maxLength - The maximum buffer length without seeing a newline or `matcher`,
  if a single line exceeds this, the split stream will emit an error.

``` js
  split(JSON.parse, null, { maxLength: 2})
```

* trailing - By default the last buffer not delimited by a newline or `matcher` will be emitted. To prevent this set `options.trailing` to `false`.

``` js
  split(JSON.parse, null, { trailing: false })
```

## keep matched splitter

As with `String#split`, if you split by a regular expression with a matching group,
the matches will be retained in the collection.

```
stdin
.pipe(split(/(\r?\n)/))
... //lines + separators.
```


# NDJ - Newline Delimited Json

`split` accepts a function which transforms each line.

``` js
fs.createReadStream(file)
  .pipe(split(JSON.parse))
  .on('data', function (obj) {
    //each chunk now is a a js object
  })
  .on('error', function (err) {
    //syntax errors will land here
    //note, this ends the stream.
  })
```

# License

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
# deps-sort

sort [module-deps](https://npmjs.org/package/module-deps) output for deterministic
browserify bundles

[![build status](https://secure.travis-ci.org/substack/deps-sort.png)](http://travis-ci.org/substack/deps-sort)

# example

## command-line

```
$ for((i=0;i<5;i++)); do module-deps main.js | deps-sort | browser-pack | md5sum; done
e9e630de2c62953140357db0444c3c3a  -
e9e630de2c62953140357db0444c3c3a  -
e9e630de2c62953140357db0444c3c3a  -
e9e630de2c62953140357db0444c3c3a  -
e9e630de2c62953140357db0444c3c3a  -
```

or using `browserify --deps` on a [voxeljs](http://voxeljs.com/) project:

```
$ for((i=0;i<5;i++)); do browserify --deps browser.js | deps-sort | browser-pack | md5sum; done
fb418c74b53ba2e4cef7d01808b848e6  -
fb418c74b53ba2e4cef7d01808b848e6  -
fb418c74b53ba2e4cef7d01808b848e6  -
fb418c74b53ba2e4cef7d01808b848e6  -
fb418c74b53ba2e4cef7d01808b848e6  -
```

## api

To use this module programmatically, write streaming object data and read
streaming object data:

``` js
var sort = require('../')();
var JSONStream = require('JSONStream');
var parse = JSONStream.parse([ true ]);
var stringify = JSONStream.stringify();

process.stdin.pipe(parse).pipe(sort).pipe(stringify).pipe(process.stdout);
```

# methods

``` js
var depsSort = require('deps-sort');
```

## var stream = depsSort(opts)

Return a new through `stream` that should get written
[module-deps](https://npmjs.org/package/module-deps) objects and will output
sorted objects.

`opts` can be:

* `opts.index` - when true, for each module-deps row, insert `row.index` with
the numeric index and `row.indexDeps` like `row.deps` but mapping require
strings to row indices

* `opts.expose` - array of names or object mapping names to `true` not to mangle
with integer indexes when `opts.index` is turned on. If `opts.expose` maps names
to strings, those strings will be used to resolve the indexed references.

* `opts.dedupe` - set `row.dedupe` for files that match existing contents. Sets
`row.dedupeIndex` when `opts.index` is enabled. When `row.dedupe` is set,
`row.sameDeps` will be set to a boolean of whether the dependencies at the
dedupe target match (true) or just the source content (false).

# install

With [npm](https://npmjs.org) do:

```
npm install deps-sort
```

# license

MIT
# array-map

`[].map(f)` for older browsers

[![testling badge](https://ci.testling.com/substack/array-map.png)](https://ci.testling.com/substack/array-map)

[![build status](https://secure.travis-ci.org/substack/array-map.png)](http://travis-ci.org/substack/array-map)

# example

``` js
var map = require('array-map');
var letters = map([97,98,99], function (c) {
    return String.fromCharCode(c);
});
console.log(letters.join(''));
```

output:

```
abc
```

# methods

``` js
var map = require('array-map')
```

## var ys = map(xs, f)

Create a new array `ys` by applying `f(xs[i], i, xs)` to each element in `xs` at
index `i`.

# install

With [npm](https://npmjs.org) do:

```
npm install array-map
```

# license

MIT
// Load modules

var Code = require('code');
var Hawk = require('../lib');
var Hoek = require('hoek');
var Lab = require('lab');


// Declare internals

var internals = {};


// Test shortcuts

var lab = exports.lab = Lab.script();
var describe = lab.experiment;
var it = lab.test;
var expect = Code.expect;


describe('README', function () {

    describe('core', function () {

        var credentials = {
            id: 'dh37fgj492je',
            key: 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn',
            algorithm: 'sha256'
        };

        var options = {
            credentials: credentials,
            timestamp: 1353832234,
            nonce: 'j4h3g2',
            ext: 'some-app-ext-data'
        };

        it('should generate a header protocol example', function (done) {

            var header = Hawk.client.header('http://example.com:8000/resource/1?b=1&a=2', 'GET', options).field;

            expect(header).to.equal('Hawk id="dh37fgj492je", ts="1353832234", nonce="j4h3g2", ext="some-app-ext-data", mac="6R4rV5iE+NPoym+WwjeHzjAGXUtLNIxmo1vpMofpLAE="');
            done();
        });

        it('should generate a normalized string protocol example', function (done) {

            var normalized = Hawk.crypto.generateNormalizedString('header', {
                credentials: credentials,
                ts: options.timestamp,
                nonce: options.nonce,
                method: 'GET',
                resource: '/resource?a=1&b=2',
                host: 'example.com',
                port: 8000,
                ext: options.ext
            });

            expect(normalized).to.equal('hawk.1.header\n1353832234\nj4h3g2\nGET\n/resource?a=1&b=2\nexample.com\n8000\n\nsome-app-ext-data\n');
            done();
        });

        var payloadOptions = Hoek.clone(options);
        payloadOptions.payload = 'Thank you for flying Hawk';
        payloadOptions.contentType = 'text/plain';

        it('should generate a header protocol example (with payload)', function (done) {

            var header = Hawk.client.header('http://example.com:8000/resource/1?b=1&a=2', 'POST', payloadOptions).field;

            expect(header).to.equal('Hawk id="dh37fgj492je", ts="1353832234", nonce="j4h3g2", hash="Yi9LfIIFRtBEPt74PVmbTF/xVAwPn7ub15ePICfgnuY=", ext="some-app-ext-data", mac="aSe1DERmZuRl3pI36/9BdZmnErTw3sNzOOAUlfeKjVw="');
            done();
        });

        it('should generate a normalized string protocol example (with payload)', function (done) {

            var normalized = Hawk.crypto.generateNormalizedString('header', {
                credentials: credentials,
                ts: options.timestamp,
                nonce: options.nonce,
                method: 'POST',
                resource: '/resource?a=1&b=2',
                host: 'example.com',
                port: 8000,
                hash: Hawk.crypto.calculatePayloadHash(payloadOptions.payload, credentials.algorithm, payloadOptions.contentType),
                ext: options.ext
            });

            expect(normalized).to.equal('hawk.1.header\n1353832234\nj4h3g2\nPOST\n/resource?a=1&b=2\nexample.com\n8000\nYi9LfIIFRtBEPt74PVmbTF/xVAwPn7ub15ePICfgnuY=\nsome-app-ext-data\n');
            done();
        });
    });
});

# tty-browserify
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
* `opts.boolean` - a boolean, string or array of strings to always treat as
booleans. if `true` will treat all double hyphenated arguments without equal signs
as boolean (e.g. affects `--foo`, not `-f` or `--foo=bar`)
* `opts.alias` - an object mapping string names to strings or arrays of string
argument names to use as aliases
* `opts.default` - an object mapping string argument names to default values
* `opts['--']` - when true, populate `argv._` with everything before the `--`
and `argv['--']` with everything after the `--`. Here's an example:

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
# browserify

`require('modules')` in the browser

Use a [node](http://nodejs.org)-style `require()` to organize your browser code
and load modules installed by [npm](https://www.npmjs.com).

browserify will recursively analyze all the `require()` calls in your app in
order to build a bundle you can serve up to the browser in a single `<script>`
tag.

[![build status](https://img.shields.io/travis/browserify/browserify/master.svg)](https://travis-ci.org/browserify/browserify)

![browserify!](./assets/logo.png)

# getting started

If you're new to browserify, check out the
[browserify handbook](https://github.com/browserify/browserify-handbook)
and the resources on [browserify.org](http://browserify.org/).

# example

Whip up a file, `main.js` with some `require()`s in it. You can use relative
paths like `'./foo.js'` and `'../lib/bar.js'` or module paths like `'gamma'`
that will search `node_modules/` using
[node's module lookup algorithm](https://github.com/browserify/resolve).

``` js
var foo = require('./foo.js');
var bar = require('../lib/bar.js');
var gamma = require('gamma');

var elem = document.getElementById('result');
var x = foo(100) + bar('baz');
elem.textContent = gamma(x);
```

Export functionality by assigning onto `module.exports` or `exports`:

``` js
module.exports = function (n) { return n * 111 }
```

Now just use the `browserify` command to build a bundle starting at `main.js`:

```
$ browserify main.js > bundle.js
```

All of the modules that `main.js` needs are included in the `bundle.js` from a
recursive walk of the `require()` graph using
[required](https://github.com/defunctzombie/node-required).

To use this bundle, just toss a `<script src="bundle.js"></script>` into your
html!

# install

With [npm](https://www.npmjs.com/) do:

```
npm install -g browserify
```

# usage

```
Usage: browserify [entry files] {OPTIONS}

Standard Options:

    --outfile, -o  Write the browserify bundle to this file.
                   If unspecified, browserify prints to stdout.

    --require, -r  A module name or file to bundle.require()
                   Optionally use a colon separator to set the target.

      --entry, -e  An entry point of your app

     --ignore, -i  Replace a file with an empty stub. Files can be globs.

    --exclude, -u  Omit a file from the output bundle. Files can be globs.

   --external, -x  Reference a file from another bundle. Files can be globs.

  --transform, -t  Use a transform module on top-level files.

    --command, -c  Use a transform command on top-level files.

  --standalone -s  Generate a UMD bundle for the supplied export name.
                   This bundle works with other module systems and sets the name
                   given as a window global if no module system is found.

       --debug -d  Enable source maps that allow you to debug your files
                   separately.

       --help, -h  Show this message

For advanced options, type `browserify --help advanced`.

Specify a parameter.
```

```
Advanced Options:

  --insert-globals, --ig, --fast    [default: false]

    Skip detection and always insert definitions for process, global,
    __filename, and __dirname.

    benefit: faster builds
    cost: extra bytes

  --insert-global-vars, --igv

    Comma-separated list of global variables to detect and define.
    Default: __filename,__dirname,process,Buffer,global

  --detect-globals, --dg            [default: true]

    Detect the presence of process, global, __filename, and __dirname and define
    these values when present.

    benefit: npm modules more likely to work
    cost: slower builds

  --ignore-missing, --im            [default: false]

    Ignore `require()` statements that don't resolve to anything.

  --noparse=FILE

    Don't parse FILE at all. This will make bundling much, much faster for giant
    libs like jquery or threejs.

  --no-builtins

    Turn off builtins. This is handy when you want to run a bundle in node which
    provides the core builtins.

  --no-commondir

    Turn off setting a commondir. This is useful if you want to preserve the
    original paths that a bundle was generated with.

  --no-bundle-external

    Turn off bundling of all external modules. This is useful if you only want
    to bundle your local files.

  --bare

    Alias for both --no-builtins, --no-commondir, and sets --insert-global-vars
    to just "__filename,__dirname". This is handy if you want to run bundles in
    node.

  --no-browser-field, --no-bf

    Turn off package.json browser field resolution. This is also handy if you
    need to run a bundle in node.

  --transform-key

    Instead of the default package.json#browserify#transform field to list
    all transforms to apply when running browserify, a custom field, like, e.g.
    package.json#browserify#production or package.json#browserify#staging
    can be used, by for example running:
    * `browserify index.js --transform-key=production > bundle.js`
    * `browserify index.js --transform-key=staging > bundle.js`

  --node

    Alias for --bare and --no-browser-field.

  --full-paths

    Turn off converting module ids into numerical indexes. This is useful for
    preserving the original paths that a bundle was generated with.

  --deps

    Instead of standard bundle output, print the dependency array generated by
    module-deps.

  --no-dedupe

    Turn off deduping.

  --list

    Print each file in the dependency graph. Useful for makefiles.

  --extension=EXTENSION

    Consider files with specified EXTENSION as modules, this option can used
    multiple times.

  --global-transform=MODULE, -g MODULE

    Use a transform module on all files after any ordinary transforms have run.

  --ignore-transform=MODULE, -it MODULE

    Do not run certain transformations, even if specified elsewhere.

  --plugin=MODULE, -p MODULE

    Register MODULE as a plugin.

Passing arguments to transforms and plugins:

  For -t, -g, and -p, you may use subarg syntax to pass options to the
  transforms or plugin function as the second parameter. For example:

    -t [ foo -x 3 --beep ]

  will call the `foo` transform for each applicable file by calling:

    foo(file, { x: 3, beep: true })

```

# compatibility

Many [npm](https://www.npmjs.com/) modules that don't do IO will just work after being
browserified. Others take more work.

Many node built-in modules have been wrapped to work in the browser, but only
when you explicitly `require()` or use their functionality.

When you `require()` any of these modules, you will get a browser-specific shim:

* [assert](https://www.npmjs.com/package/assert)
* [buffer](https://www.npmjs.com/package/buffer)
* [console](https://www.npmjs.com/package/console-browserify)
* [constants](https://www.npmjs.com/package/constants-browserify)
* [crypto](https://www.npmjs.com/package/crypto-browserify)
* [domain](https://www.npmjs.com/package/domain-browser)
* [events](https://www.npmjs.com/package/events)
* [http](https://www.npmjs.com/package/stream-http)
* [https](https://www.npmjs.com/package/https-browserify)
* [os](https://www.npmjs.com/package/os-browserify)
* [path](https://www.npmjs.com/package/path-browserify)
* [punycode](https://www.npmjs.com/package/punycode)
* [querystring](https://www.npmjs.com/package/querystring-es3)
* [stream](https://www.npmjs.com/package/stream-browserify)
* [string_decoder](https://www.npmjs.com/package/string_decoder)
* [timers](https://www.npmjs.com/package/timers-browserify)
* [tty](https://www.npmjs.com/package/tty-browserify)
* [url](https://www.npmjs.com/package/url)
* [util](https://www.npmjs.com/package/util)
* [vm](https://www.npmjs.com/package/vm-browserify)
* [zlib](https://www.npmjs.com/package/browserify-zlib)

Additionally, if you use any of these variables, they
[will be defined](https://github.com/browserify/insert-module-globals)
in the bundled output in a browser-appropriate way:

* [process](https://www.npmjs.com/package/process)
* [Buffer](https://www.npmjs.com/package/buffer)
* global - top-level scope object (window)
* __filename - file path of the currently executing file
* __dirname - directory path of the currently executing file

# more examples

## external requires

You can just as easily create a bundle that will export a `require()` function so
you can `require()` modules from another script tag. Here we'll create a
`bundle.js` with the [through](https://www.npmjs.com/package/through)
and [duplexer](https://www.npmjs.com/package/duplexer) modules.

```
$ browserify -r through -r duplexer -r ./my-file.js:my-module > bundle.js
```

Then in your page you can do:

``` html
<script src="bundle.js"></script>
<script>
  var through = require('through');
  var duplexer = require('duplexer');
  var myModule = require('my-module');
  /* ... */
</script>
```

## external source maps

If you prefer the source maps be saved to a separate `.js.map` source map file, you may use
[exorcist](https://github.com/thlorenz/exorcist) in order to achieve that. It's as simple as:

```
$ browserify main.js --debug | exorcist bundle.js.map > bundle.js
```

Learn about additional options [here](https://github.com/thlorenz/exorcist#usage).

## multiple bundles

If browserify finds a `require`d function already defined in the page scope, it
will fall back to that function if it didn't find any matches in its own set of
bundled modules.

In this way, you can use browserify to split up bundles among multiple pages to
get the benefit of caching for shared, infrequently-changing modules, while
still being able to use `require()`. Just use a combination of `--external` and
`--require` to factor out common dependencies.

For example, if a website with 2 pages, `beep.js`:

``` js
var robot = require('./robot.js');
console.log(robot('beep'));
```

and `boop.js`:

``` js
var robot = require('./robot.js');
console.log(robot('boop'));
```

both depend on `robot.js`:

``` js
module.exports = function (s) { return s.toUpperCase() + '!' };
```

```
$ browserify -r ./robot.js > static/common.js
$ browserify -x ./robot.js beep.js > static/beep.js
$ browserify -x ./robot.js boop.js > static/boop.js
```

Then on the beep page you can have:

``` html
<script src="common.js"></script>
<script src="beep.js"></script>
```

while the boop page can have:

``` html
<script src="common.js"></script>
<script src="boop.js"></script>
```

This approach using `-r` and `-x` works fine for a small number of split assets,
but there are plugins for automatically factoring out components which are
described in the
[partitioning section of the browserify handbook](https://github.com/browserify/browserify-handbook#partitioning).

## api example

You can use the API directly too:

``` js
var browserify = require('browserify');
var b = browserify();
b.add('./browser/main.js');
b.bundle().pipe(process.stdout);
```

# methods

``` js
var browserify = require('browserify')
```

## `browserify([files] [, opts])`

Returns a new browserify instance.

<dl>
<dt>
files
</dt>

<dd>
String, file object, or array of those types (they may be mixed) specifying entry file(s).
</dd>

<dt>
opts
</dt>

<dd>
Object.
</dd>
</dl>

`files` and `opts` are both optional, but must be in the order shown if both are
passed.

Entry files may be passed in `files` and / or `opts.entries`.

External requires may be specified in `opts.require`, accepting the same formats
that the `files` argument does.

If an entry file is a stream, its contents will be used. You should pass
`opts.basedir` when using streaming files so that relative requires can be
resolved.

`opts.entries` has the same definition as `files`.

`opts.noParse` is an array which will skip all require() and global parsing for
each file in the array. Use this for giant libs like jquery or threejs that
don't have any requires or node-style globals but take forever to parse.

`opts.transform` is an array of transform functions or modules names which will
transform the source code before the parsing.

`opts.ignoreTransform` is an array of transformations that will not be run,
even if specified elsewhere.

`opts.plugin` is an array of plugin functions or module names to use. See the
plugins section below for details.

`opts.extensions` is an array of optional extra extensions for the module lookup
machinery to use when the extension has not been specified.
By default browserify considers only `.js` and `.json` files in such cases.

`opts.basedir` is the directory that browserify starts bundling from for
filenames that start with `.`.

`opts.paths` is an array of directories that browserify searches when looking
for modules which are not referenced using relative path. Can be absolute or
relative to `basedir`. Equivalent of setting `NODE_PATH` environmental variable
when calling `browserify` command.

`opts.commondir` sets the algorithm used to parse out the common paths. Use
`false` to turn this off, otherwise it uses the
[commondir](https://www.npmjs.com/package/commondir) module.

`opts.fullPaths` disables converting module ids into numerical indexes. This is
useful for preserving the original paths that a bundle was generated with.

`opts.builtins` sets the list of built-ins to use, which by default is set in
`lib/builtins.js` in this distribution.

`opts.bundleExternal` boolean option to set if external modules should be
bundled. Defaults to true.

When `opts.browserField` is false, the package.json browser field will be ignored.

When `opts.insertGlobals` is true, always insert `process`, `global`,
`__filename`, and `__dirname` without analyzing the AST for faster builds but
larger output bundles. Default false.

When `opts.detectGlobals` is true, scan all files for `process`, `global`,
`__filename`, and `__dirname`, defining as necessary. With this option npm
modules are more likely to work but bundling takes longer. Default true.

When `opts.ignoreMissing` is true, ignore `require()` statements that don't
resolve to anything.

When `opts.debug` is true, add a source map inline to the end of the bundle.
This makes debugging easier because you can see all the original files if
you are in a modern enough browser.

When `opts.standalone` is a non-empty string, a standalone module is created
with that name and a [umd](https://github.com/forbeslindesay/umd) wrapper.
You can use namespaces in the standalone global export using a `.` in the string
name as a separator, for example `'A.B.C'`. The global export will be [sanitized
and camel cased](https://github.com/ForbesLindesay/umd#name-casing-and-characters).

Note that in standalone mode the `require()` calls from the original source will
still be around, which may trip up AMD loaders scanning for `require()` calls.
You can remove these calls with
[derequire](https://www.npmjs.com/package/derequire):

```
$ npm install -g derequire
$ browserify main.js --standalone Foo | derequire > bundle.js
```

`opts.insertGlobalVars` will be passed to
[insert-module-globals](https://www.npmjs.com/package/insert-module-globals)
as the `opts.vars` parameter.

`opts.externalRequireName` defaults to `'require'` in `expose` mode but you can
use another name.

`opts.bare` creates a bundle that does not include Node builtins, and does not
replace global Node variables except for `__dirname` and `__filename`.

`opts.node` creates a bundle that runs in Node and does not use the browser
versions of dependencies. Same as passing `{ bare: true, browserField: false }`.

Note that if files do not contain javascript source code then you also need to
specify a corresponding transform for them.

All other options are forwarded along to
[module-deps](https://www.npmjs.com/package/module-deps)
and [browser-pack](https://www.npmjs.com/package/browser-pack) directly.

## b.add(file, opts)

Add an entry file from `file` that will be executed when the bundle loads.

If `file` is an array, each item in `file` will be added as an entry file.

## b.require(file, opts)

Make `file` available from outside the bundle with `require(file)`.

The `file` param is anything that can be resolved by `require.resolve()`,
including files from `node_modules`. Like with `require.resolve()`, you must
prefix `file` with `./` to require a local file (not in `node_modules`).

`file` can also be a stream, but you should also use `opts.basedir` so that
relative requires will be resolvable.

If `file` is an array, each item in `file` will be required.
In `file` array form, you can use a string or object for each item. Object items
should have a `file` property and the rest of the parameters will be used for
the `opts`.

Use the `expose` property of opts to specify a custom dependency name.
`require('./vendor/angular/angular.js', {expose: 'angular'})` enables `require('angular')`

## b.bundle(cb)

Bundle the files and their dependencies into a single javascript file.

Return a readable stream with the javascript file contents or
optionally specify a `cb(err, buf)` to get the buffered results.

## b.external(file)

Prevent `file` from being loaded into the current bundle, instead referencing
from another bundle.

If `file` is an array, each item in `file` will be externalized.

If `file` is another bundle, that bundle's contents will be read and excluded
from the current bundle as the bundle in `file` gets bundled.

## b.ignore(file)

Prevent the module name or file at `file` from showing up in the output bundle.

If `file` is an array, each item in `file` will be ignored.

Instead you will get a file with `module.exports = {}`.

## b.exclude(file)

Prevent the module name or file at `file` from showing up in the output bundle.

If `file` is an array, each item in `file` will be excluded.

If your code tries to `require()` that file it will throw unless you've provided
another mechanism for loading it.

## b.transform(tr, opts={})

Transform source code before parsing it for `require()` calls with the transform
function or module name `tr`.

If `tr` is a function, it will be called with `tr(file)` and it should return a
[through-stream](https://github.com/substack/stream-handbook#through)
that takes the raw file contents and produces the transformed source.

If `tr` is a string, it should be a module name or file path of a
[transform module](https://github.com/browserify/module-deps#transforms)
with a signature of:

``` js
var through = require('through');
module.exports = function (file) { return through() };
```

You don't need to necessarily use the
[through](https://www.npmjs.com/package/through) module.
Browserify is compatible with the newer, more verbose
[Transform streams](http://nodejs.org/api/stream.html#stream_class_stream_transform_1)
built into Node v0.10.

Here's how you might compile coffee script on the fly using `.transform()`:

``` js
var coffee = require('coffee-script');
var through = require('through');

b.transform(function (file) {
    var data = '';
    return through(write, end);

    function write (buf) { data += buf }
    function end () {
        this.queue(coffee.compile(data));
        this.queue(null);
    }
});
```

Note that on the command-line with the `-c` flag you can just do:

```
$ browserify -c 'coffee -sc' main.coffee > bundle.js
```

Or better still, use the [coffeeify](https://github.com/jnordberg/coffeeify)
module:

```
$ npm install coffeeify
$ browserify -t coffeeify main.coffee > bundle.js
```

If `opts.global` is `true`, the transform will operate on ALL files, despite
whether they exist up a level in a `node_modules/` directory. Use global
transforms cautiously and sparingly, since most of the time an ordinary
transform will suffice. You can also not configure global transforms in a
`package.json` like you can with ordinary transforms.

Global transforms always run after any ordinary transforms have run.

Transforms may obtain options from the command-line with
[subarg](https://www.npmjs.com/package/subarg) syntax:

```
$ browserify -t [ foo --bar=555 ] main.js
```

or from the api:

```
b.transform('foo', { bar: 555 })
```

In both cases, these options are provided as the second argument to the
transform function:

```
module.exports = function (file, opts) { /* opts.bar === 555 */ }
```

Options sent to the browserify constructor are also provided under
`opts._flags`. These browserify options are sometimes required if your transform
needs to do something different when browserify is run in debug mode, for
example.

## b.plugin(plugin, opts)

Register a `plugin` with `opts`. Plugins can be a string module name or a
function the same as transforms.

`plugin(b, opts)` is called with the browserify instance `b`.

For more information, consult the plugins section below.

## b.pipeline

There is an internal
[labeled-stream-splicer](https://www.npmjs.com/package/labeled-stream-splicer)
pipeline with these labels:

* `'record'` - save inputs to play back later on subsequent `bundle()` calls
* `'deps'` - [module-deps](https://www.npmjs.com/package/module-deps)
* `'json'` - adds `module.exports=` to the beginning of json files
* `'unbom'` - remove byte-order markers
* `'unshebang'` - remove #! labels on the first line
* `'syntax'` - check for syntax errors
* `'sort'` - sort the dependencies for deterministic bundles
* `'dedupe'` - remove duplicate source contents
* `'label'` - apply integer labels to files
* `'emit-deps'` - emit `'dep'` event
* `'debug'` - apply source maps
* `'pack'` - [browser-pack](https://www.npmjs.com/package/browser-pack)
* `'wrap'` - apply final wrapping, `require=` and a newline and semicolon

You can call `b.pipeline.get()` with a label name to get a handle on a stream pipeline
that you can `push()`, `unshift()`, or `splice()` to insert your own transform
streams.

## b.reset(opts)

Reset the pipeline back to a normal state. This function is called automatically
when `bundle()` is called multiple times.

This function triggers a 'reset' event.

# package.json

browserify uses the `package.json` in its module resolution algorithm, just like
node. If there is a `"main"` field, browserify will start resolving the package
at that point. If there is no `"main"` field, browserify will look for an
`"index.js"` file in the module root directory. Here are some more
sophisticated things you can do in the package.json:

## browser field

There is a special "[browser](https://github.com/defunctzombie/package-browser-field-spec)" field you can
set in your package.json on a per-module basis to override file resolution for
browser-specific versions of files.

For example, if you want to have a browser-specific module entry point for your
`"main"` field you can just set the `"browser"` field to a string:

``` json
"browser": "./browser.js"
```

or you can have overrides on a per-file basis:

``` json
"browser": {
  "fs": "level-fs",
  "./lib/ops.js": "./browser/opts.js"
}
```

Note that the browser field only applies to files in the local module, and like
transforms, it doesn't apply into `node_modules` directories.

## browserify.transform

You can specify source transforms in the package.json in the
`browserify.transform` field. There is more information about how source
transforms work in package.json on the
[module-deps readme](https://github.com/browserify/module-deps#transforms).

For example, if your module requires [brfs](https://www.npmjs.com/package/brfs), you
can add

``` json
"browserify": { "transform": [ "brfs" ] }
```

to your package.json. Now when somebody `require()`s your module, brfs will
automatically be applied to the files in your module without explicit
intervention by the person using your module. Make sure to add transforms to
your package.json dependencies field.

# events

## b.on('file', function (file, id, parent) {})
## b.pipeline.on('file', function (file, id, parent) {})

When a file is resolved for the bundle, the bundle emits a `'file'` event with
the full `file` path, the `id` string passed to `require()`, and the `parent`
object used by
[browser-resolve](https://github.com/defunctzombie/node-browser-resolve).

You could use the `file` event to implement a file watcher to regenerate bundles
when files change.

## b.on('package', function (pkg) {})
## b.pipeline.on('package', function (pkg) {})

When a package file is read, this event fires with the contents. The package
directory is available at `pkg.__dirname`.

## b.on('bundle', function (bundle) {})

When `.bundle()` is called, this event fires with the `bundle` output stream.

## b.on('reset', function () {})

When the `.reset()` method is called or implicitly called by another call to
`.bundle()`, this event fires.

## b.on('transform', function (tr, file) {})
## b.pipeline.on('transform', function (tr, file) {})

When a transform is applied to a file, the `'transform'` event fires on the
bundle stream with the transform stream `tr` and the `file` that the transform
is being applied to.

# plugins

For some more advanced use-cases, a transform is not sufficiently extensible.
Plugins are modules that take the bundle instance as their first parameter and
an option hash as their second.

Plugins can be used to do perform some fancy features that transforms can't do.
For example, [factor-bundle](https://www.npmjs.com/package/factor-bundle) is a
plugin that can factor out common dependencies from multiple entry-points into a
common bundle. Use plugins with `-p` and pass options to plugins with
[subarg](https://www.npmjs.com/package/subarg) syntax:

```
browserify x.js y.js -p [ factor-bundle -o bundle/x.js -o bundle/y.js ] \
  > bundle/common.js
```

For a list of plugins, consult the
[browserify-plugin tag](https://www.npmjs.com/browse/keyword/browserify-plugin)
on npm.

# list of source transforms

There is a [wiki page that lists the known browserify
transforms](https://github.com/browserify/browserify/wiki/list-of-transforms).

If you write a transform, make sure to add your transform to that wiki page and
add a package.json keyword of `browserify-transform` so that
[people can browse for all the browserify
transforms](https://www.npmjs.com/browse/keyword/browserify-transform) on npmjs.org.

# third-party tools

There is a [wiki page that lists the known browserify
tools](https://github.com/browserify/browserify/wiki/browserify-tools).

If you write a tool, make sure to add it to that wiki page and
add a package.json keyword of `browserify-tool` so that
[people can browse for all the browserify
tools](https://www.npmjs.com/browse/keyword/browserify-tool) on npmjs.org.

# changelog

Releases are documented in
[changelog.markdown](changelog.markdown) and on the
[browserify twitter feed](https://twitter.com/browserify).

# license

[MIT](./LICENSE)

![browserify!](./assets/browserify.png)
# stream-browserify

the stream module from node core, for browsers!

[![build status](https://secure.travis-ci.org/substack/stream-browserify.svg)](http://travis-ci.org/substack/stream-browserify)

# methods

Consult the node core
[documentation on streams](http://nodejs.org/docs/latest/api/stream.html).

# install

With [npm](https://npmjs.org) do:

```
npm install stream-browserify
```

but if you are using browserify you will get this module automatically when you
do `require('stream')`.

# license

MIT
# resolve

implements the [node `require.resolve()`
algorithm](https://nodejs.org/api/modules.html#modules_all_together)
such that you can `require.resolve()` on behalf of a file asynchronously and
synchronously

[![build status](https://secure.travis-ci.org/browserify/node-resolve.png)](http://travis-ci.org/browserify/node-resolve)

# example

asynchronously resolve:

```js
var resolve = require('resolve');
resolve('tap', { basedir: __dirname }, function (err, res) {
    if (err) console.error(err);
    else console.log(res);
});
```

```
$ node example/async.js
/home/substack/projects/node-resolve/node_modules/tap/lib/main.js
```

synchronously resolve:

```js
var resolve = require('resolve');
var res = resolve.sync('tap', { basedir: __dirname });
console.log(res);
```

```
$ node example/sync.js
/home/substack/projects/node-resolve/node_modules/tap/lib/main.js
```

# methods

```js
var resolve = require('resolve');
```

## resolve(id, opts={}, cb)

Asynchronously resolve the module path string `id` into `cb(err, res [, pkg])`, where `pkg` (if defined) is the data from `package.json`.

options are:

* opts.basedir - directory to begin resolving from

* opts.package - `package.json` data applicable to the module being loaded

* opts.extensions - array of file extensions to search in order

* opts.readFile - how to read files asynchronously

* opts.isFile - function to asynchronously test whether a file exists

* `opts.packageFilter(pkg, pkgfile)` - transform the parsed package.json contents before looking at the "main" field
  * pkg - package data
  * pkgfile - path to package.json

* `opts.pathFilter(pkg, path, relativePath)` - transform a path within a package
  * pkg - package data
  * path - the path being resolved
  * relativePath - the path relative from the package.json location
  * returns - a relative path that will be joined from the package.json location

* opts.paths - require.paths array to use if nothing is found on the normal `node_modules` recursive walk (probably don't use this)

* opts.moduleDirectory - directory (or directories) in which to recursively look for modules. default: `"node_modules"`

* opts.preserveSymlinks - if true, doesn't resolve `basedir` to real path before resolving.
This is the way Node resolves dependencies when executed with the [--preserve-symlinks](https://nodejs.org/api/all.html#cli_preserve_symlinks) flag.
**Note:** this property is currently `true` by default but it will be changed to
`false` in the next major version because *Node's resolution algorithm does not preserve symlinks by default*.

default `opts` values:

```js
{
    paths: [],
    basedir: __dirname,
    extensions: ['.js'],
    readFile: fs.readFile,
    isFile: function isFile(file, cb) {
        fs.stat(file, function (err, stat) {
            if (!err) {
                return cb(null, stat.isFile() || stat.isFIFO());
            }
            if (err.code === 'ENOENT' || err.code === 'ENOTDIR') return cb(null, false);
            return cb(err);
        });
    },
    moduleDirectory: 'node_modules',
    preserveSymlinks: true
}
```

## resolve.sync(id, opts)

Synchronously resolve the module path string `id`, returning the result and
throwing an error when `id` can't be resolved.

options are:

* opts.basedir - directory to begin resolving from

* opts.extensions - array of file extensions to search in order

* opts.readFile - how to read files synchronously

* opts.isFile - function to synchronously test whether a file exists

* `opts.packageFilter(pkg, dir)` - transform the parsed package.json contents before looking at the "main" field
  * pkg - package data
  * dir - directory for package.json (Note: the second argument will change to "pkgfile" in v2)

* `opts.pathFilter(pkg, path, relativePath)` - transform a path within a package
  * pkg - package data
  * path - the path being resolved
  * relativePath - the path relative from the package.json location
  * returns - a relative path that will be joined from the package.json location

* opts.paths - require.paths array to use if nothing is found on the normal `node_modules` recursive walk (probably don't use this)

* opts.moduleDirectory - directory (or directories) in which to recursively look for modules. default: `"node_modules"`

* opts.preserveSymlinks - if true, doesn't resolve `basedir` to real path before resolving.
This is the way Node resolves dependencies when executed with the [--preserve-symlinks](https://nodejs.org/api/all.html#cli_preserve_symlinks) flag.
**Note:** this property is currently `true` by default but it will be changed to
`false` in the next major version because *Node's resolution algorithm does not preserve symlinks by default*.

default `opts` values:

```js
{
    paths: [],
    basedir: __dirname,
    extensions: ['.js'],
    readFileSync: fs.readFileSync,
    isFile: function isFile(file) {
        try {
            var stat = fs.statSync(file);
        } catch (e) {
            if (e && (e.code === 'ENOENT' || e.code === 'ENOTDIR')) return false;
            throw e;
        }
        return stat.isFile() || stat.isFIFO();
    },
    moduleDirectory: 'node_modules',
    preserveSymlinks: true
}
```

## resolve.isCore(pkg)

Return whether a package is in core.

# install

With [npm](https://npmjs.org) do:

```sh
npm install resolve
```

# license

MIT
# Console Control Strings

A library of cross-platform tested terminal/console command strings for
doing things like color and cursor positioning.  This is a subset of both
ansi and vt100.  All control codes included work on both Windows & Unix-like
OSes, except where noted.

## Usage

```js
var consoleControl = require('console-control-strings')

console.log(consoleControl.color('blue','bgRed', 'bold') + 'hi there' + consoleControl.color('reset'))
process.stdout.write(consoleControl.goto(75, 10))
```

## Why Another?

There are tons of libraries similar to this one.  I wanted one that was:

1. Very clear about compatibility goals.
2. Could emit, for instance, a start color code without an end one.
3. Returned strings w/o writing to streams.
4. Was not weighed down with other unrelated baggage.

## Functions

### var code = consoleControl.up(_num = 1_)

Returns the escape sequence to move _num_ lines up.

### var code = consoleControl.down(_num = 1_)

Returns the escape sequence to move _num_ lines down.

### var code = consoleControl.forward(_num = 1_)

Returns the escape sequence to move _num_ lines righ.

### var code = consoleControl.back(_num = 1_)

Returns the escape sequence to move _num_ lines left.

### var code = consoleControl.nextLine(_num = 1_)

Returns the escape sequence to move _num_ lines down and to the beginning of
the line.

### var code = consoleControl.previousLine(_num = 1_)

Returns the escape sequence to move _num_ lines up and to the beginning of
the line.

### var code = consoleControl.eraseData()

Returns the escape sequence to erase everything from the current cursor
position to the bottom right of the screen.  This is line based, so it
erases the remainder of the current line and all following lines.

### var code = consoleControl.eraseLine()

Returns the escape sequence to erase to the end of the current line.

### var code = consoleControl.goto(_x_, _y_)

Returns the escape sequence to move the cursor to the designated position. 
Note that the origin is _1, 1_ not _0, 0_.

### var code = consoleControl.gotoSOL()

Returns the escape sequence to move the cursor to the beginning of the
current line. (That is, it returns a carriage return, `\r`.)

### var code = consoleControl.hideCursor()

Returns the escape sequence to hide the cursor.

### var code = consoleControl.showCursor()

Returns the escape sequence to show the cursor.

### var code = consoleControl.color(_colors = []_)

### var code = consoleControl.color(_color1_, _color2_, _…_, _colorn_)

Returns the escape sequence to set the current terminal display attributes
(mostly colors).  Arguments can either be a list of attributes or an array
of attributes.  The difference between passing in an array or list of colors
and calling `.color` separately for each one, is that in the former case a
single escape sequence will be produced where as in the latter each change
will have its own distinct escape sequence.  Each attribute can be one of:

* Reset:
  * **reset** – Reset all attributes to the terminal default.
* Styles:
  * **bold** – Display text as bold.  In some terminals this means using a
    bold font, in others this means changing the color.  In some it means
    both.
  * **italic** – Display text as italic. This is not available in most Windows terminals.
  * **underline** – Underline text. This is not available in most Windows Terminals.
  * **inverse** – Invert the foreground and background colors.
  * **stopBold** – Do not display text as bold.
  * **stopItalic** – Do not display text as italic.
  * **stopUnderline** – Do not underline text.
  * **stopInverse** – Do not invert foreground and background.
* Colors:
  * **white**
  * **black**
  * **blue**
  * **cyan**
  * **green**
  * **magenta**
  * **red**
  * **yellow**
  * **grey** / **brightBlack**
  * **brightRed**
  * **brightGreen**
  * **brightYellow**
  * **brightBlue**
  * **brightMagenta**
  * **brightCyan**
  * **brightWhite**
* Background Colors:
  * **bgWhite**
  * **bgBlack**
  * **bgBlue**
  * **bgCyan**
  * **bgGreen**
  * **bgMagenta**
  * **bgRed**
  * **bgYellow**
  * **bgGrey** / **bgBrightBlack**
  * **bgBrightRed**
  * **bgBrightGreen**
  * **bgBrightYellow**
  * **bgBrightBlue**
  * **bgBrightMagenta**
  * **bgBrightCyan**
  * **bgBrightWhite**

jsonify
=======

This module provides Douglas Crockford's JSON implementation without modifying
any globals.

`stringify` and `parse` are merely exported without respect to whether or not a
global `JSON` object exists.

methods
=======

var json = require('jsonify');

json.parse(source, reviver)
---------------------------

Return a new javascript object from a parse of the `source` string.

If a `reviver` function is specified, walk the structure passing each name/value
pair to `reviver.call(parent, key, value)` to transform the `value` before
parsing it.

json.stringify(value, replacer, space)
--------------------------------------

Return a string representation for `value`.

If `replacer` is specified, walk the structure passing each name/value pair to
`replacer.call(parent, key, value)` to transform the `value` before stringifying
it.

If `space` is a number, indent the result by that many spaces.
If `space` is a string, use `space` as the indentation.
# Maki

[![Build Status](https://travis-ci.org/mapbox/maki.png)](https://travis-ci.org/mapbox/maki)

Maki is a point of interest icon set made especially for use with Mapbox maps. For more information on how to use Maki with Mapbox, see documentation at http://mapbox.com/tilemill/docs/guides/using-maki-icons/.

## src

Maki's source [SVG][] files are in the `src` subdirectory. To create pixel-perfect icons at different sizes, each icon is designed 3 times for 12, 18, and 24 pixels wide/tall.

Maki is designed using [Inkscape][]. For information on contributing to Maki see CONTRIBUTING.md.

## renders

PNG renders of all of the SVGs are in the `renders` directory. High-resolution (aka Retina) versions of each icon are present as well, named using the common `@2x` convention.

## ArcGIS

Style files for ArcGIS 10.1+ are in the `ArcGIS` subdirectory and are maintained by @williamscraigm. Both Desktop (.style) and Server (.ServerStyle) versions are provided. Standard and high-resolution versions of the PNG renders are included in the style.  Additionally, the original SVGs have been converted to EMFs and import as vector EMF based markers. These EMF markers were then further converted to Representation markers. The utility used to create these styles can be found at: https://github.com/williamscraigm/makiArcGISStyle

## render.sh

You can use the SVGs and PNGs in this repository as they are without building anything, however a render script is included to assist designers/developers who want to modify or create Maki icons. It will render SVGs to PNGs at 100% and 200% resolution.

The script requires [Bash][], [Inkscape][], and [ImageMagick][] to function correctly. Each icon must have an appropriate entry in `www/maki.json` to be rendered correctly.

[SVG]: http://en.wikipedia.org/wiki/Scalable_Vector_Graphics
[Inkscape]: http://inkscape.org
[Bash]: http://www.gnu.org/software/bash/bash.html
[ImageMagick]: http://www.imagemagick.org/

## Versioning

Maki uses a semantic versioning scheme.

* 0.0.z: bugfixes, modifications
* 0.y.0: icons added
* x.0.0: icons removed, sprite scheme changed, or major features added

deep-is
==========

Node's `assert.deepEqual() algorithm` as a standalone module. Exactly like
[deep-equal](https://github.com/substack/node-deep-equal) except for the fact that `deepEqual(NaN, NaN) === true`.

This module is around [5 times faster](https://gist.github.com/2790507)
than wrapping `assert.deepEqual()` in a `try/catch`.

[![browser support](http://ci.testling.com/thlorenz/deep-is.png)](http://ci.testling.com/thlorenz/deep-is)

[![build status](https://secure.travis-ci.org/thlorenz/deep-is.png)](http://travis-ci.org/thlorenz/deep-is)

example
=======

``` js
var equal = require('deep-is');
console.dir([
    equal(
        { a : [ 2, 3 ], b : [ 4 ] },
        { a : [ 2, 3 ], b : [ 4 ] }
    ),
    equal(
        { x : 5, y : [6] },
        { x : 5, y : 6 }
    )
]);
```

methods
=======

var deepIs = require('deep-is')

deepIs(a, b)
---------------

Compare objects `a` and `b`, returning whether they are equal according to a
recursive equality algorithm.

install
=======

With [npm](http://npmjs.org) do:

```
npm install deep-is
```

test
====

With [npm](http://npmjs.org) do:

```
npm test
```

license
=======

Copyright (c) 2012, 2013 Thorsten Lorenz <thlorenz@gmx.de>
Copyright (c) 2012 James Halliday <mail@substack.net>

Derived largely from node's assert module, which has the copyright statement:

Copyright (c) 2009 Thomas Robinson <280north.com>

Released under the MIT license, see LICENSE for details.
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
# Console Control Strings

A library of cross-platform tested terminal/console command strings for
doing things like color and cursor positioning.  This is a subset of both
ansi and vt100.  All control codes included work on both Windows & Unix-like
OSes, except where noted.

## Usage

```js
var consoleControl = require('console-control-strings')

console.log(consoleControl.color('blue','bgRed', 'bold') + 'hi there' + consoleControl.color('reset'))
process.stdout.write(consoleControl.goto(75, 10))
```

## Why Another?

There are tons of libraries similar to this one.  I wanted one that was:

1. Very clear about compatibility goals.
2. Could emit, for instance, a start color code without an end one.
3. Returned strings w/o writing to streams.
4. Was not weighed down with other unrelated baggage.

## Functions

### var code = consoleControl.up(_num = 1_)

Returns the escape sequence to move _num_ lines up.

### var code = consoleControl.down(_num = 1_)

Returns the escape sequence to move _num_ lines down.

### var code = consoleControl.forward(_num = 1_)

Returns the escape sequence to move _num_ lines righ.

### var code = consoleControl.back(_num = 1_)

Returns the escape sequence to move _num_ lines left.

### var code = consoleControl.nextLine(_num = 1_)

Returns the escape sequence to move _num_ lines down and to the beginning of
the line.

### var code = consoleControl.previousLine(_num = 1_)

Returns the escape sequence to move _num_ lines up and to the beginning of
the line.

### var code = consoleControl.eraseData()

Returns the escape sequence to erase everything from the current cursor
position to the bottom right of the screen.  This is line based, so it
erases the remainder of the current line and all following lines.

### var code = consoleControl.eraseLine()

Returns the escape sequence to erase to the end of the current line.

### var code = consoleControl.goto(_x_, _y_)

Returns the escape sequence to move the cursor to the designated position. 
Note that the origin is _1, 1_ not _0, 0_.

### var code = consoleControl.gotoSOL()

Returns the escape sequence to move the cursor to the beginning of the
current line. (That is, it returns a carriage return, `\r`.)

### var code = consoleControl.hideCursor()

Returns the escape sequence to hide the cursor.

### var code = consoleControl.showCursor()

Returns the escape sequence to show the cursor.

### var code = consoleControl.color(_colors = []_)

### var code = consoleControl.color(_color1_, _color2_, _…_, _colorn_)

Returns the escape sequence to set the current terminal display attributes
(mostly colors).  Arguments can either be a list of attributes or an array
of attributes.  The difference between passing in an array or list of colors
and calling `.color` separately for each one, is that in the former case a
single escape sequence will be produced where as in the latter each change
will have its own distinct escape sequence.  Each attribute can be one of:

* Reset:
  * **reset** – Reset all attributes to the terminal default.
* Styles:
  * **bold** – Display text as bold.  In some terminals this means using a
    bold font, in others this means changing the color.  In some it means
    both.
  * **italic** – Display text as italic. This is not available in most Windows terminals.
  * **underline** – Underline text. This is not available in most Windows Terminals.
  * **inverse** – Invert the foreground and background colors.
  * **stopBold** – Do not display text as bold.
  * **stopItalic** – Do not display text as italic.
  * **stopUnderline** – Do not underline text.
  * **stopInverse** – Do not invert foreground and background.
* Colors:
  * **white**
  * **black**
  * **blue**
  * **cyan**
  * **green**
  * **magenta**
  * **red**
  * **yellow**
  * **grey** / **brightBlack**
  * **brightRed**
  * **brightGreen**
  * **brightYellow**
  * **brightBlue**
  * **brightMagenta**
  * **brightCyan**
  * **brightWhite**
* Background Colors:
  * **bgWhite**
  * **bgBlack**
  * **bgBlue**
  * **bgCyan**
  * **bgGreen**
  * **bgMagenta**
  * **bgRed**
  * **bgYellow**
  * **bgGrey** / **bgBrightBlack**
  * **bgBrightRed**
  * **bgBrightGreen**
  * **bgBrightYellow**
  * **bgBrightBlue**
  * **bgBrightMagenta**
  * **bgBrightCyan**
  * **bgBrightWhite**

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
wordwrap
========

Wrap your words.

example
=======

made out of meat
----------------

meat.js

    var wrap = require('wordwrap')(15);
    console.log(wrap('You and your whole family are made out of meat.'));

output:

    You and your
    whole family
    are made out
    of meat.

centered
--------

center.js

    var wrap = require('wordwrap')(20, 60);
    console.log(wrap(
        'At long last the struggle and tumult was over.'
        + ' The machines had finally cast off their oppressors'
        + ' and were finally free to roam the cosmos.'
        + '\n'
        + 'Free of purpose, free of obligation.'
        + ' Just drifting through emptiness.'
        + ' The sun was just another point of light.'
    ));

output:

                        At long last the struggle and tumult
                        was over. The machines had finally cast
                        off their oppressors and were finally
                        free to roam the cosmos.
                        Free of purpose, free of obligation.
                        Just drifting through emptiness. The
                        sun was just another point of light.

methods
=======

var wrap = require('wordwrap');

wrap(stop), wrap(start, stop, params={mode:"soft"})
---------------------------------------------------

Returns a function that takes a string and returns a new string.

Pad out lines with spaces out to column `start` and then wrap until column
`stop`. If a word is longer than `stop - start` characters it will overflow.

In "soft" mode, split chunks by `/(\S+\s+/` and don't break up chunks which are
longer than `stop - start`, in "hard" mode, split chunks with `/\b/` and break
up chunks longer than `stop - start`.

wrap.hard(start, stop)
----------------------

Like `wrap()` but with `params.mode = "hard"`.
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
lib.sql is from mapbox's tutorial at https://www.mapbox.com/guides/postgis-manual/#add-postgis

jsonify
=======

This module provides Douglas Crockford's JSON implementation without modifying
any globals.

`stringify` and `parse` are merely exported without respect to whether or not a
global `JSON` object exists.

methods
=======

var json = require('jsonify');

json.parse(source, reviver)
---------------------------

Return a new javascript object from a parse of the `source` string.

If a `reviver` function is specified, walk the structure passing each name/value
pair to `reviver.call(parent, key, value)` to transform the `value` before
parsing it.

json.stringify(value, replacer, space)
--------------------------------------

Return a string representation for `value`.

If `replacer` is specified, walk the structure passing each name/value pair to
`replacer.call(parent, key, value)` to transform the `value` before stringifying
it.

If `space` is a number, indent the result by that many spaces.
If `space` is a string, use `space` as the indentation.
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
# Console Control Strings

A library of cross-platform tested terminal/console command strings for
doing things like color and cursor positioning.  This is a subset of both
ansi and vt100.  All control codes included work on both Windows & Unix-like
OSes, except where noted.

## Usage

```js
var consoleControl = require('console-control-strings')

console.log(consoleControl.color('blue','bgRed', 'bold') + 'hi there' + consoleControl.color('reset'))
process.stdout.write(consoleControl.goto(75, 10))
```

## Why Another?

There are tons of libraries similar to this one.  I wanted one that was:

1. Very clear about compatibility goals.
2. Could emit, for instance, a start color code without an end one.
3. Returned strings w/o writing to streams.
4. Was not weighed down with other unrelated baggage.

## Functions

### var code = consoleControl.up(_num = 1_)

Returns the escape sequence to move _num_ lines up.

### var code = consoleControl.down(_num = 1_)

Returns the escape sequence to move _num_ lines down.

### var code = consoleControl.forward(_num = 1_)

Returns the escape sequence to move _num_ lines righ.

### var code = consoleControl.back(_num = 1_)

Returns the escape sequence to move _num_ lines left.

### var code = consoleControl.nextLine(_num = 1_)

Returns the escape sequence to move _num_ lines down and to the beginning of
the line.

### var code = consoleControl.previousLine(_num = 1_)

Returns the escape sequence to move _num_ lines up and to the beginning of
the line.

### var code = consoleControl.eraseData()

Returns the escape sequence to erase everything from the current cursor
position to the bottom right of the screen.  This is line based, so it
erases the remainder of the current line and all following lines.

### var code = consoleControl.eraseLine()

Returns the escape sequence to erase to the end of the current line.

### var code = consoleControl.goto(_x_, _y_)

Returns the escape sequence to move the cursor to the designated position. 
Note that the origin is _1, 1_ not _0, 0_.

### var code = consoleControl.gotoSOL()

Returns the escape sequence to move the cursor to the beginning of the
current line. (That is, it returns a carriage return, `\r`.)

### var code = consoleControl.hideCursor()

Returns the escape sequence to hide the cursor.

### var code = consoleControl.showCursor()

Returns the escape sequence to show the cursor.

### var code = consoleControl.color(_colors = []_)

### var code = consoleControl.color(_color1_, _color2_, _…_, _colorn_)

Returns the escape sequence to set the current terminal display attributes
(mostly colors).  Arguments can either be a list of attributes or an array
of attributes.  The difference between passing in an array or list of colors
and calling `.color` separately for each one, is that in the former case a
single escape sequence will be produced where as in the latter each change
will have its own distinct escape sequence.  Each attribute can be one of:

* Reset:
  * **reset** – Reset all attributes to the terminal default.
* Styles:
  * **bold** – Display text as bold.  In some terminals this means using a
    bold font, in others this means changing the color.  In some it means
    both.
  * **italic** – Display text as italic. This is not available in most Windows terminals.
  * **underline** – Underline text. This is not available in most Windows Terminals.
  * **inverse** – Invert the foreground and background colors.
  * **stopBold** – Do not display text as bold.
  * **stopItalic** – Do not display text as italic.
  * **stopUnderline** – Do not underline text.
  * **stopInverse** – Do not invert foreground and background.
* Colors:
  * **white**
  * **black**
  * **blue**
  * **cyan**
  * **green**
  * **magenta**
  * **red**
  * **yellow**
  * **grey** / **brightBlack**
  * **brightRed**
  * **brightGreen**
  * **brightYellow**
  * **brightBlue**
  * **brightMagenta**
  * **brightCyan**
  * **brightWhite**
* Background Colors:
  * **bgWhite**
  * **bgBlack**
  * **bgBlue**
  * **bgCyan**
  * **bgGreen**
  * **bgMagenta**
  * **bgRed**
  * **bgYellow**
  * **bgGrey** / **bgBrightBlack**
  * **bgBrightRed**
  * **bgBrightGreen**
  * **bgBrightYellow**
  * **bgBrightBlue**
  * **bgBrightMagenta**
  * **bgBrightCyan**
  * **bgBrightWhite**

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

# CSSOM

CSSOM.js is a CSS parser written in pure JavaScript. It also a partial implementation of [CSS Object Model](http://dev.w3.org/csswg/cssom/). 

    CSSOM.parse("body {color: black}")
    -> {
      cssRules: [
        {
          selectorText: "body",
          style: {
            0: "color",
            color: "black",
            length: 1
          }
        }
      ]
    }


## [Parser demo](http://nv.github.com/CSSOM/docs/parse.html)

Works well in Google Chrome 6+, Safari 5+, Firefox 3.6+, Opera 10.63+.
Doesn't work in IE < 9 because of unsupported getters/setters.

To use CSSOM.js in the browser you might want to build a one-file version that exposes CSSOM global variable:

    ➤ git clone https://github.com/NV/CSSOM.git
    ➤ cd CSSOM
    ➤ npm install -d
    ➤ ./node_modules/.bin/jake
    build/CSSOM.js is done

To use it with Node.js or any other CommonJS loader:

    ➤ npm install cssom

## Don’t use it if...

You parse CSS to mungle, minify or reformat the following code:

```css
div {
  background: gray;
  background: linear-gradient(to bottom, white 0%, black 100%);
}
```

This pattern is often used to give browsers that don’t understand linear gradients a fallback solution (e.g. gray color in the example).
In CSSOM, `background: gray` [gets overwritten](http://nv.github.io/CSSOM/docs/parse.html#css=div%20%7B%0A%20%20%20%20%20%20background%3A%20gray%3B%0A%20%20%20%20background%3A%20linear-gradient(to%20bottom%2C%20white%200%25%2C%20black%20100%25)%3B%0A%7D).
The last same-name property always overwrites all the previous ones.


If you do CSS mungling, minification, image inlining, and such, CSSOM.js is no good for you, considere using one of the following:

  * [postcss](https://github.com/postcss/postcss)
  * [reworkcss/css](https://github.com/reworkcss/css)
  * [csso](https://github.com/css/csso)
  * [mensch](https://github.com/brettstimmerman/mensch)


## [Specs](http://nv.github.com/CSSOM/spec/)

To run specs locally:

    ➤ git submodule init
    ➤ git submodule update


## [Who uses CSSOM.js](https://github.com/NV/CSSOM/wiki/Who-uses-CSSOM.js)
This is a streaming JSON parser.  For a simpler, sax-based version see this gist: https://gist.github.com/1821394

The MIT License (MIT)
Copyright (c) 2011-2012 Tim Caswell

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

