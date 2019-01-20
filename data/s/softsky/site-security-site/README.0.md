# Validator, for Bootstrap 3
The Validator plugin offers automatic form validation configurable via mostly HTML5 standard attributes.
It also provides an unobtrusive user experience, because nobody likes a naggy form.

## Features
- Configurable via data-api and standard HTML5 attributes
- Patient to inform user of errors and eager to let them know the errors have been resolved
- Submit is disabled until the form is valid and all required fields are complete
- Customizable error messages
- Custom validator functions
- Validation of an input field via AJAX

## Installation
* CDN on [CDNJS](https://cdnjs.com): https://cdnjs.com/libraries/1000hz-bootstrap-validator
* Clone the repo: `git clone https://github.com/1000hz/bootstrap-validator.git`.
* Install with [Bower](http://bower.io): `bower install bootstrap-validator`.
* Install with [npm](https://www.npmjs.com): `npm install bootstrap-validator`.

## Documentation

See the project docs at http://1000hz.github.io/bootstrap-validator

## Contributing
#### Found an issue?
Be sure to include a reproducible test case on JS Bin with your report. Here's a [template](http://jsbin.com/fopaposaci/1/edit?html,js,output) to get started.
#### Submitting a pull request?
Fork this repo and create a new branch for your patch.
Try to adhere to the code style of Bootstrap 3's JS as much as possible.
Be sure to add any relevant unit tests.
Make sure everything's still ok by running `grunt test`.
Lastly, don't pollute your patch branch with any unrelated changes.

## Donating
If you've found this project particularly useful and feel like giving a little back, you can donate what you want via PayPal or Square Cash.

<a href="https://paypal.me/1000hz"><img src="https://img.shields.io/badge/Donate-PayPal-blue.svg" alt="Donate via PayPal"></a>
<a href="https://cash.me/$cina"><img src="https://img.shields.io/badge/Donate-Square Cash-brightgreen.svg" alt="Donate via Square Cash"></a>


## Author

**Cina Saffary**
- http://twitter.com/1000hz
- http://github.com/1000hz

Thanks to  [@mdo](https://github.com/mdo) and [@fat](https://github.com/fat) for [Bootstrap](http://getbootstrap.com). <3

## Copyright and license
Copyright 2016 Cina Saffary under the MIT license.
# [Bootstrap](http://getbootstrap.com)
[![Bower version](https://badge.fury.io/bo/bootstrap.svg)](http://badge.fury.io/bo/bootstrap)
[![NPM version](https://badge.fury.io/js/bootstrap.svg)](http://badge.fury.io/js/bootstrap)
[![Build Status](https://secure.travis-ci.org/twbs/bootstrap.svg?branch=master)](https://travis-ci.org/twbs/bootstrap)
[![devDependency Status](https://david-dm.org/twbs/bootstrap/dev-status.svg)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat), and maintained by the [core team](https://github.com/twbs?tab=members) with the massive support and involvement of the community.

To get started, check out <http://getbootstrap.com>!

## Table of contents

- [Quick start](#quick-start)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Quick start

Four quick start options are available:

- [Download the latest release](https://github.com/twbs/bootstrap/archive/v3.3.1.zip).
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
- Install with [Bower](http://bower.io): `bower install bootstrap`.
- Install with [npm](https://www.npmjs.org): `npm install bootstrap`.

Read the [Getting started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.min.css
│   ├── bootstrap-theme.css
│   └── bootstrap-theme.min.css
├── js/
│   ├── bootstrap.js
│   └── bootstrap.min.js
└── fonts/
    ├── glyphicons-halflings-regular.eot
    ├── glyphicons-halflings-regular.svg
    ├── glyphicons-halflings-regular.ttf
    └── glyphicons-halflings-regular.woff
```

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). Fonts from Glyphicons are included, as is the optional Bootstrap theme.



## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](http://jekyllrb.com) and publicly hosted on GitHub Pages at <http://getbootstrap.com>. The docs may also be run locally.

### Running documentation locally

1. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) (requires v2.5.x).
  - **Windows users:** Read [this unofficial guide](http://jekyll-windows.juthilo.com/) to get Jekyll up and running without problems.
2. Install the Ruby-based syntax highlighter, [Rouge](https://github.com/jneen/rouge), with `gem install rouge`.
3. From the root `/bootstrap` directory, run `jekyll serve` in the command line.
4. Open <http://localhost:9001> in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.



## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include relevant unit tests. All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.



## Community

Keep track of development and community news.

- Follow [@twbootstrap on Twitter](https://twitter.com/twbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`twitter-bootstrap-3`](http://stackoverflow.com/questions/tagged/twitter-bootstrap-3)).



## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.



## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>



## Copyright and license

Code and documentation copyright 2011-2014 Twitter, Inc. Code released under [the MIT license](LICENSE). Docs released under [Creative Commons](docs/LICENSE).
## What does `s3_cache.py` do?

### In general
`s3_cache.py` maintains a cache, stored in an Amazon S3 (Simple Storage Service) bucket, of a given directory whose contents are considered non-critical and are completely & solely determined by (and should be able to be regenerated from) a single given file.

The SHA-256 hash of the single file is used as the key for the cache. The directory is stored as a gzipped tarball.

All the tarballs are stored in S3's Reduced Redundancy Storage (RRS) storage class, since this is cheaper and the data is non-critical.

`s3_cache.py` itself never deletes cache entries; deletion should either be done manually or using automatic S3 lifecycle rules on the bucket.

Similar to git, `s3_cache.py` makes the assumption that [SHA-256 will effectively never have a collision](http://stackoverflow.com/questions/4014090/is-it-safe-to-ignore-the-possibility-of-sha-collisions-in-practice).


### For Bootstrap specifically
`s3_cache.py` is used to cache the npm packages that our Grunt tasks depend on and the RubyGems that Jekyll depends on. (Jekyll is needed to compile our docs to HTML so that we can run them thru an HTML5 validator.)

For npm, the `node_modules` directory is cached based on our `npm-shrinkwrap.json` file.

For RubyGems, the `gemdir` of the current RVM-selected Ruby is cached based on the `pseudo_Gemfile.lock` file generated by our Travis build script.
`pseudo_Gemfile.lock` contains the versions of Ruby and Jekyll that we're using (read our `.travis.yml` for details).


## Why is `s3_cache.py` necessary?
`s3_cache.py` is used to speed up Bootstrap's Travis builds. Installing npm packages and RubyGems used to take up a significant fraction of our total build times. Also, at the time that `s3_cache.py` was written, npm was occasionally unreliable.

Travis does offer built-in caching on their paid plans, but this do-it-ourselves S3 solution is significantly cheaper since we only need caching and not Travis' other paid features.


## Configuration
`s3_cache.py` is configured via `S3Cachefile.json`, which has the following format:
```json
{
    "cache-name-here": {
        "key": "path/to/file/to/SHA-256/hash/and/use/that/as/the/cache.key",
        "cache": "path/to/directory/to/be/cached",
        "generate": "shell-command --to run --to regenerate --the-cache $from scratch"
    },
    ...
}
```

`s3_cache.py` will SHA-256 hash the contents of the `key` file and try to fetch a tarball from S3 using the hash as the filename.
If it's unable to fetch the tarball (either because it doesn't exist or there was a network error), it will run the `generate` command. If it was able to fetch the tarball, it will extract it to the `cache` directory.
If it had to `generate` the cache, it will later create a tarball of the `cache` directory and try to upload the tarball to S3 using the SHA-256 hash of the `key` file as the tarball's filename.


## AWS Setup

### Overview
1. Create an Amazon Web Services (AWS) account.
2. Create an Identity & Access Management (IAM) user, and note their credentials.
3. Create an S3 bucket.
4. Set permissions on the bucket to grant the user read+write access.
5. Set the user credentials as secure Travis environment variables.

### In detail
1. Create an AWS account.
2. Login to the [AWS Management Console](https://console.aws.amazon.com).
3. Go to the IAM Management Console.
4. Create a new user (named e.g. `travis-ci`) and generate an access key for them. Note both the Access Key ID and the Secret Access Key.
5. Note the user's ARN (Amazon Resource Name), which can be found in the "Summary" tab of the user browser. This will be of the form: `arn:aws:iam::XXXXXXXXXXXXXX:user/the-username-goes-here`
6. Note the user's access key, which can be found in the "Security Credentials" tab of the user browser.
7. Go to the S3 Management Console.
8. Create a new bucket. For a non-publicly-accessible bucket (like Bootstrap uses), it's recommended that the bucket name be random to increase security. On most *nix machines, you can easily generate a random UUID to use as the bucket name using Python:

    ```bash
    python -c "import uuid; print(uuid.uuid4())"
    ```

9. Determine and note what your bucket's ARN is. The ARN for an S3 bucket is of the form: `arn:aws:s3:::the-bucket-name-goes-here`
10. In the bucket's Properties pane, in the "Permissions" section, click the "Edit bucket policy" button.
11. Input and submit an IAM Policy that grants the user at least read+write rights to the bucket. AWS has a policy generator and some examples to help with crafting the policy. Here's the policy that Bootstrap uses, with the sensitive bits censored:

    ```json
    {
        "Version": "2012-10-17",
        "Id": "PolicyTravisReadWriteNoAdmin",
        "Statement": [
            {
                "Sid": "StmtXXXXXXXXXXXXXX",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::XXXXXXXXXXXXXX:user/travis-ci"
                },
                "Action": [
                    "s3:AbortMultipartUpload",
                    "s3:GetObjectVersion",
                    "s3:ListBucket",
                    "s3:DeleteObject",
                    "s3:DeleteObjectVersion",
                    "s3:GetObject",
                    "s3:PutObject"
                ],
                "Resource": [
                    "arn:aws:s3:::XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                    "arn:aws:s3:::XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/*"
                ]
            }
        ]
    }
    ```

12. If you want deletion from the cache to be done automatically based on age (like Bootstrap does): In the bucket's Properties pane, in the "Lifecycle" section, add a rule to expire/delete files based on creation date.
13. Install the [`travis` RubyGem](https://github.com/travis-ci/travis): `gem install travis`
14. Encrypt the environment variables:

    ```bash
    travis encrypt --repo twbs/bootstrap "AWS_ACCESS_KEY_ID=XXX"
    travis encrypt --repo twbs/bootstrap "AWS_SECRET_ACCESS_KEY=XXX"
    travis encrypt --repo twbs/bootstrap "TWBS_S3_BUCKET=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
    ```

14. Add the resulting secure environment variables to `.travis.yml`.


## Usage
Read `s3_cache.py`'s source code and Bootstrap's `.travis.yml` for how to invoke and make use of `s3_cache.py`.
# [Bootstrap](http://getbootstrap.com)

[![Slack](https://bootstrap-slack.herokuapp.com/badge.svg)](https://bootstrap-slack.herokuapp.com)
![Bower version](https://img.shields.io/bower/v/bootstrap.svg)
[![npm version](https://img.shields.io/npm/v/bootstrap.svg)](https://www.npmjs.com/package/bootstrap)
[![Build Status](https://img.shields.io/travis/twbs/bootstrap/master.svg)](https://travis-ci.org/twbs/bootstrap)
[![devDependency Status](https://img.shields.io/david/dev/twbs/bootstrap.svg)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![NuGet](https://img.shields.io/nuget/v/bootstrap.svg)](https://www.nuget.org/packages/Bootstrap)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat), and maintained by the [core team](https://github.com/orgs/twbs/people) with the massive support and involvement of the community.

To get started, check out <http://getbootstrap.com>!


## Table of contents

* [Quick start](#quick-start)
* [Bugs and feature requests](#bugs-and-feature-requests)
* [Documentation](#documentation)
* [Contributing](#contributing)
* [Community](#community)
* [Versioning](#versioning)
* [Creators](#creators)
* [Copyright and license](#copyright-and-license)


## Quick start

Several quick start options are available:

* [Download the latest release](https://github.com/twbs/bootstrap/archive/v3.3.7.zip).
* Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
* Install with [Bower](http://bower.io): `bower install bootstrap`.
* Install with [npm](https://www.npmjs.com): `npm install bootstrap@3`.
* Install with [Meteor](https://www.meteor.com): `meteor add twbs:bootstrap`.
* Install with [Composer](https://getcomposer.org): `composer require twbs/bootstrap`.

Read the [Getting started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   ├── bootstrap-theme.min.css
│   └── bootstrap-theme.min.css.map
├── js/
│   ├── bootstrap.js
│   └── bootstrap.min.js
└── fonts/
    ├── glyphicons-halflings-regular.eot
    ├── glyphicons-halflings-regular.svg
    ├── glyphicons-halflings-regular.ttf
    ├── glyphicons-halflings-regular.woff
    └── glyphicons-halflings-regular.woff2
```

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). CSS [source maps](https://developer.chrome.com/devtools/docs/css-preprocessors) (`bootstrap.*.map`) are available for use with certain browsers' developer tools. Fonts from Glyphicons are included, as is the optional Bootstrap theme.


## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).

Note that **feature requests must target [Bootstrap v4](https://github.com/twbs/bootstrap/tree/v4-dev),** because Bootstrap v3 is now in maintenance mode and is closed off to new features. This is so that we can focus our efforts on Bootstrap v4.


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](http://jekyllrb.com) and publicly hosted on GitHub Pages at <http://getbootstrap.com>. The docs may also be run locally.

### Running documentation locally

1. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) and other Ruby dependencies with `bundle install`.
   **Note for Windows users:** Read [this unofficial guide](http://jekyll-windows.juthilo.com/) to get Jekyll up and running without problems.
2. From the root `/bootstrap` directory, run `bundle exec jekyll serve` in the command line.
4. Open `http://localhost:9001` in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.


## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include [relevant unit tests](https://github.com/twbs/bootstrap/tree/master/js/tests). All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

**Bootstrap v3 is now closed off to new features.** It has gone into maintenance mode so that we can focus our efforts on [Bootstrap v4](https://github.com/twbs/bootstrap/tree/v4-dev), the future of the framework. Pull requests which add new features (rather than fix bugs) should target [Bootstrap v4 (the `v4-dev` git branch)](https://github.com/twbs/bootstrap/tree/v4-dev) instead.

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.


## Community

Get updates on Bootstrap's development and chat with the project maintainers and community members.

* Follow [@getbootstrap on Twitter](https://twitter.com/getbootstrap).
* Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
* Join [the official Slack room](https://bootstrap-slack.herokuapp.com).
* Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
* Implementation help may be found at Stack Overflow (tagged [`twitter-bootstrap-3`](https://stackoverflow.com/questions/tagged/twitter-bootstrap-3)).
* Developers should use the keyword `bootstrap` on packages which modify or add to the functionality of Bootstrap when distributing through [npm](https://www.npmjs.com/browse/keyword/bootstrap) or similar delivery mechanisms for maximum discoverability.


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.

See [the Releases section of our GitHub project](https://github.com/twbs/bootstrap/releases) for changelogs for each release version of Bootstrap. Release announcement posts on [the official Bootstrap blog](http://blog.getbootstrap.com) contain summaries of the most noteworthy changes made in each release.


## Creators

**Mark Otto**

* <https://twitter.com/mdo>
* <https://github.com/mdo>

**Jacob Thornton**

* <https://twitter.com/fat>
* <https://github.com/fat>


## Copyright and license

Code and documentation copyright 2011-2016 Twitter, Inc. Code released under [the MIT license](https://github.com/twbs/bootstrap/blob/master/LICENSE). Docs released under [Creative Commons](https://github.com/twbs/bootstrap/blob/master/docs/LICENSE).
# jQuery

> jQuery is a fast, small, and feature-rich JavaScript library.

For information on how to get started and how to use jQuery, please see [jQuery's documentation](http://api.jquery.com/).
For source files and issues, please visit the [jQuery repo](https://github.com/jquery/jquery).

## Including jQuery

Below are some of the most common ways to include jQuery.

### Browser

#### Script tag

```html
<script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
```

#### Babel

[Babel](http://babeljs.io/) is a next generation JavaScript compiler. One of the features is the ability to use ES6/ES2015 modules now, even though browsers do not yet support this feature natively.

```js
import $ from "jquery";
```

#### Browserify/Webpack

There are several ways to use [Browserify](http://browserify.org/) and [Webpack](https://webpack.github.io/). For more information on using these tools, please refer to the corresponding project's documention. In the script, including jQuery will usually look like this...

```js
var $ = require("jquery");
```

#### AMD (Asynchronous Module Definition)

AMD is a module format built for the browser. For more information, we recommend [require.js' documentation](http://requirejs.org/docs/whyamd.html).

```js
define(["jquery"], function($) {

});
```

### Node

To include jQuery in [Node](nodejs.org), first install with npm.

```sh
npm install jquery
```

For jQuery to work in Node, a window with a document is required. Since no such window exists natively in Node, one can be mocked by tools such as [jsdom](https://github.com/tmpvar/jsdom). This can be useful for testing purposes.

```js
require("jsdom").env("", function(err, window) {
	if (err) {
		console.error(err);
		return;
	}

	var $ = require("jquery")(window);
});
```
