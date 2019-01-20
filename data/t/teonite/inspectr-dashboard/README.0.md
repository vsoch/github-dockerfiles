# Documentation

## Table of Contents

- [General](general)
  - [**CLI Commands**](general/commands.md)
  - [Tool Configuration](general/files.md)
  - [Server Configurations](general/server-configs.md)
  - [Deployment](general/deployment.md) *(currently Heroku specific)*
  - [FAQ](general/faq.md)
  - [Gotchas](general/gotchas.md)
  - [Remove](general/remove.md)
- [Testing](testing)
  - [Unit Testing](testing/unit-testing.md)
  - [Component Testing](testing/component-testing.md)
  - [Remote Testing](testing/remote-testing.md)
- [CSS](css)
  - [PostCSS](css/postcss.md)
  - [CSS Modules](css/css-modules.md)
  - [sanitize.css](css/sanitize.md)
- [JS](js)
  - [Redux](js/redux.md)
  - [ImmutableJS](js/immutablejs.md)
  - [reselect](js/reselect.md)
  - [redux-saga](js/redux-saga.md)
  - [routing](js/routing.md)

## Overview

### Quickstart

1. First, let's kick the tyres by launching the sample _Repospective_ app
   bundled with this project to demo some of its best features:

    ```Shell
    npm run setup && npm start
    ```

1. Open [localhost:3000](http://localhost:3000) to see it in action.

    - Add a Github username to see Redux and Redux Sagas in action: effortless
      async state updates and side effects are now yours :)
    - Edit the file at `./app/containers/HomePage/index.js` so that the text of
      the `<Button>` component reads "Features!!!"... Hot Module Reloading gives
      you a feedback loop with your UI so smooth it's almost conversational!
    - Click your (newly emphatic) Features button to see React Router in action...
      Now you can share a direct link to that content privately over your LAN or
      globally addressable to any device, anywhere. Not bad for a locally-running
      Single Page App.

1. Time to build your own app: run

    ```shell
    npm run clean
    ```

    ...and use the built-in generators to start your first feature.

### Development

Run `$ npm start` to see your app at `localhost:3000`

### Building & Deploying

1. Run `$ npm run build`, which will compile all the necessary files to the
`build` folder.

2. Upload the contents of the `build` folder to your web server's root folder.

### Structure

The [`app/`](app) directory contains your entire application code, including CSS,
JavaScript, HTML and tests.

The rest of the folders and files only exist to make your life easier, and
should not need to be touched.

*(If they do have to be changed, please [submit an issue](https://github.com/mxstbr/react-boilerplate/issues)!)*

### CSS

Each component `import`s its styling dependencies from a co-located `styles.css`
module.

A production build transpiles these modules into page-specific CSS files (based
on which components are actually used), while any shared styles are automatically
extracted into a "common" stylesheet.

This means the leanest, fastest payload for your users.

See the [CSS documentation](./css/README.md) for more information about PostCSS
and CSS modules.

### JS

We bundle all your clientside scripts and chunk them into several files using
code splitting where possible. We then automatically optimize your code when
building for production so you don't have to worry about that.

See the [JS documentation](./js/README.md) for more information about the
JavaScript side of things.

### Testing

For a thorough explanation of the testing procedure, see the
[testing documentation](./testing/README.md)!

#### Performance testing

With the production server running (i.e. while `$ npm run serve` is running in
another tab), enter `$ npm run pagespeed` to run Google PageSpeed Insights and
get a performance check right in your terminal!

#### Browser testing

`$ npm run serve` makes your locally-running app globally available on the web
via a temporary URL: great for testing on different devices, client demos, etc!

#### Unit testing

Unit tests live in `test/` directories right next to the components being tested
and are run with `$ npm run test`.
# Introduction

The JavaScript ecosystem evolves at incredible speed: staying current can feel
overwhelming. So, instead of you having to stay on top of every new tool,
feature and technique to hit the headlines, this project aims to lighten the
load by providing a curated baseline of the most valuable ones.

Using React Boilerplate, you get to start your app with our community's current
ideas on what represents optimal developer experience, best practice, most
efficient tooling and cleanest project structure.

- [**CLI Commands**](commands.md)
- [Tool Configuration](files.md)
- [Server Configurations](server-configs.md)
- [Deployment](deployment.md) *(currently Heroku specific)*
- [FAQ](faq.md)
- [Gotchas](gotchas.md)

# Feature overview

## Quick scaffolding

Automate the creation of components, containers, routes, selectors and sagas -
and their tests - right from the CLI!

Run `$ npm run generate` in your terminal and choose one of the parts you want
to generate. They'll automatically be imported in the correct places and have
everything set up correctly.

> We use [plop] to generate new components, you can find all the logic and
templates for the generation in `internals/generators`.

[plop]: https://github.com/amwmedia/plop

## Instant feedback

Enjoy the best DX and code your app at the speed of thought! Your saved changes
to the CSS and JS are reflected instantaneously without refreshing the page.
Preserve application state even when you update something in the underlying code!

## Predictable state management

We use Redux to manage our applications state. We have also added optional
support for the [Chrome Redux DevTools Extension] – if you have it installed,
you can see, play back and change your action history!

[Chrome Redux DevTools Extension]: https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd

## Next generation JavaScript

Use ESNext template strings, object destructuring, arrow functions, JSX syntax
and more, today. This is possible thanks to Babel with the `es2015`, `stage-0`
and `react` presets!

## Next generation CSS

Write composable CSS that's co-located with your components using [CSS modules]
for complete modularity. Unique generated class names keep the specificity low
while eliminating style clashes. Ship only the styles that are used on the
visible page for the best performance.

[CSS modules]: ../css/css-modules.md

## Industry-standard routing

It's natural to want to add pages (e.g. `/about`) to your application, and
routing makes this possible. Thanks to [react-router] with [react-router-redux],
that's as easy as pie and the url is auto-synced to your application state!

[react-router]: https://github.com/reactjs/react-router
[react-router-redux]: https://github.com/reactjs/react-router-redux

# Optional extras

_Don't like any of these features? [Click here](remove.md)_

## Offline-first

The next frontier in performant web apps: availability without a network
connection from the instant your users load the app. This is done with a
ServiceWorker and a fallback to AppCache, so this feature even works on older
browsers!

> All your files are included automatically. No manual intervention needed
thanks to Webpack's [`offline-plugin`](https://github.com/NekR/offline-plugin)

### Add To Homescreen

After repeat visits to your site, users will get a prompt to add your application
to their homescreen. Combined with offline caching, this means your web app can
be used exactly like a native application (without the limitations of an app store).

The name and icon to be displayed are set in the `app/manifest.json` file.
Change them to your project name and icon, and try it!

## Performant Web Font Loading

If you simply use web fonts in your project, the page will stay blank until
these fonts are downloaded. That means a lot of waiting time in which users
could already read the content.

[FontFaceObserver](https://github.com/bramstein/fontfaceobserver) adds a class
to the `body` when the fonts have loaded. (see [`app.js`](../../app/app.js#L26-L36)
and [`App/styles.css`](../../app/containers/App/styles.css))

### Adding a new font

1. Either add the `@font-face` declaration to `App/styles.css` or add a `<link>`
tag to the [`index.html`](../../app/index.html). (Don't forget to remove the `<link>`
for Open Sans from the [`index.html`](../../app/index.html)!)

2. In `App/styles.css`, specify your initial `font-family` in the `body` tag
with only web-save fonts. In the `body.jsFontLoaded` tag, specify your
`font-family` stack with your web font.

3. In `app.js` add a `<fontName>Observer` for your font.

## Image optimization

Images often represent the majority of bytes downloaded on a web page, so image
optimization can often be a notable performance improvement. Thanks to Webpack's
[`image-loader`](https://github.com/tcoopman/image-webpack-loader), every PNG, JPEG, GIF and SVG images
is optimized.

See [`image-loader`](https://github.com/tcoopman/image-webpack-loader) to customize optimizations options.
# Testing

- [Unit Testing](unit-testing.md)
- [Component Testing](component-testing.md)
- [Remote Testing](remote-testing.md)

Testing your application is a vital part of serious development. There are a few
things you should test. If you've never done this before start with [unit testing](unit-testing.md).
Move on to [component testing](component-testing.md) when you feel like you
understand that!

We also support [remote testing](remote-testing.md) your local application,
which is quite awesome, so definitely check that out!

## Usage with this boilerplate

To test your application started with this boilerplate do the following:

1. Sprinkle `.test.js` files directly next to the parts of your application you
   want to test. (Or in `test/` subdirectories, it doesn't really matter as long
   as they are directly next to those parts and end in `.test.js`)

1. Write your unit and component tests in those files.

1. Run `$ npm run test` in your terminal and see all the tests pass! (hopefully)

There are a few more commands related to testing, checkout the [commands documentation](../general/commands.md#testing)
for the full list!
# JavaScript

## State management

This boilerplate manages application state using [Redux](redux.md), makes it
immutable with [`ImmutableJS`](immutablejs.md) and keeps access performant
via [`reselect`](reselect.md).

For managing asynchronous flows (e.g. logging in) we use [`redux-saga`](redux-saga.md).

For routing, we use [`react-router` in combination with `react-router-redux`](routing.md).

We include a generator for components, containers, sagas, routes and selectors.
Run `$ npm run generate` to choose from the available generators, and automatically
add new parts of your application!

> Note: If you want to skip the generator selection process,
  `$ npm run generate <generator>` also works. (e.g. `$ npm run generate route`)

### Learn more

- [Redux](redux.md)
- [ImmutableJS](immutablejs.md)
- [reselect](reselect.md)
- [redux-saga](redux-saga.md)
- [routing](routing.md)

## Architecture: `components` and `containers`

We adopted a split between stateless, reusable components called (wait for it...)
`components` and stateful parent components called `containers`.

### Learn more

See [this article](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)
by Dan Abramov for a great introduction to this approach.
# CSS

This boilerplate uses PostCSS as a CSS preprocessor with a few utility plugins
to make it "batteries included".

CSS Modules lets us embrace component encapsulation while sanitize.css gives us
data-driven cross-browser normalisation.

Learn more:

- [PostCSS](postcss.md)
- [CSS Modules](css-modules.md)
- [sanitize.css](sanitize.md)
- [stylelint.css](stylelint.md)
- [Using Sass](sass.md)
