1. Compile RocksDB first by executing `make static_lib` in parent dir
2. Compile all examples: `cd examples/; make all`
## User Documentation for rocksdb.org

This directory will contain the user and feature documentation for RocksDB. The documentation will be hosted on GitHub pages.

### Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details on how to add or modify content.

### Run the Site Locally

The requirements for running a GitHub pages site locally is described in [GitHub help](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#requirements). The steps below summarize these steps.

> If you have run the site before, you can start with step 1 and then move on to step 5.

1. Ensure that you are in the `/docs` directory in your local RocksDB clone (i.e., the same directory where this `README.md` exists). The below RubyGems commands, etc. must be run from there.

1. Make sure you have Ruby and [RubyGems](https://rubygems.org/) installed.

   > Ruby >= 2.2 is required for the gems. On the latest versions of Mac OS X, Ruby 2.0 is the
   > default. Use `brew install ruby` (or your preferred upgrade mechanism) to install a newer
   > version of Ruby for your Mac OS X system.

1. Make sure you have [Bundler](http://bundler.io/) installed.

    ```
    # may require sudo
    gem install bundler
    ```
1. Install the project's dependencies

    ```
    # run this in the 'docs' directory
    bundle install
    ```

    > If you get an error when installing `nokogiri`, you may be running into the problem described
    > in [this nokogiri issue](https://github.com/sparklemotion/nokogiri/issues/1483). You can
    > either `brew uninstall xz` (and then `brew install xz` after the bundle is installed) or
    > `xcode-select --install` (although this may not work if you have already installed command
    > line tools).

1. Run Jekyll's server.

    - On first runs or for structural changes to the documentation (e.g., new sidebar menu item), do a full build.

    ```
    bundle exec jekyll serve
    ```

    - For content changes only, you can use `--incremental` for faster builds.

    ```
    bundle exec jekyll serve --incremental
    ```

    > We use `bundle exec` instead of running straight `jekyll` because `bundle exec` will always use the version of Jekyll from our `Gemfile`. Just running `jekyll` will use the system version and may not necessarily be compatible.

    - To run using an actual IP address, you can use `--host=0.0.0.0`

    ```
    bundle exec jekyll serve --host=0.0.0.0
    ```

    This will allow you to use the IP address associated with your machine in the URL. That way you could share it with other people.

    e.g., on a Mac, you can your IP address with something like `ifconfig | grep "inet " | grep -v 127.0.0.1`.    

1. Either of commands in the previous step will serve up the site on your local device at http://127.0.0.1:4000/ or http://localhost:4000.

### Updating the Bundle

The site depends on Github Pages and the installed bundle is based on the `github-pages` gem.
Occasionally that gem might get updated with new or changed functionality. If that is the case,
you can run:

```
bundle update
```

to get the latest packages for the installation.
This directory contains interfaces and implementations that isolate the
rest of the package from platform details.

Code in the rest of the package includes "port.h" from this directory.
"port.h" in turn includes a platform specific "port_<platform>.h" file
that provides the platform specific implementation.

See port_posix.h for an example of what must be provided in a platform
specific header file.

This directory contains the hdfs extensions needed to make rocksdb store
files in HDFS.

It has been compiled and testing against CDH 4.4 (2.0.0+1475-1.cdh4.4.0.p0.23~precise-cdh4.4.0).

The configuration assumes that packages libhdfs0, libhdfs0-dev are 
installed which basically means that hdfs.h is in /usr/include and libhdfs in /usr/lib

The env_hdfs.h file defines the rocksdb objects that are needed to talk to an
underlying filesystem. 

If you want to compile rocksdb with hdfs support, please set the following
environment variables appropriately (also defined in setup.sh for convenience)
   USE_HDFS=1
   JAVA_HOME=/usr/local/jdk-7u79-64
   LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/jdk-7u79-64/jre/lib/amd64/server:/usr/local/jdk-7u79-64/jre/lib/amd64/:./snappy/libs
   make clean all db_bench

To run dbbench,
  set CLASSPATH to include your hadoop distribution
  db_bench --hdfs="hdfs://hbaseudbperf001.snc1.facebook.com:9000"


# RDB - RocksDB Shell

RDB is a NodeJS-based shell interface to RocksDB. It can also be used as a
JavaScript binding for RocksDB within a Node application.

## Setup/Compilation

### Requirements

* static RocksDB library (i.e. librocksdb.a)
* libsnappy
* node (tested onv0.10.33, no guarantees on anything else!)
* node-gyp
* python2 (for node-gyp; tested with 2.7.8)

### Installation

NOTE: If your default `python` binary is not a version of python2, add
the arguments `--python /path/to/python2` to the `node-gyp` commands.

1. Make sure you have the static library (i.e. "librocksdb.a") in the root
directory of your rocksdb installation. If not, `cd` there and run
`make static_lib`.

2. Run `node-gyp configure` to generate the build.

3. Run `node-gyp build` to compile RDB.

## Usage

### Running the shell

Assuming everything compiled correctly, you can run the `rdb` executable
located in the root of the `tools/rdb` directory to start the shell. The file is
just a shell script that runs the node shell and loads the constructor for the
RDB object into the top-level function `RDB`.

### JavaScript API

See `API.md` for how to use RocksDB from the shell.
# Rocksdb Tuning Advisor

## Motivation

The performance of Rocksdb is contingent on its tuning. However,
because of the complexity of its underlying technology and a large number of
configurable parameters, a good configuration is sometimes hard to obtain. The aim of
the python command-line tool, Rocksdb Advisor, is to automate the process of
suggesting improvements in the configuration based on advice from Rocksdb
experts.

## Overview

Experts share their wisdom as rules comprising of conditions and suggestions in the INI format (refer
[rules.ini](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/rules.ini)).
Users provide the Rocksdb configuration that they want to improve upon (as the
familiar Rocksdb OPTIONS file —
[example](https://github.com/facebook/rocksdb/blob/master/examples/rocksdb_option_file_example.ini))
and the path of the file which contains Rocksdb logs and statistics.
The [Advisor](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/rule_parser_example.py)
creates appropriate DataSource objects (for Rocksdb
[logs](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/db_log_parser.py),
[options](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/db_options_parser.py),
[statistics](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/db_stats_fetcher.py) etc.)
and provides them to the [Rules Engine](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/rule_parser.py).
The Rules uses rules from experts to parse data-sources and trigger appropriate rules.
The Advisor's output gives information about which rules were triggered,
why they were triggered and what each of them suggests. Each suggestion
provided by a triggered rule advises some action on a Rocksdb
configuration option, for example, increase CFOptions.write_buffer_size,
set bloom_bits to 2 etc.

## Usage

### Prerequisites
The tool needs the following to run:
* python3

### Running the tool
An example command to run the tool:

```shell
cd rocksdb/tools/advisor
python3 -m advisor.rule_parser_example --rules_spec=advisor/rules.ini --rocksdb_options=test/input_files/OPTIONS-000005 --log_files_path_prefix=test/input_files/LOG-0 --stats_dump_period_sec=20
```

### Command-line arguments

Most important amongst all the input that the Advisor needs, are the rules
spec and starting Rocksdb configuration. The configuration is provided as the
familiar Rocksdb Options file (refer [example](https://github.com/facebook/rocksdb/blob/master/examples/rocksdb_option_file_example.ini)).
The Rules spec is written in the INI format (more details in
[rules.ini](https://github.com/facebook/rocksdb/blob/master/tools/advisor/advisor/rules.ini)).

In brief, a Rule is made of conditions and is triggered when all its
constituent conditions are triggered. When triggered, a Rule suggests changes
(increase/decrease/set to a suggested value) to certain Rocksdb options that
aim to improve Rocksdb performance. Every Condition has a 'source' i.e.
the data source that would be checked for triggering that condition.
For example, a log Condition (with 'source=LOG') is triggered if a particular
'regex' is found in the Rocksdb LOG files. As of now the Rules Engine
supports 3 types of Conditions (and consequently data-sources):
LOG, OPTIONS, TIME_SERIES. The TIME_SERIES data can be sourced from the
Rocksdb [statistics](https://github.com/facebook/rocksdb/blob/master/include/rocksdb/statistics.h)
or [perf context](https://github.com/facebook/rocksdb/blob/master/include/rocksdb/perf_context.h).

For more information about the remaining command-line arguments, run:

```shell
cd rocksdb/tools/advisor
python3 -m advisor.rule_parser_example --help
```

### Sample output

Here, a Rocksdb log-based rule has been triggered:

```shell
Rule: stall-too-many-memtables
LogCondition: stall-too-many-memtables regex: Stopping writes because we have \d+ immutable memtables \(waiting for flush\), max_write_buffer_number is set to \d+
Suggestion: inc-bg-flush option : DBOptions.max_background_flushes action : increase suggested_values : ['2']
Suggestion: inc-write-buffer option : CFOptions.max_write_buffer_number action : increase
scope: col_fam:
{'default'}
```

## Running the tests

Tests for the code have been added to the
[test/](https://github.com/facebook/rocksdb/tree/master/tools/advisor/test)
directory. For example, to run the unit tests for db_log_parser.py:

```shell
cd rocksdb/tools/advisor
python3 -m unittest -v test.test_db_log_parser
```
