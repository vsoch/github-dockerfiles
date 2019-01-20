# regenerator-runtime

Standalone runtime for
[Regenerator](https://github.com/facebook/regenerator)-compiled generator
and `async` functions.

To import the runtime as a module (recommended), either of the following
import styles will work:
```js
// CommonJS
const regeneratorRuntime = require("regenerator-runtime");

// ECMAScript 2015
import regeneratorRuntime from "regenerator-runtime";
```

To ensure that `regeneratorRuntime` is defined globally, either of the
following styles will work:
```js
// CommonJS
require("regenerator-runtime/runtime");

// ECMAScript 2015
import "regenerator-runtime/runtime";
```

To get the absolute file system path of `runtime.js`, evaluate the
following expression:
```js
require("regenerator-runtime/path").path
```
# Documentation

This directory contains Sharetribe documentation.

## Advanced configuration

Guides about advanced configurations.

#### [Using Amazon Simple Email Service with Simple Notification Service](./using-amazon-ses-with-sns.md)

This guide helps you to configure Amazon Simple Email Service to send emails and Simple Notification Service to receive bounce and spam notifications.

#### [Landing page](./landing-page.md)

This guide helps you to enable the landing page feature.

#### [Landing page JSON structure](./landing-page-structure.md)

This document describes the landing page structure JSON format.

#### [Configure Harmony service for availability management](./configure_harmony.md)

This guide instructs how to configure your marketplace to use [Harmony](https://www.github.com/sharetribe/harmony) service for availability management.

#### [Scheduled tasks](./scheduled_tasks.md)

This guide shows what scheduled tasks are required to properly run Sharetribe in production.

## Coding guidelines

Coding guidelines followed in this project.

#### [Supported browsers](./supported-browsers.md)

List of supported browsers.

#### [UI testing guidelines](./ui-testing.md)

Guidelines for writing new UI tests.

#### [SCSS coding guidelines](./scss-coding-guidelines.md)

Documentation of SCSS coding guidelines and directory structure.


## Technical documentation

Technical documentation of different components.

#### [Delayed Job Priorities](./delayed-job-priorities.md)

List of commonly used Delayed Job priorities.

#### [Feature flags](./feature-flags.md)

How to use feature flags in the code and how to enable/disable them.

#### [Client-side routes](./js-routes.md)

Documentation of how to use Rails routes in JavaScript code.

#### [Client-side translations](./js-translations.md)

Documentation of how to use translation in JavaScript code.

#### [Method deprecator](./method-deprecator.md)

How to deprecate old methods in the code.

#### [Testing](./testing.md)

This guide contains information how to run tests.

#### [Testing without Rails](./testing-without-rails.md)

This guide shows how to write fast RSpec tests without requiring Rails environment

#### [Upgrade Facebook SDK version](./upgrade-facebook-sdk-version.md)

This guide shows how upgrade the Facebook SDK version

#### [SessionContextStore](./session-context-store.md)

This document explains what is SessionContextStore, how and when to use it.

#### [Using Fakepal](./using-fakepal.md)

This guide shows how to use "Fakepal", which is a fake PayPal implementation that can be used for development purposes

## Process documentation

Documentation of the development process.

#### [How to handle Github issues](./how-to-handle-github-issues.md)

Documentation of the Github issue handling process followed by this project.

#### [Semantic versioning](./semantic-versioning.md)

Documentation of how Sharetribe applies Semantic versioning.
Please see parent directory [README.md](../README.md).

Building options
==========================
  1. Rails & React with hot reloading styleguide

  ```bash
  foreman start -f Procfile.hot
  ```
    > Currently runs all webpack configs options:
    > - webpack.client.config.js => .js & .css files to be imported in the Rails side
    > - webpack.server.config.js => server-bundle.js to be used if 'prerender: true'
    > - webpack.storybook.config.js => Hot reloading styleguide setup

  1. Rails & React
  ```bash
  foreman start -f Procfile.static
  ```
  > Currently runs build configs options
  > - webpack.client.config.js => .js & .css files to be imported in the Rails side
  > - webpack.server.config.js => server-bundle.js to be used if 'prerender: true'


  1. Creating Assets for Tests
  ```bash
  foreman start -f Procfile.spec
  ```
  > Currently runs build configs options
  > - webpack.client.config.js => .js & .css files to be imported in the Rails side
  > - webpack.server.config.js => server-bundle.js to be used if 'prerender: true'

If you need to debug the Rails parts of Sharetribe with [Pry](https://github.com/pry/pry), it's not possible with Foreman due to a [known compatibility issue](https://github.com/ddollar/foreman/pull/536). In this case we recommend running Rails with old-fashioned `rails server` and React builds with Foreman in a separate terminal. That way your `binding.pry` calls open nicely in the same window with the Rails process. Procfiles `Procfile.client-static` and `Procfile.client-hot` are configured for that, respective descriptions above apply.


Developing new components
==========================

Components are separated based on [Atomic design](http://bradfrost.com/blog/post/atomic-web-design/): _elements_ (aka atoms), _composites_ (aka molecules), and _sections_ (aka organisms).
- **Elements** are React components which are basic visual elements. For example: avatar image.
- **Composites** are combined elements. E.g. ProfileCard combining Avatar and Name atoms could be a composte.
- **Sections** are higher level composites. They are responsible for page sections like html5 tags do. (Think about ```<header>```, ```<footer>```, ```<main>```, ```<aside>```, and ```<section>```)

Later we might add template & page levels too.


You need to register new React components (e.g. "ExampleApp") for react_on_rails gem to recognize it.
```js
ReactOnRails.register({ ExampleApp });
```
Add it to _sharetribe/client/app/startup/clientRegistration.js_ and _serverRegistration.js_. Read more from [react_on_rails repository](https://github.com/shakacode/react_on_rails) and check [their example app](https://github.com/shakacode/react_on_rails/tree/master/spec/dummy).

New React components can be included to HAML and ERB files with '_react_component_':
```erb
<%= react_component("ExampleApp", props: @app_props_server_render, prerender: true, trace: true) %>
```

_webpack.server.config.js_ creates a _server-bundle.js_ file which is used by react_on_rails gem to create server-side rendering.

_webpack.client.config.js_ defines how component specific styles are extracted using ExtractTextPlugin (if you have imported style.css file in your React component). These generated files (_app-bundle.js_, _vendor-bundle.js_, and _app-bundle.css_) and they are saved to _sharetribe/app/assets/webpack_ folder.

For stylesheets, we are using [CSS Modules](https://github.com/css-modules/css-modules) and [PostCSS](https://github.com/postcss/postcss) with [cssnext](http://cssnext.io/).

We use [React Storybook](https://github.com/kadirahq/react-storybook) for a hot reloading component development environment, in `http://localhost:9001/`. See [instructions for writing stories](https://github.com/kadirahq/react-storybook#writing-stories), for example story see [OnboardingTopBar.story.js](app/components/OnboardingTopBar/OnboardingTopBar.story.js).

Publishing styleguide for preview
---------------------------------

Styleguide can be published as a static build, to be used for e.g. reviews by other team members. Running `npm run deploy-storybook` in `client` directory publishes styleguide from your branch to `https://sharetribe.github.io/sharetribe/[BRANCH_NAME]/`.

We're using a [custom fork](https://github.com/mporkola/storybook-deployer) of [Storybook deployer](https://github.com/kadirahq/storybook-deployer), modified to output different branches to different directories. The goal is to get it merged upstream, but it still requires some work.

Running tests
=============

Run full test suite:

```
npm run test
```

For TDD type of development, where you run the same test multiple times, you may want to use `npm run devspecs`, which runs only specs and runs them a bit faster.

```
npm run test:devspecs
```

Linting JavaScript and CSS files
================================

For static code linting, we use [ESLint](http://eslint.org/) for JavaScript code and [stylelint](http://stylelint.io/) for CSS code. The configuration can be found in `.eslintrc.js` and `.stylelintrc.js`, respectively.

You can run the linting with:

    npm run lint       # run both ESLint and stylelint
    npm run eslint     # run only ESLint
    npm run stylelint  # run only stylelint

Troubleshooting
===============

Changes in `variables.js` file don't seem to take an effect
-----------------------------------------------------------

Restarting foreman is needed when `variables.js` is changes

Changes in translations don't seem to take an effect
----------------------------------------------------

Run `rake assets:clobber` and restart foreman
