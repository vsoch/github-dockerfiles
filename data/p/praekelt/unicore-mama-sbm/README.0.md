mamasbm README
==================

Getting Started
---------------

- cd <directory containing this file>

- $python setup.py develop

- $initialize_mamasbm_db development.ini

- $pserve development.ini --reload

                       __
                      /\ \                                                         __
     __  __    ___    \_\ \     __   _ __   ____    ___    ___   _ __    __       /\_\    ____
    /\ \/\ \ /' _ `\  /'_  \  /'__`\/\  __\/ ,__\  / ___\ / __`\/\  __\/'__`\     \/\ \  /',__\
    \ \ \_\ \/\ \/\ \/\ \ \ \/\  __/\ \ \//\__, `\/\ \__//\ \ \ \ \ \//\  __/  __  \ \ \/\__, `\
     \ \____/\ \_\ \_\ \___,_\ \____\\ \_\\/\____/\ \____\ \____/\ \_\\ \____\/\_\ _\ \ \/\____/
      \/___/  \/_/\/_/\/__,_ /\/____/ \/_/ \/___/  \/____/\/___/  \/_/ \/____/\/_//\ \_\ \/___/
                                                                                  \ \____/
                                                                                   \/___/

Underscore.js is a utility-belt library for JavaScript that provides
support for the usual functional suspects (each, map, reduce, filter...)
without extending any core JavaScript objects.

For Docs, License, Tests, and pre-packed downloads, see:
http://underscorejs.org

Underscore is an open-sourced component of DocumentCloud:
https://github.com/documentcloud

Many thanks to our contributors:
https://github.com/jashkenas/underscore/contributors
# Bootstrap Multiselect

Bootstrap Multiselect is a JQuery based plugin to provide an intuitive user interface for using select inputs with the multiple attribute present. Instead of a select a bootstrap button will be shown as dropdown menu containing the single options as checkboxes.

Bootstrap 3 port by [Eduard Dudar](https://github.com/edudar).

## Documentation

Documentation, demonstrations and FAQ: [http://davidstutz.github.com/bootstrap-multiselect/](http://davidstutz.github.com/bootstrap-multiselect/).

**Note**: The demo page is based on JQuery 2 - so for IE 6,7 and 8 the plugin will not work properly. Nevertheless, the plugin should run as expected using the .x branch of jQuery.

## Contribute!

Every pull request is appreciated. To make it easier for me to merge fixes and new features have a look at the following guidelines:

* Include documentation for new options and features to avoid undocumented features.
* Add a thorough description to every pull request - so I am able to understand the purpose of the pull request.
* Have a look at the code as to keep the code as comprehensible and coherent as possible (concerning code style, indentation etc. ...).
* Add comments to your code - to help me understand the committed code.
* Add a single pull request per fix or feature you add.

## License

This project is dual licensed under the Apache License, Version 2.0 and the BSD 3-Clause license.

### Apache License, Version 2.0

Copyright 2012 - 2014 David Stutz

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

### BSD 3-Clause License

Copyright (c) 2012 - 2014 David Stutz
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the <ORGANIZATION> nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.# bower-angular-resource

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngResource).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-resource
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-resource/angular-resource.js"></script>
```

And add `ngResource` as a dependency for your app:

```javascript
angular.module('myApp', ['ngResource']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngResource).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

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
# [Bootstrap](http://getbootstrap.com) [![Build Status](https://secure.travis-ci.org/twbs/bootstrap.png)](http://travis-ci.org/twbs/bootstrap) [![devDependency Status](https://david-dm.org/twbs/bootstrap/dev-status.png?theme=shields.io)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](http://twitter.com/mdo) and [Jacob Thornton](http://twitter.com/fat), and maintained by the [core team](https://github.com/twbs?tab=members) with the massive support and involvement of the community.

To get started, check out <http://getbootstrap.com>!

## Table of contents

 - [Quick start](#quick-start)
 - [Bugs and feature requests](#bugs-and-feature-requests)
 - [Documentation](#documentation)
 - [Compiling CSS and JavaScript](#compiling-css-and-javascript)
 - [Contributing](#contributing)
 - [Community](#community)
 - [Versioning](#versioning)
 - [Authors](#authors)
 - [Copyright and license](#copyright-and-license)

## Quick start

Three quick start options are available:

- [Download the latest release](https://github.com/twbs/bootstrap/archive/v3.1.0.zip).
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
- Install with [Bower](http://bower.io): `bower install bootstrap`.

Read the [Getting Started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.min.css
│   ├── bootstrap-theme.css
│   └── bootstrap-theme.min.css
├── js/
│   ├── bootstrap.js
│   └── bootstrap.min.js
└── fonts/
    ├── glyphicons-halflings-regular.eot
    ├── glyphicons-halflings-regular.svg
    ├── glyphicons-halflings-regular.ttf
    └── glyphicons-halflings-regular.woff
```

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). Fonts from Glyphicons are included, as is the optional Bootstrap theme.



## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](http://jekyllrb.com) and publicly hosted on GitHub Pages at <http://getbootstrap.com>. The docs may also be run locally.

### Running documentation locally

1. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) (requires v1.x).
  - **Windows users:** Read [this unofficial guide](https://github.com/juthilo/run-jekyll-on-windows/) to get Jekyll up and running without problems. We use Pygments for syntax highlighting, so make sure to read the sections on installing Python and Pygments.
2. From the root `/bootstrap` directory, run `jekyll serve` in the command line.
  - **Windows users:** While we use Jekyll's `encoding` setting, you might still need to change the command prompt's character encoding ([code page](http://en.wikipedia.org/wiki/Windows_code_page)) to UTF-8 so Jekyll runs without errors. For Ruby 2.0.0, run `chcp 65001` first. For Ruby 1.9.3, you can alternatively do `SET LANG=en_EN.UTF-8`.
3. Open <http://localhost:9001> in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.



## Compiling CSS and JavaScript

Bootstrap uses [Grunt](http://gruntjs.com/) with convenient methods for working with the framework. It's how we compile our code, run tests, and more. To use it, install the required dependencies as directed and then run some Grunt commands.

### Install Grunt

From the command line:

1. Install `grunt-cli` globally with `npm install -g grunt-cli`.
2. Navigate to the root `/bootstrap` directory, then run `npm install`. npm will look at [package.json](https://github.com/twbs/bootstrap/blob/master/package.json) and automatically install the necessary local dependencies listed there.

When completed, you'll be able to run the various Grunt commands provided from the command line.

**Unfamiliar with `npm`? Don't have node installed?** That's a-okay. npm stands for [node packaged modules](http://npmjs.org/) and is a way to manage development dependencies through node.js. [Download and install node.js](http://nodejs.org/download/) before proceeding.

### Available Grunt commands

#### Build - `grunt`
Run `grunt` to run tests locally and compile the CSS and JavaScript into `/dist`. **Uses [Less](http://lesscss.org/) and [UglifyJS](http://lisperator.net/uglifyjs/).**

#### Only compile CSS and JavaScript - `grunt dist`
`grunt dist` creates the `/dist` directory with compiled files. **Uses [Less](http://lesscss.org/) and [UglifyJS](http://lisperator.net/uglifyjs/).**

#### Tests - `grunt test`
Runs [JSHint](http://jshint.com) and [QUnit](http://qunitjs.com/) tests headlessly in [PhantomJS](http://phantomjs.org/) (used for CI).

#### Watch - `grunt watch`
This is a convenience method for watching just Less files and automatically building them whenever you save.

### Troubleshooting dependencies

Should you encounter problems with installing dependencies or running Grunt commands, uninstall all previous dependency versions (global and local). Then, rerun `npm install`.



## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include relevant unit tests. All HTML and CSS should conform to the [Code Guide](http://github.com/mdo/code-guide), maintained by [Mark Otto](http://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.



## Community

Keep track of development and community news.

- Follow [@twbootstrap on Twitter](http://twitter.com/twbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##twitter-bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`twitter-bootstrap-3`](http://stackoverflow.com/questions/tagged/twitter-bootstrap-3)).




## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under the Semantic Versioning guidelines. Sometimes we screw up, but we'll adhere to these rules whenever possible.

Releases will be numbered with the following format:

`<major>.<minor>.<patch>`

And constructed with the following guidelines:

- Breaking backward compatibility **bumps the major** while resetting minor and patch
- New additions without breaking backward compatibility **bumps the minor** while resetting the patch
- Bug fixes and misc changes **bumps only the patch**

For more information on SemVer, please visit <http://semver.org/>.



## Authors

**Mark Otto**

- <http://twitter.com/mdo>
- <http://github.com/mdo>

**Jacob Thornton**

- <http://twitter.com/fat>
- <http://github.com/fat>



## Copyright and license

Code and documentation copyright 2011-2014 Twitter, Inc. Code released under [the MIT license](LICENSE). Docs released under [Creative Commons](docs/LICENSE).
# bower-angular

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular/angular.js"></script>
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

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
# bower-angular-route

This repo is for distribution on `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngRoute).
Please file issues and pull requests against that repo.

## Install

Install with `bower`:

```shell
bower install angular-route
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-route/angular-route.js"></script>
```

And add `ngRoute` as a dependency for your app:

```javascript
angular.module('myApp', ['ngRoute']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngRoute).

## License

The MIT License

Copyright (c) 2010-2012 Google, Inc. http://angularjs.org

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
Generic single-database configuration.