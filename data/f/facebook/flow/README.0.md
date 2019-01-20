# Flow Documentation & Website

We use [Jekyll](http://jekyllrb.com/) to build the site.

## Installation

If you are working on the site, you will want to install and run a local copy
of it.

Start by cloning the website recursively to pull in all submodules:

```sh
git clone git@github.com:facebook/flow.git
```

### Dependencies

In order to use Jekyll, you will need to have Ruby installed. macOS comes
pre-installed with Ruby, but you may need to update RubyGems (via
`gem update --system`). Otherwise, [RVM](https://rvm.io/) and
[rbenv](https://github.com/sstephenson/rbenv) are popular ways to install Ruby.

- [Ruby](http://www.ruby-lang.org/) (version >= 1.8.7)
- [RubyGems](http://rubygems.org/) (version >= 1.3.7)
- [Bundler](http://bundler.io/)

The version of the Pygment syntax highlighter used by Jekyll requires Python
2.7.x (not 3.x). macOS comes pre-installed with Python 2.7, but you may need to
install it on other OSs.

- [Python](https://www.python.org) (version 2.7.x)

Once you have RubyGems and installed Bundler (via `gem install bundler`), use
it to install the dependencies:

```sh
$ cd website
$ bundle install
```

### Instructions

Use Jekyll to serve the website locally (by default, at
`http://localhost:8080`):

```sh
$ cd website
$ make
$ open http://127.0.0.1:8080/
```
# The Flow Parser

The Flow Parser is a JavaScript parser written in OCaml. It produces an AST that conforms to [SpiderMonkey's Parser API](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API) and that mostly matches what [esprima](http://esprima.org/) produces. The Flow Parser can be compiled to native code or can be compiled to JavaScript using [js_of_ocaml](http://ocsigen.org/js_of_ocaml/).

## Building the Flow Parser

Building the Flow Parser requires OCaml. Compiling to JavaScript requires js_of_ocaml >= 2.8.

### Initial set up

* [Install opam](https://opam.ocaml.org/doc/Install.html)
* `opam install js_of_ocaml`

### Building the OCaml Flow Parser library

    make
    
### Compiling the Flow Parser to JavaScript

    make js

## Tests

The Flow Parser's test suite tests the JavaScript version of the parser, so you will need js_of_ocaml installed. The tests and tools also have some node module dependencies, so you will need to run

### Initial set up

* Follow the steps in [Building the Flow Parser](https://github.com/facebook/flow/blob/master/src/parser/README.md#building-the-flow-parser)
* `npm install`

### Running the Tests

    make test
LZ4 - Library Files
================================

The `/lib` directory contains many files, but depending on project's objectives,
not all of them are necessary.

#### Minimal LZ4 build

The minimum required is **`lz4.c`** and **`lz4.h`**,
which provides the fast compression and decompression algorithm.
They generate and decode data using [LZ4 block format].


#### High Compression variant

For more compression ratio at the cost of compression speed,
the High Compression variant called **lz4hc** is available.
Add files **`lz4hc.c`** and **`lz4hc.h`**.
The variant still depends on regular `lib/lz4.*` source files.


#### Frame variant, for interoperability

In order to produce compressed data compatible with `lz4` command line utility,
it's necessary to encode lz4-compressed blocks using the [official interoperable frame format].
This format is generated and decoded automatically by the **lz4frame** library.
Its public API is described in `lib/lz4frame.h`.
In order to work properly, lz4frame needs all other modules present in `/lib`,
including, lz4 and lz4hc, and also **xxhash**.
So it's necessary to include all `*.c` and `*.h` files present in `/lib`.


#### Advanced / Experimental API

A complex API defined in `lz4frame_static.h` contains definitions
which are not guaranteed to remain stable in future versions.
As a consequence, it must be used with static linking ***only***.


#### Windows : using MinGW+MSYS to create DLL

DLL can be created using MinGW+MSYS with the `make liblz4` command.
This command creates `dll\liblz4.dll` and the import library `dll\liblz4.lib`.
The import library is only required with Visual C++.
The header files `lz4.h`, `lz4hc.h`, `lz4frame.h` and the dynamic library
`dll\liblz4.dll` are required to compile a project using gcc/MinGW.
The dynamic library has to be added to linking options.
It means that if a project that uses LZ4 consists of a single `test-dll.c`
file it should be linked with `dll\liblz4.dll`. For example:
```
    gcc $(CFLAGS) -Iinclude/ test-dll.c -o test-dll dll\liblz4.dll
```
The compiled executable will require LZ4 DLL which is available at `dll\liblz4.dll`.


#### Miscellaneous

Other files present in the directory are not source code. There are :

 - `LICENSE` : contains the BSD license text
 - `Makefile` : `make` script to compile and install lz4 library (static and dynamic)
 - `liblz4.pc.in` : for `pkg-config` (used in `make install`)
 - `README.md` : this file

[official interoperable frame format]: ../doc/lz4_Frame_format.md
[LZ4 block format]: ../doc/lz4_Block_format.md


#### License

All source material within __lib__ directory are BSD 2-Clause licensed.
See [LICENSE](LICENSE) for details.
The license is also reminded at the top of each source file.
dfind is a tool to quickly find what has changed in a directory.
It's a "difference finder".
The way it works

$ dfind your_directory your_handle

On the first call, it will give you all the files in this directory.

If you call dfind again with the same directory and the same handle,
it will only print the files that have changed.

Note that you can do: dfind -f, if you want to get the differences incrementally.

What happens under the hood:
If you are the first one to call dfind, it forks, and creates a server.
The dfind server is shared across all the users of the machine.
You can find the log in /tmp/dfind.log and the pid in /tmp/dfind.pid

NOTE: dfind is very dumb, and very conservative. It can give you MORE files that what has actually changed. But it will never give you less (unless there is a bug). The idea is to use dfind to narrow down the results, not to give and accurate view of the current state of the world.
# `./tool test`

`./tool` is a script in the root of this project. `./tool test` runs the tests in this directory.

To make it work: run `yarn install` in the flow directory. This is needed both for `tool` to run, and also for `flow check` to work in the newtests directory.

## Motivation behind `./tool test`

* Tests should pair small examples with the expectations for each example.
* We should dogfood Flow

## Example test

Check out [tool_test_example](https://github.com/facebook/flow/blob/master/newtests/tool_test_example/test.js), which is an example test.

## Structure of a test

* A test is a file named `./**/test.js`.
* Each `test.js` file exports a `Suite` by default
* Each `Suite` contains a list of `Test`s.
* Each `Test` contains a list of `TestSteps`

### Exporting a `Suite`

The only way to create a `Suite` is to call the `suite()` function. The `suite()` function takes a callback, like so

```JavaScript
import {suite} from 'flow-dev-tools/src/test/Tester';
import type TestStep from 'flow-dev-tools/src/test/TestStep';
export default suite((emptyTestStep: TestStep) => [ < List of Tests >]);
```

(Why the `suite()` function? Why not just export the callback directly? Well, it removes the need for type annotations!)

### Creating a `Test`

The only way to create a `Test` is to call the `test()` function. The `test()` function takes a test name and a list of `TestStep`s, like so

```JavaScript
import {suite, test} from 'flow-dev-tools/src/test/Tester';
import type TestStep from 'flow-dev-tools/src/test/TestStep';
export default suite((emptyTestStep: TestStep) => [
  test('My first test, [ < List of TestSteps > ]'),
]);
```

### `TestStep`s

A `TestStep` is made up of 0 or more actions and 0 or more assertions. The `emptyTestStep` passed to `suite()`'s callback is a `TestStep` with 0 actions and 0 assertions. `TestStep`s are immutable, so when you call `emptyTestStep.addFile('foo.js')` you get back a new `TestStep` with 1 action and 0 assertions. So a test looks like

```JavaScript
import {suite, test} from 'flow-dev-tools/src/test/Tester';
import type TestStep from 'flow-dev-tools/src/test/TestStep';
export default suite((emptyTestStep: TestStep) => [
  test('My first test', [
    emptyTestStep
      .addCode('var x = 123')
      .noNewErrors(),
    emptyTestStep
      .addCode('var y = "hello"')
      .noNewErrors(),
  ]),
]);
```

More concisely, this can be written

```JavaScript
import {suite, test} from 'flow-dev-tools/src/test/Tester';
export default suite(({addCode}) => [
  test('My first test', [
    addCode('var x = 123')
      .noNewErrors(),
    addCode('var y = "hello"')
      .noNewErrors(),
  ]),
]);
```

Note: You cannot add actions to a `TestStep` after an assertion because @gabelevi felt like messing around with the type system to prevent it :)
# The flow-parser package

This package contains the Flow parser in its compiled-to-JavaScript form.

# What is Flow

See [flow.org](https://flow.org/). The code for the Flow parser [lives on GitHub](https://github.com/facebook/flow/tree/master/src/parser).

# What is the Flow Parser

The Flow Parser is a JavaScript parser written in OCaml. It produces an AST that conforms to the [ESTree spec](https://github.com/estree/estree) and that mostly matches what [esprima](http://esprima.org/) produces. The Flow Parser can be compiled to native code or can be compiled to JavaScript using [js_of_ocaml](http://ocsigen.org/js_of_ocaml/). This npm package contains the Flow parser compiled to JavaScript.

# Usage

You can use the Flow parser in your browser or in node. To use in node you can just do

```JavaScript
require('flow-parser').parse('1+1', {});
```

To use in the browser, you can add

```HTML
<script src="flow_parser.js"></script>
```

which will make the `flow` object available to use like so:

```JavaScript
flow.parse('1+1', {});
```

## Options

The second argument to `flow.parse` is the options object. Currently supported options:

* `esproposal_decorators` (boolean, default `false`) - enable parsing of decorators
* `esproposal_class_instance_fields` (boolean, default `false`) - enable parsing of class instance fields
* `esproposal_class_static_fields` (boolean, default `false`) - enable parsing of class static fields
* `esproposal_export_star_as` (boolean, default `false`) - enable parsing of `export * as` syntax
* `esproposal_optional_chaining` (boolean, default `false`) - enable parsing of optional chaining (`?.`)
* `esproposal_nullish_coalescing` (boolean, default `false`) - enable parsing of nullish coalescing (`??`)
* `types` (boolean, default `true`) - enable parsing of Flow types
# `flow-upgrade`

A utility for upgrading your codebase to the latest version of Flow.

To run this utility to upgrade your codebase you can use [`yarn create`][]:

[`yarn create`]: https://yarnpkg.com/en/docs/cli/create#search

```
yarn create flow-upgrade
```

This is a shorter version which is equivalent to:

```
yarn global add flow-upgrade
flow-upgrade
```

You may also use [`npx`][]:

[`npx`]: https://www.npmjs.com/package/npx

```
npx flow-upgrade
```

## Options

By default, Flow will only upgrade files that have an `// @flow` header comment.
If you want to upgrade all of your JavaScript files you may pass in the `--all`:

```
yarn create flow-upgrade --all
```
# Testgen
This project is a test generator for type checkers such as Flow. It
generates programs with runtime checks, feeds them to a type checker
and runs those programs to see if the type checker will reject bad
programs.

## Building Testgen
To build the executable, run `make`.

## Extending Testgen
`ruleset_base.ml` contains a lot of rules used to generate
programs. However, to accomplish a certain task, one might not want to
use all those rules. Instead, a recommended way to do that is to
inherit the `ruleset_base` class, pick the necessary rules and
possibly overwrite those methods. 

Here are the steps to extend the 
base ruleset and `ruleset_optional.ml`, `ruleset_func.ml`,
`ruleset_depth.ml`, `ruleset_union.ml` and `ruleset_exact.ml` serve as
examples for this extension:

0. Suppose you want to test exact object types and want to generate
   some programs related to exact object types. (`ruleset_exact.ml`
   has all the code)
1. Copy one of the children class of base ruleset, say,
   `ruleset_depth.ml` to `ruleset_exact.ml`. Make classname
   adjustments in there appropriately.
2. Modify the build file
3. Then, in `codegen.ml`, add `ruleset_exact` as one of the engines
4. Compile the program and run
 
## Running Testgen
In the folder where binary lives, run the program once to let it
generate an initial config file called `flowtestgen.json.` Then edit
`flowtestgen.json` to up the number of trials `(num_prog)`. The
typecheck flag controls whether Flow is invoked or not.
Log_to_console controls prints programs to console.

To try random searching,  each ruleset has a random version of that
class as well at the bottom of the file.
