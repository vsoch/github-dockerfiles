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
# DeployServer

A sample implementation for using GitHub Deployment API.

Ported [this](https://developer.github.com/guides/delivering-deployments/) by Java. Powered by [Spark](http://sparkjava.com/).

## Prerequisite
- JDK8
- Maven3
- GitHub OAuth Token

## Getting Started
First, you should set your OAuth token into an environment variable somewhere, like:
```
export GITHUB_OAUTH=xxxxxxx
```

After that, you can:

- For development

```
$ mvn compile exec:java
```

If you aren't familiar with CLI, you can just run the main class via an execution button in your IDE as well.

- For deployment

```
$ mvn clean package
$ java -jar target/DeployServer-{version}.jar
```

Then you can see it works on `http://localhost:4567`.

After you make sure this sever deployed a place where GitHub can reach out to, you can test how it interacts with GitHub via its Deployment API.

You can also place it on your local pc, then expose it by using ngrok. Please refer the direction described [here](https://developer.github.com/guides/delivering-deployments/).
# basics-of-authentication

This is the sample project built by following the "[Basics of Authentication][basics of auth]"
guide on developer.github.com.

It consists of two different servers: one built correctly, and one built less optimally.

## Install and Run project

To run these projects, make sure you have [Bundler][bundler] installed; then type
`bundle install` on the command line.

For the "less optimal" server, type `ruby server.rb` on the command line.

For the correct server, enter `ruby advanced_server.rb` on the command line.

Both commands will run the server at `localhost:4567`.

[basics of auth]: http://developer.github.com/guides/basics-of-authentication/
[bundler]: http://gembundler.com/
This is the sample project built by following the "[Building Your First GitHub App](https://developer.github.com/apps/building-your-first-github-app)" Quickstart guide on developer.github.com.

It consists of two different servers: `server.rb` (boilerplate) and `advanced_server.rb` (completed project).

## Install and run

To run the code, make sure you have [Bundler](http://gembundler.com/) installed; then enter `bundle install` on the command line.

* For the boilerplate project, enter `ruby server.rb` on the command line.

* For the completed project, enter `ruby advanced_server.rb` on the command line.

Both commands will run the server at `localhost:3000`.
# Instance auditor

This script creates an spreadsheet file that will allow you to audit the access of each team and user with all of the organizations across your GitHub Enterprise instance.

## Getting started

The user who is going to run the script must be on the "Owners" team of every organization you wish to audit. You can promote all users with Site Admin access to owners of every organization by running [`ghe-org-admin-promote`](https://help.github.com/enterprise/admin/articles/command-line-utilities/#ghe-org-admin-promote).

You will also need to [generate a Personal Access Token](https://help.github.com/enterprise/user/articles/creating-an-access-token-for-command-line-use/) for that user with the `admin:org` permission.

## Output

This utility will create a file in the same directory called `audit.xlsx` containing the audit data. 
# Suspended User Audit

Lists total number of active, suspended, and recently suspended users. Gives the option to unsuspend all recently suspended users. This is mostly useful when a configuration change may have caused a large number of users to become suspended.

## Installation


### Clone this repository

```shell
git clone git@github.com:github/platform-samples.git
cd api/ruby/user-auditing
```


### Install dependencies

```shell
gem install octokit
```


## Usage

### Configure Octokit

```shell
export OCTOKIT_API_ENDPOINT="https://github.example.com/api/v3" # Default: "https://api.github.com"
export OCTOKIT_ACCESS_TOKEN=00000000000000000000000
```

### Execute

```shell
ruby suspended_user_audit.rb
```
# Find Inactive Organization Members

```
find_inactive_members.rb - Find and output inactive members in an organization
    -c, --check                      Check connectivity and scope
    -d, --date MANDATORY             Date from which to start looking for activity
    -e, --email                      Fetch the user email (can make the script take longer
    -o, --organization MANDATORY     Organization to scan for inactive users
    -v, --verbose                    More output to STDERR
    -h, --help                       Display this help
```

This utility finds users inactive since a configured date, writes those users to a file `inactive_users.csv`.

## Installation

### Clone this repository

```shell
git clone https://github.com/github/platform-samples.git
cd api/ruby/find-inactive-members
```

### Install dependencies

```shell
gem install octokit
```

### Configure Octokit

The `OCTOKIT_ACCESS_TOKEN` is required in order to see activities on private repositories. However the `OCTOKIT_API_ENDPOINT` isn't required if connecting to GitHub.com, but is required if connecting to a GitHub Enterprise instance.

```shell
export OCTOKIT_ACCESS_TOKEN=00000000000000000000000     # Required if looking for activity in private repositories.
export OCTOKIT_API_ENDPOINT="https://<your_github_enterprise_instance>/api/v3" # Not required if connecting to GitHub.com.
```

## Usage

```
ruby find_inactive_members.rb [-cehv] -o ORGANIZATION -d DATE
```

## How Inactivity is Defined

Members are defined as inactive if they haven't, since the specified **DATE**,  in any repository in the specified **ORGANIZATION**:

* Have not merged or pushed commits into the default branch
* Have not opened an Issue or Pull Request
* Have not commented on an Issue or Pull Request
rendering-data-as-graphs
================

This is the sample project built by following the "[Rendering Data as Graphs][rendering data]"
guide on developer.github.com.

To run these projects, make sure you have [Bundler][bundler] installed; then type
`bundle install` on the command line.

Then, enter `bundle exec rackup -p 4567` on the command line.

[rendering data]: http://developer.github.com/guides/rendering-data-as-graphs/
[bundler]: http://gembundler.com/
# GitHub API + ES2015 + node.js

## Setup

- see the `package.json` of the `es2015-nodejs` directory
- type `npm install`
- you need the content of `libs/*`


## Use `/libs/GitHubClient.js`

This library can work with :octocat:.com and :octocat: Enterprise

### Create a GitHub client

- First, go to your GitHub profile settings and define a **Personal access token** (https://github.com/settings/tokens)
- Then, add the token to the environment variables (eg: `export TOKEN_GITHUB_DOT_COM=token_string`)
- Now you can get the token like that: `process.env.TOKEN_GITHUB_DOT_COM`

```javascript
const GitHubClient = require('../libs/GitHubClient.js').GitHubClient;

let githubCliEnterprise = new GitHubClient({
  baseUri: "http://github.at.home/api/v3",
  token: process.env.TOKEN_GHITHUB_ENTERPRISE
});

let githubCliDotCom = new GitHubClient({
  baseUri:"https://api.github.com",
  token: process.env.TOKEN_GITHUB_DOT_COM
});

```

- if you use GitHub Enterprise, `baseUri` has to be set with `http(s)://your_domain_name/api/v3`
- if you use GitHub.com, `baseUri` has to be set with `https://api.github.com`

### Use the GitHub client

For example, you want to get the information about a user:
(see https://developer.github.com/v3/users/#get-a-single-user)

```javascript
let githubCliEnterprise = new GitHubClient({
  baseUri:"http://github.at.home/api/v3",
  token:process.env.TOKEN_GHITHUB_ENTERPRISE
});

var handle = "k33g";
githubCliEnterprise.getData({path:`/users/${handle}`})
  .then(response => {
    console.log(response.data);
  });
```

## The easier way: adding features

You can add "features" to `GitHubClient` (like traits):

```javascript
const GitHubClient = require('../libs/GitHubClient.js').GitHubClient;
const octocat = require('../libs/features/octocat');
const users = require('../libs/features/users');

// add octocat and users features to GitHubClient
let githubCli = new GitHubClient({
  baseUri:"http://github.at.home/api/v3",
  token:process.env.TOKEN_GHITHUB_ENTERPRISE
}, octocat, users);

githubCli.octocat()
  .then(data => {
    // display the Zen of Octocat
    console.log(data);
  })

githubCli.fetchUser({handle:'k33g'})
  .then(user => {
    // all about @k33g
    console.log(user);
  })

```

## Recipes (and features)

See the `/recipes` directory (more samples to come)

node-fetch
==========

[![npm version][npm-image]][npm-url]
[![build status][travis-image]][travis-url]
[![coverage status][coveralls-image]][coveralls-url]

A light-weight module that brings `window.fetch` to Node.js


# Motivation

Instead of implementing `XMLHttpRequest` in Node.js to run browser-specific [Fetch polyfill](https://github.com/github/fetch), why not go from native `http` to `Fetch` API directly? Hence `node-fetch`, minimal code for a `window.fetch` compatible API on Node.js runtime.

See Matt Andrews' [isomorphic-fetch](https://github.com/matthew-andrews/isomorphic-fetch) for isomorphic usage (exports `node-fetch` for server-side, `whatwg-fetch` for client-side).


# Features

- Stay consistent with `window.fetch` API.
- Make conscious trade-off when following [whatwg fetch spec](https://fetch.spec.whatwg.org/) and [stream spec](https://streams.spec.whatwg.org/) implementation details, document known difference.
- Use native promise, but allow substituting it with [insert your favorite promise library].
- Use native stream for body, on both request and response.
- Decode content encoding (gzip/deflate) properly, and convert string output (such as `res.text()` and `res.json()`) to UTF-8 automatically.
- Useful extensions such as timeout, redirect limit, response size limit, [explicit errors](https://github.com/bitinn/node-fetch/blob/master/ERROR-HANDLING.md) for troubleshooting.


# Difference from client-side fetch

- See [Known Differences](https://github.com/bitinn/node-fetch/blob/master/LIMITS.md) for details.
- If you happen to use a missing feature that `window.fetch` offers, feel free to open an issue.
- Pull requests are welcomed too!


# Install

`npm install node-fetch --save`


# Usage

```javascript
var fetch = require('node-fetch');

// if you are on node v0.10, set a Promise library first, eg.
// fetch.Promise = require('bluebird');

// plain text or html

fetch('https://github.com/')
	.then(function(res) {
		return res.text();
	}).then(function(body) {
		console.log(body);
	});

// json

fetch('https://api.github.com/users/github')
	.then(function(res) {
		return res.json();
	}).then(function(json) {
		console.log(json);
	});

// catching network error
// 3xx-5xx responses are NOT network errors, and should be handled in then()
// you only need one catch() at the end of your promise chain

fetch('http://domain.invalid/')
	.catch(function(err) {
		console.log(err);
	});

// stream
// the node.js way is to use stream when possible

fetch('https://assets-cdn.github.com/images/modules/logos_page/Octocat.png')
	.then(function(res) {
		var dest = fs.createWriteStream('./octocat.png');
		res.body.pipe(dest);
	});

// buffer
// if you prefer to cache binary data in full, use buffer()
// note that buffer() is a node-fetch only API

var fileType = require('file-type');
fetch('https://assets-cdn.github.com/images/modules/logos_page/Octocat.png')
	.then(function(res) {
		return res.buffer();
	}).then(function(buffer) {
		fileType(buffer);
	});

// meta

fetch('https://github.com/')
	.then(function(res) {
		console.log(res.ok);
		console.log(res.status);
		console.log(res.statusText);
		console.log(res.headers.raw());
		console.log(res.headers.get('content-type'));
	});

// post

fetch('http://httpbin.org/post', { method: 'POST', body: 'a=1' })
	.then(function(res) {
		return res.json();
	}).then(function(json) {
		console.log(json);
	});

// post with stream from resumer

var resumer = require('resumer');
var stream = resumer().queue('a=1').end();
fetch('http://httpbin.org/post', { method: 'POST', body: stream })
	.then(function(res) {
		return res.json();
	}).then(function(json) {
		console.log(json);
	});

// post with form-data (detect multipart)

var FormData = require('form-data');
var form = new FormData();
form.append('a', 1);
fetch('http://httpbin.org/post', { method: 'POST', body: form })
	.then(function(res) {
		return res.json();
	}).then(function(json) {
		console.log(json);
	});

// post with form-data (custom headers)
// note that getHeaders() is non-standard API

var FormData = require('form-data');
var form = new FormData();
form.append('a', 1);
fetch('http://httpbin.org/post', { method: 'POST', body: form, headers: form.getHeaders() })
	.then(function(res) {
		return res.json();
	}).then(function(json) {
		console.log(json);
	});

// node 0.12+, yield with co

var co = require('co');
co(function *() {
	var res = yield fetch('https://api.github.com/users/github');
	var json = yield res.json();
	console.log(res);
});
```

See [test cases](https://github.com/bitinn/node-fetch/blob/master/test/test.js) for more examples.


# API

## fetch(url, options)

Returns a `Promise`

### Url

Should be an absolute url, eg `http://example.com/`

### Options

default values are shown, note that only `method`, `headers`, `redirect` and `body` are allowed in `window.fetch`, others are node.js extensions.

```
{
	method: 'GET'
	, headers: {}        // request header. format {a:'1'} or {b:['1','2','3']}
	, redirect: 'follow' // set to `manual` to extract redirect headers, `error` to reject redirect
	, follow: 20         // maximum redirect count. 0 to not follow redirect
	, timeout: 0         // req/res timeout in ms, it resets on redirect. 0 to disable (OS limit applies)
	, compress: true     // support gzip/deflate content encoding. false to disable
	, size: 0            // maximum response body size in bytes. 0 to disable
	, body: empty        // request body. can be a string, buffer, readable stream
	, agent: null        // http.Agent instance, allows custom proxy, certificate etc.
}
```


# License

MIT


# Acknowledgement

Thanks to [github/fetch](https://github.com/github/fetch) for providing a solid implementation reference.


[npm-image]: https://img.shields.io/npm/v/node-fetch.svg?style=flat-square
[npm-url]: https://www.npmjs.com/package/node-fetch
[travis-image]: https://img.shields.io/travis/bitinn/node-fetch.svg?style=flat-square
[travis-url]: https://travis-ci.org/bitinn/node-fetch
[coveralls-image]: https://img.shields.io/coveralls/bitinn/node-fetch.svg?style=flat-square
[coveralls-url]: https://coveralls.io/r/bitinn/node-fetch
# Encoding

**encoding** is a simple wrapper around [node-iconv](https://github.com/bnoordhuis/node-iconv) and [iconv-lite](https://github.com/ashtuchkin/iconv-lite/) to convert strings from one encoding to another. If node-iconv is not available for some reason,
iconv-lite will be used instead of it as a fallback.

[![Build Status](https://secure.travis-ci.org/andris9/encoding.svg)](http://travis-ci.org/andris9/Nodemailer)
[![npm version](https://badge.fury.io/js/encoding.svg)](http://badge.fury.io/js/encoding)

## Install

Install through npm

    npm install encoding

## Usage

Require the module

    var encoding = require("encoding");

Convert with encoding.convert()

    var resultBuffer = encoding.convert(text, toCharset, fromCharset);

Where

  * **text** is either a Buffer or a String to be converted
  * **toCharset** is the characterset to convert the string
  * **fromCharset** (*optional*, defaults to UTF-8) is the source charset

Output of the conversion is always a Buffer object.

Example

    var result = encoding.convert("ÕÄÖÜ", "Latin_1");
    console.log(result); //<Buffer d5 c4 d6 dc>

## iconv support

By default only iconv-lite is bundled. If you need node-iconv support, you need to add it
as an additional dependency for your project:

    ...,
    "dependencies":{
        "encoding": "*",
        "iconv": "*"
    },
    ...

## License

**MIT**
## Pure JS character encoding conversion [![Build Status](https://travis-ci.org/ashtuchkin/iconv-lite.svg?branch=master)](https://travis-ci.org/ashtuchkin/iconv-lite)

 * Doesn't need native code compilation. Works on Windows and in sandboxed environments like [Cloud9](http://c9.io).
 * Used in popular projects like [Express.js (body_parser)](https://github.com/expressjs/body-parser), 
   [Grunt](http://gruntjs.com/), [Nodemailer](http://www.nodemailer.com/), [Yeoman](http://yeoman.io/) and others.
 * Faster than [node-iconv](https://github.com/bnoordhuis/node-iconv) (see below for performance comparison).
 * Intuitive encode/decode API
 * Streaming support for Node v0.10+
 * [Deprecated] Can extend Node.js primitives (buffers, streams) to support all iconv-lite encodings.
 * In-browser usage via [Browserify](https://github.com/substack/node-browserify) (~180k gzip compressed with Buffer shim included).
 * License: MIT.

[![NPM Stats](https://nodei.co/npm/iconv-lite.png?downloads=true&downloadRank=true)](https://npmjs.org/packages/iconv-lite/)

## Usage
### Basic API
```javascript
var iconv = require('iconv-lite');

// Convert from an encoded buffer to js string.
str = iconv.decode(new Buffer([0x68, 0x65, 0x6c, 0x6c, 0x6f]), 'win1251');

// Convert from js string to an encoded buffer.
buf = iconv.encode("Sample input string", 'win1251');

// Check if encoding is supported
iconv.encodingExists("us-ascii")
```

### Streaming API (Node v0.10+)
```javascript

// Decode stream (from binary stream to js strings)
http.createServer(function(req, res) {
    var converterStream = iconv.decodeStream('win1251');
    req.pipe(converterStream);

    converterStream.on('data', function(str) {
        console.log(str); // Do something with decoded strings, chunk-by-chunk.
    });
});

// Convert encoding streaming example
fs.createReadStream('file-in-win1251.txt')
    .pipe(iconv.decodeStream('win1251'))
    .pipe(iconv.encodeStream('ucs2'))
    .pipe(fs.createWriteStream('file-in-ucs2.txt'));

// Sugar: all encode/decode streams have .collect(cb) method to accumulate data.
http.createServer(function(req, res) {
    req.pipe(iconv.decodeStream('win1251')).collect(function(err, body) {
        assert(typeof body == 'string');
        console.log(body); // full request body string
    });
});
```

### [Deprecated] Extend Node.js own encodings
> NOTE: This doesn't work on latest Node versions. See [details](https://github.com/ashtuchkin/iconv-lite/wiki/Node-v4-compatibility).

```javascript
// After this call all Node basic primitives will understand iconv-lite encodings.
iconv.extendNodeEncodings();

// Examples:
buf = new Buffer(str, 'win1251');
buf.write(str, 'gbk');
str = buf.toString('latin1');
assert(Buffer.isEncoding('iso-8859-15'));
Buffer.byteLength(str, 'us-ascii');

http.createServer(function(req, res) {
    req.setEncoding('big5');
    req.collect(function(err, body) {
        console.log(body);
    });
});

fs.createReadStream("file.txt", "shift_jis");

// External modules are also supported (if they use Node primitives, which they probably do).
request = require('request');
request({
    url: "http://github.com/", 
    encoding: "cp932"
});

// To remove extensions
iconv.undoExtendNodeEncodings();
```

## Supported encodings

 *  All node.js native encodings: utf8, ucs2 / utf16-le, ascii, binary, base64, hex.
 *  Additional unicode encodings: utf16, utf16-be, utf-7, utf-7-imap.
 *  All widespread singlebyte encodings: Windows 125x family, ISO-8859 family, 
    IBM/DOS codepages, Macintosh family, KOI8 family, all others supported by iconv library. 
    Aliases like 'latin1', 'us-ascii' also supported.
 *  All widespread multibyte encodings: CP932, CP936, CP949, CP950, GB2313, GBK, GB18030, Big5, Shift_JIS, EUC-JP.

See [all supported encodings on wiki](https://github.com/ashtuchkin/iconv-lite/wiki/Supported-Encodings).

Most singlebyte encodings are generated automatically from [node-iconv](https://github.com/bnoordhuis/node-iconv). Thank you Ben Noordhuis and libiconv authors!

Multibyte encodings are generated from [Unicode.org mappings](http://www.unicode.org/Public/MAPPINGS/) and [WHATWG Encoding Standard mappings](http://encoding.spec.whatwg.org/). Thank you, respective authors!


## Encoding/decoding speed

Comparison with node-iconv module (1000x256kb, on MacBook Pro, Core i5/2.6 GHz, Node v0.12.0). 
Note: your results may vary, so please always check on your hardware.

    operation             iconv@2.1.4   iconv-lite@0.4.7
    ----------------------------------------------------------
    encode('win1251')     ~96 Mb/s      ~320 Mb/s
    decode('win1251')     ~95 Mb/s      ~246 Mb/s

## BOM handling

 * Decoding: BOM is stripped by default, unless overridden by passing `stripBOM: false` in options
   (f.ex. `iconv.decode(buf, enc, {stripBOM: false})`).
   A callback might also be given as a `stripBOM` parameter - it'll be called if BOM character was actually found.
 * Encoding: No BOM added, unless overridden by `addBOM: true` option.

## UTF-16 Encodings

This library supports UTF-16LE, UTF-16BE and UTF-16 encodings. First two are straightforward, but UTF-16 is trying to be
smart about endianness in the following ways:
 * Decoding: uses BOM and 'spaces heuristic' to determine input endianness. Default is UTF-16LE, but can be 
   overridden with `defaultEncoding: 'utf-16be'` option. Strips BOM unless `stripBOM: false`.
 * Encoding: uses UTF-16LE and writes BOM by default. Use `addBOM: false` to override.

## Other notes

When decoding, be sure to supply a Buffer to decode() method, otherwise [bad things usually happen](https://github.com/ashtuchkin/iconv-lite/wiki/Use-Buffers-when-decoding).  
Untranslatable characters are set to � or ?. No transliteration is currently supported.  
Node versions 0.10.31 and 0.11.13 are buggy, don't use them (see #65, #77).  

## Testing

```bash
$ git clone git@github.com:ashtuchkin/iconv-lite.git
$ cd iconv-lite
$ npm install
$ npm test
    
$ # To view performance:
$ node test/performance.js

$ # To view test coverage:
$ npm run coverage
$ open coverage/lcov-report/index.html
```

## Adoption
[![NPM](https://nodei.co/npm-dl/iconv-lite.png)](https://nodei.co/npm/iconv-lite/)
[![Codeship Status for ashtuchkin/iconv-lite](https://www.codeship.io/projects/81670840-fa72-0131-4520-4a01a6c01acc/status)](https://www.codeship.io/projects/29053)
# GitHub API + Scala

## Setup and Run

- This is a `sbt` project. See http://www.scala-sbt.org/0.13/docs/Setup.html
- Run `sbt` in a Terminal (at the root of this project: `/platform-samples/API/scala.wit.sbt/octocat-samples`)
- Type `run`, and you'll get this:
```shell
> run
[warn] Multiple main classes detected.  Run 'show discoveredMainClasses' to see the list

Multiple main classes detected, select one to run:

 [1] DemoOrganizations
 [2] DemoRepositories
 [3] DemoUser
 [4] DemoZen

Enter number:
```
- Chose the number of the demo to run

eg, if you choose `4` you'll get something like that:

```shell
[info] Running DemoZen

               MMM.           .MMM
               MMMMMMMMMMMMMMMMMMM
               MMMMMMMMMMMMMMMMMMM      _____________________
              MMMMMMMMMMMMMMMMMMMMM    |                     |
             MMMMMMMMMMMMMMMMMMMMMMM   | Speak like a human. |
            MMMMMMMMMMMMMMMMMMMMMMMM   |_   _________________|
            MMMM::- -:::::::- -::MMMM    |/
             MM~:~ 00~:::::~ 00~:~MM
        .. MMMMM::.00:::+:::.00::MMMMM ..
              .MM::::: ._. :::::MM.
                 MMMM;:::::;MMMM
          -MM        MMMMMMM
          ^  M+     MMMMMMMMM
              MMMMMMM MM MM MM
                   MM MM MM MM
                   MM MM MM MM
                .~~MM~MM~MM~MM~~.
             ~~~~MM:~MM~~~MM~:MM~~~~
            ~~~~~~==~==~~~==~==~~~~~~
             ~~~~~~==~==~==~==~~~~~~
                 :~==~==~==~==~~

[success] Total time: 112 s, completed Nov 1, 2016 11:31:15 AM
```

## Use `src/main/scala/Client.scala`

This source code can work with :octocat:.com and :octocat: Enterprise

### Create a GitHub client

- First, go to your GitHub profile settings and define a **Personal access token** (https://github.com/settings/tokens)
- Then, add the token to the environment variables (eg: `export TOKEN_GITHUB_DOT_COM=token_string`)
- Now you can get the token like that: `sys.env("TOKEN_GITHUB_DOT_COM")`

```scala
val githubCliEnterprise = new github.Client(
  "http://github.at.home/api/v3",
  sys.env("TOKEN_GITHUB_ENTERPRISE")
)

val githubCliDotCom = new github.Client(
  "https://api.github.com",
  sys.env("TOKEN_GITHUB_DOT_COM")
)
```

- if you use GitHub Enterprise, `baseUri` has to be set with `http(s)://your_domain_name/api/v3`
- if you use GitHub.com, `baseUri` has to be set with `https://api.github.com`

### Use the GitHub client

For example, you want to get the information about a user:
(see https://developer.github.com/v3/users/#get-a-single-user)

#### Adding features

You can add "features" to `GitHubClient` using Scala traits:

```scala
val gitHubCli = new github.Client(
  "https://api.github.com",
  sys.env("TOKEN_GITHUB_DOT_COM")
) with Users


gitHubCli.fetchUser("k33g").fold(
  {errorMessage => println(errorMessage)},
  {userInformation:Option[Any] =>
    println(
      userInformation
        .map(user => user.asInstanceOf[Map[String, Any]])
        .getOrElse("Huston? We've got a problem!")
    )
  }
)
```

You can add more than one feature:

```scala
val gitHubCli = new github.Client(
  "http://github.at.home/api/v3",
  sys.env("TOKEN_GITHUB_ENTERPRISE")
) with Organizations
  with Repositories
```

## Add features to the GitHub Client

- It's simple: just add a trait to the `github.features` package.
- The trait must extend `RESTMethods` from `github.features`

```scala
trait KillerFeatures extends RESTMethods {

  def feature1():Either[String, String] = {
    // foo
  }

  def feature2():Either[String, String] = {
    // foo
  }
}
```

See the `github.features` package for more samples

## About Models

There is no GitHub Model, data are provided inside `Map[String, Any]`
# GitHub GraphQL API: Query Samples

This repository holds query samples for the GitHub GraphQL API. It's an easy way to get started using the GraphQL API for common workflows. You can copy and paste these queries into [GraphQL Explorer](https://developer.github.com/early-access/graphql/explorer) or you can use the included script.

### How to use the included script

1. Generate a [personal access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/) for use with these queries.
1. Run `npm install`
1. Pick the name of one of the included queries in the `/queries` directory, such as `viewer.graphql`.
1. Run `bin/run-query <query_file> <token>`

To change variable values, modify the variables in the `.graphql` file.
# Running GraphiQL on Enterprise

The GraphiQL Editor hosted on https://developer.github.com/v4/explorer/ is tied to your GitHub.com account, so in order to use this IDE with GitHub Enterprise, you'll need your own copy of GraphiQL that has access to your instance. There are a couple of options available, depending on your preference:

### MacOS App
Download the [GraphiQL App](https://github.com/skevy/graphiql-app) and you'll be able to specify the endpoint of your GitHub Enterprise instance.

You can download a binary directly from the [releases](https://github.com/skevy/graphiql-app/releases) tab, but there's also a Cask for use with Homebrew which will download and install the latest release:
`brew cask install graphiql`

### Browser Client
GraphiQL is also available as an NPM module that can be deployed to the browser. This folder includes an adaptation of the official [GraphQL NodeJS example](https://github.com/graphql/graphiql/tree/master/example) designed to be deployed to Pages on GitHub Enterprise.

#### On-prem Considerations
As GitHub Enterprise is designed to run "behind your firewall" and is sometimes deployed in environments without direct internet access, this repo is setup to host the React and GraphiQL dependencies locally.

By default, this example will query against the GitHub Enterprise appliance it's hosted on. For instance, if the repo is located at `https://example.com/<username>/graphiql-pages`, the IDE will query the GraphQL API located at `https://example.com/api/graphql`. This will work whether or not subdomain isolation is enabled.


#### Setup
The example in this folder contains all source files necessary to get GraphiQL working with Pages on GitHub Enterprise. Copy the `graphql/enterprise` directory from this repository into a new repository on your Enterprise server, then [configure GitHub Pages to publish the master branch](https://help.github.com/enterprise/user/articles/configuring-a-publishing-source-for-github-pages/). A URL will be created for you automatically.

#### Development
There is a basic build script included that will copy the minified react and graphiql dependencies into the `dist/` folder. For further development, you can use `npm` or `yarn` to work with the original source libraries.

**NPM**
```shell
// Install full dependencies
$ npm install
// Copy the minified React, GraphiQL and Primer-CSS modules into the `dist/` folder
$ npm run build

```
**Yarn**
```shell
// Install dependencies
$ yarn
// Copy the minified React, GraphiQL and Primer-CSS modules into the `dist/` folder
$ yarn build
```

### Authentication
In both cases, you'll need to [create a personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) with the appropriate scopes to the data you want to query.
# app-issue-creator

This is the sample project that walks through creating a GitHub App and configuring a server to listen to [`installation` events](https://developer.github.com/v3/activity/events/types/#installationevent). When an App is added to an account, it will create an issue in each repository with a message, "added new app!".

## Requirements

* Ruby installed
* [Bundler](http://bundler.io/) installed
* [ngrok](https://ngrok.com/) or [localtunnel](https://localtunnel.github.io/www/) exposing port `4567` to allow GitHub to access your server

## Set up a GitHub App

* [Set up and register GitHub App](https://developer.github.com/apps/building-integrations/setting-up-and-registering-github-apps/)
* [Enable `issue` write permissions](https://developer.github.com/v3/apps/permissions/#permission-on-issues)
* If not running on a public-facing IP, use ngrok to generate a URL as [documented here](https://developer.github.com/v3/guides/building-a-ci-server/#writing-your-server)

## Install and Run project

Install the required Ruby Gems by entering `bundle install` on the command line. 

Set environment variables `GITHUB_APP_ID` and `GITHUB_APP_PRIVATE_KEY`. For example, run the following to store the private key to an environment variable: `export GITHUB_APP_PRIVATE_KEY="$(less private-key.pem)"`

To start the server, type `ruby server.rb` on the command line.

The [sinatra server](http://www.sinatrarb.com/) will be running at `localhost:4567`.

[basics of auth]: http://developer.github.com/guides/basics-of-authentication/
## Getting started
This example will take action based on webhooks received from Jira. The actions demonstrated here are:

1. Create a `branch` in GitHub when a `Version` is _created_ in Jira
2. Create a `release` in GitHub when a `Version` is _released_ in Jira

Projects in Jira are mapped to repositories in GitHub based on a `.github/jira-workflow.yml` file and can be altered to suit your needs

### Plugins
In order to configure our Jenkins instance to receive `webhooks` and process them for this example, while storing our [Pipeline as Code](https://jenkins.io/solutions/pipeline), we will need to install a few plugins.

- [Pipeline](https://plugins.jenkins.io/workflow-aggregator): This plugin allows us to store our `Jenkins` _jobs_ as code, and moves away from the common understanding of Jenkins `builds` to an `Agile` and `DevOps` model
- [Pipeline: Declarative](https://plugins.jenkins.io/pipeline-model-definition): Provides the ability to write _declarative pipelines_ and add `Parallel Steps`, `Wait Conditions` and more
- [Pipeline: Basic Steps](https://plugins.jenkins.io/workflow-basic-steps): Provides many of the most commonly used classes and functions used in _Pipelines_
- [Pipeline: Job](https://plugins.jenkins.io/workflow-job): Allows us to define `Triggers` within our _Pipeline_
- [Pipeline: Utility Steps](https://plugins.jenkins.io/pipeline-utility-steps): Provides us with the ability to read config files, zip archives and files on the filesystem
- [Build with Parameters](https://plugins.jenkins.io/build-with-parameters): Allows us to provide parameters to our pipeline
- [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger): This plugin allows any webhook to trigger a build in Jenkins with variables contributed from the JSON/XML. We'll use this plugin instead of a _GitHub specific_ plugin because this one allows us to trigger on _any_ webhook, not just `pull requests` and `commits`
- [HTTP Request](https://plugins.jenkins.io/http_request): This plugin allows us to send HTTP requests (`POST`,`GET`,`PUT`,`DELETE`) with parameters to a URL
- [Jira Pipeline Steps](https://plugins.jenkins.io/jira-steps): Allows using Jira steps within a _Jenkinsfile_
- [Jira](https://plugins.jenkins.io/jira): Enables integration with Jira
- [Credentials Binding](https://plugins.jenkins.io/credentials-binding): Allows credentials to be bound to environment variables for use from miscellaneous build steps.
- [Credentials](https://plugins.jenkins.io/credentials): This plugin allows you to store credentials in Jenkins.

### Setting up the repo

This example pipeline will read the workflow settings from a YAML file in the `.github` directory of the repository where the pipeline lives, _not_ the repository where the code for your project lives. This particular example is a standalone Jenkins pipeline that will be triggered by multiple projects/orgs.

<details><summary>Sample .github/jira-workflow.yml</summary>

```yaml
# The list of Jira projects that we care about 
# will be keys under 'project'
project:
    # The name of the project in Jira, not the key.
    # if we want the key we can certainly update the
    # pipeline to use that instead
  - name: GitHub-Demo
    # The name of the org in GitHub that will be mapped
    # to this project. We cannot use a list here, since
    # we will use a list for the repos
    org: GitHub-Demo
    # A list of repositories that are tied to this project.
    # Each repo here will get a branch matching the version
    repos: 
      - sample-core
      - sample-api
      - sample-ui
```
</details>

### Getting Jenkins set up
Before getting started with the pipeline you'll need to setup a few things.

1. Create a `username`/`password` credential which uses your GitHub token
2. Create a `username`/`password` credential which has access to Jira
3. Create a Jira configuration in `Settings`


This demonstration will make use of the [Declarative Pipeline](https://jenkins.io/doc/book/pipeline/syntax) syntax for Jenkins, and not the less structured _advanced scripting_ syntax. So, in getting started we'll note a few things. 

First, because we're dynamically generating parallel steps, we'll need to declare our variables _outside_ the pipeline so we don't hit errors when assigning values to them.

```groovy
def settings
def projectInfo
def githubUrl = "https://api.github.com/"
// This is an array we'll use for dynamic parallization
def repos = [:]
```

Once you've declared them, some with values you won't change and some with no values (we'll set them dynamically), let's enable some debug output so we can test our pipeline and adjust it for the things we need. **This step is optional, but will help you extend this example.**

```groovy
node {
  echo sh(returnStdout: true, script: 'env')
}
```

Now we can begin the pipeline itself

```groovy
pipeline {
```

#### Setting up the triggers
The *Generic Webhook Trigger* plugin makes use of a token to differentiate pipelines. You can generate a generic token for this pipeline by running `uuidgen` at the command line on a Unix system, or `[Guid]::NewGuid().ToString()` in PowerShell. 

##### Bash
```bash
Shenmue:~ primetheus$ uuidgen
6955F09B-EF96-467F-82EB-A35997A0C141
```
##### Powershell
```powershell
PS /Users/primetheus> [Guid]::NewGuid().ToString()
b92bd80d-375d-4d85-8ba5-0c923e482262
```

Once you have generated your unique ID, add the token to the pipeline as a trigger. We'll capture a few variables about the webhook we'll receive as well, and use them later in the pipeline

```groovy
  triggers {
    GenericTrigger(
      genericVariables: [
        [key: 'event', value: '$.webhookEvent'],
        [key: 'version', value: '$.version'],
        [key: 'projectId', value: '$.version.projectId'],
        [key: 'name', value: '$.version.name'],
        [key: 'description', value: '$.version.description']
      ],

      causeString: 'Triggered on $ref',
      // This token is arbitrary, but is used to trigger this pipeline.
      // Without a token, ALL pipelines that use the Generic Webhook Trigger
      // plugin will trigger 
      token: 'b92bd80d-375d-4d85-8ba5-0c923e482262',
      printContributedVariables: true,
      printPostContent: true,
      silentResponse: false,
      regexpFilterText: '',
      regexpFilterExpression: ''
    )
  }
```

#### Creating our stages
Once we have the triggers created, let's begin creating our [Stages](https://jenkins.io/doc/book/pipeline/syntax/#stages) for the pipeline.

First, open the `Stages` section

```groovy
stages {
```

Then let's read our YAML file from the repo

```groovy
    stage('Get our settings') {
      steps {
        script {
          try {
            settings = readYaml(file: '.github/jira-workflow.yml')
          } catch(err) {
            echo "Please create .github/jira-workflow.yml"
            throw err
          }
        }
      }
    }
```

Once we've read the settings file (or aborted because one doesn't exist), we'll lookup the project info from Jira. The webhook will send us a Project ID, which won't really help us as humans to map, so we'll look this up once we get the payload.

```groovy
    stage('Get project info') {
      steps {
        script {
          projectInfo = jiraGetProject(idOrKey: projectId, site: 'Jira')
        }
      }
    }
```

Now we're going to apply the mapping to our repositories, and if we have multiple repos we'll generate parallel steps for each one.

```groovy
    stage('Create Release Branches') {
      when {
        expression { event == 'jira:version_created' }
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: '<github_credentials_id>', 
                              passwordVariable: 'githubToken', 
                              usernameVariable: 'githubUser')]) {
            settings.project.each { p ->
              if (p.name.toString() == projectInfo.data.name.toString()) {
                p.repos.each { repo ->
                  repos[repo] = {
                    node {
                      httpRequest(
                        contentType: 'APPLICATION_JSON',
                        consoleLogResponseBody: true,
                        customHeaders: [[maskValue: true, name: 'Authorization', value: "token ${githubToken}"]],
                        httpMode: 'GET',
                        outputFile: "${p.org}_${repo}_master_refs.json",
                        url: "${githubUrl}/repos/${p.org}/${repo}/git/refs/heads/master")
                      masterRefs = readJSON(file: "${p.org}_${repo}_master_refs.json")
                      payload = """{
                        "ref": "refs/heads/${name}",
                        "sha": "${masterRefs['object']['sha']}"
                      }"""
                      httpRequest(
                        contentType: 'APPLICATION_JSON',
                        consoleLogResponseBody: true,
                        customHeaders: [[maskValue: true, name: 'Authorization', value: "token ${githubToken}"]],
                        httpMode: 'POST',
                        ignoreSslErrors: false,
                        requestBody: payload,
                        responseHandle: 'NONE',
                        url: "${githubUrl}/repos/${p.org}/${repo}/git/refs")
                    }
                  }
                }
                parallel repos
              }
            }
          }
        }
      }
```

<details><summary>Sample Pipeline</summary>

```groovy
// Define variables that we'll set values to later on
// We only need to define the vars we'll use across stages
def settings
def projectInfo
// This is an array we'll use for dynamic parallization
def repos = [:]
def githubUrl = "https://github.example.com/api/v3"
//def githubUrl = "https://api.github.com/"

node {
  // useful debugging info 
  echo sh(returnStdout: true, script: 'env')
}

pipeline {
  // This can run on any agent... we can lock it down to a 
  // particular node if we have multiple nodes, but we won't here
  agent any
  triggers {
    GenericTrigger(
      genericVariables: [
        [key: 'event', value: '$.webhookEvent'],
        [key: 'version', value: '$.version'],
        [key: 'projectId', value: '$.version.projectId'],
        [key: 'name', value: '$.version.name'],
        [key: 'description', value: '$.version.description']
      ],

      causeString: 'Triggered on $ref',
      // This token is arbitrary, but is used to trigger this pipeline.
      // Without a token, ALL pipelines that use the Generic Webhook Trigger
      // plugin will trigger 
      token: '6BE4BF6E-A319-40A8-8FE9-D82AE08ABD03',
      printContributedVariables: true,
      printPostContent: true,
      silentResponse: false,
      regexpFilterText: '',
      regexpFilterExpression: ''
    )
  }
  stages {
    // We'll read our settings in this step
    stage('Get our settings') {
      steps {
        script {
          try {
            settings = readYaml(file: '.github/jira-workflow.yml')
            //sh("echo ${settings.project}")
          } catch(err) {
            echo "Please create .github/jira-workflow.yml"
            throw err
            //currentBuild.result = 'ABORTED'
            //return
            //currentBuild.rawBuild.result = Result.ABORTED //This method requires in-process script approval, but is nicer than what's running currently
          }
        }
      }
    }
    stage('Get project info') {
      steps {
        script {
          //  echo projectId
          projectInfo = jiraGetProject(idOrKey: projectId, site: 'Jira')
          //  echo projectInfo.data.name.toString()
        }
      }
    }
    stage('Create Release Branches') {
      when {
        // Let's only run this stage when we have a 'version created' event
        expression { event == 'jira:version_created' }
      }
      steps {
        script {
          // Specify our credentials to use for the steps
          withCredentials([usernamePassword(credentialsId: '<github_credentials_id>', 
                              passwordVariable: 'githubToken', 
                              usernameVariable: 'githubUser')]) {
            // Loop through our list of Projects in Jira, which will map to Orgs in GitHub.
            // We're assigning it 'p' since 'project' is assigned as part of the YAML structure
            settings.project.each { p ->
              // Only apply this release to the proper Org
              if (p.name.toString() == projectInfo.data.name.toString()) {
                // Loop through each repo in the Org
                p.repos.each { repo ->
                  // Create an array that we will use to dynamically parallelize the 
                  // actions with. 
                  repos[repo] = {
                    node {
                      // Get the master refs to create the branches from
                      httpRequest(
                        contentType: 'APPLICATION_JSON',
                        consoleLogResponseBody: true,
                        customHeaders: [[maskValue: true, name: 'Authorization', value: "token ${githubToken}"]],
                        httpMode: 'GET',
                        outputFile: "${p.org}_${repo}_master_refs.json",
                        url: "${githubUrl}/repos/${p.org}/${repo}/git/refs/heads/master")
                      // Create a variable with the values from the GET response
                      masterRefs = readJSON(file: "${p.org}_${repo}_master_refs.json")
                      // Define the payload for the GitHub API call
                      payload = """{
                        "ref": "refs/heads/${name}",
                        "sha": "${masterRefs['object']['sha']}"
                      }"""
                      // Create the new branches
                      httpRequest(
                        contentType: 'APPLICATION_JSON',
                        consoleLogResponseBody: true,
                        customHeaders: [[maskValue: true, name: 'Authorization', value: "token ${githubToken}"]],
                        httpMode: 'POST',
                        ignoreSslErrors: false,
                        requestBody: payload,
                        responseHandle: 'NONE',
                        url: "${githubUrl}/repos/${p.org}/${repo}/git/refs")
                    }
                  }
                }
                // Execute the API calls simultaneously for each repo in the Org
                parallel repos
              }
            }
          }
        }
      }
    }
    stage('Create Release') {
      when {
        // Let's only run this stage when we have a 'version created' event
        expression { event == 'jira:version_released' }
      }
      steps {
        script {
          // Specify our credentials to use for the steps
          withCredentials([usernamePassword(credentialsId: '<github_credentials_id>', 
                              passwordVariable: 'githubToken', 
                              usernameVariable: 'githubUser')]) {
            // Loop through our list of Projects in Jira, which will map to Orgs in GitHub.
            // We're assigning it 'p' since 'project' is assigned as part of the YAML structure
            settings.project.each { p ->
              // Only apply this release to the proper Org
              if (p.name.toString() == projectInfo.data.name.toString()) {
                // Loop through each repo in the Org
                p.repos.each { repo ->
                  // Create an array that we will use to dynamically parallelize the actions with. 
                  repos[repo] = {
                    node {
                      // Get the current releases
                      httpRequest(
                        contentType: 'APPLICATION_JSON',
                        consoleLogResponseBody: true,
                        customHeaders: [[maskValue: true, name: 'Authorization', value: "token ${githubToken}"]],
                        httpMode: 'GET',
                        outputFile: "${p.org}_${repo}_releases.json",
                        url: "${githubUrl}/repos/${p.org}/${repo}/releases")
                      // Create a variable with the values from the GET response
                      releases = readJSON(file: "${p.org}_${repo}_releases.json")
                      // Define the payload for the GitHub API call
                      def payload = """{
                        "tag_name": "${name}",
                        "target_commitish": "${name}",
                        "name": "${name}",
                        "body": "${description}",
                        "draft": false,
                        "prerelease": false
                      }"""
                      // Create the new release
                      httpRequest(
                        contentType: 'APPLICATION_JSON',
                        consoleLogResponseBody: true,
                        customHeaders: [[maskValue: true, name: 'Authorization', value: "token ${githubToken}"]],
                        httpMode: 'POST',
                        ignoreSslErrors: false,
                        requestBody: payload,
                        responseHandle: 'NONE',
                        url: "${githubUrl}/repos/${p.org}/${repo}/releases")
                    }
                  }
                }
                // Execute the API calls simultaneously for each repo in the Org
                parallel repos
              }
            }
          }
        }
      }
    }
  }
}
```

</details>
## Jira issue validator
In order to use this pipeline, you will need the following plugins:

- [Pipeline](https://plugins.jenkins.io/workflow-aggregator): This plugin allows us to store our `Jenkins` _jobs_ as code, and moves away from the common understanding of Jenkins `builds` to an `Agile` and `DevOps` model
- [Pipeline: Declarative](https://plugins.jenkins.io/pipeline-model-definition): Provides the ability to write _declarative pipelines_ and add `Parallel Steps`, `Wait Conditions` and more
- [Pipeline: Basic Steps](https://plugins.jenkins.io/workflow-basic-steps): Provides many of the most commonly used classes and functions used in _Pipelines_
- [Pipeline: Job](https://plugins.jenkins.io/workflow-job): Allows us to define `Triggers` within our _Pipeline_
- [Pipeline: Utility Steps](https://plugins.jenkins.io/pipeline-utility-steps): Provides us with the ability to read config files, zip archives and files on the filesystem
- [GitHub Integration](https://plugins.jenkins.io/github-pullrequest): Provides the ability to customize pull request builds
- [Pipeline: GitHub](https://plugins.jenkins.io/pipeline-github): Allows using GitHub steps within a _Jenkinsfile_
- [GitHub](https://plugins.jenkins.io/github): Provides integration with GitHub
- [Jira Pipeline Steps](https://plugins.jenkins.io/jira-steps): Allows using Jira steps within a _Jenkinsfile_
- [Jira](https://plugins.jenkins.io/jira): Enables integration with Jira

### Configuring Jenkins

1. Log in to Jenkins and click _Manage Jenkins_
2. Click _Configure System_
3. In the **Jira Steps** section, provide the required information for connecting to your Jira server
![jenkins-setup-jira](https://user-images.githubusercontent.com/865381/39254110-587316e2-4877-11e8-93f0-9050a7144ea2.png)
4. In the **GitHub Pull Request Builder** section, fill out the connection information
![jenkins-config-gh-pull-1](https://user-images.githubusercontent.com/865381/39254113-5d8fde58-4877-11e8-81f5-fb037ae06266.png)
![jenkins-setup-gh-pull-2](https://user-images.githubusercontent.com/865381/39254114-5dacc112-4877-11e8-9a0b-f1a8643de7c0.png)

### Creating the pipeline
1. Log in to Jenkins and click _New Item_
2. Give it a name and select _Pipeline_ as the type
![jira-github-validation](https://user-images.githubusercontent.com/865381/37780888-0e1d3c88-2dc6-11e8-8cd8-4b3efc55a1f1.png)
3. Check the box to enable _GitHub Project_ and provide the URL for the repository
![jenkins-github-pr-validation](https://user-images.githubusercontent.com/865381/37780961-31ee22bc-2dc6-11e8-88a3-9bec66621840.png)
4. Check the box to trigger on _GitHub Pull Requests_
  4a. Choose _Hooks with Persisted Data_ as the **Trigger Mode*
  4b. Check the box to _Set status before build_
  4c. Add _Commit changed_ and _Pull Request Opened_ as the **Trigger Events**
![jenkins-github-integration-pr-trigger](https://user-images.githubusercontent.com/865381/37780979-38469c84-2dc6-11e8-98b2-19c06b77fcf4.png)


### Example pipeline
This pipeline functions by taking the _issue ID_ from the pull request body, performing a lookup in Jira, then setting the status of the build in GitHub based on the _transition_ in Jira.

```groovy
node {
  properties([
    [$class: 'BuildDiscarderProperty',
      strategy: [$class: 'LogRotator',
        artifactDaysToKeepStr: '',
        artifactNumToKeepStr: '',
        daysToKeepStr: '',
        numToKeepStr: '5']
    ]
  ])
  stage('Validate JIRA Issue') {
    //echo sh(returnStdout: true, script: 'env')
    // Get the issue number from the PR Title
    def prTitleJira = sh(
        script: "echo \${GITHUB_PR_TITLE}|awk {'print \$1'}",
        returnStdout: true)

    // Get the issue number from the PR Body
    def prBodyJira = sh(
        script: "echo \${GITHUB_PR_BODY}|awk {'print \$1'}",
        returnStdout: true)

    // Convert the discovered issue to a string
    def prIssue = prBodyJira.trim()

    // Validate that the issue exists in JIRA
    def issue = jiraGetIssue (
        site: "JIRA",
        idOrKey: "${prIssue}")

    // Validate the state of the ticket in JIRA
    def transitions = jiraGetIssueTransitions (
        site: "JIRA",
        idOrKey: "${prIssue}")

    // Create a variable from the issue state
    def statusId = issue.data.fields.status.statusCategory.id.toString()
    def statusName = issue.data.fields.status.statusCategory.name.toString()

    // Validate that it's in the state that we want
    if (statusId == '4') {
        setGitHubPullRequestStatus (
            context: "",
            message: "${prIssue} is in the correct status",
            state: "SUCCESS")
    } else {
        setGitHubPullRequestStatus (
            context: "",
            message: "${prIssue} is not properly prepared in JIRA. Please place it in the current sprint and begin working on it",
            state: "FAILURE")
    }
  }
}
```

### Visual status
1. Create a new file with a commit message. The Jira plugin will automatically comment on the ticket if you use the `JIRA-[number] #comment <comment>` format
![jenkins-jira-commit](https://user-images.githubusercontent.com/865381/37779241-544b8bc8-2dc2-11e8-8dd6-aaca12556ed0.png)

2. Create a new pull request, and be sure that `JIRA-[number]` is the first word in the _body_
![jenkins-jira-pr-body](https://user-images.githubusercontent.com/865381/37779286-7056832c-2dc2-11e8-9cfb-82a931d40ca0.png)

#### Ticket is not _In Progress_
![jenkins-jira-pr-check-fail](https://user-images.githubusercontent.com/865381/37779349-9480bfd8-2dc2-11e8-895a-38088692f071.png)

#### Ticket is _In Progress_
![jenkins-jira-validator-pass](https://user-images.githubusercontent.com/865381/37779337-8f198138-2dc2-11e8-915f-a28130bc02ba.png)
# GitHub webhooks in Jenkins
- [Installing Jenkins](#installing-jenkins)
  * [Running in Docker](#running-jenkins-in-docker)
     - [Upgrading Jenkins in Docker](#upgrading-jenkins-in-docker)
  * [Installing Jenkins on RedHat/CentOS 7](#installing-jenkins-on-redhatcentos-7)
  * [Installing Jenkins on Ubuntu/Debian](#installing-jenkins-on-ubuntudebian)
  * [Additional installation options](#additional-installation-options)
  * [Obtaining the initial password](#obtaining-the-initial-password)
     - [Docker](#docker)
     - [Linux](#linux)
  * [Completing the setup](#completing-the-setup)
- [Installing plugins](#installing-plugins)
- [Styling Jenkins](#styling-jenkins)
- [Creating the webhook](#creating-the-webhook)
- [Creating the pipeline](#creating-the-pipeline)
  * [Git credentials in Jenkins](#git-credentials-in-jenkins)
  * [Defining our actions](#defining-our-actions)
  * [Defining the payload](#defining-the-payload)
  * [Tying it all together](#tying-it-all-together)
- [Adding the pipeline to Jenkins as a webhook listener](#adding-the-pipeline-to-jenkins-as-a-webhook-listener)

# Overview
The purpose of this guide is to address a particular scenario, wherein repositories are created but no branches are protected. In this example we will utilize `Jenkins` to process _webhooks_ that GitHub sends each time a branch is created. Once the webhook is received, Jenkins will analyse the payload and make an API call back to GitHub to:

1. Protect the `master` branch. If the `master` branch is named anything but `master`, then whatever branch that is will be protected instead
2. Ensure pull request reviews are required
3. Add administrators to the repository
4. Dismiss stale pull requests
5. Require `Code Owner` reviews

In order to achieve this goal, we will enable a webhook at the _Organization_ level to trigger on `Create` actions for any existing or new repositories. We chose `Create` actions instead of `Repository` because it is possible to create a repository without initializing it, which will send a payload to Jenkins with an empty branch name, and will ultimately cause the execution to fail. Subsequently, if this happens, a new webhook will not trigger if a new `master` branch is created after the fact. Therefore, triggering on `Create` will trigger when and only when branches or tags are created, which produces the precise effect we desire in the scenario.

#### Certificates
Before getting started, ensure that you have a trusted certificate, or that you import the GitHub certificate into Jenkins. Without this step, Jenkins will fail to clone any repositories via `HTTPS`, and the webhook will likely fail as well.

## Installing Jenkins
For this instance we will be using **_Jenkins 2.x_** because of its support for storing _Pipeline as Code_ and keeping in line with the DevOps phylosophy and spirit of collaboration.

### Running Jenkins in Docker
Let's create a container in `Docker` to run Jenkins. In this demo, we want it to run as a service and behave in a _production-like_ manner. To do this, we'll utilize the following flags:

Flag | Description
--- | ---
-d | This allows the container to run as a daemon, rather than running in the foreground of your terminal
-i | This allows _interaction_ with the container
-t | This will assign a _pseudo TTY_ interface
-p | This will map ports from the host to the container
--name | Allows you to set a name so you can manage the container with a _human-readable_ reference
--restart | Determine the restart behavior. This is particularly useful when using Docker to run services. **Options:** `always`, `unless-stopped`

We'll be mapping port `8080`, naming the container `jenkins` and configuring it to restart anytime it might crash, unless we explicitly stop it with `docker stop jenkins`.

```bash
docker run -ditp 8080:8080 --restart unless-stopped --name jenkins jenkins:latest
```

#### Upgrading Jenkins in Docker
1. If the container is already running, stop the container
```bash
docker stop jenkins
```
2. Download the latest version of Jenkins
```bash
wget http://updates.jenkins-ci.org/download/war/2.89.2/jenkins.war
```
3. Copy the `war` file into the container
```bash
docker cp jenkins.war jenkins:/usr/share/jenkins/jenkins.war
```
4. Start the container
```bash
docker start jenkins
```

### Installing Jenkins on RedHat/CentOS 7
1. Add the Jenkins repository

```bash
sudo curl -C - -LR#o /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
```
```bash
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
```

2. Install OpenJDK-8 and Jenkins

```bash
yum -y install openjdk-8-jdk jenkins
```
_**Alternate Option: Oracle Java with Jenkins RPM**_
<details>

Download the Oracle Java JDK 8u152 RPM

```bash
curl -C - -LR#OH "Cookie: oraclelicense=accept-securebackup-cookie" -k http://download.oracle.com/otn-pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.rpm
```

Download the Jenkins 2.89.2-1.1 RPM
```bash
curl -C - -LR#O -k https://pkg.jenkins.io/redhat-stable/jenkins-2.89.2-1.1.noarch.rpm
```

Install Java and Jenkins
```bash
yum -y localinstall jdk-8u152-linux-x64.rpm jenkins-2.89.2-1.1.noarch.rpm
```

</details>

### Installing Jenkins on Ubuntu/Debian
![important note](https://www.iconsdb.com/icons/download/orange/warning-16.png) **It _may_ be necessary to install `wget` if you are working with a minimal installation. If that is the case, simply run `sudo apt install wget` before running the following steps.**

1. Add the Jenkins repository

```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
```
```bash
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

```bash
sudo apt-get update
```

2. Install OpenJDK-8 and Jenkins

```bash
sudo apt-get -y install openjdk-8-jre-headless jenkins
```

### Additional installation options
For more information on installing Jenkins on another operating system, or to install using the `WAR` file, please refer to [https://jenkins.io/doc/book/installing](https://jenkins.io/doc/book/installing)

### Obtaining the initial password
Now we have a running instance of Jenkins. Let's grab the administrative key, which is stored in `/var/jenkins_home/secrets/initialAdminPassword`, so we can initially configure our instance

![unlock jenkins](https://user-images.githubusercontent.com/865381/39252315-65b30e6a-4873-11e8-9855-d12bdc4ff36c.png)

#### Docker
```bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

#### Linux
```bash
cat /var/jenkins_home/secrets/initialAdminPassword
```

The output should be something similar to `91d94f8f73df4f1c809e014fd51bb78c`, which is our initial password.

### Completing the setup
Once you've entered the password, install the suggested plugins and configure the first _admin user_.

1. Click _Install suggested plugins_
![click install suggested plugins](https://user-images.githubusercontent.com/865381/39252351-78722950-4873-11e8-9732-c311ef1897f4.png)
![plugin install status](https://user-images.githubusercontent.com/865381/39252369-80f0567e-4873-11e8-911e-0026375be005.png)
2. Create the first _admin_ user
![create first admin user](https://user-images.githubusercontent.com/865381/39252373-829958fe-4873-11e8-9abf-de69626d468b.png)
3. Click _Start using Jenkins_ to complete the setup
![finish. click start using jenkins](https://user-images.githubusercontent.com/865381/39252375-83dd970c-4873-11e8-98df-2b0d7a2a57ab.png)


## Installing plugins
In order to configure our Jenkins instance to receive `webhooks` and process them for this example, while storing our [Pipeline as Code](https://jenkins.io/solutions/pipeline), we will need to install a few plugins.

- [Pipeline](https://plugins.jenkins.io/workflow-aggregator): This plugin allows us to store our `Jenkins` _jobs_ as code, and moves away from the common understanding of Jenkins `builds` to an `Agile` and `DevOps` model
- [Pipeline: Declarative](https://plugins.jenkins.io/pipeline-model-definition): Provides the ability to write _declarative pipelines_ and add `Parallel Steps`, `Wait Conditions` and more
- [Pipeline: Basic Steps](https://plugins.jenkins.io/workflow-basic-steps): Provides many of the most commonly used classes and functions used in _Pipelines_
- [Pipeline: Job](https://plugins.jenkins.io/workflow-job): Allows us to define `Triggers` within our _Pipeline_
- [Pipeline: Utility Steps](https://plugins.jenkins.io/pipeline-utility-steps): Provides us with the ability to read config files, zip archives and files on the filesystem
- [Build with Parameters](https://plugins.jenkins.io/build-with-parameters): Allows us to provide parameters to our pipeline
- [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger): This plugin allows any webhook to trigger a build in Jenkins with variables contributed from the JSON/XML. We'll use this plugin instead of a _GitHub specific_ plugin because this one allows us to trigger on _any_ webhook, not just `pull requests` and `commits`
- [HTTP Request](https://plugins.jenkins.io/http_request): This plugin allows us to send HTTP requests (`POST`,`GET`,`PUT`,`DELETE`) with parameters to a URL
- [Simple Theme](https://plugins.jenkins.io/simple-theme-plugin): _**OPTIONAL**_ - We'll use this plugin to make our Jenkins instance look a little nicer with a [material theme](http://afonsof.com/jenkins-material-theme/)

### Plugin installation steps
1. Click `Manage Jenkins`
2. Click `Manage Plugins`
3. Click the _Available_ tab
4. Type the name of the plugin in the _Search_ box
5. Check the box next to the plugin
6. Repeat the search and selection for each plugin
7. Click `Download now and install after restart` when all plugins have been selected
8. Check the box to `Restart Jenkins when installation is complete and no jobs are running`


![install jenkins plugins](https://user-images.githubusercontent.com/865381/39252453-a9ddf24e-4873-11e8-8202-8be8911bcbd1.gif)

## Styling Jenkins
1. Head over to the [Jenkins Material Theme Builder](http://afonsof.com/jenkins-material-theme) and choose a theme. You can even upload a custom logo for your instance.

![download jenkins material theme](https://user-images.githubusercontent.com/865381/39252474-b7beacdc-4873-11e8-8269-d7329ad1da13.gif)


2. Once you've selected and downloaded the theme, place it in the `userContent` directory of your Jenkins instance. To do this in **_Docker_**, run the following command:

```bash
docker cp jenkins-material-theme.css jenkins:/var/jenkins_home/userContent/jenkins-material-theme.css
```

3. Finally, apply the theme:

- Click _Manage Jenkins_ from the Jenkins dashboard
- Click _Configure System_
- Scroll down to the **_Theme_** section and add `/userContent/jenkins-material-theme.css` to the _URL of theme CSS_ field


![apply material theme](https://user-images.githubusercontent.com/865381/39252490-c4872066-4873-11e8-89c6-fc9829796f88.gif)

---
## Creating the webhook

The webhook that we'll create is going to be at the _Organization_, so that we can ensure that each repository created will have this webhook triggered.

In order to utilize this webhook, we'll need to create a token. This token will be unique to the _pipeline_ that we create, **_so it's important not to re-use tokens in Jenkins_**, or each pipeline that is associated with that token will be triggered when the webhook is triggered. To create our token, run the following command on _any_ unix-based system:

```bash
$ uuidgen
```

![important note](https://www.iconsdb.com/icons/download/orange/warning-16.png)  **Be sure to save this token, as we will need it when we create the pipeline in Jenkins as well!**

### Webhook settings

| Option | Value |
| --- | --- |
| **Payload URL** | `http://<jenkins_hostname>:<port>/generic-webhook-trigger/invoke?token=<token>` |
| **Content Type** | `application/json` |
| **Events** | `Create` |

![create new webhook](https://user-images.githubusercontent.com/865381/39252518-d7403f58-4873-11e8-8959-6bb04286d66c.gif)

## Creating the pipeline
### Git credentials in Jenkins
Create a credential store that will be used to checkout the Pipeline from Git. If your `Jenkinsfile` is in a _public_ repository then this credential is not necessary. It is also a good practice to provide useful descriptions when creating these credentials.

![important note](https://www.iconsdb.com/icons/download/orange/warning-16.png)  **This particular credential _must_ be a username/password credential for checking out the _Jenkinsfile_, as the _Git_ plugin currently does not support tokens for this portion. Alternately, you may use an SSH key or make the repository public**

![important note](https://www.iconsdb.com/icons/download/orange/warning-16.png) **Jenkins will store this as an _encrypted credential_ that can be called in a _pipeline_ by the credential ID.**

Since this particular pipeline is a webhook listener, it is not necessary for this user to have _write_ access to the repository. The user can safely be restricted to _read_ access without impacting the functionality.

If you have extended security settings applied you may have issues with authentication on a private repository. For that reason, it's recommended to use a _Personal Access Token_ and _SSH_ for checking out the repo.

1. Click on _Credentials_
2. Select the _Jenkins_ domain
3. Click _Global credentials (unrestricted)_
4. On the left, click _Add Credential_
5. Enter the credentials and save. The username should be _token_ if you're using a _Personal Access Token_, and the password should be the actual token

![important note](https://www.iconsdb.com/icons/download/orange/warning-16.png) **Note the ID here for using later in the pipeline**

![create jenkins credential - username, password](https://user-images.githubusercontent.com/865381/39252547-eb8cb70c-4873-11e8-9d65-6e93f73d87f9.gif)

Now we need to create a credential for Jenkins to protect a repo in GitHub.

![important note](https://www.iconsdb.com/icons/download/orange/warning-16.png)  **This must be a user in GitHub that has the ability to alter repositories in an organization!**

Log in to GitHub as the privileged user and create a _Personal Access Token_. This can be an admin specifically created for Jenkins, as the credentials will be securely stored in Jenkins.

It is also a good practice to give a useful description so that other administrators, or even yourself, can more easily maintain security as your team or organization scales.

1. Login to GitHub
2. Click _Settings_
3. Click _Developer settings_
4. Click _Personal access tokens_
5. Click _Generate token_
6. Give the token a descriptive name
7. Select the privileges required for your account

![create personal access token](https://user-images.githubusercontent.com/865381/39252589-fd3fa66c-4873-11e8-9737-1b03d4e8978f.gif)

![create jenkins credential - secret text](https://user-images.githubusercontent.com/865381/39252617-0a8db19c-4874-11e8-8698-05d898c900f3.gif)

#### Defining our actions
In this demo we'll be defining our _payload_ to execute the following actions against the **GitHub REST API**. Utilizing the _GraphQL v4 API_ is outside the scope of this project.

- Protect the `master` branch, which may or may not be named _master_. In this demo, it is named _master_
- Enforce admins
- Require `CODEOWNERS` review
- Define repository owners
- Define repository team ownership
The payload is defined in `JSON` format and will be stored in the pipeline as a _variable_

#### Defining the payload

```json
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
        "continuous-integration/jenkins/branch"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismissal_restrictions": {
      "users": [
        "hollyw0od",
        "primetheus"
      ],
      "teams": [
        "test-team"
      ]
    },
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true
  },
  "restrictions": {
    "users": [
      "hollyw0od",
      "primetheus"
    ],
    "teams": [
      "test-team"
    ]
  }
}
```

#### Processing the webhook
As the _GitHub Webhook_ is received, Jenkins needs to process the payload and we'll use some of the data as variables in our pipeline. In order to do this, we'll need to assign _variable prefixes_ to the payload so we can access the data programatically. What we need are the following:

Name | Variable | Description
--- | --- | ---
**repository** | `$.repository` | JSON object containing info about the repository
**organization** | `$.organization` | The name of the org that the repository lives in
**sender** | `$.sender` | The user that created the repo
**ref_type** | `$.ref_type` | The event type in the payload. This should be _branch_
**master_branch** | `$.master_branch` | The default branch of the repo. _This can be anything, but defaults to `master`_
**branch_name** | `ref` | The name of the branch that was just created

```groovy
    pipelineTriggers([
      [$class: 'GenericTrigger',
        genericVariables: [
          [expressionType: 'JSONPath', key: 'repository', value: '$.repository'],
          [expressionType: 'JSONPath', key: 'organization', value: '$.organization'],
          [expressionType: 'JSONPath', key: 'sender', value: '$.sender'],
          [expressionType: 'JSONPath', key: 'ref_type', value: '$.ref_type'],
          [expressionType: 'JSONPath', key: 'master_branch', value: '$.master_branch'],
          [expressionType: 'JSONPath', key: 'branch_name', value: 'ref']
        ],
        regexpFilterText: '',
        regexpFilterExpression: ''
      ]
    ])
```

#### Log rotation
We don't want to endlessly store these logs, but we can configure a retention period, or max number of logs to store. To do this, add properties to the `node { properties([ ]) }` section of the pipeline:

```groovy
    [$class: 'BuildDiscarderProperty',
      strategy: [$class: 'LogRotator',
        artifactDaysToKeepStr: '',
        artifactNumToKeepStr: '',
        daysToKeepStr: '',
        numToKeepStr: '5']
    ]
```

What the block of code specifies is:

| Setting | Value |
| --- | --- |
| Feature | Log rotation |
| Number of artifacts to keep | _unspecified_ |
| Number of days to keep artifacts | _unspecified_ |
| Number of days to keep logs | _unspecified_ |
| Number of logs to keep | 5 |

This pipeline does not generate artifacts, so the first to options will have no impact whatsoever. The number of days to keep _logs_ is also unspecified, so Jenkins will not clean up logs based on _when_ it runs, but we specify that it will only keep a total of 5 logs. This number can and should be adjusted to suit your specific needs.

#### Adding the HTTP request with credentials
Now that we've grabbed our variables, defined our payload, and set our log rotation, let's take action on the webhook. We'll need to create a `stage { }` section, match the incoming branch name to the _master branch_ name, and protect the branch if it is the master. We'll also add our credentials from our _Jenkins Credential Store_, which allows us to avoid storing usernames and passwords in our pipelines, and to keep things dynamic. See the [Jenkins documentation](https://jenkins.io/doc/pipeline/steps/credentials-binding/) for more information on credentials binding.

```groovy
withCredentials([string(credentialsId: '<credential_id>', variable: '<variable_name>')]) {
    //do something
}
```

**HTTP Request with Credentials**
>The code section below utilizes the `loki-preview` _application type_ in the header. This is a custom header type that GitHub uses for protected branches. Refer to [GitHub's documentation](https://developer.github.com/changes/2015-11-11-protected-branches-api/) for more info.

In this example, we are utilizing the **_HTTP Request_** plugin, and placing this request inside of the `withCredentials` block. This will wrap the HTTP data inside of the authentication.

```groovy
  stage("Protect Master Branch") {
    if(env.branch_name && "${branch_name}" == "${master_branch}") {
        withCredentials([string(credentialsId: '1cf07897-ad01-4e59-9975-617ea40cf111', variable: 'githubToken')]) {
          httpRequest(
              contentType: 'APPLICATION_JSON',
              consoleLogResponseBody: true,
              customHeaders: [
                  [maskValue: true, name: 'Authorization', value: "token ${githubToken}"],
                  [name: 'Accept', value: 'application/vnd.github.loki-preview']],
              httpMode: 'PUT',
              ignoreSslErrors: true,
              requestBody: githubPayload,
              responseHandle: 'NONE',
              url: "${repository_url}/branches/${repository_default_branch}/protection")
        }
    } else {
        sh(name: "Skip", script: 'echo "Move along, nothing to see here"')
    }
  }
```  

#### Tying it all together
The final result of the _Jenkins Pipeline_ is as follows, and is stored as a file called `Jenkinsfile` inside a git repo:

```groovy
node {
  properties([
    [$class: 'BuildDiscarderProperty',
      strategy: [$class: 'LogRotator',
        artifactDaysToKeepStr: '',
        artifactNumToKeepStr: '',
        daysToKeepStr: '',
        numToKeepStr: '5']
    ],
    pipelineTriggers([
      [$class: 'GenericTrigger',
        genericVariables: [
          [expressionType: 'JSONPath', key: 'repository', value: '$.repository'],
          [expressionType: 'JSONPath', key: 'organization', value: '$.organization'],
          [expressionType: 'JSONPath', key: 'sender', value: '$.sender'],
          [expressionType: 'JSONPath', key: 'ref_type', value: '$.ref_type'],
          [expressionType: 'JSONPath', key: 'master_branch', value: '$.master_branch'],
          [expressionType: 'JSONPath', key: 'branch_name', value: 'ref']
        ],
        regexpFilterText: '',
        regexpFilterExpression: ''
      ]
    ])
  ])
  def githubPayload = """{
      "required_status_checks": {
        "strict": true,
        "contexts": [
          "continuous-integration/jenkins/branch"
        ]
      },
      "enforce_admins": true,
      "required_pull_request_reviews": {
        "dismissal_restrictions": {
          "users": [
            "hollyw0od",
            "primetheus"
          ],
          "teams": [
            "test-team"
          ]
        },
        "dismiss_stale_reviews": true,
        "require_code_owner_reviews": true
      },
      "restrictions": {
        "users": [
          "hollyw0od",
          "primetheus"
        ],
        "teams": [
          "test-team"
        ]
      }
    }"""

  stage("Protect Master Branch") {
    if(env.branch_name && "${branch_name}" == "${master_branch}") {
        withCredentials([string(credentialsId: '1cf07897-ad01-4e59-9975-617ea40cf111', variable: 'githubToken')]) {
          httpRequest(
              contentType: 'APPLICATION_JSON',
              consoleLogResponseBody: true,
              customHeaders: [
                  [maskValue: true, name: 'Authorization', value: "token ${githubToken}"],
                  [name: 'Accept', value: 'application/vnd.github.loki-preview']],
              httpMode: 'PUT',
              ignoreSslErrors: true,
              requestBody: githubPayload,
              responseHandle: 'NONE',
              url: "${repository_url}/branches/${repository_default_branch}/protection")
        }
    } else {
        sh(name: "Skip", script: 'echo "Move along, nothing to see here"')
    }
  }
}
```

## Adding the pipeline to Jenkins as a webhook listener
Once you've created your pipeline, check it into GitHub and now we'll create the job in Jenkins. Let's create a new job, and configure it with the following settings:

Key | Value
--- | ---
Type | Pipeline
Pipeline Source | Pipeline from SCM
Additional | Build Remotely
Build Token | [_uuid_ from Creating the Webhook](#creating-the-webhook)

1. Click _New Item_
2. Give it a name
3. Select _Pipeline_ as the type and click _OK_
4. Click `Trigger builds remotely` and provide the token you created earlier with `uuidgen`. _This is a necessary step to link the token to this pipeline. Any other pipeline that uses the same token will also be triggered, so tokens should **not** be re-used_
5. Choose `Pipeline script from SCM` as the _Pipeline Definition_
6. Provide your _repository URL_
7. Choose your credentials for cloning the `Jenkinsfile`. If this is a public repo, no credentials are necessary
8. Add an _Additional Behavior_ to _Wipe out repository & force clone_, which will provide a fresh copy of the `Jenkinsfile` each time the pipeline runs
9. Save the job
10. **If this job has never been run, click _Build Now_ so it can pull down the definition**
11. _Depending on your version of Jenkins and the **Generic Webhook** plugin, you may need to re-deliver the payload the first time to ensure you don't hit a bug where it fails to read the payload_. It's a good idea to double and triple check the functionality before going live.

![create jenkins pipeline](https://user-images.githubusercontent.com/865381/39252653-1c318d56-4874-11e8-90d6-2ba21b5fa20f.gif)

## Triggering the build
Once you have the pipeline created, simply create a new repository and initialize it with some content. The creation of that first branch will trigger the webhook and execute the pipeline.

1. Login to GitHub
2. Navigate to the _Organization_ to create a repository
3. Create a repository. In this example we'll use **_demo_** as the name

![create repository](https://user-images.githubusercontent.com/865381/39252675-2c087d84-4874-11e8-9fc7-3bf6d950caf0.gif)

## The completed workflow
Once the pipeline has been triggered and completes, view the console output to see the payload and actions taken.

<details>
  <summary>Example Pipeline Output</summary>

```
Generic Cause
Obtained Jenkinsfile from git git@github-test.local:GitHub-Demo/jenkins-protect-branch.git
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/github-demo
[Pipeline] {
[Pipeline] properties
GenericWebhookEnvironmentContributor Received:

{"ref":"master","ref_type":"branch","master_branch":"master","description":null,"pusher_type":"user","repository":{"id":3,"name":"demo","full_name":"GitHub-Demo/demo","owner":{"login":"GitHub-Demo","id":6,"avatar_url":"https://github-test.local/avatars/u/6?","gravatar_id":"","url":"https://github-test.local/api/v3/users/GitHub-Demo","html_url":"https://github-test.local/GitHub-Demo","followers_url":"https://github-test.local/api/v3/users/GitHub-Demo/followers","following_url":"https://github-test.local/api/v3/users/GitHub-Demo/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/GitHub-Demo/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/GitHub-Demo/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/GitHub-Demo/subscriptions","organizations_url":"https://github-test.local/api/v3/users/GitHub-Demo/orgs","repos_url":"https://github-test.local/api/v3/users/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/users/GitHub-Demo/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/GitHub-Demo/received_events","type":"Organization","site_admin":false},"private":false,"html_url":"https://github-test.local/GitHub-Demo/demo","description":null,"fork":false,"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo","forks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/forks","keys_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/keys{/key_id}","collaborators_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/collaborators{/collaborator}","teams_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/teams","hooks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/hooks","issue_events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/events{/number}","events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/events","assignees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/assignees{/user}","branches_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches{/branch}","tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/tags","blobs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/blobs{/sha}","git_tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/tags{/sha}","git_refs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/refs{/sha}","trees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/trees{/sha}","statuses_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/statuses/{sha}","languages_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/languages","stargazers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/stargazers","contributors_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contributors","subscribers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscribers","subscription_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscription","commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/commits{/sha}","git_commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/commits{/sha}","comments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/comments{/number}","issue_comment_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/comments{/number}","contents_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contents/{+path}","compare_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/compare/{base}...{head}","merges_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/merges","archive_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/{archive_format}{/ref}","downloads_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/downloads","issues_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues{/number}","pulls_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/pulls{/number}","milestones_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/milestones{/number}","notifications_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/notifications{?since,all,participating}","labels_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/labels{/name}","releases_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/releases{/id}","deployments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/deployments","created_at":"2018-01-19T20:04:24Z","updated_at":"2018-01-19T20:04:24Z","pushed_at":"2018-01-19T20:04:25Z","git_url":"git://github-test.local/GitHub-Demo/demo.git","ssh_url":"git@github-test.local:GitHub-Demo/demo.git","clone_url":"https://github-test.local/GitHub-Demo/demo.git","svn_url":"https://github-test.local/GitHub-Demo/demo","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"open_issues_count":0,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"},"organization":{"login":"GitHub-Demo","id":6,"url":"https://github-test.local/api/v3/orgs/GitHub-Demo","repos_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/events","hooks_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/hooks","issues_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/issues","members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/members{/member}","public_members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/public_members{/member}","avatar_url":"https://github-test.local/avatars/u/6?","description":null},"sender":{"login":"primetheus","id":3,"avatar_url":"https://github-test.local/avatars/u/3?","gravatar_id":"","url":"https://github-test.local/api/v3/users/primetheus","html_url":"https://github-test.local/primetheus","followers_url":"https://github-test.local/api/v3/users/primetheus/followers","following_url":"https://github-test.local/api/v3/users/primetheus/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/primetheus/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/primetheus/subscriptions","organizations_url":"https://github-test.local/api/v3/users/primetheus/orgs","repos_url":"https://github-test.local/api/v3/users/primetheus/repos","events_url":"https://github-test.local/api/v3/users/primetheus/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/primetheus/received_events","type":"User","site_admin":true,"ldap_dn":"CN=Jared Murrell,CN=Users,DC=github-test,DC=local"}}


Contributing variables:

    repository_has_projects = true
    repository_open_issues = 0
    repository = {"id":3,"name":"demo","full_name":"GitHub-Demo/demo","owner":{"login":"GitHub-Demo","id":6,"avatar_url":"https://github-test.local/avatars/u/6?","gravatar_id":"","url":"https://github-test.local/api/v3/users/GitHub-Demo","html_url":"https://github-test.local/GitHub-Demo","followers_url":"https://github-test.local/api/v3/users/GitHub-Demo/followers","following_url":"https://github-test.local/api/v3/users/GitHub-Demo/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/GitHub-Demo/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/GitHub-Demo/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/GitHub-Demo/subscriptions","organizations_url":"https://github-test.local/api/v3/users/GitHub-Demo/orgs","repos_url":"https://github-test.local/api/v3/users/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/users/GitHub-Demo/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/GitHub-Demo/received_events","type":"Organization","site_admin":false},"private":false,"html_url":"https://github-test.local/GitHub-Demo/demo","fork":false,"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo","forks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/forks","keys_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/keys{/key_id}","collaborators_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/collaborators{/collaborator}","teams_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/teams","hooks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/hooks","issue_events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/events{/number}","events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/events","assignees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/assignees{/user}","branches_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches{/branch}","tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/tags","blobs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/blobs{/sha}","git_tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/tags{/sha}","git_refs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/refs{/sha}","trees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/trees{/sha}","statuses_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/statuses/{sha}","languages_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/languages","stargazers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/stargazers","contributors_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contributors","subscribers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscribers","subscription_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscription","commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/commits{/sha}","git_commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/commits{/sha}","comments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/comments{/number}","issue_comment_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/comments{/number}","contents_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contents/{+path}","compare_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/compare/{base}...{head}","merges_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/merges","archive_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/{archive_format}{/ref}","downloads_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/downloads","issues_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues{/number}","pulls_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/pulls{/number}","milestones_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/milestones{/number}","notifications_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/notifications{?since,all,participating}","labels_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/labels{/name}","releases_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/releases{/id}","deployments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/deployments","created_at":"2018-01-19T20:04:24Z","updated_at":"2018-01-19T20:04:24Z","pushed_at":"2018-01-19T20:04:25Z","git_url":"git://github-test.local/GitHub-Demo/demo.git","ssh_url":"git@github-test.local:GitHub-Demo/demo.git","clone_url":"https://github-test.local/GitHub-Demo/demo.git","svn_url":"https://github-test.local/GitHub-Demo/demo","size":0,"stargazers_count":0,"watchers_count":0,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"archived":false,"open_issues_count":0,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"}
    repository_owner_url = https://github-test.local/api/v3/users/GitHub-Demo
    repository_clone_url = https://github-test.local/GitHub-Demo/demo.git
    sender_subscriptions_url = https://github-test.local/api/v3/users/primetheus/subscriptions
    repository_owner_following_url = https://github-test.local/api/v3/users/GitHub-Demo/following{/other_user}
    repository_teams_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/teams
    repository_trees_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/trees{/sha}
    repository_pulls_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/pulls{/number}
    repository_name = demo
    sender_url = https://github-test.local/api/v3/users/primetheus
    repository_has_pages = false
    repository_deployments_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/deployments
    repository_labels_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/labels{/name}
    sender_login = primetheus
    repository_svn_url = https://github-test.local/GitHub-Demo/demo
    repository_merges_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/merges
    sender = {"login":"primetheus","id":3,"avatar_url":"https://github-test.local/avatars/u/3?","gravatar_id":"","url":"https://github-test.local/api/v3/users/primetheus","html_url":"https://github-test.local/primetheus","followers_url":"https://github-test.local/api/v3/users/primetheus/followers","following_url":"https://github-test.local/api/v3/users/primetheus/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/primetheus/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/primetheus/subscriptions","organizations_url":"https://github-test.local/api/v3/users/primetheus/orgs","repos_url":"https://github-test.local/api/v3/users/primetheus/repos","events_url":"https://github-test.local/api/v3/users/primetheus/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/primetheus/received_events","type":"User","site_admin":true,"ldap_dn":"CN\u003dJared Murrell,CN\u003dUsers,DC\u003dgithub-test,DC\u003dlocal"}
    repository_keys_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/keys{/key_id}
    repository_events_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/events
    repository_updated_at = 2018-01-19T20:04:24Z
    sender_ldap_dn = CN=Jared Murrell,CN=Users,DC=github-test,DC=local
    repository_releases_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/releases{/id}
    repository_default_branch = master
    repository_forks = 0
    sender_repos_url = https://github-test.local/api/v3/users/primetheus/repos
    repository_assignees_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/assignees{/user}
    repository_comments_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/comments{/number}
    repository_size = 0
    organization_issues_url = https://github-test.local/api/v3/orgs/GitHub-Demo/issues
    repository_private = false
    repository_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo
    repository_owner_site_admin = false
    sender_starred_url = https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}
    sender_organizations_url = https://github-test.local/api/v3/users/primetheus/orgs
    organization_url = https://github-test.local/api/v3/orgs/GitHub-Demo
    organization_login = GitHub-Demo
    sender_received_events_url = https://github-test.local/api/v3/users/primetheus/received_events
    repository_branches_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches{/branch}
    repository_contributors_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/contributors
    organization = {"login":"GitHub-Demo","id":6,"url":"https://github-test.local/api/v3/orgs/GitHub-Demo","repos_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/events","hooks_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/hooks","issues_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/issues","members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/members{/member}","public_members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/public_members{/member}","avatar_url":"https://github-test.local/avatars/u/6?"}
    repository_owner_html_url = https://github-test.local/GitHub-Demo
    repository_issue_events_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/events{/number}
    repository_git_url = git://github-test.local/GitHub-Demo/demo.git
    repository_owner_id = 6
    repository_has_downloads = true
    organization_avatar_url = https://github-test.local/avatars/u/6?
    repository_owner_gravatar_id =
    repository_statuses_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/statuses/{sha}
    repository_commits_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/commits{/sha}
    organization_events_url = https://github-test.local/api/v3/orgs/GitHub-Demo/events
    repository_owner_received_events_url = https://github-test.local/api/v3/users/GitHub-Demo/received_events
    repository_archive_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/{archive_format}{/ref}
    repository_owner_subscriptions_url = https://github-test.local/api/v3/users/GitHub-Demo/subscriptions
    sender_id = 3
    repository_owner_organizations_url = https://github-test.local/api/v3/users/GitHub-Demo/orgs
    repository_full_name = GitHub-Demo/demo
    repository_id = 3
    repository_issue_comment_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/comments{/number}
    repository_collaborators_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/collaborators{/collaborator}
    repository_owner_login = GitHub-Demo
    master_branch = master
    sender_site_admin = true
    repository_archived = false
    sender_html_url = https://github-test.local/primetheus
    repository_has_issues = true
    repository_forks_count = 0
    repository_created_at = 2018-01-19T20:04:24Z
    repository_stargazers_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/stargazers
    repository_compare_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/compare/{base}...{head}
    sender_gists_url = https://github-test.local/api/v3/users/primetheus/gists{/gist_id}
    repository_stargazers_count = 0
    organization_id = 6
    repository_owner_avatar_url = https://github-test.local/avatars/u/6?
    organization_hooks_url = https://github-test.local/api/v3/orgs/GitHub-Demo/hooks
    repository_owner_type = Organization
    repository_downloads_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/downloads
    repository_owner_events_url = https://github-test.local/api/v3/users/GitHub-Demo/events{/privacy}
    sender_following_url = https://github-test.local/api/v3/users/primetheus/following{/other_user}
    repository_issues_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues{/number}
    sender_avatar_url = https://github-test.local/avatars/u/3?
    repository_blobs_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/blobs{/sha}
    sender_events_url = https://github-test.local/api/v3/users/primetheus/events{/privacy}
    repository_hooks_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/hooks
    repository_subscription_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscription
    repository_watchers_count = 0
    repository_git_tags_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/tags{/sha}
    repository_open_issues_count = 0
    repository_contents_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/contents/{+path}
    repository_notifications_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/notifications{?since,all,participating}
    sender_gravatar_id =
    repository_pushed_at = 2018-01-19T20:04:25Z
    repository_git_commits_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/commits{/sha}
    repository_has_wiki = true
    repository_watchers = 0
    sender_followers_url = https://github-test.local/api/v3/users/primetheus/followers
    repository_owner_gists_url = https://github-test.local/api/v3/users/GitHub-Demo/gists{/gist_id}
    branch_name = master
    organization_public_members_url = https://github-test.local/api/v3/orgs/GitHub-Demo/public_members{/member}
    repository_git_refs_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/refs{/sha}
    repository_subscribers_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscribers
    organization_members_url = https://github-test.local/api/v3/orgs/GitHub-Demo/members{/member}
    organization_repos_url = https://github-test.local/api/v3/orgs/GitHub-Demo/repos
    sender_type = User
    repository_ssh_url = git@github-test.local:GitHub-Demo/demo.git
    repository_owner_repos_url = https://github-test.local/api/v3/users/GitHub-Demo/repos
    repository_milestones_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/milestones{/number}
    repository_fork = false
    repository_languages_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/languages
    repository_tags_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/tags
    repository_html_url = https://github-test.local/GitHub-Demo/demo
    repository_owner_followers_url = https://github-test.local/api/v3/users/GitHub-Demo/followers
    ref_type = branch
    repository_forks_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/forks
    repository_owner_starred_url = https://github-test.local/api/v3/users/GitHub-Demo/starred{/owner}{/repo}


[Pipeline] stage
GenericWebhookEnvironmentContributor Received:

{"ref":"master","ref_type":"branch","master_branch":"master","description":null,"pusher_type":"user","repository":{"id":3,"name":"demo","full_name":"GitHub-Demo/demo","owner":{"login":"GitHub-Demo","id":6,"avatar_url":"https://github-test.local/avatars/u/6?","gravatar_id":"","url":"https://github-test.local/api/v3/users/GitHub-Demo","html_url":"https://github-test.local/GitHub-Demo","followers_url":"https://github-test.local/api/v3/users/GitHub-Demo/followers","following_url":"https://github-test.local/api/v3/users/GitHub-Demo/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/GitHub-Demo/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/GitHub-Demo/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/GitHub-Demo/subscriptions","organizations_url":"https://github-test.local/api/v3/users/GitHub-Demo/orgs","repos_url":"https://github-test.local/api/v3/users/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/users/GitHub-Demo/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/GitHub-Demo/received_events","type":"Organization","site_admin":false},"private":false,"html_url":"https://github-test.local/GitHub-Demo/demo","description":null,"fork":false,"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo","forks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/forks","keys_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/keys{/key_id}","collaborators_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/collaborators{/collaborator}","teams_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/teams","hooks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/hooks","issue_events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/events{/number}","events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/events","assignees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/assignees{/user}","branches_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches{/branch}","tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/tags","blobs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/blobs{/sha}","git_tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/tags{/sha}","git_refs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/refs{/sha}","trees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/trees{/sha}","statuses_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/statuses/{sha}","languages_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/languages","stargazers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/stargazers","contributors_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contributors","subscribers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscribers","subscription_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscription","commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/commits{/sha}","git_commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/commits{/sha}","comments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/comments{/number}","issue_comment_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/comments{/number}","contents_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contents/{+path}","compare_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/compare/{base}...{head}","merges_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/merges","archive_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/{archive_format}{/ref}","downloads_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/downloads","issues_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues{/number}","pulls_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/pulls{/number}","milestones_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/milestones{/number}","notifications_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/notifications{?since,all,participating}","labels_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/labels{/name}","releases_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/releases{/id}","deployments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/deployments","created_at":"2018-01-19T20:04:24Z","updated_at":"2018-01-19T20:04:24Z","pushed_at":"2018-01-19T20:04:25Z","git_url":"git://github-test.local/GitHub-Demo/demo.git","ssh_url":"git@github-test.local:GitHub-Demo/demo.git","clone_url":"https://github-test.local/GitHub-Demo/demo.git","svn_url":"https://github-test.local/GitHub-Demo/demo","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"open_issues_count":0,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"},"organization":{"login":"GitHub-Demo","id":6,"url":"https://github-test.local/api/v3/orgs/GitHub-Demo","repos_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/events","hooks_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/hooks","issues_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/issues","members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/members{/member}","public_members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/public_members{/member}","avatar_url":"https://github-test.local/avatars/u/6?","description":null},"sender":{"login":"primetheus","id":3,"avatar_url":"https://github-test.local/avatars/u/3?","gravatar_id":"","url":"https://github-test.local/api/v3/users/primetheus","html_url":"https://github-test.local/primetheus","followers_url":"https://github-test.local/api/v3/users/primetheus/followers","following_url":"https://github-test.local/api/v3/users/primetheus/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/primetheus/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/primetheus/subscriptions","organizations_url":"https://github-test.local/api/v3/users/primetheus/orgs","repos_url":"https://github-test.local/api/v3/users/primetheus/repos","events_url":"https://github-test.local/api/v3/users/primetheus/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/primetheus/received_events","type":"User","site_admin":true,"ldap_dn":"CN=Jared Murrell,CN=Users,DC=github-test,DC=local"}}


Contributing variables:

    repository_has_projects = true
    repository_open_issues = 0
    repository = {"id":3,"name":"demo","full_name":"GitHub-Demo/demo","owner":{"login":"GitHub-Demo","id":6,"avatar_url":"https://github-test.local/avatars/u/6?","gravatar_id":"","url":"https://github-test.local/api/v3/users/GitHub-Demo","html_url":"https://github-test.local/GitHub-Demo","followers_url":"https://github-test.local/api/v3/users/GitHub-Demo/followers","following_url":"https://github-test.local/api/v3/users/GitHub-Demo/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/GitHub-Demo/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/GitHub-Demo/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/GitHub-Demo/subscriptions","organizations_url":"https://github-test.local/api/v3/users/GitHub-Demo/orgs","repos_url":"https://github-test.local/api/v3/users/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/users/GitHub-Demo/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/GitHub-Demo/received_events","type":"Organization","site_admin":false},"private":false,"html_url":"https://github-test.local/GitHub-Demo/demo","fork":false,"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo","forks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/forks","keys_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/keys{/key_id}","collaborators_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/collaborators{/collaborator}","teams_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/teams","hooks_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/hooks","issue_events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/events{/number}","events_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/events","assignees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/assignees{/user}","branches_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches{/branch}","tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/tags","blobs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/blobs{/sha}","git_tags_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/tags{/sha}","git_refs_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/refs{/sha}","trees_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/trees{/sha}","statuses_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/statuses/{sha}","languages_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/languages","stargazers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/stargazers","contributors_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contributors","subscribers_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscribers","subscription_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscription","commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/commits{/sha}","git_commits_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/commits{/sha}","comments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/comments{/number}","issue_comment_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/comments{/number}","contents_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/contents/{+path}","compare_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/compare/{base}...{head}","merges_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/merges","archive_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/{archive_format}{/ref}","downloads_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/downloads","issues_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues{/number}","pulls_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/pulls{/number}","milestones_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/milestones{/number}","notifications_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/notifications{?since,all,participating}","labels_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/labels{/name}","releases_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/releases{/id}","deployments_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/deployments","created_at":"2018-01-19T20:04:24Z","updated_at":"2018-01-19T20:04:24Z","pushed_at":"2018-01-19T20:04:25Z","git_url":"git://github-test.local/GitHub-Demo/demo.git","ssh_url":"git@github-test.local:GitHub-Demo/demo.git","clone_url":"https://github-test.local/GitHub-Demo/demo.git","svn_url":"https://github-test.local/GitHub-Demo/demo","size":0,"stargazers_count":0,"watchers_count":0,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"archived":false,"open_issues_count":0,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"}
    repository_owner_url = https://github-test.local/api/v3/users/GitHub-Demo
    repository_clone_url = https://github-test.local/GitHub-Demo/demo.git
    sender_subscriptions_url = https://github-test.local/api/v3/users/primetheus/subscriptions
    repository_owner_following_url = https://github-test.local/api/v3/users/GitHub-Demo/following{/other_user}
    repository_teams_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/teams
    repository_trees_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/trees{/sha}
    repository_pulls_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/pulls{/number}
    repository_name = demo
    sender_url = https://github-test.local/api/v3/users/primetheus
    repository_has_pages = false
    repository_deployments_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/deployments
    repository_labels_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/labels{/name}
    sender_login = primetheus
    repository_svn_url = https://github-test.local/GitHub-Demo/demo
    repository_merges_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/merges
    sender = {"login":"primetheus","id":3,"avatar_url":"https://github-test.local/avatars/u/3?","gravatar_id":"","url":"https://github-test.local/api/v3/users/primetheus","html_url":"https://github-test.local/primetheus","followers_url":"https://github-test.local/api/v3/users/primetheus/followers","following_url":"https://github-test.local/api/v3/users/primetheus/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/primetheus/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/primetheus/subscriptions","organizations_url":"https://github-test.local/api/v3/users/primetheus/orgs","repos_url":"https://github-test.local/api/v3/users/primetheus/repos","events_url":"https://github-test.local/api/v3/users/primetheus/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/primetheus/received_events","type":"User","site_admin":true,"ldap_dn":"CN\u003dJared Murrell,CN\u003dUsers,DC\u003dgithub-test,DC\u003dlocal"}
    repository_keys_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/keys{/key_id}
    repository_events_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/events
    repository_updated_at = 2018-01-19T20:04:24Z
    sender_ldap_dn = CN=Jared Murrell,CN=Users,DC=github-test,DC=local
    repository_releases_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/releases{/id}
    repository_default_branch = master
    repository_forks = 0
    sender_repos_url = https://github-test.local/api/v3/users/primetheus/repos
    repository_assignees_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/assignees{/user}
    repository_comments_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/comments{/number}
    repository_size = 0
    organization_issues_url = https://github-test.local/api/v3/orgs/GitHub-Demo/issues
    repository_private = false
    repository_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo
    repository_owner_site_admin = false
    sender_starred_url = https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}
    sender_organizations_url = https://github-test.local/api/v3/users/primetheus/orgs
    organization_url = https://github-test.local/api/v3/orgs/GitHub-Demo
    organization_login = GitHub-Demo
    sender_received_events_url = https://github-test.local/api/v3/users/primetheus/received_events
    repository_branches_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches{/branch}
    repository_contributors_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/contributors
    organization = {"login":"GitHub-Demo","id":6,"url":"https://github-test.local/api/v3/orgs/GitHub-Demo","repos_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/repos","events_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/events","hooks_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/hooks","issues_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/issues","members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/members{/member}","public_members_url":"https://github-test.local/api/v3/orgs/GitHub-Demo/public_members{/member}","avatar_url":"https://github-test.local/avatars/u/6?"}
    repository_owner_html_url = https://github-test.local/GitHub-Demo
    repository_issue_events_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/events{/number}
    repository_git_url = git://github-test.local/GitHub-Demo/demo.git
    repository_owner_id = 6
    repository_has_downloads = true
    organization_avatar_url = https://github-test.local/avatars/u/6?
    repository_owner_gravatar_id =
    repository_statuses_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/statuses/{sha}
    repository_commits_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/commits{/sha}
    organization_events_url = https://github-test.local/api/v3/orgs/GitHub-Demo/events
    repository_owner_received_events_url = https://github-test.local/api/v3/users/GitHub-Demo/received_events
    repository_archive_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/{archive_format}{/ref}
    repository_owner_subscriptions_url = https://github-test.local/api/v3/users/GitHub-Demo/subscriptions
    sender_id = 3
    repository_owner_organizations_url = https://github-test.local/api/v3/users/GitHub-Demo/orgs
    repository_full_name = GitHub-Demo/demo
    repository_id = 3
    repository_issue_comment_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues/comments{/number}
    repository_collaborators_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/collaborators{/collaborator}
    repository_owner_login = GitHub-Demo
    master_branch = master
    sender_site_admin = true
    repository_archived = false
    sender_html_url = https://github-test.local/primetheus
    repository_has_issues = true
    repository_forks_count = 0
    repository_created_at = 2018-01-19T20:04:24Z
    repository_stargazers_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/stargazers
    repository_compare_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/compare/{base}...{head}
    sender_gists_url = https://github-test.local/api/v3/users/primetheus/gists{/gist_id}
    repository_stargazers_count = 0
    organization_id = 6
    repository_owner_avatar_url = https://github-test.local/avatars/u/6?
    organization_hooks_url = https://github-test.local/api/v3/orgs/GitHub-Demo/hooks
    repository_owner_type = Organization
    repository_downloads_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/downloads
    repository_owner_events_url = https://github-test.local/api/v3/users/GitHub-Demo/events{/privacy}
    sender_following_url = https://github-test.local/api/v3/users/primetheus/following{/other_user}
    repository_issues_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/issues{/number}
    sender_avatar_url = https://github-test.local/avatars/u/3?
    repository_blobs_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/blobs{/sha}
    sender_events_url = https://github-test.local/api/v3/users/primetheus/events{/privacy}
    repository_hooks_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/hooks
    repository_subscription_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscription
    repository_watchers_count = 0
    repository_git_tags_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/tags{/sha}
    repository_open_issues_count = 0
    repository_contents_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/contents/{+path}
    repository_notifications_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/notifications{?since,all,participating}
    sender_gravatar_id =
    repository_pushed_at = 2018-01-19T20:04:25Z
    repository_git_commits_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/commits{/sha}
    repository_has_wiki = true
    repository_watchers = 0
    sender_followers_url = https://github-test.local/api/v3/users/primetheus/followers
    repository_owner_gists_url = https://github-test.local/api/v3/users/GitHub-Demo/gists{/gist_id}
    branch_name = master
    organization_public_members_url = https://github-test.local/api/v3/orgs/GitHub-Demo/public_members{/member}
    repository_git_refs_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/git/refs{/sha}
    repository_subscribers_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/subscribers
    organization_members_url = https://github-test.local/api/v3/orgs/GitHub-Demo/members{/member}
    organization_repos_url = https://github-test.local/api/v3/orgs/GitHub-Demo/repos
    sender_type = User
    repository_ssh_url = git@github-test.local:GitHub-Demo/demo.git
    repository_owner_repos_url = https://github-test.local/api/v3/users/GitHub-Demo/repos
    repository_milestones_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/milestones{/number}
    repository_fork = false
    repository_languages_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/languages
    repository_tags_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/tags
    repository_html_url = https://github-test.local/GitHub-Demo/demo
    repository_owner_followers_url = https://github-test.local/api/v3/users/GitHub-Demo/followers
    ref_type = branch
    repository_forks_url = https://github-test.local/api/v3/repos/GitHub-Demo/demo/forks
    repository_owner_starred_url = https://github-test.local/api/v3/users/GitHub-Demo/starred{/owner}{/repo}


[Pipeline] { (Protect Master Branch)
[Pipeline] withCredentials
[Pipeline] {
[Pipeline] httpRequest
HttpMethod: PUT
URL: https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection
Content-type: application/json
Authorization: *****
Accept: application/vnd.github.loki-preview
Sending request to url: https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection
Response Code: HTTP/1.1 200 OK
Response:
{"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection","required_status_checks":{"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/required_status_checks","strict":true,"contexts":["continuous-integration/jenkins/branch"],"contexts_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/required_status_checks/contexts"},"restrictions":{"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/restrictions","users_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/restrictions/users","teams_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/restrictions/teams","users":[{"login":"primetheus","id":3,"avatar_url":"https://github-test.local/avatars/u/3?","gravatar_id":"","url":"https://github-test.local/api/v3/users/primetheus","html_url":"https://github-test.local/primetheus","followers_url":"https://github-test.local/api/v3/users/primetheus/followers","following_url":"https://github-test.local/api/v3/users/primetheus/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/primetheus/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/primetheus/subscriptions","organizations_url":"https://github-test.local/api/v3/users/primetheus/orgs","repos_url":"https://github-test.local/api/v3/users/primetheus/repos","events_url":"https://github-test.local/api/v3/users/primetheus/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/primetheus/received_events","type":"User","site_admin":true,"ldap_dn":"CN=Jared Murrell,CN=Users,DC=github-test,DC=local"}],"teams":[]},"required_pull_request_reviews":{"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/required_pull_request_reviews","dismiss_stale_reviews":true,"require_code_owner_reviews":true,"dismissal_restrictions":{"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/dismissal_restrictions","users_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/dismissal_restrictions/users","teams_url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/dismissal_restrictions/teams","users":[{"login":"primetheus","id":3,"avatar_url":"https://github-test.local/avatars/u/3?","gravatar_id":"","url":"https://github-test.local/api/v3/users/primetheus","html_url":"https://github-test.local/primetheus","followers_url":"https://github-test.local/api/v3/users/primetheus/followers","following_url":"https://github-test.local/api/v3/users/primetheus/following{/other_user}","gists_url":"https://github-test.local/api/v3/users/primetheus/gists{/gist_id}","starred_url":"https://github-test.local/api/v3/users/primetheus/starred{/owner}{/repo}","subscriptions_url":"https://github-test.local/api/v3/users/primetheus/subscriptions","organizations_url":"https://github-test.local/api/v3/users/primetheus/orgs","repos_url":"https://github-test.local/api/v3/users/primetheus/repos","events_url":"https://github-test.local/api/v3/users/primetheus/events{/privacy}","received_events_url":"https://github-test.local/api/v3/users/primetheus/received_events","type":"User","site_admin":true,"ldap_dn":"CN=Jared Murrell,CN=Users,DC=github-test,DC=local"}],"teams":[]}},"enforce_admins":{"url":"https://github-test.local/api/v3/repos/GitHub-Demo/demo/branches/master/protection/enforce_admins","enabled":true}}
Success code from [100‥399]
[Pipeline] }
[Pipeline] // withCredentials
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```

</details>

Notice in the sample output above, the received payload is in `JSON` format, but when Jenkins processes the data it is flattened and referenced as **_Contributing Variables_**. You will find a long list of `repository_<field>` items in the data, which is the **Generic Webhook** plugin's method of mapping the keys that we specified in [our table earlier](#processing-the-webhook). If there are other keys in the `JSON` payload we receive that we want to process, simply map them in the same manner.

To verify the protection in GitHub, navigate to the repository in GitHub.

1. Click on _Settings_
2. Click on _Branches_

Notice that we already have protection on the `master` branch.

![branch protection settings](https://user-images.githubusercontent.com/865381/39252741-5022b6d0-4874-11e8-969f-1db4b4ec35cf.gif)

3. Click on _Edit_ to see the individual protection settings configured

![individual branch protection settings](https://user-images.githubusercontent.com/865381/39252951-c447c4d8-4874-11e8-99f8-6095216912da.gif)

## Conclusion
This wraps up our example. This article will hopefully empower you to automate many more tasks for your teams and company as you explore the capabilities of GitHub and Jenkins together!
# Dismiss Review Server

A ruby server that listens for GitHub webhook `push` events, based on [the documentation](https://developer.github.com/webhooks/configuring/#writing-the-server), that will dismiss any `APPROVED` [Pull Request Reviews](https://help.github.com/articles/about-pull-request-reviews/).

## Configuration

Follow the [instructions](https://developer.github.com/webhooks/) of setting up a Webhook on GitHub to this server. Set the following environment variables:
- GITHUB_API_TOKEN - (Required) [OAuth token](https://developer.github.com/v3/#authentication) with write access to the repository.
- SECRET_TOKEN - (Optional) [Shared secret token](https://developer.github.com/webhooks/securing/#validating-payloads-from-github) between the GitHub Webhook and this application. Leave this unset if not using a secret token.
# :x: Delete Repository Event

### :dart: Purpose

This Ruby server:

1. Listens for when a [repository is deleted](https://help.github.com/enterprise/user/articles/deleting-a-repository/) using the [`repository`](https://developer.github.com/enterprise/v3/activity/events/types/#repositoryevent) event and `deleted` action.

2. Creates an issue in `GITHUB_NOTIFICATION_REPOSITORY` as a notification and includes: 

    - a link to restore the repository
    - the delete repository payload

### :gear: Configuration

1. See the [webhooks](https://developer.github.com/webhooks/) documentation for information on how to [create webhooks](https://developer.github.com/webhooks/creating/) and [configure your server](https://developer.github.com/webhooks/configuring/).

2. Set the following required environment variables:

    - `GITHUB_HOST` - the domain of the GitHub Enterprise instance. e.g. github.example.com
    - `GITHUB_API_TOKEN` - a [Personal Access Token](https://help.github.com/enterprise/user/articles/creating-a-personal-access-token-for-the-command-line/) that has the ability to create an issue in the notification repository
    - `GITHUB_NOTIFICATION_REPOSITORY` - the repository in which to create the nofication issue. e.g. github.example.com/administrative-notifications
GitHub webhooks test
====================
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This is a simple WSGI application written in Flask to allow you to register and run your own Git hooks. Python is a
favorite programming language of many, so this might be familiar to work with.


Install
=======
```bash
    git clone https://github.com/github/platform-samples.git
    cd platform-samples/hooks/python/flask-github-webhooks
```

Dependencies
============
There are a few dependencies to install before this can run
* Flask
* ipaddress
* requests
* pyOpenSSL==16.2.0 (required if you have issues with SSL libraries and the GitHub API)
```bash
   sudo pip install -r requirements.txt
```

Setup
=====

You can configure what the application does by copying the sample config file
``config.json.sample`` to ``config.json`` and adapting it to your needs:

```json
{
    "github_ips_only": true,
    "enforce_secret": "",
    "return_scripts_info": true,
    "hooks_path": "/<other>/<path>/<to>/hooks/"
}
```

| Setting | Description |
|---------|-------------|
| github_ips_only | Restrict application to be called only by GitHub IPs. IPs whitelist is obtained from [GitHub Meta](https://developer.github.com/v3/meta/) ([endpoint](https://api.github.com/meta)). _Default_: ``true``. |
| enforce_secret | Enforce body signature with HTTP header ``X-Hub-Signature``. See ``secret`` at [GitHub WebHooks Documentation](https://developer.github.com/v3/repos/hooks/). _Default_: ``''`` (do not enforce). |
| return_scripts_info | Return a JSON with the ``stdout``, ``stderr`` and exit code for each executed hook using the hook name as key. If this option is set you will be able to see the result of your hooks from within your GitHub hooks configuration page (see "Recent Deliveries"). _*Default*_: ``true``. |
| hooks_path | Configures a path to import the hooks. If not set, it'll import the hooks from the default location (/.../python-github-webhooks/hooks) |


Adding hooks
============

This application uses the following precedence for executing hooks:

```bash
    hooks/{event}-{reponame}-{branch}
    hooks/{event}-{reponame}
    hooks/{event}
    hooks/all
```
Hooks are passed to the path to a JSON file holding the
payload for the request as first argument. The event type will be passed
as second argument. For example:

```
    hooks/reposotory-mygithubrepo-master /tmp/ksAHXk8 push
```

Webhooks can be written in any language. Simply add a ``shebang`` and enable the execute bit (_chmod 755_)
The following example is a Python webhook receiver that will create an issue when a repository in an organization is deleted:

```python
#!/usr/bin/env python

import sys
import json
import requests

# Authentication for the user who is filing the issue. Username/API_KEY
USERNAME = '<api_username>'
API_KEY = '<github-api-key>'

# The repository to add this issue to
REPO_OWNER = '<repository-owner>'
REPO_NAME = '<repository-name>'


def create_github_issue(title, body=None, labels=None):
    """
    Create an issue on github.com using the given parameters.
    :param title: This is the title of the GitHub Issue
    :param body: Optional - This is the body of the issue, or the main text
    :param labels: Optional - What type of issue are we creating
    :return:
    """
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, API_KEY)
    # Create the issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print 'Successfully created Issue "%s"' % title
    else:
        print 'Failed to create Issue "%s"' % title
        print 'Response:', r.content


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as jsp:
        payload = json.loads(jsp.read())
    # What was done to the repo
    action = payload['action']
    # What is the repo name
    repo = payload['repository']['full_name']
    # Create an issue if the repository was deleted
    if action == 'deleted':
        create_github_issue('%s was deleted' % repo, 'Seems we\'ve got ourselves a bit of an issue here.\n\n@<repository-owner>',
                            ['deleted'])
    # Log the payload to a file
    outfile = '/tmp/webhook-{}.log'.format(repo)
    with open(outfile, 'w') as f:
        f.write(json.dumps(payload))
```

Not all events have an associated branch, so a branch-specific hook cannot
fire for such events. For events that contain a pull_request object, the
base branch (target for the pull request) is used, not the head branch.

The payload structure depends on the event type. Please review:

    https://developer.github.com/v3/activity/events/types/


Deploy
======

Apache
------

To deploy in Apache, just add a ``WSGIScriptAlias`` directive to your
VirtualHost file:

```bash
<VirtualHost *:80>
    ServerAdmin you@my.site.com
    ServerName  my.site.com
    DocumentRoot /var/www/site.com/my/htdocs/

    # Handle Github webhook
    <Directory "/var/www/site.com/my/flask-github-webhooks">
        Order deny,allow
        Allow from all
    </Directory>
    WSGIScriptAlias /webhooks /var/www/site.com/my/flas-github-webhooks/webhooks.py
</VirtualHost>
```
You can now register the hook in your Github repository settings:

    https://github.com/youruser/myrepo/settings/hooks

To register the webhook select Content type: ``application/json`` and set the URL to the URL
of your WSGI script:

   http://my.site.com/webhooks

Docker
------

To deploy in a Docker container you have to expose the port 5000, for example
with the following command:

```bash
git clone https://github.com/github/platform-samples.git
docker build -t flask-github-webhooks platform-samples/hooks/python/flask-github-webhooks
docker run -ditp 5000:5000 --restart=unless-stopped --name webhooks flask-github-webhooks
```
You can also mount volume to setup the ``hooks/`` directory, and the file
``config.json``:

```bash
docker run -ditp 5000:5000 --name webhooks \
      --restart=unless-stopped \
      -v /path/to/my/hooks:/app/hooks \
      -v /path/to/my/config.json:/app/config.json \
      flask-github-webhooks
```

Test your deployment
====================

To test your hook you may use the GitHub REST API with ``curl``:

    https://developer.github.com/v3/

```bash
curl --user "<youruser>" https://api.github.com/repos/<youruser>/<myrepo>/hooks
```
Take note of the test_url.

```bash
curl --user "<youruser>" -i -X POST <test_url>
```
You should be able to see any log error in your web app.


Debug
=====

When running in Apache, the ``stderr`` of the hooks that return non-zero will
be logged in Apache's error logs. For example:

```bash
sudo tail -f /var/log/apache2/error.log
```
Will log errors in your scripts if printed to ``stderr``.

You can also launch the Flask web server in debug mode at port ``5000``.

```bash
python webhooks.py
```
This can help debug problem with the WSGI application itself.


Credits
=======

This project is just the reinterpretation and merge of two approaches and a modification of Carlos Jenkins' work:

- [github-webhook-wrapper](https://github.com/datafolklabs/github-webhook-wrapper)
- [flask-github-webhook](https://github.com/razius/flask-github-webhook)
- [python-github-webhooks](https://github.com/carlos-jenkins/python-github-webhooks)
## Pre-receive hooks

### tl;dr

This directory contains examples for [pre-receive hooks ](https://help.github.com/enterprise/user/articles/working-with-pre-receive-hooks/) which are a [GitHub Enterprise feature](https://developer.github.com/v3/enterprise/pre_receive_hooks/) to block unwanted commits before they even reach your repository.

If you have a great example for a pre-receive hook you used with GitHub Enterprise that is not yet part of this directory, create a pull request and we will happily review it.

While blocking commits at push time using pre-receive-hooks seems like an awesome idea, there are many cases where other approaches work much better for your developers, check out the rest of this README for more info.

### Pre-receive hooks - The longer story

As of GitHub Enterprise 2.6 we [support pre-receive hooks](https://help.github.com/enterprise/user/articles/working-with-pre-receive-hooks/). [Pre-receive hooks](https://help.github.com/enterprise/user/articles/working-with-pre-receive-hooks/) run tests on code pushed to a repository to ensure contributions meet repository or organization policy. If the commits pass the tests, the push will be accepted into the repository. If the commits do not pass the tests, the push will not be accepted.

Your GitHub Enterprise site administrator can [create and remove pre-receive hooks](https://help.github.com/enterprise/admin/guides/developer-workflow/managing-pre-receive-hooks-on-the-github-enterprise-appliance/) for your organization or repository, and may allow organization or repository administrators to enable or disable pre-receive hooks. GitHub Enterprise allows you to [develop and test](https://help.github.com/enterprise/admin/guides/developer-workflow/creating-a-pre-receive-hook-script/) all scripts locally in a [pre-receive hook environment](https://help.github.com/enterprise/2.6/admin/guides/developer-workflow/creating-a-pre-receive-hook-environment/).

Examples of pre-receive hooks:
* Require commit messages to follow a specific pattern or format, such as including a valid ticket number or being over a certain length.
* Prevent sensitive data from being added to the repository by blocking keywords, patterns or filetypes.
* Prevent a PR author from merging their own changes.
* Prevent a developer from pushing commits of a different author or committer.
* Prevent a developer from pushing unsigned commits.

You can find examples on how to write pre-receive hooks on the [Pro Git website](https://git-scm.com/book/en/v2/Customizing-Git-An-Example-Git-Enforced-Policy) and within this directory.

### Think twice before you deploy a pre-receive hook

GitHub recommends a cautious and thoughtful approach when applying mechanisms like pre-receive hooks that can block Git push operations. Blocking pushes right away typically prevents contribution and visibility into proposed changes. We think it's best that individuals collaborate with each other to identify and fix any problems after changes have been proposed. Even some of our largest customers have found that a subtle shift to [non-blocking web-hooks](https://help.github.com/enterprise/admin/guides/developer-workflow/using-webhooks-for-continuous-integration/) allowed more individuals to contribute and provided more opportunities for learning and collaboration. Combined with asynchronous collaboration workflows like [GitHubFlow](https://guides.github.com/introduction/flow/), non-blocking web-hooks typically resulted in higher-quality output.

That said, we understand there may be compliance or other organizational reasons to incorporate pre-receive hooks into a development workflow, e.g. ensuring that sensitive information is not included as part of pushed commits.

### Performance, stability and workflow implications of pre-receive hooks

Pre-receive hooks can have unintended effects on the performance of the GitHub Enterprise appliance and should be carefully [implemented and reviewed](https://help.github.com/enterprise/admin/guides/developer-workflow/creating-a-pre-receive-hook-script/). A misconfigured pre-receive hook may block all developers from contributing/pushing to a repository or consume all system resources on the appliance.

Running scripts will be automatically terminated after 5 seconds (blocking the push). Consequently, pre-receive hooks should not rely on the results of external systems that may not be always available or on any other potentially blocking resource. As any negative exit code of a pre-receive hook will reject the associated push attempt, your scripts should handle unforeseen standard input and environment variable values in a robust way.

When designing your scripts, also consider scenarios where many developers push at once (e.g. before lunch time). Parallel pushes will result in parallel runs of hook scripts. All parallel script runs have to compete for the same resources: CPU, memory, files, network, external systems. If any of the parallel runs needed more than 5 seconds to complete or triggered a programming error ([race condition](https://en.wikipedia.org/wiki/Race_condition#Software)), this may result in an unhappy developer whose push just got rejected for the wrong reasons.

**Any acceptable approach that can enforce your policy in an asynchronous fashion (see following paragraphs), will have less risk on the performance of your appliance and the effectiveness of your developer workflow.**

### Alternatives to pre-receive-hooks

Depending on your particular use case, you might be able to achieve your goals using [Protected Branches and Required Status checks](https://github.com/blog/2051-protected-branches-and-required-status-checks). Starting GitHub Enterprise 2.4, you can use Protected Branches to ensure that collaborators on your repository cannot make irrevocable changes to branches. If you [configure a branch as protected](https://help.github.com/articles/configuring-protected-branches/) it:

 - Can't be force pushed
 - Can't be deleted

If you also enable [Required Status](https://help.github.com/articles/enabling-required-status-checks/) on a protected branch, all required checks must succeed before team members are able to merge a Pull Request. Using our [Status API](https://developer.github.com/v3/repos/statuses/) you are able to define which checks (required or optional) should be triggered upon a Pull Request submission.

Instead of preventing the code from being committed you can also prevent it from being deployed. To do this, you can configure your deployment process to be triggered by the Pull Request merge event. Using the information that [GitHub's webhooks](https://developer.github.com/webhooks/) provide, you'll be able to determine whether the Pull Request meets the review and CI requirements. If it does not, you can reject the deployment and post the failure information back to the Pull Request. You can learn more about delivering deployments at https://developer.github.com/guides/delivering-deployments/.

Instead of putting controls in place that technically enforce your policy, you can also socially enforce it. Let's say your policy prescribes that pull requests should not be merged by the author of the pull request. You can build a culture within the company which makes merging your own Pull Request unacceptable behavior. To do this, you will need to be notified when someone merges their own Pull Request so that you can revert it and educate them on why having independent review is important. You can write a simple script, and attach it to a [webhook](https://developer.github.com/webhooks/), that looks for Pull Requests that were merged by the author. When this happens you can either post a comment in the Pull Request pinging a compliance team or send an email to a mailing list reporting the transgression. Once a developer has had their Pull Request reverted, they will be unlikely to make the same mistake again. This model places trust in the developers but still allows a certain degree of control and audibility. The power of Git makes undoing any unreviewed changes easy.

Worth noting if you haven't already considered it, you can set up a similar mechanism on your team members' local machines using a pre-commit hook which could certainly be faster than a server-side implementation: http://git-scm.com/book/en/Customizing-Git-Git-Hooks#Client-Side-Hooks
