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

## Apache Arrow

<table>
  <tr>
    <td>Build Status</td>
    <td>
    <a href="https://travis-ci.org/apache/arrow">
    <img src="https://travis-ci.org/apache/arrow.svg?branch=master" alt="travis build status" />
    </a>
    </td>
    <td>Code Coverage</td>
    <td>
    <a href="https://codecov.io/gh/apache/arrow">
    <img src="https://codecov.io/gh/apache/arrow/branch/master/graph/badge.svg" alt="codecov.io code coverage" />
    </a>
    </td>
  </tr>
</table>

### Powering In-Memory Analytics

Apache Arrow is a development platform for in-memory analytics. It contains a
set of technologies that enable big data systems to process and move data fast.

Major components of the project include:

 - [The Arrow Columnar In-Memory Format](https://github.com/apache/arrow/tree/master/format)
 - [C++ libraries](https://github.com/apache/arrow/tree/master/cpp)
 - [C bindings using GLib](https://github.com/apache/arrow/tree/master/c_glib)
 - [C# .NET libraries](https://github.com/apache/arrow/tree/master/csharp)
 - [Gandiva](https://github.com/apache/arrow/tree/master/cpp/src/gandiva): an [LLVM](https://llvm.org)-based Arrow expression compiler, part of the C++ codebase
 - [Go libraries](https://github.com/apache/arrow/tree/master/go)
 - [Java libraries](https://github.com/apache/arrow/tree/master/java)
 - [JavaScript libraries](https://github.com/apache/arrow/tree/master/js)
 - [Plasma Object Store](https://github.com/apache/arrow/tree/master/cpp/src/plasma): a
   shared-memory blob store, part of the C++ codebase
 - [Python libraries](https://github.com/apache/arrow/tree/master/python)
 - [R libraries](https://github.com/apache/arrow/tree/master/r)
 - [Ruby libraries](https://github.com/apache/arrow/tree/master/ruby)
 - [Rust libraries](https://github.com/apache/arrow/tree/master/rust)

Arrow is an [Apache Software Foundation](https://www.apache.org) project. Learn more at
[arrow.apache.org](https://arrow.apache.org).

### What's in the Arrow libraries?

The reference Arrow libraries contain a number of distinct software components:

- Columnar vector and table-like containers (similar to data frames) supporting
  flat or nested types
- Fast, language agnostic metadata messaging layer (using Google's Flatbuffers
  library)
- Reference-counted off-heap buffer memory management, for zero-copy memory
  sharing and handling memory-mapped files
- Low-overhead IO interfaces to files on disk, HDFS (C++ only)
- Self-describing binary wire formats (streaming and batch/file-like) for
  remote procedure calls (RPC) and
  interprocess communication (IPC)
- Integration tests for verifying binary compatibility between the
  implementations (e.g. sending data from Java to C++)
- Conversions to and from other in-memory data structures

### Getting involved

Even if you do not plan to contribute to Apache Arrow itself or Arrow
integrations in other projects, we'd be happy to have you involved:

- Join the mailing list: send an email to
  [dev-subscribe@arrow.apache.org][1]. Share your ideas and use cases for the
  project.
- [Follow our activity on JIRA][3]
- [Learn the format][2]
- Contribute code to one of the reference implementations

### How to Contribute

We prefer to receive contributions in the form of GitHub pull requests. Please
send pull requests against the [github.com/apache/arrow][4] repository.

If you are looking for some ideas on what to contribute, check out the [JIRA
issues][3] for the Apache Arrow project. Comment on the issue and/or contact
[dev@arrow.apache.org](http://mail-archives.apache.org/mod_mbox/arrow-dev/)
with your questions and ideas.

If you’d like to report a bug but don’t have time to fix it, you can still post
it on JIRA, or email the mailing list
[dev@arrow.apache.org](http://mail-archives.apache.org/mod_mbox/arrow-dev/)

To contribute a patch:

1. Break your work into small, single-purpose patches if possible. It’s much
harder to merge in a large change with a lot of disjoint features.
2. Create a JIRA for your patch on the [Arrow Project
JIRA](https://issues.apache.org/jira/browse/ARROW).
3. Submit the patch as a GitHub pull request against the master branch. For a
tutorial, see the GitHub guides on forking a repo and sending a pull
request. Prefix your pull request name with the JIRA name (ex:
https://github.com/apache/arrow/pull/240).
4. Make sure that your code passes the unit tests. You can find instructions
how to run the unit tests for each Arrow component in its respective README
file.
5. Add new unit tests for your code.

Thank you in advance for your contributions!

[1]: mailto:dev-subscribe@arrow.apache.org
[2]: https://github.com/apache/arrow/tree/master/format
[3]: https://issues.apache.org/jira/browse/ARROW
[4]: https://github.com/apache/arrow
