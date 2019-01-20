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

# Apache Arrow Documentation

This directory contains source files for building the main project
documentation. This includes the [Arrow columnar format specification][2].

Instructions for building the documentation site are found in
[docs/source/python/development.rst][1]. The build depends on the API
documentation for some of the project subcomponents.

[1]: https://github.com/apache/arrow/blob/master/docs/source/python/development.rst#building-the-documentation
[2]: https://github.com/apache/arrow/tree/master/docs/source/format.. Licensed to the Apache Software Foundation (ASF) under one
.. or more contributor license agreements.  See the NOTICE file
.. distributed with this work for additional information
.. regarding copyright ownership.  The ASF licenses this file
.. to you under the Apache License, Version 2.0 (the
.. "License"); you may not use this file except in compliance
.. with the License.  You may obtain a copy of the License at

..   http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing,
.. software distributed under the License is distributed on an
.. "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
.. KIND, either express or implied.  See the License for the
.. specific language governing permissions and limitations
.. under the License.

Arrow specification documents
=============================

Currently, the Arrow specification consists of these pieces:

- Metadata specification (see :doc:`Metadata`)
- Physical memory layout specification (see :doc:`Layout`)
- Logical Types, Schemas, and Record Batch Metadata (see Schema.fbs)
- Encapsulated Messages (see Message.fbs)
- Mechanics of messaging between Arrow systems (IPC, RPC, etc.) (see :doc:`IPC`)
- Tensor (Multi-dimensional array) Metadata (see Tensor.fbs)

The metadata currently uses Google's `flatbuffers library`_ for serializing a
couple related pieces of information:

- Schemas for tables or record (row) batches. This contains the logical types,
  field names, and other metadata. Schemas do not contain any information about
  actual data.
- *Data headers* for record (row) batches. These must correspond to a known
  schema, and enable a system to send and receive Arrow row batches in a form
  that can be precisely disassembled or reconstructed.

Arrow Format Maturity and Stability
-----------------------------------

We have made significant progress hardening the Arrow in-memory format and
Flatbuffer metadata since the project started in February 2016. We have
integration tests which verify binary compatibility between the Java and C++
implementations, for example.

Major versions may still include breaking changes to the memory format or
metadata, so it is recommended to use the same released version of all
libraries in your applications for maximum compatibility. Data stored in the
Arrow IPC formats should not be used for long term storage.

.. _flatbuffers library: http://github.com/google/flatbuffers
