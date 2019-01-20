<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Apache Arrow Ruby

There are the official Ruby bindings for Apache Arrow.

[Red Arrow](https://github.com/apache/arrow/tree/master/ruby/red-arrow) is the base Apache Arrow bindings.

[Red Arrow CUDA](https://github.com/apache/arrow/tree/master/ruby/red-arrow-cuda) is the Apache Arrow bindings of CUDA part.

[Red Gandiva](https://github.com/apache/arrow/tree/master/ruby/red-gandiva) is the Gandiva bindings.

[Red Plasma](https://github.com/apache/arrow/tree/master/ruby/red-plasma) is the Plasma bindings.

[Red Parquet](https://github.com/apache/arrow/tree/master/ruby/red-parquet) is the Parquet bindings.


<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Red Gandiva - Gandiva Ruby

Red Gandiva is the Ruby bindings of Gandiva. Red Gandiva is based on GObject Introspection.

Gandiva is a toolset for compiling and evaluating expressions on Arrow data.

[GObject Introspection](https://wiki.gnome.org/action/show/Projects/GObjectIntrospection) is a middleware for language bindings of C library. GObject Introspection can generate language bindings automatically at runtime.

Red Gandiva uses [Gandiva GLib](https://github.com/apache/arrow/tree/master/c_glib/gandiva-glib) and [gobject-introspection gem](https://rubygems.org/gems/gobject-introspection) to generate Ruby bindings of Gandiva.

Gandiva GLib is a C wrapper for [Gandiva C++](https://github.com/apache/arrow/tree/master/cpp/gandiva). GObject Introspection can't use Gandiva C++ directly. Gandiva GLib is a bridge between Gandiva C++ and GObject Introspection.

gobject-introspection gem is a Ruby bindings of GObject Introspection. Red Gandiva uses GObject Introspection via gobject-introspection gem.

## Install

Install Gandiva GLib before install Red Gandiva. Use [packages.red-data-tools.org](https://github.com/red-data-tools/packages.red-data-tools.org) for installing Gandiva GLib.

Note that the Gandiva GLib packages are "unofficial". "Official" packages will be released in the future.

Install Red Gandiva after you install Gandiva GLib:

```text
% gem install red-gandiva
```

## Usage

```ruby
require "gandiva"

field1 = Arrow::Field.new("field1", Arrow::Int32DataType.new)
field2 = Arrow::Field.new("field2", Arrow::Int32DataType.new)
schema = Arrow::Schema.new([field1, field2])
add_result = Arrow::Field.new("add_result", Arrow::Int32DataType.new)
subtract_result = Arrow::Field.new("subtract_result", Arrow::Int32DataType.new)
add_expression = Gandiva::Expression.new("add", [field1, field2], add_result)
subtract_expression = Gandiva::Expression.new("subtract", [field1, field2], subtract_result)
projector = Gandiva::Projector.new(schema, [add_expression, subtract_expression])
input_arrays = [
  Arrow::Int32Array.new([1, 2, 3, 4]),
  Arrow::Int32Array.new([11, 13, 15, 17]),
]
record_batch = Arrow::RecordBatch.new(schema, 4, input_arrays)
output_arrays = projector.evaluate(record_batch)
```
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Red Plasma - Plasma Ruby

Red Plasma is the Ruby bindings of Plasma. Red Plasma is based on GObject Introspection.

Plasma is an in-memory object store and cache for big data.

[GObject Introspection](https://wiki.gnome.org/action/show/Projects/GObjectIntrospection) is a middleware for language bindings of C library. GObject Introspection can generate language bindings automatically at runtime.

Red Plasma uses [Plasma GLib](https://github.com/apache/arrow/tree/master/c_glib/plasma-glib) and [gobject-introspection gem](https://rubygems.org/gems/gobject-introspection) to generate Ruby bindings of Plasma.

Plasma GLib is a C wrapper for [Plasma C++](https://github.com/apache/arrow/tree/master/cpp/plasma). GObject Introspection can't use Plasma C++ directly. Plasma GLib is a bridge between Plasma C++ and GObject Introspection.

gobject-introspection gem is a Ruby bindings of GObject Introspection. Red Plasma uses GObject Introspection via gobject-introspection gem.

## Install

Install Plasma GLib before install Red Plasma. Use [packages.red-data-tools.org](https://github.com/red-data-tools/packages.red-data-tools.org) for installing Plasma GLib.

Note that the Plasma GLib packages are "unofficial". "Official" packages will be released in the future.

Install Red Plasma after you install Plasma GLib:

```text
% gem install red-plasma
```

## Usage

Starting the Plasma store

```console
plasma_store_server -m 1000000000 -s /tmp/plasma
```

Creating a Plasma client

```ruby
require "plasma"

client = Plasma::Client.new("/tmp/plasma")
```
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Red Parquet - Apache Parquet Ruby

Red Parquet is the Ruby bindings of Apache Parquet. Red Parquet is based on GObject Introspection.

[Apache Parquet](https://parquet.apache.org/) is a columnar storage format.

[GObject Introspection](https://wiki.gnome.org/action/show/Projects/GObjectIntrospection) is a middleware for language bindings of C library. GObject Introspection can generate language bindings automatically at runtime.

Red Parquet uses [Apache Parquet GLib](https://github.com/apache/arrow/tree/master/c_glib/parquet-glib) and [gobject-introspection gem](https://rubygems.org/gems/gobject-introspection) to generate Ruby bindings of Apache Parquet.

Apache Parquet GLib is a C wrapper for [Apache Parquet C++](https://github.com/apache/arrow/tree/master/cpp/parquet). GObject Introspection can't use Apache Parquet C++ directly. Apache Parquet GLib is a bridge between Apache Parquet C++ and GObject Introspection.

gobject-introspection gem is a Ruby bindings of GObject Introspection. Red Parquet uses GObject Introspection via gobject-introspection gem.

## Install

Install Apache Parquet GLib before install Red Parquet. Use [packages.red-data-tools.org](https://github.com/red-data-tools/packages.red-data-tools.org) for installing Apache Parquet GLib.

Note that the Apache Parquet GLib packages are "unofficial". "Official" packages will be released in the future.

Install Red Parquet after you install Apache Parquet GLib:

```text
% gem install red-parquet
```

## Usage

```ruby
require "parquet"

table = Arrow::Table.load("/dev/shm/data.parquet")
# Process data in table
table.save("/dev/shm/data-processed.parquet")
```
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Red Arrow CUDA - Apache Arrow CUDA Ruby

Red Arrow CUDA is the Ruby bindings of Apache Arrow CUDA. Red Arrow CUDA is based on GObject Introspection.

[Apache Arrow CUDA](https://arrow.apache.org/) is an in-memory columnar data store on GPU.

[GObject Introspection](https://wiki.gnome.org/action/show/Projects/GObjectIntrospection) is a middleware for language bindings of C library. GObject Introspection can generate language bindings automatically at runtime.

Red Arrow CUDA uses [Apache Arrow CUDA GLib](https://github.com/apache/arrow/tree/master/c_glib) and [gobject-introspection gem](https://rubygems.org/gems/gobject-introspection) to generate Ruby bindings of Apache Arrow CUDA.

Apache Arrow CUDA GLib is a C wrapper for [Apache Arrow CUDA C++](https://github.com/apache/arrow/tree/master/cpp). GObject Introspection can't use Apache Arrow CUDA C++ directly. Apache Arrow CUDA GLib is a bridge between Apache Arrow CUDA C++ and GObject Introspection.

gobject-introspection gem is a Ruby bindings of GObject Introspection. Red Arrow CUDA uses GObject Introspection via gobject-introspection gem.

## Install

Install Apache Arrow CUDA GLib before install Red Arrow CUDA. Use [packages.red-data-tools.org](https://github.com/red-data-tools/packages.red-data-tools.org) for installing Apache Arrow CUDA GLib.

Note that the Apache Arrow CUDA GLib packages are "unofficial". "Official" packages will be released in the future.

Install Red Arrow CUDA after you install Apache Arrow CUDA GLib:

```text
% gem install red-arrow-cuda
```

## Usage

```ruby
require "arrow-cuda"

manager = ArrowCUDA::DeviceManager.new
if manager.n_devices.zero?
  raise "No GPU is found"
end

context = manager[0]
buffer = ArrowCUDA::Buffer.new(context, 128)
ArrowCUDA::BufferOutputStream.open(buffer) do |stream|
  stream.write("Hello World")
end
puts buffer.copy_to_host(0, 11) # => "Hello World"
```
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Red Arrow - Apache Arrow Ruby

Red Arrow is the Ruby bindings of Apache Arrow. Red Arrow is based on GObject Introspection.

[Apache Arrow](https://arrow.apache.org/) is an in-memory columnar data store. It's used by many products for data analytics.

[GObject Introspection](https://wiki.gnome.org/action/show/Projects/GObjectIntrospection) is a middleware for language bindings of C library. GObject Introspection can generate language bindings automatically at runtime.

Red Arrow uses [Apache Arrow GLib](https://github.com/apache/arrow/tree/master/c_glib) and [gobject-introspection gem](https://rubygems.org/gems/gobject-introspection) to generate Ruby bindings of Apache Arrow.

Apache Arrow GLib is a C wrapper for [Apache Arrow C++](https://github.com/apache/arrow/tree/master/cpp). GObject Introspection can't use Apache Arrow C++ directly. Apache Arrow GLib is a bridge between Apache Arrow C++ and GObject Introspection.

gobject-introspection gem is a Ruby bindings of GObject Introspection. Red Arrow uses GObject Introspection via gobject-introspection gem.

## Install

Install Apache Arrow GLib before install Red Arrow. Use [packages.red-data-tools.org](https://github.com/red-data-tools/packages.red-data-tools.org) for installing Apache Arrow GLib.

Note that the Apache Arrow GLib packages are "unofficial". "Official" packages will be released in the future.

Install Red Arrow after you install Apache Arrow GLib:

```console
% gem install red-arrow
```

## Usage

```ruby
require "arrow"

table = Arrow::Table.load("/dev/shm/data.arrow")
# Process data in table
table.save("/dev/shm/data-processed.arrow")
```
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Native Rust implementation of Apache Arrow

## The Rust implementation of Arrow consists of the following crates

- Arrow [(README)](arrow/README.md)
- Parquet [(README)](parquet/README.md)

## Run Tests

Parquet support in Arrow requires data to test against, this data is in a
git submodule.  To pull down this data run the following:

```bash
git submodule update --init
```

The data can then be found in `cpp/submodules/parquet_testing/data`.
Create a new environment variable called `PARQUET_TEST_DATA` to point
to this location and then `cargo test` as usual.

## Code Formatting

Our CI uses `rustfmt` to check code formatting.  Although the project is
built and tested against nightly rust we use the stable version of
`rustfmt`.  So before submitting a PR be sure to run the following
and check for lint issues:

```bash
cargo +stable fmt --all -- --check
```

<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# An Apache Parquet implementation in Rust

## Usage
Add this to your Cargo.toml:
```toml
[dependencies]
parquet = "0.4"
```

and this to your crate root:
```rust
extern crate parquet;
```

Example usage of reading data:
```rust
use std::fs::File;
use std::path::Path;
use parquet::file::reader::{FileReader, SerializedFileReader};

let file = File::open(&Path::new("/path/to/file")).unwrap();
let reader = SerializedFileReader::new(file).unwrap();
let mut iter = reader.get_row_iter(None).unwrap();
while let Some(record) = iter.next() {
    println!("{}", record);
}
```
See [crate documentation](https://docs.rs/crate/parquet/0.4.2) on available API.

## Supported Parquet Version
- Parquet-format 2.4.0

To update Parquet format to a newer version, check if [parquet-format](https://github.com/sunchao/parquet-format-rs)
version is available. Then simply update version of `parquet-format` crate in Cargo.toml.

## Features
- [X] All encodings supported
- [X] All compression codecs supported
- [X] Read support
  - [X] Primitive column value readers
  - [X] Row record reader
  - [ ] Arrow record reader
- [X] Statistics support
- [X] Write support
  - [X] Primitive column value writers
  - [ ] Row record writer
  - [ ] Arrow record writer
- [ ] Predicate pushdown
- [ ] Parquet format 2.5 support
- [ ] HDFS support

## Requirements
- Rust nightly

See [Working with nightly Rust](https://github.com/rust-lang-nursery/rustup.rs/blob/master/README.md#working-with-nightly-rust)
to install nightly toolchain and set it as default.

Parquet requires LLVM.  Our windows CI image includes LLVM but to build the libraries locally windows
users will have to install LLVM. Follow [this](https://github.com/appveyor/ci/issues/2651) link for info.

## Build
Run `cargo build` or `cargo build --release` to build in release mode.
Some features take advantage of SSE4.2 instructions, which can be
enabled by adding `RUSTFLAGS="-C target-feature=+sse4.2"` before the
`cargo build` command.

## Test
Run `cargo test` for unit tests.

## Binaries
The following binaries are provided (use `cargo install` to install them):
- **parquet-schema** for printing Parquet file schema and metadata.
`Usage: parquet-schema <file-path> [verbose]`, where `file-path` is the path to a Parquet file,
and optional `verbose` is the boolean flag that allows to print full metadata or schema only
(when not specified only schema will be printed).

- **parquet-read** for reading records from a Parquet file.
`Usage: parquet-read <file-path> [num-records]`, where `file-path` is the path to a Parquet file,
and `num-records` is the number of records to read from a file (when not specified all records will
be printed).

If you see `Library not loaded` error, please make sure `LD_LIBRARY_PATH` is set properly:
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(rustc --print sysroot)/lib
```

## Benchmarks
Run `cargo bench` for benchmarks.

## Docs
To build documentation, run `cargo doc --no-deps`.
To compile and view in the browser, run `cargo doc --no-deps --open`.

## License
Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0.
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Native Rust implementation of Apache Arrow

[![Build Status](https://travis-ci.org/apache/arrow.svg?branch=master)](https://travis-ci.org/apache/arrow)
[![Coverage Status](https://coveralls.io/repos/github/apache/arrow/badge.svg)](https://coveralls.io/github/apache/arrow)

## Status

This is a native Rust implementation of Apache Arrow. Currently the project
is developed and tested against nightly Rust.  The current status is:

- [x] Primitive Arrays
- [x] List Arrays
- [x] Struct Arrays
- [x] CSV Reader
- [ ] CSV Writer
- [ ] Parquet Reader
- [ ] Parquet Writer
- [ ] Arrow IPC
- [ ] Interop tests with other implementations

## Examples

The examples folder shows how to construct some different types of Arrow
arrays, including dynamic arrays created at runtime.

Examples can be run using the `cargo run --example` command. For example:

```bash
cargo run --example builders
cargo run --example dynamic_types
cargo run --example read_csv
```

# Publishing to crates.io

An Arrow committer can publish this crate after an official project release has
been made to crates.io using the following instructions.

Follow [these
instructions](https://doc.rust-lang.org/cargo/reference/publishing.html) to
create an account and login to crates.io before asking to be added as an owner
of the [arrow crate](https://crates.io/crates/arrow).

Checkout the tag for the version to be released. For example:

```bash
git checkout apache-arrow-0.11.0
```

If the Cargo.toml in this tag already contains `version = "0.11.0"` (as it
should) then the crate can be published with the following command:

```bash
cargo publish
```

If the Cargo.toml does not have the correct version then it will be necessary
to modify it manually. Since there is now a modified file locally that is not
committed to github it will be necessary to use the following command.

```bash
cargo publish --allow-dirty
```

<!-- README.md is generated from README.Rmd. Please edit that file -->

# arrow

R integration with Apache Arrow.

## Installation

First install a release build of the C++ bindings to arrow.

``` shell
git clone https://github.com/apache/arrow.git
cd arrow/cpp && mkdir release && cd release

# It is important to statically link to boost libraries
cmake .. -DARROW_PARQUET=ON -DCMAKE_BUILD_TYPE=Release -DARROW_BOOST_USE_SHARED:BOOL=Off
make install
```

Then the R package:

``` r
devtools::install_github("apache/arrow/r")
```

## Example

``` r
library(arrow, warn.conflicts = FALSE)
library(tibble)
library(reticulate)

tf <- tempfile()

# write arrow::Table to file
(tib <- tibble(x = 1:10, y = rnorm(10)))
#> # A tibble: 10 x 2
#>        x       y
#>    <int>   <dbl>
#>  1     1  0.0855
#>  2     2 -1.68  
#>  3     3 -0.0294
#>  4     4 -0.124 
#>  5     5  0.0675
#>  6     6  1.64  
#>  7     7  1.54  
#>  8     8 -0.0209
#>  9     9 -0.982 
#> 10    10  0.349
# arrow::write_arrow(tib, tf)

# # read it back with pyarrow
# pa <- import("pyarrow")
# as_tibble(pa$open_file(tf)$read_pandas())
```
---
output: github_document
---

<!-- README.md is generated from README.Rmd. Please edit that file -->

```{r setup, include = FALSE}
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>",
  fig.path = "man/figures/README-",
  out.width = "100%"
)
```
# arrow

R integration with Apache Arrow.

## Installation

First install a release build of the C++ bindings to arrow.

```shell
git clone https://github.com/apache/arrow.git
cd arrow/cpp && mkdir release && cd release

# It is important to statically link to boost libraries
cmake .. -DARROW_PARQUET=ON -DCMAKE_BUILD_TYPE=Release -DARROW_BOOST_USE_SHARED:BOOL=Off
make install
```

Then the R package:

```r
devtools::install_github("apache/arrow/r")
```

## Example

```{r}
library(arrow, warn.conflicts = FALSE)
library(tibble)
library(reticulate)

tf <- tempfile()

# write arrow::Table to file
(tib <- tibble(x = 1:10, y = rnorm(10)))
# arrow::write_arrow(tib, tf)

# # read it back with pyarrow
# pa <- import("pyarrow")
# as_tibble(pa$open_file(tf)$read_pandas())
```
