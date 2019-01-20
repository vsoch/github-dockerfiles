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
# path-is-absolute [![Build Status](https://travis-ci.org/sindresorhus/path-is-absolute.svg?branch=master)](https://travis-ci.org/sindresorhus/path-is-absolute)

> Node.js 0.12 [`path.isAbsolute()`](http://nodejs.org/api/path.html#path_path_isabsolute_path) ponyfill

> Ponyfill: A polyfill that doesn't overwrite the native method


## Install

```
$ npm install --save path-is-absolute
```


## Usage

```js
var pathIsAbsolute = require('path-is-absolute');

// Linux
pathIsAbsolute('/home/foo');
//=> true

// Windows
pathIsAbsolute('C:/Users/');
//=> true

// Any OS
pathIsAbsolute.posix('/home/foo');
//=> true
```


## API

See the [`path.isAbsolute()` docs](http://nodejs.org/api/path.html#path_path_isabsolute_path).

### pathIsAbsolute(path)

### pathIsAbsolute.posix(path)

The Posix specific version.

### pathIsAbsolute.win32(path)

The Windows specific version.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
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
# path-is-absolute [![Build Status](https://travis-ci.org/sindresorhus/path-is-absolute.svg?branch=master)](https://travis-ci.org/sindresorhus/path-is-absolute)

> Node.js 0.12 [`path.isAbsolute()`](http://nodejs.org/api/path.html#path_path_isabsolute_path) ponyfill

> Ponyfill: A polyfill that doesn't overwrite the native method


## Install

```
$ npm install --save path-is-absolute
```


## Usage

```js
var pathIsAbsolute = require('path-is-absolute');

// Linux
pathIsAbsolute('/home/foo');
//=> true

// Windows
pathIsAbsolute('C:/Users/');
//=> true

// Any OS
pathIsAbsolute.posix('/home/foo');
//=> true
```


## API

See the [`path.isAbsolute()` docs](http://nodejs.org/api/path.html#path_path_isabsolute_path).

### pathIsAbsolute(path)

### pathIsAbsolute.posix(path)

The Posix specific version.

### pathIsAbsolute.win32(path)

The Windows specific version.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
TolaBoard

===

To deploy TolaBoard to TolaTables:
    - comment the following lines b/c TolaTables already has bootstrap loaded in `ember-cli-build.js` file:
        -- app.import('bower_components/bootstrap/dist/css/bootstrap.min.css');
        -- app.import('bower_components/bootstrap/dist/js/bootstrap.min.js');
    - Remove `{{partial 'nav'}}` from the file: `app/templates/application.hbs` because we want to keep the TolaTables navigation bar.
    - ember build --environment=production  --output-path dist/static/
#broccoli-asset-rev

[![Build Status](https://circleci.com/gh/rickharrison/broccoli-asset-rev.svg?style=shield)](https://circleci.com/gh/rickharrison/broccoli-asset-rev)
[![codecov.io](https://codecov.io/github/rickharrison/broccoli-asset-rev/coverage.svg?branch=master&precision=2)](https://codecov.io/github/rickharrison/broccoli-asset-rev?branch=master)
[![npm](https://img.shields.io/npm/v/broccoli-asset-rev.svg)](https://www.npmjs.com/package/broccoli-asset-rev)

[Broccoli](https://github.com/broccolijs/broccoli) plugin to add fingerprint checksums to your files and update the source to reflect the new filenames.

Turns

```
<script src="assets/appname.js">
background: url('/images/foo.png');
```

Into

```
<script src="https://subdomain.cloudfront.net/assets/appname-342b0f87ea609e6d349c7925d86bd597.js">
background: url('https://subdomain.cloudfront.net/images/foo-735d6c098496507e26bb40ecc8c1394d.png');
```

## Installation

```js
npm install broccoli-asset-rev --save-dev
```

## Usage

```js
var AssetRev = require('broccoli-asset-rev');

var assetNode = new AssetRev(node, {
  extensions: ['js', 'css', 'png', 'jpg', 'gif'],
  exclude: ['fonts/169929'],
  replaceExtensions: ['html', 'js', 'css'],
  prepend: 'https://subdomain.cloudfront.net/'
});
```

## Options

  - `extensions` - Default: `['js', 'css', 'png', 'jpg', 'gif', 'map']` - The file types to add md5 checksums.
  - `exclude` - Default: `[]` - An array of globs. If a filename contains any item in the exclude array, it will not be fingerprinted.
  - `replaceExtensions` - Default: `['html', 'css', 'js']` - The file types to replace source code with new checksum file names.
  - `prepend` - Default: `''` - A string to prepend to all of the assets. Useful for CDN urls like `https://subdomain.cloudfront.net/`
  - `generateRailsManifest` - Default: none - If true, will generate a `manifest.json` to be used by Sprockets for the Rails Asset Pipeline. The manifest will be fingerprinted by default but this can be avoided by adding `'manifest.json'` to the `exclude` list.
  - `railsManifestPath` - Default: `'assets/manifest-HASH.json'` - The path in the destination folder to store the Rails manifest. Only for the default value, `HASH` will be replace with the fingerprint of the file.
  - `customHash` - Default: none - If set, overrides the md5 checksum calculation with the result of calling `customHash(buffer, pathToFile)`. If it is not a `function`, `customHash` is used as the hash value. If it is set to `null`, fingerprinting is skipped and only prepending occurs.
  - `generateAssetMap` - Default: false. If true, will generate a `assetMap.json` file in a `assets` directory on the output node. This file contains a mapping of the original asset name to the fingerprinted asset, like the following:
  - `assetMapPath` - Default: `'assets/assetMap-HASH.json'` - The path in the destination folder to store the `assetMap.json` in. Only for the default value, `HASH` will be replace with the fingerprint of the file.

```js
{
	assets: {
		css/file1.css: css/file1-sdaa7d6a87d6ada78ds.css,
		images/image1.png: images/image1-sdaa7d6a87d6ada78ds.css,
	}
}
```
  - `fingerprintAssetMap` - Default: false. If true, will fingerprint `assetMap.json`.
  - `ignore` - Default: `[]` - An array of strings.  If a filename contains any item in the ignore array, the contents of the file will not be processed for fingerprinting.
  - `annotation` - Default: null. A human-readable description for this plugin instance.

## Default settings
The default [settings](https://github.com/rickharrison/broccoli-asset-rev/blob/master/lib/default-options.js) are available if needed in your application or addon via:
`var broccoliAssetRevDefaults = require( 'broccoli-asset-rev/lib/default-options' );`

## Ember CLI addon usage

```js
var app = new EmberApp({
  fingerprint: {
    exclude: ['fonts/169929'],
    prepend: 'https://sudomain.cloudfront.net/'
  }
});
```

## Ember CLI addon options

  - `enabled` - Default: `app.env === 'production'` - Boolean. Enables fingerprinting if true. **True by default if current environment is production.**
  - `exclude` - Default: `[]` - An array of globs. If a filename contains any item in the exclude array, it will not be fingerprinted.
  - `extensions` - Default: `['js', 'css', 'png', 'jpg', 'gif', 'map']` - The file types to add md5 checksums.
  - `prepend` - Default: `''` - A string to prepend to all of the assets. Useful for CDN urls like `https://subdomain.cloudfront.net/`
  - `replaceExtensions` - Default: `['html', 'css', 'js']` - The file types to replace source code with new checksum file names.

[![ghit.me](https://ghit.me/badge.svg?repo=rickharrison/broccoli-asset-rev)](https://ghit.me/repo/rickharrison/broccoli-asset-rev)
# MatcherCollection [![Build Status](https://travis-ci.org/stefanpenner/matcher-collection.svg?branch=master)](https://travis-ci.org/stefanpenner/matcher-collection)

Minimatch but for collections of minimatcher matchers.

## Install

```sh
npm install matcher-collection
```

## Examples

```js
let m = new MatcherCollection([
  'tests/',
  '**/*.js',
]);

m.match('tests/foo.js') // => true
m.match('foo.js')       // => false

m.mayContain('tests') // => true
m.mayContain('foo')   // => false
```
# minimatch

A minimal matching utility.

[![Build Status](https://secure.travis-ci.org/isaacs/minimatch.svg)](http://travis-ci.org/isaacs/minimatch)


This is the matching library used internally by npm.

It works by converting glob expressions into JavaScript `RegExp`
objects.

## Usage

```javascript
var minimatch = require("minimatch")

minimatch("bar.foo", "*.foo") // true!
minimatch("bar.foo", "*.bar") // false!
minimatch("bar.foo", "*.+(bar|foo)", { debug: true }) // true, and noisy!
```

## Features

Supports these glob features:

* Brace Expansion
* Extended glob matching
* "Globstar" `**` matching

See:

* `man sh`
* `man bash`
* `man 3 fnmatch`
* `man 5 gitignore`

## Minimatch Class

Create a minimatch object by instantiating the `minimatch.Minimatch` class.

```javascript
var Minimatch = require("minimatch").Minimatch
var mm = new Minimatch(pattern, options)
```

### Properties

* `pattern` The original pattern the minimatch object represents.
* `options` The options supplied to the constructor.
* `set` A 2-dimensional array of regexp or string expressions.
  Each row in the
  array corresponds to a brace-expanded pattern.  Each item in the row
  corresponds to a single path-part.  For example, the pattern
  `{a,b/c}/d` would expand to a set of patterns like:

        [ [ a, d ]
        , [ b, c, d ] ]

    If a portion of the pattern doesn't have any "magic" in it
    (that is, it's something like `"foo"` rather than `fo*o?`), then it
    will be left as a string rather than converted to a regular
    expression.

* `regexp` Created by the `makeRe` method.  A single regular expression
  expressing the entire pattern.  This is useful in cases where you wish
  to use the pattern somewhat like `fnmatch(3)` with `FNM_PATH` enabled.
* `negate` True if the pattern is negated.
* `comment` True if the pattern is a comment.
* `empty` True if the pattern is `""`.

### Methods

* `makeRe` Generate the `regexp` member if necessary, and return it.
  Will return `false` if the pattern is invalid.
* `match(fname)` Return true if the filename matches the pattern, or
  false otherwise.
* `matchOne(fileArray, patternArray, partial)` Take a `/`-split
  filename, and match it against a single row in the `regExpSet`.  This
  method is mainly for internal use, but is exposed so that it can be
  used by a glob-walker that needs to avoid excessive filesystem calls.

All other methods are internal, and will be called as necessary.

### minimatch(path, pattern, options)

Main export.  Tests a path against the pattern using the options.

```javascript
var isJS = minimatch(file, "*.js", { matchBase: true })
```

### minimatch.filter(pattern, options)

Returns a function that tests its
supplied argument, suitable for use with `Array.filter`.  Example:

```javascript
var javascripts = fileList.filter(minimatch.filter("*.js", {matchBase: true}))
```

### minimatch.match(list, pattern, options)

Match against the list of
files, in the style of fnmatch or glob.  If nothing is matched, and
options.nonull is set, then return a list containing the pattern itself.

```javascript
var javascripts = minimatch.match(fileList, "*.js", {matchBase: true}))
```

### minimatch.makeRe(pattern, options)

Make a regular expression object from the pattern.

## Options

All options are `false` by default.

### debug

Dump a ton of stuff to stderr.

### nobrace

Do not expand `{a,b}` and `{1..3}` brace sets.

### noglobstar

Disable `**` matching against multiple folder names.

### dot

Allow patterns to match filenames starting with a period, even if
the pattern does not explicitly have a period in that spot.

Note that by default, `a/**/b` will **not** match `a/.d/b`, unless `dot`
is set.

### noext

Disable "extglob" style patterns like `+(a|b)`.

### nocase

Perform a case-insensitive match.

### nonull

When a match is not found by `minimatch.match`, return a list containing
the pattern itself if this option is set.  When not set, an empty list
is returned if there are no matches.

### matchBase

If set, then patterns without slashes will be matched
against the basename of the path if it contains slashes.  For example,
`a?b` would match the path `/xyz/123/acb`, but not `/xyz/acb/123`.

### nocomment

Suppress the behavior of treating `#` at the start of a pattern as a
comment.

### nonegate

Suppress the behavior of treating a leading `!` character as negation.

### flipNegate

Returns from negate expressions the same as if they were not negated.
(Ie, true on a hit, false on a miss.)


## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between minimatch and other
implementations, and are intentional.

If the pattern starts with a `!` character, then it is negated.  Set the
`nonegate` flag to suppress this behavior, and treat leading `!`
characters normally.  This is perhaps relevant if you wish to start the
pattern with a negative extglob pattern like `!(a|B)`.  Multiple `!`
characters at the start of a pattern will negate the pattern multiple
times.

If a pattern starts with `#`, then it is treated as a comment, and
will not match anything.  Use `\#` to match a literal `#` at the
start of a line, or set the `nocomment` flag to suppress this behavior.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.1, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

If an escaped pattern has no matches, and the `nonull` flag is set,
then minimatch.match returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`minimatch.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.
# brace-expansion

[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), 
as known from sh/bash, in JavaScript.

[![build status](https://secure.travis-ci.org/juliangruber/brace-expansion.svg)](http://travis-ci.org/juliangruber/brace-expansion)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)

[![testling badge](https://ci.testling.com/juliangruber/brace-expansion.png)](https://ci.testling.com/juliangruber/brace-expansion)

## Example

```js
var expand = require('brace-expansion');

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API

```js
var expand = require('brace-expansion');
```

### var expanded = expand(str)

Return an array of all possible and valid expansions of `str`. If none are
found, `[str]` is returned.

Valid expansions are:

```js
/^(.*,)+(.+)?$/
// {a,b,...}
```

A comma seperated list of options, like `{a,b}` or `{a,{b,c}}` or `{,a,}`.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.

For compatibility reasons, the string `${` is not eligible for brace expansion.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install brace-expansion
```

## Contributors

- [Julian Gruber](https://github.com/juliangruber)
- [Isaac Z. Schlueter](https://github.com/isaacs)

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
# balanced-match

Match balanced string pairs, like `{` and `}` or `<b>` and `</b>`. Supports regular expressions as well!

[![build status](https://secure.travis-ci.org/juliangruber/balanced-match.svg)](http://travis-ci.org/juliangruber/balanced-match)
[![downloads](https://img.shields.io/npm/dm/balanced-match.svg)](https://www.npmjs.org/package/balanced-match)

[![testling badge](https://ci.testling.com/juliangruber/balanced-match.png)](https://ci.testling.com/juliangruber/balanced-match)

## Example

Get the first matching pair of braces:

```js
var balanced = require('balanced-match');

console.log(balanced('{', '}', 'pre{in{nested}}post'));
console.log(balanced('{', '}', 'pre{first}between{second}post'));
console.log(balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'));
```

The matches are:

```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## API

### var m = balanced(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:

* **start** the index of the first match of `a`
* **end** the index of the matching `b`
* **pre** the preamble, `a` and `b` not included
* **body** the match, `a` and `b` not included
* **post** the postscript, `a` and `b` not included

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `['{', 'a', '']` and `{a}}` will match `['', 'a', '}']`.

### var r = balanced.range(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ <a index>, <b index> ]`.

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `[ 1, 3 ]` and `{a}}` will match `[0, 2]`.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install balanced-match
```

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
# broccoli-filter

[![Build Status](https://travis-ci.org/broccolijs/broccoli-filter.svg?branch=master)](https://travis-ci.org/broccolijs/broccoli-filter)
[![Build status](https://ci.appveyor.com/api/projects/status/hc68s0vbn9di4ehi/branch/master?svg=true)](https://ci.appveyor.com/project/joliss/broccoli-filter/branch/master)

Helper base class for Broccoli plugins that map input files into output files
one-to-one.

## API

```js
class Filter {
  /**
   * Abstract base-class for filtering purposes.
   *
   * Enforces that it is invoked on an instance of a class which prototypically
   * inherits from Filter, and which is not itself Filter.
   */
  constructor(inputNode: BroccoliNode, options: FilterOptions): Filter;

  /**
   * Abstract method `processString`: must be implemented on subclasses of
   * Filter.
   *
   * The return value is written as the contents of the output file
   */
  abstract processString(contents: string, relativePath: string): string;

  /**
   * Virtual method `getDestFilePath`: determine whether the source file should
   * be processed, and optionally rename the output file when processing occurs.
   *
   * Return `null` to pass the file through without processing. Return
   * `relativePath` to process the file with `processString`. Return a
   * different path to process the file with `processString` and rename it.
   *
   * By default, if the options passed into the `Filter` constructor contain a
   * property `extensions`, and `targetExtension` is supplied, the first matching
   * extension in the list is replaced with the `targetExtension` option's value.
   */
  virtual getDestFilePath(relativePath: string): string;
}
```

### Options

* `extensions`: An array of file extensions to process, e.g. `['md', 'markdown']`.
* `targetExtension`: The file extension of the corresponding output files, e.g.
  `'html'`.
* `inputEncoding`: The character encoding used for reading input files to be
  processed (default: `'utf8'`). For binary files, pass `null` to receive a
  `Buffer` object in `processString`.
* `outputEncoding`: The character encoding used for writing output files after
  processing (default: `'utf8'`). For binary files, pass `null` and return a
  `Buffer` object from `processString`.
* `name`, `annotation`: Same as
  [broccoli-plugin](https://github.com/broccolijs/broccoli-plugin#new-plugininputnodes-options);
  see there.

All options except `name` and `annotation` can also be set on the prototype
instead of being passed into the constructor.

### Example Usage

```js
var Filter = require('broccoli-filter');

Awk.prototype = Object.create(Filter.prototype);
Awk.prototype.constructor = Awk;
function Awk(inputNode, search, replace, options) {
  options = options || {};
  Filter.call(this, inputNode, {
    annotation: options.annotation
  });
  this.search = search;
  this.replace = replace;
}

Awk.prototype.extensions = ['txt'];
Awk.prototype.targetExtension = 'txt';

Awk.prototype.processString = function(content, relativePath) {
  return content.replace(this.search, this.replace);
};
```

In `Brocfile.js`, use your new `Awk` plugin like so:

```
var node = new Awk('docs', 'ES6', 'ECMAScript 2015');

module.exports = node;
```

## FAQ

### Upgrading from 0.1.x to 1.x

You must now call the base class constructor. For example:

```js
// broccoli-filter 0.1.x:
function MyPlugin(inputTree) {
  this.inputTree = inputTree;
}

// broccoli-filter 1.x:
function MyPlugin(inputNode) {
  Filter.call(this, inputNode);
}
```

Note that "node" is simply new terminology for "tree".

### Source Maps

**Can this help with compilers that are almost 1:1, like a minifier that takes
a `.js` and `.js.map` file and outputs a `.js` and `.js.map` file?**

Not at the moment. I don't know yet how to implement this and still have the
API look beautiful. We also have to make sure that caching works correctly, as
we have to invalidate if either the `.js` or the `.js.map` file changes. My
plan is to write a source-map-aware uglifier plugin to understand this use
case better, and then extract common code back into this `Filter` base class.
# promise-map-series

[![Build Status](https://travis-ci.org/joliss/promise-map-series.png?branch=master)](https://travis-ci.org/joliss/promise-map-series)

Call an iterator function for each element of an array in series, ensuring
that no iterator is called before the promise returned by the previous
iterator is fulfilled, in effect preventing parallel execution. Like
[async.mapSeries](https://github.com/caolan/async#mapseriesarr-iterator-callback),
but for promises.

## Installation

```bash
npm install --save promise-map-series
```

## Usage

```js
var mapSeries = require('promise-map-series')

mapSeries(array, iterator[, thisArg]).then(function (newArray) {
  ...
})
```

* **`array`**: An array of values (should not be promises).

* **`iterator`**: Function that returns a promise or a value for the new
  array. The `iterator` will be called once for each element. If `iterator`
  returns a promise, then `iterator` will only be called for the next element
  once that promise is fulfilled. If the promise is rejected or `iterator`
  throws an error, iteration will stop immediately and `mapSeries` returns a
  rejected promise. The `iterator` function receives three arguments:

    * **`item`**: The current item in the array.

    * **`index`**: The current index in the array.

    * **`array`**: The original `array` argument.

* **`thisArg`** (optional): Value to use as `this` when executing `iterator`.
# broccoli-kitchen-sink-helpers

A disparate collection of helper functions used by Broccoli and Broccoli
plugins, though none of them are necessarily specific to Broccoli. Not
documented, specced, tested.

All of these are yearning to be extracted into packages of their own. Takers
are welcome.
[![Build Status](https://travis-ci.org/isaacs/node-glob.svg?branch=master)](https://travis-ci.org/isaacs/node-glob/) [![Dependency Status](https://david-dm.org/isaacs/node-glob.svg)](https://david-dm.org/isaacs/node-glob) [![devDependency Status](https://david-dm.org/isaacs/node-glob/dev-status.svg)](https://david-dm.org/isaacs/node-glob#info=devDependencies) [![optionalDependency Status](https://david-dm.org/isaacs/node-glob/optional-status.svg)](https://david-dm.org/isaacs/node-glob#info=optionalDependencies)

# Glob

Match files using the patterns the shell uses, like stars and stuff.

This is a glob implementation in JavaScript.  It uses the `minimatch`
library to do its matching.

![](oh-my-glob.gif)

## Usage

```javascript
var glob = require("glob")

// options is optional
glob("**/*.js", options, function (er, files) {
  // files is an array of filenames.
  // If the `nonull` option is set, and nothing
  // was found, then files is ["**/*.js"]
  // er is an error object or null.
})
```

## Glob Primer

"Globs" are the patterns you type when you do stuff like `ls *.js` on
the command line, or put `build/*` in a `.gitignore` file.

Before parsing the path part patterns, braced sections are expanded
into a set.  Braced sections start with `{` and end with `}`, with any
number of comma-delimited sections within.  Braced sections may contain
slash characters, so `a{/b/c,bcd}` would expand into `a/b/c` and `abcd`.

The following characters have special magic meaning when used in a
path portion:

* `*` Matches 0 or more characters in a single path portion
* `?` Matches 1 character
* `[...]` Matches a range of characters, similar to a RegExp range.
  If the first character of the range is `!` or `^` then it matches
  any character not in the range.
* `!(pattern|pattern|pattern)` Matches anything that does not match
  any of the patterns provided.
* `?(pattern|pattern|pattern)` Matches zero or one occurrence of the
  patterns provided.
* `+(pattern|pattern|pattern)` Matches one or more occurrences of the
  patterns provided.
* `*(a|b|c)` Matches zero or more occurrences of the patterns provided
* `@(pattern|pat*|pat?erN)` Matches exactly one of the patterns
  provided
* `**` If a "globstar" is alone in a path portion, then it matches
  zero or more directories and subdirectories searching for matches.
  It does not crawl symlinked directories.

### Dots

If a file or directory path portion has a `.` as the first character,
then it will not match any glob pattern unless that pattern's
corresponding path part also has a `.` as its first character.

For example, the pattern `a/.*/c` would match the file at `a/.b/c`.
However the pattern `a/*/c` would not, because `*` does not start with
a dot character.

You can make glob treat dots as normal characters by setting
`dot:true` in the options.

### Basename Matching

If you set `matchBase:true` in the options, and the pattern has no
slashes in it, then it will seek for any file anywhere in the tree
with a matching basename.  For example, `*.js` would match
`test/simple/basic.js`.

### Negation

The intent for negation would be for a pattern starting with `!` to
match everything that *doesn't* match the supplied pattern.  However,
the implementation is weird, and for the time being, this should be
avoided.  The behavior is deprecated in version 5, and will be removed
entirely in version 6.

### Empty Sets

If no matching files are found, then an empty array is returned.  This
differs from the shell, where the pattern itself is returned.  For
example:

    $ echo a*s*d*f
    a*s*d*f

To get the bash-style behavior, set the `nonull:true` in the options.

### See Also:

* `man sh`
* `man bash` (Search for "Pattern Matching")
* `man 3 fnmatch`
* `man 5 gitignore`
* [minimatch documentation](https://github.com/isaacs/minimatch)

## glob.hasMagic(pattern, [options])

Returns `true` if there are any special characters in the pattern, and
`false` otherwise.

Note that the options affect the results.  If `noext:true` is set in
the options object, then `+(a|b)` will not be considered a magic
pattern.  If the pattern has a brace expansion, like `a/{b/c,x/y}`
then that is considered magical, unless `nobrace:true` is set in the
options.

## glob(pattern, [options], cb)

* `pattern` {String} Pattern to be matched
* `options` {Object}
* `cb` {Function}
  * `err` {Error | null}
  * `matches` {Array<String>} filenames found matching the pattern

Perform an asynchronous glob search.

## glob.sync(pattern, [options])

* `pattern` {String} Pattern to be matched
* `options` {Object}
* return: {Array<String>} filenames found matching the pattern

Perform a synchronous glob search.

## Class: glob.Glob

Create a Glob object by instantiating the `glob.Glob` class.

```javascript
var Glob = require("glob").Glob
var mg = new Glob(pattern, options, cb)
```

It's an EventEmitter, and starts walking the filesystem to find matches
immediately.

### new glob.Glob(pattern, [options], [cb])

* `pattern` {String} pattern to search for
* `options` {Object}
* `cb` {Function} Called when an error occurs, or matches are found
  * `err` {Error | null}
  * `matches` {Array<String>} filenames found matching the pattern

Note that if the `sync` flag is set in the options, then matches will
be immediately available on the `g.found` member.

### Properties

* `minimatch` The minimatch object that the glob uses.
* `options` The options object passed in.
* `aborted` Boolean which is set to true when calling `abort()`.  There
  is no way at this time to continue a glob search after aborting, but
  you can re-use the statCache to avoid having to duplicate syscalls.
* `cache` Convenience object.  Each field has the following possible
  values:
  * `false` - Path does not exist
  * `true` - Path exists
  * `'DIR'` - Path exists, and is not a directory
  * `'FILE'` - Path exists, and is a directory
  * `[file, entries, ...]` - Path exists, is a directory, and the
    array value is the results of `fs.readdir`
* `statCache` Cache of `fs.stat` results, to prevent statting the same
  path multiple times.
* `symlinks` A record of which paths are symbolic links, which is
  relevant in resolving `**` patterns.
* `realpathCache` An optional object which is passed to `fs.realpath`
  to minimize unnecessary syscalls.  It is stored on the instantiated
  Glob object, and may be re-used.

### Events

* `end` When the matching is finished, this is emitted with all the
  matches found.  If the `nonull` option is set, and no match was found,
  then the `matches` list contains the original pattern.  The matches
  are sorted, unless the `nosort` flag is set.
* `match` Every time a match is found, this is emitted with the matched.
* `error` Emitted when an unexpected error is encountered, or whenever
  any fs error occurs if `options.strict` is set.
* `abort` When `abort()` is called, this event is raised.

### Methods

* `pause` Temporarily stop the search
* `resume` Resume the search
* `abort` Stop the search forever

### Options

All the options that can be passed to Minimatch can also be passed to
Glob to change pattern matching behavior.  Also, some have been added,
or have glob-specific ramifications.

All options are false by default, unless otherwise noted.

All options are added to the Glob object, as well.

If you are running many `glob` operations, you can pass a Glob object
as the `options` argument to a subsequent operation to shortcut some
`stat` and `readdir` calls.  At the very least, you may pass in shared
`symlinks`, `statCache`, `realpathCache`, and `cache` options, so that
parallel glob operations will be sped up by sharing information about
the filesystem.

* `cwd` The current working directory in which to search.  Defaults
  to `process.cwd()`.
* `root` The place where patterns starting with `/` will be mounted
  onto.  Defaults to `path.resolve(options.cwd, "/")` (`/` on Unix
  systems, and `C:\` or some such on Windows.)
* `dot` Include `.dot` files in normal matches and `globstar` matches.
  Note that an explicit dot in a portion of the pattern will always
  match dot files.
* `nomount` By default, a pattern starting with a forward-slash will be
  "mounted" onto the root setting, so that a valid filesystem path is
  returned.  Set this flag to disable that behavior.
* `mark` Add a `/` character to directory matches.  Note that this
  requires additional stat calls.
* `nosort` Don't sort the results.
* `stat` Set to true to stat *all* results.  This reduces performance
  somewhat, and is completely unnecessary, unless `readdir` is presumed
  to be an untrustworthy indicator of file existence.
* `silent` When an unusual error is encountered when attempting to
  read a directory, a warning will be printed to stderr.  Set the
  `silent` option to true to suppress these warnings.
* `strict` When an unusual error is encountered when attempting to
  read a directory, the process will just continue on in search of
  other matches.  Set the `strict` option to raise an error in these
  cases.
* `cache` See `cache` property above.  Pass in a previously generated
  cache object to save some fs calls.
* `statCache` A cache of results of filesystem information, to prevent
  unnecessary stat calls.  While it should not normally be necessary
  to set this, you may pass the statCache from one glob() call to the
  options object of another, if you know that the filesystem will not
  change between calls.  (See "Race Conditions" below.)
* `symlinks` A cache of known symbolic links.  You may pass in a
  previously generated `symlinks` object to save `lstat` calls when
  resolving `**` matches.
* `sync` DEPRECATED: use `glob.sync(pattern, opts)` instead.
* `nounique` In some cases, brace-expanded patterns can result in the
  same file showing up multiple times in the result set.  By default,
  this implementation prevents duplicates in the result set.  Set this
  flag to disable that behavior.
* `nonull` Set to never return an empty set, instead returning a set
  containing the pattern itself.  This is the default in glob(3).
* `debug` Set to enable debug logging in minimatch and glob.
* `nobrace` Do not expand `{a,b}` and `{1..3}` brace sets.
* `noglobstar` Do not match `**` against multiple filenames.  (Ie,
  treat it as a normal `*` instead.)
* `noext` Do not match `+(a|b)` "extglob" patterns.
* `nocase` Perform a case-insensitive match.  Note: on
  case-insensitive filesystems, non-magic patterns will match by
  default, since `stat` and `readdir` will not raise errors.
* `matchBase` Perform a basename-only match if the pattern does not
  contain any slash characters.  That is, `*.js` would be treated as
  equivalent to `**/*.js`, matching all js files in all directories.
* `nodir` Do not match directories, only files.  (Note: to match
  *only* directories, simply put a `/` at the end of the pattern.)
* `ignore` Add a pattern or an array of patterns to exclude matches.
* `follow` Follow symlinked directories when expanding `**` patterns.
  Note that this can result in a lot of duplicate references in the
  presence of cyclic links.
* `realpath` Set to true to call `fs.realpath` on all of the results.
  In the case of a symlink that cannot be resolved, the full absolute
  path to the matched entry is returned (though it will usually be a
  broken symlink)
* `nonegate` Suppress deprecated `negate` behavior.  (See below.)
  Default=true
* `nocomment` Suppress deprecated `comment` behavior.  (See below.)
  Default=true

## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between node-glob and other
implementations, and are intentional.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.3, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

Note that symlinked directories are not crawled as part of a `**`,
though their contents may match against subsequent portions of the
pattern.  This prevents infinite loops and duplicates and the like.

If an escaped pattern has no matches, and the `nonull` flag is set,
then glob returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`glob.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.

### Comments and Negation

**Note**: In version 5 of this module, negation and comments are
**disabled** by default.  You can explicitly set `nonegate:false` or
`nocomment:false` to re-enable them.  They are going away entirely in
version 6.

The intent for negation would be for a pattern starting with `!` to
match everything that *doesn't* match the supplied pattern.  However,
the implementation is weird.  It is better to use the `ignore` option
to set a pattern or set of patterns to exclude from matches.  If you
want the "everything except *x*" type of behavior, you can use `**` as
the main pattern, and set an `ignore` for the things to exclude.

The comments feature is added in minimatch, primarily to more easily
support use cases like ignore files, where a `#` at the start of a
line makes the pattern "empty".  However, in the context of a
straightforward filesystem globber, "comments" don't make much sense.

## Windows

**Please only use forward-slashes in glob expressions.**

Though windows uses either `/` or `\` as its path separator, only `/`
characters are used by this glob implementation.  You must use
forward-slashes **only** in glob expressions.  Back-slashes will always
be interpreted as escape characters, not path separators.

Results from absolute patterns such as `/foo/*` are mounted onto the
root setting using `path.join`.  On windows, this will by default result
in `/foo/*` matching `C:\foo\bar.txt`.

## Race Conditions

Glob searching, by its very nature, is susceptible to race conditions,
since it relies on directory walking and such.

As a result, it is possible that a file that exists when glob looks for
it may have been deleted or modified by the time it returns the result.

As part of its internal implementation, this program caches all stat
and readdir calls that it makes, in order to cut down on system
overhead.  However, this also makes it even more susceptible to races,
especially if the cache or statCache objects are reused between glob
calls.

Users are thus advised not to use a glob result as a guarantee of
filesystem state in the face of rapid changes.  For the vast majority
of operations, this is never a problem.

## Contributing

Any change to behavior (including bugfixes) must come with a test.

Patches that fail tests or reduce performance will be rejected.

```
# to run tests
npm test

# to re-generate test fixtures
npm run test-regen

# to benchmark against bash/zsh
npm run bench

# to profile javascript
npm run prof
```
# minimatch

A minimal matching utility.

[![Build Status](https://secure.travis-ci.org/isaacs/minimatch.svg)](http://travis-ci.org/isaacs/minimatch)


This is the matching library used internally by npm.

It works by converting glob expressions into JavaScript `RegExp`
objects.

## Usage

```javascript
var minimatch = require("minimatch")

minimatch("bar.foo", "*.foo") // true!
minimatch("bar.foo", "*.bar") // false!
minimatch("bar.foo", "*.+(bar|foo)", { debug: true }) // true, and noisy!
```

## Features

Supports these glob features:

* Brace Expansion
* Extended glob matching
* "Globstar" `**` matching

See:

* `man sh`
* `man bash`
* `man 3 fnmatch`
* `man 5 gitignore`

## Minimatch Class

Create a minimatch object by instantiating the `minimatch.Minimatch` class.

```javascript
var Minimatch = require("minimatch").Minimatch
var mm = new Minimatch(pattern, options)
```

### Properties

* `pattern` The original pattern the minimatch object represents.
* `options` The options supplied to the constructor.
* `set` A 2-dimensional array of regexp or string expressions.
  Each row in the
  array corresponds to a brace-expanded pattern.  Each item in the row
  corresponds to a single path-part.  For example, the pattern
  `{a,b/c}/d` would expand to a set of patterns like:

        [ [ a, d ]
        , [ b, c, d ] ]

    If a portion of the pattern doesn't have any "magic" in it
    (that is, it's something like `"foo"` rather than `fo*o?`), then it
    will be left as a string rather than converted to a regular
    expression.

* `regexp` Created by the `makeRe` method.  A single regular expression
  expressing the entire pattern.  This is useful in cases where you wish
  to use the pattern somewhat like `fnmatch(3)` with `FNM_PATH` enabled.
* `negate` True if the pattern is negated.
* `comment` True if the pattern is a comment.
* `empty` True if the pattern is `""`.

### Methods

* `makeRe` Generate the `regexp` member if necessary, and return it.
  Will return `false` if the pattern is invalid.
* `match(fname)` Return true if the filename matches the pattern, or
  false otherwise.
* `matchOne(fileArray, patternArray, partial)` Take a `/`-split
  filename, and match it against a single row in the `regExpSet`.  This
  method is mainly for internal use, but is exposed so that it can be
  used by a glob-walker that needs to avoid excessive filesystem calls.

All other methods are internal, and will be called as necessary.

### minimatch(path, pattern, options)

Main export.  Tests a path against the pattern using the options.

```javascript
var isJS = minimatch(file, "*.js", { matchBase: true })
```

### minimatch.filter(pattern, options)

Returns a function that tests its
supplied argument, suitable for use with `Array.filter`.  Example:

```javascript
var javascripts = fileList.filter(minimatch.filter("*.js", {matchBase: true}))
```

### minimatch.match(list, pattern, options)

Match against the list of
files, in the style of fnmatch or glob.  If nothing is matched, and
options.nonull is set, then return a list containing the pattern itself.

```javascript
var javascripts = minimatch.match(fileList, "*.js", {matchBase: true}))
```

### minimatch.makeRe(pattern, options)

Make a regular expression object from the pattern.

## Options

All options are `false` by default.

### debug

Dump a ton of stuff to stderr.

### nobrace

Do not expand `{a,b}` and `{1..3}` brace sets.

### noglobstar

Disable `**` matching against multiple folder names.

### dot

Allow patterns to match filenames starting with a period, even if
the pattern does not explicitly have a period in that spot.

Note that by default, `a/**/b` will **not** match `a/.d/b`, unless `dot`
is set.

### noext

Disable "extglob" style patterns like `+(a|b)`.

### nocase

Perform a case-insensitive match.

### nonull

When a match is not found by `minimatch.match`, return a list containing
the pattern itself if this option is set.  When not set, an empty list
is returned if there are no matches.

### matchBase

If set, then patterns without slashes will be matched
against the basename of the path if it contains slashes.  For example,
`a?b` would match the path `/xyz/123/acb`, but not `/xyz/acb/123`.

### nocomment

Suppress the behavior of treating `#` at the start of a pattern as a
comment.

### nonegate

Suppress the behavior of treating a leading `!` character as negation.

### flipNegate

Returns from negate expressions the same as if they were not negated.
(Ie, true on a hit, false on a miss.)


## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between minimatch and other
implementations, and are intentional.

If the pattern starts with a `!` character, then it is negated.  Set the
`nonegate` flag to suppress this behavior, and treat leading `!`
characters normally.  This is perhaps relevant if you wish to start the
pattern with a negative extglob pattern like `!(a|B)`.  Multiple `!`
characters at the start of a pattern will negate the pattern multiple
times.

If a pattern starts with `#`, then it is treated as a comment, and
will not match anything.  Use `\#` to match a literal `#` at the
start of a line, or set the `nocomment` flag to suppress this behavior.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.1, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

If an escaped pattern has no matches, and the `nonull` flag is set,
then minimatch.match returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`minimatch.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.
# brace-expansion

[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), 
as known from sh/bash, in JavaScript.

[![build status](https://secure.travis-ci.org/juliangruber/brace-expansion.svg)](http://travis-ci.org/juliangruber/brace-expansion)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)

[![testling badge](https://ci.testling.com/juliangruber/brace-expansion.png)](https://ci.testling.com/juliangruber/brace-expansion)

## Example

```js
var expand = require('brace-expansion');

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API

```js
var expand = require('brace-expansion');
```

### var expanded = expand(str)

Return an array of all possible and valid expansions of `str`. If none are
found, `[str]` is returned.

Valid expansions are:

```js
/^(.*,)+(.+)?$/
// {a,b,...}
```

A comma seperated list of options, like `{a,b}` or `{a,{b,c}}` or `{,a,}`.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.

For compatibility reasons, the string `${` is not eligible for brace expansion.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install brace-expansion
```

## Contributors

- [Julian Gruber](https://github.com/juliangruber)
- [Isaac Z. Schlueter](https://github.com/isaacs)

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
# balanced-match

Match balanced string pairs, like `{` and `}` or `<b>` and `</b>`. Supports regular expressions as well!

[![build status](https://secure.travis-ci.org/juliangruber/balanced-match.svg)](http://travis-ci.org/juliangruber/balanced-match)
[![downloads](https://img.shields.io/npm/dm/balanced-match.svg)](https://www.npmjs.org/package/balanced-match)

[![testling badge](https://ci.testling.com/juliangruber/balanced-match.png)](https://ci.testling.com/juliangruber/balanced-match)

## Example

Get the first matching pair of braces:

```js
var balanced = require('balanced-match');

console.log(balanced('{', '}', 'pre{in{nested}}post'));
console.log(balanced('{', '}', 'pre{first}between{second}post'));
console.log(balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'));
```

The matches are:

```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## API

### var m = balanced(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:

* **start** the index of the first match of `a`
* **end** the index of the matching `b`
* **pre** the preamble, `a` and `b` not included
* **body** the match, `a` and `b` not included
* **post** the postscript, `a` and `b` not included

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `['{', 'a', '']` and `{a}}` will match `['', 'a', '}']`.

### var r = balanced.range(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ <a index>, <b index> ]`.

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `[ 1, 3 ]` and `{a}}` will match `[0, 2]`.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install balanced-match
```

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Browser-friendly inheritance fully compatible with standard node.js
[inherits](http://nodejs.org/api/util.html#util_util_inherits_constructor_superconstructor).

This package exports standard `inherits` from node.js `util` module in
node environment, but also provides alternative browser-friendly
implementation through [browser
field](https://gist.github.com/shtylman/4339901). Alternative
implementation is a literal copy of standard one located in standalone
module to avoid requiring of `util`. It also has a shim for old
browsers with no `Object.create` support.

While keeping you sure you are using standard `inherits`
implementation in node.js environment, it allows bundlers such as
[browserify](https://github.com/substack/node-browserify) to not
include full `util` package to your client code if all you need is
just `inherits` function. It worth, because browser shim for `util`
package is large and `inherits` is often the single function you need
from it.

It's recommended to use this package instead of
`require('util').inherits` for any code that has chances to be used
not only in node.js but in browser too.

## usage

```js
var inherits = require('inherits');
// then use exactly as the standard one
```

## note on version ~1.0

Version ~1.0 had completely different motivation and is not compatible
neither with 2.0 nor with standard node.js `inherits`.

If you are using version ~1.0 and planning to switch to ~2.0, be
careful:

* new version uses `super_` instead of `super` for referencing
  superclass
* new version overwrites current prototype while old one preserves any
  existing fields on it
# inflight

Add callbacks to requests in flight to avoid async duplication

## USAGE

```javascript
var inflight = require('inflight')

// some request that does some stuff
function req(key, callback) {
  // key is any random string.  like a url or filename or whatever.
  //
  // will return either a falsey value, indicating that the
  // request for this key is already in flight, or a new callback
  // which when called will call all callbacks passed to inflightk
  // with the same key
  callback = inflight(key, callback)

  // If we got a falsey value back, then there's already a req going
  if (!callback) return

  // this is where you'd fetch the url or whatever
  // callback is also once()-ified, so it can safely be assigned
  // to multiple events etc.  First call wins.
  setTimeout(function() {
    callback(null, key)
  }, 100)
}

// only assigns a single setTimeout
// when it dings, all cbs get called
req('foo', cb1)
req('foo', cb2)
req('foo', cb3)
req('foo', cb4)
```
# wrappy

Callback wrapping utility

## USAGE

```javascript
var wrappy = require("wrappy")

// var wrapper = wrappy(wrapperFunction)

// make sure a cb is called only once
// See also: http://npm.im/once for this specific use case
var once = wrappy(function (cb) {
  var called = false
  return function () {
    if (called) return
    called = true
    return cb.apply(this, arguments)
  }
})

function printBoo () {
  console.log('boo')
}
// has some rando property
printBoo.iAmBooPrinter = true

var onlyPrintOnce = once(printBoo)

onlyPrintOnce() // prints 'boo'
onlyPrintOnce() // does nothing

// random property is retained!
assert.equal(onlyPrintOnce.iAmBooPrinter, true)
```
# once

Only call a function once.

## usage

```javascript
var once = require('once')

function load (file, cb) {
  cb = once(cb)
  loader.load('file')
  loader.once('load', cb)
  loader.once('error', cb)
}
```

Or add to the Function.prototype in a responsible way:

```javascript
// only has to be done once
require('once').proto()

function load (file, cb) {
  cb = cb.once()
  loader.load('file')
  loader.once('load', cb)
  loader.once('error', cb)
}
```

Ironically, the prototype feature makes this module twice as
complicated as necessary.

To check whether you function has been called, use `fn.called`. Once the
function is called for the first time the return value of the original
function is saved in `fn.value` and subsequent calls will continue to
return this value.

```javascript
var once = require('once')

function load (cb) {
  cb = once(cb)
  var stream = createStream()
  stream.once('data', cb)
  stream.once('end', function () {
    if (!cb.called) cb(new Error('not found'))
  })
}
```

## `once.strict(func)`

Throw an error if the function is called twice.

Some functions are expected to be called only once. Using `once` for them would
potentially hide logical errors.

In the example below, the `greet` function has to call the callback only once:

```javascript
function greet (name, cb) {
  // return is missing from the if statement
  // when no name is passed, the callback is called twice
  if (!name) cb('Hello anonymous')
  cb('Hello ' + name)
}

function log (msg) {
  console.log(msg)
}

// this will print 'Hello anonymous' but the logical error will be missed
greet(null, once(msg))

// once.strict will print 'Hello anonymous' and throw an error when the callback will be called the second time
greet(null, once.strict(msg))
```
# wrappy

Callback wrapping utility

## USAGE

```javascript
var wrappy = require("wrappy")

// var wrapper = wrappy(wrapperFunction)

// make sure a cb is called only once
// See also: http://npm.im/once for this specific use case
var once = wrappy(function (cb) {
  var called = false
  return function () {
    if (called) return
    called = true
    return cb.apply(this, arguments)
  }
})

function printBoo () {
  console.log('boo')
}
// has some rando property
printBoo.iAmBooPrinter = true

var onlyPrintOnce = once(printBoo)

onlyPrintOnce() // prints 'boo'
onlyPrintOnce() // does nothing

// random property is retained!
assert.equal(onlyPrintOnce.iAmBooPrinter, true)
```
# node-copy-dereference

Copy a file or directory, dereferencing symlinks in the process, and
preserving last-modified times and file modes.

Made for use by Broccoli and Broccoli plugins.

## Installation

```sh
npm install --save copy-dereference
```

## Example

```js
var copyDereferenceSync = require('copy-dereference').sync;

copyDereferenceSync('src_dir/some_file.txt', 'dest_dir/some_file.txt');
copyDereferenceSync('src_dir/some_dir', 'dest_dir/some_dir');
```

## Description

```js
copyDereferenceSync(srcPath, destPath)
```

Copy the file or directory at `srcPath` to `destPath`.

If `srcPath` is a symlink, or if there is a symlink somewhere underneath the
directory at `srcPath`, it will be dereferenced, that is, it will be replaced
with the thing it points to.

File & directory last-modified times as well as file modes (permissions &
executable bit) will be preserved.

We throw an exception if there are any broken symlinks at or beneath
`srcPath`, if `srcPath` does not exist, of if `destPath`'s parent directory
does not exist.

Furthermore, we throw an exception if `destPath` already exists. Thus in
contrast to Unix `cp`, the following will fail:

```js
// dest_dir already exists, and we might expect dest_dir/some_dir to be
// created. This does not work; pass 'dest_dir/some_dir' instead.
copyDereferenceSync('src_dir/some_dir', 'dest_dir');
```

File types other than files, directories and symlinks (such as device files or
sockets) are not supported and will cause an exception.

## Notes

* There intentionally isn't an asynchronous version. It's not clear that we
need or want one. Before sending a patch to add an async version, please share
your use case on the issue tracker.
# node-symlink-or-copy

[![Build Status](https://travis-ci.org/broccolijs/node-symlink-or-copy.svg?branch=master)](https://travis-ci.org/broccolijs/node-symlink-or-copy)
[![Build status](https://ci.appveyor.com/api/projects/status/rilxgmo21j3qth3v/branch/master?svg=true)](https://ci.appveyor.com/project/joliss/node-symlink-or-copy/branch/master)

Symlink a file or directory to another place. Fall back to copying on Windows.
Made for use with Broccoli plugins, for "do what I mean" behavior.

## Installation

```sh
npm install --save symlink-or-copy
```

## Example

```js
var symlinkOrCopySync = require('symlink-or-copy').sync;

symlinkOrCopySync('src_dir/some_file.txt', 'dest_dir/some_file.txt');
symlinkOrCopySync('src_dir/some_dir', 'dest_dir/some_dir');
```

## Description

```js
symlinkOrCopySync(srcPath, destPath)
```

Create a symlink at `destPath` pointing to `srcPath`.

On Windows, we may fall back to copying `srcPath` to `destPath`, preserving
last-modified times. However, do not *rely* on always getting a copy on
Windows (see Notes below).

If you pass a relative `srcPath`, it will be resolved relative to
`process.cwd()`, akin to a copy function. Note that this is unlike
[`fs.symlinkSync`](http://nodejs.org/api/fs.html#fs_fs_symlink_srcpath_dstpath_type_callback),
whose `srcPath` is relative to `destPath`.

If `srcPath` does not exist or is a broken symlink, we might throw an
exception, or we might create a broken symlink.

When we fall back to copying, symlinks at or beneath `srcPath` will be
dereferenced, and broken symlinks will cause exceptions.

We will throw an exception if `destPath` already exists. Thus in contrast to
Unix `cp` or `ln`, the following will fail:

```js
// dest_dir already exists, and we might expect dest_dir/some_dir to be
// created. This does not work; pass 'dest_dir/some_dir' instead.
symlinkOrCopySync('src_dir/some_dir', 'dest_dir');
```

It is an error if the parent directory of `destPath` does not already exist.

When we symlink, if the file at `srcPath` is a symlink as well, it will be
dereferenced before symlinking, to avoid runaway symlink indirection.

## Notes

* Symlinks technically work on Windows, but they require special rights. For
  users with those rights, symlinks are used, but when not available, a
  combination of junctions and copying is used to mimic the behavior somewhat
  performantly.

* There intentionally isn't an asynchronoukks version. It's not clear that we
  need or want one. Before sending a patch to add an async version, please
  share your use case on the issue tracker.
# ms.js: miliseconds conversion utility

```js
ms('2 days')  // 172800000
ms('1d')      // 86400000
ms('10h')     // 36000000
ms('2.5 hrs') // 9000000
ms('2h')      // 7200000
ms('1m')      // 60000
ms('5s')      // 5000
ms('100')     // 100
```

```js
ms(60000)             // "1m"
ms(2 * 60000)         // "2m"
ms(ms('10 hours'))    // "10h"
```

```js
ms(60000, { long: true })             // "1 minute"
ms(2 * 60000, { long: true })         // "2 minutes"
ms(ms('10 hours'), { long: true })    // "10 hours"
```

- Node/Browser compatible. Published as [`ms`](https://www.npmjs.org/package/ms) in [NPM](http://nodejs.org/download).
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT
# The Broccoli Plugin Base Class

[![Build Status](https://travis-ci.org/broccolijs/broccoli-plugin.svg?branch=master)](https://travis-ci.org/broccolijs/broccoli-plugin)
[![Build status](https://ci.appveyor.com/api/projects/status/k4tk8b99m1e58ftd?svg=true)](https://ci.appveyor.com/project/joliss/broccoli-plugin)

## Example Usage

```js
var Plugin = require('broccoli-plugin');
var path = require('path');

// Create a subclass MyPlugin derived from Plugin
MyPlugin.prototype = Object.create(Plugin.prototype);
MyPlugin.prototype.constructor = MyPlugin;
function MyPlugin(inputNodes, options) {
  options = options || {};
  Plugin.call(this, inputNodes, {
    annotation: options.annotation
  });
  this.options = options;
}

MyPlugin.prototype.build = function() {
  // Read files from this.inputPaths, and write files to this.outputPath.
  // Silly example:

  // Read 'foo.txt' from the third input node
  var inputBuffer = fs.readFileSync(path.join(this.inputPaths[2], 'foo.txt'));
  var outputBuffer = someCompiler(inputBuffer);
  // Write to 'bar.txt' in this node's output
  fs.writeFileSync(path.join(this.outputPath, 'bar.txt'), outputBuffer);
};
```

## Reference

### `new Plugin(inputNodes, options)`

Call this base class constructor from your subclass constructor.

* `inputNodes`: An array of node objects that this plugin will read from.
  Nodes are usually other plugin instances; they were formerly known as
  "trees".

* `options`

    * `name`: The name of this plugin class. Defaults to `this.constructor.name`.
    * `annotation`: A descriptive annotation. Useful for debugging, to tell
      multiple instances of the same plugin apart.
    * `persistentOutput`: If true, the output directory is not automatically
      emptied between builds.

### `Plugin.prototype.build()`

Override this method in your subclass. It will be called on each (re-)build.

This function will typically access the following read-only properties:

* `this.inputPaths`: An array of paths on disk corresponding to each node in
  `inputNodes`. Your plugin will read files from these paths.

* `this.outputPath`: The path on disk corresponding to this plugin instance
  (this node). Your plugin will write files to this path. This directory is
  emptied by Broccoli before each build, unless the `persistentOutput` options
  is true.

* `this.cachePath`: The path on disk to an auxiliary cache directory. Use this
  to store files that you want preserved between builds. This directory will
  only be deleted when Broccoli exits.

All paths stay the same between builds.

To perform asynchronous work, return a promise. The promise's eventual value
is ignored (typically `null`).

To report a compile error, `throw` it or return a rejected promise. Also see
section "Error Objects" below.

### `Plugin.prototype.getCallbackObject()`

Advanced usage only.

Return the object on which Broccoli will call `obj.build()`. Called once after
instantiation. By default, returns `this`. Plugins do not usually need to
override this, but it can be useful for base classes that other plugins in turn
derive from, such as
[broccoli-caching-writer](https://github.com/ember-cli/broccoli-caching-writer).

For example, to intercept `.build()` calls, you might
`return { build: this.buildWrapper.bind(this) }`.
Or, to hand off the plugin implementation to a completely separate object:
`return new MyPluginWorker(this.inputPaths, this.outputPath, this.cachePath)`,
where `MyPluginWorker` provides a `.build` method.

### Error Objects

To help with displaying clear error messages for build errors, error objects
may have the following optional properties in addition to the standard
`message` property:

* `file`: Path of the file in which the error occurred, relative to one of the
  `inputPaths` directories
* `treeDir`: The path that `file` is relative to. Must be an element of
  `this.inputPaths`. (The name `treeDir` is for historical reasons.)
* `line`: Line in which the error occurred (one-indexed)
* `column`: Column in which the error occurred (zero-indexed)
[![Build Status](https://travis-ci.org/isaacs/rimraf.svg?branch=master)](https://travis-ci.org/isaacs/rimraf) [![Dependency Status](https://david-dm.org/isaacs/rimraf.svg)](https://david-dm.org/isaacs/rimraf) [![devDependency Status](https://david-dm.org/isaacs/rimraf/dev-status.svg)](https://david-dm.org/isaacs/rimraf#info=devDependencies)

The [UNIX command](http://en.wikipedia.org/wiki/Rm_(Unix)) `rm -rf` for node.

Install with `npm install rimraf`, or just drop rimraf.js somewhere.

## API

`rimraf(f, [opts], callback)`

The first parameter will be interpreted as a globbing pattern for files. If you
want to disable globbing you can do so with `opts.disableGlob` (defaults to
`false`). This might be handy, for instance, if you have filenames that contain
globbing wildcard characters.

The callback will be called with an error if there is one.  Certain
errors are handled for you:

* Windows: `EBUSY` and `ENOTEMPTY` - rimraf will back off a maximum of
  `opts.maxBusyTries` times before giving up, adding 100ms of wait
  between each attempt.  The default `maxBusyTries` is 3.
* `ENOENT` - If the file doesn't exist, rimraf will return
  successfully, since your desired outcome is already the case.
* `EMFILE` - Since `readdir` requires opening a file descriptor, it's
  possible to hit `EMFILE` if too many file descriptors are in use.
  In the sync case, there's nothing to be done for this.  But in the
  async case, rimraf will gradually back off with timeouts up to
  `opts.emfileWait` ms, which defaults to 1000.

## options

* unlink, chmod, stat, lstat, rmdir, readdir,
  unlinkSync, chmodSync, statSync, lstatSync, rmdirSync, readdirSync

    In order to use a custom file system library, you can override
    specific fs functions on the options object.

    If any of these functions are present on the options object, then
    the supplied function will be used instead of the default fs
    method.

    Sync methods are only relevant for `rimraf.sync()`, of course.

    For example:

    ```javascript
    var myCustomFS = require('some-custom-fs')

    rimraf('some-thing', myCustomFS, callback)
    ```

* maxBusyTries

    If an `EBUSY`, `ENOTEMPTY`, or `EPERM` error code is encountered
    on Windows systems, then rimraf will retry with a linear backoff
    wait of 100ms longer on each try.  The default maxBusyTries is 3.

    Only relevant for async usage.

* emfileWait

    If an `EMFILE` error is encountered, then rimraf will retry
    repeatedly with a linear backoff of 1ms longer on each try, until
    the timeout counter hits this max.  The default limit is 1000.

    If you repeatedly encounter `EMFILE` errors, then consider using
    [graceful-fs](http://npm.im/graceful-fs) in your program.

    Only relevant for async usage.

* glob

    Set to `false` to disable [glob](http://npm.im/glob) pattern
    matching.

    Set to an object to pass options to the glob module.  The default
    glob options are `{ nosort: true, silent: true }`.

    Glob version 6 is used in this module.

    Relevant for both sync and async usage.

* disableGlob

    Set to any non-falsey value to disable globbing entirely.
    (Equivalent to setting `glob: false`.)

## rimraf.sync

It can remove stuff synchronously, too.  But that's not so good.  Use
the async API.  It's better.

## CLI

If installed with `npm install rimraf -g` it can be used as a global
command `rimraf <path> [<path> ...]` which is useful for cross platform support.

## mkdirp

If you need to create a directory recursively, check out
[mkdirp](https://github.com/substack/node-mkdirp).
# Glob

Match files using the patterns the shell uses, like stars and stuff.

[![Build Status](https://travis-ci.org/isaacs/node-glob.svg?branch=master)](https://travis-ci.org/isaacs/node-glob/) [![Build Status](https://ci.appveyor.com/api/projects/status/kd7f3yftf7unxlsx?svg=true)](https://ci.appveyor.com/project/isaacs/node-glob) [![Coverage Status](https://coveralls.io/repos/isaacs/node-glob/badge.svg?branch=master&service=github)](https://coveralls.io/github/isaacs/node-glob?branch=master)

This is a glob implementation in JavaScript.  It uses the `minimatch`
library to do its matching.

![](oh-my-glob.gif)

## Usage

Install with npm

```
npm i glob
```

```javascript
var glob = require("glob")

// options is optional
glob("**/*.js", options, function (er, files) {
  // files is an array of filenames.
  // If the `nonull` option is set, and nothing
  // was found, then files is ["**/*.js"]
  // er is an error object or null.
})
```

## Glob Primer

"Globs" are the patterns you type when you do stuff like `ls *.js` on
the command line, or put `build/*` in a `.gitignore` file.

Before parsing the path part patterns, braced sections are expanded
into a set.  Braced sections start with `{` and end with `}`, with any
number of comma-delimited sections within.  Braced sections may contain
slash characters, so `a{/b/c,bcd}` would expand into `a/b/c` and `abcd`.

The following characters have special magic meaning when used in a
path portion:

* `*` Matches 0 or more characters in a single path portion
* `?` Matches 1 character
* `[...]` Matches a range of characters, similar to a RegExp range.
  If the first character of the range is `!` or `^` then it matches
  any character not in the range.
* `!(pattern|pattern|pattern)` Matches anything that does not match
  any of the patterns provided.
* `?(pattern|pattern|pattern)` Matches zero or one occurrence of the
  patterns provided.
* `+(pattern|pattern|pattern)` Matches one or more occurrences of the
  patterns provided.
* `*(a|b|c)` Matches zero or more occurrences of the patterns provided
* `@(pattern|pat*|pat?erN)` Matches exactly one of the patterns
  provided
* `**` If a "globstar" is alone in a path portion, then it matches
  zero or more directories and subdirectories searching for matches.
  It does not crawl symlinked directories.

### Dots

If a file or directory path portion has a `.` as the first character,
then it will not match any glob pattern unless that pattern's
corresponding path part also has a `.` as its first character.

For example, the pattern `a/.*/c` would match the file at `a/.b/c`.
However the pattern `a/*/c` would not, because `*` does not start with
a dot character.

You can make glob treat dots as normal characters by setting
`dot:true` in the options.

### Basename Matching

If you set `matchBase:true` in the options, and the pattern has no
slashes in it, then it will seek for any file anywhere in the tree
with a matching basename.  For example, `*.js` would match
`test/simple/basic.js`.

### Empty Sets

If no matching files are found, then an empty array is returned.  This
differs from the shell, where the pattern itself is returned.  For
example:

    $ echo a*s*d*f
    a*s*d*f

To get the bash-style behavior, set the `nonull:true` in the options.

### See Also:

* `man sh`
* `man bash` (Search for "Pattern Matching")
* `man 3 fnmatch`
* `man 5 gitignore`
* [minimatch documentation](https://github.com/isaacs/minimatch)

## glob.hasMagic(pattern, [options])

Returns `true` if there are any special characters in the pattern, and
`false` otherwise.

Note that the options affect the results.  If `noext:true` is set in
the options object, then `+(a|b)` will not be considered a magic
pattern.  If the pattern has a brace expansion, like `a/{b/c,x/y}`
then that is considered magical, unless `nobrace:true` is set in the
options.

## glob(pattern, [options], cb)

* `pattern` `{String}` Pattern to be matched
* `options` `{Object}`
* `cb` `{Function}`
  * `err` `{Error | null}`
  * `matches` `{Array<String>}` filenames found matching the pattern

Perform an asynchronous glob search.

## glob.sync(pattern, [options])

* `pattern` `{String}` Pattern to be matched
* `options` `{Object}`
* return: `{Array<String>}` filenames found matching the pattern

Perform a synchronous glob search.

## Class: glob.Glob

Create a Glob object by instantiating the `glob.Glob` class.

```javascript
var Glob = require("glob").Glob
var mg = new Glob(pattern, options, cb)
```

It's an EventEmitter, and starts walking the filesystem to find matches
immediately.

### new glob.Glob(pattern, [options], [cb])

* `pattern` `{String}` pattern to search for
* `options` `{Object}`
* `cb` `{Function}` Called when an error occurs, or matches are found
  * `err` `{Error | null}`
  * `matches` `{Array<String>}` filenames found matching the pattern

Note that if the `sync` flag is set in the options, then matches will
be immediately available on the `g.found` member.

### Properties

* `minimatch` The minimatch object that the glob uses.
* `options` The options object passed in.
* `aborted` Boolean which is set to true when calling `abort()`.  There
  is no way at this time to continue a glob search after aborting, but
  you can re-use the statCache to avoid having to duplicate syscalls.
* `cache` Convenience object.  Each field has the following possible
  values:
  * `false` - Path does not exist
  * `true` - Path exists
  * `'FILE'` - Path exists, and is not a directory
  * `'DIR'` - Path exists, and is a directory
  * `[file, entries, ...]` - Path exists, is a directory, and the
    array value is the results of `fs.readdir`
* `statCache` Cache of `fs.stat` results, to prevent statting the same
  path multiple times.
* `symlinks` A record of which paths are symbolic links, which is
  relevant in resolving `**` patterns.
* `realpathCache` An optional object which is passed to `fs.realpath`
  to minimize unnecessary syscalls.  It is stored on the instantiated
  Glob object, and may be re-used.

### Events

* `end` When the matching is finished, this is emitted with all the
  matches found.  If the `nonull` option is set, and no match was found,
  then the `matches` list contains the original pattern.  The matches
  are sorted, unless the `nosort` flag is set.
* `match` Every time a match is found, this is emitted with the specific
  thing that matched. It is not deduplicated or resolved to a realpath.
* `error` Emitted when an unexpected error is encountered, or whenever
  any fs error occurs if `options.strict` is set.
* `abort` When `abort()` is called, this event is raised.

### Methods

* `pause` Temporarily stop the search
* `resume` Resume the search
* `abort` Stop the search forever

### Options

All the options that can be passed to Minimatch can also be passed to
Glob to change pattern matching behavior.  Also, some have been added,
or have glob-specific ramifications.

All options are false by default, unless otherwise noted.

All options are added to the Glob object, as well.

If you are running many `glob` operations, you can pass a Glob object
as the `options` argument to a subsequent operation to shortcut some
`stat` and `readdir` calls.  At the very least, you may pass in shared
`symlinks`, `statCache`, `realpathCache`, and `cache` options, so that
parallel glob operations will be sped up by sharing information about
the filesystem.

* `cwd` The current working directory in which to search.  Defaults
  to `process.cwd()`.
* `root` The place where patterns starting with `/` will be mounted
  onto.  Defaults to `path.resolve(options.cwd, "/")` (`/` on Unix
  systems, and `C:\` or some such on Windows.)
* `dot` Include `.dot` files in normal matches and `globstar` matches.
  Note that an explicit dot in a portion of the pattern will always
  match dot files.
* `nomount` By default, a pattern starting with a forward-slash will be
  "mounted" onto the root setting, so that a valid filesystem path is
  returned.  Set this flag to disable that behavior.
* `mark` Add a `/` character to directory matches.  Note that this
  requires additional stat calls.
* `nosort` Don't sort the results.
* `stat` Set to true to stat *all* results.  This reduces performance
  somewhat, and is completely unnecessary, unless `readdir` is presumed
  to be an untrustworthy indicator of file existence.
* `silent` When an unusual error is encountered when attempting to
  read a directory, a warning will be printed to stderr.  Set the
  `silent` option to true to suppress these warnings.
* `strict` When an unusual error is encountered when attempting to
  read a directory, the process will just continue on in search of
  other matches.  Set the `strict` option to raise an error in these
  cases.
* `cache` See `cache` property above.  Pass in a previously generated
  cache object to save some fs calls.
* `statCache` A cache of results of filesystem information, to prevent
  unnecessary stat calls.  While it should not normally be necessary
  to set this, you may pass the statCache from one glob() call to the
  options object of another, if you know that the filesystem will not
  change between calls.  (See "Race Conditions" below.)
* `symlinks` A cache of known symbolic links.  You may pass in a
  previously generated `symlinks` object to save `lstat` calls when
  resolving `**` matches.
* `sync` DEPRECATED: use `glob.sync(pattern, opts)` instead.
* `nounique` In some cases, brace-expanded patterns can result in the
  same file showing up multiple times in the result set.  By default,
  this implementation prevents duplicates in the result set.  Set this
  flag to disable that behavior.
* `nonull` Set to never return an empty set, instead returning a set
  containing the pattern itself.  This is the default in glob(3).
* `debug` Set to enable debug logging in minimatch and glob.
* `nobrace` Do not expand `{a,b}` and `{1..3}` brace sets.
* `noglobstar` Do not match `**` against multiple filenames.  (Ie,
  treat it as a normal `*` instead.)
* `noext` Do not match `+(a|b)` "extglob" patterns.
* `nocase` Perform a case-insensitive match.  Note: on
  case-insensitive filesystems, non-magic patterns will match by
  default, since `stat` and `readdir` will not raise errors.
* `matchBase` Perform a basename-only match if the pattern does not
  contain any slash characters.  That is, `*.js` would be treated as
  equivalent to `**/*.js`, matching all js files in all directories.
* `nodir` Do not match directories, only files.  (Note: to match
  *only* directories, simply put a `/` at the end of the pattern.)
* `ignore` Add a pattern or an array of glob patterns to exclude matches.
  Note: `ignore` patterns are *always* in `dot:true` mode, regardless
  of any other settings.
* `follow` Follow symlinked directories when expanding `**` patterns.
  Note that this can result in a lot of duplicate references in the
  presence of cyclic links.
* `realpath` Set to true to call `fs.realpath` on all of the results.
  In the case of a symlink that cannot be resolved, the full absolute
  path to the matched entry is returned (though it will usually be a
  broken symlink)

## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between node-glob and other
implementations, and are intentional.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.3, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

Note that symlinked directories are not crawled as part of a `**`,
though their contents may match against subsequent portions of the
pattern.  This prevents infinite loops and duplicates and the like.

If an escaped pattern has no matches, and the `nonull` flag is set,
then glob returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`glob.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.

### Comments and Negation

Previously, this module let you mark a pattern as a "comment" if it
started with a `#` character, or a "negated" pattern if it started
with a `!` character.

These options were deprecated in version 5, and removed in version 6.

To specify things that should not match, use the `ignore` option.

## Windows

**Please only use forward-slashes in glob expressions.**

Though windows uses either `/` or `\` as its path separator, only `/`
characters are used by this glob implementation.  You must use
forward-slashes **only** in glob expressions.  Back-slashes will always
be interpreted as escape characters, not path separators.

Results from absolute patterns such as `/foo/*` are mounted onto the
root setting using `path.join`.  On windows, this will by default result
in `/foo/*` matching `C:\foo\bar.txt`.

## Race Conditions

Glob searching, by its very nature, is susceptible to race conditions,
since it relies on directory walking and such.

As a result, it is possible that a file that exists when glob looks for
it may have been deleted or modified by the time it returns the result.

As part of its internal implementation, this program caches all stat
and readdir calls that it makes, in order to cut down on system
overhead.  However, this also makes it even more susceptible to races,
especially if the cache or statCache objects are reused between glob
calls.

Users are thus advised not to use a glob result as a guarantee of
filesystem state in the face of rapid changes.  For the vast majority
of operations, this is never a problem.

## Contributing

Any change to behavior (including bugfixes) must come with a test.

Patches that fail tests or reduce performance will be rejected.

```
# to run tests
npm test

# to re-generate test fixtures
npm run test-regen

# to benchmark against bash/zsh
npm run bench

# to profile javascript
npm run prof
```
# minimatch

A minimal matching utility.

[![Build Status](https://secure.travis-ci.org/isaacs/minimatch.svg)](http://travis-ci.org/isaacs/minimatch)


This is the matching library used internally by npm.

It works by converting glob expressions into JavaScript `RegExp`
objects.

## Usage

```javascript
var minimatch = require("minimatch")

minimatch("bar.foo", "*.foo") // true!
minimatch("bar.foo", "*.bar") // false!
minimatch("bar.foo", "*.+(bar|foo)", { debug: true }) // true, and noisy!
```

## Features

Supports these glob features:

* Brace Expansion
* Extended glob matching
* "Globstar" `**` matching

See:

* `man sh`
* `man bash`
* `man 3 fnmatch`
* `man 5 gitignore`

## Minimatch Class

Create a minimatch object by instantiating the `minimatch.Minimatch` class.

```javascript
var Minimatch = require("minimatch").Minimatch
var mm = new Minimatch(pattern, options)
```

### Properties

* `pattern` The original pattern the minimatch object represents.
* `options` The options supplied to the constructor.
* `set` A 2-dimensional array of regexp or string expressions.
  Each row in the
  array corresponds to a brace-expanded pattern.  Each item in the row
  corresponds to a single path-part.  For example, the pattern
  `{a,b/c}/d` would expand to a set of patterns like:

        [ [ a, d ]
        , [ b, c, d ] ]

    If a portion of the pattern doesn't have any "magic" in it
    (that is, it's something like `"foo"` rather than `fo*o?`), then it
    will be left as a string rather than converted to a regular
    expression.

* `regexp` Created by the `makeRe` method.  A single regular expression
  expressing the entire pattern.  This is useful in cases where you wish
  to use the pattern somewhat like `fnmatch(3)` with `FNM_PATH` enabled.
* `negate` True if the pattern is negated.
* `comment` True if the pattern is a comment.
* `empty` True if the pattern is `""`.

### Methods

* `makeRe` Generate the `regexp` member if necessary, and return it.
  Will return `false` if the pattern is invalid.
* `match(fname)` Return true if the filename matches the pattern, or
  false otherwise.
* `matchOne(fileArray, patternArray, partial)` Take a `/`-split
  filename, and match it against a single row in the `regExpSet`.  This
  method is mainly for internal use, but is exposed so that it can be
  used by a glob-walker that needs to avoid excessive filesystem calls.

All other methods are internal, and will be called as necessary.

### minimatch(path, pattern, options)

Main export.  Tests a path against the pattern using the options.

```javascript
var isJS = minimatch(file, "*.js", { matchBase: true })
```

### minimatch.filter(pattern, options)

Returns a function that tests its
supplied argument, suitable for use with `Array.filter`.  Example:

```javascript
var javascripts = fileList.filter(minimatch.filter("*.js", {matchBase: true}))
```

### minimatch.match(list, pattern, options)

Match against the list of
files, in the style of fnmatch or glob.  If nothing is matched, and
options.nonull is set, then return a list containing the pattern itself.

```javascript
var javascripts = minimatch.match(fileList, "*.js", {matchBase: true}))
```

### minimatch.makeRe(pattern, options)

Make a regular expression object from the pattern.

## Options

All options are `false` by default.

### debug

Dump a ton of stuff to stderr.

### nobrace

Do not expand `{a,b}` and `{1..3}` brace sets.

### noglobstar

Disable `**` matching against multiple folder names.

### dot

Allow patterns to match filenames starting with a period, even if
the pattern does not explicitly have a period in that spot.

Note that by default, `a/**/b` will **not** match `a/.d/b`, unless `dot`
is set.

### noext

Disable "extglob" style patterns like `+(a|b)`.

### nocase

Perform a case-insensitive match.

### nonull

When a match is not found by `minimatch.match`, return a list containing
the pattern itself if this option is set.  When not set, an empty list
is returned if there are no matches.

### matchBase

If set, then patterns without slashes will be matched
against the basename of the path if it contains slashes.  For example,
`a?b` would match the path `/xyz/123/acb`, but not `/xyz/acb/123`.

### nocomment

Suppress the behavior of treating `#` at the start of a pattern as a
comment.

### nonegate

Suppress the behavior of treating a leading `!` character as negation.

### flipNegate

Returns from negate expressions the same as if they were not negated.
(Ie, true on a hit, false on a miss.)


## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between minimatch and other
implementations, and are intentional.

If the pattern starts with a `!` character, then it is negated.  Set the
`nonegate` flag to suppress this behavior, and treat leading `!`
characters normally.  This is perhaps relevant if you wish to start the
pattern with a negative extglob pattern like `!(a|B)`.  Multiple `!`
characters at the start of a pattern will negate the pattern multiple
times.

If a pattern starts with `#`, then it is treated as a comment, and
will not match anything.  Use `\#` to match a literal `#` at the
start of a line, or set the `nocomment` flag to suppress this behavior.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.1, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

If an escaped pattern has no matches, and the `nonull` flag is set,
then minimatch.match returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`minimatch.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.
# brace-expansion

[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), 
as known from sh/bash, in JavaScript.

[![build status](https://secure.travis-ci.org/juliangruber/brace-expansion.svg)](http://travis-ci.org/juliangruber/brace-expansion)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)

[![testling badge](https://ci.testling.com/juliangruber/brace-expansion.png)](https://ci.testling.com/juliangruber/brace-expansion)

## Example

```js
var expand = require('brace-expansion');

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API

```js
var expand = require('brace-expansion');
```

### var expanded = expand(str)

Return an array of all possible and valid expansions of `str`. If none are
found, `[str]` is returned.

Valid expansions are:

```js
/^(.*,)+(.+)?$/
// {a,b,...}
```

A comma seperated list of options, like `{a,b}` or `{a,{b,c}}` or `{,a,}`.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.

For compatibility reasons, the string `${` is not eligible for brace expansion.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install brace-expansion
```

## Contributors

- [Julian Gruber](https://github.com/juliangruber)
- [Isaac Z. Schlueter](https://github.com/isaacs)

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
# balanced-match

Match balanced string pairs, like `{` and `}` or `<b>` and `</b>`. Supports regular expressions as well!

[![build status](https://secure.travis-ci.org/juliangruber/balanced-match.svg)](http://travis-ci.org/juliangruber/balanced-match)
[![downloads](https://img.shields.io/npm/dm/balanced-match.svg)](https://www.npmjs.org/package/balanced-match)

[![testling badge](https://ci.testling.com/juliangruber/balanced-match.png)](https://ci.testling.com/juliangruber/balanced-match)

## Example

Get the first matching pair of braces:

```js
var balanced = require('balanced-match');

console.log(balanced('{', '}', 'pre{in{nested}}post'));
console.log(balanced('{', '}', 'pre{first}between{second}post'));
console.log(balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'));
```

The matches are:

```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## API

### var m = balanced(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:

* **start** the index of the first match of `a`
* **end** the index of the matching `b`
* **pre** the preamble, `a` and `b` not included
* **body** the match, `a` and `b` not included
* **post** the postscript, `a` and `b` not included

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `['{', 'a', '']` and `{a}}` will match `['', 'a', '}']`.

### var r = balanced.range(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ <a index>, <b index> ]`.

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `[ 1, 3 ]` and `{a}}` will match `[0, 2]`.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install balanced-match
```

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Browser-friendly inheritance fully compatible with standard node.js
[inherits](http://nodejs.org/api/util.html#util_util_inherits_constructor_superconstructor).

This package exports standard `inherits` from node.js `util` module in
node environment, but also provides alternative browser-friendly
implementation through [browser
field](https://gist.github.com/shtylman/4339901). Alternative
implementation is a literal copy of standard one located in standalone
module to avoid requiring of `util`. It also has a shim for old
browsers with no `Object.create` support.

While keeping you sure you are using standard `inherits`
implementation in node.js environment, it allows bundlers such as
[browserify](https://github.com/substack/node-browserify) to not
include full `util` package to your client code if all you need is
just `inherits` function. It worth, because browser shim for `util`
package is large and `inherits` is often the single function you need
from it.

It's recommended to use this package instead of
`require('util').inherits` for any code that has chances to be used
not only in node.js but in browser too.

## usage

```js
var inherits = require('inherits');
// then use exactly as the standard one
```

## note on version ~1.0

Version ~1.0 had completely different motivation and is not compatible
neither with 2.0 nor with standard node.js `inherits`.

If you are using version ~1.0 and planning to switch to ~2.0, be
careful:

* new version uses `super_` instead of `super` for referencing
  superclass
* new version overwrites current prototype while old one preserves any
  existing fields on it
# inflight

Add callbacks to requests in flight to avoid async duplication

## USAGE

```javascript
var inflight = require('inflight')

// some request that does some stuff
function req(key, callback) {
  // key is any random string.  like a url or filename or whatever.
  //
  // will return either a falsey value, indicating that the
  // request for this key is already in flight, or a new callback
  // which when called will call all callbacks passed to inflightk
  // with the same key
  callback = inflight(key, callback)

  // If we got a falsey value back, then there's already a req going
  if (!callback) return

  // this is where you'd fetch the url or whatever
  // callback is also once()-ified, so it can safely be assigned
  // to multiple events etc.  First call wins.
  setTimeout(function() {
    callback(null, key)
  }, 100)
}

// only assigns a single setTimeout
// when it dings, all cbs get called
req('foo', cb1)
req('foo', cb2)
req('foo', cb3)
req('foo', cb4)
```
# wrappy

Callback wrapping utility

## USAGE

```javascript
var wrappy = require("wrappy")

// var wrapper = wrappy(wrapperFunction)

// make sure a cb is called only once
// See also: http://npm.im/once for this specific use case
var once = wrappy(function (cb) {
  var called = false
  return function () {
    if (called) return
    called = true
    return cb.apply(this, arguments)
  }
})

function printBoo () {
  console.log('boo')
}
// has some rando property
printBoo.iAmBooPrinter = true

var onlyPrintOnce = once(printBoo)

onlyPrintOnce() // prints 'boo'
onlyPrintOnce() // does nothing

// random property is retained!
assert.equal(onlyPrintOnce.iAmBooPrinter, true)
```
# fs.realpath

A backwards-compatible fs.realpath for Node v6 and above

In Node v6, the JavaScript implementation of fs.realpath was replaced
with a faster (but less resilient) native implementation.  That raises
new and platform-specific errors and cannot handle long or excessively
symlink-looping paths.

This module handles those cases by detecting the new errors and
falling back to the JavaScript implementation.  On versions of Node
prior to v6, it has no effect.

## USAGE

```js
var rp = require('fs.realpath')

// async version
rp.realpath(someLongAndLoopingPath, function (er, real) {
  // the ELOOP was handled, but it was a bit slower
})

// sync version
var real = rp.realpathSync(someLongAndLoopingPath)

// monkeypatch at your own risk!
// This replaces the fs.realpath/fs.realpathSync builtins
rp.monkeypatch()

// un-do the monkeypatching
rp.unmonkeypatch()
```
# once

Only call a function once.

## usage

```javascript
var once = require('once')

function load (file, cb) {
  cb = once(cb)
  loader.load('file')
  loader.once('load', cb)
  loader.once('error', cb)
}
```

Or add to the Function.prototype in a responsible way:

```javascript
// only has to be done once
require('once').proto()

function load (file, cb) {
  cb = cb.once()
  loader.load('file')
  loader.once('load', cb)
  loader.once('error', cb)
}
```

Ironically, the prototype feature makes this module twice as
complicated as necessary.

To check whether you function has been called, use `fn.called`. Once the
function is called for the first time the return value of the original
function is saved in `fn.value` and subsequent calls will continue to
return this value.

```javascript
var once = require('once')

function load (cb) {
  cb = once(cb)
  var stream = createStream()
  stream.once('data', cb)
  stream.once('end', function () {
    if (!cb.called) cb(new Error('not found'))
  })
}
```

## `once.strict(func)`

Throw an error if the function is called twice.

Some functions are expected to be called only once. Using `once` for them would
potentially hide logical errors.

In the example below, the `greet` function has to call the callback only once:

```javascript
function greet (name, cb) {
  // return is missing from the if statement
  // when no name is passed, the callback is called twice
  if (!name) cb('Hello anonymous')
  cb('Hello ' + name)
}

function log (msg) {
  console.log(msg)
}

// this will print 'Hello anonymous' but the logical error will be missed
greet(null, once(msg))

// once.strict will print 'Hello anonymous' and throw an error when the callback will be called the second time
greet(null, once.strict(msg))
```
# wrappy

Callback wrapping utility

## USAGE

```javascript
var wrappy = require("wrappy")

// var wrapper = wrappy(wrapperFunction)

// make sure a cb is called only once
// See also: http://npm.im/once for this specific use case
var once = wrappy(function (cb) {
  var called = false
  return function () {
    if (called) return
    called = true
    return cb.apply(this, arguments)
  }
})

function printBoo () {
  console.log('boo')
}
// has some rando property
printBoo.iAmBooPrinter = true

var onlyPrintOnce = once(printBoo)

onlyPrintOnce() // prints 'boo'
onlyPrintOnce() // does nothing

// random property is retained!
assert.equal(onlyPrintOnce.iAmBooPrinter, true)
```
# node-quick-temp

Create and remove temporary directories. Useful for build tools, like Broccoli
plugins. Smart about naming, and placing them in `./tmp` if possible, so you
don't have to worry about this.

## Installation

```bash
npm install --save quick-temp
```

## Usage

```js
var quickTemp = require('quick-temp');
```

### Creating a temporary directory

To make a temporary and assign its path to `this.tmpDestDir`, call either one
of these:

```js
quickTemp.makeOrRemake(this, 'tmpDestDir');
// or
quickTemp.makeOrReuse(this, 'tmpDestDir');
```

If `this.tmpDestDir` already contains a path, `makeOrRemake` will remove it
first and then create a new directory, whereas `makeOrReuse` will be a no-op.

Both functions also return the path of the temporary directory.

An optional third argument lets you override the class-name component of the
temporary directory name:

```js
quickTemp.makeOrRemake(this, 'tmpDestDir', 'TreeMerger');
quickTemp.makeOrRemake(this, 'tmpDestDir', this.constructor.name); // default
```

### Removing a temporary directory

To remove a previously-created temporary directory and all its contents, call

```js
quickTemp.remove(this, 'tmpDestDir');
```

This will also assign `this.tmpDestDir = null`. If `this.tmpDestDir` is
already null or undefined, it will be a no-op.
# mktemp

[![Build Status](https://travis-ci.org/sasaplus1/mktemp.svg)](https://travis-ci.org/sasaplus1/mktemp)
[![Dependency Status](https://gemnasium.com/sasaplus1/mktemp.svg)](https://gemnasium.com/sasaplus1/mktemp)
[![NPM version](https://badge.fury.io/js/mktemp.svg)](http://badge.fury.io/js/mktemp)

mktemp command for node.js

## Installation

```sh
$ npm install mktemp
```

## Usage

```js
var mktemp = require('mktemp');

mktemp.createFile('XXXXX.txt', function(err, path) {
  if (err) throw err;

  // path match a /^[\da-zA-Z]{5}\.txt$/
  console.log(path);
});

// return value match a /^[\da-zA-Z]{5}\.tmp$/
mktemp.createFileSync('XXXXX.tmp');

mktemp.createDir('XXXXXXX', function(err, path) {
  if (err) throw err;

  // path match a /^[\da-zA-Z]{7}$/
  console.log(path);
});

// return value match a /^XXX-[\da-zA-Z]{3}$/
mktemp.createDirSync('XXX-XXX');
```

if support Promise, can use Promise style.

```js
var mktemp = require('mktemp');

mktemp
  .createFile('XXXXX.txt')
  .then(function(path) {
    // path match a /^[\da-zA-Z]{5}\.txt$/
    console.log(path);
  })
  .catch(function(err) {
    console.error(err);
  });

mktemp
  .createDir('XXXXX')
  .then(function(path) {
    // path match a /^[\da-zA-Z]{5}$/
    console.log(path);
  })
  .catch(function(err) {
    console.error(err);
  });
```

mktemp functions are replace to random string from placeholder "X" in template. see example:

```js
mktemp.createFileSync('XXXXXXX');  // match a /^[\da-zA-Z]{7}$/
mktemp.createFileSync('XXX.tmp');  // match a /^[\da-zA-Z]{3}\.tmp$/
mktemp.createFileSync('XXX-XXX');  // match a /^XXX-[\da-zA-Z]{3}$/
```

## Functions

### createFile(template[, callback])

* `template`
  * `String` - filename template
* `callback`
  * `function(err, path)` - callback function
    * `err` : `Error|Null` - error object
    * `path` :  `String` -  path

create blank file of unique filename. permission is `0600`.

it throws TypeError if node.js unsupported Promise and callback is not a function.

### createFileSync(template)

* `template`
  * `String` - filename template
* `return`
  * `String` - path

sync version createFile.

### createDir(template[, callback])

* `template`
  * `String` - dirname template
* `callback`
  * `function(err, path)` - callback function
    * `err` : `Error|Null` - error object
    * `path` : `String` - path

create directory of unique dirname. permission is `0700`.

it throws TypeError if node.js unsupported Promise and callback is not a function.

### createDirSync(template)

* `template`
  * `String` - dirname template
* `return`
  * `String` - path

sync version createDir.

## Test

```sh
$ npm install
$ npm test
```

## Contributors

* [Michael Ficarra](https://github.com/michaelficarra)

## License

The MIT license. Please see LICENSE file.
# Underscore.string [![Build Status](https://secure.travis-ci.org/epeli/underscore.string.png?branch=master)](http://travis-ci.org/epeli/underscore.string) #



Javascript lacks complete string manipulation operations.
This an attempt to fill that gap. List of build-in methods can be found
for example from [Dive Into JavaScript][d].

[d]: http://www.diveintojavascript.com/core-javascript-reference/the-string-object


As name states this an extension for [Underscore.js][u], but it can be used
independently from **_s**-global variable. But with Underscore.js you can
use Object-Oriented style and chaining:

[u]: http://documentcloud.github.com/underscore/

```javascript
_("   epeli  ").chain().trim().capitalize().value()
=> "Epeli"
```

## Download ##

  * [Development version](https://raw.github.com/epeli/underscore.string/master/lib/underscore.string.js) *Uncompressed with Comments 18kb*
  * [Production version](https://github.com/epeli/underscore.string/raw/master/dist/underscore.string.min.js) *Minified 7kb*


## Node.js installation ##

**npm package**

    npm install underscore.string

**Standalone usage**:

```javascript
var _s = require('underscore.string');
```

**Integrate with Underscore.js**:

```javascript
var _  = require('underscore');

// Import Underscore.string to separate object, because there are conflict functions (include, reverse, contains)
_.str = require('underscore.string');

// Mix in non-conflict functions to Underscore namespace if you want
_.mixin(_.str.exports());

// All functions, include conflict, will be available through _.str object
_.str.include('Underscore.string', 'string'); // => true
```

**Or Integrate with Underscore.js without module loading**

Run the following expression after Underscore.js and Underscore.string are loaded
```javascript
// _.str becomes a global variable if no module loading is detected
// Mix in non-conflict functions to Underscore namespace
_.mixin(_.str.exports());
```

## String Functions ##

For availability of functions in this way you need to mix in Underscore.string functions:

```javascript
_.mixin(_.string.exports());
```

otherwise functions from examples will be available through _.string or _.str objects:

```javascript
_.str.capitalize('epeli')
=> "Epeli"
```

**numberFormat** _.numberFormat(number, [ decimals=0, decimalSeparator='.', orderSeparator=','])

Formats the numbers.

```javascript
_.numberFormat(1000, 2)
=> "1,000.00"

_.numberFormat(123456789.123, 5, '.', ',')
=> "123,456,789.12300"
```


**levenshtein** _.levenshtein(string1, string2)

Calculates [Levenshtein distance][ld] between two strings.
[ld]: http://en.wikipedia.org/wiki/Levenshtein_distance

```javascript
_.levenshtein('kitten', 'kittah')
=> 2
```

**capitalize** _.capitalize(string)

Converts first letter of the string to uppercase.

```javascript
_.capitalize("foo Bar")
=> "Foo Bar"
```

**chop** _.chop(string, step)

```javascript
_.chop('whitespace', 3)
=> ['whi','tes','pac','e']
```

**clean** _.clean(str)

Compress some whitespaces to one.

```javascript
_.clean(" foo    bar   ")
=> 'foo bar'
```

**chars** _.chars(str)

```javascript
_.chars('Hello')
=> ['H','e','l','l','o']
```

**swapCase** _.swapCase(str)

Returns a copy of the string in which all the case-based characters have had their case swapped.

```javascript
_.swapCase('hELLO')
=> 'Hello'
```

**include** available only through _.str object, because Underscore has function with the same name.

```javascript
_.str.include("foobar", "ob")
=> true
```

(removed) **includes** _.includes(string, substring)

Tests if string contains a substring.

```javascript
_.includes("foobar", "ob")
=> true
```

**includes** function was removed

But you can create it in this way, for compatibility with previous versions:

```javascript
_.includes = _.str.include
```

**count** _.count(string, substring)

```javascript
_('Hello world').count('l')
=> 3
```

**escapeHTML** _.escapeHTML(string)

Converts HTML special characters to their entity equivalents.

```javascript
_('<div>Blah blah blah</div>').escapeHTML();
=> '&lt;div&gt;Blah blah blah&lt;/div&gt;'
```

**unescapeHTML** _.unescapeHTML(string)

Converts entity characters to HTML equivalents.

```javascript
_('&lt;div&gt;Blah blah blah&lt;/div&gt;').unescapeHTML();
=> '<div>Blah blah blah</div>'
```

**insert** _.insert(string, index, substing)

```javascript
_('Hello ').insert(6, 'world')
=> 'Hello world'
```

**isBlank** _.isBlank(string)

```javascript
_('').isBlank(); // => true
_('\n').isBlank(); // => true
_(' ').isBlank(); // => true
_('a').isBlank(); // => false
```

**join** _.join(separator, *strings)

Joins strings together with given separator

```javascript
_.join(" ", "foo", "bar")
=> "foo bar"
```

**lines** _.lines(str)

```javascript
_.lines("Hello\nWorld")
=> ["Hello", "World"]
```

**reverse** available only through _.str object, because Underscore has function with the same name.

Return reversed string:

```javascript
_.str.reverse("foobar")
=> 'raboof'
```

**splice**  _.splice(string, index, howmany, substring)

Like a array splice.

```javascript
_('https://edtsech@bitbucket.org/edtsech/underscore.strings').splice(30, 7, 'epeli')
=> 'https://edtsech@bitbucket.org/epeli/underscore.strings'
```

**startsWith** _.startsWith(string, starts)

This method checks whether string starts with starts.

```javascript
_("image.gif").startsWith("image")
=> true
```

**endsWith** _.endsWith(string, ends)

This method checks whether string ends with ends.

```javascript
_("image.gif").endsWith("gif")
=> true
```

**succ**  _.succ(str)

Returns the successor to str.

```javascript
_('a').succ()
=> 'b'

_('A').succ()
=> 'B'
```

**supplant**

Supplant function was removed, use Underscore.js [template function][p].

[p]: http://documentcloud.github.com/underscore/#template

**strip** alias for *trim*

**lstrip** alias for *ltrim*

**rstrip** alias for *rtrim*

**titleize** _.titleize(string)

```javascript
_('my name is epeli').titleize()
=> 'My Name Is Epeli'
```

**camelize** _.camelize(string)

Converts underscored or dasherized string to a camelized one

```javascript
_('-moz-transform').camelize()
=> 'MozTransform'
```

**classify** _.classify(string)

Converts string to camelized class name

```javascript
_('some_class_name').classify()
=> 'SomeClassName'
```

**underscored** _.underscored(string)

Converts a camelized or dasherized string into an underscored one

```javascript
_('MozTransform').underscored()
=> 'moz_transform'
```

**dasherize** _.dasherize(string)

Converts a underscored or camelized string into an dasherized one

```javascript
_('MozTransform').dasherize()
=> '-moz-transform'
```

**humanize** _.humanize(string)

Converts an underscored, camelized, or dasherized string into a humanized one.
Also removes beginning and ending whitespace, and removes the postfix '_id'.

```javascript
_('  capitalize dash-CamelCase_underscore trim  ').humanize()
=> 'Capitalize dash camel case underscore trim'
```

**trim** _.trim(string, [characters])

trims defined characters from begining and ending of the string.
Defaults to whitespace characters.

```javascript
_.trim("  foobar   ")
=> "foobar"

_.trim("_-foobar-_", "_-")
=> "foobar"
```


**ltrim** _.ltrim(string, [characters])

Left trim. Similar to trim, but only for left side.


**rtrim** _.rtrim(string, [characters])

Right trim. Similar to trim, but only for right side.

**truncate** _.truncate(string, length, truncateString)

```javascript
_('Hello world').truncate(5)
=> 'Hello...'

_('Hello').truncate(10)
=> 'Hello'
```

**prune** _.prune(string, length, pruneString)

Elegant version of truncate.
Makes sure the pruned string does not exceed the original length.
Avoid half-chopped words when truncating.

```javascript
_('Hello, world').prune(5)
=> 'Hello...'

_('Hello, world').prune(8)
=> 'Hello...'

_('Hello, world').prune(5, ' (read a lot more)')
=> 'Hello, world' (as adding "(read a lot more)" would be longer than the original string)

_('Hello, cruel world').prune(15)
=> 'Hello, cruel...'

_('Hello').prune(10)
=> 'Hello'
```

**words** _.words(str, delimiter=/\s+/)

Split string by delimiter (String or RegExp), /\s+/ by default.

```javascript
_.words("   I   love   you   ")
=> ["I","love","you"]

_.words("I_love_you", "_")
=> ["I","love","you"]

_.words("I-love-you", /-/)
=> ["I","love","you"]

_.words("   ")
=> []
```

**sprintf** _.sprintf(string format, *arguments)

C like string formatting.
Credits goes to [Alexandru Marasteanu][o].
For more detailed documentation, see the [original page][o].

[o]: http://www.diveintojavascript.com/projects/sprintf-for-javascript

```javascript
_.sprintf("%.1f", 1.17)
"1.2"
```

**pad** _.pad(str, length, [padStr, type])

pads the `str` with characters until the total string length is equal to the passed `length` parameter. By default, pads on the **left** with the space char (`" "`). `padStr` is truncated to a single character if necessary.

```javascript
_.pad("1", 8)
-> "       1";

_.pad("1", 8, '0')
-> "00000001";

_.pad("1", 8, '0', 'right')
-> "10000000";

_.pad("1", 8, '0', 'both')
-> "00001000";

_.pad("1", 8, 'bleepblorp', 'both')
-> "bbbb1bbb";
```

**lpad** _.lpad(str, length, [padStr])

left-pad a string. Alias for `pad(str, length, padStr, 'left')`

```javascript
_.lpad("1", 8, '0')
-> "00000001";
```

**rpad** _.rpad(str, length, [padStr])

right-pad a string. Alias for `pad(str, length, padStr, 'right')`

```javascript
_.rpad("1", 8, '0')
-> "10000000";
```

**lrpad** _.lrpad(str, length, [padStr])

left/right-pad a string. Alias for `pad(str, length, padStr, 'both')`

```javascript
_.lrpad("1", 8, '0')
-> "00001000";
```

**center** alias for **lrpad**

**ljust** alias for *rpad*

**rjust** alias for *lpad*

**toNumber**  _.toNumber(string, [decimals])

Parse string to number. Returns NaN if string can't be parsed to number.

```javascript
_('2.556').toNumber()
=> 3

_('2.556').toNumber(1)
=> 2.6
```

**strRight**  _.strRight(string, pattern)

Searches a string from left to right for a pattern and returns a substring consisting of the characters in the string that are to the right of the pattern or all string if no match found.

```javascript
_('This_is_a_test_string').strRight('_')
=> "is_a_test_string";
```

**strRightBack**  _.strRightBack(string, pattern)

Searches a string from right to left for a pattern and returns a substring consisting of the characters in the string that are to the right of the pattern or all string if no match found.

```javascript
_('This_is_a_test_string').strRightBack('_')
=> "string";
```

**strLeft**  _.strLeft(string, pattern)

Searches a string from left to right for a pattern and returns a substring consisting of the characters in the string that are to the left of the pattern or all string if no match found.

```javascript
_('This_is_a_test_string').strLeft('_')
=> "This";
```

**strLeftBack**  _.strLeftBack(string, pattern)

Searches a string from right to left for a pattern and returns a substring consisting of the characters in the string that are to the left of the pattern or all string if no match found.

```javascript
_('This_is_a_test_string').strLeftBack('_')
=> "This_is_a_test";
```

**stripTags**

Removes all html tags from string.

```javascript
_('a <a href="#">link</a>').stripTags()
=> 'a link'

_('a <a href="#">link</a><script>alert("hello world!")</script>').stripTags()
=> 'a linkalert("hello world!")'
```

**toSentence**  _.toSentence(array, [delimiter, lastDelimiter])

Join an array into a human readable sentence.

```javascript
_.toSentence(['jQuery', 'Mootools', 'Prototype'])
=> 'jQuery, Mootools and Prototype';

_.toSentence(['jQuery', 'Mootools', 'Prototype'], ', ', ' unt ')
=> 'jQuery, Mootools unt Prototype';
```

**toSentenceSerial**  _.toSentenceSerial(array, [delimiter, lastDelimiter])

The same as `toSentence`, but adjusts delimeters to use [Serial comma](http://en.wikipedia.org/wiki/Serial_comma).

```javascript
_.toSentenceSerial(['jQuery', 'Mootools'])
=> 'jQuery and Mootools';

_.toSentenceSerial(['jQuery', 'Mootools', 'Prototype'])
=> 'jQuery, Mootools, and Prototype'

_.toSentenceSerial(['jQuery', 'Mootools', 'Prototype'], ', ', ' unt ');
=> 'jQuery, Mootools, unt Prototype';
```

**repeat** _.repeat(string, count, [separator])

Repeats a string count times.

```javascript
_.repeat("foo", 3)
=> 'foofoofoo';

_.repeat("foo", 3, "bar")
=> 'foobarfoobarfoo'
```

**surround** _.surround(string, wrap)

Surround a string with another string.

```javascript
_.surround("foo", "ab")
=> 'abfooab';
```

**quote** _.quote(string, quoteChar) or _.q(string, quoteChar)

Quotes a string. `quoteChar` defaults to `"`.

```javascript
_.quote('foo', quoteChar)
=> '"foo"';
```
**unquote** _.unquote(string, quoteChar)

Unquotes a string. `quoteChar` defaults to `"`.

```javascript
_.unquote('"foo"')
=> 'foo';
_.unquote("'foo'", "'")
=> 'foo';
```


**slugify** _.slugify(string)

Transform text into a URL slug. Replaces whitespaces, accentuated, and special characters with a dash.

```javascript
_.slugify("Un éléphant à l'orée du bois")
=> 'un-elephant-a-loree-du-bois';
```

***Caution: this function is charset dependent***

**naturalCmp** array.sort(_.naturalCmp)

Naturally sort strings like humans would do.

```javascript
['foo20', 'foo5'].sort(_.naturalCmp)
=> [ 'foo5', 'foo20' ]
```

**toBoolean** _.toBoolean(string) or _.toBool(string)

Turn strings that can be commonly considered as booleas to real booleans. Such as "true", "false", "1" and "0". This function is case insensitive.

```javascript
_.toBoolean("true")
=> true
_.toBoolean("FALSE")
=> false
_.toBoolean("random")
=> undefined
```

It can be customized by giving arrays of truth and falsy value matcher as parameters. Matchers can be also RegExp objects.

```javascript
_.toBoolean("truthy", ["truthy"], ["falsy"])
=> true
_.toBoolean("true only at start", [/^true/])
=> true
```

## Roadmap ##

Any suggestions or bug reports are welcome. Just email me or more preferably open an issue.

#### Problems

We lose two things for `include` and `reverse` methods from `_.string`:

* Calls like `_('foobar').include('bar')` aren't available;
* Chaining isn't available too.

But if you need this functionality you can create aliases for conflict functions which will be convenient for you:

```javascript
_.mixin({
    includeString: _.str.include,
    reverseString: _.str.reverse
})

// Now wrapper calls and chaining are available.
_('foobar').chain().reverseString().includeString('rab').value()
```

#### Standalone Usage

If you are using Underscore.string without Underscore. You also have `_.string` namespace for it and `_.str` alias
But of course you can just reassign `_` variable with `_.string`

```javascript
_ = _.string
```

## Changelog ##

### 2.3.3 ###

* Add `toBoolean`
* Add `unquote`
* Add quote char option to `quote`
* Support dash-separated words in `titleize`

### 2.3.2 ###

* Add `naturalCmp`
* Bug fix to `camelize`
* Add ă, ș, ț and ś to `slugify`
* Doc updates
* Add support for [component](http://component.io/)
* [Full changelog](https://github.com/epeli/underscore.string/compare/v2.3.1...v2.3.2)

### 2.3.1 ###

* Bug fixes to `escapeHTML`, `classify`, `substr`
* Faster `count`
* Documentation fixes
* [Full changelog](https://github.com/epeli/underscore.string/compare/v2.3.0...v2.3.1)

### 2.3.0 ###

* Added `numberformat` method
* Added `levenshtein` method (Levenshtein distance calculation)
* Added `swapCase` method
* Changed default behavior of `words` method
* Added `toSentenceSerial` method
* Added `surround` and `quote` methods

### 2.2.1 ###

* Same as 2.2.0 (2.2.0rc on npm) to fix some npm drama

### 2.2.0 ###

* Capitalize method behavior changed
* Various perfomance tweaks

### 2.1.1###

* Fixed words method bug
* Added classify method

### 2.1.0 ###

* AMD support
* Added toSentence method
* Added slugify method
* Lots of speed optimizations

### 2.0.0 ###

* Added prune, humanize functions
* Added _.string (_.str) namespace for Underscore.string library
* Removed includes function

For upgrading to this version you need to mix in Underscore.string library to Underscore object:

```javascript
_.mixin(_.string.exports());
```

and all non-conflict Underscore.string functions will be available through Underscore object.
Also function `includes` has been removed, you should replace this function by `_.str.include`
or create alias `_.includes = _.str.include` and all your code will work fine.

### 1.1.6 ###

* Fixed reverse and truncate
* Added isBlank, stripTags, inlude(alias for includes)
* Added uglifier compression

### 1.1.5 ###

* Added strRight, strRightBack, strLeft, strLeftBack

### 1.1.4 ###

* Added pad, lpad, rpad, lrpad methods and aliases center, ljust, rjust
* Integration with Underscore 1.1.6

### 1.1.3 ###

* Added methods: underscored, camelize, dasherize
* Support newer version of npm

### 1.1.2 ###

* Created functions: lines, chars, words functions

### 1.0.2 ###

* Created integration test suite with underscore.js 1.1.4 (now it's absolutely compatible)
* Removed 'reverse' function, because this function override underscore.js 'reverse'

## Contribute ##

* Fork & pull request. Don't forget about tests.
* If you planning add some feature please create issue before.

Otherwise changes will be rejected.

## Contributors list ##
[Can be found here](https://github.com/epeli/underscore.string/graphs/contributors).


## Licence ##

The MIT License

Copyright (c) 2011 Esa-Matti Suuronen esa-matti@suuronen.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
`rm -rf` for node.

Install with `npm install rimraf`, or just drop rimraf.js somewhere.

## API

`rimraf(f, callback)`

The callback will be called with an error if there is one.  Certain
errors are handled for you:

* Windows: `EBUSY` and `ENOTEMPTY` - rimraf will back off a maximum of
  `opts.maxBusyTries` times before giving up.
* `ENOENT` - If the file doesn't exist, rimraf will return
  successfully, since your desired outcome is already the case.

## rimraf.sync

It can remove stuff synchronously, too.  But that's not so good.  Use
the async API.  It's better.

## CLI

If installed with `npm install rimraf -g` it can be used as a global
command `rimraf <path>` which is useful for cross platform support.

## mkdirp

If you need to create a directory recursively, check out
[mkdirp](https://github.com/substack/node-mkdirp).
# node-walk-sync

[![Build Status](https://travis-ci.org/joliss/node-walk-sync.png?branch=master)](https://travis-ci.org/joliss/node-walk-sync)
[![Build status](https://ci.appveyor.com/api/projects/status/sqe785gqb2qfmxbx/branch/master?svg=true)](https://ci.appveyor.com/project/joliss/node-walk-sync/branch/master)

Return an array containing all recursive files and directories under a given
directory, similar to Unix `find`. Follows symlinks. Bare-bones, but
very fast.

Similar to [`wrench.readdirSyncRecursive`](https://github.com/ryanmcgrath/wrench-js#synchronous-operations),
but adds trailing slashes to directories.

Not to be confused with [node-walk](https://github.com/coolaj86/node-walk),
which has both an asynchronous and a synchronous API.

## Installation

```bash
npm install --save walk-sync
```

## Usage

```js
var walkSync = require('walk-sync');
var paths = walkSync('project')
```

Given `project/one.txt` and `project/subdir/two.txt`, `paths` will be the following
array:

```js
['one.txt', 'subdir/', 'subdir/two.txt']
```

Directories come before their contents, and have a trailing forward-slash (on
all platforms).

Symlinks are followed.

### Entries

Sometimes, it is important to get additional information from a walk of a
directory; for instance if the downstream consumer needs to stat the files we
can leverage the stats from the walk.

To accommodate, `walkSync.entries(path [, options])` is also provided, instead
of returning a list of files and/or directories it returns an array of objects
which correspond to a given file or directory, except with more data.

```
entry.relativePath
entry.mode  // => fs.statSync(fullPath).mode
entry.size  // => fs.statSync(fullPath).size
entry.mtime // => fs.statSync(fullPath).mtime.getTime()

entry.isDirectory() // => true if directory
```

### Options

* `globs`: An array of globs. Only files and directories that match at least
  one of the provided globs will be returned.

    ```js
    var paths = walkSync('project', { globs: ['subdir/**/*.txt'] });
    // => ['subdir/two.txt']
    ```

    As an alternative to string globs, you can pass an array of precompiled
    [`minimatch.Minimatch`](https://github.com/isaacs/minimatch#minimatch-class)
    instances. This is faster and allows to specify your own globbing options.

* `directories` (default: true): Pass `false` to only return files, not
  directories:

    ```js
    var paths = walkSync('project', { directories: false })
    // => ['one.txt', 'subdir/two.txt']
    ```

* `ignore`: An array of globs. Files and directories that match at least one
  of the provided globs will be pruned while searching.

    ```js
    var paths = walkSync('project', { ignore: ['subdir'] })
    // => ['one.txt']
    ```

## Background

`walkSync(baseDir)` is a faster substitute for

```js
glob.sync('**', {
  cwd: baseDir,
  dot: true,
  mark: true,
  strict: true
})
```
# ensure-posix-path

[![Build Status](https://travis-ci.org/stefanpenner/ensure-posix-path.svg)](https://travis-ci.org/stefanpenner/ensure-posix-path)
[![Build status](https://ci.appveyor.com/api/projects/status/bt015k54b2ohk1oi?svg=true)](https://ci.appveyor.com/project/embercli/ensure-posix-path)
#broccoli-asset-rewrite

[![CircleCI](https://img.shields.io/circleci/project/rickharrison/broccoli-asset-rewrite.svg)](https://circleci.com/gh/rickharrison/broccoli-asset-rewrite)
[![codecov.io](https://codecov.io/github/rickharrison/broccoli-asset-rewrite/coverage.svg?branch=master&precision=2)](https://codecov.io/github/rickharrison/broccoli-asset-rewrite?branch=master)
[![npm](https://img.shields.io/npm/v/broccoli-asset-rewrite.svg)](https://www.npmjs.com/package/broccoli-asset-rewrite)

[Broccoli](https://github.com/broccolijs/broccoli) plugin to rewrite a source node from an asset map.

Turns

```
<script src="assets/appname.js">
background: url('/images/foo.png');
```

Into

```
<script src="https://subdomain.cloudfront.net/assets/appname-342b0f87ea609e6d349c7925d86bd597.js">
background: url('https://subdomain.cloudfront.net/images/foo-735d6c098496507e26bb40ecc8c1394d.png');
```

## Installation

```js
npm install broccoli-asset-rewrite --save-dev
```

## Usage

The asset map should have keys of the original names and values of the new names.

```js
var AssetRewrite = require('broccoli-asset-rewrite');

var generatedMap = {
  'assets/appname.css': 'assets/appname-d1d59e0fdcfc183415ab0b72a4f78d9c.css',
  'assets/appname.js': 'assets/appname-ed50537fcd5a71113cf79908f49e854d.js',
  'assets/vendor.css': 'assets/vendor-d41d8cd98f00b204e9800998ecf8427e.css',
  'logo.png': 'logo-c4ab8191636f0a520d1f7f7a82c455a3.png'
};

var assetNode = new AssetRewrite(node, {
  assetMap: generatedMap,
  replaceExtensions: ['html', 'js', 'css'],
  prepend: 'https://subdomain.cloudfront.net/'
});
```

## Options

  - `assetMap` - Default: `{}` - The asset map to rewrite source from.
  - `replaceExtensions` - Default: `['html', 'css']` - The file types to replace source code with new checksum file names.
  - `prepend` - Default: `''` - A string to prepend to all of the assets. Useful for CDN urls like `https://subdomain.cloudfront.net/`
  - `ignore` - Default: `[]` - Ignore files from being rewritten.
  - `annotation` - Default: null - A human-readable description for this plugin instance.

[![ghit.me](https://ghit.me/badge.svg?repo=rickharrison/broccoli-asset-rewrite)](https://ghit.me/repo/rickharrison/broccoli-asset-rewrite)
# RSVP.js  [![Build Status](https://secure.travis-ci.org/tildeio/rsvp.js.png?branch=master)](http://travis-ci.org/tildeio/rsvp.js) [![Inline docs](http://inch-ci.org/github/tildeio/rsvp.js.svg?branch=master)](http://inch-ci.org/github/tildeio/rsvp.js)

RSVP.js provides simple tools for organizing asynchronous code.

Specifically, it is a tiny implementation of Promises/A+.

It works in node and the browser (IE6+, all the popular evergreen ones).

## downloads

- [rsvp-latest](http://rsvpjs-builds.s3.amazonaws.com/rsvp-latest.js)
- [rsvp-latest (minified)](http://rsvpjs-builds.s3.amazonaws.com/rsvp-latest.min.js)

## Promises

Although RSVP is es6 compliant, it does bring along some extra toys. If you would prefer a strict es6 subset, I would suggest checking out our sibling project https://github.com/stefanpenner/es6-promise, It is RSVP but stripped down to the es6 spec features.

## Bower

`bower install -S rsvp`

## NPM

`npm install --save rsvp`

`RSVP.Promise` is an implementation of
[Promises/A+](http://promises-aplus.github.com/promises-spec/) that passes the
[test suite](https://github.com/promises-aplus/promises-tests).

It delivers all promises asynchronously, even if the value is already
available, to help you write consistent code that doesn't change if the
underlying data provider changes from synchronous to asynchronous.

It is compatible with [TaskJS](http://taskjs.org/), a library by Dave
Herman of Mozilla that uses ES6 generators to allow you to write
synchronous code with promises. It currently works in Firefox, and will
work in any browser that adds support for ES6 generators. See the
section below on TaskJS for more information.

### Basic Usage

```javascript
var RSVP = require('rsvp');

var promise = new RSVP.Promise(function(resolve, reject) {
  // succeed
  resolve(value);
  // or reject
  reject(error);
});

promise.then(function(value) {
  // success
}).catch(function(error) {
  // failure
});
```

Once a promise has been resolved or rejected, it cannot be resolved or
rejected again.

Here is an example of a simple XHR2 wrapper written using RSVP.js:

```javascript
var getJSON = function(url) {
  var promise = new RSVP.Promise(function(resolve, reject){
    var client = new XMLHttpRequest();
    client.open("GET", url);
    client.onreadystatechange = handler;
    client.responseType = "json";
    client.setRequestHeader("Accept", "application/json");
    client.send();

    function handler() {
      if (this.readyState === this.DONE) {
        if (this.status === 200) { resolve(this.response); }
        else { reject(this); }
      }
    };
  });

  return promise;
};

getJSON("/posts.json").then(function(json) {
  // continue
}).catch(function(error) {
  // handle errors
});
```

### Chaining

One of the really awesome features of Promises/A+ promises are that they
can be chained together. In other words, the return value of the first
resolve handler will be passed to the second resolve handler.

If you return a regular value, it will be passed, as is, to the next
handler.

```javascript
getJSON("/posts.json").then(function(json) {
  return json.post;
}).then(function(post) {
  // proceed
});
```

The really awesome part comes when you return a promise from the first
handler:

```javascript
getJSON("/post/1.json").then(function(post) {
  // save off post
  return getJSON(post.commentURL);
}).then(function(comments) {
  // proceed with access to post and comments
});
```

This allows you to flatten out nested callbacks, and is the main feature
of promises that prevents "rightward drift" in programs with a lot of
asynchronous code.

Errors also propagate:

```javascript
getJSON("/posts.json").then(function(posts) {

}).catch(function(error) {
  // since no rejection handler was passed to the
  // first `.then`, the error propagates.
});
```

You can use this to emulate `try/catch` logic in synchronous code.
Simply chain as many resolve callbacks as a you want, and add a failure
handler at the end to catch errors.

```javascript
getJSON("/post/1.json").then(function(post) {
  return getJSON(post.commentURL);
}).then(function(comments) {
  // proceed with access to posts and comments
}).catch(function(error) {
  // handle errors in either of the two requests
});
```

## Error Handling

There are times when dealing with promises that it seems like any errors
are being 'swallowed', and not properly raised. This makes it extremely
difficult to track down where a given issue is coming from. Thankfully,
`RSVP` has a solution for this problem built in.

You can register functions to be called when an uncaught error occurs
within your promises. These callback functions can be anything, but a common
practice is to call `console.assert` to dump the error to the console.

```javascript
RSVP.on('error', function(reason) {
  console.assert(false, reason);
});
```

`RSVP` allows Promises to be labeled: `Promise.resolve(value, 'I AM A LABEL')`
If provided, this label is passed as the second argument to `RSVP.on('error')`

```javascript
RSVP.on('error', function(reason, label) {
  if (label) {
    console.error(label);
  }

  console.assert(false, reason);
});
```


**NOTE:** promises do allow for errors to be handled asynchronously, so
this callback may result in false positives.

**NOTE:** Usage of `RSVP.configure('onerror', yourCustomFunction);` is
deprecated in favor of using `RSVP.on`.


## Finally

`finally` will be invoked regardless of the promise's fate, just as native
try/catch/finally behaves.

```js
findAuthor().catch(function(reason){
  return findOtherAuthor();
}).finally(function(){
  // author was either found, or not
});
```


## Arrays of promises

Sometimes you might want to work with many promises at once. If you
pass an array of promises to the `all()` method it will return a new
promise that will be fulfilled when all of the promises in the array
have been fulfilled; or rejected immediately if any promise in the array
is rejected.

```javascript
var promises = [2, 3, 5, 7, 11, 13].map(function(id){
  return getJSON("/post/" + id + ".json");
});

RSVP.all(promises).then(function(posts) {
  // posts contains an array of results for the given promises
}).catch(function(reason){
  // if any of the promises fails.
});
```

## Hash of promises

If you need to reference many promises at once (like `all()`), but would like
to avoid encoding the actual promise order you can use `hash()`. If you pass
an object literal (where the values are promises) to the `hash()` method it will
return a new promise that will be fulfilled when all of the promises have been
fulfilled; or rejected immediately if any promise is rejected.

The key difference to the `all()` function is that both the fulfillment value
and the argument to the `hash()` function are object literals. This allows
you to simply reference the results directly off the returned object without
having to remember the initial order like you would with `all()`.

```javascript
var promises = {
  posts: getJSON("/posts.json"),
  users: getJSON("/users.json")
};

RSVP.hash(promises).then(function(results) {
  console.log(results.users) // print the users.json results
  console.log(results.posts) // print the posts.json results
});
```

## All settled and hash settled

Sometimes you want to work with several promises at once, but instead of
rejecting immediately if any promise is rejected, as with `all()` or `hash()`,
you want to be able to inspect the results of all your promises, whether
they fulfill or reject. For this purpose, you can use `allSettled()` and
`hashSettled()`. These work exactly like `all()` and `hash()`, except that
they fulfill with an array or hash (respectively) of the constituent promises'
result states. Each state object will either indicate fulfillment or
rejection, and provide the corresponding value or reason. The states will take
one of the following formats:

```javascript
{ state: 'fulfilled', value: value }
  or
{ state: 'rejected', reason: reason }
```

## Deferred

> The `RSVP.Promise` constructor is generally a better, less error-prone choice
> than `RSVP.defer()`. Promises are recommended unless the specific
> properties of deferred are needed.

Sometimes one needs to create a deferred object, without immediately specifying
how it will be resolved. These deferred objects are essentially a wrapper around
a promise, whilst providing late access to the `resolve()` and `reject()` methods.

A deferred object has this form: `{ promise, resolve(x), reject(r) }`.

```javascript
var deferred = RSVP.defer();
// ...
deferred.promise // access the promise
// ...
deferred.resolve();

```

## TaskJS

The [TaskJS](http://taskjs.org/) library makes it possible to take
promises-oriented code and make it synchronous using ES6 generators.

Let's review an earlier example:

```javascript
getJSON("/post/1.json").then(function(post) {
  return getJSON(post.commentURL);
}).then(function(comments) {
  // proceed with access to posts and comments
}).catch(function(reason) {
  // handle errors in either of the two requests
});
```

Without any changes to the implementation of `getJSON`, you could write
the following code with TaskJS:

```javascript
spawn(function *() {
  try {
    var post = yield getJSON("/post/1.json");
    var comments = yield getJSON(post.commentURL);
  } catch(error) {
    // handle errors
  }
});
```

In the above example, `function *` is new syntax in ES6 for
[generators](http://wiki.ecmascript.org/doku.php?id=harmony:generators).
Inside a generator, `yield` pauses the generator, returning control to
the function that invoked the generator. In this case, the invoker is a
special function that understands the semantics of Promises/A, and will
automatically resume the generator as soon as the promise is resolved.

The cool thing here is the same promises that work with current
JavaScript using `.then` will work seamlessly with TaskJS once a browser
has implemented it!

## Instrumentation

```js
function listener (event) {
  event.guid      // guid of promise. Must be globally unique, not just within the implementation
  event.childGuid // child of child promise (for chained via `then`)
  event.eventName // one of ['created', 'chained', 'fulfilled', 'rejected']
  event.detail    // fulfillment value or rejection reason, if applicable
  event.label     // label passed to promise's constructor
  event.timeStamp // milliseconds elapsed since 1 January 1970 00:00:00 UTC up until now
  event.stack     // stack at the time of the event. (if  'instrument-with-stack' is true)
}

RSVP.configure('instrument', true | false);
// capturing the stacks is slow, so you also have to opt in
RSVP.configure('instrument-with-stack', true | false);

// events
RSVP.on('created', listener);
RSVP.on('chained', listener);
RSVP.on('fulfilled', listener);
RSVP.on('rejected', listener);
```

Events are only triggered when `RSVP.configure('instrument')` is true, although
listeners can be registered at any time.

## Building & Testing

Custom tasks:

* `npm test` - build & test
* `npm test:node` - build & test just node
* `npm test:server` - build/watch & test
* `npm run build` - Build
* `npm run build:production` - Build production (with minified output)
* `npm start` - build, watch and run interactive server at http://localhost:4200'

## Releasing

Check what release-it will do by running `npm run-script dry-run-release`.
To actually release, run `node_modules/.bin/release-it`.
loader.js [![Build Status](https://travis-ci.org/ember-cli/loader.js.png?branch=master)](https://travis-ci.org/ember-cli/loader.js)
=========

Minimal AMD loader mostly stolen from [@wycats](https://github.com/wycats).

## No Conflict

To prevent the loader from overriding `require`, `define`, or `requirejs` you can instruct the loader
to use no conflict mode by providing it an alternative name for the various globals that are normally used.

Example:

```js
loader.noConflict({
  define: 'newDefine',
  require: 'newRequire'
});
```

Note: To be able to take advantage of alternate `define` method name, you will also need to ensure that your
build tooling generates using the alternate.  An example of this is done in the [emberjs-build](https://github.com/emberjs/emberjs-build)
project in the [babel-enifed-module-formatter plugin](https://github.com/emberjs/emberjs-build/blob/v0.4.2/lib/utils/babel-enifed-module-formatter.js).

## wrapModules

It is possible to hook loader to augment or transform the loaded code.  `wrapModules` is an optional method on the loader that is called as each module is originally loaded.  `wrapModules` must be a function of the form `wrapModules(name, callback)`. The `callback` is the original AMD callback.  The return value of `wrapModules` is then used in subsequent requests for `name`

This functionality is useful for instrumenting code, for instance in code coverage libraries.

```js
loader.wrapModules = function(name, callback) {
            if (shouldTransform(name) {
                    return myTransformer(name, callback);
                }
            }
            return callback;
    };
```

## Tests

We use [testem](https://github.com/airportyh/testem) for running our test suite.

You may run them with:
```sh
npm test
```

You can also launch testem development mode with:
```sh
npm run test:dev
```

## License

loader.js is [MIT Licensed](https://github.com/ember-cli/loader.js/blob/master/LICENSE.md).
