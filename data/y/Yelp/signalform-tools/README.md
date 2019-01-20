# signalform-tools

[![GitHub version](https://badge.fury.io/gh/Yelp%2Fsignalform-tools.svg)](https://badge.fury.io/gh/Yelp%2Fsignalform-tools)
[![Build Status](https://travis-ci.org/Yelp/signalform-tools.svg?branch=master)](https://travis-ci.org/Yelp/signalform-tools)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

signalform-tools is a collection of tools for working with [terraform-provider-signalform](https://github.com/Yelp/terraform-provider-signalform).

The Metrics Team at Yelp has built these in order to make managing terraform-provider-signalform a little bit easier. Our intention is to add to this repository as more tools are developed.

signalform-tools is not an official SignalFx product, so we do not guarantee a 1:1 mapping between the SignalFx API and the functionalities offered by this repo.

We welcome additions and modifications that make managing terraform-provider-signalform better for all!

Documentation is available [here](https://yelp.github.io/signalform-tools/).

Changelog is avaliable [here](https://github.com/Yelp/signalform-tools/blob/master/debian/changelog).

## Build And Install

If you want to build the package, then run:
```shell
make package
```

The output packages (trusty and xenial) will be placed in the `dist/` folder (e.g. `dist/trusty/signalform-tools-0.0.10_amd64.deb`)

You can set environament variables to customize your build:

* `CUSTOM_PYPI_URL`: Environment variable to make dh-virtualenv and tox install packages from your internal python package index

Once you built the package, you can just install like:
```shell
sudo dpkg -i dist/trusty/signalform-tools.deb
```

## Usage

signalform-tools has 3 functionalities so far: validate, preflight and show.

### validate: validates resources inside one or more directories
```
usage: signalform-tools validate [-h] [--dir DIR] [filenames [filenames ...]]

Validate resources inside one or more directories.

positional arguments:
  filenames

optional arguments:
  -h, --help  show this help message and exit
  --dir DIR   directory to validate
```

### preflight: helps testing your detectors
```
usage: signalform-tools preflight [-h] [--file FILE | -r] [--label LABEL]
                                  [--start START] [--stop STOP]

Test your detector.

optional arguments:
  -h, --help     show this help message and exit
  --file FILE    Path to tfstate file
  -r, --remote   Use remote state
  --label LABEL  Specific detect label to test, checks all in the current
                 folder by default
  --start START  Start time to check from. Can be either SignalFx relative
                 time format (e.g. "-60m", "-3d", "-1w"), a date or a UNIX
                 epoch timestamp in seconds or milliseconds
  --stop STOP    End time to check until. Can be either SignalFx relative time
                 format (e.g. "Now", "-60m", "-3d"), a date or a UNIX epoch
                 timestamp in seconds or milliseconds
```

### show: shows resources inside the tfstate of the current directory
```
usage: signalform-tools show [-h] [-r]

Show resources inside the tfstate of the current directory.

optional arguments:
  -h, --help    show this help message and exit
  -r, --remote  Use remote state
```

## Development

If you want to test your changes locally:
```shell
virtualenv -p python3.6 foo
source foo/bin/activate
pip /path/to/local/checkout/of/signalform-tools/ --no-use-wheel
signalform-tools CMD

# do more changes
pip uninstall signalform-tools
pip /path/to/local/checkout/of/signalform-tools/ --no-use-wheel
```

## Release

When you're ready to release a new version, steps to take are:

1. Update the release number in `signalform_tools/__about__.py`. Follow [Semantic Versioning](http://semver.org/)
1. Run `make changelog` to add a Debian changelog entry
1. Commit your changes
1. Run `make package` to test the package using Docker
1. Run `make tag` to create another Git lightweight tag
1. Run `git push origin master && git push origin --tags`

## Contributing
Everyone is encouraged to contribute to `signalform-tools`. You can contribute by forking the GitHub repo and making a pull request or opening an issue.
