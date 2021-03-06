# Cross Agent Tests

At commit a891b0c7180c1a10b7abdf5f811081a12f9a8c69.
# Cross Agent Tests

### Data Policy

None of these tests should contain customer data such as SQL strings.
Please be careful when adding new tests from real world failures.

### Access

Push access to this repository is granted via membership in the cross-agent-team GHE group. Contact Belinda Runkle if you are on the agent team but don't have push access.

### Tests

| Test Files    | Description   |
| ------------- |-------------|
| [rum_loader_insertion_location](rum_loader_insertion_location) | Describe where the RUM loader (formerly known as header) should be inserted. |
| [rum_footer_insertion_location](rum_footer_insertion_location) | Describe where the RUM footer (aka "client config") should be inserted.  These tests do not apply to agents which insert the footer directly after the loader. |
| [rules.json](rules.json) | Describe how url/metric/txn-name rules should be applied. |
| [rum_client_config.json](rum_client_config.json) | These tests dictate the format and contents of the browser monitoring client configuration.  For more information see: [SPEC](https://newrelic.atlassian.net/wiki/display/eng/BAM+Agent+Auto-Instrumentation) |
| [sql_parsing.json](sql_parsing.json) | These tests show how an SQL string should be parsed for the operation and table name. |
| [url_clean.json](url_clean.json) | These tests show how URLs should be cleaned before putting them into a trace segment's parameter hash (under the key 'uri'). |
| [url_domain_extraction.json](url_domain_extraction.json) | These tests show how the domain of a URL should be extracted (for the purpose of creating external metrics). |
| [postgres_explain_obfuscation](postgres_explain_obfuscation) | These tests show how plain-text explain plan output from PostgreSQL should be obfuscated when SQL obfuscation is enabled. |
| [sql_obfuscation](sql_obfuscation) | Describe how agents should obfuscate SQL queries before transmission to the collector. |
| [attribute_configuration](attribute_configuration.json) | These tests show how agents should respond to the various attribute configuration settings.  For more information see: [Attributes SPEC](https://source.datanerd.us/agents/agent-specs/blob/master/Agent-Attributes-PORTED.md) |
| [cat](cat) | These tests cover the new Dirac attributes that are added for the CAT Map project. See the [CAT Spec](https://source.datanerd.us/agents/agent-specs/blob/master/Cross-Application-Tracing-PORTED.md) and the [README](cat/README.md) for details.|
| [labels](labels.json) | These tests cover the Labels for Language Agents project. See the [Labels for Language Agents Spec](https://newrelic.atlassian.net/wiki/display/eng/Labels+for+Language+Agents) for details.|
| [proc_cpuinfo](proc_cpuinfo) | These test correct processing of `/proc/cpuinfo` output on Linux hosts. |
| [proc_meminfo](proc_meminfo) | These test correct processing of `/proc/meminfo` output on Linux hosts. |
| [transaction_segment_terms.json](transaction_segment_terms.json) | These tests cover agent implementations of the `transaction_segment_terms` transaction renaming rules introduced in collector protocol 14. See [the spec](https://newrelic.atlassian.net/wiki/display/eng/Language+agent+transaction+segment+terms+rules) for details. |
| [synthetics](synthetics) | These tests cover agent support for Synthetics. For details, see [Agent Support for Synthetics: Forced Transaction Traces and Analytic Events](https://source.datanerd.us/agents/agent-specs/blob/master/Synthetics-PORTED.md). |
| [docker_container_id](docker_container_id) | These tests cover parsing of Docker container IDs from `/proc/*/cgroup` on Linux hosts. |
| [utilization](utilization) | These tests cover the collection and validation of metadata for billing purposes as per the [Utilization spec](https://source.datanerd.us/agents/agent-specs/blob/master/Utilization.md). |
| [utilization_vendor_specific](utilization_vendor_specific) | These tests cover the collection and validation of metadata for AWS, Pivotal Cloud Foundry, Google Cloud Platform, and Azure as per the [Utilization spec](https://source.datanerd.us/agents/agent-specs/blob/master/Utilization.md). |
| [distributed_tracing](distributed_tracing) | distributed tracing, a.k.a. CAT CATs |
# The Utilization Tests

The Utilization tests ensure that the appropriate information is being gathered for pricing. It is centered around ensuring that the JSON generated by all agents is correct. Each JSON block is a test case, with potentially the following fields:

  - `testname`: The name of the test.
  - `input_total_ram_mib`: The total ram number calculated by the agent.
  - `input_logical_processors`: The number of logical processors calculated by the agent.
  - `input_hostname`: The `hostname` calculated by the agent.
  - `input_aws_id`: The aws `id` determined by the agent.
  - `input_aws_type`: The aws `type` determined by the agent.
  - `input_aws_zone`: The aws `zone` determined by the agent.
  - `input_environment_variables`: Any environment variables which have been set.
  - `expected_output_json`: The expected JSON output from the agent for the `utilization` hash.

New fields for Google Cloud Platform (gcp), Pivotal Cloud Foundry (pcf), and Azure added as of [Utilization spec version 7](https://source.datanerd.us/agents/agent-specs/blob/c78cddeaa5fa23dce892b8c6da95b9f900636c35/Utilization.md):
  - `input_gcp_id`: The gcp `id` determined by the agent.
  - `input_gcp_type`: The gcp `machineType` determined by the agent.
  - `input_gcp_name`: The gcp `name` determined by the agent.
  - `input_gcp_zone`: The gcp `zone` determined by the agent.
  - `input_pcf_guid`: The pcf `cf_instance_guid` determined by the agent.
  - `input_pcf_ip`: The pcf `cf_instance_ip` determined by the agent.
  - `input_pcf_mem_limit`: The pcf `memory_limit` determined by the agent.
  - `input_azure_location`: The azure `location` determined by the agent.
  - `input_azure_name`: The azure `name` determined by the agent.
  - `input_azure_id`: The azure `vmId` determined by the agent.
  - `input_azure_size`: The azure `vmSize` determined by the agent.
 
Test cases for `boot_id.json` added as of [Utilization spec version 7](https://source.datanerd.us/agents/agent-specs/blob/c78cddeaa5fa23dce892b8c6da95b9f900636c35/Utilization.md):
  - `testname`: The name of the test.
  - `input_total_ram_mib`: The total ram number calculated by the agent.
  - `input_logical_processors`: The number of logical processors calculated by the agent.
  - `input_hostname`: The hostname calculated by the agent.
  - `input_boot_id`: The `boot_id` determined by the agent.
  - `expected_output_json`: The expected JSON output from the agent for the utilization hash.
  - `expected_metrics`: Supportability metrics that are either expected or unexpected in a given case. If the `call_count` is 0 it should be asserted that the Supportability metric was not sent.
### CAT Map test details

The CAT map test cases in `cat_map.json` are meant to be used to verify the
attributes that agents collect and attach to analytics transaction events for
the CAT map project.

**NOTE** currently `nr.apdexPerfZone` is not covered by these tests, make sure you test for this yourself until it is added to these tests.

Each test case should correspond to a simulated transaction in the agent under
test. Here's what the various fields in each test case mean:

| Name | Meaning |
| ---- | ------- |
| `name` | A human-meaningful name for the test case. |
| `appName` | The name of the New Relic application for the simulated transaction. |
| `transactionName` | The final name of the simulated transaction. |
| `transactionGuid` | The GUID of the simulated transaction. |
| `inboundPayload` | The (non-serialized) contents of the `X-NewRelic-Transaction` HTTP request header on the simulated transaction. Note that this value should be serialized to JSON, obfuscated using the CAT obfuscation algorithm, and Base64-encoded before being used in the header value. Note also that the `X-NewRelic-ID` header should be set on the simulated transaction, though its value is not specified in these tests. |
| `expectedIntrinsicFields` | A set of key-value pairs that are expected to be present in the analytics event generated for the simulated transaction. These fields should be present in the first hash of the analytic event payload (built-in agent-supplied fields). |
| `nonExpectedIntrinsicFields` | An array of attribute names that should *not* be present in the analytics event generated for the simulated transaction. |
| `outboundRequests` | An array of objects representing outbound requests that should be made in the context of the simulated transaction. See the table below for details. Only present if the test case involves making outgoing requests from the simulated transaction. |

Here's what the fields of each entry in the `outboundRequests` array mean:

| Name | Meaning |
| ---- | ------- |
| `outboundTxnName` | The name of the simulated transaction at the time this outbound request is made. Your test driver should set the transaction name to this value prior to simulating the outbound request. |
| `expectedOutboundPayload` | The expected (un-obfuscated) content of the outbound `X-NewRelic-Transaction` request header for this request. |
These tests are for determining the numbers of physical packages, physical cores,
and logical processors from the data returned by /proc/cpuinfo on Linux hosts.
Each text file in this directory is the output of /proc/cpuinfo on various machines.

The names of all test files should be of the form `Apack_Bcore_Clogical.txt`
where `A`, `B`, and `C` are integers or the character `X`. For example,
a single quad-core processor without hyperthreading would correspond to
`1pack_4core_4logical.txt`, while two 6-core processors with hyperthreading
would correspond to `2pack_12core_24logical.txt`, and would be pretty sweet.

Using `A`, `B`, and `C` from above, code processing the text in these files
should produce the following expected values:

| property             | value   |
| -------------------- |---------|
| # physical packages  | `A`     |
| # physical cores     | `B`     |
| # logical processors | `C`     |

(Obviously, the processing code should do this with no knowledge of the filenames.)

If any of `A`, `B`, or `C` are the character `X` instead of an integer, then
processing code should not return a value (return `null`, return `nil`,
raise an exception... whatever makes most sense for your agent).

There is a malformed.txt file which is a random file that does not adhere to
any /proc/cpuinfo format. The expected result is `null` for packages, cores and
processors.
These test cases cover obfuscation (more properly, masking) of literal values
from SQL statements captured by agents. SQL statements may be captured and
attached to transaction trace nodes, or to slow SQL traces.

`sql_obfuscation.json` contains an array of test cases.  The inputs for each
test case are in the `sql` property of each object. Each test case also has an
`obfuscated` property which is an array containing at least one valid output.

Test cases also have a `dialects` property, which is an array of strings which
specify which sql dialects the test should apply to. See "SQL Syntax Documentation" list below. This is relevant because for example, PostgreSQL uses
different identifier and string quoting rules than MySQL (most notably,
double-quoted string literals are not allowed in PostgreSQL, where
double-quotes are instead used around identifiers).

Test cases may also contain the following properties:
  * `malformed`: (boolean) tests who's SQL queries are not valid SQL in any
  quoting mode. Some agents may choose to attempt to obfuscate these cases,
  and others may instead just replace the query entirely with a placeholder
  message.
  * `pathological`: (boolean) tests which are designed specifically to break
  specific methods of obfuscation, or contain patterns that are known to be
  difficult to handle correctly
  * `comments`: an array of strings that could be usefult for understanding
  the test.

The following database documentation may be helpful in understanding these test
cases:
* [MySQL String Literals](http://dev.mysql.com/doc/refman/5.5/en/string-literals.html)
* [PostgreSQL String Constants](http://www.postgresql.org/docs/8.2/static/sql-syntax-lexical.html#SQL-SYNTAX-CONSTANTS)

SQL Syntax Documentation:
* [MySQL](http://dev.mysql.com/doc/refman/5.5/en/language-structure.html)
* [PostgreSQL](http://www.postgresql.org/docs/8.4/static/sql-syntax.html)
* [Cassandra](http://docs.datastax.com/en/cql/3.1/cql/cql_reference/cql_lexicon_c.html)
* [Oracle](http://docs.oracle.com/cd/B28359_01/appdev.111/b28370/langelems.htm)
* [SQLite](https://www.sqlite.org/lang.html)
# Vendor Specific Utilization Tests

The Utilization tests ensure that the appropriate information is being gathered for pricing for a particular cloud vendor. It is centered around ensuring that the JSON generated by all agents is correct. Each JSON block is a test case, with potentially the following fields:

  - `testname`: The name of the test.
  - `uri`: The API endpoint for the cloud vendor. This contains a response indicating what the expected return from the API is for a given test. 
  - `expected_vendors_hash`: The vendor hash that should be generated by the agent based on the uri response.
  - `expected_metrics`: Supportability metrics that are either expected or unexpected in a given case. If the `call_count` is 0 it should be asserted that the Supportability metric was not sent.

As of [Metadata version 3](https://source.datanerd.us/agents/agent-specs/blob/c78cddeaa5fa23dce892b8c6da95b9f900636c35/Utilization.md) specs have been added for Azure, Google Cloud Platform, and Pivotal Cloud Foundry in addition to updates for AWS.These tests cover parsing of Docker container IDs on Linux hosts out of
`/proc/self/cgroup` (or `/proc/<pid>/cgroup` more generally).

The `cases.json` file lists each filename in this directory containing
example `/proc/self/cgroup` content, and the expected Docker container ID that
should be parsed from that file.
# Synthetics Tests

The Synthetics tests are designed to verify that the agent handles valid and invalid Synthetics requests.

Each test should run a simulated web transaction. A Synthetics HTTP request header is added to the incoming request at the beginning of a web transaction. During the course of the web transaction, an external request is made. And, at the completion of the web transaction, both a Transaction Trace and Transaction Event are recorded.

Each test then verifies that the correct attributes are added to the Transaction Trace and Transaction Event, and the proper request header is added to the external request when required. Or, in the case of an invalid Synthetics request, that the attributes and request header are **not** added.

## Name

| Name | Meaning |
| ---- | ------- |
| `name` | A human-meaningful name for the test case. |

## Settings

The `settings` hash contains a number of key-value pairs that the agent will need to use for configuration for the test.

| Name | Meaning |
| ---- | ------- |
| `agentEncodingKey`| The encoding key used by the agent for deobfuscation of the Synthetics request header. |
| `syntheticsEncodingKey` | The encoding key used by Synthetics to obfuscate the Synthetics request header. In most tests, `agentEncodingKey` and `syntheticsEncodingKey` are the same. |
| `transactionGuid` | The GUID of the simulated transaction. In a non-simulated transaction, this will be randomly generated. But, for testing purposes, you should assign this value as the GUID, since the tests will check for this value to be set in the `nr.guid` attribute of the Transaction Event. |
| `trustedAccountIds` | A list of accounts ids that the agent trusts. If the Synthetics request contains a non-trusted account id, it is an invalid request.|

## Inputs

The input for each test is a Synthetics request header. The test fixture file shows both the de-obfuscated version of the payload, as well as the resulting obfuscated version.

| Name | Meaning |
| ---- | ------- |
| `inputHeaderPayload` | A decoded form of the contents of the `X-NewRelic-Synthetics` request header. |
| `inputObfuscatedHeader` | An obfuscated form of the `X-NewRelic-Synthetics` request header. If you obfuscate `inputHeaderPayload` using the `syntheticsEncodingKey`, this should be the output. |

## Outputs

There are three different outputs that are tested for: Transaction Trace, Transaction Event, and External Request Header.

### outputTransactionTrace

The `outputTransactionTrace` hash contains three objects:

| Name | Meaning |
| ---- | ------- |
| `header` | The last field of the transaction sample array should be set to the Synthetics Resource ID for a Synthetics request, and should be set to `null` if it isn't. (The last field in the array is the 10th element in the header array, but is `header[9]` in zero-based array notation, so the key name is `field_9`.) |
| `expectedIntrinsics` | A set of key-value pairs that represent the attributes that should be set in the intrinsics section of the Transaction Trace. **Note**: If the agent has not implemented the Agent Attributes spec, then the agent should save the attributes in the `Custom` section, and the attribute names should have 'nr.' prepended to them. Read the spec for details. For agents in this situation, they will need to adjust the expected output of the tests accordingly. |
| `nonExpectedIntrinsics` | An array of names that represent the attributes that should **not** be set in the intrinsics section of the Transaction Trace.|

### outputTransactionEvent

The `outputTransactionEvent` hash contains two objects:

| Name | Meaning |
| ---- | ------- |
| `expectedAttributes` | A set of key-value pairs that represent the attributes that should be set in the `Intrinsic` hash of the Transaction Event. |
| `nonExpectedAttributes` | An array of names that represent the attributes that should **not** be set in the `Intrinsic` hash of the Transaction Event. |

### outputExternalRequestHeader

The `outputExternalRequestHeader` hash contains two objects:

| Name | Meaning |
| ---- | ------- |
| `expectedHeader` | The outbound header that should be added to external requests (similar to the CAT header), when the original request was made from a valid Synthetics request. |
| `nonExpectedHeader` | The outbound header that should **not** be added to external requests, when the original request was made from a non-Synthetics request. |
# PostgreSQL explain plan obfuscation tests

These tests show how explain plans for PostgreSQL should be obfuscated when
SQL obfuscation is enabled. Obfuscation of explain plans for PostgreSQL is
necessary because they can include portions of the original query that may
contain sensitive data.

Each test case consists of a set of files with the following extensions:

* `.query.txt` - the original SQL query that is being explained
* `.explain.txt` - the raw un-obfuscated output from running `EXPLAIN <query>`
* `.colon_obfuscated.txt` - the desired obfuscated explain output if using the
default, more aggressive obfuscation strategy described [here](https://newrelic.atlassian.net/wiki/display/eng/Obfuscating+PostgreSQL+Explain+plans).
* `.obfuscated.txt` - the desired obfuscated explain output if using a more
accurate, less aggressive obfuscation strategy detailed in this
[Jive thread](https://newrelic.jiveon.com/thread/1851).
These tests are for determining the physical memory from the data returned by
/proc/meminfo on Linux hosts. The total physical memory of the linux system is 
reported as part of the enviornment values. The key used by the Python agent
is 'Total Physical Memory (MB)'. 

The names of all test files should be of the form `meminfo_nnnnMB.txt`. The
value `nnnn` in the filename is the physical memory of that system in MB.
## Datastore instance tests

The datastore instance tests provide attributes similar to what an agent could expect to find regarding a database configuration and specifies the expected [datastore instance metric](https://source.datanerd.us/agents/agent-specs/blob/master/Datastore-Metrics-PORTED.md#datastore-metric-namespace) that should be generated. The table below lists types attributes and whether will will always be included or optionally included in each test case.

| Name | Present | Description |
|---|---|---|
| system_hostname | always | the hostname of the machine |
| db_hostname | sometimes | the hostname reported by the database adapter |
| product | always | the database product for this configuration
| port | sometimes | the port reported by the database adapter |
| unix_socket | sometimes |the path to a unix domain socket reported by a database adapter |
| database_path | sometimes |the path to a filesystem database |
| expected\_instance\_metric | always | the instance metric expected to be generated from the given attributes |

## Implementing the test cases
The idea behind these test cases are that you are able to determine a set of configuration properties from a database connection, and based on those properties you should generate the `expected_instance_metric`. Sometimes the properties available are minimal and will mean that you will need to fall back to defaults to obtain some of the information. When there is missing information from a database adapter the guiding principle is to fill in the defaults when they can be inferred, but do not make guesses that could be incorrect or misleading. Some agents may have access to better data and may not need to make inferences. If this applies to your agent then many of these tests will not be applicable.
