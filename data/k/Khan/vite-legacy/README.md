# vite

`vite` is a fast test environment focused on visual regression testing.

## Quickstart

- `yarn build`
- install the extension folder as a unpackage extension in Chrome
  - go to `chrome://extensions/`
  - click `Load Unpacked`
  - select the `extensions/dist` folder in this repo
- `yarn start`

## Devevelopment Guide

- run `yarn watch`
- changes to anything in the `extensions` folder will require reloading
  the extension in `chrome://extensions/`
- you can "Inspect views `background page`" to debug background.js

## Roadmap

- screenshot elements
- Firefox support
- use docker for reproducible runs
- record and playback user interaction
- playback user interactions faster than real-time (mock out `setTimeout()` and `setInterval()`)
- detect DOM changes and take multiple screenshots
- eliminate factors that produce consistency (mock out `Math.random()` and `Date.now()`)
- code coverage
- props coverage (are all possible combination of props covered?)

## FAQ

**Q: Isn't image testing fragile?**

A: If things that can introduce inconsistencies between runs can be eliminiated
image comparison tests can be quite robust.  Using docker will ensure the test 
environment is the same between each run even when running on different machines.
Mocking out `Math.random()` and `Date.now()` will help when testing code that use
those functions.

**Q: Why not jest's snapshot testing?**

A: Snapshot testing produces markup which can be used to detect certain
issues, but sometimes it's hard to tell if there's an issue simply looking
at markup.  This is why image regression testing is important.

**Q: Why not selenium?**

A: Selenium is slow.  `vite` uses the Web Extension API to take screenshots.
This is very fast in practice.  One of the `vite`'s use cases is regression
testing component libraries.  In this situation we want to take screenshots
of each component use as many different combinations as possible.  Rendering
each in isolation helps to isolate issues from other test cases.  The consequence
is that we need take a lot of indepedent screenshots which would take too 
long using selenium.

**Q: Why record/play back user actions?**

A: Simulating click events on particular elements does not detect a certain
class of issues.  For instance a element may be obscured by a transparent 
element or the element may have `pointer-events: none`.  Both would result 
in a user being unable to click the element.

Recording and play back of user actions removes the need to write code to
simulate events speeding up test case creation.

**Q: Why not chromaticqa or screenster?**

A: These are paid for services and the volume of screenshots that we'll
eventually want to take across wonder-blocks, webapp, KaTeX, etc. will
add up pretty quick.  Also, these services don't seem to proide a way to
simulate events so getting stateful components into different states is
impossible.
