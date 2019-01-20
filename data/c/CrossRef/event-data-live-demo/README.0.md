# The HTML5 Shiv

The HTML5 Shiv enables use of HTML5 sectioning elements in legacy Internet Explorer and provides basic HTML5 styling for Internet Explorer 6-9, Safari 4.x (and iPhone 3.x), and Firefox 3.x.

### What do these files do?

#### `html5shiv.js`
*  This includes the basic `createElement()` shiv technique, along with monkeypatches for `document.createElement` and `document.createDocumentFragment` for IE6-8. It also applies [basic styling](https://github.com/aFarkas/html5shiv/blob/51da98dabd3c537891b7fe6114633fb10de52473/src/html5shiv.js#L216-220) for HTML5 elements for IE6-9, Safari 4.x and FF 3.x.

####`html5shiv-printshiv.js` 
*  This includes all of the above, as well as a mechanism allowing HTML5 elements to be styled and contain children while being printed in IE 6-8.

### Who can I get mad at now?

HTML5 Shiv is maintained by [Alexander Farkas](https://github.com/aFarkas/), [Jonathan Neal](https://twitter.com/jon_neal) and [Paul Irish](https://twitter.com/paul_irish), with many contributions from [John-David Dalton](https://twitter.com/jdalton). It is also distributed with [Modernizr](http://modernizr.com/), and the two google code projects, [html5shiv](https://code.google.com/p/html5shiv/) and [html5shim](https://code.google.com/p/html5shim/), maintained by [Remy Sharp](https://twitter.com/rem).

If you have any issues in these implementations, you can report them here! :)

For the full story of HTML5 Shiv and all of the people involved in making it, read [The Story of the HTML5 Shiv](http://paulirish.com/2011/the-history-of-the-html5-shiv/).

## Installation

###Using [Bower](http://bower.io/)

`bower install html5shiv --save-dev`

This will clone the latest version of the HTML5 shiv into the `bower_components` directory at the root of your project and also create or update the file `bower.json` which specifies your projects dependencies.

Include the HTML5 shiv in the `<head>` of your page in a conditional comment and after any stylesheets.

```html
<!--[if lt IE 9]>
	<script src="bower_components/html5shiv/html5shiv.js"></script>
<![endif]-->
```

###Manual installation

Download and extract the [latest zip package](https://github.com/aFarkas/html5shiv/archive/master.zip) from this repositiory and copy the two files `dist/html5shiv.js` and `dist/html5shiv-printshiv.js` into your project. Then include one of them into your `<head>` as above. 

## HTML5 Shiv API

HTML5 Shiv works as a simple drop-in solution. In most cases there is no need to configure HTML5 Shiv or use methods provided by HTML5 Shiv.

### `html5.elements` option

The `elements` option is a space separated string or array, which describes the **full** list of the elements to shiv. see also `addElements`.

**Configuring `elements` before `html5shiv.js` is included.**

```js
//create a global html5 options object
window.html5 = {
  'elements': 'mark section customelement' 
};
```
**Configuring `elements` after `html5shiv.js` is included.**

```js
//change the html5shiv options object 
window.html5.elements = 'mark section customelement';
//and re-invoke the `shivDocument` method
html5.shivDocument(document);
```

### `html5.shivCSS`

If `shivCSS` is set to `true` HTML5 Shiv will add basic styles (mostly display: block) to sectioning elements (like section, article). In most cases a webpage author should include those basic styles in his normal stylesheet to ensure older browser support (i.e. Firefox 3.6) without JavaScript.

The `shivCSS` is true by default and can be set false, only before html5shiv.js is included: 

```js
//create a global html5 options object
window.html5 = {
	'shivCSS': false
};
```

### `html5.shivMethods`

If the `shivMethods` option is set to `true` (by default) HTML5 Shiv will override `document.createElement`/`document.createDocumentFragment` in Internet Explorer 6-8 to allow dynamic DOM creation of HTML5 elements. 

Known issue: If an element is created using the overridden `createElement` method this element returns a document fragment as its `parentNode`, but should be normally `null`. If a script relies on this behavior, `shivMethods`should be set to `false`.
Note: jQuery 1.7+ has implemented his own HTML5 DOM creation fix for Internet Explorer 6-8. If all your scripts (including Third party scripts) are using jQuery's manipulation and DOM creation methods, you might want to set this option to `false`.

**Configuring `shivMethods` before `html5shiv.js` is included.**

```js
//create a global html5 options object
window.html5 = {
	'shivMethods': false
};
```
**Configuring `elements` after `html5shiv.js` is included.**

```js
//change the html5shiv options object 
window.html5.shivMethods = false;
```

### `html5.addElements( newElements [, document] )`

The `html5.addElements` method extends the list of elements to shiv. The newElements argument can be a whitespace separated list or an array.

```js
//extend list of elements to shiv
html5.addElements('element content');
```

### `html5.createElement( nodeName [, document] )`

The `html5.createElement` method creates a shived element, even if `shivMethods` is set to false.

```js
var container = html5.createElement('div');
//container is shived so we can add HTML5 elements using `innerHTML`
container.innerHTML = '<section>This is a section</section>';
```

### `html5.createDocumentFragment( [document] )`

The `html5.createDocumentFragment` method creates a shived document fragment, even if `shivMethods` is set to false.

```js
var fragment = html5.createDocumentFragment();
var container = document.createElement('div');
fragment.appendChild(container);
//fragment is shived so we can add HTML5 elements using `innerHTML`
container.innerHTML = '<section>This is a section</section>';
```

## HTML5 Shiv Known Issues and Limitations

- The `shivMethods` option (overriding `document.createElement`) and the `html5.createElement` method create elements, which are not disconnected and have a parentNode (see also issue #64)
- The cloneNode problem is currently not addressed by HTML5 Shiv. HTML5 elements can be dynamically created, but can't be cloned in all cases.
- The printshiv version of HTML5 Shiv has to alter the print styles and the whole DOM for printing. In case of complex websites and or a lot of print styles this might cause performance and/or styling issues. A possible solution could be the [htc-branch](https://github.com/aFarkas/html5shiv/tree/iepp-htc) of HTML5 Shiv, which uses another technique to implement print styles for Internet Explorer 6-8.

### What about the other HTML5 element projects?

- The original conception and community collaboration story of the project is described at [The History of the HTML5 Shiv](http://paulirish.com/2011/the-history-of-the-html5-shiv/). 
- [IEPP](https://code.google.com/p/ie-print-protector), by Jon Neal, addressed the printing fault of the original `html5shiv`. It was merged into `html5shiv`.
- **Shimprove**, in April 2010, patched `cloneNode` and `createElement` was later merged into `html5shiv`
- **innerShiv**, introduced in August 2010 by JD Barlett, addressed dynamically adding new HTML5 elements into the DOM. [jQuery added support](http://blog.jquery.com/2011/11/03/jquery-1-7-released/) that made innerShiv redundant and `html5shiv` addressed the same issues as well, so the project was completed.
- The **html5shim** and **html5shiv** sites on Google Code are maintained by Remy Sharp and are identical distribution points of this `html5shiv` project.
- **Modernizr** is developed by the same people as `html5shiv` and can include the latest version in any custom builds created at modernizr.com
- This `html5shiv` repo now contains tests for all the edge cases pursued by the above libraries and has been extensively tested, both in development and production. 

A [detailed changelog of html5shiv](https://github.com/aFarkas/html5shiv/wiki) is available.

### Why is it called a *shiv*?

The term **shiv** [originates](http://ejohn.org/blog/html5-shiv/) from [John Resig](https://github.com/jeresig), who was thought to have used the word for its slang meaning, *a sharp object used as a knife-like weapon*, intended for Internet Explorer. Truth be known, John probably intended to use the word [shim](http://en.wikipedia.org/wiki/Shim_(computing\)), which in computing means *an application compatibility workaround*. Rather than correct his mispelling, most developers familiar with Internet Explorer appreciated the visual imagery. And that, [kids](http://html5homi.es/), is [etymology](https://en.wikipedia.org/wiki/Etymology).
# [Bootstrap](http://getbootstrap.com)
[![Bower version](https://badge.fury.io/bo/bootstrap.svg)](http://badge.fury.io/bo/bootstrap)
[![NPM version](https://badge.fury.io/js/bootstrap.svg)](http://badge.fury.io/js/bootstrap)
[![Build Status](https://secure.travis-ci.org/twbs/bootstrap.svg?branch=master)](https://travis-ci.org/twbs/bootstrap)
[![devDependency Status](https://david-dm.org/twbs/bootstrap/dev-status.svg)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat), and maintained by the [core team](https://github.com/twbs?tab=members) with the massive support and involvement of the community.

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

Four quick start options are available:

- [Download the latest release](https://github.com/twbs/bootstrap/archive/v3.3.1.zip).
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
- Install with [Bower](http://bower.io): `bower install bootstrap`.
- Install with [npm](https://www.npmjs.org): `npm install bootstrap`.

Read the [Getting started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

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

1. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) (requires v2.5.x).
  - **Windows users:** Read [this unofficial guide](http://jekyll-windows.juthilo.com/) to get Jekyll up and running without problems.
2. Install the Ruby-based syntax highlighter, [Rouge](https://github.com/jneen/rouge), with `gem install rouge`.
3. From the root `/bootstrap` directory, run `jekyll serve` in the command line.
4. Open <http://localhost:9001> in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.



## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include relevant unit tests. All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.



## Community

Keep track of development and community news.

- Follow [@twbootstrap on Twitter](https://twitter.com/twbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`twitter-bootstrap-3`](http://stackoverflow.com/questions/tagged/twitter-bootstrap-3)).



## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.



## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>



## Copyright and license

Code and documentation copyright 2011-2014 Twitter, Inc. Code released under [the MIT license](LICENSE). Docs released under [Creative Commons](docs/LICENSE).
# Respond.js
### A fast & lightweight polyfill for min/max-width CSS3 Media Queries (for IE 6-8, and more)

 - Copyright 2011: Scott Jehl, scottjehl.com

 - Licensed under the MIT license.
 
The goal of this script is to provide a fast and lightweight (3kb minified / 1kb gzipped) script to enable [responsive web designs](http://www.alistapart.com/articles/responsive-web-design/) in browsers that don't support CSS3 Media Queries - in particular, Internet Explorer 8 and under. It's written in such a way that it will probably patch support for other non-supporting browsers as well (more information on that soon).

If you're unfamiliar with the concepts surrounding Responsive Web Design, you can read up [here](http://www.alistapart.com/articles/responsive-web-design/) and also [here](http://filamentgroup.com/examples/responsive-images/)

[Demo page](https://rawgithub.com/scottjehl/Respond/master/test/test.html) (the colors change to show media queries working)


Usage Instructions
======

1. Craft your CSS with min/max-width media queries to adapt your layout from mobile (first) all the way up to desktop


<pre>
    @media screen and (min-width: 480px){
        ...styles for 480px and up go here
    }
</pre>

2. Reference the respond.min.js script (1kb min/gzipped) after all of your CSS (the earlier it runs, the greater chance IE users will not see a flash of un-media'd content)

3. Crack open Internet Explorer and pump fists in delight


CDN/X-Domain Setup
======

Respond.js works by requesting a pristine copy of your CSS via AJAX, so if you host your stylesheets on a CDN (or a subdomain), you'll need to upload a proxy page to enable cross-domain communication.

See `cross-domain/example.html` for a demo:

- Upload `cross-domain/respond-proxy.html` to your external domain
- Upload `cross-domain/respond.proxy.gif` to your origin domain
- Reference the file(s) via `<link />` element(s):

<pre>
	&lt;!-- Respond.js proxy on external server --&gt;
	&lt;link href=&quot;http://externalcdn.com/respond-proxy.html&quot; id=&quot;respond-proxy&quot; rel=&quot;respond-proxy&quot; /&gt;

	&lt;!-- Respond.js redirect location on local server --&gt;
	&lt;link href=&quot;/path/to/respond.proxy.gif&quot; id=&quot;respond-redirect&quot; rel=&quot;respond-redirect&quot; /&gt;

	&lt;!-- Respond.js proxy script on local server --&gt;
	&lt;script src="/path/to/respond.proxy.js"&gt;&lt;/script&gt;
</pre>

If you are having problems with the cross-domain setup, make sure respond-proxy.html does not have a query string appended to it.

Note: HUGE thanks to @doctyper for the contributions in the cross-domain proxy!


Support & Caveats
======

Some notes to keep in mind:

- This script's focus is purposely very narrow: only min-width and max-width media queries and all media types (screen, print, etc) are translated to non-supporting browsers. I wanted to keep things simple for filesize, maintenance, and performance, so I've intentionally limited support to queries that are essential to building a (mobile-first) responsive design. In the future, I may rework things a bit to include a hook for patching-in additional media query features - stay tuned!

- Browsers that natively support CSS3 Media Queries are opted-out of running this script as quickly as possible. In testing for support, all other browsers are subjected to a quick  test to determine whether they support media queries or not before proceeding to run the script. This test is now included separately at the top, and uses the window.matchMedia polyfill found here: https://github.com/paulirish/matchMedia.js . If you are already including this polyfill via Modernizr or otherwise, feel free to remove that part.

- This script relies on no other scripts or frameworks (aside from the included matchMedia polyfill), and is optimized for mobile delivery (~1kb total filesize min/gzip)

- As you might guess, this implementation is quite dumb in regards to CSS parsing rules. This is a good thing, because that allows it to run really fast, but its looseness may also cause unexpected behavior. For example: if you enclose a whole media query in a comment intending to disable its rules, you'll probably find that those rules will end up enabled in non-media-query-supporting browsers.

- Respond.js doesn't parse CSS referenced via @import, nor does it work with media queries within style elements, as those styles can't be re-requested for parsing.

- Due to security restrictions, some browsers may not allow this script to work on file:// urls (because it uses xmlHttpRequest). Run it on a web server.

- If the request for the CSS file that includes MQ-specific styling is
  behind a redirect, Respond.js will fail silently. CSS files should
respond with a 200 status.

- Currently, media attributes on link elements are supported, but only if the linked stylesheet contains no media queries. If it does contain queries, the media attribute will be ignored and the internal queries will be parsed normally. In other words, @media statements in the CSS take priority.

- Reportedly, if CSS files are encoded in UTF-8 with Byte-Order-Mark (BOM), they will not work with Respond.js in IE7 or IE8. Noted in issue #97

- WARNING: Including @font-face rules inside a media query will cause IE7 and IE8 to hang during load. To work around this, place @font-face rules in the wide open, as a sibling to other media queries.

- If you have more than 32 stylesheets referenced, IE will throw an error, `Invalid procedure call or argument`. Concatenate your CSS and the issue should go away.

- Sass/SCSS source maps are not supported; `@media -sass-debug-info` will break respond.js. Noted in issue [#148](https://github.com/scottjehl/Respond/issues/148)

- Internet Explorer 9 supports css3 media queries, but not within frames when the CSS containing the media query is in an external file (this appears to be a bug in IE9 — see http://stackoverflow.com/questions/10316247/media-queries-fail-inside-ie9-iframe). See this commit for a fix if you're having this problem. https://github.com/NewSignature/Respond/commit/1c86c66075f0a2099451eb426702fc3540d2e603

- Nested Media Queries are not supported


How's it work?
======
Basically, the script loops through the CSS referenced in the page and runs a regular expression or two on their contents to find media queries and their associated blocks of CSS. In Internet Explorer, the content of the stylesheet is impossible to retrieve in its pre-parsed state (which in IE 8-, means its media queries are removed from the text), so Respond.js re-requests the CSS files using Ajax and parses the text response from there. Be sure to configure your CSS files' caching properly so that this re-request doesn't actually go to the server, hitting your browser cache instead.

From there, each media query block is appended to the head in order via style elements, and those style elements are enabled and disabled (read: appended and removed from the DOM) depending on how their min/max width compares with the browser width. The media attribute on the style elements will match that of the query in the CSS, so it could be "screen", "projector", or whatever you want. Any relative paths contained in the CSS will be prefixed by their stylesheet's href, so image paths will direct to their proper destination

API Options?
======
Sure, a couple:

- respond.update() : rerun the parser (helpful if you added a stylesheet to the page and it needs to be translated)
- respond.mediaQueriesSupported: set to true if the browser natively supports media queries.
- respond.getEmValue() : returns the pixel value of one em


Alternatives to this script
======
This isn't the only CSS3 Media Query polyfill script out there; but it damn well may be the fastest.

If you're looking for more robust CSS3 Media Query support, you might check out http://code.google.com/p/css3-mediaqueries-js/. In testing, I've found that script to be noticeably slow when rendering complex responsive designs (both in filesize and performance), but it really does support a lot more media query features than this script. Big hat tip to the authors! :)
