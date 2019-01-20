# Dirac DevTools

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](license.txt) 
[![Clojars Project](https://img.shields.io/clojars/v/binaryage/dirac.svg)](https://clojars.org/binaryage/dirac) 
[![Travis](https://img.shields.io/travis/binaryage/dirac/master.svg)](https://travis-ci.org/binaryage/dirac) 
[![Sample Project](https://img.shields.io/badge/project-example-ff69b4.svg)](https://github.com/binaryage/dirac-sample) 
[![Chrome Extension](https://img.shields.io/badge/chrome-extension-ebb338.svg)](https://chrome.google.com/webstore/detail/dirac-devtools/kbkdngfljkchidcjpnfcgcokkbhlkogi)

Dirac is a [Chrome DevTools][1] fork with extra features for ClojureScript developers.

**TOC** 
: **[Introduction](#introduction)**
| **[Screenshots](#screenshots)**

**DOC** 
: **[Motivation](docs/motivation.md)**
| **[Installation](docs/installation.md)**
| **[Upgrading](docs/upgrading.md)**
| **[Configuration](docs/configuration.md)**
| **[Integration](docs/integration.md)**
| **[Example project](https://github.com/binaryage/dirac-sample)**
| **[FAQ](docs/faq.md)**

### Introduction

Dirac project maintains [a set of patches][2] rolling on top of official Chrome DevTools.
That means you don't lose any functionality, you just add ClojureScript support on top.
Additionally we provide [a Chrome Extension][3] which packages this enhanced DevTools version and hosts it within Chrome for convenient access.
Dirac DevTools can be just a keystroke away enabling following features:

  * ClojureScript-aware REPL integrated into DevTools Javascript console
    * can eval ClojureScript in the context of currently selected stack frame (when paused on a breakpoint)
    * ClojureScript [code completion suggestions][4] (like completions in Javascript console)
    * [Parinfer][5] goodness
    * adds a global keyboard shortcut for focusing the console prompt
  * enables [custom formatters][6] by default (for [cljs-devtools][7])
     * custom formatters are displayed inline on Source Panel (during debugging)
  * better [display of ClojureScript function names][8]
  * improved display of URLs
  * better display of ClojureScript property names:
    * macro-generated names are renamed to friendly names using sub-indexes
    * properties are grouped, the most important properties go first

### Screenshots

![ClojureScript REPL][9]

<table>
<tr>
<td><a href="https://box.binaryage.com/dirac-general-completions.png"><img src="https://box.binaryage.com/dirac-general-completions.png"></a></td>
<td><a href="https://box.binaryage.com/dirac-ns-completions.png"><img src="https://box.binaryage.com/dirac-ns-completions.png"></a></td>
<td><a href="https://box.binaryage.com/dirac-js-completions.png"><img src="https://box.binaryage.com/dirac-js-completions.png"></a></td>
</tr>
</table>

[1]: https://developer.chrome.com/devtools
[2]: https://github.com/binaryage/dirac/commit/devtools-diff
[3]: https://chrome.google.com/webstore/detail/dirac-devtools/kbkdngfljkchidcjpnfcgcokkbhlkogi
[4]: https://github.com/binaryage/dirac/releases/tag/v0.4.0
[5]: https://shaunlebron.github.io/parinfer
[6]: https://docs.google.com/document/d/1FTascZXT9cxfetuPRT2eXPQKXui4nWFivUnS_335T3U
[7]: https://github.com/binaryage/cljs-devtools
[8]: https://box.binaryage.com/dirac-non-trivial-beautified-stack-trace.png
[9]: https://box.binaryage.com/dirac-main-01.png
this code was taken from https://github.com/semperos/clj-webdriver/releases/tag/v0.7.2

see https://github.com/semperos/clj-webdriver

* Clj-webdriver is distributed under the Eclipse Public License, the same as Clojure.
This folder is intentionally left empty (no sources).

It is used in project.clj to work around some unwanted cljsbuild behaviour.# Chrome DevTools frontend

<!-- [START badges] -->
[![NPM package](https://img.shields.io/npm/v/chrome-devtools-frontend.svg)](https://npmjs.org/package/chrome-devtools-frontend)
<!-- [END badges] -->

The client-side of the Chrome DevTools, including all JS & CSS to run the DevTools webapp.

It is available on NPM as the [chrome-devtools-frontend](https://www.npmjs.com/package/chrome-devtools-frontend) package. It's not currently available via CJS or ES2015 modules, so consuming this package in other tools may require [some effort](https://github.com/paulirish/devtools-timeline-model/blob/master/index.js).

#### Package versioning
The version number of the npm package (e.g. `1.0.373466`) refers to the Chromium commit position of latest frontend git commit. It's incremented with every Chromium commit, however the package is updated roughly daily.

### Source code
The frontend is available through a git subtree mirror on [chromium.googlesource.com](https://chromium.googlesource.com/chromium/src/third_party/blink/renderer/devtools/), with a regularly updating GitHub mirror at [github.com/ChromeDevTools/devtools-frontend](https://github.com/ChromeDevTools/devtools-frontend). The codebase's true location is in `third_party/blink/renderer/devtools/` in [Chromium's git repo](https://chromium.googlesource.com/chromium/src/).

### Getting Started

1. Clone the repo
2. Go to repo root and run:  `npm start`
    - This launches Chrome Canary and starts the dev server with 1 command
3. Go to http://localhost:9222#custom=true&experiments=true

> **Power user tips:**
>
> You can customize the port for the dev server: e.g. `PORT=8888 npm start`.
>
> You can also launch chrome and start the server separately:
> - `npm run chrome`
> - `npm run server`
>
> When you start Chrome separately, you can pass extra args to Chrome:
> ```
> npm run chrome -- https://news.ycombinator.com
> ```
> (e.g. this launches Hacker News on startup)
>
> If you want to reset your development profile for Chrome, pass in "--reset-profile":
> ```
> npm start -- --reset-profile
> ```
> *OR*
> ```
> npm run chrome -- --reset-profile
> ```

### Hacking
* DevTools documentation: [devtools.chrome.com](https://devtools.chrome.com)
* [Debugging protocol docs](https://developer.chrome.com/devtools/docs/debugger-protocol) and [Chrome Debugging Protocol Viewer](http://chromedevtools.github.io/debugger-protocol-viewer/)
* [awesome-chrome-devtools](https://github.com/paulirish/awesome-chrome-devtools): recommended tools and resources
* Contributing to DevTools: [bit.ly/devtools-contribution-guide](http://bit.ly/devtools-contribution-guide)
* Contributing To Chrome DevTools Protocol: [docs.google.com](https://docs.google.com/document/d/1c-COD2kaK__5iMM5SEx-PzNA7HFmgttcYfOHHX0HaOM/edit?usp=sharing)

### Useful Commands

#### Simpler npm commands w/ `dtrun`
If you want to run these npm commands anywhere in the chromium repo (e.g. in chromium/src), you'll want to setup our `dtrun` CLI helper.

One-time setup:
```
npm run setup-dtrun
```

Now, you can use any of the following commands by simply doing: `dtrun test`. 

In addition, you no longer need to pass double dashes (e.g. `--`) before you pass in the flags. So you can do: `dtrun test -d inspector/test.html`.

#### `npm run format` 
Formats your code using clang-format

### `npm run format-py`
Formats your Python code using [yapf](https://github.com/google/yapf)

> Note: Yapf is a command line tool. You will have to install this manually, either from PyPi through `pip install yapf` or if you want to enable multiprocessing in Python 2.7, `pip install futures`

#### `npm test`
Builds devtools and runs all inspector/devtools web tests.

> Note: If you're using a full chromium checkout and compiled content shell in out/Release, then `npm test` uses that. Otherwise, with only a front-end checkout (i.e. cloning from GitHub), then `npm test` will fetch a previously compiled content shell from the cloud (and cache it for future test runs).

#### `npm test` basics
```
# run specific tests
npm test -- inspector/sources inspector/console

# debug a specific test. Any one of:
npm run debug-test inspector/cookie-resource-match.html
npm test -- --debug-devtools inspector/cookie-resource-match.html 
npm test -- -d inspector/cookie-resource-match.html 

# pass in additional flags to the test harness
npm test -- -f --child-processes=16

# ...for example, use a higher test timeout
npm test -- --time-out-ms=6000000 <test_path>
```

> **Tip**: [Learn about the test harness flags](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_tests.md#Test-Harness-Options)

#### `--fetch-content-shell`
```
# If you're using a full chromium checkout and have a compiled content shell, 
# this will fetch a pre-compiled content shell. This is useful if you 
# haven't compiled your content shell recently
npm test -- --fetch-content-shell
```

#### `--target=SUB_DIRECTORY_NAME`
```
# If you're using a build sub-directory that's not out/Release, 
# such as out/Default, then use --target=SUB_DIRECTORY_NAME
npm test -- --target=Default
```
### Development
* All devtools commits: [View the log], [RSS feed] or [@DevToolsCommits] on Twitter
* [All open DevTools tickets] on crbug.com
* File a new DevTools ticket: [new.crbug.com](https://bugs.chromium.org/p/chromium/issues/entry?labels=OS-All,Type-Bug,Pri-2&components=Platform%3EDevTools)
* Code reviews mailing list: [devtools-reviews@chromium.org]

### Getting in touch
* [@ChromeDevTools] on Twitter
* Chrome DevTools mailing list: [groups.google.com/forum/google-chrome-developer-tools](https://groups.google.com/forum/#!forum/google-chrome-developer-tools)

  [devtools-reviews@chromium.org]: https://groups.google.com/a/chromium.org/forum/#!forum/devtools-reviews
  [RSS feed]: https://feeds.peter.sh/chrome-devtools/
  [View the log]: https://chromium.googlesource.com/chromium/src/third_party/blink/renderer/devtools/+log/master
  [@ChromeDevTools]: http://twitter.com/ChromeDevTools
  [@DevToolsCommits]: http://twitter.com/DevToolsCommits
  [all open DevTools tickets]: https://bugs.chromium.org/p/chromium/issues/list?can=2&q=component%3APlatform%3EDevTools&sort=&groupby=&colspec=ID+Stars+Owner+Summary+Modified+Opened
## Adding new icons

1. Use Inkscape 0.92 or newer.
1. Choose an existing spritesheet, like `largeIcons.svg` to add the icon to
1. Open that file with Inkscape and import the new SVG into the document
1. Place in an open spot, and use guides to scale the icon to a good size, relative to other icons
1. Any straight lines should be snapped to the closest pixel value.
   - Use the `Edit paths by nodes` tool (F2) to edit the path directly.
   - Tweak the X, Y values at the top to be integers.
1. Generate PNGs from the SVGs:
   - `./scripts/convert_svg_images_to_png.py`
1. Optimize PNGs:
   - `./scripts/optimize_png_images.py`
1. In `ui/Icon.js` add an entry in `UI.Icon.Descriptors`.
   - Look at the spritesheet's axes to identify the correct grid position.
1. You may want to regenerate devtools resources:
   - `ninja -C ~/chromium/src/out/Release/ devtools_frontend_resources`

# DevTools Scripts

## Development workflow scripts

These are scripts that can be useful to run independently as you're working on Chrome DevTools front-end.

The newer scripts such as for testing and hosted mode are written in Node.js, which has become the standard toolchain for web apps. The older scripts such as building (e.g. bundling and minifying) are written in Python, which has first-class support in Chromium's infrastructure.

## Overview

### Folders

- build - Python package for generating DevTools debug and release mode
- chrome_debug_launcher - automagically finds Chrome Canary and launches it with debugging flags (e.g. remote debugging port)
- closure - see section on Closure Compiler below
- gulp - experimental build process written in node.js & gulp to remove the dependency on Chromium-specific build tools (i.e. gn and ninja)
- hosted_mode - run DevTools on a localhost development server
- jsdoc_validator - enforces the use of Closure type annotations
- local_node - installs a local runtime of node.js

### Python Scripts
- convert_svg_images_to_png.py - manually run when adding svg images
- compile_frontend.py - runs closure compiler to do static type analysis
    - Note: the compiled outputs are not actually used to run DevTools
- lint_javascript.py - run eslint
- optimize_png_images.py - manually run when adding png images

### Node.js scripts

The easiest way to run the node.js scripts is to use `npm run` which displays all the commands. For more information on the specific `npm run` commands, take a look at the primary devtools front-end readme (`../readme.md`).

## Closure

DevTools manually rolls the closure compiler to ./closure. If you manually roll closure compiler, you will need to re-generate the closure_runner (in ./closure) and jsdoc_validator custom jars using the python scripts in their respective directory.# Running Old Devtools

This package launches your current version of Chromium, and an old version of Chromium.
It then opens the DevTools of the old Chromium inside the new Chromium. This can be
used to test devtools_compatibility.js. Remember to recompile after making changes
to devtools_compatibility.js.

## Usage
First run `npm install` in this directory. Then run `node index.js <revision_number>`.
# [Google Closure Compiler](https://developers.google.com/closure/compiler/)

[![Build Status](https://travis-ci.org/google/closure-compiler.svg?branch=master)](https://travis-ci.org/google/closure-compiler)

The [Closure Compiler](https://developers.google.com/closure/compiler/) is a tool for making JavaScript download and run faster. It is a true compiler for JavaScript. Instead of compiling from a source language to machine code, it compiles from JavaScript to better JavaScript. It parses your JavaScript, analyzes it, removes dead code and rewrites and minimizes what's left. It also checks syntax, variable references, and types, and warns about common JavaScript pitfalls.

## Getting Started
 * [Download the latest version](http://dl.google.com/closure-compiler/compiler-latest.zip) ([Release details here](https://github.com/google/closure-compiler/wiki/Releases))
 * [Download a specific version](https://github.com/google/closure-compiler/wiki/Binary-Downloads)
 * See the [Google Developers Site](https://developers.google.com/closure/compiler/docs/gettingstarted_app) for documentation including instructions for running the compiler from the command line.

## Options for Getting Help
1. Post in the [Closure Compiler Discuss Group](https://groups.google.com/forum/#!forum/closure-compiler-discuss)
2. Ask a question on [Stack Overflow](http://stackoverflow.com/questions/tagged/google-closure-compiler)
3. Consult the [FAQ](https://github.com/google/closure-compiler/wiki/FAQ)

## Building it Yourself

Note: The Closure Compiler requires [Java 7 or higher](http://www.java.com/).

### Using [Ant](http://ant.apache.org/)

1. Download the [Ant build tool](http://ant.apache.org/bindownload.cgi).

2. At the root of the source tree, there is an Ant file named ```build.xml```.
   To use it, navigate to the same directory and type the command

    ```
    ant jar
    ```

    This will produce a jar file called ```build/compiler.jar```.

### Using [Eclipse](http://www.eclipse.org/)

1. Download and open the [Eclipse IDE](http://www.eclipse.org/).
2. Navigate to ```File > New > Project ...``` and create a Java Project. Give
   the project a name.
3. Select ```Create project from existing source``` and choose the root of the
   checked-out source tree as the existing directory.
3. Navigate to the ```build.xml``` file. You will see all the build rules in
   the Outline pane. Run the ```jar``` rule to build the compiler in
   ```build/compiler.jar```.

## Running

On the command line, at the root of this project, type

```
java -jar build/compiler.jar
```

This starts the compiler in interactive mode. Type

```javascript
var x = 17 + 25;
```

then hit "Enter", then hit "Ctrl-Z" (on Windows) or "Ctrl-D" (on Mac or Linux)
and "Enter" again. The Compiler will respond:

```javascript
var x=42;
```

The Closure Compiler has many options for reading input from a file, writing
output to a file, checking your code, and running optimizations. To learn more,
type

```
java -jar compiler.jar --help
```

More detailed information about running the Closure Compiler is available in the
[documentation](http://code.google.com/closure/compiler/docs/gettingstarted_app.html).

## Compiling Multiple Scripts

If you have multiple scripts, you should compile them all together with one
compile command.

```bash
java -jar compiler.jar --js_output_file=out.js in1.js in2.js in3.js ...
```

You can also use minimatch-style globs.

```bash
# Recursively include all js files in subdirs
java -jar compiler.jar --js_output_file=out.js 'src/**.js'

# Recursively include all js files in subdirs, exclusing test files.
# Use single-quotes, so that bash doesn't try to expand the '!'
java -jar compiler.jar --js_output_file=out.js 'src/**.js' '!**_test.js'
```

The Closure Compiler will concatenate the files in the order they're passed at
the command line.

If you're using globs or many files, you may start to run into
problems with managing dependencies between scripts. In this case, you should
use the [Closure Library](https://developers.google.com/closure/library/). It
contains functions for enforcing dependencies between scripts, and Closure Compiler
will re-order the inputs automatically.

## How to Contribute
### Reporting a bug
1. First make sure that it is really a bug and not simply the way that Closure Compiler works (especially true for ADVANCED_OPTIMIZATIONS).
 * Check the [official documentation](https://developers.google.com/closure/compiler/)
 * Consult the [FAQ](https://github.com/google/closure-compiler/wiki/FAQ)
 * Search on [Stack Overflow](http://stackoverflow.com/questions/tagged/google-closure-compiler) and in the [Closure Compiler Discuss Group](https://groups.google.com/forum/#!forum/closure-compiler-discuss)
2. If you still think you have found a bug, make sure someone hasn't already reported it. See the list of [known issues](https://github.com/google/closure-compiler/issues).
3. If it hasn't been reported yet, post a new issue. Make sure to add enough detail so that the bug can be recreated. The smaller the reproduction code, the better.

### Suggesting a Feature
1. Consult the [FAQ](https://github.com/google/closure-compiler/wiki/FAQ) to make sure that the behaviour you would like isn't specifically excluded (such as string inlining).
2. Make sure someone hasn't requested the same thing. See the list of [known issues](https://github.com/google/closure-compiler/issues).
3. Read up on [what type of feature requests are accepted](https://github.com/google/closure-compiler/wiki/FAQ#how-do-i-submit-a-feature-request-for-a-new-type-of-optimization).
4. Submit your reqest as an issue.

### Submitting patches
1. All contributors must sign a contributor license agreement. See the [CONTRIBUTORS](https://raw.githubusercontent.com/google/closure-compiler/master/CONTRIBUTORS) file for details.
2. To make sure your changes are of the type that will be accepted, ask about your patch on the [Closure Compiler Discuss Group](https://groups.google.com/forum/#!forum/closure-compiler-discuss)
3. Fork the repository.
4. Make your changes.
5. Submit a pull request for your changes. A project developer will review your work and then merge your request into the project.

## Closure Compiler License

Copyright 2009 The Closure Compiler Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Dependency Licenses

### Rhino

<table>
  <tr>
    <td>Code Path</td>
    <td>
      <code>src/com/google/javascript/rhino</code>, <code>test/com/google/javascript/rhino</code>
    </td>
  </tr>

  <tr>
    <td>URL</td>
    <td>http://www.mozilla.org/rhino</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>1.5R3, with heavy modifications</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Netscape Public License and MPL / GPL dual license</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>A partial copy of Mozilla Rhino. Mozilla Rhino is an
implementation of JavaScript for the JVM.  The JavaScript
parse tree data structures were extracted and modified
significantly for use by Google's JavaScript compiler.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>The packages have been renamespaced. All code not
relevant to the parse tree has been removed. A JsDoc parser and static typing
system have been added.</td>
  </tr>
</table>

### Args4j

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/args4j.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>https://args4j.dev.java.net/</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>2.0.26</td>
  </tr>

  <tr>
    <td>License</td>
    <td>MIT</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>args4j is a small Java class library that makes it easy to parse command line
options/arguments in your CUI application.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### Guava Libraries

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/guava.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>https://github.com/google/guava</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>18.0</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Apache License 2.0</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>Google's core Java libraries.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### JSR 305

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/jsr305.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>http://code.google.com/p/jsr-305/</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>svn revision 47</td>
  </tr>

  <tr>
    <td>License</td>
    <td>BSD License</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>Annotations for software defect detection.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### JUnit

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/junit.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>http://sourceforge.net/projects/junit/</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>4.11</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Common Public License 1.0</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>A framework for writing and running automated tests in Java.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### Protocol Buffers

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/protobuf-java.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>http://code.google.com/p/protobuf/</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>2.5.0</td>
  </tr>

  <tr>
    <td>License</td>
    <td>New BSD License</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>Supporting libraries for protocol buffers,
an encoding of structured data.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### Truth

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/truth.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>https://github.com/google/truth</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>0.24</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Apache License 2.0</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>Assertion/Proposition framework for Java unit tests</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### Ant

<table>
  <tr>
    <td>Code Path</td>
    <td>
      <code>lib/ant.jar</code>, <code>lib/ant-launcher.jar</code>
    </td>
  </tr>

  <tr>
    <td>URL</td>
    <td>http://ant.apache.org/bindownload.cgi</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>1.8.1</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Apache License 2.0</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>Ant is a Java based build tool. In theory it is kind of like "make"
without make's wrinkles and with the full portability of pure java code.</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### GSON

<table>
  <tr>
    <td>Code Path</td>
    <td><code>lib/gson.jar</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>https://code.google.com/p/google-gson/</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>2.2.4</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Apache license 2.0</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>A Java library to convert JSON to Java objects and vice-versa</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>None</td>
  </tr>
</table>

### Node.js Closure Compiler Externs

<table>
  <tr>
    <td>Code Path</td>
    <td><code>contrib/nodejs</code></td>
  </tr>

  <tr>
    <td>URL</td>
    <td>https://github.com/dcodeIO/node.js-closure-compiler-externs</td>
  </tr>

  <tr>
    <td>Version</td>
    <td>e891b4fbcf5f466cc4307b0fa842a7d8163a073a</td>
  </tr>

  <tr>
    <td>License</td>
    <td>Apache 2.0 license</td>
  </tr>

  <tr>
    <td>Description</td>
    <td>Type contracts for NodeJS APIs</td>
  </tr>

  <tr>
    <td>Local Modifications</td>
    <td>Substantial changes to make them compatible with NpmCommandLineRunner.</td>
  </tr>
</table>
Name: Xterm.js is a terminal front-end component written in JavaScript that works in the browser.
Short Name: xterm.js
URL: https://github.com/sourcelair/xterm.js
License: MIT
Security Critical: no

This directory contains Chrome's version of xterm.js with tests, demo and some addons folders removed.
# Rolling CodeMirror

## What's this about?
CodeMirror is a third-party library, which supports editing experience in Chrome DevTools. DevTools does not fork CodeMirror, thus all CodeMirror patches should go upstream to http://codemirror.net.
Every once in a while, the CodeMirror dependency (which is located in Source/devtools/front_end/cm/ folder) should be updated to a newer version.

## Updating CodeMirror
This requires the following steps to be done:
1. File `headlesscodemirror.js` is a `runmode-standalone.js` file from CodeMirror distribution, but wrapped in `(function(window) { ... }(this))`
construction. This is needed to support in web workers.
2. File `markselection.js` is a `mark-selection.js` from CodeMirror distribution. The "dash" is removed due to the restriction on the chromium grd generator.
4. File codemirror.css contains both the default theme of CodeMirror and structural css required for it to work. Discard everything in the file up to the word `/* STOP */`.
3. All other files in front_end/cm/ folder should be substituted with their newer versions from the upstream.

## Testing
DevTools wrap CodeMirror via `CodeMirrorTextEditor.js` and `cmdevtools.css` files.
Although there are a couple of automated tests (web_tests/inspector/editor/) to verify overall sanity of the setup, a manual testing is mandatory before
landing a roll. Here is a rough testing scenario outline:
1. Create a new snippet and type in a small function with a few nested for-loops. (The author suggests a bubble-sort). Make sure that:
   * Words `function`, `for`, `var` are highlighted
   * "Smart braces" behavior works
   * "Enter" after opening curly brace adds correct indent
   * Autocompletion works
   * Multiple cursors functionality works as intended - Ctrl+D/Ctrl+U shortcuts
   * Set a breakpoint inside a function, select some text and summon a context menu over it.
2. Make sure there are items such as "Add to Watch", "Evaluate in Console" and "Copy/Paste"
Make sure minified jquery opens nicely in the editor (minified jquery could be found as a resource on http://jquery.com)
   * Verify `jquery.min.js` is formatted via "Pretty print" action
3. Go to the Elements panel, select a node and verify the "Edit it as HTML" command works.

## Committing
The only changes allowed to front_end/cm/ folder are CodeMirror rolls. There's a presubmit check that enforces this, so make sure you include the phrase "roll CodeMirror" into
your patch description.

## Example
Example CodeMirror roll patchset: https://codereview.chromium.org/273763003
Name: A JavaScript implementation of the Secure Hash Algorithm, SHA-1, as defined in FIPS 180-1.
Short Name: sha1.js
URL: http://pajhome.org.uk/crypt/md5/
License: BSD
Security Critical: no

This directory contains Chromium's version of sha1.js which is for hashing strings in javascript synchronously. Added
jsdoc types to functions, wrapped functions in an outer function and removed portions of code that are not needed by
Chromium.Name: Lighthouse is a performance auditing component written in JavaScript that works in the browser.
Short Name: lighthouse
URL: github.com/GoogleChrome/lighthouse
License: Apache License 2.0
Security Critical: no

This directory contains Chromium's version of the lighthouse report assets, including renderer.

Name: Lighthouse is a performance auditing component written in JavaScript that works in the browser.
Short Name: lighthouse
URL: github.com/GoogleChrome/lighthouse
License: Apache License 2.0
Security Critical: no

This directory contains Chromium's version of lighthouse with tests, demo and sources removed.

