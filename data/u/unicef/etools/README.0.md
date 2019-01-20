[![Build Status](https://travis-ci.org/GoogleChrome/accessibility-developer-tools.svg?branch=master)](https://travis-ci.org/GoogleChrome/accessibility-developer-tools)
[![npm version](https://img.shields.io/npm/v/accessibility-developer-tools.svg)](https://www.npmjs.com/package/accessibility-developer-tools)
[![npm downloads](https://img.shields.io/npm/dm/accessibility-developer-tools.svg)](https://www.npmjs.com/package/accessibility-developer-tools)

# Accessibility Developer Tools

This is a library of accessibility-related testing and utility code.

Its main component is the accessibility audit: a collection of audit rules checking for common accessibility problems, and an API for running these rules in an HTML page.

There is also a collection of accessibility-related utility code, including but not limited to:
* contrast ratio calculation and color suggestions
* retrieving and validating ARIA attributes and states
* accessible name calculation using the algorithm at [http://www.w3.org/TR/wai-aria/roles#textalternativecomputation](http://www.w3.org/TR/wai-aria/roles#textalternativecomputation)

# Getting the code

To include just the javascript rules, require the following file:

    https://raw.github.com/GoogleChrome/accessibility-developer-tools/stable/dist/js/axs_testing.js

  `git 1.6.5` or later:

    % git clone --recursive https://github.com/GoogleChrome/accessibility-developer-tools.git

  Before `git 1.6.5`:

    % git clone https://github.com/GoogleChrome/accessibility-developer-tools.git
    % cd accessibility-developer-tools
    % git submodule init; git submodule update

# Building

You will need `node` and `grunt-cli` to build.

1. (Once only) Install [Node.js](http://nodejs.org/) and `npm` - useful instructions here: [https://gist.github.com/isaacs/579814](https://gist.github.com/isaacs/579814)

    Make sure you have Node.js v 0.8 or higher.

2. (Once only) Use `npm` to install `grunt-cli`

        % npm install -g grunt-cli  # May need to be run as root

3. (Every time you make a fresh checkout) Install dependencies (including `grunt`) for this project (run from project root)

        % npm install

4. (Rebuild if you make changes) Build using `grunt` (run from project root)

        % grunt


## Troubleshooting

This project uses [Closure Compiler](https://github.com/google/closure-compiler) to build our releases. You may need to install a recent version of [JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html) in order for builds to successfully complete.

# Using the Audit API

## Including the library

The simplest option is to include the generated `axs_testing.js` library on your page. After you build, you will have two versions of `axs_testings.js`:
* Distribution Build: project-root/dist/js/axs_testing.js
* Local Build (use if you make changes): project-root/tmp/build/axs_testing.js

Work is underway to include the library in WebDriver and other automated testing frameworks.

## The `axs.Audit.run()` method

Once you have included `axs_testing.js`, you can call `axs.Audit.run()`. This returns an object in the following form:

    {
      /** @type {axs.constants.AuditResult} */
      result,  // one of PASS, FAIL or NA

      /** @type {Array.<Element>} */
      elements,  // The elements which the rule fails on, if result == axs.constants.AuditResult.FAIL

      /** @type {axs.AuditRule} */
      rule  // The rule which this result is for.
    }

### Command Line Runner

The Accessibility Developer Tools project includes a command line runner for the audit. To use the runner, [install phantomjs](http://phantomjs.org/download.html) then run the following command from the project root directory.

    $ phantomjs tools/runner/audit.js <url-or-filepath>

The runner will load the specified file or URL in a headless browser, inject axs_testing.js, run the audit and output the report text.

### Run audit from Selenium WebDriver (Scala):
     val driver = org.openqa.selenium.firefox.FirefoxDriver //use driver of your choice
     val jse = driver.asInstanceOf[JavascriptExecutor]
     jse.executeScript(scala.io.Source.fromURL("https://raw.githubusercontent.com/GoogleChrome/" +
       "accessibility-developer-tools/stable/dist/js/axs_testing.js").mkString)
     val report = jse.executeScript("var results = axs.Audit.run();return axs.Audit.createReport(results);")
     println(report)

### Run audit from Selenium WebDriver (Scala)(with caching):
     val cache = collection.mutable.Map[String, String]()
     val driver = org.openqa.selenium.firefox.FirefoxDriver //use driver of your choice
     val jse = driver.asInstanceOf[JavascriptExecutor]
     def getUrlSource(arg: String): String = cache get arg match {
        case Some(result) => result
        case None =>
          val result: String = scala.io.Source.fromURL(arg).mkString
          cache(arg) = result
          result
      }
     jse.executeScript(getUrlSource("https://raw.githubusercontent.com/GoogleChrome/" +
       "accessibility-developer-tools/stable/dist/js/axs_testing.js"))
     val report = js.executeScript("var results = axs.Audit.run();return axs.Audit.createReport(results);")
     println(report)

If println() outputs nothing, check if you need to set DesiredCapabilities for your WebDriver (such as loggingPrefs):
https://code.google.com/p/selenium/wiki/DesiredCapabilities

## Using the results

### Interpreting the result

The result may be one of three constants:
* `axs.constants.AuditResult.PASS` - This implies that there were elements on the page that may potentially have failed this audit rule, but they passed. Congratulations!
* `axs.constants.AuditResult.NA` - This implies that there were no elements on the page that may potentially have failed this audit rule. For example, an audit rule that checks video elements for subtitles would return this result if there were no video elements on the page.
* `axs.constants.AuditResult.FAIL` - This implies that there were elements on the page that did not pass this audit rule. This is the only result you will probably be interested in.

### Creating a useful error message

The static, global `axs.Audit.createReport(results, opt_url)` may be used to create an error message using the return value of axs.Audit.run(). This will look like the following:

    *** Begin accessibility audit results ***
    An accessibility audit found 4 errors and 4 warnings on this page.
    For more information, please see https://github.com/GoogleChrome/accessibility-developer-tools/wiki/Audit-Rules

    Error: badAriaAttributeValue (AX_ARIA_04) failed on the following elements (1 - 3 of 3):
    DIV:nth-of-type(3) > INPUT
    DIV:nth-of-type(5) > INPUT
    #aria-invalid

    Error: badAriaRole (AX_ARIA_01) failed on the following element:
    DIV:nth-of-type(11) > SPAN

    Error: controlsWithoutLabel (AX_TEXT_01) failed on the following elements (1 - 3 of 3):
    DIV > INPUT
    DIV:nth-of-type(12) > DIV:nth-of-type(3) > INPUT
    LABEL > INPUT

    Error: requiredAriaAttributeMissing (AX_ARIA_03) failed on the following element:
    DIV:nth-of-type(13) > DIV:nth-of-type(11) > DIV

    Warning: focusableElementNotVisibleAndNotAriaHidden (AX_FOCUS_01) failed on the following element:
    #notariahidden

    Warning: imagesWithoutAltText (AX_TEXT_02) failed on the following elements (1 - 2 of 2):
    #deceptive-img
    DIV:nth-of-type(13) > IMG

    Warning: lowContrastElements (AX_COLOR_01) failed on the following elements (1 - 2 of 2):
    DIV:nth-of-type(13) > DIV
    DIV:nth-of-type(13) > DIV:nth-of-type(3)

    Warning: nonExistentAriaLabelledbyElement (AX_ARIA_02) failed on the following elements (1 - 2 of 2):
    DIV:nth-of-type(3) > INPUT
    DIV:nth-of-type(5) > INPUT
    *** End accessibility audit results ***

Each rule will have at most five elements listed as failures, in the form of a unique query selector for each element.

### Configuring the Audit

If you wish to fine-tune the audit, you can create an `axs.AuditConfiguration` object, with the following options:

#### Ignore parts of the page for a particular audit rule

For example, say you have a separate high-contrast version of your page, and there is a CSS rule which causes certain elements (with class `pretty`) on the page to be low-contrast for stylistic reasons. Running the audit unmodified produces results something like

    Warning: lowContrastElements (AX_COLOR_01) failed on the following elements (1 - 5 of 15):
    ...

You can modify the audit to ignore the elements which are known and intended to have low contrast like this:

    var configuration = new axs.AuditConfiguration();
    configuration.ignoreSelectors('lowContrastElements', '.pretty');
    axs.Audit.run(configuration);

The `AuditConfiguration.ignoreSelectors()` method takes a rule name, which you can find in the audit report, and a query selector string representing the parts of the page to be ignored for that audit rule. Multiple calls to `ignoreSelectors()` can be made for each audit rule, if multiple selectors need to be ignored.

#### Restrict the scope of the entire audit to a subsection of the page

You may have a part of the page which varies while other parts of the page stay constant, like a content area vs. a toolbar. In this case, running the audit on the entire page may give you spurious results in the part of the page which doesn't vary, which may drown out regressions in the main part of the page.

You can set a `scope` on the `AuditConfiguration` object like this:

    var configuration = new axs.AuditConfiguration();
    configuration.scope = document.querySelector('main');  // or however you wish to choose your scope element
    axs.Audit.run(configuration);

You may also specify a configuration payload while instantiating the `axs.AuditConfiguration`,
which allows you to provide multiple configuration options at once.

    var configuration = new axs.AuditConfiguration({
      auditRulesToRun: ['badAriaRole'],
      scope: document.querySelector('main'),
      maxResults: 5
    });

    axs.Audit.run(configuration);

## License

Copyright 2013 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
webcomponents.js
================

[![Build Status](https://travis-ci.org/webcomponents/webcomponentsjs.svg?branch=master)](https://travis-ci.org/webcomponents/webcomponentsjs)

A suite of polyfills supporting the [Web Components](http://webcomponents.org) specs:

**Custom Elements**: allows authors to define their own custom tags ([spec](https://w3c.github.io/webcomponents/spec/custom/)).

**HTML Imports**: a way to include and reuse HTML documents via other HTML documents ([spec](https://w3c.github.io/webcomponents/spec/imports/)).

**Shadow DOM**: provides encapsulation by hiding DOM subtrees under shadow roots ([spec](https://w3c.github.io/webcomponents/spec/shadow/)).

This also folds in polyfills for `MutationObserver` and `WeakMap`.


## Releases

Pre-built (concatenated & minified) versions of the polyfills are maintained in the [tagged versions](https://github.com/webcomponents/webcomponentsjs/releases) of this repo. There are two variants:

`webcomponents.js` includes all of the polyfills.

`webcomponents-lite.js` includes all polyfills except for shadow DOM.


## Browser Support

Our polyfills are intended to work in the latest versions of evergreen browsers. See below
for our complete browser support matrix:

| Polyfill   | IE10 | IE11+ | Chrome* | Firefox* | Safari 7+* | Chrome Android* | Mobile Safari* |
| ---------- |:----:|:-----:|:-------:|:--------:|:----------:|:---------------:|:--------------:|
| Custom Elements | ~ | ✓ | ✓ | ✓ | ✓ | ✓| ✓ |
| HTML Imports | ~ | ✓ | ✓ | ✓ | ✓| ✓| ✓ |
| Shadow DOM | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Templates | ✓ | ✓ | ✓ | ✓| ✓ | ✓ | ✓ |


*Indicates the current version of the browser

~Indicates support may be flaky. If using Custom Elements or HTML Imports with Shadow DOM,
you will get the non-flaky Mutation Observer polyfill that Shadow DOM includes.

The polyfills may work in older browsers, however require additional polyfills (such as classList)
to be used. We cannot guarantee support for browsers outside of our compatibility matrix.


### Manually Building

If you wish to build the polyfills yourself, you'll need `node` and `gulp` on your system:

 * install [node.js](http://nodejs.org/) using the instructions on their website
 * use `npm` to install [gulp.js](http://gulpjs.com/): `npm install -g gulp`

Now you are ready to build the polyfills with:

    # install dependencies
    npm install
    # build
    gulp build

The builds will be placed into the `dist/` directory.

## Contribute

See the [contributing guide](CONTRIBUTING.md)

## License

Everything in this repository is BSD style license unless otherwise specified.

Copyright (c) 2015 The Polymer Authors. All rights reserved.

## Helper utilities

### `WebComponentsReady`

Under native HTML Imports, `<script>` tags in the main document block the loading of such imports. This is to ensure the imports have loaded and any registered elements in them have been upgraded. 

The webcomponents.js and webcomponents-lite.js polyfills parse element definitions and handle their upgrade asynchronously. If prematurely fetching the element from the DOM before it has an opportunity to upgrade, you'll be working with an `HTMLUnknownElement`. 

For these situations (or when you need an approximate replacement for the Polymer 0.5 `polymer-ready` behavior), you can use the `WebComponentsReady` event as a signal before interacting with the element. The criteria for this event to fire is all Custom Elements with definitions registered by the time HTML Imports available at load time have loaded have upgraded.

```js
window.addEventListener('WebComponentsReady', function(e) {
  // imports are loaded and elements have been registered
  console.log('Components are ready');
});
```

## Known Issues

  * [Limited CSS encapsulation](#encapsulation)
  * [Element wrapping / unwrapping limitations](#wrapping)
  * [Custom element's constructor property is unreliable](#constructor)
  * [Contenteditable elements do not trigger MutationObserver](#contentedit)
  * [ShadowCSS: :host-context(...):host(...) doesn't work](#hostcontext)
  * [ShadowCSS: :host(.zot:not(.bar:nth-child(2))) doesn't work](#nestedparens)
  * [HTML imports: document.currentScript doesn't work as expected](#currentscript)
  * [execCommand isn't supported under Shadow DOM](#execcommand)

### Limited CSS encapsulation <a id="encapsulation"></a>
Under native Shadow DOM, CSS selectors cannot cross the shadow boundary. This means document level styles don't apply to shadow roots, and styles defined within a shadow root don't apply outside of that shadow root. [Several selectors](http://www.html5rocks.com/en/tutorials/webcomponents/shadowdom-201/) are provided to be able to deal with the shadow boundary.

The Shadow DOM polyfill can't prevent document styles from leaking into shadow roots. It can, however, encapsulate styles within shadow roots to some extent. This behavior isn't automatically emulated by the Shadow DOM polyfill, but it can be achieved by manually using the included ShadowCSS shim:

```
WebComponents.ShadowCSS.shimStyling( shadowRoot, scope );
```

... where `shadowRoot` is the shadow root of a DOM element, and `scope` is the name of the scope used to prefix the selectors. This removes all `<style>` elements from the shadow root, rewrites it rules using the given scope and reinserts the style as a document level stylesheet. Note that the `:host` and `:host-context` pseudo classes are also rewritten.

For a full explanation on the implementation and both the possibilities and the limitations of ShadowCSS please view the documentation in the [ShadowCSS source](src/ShadowCSS/ShadowCSS.js).

### Element wrapping / unwrapping limitations <a id="wrapping"></a>
The Shadow DOM polyfill is implemented by [wrapping](http://webcomponents.org/polyfills/shadow-dom/#wrappers) DOM elements whenever possible. It does this by wrapping methods like `document.querySelector` to return wrapped DOM elements. This has a few caveats:
   * Not _everything_ can be wrapped. For example, elements like `document`, `window`, `document.body`, `document.fullscreenElement` and others are non-configurable and thus cannot be overridden.
   * Wrappers don't support [live NodeLists](https://developer.mozilla.org/en-US/docs/Web/API/NodeList#A_sometimes-live_collection) like `HTMLElement.childNodes` and `HTMLFormElement.elements`. All NodeLists are snapshotted upon read. See [#217](https://github.com/webcomponents/webcomponentsjs/issues/217) for an explanation.

In order to work around these limitations the polyfill provides the `ShadowDOMPolyfill.wrap` and `ShadowDOMPolyfill.unwrap` methods to respectively wrap and unwrap DOM elements manually.

### Custom element's constructor property is unreliable <a id="constructor"></a>
See [#215](https://github.com/webcomponents/webcomponentsjs/issues/215) for background.

In Safari and IE, instances of Custom Elements have a `constructor` property of `HTMLUnknownElementConstructor` and `HTMLUnknownElement`, respectively. It's unsafe to rely on this property for checking element types.

It's worth noting that `customElement.__proto__.__proto__.constructor` is `HTMLElementPrototype` and that the prototype chain isn't modified by the polyfills(onto `ElementPrototype`, etc.)

### Contenteditable elements do not trigger MutationObserver <a id="contentedit"></a>
Using the MutationObserver polyfill, it isn't possible to monitor mutations of an element marked `contenteditable`.
See [the mailing list](https://groups.google.com/forum/#!msg/polymer-dev/LHdtRVXXVsA/v1sGoiTYWUkJ)

### ShadowCSS: :host-context(...):host(...) doesn't work <a id="hostcontext"></a>
See [#16](https://github.com/webcomponents/webcomponentsjs/issues/16) for background.

Under the shadow DOM polyfill, rules like:
```
:host-context(.foo):host(.bar) {...}
```
don't work, despite working under native Shadow DOM. The solution is to use `polyfill-next-selector` like:

```
polyfill-next-selector { content: '.foo :host.bar, :host.foo.bar'; }
```

### ShadowCSS: :host(.zot:not(.bar:nth-child(2))) doesn't work <a id="nestedparens"></a>
ShadowCSS `:host()` rules can only have (at most) 1-level of nested parentheses in its argument selector under ShadowCSS. For example, `:host(.zot)` and `:host(.zot:not(.bar))` both work, but `:host(.zot:not(.bar:nth-child(2)))` does not. 

### HTML imports: document.currentScript doesn't work as expected <a id="currentscript"></a>
In native HTML Imports, document.currentScript.ownerDocument references the import document itself. In the polyfill use document._currentScript.ownerDocument (note the underscore).

### execCommand and contenteditable isn't supported under Shadow DOM <a id="execcommand"></a>
See [#212](https://github.com/webcomponents/webcomponentsjs/issues/212)

`execCommand`, and `contenteditable` aren't supported under the ShadowDOM polyfill, with commands that insert or remove nodes being especially prone to failure.

<!---

This README is automatically generated from the comments in these files:


Edit those files, and our readme bot will duplicate them over here!
Edit this file, and the bot will squash your changes :)

The bot does some handling of markdown. Please file a bug if it does the wrong
thing! https://github.com/PolymerLabs/tedium/issues

-->

[![Build status](https://travis-ci.org/PolymerLabs/promise-polyfill.svg?branch=master)](https://travis-ci.org/PolymerLabs/promise-polyfill)


Quick Start
-----------

To provide native Chrome Web Animation features (`Element.animate` and Playback
Control) in other browsers, use `web-animations.min.js`. To explore all of the
proposed Web Animations API, use `web-animations-next.min.js`.

What is Web Animations?
-----------------------

Web Animations is a new JavaScript API for driving animated content on the web.
By unifying the animation features of SVG and CSS, Web Animations unlocks
features previously only usable declaratively, and exposes powerful,
high-performance animation capabilities to developers.

For more details see the
[W3C specification](http://w3c.github.io/web-animations/).

What is the polyfill?
---------------------

The polyfill is a JavaScript implementation of the Web Animations API. It is
supported on modern versions of all major browsers, including:

* Chrome
* Firefox 27+
* IE10+ (including Edge)
* Safari (iOS) 7.1+
* Safari (Mac) 9+

Getting Started
---------------

Here's a simple example of an animation that scales and changes the opacity of
a `<div>` over 0.5 seconds. The animation alternates producing a pulsing
effect.

```html
<script src="web-animations.min.js"></script>
<div class="pulse" style="width:150px;">Hello world!</div>
<script>
    var elem = document.querySelector('.pulse');
    var animation = elem.animate([
        {opacity: 0.5, transform: "scale(0.5)"},
        {opacity: 1.0, transform: "scale(1)"}
    ], {
        direction: 'alternate',
        duration: 500,
        iterations: Infinity
    });
</script>
```

Web Animations supports off-main-thread animations, and also allows procedural
generation of animations and fine-grained control of animation playback. See
<http://web-animations.github.io> for ideas and inspiration - or [web-animations-codelabs](https://github.com/web-animations/web-animations-codelabs).

Native Fallback
---------------

When the polyfill runs on a browser that implements `Element.animate` and
`Animation` Playback Control it will detect and use the underlying native
features.

Different Build Targets
-----------------------

### web-animations.min.js

Tracks the Web Animations features that are supported natively in browsers.
Today that means Element.animate and Playback Control in Chrome. If you’re not
sure what features you will need, start with this.

### web-animations-next.min.js

Contains all of web-animations.min.js plus features that are still undergoing
discussion or have yet to be implemented natively.

### web-animations-next-lite.min.js

A cut down version of web-animations-next, it removes several lesser used
property handlers and some of the larger and less used features such as matrix
interpolation/decomposition.

### Build Target Comparison

|                        | web-animations | web-animations-next | web-animations-next-lite |
|------------------------|:--------------:|:-------------------:|:------------------------:|
|Size (gzipped)          | 15KB           | 18KB                | 15KB                     |
|Element.animate         | ✔             | ✔                  | ✔                       |
|Timing input (easings, duration, fillMode, etc.) for animation effects| ✔ | ✔ | ✔             | 
|Playback control        | ✔             | ✔                  | ✔                       |
|Support for animating lengths, transforms and opacity| ✔ | ✔ | ✔                       |
|Support for animating other CSS properties| ✔ | ✔            | 🚫                       |
|Matrix fallback for transform animations | ✔ | ✔             | 🚫                       |
|KeyframeEffect constructor   | 🚫             | ✔                  | ✔                       |
|Simple GroupEffects & SequenceEffects           | 🚫             | ✔                  | ✔                       |
|Custom Effects          | 🚫             | ✔                  | ✔                       |
|Timing input (easings, duration, fillMode, etc.) for groups</div>| 🚫 | 🚫\* | 🚫         |
|Additive animation      | 🚫\*           | 🚫\*                | 🚫                       |
|Motion path             | 🚫\*           | 🚫\*                | 🚫                       |
|Modifiable keyframe effect timing| 🚫          | 🚫\*                | 🚫\*                     |
|Modifiable group timing | 🚫             | 🚫\*                | 🚫\*                     |
|Usable inline style\*\* | ✔             | ✔                  | 🚫                       |

\* support is planned for these features.
\*\* see inline style caveat below.

Caveats
-------

Some things won’t ever be faithful to the native implementation due to browser
and CSS API limitations. These include:

### Inline Style

Inline style modification is the mechanism used by the polyfill to animate
properties. Both web-animations and web-animations-next incorporate a module
that emulates a vanilla inline style object, so that style modification from
JavaScript can still work in the presence of animations. However, to keep the
size of web-animations-next-lite as small as possible, the style emulation
module is not included. When using this version of the polyfill, JavaScript
inline style modification will be overwritten by animations.
Due to browser constraints inline style modification is not supported on iOS 7
or Safari 6 (or earlier versions).

### Prefix handling

The polyfill will automatically detect the correctly prefixed name to use when
writing animated properties back to the platform. Where possible, the polyfill
will only accept unprefixed versions of experimental features. For example:

```js
var effect = new KeyframeEffect(elem, {"transform": "translate(100px, 100px)"}, 2000);
```

will work in all browsers that implement a conforming version of transform, but

```js
var effect = new KeyframeEffect(elem, {"-webkit-transform": "translate(100px, 100px)"}, 2000);
```

will not work anywhere.

API and Specification Feedback
------------------------------

File an issue on GitHub: <https://github.com/w3c/web-animations/issues/new>.
Alternatively, send an email to <public-fx@w3.org> with subject line
“[web-animations] … message topic …”
([archives](http://lists.w3.org/Archives/Public/public-fx/)).

Polyfill Issues
---------------

Report any issues with this implementation on GitHub:
<https://github.com/web-animations/web-animations-next/issues/new>.

Breaking changes
----------------

When we make a potentially breaking change to the polyfill's API
surface (like a rename) we will, where possible, continue supporting the
old version, deprecated, for three months, and ensure that there are
console warnings to indicate that a change is pending. After three
months, the old version of the API surface (e.g. the old version of a
function name) will be removed. *If you see deprecation warnings you
can't avoid it by not updating*.

We also announce anything that isn't a bug fix on
[web-animations-changes@googlegroups.com](https://groups.google.com/forum/#!forum/web-animations-changes).
# Management App

This app is currently meant to be used to flag potential issues (either bad data or policy violations).

## Classes involved

The main two important categories of things are *Issue Checks* (subclasses of `BaseIssueCheck`) and
*Flagged Issues* instances of `FlaggedIssue`.
**Both of these names might change soon.**

Issue checks represent *types* of issues that can be raised. Examples of issue checks might include
"an Agreement did not have a signed PCA attached to it" or "an Intervention failed validation".
**Issue checks live in code.**

However, each Issue check also has an associated `IssueCheckConfig` object.
The `IssueCheckConfig` is generated automatically, and is used to turn on/off issue checks at the database level
(instead of having to deploy code to turn on/off checks).
`IssueCheckConfig` objects are editable in the admin.

Flagged issues represent *instances* of an issue.
For example, "*This particular Agreement* did not have a signed PCA attached to it" or
"*this particular Intervention* failed validation".
Flagged issues are associated with an Issue Check by ID, and also point at an associated object in the database.

## High level function

There are two high-level functions - provided both as management commands and celery tasks.

### Check issues

`./manage.py check_issues`

This will run all Issue Checks against the entire database and create (or update) any relevant `FlaggedIssue` objects.
In the future this could be updated to only test since the last check.

### Recheck issues

`./manage.py recheck_issues`

This will re-run all checks against the current set of existing `FlaggedIssue` objects.
If the issue has been addressed the `FlaggedIssue`'s status will be set to "resolved".
Else it will stay active.

## Adding a new check

Adding a new check is a two step process:

1. Create a new subclass of `BaseIssueCheck` and implement the appropriate methods
2. Add the class to the list of `ISSUE_CHECKS` in settings/base.py

### Required methods

The jobs a check has are to:

1. Generate a set of potentially relevant objects that should be checked.
   This is used in the code that runs all checks (`./manage.py check_issues`).
2. Check an individual object.
   This is used both in the code that runs all checks (`./manage.py check_issues`) and the code that rechecks
   individual issues (`./manage.py recheck_issues`).

#### Getting relevant objects

Generally the issue check should return the smallest possible set of potential objects to check.
The `BaseIssueCheck` class provides two ways of implementing this: either by overriding `get_queryset`
or by overriding `get_objects_to_check`.

`get_queryset` should be overridden if the relevant set of objects can be easily represented in a single queryset,
and no additional metadata is required for the check (see below).

`get_objects_to_check` should be overridden if the relevant set of objects to check is too complex to represent
in a single queryset, or if additional metadata is needed (see below).

#### Checking an individual object

All issue checks must implement `run_check`, which takes an object, (optional) metadata, and should either
do nothing (if the check is successful) or raise an `IssueFoundException` if there is something wrong.

As mentioned above, this method is called during checking all issues as well as during rechecks.

#### Metadata

In some instances, the object itself is not enough information to run the check.
For example, when validating an `Intervention`'s lower result data matches the correct `CountryProgramme`
you need to know which `CountryProgramme` you are looking at.
In this scenario you should to include a dictionary of metadata with the check.

The metadata needs to be provided in two places:

1. In the `get_objects_to_check` function - so it can be passed during normal checks.
2. By overriding `get_object_metadata` in the issue check - so the metadata can be reconstructed from
   the `FlaggedIssue` object during rechecks.

See `PdOutputsWrongCheck` for an example of check metadata in use.
