# Lab Interactives Site

Set of interactives built using the [Lab Framework](http://lab-framework.concord.org) from the [Concord Consortium](http://www.concord.org). This site is deployed to:

**[lab.concord.org](http://lab.concord.org)**

## Licensing

Lab Interactives Site is Copyright 2012 (c) by the Concord Consortium and is distributed under
the [MIT](http://www.opensource.org/licenses/MIT) license.

The complete licensing details can be read [here](license.md).

If you have have received a **distribution archive** of the
[Concord Consortium Lab project](https://github.com/concord-consortium/lab)
our copyright applies to all resources **except** the files in the
`vendor/` directory. The files in the `vendor/` directory are from
third-parties and are distributed under either BSD, MIT, or Apache 2.0 licenses.

## Setup Development

### Prerequisites:

- [RVM, Ruby 2.0 and Bundler](developer-doc/setup-ruby.md)
- [node.js, npm and yarn](developer-doc/setup-node.md)
- [additional Linux notes](developer-doc/linux-notes.md)

### Setup the local Lab repository for development

1. Clone the git repository
2. `cd lab-interactives-site`
3. `bundle install`
4. `make everything`
5. open another new terminal and run `rackup`
6. open http://localhost:9292
7. (optional) open a new terminal and run `guard`

It is recommended that you review the [initial setup details](developer-doc/initial-setup-details.md).
They describe what each of the steps above does.

## Run Docker Container

See the [Docker documentation](developer-doc/docker.md) for more information.

## Contributing to Lab Interactives Site

If you think you'd like to contribute to Lab Interactives Site as an external developer:

1. Create a local clone from the repository located here: http://github.com/concord-consortium/lab-interactives-site.
   This will by default have the git-remote name: **origin**.

2. Make a fork of http://github.com/concord-consortium/lab-interactives-site to your account on github.

3. Make a new git-remote referencing your fork. I recommend making the remote name your github user name.
   For example my username is `stepheneb` so I would add a remote to my fork like this:

        git remote add stepheneb git@github.com:stepheneb/lab-interactives-site.git

4. Create your changes on a topic branch. Please include tests if you can. When your commits are ready
   push your topic branch to your fork and send a pull request.

## `src/models`, `src/models-converted` and `imports` directories

* [`src/models`](https://github.com/concord-consortium/lab-interactives-site/tree/master/src/models) should be a default directory for models that are created or updated manually by authors.

* [`src/models-converted`](https://github.com/concord-consortium/lab-interactives-site/tree/master/src/models-converted) should contain only models that are created using automated conversion tool, for example [MML Converter](http://lab-framework.concord.org/mml-converter.html).
  If you modify model JSON after conversion, such model should be moved to `src/models`! You should assume that each model that lives in `src/models-converted` may be
  converted again in the future (e.g. when MML Converter is updated). In such case you would lose your manual tweaks.

* [`imports`](https://github.com/concord-consortium/lab-interactives-site/tree/master/imports) should contain original models (e.g. `.MML` and `.E2D` files) that are related to JSONs in `src/models-converted`
  and **optionally** models related to JSONs in `src/models` (if author thinks it may be useful in the future).


## More Documentation

- [Project Configuration](developer-doc/configuration.md)
- [Deployment](developer-doc/deployment.md)
- [Working with different Lab Framework versions](developer-doc/lab-framework-versions.md)
- [Localization](developer-doc/localization.md)
body {
  font-family: Lato, Verdana, Geneva, sans-serif;
  font-size: 14px;
  padding: 5px 20px 5px 20px;
  background: {
    image: url(resources/diagonal-lines.jpg);
    repeat: repeat; };
  margin: 10px {
    bottom: 0px; }; }

#main {
  background-color: #f2f8fc;
  color: #00233a;
  border: 1px solid;
  display: inline;
  float: left;
  padding: 10px;
  height: auto;
  margin-right: 0;
  min-height: 600px;
  width: 900px; }

h1 {
  color: #5f5f5f;
  font-weight: bold;
  font-size: 1.6em;
  border-top: 3px solid #aaaaaa;
  padding-top: 0.5em;
  margin: 1.5em 0em 0.6em 0em;
  &:first-child {
    margin-top: 0;
    padding-top: 0.25em;
    border-top: none; } }

h2 {
  color: #5f5f5f;
  font-weight: bold;
  font-size: 1.4em;
  border-top: 6px double #d0d0d0;
  margin: 1.5em 0em 0.6em 0em;
  padding-top: 1.0em;
  &:first-child {
    margin-top: 0;
    padding-top: 0.25em;
    border-top: none; } }

h3 {
  font-weight: normal;
  font-size: 1.2em;
  margin: 1.4em 1.0em 0.6em 0em;
  padding-top: 0.8em;
  border-top: 2px solid #e0e0e0; }

h4 {
  font-weight: normal;
  font-size: 1.125em;
  margin: 0.6em 2.0em 0.6em 0em;
  padding-top: 0.4em; }

h5 {
  font-weight: normal;
  font-size: 1.1em;
  margin: 0.6em 2.0em 0.6em 0em;
  padding-top: 0.2em; }

h5 {
  font-weight: normal;
  font-size: 1.05em;
  margin: 0.6em 2.0em 0.6em 0em;
  padding-top: 0.2em; }

a {
  text-decoration: none; }

p {
  margin: 1em 0;
  line-height: 1.5em; }

ul {
  margin: 1em 0em;
  li {
    margin: 0.5em 0em; } }

ol {
  margin: 1em 0em;
  li {
    margin: 0.5em 0em; } }

blockquote {
  margin: 1em 0em;
  border-left: 5px solid #dddddd;
  padding-left: 0.6em;
  color: #555555; }

dl {
  width: 100%;
  margin: 1em; }

dt {
  float: left;
  margin-left: 1%;
  width: 27%; }

dd {
  float: left;
  margin-bottom: 0.6em;
  margin-left: 0;
  width: 72%; }

table {
  margin: 1em 0;
  th {
    border-bottom: 1px solid #bbbbbb;
    padding: 0.2em 1em; }
  td {
    border-bottom: 1px solid #dddddd;
    padding: 0.2em 1em; } }

pre {
  margin: 1em 1em;
  font-size: 88%;
  background-color: #f8f8ff;
  border: 1px solid #dedede;
  padding: 0.5em;
  line-height: 1.5em;
  color: #444444;
  overflow: auto;
  code {
    padding: 0;
    font-size: 100%;
    background-color: #f8f8ff;
    border: none; } }

code {
  font-size: 90%;
  background-color: #f8f8ff;
  color: #444444;
  padding: 0 0.2em;
  border: 1px solid #dedede;
  .keyword { font-weight: bold }
  .string, .regexp  { color: darkgreen }
  .class,  .special { color: darkblue }
  .number           { color: darkred }
  .comment          { color: grey } }

a { code { color: darkblue; } }

pre.console {
  margin: 1em 0;
  font-size: 90%;
  background-color: black;
  padding: 0.5em;
  line-height: 1.5em;
  color: white;
  code {
    padding: 0;
    font-size: 100%;
    background-color: black;
    border: none;
    color: white; } }
