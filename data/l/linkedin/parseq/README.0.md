Parseq Lambda Names
==========================

One of the fields in Parseq trace is task name, an optional, human readable field. The intention behind this field was to:
* Provide developers a way to "uniquely" identify a task across different Parseq traces. This is critical for running any analysis like figure out that longest task from Parseq traces for an API call.
* Make it easier for developer to go to source code provided the name. This helps in debugging issues like why a task failed etc.

Parseq uses generated Lambda class name as default value for name field. This was not working for multiple reasons:
* Lambda classes are generated at runtime, so although Lambda class name would be unique across traces sent from one instance of the service, it would not be the same as name in traces emitted from other instances.
* There was no way to point to task in source code by looking at name.

This project aims to provide more meaningful default descriptions for Parseq tasks. Using ASM, this project tries to locate where lambda expression is defined in source code and also infer some details about its execution like function call within lambda expression with number of arguments.

Examples
==========================
For the following code:
```java
  public Task<BatchResult<Long, JobPosting>> fetchJobPostings(Set<Long> jobPostingIds, PathSpecSet projectionSet) { 
    return decorator.batchGet(jobPostingIds, new JobPostingsContext(Optional.empty()), projectionSet) 
        .andThen(batchResult -> 
          updateJobPostingDecoratorSensor(jobPostingIds.size(), batchResult.getErrors().size()) 
        ) 
        .onFailure(t -> updateJobPostingDecoratorSensor(jobPostingIds.size(), jobPostingIds.size())); 
  } 
```

| Before | After |
| ------ | ----- |
| `andThen: com.linkedin.voyager.jobs.services.JobPostingsService$$Lambda$2760/928179328` | `andThen: fetchJobPostings(JobPostingsService:112)` |
| `onFailure: com.linkedin.voyager.jobs.services.JobPostingsService$$Lambda$2761/813689833` | `onFailure: fetchJobPostings(JobPostingsService:114)` |

For the following code:

```java
    return lixTreatmentsTask.map(lixTreatments -> MapHelpers.mergeMaps(lixTreatments, lixOverrides)) 
      .map(treatmentsWithOverrides -> lixTestKeys.stream().filter(k -> treatmentsWithOverrides.containsKey(k.getKey())) 
          .collect(Collectors.toMap(Function.identity(), k -> treatmentsWithOverrides.get(k.getKey())))); 
```

| Before | After |
| ------ | ----- |
| `map: com.linkedin.pemberly.api.server.lix.LixServiceImpl$$Lambda$1211/1604155334` | `map: MapHelpers.mergeMaps(_,_) fetchTreatments(LixServiceImpl:124)` |


How to use
==========================

The shaded jar of parseq-lambda-names should be present on classpath along with parseq jar in order to analyze
generated Lambda classes once when Lambda is executed for first time. If parseq-lambda-names jar is not present
on classpath, then parseq will behave as usual i.e. uses Lambda class name as task description.

Limitations
==========================

As this project uses ASM to analyze generated Lambda bytecode, it is a very fragile mechanism that can potentially break between minor JVM versions.
Currently its tested for jvm versions: 1.8.0_5, 1.8.0_40, 1.8.0_72
ParSeq Rest.li Client
==========================

This project provides implementation of ParSeq rest.li client. It provides two features on top of regular rest.li client:
 * Batching
 * Configuration

Batching
========

ParSeq rest.li client is using ParSeq [Batching](https://github.com/linkedin/parseq/tree/master/subprojects/parseq-batching) feature to transparently aggregate individual requests into BATCH requests. Currently only GET and BATCH_GET operations are supported. Batching functionality can be selectively enabled for subset of requests made by ParSeq rest.li client.

Configuration
=============
ParSeq rest.li client implementation allows fine-grained configuration of the following properties:
 * timeoutMs (long) - timeout in milliseconds. Returned Task will complete with TimeoutException if response is not available within specified amount of time. TimeoutException contains information about what configuration has caused it.
 * batchingEnabled (boolean) - is batching enabled. Enables batching functionality for specified subset of requests. See [Batching](https://github.com/linkedin/parseq/tree/master/subprojects/parseq-batching) for more information about this feature. Currently only GET and BATCH_GET operations are supported.
 * maxBatchSize (int) - Max batch size. Maximum number of keys that will be aggregated together into one BATCH request. If there are more requests that can be batched then they will be grouped into number of BATCH requests, for example, if maxBatchSize is 100 and there are 256 GET requests, then they will be aggregated into 3 BATCH_GET requests containing respectively: 100, 100, 56 elements. However, maxBatchSize does not affect existing rest.li BATCH_GET requests, and it is only used to limit size of batch requests created as a result of aggregation. For example, if maxBatchSize is 100 and there are a BATCH_GET request with 120 elements and 120 GET requests, then they will be aggregated into 3 BATCH_GET requests containing respectively 120, 100, 20 elements. Note that the original 120-element BATCH_GET request will not be splitted into smaller batches.

Each property is defined by a set of Key-Value pairs where Key has the following form:

```
<INBOUND_RESOURCE>.<OPERATION>/<OUTBOUND_RESOURCE>.<OPERATION>
```

Every part of the Key can be substituted with wildcard symbol: `*`.

Inbound and outbound resource names may consist of more than one part if they refer to a sub-resources. In this case path components are separated with a `:` symbol. If name consist of one part and is a name of a parent resource then it will apply to all it's sub-resources.  

More formally, Key is specified by the following grammar:

```
grammar RequestConfigKey;

key 				: inbound '/' outbound EOF;
inbound			: ( restResource | '*' ) '.' ( operationIn | '*' );
outbound			: ( restResource | '*' ) '.' ( operationOut | '*' );
restResource		: Name ( '-' Name )* ( ':' Name )*;
operationIn		: simpleOp | complex | httpExtraOp;
operationOut		: simpleOp | complex;
simpleOp   		: 'GET' | 'BATCH_GET' | 'CREATE' | 'BATCH_CREATE' |
				  'PARTIAL_UPDATE' | 'UPDATE' | 'BATCH_UPDATE' |
				  'DELETE' | 'BATCH_PARTIAL_UPDATE' | 'BATCH_DELETE' |
				  'GET_ALL' | 'OPTIONS';
httpExtraOp		: 'HEAD' | 'POST' | 'PUT' | 'TRACE' | 'CONNECT';
complex 			: complexOp '-' ( Name | '*' );
complexOp   		: 'FINDER' | 'ACTION';
Name 			: [a-zA-Z0-9]+;
```

Examples:
```
*.*/*.*                fallback configuration
*.*/*.GET              configuration for all outgoing GET requests
*.*/assets:media.GET   configuration for all outgoing GET requests to assets/media sub-resource
*.*/assets.GET         configuration for all outgoing GET requests to all assets resource
                       and all it's sub-resources
profileView.*/*.*      configuration for all downstream requests if 'profileView' resource was called
```

The format consists of fixed number of parts, is explicit and resembles familiar file-path structure to make it easier for humans to understand and manipulate.

Each key is assigned a priority and key with highest priority is used at runtime. General principle behind priorities is that more specific key should have higher priority than less specific one. More formally, the following rules apply:
* resource name is more specific than operation type
* outbound resource is more specific than inbound resource

What follows is that each part of the key can be assigned a priority score where higher priority means it is more specific:

```
<2>.<0>/<3>.<1>
```

It means that outbound resource name is most specific part of the key and operation type of inbound resource is least specific.

Defining priorities this way makes them unambiguous - there is a deterministic order for all applicable keys for every request. In other words, the decision which key will be used is structurally deterministic and does not depend on order of the keys in configuration source.

In examples below, keys are sorted by their priority (highest priority - most specific ones are on top):

```
profileView.*/profile.FINDER-firstDegree
*.*/profile.GET
profileView.*/*.*
*.*/*.GET
*.*/*.*
```

ParSeq Batching
==========================

Often, especially when IO is involved, it is more efficient to perform operations in batches rather than individually. This is the reason why many APIs provide a "batch" version of an operation e.g. [BATCH_GET](https://github.com/linkedin/rest.li/wiki/Rest.li-User-Guide#batch_get) in [Rest.li](http://rest.li/) framework. Typically for optimal efficiency everything that can be batched should be batched.

Unfortunately batching things together may be difficult because instead of working with a single item we need to think about all other places where similar items are used and somehow combine all usages to leverage batching. This breaks modularity, adds complexity and leads to a tradeoff between efficiency and simplicity.

ParSeq Batching provides a mechanism through which asynchronous operations are automatically batched. It can be used to implement efficient "batching clients" where "client" means on object that given ```K key``` provides a task that returns ```T value```.

Example
=======

We have two methods that return tasks returning a Person and Company object given their id:

```java
public Task<Person> fetchPerson(int id) { /* ... */ }
public Task<Company> fetchCompany(int id) { /* ... */ }
```

We would like to write a method that given a person id will return a short description e.g. "John Smith working at LinkedIn". With ParSeq we would write the following code:

```java
// create extended summary for a person: "<first name> <last name> working at <company name>"
Task<String> createExtendedSummary(int id) {
  return fetchPerson(id)
      .flatMap("createExtendedSummary", this::createExtendedSummary);
}

Task<String> createExtendedSummary(final Person p) {
  return fetchCompany(p.getCompanyId())
      .map("summary", company -> shortSummary(p) + " working at " + company.getName());
}

String shortSummary(Person p) {
  return p.getFirstName() + " " + p.getLastName();
}
```

Running ```createExtendedSummary(1)``` task and visualizing it using [ParSeq tracing](https://github.com/linkedin/parseq/wiki/Tracing) will generate the following diagram:

![createExtendedSummary.png](images/createExtendedSummary.png)

Now suppose that we need to create a summary for two Persons. The most obvious solution would be to write:

```java
Task.par(createExtendedSummary(1), createExtendedSummary(2));
```

Diagram representing execution of above code:

![createExtendedSummaryPar2.png](images/createExtendedSummaryPar2.png)

We have four individual fetch operations. If there was a batch fetch available for Person and Company then we would be able to implement batching-aware method that would leverage batch API. We would not be able to simply reuse existing code. With ParSeq Batching an execution of above code would generate the following trace:

![createExtendedSummaryPar2Batching.png](images/createExtendedSummaryPar2Batching.png)

Notice that descriptions of fetching tasks have been prefixed with "batch:". This is a hint that those tasks participated in batched operations. In order to see details select "System hidden" option in Trace Viewer:

![createExtendedSummaryPar2BatchingSystemHidden.png](images/createExtendedSummaryPar2BatchingSystemHidden.png)

Only two fetch operation were executed. First operation fetched Persons with ids 1 and 2. Task with description "batch(2)" represents an actual operation. Since both Persons have a reference to Company with Id 1 they have been de-duplicated and in effect single fetch Company operation have been executed. This is represented by task with description "batch(1)".

How to use ParSeq Batching
==========================

In order to use ParSeq Batching we need to set ```BatchingSupport``` as a ```PlanDeactivationListener``` to the ```Engine```:

```java
final BatchingSupport _batchingSupport = new BatchingSupport();
engineBuilder.setPlanDeactivationListener(_batchingSupport);
```

To integrate an asynchronous API with ParSeq Batching we need to implement an instance of a ```BatchingStrategy``` and register it with the ```BatchingSupport``` (we will cover implementation of ```BatchingStrategy``` in next section):

```java
MyBatchingStrategy myBatchingStrategy = new MyBatchingStrategy();
_batchingSupport.registerStrategy(myBatchingStrategy);
```

BatchingStrategy
================

```BatchingStrategy``` allows building "batching clients" where "client" means an object that given ```K key``` provides a task that returns ```T value```. ```BatchingStrategy``` defines which keys can be grouped together into batches and how batches are executed.

```BatchingStrategy``` class has 3 type parameters:
* ```<G>``` Type of a Group,
* ```<K>``` Type of a Key,
* ```<T>``` Type of a Value,

Actual types will depend on specific use case.

```BatchingStrategy``` class declares 2 abstract methods:
* ```G classify(K key)``` - specifies what keys will be grouped together to form a batch,
* ```void executeBatch(G group, Batch<K, T> batch)``` - executes batch and must ensure that all ```Promise``` contained in a given ```Batch``` eventually will be completed

```BatchingStrategy``` has one more method worth mentioning: ```String getBatchName(G group, Batch<K, T> batch)```. It allows to provide a description for a task that executes a batch. By default it is equal to ```"batch(" + batch.size() + ")"```.

Example
=======

Assuming that we have an async API for fetching a Person by id we will create a ParSeq client that will perform batching automatically:
```java
public interface AsyncPersonClient {
  CompletableFuture<Person> get(Long id);
  CompletableFuture<Map<Long, Person>> batchGet(Collection<Long> ids);
}
```
For simplicity we will assume that all individual ```get``` operations can be grouped together. In this example we assume that async client is using Java ```CompletableFuture``` but our code would look very similar if we had to deal with other async mechanisms e.g. callbacks.


```ParSeqPersonClient``` will use ```AsynPersonClient``` internally and will implement ```SimpleBatchingStrategy```:
```java
public class ParSeqPersonClient extends SimpleBatchingStrategy<Long, Person> {
  private final AsyncPersonClient _client;
  public ParSeqPersonClient(AsyncPersonClient client) {
    _client = client;
  }
  // ...
}
```

Since we can group all individual ```get``` into one batch we used ```SimpleBatchingStrategy```. If we had to create multiple batches then we would extend more general ```BatchingStrategy``` that would allow us to declare ```classify``` function that would determine how many batches are created. ```SimpleBatchingStrategy``` class declare a trivial ```classify``` function that groups all keys into one group.

To execute batch we call async ```batchGet``` method and complete ParSeq promises once result is known. All promises belonging to the batch have to be resolved with either successful result or a failure. Leaving any of the promises unresolved may lead to plan that remains uncompleted forever.
```java
  @Override
  public void executeBatch(Batch<Long, Person> batch) {
    _client.batchGet(batch.keys()).whenComplete((results, exception) -> {
      if (exception != null) {
        // batch operation failed so we need to fail all promises
        batch.failAll(exception);
      } else {
        // complete promises with values from results
        batch.foreach((key, promise) -> promise.done(results.get(key)));
      }
    });
  }
```

Finally we need to define main API for our ```ParSeqPersonClient```:
```java
  public Task<Person> get(Long id) {
    return batchable("fetch Person " + id, id);
  }
```
```batchable()``` method is declared by a ```BatchingStrategy``` and returns a task that cooperates with a batching strategy to performa a batchable operation.

Source code for above example can be found [here](https://github.com/linkedin/parseq/blob/master/subprojects/parseq-examples/src/main/java/com/linkedin/parseq/example/domain/ParSeqPersonClient.java).

Task-based BatchingStrategy
===========================

```BatchingStrategy``` API is intended to be used when integrating asynchronous API (e.g. based on callbacks or ```CompletableFuture``` ) with parseq. It is not convenient to use when we have an existing parseq API. In those cases we can use ```TaskBatchingStrategy```.

```TaskBatchingStrategy``` class has 3 type parameters:
* ```<G>``` Type of a Group,
* ```<K>``` Type of a Key,
* ```<T>``` Type of a Value,

Actual types will depend on specific use case.

```TaskBatchingStrategy``` class declares 2 abstract methods:
* ```G classify(K key)``` - specifies what keys will be grouped together to form a batch,
* ```Task<Map<K, Try<T>>> taskForBatch(G group, Set<K> keys)``` - returns a ```Task``` that given set of keys return a map containing successful result or a failure for every key.

```TaskBatchingStrategy``` has one more method worth mentioning: ```String getBatchName(G group, Set<K> key)```. It allows to provide a description for a task that executes a batch. By default it is equal to ```"batch(" + keys.size() + ")"```.

For a simple case when all keys can always be grouped into a batch there exists a ```SimpleTaskBatchingStrategy``` that requires only one method to be declared: ```Task<Map<K, Try<T>>> taskForBatch(Set<K> keys)```.
ParSeq Trace Visualization Server
==========================

This project includes a trace visualization server for
[https://github.com/linkedin/parseq](ParSeq) traces.


Building
========

To build the trace visualization server, use `./gradlew build`. This creates a runnable jar file under `build/libs/parseq-tracevis-server-jar-with-dependencies.jar`.


Downloading
===========

You can download latest version of `parseq-tracevis-server-jar-with-dependencies.jar` from [maven central repository](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.linkedin.parseq%22%20AND%20a%3A%22parseq-tracevis-server%22).


Running the Trace Visualization Server
======================================

First install [graphviz](http://www.graphviz.org/) e.g. on mac you might run `brew install graphviz`.

Find path to a `dot` executable. `dot` is part of graphviz installation e.g. `which dot`.

Run server passing path to `dot` as an argument e.g. `java -jar parseq-tracevis-server-jar-with-dependencies.jar /usr/bin/dot`.

(Alternative) After graphviz installation, just run `./gradlew runTracevisServer`

You can optionally specify port number, by default it will run on port 8080.


Docker
======================================

To start tracevis server using docker: `docker run -d -p 8080:8080 jodzga/parseq-tracevis-server:latest`. The server is accessible at [http://localhost:8080](http://localhost:8080).

More Info
=========

For more information, see the [ParSeq trace wiki](https://github.com/linkedin/parseq/wiki/Tracing).


License
=======

This tool is licensed under the terms of the Apache License, Version 2.0.
ParSeq Trace Visualization
==========================

This project includes a trace visualizer for
[https://github.com/linkedin/parseq](ParSeq) traces.


Building
========

To build the trace visualizer, use `make dist`. This creates a package for the
trace visualizer at `dist/parseq-tracevis.tar.gz`.


Running the Trace Visualizer
============================

To run the trace visualizer, extract `parseq-tracevis.tar.gz` and open
index.html in a browser. The tool can also be hosted from a web server.

For coding / debugging, the trace visualizer can also be run from the directory
that hosts this README.

More Info
=========

For more information, see the [ParSeq trace wiki](https://github.com/linkedin/parseq/wiki/Tracing#wiki-trace-tools).

License
=======

This tool is licensed under the terms of the Apache License, Version 2.0.
Benchmarks are based on [Oracle Java Microbenchmark Harness](http://openjdk.java.net/projects/code-tools/jmh/).

### Results interpretation

Be cautious with conclusions based on microbenchmarking as there are plenty possible pitfalls for goals, test compositions, input data, an environment and the analyze itself.

### Command line launching

Execute all benchmark methods with 4 worker threads:

    ./gradlew clean build
    java -jar build/libs/benchmarks.jar  ".*" -t 4

or specify a filter for benchmark methods and the number of forks and warmup/measurements iterations, e.g.:

    java -jar build/libs/benchmarks.jar  -t 4  -f 3 -i 10 -wi 5  ".*IdGeneratorBenchmark.*"
    java -jar build/libs/benchmarks.jar  -t 4  -f 3 -i 10 -wi 5  ".*LongIdGeneratorBenchmark.*"

### Command line options

The whole list of command line options is available by:

    java -jar build/libs/benchmarks.jar -h
