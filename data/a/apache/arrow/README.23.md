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

## Python library for Apache Arrow

This library provides a Python API for functionality provided by the Arrow C++
libraries, along with tools for Arrow integration and interoperability with
pandas, NumPy, and other software in the Python ecosystem.

## Installing

Across platforms, you can install a recent version of pyarrow with the conda
package manager:

```shell
conda install pyarrow -c conda-forge
```

On Linux/macOS and Windows, you can also install binary wheels from PyPI with pip:

```shell
pip install pyarrow
```

## Development

### Coding Style

We follow a similar PEP8-like coding style to the [pandas project][3].

The code must pass `flake8` (available from pip or conda) or it will fail the
build. Check for style errors before submitting your pull request with:

```
flake8 .
flake8 --config=.flake8.cython .
```

### Building from Source

See the [Development][2] page in the documentation.

### Running the unit tests

We are using [pytest][4] to develop our unit test suite. After building the
project using `setup.py build_ext --inplace`, you can run its unit tests like
so:

```bash
pytest pyarrow
```

The project has a number of custom command line options for its test
suite. Some tests are disabled by default, for example. To see all the options,
run

```bash
pytest pyarrow --help
```

and look for the "custom options" section.

For running the benchmarks, see the [Sphinx documentation][5].

### Building the documentation

```bash
pip install -r ../docs/requirements.txt
python setup.py build_sphinx -s ../docs/source
```

[2]: https://github.com/apache/arrow/blob/master/docs/source/python/development.rst
[3]: https://github.com/pandas-dev/pandas
[4]: https://docs.pytest.org/en/latest/
[5]: https://arrow.apache.org/docs/latest/python/benchmarks.html
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

## Manylinux1 wheels for Apache Arrow

This folder provides base Docker images and an infrastructure to build
`manylinux1` compatible Python wheels that should be installable on all
Linux distributions published in last four years.

The process is split up in two parts: There are base Docker images that build
the native, Python-indenpendent dependencies. For these you can select if you
want to also build the dependencies used for the Parquet support. Depending on
these images, there is also a bash script that will build the pyarrow wheels
for all supported Python versions and place them in the `dist` folder.

### Build instructions

```bash
# Build the python packages
docker run --shm-size=2g --rm -t -i -v $PWD:/io -v $PWD/../../:/arrow quay.io/xhochy/arrow_manylinux1_x86_64_base:latest /io/build_arrow.sh
# Now the new packages are located in the dist/ folder
ls -l dist/
```

### Updating the build environment
The base docker image is less often updated. In the case we want to update
a dependency to a new version, we also need to adjust it. You can rebuild
this image using

```bash
docker build -t arrow_manylinux1_x86_64_base -f Dockerfile-x86_64_base .
```

For each dependency, we have a bash script in the directory `scripts/` that
downloads the sources, builds and installs them. At the end of each dependency
build the sources are removed again so that only the binary installation of a
dependency is persisted in the docker image. When you do local adjustments to
this image, you need to change the name of the docker image in the `docker run`
command.
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

The ORC and JSON files come from the `examples` directory in the Apache ORC
source tree:
https://github.com/apache/orc/tree/master/examples
