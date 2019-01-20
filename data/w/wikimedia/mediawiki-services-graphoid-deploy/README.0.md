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
# static-eval

evaluate statically-analyzable expressions

[![testling badge](https://ci.testling.com/substack/static-eval.png)](https://ci.testling.com/substack/static-eval)

[![build status](https://secure.travis-ci.org/substack/static-eval.png)](http://travis-ci.org/substack/static-eval)

# example

``` js
var evaluate = require('static-eval');
var parse = require('esprima').parse;

var src = process.argv[2];
var ast = parse(src).body[0].expression;

console.log(evaluate(ast));
```

If you stick to simple expressions, the result is statically analyzable:

```
$ node '7*8+9'
65
$ node eval.js '[1,2,3+4*5-(5*11)]'
[ 1, 2, -32 ]
```

but if you use statements, undeclared identifiers, or syntax, the result is no
longer statically analyzable and `evaluate()` returns `undefined`:

```
$ node eval.js '1+2+3*n'
undefined
$ node eval.js 'x=5; x*2'
undefined
$ node eval.js '5-4*3'
-7
```

You can also declare variables and functions to use in the static evaluation:

``` js
var evaluate = require('static-eval');
var parse = require('esprima').parse;

var src = '[1,2,3+4*10+n,foo(3+5),obj[""+"x"].y]';
var ast = parse(src).body[0].expression;

console.log(evaluate(ast, {
    n: 6,
    foo: function (x) { return x * 100 },
    obj: { x: { y: 555 } }
}));
```

# methods

``` js
var evaluate = require('static-eval');
```

## evaluate(ast, vars={})

Evaluate the [esprima](https://npmjs.org/package/esprima)-parsed abstract syntax
tree object `ast` with an optional collection of variables `vars` to use in the
static expression resolution.

If the expression contained in `ast` can't be statically resolved, `evaluate()`
returns undefined.

# install

With [npm](https://npmjs.org) do:

```
npm install static-eval
```

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
optimist
========

Optimist is a node.js library for option parsing for people who hate option
parsing. More specifically, this module is for people who like all the --bells
and -whistlz of program usage but think optstrings are a waste of time.

With optimist, option parsing doesn't have to suck (as much).

[![build status](https://secure.travis-ci.org/substack/node-optimist.png)](http://travis-ci.org/substack/node-optimist)

examples
========

With Optimist, the options are just a hash! No optstrings attached.
-------------------------------------------------------------------

xup.js:

````javascript
#!/usr/bin/env node
var argv = require('optimist').argv;

if (argv.rif - 5 * argv.xup > 7.138) {
    console.log('Buy more riffiwobbles');
}
else {
    console.log('Sell the xupptumblers');
}
````

***

    $ ./xup.js --rif=55 --xup=9.52
    Buy more riffiwobbles
    
    $ ./xup.js --rif 12 --xup 8.1
    Sell the xupptumblers

![This one's optimistic.](http://substack.net/images/optimistic.png)

But wait! There's more! You can do short options:
-------------------------------------------------
 
short.js:

````javascript
#!/usr/bin/env node
var argv = require('optimist').argv;
console.log('(%d,%d)', argv.x, argv.y);
````

***

    $ ./short.js -x 10 -y 21
    (10,21)

And booleans, both long and short (and grouped):
----------------------------------

bool.js:

````javascript
#!/usr/bin/env node
var util = require('util');
var argv = require('optimist').argv;

if (argv.s) {
    util.print(argv.fr ? 'Le chat dit: ' : 'The cat says: ');
}
console.log(
    (argv.fr ? 'miaou' : 'meow') + (argv.p ? '.' : '')
);
````

***

    $ ./bool.js -s
    The cat says: meow
    
    $ ./bool.js -sp
    The cat says: meow.

    $ ./bool.js -sp --fr
    Le chat dit: miaou.

And non-hypenated options too! Just use `argv._`!
-------------------------------------------------
 
nonopt.js:

````javascript
#!/usr/bin/env node
var argv = require('optimist').argv;
console.log('(%d,%d)', argv.x, argv.y);
console.log(argv._);
````

***

    $ ./nonopt.js -x 6.82 -y 3.35 moo
    (6.82,3.35)
    [ 'moo' ]
    
    $ ./nonopt.js foo -x 0.54 bar -y 1.12 baz
    (0.54,1.12)
    [ 'foo', 'bar', 'baz' ]

Plus, Optimist comes with .usage() and .demand()!
-------------------------------------------------

divide.js:

````javascript
#!/usr/bin/env node
var argv = require('optimist')
    .usage('Usage: $0 -x [num] -y [num]')
    .demand(['x','y'])
    .argv;

console.log(argv.x / argv.y);
````

***
 
    $ ./divide.js -x 55 -y 11
    5
    
    $ node ./divide.js -x 4.91 -z 2.51
    Usage: node ./divide.js -x [num] -y [num]

    Options:
      -x  [required]
      -y  [required]

    Missing required arguments: y

EVEN MORE HOLY COW
------------------

default_singles.js:

````javascript
#!/usr/bin/env node
var argv = require('optimist')
    .default('x', 10)
    .default('y', 10)
    .argv
;
console.log(argv.x + argv.y);
````

***

    $ ./default_singles.js -x 5
    15

default_hash.js:

````javascript
#!/usr/bin/env node
var argv = require('optimist')
    .default({ x : 10, y : 10 })
    .argv
;
console.log(argv.x + argv.y);
````

***

    $ ./default_hash.js -y 7
    17

And if you really want to get all descriptive about it...
---------------------------------------------------------

boolean_single.js

````javascript
#!/usr/bin/env node
var argv = require('optimist')
    .boolean('v')
    .argv
;
console.dir(argv);
````

***

    $ ./boolean_single.js -v foo bar baz
    true
    [ 'bar', 'baz', 'foo' ]

boolean_double.js

````javascript
#!/usr/bin/env node
var argv = require('optimist')
    .boolean(['x','y','z'])
    .argv
;
console.dir([ argv.x, argv.y, argv.z ]);
console.dir(argv._);
````

***

    $ ./boolean_double.js -x -z one two three
    [ true, false, true ]
    [ 'one', 'two', 'three' ]

Optimist is here to help...
---------------------------

You can describe parameters for help messages and set aliases. Optimist figures
out how to format a handy help string automatically.

line_count.js

````javascript
#!/usr/bin/env node
var argv = require('optimist')
    .usage('Count the lines in a file.\nUsage: $0')
    .demand('f')
    .alias('f', 'file')
    .describe('f', 'Load a file')
    .argv
;

var fs = require('fs');
var s = fs.createReadStream(argv.file);

var lines = 0;
s.on('data', function (buf) {
    lines += buf.toString().match(/\n/g).length;
});

s.on('end', function () {
    console.log(lines);
});
````

***

    $ node line_count.js
    Count the lines in a file.
    Usage: node ./line_count.js

    Options:
      -f, --file  Load a file  [required]

    Missing required arguments: f

    $ node line_count.js --file line_count.js 
    20
    
    $ node line_count.js -f line_count.js 
    20

methods
=======

By itself,

````javascript
require('optimist').argv
`````

will use `process.argv` array to construct the `argv` object.

You can pass in the `process.argv` yourself:

````javascript
require('optimist')([ '-x', '1', '-y', '2' ]).argv
````

or use .parse() to do the same thing:

````javascript
require('optimist').parse([ '-x', '1', '-y', '2' ])
````

The rest of these methods below come in just before the terminating `.argv`.

.alias(key, alias)
------------------

Set key names as equivalent such that updates to a key will propagate to aliases
and vice-versa.

Optionally `.alias()` can take an object that maps keys to aliases.

.default(key, value)
--------------------

Set `argv[key]` to `value` if no option was specified on `process.argv`.

Optionally `.default()` can take an object that maps keys to default values.

.demand(key)
------------

If `key` is a string, show the usage information and exit if `key` wasn't
specified in `process.argv`.

If `key` is a number, demand at least as many non-option arguments, which show
up in `argv._`.

If `key` is an Array, demand each element.

.describe(key, desc)
--------------------

Describe a `key` for the generated usage information.

Optionally `.describe()` can take an object that maps keys to descriptions.

.options(key, opt)
------------------

Instead of chaining together `.alias().demand().default()`, you can specify
keys in `opt` for each of the chainable methods.

For example:

````javascript
var argv = require('optimist')
    .options('f', {
        alias : 'file',
        default : '/etc/passwd',
    })
    .argv
;
````

is the same as

````javascript
var argv = require('optimist')
    .alias('f', 'file')
    .default('f', '/etc/passwd')
    .argv
;
````

Optionally `.options()` can take an object that maps keys to `opt` parameters.

.usage(message)
---------------

Set a usage message to show which commands to use. Inside `message`, the string
`$0` will get interpolated to the current script name or node command for the
present script similar to how `$0` works in bash or perl.

.check(fn)
----------

Check that certain conditions are met in the provided arguments.

If `fn` throws or returns `false`, show the thrown error, usage information, and
exit.

.boolean(key)
-------------

Interpret `key` as a boolean. If a non-flag option follows `key` in
`process.argv`, that string won't get set as the value of `key`.

If `key` never shows up as a flag in `process.arguments`, `argv[key]` will be
`false`.

If `key` is an Array, interpret all the elements as booleans.

.string(key)
------------

Tell the parser logic not to interpret `key` as a number or boolean.
This can be useful if you need to preserve leading zeros in an input.

If `key` is an Array, interpret all the elements as strings.

.wrap(columns)
--------------

Format usage output to wrap at `columns` many columns.

.help()
-------

Return the generated usage string.

.showHelp(fn=console.error)
---------------------------

Print the usage data using `fn` for printing.

.parse(args)
------------

Parse `args` instead of `process.argv`. Returns the `argv` object.

.argv
-----

Get the arguments as a plain old object.

Arguments without a corresponding flag show up in the `argv._` array.

The script name or node command is available at `argv.$0` similarly to how `$0`
works in bash or perl.

parsing tricks
==============

stop parsing
------------

Use `--` to stop parsing flags and stuff the remainder into `argv._`.

    $ node examples/reflect.js -a 1 -b 2 -- -c 3 -d 4
    { _: [ '-c', '3', '-d', '4' ],
      '$0': 'node ./examples/reflect.js',
      a: 1,
      b: 2 }

negate fields
-------------

If you want to explicity set a field to false instead of just leaving it
undefined or to override a default you can do `--no-key`.

    $ node examples/reflect.js -a --no-b
    { _: [],
      '$0': 'node ./examples/reflect.js',
      a: true,
      b: false }

numbers
-------

Every argument that looks like a number (`!isNaN(Number(arg))`) is converted to
one. This way you can just `net.createConnection(argv.port)` and you can add
numbers out of `argv` with `+` without having that mean concatenation,
which is super frustrating.

duplicates
----------

If you specify a flag multiple times it will get turned into an array containing
all the values in order.

    $ node examples/reflect.js -x 5 -x 8 -x 0
    { _: [],
      '$0': 'node ./examples/reflect.js',
        x: [ 5, 8, 0 ] }

dot notation
------------

When you use dots (`.`s) in argument names, an implicit object path is assumed.
This lets you organize arguments into nested objects.

     $ node examples/reflect.js --foo.bar.baz=33 --foo.quux=5
     { _: [],
       '$0': 'node ./examples/reflect.js',
         foo: { bar: { baz: 33 }, quux: 5 } }

installation
============

With [npm](http://github.com/isaacs/npm), just do:
    npm install optimist
 
or clone this project on github:

    git clone http://github.com/substack/node-optimist.git

To run the tests with [expresso](http://github.com/visionmedia/expresso),
just do:
    
    expresso

inspired By
===========

This module is loosely inspired by Perl's
[Getopt::Casual](http://search.cpan.org/~photo/Getopt-Casual-0.13.1/Casual.pm).
# brfs

fs.readFileSync() and fs.readFile() static asset browserify transform

[![build status](https://secure.travis-ci.org/substack/brfs.png)](http://travis-ci.org/substack/brfs)

This module is a plugin for [browserify](http://browserify.org) to parse the AST
for `fs.readFileSync()` calls so that you can inline file contents into your
bundles.

Even though this module is intended for use with browserify, nothing about it is
particularly specific to browserify so it should be generally useful in other
projects.

# example

for a main.js:

``` js
var fs = require('fs');
var html = fs.readFileSync(__dirname + '/robot.html', 'utf8');
console.log(html);
```

and a robot.html:

``` html
<b>beep boop</b>
```

first `npm install brfs` into your project, then:

## on the command-line

```
$ browserify -t brfs example/main.js > bundle.js
```

now in the bundle output file,

``` js
var html = fs.readFileSync(__dirname + '/robot.html', 'utf8');
```

turns into:

``` js
var html = "<b>beep boop</b>\n";
```

## or with the api

``` js
var browserify = require('browserify');
var fs = require('fs');

var b = browserify('example/main.js');
b.transform('brfs');

b.bundle().pipe(fs.createWriteStream('bundle.js'));
```

## async

You can also use `fs.readFile()`:

``` js
var fs = require('fs');
fs.readFile(__dirname + '/robot.html', 'utf8', function (err, html) {
    console.log(html);
});
```

When you run this code through brfs, it turns into:

``` js
var fs = require('fs');
process.nextTick(function () {(function (err, html) {
    console.log(html);
})(null,"<b>beep boop</b>\n")});
```

# methods

brfs looks for:

* `fs.readFileSync(pathExpr, enc=null)`
* `fs.readFile(pathExpr, enc=null, cb)`
* `fs.readdirSync(pathExpr)`
* `fs.readdir(pathExpr, cb)`

Inside of each `pathExpr`, you can use
[statically analyzable](http://npmjs.org/package/static-eval) expressions and
these variables and functions:

* `__dirname`
* `__filename`
* `path` if you `var path = require('path')` first
* `require.resolve()`

Just like node, the default encoding is `null` and will give back a `Buffer`.
If you want differently-encoded file contents for your inline content you can
set `enc` to `'utf8'`, `'base64'`, or `'hex'`.

In async mode when a callback `cb` is given, the contents of `pathExpr` are
inlined into the source inside of a `process.nextTick()` call.

When you use a `'file'`-event aware watcher such as
[watchify](https://npmjs.org/package/watchify), the inlined assets will be
updated automatically.

If you want to use this plugin directly, not through browserify, the api
follows.

``` js
var brfs = require('brfs')
```

## var tr = brfs(file, opts)

Return a through stream `tr` inlining `fs.readFileSync()` file contents
in-place.

Optionally, you can set which `opts.vars` will be used in the
[static argument evaluation](https://npmjs.org/package/static-eval)
in addition to `__dirname` and `__filename`.

# events

## tr.on('file', function (file) {})

For every file included with `fs.readFileSync()` or `fs.readFile()`, the `tr`
instance emits a `'file'` event with the `file` path.

# usage

A tiny command-line program ships with this module to make debugging easier.

```
usage:

  brfs file
 
    Inline `fs.readFileSync()` calls from `file`, printing the transformed file
    contents to stdout.

  brfs
  brfs -
 
    Inline `fs.readFileSync()` calls from stdin, printing the transformed file
    contents to stdout.

```

# install

With [npm](https://npmjs.org) do:

```
npm install brfs
```

then use `-t brfs` with the browserify command or use `.transform('brfs')` from
the browserify api.

# gotchas

Since `brfs` evaluates your source code *statically*, you can't use dynamic expressions that need to be evaluated at run time. For example:

```js
// WILL NOT WORK!
var file = window.someFilePath;
var str = require('fs').readFileSync(file, 'utf8');
```

Instead, you must use simpler expressions that can be resolved at build-time:

```js
var str = require('fs').readFileSync(__dirname + '/file.txt', 'utf8');
```

Another gotcha: `brfs` does not yet support ES2015 syntax like destructuring or `import` statements. See [brfs-babel](https://github.com/Jam3/brfs-babel) for an experimental replacement that supports this syntax.

# license

MIT
# static-module

convert module usage to inline expressions

# example

Here's a simplified version of the [brfs](https://npmjs.org/package/brfs) module
using static-module.

brfs converts `fs.readFileSync(file)` calls to inline strings with the contents
of `file` included in-place.

``` js
var staticModule = require('static-module');
var quote = require('quote-stream');
var fs = require('fs');

var sm = staticModule({
    fs: {
        readFileSync: function (file) {
            return fs.createReadStream(file).pipe(quote());
        }
    }
}, { vars: { __dirname: __dirname + '/brfs' } });
process.stdin.pipe(sm).pipe(process.stdout);
```

input:

```
$ cat brfs/source.js
var fs = require('fs');
var src = fs.readFileSync(__dirname + '/x.txt');
console.log(src);
```

output:

```
$ node brfs.js < brfs/source.js 

var src = "beep boop\n";
console.log(src);
```

# methods

``` js
var staticModule = require('static-module')
```

## var sm = staticModule(modules, opts={})

Return a transform stream `sm` that transforms javascript source input to
javascript source output with each property in the `modules` object expanded in
inline form.

Properties in the `modules` object can be ordinary values that will be included
directly or functions that will be executed with the [statically
evaluated](https://npmjs.org/package/static-eval) arguments from the source
under an optional set of `opts.vars` variables.

Property functions can return streams, in which case their contents will be
piped directly into the source output.

Otherwise, the return values of functions will be inlined into the source in
place as strings.

Use `opts.varModules` to map whitelisted module names to definitions that can be
declared in client code with `var` and will appear in static expressions like
`opts.vars`.

For example, to make this code with `path.join()` work:

``` js
var fs = require('fs');
var path = require('path');
var src = fs.readFileSync(path.join(__dirname, 'x.txt'), 'utf8');
console.log(src);
```

you can do:

``` js
var staticModule = require('static-module');
var quote = require('quote-stream');
var fs = require('fs');

var sm = staticModule({
    fs: {
        readFileSync: function (file) {
            return fs.createReadStream(file).pipe(quote());
        }
    },
    varMods: { path: require('path') }
}, { vars: { __dirname: __dirname + '/brfs' } });
process.stdin.pipe(sm).pipe(process.stdout);
```

# install

With [npm](https://npmjs.org) do:

```
npm install static-module
```

# license

MIT
# quote-stream

transform a stream into a quoted string

[![testling badge](https://ci.testling.com/substack/quote-stream.png)](https://ci.testling.com/substack/quote-stream)

[![build status](https://secure.travis-ci.org/substack/quote-stream.png)](http://travis-ci.org/substack/quote-stream)

# example

``` js
var quote = require('quote-stream');
process.stdin.pipe(quote()).pipe(process.stdout);
```

output:

```
$ echo beep boop | node example/stream.js
"beep boop\n"
```

# methods

``` js
var quote = require('quote-stream')
```

## var q = quote()

Return a transform stream `q` that wraps input in double quotes and adds escape
characters to the chunks.

# usage

```
usage: quote-stream

  Transform stdin to a quoted string on stdout.

```

# install

With [npm](https://npmjs.org) do:

```
npm install quote-stream
```

# license

MIT
# object-inspect

string representations of objects in node and the browser

[![testling badge](https://ci.testling.com/substack/object-inspect.png)](https://ci.testling.com/substack/object-inspect)

[![build status](https://secure.travis-ci.org/substack/object-inspect.png)](http://travis-ci.org/substack/object-inspect)

# example

## circular

``` js
var inspect = require('object-inspect');
var obj = { a: 1, b: [3,4] };
obj.c = obj;
console.log(inspect(obj));
```

## dom element

``` js
var inspect = require('object-inspect');

var d = document.createElement('div');
d.setAttribute('id', 'beep');
d.innerHTML = '<b>wooo</b><i>iiiii</i>';

console.log(inspect([ d, { a: 3, b : 4, c: [5,6,[7,[8,[9]]]] } ]));
```

output:

```
[ <div id="beep">...</div>, { a: 3, b: 4, c: [ 5, 6, [ 7, [ 8, [ ... ] ] ] ] } ]
```

# methods

``` js
var inspect = require('object-inspect')
```

## var s = inspect(obj, opts={})

Return a string `s` with the string representation of `obj` up to a depth of
`opts.depth`.

# install

With [npm](https://npmjs.org) do:

```
npm install object-inspect
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
# shallow-copy

make a shallow copy of an object or array

[![testling badge](https://ci.testling.com/substack/shallow-copy.png)](https://ci.testling.com/substack/shallow-copy)

[![build status](https://secure.travis-ci.org/substack/shallow-copy.png)](http://travis-ci.org/substack/shallow-copy)

# example

you can copy objects shallowly:

``` js
var copy = require('shallow-copy');

var obj = { a: 3, b: 4, c: [5,6] };
var dup = copy(obj);
dup.b *= 111;
dup.c.push(7);

console.log('original: ', obj);
console.log('copy: ', dup);
```

and you can copy arrays shallowly:

``` js
var copy = require('shallow-copy');

var xs = [ 3, 4, 5, { f: 6, g: 7 } ];
var dup = copy(xs);
dup.unshift(1, 2);
dup[5].g += 100;

console.log('original: ', xs);
console.log('copy: ', dup);
```

# methods

``` js
var copy = require('shallow-copy')
```

## copy(obj)

Return a copy of the enumerable properties of the object `obj` without making
copies of nested objects inside of `obj`.

If `obj` is an array, the result will be an array.
If `obj` is an object, the result will be an object.
If `obj` is not an object, its value is returned.

# install

With [npm](https://npmjs.org) do:

```
npm install shallow-copy
```

# license

MIT
# falafel

Transform the [ast](http://en.wikipedia.org/wiki/Abstract_syntax_tree) on a
recursive walk.

[![browser support](http://ci.testling.com/substack/node-falafel.png)](http://ci.testling.com/substack/node-falafel)

[![build status](https://secure.travis-ci.org/substack/node-falafel.png)](http://travis-ci.org/substack/node-falafel)

This modules uses [acorn](https://npmjs.org/package/acorn) to create an AST from
source code.

![falafel döner](http://substack.net/images/falafel.png)

# example

## array.js

Put a function wrapper around all array literals.

``` js
var falafel = require('falafel');

var src = '(' + function () {
    var xs = [ 1, 2, [ 3, 4 ] ];
    var ys = [ 5, 6 ];
    console.dir([ xs, ys ]);
} + ')()';

var output = falafel(src, function (node) {
    if (node.type === 'ArrayExpression') {
        node.update('fn(' + node.source() + ')');
    }
});
console.log(output);
```

output:

```
(function () {
    var xs = fn([ 1, 2, fn([ 3, 4 ]) ]);
    var ys = fn([ 5, 6 ]);
    console.dir(fn([ xs, ys ]));
})()
```

# methods

``` js
var falafel = require('falafel')
```

## falafel(src, opts={}, fn)

Transform the string source `src` with the function `fn`, returning a
string-like transformed output object.

For every node in the ast, `fn(node)` fires. The recursive walk is a
pre-traversal, so children get called before their parents.

Performing a pre-traversal makes it easier to write nested transforms since
transforming parents often requires transforming all its children first.

The return value is string-like (it defines `.toString()` and `.inspect()`) so
that you can call `node.update()` asynchronously after the function has
returned and still capture the output.

Instead of passing a `src` you can also use `opts.source`.

All of the `opts` will be passed directly to
[acorn](https://npmjs.org/package/acorn).

## custom parser

You may pass in an instance of acorn to the opts as `opts.parser` to use that
version instead of the version of acorn packaged with this library.

```js
var acorn = require('acorn-jsx');

falafel(src, {parser: acorn, plugins: { jsx: true }}, function(node) {
  // this will parse jsx
});
```

# nodes

Aside from the regular [esprima](http://esprima.org) data, you can also call
some inserted methods on nodes.

Aside from updating the current node, you can also reach into sub-nodes to call
update functions on children from parent nodes.

## node.source()

Return the source for the given node, including any modifications made to
children nodes.

## node.update(s)

Transform the source for the present node to the string `s`.

Note that in `'ForStatement'` node types, there is an existing subnode called
`update`. For those nodes all the properties are copied over onto the
`node.update()` function.

## node.parent

Reference to the parent element or `null` at the root element.

# install

With [npm](http://npmjs.org) do:

```
npm install falafel
```

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

* opts.preserveSymlinks - if true, doesn't resolve `basedir` to real path before resolving.
This is the way Node resolves dependencies when executed with the [--preserve-symlinks](https://nodejs.org/api/all.html#cli_preserve_symlinks) flag.
**Note:** this property is currently `true` by default but it will be changed to
`false` in the next major version because *Node's resolution algorithm does not preserve symlinks by default*.

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

* `opts.packageFilter(pkg, pkgfile)` - transform the parsed package.json
* contents before looking at the "main" field

* opts.paths - require.paths array to use if nothing is found on the normal
node_modules recursive walk (probably don't use this)

* opts.moduleDirectory - directory (or directories) in which to recursively look for modules. default: `"node_modules"`

* opts.preserveSymlinks - if true, doesn't resolve `basedir` to real path before resolving.
This is the way Node resolves dependencies when executed with the [--preserve-symlinks](https://nodejs.org/api/all.html#cli_preserve_symlinks) flag.
**Note:** this property is currently `true` by default but it will be changed to
`false` in the next major version because *Node's resolution algorithm does not preserve symlinks by default*.

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
    moduleDirectory: 'node_modules',
    preserveSymlinks: true
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
# quote-stream

transform a stream into a quoted string

[![testling badge](https://ci.testling.com/substack/quote-stream.png)](https://ci.testling.com/substack/quote-stream)

[![build status](https://secure.travis-ci.org/substack/quote-stream.png)](http://travis-ci.org/substack/quote-stream)

# example

``` js
var quote = require('quote-stream');
process.stdin.pipe(quote()).pipe(process.stdout);
```

output:

```
$ echo beep boop | node example/stream.js
"beep boop\n"
```

# methods

``` js
var quote = require('quote-stream')
```

## var q = quote()

Return a transform stream `q` that wraps input in double quotes and adds escape
characters to the chunks.

# usage

```
usage: quote-stream

  Transform stdin to a quoted string on stdout.

```

# install

With [npm](https://npmjs.org) do:

```
npm install quote-stream
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
# Form-Data [![NPM Module](https://img.shields.io/npm/v/form-data.svg)](https://www.npmjs.com/package/form-data) [![Join the chat at https://gitter.im/form-data/form-data](http://form-data.github.io/images/gitterbadge.svg)](https://gitter.im/form-data/form-data)

A library to create readable ```"multipart/form-data"``` streams. Can be used to submit forms and file uploads to other web applications.

The API of this library is inspired by the [XMLHttpRequest-2 FormData Interface][xhr2-fd].

[xhr2-fd]: http://dev.w3.org/2006/webapi/XMLHttpRequest-2/Overview.html#the-formdata-interface

[![Linux Build](https://img.shields.io/travis/form-data/form-data/master.svg?label=linux:0.12-8.x)](https://travis-ci.org/form-data/form-data)
[![MacOS Build](https://img.shields.io/travis/form-data/form-data/master.svg?label=macos:0.12-8.x)](https://travis-ci.org/form-data/form-data)
[![Windows Build](https://img.shields.io/appveyor/ci/alexindigo/form-data/master.svg?label=windows:0.12-8.x)](https://ci.appveyor.com/project/alexindigo/form-data)

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
# has

> Object.prototype.hasOwnProperty.call shortcut

## Installation

```sh
npm install --save has
```

## Usage

```js
var has = require('has');

has({}, 'hasOwnProperty'); // false
has(Object.prototype, 'hasOwnProperty'); // true
```
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
buffer-equal
============

Return whether two buffers are equal.

[![build status](https://secure.travis-ci.org/substack/node-buffer-equal.png)](http://travis-ci.org/substack/node-buffer-equal)

example
=======

``` js
var bufferEqual = require('buffer-equal');

console.dir(bufferEqual(
    new Buffer([253,254,255]),
    new Buffer([253,254,255])
));
console.dir(bufferEqual(
    new Buffer('abc'),
    new Buffer('abcd')
));
console.dir(bufferEqual(
    new Buffer('abc'),
    'abc'
));
```

output:

```
true
false
undefined
```

methods
=======

``` js
var bufferEqual = require('buffer-equal')
```

bufferEqual(a, b)
-----------------

Return whether the two buffers `a` and `b` are equal.

If `a` or `b` is not a buffer, return `undefined`.

install
=======

With [npm](http://npmjs.org) do:

```
npm install buffer-equal
```

license
=======

MIT
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

