# has-ansi [![Build Status](https://travis-ci.org/sindresorhus/has-ansi.svg?branch=master)](https://travis-ci.org/sindresorhus/has-ansi)

> Check if a string has [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code)


## Install

```
$ npm install --save has-ansi
```


## Usage

```js
var hasAnsi = require('has-ansi');

hasAnsi('\u001b[4mcake\u001b[0m');
//=> true

hasAnsi('cake');
//=> false
```


## Related

- [has-ansi-cli](https://github.com/sindresorhus/has-ansi-cli) - CLI for this module
- [strip-ansi](https://github.com/sindresorhus/strip-ansi) - Strip ANSI escape codes
- [ansi-regex](https://github.com/sindresorhus/ansi-regex) - Regular expression for matching ANSI escape codes
- [chalk](https://github.com/sindresorhus/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# log-update [![Build Status](https://travis-ci.org/sindresorhus/log-update.svg?branch=master)](https://travis-ci.org/sindresorhus/log-update)

> Log by overwriting the previous output in the terminal.  
> Useful for rendering progress bars, animations, etc.

![](screenshot.gif)


## Install

```
$ npm install --save log-update
```


## Usage

```js
var logUpdate = require('log-update');

var i = 0;
var frames = ['-', '\\', '|', '/'];

setInterval(function () {
	var frame = frames[i++ % frames.length];
	logUpdate('\n' + '        ♥♥\n   ' + frame + ' unicorns ' + frame + '\n        ♥♥');
}, 100);
```


## API

### logUpdate(text, ...)

Log to stdout.

### logUpdate.clear()

Clear the logged output.

### logUpdate.done()

Persist the logged output.  
Useful if you want to start a new log session below the current one.

### logUpdate.stderr(text, ...)

Log to stderr.

### logUpdate.stderr.clear()
### logUpdate.stderr.done()

### logUpdate.create(stream)

Get a `logUpdate` method that logs to the specified stream.


## Examples

- [speed-test](https://github.com/sindresorhus/speed-test) - Uses this module to render a spinner


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# listr-verbose-renderer [![Build Status](https://travis-ci.org/SamVerschueren/listr-verbose-renderer.svg?branch=master)](https://travis-ci.org/SamVerschueren/listr-verbose-renderer)

> [Listr](https://github.com/SamVerschueren/listr) verbose renderer

<img src="screenshot.gif" />


## Install

```
$ npm install --save listr-verbose-renderer
```


## Usage

```js
const VerboseRenderer = require('listr-verbose-renderer');
const Listr = require('listr');

const list = new Listr([
	{
		title: 'foo',
		task: () => Promise.resolve('bar')
	}
], {
	renderer: VerboseRenderer
});

list.run();
```

> Note: This renderer supports non-TTY environments.


## Options

These options should be provided in the [Listr](https://github.com/SamVerschueren/listr) options object.

### dateFormat

Type: `string` `false`<br>
Default: `HH:mm:ss`

Format of the rendered timestamp. Use the [date-fns string format](https://date-fns.org/docs/format). If `false` is passed in, the timestamp will be hidden.


## Related

- [listr](https://github.com/SamVerschueren/listr) - Terminal task list
- [listr-update-renderer](https://github.com/SamVerschueren/listr-update-renderer) - Listr update renderer
- [listr-silent-renderer](https://github.com/SamVerschueren/listr-silent-renderer) - Suppress Listr rendering output


## License

MIT © [Sam Verschueren](https://github.com/SamVerschueren)
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install --save supports-color
```


## Usage

```js
var supportsColor = require('supports-color');

if (supportsColor) {
	console.log('Terminal supports color');
}
```

It obeys the `--color` and `--no-color` CLI flags.

For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
<h1 align="center">
	<br>
	<br>
	<img width="360" src="https://cdn.rawgit.com/chalk/chalk/19935d6484811c5e468817f846b7b3d417d7bf4a/logo.svg" alt="chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Build Status](https://travis-ci.org/chalk/chalk.svg?branch=master)](https://travis-ci.org/chalk/chalk)
[![Coverage Status](https://coveralls.io/repos/chalk/chalk/badge.svg?branch=master)](https://coveralls.io/r/chalk/chalk?branch=master)
[![](http://img.shields.io/badge/unicorn-approved-ff69b4.svg)](https://www.youtube.com/watch?v=9auOCbH5Ns4)


[colors.js](https://github.com/Marak/colors.js) used to be the most popular string styling module, but it has serious deficiencies like extending `String.prototype` which causes all kinds of [problems](https://github.com/yeoman/yo/issues/68). Although there are other ones, they either do too much or not enough.

**Chalk is a clean and focused alternative.**

![](https://github.com/chalk/ansi-styles/raw/master/screenshot.png)


## Why

- Highly performant
- Doesn't extend `String.prototype`
- Expressive API
- Ability to nest styles
- Clean and focused
- Auto-detects color support
- Actively maintained
- [Used by ~4500 modules](https://www.npmjs.com/browse/depended/chalk) as of July 15, 2015


## Install

```
$ npm install --save chalk
```


## Usage

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
var chalk = require('chalk');

// style a string
chalk.blue('Hello world!');

// combine styled and normal strings
chalk.blue('Hello') + 'World' + chalk.red('!');

// compose multiple styles using the chainable API
chalk.blue.bgRed.bold('Hello world!');

// pass in multiple arguments
chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz');

// nest styles
chalk.red('Hello', chalk.underline.bgBlue('world') + '!');

// nest styles of the same type even (color, underline, background)
chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
);
```

Easily define your own themes.

```js
var chalk = require('chalk');
var error = chalk.bold.red;
console.log(error('Error!'));
```

Take advantage of console.log [string substitution](http://nodejs.org/docs/latest/api/console.html#console_console_log_data).

```js
var name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> Hello Sindre
```


## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `Chalk.red.yellow.green` is equivalent to `Chalk.green`.

Multiple arguments will be separated by space.

### chalk.enabled

Color support is automatically detected, but you can override it by setting the `enabled` property. You should however only do this in your own code as it applies globally to all chalk consumers.

If you need to change this in a reusable module create a new instance:

```js
var ctx = new chalk.constructor({enabled: false});
```

### chalk.supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.

### chalk.styles

Exposes the styles as [ANSI escape codes](https://github.com/chalk/ansi-styles).

Generally not useful, but you might need just the `.open` or `.close` escape code if you're mixing externally styled strings with your own.

```js
var chalk = require('chalk');

console.log(chalk.styles.red);
//=> {open: '\u001b[31m', close: '\u001b[39m'}

console.log(chalk.styles.red.open + 'Hello' + chalk.styles.red.close);
```

### chalk.hasColor(string)

Check whether a string [has color](https://github.com/chalk/has-ansi).

### chalk.stripColor(string)

[Strip color](https://github.com/chalk/strip-ansi) from a string.

Can be useful in combination with `.supportsColor` to strip color on externally styled text when it's not supported.

Example:

```js
var chalk = require('chalk');
var styledString = getText();

if (!chalk.supportsColor) {
	styledString = chalk.stripColor(styledString);
}
```


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue` *(on Windows the bright version is used as normal blue is illegible)*
- `magenta`
- `cyan`
- `white`
- `gray`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`


## 256-colors

Chalk does not support anything other than the base eight colors, which guarantees it will work on all terminals and systems. Some terminals, specifically `xterm` compliant ones, will support the full range of 8-bit colors. For this the lower level [ansi-256-colors](https://github.com/jbnicolai/ansi-256-colors) package can be used.


## Windows

If you're on Windows, do yourself a favor and use [`cmder`](http://bliker.github.io/cmder/) instead of `cmd.exe`.


## Related

- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles/) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color/) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# ansi-escapes [![Build Status](https://travis-ci.org/sindresorhus/ansi-escapes.svg?branch=master)](https://travis-ci.org/sindresorhus/ansi-escapes)

> [ANSI escape codes](http://www.termsys.demon.co.uk/vtansi.htm) for manipulating the terminal


## Install

```
$ npm install --save ansi-escapes
```


## Usage

```js
const ansiEscapes = require('ansi-escapes');

// moves the cursor two rows up and to the left
process.stdout.write(ansiEscapes.cursorUp(2) + ansiEscapes.cursorLeft);
//=> '\u001b[2A\u001b[1000D'
```


## API

### cursorTo([x, [y]])

Set the absolute position of the cursor. `x0` `y0` is the top left of the screen.

Specify either both `x` & `y`, only `x`, or nothing.

### cursorMove(x, [y])

Set the position of the cursor relative to its current position.

### cursorUp(count)

Move cursor up a specific amount of rows. Default is `1`.

### cursorDown(count)

Move cursor down a specific amount of rows. Default is `1`.

### cursorForward(count)

Move cursor forward a specific amount of rows. Default is `1`.

### cursorBackward(count)

Move cursor backward a specific amount of rows. Default is `1`.

### cursorLeft

Move cursor to the left side.

### cursorSavePosition

Save cursor position.

### cursorRestorePosition

Restore saved cursor position.

### cursorGetPosition

Get cursor position.

### cursorNextLine

Move cursor to the next line.

### cursorPrevLine

Move cursor to the previous line.

### cursorHide

Hide cursor.

### cursorShow

Show cursor.

### eraseLines(count)

Erase from the current cursor position up the specified amount of rows.

### eraseEndLine

Erase from the current cursor position to the end of the current line.

### eraseStartLine

Erase from the current cursor position to the start of the current line.

### eraseLine

Erase the entire current line.

### eraseDown

Erase the screen from the current line down to the bottom of the screen.

### eraseUp

Erase the screen from the current line up to the top of the screen.

### eraseScreen

Erase the screen and move the cursor the top left position.

### scrollUp

Scroll display up one line.

### scrollDown

Scroll display down one line.

### clearScreen

Clear the terminal screen.

### beep

Output a beeping sound.

### image(input, [options])

Display an image.

*Currently only supported on iTerm >=2.9.*

See [term-img](https://github.com/sindresorhus/term-img) for a higher-level module.

#### input

Type: `buffer`

Buffer of an image. Usually read in with `fs.readFile()`.

#### options

##### width
##### height

Type: `string` `number`

The width and height are given as a number followed by a unit, or the word "auto".

- `N`: N character cells.
- `Npx`: N pixels.
- `N%`: N percent of the session's width or height.
- `auto`: The image's inherent size will be used to determine an appropriate dimension.

##### preserveAspectRatio

Type: `boolean`<br>
Default: `true`

### iTerm.setCwd([path])

Type: `string`<br>
Default: `process.cwd()`

[Inform iTerm](https://www.iterm2.com/documentation-escape-codes.html) of the current directory to help semantic history and enable [Cmd-clicking relative paths](https://coderwall.com/p/b7e82q/quickly-open-files-in-iterm-with-cmd-click).


## Related

- [ansi-styles](https://github.com/chalk/ansi-styles) - ANSI escape codes for styling strings in the terminal


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# string-width [![Build Status](https://travis-ci.org/sindresorhus/string-width.svg?branch=master)](https://travis-ci.org/sindresorhus/string-width)

> Get the visual width of a string - the number of columns required to display it

Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width. [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code) are stripped and doesn't affect the width.

Useful to be able to measure the actual width of command-line output.


## Install

```
$ npm install --save string-width
```


## Usage

```js
const stringWidth = require('string-width');

stringWidth('古');
//=> 2

stringWidth('\u001b[1m古\u001b[22m');
//=> 2

stringWidth('a');
//=> 1
```


## Related

- [string-width-cli](https://github.com/sindresorhus/string-width-cli) - CLI for this module
- [string-length](https://github.com/sindresorhus/string-length) - Get the real length of a string
- [widest-line](https://github.com/sindresorhus/widest-line) - Get the visual width of the widest line in a string


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# onetime [![Build Status](https://travis-ci.org/sindresorhus/onetime.svg?branch=master)](https://travis-ci.org/sindresorhus/onetime)

> Only call a function once

When called multiple times it will return the return value from the first call.

*Unlike the module [once](https://github.com/isaacs/once), this one isn't naughty extending `Function.prototype`.*


## Install

```
$ npm install --save onetime
```


## Usage

```js
let i = 0;

const foo = onetime(() => i++);

foo(); //=> 0
foo(); //=> 0
foo(); //=> 0
```


## API

### onetime(function, [shouldThrow])

#### function

Type: `function`

Function that should only be called once.

#### shouldThrow

Type: `boolean`  
Default: `false`

![](screenshot-shouldthrow.png)

Set to `true` if you want it to fail with a nice and descriptive error when called more than once.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# npm-run-path [![Build Status](https://travis-ci.org/sindresorhus/npm-run-path.svg?branch=master)](https://travis-ci.org/sindresorhus/npm-run-path)

> Get your [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) prepended with locally installed binaries

In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name. This enables the same outside npm.


## Install

```
$ npm install --save npm-run-path
```


## Usage

```js
const childProcess = require('child_process');
const npmRunPath = require('npm-run-path');

console.log(process.env.PATH);
//=> '/usr/local/bin'

console.log(npmRunPath());
//=> '/Users/sindresorhus/dev/foo/node_modules/.bin:/Users/sindresorhus/dev/node_modules/.bin:/Users/sindresorhus/node_modules/.bin:/Users/node_modules/.bin:/node_modules/.bin:/usr/local/bin'

// `foo` is a locally installed binary
childProcess.execFileSync('foo', {
	env: npmRunPath.env()
});
```


## API

### npmRunPath([options])

#### options

##### cwd

Type: `string`<br>
Default: `process.cwd()`

Working directory.

##### path

Type: `string`<br>
Default: [`PATH`](https://github.com/sindresorhus/path-key)

PATH to be appended.<br>
Set it to an empty string to exclude the default PATH.

### npmRunPath.env([options])

#### options

##### cwd

Type: `string`<br>
Default: `process.cwd()`

Working directory.

##### env

Type: `Object`

Accepts an object of environment variables, like `process.env`, and modifies the PATH using the correct [PATH key](https://github.com/sindresorhus/path-key). Use this if you're modifying the PATH for use in the `child_process` options.


## Related

- [npm-run-path-cli](https://github.com/sindresorhus/npm-run-path-cli) - CLI for this module
- [execa](https://github.com/sindresorhus/execa) - Execute a locally installed binary


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# slice-ansi 

[![Build Status](https://travis-ci.org/vorpaljs/slice-ansi.svg?branch=master)](https://travis-ci.org/vorpaljs/slice-ansi)
[![XO: Linted](https://img.shields.io/badge/xo-linted-blue.svg)](https://github.com/sindresorhus/xo)

> Slice a string with [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles)

## Install

```
$ npm install --save slice-ansi
```

## Usage

```js
var chalk = require('chalk');
var sliceAnsi = require('slice-ansi');

var input = 'The quick brown ' + chalk.red('fox jumped over ') +
	'the lazy ' + chalk.green('dog and then ran away with the unicorn.');

console.log(sliceAnsi(input, 20, 30));
```

## API

### sliceAnsi(input, beginSlice[, endSlice])

#### input

Type: `string`

String with ANSI escape codes. Like one styled by [`chalk`](https://github.com/chalk/chalk).

#### beginSlice

Type: `number`

The zero-based index at which to begin the slice.

#### endSlice

Type: `number`

Optional. The zero-based index at which to end the slice.


## Related

- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [David Caccavella](https://githbu.com/dthree)
# listr-update-renderer [![Build Status](https://travis-ci.org/SamVerschueren/listr-update-renderer.svg?branch=master)](https://travis-ci.org/SamVerschueren/listr-update-renderer)

> [Listr](https://github.com/SamVerschueren/listr) update renderer

<img src="screenshot.gif" />


## Install

```
$ npm install --save listr-update-renderer
```


## Usage

```js
const UpdaterRenderer = require('listr-update-renderer');
const Listr = require('listr');

const list = new Listr([
    {
        title: 'foo',
        task: () => Promise.resolve('bar')
    }
], {
    renderer: UpdaterRenderer,
	collapse: false
});

list.run();
```

> Note: This is the default renderer for [Listr](https://github.com/SamVerschueren/listr) and doesn't need to be specified.


## Options

These options should be provided in the [Listr](https://github.com/SamVerschueren/listr) options object.

### showSubtasks

Type: `boolean`<br>
Default: `true`

Set to `false` if you want to disable the rendering of the subtasks. Subtasks will be rendered if an error occurred in one of them.

### collapse

Type: `boolean`<br>
Default: `true`

Set to `false` if you don't want subtasks to be hidden after the main task succeed.


## Related

- [listr](https://github.com/SamVerschueren/listr) - Terminal task list
- [listr-verbose-renderer](https://github.com/SamVerschueren/listr-verbose-renderer) - Listr verbose renderer
- [listr-silent-renderer](https://github.com/SamVerschueren/listr-silent-renderer) - Suppress Listr rendering output


## License

MIT © [Sam Verschueren](https://github.com/SamVerschueren)
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install --save supports-color
```


## Usage

```js
var supportsColor = require('supports-color');

if (supportsColor) {
	console.log('Terminal supports color');
}
```

It obeys the `--color` and `--no-color` CLI flags.

For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
<h1 align="center">
	<br>
	<br>
	<img width="360" src="https://cdn.rawgit.com/chalk/chalk/19935d6484811c5e468817f846b7b3d417d7bf4a/logo.svg" alt="chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Build Status](https://travis-ci.org/chalk/chalk.svg?branch=master)](https://travis-ci.org/chalk/chalk)
[![Coverage Status](https://coveralls.io/repos/chalk/chalk/badge.svg?branch=master)](https://coveralls.io/r/chalk/chalk?branch=master)
[![](http://img.shields.io/badge/unicorn-approved-ff69b4.svg)](https://www.youtube.com/watch?v=9auOCbH5Ns4)


[colors.js](https://github.com/Marak/colors.js) used to be the most popular string styling module, but it has serious deficiencies like extending `String.prototype` which causes all kinds of [problems](https://github.com/yeoman/yo/issues/68). Although there are other ones, they either do too much or not enough.

**Chalk is a clean and focused alternative.**

![](https://github.com/chalk/ansi-styles/raw/master/screenshot.png)


## Why

- Highly performant
- Doesn't extend `String.prototype`
- Expressive API
- Ability to nest styles
- Clean and focused
- Auto-detects color support
- Actively maintained
- [Used by ~4500 modules](https://www.npmjs.com/browse/depended/chalk) as of July 15, 2015


## Install

```
$ npm install --save chalk
```


## Usage

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
var chalk = require('chalk');

// style a string
chalk.blue('Hello world!');

// combine styled and normal strings
chalk.blue('Hello') + 'World' + chalk.red('!');

// compose multiple styles using the chainable API
chalk.blue.bgRed.bold('Hello world!');

// pass in multiple arguments
chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz');

// nest styles
chalk.red('Hello', chalk.underline.bgBlue('world') + '!');

// nest styles of the same type even (color, underline, background)
chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
);
```

Easily define your own themes.

```js
var chalk = require('chalk');
var error = chalk.bold.red;
console.log(error('Error!'));
```

Take advantage of console.log [string substitution](http://nodejs.org/docs/latest/api/console.html#console_console_log_data).

```js
var name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> Hello Sindre
```


## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `Chalk.red.yellow.green` is equivalent to `Chalk.green`.

Multiple arguments will be separated by space.

### chalk.enabled

Color support is automatically detected, but you can override it by setting the `enabled` property. You should however only do this in your own code as it applies globally to all chalk consumers.

If you need to change this in a reusable module create a new instance:

```js
var ctx = new chalk.constructor({enabled: false});
```

### chalk.supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.

### chalk.styles

Exposes the styles as [ANSI escape codes](https://github.com/chalk/ansi-styles).

Generally not useful, but you might need just the `.open` or `.close` escape code if you're mixing externally styled strings with your own.

```js
var chalk = require('chalk');

console.log(chalk.styles.red);
//=> {open: '\u001b[31m', close: '\u001b[39m'}

console.log(chalk.styles.red.open + 'Hello' + chalk.styles.red.close);
```

### chalk.hasColor(string)

Check whether a string [has color](https://github.com/chalk/has-ansi).

### chalk.stripColor(string)

[Strip color](https://github.com/chalk/strip-ansi) from a string.

Can be useful in combination with `.supportsColor` to strip color on externally styled text when it's not supported.

Example:

```js
var chalk = require('chalk');
var styledString = getText();

if (!chalk.supportsColor) {
	styledString = chalk.stripColor(styledString);
}
```


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue` *(on Windows the bright version is used as normal blue is illegible)*
- `magenta`
- `cyan`
- `white`
- `gray`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`


## 256-colors

Chalk does not support anything other than the base eight colors, which guarantees it will work on all terminals and systems. Some terminals, specifically `xterm` compliant ones, will support the full range of 8-bit colors. For this the lower level [ansi-256-colors](https://github.com/jbnicolai/ansi-256-colors) package can be used.


## Windows

If you're on Windows, do yourself a favor and use [`cmder`](http://bliker.github.io/cmder/) instead of `cmd.exe`.


## Related

- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles/) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color/) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# log-symbols [![Build Status](https://travis-ci.org/sindresorhus/log-symbols.svg?branch=master)](https://travis-ci.org/sindresorhus/log-symbols)

> Colored symbols for various log levels

Includes fallbacks for Windows CMD which only supports a [limited character set](http://en.wikipedia.org/wiki/Code_page_437).

![](screenshot.png)


## Install

```sh
$ npm install --save log-symbols
```


## Usage

```js
var logSymbols = require('log-symbols');

console.log(logSymbols.success, 'finished successfully!');
// On real OSes:  ✔ finished successfully!
// On Windows:    √ finished successfully!
```

## API

### logSymbols

#### info
#### success
#### warning
#### error


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# indent-string [![Build Status](https://travis-ci.org/sindresorhus/indent-string.svg?branch=master)](https://travis-ci.org/sindresorhus/indent-string)

> Indent each line in a string


## Install

```
$ npm install indent-string
```


## Usage

```js
const indentString = require('indent-string');

indentString('Unicorns\nRainbows', 4);
//=> '    Unicorns'
//=> '    Rainbows'

indentString('Unicorns\nRainbows', 4, {indent: '♥'});
//=> '♥♥♥♥Unicorns'
//=> '♥♥♥♥Rainbows'
```


## API

### indentString(input, [count], [options])

#### input

Type: `string`

String you want to indent.

#### count

Type: `number`<br>
Default: `1`

How many times you want `indent` repeated.

#### options

Type: `Object`<br>

##### indent

Type: `string`<br>
Default: `' '`

String to use for the indent.

##### includeEmptyLines

Type: `boolean`<br>
Default: `false`

Also indent empty lines.


## Related

- [indent-string-cli](https://github.com/sindresorhus/indent-string-cli) - CLI for this module
- [strip-indent](https://github.com/sindresorhus/strip-indent) - Strip leading whitespace from every line in a string


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# listr-silent-renderer [![Build Status](https://travis-ci.org/SamVerschueren/listr-silent-renderer.svg?branch=master)](https://travis-ci.org/SamVerschueren/listr-silent-renderer)

> Suppress [Listr](https://github.com/SamVerschueren/listr) rendering output


## Install

```
$ npm install --save listr-silent-renderer
```


## Usage

```js
const SilentRenderer = require('listr-silent-renderer');
const Listr = require('listr');

const list = new Listr([
    {
        title: 'foo',
        task: () => Promise.resolve('bar')
    }
], {
    renderer: SilentRenderer
});

list.run();
```


## Related

- [listr](https://github.com/SamVerschueren/listr) - Terminal task list
- [listr-update-renderer](https://github.com/SamVerschueren/listr-update-renderer) - Listr update renderer
- [listr-verbose-renderer](https://github.com/SamVerschueren/listr-verbose-renderer) - Listr verbose renderer


## License

MIT © [Sam Verschueren](https://github.com/SamVerschueren)
# extract-zip

Unzip written in pure JavaScript. Extracts a zip into a directory. Available as a library or a command line program.

Uses the [`yauzl`](http://npmjs.org/yauzl) ZIP parser.

[![NPM](https://nodei.co/npm/extract-zip.png?global=true)](https://nodei.co/npm/extract-zip/)
[![js-standard-style](https://cdn.rawgit.com/feross/standard/master/badge.svg)](https://github.com/feross/standard)
[![Build Status](https://travis-ci.org/maxogden/extract-zip.svg?branch=master)](https://travis-ci.org/maxogden/extract-zip)

## Installation

Get the library:

```
npm install extract-zip --save
```

Install the command line program:

```
npm install extract-zip -g
```

## JS API

```js
var extract = require('extract-zip')
extract(source, {dir: target}, function (err) {
 // extraction is complete. make sure to handle the err
})
```

### Options

- `dir` - defaults to `process.cwd()`
- `defaultDirMode` - integer - Directory Mode (permissions) will default to `493` (octal `0755` in integer)
- `defaultFileMode` - integer - File Mode (permissions) will default to `420` (octal `0644` in integer)
- `onEntry` - function - if present, will be called with `(entry, zipfile)`, entry is every entry from the zip file forwarded from the `entry` event from yauzl. `zipfile` is the `yauzl` instance

Default modes are only used if no permissions are set in the zip file.

## CLI Usage

```
extract-zip foo.zip <targetDirectory>
```

If not specified, `targetDirectory` will default to `process.cwd()`.
# escape-string-regexp [![Build Status](https://travis-ci.org/sindresorhus/escape-string-regexp.svg?branch=master)](https://travis-ci.org/sindresorhus/escape-string-regexp)

> Escape RegExp special characters


## Install

```
$ npm install --save escape-string-regexp
```


## Usage

```js
const escapeStringRegexp = require('escape-string-regexp');

const escapedString = escapeStringRegexp('how much $ for a unicorn?');
//=> 'how much \$ for a unicorn\?'

new RegExp(escapedString);
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
![](http://imgh.us/common-tags_5.png)

> :bookmark: A set of **well-tested**, commonly used template literal tag functions for use in ES2015+.
>
> :star2: Plus some extra goodies for easily making your own tags.



# :battery: Project Status

| Info       | Badges                                   |
| ---------- | ---------------------------------------- |
| Version    | [![github release](https://img.shields.io/github/release/declandewet/common-tags.svg?style=flat-square)](https://github.com/declandewet/common-tags/releases/latest) [![npm version](https://img.shields.io/npm/v/common-tags.svg?style=flat-square)](http://npmjs.org/package/common-tags) |
| License    | [![npm license](https://img.shields.io/npm/l/common-tags.svg?style=flat-square)](https://github.com/declandewet/common-tags/blob/master/license.md) |
| Popularity | [![npm downloads](https://img.shields.io/npm/dm/common-tags.svg?style=flat-square)](http://npm-stat.com/charts.html?package=common-tags) |
| Testing    | [![Build status](https://ci.appveyor.com/api/projects/status/75eiommx0llt3sgd?svg=true)](https://ci.appveyor.com/project/declandewet/common-tags) [![build status](https://img.shields.io/travis/declandewet/common-tags.svg?style=flat-square)](https://travis-ci.org/declandewet/common-tags) [![codecov.io](https://img.shields.io/codecov/c/gh/declandewet/common-tags.svg?style=flat-square)](https://codecov.io/gh/declandewet/common-tags?branch=master) |
| Quality    | [![bitHound Overall Score](https://www.bithound.io/github/declandewet/common-tags/badges/score.svg)](https://www.bithound.io/github/declandewet/common-tags) [![dependency status](https://img.shields.io/david/declandewet/common-tags.svg?style=flat-square)](https://david-dm.org/declandewet/common-tags) [![dev dependency status](https://img.shields.io/david/dev/declandewet/common-tags.svg?style=flat-square)](https://david-dm.org/declandewet/common-tags#info=devDependencies) |
| Style      | [![js-standard-style](https://cdn.rawgit.com/feross/standard/master/badge.svg)](https://github.com/feross/standard) |



<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# :books: Table of Contents

- [:wave: Introduction](#wave-introduction)
- [:revolving_hearts: Why should you care?](#revolving_hearts-why-should-you-care)
- [:arrow_double_down: Installation](#arrow_double_down-installation)
    - [Requirements](#requirements)
    - [Instructions](#instructions)
- [:books: Usage](#books-usage)
    - [Imports](#imports)
    - [Available Tags](#available-tags)
      - [`html`](#html)
        - [Aliases: `source`, `codeBlock`](#aliases-source-codeblock)
      - [`safeHtml`](#safehtml)
      - [`oneLine`](#oneline)
      - [`oneLineTrim`](#onelinetrim)
      - [`stripIndent`](#stripindent)
      - [`stripIndents`](#stripindents)
      - [`inlineLists`](#inlinelists)
      - [`oneLineInlineLists`](#onelineinlinelists)
      - [`commaLists`](#commalists)
      - [`commaListsOr`](#commalistsor)
      - [`commaListsAnd`](#commalistsand)
      - [`oneLineCommaLists`](#onelinecommalists)
      - [`oneLineCommaListsOr`](#onelinecommalistsor)
      - [`oneLineCommaListsAnd`](#onelinecommalistsand)
- [:wrench: Advanced Usage](#wrench-advanced-usage)
    - [Tail Processing](#tail-processing)
    - [Make Your Own Template Tag](#make-your-own-template-tag)
      - [Class is in Session: TemplateTag](#class-is-in-session-templatetag)
      - [The Anatomy of a Transformer](#the-anatomy-of-a-transformer)
      - [Plugin Transformers](#plugin-transformers)
      - [Plugin Pipeline](#plugin-pipeline)
      - [Returning Other Values from a Transformer](#returning-other-values-from-a-transformer)
      - [List of Built-in Transformers](#list-of-built-in-transformers)
        - [`trimResultTransformer([side])`](#trimresulttransformerside)
        - [`stripIndentTransformer([type='initial'])`](#stripindenttransformertypeinitial)
        - [`replaceResultTransformer(replaceWhat, replaceWith)`](#replaceresulttransformerreplacewhat-replacewith)
        - [`replaceSubstitutionTransformer(replaceWhat, replaceWith)`](#replacesubstitutiontransformerreplacewhat-replacewith)
        - [`inlineArrayTransformer(opts)`](#inlinearraytransformeropts)
        - [`splitStringTransformer(splitBy)`](#splitstringtransformersplitby)
- [How to Contribute](#how-to-contribute)
- [License](#license)
- [:stars: Other ES2015 Template Tag Modules](#stars-other-es2015-template-tag-modules)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



# :wave: Introduction

`common-tags` initially started out as two template tags I'd always find myself writing - one for stripping indents, and one for trimming multiline strings down to a single line. In it's prime, I was an avid user of [CoffeeScript](http://coffeescript.org), which had this behaviour by default as part of it's block strings feature. I also started out programming in Ruby, which has a similar mechanism called Heredocs.

Over time, I found myself needing a few more template tags to cover edge cases - ones that supported including arrays, or ones that helped to render out tiny bits of HTML not large enough to deserve their own file or an entire template engine. So I packaged all of these up into this module.

As more features were proposed, and I found myself needing a way to override the default settings to cover even more edge cases, I realized that my initial implementation wouldn't be easy to scale.

So I re-wrote this module on top of a core architecture that makes use of transformer plugins which can be composed, imported independently and re-used.

Have a read of the next section to find out why you should care. :smile:



# :revolving_hearts: Why should you care?

Tagged templates in ES2015 are a welcome feature. But, they have their downsides. One such downside is that they preserve all whitespace by default - which makes multiline strings in source code look terrible.

Source code is not just for computers to interpret. Humans have to read it too :grin:. If you care at all about how neat your source code is, or come from a [CoffeeScript](http://coffeescript.org/) background and miss the [block string syntax](http://coffeescript.org/#strings), then you will love `common-tags`, as it was initially intended to bring this feature "back" to JS since it's [initial commit](https://github.com/declandewet/common-tags/commit/2595288d6c276439d98d1bcbbb0aa113f4f7cd86).

`common-tags` also [exposes a means of composing pipelines of dynamic transformer plugins](#plugin-transformers). As someone with a little experience writing tagged templates, I can admit that it is often the case that one tag might need to do the same thing as another tag before doing any further processing; for example - a typical tag that renders out HTML could strip initial indents first, then worry about handling character escapes. Both steps could easily be useful as their own separate template tags, but there isn't an immediately obvious way of composing the two together for maximum re-use. `common-tags` offers not [one](#tail-processing), but [two](#plugin-pipeline) ways of doing this.

Furthermore, I try to keep this project as transparently stable and updated as frequently as I possibly can. As you may have already seen by the [project status table](#battery-project-status), `common-tags` is linted, well tested, tests are well covered, tests pass on both Unix and Windows operating systems, the popularity bandwidth is easily referenced and dependency health is in plain sight :smile:. `common-tags` is also already used in production on a number of proprietary sites and dependent projects, and [contributions are always welcome](#how-to-contribute), as are [suggestions](issues).





# :arrow_double_down: Installation

### Requirements

The official recommendation for running `common-tags` is as follows:

- [Node.js](https://nodejs.org/en/download/) v5.0.0 or higher
- In order to use `common-tags`, your environment will also need to support ES2015 tagged templates ([pssst… check Babel out](http://babeljs.io)).

It might work with below versions of Node, but this is not a gaurantee.


### Instructions

`common-tags` is a [Node](https://nodejs.org/) module. So, as long as you have Node.js and NPM installed, installing `common-tags` is as simple as running this in a terminal at the root of your project:

```sh
$ npm install common-tags --save
```





# :books: Usage

### Imports

Like all modules, `common-tags` begins with an `import`. In fact, `common-tags` supports two styles of import:

**Named imports:**

```js
import {stripIndent} from 'common-tags'
```

**Direct module imports:**

*(Useful if your bundler doesn't support [tree shaking](https://medium.com/@roman01la/dead-code-elimination-and-tree-shaking-in-javascript-build-systems-fb8512c86edf#.p30lbjm94) but you still want to only include modules you need).*

```js
import stripIndent from 'common-tags/lib/stripIndent'
```



### Available Tags

`common-tags` exports a bunch of wonderful pre-cooked template tags for your eager consumption. They are as follows:



#### `html`
##### Aliases: `source`, `codeBlock`

You'll often find that you might want to include an array in a template. Typically, doing something like `${array.join(', ')}` would work - but what if you're printing a list of items in an HTML template and want to maintain the indentation? You'd have to count the spaces manually and include them in the `.join()` call - which is a bit *ugly* for my taste. This tag properly indents arrays, as well as newline characters in string substitutions, by converting them to an array split by newline and re-using the same array inclusion logic:

```js
import {html} from 'common-tags'
let fruits = ['apple', 'orange', 'watermelon']
html`
  <div class="list">
    <ul>
      ${fruits.map(fruit => `<li>${fruit}</li>`)}
      ${'<li>kiwi</li>\n<li>guava</li>'}
    </ul>
  </div>
`);
```

Outputs:

```html
<div class="list">
  <ul>
    <li>apple</li>
    <li>orange</li>
    <li>watermelon</li>
    <li>kiwi</li>
    <li>guava</li>
  </ul>
</div>
```





#### `safeHtml`

A tag very similar to `html` but it does safe HTML escaping for strings coming from substitutions. When combined with regular `html` tag, you can do basic HTML templating that is safe from XSS (Cross-Site Scripting) attacks.

```js
import {html, safeHtml} from 'common-tags'
let userMessages = ['hi', 'what are you up to?', '<script>alert("something evil")</script>']
html`
  <div class="chat-list">
    <ul>
      ${userMessages.map(message => safeHtml`<li>${message}</li>`)}
    </ul>
  </div>
`
```

Outputs:

```html
<div class="chat-list">
  <ul>
    <li>hi</li>
    <li>what are you up to?</li>
    <li>&lt;script&gt;alert(&quot;something evil&quot;)&lt;/script&gt;</li>
  </ul>
</div>
```





#### `oneLine`

Allows you to keep your single-line strings under 80 characters without resorting to crazy string concatenation.
```js
import {oneLine} from 'common-tags'

oneLine`
  foo
  bar
  baz
`)
// "foo bar baz"
```





#### `oneLineTrim`

Allows you to keep your single-line strings under 80 characters while trimming the new lines:

```js
import {oneLineTrim} from 'common-tags'

oneLineTrim`
  https://news.com/article
  ?utm_source=designernews.co
`)
// https://news.com/article?utm_source=designernews.co
```





#### `stripIndent`

If you want to strip the initial indentation from the beginning of each line in a multiline string:

```js
import {stripIndent} from 'common-tags'

stripIndent`
  This is a multi-line string.
  You'll ${verb} that it is indented.
  We don't want to output this indentation.
    But we do want to keep this line indented.
`
// This is a multi-line string.
// You'll notice that it is indented.
// We don't want to output this indentation.
//   But we do want to keep this line indented.
```





#### `stripIndents`

If you want to strip *all* of the indentation from the beginning of each line in a multiline string:

```js
import {stripIndents} from 'common-tags'

stripIndents`
  This is a multi-line string.
  You'll ${verb} that it is indented.
  We don't want to output this indentation.
    We don't want to keep this line indented either.
`
// This is a multi-line string.
// You'll notice that it is indented.
// We don't want to output this indentation.
// We don't want to keep this line indented either.
```





#### `inlineLists`

Allows you to inline an array substitution as a list:

```js
import {inlineLists} from 'common-tags'

inlineLists`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples bananas watermelons
// They're good!
```





#### `oneLineInlineLists`

Allows you to inline an array substitution as a list, rendered out on a single line:

```js
import {oneLineInlineLists} from 'common-tags'

oneLineInlineLists`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples bananas watermelons They're good!
```





#### `commaLists`

Allows you to inline an array substitution as a comma-separated list:

```js
import {commaLists} from 'common-tags'

commaLists`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples, bananas, watermelons
// They're good!
```





#### `commaListsOr`

Allows you to inline an array substitution as a comma-separated list, the last of which is preceded by the word "or":

```js
import {commaListsOr} from 'common-tags'

commaListsOr`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples, bananas or watermelons
// They're good!
```





#### `commaListsAnd`

Allows you to inline an array substitution as a comma-separated list, the last of which is preceded by the word "and":

```js
import {commaListsAnd} from 'common-tags'

commaListsAnd`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples, bananas and watermelons
// They're good!
```





#### `oneLineCommaLists`

Allows you to inline an array substitution as a comma-separated list, and is rendered out on to a single line:

```js
import {oneLineCommaLists} from 'common-tags'

oneLineCommaLists`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples, bananas or watermelons They're good!
```





#### `oneLineCommaListsOr`

Allows you to inline an array substitution as a comma-separated list, the last of which is preceded by the word "or", and is rendered out on to a single line:

```js
import {oneLineCommaListsOr} from 'common-tags'

oneLineCommaListsOr`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples, bananas or watermelons They're good!
```





#### `oneLineCommaListsAnd`

Allows you to inline an array substitution as a comma-separated list, the last of which is preceded by the word "and", and is rendered out on to a single line:

```js
import {oneLineCommaListsAnd} from 'common-tags'

oneLineCommaListsAnd`
  I like ${['apples', 'bananas', 'watermelons']}
  They're good!
`
// I like apples, bananas and watermelons They're good!
```



# :wrench: Advanced Usage

### Tail Processing

It's possible to pass the output of a tagged template to another template tag in pure ES2015+:

```js
import {oneLine} from 'common-tags'

oneLine`
  ${String.raw`
    foo
    bar\nbaz
  `}
`
// "foo bar\nbaz"
```



We can make this neater. Every tag `common-tags` exports can delay execution if it receives a function as it's first argument. This function is assumed to be a template tag, and is called via an intermediary tagging process before the result is passed back to our tag. Use it like so (this code is equivalent to the previous code block):

```js
import {oneLine} from 'common-tags'

oneLine(String.raw)`
  foo
  bar\nbaz
`
// "foo bar\nbaz"
```



### Make Your Own Template Tag

`common-tags` exposes an interface that allows you to painlessly create your own template tags.



#### Class is in Session: TemplateTag

`common-tags` exports a `TemplateTag` class. This class is the foundation of `common-tags`. The concept of the class works on the premise that transformations occur on a template either when the template is finished being processed (`onEndResult`), or when the tag encounters a substitution (`onSubstitution`). Any tag produced by this class supports [tail processing](#tail-processing).

The easiest tag to create is a tag that does nothing:

```js
import {TemplateTag} from 'common-tags'

const doNothing = new TemplateTag()

doNothing`foo bar`
// 'foo bar'
```





#### The Anatomy of a Transformer

`TemplateTag` receives either an array or argument list of `transformers`. A `transformer` is just a plain object with two optional methods - `onSubstitution` and `onEndResult` - it looks like this:

```js
{
  onSubstitution (substitution, resultSoFar) {
    // optional. Called when the tag encounters a substitution.
    // (a substitution is whatever's inside "${}" in your template literal)
    // `substitution` is the value of the current substitution
    // `resultSoFar` is the end result up to the point of this substitution
  },
  onEndResult (endResult) {
  	// optional. Called when all substitutions have been parsed
    // `endResult` is the final value.
  }
}
```





#### Plugin Transformers

You can wrap a transformer in a function that receives arguments in order to create a dynamic plugin:

```js
const substitutionReplacer = (oldValue, newValue) => ({
  onSubstitution(substitution, resultSoFar) {
    if (substitution === oldValue) {
      return newValue
    }
    return substitution
  }
})

const replaceFizzWithBuzz = new TemplateTag(substitutionReplacer('fizz', 'buzz'))

replaceFizzWithBuzz`foo bar ${"fizz"}`
// "foo bar buzz"
```

> **note** - if you call `new TemplateTag(substitutionReplacer)`, `substitutionReplacer` will automatically be initiated with no arguments.



#### Plugin Pipeline

You can pass a list of transformers, and `TemplateTag` will call them on your tag in the order they are specified:

```js
// note: passing these as an array also works
const replace = new TemplateTag(
  substitutionReplacer('fizz', 'buzz'),
  substitutionReplacer('foo', 'bar')
)

replace`${"foo"} ${"fizz"}`
// "bar buzz"
```



When multiple transformers are passed to `TemplateTag`, they will be iterated twice - first, all transformer `onSubstitution` methods will be called. Once they are done processing, all transformer `onEndResult` methods will be called.



#### Returning Other Values from a Transformer

This is super easy. Transformers are just objects, after all. They have full access to `this`:

```js
const listSubs = {
  onSubstitution(sub, res) {
    this.ctx = this.ctx || { subs: [] }
    this.ctx.subs.push({ sub, precededBy: res })
    return sub
  },
  onEndResult(res) {
    return this.ctx
  }
}

const toJSON = {
  onEndResult(res) {
    return JSON.stringify(res, null, 2)
  }
}

const log = {
  onEndResult(res) {
    console.log(res)
    return res
  }
}

const process = new TemplateTag([listSubs, toJSON, log])

process`
  foo ${'bar'}
  fizz ${'buzz'}
`
// {
//  "subs": [
//    {
//      "sub": "bar",
//      "precededBy": "\n  foo "
//    },
//    {
//      "sub": "buzz",
//      "precededBy": "\n  foo bar\n  fizz "
//    }
//  ]
// }
```



#### List of Built-in Transformers

Since `common-tags` is built on the foundation of this TemplateTag class, it comes with its own set of built-in transformers:



##### `trimResultTransformer([side])`

Trims the whitespace surrounding the end result. Accepts an optional `side` (can be `"left"` or `"right"`) that when supplied, will only trim whitespace from that side of the string.



##### `stripIndentTransformer([type='initial'])`

Strips the indents from the end result. Offers two types: `all`, which removes all indentation from each line, and `initial`, which removes the shortest indent level from each line. Defaults to `initial`.



##### `replaceResultTransformer(replaceWhat, replaceWith)`

Replaces a value or pattern in the end result with a new value. `replaceWhat` can be a string or a regular expression, `replaceWith` is the new value.



##### `replaceSubstitutionTransformer(replaceWhat, replaceWith)`

Replaces the result of all substitutions (results of calling `${ ... }`) with a new value. Same as for `replaceResultTransformer`, `replaceWhat` can be a string or regular expression and `replaceWith` is the new value.



##### `inlineArrayTransformer(opts)`

Converts any array substitutions into a string that represents a list. Accepts an options object:

```js
opts = {
  separator: ',', // what to separate each item with (always followed by a space)
  conjunction: 'and', // replace the last separator with this value
  serial: true // should the separator be included before the conjunction? As in the case of serial/oxford commas
}
```



##### `splitStringTransformer(splitBy)`

Splits a string substitution into an array by the provided `splitBy` substring, **only** if the string contains the `splitBy` substring.



# How to Contribute

Please see the [Contribution Guidelines](contributing.md).



# License

MIT. See [license.md](license.md).





# :stars: Other ES2015 Template Tag Modules

If `common-tags` doesn't quite fit your bill, and you just can't seem to find what you're looking for - perhaps these might be of use to you?



- [tage](https://www.npmjs.com/package/tage) - make functions work as template tags too
- [is-tagged](https://www.npmjs.com/package/is-tagged) - Check whether a function call is initiated by a tagged template string or invoked in a regular way
- [es6-template-strings](https://www.npmjs.com/package/es6-template-strings) - Compile and resolve template strings notation as specified in ES6
- [t7](https://github.com/trueadm/t7) - A light-weight virtual-dom template library
- [html-template-tag](https://www.npmjs.com/package/html-template-tag) - ES6 Tagged Template for compiling HTML template strings.
- [clean-tagged-string](https://www.npmjs.com/package/clean-tagged-string) - A simple utility function to clean ES6 template strings.
- [multiline-tag](https://www.npmjs.com/package/multiline-tag) - Tags for template strings making them behave like coffee multiline strings
- [deindent](https://www.npmjs.com/package/deindent) - ES6 template string helper for deindentation.
- [heredoc-tag](https://www.npmjs.com/package/heredoc-tag) - Heredoc helpers for ES2015 template strings
- [regx](https://www.npmjs.com/package/regx) - Tagged template string regular expression compiler.
- [regexr](https://www.npmjs.org/package/regexr) - Provides an ES6 template tag function that makes it easy to compose regexes out of template strings without double-escaped hell.
- [url-escape-tag](https://www.npmjs.com/package/url-escape-tag) - A template tag for escaping url parameters based on ES2015 tagged templates.
- [shell-escape-tag](https://www.npmjs.com/package/shell-escape-tag) - An ES6+ template tag which escapes parameters for interpolation into shell commands.
- [sql-tags](https://www.npmjs.com/package/sql-tags) - ES6 tagged template string functions for SQL statements.
- [sql-tag](https://www.npmjs.com/package/sql-tag) - A template tag for writing elegant sql strings.
- [sequelize-sql-tag](https://www.npmjs.com/package/sequelize-sql-tag) - A sequelize plugin for sql-tag
- [pg-sql-tag](https://www.npmjs.com/package/pg-sql-tag) - A pg plugin for sql-tag
- [sql-template-strings](https://www.npmjs.com/package/sql-template-strings) - ES6 tagged template strings for prepared statements with mysql and postgres
- [sql-composer](https://www.npmjs.com/package/sql-composer) - Composable SQL template strings for Node.js
- [pg-template-tag](https://www.npmjs.com/package/pg-template-tag) - ECMAScript 6 (2015) template tag function to write queries for node-postgres.
- [digraph-tag](https://www.npmjs.com/package/digraph-tag) - ES6 string template tag for quickly generating directed graph data
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install supports-color
```


## Usage

```js
const supportsColor = require('supports-color');

if (supportsColor.stdout) {
	console.log('Terminal stdout supports color');
}

if (supportsColor.stdout.has256) {
	console.log('Terminal stdout supports 256 colors');
}

if (supportsColor.stderr.has16m) {
	console.log('Terminal stderr supports 16 million colors (truecolor)');
}
```


## API

Returns an `Object` with a `stdout` and `stderr` property for testing either streams. Each property is an `Object`, or `false` if color is not supported.

The `stdout`/`stderr` objects specifies a level of support for color through a `.level` property and a corresponding flag:

- `.level = 1` and `.hasBasic = true`: Basic color support (16 colors)
- `.level = 2` and `.has256 = true`: 256 color support
- `.level = 3` and `.has16m = true`: Truecolor support (16 million colors)


## Info

It obeys the `--color` and `--no-color` CLI flags.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add the environment variable `FORCE_COLOR=1` to forcefully enable color or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.

Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)


## License

MIT
# has-flag [![Build Status](https://travis-ci.org/sindresorhus/has-flag.svg?branch=master)](https://travis-ci.org/sindresorhus/has-flag)

> Check if [`argv`](https://nodejs.org/docs/latest/api/process.html#process_process_argv) has a specific flag

Correctly stops looking after an `--` argument terminator.


## Install

```
$ npm install --save has-flag
```


## Usage

```js
// foo.js
const hasFlag = require('has-flag');

hasFlag('unicorn');
//=> true

hasFlag('--unicorn');
//=> true

hasFlag('-f');
//=> true

hasFlag('foo=bar');
//=> true

hasFlag('foo');
//=> false

hasFlag('rainbow');
//=> false
```

```
$ node foo.js -f --unicorn --foo=bar -- --rainbow
```


## API

### hasFlag(flag, [argv])

Returns a boolean whether the flag exists.

#### flag

Type: `string`

CLI flag to look for. The `--` prefix is optional.

#### argv

Type: `array`<br>
Default: `process.argv`

CLI arguments.


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# ms

[![Build Status](https://travis-ci.org/zeit/ms.svg?branch=master)](https://travis-ci.org/zeit/ms)
[![Slack Channel](http://zeit-slackin.now.sh/badge.svg)](https://zeit.chat/)

Use this package to easily convert various time formats to milliseconds.

## Examples

```js
ms('2 days')  // 172800000
ms('1d')      // 86400000
ms('10h')     // 36000000
ms('2.5 hrs') // 9000000
ms('2h')      // 7200000
ms('1m')      // 60000
ms('5s')      // 5000
ms('1y')      // 31557600000
ms('100')     // 100
```

### Convert from milliseconds

```js
ms(60000)             // "1m"
ms(2 * 60000)         // "2m"
ms(ms('10 hours'))    // "10h"
```

### Time format written-out

```js
ms(60000, { long: true })             // "1 minute"
ms(2 * 60000, { long: true })         // "2 minutes"
ms(ms('10 hours'), { long: true })    // "10 hours"
```

## Features

- Works both in [node](https://nodejs.org) and in the browser.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as a number (e.g.: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of equivalent ms is returned.

## Caught a bug?

1. [Fork](https://help.github.com/articles/fork-a-repo/) this repository to your own GitHub account and then [clone](https://help.github.com/articles/cloning-a-repository/) it to your local device
2. Link the package to the global module directory: `npm link`
3. Within the module you want to test your local development instance of ms, just link it to the dependencies: `npm link ms`. Instead of the default one from npm, node will now use your clone of ms!

As always, you can run the tests using: `npm test`
# strip-ansi [![Build Status](https://travis-ci.org/chalk/strip-ansi.svg?branch=master)](https://travis-ci.org/chalk/strip-ansi)

> Strip [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code)


## Install

```
$ npm install --save strip-ansi
```


## Usage

```js
var stripAnsi = require('strip-ansi');

stripAnsi('\u001b[4mcake\u001b[0m');
//=> 'cake'
```


## Related

- [strip-ansi-cli](https://github.com/chalk/strip-ansi-cli) - CLI for this module
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# cli-truncate [![Build Status](https://travis-ci.org/sindresorhus/cli-truncate.svg?branch=master)](https://travis-ci.org/sindresorhus/cli-truncate)

> Truncate a string to a specific width in the terminal

Gracefully handles [ANSI escapes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles). Like a string styled with [`chalk`](https://github.com/chalk/chalk).


## Install

```
$ npm install --save cli-truncate
```


## Usage

```js
const cliTruncate = require('cli-truncate');

cliTruncate('unicorn', 4);
//=> 'uni…'

// truncate at different positions
cliTruncate('unicorn', 4, {position: 'start'});
//=> '…orn'

cliTruncate('unicorn', 4, {position: 'middle'});
//=> 'un…n'

cliTruncate('\u001b[31municorn\u001b[39m', 4);
//=> '\u001b[31muni\u001b[39m…'

// truncate the paragraph to the terminal width
const paragraph = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.';
cliTruncate(paragraph, process.stdout.columns));
//=> 'Lorem ipsum dolor sit amet, consectetuer adipiscing…'
```


## API

### cliTruncate(input, columns, [options])

#### input

Type: `string`

Text to truncate.

#### columns

Type: `number`

Columns to occupy in the terminal.

#### options

##### position

Type: `string`<br>
Default: `'end'`<br>
Values: `'start'`, `'middle'`, `'end'`

Position to truncate the string.


## Related

- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes
- [slice-ansi](https://github.com/chalk/slice-ansi) - Slice a string with ANSI escape codes


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# exit-hook [![Build Status](https://travis-ci.org/sindresorhus/exit-hook.svg?branch=master)](https://travis-ci.org/sindresorhus/exit-hook)

> Run some code when the process exits

The `process.on('exit')` event doesn't catch all the ways a process can exit.

Useful for cleaning up.


## Install

```sh
$ npm install --save exit-hook
```


## Usage

```js
var exitHook = require('exit-hook');

exitHook(function () {
	console.log('exiting');
});

// you can add multiple hooks, even across files
exitHook(function () {
	console.log('exiting 2');
});

throw new Error('unicorns');

//=> exiting
//=> exiting 2
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
<h1 align="center">
	<br>
	<br>
	<img width="320" src="media/logo.svg" alt="Chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Build Status](https://travis-ci.org/chalk/chalk.svg?branch=master)](https://travis-ci.org/chalk/chalk) [![Coverage Status](https://coveralls.io/repos/github/chalk/chalk/badge.svg?branch=master)](https://coveralls.io/github/chalk/chalk?branch=master) [![](https://img.shields.io/badge/unicorn-approved-ff69b4.svg)](https://www.youtube.com/watch?v=9auOCbH5Ns4) [![XO code style](https://img.shields.io/badge/code_style-XO-5ed9c7.svg)](https://github.com/xojs/xo) [![Mentioned in Awesome Node.js](https://awesome.re/mentioned-badge.svg)](https://github.com/sindresorhus/awesome-nodejs)

### [See what's new in Chalk 2](https://github.com/chalk/chalk/releases/tag/v2.0.0)

<img src="https://cdn.rawgit.com/chalk/ansi-styles/8261697c95bf34b6c7767e2cbe9941a851d59385/screenshot.svg" alt="" width="900">


## Highlights

- Expressive API
- Highly performant
- Ability to nest styles
- [256/Truecolor color support](#256-and-truecolor-color-support)
- Auto-detects color support
- Doesn't extend `String.prototype`
- Clean and focused
- Actively maintained
- [Used by ~23,000 packages](https://www.npmjs.com/browse/depended/chalk) as of December 31, 2017


## Install

```console
$ npm install chalk
```

<a href="https://www.patreon.com/sindresorhus">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>


## Usage

```js
const chalk = require('chalk');

console.log(chalk.blue('Hello world!'));
```

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
const chalk = require('chalk');
const log = console.log;

// Combine styled and normal strings
log(chalk.blue('Hello') + ' World' + chalk.red('!'));

// Compose multiple styles using the chainable API
log(chalk.blue.bgRed.bold('Hello world!'));

// Pass in multiple arguments
log(chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz'));

// Nest styles
log(chalk.red('Hello', chalk.underline.bgBlue('world') + '!'));

// Nest styles of the same type even (color, underline, background)
log(chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
));

// ES2015 template literal
log(`
CPU: ${chalk.red('90%')}
RAM: ${chalk.green('40%')}
DISK: ${chalk.yellow('70%')}
`);

// ES2015 tagged template literal
log(chalk`
CPU: {red ${cpu.totalPercent}%}
RAM: {green ${ram.used / ram.total * 100}%}
DISK: {rgb(255,131,0) ${disk.used / disk.total * 100}%}
`);

// Use RGB colors in terminal emulators that support it.
log(chalk.keyword('orange')('Yay for orange colored text!'));
log(chalk.rgb(123, 45, 67).underline('Underlined reddish color'));
log(chalk.hex('#DEADED').bold('Bold gray!'));
```

Easily define your own themes:

```js
const chalk = require('chalk');

const error = chalk.bold.red;
const warning = chalk.keyword('orange');

console.log(error('Error!'));
console.log(warning('Warning!'));
```

Take advantage of console.log [string substitution](https://nodejs.org/docs/latest/api/console.html#console_console_log_data_args):

```js
const name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> 'Hello Sindre'
```


## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `chalk.red.yellow.green` is equivalent to `chalk.green`.

Multiple arguments will be separated by space.

### chalk.enabled

Color support is automatically detected, as is the level (see `chalk.level`). However, if you'd like to simply enable/disable Chalk, you can do so via the `.enabled` property.

Chalk is enabled by default unless explicitly disabled via the constructor or `chalk.level` is `0`.

If you need to change this in a reusable module, create a new instance:

```js
const ctx = new chalk.constructor({enabled: false});
```

### chalk.level

Color support is automatically detected, but you can override it by setting the `level` property. You should however only do this in your own code as it applies globally to all Chalk consumers.

If you need to change this in a reusable module, create a new instance:

```js
const ctx = new chalk.constructor({level: 0});
```

Levels are as follows:

0. All colors disabled
1. Basic color support (16 colors)
2. 256 color support
3. Truecolor support (16 million colors)

### chalk.supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add the environment variable `FORCE_COLOR=1` to forcefully enable color or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.

Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(Not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(Not widely supported)*
- `visible` (Text is emitted only if enabled)

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue` *(On Windows the bright version is used since normal blue is illegible)*
- `magenta`
- `cyan`
- `white`
- `gray` ("bright black")
- `redBright`
- `greenBright`
- `yellowBright`
- `blueBright`
- `magentaBright`
- `cyanBright`
- `whiteBright`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`
- `bgBlackBright`
- `bgRedBright`
- `bgGreenBright`
- `bgYellowBright`
- `bgBlueBright`
- `bgMagentaBright`
- `bgCyanBright`
- `bgWhiteBright`


## Tagged template literal

Chalk can be used as a [tagged template literal](http://exploringjs.com/es6/ch_template-literals.html#_tagged-template-literals).

```js
const chalk = require('chalk');

const miles = 18;
const calculateFeet = miles => miles * 5280;

console.log(chalk`
  There are {bold 5280 feet} in a mile.
  In {bold ${miles} miles}, there are {green.bold ${calculateFeet(miles)} feet}.
`);
```

Blocks are delimited by an opening curly brace (`{`), a style, some content, and a closing curly brace (`}`).

Template styles are chained exactly like normal Chalk styles. The following two statements are equivalent:

```js
console.log(chalk.bold.rgb(10, 100, 200)('Hello!'));
console.log(chalk`{bold.rgb(10,100,200) Hello!}`);
```

Note that function styles (`rgb()`, `hsl()`, `keyword()`, etc.) may not contain spaces between parameters.

All interpolated values (`` chalk`${foo}` ``) are converted to strings via the `.toString()` method. All curly braces (`{` and `}`) in interpolated value strings are escaped.


## 256 and Truecolor color support

Chalk supports 256 colors and [Truecolor](https://gist.github.com/XVilka/8346728) (16 million colors) on supported terminal apps.

Colors are downsampled from 16 million RGB values to an ANSI color format that is supported by the terminal emulator (or by specifying `{level: n}` as a Chalk option). For example, Chalk configured to run at level 1 (basic color support) will downsample an RGB value of #FF0000 (red) to 31 (ANSI escape for red).

Examples:

- `chalk.hex('#DEADED').underline('Hello, world!')`
- `chalk.keyword('orange')('Some orange text')`
- `chalk.rgb(15, 100, 204).inverse('Hello!')`

Background versions of these models are prefixed with `bg` and the first level of the module capitalized (e.g. `keyword` for foreground colors and `bgKeyword` for background colors).

- `chalk.bgHex('#DEADED').underline('Hello, world!')`
- `chalk.bgKeyword('orange')('Some orange text')`
- `chalk.bgRgb(15, 100, 204).inverse('Hello!')`

The following color models can be used:

- [`rgb`](https://en.wikipedia.org/wiki/RGB_color_model) - Example: `chalk.rgb(255, 136, 0).bold('Orange!')`
- [`hex`](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) - Example: `chalk.hex('#FF8800').bold('Orange!')`
- [`keyword`](https://www.w3.org/wiki/CSS/Properties/color/keywords) (CSS keywords) - Example: `chalk.keyword('orange').bold('Orange!')`
- [`hsl`](https://en.wikipedia.org/wiki/HSL_and_HSV) - Example: `chalk.hsl(32, 100, 50).bold('Orange!')`
- [`hsv`](https://en.wikipedia.org/wiki/HSL_and_HSV) - Example: `chalk.hsv(32, 100, 100).bold('Orange!')`
- [`hwb`](https://en.wikipedia.org/wiki/HWB_color_model)  - Example: `chalk.hwb(32, 0, 50).bold('Orange!')`
- `ansi16`
- `ansi256`


## Windows

If you're on Windows, do yourself a favor and use [`cmder`](http://cmder.net/) instead of `cmd.exe`.


## Origin story

[colors.js](https://github.com/Marak/colors.js) used to be the most popular string styling module, but it has serious deficiencies like extending `String.prototype` which causes all kinds of [problems](https://github.com/yeoman/yo/issues/68) and the package is unmaintained. Although there are other packages, they either do too much or not enough. Chalk is a clean and focused alternative.


## Related

- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [strip-ansi-stream](https://github.com/chalk/strip-ansi-stream) - Strip ANSI escape codes from a stream
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes
- [slice-ansi](https://github.com/chalk/slice-ansi) - Slice a string with ANSI escape codes
- [color-convert](https://github.com/qix-/color-convert) - Converts colors between different models
- [chalk-animation](https://github.com/bokub/chalk-animation) - Animate strings in the terminal
- [gradient-string](https://github.com/bokub/gradient-string) - Apply color gradients to strings
- [chalk-pipe](https://github.com/LitoMore/chalk-pipe) - Create chalk style schemes with simpler style strings
- [terminal-link](https://github.com/sindresorhus/terminal-link) - Create clickable links in the terminal


## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)


## License

MIT
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install supports-color
```


## Usage

```js
const supportsColor = require('supports-color');

if (supportsColor.stdout) {
	console.log('Terminal stdout supports color');
}

if (supportsColor.stdout.has256) {
	console.log('Terminal stdout supports 256 colors');
}

if (supportsColor.stderr.has16m) {
	console.log('Terminal stderr supports 16 million colors (truecolor)');
}
```


## API

Returns an `Object` with a `stdout` and `stderr` property for testing either streams. Each property is an `Object`, or `false` if color is not supported.

The `stdout`/`stderr` objects specifies a level of support for color through a `.level` property and a corresponding flag:

- `.level = 1` and `.hasBasic = true`: Basic color support (16 colors)
- `.level = 2` and `.has256 = true`: 256 color support
- `.level = 3` and `.has16m = true`: Truecolor support (16 million colors)


## Info

It obeys the `--color` and `--no-color` CLI flags.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add the environment variable `FORCE_COLOR=1` to forcefully enable color or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.

Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)


## License

MIT
# ansi-styles [![Build Status](https://travis-ci.org/chalk/ansi-styles.svg?branch=master)](https://travis-ci.org/chalk/ansi-styles)

> [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles) for styling strings in the terminal

You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

<img src="https://cdn.rawgit.com/chalk/ansi-styles/8261697c95bf34b6c7767e2cbe9941a851d59385/screenshot.svg" width="900">


## Install

```
$ npm install ansi-styles
```


## Usage

```js
const style = require('ansi-styles');

console.log(`${style.green.open}Hello world!${style.green.close}`);


// Color conversion between 16/256/truecolor
// NOTE: If conversion goes to 16 colors or 256 colors, the original color
//       may be degraded to fit that color palette. This means terminals
//       that do not support 16 million colors will best-match the
//       original color.
console.log(style.bgColor.ansi.hsl(120, 80, 72) + 'Hello world!' + style.bgColor.close);
console.log(style.color.ansi256.rgb(199, 20, 250) + 'Hello world!' + style.color.close);
console.log(style.color.ansi16m.hex('#ABCDEF') + 'Hello world!' + style.color.close);
```

## API

Each style has an `open` and `close` property.


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(Not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(Not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `gray` ("bright black")
- `redBright`
- `greenBright`
- `yellowBright`
- `blueBright`
- `magentaBright`
- `cyanBright`
- `whiteBright`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`
- `bgBlackBright`
- `bgRedBright`
- `bgGreenBright`
- `bgYellowBright`
- `bgBlueBright`
- `bgMagentaBright`
- `bgCyanBright`
- `bgWhiteBright`


## Advanced usage

By default, you get a map of styles, but the styles are also available as groups. They are non-enumerable so they don't show up unless you access them explicitly. This makes it easier to expose only a subset in a higher-level module.

- `style.modifier`
- `style.color`
- `style.bgColor`

###### Example

```js
console.log(style.color.green.open);
```

Raw escape codes (i.e. without the CSI escape prefix `\u001B[` and render mode postfix `m`) are available under `style.codes`, which returns a `Map` with the open codes as keys and close codes as values.

###### Example

```js
console.log(style.codes.get(36));
//=> 39
```


## [256 / 16 million (TrueColor) support](https://gist.github.com/XVilka/8346728)

`ansi-styles` uses the [`color-convert`](https://github.com/Qix-/color-convert) package to allow for converting between various colors and ANSI escapes, with support for 256 and 16 million colors.

To use these, call the associated conversion function with the intended output, for example:

```js
style.color.ansi.rgb(100, 200, 15); // RGB to 16 color ansi foreground code
style.bgColor.ansi.rgb(100, 200, 15); // RGB to 16 color ansi background code

style.color.ansi256.hsl(120, 100, 60); // HSL to 256 color ansi foreground code
style.bgColor.ansi256.hsl(120, 100, 60); // HSL to 256 color ansi foreground code

style.color.ansi16m.hex('#C0FFEE'); // Hex (RGB) to 16 million color foreground code
style.bgColor.ansi16m.hex('#C0FFEE'); // Hex (RGB) to 16 million color background code
```


## Related

- [ansi-escapes](https://github.com/sindresorhus/ansi-escapes) - ANSI escape codes for manipulating the terminal


## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)


## License

MIT
# shebang-command [![Build Status](https://travis-ci.org/kevva/shebang-command.svg?branch=master)](https://travis-ci.org/kevva/shebang-command)

> Get the command from a shebang


## Install

```
$ npm install --save shebang-command
```


## Usage

```js
const shebangCommand = require('shebang-command');

shebangCommand('#!/usr/bin/env node');
//=> 'node'

shebangCommand('#!/bin/bash');
//=> 'bash'
```


## API

### shebangCommand(string)

#### string

Type: `string`

String containing a shebang.


## License

MIT © [Kevin Martensson](http://github.com/kevva)
# log-symbols [![Build Status](https://travis-ci.org/sindresorhus/log-symbols.svg?branch=master)](https://travis-ci.org/sindresorhus/log-symbols)

<img src="screenshot.png" width="226" align="right">

> Colored symbols for various log levels

Includes fallbacks for Windows CMD which only supports a [limited character set](https://en.wikipedia.org/wiki/Code_page_437).


## Install

```
$ npm install log-symbols
```


## Usage

```js
const logSymbols = require('log-symbols');

console.log(logSymbols.success, 'Finished successfully!');
// On good OSes:  ✔ Finished successfully!
// On Windows:    √ Finished successfully!
```

## API

### logSymbols

#### info
#### success
#### warning
#### error


## Related

- [figures](https://github.com/sindresorhus/figures) - Unicode symbols with Windows CMD fallbacks
- [py-log-symbols](https://github.com/ManrajGrover/py-log-symbols) - Python port


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# os-homedir [![Build Status](https://travis-ci.org/sindresorhus/os-homedir.svg?branch=master)](https://travis-ci.org/sindresorhus/os-homedir)

> Node.js 4 [`os.homedir()`](https://nodejs.org/api/os.html#os_os_homedir) [ponyfill](https://ponyfill.com)


## Install

```
$ npm install --save os-homedir
```


## Usage

```js
const osHomedir = require('os-homedir');

console.log(osHomedir());
//=> '/Users/sindresorhus'
```


## Related

- [user-home](https://github.com/sindresorhus/user-home) - Same as this module but caches the result
- [home-or-tmp](https://github.com/sindresorhus/home-or-tmp) - Get the user home directory with fallback to the system temp directory


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
process-nextick-args
=====

[![Build Status](https://travis-ci.org/calvinmetcalf/process-nextick-args.svg?branch=master)](https://travis-ci.org/calvinmetcalf/process-nextick-args)

```bash
npm install --save process-nextick-args
```

Always be able to pass arguments to process.nextTick, no matter the platform

```js
var pna = require('process-nextick-args');

pna.nextTick(function (a, b, c) {
  console.log(a, b, c);
}, 'step', 3,  'profit');
```
# figures [![Build Status: Linux](https://travis-ci.org/sindresorhus/figures.svg?branch=master)](https://travis-ci.org/sindresorhus/figures) [![Build status: Windows](https://ci.appveyor.com/api/projects/status/mb743hl70269be3r/branch/master?svg=true)](https://ci.appveyor.com/project/sindresorhus/figures/branch/master)

> Unicode symbols with Windows CMD fallbacks

[![](screenshot.png)](index.js)

[*and more...*](index.js)

Windows CMD only supports a [limited character set](http://en.wikipedia.org/wiki/Code_page_437).


## Install

```
$ npm install --save figures
```


## Usage

See the [source](index.js) for supported symbols.

```js
const figures = require('figures');

console.log(figures('✔︎ check'));
// On real OSes:  ✔︎ check
// On Windows:    √ check

console.log(figures.tick);
// On real OSes:  ✔︎
// On Windows:    √
```


## API

### figures(input)

Returns the input with replaced fallback unicode symbols on Windows.

All the below [figures](#figures) are attached to the main export as shown in the example above.

#### input

Type: `string`

String where the unicode symbols will be replaced with fallback symbols depending on the OS.


## Figures

| Name               | Real OSes | Windows |
| ------------------ | :-------: | :-----: |
| tick               |     ✔     |    √    |
| cross              |     ✖     |    ×    |
| star               |     ★     |    *    |
| square             |     ▇     |    █    |
| squareSmall        |     ◻     |   [ ]   |
| squareSmallFilled  |     ◼     |   [█]   |
| play               |     ▶     |    ►    |
| circle             |     ◯     |   ( )   |
| circleFilled       |     ◉     |   (*)   |
| circleDotted       |     ◌     |   ( )   |
| circleDouble       |     ◎     |   ( )   |
| circleCircle       |     ⓞ     |   (○)   |
| circleCross        |     ⓧ     |   (×)   |
| circlePipe         |     Ⓘ     |   (│)   |
| circleQuestionMark |     ?⃝    |   (?)   |
| bullet             |     ●     |    *    |
| dot                |     ․     |    .    |
| line               |     ─     |    ─    |
| ellipsis           |     …     |   ...   |
| pointer            |     ❯     |    >    |
| pointerSmall       |     ›     |    »    |
| info               |     ℹ     |    i    |
| warning            |     ⚠     |    ‼    |
| hamburger          |     ☰     |    ≡    |
| smiley             |     ㋡     |    ☺    |
| mustache           |     ෴     |   ┌─┐   |
| heart              |     ♥     |    ♥    |
| arrowUp            |     ↑     |    ↑    |
| arrowDown          |     ↓     |    ↓    |
| arrowLeft          |     ←     |    ←    |
| arrowRight         |     →     |    →    |
| radioOn            |     ◉     |   (*)   |
| radioOff           |     ◯     |   ( )   |
| checkboxOn         |     ☒     |   [×]   |
| checkboxOff        |     ☐     |   [ ]   |
| checkboxCircleOn   |     ⓧ     |   (×)   |
| checkboxCircleOff  |     Ⓘ     |   ( )   |
| questionMarkPrefix |     ?⃝    |    ？    |
| oneHalf            |     ½     |   1/2   |
| oneThird           |     ⅓     |   1/3   |
| oneQuarter         |     ¼     |   1/4   |
| oneFifth           |     ⅕     |   1/5   |
| oneSixth           |     ⅙     |   1/6   |
| oneSeventh         |     ⅐     |   1/7   |
| oneEighth          |     ⅛     |   1/8   |
| oneNinth           |     ⅑     |   1/9   |
| oneTenth           |     ⅒     |   1/10  |
| twoThirds          |     ⅔     |   2/3   |
| twoFifths          |     ⅖     |   2/5   |
| threeQuarters      |     ¾     |   3/4   |
| threeFifths        |     ⅗     |   3/5   |
| threeEighths       |     ⅜     |   3/8   |
| fourFifths         |     ⅘     |   4/5   |
| fiveSixths         |     ⅚     |   5/6   |
| fiveEighths        |     ⅝     |   5/8   |
| sevenEighths       |     ⅞     |   7/8   |


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# typedarray

TypedArray polyfill ripped from [this
module](https://raw.github.com/inexorabletash/polyfill).

[![build status](https://secure.travis-ci.org/substack/typedarray.png)](http://travis-ci.org/substack/typedarray)

[![testling badge](https://ci.testling.com/substack/typedarray.png)](https://ci.testling.com/substack/typedarray)

# example

``` js
var Uint8Array = require('typedarray').Uint8Array;
var ua = new Uint8Array(5);
ua[1] = 256 + 55;
console.log(ua[1]);
```

output:

```
55
```

# methods

``` js
var TA = require('typedarray')
```

The `TA` object has the following constructors:

* TA.ArrayBuffer
* TA.DataView
* TA.Float32Array
* TA.Float64Array
* TA.Int8Array
* TA.Int16Array
* TA.Int32Array
* TA.Uint8Array
* TA.Uint8ClampedArray
* TA.Uint16Array
* TA.Uint32Array

# install

With [npm](https://npmjs.org) do:

```
npm install typedarray
```

To use this module in the browser, compile with
[browserify](http://browserify.org)
or download a UMD build from browserify CDN:

http://wzrd.in/standalone/typedarray@latest

# license

MIT
# execa [![Build Status: Linux](https://travis-ci.org/sindresorhus/execa.svg?branch=master)](https://travis-ci.org/sindresorhus/execa) [![Build status: Windows](https://ci.appveyor.com/api/projects/status/x5ajamxtjtt93cqv/branch/master?svg=true)](https://ci.appveyor.com/project/sindresorhus/execa/branch/master) [![Coverage Status](https://coveralls.io/repos/github/sindresorhus/execa/badge.svg?branch=master)](https://coveralls.io/github/sindresorhus/execa?branch=master)

> A better [`child_process`](https://nodejs.org/api/child_process.html)


## Why

- Promise interface.
- [Strips EOF](https://github.com/sindresorhus/strip-eof) from the output so you don't have to `stdout.trim()`.
- Supports [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) binaries cross-platform.
- [Improved Windows support.](https://github.com/IndigoUnited/node-cross-spawn#why)
- Higher max buffer. 10 MB instead of 200 KB.
- [Executes locally installed binaries by name.](#preferlocal)
- [Cleans up spawned processes when the parent process dies.](#cleanup)


## Install

```
$ npm install --save execa
```


## Usage

```js
const execa = require('execa');

execa('echo', ['unicorns']).then(result => {
	console.log(result.stdout);
	//=> 'unicorns'
});

// pipe the child process stdout to the current stdout
execa('echo', ['unicorns']).stdout.pipe(process.stdout);

execa.shell('echo unicorns').then(result => {
	console.log(result.stdout);
	//=> 'unicorns'
});

// example of catching an error
execa.shell('exit 3').catch(error => {
	console.log(error);
	/*
	{
		message: 'Command failed: /bin/sh -c exit 3'
		killed: false,
		code: 3,
		signal: null,
		cmd: '/bin/sh -c exit 3',
		stdout: '',
		stderr: '',
		timedOut: false
	}
	*/
});

// example of catching an error with a sync method
try {
	execa.shellSync('exit 3');
} catch (err) {
	console.log(err);
	/*
	{
		message: 'Command failed: /bin/sh -c exit 3'
		code: 3,
		signal: null,
		cmd: '/bin/sh -c exit 3',
		stdout: '',
		stderr: '',
		timedOut: false
	}
	*/
}
```


## API

### execa(file, [arguments], [options])

Execute a file.

Think of this as a mix of `child_process.execFile` and `child_process.spawn`.

Returns a [`child_process` instance](https://nodejs.org/api/child_process.html#child_process_class_childprocess), which is enhanced to also be a `Promise` for a result `Object` with `stdout` and `stderr` properties.

### execa.stdout(file, [arguments], [options])

Same as `execa()`, but returns only `stdout`.

### execa.stderr(file, [arguments], [options])

Same as `execa()`, but returns only `stderr`.

### execa.shell(command, [options])

Execute a command through the system shell. Prefer `execa()` whenever possible, as it's both faster and safer.

Returns a [`child_process` instance](https://nodejs.org/api/child_process.html#child_process_class_childprocess).

The `child_process` instance is enhanced to also be promise for a result object with `stdout` and `stderr` properties.

### execa.sync(file, [arguments], [options])

Execute a file synchronously.

Returns the same result object as [`child_process.spawnSync`](https://nodejs.org/api/child_process.html#child_process_child_process_spawnsync_command_args_options).

This method throws an `Error` if the command fails.

### execa.shellSync(file, [options])

Execute a command synchronously through the system shell.

Returns the same result object as [`child_process.spawnSync`](https://nodejs.org/api/child_process.html#child_process_child_process_spawnsync_command_args_options).

### options

Type: `Object`

#### cwd

Type: `string`<br>
Default: `process.cwd()`

Current working directory of the child process.

#### env

Type: `Object`<br>
Default: `process.env`

Environment key-value pairs. Extends automatically from `process.env`. Set `extendEnv` to `false` if you don't want this.

#### extendEnv

Type: `boolean`<br>
Default: `true`

Set to `false` if you don't want to extend the environment variables when providing the `env` property.

#### argv0

Type: `string`

Explicitly set the value of `argv[0]` sent to the child process. This will be set to `command` or `file` if not specified.

#### stdio

Type: `Array` `string`<br>
Default: `pipe`

Child's [stdio](https://nodejs.org/api/child_process.html#child_process_options_stdio) configuration.

#### detached

Type: `boolean`

Prepare child to run independently of its parent process. Specific behavior [depends on the platform](https://nodejs.org/api/child_process.html#child_process_options_detached).

#### uid

Type: `number`

Sets the user identity of the process.

#### gid

Type: `number`

Sets the group identity of the process.

#### shell

Type: `boolean` `string`<br>
Default: `false`

If `true`, runs `command` inside of a shell. Uses `/bin/sh` on UNIX and `cmd.exe` on Windows. A different shell can be specified as a string. The shell should understand the `-c` switch on UNIX or `/d /s /c` on Windows.

#### stripEof

Type: `boolean`<br>
Default: `true`

[Strip EOF](https://github.com/sindresorhus/strip-eof) (last newline) from the output.

#### preferLocal

Type: `boolean`<br>
Default: `true`

Prefer locally installed binaries when looking for a binary to execute.<br>
If you `$ npm install foo`, you can then `execa('foo')`.

#### localDir

Type: `string`<br>
Default: `process.cwd()`

Preferred path to find locally installed binaries in (use with `preferLocal`).

#### input

Type: `string` `Buffer` `stream.Readable`

Write some input to the `stdin` of your binary.<br>
Streams are not allowed when using the synchronous methods.

#### reject

Type: `boolean`<br>
Default: `true`

Setting this to `false` resolves the promise with the error instead of rejecting it.

#### cleanup

Type: `boolean`<br>
Default: `true`

Keep track of the spawned process and `kill` it when the parent process exits.

#### encoding

Type: `string`<br>
Default: `utf8`

Specify the character encoding used to decode the `stdout` and `stderr` output.

#### timeout

Type: `number`<br>
Default: `0`

If timeout is greater than `0`, the parent will send the signal identified by the `killSignal` property (the default is `SIGTERM`) if the child runs longer than timeout milliseconds.

#### maxBuffer

Type: `number`<br>
Default: `10000000` (10MB)

Largest amount of data in bytes allowed on `stdout` or `stderr`.

#### killSignal

Type: `string` `number`<br>
Default: `SIGTERM`

Signal value to be used when the spawned process will be killed.

#### stdin

Type: `string` `number` `Stream` `undefined` `null`<br>
Default: `pipe`

Same options as [`stdio`](https://nodejs.org/dist/latest-v6.x/docs/api/child_process.html#child_process_options_stdio).

#### stdout

Type: `string` `number` `Stream` `undefined` `null`<br>
Default: `pipe`

Same options as [`stdio`](https://nodejs.org/dist/latest-v6.x/docs/api/child_process.html#child_process_options_stdio).

#### stderr

Type: `string` `number` `Stream` `undefined` `null`<br>
Default: `pipe`

Same options as [`stdio`](https://nodejs.org/dist/latest-v6.x/docs/api/child_process.html#child_process_options_stdio).

#### windowsVerbatimArguments

Type: `boolean`<br>
Default: `false`

If `true`, no quoting or escaping of arguments is done on Windows. Ignored on other platforms. This is set to `true` automatically when the `shell` option is `true`.


## Tips

### Save and pipe output from a child process

Let's say you want to show the output of a child process in real-time while also saving it to a variable.

```js
const execa = require('execa');
const getStream = require('get-stream');

const stream = execa('echo', ['foo']).stdout;

stream.pipe(process.stdout);

getStream(stream).then(value => {
	console.log('child output:', value);
});
```


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
<a href="http://promises-aplus.github.com/promises-spec"><img src="http://promises-aplus.github.com/promises-spec/assets/logo-small.png" align="right" /></a>
# is-promise

  Test whether an object looks like a promises-a+ promise

 [![Build Status](https://img.shields.io/travis/then/is-promise/master.svg)](https://travis-ci.org/then/is-promise)
 [![Dependency Status](https://img.shields.io/gemnasium/then/is-promise.svg)](https://gemnasium.com/then/is-promise)
 [![NPM version](https://img.shields.io/npm/v/is-promise.svg)](https://www.npmjs.org/package/is-promise)

## Installation

    $ npm install is-promise

You can also use it client side via npm.

## API

```javascript
var isPromise = require('is-promise');

isPromise({then:function () {...}});//=>true
isPromise(null);//=>false
isPromise({});//=>false
isPromise({then: true})//=>false
```

## License

  MIT
# minimist

parse argument options

This module is the guts of optimist's argument parser without all the
fanciful decoration.

[![browser support](https://ci.testling.com/substack/minimist.png)](http://ci.testling.com/substack/minimist)

[![build status](https://secure.travis-ci.org/substack/minimist.png)](http://travis-ci.org/substack/minimist)

# example

``` js
var argv = require('minimist')(process.argv.slice(2));
console.dir(argv);
```

```
$ node example/parse.js -a beep -b boop
{ _: [], a: 'beep', b: 'boop' }
```

```
$ node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
{ _: [ 'foo', 'bar', 'baz' ],
  x: 3,
  y: 4,
  n: 5,
  a: true,
  b: true,
  c: true,
  beep: 'boop' }
```

# methods

``` js
var parseArgs = require('minimist')
```

## var argv = parseArgs(args, opts={})

Return an argument object `argv` populated with the array arguments from `args`.

`argv._` contains all the arguments that didn't have an option associated with
them.

Numeric-looking arguments will be returned as numbers unless `opts.string` or
`opts.boolean` is set for that argument name.

Any arguments after `'--'` will not be parsed and will end up in `argv._`.

options can be:

* `opts.string` - a string or array of strings argument names to always treat as
strings
* `opts.boolean` - a boolean, string or array of strings to always treat as
booleans. if `true` will treat all double hyphenated arguments without equal signs
as boolean (e.g. affects `--foo`, not `-f` or `--foo=bar`)
* `opts.alias` - an object mapping string names to strings or arrays of string
argument names to use as aliases
* `opts.default` - an object mapping string argument names to default values
* `opts.stopEarly` - when true, populate `argv._` with everything after the
first non-option
* `opts['--']` - when true, populate `argv._` with everything before the `--`
and `argv['--']` with everything after the `--`. Here's an example:
* `opts.unknown` - a function which is invoked with a command line parameter not
defined in the `opts` configuration object. If the function returns `false`, the
unknown option is not added to `argv`.

```
> require('./')('one two three -- four five --six'.split(' '), { '--': true })
{ _: [ 'one', 'two', 'three' ],
  '--': [ 'four', 'five', '--six' ] }
```

Note that with `opts['--']` set, parsing for arguments still stops after the
`--`.

# install

With [npm](https://npmjs.org) do:

```
npm install minimist
```

# license

MIT
# p-map [![Build Status](https://travis-ci.org/sindresorhus/p-map.svg?branch=master)](https://travis-ci.org/sindresorhus/p-map)

> Map over promises concurrently

Useful when you need to run promise-returning & async functions multiple times with different inputs concurrently.


## Install

```
$ npm install p-map
```


## Usage

```js
const pMap = require('p-map');
const got = require('got');

const sites = [
	getWebsiteFromUsername('sindresorhus'), //=> Promise
	'ava.li',
	'todomvc.com',
	'github.com'
];

const mapper = el => got.head(el).then(res => res.requestUrl);

pMap(sites, mapper, {concurrency: 2}).then(result => {
	console.log(result);
	//=> ['http://sindresorhus.com/', 'http://ava.li/', 'http://todomvc.com/', 'http://github.com/']
});
```


## API

### pMap(input, mapper, [options])

Returns a `Promise` that is fulfilled when all promises in `input` and ones returned from `mapper` are fulfilled, or rejects if any of the promises reject. The fulfilled value is an `Array` of the fulfilled values returned from `mapper` in `input` order.

#### input

Type: `Iterable<Promise|any>`

Iterated over concurrently in the `mapper` function.

#### mapper(element, index)

Type: `Function`

Expected to return a `Promise` or value.

#### options

Type: `Object`

##### concurrency

Type: `number`<br>
Default: `Infinity`<br>
Minimum: `1`

Number of concurrently pending promises returned by `mapper`.


## Related

- [p-all](https://github.com/sindresorhus/p-all) - Run promise-returning & async functions concurrently with optional limited concurrency
- [p-filter](https://github.com/sindresorhus/p-filter) - Filter promises concurrently
- [p-times](https://github.com/sindresorhus/p-times) - Run promise-returning & async functions a specific number of times concurrently
- [p-props](https://github.com/sindresorhus/p-props) - Like `Promise.all()` but for `Map` and `Object`
- [p-map-series](https://github.com/sindresorhus/p-map-series) - Map over promises serially
- [p-queue](https://github.com/sindresorhus/p-queue) - Promise queue with concurrency control
- [More…](https://github.com/sindresorhus/promise-fun)


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# shebang-regex [![Build Status](https://travis-ci.org/sindresorhus/shebang-regex.svg?branch=master)](https://travis-ci.org/sindresorhus/shebang-regex)

> Regular expression for matching a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))


## Install

```
$ npm install --save shebang-regex
```


## Usage

```js
var shebangRegex = require('shebang-regex');
var str = '#!/usr/bin/env node\nconsole.log("unicorns");';

shebangRegex.test(str);
//=> true

shebangRegex.exec(str)[0];
//=> '#!/usr/bin/env node'
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# get-stream [![Build Status](https://travis-ci.org/sindresorhus/get-stream.svg?branch=master)](https://travis-ci.org/sindresorhus/get-stream)

> Get a stream as a string, buffer, or array


## Install

```
$ npm install --save get-stream
```


## Usage

```js
const fs = require('fs');
const getStream = require('get-stream');
const stream = fs.createReadStream('unicorn.txt');

getStream(stream).then(str => {
	console.log(str);
	/*
	              ,,))))))));,
	           __)))))))))))))),
	\|/       -\(((((''''((((((((.
	-*-==//////((''  .     `)))))),
	/|\      ))| o    ;-.    '(((((                                  ,(,
	         ( `|    /  )    ;))))'                               ,_))^;(~
	            |   |   |   ,))((((_     _____------~~~-.        %,;(;(>';'~
	            o_);   ;    )))(((` ~---~  `::           \      %%~~)(v;(`('~
	                  ;    ''''````         `:       `:::|\,__,%%    );`'; ~
	                 |   _                )     /      `:|`----'     `-'
	           ______/\/~    |                 /        /
	         /~;;.____/;;'  /          ___--,-(   `;;;/
	        / //  _;______;'------~~~~~    /;;/\    /
	       //  | |                        / ;   \;;,\
	      (<_  | ;                      /',/-----'  _>
	       \_| ||_                     //~;~~~~~~~~~
	           `\_|                   (,~~
	                                   \~\
	                                    ~~
	*/
});
```


## API

The methods returns a promise that resolves when the `end` event fires on the stream, indicating that there is no more data to be read. The stream is switched to flowing mode.

### getStream(stream, [options])

Get the `stream` as a string.

#### options

##### encoding

Type: `string`<br>
Default: `utf8`

[Encoding](https://nodejs.org/api/buffer.html#buffer_buffer) of the incoming stream.

##### maxBuffer

Type: `number`<br>
Default: `Infinity`

Maximum length of the returned string. If it exceeds this value before the stream ends, the promise will be rejected.

### getStream.buffer(stream, [options])

Get the `stream` as a buffer.

It honors the `maxBuffer` option as above, but it refers to byte length rather than string length.

### getStream.array(stream, [options])

Get the `stream` as an array of values.

It honors both the `maxBuffer` and `encoding` options. The behavior changes slightly based on the encoding chosen:

- When `encoding` is unset, it assumes an [object mode stream](https://nodesource.com/blog/understanding-object-streams/) and collects values emitted from `stream` unmodified. In this case `maxBuffer` refers to the number of items in the array (not the sum of their sizes).

- When `encoding` is set to `buffer`, it collects an array of buffers. `maxBuffer` refers to the summed byte lengths of every buffer in the array.

- When `encoding` is set to anything else, it collects an array of strings. `maxBuffer` refers to the summed character lengths of every string in the array.


## Errors

If the input stream emits an `error` event, the promise will be rejected with the error. The buffered data will be attached to the `bufferedData` property of the error.

```js
getStream(streamThatErrorsAtTheEnd('unicorn'))
	.catch(err => {
		console.log(err.bufferedData);
		//=> 'unicorn'
	});
```


## FAQ

### How is this different from [`concat-stream`](https://github.com/maxogden/concat-stream)?

This module accepts a stream instead of being one and returns a promise instead of using a callback. The API is simpler and it only supports returning a string, buffer, or array. It doesn't have a fragile type inference. You explicitly choose what you want. And it doesn't depend on the huge `readable-stream` package.


## Related

- [get-stdin](https://github.com/sindresorhus/get-stdin) - Get stdin as a string or buffer


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# cli-cursor [![Build Status](https://travis-ci.org/sindresorhus/cli-cursor.svg?branch=master)](https://travis-ci.org/sindresorhus/cli-cursor)

> Toggle the CLI cursor

The cursor is [gracefully restored](https://github.com/sindresorhus/restore-cursor) if the process exits.


## Install

```
$ npm install --save cli-cursor
```


## Usage

```js
const cliCursor = require('cli-cursor');

cliCursor.hide();

const unicornsAreAwesome = true;
cliCursor.toggle(unicornsAreAwesome);
```


## API

### .show()

### .hide()

### .toggle(force)

`force` is useful to show or hide the cursor based an a boolean.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# is-fullwidth-code-point [![Build Status](https://travis-ci.org/sindresorhus/is-fullwidth-code-point.svg?branch=master)](https://travis-ci.org/sindresorhus/is-fullwidth-code-point)

> Check if the character represented by a given [Unicode code point](https://en.wikipedia.org/wiki/Code_point) is [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms)


## Install

```
$ npm install --save is-fullwidth-code-point
```


## Usage

```js
var isFullwidthCodePoint = require('is-fullwidth-code-point');

isFullwidthCodePoint('谢'.codePointAt());
//=> true

isFullwidthCodePoint('a'.codePointAt());
//=> false
```


## API

### isFullwidthCodePoint(input)

#### input

Type: `number`

[Code point](https://en.wikipedia.org/wiki/Code_point) of a character.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# ansi-regex [![Build Status](https://travis-ci.org/chalk/ansi-regex.svg?branch=master)](https://travis-ci.org/chalk/ansi-regex)

> Regular expression for matching [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code)


## Install

```
$ npm install --save ansi-regex
```


## Usage

```js
const ansiRegex = require('ansi-regex');

ansiRegex().test('\u001b[4mcake\u001b[0m');
//=> true

ansiRegex().test('cake');
//=> false

'\u001b[4mcake\u001b[0m'.match(ansiRegex());
//=> ['\u001b[4m', '\u001b[0m']
```

## FAQ

### Why do you test for codes not in the ECMA 48 standard?

Some of the codes we run as a test are codes that we acquired finding various lists of non-standard or manufacturer specific codes. If I recall correctly, we test for both standard and non-standard codes, as most of them follow the same or similar format and can be safely matched in strings without the risk of removing actual string content. There are a few non-standard control codes that do not follow the traditional format (i.e. they end in numbers) thus forcing us to exclude them from the test because we cannot reliably match them.

On the historical side, those ECMA standards were established in the early 90's whereas the VT100, for example, was designed in the mid/late 70's. At that point in time, control codes were still pretty ungoverned and engineers used them for a multitude of things, namely to activate hardware ports that may have been proprietary. Somewhere else you see a similar 'anarchy' of codes is in the x86 architecture for processors; there are a ton of "interrupts" that can mean different things on certain brands of processors, most of which have been phased out.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# ora [![Build Status](https://travis-ci.org/sindresorhus/ora.svg?branch=master)](https://travis-ci.org/sindresorhus/ora)

> Elegant terminal spinner

<img src="screenshot.gif" width="629">


## Install

```
$ npm install --save ora
```


## Usage

```js
const ora = require('ora');

const spinner = ora('Loading unicorns').start();

setTimeout(() => {
	spinner.color = 'yellow';
	spinner.text = 'Loading rainbows';
}, 1000);
```


## API

It will gracefully not do anything when there's no TTY or when in a CI.

### ora([options|text])

If a string is provided, it is treated as a shortcut for [`options.text`](#text).

#### options

Type: `object`

##### text

Type: `string`

Text to display after the spinner.

##### spinner

Type: `string` `object`<br>
Default: `dots` <img src="screenshot-spinner.gif" width="14">

Name of one of the [provided spinners](https://github.com/sindresorhus/cli-spinners/blob/master/spinners.json). See `example.js` in this repo if you want to test out different spinners.

Or an object like:

```js
{
	interval: 80, // optional
	frames: ['-', '+', '-']
}
```

##### color

Type: `string`<br>
Default: `cyan`<br>
Values: `black` `red` `green` `yellow` `blue` `magenta` `cyan` `white` `gray`

Color of the spinner.

##### interval

Type: `number`<br>
Default: Provided by the spinner or `100`

Interval between each frame.

Spinners provide their own recommended interval, so you don't really need to specify this.

##### stream

Type: `WritableStream`<br>
Default: `process.stderr`

Stream to write the output.

You could for example set this to `process.stdout` instead.

##### enabled

Type: `boolean`<br>
Default: `false`

Force enabling of the spinner regardless of the `stream` not being run inside a TTY context and/or in a CI environment.

### Instance

#### .start()

Start the spinner. Returns the instance.

#### .stop()

Stop and clear the spinner. Returns the instance.

#### .clear()

Clear the spinner. Returns the instance.

#### .render()

Manually render a new frame. Returns the instance.

#### .frame()

Get a new frame.

#### .text

Change the text.

#### .color

Change the spinner color.


## Related

- [cli-spinners](https://github.com/sindresorhus/cli-spinners) - Spinners for use in the terminal


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install --save supports-color
```


## Usage

```js
var supportsColor = require('supports-color');

if (supportsColor) {
	console.log('Terminal supports color');
}
```

It obeys the `--color` and `--no-color` CLI flags.

For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
<h1 align="center">
	<br>
	<br>
	<img width="360" src="https://cdn.rawgit.com/chalk/chalk/19935d6484811c5e468817f846b7b3d417d7bf4a/logo.svg" alt="chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Build Status](https://travis-ci.org/chalk/chalk.svg?branch=master)](https://travis-ci.org/chalk/chalk)
[![Coverage Status](https://coveralls.io/repos/chalk/chalk/badge.svg?branch=master)](https://coveralls.io/r/chalk/chalk?branch=master)
[![](http://img.shields.io/badge/unicorn-approved-ff69b4.svg)](https://www.youtube.com/watch?v=9auOCbH5Ns4)


[colors.js](https://github.com/Marak/colors.js) used to be the most popular string styling module, but it has serious deficiencies like extending `String.prototype` which causes all kinds of [problems](https://github.com/yeoman/yo/issues/68). Although there are other ones, they either do too much or not enough.

**Chalk is a clean and focused alternative.**

![](https://github.com/chalk/ansi-styles/raw/master/screenshot.png)


## Why

- Highly performant
- Doesn't extend `String.prototype`
- Expressive API
- Ability to nest styles
- Clean and focused
- Auto-detects color support
- Actively maintained
- [Used by ~4500 modules](https://www.npmjs.com/browse/depended/chalk) as of July 15, 2015


## Install

```
$ npm install --save chalk
```


## Usage

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
var chalk = require('chalk');

// style a string
chalk.blue('Hello world!');

// combine styled and normal strings
chalk.blue('Hello') + 'World' + chalk.red('!');

// compose multiple styles using the chainable API
chalk.blue.bgRed.bold('Hello world!');

// pass in multiple arguments
chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz');

// nest styles
chalk.red('Hello', chalk.underline.bgBlue('world') + '!');

// nest styles of the same type even (color, underline, background)
chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
);
```

Easily define your own themes.

```js
var chalk = require('chalk');
var error = chalk.bold.red;
console.log(error('Error!'));
```

Take advantage of console.log [string substitution](http://nodejs.org/docs/latest/api/console.html#console_console_log_data).

```js
var name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> Hello Sindre
```


## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `Chalk.red.yellow.green` is equivalent to `Chalk.green`.

Multiple arguments will be separated by space.

### chalk.enabled

Color support is automatically detected, but you can override it by setting the `enabled` property. You should however only do this in your own code as it applies globally to all chalk consumers.

If you need to change this in a reusable module create a new instance:

```js
var ctx = new chalk.constructor({enabled: false});
```

### chalk.supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.

### chalk.styles

Exposes the styles as [ANSI escape codes](https://github.com/chalk/ansi-styles).

Generally not useful, but you might need just the `.open` or `.close` escape code if you're mixing externally styled strings with your own.

```js
var chalk = require('chalk');

console.log(chalk.styles.red);
//=> {open: '\u001b[31m', close: '\u001b[39m'}

console.log(chalk.styles.red.open + 'Hello' + chalk.styles.red.close);
```

### chalk.hasColor(string)

Check whether a string [has color](https://github.com/chalk/has-ansi).

### chalk.stripColor(string)

[Strip color](https://github.com/chalk/strip-ansi) from a string.

Can be useful in combination with `.supportsColor` to strip color on externally styled text when it's not supported.

Example:

```js
var chalk = require('chalk');
var styledString = getText();

if (!chalk.supportsColor) {
	styledString = chalk.stripColor(styledString);
}
```


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue` *(on Windows the bright version is used as normal blue is illegible)*
- `magenta`
- `cyan`
- `white`
- `gray`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`


## 256-colors

Chalk does not support anything other than the base eight colors, which guarantees it will work on all terminals and systems. Some terminals, specifically `xterm` compliant ones, will support the full range of 8-bit colors. For this the lower level [ansi-256-colors](https://github.com/jbnicolai/ansi-256-colors) package can be used.


## Windows

If you're on Windows, do yourself a favor and use [`cmder`](http://bliker.github.io/cmder/) instead of `cmd.exe`.


## Related

- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles/) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color/) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# path-is-absolute [![Build Status](https://travis-ci.org/sindresorhus/path-is-absolute.svg?branch=master)](https://travis-ci.org/sindresorhus/path-is-absolute)

> Node.js 0.12 [`path.isAbsolute()`](http://nodejs.org/api/path.html#path_path_isabsolute_path) [ponyfill](https://ponyfill.com)


## Install

```
$ npm install --save path-is-absolute
```


## Usage

```js
const pathIsAbsolute = require('path-is-absolute');

// Running on Linux
pathIsAbsolute('/home/foo');
//=> true
pathIsAbsolute('C:/Users/foo');
//=> false

// Running on Windows
pathIsAbsolute('C:/Users/foo');
//=> true
pathIsAbsolute('/home/foo');
//=> false

// Running on any OS
pathIsAbsolute.posix('/home/foo');
//=> true
pathIsAbsolute.posix('C:/Users/foo');
//=> false
pathIsAbsolute.win32('C:/Users/foo');
//=> true
pathIsAbsolute.win32('/home/foo');
//=> false
```


## API

See the [`path.isAbsolute()` docs](http://nodejs.org/api/path.html#path_path_isabsolute_path).

### pathIsAbsolute(path)

### pathIsAbsolute.posix(path)

POSIX specific version.

### pathIsAbsolute.win32(path)

Windows specific version.


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# number-is-nan [![Build Status](https://travis-ci.org/sindresorhus/number-is-nan.svg?branch=master)](https://travis-ci.org/sindresorhus/number-is-nan)

> ES2015 [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN) [ponyfill](https://ponyfill.com)


## Install

```
$ npm install --save number-is-nan
```


## Usage

```js
var numberIsNan = require('number-is-nan');

numberIsNan(NaN);
//=> true

numberIsNan('unicorn');
//=> false
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# code-point-at [![Build Status](https://travis-ci.org/sindresorhus/code-point-at.svg?branch=master)](https://travis-ci.org/sindresorhus/code-point-at)

> ES2015 [`String#codePointAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt) [ponyfill](https://ponyfill.com)


## Install

```
$ npm install --save code-point-at
```


## Usage

```js
var codePointAt = require('code-point-at');

codePointAt('🐴');
//=> 128052

codePointAt('abc', 2);
//=> 99
```

## API

### codePointAt(input, [position])


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# concat-stream

Writable stream that concatenates all the data from a stream and calls a callback with the result. Use this when you want to collect all the data from a stream into a single buffer.

[![Build Status](https://travis-ci.org/maxogden/concat-stream.svg?branch=master)](https://travis-ci.org/maxogden/concat-stream)

[![NPM](https://nodei.co/npm/concat-stream.png)](https://nodei.co/npm/concat-stream/)

### description

Streams emit many buffers. If you want to collect all of the buffers, and when the stream ends concatenate all of the buffers together and receive a single buffer then this is the module for you.

Only use this if you know you can fit all of the output of your stream into a single Buffer (e.g. in RAM).

There are also `objectMode` streams that emit things other than Buffers, and you can concatenate these too. See below for details.

## Related

`concat-stream` is part of the [mississippi stream utility collection](https://github.com/maxogden/mississippi) which includes more useful stream modules similar to this one.

### examples

#### Buffers

```js
var fs = require('fs')
var concat = require('concat-stream')

var readStream = fs.createReadStream('cat.png')
var concatStream = concat(gotPicture)

readStream.on('error', handleError)
readStream.pipe(concatStream)

function gotPicture(imageBuffer) {
  // imageBuffer is all of `cat.png` as a node.js Buffer
}

function handleError(err) {
  // handle your error appropriately here, e.g.:
  console.error(err) // print the error to STDERR
  process.exit(1) // exit program with non-zero exit code
}

```

#### Arrays

```js
var write = concat(function(data) {})
write.write([1,2,3])
write.write([4,5,6])
write.end()
// data will be [1,2,3,4,5,6] in the above callback
```

#### Uint8Arrays

```js
var write = concat(function(data) {})
var a = new Uint8Array(3)
a[0] = 97; a[1] = 98; a[2] = 99
write.write(a)
write.write('!')
write.end(Buffer('!!1'))
```

See `test/` for more examples

# methods

```js
var concat = require('concat-stream')
```

## var writable = concat(opts={}, cb)

Return a `writable` stream that will fire `cb(data)` with all of the data that
was written to the stream. Data can be written to `writable` as strings,
Buffers, arrays of byte integers, and Uint8Arrays. 

By default `concat-stream` will give you back the same data type as the type of the first buffer written to the stream. Use `opts.encoding` to set what format `data` should be returned as, e.g. if you if you don't want to rely on the built-in type checking or for some other reason.

* `string` - get a string
* `buffer` - get back a Buffer
* `array` - get an array of byte integers
* `uint8array`, `u8`, `uint8` - get back a Uint8Array
* `object`, get back an array of Objects

If you don't specify an encoding, and the types can't be inferred (e.g. you write things that aren't in the list above), it will try to convert concat them into a `Buffer`.

If nothing is written to `writable` then `data` will be an empty array `[]`.

# error handling

`concat-stream` does not handle errors for you, so you must handle errors on whatever streams you pipe into `concat-stream`. This is a general rule when programming with node.js streams: always handle errors on each and every stream. Since `concat-stream` is not itself a stream it does not emit errors.

We recommend using [`end-of-stream`](https://npmjs.org/end-of-stream) or [`pump`](https://npmjs.org/pump) for writing error tolerant stream code.

# license

MIT LICENSE
# stream-to-observable [![Build Status](https://travis-ci.org/jamestalmage/stream-to-observable.svg?branch=master)](https://travis-ci.org/jamestalmage/stream-to-observable) [![Coverage Status](https://coveralls.io/repos/github/jamestalmage/stream-to-observable/badge.svg?branch=master)](https://coveralls.io/github/jamestalmage/stream-to-observable?branch=master)

> Convert Node Streams into ECMAScript-Observables

[`Observables`](https://github.com/zenparsing/es-observable) are rapidly gaining popularity. They have much in common with Streams, in that they both represent data that arrives over time. Most Observable implementations provide expressive methods for filtering and mutating incoming data. Methods like `.map()`, `.filter()`, and `.forEach` behave very similarly to their Array counterparts, so using Observables can be very intuitive.

[Learn more about Observables](#learn-about-observables)

## Install

```
$ npm install --save stream-to-observable

# You also need to install an Observable implementation (pick one):

$ npm install --save zen-observable rxjs

```


## Usage

```js
const fs = require('fs');
const split = require('split');

// You provide the Observable implmentation
const Observable = require('zen-observable')
const streamToObservable = require('stream-to-observable')(Observable);

const readStream = fs
  .createReadStream('./hello-world.txt', {encoding: 'utf8'})
  .pipe(split()); // chunks a stream into individual lines

streamToObservable(readStream)
  .filter(chunk => /hello/i.test(chunk))
  .map(chunk => chunk.toUpperCase())
  .forEach(chunk => {
    console.log(chunk); // only the lines containing "hello" - and they will be capitalized
  });
```

There are convenience imports for [`rxjs` observables](http://reactivex.io/rxjs/class/es6/Observable.js~Observable.html) and [`zen-observables`](https://github.com/zenparsing/zen-observable):

```js
const streamToObservable = require('stream-to-observable/zen'); // zen-observables
// or
const streamToObservable = require('stream-to-observable/rxjs-all'); // full rxjs implementation
// or
const streamToObservable = require('stream-to-observable/rxjs'); // minimal rxjs implementation
// you can patch the minimal rxjs.
require('rxjs/add/operator/map');
```

None of the above implementations are included as dependencies of this package, so you still need to install them yourself using `npm install`. If using the minimal `rxjs` import, be sure to see [the documentation](http://reactivex.io/rxjs/manual/installation.html) regarding patching it with additional convenience methods.


## API

### streamToObservable(stream, [options])

#### stream

Type: [`ReadableStream`](https://nodejs.org/api/stream.html#stream_class_stream_readable)

*Note:*
`stream` can technically be any [`EventEmitter`](https://nodejs.org/api/events.html#events_class_eventemitter) instance. By default the `stream-to-observable` listens to the standard Stream events (`data`, `error`, and `end`), but those are configurable via the `options` parameter. If you are using this with a standard Stream, you likely won't need the `options` parameter.

#### options

##### await

Type: `Promies`<br>

If provided, the Observable will not "complete" until `await` is resolved. If `await` is rejected, the Observable will immediately emit an `error` event and disconnect from the stream. This is mostly useful when attaching to the `stdin` or `stdout` streams of a  [`child_process`](https://nodejs.org/api/child_process.html#child_process_child_stdio). Those streams usually do not emit `error` events, even if the underlying process exits with an error. This provides a means to reject the Observable if the child process exits with an unexpected error code.

##### endEvent

Type: `String` or `false` <br>
Default: `"end"`

If you are using an `EventEmitter` or non-standard Stream, you can change which event signals that the Observable should be completed.

Setting this to `false` will avoid listening for any end events.

Setting this to `false` and providing an `await` Promise will cause the Observable to resolve immediately with the `await` Promise (the Observable will remove all it's `data` event listeners from the stream once the Promise is resolved).

##### errorEvent

Type: `String` or `false` <br>
Default: `"error"`

If you are using an `EventEmitter` or non-standard Stream, you can change which event signals that the Observable should be closed with an error.

Setting this to `false` will avoid listening for any error events.

##### dataEvent

Type: `String`<br>
Default: `"data"`

If you are using an `EventEmitter` or non-standard Stream, you can change which event causes data to be emitted to the Observable.

## Learn about Observables

 - Overview: https://github.com/zenparsing/es-observable
 - Formal Spec: https://zenparsing.github.io/es-observable/
 - [egghead.io lesson](https://egghead.io/lessons/javascript-introducing-the-observable) - Video
 - [`rxjs` observables](http://reactivex.io/rxjs/class/es6/Observable.js~Observable.html) - Observables Implementation
 - [`zen-observables`](https://github.com/zenparsing/zen-observable) - Observables Implementation

## Transform Streams

`data` events on the stream will be emitted as events in the Observable. Since most native streams emit `chunks` of binary data, you will likely want to use a `TransformStream` to convert those chunks of binary data into an object stream. [`split`](https://github.com/dominictarr/split) is just one popular TransformStream that splits streams into individual lines of text.

## Caveats

It is important Note that using this module disables back-pressure controls on the stream. As such it should not be used where back-pressure throttling is required (i.e. high volume web servers). It still has value for larger projects, as it can make unit testing streams much cleaner.

## License

MIT © [James Talmage](http://github.com/jamestalmage)
# elegant-spinner [![Build Status](https://travis-ci.org/sindresorhus/elegant-spinner.svg?branch=master)](https://travis-ci.org/sindresorhus/elegant-spinner)

> Elegant spinner for interactive CLI apps

<img width="173" src="screenshot.gif">


## Install

```
$ npm install --save elegant-spinner
```


## Usage

```js
var elegantSpinner = require('elegant-spinner');
var logUpdate = require('log-update');
var frame = elegantSpinner();

setInterval(function () {
	logUpdate(frame());
}, 50);
```


## Relevant

- [log-update](https://github.com/sindresorhus/log-update) - Log by overwriting the previous output in the terminal. Useful for rendering progress bars, animations, etc.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# repeating [![Build Status](https://travis-ci.org/sindresorhus/repeating.svg?branch=master)](https://travis-ci.org/sindresorhus/repeating)

> Repeat a string - fast


## Install

```
$ npm install --save repeating
```


## Usage

```js
const repeating = require('repeating');

repeating('unicorn ', 100);
//=> 'unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn unicorn '
```


## Related

- [repeating-cli](https://github.com/sindresorhus/repeating-cli) - CLI for this module


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# is-installed-globally [![Build Status](https://travis-ci.org/sindresorhus/is-installed-globally.svg?branch=master)](https://travis-ci.org/sindresorhus/is-installed-globally)

> Check if your package was installed globally

Can be useful if your CLI needs different behavior when installed globally and locally.


## Install

```
$ npm install is-installed-globally
```


## Usage

```js
const isInstalledGlobally = require('is-installed-globally');

// With `npm install your-package`
console.log(isInstalledGlobally);
//=> false

// With `npm install --global your-package`
console.log(isInstalledGlobally);
//=> true
```


## Related

- [import-global](https://github.com/sindresorhus/import-global) - Import a globally installed module
- [resolve-global](https://github.com/sindresorhus/resolve-global) - Resolve the path of a globally installed module
- [global-dirs](https://github.com/sindresorhus/global-dirs) - Get the directory of globally installed packages and binaries


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# restore-cursor

> Gracefully restore the CLI cursor on exit

Prevent the cursor you've hidden interactively to remain hidden if the process crashes.


## Install

```sh
$ npm install --save restore-cursor
```


## Usage

```js
var restoreCursor = require('restore-cursor');
restoreCursor();
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# listr-verbose-renderer [![Build Status](https://travis-ci.org/SamVerschueren/listr-verbose-renderer.svg?branch=master)](https://travis-ci.org/SamVerschueren/listr-verbose-renderer)

> [Listr](https://github.com/SamVerschueren/listr) verbose renderer

<img src="screenshot.gif" />


## Install

```
$ npm install --save listr-verbose-renderer
```


## Usage

```js
const VerboseRenderer = require('listr-verbose-renderer');
const Listr = require('listr');

const list = new Listr([
	{
		title: 'foo',
		task: () => Promise.resolve('bar')
	}
], {
	renderer: VerboseRenderer
});

list.run();
```

> Note: This renderer supports non-TTY environments.


## Options

These options should be provided in the [Listr](https://github.com/SamVerschueren/listr) options object.

### dateFormat

Type: `string`<br>
Default: `HH:mm:ss`

Format of the rendered timestamp. Use the [date-fns string format](https://date-fns.org/docs/format).


## Related

- [listr](https://github.com/SamVerschueren/listr) - Terminal task list
- [listr-update-renderer](https://github.com/SamVerschueren/listr-update-renderer) - Listr update renderer
- [listr-silent-renderer](https://github.com/SamVerschueren/listr-silent-renderer) - Suppress Listr rendering output


## License

MIT © [Sam Verschueren](https://github.com/SamVerschueren)


## Changelog

#### 0.4.1 - *(09/04/17)*
- don't output on DATA events
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install --save supports-color
```


## Usage

```js
var supportsColor = require('supports-color');

if (supportsColor) {
	console.log('Terminal supports color');
}
```

It obeys the `--color` and `--no-color` CLI flags.

For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
<h1 align="center">
	<br>
	<br>
	<img width="360" src="https://cdn.rawgit.com/chalk/chalk/19935d6484811c5e468817f846b7b3d417d7bf4a/logo.svg" alt="chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Build Status](https://travis-ci.org/chalk/chalk.svg?branch=master)](https://travis-ci.org/chalk/chalk)
[![Coverage Status](https://coveralls.io/repos/chalk/chalk/badge.svg?branch=master)](https://coveralls.io/r/chalk/chalk?branch=master)
[![](http://img.shields.io/badge/unicorn-approved-ff69b4.svg)](https://www.youtube.com/watch?v=9auOCbH5Ns4)


[colors.js](https://github.com/Marak/colors.js) used to be the most popular string styling module, but it has serious deficiencies like extending `String.prototype` which causes all kinds of [problems](https://github.com/yeoman/yo/issues/68). Although there are other ones, they either do too much or not enough.

**Chalk is a clean and focused alternative.**

![](https://github.com/chalk/ansi-styles/raw/master/screenshot.png)


## Why

- Highly performant
- Doesn't extend `String.prototype`
- Expressive API
- Ability to nest styles
- Clean and focused
- Auto-detects color support
- Actively maintained
- [Used by ~4500 modules](https://www.npmjs.com/browse/depended/chalk) as of July 15, 2015


## Install

```
$ npm install --save chalk
```


## Usage

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
var chalk = require('chalk');

// style a string
chalk.blue('Hello world!');

// combine styled and normal strings
chalk.blue('Hello') + 'World' + chalk.red('!');

// compose multiple styles using the chainable API
chalk.blue.bgRed.bold('Hello world!');

// pass in multiple arguments
chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz');

// nest styles
chalk.red('Hello', chalk.underline.bgBlue('world') + '!');

// nest styles of the same type even (color, underline, background)
chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
);
```

Easily define your own themes.

```js
var chalk = require('chalk');
var error = chalk.bold.red;
console.log(error('Error!'));
```

Take advantage of console.log [string substitution](http://nodejs.org/docs/latest/api/console.html#console_console_log_data).

```js
var name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> Hello Sindre
```


## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `Chalk.red.yellow.green` is equivalent to `Chalk.green`.

Multiple arguments will be separated by space.

### chalk.enabled

Color support is automatically detected, but you can override it by setting the `enabled` property. You should however only do this in your own code as it applies globally to all chalk consumers.

If you need to change this in a reusable module create a new instance:

```js
var ctx = new chalk.constructor({enabled: false});
```

### chalk.supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.

### chalk.styles

Exposes the styles as [ANSI escape codes](https://github.com/chalk/ansi-styles).

Generally not useful, but you might need just the `.open` or `.close` escape code if you're mixing externally styled strings with your own.

```js
var chalk = require('chalk');

console.log(chalk.styles.red);
//=> {open: '\u001b[31m', close: '\u001b[39m'}

console.log(chalk.styles.red.open + 'Hello' + chalk.styles.red.close);
```

### chalk.hasColor(string)

Check whether a string [has color](https://github.com/chalk/has-ansi).

### chalk.stripColor(string)

[Strip color](https://github.com/chalk/strip-ansi) from a string.

Can be useful in combination with `.supportsColor` to strip color on externally styled text when it's not supported.

Example:

```js
var chalk = require('chalk');
var styledString = getText();

if (!chalk.supportsColor) {
	styledString = chalk.stripColor(styledString);
}
```


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue` *(on Windows the bright version is used as normal blue is illegible)*
- `magenta`
- `cyan`
- `white`
- `gray`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`


## 256-colors

Chalk does not support anything other than the base eight colors, which guarantees it will work on all terminals and systems. Some terminals, specifically `xterm` compliant ones, will support the full range of 8-bit colors. For this the lower level [ansi-256-colors](https://github.com/jbnicolai/ansi-256-colors) package can be used.


## Windows

If you're on Windows, do yourself a favor and use [`cmder`](http://bliker.github.io/cmder/) instead of `cmd.exe`.


## Related

- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles/) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color/) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# mkdirp

Like `mkdir -p`, but in node.js!

[![build status](https://secure.travis-ci.org/substack/node-mkdirp.png)](http://travis-ci.org/substack/node-mkdirp)

# example

## pow.js

```js
var mkdirp = require('mkdirp');
    
mkdirp('/tmp/foo/bar/baz', function (err) {
    if (err) console.error(err)
    else console.log('pow!')
});
```

Output

```
pow!
```

And now /tmp/foo/bar/baz exists, huzzah!

# methods

```js
var mkdirp = require('mkdirp');
```

## mkdirp(dir, opts, cb)

Create a new directory and any necessary subdirectories at `dir` with octal
permission string `opts.mode`. If `opts` is a non-object, it will be treated as
the `opts.mode`.

If `opts.mode` isn't specified, it defaults to `0777 & (~process.umask())`.

`cb(err, made)` fires with the error or the first directory `made`
that had to be created, if any.

You can optionally pass in an alternate `fs` implementation by passing in
`opts.fs`. Your implementation should have `opts.fs.mkdir(path, mode, cb)` and
`opts.fs.stat(path, cb)`.

## mkdirp.sync(dir, opts)

Synchronously create a new directory and any necessary subdirectories at `dir`
with octal permission string `opts.mode`. If `opts` is a non-object, it will be
treated as the `opts.mode`.

If `opts.mode` isn't specified, it defaults to `0777 & (~process.umask())`.

Returns the first directory that had to be created, if any.

You can optionally pass in an alternate `fs` implementation by passing in
`opts.fs`. Your implementation should have `opts.fs.mkdirSync(path, mode)` and
`opts.fs.statSync(path)`.

# usage

This package also ships with a `mkdirp` command.

```
usage: mkdirp [DIR1,DIR2..] {OPTIONS}

  Create each supplied directory including any necessary parent directories that
  don't yet exist.
  
  If the directory already exists, do nothing.

OPTIONS are:

  -m, --mode   If a directory needs to be created, set the mode as an octal
               permission string.

```

# install

With [npm](http://npmjs.org) do:

```
npm install mkdirp
```

to get the library, or

```
npm install -g mkdirp
```

to get the command.

# license

MIT
# minimist

parse argument options

This module is the guts of optimist's argument parser without all the
fanciful decoration.

[![browser support](https://ci.testling.com/substack/minimist.png)](http://ci.testling.com/substack/minimist)

[![build status](https://secure.travis-ci.org/substack/minimist.png)](http://travis-ci.org/substack/minimist)

# example

``` js
var argv = require('minimist')(process.argv.slice(2));
console.dir(argv);
```

```
$ node example/parse.js -a beep -b boop
{ _: [], a: 'beep', b: 'boop' }
```

```
$ node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
{ _: [ 'foo', 'bar', 'baz' ],
  x: 3,
  y: 4,
  n: 5,
  a: true,
  b: true,
  c: true,
  beep: 'boop' }
```

# methods

``` js
var parseArgs = require('minimist')
```

## var argv = parseArgs(args, opts={})

Return an argument object `argv` populated with the array arguments from `args`.

`argv._` contains all the arguments that didn't have an option associated with
them.

Numeric-looking arguments will be returned as numbers unless `opts.string` or
`opts.boolean` is set for that argument name.

Any arguments after `'--'` will not be parsed and will end up in `argv._`.

options can be:

* `opts.string` - a string or array of strings argument names to always treat as
strings
* `opts.boolean` - a string or array of strings to always treat as booleans
* `opts.alias` - an object mapping string names to strings or arrays of string
argument names to use as aliases
* `opts.default` - an object mapping string argument names to default values

# install

With [npm](https://npmjs.org) do:

```
npm install minimist
```

# license

MIT
# path-key [![Build Status](https://travis-ci.org/sindresorhus/path-key.svg?branch=master)](https://travis-ci.org/sindresorhus/path-key)

> Get the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) environment variable key cross-platform

It's usually `PATH`, but on Windows it can be any casing like `Path`...


## Install

```
$ npm install --save path-key
```


## Usage

```js
const pathKey = require('path-key');

const key = pathKey();
//=> 'PATH'

const PATH = process.env[key];
//=> '/usr/local/bin:/usr/bin:/bin'
```


## API

### pathKey([options])

#### options

##### env

Type: `Object`<br>
Default: [`process.env`](https://nodejs.org/api/process.html#process_process_env)

Use a custom environment variables object.

#### platform

Type: `string`<br>
Default: [`process.platform`](https://nodejs.org/api/process.html#process_process_platform)

Get the PATH key for a specific platform.


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# os-tmpdir [![Build Status](https://travis-ci.org/sindresorhus/os-tmpdir.svg?branch=master)](https://travis-ci.org/sindresorhus/os-tmpdir)

> Node.js [`os.tmpdir()`](https://nodejs.org/api/os.html#os_os_tmpdir) [ponyfill](https://ponyfill.com)

Use this instead of `require('os').tmpdir()` to get a consistent behavior on different Node.js versions (even 0.8).


## Install

```
$ npm install --save os-tmpdir
```


## Usage

```js
const osTmpdir = require('os-tmpdir');

osTmpdir();
//=> '/var/folders/m3/5574nnhn0yj488ccryqr7tc80000gn/T'
```


## API

See the [`os.tmpdir()` docs](https://nodejs.org/api/os.html#os_os_tmpdir).


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# ansi-styles [![Build Status](https://travis-ci.org/chalk/ansi-styles.svg?branch=master)](https://travis-ci.org/chalk/ansi-styles)

> [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles) for styling strings in the terminal

You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

![](screenshot.png)


## Install

```
$ npm install --save ansi-styles
```


## Usage

```js
var ansi = require('ansi-styles');

console.log(ansi.green.open + 'Hello world!' + ansi.green.close);
```


## API

Each style has an `open` and `close` property.


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `gray`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`


## Advanced usage

By default you get a map of styles, but the styles are also available as groups. They are non-enumerable so they don't show up unless you access them explicitly. This makes it easier to expose only a subset in a higher-level module.

- `ansi.modifiers`
- `ansi.colors`
- `ansi.bgColors`


###### Example

```js
console.log(ansi.colors.green.open);
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# pify [![Build Status](https://travis-ci.org/sindresorhus/pify.svg?branch=master)](https://travis-ci.org/sindresorhus/pify)

> Promisify a callback-style function


## Install

```
$ npm install --save pify
```


## Usage

```js
const fs = require('fs');
const pify = require('pify');

// promisify a single function

pify(fs.readFile)('package.json', 'utf8').then(data => {
	console.log(JSON.parse(data).name);
	//=> 'pify'
});

// or promisify all methods in a module

pify(fs).readFile('package.json', 'utf8').then(data => {
	console.log(JSON.parse(data).name);
	//=> 'pify'
});
```


## API

### pify(input, [promiseModule], [options])

Returns a promise wrapped version of the supplied function or module.

#### input

Type: `function`, `object`

Callback-style function or module whose methods you want to promisify.

#### promiseModule

Type: `function`

Custom promise module to use instead of the native one.

Check out [`pinkie-promise`](https://github.com/floatdrop/pinkie-promise) if you need a tiny promise polyfill.

#### options

##### multiArgs

Type: `boolean`  
Default: `false`

By default, the promisified function will only return the second argument from the callback, which works fine for most APIs. This option can be useful for modules like `request` that return multiple arguments. Turning this on will make it return an array of all arguments from the callback, excluding the error argument, instead of just the second argument.

```js
const request = require('request');
const pify = require('pify');

pify(request, {multiArgs: true})('https://sindresorhus.com').then(result => {
	const [httpResponse, body] = result;
});
```

##### include

Type: `array` of (`string`|`regex`)

Methods in a module to promisify. Remaining methods will be left untouched.

##### exclude

Type: `array` of (`string`|`regex`)  
Default: `[/.+Sync$/]`

Methods in a module **not** to promisify. Methods with names ending with `'Sync'` are excluded by default.

##### excludeMain

Type: `boolean`  
Default: `false`

By default, if given module is a function itself, this function will be promisified. Turn this option on if you want to promisify only methods of the module.

```js
const pify = require('pify');

function fn() {
	return true;
}

fn.method = (data, callback) => {
	setImmediate(() => {
		callback(data, null);
	});
};

// promisify methods but not fn()
const promiseFn = pify(fn, {excludeMain: true});

if (promiseFn()) {
	promiseFn.method('hi').then(data => {
		console.log(data);
	});
}
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# indent-string [![Build Status](https://travis-ci.org/sindresorhus/indent-string.svg?branch=master)](https://travis-ci.org/sindresorhus/indent-string)

> Indent each line in a string


## Install

```
$ npm install --save indent-string
```


## Usage

```js
var indentString = require('indent-string');

indentString('Unicorns\nRainbows', '♥', 4);
//=> ♥♥♥♥Unicorns
//=> ♥♥♥♥Rainbows
```


## API

### indentString(string, indent, count)

#### string

**Required**  
Type: `string`

The string you want to indent.

#### indent

**Required**  
Type: `string`

The string to use for the indent.

#### count

Type: `number`  
Default: `1`

How many times you want `indent` repeated.


## Related

- [indent-string-cli](https://github.com/sindresorhus/indent-string-cli) - CLI for this module
- [strip-indent](https://github.com/sindresorhus/strip-indent) - Strip leading whitespace from every line in a string


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# symbol-observable [![Build Status](https://travis-ci.org/blesh/symbol-observable.svg?branch=master)](https://travis-ci.org/blesh/symbol-observable)

> [Symbol.observable](https://github.com/zenparsing/es-observable) ponyfill


## Install

```
$ npm install --save symbol-observable
```


## Usage

```js
const symbolObservable = require('symbol-observable');

console.log(symbolObservable);
//=> Symbol(observable)
```


## Related

- [is-observable](https://github.com/sindresorhus/is-observable) - Check if a value is an Observable
- [observable-to-promise](https://github.com/sindresorhus/observable-to-promise) - Convert an Observable to a Promise


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# global-dirs [![Build Status](https://travis-ci.org/sindresorhus/global-dirs.svg?branch=master)](https://travis-ci.org/sindresorhus/global-dirs)

> Get the directory of globally installed packages and binaries

Uses the same resolution logic as `npm` and `yarn`.


## Install

```
$ npm install global-dirs
```


## Usage

```js
const globalDirs = require('global-dirs');

console.log(globalDirs.npm.prefix);
//=> '/usr/local'

console.log(globalDirs.npm.packages);
//=> '/usr/local/lib/node_modules'

console.log(globalDirs.npm.binaries);
//=> '/usr/local/bin'

console.log(globalDirs.yarn.packages);
//=> '/Users/sindresorhus/.config/yarn/global/node_modules'
```


## API

### globalDirs

#### npm
#### yarn

##### packages

Directory with globally installed packages.

Equivalent to `npm root --global`.

##### binaries

Directory with globally installed binaries.

Equivalent to `npm bin --global`.

##### prefix

Directory with directories for packages and binaries. You probably want either of the above.

Equivalent to `npm prefix --global`.


## Related

- [import-global](https://github.com/sindresorhus/import-global) - Import a globally installed module
- [resolve-global](https://github.com/sindresorhus/resolve-global) - Resolve the path of a globally installed module
- [is-installed-globally](https://github.com/sindresorhus/is-installed-globally) - Check if your package was installed globally


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# has-flag [![Build Status](https://travis-ci.org/sindresorhus/has-flag.svg?branch=master)](https://travis-ci.org/sindresorhus/has-flag)

> Check if [`argv`](https://nodejs.org/docs/latest/api/process.html#process_process_argv) has a specific flag

Correctly stops looking after an `--` argument terminator.


## Install

```
$ npm install has-flag
```


## Usage

```js
// foo.js
const hasFlag = require('has-flag');

hasFlag('unicorn');
//=> true

hasFlag('--unicorn');
//=> true

hasFlag('f');
//=> true

hasFlag('-f');
//=> true

hasFlag('foo=bar');
//=> true

hasFlag('foo');
//=> false

hasFlag('rainbow');
//=> false
```

```
$ node foo.js -f --unicorn --foo=bar -- --rainbow
```


## API

### hasFlag(flag, [argv])

Returns a boolean for whether the flag exists.

#### flag

Type: `string`

CLI flag to look for. The `--` prefix is optional.

#### argv

Type: `string[]`<br>
Default: `process.argv`

CLI arguments.


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# is-path-inside [![Build Status](https://travis-ci.org/sindresorhus/is-path-inside.svg?branch=master)](https://travis-ci.org/sindresorhus/is-path-inside)

> Check if a path is inside another path


## Install

```
$ npm install --save is-path-inside
```


## Usage

```js
var isPathInside = require('is-path-inside');

isPathInside('a/b/c', 'a/b');
//=> true

isPathInside('a/b/c', 'x/y');
//=> false

isPathInside('a/b/c', 'a/b/c');
//=> false

isPathInside('/Users/sindresorhus/dev/unicorn', '/Users/sindresorhus');
//=> true
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# listr

[![Build Status Linux](https://travis-ci.org/SamVerschueren/listr.svg?branch=master)](https://travis-ci.org/SamVerschueren/listr) [![Build status Windows](https://ci.appveyor.com/api/projects/status/y8vhpwsb98b8o4cm?svg=true)](https://ci.appveyor.com/project/SamVerschueren/listr) [![Coverage Status](https://coveralls.io/repos/SamVerschueren/listr/badge.svg?branch=master&service=github)](https://coveralls.io/github/SamVerschueren/listr?branch=master)

> Terminal task list

<img src="media/screenshot.gif">

## Install

```
$ npm install --save listr
```


## Usage

```js
const execa = require('execa');
const Listr = require('listr');

const tasks = new Listr([
	{
		title: 'Git',
		task: () => {
			return new Listr([
				{
					title: 'Checking git status',
					task: () => execa.stdout('git', ['status', '--porcelain']).then(result => {
						if (result !== '') {
							throw new Error('Unclean working tree. Commit or stash changes first.');
						}
					})
				},
				{
					title: 'Checking remote history',
					task: () => execa.stdout('git', ['rev-list', '--count', '--left-only', '@{u}...HEAD']).then(result => {
						if (result !== '0') {
							throw new Error('Remote history differ. Please pull changes.');
						}
					})
				}
			], {concurrent: true});
		}
	},
	{
		title: 'Install package dependencies with Yarn',
		task: (ctx, task) => execa('yarn')
			.catch(() => {
				ctx.yarn === false;

				task.skip('Yarn not available, install it via `npm install -g yarn`');
			})
	},
	{
		title: 'Install package dependencies with npm',
		enabled: ctx => ctx.yarn === false,
		task: () => execa('npm', ['install'])
	},
	{
		title: 'Run tests',
		task: () => execa('npm', ['test'])
	},
	{
		title: 'Publish package',
		task: () => execa('npm', ['publish'])
	}
]);

tasks.run().catch(err => {
	console.error(err);
});
```


## Task

A `task` can return different values. If a `task` returns, it means the task was completed successfully. If a task throws an error, the task failed.

```js
const tasks = new Listr([
	{
		title: 'Success',
		task: () => 'Foo'
	},
	{
		title: 'Failure',
		task: () => {
			throw new Error('Bar')
		}
	}
]);
```


### Promises

A `task` can also be async by returning a `Promise`. If the promise resolves, the task completed successfully, it it rejects, the task failed.

```js
const tasks = new Listr([
	{
		title: 'Success',
		task: () => Promise.resolve('Foo')
	},
	{
		title: 'Failure',
		task: () => Promise.reject(new Error('Bar'))
	}
]);
```

> Tip: Always reject a promise with some kind of `Error` object.

### Observable

<img src="media/observable.gif" width="250" align="right">

A `task` can also return an `Observable`. The thing about observables is that it can emit multiple values and can be used to show the output of the
task. Please note that only the last line of the output is rendered.

```js
const tasks = new Listr([
	{
		title: 'Success',
		task: () => {
			return new Observable(observer => {
				observer.next('Foo');

				setTimeout(() => {
					observer.next('Bar');
				}, 2000);

				setTimeout(() => {
					observer.complete();
				}, 4000);
			});
		}
	},
	{
		title: 'Failure',
		task: () => Promise.reject(new Error('Bar'))
	}
]);
```

### Streams

It's also possible to return a `stream`. The stream will be converted to an `Observable` and handled as such.


### Skipping tasks

<img src="media/skipped.png" width="250" align="right">

Optionally specify a `skip` function to determine whether a task can be skipped.

- If the `skip` function returns a truthy value or a `Promise` that resolves to a truthy value then the task will be skipped.
- If the returned value is a string it will be displayed as the reason for skipping the task.
- If the `skip` function returns a falsey value or a `Promise` that resolves to a falsey value then the task will be executed as normal.
- If the `skip` function throws or returns a `Promise` that rejects, the task (and the whole build) will fail.

```js
const tasks = new Listr([
	{
		title: 'Task 1',
		task: () => Promise.resolve('Foo')
	},
	{
		title: 'Can be skipped',
		skip: () => {
			if (Math.random() > 0.5) {
				return 'Reason for skipping';
			}
		},
		task: () => 'Bar'
	},
	{
		title: 'Task 3',
		task: () => Promise.resolve('Bar')
	}
]);
```

> Tip: You can still skip a task while already executing the `task` function with the [task object](#task-object).

## Enabling tasks

By default, every task is enabled which means that every task will be executed. However, it's also possible to provide an `enabled` function that returns wheter the task should be executed or not.

```js
const tasks = new Listr([
	{
		title: 'Install package dependencies with Yarn',
		task: (ctx, task) => execa('yarn')
			.catch(() => {
				ctx.yarn === false;

				task.skip('Yarn not available, install it via `npm install -g yarn`');
			})
	},
	{
		title: 'Install package dependencies with npm',
		enabled: ctx => ctx.yarn === false,
		task: () => execa('npm', ['install'])
	}
]);
```

In the above example, we try to run `yarn` first, if that fails we will fall back to `npm`. However, at first only the Yarn task will be visible. Because we set the `yarn` flag of the [context](https://github.com/SamVerschueren/listr#context) object to `false`, the second task will automatically be enabled and will be executed.

> Note: This does not work in combination with [concurrent](https://github.com/SamVerschueren/listr#concurrent) tasks.


## Context

A context object is being passed as argument into every `skip` and `task` function. This allows you to create composable tasks and change the behaviour of your task depending on previous results.

```js
const tasks = new Listr([
	{
		title: 'Task 1',
		skip: ctx => ctx.foo === 'bar',
		task: () => Promise.resolve('Foo')
	},
	{
		title: 'Can be skipped',
		skip: () => {
			if (Math.random() > 0.5) {
				return 'Reason for skipping';
			}
		},
		task: ctx => {
			ctx.unicorn = 'rainbow';
		}
	},
	{
		title: 'Task 3',
		task: ctx => Promise.resolve(`${ctx.foo} ${ctx.bar}`)
	}
]);

tasks.run({
	foo: 'bar'
}).then(ctx => {
	console.log(ctx);
	//=> {foo: 'bar', unicorn: 'rainbow'}
});
```


## Task object

A special task object is being passed as second argument into the `task` function. This task object lets you change the title while running your task, you can skip it depending on some results or you can update the task's output.

```js
const tasks = new Listr([
	{
		title: 'Install package dependencies with Yarn',
		task: (ctx, task) => execa('yarn')
			.catch(() => {
				ctx.yarn = false;

				task.title = `${task.title} (or not)`;
				task.skip('Yarn not available');
			})
	},
	{
		title: 'Install package dependencies with npm',
		skip: ctx => ctx.yarn !== false && 'Dependencies already installed with Yarn'
		task: (ctx, task) => {
			task.output = 'Installing dependencies...';

			return execa('npm', ['install'])
		}
	}
]);

tasks.run();
```


## Custom renderers

It's possible to write custom renderers for Listr. A renderer is an ES6 class that accepts the tasks that it should renderer, and the Listr options object. It has two methods, the `render` method which is called when it should start rendering, and the `end` method. The `end` method is called all the tasks are completed or if a task failed. If a task failed, the error object is passed in via an argument.

```js
class CustomRenderer {

	constructor(tasks, options) { }

	static get nonTTY() {
		return false;
	}

	render() { }

	end(err) { }
}

module.exports = CustomRenderer;
```

> Note: A renderer is not passed through to the subtasks, only to the main task. It is up to you to handle that case.

The `nonTTY` property returns a boolean indicating if the renderer supports non-TTY environments. The default for this property is `false` if you do not implement it.

### Observables

Every task is an observable. The task emits three different events and every event is an object with a `type` property.

1. The state of the task has changed (`STATE`).
2. The task outputted data (`DATA`).
3. The task returns a subtask list (`SUBTASKS`).
4. The task's title changed (`TITLE`).
5. The task became enabled or disabled (`ENABLED`).

This allows you to flexibly build up your UI. Let's render every task that starts executing.

```js
class CustomRenderer {

	constructor(tasks, options) {
		this._tasks = tasks;
		this._options = Object.assign({}, options);
	}

	static get nonTTY() {
		return true;
	}

	render() {
		for (const task of this._tasks) {
			task.subscribe(event => {
				if (event.type === 'STATE' && task.isPending()) {
					console.log(`${task.title} [started]`);
				}
			});
		}
	}

	end(err) { }
}

module.exports = CustomRenderer;
```

If you want more complex examples, take a look at the [update](https://github.com/SamVerschueren/listr-update-renderer) and [verbose](https://github.com/SamVerschueren/listr-verbose-renderer) renderers.


## API

### Listr([tasks], [options])

#### tasks

Type: `object[]`

List of tasks.

##### title

Type: `string`

Title of the task.

##### task

Type: `Function`

Task function.

##### skip

Type: `Function`

Skip function. Read more about [skipping tasks](#skipping-tasks).

#### options

Any renderer specific options.

##### concurrent

Type: `boolean` `number`<br>
Default: `false`

Set to `true` if you want to run tasks in parallel, set to a number to control the concurrency. By default it runs tasks sequentially.

##### exitOnError

Type: `boolean`<br>
Default: `true`

Set to `false` if you don't want to stop the execution of other tasks when one or more tasks fail.

##### renderer

Type: `string` `object`<br>
Default: `default`<br>
Options: `default` `verbose` `silent`

Renderer that should be used. You can either pass in the name of the known renderer, or a class of a custom renderer.

##### nonTTYRenderer

Type: `string` `object`<br>
Default: `verbose`

The renderer that should be used if the main renderer does not support TTY environments. You can either pass in the name of the renderer, or a class of a custom renderer.

### Instance

#### add(task)

Returns the instance.

##### task

Type: `object` `object[]`

Task object or multiple task objects.

#### run([context])

Start executing the tasks. Returns a `Promise` for the context object.

##### context

Type: `object`<br>
Default: `Object.create(null)`

Initial context object.


## Related

- [ora](https://github.com/sindresorhus/ora) - Elegant terminal spinner
- [cli-spinners](https://github.com/sindresorhus/cli-spinners) - Spinners for use in the terminal


## License

MIT © [Sam Verschueren](https://github.com/SamVerschueren)
# supports-color [![Build Status](https://travis-ci.org/chalk/supports-color.svg?branch=master)](https://travis-ci.org/chalk/supports-color)

> Detect whether a terminal supports color


## Install

```
$ npm install --save supports-color
```


## Usage

```js
var supportsColor = require('supports-color');

if (supportsColor) {
	console.log('Terminal supports color');
}
```

It obeys the `--color` and `--no-color` CLI flags.

For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.


## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
<h1 align="center">
	<br>
	<br>
	<img width="360" src="https://cdn.rawgit.com/chalk/chalk/19935d6484811c5e468817f846b7b3d417d7bf4a/logo.svg" alt="chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Build Status](https://travis-ci.org/chalk/chalk.svg?branch=master)](https://travis-ci.org/chalk/chalk)
[![Coverage Status](https://coveralls.io/repos/chalk/chalk/badge.svg?branch=master)](https://coveralls.io/r/chalk/chalk?branch=master)
[![](http://img.shields.io/badge/unicorn-approved-ff69b4.svg)](https://www.youtube.com/watch?v=9auOCbH5Ns4)


[colors.js](https://github.com/Marak/colors.js) used to be the most popular string styling module, but it has serious deficiencies like extending `String.prototype` which causes all kinds of [problems](https://github.com/yeoman/yo/issues/68). Although there are other ones, they either do too much or not enough.

**Chalk is a clean and focused alternative.**

![](https://github.com/chalk/ansi-styles/raw/master/screenshot.png)


## Why

- Highly performant
- Doesn't extend `String.prototype`
- Expressive API
- Ability to nest styles
- Clean and focused
- Auto-detects color support
- Actively maintained
- [Used by ~4500 modules](https://www.npmjs.com/browse/depended/chalk) as of July 15, 2015


## Install

```
$ npm install --save chalk
```


## Usage

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
var chalk = require('chalk');

// style a string
chalk.blue('Hello world!');

// combine styled and normal strings
chalk.blue('Hello') + 'World' + chalk.red('!');

// compose multiple styles using the chainable API
chalk.blue.bgRed.bold('Hello world!');

// pass in multiple arguments
chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz');

// nest styles
chalk.red('Hello', chalk.underline.bgBlue('world') + '!');

// nest styles of the same type even (color, underline, background)
chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
);
```

Easily define your own themes.

```js
var chalk = require('chalk');
var error = chalk.bold.red;
console.log(error('Error!'));
```

Take advantage of console.log [string substitution](http://nodejs.org/docs/latest/api/console.html#console_console_log_data).

```js
var name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> Hello Sindre
```


## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `Chalk.red.yellow.green` is equivalent to `Chalk.green`.

Multiple arguments will be separated by space.

### chalk.enabled

Color support is automatically detected, but you can override it by setting the `enabled` property. You should however only do this in your own code as it applies globally to all chalk consumers.

If you need to change this in a reusable module create a new instance:

```js
var ctx = new chalk.constructor({enabled: false});
```

### chalk.supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, add an environment variable `FORCE_COLOR` with any value to force color. Trumps `--no-color`.

### chalk.styles

Exposes the styles as [ANSI escape codes](https://github.com/chalk/ansi-styles).

Generally not useful, but you might need just the `.open` or `.close` escape code if you're mixing externally styled strings with your own.

```js
var chalk = require('chalk');

console.log(chalk.styles.red);
//=> {open: '\u001b[31m', close: '\u001b[39m'}

console.log(chalk.styles.red.open + 'Hello' + chalk.styles.red.close);
```

### chalk.hasColor(string)

Check whether a string [has color](https://github.com/chalk/has-ansi).

### chalk.stripColor(string)

[Strip color](https://github.com/chalk/strip-ansi) from a string.

Can be useful in combination with `.supportsColor` to strip color on externally styled text when it's not supported.

Example:

```js
var chalk = require('chalk');
var styledString = getText();

if (!chalk.supportsColor) {
	styledString = chalk.stripColor(styledString);
}
```


## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(not widely supported)*
- `underline`
- `inverse`
- `hidden`
- `strikethrough` *(not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue` *(on Windows the bright version is used as normal blue is illegible)*
- `magenta`
- `cyan`
- `white`
- `gray`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`


## 256-colors

Chalk does not support anything other than the base eight colors, which guarantees it will work on all terminals and systems. Some terminals, specifically `xterm` compliant ones, will support the full range of 8-bit colors. For this the lower level [ansi-256-colors](https://github.com/jbnicolai/ansi-256-colors) package can be used.


## Windows

If you're on Windows, do yourself a favor and use [`cmder`](http://bliker.github.io/cmder/) instead of `cmd.exe`.


## Related

- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles/) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color/) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# log-symbols [![Build Status](https://travis-ci.org/sindresorhus/log-symbols.svg?branch=master)](https://travis-ci.org/sindresorhus/log-symbols)

> Colored symbols for various log levels

Includes fallbacks for Windows CMD which only supports a [limited character set](http://en.wikipedia.org/wiki/Code_page_437).

![](screenshot.png)


## Install

```sh
$ npm install --save log-symbols
```


## Usage

```js
var logSymbols = require('log-symbols');

console.log(logSymbols.success, 'finished successfully!');
// On real OSes:  ✔ finished successfully!
// On Windows:    √ finished successfully!
```

## API

### logSymbols

#### info
#### success
#### warning
#### error


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# object-assign [![Build Status](https://travis-ci.org/sindresorhus/object-assign.svg?branch=master)](https://travis-ci.org/sindresorhus/object-assign)

> ES2015 [`Object.assign()`](http://www.2ality.com/2014/01/object-assign.html) [ponyfill](https://ponyfill.com)


## Use the built-in

Node.js 4 and up, as well as every evergreen browser (Chrome, Edge, Firefox, Opera, Safari),
support `Object.assign()` :tada:. If you target only those environments, then by all
means, use `Object.assign()` instead of this package.


## Install

```
$ npm install --save object-assign
```


## Usage

```js
const objectAssign = require('object-assign');

objectAssign({foo: 0}, {bar: 1});
//=> {foo: 0, bar: 1}

// multiple sources
objectAssign({foo: 0}, {bar: 1}, {baz: 2});
//=> {foo: 0, bar: 1, baz: 2}

// overwrites equal keys
objectAssign({foo: 0}, {foo: 1}, {foo: 2});
//=> {foo: 2}

// ignores null and undefined sources
objectAssign({foo: 0}, null, {bar: 1}, undefined);
//=> {foo: 0, bar: 1}
```


## API

### objectAssign(target, [source, ...])

Assigns enumerable own properties of `source` objects to the `target` object and returns the `target` object. Additional `source` objects will overwrite previous ones.


## Resources

- [ES2015 spec - Object.assign](https://people.mozilla.org/~jorendorff/es6-draft.html#sec-object.assign)


## Related

- [deep-assign](https://github.com/sindresorhus/deep-assign) - Recursive `Object.assign()`


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# is-stream [![Build Status](https://travis-ci.org/sindresorhus/is-stream.svg?branch=master)](https://travis-ci.org/sindresorhus/is-stream)

> Check if something is a [Node.js stream](https://nodejs.org/api/stream.html)


## Install

```
$ npm install --save is-stream
```


## Usage

```js
const fs = require('fs');
const isStream = require('is-stream');

isStream(fs.createReadStream('unicorn.png'));
//=> true

isStream({});
//=> false
```


## API

### isStream(stream)

#### isStream.writable(stream)

#### isStream.readable(stream)

#### isStream.duplex(stream)

#### isStream.transform(stream)


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# strip-eof [![Build Status](https://travis-ci.org/sindresorhus/strip-eof.svg?branch=master)](https://travis-ci.org/sindresorhus/strip-eof)

> Strip the [End-Of-File](https://en.wikipedia.org/wiki/End-of-file) (EOF) character from a string/buffer


## Install

```
$ npm install --save strip-eof
```


## Usage

```js
const stripEof = require('strip-eof');

stripEof('foo\nbar\n\n');
//=> 'foo\nbar\n'

stripEof(new Buffer('foo\nbar\n\n')).toString();
//=> 'foo\nbar\n'
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# p-finally [![Build Status](https://travis-ci.org/sindresorhus/p-finally.svg?branch=master)](https://travis-ci.org/sindresorhus/p-finally)

> [`Promise#finally()`](https://github.com/tc39/proposal-promise-finally) [ponyfill](https://ponyfill.com) - Invoked when the promise is settled regardless of outcome

Useful for cleanup.


## Install

```
$ npm install --save p-finally
```


## Usage

```js
const pFinally = require('p-finally');

const dir = createTempDir();

pFinally(write(dir), () => cleanup(dir));
```


## API

### pFinally(promise, [onFinally])

Returns a `Promise`.

#### onFinally

Type: `Function`

Note: Throwing or returning a rejected promise will reject `promise` with the rejection reason.


## Related

- [p-try](https://github.com/sindresorhus/p-try) - `Promise#try()` ponyfill - Starts a promise chain
- [More…](https://github.com/sindresorhus/promise-fun)


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# is-finite [![Build Status](https://travis-ci.org/sindresorhus/is-finite.svg?branch=master)](https://travis-ci.org/sindresorhus/is-finite)

> ES2015 [`Number.isFinite()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isFinite) [ponyfill](https://ponyfill.com)


## Install

```sh
$ npm install --save is-finite
```


## Usage

```js
var numIsFinite = require('is-finite');

numIsFinite(4);
//=> true

numIsFinite(Infinity);
//=> false
```


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
# cli-spinners [![Build Status](https://travis-ci.org/sindresorhus/cli-spinners.svg?branch=master)](https://travis-ci.org/sindresorhus/cli-spinners)

> 50+ spinners for use in the terminal

![](screenshot.gif)

The list of spinners is just a [JSON file](spinners.json) and can be used wherever.

You probably want to use one of these spinners through the [`ora`](https://github.com/sindresorhus/ora) module.


## Install

```
$ npm install --save cli-spinners
```


## Usage

```js
const cliSpinners = require('cli-spinners');

console.log(cliSpinners.dots);
/*
{
	interval: 80,
	frames: ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
}
*/
```


## API

Each spinner comes with a recommended `interval` and an array of `frames`.

[See the spinners.](spinners.json)


## Related

- [ora](https://github.com/sindresorhus/ora) - Elegant terminal spinner


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
# executable [![Build Status](https://travis-ci.org/kevva/executable.svg?branch=master)](https://travis-ci.org/kevva/executable)

> Check if a file is executable


## Install

```
$ npm install --save executable
```


## Usage

```js
const executable = require('executable');

executable('bash').then(exec => {
	console.log(exec);
	//=> true
});
```


## API

### executable(file)

Returns a Promise for a boolean.

### executable.sync(file)

Returns a boolean of whether the file is executable.

#### file

Type: `string`

Path of the file.

### executable.checkMode(mode, [gid], [uid])

Returns a boolean of whether the mode passed as first argument means that the file is executable.

#### mode

Type: `number`

Property `mode` of `fs.Stats` instance returned by `fs.stat()` (or `fs.statSync()`) function.

#### gid, uid

Type: `number`

Respectively the group identity and user identity of the file. If not set, permissions will be evaluated without considering owner or group of the file.

## Related

* [executable-cli](https://github.com/kevva/executable-cli) - CLI for this module


## License

MIT © [Kevin Mårtensson](https://github.com/kevva)
# core-util-is

The `util.is*` functions introduced in Node v0.12.
# safe-buffer [![travis][travis-image]][travis-url] [![npm][npm-image]][npm-url] [![downloads][downloads-image]][downloads-url] [![javascript style guide][standard-image]][standard-url]

[travis-image]: https://img.shields.io/travis/feross/safe-buffer/master.svg
[travis-url]: https://travis-ci.org/feross/safe-buffer
[npm-image]: https://img.shields.io/npm/v/safe-buffer.svg
[npm-url]: https://npmjs.org/package/safe-buffer
[downloads-image]: https://img.shields.io/npm/dm/safe-buffer.svg
[downloads-url]: https://npmjs.org/package/safe-buffer
[standard-image]: https://img.shields.io/badge/code_style-standard-brightgreen.svg
[standard-url]: https://standardjs.com

#### Safer Node.js Buffer API

**Use the new Node.js Buffer APIs (`Buffer.from`, `Buffer.alloc`,
`Buffer.allocUnsafe`, `Buffer.allocUnsafeSlow`) in all versions of Node.js.**

**Uses the built-in implementation when available.**

## install

```
npm install safe-buffer
```

## usage

The goal of this package is to provide a safe replacement for the node.js `Buffer`.

It's a drop-in replacement for `Buffer`. You can use it by adding one `require` line to
the top of your node.js modules:

```js
var Buffer = require('safe-buffer').Buffer

// Existing buffer code will continue to work without issues:

new Buffer('hey', 'utf8')
new Buffer([1, 2, 3], 'utf8')
new Buffer(obj)
new Buffer(16) // create an uninitialized buffer (potentially unsafe)

// But you can use these new explicit APIs to make clear what you want:

Buffer.from('hey', 'utf8') // convert from many types to a Buffer
Buffer.alloc(16) // create a zero-filled buffer (safe)
Buffer.allocUnsafe(16) // create an uninitialized buffer (potentially unsafe)
```

## api

### Class Method: Buffer.from(array)
<!-- YAML
added: v3.0.0
-->

* `array` {Array}

Allocates a new `Buffer` using an `array` of octets.

```js
const buf = Buffer.from([0x62,0x75,0x66,0x66,0x65,0x72]);
  // creates a new Buffer containing ASCII bytes
  // ['b','u','f','f','e','r']
```

A `TypeError` will be thrown if `array` is not an `Array`.

### Class Method: Buffer.from(arrayBuffer[, byteOffset[, length]])
<!-- YAML
added: v5.10.0
-->

* `arrayBuffer` {ArrayBuffer} The `.buffer` property of a `TypedArray` or
  a `new ArrayBuffer()`
* `byteOffset` {Number} Default: `0`
* `length` {Number} Default: `arrayBuffer.length - byteOffset`

When passed a reference to the `.buffer` property of a `TypedArray` instance,
the newly created `Buffer` will share the same allocated memory as the
TypedArray.

```js
const arr = new Uint16Array(2);
arr[0] = 5000;
arr[1] = 4000;

const buf = Buffer.from(arr.buffer); // shares the memory with arr;

console.log(buf);
  // Prints: <Buffer 88 13 a0 0f>

// changing the TypedArray changes the Buffer also
arr[1] = 6000;

console.log(buf);
  // Prints: <Buffer 88 13 70 17>
```

The optional `byteOffset` and `length` arguments specify a memory range within
the `arrayBuffer` that will be shared by the `Buffer`.

```js
const ab = new ArrayBuffer(10);
const buf = Buffer.from(ab, 0, 2);
console.log(buf.length);
  // Prints: 2
```

A `TypeError` will be thrown if `arrayBuffer` is not an `ArrayBuffer`.

### Class Method: Buffer.from(buffer)
<!-- YAML
added: v3.0.0
-->

* `buffer` {Buffer}

Copies the passed `buffer` data onto a new `Buffer` instance.

```js
const buf1 = Buffer.from('buffer');
const buf2 = Buffer.from(buf1);

buf1[0] = 0x61;
console.log(buf1.toString());
  // 'auffer'
console.log(buf2.toString());
  // 'buffer' (copy is not changed)
```

A `TypeError` will be thrown if `buffer` is not a `Buffer`.

### Class Method: Buffer.from(str[, encoding])
<!-- YAML
added: v5.10.0
-->

* `str` {String} String to encode.
* `encoding` {String} Encoding to use, Default: `'utf8'`

Creates a new `Buffer` containing the given JavaScript string `str`. If
provided, the `encoding` parameter identifies the character encoding.
If not provided, `encoding` defaults to `'utf8'`.

```js
const buf1 = Buffer.from('this is a tést');
console.log(buf1.toString());
  // prints: this is a tést
console.log(buf1.toString('ascii'));
  // prints: this is a tC)st

const buf2 = Buffer.from('7468697320697320612074c3a97374', 'hex');
console.log(buf2.toString());
  // prints: this is a tést
```

A `TypeError` will be thrown if `str` is not a string.

### Class Method: Buffer.alloc(size[, fill[, encoding]])
<!-- YAML
added: v5.10.0
-->

* `size` {Number}
* `fill` {Value} Default: `undefined`
* `encoding` {String} Default: `utf8`

Allocates a new `Buffer` of `size` bytes. If `fill` is `undefined`, the
`Buffer` will be *zero-filled*.

```js
const buf = Buffer.alloc(5);
console.log(buf);
  // <Buffer 00 00 00 00 00>
```

The `size` must be less than or equal to the value of
`require('buffer').kMaxLength` (on 64-bit architectures, `kMaxLength` is
`(2^31)-1`). Otherwise, a [`RangeError`][] is thrown. A zero-length Buffer will
be created if a `size` less than or equal to 0 is specified.

If `fill` is specified, the allocated `Buffer` will be initialized by calling
`buf.fill(fill)`. See [`buf.fill()`][] for more information.

```js
const buf = Buffer.alloc(5, 'a');
console.log(buf);
  // <Buffer 61 61 61 61 61>
```

If both `fill` and `encoding` are specified, the allocated `Buffer` will be
initialized by calling `buf.fill(fill, encoding)`. For example:

```js
const buf = Buffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');
console.log(buf);
  // <Buffer 68 65 6c 6c 6f 20 77 6f 72 6c 64>
```

Calling `Buffer.alloc(size)` can be significantly slower than the alternative
`Buffer.allocUnsafe(size)` but ensures that the newly created `Buffer` instance
contents will *never contain sensitive data*.

A `TypeError` will be thrown if `size` is not a number.

### Class Method: Buffer.allocUnsafe(size)
<!-- YAML
added: v5.10.0
-->

* `size` {Number}

Allocates a new *non-zero-filled* `Buffer` of `size` bytes.  The `size` must
be less than or equal to the value of `require('buffer').kMaxLength` (on 64-bit
architectures, `kMaxLength` is `(2^31)-1`). Otherwise, a [`RangeError`][] is
thrown. A zero-length Buffer will be created if a `size` less than or equal to
0 is specified.

The underlying memory for `Buffer` instances created in this way is *not
initialized*. The contents of the newly created `Buffer` are unknown and
*may contain sensitive data*. Use [`buf.fill(0)`][] to initialize such
`Buffer` instances to zeroes.

```js
const buf = Buffer.allocUnsafe(5);
console.log(buf);
  // <Buffer 78 e0 82 02 01>
  // (octets will be different, every time)
buf.fill(0);
console.log(buf);
  // <Buffer 00 00 00 00 00>
```

A `TypeError` will be thrown if `size` is not a number.

Note that the `Buffer` module pre-allocates an internal `Buffer` instance of
size `Buffer.poolSize` that is used as a pool for the fast allocation of new
`Buffer` instances created using `Buffer.allocUnsafe(size)` (and the deprecated
`new Buffer(size)` constructor) only when `size` is less than or equal to
`Buffer.poolSize >> 1` (floor of `Buffer.poolSize` divided by two). The default
value of `Buffer.poolSize` is `8192` but can be modified.

Use of this pre-allocated internal memory pool is a key difference between
calling `Buffer.alloc(size, fill)` vs. `Buffer.allocUnsafe(size).fill(fill)`.
Specifically, `Buffer.alloc(size, fill)` will *never* use the internal Buffer
pool, while `Buffer.allocUnsafe(size).fill(fill)` *will* use the internal
Buffer pool if `size` is less than or equal to half `Buffer.poolSize`. The
difference is subtle but can be important when an application requires the
additional performance that `Buffer.allocUnsafe(size)` provides.

### Class Method: Buffer.allocUnsafeSlow(size)
<!-- YAML
added: v5.10.0
-->

* `size` {Number}

Allocates a new *non-zero-filled* and non-pooled `Buffer` of `size` bytes.  The
`size` must be less than or equal to the value of
`require('buffer').kMaxLength` (on 64-bit architectures, `kMaxLength` is
`(2^31)-1`). Otherwise, a [`RangeError`][] is thrown. A zero-length Buffer will
be created if a `size` less than or equal to 0 is specified.

The underlying memory for `Buffer` instances created in this way is *not
initialized*. The contents of the newly created `Buffer` are unknown and
*may contain sensitive data*. Use [`buf.fill(0)`][] to initialize such
`Buffer` instances to zeroes.

When using `Buffer.allocUnsafe()` to allocate new `Buffer` instances,
allocations under 4KB are, by default, sliced from a single pre-allocated
`Buffer`. This allows applications to avoid the garbage collection overhead of
creating many individually allocated Buffers. This approach improves both
performance and memory usage by eliminating the need to track and cleanup as
many `Persistent` objects.

However, in the case where a developer may need to retain a small chunk of
memory from a pool for an indeterminate amount of time, it may be appropriate
to create an un-pooled Buffer instance using `Buffer.allocUnsafeSlow()` then
copy out the relevant bits.

```js
// need to keep around a few small chunks of memory
const store = [];

socket.on('readable', () => {
  const data = socket.read();
  // allocate for retained data
  const sb = Buffer.allocUnsafeSlow(10);
  // copy the data into the new allocation
  data.copy(sb, 0, 0, 10);
  store.push(sb);
});
```

Use of `Buffer.allocUnsafeSlow()` should be used only as a last resort *after*
a developer has observed undue memory retention in their applications.

A `TypeError` will be thrown if `size` is not a number.

### All the Rest

The rest of the `Buffer` API is exactly the same as in node.js.
[See the docs](https://nodejs.org/api/buffer.html).


## Related links

- [Node.js issue: Buffer(number) is unsafe](https://github.com/nodejs/node/issues/4660)
- [Node.js Enhancement Proposal: Buffer.from/Buffer.alloc/Buffer.zalloc/Buffer() soft-deprecate](https://github.com/nodejs/node-eps/pull/4)

## Why is `Buffer` unsafe?

Today, the node.js `Buffer` constructor is overloaded to handle many different argument
types like `String`, `Array`, `Object`, `TypedArrayView` (`Uint8Array`, etc.),
`ArrayBuffer`, and also `Number`.

The API is optimized for convenience: you can throw any type at it, and it will try to do
what you want.

Because the Buffer constructor is so powerful, you often see code like this:

```js
// Convert UTF-8 strings to hex
function toHex (str) {
  return new Buffer(str).toString('hex')
}
```

***But what happens if `toHex` is called with a `Number` argument?***

### Remote Memory Disclosure

If an attacker can make your program call the `Buffer` constructor with a `Number`
argument, then they can make it allocate uninitialized memory from the node.js process.
This could potentially disclose TLS private keys, user data, or database passwords.

When the `Buffer` constructor is passed a `Number` argument, it returns an
**UNINITIALIZED** block of memory of the specified `size`. When you create a `Buffer` like
this, you **MUST** overwrite the contents before returning it to the user.

From the [node.js docs](https://nodejs.org/api/buffer.html#buffer_new_buffer_size):

> `new Buffer(size)`
>
> - `size` Number
>
> The underlying memory for `Buffer` instances created in this way is not initialized.
> **The contents of a newly created `Buffer` are unknown and could contain sensitive
> data.** Use `buf.fill(0)` to initialize a Buffer to zeroes.

(Emphasis our own.)

Whenever the programmer intended to create an uninitialized `Buffer` you often see code
like this:

```js
var buf = new Buffer(16)

// Immediately overwrite the uninitialized buffer with data from another buffer
for (var i = 0; i < buf.length; i++) {
  buf[i] = otherBuf[i]
}
```


### Would this ever be a problem in real code?

Yes. It's surprisingly common to forget to check the type of your variables in a
dynamically-typed language like JavaScript.

Usually the consequences of assuming the wrong type is that your program crashes with an
uncaught exception. But the failure mode for forgetting to check the type of arguments to
the `Buffer` constructor is more catastrophic.

Here's an example of a vulnerable service that takes a JSON payload and converts it to
hex:

```js
// Take a JSON payload {str: "some string"} and convert it to hex
var server = http.createServer(function (req, res) {
  var data = ''
  req.setEncoding('utf8')
  req.on('data', function (chunk) {
    data += chunk
  })
  req.on('end', function () {
    var body = JSON.parse(data)
    res.end(new Buffer(body.str).toString('hex'))
  })
})

server.listen(8080)
```

In this example, an http client just has to send:

```json
{
  "str": 1000
}
```

and it will get back 1,000 bytes of uninitialized memory from the server.

This is a very serious bug. It's similar in severity to the
[the Heartbleed bug](http://heartbleed.com/) that allowed disclosure of OpenSSL process
memory by remote attackers.


### Which real-world packages were vulnerable?

#### [`bittorrent-dht`](https://www.npmjs.com/package/bittorrent-dht)

[Mathias Buus](https://github.com/mafintosh) and I
([Feross Aboukhadijeh](http://feross.org/)) found this issue in one of our own packages,
[`bittorrent-dht`](https://www.npmjs.com/package/bittorrent-dht). The bug would allow
anyone on the internet to send a series of messages to a user of `bittorrent-dht` and get
them to reveal 20 bytes at a time of uninitialized memory from the node.js process.

Here's
[the commit](https://github.com/feross/bittorrent-dht/commit/6c7da04025d5633699800a99ec3fbadf70ad35b8)
that fixed it. We released a new fixed version, created a
[Node Security Project disclosure](https://nodesecurity.io/advisories/68), and deprecated all
vulnerable versions on npm so users will get a warning to upgrade to a newer version.

#### [`ws`](https://www.npmjs.com/package/ws)

That got us wondering if there were other vulnerable packages. Sure enough, within a short
period of time, we found the same issue in [`ws`](https://www.npmjs.com/package/ws), the
most popular WebSocket implementation in node.js.

If certain APIs were called with `Number` parameters instead of `String` or `Buffer` as
expected, then uninitialized server memory would be disclosed to the remote peer.

These were the vulnerable methods:

```js
socket.send(number)
socket.ping(number)
socket.pong(number)
```

Here's a vulnerable socket server with some echo functionality:

```js
server.on('connection', function (socket) {
  socket.on('message', function (message) {
    message = JSON.parse(message)
    if (message.type === 'echo') {
      socket.send(message.data) // send back the user's message
    }
  })
})
```

`socket.send(number)` called on the server, will disclose server memory.

Here's [the release](https://github.com/websockets/ws/releases/tag/1.0.1) where the issue
was fixed, with a more detailed explanation. Props to
[Arnout Kazemier](https://github.com/3rd-Eden) for the quick fix. Here's the
[Node Security Project disclosure](https://nodesecurity.io/advisories/67).


### What's the solution?

It's important that node.js offers a fast way to get memory otherwise performance-critical
applications would needlessly get a lot slower.

But we need a better way to *signal our intent* as programmers. **When we want
uninitialized memory, we should request it explicitly.**

Sensitive functionality should not be packed into a developer-friendly API that loosely
accepts many different types. This type of API encourages the lazy practice of passing
variables in without checking the type very carefully.

#### A new API: `Buffer.allocUnsafe(number)`

The functionality of creating buffers with uninitialized memory should be part of another
API. We propose `Buffer.allocUnsafe(number)`. This way, it's not part of an API that
frequently gets user input of all sorts of different types passed into it.

```js
var buf = Buffer.allocUnsafe(16) // careful, uninitialized memory!

// Immediately overwrite the uninitialized buffer with data from another buffer
for (var i = 0; i < buf.length; i++) {
  buf[i] = otherBuf[i]
}
```


### How do we fix node.js core?

We sent [a PR to node.js core](https://github.com/nodejs/node/pull/4514) (merged as
`semver-major`) which defends against one case:

```js
var str = 16
new Buffer(str, 'utf8')
```

In this situation, it's implied that the programmer intended the first argument to be a
string, since they passed an encoding as a second argument. Today, node.js will allocate
uninitialized memory in the case of `new Buffer(number, encoding)`, which is probably not
what the programmer intended.

But this is only a partial solution, since if the programmer does `new Buffer(variable)`
(without an `encoding` parameter) there's no way to know what they intended. If `variable`
is sometimes a number, then uninitialized memory will sometimes be returned.

### What's the real long-term fix?

We could deprecate and remove `new Buffer(number)` and use `Buffer.allocUnsafe(number)` when
we need uninitialized memory. But that would break 1000s of packages.

~~We believe the best solution is to:~~

~~1. Change `new Buffer(number)` to return safe, zeroed-out memory~~

~~2. Create a new API for creating uninitialized Buffers. We propose: `Buffer.allocUnsafe(number)`~~

#### Update

We now support adding three new APIs:

- `Buffer.from(value)` - convert from any type to a buffer
- `Buffer.alloc(size)` - create a zero-filled buffer
- `Buffer.allocUnsafe(size)` - create an uninitialized buffer with given size

This solves the core problem that affected `ws` and `bittorrent-dht` which is
`Buffer(variable)` getting tricked into taking a number argument.

This way, existing code continues working and the impact on the npm ecosystem will be
minimal. Over time, npm maintainers can migrate performance-critical code to use
`Buffer.allocUnsafe(number)` instead of `new Buffer(number)`.


### Conclusion

We think there's a serious design issue with the `Buffer` API as it exists today. It
promotes insecure software by putting high-risk functionality into a convenient API
with friendly "developer ergonomics".

This wasn't merely a theoretical exercise because we found the issue in some of the
most popular npm packages.

Fortunately, there's an easy fix that can be applied today. Use `safe-buffer` in place of
`buffer`.

```js
var Buffer = require('safe-buffer').Buffer
```

Eventually, we hope that node.js core can switch to this new, safer behavior. We believe
the impact on the ecosystem would be minimal since it's not a breaking change.
Well-maintained, popular packages would be updated to use `Buffer.alloc` quickly, while
older, insecure packages would magically become safe from this attack vector.


## links

- [Node.js PR: buffer: throw if both length and enc are passed](https://github.com/nodejs/node/pull/4514)
- [Node Security Project disclosure for `ws`](https://nodesecurity.io/advisories/67)
- [Node Security Project disclosure for`bittorrent-dht`](https://nodesecurity.io/advisories/68)


## credit

The original issues in `bittorrent-dht`
([disclosure](https://nodesecurity.io/advisories/68)) and
`ws` ([disclosure](https://nodesecurity.io/advisories/67)) were discovered by
[Mathias Buus](https://github.com/mafintosh) and
[Feross Aboukhadijeh](http://feross.org/).

Thanks to [Adam Baldwin](https://github.com/evilpacket) for helping disclose these issues
and for his work running the [Node Security Project](https://nodesecurity.io/).

Thanks to [John Hiesey](https://github.com/jhiesey) for proofreading this README and
auditing the code.


## license

MIT. Copyright (C) [Feross Aboukhadijeh](http://feross.org)
# color-convert

[![Build Status](https://travis-ci.org/Qix-/color-convert.svg?branch=master)](https://travis-ci.org/Qix-/color-convert)

Color-convert is a color conversion library for JavaScript and node.
It converts all ways between `rgb`, `hsl`, `hsv`, `hwb`, `cmyk`, `ansi`, `ansi16`, `hex` strings, and CSS `keyword`s (will round to closest):

```js
var convert = require('color-convert');

convert.rgb.hsl(140, 200, 100);             // [96, 48, 59]
convert.keyword.rgb('blue');                // [0, 0, 255]

var rgbChannels = convert.rgb.channels;     // 3
var cmykChannels = convert.cmyk.channels;   // 4
var ansiChannels = convert.ansi16.channels; // 1
```

# Install

```console
$ npm install color-convert
```

# API

Simply get the property of the _from_ and _to_ conversion that you're looking for.

All functions have a rounded and unrounded variant. By default, return values are rounded. To get the unrounded (raw) results, simply tack on `.raw` to the function.

All 'from' functions have a hidden property called `.channels` that indicates the number of channels the function expects (not including alpha).

```js
var convert = require('color-convert');

// Hex to LAB
convert.hex.lab('DEADBF');         // [ 76, 21, -2 ]
convert.hex.lab.raw('DEADBF');     // [ 75.56213190997677, 20.653827952644754, -2.290532499330533 ]

// RGB to CMYK
convert.rgb.cmyk(167, 255, 4);     // [ 35, 0, 98, 0 ]
convert.rgb.cmyk.raw(167, 255, 4); // [ 34.509803921568626, 0, 98.43137254901961, 0 ]
```

### Arrays
All functions that accept multiple arguments also support passing an array.

Note that this does **not** apply to functions that convert from a color that only requires one value (e.g. `keyword`, `ansi256`, `hex`, etc.)

```js
var convert = require('color-convert');

convert.rgb.hex(123, 45, 67);      // '7B2D43'
convert.rgb.hex([123, 45, 67]);    // '7B2D43'
```

## Routing

Conversions that don't have an _explicitly_ defined conversion (in [conversions.js](conversions.js)), but can be converted by means of sub-conversions (e.g. XYZ -> **RGB** -> CMYK), are automatically routed together. This allows just about any color model supported by `color-convert` to be converted to any other model, so long as a sub-conversion path exists. This is also true for conversions requiring more than one step in between (e.g. LCH -> **LAB** -> **XYZ** -> **RGB** -> Hex).

Keep in mind that extensive conversions _may_ result in a loss of precision, and exist only to be complete. For a list of "direct" (single-step) conversions, see [conversions.js](conversions.js).

# Contribute

If there is a new model you would like to support, or want to add a direct conversion between two existing models, please send us a pull request.

# License
Copyright &copy; 2011-2016, Heather Arthur and Josh Junon. Licensed under the [MIT License](LICENSE).
# Installation
> `npm install --save @types/bluebird`

# Summary
This package contains type definitions for bluebird (https://github.com/petkaantonov/bluebird).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/bluebird

Additional Details
 * Last updated: Tue, 31 Oct 2017 00:15:11 GMT
 * Dependencies: none
 * Global values: none

# Credits
These definitions were written by Leonard Hecker <https://github.com/lhecker>.
# Installation
> `npm install --save @types/minimatch`

# Summary
This package contains type definitions for Minimatch (https://github.com/isaacs/minimatch).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/minimatch

Additional Details
 * Last updated: Thu, 04 Jan 2018 23:26:01 GMT
 * Dependencies: none
 * Global values: none

# Credits
These definitions were written by vvakame <https://github.com/vvakame>, Shant Marouti <https://github.com/shantmarouti>.
# Installation
> `npm install --save @types/chai`

# Summary
This package contains type definitions for chai (http://chaijs.com/).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/chai

Additional Details
 * Last updated: Mon, 04 Dec 2017 20:31:32 GMT
 * Dependencies: none
 * Global values: Chai, chai

# Credits
These definitions were written by Jed Mao <https://github.com/jedmao>, Bart van der Schoor <https://github.com/Bartvds>, Andrew Brown <https://github.com/AGBrown>, Olivier Chevet <https://github.com/olivr70>, Matt Wistrand <https://github.com/mwistrand>, Josh Goldberg <https://github.com/joshuakgoldberg>, Shaun Luttin <https://github.com/shaunluttin>, Gintautas Miselis <https://github.com/Naktibalda>.
# Installation
> `npm install --save @types/sinon-chai`

# Summary
This package contains type definitions for sinon-chai (https://github.com/domenic/sinon-chai).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/sinon-chai

Additional Details
 * Last updated: Mon, 21 Aug 2017 22:03:22 GMT
 * Dependencies: sinon, chai
 * Global values: none

# Credits
These definitions were written by Kazi Manzur Rashid <https://github.com/kazimanzurrashid>, Jed Mao <https://github.com/jedmao>.
# Installation
> `npm install --save @types/sinon`

# Summary
This package contains type definitions for Sinon (http://sinonjs.org/).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/sinon

Additional Details
 * Last updated: Mon, 13 Nov 2017 23:49:21 GMT
 * Dependencies: none
 * Global values: sinon

# Credits
These definitions were written by William Sears <https://github.com/mrbigdog2u>, Jonathan Little <https://github.com/rationull>, Lukas Spieß <https://github.com/lumaxis>, Nico Jansen <https://github.com/nicojs>, James Garbutt <https://github.com/43081j>.
# Installation
> `npm install --save @types/chai-jquery`

# Summary
This package contains type definitions for chai-jquery (https://github.com/chaijs/chai-jquery).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/chai-jquery

Additional Details
 * Last updated: Mon, 21 Aug 2017 21:49:18 GMT
 * Dependencies: chai, jquery
 * Global values: none

# Credits
These definitions were written by Kazi Manzur Rashid <https://github.com/kazimanzurrashid>.
# Installation
> `npm install --save @types/jquery`

# Summary
This package contains type definitions for jquery (https://jquery.com).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jquery

Additional Details
 * Last updated: Mon, 30 Oct 2017 15:12:36 GMT
 * Dependencies: none
 * Global values: $, JQuery, jQuery

# Credits
These definitions were written by Leonard Thieu <https://github.com/leonard-thieu>, Boris Yankov <https://github.com/borisyankov>, Christian Hoffmeister <https://github.com/choffmeister>, Steve Fenton <https://github.com/Steve-Fenton>, Diullei Gomes <https://github.com/Diullei>, Tass Iliopoulos <https://github.com/tasoili>, Jason Swearingen <https://github.com/jasons-novaleaf>, Sean Hill <https://github.com/seanski>, Guus Goossens <https://github.com/Guuz>, Kelly Summerlin <https://github.com/ksummerlin>, Basarat Ali Syed <https://github.com/basarat>, Nicholas Wolverson <https://github.com/nwolverson>, Derek Cicerone <https://github.com/derekcicerone>, Andrew Gaspar <https://github.com/AndrewGaspar>, Seikichi Kondo <https://github.com/seikichi>, Benjamin Jackman <https://github.com/benjaminjackman>, Poul Sorensen <https://github.com/s093294>, Josh Strobl <https://github.com/JoshStrobl>, John Reilly <https://github.com/johnnyreilly>, Dick van den Brink <https://github.com/DickvdBrink>, Thomas Schulz <https://github.com/King2500>.
# Installation
> `npm install --save @types/lodash`

# Summary
This package contains type definitions for Lo-Dash (http://lodash.com/).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/lodash

Additional Details
 * Last updated: Sun, 03 Dec 2017 16:26:41 GMT
 * Dependencies: none
 * Global values: _

# Credits
These definitions were written by Brian Zengel <https://github.com/bczengel>, Ilya Mochalov <https://github.com/chrootsu>, Stepan Mikhaylyuk <https://github.com/stepancar>, Eric L Anderson <https://github.com/ericanderson>, AJ Richardson <https://github.com/aj-r>, Junyoung Clare Jang <https://github.com/ailrun>, e-cloud <https://github.com/e-cloud>, Georgii Dolzhykov <https://github.com/thorn0>, Jack Moore <https://github.com/jtmthf>.
# Installation
> `npm install --save @types/mocha`

# Summary
This package contains type definitions for mocha (http://mochajs.org/).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/mocha

Additional Details
 * Last updated: Thu, 26 Oct 2017 18:02:22 GMT
 * Dependencies: none
 * Global values: Mocha, after, afterEach, before, beforeEach, context, describe, it, mocha, run, setup, specify, suite, suiteSetup, suiteTeardown, teardown, test, xdescribe, xit

# Credits
These definitions were written by Kazi Manzur Rashid <https://github.com/kazimanzurrashid>, otiai10 <https://github.com/otiai10>, jt000 <https://github.com/jt000>, Vadim Macagon <https://github.com/enlight>.
# Installation
> `npm install --save @types/blob-util`

# Summary
This package contains type definitions for blob-util (https://github.com/nolanlawson/blob-util#readme).

# Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/blob-util

Additional Details
 * Last updated: Wed, 25 Oct 2017 00:19:45 GMT
 * Dependencies: none
 * Global values: none

# Credits
These definitions were written by Max Battcher <https://github.com/WorldMaker>.
<a href="http://promisesaplus.com/">
    <img src="http://promisesaplus.com/assets/logo-small.png" alt="Promises/A+ logo"
         title="Promises/A+ 1.1 compliant" align="right" />
</a>
[![Build Status](https://travis-ci.org/petkaantonov/bluebird.svg?branch=master)](https://travis-ci.org/petkaantonov/bluebird)
[![coverage-98%](http://img.shields.io/badge/coverage-98%-brightgreen.svg?style=flat)](http://petkaantonov.github.io/bluebird/coverage/debug/index.html)

**Got a question?** Join us on [stackoverflow](http://stackoverflow.com/questions/tagged/bluebird), the [mailing list](https://groups.google.com/forum/#!forum/bluebird-js) or chat on [IRC](https://webchat.freenode.net/?channels=#promises)

# Introduction

Bluebird is a fully featured promise library with focus on innovative features and performance

See the [**bluebird website**](http://bluebirdjs.com/docs/getting-started.html) for further documentation, references and instructions. See the [**API reference**](http://bluebirdjs.com/docs/api-reference.html) here.

For bluebird 2.x documentation and files, see the [2.x tree](https://github.com/petkaantonov/bluebird/tree/2.x).

# Questions and issues

The [github issue tracker](https://github.com/petkaantonov/bluebird/issues) is **_only_** for bug reports and feature requests. Anything else, such as questions for help in using the library, should be posted in [StackOverflow](http://stackoverflow.com/questions/tagged/bluebird) under tags `promise` and `bluebird`.



## Thanks

Thanks to BrowserStack for providing us with a free account which lets us support old browsers like IE8. 

# License

The MIT License (MIT)

Copyright (c) 2013-2017 Petka Antonov

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
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

# getos

[![Greenkeeper badge](https://badges.greenkeeper.io/retrohacker/getos.svg)](https://greenkeeper.io/)

![getos](./imgs/logo.png)

[![Build Status](https://travis-ci.org/retrohacker/getos.png?branch=master)](https://travis-ci.org/retrohacker/getos) ![](https://img.shields.io/github/issues/retrohacker/getos.svg) ![](https://img.shields.io/npm/dm/getos.svg) ![](https://img.shields.io/npm/v/getos.svg) ![](https://img.shields.io/npm/l/getos.svg)  ![](https://img.shields.io/twitter/url/https/github.com/retrohacker/getos.svg?style=social)

[![NPM](https://nodei.co/npm/getos.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/getos/)[![NPM](https://nodei.co/npm-dl/getos.png?months=9&height=3)](https://nodei.co/npm/getos/)

[![JavaScript Style Guide](https://cdn.rawgit.com/feross/standard/master/badge.svg)](https://github.com/feross/standard)


Get the OS/Distribution name of the environment you are working on

## Problem

`os.platform()` returns `linux`. If you want the distrubtion name, you're out of luck.

## Solution

This. Simply call:

```js
var getos = require('getos')

getos(function(e,os) {
  if(e) return console.log(e)
  console.log("Your OS is:" +JSON.stringify(os))
})
```

The `os` object conforms to:

```js
{
  os: [OS NAME],
  dist:[DIST NAME],
  codename:[CODENAME],
  release:[VERSION]
}
```

For example:

```js
{
  os: "linux",
  dist: "Ubuntu Linux",
  codename: "precise",
  release: "12.04"
}
```

## Disclaimer
Check `os.json` in this repo. Any distribution that *shares* a common resource file with another distrubtion is currently untested. These are the arrays of distrubitons with more than 1 member. If you are using one of these distrubtions, please submit an issue letting me know if it works. If it fails, please post the content of the file.

If you have a distrubtion *not* in `os.json`, please identify your resource file and submit it's name and content along with your distrbution/version in an issue.

Thanks for helping make this tool great.

## Unit Tests

Unit tests stub out the behaviour of the OS files and libraries we depend on to ensure the behaviour of the application is sound. You can run these simply by running `npm test`

## Authors and Contributors

getos has been made possible by these fantastic contributors:

<table><tbody>
<tr><th align="left">Benjamin E. Coe</th><td><a href="https://github.com/bcoe">GitHub/bcoe</a></td><td><a href="http://twitter.com/benjamincoe">Twitter/@benjamincoe</a></td></tr>
<tr><th align="left">Eugene Sharygin</th><td><a href="https://github.com/eush77">GitHub/eush77</a></td><td><a href="http://twitter.com/eush77">Twitter/@eush77</a></td></tr>
<tr><th align="left">David Routhieau</th><td><a href="https://github.com/root-io">GitHub/root-io</a></td><td>unknown</td></tr>
<tr><th align="left">Lawrence</th><td><a href="https://github.com/mindmelting">GitHub/mindmelting</a></td><td><a href="http://twitter.com/mindmelting">Twitter/@mindmelting</a></td></tr>
<tr><th align="left">Roman Jurkov</th><td><a href="https://github.com/winfinit">GitHub/winfinit</a></td><td><a href="http://twitter.com/winfinit">Twitter/@winfinit</a></td></tr>
<tr><th align="left">Rod Vagg</th><td><a href="https://github.com/rvagg">GitHub/rvagg</a></td><td><a href="http://twitter.com/rvagg">Twitter/@rvagg</a></td></tr>
<tr><th align="left">Zeke Sikelianos</th><td><a href="https://github.com/zeke">GitHub/zeke</a></td><td><a href="http://twitter.com/zeke">Twitter/@zeke</a></td></tr>
<tr><th align="left">Alexander</th><td><a href="https://github.com/alex4Zero">GitHub/alex4Zero</a></td><td><a href="http://twitter.com/alex4Zero">Twitter/@alex4Zero</a></td></tr>
</tbody></table>
## Caseless -- wrap an object to set and get property with caseless semantics but also preserve caseing.

This library is incredibly useful when working with HTTP headers. It allows you to get/set/check for headers in a caseless manner while also preserving the caseing of headers the first time they are set.

## Usage

```javascript
var headers = {}
  , c = caseless(headers)
  ;
c.set('a-Header', 'asdf')
c.get('a-header') === 'asdf'
```

## has(key)

Has takes a name and if it finds a matching header will return that header name with the preserved caseing it was set with.

```javascript
c.has('a-header') === 'a-Header'
```

## set(key, value[, clobber=true])

Set is fairly straight forward except that if the header exists and clobber is disabled it will add `','+value` to the existing header.

```javascript
c.set('a-Header', 'fdas')
c.set('a-HEADER', 'more', false)
c.get('a-header') === 'fdsa,more'
```

## swap(key)

Swaps the casing of a header with the new one that is passed in.

```javascript
var headers = {}
  , c = caseless(headers)
  ;
c.set('a-Header', 'fdas')
c.swap('a-HEADER')
c.has('a-header') === 'a-HEADER'
headers === {'a-HEADER': 'fdas'}
```
Node.js - jsonfile
================

Easily read/write JSON files.

[![npm Package](https://img.shields.io/npm/v/jsonfile.svg?style=flat-square)](https://www.npmjs.org/package/jsonfile)
[![build status](https://secure.travis-ci.org/jprichardson/node-jsonfile.svg)](http://travis-ci.org/jprichardson/node-jsonfile)
[![windows Build status](https://img.shields.io/appveyor/ci/jprichardson/node-jsonfile/master.svg?label=windows%20build)](https://ci.appveyor.com/project/jprichardson/node-jsonfile/branch/master)

<a href="https://github.com/feross/standard"><img src="https://cdn.rawgit.com/feross/standard/master/sticker.svg" alt="Standard JavaScript" width="100"></a>

Why?
----

Writing `JSON.stringify()` and then `fs.writeFile()` and `JSON.parse()` with `fs.readFile()` enclosed in `try/catch` blocks became annoying.



Installation
------------

    npm install --save jsonfile



API
---

### readFile(filename, [options], callback)

`options` (`object`, default `undefined`): Pass in any `fs.readFile` options or set `reviver` for a [JSON reviver](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse).
  - `throws` (`boolean`, default: `true`). If `JSON.parse` throws an error, pass this error to the callback.
  If `false`, returns `null` for the object.


```js
var jsonfile = require('jsonfile')
var file = '/tmp/data.json'
jsonfile.readFile(file, function(err, obj) {
  console.dir(obj)
})
```


### readFileSync(filename, [options])

`options` (`object`, default `undefined`): Pass in any `fs.readFileSync` options or set `reviver` for a [JSON reviver](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse).
- `throws` (`boolean`, default: `true`). If an error is encountered reading or parsing the file, throw the error. If `false`, returns `null` for the object.

```js
var jsonfile = require('jsonfile')
var file = '/tmp/data.json'

console.dir(jsonfile.readFileSync(file))
```


### writeFile(filename, obj, [options], callback)

`options`: Pass in any `fs.writeFile` options or set `replacer` for a [JSON replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify). Can also pass in `spaces`.


```js
var jsonfile = require('jsonfile')

var file = '/tmp/data.json'
var obj = {name: 'JP'}

jsonfile.writeFile(file, obj, function (err) {
  console.error(err)
})
```

**formatting with spaces:**

```js
var jsonfile = require('jsonfile')

var file = '/tmp/data.json'
var obj = {name: 'JP'}

jsonfile.writeFile(file, obj, {spaces: 2}, function(err) {
  console.error(err)
})
```

**appending to an existing JSON file:**

You can use `fs.writeFile` option `{flag: 'a'}` to achieve this.

```js
var jsonfile = require('jsonfile')

var file = '/tmp/mayAlreadyExistedData.json'
var obj = {name: 'JP'}

jsonfile.writeFile(file, obj, {flag: 'a'}, function (err) {
  console.error(err)
})
```

### writeFileSync(filename, obj, [options])

`options`: Pass in any `fs.writeFileSync` options or set `replacer` for a [JSON replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify). Can also pass in `spaces`.

```js
var jsonfile = require('jsonfile')

var file = '/tmp/data.json'
var obj = {name: 'JP'}

jsonfile.writeFileSync(file, obj)
```

**formatting with spaces:**

```js
var jsonfile = require('jsonfile')

var file = '/tmp/data.json'
var obj = {name: 'JP'}

jsonfile.writeFileSync(file, obj, {spaces: 2})
```

**appending to an existing JSON file:**

You can use `fs.writeFileSync` option `{flag: 'a'}` to achieve this.

```js
var jsonfile = require('jsonfile')

var file = '/tmp/mayAlreadyExistedData.json'
var obj = {name: 'JP'}

jsonfile.writeFileSync(file, obj, {flag: 'a'})
```

### spaces

Global configuration to set spaces to indent JSON files.

**default:** `null`

```js
var jsonfile = require('jsonfile')

jsonfile.spaces = 4

var file = '/tmp/data.json'
var obj = {name: 'JP'}

// json file has four space indenting now
jsonfile.writeFile(file, obj, function (err) {
  console.error(err)
})
```

Note, it's bound to `this.spaces`. So, if you do this:

```js
var myObj = {}
myObj.writeJsonSync = jsonfile.writeFileSync
// => this.spaces = null
```

Could do the following:

```js
var jsonfile = require('jsonfile')
jsonfile.spaces = 4
jsonfile.writeFileSync(file, obj) // will have 4 spaces indentation

var myCrazyObj = {spaces: 32}
myCrazyObj.writeJsonSync = jsonfile.writeFileSync
myCrazyObj.writeJsonSync(file, obj) // will have 32 space indentation
myCrazyObj.writeJsonSync(file, obj, {spaces: 2}) // will have only 2
```


License
-------

(MIT License)

Copyright 2012-2016, JP Richardson  <jprichardson@gmail.com>
[![Build Status][travis-svg]][travis-url]
[![dependency status][deps-svg]][deps-url]
[![dev dependency status][dev-deps-svg]][dev-deps-url]

# extend() for Node.js <sup>[![Version Badge][npm-version-png]][npm-url]</sup>

`node-extend` is a port of the classic extend() method from jQuery. It behaves as you expect. It is simple, tried and true.

Notes:

* Since Node.js >= 4,
  [`Object.assign`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
  now offers the same functionality natively (but without the "deep copy" option).
  See [ECMAScript 2015 (ES6) in Node.js](https://nodejs.org/en/docs/es6).
* Some native implementations of `Object.assign` in both Node.js and many
  browsers (since NPM modules are for the browser too) may not be fully
  spec-compliant.
  Check [`object.assign`](https://www.npmjs.com/package/object.assign) module for
  a compliant candidate.

## Installation

This package is available on [npm][npm-url] as: `extend`

``` sh
npm install extend
```

## Usage

**Syntax:** extend **(** [`deep`], `target`, `object1`, [`objectN`] **)**

*Extend one object with one or more others, returning the modified object.*

**Example:**

``` js
var extend = require('extend');
extend(targetObject, object1, object2);
```

Keep in mind that the target object will be modified, and will be returned from extend().

If a boolean true is specified as the first argument, extend performs a deep copy, recursively copying any objects it finds. Otherwise, the copy will share structure with the original object(s).
Undefined properties are not copied. However, properties inherited from the object's prototype will be copied over.
Warning: passing `false` as the first argument is not supported.

### Arguments

* `deep` *Boolean* (optional)
If set, the merge becomes recursive (i.e. deep copy).
* `target`	*Object*
The object to extend.
* `object1`	*Object*
The object that will be merged into the first.
* `objectN` *Object* (Optional)
More objects to merge into the first.

## License

`node-extend` is licensed under the [MIT License][mit-license-url].

## Acknowledgements

All credit to the jQuery authors for perfecting this amazing utility.

Ported to Node.js by [Stefan Thomas][github-justmoon] with contributions by [Jonathan Buchanan][github-insin] and [Jordan Harband][github-ljharb].

[travis-svg]: https://travis-ci.org/justmoon/node-extend.svg
[travis-url]: https://travis-ci.org/justmoon/node-extend
[npm-url]: https://npmjs.org/package/extend
[mit-license-url]: http://opensource.org/licenses/MIT
[github-justmoon]: https://github.com/justmoon
[github-insin]: https://github.com/insin
[github-ljharb]: https://github.com/ljharb
[npm-version-png]: http://versionbadg.es/justmoon/node-extend.svg
[deps-svg]: https://david-dm.org/justmoon/node-extend.svg
[deps-url]: https://david-dm.org/justmoon/node-extend
[dev-deps-svg]: https://david-dm.org/justmoon/node-extend/dev-status.svg
[dev-deps-url]: https://david-dm.org/justmoon/node-extend#info=devDependencies

# yauzl

[![Build Status](https://travis-ci.org/thejoshwolfe/yauzl.svg?branch=master)](https://travis-ci.org/thejoshwolfe/yauzl)
[![Coverage Status](https://img.shields.io/coveralls/thejoshwolfe/yauzl.svg)](https://coveralls.io/r/thejoshwolfe/yauzl)

yet another unzip library for node. For zipping, see
[yazl](https://github.com/thejoshwolfe/yazl).

Design principles:

 * Follow the spec.
   Don't scan for local file headers.
   Read the central directory for file metadata.
   (see [No Streaming Unzip API](#no-streaming-unzip-api)).
 * Don't block the JavaScript thread.
   Use and provide async APIs.
 * Keep memory usage under control.
   Don't attempt to buffer entire files in RAM at once.
 * Never crash (if used properly).
   Don't let malformed zip files bring down client applications who are trying to catch errors.
 * Catch unsafe filenames entries.
   A zip file entry throws an error if its file name starts with `"/"` or `/[A-Za-z]:\//`
   or if it contains `".."` path segments or `"\\"` (per the spec).

## Usage

```js
var yauzl = require("yauzl");
var fs = require("fs");
var path = require("path");
var mkdirp = require("mkdirp"); // or similar

yauzl.open("path/to/file.zip", {lazyEntries: true}, function(err, zipfile) {
  if (err) throw err;
  zipfile.readEntry();
  zipfile.on("entry", function(entry) {
    if (/\/$/.test(entry.fileName)) {
      // directory file names end with '/'
      mkdirp(entry.fileName, function(err) {
        if (err) throw err;
        zipfile.readEntry();
      });
    } else {
      // file entry
      zipfile.openReadStream(entry, function(err, readStream) {
        if (err) throw err;
        // ensure parent directory exists
        mkdirp(path.dirname(entry.fileName), function(err) {
          if (err) throw err;
          readStream.pipe(fs.createWriteStream(entry.fileName));
          readStream.on("end", function() {
            zipfile.readEntry();
          });
        });
      });
    }
  });
});
```

## API

The default for every optional `callback` parameter is:

```js
function defaultCallback(err) {
  if (err) throw err;
}
```

### open(path, [options], [callback])

Calls `fs.open(path, "r")` and gives the `fd`, `options`, and `callback` to `fromFd()` below.

`options` may be omitted or `null`. The defaults are `{autoClose: true, lazyEntries: false}`.

`autoClose` is effectively equivalent to:

```js
zipfile.once("end", function() {
  zipfile.close();
});
```

`lazyEntries` indicates that entries should be read only when `readEntry()` is called.
If `lazyEntries` is `false`, `entry` events will be emitted as fast as possible to allow `pipe()`ing
file data from all entries in parallel.
This is not recommended, as it can lead to out of control memory usage for zip files with many entries.
See [issue #22](https://github.com/thejoshwolfe/yauzl/issues/22).
If `lazyEntries` is `true`, an `entry` or `end` event will be emitted in response to each call to `readEntry()`.
This allows processing of one entry at a time, and will keep memory usage under control for zip files with many entries.

### fromFd(fd, [options], [callback])

Reads from the fd, which is presumed to be an open .zip file.
Note that random access is required by the zip file specification,
so the fd cannot be an open socket or any other fd that does not support random access.

The `callback` is given the arguments `(err, zipfile)`.
An `err` is provided if the End of Central Directory Record Signature cannot be found in the file,
which indicates that the fd is not a zip file.
`zipfile` is an instance of `ZipFile`.

`options` may be omitted or `null`. The defaults are `{autoClose: false, lazyEntries: false}`.
See `open()` for the meaning of the options.

### fromBuffer(buffer, [options], [callback])

Like `fromFd()`, but reads from a RAM buffer instead of an open file.
`buffer` is a `Buffer`.
`callback` is effectively passed directly to `fromFd()`.

If a `ZipFile` is acquired from this method,
it will never emit the `close` event,
and calling `close()` is not necessary.

`options` may be omitted or `null`. The defaults are `{lazyEntries: false}`.
See `open()` for the meaning of the options.
The `autoClose` option is ignored for this method.

### fromRandomAccessReader(reader, totalSize, [options], [callback])

This method of creating a zip file allows clients to implement their own back-end file system.
For example, a client might translate read calls into network requests.

The `reader` parameter must be of a type that is a subclass of
[RandomAccessReader](#class-randomaccessreader) that implements the required methods.
The `totalSize` is a Number and indicates the total file size of the zip file.

`options` may be omitted or `null`. The defaults are `{autoClose: true, lazyEntries: false}`.
See `open()` for the meaning of the options.

### dosDateTimeToDate(date, time)

Converts MS-DOS `date` and `time` data into a JavaScript `Date` object.
Each parameter is a `Number` treated as an unsigned 16-bit integer.
Note that this format does not support timezones,
so the returned object will use the local timezone.

### Class: ZipFile

The constructor for the class is not part of the public API.
Use `open()`, `fromFd()`, `fromBuffer()`, or `fromRandomAccessReader()` instead.

#### Event: "entry"

Callback gets `(entry)`, which is an `Entry`.
See `open()` and `readEntry()` for when this event is emitted.

#### Event: "end"

Emitted after the last `entry` event has been emitted.
See `open()` and `readEntry()` for more info on when this event is emitted.

#### Event: "close"

Emitted after the fd is actually closed.
This is after calling `close()` (or after the `end` event when `autoClose` is `true`),
and after all stream pipelines created from `openReadStream()` have finished reading data from the fd.

If this `ZipFile` was acquired from `fromRandomAccessReader()`,
the "fd" in the previous paragraph refers to the `RandomAccessReader` implemented by the client.

If this `ZipFile` was acquired from `fromBuffer()`, this event is never emitted.

#### Event: "error"

Emitted in the case of errors with reading the zip file.
(Note that other errors can be emitted from the streams created from `openReadStream()` as well.)
After this event has been emitted, no further `entry`, `end`, or `error` events will be emitted,
but the `close` event may still be emitted.

#### readEntry()

Causes this `ZipFile` to emit an `entry` or `end` event (or an `error` event).
This method must only be called when this `ZipFile` was created with the `lazyEntries` option set to `true` (see `open()`).
When this `ZipFile` was created with the `lazyEntries` option set to `true`,
`entry` and `end` events are only ever emitted in response to this method call.

The event that is emitted in response to this method will not be emitted until after this method has returned,
so it is safe to call this method before attaching event listeners.

After calling this method, calling this method again before the response event has been emitted will cause undefined behavior.
Calling this method after the `end` event has been emitted will cause undefined behavior.
Calling this method after calling `close()` will cause undefined behavior.

#### openReadStream(entry, callback)

`entry` must be an `Entry` object from this `ZipFile`.
`callback` gets `(err, readStream)`, where `readStream` is a `Readable Stream`.
If the entry is compressed (with a supported compression method),
the read stream provides the decompressed data.
If this zipfile is already closed (see `close()`), the `callback` will receive an `err`.

It's possible for the `readStream` it to emit errors for several reasons.
For example, if zlib cannot decompress the data, the zlib error will be emitted from the `readStream`.
Two more error cases are if the decompressed data has too many or too few actual bytes
compared to the reported byte count from the entry's `uncompressedSize` field.
yauzl notices this false information and emits an error from the `readStream`
after some number of bytes have already been piped through the stream.

Because of this check, clients can always trust the `uncompressedSize` field in `Entry` objects.
Guarding against [zip bomb](http://en.wikipedia.org/wiki/Zip_bomb) attacks can be accomplished by
doing some heuristic checks on the size metadata and then watching out for the above errors.
Such heuristics are outside the scope of this library,
but enforcing the `uncompressedSize` is implemented here as a security feature.

It is possible to destroy the `readStream` before it has piped all of its data.
To do this, call `readStream.destroy()`.
You must `unpipe()` the `readStream` from any destination before calling `readStream.destroy()`.
If this zipfile was created using `fromRandomAccessReader()`, the `RandomAccessReader` implementation
must provide readable streams that implement a `.destroy()` method (see `randomAccessReader._readStreamForRange()`)
in order for calls to `readStream.destroy()` to work in this context.

#### close()

Causes all future calls to `openReadStream()` to fail,
and closes the fd after all streams created by `openReadStream()` have emitted their `end` events.

If the `autoClose` option is set to `true` (see `open()`),
this function will be called automatically effectively in response to this object's `end` event.

If the `lazyEntries` option is set to `false` (see `open()`) and this object's `end` event has not been emitted yet,
this function causes undefined behavior.
If the `lazyEntries` option is set to `true`,
you can call this function instead of calling `readEntry()` to abort reading the entries of a zipfile.

It is safe to call this function multiple times; after the first call, successive calls have no effect.
This includes situations where the `autoClose` option effectively calls this function for you.

#### isOpen

`Boolean`. `true` until `close()` is called; then it's `false`.

#### entryCount

`Number`. Total number of central directory records.

#### comment

`String`. Always decoded with `CP437` per the spec.

### Class: Entry

Objects of this class represent Central Directory Records.
Refer to the zipfile specification for more details about these fields.

These fields are of type `Number`:

 * `versionMadeBy`
 * `versionNeededToExtract`
 * `generalPurposeBitFlag`
 * `compressionMethod`
 * `lastModFileTime` (MS-DOS format, see `getLastModDateTime`)
 * `lastModFileDate` (MS-DOS format, see `getLastModDateTime`)
 * `crc32`
 * `compressedSize`
 * `uncompressedSize`
 * `fileNameLength` (bytes)
 * `extraFieldLength` (bytes)
 * `fileCommentLength` (bytes)
 * `internalFileAttributes`
 * `externalFileAttributes`
 * `relativeOffsetOfLocalHeader`

#### fileName

`String`.
Following the spec, the bytes for the file name are decoded with
`UTF-8` if `generalPurposeBitFlag & 0x800`, otherwise with `CP437`.

If `fileName` would contain unsafe characters, such as an absolute path or
a relative directory, yauzl emits an error instead of an entry.

#### extraFields

`Array` with each entry in the form `{id: id, data: data}`,
where `id` is a `Number` and `data` is a `Buffer`.
This library looks for and reads the ZIP64 Extended Information Extra Field (0x0001)
in order to support ZIP64 format zip files.
None of the other fields are considered significant by this library.

#### comment

`String` decoded with the same charset as used for `fileName`.

#### getLastModDate()

Effectively implemented as:

```js
return dosDateTimeToDate(this.lastModFileDate, this.lastModFileTime);
```

### Class: RandomAccessReader

This class is meant to be subclassed by clients and instantiated for the `fromRandomAccessReader()` function.

An example implementation can be found in `test/test.js`.

#### randomAccessReader._readStreamForRange(start, end)

Subclasses *must* implement this method.

`start` and `end` are Numbers and indicate byte offsets from the start of the file.
`end` is exclusive, so `_readStreamForRange(0x1000, 0x2000)` would indicate to read `0x1000` bytes.
`end - start` will always be at least `1`.

This method should return a readable stream which will be `pipe()`ed into another stream.
It is expected that the readable stream will provide data in several chunks if necessary.
If the readable stream provides too many or too few bytes, an error will be emitted.
Any errors emitted on the readable stream will be handled and re-emitted on the client-visible stream
(returned from `zipfile.openReadStream()`) or provided as the `err` argument to the appropriate callback
(for example, for `fromRandomAccessReader()`).

The returned stream *must* implement a method `.destroy()`
if you call `readStream.destroy()` on streams you get from `openReadStream()`.
If you never call `readStream.destroy()`, then streams returned from this method do not need to implement a method `.destroy()`.
`.destroy()` should abort any streaming that is in progress and clean up any associated resources.
`.destroy()` will only be called after the stream has been `unpipe()`d from its destination.

Note that the stream returned from this method might not be the same object that is provided by `openReadStream()`.
The stream returned from this method might be `pipe()`d through one or more filter streams (for example, a zlib inflate stream).

#### randomAccessReader.read(buffer, offset, length, position, callback)

Subclasses may implement this method.
The default implementation uses `createReadStream()` to fill the `buffer`.

This method should behave like `fs.read()`.

#### randomAccessReader.close(callback)

Subclasses may implement this method.
The default implementation is effectively `setImmediate(callback);`.

`callback` takes parameters `(err)`.

This method is called once the all streams returned from `_readStreamForRange()` have ended,
and no more `_readStreamForRange()` or `read()` requests will be issued to this object.

## How to Avoid Crashing

When a malformed zipfile is encountered, the default behavior is to crash (throw an exception).
If you want to handle errors more gracefully than this,
be sure to do the following:

 * Provide `callback` parameters where they are allowed, and check the `err` parameter.
 * Attach a listener for the `error` event on any `ZipFile` object you get from `open()`, `fromFd()`, `fromBuffer()`, or `fromRandomAccessReader()`.
 * Attach a listener for the `error` event on any stream you get from `openReadStream()`.

## Limitations

### No Streaming Unzip API

Due to the design of the .zip file format, it's impossible to interpret a .zip file from start to finish
(such as from a readable stream) without sacrificing correctness.
The Central Directory, which is the authority on the contents of the .zip file, is at the end of a .zip file, not the beginning.
A streaming API would need to either buffer the entire .zip file to get to the Central Directory before interpreting anything
(defeating the purpose of a streaming interface), or rely on the Local File Headers which are interspersed through the .zip file.
However, the Local File Headers are explicitly denounced in the spec as being unreliable copies of the Central Directory,
so trusting them would be a violation of the spec.

Any library that offers a streaming unzip API must make one of the above two compromises,
which makes the library either dishonest or nonconformant (usually the latter).
This library insists on correctness and adherence to the spec, and so does not offer a streaming API.

### Limitted ZIP64 Support

For ZIP64, only zip files smaller than `8PiB` are supported,
not the full `16EiB` range that a 64-bit integer should be able to index.
This is due to the JavaScript Number type being an IEEE 754 double precision float.

The Node.js `fs` module probably has this same limitation.

### ZIP64 Extensible Data Sector Is Ignored

The spec does not allow zip file creators to put arbitrary data here,
but rather reserves its use for PKWARE and mentions something about Z390.
This doesn't seem useful to expose in this library, so it is ignored.

### No Multi-Disk Archive Support

This library does not support multi-disk zip files.
The multi-disk fields in the zipfile spec were intended for a zip file to span multiple floppy disks,
which probably never happens now.
If the "number of this disk" field in the End of Central Directory Record is not `0`,
the `open()`, `fromFd()`, `fromBuffer()`, or `fromRandomAccessReader()` `callback` will receive an `err`.
By extension the following zip file fields are ignored by this library and not provided to clients:

 * Disk where central directory starts
 * Number of central directory records on this disk
 * Disk number where file starts

### No Encryption Support

Currently, the presence of encryption is not even checked,
and encrypted zip files will cause undefined behavior.

### Local File Headers Are Ignored

Many unzip libraries mistakenly read the Local File Header data in zip files.
This data is officially defined to be redundant with the Central Directory information,
and is not to be trusted.
Aside from checking the signature, yauzl ignores the content of the Local File Header.

### No CRC-32 Checking

This library provides the `crc32` field of `Entry` objects read from the Central Directory.
However, this field is not used for anything in this library.

### versionNeededToExtract Is Ignored

The field `versionNeededToExtract` is ignored,
because this library doesn't support the complete zip file spec at any version,

### No Support For Obscure Compression Methods

Regarding the `compressionMethod` field of `Entry` objects,
only method `0` (stored with no compression)
and method `8` (deflated) are supported.
Any of the other 15 official methods will cause the `openReadStream()` `callback` to receive an `err`.

### Data Descriptors Are Ignored

There may or may not be Data Descriptor sections in a zip file.
This library provides no support for finding or interpreting them.

### Archive Extra Data Record Is Ignored

There may or may not be an Archive Extra Data Record section in a zip file.
This library provides no support for finding or interpreting it.

### No Language Encoding Flag Support

Zip files officially support charset encodings other than CP437 and UTF-8,
but the zip file spec does not specify how it works.
This library makes no attempt to interpret the Language Encoding Flag.

## Change History

 * 2.4.1
   * Fix error handling.
 * 2.4.0
   * Add ZIP64 support. [issue #6](https://github.com/thejoshwolfe/yazl/issues/6)
   * Add `lazyEntries` option. [issue #22](https://github.com/thejoshwolfe/yazl/issues/22)
   * Add `readStream.destroy()` method. [issue #26](https://github.com/thejoshwolfe/yazl/issues/26)
   * Add `fromRandomAccessReader()`. [issue #14](https://github.com/thejoshwolfe/yazl/issues/14)
   * Add `examples/unzip.js`.
 * 2.3.1
   * Documentation updates.
 * 2.3.0
   * Check that `uncompressedSize` is correct, or else emit an error. [issue #13](https://github.com/thejoshwolfe/yazl/issues/13)
 * 2.2.1
   * Update dependencies.
 * 2.2.0
   * Update dependencies.
 * 2.1.0
   * Remove dependency on `iconv`.
 * 2.0.3
   * Fix crash when trying to read a 0-byte file.
 * 2.0.2
   * Fix event behavior after errors.
 * 2.0.1
   * Fix bug with using `iconv`.
 * 2.0.0
   * Initial release.
# debug
[![Build Status](https://travis-ci.org/visionmedia/debug.svg?branch=master)](https://travis-ci.org/visionmedia/debug)  [![Coverage Status](https://coveralls.io/repos/github/visionmedia/debug/badge.svg?branch=master)](https://coveralls.io/github/visionmedia/debug?branch=master)  [![Slack](https://visionmedia-community-slackin.now.sh/badge.svg)](https://visionmedia-community-slackin.now.sh/) [![OpenCollective](https://opencollective.com/debug/backers/badge.svg)](#backers) 
[![OpenCollective](https://opencollective.com/debug/sponsors/badge.svg)](#sponsors)



A tiny node.js debugging utility modelled after node core's debugging technique.

**Discussion around the V3 API is under way [here](https://github.com/visionmedia/debug/issues/370)**

## Installation

```bash
$ npm install debug
```

## Usage

`debug` exposes a function; simply pass this function the name of your module, and it will return a decorated version of `console.error` for you to pass debug statements to. This will allow you to toggle the debug output for different parts of your module as well as the module as a whole.

Example _app.js_:

```js
var debug = require('debug')('http')
  , http = require('http')
  , name = 'My App';

// fake app

debug('booting %s', name);

http.createServer(function(req, res){
  debug(req.method + ' ' + req.url);
  res.end('hello\n');
}).listen(3000, function(){
  debug('listening');
});

// fake worker of some kind

require('./worker');
```

Example _worker.js_:

```js
var debug = require('debug')('worker');

setInterval(function(){
  debug('doing some work');
}, 1000);
```

 The __DEBUG__ environment variable is then used to enable these based on space or comma-delimited names. Here are some examples:

  ![debug http and worker](http://f.cl.ly/items/18471z1H402O24072r1J/Screenshot.png)

  ![debug worker](http://f.cl.ly/items/1X413v1a3M0d3C2c1E0i/Screenshot.png)

#### Windows note

 On Windows the environment variable is set using the `set` command.

 ```cmd
 set DEBUG=*,-not_this
 ```

 Note that PowerShell uses different syntax to set environment variables.

 ```cmd
 $env:DEBUG = "*,-not_this"
  ```

Then, run the program to be debugged as usual.

## Millisecond diff

  When actively developing an application it can be useful to see when the time spent between one `debug()` call and the next. Suppose for example you invoke `debug()` before requesting a resource, and after as well, the "+NNNms" will show you how much time was spent between calls.

  ![](http://f.cl.ly/items/2i3h1d3t121M2Z1A3Q0N/Screenshot.png)

  When stdout is not a TTY, `Date#toUTCString()` is used, making it more useful for logging the debug information as shown below:

  ![](http://f.cl.ly/items/112H3i0e0o0P0a2Q2r11/Screenshot.png)

## Conventions

  If you're using this in one or more of your libraries, you _should_ use the name of your library so that developers may toggle debugging as desired without guessing names. If you have more than one debuggers you _should_ prefix them with your library name and use ":" to separate features. For example "bodyParser" from Connect would then be "connect:bodyParser".

## Wildcards

  The `*` character may be used as a wildcard. Suppose for example your library has debuggers named "connect:bodyParser", "connect:compress", "connect:session", instead of listing all three with `DEBUG=connect:bodyParser,connect:compress,connect:session`, you may simply do `DEBUG=connect:*`, or to run everything using this module simply use `DEBUG=*`.

  You can also exclude specific debuggers by prefixing them with a "-" character.  For example, `DEBUG=*,-connect:*` would include all debuggers except those starting with "connect:".

## Environment Variables

  When running through Node.js, you can set a few environment variables that will
  change the behavior of the debug logging:

| Name      | Purpose                                         |
|-----------|-------------------------------------------------|
| `DEBUG`   | Enables/disables specific debugging namespaces. |
| `DEBUG_COLORS`| Whether or not to use colors in the debug output. |
| `DEBUG_DEPTH` | Object inspection depth. |
| `DEBUG_SHOW_HIDDEN` | Shows hidden properties on inspected objects. |


  __Note:__ The environment variables beginning with `DEBUG_` end up being
  converted into an Options object that gets used with `%o`/`%O` formatters.
  See the Node.js documentation for
  [`util.inspect()`](https://nodejs.org/api/util.html#util_util_inspect_object_options)
  for the complete list.

## Formatters


  Debug uses [printf-style](https://wikipedia.org/wiki/Printf_format_string) formatting. Below are the officially supported formatters:

| Formatter | Representation |
|-----------|----------------|
| `%O`      | Pretty-print an Object on multiple lines. |
| `%o`      | Pretty-print an Object all on a single line. |
| `%s`      | String. |
| `%d`      | Number (both integer and float). |
| `%j`      | JSON. Replaced with the string '[Circular]' if the argument contains circular references. |
| `%%`      | Single percent sign ('%'). This does not consume an argument. |

### Custom formatters

  You can add custom formatters by extending the `debug.formatters` object. For example, if you wanted to add support for rendering a Buffer as hex with `%h`, you could do something like:

```js
const createDebug = require('debug')
createDebug.formatters.h = (v) => {
  return v.toString('hex')
}

// …elsewhere
const debug = createDebug('foo')
debug('this is hex: %h', new Buffer('hello world'))
//   foo this is hex: 68656c6c6f20776f726c6421 +0ms
```

## Browser support
  You can build a browser-ready script using [browserify](https://github.com/substack/node-browserify),
  or just use the [browserify-as-a-service](https://wzrd.in/) [build](https://wzrd.in/standalone/debug@latest),
  if you don't want to build it yourself.

  Debug's enable state is currently persisted by `localStorage`.
  Consider the situation shown below where you have `worker:a` and `worker:b`,
  and wish to debug both. You can enable this using `localStorage.debug`:

```js
localStorage.debug = 'worker:*'
```

And then refresh the page.

```js
a = debug('worker:a');
b = debug('worker:b');

setInterval(function(){
  a('doing some work');
}, 1000);

setInterval(function(){
  b('doing some work');
}, 1200);
```

#### Web Inspector Colors

  Colors are also enabled on "Web Inspectors" that understand the `%c` formatting
  option. These are WebKit web inspectors, Firefox ([since version
  31](https://hacks.mozilla.org/2014/05/editable-box-model-multiple-selection-sublime-text-keys-much-more-firefox-developer-tools-episode-31/))
  and the Firebug plugin for Firefox (any version).

  Colored output looks something like:

  ![](https://cloud.githubusercontent.com/assets/71256/3139768/b98c5fd8-e8ef-11e3-862a-f7253b6f47c6.png)


## Output streams

  By default `debug` will log to stderr, however this can be configured per-namespace by overriding the `log` method:

Example _stdout.js_:

```js
var debug = require('debug');
var error = debug('app:error');

// by default stderr is used
error('goes to stderr!');

var log = debug('app:log');
// set this namespace to log via console.log
log.log = console.log.bind(console); // don't forget to bind to console!
log('goes to stdout');
error('still goes to stderr!');

// set all output to go via console.info
// overrides all per-namespace log settings
debug.log = console.info.bind(console);
error('now goes to stdout via console.info');
log('still goes to stdout, but via console.info now');
```


## Authors

 - TJ Holowaychuk
 - Nathan Rajlich
 - Andrew Rhyne
 
## Backers

Support us with a monthly donation and help us continue our activities. [[Become a backer](https://opencollective.com/debug#backer)]

<a href="https://opencollective.com/debug/backer/0/website" target="_blank"><img src="https://opencollective.com/debug/backer/0/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/1/website" target="_blank"><img src="https://opencollective.com/debug/backer/1/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/2/website" target="_blank"><img src="https://opencollective.com/debug/backer/2/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/3/website" target="_blank"><img src="https://opencollective.com/debug/backer/3/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/4/website" target="_blank"><img src="https://opencollective.com/debug/backer/4/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/5/website" target="_blank"><img src="https://opencollective.com/debug/backer/5/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/6/website" target="_blank"><img src="https://opencollective.com/debug/backer/6/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/7/website" target="_blank"><img src="https://opencollective.com/debug/backer/7/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/8/website" target="_blank"><img src="https://opencollective.com/debug/backer/8/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/9/website" target="_blank"><img src="https://opencollective.com/debug/backer/9/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/10/website" target="_blank"><img src="https://opencollective.com/debug/backer/10/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/11/website" target="_blank"><img src="https://opencollective.com/debug/backer/11/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/12/website" target="_blank"><img src="https://opencollective.com/debug/backer/12/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/13/website" target="_blank"><img src="https://opencollective.com/debug/backer/13/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/14/website" target="_blank"><img src="https://opencollective.com/debug/backer/14/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/15/website" target="_blank"><img src="https://opencollective.com/debug/backer/15/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/16/website" target="_blank"><img src="https://opencollective.com/debug/backer/16/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/17/website" target="_blank"><img src="https://opencollective.com/debug/backer/17/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/18/website" target="_blank"><img src="https://opencollective.com/debug/backer/18/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/19/website" target="_blank"><img src="https://opencollective.com/debug/backer/19/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/20/website" target="_blank"><img src="https://opencollective.com/debug/backer/20/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/21/website" target="_blank"><img src="https://opencollective.com/debug/backer/21/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/22/website" target="_blank"><img src="https://opencollective.com/debug/backer/22/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/23/website" target="_blank"><img src="https://opencollective.com/debug/backer/23/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/24/website" target="_blank"><img src="https://opencollective.com/debug/backer/24/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/25/website" target="_blank"><img src="https://opencollective.com/debug/backer/25/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/26/website" target="_blank"><img src="https://opencollective.com/debug/backer/26/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/27/website" target="_blank"><img src="https://opencollective.com/debug/backer/27/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/28/website" target="_blank"><img src="https://opencollective.com/debug/backer/28/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/29/website" target="_blank"><img src="https://opencollective.com/debug/backer/29/avatar.svg"></a>


## Sponsors

Become a sponsor and get your logo on our README on Github with a link to your site. [[Become a sponsor](https://opencollective.com/debug#sponsor)]

<a href="https://opencollective.com/debug/sponsor/0/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/1/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/2/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/3/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/4/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/5/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/6/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/7/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/8/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/9/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/9/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/10/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/10/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/11/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/11/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/12/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/12/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/13/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/13/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/14/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/14/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/15/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/15/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/16/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/16/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/17/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/17/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/18/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/18/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/19/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/19/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/20/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/20/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/21/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/21/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/22/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/22/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/23/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/23/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/24/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/24/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/25/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/25/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/26/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/26/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/27/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/27/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/28/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/28/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/29/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/29/avatar.svg"></a>

## License

(The MIT License)

Copyright (c) 2014-2016 TJ Holowaychuk &lt;tj@vision-media.ca&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# nice-try

[![Travis Build Status](https://travis-ci.org/electerious/nice-try.svg?branch=master)](https://travis-ci.org/electerious/nice-try) [![AppVeyor Status](https://ci.appveyor.com/api/projects/status/8tqb09wrwci3xf8l?svg=true)](https://ci.appveyor.com/project/electerious/nice-try) [![Coverage Status](https://coveralls.io/repos/github/electerious/nice-try/badge.svg?branch=master)](https://coveralls.io/github/electerious/nice-try?branch=master) [![Dependencies](https://david-dm.org/electerious/nice-try.svg)](https://david-dm.org/electerious/nice-try#info=dependencies) [![Greenkeeper badge](https://badges.greenkeeper.io/electerious/nice-try.svg)](https://greenkeeper.io/)

A function that tries to execute a function and discards any error that occurs.

## Install

```
npm install nice-try
```

## Usage

```js
const niceTry = require('nice-try')

niceTry(() => JSON.parse('true')) // true
niceTry(() => JSON.parse('truee')) // undefined
niceTry() // undefined
niceTry(true) // undefined
```

## API

### Parameters

- `fn` `{Function}` Function that might or might not throw an error.

### Returns

- `{?*}` Return-value of the function when no error occurred.
# Request - Simplified HTTP client

[![npm package](https://nodei.co/npm/request.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/request/)

[![Build status](https://img.shields.io/travis/request/request/master.svg?style=flat-square)](https://travis-ci.org/request/request)
[![Coverage](https://img.shields.io/codecov/c/github/request/request.svg?style=flat-square)](https://codecov.io/github/request/request?branch=master)
[![Coverage](https://img.shields.io/coveralls/request/request.svg?style=flat-square)](https://coveralls.io/r/request/request)
[![Dependency Status](https://img.shields.io/david/request/request.svg?style=flat-square)](https://david-dm.org/request/request)
[![Known Vulnerabilities](https://snyk.io/test/npm/request/badge.svg?style=flat-square)](https://snyk.io/test/npm/request)
[![Gitter](https://img.shields.io/badge/gitter-join_chat-blue.svg?style=flat-square)](https://gitter.im/request/request?utm_source=badge)


## Super simple to use

Request is designed to be the simplest way possible to make http calls. It supports HTTPS and follows redirects by default.

```js
var request = require('request');
request('http://www.google.com', function (error, response, body) {
  console.log('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the HTML for the Google homepage.
});
```


## Table of contents

- [Streaming](#streaming)
- [Promises & Async/Await](#promises--asyncawait)
- [Forms](#forms)
- [HTTP Authentication](#http-authentication)
- [Custom HTTP Headers](#custom-http-headers)
- [OAuth Signing](#oauth-signing)
- [Proxies](#proxies)
- [Unix Domain Sockets](#unix-domain-sockets)
- [TLS/SSL Protocol](#tlsssl-protocol)
- [Support for HAR 1.2](#support-for-har-12)
- [**All Available Options**](#requestoptions-callback)

Request also offers [convenience methods](#convenience-methods) like
`request.defaults` and `request.post`, and there are
lots of [usage examples](#examples) and several
[debugging techniques](#debugging).


---


## Streaming

You can stream any response to a file stream.

```js
request('http://google.com/doodle.png').pipe(fs.createWriteStream('doodle.png'))
```

You can also stream a file to a PUT or POST request. This method will also check the file extension against a mapping of file extensions to content-types (in this case `application/json`) and use the proper `content-type` in the PUT request (if the headers don’t already provide one).

```js
fs.createReadStream('file.json').pipe(request.put('http://mysite.com/obj.json'))
```

Request can also `pipe` to itself. When doing so, `content-type` and `content-length` are preserved in the PUT headers.

```js
request.get('http://google.com/img.png').pipe(request.put('http://mysite.com/img.png'))
```

Request emits a "response" event when a response is received. The `response` argument will be an instance of [http.IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage).

```js
request
  .get('http://google.com/img.png')
  .on('response', function(response) {
    console.log(response.statusCode) // 200
    console.log(response.headers['content-type']) // 'image/png'
  })
  .pipe(request.put('http://mysite.com/img.png'))
```

To easily handle errors when streaming requests, listen to the `error` event before piping:

```js
request
  .get('http://mysite.com/doodle.png')
  .on('error', function(err) {
    console.log(err)
  })
  .pipe(fs.createWriteStream('doodle.png'))
```

Now let’s get fancy.

```js
http.createServer(function (req, resp) {
  if (req.url === '/doodle.png') {
    if (req.method === 'PUT') {
      req.pipe(request.put('http://mysite.com/doodle.png'))
    } else if (req.method === 'GET' || req.method === 'HEAD') {
      request.get('http://mysite.com/doodle.png').pipe(resp)
    }
  }
})
```

You can also `pipe()` from `http.ServerRequest` instances, as well as to `http.ServerResponse` instances. The HTTP method, headers, and entity-body data will be sent. Which means that, if you don't really care about security, you can do:

```js
http.createServer(function (req, resp) {
  if (req.url === '/doodle.png') {
    var x = request('http://mysite.com/doodle.png')
    req.pipe(x)
    x.pipe(resp)
  }
})
```

And since `pipe()` returns the destination stream in ≥ Node 0.5.x you can do one line proxying. :)

```js
req.pipe(request('http://mysite.com/doodle.png')).pipe(resp)
```

Also, none of this new functionality conflicts with requests previous features, it just expands them.

```js
var r = request.defaults({'proxy':'http://localproxy.com'})

http.createServer(function (req, resp) {
  if (req.url === '/doodle.png') {
    r.get('http://google.com/doodle.png').pipe(resp)
  }
})
```

You can still use intermediate proxies, the requests will still follow HTTP forwards, etc.

[back to top](#table-of-contents)


---


## Promises & Async/Await

`request` supports both streaming and callback interfaces natively. If you'd like `request` to return a Promise instead, you can use an alternative interface wrapper for `request`. These wrappers can be useful if you prefer to work with Promises, or if you'd like to use `async`/`await` in ES2017.

Several alternative interfaces are provided by the request team, including:
- [`request-promise`](https://github.com/request/request-promise) (uses [Bluebird](https://github.com/petkaantonov/bluebird) Promises)
- [`request-promise-native`](https://github.com/request/request-promise-native) (uses native Promises)
- [`request-promise-any`](https://github.com/request/request-promise-any) (uses [any-promise](https://www.npmjs.com/package/any-promise) Promises)


[back to top](#table-of-contents)


---


## Forms

`request` supports `application/x-www-form-urlencoded` and `multipart/form-data` form uploads. For `multipart/related` refer to the `multipart` API.


#### application/x-www-form-urlencoded (URL-Encoded Forms)

URL-encoded forms are simple.

```js
request.post('http://service.com/upload', {form:{key:'value'}})
// or
request.post('http://service.com/upload').form({key:'value'})
// or
request.post({url:'http://service.com/upload', form: {key:'value'}}, function(err,httpResponse,body){ /* ... */ })
```


#### multipart/form-data (Multipart Form Uploads)

For `multipart/form-data` we use the [form-data](https://github.com/form-data/form-data) library by [@felixge](https://github.com/felixge). For the most cases, you can pass your upload form data via the `formData` option.


```js
var formData = {
  // Pass a simple key-value pair
  my_field: 'my_value',
  // Pass data via Buffers
  my_buffer: Buffer.from([1, 2, 3]),
  // Pass data via Streams
  my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
  // Pass multiple values /w an Array
  attachments: [
    fs.createReadStream(__dirname + '/attachment1.jpg'),
    fs.createReadStream(__dirname + '/attachment2.jpg')
  ],
  // Pass optional meta-data with an 'options' object with style: {value: DATA, options: OPTIONS}
  // Use case: for some types of streams, you'll need to provide "file"-related information manually.
  // See the `form-data` README for more information about options: https://github.com/form-data/form-data
  custom_file: {
    value:  fs.createReadStream('/dev/urandom'),
    options: {
      filename: 'topsecret.jpg',
      contentType: 'image/jpeg'
    }
  }
};
request.post({url:'http://service.com/upload', formData: formData}, function optionalCallback(err, httpResponse, body) {
  if (err) {
    return console.error('upload failed:', err);
  }
  console.log('Upload successful!  Server responded with:', body);
});
```

For advanced cases, you can access the form-data object itself via `r.form()`. This can be modified until the request is fired on the next cycle of the event-loop. (Note that this calling `form()` will clear the currently set form data for that request.)

```js
// NOTE: Advanced use-case, for normal use see 'formData' usage above
var r = request.post('http://service.com/upload', function optionalCallback(err, httpResponse, body) {...})
var form = r.form();
form.append('my_field', 'my_value');
form.append('my_buffer', Buffer.from([1, 2, 3]));
form.append('custom_file', fs.createReadStream(__dirname + '/unicycle.jpg'), {filename: 'unicycle.jpg'});
```
See the [form-data README](https://github.com/form-data/form-data) for more information & examples.


#### multipart/related

Some variations in different HTTP implementations require a newline/CRLF before, after, or both before and after the boundary of a `multipart/related` request (using the multipart option). This has been observed in the .NET WebAPI version 4.0. You can turn on a boundary preambleCRLF or postamble by passing them as `true` to your request options.

```js
  request({
    method: 'PUT',
    preambleCRLF: true,
    postambleCRLF: true,
    uri: 'http://service.com/upload',
    multipart: [
      {
        'content-type': 'application/json',
        body: JSON.stringify({foo: 'bar', _attachments: {'message.txt': {follows: true, length: 18, 'content_type': 'text/plain' }}})
      },
      { body: 'I am an attachment' },
      { body: fs.createReadStream('image.png') }
    ],
    // alternatively pass an object containing additional options
    multipart: {
      chunked: false,
      data: [
        {
          'content-type': 'application/json',
          body: JSON.stringify({foo: 'bar', _attachments: {'message.txt': {follows: true, length: 18, 'content_type': 'text/plain' }}})
        },
        { body: 'I am an attachment' }
      ]
    }
  },
  function (error, response, body) {
    if (error) {
      return console.error('upload failed:', error);
    }
    console.log('Upload successful!  Server responded with:', body);
  })
```

[back to top](#table-of-contents)


---


## HTTP Authentication

```js
request.get('http://some.server.com/').auth('username', 'password', false);
// or
request.get('http://some.server.com/', {
  'auth': {
    'user': 'username',
    'pass': 'password',
    'sendImmediately': false
  }
});
// or
request.get('http://some.server.com/').auth(null, null, true, 'bearerToken');
// or
request.get('http://some.server.com/', {
  'auth': {
    'bearer': 'bearerToken'
  }
});
```

If passed as an option, `auth` should be a hash containing values:

- `user` || `username`
- `pass` || `password`
- `sendImmediately` (optional)
- `bearer` (optional)

The method form takes parameters
`auth(username, password, sendImmediately, bearer)`.

`sendImmediately` defaults to `true`, which causes a basic or bearer
authentication header to be sent. If `sendImmediately` is `false`, then
`request` will retry with a proper authentication header after receiving a
`401` response from the server (which must contain a `WWW-Authenticate` header
indicating the required authentication method).

Note that you can also specify basic authentication using the URL itself, as
detailed in [RFC 1738](http://www.ietf.org/rfc/rfc1738.txt). Simply pass the
`user:password` before the host with an `@` sign:

```js
var username = 'username',
    password = 'password',
    url = 'http://' + username + ':' + password + '@some.server.com';

request({url: url}, function (error, response, body) {
   // Do more stuff with 'body' here
});
```

Digest authentication is supported, but it only works with `sendImmediately`
set to `false`; otherwise `request` will send basic authentication on the
initial request, which will probably cause the request to fail.

Bearer authentication is supported, and is activated when the `bearer` value is
available. The value may be either a `String` or a `Function` returning a
`String`. Using a function to supply the bearer token is particularly useful if
used in conjunction with `defaults` to allow a single function to supply the
last known token at the time of sending a request, or to compute one on the fly.

[back to top](#table-of-contents)


---


## Custom HTTP Headers

HTTP Headers, such as `User-Agent`, can be set in the `options` object.
In the example below, we call the github API to find out the number
of stars and forks for the request repository. This requires a
custom `User-Agent` header as well as https.

```js
var request = require('request');

var options = {
  url: 'https://api.github.com/repos/request/request',
  headers: {
    'User-Agent': 'request'
  }
};

function callback(error, response, body) {
  if (!error && response.statusCode == 200) {
    var info = JSON.parse(body);
    console.log(info.stargazers_count + " Stars");
    console.log(info.forks_count + " Forks");
  }
}

request(options, callback);
```

[back to top](#table-of-contents)


---


## OAuth Signing

[OAuth version 1.0](https://tools.ietf.org/html/rfc5849) is supported. The
default signing algorithm is
[HMAC-SHA1](https://tools.ietf.org/html/rfc5849#section-3.4.2):

```js
// OAuth1.0 - 3-legged server side flow (Twitter example)
// step 1
var qs = require('querystring')
  , oauth =
    { callback: 'http://mysite.com/callback/'
    , consumer_key: CONSUMER_KEY
    , consumer_secret: CONSUMER_SECRET
    }
  , url = 'https://api.twitter.com/oauth/request_token'
  ;
request.post({url:url, oauth:oauth}, function (e, r, body) {
  // Ideally, you would take the body in the response
  // and construct a URL that a user clicks on (like a sign in button).
  // The verifier is only available in the response after a user has
  // verified with twitter that they are authorizing your app.

  // step 2
  var req_data = qs.parse(body)
  var uri = 'https://api.twitter.com/oauth/authenticate'
    + '?' + qs.stringify({oauth_token: req_data.oauth_token})
  // redirect the user to the authorize uri

  // step 3
  // after the user is redirected back to your server
  var auth_data = qs.parse(body)
    , oauth =
      { consumer_key: CONSUMER_KEY
      , consumer_secret: CONSUMER_SECRET
      , token: auth_data.oauth_token
      , token_secret: req_data.oauth_token_secret
      , verifier: auth_data.oauth_verifier
      }
    , url = 'https://api.twitter.com/oauth/access_token'
    ;
  request.post({url:url, oauth:oauth}, function (e, r, body) {
    // ready to make signed requests on behalf of the user
    var perm_data = qs.parse(body)
      , oauth =
        { consumer_key: CONSUMER_KEY
        , consumer_secret: CONSUMER_SECRET
        , token: perm_data.oauth_token
        , token_secret: perm_data.oauth_token_secret
        }
      , url = 'https://api.twitter.com/1.1/users/show.json'
      , qs =
        { screen_name: perm_data.screen_name
        , user_id: perm_data.user_id
        }
      ;
    request.get({url:url, oauth:oauth, qs:qs, json:true}, function (e, r, user) {
      console.log(user)
    })
  })
})
```

For [RSA-SHA1 signing](https://tools.ietf.org/html/rfc5849#section-3.4.3), make
the following changes to the OAuth options object:
* Pass `signature_method : 'RSA-SHA1'`
* Instead of `consumer_secret`, specify a `private_key` string in
  [PEM format](http://how2ssl.com/articles/working_with_pem_files/)

For [PLAINTEXT signing](http://oauth.net/core/1.0/#anchor22), make
the following changes to the OAuth options object:
* Pass `signature_method : 'PLAINTEXT'`

To send OAuth parameters via query params or in a post body as described in The
[Consumer Request Parameters](http://oauth.net/core/1.0/#consumer_req_param)
section of the oauth1 spec:
* Pass `transport_method : 'query'` or `transport_method : 'body'` in the OAuth
  options object.
* `transport_method` defaults to `'header'`

To use [Request Body Hash](https://oauth.googlecode.com/svn/spec/ext/body_hash/1.0/oauth-bodyhash.html) you can either
* Manually generate the body hash and pass it as a string `body_hash: '...'`
* Automatically generate the body hash by passing `body_hash: true`

[back to top](#table-of-contents)


---


## Proxies

If you specify a `proxy` option, then the request (and any subsequent
redirects) will be sent via a connection to the proxy server.

If your endpoint is an `https` url, and you are using a proxy, then
request will send a `CONNECT` request to the proxy server *first*, and
then use the supplied connection to connect to the endpoint.

That is, first it will make a request like:

```
HTTP/1.1 CONNECT endpoint-server.com:80
Host: proxy-server.com
User-Agent: whatever user agent you specify
```

and then the proxy server make a TCP connection to `endpoint-server`
on port `80`, and return a response that looks like:

```
HTTP/1.1 200 OK
```

At this point, the connection is left open, and the client is
communicating directly with the `endpoint-server.com` machine.

See [the wikipedia page on HTTP Tunneling](https://en.wikipedia.org/wiki/HTTP_tunnel)
for more information.

By default, when proxying `http` traffic, request will simply make a
standard proxied `http` request. This is done by making the `url`
section of the initial line of the request a fully qualified url to
the endpoint.

For example, it will make a single request that looks like:

```
HTTP/1.1 GET http://endpoint-server.com/some-url
Host: proxy-server.com
Other-Headers: all go here

request body or whatever
```

Because a pure "http over http" tunnel offers no additional security
or other features, it is generally simpler to go with a
straightforward HTTP proxy in this case. However, if you would like
to force a tunneling proxy, you may set the `tunnel` option to `true`.

You can also make a standard proxied `http` request by explicitly setting
`tunnel : false`, but **note that this will allow the proxy to see the traffic
to/from the destination server**.

If you are using a tunneling proxy, you may set the
`proxyHeaderWhiteList` to share certain headers with the proxy.

You can also set the `proxyHeaderExclusiveList` to share certain
headers only with the proxy and not with destination host.

By default, this set is:

```
accept
accept-charset
accept-encoding
accept-language
accept-ranges
cache-control
content-encoding
content-language
content-length
content-location
content-md5
content-range
content-type
connection
date
expect
max-forwards
pragma
proxy-authorization
referer
te
transfer-encoding
user-agent
via
```

Note that, when using a tunneling proxy, the `proxy-authorization`
header and any headers from custom `proxyHeaderExclusiveList` are
*never* sent to the endpoint server, but only to the proxy server.


### Controlling proxy behaviour using environment variables

The following environment variables are respected by `request`:

 * `HTTP_PROXY` / `http_proxy`
 * `HTTPS_PROXY` / `https_proxy`
 * `NO_PROXY` / `no_proxy`

When `HTTP_PROXY` / `http_proxy` are set, they will be used to proxy non-SSL requests that do not have an explicit `proxy` configuration option present. Similarly, `HTTPS_PROXY` / `https_proxy` will be respected for SSL requests that do not have an explicit `proxy` configuration option. It is valid to define a proxy in one of the environment variables, but then override it for a specific request, using the `proxy` configuration option. Furthermore, the `proxy` configuration option can be explicitly set to false / null to opt out of proxying altogether for that request.

`request` is also aware of the `NO_PROXY`/`no_proxy` environment variables. These variables provide a granular way to opt out of proxying, on a per-host basis. It should contain a comma separated list of hosts to opt out of proxying. It is also possible to opt of proxying when a particular destination port is used. Finally, the variable may be set to `*` to opt out of the implicit proxy configuration of the other environment variables.

Here's some examples of valid `no_proxy` values:

 * `google.com` - don't proxy HTTP/HTTPS requests to Google.
 * `google.com:443` - don't proxy HTTPS requests to Google, but *do* proxy HTTP requests to Google.
 * `google.com:443, yahoo.com:80` - don't proxy HTTPS requests to Google, and don't proxy HTTP requests to Yahoo!
 * `*` - ignore `https_proxy`/`http_proxy` environment variables altogether.

[back to top](#table-of-contents)


---


## UNIX Domain Sockets

`request` supports making requests to [UNIX Domain Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket). To make one, use the following URL scheme:

```js
/* Pattern */ 'http://unix:SOCKET:PATH'
/* Example */ request.get('http://unix:/absolute/path/to/unix.socket:/request/path')
```

Note: The `SOCKET` path is assumed to be absolute to the root of the host file system.

[back to top](#table-of-contents)


---


## TLS/SSL Protocol

TLS/SSL Protocol options, such as `cert`, `key` and `passphrase`, can be
set directly in `options` object, in the `agentOptions` property of the `options` object, or even in `https.globalAgent.options`. Keep in mind that, although `agentOptions` allows for a slightly wider range of configurations, the recommended way is via `options` object directly, as using `agentOptions` or `https.globalAgent.options` would not be applied in the same way in proxied environments (as data travels through a TLS connection instead of an http/https agent).

```js
var fs = require('fs')
    , path = require('path')
    , certFile = path.resolve(__dirname, 'ssl/client.crt')
    , keyFile = path.resolve(__dirname, 'ssl/client.key')
    , caFile = path.resolve(__dirname, 'ssl/ca.cert.pem')
    , request = require('request');

var options = {
    url: 'https://api.some-server.com/',
    cert: fs.readFileSync(certFile),
    key: fs.readFileSync(keyFile),
    passphrase: 'password',
    ca: fs.readFileSync(caFile)
};

request.get(options);
```

### Using `options.agentOptions`

In the example below, we call an API that requires client side SSL certificate
(in PEM format) with passphrase protected private key (in PEM format) and disable the SSLv3 protocol:

```js
var fs = require('fs')
    , path = require('path')
    , certFile = path.resolve(__dirname, 'ssl/client.crt')
    , keyFile = path.resolve(__dirname, 'ssl/client.key')
    , request = require('request');

var options = {
    url: 'https://api.some-server.com/',
    agentOptions: {
        cert: fs.readFileSync(certFile),
        key: fs.readFileSync(keyFile),
        // Or use `pfx` property replacing `cert` and `key` when using private key, certificate and CA certs in PFX or PKCS12 format:
        // pfx: fs.readFileSync(pfxFilePath),
        passphrase: 'password',
        securityOptions: 'SSL_OP_NO_SSLv3'
    }
};

request.get(options);
```

It is able to force using SSLv3 only by specifying `secureProtocol`:

```js
request.get({
    url: 'https://api.some-server.com/',
    agentOptions: {
        secureProtocol: 'SSLv3_method'
    }
});
```

It is possible to accept other certificates than those signed by generally allowed Certificate Authorities (CAs).
This can be useful, for example,  when using self-signed certificates.
To require a different root certificate, you can specify the signing CA by adding the contents of the CA's certificate file to the `agentOptions`.
The certificate the domain presents must be signed by the root certificate specified:

```js
request.get({
    url: 'https://api.some-server.com/',
    agentOptions: {
        ca: fs.readFileSync('ca.cert.pem')
    }
});
```

[back to top](#table-of-contents)


---

## Support for HAR 1.2

The `options.har` property will override the values: `url`, `method`, `qs`, `headers`, `form`, `formData`, `body`, `json`, as well as construct multipart data and read files from disk when `request.postData.params[].fileName` is present without a matching `value`.

A validation step will check if the HAR Request format matches the latest spec (v1.2) and will skip parsing if not matching.

```js
  var request = require('request')
  request({
    // will be ignored
    method: 'GET',
    uri: 'http://www.google.com',

    // HTTP Archive Request Object
    har: {
      url: 'http://www.mockbin.com/har',
      method: 'POST',
      headers: [
        {
          name: 'content-type',
          value: 'application/x-www-form-urlencoded'
        }
      ],
      postData: {
        mimeType: 'application/x-www-form-urlencoded',
        params: [
          {
            name: 'foo',
            value: 'bar'
          },
          {
            name: 'hello',
            value: 'world'
          }
        ]
      }
    }
  })

  // a POST request will be sent to http://www.mockbin.com
  // with body an application/x-www-form-urlencoded body:
  // foo=bar&hello=world
```

[back to top](#table-of-contents)


---

## request(options, callback)

The first argument can be either a `url` or an `options` object. The only required option is `uri`; all others are optional.

- `uri` || `url` - fully qualified uri or a parsed url object from `url.parse()`
- `baseUrl` - fully qualified uri string used as the base url. Most useful with `request.defaults`, for example when you want to do many requests to the same domain. If `baseUrl` is `https://example.com/api/`, then requesting `/end/point?test=true` will fetch `https://example.com/api/end/point?test=true`. When `baseUrl` is given, `uri` must also be a string.
- `method` - http method (default: `"GET"`)
- `headers` - http headers (default: `{}`)

---

- `qs` - object containing querystring values to be appended to the `uri`
- `qsParseOptions` - object containing options to pass to the [qs.parse](https://github.com/hapijs/qs#parsing-objects) method. Alternatively pass options to the [querystring.parse](https://nodejs.org/docs/v0.12.0/api/querystring.html#querystring_querystring_parse_str_sep_eq_options) method using this format `{sep:';', eq:':', options:{}}`
- `qsStringifyOptions` - object containing options to pass to the [qs.stringify](https://github.com/hapijs/qs#stringifying) method. Alternatively pass options to the  [querystring.stringify](https://nodejs.org/docs/v0.12.0/api/querystring.html#querystring_querystring_stringify_obj_sep_eq_options) method using this format `{sep:';', eq:':', options:{}}`. For example, to change the way arrays are converted to query strings using the `qs` module pass the `arrayFormat` option with one of `indices|brackets|repeat`
- `useQuerystring` - if true, use `querystring` to stringify and parse
  querystrings, otherwise use `qs` (default: `false`). Set this option to
  `true` if you need arrays to be serialized as `foo=bar&foo=baz` instead of the
  default `foo[0]=bar&foo[1]=baz`.

---

- `body` - entity body for PATCH, POST and PUT requests. Must be a `Buffer`, `String` or `ReadStream`. If `json` is `true`, then `body` must be a JSON-serializable object.
- `form` - when passed an object or a querystring, this sets `body` to a querystring representation of value, and adds `Content-type: application/x-www-form-urlencoded` header. When passed no options, a `FormData` instance is returned (and is piped to request). See "Forms" section above.
- `formData` - data to pass for a `multipart/form-data` request. See
  [Forms](#forms) section above.
- `multipart` - array of objects which contain their own headers and `body`
  attributes. Sends a `multipart/related` request. See [Forms](#forms) section
  above.
  - Alternatively you can pass in an object `{chunked: false, data: []}` where
    `chunked` is used to specify whether the request is sent in
    [chunked transfer encoding](https://en.wikipedia.org/wiki/Chunked_transfer_encoding)
    In non-chunked requests, data items with body streams are not allowed.
- `preambleCRLF` - append a newline/CRLF before the boundary of your `multipart/form-data` request.
- `postambleCRLF` - append a newline/CRLF at the end of the boundary of your `multipart/form-data` request.
- `json` - sets `body` to JSON representation of value and adds `Content-type: application/json` header. Additionally, parses the response body as JSON.
- `jsonReviver` - a [reviver function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) that will be passed to `JSON.parse()` when parsing a JSON response body.
- `jsonReplacer` - a [replacer function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) that will be passed to `JSON.stringify()` when stringifying a JSON request body.

---

- `auth` - a hash containing values `user` || `username`, `pass` || `password`, and `sendImmediately` (optional). See documentation above.
- `oauth` - options for OAuth HMAC-SHA1 signing. See documentation above.
- `hawk` - options for [Hawk signing](https://github.com/hueniverse/hawk). The `credentials` key must contain the necessary signing info, [see hawk docs for details](https://github.com/hueniverse/hawk#usage-example).
- `aws` - `object` containing AWS signing information. Should have the properties `key`, `secret`, and optionally `session` (note that this only works for services that require session as part of the canonical string). Also requires the property `bucket`, unless you’re specifying your `bucket` as part of the path, or the request doesn’t use a bucket (i.e. GET Services). If you want to use AWS sign version 4 use the parameter `sign_version` with value `4` otherwise the default is version 2. **Note:** you need to `npm install aws4` first.
- `httpSignature` - options for the [HTTP Signature Scheme](https://github.com/joyent/node-http-signature/blob/master/http_signing.md) using [Joyent's library](https://github.com/joyent/node-http-signature). The `keyId` and `key` properties must be specified. See the docs for other options.

---

- `followRedirect` - follow HTTP 3xx responses as redirects (default: `true`). This property can also be implemented as function which gets `response` object as a single argument and should return `true` if redirects should continue or `false` otherwise.
- `followAllRedirects` - follow non-GET HTTP 3xx responses as redirects (default: `false`)
- `followOriginalHttpMethod` - by default we redirect to HTTP method GET. you can enable this property to redirect to the original HTTP method (default: `false`)
- `maxRedirects` - the maximum number of redirects to follow (default: `10`)
- `removeRefererHeader` - removes the referer header when a redirect happens (default: `false`). **Note:** if true, referer header set in the initial request is preserved during redirect chain.

---

- `encoding` - encoding to be used on `setEncoding` of response data. If `null`, the `body` is returned as a `Buffer`. Anything else **(including the default value of `undefined`)** will be passed as the [encoding](http://nodejs.org/api/buffer.html#buffer_buffer) parameter to `toString()` (meaning this is effectively `utf8` by default). (**Note:** if you expect binary data, you should set `encoding: null`.)
- `gzip` - if `true`, add an `Accept-Encoding` header to request compressed content encodings from the server (if not already present) and decode supported content encodings in the response. **Note:** Automatic decoding of the response content is performed on the body data returned through `request` (both through the `request` stream and passed to the callback function) but is not performed on the `response` stream (available from the `response` event) which is the unmodified `http.IncomingMessage` object which may contain compressed data. See example below.
- `jar` - if `true`, remember cookies for future use (or define your custom cookie jar; see examples section)

---

- `agent` - `http(s).Agent` instance to use
- `agentClass` - alternatively specify your agent's class name
- `agentOptions` - and pass its options. **Note:** for HTTPS see [tls API doc for TLS/SSL options](http://nodejs.org/api/tls.html#tls_tls_connect_options_callback) and the [documentation above](#using-optionsagentoptions).
- `forever` - set to `true` to use the [forever-agent](https://github.com/request/forever-agent) **Note:** Defaults to `http(s).Agent({keepAlive:true})` in node 0.12+
- `pool` - an object describing which agents to use for the request. If this option is omitted the request will use the global agent (as long as your options allow for it). Otherwise, request will search the pool for your custom agent. If no custom agent is found, a new agent will be created and added to the pool. **Note:** `pool` is used only when the `agent` option is not specified.
  - A `maxSockets` property can also be provided on the `pool` object to set the max number of sockets for all agents created (ex: `pool: {maxSockets: Infinity}`).
  - Note that if you are sending multiple requests in a loop and creating
    multiple new `pool` objects, `maxSockets` will not work as intended. To
    work around this, either use [`request.defaults`](#requestdefaultsoptions)
    with your pool options or create the pool object with the `maxSockets`
    property outside of the loop.
- `timeout` - integer containing the number of milliseconds to wait for a
server to send response headers (and start the response body) before aborting
the request. Note that if the underlying TCP connection cannot be established,
the OS-wide TCP connection timeout will overrule the `timeout` option ([the
default in Linux can be anywhere from 20-120 seconds][linux-timeout]).

[linux-timeout]: http://www.sekuda.com/overriding_the_default_linux_kernel_20_second_tcp_socket_connect_timeout

---

- `localAddress` - local interface to bind for network connections.
- `proxy` - an HTTP proxy to be used. Supports proxy Auth with Basic Auth, identical to support for the `url` parameter (by embedding the auth info in the `uri`)
- `strictSSL` - if `true`, requires SSL certificates be valid. **Note:** to use your own certificate authority, you need to specify an agent that was created with that CA as an option.
- `tunnel` - controls the behavior of
  [HTTP `CONNECT` tunneling](https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_tunneling)
  as follows:
   - `undefined` (default) - `true` if the destination is `https`, `false` otherwise
   - `true` - always tunnel to the destination by making a `CONNECT` request to
     the proxy
   - `false` - request the destination as a `GET` request.
- `proxyHeaderWhiteList` - a whitelist of headers to send to a
  tunneling proxy.
- `proxyHeaderExclusiveList` - a whitelist of headers to send
  exclusively to a tunneling proxy and not to destination.

---

- `time` - if `true`, the request-response cycle (including all redirects) is timed at millisecond resolution. When set, the following properties are added to the response object:
  - `elapsedTime` Duration of the entire request/response in milliseconds (*deprecated*).
  - `responseStartTime` Timestamp when the response began (in Unix Epoch milliseconds) (*deprecated*).
  - `timingStart` Timestamp of the start of the request (in Unix Epoch milliseconds).
  - `timings` Contains event timestamps in millisecond resolution relative to `timingStart`. If there were redirects, the properties reflect the timings of the final request in the redirect chain:
    - `socket` Relative timestamp when the [`http`](https://nodejs.org/api/http.html#http_event_socket) module's `socket` event fires. This happens when the socket is assigned to the request.
    - `lookup` Relative timestamp when the [`net`](https://nodejs.org/api/net.html#net_event_lookup) module's `lookup` event fires. This happens when the DNS has been resolved.
    - `connect`: Relative timestamp when the [`net`](https://nodejs.org/api/net.html#net_event_connect) module's `connect` event fires. This happens when the server acknowledges the TCP connection.
    - `response`: Relative timestamp when the [`http`](https://nodejs.org/api/http.html#http_event_response) module's `response` event fires. This happens when the first bytes are received from the server.
    - `end`: Relative timestamp when the last bytes of the response are received.
  - `timingPhases` Contains the durations of each request phase. If there were redirects, the properties reflect the timings of the final request in the redirect chain:
    - `wait`: Duration of socket initialization (`timings.socket`)
    - `dns`: Duration of DNS lookup (`timings.lookup` - `timings.socket`)
    - `tcp`: Duration of TCP connection (`timings.connect` - `timings.socket`)
    - `firstByte`: Duration of HTTP server response (`timings.response` - `timings.connect`)
    - `download`: Duration of HTTP download (`timings.end` - `timings.response`)
    - `total`: Duration entire HTTP round-trip (`timings.end`)

- `har` - a [HAR 1.2 Request Object](http://www.softwareishard.com/blog/har-12-spec/#request), will be processed from HAR format into options overwriting matching values *(see the [HAR 1.2 section](#support-for-har-1.2) for details)*
- `callback` - alternatively pass the request's callback in the options object

The callback argument gets 3 arguments:

1. An `error` when applicable (usually from [`http.ClientRequest`](http://nodejs.org/api/http.html#http_class_http_clientrequest) object)
2. An [`http.IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage) object (Response object)
3. The third is the `response` body (`String` or `Buffer`, or JSON object if the `json` option is supplied)

[back to top](#table-of-contents)


---

## Convenience methods

There are also shorthand methods for different HTTP METHODs and some other conveniences.


### request.defaults(options)

This method **returns a wrapper** around the normal request API that defaults
to whatever options you pass to it.

**Note:** `request.defaults()` **does not** modify the global request API;
instead, it **returns a wrapper** that has your default settings applied to it.

**Note:** You can call `.defaults()` on the wrapper that is returned from
`request.defaults` to add/override defaults that were previously defaulted.

For example:
```js
//requests using baseRequest() will set the 'x-token' header
var baseRequest = request.defaults({
  headers: {'x-token': 'my-token'}
})

//requests using specialRequest() will include the 'x-token' header set in
//baseRequest and will also include the 'special' header
var specialRequest = baseRequest.defaults({
  headers: {special: 'special value'}
})
```

### request.METHOD()

These HTTP method convenience functions act just like `request()` but with a default method already set for you:

- *request.get()*: Defaults to `method: "GET"`.
- *request.post()*: Defaults to `method: "POST"`.
- *request.put()*: Defaults to `method: "PUT"`.
- *request.patch()*: Defaults to `method: "PATCH"`.
- *request.del() / request.delete()*: Defaults to `method: "DELETE"`.
- *request.head()*: Defaults to `method: "HEAD"`.
- *request.options()*: Defaults to `method: "OPTIONS"`.

### request.cookie()

Function that creates a new cookie.

```js
request.cookie('key1=value1')
```
### request.jar()

Function that creates a new cookie jar.

```js
request.jar()
```

[back to top](#table-of-contents)


---


## Debugging

There are at least three ways to debug the operation of `request`:

1. Launch the node process like `NODE_DEBUG=request node script.js`
   (`lib,request,otherlib` works too).

2. Set `require('request').debug = true` at any time (this does the same thing
   as #1).

3. Use the [request-debug module](https://github.com/request/request-debug) to
   view request and response headers and bodies.

[back to top](#table-of-contents)


---

## Timeouts

Most requests to external servers should have a timeout attached, in case the
server is not responding in a timely manner. Without a timeout, your code may
have a socket open/consume resources for minutes or more.

There are two main types of timeouts: **connection timeouts** and **read
timeouts**. A connect timeout occurs if the timeout is hit while your client is
attempting to establish a connection to a remote machine (corresponding to the
[connect() call][connect] on the socket). A read timeout occurs any time the
server is too slow to send back a part of the response.

These two situations have widely different implications for what went wrong
with the request, so it's useful to be able to distinguish them. You can detect
timeout errors by checking `err.code` for an 'ETIMEDOUT' value. Further, you
can detect whether the timeout was a connection timeout by checking if the
`err.connect` property is set to `true`.

```js
request.get('http://10.255.255.1', {timeout: 1500}, function(err) {
    console.log(err.code === 'ETIMEDOUT');
    // Set to `true` if the timeout was a connection timeout, `false` or
    // `undefined` otherwise.
    console.log(err.connect === true);
    process.exit(0);
});
```

[connect]: http://linux.die.net/man/2/connect

## Examples:

```js
  var request = require('request')
    , rand = Math.floor(Math.random()*100000000).toString()
    ;
  request(
    { method: 'PUT'
    , uri: 'http://mikeal.iriscouch.com/testjs/' + rand
    , multipart:
      [ { 'content-type': 'application/json'
        ,  body: JSON.stringify({foo: 'bar', _attachments: {'message.txt': {follows: true, length: 18, 'content_type': 'text/plain' }}})
        }
      , { body: 'I am an attachment' }
      ]
    }
  , function (error, response, body) {
      if(response.statusCode == 201){
        console.log('document saved as: http://mikeal.iriscouch.com/testjs/'+ rand)
      } else {
        console.log('error: '+ response.statusCode)
        console.log(body)
      }
    }
  )
```

For backwards-compatibility, response compression is not supported by default.
To accept gzip-compressed responses, set the `gzip` option to `true`. Note
that the body data passed through `request` is automatically decompressed
while the response object is unmodified and will contain compressed data if
the server sent a compressed response.

```js
  var request = require('request')
  request(
    { method: 'GET'
    , uri: 'http://www.google.com'
    , gzip: true
    }
  , function (error, response, body) {
      // body is the decompressed response body
      console.log('server encoded the data as: ' + (response.headers['content-encoding'] || 'identity'))
      console.log('the decoded data is: ' + body)
    }
  )
  .on('data', function(data) {
    // decompressed data as it is received
    console.log('decoded chunk: ' + data)
  })
  .on('response', function(response) {
    // unmodified http.IncomingMessage object
    response.on('data', function(data) {
      // compressed data as it is received
      console.log('received ' + data.length + ' bytes of compressed data')
    })
  })
```

Cookies are disabled by default (else, they would be used in subsequent requests). To enable cookies, set `jar` to `true` (either in `defaults` or `options`).

```js
var request = request.defaults({jar: true})
request('http://www.google.com', function () {
  request('http://images.google.com')
})
```

To use a custom cookie jar (instead of `request`’s global cookie jar), set `jar` to an instance of `request.jar()` (either in `defaults` or `options`)

```js
var j = request.jar()
var request = request.defaults({jar:j})
request('http://www.google.com', function () {
  request('http://images.google.com')
})
```

OR

```js
var j = request.jar();
var cookie = request.cookie('key1=value1');
var url = 'http://www.google.com';
j.setCookie(cookie, url);
request({url: url, jar: j}, function () {
  request('http://images.google.com')
})
```

To use a custom cookie store (such as a
[`FileCookieStore`](https://github.com/mitsuru/tough-cookie-filestore)
which supports saving to and restoring from JSON files), pass it as a parameter
to `request.jar()`:

```js
var FileCookieStore = require('tough-cookie-filestore');
// NOTE - currently the 'cookies.json' file must already exist!
var j = request.jar(new FileCookieStore('cookies.json'));
request = request.defaults({ jar : j })
request('http://www.google.com', function() {
  request('http://images.google.com')
})
```

The cookie store must be a
[`tough-cookie`](https://github.com/SalesforceEng/tough-cookie)
store and it must support synchronous operations; see the
[`CookieStore` API docs](https://github.com/SalesforceEng/tough-cookie#cookiestore-api)
for details.

To inspect your cookie jar after a request:

```js
var j = request.jar()
request({url: 'http://www.google.com', jar: j}, function () {
  var cookie_string = j.getCookieString(url); // "key1=value1; key2=value2; ..."
  var cookies = j.getCookies(url);
  // [{key: 'key1', value: 'value1', domain: "www.google.com", ...}, ...]
})
```

[back to top](#table-of-contents)
# is-ci

Returns `true` if the current environment is a Continuous Integration
server.

Please [open an issue](https://github.com/watson/is-ci/issues) if your
CI server isn't properly detected :)

[![Build status](https://travis-ci.org/watson/is-ci.svg?branch=master)](https://travis-ci.org/watson/is-ci)
[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Installation

```
npm install is-ci --save
```

## Usage

```js
var isCI = require('is-ci')

if (isCI) {
  console.log('The code is running on a CI server')
}
```

## Supported CI tools

Officially supported CI servers:

- [Travis CI](http://travis-ci.org)
- [CircleCI](http://circleci.com)
- [Jenkins CI](https://jenkins-ci.org)
- [Hudson](http://hudson-ci.org)
- [Bamboo](https://www.atlassian.com/software/bamboo)
- [TeamCity](https://www.jetbrains.com/teamcity/)
- [Team Foundation Server](https://www.visualstudio.com/en-us/products/tfs-overview-vs.aspx)
- [GitLab CI](https://about.gitlab.com/gitlab-ci/)
- [Codeship](https://codeship.com)
- [Drone.io](https://drone.io)
- [Magnum CI](https://magnum-ci.com)
- [Semaphore](https://semaphoreci.com)
- [AppVeyor](http://www.appveyor.com)
- [Buildkite](https://buildkite.com)
- [TaskCluster](http://docs.taskcluster.net)
- [GoCD](https://www.go.cd/)
- [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)

Other CI tools using environment variables like `BUILD_ID` or `CI` would be detected as well.

## License

MIT
aws-sign
========

AWS signing. Originally pulled from LearnBoost/knox, maintained as vendor in request, now a standalone module.
# Punycode.js [![Build status](https://travis-ci.org/bestiejs/punycode.js.svg?branch=master)](https://travis-ci.org/bestiejs/punycode.js) [![Code coverage status](http://img.shields.io/coveralls/bestiejs/punycode.js/master.svg)](https://coveralls.io/r/bestiejs/punycode.js) [![Dependency status](https://gemnasium.com/bestiejs/punycode.js.svg)](https://gemnasium.com/bestiejs/punycode.js)

A robust Punycode converter that fully complies to [RFC 3492](https://tools.ietf.org/html/rfc3492) and [RFC 5891](https://tools.ietf.org/html/rfc5891), and works on nearly all JavaScript platforms.

This JavaScript library is the result of comparing, optimizing and documenting different open-source implementations of the Punycode algorithm:

* [The C example code from RFC 3492](https://tools.ietf.org/html/rfc3492#appendix-C)
* [`punycode.c` by _Markus W. Scherer_ (IBM)](http://opensource.apple.com/source/ICU/ICU-400.42/icuSources/common/punycode.c)
* [`punycode.c` by _Ben Noordhuis_](https://github.com/bnoordhuis/punycode/blob/master/punycode.c)
* [JavaScript implementation by _some_](http://stackoverflow.com/questions/183485/can-anyone-recommend-a-good-free-javascript-for-punycode-to-unicode-conversion/301287#301287)
* [`punycode.js` by _Ben Noordhuis_](https://github.com/joyent/node/blob/426298c8c1c0d5b5224ac3658c41e7c2a3fe9377/lib/punycode.js) (note: [not fully compliant](https://github.com/joyent/node/issues/2072))

This project is [bundled](https://github.com/joyent/node/blob/master/lib/punycode.js) with [Node.js v0.6.2+](https://github.com/joyent/node/compare/975f1930b1...61e796decc) and [io.js v1.0.0+](https://github.com/iojs/io.js/blob/v1.x/lib/punycode.js).

## Installation

Via [npm](https://www.npmjs.com/) (only required for Node.js releases older than v0.6.2):

```bash
npm install punycode
```

Via [Bower](http://bower.io/):

```bash
bower install punycode
```

Via [Component](https://github.com/component/component):

```bash
component install bestiejs/punycode.js
```

In a browser:

```html
<script src="punycode.js"></script>
```

In [Node.js](https://nodejs.org/), [io.js](https://iojs.org/), [Narwhal](http://narwhaljs.org/), and [RingoJS](http://ringojs.org/):

```js
var punycode = require('punycode');
```

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('punycode.js');
```

Using an AMD loader like [RequireJS](http://requirejs.org/):

```js
require(
  {
    'paths': {
      'punycode': 'path/to/punycode'
    }
  },
  ['punycode'],
  function(punycode) {
    console.log(punycode);
  }
);
```

## API

### `punycode.decode(string)`

Converts a Punycode string of ASCII symbols to a string of Unicode symbols.

```js
// decode domain name parts
punycode.decode('maana-pta'); // 'mañana'
punycode.decode('--dqo34k'); // '☃-⌘'
```

### `punycode.encode(string)`

Converts a string of Unicode symbols to a Punycode string of ASCII symbols.

```js
// encode domain name parts
punycode.encode('mañana'); // 'maana-pta'
punycode.encode('☃-⌘'); // '--dqo34k'
```

### `punycode.toUnicode(input)`

Converts a Punycode string representing a domain name or an email address to Unicode. Only the Punycoded parts of the input will be converted, i.e. it doesn’t matter if you call it on a string that has already been converted to Unicode.

```js
// decode domain names
punycode.toUnicode('xn--maana-pta.com');
// → 'mañana.com'
punycode.toUnicode('xn----dqo34k.com');
// → '☃-⌘.com'

// decode email addresses
punycode.toUnicode('джумла@xn--p-8sbkgc5ag7bhce.xn--ba-lmcq');
// → 'джумла@джpумлатест.bрфa'
```

### `punycode.toASCII(input)`

Converts a lowercased Unicode string representing a domain name or an email address to Punycode. Only the non-ASCII parts of the input will be converted, i.e. it doesn’t matter if you call it with a domain that’s already in ASCII.

```js
// encode domain names
punycode.toASCII('mañana.com');
// → 'xn--maana-pta.com'
punycode.toASCII('☃-⌘.com');
// → 'xn----dqo34k.com'

// encode email addresses
punycode.toASCII('джумла@джpумлатест.bрфa');
// → 'джумла@xn--p-8sbkgc5ag7bhce.xn--ba-lmcq'
```

### `punycode.ucs2`

#### `punycode.ucs2.decode(string)`

Creates an array containing the numeric code point values of each Unicode symbol in the string. While [JavaScript uses UCS-2 internally](https://mathiasbynens.be/notes/javascript-encoding), this function will convert a pair of surrogate halves (each of which UCS-2 exposes as separate characters) into a single code point, matching UTF-16.

```js
punycode.ucs2.decode('abc');
// → [0x61, 0x62, 0x63]
// surrogate pair for U+1D306 TETRAGRAM FOR CENTRE:
punycode.ucs2.decode('\uD834\uDF06');
// → [0x1D306]
```

#### `punycode.ucs2.encode(codePoints)`

Creates a string based on an array of numeric code point values.

```js
punycode.ucs2.encode([0x61, 0x62, 0x63]);
// → 'abc'
punycode.ucs2.encode([0x1D306]);
// → '\uD834\uDF06'
```

### `punycode.version`

A string representing the current Punycode.js version number.

## Unit tests & code coverage

After cloning this repository, run `npm install --dev` to install the dependencies needed for Punycode.js development and testing. You may want to install Istanbul _globally_ using `npm install istanbul -g`.

Once that’s done, you can run the unit tests in Node using `npm test` or `node tests/tests.js`. To run the tests in Rhino, Ringo, Narwhal, PhantomJS, and web browsers as well, use `grunt test`.

To generate the code coverage report, use `grunt cover`.

Feel free to fork if you see possible improvements!

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## Contributors

| [![twitter/jdalton](https://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter") |
|---|
| [John-David Dalton](http://allyoucanleet.com/) |

## License

Punycode.js is available under the [MIT](https://mths.be/mit) license.
# request-progress [![Build Status](https://secure.travis-ci.org/IndigoUnited/node-request-progress.png)](http://travis-ci.org/IndigoUnited/node-request-progress.png)

Tracks the download progress of a request made with [request](https://github.com/mikeal/request).


## Installation

`$ npm install request-progress`


## Usage

```js
var fs = require('fs');
var request = require('request');
var progress = require('request-progress');

// Note that the options argument is optional
progress(request('http://google.com/doodle.png'), {
    throttle: 2000,  // Throttle the progress event to 2000ms, defaults to 1000ms
    delay: 1000      // Only start to emit after 1000ms delay, defaults to 0ms
})
.on('progress', function (state) {
    console.log('received size in bytes', state.received);
    // The properties bellow can be null if response does not contain
    // the content-length header
    console.log('total size in bytes', state.total);
    console.log('percent', state.percent);
})
.on('error', function (err) {
    // Do something with err
})
.pipe(fs.createWriteStream('doodle.png'))
.on('error', function (err) {
    // Do something with err
})
.on('close', function (err) {
    // Saved to doogle.png!
})
```

Note that the `state` object emitted in the `progress` event is reused to avoid creating a new object for each event.


## License

Released under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
# qs <sup>[![Version Badge][2]][1]</sup>

[![Build Status][3]][4]
[![dependency status][5]][6]
[![dev dependency status][7]][8]
[![License][license-image]][license-url]
[![Downloads][downloads-image]][downloads-url]

[![npm badge][11]][1]

A querystring parsing and stringifying library with some added security.

Lead Maintainer: [Jordan Harband](https://github.com/ljharb)

The **qs** module was originally created and maintained by [TJ Holowaychuk](https://github.com/visionmedia/node-querystring).

## Usage

```javascript
var qs = require('qs');
var assert = require('assert');

var obj = qs.parse('a=c');
assert.deepEqual(obj, { a: 'c' });

var str = qs.stringify(obj);
assert.equal(str, 'a=c');
```

### Parsing Objects

[](#preventEval)
```javascript
qs.parse(string, [options]);
```

**qs** allows you to create nested objects within your query strings, by surrounding the name of sub-keys with square brackets `[]`.
For example, the string `'foo[bar]=baz'` converts to:

```javascript
assert.deepEqual(qs.parse('foo[bar]=baz'), {
    foo: {
        bar: 'baz'
    }
});
```

When using the `plainObjects` option the parsed value is returned as a null object, created via `Object.create(null)` and as such you should be aware that prototype methods will not exist on it and a user may set those names to whatever value they like:

```javascript
var nullObject = qs.parse('a[hasOwnProperty]=b', { plainObjects: true });
assert.deepEqual(nullObject, { a: { hasOwnProperty: 'b' } });
```

By default parameters that would overwrite properties on the object prototype are ignored, if you wish to keep the data from those fields either use `plainObjects` as mentioned above, or set `allowPrototypes` to `true` which will allow user input to overwrite those properties. *WARNING* It is generally a bad idea to enable this option as it can cause problems when attempting to use the properties that have been overwritten. Always be careful with this option.

```javascript
var protoObject = qs.parse('a[hasOwnProperty]=b', { allowPrototypes: true });
assert.deepEqual(protoObject, { a: { hasOwnProperty: 'b' } });
```

URI encoded strings work too:

```javascript
assert.deepEqual(qs.parse('a%5Bb%5D=c'), {
    a: { b: 'c' }
});
```

You can also nest your objects, like `'foo[bar][baz]=foobarbaz'`:

```javascript
assert.deepEqual(qs.parse('foo[bar][baz]=foobarbaz'), {
    foo: {
        bar: {
            baz: 'foobarbaz'
        }
    }
});
```

By default, when nesting objects **qs** will only parse up to 5 children deep. This means if you attempt to parse a string like
`'a[b][c][d][e][f][g][h][i]=j'` your resulting object will be:

```javascript
var expected = {
    a: {
        b: {
            c: {
                d: {
                    e: {
                        f: {
                            '[g][h][i]': 'j'
                        }
                    }
                }
            }
        }
    }
};
var string = 'a[b][c][d][e][f][g][h][i]=j';
assert.deepEqual(qs.parse(string), expected);
```

This depth can be overridden by passing a `depth` option to `qs.parse(string, [options])`:

```javascript
var deep = qs.parse('a[b][c][d][e][f][g][h][i]=j', { depth: 1 });
assert.deepEqual(deep, { a: { b: { '[c][d][e][f][g][h][i]': 'j' } } });
```

The depth limit helps mitigate abuse when **qs** is used to parse user input, and it is recommended to keep it a reasonably small number.

For similar reasons, by default **qs** will only parse up to 1000 parameters. This can be overridden by passing a `parameterLimit` option:

```javascript
var limited = qs.parse('a=b&c=d', { parameterLimit: 1 });
assert.deepEqual(limited, { a: 'b' });
```

To bypass the leading question mark, use `ignoreQueryPrefix`:

```javascript
var prefixed = qs.parse('?a=b&c=d', { ignoreQueryPrefix: true });
assert.deepEqual(prefixed, { a: 'b', c: 'd' });
```

An optional delimiter can also be passed:

```javascript
var delimited = qs.parse('a=b;c=d', { delimiter: ';' });
assert.deepEqual(delimited, { a: 'b', c: 'd' });
```

Delimiters can be a regular expression too:

```javascript
var regexed = qs.parse('a=b;c=d,e=f', { delimiter: /[;,]/ });
assert.deepEqual(regexed, { a: 'b', c: 'd', e: 'f' });
```

Option `allowDots` can be used to enable dot notation:

```javascript
var withDots = qs.parse('a.b=c', { allowDots: true });
assert.deepEqual(withDots, { a: { b: 'c' } });
```

### Parsing Arrays

**qs** can also parse arrays using a similar `[]` notation:

```javascript
var withArray = qs.parse('a[]=b&a[]=c');
assert.deepEqual(withArray, { a: ['b', 'c'] });
```

You may specify an index as well:

```javascript
var withIndexes = qs.parse('a[1]=c&a[0]=b');
assert.deepEqual(withIndexes, { a: ['b', 'c'] });
```

Note that the only difference between an index in an array and a key in an object is that the value between the brackets must be a number
to create an array. When creating arrays with specific indices, **qs** will compact a sparse array to only the existing values preserving
their order:

```javascript
var noSparse = qs.parse('a[1]=b&a[15]=c');
assert.deepEqual(noSparse, { a: ['b', 'c'] });
```

Note that an empty string is also a value, and will be preserved:

```javascript
var withEmptyString = qs.parse('a[]=&a[]=b');
assert.deepEqual(withEmptyString, { a: ['', 'b'] });

var withIndexedEmptyString = qs.parse('a[0]=b&a[1]=&a[2]=c');
assert.deepEqual(withIndexedEmptyString, { a: ['b', '', 'c'] });
```

**qs** will also limit specifying indices in an array to a maximum index of `20`. Any array members with an index of greater than `20` will
instead be converted to an object with the index as the key:

```javascript
var withMaxIndex = qs.parse('a[100]=b');
assert.deepEqual(withMaxIndex, { a: { '100': 'b' } });
```

This limit can be overridden by passing an `arrayLimit` option:

```javascript
var withArrayLimit = qs.parse('a[1]=b', { arrayLimit: 0 });
assert.deepEqual(withArrayLimit, { a: { '1': 'b' } });
```

To disable array parsing entirely, set `parseArrays` to `false`.

```javascript
var noParsingArrays = qs.parse('a[]=b', { parseArrays: false });
assert.deepEqual(noParsingArrays, { a: { '0': 'b' } });
```

If you mix notations, **qs** will merge the two items into an object:

```javascript
var mixedNotation = qs.parse('a[0]=b&a[b]=c');
assert.deepEqual(mixedNotation, { a: { '0': 'b', b: 'c' } });
```

You can also create arrays of objects:

```javascript
var arraysOfObjects = qs.parse('a[][b]=c');
assert.deepEqual(arraysOfObjects, { a: [{ b: 'c' }] });
```

### Stringifying

[](#preventEval)
```javascript
qs.stringify(object, [options]);
```

When stringifying, **qs** by default URI encodes output. Objects are stringified as you would expect:

```javascript
assert.equal(qs.stringify({ a: 'b' }), 'a=b');
assert.equal(qs.stringify({ a: { b: 'c' } }), 'a%5Bb%5D=c');
```

This encoding can be disabled by setting the `encode` option to `false`:

```javascript
var unencoded = qs.stringify({ a: { b: 'c' } }, { encode: false });
assert.equal(unencoded, 'a[b]=c');
```

Encoding can be disabled for keys by setting the `encodeValuesOnly` option to `true`:
```javascript
var encodedValues = qs.stringify(
    { a: 'b', c: ['d', 'e=f'], f: [['g'], ['h']] },
    { encodeValuesOnly: true }
);
assert.equal(encodedValues,'a=b&c[0]=d&c[1]=e%3Df&f[0][0]=g&f[1][0]=h');
```

This encoding can also be replaced by a custom encoding method set as `encoder` option:

```javascript
var encoded = qs.stringify({ a: { b: 'c' } }, { encoder: function (str) {
    // Passed in values `a`, `b`, `c`
    return // Return encoded string
}})
```

_(Note: the `encoder` option does not apply if `encode` is `false`)_

Analogue to the `encoder` there is a `decoder` option for `parse` to override decoding of properties and values:

```javascript
var decoded = qs.parse('x=z', { decoder: function (str) {
    // Passed in values `x`, `z`
    return // Return decoded string
}})
```

Examples beyond this point will be shown as though the output is not URI encoded for clarity. Please note that the return values in these cases *will* be URI encoded during real usage.

When arrays are stringified, by default they are given explicit indices:

```javascript
qs.stringify({ a: ['b', 'c', 'd'] });
// 'a[0]=b&a[1]=c&a[2]=d'
```

You may override this by setting the `indices` option to `false`:

```javascript
qs.stringify({ a: ['b', 'c', 'd'] }, { indices: false });
// 'a=b&a=c&a=d'
```

You may use the `arrayFormat` option to specify the format of the output array:

```javascript
qs.stringify({ a: ['b', 'c'] }, { arrayFormat: 'indices' })
// 'a[0]=b&a[1]=c'
qs.stringify({ a: ['b', 'c'] }, { arrayFormat: 'brackets' })
// 'a[]=b&a[]=c'
qs.stringify({ a: ['b', 'c'] }, { arrayFormat: 'repeat' })
// 'a=b&a=c'
```

When objects are stringified, by default they use bracket notation:

```javascript
qs.stringify({ a: { b: { c: 'd', e: 'f' } } });
// 'a[b][c]=d&a[b][e]=f'
```

You may override this to use dot notation by setting the `allowDots` option to `true`:

```javascript
qs.stringify({ a: { b: { c: 'd', e: 'f' } } }, { allowDots: true });
// 'a.b.c=d&a.b.e=f'
```

Empty strings and null values will omit the value, but the equals sign (=) remains in place:

```javascript
assert.equal(qs.stringify({ a: '' }), 'a=');
```

Key with no values (such as an empty object or array) will return nothing:

```javascript
assert.equal(qs.stringify({ a: [] }), '');
assert.equal(qs.stringify({ a: {} }), '');
assert.equal(qs.stringify({ a: [{}] }), '');
assert.equal(qs.stringify({ a: { b: []} }), '');
assert.equal(qs.stringify({ a: { b: {}} }), '');
```

Properties that are set to `undefined` will be omitted entirely:

```javascript
assert.equal(qs.stringify({ a: null, b: undefined }), 'a=');
```

The query string may optionally be prepended with a question mark:

```javascript
assert.equal(qs.stringify({ a: 'b', c: 'd' }, { addQueryPrefix: true }), '?a=b&c=d');
```

The delimiter may be overridden with stringify as well:

```javascript
assert.equal(qs.stringify({ a: 'b', c: 'd' }, { delimiter: ';' }), 'a=b;c=d');
```

If you only want to override the serialization of `Date` objects, you can provide a `serializeDate` option:

```javascript
var date = new Date(7);
assert.equal(qs.stringify({ a: date }), 'a=1970-01-01T00:00:00.007Z'.replace(/:/g, '%3A'));
assert.equal(
    qs.stringify({ a: date }, { serializeDate: function (d) { return d.getTime(); } }),
    'a=7'
);
```

You may use the `sort` option to affect the order of parameter keys:

```javascript
function alphabeticalSort(a, b) {
    return a.localeCompare(b);
}
assert.equal(qs.stringify({ a: 'c', z: 'y', b : 'f' }, { sort: alphabeticalSort }), 'a=c&b=f&z=y');
```

Finally, you can use the `filter` option to restrict which keys will be included in the stringified output.
If you pass a function, it will be called for each key to obtain the replacement value. Otherwise, if you
pass an array, it will be used to select properties and array indices for stringification:

```javascript
function filterFunc(prefix, value) {
    if (prefix == 'b') {
        // Return an `undefined` value to omit a property.
        return;
    }
    if (prefix == 'e[f]') {
        return value.getTime();
    }
    if (prefix == 'e[g][0]') {
        return value * 2;
    }
    return value;
}
qs.stringify({ a: 'b', c: 'd', e: { f: new Date(123), g: [2] } }, { filter: filterFunc });
// 'a=b&c=d&e[f]=123&e[g][0]=4'
qs.stringify({ a: 'b', c: 'd', e: 'f' }, { filter: ['a', 'e'] });
// 'a=b&e=f'
qs.stringify({ a: ['b', 'c', 'd'], e: 'f' }, { filter: ['a', 0, 2] });
// 'a[0]=b&a[2]=d'
```

### Handling of `null` values

By default, `null` values are treated like empty strings:

```javascript
var withNull = qs.stringify({ a: null, b: '' });
assert.equal(withNull, 'a=&b=');
```

Parsing does not distinguish between parameters with and without equal signs. Both are converted to empty strings.

```javascript
var equalsInsensitive = qs.parse('a&b=');
assert.deepEqual(equalsInsensitive, { a: '', b: '' });
```

To distinguish between `null` values and empty strings use the `strictNullHandling` flag. In the result string the `null`
values have no `=` sign:

```javascript
var strictNull = qs.stringify({ a: null, b: '' }, { strictNullHandling: true });
assert.equal(strictNull, 'a&b=');
```

To parse values without `=` back to `null` use the `strictNullHandling` flag:

```javascript
var parsedStrictNull = qs.parse('a&b=', { strictNullHandling: true });
assert.deepEqual(parsedStrictNull, { a: null, b: '' });
```

To completely skip rendering keys with `null` values, use the `skipNulls` flag:

```javascript
var nullsSkipped = qs.stringify({ a: 'b', c: null}, { skipNulls: true });
assert.equal(nullsSkipped, 'a=b');
```

### Dealing with special character sets

By default the encoding and decoding of characters is done in `utf-8`. If you
wish to encode querystrings to a different character set (i.e.
[Shift JIS](https://en.wikipedia.org/wiki/Shift_JIS)) you can use the
[`qs-iconv`](https://github.com/martinheidegger/qs-iconv) library:

```javascript
var encoder = require('qs-iconv/encoder')('shift_jis');
var shiftJISEncoded = qs.stringify({ a: 'こんにちは！' }, { encoder: encoder });
assert.equal(shiftJISEncoded, 'a=%82%B1%82%F1%82%C9%82%BF%82%CD%81I');
```

This also works for decoding of query strings:

```javascript
var decoder = require('qs-iconv/decoder')('shift_jis');
var obj = qs.parse('a=%82%B1%82%F1%82%C9%82%BF%82%CD%81I', { decoder: decoder });
assert.deepEqual(obj, { a: 'こんにちは！' });
```

### RFC 3986 and RFC 1738 space encoding

RFC3986 used as default option and encodes ' ' to *%20* which is backward compatible.
In the same time, output can be stringified as per RFC1738 with ' ' equal to '+'.

```
assert.equal(qs.stringify({ a: 'b c' }), 'a=b%20c');
assert.equal(qs.stringify({ a: 'b c' }, { format : 'RFC3986' }), 'a=b%20c');
assert.equal(qs.stringify({ a: 'b c' }, { format : 'RFC1738' }), 'a=b+c');
```

[1]: https://npmjs.org/package/qs
[2]: http://versionbadg.es/ljharb/qs.svg
[3]: https://api.travis-ci.org/ljharb/qs.svg
[4]: https://travis-ci.org/ljharb/qs
[5]: https://david-dm.org/ljharb/qs.svg
[6]: https://david-dm.org/ljharb/qs
[7]: https://david-dm.org/ljharb/qs/dev-status.svg
[8]: https://david-dm.org/ljharb/qs?type=dev
[9]: https://ci.testling.com/ljharb/qs.png
[10]: https://ci.testling.com/ljharb/qs
[11]: https://nodei.co/npm/qs.png?downloads=true&stars=true
[license-image]: http://img.shields.io/npm/l/qs.svg
[license-url]: LICENSE
[downloads-image]: http://img.shields.io/npm/dm/qs.svg
[downloads-url]: http://npm-stat.com/charts.html?package=qs

# isarray

`Array#isArray` for older browsers.

[![build status](https://secure.travis-ci.org/juliangruber/isarray.svg)](http://travis-ci.org/juliangruber/isarray)
[![downloads](https://img.shields.io/npm/dm/isarray.svg)](https://www.npmjs.org/package/isarray)

[![browser support](https://ci.testling.com/juliangruber/isarray.png)
](https://ci.testling.com/juliangruber/isarray)

## Usage

```js
var isArray = require('isarray');

console.log(isArray([])); // => true
console.log(isArray({})); // => false
```

## Installation

With [npm](http://npmjs.org) do

```bash
$ npm install isarray
```

Then bundle for the browser with
[browserify](https://github.com/substack/browserify).

With [component](http://component.io) do

```bash
$ component install juliangruber/isarray
```

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# minimatch

A minimal matching utility.

[![Build Status](https://secure.travis-ci.org/isaacs/minimatch.svg)](http://travis-ci.org/isaacs/minimatch)


This is the matching library used internally by npm.

It works by converting glob expressions into JavaScript `RegExp`
objects.

## Usage

```javascript
var minimatch = require("minimatch")

minimatch("bar.foo", "*.foo") // true!
minimatch("bar.foo", "*.bar") // false!
minimatch("bar.foo", "*.+(bar|foo)", { debug: true }) // true, and noisy!
```

## Features

Supports these glob features:

* Brace Expansion
* Extended glob matching
* "Globstar" `**` matching

See:

* `man sh`
* `man bash`
* `man 3 fnmatch`
* `man 5 gitignore`

## Minimatch Class

Create a minimatch object by instantiating the `minimatch.Minimatch` class.

```javascript
var Minimatch = require("minimatch").Minimatch
var mm = new Minimatch(pattern, options)
```

### Properties

* `pattern` The original pattern the minimatch object represents.
* `options` The options supplied to the constructor.
* `set` A 2-dimensional array of regexp or string expressions.
  Each row in the
  array corresponds to a brace-expanded pattern.  Each item in the row
  corresponds to a single path-part.  For example, the pattern
  `{a,b/c}/d` would expand to a set of patterns like:

        [ [ a, d ]
        , [ b, c, d ] ]

    If a portion of the pattern doesn't have any "magic" in it
    (that is, it's something like `"foo"` rather than `fo*o?`), then it
    will be left as a string rather than converted to a regular
    expression.

* `regexp` Created by the `makeRe` method.  A single regular expression
  expressing the entire pattern.  This is useful in cases where you wish
  to use the pattern somewhat like `fnmatch(3)` with `FNM_PATH` enabled.
* `negate` True if the pattern is negated.
* `comment` True if the pattern is a comment.
* `empty` True if the pattern is `""`.

### Methods

* `makeRe` Generate the `regexp` member if necessary, and return it.
  Will return `false` if the pattern is invalid.
* `match(fname)` Return true if the filename matches the pattern, or
  false otherwise.
* `matchOne(fileArray, patternArray, partial)` Take a `/`-split
  filename, and match it against a single row in the `regExpSet`.  This
  method is mainly for internal use, but is exposed so that it can be
  used by a glob-walker that needs to avoid excessive filesystem calls.

All other methods are internal, and will be called as necessary.

### minimatch(path, pattern, options)

Main export.  Tests a path against the pattern using the options.

```javascript
var isJS = minimatch(file, "*.js", { matchBase: true })
```

### minimatch.filter(pattern, options)

Returns a function that tests its
supplied argument, suitable for use with `Array.filter`.  Example:

```javascript
var javascripts = fileList.filter(minimatch.filter("*.js", {matchBase: true}))
```

### minimatch.match(list, pattern, options)

Match against the list of
files, in the style of fnmatch or glob.  If nothing is matched, and
options.nonull is set, then return a list containing the pattern itself.

```javascript
var javascripts = minimatch.match(fileList, "*.js", {matchBase: true}))
```

### minimatch.makeRe(pattern, options)

Make a regular expression object from the pattern.

## Options

All options are `false` by default.

### debug

Dump a ton of stuff to stderr.

### nobrace

Do not expand `{a,b}` and `{1..3}` brace sets.

### noglobstar

Disable `**` matching against multiple folder names.

### dot

Allow patterns to match filenames starting with a period, even if
the pattern does not explicitly have a period in that spot.

Note that by default, `a/**/b` will **not** match `a/.d/b`, unless `dot`
is set.

### noext

Disable "extglob" style patterns like `+(a|b)`.

### nocase

Perform a case-insensitive match.

### nonull

When a match is not found by `minimatch.match`, return a list containing
the pattern itself if this option is set.  When not set, an empty list
is returned if there are no matches.

### matchBase

If set, then patterns without slashes will be matched
against the basename of the path if it contains slashes.  For example,
`a?b` would match the path `/xyz/123/acb`, but not `/xyz/acb/123`.

### nocomment

Suppress the behavior of treating `#` at the start of a pattern as a
comment.

### nonegate

Suppress the behavior of treating a leading `!` character as negation.

### flipNegate

Returns from negate expressions the same as if they were not negated.
(Ie, true on a hit, false on a miss.)


## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between minimatch and other
implementations, and are intentional.

If the pattern starts with a `!` character, then it is negated.  Set the
`nonegate` flag to suppress this behavior, and treat leading `!`
characters normally.  This is perhaps relevant if you wish to start the
pattern with a negative extglob pattern like `!(a|B)`.  Multiple `!`
characters at the start of a pattern will negate the pattern multiple
times.

If a pattern starts with `#`, then it is treated as a comment, and
will not match anything.  Use `\#` to match a literal `#` at the
start of a line, or set the `nocomment` flag to suppress this behavior.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.1, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

If an escaped pattern has no matches, and the `nonull` flag is set,
then minimatch.match returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`minimatch.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.
TweetNaCl.js
============

Port of [TweetNaCl](http://tweetnacl.cr.yp.to) / [NaCl](http://nacl.cr.yp.to/)
to JavaScript for modern browsers and Node.js. Public domain.

[![Build Status](https://travis-ci.org/dchest/tweetnacl-js.svg?branch=master)
](https://travis-ci.org/dchest/tweetnacl-js)

Demo: <https://tweetnacl.js.org>

**:warning: The library is stable and API is frozen, however it has not been
independently reviewed. If you can help reviewing it, please [contact
me](mailto:dmitry@codingrobots.com).**

Documentation
=============

* [Overview](#overview)
* [Installation](#installation)
* [Usage](#usage)
  * [Public-key authenticated encryption (box)](#public-key-authenticated-encryption-box)
  * [Secret-key authenticated encryption (secretbox)](#secret-key-authenticated-encryption-secretbox)
  * [Scalar multiplication](#scalar-multiplication)
  * [Signatures](#signatures)
  * [Hashing](#hashing)
  * [Random bytes generation](#random-bytes-generation)
  * [Constant-time comparison](#constant-time-comparison)
* [System requirements](#system-requirements)
* [Development and testing](#development-and-testing)
* [Benchmarks](#benchmarks)
* [Contributors](#contributors)
* [Who uses it](#who-uses-it)


Overview
--------

The primary goal of this project is to produce a translation of TweetNaCl to
JavaScript which is as close as possible to the original C implementation, plus
a thin layer of idiomatic high-level API on top of it.

There are two versions, you can use either of them:

* `nacl.js` is the port of TweetNaCl with minimum differences from the
  original + high-level API.

* `nacl-fast.js` is like `nacl.js`, but with some functions replaced with
  faster versions.


Installation
------------

You can install TweetNaCl.js via a package manager:

[Bower](http://bower.io):

    $ bower install tweetnacl

[NPM](https://www.npmjs.org/):

    $ npm install tweetnacl

or [download source code](https://github.com/dchest/tweetnacl-js/releases).


Usage
-----

All API functions accept and return bytes as `Uint8Array`s.  If you need to
encode or decode strings, use functions from
<https://github.com/dchest/tweetnacl-util-js> or one of the more robust codec
packages.

In Node.js v4 and later `Buffer` objects are backed by `Uint8Array`s, so you
can freely pass them to TweetNaCl.js functions as arguments. The returned
objects are still `Uint8Array`s, so if you need `Buffer`s, you'll have to
convert them manually; make sure to convert using copying: `new Buffer(array)`,
instead of sharing: `new Buffer(array.buffer)`, because some functions return
subarrays of their buffers.


### Public-key authenticated encryption (box)

Implements *curve25519-xsalsa20-poly1305*.

#### nacl.box.keyPair()

Generates a new random key pair for box and returns it as an object with
`publicKey` and `secretKey` members:

    {
       publicKey: ...,  // Uint8Array with 32-byte public key
       secretKey: ...   // Uint8Array with 32-byte secret key
    }


#### nacl.box.keyPair.fromSecretKey(secretKey)

Returns a key pair for box with public key corresponding to the given secret
key.

#### nacl.box(message, nonce, theirPublicKey, mySecretKey)

Encrypt and authenticates message using peer's public key, our secret key, and
the given nonce, which must be unique for each distinct message for a key pair.

Returns an encrypted and authenticated message, which is
`nacl.box.overheadLength` longer than the original message.

#### nacl.box.open(box, nonce, theirPublicKey, mySecretKey)

Authenticates and decrypts the given box with peer's public key, our secret
key, and the given nonce.

Returns the original message, or `false` if authentication fails.

#### nacl.box.before(theirPublicKey, mySecretKey)

Returns a precomputed shared key which can be used in `nacl.box.after` and
`nacl.box.open.after`.

#### nacl.box.after(message, nonce, sharedKey)

Same as `nacl.box`, but uses a shared key precomputed with `nacl.box.before`.

#### nacl.box.open.after(box, nonce, sharedKey)

Same as `nacl.box.open`, but uses a shared key precomputed with `nacl.box.before`.

#### nacl.box.publicKeyLength = 32

Length of public key in bytes.

#### nacl.box.secretKeyLength = 32

Length of secret key in bytes.

#### nacl.box.sharedKeyLength = 32

Length of precomputed shared key in bytes.

#### nacl.box.nonceLength = 24

Length of nonce in bytes.

#### nacl.box.overheadLength = 16

Length of overhead added to box compared to original message.


### Secret-key authenticated encryption (secretbox)

Implements *xsalsa20-poly1305*.

#### nacl.secretbox(message, nonce, key)

Encrypt and authenticates message using the key and the nonce. The nonce must
be unique for each distinct message for this key.

Returns an encrypted and authenticated message, which is
`nacl.secretbox.overheadLength` longer than the original message.

#### nacl.secretbox.open(box, nonce, key)

Authenticates and decrypts the given secret box using the key and the nonce.

Returns the original message, or `false` if authentication fails.

#### nacl.secretbox.keyLength = 32

Length of key in bytes.

#### nacl.secretbox.nonceLength = 24

Length of nonce in bytes.

#### nacl.secretbox.overheadLength = 16

Length of overhead added to secret box compared to original message.


### Scalar multiplication

Implements *curve25519*.

#### nacl.scalarMult(n, p)

Multiplies an integer `n` by a group element `p` and returns the resulting
group element.

#### nacl.scalarMult.base(n)

Multiplies an integer `n` by a standard group element and returns the resulting
group element.

#### nacl.scalarMult.scalarLength = 32

Length of scalar in bytes.

#### nacl.scalarMult.groupElementLength = 32

Length of group element in bytes.


### Signatures

Implements [ed25519](http://ed25519.cr.yp.to).

#### nacl.sign.keyPair()

Generates new random key pair for signing and returns it as an object with
`publicKey` and `secretKey` members:

    {
       publicKey: ...,  // Uint8Array with 32-byte public key
       secretKey: ...   // Uint8Array with 64-byte secret key
    }

#### nacl.sign.keyPair.fromSecretKey(secretKey)

Returns a signing key pair with public key corresponding to the given
64-byte secret key. The secret key must have been generated by
`nacl.sign.keyPair` or `nacl.sign.keyPair.fromSeed`.

#### nacl.sign.keyPair.fromSeed(seed)

Returns a new signing key pair generated deterministically from a 32-byte seed.
The seed must contain enough entropy to be secure. This method is not
recommended for general use: instead, use `nacl.sign.keyPair` to generate a new
key pair from a random seed.

#### nacl.sign(message, secretKey)

Signs the message using the secret key and returns a signed message.

#### nacl.sign.open(signedMessage, publicKey)

Verifies the signed message and returns the message without signature.

Returns `null` if verification failed.

#### nacl.sign.detached(message, secretKey)

Signs the message using the secret key and returns a signature.

#### nacl.sign.detached.verify(message, signature, publicKey)

Verifies the signature for the message and returns `true` if verification
succeeded or `false` if it failed.

#### nacl.sign.publicKeyLength = 32

Length of signing public key in bytes.

#### nacl.sign.secretKeyLength = 64

Length of signing secret key in bytes.

#### nacl.sign.seedLength = 32

Length of seed for `nacl.sign.keyPair.fromSeed` in bytes.

#### nacl.sign.signatureLength = 64

Length of signature in bytes.


### Hashing

Implements *SHA-512*.

#### nacl.hash(message)

Returns SHA-512 hash of the message.

#### nacl.hash.hashLength = 64

Length of hash in bytes.


### Random bytes generation

#### nacl.randomBytes(length)

Returns a `Uint8Array` of the given length containing random bytes of
cryptographic quality.

**Implementation note**

TweetNaCl.js uses the following methods to generate random bytes,
depending on the platform it runs on:

* `window.crypto.getRandomValues` (WebCrypto standard)
* `window.msCrypto.getRandomValues` (Internet Explorer 11)
* `crypto.randomBytes` (Node.js)

If the platform doesn't provide a suitable PRNG, the following functions,
which require random numbers, will throw exception:

* `nacl.randomBytes`
* `nacl.box.keyPair`
* `nacl.sign.keyPair`

Other functions are deterministic and will continue working.

If a platform you are targeting doesn't implement secure random number
generator, but you somehow have a cryptographically-strong source of entropy
(not `Math.random`!), and you know what you are doing, you can plug it into
TweetNaCl.js like this:

    nacl.setPRNG(function(x, n) {
      // ... copy n random bytes into x ...
    });

Note that `nacl.setPRNG` *completely replaces* internal random byte generator
with the one provided.


### Constant-time comparison

#### nacl.verify(x, y)

Compares `x` and `y` in constant time and returns `true` if their lengths are
non-zero and equal, and their contents are equal.

Returns `false` if either of the arguments has zero length, or arguments have
different lengths, or their contents differ.


System requirements
-------------------

TweetNaCl.js supports modern browsers that have a cryptographically secure
pseudorandom number generator and typed arrays, including the latest versions
of:

* Chrome
* Firefox
* Safari (Mac, iOS)
* Internet Explorer 11

Other systems:

* Node.js


Development and testing
------------------------

Install NPM modules needed for development:

    $ npm install

To build minified versions:

    $ npm run build

Tests use minified version, so make sure to rebuild it every time you change
`nacl.js` or `nacl-fast.js`.

### Testing

To run tests in Node.js:

    $ npm run test-node

By default all tests described here work on `nacl.min.js`. To test other
versions, set environment variable `NACL_SRC` to the file name you want to test.
For example, the following command will test fast minified version:

    $ NACL_SRC=nacl-fast.min.js npm run test-node

To run full suite of tests in Node.js, including comparing outputs of
JavaScript port to outputs of the original C version:

    $ npm run test-node-all

To prepare tests for browsers:

    $ npm run build-test-browser

and then open `test/browser/test.html` (or `test/browser/test-fast.html`) to
run them.

To run headless browser tests with `tape-run` (powered by Electron):

    $ npm run test-browser

(If you get `Error: spawn ENOENT`, install *xvfb*: `sudo apt-get install xvfb`.)

To run tests in both Node and Electron:

    $ npm test

### Benchmarking

To run benchmarks in Node.js:

    $ npm run bench
    $ NACL_SRC=nacl-fast.min.js npm run bench

To run benchmarks in a browser, open `test/benchmark/bench.html` (or
`test/benchmark/bench-fast.html`).


Benchmarks
----------

For reference, here are benchmarks from MacBook Pro (Retina, 13-inch, Mid 2014)
laptop with 2.6 GHz Intel Core i5 CPU (Intel) in Chrome 53/OS X and Xiaomi Redmi
Note 3 smartphone with 1.8 GHz Qualcomm Snapdragon 650 64-bit CPU (ARM) in
Chrome 52/Android:

|               | nacl.js Intel | nacl-fast.js Intel  |   nacl.js ARM | nacl-fast.js ARM  |
| ------------- |:-------------:|:-------------------:|:-------------:|:-----------------:|
| salsa20       | 1.3 MB/s      | 128 MB/s            |  0.4 MB/s     |  43 MB/s          |
| poly1305      | 13 MB/s       | 171 MB/s            |  4 MB/s       |  52 MB/s          |
| hash          | 4 MB/s        | 34 MB/s             |  0.9 MB/s     |  12 MB/s          |
| secretbox 1K  | 1113 op/s     | 57583 op/s          |  334 op/s     |  14227 op/s       |
| box 1K        | 145 op/s      | 718 op/s            |  37 op/s      |  368 op/s         |
| scalarMult    | 171 op/s      | 733 op/s            |  56 op/s      |  380 op/s         |
| sign          | 77  op/s      | 200 op/s            |  20 op/s      |  61 op/s          |
| sign.open     | 39  op/s      | 102  op/s           |  11 op/s      |  31 op/s          |

(You can run benchmarks on your devices by clicking on the links at the bottom
of the [home page](https://tweetnacl.js.org)).

In short, with *nacl-fast.js* and 1024-byte messages you can expect to encrypt and
authenticate more than 57000 messages per second on a typical laptop or more than
14000 messages per second on a $170 smartphone, sign about 200 and verify 100
messages per second on a laptop or 60 and 30 messages per second on a smartphone,
per CPU core (with Web Workers you can do these operations in parallel),
which is good enough for most applications.


Contributors
------------

See AUTHORS.md file.


Third-party libraries based on TweetNaCl.js
-------------------------------------------

* [forward-secrecy](https://github.com/alax/forward-secrecy) — Axolotl ratchet implementation
* [nacl-stream](https://github.com/dchest/nacl-stream-js) - streaming encryption
* [tweetnacl-auth-js](https://github.com/dchest/tweetnacl-auth-js) — implementation of [`crypto_auth`](http://nacl.cr.yp.to/auth.html)
* [chloride](https://github.com/dominictarr/chloride) - unified API for various NaCl modules


Who uses it
-----------

Some notable users of TweetNaCl.js:

* [miniLock](http://minilock.io/)
* [Stellar](https://www.stellar.org/)
A light, featureful and explicit option parsing library for node.js.

[Why another one? See below](#why). tl;dr: The others I've tried are one of
too loosey goosey (not explicit), too big/too many deps, or ill specified.
YMMV.

Follow <a href="https://twitter.com/intent/user?screen_name=trentmick" target="_blank">@trentmick</a>
for updates to node-dashdash.

# Install

    npm install dashdash


# Usage

```javascript
var dashdash = require('dashdash');

// Specify the options. Minimally `name` (or `names`) and `type`
// must be given for each.
var options = [
    {
        // `names` or a single `name`. First element is the `opts.KEY`.
        names: ['help', 'h'],
        // See "Option specs" below for types.
        type: 'bool',
        help: 'Print this help and exit.'
    }
];

// Shortcut form. As called it infers `process.argv`. See below for
// the longer form to use methods like `.help()` on the Parser object.
var opts = dashdash.parse({options: options});

console.log("opts:", opts);
console.log("args:", opts._args);
```


# Longer Example

A more realistic [starter script "foo.js"](./examples/foo.js) is as follows.
This also shows using `parser.help()` for formatted option help.

```javascript
var dashdash = require('./lib/dashdash');

var options = [
    {
        name: 'version',
        type: 'bool',
        help: 'Print tool version and exit.'
    },
    {
        names: ['help', 'h'],
        type: 'bool',
        help: 'Print this help and exit.'
    },
    {
        names: ['verbose', 'v'],
        type: 'arrayOfBool',
        help: 'Verbose output. Use multiple times for more verbose.'
    },
    {
        names: ['file', 'f'],
        type: 'string',
        help: 'File to process',
        helpArg: 'FILE'
    }
];

var parser = dashdash.createParser({options: options});
try {
    var opts = parser.parse(process.argv);
} catch (e) {
    console.error('foo: error: %s', e.message);
    process.exit(1);
}

console.log("# opts:", opts);
console.log("# args:", opts._args);

// Use `parser.help()` for formatted options help.
if (opts.help) {
    var help = parser.help({includeEnv: true}).trimRight();
    console.log('usage: node foo.js [OPTIONS]\n'
                + 'options:\n'
                + help);
    process.exit(0);
}

// ...
```


Some example output from this script (foo.js):

```
$ node foo.js -h
# opts: { help: true,
  _order: [ { name: 'help', value: true, from: 'argv' } ],
  _args: [] }
# args: []
usage: node foo.js [OPTIONS]
options:
    --version             Print tool version and exit.
    -h, --help            Print this help and exit.
    -v, --verbose         Verbose output. Use multiple times for more verbose.
    -f FILE, --file=FILE  File to process

$ node foo.js -v
# opts: { verbose: [ true ],
  _order: [ { name: 'verbose', value: true, from: 'argv' } ],
  _args: [] }
# args: []

$ node foo.js --version arg1
# opts: { version: true,
  _order: [ { name: 'version', value: true, from: 'argv' } ],
  _args: [ 'arg1' ] }
# args: [ 'arg1' ]

$ node foo.js -f bar.txt
# opts: { file: 'bar.txt',
  _order: [ { name: 'file', value: 'bar.txt', from: 'argv' } ],
  _args: [] }
# args: []

$ node foo.js -vvv --file=blah
# opts: { verbose: [ true, true, true ],
  file: 'blah',
  _order:
   [ { name: 'verbose', value: true, from: 'argv' },
     { name: 'verbose', value: true, from: 'argv' },
     { name: 'verbose', value: true, from: 'argv' },
     { name: 'file', value: 'blah', from: 'argv' } ],
  _args: [] }
# args: []
```


See the ["examples"](examples/) dir for a number of starter examples using
some of dashdash's features.


# Environment variable integration

If you want to allow environment variables to specify options to your tool,
dashdash makes this easy. We can change the 'verbose' option in the example
above to include an 'env' field:

```javascript
    {
        names: ['verbose', 'v'],
        type: 'arrayOfBool',
        env: 'FOO_VERBOSE',         // <--- add this line
        help: 'Verbose output. Use multiple times for more verbose.'
    },
```

then the **"FOO_VERBOSE" environment variable** can be used to set this
option:

```shell
$ FOO_VERBOSE=1 node foo.js
# opts: { verbose: [ true ],
  _order: [ { name: 'verbose', value: true, from: 'env' } ],
  _args: [] }
# args: []
```

Boolean options will interpret the empty string as unset, '0' as false
and anything else as true.

```shell
$ FOO_VERBOSE= node examples/foo.js                 # not set
# opts: { _order: [], _args: [] }
# args: []

$ FOO_VERBOSE=0 node examples/foo.js                # '0' is false
# opts: { verbose: [ false ],
  _order: [ { key: 'verbose', value: false, from: 'env' } ],
  _args: [] }
# args: []

$ FOO_VERBOSE=1 node examples/foo.js                # true
# opts: { verbose: [ true ],
  _order: [ { key: 'verbose', value: true, from: 'env' } ],
  _args: [] }
# args: []

$ FOO_VERBOSE=boogabooga node examples/foo.js       # true
# opts: { verbose: [ true ],
  _order: [ { key: 'verbose', value: true, from: 'env' } ],
  _args: [] }
# args: []
```

Non-booleans can be used as well. Strings:

```shell
$ FOO_FILE=data.txt node examples/foo.js
# opts: { file: 'data.txt',
  _order: [ { key: 'file', value: 'data.txt', from: 'env' } ],
  _args: [] }
# args: []
```

Numbers:

```shell
$ FOO_TIMEOUT=5000 node examples/foo.js
# opts: { timeout: 5000,
  _order: [ { key: 'timeout', value: 5000, from: 'env' } ],
  _args: [] }
# args: []

$ FOO_TIMEOUT=blarg node examples/foo.js
foo: error: arg for "FOO_TIMEOUT" is not a positive integer: "blarg"
```

With the `includeEnv: true` config to `parser.help()` the environment
variable can also be included in **help output**:

    usage: node foo.js [OPTIONS]
    options:
        --version             Print tool version and exit.
        -h, --help            Print this help and exit.
        -v, --verbose         Verbose output. Use multiple times for more verbose.
                              Environment: FOO_VERBOSE=1
        -f FILE, --file=FILE  File to process


# Bash completion

Dashdash provides a simple way to create a Bash completion file that you
can place in your "bash_completion.d" directory -- sometimes that is
"/usr/local/etc/bash_completion.d/"). Features:

- Support for short and long opts
- Support for knowing which options take arguments
- Support for subcommands (e.g. 'git log <TAB>' to show just options for the
  log subcommand). See
  [node-cmdln](https://github.com/trentm/node-cmdln#bash-completion) for
  how to integrate that.
- Does the right thing with "--" to stop options.
- Custom optarg and arg types for custom completions.

Dashdash will return bash completion file content given a parser instance:

    var parser = dashdash.createParser({options: options});
    console.log( parser.bashCompletion({name: 'mycli'}) );

or directly from a `options` array of options specs:

    var code = dashdash.bashCompletionFromOptions({
        name: 'mycli',
        options: OPTIONS
    });

Write that content to "/usr/local/etc/bash_completion.d/mycli" and you will
have Bash completions for `mycli`. Alternatively you can write it to
any file (e.g. "~/.bashrc") and source it.

You could add a `--completion` hidden option to your tool that emits the
completion content and document for your users to call that to install
Bash completions.

See [examples/ddcompletion.js](examples/ddcompletion.js) for a complete
example, including how one can define bash functions for completion of custom
option types. Also see [node-cmdln](https://github.com/trentm/node-cmdln) for
how it uses this for Bash completion for full multi-subcommand tools.

- TODO: document specExtra
- TODO: document includeHidden
- TODO: document custom types, `function complete\_FOO` guide, completionType
- TODO: document argtypes


# Parser config

Parser construction (i.e. `dashdash.createParser(CONFIG)`) takes the
following fields:

- `options` (Array of option specs). Required. See the
  [Option specs](#option-specs) section below.

- `interspersed` (Boolean). Optional. Default is true. If true this allows
  interspersed arguments and options. I.e.:

        node ./tool.js -v arg1 arg2 -h   # '-h' is after interspersed args

  Set it to false to have '-h' **not** get parsed as an option in the above
  example.

- `allowUnknown` (Boolean).  Optional.  Default is false.  If false, this causes
  unknown arguments to throw an error.  I.e.:

        node ./tool.js -v arg1 --afe8asefksjefhas

  Set it to true to treat the unknown option as a positional
  argument.

  **Caveat**: When a shortopt group, such as `-xaz` contains a mix of
  known and unknown options, the *entire* group is passed through
  unmolested as a positional argument.

  Consider if you have a known short option `-a`, and parse the
  following command line:

        node ./tool.js -xaz

  where `-x` and `-z` are unknown.  There are multiple ways to
  interpret this:

    1. `-x` takes a value: `{x: 'az'}`
    2. `-x` and `-z` are both booleans: `{x:true,a:true,z:true}`

  Since dashdash does not know what `-x` and `-z` are, it can't know
  if you'd prefer to receive `{a:true,_args:['-x','-z']}` or
  `{x:'az'}`, or `{_args:['-xaz']}`. Leaving the positional arg unprocessed
  is the easiest mistake for the user to recover from.


# Option specs

Example using all fields (required fields are noted):

```javascript
{
    names: ['file', 'f'],       // Required (one of `names` or `name`).
    type: 'string',             // Required.
    completionType: 'filename',
    env: 'MYTOOL_FILE',
    help: 'Config file to load before running "mytool"',
    helpArg: 'PATH',
    helpWrap: false,
    default: path.resolve(process.env.HOME, '.mytoolrc')
}
```

Each option spec in the `options` array must/can have the following fields:

- `name` (String) or `names` (Array). Required. These give the option name
  and aliases. The first name (if more than one given) is the key for the
  parsed `opts` object.

- `type` (String). Required. One of:

    - bool
    - string
    - number
    - integer
    - positiveInteger
    - date (epoch seconds, e.g. 1396031701, or ISO 8601 format
      `YYYY-MM-DD[THH:MM:SS[.sss][Z]]`, e.g. "2014-03-28T18:35:01.489Z")
    - arrayOfBool
    - arrayOfString
    - arrayOfNumber
    - arrayOfInteger
    - arrayOfPositiveInteger
    - arrayOfDate

  FWIW, these names attempt to match with asserts on
  [assert-plus](https://github.com/mcavage/node-assert-plus).
  You can add your own custom option types with `dashdash.addOptionType`.
  See below.

- `completionType` (String). Optional. This is used for [Bash
  completion](#bash-completion) for an option argument. If not specified,
  then the value of `type` is used. Any string may be specified, but only the
  following values have meaning:

    - `none`: Provide no completions.
    - `file`: Bash's default completion (i.e. `complete -o default`), which
      includes filenames.
    - *Any string FOO for which a `function complete_FOO` Bash function is
      defined.* This is for custom completions for a given tool. Typically
      these custom functions are provided in the `specExtra` argument to
      `dashdash.bashCompletionFromOptions()`. See
      ["examples/ddcompletion.js"](examples/ddcompletion.js) for an example.

- `env` (String or Array of String). Optional. An environment variable name
  (or names) that can be used as a fallback for this option. For example,
  given a "foo.js" like this:

        var options = [{names: ['dry-run', 'n'], env: 'FOO_DRY_RUN'}];
        var opts = dashdash.parse({options: options});

  Both `node foo.js --dry-run` and `FOO_DRY_RUN=1 node foo.js` would result
  in `opts.dry_run = true`.

  An environment variable is only used as a fallback, i.e. it is ignored if
  the associated option is given in `argv`.

- `help` (String). Optional. Used for `parser.help()` output.

- `helpArg` (String). Optional. Used in help output as the placeholder for
  the option argument, e.g. the "PATH" in:

        ...
        -f PATH, --file=PATH    File to process
        ...

- `helpWrap` (Boolean). Optional, default true. Set this to `false` to have
  that option's `help` *not* be text wrapped in `<parser>.help()` output.

- `default`. Optional. A default value used for this option, if the
  option isn't specified in argv.

- `hidden` (Boolean). Optional, default false. If true, help output will not
  include this option. See also the `includeHidden` option to
  `bashCompletionFromOptions()` for [Bash completion](#bash-completion).


# Option group headings

You can add headings between option specs in the `options` array.  To do so,
simply add an object with only a `group` property -- the string to print as
the heading for the subsequent options in the array.  For example:

```javascript
var options = [
    {
        group: 'Armament Options'
    },
    {
        names: [ 'weapon', 'w' ],
        type: 'string'
    },
    {
        group: 'General Options'
    },
    {
        names: [ 'help', 'h' ],
        type: 'bool'
    }
];
...
```

Note: You can use an empty string, `{group: ''}`, to get a blank line in help
output between groups of options.


# Help config

The `parser.help(...)` function is configurable as follows:

        Options:
          Armament Options:
        ^^  -w WEAPON, --weapon=WEAPON  Weapon with which to crush. One of: |
       /                                sword, spear, maul                  |
      /   General Options:                                                  |
     /      -h, --help                  Print this help and exit.           |
    /   ^^^^                            ^                                   |
    \       `-- indent                   `-- helpCol              maxCol ---'
     `-- headingIndent

- `indent` (Number or String). Default 4. Set to a number (for that many
  spaces) or a string for the literal indent.
- `headingIndent` (Number or String). Default half length of `indent`. Set to
  a number (for that many spaces) or a string for the literal indent. This
  indent applies to group heading lines, between normal option lines.
- `nameSort` (String). Default is 'length'. By default the names are
  sorted to put the short opts first (i.e. '-h, --help' preferred
  to '--help, -h'). Set to 'none' to not do this sorting.
- `maxCol` (Number). Default 80. Note that reflow is just done on whitespace
  so a long token in the option help can overflow maxCol.
- `helpCol` (Number). If not set a reasonable value will be determined
  between `minHelpCol` and `maxHelpCol`.
- `minHelpCol` (Number). Default 20.
- `maxHelpCol` (Number). Default 40.
- `helpWrap` (Boolean). Default true. Set to `false` to have option `help`
  strings *not* be textwrapped to the helpCol..maxCol range.
- `includeEnv` (Boolean). Default false. If the option has associated
  environment variables (via the `env` option spec attribute), then
  append mentioned of those envvars to the help string.
- `includeDefault` (Boolean). Default false. If the option has a default value
  (via the `default` option spec attribute, or a default on the option's type),
  then a "Default: VALUE" string will be appended to the help string.


# Custom option types

Dashdash includes a good starter set of option types that it will parse for
you. However, you can add your own via:

    var dashdash = require('dashdash');
    dashdash.addOptionType({
        name: '...',
        takesArg: true,
        helpArg: '...',
        parseArg: function (option, optstr, arg) {
            ...
        },
        array: false,  // optional
        arrayFlatten: false,  // optional
        default: ...,   // optional
        completionType: ...  // optional
    });

For example, a simple option type that accepts 'yes', 'y', 'no' or 'n' as
a boolean argument would look like:

    var dashdash = require('dashdash');

    function parseYesNo(option, optstr, arg) {
        var argLower = arg.toLowerCase()
        if (~['yes', 'y'].indexOf(argLower)) {
            return true;
        } else if (~['no', 'n'].indexOf(argLower)) {
            return false;
        } else {
            throw new Error(format(
                'arg for "%s" is not "yes" or "no": "%s"',
                optstr, arg));
        }
    }

    dashdash.addOptionType({
        name: 'yesno'
        takesArg: true,
        helpArg: '<yes|no>',
        parseArg: parseYesNo
    });

    var options = {
        {names: ['answer', 'a'], type: 'yesno'}
    };
    var opts = dashdash.parse({options: options});

See "examples/custom-option-\*.js" for other examples.
See the `addOptionType` block comment in "lib/dashdash.js" for more details.
Please let me know [with an
issue](https://github.com/trentm/node-dashdash/issues/new) if you write a
generally useful one.



# Why

Why another node.js option parsing lib?

- `nopt` really is just for "tools like npm". Implicit opts (e.g. '--no-foo'
  works for every '--foo'). Can't disable abbreviated opts. Can't do multiple
  usages of same opt, e.g. '-vvv' (I think). Can't do grouped short opts.

- `optimist` has surprise interpretation of options (at least to me).
  Implicit opts mean ambiguities and poor error handling for fat-fingering.
  `process.exit` calls makes it hard to use as a libary.

- `optparse` Incomplete docs. Is this an attempted clone of Python's `optparse`.
  Not clear. Some divergence. `parser.on("name", ...)` API is weird.

- `argparse` Dep on underscore. No thanks just for option processing.
  `find lib | wc -l` -> `26`. Overkill.
  Argparse is a bit different anyway. Not sure I want that.

- `posix-getopt` No type validation. Though that isn't a killer. AFAIK can't
  have a long opt without a short alias. I.e. no `getopt_long` semantics.
  Also, no whizbang features like generated help output.

- ["commander.js"](https://github.com/visionmedia/commander.js): I wrote
  [a critique](http://trentm.com/2014/01/a-critique-of-commander-for-nodejs.html)
  a while back. It seems fine, but last I checked had
  [an outstanding bug](https://github.com/visionmedia/commander.js/pull/121)
  that would prevent me from using it.


# License

MIT. See LICENSE.txt.
# performance-now [![Build Status](https://travis-ci.org/braveg1rl/performance-now.png?branch=master)](https://travis-ci.org/braveg1rl/performance-now) [![Dependency Status](https://david-dm.org/braveg1rl/performance-now.png)](https://david-dm.org/braveg1rl/performance-now)

Implements a function similar to `performance.now` (based on `process.hrtime`).

Modern browsers have a `window.performance` object with - among others - a `now` method which gives time in milliseconds, but with sub-millisecond precision. This module offers the same function based on the Node.js native `process.hrtime` function.

Using `process.hrtime` means that the reported time will be monotonically increasing, and not subject to clock-drift.

According to the [High Resolution Time specification](http://www.w3.org/TR/hr-time/), the number of milliseconds reported by `performance.now` should be relative to the value of `performance.timing.navigationStart`.

In the current version of the module (2.0) the reported time is relative to the time the current Node process has started (inferred from `process.uptime()`).

Version 1.0 reported a different time. The reported time was relative to the time the module was loaded (i.e. the time it was first `require`d). If you need this functionality, version 1.0 is still available on NPM.

## Example usage

```javascript
var now = require("performance-now")
var start = now()
var end = now()
console.log(start.toFixed(3)) // the number of milliseconds the current node process is running
console.log((start-end).toFixed(3)) // ~ 0.002 on my system
```

Running the now function two times right after each other yields a time difference of a few microseconds. Given this overhead, I think it's best to assume that the precision of intervals computed with this method is not higher than 10 microseconds, if you don't know the exact overhead on your own system.

## License

performance-now is released under the [MIT License](http://opensource.org/licenses/MIT).
Copyright (c) 2017 Braveg1rl
# Form-Data [![NPM Module](https://img.shields.io/npm/v/form-data.svg)](https://www.npmjs.com/package/form-data) [![Join the chat at https://gitter.im/form-data/form-data](http://form-data.github.io/images/gitterbadge.svg)](https://gitter.im/form-data/form-data)

A library to create readable ```"multipart/form-data"``` streams. Can be used to submit forms and file uploads to other web applications.

The API of this library is inspired by the [XMLHttpRequest-2 FormData Interface][xhr2-fd].

[xhr2-fd]: http://dev.w3.org/2006/webapi/XMLHttpRequest-2/Overview.html#the-formdata-interface

[![Linux Build](https://img.shields.io/travis/form-data/form-data/v2.3.2.svg?label=linux:4.x-9.x)](https://travis-ci.org/form-data/form-data)
[![MacOS Build](https://img.shields.io/travis/form-data/form-data/v2.3.2.svg?label=macos:4.x-9.x)](https://travis-ci.org/form-data/form-data)
[![Windows Build](https://img.shields.io/appveyor/ci/alexindigo/form-data/v2.3.2.svg?label=windows:4.x-9.x)](https://ci.appveyor.com/project/alexindigo/form-data)

[![Coverage Status](https://img.shields.io/coveralls/form-data/form-data/v2.3.2.svg?label=code+coverage)](https://coveralls.io/github/form-data/form-data?branch=master)
[![Dependency Status](https://img.shields.io/david/form-data/form-data.svg)](https://david-dm.org/form-data/form-data)
[![bitHound Overall Score](https://www.bithound.io/github/form-data/form-data/badges/score.svg)](https://www.bithound.io/github/form-data/form-data)

## Install

```
npm install --save form-data
```

## Usage

In this example we are constructing a form with 3 fields that contain a string,
a buffer and a file stream.

``` javascript
var FormData = require('form-data');
var fs = require('fs');

var form = new FormData();
form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_file', fs.createReadStream('/foo/bar.jpg'));
```

Also you can use http-response stream:

``` javascript
var FormData = require('form-data');
var http = require('http');

var form = new FormData();

http.request('http://nodejs.org/images/logo.png', function(response) {
  form.append('my_field', 'my value');
  form.append('my_buffer', new Buffer(10));
  form.append('my_logo', response);
});
```

Or @mikeal's [request](https://github.com/request/request) stream:

``` javascript
var FormData = require('form-data');
var request = require('request');

var form = new FormData();

form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_logo', request('http://nodejs.org/images/logo.png'));
```

In order to submit this form to a web application, call ```submit(url, [callback])``` method:

``` javascript
form.submit('http://example.org/', function(err, res) {
  // res – response object (http.IncomingMessage)  //
  res.resume();
});

```

For more advanced request manipulations ```submit()``` method returns ```http.ClientRequest``` object, or you can choose from one of the alternative submission methods.

### Custom options

You can provide custom options, such as `maxDataSize`:

``` javascript
var FormData = require('form-data');

var form = new FormData({ maxDataSize: 20971520 });
form.append('my_field', 'my value');
form.append('my_buffer', /* something big */);
```

List of available options could be found in [combined-stream](https://github.com/felixge/node-combined-stream/blob/master/lib/combined_stream.js#L7-L15)

### Alternative submission methods

You can use node's http client interface:

``` javascript
var http = require('http');

var request = http.request({
  method: 'post',
  host: 'example.org',
  path: '/upload',
  headers: form.getHeaders()
});

form.pipe(request);

request.on('response', function(res) {
  console.log(res.statusCode);
});
```

Or if you would prefer the `'Content-Length'` header to be set for you:

``` javascript
form.submit('example.org/upload', function(err, res) {
  console.log(res.statusCode);
});
```

To use custom headers and pre-known length in parts:

``` javascript
var CRLF = '\r\n';
var form = new FormData();

var options = {
  header: CRLF + '--' + form.getBoundary() + CRLF + 'X-Custom-Header: 123' + CRLF + CRLF,
  knownLength: 1
};

form.append('my_buffer', buffer, options);

form.submit('http://example.com/', function(err, res) {
  if (err) throw err;
  console.log('Done');
});
```

Form-Data can recognize and fetch all the required information from common types of streams (```fs.readStream```, ```http.response``` and ```mikeal's request```), for some other types of streams you'd need to provide "file"-related information manually:

``` javascript
someModule.stream(function(err, stdout, stderr) {
  if (err) throw err;

  var form = new FormData();

  form.append('file', stdout, {
    filename: 'unicycle.jpg', // ... or:
    filepath: 'photos/toys/unicycle.jpg',
    contentType: 'image/jpeg',
    knownLength: 19806
  });

  form.submit('http://example.com/', function(err, res) {
    if (err) throw err;
    console.log('Done');
  });
});
```

The `filepath` property overrides `filename` and may contain a relative path. This is typically used when uploading [multiple files from a directory](https://wicg.github.io/entries-api/#dom-htmlinputelement-webkitdirectory).

For edge cases, like POST request to URL with query string or to pass HTTP auth credentials, object can be passed to `form.submit()` as first parameter:

``` javascript
form.submit({
  host: 'example.com',
  path: '/probably.php?extra=params',
  auth: 'username:password'
}, function(err, res) {
  console.log(res.statusCode);
});
```

In case you need to also send custom HTTP headers with the POST request, you can use the `headers` key in first parameter of `form.submit()`:

``` javascript
form.submit({
  host: 'example.com',
  path: '/surelynot.php',
  headers: {'x-test-header': 'test-header-value'}
}, function(err, res) {
  console.log(res.statusCode);
});
```

### Integration with other libraries

#### Request

Form submission using  [request](https://github.com/request/request):

```javascript
var formData = {
  my_field: 'my_value',
  my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
};

request.post({url:'http://service.com/upload', formData: formData}, function(err, httpResponse, body) {
  if (err) {
    return console.error('upload failed:', err);
  }
  console.log('Upload successful!  Server responded with:', body);
});
```

For more details see [request readme](https://github.com/request/request#multipartform-data-multipart-form-uploads).

#### node-fetch

You can also submit a form using [node-fetch](https://github.com/bitinn/node-fetch):

```javascript
var form = new FormData();

form.append('a', 1);

fetch('http://example.com', { method: 'POST', body: form })
    .then(function(res) {
        return res.json();
    }).then(function(json) {
        console.log(json);
    });
```

## Notes

- ```getLengthSync()``` method DOESN'T calculate length for streams, use ```knownLength``` options as workaround.
- Starting version `2.x` FormData has dropped support for `node@0.10.x`.

## License

Form-Data is released under the [MIT](License) license.
# Form-Data [![NPM Module](https://img.shields.io/npm/v/form-data.svg)](https://www.npmjs.com/package/form-data) [![Join the chat at https://gitter.im/form-data/form-data](http://form-data.github.io/images/gitterbadge.svg)](https://gitter.im/form-data/form-data)

A library to create readable ```"multipart/form-data"``` streams. Can be used to submit forms and file uploads to other web applications.

The API of this library is inspired by the [XMLHttpRequest-2 FormData Interface][xhr2-fd].

[xhr2-fd]: http://dev.w3.org/2006/webapi/XMLHttpRequest-2/Overview.html#the-formdata-interface

[![Linux Build](https://img.shields.io/travis/form-data/form-data/master.svg?label=linux:4.x-9.x)](https://travis-ci.org/form-data/form-data)
[![MacOS Build](https://img.shields.io/travis/form-data/form-data/master.svg?label=macos:4.x-9.x)](https://travis-ci.org/form-data/form-data)
[![Windows Build](https://img.shields.io/appveyor/ci/alexindigo/form-data/master.svg?label=windows:4.x-9.x)](https://ci.appveyor.com/project/alexindigo/form-data)

[![Coverage Status](https://img.shields.io/coveralls/form-data/form-data/master.svg?label=code+coverage)](https://coveralls.io/github/form-data/form-data?branch=master)
[![Dependency Status](https://img.shields.io/david/form-data/form-data.svg)](https://david-dm.org/form-data/form-data)
[![bitHound Overall Score](https://www.bithound.io/github/form-data/form-data/badges/score.svg)](https://www.bithound.io/github/form-data/form-data)

## Install

```
npm install --save form-data
```

## Usage

In this example we are constructing a form with 3 fields that contain a string,
a buffer and a file stream.

``` javascript
var FormData = require('form-data');
var fs = require('fs');

var form = new FormData();
form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_file', fs.createReadStream('/foo/bar.jpg'));
```

Also you can use http-response stream:

``` javascript
var FormData = require('form-data');
var http = require('http');

var form = new FormData();

http.request('http://nodejs.org/images/logo.png', function(response) {
  form.append('my_field', 'my value');
  form.append('my_buffer', new Buffer(10));
  form.append('my_logo', response);
});
```

Or @mikeal's [request](https://github.com/request/request) stream:

``` javascript
var FormData = require('form-data');
var request = require('request');

var form = new FormData();

form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_logo', request('http://nodejs.org/images/logo.png'));
```

In order to submit this form to a web application, call ```submit(url, [callback])``` method:

``` javascript
form.submit('http://example.org/', function(err, res) {
  // res – response object (http.IncomingMessage)  //
  res.resume();
});

```

For more advanced request manipulations ```submit()``` method returns ```http.ClientRequest``` object, or you can choose from one of the alternative submission methods.

### Custom options

You can provide custom options, such as `maxDataSize`:

``` javascript
var FormData = require('form-data');

var form = new FormData({ maxDataSize: 20971520 });
form.append('my_field', 'my value');
form.append('my_buffer', /* something big */);
```

List of available options could be found in [combined-stream](https://github.com/felixge/node-combined-stream/blob/master/lib/combined_stream.js#L7-L15)

### Alternative submission methods

You can use node's http client interface:

``` javascript
var http = require('http');

var request = http.request({
  method: 'post',
  host: 'example.org',
  path: '/upload',
  headers: form.getHeaders()
});

form.pipe(request);

request.on('response', function(res) {
  console.log(res.statusCode);
});
```

Or if you would prefer the `'Content-Length'` header to be set for you:

``` javascript
form.submit('example.org/upload', function(err, res) {
  console.log(res.statusCode);
});
```

To use custom headers and pre-known length in parts:

``` javascript
var CRLF = '\r\n';
var form = new FormData();

var options = {
  header: CRLF + '--' + form.getBoundary() + CRLF + 'X-Custom-Header: 123' + CRLF + CRLF,
  knownLength: 1
};

form.append('my_buffer', buffer, options);

form.submit('http://example.com/', function(err, res) {
  if (err) throw err;
  console.log('Done');
});
```

Form-Data can recognize and fetch all the required information from common types of streams (```fs.readStream```, ```http.response``` and ```mikeal's request```), for some other types of streams you'd need to provide "file"-related information manually:

``` javascript
someModule.stream(function(err, stdout, stderr) {
  if (err) throw err;

  var form = new FormData();

  form.append('file', stdout, {
    filename: 'unicycle.jpg', // ... or:
    filepath: 'photos/toys/unicycle.jpg',
    contentType: 'image/jpeg',
    knownLength: 19806
  });

  form.submit('http://example.com/', function(err, res) {
    if (err) throw err;
    console.log('Done');
  });
});
```

The `filepath` property overrides `filename` and may contain a relative path. This is typically used when uploading [multiple files from a directory](https://wicg.github.io/entries-api/#dom-htmlinputelement-webkitdirectory).

For edge cases, like POST request to URL with query string or to pass HTTP auth credentials, object can be passed to `form.submit()` as first parameter:

``` javascript
form.submit({
  host: 'example.com',
  path: '/probably.php?extra=params',
  auth: 'username:password'
}, function(err, res) {
  console.log(res.statusCode);
});
```

In case you need to also send custom HTTP headers with the POST request, you can use the `headers` key in first parameter of `form.submit()`:

``` javascript
form.submit({
  host: 'example.com',
  path: '/surelynot.php',
  headers: {'x-test-header': 'test-header-value'}
}, function(err, res) {
  console.log(res.statusCode);
});
```

### Integration with other libraries

#### Request

Form submission using  [request](https://github.com/request/request):

```javascript
var formData = {
  my_field: 'my_value',
  my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
};

request.post({url:'http://service.com/upload', formData: formData}, function(err, httpResponse, body) {
  if (err) {
    return console.error('upload failed:', err);
  }
  console.log('Upload successful!  Server responded with:', body);
});
```

For more details see [request readme](https://github.com/request/request#multipartform-data-multipart-form-uploads).

#### node-fetch

You can also submit a form using [node-fetch](https://github.com/bitinn/node-fetch):

```javascript
var form = new FormData();

form.append('a', 1);

fetch('http://example.com', { method: 'POST', body: form })
    .then(function(res) {
        return res.json();
    }).then(function(json) {
        console.log(json);
    });
```

## Notes

- ```getLengthSync()``` method DOESN'T calculate length for streams, use ```knownLength``` options as workaround.
- Starting version `2.x` FormData has dropped support for `node@0.10.x`.

## License

Form-Data is released under the [MIT](License) license.
![Async Logo](https://raw.githubusercontent.com/caolan/async/master/logo/async-logo_readme.jpg)

[![Build Status via Travis CI](https://travis-ci.org/caolan/async.svg?branch=master)](https://travis-ci.org/caolan/async)
[![NPM version](https://img.shields.io/npm/v/async.svg)](https://www.npmjs.com/package/async)
[![Coverage Status](https://coveralls.io/repos/caolan/async/badge.svg?branch=master)](https://coveralls.io/r/caolan/async?branch=master)
[![Join the chat at https://gitter.im/caolan/async](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/caolan/async?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![libhive - Open source examples](https://www.libhive.com/providers/npm/packages/async/examples/badge.svg)](https://www.libhive.com/providers/npm/packages/async)


Async is a utility module which provides straight-forward, powerful functions for working with asynchronous JavaScript. Although originally designed for use with [Node.js](https://nodejs.org/) and installable via `npm install --save async`, it can also be used directly in the browser.

For Documentation, visit <http://caolan.github.io/async/>

*For Async v1.5.x documentation, go [HERE](https://github.com/caolan/async/blob/v1.5.2/README.md)*
Browser-friendly inheritance fully compatible with standard node.js
[inherits](http://nodejs.org/api/util.html#util_util_inherits_constructor_superconstructor).

This package exports standard `inherits` from node.js `util` module in
node environment, but also provides alternative browser-friendly
implementation through [browser
field](https://gist.github.com/shtylman/4339901). Alternative
implementation is a literal copy of standard one located in standalone
module to avoid requiring of `util`. It also has a shim for old
browsers with no `Object.create` support.

While keeping you sure you are using standard `inherits`
implementation in node.js environment, it allows bundlers such as
[browserify](https://github.com/substack/node-browserify) to not
include full `util` package to your client code if all you need is
just `inherits` function. It worth, because browser shim for `util`
package is large and `inherits` is often the single function you need
from it.

It's recommended to use this package instead of
`require('util').inherits` for any code that has chances to be used
not only in node.js but in browser too.

## usage

```js
var inherits = require('inherits');
// then use exactly as the standard one
```

## note on version ~1.0

Version ~1.0 had completely different motivation and is not compatible
neither with 2.0 nor with standard node.js `inherits`.

If you are using version ~1.0 and planning to switch to ~2.0, be
careful:

* new version uses `super_` instead of `super` for referencing
  superclass
* new version overwrites current prototype while old one preserves any
  existing fields on it
# fast-deep-equal
The fastest deep equal

[![Build Status](https://travis-ci.org/epoberezkin/fast-deep-equal.svg?branch=master)](https://travis-ci.org/epoberezkin/fast-deep-equal)
[![npm version](https://badge.fury.io/js/fast-deep-equal.svg)](http://badge.fury.io/js/fast-deep-equal)
[![Coverage Status](https://coveralls.io/repos/github/epoberezkin/fast-deep-equal/badge.svg?branch=master)](https://coveralls.io/github/epoberezkin/fast-deep-equal?branch=master)


## Install

```bash
npm install fast-deep-equal
```


## Features

- ES5 compatible
- works in node.js (0.10+) and browsers (IE9+)
- checks equality of Date and RegExp objects by value.


## Usage

```javascript
var equal = require('fast-deep-equal');
console.log(equal({foo: 'bar'}, {foo: 'bar'})); // true
```


## Performance benchmark

```
fast-deep-equal x 82,915 ops/sec ±0.63% (89 runs sampled)
nano-equal x 50,506 ops/sec ±2.23% (86 runs sampled)
shallow-equal-fuzzy x 14,873 ops/sec ±3.19% (83 runs sampled)
underscore.isEqual x 16,055 ops/sec ±2.29% (85 runs sampled)
lodash.isEqual x 10,740 ops/sec ±1.04% (89 runs sampled)
deep-equal x 12,276 ops/sec ±2.44% (84 runs sampled)
deep-eql x 10,565 ops/sec ±0.89% (90 runs sampled)
assert.deepStrictEqual x 965 ops/sec ±2.99% (81 runs sampled)
The fastest is fast-deep-equal
```

To run benchmark (requires node.js 6+):

```bash
npm install
node benchmark
```


## License

[MIT](https://github.com/epoberezkin/fast-deep-equal/blob/master/LICENSE)
# extsprintf: extended POSIX-style sprintf

Stripped down version of s[n]printf(3c).  We make a best effort to throw an
exception when given a format string we don't understand, rather than ignoring
it, so that we won't break existing programs if/when we go implement the rest
of this.

This implementation currently supports specifying

* field alignment ('-' flag),
* zero-pad ('0' flag)
* always show numeric sign ('+' flag),
* field width
* conversions for strings, decimal integers, and floats (numbers).
* argument size specifiers.  These are all accepted but ignored, since
  Javascript has no notion of the physical size of an argument.

Everything else is currently unsupported, most notably: precision, unsigned
numbers, non-decimal numbers, and characters.

Besides the usual POSIX conversions, this implementation supports:

* `%j`: pretty-print a JSON object (using node's "inspect")
* `%r`: pretty-print an Error object

# Example

First, install it:

    # npm install extsprintf

Now, use it:

    var mod_extsprintf = require('extsprintf');
    console.log(mod_extsprintf.sprintf('hello %25s', 'world'));

outputs:

    hello                     world

# Also supported

**printf**: same args as sprintf, but prints the result to stdout

**fprintf**: same args as sprintf, preceded by a Node stream.  Prints the result
to the given stream.
# Pend

Dead-simple optimistic async helper.

## Usage

```js
var Pend = require('pend');
var pend = new Pend();
pend.max = 10; // defaults to Infinity
setTimeout(pend.hold(), 1000); // pend.wait will have to wait for this hold to finish
pend.go(function(cb) {
  console.log("this function is immediately executed");
  setTimeout(function() {
    console.log("calling cb 1");
    cb();
  }, 500);
});
pend.go(function(cb) {
  console.log("this function is also immediately executed");
  setTimeout(function() {
    console.log("calling cb 2");
    cb();
  }, 1000);
});
pend.wait(function(err) {
  console.log("this is excuted when the first 2 have returned.");
  console.log("err is a possible error in the standard callback style.");
});
```

Output:

```
this function is immediately executed
this function is also immediately executed
calling cb 1
calling cb 2
this is excuted when the first 2 have returned.
err is a possible error in the standard callback style.
```
[![Build Status](https://travis-ci.org/ReactiveX/rxjs.svg?branch=master)](https://travis-ci.org/ReactiveX/rxjs)
[![Coverage Status](https://coveralls.io/repos/github/ReactiveX/rxjs/badge.svg?branch=master)](https://coveralls.io/github/ReactiveX/rxjs?branch=master)
[![npm version](https://badge.fury.io/js/%40reactivex%2Frxjs.svg)](http://badge.fury.io/js/%40reactivex%2Frxjs)
[![Join the chat at https://gitter.im/Reactive-Extensions/RxJS](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Reactive-Extensions/RxJS?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Selenium Test Status](https://saucelabs.com/browser-matrix/rxjs5.svg)](https://saucelabs.com/u/rxjs5)

# RxJS 5

Reactive Extensions Library for JavaScript. This is a rewrite of [Reactive-Extensions/RxJS](https://github.com/Reactive-Extensions/RxJS) and is the latest production-ready version of RxJS. This rewrite is meant to have better performance, better modularity, better debuggable call stacks, while staying mostly backwards compatible, with some breaking changes that reduce the API surface.

[Apache 2.0 License](LICENSE.txt)

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Maintainer Guidelines](doc/maintainer-guidelines.md)
- [Creating Operators](doc/operator-creation.md)
- [Migrating From RxJS 4 to RxJS 5](MIGRATION.md)
- [API Documentation (WIP)](http://reactivex.io/rxjs)

## Versions In This Repository

- [master](https://github.com/ReactiveX/rxjs/commits/master) - commits that will be included in the next _minor_ or _patch_ release
- [next](https://github.com/ReactiveX/rxjs/commits/next) - commits that will be included in the next _major_ release (breaking changes)

Most PRs should be made to **master**, unless you know it is a breaking change.

## Important

By contributing or commenting on issues in this repository, whether you've read them or not, you're agreeing to the [Contributor Code of Conduct](CODE_OF_CONDUCT.md). Much like traffic laws, ignorance doesn't grant you immunity.

## Installation and Usage

### ES6 via npm

```sh
npm install rxjs
```

To import the entire core set of functionality:

```js
import Rx from 'rxjs/Rx';

Rx.Observable.of(1,2,3)
```

To import only what you need by patching (this is useful for size-sensitive bundling):

```js
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/map';

Observable.of(1,2,3).map(x => x + '!!!'); // etc
```

To import what you need and use it with proposed [bind operator](https://github.com/tc39/proposal-bind-operator):

> Note: This additional syntax requires [transpiler support](http://babeljs.io/docs/plugins/transform-function-bind/) and this syntax may be completely withdrawn from TC39 without notice! Use at your own risk.

```js
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { map } from 'rxjs/operator/map';

Observable::of(1,2,3)::map(x => x + '!!!'); // etc
```

### CommonJS via npm

To install this library for CommonJS (CJS) usage, use the following command:

```sh
npm install rxjs
```

Import all core functionality:

```js
var Rx = require('rxjs/Rx');

Rx.Observable.of(1,2,3); // etc
```

Import only what you need and patch Observable (this is useful in size-sensitive bundling scenarios):

```js
var Observable = require('rxjs/Observable').Observable;
// patch Observable with appropriate methods
require('rxjs/add/observable/of');
require('rxjs/add/operator/map');

Observable.of(1,2,3).map(function (x) { return x + '!!!'; }); // etc
```

Import operators and use them _manually_ you can do the following (this is also useful for bundling):

```js
var of = require('rxjs/observable/of').of;
var map = require('rxjs/operator/map').map;

map.call(of(1,2,3), function (x) { return x + '!!!'; });
```

You can also use the above method to build your own Observable and export it from your own module.


### All Module Types (CJS/ES6/AMD/TypeScript) via npm

To install this library via [npm](https://www.npmjs.org) **version 3**, use the following command:

```sh
npm install @reactivex/rxjs
```

This will include CJS/Global builds and can be used for all module types.

If you are using npm **version 2** before this library has achieved a stable version, you need to specify the library version explicitly:

```sh
npm install @reactivex/rxjs@5.0.0
```

### CDN

For CDN, you can use [unpkg](https://unpkg.com/):
  
https://unpkg.com/rxjs@version/bundles/Rx.min.js

*replace **version** with the current version. See [docs](http://reactivex.io/rxjs/manual/installation.html#cdn).*

#### Node.js Usage:

```js
var Rx = require('@reactivex/rxjs');

Rx.Observable.of('hello world')
  .subscribe(function(x) { console.log(x); });
```

## Goals

- Provide better performance than preceding versions of RxJS
- To model/follow the [Observable Spec Proposal](https://github.com/zenparsing/es-observable) to the observable.
- Provide more modular file structure in a variety of formats
- Provide more debuggable call stacks than preceding versions of RxJS

## Building/Testing

The build and test structure is fairly primitive at the moment. There are various npm scripts that can be run:

- build_es6: Transpiles the TypeScript files from `src/` to `dist/es6`
- build_cjs: Transpiles the ES6 files from `dist/es6` to `dist/cjs`
- build_amd: Transpiles the ES6 files from `dist/es6` to `dist/amd`
- build_global: Transpiles/Bundles the CommonJS files from `dist/cjs` to `dist/global/Rx.js`
- build_all: Performs all of the above in the proper order.
- build_test: builds ES6, then CommonJS, then runs the tests with `jasmine`
- build_perf: builds ES6, CommonJS, then global, then runs the performance tests with `protractor`
- build_docs: generates API documentation from `dist/es6` to `dist/docs`
- build_cover: runs `istanbul` code coverage against test cases
- test: runs tests with `jasmine`, must have built prior to running.
- tests2png: generates PNG marble diagrams from test cases.

`npm run info` will list available script.

### Example

```sh
# build all the things!
npm run build_all
```

## Performance Tests

Run `npm run build_perf` or `npm run perf` to run the performance tests with `protractor`.
Run `npm run perf_micro` to run micro performance test benchmarking operator.

## Adding documentation
RxNext uses [ESDoc](https://esdoc.org/) to generate API documentation. Refer to ESDoc's documentation for syntax. Run `npm run build_docs` to generate.

## Generating PNG marble diagrams

The script `npm run tests2png` requires some native packages installed locally: `imagemagick`, `graphicsmagick`, and `ghostscript`.

For Mac OS X with [Homebrew](http://brew.sh/):

- `brew install imagemagick`
- `brew install graphicsmagick`
- `brew install ghostscript`
- You may need to install the Ghostscript fonts manually:
  - Download the tarball from the [gs-fonts project](https://sourceforge.net/projects/gs-fonts)
  - `mkdir -p /usr/local/share/ghostscript && tar zxvf /path/to/ghostscript-fonts.tar.gz -C /usr/local/share/ghostscript`

For Debian Linux:

- `sudo add-apt-repository ppa:dhor/myway`
- `apt-get install imagemagick`
- `apt-get install graphicsmagick`
- `apt-get install ghostscript`

For Windows and other Operating Systems, check the download instructions here:

- http://imagemagick.org
- http://www.graphicsmagick.org
- http://www.ghostscript.com/
[![Build Status](https://travis-ci.org/ReactiveX/rxjs.svg?branch=master)](https://travis-ci.org/ReactiveX/rxjs)
[![Coverage Status](https://coveralls.io/repos/github/ReactiveX/rxjs/badge.svg?branch=master)](https://coveralls.io/github/ReactiveX/rxjs?branch=master)
[![npm version](https://badge.fury.io/js/%40reactivex%2Frxjs.svg)](http://badge.fury.io/js/%40reactivex%2Frxjs)
[![Join the chat at https://gitter.im/Reactive-Extensions/RxJS](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Reactive-Extensions/RxJS?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Selenium Test Status](https://saucelabs.com/browser-matrix/rxjs5.svg)](https://saucelabs.com/u/rxjs5)

# RxJS 5

Reactive Extensions Library for JavaScript. This is a rewrite of [Reactive-Extensions/RxJS](https://github.com/Reactive-Extensions/RxJS) and is the latest production-ready version of RxJS. This rewrite is meant to have better performance, better modularity, better debuggable call stacks, while staying mostly backwards compatible, with some breaking changes that reduce the API surface.

[Apache 2.0 License](LICENSE.txt)

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Maintainer Guidelines](doc/maintainer-guidelines.md)
- [Creating Operators](doc/operator-creation.md)
- [Migrating From RxJS 4 to RxJS 5](MIGRATION.md)
- [API Documentation (WIP)](http://reactivex.io/rxjs)

## Versions In This Repository

- [master](https://github.com/ReactiveX/rxjs/commits/master) - commits that will be included in the next _minor_ or _patch_ release
- [next](https://github.com/ReactiveX/rxjs/commits/next) - commits that will be included in the next _major_ release (breaking changes)

Most PRs should be made to **master**, unless you know it is a breaking change.

## Important

By contributing or commenting on issues in this repository, whether you've read them or not, you're agreeing to the [Contributor Code of Conduct](CODE_OF_CONDUCT.md). Much like traffic laws, ignorance doesn't grant you immunity.

## Installation and Usage

### ES6 via npm

```sh
npm install rxjs
```

To import the entire core set of functionality:

```js
import Rx from 'rxjs/Rx';

Rx.Observable.of(1,2,3)
```

To import only what you need by patching (this is useful for size-sensitive bundling):

```js
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/map';

Observable.of(1,2,3).map(x => x + '!!!'); // etc
```

To import what you need and use it with proposed [bind operator](https://github.com/tc39/proposal-bind-operator):

> Note: This additional syntax requires [transpiler support](http://babeljs.io/docs/plugins/transform-function-bind/) and this syntax may be completely withdrawn from TC39 without notice! Use at your own risk.

```js
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { map } from 'rxjs/operator/map';

Observable::of(1,2,3)::map(x => x + '!!!'); // etc
```

### CommonJS via npm

To install this library for CommonJS (CJS) usage, use the following command:

```sh
npm install rxjs
```

Import all core functionality:

```js
var Rx = require('rxjs/Rx');

Rx.Observable.of(1,2,3); // etc
```

Import only what you need and patch Observable (this is useful in size-sensitive bundling scenarios):

```js
var Observable = require('rxjs/Observable').Observable;
// patch Observable with appropriate methods
require('rxjs/add/observable/of');
require('rxjs/add/operator/map');

Observable.of(1,2,3).map(function (x) { return x + '!!!'; }); // etc
```

Import operators and use them _manually_ you can do the following (this is also useful for bundling):

```js
var of = require('rxjs/observable/of').of;
var map = require('rxjs/operator/map').map;

map.call(of(1,2,3), function (x) { return x + '!!!'; });
```

You can also use the above method to build your own Observable and export it from your own module.


### All Module Types (CJS/ES6/AMD/TypeScript) via npm

To install this library via [npm](https://www.npmjs.org) **version 3**, use the following command:

```sh
npm install @reactivex/rxjs
```

This will include CJS/Global builds and can be used for all module types.

If you are using npm **version 2** before this library has achieved a stable version, you need to specify the library version explicitly:

```sh
npm install @reactivex/rxjs@5.0.0
```

### CDN

For CDN, you can use [unpkg](https://unpkg.com/):
  
https://unpkg.com/rxjs@version/bundles/Rx.min.js

*replace **version** with the current version. See [docs](http://reactivex.io/rxjs/manual/installation.html#cdn).*

#### Node.js Usage:

```js
var Rx = require('@reactivex/rxjs');

Rx.Observable.of('hello world')
  .subscribe(function(x) { console.log(x); });
```

## Goals

- Provide better performance than preceding versions of RxJS
- To model/follow the [Observable Spec Proposal](https://github.com/zenparsing/es-observable) to the observable.
- Provide more modular file structure in a variety of formats
- Provide more debuggable call stacks than preceding versions of RxJS

## Building/Testing

The build and test structure is fairly primitive at the moment. There are various npm scripts that can be run:

- build_es6: Transpiles the TypeScript files from `src/` to `dist/es6`
- build_cjs: Transpiles the ES6 files from `dist/es6` to `dist/cjs`
- build_amd: Transpiles the ES6 files from `dist/es6` to `dist/amd`
- build_global: Transpiles/Bundles the CommonJS files from `dist/cjs` to `dist/global/Rx.js`
- build_all: Performs all of the above in the proper order.
- build_test: builds ES6, then CommonJS, then runs the tests with `jasmine`
- build_perf: builds ES6, CommonJS, then global, then runs the performance tests with `protractor`
- build_docs: generates API documentation from `dist/es6` to `dist/docs`
- build_cover: runs `istanbul` code coverage against test cases
- test: runs tests with `jasmine`, must have built prior to running.
- tests2png: generates PNG marble diagrams from test cases.

`npm run info` will list available script.

### Example

```sh
# build all the things!
npm run build_all
```

## Performance Tests

Run `npm run build_perf` or `npm run perf` to run the performance tests with `protractor`.
Run `npm run perf_micro` to run micro performance test benchmarking operator.

## Adding documentation
RxNext uses [ESDoc](https://esdoc.org/) to generate API documentation. Refer to ESDoc's documentation for syntax. Run `npm run build_docs` to generate.

## Generating PNG marble diagrams

The script `npm run tests2png` requires some native packages installed locally: `imagemagick`, `graphicsmagick`, and `ghostscript`.

For Mac OS X with [Homebrew](http://brew.sh/):

- `brew install imagemagick`
- `brew install graphicsmagick`
- `brew install ghostscript`
- You may need to install the Ghostscript fonts manually:
  - Download the tarball from the [gs-fonts project](https://sourceforge.net/projects/gs-fonts)
  - `mkdir -p /usr/local/share/ghostscript && tar zxvf /path/to/ghostscript-fonts.tar.gz -C /usr/local/share/ghostscript`

For Debian Linux:

- `sudo add-apt-repository ppa:dhor/myway`
- `apt-get install imagemagick`
- `apt-get install graphicsmagick`
- `apt-get install ghostscript`

For Windows and other Operating Systems, check the download instructions here:

- http://imagemagick.org
- http://www.graphicsmagick.org
- http://www.ghostscript.com/
[![Build Status](https://travis-ci.org/ReactiveX/rxjs.svg?branch=master)](https://travis-ci.org/ReactiveX/rxjs)
[![Coverage Status](https://coveralls.io/repos/github/ReactiveX/rxjs/badge.svg?branch=master)](https://coveralls.io/github/ReactiveX/rxjs?branch=master)
[![npm version](https://badge.fury.io/js/%40reactivex%2Frxjs.svg)](http://badge.fury.io/js/%40reactivex%2Frxjs)
[![Join the chat at https://gitter.im/Reactive-Extensions/RxJS](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Reactive-Extensions/RxJS?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Selenium Test Status](https://saucelabs.com/browser-matrix/rxjs5.svg)](https://saucelabs.com/u/rxjs5)

# RxJS 5

Reactive Extensions Library for JavaScript. This is a rewrite of [Reactive-Extensions/RxJS](https://github.com/Reactive-Extensions/RxJS) and is the latest production-ready version of RxJS. This rewrite is meant to have better performance, better modularity, better debuggable call stacks, while staying mostly backwards compatible, with some breaking changes that reduce the API surface.

[Apache 2.0 License](LICENSE.txt)

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Maintainer Guidelines](doc/maintainer-guidelines.md)
- [Creating Operators](doc/operator-creation.md)
- [Migrating From RxJS 4 to RxJS 5](MIGRATION.md)
- [API Documentation (WIP)](http://reactivex.io/rxjs)

## Versions In This Repository

- [master](https://github.com/ReactiveX/rxjs/commits/master) - commits that will be included in the next _minor_ or _patch_ release
- [next](https://github.com/ReactiveX/rxjs/commits/next) - commits that will be included in the next _major_ release (breaking changes)

Most PRs should be made to **master**, unless you know it is a breaking change.

## Important

By contributing or commenting on issues in this repository, whether you've read them or not, you're agreeing to the [Contributor Code of Conduct](CODE_OF_CONDUCT.md). Much like traffic laws, ignorance doesn't grant you immunity.

## Installation and Usage

### ES6 via npm

```sh
npm install rxjs
```

To import the entire core set of functionality:

```js
import Rx from 'rxjs/Rx';

Rx.Observable.of(1,2,3)
```

To import only what you need by patching (this is useful for size-sensitive bundling):

```js
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/map';

Observable.of(1,2,3).map(x => x + '!!!'); // etc
```

To import what you need and use it with proposed [bind operator](https://github.com/tc39/proposal-bind-operator):

> Note: This additional syntax requires [transpiler support](http://babeljs.io/docs/plugins/transform-function-bind/) and this syntax may be completely withdrawn from TC39 without notice! Use at your own risk.

```js
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { map } from 'rxjs/operator/map';

Observable::of(1,2,3)::map(x => x + '!!!'); // etc
```

### CommonJS via npm

To install this library for CommonJS (CJS) usage, use the following command:

```sh
npm install rxjs
```

Import all core functionality:

```js
var Rx = require('rxjs/Rx');

Rx.Observable.of(1,2,3); // etc
```

Import only what you need and patch Observable (this is useful in size-sensitive bundling scenarios):

```js
var Observable = require('rxjs/Observable').Observable;
// patch Observable with appropriate methods
require('rxjs/add/observable/of');
require('rxjs/add/operator/map');

Observable.of(1,2,3).map(function (x) { return x + '!!!'; }); // etc
```

Import operators and use them _manually_ you can do the following (this is also useful for bundling):

```js
var of = require('rxjs/observable/of').of;
var map = require('rxjs/operator/map').map;

map.call(of(1,2,3), function (x) { return x + '!!!'; });
```

You can also use the above method to build your own Observable and export it from your own module.


### All Module Types (CJS/ES6/AMD/TypeScript) via npm

To install this library via [npm](https://www.npmjs.org) **version 3**, use the following command:

```sh
npm install @reactivex/rxjs
```

This will include CJS/Global builds and can be used for all module types.

If you are using npm **version 2** before this library has achieved a stable version, you need to specify the library version explicitly:

```sh
npm install @reactivex/rxjs@5.0.0
```

### CDN

For CDN, you can use [unpkg](https://unpkg.com/):
  
https://unpkg.com/rxjs@version/bundles/Rx.min.js

*replace **version** with the current version. See [docs](http://reactivex.io/rxjs/manual/installation.html#cdn).*

#### Node.js Usage:

```js
var Rx = require('@reactivex/rxjs');

Rx.Observable.of('hello world')
  .subscribe(function(x) { console.log(x); });
```

## Goals

- Provide better performance than preceding versions of RxJS
- To model/follow the [Observable Spec Proposal](https://github.com/zenparsing/es-observable) to the observable.
- Provide more modular file structure in a variety of formats
- Provide more debuggable call stacks than preceding versions of RxJS

## Building/Testing

The build and test structure is fairly primitive at the moment. There are various npm scripts that can be run:

- build_es6: Transpiles the TypeScript files from `src/` to `dist/es6`
- build_cjs: Transpiles the ES6 files from `dist/es6` to `dist/cjs`
- build_amd: Transpiles the ES6 files from `dist/es6` to `dist/amd`
- build_global: Transpiles/Bundles the CommonJS files from `dist/cjs` to `dist/global/Rx.js`
- build_all: Performs all of the above in the proper order.
- build_test: builds ES6, then CommonJS, then runs the tests with `jasmine`
- build_perf: builds ES6, CommonJS, then global, then runs the performance tests with `protractor`
- build_docs: generates API documentation from `dist/es6` to `dist/docs`
- build_cover: runs `istanbul` code coverage against test cases
- test: runs tests with `jasmine`, must have built prior to running.
- tests2png: generates PNG marble diagrams from test cases.

`npm run info` will list available script.

### Example

```sh
# build all the things!
npm run build_all
```

## Performance Tests

Run `npm run build_perf` or `npm run perf` to run the performance tests with `protractor`.
Run `npm run perf_micro` to run micro performance test benchmarking operator.

## Adding documentation
RxNext uses [ESDoc](https://esdoc.org/) to generate API documentation. Refer to ESDoc's documentation for syntax. Run `npm run build_docs` to generate.

## Generating PNG marble diagrams

The script `npm run tests2png` requires some native packages installed locally: `imagemagick`, `graphicsmagick`, and `ghostscript`.

For Mac OS X with [Homebrew](http://brew.sh/):

- `brew install imagemagick`
- `brew install graphicsmagick`
- `brew install ghostscript`
- You may need to install the Ghostscript fonts manually:
  - Download the tarball from the [gs-fonts project](https://sourceforge.net/projects/gs-fonts)
  - `mkdir -p /usr/local/share/ghostscript && tar zxvf /path/to/ghostscript-fonts.tar.gz -C /usr/local/share/ghostscript`

For Debian Linux:

- `sudo add-apt-repository ppa:dhor/myway`
- `apt-get install imagemagick`
- `apt-get install graphicsmagick`
- `apt-get install ghostscript`

For Windows and other Operating Systems, check the download instructions here:

- http://imagemagick.org
- http://www.graphicsmagick.org
- http://www.ghostscript.com/
[![Build Status](https://travis-ci.org/ReactiveX/rxjs.svg?branch=master)](https://travis-ci.org/ReactiveX/rxjs)
[![Coverage Status](https://coveralls.io/repos/github/ReactiveX/rxjs/badge.svg?branch=master)](https://coveralls.io/github/ReactiveX/rxjs?branch=master)
[![npm version](https://badge.fury.io/js/%40reactivex%2Frxjs.svg)](http://badge.fury.io/js/%40reactivex%2Frxjs)
[![Join the chat at https://gitter.im/Reactive-Extensions/RxJS](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Reactive-Extensions/RxJS?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Selenium Test Status](https://saucelabs.com/browser-matrix/rxjs5.svg)](https://saucelabs.com/u/rxjs5)

# RxJS 5

Reactive Extensions Library for JavaScript. This is a rewrite of [Reactive-Extensions/RxJS](https://github.com/Reactive-Extensions/RxJS) and is the latest production-ready version of RxJS. This rewrite is meant to have better performance, better modularity, better debuggable call stacks, while staying mostly backwards compatible, with some breaking changes that reduce the API surface.

[Apache 2.0 License](LICENSE.txt)

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Maintainer Guidelines](doc/maintainer-guidelines.md)
- [Creating Operators](doc/operator-creation.md)
- [Migrating From RxJS 4 to RxJS 5](MIGRATION.md)
- [API Documentation (WIP)](http://reactivex.io/rxjs)

## Versions In This Repository

- [master](https://github.com/ReactiveX/rxjs/commits/master) - commits that will be included in the next _minor_ or _patch_ release
- [next](https://github.com/ReactiveX/rxjs/commits/next) - commits that will be included in the next _major_ release (breaking changes)

Most PRs should be made to **master**, unless you know it is a breaking change.

## Important

By contributing or commenting on issues in this repository, whether you've read them or not, you're agreeing to the [Contributor Code of Conduct](CODE_OF_CONDUCT.md). Much like traffic laws, ignorance doesn't grant you immunity.

## Installation and Usage

### ES6 via npm

```sh
npm install rxjs
```

To import the entire core set of functionality:

```js
import Rx from 'rxjs/Rx';

Rx.Observable.of(1,2,3)
```

To import only what you need by patching (this is useful for size-sensitive bundling):

```js
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/map';

Observable.of(1,2,3).map(x => x + '!!!'); // etc
```

To import what you need and use it with proposed [bind operator](https://github.com/tc39/proposal-bind-operator):

> Note: This additional syntax requires [transpiler support](http://babeljs.io/docs/plugins/transform-function-bind/) and this syntax may be completely withdrawn from TC39 without notice! Use at your own risk.

```js
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { map } from 'rxjs/operator/map';

Observable::of(1,2,3)::map(x => x + '!!!'); // etc
```

### CommonJS via npm

To install this library for CommonJS (CJS) usage, use the following command:

```sh
npm install rxjs
```

Import all core functionality:

```js
var Rx = require('rxjs/Rx');

Rx.Observable.of(1,2,3); // etc
```

Import only what you need and patch Observable (this is useful in size-sensitive bundling scenarios):

```js
var Observable = require('rxjs/Observable').Observable;
// patch Observable with appropriate methods
require('rxjs/add/observable/of');
require('rxjs/add/operator/map');

Observable.of(1,2,3).map(function (x) { return x + '!!!'; }); // etc
```

Import operators and use them _manually_ you can do the following (this is also useful for bundling):

```js
var of = require('rxjs/observable/of').of;
var map = require('rxjs/operator/map').map;

map.call(of(1,2,3), function (x) { return x + '!!!'; });
```

You can also use the above method to build your own Observable and export it from your own module.


### All Module Types (CJS/ES6/AMD/TypeScript) via npm

To install this library via [npm](https://www.npmjs.org) **version 3**, use the following command:

```sh
npm install @reactivex/rxjs
```

This will include CJS/Global builds and can be used for all module types.

If you are using npm **version 2** before this library has achieved a stable version, you need to specify the library version explicitly:

```sh
npm install @reactivex/rxjs@5.0.0
```

### CDN

For CDN, you can use [unpkg](https://unpkg.com/):
  
https://unpkg.com/rxjs@version/bundles/Rx.min.js

*replace **version** with the current version. See [docs](http://reactivex.io/rxjs/manual/installation.html#cdn).*

#### Node.js Usage:

```js
var Rx = require('@reactivex/rxjs');

Rx.Observable.of('hello world')
  .subscribe(function(x) { console.log(x); });
```

## Goals

- Provide better performance than preceding versions of RxJS
- To model/follow the [Observable Spec Proposal](https://github.com/zenparsing/es-observable) to the observable.
- Provide more modular file structure in a variety of formats
- Provide more debuggable call stacks than preceding versions of RxJS

## Building/Testing

The build and test structure is fairly primitive at the moment. There are various npm scripts that can be run:

- build_es6: Transpiles the TypeScript files from `src/` to `dist/es6`
- build_cjs: Transpiles the ES6 files from `dist/es6` to `dist/cjs`
- build_amd: Transpiles the ES6 files from `dist/es6` to `dist/amd`
- build_global: Transpiles/Bundles the CommonJS files from `dist/cjs` to `dist/global/Rx.js`
- build_all: Performs all of the above in the proper order.
- build_test: builds ES6, then CommonJS, then runs the tests with `jasmine`
- build_perf: builds ES6, CommonJS, then global, then runs the performance tests with `protractor`
- build_docs: generates API documentation from `dist/es6` to `dist/docs`
- build_cover: runs `istanbul` code coverage against test cases
- test: runs tests with `jasmine`, must have built prior to running.
- tests2png: generates PNG marble diagrams from test cases.

`npm run info` will list available script.

### Example

```sh
# build all the things!
npm run build_all
```

## Performance Tests

Run `npm run build_perf` or `npm run perf` to run the performance tests with `protractor`.
Run `npm run perf_micro` to run micro performance test benchmarking operator.

## Adding documentation
RxNext uses [ESDoc](https://esdoc.org/) to generate API documentation. Refer to ESDoc's documentation for syntax. Run `npm run build_docs` to generate.

## Generating PNG marble diagrams

The script `npm run tests2png` requires some native packages installed locally: `imagemagick`, `graphicsmagick`, and `ghostscript`.

For Mac OS X with [Homebrew](http://brew.sh/):

- `brew install imagemagick`
- `brew install graphicsmagick`
- `brew install ghostscript`
- You may need to install the Ghostscript fonts manually:
  - Download the tarball from the [gs-fonts project](https://sourceforge.net/projects/gs-fonts)
  - `mkdir -p /usr/local/share/ghostscript && tar zxvf /path/to/ghostscript-fonts.tar.gz -C /usr/local/share/ghostscript`

For Debian Linux:

- `sudo add-apt-repository ppa:dhor/myway`
- `apt-get install imagemagick`
- `apt-get install graphicsmagick`
- `apt-get install ghostscript`

For Windows and other Operating Systems, check the download instructions here:

- http://imagemagick.org
- http://www.graphicsmagick.org
- http://www.ghostscript.com/
JSON Schema is a repository for the JSON Schema specification, reference schemas and a CommonJS implementation of JSON Schema (not the only JavaScript implementation of JSON Schema, JSV is another excellent JavaScript validator).

Code is licensed under the AFL or BSD license as part of the Persevere 
project which is administered under the Dojo foundation,
and all contributions require a Dojo CLA.util-deprecate
==============
### The Node.js `util.deprecate()` function with browser support

In Node.js, this module simply re-exports the `util.deprecate()` function.

In the web browser (i.e. via browserify), a browser-specific implementation
of the `util.deprecate()` function is used.


## API

A `deprecate()` function is the only thing exposed by this module.

``` javascript
// setup:
exports.foo = deprecate(foo, 'foo() is deprecated, use bar() instead');


// users see:
foo();
// foo() is deprecated, use bar() instead
foo();
foo();
```


## License

(The MIT License)

Copyright (c) 2014 Nathan Rajlich <nathan@tootallnate.net>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
# yauzl

[![Build Status](https://travis-ci.org/thejoshwolfe/yauzl.svg?branch=master)](https://travis-ci.org/thejoshwolfe/yauzl)
[![Coverage Status](https://img.shields.io/coveralls/thejoshwolfe/yauzl.svg)](https://coveralls.io/r/thejoshwolfe/yauzl)

yet another unzip library for node. For zipping, see
[yazl](https://github.com/thejoshwolfe/yazl).

Design principles:

 * Follow the spec.
   Don't scan for local file headers.
   Read the central directory for file metadata.
   (see [No Streaming Unzip API](#no-streaming-unzip-api)).
 * Don't block the JavaScript thread.
   Use and provide async APIs.
 * Keep memory usage under control.
   Don't attempt to buffer entire files in RAM at once.
 * Never crash (if used properly).
   Don't let malformed zip files bring down client applications who are trying to catch errors.
 * Catch unsafe file names.
   See `validateFileName()`.

## Usage

```js
var yauzl = require("yauzl");

yauzl.open("path/to/file.zip", {lazyEntries: true}, function(err, zipfile) {
  if (err) throw err;
  zipfile.readEntry();
  zipfile.on("entry", function(entry) {
    if (/\/$/.test(entry.fileName)) {
      // Directory file names end with '/'.
      // Note that entires for directories themselves are optional.
      // An entry's fileName implicitly requires its parent directories to exist.
    } else {
      // file entry
      zipfile.openReadStream(entry, function(err, readStream) {
        if (err) throw err;
        readStream.on("end", function() {
          zipfile.readEntry();
        });
        readStream.pipe(somewhere);
      });
    }
  });
});
```

See also `examples/` for more usage examples.

## API

The default for every optional `callback` parameter is:

```js
function defaultCallback(err) {
  if (err) throw err;
}
```

### open(path, [options], [callback])

Calls `fs.open(path, "r")` and reads the `fd` effectively the same as `fromFd()` would.

`options` may be omitted or `null`. The defaults are `{autoClose: true, lazyEntries: false, decodeStrings: true, validateEntrySizes: true}`.

`autoClose` is effectively equivalent to:

```js
zipfile.once("end", function() {
  zipfile.close();
});
```

`lazyEntries` indicates that entries should be read only when `readEntry()` is called.
If `lazyEntries` is `false`, `entry` events will be emitted as fast as possible to allow `pipe()`ing
file data from all entries in parallel.
This is not recommended, as it can lead to out of control memory usage for zip files with many entries.
See [issue #22](https://github.com/thejoshwolfe/yauzl/issues/22).
If `lazyEntries` is `true`, an `entry` or `end` event will be emitted in response to each call to `readEntry()`.
This allows processing of one entry at a time, and will keep memory usage under control for zip files with many entries.

`decodeStrings` is the default and causes yauzl to decode strings with `CP437` or `UTF-8` as required by the spec.
The exact effects of turning this option off are:

* `zipfile.comment`, `entry.fileName`, and `entry.fileComment` will be `Buffer` objects instead of `String`s.
* Any Info-ZIP Unicode Path Extra Field will be ignored. See `extraFields`.
* Automatic file name validation will not be performed. See `validateFileName()`.

`validateEntrySizes` is the default and ensures that an entry's reported uncompressed size matches its actual uncompressed size.
This check happens as early as possible, which is either before emitting each `"entry"` event (for entries with no compression),
or during the `readStream` piping after calling `openReadStream()`.
See `openReadStream()` for more information on defending against zip bomb attacks.

The `callback` is given the arguments `(err, zipfile)`.
An `err` is provided if the End of Central Directory Record cannot be found, or if its metadata appears malformed.
This kind of error usually indicates that this is not a zip file.
Otherwise, `zipfile` is an instance of `ZipFile`.

### fromFd(fd, [options], [callback])

Reads from the fd, which is presumed to be an open .zip file.
Note that random access is required by the zip file specification,
so the fd cannot be an open socket or any other fd that does not support random access.

`options` may be omitted or `null`. The defaults are `{autoClose: false, lazyEntries: false, decodeStrings: true, validateEntrySizes: true}`.

See `open()` for the meaning of the options and callback.

### fromBuffer(buffer, [options], [callback])

Like `fromFd()`, but reads from a RAM buffer instead of an open file.
`buffer` is a `Buffer`.

If a `ZipFile` is acquired from this method,
it will never emit the `close` event,
and calling `close()` is not necessary.

`options` may be omitted or `null`. The defaults are `{lazyEntries: false, decodeStrings: true, validateEntrySizes: true}`.

See `open()` for the meaning of the options and callback.
The `autoClose` option is ignored for this method.

### fromRandomAccessReader(reader, totalSize, [options], [callback])

This method of reading a zip file allows clients to implement their own back-end file system.
For example, a client might translate read calls into network requests.

The `reader` parameter must be of a type that is a subclass of
[RandomAccessReader](#class-randomaccessreader) that implements the required methods.
The `totalSize` is a Number and indicates the total file size of the zip file.

`options` may be omitted or `null`. The defaults are `{autoClose: true, lazyEntries: false, decodeStrings: true, validateEntrySizes: true}`.

See `open()` for the meaning of the options and callback.

### dosDateTimeToDate(date, time)

Converts MS-DOS `date` and `time` data into a JavaScript `Date` object.
Each parameter is a `Number` treated as an unsigned 16-bit integer.
Note that this format does not support timezones,
so the returned object will use the local timezone.

### validateFileName(fileName)

Returns `null` or a `String` error message depending on the validity of `fileName`.
If `fileName` starts with `"/"` or `/[A-Za-z]:\//` or if it contains `".."` path segments or `"\\"`,
this function returns an error message appropriate for use like this:

```js
var errorMessage = yauzl.validateFileName(fileName);
if (errorMessage != null) throw new Error(errorMessage);
```

This function is automatically run for each entry, as long as `decodeStrings` is `true`.
See `open()` and `Event: "entry"` for more information.

### Class: ZipFile

The constructor for the class is not part of the public API.
Use `open()`, `fromFd()`, `fromBuffer()`, or `fromRandomAccessReader()` instead.

#### Event: "entry"

Callback gets `(entry)`, which is an `Entry`.
See `open()` and `readEntry()` for when this event is emitted.

If `decodeStrings` is `true`, entries emitted via this event have already passed file name validation.
See `validateFileName()` and `open()` for more information.

If `validateEntrySizes` is `true` and this entry's `compressionMethod` is `0` (stored without compression),
this entry has already passed entry size validation.
See `open()` for more information.

#### Event: "end"

Emitted after the last `entry` event has been emitted.
See `open()` and `readEntry()` for more info on when this event is emitted.

#### Event: "close"

Emitted after the fd is actually closed.
This is after calling `close()` (or after the `end` event when `autoClose` is `true`),
and after all stream pipelines created from `openReadStream()` have finished reading data from the fd.

If this `ZipFile` was acquired from `fromRandomAccessReader()`,
the "fd" in the previous paragraph refers to the `RandomAccessReader` implemented by the client.

If this `ZipFile` was acquired from `fromBuffer()`, this event is never emitted.

#### Event: "error"

Emitted in the case of errors with reading the zip file.
(Note that other errors can be emitted from the streams created from `openReadStream()` as well.)
After this event has been emitted, no further `entry`, `end`, or `error` events will be emitted,
but the `close` event may still be emitted.

#### readEntry()

Causes this `ZipFile` to emit an `entry` or `end` event (or an `error` event).
This method must only be called when this `ZipFile` was created with the `lazyEntries` option set to `true` (see `open()`).
When this `ZipFile` was created with the `lazyEntries` option set to `true`,
`entry` and `end` events are only ever emitted in response to this method call.

The event that is emitted in response to this method will not be emitted until after this method has returned,
so it is safe to call this method before attaching event listeners.

After calling this method, calling this method again before the response event has been emitted will cause undefined behavior.
Calling this method after the `end` event has been emitted will cause undefined behavior.
Calling this method after calling `close()` will cause undefined behavior.

#### openReadStream(entry, [options], callback)

`entry` must be an `Entry` object from this `ZipFile`.
`callback` gets `(err, readStream)`, where `readStream` is a `Readable Stream` that provides the file data for this entry.
If this zipfile is already closed (see `close()`), the `callback` will receive an `err`.

`options` may be omitted or `null`, and has the following defaults:

```js
{
  decompress: entry.isCompressed() ? true : null,
  decrypt: null,
  start: 0,                  // actually the default is null, see below
  end: entry.compressedSize, // actually the default is null, see below
}
```

If the entry is compressed (with a supported compression method),
and the `decompress` option is `true` (or omitted),
the read stream provides the decompressed data.
Omitting the `decompress` option is what most clients should do.

The `decompress` option must be `null` (or omitted) when the entry is not compressed (see `isCompressed()`),
and either `true` (or omitted) or `false` when the entry is compressed.
Specifying `decompress: false` for a compressed entry causes the read stream
to provide the raw compressed file data without going through a zlib inflate transform.

If the entry is encrypted (see `isEncrypted()`), clients may want to avoid calling `openReadStream()` on the entry entirely.
Alternatively, clients may call `openReadStream()` for encrypted entries and specify `decrypt: false`.
If the entry is also compressed, clients must *also* specify `decompress: false`.
Specifying `decrypt: false` for an encrypted entry causes the read stream to provide the raw, still-encrypted file data.
(This data includes the 12-byte header described in the spec.)

The `decrypt` option must be `null` (or omitted) for non-encrypted entries, and `false` for encrypted entries.
Omitting the `decrypt` option (or specifying it as `null`) for an encrypted entry
will result in the `callback` receiving an `err`.
This default behavior is so that clients not accounting for encrypted files aren't surprised by bogus file data.

The `start` (inclusive) and `end` (exclusive) options are byte offsets into this entry's file data,
and can be used to obtain part of an entry's file data rather than the whole thing.
If either of these options are specified and non-`null`,
then the above options must be used to obain the file's raw data.
Speficying `{start: 0, end: entry.compressedSize}` will result in the complete file,
which is effectively the default values for these options,
but note that unlike omitting the options, when you specify `start` or `end` as any non-`null` value,
the above requirement is still enforced that you must also pass the appropriate options to get the file's raw data.

It's possible for the `readStream` provided to the `callback` to emit errors for several reasons.
For example, if zlib cannot decompress the data, the zlib error will be emitted from the `readStream`.
Two more error cases (when `validateEntrySizes` is `true`) are if the decompressed data has too many
or too few actual bytes compared to the reported byte count from the entry's `uncompressedSize` field.
yauzl notices this false information and emits an error from the `readStream`
after some number of bytes have already been piped through the stream.

This check allows clients to trust the `uncompressedSize` field in `Entry` objects.
Guarding against [zip bomb](http://en.wikipedia.org/wiki/Zip_bomb) attacks can be accomplished by
doing some heuristic checks on the size metadata and then watching out for the above errors.
Such heuristics are outside the scope of this library,
but enforcing the `uncompressedSize` is implemented here as a security feature.

It is possible to destroy the `readStream` before it has piped all of its data.
To do this, call `readStream.destroy()`.
You must `unpipe()` the `readStream` from any destination before calling `readStream.destroy()`.
If this zipfile was created using `fromRandomAccessReader()`, the `RandomAccessReader` implementation
must provide readable streams that implement a `.destroy()` method (see `randomAccessReader._readStreamForRange()`)
in order for calls to `readStream.destroy()` to work in this context.

#### close()

Causes all future calls to `openReadStream()` to fail,
and closes the fd after all streams created by `openReadStream()` have emitted their `end` events.

If the `autoClose` option is set to `true` (see `open()`),
this function will be called automatically effectively in response to this object's `end` event.

If the `lazyEntries` option is set to `false` (see `open()`) and this object's `end` event has not been emitted yet,
this function causes undefined behavior.
If the `lazyEntries` option is set to `true`,
you can call this function instead of calling `readEntry()` to abort reading the entries of a zipfile.

It is safe to call this function multiple times; after the first call, successive calls have no effect.
This includes situations where the `autoClose` option effectively calls this function for you.

#### isOpen

`Boolean`. `true` until `close()` is called; then it's `false`.

#### entryCount

`Number`. Total number of central directory records.

#### comment

`String`. Always decoded with `CP437` per the spec.

If `decodeStrings` is `false` (see `open()`), this field is the undecoded `Buffer` instead of a decoded `String`.

### Class: Entry

Objects of this class represent Central Directory Records.
Refer to the zipfile specification for more details about these fields.

These fields are of type `Number`:

 * `versionMadeBy`
 * `versionNeededToExtract`
 * `generalPurposeBitFlag`
 * `compressionMethod`
 * `lastModFileTime` (MS-DOS format, see `getLastModDateTime`)
 * `lastModFileDate` (MS-DOS format, see `getLastModDateTime`)
 * `crc32`
 * `compressedSize`
 * `uncompressedSize`
 * `fileNameLength` (bytes)
 * `extraFieldLength` (bytes)
 * `fileCommentLength` (bytes)
 * `internalFileAttributes`
 * `externalFileAttributes`
 * `relativeOffsetOfLocalHeader`

#### fileName

`String`.
Following the spec, the bytes for the file name are decoded with
`UTF-8` if `generalPurposeBitFlag & 0x800`, otherwise with `CP437`.
Alternatively, this field may be populated from the Info-ZIP Unicode Path Extra Field
(see `extraFields`).

This field is automatically validated by `validateFileName()` before yauzl emits an "entry" event.
If this field would contain unsafe characters, yauzl emits an error instead of an entry.

If `decodeStrings` is `false` (see `open()`), this field is the undecoded `Buffer` instead of a decoded `String`.
Therefore, `generalPurposeBitFlag` and any Info-ZIP Unicode Path Extra Field are ignored.
Furthermore, no automatic file name validation is performed for this file name.

#### extraFields

`Array` with each entry in the form `{id: id, data: data}`,
where `id` is a `Number` and `data` is a `Buffer`.

This library looks for and reads the ZIP64 Extended Information Extra Field (0x0001)
in order to support ZIP64 format zip files.

This library also looks for and reads the Info-ZIP Unicode Path Extra Field (0x7075)
in order to support some zipfiles that use it instead of General Purpose Bit 8
to convey `UTF-8` file names.
When the field is identified and verified to be reliable (see the zipfile spec),
the the file name in this field is stored in the `fileName` property,
and the file name in the central directory record for this entry is ignored.
Note that when `decodeStrings` is false, all Info-ZIP Unicode Path Extra Fields are ignored.

None of the other fields are considered significant by this library.
Fields that this library reads are left unalterned in the `extraFields` array.

#### fileComment

`String` decoded with the charset indicated by `generalPurposeBitFlag & 0x800` as with the `fileName`.
(The Info-ZIP Unicode Path Extra Field has no effect on the charset used for this field.)

If `decodeStrings` is `false` (see `open()`), this field is the undecoded `Buffer` instead of a decoded `String`.

Prior to yauzl version 2.7.0, this field was erroneously documented as `comment` instead of `fileComment`.
For compatibility with any code that uses the field name `comment`,
yauzl creates an alias field named `comment` which is identical to `fileComment`.

#### getLastModDate()

Effectively implemented as:

```js
return dosDateTimeToDate(this.lastModFileDate, this.lastModFileTime);
```

#### isEncrypted()

Returns is this entry encrypted with "Traditional Encryption".
Effectively implemented as:

```js
return (this.generalPurposeBitFlag & 0x1) !== 0;
```

See `openReadStream()` for the implications of this value.

Note that "Strong Encryption" is not supported, and will result in an `"error"` event emitted from the `ZipFile`.

#### isCompressed()

Effectively implemented as:

```js
return this.compressionMethod === 8;
```

See `openReadStream()` for the implications of this value.

### Class: RandomAccessReader

This class is meant to be subclassed by clients and instantiated for the `fromRandomAccessReader()` function.

An example implementation can be found in `test/test.js`.

#### randomAccessReader._readStreamForRange(start, end)

Subclasses *must* implement this method.

`start` and `end` are Numbers and indicate byte offsets from the start of the file.
`end` is exclusive, so `_readStreamForRange(0x1000, 0x2000)` would indicate to read `0x1000` bytes.
`end - start` will always be at least `1`.

This method should return a readable stream which will be `pipe()`ed into another stream.
It is expected that the readable stream will provide data in several chunks if necessary.
If the readable stream provides too many or too few bytes, an error will be emitted.
(Note that `validateEntrySizes` has no effect on this check,
because this is a low-level API that should behave correctly regardless of the contents of the file.)
Any errors emitted on the readable stream will be handled and re-emitted on the client-visible stream
(returned from `zipfile.openReadStream()`) or provided as the `err` argument to the appropriate callback
(for example, for `fromRandomAccessReader()`).

The returned stream *must* implement a method `.destroy()`
if you call `readStream.destroy()` on streams you get from `openReadStream()`.
If you never call `readStream.destroy()`, then streams returned from this method do not need to implement a method `.destroy()`.
`.destroy()` should abort any streaming that is in progress and clean up any associated resources.
`.destroy()` will only be called after the stream has been `unpipe()`d from its destination.

Note that the stream returned from this method might not be the same object that is provided by `openReadStream()`.
The stream returned from this method might be `pipe()`d through one or more filter streams (for example, a zlib inflate stream).

#### randomAccessReader.read(buffer, offset, length, position, callback)

Subclasses may implement this method.
The default implementation uses `createReadStream()` to fill the `buffer`.

This method should behave like `fs.read()`.

#### randomAccessReader.close(callback)

Subclasses may implement this method.
The default implementation is effectively `setImmediate(callback);`.

`callback` takes parameters `(err)`.

This method is called once the all streams returned from `_readStreamForRange()` have ended,
and no more `_readStreamForRange()` or `read()` requests will be issued to this object.

## How to Avoid Crashing

When a malformed zipfile is encountered, the default behavior is to crash (throw an exception).
If you want to handle errors more gracefully than this,
be sure to do the following:

 * Provide `callback` parameters where they are allowed, and check the `err` parameter.
 * Attach a listener for the `error` event on any `ZipFile` object you get from `open()`, `fromFd()`, `fromBuffer()`, or `fromRandomAccessReader()`.
 * Attach a listener for the `error` event on any stream you get from `openReadStream()`.

Minor version updates to yauzl will not add any additional requirements to this list.

## Limitations

### No Streaming Unzip API

Due to the design of the .zip file format, it's impossible to interpret a .zip file from start to finish
(such as from a readable stream) without sacrificing correctness.
The Central Directory, which is the authority on the contents of the .zip file, is at the end of a .zip file, not the beginning.
A streaming API would need to either buffer the entire .zip file to get to the Central Directory before interpreting anything
(defeating the purpose of a streaming interface), or rely on the Local File Headers which are interspersed through the .zip file.
However, the Local File Headers are explicitly denounced in the spec as being unreliable copies of the Central Directory,
so trusting them would be a violation of the spec.

Any library that offers a streaming unzip API must make one of the above two compromises,
which makes the library either dishonest or nonconformant (usually the latter).
This library insists on correctness and adherence to the spec, and so does not offer a streaming API.

### Limitted ZIP64 Support

For ZIP64, only zip files smaller than `8PiB` are supported,
not the full `16EiB` range that a 64-bit integer should be able to index.
This is due to the JavaScript Number type being an IEEE 754 double precision float.

The Node.js `fs` module probably has this same limitation.

### ZIP64 Extensible Data Sector Is Ignored

The spec does not allow zip file creators to put arbitrary data here,
but rather reserves its use for PKWARE and mentions something about Z390.
This doesn't seem useful to expose in this library, so it is ignored.

### No Multi-Disk Archive Support

This library does not support multi-disk zip files.
The multi-disk fields in the zipfile spec were intended for a zip file to span multiple floppy disks,
which probably never happens now.
If the "number of this disk" field in the End of Central Directory Record is not `0`,
the `open()`, `fromFd()`, `fromBuffer()`, or `fromRandomAccessReader()` `callback` will receive an `err`.
By extension the following zip file fields are ignored by this library and not provided to clients:

 * Disk where central directory starts
 * Number of central directory records on this disk
 * Disk number where file starts

### Limited Encryption Handling

You can detect when a file entry is encrypted with "Traditional Encryption" via `isEncrypted()`,
but yauzl will not help you decrypt it.
See `openReadStream()`.

If a zip file contains file entries encrypted with "Strong Encryption", yauzl emits an error.

If the central directory is encrypted or compressed, yauzl emits an error.

### Local File Headers Are Ignored

Many unzip libraries mistakenly read the Local File Header data in zip files.
This data is officially defined to be redundant with the Central Directory information,
and is not to be trusted.
Aside from checking the signature, yauzl ignores the content of the Local File Header.

### No CRC-32 Checking

This library provides the `crc32` field of `Entry` objects read from the Central Directory.
However, this field is not used for anything in this library.

### versionNeededToExtract Is Ignored

The field `versionNeededToExtract` is ignored,
because this library doesn't support the complete zip file spec at any version,

### No Support For Obscure Compression Methods

Regarding the `compressionMethod` field of `Entry` objects,
only method `0` (stored with no compression)
and method `8` (deflated) are supported.
Any of the other 15 official methods will cause the `openReadStream()` `callback` to receive an `err`.

### Data Descriptors Are Ignored

There may or may not be Data Descriptor sections in a zip file.
This library provides no support for finding or interpreting them.

### Archive Extra Data Record Is Ignored

There may or may not be an Archive Extra Data Record section in a zip file.
This library provides no support for finding or interpreting it.

### No Language Encoding Flag Support

Zip files officially support charset encodings other than CP437 and UTF-8,
but the zip file spec does not specify how it works.
This library makes no attempt to interpret the Language Encoding Flag.

## Change History

 * 2.8.0
   * Added option `validateEntrySizes`. [issue #53](https://github.com/thejoshwolfe/yauzl/issues/53)
   * Added `examples/promises.js`
   * Added ability to read raw file data via `decompress` and `decrypt` options. [issue #11](https://github.com/thejoshwolfe/yauzl/issues/11), [issue #38](https://github.com/thejoshwolfe/yauzl/issues/38), [pull #39](https://github.com/thejoshwolfe/yauzl/pull/39)
   * Added `start` and `end` options to `openReadStream()`. [issue #38](https://github.com/thejoshwolfe/yauzl/issues/38)
 * 2.7.0
   * Added option `decodeStrings`. [issue #42](https://github.com/thejoshwolfe/yauzl/issues/42)
   * Fixed documentation for `entry.fileComment` and added compatibility alias. [issue #47](https://github.com/thejoshwolfe/yauzl/issues/47)
 * 2.6.0
   * Support Info-ZIP Unicode Path Extra Field, used by WinRAR for Chinese file names. [issue #33](https://github.com/thejoshwolfe/yauzl/issues/33)
 * 2.5.0
   * Ignore malformed Extra Field that is common in Android .apk files. [issue #31](https://github.com/thejoshwolfe/yauzl/issues/31)
 * 2.4.3
   * Fix crash when parsing malformed Extra Field buffers. [issue #31](https://github.com/thejoshwolfe/yauzl/issues/31)
 * 2.4.2
   * Remove .npmignore and .travis.yml from npm package.
 * 2.4.1
   * Fix error handling.
 * 2.4.0
   * Add ZIP64 support. [issue #6](https://github.com/thejoshwolfe/yauzl/issues/6)
   * Add `lazyEntries` option. [issue #22](https://github.com/thejoshwolfe/yauzl/issues/22)
   * Add `readStream.destroy()` method. [issue #26](https://github.com/thejoshwolfe/yauzl/issues/26)
   * Add `fromRandomAccessReader()`. [issue #14](https://github.com/thejoshwolfe/yauzl/issues/14)
   * Add `examples/unzip.js`.
 * 2.3.1
   * Documentation updates.
 * 2.3.0
   * Check that `uncompressedSize` is correct, or else emit an error. [issue #13](https://github.com/thejoshwolfe/yauzl/issues/13)
 * 2.2.1
   * Update dependencies.
 * 2.2.0
   * Update dependencies.
 * 2.1.0
   * Remove dependency on `iconv`.
 * 2.0.3
   * Fix crash when trying to read a 0-byte file.
 * 2.0.2
   * Fix event behavior after errors.
 * 2.0.1
   * Fix bug with using `iconv`.
 * 2.0.0
   * Initial release.
☣️ **Warning**: This branch is used to generate documentation from v1 branch.
Don't merge or delete it.

See [master](https://github.com/date-fns/date-fns) for the actual date-fns version.

See [v1](https://github.com/date-fns/date-fns/tree/v1) branch for the latest v1 version.
# isexe

Minimal module to check if a file is executable, and a normal file.

Uses `fs.stat` and tests against the `PATHEXT` environment variable on
Windows.

## USAGE

```javascript
var isexe = require('isexe')
isexe('some-file-name', function (err, isExe) {
  if (err) {
    console.error('probably file does not exist or something', err)
  } else if (isExe) {
    console.error('this thing can be run')
  } else {
    console.error('cannot be run')
  }
})

// same thing but synchronous, throws errors
var isExe = isexe.sync('some-file-name')

// treat errors as just "not executable"
isexe('maybe-missing-file', { ignoreErrors: true }, callback)
var isExe = isexe.sync('maybe-missing-file', { ignoreErrors: true })
```

## API

### `isexe(path, [options], [callback])`

Check if the path is executable.  If no callback provided, and a
global `Promise` object is available, then a Promise will be returned.

Will raise whatever errors may be raised by `fs.stat`, unless
`options.ignoreErrors` is set to true.

### `isexe.sync(path, [options])`

Same as `isexe` but returns the value and throws any errors raised.

### Options

* `ignoreErrors` Treat all errors as "no, this is not executable", but
  don't raise them.
* `uid` Number to use as the user id
* `gid` Number to use as the group id
* `pathExt` List of path extensions to use instead of `PATHEXT`
  environment variable on Windows.
oauth-sign
==========

OAuth 1 signing. Formerly a vendor lib in mikeal/request, now a standalone module. 
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
# HAR Validator [![version][npm-version]][npm-url] [![License][license-image]][license-url]

> Extremely fast HTTP Archive ([HAR](https://github.com/ahmadnassri/har-spec/blob/master/versions/1.2.md)) validator using JSON Schema.

[![Build Status][travis-image]][travis-url]
[![Downloads][npm-downloads]][npm-url]
[![Code Climate][codeclimate-quality]][codeclimate-url]
[![Coverage Status][codeclimate-coverage]][codeclimate-url]
[![Dependency Status][dependencyci-image]][dependencyci-url]
[![Dependencies][david-image]][david-url]

## Install

```bash
npm install --only=production --save har-validator
```

## CLI Usage

Please refer to [`har-cli`](https://github.com/ahmadnassri/har-cli) for more info.

## API

**Note**: as of [`v2.0.0`](https://github.com/ahmadnassri/har-validator/releases/tag/v2.0.0) this module defaults to Promise based API. *For backward compatibility with `v1.x` an [async/callback API](docs/async.md) is also provided*

- [async API](docs/async.md)
- [callback API](docs/async.md)
- [Promise API](docs/promise.md) *(default)*

----
> :copyright: [ahmadnassri.com](https://www.ahmadnassri.com/) &nbsp;&middot;&nbsp;
> License: [ISC][license-url] &nbsp;&middot;&nbsp;
> Github: [@ahmadnassri](https://github.com/ahmadnassri) &nbsp;&middot;&nbsp;
> Twitter: [@ahmadnassri](https://twitter.com/ahmadnassri)

[license-url]: http://choosealicense.com/licenses/isc/
[license-image]: https://img.shields.io/github/license/ahmadnassri/har-validator.svg?style=flat-square

[travis-url]: https://travis-ci.org/ahmadnassri/har-validator
[travis-image]: https://img.shields.io/travis/ahmadnassri/har-validator.svg?style=flat-square

[npm-url]: https://www.npmjs.com/package/har-validator
[npm-version]: https://img.shields.io/npm/v/har-validator.svg?style=flat-square
[npm-downloads]: https://img.shields.io/npm/dm/har-validator.svg?style=flat-square

[codeclimate-url]: https://codeclimate.com/github/ahmadnassri/har-validator
[codeclimate-quality]: https://img.shields.io/codeclimate/github/ahmadnassri/har-validator.svg?style=flat-square
[codeclimate-coverage]: https://img.shields.io/codeclimate/coverage/github/ahmadnassri/har-validator.svg?style=flat-square

[david-url]: https://david-dm.org/ahmadnassri/har-validator
[david-image]: https://img.shields.io/david/ahmadnassri/har-validator.svg?style=flat-square

[dependencyci-url]: https://dependencyci.com/github/ahmadnassri/har-validator
[dependencyci-image]: https://dependencyci.com/github/ahmadnassri/har-validator/badge?style=flat-square
# string_decoder

***Node-core v8.9.4 string_decoder for userland***


[![NPM](https://nodei.co/npm/string_decoder.png?downloads=true&downloadRank=true)](https://nodei.co/npm/string_decoder/)
[![NPM](https://nodei.co/npm-dl/string_decoder.png?&months=6&height=3)](https://nodei.co/npm/string_decoder/)


```bash
npm install --save string_decoder
```

***Node-core string_decoder for userland***

This package is a mirror of the string_decoder implementation in Node-core.

Full documentation may be found on the [Node.js website](https://nodejs.org/dist/v8.9.4/docs/api/).

As of version 1.0.0 **string_decoder** uses semantic versioning.

## Previous versions

Previous version numbers match the versions found in Node core, e.g. 0.10.24 matches Node 0.10.24, likewise 0.11.10 matches Node 0.11.10.

## Update

The *build/* directory contains a build script that will scrape the source from the [nodejs/node](https://github.com/nodejs/node) repo given a specific Node version.

## Streams Working Group

`string_decoder` is maintained by the Streams Working Group, which
oversees the development and maintenance of the Streams API within
Node.js. The responsibilities of the Streams Working Group include:

* Addressing stream issues on the Node.js issue tracker.
* Authoring and editing stream documentation within the Node.js project.
* Reviewing changes to stream subclasses within the Node.js project.
* Redirecting changes to streams from the Node.js project to this
  project.
* Assisting in the implementation of stream providers within Node.js.
* Recommending versions of `readable-stream` to be included in Node.js.
* Messaging about the future of streams to give the community advance
  notice of changes.

See [readable-stream](https://github.com/nodejs/readable-stream) for
more details.
# isStream

[![Build Status](https://secure.travis-ci.org/rvagg/isstream.png)](http://travis-ci.org/rvagg/isstream)

**Test if an object is a `Stream`**

[![NPM](https://nodei.co/npm/isstream.svg)](https://nodei.co/npm/isstream/)

The missing `Stream.isStream(obj)`: determine if an object is standard Node.js `Stream`. Works for Node-core `Stream` objects (for 0.8, 0.10, 0.11, and in theory, older and newer versions) and all versions of **[readable-stream](https://github.com/isaacs/readable-stream)**.

## Usage:

```js
var isStream = require('isstream')
var Stream = require('stream')

isStream(new Stream()) // true

isStream({}) // false

isStream(new Stream.Readable())    // true
isStream(new Stream.Writable())    // true
isStream(new Stream.Duplex())      // true
isStream(new Stream.Transform())   // true
isStream(new Stream.PassThrough()) // true
```

## But wait! There's more!

You can also test for `isReadable(obj)`, `isWritable(obj)` and `isDuplex(obj)` to test for implementations of Streams2 (and Streams3) base classes.

```js
var isReadable = require('isstream').isReadable
var isWritable = require('isstream').isWritable
var isDuplex = require('isstream').isDuplex
var Stream = require('stream')

isReadable(new Stream()) // false
isWritable(new Stream()) // false
isDuplex(new Stream())   // false

isReadable(new Stream.Readable())    // true
isReadable(new Stream.Writable())    // false
isReadable(new Stream.Duplex())      // true
isReadable(new Stream.Transform())   // true
isReadable(new Stream.PassThrough()) // true

isWritable(new Stream.Readable())    // false
isWritable(new Stream.Writable())    // true
isWritable(new Stream.Duplex())      // true
isWritable(new Stream.Transform())   // true
isWritable(new Stream.PassThrough()) // true

isDuplex(new Stream.Readable())    // false
isDuplex(new Stream.Writable())    // false
isDuplex(new Stream.Duplex())      // true
isDuplex(new Stream.Transform())   // true
isDuplex(new Stream.PassThrough()) // true
```

*Reminder: when implementing your own streams, please [use **readable-stream** rather than core streams](http://r.va.gg/2014/06/why-i-dont-use-nodes-core-stream-module.html).*


## License

**isStream** is Copyright (c) 2015 Rod Vagg [@rvagg](https://twitter.com/rvagg) and licenced under the MIT licence. All rights not explicitly granted in the MIT license are reserved. See the included LICENSE.md file for more details.
# Cypress

## What is this?

Cypress comes packaged as an `npm` module, which is all you need to get started.

After installing you'll be able to:

- Open Cypress from the CLI
- Run Cypress from the CLI
- `require` Cypress as a module

## Install

Requires Node version >= 4.0.0

```sh
npm install --save-dev cypress
```

## Documentation

Please [visit our documentation](https://on.cypress.io/cli) for a full list of commands and examples.
# lazy-ass

> Lazy assertions without performance penalty

[![NPM][lazy-ass-icon] ][lazy-ass-url]

[![Build status][lazy-ass-ci-image] ][lazy-ass-ci-url]
[![manpm](https://img.shields.io/badge/manpm-compatible-3399ff.svg)](https://github.com/bahmutov/manpm)
[![dependencies][lazy-ass-dependencies-image] ][lazy-ass-dependencies-url]
[![devdependencies][lazy-ass-devdependencies-image] ][lazy-ass-devdependencies-url]

[![semantic-release][semantic-image] ][semantic-url]
[![Coverage Status][lazy-ass-coverage-image]][lazy-ass-coverage-url]
[![Codacy][lazy-ass-codacy-image]][lazy-ass-codacy-url]
[![Code Climate][lazy-ass-code-climate-image]][lazy-ass-code-climate-url]

[Demo](http://glebbahmutov.com/lazy-ass/)

Is the current code breaking dependencies if released?
[![Dont-break][circle-ci-image] ][circle-ci-url] - checks using
[dont-break](https://github.com/bahmutov/dont-break)
[circle-ci-image]: https://circleci.com/gh/bahmutov/lazy-ass.svg?style=svg
[circle-ci-url]: https://circleci.com/gh/bahmutov/lazy-ass

## Example

Regular assertions evaluate all arguments and concatenate message
EVERY time, even if the condition is true.

```js
console.assert(typeof foo === 'object',
  'expected ' + JSON.stringify(foo, null, 2) + ' to be an object');
```

Lazy assertion function evaluates its arguments and forms
a message ONLY IF the condition is false

```js
lazyAss(typeof foo === 'object', 'expected', foo, 'to be an object');
```

Concatenates strings, stringifies objects, calls functions - only if
condition is false.

```js
function environment() {
  // returns string
}
var user = {} // an object
lazyAsync(condition, 'something went wrong for', user, 'in', environment);
// throws an error with message equivalent of
// 'something went wrong for ' + JSON.stringify(user) + ' in ' + environment()
```

## Why?

* Passing an object reference to a function is about
[2000-3000 times faster](http://jsperf.com/object-json-stringify)
than serializing an object and passing it as a string.
* Concatenating 2 strings before passing to a function is about
[30% slower](http://jsperf.com/string-concat-vs-pass-string-reference)
than passing 2 separate strings.

## Install

Node: `npm install lazy-ass --save` then `var la = require('lazy-ass');`.
You can attach the methods to the global object using
`require('lazy-ass').globalRegister();`.

Browser: `bower install lazy-ass --save`, include `index.js`,
attaches functions `lazyAss` and `la` to `window` object.

## Notes

You can pass as many arguments to *lazyAss* after the condition. The condition
will be evaluated every time (this is required for any assertion). The rest of arguments
will be concatenated according to rules

* string will be left unchanged.
* function will be called and its output will be concatenated.
* any array or object will be JSON stringified.

There will be single space between the individual parts.

## Lazy async assertions

Sometimes you do not want to throw an error synchronously, breaking the entire
execution stack. Instead you can throw an error asynchronously using `lazyAssync`,
which internally implements logic like this:

```js
if (!condition) {
  setTimeout(function () {
    throw new Error('Conditions is false!');
  }, 0);
}
```

This allows the execution to continue, while your global error handler (like
my favorite [Sentry](http://glebbahmutov.com/blog/know-unknown-unknowns-with-sentry/))
can still forward the error with all specified information to your server.

```js
lazyAss.async(false, 'foo');
console.log('after assync');
// output
after assync
Uncaught Error: foo
```

In this case, there is no meaningful error stack, so use good message
arguments - there is no performance penalty!

## Rethrowing errors

If the condition itself is an instance of Error, it is simply rethrown (synchronously or
asynchronously).

```js
lazyAss(new Error('foo'));
// Uncaught Error: foo
```

Useful to make sure errors in the promise chains are
[not silently ignored](https://glebbahmutov.com/blog/why-promises-need-to-be-done/).

For example, a rejected promise below this will be ignored.

```js
var p = new Promise(function (resolve, reject) {
  reject(new Error('foo'));
});
p.then(...);
```

We can catch it and rethrow it *synchronously*, but it will be ignored too (same way,
only one step further)

```js
var p = new Promise(function (resolve, reject) {
  reject(new Error('foo'));
});
p.then(..., lazyAss);
```

But we can actually trigger global error if we rethrow the error *asynchronously*

```js
var p = new Promise(function (resolve, reject) {
  reject(new Error('foo'));
});
p.then(..., lazyAssync);
// Uncaught Error: foo
```

## Predicate function as a condition

Typically, JavaScript evaluates the condition expression first, then calls *lazyAss*.
This means the function itself sees only the true / false result, and not the expression
itself. This makes makes the error messages cryptic

    lazyAss(2 + 2 === 5);
    // Error

We usually get around this by giving at least one additional message argument to
explain the condition tested

    lazyAss(2 + 2 === 5, 'addition')
    // Error: addition

*lazyAss* has a better solution: if you give a function that evaluates the condition
expression, if the function returns false, the error message will include the source
of the function, making the extra arguments unnecessary

    lazyAss(function () { return 2 + 2 === 5; });
    // Error: function () { return 2 + 2 === 5; }

The condition function has access to any variables in the scope, making it extremely
powerful

    var foo = 2, bar = 2;
    lazyAss(function () { return foo + bar === 5; });
    // Error: function () { return foo + bar === 5; }

In practical terms, I recommend using separate predicates function and
passing relevant values to the *lazyAss* function. Remember, there is no performance
penalty!

    var foo = 2, bar = 2;
    function isValidPair() {
      return foo + bar === 5;
    }
    lazyAss(isValidPair, 'foo', foo, 'bar', bar);
    // Error: function isValidPair() {
    //   return foo + bar === 5;
    // } foo 2 bar 2

## Testing

This library is fully tested under Node and inside browser environment (CasperJs).
I described how one can test asynchronous assertion throwing in your own projects
using Jasmine in [a blog post](http://glebbahmutov.com/blog/testing-async-lazy-assertion/).

## TypeScript

If you use this function from a TypeScript project, we provide ambient type
definition file. Because this is CommonJS library, use it like this

```ts
import la = require('lazy-ass')
// la should have type signature
```

### Small print

Author: Gleb Bahmutov &copy; 2014

* [@bahmutov](https://twitter.com/bahmutov)
* [glebbahmutov.com](http://glebbahmutov.com)
* [blog](http://glebbahmutov.com/blog)

License: MIT - do anything with the code, but don't blame me if it does not work.

Spread the word: tweet, star on github, etc.

Support: if you find any problems with this module, email / tweet /
[open issue](https://github.com/bahmutov/lazy-ass/issues) on Github

## MIT License

Copyright (c) 2014 Gleb Bahmutov

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

[lazy-ass-icon]: https://nodei.co/npm/lazy-ass.svg?downloads=true
[lazy-ass-url]: https://npmjs.org/package/lazy-ass
[lazy-ass-ci-image]: https://travis-ci.org/bahmutov/lazy-ass.svg?branch=master
[lazy-ass-ci-url]: https://travis-ci.org/bahmutov/lazy-ass
[lazy-ass-coverage-image]: https://coveralls.io/repos/bahmutov/lazy-ass/badge.svg
[lazy-ass-coverage-url]: https://coveralls.io/r/bahmutov/lazy-ass
[lazy-ass-code-climate-image]: https://codeclimate.com/github/bahmutov/lazy-ass/badges/gpa.svg
[lazy-ass-code-climate-url]: https://codeclimate.com/github/bahmutov/lazy-ass
[lazy-ass-codacy-image]: https://www.codacy.com/project/badge/b60a0810c9af4fe4b2ae685932dbbdb8
[lazy-ass-codacy-url]: https://www.codacy.com/public/bahmutov/lazy-ass.git
[lazy-ass-dependencies-image]: https://david-dm.org/bahmutov/lazy-ass.svg
[lazy-ass-dependencies-url]: https://david-dm.org/bahmutov/lazy-ass
[lazy-ass-devdependencies-image]: https://david-dm.org/bahmutov/lazy-ass/dev-status.svg
[lazy-ass-devdependencies-url]: https://david-dm.org/bahmutov/lazy-ass#info=devDependencies
[semantic-image]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg
[semantic-url]: https://github.com/semantic-release/semantic-release
# jsprim: utilities for primitive JavaScript types

This module provides miscellaneous facilities for working with strings,
numbers, dates, and objects and arrays of these basic types.


### deepCopy(obj)

Creates a deep copy of a primitive type, object, or array of primitive types.


### deepEqual(obj1, obj2)

Returns whether two objects are equal.


### isEmpty(obj)

Returns true if the given object has no properties and false otherwise.  This
is O(1) (unlike `Object.keys(obj).length === 0`, which is O(N)).

### hasKey(obj, key)

Returns true if the given object has an enumerable, non-inherited property
called `key`.  [For information on enumerability and ownership of properties, see
the MDN
documentation.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)

### forEachKey(obj, callback)

Like Array.forEach, but iterates enumerable, owned properties of an object
rather than elements of an array.  Equivalent to:

    for (var key in obj) {
            if (Object.prototype.hasOwnProperty.call(obj, key)) {
                    callback(key, obj[key]);
            }
    }


### flattenObject(obj, depth)

Flattens an object up to a given level of nesting, returning an array of arrays
of length "depth + 1", where the first "depth" elements correspond to flattened
columns and the last element contains the remaining object .  For example:

    flattenObject({
        'I': {
            'A': {
                'i': {
                    'datum1': [ 1, 2 ],
                    'datum2': [ 3, 4 ]
                },
                'ii': {
                    'datum1': [ 3, 4 ]
                }
            },
            'B': {
                'i': {
                    'datum1': [ 5, 6 ]
                },
                'ii': {
                    'datum1': [ 7, 8 ],
                    'datum2': [ 3, 4 ],
                },
                'iii': {
                }
            }
        },
        'II': {
            'A': {
                'i': {
                    'datum1': [ 1, 2 ],
                    'datum2': [ 3, 4 ]
                }
            }
        }
    }, 3)

becomes:

    [
        [ 'I',  'A', 'i',   { 'datum1': [ 1, 2 ], 'datum2': [ 3, 4 ] } ],
        [ 'I',  'A', 'ii',  { 'datum1': [ 3, 4 ] } ],
        [ 'I',  'B', 'i',   { 'datum1': [ 5, 6 ] } ],
        [ 'I',  'B', 'ii',  { 'datum1': [ 7, 8 ], 'datum2': [ 3, 4 ] } ],
        [ 'I',  'B', 'iii', {} ],
        [ 'II', 'A', 'i',   { 'datum1': [ 1, 2 ], 'datum2': [ 3, 4 ] } ]
    ]

This function is strict: "depth" must be a non-negative integer and "obj" must
be a non-null object with at least "depth" levels of nesting under all keys.


### flattenIter(obj, depth, func)

This is similar to `flattenObject` except that instead of returning an array,
this function invokes `func(entry)` for each `entry` in the array that
`flattenObject` would return.  `flattenIter(obj, depth, func)` is logically
equivalent to `flattenObject(obj, depth).forEach(func)`.  Importantly, this
version never constructs the full array.  Its memory usage is O(depth) rather
than O(n) (where `n` is the number of flattened elements).

There's another difference between `flattenObject` and `flattenIter` that's
related to the special case where `depth === 0`.  In this case, `flattenObject`
omits the array wrapping `obj` (which is regrettable).


### pluck(obj, key)

Fetch nested property "key" from object "obj", traversing objects as needed.
For example, `pluck(obj, "foo.bar.baz")` is roughly equivalent to
`obj.foo.bar.baz`, except that:

1. If traversal fails, the resulting value is undefined, and no error is
   thrown.  For example, `pluck({}, "foo.bar")` is just undefined.
2. If "obj" has property "key" directly (without traversing), the
   corresponding property is returned.  For example,
   `pluck({ 'foo.bar': 1 }, 'foo.bar')` is 1, not undefined.  This is also
   true recursively, so `pluck({ 'a': { 'foo.bar': 1 } }, 'a.foo.bar')` is
   also 1, not undefined.


### randElt(array)

Returns an element from "array" selected uniformly at random.  If "array" is
empty, throws an Error.


### startsWith(str, prefix)

Returns true if the given string starts with the given prefix and false
otherwise.


### endsWith(str, suffix)

Returns true if the given string ends with the given suffix and false
otherwise.


### parseInteger(str, options)

Parses the contents of `str` (a string) as an integer. On success, the integer
value is returned (as a number). On failure, an error is **returned** describing
why parsing failed.

By default, leading and trailing whitespace characters are not allowed, nor are
trailing characters that are not part of the numeric representation. This
behaviour can be toggled by using the options below. The empty string (`''`) is
not considered valid input. If the return value cannot be precisely represented
as a number (i.e., is smaller than `Number.MIN_SAFE_INTEGER` or larger than
`Number.MAX_SAFE_INTEGER`), an error is returned. Additionally, the string
`'-0'` will be parsed as the integer `0`, instead of as the IEEE floating point
value `-0`.

This function accepts both upper and lowercase characters for digits, similar to
`parseInt()`, `Number()`, and [strtol(3C)](https://illumos.org/man/3C/strtol).

The following may be specified in `options`:

Option             | Type    | Default | Meaning
------------------ | ------- | ------- | ---------------------------
base               | number  | 10      | numeric base (radix) to use, in the range 2 to 36
allowSign          | boolean | true    | whether to interpret any leading `+` (positive) and `-` (negative) characters
allowImprecise     | boolean | false   | whether to accept values that may have lost precision (past `MAX_SAFE_INTEGER` or below `MIN_SAFE_INTEGER`)
allowPrefix        | boolean | false   | whether to interpret the prefixes `0b` (base 2), `0o` (base 8), `0t` (base 10), or `0x` (base 16)
allowTrailing      | boolean | false   | whether to ignore trailing characters
trimWhitespace     | boolean | false   | whether to trim any leading or trailing whitespace/line terminators
leadingZeroIsOctal | boolean | false   | whether a leading zero indicates octal

Note that if `base` is unspecified, and `allowPrefix` or `leadingZeroIsOctal`
are, then the leading characters can change the default base from 10. If `base`
is explicitly specified and `allowPrefix` is true, then the prefix will only be
accepted if it matches the specified base. `base` and `leadingZeroIsOctal`
cannot be used together.

**Context:** It's tricky to parse integers with JavaScript's built-in facilities
for several reasons:

- `parseInt()` and `Number()` by default allow the base to be specified in the
  input string by a prefix (e.g., `0x` for hex).
- `parseInt()` allows trailing nonnumeric characters.
- `Number(str)` returns 0 when `str` is the empty string (`''`).
- Both functions return incorrect values when the input string represents a
  valid integer outside the range of integers that can be represented precisely.
  Specifically, `parseInt('9007199254740993')` returns 9007199254740992.
- Both functions always accept `-` and `+` signs before the digit.
- Some older JavaScript engines always interpret a leading 0 as indicating
  octal, which can be surprising when parsing input from users who expect a
  leading zero to be insignificant.

While each of these may be desirable in some contexts, there are also times when
none of them are wanted. `parseInteger()` grants greater control over what
input's permissible.

### iso8601(date)

Converts a Date object to an ISO8601 date string of the form
"YYYY-MM-DDTHH:MM:SS.sssZ".  This format is not customizable.


### parseDateTime(str)

Parses a date expressed as a string, as either a number of milliseconds since
the epoch or any string format that Date accepts, giving preference to the
former where these two sets overlap (e.g., strings containing small numbers).


### hrtimeDiff(timeA, timeB)

Given two hrtime readings (as from Node's `process.hrtime()`), where timeA is
later than timeB, compute the difference and return that as an hrtime.  It is
illegal to invoke this for a pair of times where timeB is newer than timeA.

### hrtimeAdd(timeA, timeB)

Add two hrtime intervals (as from Node's `process.hrtime()`), returning a new
hrtime interval array.  This function does not modify either input argument.


### hrtimeAccum(timeA, timeB)

Add two hrtime intervals (as from Node's `process.hrtime()`), storing the
result in `timeA`.  This function overwrites (and returns) the first argument
passed in.


### hrtimeNanosec(timeA), hrtimeMicrosec(timeA), hrtimeMillisec(timeA)

This suite of functions converts a hrtime interval (as from Node's
`process.hrtime()`) into a scalar number of nanoseconds, microseconds or
milliseconds.  Results are truncated, as with `Math.floor()`.


### validateJsonObject(schema, object)

Uses JSON validation (via JSV) to validate the given object against the given
schema.  On success, returns null.  On failure, *returns* (does not throw) a
useful Error object.


### extraProperties(object, allowed)

Check an object for unexpected properties.  Accepts the object to check, and an
array of allowed property name strings.  If extra properties are detected, an
array of extra property names is returned.  If no properties other than those
in the allowed list are present on the object, the returned array will be of
zero length.

### mergeObjects(provided, overrides, defaults)

Merge properties from objects "provided", "overrides", and "defaults".  The
intended use case is for functions that accept named arguments in an "args"
object, but want to provide some default values and override other values.  In
that case, "provided" is what the caller specified, "overrides" are what the
function wants to override, and "defaults" contains default values.

The function starts with the values in "defaults", overrides them with the
values in "provided", and then overrides those with the values in "overrides".
For convenience, any of these objects may be falsey, in which case they will be
ignored.  The input objects are never modified, but properties in the returned
object are not deep-copied.

For example:

    mergeObjects(undefined, { 'objectMode': true }, { 'highWaterMark': 0 })

returns:

    { 'objectMode': true, 'highWaterMark': 0 }

For another example:

    mergeObjects(
        { 'highWaterMark': 16, 'objectMode': 7 }, /* from caller */
        { 'objectMode': true },                   /* overrides */
        { 'highWaterMark': 0 });                  /* default */

returns:

    { 'objectMode': true, 'highWaterMark': 16 }


# Contributing

See separate [contribution guidelines](CONTRIBUTING.md).
# signal-exit

[![Build Status](https://travis-ci.org/tapjs/signal-exit.png)](https://travis-ci.org/tapjs/signal-exit)
[![Coverage](https://coveralls.io/repos/tapjs/signal-exit/badge.svg?branch=master)](https://coveralls.io/r/tapjs/signal-exit?branch=master)
[![NPM version](https://img.shields.io/npm/v/signal-exit.svg)](https://www.npmjs.com/package/signal-exit)
[![Windows Tests](https://img.shields.io/appveyor/ci/bcoe/signal-exit/master.svg?label=Windows%20Tests)](https://ci.appveyor.com/project/bcoe/signal-exit)
[![Standard Version](https://img.shields.io/badge/release-standard%20version-brightgreen.svg)](https://github.com/conventional-changelog/standard-version)

When you want to fire an event no matter how a process exits:

* reaching the end of execution.
* explicitly having `process.exit(code)` called.
* having `process.kill(pid, sig)` called.
* receiving a fatal signal from outside the process

Use `signal-exit`.

```js
var onExit = require('signal-exit')

onExit(function (code, signal) {
  console.log('process exited!')
})
```

## API

`var remove = onExit(function (code, signal) {}, options)`

The return value of the function is a function that will remove the
handler.

Note that the function *only* fires for signals if the signal would
cause the proces to exit.  That is, there are no other listeners, and
it is a fatal signal.

## Options

* `alwaysLast`: Run this handler after any other signal or exit
  handlers.  This causes `process.emit` to be monkeypatched.
concat-map
==========

Concatenative mapdashery.

[![browser support](http://ci.testling.com/substack/node-concat-map.png)](http://ci.testling.com/substack/node-concat-map)

[![build status](https://secure.travis-ci.org/substack/node-concat-map.png)](http://travis-ci.org/substack/node-concat-map)

example
=======

``` js
var concatMap = require('concat-map');
var xs = [ 1, 2, 3, 4, 5, 6 ];
var ys = concatMap(xs, function (x) {
    return x % 2 ? [ x - 0.1, x, x + 0.1 ] : [];
});
console.dir(ys);
```

***

```
[ 0.9, 1, 1.1, 2.9, 3, 3.1, 4.9, 5, 5.1 ]
```

methods
=======

``` js
var concatMap = require('concat-map')
```

concatMap(xs, fn)
-----------------

Return an array of concatenated elements by calling `fn(x, i)` for each element
`x` and each index `i` in the array `xs`.

When `fn(x, i)` returns an array, its result will be concatenated with the
result array. If `fn(x, i)` returns anything else, that value will be pushed
onto the end of the result array.

install
=======

With [npm](http://npmjs.org) do:

```
npm install concat-map
```

license
=======

MIT

notes
=====

This module was written while sitting high above the ground in a tree.
sshpk
=========

Parse, convert, fingerprint and use SSH keys (both public and private) in pure
node -- no `ssh-keygen` or other external dependencies.

Supports RSA, DSA, ECDSA (nistp-\*) and ED25519 key types, in PEM (PKCS#1, 
PKCS#8) and OpenSSH formats.

This library has been extracted from
[`node-http-signature`](https://github.com/joyent/node-http-signature)
(work by [Mark Cavage](https://github.com/mcavage) and
[Dave Eddy](https://github.com/bahamas10)) and
[`node-ssh-fingerprint`](https://github.com/bahamas10/node-ssh-fingerprint)
(work by Dave Eddy), with additions (including ECDSA support) by
[Alex Wilson](https://github.com/arekinath).

Install
-------

```
npm install sshpk
```

Examples
--------

```js
var sshpk = require('sshpk');

var fs = require('fs');

/* Read in an OpenSSH-format public key */
var keyPub = fs.readFileSync('id_rsa.pub');
var key = sshpk.parseKey(keyPub, 'ssh');

/* Get metadata about the key */
console.log('type => %s', key.type);
console.log('size => %d bits', key.size);
console.log('comment => %s', key.comment);

/* Compute key fingerprints, in new OpenSSH (>6.7) format, and old MD5 */
console.log('fingerprint => %s', key.fingerprint().toString());
console.log('old-style fingerprint => %s', key.fingerprint('md5').toString());
```

Example output:

```
type => rsa
size => 2048 bits
comment => foo@foo.com
fingerprint => SHA256:PYC9kPVC6J873CSIbfp0LwYeczP/W4ffObNCuDJ1u5w
old-style fingerprint => a0:c8:ad:6c:32:9a:32:fa:59:cc:a9:8c:0a:0d:6e:bd
```

More examples: converting between formats:

```js
/* Read in a PEM public key */
var keyPem = fs.readFileSync('id_rsa.pem');
var key = sshpk.parseKey(keyPem, 'pem');

/* Convert to PEM PKCS#8 public key format */
var pemBuf = key.toBuffer('pkcs8');

/* Convert to SSH public key format (and return as a string) */
var sshKey = key.toString('ssh');
```

Signing and verifying:

```js
/* Read in an OpenSSH/PEM *private* key */
var keyPriv = fs.readFileSync('id_ecdsa');
var key = sshpk.parsePrivateKey(keyPriv, 'pem');

var data = 'some data';

/* Sign some data with the key */
var s = key.createSign('sha1');
s.update(data);
var signature = s.sign();

/* Now load the public key (could also use just key.toPublic()) */
var keyPub = fs.readFileSync('id_ecdsa.pub');
key = sshpk.parseKey(keyPub, 'ssh');

/* Make a crypto.Verifier with this key */
var v = key.createVerify('sha1');
v.update(data);
var valid = v.verify(signature);
/* => true! */
```

Matching fingerprints with keys:

```js
var fp = sshpk.parseFingerprint('SHA256:PYC9kPVC6J873CSIbfp0LwYeczP/W4ffObNCuDJ1u5w');

var keys = [sshpk.parseKey(...), sshpk.parseKey(...), ...];

keys.forEach(function (key) {
	if (fp.matches(key))
		console.log('found it!');
});
```

Usage
-----

## Public keys

### `parseKey(data[, format = 'auto'[, options]])`

Parses a key from a given data format and returns a new `Key` object.

Parameters

- `data` -- Either a Buffer or String, containing the key
- `format` -- String name of format to use, valid options are:
  - `auto`: choose automatically from all below
  - `pem`: supports both PKCS#1 and PKCS#8
  - `ssh`: standard OpenSSH format,
  - `pkcs1`, `pkcs8`: variants of `pem`
  - `rfc4253`: raw OpenSSH wire format
  - `openssh`: new post-OpenSSH 6.5 internal format, produced by 
               `ssh-keygen -o`
- `options` -- Optional Object, extra options, with keys:
  - `filename` -- Optional String, name for the key being parsed 
                  (eg. the filename that was opened). Used to generate
                  Error messages
  - `passphrase` -- Optional String, encryption passphrase used to decrypt an
                    encrypted PEM file

### `Key.isKey(obj)`

Returns `true` if the given object is a valid `Key` object created by a version
of `sshpk` compatible with this one.

Parameters

- `obj` -- Object to identify

### `Key#type`

String, the type of key. Valid options are `rsa`, `dsa`, `ecdsa`.

### `Key#size`

Integer, "size" of the key in bits. For RSA/DSA this is the size of the modulus;
for ECDSA this is the bit size of the curve in use.

### `Key#comment`

Optional string, a key comment used by some formats (eg the `ssh` format).

### `Key#curve`

Only present if `this.type === 'ecdsa'`, string containing the name of the
named curve used with this key. Possible values include `nistp256`, `nistp384`
and `nistp521`.

### `Key#toBuffer([format = 'ssh'])`

Convert the key into a given data format and return the serialized key as
a Buffer.

Parameters

- `format` -- String name of format to use, for valid options see `parseKey()`

### `Key#toString([format = 'ssh])`

Same as `this.toBuffer(format).toString()`.

### `Key#fingerprint([algorithm = 'sha256'])`

Creates a new `Fingerprint` object representing this Key's fingerprint.

Parameters

- `algorithm` -- String name of hash algorithm to use, valid options are `md5`,
                 `sha1`, `sha256`, `sha384`, `sha512`

### `Key#createVerify([hashAlgorithm])`

Creates a `crypto.Verifier` specialized to use this Key (and the correct public
key algorithm to match it). The returned Verifier has the same API as a regular
one, except that the `verify()` function takes only the target signature as an
argument.

Parameters

- `hashAlgorithm` -- optional String name of hash algorithm to use, any
                     supported by OpenSSL are valid, usually including
                     `sha1`, `sha256`.

`v.verify(signature[, format])` Parameters

- `signature` -- either a Signature object, or a Buffer or String
- `format` -- optional String, name of format to interpret given String with.
              Not valid if `signature` is a Signature or Buffer.

### `Key#createDiffieHellman()`
### `Key#createDH()`

Creates a Diffie-Hellman key exchange object initialized with this key and all
necessary parameters. This has the same API as a `crypto.DiffieHellman`
instance, except that functions take `Key` and `PrivateKey` objects as
arguments, and return them where indicated for.

This is only valid for keys belonging to a cryptosystem that supports DHE
or a close analogue (i.e. `dsa`, `ecdsa` and `curve25519` keys). An attempt
to call this function on other keys will yield an `Error`.

## Private keys

### `parsePrivateKey(data[, format = 'auto'[, options]])`

Parses a private key from a given data format and returns a new
`PrivateKey` object.

Parameters

- `data` -- Either a Buffer or String, containing the key
- `format` -- String name of format to use, valid options are:
  - `auto`: choose automatically from all below
  - `pem`: supports both PKCS#1 and PKCS#8
  - `ssh`, `openssh`: new post-OpenSSH 6.5 internal format, produced by
                      `ssh-keygen -o`
  - `pkcs1`, `pkcs8`: variants of `pem`
  - `rfc4253`: raw OpenSSH wire format
- `options` -- Optional Object, extra options, with keys:
  - `filename` -- Optional String, name for the key being parsed
                  (eg. the filename that was opened). Used to generate
                  Error messages
  - `passphrase` -- Optional String, encryption passphrase used to decrypt an
                    encrypted PEM file

### `generatePrivateKey(type[, options])`

Generates a new private key of a certain key type, from random data.

Parameters

- `type` -- String, type of key to generate. Currently supported are `'ecdsa'`
            and `'ed25519'`
- `options` -- optional Object, with keys:
  - `curve` -- optional String, for `'ecdsa'` keys, specifies the curve to use.
               If ECDSA is specified and this option is not given, defaults to
               using `'nistp256'`.

### `PrivateKey.isPrivateKey(obj)`

Returns `true` if the given object is a valid `PrivateKey` object created by a
version of `sshpk` compatible with this one.

Parameters

- `obj` -- Object to identify

### `PrivateKey#type`

String, the type of key. Valid options are `rsa`, `dsa`, `ecdsa`.

### `PrivateKey#size`

Integer, "size" of the key in bits. For RSA/DSA this is the size of the modulus;
for ECDSA this is the bit size of the curve in use.

### `PrivateKey#curve`

Only present if `this.type === 'ecdsa'`, string containing the name of the
named curve used with this key. Possible values include `nistp256`, `nistp384`
and `nistp521`.

### `PrivateKey#toBuffer([format = 'pkcs1'])`

Convert the key into a given data format and return the serialized key as
a Buffer.

Parameters

- `format` -- String name of format to use, valid options are listed under 
              `parsePrivateKey`. Note that ED25519 keys default to `openssh`
              format instead (as they have no `pkcs1` representation).

### `PrivateKey#toString([format = 'pkcs1'])`

Same as `this.toBuffer(format).toString()`.

### `PrivateKey#toPublic()`

Extract just the public part of this private key, and return it as a `Key`
object.

### `PrivateKey#fingerprint([algorithm = 'sha256'])`

Same as `this.toPublic().fingerprint()`.

### `PrivateKey#createVerify([hashAlgorithm])`

Same as `this.toPublic().createVerify()`.

### `PrivateKey#createSign([hashAlgorithm])`

Creates a `crypto.Sign` specialized to use this PrivateKey (and the correct
key algorithm to match it). The returned Signer has the same API as a regular
one, except that the `sign()` function takes no arguments, and returns a
`Signature` object.

Parameters

- `hashAlgorithm` -- optional String name of hash algorithm to use, any
                     supported by OpenSSL are valid, usually including
                     `sha1`, `sha256`.

`v.sign()` Parameters

- none

### `PrivateKey#derive(newType)`

Derives a related key of type `newType` from this key. Currently this is
only supported to change between `ed25519` and `curve25519` keys which are
stored with the same private key (but usually distinct public keys in order
to avoid degenerate keys that lead to a weak Diffie-Hellman exchange).

Parameters

- `newType` -- String, type of key to derive, either `ed25519` or `curve25519`

## Fingerprints

### `parseFingerprint(fingerprint[, algorithms])`

Pre-parses a fingerprint, creating a `Fingerprint` object that can be used to
quickly locate a key by using the `Fingerprint#matches` function.

Parameters

- `fingerprint` -- String, the fingerprint value, in any supported format
- `algorithms` -- Optional list of strings, names of hash algorithms to limit
                  support to. If `fingerprint` uses a hash algorithm not on
                  this list, throws `InvalidAlgorithmError`.

### `Fingerprint.isFingerprint(obj)`

Returns `true` if the given object is a valid `Fingerprint` object created by a
version of `sshpk` compatible with this one.

Parameters

- `obj` -- Object to identify

### `Fingerprint#toString([format])`

Returns a fingerprint as a string, in the given format.

Parameters

- `format` -- Optional String, format to use, valid options are `hex` and
              `base64`. If this `Fingerprint` uses the `md5` algorithm, the
              default format is `hex`. Otherwise, the default is `base64`.

### `Fingerprint#matches(key)`

Verifies whether or not this `Fingerprint` matches a given `Key`. This function
uses double-hashing to avoid leaking timing information. Returns a boolean.

Parameters

- `key` -- a `Key` object, the key to match this fingerprint against

## Signatures

### `parseSignature(signature, algorithm, format)`

Parses a signature in a given format, creating a `Signature` object. Useful
for converting between the SSH and ASN.1 (PKCS/OpenSSL) signature formats, and
also returned as output from `PrivateKey#createSign().sign()`.

A Signature object can also be passed to a verifier produced by
`Key#createVerify()` and it will automatically be converted internally into the
correct format for verification.

Parameters

- `signature` -- a Buffer (binary) or String (base64), data of the actual
                 signature in the given format
- `algorithm` -- a String, name of the algorithm to be used, possible values
                 are `rsa`, `dsa`, `ecdsa`
- `format` -- a String, either `asn1` or `ssh`

### `Signature.isSignature(obj)`

Returns `true` if the given object is a valid `Signature` object created by a
version of `sshpk` compatible with this one.

Parameters

- `obj` -- Object to identify

### `Signature#toBuffer([format = 'asn1'])`

Converts a Signature to the given format and returns it as a Buffer.

Parameters

- `format` -- a String, either `asn1` or `ssh`

### `Signature#toString([format = 'asn1'])`

Same as `this.toBuffer(format).toString('base64')`.

## Certificates

`sshpk` includes basic support for parsing certificates in X.509 (PEM) format
and the OpenSSH certificate format. This feature is intended to be used mainly
to access basic metadata about certificates, extract public keys from them, and
also to generate simple self-signed certificates from an existing key.

Notably, there is no implementation of CA chain-of-trust verification, and only
very minimal support for key usage restrictions. Please do the security world
a favour, and DO NOT use this code for certificate verification in the
traditional X.509 CA chain style.

### `parseCertificate(data, format)`

Parameters

 - `data` -- a Buffer or String
 - `format` -- a String, format to use, one of `'openssh'`, `'pem'` (X.509 in a
               PEM wrapper), or `'x509'` (raw DER encoded)

### `createSelfSignedCertificate(subject, privateKey[, options])`

Parameters

 - `subject` -- an Identity, the subject of the certificate
 - `privateKey` -- a PrivateKey, the key of the subject: will be used both to be
                   placed in the certificate and also to sign it (since this is
                   a self-signed certificate)
 - `options` -- optional Object, with keys:
   - `lifetime` -- optional Number, lifetime of the certificate from now in
                   seconds
   - `validFrom`, `validUntil` -- optional Dates, beginning and end of
                                  certificate validity period. If given
                                  `lifetime` will be ignored
   - `serial` -- optional Buffer, the serial number of the certificate
   - `purposes` -- optional Array of String, X.509 key usage restrictions

### `createCertificate(subject, key, issuer, issuerKey[, options])`

Parameters

 - `subject` -- an Identity, the subject of the certificate
 - `key` -- a Key, the public key of the subject
 - `issuer` -- an Identity, the issuer of the certificate who will sign it
 - `issuerKey` -- a PrivateKey, the issuer's private key for signing
 - `options` -- optional Object, with keys:
   - `lifetime` -- optional Number, lifetime of the certificate from now in
                   seconds
   - `validFrom`, `validUntil` -- optional Dates, beginning and end of
                                  certificate validity period. If given
                                  `lifetime` will be ignored
   - `serial` -- optional Buffer, the serial number of the certificate
   - `purposes` -- optional Array of String, X.509 key usage restrictions

### `Certificate#subjects`

Array of `Identity` instances describing the subject of this certificate.

### `Certificate#issuer`

The `Identity` of the Certificate's issuer (signer).

### `Certificate#subjectKey`

The public key of the subject of the certificate, as a `Key` instance.

### `Certificate#issuerKey`

The public key of the signing issuer of this certificate, as a `Key` instance.
May be `undefined` if the issuer's key is unknown (e.g. on an X509 certificate).

### `Certificate#serial`

The serial number of the certificate. As this is normally a 64-bit or wider
integer, it is returned as a Buffer.

### `Certificate#purposes`

Array of Strings indicating the X.509 key usage purposes that this certificate
is valid for. The possible strings at the moment are:

 * `'signature'` -- key can be used for digital signatures
 * `'identity'` -- key can be used to attest about the identity of the signer
                   (X.509 calls this `nonRepudiation`)
 * `'codeSigning'` -- key can be used to sign executable code
 * `'keyEncryption'` -- key can be used to encrypt other keys
 * `'encryption'` -- key can be used to encrypt data (only applies for RSA)
 * `'keyAgreement'` -- key can be used for key exchange protocols such as
                       Diffie-Hellman
 * `'ca'` -- key can be used to sign other certificates (is a Certificate
             Authority)
 * `'crl'` -- key can be used to sign Certificate Revocation Lists (CRLs)

### `Certificate#isExpired([when])`

Tests whether the Certificate is currently expired (i.e. the `validFrom` and
`validUntil` dates specify a range of time that does not include the current
time).

Parameters

 - `when` -- optional Date, if specified, tests whether the Certificate was or
             will be expired at the specified time instead of now

Returns a Boolean.

### `Certificate#isSignedByKey(key)`

Tests whether the Certificate was validly signed by the given (public) Key.

Parameters

 - `key` -- a Key instance

Returns a Boolean.

### `Certificate#isSignedBy(certificate)`

Tests whether this Certificate was validly signed by the subject of the given
certificate. Also tests that the issuer Identity of this Certificate and the
subject Identity of the other Certificate are equivalent.

Parameters

 - `certificate` -- another Certificate instance

Returns a Boolean.

### `Certificate#fingerprint([hashAlgo])`

Returns the X509-style fingerprint of the entire certificate (as a Fingerprint
instance). This matches what a web-browser or similar would display as the
certificate fingerprint and should not be confused with the fingerprint of the
subject's public key.

Parameters

 - `hashAlgo` -- an optional String, any hash function name

### `Certificate#toBuffer([format])`

Serializes the Certificate to a Buffer and returns it.

Parameters

 - `format` -- an optional String, output format, one of `'openssh'`, `'pem'` or
               `'x509'`. Defaults to `'x509'`.

Returns a Buffer.

### `Certificate#toString([format])`

 - `format` -- an optional String, output format, one of `'openssh'`, `'pem'` or
               `'x509'`. Defaults to `'pem'`.

Returns a String.

## Certificate identities

### `identityForHost(hostname)`

Constructs a host-type Identity for a given hostname.

Parameters

 - `hostname` -- the fully qualified DNS name of the host

Returns an Identity instance.

### `identityForUser(uid)`

Constructs a user-type Identity for a given UID.

Parameters

 - `uid` -- a String, user identifier (login name)

Returns an Identity instance.

### `identityForEmail(email)`

Constructs an email-type Identity for a given email address.

Parameters

 - `email` -- a String, email address

Returns an Identity instance.

### `identityFromDN(dn)`

Parses an LDAP-style DN string (e.g. `'CN=foo, C=US'`) and turns it into an
Identity instance.

Parameters

 - `dn` -- a String

Returns an Identity instance.

### `Identity#toString()`

Returns the identity as an LDAP-style DN string.
e.g. `'CN=foo, O=bar corp, C=us'`

### `Identity#type`

The type of identity. One of `'host'`, `'user'`, `'email'` or `'unknown'`

### `Identity#hostname`
### `Identity#uid`
### `Identity#email`

Set when `type` is `'host'`, `'user'`, or `'email'`, respectively. Strings.

### `Identity#cn`

The value of the first `CN=` in the DN, if any.

Errors
------

### `InvalidAlgorithmError`

The specified algorithm is not valid, either because it is not supported, or
because it was not included on a list of allowed algorithms.

Thrown by `Fingerprint.parse`, `Key#fingerprint`.

Properties

- `algorithm` -- the algorithm that could not be validated

### `FingerprintFormatError`

The fingerprint string given could not be parsed as a supported fingerprint
format, or the specified fingerprint format is invalid.

Thrown by `Fingerprint.parse`, `Fingerprint#toString`.

Properties

- `fingerprint` -- if caused by a fingerprint, the string value given
- `format` -- if caused by an invalid format specification, the string value given

### `KeyParseError`

The key data given could not be parsed as a valid key.

Properties

- `keyName` -- `filename` that was given to `parseKey`
- `format` -- the `format` that was trying to parse the key (see `parseKey`)
- `innerErr` -- the inner Error thrown by the format parser

### `KeyEncryptedError`

The key is encrypted with a symmetric key (ie, it is password protected). The
parsing operation would succeed if it was given the `passphrase` option.

Properties

- `keyName` -- `filename` that was given to `parseKey`
- `format` -- the `format` that was trying to parse the key (currently can only
              be `"pem"`)

### `CertificateParseError`

The certificate data given could not be parsed as a valid certificate.

Properties

- `certName` -- `filename` that was given to `parseCertificate`
- `format` -- the `format` that was trying to parse the key
              (see `parseCertificate`)
- `innerErr` -- the inner Error thrown by the format parser

Friends of sshpk
----------------

 * [`sshpk-agent`](https://github.com/arekinath/node-sshpk-agent) is a library
   for speaking the `ssh-agent` protocol from node.js, which uses `sshpk`
# core-js

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/zloirock/core-js?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![version](https://img.shields.io/npm/v/core-js.svg)](https://www.npmjs.com/package/core-js) [![npm downloads](https://img.shields.io/npm/dm/core-js.svg)](http://npm-stat.com/charts.html?package=core-js&author=&from=2014-11-18) [![Build Status](https://travis-ci.org/zloirock/core-js.svg)](https://travis-ci.org/zloirock/core-js) [![devDependency status](https://david-dm.org/zloirock/core-js/dev-status.svg)](https://david-dm.org/zloirock/core-js?type=dev)
#### As advertising: the author is looking for a good job :)

Modular standard library for JavaScript. Includes polyfills for [ECMAScript 5](#ecmascript-5), [ECMAScript 6](#ecmascript-6): [promises](#ecmascript-6-promise), [symbols](#ecmascript-6-symbol), [collections](#ecmascript-6-collections), iterators, [typed arrays](#ecmascript-6-typed-arrays), [ECMAScript 7+ proposals](#ecmascript-7-proposals), [setImmediate](#setimmediate), etc. Some additional features such as [dictionaries](#dict) or [extended partial application](#partial-application). You can require only needed features or use it without global namespace pollution.

[*Example*](http://goo.gl/a2xexl):
```js
Array.from(new Set([1, 2, 3, 2, 1]));          // => [1, 2, 3]
'*'.repeat(10);                                // => '**********'
Promise.resolve(32).then(x => console.log(x)); // => 32
setImmediate(x => console.log(x), 42);         // => 42
```

[*Without global namespace pollution*](http://goo.gl/paOHb0):
```js
var core = require('core-js/library'); // With a modular system, otherwise use global `core`
core.Array.from(new core.Set([1, 2, 3, 2, 1]));     // => [1, 2, 3]
core.String.repeat('*', 10);                        // => '**********'
core.Promise.resolve(32).then(x => console.log(x)); // => 32
core.setImmediate(x => console.log(x), 42);         // => 42
```

### Index
- [Usage](#usage)
  - [Basic](#basic)
  - [CommonJS](#commonjs)
  - [Custom build](#custom-build-from-the-command-line)
- [Supported engines](#supported-engines)
- [Features](#features)
  - [ECMAScript 5](#ecmascript-5)
  - [ECMAScript 6](#ecmascript-6)
    - [ECMAScript 6: Object](#ecmascript-6-object)
    - [ECMAScript 6: Function](#ecmascript-6-function)
    - [ECMAScript 6: Array](#ecmascript-6-array)
    - [ECMAScript 6: String](#ecmascript-6-string)
    - [ECMAScript 6: RegExp](#ecmascript-6-regexp)
    - [ECMAScript 6: Number](#ecmascript-6-number)
    - [ECMAScript 6: Math](#ecmascript-6-math)
    - [ECMAScript 6: Date](#ecmascript-6-date)
    - [ECMAScript 6: Promise](#ecmascript-6-promise)
    - [ECMAScript 6: Symbol](#ecmascript-6-symbol)
    - [ECMAScript 6: Collections](#ecmascript-6-collections)
    - [ECMAScript 6: Typed Arrays](#ecmascript-6-typed-arrays)
    - [ECMAScript 6: Reflect](#ecmascript-6-reflect)
  - [ECMAScript 7+ proposals](#ecmascript-7-proposals)
    - [stage 4 proposals](#stage-4-proposals)
    - [stage 3 proposals](#stage-3-proposals)
    - [stage 2 proposals](#stage-2-proposals)
    - [stage 1 proposals](#stage-1-proposals)
    - [stage 0 proposals](#stage-0-proposals)
    - [pre-stage 0 proposals](#pre-stage-0-proposals)
  - [Web standards](#web-standards)
    - [setTimeout / setInterval](#settimeout--setinterval)
    - [setImmediate](#setimmediate)
    - [iterable DOM collections](#iterable-dom-collections)
  - [Non-standard](#non-standard)
    - [Object](#object)
    - [Dict](#dict)
    - [partial application](#partial-application)
    - [Number Iterator](#number-iterator)
    - [escaping strings](#escaping-strings)
    - [delay](#delay)
    - [helpers for iterators](#helpers-for-iterators)
- [Missing polyfills](#missing-polyfills)
- [Changelog](./CHANGELOG.md)

## Usage
### Basic
```
npm i core-js
bower install core.js
```

```js
// Default
require('core-js');
// Without global namespace pollution
var core = require('core-js/library');
// Shim only
require('core-js/shim');
```
If you need complete build for browser, use builds from `core-js/client` path:  

* [default](https://raw.githack.com/zloirock/core-js/v2.5.7/client/core.min.js): Includes all features, standard and non-standard.
* [as a library](https://raw.githack.com/zloirock/core-js/v2.5.7/client/library.min.js): Like "default", but does not pollute the global namespace (see [2nd example at the top](#core-js)).
* [shim only](https://raw.githack.com/zloirock/core-js/v2.5.7/client/shim.min.js): Only includes the standard methods.

Warning: if you use `core-js` with the extension of native objects, require all needed `core-js` modules at the beginning of entry point of your application, otherwise, conflicts may occur.

### CommonJS
You can require only needed modules.

```js
require('core-js/fn/set');
require('core-js/fn/array/from');
require('core-js/fn/array/find-index');
Array.from(new Set([1, 2, 3, 2, 1])); // => [1, 2, 3]
[1, 2, NaN, 3, 4].findIndex(isNaN);   // => 2

// or, w/o global namespace pollution:

var Set       = require('core-js/library/fn/set');
var from      = require('core-js/library/fn/array/from');
var findIndex = require('core-js/library/fn/array/find-index');
from(new Set([1, 2, 3, 2, 1]));      // => [1, 2, 3]
findIndex([1, 2, NaN, 3, 4], isNaN); // => 2
```
Available entry points for methods / constructors, as above examples, and namespaces: for example, `core-js/es6/array` (`core-js/library/es6/array`) contains all [ES6 `Array` features](#ecmascript-6-array), `core-js/es6` (`core-js/library/es6`) contains all ES6 features.

##### Caveats when using CommonJS API:

* `modules` path is internal API, does not inject all required dependencies and can be changed in minor or patch releases. Use it only for a custom build and / or if you know what are you doing.
* `core-js` is extremely modular and uses a lot of very tiny modules, because of that for usage in browsers bundle up `core-js` instead of usage loader for each file, otherwise, you will have hundreds of requests.

#### CommonJS and prototype methods without global namespace pollution
In the `library` version, we can't pollute prototypes of native constructors. Because of that, prototype methods transformed to static methods like in examples above. `babel` `runtime` transformer also can't transform them. But with transpilers we can use one more trick - [bind operator and virtual methods](https://github.com/zenparsing/es-function-bind). Special for that, available `/virtual/` entry points. Example:
```js
import fill from 'core-js/library/fn/array/virtual/fill';
import findIndex from 'core-js/library/fn/array/virtual/find-index';

Array(10)::fill(0).map((a, b) => b * b)::findIndex(it => it && !(it % 8)); // => 4

// or

import {fill, findIndex} from 'core-js/library/fn/array/virtual';

Array(10)::fill(0).map((a, b) => b * b)::findIndex(it => it && !(it % 8)); // => 4

```

### Custom build (from the command-line)
```
npm i core-js && cd node_modules/core-js && npm i
npm run grunt build:core.dict,es6 -- --blacklist=es6.promise,es6.math --library=on --path=custom uglify
```
Where `core.dict` and `es6` are modules (namespaces) names, which will be added to the build, `es6.promise` and `es6.math` are modules (namespaces) names, which will be excluded from the build, `--library=on` is flag for build without global namespace pollution and `custom` is target file name.

Available namespaces: for example, `es6.array` contains [ES6 `Array` features](#ecmascript-6-array), `es6` contains all modules whose names start with `es6`.

### Custom build (from external scripts)

[`core-js-builder`](https://www.npmjs.com/package/core-js-builder) package exports a function that takes the same parameters as the `build` target from the previous section. This will conditionally include or exclude certain parts of `core-js`:

```js
require('core-js-builder')({
  modules: ['es6', 'core.dict'], // modules / namespaces
  blacklist: ['es6.reflect'],    // blacklist of modules / namespaces, by default - empty list
  library: false,                // flag for build without global namespace pollution, by default - false
  umd: true                      // use UMD wrapper for export `core` object, by default - true
}).then(code => {
  // ...
}).catch(error => {
  // ...
});
```
## Supported engines
**Tested in:**
- Chrome 26+
- Firefox 4+
- Safari 5+
- Opera 12+
- Internet Explorer 6+ (sure, IE8- with ES3 limitations)
- Edge
- Android Browser 2.3+
- iOS Safari 5.1+
- PhantomJS 1.9 / 2.1
- NodeJS 0.8+

...and it doesn't mean `core-js` will not work in other engines, they just have not been tested.

## Features:
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)       <- all features
core-js(/library)/shim  <- only polyfills
```
### ECMAScript 5
All features moved to the [`es6` namespace](#ecmascript-6), here just a list of features:
```js
Object
  .create(proto | null, descriptors?)    -> object
  .getPrototypeOf(object)                -> proto | null
  .defineProperty(target, key, desc)     -> target, cap for ie8-
  .defineProperties(target, descriptors) -> target, cap for ie8-
  .getOwnPropertyDescriptor(object, key) -> desc
  .getOwnPropertyNames(object)           -> array
  .keys(object)                          -> array
  .seal(object)                          -> object, cap for ie8-
  .freeze(object)                        -> object, cap for ie8-
  .preventExtensions(object)             -> object, cap for ie8-
  .isSealed(object)                      -> bool, cap for ie8-
  .isFrozen(object)                      -> bool, cap for ie8-
  .isExtensible(object)                  -> bool, cap for ie8-
Array
  .isArray(var)                                -> bool
  #slice(start?, end?)                         -> array, fix for ie7-
  #join(string = ',')                          -> string, fix for ie7-
  #indexOf(var, from?)                         -> int
  #lastIndexOf(var, from?)                     -> int
  #every(fn(val, index, @), that)              -> bool
  #some(fn(val, index, @), that)               -> bool
  #forEach(fn(val, index, @), that)            -> void
  #map(fn(val, index, @), that)                -> array
  #filter(fn(val, index, @), that)             -> array
  #reduce(fn(memo, val, index, @), memo?)      -> var
  #reduceRight(fn(memo, val, index, @), memo?) -> var
  #sort(fn?)                                   -> @, fixes for some engines
Function
  #bind(object, ...args) -> boundFn(...args)
String
  #split(separator, limit) -> array
  #trim()                  -> str
RegExp
  #toString() -> str
Number
  #toFixed(digits)        -> string
  #toPrecision(precision) -> string
parseInt(str, radix) -> int
parseFloat(str)      -> num
Date
  .now()         -> int
  #toISOString() -> string
  #toJSON()      -> string
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es5
```

### ECMAScript 6
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6
```
#### ECMAScript 6: Object
Modules [`es6.object.assign`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.assign.js), [`es6.object.is`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.is.js), [`es6.object.set-prototype-of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.set-prototype-of.js) and [`es6.object.to-string`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.to-string.js).

In ES6 most `Object` static methods should work with primitives. Modules [`es6.object.freeze`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.freeze.js), [`es6.object.seal`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.seal.js), [`es6.object.prevent-extensions`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.prevent-extensions.js), [`es6.object.is-frozen`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.is-frozen.js), [`es6.object.is-sealed`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.is-sealed.js), [`es6.object.is-extensible`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.is-extensible.js), [`es6.object.get-own-property-descriptor`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.get-own-property-descriptor.js), [`es6.object.get-prototype-of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.get-prototype-of.js), [`es6.object.keys`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.keys.js) and [`es6.object.get-own-property-names`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.get-own-property-names.js).

Just ES5 features: [`es6.object.create`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.create.js), [`es6.object.define-property`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.define-property.js) and [`es6.object.define-properties`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.object.es6.object.define-properties.js).
```js
Object
  .assign(target, ...src)                -> target
  .is(a, b)                              -> bool
  .setPrototypeOf(target, proto | null)  -> target (required __proto__ - IE11+)
  .create(object | null, descriptors?)   -> object
  .getPrototypeOf(var)                   -> object | null
  .defineProperty(object, key, desc)     -> target
  .defineProperties(object, descriptors) -> target
  .getOwnPropertyDescriptor(var, key)    -> desc | undefined
  .keys(var)                             -> array
  .getOwnPropertyNames(var)              -> array
  .freeze(var)                           -> var
  .seal(var)                             -> var
  .preventExtensions(var)                -> var
  .isFrozen(var)                         -> bool
  .isSealed(var)                         -> bool
  .isExtensible(var)                     -> bool
  #toString()                            -> string, ES6 fix: @@toStringTag support
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/object
core-js(/library)/fn/object/assign
core-js(/library)/fn/object/is
core-js(/library)/fn/object/set-prototype-of
core-js(/library)/fn/object/get-prototype-of
core-js(/library)/fn/object/create
core-js(/library)/fn/object/define-property
core-js(/library)/fn/object/define-properties
core-js(/library)/fn/object/get-own-property-descriptor
core-js(/library)/fn/object/keys
core-js(/library)/fn/object/get-own-property-names
core-js(/library)/fn/object/freeze
core-js(/library)/fn/object/seal
core-js(/library)/fn/object/prevent-extensions
core-js(/library)/fn/object/is-frozen
core-js(/library)/fn/object/is-sealed
core-js(/library)/fn/object/is-extensible
core-js/fn/object/to-string
```
[*Examples*](http://goo.gl/ywdwPz):
```js
var foo = {q: 1, w: 2}
  , bar = {e: 3, r: 4}
  , baz = {t: 5, y: 6};
Object.assign(foo, bar, baz); // => foo = {q: 1, w: 2, e: 3, r: 4, t: 5, y: 6}

Object.is(NaN, NaN); // => true
Object.is(0, -0);    // => false
Object.is(42, 42);   // => true
Object.is(42, '42'); // => false

function Parent(){}
function Child(){}
Object.setPrototypeOf(Child.prototype, Parent.prototype);
new Child instanceof Child;  // => true
new Child instanceof Parent; // => true

var O = {};
O[Symbol.toStringTag] = 'Foo';
'' + O; // => '[object Foo]'

Object.keys('qwe'); // => ['0', '1', '2']
Object.getPrototypeOf('qwe') === String.prototype; // => true
```
#### ECMAScript 6: Function
Modules [`es6.function.name`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.function.name.js), [`es6.function.has-instance`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.function.has-instance.js). Just ES5: [`es6.function.bind`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.function.bind.js).
```js
Function
  #bind(object, ...args) -> boundFn(...args)
  #name                  -> string (IE9+)
  #@@hasInstance(var)    -> bool
```
[*CommonJS entry points:*](#commonjs)
```
core-js/es6/function
core-js/fn/function/name
core-js/fn/function/has-instance
core-js/fn/function/bind
core-js/fn/function/virtual/bind
```
[*Example*](http://goo.gl/zqu3Wp):
```js
(function foo(){}).name // => 'foo'

console.log.bind(console, 42)(43); // => 42 43
```
#### ECMAScript 6: Array
Modules [`es6.array.from`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.from.js), [`es6.array.of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.of.js), [`es6.array.copy-within`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.copy-within.js), [`es6.array.fill`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.fill.js), [`es6.array.find`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.find.js), [`es6.array.find-index`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.find-index.js), [`es6.array.iterator`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.iterator.js). ES5 features with fixes: [`es6.array.is-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.is-array.js), [`es6.array.slice`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.slice.js), [`es6.array.join`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.join.js), [`es6.array.index-of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.index-of.js), [`es6.array.last-index-of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.last-index-of.js), [`es6.array.every`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.every.js), [`es6.array.some`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.some.js), [`es6.array.for-each`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.for-each.js), [`es6.array.map`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.map.js), [`es6.array.filter`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.filter.js), [`es6.array.reduce`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.reduce.js), [`es6.array.reduce-right`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.reduce-right.js), [`es6.array.sort`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.array.sort.js).
```js
Array
  .from(iterable | array-like, mapFn(val, index)?, that) -> array
  .of(...args)                                           -> array
  .isArray(var)                                          -> bool
  #copyWithin(target = 0, start = 0, end = @length)      -> @
  #fill(val, start = 0, end = @length)                   -> @
  #find(fn(val, index, @), that)                         -> val
  #findIndex(fn(val, index, @), that)                    -> index | -1
  #values()                                              -> iterator
  #keys()                                                -> iterator
  #entries()                                             -> iterator
  #join(string = ',')                                    -> string, fix for ie7-
  #slice(start?, end?)                                   -> array, fix for ie7-
  #indexOf(var, from?)                                   -> index | -1
  #lastIndexOf(var, from?)                               -> index | -1
  #every(fn(val, index, @), that)                        -> bool
  #some(fn(val, index, @), that)                         -> bool
  #forEach(fn(val, index, @), that)                      -> void
  #map(fn(val, index, @), that)                          -> array
  #filter(fn(val, index, @), that)                       -> array
  #reduce(fn(memo, val, index, @), memo?)                -> var
  #reduceRight(fn(memo, val, index, @), memo?)           -> var
  #sort(fn?)                                             -> @, invalid arguments fix
  #@@iterator()                                          -> iterator (values)
  #@@unscopables                                         -> object (cap)
Arguments
  #@@iterator() -> iterator (values, available only in core-js methods)
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/array
core-js(/library)/fn/array/from
core-js(/library)/fn/array/of
core-js(/library)/fn/array/is-array
core-js(/library)/fn/array/iterator
core-js(/library)/fn/array/copy-within
core-js(/library)/fn/array/fill
core-js(/library)/fn/array/find
core-js(/library)/fn/array/find-index
core-js(/library)/fn/array/values
core-js(/library)/fn/array/keys
core-js(/library)/fn/array/entries
core-js(/library)/fn/array/slice
core-js(/library)/fn/array/join
core-js(/library)/fn/array/index-of
core-js(/library)/fn/array/last-index-of
core-js(/library)/fn/array/every
core-js(/library)/fn/array/some
core-js(/library)/fn/array/for-each
core-js(/library)/fn/array/map
core-js(/library)/fn/array/filter
core-js(/library)/fn/array/reduce
core-js(/library)/fn/array/reduce-right
core-js(/library)/fn/array/sort
core-js(/library)/fn/array/virtual/iterator
core-js(/library)/fn/array/virtual/copy-within
core-js(/library)/fn/array/virtual/fill
core-js(/library)/fn/array/virtual/find
core-js(/library)/fn/array/virtual/find-index
core-js(/library)/fn/array/virtual/values
core-js(/library)/fn/array/virtual/keys
core-js(/library)/fn/array/virtual/entries
core-js(/library)/fn/array/virtual/slice
core-js(/library)/fn/array/virtual/join
core-js(/library)/fn/array/virtual/index-of
core-js(/library)/fn/array/virtual/last-index-of
core-js(/library)/fn/array/virtual/every
core-js(/library)/fn/array/virtual/some
core-js(/library)/fn/array/virtual/for-each
core-js(/library)/fn/array/virtual/map
core-js(/library)/fn/array/virtual/filter
core-js(/library)/fn/array/virtual/reduce
core-js(/library)/fn/array/virtual/reduce-right
core-js(/library)/fn/array/virtual/sort
```
[*Examples*](http://goo.gl/oaUFUf):
```js
Array.from(new Set([1, 2, 3, 2, 1]));      // => [1, 2, 3]
Array.from({0: 1, 1: 2, 2: 3, length: 3}); // => [1, 2, 3]
Array.from('123', Number);                 // => [1, 2, 3]
Array.from('123', function(it){
  return it * it;
});                                        // => [1, 4, 9]

Array.of(1);       // => [1]
Array.of(1, 2, 3); // => [1, 2, 3]

var array = ['a', 'b', 'c'];

for(var val of array)console.log(val);          // => 'a', 'b', 'c'
for(var val of array.values())console.log(val); // => 'a', 'b', 'c'
for(var key of array.keys())console.log(key);   // => 0, 1, 2
for(var [key, val] of array.entries()){
  console.log(key);                             // => 0, 1, 2
  console.log(val);                             // => 'a', 'b', 'c'
}

function isOdd(val){
  return val % 2;
}
[4, 8, 15, 16, 23, 42].find(isOdd);      // => 15
[4, 8, 15, 16, 23, 42].findIndex(isOdd); // => 2
[4, 8, 15, 16, 23, 42].find(isNaN);      // => undefined
[4, 8, 15, 16, 23, 42].findIndex(isNaN); // => -1

Array(5).fill(42); // => [42, 42, 42, 42, 42]

[1, 2, 3, 4, 5].copyWithin(0, 3); // => [4, 5, 3, 4, 5]
```
#### ECMAScript 6: String
Modules [`es6.string.from-code-point`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.from-code-point.js), [`es6.string.raw`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.raw.js), [`es6.string.iterator`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.iterator.js), [`es6.string.code-point-at`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.code-point-at.js), [`es6.string.ends-with`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.ends-with.js), [`es6.string.includes`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.includes.js), [`es6.string.repeat`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.repeat.js), [`es6.string.starts-with`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.starts-with.js) and [`es6.string.trim`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.trim.js).

Annex B HTML methods. Ugly, but it's also the part of the spec. Modules [`es6.string.anchor`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.anchor.js), [`es6.string.big`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.big.js), [`es6.string.blink`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.blink.js), [`es6.string.bold`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.bold.js), [`es6.string.fixed`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.fixed.js), [`es6.string.fontcolor`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.fontcolor.js), [`es6.string.fontsize`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.fontsize.js), [`es6.string.italics`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.italics.js), [`es6.string.link`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.link.js), [`es6.string.small`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.small.js), [`es6.string.strike`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.strike.js), [`es6.string.sub`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.sub.js) and [`es6.string.sup`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.string.sup.js).
```js
String
  .fromCodePoint(...codePoints) -> str
  .raw({raw}, ...substitutions) -> str
  #includes(str, from?) -> bool
  #startsWith(str, from?) -> bool
  #endsWith(str, from?) -> bool
  #repeat(num) -> str
  #codePointAt(pos) -> uint
  #trim() -> str, ES6 fix
  #anchor(name)     -> str
  #big()            -> str
  #blink()          -> str
  #bold()           -> str
  #fixed()          -> str
  #fontcolor(color) -> str
  #fontsize(size)   -> str
  #italics()        -> str
  #link(url)        -> str
  #small()          -> str
  #strike()         -> str
  #sub()            -> str
  #sup()            -> str
  #@@iterator() -> iterator (code points)
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/string
core-js(/library)/fn/string/from-code-point
core-js(/library)/fn/string/raw
core-js(/library)/fn/string/includes
core-js(/library)/fn/string/starts-with
core-js(/library)/fn/string/ends-with
core-js(/library)/fn/string/repeat
core-js(/library)/fn/string/code-point-at
core-js(/library)/fn/string/trim
core-js(/library)/fn/string/anchor
core-js(/library)/fn/string/big
core-js(/library)/fn/string/blink
core-js(/library)/fn/string/bold
core-js(/library)/fn/string/fixed
core-js(/library)/fn/string/fontcolor
core-js(/library)/fn/string/fontsize
core-js(/library)/fn/string/italics
core-js(/library)/fn/string/link
core-js(/library)/fn/string/small
core-js(/library)/fn/string/strike
core-js(/library)/fn/string/sub
core-js(/library)/fn/string/sup
core-js(/library)/fn/string/iterator
core-js(/library)/fn/string/virtual/includes
core-js(/library)/fn/string/virtual/starts-with
core-js(/library)/fn/string/virtual/ends-with
core-js(/library)/fn/string/virtual/repeat
core-js(/library)/fn/string/virtual/code-point-at
core-js(/library)/fn/string/virtual/trim
core-js(/library)/fn/string/virtual/anchor
core-js(/library)/fn/string/virtual/big
core-js(/library)/fn/string/virtual/blink
core-js(/library)/fn/string/virtual/bold
core-js(/library)/fn/string/virtual/fixed
core-js(/library)/fn/string/virtual/fontcolor
core-js(/library)/fn/string/virtual/fontsize
core-js(/library)/fn/string/virtual/italics
core-js(/library)/fn/string/virtual/link
core-js(/library)/fn/string/virtual/small
core-js(/library)/fn/string/virtual/strike
core-js(/library)/fn/string/virtual/sub
core-js(/library)/fn/string/virtual/sup
core-js(/library)/fn/string/virtual/iterator
```
[*Examples*](http://goo.gl/3UaQ93):
```js
for(var val of 'a𠮷b'){
  console.log(val); // => 'a', '𠮷', 'b'
}

'foobarbaz'.includes('bar');      // => true
'foobarbaz'.includes('bar', 4);   // => false
'foobarbaz'.startsWith('foo');    // => true
'foobarbaz'.startsWith('bar', 3); // => true
'foobarbaz'.endsWith('baz');      // => true
'foobarbaz'.endsWith('bar', 6);   // => true

'string'.repeat(3); // => 'stringstringstring'

'𠮷'.codePointAt(0); // => 134071
String.fromCodePoint(97, 134071, 98); // => 'a𠮷b'

var name = 'Bob';
String.raw`Hi\n${name}!`;           // => 'Hi\\nBob!' (ES6 template string syntax)
String.raw({raw: 'test'}, 0, 1, 2); // => 't0e1s2t'

'foo'.bold();                     // => '<b>foo</b>'
'bar'.anchor('a"b');              // => '<a name="a&quot;b">bar</a>'
'baz'.link('http://example.com'); // => '<a href="http://example.com">baz</a>'
```
#### ECMAScript 6: RegExp
Modules [`es6.regexp.constructor`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.regexp.constructor.js) and [`es6.regexp.flags`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.regexp.flags.js).

Support well-known [symbols](#ecmascript-6-symbol) `@@match`, `@@replace`, `@@search` and `@@split`, modules [`es6.regexp.match`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.regexp.match.js), [`es6.regexp.replace`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.regexp.replace.js), [`es6.regexp.search`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.regexp.search.js) and [`es6.regexp.split`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.regexp.split.js).
```
[new] RegExp(pattern, flags?) -> regexp, ES6 fix: can alter flags (IE9+)
  #flags -> str (IE9+)
  #toString() -> str, ES6 fixes
  #@@match(str)             -> array | null
  #@@replace(str, replacer) -> string
  #@@search(str)            -> index
  #@@split(str, limit)      -> array
String
  #match(tpl)             -> var, ES6 fix for support @@match
  #replace(tpl, replacer) -> var, ES6 fix for support @@replace
  #search(tpl)            -> var, ES6 fix for support @@search
  #split(tpl, limit)      -> var, ES6 fix for support @@split, some fixes for old engines
```
[*CommonJS entry points:*](#commonjs)
```
core-js/es6/regexp
core-js/fn/regexp/constructor
core-js(/library)/fn/regexp/flags
core-js/fn/regexp/to-string
core-js/fn/regexp/match
core-js/fn/regexp/replace
core-js/fn/regexp/search
core-js/fn/regexp/split
```
[*Examples*](http://goo.gl/PiJxBD):
```js
RegExp(/./g, 'm'); // => /./m

/foo/.flags;    // => ''
/foo/gim.flags; // => 'gim'

'foo'.match({[Symbol.match]: _ => 1});     // => 1
'foo'.replace({[Symbol.replace]: _ => 2}); // => 2
'foo'.search({[Symbol.search]: _ => 3});   // => 3
'foo'.split({[Symbol.split]: _ => 4});     // => 4

RegExp.prototype.toString.call({source: 'foo', flags: 'bar'}); // => '/foo/bar'
```
#### ECMAScript 6: Number
Module [`es6.number.constructor`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.constructor.js). `Number` constructor support binary and octal literals, [*example*](http://goo.gl/jRd6b3):
```js
Number('0b1010101'); // => 85
Number('0o7654321'); // => 2054353
```
Modules [`es6.number.epsilon`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.epsilon.js), [`es6.number.is-finite`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.is-finite.js), [`es6.number.is-integer`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.is-integer.js), [`es6.number.is-nan`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.is-nan.js), [`es6.number.is-safe-integer`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.is-safe-integer.js), [`es6.number.max-safe-integer`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.max-safe-integer.js), [`es6.number.min-safe-integer`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.min-safe-integer.js), [`es6.number.parse-float`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.parse-float.js), [`es6.number.parse-int`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.parse-int.js), [`es6.number.to-fixed`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.to-fixed.js), [`es6.number.to-precision`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.number.to-precision.js), [`es6.parse-int`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.parse-int.js), [`es6.parse-float`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.parse-float.js).
```js
[new] Number(var)         -> number | number object
  .isFinite(num)          -> bool
  .isNaN(num)             -> bool
  .isInteger(num)         -> bool
  .isSafeInteger(num)     -> bool
  .parseFloat(str)        -> num
  .parseInt(str)          -> int
  .EPSILON                -> num
  .MAX_SAFE_INTEGER       -> int
  .MIN_SAFE_INTEGER       -> int
  #toFixed(digits)        -> string, fixes
  #toPrecision(precision) -> string, fixes
parseFloat(str)           -> num, fixes
parseInt(str)             -> int, fixes
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/number
core-js/es6/number/constructor
core-js(/library)/fn/number/is-finite
core-js(/library)/fn/number/is-nan
core-js(/library)/fn/number/is-integer
core-js(/library)/fn/number/is-safe-integer
core-js(/library)/fn/number/parse-float
core-js(/library)/fn/number/parse-int
core-js(/library)/fn/number/epsilon
core-js(/library)/fn/number/max-safe-integer
core-js(/library)/fn/number/min-safe-integer
core-js(/library)/fn/number/to-fixed
core-js(/library)/fn/number/to-precision
core-js(/library)/fn/parse-float
core-js(/library)/fn/parse-int
```
#### ECMAScript 6: Math
Modules [`es6.math.acosh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.acosh.js), [`es6.math.asinh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.asinh.js), [`es6.math.atanh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.atanh.js), [`es6.math.cbrt`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.cbrt.js), [`es6.math.clz32`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.clz32.js), [`es6.math.cosh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.cosh.js), [`es6.math.expm1`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.expm1.js), [`es6.math.fround`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.fround.js), [`es6.math.hypot`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.hypot.js), [`es6.math.imul`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.imul.js), [`es6.math.log10`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.log10.js), [`es6.math.log1p`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.log1p.js), [`es6.math.log2`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.log2.js), [`es6.math.sign`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.sign.js), [`es6.math.sinh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.sinh.js), [`es6.math.tanh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.tanh.js), [`es6.math.trunc`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.math.trunc.js).
```js
Math
  .acosh(num)     -> num
  .asinh(num)     -> num
  .atanh(num)     -> num
  .cbrt(num)      -> num
  .clz32(num)     -> uint
  .cosh(num)      -> num
  .expm1(num)     -> num
  .fround(num)    -> num
  .hypot(...args) -> num
  .imul(num, num) -> int
  .log1p(num)     -> num
  .log10(num)     -> num
  .log2(num)      -> num
  .sign(num)      -> 1 | -1 | 0 | -0 | NaN
  .sinh(num)      -> num
  .tanh(num)      -> num
  .trunc(num)     -> num
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/math
core-js(/library)/fn/math/acosh
core-js(/library)/fn/math/asinh
core-js(/library)/fn/math/atanh
core-js(/library)/fn/math/cbrt
core-js(/library)/fn/math/clz32
core-js(/library)/fn/math/cosh
core-js(/library)/fn/math/expm1
core-js(/library)/fn/math/fround
core-js(/library)/fn/math/hypot
core-js(/library)/fn/math/imul
core-js(/library)/fn/math/log1p
core-js(/library)/fn/math/log10
core-js(/library)/fn/math/log2
core-js(/library)/fn/math/sign
core-js(/library)/fn/math/sinh
core-js(/library)/fn/math/tanh
core-js(/library)/fn/math/trunc
```
#### ECMAScript 6: Date
Modules [`es6.date.to-string`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.date.to-string.js), ES5 features with fixes: [`es6.date.now`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.date.now.js), [`es6.date.to-iso-string`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.date.to-iso-string.js), [`es6.date.to-json`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.date.to-json.js) and [`es6.date.to-primitive`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.date.to-primitive.js).
```js
Date
  .now()               -> int
  #toISOString()       -> string
  #toJSON()            -> string
  #toString()          -> string
  #@@toPrimitive(hint) -> primitive
```
[*CommonJS entry points:*](#commonjs)
```
core-js/es6/date
core-js/fn/date/to-string
core-js(/library)/fn/date/now
core-js(/library)/fn/date/to-iso-string
core-js(/library)/fn/date/to-json
core-js(/library)/fn/date/to-primitive
```
[*Example*](http://goo.gl/haeHLR):
```js
new Date(NaN).toString(); // => 'Invalid Date'
```

#### ECMAScript 6: Promise
Module [`es6.promise`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.promise.js).
```js
new Promise(executor(resolve(var), reject(var))) -> promise
  #then(resolved(var), rejected(var))            -> promise
  #catch(rejected(var))                          -> promise
  .resolve(promise | var)                        -> promise
  .reject(var)                                   -> promise
  .all(iterable)                                 -> promise
  .race(iterable)                                -> promise
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/promise
core-js(/library)/fn/promise
```
Basic [*example*](http://goo.gl/vGrtUC):
```js
function sleepRandom(time){
  return new Promise(function(resolve, reject){
    setTimeout(resolve, time * 1e3, 0 | Math.random() * 1e3);
  });
}

console.log('Run');                    // => Run
sleepRandom(5).then(function(result){
  console.log(result);                 // => 869, after 5 sec.
  return sleepRandom(10);
}).then(function(result){
  console.log(result);                 // => 202, after 10 sec.
}).then(function(){
  console.log('immediately after');    // => immediately after
  throw Error('Irror!');
}).then(function(){
  console.log('will not be displayed');
}).catch(x => console.log(x));         // => => Error: Irror!
```
`Promise.resolve` and `Promise.reject` [*example*](http://goo.gl/vr8TN3):
```js
Promise.resolve(42).then(x => console.log(x)); // => 42
Promise.reject(42).catch(x => console.log(x)); // => 42

Promise.resolve($.getJSON('/data.json')); // => ES6 promise
```
`Promise.all` [*example*](http://goo.gl/RdoDBZ):
```js
Promise.all([
  'foo',
  sleepRandom(5),
  sleepRandom(15),
  sleepRandom(10)             // after 15 sec:
]).then(x => console.log(x)); // => ['foo', 956, 85, 382]
```
`Promise.race` [*example*](http://goo.gl/L8ovkJ):
```js
function timeLimit(promise, time){
  return Promise.race([promise, new Promise(function(resolve, reject){
    setTimeout(reject, time * 1e3, Error('Await > ' + time + ' sec'));
  })]);
}

timeLimit(sleepRandom(5), 10).then(x => console.log(x));   // => 853, after 5 sec.
timeLimit(sleepRandom(15), 10).catch(x => console.log(x)); // Error: Await > 10 sec
```
ECMAScript 7 [async functions](https://tc39.github.io/ecmascript-asyncawait) [example](http://goo.gl/wnQS4j):
```js
var delay = time => new Promise(resolve => setTimeout(resolve, time))

async function sleepRandom(time){
  await delay(time * 1e3);
  return 0 | Math.random() * 1e3;
};
async function sleepError(time, msg){
  await delay(time * 1e3);
  throw Error(msg);
};

(async () => {
  try {
    console.log('Run');                // => Run
    console.log(await sleepRandom(5)); // => 936, after 5 sec.
    var [a, b, c] = await Promise.all([
      sleepRandom(5),
      sleepRandom(15),
      sleepRandom(10)
    ]);
    console.log(a, b, c);              // => 210 445 71, after 15 sec.
    await sleepError(5, 'Irror!');
    console.log('Will not be displayed');
  } catch(e){
    console.log(e);                    // => Error: 'Irror!', after 5 sec.
  }
})();
```

##### Unhandled rejection tracking

In Node.js, like in native implementation, available events [`unhandledRejection`](https://nodejs.org/api/process.html#process_event_unhandledrejection) and [`rejectionHandled`](https://nodejs.org/api/process.html#process_event_rejectionhandled):
```js
process.on('unhandledRejection', (reason, promise) => console.log('unhandled', reason, promise));
process.on('rejectionHandled', (promise) => console.log('handled', promise));

var p = Promise.reject(42);
// unhandled 42 [object Promise]

setTimeout(() => p.catch(_ => _), 1e3);
// handled [object Promise]
```
In a browser on rejection, by default, you will see notify in the console, or you can add a custom handler and a handler on handling unhandled, [*example*](http://goo.gl/Wozskl):
```js
window.onunhandledrejection = e => console.log('unhandled', e.reason, e.promise);
window.onrejectionhandled = e => console.log('handled', e.reason, e.promise);

var p = Promise.reject(42);
// unhandled 42 [object Promise]

setTimeout(() => p.catch(_ => _), 1e3);
// handled 42 [object Promise]
```

#### ECMAScript 6: Symbol
Module [`es6.symbol`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.symbol.js).
```js
Symbol(description?)  -> symbol
  .hasInstance        -> @@hasInstance
  .isConcatSpreadable -> @@isConcatSpreadable
  .iterator           -> @@iterator
  .match              -> @@match
  .replace            -> @@replace
  .search             -> @@search
  .species            -> @@species
  .split              -> @@split
  .toPrimitive        -> @@toPrimitive
  .toStringTag        -> @@toStringTag
  .unscopables        -> @@unscopables
  .for(key)           -> symbol
  .keyFor(symbol)     -> key
  .useSimple()        -> void
  .useSetter()        -> void
Object
  .getOwnPropertySymbols(object) -> array
```
Also wrapped some methods for correct work with `Symbol` polyfill.
```js
Object
  .create(proto | null, descriptors?)    -> object
  .defineProperty(target, key, desc)     -> target
  .defineProperties(target, descriptors) -> target
  .getOwnPropertyDescriptor(var, key)    -> desc | undefined
  .getOwnPropertyNames(var)              -> array
  #propertyIsEnumerable(key)             -> bool
JSON
  .stringify(target, replacer?, space?) -> string | undefined
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/symbol
core-js(/library)/fn/symbol
core-js(/library)/fn/symbol/has-instance
core-js(/library)/fn/symbol/is-concat-spreadable
core-js(/library)/fn/symbol/iterator
core-js(/library)/fn/symbol/match
core-js(/library)/fn/symbol/replace
core-js(/library)/fn/symbol/search
core-js(/library)/fn/symbol/species
core-js(/library)/fn/symbol/split
core-js(/library)/fn/symbol/to-primitive
core-js(/library)/fn/symbol/to-string-tag
core-js(/library)/fn/symbol/unscopables
core-js(/library)/fn/symbol/for
core-js(/library)/fn/symbol/key-for
```
[*Basic example*](http://goo.gl/BbvWFc):
```js
var Person = (function(){
  var NAME = Symbol('name');
  function Person(name){
    this[NAME] = name;
  }
  Person.prototype.getName = function(){
    return this[NAME];
  };
  return Person;
})();

var person = new Person('Vasya');
console.log(person.getName());          // => 'Vasya'
console.log(person['name']);            // => undefined
console.log(person[Symbol('name')]);    // => undefined, symbols are uniq
for(var key in person)console.log(key); // => only 'getName', symbols are not enumerable
```
`Symbol.for` & `Symbol.keyFor` [*example*](http://goo.gl/0pdJjX):
```js
var symbol = Symbol.for('key');
symbol === Symbol.for('key'); // true
Symbol.keyFor(symbol);        // 'key'
```
[*Example*](http://goo.gl/mKVOQJ) with methods for getting own object keys:
```js
var O = {a: 1};
Object.defineProperty(O, 'b', {value: 2});
O[Symbol('c')] = 3;
Object.keys(O);                  // => ['a']
Object.getOwnPropertyNames(O);   // => ['a', 'b']
Object.getOwnPropertySymbols(O); // => [Symbol(c)]
Reflect.ownKeys(O);              // => ['a', 'b', Symbol(c)]
```
##### Caveats when using `Symbol` polyfill:

* We can't add new primitive type, `Symbol` returns object.
* `Symbol.for` and `Symbol.keyFor` can't be shimmed cross-realm.
* By default, to hide the keys, `Symbol` polyfill defines setter in `Object.prototype`. For this reason, uncontrolled creation of symbols can cause memory leak and the `in` operator is not working correctly with `Symbol` polyfill: `Symbol() in {} // => true`.

You can disable defining setters in `Object.prototype`. [Example](http://goo.gl/N5UD7J):
```js
Symbol.useSimple();
var s1 = Symbol('s1')
  , o1 = {};
o1[s1] = true;
for(var key in o1)console.log(key); // => 'Symbol(s1)_t.qamkg9f3q', w/o native Symbol

Symbol.useSetter();
var s2 = Symbol('s2')
  , o2 = {};
o2[s2] = true;
for(var key in o2)console.log(key); // nothing
```
* Currently, `core-js` not adds setters to `Object.prototype` for well-known symbols for correct work something like `Symbol.iterator in foo`. It can cause problems with their enumerability.
* Some problems possible with environment exotic objects (for example, IE `localStorage`).

#### ECMAScript 6: Collections
`core-js` uses native collections in most case, just fixes methods / constructor, if it's required, and in old environment uses fast polyfill (O(1) lookup).
#### Map
Module [`es6.map`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.map.js).
```js
new Map(iterable (entries) ?)     -> map
  #clear()                        -> void
  #delete(key)                    -> bool
  #forEach(fn(val, key, @), that) -> void
  #get(key)                       -> val
  #has(key)                       -> bool
  #set(key, val)                  -> @
  #size                           -> uint
  #values()                       -> iterator
  #keys()                         -> iterator
  #entries()                      -> iterator
  #@@iterator()                   -> iterator (entries)
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/map
core-js(/library)/fn/map
```
[*Examples*](http://goo.gl/GWR7NI):
```js
var a = [1];

var map = new Map([['a', 1], [42, 2]]);
map.set(a, 3).set(true, 4);

console.log(map.size);        // => 4
console.log(map.has(a));      // => true
console.log(map.has([1]));    // => false
console.log(map.get(a));      // => 3
map.forEach(function(val, key){
  console.log(val);           // => 1, 2, 3, 4
  console.log(key);           // => 'a', 42, [1], true
});
map.delete(a);
console.log(map.size);        // => 3
console.log(map.get(a));      // => undefined
console.log(Array.from(map)); // => [['a', 1], [42, 2], [true, 4]]

var map = new Map([['a', 1], ['b', 2], ['c', 3]]);

for(var [key, val] of map){
  console.log(key);                           // => 'a', 'b', 'c'
  console.log(val);                           // => 1, 2, 3
}
for(var val of map.values())console.log(val); // => 1, 2, 3
for(var key of map.keys())console.log(key);   // => 'a', 'b', 'c'
for(var [key, val] of map.entries()){
  console.log(key);                           // => 'a', 'b', 'c'
  console.log(val);                           // => 1, 2, 3
}
```
#### Set
Module [`es6.set`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.set.js).
```js
new Set(iterable?)              -> set
  #add(key)                     -> @
  #clear()                      -> void
  #delete(key)                  -> bool
  #forEach(fn(el, el, @), that) -> void
  #has(key)                     -> bool
  #size                         -> uint
  #values()                     -> iterator
  #keys()                       -> iterator
  #entries()                    -> iterator
  #@@iterator()                 -> iterator (values)
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/set
core-js(/library)/fn/set
```
[*Examples*](http://goo.gl/bmhLwg):
```js
var set = new Set(['a', 'b', 'a', 'c']);
set.add('d').add('b').add('e');
console.log(set.size);        // => 5
console.log(set.has('b'));    // => true
set.forEach(function(it){
  console.log(it);            // => 'a', 'b', 'c', 'd', 'e'
});
set.delete('b');
console.log(set.size);        // => 4
console.log(set.has('b'));    // => false
console.log(Array.from(set)); // => ['a', 'c', 'd', 'e']

var set = new Set([1, 2, 3, 2, 1]);

for(var val of set)console.log(val);          // => 1, 2, 3
for(var val of set.values())console.log(val); // => 1, 2, 3
for(var key of set.keys())console.log(key);   // => 1, 2, 3
for(var [key, val] of set.entries()){
  console.log(key);                           // => 1, 2, 3
  console.log(val);                           // => 1, 2, 3
}
```
#### WeakMap
Module [`es6.weak-map`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.weak-map.js).
```js
new WeakMap(iterable (entries) ?) -> weakmap
  #delete(key)                    -> bool
  #get(key)                       -> val
  #has(key)                       -> bool
  #set(key, val)                  -> @
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/weak-map
core-js(/library)/fn/weak-map
```
[*Examples*](http://goo.gl/SILXyw):
```js
var a = [1]
  , b = [2]
  , c = [3];

var wmap = new WeakMap([[a, 1], [b, 2]]);
wmap.set(c, 3).set(b, 4);
console.log(wmap.has(a));   // => true
console.log(wmap.has([1])); // => false
console.log(wmap.get(a));   // => 1
wmap.delete(a);
console.log(wmap.get(a));   // => undefined

// Private properties store:
var Person = (function(){
  var names = new WeakMap;
  function Person(name){
    names.set(this, name);
  }
  Person.prototype.getName = function(){
    return names.get(this);
  };
  return Person;
})();

var person = new Person('Vasya');
console.log(person.getName());          // => 'Vasya'
for(var key in person)console.log(key); // => only 'getName'
```
#### WeakSet
Module [`es6.weak-set`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.weak-set.js).
```js
new WeakSet(iterable?) -> weakset
  #add(key)            -> @
  #delete(key)         -> bool
  #has(key)            -> bool
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/weak-set
core-js(/library)/fn/weak-set
```
[*Examples*](http://goo.gl/TdFbEx):
```js
var a = [1]
  , b = [2]
  , c = [3];

var wset = new WeakSet([a, b, a]);
wset.add(c).add(b).add(c);
console.log(wset.has(b));   // => true
console.log(wset.has([2])); // => false
wset.delete(b);
console.log(wset.has(b));   // => false
```
##### Caveats when using collections polyfill:

* Weak-collections polyfill stores values as hidden properties of keys. It works correct and not leak in most cases. However, it is desirable to store a collection longer than its keys.

#### ECMAScript 6: Typed Arrays
Implementations and fixes `ArrayBuffer`, `DataView`, typed arrays constructors, static and prototype methods. Typed Arrays work only in environments with support descriptors (IE9+), `ArrayBuffer` and `DataView` should work anywhere.

Modules [`es6.typed.array-buffer`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.array-buffer.js), [`es6.typed.data-view`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.data-view.js), [`es6.typed.int8-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.int8-array.js), [`es6.typed.uint8-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.uint8-array.js), [`es6.typed.uint8-clamped-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.uint8-clamped-array.js), [`es6.typed.int16-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.int16-array.js), [`es6.typed.uint16-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.uint16-array.js), [`es6.typed.int32-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.int32-array.js), [`es6.typed.uint32-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.uint32-array.js), [`es6.typed.float32-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.float32-array.js) and [`es6.typed.float64-array`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.typed.float64-array.js).
```js
new ArrayBuffer(length) -> buffer
  .isView(var) -> bool
  #slice(start = 0, end = @length) -> buffer
  #byteLength -> uint

new DataView(buffer, byteOffset = 0, byteLength = buffer.byteLength - byteOffset) -> view
  #getInt8(offset)                          -> int8
  #getUint8(offset)                         -> uint8
  #getInt16(offset, littleEndian = false)   -> int16
  #getUint16(offset, littleEndian = false)  -> uint16
  #getInt32(offset, littleEndian = false)   -> int32
  #getUint32(offset, littleEndian = false)  -> uint32
  #getFloat32(offset, littleEndian = false) -> float32
  #getFloat64(offset, littleEndian = false) -> float64
  #setInt8(offset, value)                          -> void
  #setUint8(offset, value)                         -> void
  #setInt16(offset, value, littleEndian = false)   -> void
  #setUint16(offset, value, littleEndian = false)  -> void
  #setInt32(offset, value, littleEndian = false)   -> void
  #setUint32(offset, value, littleEndian = false)  -> void
  #setFloat32(offset, value, littleEndian = false) -> void
  #setFloat64(offset, value, littleEndian = false) -> void
  #buffer     -> buffer
  #byteLength -> uint
  #byteOffset -> uint

{
  Int8Array,
  Uint8Array,
  Uint8ClampedArray,
  Int16Array,
  Uint16Array,
  Int32Array,
  Uint32Array,
  Float32Array,
  Float64Array
}
  new %TypedArray%(length)    -> typed
  new %TypedArray%(typed)     -> typed
  new %TypedArray%(arrayLike) -> typed
  new %TypedArray%(iterable)  -> typed
  new %TypedArray%(buffer, byteOffset = 0, length = (buffer.byteLength - byteOffset) / @BYTES_PER_ELEMENT) -> typed
  .BYTES_PER_ELEMENT -> uint
  .from(arrayLike | iterable, mapFn(val, index)?, that) -> typed
  .of(...args) -> typed
  #BYTES_PER_ELEMENT -> uint
  #copyWithin(target = 0, start = 0, end = @length) -> @
  #every(fn(val, index, @), that) -> bool
  #fill(val, start = 0, end = @length) -> @
  #filter(fn(val, index, @), that) -> typed
  #find(fn(val, index, @), that) -> val
  #findIndex(fn(val, index, @), that) -> index
  #forEach(fn(val, index, @), that) -> void
  #indexOf(var, from?) -> int
  #join(string = ',') -> string
  #lastIndexOf(var, from?) -> int
  #map(fn(val, index, @), that) -> typed
  #reduce(fn(memo, val, index, @), memo?) -> var
  #reduceRight(fn(memo, val, index, @), memo?) -> var
  #reverse() -> @
  #set(arrayLike, offset = 0) -> void
  #slice(start = 0, end = @length) -> typed
  #some(fn(val, index, @), that) -> bool
  #sort(fn(a, b)?) -> @
  #subarray(start = 0, end = @length) -> typed
  #toString() -> string
  #toLocaleString() -> string
  #values()     -> iterator
  #keys()       -> iterator
  #entries()    -> iterator
  #@@iterator() -> iterator (values)
  #buffer     -> buffer
  #byteLength -> uint
  #byteOffset -> uint
  #length     -> uint
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/typed
core-js(/library)/fn/typed
core-js(/library)/fn/typed/array-buffer
core-js(/library)/fn/typed/data-view
core-js(/library)/fn/typed/int8-array
core-js(/library)/fn/typed/uint8-array
core-js(/library)/fn/typed/uint8-clamped-array
core-js(/library)/fn/typed/int16-array
core-js(/library)/fn/typed/uint16-array
core-js(/library)/fn/typed/int32-array
core-js(/library)/fn/typed/uint32-array
core-js(/library)/fn/typed/float32-array
core-js(/library)/fn/typed/float64-array
```
[*Examples*](http://goo.gl/yla75z):
```js
new Int32Array(4);                          // => [0, 0, 0, 0]
new Uint8ClampedArray([1, 2, 3, 666]);      // => [1, 2, 3, 255]
new Float32Array(new Set([1, 2, 3, 2, 1])); // => [1, 2, 3]

var buffer = new ArrayBuffer(8);
var view   = new DataView(buffer);
view.setFloat64(0, 123.456, true);
new Uint8Array(buffer.slice(4)); // => [47, 221, 94, 64]

Int8Array.of(1, 1.5, 5.7, 745);      // => [1, 1, 5, -23]
Uint8Array.from([1, 1.5, 5.7, 745]); // => [1, 1, 5, 233]

var typed = new Uint8Array([1, 2, 3]);

var a = typed.slice(1);    // => [2, 3]
typed.buffer === a.buffer; // => false
var b = typed.subarray(1); // => [2, 3]
typed.buffer === b.buffer; // => true

typed.filter(it => it % 2); // => [1, 3]
typed.map(it => it * 1.5);  // => [1, 3, 4]

for(var val of typed)console.log(val);          // => 1, 2, 3
for(var val of typed.values())console.log(val); // => 1, 2, 3
for(var key of typed.keys())console.log(key);   // => 0, 1, 2
for(var [key, val] of typed.entries()){
  console.log(key);                             // => 0, 1, 2
  console.log(val);                             // => 1, 2, 3
}
```
##### Caveats when using typed arrays:

* Typed Arrays polyfills works completely how should work by the spec, but because of internal use getter / setters on each instance, is slow and consumes significant memory. However, typed arrays polyfills required mainly for IE9 (and for `Uint8ClampedArray` in IE10 and early IE11), all modern engines have native typed arrays and requires only constructors fixes and methods.
* The current version hasn't special entry points for methods, they can be added only with constructors. It can be added in the future.
* In the `library` version we can't pollute native prototypes, so prototype methods available as constructors static.

#### ECMAScript 6: Reflect
Modules [`es6.reflect.apply`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.apply.js), [`es6.reflect.construct`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.construct.js), [`es6.reflect.define-property`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.define-property.js), [`es6.reflect.delete-property`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.delete-property.js), [`es6.reflect.enumerate`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.enumerate.js), [`es6.reflect.get`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.get.js), [`es6.reflect.get-own-property-descriptor`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.get-own-property-descriptor.js), [`es6.reflect.get-prototype-of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.get-prototype-of.js), [`es6.reflect.has`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.has.js), [`es6.reflect.is-extensible`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.is-extensible.js), [`es6.reflect.own-keys`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.own-keys.js), [`es6.reflect.prevent-extensions`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.prevent-extensions.js), [`es6.reflect.set`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.set.js), [`es6.reflect.set-prototype-of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es6.reflect.set-prototype-of.js).
```js
Reflect
  .apply(target, thisArgument, argumentsList) -> var
  .construct(target, argumentsList, newTarget?) -> object
  .defineProperty(target, propertyKey, attributes) -> bool
  .deleteProperty(target, propertyKey) -> bool
  .enumerate(target) -> iterator (removed from the spec and will be removed from core-js@3)
  .get(target, propertyKey, receiver?) -> var
  .getOwnPropertyDescriptor(target, propertyKey) -> desc
  .getPrototypeOf(target) -> object | null
  .has(target, propertyKey) -> bool
  .isExtensible(target) -> bool
  .ownKeys(target) -> array
  .preventExtensions(target) -> bool
  .set(target, propertyKey, V, receiver?) -> bool
  .setPrototypeOf(target, proto) -> bool (required __proto__ - IE11+)
```
[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es6/reflect
core-js(/library)/fn/reflect
core-js(/library)/fn/reflect/apply
core-js(/library)/fn/reflect/construct
core-js(/library)/fn/reflect/define-property
core-js(/library)/fn/reflect/delete-property
core-js(/library)/fn/reflect/enumerate (deprecated and will be removed from the next major release)
core-js(/library)/fn/reflect/get
core-js(/library)/fn/reflect/get-own-property-descriptor
core-js(/library)/fn/reflect/get-prototype-of
core-js(/library)/fn/reflect/has
core-js(/library)/fn/reflect/is-extensible
core-js(/library)/fn/reflect/own-keys
core-js(/library)/fn/reflect/prevent-extensions
core-js(/library)/fn/reflect/set
core-js(/library)/fn/reflect/set-prototype-of
```
[*Examples*](http://goo.gl/gVT0cH):
```js
var O = {a: 1};
Object.defineProperty(O, 'b', {value: 2});
O[Symbol('c')] = 3;
Reflect.ownKeys(O); // => ['a', 'b', Symbol(c)]

function C(a, b){
  this.c = a + b;
}

var instance = Reflect.construct(C, [20, 22]);
instance.c; // => 42
```

### ECMAScript 7+ proposals
[The TC39 process.](https://tc39.github.io/process-document/)

[*CommonJS entry points:*](#commonjs)
```
core-js(/library)/es7
core-js(/library)/es7/array
core-js(/library)/es7/global
core-js(/library)/es7/string
core-js(/library)/es7/map
core-js(/library)/es7/set
core-js(/library)/es7/error
core-js(/library)/es7/math
core-js(/library)/es7/system
core-js(/library)/es7/symbol
core-js(/library)/es7/reflect
core-js(/library)/es7/observable
```
`core-js/stage/4` entry point contains only stage 4 proposals, `core-js/stage/3` - stage 3 and stage 4, etc.
#### Stage 4 proposals

[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/stage/4
```
* `{Array, %TypedArray%}#includes` [proposal](https://github.com/tc39/Array.prototype.includes) - module [`es7.array.includes`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.array.includes.js), `%TypedArray%` version in modules from [this section](#ecmascript-6-typed-arrays).
```js
Array
  #includes(var, from?) -> bool
{
  Int8Array,
  Uint8Array,
  Uint8ClampedArray,
  Int16Array,
  Uint16Array,
  Int32Array,
  Uint32Array,
  Float32Array,
  Float64Array
}
  #includes(var, from?) -> bool
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/array/includes
```
[*Examples*](http://goo.gl/2Gq4ma):
```js
[1, 2, 3].includes(2);        // => true
[1, 2, 3].includes(4);        // => false
[1, 2, 3].includes(2, 2);     // => false

[NaN].indexOf(NaN);           // => -1
[NaN].includes(NaN);          // => true
Array(1).indexOf(undefined);  // => -1
Array(1).includes(undefined); // => true
```
* `Object.values`, `Object.entries` [proposal](https://github.com/tc39/proposal-object-values-entries) - modules [`es7.object.values`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.values.js), [`es7.object.entries`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.entries.js)
```js
Object
  .values(object) -> array
  .entries(object) -> array
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/object/values
core-js(/library)/fn/object/entries
```
[*Examples*](http://goo.gl/6kuGOn):
```js
Object.values({a: 1, b: 2, c: 3});  // => [1, 2, 3]
Object.entries({a: 1, b: 2, c: 3}); // => [['a', 1], ['b', 2], ['c', 3]]

for(let [key, value] of Object.entries({a: 1, b: 2, c: 3})){
  console.log(key);   // => 'a', 'b', 'c'
  console.log(value); // => 1, 2, 3
}
```
* `Object.getOwnPropertyDescriptors` [proposal](https://github.com/tc39/proposal-object-getownpropertydescriptors) - module [`es7.object.get-own-property-descriptors`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.get-own-property-descriptors.js)
```js
Object
  .getOwnPropertyDescriptors(object) -> object
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/object/get-own-property-descriptors
```
*Examples*:
```js
// Shallow object cloning with prototype and descriptors:
var copy = Object.create(Object.getPrototypeOf(O), Object.getOwnPropertyDescriptors(O));
// Mixin:
Object.defineProperties(target, Object.getOwnPropertyDescriptors(source));
```
* `String#padStart`, `String#padEnd` [proposal](https://github.com/tc39/proposal-string-pad-start-end) - modules [`es7.string.pad-start`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.string.pad-start.js), [`es7.string.pad-end`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.string.pad-end.js)
```js
String
  #padStart(length, fillStr = ' ') -> string
  #padEnd(length, fillStr = ' ') -> string
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/string/pad-start
core-js(/library)/fn/string/pad-end
core-js(/library)/fn/string/virtual/pad-start
core-js(/library)/fn/string/virtual/pad-end
```
[*Examples*](http://goo.gl/hK5ccv):
```js
'hello'.padStart(10);         // => '     hello'
'hello'.padStart(10, '1234'); // => '12341hello'
'hello'.padEnd(10);           // => 'hello     '
'hello'.padEnd(10, '1234');   // => 'hello12341'
```
* `Object#__(define|lookup)[GS]etter__`, [annex B ES2017](https://github.com/tc39/ecma262/pull/381), but we haven't special namespace for that - modules [`es7.object.define-setter`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.define-setter.js), [`es7.object.define-getter`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.define-getter.js), [`es7.object.lookup-setter`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.lookup-setter.js) and [`es7.object.lookup-getter`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.object.lookup-getter.js).
```js
Object
  #__defineSetter__(key, fn) -> void
  #__defineGetter__(key, fn) -> void
  #__lookupSetter__(key) -> fn | void
  #__lookupGetter__(key) -> fn | void
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/object/define-getter
core-js(/library)/fn/object/define-setter
core-js(/library)/fn/object/lookup-getter
core-js(/library)/fn/object/lookup-setter
```

#### Stage 3 proposals
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/stage/3
```
* `global` [proposal](https://github.com/tc39/proposal-global) - modules [`es7.global`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.global.js) and [`es7.system.global`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.system.global.js) (obsolete)
```js
global -> object
System
  .global -> object (obsolete)
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/global
core-js(/library)/fn/system/global (obsolete)
```
[*Examples*](http://goo.gl/gEqMl7):
```js
global.Array === Array; // => true
```
* `Promise#finally` [proposal](https://github.com/tc39/proposal-promise-finally) - module [`es7.promise.finally`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.promise.finally.js)
```js
Promise
  #finally(onFinally()) -> promise
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/promise/finally
```
[*Examples*](https://goo.gl/AhyBbJ):
```js
Promise.resolve(42).finally(() => console.log('You will see it anyway'));

Promise.reject(42).finally(() => console.log('You will see it anyway'));

#### Stage 2 proposals
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/stage/2
```
* `String#trimLeft`, `String#trimRight` / `String#trimStart`, `String#trimEnd` [proposal](https://github.com/sebmarkbage/ecmascript-string-left-right-trim) - modules [`es7.string.trim-left`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.string.trim-right.js), [`es7.string.trim-right`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.string.trim-right.js)
```js
String
  #trimLeft()  -> string
  #trimRight() -> string
  #trimStart() -> string
  #trimEnd()   -> string
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/string/trim-start
core-js(/library)/fn/string/trim-end
core-js(/library)/fn/string/trim-left
core-js(/library)/fn/string/trim-right
core-js(/library)/fn/string/virtual/trim-start
core-js(/library)/fn/string/virtual/trim-end
core-js(/library)/fn/string/virtual/trim-left
core-js(/library)/fn/string/virtual/trim-right
```
[*Examples*](http://goo.gl/Er5lMJ):
```js
'   hello   '.trimLeft();  // => 'hello   '
'   hello   '.trimRight(); // => '   hello'
```
```
* `Symbol.asyncIterator` for [async iteration proposal](https://github.com/tc39/proposal-async-iteration) - module [`es7.symbol.async-iterator`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.symbol.async-iterator.js)
```js
Symbol
  .asyncIterator -> @@asyncIterator
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/symbol/async-iterator
```

#### Stage 1 proposals
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/stage/1
```
* `Promise.try` [proposal](https://github.com/tc39/proposal-promise-try) - module [`es7.promise.try`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.promise.try.js)
```js
Promise
  .try(function()) -> promise
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/promise/try
```
[*Examples*](https://goo.gl/k5GGRo):
```js
Promise.try(() => 42).then(it => console.log(`Promise, resolved as ${it}`));

Promise.try(() => { throw 42; }).catch(it => console.log(`Promise, rejected as ${it}`));
```
* `Array#flatten` and `Array#flatMap` [proposal](https://tc39.github.io/proposal-flatMap) - modules [`es7.array.flatten`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.array.flatten.js) and [`es7.array.flat-map`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.array.flat-map.js)
```js
Array
  #flatten(depthArg = 1) -> array
  #flatMap(fn(val, key, @), that) -> array
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/array/flatten
core-js(/library)/fn/array/flat-map
core-js(/library)/fn/array/virtual/flatten
core-js(/library)/fn/array/virtual/flat-map
```
[*Examples*](https://goo.gl/jTXsZi):
```js
[1, [2, 3], [4, 5]].flatten();    // => [1, 2, 3, 4, 5]
[1, [2, [3, [4]]], 5].flatten();  // => [1, 2, [3, [4]], 5]
[1, [2, [3, [4]]], 5].flatten(3); // => [1, 2, 3, 4, 5]

[{a: 1, b: 2}, {a: 3, b: 4}, {a: 5, b: 6}].flatMap(it => [it.a, it.b]); // => [1, 2, 3, 4, 5, 6]
```
* `.of` and `.from` methods on collection constructors [proposal](https://github.com/tc39/proposal-setmap-offrom) - modules [`es7.set.of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.set.of.js), [`es7.set.from`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.set.from.js), [`es7.map.of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.map.of.js), [`es7.map.from`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.map.from.js), [`es7.weak-set.of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.weak-set.of.js), [`es7.weak-set.from`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.weak-set.from.js), [`es7.weak-map.of`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.weak-map.of.js), [`es7.weak-map.from`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.weak-map.from.js)
```js
Set
  .of(...args) -> set
  .from(iterable, mapFn(val, index)?, that?) -> set
Map
  .of(...args) -> map
  .from(iterable, mapFn(val, index)?, that?) -> map
WeakSet
  .of(...args) -> weakset
  .from(iterable, mapFn(val, index)?, that?) -> weakset
WeakMap
  .of(...args) -> weakmap
  .from(iterable, mapFn(val, index)?, that?) -> weakmap
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/set/of
core-js(/library)/fn/set/from
core-js(/library)/fn/map/of
core-js(/library)/fn/map/from
core-js(/library)/fn/weak-set/of
core-js(/library)/fn/weak-set/from
core-js(/library)/fn/weak-map/of
core-js(/library)/fn/weak-map/from
```
[*Examples*](https://goo.gl/mSC7eU):
```js
Set.of(1, 2, 3, 2, 1); // => Set {1, 2, 3}

Map.from([[1, 2], [3, 4]], ([key, val]) => [key ** 2, val ** 2]); // => Map {1: 4, 9: 16}
```
* `String#matchAll` [proposal](https://github.com/tc39/String.prototype.matchAll) - module [`es7.string.match-all`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.string.match-all.js)
```js
String
  #matchAll(regexp) -> iterator
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/string/match-all
core-js(/library)/fn/string/virtual/match-all
```
[*Examples*](http://goo.gl/6kp9EB):
```js
for(let [_, d, D] of '1111a2b3cccc'.matchAll(/(\d)(\D)/)){
  console.log(d, D); // => 1 a, 2 b, 3 c
}
```
* `Observable` [proposal](https://github.com/zenparsing/es-observable) - modules [`es7.observable`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.observable.js) and [`es7.symbol.observable`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.symbol.observable.js)
```js
new Observable(fn)             -> observable
  #subscribe(observer)         -> subscription
  #forEach(fn)                 -> promise
  #@@observable()              -> @
  .of(...items)                -> observable
  .from(observable | iterable) -> observable
  .@@species                   -> @
Symbol
  .observable                  -> @@observable
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/observable
core-js(/library)/fn/symbol/observable
```
[*Examples*](http://goo.gl/1LDywi):
```js
new Observable(observer => {
  observer.next('hello');
  observer.next('world');
  observer.complete();
}).forEach(it => console.log(it))
  .then(_ => console.log('!'));
```
* `Math.{clamp, DEG_PER_RAD, degrees, fscale, rad-per-deg, radians, scale}` 
  [proposal](https://github.com/rwaldron/proposal-math-extensions) - modules 
  [`es7.math.clamp`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.clamp.js), 
  [`es7.math.DEG_PER_RAD`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.DEG_PER_RAD.js), 
  [`es7.math.degrees`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.degrees.js),
  [`es7.math.fscale`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.fscale.js), 
  [`es7.math.RAD_PER_DEG`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.RAD_PER_DEG.js), 
  [`es7.math.radians`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.radians.js) and
  [`es7.math.scale`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.scale.js)
```js
Math
  .DEG_PER_RAD -> number
  .RAD_PER_DEG -> number
  .clamp(x, lower, upper) -> number
  .degrees(radians) -> number
  .fscale(x, inLow, inHigh, outLow, outHigh) -> number
  .radians(degrees) -> number
  .scale(x, inLow, inHigh, outLow, outHigh) -> number
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/math/clamp
core-js(/library)/fn/math/deg-per-rad
core-js(/library)/fn/math/degrees
core-js(/library)/fn/math/fscale
core-js(/library)/fn/math/rad-per-deg
core-js(/library)/fn/math/radians
core-js(/library)/fn/math/scale
```
* `Math.signbit` [proposal](http://jfbastien.github.io/papers/Math.signbit.html) - module [`es7.math.signbit`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.signbit.js)
```js
Math
  .signbit(x) -> bool
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/math/signbit
```
[*Examples*](http://es6.zloirock.ru/):
```js
Math.signbit(NaN); // => NaN
Math.signbit(1);   // => true
Math.signbit(-1);  // => false
Math.signbit(0);   // => true
Math.signbit(-0);  // => false
```

#### Stage 0 proposals
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/stage/0
```
* `String#at` [proposal](https://github.com/mathiasbynens/String.prototype.at) - module [`es7.string.at`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.string.at.js)
```js
String
  #at(index) -> string
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/string/at
core-js(/library)/fn/string/virtual/at
```
[*Examples*](http://goo.gl/XluXI8):
```js
'a𠮷b'.at(1);        // => '𠮷'
'a𠮷b'.at(1).length; // => 2
```
* `Map#toJSON`, `Set#toJSON` [proposal](https://github.com/DavidBruant/Map-Set.prototype.toJSON) - modules [`es7.map.to-json`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.map.to-json.js), [`es7.set.to-json`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.set.to-json.js) (rejected and will be removed from `core-js@3`)
```js
Map
  #toJSON() -> array (rejected and will be removed from core-js@3)
Set
  #toJSON() -> array (rejected and will be removed from core-js@3)
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/map
core-js(/library)/fn/set
```
* `Error.isError` [proposal](https://github.com/ljharb/proposal-is-error) - module [`es7.error.is-error`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.error.is-error.js) (withdrawn and will be removed from `core-js@3`)
```js
Error
  .isError(it) -> bool (withdrawn and will be removed from core-js@3)
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/error/is-error
```
* `Math.{iaddh, isubh, imulh, umulh}` [proposal](https://gist.github.com/BrendanEich/4294d5c212a6d2254703) - modules [`es7.math.iaddh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.iaddh.js), [`es7.math.isubh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.isubh.js), [`es7.math.imulh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.imulh.js) and [`es7.math.umulh`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.math.umulh.js)
```js
Math
  .iaddh(lo0, hi0, lo1, hi1) -> int32
  .isubh(lo0, hi0, lo1, hi1) -> int32
  .imulh(a, b) -> int32
  .umulh(a, b) -> uint32
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/math/iaddh
core-js(/library)/fn/math/isubh
core-js(/library)/fn/math/imulh
core-js(/library)/fn/math/umulh
```
* `global.asap`, [TC39 discussion](https://github.com/rwaldron/tc39-notes/blob/master/es6/2014-09/sept-25.md#510-globalasap-for-enqueuing-a-microtask), module [`es7.asap`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.asap.js)
```js
asap(fn) -> void
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/asap
```
[*Examples*](http://goo.gl/tx3SRK):
```js
asap(() => console.log('called as microtask'));
```

#### Pre-stage 0 proposals
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/stage/pre
```
* `Reflect` metadata [proposal](https://github.com/jonathandturner/decorators/blob/master/specs/metadata.md) - modules [`es7.reflect.define-metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.define-metadata.js), [`es7.reflect.delete-metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.delete-metadata.js), [`es7.reflect.get-metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.get-metadata.js), [`es7.reflect.get-metadata-keys`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.get-metadata-keys.js), [`es7.reflect.get-own-metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.get-own-metadata.js), [`es7.reflect.get-own-metadata-keys`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.get-own-metadata-keys.js), [`es7.reflect.has-metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.has-metadata.js), [`es7.reflect.has-own-metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.has-own-metadata.js) and [`es7.reflect.metadata`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/es7.reflect.metadata.js).
```js
Reflect
  .defineMetadata(metadataKey, metadataValue, target, propertyKey?) -> void
  .getMetadata(metadataKey, target, propertyKey?) -> var
  .getOwnMetadata(metadataKey, target, propertyKey?) -> var
  .hasMetadata(metadataKey, target, propertyKey?) -> bool
  .hasOwnMetadata(metadataKey, target, propertyKey?) -> bool
  .deleteMetadata(metadataKey, target, propertyKey?) -> bool
  .getMetadataKeys(target, propertyKey?) -> array
  .getOwnMetadataKeys(target, propertyKey?) -> array
  .metadata(metadataKey, metadataValue) -> decorator(target, targetKey?) -> void
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/reflect/define-metadata
core-js(/library)/fn/reflect/delete-metadata
core-js(/library)/fn/reflect/get-metadata
core-js(/library)/fn/reflect/get-metadata-keys
core-js(/library)/fn/reflect/get-own-metadata
core-js(/library)/fn/reflect/get-own-metadata-keys
core-js(/library)/fn/reflect/has-metadata
core-js(/library)/fn/reflect/has-own-metadata
core-js(/library)/fn/reflect/metadata
```
[*Examples*](http://goo.gl/KCo3PS):
```js
var O = {};
Reflect.defineMetadata('foo', 'bar', O);
Reflect.ownKeys(O);               // => []
Reflect.getOwnMetadataKeys(O);    // => ['foo']
Reflect.getOwnMetadata('foo', O); // => 'bar'
```

### Web standards
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/web
```
#### setTimeout / setInterval
Module [`web.timers`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/web.timers.js). Additional arguments fix for IE9-.
```js
setTimeout(fn(...args), time, ...args) -> id
setInterval(fn(...args), time, ...args) -> id
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/web/timers
core-js(/library)/fn/set-timeout
core-js(/library)/fn/set-interval
```
```js
// Before:
setTimeout(log.bind(null, 42), 1000);
// After:
setTimeout(log, 1000, 42);
```
#### setImmediate
Module [`web.immediate`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/web.immediate.js). [`setImmediate` proposal](https://developer.mozilla.org/en-US/docs/Web/API/Window.setImmediate) polyfill.
```js
setImmediate(fn(...args), ...args) -> id
clearImmediate(id) -> void
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/web/immediate
core-js(/library)/fn/set-immediate
core-js(/library)/fn/clear-immediate
```
[*Examples*](http://goo.gl/6nXGrx):
```js
setImmediate(function(arg1, arg2){
  console.log(arg1, arg2); // => Message will be displayed with minimum delay
}, 'Message will be displayed', 'with minimum delay');

clearImmediate(setImmediate(function(){
  console.log('Message will not be displayed');
}));
```
#### Iterable DOM collections
Some DOM collections should have [iterable interface](https://heycam.github.io/webidl/#idl-iterable) or should be [inherited from `Array`](https://heycam.github.io/webidl/#LegacyArrayClass). That mean they should have `keys`, `values`, `entries` and `@@iterator` methods for iteration. So add them. Module [`web.dom.iterable`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/web.dom.iterable.js):
```js
{
  CSSRuleList,
  CSSStyleDeclaration,
  CSSValueList,
  ClientRectList,
  DOMRectList,
  DOMStringList,
  DOMTokenList,
  DataTransferItemList,
  FileList,
  HTMLAllCollection,
  HTMLCollection,
  HTMLFormElement,
  HTMLSelectElement,
  MediaList,
  MimeTypeArray,
  NamedNodeMap,
  NodeList,
  PaintRequestList,
  Plugin,
  PluginArray,
  SVGLengthList,
  SVGNumberList,
  SVGPathSegList,
  SVGPointList,
  SVGStringList,
  SVGTransformList,
  SourceBufferList,
  StyleSheetList,
  TextTrackCueList,
  TextTrackList,
  TouchList
}
  #@@iterator() -> iterator (values)

{
  DOMTokenList,
  NodeList
}
  #values()  -> iterator
  #keys()    -> iterator
  #entries() -> iterator
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/web/dom-collections
core-js(/library)/fn/dom-collections/iterator
```
[*Examples*](http://goo.gl/lfXVFl):
```js
for(var {id} of document.querySelectorAll('*')){
  if(id)console.log(id);
}

for(var [index, {id}] of document.querySelectorAll('*').entries()){
  if(id)console.log(index, id);
}
```
### Non-standard
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/core
```
#### Object
Modules [`core.object.is-object`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.object.is-object.js), [`core.object.classof`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.object.classof.js), [`core.object.define`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.object.define.js), [`core.object.make`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.object.make.js).
```js
Object
  .isObject(var) -> bool
  .classof(var) -> string
  .define(target, mixin) -> target
  .make(proto | null, mixin?) -> object
```

[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/core/object
core-js(/library)/fn/object/is-object
core-js(/library)/fn/object/define
core-js(/library)/fn/object/make
```
Object classify [*examples*](http://goo.gl/YZQmGo):
```js
Object.isObject({});    // => true
Object.isObject(isNaN); // => true
Object.isObject(null);  // => false

var classof = Object.classof;

classof(null);                 // => 'Null'
classof(undefined);            // => 'Undefined'
classof(1);                    // => 'Number'
classof(true);                 // => 'Boolean'
classof('string');             // => 'String'
classof(Symbol());             // => 'Symbol'

classof(new Number(1));        // => 'Number'
classof(new Boolean(true));    // => 'Boolean'
classof(new String('string')); // => 'String'

var fn   = function(){}
  , list = (function(){return arguments})(1, 2, 3);

classof({});                   // => 'Object'
classof(fn);                   // => 'Function'
classof([]);                   // => 'Array'
classof(list);                 // => 'Arguments'
classof(/./);                  // => 'RegExp'
classof(new TypeError);        // => 'Error'

classof(new Set);              // => 'Set'
classof(new Map);              // => 'Map'
classof(new WeakSet);          // => 'WeakSet'
classof(new WeakMap);          // => 'WeakMap'
classof(new Promise(fn));      // => 'Promise'

classof([].values());          // => 'Array Iterator'
classof(new Set().values());   // => 'Set Iterator'
classof(new Map().values());   // => 'Map Iterator'

classof(Math);                 // => 'Math'
classof(JSON);                 // => 'JSON'

function Example(){}
Example.prototype[Symbol.toStringTag] = 'Example';

classof(new Example);          // => 'Example'
```
`Object.define` and `Object.make` [*examples*](http://goo.gl/rtpD5Z):
```js
// Before:
Object.defineProperty(target, 'c', {
  enumerable: true,
  configurable: true,
  get: function(){
    return this.a + this.b;
  }
});

// After:
Object.define(target, {
  get c(){
    return this.a + this.b;
  }
});

// Shallow object cloning with prototype and descriptors:
var copy = Object.make(Object.getPrototypeOf(src), src);

// Simple inheritance:
function Vector2D(x, y){
  this.x = x;
  this.y = y;
}
Object.define(Vector2D.prototype, {
  get xy(){
    return Math.hypot(this.x, this.y);
  }
});
function Vector3D(x, y, z){
  Vector2D.apply(this, arguments);
  this.z = z;
}
Vector3D.prototype = Object.make(Vector2D.prototype, {
  constructor: Vector3D,
  get xyz(){
    return Math.hypot(this.x, this.y, this.z);
  }
});

var vector = new Vector3D(9, 12, 20);
console.log(vector.xy);  // => 15
console.log(vector.xyz); // => 25
vector.y++;
console.log(vector.xy);  // => 15.811388300841896
console.log(vector.xyz); // => 25.495097567963924
```
#### Dict
Module [`core.dict`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.dict.js). Based on [TC39 discuss](https://github.com/rwaldron/tc39-notes/blob/master/es6/2012-11/nov-29.md#collection-apis-review) / [strawman](http://wiki.ecmascript.org/doku.php?id=harmony:modules_standard#dictionaries).
```js
[new] Dict(iterable (entries) | object ?) -> dict
  .isDict(var) -> bool
  .values(object) -> iterator
  .keys(object) -> iterator
  .entries(object) -> iterator (entries)
  .has(object, key) -> bool
  .get(object, key) -> val
  .set(object, key, value) -> object
  .forEach(object, fn(val, key, @), that) -> void
  .map(object, fn(val, key, @), that) -> new @
  .mapPairs(object, fn(val, key, @), that) -> new @
  .filter(object, fn(val, key, @), that) -> new @
  .some(object, fn(val, key, @), that) -> bool
  .every(object, fn(val, key, @), that) -> bool
  .find(object, fn(val, key, @), that) -> val
  .findKey(object, fn(val, key, @), that) -> key
  .keyOf(object, var) -> key
  .includes(object, var) -> bool
  .reduce(object, fn(memo, val, key, @), memo?) -> var
```

[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/core/dict
core-js(/library)/fn/dict
```
`Dict` create object without prototype from iterable or simple object.

[*Examples*](http://goo.gl/pnp8Vr):
```js
var map = new Map([['a', 1], ['b', 2], ['c', 3]]);

Dict();                    // => {__proto__: null}
Dict({a: 1, b: 2, c: 3});  // => {__proto__: null, a: 1, b: 2, c: 3}
Dict(map);                 // => {__proto__: null, a: 1, b: 2, c: 3}
Dict([1, 2, 3].entries()); // => {__proto__: null, 0: 1, 1: 2, 2: 3}

var dict = Dict({a: 42});
dict instanceof Object;   // => false
dict.a;                   // => 42
dict.toString;            // => undefined
'a' in dict;              // => true
'hasOwnProperty' in dict; // => false

Dict.isDict({});     // => false
Dict.isDict(Dict()); // => true
```
`Dict.keys`, `Dict.values` and `Dict.entries` returns iterators for objects.

[*Examples*](http://goo.gl/xAvECH):
```js
var dict = {a: 1, b: 2, c: 3};

for(var key of Dict.keys(dict))console.log(key); // => 'a', 'b', 'c'

for(var val of Dict.values(dict))console.log(val); // => 1, 2, 3

for(var [key, val] of Dict.entries(dict)){
  console.log(key); // => 'a', 'b', 'c'
  console.log(val); // => 1, 2, 3
}

new Map(Dict.entries(dict)); // => Map {a: 1, b: 2, c: 3}
```
Basic dict operations for objects with prototype [*examples*](http://goo.gl/B28UnG):
```js
'q' in {q: 1};            // => true
'toString' in {};         // => true

Dict.has({q: 1}, 'q');    // => true
Dict.has({}, 'toString'); // => false

({q: 1})['q'];            // => 1
({}).toString;            // => function toString(){ [native code] }

Dict.get({q: 1}, 'q');    // => 1
Dict.get({}, 'toString'); // => undefined

var O = {};
O['q'] = 1;
O['q'];         // => 1
O['__proto__'] = {w: 2};
O['__proto__']; // => {w: 2}
O['w'];         // => 2

var O = {};
Dict.set(O, 'q', 1);
O['q'];         // => 1
Dict.set(O, '__proto__', {w: 2});
O['__proto__']; // => {w: 2}
O['w'];         // => undefined
```
Other methods of `Dict` module are static equivalents of `Array.prototype` methods for dictionaries.

[*Examples*](http://goo.gl/xFi1RH):
```js
var dict = {a: 1, b: 2, c: 3};

Dict.forEach(dict, console.log, console);
// => 1, 'a', {a: 1, b: 2, c: 3}
// => 2, 'b', {a: 1, b: 2, c: 3}
// => 3, 'c', {a: 1, b: 2, c: 3}

Dict.map(dict, function(it){
  return it * it;
}); // => {a: 1, b: 4, c: 9}

Dict.mapPairs(dict, function(val, key){
  if(key != 'b')return [key + key, val * val];
}); // => {aa: 1, cc: 9}

Dict.filter(dict, function(it){
  return it % 2;
}); // => {a: 1, c: 3}

Dict.some(dict, function(it){
  return it === 2;
}); // => true

Dict.every(dict, function(it){
  return it === 2;
}); // => false

Dict.find(dict, function(it){
  return it > 2;
}); // => 3
Dict.find(dict, function(it){
  return it > 4;
}); // => undefined

Dict.findKey(dict, function(it){
  return it > 2;
}); // => 'c'
Dict.findKey(dict, function(it){
  return it > 4;
}); // => undefined

Dict.keyOf(dict, 2);    // => 'b'
Dict.keyOf(dict, 4);    // => undefined

Dict.includes(dict, 2); // => true
Dict.includes(dict, 4); // => false

Dict.reduce(dict, function(memo, it){
  return memo + it;
});     // => 6
Dict.reduce(dict, function(memo, it){
  return memo + it;
}, ''); // => '123'
```
#### Partial application
Module [`core.function.part`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.function.part.js).
```js
Function
  #part(...args | _) -> fn(...args)
```

[*CommonJS entry points:*](#commonjs)
```js
core-js/core/function
core-js(/library)/fn/function/part
core-js(/library)/fn/function/virtual/part
core-js(/library)/fn/_
```
`Function#part` partial apply function without `this` binding. Uses global variable `_` (`core._` for builds without global namespace pollution) as placeholder and not conflict with `Underscore` / `LoDash`.

[*Examples*](http://goo.gl/p9ZJ8K):
```js
var fn1 = log.part(1, 2);
fn1(3, 4);    // => 1, 2, 3, 4

var fn2 = log.part(_, 2, _, 4);
fn2(1, 3);    // => 1, 2, 3, 4

var fn3 = log.part(1, _, _, 4);
fn3(2, 3);    // => 1, 2, 3, 4

fn2(1, 3, 5); // => 1, 2, 3, 4, 5
fn2(1);       // => 1, 2, undefined, 4
```
#### Number Iterator
Module [`core.number.iterator`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.number.iterator.js).
```js
Number
  #@@iterator() -> iterator
```

[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/core/number
core-js(/library)/fn/number/iterator
core-js(/library)/fn/number/virtual/iterator
```
[*Examples*](http://goo.gl/o45pCN):
```js
for(var i of 3)console.log(i); // => 0, 1, 2

[...10]; // => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Array.from(10, Math.random); // => [0.9817775336559862, 0.02720663254149258, ...]

Array.from(10, function(it){
  return this + it * it;
}, .42); // => [0.42, 1.42, 4.42, 9.42, 16.42, 25.42, 36.42, 49.42, 64.42, 81.42]
```
#### Escaping strings
Modules [`core.regexp.escape`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.regexp.escape.js), [`core.string.escape-html`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.string.escape-html.js) and [`core.string.unescape-html`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.string.unescape-html.js).
```js
RegExp
  .escape(str) -> str
String
  #escapeHTML() -> str
  #unescapeHTML() -> str
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/core/regexp
core-js(/library)/core/string
core-js(/library)/fn/regexp/escape
core-js(/library)/fn/string/escape-html
core-js(/library)/fn/string/unescape-html
core-js(/library)/fn/string/virtual/escape-html
core-js(/library)/fn/string/virtual/unescape-html
```
[*Examples*](http://goo.gl/6bOvsQ):
```js
RegExp.escape('Hello, []{}()*+?.\\^$|!'); // => 'Hello, \[\]\{\}\(\)\*\+\?\.\\\^\$\|!'

'<script>doSomething();</script>'.escapeHTML(); // => '&lt;script&gt;doSomething();&lt;/script&gt;'
'&lt;script&gt;doSomething();&lt;/script&gt;'.unescapeHTML(); // => '<script>doSomething();</script>'
```
#### delay
Module [`core.delay`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.delay.js). [Promise](#ecmascript-6-promise)-returning delay function, [esdiscuss](https://esdiscuss.org/topic/promise-returning-delay-function).
```js
delay(ms) -> promise
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/core/delay
core-js(/library)/fn/delay
```
[*Examples*](http://goo.gl/lbucba):
```js
delay(1e3).then(() => console.log('after 1 sec'));

(async () => {
  await delay(3e3);
  console.log('after 3 sec');

  while(await delay(3e3))console.log('each 3 sec');
})();
```
#### Helpers for iterators
Modules [`core.is-iterable`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.is-iterable.js), [`core.get-iterator`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.get-iterator.js), [`core.get-iterator-method`](https://github.com/zloirock/core-js/blob/v2.5.7/modules/core.get-iterator-method.js) - helpers for check iterability / get iterator in the `library` version or, for example, for `arguments` object:
```js
core
  .isIterable(var) -> bool
  .getIterator(iterable) -> iterator
  .getIteratorMethod(var) -> function | undefined
```
[*CommonJS entry points:*](#commonjs)
```js
core-js(/library)/fn/is-iterable
core-js(/library)/fn/get-iterator
core-js(/library)/fn/get-iterator-method
```
[*Examples*](http://goo.gl/SXsM6D):
```js
var list = (function(){
  return arguments;
})(1, 2, 3);

console.log(core.isIterable(list)); // true;

var iter = core.getIterator(list);
console.log(iter.next().value); // 1
console.log(iter.next().value); // 2
console.log(iter.next().value); // 3
console.log(iter.next().value); // undefined

core.getIterator({});   // TypeError: [object Object] is not iterable!

var iterFn = core.getIteratorMethod(list);
console.log(typeof iterFn);     // 'function'
var iter = iterFn.call(list);
console.log(iter.next().value); // 1
console.log(iter.next().value); // 2
console.log(iter.next().value); // 3
console.log(iter.next().value); // undefined

console.log(core.getIteratorMethod({})); // undefined
```

## Missing polyfills
- ES5 `JSON` is missing now only in IE7- and never will it be added to `core-js`, if you need it in these old browsers, many implementations are available, for example, [json3](https://github.com/bestiejs/json3).
- ES6 `String#normalize` is not a very useful feature, but this polyfill will be very large. If you need it, you can use [unorm](https://github.com/walling/unorm/).
- ES6 `Proxy` can't be polyfilled, but for Node.js / Chromium with additional flags you can try [harmony-reflect](https://github.com/tvcutsem/harmony-reflect) for adapt old style `Proxy` API to final ES6 version.
- ES6 logic for `@@isConcatSpreadable` and `@@species` (in most places) can be polyfilled without problems, but it will cause a serious slowdown in popular cases in some engines. It will be polyfilled when it will be implemented in modern engines.
- ES7 `SIMD`. `core-js` doesn't add polyfill of this feature because of large size and some other reasons. You can use [this polyfill](https://github.com/tc39/ecmascript_simd/blob/master/src/ecmascript_simd.js).
- `window.fetch` is not a cross-platform feature, in some environments it makes no sense. For this reason, I don't think it should be in `core-js`. Looking at a large number of requests it *may be*  added in the future. Now you can use, for example, [this polyfill](https://github.com/github/fetch).
- ECMA-402 `Intl` is missed because of size. You can use [this polyfill](https://github.com/andyearnshaw/Intl.js/).
Ramda
=============

A practical functional library for JavaScript programmers.

[![Build Status](https://travis-ci.org/ramda/ramda.svg?branch=master)](https://travis-ci.org/ramda/ramda)
[![npm module](https://badge.fury.io/js/ramda.svg)](https://www.npmjs.org/package/ramda)
[![dependencies](https://david-dm.org/ramda/ramda.svg)](https://david-dm.org/ramda/ramda)
[![Gitter](https://badges.gitter.im/Join_Chat.svg)](https://gitter.im/ramda/ramda?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


Why Ramda?
----------

<img src="http://ramda.jcphillipps.com/logo/ramdaFilled_200x235.png" 
     width="170" height="190" align="right" hspace="12" />

There are already several excellent libraries with a functional flavor. Typically, they are meant to be general-purpose toolkits, suitable for working in multiple paradigms. Ramda has a more focused goal. We wanted a library designed specifically for a functional programming style, one that makes it easy to create functional pipelines, one that never mutates user data. 


What's Different?
-----------------

The primary distinguishing features of Ramda are:

* Ramda emphasizes a purer functional style. Immutability and side-effect free functions 
  are at the heart of its design philosophy. This can help you get the job done with simple, 
  elegant code.

* Ramda functions are automatically curried. This allows you to easily build up new functions 
  from old ones simply by not supplying the final parameters.

* The parameters to Ramda functions are arranged to make it convenient for currying. The data 
  to be operated on is generally supplied last.

The last two points together make it very easy to build functions as sequences of simpler functions, each of which transforms the data and passes it along to the next. Ramda is designed to support this style of coding.


Introductions
-------------

* [Introducing Ramda](http://buzzdecafe.github.io/code/2014/05/16/introducing-ramda) by Buzz de Cafe
* [Why Ramda?](http://fr.umio.us/why-ramda/) by Scott Sauyet
* [Favoring Curry](http://fr.umio.us/favoring-curry/) by Scott Sauyet
* [Why Curry Helps](https://hughfdjackson.com/javascript/why-curry-helps/) by Hugh Jackson
* [Hey Underscore, You're Doing It Wrong!](https://www.youtube.com/watch?v=m3svKOdZijA&app=desktop) by Brian Lonsdorf
* [Thinking in Ramda](http://randycoulman.com/blog/categories/thinking-in-ramda) by Randy Coulman


Philosophy
----------
Using Ramda should feel much like just using JavaScript.
It is practical, functional JavaScript. We're not introducing
lambda expressions in strings, we're not borrowing consed 
lists, we're not porting over all of the Clojure functions.

Our basic data structures are plain JavaScript objects, and our
usual collections are JavaScript arrays. We also keep other
native features of JavaScript, such as functions as objects
with properties.

Functional programming is in good part about immutable objects and 
side-effect free functions. While Ramda does not *enforce* this, it
enables such style to be as frictionless as possible.

We aim for an implementation both clean and elegant, but the API is king.
We sacrifice a great deal of implementation elegance for even a slightly
cleaner API.

Last but not least, Ramda strives for performance. A reliable and quick
implementation wins over any notions of functional purity.

Installation
------------

To use with node:

```bash
$ npm install ramda
```

Then in the console:

```javascript
const R = require('ramda');
```

To use directly in the browser:

```html
<script src="path/to/yourCopyOf/ramda.js"></script>
```

or the minified version:

```html
<script src="path/to/yourCopyOf/ramda.min.js"></script>
```

or from a CDN, either cdnjs:

```html
<script src="//cdnjs.cloudflare.com/ajax/libs/ramda/0.24.1/ramda.min.js"></script>
```

or one of the below links from [jsDelivr](http://jsdelivr.com):

```html
<script src="//cdn.jsdelivr.net/ramda/0.24.1/ramda.min.js"></script>
<script src="//cdn.jsdelivr.net/ramda/0.24/ramda.min.js"></script>
<script src="//cdn.jsdelivr.net/ramda/latest/ramda.min.js"></script>
```

(note that using `latest` is taking a significant risk that ramda API changes could break your code.)

These script tags add the variable `R` on the browser's global scope.

Or you can inject ramda into virtually any unsuspecting website using [the bookmarklet](https://github.com/ramda/ramda/blob/master/BOOKMARKLET.md).

### Build

* on Unix-based platforms, `npm run build` updates __dist/ramda.js__ and __dist/ramda.min.js__
* on Windows, write the output of `scripts/build --complete` to a temporary file, then rename the temporary file __dist/ramda.js__.

#### Partial Builds

It is possible to build Ramda with a subset of the functionality to reduce its file size. Ramda's build system supports this with command line flags. For example if you're using `R.compose`, `R.reduce`, and `R.filter` you can create a partial build with:

    ./scripts/build -- src/compose.js src/reduce.js src/filter.js > dist/ramda.custom.js

This requires having Node/io.js installed. 

Documentation
-------------

Please review the [API documentation](http://ramdajs.com/docs/).

The Name
--------

Ok, so we like sheep.  That's all.  It's a short name, not already 
taken.  It could as easily have been `eweda`, but then we would be 
forced to say _eweda lamb!_, and no one wants that.  For non-English 
speakers, lambs are baby sheep, ewes are female sheep, and rams are male 
sheep.  So perhaps ramda is a grown-up lambda... but probably not.




Running The Test Suite
----------------------

**Console:**

To run the test suite from the console, you need to have `mocha` installed:

    npm install -g mocha

Then from the root of the project, you can just call

    mocha

Alternately, if you've installed the dependencies, via:

    npm install

then you can run the tests (and get detailed output) by running:

    npm test

**Browser:**

You can use [testem](https://github.com/airportyh/testem) to
test across different browsers (or even headlessly), with livereloading of
tests. Install testem (`npm install -g testem`) and run `testem`. Open the
link provided in your browser and you will see the results in your terminal.

If you have _PhantomJS_ installed, you can run `testem -l phantomjs` to run the
tests completely headlessly.


Translations
-----------------

[Chinese(中文)](http://ramda.cn/)


Acknowledgements
-----------------

Thanks to [J. C. Phillipps](http://www.jcphillipps.com) for the Ramda logo.
Ramda logo artwork &copy; 2014 J. C. Phillipps. Licensed Creative Commons 
[CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/).
# brace-expansion

[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), 
as known from sh/bash, in JavaScript.

[![build status](https://secure.travis-ci.org/juliangruber/brace-expansion.svg)](http://travis-ci.org/juliangruber/brace-expansion)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)
[![Greenkeeper badge](https://badges.greenkeeper.io/juliangruber/brace-expansion.svg)](https://greenkeeper.io/)

[![testling badge](https://ci.testling.com/juliangruber/brace-expansion.png)](https://ci.testling.com/juliangruber/brace-expansion)

## Example

```js
var expand = require('brace-expansion');

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API

```js
var expand = require('brace-expansion');
```

### var expanded = expand(str)

Return an array of all possible and valid expansions of `str`. If none are
found, `[str]` is returned.

Valid expansions are:

```js
/^(.*,)+(.+)?$/
// {a,b,...}
```

A comma separated list of options, like `{a,b}` or `{a,{b,c}}` or `{,a,}`.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.

```js
/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```

An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.

For compatibility reasons, the string `${` is not eligible for brace expansion.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install brace-expansion
```

## Contributors

- [Julian Gruber](https://github.com/juliangruber)
- [Isaac Z. Schlueter](https://github.com/isaacs)

## Sponsors

This module is proudly supported by my [Sponsors](https://github.com/juliangruber/sponsors)!

Do you want to support modules like this to improve their quality, stability and weigh in on new features? Then please consider donating to my [Patreon](https://www.patreon.com/juliangruber). Not sure how much of my modules you're using? Try [feross/thanks](https://github.com/feross/thanks)!

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
An ini format parser and serializer for node.

Sections are treated as nested objects.  Items before the first
heading are saved on the object directly.

## Usage

Consider an ini-file `config.ini` that looks like this:

    ; this comment is being ignored
    scope = global

    [database]
    user = dbuser
    password = dbpassword
    database = use_this_database

    [paths.default]
    datadir = /var/lib/data
    array[] = first value
    array[] = second value
    array[] = third value

You can read, manipulate and write the ini-file like so:

    var fs = require('fs')
      , ini = require('ini')

    var config = ini.parse(fs.readFileSync('./config.ini', 'utf-8'))

    config.scope = 'local'
    config.database.database = 'use_another_database'
    config.paths.default.tmpdir = '/tmp'
    delete config.paths.default.datadir
    config.paths.default.array.push('fourth value')

    fs.writeFileSync('./config_modified.ini', ini.stringify(config, { section: 'section' }))

This will result in a file called `config_modified.ini` being written
to the filesystem with the following content:

    [section]
    scope=local
    [section.database]
    user=dbuser
    password=dbpassword
    database=use_another_database
    [section.paths.default]
    tmpdir=/tmp
    array[]=first value
    array[]=second value
    array[]=third value
    array[]=fourth value


## API

### decode(inistring)

Decode the ini-style formatted `inistring` into a nested object.

### parse(inistring)

Alias for `decode(inistring)`

### encode(object, [options])

Encode the object `object` into an ini-style formatted string. If the
optional parameter `section` is given, then all top-level properties
of the object are put into this section and the `section`-string is
prepended to all sub-sections, see the usage example above.

The `options` object may contain the following:

* `section` A string which will be the first `section` in the encoded
  ini data.  Defaults to none.
* `whitespace` Boolean to specify whether to put whitespace around the
  `=` character.  By default, whitespace is omitted, to be friendly to
  some persnickety old parsers that don't tolerate it well.  But some
  find that it's more human-readable and pretty with the whitespace.

For backwards compatibility reasons, if a `string` options is passed
in, then it is assumed to be the `section` value.

### stringify(object, [options])

Alias for `encode(object, [options])`

### safe(val)

Escapes the string `val` such that it is safe to be used as a key or
value in an ini-file. Basically escapes quotes. For example

    ini.safe('"unsafe string"')

would result in

    "\"unsafe string\""

### unsafe(val)

Unescapes the string `val`
# cross-spawn

[![NPM version][npm-image]][npm-url] [![Downloads][downloads-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Build status][appveyor-image]][appveyor-url] [![Coverage Status][codecov-image]][codecov-url] [![Dependency status][david-dm-image]][david-dm-url] [![Dev Dependency status][david-dm-dev-image]][david-dm-dev-url] [![Greenkeeper badge][greenkeeper-image]][greenkeeper-url]

[npm-url]:https://npmjs.org/package/cross-spawn
[downloads-image]:http://img.shields.io/npm/dm/cross-spawn.svg
[npm-image]:http://img.shields.io/npm/v/cross-spawn.svg
[travis-url]:https://travis-ci.org/moxystudio/node-cross-spawn
[travis-image]:http://img.shields.io/travis/moxystudio/node-cross-spawn/master.svg
[appveyor-url]:https://ci.appveyor.com/project/satazor/node-cross-spawn
[appveyor-image]:https://img.shields.io/appveyor/ci/satazor/node-cross-spawn/master.svg
[codecov-url]:https://codecov.io/gh/moxystudio/node-cross-spawn
[codecov-image]:https://img.shields.io/codecov/c/github/moxystudio/node-cross-spawn/master.svg
[david-dm-url]:https://david-dm.org/moxystudio/node-cross-spawn
[david-dm-image]:https://img.shields.io/david/moxystudio/node-cross-spawn.svg
[david-dm-dev-url]:https://david-dm.org/moxystudio/node-cross-spawn?type=dev
[david-dm-dev-image]:https://img.shields.io/david/dev/moxystudio/node-cross-spawn.svg
[greenkeeper-image]:https://badges.greenkeeper.io/moxystudio/node-cross-spawn.svg
[greenkeeper-url]:https://greenkeeper.io/

A cross platform solution to node's spawn and spawnSync.


## Installation

`$ npm install cross-spawn`


## Why

Node has issues when using spawn on Windows:

- It ignores [PATHEXT](https://github.com/joyent/node/issues/2318)
- It does not support [shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix))
- Has problems running commands with [spaces](https://github.com/nodejs/node/issues/7367)
- Has problems running commands with posix relative paths (e.g.: `./my-folder/my-executable`)
- Has an [issue](https://github.com/moxystudio/node-cross-spawn/issues/82) with command shims (files in `node_modules/.bin/`), where arguments with quotes and parenthesis would result in [invalid syntax error](https://github.com/moxystudio/node-cross-spawn/blob/e77b8f22a416db46b6196767bcd35601d7e11d54/test/index.test.js#L149)
- No `options.shell` support on node `<v4.8`

All these issues are handled correctly by `cross-spawn`.
There are some known modules, such as [win-spawn](https://github.com/ForbesLindesay/win-spawn), that try to solve this but they are either broken or provide faulty escaping of shell arguments.


## Usage

Exactly the same way as node's [`spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) or [`spawnSync`](https://nodejs.org/api/child_process.html#child_process_child_process_spawnsync_command_args_options), so it's a drop in replacement.


```js
const spawn = require('cross-spawn');

// Spawn NPM asynchronously
const child = spawn('npm', ['list', '-g', '-depth', '0'], { stdio: 'inherit' });

// Spawn NPM synchronously
const result = spawn.sync('npm', ['list', '-g', '-depth', '0'], { stdio: 'inherit' });
```


## Caveats

### Using `options.shell` as an alternative to `cross-spawn`

Starting from node `v4.8`, `spawn` has a `shell` option that allows you run commands from within a shell. This new option solves
the [PATHEXT](https://github.com/joyent/node/issues/2318) issue but:

- It's not supported in node `<v4.8`
- You must manually escape the command and arguments which is very error prone, specially when passing user input
- There are a lot of other unresolved issues from the [Why](#why) section that you must take into account

If you are using the `shell` option to spawn a command in a cross platform way, consider using `cross-spawn` instead. You have been warned.

### `options.shell` support

While `cross-spawn` adds support for `options.shell` in node `<v4.8`, all of its enhancements are disabled.

This mimics the Node.js behavior. More specifically, the command and its arguments will not be automatically escaped nor shebang support will be offered. This is by design because if you are using `options.shell` you are probably targeting a specific platform anyway and you don't want things to get into your way.

### Shebangs support

While `cross-spawn` handles shebangs on Windows, its support is limited. More specifically, it just supports `#!/usr/bin/env <program>` where `<program>` must not contain any arguments.   
If you would like to have the shebang support improved, feel free to contribute via a pull-request.

Remember to always test your code on Windows!


## Tests

`$ npm test`   
`$ npm test -- --watch` during development

## License

Released under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
# readable-stream

***Node-core v8.11.1 streams for userland*** [![Build Status](https://travis-ci.org/nodejs/readable-stream.svg?branch=master)](https://travis-ci.org/nodejs/readable-stream)


[![NPM](https://nodei.co/npm/readable-stream.png?downloads=true&downloadRank=true)](https://nodei.co/npm/readable-stream/)
[![NPM](https://nodei.co/npm-dl/readable-stream.png?&months=6&height=3)](https://nodei.co/npm/readable-stream/)


[![Sauce Test Status](https://saucelabs.com/browser-matrix/readable-stream.svg)](https://saucelabs.com/u/readable-stream)

```bash
npm install --save readable-stream
```

***Node-core streams for userland***

This package is a mirror of the Streams2 and Streams3 implementations in
Node-core.

Full documentation may be found on the [Node.js website](https://nodejs.org/dist/v8.11.1/docs/api/stream.html).

If you want to guarantee a stable streams base, regardless of what version of
Node you, or the users of your libraries are using, use **readable-stream** *only* and avoid the *"stream"* module in Node-core, for background see [this blogpost](http://r.va.gg/2014/06/why-i-dont-use-nodes-core-stream-module.html).

As of version 2.0.0 **readable-stream** uses semantic versioning.

# Streams Working Group

`readable-stream` is maintained by the Streams Working Group, which
oversees the development and maintenance of the Streams API within
Node.js. The responsibilities of the Streams Working Group include:

* Addressing stream issues on the Node.js issue tracker.
* Authoring and editing stream documentation within the Node.js project.
* Reviewing changes to stream subclasses within the Node.js project.
* Redirecting changes to streams from the Node.js project to this
  project.
* Assisting in the implementation of stream providers within Node.js.
* Recommending versions of `readable-stream` to be included in Node.js.
* Messaging about the future of streams to give the community advance
  notice of changes.

<a name="members"></a>
## Team Members

* **Chris Dickinson** ([@chrisdickinson](https://github.com/chrisdickinson)) &lt;christopher.s.dickinson@gmail.com&gt;
  - Release GPG key: 9554F04D7259F04124DE6B476D5A82AC7E37093B
* **Calvin Metcalf** ([@calvinmetcalf](https://github.com/calvinmetcalf)) &lt;calvin.metcalf@gmail.com&gt;
  - Release GPG key: F3EF5F62A87FC27A22E643F714CE4FF5015AA242
* **Rod Vagg** ([@rvagg](https://github.com/rvagg)) &lt;rod@vagg.org&gt;
  - Release GPG key: DD8F2338BAE7501E3DD5AC78C273792F7D83545D
* **Sam Newman** ([@sonewman](https://github.com/sonewman)) &lt;newmansam@outlook.com&gt;
* **Mathias Buus** ([@mafintosh](https://github.com/mafintosh)) &lt;mathiasbuus@gmail.com&gt;
* **Domenic Denicola** ([@domenic](https://github.com/domenic)) &lt;d@domenic.me&gt;
* **Matteo Collina** ([@mcollina](https://github.com/mcollina)) &lt;matteo.collina@gmail.com&gt;
  - Release GPG key: 3ABC01543F22DD2239285CDD818674489FBC127E
* **Irina Shestak** ([@lrlna](https://github.com/lrlna)) &lt;shestak.irina@gmail.com&gt;
# which

Like the unix `which` utility.

Finds the first instance of a specified executable in the PATH
environment variable.  Does not cache the results, so `hash -r` is not
needed when the PATH changes.

## USAGE

```javascript
var which = require('which')

// async usage
which('node', function (er, resolvedPath) {
  // er is returned if no "node" is found on the PATH
  // if it is found, then the absolute path to the exec is returned
})

// sync usage
// throws if not found
var resolved = which.sync('node')

// if nothrow option is used, returns null if not found
resolved = which.sync('node', {nothrow: true})

// Pass options to override the PATH and PATHEXT environment vars.
which('node', { path: someOtherPath }, function (er, resolved) {
  if (er)
    throw er
  console.log('found at %j', resolved)
})
```

## CLI USAGE

Same as the BSD `which(1)` binary.

```
usage: which [-as] program ...
```

## OPTIONS

You may pass an options object as the second argument.

- `path`: Use instead of the `PATH` environment variable.
- `pathExt`: Use instead of the `PATHEXT` environment variable.
- `all`: Return all matches, instead of just the first one.  Note that
  this means the function returns an array of strings instead of a
  single string.
# json-stringify-safe

Like JSON.stringify, but doesn't throw on circular references.

## Usage

Takes the same arguments as `JSON.stringify`.

```javascript
var stringify = require('json-stringify-safe');
var circularObj = {};
circularObj.circularRef = circularObj;
circularObj.list = [ circularObj, circularObj ];
console.log(stringify(circularObj, null, 2));
```

Output:

```json
{
  "circularRef": "[Circular]",
  "list": [
    "[Circular]",
    "[Circular]"
  ]
}
```

## Details

```
stringify(obj, serializer, indent, decycler)
```

The first three arguments are the same as to JSON.stringify.  The last
is an argument that's only used when the object has been seen already.

The default `decycler` function returns the string `'[Circular]'`.
If, for example, you pass in `function(k,v){}` (return nothing) then it
will prune cycles.  If you pass in `function(k,v){ return {foo: 'bar'}}`,
then cyclical objects will always be represented as `{"foo":"bar"}` in
the result.

```
stringify.getSerialize(serializer, decycler)
```

Returns a serializer that can be used elsewhere.  This is the actual
function that's passed to JSON.stringify.

**Note** that the function returned from `getSerialize` is stateful for now, so
do **not** use it more than once.
# jsbn: javascript big number

[Tom Wu's Original Website](http://www-cs-students.stanford.edu/~tjw/jsbn/)

I felt compelled to put this on github and publish to npm. I haven't tested every other big integer library out there, but the few that I have tested in comparison to this one have not even come close in performance. I am aware of the `bi` module on npm, however it has been modified and I wanted to publish the original without modifications. This is jsbn and jsbn2 from Tom Wu's original website above, with the modular pattern applied to prevent global leaks and to allow for use with node.js on the server side.

## usage

    var BigInteger = require('jsbn');
    
    var a = new BigInteger('91823918239182398123');
    alert(a.bitLength()); // 67


## API

### bi.toString()

returns the base-10 number as a string

### bi.negate()

returns a new BigInteger equal to the negation of `bi`

### bi.abs

returns new BI of absolute value

### bi.compareTo



### bi.bitLength



### bi.mod



### bi.modPowInt



### bi.clone



### bi.intValue



### bi.byteValue



### bi.shortValue



### bi.signum



### bi.toByteArray



### bi.equals



### bi.min



### bi.max



### bi.and



### bi.or



### bi.xor



### bi.andNot



### bi.not



### bi.shiftLeft



### bi.shiftRight



### bi.getLowestSetBit



### bi.bitCount



### bi.testBit



### bi.setBit



### bi.clearBit



### bi.flipBit



### bi.add



### bi.subtract



### bi.multiply



### bi.divide



### bi.remainder



### bi.divideAndRemainder



### bi.modPow



### bi.modInverse



### bi.pow



### bi.gcd



### bi.isProbablePrime


# mime-types

[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][travis-image]][travis-url]
[![Test Coverage][coveralls-image]][coveralls-url]

The ultimate javascript content-type utility.

Similar to [the `mime@1.x` module](https://www.npmjs.com/package/mime), except:

- __No fallbacks.__ Instead of naively returning the first available type,
  `mime-types` simply returns `false`, so do
  `var type = mime.lookup('unrecognized') || 'application/octet-stream'`.
- No `new Mime()` business, so you could do `var lookup = require('mime-types').lookup`.
- No `.define()` functionality
- Bug fixes for `.lookup(path)`

Otherwise, the API is compatible with `mime` 1.x.

## Install

This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):

```sh
$ npm install mime-types
```

## Adding Types

All mime types are based on [mime-db](https://www.npmjs.com/package/mime-db),
so open a PR there if you'd like to add mime types.

## API

```js
var mime = require('mime-types')
```

All functions return `false` if input is invalid or not found.

### mime.lookup(path)

Lookup the content-type associated with a file.

```js
mime.lookup('json')             // 'application/json'
mime.lookup('.md')              // 'text/markdown'
mime.lookup('file.html')        // 'text/html'
mime.lookup('folder/file.js')   // 'application/javascript'
mime.lookup('folder/.htaccess') // false

mime.lookup('cats') // false
```

### mime.contentType(type)

Create a full content-type header given a content-type or extension.

```js
mime.contentType('markdown')  // 'text/x-markdown; charset=utf-8'
mime.contentType('file.json') // 'application/json; charset=utf-8'

// from a full path
mime.contentType(path.extname('/path/to/file.json')) // 'application/json; charset=utf-8'
```

### mime.extension(type)

Get the default extension for a content-type.

```js
mime.extension('application/octet-stream') // 'bin'
```

### mime.charset(type)

Lookup the implied default charset of a content-type.

```js
mime.charset('text/markdown') // 'UTF-8'
```

### var type = mime.types[extension]

A map of content-types by extension.

### [extensions...] = mime.extensions[type]

A map of extensions by content-type.

## License

[MIT](LICENSE)

[npm-image]: https://img.shields.io/npm/v/mime-types.svg
[npm-url]: https://npmjs.org/package/mime-types
[node-version-image]: https://img.shields.io/node/v/mime-types.svg
[node-version-url]: https://nodejs.org/en/download/
[travis-image]: https://img.shields.io/travis/jshttp/mime-types/master.svg
[travis-url]: https://travis-ci.org/jshttp/mime-types
[coveralls-image]: https://img.shields.io/coveralls/jshttp/mime-types/master.svg
[coveralls-url]: https://coveralls.io/r/jshttp/mime-types
[downloads-image]: https://img.shields.io/npm/dm/mime-types.svg
[downloads-url]: https://npmjs.org/package/mime-types
# assert-plus

This library is a super small wrapper over node's assert module that has two
things: (1) the ability to disable assertions with the environment variable
NODE\_NDEBUG, and (2) some API wrappers for argument testing.  Like
`assert.string(myArg, 'myArg')`.  As a simple example, most of my code looks
like this:

```javascript
    var assert = require('assert-plus');

    function fooAccount(options, callback) {
        assert.object(options, 'options');
        assert.number(options.id, 'options.id');
        assert.bool(options.isManager, 'options.isManager');
        assert.string(options.name, 'options.name');
        assert.arrayOfString(options.email, 'options.email');
        assert.func(callback, 'callback');

        // Do stuff
        callback(null, {});
    }
```

# API

All methods that *aren't* part of node's core assert API are simply assumed to
take an argument, and then a string 'name' that's not a message; `AssertionError`
will be thrown if the assertion fails with a message like:

    AssertionError: foo (string) is required
    at test (/home/mark/work/foo/foo.js:3:9)
    at Object.<anonymous> (/home/mark/work/foo/foo.js:15:1)
    at Module._compile (module.js:446:26)
    at Object..js (module.js:464:10)
    at Module.load (module.js:353:31)
    at Function._load (module.js:311:12)
    at Array.0 (module.js:484:10)
    at EventEmitter._tickCallback (node.js:190:38)

from:

```javascript
    function test(foo) {
        assert.string(foo, 'foo');
    }
```

There you go.  You can check that arrays are of a homogeneous type with `Arrayof$Type`:

```javascript
    function test(foo) {
        assert.arrayOfString(foo, 'foo');
    }
```

You can assert IFF an argument is not `undefined` (i.e., an optional arg):

```javascript
    assert.optionalString(foo, 'foo');
```

Lastly, you can opt-out of assertion checking altogether by setting the
environment variable `NODE_NDEBUG=1`.  This is pseudo-useful if you have
lots of assertions, and don't want to pay `typeof ()` taxes to v8 in
production.  Be advised:  The standard functions re-exported from `assert` are
also disabled in assert-plus if NDEBUG is specified.  Using them directly from
the `assert` module avoids this behavior.

The complete list of APIs is:

* assert.array
* assert.bool
* assert.buffer
* assert.func
* assert.number
* assert.finite
* assert.object
* assert.string
* assert.stream
* assert.date
* assert.regexp
* assert.uuid
* assert.arrayOfArray
* assert.arrayOfBool
* assert.arrayOfBuffer
* assert.arrayOfFunc
* assert.arrayOfNumber
* assert.arrayOfFinite
* assert.arrayOfObject
* assert.arrayOfString
* assert.arrayOfStream
* assert.arrayOfDate
* assert.arrayOfRegexp
* assert.arrayOfUuid
* assert.optionalArray
* assert.optionalBool
* assert.optionalBuffer
* assert.optionalFunc
* assert.optionalNumber
* assert.optionalFinite
* assert.optionalObject
* assert.optionalString
* assert.optionalStream
* assert.optionalDate
* assert.optionalRegexp
* assert.optionalUuid
* assert.optionalArrayOfArray
* assert.optionalArrayOfBool
* assert.optionalArrayOfBuffer
* assert.optionalArrayOfFunc
* assert.optionalArrayOfNumber
* assert.optionalArrayOfFinite
* assert.optionalArrayOfObject
* assert.optionalArrayOfString
* assert.optionalArrayOfStream
* assert.optionalArrayOfDate
* assert.optionalArrayOfRegexp
* assert.optionalArrayOfUuid
* assert.AssertionError
* assert.fail
* assert.ok
* assert.equal
* assert.notEqual
* assert.deepEqual
* assert.notDeepEqual
* assert.strictEqual
* assert.notStrictEqual
* assert.throws
* assert.doesNotThrow
* assert.ifError

# Installation

    npm install assert-plus

## License

The MIT License (MIT)
Copyright (c) 2012 Mark Cavage

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Bugs

See <https://github.com/mcavage/node-assert-plus/issues>.
# node-cachedir

Provides a directory where the OS wants you to store cached files.

## Installation

```sh
npm install cachedir
```

## Usage

```javascript
var cachedir = require('cachedir')
var path = cachedir('linusu')

// `path` now contains the path under which you should store cached files
```
ecc-jsbn
========

ECC package based on [jsbn](https://github.com/andyperlitch/jsbn) from [Tom Wu](http://www-cs-students.stanford.edu/~tjw/).

This is a subset of the same interface as the [node compiled module](https://github.com/quartzjer/ecc), but works in the browser too.

Also uses point compression now from [https://github.com/kaielvin](https://github.com/kaielvin/jsbn-ec-point-compression).
tunnel-agent
============

HTTP proxy tunneling agent. Formerly part of mikeal/request, now a standalone module.
Node.js: fs-extra
=================

`fs-extra` adds file system methods that aren't included in the native `fs` module and adds promise support to the `fs` methods. It should be a drop in replacement for `fs`.

[![npm Package](https://img.shields.io/npm/v/fs-extra.svg?style=flat-square)](https://www.npmjs.org/package/fs-extra)
[![build status](https://api.travis-ci.org/jprichardson/node-fs-extra.svg)](http://travis-ci.org/jprichardson/node-fs-extra)
[![windows Build status](https://img.shields.io/appveyor/ci/jprichardson/node-fs-extra/master.svg?label=windows%20build)](https://ci.appveyor.com/project/jprichardson/node-fs-extra/branch/master)
[![downloads per month](http://img.shields.io/npm/dm/fs-extra.svg)](https://www.npmjs.org/package/fs-extra)
[![Coverage Status](https://img.shields.io/coveralls/jprichardson/node-fs-extra.svg)](https://coveralls.io/r/jprichardson/node-fs-extra)

<a href="https://github.com/feross/standard"><img src="https://cdn.rawgit.com/feross/standard/master/sticker.svg" alt="Standard JavaScript" width="100"></a>


Why?
----

I got tired of including `mkdirp`, `rimraf`, and `ncp` in most of my projects.




Installation
------------

    npm install --save fs-extra



Usage
-----

`fs-extra` is a drop in replacement for native `fs`. All methods in `fs` are attached to `fs-extra`. All `fs` methods return promises if the callback isn't passed.

You don't ever need to include the original `fs` module again:

```js
const fs = require('fs') // this is no longer necessary
```

you can now do this:

```js
const fs = require('fs-extra')
```

or if you prefer to make it clear that you're using `fs-extra` and not `fs`, you may want
to name your `fs` variable `fse` like so:

```js
const fse = require('fs-extra')
```

you can also keep both, but it's redundant:

```js
const fs = require('fs')
const fse = require('fs-extra')
```

Sync vs Async
-------------
Most methods are async by default. All async methods will return a promise if the callback isn't passed.

Sync methods on the other hand will throw if an error occurs.

Example:

```js
const fs = require('fs-extra')

// Async with promises:
fs.copy('/tmp/myfile', '/tmp/mynewfile')
  .then(() => console.log('success!'))
  .catch(err => console.error(err))

// Async with callbacks:
fs.copy('/tmp/myfile', '/tmp/mynewfile', err => {
  if (err) return console.error(err)
  console.log('success!')
})

// Sync:
try {
  fs.copySync('/tmp/myfile', '/tmp/mynewfile')
  console.log('success!')
} catch (err) {
  console.error(err)
}
```


Methods
-------

### Async

- [copy](docs/copy.md)
- [emptyDir](docs/emptyDir.md)
- [ensureFile](docs/ensureFile.md)
- [ensureDir](docs/ensureDir.md)
- [ensureLink](docs/ensureLink.md)
- [ensureSymlink](docs/ensureSymlink.md)
- [mkdirs](docs/ensureDir.md)
- [move](docs/move.md)
- [outputFile](docs/outputFile.md)
- [outputJson](docs/outputJson.md)
- [pathExists](docs/pathExists.md)
- [readJson](docs/readJson.md)
- [remove](docs/remove.md)
- [writeJson](docs/writeJson.md)

### Sync

- [copySync](docs/copy-sync.md)
- [emptyDirSync](docs/emptyDir-sync.md)
- [ensureFileSync](docs/ensureFile-sync.md)
- [ensureDirSync](docs/ensureDir-sync.md)
- [ensureLinkSync](docs/ensureLink-sync.md)
- [ensureSymlinkSync](docs/ensureSymlink-sync.md)
- [mkdirsSync](docs/ensureDir-sync.md)
- [moveSync](docs/move-sync.md)
- [outputFileSync](docs/outputFile-sync.md)
- [outputJsonSync](docs/outputJson-sync.md)
- [pathExistsSync](docs/pathExists-sync.md)
- [readJsonSync](docs/readJson-sync.md)
- [removeSync](docs/remove-sync.md)
- [writeJsonSync](docs/writeJson-sync.md)


**NOTE:** You can still use the native Node.js methods. They are promisified and copied over to `fs-extra`. See [notes on `fs.read()` & `fs.write()`](docs/fs-read-write.md)

### What happened to `walk()` and `walkSync()`?

They were removed from `fs-extra` in v2.0.0. If you need the functionality, `walk` and `walkSync` are available as separate packages, [`klaw`](https://github.com/jprichardson/node-klaw) and [`klaw-sync`](https://github.com/manidlou/node-klaw-sync).


Third Party
-----------


### TypeScript

If you like TypeScript, you can use `fs-extra` with it: https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/fs-extra


### File / Directory Watching

If you want to watch for changes to files or directories, then you should use [chokidar](https://github.com/paulmillr/chokidar).


### Misc.

- [mfs](https://github.com/cadorn/mfs) - Monitor your fs-extra calls.



Hacking on fs-extra
-------------------

Wanna hack on `fs-extra`? Great! Your help is needed! [fs-extra is one of the most depended upon Node.js packages](http://nodei.co/npm/fs-extra.png?downloads=true&downloadRank=true&stars=true). This project
uses [JavaScript Standard Style](https://github.com/feross/standard) - if the name or style choices bother you,
you're gonna have to get over it :) If `standard` is good enough for `npm`, it's good enough for `fs-extra`.

[![js-standard-style](https://cdn.rawgit.com/feross/standard/master/badge.svg)](https://github.com/feross/standard)

What's needed?
- First, take a look at existing issues. Those are probably going to be where the priority lies.
- More tests for edge cases. Specifically on different platforms. There can never be enough tests.
- Improve test coverage. See coveralls output for more info.

Note: If you make any big changes, **you should definitely file an issue for discussion first.**

### Running the Test Suite

fs-extra contains hundreds of tests.

- `npm run lint`: runs the linter ([standard](http://standardjs.com/))
- `npm run unit`: runs the unit tests
- `npm test`: runs both the linter and the tests


### Windows

If you run the tests on the Windows and receive a lot of symbolic link `EPERM` permission errors, it's
because on Windows you need elevated privilege to create symbolic links. You can add this to your Windows's
account by following the instructions here: http://superuser.com/questions/104845/permission-to-make-symbolic-links-in-windows-7
However, I didn't have much luck doing this.

Since I develop on Mac OS X, I use VMWare Fusion for Windows testing. I create a shared folder that I map to a drive on Windows.
I open the `Node.js command prompt` and run as `Administrator`. I then map the network drive running the following command:

    net use z: "\\vmware-host\Shared Folders"

I can then navigate to my `fs-extra` directory and run the tests.


Naming
------

I put a lot of thought into the naming of these functions. Inspired by @coolaj86's request. So he deserves much of the credit for raising the issue. See discussion(s) here:

* https://github.com/jprichardson/node-fs-extra/issues/2
* https://github.com/flatiron/utile/issues/11
* https://github.com/ryanmcgrath/wrench-js/issues/29
* https://github.com/substack/node-mkdirp/issues/17

First, I believe that in as many cases as possible, the [Node.js naming schemes](http://nodejs.org/api/fs.html) should be chosen. However, there are problems with the Node.js own naming schemes.

For example, `fs.readFile()` and `fs.readdir()`: the **F** is capitalized in *File* and the **d** is not capitalized in *dir*. Perhaps a bit pedantic, but they should still be consistent. Also, Node.js has chosen a lot of POSIX naming schemes, which I believe is great. See: `fs.mkdir()`, `fs.rmdir()`, `fs.chown()`, etc.

We have a dilemma though. How do you consistently name methods that perform the following POSIX commands: `cp`, `cp -r`, `mkdir -p`, and `rm -rf`?

My perspective: when in doubt, err on the side of simplicity. A directory is just a hierarchical grouping of directories and files. Consider that for a moment. So when you want to copy it or remove it, in most cases you'll want to copy or remove all of its contents. When you want to create a directory, if the directory that it's suppose to be contained in does not exist, then in most cases you'll want to create that too.

So, if you want to remove a file or a directory regardless of whether it has contents, just call `fs.remove(path)`. If you want to copy a file or a directory whether it has contents, just call `fs.copy(source, destination)`. If you want to create a directory regardless of whether its parent directories exist, just call `fs.mkdirs(path)` or `fs.mkdirp(path)`.


Credit
------

`fs-extra` wouldn't be possible without using the modules from the following authors:

- [Isaac Shlueter](https://github.com/isaacs)
- [Charlie McConnel](https://github.com/avianflu)
- [James Halliday](https://github.com/substack)
- [Andrew Kelley](https://github.com/andrewrk)




License
-------

Licensed under MIT

Copyright (c) 2011-2017 [JP Richardson](https://github.com/jprichardson)

[1]: http://nodejs.org/docs/latest/api/fs.html


[jsonfile]: https://github.com/jprichardson/node-jsonfile
[RFC6265](https://tools.ietf.org/html/rfc6265) Cookies and CookieJar for Node.js

[![npm package](https://nodei.co/npm/tough-cookie.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/tough-cookie/)

[![Build Status](https://travis-ci.org/salesforce/tough-cookie.png?branch=master)](https://travis-ci.org/salesforce/tough-cookie)

# Synopsis

``` javascript
var tough = require('tough-cookie');
var Cookie = tough.Cookie;
var cookie = Cookie.parse(header);
cookie.value = 'somethingdifferent';
header = cookie.toString();

var cookiejar = new tough.CookieJar();
cookiejar.setCookie(cookie, 'http://currentdomain.example.com/path', cb);
// ...
cookiejar.getCookies('http://example.com/otherpath',function(err,cookies) {
  res.headers['cookie'] = cookies.join('; ');
});
```

# Installation

It's _so_ easy!

`npm install tough-cookie`

Why the name?  NPM modules `cookie`, `cookies` and `cookiejar` were already taken.

## Version Support

Support for versions of node.js will follow that of the [request](https://www.npmjs.com/package/request) module.

# API

## tough

Functions on the module you get from `require('tough-cookie')`.  All can be used as pure functions and don't need to be "bound".

**Note**: prior to 1.0.x, several of these functions took a `strict` parameter. This has since been removed from the API as it was no longer necessary.

### `parseDate(string)`

Parse a cookie date string into a `Date`.  Parses according to RFC6265 Section 5.1.1, not `Date.parse()`.

### `formatDate(date)`

Format a Date into a RFC1123 string (the RFC6265-recommended format).

### `canonicalDomain(str)`

Transforms a domain-name into a canonical domain-name.  The canonical domain-name is a trimmed, lowercased, stripped-of-leading-dot and optionally punycode-encoded domain-name (Section 5.1.2 of RFC6265).  For the most part, this function is idempotent (can be run again on its output without ill effects).

### `domainMatch(str,domStr[,canonicalize=true])`

Answers "does this real domain match the domain in a cookie?".  The `str` is the "current" domain-name and the `domStr` is the "cookie" domain-name.  Matches according to RFC6265 Section 5.1.3, but it helps to think of it as a "suffix match".

The `canonicalize` parameter will run the other two paramters through `canonicalDomain` or not.

### `defaultPath(path)`

Given a current request/response path, gives the Path apropriate for storing in a cookie.  This is basically the "directory" of a "file" in the path, but is specified by Section 5.1.4 of the RFC.

The `path` parameter MUST be _only_ the pathname part of a URI (i.e. excludes the hostname, query, fragment, etc.).  This is the `.pathname` property of node's `uri.parse()` output.

### `pathMatch(reqPath,cookiePath)`

Answers "does the request-path path-match a given cookie-path?" as per RFC6265 Section 5.1.4.  Returns a boolean.

This is essentially a prefix-match where `cookiePath` is a prefix of `reqPath`.

### `parse(cookieString[, options])`

alias for `Cookie.parse(cookieString[, options])`

### `fromJSON(string)`

alias for `Cookie.fromJSON(string)`

### `getPublicSuffix(hostname)`

Returns the public suffix of this hostname.  The public suffix is the shortest domain-name upon which a cookie can be set.  Returns `null` if the hostname cannot have cookies set for it.

For example: `www.example.com` and `www.subdomain.example.com` both have public suffix `example.com`.

For further information, see http://publicsuffix.org/.  This module derives its list from that site.

### `cookieCompare(a,b)`

For use with `.sort()`, sorts a list of cookies into the recommended order given in the RFC (Section 5.4 step 2). The sort algorithm is, in order of precedence:

* Longest `.path`
* oldest `.creation` (which has a 1ms precision, same as `Date`)
* lowest `.creationIndex` (to get beyond the 1ms precision)

``` javascript
var cookies = [ /* unsorted array of Cookie objects */ ];
cookies = cookies.sort(cookieCompare);
```

**Note**: Since JavaScript's `Date` is limited to a 1ms precision, cookies within the same milisecond are entirely possible. This is especially true when using the `now` option to `.setCookie()`. The `.creationIndex` property is a per-process global counter, assigned during construction with `new Cookie()`. This preserves the spirit of the RFC sorting: older cookies go first. This works great for `MemoryCookieStore`, since `Set-Cookie` headers are parsed in order, but may not be so great for distributed systems. Sophisticated `Store`s may wish to set this to some other _logical clock_ such that if cookies A and B are created in the same millisecond, but cookie A is created before cookie B, then `A.creationIndex < B.creationIndex`. If you want to alter the global counter, which you probably _shouldn't_ do, it's stored in `Cookie.cookiesCreated`.

### `permuteDomain(domain)`

Generates a list of all possible domains that `domainMatch()` the parameter.  May be handy for implementing cookie stores.

### `permutePath(path)`

Generates a list of all possible paths that `pathMatch()` the parameter.  May be handy for implementing cookie stores.


## Cookie

Exported via `tough.Cookie`.

### `Cookie.parse(cookieString[, options])`

Parses a single Cookie or Set-Cookie HTTP header into a `Cookie` object.  Returns `undefined` if the string can't be parsed.

The options parameter is not required and currently has only one property:

  * _loose_ - boolean - if `true` enable parsing of key-less cookies like `=abc` and `=`, which are not RFC-compliant.

If options is not an object, it is ignored, which means you can use `Array#map` with it.

Here's how to process the Set-Cookie header(s) on a node HTTP/HTTPS response:

``` javascript
if (res.headers['set-cookie'] instanceof Array)
  cookies = res.headers['set-cookie'].map(Cookie.parse);
else
  cookies = [Cookie.parse(res.headers['set-cookie'])];
```

_Note:_ in version 2.3.3, tough-cookie limited the number of spaces before the `=` to 256 characters. This limitation has since been removed.
See [Issue 92](https://github.com/salesforce/tough-cookie/issues/92)

### Properties

Cookie object properties:

  * _key_ - string - the name or key of the cookie (default "")
  * _value_ - string - the value of the cookie (default "")
  * _expires_ - `Date` - if set, the `Expires=` attribute of the cookie (defaults to the string `"Infinity"`). See `setExpires()`
  * _maxAge_ - seconds - if set, the `Max-Age=` attribute _in seconds_ of the cookie.  May also be set to strings `"Infinity"` and `"-Infinity"` for non-expiry and immediate-expiry, respectively.  See `setMaxAge()`
  * _domain_ - string - the `Domain=` attribute of the cookie
  * _path_ - string - the `Path=` of the cookie
  * _secure_ - boolean - the `Secure` cookie flag
  * _httpOnly_ - boolean - the `HttpOnly` cookie flag
  * _extensions_ - `Array` - any unrecognized cookie attributes as strings (even if equal-signs inside)
  * _creation_ - `Date` - when this cookie was constructed
  * _creationIndex_ - number - set at construction, used to provide greater sort precision (please see `cookieCompare(a,b)` for a full explanation)

After a cookie has been passed through `CookieJar.setCookie()` it will have the following additional attributes:

  * _hostOnly_ - boolean - is this a host-only cookie (i.e. no Domain field was set, but was instead implied)
  * _pathIsDefault_ - boolean - if true, there was no Path field on the cookie and `defaultPath()` was used to derive one.
  * _creation_ - `Date` - **modified** from construction to when the cookie was added to the jar
  * _lastAccessed_ - `Date` - last time the cookie got accessed. Will affect cookie cleaning once implemented.  Using `cookiejar.getCookies(...)` will update this attribute.

### `Cookie([{properties}])`

Receives an options object that can contain any of the above Cookie properties, uses the default for unspecified properties.

### `.toString()`

encode to a Set-Cookie header value.  The Expires cookie field is set using `formatDate()`, but is omitted entirely if `.expires` is `Infinity`.

### `.cookieString()`

encode to a Cookie header value (i.e. the `.key` and `.value` properties joined with '=').

### `.setExpires(String)`

sets the expiry based on a date-string passed through `parseDate()`.  If parseDate returns `null` (i.e. can't parse this date string), `.expires` is set to `"Infinity"` (a string) is set.

### `.setMaxAge(number)`

sets the maxAge in seconds.  Coerces `-Infinity` to `"-Infinity"` and `Infinity` to `"Infinity"` so it JSON serializes correctly.

### `.expiryTime([now=Date.now()])`

### `.expiryDate([now=Date.now()])`

expiryTime() Computes the absolute unix-epoch milliseconds that this cookie expires. expiryDate() works similarly, except it returns a `Date` object.  Note that in both cases the `now` parameter should be milliseconds.

Max-Age takes precedence over Expires (as per the RFC). The `.creation` attribute -- or, by default, the `now` paramter -- is used to offset the `.maxAge` attribute.

If Expires (`.expires`) is set, that's returned.

Otherwise, `expiryTime()` returns `Infinity` and `expiryDate()` returns a `Date` object for "Tue, 19 Jan 2038 03:14:07 GMT" (latest date that can be expressed by a 32-bit `time_t`; the common limit for most user-agents).

### `.TTL([now=Date.now()])`

compute the TTL relative to `now` (milliseconds).  The same precedence rules as for `expiryTime`/`expiryDate` apply.

The "number" `Infinity` is returned for cookies without an explicit expiry and `0` is returned if the cookie is expired.  Otherwise a time-to-live in milliseconds is returned.

### `.canonicalizedDoman()`

### `.cdomain()`

return the canonicalized `.domain` field.  This is lower-cased and punycode (RFC3490) encoded if the domain has any non-ASCII characters.

### `.toJSON()`

For convenience in using `JSON.serialize(cookie)`. Returns a plain-old `Object` that can be JSON-serialized.

Any `Date` properties (i.e., `.expires`, `.creation`, and `.lastAccessed`) are exported in ISO format (`.toISOString()`).

**NOTE**: Custom `Cookie` properties will be discarded. In tough-cookie 1.x, since there was no `.toJSON` method explicitly defined, all enumerable properties were captured. If you want a property to be serialized, add the property name to the `Cookie.serializableProperties` Array.

### `Cookie.fromJSON(strOrObj)`

Does the reverse of `cookie.toJSON()`. If passed a string, will `JSON.parse()` that first.

Any `Date` properties (i.e., `.expires`, `.creation`, and `.lastAccessed`) are parsed via `Date.parse()`, not the tough-cookie `parseDate`, since it's JavaScript/JSON-y timestamps being handled at this layer.

Returns `null` upon JSON parsing error.

### `.clone()`

Does a deep clone of this cookie, exactly implemented as `Cookie.fromJSON(cookie.toJSON())`.

### `.validate()`

Status: *IN PROGRESS*. Works for a few things, but is by no means comprehensive.

validates cookie attributes for semantic correctness.  Useful for "lint" checking any Set-Cookie headers you generate.  For now, it returns a boolean, but eventually could return a reason string -- you can future-proof with this construct:

``` javascript
if (cookie.validate() === true) {
  // it's tasty
} else {
  // yuck!
}
```


## CookieJar

Exported via `tough.CookieJar`.

### `CookieJar([store],[options])`

Simply use `new CookieJar()`.  If you'd like to use a custom store, pass that to the constructor otherwise a `MemoryCookieStore` will be created and used.

The `options` object can be omitted and can have the following properties:

  * _rejectPublicSuffixes_ - boolean - default `true` - reject cookies with domains like "com" and "co.uk"
  * _looseMode_ - boolean - default `false` - accept malformed cookies like `bar` and `=bar`, which have an implied empty name.
    This is not in the standard, but is used sometimes on the web and is accepted by (most) browsers.

Since eventually this module would like to support database/remote/etc. CookieJars, continuation passing style is used for CookieJar methods.

### `.setCookie(cookieOrString, currentUrl, [{options},] cb(err,cookie))`

Attempt to set the cookie in the cookie jar.  If the operation fails, an error will be given to the callback `cb`, otherwise the cookie is passed through.  The cookie will have updated `.creation`, `.lastAccessed` and `.hostOnly` properties.

The `options` object can be omitted and can have the following properties:

  * _http_ - boolean - default `true` - indicates if this is an HTTP or non-HTTP API.  Affects HttpOnly cookies.
  * _secure_ - boolean - autodetect from url - indicates if this is a "Secure" API.  If the currentUrl starts with `https:` or `wss:` then this is defaulted to `true`, otherwise `false`.
  * _now_ - Date - default `new Date()` - what to use for the creation/access time of cookies
  * _ignoreError_ - boolean - default `false` - silently ignore things like parse errors and invalid domains.  `Store` errors aren't ignored by this option.

As per the RFC, the `.hostOnly` property is set if there was no "Domain=" parameter in the cookie string (or `.domain` was null on the Cookie object).  The `.domain` property is set to the fully-qualified hostname of `currentUrl` in this case.  Matching this cookie requires an exact hostname match (not a `domainMatch` as per usual).

### `.setCookieSync(cookieOrString, currentUrl, [{options}])`

Synchronous version of `setCookie`; only works with synchronous stores (e.g. the default `MemoryCookieStore`).

### `.getCookies(currentUrl, [{options},] cb(err,cookies))`

Retrieve the list of cookies that can be sent in a Cookie header for the current url.

If an error is encountered, that's passed as `err` to the callback, otherwise an `Array` of `Cookie` objects is passed.  The array is sorted with `cookieCompare()` unless the `{sort:false}` option is given.

The `options` object can be omitted and can have the following properties:

  * _http_ - boolean - default `true` - indicates if this is an HTTP or non-HTTP API.  Affects HttpOnly cookies.
  * _secure_ - boolean - autodetect from url - indicates if this is a "Secure" API.  If the currentUrl starts with `https:` or `wss:` then this is defaulted to `true`, otherwise `false`.
  * _now_ - Date - default `new Date()` - what to use for the creation/access time of cookies
  * _expire_ - boolean - default `true` - perform expiry-time checking of cookies and asynchronously remove expired cookies from the store.  Using `false` will return expired cookies and **not** remove them from the store (which is useful for replaying Set-Cookie headers, potentially).
  * _allPaths_ - boolean - default `false` - if `true`, do not scope cookies by path. The default uses RFC-compliant path scoping. **Note**: may not be supported by the underlying store (the default `MemoryCookieStore` supports it).

The `.lastAccessed` property of the returned cookies will have been updated.

### `.getCookiesSync(currentUrl, [{options}])`

Synchronous version of `getCookies`; only works with synchronous stores (e.g. the default `MemoryCookieStore`).

### `.getCookieString(...)`

Accepts the same options as `.getCookies()` but passes a string suitable for a Cookie header rather than an array to the callback.  Simply maps the `Cookie` array via `.cookieString()`.

### `.getCookieStringSync(...)`

Synchronous version of `getCookieString`; only works with synchronous stores (e.g. the default `MemoryCookieStore`).

### `.getSetCookieStrings(...)`

Returns an array of strings suitable for **Set-Cookie** headers. Accepts the same options as `.getCookies()`.  Simply maps the cookie array via `.toString()`.

### `.getSetCookieStringsSync(...)`

Synchronous version of `getSetCookieStrings`; only works with synchronous stores (e.g. the default `MemoryCookieStore`).

### `.serialize(cb(err,serializedObject))`

Serialize the Jar if the underlying store supports `.getAllCookies`.

**NOTE**: Custom `Cookie` properties will be discarded. If you want a property to be serialized, add the property name to the `Cookie.serializableProperties` Array.

See [Serialization Format].

### `.serializeSync()`

Sync version of .serialize

### `.toJSON()`

Alias of .serializeSync() for the convenience of `JSON.stringify(cookiejar)`.

### `CookieJar.deserialize(serialized, [store], cb(err,object))`

A new Jar is created and the serialized Cookies are added to the underlying store. Each `Cookie` is added via `store.putCookie` in the order in which they appear in the serialization.

The `store` argument is optional, but should be an instance of `Store`. By default, a new instance of `MemoryCookieStore` is created.

As a convenience, if `serialized` is a string, it is passed through `JSON.parse` first. If that throws an error, this is passed to the callback.

### `CookieJar.deserializeSync(serialized, [store])`

Sync version of `.deserialize`.  _Note_ that the `store` must be synchronous for this to work.

### `CookieJar.fromJSON(string)`

Alias of `.deserializeSync` to provide consistency with `Cookie.fromJSON()`.

### `.clone([store,]cb(err,newJar))`

Produces a deep clone of this jar. Modifications to the original won't affect the clone, and vice versa.

The `store` argument is optional, but should be an instance of `Store`. By default, a new instance of `MemoryCookieStore` is created. Transferring between store types is supported so long as the source implements `.getAllCookies()` and the destination implements `.putCookie()`.

### `.cloneSync([store])`

Synchronous version of `.clone`, returning a new `CookieJar` instance.

The `store` argument is optional, but must be a _synchronous_ `Store` instance if specified. If not passed, a new instance of `MemoryCookieStore` is used.

The _source_ and _destination_ must both be synchronous `Store`s. If one or both stores are asynchronous, use `.clone` instead. Recall that `MemoryCookieStore` supports both synchronous and asynchronous API calls.

## Store

Base class for CookieJar stores. Available as `tough.Store`.

## Store API

The storage model for each `CookieJar` instance can be replaced with a custom implementation.  The default is `MemoryCookieStore` which can be found in the `lib/memstore.js` file.  The API uses continuation-passing-style to allow for asynchronous stores.

Stores should inherit from the base `Store` class, which is available as `require('tough-cookie').Store`.

Stores are asynchronous by default, but if `store.synchronous` is set to `true`, then the `*Sync` methods on the of the containing `CookieJar` can be used (however, the continuation-passing style

All `domain` parameters will have been normalized before calling.

The Cookie store must have all of the following methods.

### `store.findCookie(domain, path, key, cb(err,cookie))`

Retrieve a cookie with the given domain, path and key (a.k.a. name).  The RFC maintains that exactly one of these cookies should exist in a store.  If the store is using versioning, this means that the latest/newest such cookie should be returned.

Callback takes an error and the resulting `Cookie` object.  If no cookie is found then `null` MUST be passed instead (i.e. not an error).

### `store.findCookies(domain, path, cb(err,cookies))`

Locates cookies matching the given domain and path.  This is most often called in the context of `cookiejar.getCookies()` above.

If no cookies are found, the callback MUST be passed an empty array.

The resulting list will be checked for applicability to the current request according to the RFC (domain-match, path-match, http-only-flag, secure-flag, expiry, etc.), so it's OK to use an optimistic search algorithm when implementing this method.  However, the search algorithm used SHOULD try to find cookies that `domainMatch()` the domain and `pathMatch()` the path in order to limit the amount of checking that needs to be done.

As of version 0.9.12, the `allPaths` option to `cookiejar.getCookies()` above will cause the path here to be `null`.  If the path is `null`, path-matching MUST NOT be performed (i.e. domain-matching only).

### `store.putCookie(cookie, cb(err))`

Adds a new cookie to the store.  The implementation SHOULD replace any existing cookie with the same `.domain`, `.path`, and `.key` properties -- depending on the nature of the implementation, it's possible that between the call to `fetchCookie` and `putCookie` that a duplicate `putCookie` can occur.

The `cookie` object MUST NOT be modified; the caller will have already updated the `.creation` and `.lastAccessed` properties.

Pass an error if the cookie cannot be stored.

### `store.updateCookie(oldCookie, newCookie, cb(err))`

Update an existing cookie.  The implementation MUST update the `.value` for a cookie with the same `domain`, `.path` and `.key`.  The implementation SHOULD check that the old value in the store is equivalent to `oldCookie` - how the conflict is resolved is up to the store.

The `.lastAccessed` property will always be different between the two objects (to the precision possible via JavaScript's clock).  Both `.creation` and `.creationIndex` are guaranteed to be the same.  Stores MAY ignore or defer the `.lastAccessed` change at the cost of affecting how cookies are selected for automatic deletion (e.g., least-recently-used, which is up to the store to implement).

Stores may wish to optimize changing the `.value` of the cookie in the store versus storing a new cookie.  If the implementation doesn't define this method a stub that calls `putCookie(newCookie,cb)` will be added to the store object.

The `newCookie` and `oldCookie` objects MUST NOT be modified.

Pass an error if the newCookie cannot be stored.

### `store.removeCookie(domain, path, key, cb(err))`

Remove a cookie from the store (see notes on `findCookie` about the uniqueness constraint).

The implementation MUST NOT pass an error if the cookie doesn't exist; only pass an error due to the failure to remove an existing cookie.

### `store.removeCookies(domain, path, cb(err))`

Removes matching cookies from the store.  The `path` parameter is optional, and if missing means all paths in a domain should be removed.

Pass an error ONLY if removing any existing cookies failed.

### `store.getAllCookies(cb(err, cookies))`

Produces an `Array` of all cookies during `jar.serialize()`. The items in the array can be true `Cookie` objects or generic `Object`s with the [Serialization Format] data structure.

Cookies SHOULD be returned in creation order to preserve sorting via `compareCookies()`. For reference, `MemoryCookieStore` will sort by `.creationIndex` since it uses true `Cookie` objects internally. If you don't return the cookies in creation order, they'll still be sorted by creation time, but this only has a precision of 1ms.  See `compareCookies` for more detail.

Pass an error if retrieval fails.

## MemoryCookieStore

Inherits from `Store`.

A just-in-memory CookieJar synchronous store implementation, used by default. Despite being a synchronous implementation, it's usable with both the synchronous and asynchronous forms of the `CookieJar` API.

## Community Cookie Stores

These are some Store implementations authored and maintained by the community. They aren't official and we don't vouch for them but you may be interested to have a look:

- [`db-cookie-store`](https://github.com/JSBizon/db-cookie-store): SQL including SQLite-based databases
- [`file-cookie-store`](https://github.com/JSBizon/file-cookie-store): Netscape cookie file format on disk
- [`redis-cookie-store`](https://github.com/benkroeger/redis-cookie-store): Redis
- [`tough-cookie-filestore`](https://github.com/mitsuru/tough-cookie-filestore): JSON on disk
- [`tough-cookie-web-storage-store`](https://github.com/exponentjs/tough-cookie-web-storage-store): DOM localStorage and sessionStorage


# Serialization Format

**NOTE**: if you want to have custom `Cookie` properties serialized, add the property name to `Cookie.serializableProperties`.

```js
  {
    // The version of tough-cookie that serialized this jar.
    version: 'tough-cookie@1.x.y',

    // add the store type, to make humans happy:
    storeType: 'MemoryCookieStore',

    // CookieJar configuration:
    rejectPublicSuffixes: true,
    // ... future items go here

    // Gets filled from jar.store.getAllCookies():
    cookies: [
      {
        key: 'string',
        value: 'string',
        // ...
        /* other Cookie.serializableProperties go here */
      }
    ]
  }
```

# Copyright and License

(tl;dr: BSD-3-Clause with some MPL/2.0)

```text
 Copyright (c) 2015, Salesforce.com, Inc.
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:

 1. Redistributions of source code must retain the above copyright notice,
 this list of conditions and the following disclaimer.

 2. Redistributions in binary form must reproduce the above copyright notice,
 this list of conditions and the following disclaimer in the documentation
 and/or other materials provided with the distribution.

 3. Neither the name of Salesforce.com nor the names of its contributors may
 be used to endorse or promote products derived from this software without
 specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
```

Portions may be licensed under different licenses (in particular `public_suffix_list.dat` is MPL/2.0); please read that file and the LICENSE file for full details.
# verror: rich JavaScript errors

This module provides several classes in support of Joyent's [Best Practices for
Error Handling in Node.js](http://www.joyent.com/developers/node/design/errors).
If you find any of the behavior here confusing or surprising, check out that
document first.

The error classes here support:

* printf-style arguments for the message
* chains of causes
* properties to provide extra information about the error
* creating your own subclasses that support all of these

The classes here are:

* **VError**, for chaining errors while preserving each one's error message.
  This is useful in servers and command-line utilities when you want to
  propagate an error up a call stack, but allow various levels to add their own
  context.  See examples below.
* **WError**, for wrapping errors while hiding the lower-level messages from the
  top-level error.  This is useful for API endpoints where you don't want to
  expose internal error messages, but you still want to preserve the error chain
  for logging and debugging.
* **SError**, which is just like VError but interprets printf-style arguments
  more strictly.
* **MultiError**, which is just an Error that encapsulates one or more other
  errors.  (This is used for parallel operations that return several errors.)


# Quick start

First, install the package:

    npm install verror

If nothing else, you can use VError as a drop-in replacement for the built-in
JavaScript Error class, with the addition of printf-style messages:

```javascript
var err = new VError('missing file: "%s"', '/etc/passwd');
console.log(err.message);
```

This prints:

    missing file: "/etc/passwd"

You can also pass a `cause` argument, which is any other Error object:

```javascript
var fs = require('fs');
var filename = '/nonexistent';
fs.stat(filename, function (err1) {
	var err2 = new VError(err1, 'stat "%s"', filename);
	console.error(err2.message);
});
```

This prints out:

    stat "/nonexistent": ENOENT, stat '/nonexistent'

which resembles how Unix programs typically report errors:

    $ sort /nonexistent
    sort: open failed: /nonexistent: No such file or directory

To match the Unixy feel, when you print out the error, just prepend the
program's name to the VError's `message`.  Or just call
[node-cmdutil.fail(your_verror)](https://github.com/joyent/node-cmdutil), which
does this for you.

You can get the next-level Error using `err.cause()`:

```javascript
console.error(err2.cause().message);
```

prints:

    ENOENT, stat '/nonexistent'

Of course, you can chain these as many times as you want, and it works with any
kind of Error:

```javascript
var err1 = new Error('No such file or directory');
var err2 = new VError(err1, 'failed to stat "%s"', '/junk');
var err3 = new VError(err2, 'request failed');
console.error(err3.message);
```

This prints:

    request failed: failed to stat "/junk": No such file or directory

The idea is that each layer in the stack annotates the error with a description
of what it was doing.  The end result is a message that explains what happened
at each level.

You can also decorate Error objects with additional information so that callers
can not only handle each kind of error differently, but also construct their own
error messages (e.g., to localize them, format them, group them by type, and so
on).  See the example below.


# Deeper dive

The two main goals for VError are:

* **Make it easy to construct clear, complete error messages intended for
  people.**  Clear error messages greatly improve both user experience and
  debuggability, so we wanted to make it easy to build them.  That's why the
  constructor takes printf-style arguments.
* **Make it easy to construct objects with programmatically-accessible
  metadata** (which we call _informational properties_).  Instead of just saying
  "connection refused while connecting to 192.168.1.2:80", you can add
  properties like `"ip": "192.168.1.2"` and `"tcpPort": 80`.  This can be used
  for feeding into monitoring systems, analyzing large numbers of Errors (as
  from a log file), or localizing error messages.

To really make this useful, it also needs to be easy to compose Errors:
higher-level code should be able to augment the Errors reported by lower-level
code to provide a more complete description of what happened.  Instead of saying
"connection refused", you can say "operation X failed: connection refused".
That's why VError supports `causes`.

In order for all this to work, programmers need to know that it's generally safe
to wrap lower-level Errors with higher-level ones.  If you have existing code
that handles Errors produced by a library, you should be able to wrap those
Errors with a VError to add information without breaking the error handling
code.  There are two obvious ways that this could break such consumers:

* The error's name might change.  People typically use `name` to determine what
  kind of Error they've got.  To ensure compatibility, you can create VErrors
  with custom names, but this approach isn't great because it prevents you from
  representing complex failures.  For this reason, VError provides
  `findCauseByName`, which essentially asks: does this Error _or any of its
  causes_ have this specific type?  If error handling code uses
  `findCauseByName`, then subsystems can construct very specific causal chains
  for debuggability and still let people handle simple cases easily.  There's an
  example below.
* The error's properties might change.  People often hang additional properties
  off of Error objects.  If we wrap an existing Error in a new Error, those
  properties would be lost unless we copied them.  But there are a variety of
  both standard and non-standard Error properties that should _not_ be copied in
  this way: most obviously `name`, `message`, and `stack`, but also `fileName`,
  `lineNumber`, and a few others.  Plus, it's useful for some Error subclasses
  to have their own private properties -- and there'd be no way to know whether
  these should be copied.  For these reasons, VError first-classes these
  information properties.  You have to provide them in the constructor, you can
  only fetch them with the `info()` function, and VError takes care of making
  sure properties from causes wind up in the `info()` output.

Let's put this all together with an example from the node-fast RPC library.
node-fast implements a simple RPC protocol for Node programs.  There's a server
and client interface, and clients make RPC requests to servers.  Let's say the
server fails with an UnauthorizedError with message "user 'bob' is not
authorized".  The client wraps all server errors with a FastServerError.  The
client also wraps all request errors with a FastRequestError that includes the
name of the RPC call being made.  The result of this failed RPC might look like
this:

    name: FastRequestError
    message: "request failed: server error: user 'bob' is not authorized"
    rpcMsgid: <unique identifier for this request>
    rpcMethod: GetObject
    cause:
        name: FastServerError
        message: "server error: user 'bob' is not authorized"
        cause:
            name: UnauthorizedError
            message: "user 'bob' is not authorized"
            rpcUser: "bob"

When the caller uses `VError.info()`, the information properties are collapsed
so that it looks like this:

    message: "request failed: server error: user 'bob' is not authorized"
    rpcMsgid: <unique identifier for this request>
    rpcMethod: GetObject
    rpcUser: "bob"

Taking this apart:

* The error's message is a complete description of the problem.  The caller can
  report this directly to its caller, which can potentially make its way back to
  an end user (if appropriate).  It can also be logged.
* The caller can tell that the request failed on the server, rather than as a
  result of a client problem (e.g., failure to serialize the request), a
  transport problem (e.g., failure to connect to the server), or something else
  (e.g., a timeout).  They do this using `findCauseByName('FastServerError')`
  rather than checking the `name` field directly.
* If the caller logs this error, the logs can be analyzed to aggregate
  errors by cause, by RPC method name, by user, or whatever.  Or the
  error can be correlated with other events for the same rpcMsgid.
* It wasn't very hard for any part of the code to contribute to this Error.
  Each part of the stack has just a few lines to provide exactly what it knows,
  with very little boilerplate.

It's not expected that you'd use these complex forms all the time.  Despite
supporting the complex case above, you can still just do:

   new VError("my service isn't working");

for the simple cases.


# Reference: VError, WError, SError

VError, WError, and SError are convenient drop-in replacements for `Error` that
support printf-style arguments, first-class causes, informational properties,
and other useful features.


## Constructors

The VError constructor has several forms:

```javascript
/*
 * This is the most general form.  You can specify any supported options
 * (including "cause" and "info") this way.
 */
new VError(options, sprintf_args...)

/*
 * This is a useful shorthand when the only option you need is "cause".
 */
new VError(cause, sprintf_args...)

/*
 * This is a useful shorthand when you don't need any options at all.
 */
new VError(sprintf_args...)
```

All of these forms construct a new VError that behaves just like the built-in
JavaScript `Error` class, with some additional methods described below.

In the first form, `options` is a plain object with any of the following
optional properties:

Option name      | Type             | Meaning
---------------- | ---------------- | -------
`name`           | string           | Describes what kind of error this is.  This is intended for programmatic use to distinguish between different kinds of errors.  Note that in modern versions of Node.js, this name is ignored in the `stack` property value, but callers can still use the `name` property to get at it.
`cause`          | any Error object | Indicates that the new error was caused by `cause`.  See `cause()` below.  If unspecified, the cause will be `null`.
`strict`         | boolean          | If true, then `null` and `undefined` values in `sprintf_args` are passed through to `sprintf()`.  Otherwise, these are replaced with the strings `'null'`, and '`undefined`', respectively.
`constructorOpt` | function         | If specified, then the stack trace for this error ends at function `constructorOpt`.  Functions called by `constructorOpt` will not show up in the stack.  This is useful when this class is subclassed.
`info`           | object           | Specifies arbitrary informational properties that are available through the `VError.info(err)` static class method.  See that method for details.

The second form is equivalent to using the first form with the specified `cause`
as the error's cause.  This form is distinguished from the first form because
the first argument is an Error.

The third form is equivalent to using the first form with all default option
values.  This form is distinguished from the other forms because the first
argument is not an object or an Error.

The `WError` constructor is used exactly the same way as the `VError`
constructor.  The `SError` constructor is also used the same way as the
`VError` constructor except that in all cases, the `strict` property is
overriden to `true.


## Public properties

`VError`, `WError`, and `SError` all provide the same public properties as
JavaScript's built-in Error objects.

Property name | Type   | Meaning
------------- | ------ | -------
`name`        | string | Programmatically-usable name of the error.
`message`     | string | Human-readable summary of the failure.  Programmatically-accessible details are provided through `VError.info(err)` class method.
`stack`       | string | Human-readable stack trace where the Error was constructed.

For all of these classes, the printf-style arguments passed to the constructor
are processed with `sprintf()` to form a message.  For `WError`, this becomes
the complete `message` property.  For `SError` and `VError`, this message is
prepended to the message of the cause, if any (with a suitable separator), and
the result becomes the `message` property.

The `stack` property is managed entirely by the underlying JavaScript
implementation.  It's generally implemented using a getter function because
constructing the human-readable stack trace is somewhat expensive.

## Class methods

The following methods are defined on the `VError` class and as exported
functions on the `verror` module.  They're defined this way rather than using
methods on VError instances so that they can be used on Errors not created with
`VError`.

### `VError.cause(err)`

The `cause()` function returns the next Error in the cause chain for `err`, or
`null` if there is no next error.  See the `cause` argument to the constructor.
Errors can have arbitrarily long cause chains.  You can walk the `cause` chain
by invoking `VError.cause(err)` on each subsequent return value.  If `err` is
not a `VError`, the cause is `null`.

### `VError.info(err)`

Returns an object with all of the extra error information that's been associated
with this Error and all of its causes.  These are the properties passed in using
the `info` option to the constructor.  Properties not specified in the
constructor for this Error are implicitly inherited from this error's cause.

These properties are intended to provide programmatically-accessible metadata
about the error.  For an error that indicates a failure to resolve a DNS name,
informational properties might include the DNS name to be resolved, or even the
list of resolvers used to resolve it.  The values of these properties should
generally be plain objects (i.e., consisting only of null, undefined, numbers,
booleans, strings, and objects and arrays containing only other plain objects).

### `VError.fullStack(err)`

Returns a string containing the full stack trace, with all nested errors recursively
reported as `'caused by:' + err.stack`.

### `VError.findCauseByName(err, name)`

The `findCauseByName()` function traverses the cause chain for `err`, looking
for an error whose `name` property matches the passed in `name` value. If no
match is found, `null` is returned.

If all you want is to know _whether_ there's a cause (and you don't care what it
is), you can use `VError.hasCauseWithName(err, name)`.

If a vanilla error or a non-VError error is passed in, then there is no cause
chain to traverse. In this scenario, the function will check the `name`
property of only `err`.

### `VError.hasCauseWithName(err, name)`

Returns true if and only if `VError.findCauseByName(err, name)` would return
a non-null value.  This essentially determines whether `err` has any cause in
its cause chain that has name `name`.

### `VError.errorFromList(errors)`

Given an array of Error objects (possibly empty), return a single error
representing the whole collection of errors.  If the list has:

* 0 elements, returns `null`
* 1 element, returns the sole error
* more than 1 element, returns a MultiError referencing the whole list

This is useful for cases where an operation may produce any number of errors,
and you ultimately want to implement the usual `callback(err)` pattern.  You can
accumulate the errors in an array and then invoke
`callback(VError.errorFromList(errors))` when the operation is complete.


### `VError.errorForEach(err, func)`

Convenience function for iterating an error that may itself be a MultiError.

In all cases, `err` must be an Error.  If `err` is a MultiError, then `func` is
invoked as `func(errorN)` for each of the underlying errors of the MultiError.
If `err` is any other kind of error, `func` is invoked once as `func(err)`.  In
all cases, `func` is invoked synchronously.

This is useful for cases where an operation may produce any number of warnings
that may be encapsulated with a MultiError -- but may not be.

This function does not iterate an error's cause chain.


## Examples

The "Demo" section above covers several basic cases.  Here's a more advanced
case:

```javascript
var err1 = new VError('something bad happened');
/* ... */
var err2 = new VError({
    'name': 'ConnectionError',
    'cause': err1,
    'info': {
        'errno': 'ECONNREFUSED',
        'remote_ip': '127.0.0.1',
        'port': 215
    }
}, 'failed to connect to "%s:%d"', '127.0.0.1', 215);

console.log(err2.message);
console.log(err2.name);
console.log(VError.info(err2));
console.log(err2.stack);
```

This outputs:

    failed to connect to "127.0.0.1:215": something bad happened
    ConnectionError
    { errno: 'ECONNREFUSED', remote_ip: '127.0.0.1', port: 215 }
    ConnectionError: failed to connect to "127.0.0.1:215": something bad happened
        at Object.<anonymous> (/home/dap/node-verror/examples/info.js:5:12)
        at Module._compile (module.js:456:26)
        at Object.Module._extensions..js (module.js:474:10)
        at Module.load (module.js:356:32)
        at Function.Module._load (module.js:312:12)
        at Function.Module.runMain (module.js:497:10)
        at startup (node.js:119:16)
        at node.js:935:3

Information properties are inherited up the cause chain, with values at the top
of the chain overriding same-named values lower in the chain.  To continue that
example:

```javascript
var err3 = new VError({
    'name': 'RequestError',
    'cause': err2,
    'info': {
        'errno': 'EBADREQUEST'
    }
}, 'request failed');

console.log(err3.message);
console.log(err3.name);
console.log(VError.info(err3));
console.log(err3.stack);
```

This outputs:

    request failed: failed to connect to "127.0.0.1:215": something bad happened
    RequestError
    { errno: 'EBADREQUEST', remote_ip: '127.0.0.1', port: 215 }
    RequestError: request failed: failed to connect to "127.0.0.1:215": something bad happened
        at Object.<anonymous> (/home/dap/node-verror/examples/info.js:20:12)
        at Module._compile (module.js:456:26)
        at Object.Module._extensions..js (module.js:474:10)
        at Module.load (module.js:356:32)
        at Function.Module._load (module.js:312:12)
        at Function.Module.runMain (module.js:497:10)
        at startup (node.js:119:16)
        at node.js:935:3

You can also print the complete stack trace of combined `Error`s by using
`VError.fullStack(err).`

```javascript
var err1 = new VError('something bad happened');
/* ... */
var err2 = new VError(err1, 'something really bad happened here');

console.log(VError.fullStack(err2));
```

This outputs:

    VError: something really bad happened here: something bad happened
        at Object.<anonymous> (/home/dap/node-verror/examples/fullStack.js:5:12)
        at Module._compile (module.js:409:26)
        at Object.Module._extensions..js (module.js:416:10)
        at Module.load (module.js:343:32)
        at Function.Module._load (module.js:300:12)
        at Function.Module.runMain (module.js:441:10)
        at startup (node.js:139:18)
        at node.js:968:3
    caused by: VError: something bad happened
        at Object.<anonymous> (/home/dap/node-verror/examples/fullStack.js:3:12)
        at Module._compile (module.js:409:26)
        at Object.Module._extensions..js (module.js:416:10)
        at Module.load (module.js:343:32)
        at Function.Module._load (module.js:300:12)
        at Function.Module.runMain (module.js:441:10)
        at startup (node.js:139:18)
        at node.js:968:3

`VError.fullStack` is also safe to use on regular `Error`s, so feel free to use
it whenever you need to extract the stack trace from an `Error`, regardless if
it's a `VError` or not.

# Reference: MultiError

MultiError is an Error class that represents a group of Errors.  This is used
when you logically need to provide a single Error, but you want to preserve
information about multiple underying Errors.  A common case is when you execute
several operations in parallel and some of them fail.

MultiErrors are constructed as:

```javascript
new MultiError(error_list)
```

`error_list` is an array of at least one `Error` object.

The cause of the MultiError is the first error provided.  None of the other
`VError` options are supported.  The `message` for a MultiError consists the
`message` from the first error, prepended with a message indicating that there
were other errors.

For example:

```javascript
err = new MultiError([
    new Error('failed to resolve DNS name "abc.example.com"'),
    new Error('failed to resolve DNS name "def.example.com"'),
]);

console.error(err.message);
```

outputs:

    first of 2 errors: failed to resolve DNS name "abc.example.com"

See the convenience function `VError.errorFromList`, which is sometimes simpler
to use than this constructor.

## Public methods


### `errors()`

Returns an array of the errors used to construct this MultiError.


# Contributing

See separate [contribution guidelines](CONTRIBUTING.md).
# check-more-types

> Large collection of predicates, inspired by [check-types.js](https://github.com/philbooth/check-types.js)

[![NPM][check-more-types-icon] ][check-more-types-url]

[![manpm](https://img.shields.io/badge/manpm-%E2%9C%93-3399ff.svg)](https://github.com/bahmutov/manpm)
[![Build status][check-more-types-ci-image] ][check-more-types-ci-url]
[![dependencies][check-more-types-dependencies-image] ][check-more-types-dependencies-url]
[![devdependencies][check-more-types-devdependencies-image] ][check-more-types-devdependencies-url]

[![semantic-release][semantic-image] ][semantic-url]
[![Coverage Status][check-more-types-coverage-image] ][check-more-types-coverage-url]
[![Codacy Badge][check-more-types-codacy-image] ][check-more-types-codacy-url]
[![Code Climate][check-more-types-code-climate-image] ][check-more-types-code-climate-url]
![issue](http://issuestats.com/github/kensho/check-more-types/badge/issue)

[check-more-types-icon]: https://nodei.co/npm/check-more-types.png?downloads=true
[check-more-types-url]: https://npmjs.org/package/check-more-types
[check-more-types-ci-image]: https://travis-ci.org/kensho/check-more-types.png?branch=master
[check-more-types-ci-url]: https://travis-ci.org/kensho/check-more-types
[check-more-types-coverage-image]: https://coveralls.io/repos/kensho/check-more-types/badge.png
[check-more-types-coverage-url]: https://coveralls.io/r/kensho/check-more-types
[check-more-types-dependencies-image]: https://david-dm.org/kensho/check-more-types.png
[check-more-types-dependencies-url]: https://david-dm.org/kensho/check-more-types
[check-more-types-devdependencies-image]: https://david-dm.org/kensho/check-more-types/dev-status.png
[check-more-types-devdependencies-url]: https://david-dm.org/kensho/check-more-types#info=devDependencies
[check-more-types-codacy-image]: https://www.codacy.com/project/badge/25cb5d1410c7497cb057d887d1f3ea23
[check-more-types-codacy-url]: https://www.codacy.com/public/kensho/check-more-types.git
[check-more-types-code-climate-image]: https://codeclimate.com/github/kensho/check-more-types/badges/gpa.svg
[check-more-types-code-climate-url]: https://codeclimate.com/github/kensho/check-more-types
[semantic-image]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg
[semantic-url]: https://github.com/semantic-release/semantic-release



See [Readable conditions](http://glebbahmutov.com/blog/readable-conditions-using-check-types/)
for advice and examples.

## Install

**node:** `npm install check-more-types --save`

    var check = require('check-more-types');
    console.assert(check.bit(1), 'check.bit works');

**browser** `bower install check-more-types --save`

    <script src="check-more-types.js"></script>


* **API**
  * [check.email](#checkemail)
  * [check.extension (alias `check.ext`)](#checkextension-alias-checkext)
  * [check.odd and check.even](#checkodd-and-checkeven)
  * [check.port](#checkport)
  * [check.systemPort](#checksystemport)
  * [check.userPort](#checkuserport)
  * [check.error](#checkerror)
  * [check.https (alias `secure`)](#checkhttps-alias-secure)
  * [check.http](#checkhttp)
  * [check.webUrl (alias `url`)](#checkweburl-alias-url)
  * [check.contains](#checkcontains)
  * [check.defined](#checkdefined)
  * [check.semver](#checksemver)
  * [check.positiveNumber (alias `check.positive`)](#checkpositivenumber-alias-checkpositive)
  * [check.negativeNumber (alias `check.negative`)](#checknegativenumber-alias-checknegative)
  * [check.type](#checktype)
  * [check.bit](#checkbit)
  * [check.primitive](#checkprimitive)
  * [check.zero](#checkzero)
  * [check.git](#checkgit)
  * [check.commitId](#checkcommitid)
  * [check.shortCommitId](#checkshortcommitid)
  * [check.index](#checkindex)
  * [check.oneOf](#checkoneof)
  * [check.same](#checksame)
  * [check.length](#checklength)
  * [check.sameLength](#checksamelength)
  * [check.allSame](#checkallsame)
  * [check.unit](#checkunit)
  * [check.hexRgb](#checkhexrgb)
  * [check.bool](#checkbool)
  * [check.emptyString](#checkemptystring)
  * [check.empty](#checkempty)
  * [check.unempty](#checkunempty)
  * [check.unemptyArray](#checkunemptyarray)
  * [check.arrayOfStrings (alias `strings`)](#checkarrayofstrings-alias-strings)
  * [check.numbers](#checknumbers)
  * [check.arrayOf](#checkarrayof)
  * [check.badItems](#checkbaditems)
  * [check.arrayOfArraysOfStrings](#checkarrayofarraysofstrings)
  * [check.lowerCase](#checklowercase)
  * [check.has(obj, property)](#checkhasobj-property)
  * [check.all](#checkall)
  * [check.schema](#checkschema)
  * [check.schema bind](#checkschema-bind)
  * [schema composition](#schema-composition)
  * [check.raises(fn, validator)](#checkraisesfn-validator)
* [Modifiers](#modifiers)
  * [check.maybe](#checkmaybe)
  * [check.not](#checknot)
  * [check.verify](#checkverify)
* [Adding your own predicates](#adding-your-own-predicates)
  * [check.mixin(predicate, name)](#checkmixinpredicate-name)
  * [check.mixin does not override](#checkmixin-does-not-override)
* [Defending a function](#defending-a-function)
  * [check.defend(fn, predicates)](#checkdefendfn-predicates)
  * [protects optional arguments](#protects-optional-arguments)
  * [check.defend with messages](#checkdefend-with-messages)
  * [check.defend in module pattern](#checkdefend-in-module-pattern)
* [Safe callback execution](#safe-callback-execution)
  * [check.then](#checkthen)
  * [check.found](#checkfound)
  * [check.regexp](#checkregexp)
  * [check.promise](#checkpromise)
  * [check.validDate](#checkvaliddate)
  * [check.equal](#checkequal)
  * [check.or](#checkor)
  * [check.and](#checkand)


#### check.number

`check.number` is part of the `check-types` library, but as a note, it does not pass
`null`, `undefined` or `NaN` values

```js
check.number(null); // false
check.not.number(undefined); // true
check.number(NaN); // false
```

#### check.email

Really simple regex email check. Should not be relied to be robust.

```js
check.email('me@foo.bar') // true
check.email('me.foo.bar') // false
```

#### check.extension (alias `check.ext`)

Confirms that given file name has expected extension

```js
check.extension('txt', 'foo/bar.txt') // true
```

It is curried, so you can create convenient methods

```js
const isJs = check.extension('js')
isJs('script.js') // true
```

There are a couple of convenient shortcuts, like `check.isJs`, `check.isJson`, `check.isJpg`

#### check.odd and check.even

Check if a number odd or even

```js
check.odd(2) // false
check.odd(3) // true
check.even(2) // true
```

#### check.port

Returns true if passed argument is positive number less or equal to largest
allowed port number 65535

#### check.systemPort

Returns true if passed argument is number between 0 and 1024

#### check.userPort

Returns true if passed argument is a port number and larger than 1024

#### check.error

Returns true if given argument is an instance of type `Error`

#### check.https (alias `secure`)

Returns true if the provided url starts with `https://`. Alias `secure`.

#### check.http

Returns true if the provided url starts with `http://`

#### check.webUrl (alias `url`)

Returns true if the given string is http or https url.

#### check.contains

Returns true if given array contains an item, or given string contains substring.

```js
check.contains(['foo', 42], 'foo'); // true
check.contains('apple', 'pp'); // true
```

#### check.defined

    check.defined(0); // true
    check.defined(1); // true
    check.defined(true); // true
    check.defined(false); // true
    check.defined(null); // true
    check.defined(''); // true
    check.defined(); // false
    check.defined(root.doesNotExist); // false
    check.defined({}.doesNotExist); // false

---

#### check.semver

    check.semver('1.0.2'); // true
    check.semver('1.0.2-alpha'); // false

---

#### check.positiveNumber (alias `check.positive`)

```js
check.positive(100); // true
check.not.positive(-1); // true
```

---

#### check.negativeNumber (alias `check.negative`)

```js
check.negative(-10); // true
check.not.negativeNumber(1); // true
```

---

#### check.type

    check.type('string', 'foo'); // true
    check.type('number', 42); // true

`check.type` is curried.

---

#### check.bit

    check.bit(0); // true
    check.bit(1); // true
    check.bit('1'); // false
    check.bit(2); // false
    check.bit(true); // false

---

#### check.primitive

Returns true for primitive JavaScript types

    check.primitive(42); // true
    check.primitive(true); // true
    check.primitive('foo'); // true
    check.primitive([]); // false

Also returns true for `Symbol` ES6 syntax.

---

#### check.zero

    check.zero(0); // true
    check.zero(); // false
    check.zero(null); // false

---

#### check.git

    check.git('url string');

---

#### check.commitId

---

#### check.shortCommitId

---

#### check.index

---

#### check.oneOf

    var colors = ['red', 'green', 'blue'];
    var color = 'green';
    check.oneOf(colors, color); // true
    check.oneOf(colors, 'brown'); // false

Function is curried

---

#### check.same

    var foo = {}
    var bar = {}
    check.same(foo, foo); // true
    check.same(foo, bar); // false
    // primitives are compared by value
    check.same(0, 0); // true
    check.same('foo', 'foo'); // true

`check.same` should produce same result as `===`.

---

#### check.length

Confirms length of a string or an Array. The function is curried and
can guess the argument order

```js
check.length([1, 2], 2); // true
check.length('foo', 3); // true
// argument order
check.length(3, 'foo'); // true
// curried call
check.length('foo')(3); // true
check.length(3)('foo'); // true
```

---

#### check.sameLength

    check.sameLength([1, 2], ['a', 'b']); // true
    check.sameLength('ab', 'cd'); // true
    // different types
    check.sameLength([1, 2], 'ab'); // false

---

#### check.allSame

    var foo = {}
    var bar = {}
    check.allSame([foo, foo, foo]); // true
    check.allSame([foo, foo, bar]); // false
    // primitives are compared by value
    check.allSame([0, 0]); // true
    check.allSame(['foo', 'foo', 'foo']); // true
    check.allSame([false, 0]); // false

---

#### check.unit

    check.unit(0); // true
    check.unit(1); // true
    check.unit(0.1); // true
    check.unit(1.2); // false
    check.unit(-0.1); // false

---

#### check.hexRgb

    check.hexRgb('#FF00FF'); // true
    check.hexRgb('#000'); // true
    check.hexRgb('#aaffed'); // true
    check.hexRgb('#00aaffed'); // false
    check.hexRgb('aaffed'); // false

---

#### check.bool

    check.bool(true); // true
    check.bool(false); // true
    check.bool(0); // false
    check.bool(1); // false
    check.bool('1'); // false
    check.bool(2); // false

---

#### check.emptyString

    check.emptyString(''); // true
    check.emptyString(' '); // false
    check.emptyString(0); // false
    check.emptyString([]); // false

---

#### check.empty

    check.empty([]); // true
    check.empty(''); // true
    check.empty({}); // true
    check.empty(0); // false
    check.empty(['foo']); // false

---

#### check.unempty

    check.unempty([]); // false
    check.unempty(''); // false
    check.unempty({}); // false
    check.unempty(0); // true
    check.unempty(['foo']); // true
    check.unempty('foo'); // true

---

#### check.unemptyArray

    check.unemptyArray(null); // false
    check.unemptyArray(1); // false
    check.unemptyArray({}); // false
    check.unemptyArray([]); // false
    check.unemptyArray(root.doesNotExist); // false
    check.unemptyArray([1]); // true
    check.unemptyArray(['foo', 'bar']); // true

---

#### check.arrayOfStrings (alias `strings`)

    // second argument is checkLowerCase
    check.arrayOfStrings(['foo', 'Foo']); // true
    check.arrayOfStrings(['foo', 'Foo'], true); // false
    check.arrayOfStrings(['foo', 'bar'], true); // true
    check.arrayOfStrings(['FOO', 'BAR'], true); // false

---

#### check.numbers

Returns true if all items in an array are numbers

#### check.arrayOf

```js
check.arrayOf(check.unemptyString, ['foo', '']); // false
check.arrayOf(check.unemptyString, ['foo', 'bar']); // true
// can be partially applied and combined with check.schema
var person = {
  first: check.unemptyString,
  last: check.unemptyString
};
var isPerson = check.schema.bind(null, person);
var arePeople = check.arrayOf.bind(null, isPerson);
var people = [{
  first: 'foo',
  last: 'bar'
}];
arePeople(people); // true
```
---

Why would you need `check.arrayOf(predicate, x)` and not simply use `x.every(predicate)`?
Because `x` might not be an Array.

#### check.badItems

Finds items that do not pass predicate

```js
check.badItems(check.unemptyString, ['foo', '', 'bar']); // ['']
```

#### check.arrayOfArraysOfStrings

    // second argument is checkLowerCase
    check.arrayOfArraysOfStrings([['foo'], ['bar'}}); // true
    check.arrayOfArraysOfStrings([['foo'], ['bar'}}, true); // true
    check.arrayOfArraysOfStrings([['foo'], ['BAR'}}, true); // false

---

#### check.lowerCase

    check.lowerCase('foo bar'); // true
    check.lowerCase('*foo ^bar'); // true
    check.lowerCase('fooBar'); // false
    // non-strings return false
    check.lowerCase(10); // false

---

#### check.has(obj, property)

    var obj = {
    foo: 'foo',
    bar: 0
    }
    check.has(obj, 'foo'); // true
    check.has(obj, 'bar'); // true
    check.has(obj, 'baz'); // false
    // non-object returns false
    check.has(5, 'foo'); // false
    check.has('foo', 'length'); // true

---

#### check.all

    var obj = {
      foo: 'foo',
      bar: 'bar',
      baz: 'baz'
    }
    var predicates = {
      foo: check.unemptyString,
      bar: function(value) {
        return value === 'bar'
      }
    }
    check.all(obj, predicates); // true

---

#### check.schema

    var obj = {
    foo: 'foo',
    bar: 'bar',
    baz: 'baz'
    }
    var schema = {
    foo: check.unemptyString,
    bar: function(value) {
    return value === 'bar'
    }
    }
    check.schema(schema, obj); // true
    check.schema(schema, {}); // false

`check.spec` is equivalent to `check.all` but with arguments reversed.
This makes it very convenient to create new validator functions using partial
argument application

The method is curried, thus you can easily create predicate function

```js
var hasName = check.schema({ name: check.unemptyString });
hasName({ name: 'joe' }); // true
```

#### check.schema bind

    var personSchema = {
    name: check.unemptyString,
    age: check.positiveNumber
    }
    var isValidPerson = check.schema.bind(null, personSchema)
    var h1 = {
    name: 'joe',
    age: 10
    }
    var h2 = {
    name: 'ann'
    // missing age property
    }
    isValidPerson(h1); // true
    isValidPerson(h2); // false

If you want you can manually bind `check.schema` to first argument

    var personSchema = {
      name: check.unemptyString,
      age: check.positiveNumber
    };
    var isValidPerson = check.schema.bind(null, personSchema);
    var h1 = {
      name: 'joe',
      age: 10
    };
    var h2 = {
      name: 'ann'
        // missing age property
    };
    isValidPerson(h1); // true
    isValidPerson(h2); // false

You can use `Function.prototype.bind` or any partial application method, for example
`_.partial(check.schema, personSchema);`.
Because bound schema parameter generates a valid function, you can nest checks using
schema composition. For example let us combine the reuse `isValidPerson` as part of
another check

#### schema composition

    var teamSchema = {
    manager: isValidPerson,
    members: check.unemptyArray
    }
    var team = {
    manager: {
    name: 'jim',
    age: 20
    },
    members: ['joe', 'ann']
    }
    check.schema(teamSchema, team); // true

---

#### check.raises(fn, validator)

    function foo() {
    throw new Error('foo')
    }

    function bar() {}

    function isValidError(err) {
    return err.message === 'foo'
    }

    function isInvalid(err) {
    check.instance(err, Error); // true
    return false
    }
    check.raises(foo); // true
    check.raises(bar); // false
    check.raises(foo, isValidError); // true
    check.raises(foo, isInvalid); // false

### Modifiers

Every predicate function is also added to `check.maybe` object.
The `maybe` predicate passes if the argument is null or undefined,
or the predicate returns true.

#### check.maybe

    check.maybe.bool(); // true
    check.maybe.bool('true'); // false
    var empty
    check.maybe.lowerCase(empty); // true
    check.maybe.unemptyArray(); // true
    check.maybe.unemptyArray([]); // false
    check.maybe.unemptyArray(['foo', 'bar']); // true

Every function has a negated predicate in `check.not` object

#### check.not

    check.not.bool(4); // true
    check.not.bool('true'); // true
    check.not.bool(true); // false

Every predicate can also throw an exception if it fails

#### check.verify

    check.verify.arrayOfStrings(['foo', 'bar'])
    check.verify.bit(1)

    function nonStrings() {
      check.verify.arrayOfStrings(['Foo', 1])
    }
    check.raises(nonStrings); // true
    function nonLowerCase() {
      check.verify.lowerCase('Foo')
    }
    check.raises(nonLowerCase); // true

---

### Adding your own predicates

You can add new predicates to `check`, `check.maybe`, etc. by using `check.mixin(predicate)`
method. If you do not pass a name, it will try using function's name.

#### check.mixin(predicate, name)

    function isBar(a) {
      return a === 'bar'
    }
    check.mixin(isBar, 'bar')
    check.bar('bar'); // true
    check.bar('anything else'); // false
    // supports modifiers
    check.maybe.bar(); // true
    check.maybe.bar('bar'); // true
    check.not.bar('foo'); // true
    check.not.bar('bar'); // false

Mixin will not override existing functions

#### check.mixin does not override

    function isFoo(a) {
      return a === 'foo'
    }

    function isBar(a) {
      return a === 'bar'
    }
    check.mixin(isFoo, 'isFoo')
    check.isFoo; // isFoo
    check.mixin(isBar, 'isFoo')
    check.isFoo; // isFoo

### Defending a function

Using *check-more-types* you can separate the inner function logic from checking input
arguments. Instead of this

```js
function add(a, b) {
    la(check.number(a), 'first argument should be a number', a);
    la(check.number(a), 'second argument should be a number', b);
    return a + b;
}
```

you can use `check.defend` function

#### check.defend(fn, predicates)

    function add(a, b) {
      return a + b
    }
    var safeAdd = check.defend(add, check.number, check.number)
    add('foo', 2); // 'foo2'
    // calling safeAdd('foo', 2) raises an exception
    check.raises(safeAdd.bind(null, 'foo', 2)); // true

---

#### protects optional arguments

    function add(a, b) {
      if (typeof b === 'undefined') {
        return 'foo'
      }
      return a + b
    }
    add(2); // 'foo'
    var safeAdd = check.defend(add, check.number, check.maybe.number)
    safeAdd(2, 3); // 5
    safeAdd(2); // 'foo'

---

You can add extra message after a predicate

#### check.defend with messages

    function add(a, b) {
      return a + b
    }
    var safeAdd = check.defend(add, check.number, 'a should be a number', check.string, 'b should be a string')
    safeAdd(2, 'foo'); // '2foo'
    function addNumbers() {
      return safeAdd(2, 3)
    }

    function checkException(err) {
      err.message; // 'Argument 2: 3 does not pass predicate: b should be a string'
      return true
    }
    check.raises(addNumbers, checkException); // true

---

This works great when combined with JavaScript module pattern as in this example

#### check.defend in module pattern

    var add = (function() {
      // inner private function without any argument checks
      function add(a, b) {
          return a + b
        }
        // return defended function
      return check.defend(add, check.number, check.number)
    }())
    add(2, 3); // 5
    // trying to call with non-numbers raises an exception
    function callAddWithNonNumbers() {
      return add('foo', 'bar')
    }
    check.raises(callAddWithNonNumbers); // true

---

### Safe callback execution

Sometimes we want to execute a function depending on the condition, but without throwing an
exception. For these cases, there is `check.then`

#### check.then

    function isSum10(a, b) {
      return a + b === 10
    }

    function sum(a, b) {
      return a + b
    }
    var onlyAddTo10 = check.then(isSum10, sum)
      // isSum10 returns true for these arguments
      // then sum is executed
    onlyAddTo10(3, 7); // 10
    onlyAddTo10(1, 2); // undefined
    // sum is never called because isSum10 condition is false

----

#### check.found

Great for quickly checking string or array search results

```js
check.found('foo'.indexOf('f')); // true
check.found('foo bar'.indexOf('bar')); // true
```

#### check.regexp

Returns true if the passed value is a regular expression.

#### check.promise

Returns true if given object has promise methods (`.then`, etc)

#### check.validDate

Returns true if the given instance is a Date and is valid.

#### check.equal

Curried shallow strict comparison

```js
var foo = 'foo';
check.equal(foo, 'foo'); // true
var isFoo = check.equal('foo');
isFoo('foo'); // true
isFoo('bar'); // false
```

#### check.or

Combines multiple predicates into single one using OR logic

```js
var predicate = check.or(check.bool, check.unemptyString);
predicate(true); // true
predicate('foo'); // true
predicate(42); // false
```

It treats non-functions as boolean values

```js
var predicate = check.or(check.unemptyString, 42);
// will always return true
predicate('foo'); // true, because it is unempty string
predicate(false); // true, because 42 is truthy
```

Note: if there are any exceptions inside the individual predicate functions, they are
treated as `false` values.

#### check.and

Combines multiple predicates using AND. If the predicate is not a function,
evaluates it as a boolean value.

```js
function isFoo(x) { return x === 'foo'; }
check.and(check.unemptyString, isFoo); // only true for "foo"
```

Both `check.or` and `check.and` are very useful inside `check.schema` to create
more powerful predicates on the fly.

```js
var isFirstLastNames = check.schema.bind(null, {
  first: check.unemptyString,
  last: check.unemptyString
});
var isValidPerson = check.schema.bind(null, {
  name: check.or(check.unemptyString, isFirstLastNames)
});
isValidPerson({ name: 'foo' }); // true
isValidPerson({ name: {
  first: 'foo',
  last: 'bar'
}}); // true
```

### Small print

Author: Kensho &copy; 2014

* [@kensho](https://twitter.com/kensho)
* [kensho.com](http://kensho.com)

Support: if you find any problems with this library,
[open issue](https://github.com/kensho/check-more-types/issues) on Github



This documentation was generated using [grunt-xplain](https://github.com/bahmutov/grunt-xplain)
and [grunt-readme](https://github.com/jonschlinkert/grunt-readme).

## MIT License

The MIT License (MIT)

Copyright (c) 2014 Kensho

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



# inflight

Add callbacks to requests in flight to avoid async duplication

## USAGE

```javascript
var inflight = require('inflight')

// some request that does some stuff
function req(key, callback) {
  // key is any random string.  like a url or filename or whatever.
  //
  // will return either a falsey value, indicating that the
  // request for this key is already in flight, or a new callback
  // which when called will call all callbacks passed to inflightk
  // with the same key
  callback = inflight(key, callback)

  // If we got a falsey value back, then there's already a req going
  if (!callback) return

  // this is where you'd fetch the url or whatever
  // callback is also once()-ified, so it can safely be assigned
  // to multiple events etc.  First call wins.
  setTimeout(function() {
    callback(null, key)
  }, 100)
}

// only assigns a single setTimeout
// when it dings, all cbs get called
req('foo', cb1)
req('foo', cb2)
req('foo', cb3)
req('foo', cb4)
```
# babel-runtime

A JSON with color names and its values. Based on http://dev.w3.org/csswg/css-color/#named-colors.

[![NPM](https://nodei.co/npm/color-name.png?mini=true)](https://nodei.co/npm/color-name/)


```js
var colors = require('color-name');
colors.red //[255,0,0]
```

<a href="LICENSE"><img src="https://upload.wikimedia.org/wikipedia/commons/0/0c/MIT_logo.svg" width="120"/></a>
# Tmp

A simple temporary file and directory creator for [node.js.][1]

[![Build Status](https://travis-ci.org/raszi/node-tmp.svg?branch=master)](https://travis-ci.org/raszi/node-tmp)
[![Dependencies](https://david-dm.org/raszi/node-tmp.svg)](https://david-dm.org/raszi/node-tmp)
[![npm version](https://badge.fury.io/js/tmp.svg)](https://badge.fury.io/js/tmp)

## About

This is a [widely used library][2] to create temporary files and directories
in a [node.js][1] environment.

Tmp offers both an asynchronous and a synchronous API. For all API calls, all
the parameters are optional.

Tmp uses crypto for determining random file names, or, when using templates,
a six letter random identifier. And just in case that you do not have that much
entropy left on your system, Tmp will fall back to pseudo random numbers.

You can set whether you want to remove the temporary file on process exit or
not, and the destination directory can also be set.

## How to install

```bash
npm install tmp
```

## Usage

### Asynchronous file creation

Simple temporary file creation, the file will be closed and unlinked on process exit.

```javascript
var tmp = require('tmp');

tmp.file(function _tempFileCreated(err, path, fd, cleanupCallback) {
  if (err) throw err;

  console.log("File: ", path);
  console.log("Filedescriptor: ", fd);
  
  // If we don't need the file anymore we could manually call the cleanupCallback
  // But that is not necessary if we didn't pass the keep option because the library
  // will clean after itself.
  cleanupCallback();
});
```

### Synchronous file creation

A synchronous version of the above.

```javascript
var tmp = require('tmp');

var tmpobj = tmp.fileSync();
console.log("File: ", tmpobj.name);
console.log("Filedescriptor: ", tmpobj.fd);
  
// If we don't need the file anymore we could manually call the removeCallback
// But that is not necessary if we didn't pass the keep option because the library
// will clean after itself.
tmpobj.removeCallback();
```

Note that this might throw an exception if either the maximum limit of retries
for creating a temporary name fails, or, in case that you do not have the permission
to write to the directory where the temporary file should be created in.

### Asynchronous directory creation

Simple temporary directory creation, it will be removed on process exit.

If the directory still contains items on process exit, then it won't be removed.

```javascript
var tmp = require('tmp');

tmp.dir(function _tempDirCreated(err, path, cleanupCallback) {
  if (err) throw err;

  console.log("Dir: ", path);
  
  // Manual cleanup
  cleanupCallback();
});
```

If you want to cleanup the directory even when there are entries in it, then
you can pass the `unsafeCleanup` option when creating it.

### Synchronous directory creation

A synchronous version of the above.

```javascript
var tmp = require('tmp');

var tmpobj = tmp.dirSync();
console.log("Dir: ", tmpobj.name);
// Manual cleanup
tmpobj.removeCallback();
```

Note that this might throw an exception if either the maximum limit of retries
for creating a temporary name fails, or, in case that you do not have the permission
to write to the directory where the temporary directory should be created in.

### Asynchronous filename generation

It is possible with this library to generate a unique filename in the specified
directory.

```javascript
var tmp = require('tmp');

tmp.tmpName(function _tempNameGenerated(err, path) {
    if (err) throw err;

    console.log("Created temporary filename: ", path);
});
```

### Synchronous filename generation

A synchronous version of the above.

```javascript
var tmp = require('tmp');

var name = tmp.tmpNameSync();
console.log("Created temporary filename: ", name);
```

## Advanced usage

### Asynchronous file creation

Creates a file with mode `0644`, prefix will be `prefix-` and postfix will be `.txt`.

```javascript
var tmp = require('tmp');

tmp.file({ mode: 0644, prefix: 'prefix-', postfix: '.txt' }, function _tempFileCreated(err, path, fd) {
  if (err) throw err;

  console.log("File: ", path);
  console.log("Filedescriptor: ", fd);
});
```

### Synchronous file creation

A synchronous version of the above.

```javascript
var tmp = require('tmp');

var tmpobj = tmp.fileSync({ mode: 0644, prefix: 'prefix-', postfix: '.txt' });
console.log("File: ", tmpobj.name);
console.log("Filedescriptor: ", tmpobj.fd);
```

### Controlling the Descriptor

As a side effect of creating a unique file `tmp` gets a file descriptor that is
returned to the user as the `fd` parameter.  The descriptor may be used by the
application and is closed when the `removeCallback` is invoked.

In some use cases the application does not need the descriptor, needs to close it
without removing the file, or needs to remove the file without closing the
descriptor.  Two options control how the descriptor is managed:

* `discardDescriptor` - if `true` causes `tmp` to close the descriptor after the file
  is created.  In this case the `fd` parameter is undefined.
* `detachDescriptor` - if `true` causes `tmp` to return the descriptor in the `fd`
  parameter, but it is the application's responsibility to close it when it is no
  longer needed.

```javascript
var tmp = require('tmp');

tmp.file({ discardDescriptor: true }, function _tempFileCreated(err, path, fd, cleanupCallback) {
  if (err) throw err;
  // fd will be undefined, allowing application to use fs.createReadStream(path)
  // without holding an unused descriptor open.
});
```

```javascript
var tmp = require('tmp');

tmp.file({ detachDescriptor: true }, function _tempFileCreated(err, path, fd, cleanupCallback) {
  if (err) throw err;

  cleanupCallback();
  // Application can store data through fd here; the space used will automatically
  // be reclaimed by the operating system when the descriptor is closed or program
  // terminates.
});
```

### Asynchronous directory creation

Creates a directory with mode `0755`, prefix will be `myTmpDir_`.

```javascript
var tmp = require('tmp');

tmp.dir({ mode: 0750, prefix: 'myTmpDir_' }, function _tempDirCreated(err, path) {
  if (err) throw err;

  console.log("Dir: ", path);
});
```

### Synchronous directory creation

Again, a synchronous version of the above.

```javascript
var tmp = require('tmp');

var tmpobj = tmp.dirSync({ mode: 0750, prefix: 'myTmpDir_' });
console.log("Dir: ", tmpobj.name);
```

### mkstemp like, asynchronously

Creates a new temporary directory with mode `0700` and filename like `/tmp/tmp-nk2J1u`.

```javascript
var tmp = require('tmp');

tmp.dir({ template: '/tmp/tmp-XXXXXX' }, function _tempDirCreated(err, path) {
  if (err) throw err;

  console.log("Dir: ", path);
});
```

### mkstemp like, synchronously

This will behave similarly to the asynchronous version.

```javascript
var tmp = require('tmp');

var tmpobj = tmp.dirSync({ template: '/tmp/tmp-XXXXXX' });
console.log("Dir: ", tmpobj.name);
```

### Asynchronous filename generation

The `tmpName()` function accepts the `prefix`, `postfix`, `dir`, etc. parameters also:

```javascript
var tmp = require('tmp');

tmp.tmpName({ template: '/tmp/tmp-XXXXXX' }, function _tempNameGenerated(err, path) {
    if (err) throw err;

    console.log("Created temporary filename: ", path);
});
```

### Synchronous filename generation

The `tmpNameSync()` function works similarly to `tmpName()`.

```javascript
var tmp = require('tmp');
var tmpname = tmp.tmpNameSync({ template: '/tmp/tmp-XXXXXX' });
console.log("Created temporary filename: ", tmpname);
```

## Graceful cleanup

One may want to cleanup the temporary files even when an uncaught exception
occurs. To enforce this, you can call the `setGracefulCleanup()` method:

```javascript
var tmp = require('tmp');

tmp.setGracefulCleanup();
```

## Options

All options are optional :)

  * `mode`: the file mode to create with, it fallbacks to `0600` on file creation and `0700` on directory creation
  * `prefix`: the optional prefix, fallbacks to `tmp-` if not provided
  * `postfix`: the optional postfix, fallbacks to `.tmp` on file creation
  * `template`: [`mkstemp`][3] like filename template, no default
  * `dir`: the optional temporary directory, fallbacks to system default (guesses from environment)
  * `tries`: how many times should the function try to get a unique filename before giving up, default `3`
  * `keep`: signals that the temporary file or directory should not be deleted on exit, default is `false`, means delete
    * Please keep in mind that it is recommended in this case to call the provided `cleanupCallback` function manually.
  * `unsafeCleanup`: recursively removes the created temporary directory, even when it's not empty. default is `false`

[1]: http://nodejs.org/
[2]: https://www.npmjs.com/browse/depended/tmp
[3]: http://www.kernel.org/doc/man-pages/online/pages/man3/mkstemp.3.html
# buffer-crc32

[![Build Status](https://secure.travis-ci.org/brianloveswords/buffer-crc32.png?branch=master)](http://travis-ci.org/brianloveswords/buffer-crc32)

crc32 that works with binary data and fancy character sets, outputs
buffer, signed or unsigned data and has tests.

Derived from the sample CRC implementation in the PNG specification: http://www.w3.org/TR/PNG/#D-CRCAppendix

# install
```
npm install buffer-crc32
```

# example
```js
var crc32 = require('buffer-crc32');
// works with buffers
var buf = Buffer([0x00, 0x73, 0x75, 0x70, 0x20, 0x62, 0x72, 0x6f, 0x00])
crc32(buf) // -> <Buffer 94 5a ab 4a>

// has convenience methods for getting signed or unsigned ints
crc32.signed(buf) // -> -1805997238
crc32.unsigned(buf) // -> 2488970058

// will cast to buffer if given a string, so you can
// directly use foreign characters safely
crc32('自動販売機') // -> <Buffer cb 03 1a c5>

// and works in append mode too
var partialCrc = crc32('hey');
var partialCrc = crc32(' ', partialCrc);
var partialCrc = crc32('sup', partialCrc);
var partialCrc = crc32(' ', partialCrc);
var finalCrc = crc32('bros', partialCrc); // -> <Buffer 47 fa 55 70>
```

# tests
This was tested against the output of zlib's crc32 method. You can run
the tests with`npm test` (requires tap)

# see also
https://github.com/alexgorbatchev/node-crc, `crc.buffer.crc32` also
supports buffer inputs and return unsigned ints (thanks @tjholowaychuk).

# license
MIT/X11
# HAR Schema [![version][npm-version]][npm-url] [![License][npm-license]][license-url]

> JSON Schema for HTTP Archive ([HAR][spec]).

[![Build Status][travis-image]][travis-url]
[![Downloads][npm-downloads]][npm-url]
[![Code Climate][codeclimate-quality]][codeclimate-url]
[![Coverage Status][codeclimate-coverage]][codeclimate-url]
[![Dependency Status][dependencyci-image]][dependencyci-url]
[![Dependencies][david-image]][david-url]

## Install

```bash
npm install --only=production --save har-schema
```

## Usage

Compatible with any [JSON Schema validation tool][validator].

----
> :copyright: [ahmadnassri.com](https://www.ahmadnassri.com/) &nbsp;&middot;&nbsp;
> License: [ISC][license-url] &nbsp;&middot;&nbsp;
> Github: [@ahmadnassri](https://github.com/ahmadnassri) &nbsp;&middot;&nbsp;
> Twitter: [@ahmadnassri](https://twitter.com/ahmadnassri)

[license-url]: http://choosealicense.com/licenses/isc/

[travis-url]: https://travis-ci.org/ahmadnassri/har-schema
[travis-image]: https://img.shields.io/travis/ahmadnassri/har-schema.svg?style=flat-square

[npm-url]: https://www.npmjs.com/package/har-schema
[npm-license]: https://img.shields.io/npm/l/har-schema.svg?style=flat-square
[npm-version]: https://img.shields.io/npm/v/har-schema.svg?style=flat-square
[npm-downloads]: https://img.shields.io/npm/dm/har-schema.svg?style=flat-square

[codeclimate-url]: https://codeclimate.com/github/ahmadnassri/har-schema
[codeclimate-quality]: https://img.shields.io/codeclimate/github/ahmadnassri/har-schema.svg?style=flat-square
[codeclimate-coverage]: https://img.shields.io/codeclimate/coverage/github/ahmadnassri/har-schema.svg?style=flat-square

[david-url]: https://david-dm.org/ahmadnassri/har-schema
[david-image]: https://img.shields.io/david/ahmadnassri/har-schema.svg?style=flat-square

[dependencyci-url]: https://dependencyci.com/github/ahmadnassri/har-schema
[dependencyci-image]: https://dependencyci.com/github/ahmadnassri/har-schema/badge?style=flat-square

[spec]: https://github.com/ahmadnassri/har-spec/blob/master/versions/1.2.md
[validator]: https://github.com/ahmadnassri/har-validator
# node-http-signature

node-http-signature is a node.js library that has client and server components
for Joyent's [HTTP Signature Scheme](http_signing.md).

## Usage

Note the example below signs a request with the same key/cert used to start an
HTTP server. This is almost certainly not what you actually want, but is just
used to illustrate the API calls; you will need to provide your own key
management in addition to this library.

### Client

```js
var fs = require('fs');
var https = require('https');
var httpSignature = require('http-signature');

var key = fs.readFileSync('./key.pem', 'ascii');

var options = {
  host: 'localhost',
  port: 8443,
  path: '/',
  method: 'GET',
  headers: {}
};

// Adds a 'Date' header in, signs it, and adds the
// 'Authorization' header in.
var req = https.request(options, function(res) {
  console.log(res.statusCode);
});


httpSignature.sign(req, {
  key: key,
  keyId: './cert.pem'
});

req.end();
```

### Server

```js
var fs = require('fs');
var https = require('https');
var httpSignature = require('http-signature');

var options = {
  key: fs.readFileSync('./key.pem'),
  cert: fs.readFileSync('./cert.pem')
};

https.createServer(options, function (req, res) {
  var rc = 200;
  var parsed = httpSignature.parseRequest(req);
  var pub = fs.readFileSync(parsed.keyId, 'ascii');
  if (!httpSignature.verifySignature(parsed, pub))
    rc = 401;

  res.writeHead(rc);
  res.end();
}).listen(8443);
```

## Installation

    npm install http-signature

## License

MIT.

## Bugs

See <https://github.com/joyent/node-http-signature/issues>.
# fast-json-stable-stringify

Deterministic `JSON.stringify()` - a faster version of [@substack](https://github.com/substack)'s json-stable-strigify without [jsonify](https://github.com/substack/jsonify).

You can also pass in a custom comparison function.

[![Build Status](https://travis-ci.org/epoberezkin/fast-json-stable-stringify.svg?branch=master)](https://travis-ci.org/epoberezkin/fast-json-stable-stringify)
[![Coverage Status](https://coveralls.io/repos/github/epoberezkin/fast-json-stable-stringify/badge.svg?branch=master)](https://coveralls.io/github/epoberezkin/fast-json-stable-stringify?branch=master)

# example

``` js
var stringify = require('fast-json-stable-stringify');
var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
console.log(stringify(obj));
```

output:

```
{"a":3,"b":[{"x":4,"y":5,"z":6},7],"c":8}
```


# methods

``` js
var stringify = require('fast-json-stable-stringify')
```

## var str = stringify(obj, opts)

Return a deterministic stringified string `str` from the object `obj`.


## options

### cmp

If `opts` is given, you can supply an `opts.cmp` to have a custom comparison
function for object keys. Your function `opts.cmp` is called with these
parameters:

``` js
opts.cmp({ key: akey, value: avalue }, { key: bkey, value: bvalue })
```

For example, to sort on the object key names in reverse order you could write:

``` js
var stringify = require('fast-json-stable-stringify');

var obj = { c: 8, b: [{z:6,y:5,x:4},7], a: 3 };
var s = stringify(obj, function (a, b) {
    return a.key < b.key ? 1 : -1;
});
console.log(s);
```

which results in the output string:

```
{"c":8,"b":[{"z":6,"y":5,"x":4},7],"a":3}
```

Or if you wanted to sort on the object values in reverse order, you could write:

```
var stringify = require('fast-json-stable-stringify');

var obj = { d: 6, c: 5, b: [{z:3,y:2,x:1},9], a: 10 };
var s = stringify(obj, function (a, b) {
    return a.value < b.value ? 1 : -1;
});
console.log(s);
```

which outputs:

```
{"d":6,"c":5,"b":[{"z":3,"y":2,"x":1},9],"a":10}
```

### cycles

Pass `true` in `opts.cycles` to stringify circular property as `__cycle__` - the result will not be a valid JSON string in this case.

TypeError will be thrown in case of circular object without this option.


# install

With [npm](https://npmjs.org) do:

```
npm install fast-json-stable-stringify
```


# benchmark

To run benchmark (requires Node.js 6+):
```
node benchmark
```

Results:
```
fast-json-stable-stringify x 17,189 ops/sec ±1.43% (83 runs sampled)
json-stable-stringify x 13,634 ops/sec ±1.39% (85 runs sampled)
fast-stable-stringify x 20,212 ops/sec ±1.20% (84 runs sampled)
faster-stable-stringify x 15,549 ops/sec ±1.12% (84 runs sampled)
The fastest is fast-stable-stringify
```


# license

[MIT](https://github.com/epoberezkin/fast-json-stable-stringify/blob/master/LICENSE)
# json-schema-traverse
Traverse JSON Schema passing each schema object to callback

[![Build Status](https://travis-ci.org/epoberezkin/json-schema-traverse.svg?branch=master)](https://travis-ci.org/epoberezkin/json-schema-traverse)
[![npm version](https://badge.fury.io/js/json-schema-traverse.svg)](https://www.npmjs.com/package/json-schema-traverse)
[![Coverage Status](https://coveralls.io/repos/github/epoberezkin/json-schema-traverse/badge.svg?branch=master)](https://coveralls.io/github/epoberezkin/json-schema-traverse?branch=master)


## Install

```
npm install json-schema-traverse
```


## Usage

```javascript
const traverse = require('json-schema-traverse');
const schema = {
  properties: {
    foo: {type: 'string'},
    bar: {type: 'integer'}
  }
};

traverse(schema, cb);
// cb is called 3 times with:
// 1. root schema
// 2. {type: 'string'}
// 3. {type: 'integer'}
```

Callback function is called for each schema object (not including draft-06 boolean schemas), including the root schema. Schema references ($ref) are not resolved, they are passed as is.

Callback is passed these parameters:

- _schema_: the current schema object
- _JSON pointer_: from the root schema to the current schema object
- _root schema_: the schema passed to `traverse` object
- _parent JSON pointer_: from the root schema to the parent schema object (see below)
- _parent keyword_: the keyword inside which this schema appears (e.g. `properties`, `anyOf`, etc.)
- _parent schema_: not necessarily parent object/array; in the example above the parent schema for `{type: 'string'}` is the root schema
- _index/property_: index or property name in the array/object containing multiple schemas; in the example above for `{type: 'string'}` the property name is `'foo'`


## Traverse objects in all unknown keywords

```javascript
const traverse = require('json-schema-traverse');
const schema = {
  mySchema: {
    minimum: 1,
    maximum: 2
  }
};

traverse(schema, {allKeys: true}, cb);
// cb is called 2 times with:
// 1. root schema
// 2. mySchema
```

Without option `allKeys: true` callback will be called only with root schema.


## License

[MIT](https://github.com/epoberezkin/json-schema-traverse/blob/master/LICENSE)
# lodash v4.17.10

The [Lodash](https://lodash.com/) library exported as [Node.js](https://nodejs.org/) modules.

## Installation

Using npm:
```shell
$ npm i -g npm
$ npm i --save lodash
```

In Node.js:
```js
// Load the full build.
var _ = require('lodash');
// Load the core build.
var _ = require('lodash/core');
// Load the FP build for immutable auto-curried iteratee-first data-last methods.
var fp = require('lodash/fp');

// Load method categories.
var array = require('lodash/array');
var object = require('lodash/fp/object');

// Cherry-pick methods for smaller browserify/rollup/webpack bundles.
var at = require('lodash/at');
var curryN = require('lodash/fp/curryN');
```

See the [package source](https://github.com/lodash/lodash/tree/4.17.10-npm) for more details.

**Note:**<br>
Install [n_](https://www.npmjs.com/package/n_) for Lodash use in the Node.js < 6 REPL.

## Support

Tested in Chrome 63-64, Firefox 57-58, IE 11, Edge 14, Safari 10-11, Node.js 4-9, & PhantomJS 2.1.1.<br>
Automated [browser](https://saucelabs.com/u/lodash) & [CI](https://travis-ci.org/lodash/lodash/) test runs are available.
@cypress/xvfb: easily start and stop an X Virtual Frame Buffer from your node apps.
-----

[![CircleCI](https://circleci.com/gh/cypress-io/xvfb.svg?style=svg)](https://circleci.com/gh/cypress-io/xvfb)
[![Build Status](https://travis-ci.org/cypress-io/xvfb.svg?branch=master)](https://travis-ci.org/cypress-io/xvfb)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

### Usage

```javascript
var Xvfb = require('xvfb');
var options = {}; // optional
var xvfb = new Xvfb(options);
xvfb.start(function(err, xvfbProcess) {
  // code that uses the virtual frame buffer here
  xvfb.stop(function(err) {
    // the Xvfb is stopped
  });
});
```

The Xvfb constructor takes four options:

* <code>displayNum</code> - the X display to use, defaults to the lowest unused display number >= 99 if <code>reuse</code> is false or 99 if <code>reuse</code> is true.
* <code>reuse</code> - whether to reuse an existing Xvfb instance if it already exists on the X display referenced by displayNum.
* <code>timeout</code> - number of milliseconds to wait when starting Xvfb before assuming it failed to start, defaults to 2000.
* <code>silent</code> - don't pipe Xvfb stderr to the process's stderr.
* <code>xvfb_args</code> - Extra arguments to pass to `Xvfb`.
* <code>onStderrData</code> - Function to receive `stderr` output

### Debugging

Run with `DEBUG=xvfb` environment variable to see debug messages. If you want
to see log messages from the Xvfb process itself, use `DEBUG=xvfb,xvfb-process`.

### Thanks to

Forked from [node-xvfb](https://github.com/Rob--W/node-xvfb)

* [kesla](https://github.com/kesla) for https://github.com/kesla/node-headless
* [leonid-shevtsov](https://github.com/leonid-shevtsov) for https://github.com/leonid-shevtsov/headless
* [paulbaumgart](https://github.com/paulbaumgart) for creating the initial version of this package.

both of which served as inspiration for this package.
# mime-db

[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Node.js Version][node-image]][node-url]
[![Build Status][travis-image]][travis-url]
[![Coverage Status][coveralls-image]][coveralls-url]

This is a database of all mime types.
It consists of a single, public JSON file and does not include any logic,
allowing it to remain as un-opinionated as possible with an API.
It aggregates data from the following sources:

- http://www.iana.org/assignments/media-types/media-types.xhtml
- http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types
- http://hg.nginx.org/nginx/raw-file/default/conf/mime.types

## Installation

```bash
npm install mime-db
```

### Database Download

If you're crazy enough to use this in the browser, you can just grab the
JSON file using [RawGit](https://rawgit.com/). It is recommended to replace
`master` with [a release tag](https://github.com/jshttp/mime-db/tags) as the
JSON format may change in the future.

```
https://cdn.rawgit.com/jshttp/mime-db/master/db.json
```

## Usage

```js
var db = require('mime-db');

// grab data on .js files
var data = db['application/javascript'];
```

## Data Structure

The JSON file is a map lookup for lowercased mime types.
Each mime type has the following properties:

- `.source` - where the mime type is defined.
    If not set, it's probably a custom media type.
    - `apache` - [Apache common media types](http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types)
    - `iana` - [IANA-defined media types](http://www.iana.org/assignments/media-types/media-types.xhtml)
    - `nginx` - [nginx media types](http://hg.nginx.org/nginx/raw-file/default/conf/mime.types)
- `.extensions[]` - known extensions associated with this mime type.
- `.compressible` - whether a file of this type can be gzipped.
- `.charset` - the default charset associated with this type, if any.

If unknown, every property could be `undefined`.

## Contributing

To edit the database, only make PRs against `src/custom.json` or
`src/custom-suffix.json`.

The `src/custom.json` file is a JSON object with the MIME type as the keys
and the values being an object with the following keys:

- `compressible` - leave out if you don't know, otherwise `true`/`false` to
  indicate whether the data represented by the type is typically compressible.
- `extensions` - include an array of file extensions that are associated with
  the type.
- `notes` - human-readable notes about the type, typically what the type is.
- `sources` - include an array of URLs of where the MIME type and the associated
  extensions are sourced from. This needs to be a [primary source](https://en.wikipedia.org/wiki/Primary_source);
  links to type aggregating sites and Wikipedia are _not acceptable_.

To update the build, run `npm run build`.

## Adding Custom Media Types

The best way to get new media types included in this library is to register
them with the IANA. The community registration procedure is outlined in
[RFC 6838 section 5](http://tools.ietf.org/html/rfc6838#section-5). Types
registered with the IANA are automatically pulled into this library.

[npm-version-image]: https://img.shields.io/npm/v/mime-db.svg
[npm-downloads-image]: https://img.shields.io/npm/dm/mime-db.svg
[npm-url]: https://npmjs.org/package/mime-db
[travis-image]: https://img.shields.io/travis/jshttp/mime-db/master.svg
[travis-url]: https://travis-ci.org/jshttp/mime-db
[coveralls-image]: https://img.shields.io/coveralls/jshttp/mime-db/master.svg
[coveralls-url]: https://coveralls.io/r/jshttp/mime-db?branch=master
[node-image]: https://img.shields.io/node/v/mime-db.svg
[node-url]: https://nodejs.org/en/download/
aws4
----

[![Build Status](https://secure.travis-ci.org/mhart/aws4.png?branch=master)](http://travis-ci.org/mhart/aws4)

A small utility to sign vanilla node.js http(s) request options using Amazon's
[AWS Signature Version 4](http://docs.amazonwebservices.com/general/latest/gr/signature-version-4.html).

Can also be used [in the browser](./browser).

This signature is supported by nearly all Amazon services, including
[S3](http://docs.aws.amazon.com/AmazonS3/latest/API/),
[EC2](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/),
[DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API.html),
[Kinesis](http://docs.aws.amazon.com/kinesis/latest/APIReference/),
[Lambda](http://docs.aws.amazon.com/lambda/latest/dg/API_Reference.html),
[SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/),
[SNS](http://docs.aws.amazon.com/sns/latest/api/),
[IAM](http://docs.aws.amazon.com/IAM/latest/APIReference/),
[STS](http://docs.aws.amazon.com/STS/latest/APIReference/),
[RDS](http://docs.aws.amazon.com/AmazonRDS/latest/APIReference/),
[CloudWatch](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/),
[CloudWatch Logs](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/),
[CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/APIReference/),
[CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/APIReference/),
[CloudTrail](http://docs.aws.amazon.com/awscloudtrail/latest/APIReference/),
[ElastiCache](http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/),
[EMR](http://docs.aws.amazon.com/ElasticMapReduce/latest/API/),
[Glacier](http://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-api.html),
[CloudSearch](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/APIReq.html),
[Elastic Load Balancing](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/APIReference/),
[Elastic Transcoder](http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/api-reference.html),
[CloudFormation](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/),
[Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/api/),
[Storage Gateway](http://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html),
[Data Pipeline](http://docs.aws.amazon.com/datapipeline/latest/APIReference/),
[Direct Connect](http://docs.aws.amazon.com/directconnect/latest/APIReference/),
[Redshift](http://docs.aws.amazon.com/redshift/latest/APIReference/),
[OpsWorks](http://docs.aws.amazon.com/opsworks/latest/APIReference/),
[SES](http://docs.aws.amazon.com/ses/latest/APIReference/),
[SWF](http://docs.aws.amazon.com/amazonswf/latest/apireference/),
[AutoScaling](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/),
[Mobile Analytics](http://docs.aws.amazon.com/mobileanalytics/latest/ug/server-reference.html),
[Cognito Identity](http://docs.aws.amazon.com/cognitoidentity/latest/APIReference/),
[Cognito Sync](http://docs.aws.amazon.com/cognitosync/latest/APIReference/),
[Container Service](http://docs.aws.amazon.com/AmazonECS/latest/APIReference/),
[AppStream](http://docs.aws.amazon.com/appstream/latest/developerguide/appstream-api-rest.html),
[Key Management Service](http://docs.aws.amazon.com/kms/latest/APIReference/),
[Config](http://docs.aws.amazon.com/config/latest/APIReference/),
[CloudHSM](http://docs.aws.amazon.com/cloudhsm/latest/dg/api-ref.html),
[Route53](http://docs.aws.amazon.com/Route53/latest/APIReference/requests-rest.html) and
[Route53 Domains](http://docs.aws.amazon.com/Route53/latest/APIReference/requests-rpc.html).

Indeed, the only AWS services that *don't* support v4 as of 2014-12-30 are
[Import/Export](http://docs.aws.amazon.com/AWSImportExport/latest/DG/api-reference.html) and
[SimpleDB](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API.html)
(they only support [AWS Signature Version 2](https://github.com/mhart/aws2)).

It also provides defaults for a number of core AWS headers and
request parameters, making it very easy to query AWS services, or
build out a fully-featured AWS library.

Example
-------

```javascript
var http  = require('http'),
    https = require('https'),
    aws4  = require('aws4')

// given an options object you could pass to http.request
var opts = {host: 'sqs.us-east-1.amazonaws.com', path: '/?Action=ListQueues'}

// alternatively (as aws4 can infer the host):
opts = {service: 'sqs', region: 'us-east-1', path: '/?Action=ListQueues'}

// alternatively (as us-east-1 is default):
opts = {service: 'sqs', path: '/?Action=ListQueues'}

aws4.sign(opts) // assumes AWS credentials are available in process.env

console.log(opts)
/*
{
  host: 'sqs.us-east-1.amazonaws.com',
  path: '/?Action=ListQueues',
  headers: {
    Host: 'sqs.us-east-1.amazonaws.com',
    'X-Amz-Date': '20121226T061030Z',
    Authorization: 'AWS4-HMAC-SHA256 Credential=ABCDEF/20121226/us-east-1/sqs/aws4_request, ...'
  }
}
*/

// we can now use this to query AWS using the standard node.js http API
http.request(opts, function(res) { res.pipe(process.stdout) }).end()
/*
<?xml version="1.0"?>
<ListQueuesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
...
*/
```

More options
------------

```javascript
// you can also pass AWS credentials in explicitly (otherwise taken from process.env)
aws4.sign(opts, {accessKeyId: '', secretAccessKey: ''})

// can also add the signature to query strings
aws4.sign({service: 's3', path: '/my-bucket?X-Amz-Expires=12345', signQuery: true})

// create a utility function to pipe to stdout (with https this time)
function request(o) { https.request(o, function(res) { res.pipe(process.stdout) }).end(o.body || '') }

// aws4 can infer the HTTP method if a body is passed in
// method will be POST and Content-Type: 'application/x-www-form-urlencoded; charset=utf-8'
request(aws4.sign({service: 'iam', body: 'Action=ListGroups&Version=2010-05-08'}))
/*
<ListGroupsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
...
*/

// can specify any custom option or header as per usual
request(aws4.sign({
  service: 'dynamodb',
  region: 'ap-southeast-2',
  method: 'POST',
  path: '/',
  headers: {
    'Content-Type': 'application/x-amz-json-1.0',
    'X-Amz-Target': 'DynamoDB_20120810.ListTables'
  },
  body: '{}'
}))
/*
{"TableNames":[]}
...
*/

// works with all other services that support Signature Version 4

request(aws4.sign({service: 's3', path: '/', signQuery: true}))
/*
<ListAllMyBucketsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
...
*/

request(aws4.sign({service: 'ec2', path: '/?Action=DescribeRegions&Version=2014-06-15'}))
/*
<DescribeRegionsResponse xmlns="http://ec2.amazonaws.com/doc/2014-06-15/">
...
*/

request(aws4.sign({service: 'sns', path: '/?Action=ListTopics&Version=2010-03-31'}))
/*
<ListTopicsResponse xmlns="http://sns.amazonaws.com/doc/2010-03-31/">
...
*/

request(aws4.sign({service: 'sts', path: '/?Action=GetSessionToken&Version=2011-06-15'}))
/*
<GetSessionTokenResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
...
*/

request(aws4.sign({service: 'cloudsearch', path: '/?Action=ListDomainNames&Version=2013-01-01'}))
/*
<ListDomainNamesResponse xmlns="http://cloudsearch.amazonaws.com/doc/2013-01-01/">
...
*/

request(aws4.sign({service: 'ses', path: '/?Action=ListIdentities&Version=2010-12-01'}))
/*
<ListIdentitiesResponse xmlns="http://ses.amazonaws.com/doc/2010-12-01/">
...
*/

request(aws4.sign({service: 'autoscaling', path: '/?Action=DescribeAutoScalingInstances&Version=2011-01-01'}))
/*
<DescribeAutoScalingInstancesResponse xmlns="http://autoscaling.amazonaws.com/doc/2011-01-01/">
...
*/

request(aws4.sign({service: 'elasticloadbalancing', path: '/?Action=DescribeLoadBalancers&Version=2012-06-01'}))
/*
<DescribeLoadBalancersResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
...
*/

request(aws4.sign({service: 'cloudformation', path: '/?Action=ListStacks&Version=2010-05-15'}))
/*
<ListStacksResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
...
*/

request(aws4.sign({service: 'elasticbeanstalk', path: '/?Action=ListAvailableSolutionStacks&Version=2010-12-01'}))
/*
<ListAvailableSolutionStacksResponse xmlns="http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
...
*/

request(aws4.sign({service: 'rds', path: '/?Action=DescribeDBInstances&Version=2012-09-17'}))
/*
<DescribeDBInstancesResponse xmlns="http://rds.amazonaws.com/doc/2012-09-17/">
...
*/

request(aws4.sign({service: 'monitoring', path: '/?Action=ListMetrics&Version=2010-08-01'}))
/*
<ListMetricsResponse xmlns="http://monitoring.amazonaws.com/doc/2010-08-01/">
...
*/

request(aws4.sign({service: 'redshift', path: '/?Action=DescribeClusters&Version=2012-12-01'}))
/*
<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
...
*/

request(aws4.sign({service: 'cloudfront', path: '/2014-05-31/distribution'}))
/*
<DistributionList xmlns="http://cloudfront.amazonaws.com/doc/2014-05-31/">
...
*/

request(aws4.sign({service: 'elasticache', path: '/?Action=DescribeCacheClusters&Version=2014-07-15'}))
/*
<DescribeCacheClustersResponse xmlns="http://elasticache.amazonaws.com/doc/2014-07-15/">
...
*/

request(aws4.sign({service: 'elasticmapreduce', path: '/?Action=DescribeJobFlows&Version=2009-03-31'}))
/*
<DescribeJobFlowsResponse xmlns="http://elasticmapreduce.amazonaws.com/doc/2009-03-31">
...
*/

request(aws4.sign({service: 'route53', path: '/2013-04-01/hostedzone'}))
/*
<ListHostedZonesResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
...
*/

request(aws4.sign({service: 'appstream', path: '/applications'}))
/*
{"_links":{"curie":[{"href":"http://docs.aws.amazon.com/appstream/latest/...
...
*/

request(aws4.sign({service: 'cognito-sync', path: '/identitypools'}))
/*
{"Count":0,"IdentityPoolUsages":[],"MaxResults":16,"NextToken":null}
...
*/

request(aws4.sign({service: 'elastictranscoder', path: '/2012-09-25/pipelines'}))
/*
{"NextPageToken":null,"Pipelines":[]}
...
*/

request(aws4.sign({service: 'lambda', path: '/2014-11-13/functions/'}))
/*
{"Functions":[],"NextMarker":null}
...
*/

request(aws4.sign({service: 'ecs', path: '/?Action=ListClusters&Version=2014-11-13'}))
/*
<ListClustersResponse xmlns="http://ecs.amazonaws.com/doc/2014-11-13/">
...
*/

request(aws4.sign({service: 'glacier', path: '/-/vaults', headers: {'X-Amz-Glacier-Version': '2012-06-01'}}))
/*
{"Marker":null,"VaultList":[]}
...
*/

request(aws4.sign({service: 'storagegateway', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'StorageGateway_20120630.ListGateways'
}}))
/*
{"Gateways":[]}
...
*/

request(aws4.sign({service: 'datapipeline', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'DataPipeline.ListPipelines'
}}))
/*
{"hasMoreResults":false,"pipelineIdList":[]}
...
*/

request(aws4.sign({service: 'opsworks', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'OpsWorks_20130218.DescribeStacks'
}}))
/*
{"Stacks":[]}
...
*/

request(aws4.sign({service: 'route53domains', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'Route53Domains_v20140515.ListDomains'
}}))
/*
{"Domains":[]}
...
*/

request(aws4.sign({service: 'kinesis', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'Kinesis_20131202.ListStreams'
}}))
/*
{"HasMoreStreams":false,"StreamNames":[]}
...
*/

request(aws4.sign({service: 'cloudtrail', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'CloudTrail_20131101.DescribeTrails'
}}))
/*
{"trailList":[]}
...
*/

request(aws4.sign({service: 'logs', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'Logs_20140328.DescribeLogGroups'
}}))
/*
{"logGroups":[]}
...
*/

request(aws4.sign({service: 'codedeploy', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'CodeDeploy_20141006.ListApplications'
}}))
/*
{"applications":[]}
...
*/

request(aws4.sign({service: 'directconnect', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'OvertureService.DescribeConnections'
}}))
/*
{"connections":[]}
...
*/

request(aws4.sign({service: 'kms', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'TrentService.ListKeys'
}}))
/*
{"Keys":[],"Truncated":false}
...
*/

request(aws4.sign({service: 'config', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'StarlingDoveService.DescribeDeliveryChannels'
}}))
/*
{"DeliveryChannels":[]}
...
*/

request(aws4.sign({service: 'cloudhsm', body: '{}', headers: {
  'Content-Type': 'application/x-amz-json-1.1',
  'X-Amz-Target': 'CloudHsmFrontendService.ListAvailableZones'
}}))
/*
{"AZList":["us-east-1a","us-east-1b","us-east-1c"]}
...
*/

request(aws4.sign({
  service: 'swf',
  body: '{"registrationStatus":"REGISTERED"}',
  headers: {
    'Content-Type': 'application/x-amz-json-1.0',
    'X-Amz-Target': 'SimpleWorkflowService.ListDomains'
  }
}))
/*
{"domainInfos":[]}
...
*/

request(aws4.sign({
  service: 'cognito-identity',
  body: '{"MaxResults": 1}',
  headers: {
    'Content-Type': 'application/x-amz-json-1.1',
    'X-Amz-Target': 'AWSCognitoIdentityService.ListIdentityPools'
  }
}))
/*
{"IdentityPools":[]}
...
*/

request(aws4.sign({
  service: 'mobileanalytics',
  path: '/2014-06-05/events',
  body: JSON.stringify({events:[{
    eventType: 'a',
    timestamp: new Date().toISOString(),
    session: {},
  }]}),
  headers: {
    'Content-Type': 'application/json',
    'X-Amz-Client-Context': JSON.stringify({
      client: {client_id: 'a', app_title: 'a'},
      custom: {},
      env: {platform: 'a'},
      services: {},
    }),
  }
}))
/*
(HTTP 202, empty response)
*/

// Generate CodeCommit Git access password
var signer = new aws4.RequestSigner({
  service: 'codecommit',
  host: 'git-codecommit.us-east-1.amazonaws.com',
  method: 'GIT',
  path: '/v1/repos/MyAwesomeRepo',
})
var password = signer.getDateTime() + 'Z' + signer.signature()
```

API
---

### aws4.sign(requestOptions, [credentials])

This calculates and populates the `Authorization` header of
`requestOptions`, and any other necessary AWS headers and/or request
options. Returns `requestOptions` as a convenience for chaining.

`requestOptions` is an object holding the same options that the node.js
[http.request](http://nodejs.org/docs/latest/api/http.html#http_http_request_options_callback)
function takes.

The following properties of `requestOptions` are used in the signing or
populated if they don't already exist:

- `hostname` or `host` (will be determined from `service` and `region` if not given)
- `method` (will use `'GET'` if not given or `'POST'` if there is a `body`)
- `path` (will use `'/'` if not given)
- `body` (will use `''` if not given)
- `service` (will be calculated from `hostname` or `host` if not given)
- `region` (will be calculated from `hostname` or `host` or use `'us-east-1'` if not given)
- `headers['Host']` (will use `hostname` or `host` or be calculated if not given)
- `headers['Content-Type']` (will use `'application/x-www-form-urlencoded; charset=utf-8'`
  if not given and there is a `body`)
- `headers['Date']` (used to calculate the signature date if given, otherwise `new Date` is used)

Your AWS credentials (which can be found in your
[AWS console](https://portal.aws.amazon.com/gp/aws/securityCredentials))
can be specified in one of two ways:

- As the second argument, like this:

```javascript
aws4.sign(requestOptions, {
  secretAccessKey: "<your-secret-access-key>",
  accessKeyId: "<your-access-key-id>",
  sessionToken: "<your-session-token>"
})
```

- From `process.env`, such as this:

```
export AWS_SECRET_ACCESS_KEY="<your-secret-access-key>"
export AWS_ACCESS_KEY_ID="<your-access-key-id>"
export AWS_SESSION_TOKEN="<your-session-token>"
```

(will also use `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` if available)

The `sessionToken` property and `AWS_SESSION_TOKEN` environment variable are optional for signing
with [IAM STS temporary credentials](http://docs.aws.amazon.com/STS/latest/UsingSTS/using-temp-creds.html).

Installation
------------

With [npm](http://npmjs.org/) do:

```
npm install aws4
```

Can also be used [in the browser](./browser).

Thanks
------

Thanks to [@jed](https://github.com/jed) for his
[dynamo-client](https://github.com/jed/dynamo-client) lib where I first
committed and subsequently extracted this code.

Also thanks to the
[official node.js AWS SDK](https://github.com/aws/aws-sdk-js) for giving
me a start on implementing the v4 signature.

# asynckit [![NPM Module](https://img.shields.io/npm/v/asynckit.svg?style=flat)](https://www.npmjs.com/package/asynckit)

Minimal async jobs utility library, with streams support.

[![PhantomJS Build](https://img.shields.io/travis/alexindigo/asynckit/v0.4.0.svg?label=browser&style=flat)](https://travis-ci.org/alexindigo/asynckit)
[![Linux Build](https://img.shields.io/travis/alexindigo/asynckit/v0.4.0.svg?label=linux:0.12-6.x&style=flat)](https://travis-ci.org/alexindigo/asynckit)
[![Windows Build](https://img.shields.io/appveyor/ci/alexindigo/asynckit/v0.4.0.svg?label=windows:0.12-6.x&style=flat)](https://ci.appveyor.com/project/alexindigo/asynckit)

[![Coverage Status](https://img.shields.io/coveralls/alexindigo/asynckit/v0.4.0.svg?label=code+coverage&style=flat)](https://coveralls.io/github/alexindigo/asynckit?branch=master)
[![Dependency Status](https://img.shields.io/david/alexindigo/asynckit/v0.4.0.svg?style=flat)](https://david-dm.org/alexindigo/asynckit)
[![bitHound Overall Score](https://www.bithound.io/github/alexindigo/asynckit/badges/score.svg)](https://www.bithound.io/github/alexindigo/asynckit)

<!-- [![Readme](https://img.shields.io/badge/readme-tested-brightgreen.svg?style=flat)](https://www.npmjs.com/package/reamde) -->

AsyncKit provides harness for `parallel` and `serial` iterators over list of items represented by arrays or objects.
Optionally it accepts abort function (should be synchronously return by iterator for each item), and terminates left over jobs upon an error event. For specific iteration order built-in (`ascending` and `descending`) and custom sort helpers also supported, via `asynckit.serialOrdered` method.

It ensures async operations to keep behavior more stable and prevent `Maximum call stack size exceeded` errors, from sync iterators.

| compression        |     size |
| :----------------- | -------: |
| asynckit.js        | 12.34 kB |
| asynckit.min.js    |  4.11 kB |
| asynckit.min.js.gz |  1.47 kB |


## Install

```sh
$ npm install --save asynckit
```

## Examples

### Parallel Jobs

Runs iterator over provided array in parallel. Stores output in the `result` array,
on the matching positions. In unlikely event of an error from one of the jobs,
will terminate rest of the active jobs (if abort function is provided)
and return error along with salvaged data to the main callback function.

#### Input Array

```javascript
var parallel = require('asynckit').parallel
  , assert   = require('assert')
  ;

var source         = [ 1, 1, 4, 16, 64, 32, 8, 2 ]
  , expectedResult = [ 2, 2, 8, 32, 128, 64, 16, 4 ]
  , expectedTarget = [ 1, 1, 2, 4, 8, 16, 32, 64 ]
  , target         = []
  ;

parallel(source, asyncJob, function(err, result)
{
  assert.deepEqual(result, expectedResult);
  assert.deepEqual(target, expectedTarget);
});

// async job accepts one element from the array
// and a callback function
function asyncJob(item, cb)
{
  // different delays (in ms) per item
  var delay = item * 25;

  // pretend different jobs take different time to finish
  // and not in consequential order
  var timeoutId = setTimeout(function() {
    target.push(item);
    cb(null, item * 2);
  }, delay);

  // allow to cancel "leftover" jobs upon error
  // return function, invoking of which will abort this job
  return clearTimeout.bind(null, timeoutId);
}
```

More examples could be found in [test/test-parallel-array.js](test/test-parallel-array.js).

#### Input Object

Also it supports named jobs, listed via object.

```javascript
var parallel = require('asynckit/parallel')
  , assert   = require('assert')
  ;

var source         = { first: 1, one: 1, four: 4, sixteen: 16, sixtyFour: 64, thirtyTwo: 32, eight: 8, two: 2 }
  , expectedResult = { first: 2, one: 2, four: 8, sixteen: 32, sixtyFour: 128, thirtyTwo: 64, eight: 16, two: 4 }
  , expectedTarget = [ 1, 1, 2, 4, 8, 16, 32, 64 ]
  , expectedKeys   = [ 'first', 'one', 'two', 'four', 'eight', 'sixteen', 'thirtyTwo', 'sixtyFour' ]
  , target         = []
  , keys           = []
  ;

parallel(source, asyncJob, function(err, result)
{
  assert.deepEqual(result, expectedResult);
  assert.deepEqual(target, expectedTarget);
  assert.deepEqual(keys, expectedKeys);
});

// supports full value, key, callback (shortcut) interface
function asyncJob(item, key, cb)
{
  // different delays (in ms) per item
  var delay = item * 25;

  // pretend different jobs take different time to finish
  // and not in consequential order
  var timeoutId = setTimeout(function() {
    keys.push(key);
    target.push(item);
    cb(null, item * 2);
  }, delay);

  // allow to cancel "leftover" jobs upon error
  // return function, invoking of which will abort this job
  return clearTimeout.bind(null, timeoutId);
}
```

More examples could be found in [test/test-parallel-object.js](test/test-parallel-object.js).

### Serial Jobs

Runs iterator over provided array sequentially. Stores output in the `result` array,
on the matching positions. In unlikely event of an error from one of the jobs,
will not proceed to the rest of the items in the list
and return error along with salvaged data to the main callback function.

#### Input Array

```javascript
var serial = require('asynckit/serial')
  , assert = require('assert')
  ;

var source         = [ 1, 1, 4, 16, 64, 32, 8, 2 ]
  , expectedResult = [ 2, 2, 8, 32, 128, 64, 16, 4 ]
  , expectedTarget = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
  , target         = []
  ;

serial(source, asyncJob, function(err, result)
{
  assert.deepEqual(result, expectedResult);
  assert.deepEqual(target, expectedTarget);
});

// extended interface (item, key, callback)
// also supported for arrays
function asyncJob(item, key, cb)
{
  target.push(key);

  // it will be automatically made async
  // even it iterator "returns" in the same event loop
  cb(null, item * 2);
}
```

More examples could be found in [test/test-serial-array.js](test/test-serial-array.js).

#### Input Object

Also it supports named jobs, listed via object.

```javascript
var serial = require('asynckit').serial
  , assert = require('assert')
  ;

var source         = [ 1, 1, 4, 16, 64, 32, 8, 2 ]
  , expectedResult = [ 2, 2, 8, 32, 128, 64, 16, 4 ]
  , expectedTarget = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
  , target         = []
  ;

var source         = { first: 1, one: 1, four: 4, sixteen: 16, sixtyFour: 64, thirtyTwo: 32, eight: 8, two: 2 }
  , expectedResult = { first: 2, one: 2, four: 8, sixteen: 32, sixtyFour: 128, thirtyTwo: 64, eight: 16, two: 4 }
  , expectedTarget = [ 1, 1, 4, 16, 64, 32, 8, 2 ]
  , target         = []
  ;


serial(source, asyncJob, function(err, result)
{
  assert.deepEqual(result, expectedResult);
  assert.deepEqual(target, expectedTarget);
});

// shortcut interface (item, callback)
// works for object as well as for the arrays
function asyncJob(item, cb)
{
  target.push(item);

  // it will be automatically made async
  // even it iterator "returns" in the same event loop
  cb(null, item * 2);
}
```

More examples could be found in [test/test-serial-object.js](test/test-serial-object.js).

_Note: Since _object_ is an _unordered_ collection of properties,
it may produce unexpected results with sequential iterations.
Whenever order of the jobs' execution is important please use `serialOrdered` method._

### Ordered Serial Iterations

TBD

For example [compare-property](compare-property) package.

### Streaming interface

TBD

## Want to Know More?

More examples can be found in [test folder](test/).

Or open an [issue](https://github.com/alexindigo/asynckit/issues) with questions and/or suggestions.

## License

AsyncKit is licensed under the MIT license.
Port of the OpenBSD `bcrypt_pbkdf` function to pure Javascript. `npm`-ified
version of [Devi Mandiri's port](https://github.com/devi/tmp/blob/master/js/bcrypt_pbkdf.js),
with some minor performance improvements. The code is copied verbatim (and
un-styled) from Devi's work.

This product includes software developed by Niels Provos.

## API

### `bcrypt_pbkdf.pbkdf(pass, passlen, salt, saltlen, key, keylen, rounds)`

Derive a cryptographic key of arbitrary length from a given password and salt,
using the OpenBSD `bcrypt_pbkdf` function. This is a combination of Blowfish and
SHA-512.

See [this article](http://www.tedunangst.com/flak/post/bcrypt-pbkdf) for
further information.

Parameters:

 * `pass`, a Uint8Array of length `passlen`
 * `passlen`, an integer Number
 * `salt`, a Uint8Array of length `saltlen`
 * `saltlen`, an integer Number
 * `key`, a Uint8Array of length `keylen`, will be filled with output
 * `keylen`, an integer Number
 * `rounds`, an integer Number, number of rounds of the PBKDF to run

### `bcrypt_pbkdf.hash(sha2pass, sha2salt, out)`

Calculate a Blowfish hash, given SHA2-512 output of a password and salt. Used as
part of the inner round function in the PBKDF.

Parameters:

 * `sha2pass`, a Uint8Array of length 64
 * `sha2salt`, a Uint8Array of length 64
 * `out`, a Uint8Array of length 32, will be filled with output

## License

This source form is a 1:1 port from the OpenBSD `blowfish.c` and `bcrypt_pbkdf.c`.
As a result, it retains the original copyright and license. The two files are
under slightly different (but compatible) licenses, and are here combined in
one file. For each of the full license texts see `LICENSE`.
# fd-slicer

[![Build Status](https://travis-ci.org/andrewrk/node-fd-slicer.svg?branch=master)](https://travis-ci.org/andrewrk/node-fd-slicer)
[![Coverage Status](https://img.shields.io/coveralls/andrewrk/node-fd-slicer.svg)](https://coveralls.io/r/andrewrk/node-fd-slicer)

Safe `fs.ReadStream` and `fs.WriteStream` using the same fd.

Let's say that you want to perform a parallel upload of a file to a remote
server. To do this, we want to create multiple read streams. The first thing
you might think of is to use the `{start: 0, end: 0}` API of
`fs.createReadStream`. This gives you two choices:

 0. Use the same file descriptor for all `fs.ReadStream` objects.
 0. Open the file multiple times, resulting in a separate file descriptor
    for each read stream.

Neither of these are acceptable options. The first one is a severe bug,
because the API docs for `fs.write` state:

> Note that it is unsafe to use `fs.write` multiple times on the same file
> without waiting for the callback. For this scenario, `fs.createWriteStream`
> is strongly recommended.

`fs.createWriteStream` will solve the problem if you only create one of them
for the file descriptor, but it will exhibit this unsafety if you create
multiple write streams per file descriptor.

The second option suffers from a race condition. For each additional time the
file is opened after the first, it is possible that the file is modified. So
in our parallel uploading example, we might upload a corrupt file that never
existed on the client's computer.

This module solves this problem by providing `createReadStream` and
`createWriteStream` that operate on a shared file descriptor and provides
the convenient stream API while still allowing slicing and dicing.

This module also gives you some additional power that the builtin
`fs.createWriteStream` do not give you. These features are:

 * Emitting a 'progress' event on write.
 * Ability to set a maximum size and emit an error if this size is exceeded.
 * Ability to create an `FdSlicer` instance from a `Buffer`. This enables you
   to provide API for handling files as well as buffers using the same API.

## Usage

```js
var fdSlicer = require('fd-slicer');
var fs = require('fs');

fs.open("file.txt", 'r', function(err, fd) {
  if (err) throw err;
  var slicer = fdSlicer.createFromFd(fd);
  var firstPart = slicer.createReadStream({start: 0, end: 100});
  var secondPart = slicer.createReadStream({start: 100});
  var firstOut = fs.createWriteStream("first.txt");
  var secondOut = fs.createWriteStream("second.txt");
  firstPart.pipe(firstOut);
  secondPart.pipe(secondOut);
});
```

You can also create from a buffer:

```js
var fdSlicer = require('fd-slicer');
var slicer = FdSlicer.createFromBuffer(someBuffer);
var firstPart = slicer.createReadStream({start: 0, end: 100});
var secondPart = slicer.createReadStream({start: 100});
var firstOut = fs.createWriteStream("first.txt");
var secondOut = fs.createWriteStream("second.txt");
firstPart.pipe(firstOut);
secondPart.pipe(secondOut);
```

## API Documentation

### fdSlicer.createFromFd(fd, [options])

```js
var fdSlicer = require('fd-slicer');
fs.open("file.txt", 'r', function(err, fd) {
  if (err) throw err;
  var slicer = fdSlicer.createFromFd(fd);
  // ...
});
```

Make sure `fd` is a properly initialized file descriptor. If you want to
use `createReadStream` make sure you open it for reading and if you want
to use `createWriteStream` make sure you open it for writing.

`options` is an optional object which can contain:

 * `autoClose` - if set to `true`, the file descriptor will be automatically
   closed once the last stream that references it is closed. Defaults to
   `false`. `ref()` and `unref()` can be used to increase or decrease the
   reference count, respectively.

### fdSlicer.createFromBuffer(buffer)

```js
var fdSlicer = require('fd-slicer');
var slicer = fdSlicer.createFromBuffer(someBuffer);
// ...
```

#### Properties

##### fd

The file descriptor passed in. `undefined` if created from a buffer.

#### Methods

##### createReadStream(options)

Available `options`:

 * `start` - Number. The offset into the file to start reading from. Defaults
   to 0.
 * `end` - Number. Exclusive upper bound offset into the file to stop reading
   from.
 * `highWaterMark` - Number. The maximum number of bytes to store in the
   internal buffer before ceasing to read from the underlying resource.
   Defaults to 16 KB.
 * `encoding` - String. If specified, then buffers will be decoded to strings
   using the specified encoding. Defaults to `null`.

The ReadableStream that this returns has these additional methods:

 * `destroy(err)` - stop streaming. `err` is optional and is the error that
   will be emitted in order to cause the streaming to stop. Defaults to
   `new Error("stream destroyed")`.

##### createWriteStream(options)

Available `options`:

 * `start` - Number. The offset into the file to start writing to. Defaults to
   0.
 * `end` - Number. Exclusive upper bound offset into the file. If this offset
   is reached, the write stream will emit an 'error' event and stop functioning.
   In this situation, `err.code === 'ETOOBIG'`. Defaults to `Infinity`.
 * `highWaterMark` - Number. Buffer level when `write()` starts returning
   false. Defaults to 16KB.
 * `decodeStrings` - Boolean. Whether or not to decode strings into Buffers
   before passing them to` _write()`. Defaults to `true`.

The WritableStream that this returns has these additional methods:

 * `destroy()` - stop streaming

And these additional properties:

 * `bytesWritten` - number of bytes written to the stream

And these additional events:

 * 'progress' - emitted when `bytesWritten` changes.

##### read(buffer, offset, length, position, callback)

Equivalent to `fs.read`, but with concurrency protection.
`callback` must be defined.

##### write(buffer, offset, length, position, callback)

Equivalent to `fs.write`, but with concurrency protection.
`callback` must be defined.

##### ref()

Increase the `autoClose` reference count by 1.

##### unref()

Decrease the `autoClose` reference count by 1.

#### Events

##### 'error'

Emitted if `fs.close` returns an error when auto closing.

##### 'close'

Emitted when fd-slicer closes the file descriptor due to `autoClose`. Never
emitted if created from a buffer.
## getpass

Get a password from the terminal. Sounds simple? Sounds like the `readline`
module should be able to do it? NOPE.

## Install and use it

```bash
npm install --save getpass
```

```javascript
const mod_getpass = require('getpass');
```

## API

### `mod_getpass.getPass([options, ]callback)`

Gets a password from the terminal. If available, this uses `/dev/tty` to avoid
interfering with any data being piped in or out of stdio.

This function prints a prompt (by default `Password:`) and then accepts input
without echoing.

Parameters:

 * `options`, an Object, with properties:
   * `prompt`, an optional String
 * `callback`, a `Func(error, password)`, with arguments:
   * `error`, either `null` (no error) or an `Error` instance
   * `password`, a String
<!--
  -- This file is auto-generated from README_js.md. Changes should be made there.
  -->

# uuid [![Build Status](https://secure.travis-ci.org/kelektiv/node-uuid.svg?branch=master)](http://travis-ci.org/kelektiv/node-uuid) #

Simple, fast generation of [RFC4122](http://www.ietf.org/rfc/rfc4122.txt) UUIDS.

Features:

* Support for version 1, 3, 4 and 5 UUIDs
* Cross-platform
* Uses cryptographically-strong random number APIs (when available)
* Zero-dependency, small footprint (... but not [this small](https://gist.github.com/982883))

[**Deprecation warning**: The use of `require('uuid')` is deprecated and will not be
supported after version 3.x of this module.  Instead, use `require('uuid/[v1|v3|v4|v5]')` as shown in the examples below.]

## Quickstart - CommonJS (Recommended)

```shell
npm install uuid
```

Then generate your uuid version of choice ...

Version 1 (timestamp):

```javascript
const uuidv1 = require('uuid/v1');
uuidv1(); // ⇨ '45745c60-7b1a-11e8-9c9c-2d42b21b1a3e'

```

Version 3 (namespace):

```javascript
const uuidv3 = require('uuid/v3');

// ... using predefined DNS namespace (for domain names)
uuidv3('hello.example.com', uuidv3.DNS); // ⇨ '9125a8dc-52ee-365b-a5aa-81b0b3681cf6'

// ... using predefined URL namespace (for, well, URLs)
uuidv3('http://example.com/hello', uuidv3.URL); // ⇨ 'c6235813-3ba4-3801-ae84-e0a6ebb7d138'

// ... using a custom namespace
//
// Note: Custom namespaces should be a UUID string specific to your application!
// E.g. the one here was generated using this modules `uuid` CLI.
const MY_NAMESPACE = '1b671a64-40d5-491e-99b0-da01ff1f3341';
uuidv3('Hello, World!', MY_NAMESPACE); // ⇨ 'e8b5a51d-11c8-3310-a6ab-367563f20686'

```

Version 4 (random):

```javascript
const uuidv4 = require('uuid/v4');
uuidv4(); // ⇨ '10ba038e-48da-487b-96e8-8d3b99b6d18a'

```

Version 5 (namespace):

```javascript
const uuidv5 = require('uuid/v5');

// ... using predefined DNS namespace (for domain names)
uuidv5('hello.example.com', uuidv5.DNS); // ⇨ 'fdda765f-fc57-5604-a269-52a7df8164ec'

// ... using predefined URL namespace (for, well, URLs)
uuidv5('http://example.com/hello', uuidv5.URL); // ⇨ '3bbcee75-cecc-5b56-8031-b6641c1ed1f1'

// ... using a custom namespace
//
// Note: Custom namespaces should be a UUID string specific to your application!
// E.g. the one here was generated using this modules `uuid` CLI.
const MY_NAMESPACE = '1b671a64-40d5-491e-99b0-da01ff1f3341';
uuidv5('Hello, World!', MY_NAMESPACE); // ⇨ '630eb68f-e0fa-5ecc-887a-7c7a62614681'

```

## Quickstart - Browser-ready Versions

Browser-ready versions of this module are available via [wzrd.in](https://github.com/jfhbrook/wzrd.in).

For version 1 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv1@latest"></script>
<script>
uuidv1(); // -> v1 UUID
</script>
```

For version 3 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv3@latest"></script>
<script>
uuidv3('http://example.com/hello', uuidv3.URL); // -> v3 UUID
</script>
```

For version 4 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv4@latest"></script>
<script>
uuidv4(); // -> v4 UUID
</script>
```

For version 5 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv5@latest"></script>
<script>
uuidv5('http://example.com/hello', uuidv5.URL); // -> v5 UUID
</script>
```

## API

### Version 1

```javascript
const uuidv1 = require('uuid/v1');

// Incantations
uuidv1();
uuidv1(options);
uuidv1(options, buffer, offset);
```

Generate and return a RFC4122 v1 (timestamp-based) UUID.

* `options` - (Object) Optional uuid state to apply. Properties may include:

  * `node` - (Array) Node id as Array of 6 bytes (per 4.1.6). Default: Randomly generated ID.  See note 1.
  * `clockseq` - (Number between 0 - 0x3fff) RFC clock sequence.  Default: An internally maintained clockseq is used.
  * `msecs` - (Number) Time in milliseconds since unix Epoch.  Default: The current time is used.
  * `nsecs` - (Number between 0-9999) additional time, in 100-nanosecond units. Ignored if `msecs` is unspecified. Default: internal uuid counter is used, as per 4.2.1.2.

* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing.

Returns `buffer`, if specified, otherwise the string form of the UUID

Note: The <node> id is generated guaranteed to stay constant for the lifetime of the current JS runtime. (Future versions of this module may use persistent storage mechanisms to extend this guarantee.)

Example: Generate string UUID with fully-specified options

```javascript
const v1options = {
  node: [0x01, 0x23, 0x45, 0x67, 0x89, 0xab],
  clockseq: 0x1234,
  msecs: new Date('2011-11-01').getTime(),
  nsecs: 5678
};
uuidv1(v1options); // ⇨ '710b962e-041c-11e1-9234-0123456789ab'

```

Example: In-place generation of two binary IDs

```javascript
// Generate two ids in an array
const arr = new Array();
uuidv1(null, arr, 0);  // ⇨ [ 69, 117, 109, 208, 123, 26, 17, 232, 146, 52, 45, 66, 178, 27, 26, 62 ]
uuidv1(null, arr, 16); // ⇨ [ 69, 117, 109, 208, 123, 26, 17, 232, 146, 52, 45, 66, 178, 27, 26, 62, 69, 117, 109, 209, 123, 26, 17, 232, 146, 52, 45, 66, 178, 27, 26, 62 ]

```

### Version 3

```javascript
const uuidv3 = require('uuid/v3');

// Incantations
uuidv3(name, namespace);
uuidv3(name, namespace, buffer);
uuidv3(name, namespace, buffer, offset);
```

Generate and return a RFC4122 v3 UUID.

* `name` - (String | Array[]) "name" to create UUID with
* `namespace` - (String | Array[]) "namespace" UUID either as a String or Array[16] of byte values
* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing. Default = 0

Returns `buffer`, if specified, otherwise the string form of the UUID

Example:

```javascript
uuidv3('hello world', MY_NAMESPACE);  // ⇨ '042ffd34-d989-321c-ad06-f60826172424'

```

### Version 4

```javascript
const uuidv4 = require('uuid/v4')

// Incantations
uuidv4();
uuidv4(options);
uuidv4(options, buffer, offset);
```

Generate and return a RFC4122 v4 UUID.

* `options` - (Object) Optional uuid state to apply. Properties may include:
  * `random` - (Number[16]) Array of 16 numbers (0-255) to use in place of randomly generated values
  * `rng` - (Function) Random # generator function that returns an Array[16] of byte values (0-255)
* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing.

Returns `buffer`, if specified, otherwise the string form of the UUID

Example: Generate string UUID with predefined `random` values

```javascript
const v4options = {
  random: [
    0x10, 0x91, 0x56, 0xbe, 0xc4, 0xfb, 0xc1, 0xea,
    0x71, 0xb4, 0xef, 0xe1, 0x67, 0x1c, 0x58, 0x36
  ]
};
uuidv4(v4options); // ⇨ '109156be-c4fb-41ea-b1b4-efe1671c5836'

```

Example: Generate two IDs in a single buffer

```javascript
const buffer = new Array();
uuidv4(null, buffer, 0);  // ⇨ [ 54, 122, 218, 70, 45, 70, 65, 24, 171, 53, 95, 130, 83, 195, 242, 45 ]
uuidv4(null, buffer, 16); // ⇨ [ 54, 122, 218, 70, 45, 70, 65, 24, 171, 53, 95, 130, 83, 195, 242, 45, 108, 204, 255, 103, 171, 86, 76, 94, 178, 225, 188, 236, 150, 20, 151, 87 ]

```

### Version 5

```javascript
const uuidv5 = require('uuid/v5');

// Incantations
uuidv5(name, namespace);
uuidv5(name, namespace, buffer);
uuidv5(name, namespace, buffer, offset);
```

Generate and return a RFC4122 v5 UUID.

* `name` - (String | Array[]) "name" to create UUID with
* `namespace` - (String | Array[]) "namespace" UUID either as a String or Array[16] of byte values
* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing. Default = 0

Returns `buffer`, if specified, otherwise the string form of the UUID

Example:

```javascript
uuidv5('hello world', MY_NAMESPACE);  // ⇨ '9f282611-e0fd-5650-8953-89c8e342da0b'

```

## Command Line

UUIDs can be generated from the command line with the `uuid` command.

```shell
$ uuid
ddeb27fb-d9a0-4624-be4d-4615062daed4

$ uuid v1
02d37060-d446-11e7-a9fa-7bdae751ebe1
```

Type `uuid --help` for usage details

## Testing

```shell
npm test
```

----
Markdown generated from [README_js.md](README_js.md) by [![RunMD Logo](http://i.imgur.com/h0FVyzU.png)](https://github.com/broofa/runmd)```javascript --hide
runmd.onRequire = path => path.replace(/^uuid/, './');
```

# uuid [![Build Status](https://secure.travis-ci.org/kelektiv/node-uuid.svg?branch=master)](http://travis-ci.org/kelektiv/node-uuid) #

Simple, fast generation of [RFC4122](http://www.ietf.org/rfc/rfc4122.txt) UUIDS.

Features:

* Support for version 1, 3, 4 and 5 UUIDs
* Cross-platform
* Uses cryptographically-strong random number APIs (when available)
* Zero-dependency, small footprint (... but not [this small](https://gist.github.com/982883))

[**Deprecation warning**: The use of `require('uuid')` is deprecated and will not be
supported after version 3.x of this module.  Instead, use `require('uuid/[v1|v3|v4|v5]')` as shown in the examples below.]

## Quickstart - CommonJS (Recommended)

```shell
npm install uuid
```

Then generate your uuid version of choice ...

Version 1 (timestamp):

```javascript --run v1
const uuidv1 = require('uuid/v1');
uuidv1(); // RESULT
```

Version 3 (namespace):

```javascript --run v3
const uuidv3 = require('uuid/v3');

// ... using predefined DNS namespace (for domain names)
uuidv3('hello.example.com', uuidv3.DNS); // RESULT

// ... using predefined URL namespace (for, well, URLs)
uuidv3('http://example.com/hello', uuidv3.URL); // RESULT

// ... using a custom namespace
//
// Note: Custom namespaces should be a UUID string specific to your application!
// E.g. the one here was generated using this modules `uuid` CLI.
const MY_NAMESPACE = '1b671a64-40d5-491e-99b0-da01ff1f3341';
uuidv3('Hello, World!', MY_NAMESPACE); // RESULT
```

Version 4 (random):

```javascript --run v4
const uuidv4 = require('uuid/v4');
uuidv4(); // RESULT
```

Version 5 (namespace):

```javascript --run v5
const uuidv5 = require('uuid/v5');

// ... using predefined DNS namespace (for domain names)
uuidv5('hello.example.com', uuidv5.DNS); // RESULT

// ... using predefined URL namespace (for, well, URLs)
uuidv5('http://example.com/hello', uuidv5.URL); // RESULT

// ... using a custom namespace
//
// Note: Custom namespaces should be a UUID string specific to your application!
// E.g. the one here was generated using this modules `uuid` CLI.
const MY_NAMESPACE = '1b671a64-40d5-491e-99b0-da01ff1f3341';
uuidv5('Hello, World!', MY_NAMESPACE); // RESULT
```

## Quickstart - Browser-ready Versions

Browser-ready versions of this module are available via [wzrd.in](https://github.com/jfhbrook/wzrd.in).

For version 1 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv1@latest"></script>
<script>
uuidv1(); // -> v1 UUID
</script>
```

For version 3 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv3@latest"></script>
<script>
uuidv3('http://example.com/hello', uuidv3.URL); // -> v3 UUID
</script>
```

For version 4 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv4@latest"></script>
<script>
uuidv4(); // -> v4 UUID
</script>
```

For version 5 uuids:

```html
<script src="http://wzrd.in/standalone/uuid%2Fv5@latest"></script>
<script>
uuidv5('http://example.com/hello', uuidv5.URL); // -> v5 UUID
</script>
```

## API

### Version 1

```javascript
const uuidv1 = require('uuid/v1');

// Incantations
uuidv1();
uuidv1(options);
uuidv1(options, buffer, offset);
```

Generate and return a RFC4122 v1 (timestamp-based) UUID.

* `options` - (Object) Optional uuid state to apply. Properties may include:

  * `node` - (Array) Node id as Array of 6 bytes (per 4.1.6). Default: Randomly generated ID.  See note 1.
  * `clockseq` - (Number between 0 - 0x3fff) RFC clock sequence.  Default: An internally maintained clockseq is used.
  * `msecs` - (Number) Time in milliseconds since unix Epoch.  Default: The current time is used.
  * `nsecs` - (Number between 0-9999) additional time, in 100-nanosecond units. Ignored if `msecs` is unspecified. Default: internal uuid counter is used, as per 4.2.1.2.

* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing.

Returns `buffer`, if specified, otherwise the string form of the UUID

Note: The <node> id is generated guaranteed to stay constant for the lifetime of the current JS runtime. (Future versions of this module may use persistent storage mechanisms to extend this guarantee.)

Example: Generate string UUID with fully-specified options

```javascript --run v1
const v1options = {
  node: [0x01, 0x23, 0x45, 0x67, 0x89, 0xab],
  clockseq: 0x1234,
  msecs: new Date('2011-11-01').getTime(),
  nsecs: 5678
};
uuidv1(v1options); // RESULT
```

Example: In-place generation of two binary IDs

```javascript --run v1
// Generate two ids in an array
const arr = new Array();
uuidv1(null, arr, 0);  // RESULT
uuidv1(null, arr, 16); // RESULT
```

### Version 3

```javascript
const uuidv3 = require('uuid/v3');

// Incantations
uuidv3(name, namespace);
uuidv3(name, namespace, buffer);
uuidv3(name, namespace, buffer, offset);
```

Generate and return a RFC4122 v3 UUID.

* `name` - (String | Array[]) "name" to create UUID with
* `namespace` - (String | Array[]) "namespace" UUID either as a String or Array[16] of byte values
* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing. Default = 0

Returns `buffer`, if specified, otherwise the string form of the UUID

Example:

```javascript --run v3
uuidv3('hello world', MY_NAMESPACE);  // RESULT
```

### Version 4

```javascript
const uuidv4 = require('uuid/v4')

// Incantations
uuidv4();
uuidv4(options);
uuidv4(options, buffer, offset);
```

Generate and return a RFC4122 v4 UUID.

* `options` - (Object) Optional uuid state to apply. Properties may include:
  * `random` - (Number[16]) Array of 16 numbers (0-255) to use in place of randomly generated values
  * `rng` - (Function) Random # generator function that returns an Array[16] of byte values (0-255)
* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing.

Returns `buffer`, if specified, otherwise the string form of the UUID

Example: Generate string UUID with predefined `random` values

```javascript --run v4
const v4options = {
  random: [
    0x10, 0x91, 0x56, 0xbe, 0xc4, 0xfb, 0xc1, 0xea,
    0x71, 0xb4, 0xef, 0xe1, 0x67, 0x1c, 0x58, 0x36
  ]
};
uuidv4(v4options); // RESULT
```

Example: Generate two IDs in a single buffer

```javascript --run v4
const buffer = new Array();
uuidv4(null, buffer, 0);  // RESULT
uuidv4(null, buffer, 16); // RESULT
```

### Version 5

```javascript
const uuidv5 = require('uuid/v5');

// Incantations
uuidv5(name, namespace);
uuidv5(name, namespace, buffer);
uuidv5(name, namespace, buffer, offset);
```

Generate and return a RFC4122 v5 UUID.

* `name` - (String | Array[]) "name" to create UUID with
* `namespace` - (String | Array[]) "namespace" UUID either as a String or Array[16] of byte values
* `buffer` - (Array | Buffer) Array or buffer where UUID bytes are to be written.
* `offset` - (Number) Starting index in `buffer` at which to begin writing. Default = 0

Returns `buffer`, if specified, otherwise the string form of the UUID

Example:

```javascript --run v5
uuidv5('hello world', MY_NAMESPACE);  // RESULT
```

## Command Line

UUIDs can be generated from the command line with the `uuid` command.

```shell
$ uuid
ddeb27fb-d9a0-4624-be4d-4615062daed4

$ uuid v1
02d37060-d446-11e7-a9fa-7bdae751ebe1
```

Type `uuid --help` for usage details

## Testing

```shell
npm test
```
# fs.realpath

A backwards-compatible fs.realpath for Node v6 and above

In Node v6, the JavaScript implementation of fs.realpath was replaced
with a faster (but less resilient) native implementation.  That raises
new and platform-specific errors and cannot handle long or excessively
symlink-looping paths.

This module handles those cases by detecting the new errors and
falling back to the JavaScript implementation.  On versions of Node
prior to v6, it has no effect.

## USAGE

```js
var rp = require('fs.realpath')

// async version
rp.realpath(someLongAndLoopingPath, function (er, real) {
  // the ELOOP was handled, but it was a bit slower
})

// sync version
var real = rp.realpathSync(someLongAndLoopingPath)

// monkeypatch at your own risk!
// This replaces the fs.realpath/fs.realpathSync builtins
rp.monkeypatch()

// un-do the monkeypatching
rp.unmonkeypatch()
```
<img align="right" alt="Ajv logo" width="160" src="http://epoberezkin.github.io/ajv/images/ajv_logo.png">

# Ajv: Another JSON Schema Validator

The fastest JSON Schema validator for Node.js and browser with draft 6 support.


[![Build Status](https://travis-ci.org/epoberezkin/ajv.svg?branch=master)](https://travis-ci.org/epoberezkin/ajv)
[![npm version](https://badge.fury.io/js/ajv.svg)](https://www.npmjs.com/package/ajv)
[![npm@beta](https://img.shields.io/npm/v/ajv/beta.svg)](https://github.com/epoberezkin/ajv/tree/beta)
[![npm downloads](https://img.shields.io/npm/dm/ajv.svg)](https://www.npmjs.com/package/ajv)
[![Coverage Status](https://coveralls.io/repos/epoberezkin/ajv/badge.svg?branch=master&service=github)](https://coveralls.io/github/epoberezkin/ajv?branch=master)
[![Greenkeeper badge](https://badges.greenkeeper.io/epoberezkin/ajv.svg)](https://greenkeeper.io/)
[![Gitter](https://img.shields.io/gitter/room/ajv-validator/ajv.svg)](https://gitter.im/ajv-validator/ajv)


__Please note__: Ajv [version 6](https://github.com/epoberezkin/ajv/tree/beta) with [JSON Schema draft-07](http://json-schema.org/work-in-progress) support is released. Use `npm install ajv@beta` to install.


## Using version 5

[JSON Schema draft-06](https://trac.tools.ietf.org/html/draft-wright-json-schema-validation-01) is published.

[Ajv version 5.0.0](https://github.com/epoberezkin/ajv/releases/tag/5.0.0) that supports draft-06 is released. It may require either migrating your schemas or updating your code (to continue using draft-04 and v5 schemas).

__Please note__: To use Ajv with draft-04 schemas you need to explicitly add meta-schema to the validator instance:

```javascript
ajv.addMetaSchema(require('ajv/lib/refs/json-schema-draft-04.json'));
```


## Contents

- [Performance](#performance)
- [Features](#features)
- [Getting started](#getting-started)
- [Frequently Asked Questions](https://github.com/epoberezkin/ajv/blob/master/FAQ.md)
- [Using in browser](#using-in-browser)
- [Command line interface](#command-line-interface)
- Validation
  - [Keywords](#validation-keywords)
  - [Formats](#formats)
  - [Combining schemas with $ref](#ref)
  - [$data reference](#data-reference)
  - NEW: [$merge and $patch keywords](#merge-and-patch-keywords)
  - [Defining custom keywords](#defining-custom-keywords)
  - [Asynchronous schema compilation](#asynchronous-schema-compilation)
  - [Asynchronous validation](#asynchronous-validation)
- Modifying data during validation
  - [Filtering data](#filtering-data)
  - [Assigning defaults](#assigning-defaults)
  - [Coercing data types](#coercing-data-types)
- API
  - [Methods](#api)
  - [Options](#options)
  - [Validation errors](#validation-errors)
- [Related packages](#related-packages)
- [Packages using Ajv](#some-packages-using-ajv)
- [Tests, Contributing, History, License](#tests)


## Performance

Ajv generates code using [doT templates](https://github.com/olado/doT) to turn JSON schemas into super-fast validation functions that are efficient for v8 optimization.

Currently Ajv is the fastest and the most standard compliant validator according to these benchmarks:

- [json-schema-benchmark](https://github.com/ebdrup/json-schema-benchmark) - 50% faster than the second place
- [jsck benchmark](https://github.com/pandastrike/jsck#benchmarks) - 20-190% faster
- [z-schema benchmark](https://rawgit.com/zaggino/z-schema/master/benchmark/results.html)
- [themis benchmark](https://cdn.rawgit.com/playlyfe/themis/master/benchmark/results.html)


Performance of different validators by [json-schema-benchmark](https://github.com/ebdrup/json-schema-benchmark):

[![performance](https://chart.googleapis.com/chart?chxt=x,y&cht=bhs&chco=76A4FB&chls=2.0&chbh=32,4,1&chs=600x416&chxl=-1:|djv|ajv|json-schema-validator-generator|jsen|is-my-json-valid|themis|z-schema|jsck|skeemas|json-schema-library|tv4&chd=t:100,98,72.1,66.8,50.1,15.1,6.1,3.8,1.2,0.7,0.2)](https://github.com/ebdrup/json-schema-benchmark/blob/master/README.md#performance)


## Features

- Ajv implements full JSON Schema [draft 6](http://json-schema.org/) and draft 4 standards:
  - all validation keywords (see [JSON Schema validation keywords](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md))
  - full support of remote refs (remote schemas have to be added with `addSchema` or compiled to be available)
  - support of circular references between schemas
  - correct string lengths for strings with unicode pairs (can be turned off)
  - [formats](#formats) defined by JSON Schema draft 4 standard and custom formats (can be turned off)
  - [validates schemas against meta-schema](#api-validateschema)
- supports [browsers](#using-in-browser) and Node.js 0.10-8.x
- [asynchronous loading](#asynchronous-schema-compilation) of referenced schemas during compilation
- "All errors" validation mode with [option allErrors](#options)
- [error messages with parameters](#validation-errors) describing error reasons to allow creating custom error messages
- i18n error messages support with [ajv-i18n](https://github.com/epoberezkin/ajv-i18n) package
- [filtering data](#filtering-data) from additional properties
- [assigning defaults](#assigning-defaults) to missing properties and items
- [coercing data](#coercing-data-types) to the types specified in `type` keywords
- [custom keywords](#defining-custom-keywords)
- draft-6 keywords `const`, `contains` and `propertyNames`
- draft-6 boolean schemas (`true`/`false` as a schema to always pass/fail).
- keywords `switch`, `patternRequired`, `formatMaximum` / `formatMinimum` and `formatExclusiveMaximum` / `formatExclusiveMinimum` from [JSON-schema extension proposals](https://github.com/json-schema/json-schema/wiki/v5-Proposals) with [ajv-keywords](https://github.com/epoberezkin/ajv-keywords) package
- [$data reference](#data-reference) to use values from the validated data as values for the schema keywords
- [asynchronous validation](#asynchronous-validation) of custom formats and keywords

Currently Ajv is the only validator that passes all the tests from [JSON Schema Test Suite](https://github.com/json-schema/JSON-Schema-Test-Suite) (according to [json-schema-benchmark](https://github.com/ebdrup/json-schema-benchmark), apart from the test that requires that `1.0` is not an integer that is impossible to satisfy in JavaScript).


## Install

```
npm install ajv
```

or to install [version 6](https://github.com/epoberezkin/ajv/tree/beta):

```
npm install ajv@beta
```


## <a name="usage"></a>Getting started

Try it in the Node.js REPL: https://tonicdev.com/npm/ajv


The fastest validation call:

```javascript
var Ajv = require('ajv');
var ajv = new Ajv(); // options can be passed, e.g. {allErrors: true}
var validate = ajv.compile(schema);
var valid = validate(data);
if (!valid) console.log(validate.errors);
```

or with less code

```javascript
// ...
var valid = ajv.validate(schema, data);
if (!valid) console.log(ajv.errors);
// ...
```

or

```javascript
// ...
var valid = ajv.addSchema(schema, 'mySchema')
               .validate('mySchema', data);
if (!valid) console.log(ajv.errorsText());
// ...
```

See [API](#api) and [Options](#options) for more details.

Ajv compiles schemas to functions and caches them in all cases (using schema serialized with [fast-json-stable-stringify](https://github.com/epoberezkin/fast-json-stable-stringify) or a custom function as a key), so that the next time the same schema is used (not necessarily the same object instance) it won't be compiled again.

The best performance is achieved when using compiled functions returned by `compile` or `getSchema` methods (there is no additional function call).

__Please note__: every time a validation function or `ajv.validate` are called `errors` property is overwritten. You need to copy `errors` array reference to another variable if you want to use it later (e.g., in the callback). See [Validation errors](#validation-errors)


## Using in browser

You can require Ajv directly from the code you browserify - in this case Ajv will be a part of your bundle.

If you need to use Ajv in several bundles you can create a separate UMD bundle using `npm run bundle` script (thanks to [siddo420](https://github.com/siddo420)).

Then you need to load Ajv in the browser:
```html
<script src="ajv.min.js"></script>
```

This bundle can be used with different module systems; it creates global `Ajv` if no module system is found.

The browser bundle is available on [cdnjs](https://cdnjs.com/libraries/ajv).

Ajv is tested with these browsers:

[![Sauce Test Status](https://saucelabs.com/browser-matrix/epoberezkin.svg)](https://saucelabs.com/u/epoberezkin)

__Please note__: some frameworks, e.g. Dojo, may redefine global require in such way that is not compatible with CommonJS module format. In such case Ajv bundle has to be loaded before the framework and then you can use global Ajv (see issue [#234](https://github.com/epoberezkin/ajv/issues/234)).


## Command line interface

CLI is available as a separate npm package [ajv-cli](https://github.com/jessedc/ajv-cli). It supports:

- compiling JSON-schemas to test their validity
- BETA: generating standalone module exporting a validation function to be used without Ajv (using [ajv-pack](https://github.com/epoberezkin/ajv-pack))
- migrate schemas to draft-06 (using [json-schema-migrate](https://github.com/epoberezkin/json-schema-migrate))
- validating data file(s) against JSON-schema
- testing expected validity of data against JSON-schema
- referenced schemas
- custom meta-schemas
- files in JSON and JavaScript format
- all Ajv options
- reporting changes in data after validation in [JSON-patch](https://tools.ietf.org/html/rfc6902) format


## Validation keywords

Ajv supports all validation keywords from draft 4 of JSON-schema standard:

- [type](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#type)
- [for numbers](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#keywords-for-numbers) - maximum, minimum, exclusiveMaximum, exclusiveMinimum, multipleOf
- [for strings](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#keywords-for-strings) - maxLength, minLength, pattern, format
- [for arrays](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#keywords-for-arrays) - maxItems, minItems, uniqueItems, items, additionalItems, [contains](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#contains)
- [for objects](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#keywords-for-objects) - maxProperties, minProperties, required, properties, patternProperties, additionalProperties, dependencies, [propertyNames](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#propertynames)
- [for all types](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#keywords-for-all-types) - enum, [const](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#const)
- [compound keywords](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#compound-keywords) - not, oneOf, anyOf, allOf

With [ajv-keywords](https://github.com/epoberezkin/ajv-keywords) package Ajv also supports validation keywords from [JSON Schema extension proposals](https://github.com/json-schema/json-schema/wiki/v5-Proposals) for JSON-schema standard:

- [switch](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#switch-proposed) - conditional validation with a sequence of if/then clauses
- [patternRequired](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#patternrequired-proposed) - like `required` but with patterns that some property should match.
- [formatMaximum, formatMinimum, formatExclusiveMaximum, formatExclusiveMinimum](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md#formatmaximum--formatminimum-and-exclusiveformatmaximum--exclusiveformatminimum-proposed) - setting limits for date, time, etc.

See [JSON Schema validation keywords](https://github.com/epoberezkin/ajv/blob/master/KEYWORDS.md) for more details.


## Formats

The following formats are supported for string validation with "format" keyword:

- _date_: full-date according to [RFC3339](http://tools.ietf.org/html/rfc3339#section-5.6).
- _time_: time with optional time-zone.
- _date-time_: date-time from the same source (time-zone is mandatory). `date`, `time` and `date-time` validate ranges in `full` mode and only regexp in `fast` mode (see [options](#options)).
- _uri_: full uri with optional protocol.
- _url_: [URL record](https://url.spec.whatwg.org/#concept-url).
- _uri-template_: URI template according to [RFC6570](https://tools.ietf.org/html/rfc6570)
- _email_: email address.
- _hostname_: host name according to [RFC1034](http://tools.ietf.org/html/rfc1034#section-3.5).
- _ipv4_: IP address v4.
- _ipv6_: IP address v6.
- _regex_: tests whether a string is a valid regular expression by passing it to RegExp constructor.
- _uuid_: Universally Unique IDentifier according to [RFC4122](http://tools.ietf.org/html/rfc4122).
- _json-pointer_: JSON-pointer according to [RFC6901](https://tools.ietf.org/html/rfc6901).
- _relative-json-pointer_: relative JSON-pointer according to [this draft](http://tools.ietf.org/html/draft-luff-relative-json-pointer-00).

There are two modes of format validation: `fast` and `full`. This mode affects formats `date`, `time`, `date-time`, `uri`, `email`, and `hostname`. See [Options](#options) for details.

You can add additional formats and replace any of the formats above using [addFormat](#api-addformat) method.

The option `unknownFormats` allows changing the default behaviour when an unknown format is encountered. In this case Ajv can either fail schema compilation (default) or ignore it (default in versions before 5.0.0). You also can whitelist specific format(s) to be ignored. See [Options](#options) for details.

You can find patterns used for format validation and the sources that were used in [formats.js](https://github.com/epoberezkin/ajv/blob/master/lib/compile/formats.js).


## <a name="ref"></a>Combining schemas with $ref

You can structure your validation logic across multiple schema files and have schemas reference each other using `$ref` keyword.

Example:

```javascript
var schema = {
  "$id": "http://example.com/schemas/schema.json",
  "type": "object",
  "properties": {
    "foo": { "$ref": "defs.json#/definitions/int" },
    "bar": { "$ref": "defs.json#/definitions/str" }
  }
};

var defsSchema = {
  "$id": "http://example.com/schemas/defs.json",
  "definitions": {
    "int": { "type": "integer" },
    "str": { "type": "string" }
  }
};
```

Now to compile your schema you can either pass all schemas to Ajv instance:

```javascript
var ajv = new Ajv({schemas: [schema, defsSchema]});
var validate = ajv.getSchema('http://example.com/schemas/schema.json');
```

or use `addSchema` method:

```javascript
var ajv = new Ajv;
var validate = ajv.addSchema(defsSchema)
                  .compile(schema);
```

See [Options](#options) and [addSchema](#api) method.

__Please note__:
- `$ref` is resolved as the uri-reference using schema $id as the base URI (see the example).
- References can be recursive (and mutually recursive) to implement the schemas for different data structures (such as linked lists, trees, graphs, etc.).
- You don't have to host your schema files at the URIs that you use as schema $id. These URIs are only used to identify the schemas, and according to JSON Schema specification validators should not expect to be able to download the schemas from these URIs.
- The actual location of the schema file in the file system is not used.
- You can pass the identifier of the schema as the second parameter of `addSchema` method or as a property name in `schemas` option. This identifier can be used instead of (or in addition to) schema $id.
- You cannot have the same $id (or the schema identifier) used for more than one schema - the exception will be thrown.
- You can implement dynamic resolution of the referenced schemas using `compileAsync` method. In this way you can store schemas in any system (files, web, database, etc.) and reference them without explicitly adding to Ajv instance. See [Asynchronous schema compilation](#asynchronous-schema-compilation).


## $data reference

With `$data` option you can use values from the validated data as the values for the schema keywords. See [proposal](https://github.com/json-schema/json-schema/wiki/$data-(v5-proposal)) for more information about how it works.

`$data` reference is supported in the keywords: const, enum, format, maximum/minimum, exclusiveMaximum / exclusiveMinimum, maxLength / minLength, maxItems / minItems, maxProperties / minProperties, formatMaximum / formatMinimum, formatExclusiveMaximum / formatExclusiveMinimum, multipleOf, pattern, required, uniqueItems.

The value of "$data" should be a [JSON-pointer](https://tools.ietf.org/html/rfc6901) to the data (the root is always the top level data object, even if the $data reference is inside a referenced subschema) or a [relative JSON-pointer](http://tools.ietf.org/html/draft-luff-relative-json-pointer-00) (it is relative to the current point in data; if the $data reference is inside a referenced subschema it cannot point to the data outside of the root level for this subschema).

Examples.

This schema requires that the value in property `smaller` is less or equal than the value in the property larger:

```javascript
var ajv = new Ajv({$data: true});

var schema = {
  "properties": {
    "smaller": {
      "type": "number",
      "maximum": { "$data": "1/larger" }
    },
    "larger": { "type": "number" }
  }
};

var validData = {
  smaller: 5,
  larger: 7
};

ajv.validate(schema, validData); // true
```

This schema requires that the properties have the same format as their field names:

```javascript
var schema = {
  "additionalProperties": {
    "type": "string",
    "format": { "$data": "0#" }
  }
};

var validData = {
  'date-time': '1963-06-19T08:30:06.283185Z',
  email: 'joe.bloggs@example.com'
}
```

`$data` reference is resolved safely - it won't throw even if some property is undefined. If `$data` resolves to `undefined` the validation succeeds (with the exclusion of `const` keyword). If `$data` resolves to incorrect type (e.g. not "number" for maximum keyword) the validation fails.


## $merge and $patch keywords

With the package [ajv-merge-patch](https://github.com/epoberezkin/ajv-merge-patch) you can use the keywords `$merge` and `$patch` that allow extending JSON-schemas with patches using formats [JSON Merge Patch (RFC 7396)](https://tools.ietf.org/html/rfc7396) and [JSON Patch (RFC 6902)](https://tools.ietf.org/html/rfc6902).

To add keywords `$merge` and `$patch` to Ajv instance use this code:

```javascript
require('ajv-merge-patch')(ajv);
```

Examples.

Using `$merge`:

```json
{
  "$merge": {
    "source": {
      "type": "object",
      "properties": { "p": { "type": "string" } },
      "additionalProperties": false
    },
    "with": {
      "properties": { "q": { "type": "number" } }
    }
  }
}
```

Using `$patch`:

```json
{
  "$patch": {
    "source": {
      "type": "object",
      "properties": { "p": { "type": "string" } },
      "additionalProperties": false
    },
    "with": [
      { "op": "add", "path": "/properties/q", "value": { "type": "number" } }
    ]
  }
}
```

The schemas above are equivalent to this schema:

```json
{
  "type": "object",
  "properties": {
    "p": { "type": "string" },
    "q": { "type": "number" }
  },
  "additionalProperties": false
}
```

The properties `source` and `with` in the keywords `$merge` and `$patch` can use absolute or relative `$ref` to point to other schemas previously added to the Ajv instance or to the fragments of the current schema.

See the package [ajv-merge-patch](https://github.com/epoberezkin/ajv-merge-patch) for more information.


## Defining custom keywords

The advantages of using custom keywords are:

- allow creating validation scenarios that cannot be expressed using JSON Schema
- simplify your schemas
- help bringing a bigger part of the validation logic to your schemas
- make your schemas more expressive, less verbose and closer to your application domain
- implement custom data processors that modify your data (`modifying` option MUST be used in keyword definition) and/or create side effects while the data is being validated

If a keyword is used only for side-effects and its validation result is pre-defined, use option `valid: true/false` in keyword definition to simplify both generated code (no error handling in case of `valid: true`) and your keyword functions (no need to return any validation result).

The concerns you have to be aware of when extending JSON-schema standard with custom keywords are the portability and understanding of your schemas. You will have to support these custom keywords on other platforms and to properly document these keywords so that everybody can understand them in your schemas.

You can define custom keywords with [addKeyword](#api-addkeyword) method. Keywords are defined on the `ajv` instance level - new instances will not have previously defined keywords.

Ajv allows defining keywords with:
- validation function
- compilation function
- macro function
- inline compilation function that should return code (as string) that will be inlined in the currently compiled schema.

Example. `range` and `exclusiveRange` keywords using compiled schema:

```javascript
ajv.addKeyword('range', {
  type: 'number',
  compile: function (sch, parentSchema) {
    var min = sch[0];
    var max = sch[1];

    return parentSchema.exclusiveRange === true
            ? function (data) { return data > min && data < max; }
            : function (data) { return data >= min && data <= max; }
  }
});

var schema = { "range": [2, 4], "exclusiveRange": true };
var validate = ajv.compile(schema);
console.log(validate(2.01)); // true
console.log(validate(3.99)); // true
console.log(validate(2)); // false
console.log(validate(4)); // false
```

Several custom keywords (typeof, instanceof, range and propertyNames) are defined in [ajv-keywords](https://github.com/epoberezkin/ajv-keywords) package - they can be used for your schemas and as a starting point for your own custom keywords.

See [Defining custom keywords](https://github.com/epoberezkin/ajv/blob/master/CUSTOM.md) for more details.


## Asynchronous schema compilation

During asynchronous compilation remote references are loaded using supplied function. See `compileAsync` [method](#api-compileAsync) and `loadSchema` [option](#options).

Example:

```javascript
var ajv = new Ajv({ loadSchema: loadSchema });

ajv.compileAsync(schema).then(function (validate) {
  var valid = validate(data);
  // ...
});

function loadSchema(uri) {
  return request.json(uri).then(function (res) {
    if (res.statusCode >= 400)
      throw new Error('Loading error: ' + res.statusCode);
    return res.body;
  });
}
```

__Please note__: [Option](#options) `missingRefs` should NOT be set to `"ignore"` or `"fail"` for asynchronous compilation to work.


## Asynchronous validation

Example in Node.js REPL: https://tonicdev.com/esp/ajv-asynchronous-validation

You can define custom formats and keywords that perform validation asynchronously by accessing database or some other service. You should add `async: true` in the keyword or format definition (see [addFormat](#api-addformat), [addKeyword](#api-addkeyword) and [Defining custom keywords](#defining-custom-keywords)).

If your schema uses asynchronous formats/keywords or refers to some schema that contains them it should have `"$async": true` keyword so that Ajv can compile it correctly. If asynchronous format/keyword or reference to asynchronous schema is used in the schema without `$async` keyword Ajv will throw an exception during schema compilation.

__Please note__: all asynchronous subschemas that are referenced from the current or other schemas should have `"$async": true` keyword as well, otherwise the schema compilation will fail.

Validation function for an asynchronous custom format/keyword should return a promise that resolves with `true` or `false` (or rejects with `new Ajv.ValidationError(errors)` if you want to return custom errors from the keyword function). Ajv compiles asynchronous schemas to either [es7 async functions](http://tc39.github.io/ecmascript-asyncawait/) that can optionally be transpiled with [nodent](https://github.com/MatAtBread/nodent) or with [regenerator](https://github.com/facebook/regenerator) or to [generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) that can be optionally transpiled with regenerator as well. You can also supply any other transpiler as a function. See [Options](#options).

The compiled validation function has `$async: true` property (if the schema is asynchronous), so you can differentiate these functions if you are using both synchronous and asynchronous schemas.

If you are using generators, the compiled validation function can be either wrapped with [co](https://github.com/tj/co) (default) or returned as generator function, that can be used directly, e.g. in [koa](http://koajs.com/) 1.0. `co` is a small library, it is included in Ajv (both as npm dependency and in the browser bundle).

Async functions are currently supported in Chrome 55, Firefox 52, Node.js 7 (with --harmony-async-await) and MS Edge 13 (with flag).

Generator functions are currently supported in Chrome, Firefox and Node.js.

If you are using Ajv in other browsers or in older versions of Node.js you should use one of available transpiling options. All provided async modes use global Promise class. If your platform does not have Promise you should use a polyfill that defines it.

Validation result will be a promise that resolves with validated data or rejects with an exception `Ajv.ValidationError` that contains the array of validation errors in `errors` property.


Example:

```javascript
/**
 * Default mode is non-transpiled generator function wrapped with `co`.
 * Using package ajv-async (https://github.com/epoberezkin/ajv-async)
 * you can auto-detect the best async mode.
 * In this case, without "async" and "transpile" options
 * (or with option {async: true})
 * Ajv will choose the first supported/installed option in this order:
 * 1. native async function
 * 2. native generator function wrapped with co
 * 3. es7 async functions transpiled with nodent
 * 4. es7 async functions transpiled with regenerator
 */

var setupAsync = require('ajv-async');
var ajv = setupAsync(new Ajv);

ajv.addKeyword('idExists', {
  async: true,
  type: 'number',
  validate: checkIdExists
});


function checkIdExists(schema, data) {
  return knex(schema.table)
  .select('id')
  .where('id', data)
  .then(function (rows) {
    return !!rows.length; // true if record is found
  });
}

var schema = {
  "$async": true,
  "properties": {
    "userId": {
      "type": "integer",
      "idExists": { "table": "users" }
    },
    "postId": {
      "type": "integer",
      "idExists": { "table": "posts" }
    }
  }
};

var validate = ajv.compile(schema);

validate({ userId: 1, postId: 19 })
.then(function (data) {
  console.log('Data is valid', data); // { userId: 1, postId: 19 }
})
.catch(function (err) {
  if (!(err instanceof Ajv.ValidationError)) throw err;
  // data is invalid
  console.log('Validation errors:', err.errors);
});
```

### Using transpilers with asynchronous validation functions.

To use a transpiler you should separately install it (or load its bundle in the browser).

Ajv npm package includes minified browser bundles of regenerator and nodent in dist folder.


#### Using nodent

```javascript
var setupAsync = require('ajv-async');
var ajv = new Ajv({ /* async: 'es7', */ transpile: 'nodent' });
setupAsync(ajv);
var validate = ajv.compile(schema); // transpiled es7 async function
validate(data).then(successFunc).catch(errorFunc);
```

`npm install nodent` or use `nodent.min.js` from dist folder of npm package.


#### Using regenerator

```javascript
var setupAsync = require('ajv-async');
var ajv = new Ajv({ /* async: 'es7', */ transpile: 'regenerator' });
setupAsync(ajv);
var validate = ajv.compile(schema); // transpiled es7 async function
validate(data).then(successFunc).catch(errorFunc);
```

`npm install regenerator` or use `regenerator.min.js` from dist folder of npm package.


#### Using other transpilers

```javascript
var ajv = new Ajv({ async: 'es7', processCode: transpileFunc });
var validate = ajv.compile(schema); // transpiled es7 async function
validate(data).then(successFunc).catch(errorFunc);
```

See [Options](#options).


#### Comparison of async modes

|mode|transpile<br>speed*|run-time<br>speed*|bundle<br>size|
|---|:-:|:-:|:-:|
|es7 async<br>(native)|-|0.75|-|
|generators<br>(native)|-|1.0|-|
|es7.nodent|1.35|1.1|215Kb|
|es7.regenerator|1.0|2.7|1109Kb|
|regenerator|1.0|3.2|1109Kb|

\* Relative performance in Node.js 7.x — smaller is better.

[nodent](https://github.com/MatAtBread/nodent) has several advantages:

- much smaller browser bundle than regenerator
- almost the same performance of generated code as native generators in Node.js and the latest Chrome
- much better performance than native generators in other browsers
- works in IE 9 (regenerator does not)


## Filtering data

With [option `removeAdditional`](#options) (added by [andyscott](https://github.com/andyscott)) you can filter data during the validation.

This option modifies original data.

Example:

```javascript
var ajv = new Ajv({ removeAdditional: true });
var schema = {
  "additionalProperties": false,
  "properties": {
    "foo": { "type": "number" },
    "bar": {
      "additionalProperties": { "type": "number" },
      "properties": {
        "baz": { "type": "string" }
      }
    }
  }
}

var data = {
  "foo": 0,
  "additional1": 1, // will be removed; `additionalProperties` == false
  "bar": {
    "baz": "abc",
    "additional2": 2 // will NOT be removed; `additionalProperties` != false
  },
}

var validate = ajv.compile(schema);

console.log(validate(data)); // true
console.log(data); // { "foo": 0, "bar": { "baz": "abc", "additional2": 2 }
```

If `removeAdditional` option in the example above were `"all"` then both `additional1` and `additional2` properties would have been removed.

If the option were `"failing"` then property `additional1` would have been removed regardless of its value and property `additional2` would have been removed only if its value were failing the schema in the inner `additionalProperties` (so in the example above it would have stayed because it passes the schema, but any non-number would have been removed).

__Please note__: If you use `removeAdditional` option with `additionalProperties` keyword inside `anyOf`/`oneOf` keywords your validation can fail with this schema, for example:

```json
{
  "type": "object",
  "oneOf": [
    {
      "properties": {
        "foo": { "type": "string" }
      },
      "required": [ "foo" ],
      "additionalProperties": false
    },
    {
      "properties": {
        "bar": { "type": "integer" }
      },
      "required": [ "bar" ],
      "additionalProperties": false
    }
  ]
}
```

The intention of the schema above is to allow objects with either the string property "foo" or the integer property "bar", but not with both and not with any other properties.

With the option `removeAdditional: true` the validation will pass for the object `{ "foo": "abc"}` but will fail for the object `{"bar": 1}`. It happens because while the first subschema in `oneOf` is validated, the property `bar` is removed because it is an additional property according to the standard (because it is not included in `properties` keyword in the same schema).

While this behaviour is unexpected (issues [#129](https://github.com/epoberezkin/ajv/issues/129), [#134](https://github.com/epoberezkin/ajv/issues/134)), it is correct. To have the expected behaviour (both objects are allowed and additional properties are removed) the schema has to be refactored in this way:

```json
{
  "type": "object",
  "properties": {
    "foo": { "type": "string" },
    "bar": { "type": "integer" }
  },
  "additionalProperties": false,
  "oneOf": [
    { "required": [ "foo" ] },
    { "required": [ "bar" ] }
  ]
}
```

The schema above is also more efficient - it will compile into a faster function.


## Assigning defaults

With [option `useDefaults`](#options) Ajv will assign values from `default` keyword in the schemas of `properties` and `items` (when it is the array of schemas) to the missing properties and items.

This option modifies original data.

__Please note__: by default the default value is inserted in the generated validation code as a literal (starting from v4.0), so the value inserted in the data will be the deep clone of the default in the schema.

If you need to insert the default value in the data by reference pass the option `useDefaults: "shared"`.

Inserting defaults by reference can be faster (in case you have an object in `default`) and it allows to have dynamic values in defaults, e.g. timestamp, without recompiling the schema. The side effect is that modifying the default value in any validated data instance will change the default in the schema and in other validated data instances. See example 3 below.


Example 1 (`default` in `properties`):

```javascript
var ajv = new Ajv({ useDefaults: true });
var schema = {
  "type": "object",
  "properties": {
    "foo": { "type": "number" },
    "bar": { "type": "string", "default": "baz" }
  },
  "required": [ "foo", "bar" ]
};

var data = { "foo": 1 };

var validate = ajv.compile(schema);

console.log(validate(data)); // true
console.log(data); // { "foo": 1, "bar": "baz" }
```

Example 2 (`default` in `items`):

```javascript
var schema = {
  "type": "array",
  "items": [
    { "type": "number" },
    { "type": "string", "default": "foo" }
  ]
}

var data = [ 1 ];

var validate = ajv.compile(schema);

console.log(validate(data)); // true
console.log(data); // [ 1, "foo" ]
```

Example 3 (inserting "defaults" by reference):

```javascript
var ajv = new Ajv({ useDefaults: 'shared' });

var schema = {
  properties: {
    foo: {
      default: { bar: 1 }
    }
  }
}

var validate = ajv.compile(schema);

var data = {};
console.log(validate(data)); // true
console.log(data); // { foo: { bar: 1 } }

data.foo.bar = 2;

var data2 = {};
console.log(validate(data2)); // true
console.log(data2); // { foo: { bar: 2 } }
```

`default` keywords in other cases are ignored:

- not in `properties` or `items` subschemas
- in schemas inside `anyOf`, `oneOf` and `not` (see [#42](https://github.com/epoberezkin/ajv/issues/42))
- in `if` subschema of `switch` keyword
- in schemas generated by custom macro keywords


## Coercing data types

When you are validating user inputs all your data properties are usually strings. The option `coerceTypes` allows you to have your data types coerced to the types specified in your schema `type` keywords, both to pass the validation and to use the correctly typed data afterwards.

This option modifies original data.

__Please note__: if you pass a scalar value to the validating function its type will be coerced and it will pass the validation, but the value of the variable you pass won't be updated because scalars are passed by value.


Example 1:

```javascript
var ajv = new Ajv({ coerceTypes: true });
var schema = {
  "type": "object",
  "properties": {
    "foo": { "type": "number" },
    "bar": { "type": "boolean" }
  },
  "required": [ "foo", "bar" ]
};

var data = { "foo": "1", "bar": "false" };

var validate = ajv.compile(schema);

console.log(validate(data)); // true
console.log(data); // { "foo": 1, "bar": false }
```

Example 2 (array coercions):

```javascript
var ajv = new Ajv({ coerceTypes: 'array' });
var schema = {
  "properties": {
    "foo": { "type": "array", "items": { "type": "number" } },
    "bar": { "type": "boolean" }
  }
};

var data = { "foo": "1", "bar": ["false"] };

var validate = ajv.compile(schema);

console.log(validate(data)); // true
console.log(data); // { "foo": [1], "bar": false }
```

The coercion rules, as you can see from the example, are different from JavaScript both to validate user input as expected and to have the coercion reversible (to correctly validate cases where different types are defined in subschemas of "anyOf" and other compound keywords).

See [Coercion rules](https://github.com/epoberezkin/ajv/blob/master/COERCION.md) for details.


## API

##### new Ajv(Object options) -&gt; Object

Create Ajv instance.


##### .compile(Object schema) -&gt; Function&lt;Object data&gt;

Generate validating function and cache the compiled schema for future use.

Validating function returns boolean and has properties `errors` with the errors from the last validation (`null` if there were no errors) and `schema` with the reference to the original schema.

Unless the option `validateSchema` is false, the schema will be validated against meta-schema and if schema is invalid the error will be thrown. See [options](#options).


##### <a name="api-compileAsync"></a>.compileAsync(Object schema [, Boolean meta] [, Function callback]) -&gt; Promise

Asynchronous version of `compile` method that loads missing remote schemas using asynchronous function in `options.loadSchema`. This function returns a Promise that resolves to a validation function. An optional callback passed to `compileAsync` will be called with 2 parameters: error (or null) and validating function. The returned promise will reject (and the callback will be called with an error) when:

- missing schema can't be loaded (`loadSchema` returns a Promise that rejects).
- a schema containing a missing reference is loaded, but the reference cannot be resolved.
- schema (or some loaded/referenced schema) is invalid.

The function compiles schema and loads the first missing schema (or meta-schema) until all missing schemas are loaded.

You can asynchronously compile meta-schema by passing `true` as the second parameter.

See example in [Asynchronous compilation](#asynchronous-schema-compilation).


##### .validate(Object schema|String key|String ref, data) -&gt; Boolean

Validate data using passed schema (it will be compiled and cached).

Instead of the schema you can use the key that was previously passed to `addSchema`, the schema id if it was present in the schema or any previously resolved reference.

Validation errors will be available in the `errors` property of Ajv instance (`null` if there were no errors).

__Please note__: every time this method is called the errors are overwritten so you need to copy them to another variable if you want to use them later.

If the schema is asynchronous (has `$async` keyword on the top level) this method returns a Promise. See [Asynchronous validation](#asynchronous-validation).


##### .addSchema(Array&lt;Object&gt;|Object schema [, String key]) -&gt; Ajv

Add schema(s) to validator instance. This method does not compile schemas (but it still validates them). Because of that dependencies can be added in any order and circular dependencies are supported. It also prevents unnecessary compilation of schemas that are containers for other schemas but not used as a whole.

Array of schemas can be passed (schemas should have ids), the second parameter will be ignored.

Key can be passed that can be used to reference the schema and will be used as the schema id if there is no id inside the schema. If the key is not passed, the schema id will be used as the key.


Once the schema is added, it (and all the references inside it) can be referenced in other schemas and used to validate data.

Although `addSchema` does not compile schemas, explicit compilation is not required - the schema will be compiled when it is used first time.

By default the schema is validated against meta-schema before it is added, and if the schema does not pass validation the exception is thrown. This behaviour is controlled by `validateSchema` option.

__Please note__: Ajv uses the [method chaining syntax](https://en.wikipedia.org/wiki/Method_chaining) for all methods with the prefix `add*` and `remove*`.
This allows you to do nice things like the following.

```javascript
var validate = new Ajv().addSchema(schema).addFormat(name, regex).getSchema(uri);
```  

##### .addMetaSchema(Array&lt;Object&gt;|Object schema [, String key]) -&gt; Ajv

Adds meta schema(s) that can be used to validate other schemas. That function should be used instead of `addSchema` because there may be instance options that would compile a meta schema incorrectly (at the moment it is `removeAdditional` option).

There is no need to explicitly add draft 6 meta schema (http://json-schema.org/draft-06/schema and http://json-schema.org/schema) - it is added by default, unless option `meta` is set to `false`. You only need to use it if you have a changed meta-schema that you want to use to validate your schemas. See `validateSchema`.


##### <a name="api-validateschema"></a>.validateSchema(Object schema) -&gt; Boolean

Validates schema. This method should be used to validate schemas rather than `validate` due to the inconsistency of `uri` format in JSON Schema standard.

By default this method is called automatically when the schema is added, so you rarely need to use it directly.

If schema doesn't have `$schema` property, it is validated against draft 6 meta-schema (option `meta` should not be false).

If schema has `$schema` property, then the schema with this id (that should be previously added) is used to validate passed schema.

Errors will be available at `ajv.errors`.


##### .getSchema(String key) -&gt; Function&lt;Object data&gt;

Retrieve compiled schema previously added with `addSchema` by the key passed to `addSchema` or by its full reference (id). The returned validating function has `schema` property with the reference to the original schema.


##### .removeSchema([Object schema|String key|String ref|RegExp pattern]) -&gt; Ajv

Remove added/cached schema. Even if schema is referenced by other schemas it can be safely removed as dependent schemas have local references.

Schema can be removed using:
- key passed to `addSchema`
- it's full reference (id)
- RegExp that should match schema id or key (meta-schemas won't be removed)
- actual schema object that will be stable-stringified to remove schema from cache

If no parameter is passed all schemas but meta-schemas will be removed and the cache will be cleared.


##### <a name="api-addformat"></a>.addFormat(String name, String|RegExp|Function|Object format) -&gt; Ajv

Add custom format to validate strings or numbers. It can also be used to replace pre-defined formats for Ajv instance.

Strings are converted to RegExp.

Function should return validation result as `true` or `false`.

If object is passed it should have properties `validate`, `compare` and `async`:

- _validate_: a string, RegExp or a function as described above.
- _compare_: an optional comparison function that accepts two strings and compares them according to the format meaning. This function is used with keywords `formatMaximum`/`formatMinimum` (defined in [ajv-keywords](https://github.com/epoberezkin/ajv-keywords) package). It should return `1` if the first value is bigger than the second value, `-1` if it is smaller and `0` if it is equal.
- _async_: an optional `true` value if `validate` is an asynchronous function; in this case it should return a promise that resolves with a value `true` or `false`.
- _type_: an optional type of data that the format applies to. It can be `"string"` (default) or `"number"` (see https://github.com/epoberezkin/ajv/issues/291#issuecomment-259923858). If the type of data is different, the validation will pass.

Custom formats can be also added via `formats` option.


##### <a name="api-addkeyword"></a>.addKeyword(String keyword, Object definition) -&gt; Ajv

Add custom validation keyword to Ajv instance.

Keyword should be different from all standard JSON schema keywords and different from previously defined keywords. There is no way to redefine keywords or to remove keyword definition from the instance.

Keyword must start with a letter, `_` or `$`, and may continue with letters, numbers, `_`, `$`, or `-`.
It is recommended to use an application-specific prefix for keywords to avoid current and future name collisions.

Example Keywords:
- `"xyz-example"`: valid, and uses prefix for the xyz project to avoid name collisions.
- `"example"`: valid, but not recommended as it could collide with future versions of JSON schema etc.
- `"3-example"`: invalid as numbers are not allowed to be the first character in a keyword

Keyword definition is an object with the following properties:

- _type_: optional string or array of strings with data type(s) that the keyword applies to. If not present, the keyword will apply to all types.
- _validate_: validating function
- _compile_: compiling function
- _macro_: macro function
- _inline_: compiling function that returns code (as string)
- _schema_: an optional `false` value used with "validate" keyword to not pass schema
- _metaSchema_: an optional meta-schema for keyword schema
- _modifying_: `true` MUST be passed if keyword modifies data
- _valid_: pass `true`/`false` to pre-define validation result, the result returned from validation function will be ignored. This option cannot be used with macro keywords.
- _$data_: an optional `true` value to support [$data reference](#data-reference) as the value of custom keyword. The reference will be resolved at validation time. If the keyword has meta-schema it would be extended to allow $data and it will be used to validate the resolved value. Supporting $data reference requires that keyword has validating function (as the only option or in addition to compile, macro or inline function).
- _async_: an optional `true` value if the validation function is asynchronous (whether it is compiled or passed in _validate_ property); in this case it should return a promise that resolves with a value `true` or `false`. This option is ignored in case of "macro" and "inline" keywords.
- _errors_: an optional boolean indicating whether keyword returns errors. If this property is not set Ajv will determine if the errors were set in case of failed validation.

_compile_, _macro_ and _inline_ are mutually exclusive, only one should be used at a time. _validate_ can be used separately or in addition to them to support $data reference.

__Please note__: If the keyword is validating data type that is different from the type(s) in its definition, the validation function will not be called (and expanded macro will not be used), so there is no need to check for data type inside validation function or inside schema returned by macro function (unless you want to enforce a specific type and for some reason do not want to use a separate `type` keyword for that). In the same way as standard keywords work, if the keyword does not apply to the data type being validated, the validation of this keyword will succeed.

See [Defining custom keywords](#defining-custom-keywords) for more details.


##### .getKeyword(String keyword) -&gt; Object|Boolean

Returns custom keyword definition, `true` for pre-defined keywords and `false` if the keyword is unknown.


##### .removeKeyword(String keyword) -&gt; Ajv

Removes custom or pre-defined keyword so you can redefine them.

While this method can be used to extend pre-defined keywords, it can also be used to completely change their meaning - it may lead to unexpected results.

__Please note__: schemas compiled before the keyword is removed will continue to work without changes. To recompile schemas use `removeSchema` method and compile them again.


##### .errorsText([Array&lt;Object&gt; errors [, Object options]]) -&gt; String

Returns the text with all errors in a String.

Options can have properties `separator` (string used to separate errors, ", " by default) and `dataVar` (the variable name that dataPaths are prefixed with, "data" by default).


## Options

Defaults:

```javascript
{
  // validation and reporting options:
  $data:            false,
  allErrors:        false,
  verbose:          false,
  jsonPointers:     false,
  uniqueItems:      true,
  unicode:          true,
  format:           'fast',
  formats:          {},
  unknownFormats:   true,
  schemas:          {},
  logger:           undefined,
  // referenced schema options:
  schemaId:         undefined // recommended '$id'
  missingRefs:      true,
  extendRefs:       'ignore', // recommended 'fail'
  loadSchema:       undefined, // function(uri: string): Promise {}
  // options to modify validated data:
  removeAdditional: false,
  useDefaults:      false,
  coerceTypes:      false,
  // asynchronous validation options:
  async:            'co*',
  transpile:        undefined, // requires ajv-async package
  // advanced options:
  meta:             true,
  validateSchema:   true,
  addUsedSchema:    true,
  inlineRefs:       true,
  passContext:      false,
  loopRequired:     Infinity,
  ownProperties:    false,
  multipleOfPrecision: false,
  errorDataPath:    'object',
  messages:         true,
  sourceCode:       false,
  processCode:      undefined, // function (str: string): string {}
  cache:            new Cache,
  serialize:        undefined
}
```

##### Validation and reporting options

- _$data_: support [$data references](#data-reference). Draft 6 meta-schema that is added by default will be extended to allow them. If you want to use another meta-schema you need to use $dataMetaSchema method to add support for $data reference. See [API](#api).
- _allErrors_: check all rules collecting all errors. Default is to return after the first error.
- _verbose_: include the reference to the part of the schema (`schema` and `parentSchema`) and validated data in errors (false by default).
- _jsonPointers_: set `dataPath` property of errors using [JSON Pointers](https://tools.ietf.org/html/rfc6901) instead of JavaScript property access notation.
- _uniqueItems_: validate `uniqueItems` keyword (true by default).
- _unicode_: calculate correct length of strings with unicode pairs (true by default). Pass `false` to use `.length` of strings that is faster, but gives "incorrect" lengths of strings with unicode pairs - each unicode pair is counted as two characters.
- _format_: formats validation mode ('fast' by default). Pass 'full' for more correct and slow validation or `false` not to validate formats at all. E.g., 25:00:00 and 2015/14/33 will be invalid time and date in 'full' mode but it will be valid in 'fast' mode.
- _formats_: an object with custom formats. Keys and values will be passed to `addFormat` method.
- _unknownFormats_: handling of unknown formats. Option values:
  - `true` (default) - if an unknown format is encountered the exception is thrown during schema compilation. If `format` keyword value is [$data reference](#data-reference) and it is unknown the validation will fail.
  - `[String]` - an array of unknown format names that will be ignored. This option can be used to allow usage of third party schemas with format(s) for which you don't have definitions, but still fail if another unknown format is used. If `format` keyword value is [$data reference](#data-reference) and it is not in this array the validation will fail.
  - `"ignore"` - to log warning during schema compilation and always pass validation (the default behaviour in versions before 5.0.0). This option is not recommended, as it allows to mistype format name and it won't be validated without any error message. This behaviour is required by JSON-schema specification.
- _schemas_: an array or object of schemas that will be added to the instance. In case you pass the array the schemas must have IDs in them. When the object is passed the method `addSchema(value, key)` will be called for each schema in this object.
- _logger_: sets the logging method. Default is the global `console` object that should have methods `log`, `warn` and `error`. Option values:
  - custom logger - it should have methods `log`, `warn` and `error`. If any of these methods is missing an exception will be thrown.
  - `false` - logging is disabled.


##### Referenced schema options

- _schemaId_: this option defines which keywords are used as schema URI. Option value:
  - `"$id"` (recommended) - only use `$id` keyword as schema URI (as specified in JSON Schema draft-06), ignore `id` keyword (if it is present a warning will be logged).
  - `"id"` - only use `id` keyword as schema URI (as specified in JSON Schema draft-04), ignore `$id` keyword (if it is present a warning will be logged).
  - `undefined` (default) - use both `$id` and `id` keywords as schema URI. If both are present (in the same schema object) and different the exception will be thrown during schema compilation.
- _missingRefs_: handling of missing referenced schemas. Option values:
  - `true` (default) - if the reference cannot be resolved during compilation the exception is thrown. The thrown error has properties `missingRef` (with hash fragment) and `missingSchema` (without it). Both properties are resolved relative to the current base id (usually schema id, unless it was substituted).
  - `"ignore"` - to log error during compilation and always pass validation.
  - `"fail"` - to log error and successfully compile schema but fail validation if this rule is checked.
- _extendRefs_: validation of other keywords when `$ref` is present in the schema. Option values:
  - `"ignore"` (default) - when `$ref` is used other keywords are ignored (as per [JSON Reference](https://tools.ietf.org/html/draft-pbryan-zyp-json-ref-03#section-3) standard). A warning will be logged during the schema compilation.
  - `"fail"` (recommended) - if other validation keywords are used together with `$ref` the exception will be thrown when the schema is compiled. This option is recommended to make sure schema has no keywords that are ignored, which can be confusing.
  - `true` - validate all keywords in the schemas with `$ref` (the default behaviour in versions before 5.0.0).
- _loadSchema_: asynchronous function that will be used to load remote schemas when `compileAsync` [method](#api-compileAsync) is used and some reference is missing (option `missingRefs` should NOT be 'fail' or 'ignore'). This function should accept remote schema uri as a parameter and return a Promise that resolves to a schema. See example in [Asynchronous compilation](#asynchronous-schema-compilation).


##### Options to modify validated data

- _removeAdditional_: remove additional properties - see example in [Filtering data](#filtering-data). This option is not used if schema is added with `addMetaSchema` method. Option values:
  - `false` (default) - not to remove additional properties
  - `"all"` - all additional properties are removed, regardless of `additionalProperties` keyword in schema (and no validation is made for them).
  - `true` - only additional properties with `additionalProperties` keyword equal to `false` are removed.
  - `"failing"` - additional properties that fail schema validation will be removed (where `additionalProperties` keyword is `false` or schema).
- _useDefaults_: replace missing properties and items with the values from corresponding `default` keywords. Default behaviour is to ignore `default` keywords. This option is not used if schema is added with `addMetaSchema` method. See examples in [Assigning defaults](#assigning-defaults). Option values:
  - `false` (default) - do not use defaults
  - `true` - insert defaults by value (safer and slower, object literal is used).
  - `"shared"` - insert defaults by reference (faster). If the default is an object, it will be shared by all instances of validated data. If you modify the inserted default in the validated data, it will be modified in the schema as well.
- _coerceTypes_: change data type of data to match `type` keyword. See the example in [Coercing data types](#coercing-data-types) and [coercion rules](https://github.com/epoberezkin/ajv/blob/master/COERCION.md). Option values:
  - `false` (default) - no type coercion.
  - `true` - coerce scalar data types.
  - `"array"` - in addition to coercions between scalar types, coerce scalar data to an array with one element and vice versa (as required by the schema).


##### Asynchronous validation options

- _async_: determines how Ajv compiles asynchronous schemas (see [Asynchronous validation](#asynchronous-validation)) to functions. Option values:
  - `"*"` / `"co*"` (default) - compile to generator function ("co*" - wrapped with `co.wrap`). If generators are not supported and you don't provide `processCode` option (or `transpile` option if you use [ajv-async](https://github.com/epoberezkin/ajv-async) package), the exception will be thrown when async schema is compiled.
  - `"es7"` - compile to es7 async function. Unless your platform supports them you need to provide `processCode` or `transpile` option. According to [compatibility table](http://kangax.github.io/compat-table/es7/)) async functions are supported by:
    - Firefox 52,
    - Chrome 55,
    - Node.js 7 (with `--harmony-async-await`),
    - MS Edge 13 (with flag).
  - `undefined`/`true` - auto-detect async mode. It requires [ajv-async](https://github.com/epoberezkin/ajv-async) package. If `transpile` option is not passed, ajv-async will choose the first of supported/installed async/transpile modes in this order:
    - "es7" (native async functions),
    - "co*" (native generators with co.wrap),
    - "es7"/"nodent",
    - "co*"/"regenerator" during the creation of the Ajv instance.

  If none of the options is available the exception will be thrown.
- _transpile_: Requires [ajv-async](https://github.com/epoberezkin/ajv-async) package. It determines whether Ajv transpiles compiled asynchronous validation function. Option values:
  - `"nodent"` - transpile with [nodent](https://github.com/MatAtBread/nodent). If nodent is not installed, the exception will be thrown. nodent can only transpile es7 async functions; it will enforce this mode.
  - `"regenerator"` - transpile with [regenerator](https://github.com/facebook/regenerator). If regenerator is not installed, the exception will be thrown.
  - a function - this function should accept the code of validation function as a string and return transpiled code. This option allows you to use any other transpiler you prefer. If you are passing a function, you can simply pass it to `processCode` option without using ajv-async.


##### Advanced options

- _meta_: add [meta-schema](http://json-schema.org/documentation.html) so it can be used by other schemas (true by default). If an object is passed, it will be used as the default meta-schema for schemas that have no `$schema` keyword. This default meta-schema MUST have `$schema` keyword.
- _validateSchema_: validate added/compiled schemas against meta-schema (true by default). `$schema` property in the schema can either be http://json-schema.org/schema or http://json-schema.org/draft-04/schema or absent (draft-4 meta-schema will be used) or can be a reference to the schema previously added with `addMetaSchema` method. Option values:
  - `true` (default) -  if the validation fails, throw the exception.
  - `"log"` - if the validation fails, log error.
  - `false` - skip schema validation.
- _addUsedSchema_: by default methods `compile` and `validate` add schemas to the instance if they have `$id` (or `id`) property that doesn't start with "#". If `$id` is present and it is not unique the exception will be thrown. Set this option to `false` to skip adding schemas to the instance and the `$id` uniqueness check when these methods are used. This option does not affect `addSchema` method.
- _inlineRefs_: Affects compilation of referenced schemas. Option values:
  - `true` (default) - the referenced schemas that don't have refs in them are inlined, regardless of their size - that substantially improves performance at the cost of the bigger size of compiled schema functions.
  - `false` - to not inline referenced schemas (they will be compiled as separate functions).
  - integer number - to limit the maximum number of keywords of the schema that will be inlined.
- _passContext_: pass validation context to custom keyword functions. If this option is `true` and you pass some context to the compiled validation function with `validate.call(context, data)`, the `context` will be available as `this` in your custom keywords. By default `this` is Ajv instance.
- _loopRequired_: by default `required` keyword is compiled into a single expression (or a sequence of statements in `allErrors` mode). In case of a very large number of properties in this keyword it may result in a very big validation function. Pass integer to set the number of properties above which `required` keyword will be validated in a loop - smaller validation function size but also worse performance.
- _ownProperties_: by default Ajv iterates over all enumerable object properties; when this option is `true` only own enumerable object properties (i.e. found directly on the object rather than on its prototype) are iterated. Contributed by @mbroadst.
- _multipleOfPrecision_: by default `multipleOf` keyword is validated by comparing the result of division with parseInt() of that result. It works for dividers that are bigger than 1. For small dividers such as 0.01 the result of the division is usually not integer (even when it should be integer, see issue [#84](https://github.com/epoberezkin/ajv/issues/84)). If you need to use fractional dividers set this option to some positive integer N to have `multipleOf` validated using this formula: `Math.abs(Math.round(division) - division) < 1e-N` (it is slower but allows for float arithmetics deviations).
- _errorDataPath_: set `dataPath` to point to 'object' (default) or to 'property' when validating keywords `required`, `additionalProperties` and `dependencies`.
- _messages_: Include human-readable messages in errors. `true` by default. `false` can be passed when custom messages are used (e.g. with [ajv-i18n](https://github.com/epoberezkin/ajv-i18n)).
- _sourceCode_: add `sourceCode` property to validating function (for debugging; this code can be different from the result of toString call).
- _processCode_: an optional function to process generated code before it is passed to Function constructor. It can be used to either beautify (the validating function is generated without line-breaks) or to transpile code. Starting from version 5.0.0 this option replaced options:
  - `beautify` that formatted the generated function using [js-beautify](https://github.com/beautify-web/js-beautify). If you want to beautify the generated code pass `require('js-beautify').js_beautify`.
  - `transpile` that transpiled asynchronous validation function. You can still use `transpile` option with [ajv-async](https://github.com/epoberezkin/ajv-async) package. See [Asynchronous validation](#asynchronous-validation) for more information.
- _cache_: an optional instance of cache to store compiled schemas using stable-stringified schema as a key. For example, set-associative cache [sacjs](https://github.com/epoberezkin/sacjs) can be used. If not passed then a simple hash is used which is good enough for the common use case (a limited number of statically defined schemas). Cache should have methods `put(key, value)`, `get(key)`, `del(key)` and `clear()`.
- _serialize_: an optional function to serialize schema to cache key. Pass `false` to use schema itself as a key (e.g., if WeakMap used as a cache). By default [fast-json-stable-stringify](https://github.com/epoberezkin/fast-json-stable-stringify) is used.


## Validation errors

In case of validation failure, Ajv assigns the array of errors to `errors` property of validation function (or to `errors` property of Ajv instance when `validate` or `validateSchema` methods were called). In case of [asynchronous validation](#asynchronous-validation), the returned promise is rejected with exception `Ajv.ValidationError` that has `errors` property.


### Error objects

Each error is an object with the following properties:

- _keyword_: validation keyword.
- _dataPath_: the path to the part of the data that was validated. By default `dataPath` uses JavaScript property access notation (e.g., `".prop[1].subProp"`). When the option `jsonPointers` is true (see [Options](#options)) `dataPath` will be set using JSON pointer standard (e.g., `"/prop/1/subProp"`).
- _schemaPath_: the path (JSON-pointer as a URI fragment) to the schema of the keyword that failed validation.
- _params_: the object with the additional information about error that can be used to create custom error messages (e.g., using [ajv-i18n](https://github.com/epoberezkin/ajv-i18n) package). See below for parameters set by all keywords.
- _message_: the standard error message (can be excluded with option `messages` set to false).
- _schema_: the schema of the keyword (added with `verbose` option).
- _parentSchema_: the schema containing the keyword (added with `verbose` option)
- _data_: the data validated by the keyword (added with `verbose` option).

__Please note__: `propertyNames` keyword schema validation errors have an additional property `propertyName`, `dataPath` points to the object. After schema validation for each property name, if it is invalid an additional error is added with the property `keyword` equal to `"propertyNames"`.


### Error parameters

Properties of `params` object in errors depend on the keyword that failed validation.

- `maxItems`, `minItems`, `maxLength`, `minLength`, `maxProperties`, `minProperties` - property `limit` (number, the schema of the keyword).
- `additionalItems` - property `limit` (the maximum number of allowed items in case when `items` keyword is an array of schemas and `additionalItems` is false).
- `additionalProperties` - property `additionalProperty` (the property not used in `properties` and `patternProperties` keywords).
- `dependencies` - properties:
  - `property` (dependent property),
  - `missingProperty` (required missing dependency - only the first one is reported currently)
  - `deps` (required dependencies, comma separated list as a string),
  - `depsCount` (the number of required dependencies).
- `format` - property `format` (the schema of the keyword).
- `maximum`, `minimum` - properties:
  - `limit` (number, the schema of the keyword),
  - `exclusive` (boolean, the schema of `exclusiveMaximum` or `exclusiveMinimum`),
  - `comparison` (string, comparison operation to compare the data to the limit, with the data on the left and the limit on the right; can be "<", "<=", ">", ">=")
- `multipleOf` - property `multipleOf` (the schema of the keyword)
- `pattern` - property `pattern` (the schema of the keyword)
- `required` - property `missingProperty` (required property that is missing).
- `propertyNames` - property `propertyName` (an invalid property name).
- `patternRequired` (in ajv-keywords) - property `missingPattern` (required pattern that did not match any property).
- `type` - property `type` (required type(s), a string, can be a comma-separated list)
- `uniqueItems` - properties `i` and `j` (indices of duplicate items).
- `enum` - property `allowedValues` pointing to the array of values (the schema of the keyword).
- `$ref` - property `ref` with the referenced schema URI.
- custom keywords (in case keyword definition doesn't create errors) - property `keyword` (the keyword name).


## Related packages

- [ajv-async](https://github.com/epoberezkin/ajv-async) - configure async validation mode
- [ajv-cli](https://github.com/jessedc/ajv-cli) - command line interface
- [ajv-errors](https://github.com/epoberezkin/ajv-errors) - custom error messages
- [ajv-i18n](https://github.com/epoberezkin/ajv-i18n) - internationalised error messages
- [ajv-istanbul](https://github.com/epoberezkin/ajv-istanbul) - instrument generated validation code to measure test coverage of your schemas
- [ajv-keywords](https://github.com/epoberezkin/ajv-keywords) - custom validation keywords (if/then/else, select, typeof, etc.)
- [ajv-merge-patch](https://github.com/epoberezkin/ajv-merge-patch) - keywords $merge and $patch
- [ajv-pack](https://github.com/epoberezkin/ajv-pack) - produces a compact module exporting validation functions


## Some packages using Ajv

- [webpack](https://github.com/webpack/webpack) - a module bundler. Its main purpose is to bundle JavaScript files for usage in a browser
- [jsonscript-js](https://github.com/JSONScript/jsonscript-js) - the interpreter for [JSONScript](http://www.jsonscript.org) - scripted processing of existing endpoints and services
- [osprey-method-handler](https://github.com/mulesoft-labs/osprey-method-handler) - Express middleware for validating requests and responses based on a RAML method object, used in [osprey](https://github.com/mulesoft/osprey) - validating API proxy generated from a RAML definition
- [har-validator](https://github.com/ahmadnassri/har-validator) - HTTP Archive (HAR) validator
- [jsoneditor](https://github.com/josdejong/jsoneditor) - a web-based tool to view, edit, format, and validate JSON http://jsoneditoronline.org
- [JSON Schema Lint](https://github.com/nickcmaynard/jsonschemalint) - a web tool to validate JSON/YAML document against a single JSON-schema http://jsonschemalint.com
- [objection](https://github.com/vincit/objection.js) - SQL-friendly ORM for Node.js
- [table](https://github.com/gajus/table) - formats data into a string table
- [ripple-lib](https://github.com/ripple/ripple-lib) - a JavaScript API for interacting with [Ripple](https://ripple.com) in Node.js and the browser
- [restbase](https://github.com/wikimedia/restbase) - distributed storage with REST API & dispatcher for backend services built to provide a low-latency & high-throughput API for Wikipedia / Wikimedia content
- [hippie-swagger](https://github.com/CacheControl/hippie-swagger) - [Hippie](https://github.com/vesln/hippie) wrapper that provides end to end API testing with swagger validation
- [react-form-controlled](https://github.com/seeden/react-form-controlled) - React controlled form components with validation
- [rabbitmq-schema](https://github.com/tjmehta/rabbitmq-schema) - a schema definition module for RabbitMQ graphs and messages
- [@query/schema](https://www.npmjs.com/package/@query/schema) - stream filtering with a URI-safe query syntax parsing to JSON Schema
- [chai-ajv-json-schema](https://github.com/peon374/chai-ajv-json-schema) - chai plugin to us JSON-schema with expect in mocha tests
- [grunt-jsonschema-ajv](https://github.com/SignpostMarv/grunt-jsonschema-ajv) - Grunt plugin for validating files against JSON Schema
- [extract-text-webpack-plugin](https://github.com/webpack-contrib/extract-text-webpack-plugin) - extract text from bundle into a file
- [electron-builder](https://github.com/electron-userland/electron-builder) - a solution to package and build a ready for distribution Electron app
- [addons-linter](https://github.com/mozilla/addons-linter) - Mozilla Add-ons Linter
- [gh-pages-generator](https://github.com/epoberezkin/gh-pages-generator) - multi-page site generator converting markdown files to GitHub pages


## Tests

```
npm install
git submodule update --init
npm test
```

## Contributing

All validation functions are generated using doT templates in [dot](https://github.com/epoberezkin/ajv/tree/master/lib/dot) folder. Templates are precompiled so doT is not a run-time dependency.

`npm run build` - compiles templates to [dotjs](https://github.com/epoberezkin/ajv/tree/master/lib/dotjs) folder.

`npm run watch` - automatically compiles templates when files in dot folder change

Please see [Contributing guidelines](https://github.com/epoberezkin/ajv/blob/master/CONTRIBUTING.md)


## Changes history

See https://github.com/epoberezkin/ajv/releases

__Please note__: [Changes in version 5.0.0](https://github.com/epoberezkin/ajv/releases/tag/5.0.0).

[Changes in version 4.6.0](https://github.com/epoberezkin/ajv/releases/tag/4.6.0).

[Changes in version 4.0.0](https://github.com/epoberezkin/ajv/releases/tag/4.0.0).

[Changes in version 3.0.0](https://github.com/epoberezkin/ajv/releases/tag/3.0.0).

[Changes in version 2.0.0](https://github.com/epoberezkin/ajv/releases/tag/2.0.0).


## License

[MIT](https://github.com/epoberezkin/ajv/blob/master/LICENSE)
These files are compiled dot templates from dot folder.

Do NOT edit them directly, edit the templates and run `npm run build` from main ajv folder.
node-asn1 is a library for encoding and decoding ASN.1 datatypes in pure JS.
Currently BER encoding is supported; at some point I'll likely have to do DER.

## Usage

Mostly, if you're *actually* needing to read and write ASN.1, you probably don't
need this readme to explain what and why.  If you have no idea what ASN.1 is,
see this: ftp://ftp.rsa.com/pub/pkcs/ascii/layman.asc

The source is pretty much self-explanatory, and has read/write methods for the
common types out there.

### Decoding

The following reads an ASN.1 sequence with a boolean.

    var Ber = require('asn1').Ber;

    var reader = new Ber.Reader(Buffer.from([0x30, 0x03, 0x01, 0x01, 0xff]));

    reader.readSequence();
    console.log('Sequence len: ' + reader.length);
    if (reader.peek() === Ber.Boolean)
      console.log(reader.readBoolean());

### Encoding

The following generates the same payload as above.

    var Ber = require('asn1').Ber;

    var writer = new Ber.Writer();

    writer.startSequence();
    writer.writeBoolean(true);
    writer.endSequence();

    console.log(writer.buffer);

## Installation

    npm install asn1

## License

MIT.

## Bugs

See <https://github.com/joyent/node-asn1/issues>.
# once

Only call a function once.

## usage

```javascript
var once = require('once')

function load (file, cb) {
  cb = once(cb)
  loader.load('file')
  loader.once('load', cb)
  loader.once('error', cb)
}
```

Or add to the Function.prototype in a responsible way:

```javascript
// only has to be done once
require('once').proto()

function load (file, cb) {
  cb = cb.once()
  loader.load('file')
  loader.once('load', cb)
  loader.once('error', cb)
}
```

Ironically, the prototype feature makes this module twice as
complicated as necessary.

To check whether you function has been called, use `fn.called`. Once the
function is called for the first time the return value of the original
function is saved in `fn.value` and subsequent calls will continue to
return this value.

```javascript
var once = require('once')

function load (cb) {
  cb = once(cb)
  var stream = createStream()
  stream.once('data', cb)
  stream.once('end', function () {
    if (!cb.called) cb(new Error('not found'))
  })
}
```

## `once.strict(func)`

Throw an error if the function is called twice.

Some functions are expected to be called only once. Using `once` for them would
potentially hide logical errors.

In the example below, the `greet` function has to call the callback only once:

```javascript
function greet (name, cb) {
  // return is missing from the if statement
  // when no name is passed, the callback is called twice
  if (!name) cb('Hello anonymous')
  cb('Hello ' + name)
}

function log (msg) {
  console.log(msg)
}

// this will print 'Hello anonymous' but the logical error will be missed
greet(null, once(msg))

// once.strict will print 'Hello anonymous' and throw an error when the callback will be called the second time
greet(null, once.strict(msg))
```
forever-agent
=============

HTTP Agent that keeps socket connections alive between keep-alive requests. Formerly part of mikeal/request, now a standalone module.
# universalify

[![Travis branch](https://img.shields.io/travis/RyanZim/universalify/master.svg)](https://travis-ci.org/RyanZim/universalify)
![Coveralls github branch](https://img.shields.io/coveralls/github/RyanZim/universalify/master.svg)
![npm](https://img.shields.io/npm/dm/universalify.svg)
![npm](https://img.shields.io/npm/l/universalify.svg)

Make a callback- or promise-based function support both promises and callbacks.

Uses the native promise implementation.

## Installation

```bash
npm install universalify
```

## API

### `universalify.fromCallback(fn)`

Takes a callback-based function to universalify, and returns the universalified  function.

Function must take a callback as the last parameter that will be called with the signature `(error, result)`. `universalify` does not support calling the callback with more than three arguments, and does not ensure that the callback is only called once.

```js
function callbackFn (n, cb) {
  setTimeout(() => cb(null, n), 15)
}

const fn = universalify.fromCallback(callbackFn)

// Works with Promises:
fn('Hello World!')
.then(result => console.log(result)) // -> Hello World!
.catch(error => console.error(error))

// Works with Callbacks:
fn('Hi!', (error, result) => {
  if (error) return console.error(error)
  console.log(result)
  // -> Hi!
})
```

### `universalify.fromPromise(fn)`

Takes a promise-based function to universalify, and returns the universalified  function.

Function must return a valid JS promise. `universalify` does not ensure that a valid promise is returned.

```js
function promiseFn (n) {
  return new Promise(resolve => {
    setTimeout(() => resolve(n), 15)
  })
}

const fn = universalify.fromPromise(promiseFn)

// Works with Promises:
fn('Hello World!')
.then(result => console.log(result)) // -> Hello World!
.catch(error => console.error(error))

// Works with Callbacks:
fn('Hi!', (error, result) => {
  if (error) return console.error(error)
  console.log(result)
  // -> Hi!
})
```

## License

MIT
# balanced-match

Match balanced string pairs, like `{` and `}` or `<b>` and `</b>`. Supports regular expressions as well!

[![build status](https://secure.travis-ci.org/juliangruber/balanced-match.svg)](http://travis-ci.org/juliangruber/balanced-match)
[![downloads](https://img.shields.io/npm/dm/balanced-match.svg)](https://www.npmjs.org/package/balanced-match)

[![testling badge](https://ci.testling.com/juliangruber/balanced-match.png)](https://ci.testling.com/juliangruber/balanced-match)

## Example

Get the first matching pair of braces:

```js
var balanced = require('balanced-match');

console.log(balanced('{', '}', 'pre{in{nested}}post'));
console.log(balanced('{', '}', 'pre{first}between{second}post'));
console.log(balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'));
```

The matches are:

```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## API

### var m = balanced(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:

* **start** the index of the first match of `a`
* **end** the index of the matching `b`
* **pre** the preamble, `a` and `b` not included
* **body** the match, `a` and `b` not included
* **post** the postscript, `a` and `b` not included

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `['{', 'a', '']` and `{a}}` will match `['', 'a', '}']`.

### var r = balanced.range(a, b, str)

For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ <a index>, <b index> ]`.

If there's no match, `undefined` will be returned.

If the `str` contains more `a` than `b` / there are unmatched pairs, the first match that was closed will be used. For example, `{{a}` will match `[ 1, 3 ]` and `{a}}` will match `[0, 2]`.

## Installation

With [npm](https://npmjs.org) do:

```bash
npm install balanced-match
```

## License

(MIT)

Copyright (c) 2013 Julian Gruber &lt;julian@juliangruber.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# debug
[![Build Status](https://travis-ci.org/visionmedia/debug.svg?branch=master)](https://travis-ci.org/visionmedia/debug)  [![Coverage Status](https://coveralls.io/repos/github/visionmedia/debug/badge.svg?branch=master)](https://coveralls.io/github/visionmedia/debug?branch=master)  [![Slack](https://visionmedia-community-slackin.now.sh/badge.svg)](https://visionmedia-community-slackin.now.sh/) [![OpenCollective](https://opencollective.com/debug/backers/badge.svg)](#backers)
[![OpenCollective](https://opencollective.com/debug/sponsors/badge.svg)](#sponsors)

<img width="647" src="https://user-images.githubusercontent.com/71256/29091486-fa38524c-7c37-11e7-895f-e7ec8e1039b6.png">

A tiny JavaScript debugging utility modelled after Node.js core's debugging
technique. Works in Node.js and web browsers.

## Installation

```bash
$ npm install debug
```

## Usage

`debug` exposes a function; simply pass this function the name of your module, and it will return a decorated version of `console.error` for you to pass debug statements to. This will allow you to toggle the debug output for different parts of your module as well as the module as a whole.

Example [_app.js_](./examples/node/app.js):

```js
var debug = require('debug')('http')
  , http = require('http')
  , name = 'My App';

// fake app

debug('booting %o', name);

http.createServer(function(req, res){
  debug(req.method + ' ' + req.url);
  res.end('hello\n');
}).listen(3000, function(){
  debug('listening');
});

// fake worker of some kind

require('./worker');
```

Example [_worker.js_](./examples/node/worker.js):

```js
var a = require('debug')('worker:a')
  , b = require('debug')('worker:b');

function work() {
  a('doing lots of uninteresting work');
  setTimeout(work, Math.random() * 1000);
}

work();

function workb() {
  b('doing some work');
  setTimeout(workb, Math.random() * 2000);
}

workb();
```

The `DEBUG` environment variable is then used to enable these based on space or
comma-delimited names.

Here are some examples:

<img width="647" alt="screen shot 2017-08-08 at 12 53 04 pm" src="https://user-images.githubusercontent.com/71256/29091703-a6302cdc-7c38-11e7-8304-7c0b3bc600cd.png">
<img width="647" alt="screen shot 2017-08-08 at 12 53 38 pm" src="https://user-images.githubusercontent.com/71256/29091700-a62a6888-7c38-11e7-800b-db911291ca2b.png">
<img width="647" alt="screen shot 2017-08-08 at 12 53 25 pm" src="https://user-images.githubusercontent.com/71256/29091701-a62ea114-7c38-11e7-826a-2692bedca740.png">

#### Windows note

On Windows the environment variable is set using the `set` command.

```cmd
set DEBUG=*,-not_this
```

Note that PowerShell uses different syntax to set environment variables.

```cmd
$env:DEBUG = "*,-not_this"
```

Then, run the program to be debugged as usual.


## Namespace Colors

Every debug instance has a color generated for it based on its namespace name.
This helps when visually parsing the debug output to identify which debug instance
a debug line belongs to.

#### Node.js

In Node.js, colors are enabled when stderr is a TTY. You also _should_ install
the [`supports-color`](https://npmjs.org/supports-color) module alongside debug,
otherwise debug will only use a small handful of basic colors.

<img width="521" src="https://user-images.githubusercontent.com/71256/29092181-47f6a9e6-7c3a-11e7-9a14-1928d8a711cd.png">

#### Web Browser

Colors are also enabled on "Web Inspectors" that understand the `%c` formatting
option. These are WebKit web inspectors, Firefox ([since version
31](https://hacks.mozilla.org/2014/05/editable-box-model-multiple-selection-sublime-text-keys-much-more-firefox-developer-tools-episode-31/))
and the Firebug plugin for Firefox (any version).

<img width="524" src="https://user-images.githubusercontent.com/71256/29092033-b65f9f2e-7c39-11e7-8e32-f6f0d8e865c1.png">


## Millisecond diff

When actively developing an application it can be useful to see when the time spent between one `debug()` call and the next. Suppose for example you invoke `debug()` before requesting a resource, and after as well, the "+NNNms" will show you how much time was spent between calls.

<img width="647" src="https://user-images.githubusercontent.com/71256/29091486-fa38524c-7c37-11e7-895f-e7ec8e1039b6.png">

When stdout is not a TTY, `Date#toISOString()` is used, making it more useful for logging the debug information as shown below:

<img width="647" src="https://user-images.githubusercontent.com/71256/29091956-6bd78372-7c39-11e7-8c55-c948396d6edd.png">


## Conventions

If you're using this in one or more of your libraries, you _should_ use the name of your library so that developers may toggle debugging as desired without guessing names. If you have more than one debuggers you _should_ prefix them with your library name and use ":" to separate features. For example "bodyParser" from Connect would then be "connect:bodyParser".  If you append a "*" to the end of your name, it will always be enabled regardless of the setting of the DEBUG environment variable.  You can then use it for normal output as well as debug output.

## Wildcards

The `*` character may be used as a wildcard. Suppose for example your library has
debuggers named "connect:bodyParser", "connect:compress", "connect:session",
instead of listing all three with
`DEBUG=connect:bodyParser,connect:compress,connect:session`, you may simply do
`DEBUG=connect:*`, or to run everything using this module simply use `DEBUG=*`.

You can also exclude specific debuggers by prefixing them with a "-" character.
For example, `DEBUG=*,-connect:*` would include all debuggers except those
starting with "connect:".

## Environment Variables

When running through Node.js, you can set a few environment variables that will
change the behavior of the debug logging:

| Name      | Purpose                                         |
|-----------|-------------------------------------------------|
| `DEBUG`   | Enables/disables specific debugging namespaces. |
| `DEBUG_HIDE_DATE` | Hide date from debug output (non-TTY).  |
| `DEBUG_COLORS`| Whether or not to use colors in the debug output. |
| `DEBUG_DEPTH` | Object inspection depth.                    |
| `DEBUG_SHOW_HIDDEN` | Shows hidden properties on inspected objects. |


__Note:__ The environment variables beginning with `DEBUG_` end up being
converted into an Options object that gets used with `%o`/`%O` formatters.
See the Node.js documentation for
[`util.inspect()`](https://nodejs.org/api/util.html#util_util_inspect_object_options)
for the complete list.

## Formatters

Debug uses [printf-style](https://wikipedia.org/wiki/Printf_format_string) formatting.
Below are the officially supported formatters:

| Formatter | Representation |
|-----------|----------------|
| `%O`      | Pretty-print an Object on multiple lines. |
| `%o`      | Pretty-print an Object all on a single line. |
| `%s`      | String. |
| `%d`      | Number (both integer and float). |
| `%j`      | JSON. Replaced with the string '[Circular]' if the argument contains circular references. |
| `%%`      | Single percent sign ('%'). This does not consume an argument. |


### Custom formatters

You can add custom formatters by extending the `debug.formatters` object.
For example, if you wanted to add support for rendering a Buffer as hex with
`%h`, you could do something like:

```js
const createDebug = require('debug')
createDebug.formatters.h = (v) => {
  return v.toString('hex')
}

// …elsewhere
const debug = createDebug('foo')
debug('this is hex: %h', new Buffer('hello world'))
//   foo this is hex: 68656c6c6f20776f726c6421 +0ms
```


## Browser Support

You can build a browser-ready script using [browserify](https://github.com/substack/node-browserify),
or just use the [browserify-as-a-service](https://wzrd.in/) [build](https://wzrd.in/standalone/debug@latest),
if you don't want to build it yourself.

Debug's enable state is currently persisted by `localStorage`.
Consider the situation shown below where you have `worker:a` and `worker:b`,
and wish to debug both. You can enable this using `localStorage.debug`:

```js
localStorage.debug = 'worker:*'
```

And then refresh the page.

```js
a = debug('worker:a');
b = debug('worker:b');

setInterval(function(){
  a('doing some work');
}, 1000);

setInterval(function(){
  b('doing some work');
}, 1200);
```


## Output streams

  By default `debug` will log to stderr, however this can be configured per-namespace by overriding the `log` method:

Example [_stdout.js_](./examples/node/stdout.js):

```js
var debug = require('debug');
var error = debug('app:error');

// by default stderr is used
error('goes to stderr!');

var log = debug('app:log');
// set this namespace to log via console.log
log.log = console.log.bind(console); // don't forget to bind to console!
log('goes to stdout');
error('still goes to stderr!');

// set all output to go via console.info
// overrides all per-namespace log settings
debug.log = console.info.bind(console);
error('now goes to stdout via console.info');
log('still goes to stdout, but via console.info now');
```

## Checking whether a debug target is enabled

After you've created a debug instance, you can determine whether or not it is
enabled by checking the `enabled` property:

```javascript
const debug = require('debug')('http');

if (debug.enabled) {
  // do stuff...
}
```

You can also manually toggle this property to force the debug instance to be
enabled or disabled.


## Authors

 - TJ Holowaychuk
 - Nathan Rajlich
 - Andrew Rhyne

## Backers

Support us with a monthly donation and help us continue our activities. [[Become a backer](https://opencollective.com/debug#backer)]

<a href="https://opencollective.com/debug/backer/0/website" target="_blank"><img src="https://opencollective.com/debug/backer/0/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/1/website" target="_blank"><img src="https://opencollective.com/debug/backer/1/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/2/website" target="_blank"><img src="https://opencollective.com/debug/backer/2/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/3/website" target="_blank"><img src="https://opencollective.com/debug/backer/3/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/4/website" target="_blank"><img src="https://opencollective.com/debug/backer/4/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/5/website" target="_blank"><img src="https://opencollective.com/debug/backer/5/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/6/website" target="_blank"><img src="https://opencollective.com/debug/backer/6/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/7/website" target="_blank"><img src="https://opencollective.com/debug/backer/7/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/8/website" target="_blank"><img src="https://opencollective.com/debug/backer/8/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/9/website" target="_blank"><img src="https://opencollective.com/debug/backer/9/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/10/website" target="_blank"><img src="https://opencollective.com/debug/backer/10/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/11/website" target="_blank"><img src="https://opencollective.com/debug/backer/11/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/12/website" target="_blank"><img src="https://opencollective.com/debug/backer/12/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/13/website" target="_blank"><img src="https://opencollective.com/debug/backer/13/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/14/website" target="_blank"><img src="https://opencollective.com/debug/backer/14/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/15/website" target="_blank"><img src="https://opencollective.com/debug/backer/15/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/16/website" target="_blank"><img src="https://opencollective.com/debug/backer/16/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/17/website" target="_blank"><img src="https://opencollective.com/debug/backer/17/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/18/website" target="_blank"><img src="https://opencollective.com/debug/backer/18/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/19/website" target="_blank"><img src="https://opencollective.com/debug/backer/19/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/20/website" target="_blank"><img src="https://opencollective.com/debug/backer/20/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/21/website" target="_blank"><img src="https://opencollective.com/debug/backer/21/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/22/website" target="_blank"><img src="https://opencollective.com/debug/backer/22/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/23/website" target="_blank"><img src="https://opencollective.com/debug/backer/23/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/24/website" target="_blank"><img src="https://opencollective.com/debug/backer/24/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/25/website" target="_blank"><img src="https://opencollective.com/debug/backer/25/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/26/website" target="_blank"><img src="https://opencollective.com/debug/backer/26/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/27/website" target="_blank"><img src="https://opencollective.com/debug/backer/27/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/28/website" target="_blank"><img src="https://opencollective.com/debug/backer/28/avatar.svg"></a>
<a href="https://opencollective.com/debug/backer/29/website" target="_blank"><img src="https://opencollective.com/debug/backer/29/avatar.svg"></a>


## Sponsors

Become a sponsor and get your logo on our README on Github with a link to your site. [[Become a sponsor](https://opencollective.com/debug#sponsor)]

<a href="https://opencollective.com/debug/sponsor/0/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/1/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/2/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/3/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/4/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/5/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/6/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/7/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/8/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/9/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/9/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/10/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/10/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/11/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/11/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/12/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/12/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/13/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/13/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/14/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/14/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/15/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/15/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/16/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/16/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/17/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/17/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/18/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/18/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/19/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/19/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/20/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/20/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/21/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/21/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/22/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/22/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/23/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/23/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/24/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/24/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/25/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/25/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/26/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/26/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/27/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/27/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/28/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/28/avatar.svg"></a>
<a href="https://opencollective.com/debug/sponsor/29/website" target="_blank"><img src="https://opencollective.com/debug/sponsor/29/avatar.svg"></a>

## License

(The MIT License)

Copyright (c) 2014-2017 TJ Holowaychuk &lt;tj@vision-media.ca&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
semver(1) -- The semantic versioner for npm
===========================================

## Install

```bash
npm install --save semver
````

## Usage

As a node module:

```js
const semver = require('semver')

semver.valid('1.2.3') // '1.2.3'
semver.valid('a.b.c') // null
semver.clean('  =v1.2.3   ') // '1.2.3'
semver.satisfies('1.2.3', '1.x || >=2.5.0 || 5.0.0 - 7.2.3') // true
semver.gt('1.2.3', '9.8.7') // false
semver.lt('1.2.3', '9.8.7') // true
semver.valid(semver.coerce('v2')) // '2.0.0'
semver.valid(semver.coerce('42.6.7.9.3-alpha')) // '42.6.7'
```

As a command-line utility:

```
$ semver -h

SemVer 5.3.0

A JavaScript implementation of the http://semver.org/ specification
Copyright Isaac Z. Schlueter

Usage: semver [options] <version> [<version> [...]]
Prints valid versions sorted by SemVer precedence

Options:
-r --range <range>
        Print versions that match the specified range.

-i --increment [<level>]
        Increment a version by the specified level.  Level can
        be one of: major, minor, patch, premajor, preminor,
        prepatch, or prerelease.  Default level is 'patch'.
        Only one version may be specified.

--preid <identifier>
        Identifier to be used to prefix premajor, preminor,
        prepatch or prerelease version increments.

-l --loose
        Interpret versions and ranges loosely

-c --coerce
        Coerce a string into SemVer if possible
        (does not imply --loose)

Program exits successfully if any valid version satisfies
all supplied ranges, and prints all satisfying versions.

If no satisfying versions are found, then exits failure.

Versions are printed in ascending order, so supplying
multiple versions to the utility will just sort them.
```

## Versions

A "version" is described by the `v2.0.0` specification found at
<http://semver.org/>.

A leading `"="` or `"v"` character is stripped off and ignored.

## Ranges

A `version range` is a set of `comparators` which specify versions
that satisfy the range.

A `comparator` is composed of an `operator` and a `version`.  The set
of primitive `operators` is:

* `<` Less than
* `<=` Less than or equal to
* `>` Greater than
* `>=` Greater than or equal to
* `=` Equal.  If no operator is specified, then equality is assumed,
  so this operator is optional, but MAY be included.

For example, the comparator `>=1.2.7` would match the versions
`1.2.7`, `1.2.8`, `2.5.3`, and `1.3.9`, but not the versions `1.2.6`
or `1.1.0`.

Comparators can be joined by whitespace to form a `comparator set`,
which is satisfied by the **intersection** of all of the comparators
it includes.

A range is composed of one or more comparator sets, joined by `||`.  A
version matches a range if and only if every comparator in at least
one of the `||`-separated comparator sets is satisfied by the version.

For example, the range `>=1.2.7 <1.3.0` would match the versions
`1.2.7`, `1.2.8`, and `1.2.99`, but not the versions `1.2.6`, `1.3.0`,
or `1.1.0`.

The range `1.2.7 || >=1.2.9 <2.0.0` would match the versions `1.2.7`,
`1.2.9`, and `1.4.6`, but not the versions `1.2.8` or `2.0.0`.

### Prerelease Tags

If a version has a prerelease tag (for example, `1.2.3-alpha.3`) then
it will only be allowed to satisfy comparator sets if at least one
comparator with the same `[major, minor, patch]` tuple also has a
prerelease tag.

For example, the range `>1.2.3-alpha.3` would be allowed to match the
version `1.2.3-alpha.7`, but it would *not* be satisfied by
`3.4.5-alpha.9`, even though `3.4.5-alpha.9` is technically "greater
than" `1.2.3-alpha.3` according to the SemVer sort rules.  The version
range only accepts prerelease tags on the `1.2.3` version.  The
version `3.4.5` *would* satisfy the range, because it does not have a
prerelease flag, and `3.4.5` is greater than `1.2.3-alpha.7`.

The purpose for this behavior is twofold.  First, prerelease versions
frequently are updated very quickly, and contain many breaking changes
that are (by the author's design) not yet fit for public consumption.
Therefore, by default, they are excluded from range matching
semantics.

Second, a user who has opted into using a prerelease version has
clearly indicated the intent to use *that specific* set of
alpha/beta/rc versions.  By including a prerelease tag in the range,
the user is indicating that they are aware of the risk.  However, it
is still not appropriate to assume that they have opted into taking a
similar risk on the *next* set of prerelease versions.

#### Prerelease Identifiers

The method `.inc` takes an additional `identifier` string argument that
will append the value of the string as a prerelease identifier:

```javascript
semver.inc('1.2.3', 'prerelease', 'beta')
// '1.2.4-beta.0'
```

command-line example:

```bash
$ semver 1.2.3 -i prerelease --preid beta
1.2.4-beta.0
```

Which then can be used to increment further:

```bash
$ semver 1.2.4-beta.0 -i prerelease
1.2.4-beta.1
```

### Advanced Range Syntax

Advanced range syntax desugars to primitive comparators in
deterministic ways.

Advanced ranges may be combined in the same way as primitive
comparators using white space or `||`.

#### Hyphen Ranges `X.Y.Z - A.B.C`

Specifies an inclusive set.

* `1.2.3 - 2.3.4` := `>=1.2.3 <=2.3.4`

If a partial version is provided as the first version in the inclusive
range, then the missing pieces are replaced with zeroes.

* `1.2 - 2.3.4` := `>=1.2.0 <=2.3.4`

If a partial version is provided as the second version in the
inclusive range, then all versions that start with the supplied parts
of the tuple are accepted, but nothing that would be greater than the
provided tuple parts.

* `1.2.3 - 2.3` := `>=1.2.3 <2.4.0`
* `1.2.3 - 2` := `>=1.2.3 <3.0.0`

#### X-Ranges `1.2.x` `1.X` `1.2.*` `*`

Any of `X`, `x`, or `*` may be used to "stand in" for one of the
numeric values in the `[major, minor, patch]` tuple.

* `*` := `>=0.0.0` (Any version satisfies)
* `1.x` := `>=1.0.0 <2.0.0` (Matching major version)
* `1.2.x` := `>=1.2.0 <1.3.0` (Matching major and minor versions)

A partial version range is treated as an X-Range, so the special
character is in fact optional.

* `""` (empty string) := `*` := `>=0.0.0`
* `1` := `1.x.x` := `>=1.0.0 <2.0.0`
* `1.2` := `1.2.x` := `>=1.2.0 <1.3.0`

#### Tilde Ranges `~1.2.3` `~1.2` `~1`

Allows patch-level changes if a minor version is specified on the
comparator.  Allows minor-level changes if not.

* `~1.2.3` := `>=1.2.3 <1.(2+1).0` := `>=1.2.3 <1.3.0`
* `~1.2` := `>=1.2.0 <1.(2+1).0` := `>=1.2.0 <1.3.0` (Same as `1.2.x`)
* `~1` := `>=1.0.0 <(1+1).0.0` := `>=1.0.0 <2.0.0` (Same as `1.x`)
* `~0.2.3` := `>=0.2.3 <0.(2+1).0` := `>=0.2.3 <0.3.0`
* `~0.2` := `>=0.2.0 <0.(2+1).0` := `>=0.2.0 <0.3.0` (Same as `0.2.x`)
* `~0` := `>=0.0.0 <(0+1).0.0` := `>=0.0.0 <1.0.0` (Same as `0.x`)
* `~1.2.3-beta.2` := `>=1.2.3-beta.2 <1.3.0` Note that prereleases in
  the `1.2.3` version will be allowed, if they are greater than or
  equal to `beta.2`.  So, `1.2.3-beta.4` would be allowed, but
  `1.2.4-beta.2` would not, because it is a prerelease of a
  different `[major, minor, patch]` tuple.

#### Caret Ranges `^1.2.3` `^0.2.5` `^0.0.4`

Allows changes that do not modify the left-most non-zero digit in the
`[major, minor, patch]` tuple.  In other words, this allows patch and
minor updates for versions `1.0.0` and above, patch updates for
versions `0.X >=0.1.0`, and *no* updates for versions `0.0.X`.

Many authors treat a `0.x` version as if the `x` were the major
"breaking-change" indicator.

Caret ranges are ideal when an author may make breaking changes
between `0.2.4` and `0.3.0` releases, which is a common practice.
However, it presumes that there will *not* be breaking changes between
`0.2.4` and `0.2.5`.  It allows for changes that are presumed to be
additive (but non-breaking), according to commonly observed practices.

* `^1.2.3` := `>=1.2.3 <2.0.0`
* `^0.2.3` := `>=0.2.3 <0.3.0`
* `^0.0.3` := `>=0.0.3 <0.0.4`
* `^1.2.3-beta.2` := `>=1.2.3-beta.2 <2.0.0` Note that prereleases in
  the `1.2.3` version will be allowed, if they are greater than or
  equal to `beta.2`.  So, `1.2.3-beta.4` would be allowed, but
  `1.2.4-beta.2` would not, because it is a prerelease of a
  different `[major, minor, patch]` tuple.
* `^0.0.3-beta` := `>=0.0.3-beta <0.0.4`  Note that prereleases in the
  `0.0.3` version *only* will be allowed, if they are greater than or
  equal to `beta`.  So, `0.0.3-pr.2` would be allowed.

When parsing caret ranges, a missing `patch` value desugars to the
number `0`, but will allow flexibility within that value, even if the
major and minor versions are both `0`.

* `^1.2.x` := `>=1.2.0 <2.0.0`
* `^0.0.x` := `>=0.0.0 <0.1.0`
* `^0.0` := `>=0.0.0 <0.1.0`

A missing `minor` and `patch` values will desugar to zero, but also
allow flexibility within those values, even if the major version is
zero.

* `^1.x` := `>=1.0.0 <2.0.0`
* `^0.x` := `>=0.0.0 <1.0.0`

### Range Grammar

Putting all this together, here is a Backus-Naur grammar for ranges,
for the benefit of parser authors:

```bnf
range-set  ::= range ( logical-or range ) *
logical-or ::= ( ' ' ) * '||' ( ' ' ) *
range      ::= hyphen | simple ( ' ' simple ) * | ''
hyphen     ::= partial ' - ' partial
simple     ::= primitive | partial | tilde | caret
primitive  ::= ( '<' | '>' | '>=' | '<=' | '=' ) partial
partial    ::= xr ( '.' xr ( '.' xr qualifier ? )? )?
xr         ::= 'x' | 'X' | '*' | nr
nr         ::= '0' | ['1'-'9'] ( ['0'-'9'] ) *
tilde      ::= '~' partial
caret      ::= '^' partial
qualifier  ::= ( '-' pre )? ( '+' build )?
pre        ::= parts
build      ::= parts
parts      ::= part ( '.' part ) *
part       ::= nr | [-0-9A-Za-z]+
```

## Functions

All methods and classes take a final `loose` boolean argument that, if
true, will be more forgiving about not-quite-valid semver strings.
The resulting output will always be 100% strict, of course.

Strict-mode Comparators and Ranges will be strict about the SemVer
strings that they parse.

* `valid(v)`: Return the parsed version, or null if it's not valid.
* `inc(v, release)`: Return the version incremented by the release
  type (`major`,   `premajor`, `minor`, `preminor`, `patch`,
  `prepatch`, or `prerelease`), or null if it's not valid
  * `premajor` in one call will bump the version up to the next major
    version and down to a prerelease of that major version.
    `preminor`, and `prepatch` work the same way.
  * If called from a non-prerelease version, the `prerelease` will work the
    same as `prepatch`. It increments the patch version, then makes a
    prerelease. If the input version is already a prerelease it simply
    increments it.
* `prerelease(v)`: Returns an array of prerelease components, or null
  if none exist. Example: `prerelease('1.2.3-alpha.1') -> ['alpha', 1]`
* `major(v)`: Return the major version number.
* `minor(v)`: Return the minor version number.
* `patch(v)`: Return the patch version number.
* `intersects(r1, r2, loose)`: Return true if the two supplied ranges
  or comparators intersect.

### Comparison

* `gt(v1, v2)`: `v1 > v2`
* `gte(v1, v2)`: `v1 >= v2`
* `lt(v1, v2)`: `v1 < v2`
* `lte(v1, v2)`: `v1 <= v2`
* `eq(v1, v2)`: `v1 == v2` This is true if they're logically equivalent,
  even if they're not the exact same string.  You already know how to
  compare strings.
* `neq(v1, v2)`: `v1 != v2` The opposite of `eq`.
* `cmp(v1, comparator, v2)`: Pass in a comparison string, and it'll call
  the corresponding function above.  `"==="` and `"!=="` do simple
  string comparison, but are included for completeness.  Throws if an
  invalid comparison string is provided.
* `compare(v1, v2)`: Return `0` if `v1 == v2`, or `1` if `v1` is greater, or `-1` if
  `v2` is greater.  Sorts in ascending order if passed to `Array.sort()`.
* `rcompare(v1, v2)`: The reverse of compare.  Sorts an array of versions
  in descending order when passed to `Array.sort()`.
* `diff(v1, v2)`: Returns difference between two versions by the release type
  (`major`, `premajor`, `minor`, `preminor`, `patch`, `prepatch`, or `prerelease`),
  or null if the versions are the same.

### Comparators

* `intersects(comparator)`: Return true if the comparators intersect

### Ranges

* `validRange(range)`: Return the valid range or null if it's not valid
* `satisfies(version, range)`: Return true if the version satisfies the
  range.
* `maxSatisfying(versions, range)`: Return the highest version in the list
  that satisfies the range, or `null` if none of them do.
* `minSatisfying(versions, range)`: Return the lowest version in the list
  that satisfies the range, or `null` if none of them do.
* `gtr(version, range)`: Return `true` if version is greater than all the
  versions possible in the range.
* `ltr(version, range)`: Return `true` if version is less than all the
  versions possible in the range.
* `outside(version, range, hilo)`: Return true if the version is outside
  the bounds of the range in either the high or low direction.  The
  `hilo` argument must be either the string `'>'` or `'<'`.  (This is
  the function called by `gtr` and `ltr`.)
* `intersects(range)`: Return true if any of the ranges comparators intersect

Note that, since ranges may be non-contiguous, a version might not be
greater than a range, less than a range, *or* satisfy a range!  For
example, the range `1.2 <1.2.9 || >2.0.0` would have a hole from `1.2.9`
until `2.0.0`, so the version `1.2.10` would not be greater than the
range (because `2.0.1` satisfies, which is higher), nor less than the
range (since `1.2.8` satisfies, which is lower), and it also does not
satisfy the range.

If you want to know if a version satisfies or does not satisfy a
range, use the `satisfies(version, range)` function.

### Coercion

* `coerce(version)`: Coerces a string to semver if possible

This aims to provide a very forgiving translation of a non-semver
string to semver. It looks for the first digit in a string, and
consumes all remaining characters which satisfy at least a partial semver
(e.g., `1`, `1.2`, `1.2.3`) up to the max permitted length (256 characters).
Longer versions are simply truncated (`4.6.3.9.2-alpha2` becomes `4.6.3`).
All surrounding text is simply ignored (`v3.4 replaces v3.3.1` becomes `3.4.0`).
Only text which lacks digits will fail coercion (`version one` is not valid).
The maximum  length for any semver component considered for coercion is 16 characters;
longer components will be ignored (`10000000000000000.4.7.4` becomes `4.7.4`).
The maximum value for any semver component is `Integer.MAX_SAFE_INTEGER || (2**53 - 1)`;
higher value components are invalid (`9999999999999999.4.7.4` is likely invalid).
# lodash.once v4.1.1

The [lodash](https://lodash.com/) method `_.once` exported as a [Node.js](https://nodejs.org/) module.

## Installation

Using npm:
```bash
$ {sudo -H} npm i -g npm
$ npm i --save lodash.once
```

In Node.js:
```js
var once = require('lodash.once');
```

See the [documentation](https://lodash.com/docs#once) or [package source](https://github.com/lodash/lodash/blob/4.1.1-npm-packages/lodash.once) for more details.
# is-typedarray [![locked](http://badges.github.io/stability-badges/dist/locked.svg)](http://github.com/badges/stability-badges)

Detect whether or not an object is a
[Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays).

## Usage

[![NPM](https://nodei.co/npm/is-typedarray.png)](https://nodei.co/npm/is-typedarray/)

### isTypedArray(array)

Returns `true` when array is a Typed Array, and `false` when it is not.

## License

MIT. See [LICENSE.md](http://github.com/hughsk/is-typedarray/blob/master/LICENSE.md) for details.
# node-url

[![Build Status](https://travis-ci.org/defunctzombie/node-url.svg?branch=master)](https://travis-ci.org/defunctzombie/node-url)

This module has utilities for URL resolution and parsing meant to have feature parity with node.js core [url](http://nodejs.org/api/url.html) module.

```js
var url = require('url');
```

## api

Parsed URL objects have some or all of the following fields, depending on
whether or not they exist in the URL string. Any parts that are not in the URL
string will not be in the parsed object. Examples are shown for the URL

`'http://user:pass@host.com:8080/p/a/t/h?query=string#hash'`

* `href`: The full URL that was originally parsed. Both the protocol and host are lowercased.

    Example: `'http://user:pass@host.com:8080/p/a/t/h?query=string#hash'`

* `protocol`: The request protocol, lowercased.

    Example: `'http:'`

* `host`: The full lowercased host portion of the URL, including port
  information.

    Example: `'host.com:8080'`

* `auth`: The authentication information portion of a URL.

    Example: `'user:pass'`

* `hostname`: Just the lowercased hostname portion of the host.

    Example: `'host.com'`

* `port`: The port number portion of the host.

    Example: `'8080'`

* `pathname`: The path section of the URL, that comes after the host and
  before the query, including the initial slash if present.

    Example: `'/p/a/t/h'`

* `search`: The 'query string' portion of the URL, including the leading
  question mark.

    Example: `'?query=string'`

* `path`: Concatenation of `pathname` and `search`.

    Example: `'/p/a/t/h?query=string'`

* `query`: Either the 'params' portion of the query string, or a
  querystring-parsed object.

    Example: `'query=string'` or `{'query':'string'}`

* `hash`: The 'fragment' portion of the URL including the pound-sign.

    Example: `'#hash'`

The following methods are provided by the URL module:

### url.parse(urlStr, [parseQueryString], [slashesDenoteHost])

Take a URL string, and return an object.

Pass `true` as the second argument to also parse
the query string using the `querystring` module.
Defaults to `false`.

Pass `true` as the third argument to treat `//foo/bar` as
`{ host: 'foo', pathname: '/bar' }` rather than
`{ pathname: '//foo/bar' }`. Defaults to `false`.

### url.format(urlObj)

Take a parsed URL object, and return a formatted URL string.

* `href` will be ignored.
* `protocol` is treated the same with or without the trailing `:` (colon).
  * The protocols `http`, `https`, `ftp`, `gopher`, `file` will be
    postfixed with `://` (colon-slash-slash).
  * All other protocols `mailto`, `xmpp`, `aim`, `sftp`, `foo`, etc will
    be postfixed with `:` (colon)
* `auth` will be used if present.
* `hostname` will only be used if `host` is absent.
* `port` will only be used if `host` is absent.
* `host` will be used in place of `hostname` and `port`
* `pathname` is treated the same with or without the leading `/` (slash)
* `search` will be used in place of `query`
* `query` (object; see `querystring`) will only be used if `search` is absent.
* `search` is treated the same with or without the leading `?` (question mark)
* `hash` is treated the same with or without the leading `#` (pound sign, anchor)

### url.resolve(from, to)

Take a base URL, and a href URL, and resolve them as a browser would for
an anchor tag.  Examples:

    url.resolve('/one/two/three', 'four')         // '/one/two/four'
    url.resolve('http://example.com/', '/one')    // 'http://example.com/one'
    url.resolve('http://example.com/one', '/two') // 'http://example.com/two'
# Punycode.js [![Build status](https://travis-ci.org/bestiejs/punycode.js.svg?branch=master)](https://travis-ci.org/bestiejs/punycode.js) [![Code coverage status](http://img.shields.io/coveralls/bestiejs/punycode.js/master.svg)](https://coveralls.io/r/bestiejs/punycode.js) [![Dependency status](https://gemnasium.com/bestiejs/punycode.js.svg)](https://gemnasium.com/bestiejs/punycode.js)

A robust Punycode converter that fully complies to [RFC 3492](http://tools.ietf.org/html/rfc3492) and [RFC 5891](http://tools.ietf.org/html/rfc5891), and works on nearly all JavaScript platforms.

This JavaScript library is the result of comparing, optimizing and documenting different open-source implementations of the Punycode algorithm:

* [The C example code from RFC 3492](http://tools.ietf.org/html/rfc3492#appendix-C)
* [`punycode.c` by _Markus W. Scherer_ (IBM)](http://opensource.apple.com/source/ICU/ICU-400.42/icuSources/common/punycode.c)
* [`punycode.c` by _Ben Noordhuis_](https://github.com/bnoordhuis/punycode/blob/master/punycode.c)
* [JavaScript implementation by _some_](http://stackoverflow.com/questions/183485/can-anyone-recommend-a-good-free-javascript-for-punycode-to-unicode-conversion/301287#301287)
* [`punycode.js` by _Ben Noordhuis_](https://github.com/joyent/node/blob/426298c8c1c0d5b5224ac3658c41e7c2a3fe9377/lib/punycode.js) (note: [not fully compliant](https://github.com/joyent/node/issues/2072))

This project is [bundled](https://github.com/joyent/node/blob/master/lib/punycode.js) with [Node.js v0.6.2+](https://github.com/joyent/node/compare/975f1930b1...61e796decc).

## Installation

Via [npm](http://npmjs.org/) (only required for Node.js releases older than v0.6.2):

```bash
npm install punycode
```

Via [Bower](http://bower.io/):

```bash
bower install punycode
```

Via [Component](https://github.com/component/component):

```bash
component install bestiejs/punycode.js
```

In a browser:

```html
<script src="punycode.js"></script>
```

In [Narwhal](http://narwhaljs.org/), [Node.js](http://nodejs.org/), and [RingoJS](http://ringojs.org/):

```js
var punycode = require('punycode');
```

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('punycode.js');
```

Using an AMD loader like [RequireJS](http://requirejs.org/):

```js
require(
  {
    'paths': {
      'punycode': 'path/to/punycode'
    }
  },
  ['punycode'],
  function(punycode) {
    console.log(punycode);
  }
);
```

## API

### `punycode.decode(string)`

Converts a Punycode string of ASCII symbols to a string of Unicode symbols.

```js
// decode domain name parts
punycode.decode('maana-pta'); // 'mañana'
punycode.decode('--dqo34k'); // '☃-⌘'
```

### `punycode.encode(string)`

Converts a string of Unicode symbols to a Punycode string of ASCII symbols.

```js
// encode domain name parts
punycode.encode('mañana'); // 'maana-pta'
punycode.encode('☃-⌘'); // '--dqo34k'
```

### `punycode.toUnicode(input)`

Converts a Punycode string representing a domain name or an email address to Unicode. Only the Punycoded parts of the input will be converted, i.e. it doesn’t matter if you call it on a string that has already been converted to Unicode.

```js
// decode domain names
punycode.toUnicode('xn--maana-pta.com');
// → 'mañana.com'
punycode.toUnicode('xn----dqo34k.com');
// → '☃-⌘.com'

// decode email addresses
punycode.toUnicode('джумла@xn--p-8sbkgc5ag7bhce.xn--ba-lmcq');
// → 'джумла@джpумлатест.bрфa'
```

### `punycode.toASCII(input)`

Converts a Unicode string representing a domain name or an email address to Punycode. Only the non-ASCII parts of the input will be converted, i.e. it doesn’t matter if you call it with a domain that's already in ASCII.

```js
// encode domain names
punycode.toASCII('mañana.com');
// → 'xn--maana-pta.com'
punycode.toASCII('☃-⌘.com');
// → 'xn----dqo34k.com'

// encode email addresses
punycode.toASCII('джумла@джpумлатест.bрфa');
// → 'джумла@xn--p-8sbkgc5ag7bhce.xn--ba-lmcq'
```

### `punycode.ucs2`

#### `punycode.ucs2.decode(string)`

Creates an array containing the numeric code point values of each Unicode symbol in the string. While [JavaScript uses UCS-2 internally](https://mathiasbynens.be/notes/javascript-encoding), this function will convert a pair of surrogate halves (each of which UCS-2 exposes as separate characters) into a single code point, matching UTF-16.

```js
punycode.ucs2.decode('abc');
// → [0x61, 0x62, 0x63]
// surrogate pair for U+1D306 TETRAGRAM FOR CENTRE:
punycode.ucs2.decode('\uD834\uDF06');
// → [0x1D306]
```

#### `punycode.ucs2.encode(codePoints)`

Creates a string based on an array of numeric code point values.

```js
punycode.ucs2.encode([0x61, 0x62, 0x63]);
// → 'abc'
punycode.ucs2.encode([0x1D306]);
// → '\uD834\uDF06'
```

### `punycode.version`

A string representing the current Punycode.js version number.

## Unit tests & code coverage

After cloning this repository, run `npm install --dev` to install the dependencies needed for Punycode.js development and testing. You may want to install Istanbul _globally_ using `npm install istanbul -g`.

Once that’s done, you can run the unit tests in Node using `npm test` or `node tests/tests.js`. To run the tests in Rhino, Ringo, Narwhal, PhantomJS, and web browsers as well, use `grunt test`.

To generate the code coverage report, use `grunt cover`.

Feel free to fork if you see possible improvements!

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## Contributors

| [![twitter/jdalton](https://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter") |
|---|
| [John-David Dalton](http://allyoucanleet.com/) |

## License

Punycode.js is available under the [MIT](https://mths.be/mit) license.
# Glob

Match files using the patterns the shell uses, like stars and stuff.

[![Build Status](https://travis-ci.org/isaacs/node-glob.svg?branch=master)](https://travis-ci.org/isaacs/node-glob/) [![Build Status](https://ci.appveyor.com/api/projects/status/kd7f3yftf7unxlsx?svg=true)](https://ci.appveyor.com/project/isaacs/node-glob) [![Coverage Status](https://coveralls.io/repos/isaacs/node-glob/badge.svg?branch=master&service=github)](https://coveralls.io/github/isaacs/node-glob?branch=master)

This is a glob implementation in JavaScript.  It uses the `minimatch`
library to do its matching.

![](oh-my-glob.gif)

## Usage

Install with npm

```
npm i glob
```

```javascript
var glob = require("glob")

// options is optional
glob("**/*.js", options, function (er, files) {
  // files is an array of filenames.
  // If the `nonull` option is set, and nothing
  // was found, then files is ["**/*.js"]
  // er is an error object or null.
})
```

## Glob Primer

"Globs" are the patterns you type when you do stuff like `ls *.js` on
the command line, or put `build/*` in a `.gitignore` file.

Before parsing the path part patterns, braced sections are expanded
into a set.  Braced sections start with `{` and end with `}`, with any
number of comma-delimited sections within.  Braced sections may contain
slash characters, so `a{/b/c,bcd}` would expand into `a/b/c` and `abcd`.

The following characters have special magic meaning when used in a
path portion:

* `*` Matches 0 or more characters in a single path portion
* `?` Matches 1 character
* `[...]` Matches a range of characters, similar to a RegExp range.
  If the first character of the range is `!` or `^` then it matches
  any character not in the range.
* `!(pattern|pattern|pattern)` Matches anything that does not match
  any of the patterns provided.
* `?(pattern|pattern|pattern)` Matches zero or one occurrence of the
  patterns provided.
* `+(pattern|pattern|pattern)` Matches one or more occurrences of the
  patterns provided.
* `*(a|b|c)` Matches zero or more occurrences of the patterns provided
* `@(pattern|pat*|pat?erN)` Matches exactly one of the patterns
  provided
* `**` If a "globstar" is alone in a path portion, then it matches
  zero or more directories and subdirectories searching for matches.
  It does not crawl symlinked directories.

### Dots

If a file or directory path portion has a `.` as the first character,
then it will not match any glob pattern unless that pattern's
corresponding path part also has a `.` as its first character.

For example, the pattern `a/.*/c` would match the file at `a/.b/c`.
However the pattern `a/*/c` would not, because `*` does not start with
a dot character.

You can make glob treat dots as normal characters by setting
`dot:true` in the options.

### Basename Matching

If you set `matchBase:true` in the options, and the pattern has no
slashes in it, then it will seek for any file anywhere in the tree
with a matching basename.  For example, `*.js` would match
`test/simple/basic.js`.

### Empty Sets

If no matching files are found, then an empty array is returned.  This
differs from the shell, where the pattern itself is returned.  For
example:

    $ echo a*s*d*f
    a*s*d*f

To get the bash-style behavior, set the `nonull:true` in the options.

### See Also:

* `man sh`
* `man bash` (Search for "Pattern Matching")
* `man 3 fnmatch`
* `man 5 gitignore`
* [minimatch documentation](https://github.com/isaacs/minimatch)

## glob.hasMagic(pattern, [options])

Returns `true` if there are any special characters in the pattern, and
`false` otherwise.

Note that the options affect the results.  If `noext:true` is set in
the options object, then `+(a|b)` will not be considered a magic
pattern.  If the pattern has a brace expansion, like `a/{b/c,x/y}`
then that is considered magical, unless `nobrace:true` is set in the
options.

## glob(pattern, [options], cb)

* `pattern` `{String}` Pattern to be matched
* `options` `{Object}`
* `cb` `{Function}`
  * `err` `{Error | null}`
  * `matches` `{Array<String>}` filenames found matching the pattern

Perform an asynchronous glob search.

## glob.sync(pattern, [options])

* `pattern` `{String}` Pattern to be matched
* `options` `{Object}`
* return: `{Array<String>}` filenames found matching the pattern

Perform a synchronous glob search.

## Class: glob.Glob

Create a Glob object by instantiating the `glob.Glob` class.

```javascript
var Glob = require("glob").Glob
var mg = new Glob(pattern, options, cb)
```

It's an EventEmitter, and starts walking the filesystem to find matches
immediately.

### new glob.Glob(pattern, [options], [cb])

* `pattern` `{String}` pattern to search for
* `options` `{Object}`
* `cb` `{Function}` Called when an error occurs, or matches are found
  * `err` `{Error | null}`
  * `matches` `{Array<String>}` filenames found matching the pattern

Note that if the `sync` flag is set in the options, then matches will
be immediately available on the `g.found` member.

### Properties

* `minimatch` The minimatch object that the glob uses.
* `options` The options object passed in.
* `aborted` Boolean which is set to true when calling `abort()`.  There
  is no way at this time to continue a glob search after aborting, but
  you can re-use the statCache to avoid having to duplicate syscalls.
* `cache` Convenience object.  Each field has the following possible
  values:
  * `false` - Path does not exist
  * `true` - Path exists
  * `'FILE'` - Path exists, and is not a directory
  * `'DIR'` - Path exists, and is a directory
  * `[file, entries, ...]` - Path exists, is a directory, and the
    array value is the results of `fs.readdir`
* `statCache` Cache of `fs.stat` results, to prevent statting the same
  path multiple times.
* `symlinks` A record of which paths are symbolic links, which is
  relevant in resolving `**` patterns.
* `realpathCache` An optional object which is passed to `fs.realpath`
  to minimize unnecessary syscalls.  It is stored on the instantiated
  Glob object, and may be re-used.

### Events

* `end` When the matching is finished, this is emitted with all the
  matches found.  If the `nonull` option is set, and no match was found,
  then the `matches` list contains the original pattern.  The matches
  are sorted, unless the `nosort` flag is set.
* `match` Every time a match is found, this is emitted with the specific
  thing that matched. It is not deduplicated or resolved to a realpath.
* `error` Emitted when an unexpected error is encountered, or whenever
  any fs error occurs if `options.strict` is set.
* `abort` When `abort()` is called, this event is raised.

### Methods

* `pause` Temporarily stop the search
* `resume` Resume the search
* `abort` Stop the search forever

### Options

All the options that can be passed to Minimatch can also be passed to
Glob to change pattern matching behavior.  Also, some have been added,
or have glob-specific ramifications.

All options are false by default, unless otherwise noted.

All options are added to the Glob object, as well.

If you are running many `glob` operations, you can pass a Glob object
as the `options` argument to a subsequent operation to shortcut some
`stat` and `readdir` calls.  At the very least, you may pass in shared
`symlinks`, `statCache`, `realpathCache`, and `cache` options, so that
parallel glob operations will be sped up by sharing information about
the filesystem.

* `cwd` The current working directory in which to search.  Defaults
  to `process.cwd()`.
* `root` The place where patterns starting with `/` will be mounted
  onto.  Defaults to `path.resolve(options.cwd, "/")` (`/` on Unix
  systems, and `C:\` or some such on Windows.)
* `dot` Include `.dot` files in normal matches and `globstar` matches.
  Note that an explicit dot in a portion of the pattern will always
  match dot files.
* `nomount` By default, a pattern starting with a forward-slash will be
  "mounted" onto the root setting, so that a valid filesystem path is
  returned.  Set this flag to disable that behavior.
* `mark` Add a `/` character to directory matches.  Note that this
  requires additional stat calls.
* `nosort` Don't sort the results.
* `stat` Set to true to stat *all* results.  This reduces performance
  somewhat, and is completely unnecessary, unless `readdir` is presumed
  to be an untrustworthy indicator of file existence.
* `silent` When an unusual error is encountered when attempting to
  read a directory, a warning will be printed to stderr.  Set the
  `silent` option to true to suppress these warnings.
* `strict` When an unusual error is encountered when attempting to
  read a directory, the process will just continue on in search of
  other matches.  Set the `strict` option to raise an error in these
  cases.
* `cache` See `cache` property above.  Pass in a previously generated
  cache object to save some fs calls.
* `statCache` A cache of results of filesystem information, to prevent
  unnecessary stat calls.  While it should not normally be necessary
  to set this, you may pass the statCache from one glob() call to the
  options object of another, if you know that the filesystem will not
  change between calls.  (See "Race Conditions" below.)
* `symlinks` A cache of known symbolic links.  You may pass in a
  previously generated `symlinks` object to save `lstat` calls when
  resolving `**` matches.
* `sync` DEPRECATED: use `glob.sync(pattern, opts)` instead.
* `nounique` In some cases, brace-expanded patterns can result in the
  same file showing up multiple times in the result set.  By default,
  this implementation prevents duplicates in the result set.  Set this
  flag to disable that behavior.
* `nonull` Set to never return an empty set, instead returning a set
  containing the pattern itself.  This is the default in glob(3).
* `debug` Set to enable debug logging in minimatch and glob.
* `nobrace` Do not expand `{a,b}` and `{1..3}` brace sets.
* `noglobstar` Do not match `**` against multiple filenames.  (Ie,
  treat it as a normal `*` instead.)
* `noext` Do not match `+(a|b)` "extglob" patterns.
* `nocase` Perform a case-insensitive match.  Note: on
  case-insensitive filesystems, non-magic patterns will match by
  default, since `stat` and `readdir` will not raise errors.
* `matchBase` Perform a basename-only match if the pattern does not
  contain any slash characters.  That is, `*.js` would be treated as
  equivalent to `**/*.js`, matching all js files in all directories.
* `nodir` Do not match directories, only files.  (Note: to match
  *only* directories, simply put a `/` at the end of the pattern.)
* `ignore` Add a pattern or an array of glob patterns to exclude matches.
  Note: `ignore` patterns are *always* in `dot:true` mode, regardless
  of any other settings.
* `follow` Follow symlinked directories when expanding `**` patterns.
  Note that this can result in a lot of duplicate references in the
  presence of cyclic links.
* `realpath` Set to true to call `fs.realpath` on all of the results.
  In the case of a symlink that cannot be resolved, the full absolute
  path to the matched entry is returned (though it will usually be a
  broken symlink)
* `absolute` Set to true to always receive absolute paths for matched
  files.  Unlike `realpath`, this also affects the values returned in
  the `match` event.

## Comparisons to other fnmatch/glob implementations

While strict compliance with the existing standards is a worthwhile
goal, some discrepancies exist between node-glob and other
implementations, and are intentional.

The double-star character `**` is supported by default, unless the
`noglobstar` flag is set.  This is supported in the manner of bsdglob
and bash 4.3, where `**` only has special significance if it is the only
thing in a path part.  That is, `a/**/b` will match `a/x/y/b`, but
`a/**b` will not.

Note that symlinked directories are not crawled as part of a `**`,
though their contents may match against subsequent portions of the
pattern.  This prevents infinite loops and duplicates and the like.

If an escaped pattern has no matches, and the `nonull` flag is set,
then glob returns the pattern as-provided, rather than
interpreting the character escapes.  For example,
`glob.match([], "\\*a\\?")` will return `"\\*a\\?"` rather than
`"*a?"`.  This is akin to setting the `nullglob` option in bash, except
that it does not resolve escaped pattern characters.

If brace expansion is not disabled, then it is performed before any
other interpretation of the glob pattern.  Thus, a pattern like
`+(a|{b),c)}`, which would not be valid in bash or zsh, is expanded
**first** into the set of `+(a|b)` and `+(a|c)`, and those patterns are
checked for validity.  Since those two are valid, matching proceeds.

### Comments and Negation

Previously, this module let you mark a pattern as a "comment" if it
started with a `#` character, or a "negated" pattern if it started
with a `!` character.

These options were deprecated in version 5, and removed in version 6.

To specify things that should not match, use the `ignore` option.

## Windows

**Please only use forward-slashes in glob expressions.**

Though windows uses either `/` or `\` as its path separator, only `/`
characters are used by this glob implementation.  You must use
forward-slashes **only** in glob expressions.  Back-slashes will always
be interpreted as escape characters, not path separators.

Results from absolute patterns such as `/foo/*` are mounted onto the
root setting using `path.join`.  On windows, this will by default result
in `/foo/*` matching `C:\foo\bar.txt`.

## Race Conditions

Glob searching, by its very nature, is susceptible to race conditions,
since it relies on directory walking and such.

As a result, it is possible that a file that exists when glob looks for
it may have been deleted or modified by the time it returns the result.

As part of its internal implementation, this program caches all stat
and readdir calls that it makes, in order to cut down on system
overhead.  However, this also makes it even more susceptible to races,
especially if the cache or statCache objects are reused between glob
calls.

Users are thus advised not to use a glob result as a guarantee of
filesystem state in the face of rapid changes.  For the vast majority
of operations, this is never a problem.

## Contributing

Any change to behavior (including bugfixes) must come with a test.

Patches that fail tests or reduce performance will be rejected.

```
# to run tests
npm test

# to re-generate test fixtures
npm run test-regen

# to benchmark against bash/zsh
npm run bench

# to profile javascript
npm run prof
```
# wrappy

Callback wrapping utility

## USAGE

```javascript
var wrappy = require("wrappy")

// var wrapper = wrappy(wrapperFunction)

// make sure a cb is called only once
// See also: http://npm.im/once for this specific use case
var once = wrappy(function (cb) {
  var called = false
  return function () {
    if (called) return
    called = true
    return cb.apply(this, arguments)
  }
})

function printBoo () {
  console.log('boo')
}
// has some rando property
printBoo.iAmBooPrinter = true

var onlyPrintOnce = once(printBoo)

onlyPrintOnce() // prints 'boo'
onlyPrintOnce() // does nothing

// random property is retained!
assert.equal(onlyPrintOnce.iAmBooPrinter, true)
```
# ci-info

Get details about the current Continuous Integration environment.

Please [open an
issue](https://github.com/watson/ci-info/issues/new?template=ci-server-not-detected.md)
if your CI server isn't properly detected :)

[![npm](https://img.shields.io/npm/v/ci-info.svg)](https://www.npmjs.com/package/ci-info)
[![Build status](https://travis-ci.org/watson/ci-info.svg?branch=master)](https://travis-ci.org/watson/ci-info)
[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Installation

```bash
npm install ci-info --save
```

## Usage

```js
var ci = require('ci-info')

if (ci.isCI) {
  console.log('The name of the CI server is:', ci.name)
} else {
  console.log('This program is not running on a CI server')
}
```

## Supported CI tools

Officially supported CI servers:

- [AWS CodeBuild](https://aws.amazon.com/codebuild/)
- [AppVeyor](http://www.appveyor.com)
- [Bamboo](https://www.atlassian.com/software/bamboo) by Atlassian
- [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines)
- [Buildkite](https://buildkite.com)
- [CircleCI](http://circleci.com)
- [Cirrus CI](https://cirrus-ci.org)
- [Codeship](https://codeship.com)
- [Drone](https://drone.io)
- [GitLab CI](https://about.gitlab.com/gitlab-ci/)
- [GoCD](https://www.go.cd/)
- [Hudson](http://hudson-ci.org)
- [Jenkins CI](https://jenkins-ci.org)
- [Magnum CI](https://magnum-ci.com)
- [Semaphore](https://semaphoreci.com)
- [Shippable](https://www.shippable.com/)
- [Solano CI](https://www.solanolabs.com/)
- [Strider CD](https://strider-cd.github.io/)
- [TaskCluster](http://docs.taskcluster.net)
- [Team Foundation Server](https://www.visualstudio.com/en-us/products/tfs-overview-vs.aspx) by Microsoft
- [TeamCity](https://www.jetbrains.com/teamcity/) by JetBrains
- [Travis CI](http://travis-ci.org)

## API

### `ci.name`

A string. Will contain the name of the CI server the code is running on.
If not CI server is detected, it will be `null`.

Don't depend on the value of this string not to change for a specific
vendor. If you find your self writing `ci.name === 'Travis CI'`, you
most likely want to use `ci.TRAVIS` instead.

### `ci.isCI`

A boolean. Will be `true` if the code is running on a CI server.
Otherwise `false`.

Some CI servers not listed here might still trigger the `ci.isCI`
boolean to be set to `true` if they use certain vendor neutral
environment variables. In those cases `ci.name` will be `null` and no
vendor specific boolean will be set to `true`.

### `ci.<VENDOR-CONSTANT>`

The following vendor specific boolean constants are exposed. A constant
will be `true` if the code is determined to run on the given CI server.
Otherwise `false`.

- `ci.APPVEYOR`
- `ci.BAMBOO`
- `ci.BITBUCKET`
- `ci.BUILDKITE`
- `ci.CIRCLE`
- `ci.CIRRUS`
- `ci.CODEBUILD`
- `ci.CODESHIP`
- `ci.DRONE`
- `ci.GITLAB`
- `ci.GOCD`
- `ci.HUDSON`
- `ci.JENKINS`
- `ci.MAGNUM`
- `ci.SEMAPHORE`
- `ci.SHIPPABLE`
- `ci.SOLANO`
- `ci.STRIDER`
- `ci.TASKCLUSTER`
- `ci.TEAMCITY`
- `ci.TFS` (Team Foundation Server)
- `ci.TRAVIS`

Deprecated vendor constants that will be removed in the next major
release:

- `ci.TDDIUM` (Solano CI) This have been renamed `ci.SOLANO`

## License

[MIT](LICENSE)
# graceful-fs

graceful-fs functions as a drop-in replacement for the fs module,
making various improvements.

The improvements are meant to normalize behavior across different
platforms and environments, and to make filesystem access more
resilient to errors.

## Improvements over [fs module](https://nodejs.org/api/fs.html)

* Queues up `open` and `readdir` calls, and retries them once
  something closes if there is an EMFILE error from too many file
  descriptors.
* fixes `lchmod` for Node versions prior to 0.6.2.
* implements `fs.lutimes` if possible. Otherwise it becomes a noop.
* ignores `EINVAL` and `EPERM` errors in `chown`, `fchown` or
  `lchown` if the user isn't root.
* makes `lchmod` and `lchown` become noops, if not available.
* retries reading a file if `read` results in EAGAIN error.

On Windows, it retries renaming a file for up to one second if `EACCESS`
or `EPERM` error occurs, likely because antivirus software has locked
the directory.

## USAGE

```javascript
// use just like fs
var fs = require('graceful-fs')

// now go and do stuff with it...
fs.readFileSync('some-file-or-whatever')
```

## Global Patching

If you want to patch the global fs module (or any other fs-like
module) you can do this:

```javascript
// Make sure to read the caveat below.
var realFs = require('fs')
var gracefulFs = require('graceful-fs')
gracefulFs.gracefulify(realFs)
```

This should only ever be done at the top-level application layer, in
order to delay on EMFILE errors from any fs-using dependencies.  You
should **not** do this in a library, because it can cause unexpected
delays in other parts of the program.

## Changes

This module is fairly stable at this point, and used by a lot of
things.  That being said, because it implements a subtle behavior
change in a core part of the node API, even modest changes can be
extremely breaking, and the versioning is thus biased towards
bumping the major when in doubt.

The main change between major versions has been switching between
providing a fully-patched `fs` module vs monkey-patching the node core
builtin, and the approach by which a non-monkey-patched `fs` was
created.

The goal is to trade `EMFILE` errors for slower fs operations.  So, if
you try to open a zillion files, rather than crashing, `open`
operations will be queued up and wait for something else to `close`.

There are advantages to each approach.  Monkey-patching the fs means
that no `EMFILE` errors can possibly occur anywhere in your
application, because everything is using the same core `fs` module,
which is patched.  However, it can also obviously cause undesirable
side-effects, especially if the module is loaded multiple times.

Implementing a separate-but-identical patched `fs` module is more
surgical (and doesn't run the risk of patching multiple times), but
also imposes the challenge of keeping in sync with the core module.

The current approach loads the `fs` module, and then creates a
lookalike object that has all the same methods, except a few that are
patched.  It is safe to use in all versions of Node from 0.8 through
7.0.

### v4

* Do not monkey-patch the fs module.  This module may now be used as a
  drop-in dep, and users can opt into monkey-patching the fs builtin
  if their app requires it.

### v3

* Monkey-patch fs, because the eval approach no longer works on recent
  node.
* fixed possible type-error throw if rename fails on windows
* verify that we *never* get EMFILE errors
* Ignore ENOSYS from chmod/chown
* clarify that graceful-fs must be used as a drop-in

### v2.1.0

* Use eval rather than monkey-patching fs.
* readdir: Always sort the results
* win32: requeue a file if error has an OK status

### v2.0

* A return to monkey patching
* wrap process.cwd

### v1.1

* wrap readFile
* Wrap fs.writeFile.
* readdir protection
* Don't clobber the fs builtin
* Handle fs.read EAGAIN errors by trying again
* Expose the curOpen counter
* No-op lchown/lchmod if not implemented
* fs.rename patch only for win32
* Patch fs.rename to handle AV software on Windows
* Close #4 Chown should not fail on einval or eperm if non-root
* Fix isaacs/fstream#1 Only wrap fs one time
* Fix #3 Start at 1024 max files, then back off on EMFILE
* lutimes that doens't blow up on Linux
* A full on-rewrite using a queue instead of just swallowing the EMFILE error
* Wrap Read/Write streams as well

### 1.0

* Update engines for node 0.6
* Be lstat-graceful on Windows
* first
