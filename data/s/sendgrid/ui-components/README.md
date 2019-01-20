![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

# SendGrid UI Components

[![Twitter Follow](https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow)](https://twitter.com/sendgrid)
[![GitHub contributors](https://img.shields.io/github/contributors/sendgrid/docs.svg)](https://github.com/sendgrid/ui-components/graphs/contributors)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)


Re-useable React components based on the SendGrid Style Guide.
[Hosted StoryBook](https://sendgrid.github.io/ui-components)

## Getting Started with UI-components in your project

Make sure your project has all required dependencies and development dependencies installed.

Install devDependencies with:
```
yarn add node-sass -D
```

Install dependencies with:
```
yarn add lodash raf react react-animate-height react-color react-dom react-select @sendgrid/ui-components
```

### Using your local UI-components in your project

```bash
cd ~/ui-components/packages/ui-components
yarn link
> info You can now run `yarn link "@sendgrid/ui-components"` in the projects where you want to use this package and it will be used instead.
cd ~/ui-components/
npx tsc --newline lf --watch
```

```bash
cd ~/myCoolProject/
yarn link "@sendgrid/ui-components"
```

### Importing UI Components into Your Project

To import the component on your desired page:

```ts
import { Badge } from '@sendgrid/ui-components';
```

List of available components in [Available Components](#available-components) section.

### Importing a Particular Component

Maybe you don't want to import all of UI Components. You can import just the components that you need.

```js
import Badge from '@sendgrid/ui-components/badge';
```

### Getting Styles to Work

UI-Components uses a mix of module styles and global styles to insert style guide. To use module styles for each individual component, you'll need to update your webpack config to parse module styles from files with the naming convention ```.module.scss```.

```js
config.module.rules.push({
  test: /\.module.scss$/,
  use: [
    require.resolve('style-loader'),
    {
      loader: require.resolve('css-loader'),
      options: {
        sourceMap: true,
        importLoaders: 1,
        modules: true,
        localIdentName: '[name]__[local]___[hash:base64:5]',
      },
    },
    {
      loader: require.resolve('sass-loader'),
      options: {
        sourceMap: true,
        modules: true,
        importLoaders: 1,
        localIdentName: '[name]__[local]___[hash:base64:5]',
      },
    },
  ],
});
```

To use the global application styles included with styleguide (such as typography, reset, tables, and more), you'll need to include the following in your root component:

```js
import '../path_to_uicomponents/packages/styles/global/main.scss';
```

### Starting Storybook

After running `npm install` and ensuring that style-guide is pulled properly just run `npm run storybook` and you should be good to go!

### Adding Test Hooks

For many components, it's useful for testing to have attributes that make them easy to query for and select.

For this, use `attributes={{'data-test':"some-test-id}}"` as an attribute that describes the component. If it's possible, you can and should include the `data-test` attribute to create a unique identifier.

### What are these Stateful Components?

State is hard and all of the UI components should be purely presentational. But, that makes them hard to test out in Storybook. The stateful components (e.g. `StatefulTextInput`) are solely for working with Storybook and are not supported or endorsed in any way. Think of them as a private API. They can be removed at any time. You've been warned.

## Contributing to UI Components

See [CONTRIBUTING.md](https://github.com/sendgrid/ui-components/blob/master/CONTRIBUTING.md)

Install project dependencies with:
```
yarn
```

## Semver Versioning

When making a pull request, make sure the title has a [semver](https://semver.org/) bump level defined (**#major**, **#minor**, or **#patch**).

Semver bumps are used to know when to update the [@sendgrid/ui-components npm package](https://www.npmjs.com/package/@sendgrid/ui-components).
Patches and minor changes will be updated automatically, but major changes will update if you update your npm package version manually.

More information: https://semver.org/

## Available Commands

- `yarn start`: This is an alias for `yarn run storybook`
- `yarn storybook`: Start Storybook on port 6006.
- `yarn build`: Builds the assets for deployment.
- `yarn lint`: Runs the linter.
- `yarn lint-fix`: Runs the linter and auto-fixes the errors it can auto-fix.
- `yarn test`: Run the unit tests.
- `yarn snapshot`: Update snapshot tests. Make sure you run the tests first and you're not overwriting snapshots by accident.
- `yarn lint-snapshot`: A combination of `yarn run lint` and `yarn run snapshot`.
- `yarn ci-test`: Test used for the CI build (doesn't use interactive mode).
- `yarn build-storybook`: Build a deployable version of the Storybook.
- `yarn prepare`: Used by npm to build the assets before publishing.
- `yarn run image-snapshots`: Builds a static index.html file and runs image snapshot tests.
- `yarn update-icon-types`: Pull latest styleguide css and update the types of icon to match all found instances of sg-icon-${type}

## Testing

To make sure your additions don't break `ui-components`, run `npm run test`, which will test all of your changed `*.test.*` files and show a coverage report. To check image snapshots run `npm run image-snapshots` updating and other commands can be passed through to jest like `npm run image-snapshots -u`.

**Image Snapshots & Docker**:

- Since we run image snapshots in Buildkite with docker we need to run them locally with docker as well because different OSs render fonts and other things differently. We don't publish our docker image so you'll have to build and re-build the image any time our dependencies change in package.json. To do so just run the command `docker-compose build build`. This should build the container and be ready to run.

**Image Snapshots & Animations**:

- We add a css rule in storybook when we detect the `file://` pattern that disables all animations on the page so we can get consistent image snapshots with animations.

## Deploying

Visit the [Buildkite Master Branch](https://buildkite.com/sendgrid/ui-components/builds?branch=master) and select the SemVer appropriate to your deployment and you should be off and away. Make sure to post in FE Guild that a new version is going out.

<a name="license"></a>
# License
[The MIT License (MIT)](LICENSE)
