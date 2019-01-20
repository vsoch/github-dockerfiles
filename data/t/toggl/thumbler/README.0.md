# eslint-config-toggl

Reusable ESLit configuration.

## Usage

In `package.json`, specify:

```
"eslintConfig": {
  "extends": "toggl"
},
"dependencies": {
  "eslint-config-toggl": "1.0.0-next"
}
```
# @toggl/prettier

Prettier is an opinionated code formatter. It enforces a consistent style by
parsing your code and re-printing it with its own rules that take the maximum
line length into account, wrapping code when necessary.

## Enable Prettier

To enable Prettier for a module, add the `@prettier` pragma to it:

```
/** @prettier */
const code = 'here'
```

## Editor integration

To make the most out of prettier, find a suitable [editor integration].

Make sure to configure it so that ESLint applies fixes after Prettier finishes
with formatting code.

[editor integration]: https://prettier.io/docs/en/editors.html
