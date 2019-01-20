
# Tests

`wavectl` project primarily uses
[unittest](https://docs.python.org/2/library/unittest.html) framework from the
python standard library.

[unittest.mock](https://docs.python.org/3/library/unittest.mock.html) is also
heavily utilized. While testing the `wavectl` command line tool, we do not want
to reach out to a running Wavefront remote server. Instead, the tests read the
json blobs of wavefront resources from the `fixtures` directory and "mock" the
behavior of a wavefront server.

For executing test executables [Makefile.test](https://github.com/box/Makefile.test)
is used.


# Test Fixtures

This directory contains necessary data to run automated unit tests.

During execution, `wavectl` reaches out to your specified Wavefront server
using the [Wavefront API](https://docs.wavefront.com/wavefront_api.html).
However, during automated test execution, we do not want to reach out to a live
Wavefront server. Instead, the json state of some selected alerts and
dashboards are saved in json files in this directory. The json representation
in files are in the same format as a Wavefront server returns them via http
calls.

During unit test execution, the test functions read the json files in this
directory and "mock" the behavior of a Wavefront server. That way the `wavectl`
unit tests can execute independently from a live running Wavefront server.

As it turns out, Wavefront can change the json representation of alerts or
dashboards any time, without giving much notice to users. For that reason,
whenever a new Wavefront server version is deployed, we would like to update
the json files in this directory to contain the latest representations. With a
new version of Wavefont server, the json state may get new keys, or some keys
may be removed or renamed.

To update the json files in this directory, the user needs to execute the
included `create_test_fixtures.py` script. That script reaches out to the
specified Wavefront server. Then the existing alerts and dashboards in this
directory are written into the Wavefront server. After that, they are read back
and again saved in the same json files in this directory. If anything in the
Wavefront representation has changed, the json files in this directory will
have the same change.


For example to update the json files in-place execute the following from this
directory:

```
./create_test_fixtures.py <wavefront-server-url> <wavefront-server-api-token> alert TestAlerts.json TestAlerts.json
./create_test_fixtures.py <wavefront-server-url> <wavefront-server-api-token> dashboard TestDashboards.json TestDashboards.json
```


\# wavectl

\[!\[CircleCI\]\(https://circleci.com/gh/box/wavectl.svg?style=svg\)\]\(https://circleci.com/gh/box/wavectl\)
\[!\[Project Status\]\(http://opensource.box.com/badges/active.svg\)\]\(http://opensource.box.com/badges\)

A command line client for \[Wavefront\]\(https://www.wavefront.com\) inspired by
\[kubectl\]\(https://kubernetes.io/docs/reference/kubectl/overview/\) and
\[git\]\(https://git-scm.com/docs\) command line tools.


\#\# Example Commands

A short list of common usages. For more details \[Use Cases\]\(#example-use-cases\) section.


\#\#\# Show one line summaries for Wavefront alerts


```eval_rst
 .. program-output:: wavectl show alert
    :prompt:
    :returncode: 0
    :ellipsis: 4
```

\#\#\# Show json state of alerts


```eval_rst
 .. program-output:: wavectl show -o json alert
    :prompt:
    :returncode: 0
    :ellipsis: 19
```



\#\#\# Modify a dashboard's json and write it back to Wavefront



```
   $> vim ./metadata-dashboard.json    # Modify the json state of a dashboard
   $> wavectl push ./metadata-dashboard.json  dashboard  # Write the new version to Wavefront
```

```eval_rst
 .. program-output:: mutateDashboards.py
    :returncode: 0
```


\#\# Example Use Cases

\- \[Command line operations on your alerts, dashboards\]\(doc/CommandLine.md\)

\- \[Advanced grep in your alerts and dashboards\]\(doc/AdvancedGrep.md\)

\- \[Launch Wavefront GUI via \`wavectl\`\]\(doc/BrowserIntegration.md\)

\- \[Repetitive editing of alerts, dashboards\]\(doc/RepetitiveEditing.md\)

\- \[Git integration\]\(doc/GitIntegration.md\)

\- \[Easy configuration of \`wavectl\`\]\(doc/WavectlConfig.md\)


\#\# \[Command Reference\]\(doc/CommandReference.md\)


\#\# Installation

To install the latest release:

```
    pip install wavectl
```

To install from the master branch in github:

```
    pip install git+https://github.com/box/wavectl.git
```

The master branch may contain unreleased features or bug fixes. The master branch
\*should\* always stay stable.

\#\# A note about Performance

\`wavectl\`'s execution time depends on the number of alerts or dashboards you
have in Wavefront. All
\[resource filtering\]\(doc/CommandReference.md#resource-options\) except the
\`--customerTag, -t\` option is done on the client side. This enables the
powerful regular expression matching on your results. But if your organization
has thousands of alerts and dashboards, the data size may overwhelm the
\`wavectl\` execution time.

If your organization has a lot of alerts and dashboards in Wavefront we
strongly recommend to use \`--customerTag\` option in your commands. The
filtering based on customerTag is done on the Wavefront server side. With
\`--customerTags\` option, wavectl client will only receive data about
alerts/dashboards if they are tagged with all of the specified tags. This
reduces the data size processed by wavectl and results in faster execution.

\#\# Notes

If you could not find what you were looking for please consider
\[contributing\]\(CONTRIBUTING.md\). You could also take a look at
\[another\]\(https://github.com/wavefrontHQ/ruby-client/blob/master/README-cli.md\)
CLI implementation for Wavefront. That one is written by Wavefront and mirrors their
web api more closely. This \`wavectl\` CLI has evolved from our use cases.

\`wavectl\` is designed to add automation, command line access to Wavefront
data that is \*\*human generated\*\*. Initial examples are alerts and
dashboards. We see those as more permanent, slow changing state in Wavefront.
\`wavectl\` is not optimized to read, write time series data to Wavefront or
any other data that is ingested by Wavefront at real time production workload
scale.

\#\# Support

Need to contact us directly? Email oss@box.com and be sure to include the name
of this project in the subject.

\#\# Copyright and License


Copyright 2018 Box, Inc. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

```
   http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


This directory contains executables that are used in documentation generation.