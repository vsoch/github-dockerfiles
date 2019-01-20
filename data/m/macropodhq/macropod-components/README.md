# Macropod Components

[![Join the chat at https://gitter.im/macropodhq/macropod-components](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/macropodhq/macropod-components?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is a library of components that we use at Macropod.

It includes a debug server so that changes made to the components are reflected instantly in your browser. This shortens the development cycle for new components and makes debugging existing components easier.

## Requirements

### [Node.js](http://nodejs.org/download/)

On OS X, we recommend installing via [Homebrew](https://brew.sh) using `brew install nodejs`.

To check you have it installed, you can run `node -v` and `npm -v`. Both should output a version number.

## Usage

To use the Macropod packages in a Node.js-based project, you can do the following;

```sh
npm install --save-dev "git://github.com/macropodhq/macropod-components.git#1.12.0"
```

_**Note**: You can substitute `#1.12.0` in this command for the commit sha1 or tag of any version of the project you want to use._

You can then import the modules into your project by name using `require`;

```javascript
var Avatar = require('macropod-components/packages/avatar');
var Button = require('macropod-components/packages/button');
```

## Running the Playground

To install the playground's dependencies, run `npm install` from the root directory of this repository.

If that completes without showing any errors, `npm start` will run the development server, and you can then access the playground in your browser at <http://localhost:3000>.

Port 3000 is shared with some other projects and services, so if you get an error about the port being taken, you can prepend `PORT=` and a different port number to the `npm start` command to change it. For example, `PORT=8080 npm start` will launch it on port 8080, meaning the playground would be accessible in your browser at <http://localhost:8080>.

## Contributing

### Code Style

ESLint rules are configured, and the project can be linted by running `npm run lint` from the project directory. Please try to follow the advice given by ESLint's output as best you can. Ideally, with each new pull request, the number of problems reported by ESLint should either decrease, or remain the same.

An `.editorconfig` file is included with the project to increase consistency of file formatting. Please [install the appropriate plugin](http://editorconfig.org/#download) for your preferred editor.

### New Packages

Creating a new package is easy, simply create a directory within `packages` with the name you want to use for your component, within it, you should create at least two files;

* `index.jsx`, the main, re-usable package code.
* `example.jsx`, an example to display from the development server, and to serve as an implementation suggestion.

`index.jsx` within the main `packages` directory will automatically find any new `example.jsx` files within the package and import them into the demo page.

If your package includes stylesheets, it is recommended that they are implemented as `[package-name].scss` within the package's directory.

The package name should be explicitly set as the `displayName` property on React components, and, where possible, the package's React class assigned directly to `module.exports`;

```javascript
module.exports = React.createClass({
  displayName: 'MyPackage'
});
```

## Release Process

The following is done directly on `master`.

Pick a new version number based on [Semver](http://semver.org) rules.

### 1. Update `CHANGELOG.md`

From GitHub's [releases](https://github.com/macropodhq/macropod-components/releases) page, navigate to the latest release, then click the "n commits to master since this tag" link to get the comparison view.

Once there, find all the Pull Requests which have been merged since the latest release, and list them in the changelog, following the existing format. For Pull Requiests which are part of a single feature or are fixes for issues with new features, show them all in one entry, but link to each.

Each release's title should link to its corresponding GitHub tag page. Each Pull Request number should link to the PR.

Optionally, categorise the changes under headings such as `Changes`, `Features`, `Fixes` or `Improvements`.

### 2. Update `package.json`

Change the version in `package.json`. As our version format isn't `vX.Y.Z`, you must do this manually rather than with `npm`'s `version` tool.

### 3. Add and Commit

You should only have changes to `CHANGELOG.md` and `package.json` in a version bump commit. Check the `git status` and `git diff` to make sure.

The commit message should mention the version, and should note that it's a version bump commit. A good format to follow is `Bump version to vX.Y.X`.

### 4. Tag

Fairly simple, no fancy tags, just `git tag X.Y.Z`

### 5. Push to `master`

Once you're sure things are correct, push the change to `master` with `git push` and push the tag with `git push --tags` (these must be done separately).

### 6. Update the GitHub release page

Copy the changelog entry for this release into a [new release](https://github.com/macropodhq/macropod-components/releases/new) for the newly pushed tag.

Demote the markdown headings to normal text and append a `:` to each.
