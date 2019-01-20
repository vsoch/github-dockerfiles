
creating a new keymap file.

The names of the files are

km-xxxx.ini

where the xxx is replaces ny the hex number of the layout of interest.

The files have 5 section

[noshift], [shift], [altgr], [capslock], [shiftcapslock]

In each section there are multiple lines for each key
An example line looks like

Key10=49:49

In this line, 10 is the X11 scancode, the first 49 is the keysym value,
the second 49 if the unicode value of the key.  This is the definition
for the 'noshift' '1' key on a en-us keyboard.  In this case, the keysym
and the unicode value are the same.  Here is an example where they are
not.
This is the definition for the backspace key.
Key22=65288:8

And this is the star on the keypad
Key63=65450:42

To create a new file run xrdp-genkeymap filename

Example ./xrdp-genkeymap /etc/xrdp/km-0409.ini

Note: You need to have rights to the /etc/xrdp directory.

Utilities directory
-------------------

'utils' contains general purpose code not strictly dependent on RDP
protocol

Syntaxic Sugar
--------------

'sugar' gather simple syntaxic sugar used as common C++ extension.

# Install Emscripten

http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html

## Download

```bash
wget 'https://github.com/juj/emsdk/archive/master.zip' -Oemsdk-master.zip
unzip emsdk-master.zip
cd emsdk-master/
./emsdk install latest
```

## Setting

```bash
./emsdk activate latest
./emsdk_env.sh
```

## Environment

```bash
source ./emsdk_set_env.sh
```

## Update

```bash
./emsdk update
./emsdk install latest
./emsdk activate latest
./emsdk_env.sh
```

# Transpilation

```bash
em++ file.cpp -o file.html
```

## Options

`--preload-file path1`

`--embed-file path1`

`--exclude-file path1`

`-O1`, `-O2`, `-O3`

# Include path

```bash
ln -s /usr/include/boost system_include/
```

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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
# Benchmark.js <sup>v1.0.0</sup>

A [robust](http://calendar.perfplanet.com/2010/bulletproof-javascript-benchmarks/ "Bulletproof JavaScript benchmarks") benchmarking library that works on nearly all JavaScript platforms<sup><a name="fnref1" href="#fn1">1</a></sup>, supports high-resolution timers, and returns statistically significant results. As seen on [jsPerf](http://jsperf.com/).

## BestieJS

Benchmark.js is part of the BestieJS *"Best in Class"* module collection. This means we promote solid browser/environment support, ES5 precedents, unit testing, and plenty of documentation.

## Documentation

The documentation for Benchmark.js can be viewed here: <http://benchmarkjs.com/docs>

For a list of upcoming features, check out our [roadmap](https://github.com/bestiejs/benchmark.js/wiki/Roadmap).

## Support

Benchmark.js has been tested in at least Adobe AIR 3.1, Chrome 5-21, Firefox 1.5-13, IE 6-9, Opera 9.25-12.01, Safari 3-6, Node.js 0.8.6, Narwhal 0.3.2, RingoJS 0.8, and Rhino 1.7RC5.

## Installation and usage

In a browser or Adobe AIR:

~~~ html
<script src="benchmark.js"></script>
~~~

Optionally, expose Java’s nanosecond timer by adding the `nano` applet to the `<body>`:

~~~ html
<applet code="nano" archive="nano.jar"></applet>
~~~

Or enable Chrome’s microsecond timer by using the [command line switch](http://peter.sh/experiments/chromium-command-line-switches/#enable-benchmarking):

    --enable-benchmarking

Via [npm](http://npmjs.org/):

~~~ bash
npm install benchmark
~~~

In [Node.js](http://nodejs.org/) and [RingoJS v0.8.0+](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark');
~~~

Optionally, use the [microtime module](https://github.com/wadey/node-microtime) by Wade Simmons:

~~~ bash
npm install microtime
~~~

In [RingoJS v0.7.0-](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark').Benchmark;
~~~

In [Rhino](http://www.mozilla.org/rhino/):

~~~ js
load('benchmark.js');
~~~

In an AMD loader like [RequireJS](http://requirejs.org/):

~~~ js
require({
  'paths': {
    'benchmark': 'path/to/benchmark'
  }
},
['benchmark'], function(Benchmark) {
  console.log(Benchmark.version);
});

// or with platform.js
// https://github.com/bestiejs/platform.js
require({
  'paths': {
    'benchmark': 'path/to/benchmark',
    'platform': 'path/to/platform'
  }
},
['benchmark', 'platform'], function(Benchmark, platform) {
  Benchmark.platform = platform;
  console.log(Benchmark.platform.name);
});
~~~

Usage example:

~~~ js
var suite = new Benchmark.Suite;

// add tests
suite.add('RegExp#test', function() {
  /o/.test('Hello World!');
})
.add('String#indexOf', function() {
  'Hello World!'.indexOf('o') > -1;
})
// add listeners
.on('cycle', function(event) {
  console.log(String(event.target));
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
// run async
.run({ 'async': true });

// logs:
// > RegExp#test x 4,161,532 +-0.99% (59 cycles)
// > String#indexOf x 6,139,623 +-1.00% (131 cycles)
// > Fastest is String#indexOf
~~~

## Authors

* [Mathias Bynens](http://mathiasbynens.be/)
  [![twitter/mathias](http://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter")
* [John-David Dalton](http://allyoucanleet.com/)
  [![twitter/jdalton](http://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter")

## Contributors

* [Kit Cambridge](http://kitcambridge.github.com/)
  [![twitter/kitcambridge](http://gravatar.com/avatar/6662a1d02f351b5ef2f8b4d815804661?s=70)](https://twitter.com/kitcambridge "Follow @kitcambridge on Twitter")
# Benchmark.js <sup>v1.0.0</sup>

<!-- div -->


<!-- div -->

## <a id="Benchmark"></a>`Benchmark`
* [`Benchmark`](#benchmarkname-fn--options)
* [`Benchmark.version`](#benchmarkversion)
* [`Benchmark.deepClone`](#benchmarkdeepclonevalue)
* [`Benchmark.each`](#benchmarkeachobject-callback-thisarg)
* [`Benchmark.extend`](#benchmarkextenddestination--source)
* [`Benchmark.filter`](#benchmarkfilterarray-callback-thisarg)
* [`Benchmark.forEach`](#benchmarkforeacharray-callback-thisarg)
* [`Benchmark.formatNumber`](#benchmarkformatnumbernumber)
* [`Benchmark.forOwn`](#benchmarkforownobject-callback-thisarg)
* [`Benchmark.hasKey`](#benchmarkhaskeyobject-key)
* [`Benchmark.indexOf`](#benchmarkindexofarray-value--fromindex0)
* [`Benchmark.interpolate`](#benchmarkinterpolatestring-object)
* [`Benchmark.invoke`](#benchmarkinvokebenches-name--arg1-arg2-)
* [`Benchmark.join`](#benchmarkjoinobject--separator1--separator2:)
* [`Benchmark.map`](#benchmarkmaparray-callback-thisarg)
* [`Benchmark.pluck`](#benchmarkpluckarray-property)
* [`Benchmark.reduce`](#benchmarkreducearray-callback-accumulator)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype`
* [`Benchmark.prototype.aborted`](#benchmarkprototypeaborted)
* [`Benchmark.prototype.compiled`](#benchmarkprototypecompiled)
* [`Benchmark.prototype.count`](#benchmarkprototypecount)
* [`Benchmark.prototype.cycles`](#benchmarkprototypecycles)
* [`Benchmark.prototype.fn`](#benchmarkprototypefn)
* [`Benchmark.prototype.hz`](#benchmarkprototypehz)
* [`Benchmark.prototype.running`](#benchmarkprototyperunning)
* [`Benchmark.prototype.setup`](#benchmarkprototypesetup)
* [`Benchmark.prototype.teardown`](#benchmarkprototypeteardown)
* [`Benchmark.prototype.abort`](#benchmarkprototypeabort)
* [`Benchmark.prototype.clone`](#benchmarkprototypecloneoptions)
* [`Benchmark.prototype.compare`](#benchmarkprototypecompareother)
* [`Benchmark.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.prototype.reset`](#benchmarkprototypereset)
* [`Benchmark.prototype.run`](#benchmarkprototyperunoptions)
* [`Benchmark.prototype.toString`](#benchmarkprototypetostring)

<!-- /div -->


<!-- div -->

## `Benchmark.options`
* [`Benchmark.options`](#benchmarkoptions)
* [`Benchmark.options.async`](#benchmarkoptionsasync)
* [`Benchmark.options.defer`](#benchmarkoptionsdefer)
* [`Benchmark.options.delay`](#benchmarkoptionsdelay)
* [`Benchmark.options.id`](#benchmarkoptionsid)
* [`Benchmark.options.initCount`](#benchmarkoptionsinitcount)
* [`Benchmark.options.maxTime`](#benchmarkoptionsmaxtime)
* [`Benchmark.options.minSamples`](#benchmarkoptionsminsamples)
* [`Benchmark.options.minTime`](#benchmarkoptionsmintime)
* [`Benchmark.options.name`](#benchmarkoptionsname)
* [`Benchmark.options.onAbort`](#benchmarkoptionsonabort)
* [`Benchmark.options.onComplete`](#benchmarkoptionsoncomplete)
* [`Benchmark.options.onCycle`](#benchmarkoptionsoncycle)
* [`Benchmark.options.onError`](#benchmarkoptionsonerror)
* [`Benchmark.options.onReset`](#benchmarkoptionsonreset)
* [`Benchmark.options.onStart`](#benchmarkoptionsonstart)

<!-- /div -->


<!-- div -->

## `Benchmark.platform`
* [`Benchmark.platform`](#benchmarkplatform)
* [`Benchmark.platform.description`](#benchmarkplatformdescription)
* [`Benchmark.platform.layout`](#benchmarkplatformlayout)
* [`Benchmark.platform.manufacturer`](#benchmarkplatformmanufacturer)
* [`Benchmark.platform.name`](#benchmarkplatformname)
* [`Benchmark.platform.os`](#benchmarkplatformos)
* [`Benchmark.platform.prerelease`](#benchmarkplatformprerelease)
* [`Benchmark.platform.product`](#benchmarkplatformproduct)
* [`Benchmark.platform.version`](#benchmarkplatformversion)
* [`Benchmark.platform.toString`](#benchmarkplatformtostring)

<!-- /div -->


<!-- div -->

## `Benchmark.support`
* [`Benchmark.support`](#benchmarksupport)
* [`Benchmark.support.air`](#benchmarksupportair)
* [`Benchmark.support.argumentsClass`](#benchmarksupportargumentsclass)
* [`Benchmark.support.browser`](#benchmarksupportbrowser)
* [`Benchmark.support.charByIndex`](#benchmarksupportcharbyindex)
* [`Benchmark.support.charByOwnIndex`](#benchmarksupportcharbyownindex)
* [`Benchmark.support.decompilation`](#benchmarksupportdecompilation)
* [`Benchmark.support.descriptors`](#benchmarksupportdescriptors)
* [`Benchmark.support.getAllKeys`](#benchmarksupportgetallkeys)
* [`Benchmark.support.iteratesOwnLast`](#benchmarksupportiteratesownfirst)
* [`Benchmark.support.java`](#benchmarksupportjava)
* [`Benchmark.support.nodeClass`](#benchmarksupportnodeclass)
* [`Benchmark.support.timeout`](#benchmarksupporttimeout)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`
* [`Benchmark.prototype.error`](#benchmarkprototypeerror)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`
* [`Benchmark.prototype.stats`](#benchmarkprototypestats)
* [`Benchmark.prototype.stats.deviation`](#benchmark-statsdeviation)
* [`Benchmark.prototype.stats.mean`](#benchmark-statsmean)
* [`Benchmark.prototype.stats.moe`](#benchmark-statsmoe)
* [`Benchmark.prototype.stats.rme`](#benchmark-statsrme)
* [`Benchmark.prototype.stats.sample`](#benchmark-statssample)
* [`Benchmark.prototype.stats.sem`](#benchmark-statssem)
* [`Benchmark.prototype.stats.variance`](#benchmark-statsvariance)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`
* [`Benchmark.prototype.times`](#benchmarkprototypetimes)
* [`Benchmark.prototype.times.cycle`](#benchmark-timescycle)
* [`Benchmark.prototype.times.elapsed`](#benchmark-timeselapsed)
* [`Benchmark.prototype.times.period`](#benchmark-timesperiod)
* [`Benchmark.prototype.times.timeStamp`](#benchmark-timestimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`
* [`Benchmark.Deferred`](#benchmarkdeferredclone)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`
* [`Benchmark.Deferred.prototype.benchmark`](#benchmarkdeferredprototypebenchmark)
* [`Benchmark.Deferred.prototype.cycles`](#benchmarkdeferredprototypecycles)
* [`Benchmark.Deferred.prototype.elapsed`](#benchmarkdeferredprototypeelapsed)
* [`Benchmark.Deferred.prototype.resolve`](#benchmarkdeferredprototyperesolve)
* [`Benchmark.Deferred.prototype.timeStamp`](#benchmarkdeferredprototypetimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Event`
* [`Benchmark.Event`](#benchmarkeventtype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`
* [`Benchmark.Event.prototype.aborted`](#benchmarkeventprototypeaborted)
* [`Benchmark.Event.prototype.cancelled`](#benchmarkeventprototypecancelled)
* [`Benchmark.Event.prototype.result`](#benchmarkeventprototyperesult)
* [`Benchmark.Event.prototype.timeStamp`](#benchmarkeventprototypetimestamp)
* [`Benchmark.Event.prototype.type`](#benchmarkeventprototypetype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`
* [`Benchmark.Event.prototype.currentTarget`](#benchmarkeventprototypecurrenttarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`
* [`Benchmark.Event.prototype.target`](#benchmarkeventprototypetarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite`
* [`Benchmark.Suite`](#benchmarksuitename--options)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`
* [`Benchmark.Suite.prototype.aborted`](#benchmarksuiteprototypeaborted)
* [`Benchmark.Suite.prototype.length`](#benchmarksuiteprototypelength)
* [`Benchmark.Suite.prototype.running`](#benchmarksuiteprototyperunning)
* [`Benchmark.Suite.prototype.abort`](#benchmarksuiteprototypeabort)
* [`Benchmark.Suite.prototype.add`](#benchmarksuiteprototypeaddname-fn--options)
* [`Benchmark.Suite.prototype.clone`](#benchmarksuiteprototypecloneoptions)
* [`Benchmark.Suite.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.Suite.prototype.filter`](#benchmarksuiteprototypefiltercallback)
* [`Benchmark.Suite.prototype.forEach`](#benchmarksuiteprototypeforeachcallback)
* [`Benchmark.Suite.prototype.indexOf`](#benchmarksuiteprototypeindexofvalue)
* [`Benchmark.Suite.prototype.invoke`](#benchmarksuiteprototypeinvokename--arg1-arg2-)
* [`Benchmark.Suite.prototype.join`](#benchmarksuiteprototypejoinseparator-)
* [`Benchmark.Suite.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.Suite.prototype.map`](#benchmarksuiteprototypemapcallback)
* [`Benchmark.Suite.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.Suite.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.Suite.prototype.pluck`](#benchmarksuiteprototypepluckproperty)
* [`Benchmark.Suite.prototype.pop`](#benchmarksuiteprototypepop)
* [`Benchmark.Suite.prototype.push`](#benchmarksuiteprototypepush)
* [`Benchmark.Suite.prototype.reduce`](#benchmarksuiteprototypereducecallback-accumulator)
* [`Benchmark.Suite.prototype.reset`](#benchmarksuiteprototypereset)
* [`Benchmark.Suite.prototype.reverse`](#benchmarksuiteprototypereverse)
* [`Benchmark.Suite.prototype.run`](#benchmarksuiteprototyperunoptions)
* [`Benchmark.Suite.prototype.shift`](#benchmarksuiteprototypeshift)
* [`Benchmark.Suite.prototype.slice`](#benchmarksuiteprototypeslicestart-end)
* [`Benchmark.Suite.prototype.sort`](#benchmarksuiteprototypesortcomparefnnull)
* [`Benchmark.Suite.prototype.splice`](#benchmarksuiteprototypesplicestart-deletecount--val1-val2-)
* [`Benchmark.Suite.prototype.unshift`](#benchmarksuiteprototypeunshift)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`
* [`Benchmark.Suite.options`](#benchmarksuiteoptions)
* [`Benchmark.Suite.options.name`](#benchmarksuiteoptionsname)

<!-- /div -->


<!-- /div -->


<!-- div -->


<!-- div -->

## `Benchmark`

<!-- div -->

### <a id="benchmarkname-fn--options"></a>`Benchmark(name, fn [, options={}])`
<a href="#benchmarkname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L404 "View in source") [&#x24C9;][1]

The Benchmark constructor.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var bench = new Benchmark(fn);

// or using a name first
var bench = new Benchmark('foo', fn);

// or with options
var bench = new Benchmark('foo', fn, {

  // displayed by Benchmark#toString if `name` is not available
  'id': 'xyz',

  // called when the benchmark starts running
  'onStart': onStart,

  // called after each run cycle
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the benchmark completes running
  'onComplete': onComplete,

  // compiled/called before the test loop
  'setup': setup,

  // compiled/called after the test loop
  'teardown': teardown
});

// or name and options
var bench = new Benchmark('foo', {

  // a flag to indicate the benchmark is deferred
  'defer': true,

  // benchmark test function
  'fn': function(deferred) {
    // call resolve() when the deferred test is finished
    deferred.resolve();
  }
});

// or options only
var bench = new Benchmark({

  // benchmark name
  'name': 'foo',

  // benchmark test as a string
  'fn': '[1,2,3,4].sort()'
});

// a test's `this` binding is set to the benchmark instance
var bench = new Benchmark('foo', function() {
  'My name is '.concat(this.name); // My name is foo
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkversion"></a>`Benchmark.version`
<a href="#benchmarkversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3267 "View in source") [&#x24C9;][1]

*(String)*: The semantic version number.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeepclonevalue"></a>`Benchmark.deepClone(value)`
<a href="#benchmarkdeepclonevalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1225 "View in source") [&#x24C9;][1]

A deep clone utility.

#### Arguments
1. `value` *(Mixed)*: The value to clone.

#### Returns
*(Mixed)*: The cloned value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeachobject-callback-thisarg"></a>`Benchmark.each(object, callback, thisArg)`
<a href="#benchmarkeachobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1400 "View in source") [&#x24C9;][1]

An iteration utility for arrays and objects. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Array|Object)*: The object to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array, Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkextenddestination--source"></a>`Benchmark.extend(destination [, source={}])`
<a href="#benchmarkextenddestination--source">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1446 "View in source") [&#x24C9;][1]

Copies enumerable properties from the source(s) object to the destination object.

#### Arguments
1. `destination` *(Object)*: The destination object.
2. `[source={}]` *(Object)*: The source object.

#### Returns
*(Object)*: The destination object.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkfilterarray-callback-thisarg"></a>`Benchmark.filter(array, callback, thisArg)`
<a href="#benchmarkfilterarray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1485 "View in source") [&#x24C9;][1]

A generic `Array#filter` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function|String)*: The function/alias called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values that passed callback filter.

#### Example
~~~ js
// get odd numbers
Benchmark.filter([1, 2, 3, 4, 5], function(n) {
  return n % 2;
}); // -> [1, 3, 5];

// get fastest benchmarks
Benchmark.filter(benches, 'fastest');

// get slowest benchmarks
Benchmark.filter(benches, 'slowest');

// get benchmarks that completed without erroring
Benchmark.filter(benches, 'successful');
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforeacharray-callback-thisarg"></a>`Benchmark.forEach(array, callback, thisArg)`
<a href="#benchmarkforeacharray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1518 "View in source") [&#x24C9;][1]

A generic `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: Returns the array iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkformatnumbernumber"></a>`Benchmark.formatNumber(number)`
<a href="#benchmarkformatnumbernumber">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1557 "View in source") [&#x24C9;][1]

Converts a number to a more readable comma-separated string representation.

#### Arguments
1. `number` *(Number)*: The number to convert.

#### Returns
*(String)*: The more readable string representation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforownobject-callback-thisarg"></a>`Benchmark.forOwn(object, callback, thisArg)`
<a href="#benchmarkforownobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1545 "View in source") [&#x24C9;][1]

Iterates over an object's own properties, executing the `callback` for each. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `callback` *(Function)*: The function executed per own property.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkhaskeyobject-key"></a>`Benchmark.hasKey(object, key)`
<a href="#benchmarkhaskeyobject-key">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1572 "View in source") [&#x24C9;][1]

Checks if an object has the specified key as a direct property.

#### Arguments
1. `object` *(Object)*: The object to check.
2. `key` *(String)*: The key to check for.

#### Returns
*(Boolean)*: Returns `true` if key is a direct property, else `false`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkindexofarray-value--fromindex0"></a>`Benchmark.indexOf(array, value [, fromIndex=0])`
<a href="#benchmarkindexofarray-value--fromindex0">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1608 "View in source") [&#x24C9;][1]

A generic `Array#indexOf` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `value` *(Mixed)*: The value to search for.
3. `[fromIndex=0]` *(Number)*: The index to start searching from.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinterpolatestring-object"></a>`Benchmark.interpolate(string, object)`
<a href="#benchmarkinterpolatestring-object">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1630 "View in source") [&#x24C9;][1]

Modify a string by replacing named tokens with matching object property values.

#### Arguments
1. `string` *(String)*: The string to modify.
2. `object` *(Object)*: The template object.

#### Returns
*(String)*: The modified string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinvokebenches-name--arg1-arg2-"></a>`Benchmark.invoke(benches, name [, arg1, arg2, ...])`
<a href="#benchmarkinvokebenches-name--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1677 "View in source") [&#x24C9;][1]

Invokes a method on all items in an array.

#### Arguments
1. `benches` *(Array)*: Array of benchmarks to iterate over.
2. `name` *(String|Object)*: The name of the method to invoke OR options object.
3. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

#### Example
~~~ js
// invoke `reset` on all benchmarks
Benchmark.invoke(benches, 'reset');

// invoke `emit` with arguments
Benchmark.invoke(benches, 'emit', 'complete', listener);

// invoke `run(true)`, treat benchmarks as a queue, and register invoke callbacks
Benchmark.invoke(benches, {

  // invoke the `run` method
  'name': 'run',

  // pass a single argument
  'args': true,

  // treat as queue, removing benchmarks from front of `benches` until empty
  'queued': true,

  // called before any benchmarks have been invoked.
  'onStart': onStart,

  // called between invoking benchmarks
  'onCycle': onCycle,

  // called after all benchmarks have been invoked.
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkjoinobject--separator1--separator2:"></a>`Benchmark.join(object [, separator1=',', separator2=': '])`
<a href="#benchmarkjoinobject--separator1--separator2:">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1831 "View in source") [&#x24C9;][1]

Creates a string of joined array values or object key-value pairs.

#### Arguments
1. `object` *(Array|Object)*: The object to operate on.
2. `[separator1=',']` *(String)*: The separator used between key-value pairs.
3. `[separator2=': ']` *(String)*: The separator used between keys and values.

#### Returns
*(String)*: The joined result.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkmaparray-callback-thisarg"></a>`Benchmark.map(array, callback, thisArg)`
<a href="#benchmarkmaparray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1853 "View in source") [&#x24C9;][1]

A generic `Array#map` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkpluckarray-property"></a>`Benchmark.pluck(array, property)`
<a href="#benchmarkpluckarray-property">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1869 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all items in an array.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkreducearray-callback-accumulator"></a>`Benchmark.reduce(array, callback, accumulator)`
<a href="#benchmarkreducearray-callback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1885 "View in source") [&#x24C9;][1]

A generic `Array#reduce` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype`

<!-- div -->

### <a id="benchmarkprototypeaborted"></a>`Benchmark.prototype.aborted`
<a href="#benchmarkprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3377 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompiled"></a>`Benchmark.prototype.compiled`
<a href="#benchmarkprototypecompiled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3353 "View in source") [&#x24C9;][1]

*(Function, String)*: The compiled test function.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecount"></a>`Benchmark.prototype.count`
<a href="#benchmarkprototypecount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3329 "View in source") [&#x24C9;][1]

*(Number)*: The number of times a test was executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecycles"></a>`Benchmark.prototype.cycles`
<a href="#benchmarkprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3337 "View in source") [&#x24C9;][1]

*(Number)*: The number of cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypefn"></a>`Benchmark.prototype.fn`
<a href="#benchmarkprototypefn">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3369 "View in source") [&#x24C9;][1]

*(Function, String)*: The test to benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypehz"></a>`Benchmark.prototype.hz`
<a href="#benchmarkprototypehz">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3345 "View in source") [&#x24C9;][1]

*(Number)*: The number of executions per second.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunning"></a>`Benchmark.prototype.running`
<a href="#benchmarkprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3385 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypesetup"></a>`Benchmark.prototype.setup`
<a href="#benchmarkprototypesetup">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3448 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **before** the test loop.

#### Example
~~~ js
// basic usage
var bench = Benchmark({
  'setup': function() {
    var c = this.count,
        element = document.getElementById('container');
    while (c--) {
      element.appendChild(document.createElement('div'));
    }
  },
  'fn': function() {
    element.removeChild(element.lastChild);
  }
});

// compiles to something like:
var c = this.count,
    element = document.getElementById('container');
while (c--) {
  element.appendChild(document.createElement('div'));
}
var start = new Date;
while (count--) {
  element.removeChild(element.lastChild);
}
var end = new Date - start;

// or using strings
var bench = Benchmark({
  'setup': '\
    var a = 0;\n\
    (function() {\n\
      (function() {\n\
        (function() {',
  'fn': 'a += 1;',
  'teardown': '\
         }())\n\
       }())\n\
     }())'
});

// compiles to something like:
var a = 0;
(function() {
  (function() {
    (function() {
      var start = new Date;
      while (count--) {
        a += 1;
      }
      var end = new Date - start;
    }())
  }())
}())
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeteardown"></a>`Benchmark.prototype.teardown`
<a href="#benchmarkprototypeteardown">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3456 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **after** the test loop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeabort"></a>`Benchmark.prototype.abort()`
<a href="#benchmarkprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2218 "View in source") [&#x24C9;][1]

Aborts the benchmark without recording times.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecloneoptions"></a>`Benchmark.prototype.clone(options)`
<a href="#benchmarkprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2257 "View in source") [&#x24C9;][1]

Creates a new benchmark using the same test and options.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new benchmark instance.

#### Example
~~~ js
var bizarro = bench.clone({
  'name': 'doppelganger'
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompareother"></a>`Benchmark.prototype.compare(other)`
<a href="#benchmarkprototypecompareother">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2280 "View in source") [&#x24C9;][1]

Determines if a benchmark is faster than another.

#### Arguments
1. `other` *(Object)*: The benchmark to compare.

#### Returns
*(Number)*: Returns `-1` if slower, `1` if faster, and `0` if indeterminate.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypereset"></a>`Benchmark.prototype.reset()`
<a href="#benchmarkprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2334 "View in source") [&#x24C9;][1]

Reset properties and abort if running.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunoptions"></a>`Benchmark.prototype.run([options={}])`
<a href="#benchmarkprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3000 "View in source") [&#x24C9;][1]

Runs the benchmark.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
bench.run();

// or with options
bench.run({ 'async': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypetostring"></a>`Benchmark.prototype.toString()`
<a href="#benchmarkprototypetostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2405 "View in source") [&#x24C9;][1]

Displays relevant benchmark information when coerced to a string.

#### Returns
*(String)*: A string representation of the benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.options`

<!-- div -->

### <a id="benchmarkoptions"></a>`Benchmark.options`
<a href="#benchmarkoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3049 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by benchmark instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsasync"></a>`Benchmark.options.async`
<a href="#benchmarkoptionsasync">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3058 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that benchmark cycles will execute asynchronously by default.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdefer"></a>`Benchmark.options.defer`
<a href="#benchmarkoptionsdefer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3066 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that the benchmark clock is deferred.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdelay"></a>`Benchmark.options.delay`
<a href="#benchmarkoptionsdelay">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3073 "View in source") [&#x24C9;][1]

*(Number)*: The delay between test cycles *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsid"></a>`Benchmark.options.id`
<a href="#benchmarkoptionsid">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3082 "View in source") [&#x24C9;][1]

*(String)*: Displayed by Benchmark#toString when a `name` is not available *(auto-generated if absent)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsinitcount"></a>`Benchmark.options.initCount`
<a href="#benchmarkoptionsinitcount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3090 "View in source") [&#x24C9;][1]

*(Number)*: The default number of times to execute a test on a benchmark's first cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmaxtime"></a>`Benchmark.options.maxTime`
<a href="#benchmarkoptionsmaxtime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3099 "View in source") [&#x24C9;][1]

*(Number)*: The maximum time a benchmark is allowed to run before finishing *(secs)*. Note: Cycle delays aren't counted toward the maximum time.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsminsamples"></a>`Benchmark.options.minSamples`
<a href="#benchmarkoptionsminsamples">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3107 "View in source") [&#x24C9;][1]

*(Number)*: The minimum sample size required to perform statistical analysis.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmintime"></a>`Benchmark.options.minTime`
<a href="#benchmarkoptionsmintime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3115 "View in source") [&#x24C9;][1]

*(Number)*: The time needed to reduce the percent uncertainty of measurement to `1`% *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsname"></a>`Benchmark.options.name`
<a href="#benchmarkoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3123 "View in source") [&#x24C9;][1]

*(String)*: The name of the benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonabort"></a>`Benchmark.options.onAbort`
<a href="#benchmarkoptionsonabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3131 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncomplete"></a>`Benchmark.options.onComplete`
<a href="#benchmarkoptionsoncomplete">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3139 "View in source") [&#x24C9;][1]

An event listener called when the benchmark completes running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncycle"></a>`Benchmark.options.onCycle`
<a href="#benchmarkoptionsoncycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3147 "View in source") [&#x24C9;][1]

An event listener called after each run cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonerror"></a>`Benchmark.options.onError`
<a href="#benchmarkoptionsonerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3155 "View in source") [&#x24C9;][1]

An event listener called when a test errors.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonreset"></a>`Benchmark.options.onReset`
<a href="#benchmarkoptionsonreset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3163 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is reset.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonstart"></a>`Benchmark.options.onStart`
<a href="#benchmarkoptionsonstart">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3171 "View in source") [&#x24C9;][1]

An event listener called when the benchmark starts running.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.platform`

<!-- div -->

### <a id="benchmarkplatform"></a>`Benchmark.platform`
<a href="#benchmarkplatform">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3182 "View in source") [&#x24C9;][1]

*(Object)*: Platform object with properties describing things like browser name, version, and operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformdescription"></a>`Benchmark.platform.description`
<a href="#benchmarkplatformdescription">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3190 "View in source") [&#x24C9;][1]

*(String)*: The platform description.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformlayout"></a>`Benchmark.platform.layout`
<a href="#benchmarkplatformlayout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3198 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser layout engine.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformmanufacturer"></a>`Benchmark.platform.manufacturer`
<a href="#benchmarkplatformmanufacturer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3222 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product's manufacturer.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformname"></a>`Benchmark.platform.name`
<a href="#benchmarkplatformname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3214 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser/environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformos"></a>`Benchmark.platform.os`
<a href="#benchmarkplatformos">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3230 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformprerelease"></a>`Benchmark.platform.prerelease`
<a href="#benchmarkplatformprerelease">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3238 "View in source") [&#x24C9;][1]

*(String, Null)*: The alpha/beta release indicator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformproduct"></a>`Benchmark.platform.product`
<a href="#benchmarkplatformproduct">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3206 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product hosting the browser.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformversion"></a>`Benchmark.platform.version`
<a href="#benchmarkplatformversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3246 "View in source") [&#x24C9;][1]

*(String, Null)*: The browser/environment version.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformtostring"></a>`Benchmark.platform.toString()`
<a href="#benchmarkplatformtostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3255 "View in source") [&#x24C9;][1]

Return platform description when the platform object is coerced to a string.

#### Returns
*(String)*: The platform description.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.support`

<!-- div -->

### <a id="benchmarksupport"></a>`Benchmark.support`
<a href="#benchmarksupport">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L135 "View in source") [&#x24C9;][1]

*(Object)*: An object used to flag environments/features.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportair"></a>`Benchmark.support.air`
<a href="#benchmarksupportair">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L145 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect Adobe AIR.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportargumentsclass"></a>`Benchmark.support.argumentsClass`
<a href="#benchmarksupportargumentsclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L153 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if `arguments` objects have the correct internal [[Class]] value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportbrowser"></a>`Benchmark.support.browser`
<a href="#benchmarksupportbrowser">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L161 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if in a browser environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyindex"></a>`Benchmark.support.charByIndex`
<a href="#benchmarksupportcharbyindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L169 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings support accessing characters by index.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyownindex"></a>`Benchmark.support.charByOwnIndex`
<a href="#benchmarksupportcharbyownindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L179 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings have indexes as own properties.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdecompilation"></a>`Benchmark.support.decompilation`
<a href="#benchmarksupportdecompilation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L207 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if functions support decompilation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdescriptors"></a>`Benchmark.support.descriptors`
<a href="#benchmarksupportdescriptors">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L228 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ property descriptor API.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportgetallkeys"></a>`Benchmark.support.getAllKeys`
<a href="#benchmarksupportgetallkeys">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L242 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ Object.getOwnPropertyNames().

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportiteratesownfirst"></a>`Benchmark.support.iteratesOwnFirst`
<a href="#benchmarksupportiteratesownfirst">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L255 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if own properties are iterated before inherited properties *(all but IE < `9`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportjava"></a>`Benchmark.support.java`
<a href="#benchmarksupportjava">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L190 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if Java is enabled/exposed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportnodeclass"></a>`Benchmark.support.nodeClass`
<a href="#benchmarksupportnodeclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L272 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if a node's [[Class]] is resolvable *(all but IE < `9`)* and that the JS engine errors when attempting to coerce an object to a string without a `toString` property value of `typeof` "function".

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupporttimeout"></a>`Benchmark.support.timeout`
<a href="#benchmarksupporttimeout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L198 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if the Timers API exists.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`

<!-- div -->

### <a id="benchmarkprototypeerror"></a>`Benchmark.prototype.error`
<a href="#benchmarkprototypeerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3361 "View in source") [&#x24C9;][1]

*(Object)*: The error object if the test failed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`

<!-- div -->

### <a id="benchmarkprototypestats"></a>`Benchmark.prototype.stats`
<a href="#benchmarkprototypestats">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3464 "View in source") [&#x24C9;][1]

*(Object)*: An object of stats including mean, margin or error, and standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsdeviation"></a>`Benchmark.prototype.stats.deviation`
<a href="#benchmark-statsdeviation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3496 "View in source") [&#x24C9;][1]

*(Number)*: The sample standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmean"></a>`Benchmark.prototype.stats.mean`
<a href="#benchmark-statsmean">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3504 "View in source") [&#x24C9;][1]

*(Number)*: The sample arithmetic mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmoe"></a>`Benchmark.prototype.stats.moe`
<a href="#benchmark-statsmoe">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3472 "View in source") [&#x24C9;][1]

*(Number)*: The margin of error.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsrme"></a>`Benchmark.prototype.stats.rme`
<a href="#benchmark-statsrme">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3480 "View in source") [&#x24C9;][1]

*(Number)*: The relative margin of error *(expressed as a percentage of the mean)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssample"></a>`Benchmark.prototype.stats.sample`
<a href="#benchmark-statssample">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3512 "View in source") [&#x24C9;][1]

*(Array)*: The array of sampled periods.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssem"></a>`Benchmark.prototype.stats.sem`
<a href="#benchmark-statssem">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3488 "View in source") [&#x24C9;][1]

*(Number)*: The standard error of the mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsvariance"></a>`Benchmark.prototype.stats.variance`
<a href="#benchmark-statsvariance">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3520 "View in source") [&#x24C9;][1]

*(Number)*: The sample variance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`

<!-- div -->

### <a id="benchmarkprototypetimes"></a>`Benchmark.prototype.times`
<a href="#benchmarkprototypetimes">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3529 "View in source") [&#x24C9;][1]

*(Object)*: An object of timing data including cycle, elapsed, period, start, and stop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timescycle"></a>`Benchmark.prototype.times.cycle`
<a href="#benchmark-timescycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3537 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the last cycle *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timeselapsed"></a>`Benchmark.prototype.times.elapsed`
<a href="#benchmark-timeselapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3545 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timesperiod"></a>`Benchmark.prototype.times.period`
<a href="#benchmark-timesperiod">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3553 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to execute the test once *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timestimestamp"></a>`Benchmark.prototype.times.timeStamp`
<a href="#benchmark-timestimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3561 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`

<!-- div -->

### <a id="benchmarkdeferredclone"></a>`Benchmark.Deferred(clone)`
<a href="#benchmarkdeferredclone">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L445 "View in source") [&#x24C9;][1]

The Deferred constructor.

#### Arguments
1. `clone` *(Object)*: The cloned benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`

<!-- div -->

### <a id="benchmarkdeferredprototypebenchmark"></a>`Benchmark.Deferred.prototype.benchmark`
<a href="#benchmarkdeferredprototypebenchmark">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3605 "View in source") [&#x24C9;][1]

*(Object)*: The deferred benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypecycles"></a>`Benchmark.Deferred.prototype.cycles`
<a href="#benchmarkdeferredprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3613 "View in source") [&#x24C9;][1]

*(Number)*: The number of deferred cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypeelapsed"></a>`Benchmark.Deferred.prototype.elapsed`
<a href="#benchmarkdeferredprototypeelapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3621 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the deferred benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototyperesolve"></a>`Benchmark.Deferred.prototype.resolve`
<a href="#benchmarkdeferredprototyperesolve">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1188 "View in source") [&#x24C9;][1]

*(Unknown)*: Handles cycling/completing the deferred benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypetimestamp"></a>`Benchmark.Deferred.prototype.timeStamp`
<a href="#benchmarkdeferredprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3629 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the deferred benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event`

<!-- div -->

### <a id="benchmarkeventtype"></a>`Benchmark.Event(type)`
<a href="#benchmarkeventtype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L461 "View in source") [&#x24C9;][1]

The Event constructor.

#### Arguments
1. `type` *(String|Object)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`

<!-- div -->

### <a id="benchmarkeventprototypeaborted"></a>`Benchmark.Event.prototype.aborted`
<a href="#benchmarkeventprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3645 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the emitters listener iteration is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypecancelled"></a>`Benchmark.Event.prototype.cancelled`
<a href="#benchmarkeventprototypecancelled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3653 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the default action is cancelled.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototyperesult"></a>`Benchmark.Event.prototype.result`
<a href="#benchmarkeventprototyperesult">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3669 "View in source") [&#x24C9;][1]

*(Mixed)*: The return value of the last executed listener.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetimestamp"></a>`Benchmark.Event.prototype.timeStamp`
<a href="#benchmarkeventprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3685 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the event was created *(ms)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetype"></a>`Benchmark.Event.prototype.type`
<a href="#benchmarkeventprototypetype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3693 "View in source") [&#x24C9;][1]

*(String)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`

<!-- div -->

### <a id="benchmarkeventprototypecurrenttarget"></a>`Benchmark.Event.prototype.currentTarget`
<a href="#benchmarkeventprototypecurrenttarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3661 "View in source") [&#x24C9;][1]

*(Object)*: The object whose listeners are currently being processed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`

<!-- div -->

### <a id="benchmarkeventprototypetarget"></a>`Benchmark.Event.prototype.target`
<a href="#benchmarkeventprototypetarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3677 "View in source") [&#x24C9;][1]

*(Object)*: The object to which the event was originally emitted.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite`

<!-- div -->

### <a id="benchmarksuitename--options"></a>`Benchmark.Suite(name [, options={}])`
<a href="#benchmarksuitename--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L507 "View in source") [&#x24C9;][1]

The Suite constructor.

#### Arguments
1. `name` *(String)*: A name to identify the suite.
2. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var suite = new Benchmark.Suite;

// or using a name first
var suite = new Benchmark.Suite('foo');

// or with options
var suite = new Benchmark.Suite('foo', {

  // called when the suite starts running
  'onStart': onStart,

  // called between running benchmarks
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the suite completes running
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`

<!-- div -->

### <a id="benchmarksuiteprototypeaborted"></a>`Benchmark.Suite.prototype.aborted`
<a href="#benchmarksuiteprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3734 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypelength"></a>`Benchmark.Suite.prototype.length`
<a href="#benchmarksuiteprototypelength">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3726 "View in source") [&#x24C9;][1]

*(Number)*: The number of benchmarks in the suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunning"></a>`Benchmark.Suite.prototype.running`
<a href="#benchmarksuiteprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3742 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeabort"></a>`Benchmark.Suite.prototype.abort()`
<a href="#benchmarksuiteprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1902 "View in source") [&#x24C9;][1]

Aborts all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeaddname-fn--options"></a>`Benchmark.Suite.prototype.add(name, fn [, options={}])`
<a href="#benchmarksuiteprototypeaddname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1962 "View in source") [&#x24C9;][1]

Adds a test to the benchmark suite.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
suite.add(fn);

// or using a name first
suite.add('foo', fn);

// or with options
suite.add('foo', fn, {
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or name and options
suite.add('foo', {
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or options only
suite.add({
  'name': 'foo',
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypecloneoptions"></a>`Benchmark.Suite.prototype.clone(options)`
<a href="#benchmarksuiteprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1981 "View in source") [&#x24C9;][1]

Creates a new suite with cloned benchmarks.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypefiltercallback"></a>`Benchmark.Suite.prototype.filter(callback)`
<a href="#benchmarksuiteprototypefiltercallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2004 "View in source") [&#x24C9;][1]

An `Array#filter` like method.

#### Arguments
1. `callback` *(Function|String)*: The function/alias called per iteration.

#### Returns
*(Object)*: A new suite of benchmarks that passed callback filter.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeforeachcallback"></a>`Benchmark.Suite.prototype.forEach(callback)`
<a href="#benchmarksuiteprototypeforeachcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3752 "View in source") [&#x24C9;][1]

An `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Object)*: The suite iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeindexofvalue"></a>`Benchmark.Suite.prototype.indexOf(value)`
<a href="#benchmarksuiteprototypeindexofvalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3761 "View in source") [&#x24C9;][1]

An `Array#indexOf` like method.

#### Arguments
1. `value` *(Mixed)*: The value to search for.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeinvokename--arg1-arg2-"></a>`Benchmark.Suite.prototype.invoke(name [, arg1, arg2, ...])`
<a href="#benchmarksuiteprototypeinvokename--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3771 "View in source") [&#x24C9;][1]

Invokes a method on all benchmarks in the suite.

#### Arguments
1. `name` *(String|Object)*: The name of the method to invoke OR options object.
2. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypejoinseparator-"></a>`Benchmark.Suite.prototype.join([separator=','])`
<a href="#benchmarksuiteprototypejoinseparator-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3780 "View in source") [&#x24C9;][1]

Converts the suite of benchmarks to a string.

#### Arguments
1. `[separator=',']` *(String)*: A string to separate each element of the array.

#### Returns
*(String)*: The string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypemapcallback"></a>`Benchmark.Suite.prototype.map(callback)`
<a href="#benchmarksuiteprototypemapcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3789 "View in source") [&#x24C9;][1]

An `Array#map` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepluckproperty"></a>`Benchmark.Suite.prototype.pluck(property)`
<a href="#benchmarksuiteprototypepluckproperty">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3798 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all benchmarks in the suite.

#### Arguments
1. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepop"></a>`Benchmark.Suite.prototype.pop()`
<a href="#benchmarksuiteprototypepop">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3806 "View in source") [&#x24C9;][1]

Removes the last benchmark from the suite and returns it.

#### Returns
*(Mixed)*: The removed benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepush"></a>`Benchmark.Suite.prototype.push()`
<a href="#benchmarksuiteprototypepush">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3814 "View in source") [&#x24C9;][1]

Appends benchmarks to the suite.

#### Returns
*(Number)*: The suite's new length.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereducecallback-accumulator"></a>`Benchmark.Suite.prototype.reduce(callback, accumulator)`
<a href="#benchmarksuiteprototypereducecallback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3833 "View in source") [&#x24C9;][1]

An `Array#reduce` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.
2. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereset"></a>`Benchmark.Suite.prototype.reset()`
<a href="#benchmarksuiteprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2019 "View in source") [&#x24C9;][1]

Resets all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereverse"></a>`Benchmark.Suite.prototype.reverse()`
<a href="#benchmarksuiteprototypereverse">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L638 "View in source") [&#x24C9;][1]

Rearrange the host array's elements in reverse order.

#### Returns
*(Array)*: The reversed array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunoptions"></a>`Benchmark.Suite.prototype.run([options={}])`
<a href="#benchmarksuiteprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2056 "View in source") [&#x24C9;][1]

Runs the suite.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The suite instance.

#### Example
~~~ js
// basic usage
suite.run();

// or with options
suite.run({ 'async': true, 'queued': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeshift"></a>`Benchmark.Suite.prototype.shift()`
<a href="#benchmarksuiteprototypeshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L671 "View in source") [&#x24C9;][1]

Removes the first element of the host array and returns it.

#### Returns
*(Mixed)*: The first element of the array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeslicestart-end"></a>`Benchmark.Suite.prototype.slice(start, end)`
<a href="#benchmarksuiteprototypeslicestart-end">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L684 "View in source") [&#x24C9;][1]

Creates an array of the host array's elements from the start index up to, but not including, the end index.

#### Arguments
1. `start` *(Number)*: The starting index.
2. `end` *(Number)*: The end index.

#### Returns
*(Array)*: The new array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesortcomparefnnull"></a>`Benchmark.Suite.prototype.sort([compareFn=null])`
<a href="#benchmarksuiteprototypesortcomparefnnull">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3823 "View in source") [&#x24C9;][1]

Sorts the benchmarks of the suite.

#### Arguments
1. `[compareFn=null]` *(Function)*: A function that defines the sort order.

#### Returns
*(Object)*: The sorted suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesplicestart-deletecount--val1-val2-"></a>`Benchmark.Suite.prototype.splice(start, deleteCount [, val1, val2, ...])`
<a href="#benchmarksuiteprototypesplicestart-deletecount--val1-val2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L714 "View in source") [&#x24C9;][1]

Allows removing a range of elements and/or inserting elements into the host array.

#### Arguments
1. `start` *(Number)*: The start index.
2. `deleteCount` *(Number)*: The number of elements to delete.
3. `[val1, val2, ...]` *(Mixed)*: values to insert at the `start` index.

#### Returns
*(Array)*: An array of removed elements.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeunshift"></a>`Benchmark.Suite.prototype.unshift()`
<a href="#benchmarksuiteprototypeunshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L749 "View in source") [&#x24C9;][1]

Appends arguments to the host array.

#### Returns
*(Number)*: The new length.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`

<!-- div -->

### <a id="benchmarksuiteoptions"></a>`Benchmark.Suite.options`
<a href="#benchmarksuiteoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3705 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by suite instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteoptionsname"></a>`Benchmark.Suite.options.name`
<a href="#benchmarksuiteoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3713 "View in source") [&#x24C9;][1]

*(String)*: The name of the suite.

* * *

<!-- /div -->


<!-- /div -->


<!-- /div -->


  [1]: #Benchmark "Jump back to the TOC."# JSON 3 #

![JSON 3 Logo](http://bestiejs.github.io/json3/page/logo.png)

**JSON 3** is a modern JSON implementation compatible with a variety of JavaScript platforms, including Internet Explorer 6, Opera 7, Safari 2, and Netscape 6. The current version is **3.2.6**.

- [Development Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.js) *(40 KB; uncompressed with comments)*
- [Production Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.min.js) *(3.3 KB; compressed and `gzip`-ped)*

CDN copies are also available at [cdnjs](http://cdnjs.com/libraries/json3/) & [jsDelivr](http://www.jsdelivr.com/#!json3).

[JSON](http://json.org/) is a language-independent data interchange format based on a loose subset of the JavaScript grammar. Originally popularized by [Douglas Crockford](http://www.crockford.com/), the format was standardized in the [fifth edition](http://es5.github.com/) of the ECMAScript specification. The 5.1 edition, ratified in June 2011, incorporates several modifications to the grammar pertaining to the serialization of dates.

JSON 3 exposes two functions: `stringify()` for [serializing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/stringify) a JavaScript value to JSON, and `parse()` for [producing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/parse) a JavaScript value from a JSON source string. It is a **drop-in replacement** for [JSON 2](http://json.org/js). The functions behave exactly as described in the ECMAScript spec, **except** for the date serialization discrepancy noted below.

The JSON 3 parser does **not** use `eval` or regular expressions. This provides security and performance benefits in obsolete and mobile environments, where the margin is particularly significant. The complete [benchmark suite](http://jsperf.com/json3) is available on [jsPerf](http://jsperf.com/).

The project is [hosted on GitHub](http://git.io/json3), along with the [unit tests](http://bestiejs.github.io/json3/test/test_browser.html). It is part of the [BestieJS](https://github.com/bestiejs) family, a collection of best-in-class JavaScript libraries that promote cross-platform support, specification precedents, unit testing, and plenty of documentation.

# Changes from JSON 2 #

JSON 3...

* Correctly serializes primitive wrapper objects.
* Throws a `TypeError` when serializing cyclic structures (JSON 2 recurses until the call stack overflows).
* Utilizes **feature tests** to detect broken or incomplete *native* JSON implementations (JSON 2 only checks for the presence of the native functions). The tests are only executed once at runtime, so there is no additional performance cost when parsing or serializing values.

**As of v3.2.3**, JSON 3 is compatible with [Prototype](http://prototypejs.org) 1.6.1 and older.

In contrast to JSON 2, JSON 3 **does not**...

* Add `toJSON()` methods to the `Boolean`, `Number`, and `String` prototypes. These are not part of any standard, and are made redundant by the design of the `stringify()` implementation.
* Add `toJSON()` or `toISOString()` methods to `Date.prototype`. See the note about date serialization below.

## Date Serialization

**JSON 3 deviates from the specification in one important way**: it does not define `Date#toISOString()` or `Date#toJSON()`. This preserves CommonJS compatibility and avoids polluting native prototypes. Instead, date serialization is performed internally by the `stringify()` implementation: if a date object does not define a custom `toJSON()` method, it is serialized as a [simplified ISO 8601 date-time string](http://es5.github.com/#x15.9.1.15).

**Several native `Date#toJSON()` implementations produce date time strings that do *not* conform to the grammar outlined in the spec**. For instance, all versions of Safari 4, as well as JSON 2, fail to serialize extended years correctly. Furthermore, JSON 2 and older implementations omit the milliseconds from the date-time string (optional in ES 5, but required in 5.1). Finally, in all versions of Safari 4 and 5, serializing an invalid date will produce the string `"Invalid Date"`, rather than `null`. Because these environments exhibit other serialization bugs, however, JSON 3 will override the native `stringify()` implementation.

Portions of the date serialization code are adapted from the [`date-shim`](https://github.com/Yaffle/date-shim) project.

# Usage #

## Web Browsers

    <script src="http://bestiejs.github.io/json3/lib/json3.js"></script>
    <script>
      JSON.stringify({"Hello": 123});
      // => '{"Hello":123}'
      JSON.parse("[[1, 2, 3], 1, 2, 3, 4]", function (key, value) {
        if (typeof value == "number") {
          value = value % 2 ? "Odd" : "Even";
        }
        return value;
      });
      // => [["Odd", "Even", "Odd"], "Odd", "Even", "Odd", "Even"]
    </script>

## CommonJS Environments

    var JSON3 = require("./path/to/json3");
    JSON3.parse("[1, 2, 3]");
    // => [1, 2, 3]

## JavaScript Engines

    load("path/to/json3.js");
    JSON.stringify({"Hello": 123, "Good-bye": 456}, ["Hello"], "\t");
    // => '{\n\t"Hello": 123\n}'

# Compatibility #

JSON 3 has been **tested** with the following web browsers, CommonJS environments, and JavaScript engines.

## Web Browsers

- Windows [Internet Explorer](http://www.microsoft.com/windows/internet-explorer), version 6.0 and higher
- Mozilla [Firefox](http://www.mozilla.com/firefox), version 1.0 and higher
- Apple [Safari](http://www.apple.com/safari), version 2.0 and higher
- [Opera](http://www.opera.com) 7.02 and higher
- [Mozilla](http://sillydog.org/narchive/gecko.php) 1.0, [Netscape](http://sillydog.org/narchive/) 6.2.3, and [SeaMonkey](http://www.seamonkey-project.org/) 1.0 and higher

## CommonJS Environments

- [Node](http://nodejs.org/) 0.2.6 and higher
- [RingoJS](http://ringojs.org/) 0.4 and higher
- [Narwhal](http://narwhaljs.org/) 0.3.2 and higher

## JavaScript Engines

- Mozilla [Rhino](http://www.mozilla.org/rhino) 1.5R5 and higher
- WebKit [JSC](https://trac.webkit.org/wiki/JSC)
- Google [V8](http://code.google.com/p/v8)

## Known Incompatibilities

* Attempting to serialize the `arguments` object may produce inconsistent results across environments due to specification version differences. As a workaround, please convert the `arguments` object to an array first: `JSON.stringify([].slice.call(arguments, 0))`.

## Required Native Methods

JSON 3 assumes that the following methods exist and function as described in the ECMAScript specification:

- The `Number`, `String`, `Array`, `Object`, `Date`, `SyntaxError`, and `TypeError` constructors.
- `String.fromCharCode`
- `Object#toString`
- `Function#call`
- `Math.floor`
- `Number#toString`
- `Date#valueOf`
- `String.prototype`: `indexOf`, `charCodeAt`, `charAt`, `slice`.
- `Array.prototype`: `push`, `pop`, `join`.

# Contribute #

Check out a working copy of the JSON 3 source code with [Git](http://git-scm.com/):

    $ git clone git://github.com/bestiejs/json3.git
    $ cd json3
    $ git submodule update --init

If you'd like to contribute a feature or bug fix, you can [fork](http://help.github.com/fork-a-repo/) JSON 3, commit your changes, and [send a pull request](http://help.github.com/send-pull-requests/). Please make sure to update the unit tests in the `test` directory as well.

Alternatively, you can use the [GitHub issue tracker](https://github.com/bestiejs/json3/issues) to submit bug reports, feature requests, and questions, or send tweets to [@kitcambridge](http://twitter.com/kitcambridge).

JSON 3 is released under the [MIT License](http://kit.mit-license.org/).
# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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
# Benchmark.js <sup>v1.0.0</sup>

A [robust](http://calendar.perfplanet.com/2010/bulletproof-javascript-benchmarks/ "Bulletproof JavaScript benchmarks") benchmarking library that works on nearly all JavaScript platforms<sup><a name="fnref1" href="#fn1">1</a></sup>, supports high-resolution timers, and returns statistically significant results. As seen on [jsPerf](http://jsperf.com/).

## BestieJS

Benchmark.js is part of the BestieJS *"Best in Class"* module collection. This means we promote solid browser/environment support, ES5 precedents, unit testing, and plenty of documentation.

## Documentation

The documentation for Benchmark.js can be viewed here: <http://benchmarkjs.com/docs>

For a list of upcoming features, check out our [roadmap](https://github.com/bestiejs/benchmark.js/wiki/Roadmap).

## Support

Benchmark.js has been tested in at least Adobe AIR 3.1, Chrome 5-21, Firefox 1.5-13, IE 6-9, Opera 9.25-12.01, Safari 3-6, Node.js 0.8.6, Narwhal 0.3.2, RingoJS 0.8, and Rhino 1.7RC5.

## Installation and usage

In a browser or Adobe AIR:

~~~ html
<script src="benchmark.js"></script>
~~~

Optionally, expose Java’s nanosecond timer by adding the `nano` applet to the `<body>`:

~~~ html
<applet code="nano" archive="nano.jar"></applet>
~~~

Or enable Chrome’s microsecond timer by using the [command line switch](http://peter.sh/experiments/chromium-command-line-switches/#enable-benchmarking):

    --enable-benchmarking

Via [npm](http://npmjs.org/):

~~~ bash
npm install benchmark
~~~

In [Node.js](http://nodejs.org/) and [RingoJS v0.8.0+](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark');
~~~

Optionally, use the [microtime module](https://github.com/wadey/node-microtime) by Wade Simmons:

~~~ bash
npm install microtime
~~~

In [RingoJS v0.7.0-](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark').Benchmark;
~~~

In [Rhino](http://www.mozilla.org/rhino/):

~~~ js
load('benchmark.js');
~~~

In an AMD loader like [RequireJS](http://requirejs.org/):

~~~ js
require({
  'paths': {
    'benchmark': 'path/to/benchmark'
  }
},
['benchmark'], function(Benchmark) {
  console.log(Benchmark.version);
});

// or with platform.js
// https://github.com/bestiejs/platform.js
require({
  'paths': {
    'benchmark': 'path/to/benchmark',
    'platform': 'path/to/platform'
  }
},
['benchmark', 'platform'], function(Benchmark, platform) {
  Benchmark.platform = platform;
  console.log(Benchmark.platform.name);
});
~~~

Usage example:

~~~ js
var suite = new Benchmark.Suite;

// add tests
suite.add('RegExp#test', function() {
  /o/.test('Hello World!');
})
.add('String#indexOf', function() {
  'Hello World!'.indexOf('o') > -1;
})
// add listeners
.on('cycle', function(event) {
  console.log(String(event.target));
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
// run async
.run({ 'async': true });

// logs:
// > RegExp#test x 4,161,532 +-0.99% (59 cycles)
// > String#indexOf x 6,139,623 +-1.00% (131 cycles)
// > Fastest is String#indexOf
~~~

## Authors

* [Mathias Bynens](http://mathiasbynens.be/)
  [![twitter/mathias](http://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter")
* [John-David Dalton](http://allyoucanleet.com/)
  [![twitter/jdalton](http://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter")

## Contributors

* [Kit Cambridge](http://kitcambridge.github.com/)
  [![twitter/kitcambridge](http://gravatar.com/avatar/6662a1d02f351b5ef2f8b4d815804661?s=70)](https://twitter.com/kitcambridge "Follow @kitcambridge on Twitter")
# Benchmark.js <sup>v1.0.0</sup>

<!-- div -->


<!-- div -->

## <a id="Benchmark"></a>`Benchmark`
* [`Benchmark`](#benchmarkname-fn--options)
* [`Benchmark.version`](#benchmarkversion)
* [`Benchmark.deepClone`](#benchmarkdeepclonevalue)
* [`Benchmark.each`](#benchmarkeachobject-callback-thisarg)
* [`Benchmark.extend`](#benchmarkextenddestination--source)
* [`Benchmark.filter`](#benchmarkfilterarray-callback-thisarg)
* [`Benchmark.forEach`](#benchmarkforeacharray-callback-thisarg)
* [`Benchmark.formatNumber`](#benchmarkformatnumbernumber)
* [`Benchmark.forOwn`](#benchmarkforownobject-callback-thisarg)
* [`Benchmark.hasKey`](#benchmarkhaskeyobject-key)
* [`Benchmark.indexOf`](#benchmarkindexofarray-value--fromindex0)
* [`Benchmark.interpolate`](#benchmarkinterpolatestring-object)
* [`Benchmark.invoke`](#benchmarkinvokebenches-name--arg1-arg2-)
* [`Benchmark.join`](#benchmarkjoinobject--separator1--separator2:)
* [`Benchmark.map`](#benchmarkmaparray-callback-thisarg)
* [`Benchmark.pluck`](#benchmarkpluckarray-property)
* [`Benchmark.reduce`](#benchmarkreducearray-callback-accumulator)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype`
* [`Benchmark.prototype.aborted`](#benchmarkprototypeaborted)
* [`Benchmark.prototype.compiled`](#benchmarkprototypecompiled)
* [`Benchmark.prototype.count`](#benchmarkprototypecount)
* [`Benchmark.prototype.cycles`](#benchmarkprototypecycles)
* [`Benchmark.prototype.fn`](#benchmarkprototypefn)
* [`Benchmark.prototype.hz`](#benchmarkprototypehz)
* [`Benchmark.prototype.running`](#benchmarkprototyperunning)
* [`Benchmark.prototype.setup`](#benchmarkprototypesetup)
* [`Benchmark.prototype.teardown`](#benchmarkprototypeteardown)
* [`Benchmark.prototype.abort`](#benchmarkprototypeabort)
* [`Benchmark.prototype.clone`](#benchmarkprototypecloneoptions)
* [`Benchmark.prototype.compare`](#benchmarkprototypecompareother)
* [`Benchmark.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.prototype.reset`](#benchmarkprototypereset)
* [`Benchmark.prototype.run`](#benchmarkprototyperunoptions)
* [`Benchmark.prototype.toString`](#benchmarkprototypetostring)

<!-- /div -->


<!-- div -->

## `Benchmark.options`
* [`Benchmark.options`](#benchmarkoptions)
* [`Benchmark.options.async`](#benchmarkoptionsasync)
* [`Benchmark.options.defer`](#benchmarkoptionsdefer)
* [`Benchmark.options.delay`](#benchmarkoptionsdelay)
* [`Benchmark.options.id`](#benchmarkoptionsid)
* [`Benchmark.options.initCount`](#benchmarkoptionsinitcount)
* [`Benchmark.options.maxTime`](#benchmarkoptionsmaxtime)
* [`Benchmark.options.minSamples`](#benchmarkoptionsminsamples)
* [`Benchmark.options.minTime`](#benchmarkoptionsmintime)
* [`Benchmark.options.name`](#benchmarkoptionsname)
* [`Benchmark.options.onAbort`](#benchmarkoptionsonabort)
* [`Benchmark.options.onComplete`](#benchmarkoptionsoncomplete)
* [`Benchmark.options.onCycle`](#benchmarkoptionsoncycle)
* [`Benchmark.options.onError`](#benchmarkoptionsonerror)
* [`Benchmark.options.onReset`](#benchmarkoptionsonreset)
* [`Benchmark.options.onStart`](#benchmarkoptionsonstart)

<!-- /div -->


<!-- div -->

## `Benchmark.platform`
* [`Benchmark.platform`](#benchmarkplatform)
* [`Benchmark.platform.description`](#benchmarkplatformdescription)
* [`Benchmark.platform.layout`](#benchmarkplatformlayout)
* [`Benchmark.platform.manufacturer`](#benchmarkplatformmanufacturer)
* [`Benchmark.platform.name`](#benchmarkplatformname)
* [`Benchmark.platform.os`](#benchmarkplatformos)
* [`Benchmark.platform.prerelease`](#benchmarkplatformprerelease)
* [`Benchmark.platform.product`](#benchmarkplatformproduct)
* [`Benchmark.platform.version`](#benchmarkplatformversion)
* [`Benchmark.platform.toString`](#benchmarkplatformtostring)

<!-- /div -->


<!-- div -->

## `Benchmark.support`
* [`Benchmark.support`](#benchmarksupport)
* [`Benchmark.support.air`](#benchmarksupportair)
* [`Benchmark.support.argumentsClass`](#benchmarksupportargumentsclass)
* [`Benchmark.support.browser`](#benchmarksupportbrowser)
* [`Benchmark.support.charByIndex`](#benchmarksupportcharbyindex)
* [`Benchmark.support.charByOwnIndex`](#benchmarksupportcharbyownindex)
* [`Benchmark.support.decompilation`](#benchmarksupportdecompilation)
* [`Benchmark.support.descriptors`](#benchmarksupportdescriptors)
* [`Benchmark.support.getAllKeys`](#benchmarksupportgetallkeys)
* [`Benchmark.support.iteratesOwnLast`](#benchmarksupportiteratesownfirst)
* [`Benchmark.support.java`](#benchmarksupportjava)
* [`Benchmark.support.nodeClass`](#benchmarksupportnodeclass)
* [`Benchmark.support.timeout`](#benchmarksupporttimeout)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`
* [`Benchmark.prototype.error`](#benchmarkprototypeerror)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`
* [`Benchmark.prototype.stats`](#benchmarkprototypestats)
* [`Benchmark.prototype.stats.deviation`](#benchmark-statsdeviation)
* [`Benchmark.prototype.stats.mean`](#benchmark-statsmean)
* [`Benchmark.prototype.stats.moe`](#benchmark-statsmoe)
* [`Benchmark.prototype.stats.rme`](#benchmark-statsrme)
* [`Benchmark.prototype.stats.sample`](#benchmark-statssample)
* [`Benchmark.prototype.stats.sem`](#benchmark-statssem)
* [`Benchmark.prototype.stats.variance`](#benchmark-statsvariance)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`
* [`Benchmark.prototype.times`](#benchmarkprototypetimes)
* [`Benchmark.prototype.times.cycle`](#benchmark-timescycle)
* [`Benchmark.prototype.times.elapsed`](#benchmark-timeselapsed)
* [`Benchmark.prototype.times.period`](#benchmark-timesperiod)
* [`Benchmark.prototype.times.timeStamp`](#benchmark-timestimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`
* [`Benchmark.Deferred`](#benchmarkdeferredclone)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`
* [`Benchmark.Deferred.prototype.benchmark`](#benchmarkdeferredprototypebenchmark)
* [`Benchmark.Deferred.prototype.cycles`](#benchmarkdeferredprototypecycles)
* [`Benchmark.Deferred.prototype.elapsed`](#benchmarkdeferredprototypeelapsed)
* [`Benchmark.Deferred.prototype.resolve`](#benchmarkdeferredprototyperesolve)
* [`Benchmark.Deferred.prototype.timeStamp`](#benchmarkdeferredprototypetimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Event`
* [`Benchmark.Event`](#benchmarkeventtype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`
* [`Benchmark.Event.prototype.aborted`](#benchmarkeventprototypeaborted)
* [`Benchmark.Event.prototype.cancelled`](#benchmarkeventprototypecancelled)
* [`Benchmark.Event.prototype.result`](#benchmarkeventprototyperesult)
* [`Benchmark.Event.prototype.timeStamp`](#benchmarkeventprototypetimestamp)
* [`Benchmark.Event.prototype.type`](#benchmarkeventprototypetype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`
* [`Benchmark.Event.prototype.currentTarget`](#benchmarkeventprototypecurrenttarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`
* [`Benchmark.Event.prototype.target`](#benchmarkeventprototypetarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite`
* [`Benchmark.Suite`](#benchmarksuitename--options)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`
* [`Benchmark.Suite.prototype.aborted`](#benchmarksuiteprototypeaborted)
* [`Benchmark.Suite.prototype.length`](#benchmarksuiteprototypelength)
* [`Benchmark.Suite.prototype.running`](#benchmarksuiteprototyperunning)
* [`Benchmark.Suite.prototype.abort`](#benchmarksuiteprototypeabort)
* [`Benchmark.Suite.prototype.add`](#benchmarksuiteprototypeaddname-fn--options)
* [`Benchmark.Suite.prototype.clone`](#benchmarksuiteprototypecloneoptions)
* [`Benchmark.Suite.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.Suite.prototype.filter`](#benchmarksuiteprototypefiltercallback)
* [`Benchmark.Suite.prototype.forEach`](#benchmarksuiteprototypeforeachcallback)
* [`Benchmark.Suite.prototype.indexOf`](#benchmarksuiteprototypeindexofvalue)
* [`Benchmark.Suite.prototype.invoke`](#benchmarksuiteprototypeinvokename--arg1-arg2-)
* [`Benchmark.Suite.prototype.join`](#benchmarksuiteprototypejoinseparator-)
* [`Benchmark.Suite.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.Suite.prototype.map`](#benchmarksuiteprototypemapcallback)
* [`Benchmark.Suite.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.Suite.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.Suite.prototype.pluck`](#benchmarksuiteprototypepluckproperty)
* [`Benchmark.Suite.prototype.pop`](#benchmarksuiteprototypepop)
* [`Benchmark.Suite.prototype.push`](#benchmarksuiteprototypepush)
* [`Benchmark.Suite.prototype.reduce`](#benchmarksuiteprototypereducecallback-accumulator)
* [`Benchmark.Suite.prototype.reset`](#benchmarksuiteprototypereset)
* [`Benchmark.Suite.prototype.reverse`](#benchmarksuiteprototypereverse)
* [`Benchmark.Suite.prototype.run`](#benchmarksuiteprototyperunoptions)
* [`Benchmark.Suite.prototype.shift`](#benchmarksuiteprototypeshift)
* [`Benchmark.Suite.prototype.slice`](#benchmarksuiteprototypeslicestart-end)
* [`Benchmark.Suite.prototype.sort`](#benchmarksuiteprototypesortcomparefnnull)
* [`Benchmark.Suite.prototype.splice`](#benchmarksuiteprototypesplicestart-deletecount--val1-val2-)
* [`Benchmark.Suite.prototype.unshift`](#benchmarksuiteprototypeunshift)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`
* [`Benchmark.Suite.options`](#benchmarksuiteoptions)
* [`Benchmark.Suite.options.name`](#benchmarksuiteoptionsname)

<!-- /div -->


<!-- /div -->


<!-- div -->


<!-- div -->

## `Benchmark`

<!-- div -->

### <a id="benchmarkname-fn--options"></a>`Benchmark(name, fn [, options={}])`
<a href="#benchmarkname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L404 "View in source") [&#x24C9;][1]

The Benchmark constructor.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var bench = new Benchmark(fn);

// or using a name first
var bench = new Benchmark('foo', fn);

// or with options
var bench = new Benchmark('foo', fn, {

  // displayed by Benchmark#toString if `name` is not available
  'id': 'xyz',

  // called when the benchmark starts running
  'onStart': onStart,

  // called after each run cycle
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the benchmark completes running
  'onComplete': onComplete,

  // compiled/called before the test loop
  'setup': setup,

  // compiled/called after the test loop
  'teardown': teardown
});

// or name and options
var bench = new Benchmark('foo', {

  // a flag to indicate the benchmark is deferred
  'defer': true,

  // benchmark test function
  'fn': function(deferred) {
    // call resolve() when the deferred test is finished
    deferred.resolve();
  }
});

// or options only
var bench = new Benchmark({

  // benchmark name
  'name': 'foo',

  // benchmark test as a string
  'fn': '[1,2,3,4].sort()'
});

// a test's `this` binding is set to the benchmark instance
var bench = new Benchmark('foo', function() {
  'My name is '.concat(this.name); // My name is foo
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkversion"></a>`Benchmark.version`
<a href="#benchmarkversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3267 "View in source") [&#x24C9;][1]

*(String)*: The semantic version number.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeepclonevalue"></a>`Benchmark.deepClone(value)`
<a href="#benchmarkdeepclonevalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1225 "View in source") [&#x24C9;][1]

A deep clone utility.

#### Arguments
1. `value` *(Mixed)*: The value to clone.

#### Returns
*(Mixed)*: The cloned value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeachobject-callback-thisarg"></a>`Benchmark.each(object, callback, thisArg)`
<a href="#benchmarkeachobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1400 "View in source") [&#x24C9;][1]

An iteration utility for arrays and objects. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Array|Object)*: The object to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array, Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkextenddestination--source"></a>`Benchmark.extend(destination [, source={}])`
<a href="#benchmarkextenddestination--source">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1446 "View in source") [&#x24C9;][1]

Copies enumerable properties from the source(s) object to the destination object.

#### Arguments
1. `destination` *(Object)*: The destination object.
2. `[source={}]` *(Object)*: The source object.

#### Returns
*(Object)*: The destination object.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkfilterarray-callback-thisarg"></a>`Benchmark.filter(array, callback, thisArg)`
<a href="#benchmarkfilterarray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1485 "View in source") [&#x24C9;][1]

A generic `Array#filter` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function|String)*: The function/alias called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values that passed callback filter.

#### Example
~~~ js
// get odd numbers
Benchmark.filter([1, 2, 3, 4, 5], function(n) {
  return n % 2;
}); // -> [1, 3, 5];

// get fastest benchmarks
Benchmark.filter(benches, 'fastest');

// get slowest benchmarks
Benchmark.filter(benches, 'slowest');

// get benchmarks that completed without erroring
Benchmark.filter(benches, 'successful');
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforeacharray-callback-thisarg"></a>`Benchmark.forEach(array, callback, thisArg)`
<a href="#benchmarkforeacharray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1518 "View in source") [&#x24C9;][1]

A generic `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: Returns the array iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkformatnumbernumber"></a>`Benchmark.formatNumber(number)`
<a href="#benchmarkformatnumbernumber">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1557 "View in source") [&#x24C9;][1]

Converts a number to a more readable comma-separated string representation.

#### Arguments
1. `number` *(Number)*: The number to convert.

#### Returns
*(String)*: The more readable string representation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforownobject-callback-thisarg"></a>`Benchmark.forOwn(object, callback, thisArg)`
<a href="#benchmarkforownobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1545 "View in source") [&#x24C9;][1]

Iterates over an object's own properties, executing the `callback` for each. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `callback` *(Function)*: The function executed per own property.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkhaskeyobject-key"></a>`Benchmark.hasKey(object, key)`
<a href="#benchmarkhaskeyobject-key">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1572 "View in source") [&#x24C9;][1]

Checks if an object has the specified key as a direct property.

#### Arguments
1. `object` *(Object)*: The object to check.
2. `key` *(String)*: The key to check for.

#### Returns
*(Boolean)*: Returns `true` if key is a direct property, else `false`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkindexofarray-value--fromindex0"></a>`Benchmark.indexOf(array, value [, fromIndex=0])`
<a href="#benchmarkindexofarray-value--fromindex0">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1608 "View in source") [&#x24C9;][1]

A generic `Array#indexOf` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `value` *(Mixed)*: The value to search for.
3. `[fromIndex=0]` *(Number)*: The index to start searching from.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinterpolatestring-object"></a>`Benchmark.interpolate(string, object)`
<a href="#benchmarkinterpolatestring-object">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1630 "View in source") [&#x24C9;][1]

Modify a string by replacing named tokens with matching object property values.

#### Arguments
1. `string` *(String)*: The string to modify.
2. `object` *(Object)*: The template object.

#### Returns
*(String)*: The modified string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinvokebenches-name--arg1-arg2-"></a>`Benchmark.invoke(benches, name [, arg1, arg2, ...])`
<a href="#benchmarkinvokebenches-name--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1677 "View in source") [&#x24C9;][1]

Invokes a method on all items in an array.

#### Arguments
1. `benches` *(Array)*: Array of benchmarks to iterate over.
2. `name` *(String|Object)*: The name of the method to invoke OR options object.
3. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

#### Example
~~~ js
// invoke `reset` on all benchmarks
Benchmark.invoke(benches, 'reset');

// invoke `emit` with arguments
Benchmark.invoke(benches, 'emit', 'complete', listener);

// invoke `run(true)`, treat benchmarks as a queue, and register invoke callbacks
Benchmark.invoke(benches, {

  // invoke the `run` method
  'name': 'run',

  // pass a single argument
  'args': true,

  // treat as queue, removing benchmarks from front of `benches` until empty
  'queued': true,

  // called before any benchmarks have been invoked.
  'onStart': onStart,

  // called between invoking benchmarks
  'onCycle': onCycle,

  // called after all benchmarks have been invoked.
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkjoinobject--separator1--separator2:"></a>`Benchmark.join(object [, separator1=',', separator2=': '])`
<a href="#benchmarkjoinobject--separator1--separator2:">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1831 "View in source") [&#x24C9;][1]

Creates a string of joined array values or object key-value pairs.

#### Arguments
1. `object` *(Array|Object)*: The object to operate on.
2. `[separator1=',']` *(String)*: The separator used between key-value pairs.
3. `[separator2=': ']` *(String)*: The separator used between keys and values.

#### Returns
*(String)*: The joined result.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkmaparray-callback-thisarg"></a>`Benchmark.map(array, callback, thisArg)`
<a href="#benchmarkmaparray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1853 "View in source") [&#x24C9;][1]

A generic `Array#map` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkpluckarray-property"></a>`Benchmark.pluck(array, property)`
<a href="#benchmarkpluckarray-property">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1869 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all items in an array.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkreducearray-callback-accumulator"></a>`Benchmark.reduce(array, callback, accumulator)`
<a href="#benchmarkreducearray-callback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1885 "View in source") [&#x24C9;][1]

A generic `Array#reduce` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype`

<!-- div -->

### <a id="benchmarkprototypeaborted"></a>`Benchmark.prototype.aborted`
<a href="#benchmarkprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3377 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompiled"></a>`Benchmark.prototype.compiled`
<a href="#benchmarkprototypecompiled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3353 "View in source") [&#x24C9;][1]

*(Function, String)*: The compiled test function.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecount"></a>`Benchmark.prototype.count`
<a href="#benchmarkprototypecount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3329 "View in source") [&#x24C9;][1]

*(Number)*: The number of times a test was executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecycles"></a>`Benchmark.prototype.cycles`
<a href="#benchmarkprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3337 "View in source") [&#x24C9;][1]

*(Number)*: The number of cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypefn"></a>`Benchmark.prototype.fn`
<a href="#benchmarkprototypefn">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3369 "View in source") [&#x24C9;][1]

*(Function, String)*: The test to benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypehz"></a>`Benchmark.prototype.hz`
<a href="#benchmarkprototypehz">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3345 "View in source") [&#x24C9;][1]

*(Number)*: The number of executions per second.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunning"></a>`Benchmark.prototype.running`
<a href="#benchmarkprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3385 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypesetup"></a>`Benchmark.prototype.setup`
<a href="#benchmarkprototypesetup">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3448 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **before** the test loop.

#### Example
~~~ js
// basic usage
var bench = Benchmark({
  'setup': function() {
    var c = this.count,
        element = document.getElementById('container');
    while (c--) {
      element.appendChild(document.createElement('div'));
    }
  },
  'fn': function() {
    element.removeChild(element.lastChild);
  }
});

// compiles to something like:
var c = this.count,
    element = document.getElementById('container');
while (c--) {
  element.appendChild(document.createElement('div'));
}
var start = new Date;
while (count--) {
  element.removeChild(element.lastChild);
}
var end = new Date - start;

// or using strings
var bench = Benchmark({
  'setup': '\
    var a = 0;\n\
    (function() {\n\
      (function() {\n\
        (function() {',
  'fn': 'a += 1;',
  'teardown': '\
         }())\n\
       }())\n\
     }())'
});

// compiles to something like:
var a = 0;
(function() {
  (function() {
    (function() {
      var start = new Date;
      while (count--) {
        a += 1;
      }
      var end = new Date - start;
    }())
  }())
}())
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeteardown"></a>`Benchmark.prototype.teardown`
<a href="#benchmarkprototypeteardown">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3456 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **after** the test loop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeabort"></a>`Benchmark.prototype.abort()`
<a href="#benchmarkprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2218 "View in source") [&#x24C9;][1]

Aborts the benchmark without recording times.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecloneoptions"></a>`Benchmark.prototype.clone(options)`
<a href="#benchmarkprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2257 "View in source") [&#x24C9;][1]

Creates a new benchmark using the same test and options.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new benchmark instance.

#### Example
~~~ js
var bizarro = bench.clone({
  'name': 'doppelganger'
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompareother"></a>`Benchmark.prototype.compare(other)`
<a href="#benchmarkprototypecompareother">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2280 "View in source") [&#x24C9;][1]

Determines if a benchmark is faster than another.

#### Arguments
1. `other` *(Object)*: The benchmark to compare.

#### Returns
*(Number)*: Returns `-1` if slower, `1` if faster, and `0` if indeterminate.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypereset"></a>`Benchmark.prototype.reset()`
<a href="#benchmarkprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2334 "View in source") [&#x24C9;][1]

Reset properties and abort if running.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunoptions"></a>`Benchmark.prototype.run([options={}])`
<a href="#benchmarkprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3000 "View in source") [&#x24C9;][1]

Runs the benchmark.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
bench.run();

// or with options
bench.run({ 'async': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypetostring"></a>`Benchmark.prototype.toString()`
<a href="#benchmarkprototypetostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2405 "View in source") [&#x24C9;][1]

Displays relevant benchmark information when coerced to a string.

#### Returns
*(String)*: A string representation of the benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.options`

<!-- div -->

### <a id="benchmarkoptions"></a>`Benchmark.options`
<a href="#benchmarkoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3049 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by benchmark instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsasync"></a>`Benchmark.options.async`
<a href="#benchmarkoptionsasync">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3058 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that benchmark cycles will execute asynchronously by default.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdefer"></a>`Benchmark.options.defer`
<a href="#benchmarkoptionsdefer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3066 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that the benchmark clock is deferred.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdelay"></a>`Benchmark.options.delay`
<a href="#benchmarkoptionsdelay">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3073 "View in source") [&#x24C9;][1]

*(Number)*: The delay between test cycles *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsid"></a>`Benchmark.options.id`
<a href="#benchmarkoptionsid">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3082 "View in source") [&#x24C9;][1]

*(String)*: Displayed by Benchmark#toString when a `name` is not available *(auto-generated if absent)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsinitcount"></a>`Benchmark.options.initCount`
<a href="#benchmarkoptionsinitcount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3090 "View in source") [&#x24C9;][1]

*(Number)*: The default number of times to execute a test on a benchmark's first cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmaxtime"></a>`Benchmark.options.maxTime`
<a href="#benchmarkoptionsmaxtime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3099 "View in source") [&#x24C9;][1]

*(Number)*: The maximum time a benchmark is allowed to run before finishing *(secs)*. Note: Cycle delays aren't counted toward the maximum time.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsminsamples"></a>`Benchmark.options.minSamples`
<a href="#benchmarkoptionsminsamples">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3107 "View in source") [&#x24C9;][1]

*(Number)*: The minimum sample size required to perform statistical analysis.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmintime"></a>`Benchmark.options.minTime`
<a href="#benchmarkoptionsmintime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3115 "View in source") [&#x24C9;][1]

*(Number)*: The time needed to reduce the percent uncertainty of measurement to `1`% *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsname"></a>`Benchmark.options.name`
<a href="#benchmarkoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3123 "View in source") [&#x24C9;][1]

*(String)*: The name of the benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonabort"></a>`Benchmark.options.onAbort`
<a href="#benchmarkoptionsonabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3131 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncomplete"></a>`Benchmark.options.onComplete`
<a href="#benchmarkoptionsoncomplete">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3139 "View in source") [&#x24C9;][1]

An event listener called when the benchmark completes running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncycle"></a>`Benchmark.options.onCycle`
<a href="#benchmarkoptionsoncycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3147 "View in source") [&#x24C9;][1]

An event listener called after each run cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonerror"></a>`Benchmark.options.onError`
<a href="#benchmarkoptionsonerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3155 "View in source") [&#x24C9;][1]

An event listener called when a test errors.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonreset"></a>`Benchmark.options.onReset`
<a href="#benchmarkoptionsonreset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3163 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is reset.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonstart"></a>`Benchmark.options.onStart`
<a href="#benchmarkoptionsonstart">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3171 "View in source") [&#x24C9;][1]

An event listener called when the benchmark starts running.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.platform`

<!-- div -->

### <a id="benchmarkplatform"></a>`Benchmark.platform`
<a href="#benchmarkplatform">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3182 "View in source") [&#x24C9;][1]

*(Object)*: Platform object with properties describing things like browser name, version, and operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformdescription"></a>`Benchmark.platform.description`
<a href="#benchmarkplatformdescription">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3190 "View in source") [&#x24C9;][1]

*(String)*: The platform description.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformlayout"></a>`Benchmark.platform.layout`
<a href="#benchmarkplatformlayout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3198 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser layout engine.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformmanufacturer"></a>`Benchmark.platform.manufacturer`
<a href="#benchmarkplatformmanufacturer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3222 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product's manufacturer.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformname"></a>`Benchmark.platform.name`
<a href="#benchmarkplatformname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3214 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser/environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformos"></a>`Benchmark.platform.os`
<a href="#benchmarkplatformos">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3230 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformprerelease"></a>`Benchmark.platform.prerelease`
<a href="#benchmarkplatformprerelease">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3238 "View in source") [&#x24C9;][1]

*(String, Null)*: The alpha/beta release indicator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformproduct"></a>`Benchmark.platform.product`
<a href="#benchmarkplatformproduct">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3206 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product hosting the browser.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformversion"></a>`Benchmark.platform.version`
<a href="#benchmarkplatformversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3246 "View in source") [&#x24C9;][1]

*(String, Null)*: The browser/environment version.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformtostring"></a>`Benchmark.platform.toString()`
<a href="#benchmarkplatformtostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3255 "View in source") [&#x24C9;][1]

Return platform description when the platform object is coerced to a string.

#### Returns
*(String)*: The platform description.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.support`

<!-- div -->

### <a id="benchmarksupport"></a>`Benchmark.support`
<a href="#benchmarksupport">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L135 "View in source") [&#x24C9;][1]

*(Object)*: An object used to flag environments/features.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportair"></a>`Benchmark.support.air`
<a href="#benchmarksupportair">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L145 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect Adobe AIR.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportargumentsclass"></a>`Benchmark.support.argumentsClass`
<a href="#benchmarksupportargumentsclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L153 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if `arguments` objects have the correct internal [[Class]] value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportbrowser"></a>`Benchmark.support.browser`
<a href="#benchmarksupportbrowser">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L161 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if in a browser environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyindex"></a>`Benchmark.support.charByIndex`
<a href="#benchmarksupportcharbyindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L169 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings support accessing characters by index.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyownindex"></a>`Benchmark.support.charByOwnIndex`
<a href="#benchmarksupportcharbyownindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L179 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings have indexes as own properties.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdecompilation"></a>`Benchmark.support.decompilation`
<a href="#benchmarksupportdecompilation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L207 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if functions support decompilation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdescriptors"></a>`Benchmark.support.descriptors`
<a href="#benchmarksupportdescriptors">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L228 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ property descriptor API.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportgetallkeys"></a>`Benchmark.support.getAllKeys`
<a href="#benchmarksupportgetallkeys">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L242 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ Object.getOwnPropertyNames().

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportiteratesownfirst"></a>`Benchmark.support.iteratesOwnFirst`
<a href="#benchmarksupportiteratesownfirst">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L255 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if own properties are iterated before inherited properties *(all but IE < `9`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportjava"></a>`Benchmark.support.java`
<a href="#benchmarksupportjava">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L190 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if Java is enabled/exposed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportnodeclass"></a>`Benchmark.support.nodeClass`
<a href="#benchmarksupportnodeclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L272 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if a node's [[Class]] is resolvable *(all but IE < `9`)* and that the JS engine errors when attempting to coerce an object to a string without a `toString` property value of `typeof` "function".

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupporttimeout"></a>`Benchmark.support.timeout`
<a href="#benchmarksupporttimeout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L198 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if the Timers API exists.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`

<!-- div -->

### <a id="benchmarkprototypeerror"></a>`Benchmark.prototype.error`
<a href="#benchmarkprototypeerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3361 "View in source") [&#x24C9;][1]

*(Object)*: The error object if the test failed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`

<!-- div -->

### <a id="benchmarkprototypestats"></a>`Benchmark.prototype.stats`
<a href="#benchmarkprototypestats">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3464 "View in source") [&#x24C9;][1]

*(Object)*: An object of stats including mean, margin or error, and standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsdeviation"></a>`Benchmark.prototype.stats.deviation`
<a href="#benchmark-statsdeviation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3496 "View in source") [&#x24C9;][1]

*(Number)*: The sample standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmean"></a>`Benchmark.prototype.stats.mean`
<a href="#benchmark-statsmean">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3504 "View in source") [&#x24C9;][1]

*(Number)*: The sample arithmetic mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmoe"></a>`Benchmark.prototype.stats.moe`
<a href="#benchmark-statsmoe">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3472 "View in source") [&#x24C9;][1]

*(Number)*: The margin of error.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsrme"></a>`Benchmark.prototype.stats.rme`
<a href="#benchmark-statsrme">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3480 "View in source") [&#x24C9;][1]

*(Number)*: The relative margin of error *(expressed as a percentage of the mean)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssample"></a>`Benchmark.prototype.stats.sample`
<a href="#benchmark-statssample">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3512 "View in source") [&#x24C9;][1]

*(Array)*: The array of sampled periods.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssem"></a>`Benchmark.prototype.stats.sem`
<a href="#benchmark-statssem">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3488 "View in source") [&#x24C9;][1]

*(Number)*: The standard error of the mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsvariance"></a>`Benchmark.prototype.stats.variance`
<a href="#benchmark-statsvariance">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3520 "View in source") [&#x24C9;][1]

*(Number)*: The sample variance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`

<!-- div -->

### <a id="benchmarkprototypetimes"></a>`Benchmark.prototype.times`
<a href="#benchmarkprototypetimes">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3529 "View in source") [&#x24C9;][1]

*(Object)*: An object of timing data including cycle, elapsed, period, start, and stop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timescycle"></a>`Benchmark.prototype.times.cycle`
<a href="#benchmark-timescycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3537 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the last cycle *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timeselapsed"></a>`Benchmark.prototype.times.elapsed`
<a href="#benchmark-timeselapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3545 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timesperiod"></a>`Benchmark.prototype.times.period`
<a href="#benchmark-timesperiod">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3553 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to execute the test once *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timestimestamp"></a>`Benchmark.prototype.times.timeStamp`
<a href="#benchmark-timestimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3561 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`

<!-- div -->

### <a id="benchmarkdeferredclone"></a>`Benchmark.Deferred(clone)`
<a href="#benchmarkdeferredclone">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L445 "View in source") [&#x24C9;][1]

The Deferred constructor.

#### Arguments
1. `clone` *(Object)*: The cloned benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`

<!-- div -->

### <a id="benchmarkdeferredprototypebenchmark"></a>`Benchmark.Deferred.prototype.benchmark`
<a href="#benchmarkdeferredprototypebenchmark">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3605 "View in source") [&#x24C9;][1]

*(Object)*: The deferred benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypecycles"></a>`Benchmark.Deferred.prototype.cycles`
<a href="#benchmarkdeferredprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3613 "View in source") [&#x24C9;][1]

*(Number)*: The number of deferred cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypeelapsed"></a>`Benchmark.Deferred.prototype.elapsed`
<a href="#benchmarkdeferredprototypeelapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3621 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the deferred benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototyperesolve"></a>`Benchmark.Deferred.prototype.resolve`
<a href="#benchmarkdeferredprototyperesolve">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1188 "View in source") [&#x24C9;][1]

*(Unknown)*: Handles cycling/completing the deferred benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypetimestamp"></a>`Benchmark.Deferred.prototype.timeStamp`
<a href="#benchmarkdeferredprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3629 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the deferred benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event`

<!-- div -->

### <a id="benchmarkeventtype"></a>`Benchmark.Event(type)`
<a href="#benchmarkeventtype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L461 "View in source") [&#x24C9;][1]

The Event constructor.

#### Arguments
1. `type` *(String|Object)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`

<!-- div -->

### <a id="benchmarkeventprototypeaborted"></a>`Benchmark.Event.prototype.aborted`
<a href="#benchmarkeventprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3645 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the emitters listener iteration is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypecancelled"></a>`Benchmark.Event.prototype.cancelled`
<a href="#benchmarkeventprototypecancelled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3653 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the default action is cancelled.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototyperesult"></a>`Benchmark.Event.prototype.result`
<a href="#benchmarkeventprototyperesult">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3669 "View in source") [&#x24C9;][1]

*(Mixed)*: The return value of the last executed listener.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetimestamp"></a>`Benchmark.Event.prototype.timeStamp`
<a href="#benchmarkeventprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3685 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the event was created *(ms)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetype"></a>`Benchmark.Event.prototype.type`
<a href="#benchmarkeventprototypetype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3693 "View in source") [&#x24C9;][1]

*(String)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`

<!-- div -->

### <a id="benchmarkeventprototypecurrenttarget"></a>`Benchmark.Event.prototype.currentTarget`
<a href="#benchmarkeventprototypecurrenttarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3661 "View in source") [&#x24C9;][1]

*(Object)*: The object whose listeners are currently being processed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`

<!-- div -->

### <a id="benchmarkeventprototypetarget"></a>`Benchmark.Event.prototype.target`
<a href="#benchmarkeventprototypetarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3677 "View in source") [&#x24C9;][1]

*(Object)*: The object to which the event was originally emitted.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite`

<!-- div -->

### <a id="benchmarksuitename--options"></a>`Benchmark.Suite(name [, options={}])`
<a href="#benchmarksuitename--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L507 "View in source") [&#x24C9;][1]

The Suite constructor.

#### Arguments
1. `name` *(String)*: A name to identify the suite.
2. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var suite = new Benchmark.Suite;

// or using a name first
var suite = new Benchmark.Suite('foo');

// or with options
var suite = new Benchmark.Suite('foo', {

  // called when the suite starts running
  'onStart': onStart,

  // called between running benchmarks
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the suite completes running
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`

<!-- div -->

### <a id="benchmarksuiteprototypeaborted"></a>`Benchmark.Suite.prototype.aborted`
<a href="#benchmarksuiteprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3734 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypelength"></a>`Benchmark.Suite.prototype.length`
<a href="#benchmarksuiteprototypelength">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3726 "View in source") [&#x24C9;][1]

*(Number)*: The number of benchmarks in the suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunning"></a>`Benchmark.Suite.prototype.running`
<a href="#benchmarksuiteprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3742 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeabort"></a>`Benchmark.Suite.prototype.abort()`
<a href="#benchmarksuiteprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1902 "View in source") [&#x24C9;][1]

Aborts all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeaddname-fn--options"></a>`Benchmark.Suite.prototype.add(name, fn [, options={}])`
<a href="#benchmarksuiteprototypeaddname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1962 "View in source") [&#x24C9;][1]

Adds a test to the benchmark suite.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
suite.add(fn);

// or using a name first
suite.add('foo', fn);

// or with options
suite.add('foo', fn, {
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or name and options
suite.add('foo', {
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or options only
suite.add({
  'name': 'foo',
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypecloneoptions"></a>`Benchmark.Suite.prototype.clone(options)`
<a href="#benchmarksuiteprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1981 "View in source") [&#x24C9;][1]

Creates a new suite with cloned benchmarks.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypefiltercallback"></a>`Benchmark.Suite.prototype.filter(callback)`
<a href="#benchmarksuiteprototypefiltercallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2004 "View in source") [&#x24C9;][1]

An `Array#filter` like method.

#### Arguments
1. `callback` *(Function|String)*: The function/alias called per iteration.

#### Returns
*(Object)*: A new suite of benchmarks that passed callback filter.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeforeachcallback"></a>`Benchmark.Suite.prototype.forEach(callback)`
<a href="#benchmarksuiteprototypeforeachcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3752 "View in source") [&#x24C9;][1]

An `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Object)*: The suite iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeindexofvalue"></a>`Benchmark.Suite.prototype.indexOf(value)`
<a href="#benchmarksuiteprototypeindexofvalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3761 "View in source") [&#x24C9;][1]

An `Array#indexOf` like method.

#### Arguments
1. `value` *(Mixed)*: The value to search for.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeinvokename--arg1-arg2-"></a>`Benchmark.Suite.prototype.invoke(name [, arg1, arg2, ...])`
<a href="#benchmarksuiteprototypeinvokename--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3771 "View in source") [&#x24C9;][1]

Invokes a method on all benchmarks in the suite.

#### Arguments
1. `name` *(String|Object)*: The name of the method to invoke OR options object.
2. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypejoinseparator-"></a>`Benchmark.Suite.prototype.join([separator=','])`
<a href="#benchmarksuiteprototypejoinseparator-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3780 "View in source") [&#x24C9;][1]

Converts the suite of benchmarks to a string.

#### Arguments
1. `[separator=',']` *(String)*: A string to separate each element of the array.

#### Returns
*(String)*: The string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypemapcallback"></a>`Benchmark.Suite.prototype.map(callback)`
<a href="#benchmarksuiteprototypemapcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3789 "View in source") [&#x24C9;][1]

An `Array#map` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepluckproperty"></a>`Benchmark.Suite.prototype.pluck(property)`
<a href="#benchmarksuiteprototypepluckproperty">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3798 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all benchmarks in the suite.

#### Arguments
1. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepop"></a>`Benchmark.Suite.prototype.pop()`
<a href="#benchmarksuiteprototypepop">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3806 "View in source") [&#x24C9;][1]

Removes the last benchmark from the suite and returns it.

#### Returns
*(Mixed)*: The removed benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepush"></a>`Benchmark.Suite.prototype.push()`
<a href="#benchmarksuiteprototypepush">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3814 "View in source") [&#x24C9;][1]

Appends benchmarks to the suite.

#### Returns
*(Number)*: The suite's new length.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereducecallback-accumulator"></a>`Benchmark.Suite.prototype.reduce(callback, accumulator)`
<a href="#benchmarksuiteprototypereducecallback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3833 "View in source") [&#x24C9;][1]

An `Array#reduce` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.
2. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereset"></a>`Benchmark.Suite.prototype.reset()`
<a href="#benchmarksuiteprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2019 "View in source") [&#x24C9;][1]

Resets all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereverse"></a>`Benchmark.Suite.prototype.reverse()`
<a href="#benchmarksuiteprototypereverse">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L638 "View in source") [&#x24C9;][1]

Rearrange the host array's elements in reverse order.

#### Returns
*(Array)*: The reversed array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunoptions"></a>`Benchmark.Suite.prototype.run([options={}])`
<a href="#benchmarksuiteprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2056 "View in source") [&#x24C9;][1]

Runs the suite.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The suite instance.

#### Example
~~~ js
// basic usage
suite.run();

// or with options
suite.run({ 'async': true, 'queued': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeshift"></a>`Benchmark.Suite.prototype.shift()`
<a href="#benchmarksuiteprototypeshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L671 "View in source") [&#x24C9;][1]

Removes the first element of the host array and returns it.

#### Returns
*(Mixed)*: The first element of the array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeslicestart-end"></a>`Benchmark.Suite.prototype.slice(start, end)`
<a href="#benchmarksuiteprototypeslicestart-end">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L684 "View in source") [&#x24C9;][1]

Creates an array of the host array's elements from the start index up to, but not including, the end index.

#### Arguments
1. `start` *(Number)*: The starting index.
2. `end` *(Number)*: The end index.

#### Returns
*(Array)*: The new array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesortcomparefnnull"></a>`Benchmark.Suite.prototype.sort([compareFn=null])`
<a href="#benchmarksuiteprototypesortcomparefnnull">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3823 "View in source") [&#x24C9;][1]

Sorts the benchmarks of the suite.

#### Arguments
1. `[compareFn=null]` *(Function)*: A function that defines the sort order.

#### Returns
*(Object)*: The sorted suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesplicestart-deletecount--val1-val2-"></a>`Benchmark.Suite.prototype.splice(start, deleteCount [, val1, val2, ...])`
<a href="#benchmarksuiteprototypesplicestart-deletecount--val1-val2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L714 "View in source") [&#x24C9;][1]

Allows removing a range of elements and/or inserting elements into the host array.

#### Arguments
1. `start` *(Number)*: The start index.
2. `deleteCount` *(Number)*: The number of elements to delete.
3. `[val1, val2, ...]` *(Mixed)*: values to insert at the `start` index.

#### Returns
*(Array)*: An array of removed elements.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeunshift"></a>`Benchmark.Suite.prototype.unshift()`
<a href="#benchmarksuiteprototypeunshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L749 "View in source") [&#x24C9;][1]

Appends arguments to the host array.

#### Returns
*(Number)*: The new length.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`

<!-- div -->

### <a id="benchmarksuiteoptions"></a>`Benchmark.Suite.options`
<a href="#benchmarksuiteoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3705 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by suite instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteoptionsname"></a>`Benchmark.Suite.options.name`
<a href="#benchmarksuiteoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3713 "View in source") [&#x24C9;][1]

*(String)*: The name of the suite.

* * *

<!-- /div -->


<!-- /div -->


<!-- /div -->


  [1]: #Benchmark "Jump back to the TOC."# JSON 3 #

![JSON 3 Logo](http://bestiejs.github.io/json3/page/logo.png)

**JSON 3** is a modern JSON implementation compatible with a variety of JavaScript platforms, including Internet Explorer 6, Opera 7, Safari 2, and Netscape 6. The current version is **3.2.6**.

- [Development Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.js) *(40 KB; uncompressed with comments)*
- [Production Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.min.js) *(3.3 KB; compressed and `gzip`-ped)*

CDN copies are also available at [cdnjs](http://cdnjs.com/libraries/json3/) & [jsDelivr](http://www.jsdelivr.com/#!json3).

[JSON](http://json.org/) is a language-independent data interchange format based on a loose subset of the JavaScript grammar. Originally popularized by [Douglas Crockford](http://www.crockford.com/), the format was standardized in the [fifth edition](http://es5.github.com/) of the ECMAScript specification. The 5.1 edition, ratified in June 2011, incorporates several modifications to the grammar pertaining to the serialization of dates.

JSON 3 exposes two functions: `stringify()` for [serializing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/stringify) a JavaScript value to JSON, and `parse()` for [producing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/parse) a JavaScript value from a JSON source string. It is a **drop-in replacement** for [JSON 2](http://json.org/js). The functions behave exactly as described in the ECMAScript spec, **except** for the date serialization discrepancy noted below.

The JSON 3 parser does **not** use `eval` or regular expressions. This provides security and performance benefits in obsolete and mobile environments, where the margin is particularly significant. The complete [benchmark suite](http://jsperf.com/json3) is available on [jsPerf](http://jsperf.com/).

The project is [hosted on GitHub](http://git.io/json3), along with the [unit tests](http://bestiejs.github.io/json3/test/test_browser.html). It is part of the [BestieJS](https://github.com/bestiejs) family, a collection of best-in-class JavaScript libraries that promote cross-platform support, specification precedents, unit testing, and plenty of documentation.

# Changes from JSON 2 #

JSON 3...

* Correctly serializes primitive wrapper objects.
* Throws a `TypeError` when serializing cyclic structures (JSON 2 recurses until the call stack overflows).
* Utilizes **feature tests** to detect broken or incomplete *native* JSON implementations (JSON 2 only checks for the presence of the native functions). The tests are only executed once at runtime, so there is no additional performance cost when parsing or serializing values.

**As of v3.2.3**, JSON 3 is compatible with [Prototype](http://prototypejs.org) 1.6.1 and older.

In contrast to JSON 2, JSON 3 **does not**...

* Add `toJSON()` methods to the `Boolean`, `Number`, and `String` prototypes. These are not part of any standard, and are made redundant by the design of the `stringify()` implementation.
* Add `toJSON()` or `toISOString()` methods to `Date.prototype`. See the note about date serialization below.

## Date Serialization

**JSON 3 deviates from the specification in one important way**: it does not define `Date#toISOString()` or `Date#toJSON()`. This preserves CommonJS compatibility and avoids polluting native prototypes. Instead, date serialization is performed internally by the `stringify()` implementation: if a date object does not define a custom `toJSON()` method, it is serialized as a [simplified ISO 8601 date-time string](http://es5.github.com/#x15.9.1.15).

**Several native `Date#toJSON()` implementations produce date time strings that do *not* conform to the grammar outlined in the spec**. For instance, all versions of Safari 4, as well as JSON 2, fail to serialize extended years correctly. Furthermore, JSON 2 and older implementations omit the milliseconds from the date-time string (optional in ES 5, but required in 5.1). Finally, in all versions of Safari 4 and 5, serializing an invalid date will produce the string `"Invalid Date"`, rather than `null`. Because these environments exhibit other serialization bugs, however, JSON 3 will override the native `stringify()` implementation.

Portions of the date serialization code are adapted from the [`date-shim`](https://github.com/Yaffle/date-shim) project.

# Usage #

## Web Browsers

    <script src="http://bestiejs.github.io/json3/lib/json3.js"></script>
    <script>
      JSON.stringify({"Hello": 123});
      // => '{"Hello":123}'
      JSON.parse("[[1, 2, 3], 1, 2, 3, 4]", function (key, value) {
        if (typeof value == "number") {
          value = value % 2 ? "Odd" : "Even";
        }
        return value;
      });
      // => [["Odd", "Even", "Odd"], "Odd", "Even", "Odd", "Even"]
    </script>

## CommonJS Environments

    var JSON3 = require("./path/to/json3");
    JSON3.parse("[1, 2, 3]");
    // => [1, 2, 3]

## JavaScript Engines

    load("path/to/json3.js");
    JSON.stringify({"Hello": 123, "Good-bye": 456}, ["Hello"], "\t");
    // => '{\n\t"Hello": 123\n}'

# Compatibility #

JSON 3 has been **tested** with the following web browsers, CommonJS environments, and JavaScript engines.

## Web Browsers

- Windows [Internet Explorer](http://www.microsoft.com/windows/internet-explorer), version 6.0 and higher
- Mozilla [Firefox](http://www.mozilla.com/firefox), version 1.0 and higher
- Apple [Safari](http://www.apple.com/safari), version 2.0 and higher
- [Opera](http://www.opera.com) 7.02 and higher
- [Mozilla](http://sillydog.org/narchive/gecko.php) 1.0, [Netscape](http://sillydog.org/narchive/) 6.2.3, and [SeaMonkey](http://www.seamonkey-project.org/) 1.0 and higher

## CommonJS Environments

- [Node](http://nodejs.org/) 0.2.6 and higher
- [RingoJS](http://ringojs.org/) 0.4 and higher
- [Narwhal](http://narwhaljs.org/) 0.3.2 and higher

## JavaScript Engines

- Mozilla [Rhino](http://www.mozilla.org/rhino) 1.5R5 and higher
- WebKit [JSC](https://trac.webkit.org/wiki/JSC)
- Google [V8](http://code.google.com/p/v8)

## Known Incompatibilities

* Attempting to serialize the `arguments` object may produce inconsistent results across environments due to specification version differences. As a workaround, please convert the `arguments` object to an array first: `JSON.stringify([].slice.call(arguments, 0))`.

## Required Native Methods

JSON 3 assumes that the following methods exist and function as described in the ECMAScript specification:

- The `Number`, `String`, `Array`, `Object`, `Date`, `SyntaxError`, and `TypeError` constructors.
- `String.fromCharCode`
- `Object#toString`
- `Function#call`
- `Math.floor`
- `Number#toString`
- `Date#valueOf`
- `String.prototype`: `indexOf`, `charCodeAt`, `charAt`, `slice`.
- `Array.prototype`: `push`, `pop`, `join`.

# Contribute #

Check out a working copy of the JSON 3 source code with [Git](http://git-scm.com/):

    $ git clone git://github.com/bestiejs/json3.git
    $ cd json3
    $ git submodule update --init

If you'd like to contribute a feature or bug fix, you can [fork](http://help.github.com/fork-a-repo/) JSON 3, commit your changes, and [send a pull request](http://help.github.com/send-pull-requests/). Please make sure to update the unit tests in the `test` directory as well.

Alternatively, you can use the [GitHub issue tracker](https://github.com/bestiejs/json3/issues) to submit bug reports, feature requests, and questions, or send tweets to [@kitcambridge](http://twitter.com/kitcambridge).

JSON 3 is released under the [MIT License](http://kit.mit-license.org/).#object-keys <sup>[![Version Badge][2]][1]</sup>

[![Build Status][3]][4]
[![dependency status][5]][6]
[![dev dependency status][7]][8]
[![License][license-image]][license-url]
[![Downloads][downloads-image]][downloads-url]

[![npm badge][13]][1]

[![browser support][9]][10]

An Object.keys shim. Invoke its "shim" method to shim Object.keys if it is unavailable.

Most common usage:
```js
var keys = Object.keys || require('object-keys');
```

## Example

```js
var keys = require('object-keys');
var assert = require('assert');
var obj = {
	a: true,
	b: true,
	c: true
};

assert.deepEqual(keys(obj), ['a', 'b', 'c']);
```

```js
var keys = require('object-keys');
var assert = require('assert');
/* when Object.keys is not present */
delete Object.keys;
var shimmedKeys = keys.shim();
assert.equal(shimmedKeys, keys);
assert.deepEqual(Object.keys(obj), keys(obj));
```

```js
var keys = require('object-keys');
var assert = require('assert');
/* when Object.keys is present */
var shimmedKeys = keys.shim();
assert.equal(shimmedKeys, Object.keys);
assert.deepEqual(Object.keys(obj), keys(obj));
```

## Source
Implementation taken directly from [es5-shim][11], with modifications, including from [lodash][12].

## Tests
Simply clone the repo, `npm install`, and run `npm test`

[1]: https://npmjs.org/package/object-keys
[2]: http://vb.teelaun.ch/ljharb/object-keys.svg
[3]: https://travis-ci.org/ljharb/object-keys.svg
[4]: https://travis-ci.org/ljharb/object-keys
[5]: https://david-dm.org/ljharb/object-keys.svg
[6]: https://david-dm.org/ljharb/object-keys
[7]: https://david-dm.org/ljharb/object-keys/dev-status.svg
[8]: https://david-dm.org/ljharb/object-keys#info=devDependencies
[9]: https://ci.testling.com/ljharb/object-keys.png
[10]: https://ci.testling.com/ljharb/object-keys
[11]: https://github.com/es-shims/es5-shim/blob/master/es5-shim.js#L542-589
[12]: https://github.com/bestiejs/lodash
[13]: https://nodei.co/npm/object-keys.png?downloads=true&stars=true
[license-image]: http://img.shields.io/npm/l/object-keys.svg
[license-url]: LICENSE
[downloads-image]: http://img.shields.io/npm/dm/object-keys.svg
[downloads-url]: http://npm-stat.com/charts.html?package=object-keys

# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT
# socket.io-client

[![Build Status](https://secure.travis-ci.org/Automattic/socket.io-client.svg)](http://travis-ci.org/Automattic/socket.io-client)
![NPM version](https://badge.fury.io/js/socket.io-client.svg)
![Downloads](http://img.shields.io/npm/dm/socket.io-client.svg?style=flat)

## How to use

A standalone build of `socket.io-client` is exposed automatically by the
socket.io server as `/socket.io/socket.io.js`. Alternatively you can
serve the file `socket.io.js` found at the root of this repository.

```html
<script src="/socket.io/socket.io.js"></script>
<script>
  var socket = io('http://localhost');
  socket.on('connect', function(){});
  socket.on('event', function(data){});
  socket.on('disconnect', function(){});
</script>
```

Socket.IO is compatible with [browserify](http://browserify.org/).

### Node.JS (server-side usage)

  Add `socket.io-client` to your `package.json` and then:

  ```js
  var socket = require('socket.io-client')('http://localhost');
  socket.on('connect', function(){});
  socket.on('event', function(data){});
  socket.on('disconnect', function(){});
  ```

## API

### IO(url:String, opts:Object):Socket

  Exposed as the `io` namespace in the standalone build, or the result
  of calling `require('socket.io-client')`.

  When called, it creates a new `Manager` for the given URL, and attempts
  to reuse an existing `Manager` for subsequent calls, unless the
  `multiplex` option is passed with `false`.

  The rest of the options are passed to the `Manager` constructor (see below
  for details).

  A `Socket` instance is returned for the namespace specified by the
  pathname in the URL, defaulting to `/`. For example, if the `url` is
  `http://localhost/users`, a transport connection will be established to
  `http://localhost` and a Socket.IO connection will be established to
  `/users`.

### IO#protocol

  Socket.io protocol revision number this client works with.

### IO#Socket

  Reference to the `Socket` constructor.

### IO#Manager

  Reference to the `Manager` constructor.

### IO#Emitter

  Reference to the `Emitter` constructor.

### Manager(url:String, opts:Object)

  A `Manager` represents a connection to a given Socket.IO server. One or
  more `Socket` instances are associated with the manager. The manager
  can be accessed through the `io` property of each `Socket` instance.

  The `opts` are also passed to `engine.io` upon initialization of the
  underlying `Socket`.

  Options:
  - `reconnection` whether to reconnect automatically (`true`)
  - `reconnectionAttempts` (`Infinity`) before giving up
  - `reconnectionDelay` how long to initially wait before attempting a new
    reconnection (`1000`). Affected by +/- `randomizationFactor`,
    for example the default initial delay will be between 500 to 1500ms.
  - `reconnectionDelayMax` maximum amount of time to wait between
    reconnections (`5000`). Each attempt increases the reconnection delay by 2x
    along with a randomization as above
  - `randomizationFactor(`0.5`), 0 <= randomizationFactor <= 1
  - `timeout` connection timeout before a `connect_error`
    and `connect_timeout` events are emitted (`20000`)
  - `autoConnect` by setting this false, you have to call `manager.open`
    whenever you decide it's appropriate

#### Events

  - `connect`. Fired upon a successful connection.
  - `connect_error`. Fired upon a connection error.
    Parameters:
      - `Object` error object
  - `connect_timeout`. Fired upon a connection timeout.
  - `reconnect`. Fired upon a successful reconnection.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_attempt`. Fired upon an attempt to reconnect.
  - `reconnecting`. Fired upon an attempt to reconnect.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_error`. Fired upon a reconnection attempt error.
    Parameters:
      - `Object` error object
  - `reconnect_failed`. Fired when couldn't reconnect within `reconnectionAttempts`

The events above are also emitted on the individual sockets that
reconnect that depend on this `Manager`.

### Manager#reconnection(v:Boolean):Manager

  Sets the `reconnection` option, or returns it if no parameters
  are passed.

### Manager#reconnectionAttempts(v:Boolean):Manager

  Sets the `reconnectionAttempts` option, or returns it if no parameters
  are passed.

### Manager#reconnectionDelay(v:Boolean):Manager

  Sets the `reconectionDelay` option, or returns it if no parameters
  are passed.

### Manager#reconnectionDelayMax(v:Boolean):Manager

  Sets the `reconectionDelayMax` option, or returns it if no parameters
  are passed.

### Manager#timeout(v:Boolean):Manager

  Sets the `timeout` option, or returns it if no parameters
  are passed.

### Socket

#### Socket#id:String

A property on the `socket` instance that is equal to the underlying engine.io socket id.

The property is present once the socket has connected, is removed when the socket disconnects and is updated if the socket reconnects.

#### Events

  - `connect`. Fired upon a connection including a successful reconnection.
  - `error`. Fired upon a connection error
    Parameters:
      - `Object` error data
  - `disconnect`. Fired upon a disconnection.
  - `reconnect`. Fired upon a successful reconnection.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_attempt`. Fired upon an attempt to reconnect.
  - `reconnecting`. Fired upon an attempt to reconnect.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_error`. Fired upon a reconnection attempt error.
    Parameters:
      - `Object` error object
  - `reconnect_failed`. Fired when couldn't reconnect within `reconnectionAttempts`

## License

[MIT](/LICENSE)
# to-array

Turn an array like into an array

## Example

``` js
var toArray = require("to-array")
    , elems = document.links

var array = toArray(elems)
```

## Installation

`npm install to-array`

## Contributors

 - Raynos

## MIT Licenced
has-binarydata.js
=================

Simple module to test if an object contains binary data

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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

# Engine.IO client

[![Build Status](https://secure.travis-ci.org/Automattic/engine.io-client.png)](http://travis-ci.org/Automattic/engine.io-client)
[![NPM version](https://badge.fury.io/js/engine.io-client.png)](http://badge.fury.io/js/engine.io-client)

This is the client for [Engine.IO](http://github.com/automattic/engine.io),
the implementation of transport-based cross-browser/cross-device
bi-directional communication layer for [Socket.IO](http://github.com/automattic/socket.io).

## How to use

### Standalone

You can find an `engine.io.js` file in this repository, which is a
standalone build you can use as follows:

```html
<script src="/path/to/engine.io.js"></script>
<script>
  // eio = Socket
  var socket = eio('ws://localhost');
  socket.on('open', function(){
    socket.on('message', function(data){});
    socket.on('close', function(){});
  });
</script>
```

### With browserify

Engine.IO is a commonjs module, which means you can include it by using
`require` on the browser and package using [browserify](http://browserify.org/):

1. install the client package

    ```bash
    $ npm install engine.io-client
    ```

1. write your app code

    ```js
    var socket = require('engine.io-client')('ws://localhost');
    socket.on('open', function(){
      socket.on('message', function(data){});
      socket.on('close', function(){});
    });
    ```

1. build your app bundle

    ```bash
    $ browserify app.js > bundle.js
    ```

1. include on your page

    ```html
    <script src="/path/to/bundle.js"></script>
    ```

### Sending and receiving binary

```html
<script src="/path/to/engine.io.js"></script>
<script>
  var socket = new eio.Socket('ws://localhost/');
  socket.binaryType = 'blob';
  socket.on('open', function () {
    socket.send(new Int8Array(5));
    socket.on('message', function(blob){});
    socket.on('close', function(){ });
  });
</script>
```

### Node.JS

Add `engine.io-client` to your `package.json` and then:

```js
var socket = require('engine.io-client')('ws://localhost');
socket.on('open', function(){
  socket.on('message', function(data){});
  socket.on('close', function(){});
});
```

### Node.js with certificates
```js
var opts = {
  key: fs.readFileSync('test/fixtures/client.key'),
  cert: fs.readFileSync('test/fixtures/client.crt'),
  ca: fs.readFileSync('test/fixtures/ca.crt')
};

var socket = require('engine.io-client')('ws://localhost', opts);
socket.on('open', function(){
  socket.on('message', function(data){});
  socket.on('close', function(){});
});
```

## Features

- Lightweight
- Runs on browser and node.js seamlessly
- Transports are independent of `Engine`
  - Easy to debug
  - Easy to unit test
- Runs inside HTML5 WebWorker
- Can send and receive binary data
  - Receives as ArrayBuffer or Blob when in browser, and Buffer or ArrayBuffer
    in Node
  - When XHR2 or WebSockets are used, binary is emitted directly. Otherwise
    binary is encoded into base64 strings, and decoded when binary types are
    supported.
  - With browsers that don't support ArrayBuffer, an object { base64: true,
    data: dataAsBase64String } is emitted on the `message` event.

## API

### Socket

The client class. Mixes in [Emitter](http://github.com/component/emitter).
Exposed as `eio` in the browser standalone build.

#### Properties

- `protocol` _(Number)_: protocol revision number
- `binaryType` _(String)_ : can be set to 'arraybuffer' or 'blob' in browsers,
  and `buffer` or `arraybuffer` in Node. Blob is only used in browser if it's
  supported.

#### Events

- `open`
  - Fired upon successful connection.
- `message`
  - Fired when data is received from the server.
  - **Arguments**
    - `String` | `ArrayBuffer`: utf-8 encoded data or ArrayBuffer containing
      binary data
- `close`
  - Fired upon disconnection. In compliance with the WebSocket API spec, this event may be 
    fired even if the `open` event does not occur (i.e. due to connection error or `close()`).
- `error`
  - Fired when an error occurs.
- `flush`
  - Fired upon completing a buffer flush
- `drain`
  - Fired after `drain` event of transport if writeBuffer is empty
- `upgradeError`
  - Fired if an error occurs with a transport we're trying to upgrade to.
- `upgrade`
  - Fired upon upgrade success, after the new transport is set

#### Methods

- **constructor**
    - Initializes the client
    - **Parameters**
      - `String` uri
      - `Object`: optional, options object
    - **Options**
      - `agent` (`http.Agent`): `http.Agent` to use, defaults to `false` (NodeJS only)
      - `upgrade` (`Boolean`): defaults to true, whether the client should try
      to upgrade the transport from long-polling to something better.
      - `forceJSONP` (`Boolean`): forces JSONP for polling transport.
      - `jsonp` (`Boolean`): determines whether to use JSONP when
        necessary for polling. If disabled (by settings to false) an error will
        be emitted (saying "No transports available") if no other transports
        are available. If another transport is available for opening a
        connection (e.g. WebSocket) that transport
        will be used instead.
      - `forceBase64` (`Boolean`): forces base 64 encoding for polling transport even when XHR2 responseType is available and WebSocket even if the used standard supports binary.
      - `enablesXDR` (`Boolean`): enables XDomainRequest for IE8 to avoid loading bar flashing with click sound. default to `false` because XDomainRequest has a flaw of not sending cookie.
      - `timestampRequests` (`Boolean`): whether to add the timestamp with
        each transport request. Note: this is ignored if the browser is
        IE or Android, in which case requests are always stamped (`false`)
      - `timestampParam` (`String`): timestamp parameter (`t`)
      - `policyPort` (`Number`): port the policy server listens on (`843`)
      - `path` (`String`): path to connect to, default is `/engine.io`
      - `transports` (`Array`): a list of transports to try (in order).
      Defaults to `['polling', 'websocket']`. `Engine`
      always attempts to connect directly with the first one, provided the
      feature detection test for it passes.
      - `rememberUpgrade` (`Boolean`): defaults to false.
        If true and if the previous websocket connection to the server succeeded,
        the connection attempt will bypass the normal upgrade process and will initially
        try websocket. A connection attempt following a transport error will use the 
        normal upgrade process. It is recommended you turn this on only when using
        SSL/TLS connections, or if you know that your network does not block websockets.
      - `pfx` (`String`): Certificate, Private key and CA certificates to use for SSL. Can be used in Node.js client environment to manually specify certificate information.
      - `key` (`String`): Private key to use for SSL. Can be used in Node.js client environment to manually specify certificate information.
      - `passphrase` (`String`): A string of passphrase for the private key or pfx. Can be used in Node.js client environment to manually specify certificate information.
      - `cert` (`String`): Public x509 certificate to use. Can be used in Node.js client environment to manually specify certificate information.
      - `ca` (`String`|`Array`): An authority certificate or array of authority certificates to check the remote host against.. Can be used in Node.js client environment to manually specify certificate information.
      - `ciphers` (`String`): A string describing the ciphers to use or exclude. Consult the [cipher format list](http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT) for details on the format.. Can be used in Node.js client environment to manually specify certificate information.
      - `rejectUnauthorized` (`Boolean`): If true, the server certificate is verified against the list of supplied CAs. An 'error' event is emitted if verification fails. Verification happens at the connection level, before the HTTP request is sent. Can be used in Node.js client environment to manually specify certificate information.
- `send`
    - Sends a message to the server
    - **Parameters**
      - `String` | `ArrayBuffer` | `ArrayBufferView` | `Blob`: data to send
      - `Function`: optional, callback upon `drain`
- `close`
    - Disconnects the client.

### Transport

The transport class. Private. _Inherits from EventEmitter_.

#### Events

- `poll`: emitted by polling transports upon starting a new request
- `pollComplete`: emitted by polling transports upon completing a request
- `drain`: emitted by polling transports upon a buffer drain

## Tests

`engine.io-client` is used to test
[engine](http://github.com/automattic/engine.io). Running the `engine.io`
test suite ensures the client works and vice-versa.

Browser tests are run using [zuul](https://github.com/defunctzombie/zuul). You can
run the tests locally using the following command.

```
./node_modules/.bin/zuul --local 8080 -- test/index.js
```

Additionally, `engine.io-client` has a standalone test suite you can run
with `make test` which will run node.js and browser tests. You must have zuul setup with
a saucelabs account.

## Support

The support channels for `engine.io-client` are the same as `socket.io`:
  - irc.freenode.net **#socket.io**
  - [Google Groups](http://groups.google.com/group/socket_io)
  - [Website](http://socket.io)

## Development

To contribute patches, run tests or benchmarks, make sure to clone the
repository:

```bash
git clone git://github.com/automattic/engine.io-client.git
```

Then:

```bash
cd engine.io-client
npm install
```

See the `Tests` section above for how to run tests before submitting any patches.

## License

MIT - Copyright (c) 2014 Automattic, Inc.

# node-XMLHttpRequest #

node-XMLHttpRequest is a wrapper for the built-in http client to emulate the
browser XMLHttpRequest object.

This can be used with JS designed for browsers to improve reuse of code and
allow the use of existing libraries.

Note: This library currently conforms to [XMLHttpRequest 1](http://www.w3.org/TR/XMLHttpRequest/). Version 2.0 will target [XMLHttpRequest Level 2](http://www.w3.org/TR/XMLHttpRequest2/).

## Usage ##

Here's how to include the module in your project and use as the browser-based
XHR object.

	var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
	var xhr = new XMLHttpRequest();

Note: use the lowercase string "xmlhttprequest" in your require(). On
case-sensitive systems (eg Linux) using uppercase letters won't work.

## Versions ##

Prior to 1.4.0 version numbers were arbitrary. From 1.4.0 on they conform to
the standard major.minor.bugfix. 1.x shouldn't necessarily be considered
stable just because it's above 0.x.

Since the XMLHttpRequest API is stable this library's API is stable as
well. Major version numbers indicate significant core code changes.
Minor versions indicate minor core code changes or better conformity to
the W3C spec.

## License ##

MIT license. See LICENSE for full details.

## Supports ##

* Async and synchronous requests
* GET, POST, PUT, and DELETE requests
* All spec methods (open, send, abort, getRequestHeader,
  getAllRequestHeaders, event methods)
* Requests to all domains

## Known Issues / Missing Features ##

For a list of open issues or to report your own visit the [github issues
page](https://github.com/driverdan/node-XMLHttpRequest/issues).

* Local file access may have unexpected results for non-UTF8 files
* Synchronous requests don't set headers properly
* Synchronous requests freeze node while waiting for response (But that's what you want, right? Stick with async!).
* Some events are missing, such as abort
* getRequestHeader is case-sensitive
* Cookies aren't persisted between requests
* Missing XML support
* Missing basic auth
# ws: a node.js websocket library

[![Build Status](https://travis-ci.org/websockets/ws.svg?branch=master)](https://travis-ci.org/websockets/ws)

`ws` is a simple to use WebSocket implementation, up-to-date against RFC-6455,
and [probably the fastest WebSocket library for node.js][archive].

Passes the quite extensive Autobahn test suite. See http://websockets.github.com/ws
for the full reports.

## Protocol support

* **Hixie draft 76** (Old and deprecated, but still in use by Safari and Opera.
  Added to ws version 0.4.2, but server only. Can be disabled by setting the
  `disableHixie` option to true.)
* **HyBi drafts 07-12** (Use the option `protocolVersion: 8`)
* **HyBi drafts 13-17** (Current default, alternatively option `protocolVersion: 13`)

### Installing

```
npm install --save ws
```

### Sending and receiving text data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  ws.send('something');
});

ws.on('message', function(data, flags) {
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
});
```

### Sending binary data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  var array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }

  ws.send(array, { binary: true, mask: true });
});
```

Setting `mask`, as done for the send options above, will cause the data to be
masked according to the WebSocket protocol. The same option applies for text
data.

### Server example

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});
```

### ExpressJS example

```js
var server = require('http').createServer()
  , url = require('url')
  , WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ server: server })
  , express = require('express')
  , app = express()
  , port = 4080;

app.use(function (req, res) {
  res.send({ msg: "hello" });
});

wss.on('connection', function connection(ws) {
  var location = url.parse(ws.upgradeReq.url, true);
  // you might use location.query.access_token to authenticate or share sessions
  // or ws.upgradeReq.headers.cookie (see http://stackoverflow.com/a/16395220/151312)
  
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});

server.on('request', app);
server.listen(port, function () { console.log('Listening on ' + server.address().port) });
```

### Server sending broadcast data

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    client.send(data);
  });
};
```

### Error handling best practices

```js
// If the WebSocket is closed before the following send is attempted
ws.send('something');

// Errors (both immediate and async write errors) can be detected in an optional
// callback. The callback is also the only way of being notified that data has
// actually been sent.
ws.send('something', function ack(error) {
  // if error is not defined, the send has been completed,
  // otherwise the error object will indicate what failed.
});

// Immediate errors can also be handled with try/catch-blocks, but **note** that
// since sends are inherently asynchronous, socket write failures will *not* be
// captured when this technique is used.
try { ws.send('something'); }
catch (e) { /* handle error */ }
```

### echo.websocket.org demo

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://echo.websocket.org/', {
  protocolVersion: 8, 
  origin: 'http://websocket.org'
});

ws.on('open', function open() {
  console.log('connected');
  ws.send(Date.now().toString(), {mask: true});
});

ws.on('close', function close() {
  console.log('disconnected');
});

ws.on('message', function message(data, flags) {
  console.log('Roundtrip time: ' + (Date.now() - parseInt(data)) + 'ms', flags);

  setTimeout(function timeout() {
    ws.send(Date.now().toString(), {mask: true});
  }, 500);
});
```

### Browserify users
When including ws via a browserify bundle, ws returns global.WebSocket which has slightly different API. 
You should use the standard WebSockets API instead.

https://developer.mozilla.org/en-US/docs/WebSockets/Writing_WebSocket_client_applications#Availability_of_WebSockets


### Other examples

For a full example with a browser client communicating with a ws server, see the
examples folder.

Note that the usage together with Express 3.0 is quite different from Express
2.x. The difference is expressed in the two different serverstats-examples.

Otherwise, see the test cases.

### Running the tests

```
make test
```

## API Docs

See [`/doc/ws.md`](https://github.com/websockets/ws/blob/master/doc/ws.md) for Node.js-like docs for the ws classes.

## Changelog

We're using the GitHub [`releases`](https://github.com/websockets/ws/releases) for changelog entries.

## License

(The MIT License)

Copyright (c) 2011 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[archive]: http://web.archive.org/web/20130314230536/http://hobbycoding.posterous.com/the-fastest-websocket-module-for-nodejs
# Ultron

[![Made by unshift](https://img.shields.io/badge/made%20by-unshift-00ffcc.svg?style=flat-square)](http://unshift.io)[![Version npm](http://img.shields.io/npm/v/ultron.svg?style=flat-square)](http://browsenpm.org/package/ultron)[![Build Status](http://img.shields.io/travis/unshiftio/ultron/master.svg?style=flat-square)](https://travis-ci.org/unshiftio/ultron)[![Dependencies](https://img.shields.io/david/unshiftio/ultron.svg?style=flat-square)](https://david-dm.org/unshiftio/ultron)[![Coverage Status](http://img.shields.io/coveralls/unshiftio/ultron/master.svg?style=flat-square)](https://coveralls.io/r/unshiftio/ultron?branch=master)[![IRC channel](http://img.shields.io/badge/IRC-irc.freenode.net%23unshift-00a8ff.svg?style=flat-square)](http://webchat.freenode.net/?channels=unshift)

Ultron is a high-intelligence robot. It gathers intelligence so it can start
improving upon his rudimentary design. It will learn your event emitting
patterns and find ways to exterminate them. Allowing you to remove only the
event emitters that **you** assigned and not the ones that your users or
developers assigned. This can prevent race conditions, memory leaks and even file
descriptor leaks from ever happening as you won't remove clean up processes.

## Installation

The module is designed to be used in browsers using browserify and in Node.js.
You can install the module through the public npm registry by running the
following command in CLI:

```
npm install --save ultron
```

## Usage

In all examples we assume that you've required the library as following:

```js
'use strict';

var Ultron = require('ultron');
```

Now that we've required the library we can construct our first `Ultron` instance.
The constructor requires one argument which should be the `EventEmitter`
instance that we need to operate upon. This can be the `EventEmitter` module
that ships with Node.js or `EventEmitter3` or anything else as long as it
follow the same API and internal structure as these 2. So with that in mind we
can create the instance:

```js
//
// For the sake of this example we're going to construct an empty EventEmitter
//
var EventEmitter = require('events').EventEmitter; // or require('eventmitter3');
var events = new EventEmitter();

var ultron = new Ultron(events);
```

You can now use the following API's from the Ultron instance:

### Ultron.on

Register a new event listener for the given event. It follows the exact same API
as `EventEmitter.on` but it will return itself instead of returning the
EventEmitter instance. If you are using EventEmitter3 it also supports the
context param:

```js
ultron.on('event-name', handler, { custom: 'function context' });
```

### Ultron.once

Exactly the same as the [Ultron.on](#ultronon) but it only allows the execution
once.

### Ultron.remove

This is where all the magic happens and the safe removal starts. This function
accepts different argument styles:

- No arguments, assume that all events need to be removed so it will work as
  `removeAllListeners()` API.
- 1 argument, when it's a string it will be split on ` ` and `,` to create a
  list of events that need to be cleared.
- Multiple arguments, we assume that they are all names of events that need to
  be cleared.

```js
ultron.remove('foo, bar baz');        // Removes foo, bar and baz.
ultron.remove('foo', 'bar', 'baz');   // Removes foo, bar and baz.
ultron.remove();                      // Removes everything.
```

If you just want to remove a single event listener using a function reference
you can still use the EventEmitter's `removeListener(event, fn)` API:

```js
function foo() {}

ulton.on('foo', foo);
events.removeListener('foo', foo);
```

## License

MIT
# options.js #

A very light-weight in-code option parsers for node.js.

## Usage ##

``` js
var Options = require("options");

// Create an Options object
function foo(options) {
        var default_options = {
                foo : "bar"
        };
        
        // Create an option object with default value
        var opts = new Options(default_options);
        
        // Merge options
        opts = opts.merge(options);
        
        // Reset to default value
        opts.reset();
        
        // Copy selected attributes out
        var seled_att = opts.copy("foo");
        
        // Read json options from a file. 
        opts.read("options.file"); // Sync
        opts.read("options.file", function(err){ // Async
                if(err){ // If error occurs
                        console.log("File error.");
                }else{
                        // No error
                }
        });
        
        // Attributes defined or not
        opts.isDefinedAndNonNull("foobar");
        opts.isDefined("foobar");
}

```


## License ##

(The MIT License)

Copyright (c) 2012 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# After [![Build Status][1]][2]

Invoke callback after n calls

## Status: production ready

## Example

    var after = require("after")
        , next = after(3, logItWorks)

    next()
    next()
    next() // it works

    function logItWorks() {
        console.log("it works!")
    }

## Example with error handling

    var after = require("after")
        , next = after(3, logError)

    next()
    next(new Error("oops")) // logs oops
    next() // does nothing

    function logError(err) {
        console.log(err)
    }

## After < 0.6.0

Older versions of after had iterators and flows in them.

These have been replaced with seperate modules

 - [iterators][8]
 - [composite][9]

## Installation

`npm install after`

## Tests

`npm test`

## Blog post

 - [Flow control in node.js][3]

## Examples :

 - [Determining the end of asynchronous operations][4]
 - [In javascript what are best practices for executing multiple asynchronous functions][5]
 - [JavaScript performance long running tasks][6]
 - [Synchronous database queries with node.js][7]

## Contributors

 - Raynos

## MIT Licenced

  [1]: https://secure.travis-ci.org/Raynos/after.png
  [2]: http://travis-ci.org/Raynos/after
  [3]: http://raynos.org/blog/2/Flow-control-in-node.js
  [4]: http://stackoverflow.com/questions/6852059/determining-the-end-of-asynchronous-operations-javascript/6852307#6852307
  [5]: http://stackoverflow.com/questions/6869872/in-javascript-what-are-best-practices-for-executing-multiple-asynchronous-functi/6870031#6870031
  [6]: http://stackoverflow.com/questions/6864397/javascript-performance-long-running-tasks/6889419#6889419
  [7]: http://stackoverflow.com/questions/6597493/synchronous-database-queries-with-node-js/6620091#6620091
  [8]: http://github.com/Raynos/iterators
  [9]: http://github.com/Raynos/composite
# How to
```javascript
var sliceBuffer = require('arraybuffer.slice');
var ab = (new Int8Array(5)).buffer;
var sliced = sliceBuffer(ab, 1, 3);
sliced = sliceBuffer(ab, 1);
```

# Licence (MIT)
Copyright (C) 2013 Rase-


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Blob
====

A module that exports a constructor that uses window.Blob when available, and a BlobBuilder with any vendor prefix in other cases. If neither is available, it exports undefined.

Usage:

```javascript
var Blob = require('blob');
var b = new Blob(['hi', 'constructing', 'a', 'blob']);
```

## Licence
MIT
# base64-arraybuffer

[![Build Status](https://travis-ci.org/niklasvh/base64-arraybuffer.png)](https://travis-ci.org/niklasvh/base64-arraybuffer)

Encode/decode base64 data into ArrayBuffers

## Getting Started
Install the module with: `npm install base64-arraybuffer`

## API
The library encodes and decodes base64 to and from ArrayBuffers

 - __encode(buffer)__ - Encodes `ArrayBuffer` into base64 string
 - __decode(str)__ - Decodes base64 string to `ArrayBuffer`

## Release History

 - 0.1.2 - Fix old format of typed arrays
 - 0.1.0 - Initial version, basic decode/encode base64 to and from ArrayBuffer

## License
Copyright (c) 2012 Niklas von Hertzen
Licensed under the MIT license.
# utf8.js [![Build status](https://travis-ci.org/mathiasbynens/utf8.js.svg?branch=master)](https://travis-ci.org/mathiasbynens/utf8.js) [![Code coverage status](http://img.shields.io/coveralls/mathiasbynens/utf8.js/master.svg)](https://coveralls.io/r/mathiasbynens/utf8.js) [![Dependency status](https://gemnasium.com/mathiasbynens/utf8.js.svg)](https://gemnasium.com/mathiasbynens/utf8.js)

_utf8.js_ is a well-tested UTF-8 encoder/decoder written in JavaScript. Unlike many other JavaScript solutions, it is designed to be a _proper_ UTF-8 encoder/decoder: it can encode/decode any scalar Unicode code point values, as per [the Encoding Standard](https://encoding.spec.whatwg.org/#utf-8). [Here’s an online demo.](https://mothereff.in/utf-8)

Feel free to fork if you see possible improvements!

## Installation

Via [npm](https://www.npmjs.org/):

```bash
npm install utf8
```

Via [Bower](http://bower.io/):

```bash
bower install utf8
```

Via [Component](https://github.com/component/component):

```bash
component install mathiasbynens/utf8.js
```

In a browser:

```html
<script src="utf8.js"></script>
```

In [Narwhal](http://narwhaljs.org/), [Node.js](https://nodejs.org/), and [RingoJS ≥ v0.8.0](http://ringojs.org/):

```js
var utf8 = require('utf8');
```

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('utf8.js');
```

Using an AMD loader like [RequireJS](http://requirejs.org/):

```js
require(
  {
    'paths': {
      'utf8': 'path/to/utf8'
    }
  },
  ['utf8'],
  function(utf8) {
    console.log(utf8);
  }
);
```

## API

### `utf8.encode(string)`

Encodes any given JavaScript string (`string`) as UTF-8, and returns the UTF-8-encoded version of the string. It throws an error if the input string contains a non-scalar value, i.e. a lone surrogate. (If you need to be able to encode non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
// U+00A9 COPYRIGHT SIGN; see http://codepoints.net/U+00A9
utf8.encode('\xA9');
// → '\xC2\xA9'
// U+10001 LINEAR B SYLLABLE B038 E; see http://codepoints.net/U+10001
utf8.encode('\uD800\uDC01');
// → '\xF0\x90\x80\x81'
```

### `utf8.decode(byteString)`

Decodes any given UTF-8-encoded string (`byteString`) as UTF-8, and returns the UTF-8-decoded version of the string. It throws an error when malformed UTF-8 is detected. (If you need to be able to decode encoded non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
utf8.decode('\xC2\xA9');
// → '\xA9'

utf8.decode('\xF0\x90\x80\x81');
// → '\uD800\uDC01'
// → U+10001 LINEAR B SYLLABLE B038 E
```

### `utf8.version`

A string representing the semantic version number.

## Support

utf8.js has been tested in at least Chrome 27-39, Firefox 3-34, Safari 4-8, Opera 10-28, IE 6-11, Node.js v0.10.0, Narwhal 0.3.2, RingoJS 0.8-0.11, PhantomJS 1.9.0, and Rhino 1.7RC4.

## Unit tests & code coverage

After cloning this repository, run `npm install` to install the dependencies needed for development and testing. You may want to install Istanbul _globally_ using `npm install istanbul -g`.

Once that’s done, you can run the unit tests in Node using `npm test` or `node tests/tests.js`. To run the tests in Rhino, Ringo, Narwhal, PhantomJS, and web browsers as well, use `grunt test`.

To generate the code coverage report, use `grunt cover`.

## FAQ

### Why is the first release named v2.0.0? Haven’t you heard of [semantic versioning](http://semver.org/)?

Long before utf8.js was created, the `utf8` module on npm was registered and used by another (slightly buggy) library. @ryanmcgrath was kind enough to give me access to the `utf8` package on npm when I told him about utf8.js. Since there has already been a v1.0.0 release of the old library, and to avoid breaking backwards compatibility with projects that rely on the `utf8` npm package, I decided the tag the first release of utf8.js as v2.0.0 and take it from there.

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

utf8.js is available under the [MIT](https://mths.be/mit) license.
# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIThas-binarydata.js
=================

Simple module to test if an object contains binary data

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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

# Engine.IO: the realtime engine

[![Build Status](https://secure.travis-ci.org/Automattic/engine.io.png)](http://travis-ci.org/Automattic/engine.io)
[![NPM version](https://badge.fury.io/js/engine.io.png)](http://badge.fury.io/js/engine.io)

`Engine.IO` is the implementation of transport-based
cross-browser/cross-device bi-directional communication layer for
[Socket.IO](http://github.com/learnboost/socket.io).

## How to use

### Server

#### (A) Listening on a port

```js
var engine = require('engine.io');
var server = engine.listen(80);

server.on('connection', function(socket){
  socket.send('utf 8 string');
  socket.send(new Buffer([0, 1, 2, 3, 4, 5])); // binary data
});
```

#### (B) Intercepting requests for a http.Server

```js
var engine = require('engine.io');
var http = require('http').createServer().listen(3000);
var server = engine.attach(http);

server.on('connection', function (socket) {
  socket.on('message', function(data){ });
  socket.on('close', function(){ });
});
```

#### (C) Passing in requests

```js
var engine = require('engine.io');
var server = new engine.Server();

server.on('connection', function(socket){
  socket.send('hi');
});

// …
httpServer.on('upgrade', function(req, socket, head){
  server.handleUpgrade(req, socket, head);
});
httpServer.on('request', function(req, res){
  server.handleRequest(req, res);
});
```

### Client

```html
<script src="/path/to/engine.io.js"></script>
<script>
  var socket = new eio.Socket('ws://localhost/');
  socket.on('open', function(){
    socket.on('message', function(data){});
    socket.on('close', function(){});
  });
</script>
```

For more information on the client refer to the
[engine-client](http://github.com/learnboost/engine.io-client) repository.

## What features does it have?

- **Maximum reliability**. Connections are established even in the presence of:
  - proxies and load balancers.
  - personal firewall and antivirus software.
  - for more information refer to **Goals** and **Architecture** sections
- **Minimal client size** aided by:
  - lazy loading of flash transports.
  - lack of redundant transports.
- **Scalable**
  - load balancer friendly
- **Future proof**
- **100% Node.JS core style**
  - No API sugar (left for higher level projects)
  - Written in readable vanilla JavaScript

## API

### Server

<hr><br>

#### Top-level

These are exposed by `require('engine.io')`:

##### Events

- `flush`
    - Called when a socket buffer is being flushed.
    - **Arguments**
      - `Socket`: socket being flushed
      - `Array`: write buffer
- `drain`
    - Called when a socket buffer is drained
    - **Arguments**
      - `Socket`: socket being flushed

##### Properties

- `protocol` _(Number)_: protocol revision number
- `Server`: Server class constructor
- `Socket`: Socket class constructor
- `Transport` _(Function)_: transport constructor
- `transports` _(Object)_: map of available transports

##### Methods

- `()`
    - Returns a new `Server` instance. If the first argument is an `http.Server` then the
      new `Server` instance will be attached to it. Otherwise, the arguments are passed
      directly to the `Server` constructor.
    - **Parameters**
      - `http.Server`: optional, server to attach to.
      - `Object`: optional, options object (see `Server#constructor` api docs below)

  The following are identical ways to instantiate a server and then attach it.
  ```js
  var httpServer; // previously created with `http.createServer();` from node.js api.

  // create a server first, and then attach
  var eioServer = require('engine.io').Server();
  eioServer.attach(httpServer);

  // or call the module as a function to get `Server`
  var eioServer = require('engine.io')();
  eioServer.attach(httpServer);

  // immediately attach
  var eioServer = require('engine.io')(httpServer);
  ```

- `listen`
    - Creates an `http.Server` which listens on the given port and attaches WS
      to it. It returns `501 Not Implemented` for regular http requests.
    - **Parameters**
      - `Number`: port to listen on.
      - `Object`: optional, options object
      - `Function`: callback for `listen`.
    - **Options**
      - All options from `Server.attach` method, documented below.
      - **Additionally** See Server `constructor` below for options you can pass for creating the new Server
    - **Returns** `Server`
- `attach`
    - Captures `upgrade` requests for a `http.Server`. In other words, makes
      a regular http.Server WebSocket-compatible.
    - **Parameters**
      - `http.Server`: server to attach to.
      - `Object`: optional, options object
    - **Options**
      - All options from `Server.attach` method, documented below.
      - **Additionally** See Server `constructor` below for options you can pass for creating the new Server
    - **Returns** `Server` a new Server instance.

<hr><br>

#### Server

The main server/manager. _Inherits from EventEmitter_.

##### Events

- `connection`
    - Fired when a new connection is established.
    - **Arguments**
      - `Socket`: a Socket object

##### Properties

**Important**: if you plan to use Engine.IO in a scalable way, please
keep in mind the properties below will only reflect the clients connected
to a single process.

- `clients` _(Object)_: hash of connected clients by id.
- `clientsCount` _(Number)_: number of connected clients.

##### Methods

- **constructor**
    - Initializes the server
    - **Parameters**
      - `Object`: optional, options object
    - **Options**
      - `pingTimeout` (`Number`): how many ms without a pong packet to
        consider the connection closed (`60000`)
      - `pingInterval` (`Number`): how many ms before sending a new ping
        packet (`25000`)
      - `maxHttpBufferSize` (`Number`): how many bytes or characters a message
        can be when polling, before closing the session (to avoid DoS). Default
        value is `10E7`.
      - `allowRequest` (`Function`): A function that receives a given handshake
        or upgrade request as its first parameter, and can decide whether to
        continue or not. The second argument is a function that needs to be
        called with the decided information: `fn(err, success)`, where
        `success` is a boolean value where false means that the request is
        rejected, and err is an error code.
      - `transports` (`<Array> String`): transports to allow connections
        to (`['polling', 'websocket']`)
      - `allowUpgrades` (`Boolean`): whether to allow transport upgrades
        (`true`)
      - `cookie` (`String|Boolean`): name of the HTTP cookie that
        contains the client sid to send as part of handshake response
        headers. Set to `false` to not send one. (`io`)
- `close`
    - Closes all clients
    - **Returns** `Server` for chaining
- `handleRequest`
    - Called internally when a `Engine` request is intercepted.
    - **Parameters**
      - `http.ServerRequest`: a node request object
      - `http.ServerResponse`: a node response object
    - **Returns** `Server` for chaining
- `handleUpgrade`
    - Called internally when a `Engine` ws upgrade is intercepted.
    - **Parameters** (same as `upgrade` event)
      - `http.ServerRequest`: a node request object
      - `net.Stream`: TCP socket for the request
      - `Buffer`: legacy tail bytes
    - **Returns** `Server` for chaining
- `attach`
    - Attach this Server instance to an `http.Server`
    - Captures `upgrade` requests for a `http.Server`. In other words, makes
      a regular http.Server WebSocket-compatible.
    - **Parameters**
      - `http.Server`: server to attach to.
      - `Object`: optional, options object
    - **Options**
      - `path` (`String`): name of the path to capture (`/engine.io`).
      - `destroyUpgrade` (`Boolean`): destroy unhandled upgrade requests (`true`)
      - `destroyUpgradeTimeout` (`Number`): milliseconds after which unhandled requests are ended (`1000`)

<hr><br>

#### Socket

A representation of a client. _Inherits from EventEmitter_.

##### Events

- `close`
    - Fired when the client is disconnected.
    - **Arguments**
      - `String`: reason for closing
      - `Object`: description object (optional)
- `message`
    - Fired when the client sends a message.
    - **Arguments**
      - `String` or `Buffer`: Unicode string or Buffer with binary contents
- `error`
    - Fired when an error occurs.
    - **Arguments**
      - `Error`: error object
- `flush`
    - Called when the write buffer is being flushed.
    - **Arguments**
      - `Array`: write buffer
- `drain`
    - Called when the write buffer is drained
- `packet`
    - Called when a socket received a packet (`message`, `ping`)
    - **Arguments**
      - `type`: packet type
      - `data`: packet data (if type is message)
- `packetCreate`
    - Called before a socket sends a packet (`message`, `pong`)
    - **Arguments**
      - `type`: packet type
      - `data`: packet data (if type is message)

##### Properties

- `id` _(String)_: unique identifier
- `server` _(Server)_: engine parent reference
- `request` _(http.ServerRequest)_: request that originated the Socket
- `upgraded` _(Boolean)_: whether the transport has been upgraded
- `readyState` _(String)_: opening|open|closing|closed
- `transport` _(Transport)_: transport reference

##### Methods

- `send`:
    - Sends a message, performing `message = toString(arguments[0])` unless
      sending binary data, which is sent as is.
    - **Parameters**
      - `String` | `Buffer` | `ArrayBuffer` | `ArrayBufferView`: a string or any object implementing `toString()`, with outgoing data, or a Buffer or ArrayBuffer with binary data. Also any ArrayBufferView can be sent as is.
      - `Function`: optional, a callback executed when the message gets flushed out by the transport
    - **Returns** `Socket` for chaining
- `close`
    - Disconnects the client
    - **Returns** `Socket` for chaining

### Client

<hr><br>

Exposed in the `eio` global namespace (in the browser), or by
`require('engine.io-client')` (in Node.JS).

For the client API refer to the 
[engine-client](http://github.com/learnboost/engine.io-client) repository.

## Debug / logging

Engine.IO is powered by [debug](http://github.com/visionmedia/debug).
In order to see all the debug output, run your app with the environment variable
`DEBUG` including the desired scope.

To see the output from all of Engine.IO's debugging scopes you can use:

```
DEBUG=engine* node myapp
```

## Transports

- `polling`: XHR / JSONP polling transport.
- `websocket`: WebSocket transport.

## Plugins

- [engine.io-conflation](https://github.com/EugenDueck/engine.io-conflation): Makes **conflation and aggregation** of messages straightforward.

## Support

The support channels for `engine.io` are the same as `socket.io`:
  - irc.freenode.net **#socket.io**
  - [Google Groups](http://groups.google.com/group/socket_io)
  - [Website](http://socket.io)

## Development

To contribute patches, run tests or benchmarks, make sure to clone the
repository:

```
git clone git://github.com/LearnBoost/engine.io.git
```

Then:

```
cd engine.io
npm install
```

## Tests

Tests run with `make test`. It runs the server tests that are aided by
the usage of `engine.io-client`.

Make sure `npm install` is run first.

## Goals

The main goal of `Engine` is ensuring the most reliable realtime communication.
Unlike the previous Socket.IO core, it always establishes a long-polling
connection first, then tries to upgrade to better transports that are "tested" on
the side.

During the lifetime of the Socket.IO projects, we've found countless drawbacks
to relying on `HTML5 WebSocket` or `Flash Socket` as the first connection
mechanisms.

Both are clearly the _right way_ of establishing a bidirectional communication,
with HTML5 WebSocket being the way of the future. However, to answer most business
needs, alternative traditional HTTP 1.1 mechanisms are just as good as delivering
the same solution.

WebSocket based connections have two fundamental benefits:

1. **Better server performance**
  - _A: Load balancers_<br>
      Load balancing a long polling connection poses a serious architectural nightmare
      since requests can come from any number of open sockets by the user agent, but
      they all need to be routed to the process and computer that owns the `Engine`
      connection. This negatively impacts RAM and CPU usage.
  - _B: Network traffic_<br>
      WebSocket is designed around the premise that each message frame has to be 
      surrounded by the least amount of data. In HTTP 1.1 transports, each message
      frame is surrounded by HTTP headers and chunked encoding frames. If you try to
      send the message _"Hello world"_ with xhr-polling, the message ultimately
      becomes larger than if you were to send it with WebSocket.
  - _C: Lightweight parser_<br>
      As an effect of **B**, the server has to do a lot more work to parse the network
      data and figure out the message when traditional HTTP requests are used
      (as in long polling). This means that another advantage of WebSocket is
      less server CPU usage.

2. **Better user experience**

    Due to the reasons stated in point **1**, the most important effect of being able
    to establish a WebSocket connection is raw data transfer speed, which translates
    in _some_ cases in better user experience.

    Applications with heavy realtime interaction (such as games) will benefit greatly,
    whereas applications like realtime chat (Gmail/Facebook), newsfeeds (Facebook) or
    timelines (Twitter) will have negligible user experience improvements.

Having said this, attempting to establish a WebSocket connection directly so far has
proven problematic:

1. **Proxies**<br>
    Many corporate proxies block WebSocket traffic.

2. **Personal firewall and antivirus software**<br>
    As a result of our research, we've found that at least 3 personal security
    applications block WebSocket traffic.

3. **Cloud application platforms**<br>
    Platforms like Heroku or No.de have had trouble keeping up with the fast-paced
    nature of the evolution of the WebSocket protocol. Applications therefore end up
    inevitably using long polling, but the seamless installation experience of 
    Socket.IO we strive for (_"require() it and it just works"_) disappears.

Some of these problems have solutions. In the case of proxies and personal programs,
however, the solutions many times involve upgrading software. Experience has shown
that relying on client software upgrades to deliver a business solution is
fruitless: the very existence of this project has to do with a fragmented panorama
of user agent distribution, with clients connecting with latest versions of the most
modern user agents (Chrome, Firefox and Safari), but others with versions as low as
IE 5.5.

From the user perspective, an unsuccessful WebSocket connection can translate in
up to at least 10 seconds of waiting for the realtime application to begin
exchanging data. This **perceptively** hurts user experience.

To summarize, **Engine** focuses on reliability and user experience first, marginal
potential UX improvements and increased server performance second. `Engine` is the
result of all the lessons learned with WebSocket in the wild.

## Architecture

The main premise of `Engine`, and the core of its existence, is the ability to
swap transports on the fly. A connection starts as xhr-polling, but it can
switch to WebSocket.

The central problem this poses is: how do we switch transports without losing
messages?

`Engine` only switches from polling to another transport in between polling
cycles. Since the server closes the connection after a certain timeout when
there's no activity, and the polling transport implementation buffers messages
in between connections, this ensures no message loss and optimal performance.

Another benefit of this design is that we workaround almost all the limitations
of **Flash Socket**, such as slow connection times, increased file size (we can
safely lazy load it without hurting user experience), etc.

## FAQ

### Can I use engine without Socket.IO ?

Absolutely. Although the recommended framework for building realtime applications
is Socket.IO, since it provides fundamental features for real-world applications 
such as multiplexing, reconnection support, etc.

`Engine` is to Socket.IO what Connect is to Express. An essential piece for building
realtime frameworks, but something you _probably_ won't be using for building
actual applications.

### Does the server serve the client?

No. The main reason is that `Engine` is meant to be bundled with frameworks.
Socket.IO includes `Engine`, therefore serving two clients is not necessary. If
you use Socket.IO, including

```html
<script src="/socket.io/socket.io.js">
```

has you covered.

### Can I implement `Engine` in other languages?

Absolutely. The [engine.io-protocol](https://github.com/LearnBoost/engine.io-protocol)
repository contains the most up to date description of the specification
at all times, and the parser implementation in JavaScript.

## License 

(The MIT License)

Copyright (c) 2014 Guillermo Rauch &lt;guillermo@learnboost.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

base64id
========

Node.js module that generates a base64 id.

Uses crypto.randomBytes when available, falls back to unsafe methods for node.js <= 0.4.

To increase performance, random bytes are buffered to minimize the number of synchronous calls to crypto.randomBytes.

## Installation

   $ npm install mongoose

## Usage

   var base64id = require('base64id');

   var id = base64id.generateId();
# ws: a node.js websocket library

[![Build Status](https://travis-ci.org/websockets/ws.svg?branch=master)](https://travis-ci.org/websockets/ws)

`ws` is a simple to use WebSocket implementation, up-to-date against RFC-6455,
and [probably the fastest WebSocket library for node.js][archive].

Passes the quite extensive Autobahn test suite. See http://websockets.github.com/ws
for the full reports.

## Protocol support

* **Hixie draft 76** (Old and deprecated, but still in use by Safari and Opera.
  Added to ws version 0.4.2, but server only. Can be disabled by setting the
  `disableHixie` option to true.)
* **HyBi drafts 07-12** (Use the option `protocolVersion: 8`)
* **HyBi drafts 13-17** (Current default, alternatively option `protocolVersion: 13`)

### Installing

```
npm install --save ws
```

### Sending and receiving text data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  ws.send('something');
});

ws.on('message', function(data, flags) {
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
});
```

### Sending binary data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  var array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }

  ws.send(array, { binary: true, mask: true });
});
```

Setting `mask`, as done for the send options above, will cause the data to be
masked according to the WebSocket protocol. The same option applies for text
data.

### Server example

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});
```

### ExpressJS example

```js
var server = require('http').createServer()
  , url = require('url')
  , WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ server: server })
  , express = require('express')
  , app = express()
  , port = 4080;

app.use(function (req, res) {
  res.send({ msg: "hello" });
});

wss.on('connection', function connection(ws) {
  var location = url.parse(ws.upgradeReq.url, true);
  // you might use location.query.access_token to authenticate or share sessions
  // or ws.upgradeReq.headers.cookie (see http://stackoverflow.com/a/16395220/151312)
  
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});

server.on('request', app);
server.listen(port, function () { console.log('Listening on ' + server.address().port) });
```

### Server sending broadcast data

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    client.send(data);
  });
};
```

### Error handling best practices

```js
// If the WebSocket is closed before the following send is attempted
ws.send('something');

// Errors (both immediate and async write errors) can be detected in an optional
// callback. The callback is also the only way of being notified that data has
// actually been sent.
ws.send('something', function ack(error) {
  // if error is not defined, the send has been completed,
  // otherwise the error object will indicate what failed.
});

// Immediate errors can also be handled with try/catch-blocks, but **note** that
// since sends are inherently asynchronous, socket write failures will *not* be
// captured when this technique is used.
try { ws.send('something'); }
catch (e) { /* handle error */ }
```

### echo.websocket.org demo

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://echo.websocket.org/', {
  protocolVersion: 8, 
  origin: 'http://websocket.org'
});

ws.on('open', function open() {
  console.log('connected');
  ws.send(Date.now().toString(), {mask: true});
});

ws.on('close', function close() {
  console.log('disconnected');
});

ws.on('message', function message(data, flags) {
  console.log('Roundtrip time: ' + (Date.now() - parseInt(data)) + 'ms', flags);

  setTimeout(function timeout() {
    ws.send(Date.now().toString(), {mask: true});
  }, 500);
});
```

### Browserify users
When including ws via a browserify bundle, ws returns global.WebSocket which has slightly different API. 
You should use the standard WebSockets API instead.

https://developer.mozilla.org/en-US/docs/WebSockets/Writing_WebSocket_client_applications#Availability_of_WebSockets


### Other examples

For a full example with a browser client communicating with a ws server, see the
examples folder.

Note that the usage together with Express 3.0 is quite different from Express
2.x. The difference is expressed in the two different serverstats-examples.

Otherwise, see the test cases.

### Running the tests

```
make test
```

## API Docs

See [`/doc/ws.md`](https://github.com/websockets/ws/blob/master/doc/ws.md) for Node.js-like docs for the ws classes.

## Changelog

We're using the GitHub [`releases`](https://github.com/websockets/ws/releases) for changelog entries.

## License

(The MIT License)

Copyright (c) 2011 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[archive]: http://web.archive.org/web/20130314230536/http://hobbycoding.posterous.com/the-fastest-websocket-module-for-nodejs
# Ultron

[![Made by unshift](https://img.shields.io/badge/made%20by-unshift-00ffcc.svg?style=flat-square)](http://unshift.io)[![Version npm](http://img.shields.io/npm/v/ultron.svg?style=flat-square)](http://browsenpm.org/package/ultron)[![Build Status](http://img.shields.io/travis/unshiftio/ultron/master.svg?style=flat-square)](https://travis-ci.org/unshiftio/ultron)[![Dependencies](https://img.shields.io/david/unshiftio/ultron.svg?style=flat-square)](https://david-dm.org/unshiftio/ultron)[![Coverage Status](http://img.shields.io/coveralls/unshiftio/ultron/master.svg?style=flat-square)](https://coveralls.io/r/unshiftio/ultron?branch=master)[![IRC channel](http://img.shields.io/badge/IRC-irc.freenode.net%23unshift-00a8ff.svg?style=flat-square)](http://webchat.freenode.net/?channels=unshift)

Ultron is a high-intelligence robot. It gathers intelligence so it can start
improving upon his rudimentary design. It will learn your event emitting
patterns and find ways to exterminate them. Allowing you to remove only the
event emitters that **you** assigned and not the ones that your users or
developers assigned. This can prevent race conditions, memory leaks and even file
descriptor leaks from ever happening as you won't remove clean up processes.

## Installation

The module is designed to be used in browsers using browserify and in Node.js.
You can install the module through the public npm registry by running the
following command in CLI:

```
npm install --save ultron
```

## Usage

In all examples we assume that you've required the library as following:

```js
'use strict';

var Ultron = require('ultron');
```

Now that we've required the library we can construct our first `Ultron` instance.
The constructor requires one argument which should be the `EventEmitter`
instance that we need to operate upon. This can be the `EventEmitter` module
that ships with Node.js or `EventEmitter3` or anything else as long as it
follow the same API and internal structure as these 2. So with that in mind we
can create the instance:

```js
//
// For the sake of this example we're going to construct an empty EventEmitter
//
var EventEmitter = require('events').EventEmitter; // or require('eventmitter3');
var events = new EventEmitter();

var ultron = new Ultron(events);
```

You can now use the following API's from the Ultron instance:

### Ultron.on

Register a new event listener for the given event. It follows the exact same API
as `EventEmitter.on` but it will return itself instead of returning the
EventEmitter instance. If you are using EventEmitter3 it also supports the
context param:

```js
ultron.on('event-name', handler, { custom: 'function context' });
```

### Ultron.once

Exactly the same as the [Ultron.on](#ultronon) but it only allows the execution
once.

### Ultron.remove

This is where all the magic happens and the safe removal starts. This function
accepts different argument styles:

- No arguments, assume that all events need to be removed so it will work as
  `removeAllListeners()` API.
- 1 argument, when it's a string it will be split on ` ` and `,` to create a
  list of events that need to be cleared.
- Multiple arguments, we assume that they are all names of events that need to
  be cleared.

```js
ultron.remove('foo, bar baz');        // Removes foo, bar and baz.
ultron.remove('foo', 'bar', 'baz');   // Removes foo, bar and baz.
ultron.remove();                      // Removes everything.
```

If you just want to remove a single event listener using a function reference
you can still use the EventEmitter's `removeListener(event, fn)` API:

```js
function foo() {}

ulton.on('foo', foo);
events.removeListener('foo', foo);
```

## License

MIT
# options.js #

A very light-weight in-code option parsers for node.js.

## Usage ##

``` js
var Options = require("options");

// Create an Options object
function foo(options) {
        var default_options = {
                foo : "bar"
        };
        
        // Create an option object with default value
        var opts = new Options(default_options);
        
        // Merge options
        opts = opts.merge(options);
        
        // Reset to default value
        opts.reset();
        
        // Copy selected attributes out
        var seled_att = opts.copy("foo");
        
        // Read json options from a file. 
        opts.read("options.file"); // Sync
        opts.read("options.file", function(err){ // Async
                if(err){ // If error occurs
                        console.log("File error.");
                }else{
                        // No error
                }
        });
        
        // Attributes defined or not
        opts.isDefinedAndNonNull("foobar");
        opts.isDefined("foobar");
}

```


## License ##

(The MIT License)

Copyright (c) 2012 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# After [![Build Status][1]][2]

Invoke callback after n calls

## Status: production ready

## Example

    var after = require("after")
        , next = after(3, logItWorks)

    next()
    next()
    next() // it works

    function logItWorks() {
        console.log("it works!")
    }

## Example with error handling

    var after = require("after")
        , next = after(3, logError)

    next()
    next(new Error("oops")) // logs oops
    next() // does nothing

    function logError(err) {
        console.log(err)
    }

## After < 0.6.0

Older versions of after had iterators and flows in them.

These have been replaced with seperate modules

 - [iterators][8]
 - [composite][9]

## Installation

`npm install after`

## Tests

`npm test`

## Blog post

 - [Flow control in node.js][3]

## Examples :

 - [Determining the end of asynchronous operations][4]
 - [In javascript what are best practices for executing multiple asynchronous functions][5]
 - [JavaScript performance long running tasks][6]
 - [Synchronous database queries with node.js][7]

## Contributors

 - Raynos

## MIT Licenced

  [1]: https://secure.travis-ci.org/Raynos/after.png
  [2]: http://travis-ci.org/Raynos/after
  [3]: http://raynos.org/blog/2/Flow-control-in-node.js
  [4]: http://stackoverflow.com/questions/6852059/determining-the-end-of-asynchronous-operations-javascript/6852307#6852307
  [5]: http://stackoverflow.com/questions/6869872/in-javascript-what-are-best-practices-for-executing-multiple-asynchronous-functi/6870031#6870031
  [6]: http://stackoverflow.com/questions/6864397/javascript-performance-long-running-tasks/6889419#6889419
  [7]: http://stackoverflow.com/questions/6597493/synchronous-database-queries-with-node-js/6620091#6620091
  [8]: http://github.com/Raynos/iterators
  [9]: http://github.com/Raynos/composite
# How to
```javascript
var sliceBuffer = require('arraybuffer.slice');
var ab = (new Int8Array(5)).buffer;
var sliced = sliceBuffer(ab, 1, 3);
sliced = sliceBuffer(ab, 1);
```

# Licence (MIT)
Copyright (C) 2013 Rase-


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
has-binarydata.js
=================

Simple module to test if an object contains binary data

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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
Blob
====

A module that exports a constructor that uses window.Blob when available, and a BlobBuilder with any vendor prefix in other cases. If neither is available, it exports undefined.

Usage:

```javascript
var Blob = require('blob');
var b = new Blob(['hi', 'constructing', 'a', 'blob']);
```

## Licence
MIT
# base64-arraybuffer

[![Build Status](https://travis-ci.org/niklasvh/base64-arraybuffer.png)](https://travis-ci.org/niklasvh/base64-arraybuffer)

Encode/decode base64 data into ArrayBuffers

## Getting Started
Install the module with: `npm install base64-arraybuffer`

## API
The library encodes and decodes base64 to and from ArrayBuffers

 - __encode(buffer)__ - Encodes `ArrayBuffer` into base64 string
 - __decode(str)__ - Decodes base64 string to `ArrayBuffer`

## Release History

 - 0.1.2 - Fix old format of typed arrays
 - 0.1.0 - Initial version, basic decode/encode base64 to and from ArrayBuffer

## License
Copyright (c) 2012 Niklas von Hertzen
Licensed under the MIT license.
# utf8.js [![Build status](https://travis-ci.org/mathiasbynens/utf8.js.svg?branch=master)](https://travis-ci.org/mathiasbynens/utf8.js) [![Code coverage status](http://img.shields.io/coveralls/mathiasbynens/utf8.js/master.svg)](https://coveralls.io/r/mathiasbynens/utf8.js) [![Dependency status](https://gemnasium.com/mathiasbynens/utf8.js.svg)](https://gemnasium.com/mathiasbynens/utf8.js)

_utf8.js_ is a well-tested UTF-8 encoder/decoder written in JavaScript. Unlike many other JavaScript solutions, it is designed to be a _proper_ UTF-8 encoder/decoder: it can encode/decode any scalar Unicode code point values, as per [the Encoding Standard](https://encoding.spec.whatwg.org/#utf-8). [Here’s an online demo.](https://mothereff.in/utf-8)

Feel free to fork if you see possible improvements!

## Installation

Via [npm](https://www.npmjs.org/):

```bash
npm install utf8
```

Via [Bower](http://bower.io/):

```bash
bower install utf8
```

Via [Component](https://github.com/component/component):

```bash
component install mathiasbynens/utf8.js
```

In a browser:

```html
<script src="utf8.js"></script>
```

In [Narwhal](http://narwhaljs.org/), [Node.js](https://nodejs.org/), and [RingoJS ≥ v0.8.0](http://ringojs.org/):

```js
var utf8 = require('utf8');
```

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('utf8.js');
```

Using an AMD loader like [RequireJS](http://requirejs.org/):

```js
require(
  {
    'paths': {
      'utf8': 'path/to/utf8'
    }
  },
  ['utf8'],
  function(utf8) {
    console.log(utf8);
  }
);
```

## API

### `utf8.encode(string)`

Encodes any given JavaScript string (`string`) as UTF-8, and returns the UTF-8-encoded version of the string. It throws an error if the input string contains a non-scalar value, i.e. a lone surrogate. (If you need to be able to encode non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
// U+00A9 COPYRIGHT SIGN; see http://codepoints.net/U+00A9
utf8.encode('\xA9');
// → '\xC2\xA9'
// U+10001 LINEAR B SYLLABLE B038 E; see http://codepoints.net/U+10001
utf8.encode('\uD800\uDC01');
// → '\xF0\x90\x80\x81'
```

### `utf8.decode(byteString)`

Decodes any given UTF-8-encoded string (`byteString`) as UTF-8, and returns the UTF-8-decoded version of the string. It throws an error when malformed UTF-8 is detected. (If you need to be able to decode encoded non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
utf8.decode('\xC2\xA9');
// → '\xA9'

utf8.decode('\xF0\x90\x80\x81');
// → '\uD800\uDC01'
// → U+10001 LINEAR B SYLLABLE B038 E
```

### `utf8.version`

A string representing the semantic version number.

## Support

utf8.js has been tested in at least Chrome 27-39, Firefox 3-34, Safari 4-8, Opera 10-28, IE 6-11, Node.js v0.10.0, Narwhal 0.3.2, RingoJS 0.8-0.11, PhantomJS 1.9.0, and Rhino 1.7RC4.

## Unit tests & code coverage

After cloning this repository, run `npm install` to install the dependencies needed for development and testing. You may want to install Istanbul _globally_ using `npm install istanbul -g`.

Once that’s done, you can run the unit tests in Node using `npm test` or `node tests/tests.js`. To run the tests in Rhino, Ringo, Narwhal, PhantomJS, and web browsers as well, use `grunt test`.

To generate the code coverage report, use `grunt cover`.

## FAQ

### Why is the first release named v2.0.0? Haven’t you heard of [semantic versioning](http://semver.org/)?

Long before utf8.js was created, the `utf8` module on npm was registered and used by another (slightly buggy) library. @ryanmcgrath was kind enough to give me access to the `utf8` package on npm when I told him about utf8.js. Since there has already been a v1.0.0 release of the old library, and to avoid breaking backwards compatibility with projects that rely on the `utf8` npm package, I decided the tag the first release of utf8.js as v2.0.0 and take it from there.

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

utf8.js is available under the [MIT](https://mths.be/mit) license.
# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT# jQuery

> jQuery is a fast, small, and feature-rich JavaScript library.

For information on how to get started and how to use jQuery, please see [jQuery's documentation](http://api.jquery.com/).
For source files and issues, please visit the [jQuery repo](https://github.com/jquery/jquery).

## Including jQuery

Below are some of the most common ways to include jQuery.

### Browser

#### Script tag

```html
<script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
```

#### Babel

[Babel](http://babeljs.io/) is a next generation JavaScript compiler. One of the features is the ability to use ES6/ES2015 modules now, even though browsers do not yet support this feature natively.

```js
import $ from "jquery";
```

#### Browserify/Webpack

There are several ways to use [Browserify](http://browserify.org/) and [Webpack](https://webpack.github.io/). For more information on using these tools, please refer to the corresponding project's documention. In the script, including jQuery will usually look like this...

```js
var $ = require("jquery");
```

#### AMD (Asynchronous Module Definition)

AMD is a module format built for the browser. For more information, we recommend [require.js' documentation](http://requirejs.org/docs/whyamd.html).

```js
define(["jquery"], function($) {

});
```

### Node

To include jQuery in [Node](nodejs.org), first install with npm.

```sh
npm install jquery
```

For jQuery to work in Node, a window with a document is required. Since no such window exists natively in Node, one can be mocked by tools such as [jsdom](https://github.com/tmpvar/jsdom). This can be useful for testing purposes.

```js
require("jsdom").env("", function(err, window) {
	if (err) {
		console.error(err);
		return;
	}

	var $ = require("jquery")(window);
});
```

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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
# Benchmark.js <sup>v1.0.0</sup>

A [robust](http://calendar.perfplanet.com/2010/bulletproof-javascript-benchmarks/ "Bulletproof JavaScript benchmarks") benchmarking library that works on nearly all JavaScript platforms<sup><a name="fnref1" href="#fn1">1</a></sup>, supports high-resolution timers, and returns statistically significant results. As seen on [jsPerf](http://jsperf.com/).

## BestieJS

Benchmark.js is part of the BestieJS *"Best in Class"* module collection. This means we promote solid browser/environment support, ES5 precedents, unit testing, and plenty of documentation.

## Documentation

The documentation for Benchmark.js can be viewed here: <http://benchmarkjs.com/docs>

For a list of upcoming features, check out our [roadmap](https://github.com/bestiejs/benchmark.js/wiki/Roadmap).

## Support

Benchmark.js has been tested in at least Adobe AIR 3.1, Chrome 5-21, Firefox 1.5-13, IE 6-9, Opera 9.25-12.01, Safari 3-6, Node.js 0.8.6, Narwhal 0.3.2, RingoJS 0.8, and Rhino 1.7RC5.

## Installation and usage

In a browser or Adobe AIR:

~~~ html
<script src="benchmark.js"></script>
~~~

Optionally, expose Java’s nanosecond timer by adding the `nano` applet to the `<body>`:

~~~ html
<applet code="nano" archive="nano.jar"></applet>
~~~

Or enable Chrome’s microsecond timer by using the [command line switch](http://peter.sh/experiments/chromium-command-line-switches/#enable-benchmarking):

    --enable-benchmarking

Via [npm](http://npmjs.org/):

~~~ bash
npm install benchmark
~~~

In [Node.js](http://nodejs.org/) and [RingoJS v0.8.0+](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark');
~~~

Optionally, use the [microtime module](https://github.com/wadey/node-microtime) by Wade Simmons:

~~~ bash
npm install microtime
~~~

In [RingoJS v0.7.0-](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark').Benchmark;
~~~

In [Rhino](http://www.mozilla.org/rhino/):

~~~ js
load('benchmark.js');
~~~

In an AMD loader like [RequireJS](http://requirejs.org/):

~~~ js
require({
  'paths': {
    'benchmark': 'path/to/benchmark'
  }
},
['benchmark'], function(Benchmark) {
  console.log(Benchmark.version);
});

// or with platform.js
// https://github.com/bestiejs/platform.js
require({
  'paths': {
    'benchmark': 'path/to/benchmark',
    'platform': 'path/to/platform'
  }
},
['benchmark', 'platform'], function(Benchmark, platform) {
  Benchmark.platform = platform;
  console.log(Benchmark.platform.name);
});
~~~

Usage example:

~~~ js
var suite = new Benchmark.Suite;

// add tests
suite.add('RegExp#test', function() {
  /o/.test('Hello World!');
})
.add('String#indexOf', function() {
  'Hello World!'.indexOf('o') > -1;
})
// add listeners
.on('cycle', function(event) {
  console.log(String(event.target));
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
// run async
.run({ 'async': true });

// logs:
// > RegExp#test x 4,161,532 +-0.99% (59 cycles)
// > String#indexOf x 6,139,623 +-1.00% (131 cycles)
// > Fastest is String#indexOf
~~~

## Authors

* [Mathias Bynens](http://mathiasbynens.be/)
  [![twitter/mathias](http://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter")
* [John-David Dalton](http://allyoucanleet.com/)
  [![twitter/jdalton](http://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter")

## Contributors

* [Kit Cambridge](http://kitcambridge.github.com/)
  [![twitter/kitcambridge](http://gravatar.com/avatar/6662a1d02f351b5ef2f8b4d815804661?s=70)](https://twitter.com/kitcambridge "Follow @kitcambridge on Twitter")
# Benchmark.js <sup>v1.0.0</sup>

<!-- div -->


<!-- div -->

## <a id="Benchmark"></a>`Benchmark`
* [`Benchmark`](#benchmarkname-fn--options)
* [`Benchmark.version`](#benchmarkversion)
* [`Benchmark.deepClone`](#benchmarkdeepclonevalue)
* [`Benchmark.each`](#benchmarkeachobject-callback-thisarg)
* [`Benchmark.extend`](#benchmarkextenddestination--source)
* [`Benchmark.filter`](#benchmarkfilterarray-callback-thisarg)
* [`Benchmark.forEach`](#benchmarkforeacharray-callback-thisarg)
* [`Benchmark.formatNumber`](#benchmarkformatnumbernumber)
* [`Benchmark.forOwn`](#benchmarkforownobject-callback-thisarg)
* [`Benchmark.hasKey`](#benchmarkhaskeyobject-key)
* [`Benchmark.indexOf`](#benchmarkindexofarray-value--fromindex0)
* [`Benchmark.interpolate`](#benchmarkinterpolatestring-object)
* [`Benchmark.invoke`](#benchmarkinvokebenches-name--arg1-arg2-)
* [`Benchmark.join`](#benchmarkjoinobject--separator1--separator2:)
* [`Benchmark.map`](#benchmarkmaparray-callback-thisarg)
* [`Benchmark.pluck`](#benchmarkpluckarray-property)
* [`Benchmark.reduce`](#benchmarkreducearray-callback-accumulator)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype`
* [`Benchmark.prototype.aborted`](#benchmarkprototypeaborted)
* [`Benchmark.prototype.compiled`](#benchmarkprototypecompiled)
* [`Benchmark.prototype.count`](#benchmarkprototypecount)
* [`Benchmark.prototype.cycles`](#benchmarkprototypecycles)
* [`Benchmark.prototype.fn`](#benchmarkprototypefn)
* [`Benchmark.prototype.hz`](#benchmarkprototypehz)
* [`Benchmark.prototype.running`](#benchmarkprototyperunning)
* [`Benchmark.prototype.setup`](#benchmarkprototypesetup)
* [`Benchmark.prototype.teardown`](#benchmarkprototypeteardown)
* [`Benchmark.prototype.abort`](#benchmarkprototypeabort)
* [`Benchmark.prototype.clone`](#benchmarkprototypecloneoptions)
* [`Benchmark.prototype.compare`](#benchmarkprototypecompareother)
* [`Benchmark.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.prototype.reset`](#benchmarkprototypereset)
* [`Benchmark.prototype.run`](#benchmarkprototyperunoptions)
* [`Benchmark.prototype.toString`](#benchmarkprototypetostring)

<!-- /div -->


<!-- div -->

## `Benchmark.options`
* [`Benchmark.options`](#benchmarkoptions)
* [`Benchmark.options.async`](#benchmarkoptionsasync)
* [`Benchmark.options.defer`](#benchmarkoptionsdefer)
* [`Benchmark.options.delay`](#benchmarkoptionsdelay)
* [`Benchmark.options.id`](#benchmarkoptionsid)
* [`Benchmark.options.initCount`](#benchmarkoptionsinitcount)
* [`Benchmark.options.maxTime`](#benchmarkoptionsmaxtime)
* [`Benchmark.options.minSamples`](#benchmarkoptionsminsamples)
* [`Benchmark.options.minTime`](#benchmarkoptionsmintime)
* [`Benchmark.options.name`](#benchmarkoptionsname)
* [`Benchmark.options.onAbort`](#benchmarkoptionsonabort)
* [`Benchmark.options.onComplete`](#benchmarkoptionsoncomplete)
* [`Benchmark.options.onCycle`](#benchmarkoptionsoncycle)
* [`Benchmark.options.onError`](#benchmarkoptionsonerror)
* [`Benchmark.options.onReset`](#benchmarkoptionsonreset)
* [`Benchmark.options.onStart`](#benchmarkoptionsonstart)

<!-- /div -->


<!-- div -->

## `Benchmark.platform`
* [`Benchmark.platform`](#benchmarkplatform)
* [`Benchmark.platform.description`](#benchmarkplatformdescription)
* [`Benchmark.platform.layout`](#benchmarkplatformlayout)
* [`Benchmark.platform.manufacturer`](#benchmarkplatformmanufacturer)
* [`Benchmark.platform.name`](#benchmarkplatformname)
* [`Benchmark.platform.os`](#benchmarkplatformos)
* [`Benchmark.platform.prerelease`](#benchmarkplatformprerelease)
* [`Benchmark.platform.product`](#benchmarkplatformproduct)
* [`Benchmark.platform.version`](#benchmarkplatformversion)
* [`Benchmark.platform.toString`](#benchmarkplatformtostring)

<!-- /div -->


<!-- div -->

## `Benchmark.support`
* [`Benchmark.support`](#benchmarksupport)
* [`Benchmark.support.air`](#benchmarksupportair)
* [`Benchmark.support.argumentsClass`](#benchmarksupportargumentsclass)
* [`Benchmark.support.browser`](#benchmarksupportbrowser)
* [`Benchmark.support.charByIndex`](#benchmarksupportcharbyindex)
* [`Benchmark.support.charByOwnIndex`](#benchmarksupportcharbyownindex)
* [`Benchmark.support.decompilation`](#benchmarksupportdecompilation)
* [`Benchmark.support.descriptors`](#benchmarksupportdescriptors)
* [`Benchmark.support.getAllKeys`](#benchmarksupportgetallkeys)
* [`Benchmark.support.iteratesOwnLast`](#benchmarksupportiteratesownfirst)
* [`Benchmark.support.java`](#benchmarksupportjava)
* [`Benchmark.support.nodeClass`](#benchmarksupportnodeclass)
* [`Benchmark.support.timeout`](#benchmarksupporttimeout)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`
* [`Benchmark.prototype.error`](#benchmarkprototypeerror)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`
* [`Benchmark.prototype.stats`](#benchmarkprototypestats)
* [`Benchmark.prototype.stats.deviation`](#benchmark-statsdeviation)
* [`Benchmark.prototype.stats.mean`](#benchmark-statsmean)
* [`Benchmark.prototype.stats.moe`](#benchmark-statsmoe)
* [`Benchmark.prototype.stats.rme`](#benchmark-statsrme)
* [`Benchmark.prototype.stats.sample`](#benchmark-statssample)
* [`Benchmark.prototype.stats.sem`](#benchmark-statssem)
* [`Benchmark.prototype.stats.variance`](#benchmark-statsvariance)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`
* [`Benchmark.prototype.times`](#benchmarkprototypetimes)
* [`Benchmark.prototype.times.cycle`](#benchmark-timescycle)
* [`Benchmark.prototype.times.elapsed`](#benchmark-timeselapsed)
* [`Benchmark.prototype.times.period`](#benchmark-timesperiod)
* [`Benchmark.prototype.times.timeStamp`](#benchmark-timestimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`
* [`Benchmark.Deferred`](#benchmarkdeferredclone)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`
* [`Benchmark.Deferred.prototype.benchmark`](#benchmarkdeferredprototypebenchmark)
* [`Benchmark.Deferred.prototype.cycles`](#benchmarkdeferredprototypecycles)
* [`Benchmark.Deferred.prototype.elapsed`](#benchmarkdeferredprototypeelapsed)
* [`Benchmark.Deferred.prototype.resolve`](#benchmarkdeferredprototyperesolve)
* [`Benchmark.Deferred.prototype.timeStamp`](#benchmarkdeferredprototypetimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Event`
* [`Benchmark.Event`](#benchmarkeventtype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`
* [`Benchmark.Event.prototype.aborted`](#benchmarkeventprototypeaborted)
* [`Benchmark.Event.prototype.cancelled`](#benchmarkeventprototypecancelled)
* [`Benchmark.Event.prototype.result`](#benchmarkeventprototyperesult)
* [`Benchmark.Event.prototype.timeStamp`](#benchmarkeventprototypetimestamp)
* [`Benchmark.Event.prototype.type`](#benchmarkeventprototypetype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`
* [`Benchmark.Event.prototype.currentTarget`](#benchmarkeventprototypecurrenttarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`
* [`Benchmark.Event.prototype.target`](#benchmarkeventprototypetarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite`
* [`Benchmark.Suite`](#benchmarksuitename--options)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`
* [`Benchmark.Suite.prototype.aborted`](#benchmarksuiteprototypeaborted)
* [`Benchmark.Suite.prototype.length`](#benchmarksuiteprototypelength)
* [`Benchmark.Suite.prototype.running`](#benchmarksuiteprototyperunning)
* [`Benchmark.Suite.prototype.abort`](#benchmarksuiteprototypeabort)
* [`Benchmark.Suite.prototype.add`](#benchmarksuiteprototypeaddname-fn--options)
* [`Benchmark.Suite.prototype.clone`](#benchmarksuiteprototypecloneoptions)
* [`Benchmark.Suite.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.Suite.prototype.filter`](#benchmarksuiteprototypefiltercallback)
* [`Benchmark.Suite.prototype.forEach`](#benchmarksuiteprototypeforeachcallback)
* [`Benchmark.Suite.prototype.indexOf`](#benchmarksuiteprototypeindexofvalue)
* [`Benchmark.Suite.prototype.invoke`](#benchmarksuiteprototypeinvokename--arg1-arg2-)
* [`Benchmark.Suite.prototype.join`](#benchmarksuiteprototypejoinseparator-)
* [`Benchmark.Suite.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.Suite.prototype.map`](#benchmarksuiteprototypemapcallback)
* [`Benchmark.Suite.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.Suite.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.Suite.prototype.pluck`](#benchmarksuiteprototypepluckproperty)
* [`Benchmark.Suite.prototype.pop`](#benchmarksuiteprototypepop)
* [`Benchmark.Suite.prototype.push`](#benchmarksuiteprototypepush)
* [`Benchmark.Suite.prototype.reduce`](#benchmarksuiteprototypereducecallback-accumulator)
* [`Benchmark.Suite.prototype.reset`](#benchmarksuiteprototypereset)
* [`Benchmark.Suite.prototype.reverse`](#benchmarksuiteprototypereverse)
* [`Benchmark.Suite.prototype.run`](#benchmarksuiteprototyperunoptions)
* [`Benchmark.Suite.prototype.shift`](#benchmarksuiteprototypeshift)
* [`Benchmark.Suite.prototype.slice`](#benchmarksuiteprototypeslicestart-end)
* [`Benchmark.Suite.prototype.sort`](#benchmarksuiteprototypesortcomparefnnull)
* [`Benchmark.Suite.prototype.splice`](#benchmarksuiteprototypesplicestart-deletecount--val1-val2-)
* [`Benchmark.Suite.prototype.unshift`](#benchmarksuiteprototypeunshift)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`
* [`Benchmark.Suite.options`](#benchmarksuiteoptions)
* [`Benchmark.Suite.options.name`](#benchmarksuiteoptionsname)

<!-- /div -->


<!-- /div -->


<!-- div -->


<!-- div -->

## `Benchmark`

<!-- div -->

### <a id="benchmarkname-fn--options"></a>`Benchmark(name, fn [, options={}])`
<a href="#benchmarkname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L404 "View in source") [&#x24C9;][1]

The Benchmark constructor.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var bench = new Benchmark(fn);

// or using a name first
var bench = new Benchmark('foo', fn);

// or with options
var bench = new Benchmark('foo', fn, {

  // displayed by Benchmark#toString if `name` is not available
  'id': 'xyz',

  // called when the benchmark starts running
  'onStart': onStart,

  // called after each run cycle
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the benchmark completes running
  'onComplete': onComplete,

  // compiled/called before the test loop
  'setup': setup,

  // compiled/called after the test loop
  'teardown': teardown
});

// or name and options
var bench = new Benchmark('foo', {

  // a flag to indicate the benchmark is deferred
  'defer': true,

  // benchmark test function
  'fn': function(deferred) {
    // call resolve() when the deferred test is finished
    deferred.resolve();
  }
});

// or options only
var bench = new Benchmark({

  // benchmark name
  'name': 'foo',

  // benchmark test as a string
  'fn': '[1,2,3,4].sort()'
});

// a test's `this` binding is set to the benchmark instance
var bench = new Benchmark('foo', function() {
  'My name is '.concat(this.name); // My name is foo
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkversion"></a>`Benchmark.version`
<a href="#benchmarkversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3267 "View in source") [&#x24C9;][1]

*(String)*: The semantic version number.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeepclonevalue"></a>`Benchmark.deepClone(value)`
<a href="#benchmarkdeepclonevalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1225 "View in source") [&#x24C9;][1]

A deep clone utility.

#### Arguments
1. `value` *(Mixed)*: The value to clone.

#### Returns
*(Mixed)*: The cloned value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeachobject-callback-thisarg"></a>`Benchmark.each(object, callback, thisArg)`
<a href="#benchmarkeachobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1400 "View in source") [&#x24C9;][1]

An iteration utility for arrays and objects. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Array|Object)*: The object to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array, Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkextenddestination--source"></a>`Benchmark.extend(destination [, source={}])`
<a href="#benchmarkextenddestination--source">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1446 "View in source") [&#x24C9;][1]

Copies enumerable properties from the source(s) object to the destination object.

#### Arguments
1. `destination` *(Object)*: The destination object.
2. `[source={}]` *(Object)*: The source object.

#### Returns
*(Object)*: The destination object.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkfilterarray-callback-thisarg"></a>`Benchmark.filter(array, callback, thisArg)`
<a href="#benchmarkfilterarray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1485 "View in source") [&#x24C9;][1]

A generic `Array#filter` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function|String)*: The function/alias called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values that passed callback filter.

#### Example
~~~ js
// get odd numbers
Benchmark.filter([1, 2, 3, 4, 5], function(n) {
  return n % 2;
}); // -> [1, 3, 5];

// get fastest benchmarks
Benchmark.filter(benches, 'fastest');

// get slowest benchmarks
Benchmark.filter(benches, 'slowest');

// get benchmarks that completed without erroring
Benchmark.filter(benches, 'successful');
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforeacharray-callback-thisarg"></a>`Benchmark.forEach(array, callback, thisArg)`
<a href="#benchmarkforeacharray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1518 "View in source") [&#x24C9;][1]

A generic `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: Returns the array iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkformatnumbernumber"></a>`Benchmark.formatNumber(number)`
<a href="#benchmarkformatnumbernumber">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1557 "View in source") [&#x24C9;][1]

Converts a number to a more readable comma-separated string representation.

#### Arguments
1. `number` *(Number)*: The number to convert.

#### Returns
*(String)*: The more readable string representation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforownobject-callback-thisarg"></a>`Benchmark.forOwn(object, callback, thisArg)`
<a href="#benchmarkforownobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1545 "View in source") [&#x24C9;][1]

Iterates over an object's own properties, executing the `callback` for each. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `callback` *(Function)*: The function executed per own property.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkhaskeyobject-key"></a>`Benchmark.hasKey(object, key)`
<a href="#benchmarkhaskeyobject-key">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1572 "View in source") [&#x24C9;][1]

Checks if an object has the specified key as a direct property.

#### Arguments
1. `object` *(Object)*: The object to check.
2. `key` *(String)*: The key to check for.

#### Returns
*(Boolean)*: Returns `true` if key is a direct property, else `false`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkindexofarray-value--fromindex0"></a>`Benchmark.indexOf(array, value [, fromIndex=0])`
<a href="#benchmarkindexofarray-value--fromindex0">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1608 "View in source") [&#x24C9;][1]

A generic `Array#indexOf` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `value` *(Mixed)*: The value to search for.
3. `[fromIndex=0]` *(Number)*: The index to start searching from.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinterpolatestring-object"></a>`Benchmark.interpolate(string, object)`
<a href="#benchmarkinterpolatestring-object">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1630 "View in source") [&#x24C9;][1]

Modify a string by replacing named tokens with matching object property values.

#### Arguments
1. `string` *(String)*: The string to modify.
2. `object` *(Object)*: The template object.

#### Returns
*(String)*: The modified string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinvokebenches-name--arg1-arg2-"></a>`Benchmark.invoke(benches, name [, arg1, arg2, ...])`
<a href="#benchmarkinvokebenches-name--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1677 "View in source") [&#x24C9;][1]

Invokes a method on all items in an array.

#### Arguments
1. `benches` *(Array)*: Array of benchmarks to iterate over.
2. `name` *(String|Object)*: The name of the method to invoke OR options object.
3. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

#### Example
~~~ js
// invoke `reset` on all benchmarks
Benchmark.invoke(benches, 'reset');

// invoke `emit` with arguments
Benchmark.invoke(benches, 'emit', 'complete', listener);

// invoke `run(true)`, treat benchmarks as a queue, and register invoke callbacks
Benchmark.invoke(benches, {

  // invoke the `run` method
  'name': 'run',

  // pass a single argument
  'args': true,

  // treat as queue, removing benchmarks from front of `benches` until empty
  'queued': true,

  // called before any benchmarks have been invoked.
  'onStart': onStart,

  // called between invoking benchmarks
  'onCycle': onCycle,

  // called after all benchmarks have been invoked.
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkjoinobject--separator1--separator2:"></a>`Benchmark.join(object [, separator1=',', separator2=': '])`
<a href="#benchmarkjoinobject--separator1--separator2:">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1831 "View in source") [&#x24C9;][1]

Creates a string of joined array values or object key-value pairs.

#### Arguments
1. `object` *(Array|Object)*: The object to operate on.
2. `[separator1=',']` *(String)*: The separator used between key-value pairs.
3. `[separator2=': ']` *(String)*: The separator used between keys and values.

#### Returns
*(String)*: The joined result.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkmaparray-callback-thisarg"></a>`Benchmark.map(array, callback, thisArg)`
<a href="#benchmarkmaparray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1853 "View in source") [&#x24C9;][1]

A generic `Array#map` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkpluckarray-property"></a>`Benchmark.pluck(array, property)`
<a href="#benchmarkpluckarray-property">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1869 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all items in an array.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkreducearray-callback-accumulator"></a>`Benchmark.reduce(array, callback, accumulator)`
<a href="#benchmarkreducearray-callback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1885 "View in source") [&#x24C9;][1]

A generic `Array#reduce` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype`

<!-- div -->

### <a id="benchmarkprototypeaborted"></a>`Benchmark.prototype.aborted`
<a href="#benchmarkprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3377 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompiled"></a>`Benchmark.prototype.compiled`
<a href="#benchmarkprototypecompiled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3353 "View in source") [&#x24C9;][1]

*(Function, String)*: The compiled test function.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecount"></a>`Benchmark.prototype.count`
<a href="#benchmarkprototypecount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3329 "View in source") [&#x24C9;][1]

*(Number)*: The number of times a test was executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecycles"></a>`Benchmark.prototype.cycles`
<a href="#benchmarkprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3337 "View in source") [&#x24C9;][1]

*(Number)*: The number of cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypefn"></a>`Benchmark.prototype.fn`
<a href="#benchmarkprototypefn">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3369 "View in source") [&#x24C9;][1]

*(Function, String)*: The test to benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypehz"></a>`Benchmark.prototype.hz`
<a href="#benchmarkprototypehz">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3345 "View in source") [&#x24C9;][1]

*(Number)*: The number of executions per second.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunning"></a>`Benchmark.prototype.running`
<a href="#benchmarkprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3385 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypesetup"></a>`Benchmark.prototype.setup`
<a href="#benchmarkprototypesetup">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3448 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **before** the test loop.

#### Example
~~~ js
// basic usage
var bench = Benchmark({
  'setup': function() {
    var c = this.count,
        element = document.getElementById('container');
    while (c--) {
      element.appendChild(document.createElement('div'));
    }
  },
  'fn': function() {
    element.removeChild(element.lastChild);
  }
});

// compiles to something like:
var c = this.count,
    element = document.getElementById('container');
while (c--) {
  element.appendChild(document.createElement('div'));
}
var start = new Date;
while (count--) {
  element.removeChild(element.lastChild);
}
var end = new Date - start;

// or using strings
var bench = Benchmark({
  'setup': '\
    var a = 0;\n\
    (function() {\n\
      (function() {\n\
        (function() {',
  'fn': 'a += 1;',
  'teardown': '\
         }())\n\
       }())\n\
     }())'
});

// compiles to something like:
var a = 0;
(function() {
  (function() {
    (function() {
      var start = new Date;
      while (count--) {
        a += 1;
      }
      var end = new Date - start;
    }())
  }())
}())
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeteardown"></a>`Benchmark.prototype.teardown`
<a href="#benchmarkprototypeteardown">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3456 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **after** the test loop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeabort"></a>`Benchmark.prototype.abort()`
<a href="#benchmarkprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2218 "View in source") [&#x24C9;][1]

Aborts the benchmark without recording times.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecloneoptions"></a>`Benchmark.prototype.clone(options)`
<a href="#benchmarkprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2257 "View in source") [&#x24C9;][1]

Creates a new benchmark using the same test and options.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new benchmark instance.

#### Example
~~~ js
var bizarro = bench.clone({
  'name': 'doppelganger'
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompareother"></a>`Benchmark.prototype.compare(other)`
<a href="#benchmarkprototypecompareother">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2280 "View in source") [&#x24C9;][1]

Determines if a benchmark is faster than another.

#### Arguments
1. `other` *(Object)*: The benchmark to compare.

#### Returns
*(Number)*: Returns `-1` if slower, `1` if faster, and `0` if indeterminate.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypereset"></a>`Benchmark.prototype.reset()`
<a href="#benchmarkprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2334 "View in source") [&#x24C9;][1]

Reset properties and abort if running.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunoptions"></a>`Benchmark.prototype.run([options={}])`
<a href="#benchmarkprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3000 "View in source") [&#x24C9;][1]

Runs the benchmark.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
bench.run();

// or with options
bench.run({ 'async': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypetostring"></a>`Benchmark.prototype.toString()`
<a href="#benchmarkprototypetostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2405 "View in source") [&#x24C9;][1]

Displays relevant benchmark information when coerced to a string.

#### Returns
*(String)*: A string representation of the benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.options`

<!-- div -->

### <a id="benchmarkoptions"></a>`Benchmark.options`
<a href="#benchmarkoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3049 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by benchmark instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsasync"></a>`Benchmark.options.async`
<a href="#benchmarkoptionsasync">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3058 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that benchmark cycles will execute asynchronously by default.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdefer"></a>`Benchmark.options.defer`
<a href="#benchmarkoptionsdefer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3066 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that the benchmark clock is deferred.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdelay"></a>`Benchmark.options.delay`
<a href="#benchmarkoptionsdelay">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3073 "View in source") [&#x24C9;][1]

*(Number)*: The delay between test cycles *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsid"></a>`Benchmark.options.id`
<a href="#benchmarkoptionsid">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3082 "View in source") [&#x24C9;][1]

*(String)*: Displayed by Benchmark#toString when a `name` is not available *(auto-generated if absent)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsinitcount"></a>`Benchmark.options.initCount`
<a href="#benchmarkoptionsinitcount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3090 "View in source") [&#x24C9;][1]

*(Number)*: The default number of times to execute a test on a benchmark's first cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmaxtime"></a>`Benchmark.options.maxTime`
<a href="#benchmarkoptionsmaxtime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3099 "View in source") [&#x24C9;][1]

*(Number)*: The maximum time a benchmark is allowed to run before finishing *(secs)*. Note: Cycle delays aren't counted toward the maximum time.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsminsamples"></a>`Benchmark.options.minSamples`
<a href="#benchmarkoptionsminsamples">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3107 "View in source") [&#x24C9;][1]

*(Number)*: The minimum sample size required to perform statistical analysis.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmintime"></a>`Benchmark.options.minTime`
<a href="#benchmarkoptionsmintime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3115 "View in source") [&#x24C9;][1]

*(Number)*: The time needed to reduce the percent uncertainty of measurement to `1`% *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsname"></a>`Benchmark.options.name`
<a href="#benchmarkoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3123 "View in source") [&#x24C9;][1]

*(String)*: The name of the benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonabort"></a>`Benchmark.options.onAbort`
<a href="#benchmarkoptionsonabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3131 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncomplete"></a>`Benchmark.options.onComplete`
<a href="#benchmarkoptionsoncomplete">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3139 "View in source") [&#x24C9;][1]

An event listener called when the benchmark completes running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncycle"></a>`Benchmark.options.onCycle`
<a href="#benchmarkoptionsoncycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3147 "View in source") [&#x24C9;][1]

An event listener called after each run cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonerror"></a>`Benchmark.options.onError`
<a href="#benchmarkoptionsonerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3155 "View in source") [&#x24C9;][1]

An event listener called when a test errors.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonreset"></a>`Benchmark.options.onReset`
<a href="#benchmarkoptionsonreset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3163 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is reset.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonstart"></a>`Benchmark.options.onStart`
<a href="#benchmarkoptionsonstart">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3171 "View in source") [&#x24C9;][1]

An event listener called when the benchmark starts running.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.platform`

<!-- div -->

### <a id="benchmarkplatform"></a>`Benchmark.platform`
<a href="#benchmarkplatform">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3182 "View in source") [&#x24C9;][1]

*(Object)*: Platform object with properties describing things like browser name, version, and operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformdescription"></a>`Benchmark.platform.description`
<a href="#benchmarkplatformdescription">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3190 "View in source") [&#x24C9;][1]

*(String)*: The platform description.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformlayout"></a>`Benchmark.platform.layout`
<a href="#benchmarkplatformlayout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3198 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser layout engine.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformmanufacturer"></a>`Benchmark.platform.manufacturer`
<a href="#benchmarkplatformmanufacturer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3222 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product's manufacturer.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformname"></a>`Benchmark.platform.name`
<a href="#benchmarkplatformname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3214 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser/environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformos"></a>`Benchmark.platform.os`
<a href="#benchmarkplatformos">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3230 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformprerelease"></a>`Benchmark.platform.prerelease`
<a href="#benchmarkplatformprerelease">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3238 "View in source") [&#x24C9;][1]

*(String, Null)*: The alpha/beta release indicator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformproduct"></a>`Benchmark.platform.product`
<a href="#benchmarkplatformproduct">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3206 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product hosting the browser.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformversion"></a>`Benchmark.platform.version`
<a href="#benchmarkplatformversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3246 "View in source") [&#x24C9;][1]

*(String, Null)*: The browser/environment version.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformtostring"></a>`Benchmark.platform.toString()`
<a href="#benchmarkplatformtostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3255 "View in source") [&#x24C9;][1]

Return platform description when the platform object is coerced to a string.

#### Returns
*(String)*: The platform description.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.support`

<!-- div -->

### <a id="benchmarksupport"></a>`Benchmark.support`
<a href="#benchmarksupport">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L135 "View in source") [&#x24C9;][1]

*(Object)*: An object used to flag environments/features.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportair"></a>`Benchmark.support.air`
<a href="#benchmarksupportair">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L145 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect Adobe AIR.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportargumentsclass"></a>`Benchmark.support.argumentsClass`
<a href="#benchmarksupportargumentsclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L153 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if `arguments` objects have the correct internal [[Class]] value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportbrowser"></a>`Benchmark.support.browser`
<a href="#benchmarksupportbrowser">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L161 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if in a browser environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyindex"></a>`Benchmark.support.charByIndex`
<a href="#benchmarksupportcharbyindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L169 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings support accessing characters by index.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyownindex"></a>`Benchmark.support.charByOwnIndex`
<a href="#benchmarksupportcharbyownindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L179 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings have indexes as own properties.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdecompilation"></a>`Benchmark.support.decompilation`
<a href="#benchmarksupportdecompilation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L207 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if functions support decompilation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdescriptors"></a>`Benchmark.support.descriptors`
<a href="#benchmarksupportdescriptors">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L228 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ property descriptor API.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportgetallkeys"></a>`Benchmark.support.getAllKeys`
<a href="#benchmarksupportgetallkeys">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L242 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ Object.getOwnPropertyNames().

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportiteratesownfirst"></a>`Benchmark.support.iteratesOwnFirst`
<a href="#benchmarksupportiteratesownfirst">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L255 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if own properties are iterated before inherited properties *(all but IE < `9`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportjava"></a>`Benchmark.support.java`
<a href="#benchmarksupportjava">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L190 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if Java is enabled/exposed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportnodeclass"></a>`Benchmark.support.nodeClass`
<a href="#benchmarksupportnodeclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L272 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if a node's [[Class]] is resolvable *(all but IE < `9`)* and that the JS engine errors when attempting to coerce an object to a string without a `toString` property value of `typeof` "function".

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupporttimeout"></a>`Benchmark.support.timeout`
<a href="#benchmarksupporttimeout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L198 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if the Timers API exists.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`

<!-- div -->

### <a id="benchmarkprototypeerror"></a>`Benchmark.prototype.error`
<a href="#benchmarkprototypeerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3361 "View in source") [&#x24C9;][1]

*(Object)*: The error object if the test failed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`

<!-- div -->

### <a id="benchmarkprototypestats"></a>`Benchmark.prototype.stats`
<a href="#benchmarkprototypestats">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3464 "View in source") [&#x24C9;][1]

*(Object)*: An object of stats including mean, margin or error, and standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsdeviation"></a>`Benchmark.prototype.stats.deviation`
<a href="#benchmark-statsdeviation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3496 "View in source") [&#x24C9;][1]

*(Number)*: The sample standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmean"></a>`Benchmark.prototype.stats.mean`
<a href="#benchmark-statsmean">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3504 "View in source") [&#x24C9;][1]

*(Number)*: The sample arithmetic mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmoe"></a>`Benchmark.prototype.stats.moe`
<a href="#benchmark-statsmoe">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3472 "View in source") [&#x24C9;][1]

*(Number)*: The margin of error.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsrme"></a>`Benchmark.prototype.stats.rme`
<a href="#benchmark-statsrme">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3480 "View in source") [&#x24C9;][1]

*(Number)*: The relative margin of error *(expressed as a percentage of the mean)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssample"></a>`Benchmark.prototype.stats.sample`
<a href="#benchmark-statssample">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3512 "View in source") [&#x24C9;][1]

*(Array)*: The array of sampled periods.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssem"></a>`Benchmark.prototype.stats.sem`
<a href="#benchmark-statssem">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3488 "View in source") [&#x24C9;][1]

*(Number)*: The standard error of the mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsvariance"></a>`Benchmark.prototype.stats.variance`
<a href="#benchmark-statsvariance">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3520 "View in source") [&#x24C9;][1]

*(Number)*: The sample variance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`

<!-- div -->

### <a id="benchmarkprototypetimes"></a>`Benchmark.prototype.times`
<a href="#benchmarkprototypetimes">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3529 "View in source") [&#x24C9;][1]

*(Object)*: An object of timing data including cycle, elapsed, period, start, and stop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timescycle"></a>`Benchmark.prototype.times.cycle`
<a href="#benchmark-timescycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3537 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the last cycle *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timeselapsed"></a>`Benchmark.prototype.times.elapsed`
<a href="#benchmark-timeselapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3545 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timesperiod"></a>`Benchmark.prototype.times.period`
<a href="#benchmark-timesperiod">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3553 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to execute the test once *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timestimestamp"></a>`Benchmark.prototype.times.timeStamp`
<a href="#benchmark-timestimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3561 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`

<!-- div -->

### <a id="benchmarkdeferredclone"></a>`Benchmark.Deferred(clone)`
<a href="#benchmarkdeferredclone">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L445 "View in source") [&#x24C9;][1]

The Deferred constructor.

#### Arguments
1. `clone` *(Object)*: The cloned benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`

<!-- div -->

### <a id="benchmarkdeferredprototypebenchmark"></a>`Benchmark.Deferred.prototype.benchmark`
<a href="#benchmarkdeferredprototypebenchmark">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3605 "View in source") [&#x24C9;][1]

*(Object)*: The deferred benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypecycles"></a>`Benchmark.Deferred.prototype.cycles`
<a href="#benchmarkdeferredprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3613 "View in source") [&#x24C9;][1]

*(Number)*: The number of deferred cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypeelapsed"></a>`Benchmark.Deferred.prototype.elapsed`
<a href="#benchmarkdeferredprototypeelapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3621 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the deferred benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototyperesolve"></a>`Benchmark.Deferred.prototype.resolve`
<a href="#benchmarkdeferredprototyperesolve">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1188 "View in source") [&#x24C9;][1]

*(Unknown)*: Handles cycling/completing the deferred benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypetimestamp"></a>`Benchmark.Deferred.prototype.timeStamp`
<a href="#benchmarkdeferredprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3629 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the deferred benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event`

<!-- div -->

### <a id="benchmarkeventtype"></a>`Benchmark.Event(type)`
<a href="#benchmarkeventtype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L461 "View in source") [&#x24C9;][1]

The Event constructor.

#### Arguments
1. `type` *(String|Object)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`

<!-- div -->

### <a id="benchmarkeventprototypeaborted"></a>`Benchmark.Event.prototype.aborted`
<a href="#benchmarkeventprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3645 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the emitters listener iteration is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypecancelled"></a>`Benchmark.Event.prototype.cancelled`
<a href="#benchmarkeventprototypecancelled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3653 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the default action is cancelled.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototyperesult"></a>`Benchmark.Event.prototype.result`
<a href="#benchmarkeventprototyperesult">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3669 "View in source") [&#x24C9;][1]

*(Mixed)*: The return value of the last executed listener.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetimestamp"></a>`Benchmark.Event.prototype.timeStamp`
<a href="#benchmarkeventprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3685 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the event was created *(ms)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetype"></a>`Benchmark.Event.prototype.type`
<a href="#benchmarkeventprototypetype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3693 "View in source") [&#x24C9;][1]

*(String)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`

<!-- div -->

### <a id="benchmarkeventprototypecurrenttarget"></a>`Benchmark.Event.prototype.currentTarget`
<a href="#benchmarkeventprototypecurrenttarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3661 "View in source") [&#x24C9;][1]

*(Object)*: The object whose listeners are currently being processed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`

<!-- div -->

### <a id="benchmarkeventprototypetarget"></a>`Benchmark.Event.prototype.target`
<a href="#benchmarkeventprototypetarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3677 "View in source") [&#x24C9;][1]

*(Object)*: The object to which the event was originally emitted.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite`

<!-- div -->

### <a id="benchmarksuitename--options"></a>`Benchmark.Suite(name [, options={}])`
<a href="#benchmarksuitename--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L507 "View in source") [&#x24C9;][1]

The Suite constructor.

#### Arguments
1. `name` *(String)*: A name to identify the suite.
2. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var suite = new Benchmark.Suite;

// or using a name first
var suite = new Benchmark.Suite('foo');

// or with options
var suite = new Benchmark.Suite('foo', {

  // called when the suite starts running
  'onStart': onStart,

  // called between running benchmarks
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the suite completes running
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`

<!-- div -->

### <a id="benchmarksuiteprototypeaborted"></a>`Benchmark.Suite.prototype.aborted`
<a href="#benchmarksuiteprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3734 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypelength"></a>`Benchmark.Suite.prototype.length`
<a href="#benchmarksuiteprototypelength">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3726 "View in source") [&#x24C9;][1]

*(Number)*: The number of benchmarks in the suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunning"></a>`Benchmark.Suite.prototype.running`
<a href="#benchmarksuiteprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3742 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeabort"></a>`Benchmark.Suite.prototype.abort()`
<a href="#benchmarksuiteprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1902 "View in source") [&#x24C9;][1]

Aborts all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeaddname-fn--options"></a>`Benchmark.Suite.prototype.add(name, fn [, options={}])`
<a href="#benchmarksuiteprototypeaddname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1962 "View in source") [&#x24C9;][1]

Adds a test to the benchmark suite.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
suite.add(fn);

// or using a name first
suite.add('foo', fn);

// or with options
suite.add('foo', fn, {
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or name and options
suite.add('foo', {
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or options only
suite.add({
  'name': 'foo',
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypecloneoptions"></a>`Benchmark.Suite.prototype.clone(options)`
<a href="#benchmarksuiteprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1981 "View in source") [&#x24C9;][1]

Creates a new suite with cloned benchmarks.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypefiltercallback"></a>`Benchmark.Suite.prototype.filter(callback)`
<a href="#benchmarksuiteprototypefiltercallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2004 "View in source") [&#x24C9;][1]

An `Array#filter` like method.

#### Arguments
1. `callback` *(Function|String)*: The function/alias called per iteration.

#### Returns
*(Object)*: A new suite of benchmarks that passed callback filter.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeforeachcallback"></a>`Benchmark.Suite.prototype.forEach(callback)`
<a href="#benchmarksuiteprototypeforeachcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3752 "View in source") [&#x24C9;][1]

An `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Object)*: The suite iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeindexofvalue"></a>`Benchmark.Suite.prototype.indexOf(value)`
<a href="#benchmarksuiteprototypeindexofvalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3761 "View in source") [&#x24C9;][1]

An `Array#indexOf` like method.

#### Arguments
1. `value` *(Mixed)*: The value to search for.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeinvokename--arg1-arg2-"></a>`Benchmark.Suite.prototype.invoke(name [, arg1, arg2, ...])`
<a href="#benchmarksuiteprototypeinvokename--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3771 "View in source") [&#x24C9;][1]

Invokes a method on all benchmarks in the suite.

#### Arguments
1. `name` *(String|Object)*: The name of the method to invoke OR options object.
2. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypejoinseparator-"></a>`Benchmark.Suite.prototype.join([separator=','])`
<a href="#benchmarksuiteprototypejoinseparator-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3780 "View in source") [&#x24C9;][1]

Converts the suite of benchmarks to a string.

#### Arguments
1. `[separator=',']` *(String)*: A string to separate each element of the array.

#### Returns
*(String)*: The string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypemapcallback"></a>`Benchmark.Suite.prototype.map(callback)`
<a href="#benchmarksuiteprototypemapcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3789 "View in source") [&#x24C9;][1]

An `Array#map` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepluckproperty"></a>`Benchmark.Suite.prototype.pluck(property)`
<a href="#benchmarksuiteprototypepluckproperty">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3798 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all benchmarks in the suite.

#### Arguments
1. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepop"></a>`Benchmark.Suite.prototype.pop()`
<a href="#benchmarksuiteprototypepop">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3806 "View in source") [&#x24C9;][1]

Removes the last benchmark from the suite and returns it.

#### Returns
*(Mixed)*: The removed benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepush"></a>`Benchmark.Suite.prototype.push()`
<a href="#benchmarksuiteprototypepush">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3814 "View in source") [&#x24C9;][1]

Appends benchmarks to the suite.

#### Returns
*(Number)*: The suite's new length.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereducecallback-accumulator"></a>`Benchmark.Suite.prototype.reduce(callback, accumulator)`
<a href="#benchmarksuiteprototypereducecallback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3833 "View in source") [&#x24C9;][1]

An `Array#reduce` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.
2. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereset"></a>`Benchmark.Suite.prototype.reset()`
<a href="#benchmarksuiteprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2019 "View in source") [&#x24C9;][1]

Resets all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereverse"></a>`Benchmark.Suite.prototype.reverse()`
<a href="#benchmarksuiteprototypereverse">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L638 "View in source") [&#x24C9;][1]

Rearrange the host array's elements in reverse order.

#### Returns
*(Array)*: The reversed array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunoptions"></a>`Benchmark.Suite.prototype.run([options={}])`
<a href="#benchmarksuiteprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2056 "View in source") [&#x24C9;][1]

Runs the suite.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The suite instance.

#### Example
~~~ js
// basic usage
suite.run();

// or with options
suite.run({ 'async': true, 'queued': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeshift"></a>`Benchmark.Suite.prototype.shift()`
<a href="#benchmarksuiteprototypeshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L671 "View in source") [&#x24C9;][1]

Removes the first element of the host array and returns it.

#### Returns
*(Mixed)*: The first element of the array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeslicestart-end"></a>`Benchmark.Suite.prototype.slice(start, end)`
<a href="#benchmarksuiteprototypeslicestart-end">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L684 "View in source") [&#x24C9;][1]

Creates an array of the host array's elements from the start index up to, but not including, the end index.

#### Arguments
1. `start` *(Number)*: The starting index.
2. `end` *(Number)*: The end index.

#### Returns
*(Array)*: The new array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesortcomparefnnull"></a>`Benchmark.Suite.prototype.sort([compareFn=null])`
<a href="#benchmarksuiteprototypesortcomparefnnull">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3823 "View in source") [&#x24C9;][1]

Sorts the benchmarks of the suite.

#### Arguments
1. `[compareFn=null]` *(Function)*: A function that defines the sort order.

#### Returns
*(Object)*: The sorted suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesplicestart-deletecount--val1-val2-"></a>`Benchmark.Suite.prototype.splice(start, deleteCount [, val1, val2, ...])`
<a href="#benchmarksuiteprototypesplicestart-deletecount--val1-val2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L714 "View in source") [&#x24C9;][1]

Allows removing a range of elements and/or inserting elements into the host array.

#### Arguments
1. `start` *(Number)*: The start index.
2. `deleteCount` *(Number)*: The number of elements to delete.
3. `[val1, val2, ...]` *(Mixed)*: values to insert at the `start` index.

#### Returns
*(Array)*: An array of removed elements.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeunshift"></a>`Benchmark.Suite.prototype.unshift()`
<a href="#benchmarksuiteprototypeunshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L749 "View in source") [&#x24C9;][1]

Appends arguments to the host array.

#### Returns
*(Number)*: The new length.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`

<!-- div -->

### <a id="benchmarksuiteoptions"></a>`Benchmark.Suite.options`
<a href="#benchmarksuiteoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3705 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by suite instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteoptionsname"></a>`Benchmark.Suite.options.name`
<a href="#benchmarksuiteoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3713 "View in source") [&#x24C9;][1]

*(String)*: The name of the suite.

* * *

<!-- /div -->


<!-- /div -->


<!-- /div -->


  [1]: #Benchmark "Jump back to the TOC."# JSON 3 #

![JSON 3 Logo](http://bestiejs.github.io/json3/page/logo.png)

**JSON 3** is a modern JSON implementation compatible with a variety of JavaScript platforms, including Internet Explorer 6, Opera 7, Safari 2, and Netscape 6. The current version is **3.2.6**.

- [Development Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.js) *(40 KB; uncompressed with comments)*
- [Production Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.min.js) *(3.3 KB; compressed and `gzip`-ped)*

CDN copies are also available at [cdnjs](http://cdnjs.com/libraries/json3/) & [jsDelivr](http://www.jsdelivr.com/#!json3).

[JSON](http://json.org/) is a language-independent data interchange format based on a loose subset of the JavaScript grammar. Originally popularized by [Douglas Crockford](http://www.crockford.com/), the format was standardized in the [fifth edition](http://es5.github.com/) of the ECMAScript specification. The 5.1 edition, ratified in June 2011, incorporates several modifications to the grammar pertaining to the serialization of dates.

JSON 3 exposes two functions: `stringify()` for [serializing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/stringify) a JavaScript value to JSON, and `parse()` for [producing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/parse) a JavaScript value from a JSON source string. It is a **drop-in replacement** for [JSON 2](http://json.org/js). The functions behave exactly as described in the ECMAScript spec, **except** for the date serialization discrepancy noted below.

The JSON 3 parser does **not** use `eval` or regular expressions. This provides security and performance benefits in obsolete and mobile environments, where the margin is particularly significant. The complete [benchmark suite](http://jsperf.com/json3) is available on [jsPerf](http://jsperf.com/).

The project is [hosted on GitHub](http://git.io/json3), along with the [unit tests](http://bestiejs.github.io/json3/test/test_browser.html). It is part of the [BestieJS](https://github.com/bestiejs) family, a collection of best-in-class JavaScript libraries that promote cross-platform support, specification precedents, unit testing, and plenty of documentation.

# Changes from JSON 2 #

JSON 3...

* Correctly serializes primitive wrapper objects.
* Throws a `TypeError` when serializing cyclic structures (JSON 2 recurses until the call stack overflows).
* Utilizes **feature tests** to detect broken or incomplete *native* JSON implementations (JSON 2 only checks for the presence of the native functions). The tests are only executed once at runtime, so there is no additional performance cost when parsing or serializing values.

**As of v3.2.3**, JSON 3 is compatible with [Prototype](http://prototypejs.org) 1.6.1 and older.

In contrast to JSON 2, JSON 3 **does not**...

* Add `toJSON()` methods to the `Boolean`, `Number`, and `String` prototypes. These are not part of any standard, and are made redundant by the design of the `stringify()` implementation.
* Add `toJSON()` or `toISOString()` methods to `Date.prototype`. See the note about date serialization below.

## Date Serialization

**JSON 3 deviates from the specification in one important way**: it does not define `Date#toISOString()` or `Date#toJSON()`. This preserves CommonJS compatibility and avoids polluting native prototypes. Instead, date serialization is performed internally by the `stringify()` implementation: if a date object does not define a custom `toJSON()` method, it is serialized as a [simplified ISO 8601 date-time string](http://es5.github.com/#x15.9.1.15).

**Several native `Date#toJSON()` implementations produce date time strings that do *not* conform to the grammar outlined in the spec**. For instance, all versions of Safari 4, as well as JSON 2, fail to serialize extended years correctly. Furthermore, JSON 2 and older implementations omit the milliseconds from the date-time string (optional in ES 5, but required in 5.1). Finally, in all versions of Safari 4 and 5, serializing an invalid date will produce the string `"Invalid Date"`, rather than `null`. Because these environments exhibit other serialization bugs, however, JSON 3 will override the native `stringify()` implementation.

Portions of the date serialization code are adapted from the [`date-shim`](https://github.com/Yaffle/date-shim) project.

# Usage #

## Web Browsers

    <script src="http://bestiejs.github.io/json3/lib/json3.js"></script>
    <script>
      JSON.stringify({"Hello": 123});
      // => '{"Hello":123}'
      JSON.parse("[[1, 2, 3], 1, 2, 3, 4]", function (key, value) {
        if (typeof value == "number") {
          value = value % 2 ? "Odd" : "Even";
        }
        return value;
      });
      // => [["Odd", "Even", "Odd"], "Odd", "Even", "Odd", "Even"]
    </script>

## CommonJS Environments

    var JSON3 = require("./path/to/json3");
    JSON3.parse("[1, 2, 3]");
    // => [1, 2, 3]

## JavaScript Engines

    load("path/to/json3.js");
    JSON.stringify({"Hello": 123, "Good-bye": 456}, ["Hello"], "\t");
    // => '{\n\t"Hello": 123\n}'

# Compatibility #

JSON 3 has been **tested** with the following web browsers, CommonJS environments, and JavaScript engines.

## Web Browsers

- Windows [Internet Explorer](http://www.microsoft.com/windows/internet-explorer), version 6.0 and higher
- Mozilla [Firefox](http://www.mozilla.com/firefox), version 1.0 and higher
- Apple [Safari](http://www.apple.com/safari), version 2.0 and higher
- [Opera](http://www.opera.com) 7.02 and higher
- [Mozilla](http://sillydog.org/narchive/gecko.php) 1.0, [Netscape](http://sillydog.org/narchive/) 6.2.3, and [SeaMonkey](http://www.seamonkey-project.org/) 1.0 and higher

## CommonJS Environments

- [Node](http://nodejs.org/) 0.2.6 and higher
- [RingoJS](http://ringojs.org/) 0.4 and higher
- [Narwhal](http://narwhaljs.org/) 0.3.2 and higher

## JavaScript Engines

- Mozilla [Rhino](http://www.mozilla.org/rhino) 1.5R5 and higher
- WebKit [JSC](https://trac.webkit.org/wiki/JSC)
- Google [V8](http://code.google.com/p/v8)

## Known Incompatibilities

* Attempting to serialize the `arguments` object may produce inconsistent results across environments due to specification version differences. As a workaround, please convert the `arguments` object to an array first: `JSON.stringify([].slice.call(arguments, 0))`.

## Required Native Methods

JSON 3 assumes that the following methods exist and function as described in the ECMAScript specification:

- The `Number`, `String`, `Array`, `Object`, `Date`, `SyntaxError`, and `TypeError` constructors.
- `String.fromCharCode`
- `Object#toString`
- `Function#call`
- `Math.floor`
- `Number#toString`
- `Date#valueOf`
- `String.prototype`: `indexOf`, `charCodeAt`, `charAt`, `slice`.
- `Array.prototype`: `push`, `pop`, `join`.

# Contribute #

Check out a working copy of the JSON 3 source code with [Git](http://git-scm.com/):

    $ git clone git://github.com/bestiejs/json3.git
    $ cd json3
    $ git submodule update --init

If you'd like to contribute a feature or bug fix, you can [fork](http://help.github.com/fork-a-repo/) JSON 3, commit your changes, and [send a pull request](http://help.github.com/send-pull-requests/). Please make sure to update the unit tests in the `test` directory as well.

Alternatively, you can use the [GitHub issue tracker](https://github.com/bestiejs/json3/issues) to submit bug reports, feature requests, and questions, or send tweets to [@kitcambridge](http://twitter.com/kitcambridge).

JSON 3 is released under the [MIT License](http://kit.mit-license.org/).
# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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
# Benchmark.js <sup>v1.0.0</sup>

A [robust](http://calendar.perfplanet.com/2010/bulletproof-javascript-benchmarks/ "Bulletproof JavaScript benchmarks") benchmarking library that works on nearly all JavaScript platforms<sup><a name="fnref1" href="#fn1">1</a></sup>, supports high-resolution timers, and returns statistically significant results. As seen on [jsPerf](http://jsperf.com/).

## BestieJS

Benchmark.js is part of the BestieJS *"Best in Class"* module collection. This means we promote solid browser/environment support, ES5 precedents, unit testing, and plenty of documentation.

## Documentation

The documentation for Benchmark.js can be viewed here: <http://benchmarkjs.com/docs>

For a list of upcoming features, check out our [roadmap](https://github.com/bestiejs/benchmark.js/wiki/Roadmap).

## Support

Benchmark.js has been tested in at least Adobe AIR 3.1, Chrome 5-21, Firefox 1.5-13, IE 6-9, Opera 9.25-12.01, Safari 3-6, Node.js 0.8.6, Narwhal 0.3.2, RingoJS 0.8, and Rhino 1.7RC5.

## Installation and usage

In a browser or Adobe AIR:

~~~ html
<script src="benchmark.js"></script>
~~~

Optionally, expose Java’s nanosecond timer by adding the `nano` applet to the `<body>`:

~~~ html
<applet code="nano" archive="nano.jar"></applet>
~~~

Or enable Chrome’s microsecond timer by using the [command line switch](http://peter.sh/experiments/chromium-command-line-switches/#enable-benchmarking):

    --enable-benchmarking

Via [npm](http://npmjs.org/):

~~~ bash
npm install benchmark
~~~

In [Node.js](http://nodejs.org/) and [RingoJS v0.8.0+](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark');
~~~

Optionally, use the [microtime module](https://github.com/wadey/node-microtime) by Wade Simmons:

~~~ bash
npm install microtime
~~~

In [RingoJS v0.7.0-](http://ringojs.org/):

~~~ js
var Benchmark = require('benchmark').Benchmark;
~~~

In [Rhino](http://www.mozilla.org/rhino/):

~~~ js
load('benchmark.js');
~~~

In an AMD loader like [RequireJS](http://requirejs.org/):

~~~ js
require({
  'paths': {
    'benchmark': 'path/to/benchmark'
  }
},
['benchmark'], function(Benchmark) {
  console.log(Benchmark.version);
});

// or with platform.js
// https://github.com/bestiejs/platform.js
require({
  'paths': {
    'benchmark': 'path/to/benchmark',
    'platform': 'path/to/platform'
  }
},
['benchmark', 'platform'], function(Benchmark, platform) {
  Benchmark.platform = platform;
  console.log(Benchmark.platform.name);
});
~~~

Usage example:

~~~ js
var suite = new Benchmark.Suite;

// add tests
suite.add('RegExp#test', function() {
  /o/.test('Hello World!');
})
.add('String#indexOf', function() {
  'Hello World!'.indexOf('o') > -1;
})
// add listeners
.on('cycle', function(event) {
  console.log(String(event.target));
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
// run async
.run({ 'async': true });

// logs:
// > RegExp#test x 4,161,532 +-0.99% (59 cycles)
// > String#indexOf x 6,139,623 +-1.00% (131 cycles)
// > Fastest is String#indexOf
~~~

## Authors

* [Mathias Bynens](http://mathiasbynens.be/)
  [![twitter/mathias](http://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter")
* [John-David Dalton](http://allyoucanleet.com/)
  [![twitter/jdalton](http://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter")

## Contributors

* [Kit Cambridge](http://kitcambridge.github.com/)
  [![twitter/kitcambridge](http://gravatar.com/avatar/6662a1d02f351b5ef2f8b4d815804661?s=70)](https://twitter.com/kitcambridge "Follow @kitcambridge on Twitter")
# Benchmark.js <sup>v1.0.0</sup>

<!-- div -->


<!-- div -->

## <a id="Benchmark"></a>`Benchmark`
* [`Benchmark`](#benchmarkname-fn--options)
* [`Benchmark.version`](#benchmarkversion)
* [`Benchmark.deepClone`](#benchmarkdeepclonevalue)
* [`Benchmark.each`](#benchmarkeachobject-callback-thisarg)
* [`Benchmark.extend`](#benchmarkextenddestination--source)
* [`Benchmark.filter`](#benchmarkfilterarray-callback-thisarg)
* [`Benchmark.forEach`](#benchmarkforeacharray-callback-thisarg)
* [`Benchmark.formatNumber`](#benchmarkformatnumbernumber)
* [`Benchmark.forOwn`](#benchmarkforownobject-callback-thisarg)
* [`Benchmark.hasKey`](#benchmarkhaskeyobject-key)
* [`Benchmark.indexOf`](#benchmarkindexofarray-value--fromindex0)
* [`Benchmark.interpolate`](#benchmarkinterpolatestring-object)
* [`Benchmark.invoke`](#benchmarkinvokebenches-name--arg1-arg2-)
* [`Benchmark.join`](#benchmarkjoinobject--separator1--separator2:)
* [`Benchmark.map`](#benchmarkmaparray-callback-thisarg)
* [`Benchmark.pluck`](#benchmarkpluckarray-property)
* [`Benchmark.reduce`](#benchmarkreducearray-callback-accumulator)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype`
* [`Benchmark.prototype.aborted`](#benchmarkprototypeaborted)
* [`Benchmark.prototype.compiled`](#benchmarkprototypecompiled)
* [`Benchmark.prototype.count`](#benchmarkprototypecount)
* [`Benchmark.prototype.cycles`](#benchmarkprototypecycles)
* [`Benchmark.prototype.fn`](#benchmarkprototypefn)
* [`Benchmark.prototype.hz`](#benchmarkprototypehz)
* [`Benchmark.prototype.running`](#benchmarkprototyperunning)
* [`Benchmark.prototype.setup`](#benchmarkprototypesetup)
* [`Benchmark.prototype.teardown`](#benchmarkprototypeteardown)
* [`Benchmark.prototype.abort`](#benchmarkprototypeabort)
* [`Benchmark.prototype.clone`](#benchmarkprototypecloneoptions)
* [`Benchmark.prototype.compare`](#benchmarkprototypecompareother)
* [`Benchmark.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.prototype.reset`](#benchmarkprototypereset)
* [`Benchmark.prototype.run`](#benchmarkprototyperunoptions)
* [`Benchmark.prototype.toString`](#benchmarkprototypetostring)

<!-- /div -->


<!-- div -->

## `Benchmark.options`
* [`Benchmark.options`](#benchmarkoptions)
* [`Benchmark.options.async`](#benchmarkoptionsasync)
* [`Benchmark.options.defer`](#benchmarkoptionsdefer)
* [`Benchmark.options.delay`](#benchmarkoptionsdelay)
* [`Benchmark.options.id`](#benchmarkoptionsid)
* [`Benchmark.options.initCount`](#benchmarkoptionsinitcount)
* [`Benchmark.options.maxTime`](#benchmarkoptionsmaxtime)
* [`Benchmark.options.minSamples`](#benchmarkoptionsminsamples)
* [`Benchmark.options.minTime`](#benchmarkoptionsmintime)
* [`Benchmark.options.name`](#benchmarkoptionsname)
* [`Benchmark.options.onAbort`](#benchmarkoptionsonabort)
* [`Benchmark.options.onComplete`](#benchmarkoptionsoncomplete)
* [`Benchmark.options.onCycle`](#benchmarkoptionsoncycle)
* [`Benchmark.options.onError`](#benchmarkoptionsonerror)
* [`Benchmark.options.onReset`](#benchmarkoptionsonreset)
* [`Benchmark.options.onStart`](#benchmarkoptionsonstart)

<!-- /div -->


<!-- div -->

## `Benchmark.platform`
* [`Benchmark.platform`](#benchmarkplatform)
* [`Benchmark.platform.description`](#benchmarkplatformdescription)
* [`Benchmark.platform.layout`](#benchmarkplatformlayout)
* [`Benchmark.platform.manufacturer`](#benchmarkplatformmanufacturer)
* [`Benchmark.platform.name`](#benchmarkplatformname)
* [`Benchmark.platform.os`](#benchmarkplatformos)
* [`Benchmark.platform.prerelease`](#benchmarkplatformprerelease)
* [`Benchmark.platform.product`](#benchmarkplatformproduct)
* [`Benchmark.platform.version`](#benchmarkplatformversion)
* [`Benchmark.platform.toString`](#benchmarkplatformtostring)

<!-- /div -->


<!-- div -->

## `Benchmark.support`
* [`Benchmark.support`](#benchmarksupport)
* [`Benchmark.support.air`](#benchmarksupportair)
* [`Benchmark.support.argumentsClass`](#benchmarksupportargumentsclass)
* [`Benchmark.support.browser`](#benchmarksupportbrowser)
* [`Benchmark.support.charByIndex`](#benchmarksupportcharbyindex)
* [`Benchmark.support.charByOwnIndex`](#benchmarksupportcharbyownindex)
* [`Benchmark.support.decompilation`](#benchmarksupportdecompilation)
* [`Benchmark.support.descriptors`](#benchmarksupportdescriptors)
* [`Benchmark.support.getAllKeys`](#benchmarksupportgetallkeys)
* [`Benchmark.support.iteratesOwnLast`](#benchmarksupportiteratesownfirst)
* [`Benchmark.support.java`](#benchmarksupportjava)
* [`Benchmark.support.nodeClass`](#benchmarksupportnodeclass)
* [`Benchmark.support.timeout`](#benchmarksupporttimeout)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`
* [`Benchmark.prototype.error`](#benchmarkprototypeerror)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`
* [`Benchmark.prototype.stats`](#benchmarkprototypestats)
* [`Benchmark.prototype.stats.deviation`](#benchmark-statsdeviation)
* [`Benchmark.prototype.stats.mean`](#benchmark-statsmean)
* [`Benchmark.prototype.stats.moe`](#benchmark-statsmoe)
* [`Benchmark.prototype.stats.rme`](#benchmark-statsrme)
* [`Benchmark.prototype.stats.sample`](#benchmark-statssample)
* [`Benchmark.prototype.stats.sem`](#benchmark-statssem)
* [`Benchmark.prototype.stats.variance`](#benchmark-statsvariance)

<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`
* [`Benchmark.prototype.times`](#benchmarkprototypetimes)
* [`Benchmark.prototype.times.cycle`](#benchmark-timescycle)
* [`Benchmark.prototype.times.elapsed`](#benchmark-timeselapsed)
* [`Benchmark.prototype.times.period`](#benchmark-timesperiod)
* [`Benchmark.prototype.times.timeStamp`](#benchmark-timestimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`
* [`Benchmark.Deferred`](#benchmarkdeferredclone)

<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`
* [`Benchmark.Deferred.prototype.benchmark`](#benchmarkdeferredprototypebenchmark)
* [`Benchmark.Deferred.prototype.cycles`](#benchmarkdeferredprototypecycles)
* [`Benchmark.Deferred.prototype.elapsed`](#benchmarkdeferredprototypeelapsed)
* [`Benchmark.Deferred.prototype.resolve`](#benchmarkdeferredprototyperesolve)
* [`Benchmark.Deferred.prototype.timeStamp`](#benchmarkdeferredprototypetimestamp)

<!-- /div -->


<!-- div -->

## `Benchmark.Event`
* [`Benchmark.Event`](#benchmarkeventtype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`
* [`Benchmark.Event.prototype.aborted`](#benchmarkeventprototypeaborted)
* [`Benchmark.Event.prototype.cancelled`](#benchmarkeventprototypecancelled)
* [`Benchmark.Event.prototype.result`](#benchmarkeventprototyperesult)
* [`Benchmark.Event.prototype.timeStamp`](#benchmarkeventprototypetimestamp)
* [`Benchmark.Event.prototype.type`](#benchmarkeventprototypetype)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`
* [`Benchmark.Event.prototype.currentTarget`](#benchmarkeventprototypecurrenttarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`
* [`Benchmark.Event.prototype.target`](#benchmarkeventprototypetarget)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite`
* [`Benchmark.Suite`](#benchmarksuitename--options)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`
* [`Benchmark.Suite.prototype.aborted`](#benchmarksuiteprototypeaborted)
* [`Benchmark.Suite.prototype.length`](#benchmarksuiteprototypelength)
* [`Benchmark.Suite.prototype.running`](#benchmarksuiteprototyperunning)
* [`Benchmark.Suite.prototype.abort`](#benchmarksuiteprototypeabort)
* [`Benchmark.Suite.prototype.add`](#benchmarksuiteprototypeaddname-fn--options)
* [`Benchmark.Suite.prototype.clone`](#benchmarksuiteprototypecloneoptions)
* [`Benchmark.Suite.prototype.emit`](#benchmarkprototypeemittype)
* [`Benchmark.Suite.prototype.filter`](#benchmarksuiteprototypefiltercallback)
* [`Benchmark.Suite.prototype.forEach`](#benchmarksuiteprototypeforeachcallback)
* [`Benchmark.Suite.prototype.indexOf`](#benchmarksuiteprototypeindexofvalue)
* [`Benchmark.Suite.prototype.invoke`](#benchmarksuiteprototypeinvokename--arg1-arg2-)
* [`Benchmark.Suite.prototype.join`](#benchmarksuiteprototypejoinseparator-)
* [`Benchmark.Suite.prototype.listeners`](#benchmarkprototypelistenerstype)
* [`Benchmark.Suite.prototype.map`](#benchmarksuiteprototypemapcallback)
* [`Benchmark.Suite.prototype.off`](#benchmarkprototypeofftype-listener)
* [`Benchmark.Suite.prototype.on`](#benchmarkprototypeontype-listener)
* [`Benchmark.Suite.prototype.pluck`](#benchmarksuiteprototypepluckproperty)
* [`Benchmark.Suite.prototype.pop`](#benchmarksuiteprototypepop)
* [`Benchmark.Suite.prototype.push`](#benchmarksuiteprototypepush)
* [`Benchmark.Suite.prototype.reduce`](#benchmarksuiteprototypereducecallback-accumulator)
* [`Benchmark.Suite.prototype.reset`](#benchmarksuiteprototypereset)
* [`Benchmark.Suite.prototype.reverse`](#benchmarksuiteprototypereverse)
* [`Benchmark.Suite.prototype.run`](#benchmarksuiteprototyperunoptions)
* [`Benchmark.Suite.prototype.shift`](#benchmarksuiteprototypeshift)
* [`Benchmark.Suite.prototype.slice`](#benchmarksuiteprototypeslicestart-end)
* [`Benchmark.Suite.prototype.sort`](#benchmarksuiteprototypesortcomparefnnull)
* [`Benchmark.Suite.prototype.splice`](#benchmarksuiteprototypesplicestart-deletecount--val1-val2-)
* [`Benchmark.Suite.prototype.unshift`](#benchmarksuiteprototypeunshift)

<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`
* [`Benchmark.Suite.options`](#benchmarksuiteoptions)
* [`Benchmark.Suite.options.name`](#benchmarksuiteoptionsname)

<!-- /div -->


<!-- /div -->


<!-- div -->


<!-- div -->

## `Benchmark`

<!-- div -->

### <a id="benchmarkname-fn--options"></a>`Benchmark(name, fn [, options={}])`
<a href="#benchmarkname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L404 "View in source") [&#x24C9;][1]

The Benchmark constructor.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var bench = new Benchmark(fn);

// or using a name first
var bench = new Benchmark('foo', fn);

// or with options
var bench = new Benchmark('foo', fn, {

  // displayed by Benchmark#toString if `name` is not available
  'id': 'xyz',

  // called when the benchmark starts running
  'onStart': onStart,

  // called after each run cycle
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the benchmark completes running
  'onComplete': onComplete,

  // compiled/called before the test loop
  'setup': setup,

  // compiled/called after the test loop
  'teardown': teardown
});

// or name and options
var bench = new Benchmark('foo', {

  // a flag to indicate the benchmark is deferred
  'defer': true,

  // benchmark test function
  'fn': function(deferred) {
    // call resolve() when the deferred test is finished
    deferred.resolve();
  }
});

// or options only
var bench = new Benchmark({

  // benchmark name
  'name': 'foo',

  // benchmark test as a string
  'fn': '[1,2,3,4].sort()'
});

// a test's `this` binding is set to the benchmark instance
var bench = new Benchmark('foo', function() {
  'My name is '.concat(this.name); // My name is foo
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkversion"></a>`Benchmark.version`
<a href="#benchmarkversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3267 "View in source") [&#x24C9;][1]

*(String)*: The semantic version number.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeepclonevalue"></a>`Benchmark.deepClone(value)`
<a href="#benchmarkdeepclonevalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1225 "View in source") [&#x24C9;][1]

A deep clone utility.

#### Arguments
1. `value` *(Mixed)*: The value to clone.

#### Returns
*(Mixed)*: The cloned value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeachobject-callback-thisarg"></a>`Benchmark.each(object, callback, thisArg)`
<a href="#benchmarkeachobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1400 "View in source") [&#x24C9;][1]

An iteration utility for arrays and objects. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Array|Object)*: The object to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array, Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkextenddestination--source"></a>`Benchmark.extend(destination [, source={}])`
<a href="#benchmarkextenddestination--source">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1446 "View in source") [&#x24C9;][1]

Copies enumerable properties from the source(s) object to the destination object.

#### Arguments
1. `destination` *(Object)*: The destination object.
2. `[source={}]` *(Object)*: The source object.

#### Returns
*(Object)*: The destination object.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkfilterarray-callback-thisarg"></a>`Benchmark.filter(array, callback, thisArg)`
<a href="#benchmarkfilterarray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1485 "View in source") [&#x24C9;][1]

A generic `Array#filter` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function|String)*: The function/alias called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values that passed callback filter.

#### Example
~~~ js
// get odd numbers
Benchmark.filter([1, 2, 3, 4, 5], function(n) {
  return n % 2;
}); // -> [1, 3, 5];

// get fastest benchmarks
Benchmark.filter(benches, 'fastest');

// get slowest benchmarks
Benchmark.filter(benches, 'slowest');

// get benchmarks that completed without erroring
Benchmark.filter(benches, 'successful');
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforeacharray-callback-thisarg"></a>`Benchmark.forEach(array, callback, thisArg)`
<a href="#benchmarkforeacharray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1518 "View in source") [&#x24C9;][1]

A generic `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: Returns the array iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkformatnumbernumber"></a>`Benchmark.formatNumber(number)`
<a href="#benchmarkformatnumbernumber">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1557 "View in source") [&#x24C9;][1]

Converts a number to a more readable comma-separated string representation.

#### Arguments
1. `number` *(Number)*: The number to convert.

#### Returns
*(String)*: The more readable string representation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkforownobject-callback-thisarg"></a>`Benchmark.forOwn(object, callback, thisArg)`
<a href="#benchmarkforownobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1545 "View in source") [&#x24C9;][1]

Iterates over an object's own properties, executing the `callback` for each. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `callback` *(Function)*: The function executed per own property.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Object)*: Returns the object iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkhaskeyobject-key"></a>`Benchmark.hasKey(object, key)`
<a href="#benchmarkhaskeyobject-key">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1572 "View in source") [&#x24C9;][1]

Checks if an object has the specified key as a direct property.

#### Arguments
1. `object` *(Object)*: The object to check.
2. `key` *(String)*: The key to check for.

#### Returns
*(Boolean)*: Returns `true` if key is a direct property, else `false`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkindexofarray-value--fromindex0"></a>`Benchmark.indexOf(array, value [, fromIndex=0])`
<a href="#benchmarkindexofarray-value--fromindex0">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1608 "View in source") [&#x24C9;][1]

A generic `Array#indexOf` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `value` *(Mixed)*: The value to search for.
3. `[fromIndex=0]` *(Number)*: The index to start searching from.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinterpolatestring-object"></a>`Benchmark.interpolate(string, object)`
<a href="#benchmarkinterpolatestring-object">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1630 "View in source") [&#x24C9;][1]

Modify a string by replacing named tokens with matching object property values.

#### Arguments
1. `string` *(String)*: The string to modify.
2. `object` *(Object)*: The template object.

#### Returns
*(String)*: The modified string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkinvokebenches-name--arg1-arg2-"></a>`Benchmark.invoke(benches, name [, arg1, arg2, ...])`
<a href="#benchmarkinvokebenches-name--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1677 "View in source") [&#x24C9;][1]

Invokes a method on all items in an array.

#### Arguments
1. `benches` *(Array)*: Array of benchmarks to iterate over.
2. `name` *(String|Object)*: The name of the method to invoke OR options object.
3. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

#### Example
~~~ js
// invoke `reset` on all benchmarks
Benchmark.invoke(benches, 'reset');

// invoke `emit` with arguments
Benchmark.invoke(benches, 'emit', 'complete', listener);

// invoke `run(true)`, treat benchmarks as a queue, and register invoke callbacks
Benchmark.invoke(benches, {

  // invoke the `run` method
  'name': 'run',

  // pass a single argument
  'args': true,

  // treat as queue, removing benchmarks from front of `benches` until empty
  'queued': true,

  // called before any benchmarks have been invoked.
  'onStart': onStart,

  // called between invoking benchmarks
  'onCycle': onCycle,

  // called after all benchmarks have been invoked.
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkjoinobject--separator1--separator2:"></a>`Benchmark.join(object [, separator1=',', separator2=': '])`
<a href="#benchmarkjoinobject--separator1--separator2:">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1831 "View in source") [&#x24C9;][1]

Creates a string of joined array values or object key-value pairs.

#### Arguments
1. `object` *(Array|Object)*: The object to operate on.
2. `[separator1=',']` *(String)*: The separator used between key-value pairs.
3. `[separator2=': ']` *(String)*: The separator used between keys and values.

#### Returns
*(String)*: The joined result.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkmaparray-callback-thisarg"></a>`Benchmark.map(array, callback, thisArg)`
<a href="#benchmarkmaparray-callback-thisarg">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1853 "View in source") [&#x24C9;][1]

A generic `Array#map` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `thisArg` *(Mixed)*: The `this` binding for the callback.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkpluckarray-property"></a>`Benchmark.pluck(array, property)`
<a href="#benchmarkpluckarray-property">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1869 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all items in an array.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkreducearray-callback-accumulator"></a>`Benchmark.reduce(array, callback, accumulator)`
<a href="#benchmarkreducearray-callback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1885 "View in source") [&#x24C9;][1]

A generic `Array#reduce` like method.

#### Arguments
1. `array` *(Array)*: The array to iterate over.
2. `callback` *(Function)*: The function called per iteration.
3. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype`

<!-- div -->

### <a id="benchmarkprototypeaborted"></a>`Benchmark.prototype.aborted`
<a href="#benchmarkprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3377 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompiled"></a>`Benchmark.prototype.compiled`
<a href="#benchmarkprototypecompiled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3353 "View in source") [&#x24C9;][1]

*(Function, String)*: The compiled test function.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecount"></a>`Benchmark.prototype.count`
<a href="#benchmarkprototypecount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3329 "View in source") [&#x24C9;][1]

*(Number)*: The number of times a test was executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecycles"></a>`Benchmark.prototype.cycles`
<a href="#benchmarkprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3337 "View in source") [&#x24C9;][1]

*(Number)*: The number of cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypefn"></a>`Benchmark.prototype.fn`
<a href="#benchmarkprototypefn">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3369 "View in source") [&#x24C9;][1]

*(Function, String)*: The test to benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypehz"></a>`Benchmark.prototype.hz`
<a href="#benchmarkprototypehz">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3345 "View in source") [&#x24C9;][1]

*(Number)*: The number of executions per second.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunning"></a>`Benchmark.prototype.running`
<a href="#benchmarkprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3385 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the benchmark is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypesetup"></a>`Benchmark.prototype.setup`
<a href="#benchmarkprototypesetup">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3448 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **before** the test loop.

#### Example
~~~ js
// basic usage
var bench = Benchmark({
  'setup': function() {
    var c = this.count,
        element = document.getElementById('container');
    while (c--) {
      element.appendChild(document.createElement('div'));
    }
  },
  'fn': function() {
    element.removeChild(element.lastChild);
  }
});

// compiles to something like:
var c = this.count,
    element = document.getElementById('container');
while (c--) {
  element.appendChild(document.createElement('div'));
}
var start = new Date;
while (count--) {
  element.removeChild(element.lastChild);
}
var end = new Date - start;

// or using strings
var bench = Benchmark({
  'setup': '\
    var a = 0;\n\
    (function() {\n\
      (function() {\n\
        (function() {',
  'fn': 'a += 1;',
  'teardown': '\
         }())\n\
       }())\n\
     }())'
});

// compiles to something like:
var a = 0;
(function() {
  (function() {
    (function() {
      var start = new Date;
      while (count--) {
        a += 1;
      }
      var end = new Date - start;
    }())
  }())
}())
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeteardown"></a>`Benchmark.prototype.teardown`
<a href="#benchmarkprototypeteardown">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3456 "View in source") [&#x24C9;][1]

*(Function, String)*: Compiled into the test and executed immediately **after** the test loop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeabort"></a>`Benchmark.prototype.abort()`
<a href="#benchmarkprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2218 "View in source") [&#x24C9;][1]

Aborts the benchmark without recording times.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecloneoptions"></a>`Benchmark.prototype.clone(options)`
<a href="#benchmarkprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2257 "View in source") [&#x24C9;][1]

Creates a new benchmark using the same test and options.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new benchmark instance.

#### Example
~~~ js
var bizarro = bench.clone({
  'name': 'doppelganger'
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypecompareother"></a>`Benchmark.prototype.compare(other)`
<a href="#benchmarkprototypecompareother">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2280 "View in source") [&#x24C9;][1]

Determines if a benchmark is faster than another.

#### Arguments
1. `other` *(Object)*: The benchmark to compare.

#### Returns
*(Number)*: Returns `-1` if slower, `1` if faster, and `0` if indeterminate.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypereset"></a>`Benchmark.prototype.reset()`
<a href="#benchmarkprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2334 "View in source") [&#x24C9;][1]

Reset properties and abort if running.

#### Returns
*(Object)*: The benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototyperunoptions"></a>`Benchmark.prototype.run([options={}])`
<a href="#benchmarkprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3000 "View in source") [&#x24C9;][1]

Runs the benchmark.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
bench.run();

// or with options
bench.run({ 'async': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypetostring"></a>`Benchmark.prototype.toString()`
<a href="#benchmarkprototypetostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2405 "View in source") [&#x24C9;][1]

Displays relevant benchmark information when coerced to a string.

#### Returns
*(String)*: A string representation of the benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.options`

<!-- div -->

### <a id="benchmarkoptions"></a>`Benchmark.options`
<a href="#benchmarkoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3049 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by benchmark instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsasync"></a>`Benchmark.options.async`
<a href="#benchmarkoptionsasync">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3058 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that benchmark cycles will execute asynchronously by default.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdefer"></a>`Benchmark.options.defer`
<a href="#benchmarkoptionsdefer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3066 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate that the benchmark clock is deferred.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsdelay"></a>`Benchmark.options.delay`
<a href="#benchmarkoptionsdelay">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3073 "View in source") [&#x24C9;][1]

*(Number)*: The delay between test cycles *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsid"></a>`Benchmark.options.id`
<a href="#benchmarkoptionsid">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3082 "View in source") [&#x24C9;][1]

*(String)*: Displayed by Benchmark#toString when a `name` is not available *(auto-generated if absent)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsinitcount"></a>`Benchmark.options.initCount`
<a href="#benchmarkoptionsinitcount">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3090 "View in source") [&#x24C9;][1]

*(Number)*: The default number of times to execute a test on a benchmark's first cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmaxtime"></a>`Benchmark.options.maxTime`
<a href="#benchmarkoptionsmaxtime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3099 "View in source") [&#x24C9;][1]

*(Number)*: The maximum time a benchmark is allowed to run before finishing *(secs)*. Note: Cycle delays aren't counted toward the maximum time.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsminsamples"></a>`Benchmark.options.minSamples`
<a href="#benchmarkoptionsminsamples">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3107 "View in source") [&#x24C9;][1]

*(Number)*: The minimum sample size required to perform statistical analysis.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsmintime"></a>`Benchmark.options.minTime`
<a href="#benchmarkoptionsmintime">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3115 "View in source") [&#x24C9;][1]

*(Number)*: The time needed to reduce the percent uncertainty of measurement to `1`% *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsname"></a>`Benchmark.options.name`
<a href="#benchmarkoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3123 "View in source") [&#x24C9;][1]

*(String)*: The name of the benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonabort"></a>`Benchmark.options.onAbort`
<a href="#benchmarkoptionsonabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3131 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncomplete"></a>`Benchmark.options.onComplete`
<a href="#benchmarkoptionsoncomplete">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3139 "View in source") [&#x24C9;][1]

An event listener called when the benchmark completes running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsoncycle"></a>`Benchmark.options.onCycle`
<a href="#benchmarkoptionsoncycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3147 "View in source") [&#x24C9;][1]

An event listener called after each run cycle.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonerror"></a>`Benchmark.options.onError`
<a href="#benchmarkoptionsonerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3155 "View in source") [&#x24C9;][1]

An event listener called when a test errors.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonreset"></a>`Benchmark.options.onReset`
<a href="#benchmarkoptionsonreset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3163 "View in source") [&#x24C9;][1]

An event listener called when the benchmark is reset.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkoptionsonstart"></a>`Benchmark.options.onStart`
<a href="#benchmarkoptionsonstart">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3171 "View in source") [&#x24C9;][1]

An event listener called when the benchmark starts running.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.platform`

<!-- div -->

### <a id="benchmarkplatform"></a>`Benchmark.platform`
<a href="#benchmarkplatform">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3182 "View in source") [&#x24C9;][1]

*(Object)*: Platform object with properties describing things like browser name, version, and operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformdescription"></a>`Benchmark.platform.description`
<a href="#benchmarkplatformdescription">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3190 "View in source") [&#x24C9;][1]

*(String)*: The platform description.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformlayout"></a>`Benchmark.platform.layout`
<a href="#benchmarkplatformlayout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3198 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser layout engine.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformmanufacturer"></a>`Benchmark.platform.manufacturer`
<a href="#benchmarkplatformmanufacturer">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3222 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product's manufacturer.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformname"></a>`Benchmark.platform.name`
<a href="#benchmarkplatformname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3214 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the browser/environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformos"></a>`Benchmark.platform.os`
<a href="#benchmarkplatformos">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3230 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the operating system.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformprerelease"></a>`Benchmark.platform.prerelease`
<a href="#benchmarkplatformprerelease">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3238 "View in source") [&#x24C9;][1]

*(String, Null)*: The alpha/beta release indicator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformproduct"></a>`Benchmark.platform.product`
<a href="#benchmarkplatformproduct">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3206 "View in source") [&#x24C9;][1]

*(String, Null)*: The name of the product hosting the browser.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformversion"></a>`Benchmark.platform.version`
<a href="#benchmarkplatformversion">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3246 "View in source") [&#x24C9;][1]

*(String, Null)*: The browser/environment version.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkplatformtostring"></a>`Benchmark.platform.toString()`
<a href="#benchmarkplatformtostring">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3255 "View in source") [&#x24C9;][1]

Return platform description when the platform object is coerced to a string.

#### Returns
*(String)*: The platform description.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.support`

<!-- div -->

### <a id="benchmarksupport"></a>`Benchmark.support`
<a href="#benchmarksupport">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L135 "View in source") [&#x24C9;][1]

*(Object)*: An object used to flag environments/features.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportair"></a>`Benchmark.support.air`
<a href="#benchmarksupportair">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L145 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect Adobe AIR.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportargumentsclass"></a>`Benchmark.support.argumentsClass`
<a href="#benchmarksupportargumentsclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L153 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if `arguments` objects have the correct internal [[Class]] value.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportbrowser"></a>`Benchmark.support.browser`
<a href="#benchmarksupportbrowser">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L161 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if in a browser environment.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyindex"></a>`Benchmark.support.charByIndex`
<a href="#benchmarksupportcharbyindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L169 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings support accessing characters by index.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportcharbyownindex"></a>`Benchmark.support.charByOwnIndex`
<a href="#benchmarksupportcharbyownindex">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L179 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if strings have indexes as own properties.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdecompilation"></a>`Benchmark.support.decompilation`
<a href="#benchmarksupportdecompilation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L207 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if functions support decompilation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportdescriptors"></a>`Benchmark.support.descriptors`
<a href="#benchmarksupportdescriptors">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L228 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ property descriptor API.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportgetallkeys"></a>`Benchmark.support.getAllKeys`
<a href="#benchmarksupportgetallkeys">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L242 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect ES5+ Object.getOwnPropertyNames().

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportiteratesownfirst"></a>`Benchmark.support.iteratesOwnFirst`
<a href="#benchmarksupportiteratesownfirst">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L255 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if own properties are iterated before inherited properties *(all but IE < `9`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportjava"></a>`Benchmark.support.java`
<a href="#benchmarksupportjava">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L190 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if Java is enabled/exposed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupportnodeclass"></a>`Benchmark.support.nodeClass`
<a href="#benchmarksupportnodeclass">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L272 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if a node's [[Class]] is resolvable *(all but IE < `9`)* and that the JS engine errors when attempting to coerce an object to a string without a `toString` property value of `typeof` "function".

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksupporttimeout"></a>`Benchmark.support.timeout`
<a href="#benchmarksupporttimeout">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L198 "View in source") [&#x24C9;][1]

*(Boolean)*: Detect if the Timers API exists.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.error`

<!-- div -->

### <a id="benchmarkprototypeerror"></a>`Benchmark.prototype.error`
<a href="#benchmarkprototypeerror">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3361 "View in source") [&#x24C9;][1]

*(Object)*: The error object if the test failed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.stats`

<!-- div -->

### <a id="benchmarkprototypestats"></a>`Benchmark.prototype.stats`
<a href="#benchmarkprototypestats">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3464 "View in source") [&#x24C9;][1]

*(Object)*: An object of stats including mean, margin or error, and standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsdeviation"></a>`Benchmark.prototype.stats.deviation`
<a href="#benchmark-statsdeviation">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3496 "View in source") [&#x24C9;][1]

*(Number)*: The sample standard deviation.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmean"></a>`Benchmark.prototype.stats.mean`
<a href="#benchmark-statsmean">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3504 "View in source") [&#x24C9;][1]

*(Number)*: The sample arithmetic mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsmoe"></a>`Benchmark.prototype.stats.moe`
<a href="#benchmark-statsmoe">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3472 "View in source") [&#x24C9;][1]

*(Number)*: The margin of error.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsrme"></a>`Benchmark.prototype.stats.rme`
<a href="#benchmark-statsrme">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3480 "View in source") [&#x24C9;][1]

*(Number)*: The relative margin of error *(expressed as a percentage of the mean)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssample"></a>`Benchmark.prototype.stats.sample`
<a href="#benchmark-statssample">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3512 "View in source") [&#x24C9;][1]

*(Array)*: The array of sampled periods.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statssem"></a>`Benchmark.prototype.stats.sem`
<a href="#benchmark-statssem">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3488 "View in source") [&#x24C9;][1]

*(Number)*: The standard error of the mean.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-statsvariance"></a>`Benchmark.prototype.stats.variance`
<a href="#benchmark-statsvariance">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3520 "View in source") [&#x24C9;][1]

*(Number)*: The sample variance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.prototype.times`

<!-- div -->

### <a id="benchmarkprototypetimes"></a>`Benchmark.prototype.times`
<a href="#benchmarkprototypetimes">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3529 "View in source") [&#x24C9;][1]

*(Object)*: An object of timing data including cycle, elapsed, period, start, and stop.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timescycle"></a>`Benchmark.prototype.times.cycle`
<a href="#benchmark-timescycle">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3537 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the last cycle *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timeselapsed"></a>`Benchmark.prototype.times.elapsed`
<a href="#benchmark-timeselapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3545 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timesperiod"></a>`Benchmark.prototype.times.period`
<a href="#benchmark-timesperiod">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3553 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to execute the test once *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmark-timestimestamp"></a>`Benchmark.prototype.times.timeStamp`
<a href="#benchmark-timestimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3561 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred`

<!-- div -->

### <a id="benchmarkdeferredclone"></a>`Benchmark.Deferred(clone)`
<a href="#benchmarkdeferredclone">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L445 "View in source") [&#x24C9;][1]

The Deferred constructor.

#### Arguments
1. `clone` *(Object)*: The cloned benchmark instance.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Deferred.prototype`

<!-- div -->

### <a id="benchmarkdeferredprototypebenchmark"></a>`Benchmark.Deferred.prototype.benchmark`
<a href="#benchmarkdeferredprototypebenchmark">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3605 "View in source") [&#x24C9;][1]

*(Object)*: The deferred benchmark instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypecycles"></a>`Benchmark.Deferred.prototype.cycles`
<a href="#benchmarkdeferredprototypecycles">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3613 "View in source") [&#x24C9;][1]

*(Number)*: The number of deferred cycles performed while benchmarking.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypeelapsed"></a>`Benchmark.Deferred.prototype.elapsed`
<a href="#benchmarkdeferredprototypeelapsed">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3621 "View in source") [&#x24C9;][1]

*(Number)*: The time taken to complete the deferred benchmark *(secs)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototyperesolve"></a>`Benchmark.Deferred.prototype.resolve`
<a href="#benchmarkdeferredprototyperesolve">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1188 "View in source") [&#x24C9;][1]

*(Unknown)*: Handles cycling/completing the deferred benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkdeferredprototypetimestamp"></a>`Benchmark.Deferred.prototype.timeStamp`
<a href="#benchmarkdeferredprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3629 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the deferred benchmark started *(ms)*.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event`

<!-- div -->

### <a id="benchmarkeventtype"></a>`Benchmark.Event(type)`
<a href="#benchmarkeventtype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L461 "View in source") [&#x24C9;][1]

The Event constructor.

#### Arguments
1. `type` *(String|Object)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype`

<!-- div -->

### <a id="benchmarkeventprototypeaborted"></a>`Benchmark.Event.prototype.aborted`
<a href="#benchmarkeventprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3645 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the emitters listener iteration is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypecancelled"></a>`Benchmark.Event.prototype.cancelled`
<a href="#benchmarkeventprototypecancelled">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3653 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the default action is cancelled.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototyperesult"></a>`Benchmark.Event.prototype.result`
<a href="#benchmarkeventprototyperesult">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3669 "View in source") [&#x24C9;][1]

*(Mixed)*: The return value of the last executed listener.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetimestamp"></a>`Benchmark.Event.prototype.timeStamp`
<a href="#benchmarkeventprototypetimestamp">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3685 "View in source") [&#x24C9;][1]

*(Number)*: A timestamp of when the event was created *(ms)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkeventprototypetype"></a>`Benchmark.Event.prototype.type`
<a href="#benchmarkeventprototypetype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3693 "View in source") [&#x24C9;][1]

*(String)*: The event type.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.currentTarget`

<!-- div -->

### <a id="benchmarkeventprototypecurrenttarget"></a>`Benchmark.Event.prototype.currentTarget`
<a href="#benchmarkeventprototypecurrenttarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3661 "View in source") [&#x24C9;][1]

*(Object)*: The object whose listeners are currently being processed.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Event.prototype.target`

<!-- div -->

### <a id="benchmarkeventprototypetarget"></a>`Benchmark.Event.prototype.target`
<a href="#benchmarkeventprototypetarget">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3677 "View in source") [&#x24C9;][1]

*(Object)*: The object to which the event was originally emitted.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite`

<!-- div -->

### <a id="benchmarksuitename--options"></a>`Benchmark.Suite(name [, options={}])`
<a href="#benchmarksuitename--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L507 "View in source") [&#x24C9;][1]

The Suite constructor.

#### Arguments
1. `name` *(String)*: A name to identify the suite.
2. `[options={}]` *(Object)*: Options object.

#### Example
~~~ js
// basic usage (the `new` operator is optional)
var suite = new Benchmark.Suite;

// or using a name first
var suite = new Benchmark.Suite('foo');

// or with options
var suite = new Benchmark.Suite('foo', {

  // called when the suite starts running
  'onStart': onStart,

  // called between running benchmarks
  'onCycle': onCycle,

  // called when aborted
  'onAbort': onAbort,

  // called when a test errors
  'onError': onError,

  // called when reset
  'onReset': onReset,

  // called when the suite completes running
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.prototype`

<!-- div -->

### <a id="benchmarksuiteprototypeaborted"></a>`Benchmark.Suite.prototype.aborted`
<a href="#benchmarksuiteprototypeaborted">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3734 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is aborted.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypelength"></a>`Benchmark.Suite.prototype.length`
<a href="#benchmarksuiteprototypelength">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3726 "View in source") [&#x24C9;][1]

*(Number)*: The number of benchmarks in the suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunning"></a>`Benchmark.Suite.prototype.running`
<a href="#benchmarksuiteprototyperunning">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3742 "View in source") [&#x24C9;][1]

*(Boolean)*: A flag to indicate if the suite is running.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeabort"></a>`Benchmark.Suite.prototype.abort()`
<a href="#benchmarksuiteprototypeabort">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1902 "View in source") [&#x24C9;][1]

Aborts all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeaddname-fn--options"></a>`Benchmark.Suite.prototype.add(name, fn [, options={}])`
<a href="#benchmarksuiteprototypeaddname-fn--options">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1962 "View in source") [&#x24C9;][1]

Adds a test to the benchmark suite.

#### Arguments
1. `name` *(String)*: A name to identify the benchmark.
2. `fn` *(Function|String)*: The test to benchmark.
3. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// basic usage
suite.add(fn);

// or using a name first
suite.add('foo', fn);

// or with options
suite.add('foo', fn, {
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or name and options
suite.add('foo', {
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});

// or options only
suite.add({
  'name': 'foo',
  'fn': fn,
  'onCycle': onCycle,
  'onComplete': onComplete
});
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypecloneoptions"></a>`Benchmark.Suite.prototype.clone(options)`
<a href="#benchmarksuiteprototypecloneoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L1981 "View in source") [&#x24C9;][1]

Creates a new suite with cloned benchmarks.

#### Arguments
1. `options` *(Object)*: Options object to overwrite cloned options.

#### Returns
*(Object)*: The new suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeemittype"></a>`Benchmark.Suite.prototype.emit(type)`
<a href="#benchmarkprototypeemittype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2095 "View in source") [&#x24C9;][1]

Executes all registered listeners of the specified event type.

#### Arguments
1. `type` *(String|Object)*: The event type or object.

#### Returns
*(Mixed)*: Returns the return value of the last listener executed.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypefiltercallback"></a>`Benchmark.Suite.prototype.filter(callback)`
<a href="#benchmarksuiteprototypefiltercallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2004 "View in source") [&#x24C9;][1]

An `Array#filter` like method.

#### Arguments
1. `callback` *(Function|String)*: The function/alias called per iteration.

#### Returns
*(Object)*: A new suite of benchmarks that passed callback filter.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeforeachcallback"></a>`Benchmark.Suite.prototype.forEach(callback)`
<a href="#benchmarksuiteprototypeforeachcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3752 "View in source") [&#x24C9;][1]

An `Array#forEach` like method. Callbacks may terminate the loop by explicitly returning `false`.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Object)*: The suite iterated over.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeindexofvalue"></a>`Benchmark.Suite.prototype.indexOf(value)`
<a href="#benchmarksuiteprototypeindexofvalue">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3761 "View in source") [&#x24C9;][1]

An `Array#indexOf` like method.

#### Arguments
1. `value` *(Mixed)*: The value to search for.

#### Returns
*(Number)*: The index of the matched value or `-1`.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeinvokename--arg1-arg2-"></a>`Benchmark.Suite.prototype.invoke(name [, arg1, arg2, ...])`
<a href="#benchmarksuiteprototypeinvokename--arg1-arg2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3771 "View in source") [&#x24C9;][1]

Invokes a method on all benchmarks in the suite.

#### Arguments
1. `name` *(String|Object)*: The name of the method to invoke OR options object.
2. `[arg1, arg2, ...]` *(Mixed)*: Arguments to invoke the method with.

#### Returns
*(Array)*: A new array of values returned from each method invoked.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypejoinseparator-"></a>`Benchmark.Suite.prototype.join([separator=','])`
<a href="#benchmarksuiteprototypejoinseparator-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3780 "View in source") [&#x24C9;][1]

Converts the suite of benchmarks to a string.

#### Arguments
1. `[separator=',']` *(String)*: A string to separate each element of the array.

#### Returns
*(String)*: The string.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypelistenerstype"></a>`Benchmark.Suite.prototype.listeners(type)`
<a href="#benchmarkprototypelistenerstype">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2125 "View in source") [&#x24C9;][1]

Returns an array of event listeners for a given type that can be manipulated to add or remove listeners.

#### Arguments
1. `type` *(String)*: The event type.

#### Returns
*(Array)*: The listeners array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypemapcallback"></a>`Benchmark.Suite.prototype.map(callback)`
<a href="#benchmarksuiteprototypemapcallback">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3789 "View in source") [&#x24C9;][1]

An `Array#map` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.

#### Returns
*(Array)*: A new array of values returned by the callback.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeofftype-listener"></a>`Benchmark.Suite.prototype.off([type, listener])`
<a href="#benchmarkprototypeofftype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2158 "View in source") [&#x24C9;][1]

Unregisters a listener for the specified event type(s), or unregisters all listeners for the specified event type(s), or unregisters all listeners for all event types.

#### Arguments
1. `[type]` *(String)*: The event type.
2. `[listener]` *(Function)*: The function to unregister.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// unregister a listener for an event type
bench.off('cycle', listener);

// unregister a listener for multiple event types
bench.off('start cycle', listener);

// unregister all listeners for an event type
bench.off('cycle');

// unregister all listeners for multiple event types
bench.off('start cycle complete');

// unregister all listeners for all event types
bench.off();
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarkprototypeontype-listener"></a>`Benchmark.Suite.prototype.on(type, listener)`
<a href="#benchmarkprototypeontype-listener">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2197 "View in source") [&#x24C9;][1]

Registers a listener for the specified event type(s).

#### Arguments
1. `type` *(String)*: The event type.
2. `listener` *(Function)*: The function to register.

#### Returns
*(Object)*: The benchmark instance.

#### Example
~~~ js
// register a listener for an event type
bench.on('cycle', listener);

// register a listener for multiple event types
bench.on('start cycle', listener);
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepluckproperty"></a>`Benchmark.Suite.prototype.pluck(property)`
<a href="#benchmarksuiteprototypepluckproperty">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3798 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all benchmarks in the suite.

#### Arguments
1. `property` *(String)*: The property to pluck.

#### Returns
*(Array)*: A new array of property values.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepop"></a>`Benchmark.Suite.prototype.pop()`
<a href="#benchmarksuiteprototypepop">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3806 "View in source") [&#x24C9;][1]

Removes the last benchmark from the suite and returns it.

#### Returns
*(Mixed)*: The removed benchmark.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypepush"></a>`Benchmark.Suite.prototype.push()`
<a href="#benchmarksuiteprototypepush">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3814 "View in source") [&#x24C9;][1]

Appends benchmarks to the suite.

#### Returns
*(Number)*: The suite's new length.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereducecallback-accumulator"></a>`Benchmark.Suite.prototype.reduce(callback, accumulator)`
<a href="#benchmarksuiteprototypereducecallback-accumulator">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3833 "View in source") [&#x24C9;][1]

An `Array#reduce` like method.

#### Arguments
1. `callback` *(Function)*: The function called per iteration.
2. `accumulator` *(Mixed)*: Initial value of the accumulator.

#### Returns
*(Mixed)*: The accumulator.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereset"></a>`Benchmark.Suite.prototype.reset()`
<a href="#benchmarksuiteprototypereset">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2019 "View in source") [&#x24C9;][1]

Resets all benchmarks in the suite.

#### Returns
*(Object)*: The suite instance.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypereverse"></a>`Benchmark.Suite.prototype.reverse()`
<a href="#benchmarksuiteprototypereverse">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L638 "View in source") [&#x24C9;][1]

Rearrange the host array's elements in reverse order.

#### Returns
*(Array)*: The reversed array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototyperunoptions"></a>`Benchmark.Suite.prototype.run([options={}])`
<a href="#benchmarksuiteprototyperunoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L2056 "View in source") [&#x24C9;][1]

Runs the suite.

#### Arguments
1. `[options={}]` *(Object)*: Options object.

#### Returns
*(Object)*: The suite instance.

#### Example
~~~ js
// basic usage
suite.run();

// or with options
suite.run({ 'async': true, 'queued': true });
~~~

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeshift"></a>`Benchmark.Suite.prototype.shift()`
<a href="#benchmarksuiteprototypeshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L671 "View in source") [&#x24C9;][1]

Removes the first element of the host array and returns it.

#### Returns
*(Mixed)*: The first element of the array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeslicestart-end"></a>`Benchmark.Suite.prototype.slice(start, end)`
<a href="#benchmarksuiteprototypeslicestart-end">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L684 "View in source") [&#x24C9;][1]

Creates an array of the host array's elements from the start index up to, but not including, the end index.

#### Arguments
1. `start` *(Number)*: The starting index.
2. `end` *(Number)*: The end index.

#### Returns
*(Array)*: The new array.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesortcomparefnnull"></a>`Benchmark.Suite.prototype.sort([compareFn=null])`
<a href="#benchmarksuiteprototypesortcomparefnnull">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3823 "View in source") [&#x24C9;][1]

Sorts the benchmarks of the suite.

#### Arguments
1. `[compareFn=null]` *(Function)*: A function that defines the sort order.

#### Returns
*(Object)*: The sorted suite.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypesplicestart-deletecount--val1-val2-"></a>`Benchmark.Suite.prototype.splice(start, deleteCount [, val1, val2, ...])`
<a href="#benchmarksuiteprototypesplicestart-deletecount--val1-val2-">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L714 "View in source") [&#x24C9;][1]

Allows removing a range of elements and/or inserting elements into the host array.

#### Arguments
1. `start` *(Number)*: The start index.
2. `deleteCount` *(Number)*: The number of elements to delete.
3. `[val1, val2, ...]` *(Mixed)*: values to insert at the `start` index.

#### Returns
*(Array)*: An array of removed elements.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteprototypeunshift"></a>`Benchmark.Suite.prototype.unshift()`
<a href="#benchmarksuiteprototypeunshift">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L749 "View in source") [&#x24C9;][1]

Appends arguments to the host array.

#### Returns
*(Number)*: The new length.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Benchmark.Suite.options`

<!-- div -->

### <a id="benchmarksuiteoptions"></a>`Benchmark.Suite.options`
<a href="#benchmarksuiteoptions">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3705 "View in source") [&#x24C9;][1]

*(Object)*: The default options copied by suite instances.

* * *

<!-- /div -->


<!-- div -->

### <a id="benchmarksuiteoptionsname"></a>`Benchmark.Suite.options.name`
<a href="#benchmarksuiteoptionsname">#</a> [&#x24C8;](https://github.com/bestiejs/benchmark.js/blob/master/benchmark.js#L3713 "View in source") [&#x24C9;][1]

*(String)*: The name of the suite.

* * *

<!-- /div -->


<!-- /div -->


<!-- /div -->


  [1]: #Benchmark "Jump back to the TOC."# JSON 3 #

![JSON 3 Logo](http://bestiejs.github.io/json3/page/logo.png)

**JSON 3** is a modern JSON implementation compatible with a variety of JavaScript platforms, including Internet Explorer 6, Opera 7, Safari 2, and Netscape 6. The current version is **3.2.6**.

- [Development Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.js) *(40 KB; uncompressed with comments)*
- [Production Version](https://raw.github.com/bestiejs/json3/v3.2.6/lib/json3.min.js) *(3.3 KB; compressed and `gzip`-ped)*

CDN copies are also available at [cdnjs](http://cdnjs.com/libraries/json3/) & [jsDelivr](http://www.jsdelivr.com/#!json3).

[JSON](http://json.org/) is a language-independent data interchange format based on a loose subset of the JavaScript grammar. Originally popularized by [Douglas Crockford](http://www.crockford.com/), the format was standardized in the [fifth edition](http://es5.github.com/) of the ECMAScript specification. The 5.1 edition, ratified in June 2011, incorporates several modifications to the grammar pertaining to the serialization of dates.

JSON 3 exposes two functions: `stringify()` for [serializing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/stringify) a JavaScript value to JSON, and `parse()` for [producing](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/JSON/parse) a JavaScript value from a JSON source string. It is a **drop-in replacement** for [JSON 2](http://json.org/js). The functions behave exactly as described in the ECMAScript spec, **except** for the date serialization discrepancy noted below.

The JSON 3 parser does **not** use `eval` or regular expressions. This provides security and performance benefits in obsolete and mobile environments, where the margin is particularly significant. The complete [benchmark suite](http://jsperf.com/json3) is available on [jsPerf](http://jsperf.com/).

The project is [hosted on GitHub](http://git.io/json3), along with the [unit tests](http://bestiejs.github.io/json3/test/test_browser.html). It is part of the [BestieJS](https://github.com/bestiejs) family, a collection of best-in-class JavaScript libraries that promote cross-platform support, specification precedents, unit testing, and plenty of documentation.

# Changes from JSON 2 #

JSON 3...

* Correctly serializes primitive wrapper objects.
* Throws a `TypeError` when serializing cyclic structures (JSON 2 recurses until the call stack overflows).
* Utilizes **feature tests** to detect broken or incomplete *native* JSON implementations (JSON 2 only checks for the presence of the native functions). The tests are only executed once at runtime, so there is no additional performance cost when parsing or serializing values.

**As of v3.2.3**, JSON 3 is compatible with [Prototype](http://prototypejs.org) 1.6.1 and older.

In contrast to JSON 2, JSON 3 **does not**...

* Add `toJSON()` methods to the `Boolean`, `Number`, and `String` prototypes. These are not part of any standard, and are made redundant by the design of the `stringify()` implementation.
* Add `toJSON()` or `toISOString()` methods to `Date.prototype`. See the note about date serialization below.

## Date Serialization

**JSON 3 deviates from the specification in one important way**: it does not define `Date#toISOString()` or `Date#toJSON()`. This preserves CommonJS compatibility and avoids polluting native prototypes. Instead, date serialization is performed internally by the `stringify()` implementation: if a date object does not define a custom `toJSON()` method, it is serialized as a [simplified ISO 8601 date-time string](http://es5.github.com/#x15.9.1.15).

**Several native `Date#toJSON()` implementations produce date time strings that do *not* conform to the grammar outlined in the spec**. For instance, all versions of Safari 4, as well as JSON 2, fail to serialize extended years correctly. Furthermore, JSON 2 and older implementations omit the milliseconds from the date-time string (optional in ES 5, but required in 5.1). Finally, in all versions of Safari 4 and 5, serializing an invalid date will produce the string `"Invalid Date"`, rather than `null`. Because these environments exhibit other serialization bugs, however, JSON 3 will override the native `stringify()` implementation.

Portions of the date serialization code are adapted from the [`date-shim`](https://github.com/Yaffle/date-shim) project.

# Usage #

## Web Browsers

    <script src="http://bestiejs.github.io/json3/lib/json3.js"></script>
    <script>
      JSON.stringify({"Hello": 123});
      // => '{"Hello":123}'
      JSON.parse("[[1, 2, 3], 1, 2, 3, 4]", function (key, value) {
        if (typeof value == "number") {
          value = value % 2 ? "Odd" : "Even";
        }
        return value;
      });
      // => [["Odd", "Even", "Odd"], "Odd", "Even", "Odd", "Even"]
    </script>

## CommonJS Environments

    var JSON3 = require("./path/to/json3");
    JSON3.parse("[1, 2, 3]");
    // => [1, 2, 3]

## JavaScript Engines

    load("path/to/json3.js");
    JSON.stringify({"Hello": 123, "Good-bye": 456}, ["Hello"], "\t");
    // => '{\n\t"Hello": 123\n}'

# Compatibility #

JSON 3 has been **tested** with the following web browsers, CommonJS environments, and JavaScript engines.

## Web Browsers

- Windows [Internet Explorer](http://www.microsoft.com/windows/internet-explorer), version 6.0 and higher
- Mozilla [Firefox](http://www.mozilla.com/firefox), version 1.0 and higher
- Apple [Safari](http://www.apple.com/safari), version 2.0 and higher
- [Opera](http://www.opera.com) 7.02 and higher
- [Mozilla](http://sillydog.org/narchive/gecko.php) 1.0, [Netscape](http://sillydog.org/narchive/) 6.2.3, and [SeaMonkey](http://www.seamonkey-project.org/) 1.0 and higher

## CommonJS Environments

- [Node](http://nodejs.org/) 0.2.6 and higher
- [RingoJS](http://ringojs.org/) 0.4 and higher
- [Narwhal](http://narwhaljs.org/) 0.3.2 and higher

## JavaScript Engines

- Mozilla [Rhino](http://www.mozilla.org/rhino) 1.5R5 and higher
- WebKit [JSC](https://trac.webkit.org/wiki/JSC)
- Google [V8](http://code.google.com/p/v8)

## Known Incompatibilities

* Attempting to serialize the `arguments` object may produce inconsistent results across environments due to specification version differences. As a workaround, please convert the `arguments` object to an array first: `JSON.stringify([].slice.call(arguments, 0))`.

## Required Native Methods

JSON 3 assumes that the following methods exist and function as described in the ECMAScript specification:

- The `Number`, `String`, `Array`, `Object`, `Date`, `SyntaxError`, and `TypeError` constructors.
- `String.fromCharCode`
- `Object#toString`
- `Function#call`
- `Math.floor`
- `Number#toString`
- `Date#valueOf`
- `String.prototype`: `indexOf`, `charCodeAt`, `charAt`, `slice`.
- `Array.prototype`: `push`, `pop`, `join`.

# Contribute #

Check out a working copy of the JSON 3 source code with [Git](http://git-scm.com/):

    $ git clone git://github.com/bestiejs/json3.git
    $ cd json3
    $ git submodule update --init

If you'd like to contribute a feature or bug fix, you can [fork](http://help.github.com/fork-a-repo/) JSON 3, commit your changes, and [send a pull request](http://help.github.com/send-pull-requests/). Please make sure to update the unit tests in the `test` directory as well.

Alternatively, you can use the [GitHub issue tracker](https://github.com/bestiejs/json3/issues) to submit bug reports, feature requests, and questions, or send tweets to [@kitcambridge](http://twitter.com/kitcambridge).

JSON 3 is released under the [MIT License](http://kit.mit-license.org/).#object-keys <sup>[![Version Badge][2]][1]</sup>

[![Build Status][3]][4]
[![dependency status][5]][6]
[![dev dependency status][7]][8]
[![License][license-image]][license-url]
[![Downloads][downloads-image]][downloads-url]

[![npm badge][13]][1]

[![browser support][9]][10]

An Object.keys shim. Invoke its "shim" method to shim Object.keys if it is unavailable.

Most common usage:
```js
var keys = Object.keys || require('object-keys');
```

## Example

```js
var keys = require('object-keys');
var assert = require('assert');
var obj = {
	a: true,
	b: true,
	c: true
};

assert.deepEqual(keys(obj), ['a', 'b', 'c']);
```

```js
var keys = require('object-keys');
var assert = require('assert');
/* when Object.keys is not present */
delete Object.keys;
var shimmedKeys = keys.shim();
assert.equal(shimmedKeys, keys);
assert.deepEqual(Object.keys(obj), keys(obj));
```

```js
var keys = require('object-keys');
var assert = require('assert');
/* when Object.keys is present */
var shimmedKeys = keys.shim();
assert.equal(shimmedKeys, Object.keys);
assert.deepEqual(Object.keys(obj), keys(obj));
```

## Source
Implementation taken directly from [es5-shim][11], with modifications, including from [lodash][12].

## Tests
Simply clone the repo, `npm install`, and run `npm test`

[1]: https://npmjs.org/package/object-keys
[2]: http://vb.teelaun.ch/ljharb/object-keys.svg
[3]: https://travis-ci.org/ljharb/object-keys.svg
[4]: https://travis-ci.org/ljharb/object-keys
[5]: https://david-dm.org/ljharb/object-keys.svg
[6]: https://david-dm.org/ljharb/object-keys
[7]: https://david-dm.org/ljharb/object-keys/dev-status.svg
[8]: https://david-dm.org/ljharb/object-keys#info=devDependencies
[9]: https://ci.testling.com/ljharb/object-keys.png
[10]: https://ci.testling.com/ljharb/object-keys
[11]: https://github.com/es-shims/es5-shim/blob/master/es5-shim.js#L542-589
[12]: https://github.com/bestiejs/lodash
[13]: https://nodei.co/npm/object-keys.png?downloads=true&stars=true
[license-image]: http://img.shields.io/npm/l/object-keys.svg
[license-url]: LICENSE
[downloads-image]: http://img.shields.io/npm/dm/object-keys.svg
[downloads-url]: http://npm-stat.com/charts.html?package=object-keys

# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT
# socket.io-client

[![Build Status](https://secure.travis-ci.org/Automattic/socket.io-client.svg)](http://travis-ci.org/Automattic/socket.io-client)
![NPM version](https://badge.fury.io/js/socket.io-client.svg)
![Downloads](http://img.shields.io/npm/dm/socket.io-client.svg?style=flat)

## How to use

A standalone build of `socket.io-client` is exposed automatically by the
socket.io server as `/socket.io/socket.io.js`. Alternatively you can
serve the file `socket.io.js` found at the root of this repository.

```html
<script src="/socket.io/socket.io.js"></script>
<script>
  var socket = io('http://localhost');
  socket.on('connect', function(){});
  socket.on('event', function(data){});
  socket.on('disconnect', function(){});
</script>
```

Socket.IO is compatible with [browserify](http://browserify.org/).

### Node.JS (server-side usage)

  Add `socket.io-client` to your `package.json` and then:

  ```js
  var socket = require('socket.io-client')('http://localhost');
  socket.on('connect', function(){});
  socket.on('event', function(data){});
  socket.on('disconnect', function(){});
  ```

## API

### IO(url:String, opts:Object):Socket

  Exposed as the `io` namespace in the standalone build, or the result
  of calling `require('socket.io-client')`.

  When called, it creates a new `Manager` for the given URL, and attempts
  to reuse an existing `Manager` for subsequent calls, unless the
  `multiplex` option is passed with `false`.

  The rest of the options are passed to the `Manager` constructor (see below
  for details).

  A `Socket` instance is returned for the namespace specified by the
  pathname in the URL, defaulting to `/`. For example, if the `url` is
  `http://localhost/users`, a transport connection will be established to
  `http://localhost` and a Socket.IO connection will be established to
  `/users`.

### IO#protocol

  Socket.io protocol revision number this client works with.

### IO#Socket

  Reference to the `Socket` constructor.

### IO#Manager

  Reference to the `Manager` constructor.

### IO#Emitter

  Reference to the `Emitter` constructor.

### Manager(url:String, opts:Object)

  A `Manager` represents a connection to a given Socket.IO server. One or
  more `Socket` instances are associated with the manager. The manager
  can be accessed through the `io` property of each `Socket` instance.

  The `opts` are also passed to `engine.io` upon initialization of the
  underlying `Socket`.

  Options:
  - `reconnection` whether to reconnect automatically (`true`)
  - `reconnectionAttempts` (`Infinity`) before giving up
  - `reconnectionDelay` how long to initially wait before attempting a new
    reconnection (`1000`). Affected by +/- `randomizationFactor`,
    for example the default initial delay will be between 500 to 1500ms.
  - `reconnectionDelayMax` maximum amount of time to wait between
    reconnections (`5000`). Each attempt increases the reconnection delay by 2x
    along with a randomization as above
  - `randomizationFactor(`0.5`), 0 <= randomizationFactor <= 1
  - `timeout` connection timeout before a `connect_error`
    and `connect_timeout` events are emitted (`20000`)
  - `autoConnect` by setting this false, you have to call `manager.open`
    whenever you decide it's appropriate

#### Events

  - `connect`. Fired upon a successful connection.
  - `connect_error`. Fired upon a connection error.
    Parameters:
      - `Object` error object
  - `connect_timeout`. Fired upon a connection timeout.
  - `reconnect`. Fired upon a successful reconnection.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_attempt`. Fired upon an attempt to reconnect.
  - `reconnecting`. Fired upon an attempt to reconnect.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_error`. Fired upon a reconnection attempt error.
    Parameters:
      - `Object` error object
  - `reconnect_failed`. Fired when couldn't reconnect within `reconnectionAttempts`

The events above are also emitted on the individual sockets that
reconnect that depend on this `Manager`.

### Manager#reconnection(v:Boolean):Manager

  Sets the `reconnection` option, or returns it if no parameters
  are passed.

### Manager#reconnectionAttempts(v:Boolean):Manager

  Sets the `reconnectionAttempts` option, or returns it if no parameters
  are passed.

### Manager#reconnectionDelay(v:Boolean):Manager

  Sets the `reconectionDelay` option, or returns it if no parameters
  are passed.

### Manager#reconnectionDelayMax(v:Boolean):Manager

  Sets the `reconectionDelayMax` option, or returns it if no parameters
  are passed.

### Manager#timeout(v:Boolean):Manager

  Sets the `timeout` option, or returns it if no parameters
  are passed.

### Socket

#### Socket#id:String

A property on the `socket` instance that is equal to the underlying engine.io socket id.

The property is present once the socket has connected, is removed when the socket disconnects and is updated if the socket reconnects.

#### Events

  - `connect`. Fired upon a connection including a successful reconnection.
  - `error`. Fired upon a connection error
    Parameters:
      - `Object` error data
  - `disconnect`. Fired upon a disconnection.
  - `reconnect`. Fired upon a successful reconnection.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_attempt`. Fired upon an attempt to reconnect.
  - `reconnecting`. Fired upon an attempt to reconnect.
    Parameters:
      - `Number` reconnection attempt number
  - `reconnect_error`. Fired upon a reconnection attempt error.
    Parameters:
      - `Object` error object
  - `reconnect_failed`. Fired when couldn't reconnect within `reconnectionAttempts`

## License

[MIT](/LICENSE)
# to-array

Turn an array like into an array

## Example

``` js
var toArray = require("to-array")
    , elems = document.links

var array = toArray(elems)
```

## Installation

`npm install to-array`

## Contributors

 - Raynos

## MIT Licenced
has-binarydata.js
=================

Simple module to test if an object contains binary data

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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

# Engine.IO client

[![Build Status](https://secure.travis-ci.org/Automattic/engine.io-client.png)](http://travis-ci.org/Automattic/engine.io-client)
[![NPM version](https://badge.fury.io/js/engine.io-client.png)](http://badge.fury.io/js/engine.io-client)

This is the client for [Engine.IO](http://github.com/automattic/engine.io),
the implementation of transport-based cross-browser/cross-device
bi-directional communication layer for [Socket.IO](http://github.com/automattic/socket.io).

## How to use

### Standalone

You can find an `engine.io.js` file in this repository, which is a
standalone build you can use as follows:

```html
<script src="/path/to/engine.io.js"></script>
<script>
  // eio = Socket
  var socket = eio('ws://localhost');
  socket.on('open', function(){
    socket.on('message', function(data){});
    socket.on('close', function(){});
  });
</script>
```

### With browserify

Engine.IO is a commonjs module, which means you can include it by using
`require` on the browser and package using [browserify](http://browserify.org/):

1. install the client package

    ```bash
    $ npm install engine.io-client
    ```

1. write your app code

    ```js
    var socket = require('engine.io-client')('ws://localhost');
    socket.on('open', function(){
      socket.on('message', function(data){});
      socket.on('close', function(){});
    });
    ```

1. build your app bundle

    ```bash
    $ browserify app.js > bundle.js
    ```

1. include on your page

    ```html
    <script src="/path/to/bundle.js"></script>
    ```

### Sending and receiving binary

```html
<script src="/path/to/engine.io.js"></script>
<script>
  var socket = new eio.Socket('ws://localhost/');
  socket.binaryType = 'blob';
  socket.on('open', function () {
    socket.send(new Int8Array(5));
    socket.on('message', function(blob){});
    socket.on('close', function(){ });
  });
</script>
```

### Node.JS

Add `engine.io-client` to your `package.json` and then:

```js
var socket = require('engine.io-client')('ws://localhost');
socket.on('open', function(){
  socket.on('message', function(data){});
  socket.on('close', function(){});
});
```

### Node.js with certificates
```js
var opts = {
  key: fs.readFileSync('test/fixtures/client.key'),
  cert: fs.readFileSync('test/fixtures/client.crt'),
  ca: fs.readFileSync('test/fixtures/ca.crt')
};

var socket = require('engine.io-client')('ws://localhost', opts);
socket.on('open', function(){
  socket.on('message', function(data){});
  socket.on('close', function(){});
});
```

## Features

- Lightweight
- Runs on browser and node.js seamlessly
- Transports are independent of `Engine`
  - Easy to debug
  - Easy to unit test
- Runs inside HTML5 WebWorker
- Can send and receive binary data
  - Receives as ArrayBuffer or Blob when in browser, and Buffer or ArrayBuffer
    in Node
  - When XHR2 or WebSockets are used, binary is emitted directly. Otherwise
    binary is encoded into base64 strings, and decoded when binary types are
    supported.
  - With browsers that don't support ArrayBuffer, an object { base64: true,
    data: dataAsBase64String } is emitted on the `message` event.

## API

### Socket

The client class. Mixes in [Emitter](http://github.com/component/emitter).
Exposed as `eio` in the browser standalone build.

#### Properties

- `protocol` _(Number)_: protocol revision number
- `binaryType` _(String)_ : can be set to 'arraybuffer' or 'blob' in browsers,
  and `buffer` or `arraybuffer` in Node. Blob is only used in browser if it's
  supported.

#### Events

- `open`
  - Fired upon successful connection.
- `message`
  - Fired when data is received from the server.
  - **Arguments**
    - `String` | `ArrayBuffer`: utf-8 encoded data or ArrayBuffer containing
      binary data
- `close`
  - Fired upon disconnection. In compliance with the WebSocket API spec, this event may be 
    fired even if the `open` event does not occur (i.e. due to connection error or `close()`).
- `error`
  - Fired when an error occurs.
- `flush`
  - Fired upon completing a buffer flush
- `drain`
  - Fired after `drain` event of transport if writeBuffer is empty
- `upgradeError`
  - Fired if an error occurs with a transport we're trying to upgrade to.
- `upgrade`
  - Fired upon upgrade success, after the new transport is set

#### Methods

- **constructor**
    - Initializes the client
    - **Parameters**
      - `String` uri
      - `Object`: optional, options object
    - **Options**
      - `agent` (`http.Agent`): `http.Agent` to use, defaults to `false` (NodeJS only)
      - `upgrade` (`Boolean`): defaults to true, whether the client should try
      to upgrade the transport from long-polling to something better.
      - `forceJSONP` (`Boolean`): forces JSONP for polling transport.
      - `jsonp` (`Boolean`): determines whether to use JSONP when
        necessary for polling. If disabled (by settings to false) an error will
        be emitted (saying "No transports available") if no other transports
        are available. If another transport is available for opening a
        connection (e.g. WebSocket) that transport
        will be used instead.
      - `forceBase64` (`Boolean`): forces base 64 encoding for polling transport even when XHR2 responseType is available and WebSocket even if the used standard supports binary.
      - `enablesXDR` (`Boolean`): enables XDomainRequest for IE8 to avoid loading bar flashing with click sound. default to `false` because XDomainRequest has a flaw of not sending cookie.
      - `timestampRequests` (`Boolean`): whether to add the timestamp with
        each transport request. Note: this is ignored if the browser is
        IE or Android, in which case requests are always stamped (`false`)
      - `timestampParam` (`String`): timestamp parameter (`t`)
      - `policyPort` (`Number`): port the policy server listens on (`843`)
      - `path` (`String`): path to connect to, default is `/engine.io`
      - `transports` (`Array`): a list of transports to try (in order).
      Defaults to `['polling', 'websocket']`. `Engine`
      always attempts to connect directly with the first one, provided the
      feature detection test for it passes.
      - `rememberUpgrade` (`Boolean`): defaults to false.
        If true and if the previous websocket connection to the server succeeded,
        the connection attempt will bypass the normal upgrade process and will initially
        try websocket. A connection attempt following a transport error will use the 
        normal upgrade process. It is recommended you turn this on only when using
        SSL/TLS connections, or if you know that your network does not block websockets.
      - `pfx` (`String`): Certificate, Private key and CA certificates to use for SSL. Can be used in Node.js client environment to manually specify certificate information.
      - `key` (`String`): Private key to use for SSL. Can be used in Node.js client environment to manually specify certificate information.
      - `passphrase` (`String`): A string of passphrase for the private key or pfx. Can be used in Node.js client environment to manually specify certificate information.
      - `cert` (`String`): Public x509 certificate to use. Can be used in Node.js client environment to manually specify certificate information.
      - `ca` (`String`|`Array`): An authority certificate or array of authority certificates to check the remote host against.. Can be used in Node.js client environment to manually specify certificate information.
      - `ciphers` (`String`): A string describing the ciphers to use or exclude. Consult the [cipher format list](http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT) for details on the format.. Can be used in Node.js client environment to manually specify certificate information.
      - `rejectUnauthorized` (`Boolean`): If true, the server certificate is verified against the list of supplied CAs. An 'error' event is emitted if verification fails. Verification happens at the connection level, before the HTTP request is sent. Can be used in Node.js client environment to manually specify certificate information.
- `send`
    - Sends a message to the server
    - **Parameters**
      - `String` | `ArrayBuffer` | `ArrayBufferView` | `Blob`: data to send
      - `Function`: optional, callback upon `drain`
- `close`
    - Disconnects the client.

### Transport

The transport class. Private. _Inherits from EventEmitter_.

#### Events

- `poll`: emitted by polling transports upon starting a new request
- `pollComplete`: emitted by polling transports upon completing a request
- `drain`: emitted by polling transports upon a buffer drain

## Tests

`engine.io-client` is used to test
[engine](http://github.com/automattic/engine.io). Running the `engine.io`
test suite ensures the client works and vice-versa.

Browser tests are run using [zuul](https://github.com/defunctzombie/zuul). You can
run the tests locally using the following command.

```
./node_modules/.bin/zuul --local 8080 -- test/index.js
```

Additionally, `engine.io-client` has a standalone test suite you can run
with `make test` which will run node.js and browser tests. You must have zuul setup with
a saucelabs account.

## Support

The support channels for `engine.io-client` are the same as `socket.io`:
  - irc.freenode.net **#socket.io**
  - [Google Groups](http://groups.google.com/group/socket_io)
  - [Website](http://socket.io)

## Development

To contribute patches, run tests or benchmarks, make sure to clone the
repository:

```bash
git clone git://github.com/automattic/engine.io-client.git
```

Then:

```bash
cd engine.io-client
npm install
```

See the `Tests` section above for how to run tests before submitting any patches.

## License

MIT - Copyright (c) 2014 Automattic, Inc.

# node-XMLHttpRequest #

node-XMLHttpRequest is a wrapper for the built-in http client to emulate the
browser XMLHttpRequest object.

This can be used with JS designed for browsers to improve reuse of code and
allow the use of existing libraries.

Note: This library currently conforms to [XMLHttpRequest 1](http://www.w3.org/TR/XMLHttpRequest/). Version 2.0 will target [XMLHttpRequest Level 2](http://www.w3.org/TR/XMLHttpRequest2/).

## Usage ##

Here's how to include the module in your project and use as the browser-based
XHR object.

	var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
	var xhr = new XMLHttpRequest();

Note: use the lowercase string "xmlhttprequest" in your require(). On
case-sensitive systems (eg Linux) using uppercase letters won't work.

## Versions ##

Prior to 1.4.0 version numbers were arbitrary. From 1.4.0 on they conform to
the standard major.minor.bugfix. 1.x shouldn't necessarily be considered
stable just because it's above 0.x.

Since the XMLHttpRequest API is stable this library's API is stable as
well. Major version numbers indicate significant core code changes.
Minor versions indicate minor core code changes or better conformity to
the W3C spec.

## License ##

MIT license. See LICENSE for full details.

## Supports ##

* Async and synchronous requests
* GET, POST, PUT, and DELETE requests
* All spec methods (open, send, abort, getRequestHeader,
  getAllRequestHeaders, event methods)
* Requests to all domains

## Known Issues / Missing Features ##

For a list of open issues or to report your own visit the [github issues
page](https://github.com/driverdan/node-XMLHttpRequest/issues).

* Local file access may have unexpected results for non-UTF8 files
* Synchronous requests don't set headers properly
* Synchronous requests freeze node while waiting for response (But that's what you want, right? Stick with async!).
* Some events are missing, such as abort
* getRequestHeader is case-sensitive
* Cookies aren't persisted between requests
* Missing XML support
* Missing basic auth
# ws: a node.js websocket library

[![Build Status](https://travis-ci.org/websockets/ws.svg?branch=master)](https://travis-ci.org/websockets/ws)

`ws` is a simple to use WebSocket implementation, up-to-date against RFC-6455,
and [probably the fastest WebSocket library for node.js][archive].

Passes the quite extensive Autobahn test suite. See http://websockets.github.com/ws
for the full reports.

## Protocol support

* **Hixie draft 76** (Old and deprecated, but still in use by Safari and Opera.
  Added to ws version 0.4.2, but server only. Can be disabled by setting the
  `disableHixie` option to true.)
* **HyBi drafts 07-12** (Use the option `protocolVersion: 8`)
* **HyBi drafts 13-17** (Current default, alternatively option `protocolVersion: 13`)

### Installing

```
npm install --save ws
```

### Sending and receiving text data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  ws.send('something');
});

ws.on('message', function(data, flags) {
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
});
```

### Sending binary data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  var array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }

  ws.send(array, { binary: true, mask: true });
});
```

Setting `mask`, as done for the send options above, will cause the data to be
masked according to the WebSocket protocol. The same option applies for text
data.

### Server example

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});
```

### ExpressJS example

```js
var server = require('http').createServer()
  , url = require('url')
  , WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ server: server })
  , express = require('express')
  , app = express()
  , port = 4080;

app.use(function (req, res) {
  res.send({ msg: "hello" });
});

wss.on('connection', function connection(ws) {
  var location = url.parse(ws.upgradeReq.url, true);
  // you might use location.query.access_token to authenticate or share sessions
  // or ws.upgradeReq.headers.cookie (see http://stackoverflow.com/a/16395220/151312)
  
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});

server.on('request', app);
server.listen(port, function () { console.log('Listening on ' + server.address().port) });
```

### Server sending broadcast data

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    client.send(data);
  });
};
```

### Error handling best practices

```js
// If the WebSocket is closed before the following send is attempted
ws.send('something');

// Errors (both immediate and async write errors) can be detected in an optional
// callback. The callback is also the only way of being notified that data has
// actually been sent.
ws.send('something', function ack(error) {
  // if error is not defined, the send has been completed,
  // otherwise the error object will indicate what failed.
});

// Immediate errors can also be handled with try/catch-blocks, but **note** that
// since sends are inherently asynchronous, socket write failures will *not* be
// captured when this technique is used.
try { ws.send('something'); }
catch (e) { /* handle error */ }
```

### echo.websocket.org demo

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://echo.websocket.org/', {
  protocolVersion: 8, 
  origin: 'http://websocket.org'
});

ws.on('open', function open() {
  console.log('connected');
  ws.send(Date.now().toString(), {mask: true});
});

ws.on('close', function close() {
  console.log('disconnected');
});

ws.on('message', function message(data, flags) {
  console.log('Roundtrip time: ' + (Date.now() - parseInt(data)) + 'ms', flags);

  setTimeout(function timeout() {
    ws.send(Date.now().toString(), {mask: true});
  }, 500);
});
```

### Browserify users
When including ws via a browserify bundle, ws returns global.WebSocket which has slightly different API. 
You should use the standard WebSockets API instead.

https://developer.mozilla.org/en-US/docs/WebSockets/Writing_WebSocket_client_applications#Availability_of_WebSockets


### Other examples

For a full example with a browser client communicating with a ws server, see the
examples folder.

Note that the usage together with Express 3.0 is quite different from Express
2.x. The difference is expressed in the two different serverstats-examples.

Otherwise, see the test cases.

### Running the tests

```
make test
```

## API Docs

See [`/doc/ws.md`](https://github.com/websockets/ws/blob/master/doc/ws.md) for Node.js-like docs for the ws classes.

## Changelog

We're using the GitHub [`releases`](https://github.com/websockets/ws/releases) for changelog entries.

## License

(The MIT License)

Copyright (c) 2011 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[archive]: http://web.archive.org/web/20130314230536/http://hobbycoding.posterous.com/the-fastest-websocket-module-for-nodejs
# Ultron

[![Made by unshift](https://img.shields.io/badge/made%20by-unshift-00ffcc.svg?style=flat-square)](http://unshift.io)[![Version npm](http://img.shields.io/npm/v/ultron.svg?style=flat-square)](http://browsenpm.org/package/ultron)[![Build Status](http://img.shields.io/travis/unshiftio/ultron/master.svg?style=flat-square)](https://travis-ci.org/unshiftio/ultron)[![Dependencies](https://img.shields.io/david/unshiftio/ultron.svg?style=flat-square)](https://david-dm.org/unshiftio/ultron)[![Coverage Status](http://img.shields.io/coveralls/unshiftio/ultron/master.svg?style=flat-square)](https://coveralls.io/r/unshiftio/ultron?branch=master)[![IRC channel](http://img.shields.io/badge/IRC-irc.freenode.net%23unshift-00a8ff.svg?style=flat-square)](http://webchat.freenode.net/?channels=unshift)

Ultron is a high-intelligence robot. It gathers intelligence so it can start
improving upon his rudimentary design. It will learn your event emitting
patterns and find ways to exterminate them. Allowing you to remove only the
event emitters that **you** assigned and not the ones that your users or
developers assigned. This can prevent race conditions, memory leaks and even file
descriptor leaks from ever happening as you won't remove clean up processes.

## Installation

The module is designed to be used in browsers using browserify and in Node.js.
You can install the module through the public npm registry by running the
following command in CLI:

```
npm install --save ultron
```

## Usage

In all examples we assume that you've required the library as following:

```js
'use strict';

var Ultron = require('ultron');
```

Now that we've required the library we can construct our first `Ultron` instance.
The constructor requires one argument which should be the `EventEmitter`
instance that we need to operate upon. This can be the `EventEmitter` module
that ships with Node.js or `EventEmitter3` or anything else as long as it
follow the same API and internal structure as these 2. So with that in mind we
can create the instance:

```js
//
// For the sake of this example we're going to construct an empty EventEmitter
//
var EventEmitter = require('events').EventEmitter; // or require('eventmitter3');
var events = new EventEmitter();

var ultron = new Ultron(events);
```

You can now use the following API's from the Ultron instance:

### Ultron.on

Register a new event listener for the given event. It follows the exact same API
as `EventEmitter.on` but it will return itself instead of returning the
EventEmitter instance. If you are using EventEmitter3 it also supports the
context param:

```js
ultron.on('event-name', handler, { custom: 'function context' });
```

### Ultron.once

Exactly the same as the [Ultron.on](#ultronon) but it only allows the execution
once.

### Ultron.remove

This is where all the magic happens and the safe removal starts. This function
accepts different argument styles:

- No arguments, assume that all events need to be removed so it will work as
  `removeAllListeners()` API.
- 1 argument, when it's a string it will be split on ` ` and `,` to create a
  list of events that need to be cleared.
- Multiple arguments, we assume that they are all names of events that need to
  be cleared.

```js
ultron.remove('foo, bar baz');        // Removes foo, bar and baz.
ultron.remove('foo', 'bar', 'baz');   // Removes foo, bar and baz.
ultron.remove();                      // Removes everything.
```

If you just want to remove a single event listener using a function reference
you can still use the EventEmitter's `removeListener(event, fn)` API:

```js
function foo() {}

ulton.on('foo', foo);
events.removeListener('foo', foo);
```

## License

MIT
# options.js #

A very light-weight in-code option parsers for node.js.

## Usage ##

``` js
var Options = require("options");

// Create an Options object
function foo(options) {
        var default_options = {
                foo : "bar"
        };
        
        // Create an option object with default value
        var opts = new Options(default_options);
        
        // Merge options
        opts = opts.merge(options);
        
        // Reset to default value
        opts.reset();
        
        // Copy selected attributes out
        var seled_att = opts.copy("foo");
        
        // Read json options from a file. 
        opts.read("options.file"); // Sync
        opts.read("options.file", function(err){ // Async
                if(err){ // If error occurs
                        console.log("File error.");
                }else{
                        // No error
                }
        });
        
        // Attributes defined or not
        opts.isDefinedAndNonNull("foobar");
        opts.isDefined("foobar");
}

```


## License ##

(The MIT License)

Copyright (c) 2012 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# After [![Build Status][1]][2]

Invoke callback after n calls

## Status: production ready

## Example

    var after = require("after")
        , next = after(3, logItWorks)

    next()
    next()
    next() // it works

    function logItWorks() {
        console.log("it works!")
    }

## Example with error handling

    var after = require("after")
        , next = after(3, logError)

    next()
    next(new Error("oops")) // logs oops
    next() // does nothing

    function logError(err) {
        console.log(err)
    }

## After < 0.6.0

Older versions of after had iterators and flows in them.

These have been replaced with seperate modules

 - [iterators][8]
 - [composite][9]

## Installation

`npm install after`

## Tests

`npm test`

## Blog post

 - [Flow control in node.js][3]

## Examples :

 - [Determining the end of asynchronous operations][4]
 - [In javascript what are best practices for executing multiple asynchronous functions][5]
 - [JavaScript performance long running tasks][6]
 - [Synchronous database queries with node.js][7]

## Contributors

 - Raynos

## MIT Licenced

  [1]: https://secure.travis-ci.org/Raynos/after.png
  [2]: http://travis-ci.org/Raynos/after
  [3]: http://raynos.org/blog/2/Flow-control-in-node.js
  [4]: http://stackoverflow.com/questions/6852059/determining-the-end-of-asynchronous-operations-javascript/6852307#6852307
  [5]: http://stackoverflow.com/questions/6869872/in-javascript-what-are-best-practices-for-executing-multiple-asynchronous-functi/6870031#6870031
  [6]: http://stackoverflow.com/questions/6864397/javascript-performance-long-running-tasks/6889419#6889419
  [7]: http://stackoverflow.com/questions/6597493/synchronous-database-queries-with-node-js/6620091#6620091
  [8]: http://github.com/Raynos/iterators
  [9]: http://github.com/Raynos/composite
# How to
```javascript
var sliceBuffer = require('arraybuffer.slice');
var ab = (new Int8Array(5)).buffer;
var sliced = sliceBuffer(ab, 1, 3);
sliced = sliceBuffer(ab, 1);
```

# Licence (MIT)
Copyright (C) 2013 Rase-


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Blob
====

A module that exports a constructor that uses window.Blob when available, and a BlobBuilder with any vendor prefix in other cases. If neither is available, it exports undefined.

Usage:

```javascript
var Blob = require('blob');
var b = new Blob(['hi', 'constructing', 'a', 'blob']);
```

## Licence
MIT
# base64-arraybuffer

[![Build Status](https://travis-ci.org/niklasvh/base64-arraybuffer.png)](https://travis-ci.org/niklasvh/base64-arraybuffer)

Encode/decode base64 data into ArrayBuffers

## Getting Started
Install the module with: `npm install base64-arraybuffer`

## API
The library encodes and decodes base64 to and from ArrayBuffers

 - __encode(buffer)__ - Encodes `ArrayBuffer` into base64 string
 - __decode(str)__ - Decodes base64 string to `ArrayBuffer`

## Release History

 - 0.1.2 - Fix old format of typed arrays
 - 0.1.0 - Initial version, basic decode/encode base64 to and from ArrayBuffer

## License
Copyright (c) 2012 Niklas von Hertzen
Licensed under the MIT license.
# utf8.js [![Build status](https://travis-ci.org/mathiasbynens/utf8.js.svg?branch=master)](https://travis-ci.org/mathiasbynens/utf8.js) [![Code coverage status](http://img.shields.io/coveralls/mathiasbynens/utf8.js/master.svg)](https://coveralls.io/r/mathiasbynens/utf8.js) [![Dependency status](https://gemnasium.com/mathiasbynens/utf8.js.svg)](https://gemnasium.com/mathiasbynens/utf8.js)

_utf8.js_ is a well-tested UTF-8 encoder/decoder written in JavaScript. Unlike many other JavaScript solutions, it is designed to be a _proper_ UTF-8 encoder/decoder: it can encode/decode any scalar Unicode code point values, as per [the Encoding Standard](https://encoding.spec.whatwg.org/#utf-8). [Here’s an online demo.](https://mothereff.in/utf-8)

Feel free to fork if you see possible improvements!

## Installation

Via [npm](https://www.npmjs.org/):

```bash
npm install utf8
```

Via [Bower](http://bower.io/):

```bash
bower install utf8
```

Via [Component](https://github.com/component/component):

```bash
component install mathiasbynens/utf8.js
```

In a browser:

```html
<script src="utf8.js"></script>
```

In [Narwhal](http://narwhaljs.org/), [Node.js](https://nodejs.org/), and [RingoJS ≥ v0.8.0](http://ringojs.org/):

```js
var utf8 = require('utf8');
```

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('utf8.js');
```

Using an AMD loader like [RequireJS](http://requirejs.org/):

```js
require(
  {
    'paths': {
      'utf8': 'path/to/utf8'
    }
  },
  ['utf8'],
  function(utf8) {
    console.log(utf8);
  }
);
```

## API

### `utf8.encode(string)`

Encodes any given JavaScript string (`string`) as UTF-8, and returns the UTF-8-encoded version of the string. It throws an error if the input string contains a non-scalar value, i.e. a lone surrogate. (If you need to be able to encode non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
// U+00A9 COPYRIGHT SIGN; see http://codepoints.net/U+00A9
utf8.encode('\xA9');
// → '\xC2\xA9'
// U+10001 LINEAR B SYLLABLE B038 E; see http://codepoints.net/U+10001
utf8.encode('\uD800\uDC01');
// → '\xF0\x90\x80\x81'
```

### `utf8.decode(byteString)`

Decodes any given UTF-8-encoded string (`byteString`) as UTF-8, and returns the UTF-8-decoded version of the string. It throws an error when malformed UTF-8 is detected. (If you need to be able to decode encoded non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
utf8.decode('\xC2\xA9');
// → '\xA9'

utf8.decode('\xF0\x90\x80\x81');
// → '\uD800\uDC01'
// → U+10001 LINEAR B SYLLABLE B038 E
```

### `utf8.version`

A string representing the semantic version number.

## Support

utf8.js has been tested in at least Chrome 27-39, Firefox 3-34, Safari 4-8, Opera 10-28, IE 6-11, Node.js v0.10.0, Narwhal 0.3.2, RingoJS 0.8-0.11, PhantomJS 1.9.0, and Rhino 1.7RC4.

## Unit tests & code coverage

After cloning this repository, run `npm install` to install the dependencies needed for development and testing. You may want to install Istanbul _globally_ using `npm install istanbul -g`.

Once that’s done, you can run the unit tests in Node using `npm test` or `node tests/tests.js`. To run the tests in Rhino, Ringo, Narwhal, PhantomJS, and web browsers as well, use `grunt test`.

To generate the code coverage report, use `grunt cover`.

## FAQ

### Why is the first release named v2.0.0? Haven’t you heard of [semantic versioning](http://semver.org/)?

Long before utf8.js was created, the `utf8` module on npm was registered and used by another (slightly buggy) library. @ryanmcgrath was kind enough to give me access to the `utf8` package on npm when I told him about utf8.js. Since there has already been a v1.0.0 release of the old library, and to avoid breaking backwards compatibility with projects that rely on the `utf8` npm package, I decided the tag the first release of utf8.js as v2.0.0 and take it from there.

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

utf8.js is available under the [MIT](https://mths.be/mit) license.
# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIThas-binarydata.js
=================

Simple module to test if an object contains binary data

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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

# Engine.IO: the realtime engine

[![Build Status](https://secure.travis-ci.org/Automattic/engine.io.png)](http://travis-ci.org/Automattic/engine.io)
[![NPM version](https://badge.fury.io/js/engine.io.png)](http://badge.fury.io/js/engine.io)

`Engine.IO` is the implementation of transport-based
cross-browser/cross-device bi-directional communication layer for
[Socket.IO](http://github.com/learnboost/socket.io).

## How to use

### Server

#### (A) Listening on a port

```js
var engine = require('engine.io');
var server = engine.listen(80);

server.on('connection', function(socket){
  socket.send('utf 8 string');
  socket.send(new Buffer([0, 1, 2, 3, 4, 5])); // binary data
});
```

#### (B) Intercepting requests for a http.Server

```js
var engine = require('engine.io');
var http = require('http').createServer().listen(3000);
var server = engine.attach(http);

server.on('connection', function (socket) {
  socket.on('message', function(data){ });
  socket.on('close', function(){ });
});
```

#### (C) Passing in requests

```js
var engine = require('engine.io');
var server = new engine.Server();

server.on('connection', function(socket){
  socket.send('hi');
});

// …
httpServer.on('upgrade', function(req, socket, head){
  server.handleUpgrade(req, socket, head);
});
httpServer.on('request', function(req, res){
  server.handleRequest(req, res);
});
```

### Client

```html
<script src="/path/to/engine.io.js"></script>
<script>
  var socket = new eio.Socket('ws://localhost/');
  socket.on('open', function(){
    socket.on('message', function(data){});
    socket.on('close', function(){});
  });
</script>
```

For more information on the client refer to the
[engine-client](http://github.com/learnboost/engine.io-client) repository.

## What features does it have?

- **Maximum reliability**. Connections are established even in the presence of:
  - proxies and load balancers.
  - personal firewall and antivirus software.
  - for more information refer to **Goals** and **Architecture** sections
- **Minimal client size** aided by:
  - lazy loading of flash transports.
  - lack of redundant transports.
- **Scalable**
  - load balancer friendly
- **Future proof**
- **100% Node.JS core style**
  - No API sugar (left for higher level projects)
  - Written in readable vanilla JavaScript

## API

### Server

<hr><br>

#### Top-level

These are exposed by `require('engine.io')`:

##### Events

- `flush`
    - Called when a socket buffer is being flushed.
    - **Arguments**
      - `Socket`: socket being flushed
      - `Array`: write buffer
- `drain`
    - Called when a socket buffer is drained
    - **Arguments**
      - `Socket`: socket being flushed

##### Properties

- `protocol` _(Number)_: protocol revision number
- `Server`: Server class constructor
- `Socket`: Socket class constructor
- `Transport` _(Function)_: transport constructor
- `transports` _(Object)_: map of available transports

##### Methods

- `()`
    - Returns a new `Server` instance. If the first argument is an `http.Server` then the
      new `Server` instance will be attached to it. Otherwise, the arguments are passed
      directly to the `Server` constructor.
    - **Parameters**
      - `http.Server`: optional, server to attach to.
      - `Object`: optional, options object (see `Server#constructor` api docs below)

  The following are identical ways to instantiate a server and then attach it.
  ```js
  var httpServer; // previously created with `http.createServer();` from node.js api.

  // create a server first, and then attach
  var eioServer = require('engine.io').Server();
  eioServer.attach(httpServer);

  // or call the module as a function to get `Server`
  var eioServer = require('engine.io')();
  eioServer.attach(httpServer);

  // immediately attach
  var eioServer = require('engine.io')(httpServer);
  ```

- `listen`
    - Creates an `http.Server` which listens on the given port and attaches WS
      to it. It returns `501 Not Implemented` for regular http requests.
    - **Parameters**
      - `Number`: port to listen on.
      - `Object`: optional, options object
      - `Function`: callback for `listen`.
    - **Options**
      - All options from `Server.attach` method, documented below.
      - **Additionally** See Server `constructor` below for options you can pass for creating the new Server
    - **Returns** `Server`
- `attach`
    - Captures `upgrade` requests for a `http.Server`. In other words, makes
      a regular http.Server WebSocket-compatible.
    - **Parameters**
      - `http.Server`: server to attach to.
      - `Object`: optional, options object
    - **Options**
      - All options from `Server.attach` method, documented below.
      - **Additionally** See Server `constructor` below for options you can pass for creating the new Server
    - **Returns** `Server` a new Server instance.

<hr><br>

#### Server

The main server/manager. _Inherits from EventEmitter_.

##### Events

- `connection`
    - Fired when a new connection is established.
    - **Arguments**
      - `Socket`: a Socket object

##### Properties

**Important**: if you plan to use Engine.IO in a scalable way, please
keep in mind the properties below will only reflect the clients connected
to a single process.

- `clients` _(Object)_: hash of connected clients by id.
- `clientsCount` _(Number)_: number of connected clients.

##### Methods

- **constructor**
    - Initializes the server
    - **Parameters**
      - `Object`: optional, options object
    - **Options**
      - `pingTimeout` (`Number`): how many ms without a pong packet to
        consider the connection closed (`60000`)
      - `pingInterval` (`Number`): how many ms before sending a new ping
        packet (`25000`)
      - `maxHttpBufferSize` (`Number`): how many bytes or characters a message
        can be when polling, before closing the session (to avoid DoS). Default
        value is `10E7`.
      - `allowRequest` (`Function`): A function that receives a given handshake
        or upgrade request as its first parameter, and can decide whether to
        continue or not. The second argument is a function that needs to be
        called with the decided information: `fn(err, success)`, where
        `success` is a boolean value where false means that the request is
        rejected, and err is an error code.
      - `transports` (`<Array> String`): transports to allow connections
        to (`['polling', 'websocket']`)
      - `allowUpgrades` (`Boolean`): whether to allow transport upgrades
        (`true`)
      - `cookie` (`String|Boolean`): name of the HTTP cookie that
        contains the client sid to send as part of handshake response
        headers. Set to `false` to not send one. (`io`)
- `close`
    - Closes all clients
    - **Returns** `Server` for chaining
- `handleRequest`
    - Called internally when a `Engine` request is intercepted.
    - **Parameters**
      - `http.ServerRequest`: a node request object
      - `http.ServerResponse`: a node response object
    - **Returns** `Server` for chaining
- `handleUpgrade`
    - Called internally when a `Engine` ws upgrade is intercepted.
    - **Parameters** (same as `upgrade` event)
      - `http.ServerRequest`: a node request object
      - `net.Stream`: TCP socket for the request
      - `Buffer`: legacy tail bytes
    - **Returns** `Server` for chaining
- `attach`
    - Attach this Server instance to an `http.Server`
    - Captures `upgrade` requests for a `http.Server`. In other words, makes
      a regular http.Server WebSocket-compatible.
    - **Parameters**
      - `http.Server`: server to attach to.
      - `Object`: optional, options object
    - **Options**
      - `path` (`String`): name of the path to capture (`/engine.io`).
      - `destroyUpgrade` (`Boolean`): destroy unhandled upgrade requests (`true`)
      - `destroyUpgradeTimeout` (`Number`): milliseconds after which unhandled requests are ended (`1000`)

<hr><br>

#### Socket

A representation of a client. _Inherits from EventEmitter_.

##### Events

- `close`
    - Fired when the client is disconnected.
    - **Arguments**
      - `String`: reason for closing
      - `Object`: description object (optional)
- `message`
    - Fired when the client sends a message.
    - **Arguments**
      - `String` or `Buffer`: Unicode string or Buffer with binary contents
- `error`
    - Fired when an error occurs.
    - **Arguments**
      - `Error`: error object
- `flush`
    - Called when the write buffer is being flushed.
    - **Arguments**
      - `Array`: write buffer
- `drain`
    - Called when the write buffer is drained
- `packet`
    - Called when a socket received a packet (`message`, `ping`)
    - **Arguments**
      - `type`: packet type
      - `data`: packet data (if type is message)
- `packetCreate`
    - Called before a socket sends a packet (`message`, `pong`)
    - **Arguments**
      - `type`: packet type
      - `data`: packet data (if type is message)

##### Properties

- `id` _(String)_: unique identifier
- `server` _(Server)_: engine parent reference
- `request` _(http.ServerRequest)_: request that originated the Socket
- `upgraded` _(Boolean)_: whether the transport has been upgraded
- `readyState` _(String)_: opening|open|closing|closed
- `transport` _(Transport)_: transport reference

##### Methods

- `send`:
    - Sends a message, performing `message = toString(arguments[0])` unless
      sending binary data, which is sent as is.
    - **Parameters**
      - `String` | `Buffer` | `ArrayBuffer` | `ArrayBufferView`: a string or any object implementing `toString()`, with outgoing data, or a Buffer or ArrayBuffer with binary data. Also any ArrayBufferView can be sent as is.
      - `Function`: optional, a callback executed when the message gets flushed out by the transport
    - **Returns** `Socket` for chaining
- `close`
    - Disconnects the client
    - **Returns** `Socket` for chaining

### Client

<hr><br>

Exposed in the `eio` global namespace (in the browser), or by
`require('engine.io-client')` (in Node.JS).

For the client API refer to the 
[engine-client](http://github.com/learnboost/engine.io-client) repository.

## Debug / logging

Engine.IO is powered by [debug](http://github.com/visionmedia/debug).
In order to see all the debug output, run your app with the environment variable
`DEBUG` including the desired scope.

To see the output from all of Engine.IO's debugging scopes you can use:

```
DEBUG=engine* node myapp
```

## Transports

- `polling`: XHR / JSONP polling transport.
- `websocket`: WebSocket transport.

## Plugins

- [engine.io-conflation](https://github.com/EugenDueck/engine.io-conflation): Makes **conflation and aggregation** of messages straightforward.

## Support

The support channels for `engine.io` are the same as `socket.io`:
  - irc.freenode.net **#socket.io**
  - [Google Groups](http://groups.google.com/group/socket_io)
  - [Website](http://socket.io)

## Development

To contribute patches, run tests or benchmarks, make sure to clone the
repository:

```
git clone git://github.com/LearnBoost/engine.io.git
```

Then:

```
cd engine.io
npm install
```

## Tests

Tests run with `make test`. It runs the server tests that are aided by
the usage of `engine.io-client`.

Make sure `npm install` is run first.

## Goals

The main goal of `Engine` is ensuring the most reliable realtime communication.
Unlike the previous Socket.IO core, it always establishes a long-polling
connection first, then tries to upgrade to better transports that are "tested" on
the side.

During the lifetime of the Socket.IO projects, we've found countless drawbacks
to relying on `HTML5 WebSocket` or `Flash Socket` as the first connection
mechanisms.

Both are clearly the _right way_ of establishing a bidirectional communication,
with HTML5 WebSocket being the way of the future. However, to answer most business
needs, alternative traditional HTTP 1.1 mechanisms are just as good as delivering
the same solution.

WebSocket based connections have two fundamental benefits:

1. **Better server performance**
  - _A: Load balancers_<br>
      Load balancing a long polling connection poses a serious architectural nightmare
      since requests can come from any number of open sockets by the user agent, but
      they all need to be routed to the process and computer that owns the `Engine`
      connection. This negatively impacts RAM and CPU usage.
  - _B: Network traffic_<br>
      WebSocket is designed around the premise that each message frame has to be 
      surrounded by the least amount of data. In HTTP 1.1 transports, each message
      frame is surrounded by HTTP headers and chunked encoding frames. If you try to
      send the message _"Hello world"_ with xhr-polling, the message ultimately
      becomes larger than if you were to send it with WebSocket.
  - _C: Lightweight parser_<br>
      As an effect of **B**, the server has to do a lot more work to parse the network
      data and figure out the message when traditional HTTP requests are used
      (as in long polling). This means that another advantage of WebSocket is
      less server CPU usage.

2. **Better user experience**

    Due to the reasons stated in point **1**, the most important effect of being able
    to establish a WebSocket connection is raw data transfer speed, which translates
    in _some_ cases in better user experience.

    Applications with heavy realtime interaction (such as games) will benefit greatly,
    whereas applications like realtime chat (Gmail/Facebook), newsfeeds (Facebook) or
    timelines (Twitter) will have negligible user experience improvements.

Having said this, attempting to establish a WebSocket connection directly so far has
proven problematic:

1. **Proxies**<br>
    Many corporate proxies block WebSocket traffic.

2. **Personal firewall and antivirus software**<br>
    As a result of our research, we've found that at least 3 personal security
    applications block WebSocket traffic.

3. **Cloud application platforms**<br>
    Platforms like Heroku or No.de have had trouble keeping up with the fast-paced
    nature of the evolution of the WebSocket protocol. Applications therefore end up
    inevitably using long polling, but the seamless installation experience of 
    Socket.IO we strive for (_"require() it and it just works"_) disappears.

Some of these problems have solutions. In the case of proxies and personal programs,
however, the solutions many times involve upgrading software. Experience has shown
that relying on client software upgrades to deliver a business solution is
fruitless: the very existence of this project has to do with a fragmented panorama
of user agent distribution, with clients connecting with latest versions of the most
modern user agents (Chrome, Firefox and Safari), but others with versions as low as
IE 5.5.

From the user perspective, an unsuccessful WebSocket connection can translate in
up to at least 10 seconds of waiting for the realtime application to begin
exchanging data. This **perceptively** hurts user experience.

To summarize, **Engine** focuses on reliability and user experience first, marginal
potential UX improvements and increased server performance second. `Engine` is the
result of all the lessons learned with WebSocket in the wild.

## Architecture

The main premise of `Engine`, and the core of its existence, is the ability to
swap transports on the fly. A connection starts as xhr-polling, but it can
switch to WebSocket.

The central problem this poses is: how do we switch transports without losing
messages?

`Engine` only switches from polling to another transport in between polling
cycles. Since the server closes the connection after a certain timeout when
there's no activity, and the polling transport implementation buffers messages
in between connections, this ensures no message loss and optimal performance.

Another benefit of this design is that we workaround almost all the limitations
of **Flash Socket**, such as slow connection times, increased file size (we can
safely lazy load it without hurting user experience), etc.

## FAQ

### Can I use engine without Socket.IO ?

Absolutely. Although the recommended framework for building realtime applications
is Socket.IO, since it provides fundamental features for real-world applications 
such as multiplexing, reconnection support, etc.

`Engine` is to Socket.IO what Connect is to Express. An essential piece for building
realtime frameworks, but something you _probably_ won't be using for building
actual applications.

### Does the server serve the client?

No. The main reason is that `Engine` is meant to be bundled with frameworks.
Socket.IO includes `Engine`, therefore serving two clients is not necessary. If
you use Socket.IO, including

```html
<script src="/socket.io/socket.io.js">
```

has you covered.

### Can I implement `Engine` in other languages?

Absolutely. The [engine.io-protocol](https://github.com/LearnBoost/engine.io-protocol)
repository contains the most up to date description of the specification
at all times, and the parser implementation in JavaScript.

## License 

(The MIT License)

Copyright (c) 2014 Guillermo Rauch &lt;guillermo@learnboost.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

base64id
========

Node.js module that generates a base64 id.

Uses crypto.randomBytes when available, falls back to unsafe methods for node.js <= 0.4.

To increase performance, random bytes are buffered to minimize the number of synchronous calls to crypto.randomBytes.

## Installation

   $ npm install mongoose

## Usage

   var base64id = require('base64id');

   var id = base64id.generateId();
# ws: a node.js websocket library

[![Build Status](https://travis-ci.org/websockets/ws.svg?branch=master)](https://travis-ci.org/websockets/ws)

`ws` is a simple to use WebSocket implementation, up-to-date against RFC-6455,
and [probably the fastest WebSocket library for node.js][archive].

Passes the quite extensive Autobahn test suite. See http://websockets.github.com/ws
for the full reports.

## Protocol support

* **Hixie draft 76** (Old and deprecated, but still in use by Safari and Opera.
  Added to ws version 0.4.2, but server only. Can be disabled by setting the
  `disableHixie` option to true.)
* **HyBi drafts 07-12** (Use the option `protocolVersion: 8`)
* **HyBi drafts 13-17** (Current default, alternatively option `protocolVersion: 13`)

### Installing

```
npm install --save ws
```

### Sending and receiving text data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  ws.send('something');
});

ws.on('message', function(data, flags) {
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
});
```

### Sending binary data

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  var array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }

  ws.send(array, { binary: true, mask: true });
});
```

Setting `mask`, as done for the send options above, will cause the data to be
masked according to the WebSocket protocol. The same option applies for text
data.

### Server example

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});
```

### ExpressJS example

```js
var server = require('http').createServer()
  , url = require('url')
  , WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ server: server })
  , express = require('express')
  , app = express()
  , port = 4080;

app.use(function (req, res) {
  res.send({ msg: "hello" });
});

wss.on('connection', function connection(ws) {
  var location = url.parse(ws.upgradeReq.url, true);
  // you might use location.query.access_token to authenticate or share sessions
  // or ws.upgradeReq.headers.cookie (see http://stackoverflow.com/a/16395220/151312)
  
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  ws.send('something');
});

server.on('request', app);
server.listen(port, function () { console.log('Listening on ' + server.address().port) });
```

### Server sending broadcast data

```js
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    client.send(data);
  });
};
```

### Error handling best practices

```js
// If the WebSocket is closed before the following send is attempted
ws.send('something');

// Errors (both immediate and async write errors) can be detected in an optional
// callback. The callback is also the only way of being notified that data has
// actually been sent.
ws.send('something', function ack(error) {
  // if error is not defined, the send has been completed,
  // otherwise the error object will indicate what failed.
});

// Immediate errors can also be handled with try/catch-blocks, but **note** that
// since sends are inherently asynchronous, socket write failures will *not* be
// captured when this technique is used.
try { ws.send('something'); }
catch (e) { /* handle error */ }
```

### echo.websocket.org demo

```js
var WebSocket = require('ws');
var ws = new WebSocket('ws://echo.websocket.org/', {
  protocolVersion: 8, 
  origin: 'http://websocket.org'
});

ws.on('open', function open() {
  console.log('connected');
  ws.send(Date.now().toString(), {mask: true});
});

ws.on('close', function close() {
  console.log('disconnected');
});

ws.on('message', function message(data, flags) {
  console.log('Roundtrip time: ' + (Date.now() - parseInt(data)) + 'ms', flags);

  setTimeout(function timeout() {
    ws.send(Date.now().toString(), {mask: true});
  }, 500);
});
```

### Browserify users
When including ws via a browserify bundle, ws returns global.WebSocket which has slightly different API. 
You should use the standard WebSockets API instead.

https://developer.mozilla.org/en-US/docs/WebSockets/Writing_WebSocket_client_applications#Availability_of_WebSockets


### Other examples

For a full example with a browser client communicating with a ws server, see the
examples folder.

Note that the usage together with Express 3.0 is quite different from Express
2.x. The difference is expressed in the two different serverstats-examples.

Otherwise, see the test cases.

### Running the tests

```
make test
```

## API Docs

See [`/doc/ws.md`](https://github.com/websockets/ws/blob/master/doc/ws.md) for Node.js-like docs for the ws classes.

## Changelog

We're using the GitHub [`releases`](https://github.com/websockets/ws/releases) for changelog entries.

## License

(The MIT License)

Copyright (c) 2011 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[archive]: http://web.archive.org/web/20130314230536/http://hobbycoding.posterous.com/the-fastest-websocket-module-for-nodejs
# Ultron

[![Made by unshift](https://img.shields.io/badge/made%20by-unshift-00ffcc.svg?style=flat-square)](http://unshift.io)[![Version npm](http://img.shields.io/npm/v/ultron.svg?style=flat-square)](http://browsenpm.org/package/ultron)[![Build Status](http://img.shields.io/travis/unshiftio/ultron/master.svg?style=flat-square)](https://travis-ci.org/unshiftio/ultron)[![Dependencies](https://img.shields.io/david/unshiftio/ultron.svg?style=flat-square)](https://david-dm.org/unshiftio/ultron)[![Coverage Status](http://img.shields.io/coveralls/unshiftio/ultron/master.svg?style=flat-square)](https://coveralls.io/r/unshiftio/ultron?branch=master)[![IRC channel](http://img.shields.io/badge/IRC-irc.freenode.net%23unshift-00a8ff.svg?style=flat-square)](http://webchat.freenode.net/?channels=unshift)

Ultron is a high-intelligence robot. It gathers intelligence so it can start
improving upon his rudimentary design. It will learn your event emitting
patterns and find ways to exterminate them. Allowing you to remove only the
event emitters that **you** assigned and not the ones that your users or
developers assigned. This can prevent race conditions, memory leaks and even file
descriptor leaks from ever happening as you won't remove clean up processes.

## Installation

The module is designed to be used in browsers using browserify and in Node.js.
You can install the module through the public npm registry by running the
following command in CLI:

```
npm install --save ultron
```

## Usage

In all examples we assume that you've required the library as following:

```js
'use strict';

var Ultron = require('ultron');
```

Now that we've required the library we can construct our first `Ultron` instance.
The constructor requires one argument which should be the `EventEmitter`
instance that we need to operate upon. This can be the `EventEmitter` module
that ships with Node.js or `EventEmitter3` or anything else as long as it
follow the same API and internal structure as these 2. So with that in mind we
can create the instance:

```js
//
// For the sake of this example we're going to construct an empty EventEmitter
//
var EventEmitter = require('events').EventEmitter; // or require('eventmitter3');
var events = new EventEmitter();

var ultron = new Ultron(events);
```

You can now use the following API's from the Ultron instance:

### Ultron.on

Register a new event listener for the given event. It follows the exact same API
as `EventEmitter.on` but it will return itself instead of returning the
EventEmitter instance. If you are using EventEmitter3 it also supports the
context param:

```js
ultron.on('event-name', handler, { custom: 'function context' });
```

### Ultron.once

Exactly the same as the [Ultron.on](#ultronon) but it only allows the execution
once.

### Ultron.remove

This is where all the magic happens and the safe removal starts. This function
accepts different argument styles:

- No arguments, assume that all events need to be removed so it will work as
  `removeAllListeners()` API.
- 1 argument, when it's a string it will be split on ` ` and `,` to create a
  list of events that need to be cleared.
- Multiple arguments, we assume that they are all names of events that need to
  be cleared.

```js
ultron.remove('foo, bar baz');        // Removes foo, bar and baz.
ultron.remove('foo', 'bar', 'baz');   // Removes foo, bar and baz.
ultron.remove();                      // Removes everything.
```

If you just want to remove a single event listener using a function reference
you can still use the EventEmitter's `removeListener(event, fn)` API:

```js
function foo() {}

ulton.on('foo', foo);
events.removeListener('foo', foo);
```

## License

MIT
# options.js #

A very light-weight in-code option parsers for node.js.

## Usage ##

``` js
var Options = require("options");

// Create an Options object
function foo(options) {
        var default_options = {
                foo : "bar"
        };
        
        // Create an option object with default value
        var opts = new Options(default_options);
        
        // Merge options
        opts = opts.merge(options);
        
        // Reset to default value
        opts.reset();
        
        // Copy selected attributes out
        var seled_att = opts.copy("foo");
        
        // Read json options from a file. 
        opts.read("options.file"); // Sync
        opts.read("options.file", function(err){ // Async
                if(err){ // If error occurs
                        console.log("File error.");
                }else{
                        // No error
                }
        });
        
        // Attributes defined or not
        opts.isDefinedAndNonNull("foobar");
        opts.isDefined("foobar");
}

```


## License ##

(The MIT License)

Copyright (c) 2012 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# After [![Build Status][1]][2]

Invoke callback after n calls

## Status: production ready

## Example

    var after = require("after")
        , next = after(3, logItWorks)

    next()
    next()
    next() // it works

    function logItWorks() {
        console.log("it works!")
    }

## Example with error handling

    var after = require("after")
        , next = after(3, logError)

    next()
    next(new Error("oops")) // logs oops
    next() // does nothing

    function logError(err) {
        console.log(err)
    }

## After < 0.6.0

Older versions of after had iterators and flows in them.

These have been replaced with seperate modules

 - [iterators][8]
 - [composite][9]

## Installation

`npm install after`

## Tests

`npm test`

## Blog post

 - [Flow control in node.js][3]

## Examples :

 - [Determining the end of asynchronous operations][4]
 - [In javascript what are best practices for executing multiple asynchronous functions][5]
 - [JavaScript performance long running tasks][6]
 - [Synchronous database queries with node.js][7]

## Contributors

 - Raynos

## MIT Licenced

  [1]: https://secure.travis-ci.org/Raynos/after.png
  [2]: http://travis-ci.org/Raynos/after
  [3]: http://raynos.org/blog/2/Flow-control-in-node.js
  [4]: http://stackoverflow.com/questions/6852059/determining-the-end-of-asynchronous-operations-javascript/6852307#6852307
  [5]: http://stackoverflow.com/questions/6869872/in-javascript-what-are-best-practices-for-executing-multiple-asynchronous-functi/6870031#6870031
  [6]: http://stackoverflow.com/questions/6864397/javascript-performance-long-running-tasks/6889419#6889419
  [7]: http://stackoverflow.com/questions/6597493/synchronous-database-queries-with-node-js/6620091#6620091
  [8]: http://github.com/Raynos/iterators
  [9]: http://github.com/Raynos/composite
# How to
```javascript
var sliceBuffer = require('arraybuffer.slice');
var ab = (new Int8Array(5)).buffer;
var sliced = sliceBuffer(ab, 1, 3);
sliced = sliceBuffer(ab, 1);
```

# Licence (MIT)
Copyright (C) 2013 Rase-


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
has-binarydata.js
=================

Simple module to test if an object contains binary data

# isarray

`Array#isArray` for older browsers.

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
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
Blob
====

A module that exports a constructor that uses window.Blob when available, and a BlobBuilder with any vendor prefix in other cases. If neither is available, it exports undefined.

Usage:

```javascript
var Blob = require('blob');
var b = new Blob(['hi', 'constructing', 'a', 'blob']);
```

## Licence
MIT
# base64-arraybuffer

[![Build Status](https://travis-ci.org/niklasvh/base64-arraybuffer.png)](https://travis-ci.org/niklasvh/base64-arraybuffer)

Encode/decode base64 data into ArrayBuffers

## Getting Started
Install the module with: `npm install base64-arraybuffer`

## API
The library encodes and decodes base64 to and from ArrayBuffers

 - __encode(buffer)__ - Encodes `ArrayBuffer` into base64 string
 - __decode(str)__ - Decodes base64 string to `ArrayBuffer`

## Release History

 - 0.1.2 - Fix old format of typed arrays
 - 0.1.0 - Initial version, basic decode/encode base64 to and from ArrayBuffer

## License
Copyright (c) 2012 Niklas von Hertzen
Licensed under the MIT license.
# utf8.js [![Build status](https://travis-ci.org/mathiasbynens/utf8.js.svg?branch=master)](https://travis-ci.org/mathiasbynens/utf8.js) [![Code coverage status](http://img.shields.io/coveralls/mathiasbynens/utf8.js/master.svg)](https://coveralls.io/r/mathiasbynens/utf8.js) [![Dependency status](https://gemnasium.com/mathiasbynens/utf8.js.svg)](https://gemnasium.com/mathiasbynens/utf8.js)

_utf8.js_ is a well-tested UTF-8 encoder/decoder written in JavaScript. Unlike many other JavaScript solutions, it is designed to be a _proper_ UTF-8 encoder/decoder: it can encode/decode any scalar Unicode code point values, as per [the Encoding Standard](https://encoding.spec.whatwg.org/#utf-8). [Here’s an online demo.](https://mothereff.in/utf-8)

Feel free to fork if you see possible improvements!

## Installation

Via [npm](https://www.npmjs.org/):

```bash
npm install utf8
```

Via [Bower](http://bower.io/):

```bash
bower install utf8
```

Via [Component](https://github.com/component/component):

```bash
component install mathiasbynens/utf8.js
```

In a browser:

```html
<script src="utf8.js"></script>
```

In [Narwhal](http://narwhaljs.org/), [Node.js](https://nodejs.org/), and [RingoJS ≥ v0.8.0](http://ringojs.org/):

```js
var utf8 = require('utf8');
```

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('utf8.js');
```

Using an AMD loader like [RequireJS](http://requirejs.org/):

```js
require(
  {
    'paths': {
      'utf8': 'path/to/utf8'
    }
  },
  ['utf8'],
  function(utf8) {
    console.log(utf8);
  }
);
```

## API

### `utf8.encode(string)`

Encodes any given JavaScript string (`string`) as UTF-8, and returns the UTF-8-encoded version of the string. It throws an error if the input string contains a non-scalar value, i.e. a lone surrogate. (If you need to be able to encode non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
// U+00A9 COPYRIGHT SIGN; see http://codepoints.net/U+00A9
utf8.encode('\xA9');
// → '\xC2\xA9'
// U+10001 LINEAR B SYLLABLE B038 E; see http://codepoints.net/U+10001
utf8.encode('\uD800\uDC01');
// → '\xF0\x90\x80\x81'
```

### `utf8.decode(byteString)`

Decodes any given UTF-8-encoded string (`byteString`) as UTF-8, and returns the UTF-8-decoded version of the string. It throws an error when malformed UTF-8 is detected. (If you need to be able to decode encoded non-scalar values as well, use [WTF-8](https://mths.be/wtf8) instead.)

```js
utf8.decode('\xC2\xA9');
// → '\xA9'

utf8.decode('\xF0\x90\x80\x81');
// → '\uD800\uDC01'
// → U+10001 LINEAR B SYLLABLE B038 E
```

### `utf8.version`

A string representing the semantic version number.

## Support

utf8.js has been tested in at least Chrome 27-39, Firefox 3-34, Safari 4-8, Opera 10-28, IE 6-11, Node.js v0.10.0, Narwhal 0.3.2, RingoJS 0.8-0.11, PhantomJS 1.9.0, and Rhino 1.7RC4.

## Unit tests & code coverage

After cloning this repository, run `npm install` to install the dependencies needed for development and testing. You may want to install Istanbul _globally_ using `npm install istanbul -g`.

Once that’s done, you can run the unit tests in Node using `npm test` or `node tests/tests.js`. To run the tests in Rhino, Ringo, Narwhal, PhantomJS, and web browsers as well, use `grunt test`.

To generate the code coverage report, use `grunt cover`.

## FAQ

### Why is the first release named v2.0.0? Haven’t you heard of [semantic versioning](http://semver.org/)?

Long before utf8.js was created, the `utf8` module on npm was registered and used by another (slightly buggy) library. @ryanmcgrath was kind enough to give me access to the `utf8` package on npm when I told him about utf8.js. Since there has already been a v1.0.0 release of the old library, and to avoid breaking backwards compatibility with projects that rely on the `utf8` npm package, I decided the tag the first release of utf8.js as v2.0.0 and take it from there.

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

utf8.js is available under the [MIT](https://mths.be/mit) license.
# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT# ms.js: miliseconds conversion utility

```js
ms('1d')      // 86400000
ms('10h')     // 36000000
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
ms(ms('10 hours', { long: true }))    // "10 hours"
```

- Node/Browser compatible. Published as `ms` in NPM.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as
a number (e.g: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of
equivalent ms is returned.

## License

MIT# jQuery

> jQuery is a fast, small, and feature-rich JavaScript library.

For information on how to get started and how to use jQuery, please see [jQuery's documentation](http://api.jquery.com/).
For source files and issues, please visit the [jQuery repo](https://github.com/jquery/jquery).

## Including jQuery

Below are some of the most common ways to include jQuery.

### Browser

#### Script tag

```html
<script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
```

#### Babel

[Babel](http://babeljs.io/) is a next generation JavaScript compiler. One of the features is the ability to use ES6/ES2015 modules now, even though browsers do not yet support this feature natively.

```js
import $ from "jquery";
```

#### Browserify/Webpack

There are several ways to use [Browserify](http://browserify.org/) and [Webpack](https://webpack.github.io/). For more information on using these tools, please refer to the corresponding project's documention. In the script, including jQuery will usually look like this...

```js
var $ = require("jquery");
```

#### AMD (Asynchronous Module Definition)

AMD is a module format built for the browser. For more information, we recommend [require.js' documentation](http://requirejs.org/docs/whyamd.html).

```js
define(["jquery"], function($) {

});
```

### Node

To include jQuery in [Node](nodejs.org), first install with npm.

```sh
npm install jquery
```

For jQuery to work in Node, a window with a document is required. Since no such window exists natively in Node, one can be mocked by tools such as [jsdom](https://github.com/tmpvar/jsdom). This can be useful for testing purposes.

```js
require("jsdom").env("", function(err, window) {
	if (err) {
		console.error(err);
		return;
	}

	var $ = require("jquery")(window);
});
```
WebSocket Client & Server Implementation for Node
=================================================

[![npm version](https://badge.fury.io/js/websocket.svg)](http://badge.fury.io/js/websocket)

[![NPM Downloads](https://img.shields.io/npm/dm/websocket.svg)](https://www.npmjs.com/package/websocket)

[![NPM](https://nodei.co/npm/websocket.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/websocket/)

[![NPM](https://nodei.co/npm-dl/websocket.png?height=3)](https://nodei.co/npm/websocket/)

[ ![Codeship Status for theturtle32/WebSocket-Node](https://codeship.com/projects/70458270-8ee7-0132-7756-0a0cf4fe8e66/status?branch=master)](https://codeship.com/projects/61106)

Overview
--------
This is a (mostly) pure JavaScript implementation of the WebSocket protocol versions 8 and 13 for Node.  There are some example client and server applications that implement various interoperability testing protocols in the "test/scripts" folder.

For a WebSocket client written in ActionScript 3, see my [AS3WebScocket](https://github.com/theturtle32/AS3WebSocket) project.


Documentation
=============

[You can read the full API documentation in the docs folder.](docs/index.md)


Changelog
---------

***Current Version: 1.0.23*** — Released 2016-05-18***

***Version 1.0.23***

* Official support for Node 6.x
* Updating dependencies. Specifically, updating nan to ^2.3.3

***Version 1.0.22***

* Updating to work with nan 2.x


***Version 1.0.21***

* Incrememnted and re-published to work around an aborted npm publish of v1.0.20.

***Version 1.0.20***

* Added EventTarget to the W3CWebSocket interface (Thanks, [@ibc](https://github.com/ibc)!)
* Corrected an inaccurate error message. (Thanks, [@lekoaf](https://github.com/lekoaf)!)

***Version 1.0.19***

* Updated to nan v1.8.x (tested with v1.8.4)
* Added `"license": "Apache-2.0"` to package.json via [pull request #199](https://github.com/theturtle32/WebSocket-Node/pull/199) by [@pgilad](https://github.com/pgilad). See [npm1k.org](http://npm1k.org/).

[View the full changelog](CHANGELOG.md)

Browser Support
---------------

All current browsers are fully supported.

* Firefox 7-9 (Old) (Protocol Version 8)
* Firefox 10+ (Protocol Version 13)
* Chrome 14,15 (Old) (Protocol Version 8)
* Chrome 16+ (Protocol Version 13)
* Internet Explorer 10+ (Protocol Version 13)
* Safari 6+ (Protocol Version 13)

***Safari older than 6.0 is not supported since it uses a very old draft of WebSockets***

***If you need to simultaneously support legacy browser versions that had implemented draft-75/draft-76/draft-00, take a look here: https://gist.github.com/1428579***

Benchmarks
----------
There are some basic benchmarking sections in the Autobahn test suite.  I've put up a [benchmark page](http://theturtle32.github.com/WebSocket-Node/benchmarks/) that shows the results from the Autobahn tests run against AutobahnServer 0.4.10, WebSocket-Node 1.0.2, WebSocket-Node 1.0.4, and ws 0.3.4.

Autobahn Tests
--------------
The very complete [Autobahn Test Suite](http://autobahn.ws/testsuite/) is used by most WebSocket implementations to test spec compliance and interoperability.

- [View Server Test Results](http://theturtle32.github.com/WebSocket-Node/test-report/servers/)
- [View Client Test Results](http://theturtle32.github.com/WebSocket-Node/test-report/clients/)

Notes
-----
This library has been used in production on [worlize.com](https://www.worlize.com) since April 2011 and seems to be stable.  Your mileage may vary.

**Tested with the following node versions:**

- 6.2.0
- 5.11.1
- 4.4.4
- 0.10.45

It may work in earlier or later versions but I'm not actively testing it outside of the listed versions.  YMMV.

Installation
------------

A few users have reported difficulties building the native extensions without first manually installing node-gyp.  If you have trouble building the native extensions, make sure you've got a C++ compiler, and have done `npm install -g node-gyp` first. 

Native extensions are optional, however, and WebSocket-Node will work even if the extensions cannot be compiled.

In your project root:

    $ npm install websocket
  
Then in your code:

```javascript
var WebSocketServer = require('websocket').server;
var WebSocketClient = require('websocket').client;
var WebSocketFrame  = require('websocket').frame;
var WebSocketRouter = require('websocket').router;
var W3CWebSocket = require('websocket').w3cwebsocket;
```

Note for Windows Users
----------------------
Because there is a small C++ component used for validating UTF-8 data, you will need to install a few other software packages in addition to Node to be able to build this module:

- [Microsoft Visual C++](http://www.microsoft.com/visualstudio/en-us/products/2010-editions/visual-cpp-express)
- [Python 2.7](http://www.python.org/download/) (NOT Python 3.x)


Current Features:
-----------------
- Licensed under the Apache License, Version 2.0
- Protocol version "8" and "13" (Draft-08 through the final RFC) framing and handshake
- Can handle/aggregate received fragmented messages
- Can fragment outgoing messages
- Router to mount multiple applications to various path and protocol combinations
- TLS supported for outbound connections via WebSocketClient
- TLS supported for server connections (use https.createServer instead of http.createServer)
  - Thanks to [pors](https://github.com/pors) for confirming this!
- Cookie setting and parsing
- Tunable settings
  - Max Receivable Frame Size
  - Max Aggregate ReceivedMessage Size
  - Whether to fragment outgoing messages
  - Fragmentation chunk size for outgoing messages
  - Whether to automatically send ping frames for the purposes of keepalive
  - Keep-alive ping interval
  - Whether or not to automatically assemble received fragments (allows application to handle individual fragments directly)
  - How long to wait after sending a close frame for acknowledgment before closing the socket.
- [W3C WebSocket API](http://www.w3.org/TR/websockets/) for applications running on both Node and browsers (via the `W3CWebSocket` class). 


Known Issues/Missing Features:
------------------------------
- No API for user-provided protocol extensions.


Usage Examples
==============

Server Example
--------------

Here's a short example showing a server that echos back anything sent to it, whether utf-8 or binary.

```javascript
#!/usr/bin/env node
var WebSocketServer = require('websocket').server;
var http = require('http');

var server = http.createServer(function(request, response) {
    console.log((new Date()) + ' Received request for ' + request.url);
    response.writeHead(404);
    response.end();
});
server.listen(8080, function() {
    console.log((new Date()) + ' Server is listening on port 8080');
});

wsServer = new WebSocketServer({
    httpServer: server,
    // You should not use autoAcceptConnections for production
    // applications, as it defeats all standard cross-origin protection
    // facilities built into the protocol and the browser.  You should
    // *always* verify the connection's origin and decide whether or not
    // to accept it.
    autoAcceptConnections: false
});

function originIsAllowed(origin) {
  // put logic here to detect whether the specified origin is allowed.
  return true;
}

wsServer.on('request', function(request) {
    if (!originIsAllowed(request.origin)) {
      // Make sure we only accept requests from an allowed origin
      request.reject();
      console.log((new Date()) + ' Connection from origin ' + request.origin + ' rejected.');
      return;
    }
    
    var connection = request.accept('echo-protocol', request.origin);
    console.log((new Date()) + ' Connection accepted.');
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log('Received Message: ' + message.utf8Data);
            connection.sendUTF(message.utf8Data);
        }
        else if (message.type === 'binary') {
            console.log('Received Binary Message of ' + message.binaryData.length + ' bytes');
            connection.sendBytes(message.binaryData);
        }
    });
    connection.on('close', function(reasonCode, description) {
        console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.');
    });
});
```

Client Example
--------------

This is a simple example client that will print out any utf-8 messages it receives on the console, and periodically sends a random number.

*This code demonstrates a client in Node.js, not in the browser*

```javascript
#!/usr/bin/env node
var WebSocketClient = require('websocket').client;

var client = new WebSocketClient();

client.on('connectFailed', function(error) {
    console.log('Connect Error: ' + error.toString());
});

client.on('connect', function(connection) {
    console.log('WebSocket Client Connected');
    connection.on('error', function(error) {
        console.log("Connection Error: " + error.toString());
    });
    connection.on('close', function() {
        console.log('echo-protocol Connection Closed');
    });
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log("Received: '" + message.utf8Data + "'");
        }
    });
    
    function sendNumber() {
        if (connection.connected) {
            var number = Math.round(Math.random() * 0xFFFFFF);
            connection.sendUTF(number.toString());
            setTimeout(sendNumber, 1000);
        }
    }
    sendNumber();
});

client.connect('ws://localhost:8080/', 'echo-protocol');
```

Client Example using the *W3C WebSocket API*
--------------------------------------------

Same example as above but using the [W3C WebSocket API](http://www.w3.org/TR/websockets/).

```javascript
var W3CWebSocket = require('websocket').w3cwebsocket;

var client = new W3CWebSocket('ws://localhost:8080/', 'echo-protocol');

client.onerror = function() {
    console.log('Connection Error');
};

client.onopen = function() {
    console.log('WebSocket Client Connected');

    function sendNumber() {
        if (client.readyState === client.OPEN) {
            var number = Math.round(Math.random() * 0xFFFFFF);
            client.send(number.toString());
            setTimeout(sendNumber, 1000);
        }
    }
    sendNumber();
};

client.onclose = function() {
    console.log('echo-protocol Client Closed');
};

client.onmessage = function(e) {
    if (typeof e.data === 'string') {
        console.log("Received: '" + e.data + "'");
    }
};
```
    
Request Router Example
----------------------

For an example of using the request router, see `libwebsockets-test-server.js` in the `test` folder.


Resources
---------

A presentation on the state of the WebSockets protocol that I gave on July 23, 2011 at the LA Hacker News meetup.  [WebSockets: The Real-Time Web, Delivered](http://www.scribd.com/doc/60898569/WebSockets-The-Real-Time-Web-Delivered)
# typedarray-to-buffer [![travis][travis-image]][travis-url] [![npm][npm-image]][npm-url] [![downloads][downloads-image]][npm-url]

#### Convert a typed array to a [Buffer](https://github.com/feross/buffer) without a copy.

[![saucelabs][saucelabs-image]][saucelabs-url]

[travis-image]: https://img.shields.io/travis/feross/typedarray-to-buffer/master.svg
[travis-url]: https://travis-ci.org/feross/typedarray-to-buffer
[npm-image]: https://img.shields.io/npm/v/typedarray-to-buffer.svg
[npm-url]: https://npmjs.org/package/typedarray-to-buffer
[downloads-image]: https://img.shields.io/npm/dm/typedarray-to-buffer.svg
[saucelabs-image]: https://saucelabs.com/browser-matrix/typedarray-to-buffer.svg
[saucelabs-url]: https://saucelabs.com/u/typedarray-to-buffer

Say you're using the ['buffer'](https://github.com/feross/buffer) module on npm, or
[browserify](http://browserify.org/) and you're working with lots of binary data.

Unfortunately, sometimes the browser or someone else's API gives you a typed array like
`Uint8Array` to work with and you need to convert it to a `Buffer`. What do you do?

Of course: `new Buffer(uint8array)`

But, alas, every time you do `new Buffer(uint8array)` **the entire array gets copied**.
The `Buffer` constructor does a copy; this is
defined by the [node docs](http://nodejs.org/api/buffer.html) and the 'buffer' module
matches the node API exactly.

So, how can we avoid this expensive copy in
[performance critical applications](https://github.com/feross/buffer/issues/22)?

***Simply use this module, of course!***

If you have an `ArrayBuffer`, you don't need this module, because
`new Buffer(arrayBuffer)`
[is already efficient](https://nodejs.org/api/buffer.html#buffer_new_buffer_arraybuffer).

## install

```bash
npm install typedarray-to-buffer
```

## usage

To convert a typed array to a `Buffer` **without a copy**, do this:

```js
var toBuffer = require('typedarray-to-buffer')

var arr = new Uint8Array([1, 2, 3])
arr = toBuffer(arr)

// arr is a buffer now!

arr.toString()  // '\u0001\u0002\u0003'
arr.readUInt16BE(0)  // 258
```

## how it works

If the browser supports typed arrays, then `toBuffer` will **augment the typed array** you
pass in with the `Buffer` methods and return it. See [how does Buffer
work?](https://github.com/feross/buffer#how-does-it-work) for more about how augmentation
works.

This module uses the typed array's underlying `ArrayBuffer` to back the new `Buffer`. This
respects the "view" on the `ArrayBuffer`, i.e. `byteOffset` and `byteLength`. In other
words, if you do `toBuffer(new Uint32Array([1, 2, 3]))`, then the new `Buffer` will
contain `[1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0]`, **not** `[1, 2, 3]`. And it still doesn't
require a copy.

If the browser doesn't support typed arrays, then `toBuffer` will create a new `Buffer`
object, copy the data into it, and return it. There's no simple performance optimization
we can do for old browsers. Oh well.

If this module is used in node, then it will just call `new Buffer`. This is just for
the convenience of modules that work in both node and the browser.

## license

MIT. Copyright (C) [Feross Aboukhadijeh](http://feross.org).
# is-typedarray [![locked](http://badges.github.io/stability-badges/dist/locked.svg)](http://github.com/badges/stability-badges)

Detect whether or not an object is a
[Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays).

## Usage

[![NPM](https://nodei.co/npm/is-typedarray.png)](https://nodei.co/npm/is-typedarray/)

### isTypedArray(array)

Returns `true` when array is a Typed Array, and `false` when it is not.

## License

MIT. See [LICENSE.md](http://github.com/hughsk/is-typedarray/blob/master/LICENSE.md) for details.
# yaeti

Yet Another [EventTarget](https://developer.mozilla.org/es/docs/Web/API/EventTarget) Implementation.

The library exposes both the [EventTarget](https://developer.mozilla.org/es/docs/Web/API/EventTarget) interface and the [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event) interface.


## Installation

```bash
$ npm install yaeti --save
```


## Usage

```javascript
var yaeti = require('yaeti');


// Custom class we want to make an EventTarget.
function Foo() {
    // Make Foo an EventTarget.
    yaeti.EventTarget.call(this);
}

// Create an instance.
var foo = new Foo();

function listener1() {
    console.log('listener1');
}

function listener2() {
    console.log('listener2');
}
 
foo.addEventListener('bar', listener1);
foo.addEventListener('bar', listener2);
foo.removeEventListener('bar', listener1);

var event = new yaeti.Event('bar');

foo.dispatchEvent(event);


// Output:
// => "listener2"
```



## API


#### `yaeti.EventTarget` interface

Implementation of the [EventTarget](https://developer.mozilla.org/es/docs/Web/API/EventTarget) interface.

* Make a custom class inherit from `EventTarget`:
```javascript
function Foo() {
    yaeti.EventTarget.call(this);
}
```

* Make an existing object an `EventTarget`:
```javascript
yaeti.EventTarget.call(obj);
```

The interface implements the `addEventListener`, `removeEventListener` and `dispatchEvent` methods as defined by the W3C.


##### `listeners` read-only property

Returns an object whose keys are configured event types (String) and whose values are an array of listeners (functions) for those event types.


#### `yaeti.Event` interface

Implementation of the [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event) interface.

*NOTE:* Just useful in Node (the browser already exposes the native `Event` interface).

```javascript
var event = new yaeti.Event('bar');
```


## Author

[Iñaki Baz Castillo](https://github.com/ibc)


## License

[MIT](./LICENSE)
Native Abstractions for Node.js
===============================

**A header file filled with macro and utility goodness for making add-on development for Node.js easier across versions 0.8, 0.10, 0.12, 1, 4, 5 and 6.**

***Current version: 2.4.0***

*(See [CHANGELOG.md](https://github.com/nodejs/nan/blob/master/CHANGELOG.md) for complete ChangeLog)*

[![NPM](https://nodei.co/npm/nan.png?downloads=true&downloadRank=true)](https://nodei.co/npm/nan/) [![NPM](https://nodei.co/npm-dl/nan.png?months=6&height=3)](https://nodei.co/npm/nan/)

[![Build Status](https://api.travis-ci.org/nodejs/nan.svg?branch=master)](http://travis-ci.org/nodejs/nan)
[![Build status](https://ci.appveyor.com/api/projects/status/kh73pbm9dsju7fgh)](https://ci.appveyor.com/project/RodVagg/nan)

Thanks to the crazy changes in V8 (and some in Node core), keeping native addons compiling happily across versions, particularly 0.10 to 0.12 to 4.0, is a minor nightmare. The goal of this project is to store all logic necessary to develop native Node.js addons without having to inspect `NODE_MODULE_VERSION` and get yourself into a macro-tangle.

This project also contains some helper utilities that make addon development a bit more pleasant.

 * **[News & Updates](#news)**
 * **[Usage](#usage)**
 * **[Example](#example)**
 * **[API](#api)**
 * **[Tests](#tests)**
 * **[Governance & Contributing](#governance)**

<a name="news"></a>
## News & Updates

<a name="usage"></a>
## Usage

Simply add **NAN** as a dependency in the *package.json* of your Node addon:

``` bash
$ npm install --save nan
```

Pull in the path to **NAN** in your *binding.gyp* so that you can use `#include <nan.h>` in your *.cpp* files:

``` python
"include_dirs" : [
    "<!(node -e \"require('nan')\")"
]
```

This works like a `-I<path-to-NAN>` when compiling your addon.

<a name="example"></a>
## Example

Just getting started with Nan? Take a look at the **[Node Add-on Examples](https://github.com/nodejs/node-addon-examples)**.

Refer to a [quick-start **Nan** Boilerplate](https://github.com/fcanas/node-native-boilerplate) for a ready-to-go project that utilizes basic Nan functionality.

For a simpler example, see the **[async pi estimation example](https://github.com/nodejs/nan/tree/master/examples/async_pi_estimate)** in the examples directory for full code and an explanation of what this Monte Carlo Pi estimation example does. Below are just some parts of the full example that illustrate the use of **NAN**.

Yet another example is **[nan-example-eol](https://github.com/CodeCharmLtd/nan-example-eol)**. It shows newline detection implemented as a native addon.

Also take a look at our comprehensive **[C++ test suite](https://github.com/nodejs/nan/tree/master/test/cpp)** which has a plehora of code snippets for your pasting pleasure.

<a name="api"></a>
## API

Additional to the NAN documentation below, please consult:

* [The V8 Getting Started Guide](https://developers.google.com/v8/get_started)
* [The V8 Embedders Guide](https://developers.google.com/v8/embed)
* [V8 API Documentation](http://v8docs.nodesource.com/)
* [Node Add-on Documentation](https://nodejs.org/api/addons.html)

<!-- START API -->

### JavaScript-accessible methods

A _template_ is a blueprint for JavaScript functions and objects in a context. You can use a template to wrap C++ functions and data structures within JavaScript objects so that they can be manipulated from JavaScript. See the V8 Embedders Guide section on [Templates](https://developers.google.com/v8/embed#templates) for further information.

In order to expose functionality to JavaScript via a template, you must provide it to V8 in a form that it understands. Across the versions of V8 supported by NAN, JavaScript-accessible method signatures vary widely, NAN fully abstracts method declaration and provides you with an interface that is similar to the most recent V8 API but is backward-compatible with older versions that still use the now-deceased `v8::Argument` type.

* **Method argument types**
 - <a href="doc/methods.md#api_nan_function_callback_info"><b><code>Nan::FunctionCallbackInfo</code></b></a>
 - <a href="doc/methods.md#api_nan_property_callback_info"><b><code>Nan::PropertyCallbackInfo</code></b></a>
 - <a href="doc/methods.md#api_nan_return_value"><b><code>Nan::ReturnValue</code></b></a>
* **Method declarations**
 - <a href="doc/methods.md#api_nan_method"><b>Method declaration</b></a>
 - <a href="doc/methods.md#api_nan_getter"><b>Getter declaration</b></a>
 - <a href="doc/methods.md#api_nan_setter"><b>Setter declaration</b></a>
 - <a href="doc/methods.md#api_nan_property_getter"><b>Property getter declaration</b></a>
 - <a href="doc/methods.md#api_nan_property_setter"><b>Property setter declaration</b></a>
 - <a href="doc/methods.md#api_nan_property_enumerator"><b>Property enumerator declaration</b></a>
 - <a href="doc/methods.md#api_nan_property_deleter"><b>Property deleter declaration</b></a>
 - <a href="doc/methods.md#api_nan_property_query"><b>Property query declaration</b></a>
 - <a href="doc/methods.md#api_nan_index_getter"><b>Index getter declaration</b></a>
 - <a href="doc/methods.md#api_nan_index_setter"><b>Index setter declaration</b></a>
 - <a href="doc/methods.md#api_nan_index_enumerator"><b>Index enumerator declaration</b></a>
 - <a href="doc/methods.md#api_nan_index_deleter"><b>Index deleter declaration</b></a>
 - <a href="doc/methods.md#api_nan_index_query"><b>Index query declaration</b></a>
* Method and template helpers
 - <a href="doc/methods.md#api_nan_set_method"><b><code>Nan::SetMethod()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_prototype_method"><b><code>Nan::SetPrototypeMethod()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_accessor"><b><code>Nan::SetAccessor()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_named_property_handler"><b><code>Nan::SetNamedPropertyHandler()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_indexed_property_handler"><b><code>Nan::SetIndexedPropertyHandler()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_template"><b><code>Nan::SetTemplate()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_prototype_template"><b><code>Nan::SetPrototypeTemplate()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_instance_template"><b><code>Nan::SetInstanceTemplate()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_call_handler"><b><code>Nan::SetCallHandler()</code></b></a>
 - <a href="doc/methods.md#api_nan_set_call_as_function_handler"><b><code>Nan::SetCallAsFunctionHandler()</code></b></a>

### Scopes

A _local handle_ is a pointer to an object. All V8 objects are accessed using handles, they are necessary because of the way the V8 garbage collector works.

A handle scope can be thought of as a container for any number of handles. When you've finished with your handles, instead of deleting each one individually you can simply delete their scope.

The creation of `HandleScope` objects is different across the supported versions of V8. Therefore, NAN provides its own implementations that can be used safely across these.

 - <a href="doc/scopes.md#api_nan_handle_scope"><b><code>Nan::HandleScope</code></b></a>
 - <a href="doc/scopes.md#api_nan_escapable_handle_scope"><b><code>Nan::EscapableHandleScope</code></b></a>

Also see the V8 Embedders Guide section on [Handles and Garbage Collection](https://developers.google.com/v8/embed#handles).

### Persistent references

An object reference that is independent of any `HandleScope` is a _persistent_ reference. Where a `Local` handle only lives as long as the `HandleScope` in which it was allocated, a `Persistent` handle remains valid until it is explicitly disposed.

Due to the evolution of the V8 API, it is necessary for NAN to provide a wrapper implementation of the `Persistent` classes to supply compatibility across the V8 versions supported.

 - <a href="doc/persistent.md#api_nan_persistent_base"><b><code>Nan::PersistentBase & v8::PersistentBase</code></b></a>
 - <a href="doc/persistent.md#api_nan_non_copyable_persistent_traits"><b><code>Nan::NonCopyablePersistentTraits & v8::NonCopyablePersistentTraits</code></b></a>
 - <a href="doc/persistent.md#api_nan_copyable_persistent_traits"><b><code>Nan::CopyablePersistentTraits & v8::CopyablePersistentTraits</code></b></a>
 - <a href="doc/persistent.md#api_nan_persistent"><b><code>Nan::Persistent</code></b></a>
 - <a href="doc/persistent.md#api_nan_global"><b><code>Nan::Global</code></b></a>
 - <a href="doc/persistent.md#api_nan_weak_callback_info"><b><code>Nan::WeakCallbackInfo</code></b></a>
 - <a href="doc/persistent.md#api_nan_weak_callback_type"><b><code>Nan::WeakCallbackType</code></b></a>

Also see the V8 Embedders Guide section on [Handles and Garbage Collection](https://developers.google.com/v8/embed#handles).

### New

NAN provides a `Nan::New()` helper for the creation of new JavaScript objects in a way that's compatible across the supported versions of V8.

 - <a href="doc/new.md#api_nan_new"><b><code>Nan::New()</code></b></a>
 - <a href="doc/new.md#api_nan_undefined"><b><code>Nan::Undefined()</code></b></a>
 - <a href="doc/new.md#api_nan_null"><b><code>Nan::Null()</code></b></a>
 - <a href="doc/new.md#api_nan_true"><b><code>Nan::True()</code></b></a>
 - <a href="doc/new.md#api_nan_false"><b><code>Nan::False()</code></b></a>
 - <a href="doc/new.md#api_nan_empty_string"><b><code>Nan::EmptyString()</code></b></a>


### Converters

NAN contains functions that convert `v8::Value`s to other `v8::Value` types and native types. Since type conversion is not guaranteed to succeed, they return `Nan::Maybe` types. These converters can be used in place of `value->ToX()` and `value->XValue()` (where `X` is one of the types, e.g. `Boolean`) in a way that provides a consistent interface across V8 versions. Newer versions of V8 use the new `v8::Maybe` and `v8::MaybeLocal` types for these conversions, older versions don't have this functionality so it is provided by NAN.

 - <a href="doc/converters.md#api_nan_to"><b><code>Nan::To()</code></b></a>

### Maybe Types

The `Nan::MaybeLocal` and `Nan::Maybe` types are monads that encapsulate `v8::Local` handles that _may be empty_.

* **Maybe Types**
  - <a href="doc/maybe_types.md#api_nan_maybe_local"><b><code>Nan::MaybeLocal</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_maybe"><b><code>Nan::Maybe</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_nothing"><b><code>Nan::Nothing</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_just"><b><code>Nan::Just</code></b></a>
* **Maybe Helpers**
  - <a href="doc/maybe_types.md#api_nan_call"><b><code>Nan::Call()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_to_detail_string"><b><code>Nan::ToDetailString()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_to_array_index"><b><code>Nan::ToArrayIndex()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_equals"><b><code>Nan::Equals()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_new_instance"><b><code>Nan::NewInstance()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_function"><b><code>Nan::GetFunction()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_set"><b><code>Nan::Set()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_force_set"><b><code>Nan::ForceSet()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get"><b><code>Nan::Get()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_property_attribute"><b><code>Nan::GetPropertyAttributes()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_has"><b><code>Nan::Has()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_delete"><b><code>Nan::Delete()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_property_names"><b><code>Nan::GetPropertyNames()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_own_property_names"><b><code>Nan::GetOwnPropertyNames()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_set_prototype"><b><code>Nan::SetPrototype()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_object_proto_to_string"><b><code>Nan::ObjectProtoToString()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_has_own_property"><b><code>Nan::HasOwnProperty()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_has_real_named_property"><b><code>Nan::HasRealNamedProperty()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_has_real_indexed_property"><b><code>Nan::HasRealIndexedProperty()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_has_real_named_callback_property"><b><code>Nan::HasRealNamedCallbackProperty()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_real_named_property_in_prototype_chain"><b><code>Nan::GetRealNamedPropertyInPrototypeChain()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_real_named_property"><b><code>Nan::GetRealNamedProperty()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_call_as_function"><b><code>Nan::CallAsFunction()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_call_as_constructor"><b><code>Nan::CallAsConstructor()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_source_line"><b><code>Nan::GetSourceLine()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_line_number"><b><code>Nan::GetLineNumber()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_start_column"><b><code>Nan::GetStartColumn()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_get_end_column"><b><code>Nan::GetEndColumn()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_clone_element_at"><b><code>Nan::CloneElementAt()</code></b></a>
  - <a href="doc/maybe_types.md#api_nan_make_maybe"><b><code>Nan::MakeMaybe()</code></b></a>

### Script

NAN provides a `v8::Script` helpers as the API has changed over the supported versions of V8.

 - <a href="doc/script.md#api_nan_compile_script"><b><code>Nan::CompileScript()</code></b></a>
 - <a href="doc/script.md#api_nan_run_script"><b><code>Nan::RunScript()</code></b></a>


### Errors

NAN includes helpers for creating, throwing and catching Errors as much of this functionality varies across the supported versions of V8 and must be abstracted.

Note that an Error object is simply a specialized form of `v8::Value`.

Also consult the V8 Embedders Guide section on [Exceptions](https://developers.google.com/v8/embed#exceptions) for more information.

 - <a href="doc/errors.md#api_nan_error"><b><code>Nan::Error()</code></b></a>
 - <a href="doc/errors.md#api_nan_range_error"><b><code>Nan::RangeError()</code></b></a>
 - <a href="doc/errors.md#api_nan_reference_error"><b><code>Nan::ReferenceError()</code></b></a>
 - <a href="doc/errors.md#api_nan_syntax_error"><b><code>Nan::SyntaxError()</code></b></a>
 - <a href="doc/errors.md#api_nan_type_error"><b><code>Nan::TypeError()</code></b></a>
 - <a href="doc/errors.md#api_nan_throw_error"><b><code>Nan::ThrowError()</code></b></a>
 - <a href="doc/errors.md#api_nan_throw_range_error"><b><code>Nan::ThrowRangeError()</code></b></a>
 - <a href="doc/errors.md#api_nan_throw_reference_error"><b><code>Nan::ThrowReferenceError()</code></b></a>
 - <a href="doc/errors.md#api_nan_throw_syntax_error"><b><code>Nan::ThrowSyntaxError()</code></b></a>
 - <a href="doc/errors.md#api_nan_throw_type_error"><b><code>Nan::ThrowTypeError()</code></b></a>
 - <a href="doc/errors.md#api_nan_fatal_exception"><b><code>Nan::FatalException()</code></b></a>
 - <a href="doc/errors.md#api_nan_errno_exception"><b><code>Nan::ErrnoException()</code></b></a>
 - <a href="doc/errors.md#api_nan_try_catch"><b><code>Nan::TryCatch</code></b></a>


### Buffers

NAN's `node::Buffer` helpers exist as the API has changed across supported Node versions. Use these methods to ensure compatibility.

 - <a href="doc/buffers.md#api_nan_new_buffer"><b><code>Nan::NewBuffer()</code></b></a>
 - <a href="doc/buffers.md#api_nan_copy_buffer"><b><code>Nan::CopyBuffer()</code></b></a>
 - <a href="doc/buffers.md#api_nan_free_callback"><b><code>Nan::FreeCallback()</code></b></a>

### Nan::Callback

`Nan::Callback` makes it easier to use `v8::Function` handles as callbacks. A class that wraps a `v8::Function` handle, protecting it from garbage collection and making it particularly useful for storage and use across asynchronous execution.

 - <a href="doc/callback.md#api_nan_callback"><b><code>Nan::Callback</code></b></a>

### Asynchronous work helpers

`Nan::AsyncWorker` and `Nan::AsyncProgressWorker` are helper classes that make working with asynchronous code easier.

 - <a href="doc/asyncworker.md#api_nan_async_worker"><b><code>Nan::AsyncWorker</code></b></a>
 - <a href="doc/asyncworker.md#api_nan_async_progress_worker"><b><code>Nan::AsyncProgressWorkerBase & Nan::AsyncProgressWorker</code></b></a>
 - <a href="doc/asyncworker.md#api_nan_async_queue_worker"><b><code>Nan::AsyncQueueWorker</code></b></a>

### Strings & Bytes

Miscellaneous string & byte encoding and decoding functionality provided for compatibility across supported versions of V8 and Node. Implemented by NAN to ensure that all encoding types are supported, even for older versions of Node where they are missing.

 - <a href="doc/string_bytes.md#api_nan_encoding"><b><code>Nan::Encoding</code></b></a>
 - <a href="doc/string_bytes.md#api_nan_encode"><b><code>Nan::Encode()</code></b></a>
 - <a href="doc/string_bytes.md#api_nan_decode_bytes"><b><code>Nan::DecodeBytes()</code></b></a>
 - <a href="doc/string_bytes.md#api_nan_decode_write"><b><code>Nan::DecodeWrite()</code></b></a>


### Object Wrappers

The `ObjectWrap` class can be used to make wrapped C++ objects and a factory of wrapped objects.

 - <a href="doc/object_wrappers.md#api_nan_object_wrap"><b><code>Nan::ObjectWrap</code></b></a>


### V8 internals

The hooks to access V8 internals—including GC and statistics—are different across the supported versions of V8, therefore NAN provides its own hooks that call the appropriate V8 methods.

 - <a href="doc/v8_internals.md#api_nan_gc_callback"><b><code>NAN_GC_CALLBACK()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_add_gc_epilogue_callback"><b><code>Nan::AddGCEpilogueCallback()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_remove_gc_epilogue_callback"><b><code>Nan::RemoveGCEpilogueCallback()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_add_gc_prologue_callback"><b><code>Nan::AddGCPrologueCallback()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_remove_gc_prologue_callback"><b><code>Nan::RemoveGCPrologueCallback()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_get_heap_statistics"><b><code>Nan::GetHeapStatistics()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_set_counter_function"><b><code>Nan::SetCounterFunction()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_set_create_histogram_function"><b><code>Nan::SetCreateHistogramFunction()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_set_add_histogram_sample_function"><b><code>Nan::SetAddHistogramSampleFunction()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_idle_notification"><b><code>Nan::IdleNotification()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_low_memory_notification"><b><code>Nan::LowMemoryNotification()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_context_disposed_notification"><b><code>Nan::ContextDisposedNotification()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_get_internal_field_pointer"><b><code>Nan::GetInternalFieldPointer()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_set_internal_field_pointer"><b><code>Nan::SetInternalFieldPointer()</code></b></a>
 - <a href="doc/v8_internals.md#api_nan_adjust_external_memory"><b><code>Nan::AdjustExternalMemory()</code></b></a>


### Miscellaneous V8 Helpers

 - <a href="doc/v8_misc.md#api_nan_utf8_string"><b><code>Nan::Utf8String</code></b></a>
 - <a href="doc/v8_misc.md#api_nan_get_current_context"><b><code>Nan::GetCurrentContext()</code></b></a>
 - <a href="doc/v8_misc.md#api_nan_set_isolate_data"><b><code>Nan::SetIsolateData()</code></b></a>
 - <a href="doc/v8_misc.md#api_nan_get_isolate_data"><b><code>Nan::GetIsolateData()</code></b></a>
 - <a href="doc/v8_misc.md#api_nan_typedarray_contents"><b><code>Nan::TypedArrayContents</code></b></a>


### Miscellaneous Node Helpers

 - <a href="doc/node_misc.md#api_nan_make_callback"><b><code>Nan::MakeCallback()</code></b></a>
 - <a href="doc/node_misc.md#api_nan_module_init"><b><code>NAN_MODULE_INIT()</code></b></a>
 - <a href="doc/node_misc.md#api_nan_export"><b><code>Nan::Export()</code></b></a>

<!-- END API -->


<a name="tests"></a>
### Tests

To run the NAN tests do:

``` sh
npm install
npm run-script rebuild-tests
npm test
```

Or just:

``` sh
npm install
make test
```

<a name="governance"></a>
## Governance & Contributing

NAN is governed by the [io.js](https://iojs.org/) Addon API Working Group

### Addon API Working Group (WG)

The NAN project is jointly governed by a Working Group which is responsible for high-level guidance of the project.

Members of the WG are also known as Collaborators, there is no distinction between the two, unlike other io.js projects.

The WG has final authority over this project including:

* Technical direction
* Project governance and process (including this policy)
* Contribution policy
* GitHub repository hosting
* Maintaining the list of additional Collaborators

For the current list of WG members, see the project [README.md](./README.md#collaborators).

Individuals making significant and valuable contributions are made members of the WG and given commit-access to the project. These individuals are identified by the WG and their addition to the WG is discussed via GitHub and requires unanimous consensus amongst those WG members participating in the discussion with a quorum of 50% of WG members required for acceptance of the vote.

_Note:_ If you make a significant contribution and are not considered for commit-access log an issue or contact a WG member directly.

For the current list of WG members / Collaborators, see the project [README.md](./README.md#collaborators).

### Consensus Seeking Process

The WG follows a [Consensus Seeking](http://en.wikipedia.org/wiki/Consensus-seeking_decision-making) decision making model.

Modifications of the contents of the NAN repository are made on a collaborative basis. Anybody with a GitHub account may propose a modification via pull request and it will be considered by the WG. All pull requests must be reviewed and accepted by a WG member with sufficient expertise who is able to take full responsibility for the change. In the case of pull requests proposed by an existing WG member, an additional WG member is required for sign-off. Consensus should be sought if additional WG members participate and there is disagreement around a particular modification.

If a change proposal cannot reach a consensus, a WG member can call for a vote amongst the members of the WG. Simple majority wins.

<a id="developers-certificate-of-origin"></a>
## Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

* (a) The contribution was created in whole or in part by me and I
  have the right to submit it under the open source license
  indicated in the file; or

* (b) The contribution is based upon previous work that, to the best
  of my knowledge, is covered under an appropriate open source
  license and I have the right under that license to submit that
  work with modifications, whether created in whole or in part
  by me, under the same open source license (unless I am
  permitted to submit under a different license), as indicated
  in the file; or

* (c) The contribution was provided directly to me by some other
  person who certified (a), (b) or (c) and I have not modified
  it.

* (d) I understand and agree that this project and the contribution
  are public and that a record of the contribution (including all
  personal information I submit with it, including my sign-off) is
  maintained indefinitely and may be redistributed consistent with
  this project or the open source license(s) involved.

<a name="collaborators"></a>
### WG Members / Collaborators

<table><tbody>
<tr><th align="left">Rod Vagg</th><td><a href="https://github.com/rvagg">GitHub/rvagg</a></td><td><a href="http://twitter.com/rvagg">Twitter/@rvagg</a></td></tr>
<tr><th align="left">Benjamin Byholm</th><td><a href="https://github.com/kkoopa/">GitHub/kkoopa</a></td><td>-</td></tr>
<tr><th align="left">Trevor Norris</th><td><a href="https://github.com/trevnorris">GitHub/trevnorris</a></td><td><a href="http://twitter.com/trevnorris">Twitter/@trevnorris</a></td></tr>
<tr><th align="left">Nathan Rajlich</th><td><a href="https://github.com/TooTallNate">GitHub/TooTallNate</a></td><td><a href="http://twitter.com/TooTallNate">Twitter/@TooTallNate</a></td></tr>
<tr><th align="left">Brett Lawson</th><td><a href="https://github.com/brett19">GitHub/brett19</a></td><td><a href="http://twitter.com/brett19x">Twitter/@brett19x</a></td></tr>
<tr><th align="left">Ben Noordhuis</th><td><a href="https://github.com/bnoordhuis">GitHub/bnoordhuis</a></td><td><a href="http://twitter.com/bnoordhuis">Twitter/@bnoordhuis</a></td></tr>
<tr><th align="left">David Siegel</th><td><a href="https://github.com/agnat">GitHub/agnat</a></td><td>-</td></tr>
</tbody></table>

## Licence &amp; copyright

Copyright (c) 2016 NAN WG Members / Collaborators (listed above).

Native Abstractions for Node.js is licensed under an MIT license. All rights not explicitly granted in the MIT license are reserved. See the included LICENSE file for more details.
1to2 naively converts source code files from NAN 1 to NAN 2. There will be erroneous conversions,
false positives and missed opportunities. The input files are rewritten in place. Make sure that
you have backups. You will have to manually review the changes afterwards and do some touchups.

```sh
$ tools/1to2.js

  Usage: 1to2 [options] <file ...>

  Options:

    -h, --help     output usage information
    -V, --version  output the version number
```
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
# Add/Modify variable

Edit `configs_specs/configs/specs/config_spec.hpp`

- `CONFIG_DEFINE_TYPE` macro: declare a redemption type (forward declaration and more)
- `W.section(section_name, [&]{ /* members... */ })`
- `W.section(W.names(section_name, *::name{section_name}), [&]{ /* members... */ })`
- `W.member(spec_attr, sesman_io | connpolicy, log_policy, type, name[, desc][, default_value][, ...])`. Ordering value is not significant.
- `W.sep()`: empty line (human readable)



## Ini (spec::*)

- `spec::name{"variable name"}`
- `spec::type_<cpp_type>{}`


### log_policy (spec::constants::*)

- `loggable` (or `L` in const_spec.hpp)
- `unloggable` (or `NL` in const_spec.hpp)
- `unloggable_if_value_contains_password` (or `VNL` in const_spec.hpp)


### spec_attr (spec::constants::*)

- `no_ini_no_gui` incompatible with other value
- `ini_and_gui`
- `hidden_in_gui` incompatible with hex, advanced, iptable and password
- `hex_in_gui`
- `advanced_in_gui`
- `iptables_in_gui`
- `password_in_gui`

Note: special parameter: `connpolicy::allow_connpolicy_and_gui`.



## Sesman (sesman::*)

- `sesman::name{"variable name"}`
- `sesman::type_<cpp_type>{}`
- `sesman::connection_policy{name[, connpolicy_attr]}` enable connpolicy. Combinable with `connpolicy_attr`
- `sesman::deprecated_names{"name1", ...}` (sesman -> proxy for connpolicy only)


### sesman_io (sesman::constants::*)

- `no_sesman`
- `proxy_to_sesman`
- `sesman_to_proxy`
- `sesman_rw` (`proxy_to_sesman + sesman_to_proxy`)



## Connection Policy (connpolicy::*)

- `connpolicy::name{"variable name"}`
- `connpolicy::section{"name"}` overwrite section name


### connpolicy_attr (connpolicy::constants::*)

- `hex_in_connpolicy`
- `advanced_in_connpolicy`

Combination with `|`: `sesman::connection_policy{"rdp"} | advanced_in_connpolicy | hex_in_connpolicy`.



## Cpp (cpp::*)

- `cpp::name{"variable name"}`
- `cpp::type_<cpp_type>{}`
- `cpp::expr{"expr as string"}`
- `CPP_EXPR(expression)` (for macro: `CPP_EXPR(MACRO_NAME)`). equivalent to cpp::expr{#expression"}



## type

- `type_<cpp_type>()`: ini, sesman, connpolicy and cpp type
- `spec::type_<cpp_type>()`: ini type
- `sesman::type_<cpp_type>()`: connpolicy type
- `connpolicy::type_<cpp_type>()`: sesman type
- `cpp::type_<cpp_type>()`: cpp type

Note: `W.member(type_<int>(), sesman::type_<bool>(), ...)` is ok.

### special cpp_type

- `types::u16` instead of uint16_t
- `types::u32` instead of uint32_t
- `types::u64` instead of uint64_t
- `types::list<cpp_type>`: comma-separated values (cf: `0, 3, 4`)
- `types::ip_string`
- `types::dirpath`: always `/` terminated. Note: use `std::string` for file path type.
- `types::range<cpp_type, min, max>`
- `types::static_string`
- `types::fixed_string<n>`: size without zero-terminal.
- `types::fixed_binary<n>`: size without zero-terminal.



## name

- `char *`: ini, sesman, connpolicy and cpp name
- `spec::name`: ini name
- `sesman::name`: sesman name
- `cpp::name`: cpp name
- `connpolicy::name`: connection policy name

Note: `W.member("fish", sesman::name{"netfish"}, ini::name{"superfish"}, ...)` is ok.



## desc

- `desc{"desc..."}`



## default_value

- `set(CPP_EXPR(MACRO_NAME))`: instead of `MACRO_NAME` (cf: `set(CPP_MACRO(HASH_PATH)))`)
- `set(any_value)`
- `connpolicy::set(any_value)`

By default, initialized with `{}` (cf: `type value = {}`).


## prefix

- `prefix_value`: `prefix_value disable_prefix_val{"disable"}` in `const_spec.hpp`


# Add/Modify enumeration type

Edit `configs_specs/configs/specs/config_type.hpp`

```cpp
// enum { a = 1, b = 2, c = 4, ... }
e.enumeration_flags(enum_name[, enum_desc][, enum_info])
    [.set_string_parser()]
    .value(value_name[, value_desc])[.alias(alias_name)...]
    ...

// enum { a, b, c, ... }
e.enumeration_list(enum_name[, enum_desc][, enum_info])
    [.set_string_parser()]
    .value(value_name[, value_desc])[.alias(alias_name)...]
    ...

// enum { a = v1, b = v2, c = v3, ... }
e.enumeration_set(enum_name[, enum_desc][, enum_info])
    [.set_string_parser()]
    .value(value_name, integer_val[, value_desc])[.alias(alias_name)...]
    ...

// enum_info: description after values
// set_string_parser(): use a name parser instead of a value parser
```


# Build

```bash
bjam
```

or

```bash
bjam generate_cpp_enumeration
bjam generate_config_spec
```
# RDP Qt Client

Le ClientQtGraphicAPI est une couche graphique Qt pour client RDP qui assure l'affichage 
d'ordre de tracé RDP et capture les entrées souris et clavier.
Cette API est compatible avec un module de redemption (`mod_rdp`, `mod_vnc`...).

Un client Qt RDP utilisant cette API existe. Il permet de tester des connexions en utilisant
mod_rdp de façon simple et rapide en affichant. Ce client est également utile pour tester les
sous protocoles (copier/coller, partage de disque...).


## Interface graphique des fenêtre de l'API client

### La fenêtre de connexion

Un formulaire composé de 4 champs:

- `IP server`: renseigne l'IP de la cible.
- `User name`: renseigne le nom du user du compte de la cible.
- `Password`: renseigne le mot de passe du compte de la cible.
- `Port`: renseigne le port de connexion à la cible.

Et des boutons:

- `[Connection]` permet de lancer une connexion à une cible et d'ouvrir l'écran
de session.
- `[Replay]` permet de selectionner un film RDP en format `.mwrm` puis de le lire.
L'écran de session va alors s'ouvrir et afficher le contenu du film.
- `[Options]` permet d'ouvrir une fenêtre d'interface des options du client.
Cette fenêtre n'est pas contenu dans l'API et necessite d'être implémentée.


### L'écran de session

L'écran de session est une fenêtre qui permet d'afficher les ordres de tracé RDP et de capturer
les entrées claviers et souris de façon à reproduire une session RDP dont la taille s'adapte à la
résolution du client.

Il y a 3 boutons en bas de la fenêtre:

- `[CTRL + ALT + DELETE]` qui envoie le signale de la pression de ces 3 touches à
la session windows distante.
- `[Refresh]` envoie à la cible une requête de mise à jour de la totalité de l'écran.
- `[Disconnection]` deconnecte la session, ferme l'écran de session et fait un retour
sur le formulaire de connexion.

Lors de la lecture de film `.mwrm`, une barre de lecture horizontale permet de suivre la lecture
et de sauter à différent moment de la vidéo. Les boutons précedemment cités sont remplacés par
des boutons `[Play]`, `[Stop]` et `[Pause]`.


## Prerequies
	
Installer les lib Qt4 ou Qt5.

To compile ReDemPtion you need the following packages:
- libboost-tools-dev (contains bjam: software build tool) (http://sourceforge.net/projects/boost/files/boost/)
- libboost-test-dev (unit-test dependency)
- libssl-dev
- libkrb5-dev
- libsnappy-dev
- libpng12-dev
- libffmpeg-dev (see below)
- g++ >= 4.9 or clang++ >= 3.5 or other C++14 compiler


## Compilation du client Qt RDP

### Prerequies

- Installer les libs Qt4 ou Qt5.
- Installer les dépendances de redemption (`../../README.md`)


### Compilation

Pour le compiler il faut se placer dans le dossier `redemption/project/ClientQtGraphicAPI` (dossier de ce `README.md`):

Pour compiler avec la bibliothèque Qt4:

    bjam -s qt=4 client_rdp_Qt

Pour compiler avec la bibliothèque Qt5:

    bjam -s qt=5 client_rdp_Qt

Note: Les includes de Qt peuvent être configurés avec les variables d'environnement `QT4_INCLUDE`, `QT5_INCLUDE` et `QT5_PHONON_INCLUDE` depuis le shell avec `export` ou avec `-s` de bjam.

    bjam -s qt=5 -s QT4_INCLUDE=/usr/include/qt4 client_rdp_Qt

## Utilisation du client Qt RDP

//Le client Qt RDP contient une implementation de `mod_rdp` ainsi qu'une boite de dialogue
//pour renseigner les options de la session RDP.


### Virtual channels

Le client Qt RDP implémente plusieurs sous protocoles RDP passant par des cannaux virtuels:

- Le copier/coller
- Le partage de disque dur local
- Le canal son
- Le canal du partage de l'imprimante (n'est pas fonctionnel mais les logs sont implémentés)


### Lancement en ligne de commande de l'exe client_rdp_Qt4

Commandes de connexion:

	-u [user_name]     renseigne le nom de l'user du compte de la cible.
	-p [user_password] renseigne le mot de passe de l'user du compte de la cible.
	-i [target_IP]     resenigne l'adresse IP de la cible.
	-P [port]          renseigne le port de connexion à la cible.

Commandes verbose:

	--cliprdr 	    affiche le contenu des PDU reçu et envoyé par le client sur le channel du copier/coller.
	--cliprdr_dump idem que --cliprdr en ajoutant le dump des données brutes du PDU.
	--rdpdr        affiche le contenu des PDU reçu et envoyé par le client sur le channel du partage de disque.
	--rdpdr_dump   idem que --rdpdr en ajoutant le dump des données brutes du PDU.
	--rdpsnd       affiche le contenu des PDU reçu et envoyé par le client sur le channel son.
	--graphics	   affiche des informations sur les ordres de tracés reçus par le client.
	--printer      affiche le contenu des PDU reçu et envoyé par le client sur le channel de partage de l'imprimante(non implémenté).
	--basic_trace  affiche des logs du mod_rdp.
	--connection   affiche des logs du mod_rdp concernant la connexion à la cible.
	--rail_order   affiche les logs du rail order du mod_rdp.
	--asynchronous_task    affiche les logs des fonctions des tâches asynchrones du mod_rdp.
	--capabilities affiche les logs des capabilities lors de la négociation entre mod_rdp et cible.
	--keyboard     affiche les logs des entrées claviers.
	--rail         affiche les logs du cannal rail.
	--rail_dump    affiche les logs du cannal rail ainsi que le contenu brute des rail PDU.
	--remote_app
	--VNC


## Boite de dialogue des options du client Qt RDP

La boite de dialogue se divise en 4 onglets:

### Onglet "General":

- Permet d'enregistrer et de charger un profil d'option
- La checkbox "Record movie", si coché, les session seront enregistrées en format `.mwrm`
- La checkbox "TLS" active le TLS lors de la connexion
- La checkbox "NLA" active le NLA lors de la connexion

### Onglet "View":

- Des combobox permettent de selectionner la profondeur de couleur, le nombre d'écran
ainsi que la résolution.
- La checkbox "Span screen" adapte la taille de la fenêtre à celle du moniteur.
- la checkbox "Disable wallaper" permet de désactivé le fond d'écran de la cible
(pour raison de performance).

### Onglet "Services":

- Des checkbox permettent d'activer les cannaux virtuels de partage de disque et de copier/coller.
- Un champs permet de spécifier le fichier partagé par le protocole de partage de disque.

### Onglet "Keyboard":

- Une combobox permet de spécifier la langue du clavier
- Un tableau permet de configurer des touches du clavier (le Qt scan code et nécessaire
ainsi que le scan code ou le code ascii de la touche.
	

### Implémentation du client

Il suffit d'appeller le constructeur du client.

	ClientRedemption client_qt(argv, argc, verbose
		              , graphic_api_ptr
		              , clipboard_api_ptr
		              , sound_api_ptr
		              , socket_api_ptr
		              , control_api_ptr);


### La fonction "main" avec Qt

La fonction `main()` devra être de la forme suivante:

- Appel de `QApplication::QApplication(int argc, char** argv)`
- Appel du constructeur de votre classe front (celle qui hérite de `FrontQtRDPGraphicAPI`)
- Appel de `QApplication::exec()`

Exemple:

    int main(int argc, char** argv) {

	QApplication app(argc, argv);

        VotreFront votreFront();

        app.exec();
    }


### Compilation avec bjam

Dans le fichier
    `redemption/projects/ClientQtGraphicAPI/Jamroot`

Ajouter les lignes suivantes:

    obj [votre_fichier_main].o : [votre_fichier_main].cpp :
        <define>REDEMPTION_DECL_LOG_TEST
        $(EXE_DEPENDENCIES)
    ;

    exe votre_client_exe_Qt$(qtversion) :

	[votre_fichier_main].o

        [Optionnel: chemins vers les fichiers .hpp contenant des classes dérivées de QObject si vous en avez ajouté]
        [nom_du_fichier_qui_contient_votre_class_front.hpp]

        $(obj_list)
        $(lib_list)
        $(obj_list_VNC) # si necessaire
        config.o
        hexdump.o

        libqtclient
    :
        $(EXE_DEPENDENCIES)
    ;

Enfin, compiler votre client à l'aide de la commande suivante:

	bjam -s qt=$version votre_client_exe

# OCR

- Comment faire l'apprentissage sur un (nouveau) jeu de caractères ?
Les définitions de caractères sont dans learn.ok sous la forme de fichiers images .pbm
Les fichier .txt associé correspond au texte présent dans l'image.
Chaque caractères ou ensemble de caractères est séparer par un espace.
Note: '\' est un caractère d'échapement, le doubler pour le prendre en compte.

- Quel est la procédure de génération du module de reconnaissance de caractères ?
$ `make`
cette commande génère des fichier **.hxx** et les dossiers `classifiers` et `fonts`.
Les fichiers `{,classifiers/}*.hxx` sont utilisé par l'ocr.

/!\ **Ne pas oublier de modifier** `whitespace_width` **lorsqu'une police est ajoutée**.

En cas d'erreurs avec learning, display_learning permet de voir les caractères extrait.

- Comment lancer la reconnaissance de caractères sur une image fixe ?
Utiliser le programme extract_text. Celui-ci ne supporte que que les extensions ppm.
Note: Il existe des programmes comme bmptoppm ou pngtopnm dans le gestionnaire de paquets
(`pngtopnm file.png > file.pbm`).



# BUGS

Certains caractères sont reconnu en tant que plusieurs caractères.
(par exemple `ï` en Tahoma est reconnu en tant que  `.i.`).
Ceci est un "bug" de learning et la classification d'un tel caractère ammène une erreur.

Pour corriger le problème un fichier `nom_de_la_police.repl` doit être créé dans learn.ok.
Celui-ci contient les caractères de remplacement (code c++):

`{"sequence à trouver", "séquence de remplacement"},`



# Win 2012 et smoothing

`tools/ocr/img_win2012_smoothing_to_monochrome input_image output_image`
  transforme une image de barre de titre windows2012 standard en une image noir et blanc

`tools/ocr/img_win2012_smoothing_to_monochrome_d input_images`
  prend plusieurs fichier en paramètre et appel le script precédent avec une extension
  de sortie en .monochrome + en .pbm + un fichier .txt contenant le nom du fichier (il
  faut que le fichier soit nommé par les lettres dans l'image avec un espace séparateur
  entre chaque).
  À noter qu'il faut etre dans le dossier des images car le chemin complet est utilisé
  comme texte dans le fichier .txt

(Note: les couleurs en rdp et vnc sont différentes, pour avoir la liste complète des
couleurs consitutant une image: `identify -verbose -unique mon_image`.)

Questions OCR (OBSOLETE)
-----------------------

- Qu'est-ce que Milena ?

Milena est une bibliothèque générique de traitement d'image développée par le LRDE
(laboratoire de recherche dépendant de l'Epita). Milena fait partie du projet
Olena, et c'est aussi le nom des bibliothèques core d'Olena.

- Quels sont les codes livrés par l'Epita spécifiques à notre projet ?

La livraison de l'epita pour redemption comporte:
- Un Makefile -> a merger dans le Jamroot de redemption
- des fichiers README et INSTALL intégrés à OCR.txt (ce fichier) et supprimés.

- les jeux de définition de caractères : dossier learn.ok

- les fichiers source python suivants:

cart.py -> utilisé par classifieur
gen_classifier.py -> crée l'include classifier.hxx utilisé par classfier.hh
 gen_classifier utilise le contenu de features.txt, lui même construit à
 partir du contenu du dossier learn à l'aide du programme learning.

- les sources C++ suivant

classification.hh
classifier.hh
extract_bars.hh -> extraction des barres de titre d'une image
extract_text.cc
extract_text.hh -> extraction du texte contenu dans les barres de titre
learning.cc -> exploite le contenu de learn (image pbm et codes caractères) pour
            créer le fichier features.txt utilisé par gen_classifier.py


- Quels sont les codes générique Milena utilisés ?

L'OCR utilise la version de milena contenue dans le dossier milena, c'est à peu
de choses près [différences ?] la même chose que le contenu du dossier milena
de olena-1.0. L'archive olena-1.0 est conservée dans le dossier à titre de
référence, mais pas directement utilisée lors de la phase de compilation.

- Où sont les fichiers de définition de jeux de caractères ?

- Comment faire l'apprentissage sur un (nouveau) jeu de caractères ?

Les définitions de caractères sont dans learn (lien vers learn.ok) sous la forme
de fichiers images .pbm
Les fichier .txt associé correspond au texte présent dans l'image.
Chaque caractères ou ensemble de caractères est séparer par un espace.
Note: '\' est un caractère d'échapement, le doubler pour le prendre en compte.

- Quel est la procédure de génération du module de reconnaissance de caractères ?
make apprentissage

- Comment compiler Redemption avec le support de l'OCR ?

- Comment lancer la reconnaissance de caractères sur une image fixe ?
voir à "make test".

- Comment appeler la reconnaissance de caractères depuis un buffer ?



README ORIGINEL (OBSOLETE)
--------------------------

Commandes:
+ make all: compilation du programme et apprentissage.
+ make apprentissage: apprentissage seul à partir des fichiers dans
"learn"
+ make test: lancement de la procédure de test. Tout les screens se
trouvant dans le dossier "train" sont analysés puis traduit en texte.
+ make dist: génère une archive de rendu.


* extract_bars:
Détection des lignes de titres.

** Input: un screenshot ppm
** Output: plusieurs images titres pbm.
** Principe:
   + Calcul de composantes alpha-connexes à une couleur réference
   (alpha-connexion permet de gérer le dégradé)
   + Reconstruction de l'image ou on met en blanc le texte (est
   considéré comme texte tout ce qui est proche du blanc (pour l'aliasing)


* classify:
Découpage des caractères et classification.

** Input: une barre de titre
** Output: le texte du titre
** Principe:
   + calculs des composantes connexes et attributs (bbox, aire)
   + merge des composantes qui ont des points communs lors de la
   projection sur x (permet de gérer les accents)
   + classification

* classifier.cc_:
  L'arbre de décision généré.

* gen_classifier.py, cart.py:
  Construction de l'arbre de décision.
  Il faut mettre des fichiers pbm et leurs traductions dans le dossier
  "learn". Ensuite "make apprentissage" s'occupe de créer l'arbre de
  décision et créer le code c++ correspondant dans le fichier classifier.cc_.

* test.sh:
  Mettre tout plein de fichiers dans "train" et regarder les résultats
  dans "output"


* utilitaire

 recode utf-8..latin-1 < tmp > tmp2


 INSTALL ORIGINEL (OBSOLETE)
 ---------------------------

 INSTALLATION

	Instructions

I. Milena

1. Telecharger et installer milena
2. Modifier le makefile courrant pour indiquer le chemin de milena
3. Realiser l'apprentissage:
   make apprentissage


II. Integration

1. Aller dans le repertoire de redemption et compiler.
   cd integration
   make
2. Configurer utils/authhook.py puis
   python ./utils/authhook.py
   ./rdpproxy
# Dynamic analyzer

- `valgrind [-d binary-directory] [testnames...]`: run tests from `binary-directory` (bin/gcc/debug by default) with valgrind and print a little diagnostic error (see `./tools/valgrind-filter/valgrind-output-color` and `./tools/valgrind-filter/valgrind-ignore-ssl-snappy`).
- `bt [-hqsef] [--help] command [-- [gdb-args...]]`: show the backtrace with `gdb`.
- `gtrace [-cph] [--help] command [-- [gdb-args...]]`: show functions trace with `gdb`.
Ex: `./gtrace -c -- ./bin/gcc/debug/test_in_meta_sequence_transport -ex 'b test_in_meta_sequence_transport.cpp:340' | ./bt -fs`
- `gbt [-hcpqs] [--help] command line [-- [gdb-args...]]`: alias for `./gtrace [-cp] -n $command -- -ex "b $command_filename.cpp:$line" | ./bt -f[qs]`
- `tmalloc command [args]`: run command with libtmalloc (cf: `LD_PRELOAD=../tmalloc/libtmalloc.so`), see `./tools/tmalloc`.

# Static analyzer

- `cppcheck [cppcheck-args]`: run `cppcheck` on `main/*`.
- `cppcheck-full [cppcheck-args]`: run `cppcheck`.
- `scan-build [-h | jamdir [targers pattern-filter-cmd]]]`: run `scan-build` on each executable.
- `unused_files`: show unesed files (files without `#include`).
- `todo_extractor files...`: extract comment with BUG, ALERT, ATTENTION, DANGER, HACK, SECURITYFIXME, DEPRECATED, TASK, TODO, TBD, WARNING, CAUTION, NOTE, NOTICE, TEST, TESTING, PERFORMANCE, PERF

# Source corrector

- `clang-tidy [clang-tidy-args]`: run `clang-tidy`. Used `-fix` flag for fix detected errors.

# Sanitizers

- Add the ligne below at the end of your '.bashrc'.

alias bjam="ASAN_OPTIONS=detect_stack_use_after_return=1:detect_leaks=1 LSAN_OPTIONS=suppressions=./tools/c++-analyzer/suppr-leak-asan.txt bjam"

## ASan

 - help: `ASAN_OPTIONS=help=1 ./exe`
 - `export ASAN_OPTIONS=detect_stack_use_after_return=1:detect_leaks=1`

NOTE: `detect_stack_use_after_return=1` can be very slow.

## UBSan

http://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html

 -  `export UBSAN_OPTIONS=print_stacktrace=1:halt_on_error=1`

## Options

- Compile with -g and -fno-omit-frame-pointer
- `export UBSAN_OPTIONS=print_stacktrace=1`
- Make sure llvm-symbolizer binary is in PATH (example: `export ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-3.8/bin/llvm-symbolizer`).

# Utils

## include_tree

```bash
include_tree [-v filters='file1;file2'] [-v nolist=1] [-v notree=1] [-v oneline=1] [-v headeronly=1] files
```

### Examples

#### Zsh

```zsh
set extendedglob
./tools/c++-analyzer/include_tree -v oneline=1 src/**/*~src/keyboard*(^/) tests/includes/test-only/**/*(^/) tests/mod/rdp/test_rdp.cpp
```

#### Bash

```bash
find src -type f -exec ./tools/c++-analyzer/include_tree -v oneline=1 {} +
```
# Bash

In your `~/.bashrc`:

```bash
bf () {
  bjam "$@" 2>&1 \
  | stdbuf -o0 "$REDEMPTION_PATH"/tools/bjam/bjam_filter.awk \
    -v columns=$COLUMNS \
    -v "replacements=$PWD;;$HOME;" \
  | "$REDEMPTION_PATH"/tools/bjam/unit_test_color.sh
  return ${PIPESTATUS[0]}
}

pbf='REDEMPTION_LOG_PRINT=1 bf'

source $REDEMPTION_PATH/tools/bjam/bjam_completion.bash

# bf/pbf auto-completion
complete -F _bjam_completion bf pbf
```

# Zsh

In your `~/.zshrc`:

```bash
bf () {
  bjam "$@" 2>&1 \
  | stdbuf -o0 $REDEMPTION_PATH/tools/bjam/bjam_filter.awk \
    -v columns=$COLUMNS \
    -v "replacements=$PWD;;$HOME;" \
  | "$REDEMPTION_PATH"/tools/bjam/unit_test_color.sh
  return ${pipestatus[1]}
}

pbf='REDEMPTION_LOG_PRINT=1 bf'

source $REDEMPTION_PATH/tools/bjam/bjam_completion.zsh

# bf/pbf auto-completion
compctl -K _bjam_completion -M 'r:|[_/]=** r:|=*' bf
```
