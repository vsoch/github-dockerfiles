# Architecture Decision Records

- [ADR 1: Adopting Architecture Decision Records](adr-1.md)
- [ADR 2: Considering options to migrate from Next.js to another server-side rendering (SSR) framework](adr-2.md)
- [ADR 3: Designing a new auth client](adr-3.md)
- [ADR 4: Browser support](adr-4.md)
- [ADR 5: Implementing workflows in the new classifier](adr-5.md)
- [ADR 6: Organizing translations to be volunteer and dev friendly](adr-6.md)
- [ADR 7: Managing changes to classification tools](adr-7.md)
- [ADR 8: Building the TESS Light Curve Viewer](adr-8.md)
- [ADR 9: Classifier - Logic for Selecting a Subject Viewer](adr-9.md)
- [ADR 10: Type conversions from Mobx-State-Tree to JSON API for Javascript Maps](adr-10.md)
# Zooniverse Front End - Project

A [Next.js](https://github.com/zeit/next.js) app for handling the project routes, including classification.

## Getting started

This package should be cloned as part of the [front-end-monorepo](https://github.com/zooniverse/front-end-monorepo).

### Running in development

```sh
npm run dev
```

Starts a development server on port 3000 by default.

### Running in production

```sh
npm run build
npm run start
```

Next.js [treats the build and serve tasks as separate steps](https://github.com/zeit/next.js/#production-deployment) when running in production.

The production server is started on port 3000 by default.

### Tests

```sh
npm run test
```

See [Testing](#testing) for more details.

## <a name="testing"></a> Testing

Tests are run by [Mocha](https://mochajs.org/), using the [BDD](https://mochajs.org/#bdd) interface.

Assertions are provided by the [Chai](http://www.chaijs.com/) assertion library.
# ClassifyBox

A common box component for widgets on the Classify page.
# Zooniverse Grommet Theme

A Zooniverse theme for the [Grommet 2.0](https://grommet.github.io/) React component library.

## Contributing

Run `npm start` to run a script that watches for changes in the source and reruns the babel compiler. 

## Usage

To use this theme, import it and pass it as a prop to the top-level `Grommet` component:

```javascript

import { Button, Grommet } from 'grommet'
import React from 'react'
import grommetTheme from '@zooniverse/grommet-theme'

class MyComponent extends React.Component {
  render() {
    return (
      <Grommet theme={grommetTheme}>
        <Button color="teal" label="Click me!" />
      </Grommet>
    )
  }
}

```

## Development

Run `npm start` to run a script that watches for changes in the source and reruns the babel compiler.

## License

Copyright 2018 Zooniverse

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# Zooniverse React Components

Common React components used throughout the Zooniverse.

## Getting Started

Install the package from NPM:

```
npm i @zooniverse/react-components
```

and use it

ES5

```
var { ZooFooter } = require('@zooniverse/react-components');
```

ES6

```
import { ZooFooter } from '@zooniverse/react-components';
```

## Tests

`npm test` to run mocha tests

If you're using `npm link` to test the library with your app, then you may need to adjust your webpack configuration for compiling of your javascript files in development. Webpack docs do provide a cautionary note about using symlink packages with Webpack: https://webpack.js.org/configuration/module/#rule-conditions. An example webpack configuration:

```
{
  test: /\.jsx?$/,
  include: path.resolve(__dirname, 'src'),
  exclude: path.resolve(__dirname, 'node_modules'),
  use: [
    'babel-loader'
    // 'eslint-loader' uncomment if you want to use eslint while compiling
  ]
}
```

## Contributing

Components should be added to the `src/components` folder and an export to `src/index.js`

Any default styles can be added as a stylus file in `src/css`.

`npm version [semver new version]` will run helper preversion and postversion scripts. `preversion` will run the tests. `version` will run `npm run build` which will build the production css and js. `postversion` will push the updated repo and the updated git tag to github.

For now, we will git tag and install via github. 
The standard Zooniverse footer to be used on Zooniverse sites. Built using:

- [React](http://reactjs.org/)
- [Grommet v2](https://v2.grommet.io/components)
- [styled-components](https://www.styled-components.com/)
- [styled-theming](https://github.com/styled-components/styled-theming)
- @zooniverse/grommet-theme

The `ZooFooter` has two available theme variants with the light and dark themes provide in @zooniverse/grommet-theme. The theme defaults to `light` in its `colorTheme` prop. If you want to toggle between the themes, you must update the `colorTheme` prop to `dark`. How to manage the state of which theme is set is up to the consuming app. 

### Props

The navigation list props (the props ending with `URLs`) are available to you to have flexibility with absolute or relative links. The default props use absolute links. For translations, the `en.json` is in the `locales` folder and additional locales can be added there for additional language support. 
## AdminCheckbox

If you're working on a front-end app where being able to toggle admin mode would be useful, then build an AdminCheckboxContainer component using the state management of your choice and use AdminCheckbox as the rendered view. Pass your AdminCheckboxContainer component down as a prop to the ZooFooter and it will be rendered correctly. Be sure to pass down the props that AdminCheckbox is expecting.
# `ZooniverseLogotype`

A component that renders the Zooniverse logotype / wordmark as an SVG.

## Props

- `id` (Required) - a unique id used to correctly label the component for screen readers.
- `width` - desired width of the logotype. The height is calculated based on the SVG `viewBox`
# SpacedText

Creates the wider-kerned text used in titles etc. Reuses the Grommet `Text` component, and accepts the same props. Additionally, it sets the following props by default:

```js
{
  margin: 'none',
  size: 'small',
  weight: 'normal'
}
```

## Example

```js
<SpacedText>
  Letter-spaced title
</SpacedText>
```
`Tooltip` uses Grommet's [`Drop`](https://v2.grommet.io/drop) and [`Box`](https://v2.grommet.io/box) components. The `Drop` is the outer component that determines the position and function of the tooltip. The `Box` is the inner component that wraps the content or nodes passed as children to provide basic layout and styles. 

## Props

- `align` (object) - the `Drop` `align` prop
- `boxAlign` (string) - the inner `Box` `align` prop. Default: `'center'`
- `boxAnimation` (string or object) - the inner `Box` `animation` 
- `boxBackgroundColor` (string) - passed to the inner `Box` `background` prop. Set it to either the zooTheme's light or dark background or something else. The zooTheme handles the font color automatically for you depending on the light or dark background. Default: `'white'`
- `boxPad` (string or object) - the inner `Box` `pad`. Default: `{ vertical: "xsmall", horizontal: "small" }`
- `children` (string or node) - The content of the Tooltip, either just a string or text or more HTML or React nodes. Required.
- `target` (React ref object) - the `Drop` `target` prop. Required. Note that this does not work with the newest React Ref API, `React.createRef()`.

The `Tooltip` component passes any additional props to `Drop`
# Modal

![modal screenshot](screenshot.png)

A generic modal component. Accepts the following props:

- `active` (boolean) - determines whether the modal is visible or not
- `closeFn` (function) - function called when clicking outside the modal, or when the Esc button is pressed
- `colorTheme` (string) - color theme to use with the modal. Defaults to `light`
- `theme` (object) - Grommet theme to use. Defaults to `@zooniverse/grommet-theme`
- `title` (string) - string to use as the modal title

## Example

```js
<Modal active={isActive} closeFn={setActive} title={title}>
  Leo mollis dictum id dis maecenas consectetur metus elementum vivamus nisl
</Modal>
```

## Notes

This component uses the Grommet `Layer` component, which in turn uses React Portals for rendering. Enzyme doesn't currently support portals, so the modal is wrapped by default in a HOC which provides the Layer, and also exported as a named default for testing.
The standard Zooniverse header to be used on Zooniverse sites. Built using:

- [React](http://reactjs.org/)
- [Grommet v2](https://v2.grommet.io/components)
- [styled-components](https://www.styled-components.com/)

The header does not have light and dark theme variants. It remains black for both. 

The `signIn` (function), `signOut` (function), and `user` (object) props are required. These props can be defined using the API from @zooniverse/auth. See the development mini-app in the lib-auth folder for an example of using its API.# `ZooniverseLogo`

A component that renders the circular Zooniverse logo as an SVG.

## Props

- `id` (Required) - a unique id used to correctly label the component for screen readers.
- `size` - desired size of the logo. The SVG produced is square, so the same value is used for height and width. Defaults to `1em`.
# SpacedText

Creates the wider-kerned text used in titles etc. Reuses the Grommet `Text` component, and accepts the same props. Additionally, it sets the following props by default:

```js
{
  margin: 'none',
  size: 'small',
  weight: 'normal'
}
```

## Example

```js
<SpacedText>
  Letter-spaced title
</SpacedText>
```
The standard Zooniverse footer to be used on Zooniverse sites. Built using:

- [React](http://reactjs.org/)
- [Grommet v2](https://v2.grommet.io/components)
- [styled-components](https://www.styled-components.com/)
- [styled-theming](https://github.com/styled-components/styled-theming)
- @zooniverse/grommet-theme

The `ZooFooter` has two available theme variants with the light and dark themes provide in @zooniverse/grommet-theme. The theme defaults to `light` in its `colorTheme` prop. If you want to toggle between the themes, you must update the `colorTheme` prop to `dark`. How to manage the state of which theme is set is up to the consuming app. 

### Props

The navigation list props (the props ending with `URLs`) are available to you to have flexibility with absolute or relative links. The default props use absolute links. For translations, the `en.json` is in the `locales` folder and additional locales can be added there for additional language support. 
## AdminCheckbox

If you're working on a front-end app where being able to toggle admin mode would be useful, then build an AdminCheckboxContainer component using the state management of your choice and use AdminCheckbox as the rendered view. Pass your AdminCheckboxContainer component down as a prop to the ZooFooter and it will be rendered correctly. Be sure to pass down the props that AdminCheckbox is expecting.

### Props

| prop     | propType        | default      | notes |
|----------|-----------------|--------------|-------|
| checked  | PropTypes.bool  | false        |       |
| colorTheme | PropTypes.string  | 'light'  | For toggling between the Zooniverse light and dark themes |
| label    | PropTypes.string | 'Admin Mode' |       |
| onChange | PropTypes.func  | () => {}     |       |The standard Zooniverse footer to be used on Zooniverse sites. Built using:

- [React](http://reactjs.org/)
- [Grommet v2](https://v2.grommet.io/components)
- [styled-components](https://www.styled-components.com/)
# Modal

![modal screenshot](screenshot.png)

A generic modal component. Accepts the following props:

- `active` (boolean) - determines whether the modal is visible or not
- `closeFn` (function) - function called when clicking outside the modal, or when the Esc button is pressed
- `colorTheme` (string) - color theme to use with the modal. Defaults to `light`
- `theme` (object) - Grommet theme to use. Defaults to `@zooniverse/grommet-theme`
- `title` (string) - string to use as the modal title

## Example

```js
<Modal active={isActive} closeFn={setActive} title={title}>
  Leo mollis dictum id dis maecenas consectetur metus elementum vivamus nisl
</Modal>
```

## Notes

This component uses the Grommet `Layer` component, which in turn uses React Portals for rendering. Enzyme doesn't currently support portals, so the modal is wrapped by default in a HOC which provides the Layer, and also exported as a named default for testing.
# SpacedText

Creates the wider-kerned text used in titles etc. Reuses the Grommet `Text` component, and accepts the same props. Additionally, it sets the following props by default:

```js
{
  margin: 'none',
  size: 'small',
  weight: 'normal'
}
```

## Example

```js
<SpacedText>
  Letter-spaced title
</SpacedText>
```
The standard Zooniverse footer to be used on Zooniverse sites. Built using:

- [React](http://reactjs.org/)
- [Grommet v2](https://v2.grommet.io/components)
- [styled-components](https://www.styled-components.com/)
- [styled-theming](https://github.com/styled-components/styled-theming)
- @zooniverse/grommet-theme

The `ZooFooter` has two available theme variants with the light and dark themes provide in @zooniverse/grommet-theme. The theme defaults to `light` in its `colorTheme` prop. If you want to toggle between the themes, you must update the `colorTheme` prop to `dark`. How to manage the state of which theme is set is up to the consuming app. 

### Props

The navigation list props (the props ending with `URLs`) are available to you to have flexibility with absolute or relative links. The default props use absolute links. For translations, the `en.json` is in the `locales` folder and additional locales can be added there for additional language support. 
## AdminCheckbox

If you're working on a front-end app where being able to toggle admin mode would be useful, then build an AdminCheckboxContainer component using the state management of your choice and use AdminCheckbox as the rendered view. Pass your AdminCheckboxContainer component down as a prop to the ZooFooter and it will be rendered correctly. Be sure to pass down the props that AdminCheckbox is expecting.

### Props

| prop     | propType        | default      | notes |
|----------|-----------------|--------------|-------|
| checked  | PropTypes.bool  | false        |       |
| colorTheme | PropTypes.string  | 'light'  | For toggling between the Zooniverse light and dark themes |
| label    | PropTypes.string | 'Admin Mode' |       |
| onChange | PropTypes.func  | () => {}     |       |The standard Zooniverse footer to be used on Zooniverse sites. Built using:

- [React](http://reactjs.org/)
- [Grommet v2](https://v2.grommet.io/components)
- [styled-components](https://www.styled-components.com/)
# Modal

![modal screenshot](screenshot.png)

A generic modal component. Accepts the following props:

- `active` (boolean) - determines whether the modal is visible or not
- `closeFn` (function) - function called when clicking outside the modal, or when the Esc button is pressed
- `colorTheme` (string) - color theme to use with the modal. Defaults to `light`
- `theme` (object) - Grommet theme to use. Defaults to `@zooniverse/grommet-theme`
- `title` (string) - string to use as the modal title

## Example

```js
<Modal active={isActive} closeFn={setActive} title={title}>
  Leo mollis dictum id dis maecenas consectetur metus elementum vivamus nisl
</Modal>
```

## Notes

This component uses the Grommet `Layer` component, which in turn uses React Portals for rendering. Enzyme doesn't currently support portals, so the modal is wrapped by default in a HOC which provides the Layer, and also exported as a named default for testing.
# `@zooniverse/async-states`

Provides a handy immutable object for describing the state of an asynchronous request.

Available states are:

- `initialized`
- `loading`
- `success`
- `error`

## Usage

Use the `asyncStates` object to provide the strings to describe the state of your request, rather than defining them locally. For example:

```js
import asyncStates from '@zooniverse/async-states'

let requestState = asyncStates.initialized

function asyncRequest () {
  requestState = asyncStates.loading
  fetchSomething()
    .then(() => requestState.success)
    .catch(() => requestState.error)
}
```
# @zooniverse/auth

## OAuth (Implicit Grant)

Use this for custom projects, and anything else not running on the zooniverse.org domain.

### How to Use

```
import { createOAuthClient } from '@zooniverse/auth'

const auth = createOAuthClient({
  authorizationUri: 'http://meepmorop.com/oauth/authorize' // (Optional) Sets a custom OAuth endpoint to use. Must be set if `env` is not set
  clientId: '1234567890', // Your client ID from Doorkeeper
  env: 'staging', // (Optional) Can be `staging` or `production`. This must be set if `authorizationUri` is not set
  redirectUri: 'http://foobar.com/oauth' // The URI you want the user redirected to on completion
  scopes: ['public', 'user'] // The scopes you want to grant your app. Defaults to `['public', 'user']`
})

// Start the login process
auth.startLogin()

// Complete the login process after being redirected back
auth.completeLogin()

// Get the current token details
auth.getToken()

// Logout (will trash token details, but won't logout on Doorkeeper)
auth.logout()

// Unmount the React app and trash all details. You probably won't need this, but it's included for completeness.
auth.destroy()
```

## Links

### Doorkeeper (register new OAuth clients)

- [Staging](https://panoptes-staging.zooniverse.org/oauth/applications)
- [Production](https://panoptes.zooniverse.org/oauth/applications)
# `dev`

This folder contains a dummy html file and wrapper for the classifier to use when developing locally via `npm run dev`.
# `views`

Contains the React apps that make up the client frontend. These are mostly popups for login, logout, session expiry and so on.
# AuthClientContext

The OAuth client returned by [js-client-oauth2](https://github.com/mulesoft/js-client-oauth2) is:

a) a non-serializable object
b) not part of the app state

...so we're not going to try and shoehorn it into `mobx-state-tree`'s volatile state or similar. Instead, we leverage the new [React 16 Context API](https://reactjs.org/docs/context.html) to pass it down the component tree.

We don't have access to the client at this point, so the initial value is an empty object.
# `dev`

This folder contains a dummy html file and wrapper for the classifier to use when developing locally via `npm run dev`.
# Service Workers

This folder contains the functionality for any service workers we want to define and run for the classifier. Service workers are scripts that can be run by the browser independently from any web page. Currently, almost all of the features for [service workers are supported by all major browsers](https://jakearchibald.github.io/isserviceworkerready/) except for the [Background Sync API](https://developer.mozilla.org/en-US/docs/Web/API/SyncManager) which is only supported by Google as of November 2018. Background Sync API is under development by [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/platform/status/backgroundsyncapi/) and [Mozilla](https://bugzilla.mozilla.org/show_bug.cgi?id=1217544) and once one of them implements it, it will be put onto the standards track. 

## Worker lifecycle

Service workers have a registration event that is required to install and run them by the browser. Line 25 in `Classifier.js` checks for Background Sync API support, then calls the registerWorkers function. We check for Background Sync API support since the only worker we have defined right now is the queue worker which relys on this API. In the future if we add more service workers, we may want to refactor this feature detection.

In `registerWorkers.js`, an event listener is added to the window load event, service worker support is detected, then if service workers are supported, then `queue.js` worker is registered.

## Current workers

**`queue.js`**

This is the classification POST failure queue worker. It uses [Google workbox background sync worker](https://developers.google.com/web/tools/workbox/modules/workbox-background-sync) which adds an event listener to fetch events, checks if the request is a POST to the Panopts classifications endpoint, then if the `request.ok` is false or if the request Promise is rejected, then the request gets pushed into the queue, which stores it in IndexedDB. The worker then relys on background sync which can be triggered by a change in network connectivity going back online or just gets periodicly scheduled for reattempts. Note that this worker is only supported by Google Chrome. We have another queuing strategy for all other browsers. [Read about that strategy](../stores/utils/README.md) in the README.md in the store utils folder.

Note that the strategy is to have a failed queue for classifications, not queue of initial POST requests. A queue of waiting POSTs could potentially submit multiple classifications for the same initially classification (see: [zooniverse/Panoptes-Front-End#4911](https://github.com/zooniverse/Panoptes-Front-End/issues/4911)). The failure queue handles all failures except for HTTP 422. This indiciates the classification data is malformed, so those are permanently dropped. A future enhancement would be to add a log to a logging service for 422s. 

# Store utilities

## ClassificationQueue

The `ClassificationQueue` class is the failed classification queue strategy for Firefox, Safari, and Edge browser users. When a user hits submit on a classification, the event handler feature detects for Background Sync API. If it is not supported, then the classification data is added to any pending classifications waiting to be submitted by this class. A `Promise.all` is called to attempt pending classifications, then any failures are added to a retry queue that is stored in `localStorage`.

Note that it is specifically the classification submit event that triggers the queue and the queue only works during the user's session on the Zooniverse website. A new strategy using service workers and the Background Sync API is implemented for Google Chrome users. [Read about this strategy](../../workers/README.md) in the README for service workers. 

We only store failures in `localStorage`, because a pending queue of new POSTs can potentially submit multiple classifications for the same classification. (see: [zooniverse/Panoptes-Front-End#4911](https://github.com/zooniverse/Panoptes-Front-End/issues/4911)). 422 responses from Panoptes are permanently dropped. # Tabs

These are [Grommet's Tab components](https://github.com/grommet/grommet/tree/NEXT/src/js/components/Tabs) reskinned for use in the Classifier.

Usage remains the same:

```js
  import { Tabs, Tab } from './path/to/Tabs';

  <Tabs>
    <Tab title='Tab 1'>...</Tab>
    <Tab title='Tab 2'>...</Tab>
  </Tabs>
```
# Light Curve Viewer

The Light Curve Viewer is a variant of the Subject Viewer that's used to
display "light curve" data, which plots the brightness of a star over time.

The strength of the LCV over, say, a static image generated from the same
light curve data is that the LCV allows users to zoom in on different segments
of the data, at a very high precision.

The LCV was originally created by @shaun.a.noordin on Oct 2018, for the Planet
Hunters (2018/2019) project that's using data from TESS (NASA's Transiting
Exoplanet Survey Satellite)

## Features

The Light Curve Viewer...
- allows users to view light curve data (x-axis: brightness of a star, y-axis:
  time)
- allows users to zoom in and pan on the data

Note that the LCV is essentially a specialised subset of a generalised
"Scatterplot Viewer".

## External Setup: Workflows and Subjects

The Light Curve Viewer was originally designed to work with the TESS Planet
Hunters project. (Click [here](https://pfe-preview.zooniverse.org/projects/nora-dot-test/planet-finders-beta)
for the staging/development version.)

That project had a specific setup, which should be followed if we want to use
the LCV for other projects.

**Workflow**

The Workflow of the project had a configuration that specified to the Monorepo
Front End that the LCV should be used.

`workflow.configuration = { subject_viewer: 'lightcurve' }`

**Subject**

Each Subject has two files: an image file (which works as a "thumbnail" to be
seen on Talk) and a JSON file.

```
subject.locations = [
  { "image/png": "tess1234.png" },
  { "application/json": "tess1234.json" },
]
```

**JSON file**

The JSON file is a very, very basic structure of x-y coordinates.

```
//tess1234.json
{
  x: [1,2,3,4,5],
  y: [100,101,99,102,98]
}
```
# `locationValidator`

A custom prop type validator for subject locations, which are an array of objects each with a single key/value pair in the format `mimeType: uri`, e.g.:

```json
{
  "subject": {
    "locations": [
      {
        "image/jpg": "https://example.com/subject.jpg"
      }
    ]
  }
}
```

The function only tests for correctness, not whether the MIME type is supported, nor whether the URI exists.

## Usage

Use as an argument to `PropTypes.arrayOf`:

```js
import locationValidator from '../helpers/locationValidator'

MyComponent.propTypes = {
  subject: PropTypes.shape({
    locations: PropTypes.arrayOf(locationValidator)
  })
}
```
# ImageToolbar component

The toolbar used in conjunction with the `SubjectViewer` component to manipulate the subject.

Note - icons are taken from the [Simple Line Icons](http://simplelineicons.com/) set; this is an icon font, but the original SVGs [are available here](https://github.com/orchidsoftware/icons/tree/master/src/svg).
# createLocationCounts

A helper function that accepts a subject as an argument, and returns an object that lists the total number of locations for that subject, and the number of each type of location.

This is used to derive the correct subject viewer component for a given subject.
# Panoptes.js

A Javascript client for [Panoptes API](https://github.com/zooniverse/Panoptes) using [Superagent](https://github.com/visionmedia/superagent).

## Description

A new take on a javascript client for [Panoptes](https://github.com/zooniverse/Panoptes). This client is designed to be stateless. It is up to the consumers of the library to decide how to store the responses from Panoptes as state. 

TODO: Add documentation about consumer apps of this library like the classifier app.

## Getting Started

Install the client from NPM:

```
npm i @zooniverse/panoptes-js
```

and use it

ES5

```
var { panoptes } = require('@zooniverse/panoptes-js');
```

ES6

```
import { panoptes } from '@zooniverse/panoptes-js';
```

## Documentation

Full API documentation is avialable at []().

## Tests

Run the tests by command line:

```
npm test
```

Tests are run by [Mocha](https://mochajs.org/), using the [BDD](https://mochajs.org/#bdd) interface.

Assertions are provided by the [Chai](http://www.chaijs.com/) assertion library.

Panoptes API data fixture mocks are built on top of [superagent-mock](https://github.com/M6Web/superagent-mock) plugin.

Browser web standard emulation is provided by [JSDOM](https://github.com/jsdom/jsdom)

## Contributing

See the [contributing documentation](docs/CONTRIBUTING.md) for more information.

## License

Copyright 2018 Zooniverse

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


# Panoptes.js API

All of the following examples will be using ES6.

## Configuring your environment

There are currently options for running the client against the staging and production environments, which determine which endpoints are used for requests handled by the module. There are a few different ways to set which you want to use - **staging is the default environment**.

Note: There is a test environment specified in the config file, but it is set to use the same API hosts as staging. The test environment is specifically for automated test running.

The currently set environment is available from the config file exported as `env`.

### Setting the environment via URL parameter

If you're running the client in the browser, you can use the `env` URL parameter to override the current environment, like this:

```
// Default to staging
http://localhost:3000

// Switch to production
http://localhost:3000?env=production
```

If you're running an app using hash history, you'll need to add `?env=` before the `#`, like this:

```
http://localhost:3000?env=production#/classify
```

### Setting the environment via `PANOPTES_ENV`

This lets you choose a Panoptes environment in isolation from your Node environment, so you can use the production Panoptes API in development, for example.

```
PANOPTES_ENV=production npm run dev
```

This supersedes the `NODE_ENV` environment variable.

### Setting the environment via `NODE_ENV`

This is usually used for build processes before deployment.

```
NODE_ENV=production npm run build
```

### API host configurations

The available host configurations are:

``` javascript
{
  test: {
    host: 'https://panoptes-staging.zooniverse.org/api',
    oauth: 'https://panoptes-staging.zooniverse.org'
  },
  staging: {
    host: 'https://panoptes-staging.zooniverse.org/api',
    oauth: 'https://panoptes-staging.zooniverse.org'
  },
  production: {
    host: 'https://www.zooniverse.org/api',
    oauth: 'https://panoptes.zooniverse.org'
  }
}
```

## Base helpers

A base set of HTTP request functions are available from the `panoptes.js` file that set a standard set of headers and build the request URL for you. All of the request functions are preset with the following request headers:

- `Content-Type: application/json`
- `Accept: application/vnd.api+json; version=1`

All of the base helpers will take an `authorization` string parameter that will set as the `Authorization` header. This string should include the type and token, i.e. `Bearer 12345abcde`. See the docs for the specific helper you want to use for exact usage. The resource specific helpers may or may not take an `authorization` parameter depending on if it should or could be an authenticated request.

Request functions available:

- [GET](#get)
- [POST](#post)
- [PUT](#put)
- [DELETE](#delete)

This library also provides a set of helper functions per Panoptes resource, so it is unlikely you will need to use these base helpers directly unless you need to make a request that isn't already defined by the already existing helper functions. See the [resource helpers](#resource-helpers) section for more information.

### GET

**Function**

``` javascript
panoptes.get(endpoint, query, authorization, host)
```

**Arguments**

- endpoint _(string)_ - the API endpoint for the request. Required.
- query _(object)_ - an object of request query parameters. Optional.
- authorization _(string)_ - a string of the authorization type and token, i.e. `'Bearer 12345abcde'`. Optional.
- host _(string)_ - available to specifiy a different API host. Defaults to the hosts defined in the `config.js` file. Optional.

**Returns**

- Promise _(object)_ resolves to the API response with the resource, meta, links, and linked properties or the request error.

**Example**

Get many projects:

``` javascript
panoptes.get('/projects', { page: 2 }).then((response) => {
  // Do something with the response
});
```

Get a single project:

``` javascript
panoptes.get('/projects/1104', { include: 'avatar,background,owners' }).then((response) => {
  // Do something with the response
});
```

### POST

**Function**

``` javascript
panoptes.post(endpoint, data, authorization, host)
```

**Arguments**

- endpoint _(string)_ - the API endpoint for the request. Required.
- data _(object)_ - an object of data to send with the request. Optional.
- authorization _(string)_ - a string of the authorization type and token, i.e. `'Bearer 12345abcde'`. Optional.
- host _(string)_ - available to specify a different API host. Defaults to the hosts defined in the `config.js` file. Optional.

**Returns**

- Promise _(object)_ resolves to the API response with the resource, meta, links, and linked properties or the request error.

**Example**

Create a project:

``` javascript
panoptes.get('/projects', { private: true }).then((response) => {
  // Do something with the response
});
```

### PUT

**Function**

``` javascript
panoptes.post(endpoint, data, authorization, host)
```

**Arguments**

- endpoint _(string)_ - the API endpoint for the request. Required.
- data _(object)_ - an object of data to send with the request. Optional.
- authorization _(string)_ - a string of the authorization type and token, i.e. `'Bearer 12345abcde'`. Optional.
- host _(string)_ - available to specify a different API host. Defaults to the hosts defined in the `config.js` file. Optional.

**Returns**

- Promise _(object)_ resolves to the API response with the resource, meta, links, and linked properties or the request error.

**Example**

Update a project:

``` javascript
panoptes.put('/projects/1104', { display_name: 'Super Zoo' }).then((response) => {
  // Do something with the response
});
```

### DELETE

**Function**

``` javascript
panoptes.del(endpoint, authorization, host)
```

**Arguments**

- endpoint _(string)_ - the API endpoint for the request. Required.
- authorization _(string)_ - a string of the authorization type and token, i.e. `'Bearer 12345abcde'`. Optional.
- host _(string)_ - available to specify a different API host. Defaults to the hosts defined in the `config.js` file. Optional.

**Returns**

- Promise _(object)_ resolves to the API response with the resource, meta, links, and linked properties or the request error.

**Example**

Delete a project:

``` javascript
panoptes.del('/projects/1104').then((response) => {
  // Do something with the response
});
```

## Resource helpers

Using helper functions for a defined Panoptes resource in a React component. These resources have functions defined:

- [Projects](projects.md)
- [Subjects](subjects.md)
- [Tutorials](tutorials.md)

The API for resource helpers will include:

- **get** `projects.get()`
- **create** `projects.create()`
- **update** `project.update()`
- **delete** `projects.delete()`
- **endpoint** - a constant of the resource REST endpoint
- **mocks** - mocks or factories used for tests, usually including:
  - **responses** - constants for typical API responses
  - **resources** - constants for typical API resources
- Any additional common requests or helper functions. See specific documentation for that resource.

An example in a React component:

``` javascript
import React from 'react';
import { projects } from '@zooniverse/panoptes-js';

class MyComponent extends React.Component {
  constructor() {
    super();

    this.state = {
      project: {}
    };
  }

  componentDidMount() {
    projects.get({ id: '1104' }).then((response) => {
      this.setState({ project: response.body.projects[0] });
    }).catch((error) => {
      if (error.statusCode === 404) return null; // If you don't care about catching a 404
    });
  }

  render() {
    if (Object.keys(this.state.project).length === 0) {
      return (<p>Loading...</p>);
    }

    return (
      <div>
        <h1>{this.state.project.display_name}</h1>
      </div>
    )
  }
}
```
