# bootstrap-datepicker

[![Join the chat at https://gitter.im/eternicode/bootstrap-datepicker](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/eternicode/bootstrap-datepicker?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is a fork of Stefan Petre's [original code](http://www.eyecon.ro/bootstrap-datepicker/);
thanks go to him for getting this thing started!

Please note that this fork is not used on Stefan's page, nor is it maintained or contributed to by him.

Versions are incremented according to [semver](http://semver.org/).

## CDN

You can use the [CloudFlare](https://www.cloudflare.com) powered [cdnjs.com](https://cdnjs.com) on your website. 

[bootstrap-datepicker](http://cdnjs.com/libraries/bootstrap-datepicker) on cdnjs

Please note: It might take a few days until a new version is available on cdnjs.

## Links

* [Online Demo](http://eternicode.github.io/bootstrap-datepicker/)
* [Online Docs](http://bootstrap-datepicker.readthedocs.org/en/stable/) (ReadTheDocs.com)
* [Google Group](https://groups.google.com/group/bootstrap-datepicker/)
* [Travis CI ![Build Status](https://travis-ci.org/eternicode/bootstrap-datepicker.svg?branch=master)](https://travis-ci.org/eternicode/bootstrap-datepicker)

## Development

Once you cloned the repo, you'll need to install [grunt](http://gruntjs.com/) and the development dependencies using [npm](https://www.npmjs.com/).

    npm install -g grunt-cli
    npm install
Unit tests, written with [QUnit](http://docs.jquery.com/QUnit), are used to
expose bugs for squashing, prevent bugs from respawning, and suppress new
bugs when adding new features and making changes.

# Running the tests

The simplest way to run the tests is to open `tests/tests.html` in your browser.
The test suites will automatically run themselves and present their results.

To run the tests from the command line (after running jshint and jscs, which is
recommended), install Grunt and run the `test` task from anywhere within the
repo:

    $ grunt test

# Adding tests

Tests go in js files in the `tests/suites/` directory tree.  QUnit organizes
tests into suites called "modules"; there is one module per js file.  If the
tests you are adding do not fit into an existing module, create a new one at
`tests/suites/<new module>.js`, where `<new module>` is a broad yet
descriptive name for the suite.  If tests have many year-specific cases (ie,
behave differently in leap years vs normal years, or have specific buggy
behavior in a certain year), create the module in a new directory,
`tests/suites/<new module>/<year>.js`, where `<new module>` is the decriptive
name and `<year>` is the four-digit year the tests pertain to.

In order for new tests to be run, they must be imported into `tests/tests.html`.
Find the script includes headed by the html comment `<!-- Test suites -->`, and
add a new one to the list which includes the new js files.
Documentation
=============

Project documentation is built using [Sphinx docs](http://sphinx-doc.org/), which uses [ReST](http://docutils.sourceforge.net/rst.html) for markup.  This allows the docs to cover a vast amount of topics without using a thousand-line README file.

Sphinx docs is pip-installable via `pip install sphinx`.  Once installed, open a command line in the docs folder and run the following commands:

```bash
$ sudo pip install -r requirements.txt
```

This will install the requirements needed for the generating the docs. Afterwards you can run:

```bash
$ make html
```

The docs will be generated, the output files will be placed in the `_build/html/` directory, and can be browsed (locally) with any browser.

The docs can also be found online at <http://bootstrap-datepicker.readthedocs.org/>.
## Tether

[![GitHub
version](https://badge.fury.io/gh/HubSpot%2Ftether.svg)](http://badge.fury.io/gh/HubSpot%2Ftether)

[Tether](http://github.hubspot.com/tether/) is a small, focused JavaScript library for defining and managing the position of user interface (UI) elements in relation to one another on a web page. It is a tool for web developers building features that require certain UI elements to be precisely positioned based on the location of another UI element.

There are often situations in UI development where elements need to be attached to other elements, but placing them right next to each other in the [DOM tree](https://en.wikipedia.org/wiki/Document_Object_Model) can be problematic based on the context. For example, what happens if the element we’re attaching other elements to is fixed to the center of the screen? Or what if the element is inside a scrollable container? How can we prevent the attached element from being clipped as it disappears from view while a user is scrolling? Tether can solve all of these problems and more.

Some common UI elements that have been built with Tether are [tooltips](http://github.hubspot.com/tooltip/docs/welcome), [select menus](http://github.hubspot.com/select/docs/welcome), [dropdown menus](http://github.hubspot.com/drop/docs/welcome), and [guided tours](http://github.hubspot.com/shepherd/docs/welcome). Tether is flexible and can be used to [solve](http://github.hubspot.com/tether/examples/out-of-bounds/) [all](http://github.hubspot.com/tether/examples/content-visible) [kinds](http://github.hubspot.com/tether/examples/element-scroll) [of](http://github.hubspot.com/tether/examples/enable-disable) [interesting]() [problems](http://github.hubspot.com/tether/examples/viewport); it ensures UI elements stay where they need to be, based on the various user interactions (click, scroll, etc) and layout contexts (fixed positioning, inside scrollable containers, etc).

Please have a look at the [documentation](http://github.hubspot.com/tether/) for a more detailed explanation of why you might need Tether for your next project.

## What to Use Tether for and When to Use It

Tether is a small, focused JavaScript library. For those who might be new to JavaScript, a library is simply a JavaScript file (or files) that contain useful JavaScript code to help achieve tasks easier and faster. Since Tether is a JavaScript user interface (**UI**) library, it contains code to help you to manage the way your website or web app appears.

Tether’s goal to is to help you position your elements side-by-side when needed.

Let’s say you’ve started working on your dream project&mdash;a fancy web app that’s sure to become the next big thing! An important feature of your new app is to allow users to comment on shared photos. However, due to limited vertical space and the overall layout of your new app, you’d like to display the comments **next** to the image, similar to how Instagram does it.

Your HTML code might look something like this:

```html
<div class="container">
  <img src="awesome-picture.jpg" alt="Awesome Picture" class="picture">
  <div class="comments">
    ...
  </div>
</div>
```

Now, you could achieve this with some CSS using its `position` property, but going this route can be problematic since many of `position`’s values take elements **out** of the natural DOM flow. For example, if you have an element at the bottom of your HTML document, using `position: absolute` or `position: fixed` might could move it all the way to the top of your website in the browser.

Not only that, but you also have to make manual adjustments to ensure **other** elements aren’t negatively affected by the positioned elements. Not to mention, you probably want your comment box to be **responsive**, and look good across different device sizes. Coding a solution for this manually is a challenge all on its own.

**Enter Tether!**

After installing Tether and including it in your project, you can begin using it!

1. In your JavaScript file, create a new instance (or constructor function) of the `Tether` object:

    ```javascript
    new Tether({});
    ```

2. Within the curly braces (`{}`) you can configure the library’s options. Tether’s extensive list of options can be found in the [Tether documentation](http://github.hubspot.com/tether/).

    ```javascript
    new Tether({
      element: '.comments',
      target: '.picture',
      attachment: 'top right'
      targetAttachment: 'top left'
    });
    ```

Now you have a perfectly placed comment section to go with your awesome picture! It’ll even stay attached to the element when a user resizes their browser window.

There are tons of other useful features of Tether as well, instead of “comment boxes” you could also build:

* Tooltips for useful hints and tricks,
* Dropdown menus,
* Autocomplete popups for forms,
* and [more](http://github.hubspot.com/tether/examples/list_of_examples/)!

## Install

__npm__
```sh
$ npm install tether
```

__bower__
```sh
$ bower install tether
```

## Usage

[![Tether Docs](http://i.imgur.com/YCx8cLr.png)](http://github.hubspot.com/tether/#usage)

[Demo & API Documentation](http://github.hubspot.com/tether/)

## Contributing

We encourage contributions of all kinds. If you would like to contribute in some way, please review our [guidelines for contributing](CONTRIBUTING.md).

## License
Copyright &copy; 2014-2016 HubSpot - [MIT License](LICENSE)
# [Bootstrap](http://getbootstrap.com)

[![Slack](https://bootstrap-slack.herokuapp.com/badge.svg)](https://bootstrap-slack.herokuapp.com)
![Bower version](https://img.shields.io/bower/v/bootstrap.svg)
[![npm version](https://img.shields.io/npm/v/bootstrap.svg)](https://www.npmjs.com/package/bootstrap)
[![Build Status](https://img.shields.io/travis/twbs/bootstrap/master.svg)](https://travis-ci.org/twbs/bootstrap)
[![devDependency Status](https://img.shields.io/david/dev/twbs/bootstrap.svg)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![NuGet](https://img.shields.io/nuget/vpre/bootstrap.svg)](https://www.nuget.org/packages/bootstrap/4.0.0-alpha)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat), and maintained by the [core team](https://github.com/orgs/twbs/people) with the massive support and involvement of the community.

To get started, check out <http://getbootstrap.com>!

## Table of contents

- [Quick start](#quick-start)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Quick start

Several quick start options are available:

- [Download the latest release](https://github.com/twbs/bootstrap/archive/v4.0.0-alpha.2.zip).
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
- Install with [Bower](http://bower.io): `bower install bootstrap`.
- Install with [npm](https://www.npmjs.com): `npm install bootstrap`.
- Install with [Meteor](https://www.meteor.com): `meteor add twbs:bootstrap`.
- Install with [Composer](https://getcomposer.org): `composer require twbs/bootstrap`.
- Install with [NuGet](https://www.nuget.org): CSS: `Install-Package bootstrap -Pre` Sass: `Install-Package bootstrap.sass -Pre` (`-Pre` is only required until Bootstrap v4 has a stable release).

Read the [Getting started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   └── bootstrap.min.css.map
└── js/
    ├── bootstrap.js
    └── bootstrap.min.js
```

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). CSS [source maps](https://developer.chrome.com/devtools/docs/css-preprocessors) (`bootstrap.*.map`) are available for use with certain browsers' developer tools.


## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](http://jekyllrb.com) and publicly hosted on GitHub Pages at <http://getbootstrap.com>. The docs may also be run locally.

### Running documentation locally

1. Run through the [tooling setup](https://github.com/twbs/bootstrap/blob/v4-dev/docs/getting-started/build-tools.md#tooling-setup) to install Jekyll (the site builder) and other Ruby dependencies with `bundle install`.
2. From the root `/bootstrap` directory, run `bundle exec jekyll serve` in the command line.
3. Open <http://localhost:9001> in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.



## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include [relevant unit tests](https://github.com/twbs/bootstrap/tree/master/js/tests). All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.



## Community

Get updates on Bootstrap's development and chat with the project maintainers and community members.

- Follow [@getbootstrap on Twitter](https://twitter.com/getbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
- Join [the official Slack room](https://bootstrap-slack.herokuapp.com).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`bootstrap-4`](https://stackoverflow.com/questions/tagged/bootstrap-4)).
- Developers should use the keyword `bootstrap` on packages which modify or add to the functionality of Bootstrap when distributing through [npm](https://www.npmjs.com/browse/keyword/bootstrap) or similar delivery mechanisms for maximum discoverability.



## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.

See [the Releases section of our GitHub project](https://github.com/twbs/bootstrap/releases) for changelogs for each release version of Bootstrap. Release announcement posts on [the official Bootstrap blog](http://blog.getbootstrap.com) contain summaries of the most noteworthy changes made in each release.


## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>



## Copyright and license

Code and documentation copyright 2011-2015 Twitter, Inc. Code released under [the MIT license](https://github.com/twbs/bootstrap/blob/master/LICENSE). Docs released under [Creative Commons](https://github.com/twbs/bootstrap/blob/master/docs/LICENSE).
# jQuery

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
